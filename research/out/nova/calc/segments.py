#!/usr/bin/env python3
"""Implied end-market split of Nova product revenue, last four quarters (and FY2024 for reference).

Usage: python3 -I research/out/nova/calc/segments.py
Inputs: product revenue (USD k) from the quarterly releases (quarterly_items.csv) and the
percentages management gave on the calls (third-party transcripts, tag [S]); the percentages are
rounded ('approximately'), so implied dollars carry roughly +/-2.5 points of product revenue.
Advanced packaging is NOT a third bucket on the calls: it sits inside logic/foundry and memory.
"""
import csv, os
HERE = os.path.dirname(os.path.abspath(__file__))
D = {}
for r in csv.DictReader(open(os.path.join(HERE, "quarterly_items.csv"))):
    D[(r["quarter"], r["item"])] = float(r["value"])

calls = {  # (logic/foundry %, memory %, advanced packaging % of product revenue or None, AP wording)
    "Q4-2025": (75, 25, None, "FY2025 ~20% (no quarterly figure)"),
    "Q1-2026": (66, 34, 25, "'edging towards the mid-20s' -> 25 used"),
    "Q2-2026": (73, 27, 25, "'nearly one-quarter' -> 25 used"),
    "Q3-2026": (61, 39, None, "NOT DISCLOSED"),
}
out = []
for q, (lf, mem, ap, apw) in calls.items():
    prod = D[(q, "rev_products")]; svc = D[(q, "rev_services")]; tot = D[(q, "rev_total")]
    out.append({"quarter": q, "products_k": round(prod), "services_k": round(svc),
                "services_pct_of_total": round(100 * svc / tot, 1),
                "logic_foundry_pct": lf, "memory_pct": mem,
                "implied_logic_foundry_k": round(prod * lf / 100), "implied_memory_k": round(prod * mem / 100),
                "ap_pct_used": ap if ap is not None else "", "implied_ap_k": round(prod * ap / 100) if ap else "",
                "ap_wording": apw})
# memory dollars QoQ and vs FY2024 reference (Investor Day 2025: 2024 product revenue 62/23/15 logic/memory/AP)
prev = None
for r in out:
    r["implied_memory_qoq_pct"] = "" if prev is None else round(100 * (r["implied_memory_k"] - prev) / prev, 1)
    prev = r["implied_memory_k"]
fy24_prod = D[("Q4-2024", "rev_products__fy")]
ref = {"FY2024_products_k": round(fy24_prod), "FY2024_logic_k(62%)": round(fy24_prod * .62),
       "FY2024_memory_k(23%)": round(fy24_prod * .23), "FY2024_AP_k(15%)": round(fy24_prod * .15)}
with open(os.path.join(HERE, "segments.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
for r in out:
    print(r)
print(ref)
