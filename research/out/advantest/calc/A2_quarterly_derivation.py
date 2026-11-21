"""A2: derive single-quarter net sales and cost of sales from year-to-date (YTD) tanshin figures.
Fiscal year ends 31 March; Advantest names fiscal years by START year (FY2025 = Apr 2025-Mar 2026).
All inputs JPY million, IFRS, copied from the financial-results (tanshin) PDFs.
Quarter = YTD(current) - YTD(previous quarter of the same fiscal year).
"""
# --- inputs (evidence ids in comments) ---
SALES_FY2024_9M = 547_358    # A2-063  9M to 31 Dec 2024
COGS_FY2024_9M = 241_507     # A2-064
SALES_FY2024_FY = 779_707    # A2-065  FY to 31 Mar 2025
COGS_FY2024_FY = 334_622     # A2-066
SALES_FY2025_Q1 = 263_776    # A2-067  3M to 30 Jun 2025
COGS_FY2025_Q1 = 92_138      # A2-068
SALES_FY2025_1H = 526_733    # A2-069  6M to 30 Sep 2025
COGS_FY2025_1H = 191_454     # A2-070
SALES_FY2025_9M = 800_537    # A2-071  9M to 31 Dec 2025
COGS_FY2025_9M = 295_550     # A2-072
SALES_FY2025_FY = 1_128_610  # A2-073  FY to 31 Mar 2026
COGS_FY2025_FY = 402_503     # A2-074
SALES_FY2026_Q1 = 367_473    # A2-075  3M to 30 Jun 2026
COGS_FY2026_Q1 = 111_920     # A2-076
SALES_FY2026_1H = 845_200    # A2-077  6M to 30 Sep 2026
COGS_FY2026_1H = 249_822     # A2-078

# single-quarter values (JPY million)
Q = {
    "FY2024 Q4 (Jan-Mar 2025)": (SALES_FY2024_FY - SALES_FY2024_9M, COGS_FY2024_FY - COGS_FY2024_9M),
    "FY2025 Q1 (Apr-Jun 2025)": (SALES_FY2025_Q1, COGS_FY2025_Q1),
    "FY2025 Q2 (Jul-Sep 2025)": (SALES_FY2025_1H - SALES_FY2025_Q1, COGS_FY2025_1H - COGS_FY2025_Q1),
    "FY2025 Q3 (Oct-Dec 2025)": (SALES_FY2025_9M - SALES_FY2025_1H, COGS_FY2025_9M - COGS_FY2025_1H),
    "FY2025 Q4 (Jan-Mar 2026)": (SALES_FY2025_FY - SALES_FY2025_9M, COGS_FY2025_FY - COGS_FY2025_9M),
    "FY2026 Q1 (Apr-Jun 2026)": (SALES_FY2026_Q1, COGS_FY2026_Q1),
    "FY2026 Q2 (Jul-Sep 2026)": (SALES_FY2026_1H - SALES_FY2026_Q1, COGS_FY2026_1H - COGS_FY2026_Q1),
}
# cross-check against single-quarter sales printed on the FY26 Q2 briefing slides p.5 (JPY billion)
SLIDE_SALES_B = {"FY2025 Q1 (Apr-Jun 2025)": 263.8, "FY2025 Q2 (Jul-Sep 2025)": 262.9,
                 "FY2025 Q3 (Oct-Dec 2025)": 273.8, "FY2025 Q4 (Jan-Mar 2026)": 328.1,
                 "FY2026 Q1 (Apr-Jun 2026)": 367.5, "FY2026 Q2 (Jul-Sep 2026)": 477.7}
# single-quarter gross profit on the same slide p.5 (JPY billion), row A2-192; slide-implied COGS = sales - gross profit
SLIDE_GP_B = {"FY2025 Q1 (Apr-Jun 2025)": 171.6, "FY2025 Q2 (Jul-Sep 2025)": 163.7,
              "FY2025 Q3 (Oct-Dec 2025)": 169.7, "FY2025 Q4 (Jan-Mar 2026)": 221.1,
              "FY2026 Q1 (Apr-Jun 2026)": 255.6, "FY2026 Q2 (Jul-Sep 2026)": 339.8}

if __name__ == "__main__":
    print("Single-quarter net sales and cost of sales, JPY million (derived from YTD where needed)")
    print(f"{'quarter':28s} {'sales':>10s} {'COGS':>10s}  slide_sales_JPYbn  check")
    for k, (s, c) in Q.items():
        sl = SLIDE_SALES_B.get(k)
        chk = "" if sl is None else ("OK" if abs(s / 1000 - sl) <= 0.051 else ("OK within 0.1bn rounding (slide likely 526.7-263.8)" if abs(s / 1000 - sl) <= 0.1 else "MISMATCH"))
        print(f"{k:28s} {s:10,d} {c:10,d}  {'' if sl is None else sl:>17}  {chk}")
    print()
    print("Cross-check of derived quarterly COGS against slide sales minus slide gross profit (JPY billion, 1-decimal slide rounding):")
    for k, (s, c) in Q.items():
        if k in SLIDE_GP_B:
            imp = SLIDE_SALES_B[k] - SLIDE_GP_B[k]
            print(f"  {k}: tanshin-derived {c / 1000:.1f} vs slide-implied {imp:.1f} -> diff {c / 1000 - imp:+.2f} "
                  f"({'OK' if abs(c / 1000 - imp) <= 0.15 else 'CHECK'})")
    mx = max(abs(Q[k][1] / 1000 - (SLIDE_SALES_B[k] - SLIDE_GP_B[k])) for k in SLIDE_GP_B)
    print(f"  Largest absolute difference: {mx:.2f} JPY billion")
