#!/usr/bin/env python3
"""A4 - revenue by region: shares, China share, YoY, sum checks.
Advantest, fiscal year ends 31 March. Slide figures = ship-to region ("the location of customers' facilities to
which products were shipped"), JPY billion, single quarters. Annual securities report = customer location, JPY million.
Inputs are hard-coded from research/out/advantest/parts/A4.csv (evidence id in each comment).
"""

# --- quarterly ship-to region, JPY billion, Q2 FY26 deck p.7 ---
Q = {
    'FY2024 Q3': {
        'Japan': 3.4,  # A4-075: Quarterly sales by region (Japan), ship-to basis, FY2024 Q3 (single quarter) (JPY billion)
        'S. Korea': 54.9,  # A4-076: Quarterly sales by region (S. Korea), ship-to basis, FY2024 Q3 (single quarter) (JPY billion)
        'Taiwan': 78.8,  # A4-077: Quarterly sales by region (Taiwan), ship-to basis, FY2024 Q3 (single quarter) (JPY billion)
        'China': 51.8,  # A4-078: Quarterly sales by region (China), ship-to basis, FY2024 Q3 (single quarter) (JPY billion)
        'Americas': 12.6,  # A4-079: Quarterly sales by region (Americas), ship-to basis, FY2024 Q3 (single quarter) (JPY billion)
        'Europe': 5.0,  # A4-080: Quarterly sales by region (Europe), ship-to basis, FY2024 Q3 (single quarter) (JPY billion)
        'Others': 11.7,  # A4-081: Quarterly sales by region (Others), ship-to basis, FY2024 Q3 (single quarter) (JPY billion)
        'Total': 218.2,  # A4-082: Quarterly sales by region (Total), ship-to basis, FY2024 Q3 (single quarter) (JPY billion)
    },
    'FY2024 Q4': {
        'Japan': 2.5,  # A4-083: Quarterly sales by region (Japan), ship-to basis, FY2024 Q4 (single quarter) (JPY billion)
        'S. Korea': 23.7,  # A4-084: Quarterly sales by region (S. Korea), ship-to basis, FY2024 Q4 (single quarter) (JPY billion)
        'Taiwan': 133.1,  # A4-085: Quarterly sales by region (Taiwan), ship-to basis, FY2024 Q4 (single quarter) (JPY billion)
        'China': 44.6,  # A4-086: Quarterly sales by region (China), ship-to basis, FY2024 Q4 (single quarter) (JPY billion)
        'Americas': 13.0,  # A4-087: Quarterly sales by region (Americas), ship-to basis, FY2024 Q4 (single quarter) (JPY billion)
        'Europe': 5.7,  # A4-088: Quarterly sales by region (Europe), ship-to basis, FY2024 Q4 (single quarter) (JPY billion)
        'Others': 9.7,  # A4-089: Quarterly sales by region (Others), ship-to basis, FY2024 Q4 (single quarter) (JPY billion)
        'Total': 232.3,  # A4-090: Quarterly sales by region (Total), ship-to basis, FY2024 Q4 (single quarter) (JPY billion)
    },
    'FY2025 Q1': {
        'Japan': 3.8,  # A4-091: Quarterly sales by region (Japan), ship-to basis, FY2025 Q1 (single quarter) (JPY billion)
        'S. Korea': 32.7,  # A4-092: Quarterly sales by region (S. Korea), ship-to basis, FY2025 Q1 (single quarter) (JPY billion)
        'Taiwan': 162.1,  # A4-093: Quarterly sales by region (Taiwan), ship-to basis, FY2025 Q1 (single quarter) (JPY billion)
        'China': 39.0,  # A4-094: Quarterly sales by region (China), ship-to basis, FY2025 Q1 (single quarter) (JPY billion)
        'Americas': 9.6,  # A4-095: Quarterly sales by region (Americas), ship-to basis, FY2025 Q1 (single quarter) (JPY billion)
        'Europe': 4.4,  # A4-096: Quarterly sales by region (Europe), ship-to basis, FY2025 Q1 (single quarter) (JPY billion)
        'Others': 12.2,  # A4-097: Quarterly sales by region (Others), ship-to basis, FY2025 Q1 (single quarter) (JPY billion)
        'Total': 263.8,  # A4-098: Quarterly sales by region (Total), ship-to basis, FY2025 Q1 (single quarter) (JPY billion)
    },
    'FY2025 Q2': {
        'Japan': 5.2,  # A4-099: Quarterly sales by region (Japan), ship-to basis, FY2025 Q2 (single quarter) (JPY billion)
        'S. Korea': 56.1,  # A4-100: Quarterly sales by region (S. Korea), ship-to basis, FY2025 Q2 (single quarter) (JPY billion)
        'Taiwan': 115.4,  # A4-101: Quarterly sales by region (Taiwan), ship-to basis, FY2025 Q2 (single quarter) (JPY billion)
        'China': 52.1,  # A4-102: Quarterly sales by region (China), ship-to basis, FY2025 Q2 (single quarter) (JPY billion)
        'Americas': 11.3,  # A4-103: Quarterly sales by region (Americas), ship-to basis, FY2025 Q2 (single quarter) (JPY billion)
        'Europe': 6.1,  # A4-104: Quarterly sales by region (Europe), ship-to basis, FY2025 Q2 (single quarter) (JPY billion)
        'Others': 16.7,  # A4-105: Quarterly sales by region (Others), ship-to basis, FY2025 Q2 (single quarter) (JPY billion)
        'Total': 262.9,  # A4-106: Quarterly sales by region (Total), ship-to basis, FY2025 Q2 (single quarter) (JPY billion)
    },
    'FY2025 Q3': {
        'Japan': 8.5,  # A4-107: Quarterly sales by region (Japan), ship-to basis, FY2025 Q3 (single quarter) (JPY billion)
        'S. Korea': 57.0,  # A4-108: Quarterly sales by region (S. Korea), ship-to basis, FY2025 Q3 (single quarter) (JPY billion)
        'Taiwan': 103.2,  # A4-109: Quarterly sales by region (Taiwan), ship-to basis, FY2025 Q3 (single quarter) (JPY billion)
        'China': 65.4,  # A4-110: Quarterly sales by region (China), ship-to basis, FY2025 Q3 (single quarter) (JPY billion)
        'Americas': 12.0,  # A4-111: Quarterly sales by region (Americas), ship-to basis, FY2025 Q3 (single quarter) (JPY billion)
        'Europe': 5.9,  # A4-112: Quarterly sales by region (Europe), ship-to basis, FY2025 Q3 (single quarter) (JPY billion)
        'Others': 21.8,  # A4-113: Quarterly sales by region (Others), ship-to basis, FY2025 Q3 (single quarter) (JPY billion)
        'Total': 273.8,  # A4-114: Quarterly sales by region (Total), ship-to basis, FY2025 Q3 (single quarter) (JPY billion)
    },
    'FY2025 Q4': {
        'Japan': 7.6,  # A4-115: Quarterly sales by region (Japan), ship-to basis, FY2025 Q4 (single quarter) (JPY billion)
        'S. Korea': 34.5,  # A4-116: Quarterly sales by region (S. Korea), ship-to basis, FY2025 Q4 (single quarter) (JPY billion)
        'Taiwan': 188.8,  # A4-117: Quarterly sales by region (Taiwan), ship-to basis, FY2025 Q4 (single quarter) (JPY billion)
        'China': 56.8,  # A4-118: Quarterly sales by region (China), ship-to basis, FY2025 Q4 (single quarter) (JPY billion)
        'Americas': 11.6,  # A4-119: Quarterly sales by region (Americas), ship-to basis, FY2025 Q4 (single quarter) (JPY billion)
        'Europe': 6.7,  # A4-120: Quarterly sales by region (Europe), ship-to basis, FY2025 Q4 (single quarter) (JPY billion)
        'Others': 22.1,  # A4-121: Quarterly sales by region (Others), ship-to basis, FY2025 Q4 (single quarter) (JPY billion)
        'Total': 328.1,  # A4-122: Quarterly sales by region (Total), ship-to basis, FY2025 Q4 (single quarter) (JPY billion)
    },
    'FY2026 Q1': {
        'Japan': 3.3,  # A4-123: Quarterly sales by region (Japan), ship-to basis, FY2026 Q1 (single quarter) (JPY billion)
        'S. Korea': 67.4,  # A4-124: Quarterly sales by region (S. Korea), ship-to basis, FY2026 Q1 (single quarter) (JPY billion)
        'Taiwan': 178.6,  # A4-125: Quarterly sales by region (Taiwan), ship-to basis, FY2026 Q1 (single quarter) (JPY billion)
        'China': 69.4,  # A4-126: Quarterly sales by region (China), ship-to basis, FY2026 Q1 (single quarter) (JPY billion)
        'Americas': 13.2,  # A4-127: Quarterly sales by region (Americas), ship-to basis, FY2026 Q1 (single quarter) (JPY billion)
        'Europe': 6.1,  # A4-128: Quarterly sales by region (Europe), ship-to basis, FY2026 Q1 (single quarter) (JPY billion)
        'Others': 29.5,  # A4-129: Quarterly sales by region (Others), ship-to basis, FY2026 Q1 (single quarter) (JPY billion)
        'Total': 367.5,  # A4-130: Quarterly sales by region (Total), ship-to basis, FY2026 Q1 (single quarter) (JPY billion)
    },
    'FY2026 Q2': {
        'Japan': 1.8,  # A4-131: Quarterly sales by region (Japan), ship-to basis, FY2026 Q2 (single quarter) (JPY billion)
        'S. Korea': 64.6,  # A4-132: Quarterly sales by region (S. Korea), ship-to basis, FY2026 Q2 (single quarter) (JPY billion)
        'Taiwan': 261.3,  # A4-133: Quarterly sales by region (Taiwan), ship-to basis, FY2026 Q2 (single quarter) (JPY billion)
        'China': 90.1,  # A4-134: Quarterly sales by region (China), ship-to basis, FY2026 Q2 (single quarter) (JPY billion)
        'Americas': 15.7,  # A4-135: Quarterly sales by region (Americas), ship-to basis, FY2026 Q2 (single quarter) (JPY billion)
        'Europe': 6.1,  # A4-136: Quarterly sales by region (Europe), ship-to basis, FY2026 Q2 (single quarter) (JPY billion)
        'Others': 38.1,  # A4-137: Quarterly sales by region (Others), ship-to basis, FY2026 Q2 (single quarter) (JPY billion)
        'Total': 477.7,  # A4-138: Quarterly sales by region (Total), ship-to basis, FY2026 Q2 (single quarter) (JPY billion)
    },
}

# --- annual ship-to region, JPY billion, FY25 deck p.6 ---
ANN = {
    'FY2024': {
        'Japan': 15.8,  # A4-051: Sales by region (Japan), ship-to basis, FY2024 (annual chart) (JPY billion)
        'S. Korea': 157.0,  # A4-052: Sales by region (S. Korea), ship-to basis, FY2024 (annual chart) (JPY billion)
        'Taiwan': 326.5,  # A4-053: Sales by region (Taiwan), ship-to basis, FY2024 (annual chart) (JPY billion)
        'China': 175.1,  # A4-054: Sales by region (China), ship-to basis, FY2024 (annual chart) (JPY billion)
        'Americas': 47.1,  # A4-055: Sales by region (Americas), ship-to basis, FY2024 (annual chart) (JPY billion)
        'Europe': 20.0,  # A4-056: Sales by region (Europe), ship-to basis, FY2024 (annual chart) (JPY billion)
        'Others': 38.2,  # A4-057: Sales by region (Others), ship-to basis, FY2024 (annual chart) (JPY billion)
        'Total': 779.7,  # A4-058: Sales by region (Total), ship-to basis, FY2024 (annual chart) (JPY billion)
    },
    'FY2025': {
        'Japan': 25.1,  # A4-059: Sales by region (Japan), ship-to basis, FY2025 (annual chart) (JPY billion)
        'S. Korea': 180.3,  # A4-060: Sales by region (S. Korea), ship-to basis, FY2025 (annual chart) (JPY billion)
        'Taiwan': 569.5,  # A4-061: Sales by region (Taiwan), ship-to basis, FY2025 (annual chart) (JPY billion)
        'China': 213.3,  # A4-062: Sales by region (China), ship-to basis, FY2025 (annual chart) (JPY billion)
        'Americas': 44.5,  # A4-063: Sales by region (Americas), ship-to basis, FY2025 (annual chart) (JPY billion)
        'Europe': 23.1,  # A4-064: Sales by region (Europe), ship-to basis, FY2025 (annual chart) (JPY billion)
        'Others': 72.8,  # A4-065: Sales by region (Others), ship-to basis, FY2025 (annual chart) (JPY billion)
        'Total': 1128.6,  # A4-066: Sales by region (Total), ship-to basis, FY2025 (annual chart) (JPY billion)
    },
}

# --- annual customer-location region, JPY million, annual securities reports ---
ASR = {
    "FY2025": {"Japan": 25137, "Americas": 44474, "Europe": 23149, "Asia": 1035850,  # A4-015, A4-017, A4-019, A4-021
               "Taiwan": 569466, "China": 213293, "S. Korea": 180340, "Total": 1128610},  # A4-025, A4-027, A4-029, A4-023
    "FY2024": {"Japan": 15849, "Americas": 47119, "Europe": 19962, "Asia": 696777,  # A4-016, A4-018, A4-020, A4-022
               "Taiwan": 326506, "China": 175105, "S. Korea": 156994, "Total": 779707},  # A4-026, A4-028, A4-030, A4-024
    "FY2023": {"Japan": 19723, "Americas": 37621, "Europe": 17643, "Asia": 411520,  # A4-033, A4-035, A4-037, A4-039
               "Taiwan": 108357, "China": 157064, "S. Korea": 92891, "Total": 486507},  # A4-043, A4-045, A4-047, A4-041
}
ASIA_PCT_FY24_STATED = 89.4  # A4-048: Share of FY2024 net sales shipped to Asia (excluding Japan), company-stated (%)
OVERSEAS_PCT_FY25_STATED = 97.8  # A4-049: Overseas sales as a percentage of total sales, FY2025 (FY2024: 98.0%) (%)
CHINA_PCT_STATED_JUL2026 = 19  # A4-312: Management (Jul 2026): China accounts for approximately 19% of total sales and has been around  (%)

# --- semi-annual, customer location, JPY million ---
SA = {
    "FY2026 1H": {"Japan": 5152, "Americas": 28869, "Europe": 12178, "Asia": 799001, "Total": 845200},  # A4-203, A4-204, A4-205, A4-206, A4-207
    "FY2025 1H": {"Japan": 8961, "Americas": 20874, "Europe": 10499, "Asia": 486399, "Total": 526733},  # A4-208, A4-210, A4-212, A4-214, A4-216
}

REGIONS7 = ["Japan", "S. Korea", "Taiwan", "China", "Americas", "Europe", "Others"]


def pct(a, b):
    return 100.0 * a / b


print("== Quarterly ship-to shares (single quarters) ==")
for q, d in Q.items():
    s = round(sum(d[r] for r in REGIONS7), 1)
    print(f"{q}: sum of 7 regions {s:.1f} vs printed total {d['Total']:.1f} -> diff {s - d['Total']:+.1f}")
    print("   " + ", ".join(f"{r} {pct(d[r], d['Total']):.1f}%" for r in REGIONS7))
    print(f"RESULT china_share_{q.replace(' ', '_')} = {pct(d['China'], d['Total']):.4f}")
    print(f"RESULT taiwan_share_{q.replace(' ', '_')} = {pct(d['Taiwan'], d['Total']):.4f}")
    print(f"RESULT korea_share_{q.replace(' ', '_')} = {pct(d['S. Korea'], d['Total']):.4f}")
    print(f"RESULT sumcheck_{q.replace(' ', '_')} = {s - d['Total']:.1f}")

print()
print("== YoY by region, last 4 quarters ==")
pairs = [("FY2025 Q3", "FY2024 Q3"), ("FY2025 Q4", "FY2024 Q4"), ("FY2026 Q1", "FY2025 Q1"), ("FY2026 Q2", "FY2025 Q2")]
for cur, prev in pairs:
    print(cur, ", ".join(f"{r} {pct(Q[cur][r] - Q[prev][r], Q[prev][r]):+.1f}%" for r in REGIONS7 + ["Total"]))
    print(f"RESULT china_yoy_{cur.replace(' ', '_')} = {pct(Q[cur]['China'] - Q[prev]['China'], Q[prev]['China']):.4f}")

print()
print("== Last-4-quarter (Oct 2025-Sep 2026) totals ==")
l4 = ["FY2025 Q3", "FY2025 Q4", "FY2026 Q1", "FY2026 Q2"]
p4 = ["FY2024 Q3", "FY2024 Q4", "FY2025 Q1", "FY2025 Q2"]
for r in REGIONS7 + ["Total"]:
    a = sum(Q[q][r] for q in l4); b = sum(Q[q][r] for q in p4)
    print(f"{r}: last4 {a:.1f} (share {pct(a, sum(Q[q]['Total'] for q in l4)):.1f}%), prior4 {b:.1f}, change {pct(a - b, b):+.1f}%")
l4c = sum(Q[q]["China"] for q in l4); l4t = sum(Q[q]["Total"] for q in l4)
print(f"RESULT china_share_last4q = {pct(l4c, l4t):.4f}")
print(f"RESULT china_last4q_JPYbn = {l4c:.1f}")
print(f"RESULT total_last4q_JPYbn = {l4t:.1f}")
p4c = sum(Q[q]["China"] for q in p4); p4t = sum(Q[q]["Total"] for q in p4)
print(f"RESULT china_prior4q_JPYbn = {p4c:.1f}")  # Oct 2024-Sep 2025
print(f"RESULT china_yoy_last4q = {pct(l4c - p4c, p4c):.4f}")  # Oct 2025-Sep 2026 vs Oct 2024-Sep 2025
print(f"RESULT china_share_prior4q = {pct(p4c, p4t):.4f}")

print()
print("== Annual ship-to (slides) vs sum of quarters ==")
fy25q = ["FY2025 Q1", "FY2025 Q2", "FY2025 Q3", "FY2025 Q4"]
for r in REGIONS7 + ["Total"]:
    sq = sum(Q[q][r] for q in fy25q)
    print(f"FY2025 {r}: sum of quarters {sq:.1f} vs annual chart {ANN['FY2025'][r]:.1f} -> diff {sq - ANN['FY2025'][r]:+.1f}")
for fy in ("FY2024", "FY2025"):
    s = round(sum(ANN[fy][r] for r in REGIONS7), 1)
    print(f"{fy} annual: 7-region sum {s:.1f} vs total {ANN[fy]['Total']:.1f}")
    print("   " + ", ".join(f"{r} {pct(ANN[fy][r], ANN[fy]['Total']):.1f}%" for r in REGIONS7))
    print(f"RESULT china_share_slide_{fy} = {pct(ANN[fy]['China'], ANN[fy]['Total']):.4f}")

print()
print("== Annual customer location (annual securities reports) ==")
for fy, d in ASR.items():
    other_asia = d["Asia"] - d["Taiwan"] - d["China"] - d["S. Korea"]
    s4 = d["Japan"] + d["Americas"] + d["Europe"] + d["Asia"]
    print(f"{fy}: 4-region sum {s4:,} vs total {d['Total']:,} (diff {s4 - d['Total']})")
    print("   " + ", ".join(f"{r} {pct(d[r], d['Total']):.1f}%" for r in ["Japan", "Americas", "Europe", "Asia", "Taiwan", "China", "S. Korea"])
          + f", other Asia (derived) {other_asia:,} = {pct(other_asia, d['Total']):.1f}%")
    print(f"RESULT china_share_asr_{fy} = {pct(d['China'], d['Total']):.4f}")
    print(f"RESULT taiwan_share_asr_{fy} = {pct(d['Taiwan'], d['Total']):.4f}")
    print(f"RESULT korea_share_asr_{fy} = {pct(d['S. Korea'], d['Total']):.4f}")
    print(f"RESULT other_asia_asr_{fy}_JPYm = {other_asia}")
    print(f"RESULT overseas_share_asr_{fy} = {pct(d['Total'] - d['Japan'], d['Total']):.4f}")
print(f"RESULT china_yoy_asr_FY2025 = {pct(ASR['FY2025']['China'] - ASR['FY2024']['China'], ASR['FY2024']['China']):.4f}")
print(f"RESULT china_yoy_asr_FY2024 = {pct(ASR['FY2024']['China'] - ASR['FY2023']['China'], ASR['FY2023']['China']):.4f}")
print(f"RESULT asia_share_asr_FY2024 = {pct(ASR['FY2024']['Asia'], ASR['FY2024']['Total']):.4f}  (company states {ASIA_PCT_FY24_STATED}%)")
print(f"overseas FY2025 computed {pct(ASR['FY2025']['Total'] - ASR['FY2025']['Japan'], ASR['FY2025']['Total']):.2f}% vs stated {OVERSEAS_PCT_FY25_STATED}%")

print()
print("== Ship-to (slides, JPY bn) vs customer location (ASR, JPY m) ==")
for fy in ("FY2024", "FY2025"):
    for r in ["Japan", "Americas", "Europe", "Taiwan", "China", "S. Korea"]:
        a = ASR[fy][r] / 1000.0; b = ANN[fy][r]
        print(f"{fy} {r}: ASR {a:.3f} bn vs slide {b:.1f} bn -> diff {a - b:+.3f}")
    oa = (ASR[fy]["Asia"] - ASR[fy]["Taiwan"] - ASR[fy]["China"] - ASR[fy]["S. Korea"]) / 1000.0
    print(f"{fy} other Asia (ASR derived) {oa:.3f} bn vs slide 'Other' {ANN[fy]['Others']:.1f} bn -> diff {oa - ANN[fy]['Others']:+.3f}")
    print(f"RESULT otherasia_vs_slideother_{fy}_JPYbn = {oa - ANN[fy]['Others']:.3f}")

print()
print("== Semi-annual (customer location) ==")
for h, d in SA.items():
    print(h, ", ".join(f"{r} {pct(d[r], d['Total']):.1f}%" for r in ["Japan", "Americas", "Europe", "Asia"]))
    print(f"RESULT asia_share_{h.replace(' ', '_')} = {pct(d['Asia'], d['Total']):.4f}")
print(f"RESULT asia_yoy_FY2026_1H = {pct(SA['FY2026 1H']['Asia'] - SA['FY2025 1H']['Asia'], SA['FY2025 1H']['Asia']):.4f}")
print(f"China share stated by management Jul 2026: ~{CHINA_PCT_STATED_JUL2026}%")

print()
print("== Semi-annual 'main regions' (basis not stated in the semi-annual report) vs sum of two ship-to slide quarters ==")
HALVES = {"FY2026 1H": ["FY2026 Q1", "FY2026 Q2"], "FY2025 1H": ["FY2025 Q1", "FY2025 Q2"]}
maxdiff = 0.0
for h, qs in HALVES.items():
    sl = {r: sum(Q[q][r] for q in qs) for r in REGIONS7 + ["Total"]}
    sl["Asia"] = sl["S. Korea"] + sl["Taiwan"] + sl["China"] + sl["Others"]
    for r in ["Japan", "Americas", "Europe", "Asia", "Total"]:
        d = SA[h][r] / 1000.0 - sl[r]
        maxdiff = max(maxdiff, abs(d))
        print(f"{h} {r}: semi-annual {SA[h][r] / 1000.0:.3f} bn vs slides {sl[r]:.1f} bn -> diff {d:+.3f}")
print(f"RESULT halfyear_vs_slides_max_abs_diff_JPYbn = {maxdiff:.3f}")
