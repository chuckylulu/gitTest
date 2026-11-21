"""A2: check the company's 'sales up about 20% from 1H to 2H FY2026' remark (A2-026) against its own
2H FY2026 sales forecast (A2-027, Oct 2026) and reported 1H FY2026 sales (A2-077).
FY2026 = Apr 2026-Mar 2027; 1H = Apr-Sep 2026 (reported); 2H = Oct 2026-Mar 2027 (company forecast).
"""
SALES_2H_FY2026_FCST_B = 1_017.8   # A2-027 JPY billion, briefing slides p.14
SALES_1H_FY2026_M = 845_200        # A2-077 JPY million, financial results p.10

if __name__ == "__main__":
    h1 = SALES_1H_FY2026_M / 1000
    print(f"2H FY2026 forecast / 1H FY2026 reported = {SALES_2H_FY2026_FCST_B} / {h1:.1f} = "
          f"{SALES_2H_FY2026_FCST_B / h1:.3f} -> {(SALES_2H_FY2026_FCST_B / h1 - 1) * 100:+.1f}%")
