#!/usr/bin/env python3
"""A3 guidance record for Comet Holding AG (FY = calendar year). Inputs: guidance ranges and
reported results from evidence rows in research/out/comet/parts/A.csv (ids in comments).
Classification rule: actual inside [low, high] (inclusive, on the rounding used by the company)
= in-line; above high = beat; below low = miss. Guidance "at the lower end of" a range keeps the
range: actual >= low end and <= high = in-line (the company did not quantify "lower end").
Run: python3 -I research/out/comet/calc/A_guidance.py
"""

# (FY, metric, [(date, label, low, high, src)], actual, actual_note)
REC = [
    ("FY2018", "net sales CHF m", [("Aug-2018", "reiterated", 440, 460, "A-088")], 436.4, "A-190"),
    ("FY2018", "EBITDA margin %", [("Aug-2018", "reiterated", 10.0, 12.0, "A-088")], 8.7, "as reported pre-IFRS16 (A-147)"),
    ("FY2019", "net sales CHF m", [("Aug-2019", "given", 350, 370, "A-089")], 371.6, "A-190"),
    ("FY2019", "EBITDA margin %", [("Aug-2019", "given", 7.0, 8.5, "A-089")], 10.8, "A-190 / A-191"),
    ("FY2021", "net sales CHF m", [("Aug-2021", "given", 480, 500, "A-090")], 513.7, "A-190"),
    ("FY2021", "EBITDA margin %", [("Aug-2021", "given", 18.0, 20.0, "A-090")], 20.0, "A-190 / A-191"),
    ("FY2022", "net sales CHF m", [("Mar-2022", "initial", 570, 610, "A-091"), ("Jul-2022", "narrowed", 580, 610, "A-092"),
                                   ("Oct-2022", "confirmed", 580, 610, "A-093")], 586.4, "A-017"),
    ("FY2022", "EBITDA margin %", [("Mar-2022", "initial", 21.0, 23.0, "A-091"), ("Jul-2022", "narrowed", 21.0, 23.0, "A-092"),
                                   ("Oct-2022", "confirmed", 21.0, 23.0, "A-093")], 20.3, "A-019 (company-adjusted ex XP Power legal: 21.8%, A-094)"),
    ("FY2023", "net sales CHF m", [("Apr-2023", "initial", 440, 480, "A-097"), ("Jul-2023", "lower end", 440, 480, "A-098"),
                                   ("Oct-2023", "cut", 380, 400, "A-099")], 397.5, "A-017"),
    ("FY2023", "EBITDA margin %", [("Apr-2023", "initial", 13.0, 15.0, "A-097"), ("Jul-2023", "lower end", 13.0, 15.0, "A-098"),
                                   ("Oct-2023", "cut", 7.0, 9.0, "A-099")], 11.3, "A-019"),
    ("FY2024", "net sales CHF m", [("Mar-2024", "initial", 440, 480, "A-102"), ("Apr-2024", "confirmed", 440, 480, "A-103"),
                                   ("Jul-2024", "confirmed", 440, 480, "A-104"), ("Oct-2024", "lower end", 440, 480, "A-105")], 445.4, "A-107"),
    ("FY2024", "EBITDA margin %", [("Mar-2024", "initial", 15.0, 17.0, "A-102"), ("Apr-2024", "confirmed", 15.0, 17.0, "A-103"),
                                   ("Jul-2024", "confirmed", 15.0, 17.0, "A-104"), ("Oct-2024", "lower end", 15.0, 17.0, "A-105")], 13.6,
     "as first reported (A-107); restated 13.0% (A-013)"),
    ("FY2025", "net sales CHF m", [("Mar-2025", "initial", 480, 520, "A-108"), ("Apr-2025", "confirmed", 480, 520, "A-109"),
                                   ("Jul-2025", "lowered", 460, 500, "A-110"), ("Oct-2025", "lower end", 460, 500, "A-111")], 457.0, "A-010"),
    ("FY2025", "EBITDA margin %", [("Mar-2025", "initial", 17.0, 20.0, "A-108"), ("Apr-2025", "confirmed", 17.0, 20.0, "A-109"),
                                   ("Jul-2025", "lowered", 10.0, 14.0, "A-110"), ("Oct-2025", "lower end", 10.0, 14.0, "A-111")], 10.1, "A-013"),
]


def score(a, lo, hi):
    return "beat" if a > hi else ("miss" if a < lo else "in-line")


counts = {"initial": {}, "latest": {}}
print(f"{'FY':7s} {'metric':17s} {'initial':>14s} {'latest':>22s} {'actual':>7s}  vs-initial  vs-latest  late-maintained-then-missed")
for fy, m, g, act, note in REC:
    ini, last = g[0], g[-1]
    si, sl = score(act, ini[2], ini[3]), score(act, last[2], last[3])
    # 'maintained late then missed': a confirmation/narrowing given in H2 (Jul or later) without
    # lowering below the eventual result's bracket, followed by a miss vs that guidance
    late = [x for x in g if x[0][:3] in ("Jul", "Aug", "Oct") and x[1] in ("confirmed", "narrowed", "lower end", "reiterated")]
    flag = "YES" if late and score(act, late[-1][2], late[-1][3]) == "miss" else ""
    if fy >= "FY2022":
        counts["initial"][si] = counts["initial"].get(si, 0) + 1
        counts["latest"][sl] = counts["latest"].get(sl, 0) + 1
    print(f"{fy:7s} {m:17s} {ini[2]:>6}-{ini[3]:<6} {last[0]} {last[2]:>6}-{last[3]:<6} {act:>7}  {si:10s} {sl:9s}  {flag}  [{note}]")

print("\nFY2022-FY2025 (8 items = 4 years x sales & EBITDA margin), reported basis:")
print("  vs initial numeric guidance:", counts["initial"])
print("  vs last guidance before results:", counts["latest"])
print("  FY2022 margin on company-adjusted basis (21.8%) would be in-line vs 21-23%.")
print("  FY2024 margin on restated basis (13.0%) is also a miss.")

# FY2026 open guidance: implied Q4 2026
nine_m = 395.5   # A-042
for lab, lo, hi in (("Jul-2026", 540, 570), ("Oct-2026", 570, 590)):
    print(f"FY2026 {lab} net sales {lo}-{hi}: implied H2 2026 {lo-239.8:.1f}-{hi-239.8:.1f}; implied Q4 2026 {lo-nine_m:.1f}-{hi-nine_m:.1f}"
          f" vs Q3 2026 155.6 and Q4 2025 127.4")
print(f"FY2026 Oct midpoint 580 vs FY2025 457.0: {100*(580/457.0-1):.1f}%")
