#!/usr/bin/env python3
"""A6 - accounting-basis check for the 2015-16 episode (Advantest Corporation, TSE Prime 6857; JPY million).
Fiscal year ends 31 March and is named by its start year (FY2015 = Apr 2015-Mar 2016).

Advantest first reported FY2015 under U.S. GAAP and then adopted IFRS with its FY2015 annual securities report
(transition date 1 Apr 2014). The A6 quarterly series uses only IFRS figures (FY2015 quarters = IFRS comparatives in the
FY2016 releases). This script does NOT mix the two bases. It
  1. compares the IFRS and U.S. GAAP cumulative figures for the same FY2015 periods (size of the basis gap);
  2. builds a U.S. GAAP-only quarterly series FY2014 Q1 - FY2015 Q4 and its trailing-four-quarter (T4Q) sales, to see
     whether the 2015-16 T4Q peak came before FY2015 Q4, where the IFRS-only T4Q series starts.
Inputs: constants below with the evidence id (research/out/advantest/parts/A6.csv).
Run: python3 -I research/out/advantest/calc/A6_basis_check.py > research/out/advantest/calc/A6_basis_check.out.txt
"""
# IFRS cumulative (YTD) figures, FY2015, from the FY2016 releases and the IFRS voluntary disclosure
IFRS = {"Q1": (40166, 2475),    # A6-001, A6-002
        "1H": (86347, 6677),    # A6-003, A6-004
        "9M": (116232, 6458),   # A6-005, A6-006
        "FY": (162111, 12597)}  # A6-007, A6-008
# U.S. GAAP cumulative figures, FY2015 (as first reported)
USG15 = {"Q1": (40277, 2709),    # A6-334, A6-335
         "1H": (86665, 6748),    # A6-336, A6-337
         "9M": (116648, 6162),   # A6-338, A6-339
         "FY": (162463, 11903)}  # A6-340, A6-341
# U.S. GAAP cumulative figures, FY2014 (prior-year comparatives in the FY2015 U.S. GAAP releases; FY from the FY2014 release)
USG14 = {"Q1": (36829, 2402),    # A6-342, A6-343
         "1H": (78943, 6392),    # A6-344, A6-345
         "9M": (119902, 9811),   # A6-346, A6-347
         "FY": (163329, 14619)}  # A6-187, A6-188

KEYS = ["Q1", "1H", "9M", "FY"]
QN = {"Q1": "Q1", "1H": "Q2", "9M": "Q3", "FY": "Q4"}
CAL = {2014: ["Apr-Jun 2014", "Jul-Sep 2014", "Oct-Dec 2014", "Jan-Mar 2015"],
       2015: ["Apr-Jun 2015", "Jul-Sep 2015", "Oct-Dec 2015", "Jan-Mar 2016"]}


def quarters(cum):
    out, ps, po = [], 0, 0
    for k in KEYS:
        s, o = cum[k]
        out.append((QN[k], s - ps, o - po))
        ps, po = s, o
    return out


def pct(a, b):
    return 100.0 * a / b


print("1. IFRS vs U.S. GAAP, FY2015 cumulative figures (same periods)")
for k in KEYS:
    (si, oi), (su, ou) = IFRS[k], USG15[k]
    print(f"   FY2015 {k}: sales IFRS {si:,} vs US GAAP {su:,} ({pct(si - su, su):+.1f}%); OI IFRS {oi:,} vs US GAAP {ou:,} ({oi - ou:+,})")

qi, qu = quarters(IFRS), quarters(USG15)
print("\n2. FY2015 single quarters (each basis on its own)")
for (q, s1, o1), (_, s2, o2), c in zip(qi, qu, CAL[2015]):
    print(f"   FY2015 {q} ({c}): IFRS sales {s1:,} OI {o1:,} OM {pct(o1, s1):.1f}% | US GAAP sales {s2:,} OI {o2:,} OM {pct(o2, s2):.1f}%")
for lab, q in [("IFRS", qi), ("US GAAP", qu)]:
    d = pct(q[2][1] - q[1][1], q[1][1])
    print(f"   {lab}: FY2015 Q2 -> Q3 sales {q[1][1]:,} -> {q[2][1]:,} ({d:+.1f}%); OM {pct(q[1][2], q[1][1]):.1f}% -> {pct(q[2][2], q[2][1]):.1f}%"
          f" ({pct(q[2][2], q[2][1]) - pct(q[1][2], q[1][1]):+.1f} pp)")

print("\n3. U.S. GAAP-only quarterly series FY2014 Q1 - FY2015 Q4 and T4Q net sales")
ser = [(f"FY2014 {q}", c, s, o) for (q, s, o), c in zip(quarters(USG14), CAL[2014])] + \
      [(f"FY2015 {q}", c, s, o) for (q, s, o), c in zip(qu, CAL[2015])]
t4 = []
for i, (lab, c, s, o) in enumerate(ser):
    t = sum(x[2] for x in ser[i - 3:i + 1]) if i >= 3 else None
    if t is not None:
        t4.append((lab, t))
    print(f"   {lab} ({c}): sales {s:,} OI {o:,}" + (f"   T4Q sales {t:,}" if t is not None else ""))
assert t4[0][1] == USG14["FY"][0] and t4[-1][1] == USG15["FY"][0]
pk = max(t4, key=lambda x: x[1])
after = t4[t4.index(pk):]
tr = min(after, key=lambda x: x[1])
print(f"   US GAAP T4Q peak {pk[0]} {pk[1]:,} -> lowest after it {tr[0]} {tr[1]:,}: {pct(tr[1] - pk[1], pk[1]):+.1f}% "
      f"(series ends FY2015 Q4 at {t4[-1][1]:,}; FY2016 exists only under IFRS)")
print("   Reading: on U.S. GAAP the T4Q peak came in FY2015 Q2 (Oct 2014-Sep 2015), before the first IFRS T4Q value (FY2015 Q4);"
      " the IFRS-only T4Q drawdown of 2015-16 is therefore a lower bound. The two bases are not combined here.")
