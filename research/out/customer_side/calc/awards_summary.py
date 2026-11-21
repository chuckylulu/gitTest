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
        cat = r["award_category"]
        cat = cat.replace("(category NOT RETRIEVED: Intel list)", "- category NOT RETRIEVED (tried: Intel newsroom list with fetch.py, HTTP 403)")
        cat = cat.replace("(category not stated in release)", "- category NOT DISCLOSED (read: vendor release cited)")
        e["pc"].append(f"{r['vendor']} [{r['vendor_class']}] - {cat} ({r['source_type']}; {r['tag']} {r['evidence_id']})")
# Events whose source lists no inspection / metrology / test winner: say why, in the allowed forms, with tags.
NONE = {
    "2026 DS": "none of the 4 named winners is an inspection, metrology or test vendor [F] AW-040; the other 13 winners NOT DISCLOSED (read: Samsung Newsroom KR, 'DS부문 2026년 상생협력 DAY' 2026-04-03)",
    "Micron Supplier Awards 2025": "none: full list read, no inspection or metrology category [F] AW-042; vendor classification [I] AW-058",
    "Micron Supplier Awards 2026": "none: full list read, no inspection or metrology category [F] AW-043; vendor classification [I] AW-058",
    "Amkor Supplier Award (SiP": "Henkel [other] [F] AW-056; full list NOT RETRIEVED (tried: amkor.com blog index and web searches; ir.amkor.com refuses scripts)",
}
COUNT_NOTE = {"Micron Supplier Awards 2026": "13 companies (14 awards)"}
EXTRA = [
    ("SK hynix", "2025 Partners Day (파트너스데이), 14 winners", "2025-09-29", "1",
     "ULVAC [other] - Best Partner Award (vendor release; [F] AW-033); the other 13 winners NOT DISCLOSED (read: SK hynix Newsroom KR, '2025 파트너스데이' 2025-09-30, full article) [F] AW-032"),
    ("SK hynix", "2026 Partners Day, 11 winners", "2026-09-28", "0",
     "winners NOT DISCLOSED (read: SK hynix Newsroom KR, '2026 파트너스데이' 2026-09-29, full article and three photo-caption pages) [F] AW-034; Onto Innovation release on a 2026 Best Partner Award for HBM hidden-defect prevention NOT RETRIEVED (tried: investors.ontoinnovation.com, host refuses scripts; https://www.businesswire.com/news/home/20261012570961/en/ with fetch.py, curl stream error)"),
    ("Amkor", "Supplier Excellence Award 2025", "2025-12-09", "1",
     "Senju Metal Industry [other] (vendor release; [F] AW-057); full list NOT RETRIEVED (tried: amkor.com blog index and web searches; ir.amkor.com refuses scripts)"),
]
md = ["| Chipmaker | Event | Date | Winner rows in table | Inspection / metrology / test winners (category; source; tag, evidence) |", "|---|---|---|---|---|"]
for (c, e, d), v in ev.items():
    none = next((t for k, t in NONE.items() if k in e), "NOT DISCLOSED (read: sources cited in parts/AW_notes.md for this event)")
    n = next((t for k, t in COUNT_NOTE.items() if k in e), str(v["n"]))
    md.append(f"| {c} | {e} | {d} | {n} | " + ("; ".join(v["pc"]) if v["pc"] else none) + " |")
for row in EXTRA:
    md.append("| " + " | ".join(row) + " |")
open(os.path.join(OUT, "calc", "awards_summary.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
print(len(rows), "rows;", len(ev), "events")
