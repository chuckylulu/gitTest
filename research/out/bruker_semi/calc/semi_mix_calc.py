"""Shares of Bruker semiconductor-metrology revenue implied by management statements (all inputs [S], transcripts).
Run: python3 -I research/out/bruker_semi/calc/semi_mix_calc.py"""
inputs = {
    'G050 AI/HPC-related semi metrology revenue FY2024 (lower bound, $M)': 125,
    'G051 total semi metrology revenue FY2024 (lower bound, $M)': 250,
    'G060 semi metrology revenue run-rate mid-2026 (approx, $M)': 300,
    'G061 production QA/QC portion (approx, $M)': 200,
    'G062 R&D portion (approx, $M)': 50,
    'G063 mask repair portion (approx, $M)': 50,
    'G064 Q4-25 pushout ($M)': 40,
    'G064 recaptured in Q1-26, low/high ($M)': (10, 15),
}
for k, v in inputs.items():
    print(f'{k}: {v}')
print()
print(f"AI/HPC share FY2024 ~ {125/250:.0%} (both figures are lower bounds; ratio is indicative only; CEO said 'about half')")
print(f"Production QA/QC share mid-2026 ~ {200/300:.0%}; R&D ~ {50/300:.0%}; mask repair ~ {50/300:.0%}")
print(f"Q4-25 pushout recaptured in Q1-26: {10/40:.0%}-{15/40:.0%}")
