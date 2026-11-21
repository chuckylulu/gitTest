#!/usr/bin/env python3
"""M: implied vendor revenues from third-party share figures relayed by Rigaku and Park.
Inputs (rows): M001-M003 (Rigaku IPO filing, Yole WFE MM Q2 2024), R011 (MTP, Yole Q4 2024),
R012/R013 (yuho FY2025, Yole Q4 2025), M014/M015 (KIRS chart / Dealsite, MarketsandMarkets AFM 2024),
M019 (Park PR, M&M AFM market 2024 USD 513.6m); M020/M021 (QY Research via Park, 2025).
Mixing editions is flagged; every output is [I] Low unless noted."""
mkt_2023_q2_24 = 481.0     # USD m, Yole WFE MM Q2 2024 (M002)
mkt_2026f_q2_24 = 663.0    # USD m forecast (M002)
rig_2022, rig_2023 = 0.269, 0.295   # M001
rig_2023_mtp, compA_2023_mtp = 0.30, 0.24  # R011 (Q4 2024 edition, chart)
mkt_2024_q4_25, rig_2024 = 498.0, 0.38     # R013, R012

print("CAGR 2023-2026 (check vs filing 11.3%%): %.1f%%" % (((mkt_2026f_q2_24/mkt_2023_q2_24)**(1/3)-1)*100))
print("Rigaku 2023 implied X-ray metrology revenue (Q2-24 edition): $%.0fm" % (rig_2023*mkt_2023_q2_24))
print("Company A 2023 implied revenue (24%% from Q4-24 chart x Q2-24 market; mixed editions): $%.0fm" % (compA_2023_mtp*mkt_2023_q2_24))
print("Rigaku 2024 implied (Q4-25 edition): $%.0fm" % (rig_2024*mkt_2024_q4_25))
print("Rigaku share change 2023->2024 (different editions): %+.1f pts" % ((rig_2024-rig_2023)*100))

afm_mkt_2024 = 513.6       # USD m, M&M via Park PR (M019)
shares_2024 = {"Park": 0.217, "Bruker": 0.158, "Oxford": 0.143, "Others": 0.482}  # M014/M015
print("AFM 2024 shares sum: %.1f%%" % (sum(shares_2024.values())*100))
for k, v in shares_2024.items():
    print("  %s implied 2024 AFM revenue (all AFM, research+industrial): $%.0fm" % (k, v*afm_mkt_2024))
print("Park lead over Bruker 2024: %.1f pts" % ((shares_2024['Park']-shares_2024['Bruker'])*100))

qy_mkt_2025, ind_rev_share_2025 = 508.69, 0.4341   # M020, M021 (QY Research via Park)
print("Industrial-grade AFM revenue 2025 (QY): $%.0fm of $%.2fm" % (qy_mkt_2025*ind_rev_share_2025, qy_mkt_2025))
