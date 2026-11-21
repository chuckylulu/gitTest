"""A2: customer advances (contract liabilities = 'advance receipts').
Balances are disclosed only at fiscal year-ends (annual securities report, note 22). Each quarter the
cash-flow statement shows the YTD change in advance receipts; single-quarter cash-flow changes are
derived here by subtracting YTD figures. These are CASH-FLOW MOVEMENTS, not balances; FX translation
makes balance changes differ from cash-flow changes (reconciled below for FY2024 and FY2025).
Inputs JPY million.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from A2_quarterly_derivation import SALES_FY2024_FY, SALES_FY2025_FY  # A2-065, A2-073

CL_APR2024 = 18_233   # A2-123 contract liabilities (advance receipts) 1 Apr 2024
CL_MAR2025 = 28_798   # A2-124 31 Mar 2025
CL_MAR2026 = 40_143   # A2-125 31 Mar 2026
CF_FY2024 = 11_099    # A2-142 cash-flow 'Advance receipts', FY2024 (12M)
REV_FROM_OPENING_CL = {"FY2024": 15_591,   # A2-126 revenue recognized in FY2024 from the 1 Apr 2024 balance
                       "FY2025": 24_857}   # A2-127 revenue recognized in FY2025 from the 31 Mar 2025 balance
CF_YTD = {            # cash-flow 'Advance receipts' YTD
    "FY2025 Q1": 1_377,   # A2-136 3M to 30 Jun 2025
    "FY2025 1H": 9_571,   # A2-137 6M to 30 Sep 2025
    "FY2025 9M": 2_169,   # A2-138 9M to 31 Dec 2025
    "FY2025 FY": 9_748,   # A2-139 12M to 31 Mar 2026
    "FY2026 Q1": 36_984,  # A2-140 3M to 30 Jun 2026
    "FY2026 1H": 44_215,  # A2-141 6M to 30 Sep 2026
}
OCL = {  # 'Other current liabilities' balance-sheet line (contains advance receipts)
    "31 Mar 2025": 31_066,  # A2-129
    "30 Jun 2025": 33_124,  # A2-130
    "30 Sep 2025": 42_619,  # A2-131
    "31 Dec 2025": 34_788,  # A2-132
    "31 Mar 2026": 42_756,  # A2-133
    "30 Jun 2026": 80_397,  # A2-134
    "30 Sep 2026": 87_924,  # A2-135
}

if __name__ == "__main__":
    q = {
        "FY2025 Q1 (Apr-Jun 2025)": CF_YTD["FY2025 Q1"],
        "FY2025 Q2 (Jul-Sep 2025)": CF_YTD["FY2025 1H"] - CF_YTD["FY2025 Q1"],
        "FY2025 Q3 (Oct-Dec 2025)": CF_YTD["FY2025 9M"] - CF_YTD["FY2025 1H"],
        "FY2025 Q4 (Jan-Mar 2026)": CF_YTD["FY2025 FY"] - CF_YTD["FY2025 9M"],
        "FY2026 Q1 (Apr-Jun 2026)": CF_YTD["FY2026 Q1"],
        "FY2026 Q2 (Jul-Sep 2026)": CF_YTD["FY2026 1H"] - CF_YTD["FY2026 Q1"],
    }
    print("Single-quarter cash-flow increase/(decrease) in advance receipts, JPY million:")
    for k, v in q.items():
        print(f"  {k}: {v:+,d}")
    print(f"  Sum FY2025 Q3..FY2026 Q2 (last 4 quarters): {sum(list(q.values())[2:]):+,d}")
    print()
    print("Reconciliation, balance change vs cash-flow change:")
    print(f"  FY2024: balance {CL_MAR2025 - CL_APR2024:+,d} vs cash flow {CF_FY2024:+,d} -> difference {CL_MAR2025 - CL_APR2024 - CF_FY2024:+,d}")
    print(f"  FY2025: balance {CL_MAR2026 - CL_MAR2025:+,d} vs cash flow {CF_YTD['FY2025 FY']:+,d} -> difference {CL_MAR2026 - CL_MAR2025 - CF_YTD['FY2025 FY']:+,d}")
    print()
    print("Year-end contract liabilities as % of fiscal-year net sales:")
    print(f"  31 Mar 2025: {CL_MAR2025:,d} / {SALES_FY2024_FY:,d} = {CL_MAR2025 / SALES_FY2024_FY * 100:.2f}%")
    print(f"  31 Mar 2026: {CL_MAR2026:,d} / {SALES_FY2025_FY:,d} = {CL_MAR2026 / SALES_FY2025_FY * 100:.2f}%")
    print(f"  YoY growth of year-end balance: FY2024 {(CL_MAR2025 / CL_APR2024 - 1) * 100:+.1f}%, FY2025 {(CL_MAR2026 / CL_MAR2025 - 1) * 100:+.1f}%")
    print()
    print("'Other current liabilities' line, change by quarter vs advance-receipts cash flow:")
    keys = list(OCL)
    qk = list(q)
    for i in range(1, len(keys)):
        d = OCL[keys[i]] - OCL[keys[i - 1]]
        print(f"  {keys[i - 1]} -> {keys[i]}: OCL {d:+,d}; advance-receipts CF {q[qk[i - 1]]:+,d}")
    print(f"  31 Mar 2026 -> 30 Sep 2026: OCL {OCL['30 Sep 2026'] - OCL['31 Mar 2026']:+,d}; advance-receipts CF 1H {CF_YTD['FY2026 1H']:+,d}")
    same = sum(1 for i in range(1, len(keys)) if (OCL[keys[i]] - OCL[keys[i - 1]] > 0) == (q[qk[i - 1]] > 0))
    print(f"  Quarters in which the OCL change and the advance-receipts cash flow have the same sign: {same} of {len(keys) - 1}")
    print()
    print(f"FY2026 Q1 advance-receipts cash inflow vs 31 Mar 2026 contract-liability balance: "
          f"{CF_YTD['FY2026 Q1']:,d} / {CL_MAR2026:,d} = {CF_YTD['FY2026 Q1'] / CL_MAR2026 * 100:.1f}%")
    print(f"FY2026 1H advance-receipts cash inflow vs full-year FY2025 inflow: {CF_YTD['FY2026 1H']:,d} / {CF_YTD['FY2025 FY']:,d} = "
          f"{CF_YTD['FY2026 1H'] / CF_YTD['FY2025 FY']:.2f}x")
    print()
    print("Contract liabilities as share of the 'Other current liabilities' line at fiscal year-ends:")
    print(f"  31 Mar 2025: {CL_MAR2025:,d} / {OCL['31 Mar 2025']:,d} = {CL_MAR2025 / OCL['31 Mar 2025'] * 100:.1f}%")
    print(f"  31 Mar 2026: {CL_MAR2026:,d} / {OCL['31 Mar 2026']:,d} = {CL_MAR2026 / OCL['31 Mar 2026'] * 100:.1f}%")
    print()
    print("Share of the opening contract-liability balance recognized as revenue within the fiscal year:")
    print(f"  FY2024: {REV_FROM_OPENING_CL['FY2024']:,d} / {CL_APR2024:,d} = {REV_FROM_OPENING_CL['FY2024'] / CL_APR2024 * 100:.1f}%")
    print(f"  FY2025: {REV_FROM_OPENING_CL['FY2025']:,d} / {CL_MAR2025:,d} = {REV_FROM_OPENING_CL['FY2025'] / CL_MAR2025 * 100:.1f}%")
