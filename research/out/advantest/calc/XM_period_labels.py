#!/usr/bin/env python3
"""XM: unify the period labels of dated statements across research/out/advantest/parts/<MOD>.csv.

Run (rewrites the parts files in place and prints every change):
    python3 -I research/out/advantest/calc/XM_period_labels.py > research/out/advantest/calc/XM_period_labels.out.txt
    python3 -I research/out/advantest/calc/XM_period_labels.py --dry-run   # print only

Fiscal year ends 31 March and is named by its start year (FY2026 = Apr 2026-Mar 2027).

RULE (reconcile task, 2026-11-21)
  R1 A statement about the past or present uses the fiscal quarter that contains the statement date:
     period_fiscal "FY2026 Q3", period_calendar "Oct-Dec 2026 (stated 12 Nov 2026)".
  R2 A statement about a forecast period uses that forecast period plus the statement date:
     period_fiscal "FY2026", period_calendar "Apr 2026-Mar 2027 (stated 28 Oct 2026)".
  R3 Calendar-year metrics use period_fiscal "n/a (calendar year)" and period_calendar "CY2026";
     a company statement or estimate about a calendar year also carries " (stated D Mon YYYY)".

WHICH ROWS ARE "DATED STATEMENTS"
  - every [C] row (company claims, guidance, forecasts, targets, estimates, explanations);
  - [F] and [S] rows whose period_calendar already marks them as statements ("stated", "estimate of",
    "forecast of", "asked", ...) or whose claim is attributed speech (Management:, CEO, CFO, Company says,
    Teradyne:, ...), EXCEPT an attributed [F] row without such a marker whose value is a reported number
    (JPY/USD/%) for a closed fiscal period: that row is a reported figure and keeps its period.
  NOT touched: [I] rows; reported figures; dated events that are not statements (rules published, record
  dates, buyback windows, product releases with their own verbs); "n/a (preprint)", "n/a (conference
  material)" and other publication labels; Teradyne reported quarters ("Teradyne Q3 2026").

HOW A STATEMENT IS LABELLED (statement date D: the date after "stated"/"estimate of"/... in
period_calendar, else a bare "(D)" there, else the row's date column)
  CY  period_fiscal "n/a (calendar year)" or period_calendar starting "CY"  -> R3
  P   the labelled period ended before D (a statement about the past)        -> R1 (statement quarter)
  Q   the labelled period is a quarter that contains D (a present statement) -> R1 (same quarter)
  F   the labelled period runs past D (a forecast period, or a longer period in progress) -> R2
  T   third-party or undated labels ("n/a (Teradyne statement)", "n/a (Micron statement)", "n/a (no date)")
      -> R1, because they name no forecast period
  M   manual decisions listed in MANUAL below (same statement labelled differently by two modules, or a
      label the parser cannot read)
  Extra words inside the period_calendar parentheses (e.g. "horizon at least 2-3 years", "CB issued Apr
  2026") are moved to the note. When R1 moves a row away from the period it was labelled with, the note
  records "statement refers to <old label>".
"""
import csv, datetime as dt, io, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PARTS = os.path.join(os.path.dirname(HERE), "parts")
MODS = ["A1", "A2", "A3", "A4", "A5", "A6", "TH", "CL"]
MON = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
TAGNOTE = " [reconcile XM 2026-11-21]"

VERBS = r"stated in report filed|stated|published|estimate of|estimate as of|forecast of|forecast as of|outlook stated|guidance of|expectation stated|assumption of|final, as shown|as shown|presentation|presented|asked|announced|Integrated Annual Report dated"
STMT_MARK = re.compile(r"\b(stated|estimate of|estimate as of|forecast of|forecast as of|outlook stated|guidance of|expectation stated|assumption of|as shown|presentation|presented|asked)\b")
ATTRIB = re.compile(r"^(Management|CEO|CFO|CTO|Group CEO|President|Company says|Company said|Company \(|Advantest says|Advantest \(|Advantest declined|Disclosure policy|Teradyne( CEO)?[:( ]|Teradyne says|Teradyne claim|Micron \()")
DATE_RX = r"(\d{1,2} [A-Z][a-z]{2} \d{4})"

# id -> (period_fiscal, period_calendar, note addition). D placeholders are filled from the statement date.
MANUAL = {
    # same statement, two modules (A2-057 / A5-193): planned use of CB funds -> forecast period of the plan
    "A2-057": ("FY2026-FY2028", "Apr 2026-Mar 2029 (stated {D})", "Forecast period matched to A5-193 and the planned-use dates A5-072/A5-073 (by Mar 2029 / Mar 2027)."),
    # same statement (A4-314 / CL-061): China share outlook until new China fabs around 2028-2029
    "A4-314": ("n/a (calendar year)", "to CY2028-CY2029 (stated {D})", "Forecast horizon matched to CL-061 (same Q&A answer)."),
    # same statement (TH-042 / CL-001): TAM growth 'over the past few years' names no year -> statement quarter
    "CL-001": (None, None, "Statement about the past few years (no years named); labelled like TH-042."),
    # same statement (TH-117 / CL-040): path to SoC share above 70%, no timing -> statement quarter
    "CL-040": (None, None, "No timing given; labelled like TH-117."),
    # same statement (TH-041 / CL-071): reason for the raised FY2026 forecast -> forecast period FY2026
    "TH-041": ("FY2026", "Apr 2026-Mar 2027 (stated {D})", "Explains the raised FY2026 forecast; labelled like CL-071."),
    # same figures (TH-169 / CL-018): one calendar wording
    "TH-169": ("n/a (calendar year)", "CY2025; Jan-Aug 2026 (stated {D})", "Calendar wording matched to CL-018."),
    # Teradyne guidance is a forecast for Teradyne's own quarter; Teradyne present-tense statements -> statement quarter
    "CL-136": ("Teradyne Q4 2026", "Oct-Dec 2026 (stated {D})", None),
    "CL-019": (None, None, "Teradyne statement on its 2H 2026 compute program timing."),
    "CL-020": (None, None, None),
    "CL-044": (None, None, None),
    "CL-054": (None, None, None),
    "CL-080": (None, None, "Teradyne's Q4 2026 call date is not given."),
    # unparseable label: CFO statement (Nov 2026) that the 2014 CB was fully converted
    "A5-086": (None, None, "Refers to the CB issued in 2014."),
    # analyst question (secondary): keep the verb "asked"
    "CL-016": (None, "{SQ} (asked {D})", None),
    # dated press item (not a statement row): quarter did not contain its publication date
    "CL-062": ("FY2025 Q4", "Jan-Mar 2026 (published 30 Jan 2026)", "Quarter corrected: 30 Jan 2026 falls in FY2025 Q4 (Jan-Mar 2026)."),
}


def d2s(d):
    return f"{d.day} {MON[d.month - 1]} {d.year}"


def s2d(s):
    s = s.strip()
    try:
        return dt.datetime.strptime(s, "%Y-%m-%d").date()
    except ValueError:
        return dt.datetime.strptime(s, "%d %b %Y").date()


def fq(d):
    fy = d.year if d.month >= 4 else d.year - 1
    q = (d.month - 4) % 12 // 3 + 1
    return fy, q


def months(m0, y0, n):
    m1 = (m0 + n - 1) % 12
    y1 = y0 + (m0 + n - 1) // 12
    return f"{MON[m0]}-{MON[m1]} {y1}" if y0 == y1 else f"{MON[m0]} {y0}-{MON[m1]} {y1}"


def qlabel(d):
    fy, q = fq(d)
    m0 = (3 + 3 * (q - 1)) % 12
    y0 = fy + (3 + 3 * (q - 1)) // 12
    return f"FY{fy} Q{q}", months(m0, y0, 3)


def month_end(y, m):
    return (dt.date(y + (m == 12), m % 12 + 1, 1) - dt.timedelta(days=1))


def span(pf):
    """(start, end, kind, calendar label) for a fiscal label, else None."""
    pf = pf.strip()
    m = re.fullmatch(r"FY(\d{4})", pf)
    if m:
        y = int(m.group(1)); return dt.date(y, 4, 1), dt.date(y + 1, 3, 31), "year", months(3, y, 12)
    m = re.fullmatch(r"FY(\d{4}) Q([1-4])", pf)
    if m:
        y, q = int(m.group(1)), int(m.group(2)); s = 3 + 3 * (q - 1)
        y0, m0 = y + s // 12, s % 12
        return dt.date(y0, m0 + 1, 1), month_end(y0 + (m0 + 2) // 12, (m0 + 2) % 12 + 1), "quarter", months(m0, y0, 3)
    m = re.fullmatch(r"FY(\d{4}) (1H|2H|9M)", pf)
    if m:
        y, k = int(m.group(1)), m.group(2)
        if k == "1H":
            return dt.date(y, 4, 1), dt.date(y, 9, 30), "half", months(3, y, 6)
        if k == "2H":
            return dt.date(y, 10, 1), dt.date(y + 1, 3, 31), "half", months(9, y, 6)
        return dt.date(y, 4, 1), dt.date(y, 12, 31), "9m", months(3, y, 9)
    m = re.fullmatch(r"FY(\d{4})(?: Q([1-4]))? end", pf)
    if m:
        y, q = int(m.group(1)), int(m.group(2) or 4)
        e = 3 + 3 * q - 1
        d = month_end(y + e // 12, e % 12 + 1)
        return d, d, "point", d2s(d)
    m = re.fullmatch(r"FY(\d{4})-FY(\d{4})(?: avg)?", pf)
    if m:
        a, b = int(m.group(1)), int(m.group(2))
        return dt.date(a, 4, 1), dt.date(b + 1, 3, 31), "multi", f"Apr {a}-Mar {b + 1}"
    m = re.fullmatch(r"Teradyne Q([1-4]) (\d{4})", pf)
    if m:
        q, y = int(m.group(1)), int(m.group(2)); m0 = 3 * (q - 1)
        return dt.date(y, m0 + 1, 1), month_end(y, m0 + 3), "quarter", months(m0, y, 3)
    m = re.fullmatch(r"Teradyne 2H (\d{4})", pf)
    if m:
        y = int(m.group(1)); return dt.date(y, 7, 1), dt.date(y, 12, 31), "half", months(6, y, 6)
    return None


def stmt_date(r):
    pc = r["period_calendar"]
    m = re.search(r"(?:" + VERBS + r")\s+" + DATE_RX, pc)
    if m:
        return s2d(m.group(1))
    m = re.search(r"\(" + DATE_RX + r"\)", pc)
    if m:
        return s2d(m.group(1))
    m = re.search(r"\((?:[^()]*;\s*)?" + DATE_RX + r"(?:;[^()]*)?\)", pc)
    if m:
        return s2d(m.group(1))
    return s2d(r["date"])


def split_pc(pc):
    """core label and the list of extra phrases inside the trailing parentheses (dates/verbs dropped)."""
    m = re.match(r"^(.*?)\s*\((.*)\)\s*$", pc)
    if not m:
        return pc.strip(), []
    core, inner = m.group(1).strip(), m.group(2)
    extras = []
    for part in [p.strip() for p in inner.split(";")]:
        if re.fullmatch(r"(?:(?:" + VERBS + r")\s+)?" + DATE_RX, part) or not part:
            continue
        extras.append(part)
    return core, extras


def is_statement(r):
    tag, pc, pf = r["tag"], r["period_calendar"], r["period_fiscal"]
    if tag == "[I]":
        return False
    if pf.startswith(("n/a (preprint)", "n/a (conference material)", "n/a (document scan)", "n/a (Teradyne Q3", "n/a (Teradyne FY", "n/a (Teradyne target", "n/a (Teradyne event)", "n/a (standing rule)")):
        return False
    if re.match(r"Teradyne Q\d \d{4}$", pf) and tag == "[F]":
        return False
    if tag == "[C]":
        return True
    marked = bool(STMT_MARK.search(pc))
    if marked:
        return True
    if ATTRIB.search(r["claim"]):
        sp = span(pf)
        numeric = bool(re.search(r"\d", r["value"])) and r["unit"].startswith(("JPY", "USD", "%"))
        if tag == "[F]" and numeric and sp and sp[1] < stmt_date(r):
            return False  # reported figure for a closed period
        return True
    return False


def relabel(r):
    """returns (new_pf, new_pc, note_add, branch) or None if unchanged/not applicable."""
    if not is_statement(r) and r["id"] not in MANUAL:
        return None
    pf, pc = r["period_fiscal"].strip(), r["period_calendar"].strip()
    d = stmt_date(r)
    D = d2s(d)
    core, extras = split_pc(pc)
    notes = []
    if extras:
        notes.append("Period detail moved from period_calendar: " + "; ".join(extras) + ".")
    sq_pf, sq_months = qlabel(d)

    if r["id"] in MANUAL:
        mpf, mpc, mnote = MANUAL[r["id"]]
        if mpf is None:  # statement quarter
            mpf, mpc = sq_pf, (mpc or "{SQ} (stated {D})")
            if pf != sq_pf:
                notes.append(f"Statement refers to {pf} ({core})." if span(pf) else f"Former label: {pf} / {core}.")
        if mnote:
            notes.append(mnote)
        return mpf, mpc.format(D=D, SQ=sq_months), " ".join(notes), "M"

    if pf.startswith("n/a (calendar year)") or core.startswith("CY"):
        return "n/a (calendar year)", f"{core} (stated {D})", " ".join(notes), "CY"
    if pf.startswith(("n/a (Teradyne statement)", "n/a (Micron statement)", "n/a (no date)")):
        if core not in (sq_months,):
            notes.append(f"Former label: {pf} / {core}.")
        return sq_pf, f"{sq_months} (stated {D})", " ".join(notes), "T"

    base = re.sub(r"\s*\((forecast|outlook|forecast, Q3 and Q4)\)", "", pf)
    m = re.match(r"^(FY\d{4} (?:1H|2H)) \(forecast\) vs (FY\d{4} (?:1H|2H))$", pf)
    if m:
        base = m.group(1); notes.append(f"Compared with {m.group(2)}.")
    if base != pf and "forecast, Q3 and Q4" in pf:
        notes.append("Forecast covers Q3 and Q4.")
    sp = span(base)
    if sp is None:
        return ("UNPARSED", pf, pc)
    start, end, kind, cal = sp
    if end < d:
        if base != sq_pf:
            notes.append(f"Statement refers to {base} ({cal}).")
        return sq_pf, f"{sq_months} (stated {D})", " ".join(notes), "P"
    if kind == "quarter" and start <= d <= end:
        return base, f"{cal} (stated {D})", " ".join(notes), "Q"
    return base, f"{cal} (stated {D})", " ".join(notes), "F"


def main():
    dry = "--dry-run" in sys.argv
    changes, unparsed, counts = [], [], {}
    data = {}
    for mod in MODS:
        p = os.path.join(PARTS, f"{mod}.csv")
        raw = open(p, encoding="utf-8", newline="").read()
        term = "\r\n" if "\r\n" in raw else "\n"
        rows = list(csv.DictReader(io.StringIO(raw)))
        cols = list(rows[0].keys())
        for r in rows:
            res = relabel(r)
            if res is None:
                continue
            if res[0] == "UNPARSED":
                unparsed.append((r["id"], r["tag"], res[1], res[2]))
                continue
            npf, npc, nnote, br = res
            if (npf, npc) == (r["period_fiscal"], r["period_calendar"]) and not nnote:
                counts["unchanged"] = counts.get("unchanged", 0) + 1
                continue
            if (npf, npc) == (r["period_fiscal"], r["period_calendar"]):
                nnote = ""  # label already conforms; keep the note as it is
                counts["unchanged"] = counts.get("unchanged", 0) + 1
                continue
            counts[br] = counts.get(br, 0) + 1
            changes.append((r["id"], r["tag"], br, r["period_fiscal"], r["period_calendar"], npf, npc, nnote))
            r["period_fiscal"], r["period_calendar"] = npf, npc
            if nnote:
                r["note"] = (r["note"] + " " if r["note"] else "") + nnote + TAGNOTE
        data[mod] = (p, term, cols, rows)
    print(f"statement rows relabelled: {len(changes)}; by branch {dict(sorted(counts.items()))}")
    print("branch codes: CY calendar-year; P past -> statement quarter; Q present quarter; F forecast period; T third-party/undated -> statement quarter; M manual\n")
    print("id | tag | branch | period_fiscal before -> after | period_calendar before -> after | note added")
    for c in changes:
        print(f"{c[0]} | {c[1]} | {c[2]} | {c[3]} -> {c[5]} | {c[4]} -> {c[6]} | {c[7]}")
    print(f"\nstatement rows left unchanged because the label could not be parsed: {len(unparsed)}")
    for u in unparsed:
        print(f"  {u[0]} {u[1]} | {u[2]} | {u[3]}")
    # dated items that are not statements: does the quarter contain the date in brackets?
    print("\nnon-statement rows whose quarter label does not contain the single date in their period_calendar (review):")
    n = 0
    for mod, (p, term, cols, rows) in data.items():
        for r in rows:
            if r["tag"] == "[I]" or is_statement(r):
                continue
            sp = span(r["period_fiscal"])
            ds = re.findall(DATE_RX, r["period_calendar"])
            if sp and sp[2] == "quarter" and len(ds) == 1 and r["period_calendar"].startswith(sp[3]):
                d = s2d(ds[0])
                if not (sp[0] <= d <= sp[1]):
                    n += 1
                    print(f"  {r['id']} {r['tag']} | {r['period_fiscal']} | {r['period_calendar']} | {r['claim'][:80]}")
    print(f"  total: {n}")
    if not dry:
        for mod, (p, term, cols, rows) in data.items():
            out = io.StringIO()
            w = csv.DictWriter(out, fieldnames=cols, lineterminator=term)
            w.writeheader(); w.writerows(rows)
            open(p, "w", encoding="utf-8", newline="").write(out.getvalue())


if __name__ == "__main__":
    main()
