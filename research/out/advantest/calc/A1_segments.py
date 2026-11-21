#!/usr/bin/env python3
"""A1 - Results: segment arithmetic for Advantest (TSE 6857), IFRS. Fiscal year ends 31 March.
Segments from FY2025 Q1: Test System Business; Services and Others (prior periods restated by the company).
Segment income = operating income before share-based compensation expense (company's management measure).
(1) single-quarter segment sales and segment income by YTD differencing (JPY million) and cross-check with slide chart labels;
(2) YoY of segment and sub-segment sales; (3) segment margins; (4) SoC / memory shares;
(5) 'Computing / Communications' SoC sales implied by the company's rounded application split (range, because rounded to nearest 5%).
Run: python3 -I A1_segments.py > A1_segments.out.txt
"""

def pct(a, b):
    return 100.0 * a / b


def yoy(c, p):
    return 100.0 * (c / p - 1.0)


# YTD segment data: (Test System sales, S&O sales, Test System seg income, S&O seg income, Corporate, SBC)
YTD = {
    "1H FY2024": (284575, 44631, 102308, 604, -6794, 1259),       # A1-221..225, A1-227
    "9M FY2024": (478659, 68699, 176012, 465, -10349, 2002),      # A1-216..220, A1-226
    "FY2024":    (682819, 96888, 262120, -16125, -14941, 2893),   # A1-191..195, A1-175
    "Q1 FY2025": (240554, 23222, 126925, 2706, -4616, 1063),      # A1-326..330, A1-331
    "1H FY2025": (477957, 48776, 240556, 3048, -9052, 2117),      # A1-201..205, A1-181
    "9M FY2025": (723065, 77482, 357700, 4751, -13164, 3281),     # A1-211..215, A1-183
    "FY2025":    (1019390, 109230, 518760, 8758, -23948, 4450),   # A1-186..190, A1-174
    "Q1 FY2026": (333562, 33911, 190722, 8563, -7944, 1351),      # A1-206..210, A1-182
    "1H FY2026": (770231, 74969, 455564, 20866, -16986, 2635),    # A1-196..200, A1-179
}


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


Q = {
    "FY2024 Q3 (Oct-Dec 2024)": sub(YTD["9M FY2024"], YTD["1H FY2024"]),
    "FY2024 Q4 (Jan-Mar 2025)": sub(YTD["FY2024"], YTD["9M FY2024"]),
    "FY2025 Q1 (Apr-Jun 2025)": YTD["Q1 FY2025"],
    "FY2025 Q2 (Jul-Sep 2025)": sub(YTD["1H FY2025"], YTD["Q1 FY2025"]),
    "FY2025 Q3 (Oct-Dec 2025)": sub(YTD["9M FY2025"], YTD["1H FY2025"]),
    "FY2025 Q4 (Jan-Mar 2026)": sub(YTD["FY2025"], YTD["9M FY2025"]),
    "FY2026 Q1 (Apr-Jun 2026)": YTD["Q1 FY2026"],
    "FY2026 Q2 (Jul-Sep 2026)": sub(YTD["1H FY2026"], YTD["Q1 FY2026"]),
}
# slide chart labels (JPY bn): Test Systems, Services & Others, SoC, Memory, Other systems, Support services, Others
CH = {
    "FY2024 Q3 (Oct-Dec 2024)": (194.1, 24.1, 113.0, 54.6, 26.5, 13.9, 10.2),  # A1-231..237
    "FY2024 Q4 (Jan-Mar 2025)": (204.1, 28.2, 148.8, 35.1, 20.2, 14.3, 13.9),  # A1-238..244
    "FY2025 Q1 (Apr-Jun 2025)": (240.6, 23.2, 191.3, 33.5, 15.8, 13.9, 9.3),   # A1-245..251
    "FY2025 Q2 (Jul-Sep 2025)": (237.4, 25.6, 173.7, 43.9, 19.8, 15.4, 10.2),  # A1-252..258
    "FY2025 Q3 (Oct-Dec 2025)": (245.1, 28.7, 165.2, 57.3, 22.6, 17.1, 11.6),  # A1-259..265
    "FY2025 Q4 (Jan-Mar 2026)": (296.3, 31.7, 237.2, 36.8, 22.3, 18.6, 13.1),  # A1-266..272
    "FY2026 Q1 (Apr-Jun 2026)": (333.6, 33.9, 259.6, 48.0, 26.0, 20.3, 13.6),  # A1-273..279
    "FY2026 Q2 (Jul-Sep 2026)": (436.7, 41.1, 353.3, 53.4, 29.9, 25.6, 15.5),  # A1-280..286
}
TOTAL_SALES_BN = {  # A1-069, A1-076, A1-025, A1-032, A1-039, A1-046, A1-053, A1-060
    "FY2024 Q3 (Oct-Dec 2024)": 218.2, "FY2024 Q4 (Jan-Mar 2025)": 232.3, "FY2025 Q1 (Apr-Jun 2025)": 263.8,
    "FY2025 Q2 (Jul-Sep 2025)": 262.9, "FY2025 Q3 (Oct-Dec 2025)": 273.8, "FY2025 Q4 (Jan-Mar 2026)": 328.1,
    "FY2026 Q1 (Apr-Jun 2026)": 367.5, "FY2026 Q2 (Jul-Sep 2026)": 477.7}

print("=== 1. Single-quarter segment figures (JPY million; YTD differencing) and chart cross-check ===")
for k, t in Q.items():
    ts, so, tsi, soi, corp, sbc = t
    c = CH[k]
    oi = tsi + soi + corp - sbc
    print(f"{k}: Test System sales {ts:,} (chart {c[0]} bn), S&O sales {so:,} (chart {c[1]} bn); "
          f"Test System seg income {tsi:,} ({pct(tsi, ts):.1f}% of segment sales); S&O seg income {soi:,} ({pct(soi, so):.1f}%); "
          f"Corporate {corp:,}; SBC {sbc:,}; implied operating income {oi:,}")
    print(f"   sub-segment sum check: SoC+Memory+Other = {c[2] + c[3] + c[4]:.1f} vs Test Systems {c[0]}; Support+Others = {c[5] + c[6]:.1f} vs S&O {c[1]}")

print("\n=== 2. YoY growth of segment and sub-segment sales (chart labels, JPY bn) ===")
lab = ["Test Systems", "Services & Others", "SoC", "Memory", "Other systems", "Support services", "Others"]
pairs = [("FY2025 Q3 (Oct-Dec 2025)", "FY2024 Q3 (Oct-Dec 2024)"), ("FY2025 Q4 (Jan-Mar 2026)", "FY2024 Q4 (Jan-Mar 2025)"),
         ("FY2026 Q1 (Apr-Jun 2026)", "FY2025 Q1 (Apr-Jun 2025)"), ("FY2026 Q2 (Jul-Sep 2026)", "FY2025 Q2 (Jul-Sep 2025)")]
for cur, prev in pairs:
    print(f"{cur} vs {prev}: " + "; ".join(f"{lab[j]} {yoy(CH[cur][j], CH[prev][j]):+.1f}%" for j in range(7)))
    ci, pi = Q[cur], Q[prev]
    print(f"   segment income YoY: Test System {yoy(ci[2], pi[2]):+.1f}%; S&O {ci[3]:,} vs {pi[3]:,}")

print("\n=== 3. Mix: share of total net sales (single quarters, JPY bn) ===")
for k, c in CH.items():
    tot = TOTAL_SALES_BN[k]
    print(f"{k}: Test Systems {pct(c[0], tot):.1f}%; SoC {pct(c[2], tot):.1f}% of total ({pct(c[2], c[0]):.1f}% of Test Systems); "
          f"Memory {pct(c[3], tot):.1f}% of total; Other systems {pct(c[4], tot):.1f}%; S&O {pct(c[1], tot):.1f}%; Support services {pct(c[5], tot):.1f}%")

print("\n=== 4. Full years ===")
FY = {"FY2025": (767.4, 171.5, 80.5, 1019.4, 1128.6, 65.0, 44.2),  # A1-287, 288, 289; Test Systems A1-186; total A1-001; A1-293, A1-294
      "FY2024": (440.4, 157.7, 84.7, 682.8, 779.7, None, None)}    # A1-290, 291, 292; A1-191; A1-002
for k, v in FY.items():
    soc, mem, oth, ts, tot = v[:5]
    print(f"{k}: SoC {soc} ({pct(soc, tot):.1f}% of net sales); Memory {mem} ({pct(mem, tot):.1f}%); Other systems {oth} ({pct(oth, tot):.1f}%); Test Systems {ts} ({pct(ts, tot):.1f}%); sum check {soc + mem + oth:.1f}")
print(f"FY2025 vs FY2024: SoC {yoy(767.4, 440.4):+.1f}%; Memory {yoy(171.5, 157.7):+.1f}%; Other systems {yoy(80.5, 84.7):+.1f}%")
print(f"FY2025 vs FY2024 segment sales (JPY million): Test System {yoy(1019390, 682819):+.1f}%; S&O {yoy(109230, 96888):+.1f}%")
print(f"Segment margins FY2025: Test System {pct(518760, 1019390):.1f}%; S&O {pct(8758, 109230):.1f}%; FY2024: Test System {pct(262120, 682819):.1f}%; S&O {pct(-16125, 96888):.1f}%")
print(f"Segment margins 1H FY2026: Test System {pct(455564, 770231):.1f}%; S&O {pct(20866, 74969):.1f}%; 1H FY2025: Test System {pct(240556, 477957):.1f}%; S&O {pct(3048, 48776):.1f}%")
print(f"Support services share of net sales FY2025: {pct(65.0, 1128.6):.1f}%")

print("\n=== 4b. Audited / filed breakdown of Test System Business (JPY million): SoC, Memory, Others ===")
TSB = {"FY2025": (767424, 171504, 80462, 1128610),    # A1-337, A1-338, A1-339; net sales A1-001
       "FY2024": (440452, 157676, 84691, 779707),     # A1-340, A1-341, A1-342; A1-002
       "1H FY2026": (612922, 101385, 55924, 845200),  # A1-343, A1-344, A1-345; A1-094
       "1H FY2025": (364978, 77430, 35549, 526733)}   # A1-346, A1-347, A1-348; A1-102
for k, (soc, mem, oth, tot) in TSB.items():
    print(f"{k}: SoC {soc:,} ({pct(soc, tot):.1f}% of net sales); Memory {mem:,} ({pct(mem, tot):.1f}%); Others {oth:,} ({pct(oth, tot):.1f}%)")
for cur, prev in [("FY2025", "FY2024"), ("1H FY2026", "1H FY2025")]:
    c, p = TSB[cur], TSB[prev]
    print(f"{cur} vs {prev}: SoC {yoy(c[0], p[0]):+.1f}%; Memory {yoy(c[1], p[1]):+.1f}%; Others {yoy(c[2], p[2]):+.1f}%")

print("\n=== 5. 'Computing / Communications' SoC sales implied by company's rounded split (NOT an AI share) ===")
# Company: Computing/Communications = 95% of SoC Test Systems sales FY2025, 90% FY2024, rounded to nearest 5% (A1-295, A1-296, A1-298)
for k, soc, share, tot in [("FY2025", 767.424, 95, 1128.610), ("FY2024", 440.452, 90, 779.707)]:  # A1-337, A1-340 (JPY bn)
    lo, mid, hi = soc * (share - 2.5) / 100, soc * share / 100, soc * min(share + 2.5, 100) / 100
    print(f"{k}: Computing/Communications SoC sales {mid:.1f} bn (range {lo:.1f}-{hi:.1f} bn given rounding) = "
          f"{pct(mid, tot):.1f}% of net sales (range {pct(lo, tot):.1f}-{pct(hi, tot):.1f}%)")
# Memory: DRAM 90% of Memory Test Systems sales FY2025 (A1-301), rounded to nearest 5%; HBM not separated
print(f"FY2025 DRAM memory tester sales {171.504 * 0.90:.1f} bn (range {171.504 * 0.875:.1f}-{171.504 * 0.925:.1f}); HBM portion not disclosed")  # A1-338, A1-301

print("\n=== 6. LTM (Oct 2025-Sep 2026) segment mix, JPY million unless stated ===")
LTM_TOT = 1128610 + 845200 - 526733                     # A1-001, A1-094, A1-102
LTM_SO = 109230 + 74969 - 48776                          # A1-187, A1-197, A1-202
LTM_SOC = 767424 + 612922 - 364978                       # A1-337, A1-343, A1-346
LTM_SUPPORT_BN = 17.1 + 18.6 + 20.3 + 25.6               # A1-264, A1-271, A1-278, A1-285 (chart labels, JPY bn)
print(f"LTM net sales {LTM_TOT:,}; Services and Others {LTM_SO:,} = {pct(LTM_SO, LTM_TOT):.1f}% "
      "(segment share; NOT a company definition of recurring revenue)")
print(f"LTM Support Services (sum of quarterly chart labels) {LTM_SUPPORT_BN:.1f} bn = {pct(LTM_SUPPORT_BN, LTM_TOT / 1000):.1f}% of LTM net sales "
      "(NOT a company definition of recurring revenue)")
print(f"LTM SoC test system sales {LTM_SOC:,} = {pct(LTM_SOC, LTM_TOT):.1f}% of LTM net sales")
