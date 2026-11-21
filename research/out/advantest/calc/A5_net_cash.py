"""A5 - net cash / net debt at five balance-sheet dates (JPY million).

Fiscal year ends 31 March. FY2025 = Apr 2025-Mar 2026; FY2026 Q2 end = 30 Sep 2026.
Variants:
  (a) excluding lease liabilities, bonds at IFRS carrying amount (liability component)
  (b) including lease liabilities, bonds at carrying amount
  (c) excluding leases, convertible bond at face value (JPY 100,000 million repayable at maturity)
  (d) including leases, convertible bond at face value
No commercial paper line appears in any of the statements used.
Investment securities (strategic equity stakes, investment-fund LP interests) are NOT counted as cash;
they are shown separately for information only.
"""

# date: (cash, borrowings_current, borrowings_noncurrent, bonds_carrying, lease_current, lease_noncurrent, source ids)
BS = {
    "2025-03-31 (FY2024 end)": dict(cash=262544, bor_c=74952, bor_nc=3, bonds=0, lease_c=5046, lease_nc=13502,
                                    ids="A5-001..A5-006"),
    "2025-12-31 (FY2025 Q3 end)": dict(cash=329322, bor_c=75651, bor_nc=0, bonds=0, lease_c=4403, lease_nc=11149,
                                       ids="A5-008..A5-011"),
    "2026-03-31 (FY2025 end)": dict(cash=339966, bor_c=0, bor_nc=0, bonds=0, lease_c=4966, lease_nc=15226,
                                    ids="A5-001..A5-006"),
    "2026-06-30 (FY2026 Q1 end)": dict(cash=413124, bor_c=0, bor_nc=0, bonds=88930, lease_c=4977, lease_nc=14259,
                                       ids="A5-012..A5-015"),
    "2026-09-30 (FY2026 Q2 end)": dict(cash=401785, bor_c=0, bor_nc=0, bonds=89486, lease_c=4820, lease_nc=12940,
                                       ids="A5-017..A5-020"),
}
CB_FACE = 100000          # A5-061: total issue amount JPY 100 billion, issued 20 Apr 2026
CB_ISSUE_DATE = "2026-04-20"
COMPANY_NET_IBD_FY2025 = -339966   # A5-024: company-reported net interest-bearing debt at 31 Mar 2026 (borrowings only)

# Undrawn facilities
UNUSED_LINES = {"2026-03-31 (FY2025 end)": 140000,   # A5-040
                "2026-09-30 (FY2026 Q2 end)": 40000 + 100000}  # A5-042, A5-043 (commit line 40.0bn + overdraft 100.0bn, nothing drawn)

# Investment securities at 30 Sep 2026 (not counted as cash) - A5-021 / A5-026 / A5-027
INV_SEC_SEP26 = 432586
INV_EQUITY_SEP26 = 203670
INV_DEBT_FUNDS_SEP26 = 228916

print("JPY million; negative net debt = net cash")
print(f"{'date':28s} {'cash':>9s} {'borrow':>8s} {'bondsCV':>8s} {'leases':>7s} | {'(a)exL':>9s} {'(b)inL':>9s} {'(c)exL,CBface':>14s} {'(d)inL,CBface':>14s}")
for d, v in BS.items():
    bor = v["bor_c"] + v["bor_nc"]
    lease = v["lease_c"] + v["lease_nc"]
    cb_face = CB_FACE if v["bonds"] else 0
    a = bor + v["bonds"] - v["cash"]
    b = a + lease
    c = bor + cb_face - v["cash"]
    dd = c + lease
    print(f"{d:28s} {v['cash']:9,d} {bor:8,d} {v['bonds']:8,d} {lease:7,d} | {a:9,d} {b:9,d} {c:14,d} {dd:14,d}")

# check against the company's own definition at FY2025 end
v = BS["2026-03-31 (FY2025 end)"]
calc = v["bor_c"] + v["bor_nc"] - v["cash"]
print(f"\nCompany definition (borrowings - cash) at 31 Mar 2026: calc {calc:,d} vs reported {COMPANY_NET_IBD_FY2025:,d} -> match={calc == COMPANY_NET_IBD_FY2025}")

# liquidity headroom
for d, lines in UNUSED_LINES.items():
    print(f"Cash + unused committed line/overdraft at {d}: {BS[d]['cash'] + lines:,d} (cash {BS[d]['cash']:,d} + lines {lines:,d})")

# change in cash between FY2025 end and FY2026 Q2 end
print(f"Change in cash 31 Mar 2026 -> 30 Sep 2026: {BS['2026-09-30 (FY2026 Q2 end)']['cash'] - BS['2026-03-31 (FY2025 end)']['cash']:,d}")
print(f"Investment securities check 30 Sep 2026: equity {INV_EQUITY_SEP26:,d} + funds {INV_DEBT_FUNDS_SEP26:,d} = {INV_EQUITY_SEP26 + INV_DEBT_FUNDS_SEP26:,d} vs reported {INV_SEC_SEP26:,d}")
