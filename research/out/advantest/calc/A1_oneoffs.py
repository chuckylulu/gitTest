#!/usr/bin/env python3
"""A1 - Results: margins and profits with and without the one-off items management itself named
(Advantest, TSE 6857, IFRS, JPY). Fiscal year ends 31 March.
Items with a disclosed amount:
  - FY2024 Q4: impairment loss on goodwill/intangibles (Essai, SLT) 21,393 million, in other expenses -> operating income (A1-306, A1-307)
  - FY2025 Q1: gain on partial divestiture of a business 2,504 million, in other income -> operating income (A1-308)
  - FY2025 Q4: financial income from fair value of share call options 17,312 million, labelled one-off -> income before tax (A1-309, A1-310)
  - FY2026 Q1 / 1H: valuation gains on financial instruments related to strategic investments 41,075 / 54,171 million -> income before tax
    (itemised by management in the segment note, NOT labelled one-off; shown separately) (A1-312, A1-313)
Items named without an amount (cannot be removed): FY2025 Q4 one-off SG&A expenses (A1-311); FY2026 1H reversal of inventory
write-down (A1-315, A1-316). Tax effects of the items are not disclosed, so net income is not adjusted.
Run: python3 -I A1_oneoffs.py > A1_oneoffs.out.txt
"""

def pct(a, b):
    return 100.0 * a / b


IMP = 21393      # A1-306 (FY2024 Q4)
DIV = 2504       # A1-308 (FY2025 Q1)
CALL = 17312     # A1-309 (FY2025 Q4)
VAL_Q1 = 41075   # A1-312 (FY2026 Q1)
VAL_1H = 54171   # A1-313 (FY2026 1H)
VAL_Q2 = VAL_1H - VAL_Q1

rows = []
# (label, sales, gross profit, operating income, income before tax, OI adjustment, IBT adjustment, note)  all JPY million
# single quarters from YTD differencing / tanshin (see A1_pnl.out.txt section 4) or slides x1000 where only slides exist
rows.append(("FY2024 (Apr 2024-Mar 2025)", 779707, 445085, 228161, 224774, +IMP, +IMP, "add back impairment"))           # A1-002,006,014,017
rows.append(("FY2024 Q4 (Jan-Mar 2025) [FY - 9M]", 779707 - 547358, 445085 - 305851, 228161 - 164126, 224774 - 163192, +IMP, +IMP,
             "add back impairment"))                                                                   # A1-002/482, 006/483, 014/228, 017/484
rows.append(("FY2025 (Apr 2025-Mar 2026)", 1128610, 726107, 499120, 516720, -DIV, -DIV - CALL, "remove divestiture gain; remove call-option gain"))  # A1-001,005,013,016
rows.append(("FY2025 Q1 (Apr-Jun 2025)", 263776, 171638, 123952, 121357, -DIV, -DIV, "remove divestiture gain"))       # A1-324, A1-335, A1-325, A1-336
rows.append(("FY2025 Q4 (Jan-Mar 2026) [FY - 9M]", 1128610 - 800537, 726107 - 504987, 499120 - 346006, 516720 - 344349, 0, -CALL,
             "remove call-option gain; one-off SG&A amount not disclosed"))                                              # A1-001/116, 005/117, 013/118, 016/119
rows.append(("FY2026 Q1 (Apr-Jun 2026)", 367473, 255553, 189990, 234082, 0, -VAL_Q1,
             "remove valuation gains (not labelled one-off); inventory reversal amount not disclosed"))                 # A1-107,108,111,113
rows.append(("FY2026 Q2 (Jul-Sep 2026) [1H - Q1]", 845200 - 367473, 595378 - 255553, 456809 - 189990, 510234 - 234082, 0, -VAL_Q2,
             "remove valuation gains (not labelled one-off)"))                                                            # A1-094/107, 095/108, 098/111, 100/113
rows.append(("1H FY2026 (Apr-Sep 2026)", 845200, 595378, 456809, 510234, 0, -VAL_1H,
             "remove valuation gains (not labelled one-off); inventory reversal amount not disclosed"))                 # A1-094,095,098,100

print("label | GM reported | OM reported -> ex items | IBT margin reported -> ex items | OI ex items | IBT ex items | note")
for lbl, s, g, o, i, adj_o, adj_i, note in rows:
    print(f"{lbl} | GM {pct(g, s):.1f}% | OM {pct(o, s):.1f}% -> {pct(o + adj_o, s):.1f}% | IBT {pct(i, s):.1f}% -> {pct(i + adj_i, s):.1f}% | "
          f"OI ex {o + adj_o:,} | IBT ex {i + adj_i:,} | {note}")
print(f"\nFY2025 combined items removed from income before tax: divestiture {DIV:,} + call-option gain {CALL:,} = {DIV + CALL:,} million")
print(f"\nValuation gains FY2026 Q2 (1H minus Q1) = {VAL_Q2:,} million (management says Q2 financial income 14.7 bn, A1-314)")
print("Gross margin: no named one-off with a disclosed amount sits in cost of sales; reported GM = GM ex disclosed one-offs for all periods.")
print("Services & Others segment income FY2024 Q4 ex impairment (A1_segments: -16,590): %s" % f"{-16590 + IMP:,}")
print("Services & Others segment income FY2025 ex divestiture gain: %s (reported 8,758, A1-189)" % f"{8758 - DIV:,}")
print("Services & Others segment income FY2025 Q1 ex divestiture gain: %s (reported 2,706, A1-329)" % f"{2706 - DIV:,}")
print("Services & Others segment income 1H FY2025 ex divestiture gain: %s (reported 3,048, A1-204)" % f"{3048 - DIV:,}")

print("\n=== Operating income YoY with and without the named items in the comparison base (JPY million) ===")
OI_Q4_25, OI_Q4_24 = 499120 - 346006, 228161 - 164126   # A1-013/118, A1-014/228
OI_Q1_26, OI_Q1_25 = 189990, 123952                     # A1-111, A1-325
print(f"FY2025 Q4 OI {OI_Q4_25:,} vs FY2024 Q4 {OI_Q4_24:,}: reported {100 * (OI_Q4_25 / OI_Q4_24 - 1):+.1f}%; "
      f"vs FY2024 Q4 ex impairment {OI_Q4_24 + IMP:,}: {100 * (OI_Q4_25 / (OI_Q4_24 + IMP) - 1):+.1f}% "
      "(FY2025 Q4 one-off SG&A amount not disclosed, so the current quarter cannot be adjusted)")
print(f"FY2026 Q1 OI {OI_Q1_26:,} vs FY2025 Q1 {OI_Q1_25:,}: reported {100 * (OI_Q1_26 / OI_Q1_25 - 1):+.1f}%; "
      f"vs FY2025 Q1 ex divestiture gain {OI_Q1_25 - DIV:,}: {100 * (OI_Q1_26 / (OI_Q1_25 - DIV) - 1):+.1f}% "
      "(FY2026 Q1 inventory write-down reversal amount not disclosed, so the current quarter cannot be adjusted)")
