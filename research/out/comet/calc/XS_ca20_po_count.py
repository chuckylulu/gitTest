#!/usr/bin/env python3
"""XS: bounds on cumulative CA20 purchase orders implied by Comet's own wording.

Inputs (all Comet statements, see research/out/comet/parts/XS.csv):
  XS-049 Q3 2025 trading update (Oct 2025): "a handful of purchase orders" (no number)
  XS-051 CMD 2025 deck (13 Nov 2025) funnel: 2025 >60 evaluation, >25 qualification, 5 orders
  XS-052 CMD 2025 deck funnel 2023 baseline: 5 evaluation, 2 qualification, 0 orders
  XS-050 CMD 2025 release: "more than 80 active collaborations" on CA20
  XS-059/XS-060 H1 2026: "more than doubled CA20 purchase orders compared to YE25"
Reading A (deck wording): cumulative POs at 30 Jun 2026 > 2 x cumulative POs at 31 Dec 2025.
Cumulative orders cannot fall, so POs at YE25 >= 5 (the Nov 2025 funnel count).
Reading B (report wording without base): H1 2026 intake > 2 x some earlier period -> no count follows.
"""
orders_nov25 = 5          # XS-051
ye25_min = orders_nov25   # cumulative count can only rise from Nov to Dec 2025
h1_26_min_exclusive = 2 * ye25_min          # "more than doubled"
h1_26_min = h1_26_min_exclusive + 1         # integer POs
print(f"Reading A: cumulative CA20 POs at YE25 >= {ye25_min}")
print(f"Reading A: cumulative CA20 POs at 30 Jun 2026 > {h1_26_min_exclusive}, i.e. >= {h1_26_min}")
print(f"Reading A: implied new POs in H1 2026 >= {h1_26_min - ye25_min} (if YE25 were exactly {ye25_min})")

# funnel stage sums vs '>80 active collaborations'
ev25, q25, o25 = 60, 25, 5   # lower bounds (">60", ">25", "5")
print(f"Funnel 2025 stages summed: at least {ev25 + 1} + {q25 + 1} + {o25} = {ev25 + 1 + q25 + 1 + o25} (if stages are disjoint)")
print("Compare: CMD release '>80 active collaborations' (XS-050): consistent with the funnel total as a lower bound")
ev23, q23, o23 = 5, 2, 0
print(f"Funnel 2023 total engagements: {ev23 + q23 + o23}; orders 2023 -> 2025: {o23} -> {o25}")
