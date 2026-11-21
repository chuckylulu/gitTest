#!/usr/bin/env python3
"""A4 - one-off items named by management in the segment-income figures A4 cites (restatement check).
Advantest, fiscal year ends 31 March (FY2024 = Apr 2024-Mar 2025). Units: JPY million.
Inputs hard-coded from research/out/advantest/parts/A4.csv (evidence id in each comment).
Shows each segment-income figure with and without the item management itself named in the segment note.
Periods whose segment notes name no item (1H FY2024, 9M FY2024, Q1 FY2024) are listed with no adjustment.
Run: python3 -I research/out/advantest/calc/A4_oneoffs.py
"""

# --- FY2024 (Apr 2024-Mar 2025) ---
SSO_INC_OLD_FY24 = -10914    # A4-233: Services, Support and Others segment income (loss), old three-segment basis (83rd report p.132)
SO_INC_NEW_FY24 = -16125     # A4-239: Services and Others segment income (loss), restated two-segment basis (84th report p.132)
TOT_SEG_INC_FY24 = 231054    # A4-235 / A4-241: total segment income, both bases
IMPAIRMENT_FY24 = 21393      # A4-425 (84th p.132 note 2, new basis) and A4-426 (83rd p.133 note 2, old basis): Essai goodwill/intangibles impairment
# --- FY2025 1H (Apr-Sep 2025) ---
SO_INC_1H_FY25 = 3048        # A4-261: Services and Others segment income, 1H FY2025 (84th 1H report p.21)
TOT_SEG_INC_1H_FY25 = 234552 # A4-263: total segment income, 1H FY2025
DIVESTITURE_1H_FY25 = 2504   # A4-427: income from the partial divestiture of a business (84th 1H report p.21 note 2)

res = {}
res["sso_income_old_FY2024_ex_impairment"] = SSO_INC_OLD_FY24 + IMPAIRMENT_FY24
res["so_income_new_FY2024_ex_impairment"] = SO_INC_NEW_FY24 + IMPAIRMENT_FY24
res["services_income_change_reported"] = SO_INC_NEW_FY24 - SSO_INC_OLD_FY24
res["services_income_change_ex_impairment"] = res["so_income_new_FY2024_ex_impairment"] - res["sso_income_old_FY2024_ex_impairment"]
res["total_segment_income_FY2024_ex_impairment"] = TOT_SEG_INC_FY24 + IMPAIRMENT_FY24
res["so_income_1H_FY2025_ex_divestiture"] = SO_INC_1H_FY25 - DIVESTITURE_1H_FY25
res["total_segment_income_1H_FY2025_ex_divestiture"] = TOT_SEG_INC_1H_FY25 - DIVESTITURE_1H_FY25

print("Segment income with and without the one-off items management named (JPY million)")
print(f"FY2024 old 'Services, Support and Others': reported {SSO_INC_OLD_FY24:,}; ex impairment {IMPAIRMENT_FY24:,} -> {res['sso_income_old_FY2024_ex_impairment']:,}")
print(f"FY2024 new 'Services and Others':          reported {SO_INC_NEW_FY24:,}; ex impairment {IMPAIRMENT_FY24:,} -> {res['so_income_new_FY2024_ex_impairment']:,}")
print(f"   restatement effect on services income: reported {res['services_income_change_reported']:+,}; ex impairment {res['services_income_change_ex_impairment']:+,} (impairment sits in the services segment on both bases)")
print(f"FY2024 total segment income: reported {TOT_SEG_INC_FY24:,}; ex impairment {res['total_segment_income_FY2024_ex_impairment']:,}")
print(f"1H FY2025 'Services and Others': reported {SO_INC_1H_FY25:,}; ex divestiture income {DIVESTITURE_1H_FY25:,} -> {res['so_income_1H_FY2025_ex_divestiture']:,}")
print(f"1H FY2025 total segment income: reported {TOT_SEG_INC_1H_FY25:,}; ex divestiture income -> {res['total_segment_income_1H_FY2025_ex_divestiture']:,}")
print("1H FY2024, 9M FY2024, Q1 FY2024: segment notes name no one-off item for these periods (no adjustment).")
for k, v in res.items():
    print(f"RESULT {k} = {v}")
