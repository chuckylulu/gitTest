#!/usr/bin/env python3
"""Checks on research/out/advantest/review_packet.md against evidence.csv and the source manifest (fix round 2, 2026-11-21).

1. Claims table: each row's id exists; its tag equals the evidence tag; its URL equals the evidence url; every page
   number in the Page cell appears among the page numbers of the evidence page_or_section; every number in the Value
   cell appears in the evidence value, claim or quote (commas ignored); the evidence period_fiscal label (or CY label)
   appears in the Period cell.
2. URLs: every full URL in the packet is a RETRIEVED row of sources/advantest/_manifest.csv; every bare file name
   cited with a page (e.g. "E_FR_FY2025_FN.pdf p.11") matches the last path part of a RETRIEVED manifest URL.
3. Inferences: every "[I] <confidence> (ids)" group cites [I] rows whose confidence equals the stated one, and the
   evidence value of each cited row (first number) appears in the paragraph.
4. Verdict words and valuation / price vocabulary: listed (the project rules allow verdict words only inside [I]).
5. Each fiscal label (FY2026 Q2, 1H FY2026, FY2025 ...) in the packet carries calendar months somewhere in its line.

Run from the repo root: python3 -I research/out/advantest/calc/RP_check.py
Exit code 1 if check 1, 2 or 3 finds a problem.
"""
import csv, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
OUT = os.path.join(ROOT, "research", "out", "advantest")
RP = os.path.join(OUT, "review_packet.md")
EV = os.path.join(OUT, "evidence.csv")
MAN = os.path.join(ROOT, "research", "sources", "advantest", "_manifest.csv")
MON = r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)"


def nums(s):
    return [x.replace(",", "") for x in re.findall(r"\d[\d,]*(?:\.\d+)?", s or "")]


def main():
    ev = {r["id"]: r for r in csv.DictReader(open(EV, encoding="utf-8"))}
    man = list(csv.DictReader(open(MAN, encoding="utf-8")))
    got_urls = {r["url"].strip() for r in man if r["status"] == "RETRIEVED"}
    got_names = {r["url"].strip().rstrip("/").split("/")[-1] for r in man if r["status"] == "RETRIEVED"}
    text = open(RP, encoding="utf-8").read()
    lines = text.splitlines()
    problems = 0

    # 1. claims table
    # table layout: | # | Tag | Claim (id in parentheses) | Value | Period | Exact public URL | Page |
    rows = [l for l in lines if re.match(r"^\| \d+ \| \[[FCSI]\] \|", l)]
    print(f"[1] claim rows: {len(rows)}")
    for l in rows:
        c = [x.strip() for x in l.strip("|").split("|")]
        n, tag, claim, value, period, url, page = c[:7]
        m = re.search(r"\(((?:A[1-6]|TH|CL|DS)-\d{3})\)\s*$", claim) or re.search(r"((?:A[1-6]|TH|CL|DS)-\d{3})", claim)
        rid = m.group(1) if m else ""
        r = ev.get(rid)
        errs = []
        if r is None:
            errs.append("id not in evidence.csv")
        else:
            if tag != r["tag"]:
                errs.append(f"tag {tag} vs evidence {r['tag']}")
            if url != r["url"].strip():
                errs.append(f"url differs from evidence ({r['url']})")
            evpages = set(re.findall(r"p\.(\d+)", r["page_or_section"]))
            evpages |= set(re.findall(r"p\.\d+-(\d+)", r["page_or_section"]))
            for p in re.findall(r"p\.\s*(\d+)", page) or re.findall(r"^\s*(\d+)", page):
                if p not in evpages:
                    errs.append(f"page {p} not in evidence page field '{r['page_or_section'][:40]}'")
            hay = " ".join([r["value"], r["claim"], r["quote"]]).replace(",", "")
            for x in nums(value):
                if x not in hay and not re.fullmatch(r"20\d\d", x):
                    errs.append(f"value number {x} not in evidence row")
            pf = r["period_fiscal"]
            labs = re.findall(r"FY\d{4}(?: Q[1-4]| 1H| end| Q[1-4] end)?|CY\d{4}", pf)
            for lab in labs:
                k = lab.replace(" 1H", "")
                if k.endswith(" end"):
                    continue  # point-in-time rows are labelled by date in the packet
                if k not in period and lab not in period and not ("1H" in lab and f"1H {lab.split()[0]}" in period):
                    errs.append(f"evidence period '{lab}' not in Period cell")
        status = "OK" if not errs else "PROBLEM: " + "; ".join(errs)
        problems += bool(errs)
        print(f"    {n:>2} {rid}: {status}")

    # 2. URLs
    urls = sorted(set(re.findall(r"https://[^\s|)]+", text)))
    bad_u = [u for u in urls if u.rstrip(".,;") not in got_urls and not u.endswith("/")]
    names = sorted(set(re.findall(r"\b([A-Za-z0-9_]+\.pdf) p\.", text)))
    bad_n = [x for x in names if x not in got_names]
    print(f"[2] full URLs: {len(urls)} ({len(bad_u)} not RETRIEVED in the manifest); file names with a page: {len(names)} ({len(bad_n)} not matched)")
    for u in bad_u + bad_n:
        print(f"    NOT IN MANIFEST AS RETRIEVED: {u}")
    problems += len(bad_u) + len(bad_n)

    # 3. inferences
    grp = re.compile(r"\[I\] (High|Medium|Low) \(([^()]*)\)")
    nI = 0
    for l in lines:
        for m in grp.finditer(l):
            for rid in re.findall(r"(?:A[1-6]|TH|CL|DS)-\d{3}", m.group(2)):
                nI += 1
                r = ev.get(rid)
                errs = []
                if r is None:
                    errs.append("missing")
                else:
                    if r["tag"] != "[I]":
                        errs.append(f"tag {r['tag']}")
                    if r["confidence"] != m.group(1):
                        errs.append(f"confidence {m.group(1)} vs evidence {r['confidence']}")
                    v = nums(r["value"])
                    if v and v[0] not in l.replace(",", ""):
                        errs.append(f"evidence value {r['value'][:30]} not in the paragraph")
                print(f"    [I] {rid}: {'OK' if not errs else 'PROBLEM: ' + '; '.join(errs)}")
                problems += bool(errs)
    print(f"[3] [I] citations checked: {nI}")

    # 4. vocabulary
    vw = re.compile(r"\b(validat\w*|refut\w*|confirm\w*|prov(?:e|es|ed|ing)\b)", re.I)
    vv = re.compile(r"\b(valuation|multiple[s]?|P/E|price target|target price|market cap\w*|undervalued|overvalued|"
                    r"buy rating|sell rating|outperform|underperform|upside|downside|share price|stock price)\b", re.I)
    v1 = [(i, m.group(0)) for i, l in enumerate(lines, 1) for m in vw.finditer(l)]
    v2 = [(i, m.group(0)) for i, l in enumerate(lines, 1) for m in vv.finditer(l)]
    print(f"[4] verdict words: {len(v1)} {v1}; valuation/price vocabulary: {len(v2)} {v2}")

    # 5. period labels
    lab = re.compile(r"(?<![\w-])((?:[12]H )?FY20\d\d(?: Q[1-4]| 1H| 2H)?)(?![\w-])")
    miss = []
    for i, l in enumerate(lines, 1):
        for m in lab.finditer(l):
            after = l[m.end():m.end() + 30]
            if re.match(rf"\s*\(?\s*(?:end\s*,?\s*)?(?:\d{{1,2}} )?{MON}", after) or re.match(rf",?\s*{MON}", after):
                continue
            if re.search(rf"\b{re.escape(m.group(1))}\s*\((?:\d{{1,2}} )?{MON}", l) or re.match(r"\s*(?:=|end\b)", after):
                continue
            miss.append((i, m.group(1)))
    print(f"[5] fiscal labels without calendar months in their line: {len(miss)} {miss}")
    print(f"RESULT problems in checks 1-3: {problems}")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
