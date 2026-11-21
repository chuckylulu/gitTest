"""A5 - Zero Coupon Convertible Bonds due 2031: shares on conversion, dilution, liability accretion.

Issued 20 Apr 2026, redemption 28 Mar 2031, JPY 100,000 million principal, 0% coupon.
JPY million unless stated.
"""
import datetime as dt

FACE_YEN = 100_000_000_000          # A5-061
CP_INITIAL = 36000.0                # A5-065 initial conversion price (yen)
CP_ADJ = 35946.5                    # A5-075 adjusted conversion price effective 1 Oct 2026
SHARES_REPORTED = 2_777_777         # A5-066 shares subject to the stock acquisition rights (as reported)
ISSUED = 732_000_000                # A5-108 issued shares at 30 Sep 2026
OUTSTANDING_EX_TREAS = 721_952_905  # A5-103 outstanding excl. treasury at 30 Sep 2026
LIAB_JUN26 = 88930                  # A5-013 bonds carrying amount 30 Jun 2026
LIAB_SEP26 = 89486                  # A5-018 bonds carrying amount 30 Sep 2026
EQUITY_COMP = 7712                  # A5-078 share premium increase on issuance of CB
MATURITY = dt.date(2031, 3, 28)
SEP26 = dt.date(2026, 9, 30)

sh_init = FACE_YEN / CP_INITIAL
sh_adj = FACE_YEN / CP_ADJ
print(f"Shares on full conversion at initial price: {sh_init:,.1f} (reported {SHARES_REPORTED:,d})")
print(f"Shares on full conversion at adjusted price: {sh_adj:,.1f} (+{sh_adj - sh_init:,.1f})")
print(f"Dilution vs issued shares {ISSUED:,d}: initial {SHARES_REPORTED/ISSUED*100:.3f}%, adjusted {sh_adj/ISSUED*100:.3f}%")
print(f"Dilution vs shares outstanding excl. treasury {OUTSTANDING_EX_TREAS:,d}: initial {SHARES_REPORTED/OUTSTANDING_EX_TREAS*100:.3f}%, adjusted {sh_adj/OUTSTANDING_EX_TREAS*100:.3f}%")
print(f"Conversion price adjustment: {(CP_ADJ/CP_INITIAL-1)*100:.3f}%")

face_m = FACE_YEN / 1e6
print(f"\nLiability carrying amount as % of face: 30 Jun 2026 {LIAB_JUN26/face_m*100:.2f}%, 30 Sep 2026 {LIAB_SEP26/face_m*100:.2f}%")
acc_q = LIAB_SEP26 - LIAB_JUN26
print(f"Accretion Jul-Sep 2026: {acc_q:,d} -> simple annualised rate on Jun balance {acc_q*4/LIAB_JUN26*100:.2f}%")
yrs = (MATURITY - SEP26).days / 365.25
impl = (face_m / LIAB_SEP26) ** (1 / yrs) - 1
print(f"Remaining discount to face at 30 Sep 2026: {face_m - LIAB_SEP26:,.0f}; years to maturity {yrs:.2f}; implied compound accretion rate to reach face {impl*100:.2f}% p.a.")
print(f"Face {face_m:,.0f} - equity component {EQUITY_COMP:,d} = {face_m - EQUITY_COMP:,.0f} (gap to 30 Jun 2026 liability {face_m - EQUITY_COMP - LIAB_JUN26:,.0f}: transaction costs, tax effect and Q1 accretion are not separately disclosed)")

# use of proceeds (company plan) - A5-072, A5-073, A5-074
uop = {"tester supply capacity by Mar 2029": 50, "strategic inventory by Mar 2027": 20, "next-gen test development by Mar 2028": 30}
print(f"\nUse of proceeds plan total: {sum(uop.values())} JPY bn; capacity+inventory = {uop['tester supply capacity by Mar 2029'] + uop['strategic inventory by Mar 2027']} JPY bn")
