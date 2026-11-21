"""CL: customer concentration, FY2025 (Apr 2025-Mar 2026), JPY million."""
# CL-037 FY2025 net sales (tanshin p.1) [F]
SALES_FY25 = 1_128_610
# CL-068 NVIDIA Group and TSMC net sales (ASR 84th, note 6(6)) [F]
NVDA_GRP, TSMC = 243_735, 124_922
# CL-069 NVIDIA International, Inc. single counterparty, printed 20.2% [F]
NVDA_INTL = 228_273
# CL-070 top five ~50% [F]
print(f"NVIDIA Group share: {NVDA_GRP/SALES_FY25*100:.1f}%")
print(f"TSMC share: {TSMC/SALES_FY25*100:.1f}%")
print(f"Two named groups together: {(NVDA_GRP+TSMC)/SALES_FY25*100:.1f}%")
print(f"NVIDIA International, Inc. check vs printed 20.2%: {NVDA_INTL/SALES_FY25*100:.1f}%")
print(f"Top five ~50% less two named groups: about {50-(NVDA_GRP+TSMC)/SALES_FY25*100:.1f} points for the other three")
