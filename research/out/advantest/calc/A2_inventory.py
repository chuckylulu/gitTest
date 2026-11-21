"""A2: inventory days (DIO), inventory growth, and raw/WIP/finished split shares.
Formula (stated): DIO = ending inventories / single-quarter cost of sales x 91.25 days.
Caveat: cost of sales includes inventory valuation losses and, in FY2026 Q1, a reversal of
inventory obsolescence that management called non-recurring (amount not disclosed; A2-052).
Inputs JPY million. Quarterly COGS from A2_quarterly_derivation.py (derived rows A2-084..A2-088 are [I]).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from A2_quarterly_derivation import Q  # inputs A2-063..A2-078

INV = {  # Inventories, balance sheet (tanshin)
    "FY2024 Q4 (Jan-Mar 2025)": 209_707,  # A2-032  31 Mar 2025
    "FY2025 Q1 (Apr-Jun 2025)": 209_274,  # A2-033  30 Jun 2025
    "FY2025 Q2 (Jul-Sep 2025)": 210_038,  # A2-034  30 Sep 2025
    "FY2025 Q3 (Oct-Dec 2025)": 222_464,  # A2-035  31 Dec 2025
    "FY2025 Q4 (Jan-Mar 2026)": 231_718,  # A2-036  31 Mar 2026
    "FY2026 Q1 (Apr-Jun 2026)": 273_654,  # A2-037  30 Jun 2026
    "FY2026 Q2 (Jul-Sep 2026)": 352_426,  # A2-038  30 Sep 2026
}
SPLIT = {  # annual securities reports, note 9 Inventories: (finished goods, work in process, raw materials and supplies)
    "31 Mar 2024": (23_979, 38_872, 141_538),   # A2-039, A2-040, A2-041 (total 204,389)
    "31 Mar 2025": (27_730, 53_225, 128_752),   # A2-042, A2-043, A2-044 (total 209,707)
    "31 Mar 2026": (35_244, 69_240, 127_234),   # A2-045, A2-046, A2-047 (total 231,718)
}
DAYS_Q = 91.25

if __name__ == "__main__":
    print("DIO = ending inventories / single-quarter cost of sales x 91.25")
    print(f"{'quarter-end':28s} {'inventories':>12s} {'qtr COGS':>10s} {'DIO days':>9s} {'QoQ chg':>10s}")
    prev = None
    for k, inv in INV.items():
        c = Q[k][1]
        qoq = "" if prev is None else f"{inv - prev:+,d}"
        print(f"{k:28s} {inv:12,d} {c:10,d} {inv / c * DAYS_Q:9.1f} {qoq:>10s}")
        prev = inv
    a, b = INV["FY2025 Q2 (Jul-Sep 2025)"], INV["FY2026 Q2 (Jul-Sep 2026)"]
    print(f"\nInventories 30 Sep 2025 -> 30 Sep 2026: {b - a:+,d} ({(b / a - 1) * 100:+.1f}%)")
    m, s = INV["FY2025 Q4 (Jan-Mar 2026)"], INV["FY2026 Q2 (Jul-Sep 2026)"]
    print(f"Inventories 31 Mar 2026 -> 30 Sep 2026: {s - m:+,d} ({(s / m - 1) * 100:+.1f}%)")
    print(f"1H FY2026 COGS growth YoY: {(Q['FY2026 Q1 (Apr-Jun 2026)'][1] + Q['FY2026 Q2 (Jul-Sep 2026)'][1]) / (Q['FY2025 Q1 (Apr-Jun 2025)'][1] + Q['FY2025 Q2 (Jul-Sep 2025)'][1]) * 100 - 100:+.1f}%")

    print("\nInventory split (annual securities reports, note 9):")
    for d, (fg, wip, rm) in SPLIT.items():
        t = fg + wip + rm
        print(f"  {d}: total {t:,d}; FG {fg:,d} ({fg / t * 100:.1f}%), WIP {wip:,d} ({wip / t * 100:.1f}%), RM&S {rm:,d} ({rm / t * 100:.1f}%)")
    names = ("finished goods", "work in process", "raw materials and supplies")
    for (d0, v0), (d1, v1) in ((("31 Mar 2024", SPLIT["31 Mar 2024"]), ("31 Mar 2025", SPLIT["31 Mar 2025"])),
                               (("31 Mar 2025", SPLIT["31 Mar 2025"]), ("31 Mar 2026", SPLIT["31 Mar 2026"]))):
        print(f"  YoY {d0} -> {d1}: " + "; ".join(f"{n} {y - x:+,d} ({(y / x - 1) * 100:+.1f}%)" for n, x, y in zip(names, v0, v1)))
    # annual DIO on fiscal-year COGS (ending balance / annual COGS x 365)
    FY2024_COGS, FY2025_COGS = 334_622, 402_503  # A2-066, A2-074
    print(f"\nAnnual DIO (ending inventories / annual COGS x 365): FY2024 {209_707 / FY2024_COGS * 365:.1f} days; "
          f"FY2025 {231_718 / FY2025_COGS * 365:.1f} days")
