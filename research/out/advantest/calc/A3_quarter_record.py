#!/usr/bin/env python3
"""A3 - Advantest quarter-level guidance record, last 8 quarters (FY2024 Q3 .. FY2026 Q2)
plus 5 earlier quarters for context (FY2023 Q2 .. FY2024 Q2).

Fiscal year ends 31 March; FY2025 = Apr 2025-Mar 2026.

What guidance exists (see A3.csv): Advantest's formal guidance is full-year only (tanshin).
Its briefing slides split the full-year forecast into periods:
  - at the Q1 release: a Q2 forecast column (and 2H);
  - at the Q2 release: a 2H forecast column (= full year - 1H actual, company method, A3-004);
  - at the Q3 release: a Q4 forecast column (= full year - 9M actual, company method, A3-005/A3-006);
  - at the Q4 (full-year) release: next fiscal year, full year only.
Method per slot (the guidance outstanding at the START of each quarter):
  Q2 slot -> Q2 forecast from the Q1 slides vs Q2 actual (direct, quarterly)
  Q3 slot -> 2H forecast from the Q2 slides vs 2H actual (Q3+Q4) (direct, half-year; no Q3-only figure exists)
  Q4 slot -> Q4 forecast from the Q3 slides vs Q4 actual (direct, quarterly)
  Q1 slot -> only the new full-year guidance exists; compared with how the year ended
             (FY actual vs initial FY guidance). FY2026 Q1 slot: year not ended -> provisional test.
Rule: diff% = (actual - guidance)/guidance*100; beat > +2%, in-line within +/-2%, miss < -2%.
Units: slide figures JPY billion (1 decimal); tanshin YTD figures JPY million (converted /1000).
Quarter/half actuals: slide-printed single-quarter values [F] where printed; otherwise tanshin YTD
differences (computed here, [I]). EPS by YTD subtraction is approximate (share count changes).
"""

BAND, BAND2 = 2.0, 5.0


def pct(a, g):
    return (a - g) / g * 100.0


def cls(d, band=BAND):
    return "beat" if d > band else ("miss" if d < -band else "in-line")


bn = lambda x: x / 1000.0

# ---- tanshin YTD / FY actuals (JPY million; EPS JPY) ----
FY23 = dict(s=486507, oi=81628, ni=62290)                              # A3-032, A3-033, A3-035
H1_23 = dict(s=217511, oi=35269, ni=25938)                             # A3-255, A3-256, A3-257
M9_23 = dict(s=350744, oi=62099, ni=47143)                             # A3-189, A3-190, A3-191
FY24 = dict(s=779707, oi=228161, ibt=224774, ni=161177, eps=218.67)    # A3-058..A3-062
H1_24 = dict(s=329206, oi=94859, ni=69343, eps=93.92)                  # A3-192..A3-195
M9_24 = dict(s=547358, oi=164126, ibt=163192, ni=121210, eps=164.21)   # A3-196..A3-200
FY25 = dict(s=1128610, oi=499120, ibt=516720, ni=375353, eps=515.15)   # A3-086..A3-090
Q1_25 = dict(s=263776, oi=123952, ni=90180, eps=123.14)                # A3-201..A3-204
H1_25 = dict(s=526733, oi=232435, ni=169813, eps=232.19)               # A3-205..A3-208
M9_25 = dict(s=800537, oi=346006, ni=248526, eps=340.60)               # A3-209..A3-212
Q1_26 = dict(s=367473, oi=189990, ni=174780, eps=241.27)               # A3-213..A3-216
H1_26 = dict(s=845200, oi=456809, ni=368083, eps=508.99)               # A3-217..A3-220

# ---- slide-printed single-quarter actuals (JPY billion; EPS JPY) ----
SQ = {
    "FY2023 Q2": dict(s=116.2, oi=21.0, ni=16.7),          # A3-154..A3-156
    "FY2023 Q4": dict(s=135.8, oi=19.5, ni=15.2),          # A3-157..A3-159
    "FY2024 Q2": dict(s=190.5, oi=63.6, ni=45.4),          # A3-160..A3-162
    "FY2024 Q3": dict(s=218.2, oi=69.2, ni=51.9),          # A3-163..A3-165
    "FY2024 Q4": dict(s=232.3, oi=64.1, ni=40.0),          # A3-166..A3-168
    "FY2025 Q1": dict(s=263.8, oi=124.0, ni=90.2),         # A3-169..A3-171
    "FY2025 Q2": dict(s=262.9, oi=108.4, ni=79.6, eps=109.03),  # A3-172..A3-174, A3-187
    "FY2025 Q3": dict(s=273.8, oi=113.6, ni=78.7),         # A3-175..A3-177
    "FY2025 Q4": dict(s=328.1, oi=153.1, ni=126.9),        # A3-178..A3-180
    "FY2026 Q1": dict(s=367.5, oi=190.0, ni=174.8),        # A3-181..A3-183
    "FY2026 Q2": dict(s=477.7, oi=266.8, ni=193.3, eps=267.75),  # A3-184..A3-186, A3-188
}

# ---- derived period actuals from tanshin (JPY billion) ----
def diff(a, b, keys):
    out = {}
    for k in keys:
        if k in a and k in b:
            out[k] = (a[k] - b[k]) if k == "eps" else bn(a[k] - b[k])
    return out

DER = {
    "FY2023 2H": diff(FY23, H1_23, ["s", "oi", "ni"]),
    "FY2023 Q4": diff(FY23, M9_23, ["s", "oi", "ni"]),
    "FY2024 2H": diff(FY24, H1_24, ["s", "oi", "ni", "eps"]),
    "FY2024 Q4": diff(FY24, M9_24, ["s", "oi", "ibt", "ni", "eps"]),
    "FY2025 Q2": diff(H1_25, Q1_25, ["s", "oi", "ni", "eps"]),
    "FY2025 2H": diff(FY25, H1_25, ["s", "oi", "ni", "eps"]),
    "FY2025 Q4": diff(FY25, M9_25, ["s", "oi", "ni", "eps"]),
    "FY2026 Q2": diff(H1_26, Q1_26, ["s", "oi", "ni", "eps"]),
}

# ---- guidance (JPY billion; EPS JPY) ----
G = {
    "FY2023 Q2": dict(s=112.7, oi=22.3, ni=16.8),                         # A3-113..A3-115 (2023-07-26)
    "FY2023 2H": dict(s=252.5, oi=44.7, ni=34.1),                         # A3-116..A3-118 (2023-10-31)
    "FY2023 Q4": dict(s=129.3, oi=22.9, ni=17.4),                         # A3-119..A3-121 (2024-01-31)
    "FY2024 FYinit": dict(s=525.0, oi=90.0, ni=67.0),                     # A3-040, A3-041, A3-043 (2024-04-26)
    "FY2024 Q2": dict(s=153.3, oi=35.7, ni=26.7),                         # A3-122..A3-124 (2024-07-31)
    "FY2024 2H": dict(s=310.8, oi=70.1, ni=52.7, eps=71.09),              # A3-125..A3-128 (2024-10-30)
    "FY2024 Q4": dict(s=192.6, oi=61.9, ibt=61.8, ni=46.3, eps=63.53),    # A3-129..A3-133 (2025-01-29)
    "FY2025 FYinit": dict(s=755.0, oi=242.0, ni=179.0, eps=243.96),       # A3-066, A3-067, A3-069, A3-070 (2025-04-25)
    "FY2025 Q2": dict(s=237.2, oi=96.3, ni=71.8, eps=98.15),              # A3-134..A3-137 (2025-07-29)
    "FY2025 2H": dict(s=423.3, oi=141.6, ni=105.2, eps=144.61),           # A3-138..A3-141 (2025-10-28)
    "FY2025 Q4": dict(s=269.5, oi=108.0, ni=80.0, eps=111.80),            # A3-142..A3-145 (2026-01-28)
    "FY2026 FYinit": dict(s=1420.0, oi=627.5, ni=465.5, eps=641.61),      # A3-094, A3-095, A3-097, A3-098 (2026-04-27)
    "FY2026 Q2": dict(s=434.5, oi=224.5, ni=163.2, eps=225.45),           # A3-146..A3-149 (2026-07-29)
    "FY2026 2H": dict(s=1017.8, oi=510.2, ni=373.4, eps=517.23),          # A3-150..A3-153 (2026-10-28, outstanding)
}

FYACT = {"FY2024": dict(s=bn(FY24["s"]), oi=bn(FY24["oi"]), ni=bn(FY24["ni"])),
         "FY2025": dict(s=bn(FY25["s"]), oi=bn(FY25["oi"]), ni=bn(FY25["ni"]), eps=FY25["eps"])}


def actual_for(period):
    """slide value if printed, else tanshin-derived value"""
    a = dict(DER.get(period, {}))
    a.update(SQ.get(period, {}))
    src = {k: ("slide" if k in SQ.get(period, {}) else "tanshin-derived") for k in a}
    return a, src


# slot: (quarter, calendar, guidance key, guidance date, actual period, method)
SLOTS = [
    # context (before the 8-quarter window)
    ("FY2023 Q2", "Jul-Sep 2023", "FY2023 Q2", "2023-07-26", "FY2023 Q2", "direct quarterly", "context"),
    ("FY2023 Q3", "Oct-Dec 2023", "FY2023 2H", "2023-10-31", "FY2023 2H", "2H forecast vs 2H actual", "context"),
    ("FY2023 Q4", "Jan-Mar 2024", "FY2023 Q4", "2024-01-31", "FY2023 Q4", "direct quarterly", "context"),
    ("FY2024 Q1", "Apr-Jun 2024", "FY2024 FYinit", "2024-04-26", "FY2024", "initial FY guidance vs FY actual", "context"),
    ("FY2024 Q2", "Jul-Sep 2024", "FY2024 Q2", "2024-07-31", "FY2024 Q2", "direct quarterly", "context"),
    # the 8-quarter window
    ("FY2024 Q3", "Oct-Dec 2024", "FY2024 2H", "2024-10-30", "FY2024 2H", "2H forecast vs 2H actual", "window"),
    ("FY2024 Q4", "Jan-Mar 2025", "FY2024 Q4", "2025-01-29", "FY2024 Q4", "direct quarterly", "window"),
    ("FY2025 Q1", "Apr-Jun 2025", "FY2025 FYinit", "2025-04-25", "FY2025", "initial FY guidance vs FY actual", "window"),
    ("FY2025 Q2", "Jul-Sep 2025", "FY2025 Q2", "2025-07-29", "FY2025 Q2", "direct quarterly", "window"),
    ("FY2025 Q3", "Oct-Dec 2025", "FY2025 2H", "2025-10-28", "FY2025 2H", "2H forecast vs 2H actual", "window"),
    ("FY2025 Q4", "Jan-Mar 2026", "FY2025 Q4", "2026-01-28", "FY2025 Q4", "direct quarterly", "window"),
    ("FY2026 Q1", "Apr-Jun 2026", "FY2026 FYinit", "2026-04-27", None, "initial FY guidance; FY2026 not ended -> provisional", "window"),
    ("FY2026 Q2", "Jul-Sep 2026", "FY2026 Q2", "2026-07-29", "FY2026 Q2", "direct quarterly", "window"),
]

METRICS = [("s", "Sales"), ("oi", "OI"), ("ni", "NI"), ("eps", "EPS")]
counts = {m: {"beat": 0, "in-line": 0, "miss": 0, "provisional beat": 0, "n/a": 0} for m, _ in METRICS}
counts5 = {m: {"beat": 0, "in-line": 0, "miss": 0} for m, _ in METRICS}

print("A3 quarter-level guidance record. Rule: beat > +2%, in-line within +/-2%, miss < -2% (sensitivity: +/-5%).")
print("Units: JPY billion; EPS JPY.\n")
for q, cal, gk, gdate, per, method, grp in SLOTS:
    g = G[gk]
    print(f"[{grp}] {q} ({cal}) | guidance used: {gk} of {gdate} | method: {method}")
    if per is None:
        # FY2026 Q1 slot - provisional
        for m, name in METRICS:
            if m not in g:
                continue
            h1 = bn(H1_26[m]) if m != "eps" else H1_26["eps"]
            g2h = G["FY2026 2H"][m]
            need = g[m] * (1 + BAND / 100) - h1     # 2H value at/below which FY would no longer be a beat
            print(f"    {name:5s} initial FY {g[m]:,.2f}; 1H actual {h1:,.2f} = {h1/g[m]*100:.1f}% of initial FY; "
                  f"FY ends 'beat' unless 2H <= {need:,.2f} ({pct(need, h1):+.1f}% vs 1H; {pct(need, g2h):+.1f}% vs current 2H guidance {g2h:,.2f})")
            counts[m]["provisional beat"] += 1
        print()
        continue
    if per in FYACT:
        a, src = FYACT[per], {k: "tanshin FY" for k in FYACT[per]}
    else:
        a, src = actual_for(per)
    for m, name in METRICS:
        if m in g and m in a:
            d = pct(a[m], g[m])
            print(f"    {name:5s} guidance {g[m]:>9,.2f} actual {a[m]:>9,.2f} ({src[m]:15s}) diff {d:+7.1f}% -> {cls(d):7s} [+/-5%: {cls(d, BAND2)}]")
            if grp == "window":
                counts[m][cls(d)] += 1
                counts5[m][cls(d, BAND2)] += 1
        elif grp == "window":
            counts[m]["n/a"] += 1
            print(f"    {name:5s} no guidance figure for this slot")
    if per == "FY2024 Q4":
        d = pct(DER[per]["ibt"], g["ibt"])
        print(f"    IBT   guidance {g['ibt']:>9,.2f} actual {DER[per]['ibt']:>9,.2f} (tanshin-derived) diff {d:+7.1f}% -> {cls(d)}")
    if method.startswith("2H") and q in SQ:
        print(f"    (Q3 alone: sales {SQ[q]['s']} = {SQ[q]['s']/g['s']*100:.1f}% of the 2H sales guidance; OI {SQ[q]['oi']} = {SQ[q]['oi']/g['oi']*100:.1f}% of 2H OI guidance)")
    print()

print("=" * 100)
print("COUNT over the 8-quarter window FY2024 Q3 .. FY2026 Q2 (one guidance event per quarter, as defined above)")
for m, name in METRICS:
    c = counts[m]
    print(f"  {name:5s} beats {c['beat']}, in-line {c['in-line']}, misses {c['miss']}, provisional beat {c['provisional beat']}, no guidance {c['n/a']}  (of 8)")
print("  Sensitivity with +/-5% band (determinable slots only):")
for m, name in METRICS:
    c = counts5[m]
    print(f"  {name:5s} beats {c['beat']}, in-line {c['in-line']}, misses {c['miss']}")

print()
print("=" * 100)
print("Cross-check: slide-printed single-quarter actuals vs tanshin YTD differences (JPY billion)")
for per in ["FY2023 Q4", "FY2024 Q4", "FY2025 Q2", "FY2025 Q4", "FY2026 Q2"]:
    for m in ["s", "oi", "ni"]:
        if m in SQ.get(per, {}) and m in DER.get(per, {}):
            print(f"  {per} {m:3s}: slide {SQ[per][m]:8.1f} | tanshin-derived {DER[per][m]:9.3f} | gap {SQ[per][m]-DER[per][m]:+.3f}")
for per in ["FY2025 Q2", "FY2026 Q2"]:
    print(f"  {per} eps: slide {SQ[per]['eps']:.2f} | YTD-difference {DER[per]['eps']:.2f}")
print("  Q3 single quarters (no derivation needed, slide values): FY2024 Q3 sales 218.2 (A3-163), FY2025 Q3 sales 273.8 (A3-175)")

print()
print("=" * 100)
print("Direction of the full-year guidance change announced at each window quarter's results (A3 rows of each version)")
REV = [
    ("FY2024 Q3 results (2025-01-29)", 640000, 740000, 165000, 226000),   # A3-048 -> A3-053; A3-049 -> A3-054
    ("FY2025 Q1 results (2025-07-29)", 755000, 835000, 242000, 300000),   # A3-066 -> A3-071; A3-067 -> A3-072
    ("FY2025 Q2 results (2025-10-28)", 835000, 950000, 300000, 374000),   # A3-071 -> A3-076; A3-072 -> A3-077
    ("FY2025 Q3 results (2026-01-28)", 950000, 1070000, 374000, 454000),  # A3-076 -> A3-081; A3-077 -> A3-082
    ("FY2026 Q1 results (2026-07-29)", 1420000, 1714000, 627500, 846000), # A3-094 -> A3-099; A3-095 -> A3-100
    ("FY2026 Q2 results (2026-10-28)", 1714000, 1863000, 846000, 967000), # A3-099 -> A3-104; A3-100 -> A3-105
]
raises = 0
for lab, s0, s1, o0, o1 in REV:
    up = s1 > s0 and o1 > o0
    raises += up
    print(f"  {lab}: sales {pct(s1, s0):+.1f}%, OI {pct(o1, o0):+.1f}% -> {'raised' if up else 'not raised'}")
print(f"  Raised at {raises} of {len(REV)} in-year releases in the window (Q4 releases set a new fiscal year's guidance and are not counted).")
print("  Context: FY2023 initial guidance was maintained at Q1 (2023-07-26, A3-022) and cut at Q2 (2023-10-31): sales -2.1%, OI -23.8% (A3_annual_record).")

print()
print("=" * 100)
print("One-off sensitivity for slots where management named an item with an amount (JPY billion).")
print("Guidance documents do not state whether these items were in the forecast. NI 'bounds' add/remove the full")
print("pre-tax amount (no tax effect assumed) - an arithmetic bound, not an estimate of the after-tax effect, which is not disclosed.")
IMP23 = 8.998    # A3-036 goodwill impairment, Q4 FY2023, in OI
IMP24 = 21.393   # A3-063 impairment, Q4 FY2024, in OI
CALL25 = 17.312  # A3-092 call-option fair-value gain, Q4 FY2025, financial income
VAL26_H1 = 54.171  # A3-260 (1H FY2026 valuation gains)
VAL26_Q1 = 41.075  # A3-228
VAL26_Q2 = VAL26_H1 - VAL26_Q1
x = SQ["FY2023 Q4"]["oi"] + IMP23
print(f"  FY2023 Q4 OI ex impairment {x:.1f} vs guidance {G['FY2023 Q4']['oi']}: {pct(x, G['FY2023 Q4']['oi']):+.1f}% ({cls(pct(x, G['FY2023 Q4']['oi']))}); reported {pct(SQ['FY2023 Q4']['oi'], G['FY2023 Q4']['oi']):+.1f}%")
x = SQ["FY2024 Q4"]["oi"] + IMP24
print(f"  FY2024 Q4 OI ex impairment {x:.1f} vs guidance {G['FY2024 Q4']['oi']}: {pct(x, G['FY2024 Q4']['oi']):+.1f}% ({cls(pct(x, G['FY2024 Q4']['oi']))}); OPM reported {SQ['FY2024 Q4']['oi']/SQ['FY2024 Q4']['s']*100:.1f}%, ex impairment {x/SQ['FY2024 Q4']['s']*100:.1f}%")
x = SQ["FY2024 Q4"]["ni"] + IMP24
print(f"  FY2024 Q4 NI upper bound if impairment carried no tax effect {x:.1f} vs guidance {G['FY2024 Q4']['ni']}: {pct(x, G['FY2024 Q4']['ni']):+.1f}% -> the NI miss classification depends on the undisclosed tax effect")
x = SQ["FY2025 Q4"]["ni"] - CALL25
print(f"  FY2025 Q4 NI less full pre-tax call-option gain {x:.1f} vs guidance {G['FY2025 Q4']['ni']}: {pct(x, G['FY2025 Q4']['ni']):+.1f}% ({cls(pct(x, G['FY2025 Q4']['ni']))}) - beat holds")
x = SQ["FY2026 Q2"]["ni"] - VAL26_Q2
print(f"  FY2026 Q2 valuation gains = {VAL26_H1} - {VAL26_Q1} = {VAL26_Q2:.3f}; NI less full pre-tax gains {x:.1f} vs guidance {G['FY2026 Q2']['ni']}: {pct(x, G['FY2026 Q2']['ni']):+.1f}% ({cls(pct(x, G['FY2026 Q2']['ni']))}) - beat holds")
print("  FY2025 Q2 OI: management named a one-time SG&A charge (A3-093) without an amount -> cannot adjust; reported OI beat +12.6% stands.")
print("  FY2026 Q2 OI: management named a one-time inventory write-down reversal benefit in 1H (A3-229) without an amount -> cannot adjust.")
