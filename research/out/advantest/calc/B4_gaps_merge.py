#!/usr/bin/env python3
"""B4 gap log: merge every NOT DISCLOSED / NOT RETRIEVED item into out/advantest/gaps.md.

Usage (from the repo root):
    python3 -I research/out/advantest/calc/B4_gaps_merge.py            # dry run, prints the merge log
    python3 -I research/out/advantest/calc/B4_gaps_merge.py --write    # also writes out/advantest/gaps.md

Inputs (read only):
    out/advantest/parts/*_gaps.md   every gap line (the modules' gap logs)
    out/advantest/parts/*.md        exact-form occurrences inside module text, verify logs, XM and B3.md
    sources/advantest/_manifest.csv rows with status NOT RETRIEVED that no later RETRIEVED row superseded

Method:
    1. Extract every "NOT DISCLOSED (read: ...) - item" / "NOT RETRIEVED (tried: ...) - item" occurrence
       (balanced parentheses; in non-gaps files the item ends at a table-cell bar, a sentence break,
       the next gap phrase or the end of the line). "same documents as above" lists are resolved to the
       previous line's list of the same gaps file.
    2. Map each occurrence to a canonical gap with the MERGE table (regex on the item text; manifest rows
       by URL). Occurrences that no MERGE entry matches merge only on identical normalised item text.
       COVERED lists summary occurrences whose content is already split over several gap lines.
    3. For each gap keep the most precise list: the one with the most ';'-separated entries, then the most
       ','-separated parts, then the longest. A MERGE entry may give a union list instead, built only from
       the lists of the merged occurrences and the verify logs that re-read the same documents.
    4. Group under A1..A6, TH, CL/B, Sources (the group of the MERGE entry, else the first module that
       logged it; manifest-only rows go to Sources). Each gap line is exactly
       "<NOT DISCLOSED|NOT RETRIEVED> (<read|tried>: <list>) - <item>".
    5. Any "NOT DISCLOSED"/"NOT RETRIEVED" mention that is not in the exact form is printed for review.
    6. (fix round 1, 2026-11-21) Every line of a *_gaps.md file that starts with "NOT " must yield an occurrence;
       a line the parser cannot read (e.g. an unbalanced parenthesis in its read list) stops the script instead of
       being dropped silently. A gap is merged only with gaps of the same form (DISCLOSED or RETRIEVED): match_key
       compares forms and the build step raises on any form conflict. Each output item gets calendar months
       after every fiscal label that lacks them (label_months).
    7. (fix round 2, 2026-11-21) Each bare quarter-end date in an item gets its fiscal label, e.g. '30 Sep 2026 (FY2026 Q2 end)'
       (label_dates).
This script reads only our own parts files and the manifest, never a downloaded document.
"""
import csv, glob, os, re, sys
from collections import OrderedDict

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)                                   # research/out/advantest
RESEARCH = os.path.dirname(os.path.dirname(OUT))              # research
PARTS = os.path.join(OUT, "parts")
MANIFEST = os.path.join(RESEARCH, "sources", "advantest", "_manifest.csv")
DEST = os.path.join(OUT, "gaps.md")
GROUPS = ["A1", "A2", "A3", "A4", "A5", "A6", "TH", "CL/B", "Sources"]
OPEN = re.compile(r"NOT (DISCLOSED|RETRIEVED) \((read|tried): ")
NEXT = re.compile(r";?\s*NOT (?:DISCLOSED|RETRIEVED) \(")
ANY = re.compile(r"NOT (?:DISCLOSED|RETRIEVED)")


def module_of(fname):
    m = re.split(r"[_.]", fname)[0]
    if m in ("A1", "A2", "A3", "A4", "A5", "A6", "TH"):
        return m
    if m in ("CL", "B1", "B2", "B3", "B4", "B5"):
        return "CL/B"
    return "XM"


def norm(s):
    s = s.replace("’", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip()


def key_text(s):
    return re.sub(r"[^a-z0-9]+", " ", norm(s).lower()).strip()


def url_key(u):
    return re.sub(r"^https?://", "", u.strip()).rstrip("/").lower()


def precision(lst):
    return (len([x for x in lst.split(";") if x.strip()]), len(re.split(r"[;,]", lst)), len(lst))


def extract(text, whole_line):
    """Yield (form, verb, list, item, line_no) for every exact-form occurrence in text."""
    for n, line in enumerate(text.splitlines(), 1):
        for m in OPEN.finditer(line):
            depth, i = 1, m.end()
            while i < len(line) and depth:
                depth += {"(": 1, ")": -1}.get(line[i], 0)
                i += 1
            if depth:
                continue
            lst, rest = line[m.end():i - 1], line[i:]
            if not rest.startswith(" - "):
                continue
            item = NEXT.split(rest[3:])[0]
            if not whole_line:
                item = item.split(" |")[0]
                item = re.split(r"(?<=[a-z0-9)\"'])\.\s+(?=[A-Z\[])", item)[0]
            yield m.group(1), m.group(2), norm(lst), norm(item).rstrip(".;, ").strip(), n


# ---- calendar months for fiscal labels in gap items (fix round 1, 2026-11-21) ----
MON = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
MONRE = "|".join(MON)


def _span(y, q0, q1):
    """calendar span of fiscal quarters q0..q1 (1-4) of fiscal year y (FY named by start year, April start)."""
    s = 3 + 3 * (q0 - 1); e = 3 + 3 * q1 - 1
    ys, ye = y + s // 12, y + e // 12
    ms, me = MON[s % 12], MON[e % 12]
    return f"{ms}-{me} {ye}" if ys == ye else f"{ms} {ys}-{me} {ye}"


LAB = re.compile(
    r"(?P<q12>Q1 and Q2 FY(?P<q12y>\d{4}))"
    r"|(?P<qand>FY(?P<qandy>\d{4}) Q(?P<qa>[1-4]) and Q(?P<qb>[1-4]))"
    r"|(?P<qrng>FY(?P<r1y>\d{4}) Q(?P<r1q>[1-4]) to FY(?P<r2y>\d{4}) Q(?P<r2q>[1-4]))"
    r"|(?P<yrng>FY(?P<y1>\d{4})-(?:FY)?(?P<y2>\d{4}|\d{2})\b)"
    r"|(?P<half>(?P<hk>1H|2H) FY(?P<hy>\d{4})|FY(?P<hy2>\d{4}) (?P<hk2>1H|2H))"
    r"|(?P<qf>Q(?P<qfq>[1-4]) FY(?P<qfy>\d{4}))"
    r"|(?P<fq>FY(?P<fqy>\d{4}) Q(?P<fqq>[1-4]))"
    r"|(?P<fy>FY(?P<fyy>\d{4}))\b")


def _months(m):
    g = m.groupdict()
    if g["q12"]:
        y = int(g["q12y"]); return f"{_span(y, 1, 1)} and {_span(y, 2, 2)}"
    if g["qand"]:
        y = int(g["qandy"]); return f"{_span(y, int(g['qa']), int(g['qa']))} and {_span(y, int(g['qb']), int(g['qb']))}"
    if g["qrng"]:
        y1, q1, y2, q2 = int(g["r1y"]), int(g["r1q"]), int(g["r2y"]), int(g["r2q"])
        s = _span(y1, q1, q1).split("-")[0].strip(); e = _span(y2, q2, q2)
        sm = s.split()[0]; sy = y1 + (3 + 3 * (q1 - 1)) // 12
        em, ey = e.split("-")[1].split()[0] if " " in e.split("-")[1] else e.split("-")[1], e.split()[-1]
        return f"{sm} {sy}-{em} {ey}"
    if g["yrng"]:
        y1 = int(g["y1"]); y2 = g["y2"]; y2 = int(y2) if len(y2) == 4 else int(str(y1)[:2] + y2)
        return f"Apr {y1}-Mar {y2 + 1}"
    if g["half"]:
        k = g["hk"] or g["hk2"]; y = int(g["hy"] or g["hy2"])
        return _span(y, 1, 2) if k == "1H" else _span(y, 3, 4)
    if g["qf"]:
        y, q = int(g["qfy"]), int(g["qfq"]); return _span(y, q, q)
    if g["fq"]:
        y, q = int(g["fqy"]), int(g["fqq"]); return _span(y, q, q)
    y = int(g["fyy"]); return f"Apr {y}-Mar {y + 1}"


def label_months(item):
    """Add calendar months after each fiscal label in a gap item that does not already carry them."""
    out, pos, done = [], 0, set()
    for m in LAB.finditer(item):
        lab = m.group(0)
        after = item[m.end():m.end() + 40]
        already = re.match(rf"\s*(?:\(|,|;)\s*(?:\d{{1,2}} )?(?:{MONRE})\b", after) or re.match(rf"\s*\((?:[^()]*?)(?:{MONRE}) \d{{4}}", after[:30])
        if re.match(r"\s*end\b", after):        # "FY2025 end" names a date, given next to it
            continue
        if already or lab in done:
            done.add(lab)
            continue
        if re.search(rf"\b{re.escape(lab)}\s*\((?:\d{{1,2}} )?(?:{MONRE})", item):
            done.add(lab); continue   # labelled elsewhere in the same item
        done.add(lab)
        mon = _months(m)
        out.append(item[pos:m.end()])
        before = item[:m.start()]
        if before.endswith("(") and after.startswith(")"):
            out.append(f", {mon}")                      # "(FY2025)" -> "(FY2025, Apr 2025-Mar 2026)"
            pos = m.end()
        elif after.startswith(" ("):
            out.append(f" ({mon}; ")                    # "FY2025 (only ...)" -> "FY2025 (Apr 2025-Mar 2026; only ...)"
            pos = m.end() + 2
        else:
            out.append(f" ({mon})")
            pos = m.end()
    out.append(item[pos:])
    return "".join(out)


# ---- fiscal labels for bare quarter-end dates in gap items (fix round 2, 2026-11-21) ----
QEND = re.compile(r"\b(30 Jun|30 Sep|31 Dec|31 Mar) (20\d\d)\b")


def label_dates(item):
    """Add '(FYyyyy Qn end)' / '(FYyyyy end)' after each quarter-end date in a gap item that lacks a fiscal label."""
    out, pos = [], 0
    for m in QEND.finditer(item):
        after = item[m.end():m.end() + 12]
        if re.match(r"\s*[(,;]\s*FY\d{4}", after) or re.match(r"\s*\(\s*FY", after):
            continue
        dm, y = m.group(1), int(m.group(2))
        lab = {"30 Jun": f"FY{y} Q1 end", "30 Sep": f"FY{y} Q2 end", "31 Dec": f"FY{y} Q3 end", "31 Mar": f"FY{y - 1} end"}[dm]
        out.append(item[pos:m.end()] + f" ({lab})")
        pos = m.end()
    out.append(item[pos:])
    return "".join(out)


# ---------------------------------------------------------------------------------------------------
# MERGE table. key -> dict(group, form, item (canonical wording or None = first *_gaps.md wording),
#   pat (regex list on item text), url (regex list on the tried-list / manifest URL), lst (union list or None))
# ---------------------------------------------------------------------------------------------------
MERGE = OrderedDict()


def M(key, group, form, pat=(), url=(), item=None, lst=None):
    MERGE[key] = dict(group=group, form=form, pat=[re.compile(p, re.I) for p in pat],
                      url=[re.compile(u, re.I) for u in url], item=item, lst=lst)


D, R = "DISCLOSED", "RETRIEVED"
M("ai_share", "A1", D, [r"^share of Advantest revenue tied to AI", r"^AI/HPC share of revenue", r"^AI, HBM or advanced-packaging share"],
  item='share of Advantest revenue tied to AI / HPC (the company gives only the "Computing / Communications" share of SoC tester sales, rounded to the nearest 5%, which also includes smartphone application processors, and says it does not disclose further; HBM and advanced packaging are logged separately below)')
M("hbm_share", "A1", D, [r"^share of revenue from HBM testing", r"^HBM tester sales or HBM share", r"^Advantest's HBM-specific tester share"],
  item="HBM tester sales, HBM share of memory tester sales or of revenue, and an HBM-specific tester market share (HBM is named only qualitatively within high-performance DRAM; memory tester sales are split only into DRAM and non-volatile, rounded to 5%)",
  lst="Q2 FY26 / Q1 FY26 / FY25 / Q3 FY25 earnings-briefing slides and notes, incl. the memory-tester application table on Q2 FY26 slide 16 and the FY2025 Tester Market Share Report; Investors' Guide Oct 2026 p.7; Q&A summaries FY2023 Q4 to FY2026 Q2; Integrated Annual Report 2026 full text; Annual Securities Report 84th and Semi-Annual Securities Report 85th, business overview and Note 22 Revenue")
M("ap_share", "A1", D, [r"^share of revenue tied to advanced packaging", r"^revenue from advanced packaging"],
  item="revenue or share of revenue tied to advanced packaging, including die-level / known-good-die or known-good-stack test",
  lst="Q2 FY26 / Q1 FY26 / FY25 / Q3 FY25 earnings-briefing slides and notes; Q&A summaries FY2024 Q3 to FY2026 Q2; MTP3 slides; Integrated Annual Report 2026 full text; Investors' Guide Oct 2026 Ch.1; Annual Securities Report 84th and Semi-Annual Securities Report 85th, business overview and Note 22 Revenue")
M("cc_split", "A1", D, [r'^split of "Computing / Communications"', r"^split of SoC tester sales between GPUs"],
  item='split of "Computing / Communications" SoC tester sales between HPC/AI and smartphone application processors, and of SoC tester sales between GPU, custom ASIC and CPU customers',
  lst="Q2 FY26 slide 15; Investors' Guide Oct 2026 p.5; FY2025 Q1 Q&A summary A6; Q3 FY2025 Q&A summary A4")
M("recurring", "A1", D, [r"^recurring revenue amount"])
M("adj_gm", "A1", D, [r"company-adjusted (\(non-IFRS\) )?gross margin"])
M("q4_sga", "A1", D, [r"FY2025 Q4 one-off SG&A", r'one-off expenses related to business operations" in FY2025 Q4'])
M("reversal", "A1", D, [r"inventory write-down reversal", r"reversal of inventory (write-down|obsolescence)", r"whether any (part )?of the reversal fell in FY2026 Q2"],
  item="amount of the reversal of inventory write-down / obsolescence that management named for FY2026 Q1 (Apr-Jun 2026) and for 1H FY2026 (Apr-Sep 2026), the line it was booked in, and whether any part fell in FY2026 Q2 (Jul-Sep 2026); margins without it cannot be computed for FY2026 Q1, Q2, 1H and the LTM",
  lst="Q1 FY2026 briefing notes p.5 and Q&A summary A9; Q2 FY2026 briefing notes and Q&A summary A5; Q1 and Q2 FY2026 briefing slides; FY2026 Q1 and Q2 Consolidated Financial Results (tanshin); Semi-Annual Securities Report 85th, notes 1-13 (no inventories note); Integrated Annual Report 2026; IR Fireside Chat script and Q&A 2026-11-12")
M("tax_oneoffs", "A1", D, [r"^tax effect of the named"],
  item="tax effect of the named one-off items (impairment, divestiture gain, call-option gain, valuation gains), so net income and the total return ratio cannot be shown without them",
  lst="FY2025 tanshin notes; Annual Securities Report 84th, Note 15(3) tax-rate reconciliation p.146 and MD&A p.50; FY2026 Q1 and Q2 tanshin; Semi-Annual Securities Report 85th")
M("q2_charge", "A1", D, [r"one.time (SG&A )?charge related to a growth investment"])
M("purchase_commit", "A2", D, [r"^purchase commitments"],
  item="purchase commitments / purchase obligations for materials and components (amount and maturity); capex commitments are the only commitments quantified",
  lst="annual securities report 84th, notes 9, 11, 13, 16, 22 and 30, business risks p.42; full-text search for 'commitment' and 'purchase obligation'")
M("e_biz_220728", "A2", R, url=[r"E_BIZ_220728_QA"])
M("q1q3_guid", "A3", D, [r"^Q1 or Q3 single-quarter (guidance|forecast)"])
M("tax_fy23", "A3", D, [r"after-tax effect of the FY2023 Q4 goodwill impairment"])
M("tax_fy24", "A3", D, [r"exact after-tax effect of the FY2024 Q4 impairment"])
M("mtp3_status", "A3", D, [r"^company-computed MTP3 three-year average status"])
M("semi_basis", "A4", D, [r'basis (\(ship-to or customer location\) )?of the semi-annual "main regions" table'])
M("orders_restate", "A4", D, [r"^orders received and backlog, so the (requested )?orders restatement"])
M("meti", "A4", R, [r"^METI originals"])
M("china19", "A4", D, [r'^period and basis.*"approximately 19%"'])
M("asia_split", "A4", D, [r"^Taiwan, China and South Korea split of Asia"])
M("corp_adj", "A4", D, [r"explanation of the change in the (\"Elimination and Corporate\"|Corporate) adjustment"])
M("bis_faq", "A4", R, [r"^BIS FAQ II\.A\.1"], url=[r"bis\.doc\.gov/index\.php/documents/product-guidance/3211"],
  lst="https://www.bis.doc.gov/index.php/documents/product-guidance/3211-2023-1-25-updated-faqs-for-oct-7-advanced-computing-and-semiconductor-manufacturing-equipment-rule/file (URL cited in 88 FR 73424 p.7) - one attempt 2026-11-21, the response was an HTML page, not the PDF; no BIS advisory opinions searched")
M("cb_02", "A5", R, url=[r"^https://www\.advantest\.com/document/en/investors/aad/E_Info_20260401_02\.pdf - HTTP"])
M("cb_03", "A5", R, url=[r"^https://www\.advantest\.com/document/en/investors/aad/E_Info_20260401_03\.pdf - HTTP"])
M("cb_04", "A5", R, url=[r"^https://www\.advantest\.com/document/en/investors/aad/E_Info_20260401_04\.pdf - HTTP"])
M("covenants", "A5", D, [r"^financial covenants on loans"])
M("ye_div", "A5", D, [r"^FY2026 year-end dividend (forecast|per share)"],
  item='FY2026 year-end dividend per share (printed as "TBD" in the interim dividend notice and "-" in the tanshin forecast row)')
M("fy2007", "A6", R, [r"^FY2006 (and FY2007 full-year results releases|net sales and operating income)"], url=[r"E_FR_FY2007_FN"])
M("ifrs15", "A6", D, [r"^effect of IFRS 15 on FY2018"])
M("ifrs16", "A6", D, [r"^effect of IFRS 16 on FY2019"])
M("tam_method", "TH", D, [r"^method behind the tester TAM"])
M("papers", "TH", R, [r"^peer-reviewed ITC / VTS / ECTC papers"])
M("pmc", "TH", R, [r"^Do et al\. 2026"], url=[r"PMC13609547"])
M("cap10k", "TH", D, [r"10,000.(system|SoC tester)"],
  item='committed date for 10,000 SoC tester systems a year and the scale and timing of the next step (only "roughly a year in advance" of end FY2028, Mar 2029; the company says the schedule is not final)')
M("lockup", "CL/B", R, [r"^lock-up terms of the April 2026 Zero Coupon CB offering"],
  item="lock-up terms of the April 2026 Zero Coupon CB offering (catalyst B3: lock-up expiry)")
M("calendar", "CL/B", D, [r"^dates of the FY2026 full-year results", r"^dates of the Q1 and Q2 FY2027 results",
                          r"^date of the FY2026 full-year results", r"^date of the 85th Ordinary General Meeting"],
  item="dates of the FY2026 full-year results, the Q1 and Q2 FY2027 results, the 85th Ordinary General Meeting and the FY2026 year-end dividend payment (no FY2027 calendar published; only the 15 May record date and 'within three months' are given)")
M("q3day", "CL/B", D, [r"^day of the Q3 FY2026 results announcement"])
M("ter_call", "CL/B", D, [r"^date of Teradyne's Q4 2026 earnings call"])
M("mtp4date", "CL/B", D, [r"^exact release date of the Fourth Mid-Term"])
M("facilities", "A5", D, [r"^expiry dates"])
M("bbg_0428", "CL/B", R, url=[r"bloomberg\.com/news/articles/2026-04-28"])
M("streetinsider", "CL/B", R, url=[r"streetinsider\.com"],
  item="UBS note on NVIDIA test dual-sourcing and its estimate of NVIDIA test spend through Advantest: test-sourcing content only (claim C2)")
M("bernstein", "CL/B", R, url=[r"tipranks\.com/news/the-fly/advantest-downgraded", r"investing\.com/news/analyst-ratings/bernstein"],
  item="Bernstein research note on Advantest: stated demand and margin arguments only (claim C1)")
M("xeno_ter", "CL/B", R, url=[r"xenospectrum\.com/en/teradyne-q3-2026"])
M("xeno_china", "CL/B", R, url=[r"xenospectrum\.com/en/china-memory"])
M("zacks", "CL/B", R, url=[r"nasdaq\.com/articles/ter-rides"])

# Summary occurrences whose content is already logged as separate, more specific gap lines.
COVERED = [
    (re.compile(r"^customers above 10% of net sales for any half-year or quarter$", re.I),
     "split over the three A4 lines for 1H FY2026, 1H FY2025 and single quarters"),
]


def resolve_relative(cands):
    prev = {}
    for c in cands:
        if c["gapsfile"]:
            if c["lst"].lower().startswith("same documents as above") and c["src"] in prev:
                tail = c["lst"][len("same documents as above"):].lstrip(" ,")
                c["lst"] = prev[c["src"]] + (", " + tail if tail else "")
            prev[c["src"]] = c["lst"]
    return cands


def collect():
    cands, prose = [], []
    for f in sorted(glob.glob(os.path.join(PARTS, "*.md"))):
        name = os.path.basename(f)
        txt = open(f, encoding="utf-8").read()
        found = 0
        got_lines = set()
        for form, verb, lst, item, n in extract(txt, whole_line=name.endswith("_gaps.md")):
            found += 1
            got_lines.add(n)
            cands.append(dict(src=name, line=n, module=module_of(name), gapsfile=name.endswith("_gaps.md"),
                              form=form, verb=verb, lst=lst, item=item, manifest=False))
        if name.endswith("_gaps.md"):
            lost = [n for n, line in enumerate(txt.splitlines(), 1) if line.startswith("NOT ") and n not in got_lines]
            if lost:
                raise SystemExit(f"{name}: gap line(s) {lost} could not be parsed (check the parentheses of the read/tried list)")
        for n, line in enumerate(txt.splitlines(), 1):
            for m in ANY.finditer(line):
                if not OPEN.match(line, m.start()):
                    prose.append((name, n, norm(line[max(0, m.start() - 60):m.end() + 40])))
    return resolve_relative(cands), prose


def manifest_rows():
    rows = list(csv.DictReader(open(MANIFEST, encoding="utf-8")))
    got = [r for r in rows if r["status"] == "RETRIEVED"]

    def stem(p):
        return os.path.splitext(os.path.basename(p))[0]

    def code(r):
        m = re.search(r"(FR-\d{4}-\d+|E_BIZ_\d+_QA|E_FR_FY\d+_FN)", r["local_file"] + " " + r["url"])
        return m.group(1) if m else None

    out, seen = [], set()
    for r in rows:
        if r["status"] != "NOT RETRIEVED" or (r["url"], r["local_file"]) in seen:
            continue
        seen.add((r["url"], r["local_file"]))
        sup = [g["local_file"] for g in got if g["url"] == r["url"] or stem(g["local_file"]) == stem(r["local_file"])
               or (code(r) and code(g) == code(r))]
        if not sup and "teradyne-reports-third-quarter-2026-results" in r["url"]:
            sup = [g["local_file"] for g in got if "teradyne_press-release-Q3-2026-results" in g["local_file"]]
        out.append((r, sup))
    return out


def match_key(c):
    for k, e in MERGE.items():
        if e["form"] != c["form"]:
            continue
        if any(p.search(c["item"]) for p in e["pat"]):
            return k
        if any(u.search(c["lst"]) for u in e["url"]):
            return k
    return None


def main():
    write = "--write" in sys.argv
    cands, prose = collect()
    log = [f"exact-form occurrences in parts/*.md: {len(cands)} "
           f"({sum(c['gapsfile'] for c in cands)} in *_gaps.md files)"]

    # manifest rows
    man_open, man_sup = [], []
    for r, sup in manifest_rows():
        (man_sup if sup else man_open).append((r, sup))
    log.append(f"manifest NOT RETRIEVED rows: {len(man_open) + len(man_sup)} "
               f"({len(man_sup)} superseded by a later RETRIEVED file, {len(man_open)} open)")
    for r, sup in man_sup:
        log.append(f"  superseded: {r['url']} -> {os.path.basename(sup[0])}")
    all_lists = " || ".join(url_key(x) for c in cands for x in re.findall(r"https?://\S+", c["lst"]))
    for r, _ in man_open:
        lst = f"{r['url']} - HTTP {r['http_code']}"
        if r["http_code"] == "200":
            lst += " but " + norm(r["note"]).split(" | ")[-1]
        lst += " to scripted request, not retried (manifest row)"
        c = dict(src="_manifest.csv", line=0, module="Sources", gapsfile=False, form="RETRIEVED", verb="tried",
                 lst=lst, item=f"{r['issuer']} {r['doctype']} ({r['date']})", manifest=True, url=r["url"])
        k = match_key(c)
        if k is None and url_key(r["url"]) in all_lists:
            k = "url:" + url_key(r["url"])
        c["key"] = k
        cands.append(c)
        log.append(f"  open: {r['url']} -> {'merged into ' + k if k else 'own line (Sources)'}")

    # assign keys
    for c in cands:
        if c.get("manifest"):
            continue
        cov = [why for p, why in COVERED if p.search(c["item"])]
        if cov:
            c["key"] = "COVERED"
            log.append(f"  covered: {c['src']}:{c['line']} {c['item'][:80]} ({cov[0]})")
            continue
        c["key"] = match_key(c) or ("txt:" + key_text(c["item"]))

    # manifest rows merged by URL into the module line that carries the same URL
    for c in cands:
        if c.get("manifest") and c["key"] and c["key"].startswith("url:"):
            u = c["key"][4:]
            host = [d for d in cands if not d.get("manifest") and u in " ".join(url_key(x) for x in re.findall(r"https?://\S+", d["lst"]))]
            c["key"] = host[0]["key"] if host else None
    for c in cands:
        if c.get("manifest") and c["key"] is None:
            c["key"] = "man:" + url_key(c["url"])

    # build gaps; order: each module's own *_gaps.md lines first (in file order), then md-only items
    order = {g: i for i, g in enumerate(GROUPS + ["XM"])}
    cands.sort(key=lambda c: (0 if c["gapsfile"] else (2 if c.get("manifest") else 1),
                              order.get(c["module"], 99), c["src"], c["line"]))
    gaps = OrderedDict()
    for c in cands:
        if c["key"] == "COVERED":
            continue
        gaps.setdefault(c["key"], []).append(c)
    lines = {g: [] for g in GROUPS}
    merged_log = []
    for k, cs in gaps.items():
        forms = {c["form"] for c in cs}
        if len(forms) > 1:
            raise SystemExit(f"form conflict in {k}: {[(c['src'], c['form']) for c in cs]}")
        form = cs[0]["form"]
        verb = "read" if form == "DISCLOSED" else "tried"
        e = MERGE.get(k, {})
        mods = [g for g in GROUPS if any(c["module"] == g for c in cs)]
        group = e.get("group") or (mods[0] if mods else "Sources")
        gfirst = [c for c in cs if c["gapsfile"]]
        item = e.get("item") or (gfirst[0]["item"] if gfirst else cs[0]["item"])
        if k.startswith("man:"):
            r = cs[0]
            item = {"investors.teradyne.com/news-releases":
                    "Teradyne IR news-releases index page (the Q3 2026 results release itself was saved from "
                    "investors.teradyne.com/news-events/press-releases/detail/455/teradyne-reports-third-quarter-2026-results)"
                    }.get(url_key(r["url"]), r["item"])
        own = [c["lst"] for c in cs if not c.get("manifest")] or [c["lst"] for c in cs]
        lst = e.get("lst") or max(own, key=precision)
        srcs = sorted({c["module"] if c["module"] != "Sources" else "manifest" for c in cs},
                      key=lambda m: (GROUPS + ["manifest", "XM"]).index(m) if m in GROUPS + ["manifest", "XM"] else 99)
        tail = f" (logged in: {', '.join(srcs)})" if len(srcs) > 1 else ""
        item = label_dates(label_months(item))
        line = f"NOT {form} ({verb}: {lst}) - {item}{tail}"
        lines[group].append(line)
        if len(cs) > 1:
            merged_log.append(f"  {k}: {len(cs)} occurrences from {', '.join(sorted({c['src'] for c in cs}))} -> {group}")

    # checks
    total = sum(len(v) for v in lines.values())
    bad = [l for v in lines.values() for l in v
           if not re.match(r"^NOT (DISCLOSED \(read: |RETRIEVED \(tried: ).+\) - \S", l)]
    verdict = [l for v in lines.values() for l in v if re.search(r"\b(validat\w*|refut\w*|confirm\w*|prove[sdn]?|proving)\b", l, re.I)]
    log.append(f"merged gaps: {len(merged_log)} keys had more than one occurrence")
    log += merged_log
    log.append("gap lines per group: " + ", ".join(f"{g} {len(lines[g])}" for g in GROUPS) + f"; total {total}")
    log.append(f"form check: {len(bad)} lines not in the exact form; verdict-word check: {len(verdict)} lines")
    log.append(f"mentions not in the exact form (reviewed by hand; each refers to a logged gap): {len(prose)}")
    for p in prose:
        log.append(f"  {p[0]}:{p[1]} ... {p[2]}")
    print("\n".join(log))

    if write:
        with open(DEST, "w", encoding="utf-8") as fh:
            fh.write(HEADER)
            for g in GROUPS:
                fh.write(f"\n## {g}\n\n")
                for l in lines[g]:
                    fh.write(l + "\n\n")
        print(f"wrote {DEST}")


HEADER = """# Gaps - Advantest

Advantest Corporation, TSE Prime 6857. The fiscal year ends 31 March and is named by its start year (FY2026 = Apr 2026-Mar 2027). Every NOT DISCLOSED and NOT RETRIEVED item from the module parts, their verify logs, B3 and the source manifest, one line each and deduplicated; merged lines say which modules logged them. Built by `calc/B4_gaps_merge.py` (log in `calc/B4_gaps_merge.out.txt`).

## Files the user can save by hand

These documents were refused to scripts, paywalled or not found by script. A person can open each in a browser and save it to `research/sources/advantest/` under the name shown (use the date printed in the document where the name says so).

- Advantest, Notice Regarding Issuance of Zero Coupon Convertible Bonds Due 2031 (1 Apr 2026): https://www.advantest.com/document/en/investors/aad/E_Info_20260401_02.pdf -> `2026-04-01_advantest_press-release-E-Info-20260401-02-CB-issuance.pdf` (CB early-redemption terms, lock-up)
- Advantest, Supplemental Materials regarding the CB issuance (1 Apr 2026): https://www.advantest.com/document/en/investors/aad/E_Info_20260401_03.pdf -> `2026-04-01_advantest_press-release-E-Info-20260401-03-CB-supplemental.pdf`
- Advantest, Notice on Determination of Terms of Issue of the CB (1 Apr 2026): https://www.advantest.com/document/en/investors/aad/E_Info_20260401_04.pdf -> `2026-04-01_advantest_press-release-E-Info-20260401-04-CB-terms.pdf` (lock-up terms)
- BIS, updated FAQs for the Oct 7 advanced computing and SME rule (25 Jan 2023), FAQ II.A.1 on the back-end exclusion: https://www.bis.doc.gov/index.php/documents/product-guidance/3211-2023-1-25-updated-faqs-for-oct-7-advanced-computing-and-semiconductor-manufacturing-equipment-rule/file -> `2023-01-25_bis_FAQ-Oct7-advanced-computing-SME-rule.pdf`
- METI originals of Japan's export-list amendment adding advanced semiconductor manufacturing equipment (in force 23 Jul 2023) and any later METI semiconductor list changes: URL not identified (meti.go.jp refused scripts; start from METI's security export control pages) -> `<printed date>_meti_export-control-list-amendment-SME.pdf`
- sec.gov (no contact User-Agent this run): Teradyne annual report 10-K for 2025, https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=TER&type=10-K -> `<filing date>_teradyne_annual-report-10-K-2025.htm`
- sec.gov: customer filings that may name Advantest as a supplier, NVIDIA 10-K https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=NVDA&type=10-K and TSMC 20-F https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=TSM&type=20-F -> `<filing date>_nvidia_annual-report-10-K.htm`, `<filing date>_tsmc_annual-report-20-F.htm`
- sec.gov: Advantest's own 20-F for FY2007 (Apr 2007-Mar 2008), which carries FY2006 comparatives (the issuer's site returns HTTP 404 for E_FR_FY2007_FN.pdf): https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=advantest&type=20-F -> `<filing date>_advantest_annual-report-20-F-FY2007.htm`
- Bloomberg, 28 Apr 2026 (subscription): https://www.bloomberg.com/news/articles/2026-04-28/advantest-shares-decline-after-outlook-misses-on-tight-capacity -> `2026-04-28_bloomberg_press-Advantest-outlook-capacity.html` (FY2026 outlook and tight capacity)
- Bloomberg, 28 Jan 2026 (subscription): https://www.bloomberg.com/news/articles/2026-01-28/advantest-rushes-to-boost-ai-chip-tester-capacity-to-meet-demand -> `2026-01-28_bloomberg_press-Advantest-boost-AI-chip-tester-capacity.html`
- StreetInsider, UBS note on NVIDIA test dual sourcing (test-sourcing content only): https://streetinsider.com/Basic+Content/Nvidia+test+slot+could+send+this+stock+soaring%2C+UBS+says/25021163.html -> `<printed date>_streetinsider_press-UBS-note-NVIDIA-test-sourcing.html`
- TipRanks / Investing.com, Bernstein research note on Advantest (stated demand and margin arguments only): https://www.tipranks.com/news/the-fly/advantest-downgraded-to-market-perform-from-outperform-at-bernstein and https://ng.investing.com/news/analyst-ratings/bernstein-cuts-advantest-stock-rating-to-market-perform-slashes-target-93CH-1828631 -> `<printed date>_tipranks_press-Bernstein-note-Advantest.html` (one of the two is enough)
- XenoSpectrum, Teradyne Q3 2026 revenue plateau: https://xenospectrum.com/en/teradyne-q3-2026-revenue-plateau/ -> `<printed date>_xenospectrum_press-Teradyne-Q3-2026-revenue-plateau.html`
- XenoSpectrum, China memory / HBM test equipment: https://xenospectrum.com/en/china-memory-testing-hbm-equipment/ -> `<printed date>_xenospectrum_press-China-memory-testing-HBM-equipment.html`
- Nasdaq (Zacks), Teradyne semiconductor test segment: https://www.nasdaq.com/articles/ter-rides-strong-semiconductor-test-segment-more-upside-ahead-0 -> `<printed date>_nasdaq-zacks_press-TER-semiconductor-test-segment.html`
- In Practise and Seeking Alpha (paywalled): https://inpractise.com/articles/advantest-vs-teradyne-gpu-test-market-share-and-power-supply-advantage and https://seekingalpha.com/article/4837312-advantest-teradyne-market-share-shifts-in-this-duopoly -> `<printed date>_inpractise_press-Advantest-vs-Teradyne-GPU-test-share.html`, `<printed date>_seekingalpha_press-Advantest-Teradyne-share-shifts.html`
- PMC / MDPI Micromachines, Do et al. 2026 HBM packaging review (the script got a reCAPTCHA page): https://pmc.ncbi.nlm.nih.gov/articles/PMC13609547/ -> `<printed date>_mdpi-micromachines_paper-HBM-thermal-reliability-hybrid-bonding-review.pdf`
- Samsung Newsroom (HTTP 403 to the script): any Samsung release on HBM4 hybrid bonding and its test steps, starting from https://news.samsung.com/global/?s=HBM4+hybrid+bonding -> `<printed date>_samsung_press-release-HBM4-hybrid-bonding.html`
- TDnet (Japanese filings): the public list (https://www.release.tdnet.info/inbs/I_main_00.html) covers only the last month; 28 Oct-21 Nov 2026 was read by script (no Advantest forecast revision, A3-322). Advantest's Japanese filings of Jan 2024-Mar 2025 are outside it; a person can look for forecast-revision notices of that period on Advantest's Japanese-language IR news pages and save any found -> `<filing date>_advantest_tdnet-<title>.pdf`
- Not saveable from a known URL: the FY2022 Q1 Q&A summary (E_BIZ_220728_QA.pdf) and the FY2007 results release (E_FR_FY2007_FN.pdf) return HTTP 404; FormFactor (investors.formfactor.com) and TSMC (investor.tsmc.com) refused scripts but no specific document was identified; IEEE Xplore papers are paywalled.
"""

if __name__ == "__main__":
    main()
