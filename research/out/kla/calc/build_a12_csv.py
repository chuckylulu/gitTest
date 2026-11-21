import csv, sys
ROOT = "/home/user/gitTest/"
S = "research/sources/kla/"
U = {}
for r in csv.DictReader(open(ROOT + S + "_manifest.csv")):
    U[r["local_file"].split("/")[-1]] = r["url"]

D = {  # key: (file, document label, date)
    "R1": ("2026-10-28_kla_earnings-release-Fiscal-2027-First.pdf", "KLA Q1 FY27 earnings release", "2026-10-28"),
    "R4": ("2026-07-28_kla_earnings-release-Fiscal-2026-Fourth.pdf", "KLA Q4 FY26 earnings release", "2026-07-28"),
    "R3": ("2026-04-29_kla_earnings-release-Fiscal-2026-Third.pdf", "KLA Q3 FY26 earnings release", "2026-04-29"),
    "R2": ("2026-01-29_kla_earnings-release-Fiscal-2026-Second.pdf", "KLA Q2 FY26 earnings release", "2026-01-29"),
    "L1": ("2026-10-28_kla_shareholder-letter-Q1FY27.pdf", "KLA Letter to Shareholders Q1 FY27", "2026-10-28"),
    "L4": ("2026-07-28_kla_shareholder-letter-Q4FY26.pdf", "KLA Letter to Shareholders Q4 FY26", "2026-07-28"),
    "L3": ("2026-04-29_kla_shareholder-letter-Q3FY26.pdf", "KLA Letter to Shareholders Q3 FY26", "2026-04-29"),
    "L2": ("2026-01-29_kla_shareholder-letter-Q2FY26.pdf", "KLA Letter to Shareholders Q2 FY26", "2026-01-29"),
    "S1": ("2026-10-28_kla_earnings-slides-Q1FY27.pdf", "KLA earnings slides Q1 FY27", "2026-10-28"),
    "S2": ("2026-01-29_kla_earnings-slides-Q2FY26.pdf", "KLA earnings slides Q2 FY26", "2026-01-29"),
    "Q1": ("2026-10-29_kla_10-Q-Q1FY27.html", "KLA Form 10-Q Q1 FY27", "2026-10-29"),
    "Q3": ("2026-04-30_kla_10-Q-Q3FY26.html", "KLA Form 10-Q Q3 FY26", "2026-04-30"),
    "Q2": ("2026-01-30_kla_10-Q-Q2FY26.html", "KLA Form 10-Q Q2 FY26", "2026-01-30"),
    "K26": ("2026-08-06_kla_10-K-FY26.html", "KLA Form 10-K FY26", "2026-08-06"),
    "K25": ("2025-08-07_kla_10-K-FY25.html", "KLA Form 10-K FY25", "2025-08-07"),
    "ID": ("2026-03-12_kla_investor-day-2026-slides.pdf", "KLA Investor Day 2026 slides", "2026-03-12"),
    "IDT": ("2026-03-12_kla_investor-day-2026-transcript-all.pdf", "KLA Investor Day 2026 transcript (all presentations)", "2026-03-12"),
    "SU": ("2025-11-18_kla_services-update-wellsfargo.pdf", "KLA Services Update (Wells Fargo conf.)", "2025-11-18"),
}
CAL = {"Q2 FY26": "Oct-Dec 2025", "Q3 FY26": "Jan-Mar 2026", "Q4 FY26": "Apr-Jun 2026", "Q1 FY27": "Jul-Sep 2026",
       "FY26": "Jul 2025-Jun 2026", "FY25": "Jul 2024-Jun 2025", "Q2 FY27": "Oct-Dec 2026", "CY25": "Jan-Dec 2025",
       "CY26": "Jan-Dec 2026", "LTM Q1 FY27": "Oct 2025-Sep 2026", "Q1 FY26": "Jul-Sep 2025",
       "Jun 30 2026": "Jun 30, 2026", "Jun 30 2025": "Jun 30, 2025", "Sep 30 2026": "Sep 30, 2026",
       "Dec 31 2025": "Dec 31, 2025", "Mar 31 2026": "Mar 31, 2026", "Q2 FY26-Q1 FY27": "Oct 2025-Sep 2026",
       "FY24-FY26": "Jun 30, 2024-Jun 30, 2026", "CY22-CY26": "2022-2026"}
CALC1 = "research/out/kla/calc/a12_results.py"
CALC2 = "research/out/kla/calc/a12_leading.py"

rows = []
def F(part, tag, claim, value, unit, pf, doc, page, quote, conf="High", note=""):
    n = sum(1 for r in rows if r["id"].startswith(part)) + 1
    if doc in D:
        f, dl, dt = D[doc]
        lf, url = S + f, U[f]
    else:  # calc script
        f, dl, dt, lf, url = doc, doc, "2026-11-21", "", ""
    rows.append(dict(id=f"{part}-{n:03d}", tag=tag, claim=claim, value=value, unit=unit, period_fiscal=pf,
                     period_calendar=CAL.get(pf, pf), document=dl, date=dt, page_or_section=page, url=url,
                     local_file=lf, quote=quote, confidence=conf, note=note))

A = "A1"
# ---- revenue and P&L
F(A, "[F]", "Total revenue Q1 FY27 (also Q4 FY26 and Q1 FY26 comparatives)", "4136015", "USD thousands", "Q1 FY27", "R1", "p4",
  "Total revenues 4,136,015 3,657,556 3,209,696", note="Q4 FY26 3,657,556; Q1 FY26 3,209,696")
F(A, "[F]", "Total revenue Q4 FY26 and FY26 (with Q4 FY25 and FY25)", "3657556; FY26 13579476", "USD thousands", "FY26", "R4", "p4",
  "Total revenues 3,657,556 3,174,741 13,579,476 12,156,162", note="FY25 12,156,162; Q4 FY25 3,174,741")
F(A, "[F]", "Total revenue Q3 FY26 (Q3 FY25 comparative)", "3415078", "USD thousands", "Q3 FY26", "R3", "p4",
  "Total revenues 3,415,078 3,063,029 9,921,920 8,981,421")
F(A, "[F]", "Total revenue Q2 FY26 (Q2 FY25 comparative)", "3297146", "USD thousands", "Q2 FY26", "R2", "p4",
  "Total revenues 3,297,146 3,076,851 6,506,842 5,918,392")
F(A, "[I]", "Revenue YoY growth by quarter and FY26", "Q2 FY26 +7.2%; Q3 FY26 +11.5%; Q4 FY26 +15.2%; Q1 FY27 +28.9%; FY26 +11.7%; FY25 +23.9%",
  "%", "Q2 FY26-Q1 FY27", CALC1, "script output", "", note="Inputs: revenue rows A1-001..004 and prior-year comparatives in the same releases. High: direct arithmetic on reported totals.")
F(A, "[F]", "GAAP gross margin by quarter as reported in 10-Q MD&A (Q1 FY27, Q4 FY26, Q3 FY26, Q2 FY26, Q1 FY26)", "61.9; 61.4; 61.1; 61.4; 61.3", "%", "Q1 FY27", "Q1",
  "Item 2 MD&A, Executive Summary table", "Gross margin 61.9% 61.4% 61.1% 61.4% 61.3%")
F(A, "[F]", "Q1 FY27 cost of revenues (Q4 FY26, Q1 FY26 comparatives)", "1577791", "USD thousands", "Q1 FY27", "R1", "p4",
  "Costs of revenues 1,577,791 1,413,108 1,243,070")
F(A, "[F]", "Q1 FY27 pre-tax non-GAAP adjustment: acquisition-related charges 34,929 in cost of revenues and 8,111 in SG&A (total 43,040); only adjustment above net income besides tax items", "43040", "USD thousands", "Q1 FY27", "R1", "p7",
  "Costs of revenues $ 34,929 $ 34,929", note="Q4 FY26: COGS 36,200, SG&A 8,470, Other (income) -11,601; Q1 FY26: 38,053 / 10,973 (same table)")
F(A, "[F]", "KLA definition of its main non-GAAP one-off: acquisition-related charges are mainly amortisation of acquired intangibles", "definition", "text", "Q1 FY27", "R1", "p8",
  "Acquisition-related charges primarily include amortization of intangible assets.")
F(A, "[F]", "Q4 FY26 acquisition-related charges include a discrete $11.6M release of interest on unrecognized tax positions (recorded in Other expense (income), below operating line)", "11.6", "USD millions", "Q4 FY26", "R1", "p8",
  "also include a discrete release of $11.6 million of interest on unrecognized tax positions")
F(A, "[F]", "Q1 FY27 net-income-only one-offs: Pillar Two undertaxed-profits-rule taxes 20,151 and discrete tax items 5,785 added back to non-GAAP net income", "20151; 5785", "USD thousands", "Q1 FY27", "R1", "p6",
  "Pillar Two undertaxed profits rule taxes c 20,151", note="Discrete tax items Q4 FY26 6,780; Q1 FY26 15,087. KLA expects Pillar Two taxes to be temporary (footnote c, p8).")
F(A, "[F]", "Q2 FY26 pre-tax adjustments: acquisition-related 38,052 COGS + 10,950 SG&A = 49,002; no restructuring or impairment", "49002", "USD thousands", "Q2 FY26", "R2", "p7",
  "Total in three months ended Dec. 31, 2025 $ 49,002 $ — $ — $ 49,002")
F(A, "[F]", "Q3 FY26 pre-tax adjustments: acquisition-related 37,106 COGS + 9,872 SG&A = 46,978", "46978", "USD thousands", "Q3 FY26", "R3", "p7",
  "Total in three months ended March 31, 2026 $ 46,978 $ 46,978")
F(A, "[F]", "FY26 acquisition-related charges 178,075 (no restructuring, no impairment); FY25 219,690 acquisition + 7,128 restructuring + 239,100 impairment", "178075", "USD thousands", "FY26", "R4", "p6",
  "Acquisition-related charges a 33,069 46,978 50,677 178,075 219,690")
F(A, "[F]", "FY25 one-off: goodwill and purchased intangible impairment 239,100 (Q2 FY25) from deteriorated PCB business forecast", "239100", "USD thousands", "FY25", "R4", "p9",
  "resulted from the continued deterioration of the long-term forecast for our PCB business")
F(A, "[F]", "FY25 restructuring, severance and other charges 7,128 (employee severance)", "7128", "USD thousands", "FY25", "R4", "p6",
  "Restructuring, severance and other charges b — — 2,133 — 7,128")
F(A, "[F]", "Q1 FY27 non-GAAP gross margin (KLA-stated)", "62.7", "%", "Q1 FY27", "L1", "p3", "Non-GAAP gross margin was 62.7%")
F(A, "[F]", "Q1 FY27 non-GAAP operating margin (KLA-stated); non-GAAP opex $688M", "46.1", "%", "Q1 FY27", "L1", "p3",
  "Non-GAAP operating margin rose 240 bps sequentially to 46.1%")
F(A, "[F]", "Q4 FY26 non-GAAP gross margin 62.4% and operating margin 43.7% (KLA-stated)", "62.4; 43.7", "%", "Q4 FY26", "L4", "p3",
  "Non-GAAP operating margin was 43.7%", note="Same page: 'Non-GAAP gross margin was 62.4%'; letter cites memory pricing and tariff headwinds offset by services mix")
F(A, "[F]", "Q3 FY26 non-GAAP gross margin 62.2% and operating margin 42.6% (KLA-stated)", "62.2; 42.6", "%", "Q3 FY26", "L3", "p5",
  "Non-GAAP operating margin was 42.6%")
F(A, "[F]", "Q3 FY26 items KLA named but did NOT exclude or quantify: opex higher on prototype materials timing and reserve adjustments; OIE helped by mark-to-market gain on a strategic supply investment", "not quantified", "text", "Q3 FY26", "L3", "p5",
  "Operating expenses were higher than expected principally due to prototype materials timing and other reserve adjustments.", conf="High",
  note="Cannot show margin ex these items: amounts NOT DISCLOSED (read: Q3 FY26 letter p5; Q3 FY26 release recon).")
F(A, "[F]", "Q2 FY26 non-GAAP gross margin 62.6% and operating margin 42.8% (KLA-stated)", "62.6; 42.8", "%", "Q2 FY26", "L2", "p5",
  "Non-GAAP operating margin was 42.8%")
F(A, "[I]", "GAAP vs non-GAAP margins (non-GAAP = ex acquisition-related amortisation; FY25 also ex restructuring and impairment)",
  "GM GAAP/NG; OM GAAP/NG: Q2 FY26 61.45/62.60, 41.31/42.80; Q3 FY26 61.12/62.21, 41.21/42.59; Q4 FY26 61.36/62.35, 42.49/43.71; Q1 FY27 61.85/62.70, 45.01/46.05",
  "%", "Q2 FY26-Q1 FY27", CALC1, "script output", "",
  note="Inputs: P&L lines and pre-tax adjustment tables in R2-R4, R1. GAAP operating income = revenue - COGS - R&D - SG&A (KLA does not print an operating income line). High: recomputed NG margins match KLA-stated figures within 0.05pp.")
F(A, "[I]", "FY26 and FY25 margins with and without KLA-named one-offs",
  "FY26 GM 61.30 GAAP / 62.40 NG; OM 41.69 GAAP / 43.08 NG. FY25 GM 60.91 / 62.32; OM 39.28 / 43.11 (FY25 GAAP OM includes 239.1M impairment, 7.1M restructuring)",
  "%", "FY26", CALC1, "script output", "",
  note="Inputs: R4 12-month P&L; FY26 adjustments by line = sum of four quarterly tables (sum check = 178,075 OK); FY25 by line from Q1-Q4 FY25 tables (sum check 465,918 OK). High.")
F(A, "[I]", "LTM to Sep 30, 2026 revenue and YoY", "14505.8; +15.8% vs 12524.3", "USD millions", "LTM Q1 FY27", CALC1, "script output", "",
  note="Sum Q2 FY26..Q1 FY27 revenues; prior LTM = Q2 FY25..Q1 FY26. High.")
F(A, "[I]", "LTM to Sep 30, 2026 margins", "GM 61.47 GAAP / 62.47 NG; OM 42.64 GAAP / 43.91 NG", "%", "LTM Q1 FY27", CALC1, "script output", "",
  note="Summed quarterly P&L lines and adjustments. High.")
F(A, "[F]", "Q1 FY27 operating cash flow 1.53B and free cash flow 1.34B; LTM OCF 4.51B and FCF 4.04B (KLA-stated)", "1336183; LTM 4037620", "USD thousands", "Q1 FY27", "R1", "p1",
  "free cash flow was $1.34 billion and $4.04 billion")
F(A, "[F]", "Q1 FY27 capital expenditures (Q4 FY26 and Q1 FY26 comparatives)", "194756", "USD thousands", "Q1 FY27", "R1", "p5",
  "Capital expenditures (194,756) (89,288) (95,894)", note="OCF 1,530,939 - capex 194,756 = FCF 1,336,183 (p7 table)")
F(A, "[F]", "Q4 FY26 FCF 817.1M and FY26 FCF 3.77B (OCF 4.14B)", "817.1; FY26 3767.1", "USD millions", "FY26", "R4", "p1",
  "free cash flow was $817.1 million and $3.77 billion")
F(A, "[F]", "Q3 FY26 FCF (Q3 FY25 comparative; LTM Mar-26)", "622264", "USD thousands", "Q3 FY26", "R3", "p7",
  "Free cash flow $ 622,264 $ 990,024 $ 4,014,575")
F(A, "[F]", "Q2 FY26 FCF (Q2 FY25 comparative; LTM Dec-25)", "1262031", "USD thousands", "Q2 FY26", "R2", "p7",
  "Free cash flow $ 1,262,031 $ 757,192 $ 4,382,335")
F(A, "[F]", "Stock-based compensation Q1 FY27 (Q4 FY26, Q1 FY26)", "84073", "USD thousands", "Q1 FY27", "R1", "p5",
  "Stock-based compensation expense 84,073 82,104 70,182")
F(A, "[F]", "Stock-based compensation Q3 FY26 (Q3 FY25)", "83938", "USD thousands", "Q3 FY26", "R3", "p5",
  "Stock-based compensation expense 83,938 70,201")
F(A, "[F]", "Stock-based compensation Q2 FY26 (Q2 FY25)", "73947", "USD thousands", "Q2 FY26", "R2", "p5",
  "Stock-based compensation expense 73,947 61,841")
F(A, "[F]", "Stock-based compensation FY26 and FY25 (cash flow statement)", "310171; FY25 265011", "USD thousands", "FY26", "K26",
  "Item 8, Consolidated Statements of Cash Flows", "Stock-based compensation expense 310,171 265,011")
F(A, "[I]", "SBC / FCF", "Q2 FY26 5.9%; Q3 FY26 13.5%; Q4 FY26 10.0%; Q1 FY27 6.3%; FY26 8.2%; FY25 7.1%; LTM 8.0% (SBC 324.1M / FCF 4,037.6M)",
  "%", "LTM Q1 FY27", CALC1, "script output", "", note="SBC from cash-flow statements, FCF = OCF - capex. LTM FCF recomputed = KLA-stated 4,037.6M. High.")
F(A, "[F]", "Per-share figures from Q4 FY26 onward are post-split (10-for-1 effective June 11, 2026); Q2 and Q3 FY26 releases are pre-split", "10-for-1", "ratio", "Q1 FY27", "R1", "p1",
  "retroactively adjusted to reflect the ten-for-one stock split", note="Q2 FY26 NG EPS $8.85 and Q3 FY26 $9.40 are pre-split (= $0.885 / $0.94 post-split, as restated in R4)")
# ---- segments
F(A, "[F]", "Segment revenue Q1 FY27: Semiconductor Process Control (Q4 FY26, Q1 FY26)", "3754254", "USD thousands", "Q1 FY27", "R1", "p6",
  "Semiconductor Process Control $ 3,754,254 $ 3,256,781 $ 2,899,392", note="SSP 139,487 / 159,704 / 119,755; PCB & Component 242,151 / 241,110 / 189,488 (same table)")
F(A, "[F]", "Segment revenue Q4 FY26 and FY26: Semiconductor Process Control", "3256781; FY26 12244733", "USD thousands", "FY26", "R4", "p6",
  "Semiconductor Process Control $ 3,256,781 $ 2,877,647 $ 12,244,733 $ 10,947,359", note="FY26 SSP 584,064 (FY25 587,107); PCB 750,415 (FY25 621,721)")
F(A, "[F]", "Segment revenue Q3 FY26: Semiconductor Process Control", "3083912", "USD thousands", "Q3 FY26", "R3", "p6",
  "Semiconductor Process Control $ 3,083,912 $ 2,738,817", note="SSP 164,028 (156,500); PCB 167,642 (168,552)")
F(A, "[F]", "Segment revenue Q2 FY26: Semiconductor Process Control", "3004648", "USD thousands", "Q2 FY26", "R2", "p6",
  "Semiconductor Process Control $ 3,004,648 $ 2,755,743", note="SSP 140,577 (160,407); PCB 152,175 (161,080)")
F(A, "[I]", "Segment YoY and share of revenue",
  "SPC: Q2 FY26 +9.0% (91.1%), Q3 +12.6% (90.3%), Q4 +13.2% (89.0%), Q1 FY27 +29.5% (90.8%), FY26 +11.9% (90.2%); SSP: -12.4%, +4.8%, +12.6%, +16.5%, FY26 -0.5%; PCB: -5.5%, -0.5%, +56.5%, +27.8%, FY26 +20.7%",
  "%", "Q2 FY26-Q1 FY27", CALC1, "script output", "", note="Segment totals exclude FX effect line. High.")
# ---- products
F(A, "[F]", "Major products Q1 FY27 and Q4 FY26: Wafer Inspection 2,111,203 / 1,781,116; Patterning 862,468 / 728,099; Specialty Semi Process 113,597 / 136,513; PCB & Component 167,510 / 167,526; Services 850,546 / 820,405; Other 30,691 / 23,897",
  "2111203", "USD thousands", "Q1 FY27", "Q1", "Item 2 MD&A, supplementary revenue by major product categories",
  "Wafer Inspection $ 2,111,203 51 % $ 1,781,116 49 %", note="Q1 FY26 comparatives in same 10-Q: WI 1,537,244; Pat 667,427; SSP 100,219; PCB 117,298; Svc 744,690; Other 42,818")
F(A, "[F]", "Major products Q3 FY26: WI 1,739,671; Patterning 615,076; SSP 144,199; PCB 95,148; Services 774,791; Other 46,193", "1739671", "USD thousands", "Q3 FY26", "Q3",
  "Note: Segment reporting, revenues by major product categories", "Wafer Inspection $ 1,739,671 51 % $ 1,495,685 49 %")
F(A, "[F]", "Major products Q2 FY26: WI 1,572,782; Patterning 696,161; SSP 121,588; PCB 80,348; Services 786,053; Other 40,214", "1572782", "USD thousands", "Q2 FY26", "Q2",
  "Note: Segment reporting, revenues by major product categories", "Wafer Inspection $ 1,572,782 48 % $ 1,562,610 51 %")
F(A, "[F]", "Major products FY26 (FY25): WI 6,630,813 (6,198,815); Patterning 2,706,763 (2,196,347); SSP 502,519 (517,201); PCB 460,320 (355,891); Services 3,125,939 (2,683,308); Other 153,122 (204,600)",
  "6630813", "USD thousands", "FY26", "K26", "Item 8 Note: Segment reporting and geographic information", "Wafer Inspection $ 6,630,813 49 % $ 6,198,815 51 %")
F(A, "[F]", "KLA product-group definitions: Patterning = metrology + reticle inspection; Other = refurbished/remanufactured systems and upgrades (in Semi PC segment)", "definition", "text", "Q1 FY27", "Q1",
  "Note: Segment reporting", "Other includes primarily refurbished systems, remanufactured legacy systems, and enhancements and upgrades for previous-generation products")
F(A, "[I]", "Major product YoY growth",
  "WI: Q2 FY26 +0.7%, Q3 +16.3%, Q4 +0.5%, Q1 FY27 +37.3%, FY26 +7.0%; Patterning: +31.2%, -3.4%, +60.8%, +29.2%, FY26 +23.2%; SSP: -15.0%, +4.2%, +11.0%, +13.3%; PCB: -13.9%, -8.7%, +96.2%, +42.8%, FY26 +29.3%",
  "%", "Q2 FY26-Q1 FY27", CALC1, "script output", "", note="Q4 FY25 base derived = FY25 (10-K FY26) - 9M FY25 (10-Q Q3 FY26); derived base sums to reported Q4 FY25 revenue. Matches slide YoY %. High.")
F(A, "[F]", "No finer product split than these six groups (e.g. metrology vs reticle inspection, e-beam) in the quarterly docs", "NOT DISCLOSED", "text", "Q1 FY27", "L1", "p4",
  "Patterning systems, which include metrology products and reticle inspection", note="NOT DISCLOSED (read: 10-Q Q1 FY27 segment note; Q1 FY27 letter p3-4; slides p6)")
# ---- end markets
F(A, "[F]", "End-market definition: approx. Semi PC system-only sales to semiconductor customers only (not whole customer base)", "definition", "text", "Q1 FY27", "S1", "p5",
  "Represents approximate Semi Process Control system-only sales to Foundry/Logic customers or Memory customers only")
F(A, "[F]", "Q1 FY27 Semi PC systems mix: foundry/logic ~72%, memory ~28%; DRAM/NAND split for the quarter not given", "72; 28", "%", "Q1 FY27", "L1", "p4",
  "The Semi Process Control systems-only mix was approximately 72% Foundry/Logic and 28% Memory.", note="DRAM vs NAND actual: NOT DISCLOSED (read: Q1 FY27 letter p4, slides p5)")
F(A, "[F]", "Q4 FY26 Semi PC systems mix: foundry/logic ~79%, memory ~21%; DRAM ~83% / NAND 17% of memory", "79; 21; 83; 17", "%", "Q4 FY26", "L4", "p4",
  "approximately 83% of Memory revenue, and NAND 17%.")
F(A, "[F]", "Q3 FY26 Semi PC systems mix: foundry/logic ~62%, memory ~38%; DRAM 86% / NAND 14%", "62; 38; 86; 14", "%", "Q3 FY26", "L3", "p6",
  "86% of memory revenue, and NAND 14%.")
F(A, "[F]", "Q2 FY26 Semi PC systems mix: foundry/logic ~60%, memory ~40%; DRAM 75% / NAND 25%", "60; 40; 75; 25", "%", "Q2 FY26", "L2", "p6",
  "with DRAM accounting for 75% of memory revenue")
F(A, "[C]", "Q2 FY27 guidance mix: foundry/logic ~60%, memory ~40%; DRAM ~84% / NAND ~16%", "60; 40; 84; 16", "%", "Q2 FY27", "L1", "p8",
  "DRAM is expected to account for approximately 84%")
F(A, "[I]", "Implied DRAM / NAND share of Semi PC systems revenue to semi customers", "Q2 FY26 DRAM 30.0% NAND 10.0%; Q3 FY26 32.7% / 5.3%; Q4 FY26 17.4% / 3.6%",
  "%", "Q2 FY26-Q1 FY27", CALC1, "script output", "", conf="Medium", note="memory share x DRAM share of memory; both inputs are KLA approximations on a subset of revenue. Medium: approximate rounded inputs.")
# ---- services
F(A, "[F]", "Services revenue Q1 FY27 $850M, +14% YoY, 20% of revenue", "850.5", "USD millions", "Q1 FY27", "L1", "p2",
  "KLA Services revenue was $850 million in the quarter, up 14% year-over-year")
F(A, "[F]", "Services revenue Q4 FY26 $820M, +17% YoY, 22% of revenue", "820.4", "USD millions", "Q4 FY26", "L4", "p4",
  "Services revenue grew 6% sequentially and 17% year-over-year to $820 million")
F(A, "[F]", "Services revenue Q3 FY26 $775M, +16% YoY", "774.8", "USD millions", "Q3 FY26", "L3", "p6",
  "Services revenue grew 16% year-over-year and was down 1% sequentially to $775 million")
F(A, "[F]", "Services revenue Q2 FY26 $786M, +18% YoY, 24% of revenue", "786.1", "USD millions", "Q2 FY26", "L2", "p6",
  "Services revenue grew 18% year-over-year and 6% sequentially to $786 million")
F(A, "[I]", "Services FY26 total and growth; services share", "FY26 3,125.9M, +16.5% YoY, 23.0% of revenue; LTM 3,231.8M (22.3%)", "USD millions", "FY26", CALC1, "script output", "",
  note="Inputs: product/service split in R4 and quarterly releases. High.")
F(A, "[C]", "Services: >80% of revenue from multi-year subscription service contracts (up from >75% in CY22)", ">80", "% of services revenue", "CY25", "ID", "p104",
  "Industry-leading service model with >80% of revenue")
F(A, "[C]", "Services contract terms: ~3-year average contract length; 95% contract renewal rate; 95% of services revenue recurring incl. time-and-materials", "~3 yr; 95%; 95%", "text", "CY25", "ID", "p113",
  "~3-year average contract length", note="Same slide: '95% contract renewal rate' and '95% of revenue is recurring: inclusive of both contract and time-and-materials'")
F(A, "[C]", "Spoken at Investor Day: contract penetration >80%, contracts 'more than three years' (differs from slide's ~3-year average)", ">3 yr", "text", "CY25", "IDT", "p47",
  "These are more than three years")
F(A, "[C]", "Nov 2025 services update (CY24 actuals): >75% subscription-like contracts, >95% renewal, >3 yr contract length, 12-14% CAGR target", ">75%", "text", "CY24", "SU", "p3",
  ">75% of revenue coming from multi-year, subscription-like service contracts")
F(A, "[C]", "Long-term services revenue growth model raised to 13-15% CAGR at 2026 Investor Day (from 12-14% in 2022, 9-11% in 2019)", "13-15", "% CAGR", "CY25-CY30", "ID", "p109",
  "2026 Investor Day: 13-15%")
F(A, "[C]", "CY26 services growth expected at top end of the 13-15% model; 17th consecutive year of growth", "~15", "% YoY", "CY26", "L1", "p2",
  "top end of the Services revenue growth rate model of 13 to 15%")
F(A, "[F]", "CY25 services revenue $2.9B, +15%", "2.9", "USD billions", "CY25", "L2", "p2", "Services business grew 15% to $2.9")
# ---- AP / HBM / AI
F(A, "[C]", "CY25 advanced packaging total systems revenue ~ $950M, >70% YoY (KLA wording: 'total systems revenue')", "950", "USD millions", "CY25", "L2", "p4",
  "calendar 2025 total systems revenue of approximately $950 million, representing over 70% year-over-", note="Investor Day p68 also: '~$950M KLA Advanced Packaging Revenue in 2025'")
F(A, "[C]", "AP Semiconductor Process Control product revenue ~ $635M in 2025, ~ $1B expected CY26 (Apr-2026 view)", "635; 1000", "USD millions", "CY26", "L3", "p5",
  "approximately $635 million in 2025 to approximately $1 billion in calendar 2026")
F(A, "[C]", "AP process control systems revenue on track for ~ $1.1B in CY26, >70% YoY", "1100", "USD millions", "CY26", "L1", "p2",
  "Advanced Packaging process control systems revenue remains on track to hit approximately $1.1 billion", note="First raised to ~$1.1B in Q4 FY26 letter p2 ('above our prior expectation of high 50% growth')")
F(A, "[C]", "KLA AP intensity definition = Semi PC systems revenue in AP / AP market (5.6% in 2025)", "5.6", "%", "CY25", "ID", "p144",
  "KLA Packaging Intensity = KLA Semi PC systems revenue in Advanced Packaging / Advanced Packaging Market")
F(A, "[I]", "AP share of CY25 revenue on KLA's two definitions", "~7.5% (total AP systems $950M) / ~5.0% (AP process-control systems $635M) of CY25 revenue $12,745M; residual ~$315M not process control",
  "%", "CY25", CALC1, "script output", "", conf="Medium",
  note="Inputs: L2 p4, L3 p5, Q2 FY26 slides p6-7 CY25 total. Medium: KLA does not state that the $315M residual is SPTS/other; the split of $950M is inferred from the $635M figure.")
F(A, "[F]", "HBM or AI share of revenue: KLA gives no percentage; qualitative only", "NOT DISCLOSED", "text", "Q1 FY27", "L1", "p1",
  "increasing High-Bandwidth Memory (HBM) adoption", note="NOT DISCLOSED (read: Q1 FY27 letter, slides, 10-Q Q1 FY27; Q4 FY26 letter)")
F(A, "[C]", "Q2 FY27 guidance: revenue $4.7B +/- $200M; GAAP GM 61.8% +/- 1%; non-GAAP GM 62.5% +/- 1%; GAAP EPS $1.41, NG EPS $1.44 +/- $0.11 (post-split)", "4700", "USD millions", "Q2 FY27", "R1", "p2",
  "Total revenues are expected to be in a range of $4.7 billion +/- $200 million")

B = "A2"
F(B, "[F]", "Backlog (mainly written customer sales orders) $7.86B at Jun 30, 2025 -> $12.57B at Jun 30, 2026, attributed to AI-infrastructure demand", "12.57", "USD billions", "Jun 30 2026", "K26",
  "Part I Item 1 Business, Backlog", "increased from $7.86 billion as of June 30, 2025, to $12.57 billion as of June 30, 2026")
F(B, "[F]", "Backlog definition", "definition", "text", "Jun 30 2026", "K26", "Part I Item 1 Business, Backlog",
  "primarily consisting of sales orders where written customer requests have been received")
F(B, "[F]", "Backlog $9.83B (Jun 30, 2024) -> $7.86B (Jun 30, 2025); 71-76% expected as revenue in next 12 months", "7.86", "USD billions", "Jun 30 2025", "K25",
  "Part I Item 1 Business, Backlog", "We expect to recognize approximately 71% to 76% of this amount as revenue in the next 12 months",
  note="FY26 10-K gives no 12-month share: NOT DISCLOSED (read: 10-K FY26 Item 1 Backlog)")
F(B, "[C]", "Q1 FY27: backlog still growing (no amount)", "qualitative", "text", "Q1 FY27", "L1", "p8", "KLA backlog continues to grow",
  note="Quarterly backlog $, orders and book-to-bill: NOT DISCLOSED (read: 10-Q Q2 FY26, Q3 FY26, Q1 FY27; letters/slides Q2 FY26-Q1 FY27)")
F(B, "[C]", "Q2 FY26: customer lead times increasing due to supply constraints, limiting 1H CY26 growth", "qualitative", "text", "Q2 FY26", "L2", "p10",
  "Customer lead times for our products are increasing due to supply constraints")
F(B, "[I]", "Implied FY26 orders proxy and book-to-bill = (FY26 revenue + change in backlog) / FY26 revenue", "orders ~18.3B; book-to-bill ~1.35; backlog = 0.93x FY26 revenue",
  "ratio", "FY26", CALC2, "script output", "", conf="Low", note="Inputs: A2-001, FY26 revenue 13.58B. Low: KLA does not report orders; backlog scope, cancellations and FX are unknown.")
F(B, "[F]", "Inventory Sep 30, 2026 (Jun 30, 2026): service parts 639,024 (622,714); raw 2,126,927 (1,849,676); WIP 1,076,942 (937,724); FG 247,533 (238,424); total 4,090,426 (3,648,538)",
  "4090426", "USD thousands", "Sep 30 2026", "Q1", "Note 4 Financial statement components", "Raw materials 2,126,927 1,849,676")
F(B, "[F]", "Inventory Mar 31, 2026: service parts 602,543; raw 1,648,430; WIP 929,604; FG 256,469; total 3,437,046", "3437046", "USD thousands", "Mar 31 2026", "Q3",
  "Note 4 Financial statement components", "Raw materials 1,648,430 1,491,786")
F(B, "[F]", "Inventory Dec 31, 2025: service parts 625,503; raw 1,568,734; WIP 836,166; FG 252,202; total 3,282,605", "3282605", "USD thousands", "Dec 31 2025", "Q2",
  "Note 4 Financial statement components", "Raw materials 1,568,734 1,491,786")
F(B, "[F]", "Inventory Jun 30, 2025 baseline: service parts 600,769; raw 1,491,786; WIP 833,933; FG 285,661; total 3,212,149", "3212149", "USD thousands", "Jun 30 2025", "K26",
  "Item 8 Note 4 Balance sheet components", "Raw materials 1,849,676 1,491,786")
F(B, "[I]", "Inventory trend Jun-25 -> Sep-26", "total +27.3%; raw +42.6%; WIP +29.1%; FG -13.3%; raw share 47.8% (Dec-25) -> 52.0% (Sep-26); inventory days ~233-239",
  "%", "FY24-FY26", CALC2, "script output", "", note="Inventory days = ending inventory / quarterly COGS x days. High for arithmetic; interpretation (build ahead of shipments) Medium.")
F(B, "[F]", "Contract liabilities Sep 30, 2026 by expected recognition: <12m 1,477,240; 12-24m 167,971; >=24m 62,591; total 1,707,802", "1707802", "USD thousands", "Sep 30 2026", "Q1",
  "Note 2 Revenue", "Contract liabilities $ 1,477,240 $ 167,971 $ 62,591 $ 1,707,802")
F(B, "[F]", "KLA's RPO-style table covers only contract liabilities, not the full order backlog", "definition", "text", "Sep 30 2026", "Q1", "Note 2 Revenue",
  "which equals our contract liabilities")
F(B, "[F]", "Contract liabilities Jun 30, 2026: <12m 1,537,028; 12-24m 163,356; >=24m 74,755; total 1,775,139 (Jun 30, 2025: 1,713,689)", "1775139", "USD thousands", "Jun 30 2026", "K26",
  "Item 8 Note 2 Revenue", "Contract liabilities $ 1,537,028 $ 163,356 $ 74,755")
F(B, "[F]", "Contract liabilities Mar 31, 2026: <12m 1,197,342; 12-24m 170,588; >=24m 80,975; total 1,448,905", "1448905", "USD thousands", "Mar 31 2026", "Q3",
  "Note 2 Revenue", "Contract liabilities $ 1,197,342 $ 170,588 $ 80,975 $ 1,448,905")
F(B, "[F]", "Contract liabilities Dec 31, 2025: <12m 1,457,342; 12-24m 183,822; >=24m 86,727; total 1,727,891", "1727891", "USD thousands", "Dec 31 2025", "Q2",
  "Note 2 Revenue", "Contract liabilities $ 1,457,342 $ 183,822 $ 86,727 $ 1,727,891")
F(B, "[F]", "Deferred system revenue Sep 30, 2026 843,008 (Jun 30, 2026 932,901); deferred service revenue current 634,232 + non-current 230,562", "843008", "USD thousands", "Sep 30 2026", "R1", "p3",
  "Deferred system revenue 843,008 932,901", note="Dec-25: system 858,088, service 599,254+270,549 (R2 p4); Mar-26: 620,839, 576,503+251,563 (R3 p4)")
F(B, "[I]", "Contract liabilities share due <12 months and split", "Dec-25 84.3%; Mar-26 82.6%; Jun-26 86.6%; Sep-26 86.5%. Deferred system rev 858.1 / 620.8 / 932.9 / 843.0 $M",
  "%", "Q2 FY26-Q1 FY27", CALC2, "script output", "", note="Balance-sheet deferred revenue sums equal Note 2 totals (checks OK). High.")
F(B, "[F]", "Customer deposits (other current liabilities) Sep 30, 2026 493,816 vs Jun 30, 2026 430,128; non-current 13,960 vs 3,816", "493816", "USD thousands", "Sep 30 2026", "Q1",
  "Note 4 Financial statement components, Other current liabilities", "Customer deposits 493,816 430,128")
F(B, "[F]", "Customer deposits Mar 31, 2026 411,202 vs Jun 30, 2025 636,369", "411202", "USD thousands", "Mar 31 2026", "Q3",
  "Note 4, Other current liabilities", "Customer deposits 411,202 636,369")
F(B, "[F]", "Customer deposits Dec 31, 2025 363,121 vs Jun 30, 2025 636,369", "363121", "USD thousands", "Dec 31 2025", "Q2",
  "Note 4, Other current liabilities", "Customer deposits 363,121 636,369")
F(B, "[F]", "Accounts receivable, net Sep 30, 2026 3,072,087 (+6% vs Jun 30, 2026 2,889,208)", "3072087", "USD thousands", "Sep 30 2026", "Q1", "Note 2 Revenue",
  "Accounts receivable, net $ 3,072,087 $ 2,889,208 $ 182,879 6 %")
F(B, "[F]", "Long-term accounts receivable, net Sep 30, 2026 266,755 vs 180,729 (new line; nil at Jun 30, 2025)", "266755", "USD thousands", "Sep 30 2026", "Q1", "Note 2 Revenue",
  "Long-term accounts receivable, net $ 266,755 $ 180,729 $ 86,026 48 %")
F(B, "[F]", "Accounts receivable, net Mar 31, 2026", "2304454", "USD thousands", "Mar 31 2026", "Q3", "Note 2 Revenue", "Accounts receivable, net $ 2,304,454 $ 2,263,915")
F(B, "[F]", "Accounts receivable, net Dec 31, 2025", "2073581", "USD thousands", "Dec 31 2025", "Q2", "Note 2 Revenue", "Accounts receivable, net $ 2,073,581 $ 2,263,915")
F(B, "[F]", "Payment terms: 70-90% of contract value within 30-60 days of shipment, rest within 30 days of acceptance", "70-90", "%", "Q1 FY27", "Q1", "Note 2 Revenue",
  "payment of 70 % to 90 % of total contract consideration within 30 to 60 days of shipment")
F(B, "[I]", "DSO (ending net trade AR / quarterly revenue x days)", "Dec-25 57.9; Mar-26 60.7; Jun-26 71.9 (76.4 incl. LT AR); Sep-26 68.3 (74.3 incl. LT AR)", "days", "Q2 FY26-Q1 FY27", CALC2, "script output", "",
  note="High for arithmetic; factoring volumes (A2 factoring rows) reduce reported AR, so DSO is understated by an unknown amount when factoring is high.")
F(B, "[F]", "Receivables sold under factoring: FY26 515,480 (FY25 230,552); Q1 FY27 31,670 (Q1 FY26 106,367)", "515480", "USD thousands", "FY26", "K26", "Item 8 Note: Commitments and contingencies, Factoring",
  "Receivables sold under factoring agreements $ 515,480 $ 230,552 $ 254,889", note="Q2 FY26 70,425; Q3 FY26 109,405 (10-Qs); implied Q4 FY26 = 229,283 (a12_leading.py)")
F(B, "[F]", "Purchase commitments ~ $8.87B at Sep 30, 2026, majority due within 12 months", "8.87", "USD billions", "Sep 30 2026", "Q1", "Note 14 Commitments and contingencies",
  "approximately $ 8.87 billion as of September 30, 2026, a majority of which are due within the next 12 months")
F(B, "[F]", "Purchase commitments ~ $5.97B at Jun 30, 2026", "5.97", "USD billions", "Jun 30 2026", "K26", "Item 7 MD&A Liquidity, Contractual obligations",
  "significant purchase commitments primarily for material, services, supplies and asset purchases is $5.97 billion as of June 30, 2026")
F(B, "[F]", "Purchase commitments ~ $4.83B at Mar 31, 2026", "4.83", "USD billions", "Mar 31 2026", "Q3", "Note: Commitments and contingencies",
  "approximately $ 4.83 billion as of March 31, 2026")
F(B, "[F]", "Purchase commitments ~ $2.75B at Dec 31, 2025", "2.75", "USD billions", "Dec 31 2025", "Q2", "Note: Commitments and contingencies",
  "approximately $ 2.75 billion as of December 31, 2025")
F(B, "[F]", "KLA says it increased purchase commitments partly to secure key components", "qualitative", "text", "Q1 FY27", "Q1", "Item 2 MD&A, Executive summary",
  "We have also increased our purchase commitments, in part to secure the supply of key components")
F(B, "[I]", "Purchase commitments trend", "2.75 -> 4.83 -> 5.97 -> 8.87 $B (Dec-25 to Sep-26, 3.2x); Sep-26 = 1.59x LTM COGS", "ratio", "Q2 FY26-Q1 FY27", CALC2, "script output", "",
  note="High for arithmetic. Commitments are management estimates and may be cancelled/renegotiated (10-Q wording).")

sys.path.insert(0, ROOT + "research/tools")
import quote_check as qc, re
for r in rows:
    if r["local_file"].endswith(".pdf") and r["quote"] and re.match(r"p\d+$", r["page_or_section"]):
        texts, _ = qc.text_for(r["local_file"])
        nq, sq = qc.norm(r["quote"]), qc.squash(r["quote"])
        pages = [i for i, t in enumerate(texts, 1) if nq in qc.norm(t)] or [i for i, t in enumerate(texts, 1) if sq in qc.squash(t)]
        if pages and int(r["page_or_section"][1:]) not in pages:
            r["page_or_section"] = f"p{pages[0]}"
cols = ["id", "tag", "claim", "value", "unit", "period_fiscal", "period_calendar", "document", "date", "page_or_section", "url", "local_file", "quote", "confidence", "note"]
for part in ["A1", "A2"]:
    with open(ROOT + f"research/out/kla/parts/{part}.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        for r in rows:
            if r["id"].startswith(part + "-"):
                w.writerow(r)
from collections import Counter
for part in ["A1", "A2"]:
    print(part, Counter(r["tag"] for r in rows if r["id"].startswith(part + "-")))
