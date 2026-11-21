#!/usr/bin/env python3
"""A6 verification pass - independent spot-check of calc/A6_quarterly_series.csv.
For 16 quarters (every peak and trough quarter used plus a mix of others) this script re-reads net sales and operating
income straight from page 1 of the saved results releases (text copies under research/sources/advantest/_text/, no
evidence rows involved), differences the cumulative figures itself, and compares with the series CSV. Where the company
printed a single quarter (quarterly overview page of a full-year release, or briefing slides), that is compared too.
Run: python3 -I research/out/advantest/calc/A6_verify_spotcheck.py > research/out/advantest/calc/A6_verify_spotcheck.out.txt
"""
import csv, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
TXT = os.path.join(HERE, "..", "..", "..", "sources", "advantest", "_text")


def page(stem, n):
    return open(os.path.join(TXT, stem + ".txt"), encoding="utf-8", errors="replace").read().split("\f")[n - 1]


def p1(stem, label):
    """first line on page 1 starting with label -> (net sales, operating income) in JPY million."""
    for line in page(stem, 1).split("\n"):
        if re.match(r"^\s*" + re.escape(label) + r"\s+[\d,]+\s", line):
            t = line.split()
            k = len(label.split())
            return int(t[k].replace(",", "")), int(t[k + 2].replace(",", "").replace("(", "-").replace(")", ""))
    raise SystemExit(f"{label} not found in {stem}")


def row_bn(stem, pg, name, col):
    """company-printed single quarter (JPY bn) from a quarterly table: col = position among the numbers on the line."""
    for line in page(stem, pg).split("\n"):
        if re.match(r"^\s*" + re.escape(name) + r"\s", line):
            nums = re.findall(r"\(?\d+\.\d\)?", line)
            return float(nums[col].strip("()")) * (-1 if nums[col].startswith("(") else 1)
    raise SystemExit(f"{name} not found in {stem} p.{pg}")


# (quarter, current cumulative (stem, label), previous cumulative or None, printed single quarter or None)
R = "advantest_financial-results-"
CHECKS = [
    ("FY2015 Q2", ("2016-10-26_" + R + "FY2016Q2", "FY2015 Q2"), ("2016-07-27_" + R + "FY2016Q1", "FY2015 Q1"), None),
    ("FY2015 Q3", ("2017-01-26_" + R + "FY2016Q3", "FY2015 Q3"), ("2016-10-26_" + R + "FY2016Q2", "FY2015 Q2"), None),
    ("FY2016 Q3", ("2017-01-26_" + R + "FY2016Q3", "FY2016 Q3"), ("2016-10-26_" + R + "FY2016Q2", "FY2016 Q2"), None),
    ("FY2017 Q1", ("2018-07-25_" + R + "FY2018Q1", "FY2017 Q1"), None, ("2018-04-26_" + R + "FY2017Q4-full-year", 19, 1)),
    ("FY2018 Q3", ("2019-01-30_" + R + "FY2018Q3", "FY2018 Q3"), ("2018-10-30_" + R + "FY2018Q2", "FY2018 Q2"), ("2019-04-25_" + R + "FY2018Q4-full-year", 18, 3)),
    ("FY2018 Q4", ("2019-04-25_" + R + "FY2018Q4-full-year", "FY2018"), ("2019-01-30_" + R + "FY2018Q3", "FY2018 Q3"), ("2019-04-25_" + R + "FY2018Q4-full-year", 18, 4)),
    ("FY2019 Q3", ("2020-01-29_" + R + "FY2019Q3", "FY2019 Q3"), ("2019-10-30_" + R + "FY2019Q2", "FY2019 Q2"), ("2020-04-24_" + R + "FY2019Q4-full-year", 21, 3)),
    ("FY2019 Q4", ("2020-04-24_" + R + "FY2019Q4-full-year", "FY2019"), ("2020-01-29_" + R + "FY2019Q3", "FY2019 Q3"), ("2020-04-24_" + R + "FY2019Q4-full-year", 21, 4)),
    ("FY2020 Q2", ("2020-10-29_" + R + "FY2020Q2", "FY2020 Q2"), ("2020-07-30_" + R + "FY2020Q1", "FY2020 Q1"), ("2021-04-27_" + R + "FY2020Q4-full-year", 22, 2)),
    ("FY2022 Q1", ("2022-07-28_" + R + "FY2022Q1", "FY2022 Q1"), None, ("2023-04-26_" + R + "FY2022Q4-full-year", 21, 1)),
    ("FY2022 Q4", ("2023-04-26_" + R + "FY2022Q4-full-year", "FY2022"), ("2023-01-31_" + R + "FY2022Q3", "FY2022 Q3"), ("2023-04-26_" + R + "FY2022Q4-full-year", 21, 4)),
    ("FY2023 Q1", ("2023-07-26_" + R + "FY2023Q1", "FY2023 Q1"), None, ("2024-04-26_" + R + "FY2023Q4-full-year", 19, 1)),
    ("FY2023 Q4", ("2024-04-26_" + R + "FY2023Q4-full-year", "FY2023"), ("2024-01-31_" + R + "FY2023Q3", "FY2023 Q3"), ("2024-04-26_" + R + "FY2023Q4-full-year", 19, 4)),
    ("FY2024 Q2", ("2024-10-30_" + R + "FY2024Q2", "FY2024 Q2"), ("2024-07-31_" + R + "FY2024Q1", "FY2024 Q1"), ("2025-04-25_" + R + "FY2024Q4-full-year", 17, 2)),
    ("FY2025 Q4", ("2026-04-27_" + R + "FY2025Q4-full-year", "FY2025"), ("2026-01-28_" + R + "FY2025Q3", "FY2025 Q3"), ("2026-04-27_" + R + "FY2025Q4-full-year", 19, 4)),
    ("FY2026 Q2", ("2026-10-28_" + R + "FY2026Q2", "FY2026 Q2"), ("2026-07-29_" + R + "FY2026Q1", "FY2026 Q1"), None),
]
series = {r["fiscal_quarter"]: r for r in csv.DictReader(open(os.path.join(HERE, "A6_quarterly_series.csv"), encoding="utf-8"))}
bad = 0
for q, cur, prev, printed in CHECKS:
    s1, o1 = p1(*cur)
    s0, o0 = p1(*prev) if prev else (0, 0)
    s, o = s1 - s0, o1 - o0
    r = series[q]
    ok = (s == int(r["net_sales_jpy_m"]) and o == int(r["operating_income_jpy_m"]))
    msg = f"{q}: re-derived sales {s:,} OI {o:,} | series {int(r['net_sales_jpy_m']):,} / {int(r['operating_income_jpy_m']):,} -> {'MATCH' if ok else 'MISMATCH'}"
    if printed:
        ps = row_bn(printed[0], printed[1], "Net sales", printed[2])
        po = row_bn(printed[0], printed[1], "Operating income", printed[2])
        pok = abs(s / 1000 - ps) <= 0.1001 and abs(o / 1000 - po) <= 0.1001
        ok = ok and pok
        msg += f" | company-printed {ps} / {po} bn ({printed[0][:10]} p.{printed[1]}) -> {'MATCH' if pok else 'MISMATCH'}"
    bad += not ok
    print(msg)
print(f"\n{len(CHECKS)} quarters spot-checked; {bad} mismatches")
