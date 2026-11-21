#!/usr/bin/env python3
"""DV module: Comet divisional results by half-year, H1 2022 - H1 2026.

FY = calendar year. All inputs in CHF thousand, copied from the segment notes
(note 03.1 of half-year reports, note 04.1 of annual reports); evidence row ids in comments.
H2 = FY - H1 (computed here). Restatement: FY2024 was restated in the FY2025 annual report
(note 02.3) and H1 2025 was restated in the H1 2026 report (note 01.1); only PCT segment
operating income/EBITDA changed. H1 2024 was not restated. Both versions are shown.

Prints: per period and division: total net sales, external net sales, segment operating
income (EBIT), EBITDA, EBITDA margin (on total division net sales, as Comet computes it),
EBIT margin; PCT share of group EBITDA; one-off adjusted figures where management gave
an amount.
"""

# keys: ext, tot, ebit, ebitda ; group/elim/corp lines
D = {
    # H1 2022 (Jan-Jun 2022) - DV-001..004 (HY22 note 03.1)
    "H1 2022": dict(PCT=(173470, 173470, 29328, 34289), IXS=(59716, 59990, -4185, -1585),
                    IXM=(34312, 40985, 3738, 6149), ELIM=(0, -6947, -457, -457), CORP=(0, 0, -715, -715),
                    GRP=(267498, 267498, 27709, 37681)),
    # FY2022 (Jan-Dec 2022) - DV-005..008 (AR FY2022 note 04.1)
    "FY 2022": dict(PCT=(381424, 381424, 94497, 104915), IXS=(129944, 130351, -3104, 1607),
                    IXM=(75026, 88643, 10868, 15677), ELIM=(0, -14023, -1227, -1227), CORP=(0, 0, -2059, -2059),
                    GRP=(586395, 586395, 98975, 118913)),
    # H1 2023 - DV-009..012
    "H1 2023": dict(PCT=(106791, 106791, 344, 5696), IXS=(56784, 56796, -1957, 151),
                    IXM=(43450, 50830, 8272, 10375), ELIM=(0, -7392, -229, -229), CORP=(0, 0, -1720, -1720),
                    GRP=(207025, 207025, 4711, 14275)),
    # FY2023 - DV-013..016
    "FY 2023": dict(PCT=(193155, 193155, 7192, 18719), IXS=(116826, 116961, 671, 4923),
                    IXM=(87472, 100258, 19580, 23819), ELIM=(0, -12921, 761, 761), CORP=(0, 0, -3226, -3226),
                    GRP=(397453, 397453, 24978, 44996)),
    # H1 2024 - DV-017..020
    "H1 2024": dict(PCT=(94257, 94257, 3298, 9111), IXS=(55138, 55173, -4082, -1933),
                    IXM=(39920, 46472, 4971, 7298), ELIM=(0, -6587, -152, -152), CORP=(0, 0, -1344, -1344),
                    GRP=(189315, 189315, 2692, 12980)),
    # FY2024 as originally reported (AR FY2024) - DV-021..024
    "FY 2024 orig": dict(PCT=(247391, 247391, 40225, 52734), IXS=(115836, 115888, -8854, -4306),
                         IXM=(82135, 94571, 9474, 14567), ELIM=(0, -12488, -138, -138), CORP=(0, 0, -2478, -2478),
                         GRP=(445362, 445362, 38229, 60380)),
    # FY2024 restated (AR FY2025 comparative) - DV-025..026 (only PCT/group EBIT & EBITDA differ)
    "FY 2024 restated": dict(PCT=(247391, 247391, 37856, 50365), IXS=(115836, 115888, -8854, -4306),
                             IXM=(82135, 94571, 9474, 14567), ELIM=(0, -12488, -138, -138), CORP=(0, 0, -2478, -2478),
                             GRP=(445362, 445362, 35861, 58011)),
    # H1 2025 as originally reported (HY25) - DV-027..030
    "H1 2025 orig": dict(PCT=(134262, 134262, 14955, 21151), IXS=(48681, 48689, -9628, -7520),
                         IXM=(44211, 48402, 5893, 8322), ELIM=(0, -4199, -80, -80), CORP=(0, 0, -1165, -1165),
                         GRP=(227154, 227154, 9975, 20708)),
    # H1 2025 restated (HY26 comparative) - DV-031..032
    "H1 2025 restated": dict(PCT=(134262, 134262, 17225, 23421), IXS=(48681, 48689, -9628, -7520),
                             IXM=(44211, 48402, 5893, 8322), ELIM=(0, -4199, -80, -80), CORP=(0, 0, -1165, -1165),
                             GRP=(227154, 227154, 12245, 22978)),
    # FY2025 (AR FY2025; already on corrected basis) - DV-033..036
    "FY 2025": dict(PCT=(257102, 257102, 27807, 40407), IXS=(110804, 110816, -11646, -7516),
                    IXM=(89137, 99078, 10722, 15771), ELIM=(0, -9953, 263, 263), CORP=(0, 0, -2590, -2590),
                    GRP=(457044, 457044, 24556, 46335)),
    # H1 2026 - DV-037..040
    "H1 2026": dict(PCT=(143570, 143570, 22630, 28947), IXS=(48734, 48739, -5807, -3985),
                    IXM=(47530, 53539, 5793, 8630), ELIM=(0, -6014, -640, -640), CORP=(0, 0, -1585, -1585),
                    GRP=(239834, 239834, 20391, 31367)),
}

H2 = [  # (label, FY key, H1 key, note)
    ("H2 2022", "FY 2022", "H1 2022", ""),
    ("H2 2023", "FY 2023", "H1 2023", ""),
    ("H2 2024 orig", "FY 2024 orig", "H1 2024", "as first reported (AR FY2024)"),
    ("H2 2024 restated", "FY 2024 restated", "H1 2024", "FY2024 restated in AR FY2025; H1 2024 unchanged"),
    ("H2 2025 consistent", "FY 2025", "H1 2025 restated", "FY2025 and restated H1 2025 are on the same corrected basis"),
    ("H2 2025 mixed", "FY 2025", "H1 2025 orig", "mixes bases: FY2025 corrected minus H1 2025 as first reported "
                                                  "(this is how the FY2025 deck's 11.1% H2/25 margin arises)"),
]

UNITS = ["PCT", "IXS", "IXM", "ELIM", "CORP", "GRP"]


def sub(a, b):
    return tuple(x - y for x, y in zip(a, b))


for lab, fy, h1, _ in H2:
    D[lab] = {u: sub(D[fy][u], D[h1][u]) for u in UNITS}


def pct(n, d):
    return float("nan") if d == 0 else 100.0 * n / d


ORDER = ["H1 2022", "H2 2022", "H1 2023", "H2 2023", "H1 2024", "H2 2024 orig", "H2 2024 restated",
         "H1 2025 orig", "H1 2025 restated", "H2 2025 consistent", "H2 2025 mixed", "H1 2026",
         "FY 2022", "FY 2023", "FY 2024 orig", "FY 2024 restated", "FY 2025"]

print("Comet divisional results, CHF million (FY = calendar year). EBITDA margin on total division net sales.")
print(f"{'period':20s}{'div':5s}{'ext.sales':>10s}{'tot.sales':>10s}{'EBIT':>8s}{'EBIT%':>7s}{'EBITDA':>8s}{'EBITDA%':>8s}")
for p in ORDER:
    for u in ["PCT", "IXS", "IXM", "ELIM", "CORP", "GRP"]:
        ext, tot, ebit, ebitda = D[p][u]
        if u in ("ELIM", "CORP"):
            print(f"{p:20s}{u:5s}{'':>10s}{tot/1000:10.1f}{ebit/1000:8.1f}{'':>7s}{ebitda/1000:8.1f}")
            continue
        print(f"{p:20s}{u:5s}{ext/1000:10.1f}{tot/1000:10.1f}{ebit/1000:8.1f}{pct(ebit, tot):7.1f}"
              f"{ebitda/1000:8.1f}{pct(ebitda, tot):8.1f}")
    # check: segments + elim + corp == group
    s = [sum(D[p][u][i] for u in ["PCT", "IXS", "IXM", "ELIM", "CORP"]) for i in (1, 2, 3)]
    g = D[p]["GRP"][1:]
    flag = "" if all(abs(a - b) <= 2 for a, b in zip(s, g)) else "  <-- SUM MISMATCH"
    print(f"{'':20s}check sum tot/EBIT/EBITDA vs group: {s} vs {list(g)}{flag}")
print()
for lab, fy, h1, note in H2:
    if note:
        print(f"note {lab}: {note}")

print("\nPCT share of EBITDA (H = half-year)")
print(f"{'period':20s}{'PCT/group EBITDA %':>20s}{'PCT/sum of 3 segments %':>25s}{'PCT share ext sales %':>22s}")
for p in ORDER:
    pc, ix, im, g = D[p]["PCT"][3], D[p]["IXS"][3], D[p]["IXM"][3], D[p]["GRP"][3]
    print(f"{p:20s}{pct(pc, g):20.1f}{pct(pc, pc + ix + im):25.1f}{pct(D[p]['PCT'][0], D[p]['GRP'][0]):22.1f}")

print("\nIXS: D&A (EBITDA - EBIT) and EBIT, CHF m")
for p in ORDER:
    e = D[p]["IXS"]
    print(f"{p:20s} D&A {(e[3]-e[2])/1000:6.1f}  EBIT {e[2]/1000:7.1f}  EBIT% {pct(e[2], e[1]):6.1f}")

print("\nOne-off items named by management, with/without (CHF m)")
xp = 9000  # CHF 9.0m XP Power trial expense, H1 2022, PCT (DV-041, DV-042)
for p in ["H1 2022", "FY 2022"]:
    ext, tot, ebit, ebitda = D[p]["PCT"]
    g = D[p]["GRP"]
    print(f"{p}: PCT EBITDA reported {ebitda/1000:.1f} ({pct(ebitda, tot):.1f}%), ex XP trial {(ebitda+xp)/1000:.1f} "
          f"({pct(ebitda+xp, tot):.1f}%); group reported {g[3]/1000:.1f} ({pct(g[3], g[1]):.1f}%), "
          f"ex XP {(g[3]+xp)/1000:.1f} ({pct(g[3]+xp, g[1]):.1f}%)")
ext, tot, ebit, ebitda = D["H2 2022"]["PCT"]
print(f"H2 2022: PCT EBITDA {ebitda/1000:.1f} ({pct(ebitda, tot):.1f}%) - no XP trial cost (trial in Q1 2022)")
# Restatement 2024/H1 2025 (PCT only)
r24 = D["FY 2024 orig"]["PCT"][3] - D["FY 2024 restated"]["PCT"][3]
r25 = D["H1 2025 restated"]["PCT"][3] - D["H1 2025 orig"]["PCT"][3]
print(f"Restatement: FY2024 PCT EBITDA lowered by {r24/1000:.2f}; H1 2025 PCT EBITDA raised by {r25/1000:.2f}")
for p in ["H2 2024 orig", "H2 2024 restated", "H1 2025 orig", "H1 2025 restated", "H2 2025 consistent", "H2 2025 mixed"]:
    ext, tot, ebit, ebitda = D[p]["PCT"]
    g = D[p]["GRP"]
    print(f"  {p:20s} PCT EBITDA {ebitda/1000:6.1f} ({pct(ebitda, tot):5.1f}%)  group EBITDA {g[3]/1000:6.1f} ({pct(g[3], g[1]):5.1f}%)")
# FY2025 fire: insurance recovery ~2.1m in other operating income (segment not stated), Q4 2025 -> H2 2025
ins = 2100
g = D["H2 2025 consistent"]["GRP"]
gf = D["FY 2025"]["GRP"]
print(f"H2 2025 group EBITDA {g[3]/1000:.1f} ({pct(g[3], g[1]):.1f}%); ex ~2.1 fire insurance {(g[3]-ins)/1000:.1f} ({pct(g[3]-ins, g[1]):.1f}%)")
print(f"FY 2025 group EBITDA {gf[3]/1000:.1f} ({pct(gf[3], gf[1]):.1f}%); ex ~2.1 fire insurance {(gf[3]-ins)/1000:.1f} ({pct(gf[3]-ins, gf[1]):.1f}%)")
pf = D["FY 2025"]["PCT"]
print(f"  if insurance booked in PCT (not stated): FY2025 PCT EBITDA ex insurance {(pf[3]-ins)/1000:.1f} ({pct(pf[3]-ins, pf[1]):.1f}%)")
# H1 2026: CHF 4.5m one-time costs (Penang ramp-up + efficiency program), split by division not disclosed
oc = 4500
g = D["H1 2026"]["GRP"]
print(f"H1 2026 group EBITDA {g[3]/1000:.1f} ({pct(g[3], g[1]):.1f}%); ex 4.5 one-time costs {(g[3]+oc)/1000:.1f} ({pct(g[3]+oc, g[1]):.1f}%)")
# IXS: CA20 investment named at CMD 2025 for 2024 (CHF 10-15m) - not called a one-off, shown for scale
for inv in (10000, 15000):
    e = D["FY 2024 orig"]["IXS"]
    print(f"FY2024 IXS EBITDA {e[3]/1000:.1f} ({pct(e[3], e[1]):.1f}%); before CA20 investment of {inv/1000:.0f}: "
          f"{(e[3]+inv)/1000:.1f} ({pct(e[3]+inv, e[1]):.1f}%)")

print("\nPCT largest customer as % of PCT external sales (largest-customer sales from note 'Sales with key accounts',")
print("DV-119..123; PCT external sales from segment notes: FY2021 306,091k per AR FY2022 comparative p83, DV-005, DV-013, DV-021, DV-033)")
LC = {"FY2021": (156.0, 306.091, 30.4), "FY2022": (211.0, 381.424, 36.1), "FY2023": (71.0, 193.155, 17.7),
      "FY2024": (106.2, 247.391, 23.8), "FY2025": (104.4, 257.102, 22.8)}
for y, (c, p, g) in LC.items():
    print(f"{y}: largest customer CHF {c}m = {100*c/p:.1f}% of PCT sales ({g}% of group sales as reported)")
