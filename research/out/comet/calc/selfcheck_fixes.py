#!/usr/bin/env python3
"""Apply fixes from the clean-context self-check (see run_log.md) to parts CSVs. Run after any rebuild of A.csv / DV.csv,
then re-run tools/merge_parts.py."""
import csv, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
FIX = {
 ("A", "A-001"): {"page_or_section": "p10 (income statement; same figures in the book-to-bill reconciliation on p9)"},
 ("DV", "DV-142"): {"quote": "Transforming into a Scalable High-tech Leader.",
                    "note": "Figures read from the rendered slide p86 (chart layout scrambles the extracted text); self-check confirmed PCT 21 -> 27-33, IXS -4 -> 5-9, IXM 15 -> 23-27. Earlier quote 'EBITDA +6 PP to +9 PP' spliced two divisions and was replaced."},
}
for (part, rid), ch in FIX.items():
    p = os.path.join(ROOT, f"research/out/comet/parts/{part}.csv")
    rows = list(csv.DictReader(open(p, encoding="utf-8"))); cols = list(rows[0].keys())
    for r in rows:
        if r["id"] == rid:
            r.update(ch); print("fixed", rid)
    with open(p, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows)
