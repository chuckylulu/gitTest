#!/usr/bin/env python3
"""A6 - restatement check: does the prior-year comparative column on page 1 of each IFRS results release (FY2016-FY2026)
equal the cumulative net sales and operating income first reported for that period?
Inputs: the saved text copies research/sources/advantest/_text/*financial-results-FY20*.txt (read only; no arithmetic).
Run: python3 -I research/out/advantest/calc/A6_comparatives_check.py > research/out/advantest/calc/A6_comparatives_check.out.txt
"""
import glob, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))  # research/
TXT = os.path.join(ROOT, "sources", "advantest", "_text")
orig, comp = {}, {}
for f in sorted(glob.glob(os.path.join(TXT, "*financial-results-FY20*.txt"))):
    b = os.path.basename(f)
    if "revised" in b or "IFRS" in b:
        continue
    m = re.search(r"financial-results-FY(\d{4})(Q\d)", b)
    fy, q = int(m.group(1)), m.group(2)
    if fy < 2016:  # FY2015 releases are U.S. GAAP
        continue
    p1 = open(f, encoding="utf-8", errors="replace").read().split("\f")[0]
    for y, store in [(fy, orig), (fy - 1, comp)]:
        lab = f"FY{y}" + ("" if q == "Q4" else " " + q)
        mm = re.search(r"^\s*" + re.escape(lab) + r"\s+([\d,]+)\s+\S+\s+([\d,()]+)", p1, re.M)
        if mm:
            store[(y, q)] = (mm.group(1), mm.group(2), b)
n = diff = 0
for k in sorted(comp):
    if k in orig:
        n += 1
        same = comp[k][:2] == orig[k][:2]
        diff += (not same)
        print(f"FY{k[0]} {k[1]}: first reported sales {orig[k][0]} OI {orig[k][1]} ({orig[k][2]}) | comparative {comp[k][0]} / {comp[k][1]} ({comp[k][2]}) -> {'same' if same else 'DIFFERENT'}")
print(f"\n{n} period pairs compared; {diff} differences")
