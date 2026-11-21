#!/usr/bin/env python3
"""TH module: how Advantest's own tester-market (TAM) estimates moved, versus the MTP3 assumption
and versus Teradyne's stated ATE TAM. Ranges are (low, high) in USD billion; midpoint = (low+high)/2.
Inputs hard-coded from research/out/advantest/parts/TH.csv.
"""
SOC = {  # calendar year -> list of (estimate date, low, high, evidence id)
    "CY2024": [("2024-01-31 first", 3.3, 3.6, "TH-104"), ("2024-04-26", 2.9, 3.2, "TH-106"), ("final (FY25 slides 2026-04-27)", 4.1, 4.1, "TH-099")],
    "CY2025": [("2025-01-29 first", 4.2, 4.8, "TH-107"), ("2025-07-29", 5.7, 6.3, "TH-109"), ("2025-10-28", 6.5, 6.9, "TH-110"), ("final (2026-04-27)", 6.9, 6.9, "TH-096")],
    "CY2026": [("2026-01-28 first", 8.5, 9.5, "TH-111"), ("2026-04-27", 8.7, 9.5, "TH-113"), ("2026-07-29", 10.5, 11.5, "TH-114"), ("2026-10-28 'approx. 11.5'", 11.5, 11.5, "TH-102")],
}
MEM = {
    "CY2024": [("2024-01-31 first", 1.3, 1.6, "TH-105"), ("final (2025-04-25)", 1.9, 1.9, "TH-100")],
    "CY2025": [("2025-01-29 first", 1.7, 2.2, "TH-108"), ("final (2026-04-27)", 2.1, 2.1, "TH-097")],
    "CY2026": [("2026-01-28 first", 2.2, 2.7, "TH-112"), ("2026-07-29 / 2026-10-28 (around midpoint)", 2.5, 3.0, "TH-103")],
}
TOTAL = {"CY2023": 4.4,   # TH-179 (FY25 slides p.18)
         "CY2024": 6.0,   # TH-179
         "CY2025": 9.0}   # TH-098
CY26_TOTAL = (13.0, 14.5)  # TH-101
MTP3_ATE_AVG = 5.9         # USD bn, average CY2024-26 assumed in Jun 2024, TH-121
MTP2_ATE_AVG = 5.1         # TH-121
TER_TAM_2025 = 9.0         # Teradyne, TH-175
TER_TAM_TARGET = (12.0, 14.0)  # Teradyne target model, TH-175
CLAIM_GROWTH = 50          # % per year "about 50% or slightly above", TH-042


def mid(lo, hi):
    return (lo + hi) / 2


for name, data in (("SoC tester TAM", SOC), ("Memory tester TAM", MEM)):
    print(f"== {name} estimate path (USD bn) ==")
    for cy, ests in data.items():
        first = mid(ests[0][1], ests[0][2])
        last = mid(ests[-1][1], ests[-1][2])
        for d, lo, hi, eid in ests:
            print(f"  {cy} {d:<45} {lo:>5.1f}-{hi:<5.1f} mid {mid(lo,hi):.2f}  [{eid}]")
        print(f"  {cy}: latest/final midpoint vs first midpoint = {last:.2f}/{first:.2f} -> {100*(last/first-1):+.1f}%")
        lo_min = min(mid(e[1], e[2]) for e in ests)
        if lo_min < first:
            print(f"  {cy}: lowest midpoint {lo_min:.2f}; final vs lowest {100*(last/lo_min-1):+.1f}%")
    print()

print("== Year-on-year growth of company TAM (total) ==")
print(f"  CY2024 vs CY2023: {TOTAL['CY2024']}/{TOTAL['CY2023']} -> {100*(TOTAL['CY2024']/TOTAL['CY2023']-1):+.1f}%")
print(f"  CY2025 vs CY2024: {TOTAL['CY2025']}/{TOTAL['CY2024']} -> {100*(TOTAL['CY2025']/TOTAL['CY2024']-1):+.1f}%")
g_lo, g_hi = 100*(CY26_TOTAL[0]/TOTAL['CY2025']-1), 100*(CY26_TOTAL[1]/TOTAL['CY2025']-1)
print(f"  CY2026e vs CY2025: {CY26_TOTAL[0]}-{CY26_TOTAL[1]} / {TOTAL['CY2025']} -> {g_lo:+.1f}% to {g_hi:+.1f}%")
cagr_lo = ((CY26_TOTAL[0]/TOTAL['CY2023'])**(1/3)-1)*100
cagr_hi = ((CY26_TOTAL[1]/TOTAL['CY2023'])**(1/3)-1)*100
print(f"  CAGR CY2023->CY2026e: {cagr_lo:.1f}% to {cagr_hi:.1f}% per year (company says about {CLAIM_GROWTH}%/yr, TH-042)")
soc25, soc26lo, soc26hi = 6.9, 10.5, 11.5
print(f"  SoC CY2026e vs CY2025: {100*(soc26lo/soc25-1):+.1f}% to {100*(soc26hi/soc25-1):+.1f}%")
print()
print("== MTP3 (Jun 2024) market assumption vs latest company estimates ==")
avg_lo = (TOTAL['CY2024'] + TOTAL['CY2025'] + CY26_TOTAL[0]) / 3
avg_hi = (TOTAL['CY2024'] + TOTAL['CY2025'] + CY26_TOTAL[1]) / 3
print(f"  CY2024-26 average now: {avg_lo:.2f} to {avg_hi:.2f} USD bn vs MTP3 assumption {MTP3_ATE_AVG}")
print(f"  -> {100*(avg_lo/MTP3_ATE_AVG-1):+.1f}% to {100*(avg_hi/MTP3_ATE_AVG-1):+.1f}% above the MTP3 assumption")
print(f"  MTP3 assumed growth vs MTP2 average: {100*(MTP3_ATE_AVG/MTP2_ATE_AVG-1):+.1f}%; latest implies {100*(avg_lo/MTP2_ATE_AVG-1):+.1f}% to {100*(avg_hi/MTP2_ATE_AVG-1):+.1f}%")
print()
print("== Teradyne vs Advantest TAM statements ==")
print(f"  CY2025 ATE TAM: Advantest {TOTAL['CY2025']} vs Teradyne ~{TER_TAM_2025} -> difference {TOTAL['CY2025']-TER_TAM_2025:+.1f}")
print(f"  Teradyne target-model TAM {TER_TAM_TARGET[0]}-{TER_TAM_TARGET[1]} vs Advantest CY2026e {CY26_TOTAL[0]}-{CY26_TOTAL[1]}:")
print(f"    overlap range {max(TER_TAM_TARGET[0], CY26_TOTAL[0])}-{min(TER_TAM_TARGET[1], CY26_TOTAL[1])}; Advantest CY2026e midpoint {mid(*CY26_TOTAL):.2f} vs Teradyne target midpoint {mid(*TER_TAM_TARGET):.2f}")
