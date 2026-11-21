# R-series calculations (Rigaku vs Bruker X-ray metrology). Inputs typed from saved sources; see R.csv ids.
# 1) Rigaku 9M FY2025 vs 9M FY2024 semiconductor process control revenue by application (JPY bn),
#    read from chart labels on p10 of 2025-11-11_rigaku_results-presentation-FY25Q3.pdf (R030/R031)
fy24_9m = {"adv_logic_foundry": 5.5, "memory": 1.1, "wfe": 3.8, "power": 1.2, "others": 2.6, "parts_services": 2.5}
fy25_9m = {"adv_logic_foundry": 3.9, "memory": 3.6, "wfe": 1.6, "power": 1.4, "others": 2.3, "parts_services": 2.0}
for name, d, total_label in (("9M FY2024 (Jan-Sep 2024)", fy24_9m, 15.9), ("9M FY2025 (Jan-Sep 2025)", fy25_9m, 15.0)):
    s = sum(d.values())
    print(f"{name}: sum of segment labels = {s:.1f} vs bar total label {total_label}; "
          f"logic share of label total = {d['adv_logic_foundry']/total_label:.1%}, memory share = {d['memory']/total_label:.1%}")
print(f"Memory YoY 9M: {fy25_9m['memory']/fy24_9m['memory']-1:+.0%}; Logic YoY 9M: {fy25_9m['adv_logic_foundry']/fy24_9m['adv_logic_foundry']-1:+.0%}")
# 2) Implied Rigaku semiconductor X-ray metrology revenue from Rigaku-cited Yole market size x share
for yr, mkt, share, src in ((2023, 470, 0.30, "MTP Feb-2025 Fig.12/13 (Yole WFE Monitor Q4 2024)"),
                            (2024, 498, 0.38, "Yuho FY2025 p20 (Yole WFE Monitor Q4 2025)")):
    print(f"CY{yr}: market ${mkt}M x {share:.0%} = ${mkt*share:.0f}M implied Rigaku X-ray metrology revenue  [{src}]")
