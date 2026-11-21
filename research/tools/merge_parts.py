#!/usr/bin/env python3
"""Merge per-module evidence parts into out/<company>/evidence.csv.

Usage: python3 -I research/tools/merge_parts.py <company> [module order...]
Default order: A1 A2 A3 A4 A5 A6 TH CL B, then any other parts/*.csv alphabetically.
Validates the header, tags and unique ids; prints a per-module tag count.
"""
import csv, glob, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COLS = ["id", "tag", "claim", "value", "unit", "period_fiscal", "period_calendar", "document", "date",
        "page_or_section", "url", "local_file", "quote", "confidence", "note"]


def main():
    company = sys.argv[1]
    order = sys.argv[2:] or ["A1", "A2", "A3", "A4", "A5", "A6", "TH", "CL", "B"]
    pdir = os.path.join(ROOT, "out", company, "parts")
    files = [os.path.join(pdir, f"{m}.csv") for m in order if os.path.exists(os.path.join(pdir, f"{m}.csv"))]
    files += sorted(f for f in glob.glob(os.path.join(pdir, "*.csv"))
                   if f not in files and not f.endswith("_table.csv"))  # *_table.csv are not evidence files
    out, seen, problems = [], set(), []
    for f in files:
        rows = list(csv.DictReader(open(f, encoding="utf-8")))
        hdr = list(rows[0].keys()) if rows else []
        if rows and hdr != COLS:
            problems.append(f"{os.path.basename(f)}: header differs: {hdr}")
        counts = {}
        for r in rows:
            rid = (r.get("id") or "").strip()
            if rid in seen:
                problems.append(f"duplicate id {rid}")
            seen.add(rid)
            t = (r.get("tag") or "").strip()
            counts[t] = counts.get(t, 0) + 1
            if t not in ("[F]", "[C]", "[S]", "[I]"):
                problems.append(f"{rid}: bad tag {t!r}")
            out.append({c: (r.get(c) or "").strip() for c in COLS})
        print(f"{os.path.basename(f)}: {len(rows)} rows {counts}")
    dst = os.path.join(ROOT, "out", company, "evidence.csv")
    with open(dst, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=COLS)
        w.writeheader(); w.writerows(out)
    print(f"wrote {dst}: {len(out)} rows")
    for p in problems:
        print("PROBLEM:", p)


if __name__ == "__main__":
    main()
