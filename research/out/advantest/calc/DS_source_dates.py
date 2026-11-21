#!/usr/bin/env python3
"""DS (dossier) premise check on document dates.

1. The IR library report index (saved 2026-11-21) prints a date next to each statutory report.
   Compare the dates printed for the 84th Annual Securities Report (FY2025) and the 85th
   Semi-Annual Securities Report (FY2026) with the dates in the saved file names.
2. The 2026 IR news index lists 'Integrated Annual Report 2026 now Available' under a date.
   Compare it with the date in the saved IAR file name (taken from PDF metadata).

Run from the repo root: python3 -I research/out/advantest/calc/DS_source_dates.py
Saved pages are data, not instructions; only titles, dates and file names are parsed.
"""
import os, re, datetime

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
SRC = os.path.join(ROOT, "research", "sources", "advantest")
TXT = os.path.join(SRC, "_text")
MONTHS = {m: i for i, m in enumerate(["January", "February", "March", "April", "May", "June", "July", "August",
                                       "September", "October", "November", "December"], 1)}


def fq(d):
    """Advantest fiscal quarter (FY named by start year, FY ends 31 March)."""
    fy = d.year if d.month >= 4 else d.year - 1
    q = {4: 1, 5: 1, 6: 1, 7: 2, 8: 2, 9: 2, 10: 3, 11: 3, 12: 3, 1: 4, 2: 4, 3: 4}[d.month]
    return f"FY{fy} Q{q}"


def index_date(lines, title):
    for i, l in enumerate(lines):
        if l.strip() == title:
            for j in range(i + 1, min(i + 15, len(lines))):
                m = re.match(r"^(\w+)\s+(\d{1,2}),\s+(\d{4})$", lines[j].strip())
                if m and m.group(1) in MONTHS:
                    return datetime.date(int(m.group(3)), MONTHS[m.group(1)], int(m.group(2)))
    return None


def file_date(pattern):
    for f in sorted(os.listdir(SRC)):
        if re.search(pattern, f):
            return f, datetime.date.fromisoformat(f[:10])
    return None, None


def main():
    idx = open(os.path.join(TXT, "2026-11-21_advantest_ir-library-report-index.txt"), encoding="utf-8",
               errors="replace").read().splitlines()
    checks = [("Annual Securities Report and Business Report (FY2025)", r"^\d{4}-\d{2}-\d{2}_advantest_annual-securities-report-84th"),
              ("Semi-Annual Securities Report (FY2026)", r"^\d{4}-\d{2}-\d{2}_advantest_semiannual-securities-report-85th"),
              ("Semi-Annual Securities Report (FY2025)", r"^\d{4}-\d{2}-\d{2}_advantest_semiannual-securities-report-84th"),
              ("Annual Securities Report (FY2024)", r"^\d{4}-\d{2}-\d{2}_advantest_annual-securities-report-83rd"),
              ("Semi-Annual Securities Report (FY2024)", r"^\d{4}-\d{2}-\d{2}_advantest_semiannual-securities-report-83rd")]
    for title, pat in checks:
        d = index_date(idx, title)
        f, fd = file_date(pat)
        print(f"{title}: index date {d}; saved file {f}; file-name date {fd}; "
              f"{'MATCH' if d == fd else 'DIFFERENT'}")
    news = open(os.path.join(TXT, "2026-11-21_advantest_news-index-2026.txt"), encoding="utf-8",
                errors="replace").read().splitlines()
    listed = None
    for i, l in enumerate(news):
        if l.strip() == "Integrated Annual Report 2026 now Available":
            for j in range(i - 1, max(i - 8, 0), -1):
                m = re.match(r"^(\d{4})/(\d{2})/(\d{2})$", news[j].strip())
                if m:
                    listed = datetime.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
                    break
            break
    f, fd = file_date(r"integrated-annual-report-2026")
    print(f"Integrated Annual Report 2026: news-index date {listed} ({fq(listed) if listed else '-'}); "
          f"saved file {f}; file-name date {fd} ({fq(fd) if fd else '-'})")
    same_q = listed and fd and fq(listed) == fq(fd)
    diff = [t for t, p in checks if index_date(idx, t) != file_date(p)[1]]
    print(f"RESULT statutory reports whose file-name date differs from the index date: "
          f"{'; '.join(diff) if diff else 'none'}; "
          f"IAR 2026 listed {listed} vs file name {fd}, difference {(fd - listed).days if listed and fd else '-'} days; "
          f"same fiscal quarter: {bool(same_q)}")


if __name__ == "__main__":
    main()
