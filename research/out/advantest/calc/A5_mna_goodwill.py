"""A5 - acquisitions Nov 2021 - Nov 2026: consideration, goodwill, impairments, headroom (JPY million).

Fiscal year ends 31 March.
"""
deals = {
    # name: (closing date, consideration, goodwill final, acquisition-related expense, cash outflow line, ids)
    "R&D Altanova (US)": ("2021-11-17", 25521, 18946, 746, 28976, "A5-131..A5-136"),
    "CREA (Italy)": ("2022-08-10", 4167, 1449, 232, 3505, "A5-139..A5-143"),
    "Shin Puu Technology (Taiwan)": ("2023-04-28", 7497, 2522, 595, 8260, "A5-145..A5-149"),
    "Salland Engineering (Netherlands)": ("2024-04-02", 4818, 3004, 566, 3815, "A5-150..A5-154"),
}
tc = tg = te = tcash = 0
print(f"{'deal':34s} {'closed':10s} {'consid.':>8s} {'goodwill':>8s} {'GW/cons':>7s} {'acq.exp':>7s} {'cash out':>8s}")
for k, (d, c, g, e, co, ids) in deals.items():
    tc += c; tg += g; te += e; tcash += co
    print(f"{k:34s} {d:10s} {c:8,d} {g:8,d} {g/c*100:6.1f}% {e:7,d} {co:8,d}   [{ids}]")
print(f"{'TOTAL':34s} {'':10s} {tc:8,d} {tg:8,d} {tg/tc*100:6.1f}% {te:7,d} {tcash:8,d}")

# R&D Altanova PPA revision
prov_gw, final_gw = 25282, 18946    # A5-133 provisional and final
print(f"\nR&D Altanova goodwill PPA revision: {final_gw - prov_gw:,d} ({(final_gw/prov_gw-1)*100:.1f}%)")

# impairments recognised in the window (from goodwill/intangibles movement tables)
imp = {"FY2021": 0, "FY2022": 0, "FY2023": 8998, "FY2024": 21393, "FY2025": 0}   # A5-166, A5-167, A5-168, A5-181, A5-182
print("\nImpairment losses on goodwill and intangibles by fiscal year:", imp, "total", sum(imp.values()))
essai_consideration = 33576   # A5-170 (acquired Jan 2020, before the 5-year window)
print(f"Essai cumulative impairment {imp['FY2023'] + imp['FY2024']:,d} = {(imp['FY2023'] + imp['FY2024'])/essai_consideration*100:.1f}% of its consideration {essai_consideration:,d}")

# R&D Altanova CGU impairment headroom (pre-tax discount rate)
hr = {"31 Mar 2025": (19.4, 22.9), "31 Mar 2026": (20.2, 22.5)}   # A5-176, A5-177
for k, (used, brk) in hr.items():
    print(f"R&D Altanova group {k}: discount rate used {used}% vs break-even {brk}% -> headroom {brk - used:.1f} pp")

# R&D Altanova CGU goodwill trajectory (includes Shin Puu from FY2023 - inference)
cgu = {"2023-03-31": 22029, "2024-03-31": 27826, "2025-03-31": 27479, "2026-03-31": 29383}  # A5-179, A5-171
print("R&D Altanova CGU goodwill:", cgu, "; change Mar23->Mar24", cgu["2024-03-31"] - cgu["2023-03-31"])

# goodwill + intangibles relative to equity
gi = {"2026-03-31": (84250, 795726), "2026-09-30": (82520, 1145135)}   # A5-165 / A5-007 ; A5-022 / A5-023
for k, (g, eq) in gi.items():
    print(f"Goodwill+intangibles / total equity at {k}: {g:,d}/{eq:,d} = {g/eq*100:.1f}%")
gw_mar26 = 65690   # A5-165
print(f"Goodwill only / equity at 2026-03-31: {gw_mar26/795726*100:.1f}%")

# partial divestiture FY2025
print("\nPartial divestiture FY2025 [A5-156, A5-157] (Apr-Sep 2025): proceeds 2,902, gain 2,504 -> implied carrying amount of net assets/costs disposed", 2902 - 2504)
