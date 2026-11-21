#!/usr/bin/env python3
"""China revenue in USD from 20-F geographic shares (Note 16B / 15B) x total revenue.
Usage: python3 -I research/out/nova/calc/china.py
Inputs (20-F FY2025 / FY2024 / FY2023 / FY2022): China share of total revenue and total revenue (USD k).
Shares are rounded to whole percent in the filings, so dollars carry about +/-0.5% of revenue.
"""
rev = {2021: 416_113, 2022: 570_729, 2023: 517_922, 2024: 672_396, 2025: 880_577}  # 20-F FY2022/FY2023/FY2025 statements
china = {2021: 21, 2022: 28, 2023: 36, 2024: 39, 2025: 33}
prev = None
for y in sorted(china):
    usd = rev[y] * china[y] / 100
    g = "" if prev is None else f"{100 * (usd - prev) / prev:+.1f}% YoY"
    print(f"FY{y}: China {china[y]}% x revenue {rev[y]:,} = {usd:,.0f}k {g}")
    prev = usd
