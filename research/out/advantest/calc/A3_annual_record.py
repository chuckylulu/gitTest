#!/usr/bin/env python3
"""A3 - Advantest annual guidance record, FY2022 (context) and FY2023-FY2025, plus FY2026 revisions.

Fiscal year ends 31 March; Advantest names a fiscal year by its start year
(FY2025 = Apr 2025-Mar 2026). All inputs in JPY million (EPS in JPY), hard-coded
from research/out/advantest/parts/A3.csv (evidence id in each comment).

Classification rule (stated once, used everywhere in A3):
  diff% = (actual - guidance) / guidance * 100
  beat     : diff% >  +2.0
  in-line  : -2.0 <= diff% <= +2.0
  miss     : diff% <  -2.0
A +/-5% band is printed as a sensitivity check.
"""

BAND, BAND2 = 2.0, 5.0


def pct(a, g):
    return (a - g) / g * 100.0


def cls(d, band=BAND):
    return "beat" if d > band else ("miss" if d < -band else "in-line")


# version: (label, date, {metric: value})
FY = {
    "FY2022 (context; Apr 2022-Mar 2023)": {
        "versions": [
            # A3-012, A3-013, A3-014 (Q3 tanshin 2023-01-31, 'Revision ... No')
            ("maintained at Q3", "2023-01-31", {"sales": 550000, "oi": 170000, "ni": 130000}),
        ],
        # A3-015, A3-016, A3-017
        "actual": {"sales": 560191, "oi": 167687, "ni": 130400},
    },
    "FY2023 (Apr 2023-Mar 2024)": {
        "versions": [
            # A3-018..A3-021
            ("initial", "2023-04-26", {"sales": 480000, "oi": 105000, "ibt": 103500, "ni": 78000}),
            # A3-022 (maintained at Q1; same figures as initial)
            ("Q1 maintained", "2023-07-26", {"sales": 480000, "oi": 105000, "ibt": 103500, "ni": 78000}),
            # A3-023..A3-026
            ("Q2 revision", "2023-10-31", {"sales": 470000, "oi": 80000, "ibt": 78500, "ni": 60000}),
            # A3-028..A3-031
            ("Q3 revision (latest)", "2024-01-31", {"sales": 480000, "oi": 85000, "ibt": 82500, "ni": 64500}),
        ],
        # A3-032..A3-035
        "actual": {"sales": 486507, "oi": 81628, "ibt": 78170, "ni": 62290},
    },
    "FY2024 (Apr 2024-Mar 2025)": {
        "versions": [
            # A3-040..A3-043
            ("initial", "2024-04-26", {"sales": 525000, "oi": 90000, "ibt": 89000, "ni": 67000}),
            # A3-044..A3-047
            ("Q1 revision", "2024-07-31", {"sales": 600000, "oi": 138000, "ibt": 138500, "ni": 105000}),
            # A3-048..A3-052
            ("Q2 revision", "2024-10-30", {"sales": 640000, "oi": 165000, "ibt": 162500, "ni": 122000, "eps": 165.01}),
            # A3-053..A3-057
            ("Q3 revision (latest)", "2025-01-29", {"sales": 740000, "oi": 226000, "ibt": 225000, "ni": 167500, "eps": 227.74}),
        ],
        # A3-058..A3-062
        "actual": {"sales": 779707, "oi": 228161, "ibt": 224774, "ni": 161177, "eps": 218.67},
    },
    "FY2025 (Apr 2025-Mar 2026)": {
        "versions": [
            # A3-066..A3-070
            ("initial", "2025-04-25", {"sales": 755000, "oi": 242000, "ibt": 240000, "ni": 179000, "eps": 243.96}),
            # A3-071..A3-075
            ("Q1 revision", "2025-07-29", {"sales": 835000, "oi": 300000, "ibt": 297000, "ni": 221500, "eps": 302.71}),
            # A3-076..A3-080
            ("Q2 revision", "2025-10-28", {"sales": 950000, "oi": 374000, "ibt": 371500, "ni": 275000, "eps": 378.06}),
            # A3-081..A3-085
            ("Q3 revision (latest)", "2026-01-28", {"sales": 1070000, "oi": 454000, "ibt": 452500, "ni": 328500, "eps": 452.34}),
        ],
        # A3-086..A3-090
        "actual": {"sales": 1128610, "oi": 499120, "ibt": 516720, "ni": 375353, "eps": 515.15},
    },
}

FY2026 = [
    # A3-094..A3-098
    ("initial", "2026-04-27", {"sales": 1420000, "oi": 627500, "ibt": 629000, "ni": 465500, "eps": 641.61}),
    # A3-099..A3-103
    ("Q1 revision", "2026-07-29", {"sales": 1714000, "oi": 846000, "ibt": 891000, "ni": 660000, "eps": 911.64}),
    # A3-104..A3-108
    ("Q2 revision (current at 2026-11-21)", "2026-10-28", {"sales": 1863000, "oi": 967000, "ibt": 1021500, "ni": 741500, "eps": 1027.08}),
]

# One-off items named by management (JPY million)
FY23_IMPAIRMENT = 8998      # A3-036 (in OI, Q4 FY2023)
FY23_SETTLEMENT = 3179      # A3-038 (income, in OI)
FY23_DTA = 3800             # A3-039 (approx. JPY 3.8 bn, raises net income)
FY24_IMPAIRMENT = 21393     # A3-063 (in OI, Q4 FY2024)
FY25_DIVEST_GAIN = 2504     # A3-091 (in OI, Q1 FY2025)
FY25_CALLOPT_GAIN = 17312   # A3-092 (financial income, Q4 FY2025)

ORDER = ["sales", "oi", "ibt", "ni", "eps"]
NAMES = {"sales": "Net sales", "oi": "Operating income", "ibt": "Income before tax", "ni": "Net income", "eps": "Basic EPS (JPY)"}

print("A3 annual guidance record (JPY million; EPS in JPY). Rule: beat > +2%, in-line within +/-2%, miss < -2%.\n")
for fy, d in FY.items():
    print("=" * 100)
    print(fy)
    vs = d["versions"]
    act = d["actual"]
    # revision steps
    print("  Revision path:")
    prev = None
    for lab, date, v in vs:
        parts = []
        for m in ORDER:
            if m in v:
                s = f"{NAMES[m]} {v[m]:,}" if m != "eps" else f"EPS {v[m]:.2f}"
                if prev and m in prev:
                    s += f" ({pct(v[m], prev[m]):+.1f}% vs prior)"
                parts.append(s)
        print(f"    {date} {lab:22s}: " + "; ".join(parts))
        prev = v
    if "ibt" in vs[-1] and "oi" in vs[-1]:
        lab, date, v = vs[-1]
        print(f"    latest guidance operating margin {v['oi']/v['sales']*100:.1f}%; actual {act['oi']/act['sales']*100:.1f}%")
    init = vs[0][2]
    latest = vs[-1][2]
    print("  Actual vs guidance:")
    for m in ORDER:
        if m not in act:
            continue
        a = act[m]
        row = f"    {NAMES[m]:18s} actual {a:>12,.2f}" if m == "eps" else f"    {NAMES[m]:18s} actual {a:>12,}"
        if fy.startswith("FY2022"):
            row += " | vs initial: not recorded here (context row: Q3-maintained version only)"
        elif m in init:
            di = pct(a, init[m])
            row += f" | vs initial {init[m]:,} : {di:+7.1f}% {cls(di):7s}"
        else:
            row += " | vs initial: no EPS in initial guidance            "
        if m in latest:
            dl = pct(a, latest[m])
            row += f" | vs latest {latest[m]:,} : {dl:+6.1f}% {cls(dl):7s} (+/-5% band: {cls(dl, BAND2)})"
        print(row)
    print()

print("=" * 100)
print("One-off adjusted comparisons vs LATEST guidance (management-named items; guidance documents do not say whether the items were included)")
# FY2023
oi23 = 81628            # A3-033
g23 = 85000             # A3-029
oi23_x_imp = oi23 + FY23_IMPAIRMENT
oi23_x_both = oi23 + FY23_IMPAIRMENT - FY23_SETTLEMENT
print(f"  FY2023 OI reported {oi23:,} vs latest {g23:,}: {pct(oi23, g23):+.1f}% ({cls(pct(oi23, g23))})")
print(f"  FY2023 OI ex goodwill impairment {oi23_x_imp:,}: {pct(oi23_x_imp, g23):+.1f}% ({cls(pct(oi23_x_imp, g23))})")
print(f"  FY2023 OI ex impairment and ex settlement income {oi23_x_both:,}: {pct(oi23_x_both, g23):+.1f}% ({cls(pct(oi23_x_both, g23))})")
print(f"  FY2023 OPM reported {oi23/486507*100:.1f}% (A3-032); ex impairment {oi23_x_imp/486507*100:.1f}%; ex both {oi23_x_both/486507*100:.1f}%")
ni23 = 62290            # A3-035
gni23 = 64500           # A3-031
print(f"  FY2023 NI reported {ni23:,} vs latest {gni23:,}: {pct(ni23, gni23):+.1f}%; NI ex DTA benefit (approx. 3,800) {ni23-FY23_DTA:,}: {pct(ni23-FY23_DTA, gni23):+.1f}%  (after-tax effect of impairment not disclosed)")
# FY2024
oi24 = 228161           # A3-059
g24 = 226000            # A3-054
ibt24, gibt24 = 224774, 225000   # A3-060, A3-055
ni24, gni24 = 161177, 167500     # A3-061, A3-056
oi24x = oi24 + FY24_IMPAIRMENT
print(f"  FY2024 OI reported {oi24:,} vs latest {g24:,}: {pct(oi24, g24):+.1f}%; ex impairment {oi24x:,}: {pct(oi24x, g24):+.1f}% ({cls(pct(oi24x, g24))})")
print(f"  FY2024 OPM reported {oi24/779707*100:.1f}% (A3-058); ex impairment {oi24x/779707*100:.1f}%")
print(f"  FY2024 IBT reported {ibt24:,}; ex impairment {ibt24+FY24_IMPAIRMENT:,}: {pct(ibt24+FY24_IMPAIRMENT, gibt24):+.1f}% vs latest {gibt24:,}")
t_g = (gibt24 - gni24) / gibt24 * 100
t_a = (ibt24 - ni24) / ibt24 * 100
print(f"  FY2024 tax charge implied by latest guidance (IBT-NI)/IBT = {t_g:.1f}%; actual = {t_a:.1f}%  -> NI miss {pct(ni24, gni24):+.1f}% with IBT {pct(ibt24, gibt24):+.1f}%")
print(f"  FY2024 NI at the guidance-implied tax share: {ibt24*(1-t_g/100):,.0f} ({pct(ibt24*(1-t_g/100), gni24):+.1f}% vs guidance) - shows the NI shortfall sits below IBT")
# FY2025
oi25, g25 = 499120, 454000          # A3-087, A3-082
ibt25, gibt25 = 516720, 452500      # A3-088, A3-083
oi25x = oi25 - FY25_DIVEST_GAIN
ibt25x = ibt25 - FY25_DIVEST_GAIN - FY25_CALLOPT_GAIN
print(f"  FY2025 OI reported {oi25:,} ({pct(oi25, g25):+.1f}%); ex divestiture gain {oi25x:,}: {pct(oi25x, g25):+.1f}% ({cls(pct(oi25x, g25))})")
print(f"  FY2025 OPM reported {oi25/1128610*100:.1f}% (A3-086); ex divestiture gain {oi25x/1128610*100:.1f}%")
print(f"  FY2025 IBT reported {ibt25:,} ({pct(ibt25, gibt25):+.1f}%); ex divestiture and call-option gains {ibt25x:,}: {pct(ibt25x, gibt25):+.1f}% ({cls(pct(ibt25x, gibt25))})")

print()
print("=" * 100)
print("FY2026 (Apr 2026-Mar 2027) guidance path (year in progress)")
prev = None
for lab, date, v in FY2026:
    parts = []
    for m in ORDER:
        s = f"{NAMES[m]} {v[m]:,}" if m != "eps" else f"EPS {v[m]:.2f}"
        if prev:
            s += f" ({pct(v[m], prev[m]):+.1f}%)"
        parts.append(s)
    print(f"  {date} {lab}: " + "; ".join(parts) + f"; implied OPM {v['oi']/v['sales']*100:.1f}%")
    prev = v
i0, il = FY2026[0][2], FY2026[-1][2]
print("  Current vs initial: " + "; ".join(f"{NAMES[m]} {pct(il[m], i0[m]):+.1f}%" for m in ORDER))

print()
print("=" * 100)
print("Late-period flags: guidance standing after the Q3 release (no later revision found in the news index) that the year-end result missed by more than 2%")
for fy, d in FY.items():
    lab, date, v = d["versions"][-1]
    act = d["actual"]
    miss = [f"{NAMES[m]} {pct(act[m], v[m]):+.1f}%" for m in ORDER if m in v and m in act and cls(pct(act[m], v[m])) == "miss"]
    print(f"  {fy}: guidance of {date} ({lab}) -> " + (", ".join(miss) if miss else "no metric missed"))
