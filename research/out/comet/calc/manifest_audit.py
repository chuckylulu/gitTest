#!/usr/bin/env python3
"""Audit research/sources/comet/_manifest.csv: rows marked RETRIEVED whose file is missing (deleted by an agent
because it was a listing/JS page) or is a stub (bot-check / redirect page, not the document) are re-marked
NOT RETRIEVED with an audit note. Prints every change. Idempotent."""
import csv, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
M = os.path.join(ROOT, "research/sources/comet/_manifest.csv")
STUBS = {"research/sources/comet/2026-11-21_waygate_product-page-mesofocus-x-ray-tubes.html": "212-byte bot-check page",
         "research/sources/comet/2025-01-01_elsevier_microrel-115694-Dreier-nanoCT-AP.html": "redirect stub, not the paper"}
rows = list(csv.DictReader(open(M)))
fields = list(rows[0].keys())
for r in rows:
    if r["status"] != "RETRIEVED":
        continue
    p = os.path.join(ROOT, r["local_file"])
    why = None
    if not os.path.exists(p):
        why = "file deleted after download: generic listing/JS page, not the document"
    elif r["local_file"] in STUBS:
        why = STUBS[r["local_file"]] + "; file kept but must not be cited"
    if why:
        r["status"] = "NOT RETRIEVED"
        r["note"] = (r["note"] + " | AUDIT 2026-11-21: " + why).strip(" |")
        print("CHANGED", r["local_file"], "->", why)
with open(M, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)
