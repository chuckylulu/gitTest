#!/usr/bin/env python3
"""IXM intersegment (internal) sales share and IXM end-market mix.

Inputs (kCHF) read from Comet segment notes (see research/out/comet/parts/IXM.csv rows):
  intersegment sales of IXM and IXM total net sales (external + intersegment).
  FY2020/FY2021: AR FY2021 note 04.1; FY2022: AR FY2022; FY2023: AR FY2023; FY2024 (restated) and FY2025: AR FY2025;
  H1 2025 (restated) and H1 2026: half-year report H1 2026 note 03.1.
Fiscal year = calendar year (ends 31 Dec).
"""

# period: (IXM external net sales, IXM intersegment sales), kCHF
data = {
    "FY2020 (Jan-Dec 2020)": (51268, 10218),
    "FY2021 (Jan-Dec 2021)": (69259, 9687),
    "FY2022 (Jan-Dec 2022)": (75026, 13616),
    "FY2023 (Jan-Dec 2023)": (87472, 12787),
    "FY2024 (Jan-Dec 2024) restated": (82135, 12436),
    "FY2025 (Jan-Dec 2025)": (89137, 9941),
    "H1 2025 (Jan-Jun 2025) restated": (44211, 4191),
    "H1 2026 (Jan-Jun 2026)": (47530, 6008),
}

print("Period | IXM external | IXM intersegment | IXM total | intersegment share of IXM total")
for p, (ext, inter) in data.items():
    tot = ext + inter
    print(f"{p} | {ext:,} | {inter:,} | {tot:,} | {inter / tot * 100:.1f}%")

# FY2025 IXM external sales by market (AR FY2025 note 03, kCHF): FY2025, FY2024
mkt = {"Non-destructive testing": (60341, 56308), "Security": (15410, 11673), "Others": (13386, 14154)}
t25 = sum(v[0] for v in mkt.values())
t24 = sum(v[1] for v in mkt.values())
print(f"\nIXM external sales by market, FY2025 total {t25:,} kCHF (reported 89,137); FY2024 total {t24:,} (reported 82,135)")
for k, (a, b) in mkt.items():
    print(f"{k}: FY2025 {a / t25 * 100:.1f}% of IXM external; FY2024 {b / t24 * 100:.1f}%; YoY {(a / b - 1) * 100:+.1f}%")
