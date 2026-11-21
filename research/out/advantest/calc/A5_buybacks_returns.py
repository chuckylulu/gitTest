"""A5 - share repurchases, dividends, total return ratio (JPY million unless stated).

Fiscal year ends 31 March. FY2024 = Apr 2024-Mar 2025; FY2025 = Apr 2025-Mar 2026; FY2026 = Apr 2026-Mar 2027.
Company definition: total return ratio = (dividend + share repurchase) / consolidated net income (A5-092).
Dividends are counted by record date within the fiscal year (interim + year-end) - an assumption; the
company does not state whether it counts dividends by record date or payment date.
Buybacks are counted in the fiscal year in which shares were acquired (yen, excluding commissions).
"""

YEN = 1e6  # yen per JPY million

programs = {
    # name: authorised shares, authorised yen, executed shares, executed yen, ids
    "Oct-2024 (FY2024)": (9_000_000, 50_000_000_000, 5_711_000, 49_999_998_563, "A5-094,A5-095"),
    "Apr-2025 (FY2025)": (19_000_000, 70_000_000_000, 6_643_900, 69_999_937_500, "A5-096,A5-097"),
    "Oct-2025 (FY2025-26)": (18_000_000, 150_000_000_000, 5_759_000, 149_996_716_000, "A5-098,A5-101"),
    "Oct-2026 (FY2026, to 31 Oct 2026)": (11_000_000, 280_000_000_000, 420_900, 14_563_326_000, "A5-102,A5-104"),
}
# split of the Oct-2025 programme by fiscal year
OCT25_FY2025 = (2_048_700, 44_228_372_000)    # A5-099 (ISR 84th, acquired in FY ended Mar 2026)
OCT25_1H_FY2026 = (3_710_300, 105_768_344_000)  # A5-100 (semi-annual report, acquired Apr-Sep 2026)

print("Programme utilisation (executed / authorised)")
for k, (sh_a, y_a, sh_e, y_e, ids) in programs.items():
    print(f"  {k:34s} shares {sh_e:>11,d}/{sh_a:>11,d} = {sh_e/sh_a*100:5.1f}%   yen {y_e/1e9:8.2f}bn/{y_a/1e9:6.1f}bn = {y_e/y_a*100:5.1f}%   [{ids}]")

s = OCT25_FY2025[0] + OCT25_1H_FY2026[0]; y = OCT25_FY2025[1] + OCT25_1H_FY2026[1]
print(f"Oct-2025 split check: shares {s:,d} vs {programs['Oct-2025 (FY2025-26)'][2]:,d}; yen {y:,d} vs {programs['Oct-2025 (FY2025-26)'][3]:,d} -> match={s == programs['Oct-2025 (FY2025-26)'][2] and y == programs['Oct-2025 (FY2025-26)'][3]}")

buyback_by_fy = {
    "FY2023": 0.0,                                               # A5-093: no board-resolved acquisition in FY2023
    "FY2024": programs["Oct-2024 (FY2024)"][3] / YEN,
    "FY2025": (programs["Apr-2025 (FY2025)"][3] + OCT25_FY2025[1]) / YEN,
    "FY2026 1H": OCT25_1H_FY2026[1] / YEN,
    "FY2026 Oct 29-31": programs["Oct-2026 (FY2026, to 31 Oct 2026)"][3] / YEN,
}
div_by_fy = {   # record-date basis
    "FY2024": 14047 + 14674,   # A5-110 interim (rec. 30 Sep 2024) + A5-111 year-end (rec. 31 Mar 2025)
    "FY2025": 21094 + 21765,   # A5-112 interim + A5-113 year-end
    "FY2026 1H": 35376,        # A5-114 interim (rec. 30 Sep 2026)
}
ni = {"FY2024": 161177, "FY2025": 375353, "FY2026 1H": 368083}   # A5-120 (FY2024, FY2025), A5-121 (1H FY2026)

print("\nBuybacks executed by fiscal year (JPY million):")
for k, v in buyback_by_fy.items():
    print(f"  {k:18s} {v:12,.1f}")

print("\nTotal return ratio by period (company formula, dividends on record-date basis):")
tot_ret, tot_ni = 0.0, 0.0
for k in ["FY2024", "FY2025", "FY2026 1H"]:
    r = div_by_fy[k] + buyback_by_fy[k]
    tot_ret += r; tot_ni += ni[k]
    print(f"  {k:10s} dividends {div_by_fy[k]:9,.0f} + buybacks {buyback_by_fy[k]:10,.1f} = {r:10,.1f}; NI {ni[k]:9,.0f}; ratio {r/ni[k]*100:5.1f}%")
print(f"  MTP3 cumulative FY2024 to FY2026 1H: returns {tot_ret:,.1f} / NI {tot_ni:,.0f} = {tot_ret/tot_ni*100:.1f}%")
r_plus = tot_ret + buyback_by_fy["FY2026 Oct 29-31"]
print(f"  same incl. buybacks 29-31 Oct 2026 (NI unchanged, i.e. mixed periods): {r_plus:,.1f} / {tot_ni:,.0f} = {r_plus/tot_ni*100:.1f}%")

# remaining authorisation under Oct-2026 programme vs cash at 30 Sep 2026
rem = (programs["Oct-2026 (FY2026, to 31 Oct 2026)"][1] - programs["Oct-2026 (FY2026, to 31 Oct 2026)"][3]) / YEN
cash_sep26 = 401785   # A5-017
print(f"\nOct-2026 programme remaining authorisation after 31 Oct 2026: {rem:,.1f} JPY million = {rem/cash_sep26*100:.1f}% of cash at 30 Sep 2026 ({cash_sep26:,d})")

# cancellation
cancelled, before = 34_141_256, 766_141_256   # A5-105, A5-106
print(f"\nTreasury share cancellation 6 Feb 2026: {cancelled:,d} of {before:,d} = {cancelled/before*100:.2f}%; shares after = {before - cancelled:,d}")

# dividend per share growth
dps = {"FY2022": 33.75, "FY2023": 34.25, "FY2024": 39.00, "FY2025": 59.00}   # A5-115..A5-118 (split-adjusted)
print("\nDPS (split-adjusted, yen):", dps)
print(f"  FY2025 vs FY2024 DPS change: {(dps['FY2025']/dps['FY2024']-1)*100:.1f}%;  FY2026 interim 49 vs FY2025 interim 29: {(49/29-1)*100:.1f}%")
