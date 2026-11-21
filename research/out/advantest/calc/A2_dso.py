"""A2: days sales outstanding (DSO) at each quarter-end, FY2024 Q4 to FY2026 Q2.
Formula (stated): DSO = ending 'Trade and other receivables' / single-quarter net sales x 91.25 days.
Caveat: the balance-sheet line includes 'other receivables'; trade receivables from contracts with
customers alone are disclosed only at fiscal year-ends (annual securities report, note 22).
Inputs JPY million. Quarterly sales from A2_quarterly_derivation.py (ids A2-079..A2-083 are [I]).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from A2_quarterly_derivation import Q  # single-quarter sales/COGS (inputs A2-063..A2-078)

REC = {  # Trade and other receivables, balance sheet (tanshin)
    "FY2024 Q4 (Jan-Mar 2025)": 113_031,  # A2-089  31 Mar 2025
    "FY2025 Q1 (Apr-Jun 2025)": 127_959,  # A2-090  30 Jun 2025
    "FY2025 Q2 (Jul-Sep 2025)": 163_652,  # A2-091  30 Sep 2025
    "FY2025 Q3 (Oct-Dec 2025)": 143_318,  # A2-092  31 Dec 2025
    "FY2025 Q4 (Jan-Mar 2026)": 228_731,  # A2-093  31 Mar 2026
    "FY2026 Q1 (Apr-Jun 2026)": 178_497,  # A2-094  30 Jun 2026
    "FY2026 Q2 (Jul-Sep 2026)": 239_468,  # A2-095  30 Sep 2026
}
# Notes and trade accounts receivable from contracts with customers (annual securities report 84th, note 22)
CONTRACT_REC_MAR2025 = 105_884  # A2-097
CONTRACT_REC_MAR2026 = 217_454  # A2-098
# Note 8 breakdown of trade and other receivables (annual securities report 84th)
NOTE8 = {"31 Mar 2025": (4_942, 100_942, 7_197),    # A2-167 note, A2-168 trade, A2-169 other
         "31 Mar 2026": (8_279, 209_175, 11_319)}   # A2-170 note, A2-171 trade, A2-172 other
DAYS_Q = 91.25

if __name__ == "__main__":
    print("DSO = ending trade and other receivables / single-quarter net sales x 91.25")
    print(f"{'quarter-end':28s} {'receivables':>12s} {'qtr sales':>10s} {'DSO days':>9s}")
    prev = None
    for k, rec in REC.items():
        s = Q[k][0]
        dso = rec / s * DAYS_Q
        print(f"{k:28s} {rec:12,d} {s:10,d} {dso:9.1f}")
    print()
    print("Contract-receivables DSO at fiscal year-ends (notes & trade AR / Q4 sales x 91.25):")
    for k, rec in (("FY2024 Q4 (Jan-Mar 2025)", CONTRACT_REC_MAR2025), ("FY2025 Q4 (Jan-Mar 2026)", CONTRACT_REC_MAR2026)):
        s = Q[k][0]
        print(f"  {k}: {rec:,d} / {s:,d} x 91.25 = {rec / s * DAYS_Q:.1f} days")
    print()
    print("Note 8 check: note + trade receivables vs contract receivables (note 22); other receivables share of line:")
    for d, (n, t, o) in NOTE8.items():
        cr = CONTRACT_REC_MAR2025 if d == "31 Mar 2025" else CONTRACT_REC_MAR2026
        tot = REC["FY2024 Q4 (Jan-Mar 2025)"] if d == "31 Mar 2025" else REC["FY2025 Q4 (Jan-Mar 2026)"]
        print(f"  {d}: {n:,d} + {t:,d} = {n + t:,d} (note 22: {cr:,d}); other receivables {o:,d} = {o / tot * 100:.1f}% of {tot:,d}")
    print()
    print("Change in trade and other receivables:")
    print(f"  31 Mar 2026 -> 30 Jun 2026: {REC['FY2026 Q1 (Apr-Jun 2026)'] - REC['FY2025 Q4 (Jan-Mar 2026)']:+,d}")
    print(f"  30 Sep 2025 -> 30 Sep 2026: {REC['FY2026 Q2 (Jul-Sep 2026)'] - REC['FY2025 Q2 (Jul-Sep 2025)']:+,d} "
          f"({(REC['FY2026 Q2 (Jul-Sep 2026)'] / REC['FY2025 Q2 (Jul-Sep 2025)'] - 1) * 100:+.1f}%) vs quarterly sales "
          f"{(Q['FY2026 Q2 (Jul-Sep 2026)'][0] / Q['FY2025 Q2 (Jul-Sep 2025)'][0] - 1) * 100:+.1f}%")
