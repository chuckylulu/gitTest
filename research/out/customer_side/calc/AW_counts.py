#!/usr/bin/env python3
"""Module AW: count inspection/metrology/test winners per supplier-award event.

Input : research/out/customer_side/parts/AW_table.csv
Output: printed table (pasted into parts/AW_notes.md) - per event: distinct winners listed in the
        source used for the full list, how many are inspection/metrology/test, and which.
Only rows from list-type sources (source_type 'press' or 'chipmaker list') are counted, so vendor
releases do not double-count a winner. Events whose source names only part of the winners are flagged.
Run: python3 -I research/out/customer_side/calc/AW_counts.py
"""
import csv, os, collections

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rows = list(csv.DictReader(open(os.path.join(ROOT, "parts", "AW_table.csv"), encoding="utf-8")))
PM = {"inspection", "metrology", "test"}
ev = collections.OrderedDict()
for r in rows:
    if r["source_type"] not in ("press", "chipmaker list"):
        continue
    k = (r["chipmaker"], r["event"], r["date"])
    d = ev.setdefault(k, {"all": [], "pm": []})
    name = r["vendor"].split(" (")[0].strip()
    if name not in d["all"]:
        d["all"].append(name)
    if r["vendor_class"] in PM and name not in d["pm"]:
        d["pm"].append(f'{name} [{r["vendor_class"]}]')
tot_all = tot_pm = 0
print("| chipmaker | event | date | winners listed in source | insp/metro/test | names |")
print("|---|---|---|---|---|---|")
for (c, e, d), v in ev.items():
    n, m = len(v["all"]), len(v["pm"])
    partial = " (partial list)" if ("named" in e or (c == "Intel" and "2026" in e) or "blog post" in e) else ""
    print(f"| {c} | {e} | {d} | {n}{partial} | {m} | {', '.join(v['pm']) or '-'} |")
    if not partial:
        tot_all += n; tot_pm += m
print(f"\nFull lists only: {tot_pm} inspection/metrology/test entries out of {tot_all} listed winner entries "
      f"({100.0 * tot_pm / tot_all:.1f}%).")
