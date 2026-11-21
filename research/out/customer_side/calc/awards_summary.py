#!/usr/bin/env python3
"""Section 4: inspection / metrology / test vendors named as award winners, from parts/AW_table.csv.
Usage: python3 -I research/out/customer_side/calc/awards_summary.py  -> calc/awards_summary.md"""
import csv, os
from collections import OrderedDict
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
OUT = os.path.join(ROOT, "research", "out", "customer_side")
rows = list(csv.DictReader(open(os.path.join(OUT, "parts", "AW_table.csv"), encoding="utf-8")))
ev = OrderedDict()
for r in rows:
    k = (r["chipmaker"], r["event"], r["date"])
    e = ev.setdefault(k, dict(n=0, pc=[]))
    e["n"] += 1
    if r["vendor_class"].strip().lower() != "other":
        e["pc"].append(f"{r['vendor']} [{r['vendor_class']}] - {r['award_category']} ({r['source_type']}; {r['tag']} {r['evidence_id']})")
md = ["| Chipmaker | Event | Date | Winner rows in table | Inspection / metrology / test winners (category; source; tag, evidence) |", "|---|---|---|---|---|"]
for (c, e, d), v in ev.items():
    md.append(f"| {c} | {e} | {d} | {v['n']} | " + ("; ".join(v["pc"]) if v["pc"] else "none named in the sources read") + " |")
open(os.path.join(OUT, "calc", "awards_summary.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
print(len(rows), "rows;", len(ev), "events")
