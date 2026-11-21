"""A5: KLA balance sheet and capital-return arithmetic. Inputs typed from the saved filings
(sources noted per line); $ thousands unless noted. Share counts: 10-for-1 split effective June 11, 2026;
10-Qs before the split report pre-split shares, Q1 FY27 10-Q and FY26 10-K report post-split (retroactive)."""
# --- Debt ladder: Q1 FY27 10-Q Note 7 (as of Sep 30, 2026)
notes = [  # (coupon %, principal $k, maturity)
    (4.100,   800_000, "2029-03-15"), (4.650, 1_000_000, "2032-07-15"), (4.700, 500_000, "2034-02-01"),
    (5.650,   250_000, "2034-11-01"), (5.000,   400_000, "2049-03-15"), (3.300, 750_000, "2050-03-01"),
    (4.950, 1_450_000, "2052-07-15"), (5.250,   800_000, "2062-07-15")]
tot = sum(p for _, p, _ in notes)
wac = sum(c * p for c, p, _ in notes) / tot
import datetime as dt
asof = dt.date(2026, 9, 30)
wam = sum(p * (dt.date.fromisoformat(m) - asof).days / 365.25 for _, p, m in notes) / tot
print(f"Senior notes principal total: {tot:,}k (10-Q states 5,950,000)")
print(f"Principal-weighted coupon: {wac:.3f}%  (slide: 4.67% weighted avg rate excl. swaps)")
eff = [4.159, 4.657, 4.777, 5.670, 5.047, 3.302, 5.023, 5.259]  # effective rates, Q1 FY27 10-Q Note 7
print(f"Principal-weighted effective rate: {sum(e*p for e,(_,p,_) in zip(eff,notes))/tot:.3f}%")
print(f"Principal-weighted maturity from 2026-09-30: {wam:.1f} years (slide: 17.8 years)")
print(f"Annual coupon cash cost on fixed coupons (before swaps): {sum(c/100*p for c,p,_ in notes):,.0f}k")
print(f"Next maturity: {min(notes, key=lambda x: x[2])}")
carrying = 5_723_289; cash = 4_741_191
print(f"Net cash (debt) vs principal at 2026-09-30: {cash - tot:,}k ; vs carrying value: {cash - carrying:,}k")
# --- Cash + marketable securities by quarter end (10-Q liquidity tables)
cashq = {"Q1FY26 (2025-09-30)": 4_683_591, "Q2FY26 (2025-12-31)": 5_207_464, "Q3FY26 (2026-03-31)": 4_957_938,
         "Q4FY26 (2026-06-30)": 4_902_408, "Q1FY27 (2026-09-30)": 4_741_191}
for k, v in cashq.items():
    print(f"  {k}: cash+securities {v:,}k ; net of $5.95B notes principal {v - tot:,}k")
# --- Interest expense (income statements)
fy26 = 284_440; nine_fy26 = 211_166
ie = {"Q2FY26": 69_668, "Q3FY26": 70_423, "Q4FY26": fy26 - nine_fy26, "Q1FY27": 67_927}
print("Interest expense by quarter:", ie, " LTM:", sum(ie.values()))
# --- Buybacks (trade-date basis; note tables)
pre = {"Q1FY26": (623, 564_400), "Q2FY26": (460, 537_553), "Q3FY26": (440, 631_913)}  # pre-split shares (k)
fy26_post_shares, fy26_cost = 18_241, 2_303_935      # FY26 10-K, post-split
nine_pre_shares, nine_cost = 1_523, 1_733_866       # Q3 FY26 10-Q, pre-split
q4_shares_post = fy26_post_shares - nine_pre_shares * 10
q4_cost = fy26_cost - nine_cost
q1fy27 = (4_914, 942_918)                           # Q1 FY27 10-Q, post-split
print("Buybacks (post-split shares k, $k, implied avg price post-split $):")
rows = [(q, s * 10, c) for q, (s, c) in pre.items()] + [("Q4FY26", q4_shares_post, q4_cost), ("Q1FY27", *q1fy27)]
for q, s, c in rows:
    print(f"  {q}: {s:,}k shares, ${c:,}k, avg ${c / s:,.2f}")
last4 = [r for r in rows if r[0] != "Q1FY26"]
print(f"  Last 4 quarters (Q2FY26-Q1FY27): {sum(r[1] for r in last4):,}k shares, ${sum(r[2] for r in last4):,}k")
print("  Check: Q1FY26 post-split comparative in Q1 FY27 10-Q = 6,225k vs 623k x10 = 6,230k (rounding of pre-split figure)")
# --- Authorisation roll-forward
rem = {"2025-06-30": 5_030_000, "2025-09-30": 4_470_000, "2025-12-31": 3_940_000, "2026-03-31": 10_310_000,
       "2026-06-30": 9_740_000, "2026-09-30": 8_810_000}
print("Authorisation roll-forward check ($k): remaining(t-1) + new - cost(t) vs reported remaining(t)")
chk = [("2025-09-30", "2025-06-30", 0, 564_400), ("2025-12-31", "2025-09-30", 0, 537_553),
       ("2026-03-31", "2025-12-31", 7_000_000, 631_913), ("2026-06-30", "2026-03-31", 0, q4_cost),
       ("2026-09-30", "2026-06-30", 0, 942_918)]
for t, p, new, c in chk:
    print(f"  {t}: {rem[p] + new - c:,} vs reported {rem[t]:,} (diff {rem[t] - (rem[p] + new - c):,}; reported figures rounded to $10M)")
# --- Dividend
print("Dividend: $2.30/qtr pre-split (from May 2026) = $0.23 post-split; Q1 FY27 declared $0.230; annualised post-split $0.92")
print(f"Prior level $1.90 pre-split (Apr 2025) -> $2.30: +{(2.30/1.90-1)*100:.1f}%")
# --- Share count
print(f"Shares outstanding: 130,627,521 (2026-04-27, pre-split) x10 = 1,306,275,210 vs 1,302,962,435 (2026-10-26): "
      f"{(1_302_962_435/1_306_275_210-1)*100:.2f}%")
