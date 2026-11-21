"""CL: management's Oct-2025 call of a 'softer' Q3 FY2025 vs reported single-quarter sales (JPY billion)."""
# CL-030 total net sales chart (slides Q2 FY26 p.7) [F]
TOTAL = {"FY25Q2": 262.9, "FY25Q3": 273.8, "FY25Q4": 328.1}
# CL-029 segment chart (slides Q2 FY26 p.6) [F]
SOC = {"FY25Q2": 173.7, "FY25Q3": 165.2}
MEM = {"FY25Q2": 43.9, "FY25Q3": 57.3}
# CL-010 Oct 2025: "We expect Q3 FY2025 to be a softer quarter." [C]
# CL-008 Jul 2025: temporary digestion expected in 2H FY2025 [C]; CL-011 Jan 2026: did not occur [C]
print(f"Total sales QoQ FY25 Q3 (Oct-Dec 2025): {(TOTAL['FY25Q3']/TOTAL['FY25Q2']-1)*100:.1f}%")
print(f"SoC test system sales QoQ FY25 Q3: {(SOC['FY25Q3']/SOC['FY25Q2']-1)*100:.1f}%")
print(f"Memory test system sales QoQ FY25 Q3: {(MEM['FY25Q3']/MEM['FY25Q2']-1)*100:.1f}%")
print(f"Total sales QoQ FY25 Q4 (Jan-Mar 2026): {(TOTAL['FY25Q4']/TOTAL['FY25Q3']-1)*100:.1f}%")
