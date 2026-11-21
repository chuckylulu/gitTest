#!/usr/bin/env python3
"""Summarise the clean-context verification (calc/verify_results.json) and the applied fixes
(calc/fix_results.json) for run_log.md, including the 15 most important rows (review packet claims).
Usage: python3 -I research/out/customer_side/calc/selfcheck_report.py > research/out/customer_side/calc/selfcheck_report.md
"""
import csv, json, os, re
from collections import Counter
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
C = os.path.join(ROOT, "research", "out", "customer_side", "calc")
v = json.load(open(os.path.join(C, "verify_results.json")))
fx = json.load(open(os.path.join(C, "fix_results.json")))
ev = {r["id"]: r for r in csv.DictReader(open(os.path.join(C, "..", "evidence.csv"), encoding="utf-8"))}
rows = {r["id"]: r for r in v["rows"]}
conf = {c["id"]: c for c in v["confirmations"]}
real = [c for c in v["confirmations"] if c["problem_is_real"]]
print(f"- Rows checked: {len(rows)} (every row of evidence.csv at the time). First pass: {dict(Counter(r['verdict'] for r in rows.values()))}.")
print(f"- Flagged rows re-checked by a second, skeptical agent: {len(conf)}; problem confirmed: {len(real)} ({dict(Counter(c['final_verdict'] for c in real))}); not confirmed: {len(conf)-len(real)} (left unchanged).")
print(f"- Confirmed issue types: {dict(Counter(i for c in real for i in rows[c['id']]['issues']))}.")
print(f"- Confirmed problems by module: {dict(Counter(c['id'].split('-')[0] for c in real))}.")
ID = re.compile(r"\b[A-Z]+-\d{3}\b")
parts = []
for m in fx:
    if not m:
        continue
    new = sorted({x for nr in m["new_rows"] for x in ID.findall(nr.split(" ")[0] + " " + nr.split(",")[0])} - set(conf))
    parts.append(f"{m['module']} {len(m['applied'])} applied, {len(m['not_applied'])} noted, new rows {', '.join(new) or 'none'}")
print("- Fixes applied by module (fix agents): " + "; ".join(parts) + ".")
print("- CANNOT OPEN: " + str(sum(1 for r in rows.values() if r["verdict"] == "CANNOT OPEN")) + ".")
print("")
print("### The 15 most important rows (review packet claims): result of the self-check")
print("")
print("| Id | First pass | Second check | Wording found by the checker (excerpt) | Tag after fixes |")
print("|---|---|---|---|---|")
src = open(os.path.join(C, "build_review_packet.py"), encoding="utf-8").read()
ids = re.findall(r'\("((?:PAPM|PAPL|TALK|XR|SMP|AW)-\d{3})", "', src.split("INFER")[0])
for i in ids:
    r = rows.get(i, {}); c = conf.get(i)
    sec = "-" if not c else (f"confirmed {c['final_verdict']}" if c["problem_is_real"] else "not confirmed (row kept)")
    fw = (c["found_wording"] if c else r.get("found_wording", ""))[:150].replace("|", "/").replace("\n", " ")
    print(f"| {i} | {r.get('verdict','?')} | {sec} | {fw} | {ev[i]['tag']} |")
