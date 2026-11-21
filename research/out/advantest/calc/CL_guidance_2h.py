"""CL: implied 2H FY2026 (Oct 2026-Mar 2027) from FY forecast minus 1H actual (JPY million)."""
# CL-032 1H FY2026 actual (tanshin p.1) [F]
H1_SALES, H1_OI = 845_200, 456_809
# CL-033 FY2026 forecast of 28 Oct 2026 (tanshin p.2) [C]
FY_SALES, FY_OI = 1_863_000, 967_000
# CL-035 July forecast assumed 2H operating margin 47.3% [C]; CL-073 1H includes a one-time inventory
# write-down reversal, amount not disclosed -> 1H margin cannot be shown ex this item.
h2_sales = FY_SALES - H1_SALES
h2_oi = FY_OI - H1_OI
print(f"Implied 2H sales: {h2_sales:,}  (2H vs 1H: {(h2_sales/H1_SALES-1)*100:.1f}%)")
print(f"Implied 2H operating income: {h2_oi:,}")
print(f"1H operating margin (reported, incl. undisclosed inventory reversal): {H1_OI/H1_SALES*100:.1f}%")
print(f"Implied 2H operating margin: {h2_oi/h2_sales*100:.1f}%  (July-forecast 2H: 47.3%)")
print(f"FY2026 forecast operating margin: {FY_OI/FY_SALES*100:.1f}%")
