#!/usr/bin/env python3
"""A1 calculations for KLA (KLAC). FY ends June 30. All inputs in USD thousands.

Sources (research/sources/kla/):
  Q2 FY26 (Oct-Dec 2025): 2026-01-29_kla_earnings-release-Fiscal-2026-Second.pdf (P&L, CF, segment, recon)
  Q3 FY26 (Jan-Mar 2026): 2026-04-29_kla_earnings-release-Fiscal-2026-Third.pdf
  Q4 FY26 (Apr-Jun 2026) + FY26/FY25: 2026-07-28_kla_earnings-release-Fiscal-2026-Fourth.pdf
  Q1 FY27 (Jul-Sep 2026) + Q1 FY26: 2026-10-28_kla_earnings-release-Fiscal-2027-First.pdf
  FY25 Q1 adjustment split: 2024-10-30_kla_earnings-release-Fiscal-2025-First.pdf
  SBC FY26/FY25: 2026-08-06_kla_10-K-FY26.html (cash flow statement)
  Major products: 10-Q Q2 FY26, 10-Q Q3 FY26 (incl. 9M FY25), 10-K FY26 (FY26/FY25), 10-Q Q1 FY27 (Q1 FY27, Q4 FY26, Q1 FY26)
Operating income is not a reported line; GAAP operating income = revenue - cost of revenues - R&D - SG&A - impairment.
Non-GAAP adds back KLA's named items located above the operating line (acquisition-related charges,
restructuring/severance, goodwill & intangible impairment).
"""

Q = {
    # rev, product, service, cogs, rnd, sga, impairment, adj_cogs, adj_rnd, adj_sga, adj_below_op, ni, ng_ni, ocf, capex, sbc, py_rev
    "Q1FY26": dict(rev=3209696, prod=2465006, svc=744690, cogs=1243070, rnd=360461, sga=268988, imp=0,
                   a_cogs=38053, a_rnd=0, a_sga=10973, a_below=0, ni=1121040, ngni=1166805,
                   ocf=1161591, capex=95894, sbc=70182, py_rev=None),
    "Q2FY26": dict(rev=3297146, prod=2511093, svc=786053, cogs=1271210, rnd=383871, sga=279919, imp=0,
                   a_cogs=38052, a_rnd=0, a_sga=10950, a_below=0, ni=1145682, ngni=1168182,
                   ocf=1367607, capex=105576, sbc=73947, py_rev=3076851),
    "Q3FY26": dict(rev=3415078, prod=2640287, svc=774791, cogs=1327672, rnd=388763, sga=291134, imp=0,
                   a_cogs=37106, a_rnd=0, a_sga=9872, a_below=0, ni=1200990, ngni=1238628,
                   ocf=707451, capex=85187, sbc=83938, py_rev=3063029),
    "Q4FY26": dict(rev=3657556, prod=2837151, svc=820405, cogs=1413108, rnd=399023, sga=291477, imp=0,
                   a_cogs=36200, a_rnd=0, a_sga=8470, a_below=-11601, ni=1363059, ngni=1385749,
                   ocf=906430, capex=89288, sbc=82104, py_rev=3174741),
    "Q1FY27": dict(rev=4136015, prod=3285469, svc=850546, cogs=1577791, rnd=395096, sga=301458, imp=0,
                   a_cogs=34929, a_rnd=0, a_sga=8111, a_below=0, ni=1548588, ngni=1603004,
                   ocf=1530939, capex=194756, sbc=84073, py_rev=3209696),
    # FY26 adjustments = sum of the four FY26 quarterly pre-tax tables (check vs 12M total 178,075)
    "FY26": dict(rev=13579476, prod=10453537, svc=3125939, cogs=5255060, rnd=1532118, sga=1131518, imp=0,
                 a_cogs=38053 + 38052 + 37106 + 36200, a_rnd=0, a_sga=10973 + 10950 + 9872 + 8470, a_below=-11601,
                 ni=4830771, ngni=4959364, ocf=4143079, capex=375945, sbc=310171, py_rev=12156162),
    # FY25: acquisition-related by line = Q1..Q4 FY25 tables; restructuring by line likewise; impairment 239,100 (Q2 FY25)
    "FY25": dict(rev=12156162, prod=9472854, svc=2683308, cogs=4751867, rnd=1360334, sga=1029734, imp=239100,
                 a_cogs=(44090 + 43348 + 41838 + 39024) + (901 + 429 + 0 + 1233),
                 a_rnd=(0 + 2994 + 0 + 0) + (1087 + 1166 + 0 - 3),
                 a_sga=(12604 + 12314 + 11825 + 11653) + (874 + 538 + 0 + 903), a_below=0,
                 ni=4061643, ngni=4451680, ocf=4081903, capex=335259, sbc=265011, py_rev=9812247),
}

# reported totals used as checks
CHECK_ADJ_TOTAL = {"FY26": 178075, "FY25": 219690 + 7128 + 239100}

KLA_STATED = {  # non-GAAP GM / OM stated by KLA (shareholder letters / slides)
    "Q1FY26": (62.5, 43.2), "Q2FY26": (62.6, 42.8), "Q3FY26": (62.2, 42.6), "Q4FY26": (62.4, 43.7), "Q1FY27": (62.7, 46.1)}


def pct(a, b):
    return 100.0 * a / b


out = {}
print("period | rev $M | YoY% | GAAP GM% | NG GM% | GAAP OM% | NG OM% | adj in COGS | adj in opex | FCF $M | SBC $M | SBC/FCF% | svc share%")
for k, d in Q.items():
    gp = d["rev"] - d["cogs"]
    op = gp - d["rnd"] - d["sga"] - d["imp"]
    ng_gp = gp + d["a_cogs"]
    ng_op = op + d["a_cogs"] + d["a_rnd"] + d["a_sga"] + d["imp"]
    fcf = d["ocf"] - d["capex"]
    yoy = pct(d["rev"] - d["py_rev"], d["py_rev"]) if d["py_rev"] else float("nan")
    r = dict(rev=d["rev"] / 1e3, yoy=yoy, gm=pct(gp, d["rev"]), nggm=pct(ng_gp, d["rev"]), om=pct(op, d["rev"]),
             ngom=pct(ng_op, d["rev"]), fcf=fcf / 1e3, sbc=d["sbc"] / 1e3, sbc_fcf=pct(d["sbc"], fcf),
             svc_share=pct(d["svc"], d["rev"]), op=op / 1e3, ng_op=ng_op / 1e3, ng_opex=(d["rnd"] + d["sga"] - d["a_rnd"] - d["a_sga"]) / 1e3)
    out[k] = r
    print(f"{k} | {r['rev']:,.1f} | {yoy:.1f} | {r['gm']:.2f} | {r['nggm']:.2f} | {r['om']:.2f} | {r['ngom']:.2f} | "
          f"{d['a_cogs']/1e3:,.1f} | {(d['a_rnd']+d['a_sga']+d['imp'])/1e3:,.1f} | {r['fcf']:,.1f} | {r['sbc']:,.1f} | {r['sbc_fcf']:.1f} | {r['svc_share']:.1f}")
    print(f"     GAAP op income {r['op']:,.1f}  non-GAAP op income {r['ng_op']:,.1f}  non-GAAP opex {r['ng_opex']:,.1f}")
    if k in KLA_STATED:
        s = KLA_STATED[k]
        print(f"     check vs KLA-stated NG GM {s[0]} / NG OM {s[1]}: diff {r['nggm']-s[0]:+.2f} / {r['ngom']-s[1]:+.2f} pp")
    if k in CHECK_ADJ_TOTAL:
        tot = d["a_cogs"] + d["a_rnd"] + d["a_sga"] + d["a_below"] + d["imp"]
        print(f"     check: summed pre-tax adjustments {tot:,} vs reported {CHECK_ADJ_TOTAL[k]:,} -> {'OK' if tot == CHECK_ADJ_TOTAL[k] else 'MISMATCH'}")

# FY26 quarterly sum check
s = sum(Q[q]["rev"] for q in ["Q1FY26", "Q2FY26", "Q3FY26", "Q4FY26"])
print(f"\ncheck FY26 rev = sum of quarters: {s:,} vs {Q['FY26']['rev']:,} -> {'OK' if s == Q['FY26']['rev'] else 'MISMATCH'}")
s = sum(Q[q]["sbc"] for q in ["Q1FY26", "Q2FY26", "Q3FY26", "Q4FY26"])
print(f"check FY26 SBC = sum of quarters: {s:,} vs {Q['FY26']['sbc']:,} -> {'OK' if s == Q['FY26']['sbc'] else 'MISMATCH'}")

# LTM to Sep 30, 2026 (Q2 FY26..Q1 FY27) and prior LTM (Q2 FY25..Q1 FY26)
L = ["Q2FY26", "Q3FY26", "Q4FY26", "Q1FY27"]
ltm = {f: sum(Q[q][f] for q in L) for f in ["rev", "cogs", "rnd", "sga", "a_cogs", "a_rnd", "a_sga", "ocf", "capex", "sbc", "ni", "ngni", "svc"]}
ltm_py_rev = sum(Q[q]["py_rev"] for q in L)
gp = ltm["rev"] - ltm["cogs"]; op = gp - ltm["rnd"] - ltm["sga"]
fcf = ltm["ocf"] - ltm["capex"]
print("\nLTM to Sep 30, 2026 (Q2 FY26 - Q1 FY27):")
print(f"  revenue {ltm['rev']/1e3:,.1f} $M; prior LTM {ltm_py_rev/1e3:,.1f} $M; YoY {pct(ltm['rev']-ltm_py_rev, ltm_py_rev):.1f}%")
print(f"  GAAP GM {pct(gp, ltm['rev']):.2f}%  NG GM {pct(gp+ltm['a_cogs'], ltm['rev']):.2f}%")
print(f"  GAAP OM {pct(op, ltm['rev']):.2f}%  NG OM {pct(op+ltm['a_cogs']+ltm['a_rnd']+ltm['a_sga'], ltm['rev']):.2f}%")
print(f"  OCF {ltm['ocf']/1e3:,.1f}  capex {ltm['capex']/1e3:,.1f}  FCF {fcf/1e3:,.1f} $M (KLA-stated LTM FCF 4,037.6)")
print(f"  SBC {ltm['sbc']/1e3:,.1f} $M; SBC/FCF {pct(ltm['sbc'], fcf):.1f}%; FCF margin {pct(fcf, ltm['rev']):.1f}%")
print(f"  GAAP NI {ltm['ni']/1e3:,.1f}  non-GAAP NI {ltm['ngni']/1e3:,.1f}; services {ltm['svc']/1e3:,.1f} ({pct(ltm['svc'], ltm['rev']):.1f}% of rev)")

# Segments (reportable-segment revenue, $K) with prior-year quarter
SEG = {
    "Q2FY26": {"SPC": (3004648, 2755743), "SSP": (140577, 160407), "PCB": (152175, 161080)},
    "Q3FY26": {"SPC": (3083912, 2738817), "SSP": (164028, 156500), "PCB": (167642, 168552)},
    "Q4FY26": {"SPC": (3256781, 2877647), "SSP": (159704, 141866), "PCB": (241110, 154106)},
    "Q1FY27": {"SPC": (3754254, 2899392), "SSP": (139487, 119755), "PCB": (242151, 189488)},
    "FY26":   {"SPC": (12244733, 10947359), "SSP": (584064, 587107), "PCB": (750415, 621721)},
}
print("\nSegments: $M, YoY %, share of total revenue %")
for k, d in SEG.items():
    rev = Q[k]["rev"]
    print(k, " | ".join(f"{s} {v[0]/1e3:,.1f} ({pct(v[0]-v[1], v[1]):+.1f}% YoY; {pct(v[0], rev):.1f}%)" for s, v in d.items()))

# Major products ($K). Prior-year Q4 FY25 = FY25 - 9M FY25 (from 10-K FY26 and 10-Q Q3 FY26)
FY25P = dict(WI=6198815, PAT=2196347, SSP=517201, PCB=355891, SVC=2683308, OTH=204600)
NM25 = dict(WI=4427238, PAT=1743504, SSP=394165, PCB=270489, SVC=1980749)
NM25["OTH"] = 8981421 - sum(NM25.values())
Q4FY25 = {k: FY25P[k] - NM25[k] for k in FY25P}
P = {
    "Q2FY26": (dict(WI=1572782, PAT=696161, SSP=121588, PCB=80348, SVC=786053, OTH=40214),
               dict(WI=1562610, PAT=530680, SSP=142987, PCB=93327, SVC=667389)),
    "Q3FY26": (dict(WI=1739671, PAT=615076, SSP=144199, PCB=95148, SVC=774791, OTH=46193),
               dict(WI=1495685, PAT=636415, SSP=138376, PCB=104254, SVC=669208)),
    "Q4FY26": (dict(WI=1781116, PAT=728099, SSP=136513, PCB=167526, SVC=820405, OTH=23897), Q4FY25),
    "Q1FY27": (dict(WI=2111203, PAT=862468, SSP=113597, PCB=167510, SVC=850546, OTH=30691),
               dict(WI=1537244, PAT=667427, SSP=100219, PCB=117298, SVC=744690, OTH=42818)),
    "FY26":   (dict(WI=6630813, PAT=2706763, SSP=502519, PCB=460320, SVC=3125939, OTH=153122), FY25P),
}
P["Q2FY26"][1]["OTH"] = 3076851 - sum(P["Q2FY26"][1].values())
P["Q3FY26"][1]["OTH"] = 3063029 - sum(P["Q3FY26"][1].values())
print("\nMajor products: $M (YoY %, share %)")
for k, (cur, py) in P.items():
    tot = sum(cur.values())
    chk = "OK" if tot == Q[k]["rev"] else f"MISMATCH {tot}"
    print(k, f"[sum check {chk}]", " | ".join(f"{p} {cur[p]/1e3:,.1f} ({pct(cur[p]-py[p], py[p]):+.1f}%; {pct(cur[p], Q[k]['rev']):.1f}%)" for p in cur))
q4sum = sum(Q4FY25.values())
print(f"derived Q4 FY25 products sum {q4sum:,} vs Q4 FY25 revenue 3,174,741 -> {'OK' if q4sum == 3174741 else 'MISMATCH'}")
# product-group check: four FY26 quarters sum to FY26 for WI
print("check WI FY26 sum of quarters:", 1537244 + 1572782 + 1739671 + 1781116, "vs 6630813")

# Services
print("\nServices:")
svc = {k: Q[k]["svc"] for k in ["Q2FY26", "Q3FY26", "Q4FY26", "Q1FY27"]}
svc_py = {"Q2FY26": 667389, "Q3FY26": 669208, "Q4FY26": 702559, "Q1FY27": 744690}
for k in svc:
    print(f"  {k}: {svc[k]/1e3:,.1f} $M, YoY {pct(svc[k]-svc_py[k], svc_py[k]):.1f}%, {pct(svc[k], Q[k]['rev']):.1f}% of revenue")
print(f"  FY26 {Q['FY26']['svc']/1e3:,.1f} $M, YoY {pct(Q['FY26']['svc']-Q['FY25']['svc'], Q['FY25']['svc']):.1f}%")
print(f"  >80% contract share applied to FY26 services (illustrative lower bound): {0.80*Q['FY26']['svc']/1e3:,.0f} $M "
      f"= {pct(0.80*Q['FY26']['svc'], Q['FY26']['rev']):.1f}% of FY26 revenue")

# Implied end-market split of Semi PC systems (semi customers only) -> DRAM / NAND share of that base
EM = {"Q2FY26": (60, 40, 75, 25), "Q3FY26": (62, 38, 86, 14), "Q4FY26": (79, 21, 83, 17)}
print("\nImplied DRAM / NAND share of Semi PC systems revenue to semi customers (KLA approx. mix x memory split):")
for k, (fl, mem, dr, na) in EM.items():
    print(f"  {k}: foundry/logic {fl}%, DRAM {mem*dr/100:.1f}%, NAND {mem*na/100:.1f}%")

# AP: implied CY26 growth vs $635M CY25 base
print(f"\nAP process control systems: ~1,100 / ~635 = {pct(1100-635, 635):.0f}% growth; "
      f"~950 total AP systems CY25 minus ~635 process-control = {950-635} $M non-process-control residual (implied)")

# Prior-claim check: CY25 mix (KLA Q2 FY26 slides p6-7, $M): "94.2% Semi PC + Services ... ~5.8% PCB/Comp Insp"
CY25 = dict(WI=6377, PAT=2453, SSP=483, PCB=387, SVC=2903, OTH=141)
CY25_TOT, CY25_SEG = 12745, dict(SPC=11521, SSP=559, PCB=664)
pc_sys = CY25["WI"] + CY25["PAT"] + CY25["OTH"]
print(f"\nCY25 check: product sum {sum(CY25.values())} vs total {CY25_TOT}; segment sum {sum(CY25_SEG.values())}")
print(f"  Semi PC systems (WI+PAT+Other) {pc_sys} $M; + services = {pc_sys+CY25['SVC']} = {pct(pc_sys+CY25['SVC'], CY25_TOT):.1f}% of CY25 revenue")
print(f"  PCB & Component segment share {pct(CY25_SEG['PCB'], CY25_TOT):.1f}%; PCB systems share {pct(CY25['PCB'], CY25_TOT):.1f}%; "
      f"SPC segment share {pct(CY25_SEG['SPC'], CY25_TOT):.1f}%")

# AP share of CY25 revenue, using KLA's two CY25 AP figures (letters Q2 FY26 p4 and Q3 FY26 p5)
print(f"\nAP share of CY25 revenue ($12,745M): total AP systems ~$950M = {pct(950, CY25_TOT):.1f}%; "
      f"AP process-control systems ~$635M = {pct(635, CY25_TOT):.1f}%; of Semi PC systems {pct(635, pc_sys):.1f}%")
