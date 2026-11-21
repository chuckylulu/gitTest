#!/usr/bin/env python3
"""Q5 supply-limit arithmetic (KLA, FY ends June 30). Inputs from FY25/FY26 10-K, Q1 FY27 10-Q (see Q5.csv)."""
bk = {"2024-06-30":9.83,"2025-06-30":7.86,"2026-06-30":12.57}   # $B backlog, 10-K Item 1
print(f"Backlog FY25 change {bk['2025-06-30']/bk['2024-06-30']*100-100:+.1f}%; FY26 change {bk['2026-06-30']/bk['2025-06-30']*100-100:+.1f}% (+${bk['2026-06-30']-bk['2025-06-30']:.2f}B)")
pc = {"2026-06-30":5.97,"2026-09-30":8.87}                      # $B purchase commitments
print(f"Purchase commitments Jun->Sep 2026 {pc['2026-09-30']/pc['2026-06-30']*100-100:+.1f}% (+${pc['2026-09-30']-pc['2026-06-30']:.2f}B)")
fy26_rev = 13.579476
print(f"Backlog / FY26 revenue = {bk['2026-06-30']/fy26_rev:.2f}x (~{bk['2026-06-30']/fy26_rev*12:.0f} months of FY26 revenue; backlog is mostly systems, so understates systems months)")
