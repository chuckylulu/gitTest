"""CL: tester TAM growth, Advantest estimate vs Teradyne target model (USD billion)."""
import math

# CL-007 Advantest TAM chart (slides Q2 FY26 p.12), company estimates [C]
CY24_TOTAL = 6.0
CY25_TOTAL = 9.0
CY26_SOC = (10.5, 11.5)
CY26_MEM = (2.5, 3.0)
# CL-001 management: TAM grew "about 50% or slightly above" a year
# CL-079 Teradyne target model: ATE TAM ~9.0 (2025) -> 12-14, ~15-25% CAGR off FY25 [C]
TER_2025 = 9.0
TER_TARGET = (12.0, 14.0)
TER_CAGR = (0.15, 0.25)

g25 = CY25_TOTAL / CY24_TOTAL - 1
cy26 = (CY26_SOC[0] + CY26_MEM[0], CY26_SOC[1] + CY26_MEM[1])
g26 = (cy26[0] / CY25_TOTAL - 1, cy26[1] / CY25_TOTAL - 1)
print(f"Advantest CY24->CY25 tester TAM growth: {g25*100:.1f}%")
print(f"Advantest CY26e total tester TAM: {cy26[0]:.1f}-{cy26[1]:.1f} USD bn")
print(f"Advantest CY25->CY26e growth: {g26[0]*100:.1f}% to {g26[1]*100:.1f}%")
# years for Teradyne's model to reach its own target band from 9.0
yrs_min = math.log(TER_TARGET[0] / TER_2025) / math.log(1 + TER_CAGR[1])
yrs_max = math.log(TER_TARGET[1] / TER_2025) / math.log(1 + TER_CAGR[0])
print(f"Teradyne model: years from 2025 to reach 12-14 bn at 15-25% CAGR: {yrs_min:.2f} to {yrs_max:.2f}")
print(f"Teradyne 2026 point at 15-25% CAGR off 9.0: {TER_2025*1.15:.2f}-{TER_2025*1.25:.2f} USD bn")
gap_lo = cy26[0] - TER_2025 * 1.25
gap_hi = cy26[1] - TER_2025 * 1.15
print(f"Advantest CY26e minus Teradyne-model 2026 point: {gap_lo:.2f} to {gap_hi:.2f} USD bn")
overlap = (max(cy26[0], TER_TARGET[0]), min(cy26[1], TER_TARGET[1]))
print(f"Overlap of Advantest CY26e range with Teradyne target band: {overlap[0]:.1f}-{overlap[1]:.1f} USD bn")
# CL-138 Advantest's own CY2026 estimate of 28 Jan 2026 (slides Q3 FY25 p.12) [C]: SoC 8.5-9.5, memory 2.2-2.7
JAN26_SOC = (8.5, 9.5)
JAN26_MEM = (2.2, 2.7)
jan = (JAN26_SOC[0] + JAN26_MEM[0], JAN26_SOC[1] + JAN26_MEM[1])
print(f"Advantest CY26e total, Jan 2026: {jan[0]:.1f}-{jan[1]:.1f} USD bn; Oct 2026: {cy26[0]:.1f}-{cy26[1]:.1f}")
print(f"Revision Jan->Oct 2026: +{cy26[0]-jan[0]:.1f} (low end, {(cy26[0]/jan[0]-1)*100:.1f}%) / +{cy26[1]-jan[1]:.1f} (high end, {(cy26[1]/jan[1]-1)*100:.1f}%) USD bn")
# CL-109 TechNews (15 Jan 2026), attributed to Advantest materials [S]: ATE market peak ~8 USD bn in 2026
TN_2026 = 8.0
print(f"Company Oct-2026 CY26e minus TechNews-relayed 2026 figure: {cy26[0]-TN_2026:.1f} to {cy26[1]-TN_2026:.1f} USD bn")
print(f"TechNews 8.0 vs company's own Jan-2026 CY26e low end {jan[0]:.1f}: {TN_2026-jan[0]:.1f} USD bn (figure not traceable to the Jan-2026 company document)")
