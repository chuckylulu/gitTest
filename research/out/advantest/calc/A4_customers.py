#!/usr/bin/env python3
"""A4 - customer concentration: shares of net sales for customer groups >=10%.
Advantest, fiscal year ends 31 March (FY2025 = Apr 2025-Mar 2026). Units: JPY million.
Inputs are hard-coded from research/out/advantest/parts/A4.csv (evidence id in each comment).
Output lines 'RESULT <key> = <value>' are read back into A4.csv as [I] rows.
"""

# --- inputs (JPY million) ---
NVIDIA_FY25 = 243735  # A4-001: Net sales to the NVIDIA Group (customer group >=10% of net sales), FY2025 (JPY million)
TSMC_FY25 = 124922  # A4-002: Net sales to Taiwan Semiconductor Manufacturing Co., Ltd. (customer >=10% of net sales), FY2025 (JPY million)
TSMC_FY24 = 96158  # A4-003: Net sales to TSMC (>=10% customer), FY2024, as comparative in the 84th report (JPY million)
SAMSUNG_FY24 = 87734  # A4-004: Net sales to the Samsung Group (>=10% customer), FY2024, as comparative in the 84th report (JPY million)
TSMC_FY24_83 = 96158  # A4-005: Net sales to TSMC (>=10% customer), FY2024, as first reported in the 83rd report (JPY million)
SAMSUNG_FY24_83 = 87734  # A4-006: Net sales to the Samsung Group (>=10% customer), FY2024, as first reported in the 83rd report (JPY million)
SAMSUNG_FY23 = 57725  # A4-007: Net sales to the Samsung Group (only customer group >=10%), FY2023 (JPY million)
SALES_FY25 = 1128610  # A4-023: Net sales by region (Total), customer location, FY2025 (JPY million)
SALES_FY24 = 779707  # A4-024: Net sales by region (Total), customer location, FY2024 (comparative in 84th report) (JPY million)
SALES_FY23 = 486507  # A4-041: Net sales by region (Total), customer location, FY2023 (JPY million)
TOP5_FY25_PCT = 50  # A4-010: Top five customers' share of consolidated net sales, FY2025 ('approximately') (%)
TOP5_FY24_PCT = 48  # A4-009: Top five customers' share of consolidated net sales, FY2024 ('approximately') (%)
TOP5_FY23_PCT = 29  # A4-011: Five largest customers' share of net sales, FY2023 ('approximately') (%)
# --- single-counterparty table ('Sales by major counterparties', annual securities reports, Item 2 note 2) ---
NVIDIA_INTL_FY25 = 228273  # A4-406: NVIDIA International, Inc., FY2025 (JPY million), 84th report p.51
NVIDIA_INTL_PCT_FY25_PRINTED = 20.2  # A4-407: printed share, FY2025 (%)
TSMC_PCT_FY25_PRINTED = 11.1  # A4-408: printed TSMC share, FY2025 (%)
TSMC_PCT_FY24_PRINTED = 12.3  # A4-409: printed TSMC share, FY2024 (%)
SAMSUNG_EL_FY24 = 82795  # A4-410: Samsung Electronics Co., Ltd., FY2024 (JPY million), 84th report p.51
SAMSUNG_EL_PCT_FY24_PRINTED = 10.6  # A4-411: printed share, FY2024 (%)
SAMSUNG_EL_FY23 = 55325  # A4-412: Samsung Electronics Co., Ltd., FY2023 (JPY million), 83rd report p.50
SAMSUNG_EL_PCT_FY23_PRINTED = 11.4  # A4-413: printed share, FY2023 (%)


def pct(a, b):
    return 100.0 * a / b


res = {}
res["share_nvidia_FY2025"] = pct(NVIDIA_FY25, SALES_FY25)
res["share_tsmc_FY2025"] = pct(TSMC_FY25, SALES_FY25)
res["share_named_FY2025"] = pct(NVIDIA_FY25 + TSMC_FY25, SALES_FY25)
res["share_tsmc_FY2024"] = pct(TSMC_FY24, SALES_FY24)
res["share_samsung_FY2024"] = pct(SAMSUNG_FY24, SALES_FY24)
res["share_named_FY2024"] = pct(TSMC_FY24 + SAMSUNG_FY24, SALES_FY24)
res["share_samsung_FY2023"] = pct(SAMSUNG_FY23, SALES_FY23)
# top-five share left after the named >=10% customers (approximate: top-five % is 'approximately')
res["top5_minus_named_FY2025_pp"] = TOP5_FY25_PCT - res["share_named_FY2025"]
res["top5_minus_named_FY2024_pp"] = TOP5_FY24_PCT - res["share_named_FY2024"]
res["top5_minus_named_FY2023_pp"] = TOP5_FY23_PCT - res["share_samsung_FY2023"]
res["tsmc_sales_yoy_FY2025_pct"] = pct(TSMC_FY25 - TSMC_FY24, TSMC_FY24)
res["samsung_sales_yoy_FY2024_pct"] = pct(SAMSUNG_FY24 - SAMSUNG_FY23, SAMSUNG_FY23)
res["nvidia_FY2025_vs_10pct_threshold_FY2024_JPYm"] = 0.10 * SALES_FY24  # NVIDIA not named for FY2024 => below this
res["customer_FY2024_83rd_vs_84th_changed"] = int((TSMC_FY24 != TSMC_FY24_83) or (SAMSUNG_FY24 != SAMSUNG_FY24_83))
# group (note 6(6)) vs single counterparty (Item 2 table): scope difference, not a restatement
res["share_nvidia_intl_FY2025"] = pct(NVIDIA_INTL_FY25, SALES_FY25)
res["nvidia_group_minus_nvidia_intl_FY2025_JPYm"] = NVIDIA_FY25 - NVIDIA_INTL_FY25
res["nvidia_group_minus_nvidia_intl_FY2025_pp"] = pct(NVIDIA_FY25 - NVIDIA_INTL_FY25, SALES_FY25)
res["share_samsung_el_FY2024"] = pct(SAMSUNG_EL_FY24, SALES_FY24)
res["share_samsung_el_FY2023"] = pct(SAMSUNG_EL_FY23, SALES_FY23)
res["samsung_group_minus_samsung_el_FY2024_JPYm"] = SAMSUNG_FY24 - SAMSUNG_EL_FY24
res["samsung_group_minus_samsung_el_FY2023_JPYm"] = SAMSUNG_FY23 - SAMSUNG_EL_FY23
checks = [
    ("NVIDIA International FY2025", res["share_nvidia_intl_FY2025"], NVIDIA_INTL_PCT_FY25_PRINTED),
    ("TSMC FY2025", res["share_tsmc_FY2025"], TSMC_PCT_FY25_PRINTED),
    ("TSMC FY2024", res["share_tsmc_FY2024"], TSMC_PCT_FY24_PRINTED),
    ("Samsung Electronics FY2024", res["share_samsung_el_FY2024"], SAMSUNG_EL_PCT_FY24_PRINTED),
    ("Samsung Electronics FY2023", res["share_samsung_el_FY2023"], SAMSUNG_EL_PCT_FY23_PRINTED),
]
res["printed_pct_mismatches"] = sum(1 for _, c, p in checks if round(c, 1) != p)
# top-five residual on the single-counterparty basis (top-five basis, group or entity, is not stated)
res["top5_minus_named_entity_basis_FY2025_pp"] = TOP5_FY25_PCT - (NVIDIA_INTL_PCT_FY25_PRINTED + TSMC_PCT_FY25_PRINTED)

print("Customer concentration (shares of consolidated net sales)")
for k, v in res.items():
    print(f"RESULT {k} = {v:.4f}" if isinstance(v, float) else f"RESULT {k} = {v}")
print()
print(f"FY2025: NVIDIA {res['share_nvidia_FY2025']:.1f}%, TSMC {res['share_tsmc_FY2025']:.1f}%, together {res['share_named_FY2025']:.1f}%; top five ~{TOP5_FY25_PCT}%")
print(f"FY2024: TSMC {res['share_tsmc_FY2024']:.1f}%, Samsung {res['share_samsung_FY2024']:.1f}%, together {res['share_named_FY2024']:.1f}%; top five ~{TOP5_FY24_PCT}%")
print(f"FY2023: Samsung {res['share_samsung_FY2023']:.1f}%; top five ~{TOP5_FY23_PCT}%")
print(f"NVIDIA not named for FY2024 => FY2024 NVIDIA sales were below 10% of FY2024 net sales = JPY {res['nvidia_FY2025_vs_10pct_threshold_FY2024_JPYm']:,.0f} million")
print()
print("Printed single-counterparty shares vs shares computed from printed amounts:")
for name, c, p in checks:
    print(f"   {name}: computed {c:.2f}% vs printed {p}% -> {'MATCH' if round(c, 1) == p else 'MISMATCH'}")
print(f"NVIDIA Group (note 6(6)) JPY {NVIDIA_FY25:,} m vs NVIDIA International, Inc. (Item 2) JPY {NVIDIA_INTL_FY25:,} m: "
      f"other group entities JPY {res['nvidia_group_minus_nvidia_intl_FY2025_JPYm']:,} m ({res['nvidia_group_minus_nvidia_intl_FY2025_pp']:.1f} pp)")
# fix round 2 (2026-11-21): the two named >=10% customer groups in JPY million (A4-001 + A4-002), FY2025 (Apr 2025-Mar 2026)
print(f"RESULT named_FY2025_JPYm = {NVIDIA_FY25 + TSMC_FY25}  (NVIDIA Group {NVIDIA_FY25:,} + TSMC {TSMC_FY25:,}; "
      f"{pct(NVIDIA_FY25 + TSMC_FY25, SALES_FY25):.1f}% of FY2025 net sales)")
