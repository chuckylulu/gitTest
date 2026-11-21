#!/usr/bin/env python3
"""TH module: cross-check Advantest's tester market-share claims against its own segment sales.

(1) CY2025 (Jan-Dec 2025) Advantest SoC and memory tester sales converted to USD with the
    company's quarterly average USD/JPY rates, divided by the company's own CY2025 TAM.
(2) Two-vendor split for Jul-Sep 2026: Advantest FY2026 Q2 vs Teradyne Q3 2026 SoC and memory revenue.
All inputs are hard-coded from evidence rows in research/out/advantest/parts/TH.csv.
"""
# --- Advantest segment sales, JPY billion (calendar 2025 = FY2024 Q4 + FY2025 Q1-Q3) ---
SOC = {"FY24Q4 Jan-Mar 2025": 148.8,   # TH-137
       "FY25Q1 Apr-Jun 2025": 191.3,   # TH-138
       "FY25Q2 Jul-Sep 2025": 173.7,   # TH-139
       "FY25Q3 Oct-Dec 2025": 165.2}   # TH-140
MEM = {"FY24Q4 Jan-Mar 2025": 35.1,    # TH-143
       "FY25Q1 Apr-Jun 2025": 33.5,    # TH-144
       "FY25Q2 Jul-Sep 2025": 43.9,    # TH-145
       "FY25Q3 Oct-Dec 2025": 57.3}    # TH-146
FX = {"FY24Q4 Jan-Mar 2025": 154,      # TH-149 average JPY per USD
      "FY25Q1 Apr-Jun 2025": 146,      # TH-148
      "FY25Q2 Jul-Sep 2025": 146,      # TH-148
      "FY25Q3 Oct-Dec 2025": 152}      # TH-148
TAM_SOC_CY25 = 6.9       # USD bn, TH-096 (company estimate)
TAM_MEM_CY25 = 2.1       # USD bn, TH-097
CLAIM_SOC_CY25 = 66      # %, TH-116
CLAIM_MEM_CY25 = 61      # %, TH-119 (about 60% per TH-064)

# --- Jul-Sep 2026 quarter ---
ADV_SOC_Q = 353.3        # JPY bn, FY2026 Q2, TH-141
ADV_MEM_Q = 53.4         # JPY bn, FY2026 Q2, TH-147
FX_Q = 161               # JPY per USD, FY2026 Q2 result, TH-148
TER_SOC_Q = 676          # USD m, Teradyne Q3 2026, TH-166
TER_MEM_Q = 301          # USD m, Teradyne Q3 2026, TH-166


def usd(d):
    return sum(d[k] / FX[k] for k in d)


print("== (1) CY2025 implied share from Advantest's own sales and TAM ==")
for k in SOC:
    print(f"  {k}: SoC {SOC[k]:.1f} JPYbn / {FX[k]} = {SOC[k]/FX[k]:.4f} USDbn; memory {MEM[k]:.1f} / {FX[k]} = {MEM[k]/FX[k]:.4f} USDbn")
soc_usd, mem_usd = usd(SOC), usd(MEM)
print(f"  CY2025 SoC sales  = {sum(SOC.values()):.1f} JPYbn = {soc_usd:.3f} USDbn")
print(f"  CY2025 mem sales  = {sum(MEM.values()):.1f} JPYbn = {mem_usd:.3f} USDbn")
s_soc, s_mem = 100 * soc_usd / TAM_SOC_CY25, 100 * mem_usd / TAM_MEM_CY25
print(f"  implied SoC share    = {soc_usd:.3f}/{TAM_SOC_CY25} = {s_soc:.1f}%  (company claim {CLAIM_SOC_CY25}%; gap {s_soc-CLAIM_SOC_CY25:+.1f} pts)")
print(f"  implied memory share = {mem_usd:.3f}/{TAM_MEM_CY25} = {s_mem:.1f}%  (company claim {CLAIM_MEM_CY25}%; gap {s_mem-CLAIM_MEM_CY25:+.1f} pts)")
tot = soc_usd + mem_usd
print(f"  implied overall share = {tot:.3f}/{TAM_SOC_CY25+TAM_MEM_CY25:.1f} = {100*tot/(TAM_SOC_CY25+TAM_MEM_CY25):.1f}%  (company claim 65%, TH-115)")
# sensitivity: one flat FX rate for the whole year
for flat in (146, 150, 154):
    print(f"  sensitivity flat FX {flat}: SoC {100*sum(SOC.values())/flat/TAM_SOC_CY25:.1f}%, memory {100*sum(MEM.values())/flat/TAM_MEM_CY25:.1f}%")

print("\n== (2) Two-vendor split, Jul-Sep 2026 (Advantest FY2026 Q2 vs Teradyne Q3 2026) ==")
a_soc, a_mem = 1000 * ADV_SOC_Q / FX_Q, 1000 * ADV_MEM_Q / FX_Q
print(f"  Advantest SoC {ADV_SOC_Q} JPYbn / {FX_Q} = {a_soc:.0f} USDm; memory {ADV_MEM_Q} / {FX_Q} = {a_mem:.0f} USDm")
print(f"  Teradyne  SoC {TER_SOC_Q} USDm; memory {TER_MEM_Q} USDm")
print(f"  Advantest share of the two-vendor SoC total    = {100*a_soc/(a_soc+TER_SOC_Q):.1f}%  (ratio {a_soc/TER_SOC_Q:.2f}x)")
print(f"  Advantest share of the two-vendor memory total = {100*a_mem/(a_mem+TER_MEM_Q):.1f}%  (ratio {a_mem/TER_MEM_Q:.2f}x)")
print("  caveats: other vendors excluded (two-vendor shares overstate both); Teradyne segment revenue may include service;")
print("           Teradyne quarter ends late Sep 2026; revenue recognition differs from Advantest's TAM basis.")
