#!/usr/bin/env python3
"""Module A (group level) arithmetic for Comet Holding AG (COTN). FY = calendar year.
All inputs are CHF thousands unless noted, copied from saved primary documents; the
evidence row holding each input is given in the comment (research/out/comet/parts/A.csv).
Run: python3 -I research/out/comet/calc/A_periods.py
"""

def pct(a, b):
    return 100.0 * a / b

def yoy(a, b):
    return 100.0 * (a / b - 1)

print("=" * 70)
print("A1  RESULTS BY PERIOD")
print("=" * 70)
# ---- Annual (FY2025 AR, FY2024 restated) ----
FY25 = dict(sales=457_044, gp=173_677, ebit=24_556, ebitda=46_335, ocf=48_217, icf=-39_715, sbc=1_415)   # see A.csv / A_notes.md for source rows
FY24r = dict(sales=445_362, gp=190_731, ebit=35_861, ebitda=58_011, sbc=1_034)                        # see A.csv / A_notes.md for source rows
FY24o = dict(gp=193_100, ebitda=60_380)                                                                # see A.csv / A_notes.md for source rows
# ---- Half-years ----
H125r = dict(sales=227_154, gp=89_755, ebit=12_245, ebitda=22_978, fcf=1_344, sbc=370)   # see A.csv / A_notes.md for source rows
H125o = dict(gp=87_485, ebit=9_975, ebitda=20_708)                                       # see A.csv / A_notes.md for source rows
H126 = dict(sales=239_834, gp=99_362, ebit=20_391, ebitda=31_367, fcf=-19_306, sbc=666, oneoff=4_500)  # see A.csv / A_notes.md for source rows

H225 = {k: FY25[k] - H125r[k] for k in ("sales", "gp", "ebit", "ebitda", "sbc")}
H225["fcf"] = (FY25["ocf"] + FY25["icf"]) - H125r["fcf"]
FY25["fcf"] = FY25["ocf"] + FY25["icf"]
print(f"FY2025 FCF (OCF+ICF) = {FY25['fcf']:,}  (company: 8,502)")
for name, d in (("H1 2025 restated", H125r), ("H2 2025 derived", H225), ("H1 2026", H126), ("FY2025", FY25), ("FY2024 restated", FY24r)):
    s = d["sales"]
    print(f"{name:18s} sales {s:>8,}  GM {pct(d['gp'], s):5.1f}%  EBITDA {d['ebitda']:>7,} ({pct(d['ebitda'], s):5.1f}%)"
          f"  EBIT {d['ebit']:>7,} ({pct(d['ebit'], s):5.1f}%)  SBC {d['sbc']:>6,} ({pct(d['sbc'], s):.2f}% of sales)"
          + (f"  FCF {d['fcf']:>8,}" if 'fcf' in d else ""))
print(f"H2 2025 vs H2 2024 sales YoY: H2 2024 = 445,362 - 189,315 = {445_362-189_315:,}; YoY {yoy(H225['sales'], 445_362-189_315):.1f}%")
print(f"H1 2026 sales YoY {yoy(H126['sales'], H125r['sales']):.1f}%  FY2025 YoY {yoy(FY25['sales'], FY24r['sales']):.1f}%")
# SBC / FCF
print(f"SBC/FCF FY2025: {pct(FY25['sbc'], FY25['fcf']):.1f}%;  FY2024: {pct(1_034, 41_414):.1f}%")
ltm_fcf = H225["fcf"] + H126["fcf"]
ltm_sbc = H225["sbc"] + H126["sbc"]
ltm_sales = H225["sales"] + H126["sales"]
ltm_ebitda = H225["ebitda"] + H126["ebitda"]
print(f"LTM to Jun-2026 (H2 2025 + H1 2026): sales {ltm_sales:,}  EBITDA {ltm_ebitda:,} ({pct(ltm_ebitda, ltm_sales):.1f}%)  FCF {ltm_fcf:,}  SBC {ltm_sbc:,}")
print(f"LTM sales YoY vs (H2 2024 + H1 2025): {yoy(ltm_sales, (445_362-189_315)+H125r['sales']):.1f}%")

print("\n-- One-offs named by management: with / without --")
h126_ex = H126["ebitda"] + H126["oneoff"]
print(f"H1 2026 EBITDA reported {pct(H126['ebitda'], H126['sales']):.1f}%; ex CHF 4.5m one-time Penang/efficiency costs {h126_ex:,} = {pct(h126_ex, H126['sales']):.1f}%")
h126_ebit_ex = H126["ebit"] + H126["oneoff"]
print(f"H1 2026 EBIT reported {pct(H126['ebit'], H126['sales']):.1f}%; ex one-offs {pct(h126_ebit_ex, H126['sales']):.1f}%")
fire = 2_100   # see A.csv / A_notes.md for source rows
print(f"FY2025 EBITDA {pct(FY25['ebitda'], FY25['sales']):.1f}%; ex fire insurance recovery CHF 2.1m: {FY25['ebitda']-fire:,} = {pct(FY25['ebitda']-fire, FY25['sales']):.1f}%")
print(f"H2 2025 EBITDA {pct(H225['ebitda'], H225['sales']):.1f}%; ex fire insurance recovery: {pct(H225['ebitda']-fire, H225['sales']):.1f}%")
print(f"FY2025 EBIT {pct(FY25['ebit'], FY25['sales']):.1f}%; ex fire recovery net of 0.354m fire impairment: {pct(FY25['ebit']-fire+354, FY25['sales']):.1f}%")
print(f"FY2024 EBITDA as first reported {pct(FY24o['ebitda'], FY24r['sales']):.1f}% vs restated {pct(FY24r['ebitda'], FY24r['sales']):.1f}% (prior-period error CHF 2.369m)")
print(f"FY2024 GM as first reported {pct(FY24o['gp'], FY24r['sales']):.1f}% vs restated {pct(FY24r['gp'], FY24r['sales']):.1f}%")
print(f"H1 2025 EBITDA as first reported {pct(H125o['ebitda'], H125r['sales']):.1f}% vs restated {pct(H125r['ebitda'], H125r['sales']):.1f}%; GM {pct(H125o['gp'], H125r['sales']):.1f}% vs {pct(H125r['gp'], H125r['sales']):.1f}%")
# H2 2025 margin as implied by FY2025 deck (uses un-restated H1 2025)
h2_deck = FY25["ebitda"] - H125o["ebitda"]
print(f"H2 2025 EBITDA implied by FY2025 deck (FY - H1 as first reported): {h2_deck:,} = {pct(h2_deck, H225['sales']):.1f}% (deck shows 11.1%)")
print(f"H2 2025 EBITDA on consistent (restated) basis: {H225['ebitda']:,} = {pct(H225['ebitda'], H225['sales']):.1f}% vs H1 2025 restated {pct(H125r['ebitda'], H125r['sales']):.1f}%")
# FY2022 XP Power legal costs
h122 = dict(sales=267_498, ebitda=37_681, adj=46_700)   # see A.csv / A_notes.md for source rows
print(f"H1 2022 EBITDA {pct(h122['ebitda'], h122['sales']):.1f}%; adjusted ex XP Power trial cost {pct(h122['adj'], h122['sales']):.1f}%; implied one-off {h122['adj']-h122['ebitda']:,}")
fy22 = dict(sales=586_395, ebitda=118_913)
print(f"FY2022 EBITDA {pct(fy22['ebitda'], fy22['sales']):.1f}%; company adjusted 21.8% -> implied legal cost {0.218*fy22['sales']-fy22['ebitda']:,.0f} (approx., from rounded margin)")
fy18 = dict(sales=436_356, ebitda=42_966, loss=6_600)
print(f"FY2018 EBITDA (IFRS16 restated) {pct(fy18['ebitda'], fy18['sales']):.1f}%; ex CHF 6.6m loss on disposal of EBT US business {pct(fy18['ebitda']+fy18['loss'], fy18['sales']):.1f}%")
# FY2026 guidance
for lab, lo, hi in (("Jul-2026", 14.0, 17.0), ("Oct-2026", 17.0, 19.0)):
    print(f"FY2026 guidance {lab}: reported {lo}-{hi}%; ex ~3pp one-offs {lo+3:.1f}-{hi+3:.1f}% (Oct: 'up to' 3pp)")

print("\n-- Quarterly net sales (CHF m) --")
q = {"Q1 2025": 111.2, "Q2 2025": 227.2 - 111.2, "Q3 2025": 102.5, "Q4 2025": 457.0 - 329.6,
     "Q1 2026": 106.3, "Q2 2026": 133.5, "Q3 2026": 155.6,
     "Q1 2024": 80.9, "Q2 2024": 108.4, "Q3 2024": 113.2, "Q4 2024": 445.4 - 302.5}
for k in ("Q3 2025", "Q4 2025", "Q1 2026", "Q2 2026", "Q3 2026"):
    print(f"{k}: {q[k]:.1f}")
print(f"Q4 2025 YoY vs Q4 2024 ({q['Q4 2024']:.1f}): {yoy(q['Q4 2025'], q['Q4 2024']):.1f}%")
print(f"Q2 2026 YoY vs Q2 2025 ({q['Q2 2025']:.1f}): {yoy(q['Q2 2026'], q['Q2 2025']):.1f}%")
print(f"Q1 2026 + Q2 2026 = {106.3+133.5:.1f} vs H1 2026 239.8; 9M/26 = {239.834+155.6:.1f} vs reported 395.5")
ltm_q = q["Q4 2025"] + q["Q1 2026"] + q["Q2 2026"] + q["Q3 2026"]
prev_q = q["Q4 2024"] + q["Q1 2025"] + q["Q2 2025"] + q["Q3 2025"]
print(f"LTM to Sep-2026 net sales {ltm_q:.1f} vs prior LTM {prev_q:.1f}: {yoy(ltm_q, prev_q):.1f}%")

print("\n" + "=" * 70)
print("A2  ORDERS, BACKLOG, WORKING CAPITAL")
print("=" * 70)
orders = {"Q1 2025": 118.5, "H1 2025": 222.947, "9M 2025": 327.4, "Q3 2025 (as restated Oct-2026)": 102.1,
          "Q4 2025": 129.9, "Q1 2026": 144.9, "H1 2026": 354.843, "Q3 2026": 275.6}
q2_25 = orders["H1 2025"] - orders["Q1 2025"]
q3_25_implied = orders["9M 2025"] - orders["H1 2025"]
q2_26 = orders["H1 2026"] - orders["Q1 2026"]
fy25_orders = orders["9M 2025"] + orders["Q4 2025"]
print(f"Q2 2025 orders {q2_25:.1f} (b2b {q2_25/q['Q2 2025']:.2f})")
print(f"Q3 2025 orders implied by Oct-2025 release (9M - H1) {q3_25_implied:.1f} vs 102.1 stated in Oct-2026 release: diff {q3_25_implied-102.1:+.1f}")
print(f"Q3 2025 b2b {102.1/102.5:.2f} (using 102.1) / {q3_25_implied/102.5:.2f} (using implied)")
print(f"Q4 2025 b2b {orders['Q4 2025']/q['Q4 2025']:.2f}; FY2025 orders ~{fy25_orders:.1f}, b2b {fy25_orders/457.0:.2f}")
print(f"Q1 2026 b2b {orders['Q1 2026']/106.3:.2f}; Q2 2026 orders {q2_26:.1f}, b2b {q2_26/133.5:.2f}; Q3 2026 b2b {275.6/155.6:.2f}")
print(f"H1 2026 b2b {354.843/239.834:.2f}; H1 2025 b2b {222.947/227.154:.2f}")
print(f"Q1 2024: b2b stated 1.09 (Apr-2024) -> orders ~{80.9*1.09:.1f}; Q1/24 orders stated 91.0 in Apr-2025 -> b2b {91.0/80.9:.2f}")
# Backlog trend (year-end, CHF m)
bl = {2018: 113.9, 2019: 137.4, 2020: 166, 2021: 255, 2022: 200, 2023: 131, 2024: 140.7, 2025: 125.4}
print("Backlog YE: " + ", ".join(f"{k}: {v}" for k, v in bl.items()))
print(f"Backlog YE2025 / FY2025 sales = {125.4/457.0*12:.1f} months")
# Inventories
inv = {"YE2023": (66_028, 9_929, 27_473), "YE2024r": (63_409, 13_469, 27_870), "YE2025": (57_942, 11_877, 19_662)}
for k, (r, w, f) in inv.items():
    t = r + w + f
    print(f"Inventory {k}: total {t:,} raw {pct(r,t):.0f}% WIP {pct(w,t):.0f}% FG {pct(f,t):.0f}%")
cogs = {"FY2025": 283_367, "H1 2026": 140_472, "H2 2025": 283_367 - 137_399}
print(f"Inventory days YE2025: {89_481/cogs['FY2025']*365:.0f} (on FY COGS); H2-annualised {89_481/(cogs['H2 2025']*2)*365:.0f}")
print(f"Inventory days H1 2026: {113_699/(cogs['H1 2026']*2)*365:.0f} (H1 COGS x2); H1 2025: {102_733/(137_399*2)*365:.0f}")
# Receivables & DSO (trade and other receivables, net = financial assets at amortised cost)
rec = {"YE2024": (79_977, 445_362 - 189_315, 184), "H1 2025": (63_349, 227_154, 181), "YE2025": (65_838, H225['sales'], 184), "H1 2026": (78_605, 239_834, 181)}
for k, (r, s, d) in rec.items():
    print(f"DSO {k}: receivables {r:,} / half-year sales {s:,} x {d} days = {r/s*d:.0f} days")
print(f"DSO FY2025 on trade receivables net 63,169 / FY sales: {63_169/457_044*365:.0f} days; FY2024 77,347: {77_347/445_362*365:.0f} days")
print(f"Contract liabilities / LTM sales: YE2025 {pct(14_311, 457_044):.1f}%; H1 2026 {pct(21_232, ltm_sales):.1f}%")

print("\n" + "=" * 70)
print("A4  CONCENTRATION AND GEOGRAPHY")
print("=" * 70)
for y, china, tot in ((2020, 55_101, 395_816), (2021, 98_561, 513_721), (2022, 105_848, 586_395), (2023, 108_040, 397_453), (2024, 120_152, 445_362), (2025, 114_604, 457_044)):
    print(f"China share {y}: {pct(china, tot):.1f}%")
print(f"Asia share FY2025 {pct(289_842, 457_044):.1f}%; Malaysia {pct(71_204,457_044):.1f}%; North America {pct(81_578,457_044):.1f}%; Europe {pct(78_174,457_044):.1f}%")
print(f"North America share FY2022 {pct(221_944,586_395):.1f}% -> FY2023 {pct(92_736,397_453):.1f}%")
print(f"Asia share H1 2026 {pct(161_828,239_834):.1f}%, H1 2025 {pct(144_990,227_154):.1f}%; H2 2025 Asia {289_842-144_990:,} = {pct(289_842-144_990, H225['sales']):.1f}%")
print(f"H2 2025 NA {81_578-41_212:,}, Europe {78_174-37_651:,}, RoW {7_450-3_301:,}")
# semiconductor share, company sector definitions
print(f"PCT 'Semiconductor' sector / group sales FY2025 {pct(241_522,457_044):.1f}%, FY2024 {pct(226_719,445_362):.1f}%")
print(f"PCT semiconductor + IXS 'Electronics' FY2025 {pct(241_522+39_942,457_044):.1f}%, FY2024 {pct(226_719+47_702,445_362):.1f}%")
print(f"Largest customer share: 2020 32.4%, 2021 30.4%, 2022 36.1%, 2023 17.7%, 2024 23.8%, 2025 {pct(104_400,457_044):.1f}% (stated 22.8%)")

print("\n" + "=" * 70)
print("A5  BALANCE SHEET")
print("=" * 70)
for lab, cash, debt, lease_c, lease_nc, ebitda in (("YE2025", 96_587, 59_970, 5_485, 25_845, 46_335),
                                                    ("H1 2026", 69_792, 59_660, 5_326, 24_112, ltm_ebitda)):
    nd = debt + lease_c + lease_nc - cash
    print(f"{lab}: gross debt {debt:,} + leases {lease_c+lease_nc:,} - cash {cash:,} = net debt {nd:,} ; ex leases {debt-cash:,}; net debt/EBITDA {nd/ebitda:.2f}x")
print(f"Bond coupon cost: old 1.30% x 60m = {0.013*60:.2f}m/yr; new 2.00% x 60m = {0.02*60:.2f}m/yr")
print(f"Dividends paid: 2024 7,772; 2025 11,654; H1 2026 3,885; payout FY2025 0.50 x 7.77m sh = {0.5*7.766719:.2f}m vs NI 12.2m")
print(f"ORS: consideration 8,978; net assets 4,268; goodwill 4,710 ({pct(4_710,8_978):.0f}% of price)")
print(f"ebeam lamp business: cash 7,542 - price adj 261 - net assets 3,295 = gain {7_542-261-3_295:,} (reported 3,986)")
print(f"XP Power: jury USD 40m + fees/interest ~USD 19m = USD {40+19}m at stake (before success fee); at 0.809 CHF/USD = CHF {59*0.809:.1f}m")
