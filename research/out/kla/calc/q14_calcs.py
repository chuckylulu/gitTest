"""Q1/Q4/NV arithmetic. Inputs are quoted from saved sources (see comments). Run: python3 -I calc/q14_calcs.py"""
# 1) Implied KLA X-ray CD metrology revenue from CFO remarks (Q3 FY26 call, Fool transcript [S]):
#    market "about $75 million to $100 million", KLA "about, call it, 60-ish percent share".
lo, hi, share = 75.0, 100.0, 0.60
print(f"Q14-I1 implied KLA X-ray metrology revenue: ${lo*share:.0f}M - ${hi*share:.0f}M per year (share 60%)")
# 2) Lasertec FY2026 (Jul 2025-Jun 2026) orders vs FY2025, tanshin p5/p18 (JPY million)
o25, o26 = 105226, 237504
print(f"Q14-I2 Lasertec total orders FY2026 vs FY2025: {o26/o25:.3f}x, YoY {100*(o26/o25-1):.1f}%")
semi_orders, semi_backlog, total_backlog = 172216, 301303, 322964
print(f"Q14-I3 semiconductor-related share of FY2026 orders: {100*semi_orders/o26:.1f}%; of backlog Jun-30-2026: {100*semi_backlog/total_backlog:.1f}%")
# 3) Onto stake in Rigaku: JPY 113,078,356,600 for 61,123,436 shares (Onto closing release p1; Rigaku release)
jpy, shares = 113_078_356_600, 61_123_436
print(f"Q14-I4 implied price per Rigaku share: JPY {jpy/shares:,.0f}; implied 100% equity value at 27.0%: JPY {jpy/0.27/1e9:,.1f}B")
# 4) Lasertec semis sales FY2026 vs semis orders FY2026 (book-to-bill, semis only) tanshin p5/p18
semi_sales = 168090
print(f"Q14-I5 Lasertec semiconductor-related book-to-bill FY2026: {semi_orders/semi_sales:.2f}")
