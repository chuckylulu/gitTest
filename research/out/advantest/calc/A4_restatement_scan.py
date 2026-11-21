#!/usr/bin/env python3
"""A4 - restatement scan: every line item of selected statements, as first reported vs as the comparative
column in the next year's document. Reads the saved text copies (research/sources/advantest/_text/*.txt,
physical PDF pages split on form feeds); no figures are typed in by hand here.

Pairs compared (prior-period column of the later document vs current-period column of the earlier one):
  1. FY2024 results (2025-04-25) vs FY2025 results (2026-04-27): P&L FY2024 (p.11), balance sheet 31 Mar 2025 (pp.9-10),
     net sales by geographical area FY2024 (p.15)
  2. Annual Securities Report 83rd vs 84th: consolidated P&L FY2024 (p.116), balance sheet 31 Mar 2025 (p.115)
  3. Quarterly results: Q1 FY2024 (FY24Q1 p.11 vs FY25Q1 p.9), 1H FY2024 (FY24Q2 p.11 vs FY25Q2 p.11),
     9M FY2024 (FY24Q3 p.11 vs FY25Q3 p.11), Q1 FY2025 (FY25Q1 p.9 vs FY26Q1 p.9), 1H FY2025 (FY25Q2 p.11 vs FY26Q2 p.10)
  4. Briefing-slide quarterly summary tables (single quarters, JPY bn): every quarter shown in more than one deck
Run: python3 -I research/out/advantest/calc/A4_restatement_scan.py
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
TXT = os.path.normpath(os.path.join(HERE, "..", "..", "..", "sources", "advantest", "_text"))
NUM = r"\(?-?[\d,]+(?:\.\d+)?\)?|－|-"


def page(stem, n):
    return open(os.path.join(TXT, stem + ".txt"), encoding="utf-8").read().split("\f")[n - 1]


def two_col(stem, pages, col):
    """Lines 'label  num  num' -> {(label, occurrence): value in column col (0 or 1)}."""
    out, seen = {}, {}
    for n in pages:
        for line in page(stem, n).split("\n"):
            m = re.match(r"\s*(\S.*?\S)\s{2,}(" + NUM + r")\s{2,}(" + NUM + r")\s*$", line)
            if not m:
                continue
            lab = re.sub(r"[\s-]+", " ", m.group(1))  # hyphen/space-insensitive label
            if re.fullmatch(r"[\d\s,.()%－-]+", lab):
                continue
            k = seen.get(lab, 0); seen[lab] = k + 1
            out[(lab, k)] = (m.group(2), m.group(3))[col]
    return out


def compare(title, a, b):
    same = diff = 0
    print(f"--- {title}")
    for k in a:
        if k in b:
            if a[k] == b[k]:
                same += 1
            else:
                diff += 1
                print(f"   CHANGED {k[0]} (#{k[1] + 1}): {a[k]} -> {b[k]}")
    only_a = [k[0] for k in a if k not in b]
    only_b = [k[0] for k in b if k not in a]
    print(f"   lines compared {same + diff}: same {same}, changed {diff}; only in first doc {len(only_a)}, only in later doc {len(only_b)}")
    if only_a or only_b:
        print(f"   (unmatched labels: first {only_a[:6]} later {only_b[:6]})")
    return same, diff


R = {}
FR24, FR25 = "2025-04-25_advantest_financial-results-FY2024Q4-full-year", "2026-04-27_advantest_financial-results-FY2025Q4-full-year"
ASR83, ASR84 = "2025-06-25_advantest_annual-securities-report-83rd-FY2024", "2026-06-26_advantest_annual-securities-report-84th-FY2025"
jobs = [
    ("FY2024 P&L: FY2024 results vs FY2025 results", (FR24, [11], 1), (FR25, [11], 0)),
    ("31 Mar 2025 balance sheet: FY2024 results vs FY2025 results", (FR24, [9, 10], 1), (FR25, [9, 10], 0)),
    ("FY2024 net sales by geographical area: FY2024 results vs FY2025 results", (FR24, [15], 1), (FR25, [15], 0)),
    ("FY2024 consolidated P&L: 83rd vs 84th annual securities report", (ASR83, [116], 1), (ASR84, [116], 0)),
    ("31 Mar 2025 balance sheet: 83rd vs 84th annual securities report", (ASR83, [115], 1), (ASR84, [115], 0)),
    ("Q1 FY2024 P&L: FY24 Q1 results vs FY25 Q1 results", ("2024-07-31_advantest_financial-results-FY2024Q1", [11], 1), ("2025-07-29_advantest_financial-results-FY2025Q1", [9], 0)),
    ("1H FY2024 P&L: FY24 Q2 results vs FY25 Q2 results", ("2024-10-30_advantest_financial-results-FY2024Q2", [11], 1), ("2025-10-28_advantest_financial-results-FY2025Q2", [11], 0)),
    ("9M FY2024 P&L: FY24 Q3 results vs FY25 Q3 results", ("2025-01-29_advantest_financial-results-FY2024Q3", [11], 1), ("2026-01-28_advantest_financial-results-FY2025Q3", [11], 0)),
    ("Q1 FY2025 P&L: FY25 Q1 results vs FY26 Q1 results", ("2025-07-29_advantest_financial-results-FY2025Q1", [9], 1), ("2026-07-29_advantest_financial-results-FY2026Q1", [9], 0)),
    ("1H FY2025 P&L: FY25 Q2 results vs FY26 Q2 results", ("2025-10-28_advantest_financial-results-FY2025Q2", [11], 1), ("2026-10-28_advantest_financial-results-FY2026Q2", [10], 0)),
]
tot_same = tot_diff = 0
print("== Statement line items: first reported vs later comparative ==")
for title, (s1, p1, c1), (s2, p2, c2) in jobs:
    s, d = compare(title, two_col(s1, p1, c1), two_col(s2, p2, c2))
    tot_same += s; tot_diff += d

# ---- briefing-slide quarterly summary tables ----
ROWS = ["Sales", "Gross Profit", "Operating Income", "Income Before Tax", "Net Income"]
Q = lambda fy, qs: [f"FY{fy} Q{i}" for i in qs]
DECKS = [
    ("FY24 3Q deck", "2025-01-29_advantest_earnings-briefing-slides-FY2024Q3", 5, Q(2023, [1, 2, 3, 4]) + Q(2024, [1, 2, 3])),
    ("FY24 deck", "2025-04-25_advantest_earnings-briefing-slides-FY2024Q4", 6, Q(2023, [1, 2, 3, 4]) + Q(2024, [1, 2, 3, 4])),
    ("Q3 FY25 deck", "2026-01-28_advantest_earnings-briefing-slides-FY2025Q3", 5, Q(2024, [1, 2, 3, 4]) + Q(2025, [1, 2, 3])),
    ("FY25 deck", "2026-04-27_advantest_earnings-briefing-slides-FY2025Q4", 7, Q(2024, [1, 2, 3, 4]) + Q(2025, [1, 2, 3, 4])),
    ("Q1 FY26 deck", "2026-07-29_advantest_earnings-briefing-slides-FY2026Q1", 5, Q(2025, [1, 2, 3, 4]) + Q(2026, [1])),
    ("Q2 FY26 deck", "2026-10-28_advantest_earnings-briefing-slides-FY2026Q2", 5, Q(2025, [1, 2, 3, 4]) + Q(2026, [1]) + ["FY2026 Q2 forecast", "FY2026 Q2"]),
]
data = {}
for name, stem, pg, cols in DECKS:
    for line in page(stem, pg).split("\n"):
        for row in ROWS:
            if re.match(r"\s*" + row + r"(\s|/)", line) and "Margin" not in line:
                toks = [t for t in line.split() if re.fullmatch(r"[\d.]+|-", t)]
                for c, v in zip(cols, toks):
                    if v != "-":
                        data.setdefault((c, row), []).append((name, float(v)))
print()
print("== Briefing slides: single-quarter summary figures shown in more than one deck (JPY bn) ==")
s_same = s_diff = 0
for (c, row), lst in sorted(data.items()):
    if len(lst) < 2 or "forecast" in c:
        continue
    vals = {v for _, v in lst}
    if len(vals) == 1:
        s_same += 1
    else:
        s_diff += 1
        print(f"   CHANGED {c} {row}: " + "; ".join(f"{n} {v}" for n, v in lst))
print(f"   quarter-items shown in >=2 decks: {s_same + s_diff}; identical in all decks {s_same}; changed {s_diff}")
print()
print(f"RESULT statement_lines_compared = {tot_same + tot_diff}")
print(f"RESULT statement_lines_changed = {tot_diff}")
print(f"RESULT slide_quarter_items_compared = {s_same + s_diff}")
print(f"RESULT slide_quarter_items_changed = {s_diff}")
