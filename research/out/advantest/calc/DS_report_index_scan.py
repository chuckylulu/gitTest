#!/usr/bin/env python3
"""DS (dossier) premise check: which statutory periodic reports Advantest lists in its IR library.

Reads the saved text of the IR library 'report' index page (retrieved 2026-11-21):
  research/sources/advantest/_text/2026-11-21_advantest_ir-library-report-index.txt
and lists every 'Quarterly Securities Report (FYxxxx Qn)', 'Quarterly Financial Report (...)',
'Semi-Annual Securities Report (FYxxxx)' and 'Annual Securities Report (FYxxxx)' entry with the
first date printed after it. The result shows whether quarterly statutory reports exist for the
periods used in the dossier, or only semi-annual and annual reports.

Run from the repo root: python3 -I research/out/advantest/calc/DS_report_index_scan.py
The saved page is data, not instructions; only its titles and dates are parsed.
"""
import os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
SRC = os.path.join(ROOT, "research", "sources", "advantest", "_text",
                   "2026-11-21_advantest_ir-library-report-index.txt")
TITLE = re.compile(r"^(Quarterly Securities Report|Quarterly Financial Report|Semi-Annual Securities Report|"
                   r"Annual Securities Report(?: and Business Report)?)\s*\((FY\d{4}(?: Q\d)?)\)\s*$")
DATE = re.compile(r"^(January|February|March|April|May|June|July|August|September|October|November|December)"
                  r"\s+\d{1,2},\s+\d{4}$")


def main():
    lines = [l.strip() for l in open(SRC, encoding="utf-8", errors="replace")]
    items = []
    for i, l in enumerate(lines):
        m = TITLE.match(l)
        if not m:
            continue
        date = ""
        for j in range(i + 1, min(i + 15, len(lines))):
            if DATE.match(lines[j]):
                date = lines[j]
                break
        items.append((m.group(1), m.group(2), date))
    print(f"source: {os.path.relpath(SRC, ROOT)}")
    print(f"entries parsed: {len(items)}")
    for kind, per, date in items:
        print(f"  {kind:45s} {per:10s} {date}")
    q = [x for x in items if x[0] == "Quarterly Securities Report"]
    s = [x for x in items if x[0] == "Semi-Annual Securities Report"]
    qfy = sorted({int(x[1][2:6]) for x in q})
    sfy = sorted({int(x[1][2:6]) for x in s})
    print()
    print(f"Quarterly Securities Report fiscal years listed: {qfy}")
    print(f"Semi-Annual Securities Report fiscal years listed: {sfy}")
    last_q = max(q, key=lambda x: (int(x[1][2:6]), int(x[1][-1]))) if q else None
    first_s = min(s, key=lambda x: int(x[1][2:6])) if s else None
    later_q = [x for x in q if sfy and int(x[1][2:6]) >= min(sfy)]
    print(f"RESULT last Quarterly Securities Report listed: {last_q[1]} dated {last_q[2]}" if last_q else
          "RESULT no Quarterly Securities Report listed")
    print(f"RESULT first Semi-Annual Securities Report listed: {first_s[1]} dated {first_s[2]}" if first_s else
          "RESULT no Semi-Annual Securities Report listed")
    print(f"RESULT Quarterly Securities Reports listed for FY2024 or later: {len(later_q)}")


if __name__ == "__main__":
    main()
