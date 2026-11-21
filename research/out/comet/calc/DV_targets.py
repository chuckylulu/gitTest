#!/usr/bin/env python3
"""DV module: Comet mid-term targets (CMD 2025, CMD 2023, 2019 targets) vs results so far.

FY = calendar year. CHF million. Inputs from evidence rows (ids in comments).
"Latest actual" = FY2025 (Jan-Dec 2025) and LTM to Jun 2026 (H2 2025 + H1 2026, on the
corrected basis: FY2025 minus restated H1 2025 plus H1 2026). Gap = target - actual.
Required CAGR = growth per year needed from FY2025 to reach the target in the target year.
"""

# ---- actuals (CHF m), from DV_halfyears.py inputs (DV-001..040)
FY25 = dict(GRP=(457.044, 46.335), PCT=(257.102, 40.407), IXS=(110.816, -7.516), IXM=(99.078, 15.771))
H1_25R = dict(GRP=(227.154, 22.978), PCT=(134.262, 23.421), IXS=(48.689, -7.520), IXM=(48.402, 8.322))
H1_26 = dict(GRP=(239.834, 31.367), PCT=(143.570, 28.947), IXS=(48.739, -3.985), IXM=(53.539, 8.630))
FY24 = dict(GRP=(445.362, 60.380), PCT=(247.391, 52.734), IXS=(115.888, -4.306), IXM=(94.571, 14.567))  # as first reported
FY24R = dict(GRP=(445.362, 58.011), PCT=(247.391, 50.365))  # restated
EXT25 = dict(PCT=257.102, IXS=110.804, IXM=89.137, GRP=457.044)  # external sales FY2025 (DV-034)
EXT_H126 = dict(PCT=143.570, IXS=48.734, IXM=47.530, GRP=239.834)
ROCE_FY25, ROCE_H126 = 5.2, 8.7  # % (DV-085, DV-086)
GUIDE26_SALES, GUIDE26_MARGIN = (570, 590), (17.0, 19.0)  # FY2026 guidance raised Oct 2026 (DV-087)

LTM = {k: (FY25[k][0] - H1_25R[k][0] + H1_26[k][0], FY25[k][1] - H1_25R[k][1] + H1_26[k][1]) for k in FY25}


def m(t):
    return 100 * t[1] / t[0]


def cagr(a, b, n):
    return 100 * ((b / a) ** (1 / n) - 1)


print("Actuals (CHF m, EBITDA margin on total division net sales)")
for k in ["GRP", "PCT", "IXS", "IXM"]:
    s = f"{k}: FY2024 orig {FY24[k][0]:.1f} / {m(FY24[k]):.1f}%"
    if k in FY24R:
        s += f" (restated {m(FY24R[k]):.1f}%)"
    s += f"; FY2025 {FY25[k][0]:.1f} / {m(FY25[k]):.1f}%; LTM Jun-2026 {LTM[k][0]:.1f} / EBITDA {LTM[k][1]:.1f} / {m(LTM[k]):.1f}%"
    print(s)

print("\nCMD 2025 (13 Nov 2025) targets for next peak of cycle, assumed 2028 (DV-070..076)")
T25 = [("GRP sales", (670, 770), "sales", "GRP"), ("GRP EBITDA margin", (22, 27), "margin", "GRP"),
       ("PCT sales", (430, 480), "sales", "PCT"), ("PCT EBITDA margin", (27, 33), "margin", "PCT"),
       ("IXS sales", (130, 160), "sales", "IXS"), ("IXS EBITDA margin", (5, 9), "margin", "IXS"),
       ("IXM sales", (110, 130), "sales", "IXM"), ("IXM EBITDA margin", (23, 27), "margin", "IXM")]
for name, (lo, hi), kind, k in T25:
    if kind == "sales":
        a25, al = FY25[k][0], LTM[k][0]
        print(f"{name:20s} target {lo}-{hi}; FY2025 {a25:.1f} (gap {lo-a25:+.1f} to {hi-a25:+.1f}); "
              f"LTM {al:.1f}; required CAGR FY2025->2028 {cagr(a25, lo, 3):.1f}% to {cagr(a25, hi, 3):.1f}%")
    else:
        a25, al = m(FY25[k]), m(LTM[k])
        print(f"{name:20s} target {lo}-{hi}%; FY2025 {a25:.1f}% (gap {lo-a25:+.1f} to {hi-a25:+.1f} pp); "
              f"LTM {al:.1f}% (gap {lo-al:+.1f} to {hi-al:+.1f} pp)")
print(f"{'GRP ROCE':20s} target 27-32%; FY2025 {ROCE_FY25}% (gap {27-ROCE_FY25:+.1f} to {32-ROCE_FY25:+.1f} pp); H1 2026 {ROCE_H126}%")
print(f"FY2026 guidance (Oct 2026): sales {GUIDE26_SALES}, EBITDA margin {GUIDE26_MARGIN}% reported incl. up to 3pp one-offs; "
      f"growth FY2026 mid -> 2028 low/high target: {cagr(sum(GUIDE26_SALES)/2, 670, 2):.1f}% / {cagr(sum(GUIDE26_SALES)/2, 770, 2):.1f}% p.a.")

print("\nDivisional share of group external sales vs CMD ranges")
for k, (c23, c25) in dict(PCT=((60, 70), (60, 70)), IXS=((20, 25), (15, 25)), IXM=((10, 15), (10, 20))).items():
    print(f"{k}: CMD2023 {c23}% / CMD2025 {c25}%; actual FY2025 {100*EXT25[k]/EXT25['GRP']:.1f}%, "
          f"H1 2026 {100*EXT_H126[k]/EXT_H126['GRP']:.1f}%")

print("\nCMD 2023 (9 Nov 2023) targets for peak of cycle then assumed 2027 (DV-077..079)")
for name, (lo, hi), act in [("GRP sales", (800, 900), FY25["GRP"][0]), ("GRP EBITDA margin", (25, 30), m(FY25["GRP"])),
                            ("GRP ROCE", (30, 35), ROCE_FY25)]:
    print(f"{name:20s} target {lo}-{hi}; FY2025 actual {act:.1f}; gap {lo-act:+.1f} to {hi-act:+.1f}")
print(f"CMD 2023 -> CMD 2025 change: sales midpoint {850} -> {720} ({100*(720/850-1):.1f}%), "
      f"margin midpoint 27.5% -> 24.5%, ROCE midpoint 32.5% -> 29.5%, POC year 2027 -> 2028")
print(f"FX check (company says revision 'essentially unchanged in constant currencies'): 850 x 0.70/0.90 = {850*0.70/0.90:.0f} "
      f"(upper bound, assumes all sales USD-linked)")
print("2019 targets for 2025 (DV-080): sales > 830, EBITDA ~25%, ROCE ~30%; "
      f"FY2025 actual {FY25['GRP'][0]:.1f} ({FY25['GRP'][0]-830:+.1f}), {m(FY25['GRP']):.1f}% ({m(FY25['GRP'])-25:+.1f} pp), ROCE {ROCE_FY25}%")
print("FY2023 targets set 2019 (CMD 2023 slide, DV-079): sales 380-400, EBITDA 7-9%; "
      f"FY2023 actual 397.5 / {100*44.996/397.453:.1f}%")

print("\nIXS CMD 2025 bridge items (DV-074): CA20 2024 investment CHF 10-15m -> '> break-even' 2028e; non-semi 5-10% -> >10%")
print(f"IXS EBITDA FY2025 {FY25['IXS'][1]:.1f}; LTM {LTM['IXS'][1]:.1f}; 2028 target at 5-9% of 130-160 = "
      f"{0.05*130:.1f} to {0.09*160:.1f}; swing needed from LTM: {0.05*130-LTM['IXS'][1]:+.1f} to {0.09*160-LTM['IXS'][1]:+.1f}")
print(f"Efficiency program (DV-088): CHF 20-30m sustainable EBITDA improvement p.a. from 2028 = "
      f"{100*20/670:.1f}-{100*30/670:.1f} pp of the 670 low-end target sales")
