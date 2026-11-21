#!/usr/bin/env python3
"""XR module: unit conversions and simple derived dose figures.

Inputs (all read in saved documents; see research/out/customer_side/parts/XR.csv):
  - Intel, SMT007 Apr 2025 p54 (XR-002, XR-003): DRAM exposed in 50 rad steps up to 350 rads total;
    "overexposure to three times the limit provided by DRAM manufacturer".
  - Intel, same article p49 (XR-005): TLD minimum reportable dose 0.01 rad.
  - Hanyang/Radiate/Cisco, Electronics 15(22) 5391, Nov 2026 abstract (XR-026):
    HBM-relevant average dose-rate equivalent ~0.46 mGy(Si)/s at 115 kV, 130 uA, 1 mm Al.
Conventions: 1 rad = 0.01 Gy. The Intel dose is a TLD reading (material not stated in the article);
the Hanyang figure is a detector-derived equivalent, not an absorbed dose in the HBM dies.
These two quantities are NOT strictly comparable (the Hanyang TNS 2026 abstract, XR-025, reports a
5.46x spread from the choice of dose quantity alone), so any cross-study figure is Low confidence.
"""

RAD_TO_GY = 0.01

intel_total_rad = 350.0
intel_step_rad = 50.0
intel_multiple_of_limit = 3.0          # "three times the limit provided by DRAM manufacturer"
tld_min_rad = 0.01
hanyang_rate_mGy_per_s = 0.46

print(f"Intel total exposure: {intel_total_rad:.0f} rad = {intel_total_rad*RAD_TO_GY:.2f} Gy")
print(f"Intel step: {intel_step_rad:.0f} rad = {intel_step_rad*RAD_TO_GY:.2f} Gy; steps to 350 rad: {intel_total_rad/intel_step_rad:.0f}")
implied_limit_rad = intel_total_rad / intel_multiple_of_limit
print(f"Implied manufacturer limit (350 / 3): {implied_limit_rad:.1f} rad = {implied_limit_rad*RAD_TO_GY:.3f} Gy "
      f"(upper-bound reading; 'three times' may be rounded)")
print(f"TLD minimum reportable dose: {tld_min_rad} rad = {tld_min_rad*RAD_TO_GY*1000:.1f} mGy")

rate_Gy_s = hanyang_rate_mGy_per_s / 1000.0
for label, gy in [("1 Gy", 1.0), ("implied Intel limit", implied_limit_rad * RAD_TO_GY),
                  ("Intel 350 rad", intel_total_rad * RAD_TO_GY)]:
    s = gy / rate_Gy_s
    print(f"Beam-on time at 0.46 mGy(Si)/s to reach {label} ({gy:.3f} Gy): {s:,.0f} s = {s/60:,.1f} min")
