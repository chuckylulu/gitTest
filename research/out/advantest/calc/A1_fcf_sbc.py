#!/usr/bin/env python3
"""A1 - Results: free cash flow and share-based compensation for Advantest (TSE 6857), IFRS, JPY million.
Fiscal year ends 31 March; FY2025 = Apr 2025-Mar 2026.
Two FCF definitions are shown:
  (1) company definition (Q2 FY26 slides p.9 footnote, A1-163): FCF = cash flows from operating activities + cash flows from investing activities
  (2) capex-based: FCF = operating CF - purchases of PP&E - purchases of intangible assets (our definition, for comparability)
Single quarters are derived by differencing YTD cash flow statements ([I]); they are cross-checked against company-stated quarterly FCF.
SBC = share-based compensation expense (cash flow add-back for FY; segment-reconciliation adjustment for interim periods).
Run: python3 -I A1_fcf_sbc.py > A1_fcf_sbc.out.txt
"""

def pct(a, b):
    return 100.0 * a / b


# YTD cash flows: (operating CF, purchases of PP&E, purchases of intangibles, investing CF)
YTD = {
    "Q1 FY2025 (Apr-Jun 2025)": (46851, 5649, 406, -3444),         # A1-132, A1-133, A1-134, A1-135
    "1H FY2025 (Apr-Sep 2025)": (139923, 18303, 1295, -17141),     # A1-136, A1-137, A1-138, A1-139
    "9M FY2025 (Apr-Dec 2025)": (218554, 24734, 2002, -24342),     # A1-140, A1-141, A1-142, A1-143
    "FY2025 (Apr 2025-Mar 2026)": (335182, 33012, 3018, -34552),   # A1-144, A1-145, A1-146, A1-147
    "FY2024 (Apr 2024-Mar 2025)": (285971, 17414, 2017, -42189),   # A1-148, A1-149, A1-150, A1-151
    "Q1 FY2026 (Apr-Jun 2026)": (137155, 9852, 1032, -102548),     # A1-152, A1-153, A1-154, A1-155
    "1H FY2026 (Apr-Sep 2026)": (306966, 21454, 1166, -210881),    # A1-156, A1-157, A1-158, A1-159
}
DEBT_1H26, EQP_1H26, EQS_1H26 = 184365, 26053, 22133  # A1-160, A1-161, A1-162 (strategic investments, 1H FY2026)


def fcf(t):
    cfo, ppe, intg, cfi = t
    return cfo + cfi, cfo - ppe - intg


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


print("=== 1. YTD / annual periods ===")
for k, t in YTD.items():
    co, cap = fcf(t)
    print(f"{k}: CFO {t[0]:,}; PP&E {t[1]:,}; intangibles {t[2]:,} (PP&E + intangibles {t[1] + t[2]:,}); CFI {t[3]:,}; FCF company def {co:,}; FCF capex-based {cap:,}")

print("\n=== 2. Single quarters by YTD differencing ===")
Qs = {
    "FY2025 Q1 (Apr-Jun 2025)": YTD["Q1 FY2025 (Apr-Jun 2025)"],
    "FY2025 Q2 (Jul-Sep 2025)": sub(YTD["1H FY2025 (Apr-Sep 2025)"], YTD["Q1 FY2025 (Apr-Jun 2025)"]),
    "FY2025 Q3 (Oct-Dec 2025)": sub(YTD["9M FY2025 (Apr-Dec 2025)"], YTD["1H FY2025 (Apr-Sep 2025)"]),
    "FY2025 Q4 (Jan-Mar 2026)": sub(YTD["FY2025 (Apr 2025-Mar 2026)"], YTD["9M FY2025 (Apr-Dec 2025)"]),
    "FY2026 Q1 (Apr-Jun 2026)": YTD["Q1 FY2026 (Apr-Jun 2026)"],
    "FY2026 Q2 (Jul-Sep 2026)": sub(YTD["1H FY2026 (Apr-Sep 2026)"], YTD["Q1 FY2026 (Apr-Jun 2026)"]),
}
COMPANY_Q_FCF = {"FY2025 Q3 (Oct-Dec 2025)": 71.5,   # A1-170 (JPY bn)
                 "FY2025 Q4 (Jan-Mar 2026)": 106.3,  # A1-171
                 "FY2026 Q1 (Apr-Jun 2026)": 34.7,   # A1-169
                 "FY2026 Q2 (Jul-Sep 2026)": 61.5}   # A1-168
for k, t in Qs.items():
    co, cap = fcf(t)
    chk = f" | company-stated FCF {COMPANY_Q_FCF[k]} bn" if k in COMPANY_Q_FCF else ""
    print(f"{k}: CFO {t[0]:,}; PP&E {t[1]:,}; intangibles {t[2]:,} (PP&E + intangibles {t[1] + t[2]:,}); CFI {t[3]:,}; FCF company def {co:,}; FCF capex-based {cap:,}{chk}")
q2 =Qs["FY2026 Q2 (Jul-Sep 2026)"]
print(f"Check FY2026 Q2 CFO vs notes 169.8 bn (A1-166): {q2[0]:,}; CFI vs -108.3 bn (A1-167): {q2[3]:,}")

print("\n=== 3. LTM Oct 2025-Sep 2026 (FY2025 + 1H FY2026 - 1H FY2025) ===")
LTM = tuple(a + b - c for a, b, c in zip(YTD["FY2025 (Apr 2025-Mar 2026)"], YTD["1H FY2026 (Apr-Sep 2026)"], YTD["1H FY2025 (Apr-Sep 2025)"]))
co_ltm, cap_ltm = fcf(LTM)
print(f"LTM CFO {LTM[0]:,}; PP&E {LTM[1]:,}; intangibles {LTM[2]:,} (PP&E + intangibles {LTM[1] + LTM[2]:,}); CFI {LTM[3]:,}")
print(f"LTM FCF company def {co_ltm:,}; LTM FCF capex-based {cap_ltm:,}")
qsum = [fcf(Qs[k]) for k in ["FY2025 Q3 (Oct-Dec 2025)", "FY2025 Q4 (Jan-Mar 2026)", "FY2026 Q1 (Apr-Jun 2026)", "FY2026 Q2 (Jul-Sep 2026)"]]
print(f"Check: sum of four derived quarters company def {sum(x[0] for x in qsum):,}; capex-based {sum(x[1] for x in qsum):,}")
print(f"1H FY2026 strategic investment purchases in CFI: debt instruments {DEBT_1H26:,} + equity {EQP_1H26:,} - equity sale proceeds {EQS_1H26:,} = {DEBT_1H26 + EQP_1H26 - EQS_1H26:,}")

print("\n=== 4. Share-based compensation (SBC) ===")
SBC = {
    "FY2025 (Apr 2025-Mar 2026)": 4450,  # A1-174 (cash flow statement add-back)
    "FY2024 (Apr 2024-Mar 2025)": 2893,  # A1-175
    "1H FY2026 (Apr-Sep 2026)": 2635,    # A1-179 (segment reconciliation)
    "1H FY2025 (Apr-Sep 2025)": 2117,    # A1-181
    "Q1 FY2026 (Apr-Jun 2026)": 1351,    # A1-182
    "9M FY2025 (Apr-Dec 2025)": 3281,    # A1-183
    "Q1 FY2025 (Apr-Jun 2025)": 1063,    # A1-331
}
sbc_q = {
    "FY2025 Q3 (Oct-Dec 2025)": SBC["9M FY2025 (Apr-Dec 2025)"] - SBC["1H FY2025 (Apr-Sep 2025)"],
    "FY2025 Q4 (Jan-Mar 2026)": SBC["FY2025 (Apr 2025-Mar 2026)"] - SBC["9M FY2025 (Apr-Dec 2025)"],
    "FY2026 Q1 (Apr-Jun 2026)": SBC["Q1 FY2026 (Apr-Jun 2026)"],
    "FY2026 Q2 (Jul-Sep 2026)": SBC["1H FY2026 (Apr-Sep 2026)"] - SBC["Q1 FY2026 (Apr-Jun 2026)"],
}
for k, v in sbc_q.items():
    print(f"SBC {k}: {v:,}")
sbc_ltm = SBC["FY2025 (Apr 2025-Mar 2026)"] + SBC["1H FY2026 (Apr-Sep 2026)"] - SBC["1H FY2025 (Apr-Sep 2025)"]
print(f"SBC LTM Oct 2025-Sep 2026: {sbc_ltm:,}")
print(f"FY2025 SBC components: PSU 1,258 + RS/RSU 3,189 = {1258 + 3189:,} (A1-177, A1-178) vs cash-flow add-back 4,450")
for k in ["FY2025 (Apr 2025-Mar 2026)", "FY2024 (Apr 2024-Mar 2025)", "1H FY2026 (Apr-Sep 2026)"]:
    co, cap = fcf(YTD[k])
    print(f"SBC/FCF {k}: company def {pct(SBC[k], co):.2f}%; capex-based {pct(SBC[k], cap):.2f}%")
print(f"SBC/FCF LTM: company def {pct(sbc_ltm, co_ltm):.2f}%; capex-based {pct(sbc_ltm, cap_ltm):.2f}%")
print(f"SBC as % of net sales: FY2025 {pct(4450, 1128610):.2f}% (A1-001); LTM {pct(sbc_ltm, 1447077):.2f}% (LTM sales from A1_pnl)")
print(f"Parent-only J-GAAP SG&A 'share-based compensation expense' FY2025 26,134 (A1-185) / FCF company def FY2025: {pct(26134, fcf(YTD['FY2025 (Apr 2025-Mar 2026)'])[0]):.2f}% (shown for scale only; not the consolidated figure)")

print("\n=== 5. Company FCF annual cross-check (JPY bn) ===")
print(f"FY2025 company def {fcf(YTD['FY2025 (Apr 2025-Mar 2026)'])[0]/1000:.1f} vs slide 300.6 (A1-164); FY2024 {fcf(YTD['FY2024 (Apr 2024-Mar 2025)'])[0]/1000:.1f} vs slide 243.8 (A1-165)")
print(f"Cash purchases of PP&E + intangibles FY2025 {33012 + 3018:,} vs company 'Capital Expenditure' 34.3 bn (A1-172)")
print(f"Cash purchases 1H FY2026 {21454 + 1166:,} vs company 'Capital Expenditure' 23.0 bn (A1-173)")
