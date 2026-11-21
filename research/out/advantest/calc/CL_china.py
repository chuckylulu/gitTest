"""CL: China ship-to sales, share and YoY (JPY billion, slide data labels)."""
# CL-059 China series (slides Q2 FY26 p.7) [F]
CHINA = {"FY25Q2": 52.1, "FY25Q3": 65.4, "FY25Q4": 56.8, "FY26Q1": 69.4, "FY26Q2": 90.1}
# CL-030 / CL-024 totals (same chart) [F]
TOTAL = {"FY25Q2": 262.9, "FY25Q3": 273.8, "FY25Q4": 328.1, "FY26Q1": 367.5, "FY26Q2": 477.7}
for q in ["FY25Q3", "FY25Q4", "FY26Q1", "FY26Q2"]:
    print(f"China share {q}: {CHINA[q]/TOTAL[q]*100:.1f}%")
print(f"China YoY FY26 Q2 (Jul-Sep 2026): {(CHINA['FY26Q2']/CHINA['FY25Q2']-1)*100:.1f}%")
ltm_c = sum(CHINA[q] for q in ["FY25Q3", "FY25Q4", "FY26Q1", "FY26Q2"])
ltm_t = sum(TOTAL[q] for q in ["FY25Q3", "FY25Q4", "FY26Q1", "FY26Q2"])
print(f"LTM (Oct 2025-Sep 2026) China {ltm_c:.1f} of {ltm_t:.1f} = {ltm_c/ltm_t*100:.1f}%")
print(f"Total sales YoY FY26 Q2: {(TOTAL['FY26Q2']/TOTAL['FY25Q2']-1)*100:.1f}%")
