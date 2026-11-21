#!/usr/bin/env python3
"""TH module: closest available proxy for the AI/HPC share of Advantest revenue.

Advantest does not disclose an AI, HBM or advanced-packaging share of revenue. The closest
company-disclosed split is SoC test system sales by application ("Computing / Communications",
rounded to the nearest 5%; Computing includes HPC/AI, Communications includes smartphone APs)
and memory test system sales by application (DRAM vs non-volatile, rounded to 5%; HBM not split).
A share printed as X% (rounded to nearest 5%) can be anywhere in [X-2.5%, X+2.5%].
Inputs hard-coded from research/out/advantest/parts/TH.csv.
"""
YEARS = {
    # year: (SoC sales JPY bn, Computing/Comms share %, total net sales JPY bn, ids)
    "FY2024 (Apr 2024-Mar 2025)": (440.4, 90, 779.7, "TH-130, TH-127, TH-135"),
    "FY2025 (Apr 2025-Mar 2026)": (767.4, 95, 1128.6, "TH-129, TH-127, TH-133"),
    "FY2026e (Apr 2026-Mar 2027, forecast of 2026-10-28)": (1375.0, 90, 1863.0, "TH-131, TH-127, TH-134"),
}
MEM_FY25 = 171.5      # JPY bn, TH-132
DRAM_FY25 = 90        # % of memory test system sales, rounded to 5%, TH-059
SALES_FY25 = 1128.6   # TH-133
SOC_1H26 = 259.6 + 353.3   # FY2026 Q1 + Q2 SoC, TH-142 + TH-141
SALES_1H26 = 845.2    # TH-136

DEFINITION = ('Company definition (Investors Guide Oct 2026 p.5, TH-128): "Computing" in "Computing and '
              'Communications" includes leading-edge devices such as HPC (High Performance Computing) and AI, '
              'and "Communications" include application processors (APs) for smartphones.')
print("LABEL: this is a PROXY. It is NOT an AI share, NOT an HBM share and NOT an advanced-packaging share;")
print("       Advantest does not disclose any of those (TH-126). The category also contains smartphone APs.")
print(DEFINITION)
print()
print("== SoC 'Computing / Communications' sales as a share of total net sales ==")
for y, (soc, pct, sales, ids) in YEARS.items():
    c, lo, hi = soc * pct / 100, soc * (pct - 2.5) / 100, soc * (pct + 2.5) / 100
    print(f"  {y}: SoC {soc:.1f} x {pct}% = {c:.1f} JPYbn (range {lo:.1f}-{hi:.1f}); "
          f"/ net sales {sales:.1f} = {100*c/sales:.1f}% (range {100*lo/sales:.1f}-{100*hi/sales:.1f}%)  [inputs {ids}]")
    print(f"      SoC test systems / net sales = {100*soc/sales:.1f}%")
print(f"  FY2026 1H: SoC {SOC_1H26:.1f} / net sales {SALES_1H26} = {100*SOC_1H26/SALES_1H26:.1f}%")
print()
print("== Memory 'DRAM' tester sales (includes HBM; HBM not split out) ==")
d, lo, hi = MEM_FY25 * DRAM_FY25 / 100, MEM_FY25 * (DRAM_FY25 - 2.5) / 100, MEM_FY25 * (DRAM_FY25 + 2.5) / 100
print(f"  FY2025: memory {MEM_FY25} x {DRAM_FY25}% = {d:.1f} JPYbn (range {lo:.1f}-{hi:.1f}); / net sales {SALES_FY25} = "
      f"{100*d/SALES_FY25:.1f}% (range {100*lo/SALES_FY25:.1f}-{100*hi/SALES_FY25:.1f}%)")
print(f"  Memory test systems / net sales FY2025 = {100*MEM_FY25/SALES_FY25:.1f}%")

# ---- fix round 2 (2026-11-21): DRAM proxy for FY2024 and the FY2026 forecast ----
MEM_FY24, DRAM_FY24, SALES_FY24 = 157.7, 95, 779.7     # TH-203 (slide p.16), TH-059 (FY24 95%), TH-135 (JPY bn)
MEM_FY26E, DRAM_FY26E, SALES_FY26E = 229.0, 85, 1863.0  # TH-208 [C] memory forecast, TH-207 [C] DRAM 85% FY26e, TH-134 [C]
for lbl, mem, dr, sal in [("FY2024 (Apr 2024-Mar 2025)", MEM_FY24, DRAM_FY24, SALES_FY24),
                          ("FY2026e (Apr 2026-Mar 2027, forecasts of 2026-10-28)", MEM_FY26E, DRAM_FY26E, SALES_FY26E)]:
    d, lo, hi = mem * dr / 100, mem * (dr - 2.5) / 100, mem * (dr + 2.5) / 100
    print(f"  {lbl}: memory {mem} x {dr}% = {d:.1f} JPYbn (range {lo:.1f}-{hi:.1f}); / net sales {sal} = "
          f"{100*d/sal:.1f}% (range {100*lo/sal:.1f}-{100*hi/sal:.1f}%)")
print("  Cross-check FY2024 in JPY million (A1-341 memory 157,676; A1-002 net sales 779,707): "
      f"{100 * 157676 * 0.95 / 779707:.1f}%")
