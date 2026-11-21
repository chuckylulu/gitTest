#!/usr/bin/env python3
"""A3 - MTP3 (FY2024-FY2026) target status.

MTP3 targets are three-year averages (company does not say whether a margin 'average' is the mean of
annual margins or total OI / total sales; both are shown). FY2026 is not finished: the status uses
FY2024 and FY2025 actuals and the FY2026 guidance current at 2026-11-21 (2026-10-28 version).
Units: JPY million (sales, NI), %, JPY (EPS).
"""


def mean(xs):
    return sum(xs) / len(xs)


# actuals
S24, OI24, NI24, EPS24 = 779707, 228161, 161177, 218.67       # A3-058, A3-059, A3-061, A3-062
S25, OI25, NI25, EPS25 = 1128610, 499120, 375353, 515.15      # A3-086, A3-087, A3-089, A3-090
# FY2026 current guidance (2026-10-28)
S26, OI26, NI26, EPS26 = 1863000, 967000, 741500, 1027.08     # A3-104, A3-105, A3-107, A3-108
# ROIC results (company definition) from IAR 2026
ROIC24, ROIC25 = 31.5, 54.4                                   # A3-249, A3-250
# Targets (JPY billion / % / JPY)
ORIG = dict(sales=(560, 700), opm=(22, 28), ni=(93, 147), roic=(18, 28), eps=(127, 202))   # A3-234..A3-238 (Jun 2024)
REV = dict(sales=(835, 930), opm=(33, 36), ni=(207, 248), roic=(34, 39), eps=(284, 341))   # A3-242..A3-246 (Oct 2025)
# FY2025 forecast as of Oct 2025 (used by the company in the revised targets, A3-248)
S25_OCT, NI25_OCT, EPS25_OCT = 950000, 275000, 378.06         # A3-076, A3-079, A3-080


def where(v, rng):
    lo, hi = rng
    return "below range" if v < lo else ("above range" if v > hi else "within range")


sales_avg = mean([S24, S25, S26]) / 1000
opm_mean = mean([OI24 / S24, OI25 / S25, OI26 / S26]) * 100
opm_aggr = (OI24 + OI25 + OI26) / (S24 + S25 + S26) * 100
ni_avg = mean([NI24, NI25, NI26]) / 1000
eps_avg = mean([EPS24, EPS25, EPS26])

print("MTP3 three-year average status (FY2024 actual, FY2025 actual, FY2026 guidance of 2026-10-28)")
print(f"  Annual OPM: FY2024 {OI24/S24*100:.1f}%, FY2025 {OI25/S25*100:.1f}%, FY2026 guidance {OI26/S26*100:.1f}%")
print(f"  Sales avg      JPY {sales_avg:,.1f} bn | original 560-700: {where(sales_avg, ORIG['sales'])} | revised 835-930: {where(sales_avg, REV['sales'])} ({(sales_avg/REV['sales'][1]-1)*100:+.1f}% vs top of revised range)")
print(f"  OPM avg (mean of annual margins) {opm_mean:.1f}% | original 22-28: {where(opm_mean, ORIG['opm'])} | revised 33-36: {where(opm_mean, REV['opm'])}")
print(f"  OPM avg (total OI / total sales) {opm_aggr:.1f}% | revised 33-36: {where(opm_aggr, REV['opm'])}")
print(f"  NI avg         JPY {ni_avg:,.1f} bn | original 93-147: {where(ni_avg, ORIG['ni'])} | revised 207-248: {where(ni_avg, REV['ni'])} ({(ni_avg/REV['ni'][1]-1)*100:+.1f}% vs top)")
print(f"  EPS avg        JPY {eps_avg:,.2f} | original 127-202: {where(eps_avg, ORIG['eps'])} | revised 284-341: {where(eps_avg, REV['eps'])} ({(eps_avg/REV['eps'][1]-1)*100:+.1f}% vs top)")
roic2 = mean([ROIC24, ROIC25])
roic_need = 3 * REV["roic"][1] - ROIC24 - ROIC25
print(f"  ROIC: FY2024 {ROIC24}%, FY2025 {ROIC25}%, two-year mean {roic2:.2f}%; FY2026 ROIC forecast not disclosed.")
print(f"        3-yr mean stays at or below the revised top (39%) only if FY2026 ROIC <= {roic_need:.1f}% (FY2025 was {ROIC25}%).")

print()
print("Sales needed in FY2026 to bring the 3-yr mean down to the top of each range (JPY bn):")
for lab, rng in [("original", ORIG["sales"]), ("revised", REV["sales"])]:
    need = 3 * rng[1] - S24 / 1000 - S25 / 1000
    print(f"  {lab}: FY2026 sales <= {need:,.1f} (current FY2026 guidance {S26/1000:,.1f}; 1H FY2026 actual alone 845.2, A3-217)")

print()
print("FY2026 figure implied by the Oct-2025 revised targets (company: targets combine actuals to FY2025 H1 with")
print("forecasts for FY2025 H2 and FY2026, A3-248). Assumes a simple arithmetic 3-year mean (not stated by the company):")
for lab, rng, a24, a25oct, now in [
    ("Sales (JPY bn)", REV["sales"], S24 / 1000, S25_OCT / 1000, S26 / 1000),
    ("Net income (JPY bn)", REV["ni"], NI24 / 1000, NI25_OCT / 1000, NI26 / 1000),
    ("Basic EPS (JPY)", REV["eps"], EPS24, EPS25_OCT, EPS26),
]:
    lo = 3 * rng[0] - a24 - a25oct
    hi = 3 * rng[1] - a24 - a25oct
    print(f"  {lab:20s}: implied FY2026 {lo:,.1f} - {hi:,.1f}; FY2026 initial guidance (Apr 2026) vs top: ", end="")
    init = {"Sales (JPY bn)": 1420.0, "Net income (JPY bn)": 465.5, "Basic EPS (JPY)": 641.61}[lab]   # A3-094, A3-097, A3-098
    print(f"{init:,.2f} ({(init/hi-1)*100:+.1f}%); current guidance {now:,.2f} ({(now/hi-1)*100:+.1f}%)")

print()
MTP2_ROIC_PR, MTP2_ROIC_SL = 21.2, 25.5   # A3-240 (press release 2024-06-25), A3-241 (slides 2024-06-25)
print(f"MTP2 (FY2021-23 avg.) ROIC printed on 2024-06-25: press release {MTP2_ROIC_PR}% vs slides {MTP2_ROIC_SL}% -> difference {MTP2_ROIC_SL-MTP2_ROIC_PR:.1f} pts")

# ---- added by verifier 2026-11-21: which MTP2 ROIC figure matches the company's own annual series? ----
ROIC21, ROIC22, ROIC23 = 28.4, 34.6, 13.5   # A3-306 (IAR 2026 p.77, 11-year table, same ROIC definition footnote)
m = mean([ROIC21, ROIC22, ROIC23])
print(f"Simple mean of annual ROIC FY2021-23 printed in IAR 2026 p.77: ({ROIC21} + {ROIC22} + {ROIC23}) / 3 = {m:.2f}% "
      f"-> {'equals' if round(m, 1) == MTP2_ROIC_SL else 'DIFFERS FROM'} the slides figure {MTP2_ROIC_SL}% (A3-241, A3-305) to one decimal; differs from the press-release / 82nd securities-report "
      f"figure {MTP2_ROIC_PR}% (A3-240, A3-304) by {m - MTP2_ROIC_PR:.1f} pts. The company does not state how the MTP2 average was computed.")
ROIC24_P77, ROIC25_P77 = 31.5, 54.4   # IAR 2026 p.77 (same table as A3-306)
print(f"Cross-check: IAR p.77 FY2024 ROIC {ROIC24_P77}% / FY2025 {ROIC25_P77}% vs IAR p.22 {ROIC24}% / {ROIC25}% (A3-249, A3-250): "
      f"{'same' if (ROIC24_P77, ROIC25_P77) == (ROIC24, ROIC25) else 'DIFFERENT'}")
