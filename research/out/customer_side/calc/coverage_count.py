#!/usr/bin/env python3
"""Count records and affiliation coverage in the saved Crossref volume listings (non-SPIE)."""
import glob, json, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
tot = aff = 0
for f in glob.glob(os.path.join(ROOT, "research/sources/customer_side/*_crossref_*-volume-list.json")):
    if "SPIE" in f:
        continue
    for i in json.load(open(f))["message"]["items"]:
        tot += 1
        aff += any(a.get("affiliation") for a in i.get("author", []))
print(f"records={tot} with_affiliation={aff} without={tot-aff}")
