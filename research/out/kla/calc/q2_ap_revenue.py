#!/usr/bin/env python3
"""Q2: KLA advanced-packaging (AP) revenue definitions and growth arithmetic.
All inputs are KLA's own rounded statements (shareholder letters, Investor Day deck).
Calendar years (CY). KLA fiscal year ends June 30. $ millions.
Run: python3 -I research/out/kla/calc/q2_ap_revenue.py
"""

# --- Inputs (source: shareholder letters; see Q2.csv ids) ---
ap_total_cy24 = 500.0        # Q4FY24/Q2FY25 letters: "more than/approximately $500 million" (all-KLA AP revenue)
ap_total_cy25 = 950.0        # Q2FY26 letter: "calendar 2025 total systems revenue of approximately $950 million"
ap_total_cy25_growth = 0.70  # Q2FY26 letter: "over 70% year-over-year growth" (a floor)
ap_total_cy25_est_jul25 = 925.0  # Q4FY25 letter: "exceed $925 million", "process control represents over 70%"
pc_share_floor_jul25 = 0.70
ap_total_cy26_growth_jan = 0.15  # Q2FY26 letter: CY26 "mid-teens" growth (total AP systems); 15% used as mid-point proxy
pc_cy25 = 635.0              # Q3FY26 letter: Semi PC product portfolio revenue "approximately $635 million in 2025"
pc_cy26_guides = {           # PC (Semi Process Control) AP systems revenue guides for CY26
    "Jan-2026 (Q3FY26 letter: prior >30%)": pc_cy25 * 1.30,
    "Apr-2026 (Q3FY26 letter)": 1000.0,
    "Jul-2026 (Q4FY26 letter)": 1100.0,
    "Oct-2026 (Q1FY27 letter, reaffirmed)": 1100.0,
}
kla_pkg_intensity_2025 = 0.056  # Investor Day slide 144: KLA Semi PC systems rev in AP / AP market

def pct(x):
    return f"{x*100:.1f}%"

print("1) Prior-chat check: +70% applied to $950M total vs $1.1B PC target")
print(f"   950 x 1.70 = {ap_total_cy25*1.70:.0f}  (not 1,100 -> definitions differ)")
print(f"   1,100 / 950 - 1 = {pct(1100/ap_total_cy25-1)}  (mixes PC CY26 with total CY25)")
print(f"   1,100 / 635 - 1 = {pct(1100/pc_cy25-1)}  (like-for-like PC growth; KLA says >70%)")

print("2) CY26 PC guide path, implied YoY on $635M base")
for k, v in pc_cy26_guides.items():
    print(f"   {k}: {v:.0f}  -> {pct(v/pc_cy25-1)}")

print("3) CY25 split total vs PC")
print(f"   PC share of total CY25 = 635/950 = {pct(pc_cy25/ap_total_cy25)}")
print(f"   Non-PC (SPTS process + PCB/Component incl. ICOS etc., not broken out) = {ap_total_cy25-pc_cy25:.0f}")
print(f"   Jul-2025 floor: >70% of >$925M = >{ap_total_cy25_est_jul25*pc_share_floor_jul25:.1f} (vs 635 final -> {pct(pc_cy25/ap_total_cy25_est_jul25)} of 925)")

print("4) CY24 base consistency")
print(f"   950/500 - 1 = {pct(ap_total_cy25/ap_total_cy24-1)} ; implied CY24 if growth exactly 70% = {ap_total_cy25/(1+ap_total_cy25_growth):.0f}")

print("5) Jan-2026 total-AP guide (mid-teens) applied to $950M")
print(f"   950 x 1.15 = {ap_total_cy25*(1+ap_total_cy26_growth_jan):.0f} (range 13-17%: {ap_total_cy25*1.13:.0f}-{ap_total_cy25*1.17:.0f})")

print("6) Implied AP equipment market 2025 from KLA packaging intensity 5.6%")
print(f"   635 / 0.056 = {pc_cy25/kla_pkg_intensity_2025:.0f}  (rounded inputs; KLA chart shows ~$11-12B)")
print("7) 'Almost two times faster than the AP market' (Q4FY26 letter): implied CY26 AP market growth")
print(f"   ~{pct((1100/pc_cy25-1)/2)} if exactly 2x; KLA gives no market figure")
