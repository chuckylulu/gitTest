"""A4: China share of KLA revenue by quarter, Q1 FY24 (Jul-Sep 2023) .. Q1 FY27 (Jul-Sep 2026),
plus a 'first reported vs next-year comparative' restatement check for every region.
Input: a4_region_tables.json (written by a4_region_parse.py from the saved 10-Q/10-K text; the
first geography table in each file = the Note 'Segment Reporting and Geographic Information').
Q4 values = fiscal-year (10-K) minus nine months (Q3 10-Q). $ thousands."""
import json, pathlib
here = pathlib.Path(__file__).resolve().parent
T = json.load(open(here / "a4_region_tables.json"))
note = {fn: tabs[0]["amounts"] for fn, tabs in T.items() if tabs}
Q = {  # quarter -> (file, column index of 3-month current period)
 "Q1FY24": "2023-10-26_kla_10-Q-Q1FY24.txt", "Q2FY24": "2024-01-26_kla_10-Q-Q2FY24.txt",
 "Q3FY24": "2024-04-26_kla_10-Q-Q3FY24.txt", "Q1FY25": "2024-10-31_kla_10-Q-Q1FY25.txt",
 "Q2FY25": "2025-01-31_kla_10-Q-Q2FY25.txt", "Q3FY25": "2025-05-01_kla_10-Q-Q3FY25.txt",
 "Q1FY26": "2025-10-30_kla_10-Q-Q1FY26.txt", "Q2FY26": "2026-01-30_kla_10-Q-Q2FY26.txt",
 "Q3FY26": "2026-04-30_kla_10-Q-Q3FY26.txt", "Q1FY27": "2026-10-29_kla_10-Q-Q1FY27.txt"}
K = {"FY24": "2024-08-05_kla_10-K-FY24.txt", "FY25": "2025-08-07_kla_10-K-FY25.txt",
     "FY26": "2026-08-06_kla_10-K-FY26.txt"}
CAL = {"Q1FY24":"Jul-Sep 2023","Q2FY24":"Oct-Dec 2023","Q3FY24":"Jan-Mar 2024","Q4FY24":"Apr-Jun 2024",
 "Q1FY25":"Jul-Sep 2024","Q2FY25":"Oct-Dec 2024","Q3FY25":"Jan-Mar 2025","Q4FY25":"Apr-Jun 2025",
 "Q1FY26":"Jul-Sep 2025","Q2FY26":"Oct-Dec 2025","Q3FY26":"Jan-Mar 2026","Q4FY26":"Apr-Jun 2026",
 "Q1FY27":"Jul-Sep 2026"}
regions = list(note[Q["Q1FY27"]].keys())
def q(qq, r):
    if qq.startswith("Q4"):
        fy = qq[2:]; nine = note[Q["Q3" + fy]][r][2]   # col 2 = nine months current
        return note[K[fy]][r][0] - nine
    return note[Q[qq]][r][0]
order = list(CAL)
rows = {}
print("quarter,calendar,china_k,total_k,china_share_pct,china_qoq_pct,china_yoy_pct")
for i, qq in enumerate(order):
    c, t = q(qq, "China"), q(qq, "Total")
    rows[qq] = (c, t)
    qoq = (c / rows[order[i-1]][0] - 1) * 100 if i else float("nan")
    yoy = (c / rows[order[i-4]][0] - 1) * 100 if i >= 4 else float("nan")
    print(f"{qq},{CAL[qq]},{c},{t},{c/t*100:.1f},{qoq:.1f},{yoy:.1f}")
# fiscal-year China shares
for fy, fn in K.items():
    print(f"{fy} China share = {note[fn]['China'][0]/note[fn]['Total'][0]*100:.1f}% ({note[fn]['China'][0]} / {note[fn]['Total'][0]})")
print("FY23 China share (FY24 10-K comparative) = %.1f%%" % (note[K['FY24']]['China'][1]/note[K['FY24']]['Total'][1]*100))
# last 4 quarters regional mix
print("\nRegion mix, last 4 quarters ($k, share %)")
for qq in ["Q2FY26","Q3FY26","Q4FY26","Q1FY27"]:
    t = q(qq, "Total")
    print(qq, CAL[qq], "; ".join(f"{r} {q(qq,r)} ({q(qq,r)/t*100:.1f}%)" for r in regions if r != "Total"))
ltm = {r: sum(q(x, r) for x in ["Q2FY26","Q3FY26","Q4FY26","Q1FY27"]) for r in regions}
print("LTM Q2FY26-Q1FY27:", "; ".join(f"{r} {v} ({v/ltm['Total']*100:.1f}%)" for r, v in ltm.items()))
# restatement check: quarter as first reported vs prior-year column of the next year's 10-Q
print("\nRestatement check (first reported vs next-year comparative), all regions")
nxt = {"Q1FY24":"Q1FY25","Q2FY24":"Q2FY25","Q3FY24":"Q3FY25","Q1FY25":"Q1FY26","Q2FY25":"Q2FY26",
       "Q3FY25":"Q3FY26","Q1FY26":"Q1FY27"}
diffs = 0
for a, b in nxt.items():
    for r in regions:
        first = note[Q[a]][r][0]; comp = note[Q[b]][r][1]
        if first != comp:
            diffs += 1; print("  DIFF", a, r, first, comp)
print("  quarterly pairs checked:", len(nxt), "x", len(regions), "regions; differences:", diffs)
for a, b in [("FY24","FY25"),("FY25","FY26")]:
    for r in regions:
        if note[K[a]][r][0] != note[K[b]][r][1]:
            diffs += 1; print("  DIFF", a, r)
    print(f"  {a} as first reported vs {b} 10-K comparative: checked")
for r in regions:
    if note[K['FY24']][r][0] != note[K['FY26']][r][2] or note[K['FY24']][r][1] != note["2023-08-04_kla_10-K-FY23.txt"][r][0]:
        diffs += 1; print("  DIFF FY24/FY23 three-way", r)
print("  total differences found:", diffs)

# Calendar-year China totals (KLA quarters mapped to calendar quarters)
print("\nCalendar-year China revenue and share")
CY = {"CY2024": ["Q3FY24","Q4FY24","Q1FY25","Q2FY25"], "CY2025": ["Q3FY25","Q4FY25","Q1FY26","Q2FY26"],
      "CY2026 9M (Jan-Sep)": ["Q3FY26","Q4FY26","Q1FY27"]}
cyv = {}
for k, qs in CY.items():
    c = sum(rows[x][0] for x in qs); t = sum(rows[x][1] for x in qs); cyv[k] = (c, t)
    print(f"{k}: China {c} / total {t} = {c/t*100:.1f}%")
print(f"CY2025 vs CY2024 China revenue change: {(cyv['CY2025'][0]/cyv['CY2024'][0]-1)*100:.1f}%")
c9_25 = sum(rows[x][0] for x in ["Q3FY25","Q4FY25","Q1FY26"])
print(f"CY2026 9M vs CY2025 9M China revenue change: {(cyv['CY2026 9M (Jan-Sep)'][0]/c9_25-1)*100:.1f}%")
# What Q4 CY2026 (Q2 FY27) China share would put CY2026 at 'high-20s' (27-29%)? Uses guidance midpoint $4.70B (Q1 FY27 letter)
g = 4_700_000
c9, t9 = cyv['CY2026 9M (Jan-Sep)']
for s in (0.25, 0.27, 0.29):
    print(f"If Q2FY27 China share = {s:.0%} on $4.70B guide midpoint -> CY2026 China share = {(c9+s*g)/(t9+g)*100:.1f}%")

# Pre-surge baseline: China share FY21-FY23 from FY23 10-K note (columns 2023, 2022, 2021)
k23 = note["2023-08-04_kla_10-K-FY23.txt"]
for i, fy in enumerate(["FY23", "FY22", "FY21"]):
    print(f"{fy} China share = {k23['China'][i]/k23['Total'][i]*100:.1f}% ({k23['China'][i]} / {k23['Total'][i]})")
t9_25 = sum(rows[x][1] for x in ["Q3FY25","Q4FY25","Q1FY26"])
print(f"CY2026 9M vs CY2025 9M total revenue change: {(cyv['CY2026 9M (Jan-Sep)'][1]/t9_25-1)*100:.1f}%")
# Q4 FY24 letter rounding check (letter: China 44%)
print(f"Q4FY24 derived China share {rows['Q4FY24'][0]/rows['Q4FY24'][1]*100:.2f}% vs letter 44%")
