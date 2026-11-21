"""CL: inventory build in 1H FY2026, JPY million."""
# CL-088 inventories 31 Mar 2026 and 30 Sep 2026 (tanshin, statement of financial position) [F]
INV_MAR26, INV_SEP26 = 231_718, 352_426
# CL-032 1H FY2026 net sales [F]
H1_SALES = 845_200
chg = INV_SEP26 - INV_MAR26
print(f"Inventory change Apr-Sep 2026: {chg:,} ({chg/INV_MAR26*100:.1f}%)")
print(f"Inventory at 30 Sep 2026 / annualised 1H sales: {INV_SEP26/(2*H1_SALES)*100:.1f}%")
print(f"Inventory at 31 Mar 2026 / FY2025 sales (CL-037 1,128,610): {INV_MAR26/1_128_610*100:.1f}%")
