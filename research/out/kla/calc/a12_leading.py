#!/usr/bin/env python3
"""A2 leading-signal calculations for KLA (KLAC). FY ends June 30. USD thousands unless noted.

Sources (research/sources/kla/):
  Balance sheets: earnings releases Q2 FY26 (Dec 31, 2025), Q3 FY26 (Mar 31, 2026), Q1 FY27 (Sep 30, 2026 and Jun 30, 2026);
                  Jun 30, 2025 comparatives in the Q2 FY26 release.
  Inventory split: Note 4 of 10-Q Q2 FY26, 10-Q Q3 FY26, 10-Q Q1 FY27 (incl. Jun 30, 2026), 10-K FY26 (Jun 30, 2025).
  Contract liabilities and timing: Note 2 of 10-Q Q2 FY26, Q3 FY26, Q1 FY27 and 10-K FY26 Note 2.
  Customer deposits: Note 4 'Other current / non-current liabilities'.
  Purchase commitments: Commitments note (10-Q Q2 FY26 $2.75B; Q3 FY26 $4.83B; 10-K FY26 $5.97B; 10-Q Q1 FY27 $8.87B).
  Backlog: 10-K FY25 Item 1 ($9.83B Jun-24 -> $7.86B Jun-25), 10-K FY26 Item 1 ($7.86B -> $12.57B Jun-26).
DSO method: ending net trade AR / quarterly revenue x days in quarter (calendar days). Long-term AR excluded (shown separately).
"""
from datetime import date

P = ["Jun25", "Dec25", "Mar26", "Jun26", "Sep26"]
DAYS = {"Dec25": 92, "Mar26": 90, "Jun26": 91, "Sep26": 92}
REV = {"Dec25": 3297146, "Mar26": 3415078, "Jun26": 3657556, "Sep26": 4136015}
COGS = {"Dec25": 1271210, "Mar26": 1327672, "Jun26": 1413108, "Sep26": 1577791}
AR = {"Jun25": 2263915, "Dec25": 2073581, "Mar26": 2304454, "Jun26": 2889208, "Sep26": 3072087}
LTAR = {"Jun25": 0, "Dec25": 0, "Mar26": 0, "Jun26": 180729, "Sep26": 266755}
INV = {  # customer service parts, raw, WIP, finished goods
    "Jun25": (600769, 1491786, 833933, 285661),
    "Dec25": (625503, 1568734, 836166, 252202),
    "Mar26": (602543, 1648430, 929604, 256469),
    "Jun26": (622714, 1849676, 937724, 238424),
    "Sep26": (639024, 2126927, 1076942, 247533),
}
INV_TOT = {"Jun25": 3212149, "Dec25": 3282605, "Mar26": 3437046, "Jun26": 3648538, "Sep26": 4090426}
# deferred system rev (current), deferred service rev current, deferred service rev non-current
DEF = {
    "Jun25": (816834, 548011, 348844),
    "Dec25": (858088, 599254, 270549),
    "Mar26": (620839, 576503, 251563),
    "Jun26": (932901, 604127, 238111),
    "Sep26": (843008, 634232, 230562),
}
CL = {"Jun25": 1713689, "Dec25": 1727891, "Mar26": 1448905, "Jun26": 1775139, "Sep26": 1707802}
CL_TIMING = {  # <12m, 12-24m, >=24m
    "Dec25": (1457342, 183822, 86727), "Mar26": (1197342, 170588, 80975),
    "Jun26": (1537028, 163356, 74755), "Sep26": (1477240, 167971, 62591)}
DEPOSITS = {  # customer deposits current, non-current (Other liabilities, Note 4)
    "Jun25": (636369, 6823), "Dec25": (363121, 7467), "Mar26": (411202, 9653),
    "Jun26": (430128, 3816), "Sep26": (493816, 13960)}
PURCH = {"Dec25": 2.75, "Mar26": 4.83, "Jun26": 5.97, "Sep26": 8.87}  # $B
FACTORED = {"Dec25": 70425, "Mar26": 109405, "Sep26": 31670}  # receivables sold in quarter ($K); Q4 FY26 = FY26 - 9M
FACTORED["Jun26"] = 515480 - 286197
BACKLOG = {"Jun24": 9.83, "Jun25": 7.86, "Jun26": 12.57}  # $B, annual only

print("Inventory ($M): service parts / raw / WIP / FG / total ; check")
for p in P:
    s = sum(INV[p])
    print(f"  {p}: " + " / ".join(f"{x/1e3:,.1f}" for x in INV[p]) + f" / {s/1e3:,.1f}  {'OK' if s == INV_TOT[p] else 'MISMATCH'}")
for i, lab in enumerate(["service parts", "raw", "WIP", "FG", "total"]):
    a = INV["Sep26"][i] if i < 4 else INV_TOT["Sep26"]
    b = INV["Sep26".replace('Sep26', 'Sep26')][i] if False else (INV["Jun25"][i] if i < 4 else INV_TOT["Jun25"])
    c = INV["Jun26"][i] if i < 4 else INV_TOT["Jun26"]
    print(f"  {lab}: Sep26 vs Jun25 {100*(a-b)/b:+.1f}% ; Sep26 vs Jun26 (QoQ) {100*(a-c)/c:+.1f}%")
for p in ["Dec25", "Mar26", "Jun26", "Sep26"]:
    print(f"  {p}: raw share of inventory {100*INV[p][1]/INV_TOT[p]:.1f}%; inventory days (end inv / qtr COGS x days) {INV_TOT[p]/COGS[p]*DAYS[p]:.0f}")

print("\nReceivables and DSO")
for p in ["Dec25", "Mar26", "Jun26", "Sep26"]:
    dso = AR[p] / REV[p] * DAYS[p]
    dso_lt = (AR[p] + LTAR[p]) / REV[p] * DAYS[p]
    print(f"  {p}: AR {AR[p]/1e3:,.1f} $M, LT AR {LTAR[p]/1e3:,.1f} $M, DSO {dso:.1f} days (incl. LT AR {dso_lt:.1f}); factored in qtr {FACTORED[p]/1e3:,.1f} $M")

print("\nContract liabilities (= deferred system + deferred service revenue) and timing")
for p in P:
    s = sum(DEF[p])
    line = f"  {p}: def system {DEF[p][0]/1e3:,.1f}, def service {(DEF[p][1]+DEF[p][2])/1e3:,.1f}, total {s/1e3:,.1f} ({'OK' if s == CL[p] else 'MISMATCH vs ' + str(CL[p])})"
    if p in CL_TIMING:
        t = CL_TIMING[p]
        line += f"; <12m {100*t[0]/sum(t):.1f}% ({'OK' if sum(t) == CL[p] else 'MISMATCH'})"
    print(line)
print("\nCustomer deposits ($M current + non-current)")
for p in P:
    print(f"  {p}: {sum(DEPOSITS[p])/1e3:,.1f}")
print("\nPurchase commitments ($B) and change")
prev = None
for p in ["Dec25", "Mar26", "Jun26", "Sep26"]:
    print(f"  {p}: {PURCH[p]:.2f}" + (f" ({100*(PURCH[p]-prev)/prev:+.0f}% QoQ)" if prev else ""))
    prev = PURCH[p]
print(f"  Sep26 purchase commitments / LTM COGS: {PURCH['Sep26']*1e6/sum(COGS.values()):.2f}x")
print("\nBacklog ($B, fiscal year-end only)")
print(f"  Jun24 {BACKLOG['Jun24']} -> Jun25 {BACKLOG['Jun25']} ({100*(BACKLOG['Jun25']-BACKLOG['Jun24'])/BACKLOG['Jun24']:+.1f}%) -> Jun26 {BACKLOG['Jun26']} ({100*(BACKLOG['Jun26']-BACKLOG['Jun25'])/BACKLOG['Jun25']:+.1f}%)")
fy26_rev = 13.579476
print(f"  Implied FY26 orders proxy = FY26 revenue + change in backlog = {fy26_rev + BACKLOG['Jun26'] - BACKLOG['Jun25']:.2f} $B; "
      f"implied book-to-bill {(fy26_rev + BACKLOG['Jun26'] - BACKLOG['Jun25'])/fy26_rev:.2f} (ignores cancellations, FX, scope of backlog vs revenue)")
print(f"  Backlog Jun26 / FY26 revenue: {BACKLOG['Jun26']/fy26_rev:.2f}x")
