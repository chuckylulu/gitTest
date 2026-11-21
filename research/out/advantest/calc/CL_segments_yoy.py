"""CL: SoC vs memory test system sales growth (JPY billion, single quarters, slide data labels)."""
# CL-029 Test Systems breakdown chart (slides Q2 FY26 p.6) [F]
SOC = {"FY25Q2": 173.7, "FY25Q3": 165.2, "FY26Q2": 353.3}
MEM = {"FY24Q3": 54.6, "FY25Q2": 43.9, "FY25Q3": 57.3, "FY26Q2": 53.4}
# CL-049 Teradyne compute revenue "nearly 50%" YoY in Q3 2026 (Jul-Sep 2026) [F]
TER_COMPUTE_YOY = 0.50  # upper bound of "nearly 50%"

soc_yoy = SOC["FY26Q2"] / SOC["FY25Q2"] - 1
mem_yoy = MEM["FY26Q2"] / MEM["FY25Q2"] - 1
mem_vs_fy24q3 = MEM["FY26Q2"] / MEM["FY24Q3"] - 1
mem_vs_fy25q3 = MEM["FY26Q2"] / MEM["FY25Q3"] - 1  # FY25 Q3 (57.3) is the highest memory quarter on the chart
mem_share_q2_26 = MEM["FY26Q2"] / (MEM["FY26Q2"] + SOC["FY26Q2"])
mem_share_q2_25 = MEM["FY25Q2"] / (MEM["FY25Q2"] + SOC["FY25Q2"])
print(f"SoC test system sales YoY FY26 Q2 (Jul-Sep 2026): {soc_yoy*100:.1f}%")
print(f"Memory test system sales YoY FY26 Q2: {mem_yoy*100:.1f}%")
print(f"Memory FY26 Q2 vs FY24 Q3 (Oct-Dec 2024): {mem_vs_fy24q3*100:.1f}%")
print(f"Memory FY26 Q2 vs FY25 Q3 (Oct-Dec 2025, chart high): {mem_vs_fy25q3*100:.1f}%")
print(f"Memory share of SoC+memory sales: FY25 Q2 {mem_share_q2_25*100:.1f}% -> FY26 Q2 {mem_share_q2_26*100:.1f}%")
print(f"Advantest SoC YoY minus Teradyne compute YoY (<=50%): >= {(soc_yoy-TER_COMPUTE_YOY)*100:.1f} points")
print("Caveat: Teradyne 'compute' is a subset of its SoC; Advantest SoC includes non-compute; scopes differ.")
