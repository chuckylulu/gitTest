"""Quarterly RPO (10-Q/10-K 'Remaining Performance Obligations') and the dollar range due within 12 months.
Inputs are read from the saved filing texts (no hard-coded values). Run: python3 -I research/out/kla/calc/a2_rpo_series.py"""
import os, re
T = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "sources", "kla", "_text")
F = [("Q1 FY24", "Sep 30, 2023", "2023-10-26_kla_10-Q-Q1FY24"), ("Q2 FY24", "Dec 31, 2023", "2024-01-26_kla_10-Q-Q2FY24"),
     ("Q3 FY24", "Mar 31, 2024", "2024-04-26_kla_10-Q-Q3FY24"), ("Q4 FY24", "Jun 30, 2024", "2024-08-05_kla_10-K-FY24"),
     ("Q1 FY25", "Sep 30, 2024", "2024-10-31_kla_10-Q-Q1FY25"), ("Q2 FY25", "Dec 31, 2024", "2025-01-31_kla_10-Q-Q2FY25"),
     ("Q3 FY25", "Mar 31, 2025", "2025-05-01_kla_10-Q-Q3FY25"), ("Q4 FY25", "Jun 30, 2025", "2025-08-07_kla_10-K-FY25"),
     ("Q1 FY26", "Sep 30, 2025", "2025-10-30_kla_10-Q-Q1FY26"), ("Q2 FY26", "Dec 31, 2025", "2026-01-30_kla_10-Q-Q2FY26"),
     ("Q3 FY26", "Mar 31, 2026", "2026-04-30_kla_10-Q-Q3FY26"), ("Q4 FY26", "Jun 30, 2026", "2026-08-06_kla_10-K-FY26"),
     ("Q1 FY27", "Sep 30, 2026", "2026-10-29_kla_10-Q-Q1FY27")]
print("quarter | date | RPO $B | within 12m % | within 12m $B")
for q, d, stem in F:
    t = re.sub(r"\s+", " ", open(os.path.join(T, stem + ".txt"), encoding="utf-8").read())
    i = t.find("Remaining Performance Obligations As of")
    if i < 0:
        print(f"{q} | {d} | no RPO paragraph (NOT DISCLOSED) | - | -"); continue
    s = t[i:i + 900]
    rpo = float(re.search(r"\$ ([\d.]+) billion of remaining performance", s).group(1))
    m = re.search(r"approximately ([\d]+) % to ([\d]+) % of these performance obligations as revenue (beyond|in) the next 12 months", s)
    lo, hi, kind = int(m.group(1)), int(m.group(2)), m.group(3)
    if kind == "beyond":
        lo, hi = 100 - hi, 100 - lo
    print(f"{q} | {d} | {rpo:.2f} | {lo}-{hi} | {rpo*lo/100:.2f}-{rpo*hi/100:.2f}")
