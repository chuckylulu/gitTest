#!/usr/bin/env python3
"""A6 cycle analysis for Comet Holding AG (FY = calendar year).
Half-year net sales / EBITDA in CHF thousands. H2 = FY - H1 (derived). Basis notes:
 - 2017 figures are pre-IFRS 16 (H1 2017 restated for IFRS 15 in the H1 2018 report);
 - from 2018 on, IFRS 16 basis (H1 2018 restated in the H1 2019 report; FY2018 restated, FY2019 deck p21);
 - H1 2025 restated (H1 2026 report note 01.1); FY2024 restated (AR 2025 note 2.3); H1 2024 not restated.
Sources (evidence keys in A.csv): H1 reports 2018-2026, AR FY2021 five-year table (2017-2021),
AR FY2025 five-year table (2021-2025).
Run: python3 -I research/out/comet/calc/A_cycle.py
"""
FY = {2017: (443_370, 63_203), 2018: (436_356, 42_966), 2019: (371_606, 39_974), 2020: (395_816, 58_616),
      2021: (513_721, 102_749), 2022: (586_395, 118_913), 2023: (397_453, 44_996), 2024: (445_362, 58_011),
      2025: (457_044, 46_335)}
H1 = {2017: (222_624, 33_819), 2018: (232_381, 32_107), 2019: (176_959, 8_513), 2020: (182_309, 18_753),
      2021: (248_302, 44_252), 2022: (267_498, 37_681), 2023: (207_025, 14_275), 2024: (189_315, 12_980),
      2025: (227_154, 22_978), 2026: (239_834, 31_367)}
series = []
for y in range(2017, 2027):
    if y in H1:
        series.append((f"H1 {y}", *H1[y]))
    if y in FY:
        s, e = FY[y][0] - H1[y][0], FY[y][1] - H1[y][1]
        series.append((f"H2 {y}", s, e))
print("Half-year series (CHF m, EBITDA margin):")
for lab, s, e in series:
    print(f"  {lab}: sales {s/1000:6.1f}  EBITDA {e/1000:6.1f}  margin {100*e/s:5.1f}%")


def draw(peak_lab, trough_lab):
    d = {l: (s, e) for l, s, e in series}
    ps, pe = d[peak_lab]; ts, te = d[trough_lab]
    return (100 * (ts / ps - 1), 100 * pe / ps, 100 * te / ts)

print("\nDownturns (half-year, peak -> trough):")
for name, pk, tr in (("2018-19 memory downturn", "H1 2018", "H1 2019"),
                     ("2022-24 semiconductor correction", "H2 2022", "H1 2024"),
                     ("2022-23 (to first trough half)", "H2 2022", "H2 2023"),
                     ("2024-25 soft patch", "H2 2024", "H1 2025")):
    dd, pm, tm = draw(pk, tr)
    print(f"  {name}: {pk} -> {tr}: net sales {dd:+.1f}%; EBITDA margin {pm:.1f}% -> {tm:.1f}% ({tm-pm:+.1f}pp)")
# margin trough within 2022-24
d = {l: (s, e) for l, s, e in series}
print(f"  2022-24 margin trough: H1 2023 {100*d['H1 2023'][1]/d['H1 2023'][0]:.1f}% / H1 2024 {100*d['H1 2024'][1]/d['H1 2024'][0]:.1f}%")

print("\nAnnual peak -> trough:")
for pk, tr in ((2017, 2019), (2022, 2023)):
    (ps, pe), (ts, te) = FY[pk], FY[tr]
    print(f"  FY{pk} -> FY{tr}: net sales {100*(ts/ps-1):+.1f}%; EBITDA margin {100*pe/ps:.1f}% -> {100*te/ts:.1f}% ({100*te/ts-100*pe/ps:+.1f}pp)")
print("  note: FY2017 EBITDA is pre-IFRS16; FY2018 as first reported 8.7% (FY2019 deck p21) vs 9.8% restated.")
ps, pe = FY[2018]
print(f"  FY2018 ex CHF 6.6m loss on disposal (EBT US): {100*(pe+6_600)/ps:.1f}%")

print("\nQuarterly net sales (CHF m) peak -> trough:")
Q = {"Q1 2022": 124.8, "Q2 2022": 267.5 - 124.8, "Q3 2022": 164.8, "Q4 2022": 586.4 - 432.3,
     "Q1 2023": 107.5, "Q2 2023": 207.0 - 107.5, "Q3 2023": 77.7, "Q4 2023": 112.7,
     "Q1 2024": 80.9, "Q2 2024": 108.4, "Q3 2024": 113.2, "Q4 2024": 445.4 - 302.5,
     "Q1 2025": 111.2, "Q2 2025": 227.2 - 111.2, "Q3 2025": 102.5, "Q4 2025": 457.0 - 329.6,
     "Q1 2026": 106.3, "Q2 2026": 133.5, "Q3 2026": 155.6}
for k, v in Q.items():
    print(f"  {k}: {v:.1f}")
print(f"  Q3 2022 -> Q3 2023: {100*(Q['Q3 2023']/Q['Q3 2022']-1):+.1f}% (company: -52.9% YoY)")
print(f"  Q4 2024 -> Q3 2025: {100*(Q['Q3 2025']/Q['Q4 2024']-1):+.1f}%")
print(f"  Recovery: Q3 2026 vs Q3 2022 peak: {100*(Q['Q3 2026']/Q['Q3 2022']-1):+.1f}%")
print(f"  Quarters from Q3 2022 peak to regain it: Q3 2026 155.6 still {'below' if Q['Q3 2026'] < Q['Q3 2022'] else 'above'} 164.8")
