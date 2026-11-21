"""CL: second-document cross-checks of headline figures (JPY million unless stated)."""
# CL-032 FY2026 Q2 tanshin p.1, 1H (Apr-Sep 2026) YTD [F]; CL-142 FY2026 Q1 tanshin p.1, Q1 (Apr-Jun 2026) [F]
H1_S, H1_OI = 845_200, 456_809
Q1_S, Q1_OI = 367_473, 189_990
q2_s, q2_oi = H1_S - Q1_S, H1_OI - Q1_OI
print(f"FY2026 Q2 (Jul-Sep 2026) from tanshin YTD: sales {q2_s:,}; OI {q2_oi:,}; OPM {q2_oi/q2_s*100:.1f}%")
print("  vs slides p.5 (CL-024, CL-025): sales 477.7 bn, OI 266.8 bn, OPM 55.9%")
# FY2025 Q2 single quarter from YTD: FY2026 Q2 tanshin prints FY2025 1H 526,733 / 232,435; FY2026 Q1 tanshin prints FY2025 Q1 263,776 / 123,952
P_H1_S, P_Q1_S = 526_733, 263_776
p_q2 = P_H1_S - P_Q1_S
print(f"FY2025 Q2 (Jul-Sep 2025) from tanshin YTD: sales {p_q2:,} (slides p.5 print 262.9 bn; slide figure = 526.7 - 263.8)")
print(f"FY2026 Q2 sales YoY from tanshin: {(q2_s/p_q2-1)*100:.1f}% (slides p.5: +81.7%)")
# CL-137 Teradyne revenue, USD million [F]: Q3'26 1,306; Q2'26 1,329; Q3'25 769; CL-136 Q4'26 guidance 1,250-1,350 [C]
T_Q3, T_Q2, T_Q3P = 1306, 1329, 769
G_LO, G_HI = 1250, 1350
mid = (G_LO + G_HI) / 2
print(f"Teradyne Q3 2026 revenue QoQ: {(T_Q3/T_Q2-1)*100:.1f}%; YoY: {(T_Q3/T_Q3P-1)*100:.1f}%")
print(f"Teradyne Q4 2026 guidance midpoint {mid:,.0f} vs Q3 2026 actual: {(mid/T_Q3-1)*100:.1f}% (range {(G_LO/T_Q3-1)*100:.1f}% to {(G_HI/T_Q3-1)*100:.1f}%)")
