#!/usr/bin/env python3
"""A1 - Results: quarterly and annual P&L arithmetic for Advantest (TSE 6857), IFRS, JPY.
Fiscal year ends 31 March; FY2025 = Apr 2025-Mar 2026.
Computes: margins (recomputed vs printed), YoY growth per quarter and full year, single-quarter values
re-derived from YTD tanshin figures (cross-check), Q4 basic EPS by YTD difference, core operating income
per quarter (company definition: operating income excluding other income and expenses), LTM figures.
All inputs are hard-coded with their evidence ids (research/out/advantest/parts/A1.csv).
Run: python3 -I A1_pnl.py > A1_pnl.out.txt
"""

def pct(a, b):
    return 100.0 * a / b


def yoy(cur, prev):
    return 100.0 * (cur / prev - 1.0)


# ---- single-quarter P&L from briefing slides (JPY billion) ----
# key: (sales, gross profit, operating income, income before tax, net income attributable)
Q = {
    "FY2024 Q3 (Oct-Dec 2024)": (218.2, 118.9, 69.2, 70.6, 51.9),     # A1-069, A1-070, A1-072, A1-074, A1-075
    "FY2024 Q4 (Jan-Mar 2025)": (232.3, 139.2, 64.1, 61.6, 40.0),     # A1-076, A1-077, A1-079, A1-081, A1-082
    "FY2025 Q1 (Apr-Jun 2025)": (263.8, 171.6, 124.0, 121.4, 90.2),   # A1-025, A1-026, A1-028, A1-030, A1-031
    "FY2025 Q2 (Jul-Sep 2025)": (262.9, 163.7, 108.4, 109.1, 79.6),   # A1-032, A1-033, A1-035, A1-037, A1-038
    "FY2025 Q3 (Oct-Dec 2025)": (273.8, 169.7, 113.6, 113.8, 78.7),   # A1-039, A1-040, A1-042, A1-044, A1-045
    "FY2025 Q4 (Jan-Mar 2026)": (328.1, 221.1, 153.1, 172.4, 126.9),  # A1-046, A1-047, A1-049, A1-051, A1-052
    "FY2026 Q1 (Apr-Jun 2026)": (367.5, 255.6, 190.0, 234.1, 174.8),  # A1-053, A1-054, A1-056, A1-058, A1-059
    "FY2026 Q2 (Jul-Sep 2026)": (477.7, 339.8, 266.8, 276.2, 193.3),  # A1-060, A1-061, A1-063, A1-065, A1-066
}
# printed margins (%): gross, operating
PRINTED = {
    "FY2024 Q3 (Oct-Dec 2024)": (54.5, 31.8),  # A1-071, A1-073
    "FY2024 Q4 (Jan-Mar 2025)": (59.9, 27.6),  # A1-078, A1-080
    "FY2025 Q1 (Apr-Jun 2025)": (65.1, 47.0),  # A1-027, A1-029
    "FY2025 Q2 (Jul-Sep 2025)": (62.2, 41.3),  # A1-034, A1-036
    "FY2025 Q3 (Oct-Dec 2025)": (62.0, 41.5),  # A1-041, A1-043
    "FY2025 Q4 (Jan-Mar 2026)": (67.4, 46.7),  # A1-048, A1-050
    "FY2026 Q1 (Apr-Jun 2026)": (69.5, 51.7),  # A1-055, A1-057
    "FY2026 Q2 (Jul-Sep 2026)": (71.1, 55.9),  # A1-062, A1-064
}
# single-quarter basic EPS (JPY) as printed by the company
EPS = {
    "FY2024 Q3 (Oct-Dec 2024)": 70.30,   # A1-089
    "FY2025 Q1 (Apr-Jun 2025)": 123.14,  # A1-086
    "FY2025 Q2 (Jul-Sep 2025)": 109.03,  # A1-087
    "FY2025 Q3 (Oct-Dec 2025)": 108.37,  # A1-088
    "FY2026 Q1 (Apr-Jun 2026)": 241.27,  # A1-085
    "FY2026 Q2 (Jul-Sep 2026)": 267.75,  # A1-084
}
# YTD basic EPS (JPY)
EPS_FY25, EPS_9M25 = 515.15, 340.60   # A1-020, A1-090
EPS_FY24, EPS_9M24 = 218.67, 164.21   # A1-021, A1-091

print("=== 1. Single-quarter margins recomputed from slide values (JPY bn) vs printed ===")
for k, (s, g, o, i, n) in Q.items():
    gm, om, nm = pct(g, s), pct(o, s), pct(n, s)
    pg, po = PRINTED[k]
    print(f"{k}: sales {s:.1f}  GM {gm:.1f}% (printed {pg}%)  OM {om:.1f}% (printed {po}%)  IBT margin {pct(i, s):.1f}%  NI margin {nm:.1f}%")

print("\n=== 2. YoY growth, last four quarters vs year-earlier quarter ===")
# Primary basis (verified 2026-11-21): single quarters in JPY million derived from the YTD tanshin statements,
# because YoY computed on slide figures rounded to JPY 0.1 bn can differ from the company's printed YoY by 0.1-0.3 pts.
# YTD inputs (sales, gross profit, operating income, income before tax, net income attributable), JPY million
YTDM = {
    "1H FY2024": (329206, 186997, 94859, 92645, 69343),       # A1-322, A1-323, A1-229, A1-486, A1-487
    "9M FY2024": (547358, 305851, 164126, 163192, 121210),    # A1-482, A1-483, A1-228, A1-484, A1-485
    "FY2024": (779707, 445085, 228161, 224774, 161177),       # A1-002, A1-006, A1-014, A1-017, A1-019
    "Q1 FY2025": (263776, 171638, 123952, 121357, 90180),     # A1-324, A1-335, A1-325, A1-336, A1-488
    "1H FY2025": (526733, 335279, 232435, 230517, 169813),    # A1-102, A1-103, A1-104, A1-105, A1-106
    "9M FY2025": (800537, 504987, 346006, 344349, 248526),    # A1-116, A1-117, A1-118, A1-119, A1-120
    "FY2025": (1128610, 726107, 499120, 516720, 375353),      # A1-001, A1-005, A1-013, A1-016, A1-018
    "Q1 FY2026": (367473, 255553, 189990, 234082, 174780),    # A1-107, A1-108, A1-111, A1-113, A1-114
    "1H FY2026": (845200, 595378, 456809, 510234, 368083),    # A1-094, A1-095, A1-098, A1-100, A1-101
}


def dsub(a, b):
    return tuple(x - y for x, y in zip(a, b))


QM = {
    "FY2024 Q3 (Oct-Dec 2024)": dsub(YTDM["9M FY2024"], YTDM["1H FY2024"]),
    "FY2024 Q4 (Jan-Mar 2025)": dsub(YTDM["FY2024"], YTDM["9M FY2024"]),
    "FY2025 Q1 (Apr-Jun 2025)": YTDM["Q1 FY2025"],
    "FY2025 Q2 (Jul-Sep 2025)": dsub(YTDM["1H FY2025"], YTDM["Q1 FY2025"]),
    "FY2025 Q3 (Oct-Dec 2025)": dsub(YTDM["9M FY2025"], YTDM["1H FY2025"]),
    "FY2025 Q4 (Jan-Mar 2026)": dsub(YTDM["FY2025"], YTDM["9M FY2025"]),
    "FY2026 Q1 (Apr-Jun 2026)": YTDM["Q1 FY2026"],
    "FY2026 Q2 (Jul-Sep 2026)": dsub(YTDM["1H FY2026"], YTDM["Q1 FY2026"]),
}
print("2a. Single quarters, JPY million (YTD differencing), vs slide figures (JPY bn):")
for k, t in QM.items():
    sl = Q[k]
    print(f"  {k}: sales {t[0]:,} (slide {sl[0]}); GP {t[1]:,} (slide {sl[1]}); OI {t[2]:,} (slide {sl[2]}); "
          f"IBT {t[3]:,} (slide {sl[3]}); NI {t[4]:,} (slide {sl[4]}); GM {pct(t[1], t[0]):.2f}%; OM {pct(t[2], t[0]):.2f}%")
pairs = [("FY2025 Q3 (Oct-Dec 2025)", "FY2024 Q3 (Oct-Dec 2024)"),
         ("FY2025 Q4 (Jan-Mar 2026)", "FY2024 Q4 (Jan-Mar 2025)"),
         ("FY2026 Q1 (Apr-Jun 2026)", "FY2025 Q1 (Apr-Jun 2025)"),
         ("FY2026 Q2 (Jul-Sep 2026)", "FY2025 Q2 (Jul-Sep 2025)")]
names = ["sales", "gross profit", "operating income", "income before tax", "net income"]
# Q4 EPS by YTD difference (approximation: share counts differ between periods)
EPS["FY2025 Q4 (Jan-Mar 2026)"] = EPS_FY25 - EPS_9M25
EPS["FY2024 Q4 (Jan-Mar 2025)"] = EPS_FY24 - EPS_9M24
print("2b. YoY on JPY million single quarters (primary):")
for cur, prev in pairs:
    c, p = QM[cur], QM[prev]
    parts = [f"{names[j]} {yoy(c[j], p[j]):+.1f}%" for j in range(5)]
    eps_txt = f"basic EPS {EPS[cur]:.2f} vs {EPS[prev]:.2f} = {yoy(EPS[cur], EPS[prev]):+.1f}%"
    gm_chg = pct(c[1], c[0]) - pct(p[1], p[0])
    om_chg = pct(c[2], c[0]) - pct(p[2], p[0])
    print(f"  {cur} vs {prev}: " + "; ".join(parts) + f"; {eps_txt}; GM change {gm_chg:+.1f} pts; OM change {om_chg:+.1f} pts")
print("2c. YoY on slide figures rounded to JPY 0.1 bn (secondary, for comparison only):")
for cur, prev in pairs:
    c, p = Q[cur], Q[prev]
    print(f"  {cur}: " + "; ".join(f"{names[j]} {yoy(c[j], p[j]):+.1f}%" for j in range(5)))
print("2d. Company-printed YoY: FY2026 Q2 sales +81.7% (A1-067), GP +107.7% (A1-499), OI +146.0% (A1-068), NI +142.7% (A1-500); "
      "FY2025 Q4 sales +41.2% (A1-083), OI +139.1% (A1-501), NI +217.3% (A1-502)")
print(f"Derived Q4 basic EPS (FY minus 9M, approximate): FY2025 Q4 {EPS_FY25 - EPS_9M25:.2f}; FY2024 Q4 {EPS_FY24 - EPS_9M24:.2f}")

print("\n=== 3. Full year FY2025 (Apr 2025-Mar 2026) vs FY2024, JPY million ===")
FY25 = dict(sales=1128610, cogs=402503, gp=726107, sga=229628, oinc=3552, oexp=911, oi=499120, ibt=516720, ni=375353)  # A1-001,003,005,007,009,011,013,016,018
FY24 = dict(sales=779707, cogs=334622, gp=445085, sga=195392, oinc=1366, oexp=22898, oi=228161, ibt=224774, ni=161177)  # A1-002,004,006,008,010,012,014,017,019
for k in ["sales", "gp", "oi", "ibt", "ni"]:
    print(f"{k}: FY2025 {FY25[k]:,} vs FY2024 {FY24[k]:,}  YoY {yoy(FY25[k], FY24[k]):+.1f}%")
print(f"basic EPS: {EPS_FY25} vs {EPS_FY24}  YoY {yoy(EPS_FY25, EPS_FY24):+.1f}%")
for lbl, d in [("FY2025", FY25), ("FY2024", FY24)]:
    print(f"{lbl}: GM {pct(d['gp'], d['sales']):.1f}%  OM {pct(d['oi'], d['sales']):.1f}%  IBT margin {pct(d['ibt'], d['sales']):.1f}%  NI margin {pct(d['ni'], d['sales']):.1f}%")
    core = d["oi"] - (d["oinc"] - d["oexp"])
    print(f"{lbl}: core operating income (company definition, OI ex other income/expenses) {core:,} = {pct(core, d['sales']):.1f}% of sales")
# check: sum of FY2025 quarters (slides) vs annual (tanshin)
s4 = [Q[k] for k in ["FY2025 Q1 (Apr-Jun 2025)", "FY2025 Q2 (Jul-Sep 2025)", "FY2025 Q3 (Oct-Dec 2025)", "FY2025 Q4 (Jan-Mar 2026)"]]
print("Check sum of FY2025 quarters (bn): sales %.1f, GP %.1f, OI %.1f, NI %.1f" % tuple(sum(x[j] for x in s4) for j in (0, 1, 2, 4)))

print("\n=== 4. Single quarters re-derived from YTD tanshin statements (JPY million), cross-check of slides ===")
H26 = dict(sales=845200, gp=595378, oi=456809, ibt=510234, ni=368083)   # A1-094, A1-095, A1-098, A1-100, A1-101
Q126 = dict(sales=367473, gp=255553, oi=189990, ibt=234082, ni=174780)  # A1-107, A1-108, A1-111, A1-113, A1-114
H25 = dict(sales=526733, gp=335279, oi=232435, ibt=230517, ni=169813)   # A1-102, A1-103, A1-104, A1-105, A1-106
N25 = dict(sales=800537, gp=504987, oi=346006, ibt=344349, ni=248526)   # A1-116, A1-117, A1-118, A1-119, A1-120
for lbl, a, b in [("FY2026 Q2 = 1H FY2026 - Q1 FY2026", H26, Q126), ("FY2025 Q3 = 9M FY2025 - 1H FY2025", N25, H25),
                  ("FY2025 Q4 = FY2025 - 9M FY2025", FY25, N25)]:
    d = {k: a[k] - b[k] for k in ["sales", "gp", "oi", "ibt", "ni"]}
    print(f"{lbl}: sales {d['sales']:,}; GP {d['gp']:,} (GM {pct(d['gp'], d['sales']):.2f}%); OI {d['oi']:,} (OM {pct(d['oi'], d['sales']):.2f}%); IBT {d['ibt']:,}; NI {d['ni']:,}")

print("\n=== 5. Core operating income per quarter (company definition applied by us) ===")
OIE = {"FY2025 Q1 (Apr-Jun 2025)": 2.9, "FY2025 Q2 (Jul-Sep 2025)": 0.1,
       "FY2025 Q3 (Oct-Dec 2025)": 0.1, "FY2025 Q4 (Jan-Mar 2026)": -0.5}  # A1-121 (JPY bn)
for k, v in OIE.items():
    s, g, o, i, n = Q[k]
    print(f"{k}: core OI {o - v:.1f} bn, core OM {pct(o - v, s):.1f}% (reported OM {pct(o, s):.1f}%)")
oie_q1_26 = 796 - 112            # A1-109, A1-110 (JPY million)
oie_1h_26 = 1120 - 199           # A1-096, A1-097
core_q1 = 189990 - oie_q1_26     # A1-111
core_q2 = (456809 - oie_1h_26) - core_q1  # A1-098
print(f"FY2026 Q1 (Apr-Jun 2026): core OI {core_q1:,} million, core OM {pct(core_q1, 367473):.1f}%")
print(f"FY2026 Q2 (Jul-Sep 2026): core OI {core_q2:,} million, core OM {pct(core_q2, 845200 - 367473):.1f}% (other income - expenses in Q2 = {oie_1h_26 - oie_q1_26:,} million)")

print("\n=== 6. LTM = FY2025 Q3 to FY2026 Q2 (Oct 2025-Sep 2026), JPY million ===")
H24 = dict(sales=329206, gp=186997, oi=94859)  # A1-322, A1-323, A1-229
ltm = {k: FY25[k] + H26[k] - H25[k] for k in ["sales", "gp", "oi", "ibt", "ni"]}
ltm_prev = {k: FY24[k] + H25[k] - H24[k] for k in ["sales", "gp", "oi"]}
print(f"LTM sales {ltm['sales']:,}; prior LTM (Oct 2024-Sep 2025) {ltm_prev['sales']:,}; YoY {yoy(ltm['sales'], ltm_prev['sales']):+.1f}%")
print(f"LTM gross profit {ltm['gp']:,} (GM {pct(ltm['gp'], ltm['sales']):.1f}%); LTM operating income {ltm['oi']:,} (OM {pct(ltm['oi'], ltm['sales']):.1f}%)")
print(f"LTM income before tax {ltm['ibt']:,} ({pct(ltm['ibt'], ltm['sales']):.1f}% of sales); LTM net income attributable {ltm['ni']:,} ({pct(ltm['ni'], ltm['sales']):.1f}%)")
CALL, VAL_1H = 17312, 54171  # A1-309 (recognised FY2025 Q4, inside the LTM window), A1-313 (1H FY2026)
print(f"LTM income before tax ex call-option gain {ltm['ibt'] - CALL:,} ({pct(ltm['ibt'] - CALL, ltm['sales']):.1f}%); "
      f"ex call-option gain and 1H FY2026 valuation gains {ltm['ibt'] - CALL - VAL_1H:,} ({pct(ltm['ibt'] - CALL - VAL_1H, ltm['sales']):.1f}%)")
print("LTM operating income / gross profit ex one-offs: not computable (FY2025 Q4 one-off SG&A and FY2026 Q1/1H inventory write-down reversal have no disclosed amount); "
      "FY2025 Q1 divestiture gain (2,504) falls outside the LTM window")
print(f"Prior LTM GM {pct(ltm_prev['gp'], ltm_prev['sales']):.1f}%; prior LTM OM {pct(ltm_prev['oi'], ltm_prev['sales']):.1f}%")
q4 = sum(Q[k][0] for k, _ in pairs)
print(f"Check: sum of four single quarters from slides = {sum(Q[c][0] for c, _ in pairs):.1f} bn")

print("\n=== 7. 1H FY2026 (Apr-Sep 2026) operating margin (fix round 1, 2026-11-21) ===")
# A1-098 operating income 456,809 and A1-094 / CL-032 net sales 845,200, six months to 30 Sep 2026 (JPY million)
print(f"1H FY2026 operating margin = {H26['oi']:,} / {H26['sales']:,} = {pct(H26['oi'], H26['sales']):.2f}% "
      "(includes the inventory write-down reversal named for 1H, amount not disclosed)")

print("\n=== 8. FY2024 (Apr 2024-Mar 2025) vs FY2023 (Apr 2023-Mar 2024), JPY million (fix round 2, 2026-11-21) ===")
# FY2023 actuals: A3-032 net sales 486,507; A3-033 operating income 81,628; A3-035 net income 62,290 (FY2023 tanshin p.1)
# FY2024 actuals: A1-002 779,707; A1-014 228,161; A1-019 161,177. Printed FY2024 YoY (FY2024 tanshin p.1): A1-518, A1-519, A1-520
FY23 = dict(sales=486507, oi=81628, ni=62290)
PRINTED_FY24 = dict(sales=60.3, oi=179.5, ni=158.8)
for k in ["sales", "oi", "ni"]:
    v = yoy(FY24[k], FY23[k])
    print(f"{k}: FY2024 {FY24[k]:,} vs FY2023 {FY23[k]:,}  YoY {v:+.1f}% (printed {PRINTED_FY24[k]:+.1f}%; "
          f"{'agrees' if round(v, 1) == PRINTED_FY24[k] else 'DIFFERS'})")
