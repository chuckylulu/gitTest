"""Build research/out/kla/parts/A4.csv and A5.csv (15 evidence columns)."""
import csv, os
ROOT = "/home/user/gitTest"
S = "research/sources/kla/"
IR = "https://ir.kla.com/sec-filings/all-sec-filings/content/"
CDN = "https://d1io3yog0oux5.cloudfront.net/_e8ec0a75333fe915a94800e2cce2bfa3/klatencor/"
D = {  # key: (document, date, url, local_file)
 "10Q1FY23": ("KLA Form 10-Q Q1 FY23", "2022-10-27", IR+"0001628280-22-027311/klac-20220930.htm", S+"2022-10-27_kla_10-Q-Q1FY23.html"),
 "10KFY23": ("KLA Form 10-K FY23", "2023-08-04", IR+"0000319201-23-000031/klac-20230630.htm", S+"2023-08-04_kla_10-K-FY23.html"),
 "10KFY24": ("KLA Form 10-K FY24", "2024-08-05", IR+"0000319201-24-000021/klac-20240630.htm", S+"2024-08-05_kla_10-K-FY24.html"),
 "10KFY25": ("KLA Form 10-K FY25", "2025-08-07", IR+"0000319201-25-000024/klac-20250630.htm", S+"2025-08-07_kla_10-K-FY25.html"),
 "10KFY26": ("KLA Form 10-K FY26", "2026-08-06", IR+"0000319201-26-000027/klac-20260630.htm", S+"2026-08-06_kla_10-K-FY26.html"),
 "10Q1FY24": ("KLA Form 10-Q Q1 FY24", "2023-10-26", IR+"0000319201-23-000039/klac-20230930.htm", S+"2023-10-26_kla_10-Q-Q1FY24.html"),
 "10Q2FY24": ("KLA Form 10-Q Q2 FY24", "2024-01-26", IR+"0000319201-24-000006/klac-20231231.htm", S+"2024-01-26_kla_10-Q-Q2FY24.html"),
 "10Q3FY24": ("KLA Form 10-Q Q3 FY24", "2024-04-26", IR+"0000319201-24-000012/klac-20240331.htm", S+"2024-04-26_kla_10-Q-Q3FY24.html"),
 "10Q1FY25": ("KLA Form 10-Q Q1 FY25", "2024-10-31", IR+"0000319201-24-000027/klac-20240930.htm", S+"2024-10-31_kla_10-Q-Q1FY25.html"),
 "10Q2FY25": ("KLA Form 10-Q Q2 FY25", "2025-01-31", IR+"0000319201-25-000006/klac-20241231.htm", S+"2025-01-31_kla_10-Q-Q2FY25.html"),
 "10Q3FY25": ("KLA Form 10-Q Q3 FY25", "2025-05-01", IR+"0000319201-25-000012/klac-20250331.htm", S+"2025-05-01_kla_10-Q-Q3FY25.html"),
 "10Q1FY26": ("KLA Form 10-Q Q1 FY26", "2025-10-30", IR+"0000319201-25-000034/klac-20250930.htm", S+"2025-10-30_kla_10-Q-Q1FY26.html"),
 "10Q2FY26": ("KLA Form 10-Q Q2 FY26", "2026-01-30", IR+"0000319201-26-000008/klac-20251231.htm", S+"2026-01-30_kla_10-Q-Q2FY26.html"),
 "10Q3FY26": ("KLA Form 10-Q Q3 FY26", "2026-04-30", IR+"0000319201-26-000016/klac-20260331.htm", S+"2026-04-30_kla_10-Q-Q3FY26.html"),
 "10Q1FY27": ("KLA Form 10-Q Q1 FY27", "2026-10-29", IR+"0000319201-26-000034/klac-20260930.htm", S+"2026-10-29_kla_10-Q-Q1FY27.html"),
 "LQ4FY24": ("KLA Letter to Shareholders Q4 FY24", "2024-07-24", CDN+"db/1117/10550/letter_to_shareholders/KLA+Corporation+Q4FY24+Letter+to+Shareholders_FINAL.pdf", S+"2024-07-24_kla_shareholder-letter-Q4FY24.pdf"),
 "LQ2FY25": ("KLA Letter to Shareholders Q2 FY25", "2025-01-30", CDN+"db/1117/10569/letter_to_shareholders/KLA+Corporation+Q2FY25+Shareholder+Letter.pdf", S+"2025-01-30_kla_shareholder-letter-Q2FY25.pdf"),
 "LQ3FY25": ("KLA Letter to Shareholders Q3 FY25", "2025-04-30", CDN+"db/1117/10573/letter_to_shareholders/KLAC_LetterToShareholders_04.30.25-FINAL+.pdf", S+"2025-04-30_kla_shareholder-letter-Q3FY25.pdf"),
 "LQ4FY25": ("KLA Letter to Shareholders Q4 FY25", "2025-07-31", CDN+"db/1117/10585/letter_to_shareholders/KLA+Corporation+Q2CY25+Earnings+Letter+to+Shareholders.pdf", S+"2025-07-31_kla_shareholder-letter-Q4FY25.pdf"),
 "LQ1FY26": ("KLA Letter to Shareholders Q1 FY26", "2025-10-29", CDN+"db/1117/10596/letter_to_shareholders/KLA+Corporation+Letter+to+Shareholders+Q1+FY26.pdf", S+"2025-10-29_kla_shareholder-letter-Q1FY26.pdf"),
 "LQ2FY26": ("KLA Letter to Shareholders Q2 FY26", "2026-01-29", CDN+"db/1117/10612/letter_to_shareholders/KLA+Letter+to+Shareholders+-+Q2+FY26.pdf", S+"2026-01-29_kla_shareholder-letter-Q2FY26.pdf"),
 "LQ1FY27": ("KLA Letter to Shareholders Q1 FY27", "2026-10-28", CDN+"db/1117/10679/letter_to_shareholders/KLA_Earnings_Shareholder_Letter_-_Q1_FY27.pdf", S+"2026-10-28_kla_shareholder-letter-Q1FY27.pdf"),
 "SQ1FY27": ("KLA Earnings Slides Q1 FY27", "2026-10-28", CDN+"db/1117/10679/earnings_slide_presentation/KLA_Earnings_Slides_-_Q1_FY27.pdf", S+"2026-10-28_kla_earnings-slides-Q1FY27.pdf"),
 "RQ1FY24": ("KLA Earnings Release Q1 FY24", "2023-10-25", CDN+"news/2023-10-25_KLA_Corporation_Reports_Fiscal_2024_First_Quarter__466.pdf", S+"2023-10-25_kla_earnings-release-Fiscal-2024-First.pdf"),
 "RQ3FY26": ("KLA Earnings Release Q3 FY26", "2026-04-29", CDN+"news/2026-04-29_KLA_Corporation_Reports_Fiscal_2026_Third_Quarter__514.pdf", S+"2026-04-29_kla_earnings-release-Fiscal-2026-Third.pdf"),
 "SPLIT": ("KLA Stock Split FAQ", "2026-05-07", "https://d1io3yog0oux5.cloudfront.net/_0ebdd7ea4324b85d41343cefc23f5eca/klatencor/db/1126/10661/description/05.07.26-KLAC-Stock-Split-FAQs.pdf", S+"2026-05-07_kla_stock-split-FAQ.pdf"),
 "TQ1FY26": ("Motley Fool transcript, KLA Q1 FY26 call", "2025-10-29", "https://www.fool.com/earnings/call-transcripts/2025/10/30/kla-klac-q1-2026-earnings-call-transcript/", S+"2025-10-29_press-fool_call-transcript-Q1FY26.html"),
 "TQ2FY26": ("Motley Fool transcript via Yahoo Finance, KLA Q2 FY26 call", "2026-01-29", "https://finance.yahoo.com/news/kla-klac-q2-2026-earnings-234213081.html", S+"2026-01-29_press-fool-yahoo_call-transcript-Q2FY26.html"),
 "TQ3FY26": ("Motley Fool transcript, KLA Q3 FY26 call", "2026-04-29", "https://www.fool.com/earnings/call-transcripts/2026/04/29/kla-klac-q3-2026-earnings-call-transcript/", S+"2026-04-29_press-fool_call-transcript-Q3FY26.html"),
 "TQ1FY27": ("Motley Fool transcript, KLA Q1 FY27 call", "2026-10-28", "https://www.fool.com/earnings/call-transcripts/2026/10/29/kla-klac-q1-2027-earnings-call-transcript/", S+"2026-10-28_press-fool_call-transcript-Q1FY27.html"),
 "TF": ("TrendForce news: KLA predicts 20% drop in China sales for 2025", "2024-12-10", "https://www.trendforce.com/news/2024/12/10/news-chip-equipment-giant-kla-predicts-20-drop-in-china-sales-for-2025-amid-new-u-s-export-curbs/", S+"2024-12-10_press-trendforce_kla-china-2025-export-impact.html"),
 "SPB": ("Squire Patton Boggs alert: BIS extends suspension of Affiliates Rule", "2026-11-09", "https://www.squirepattonboggs.com/insights/publications/bis-extends-suspension-of-affiliates-rule/", S+"2026-11-09_press-squirepb_affiliates-suspension-extension.html"),
 "FR23": ("Federal Register 88 FR 73424, BIS IFR Export Controls on Semiconductor Manufacturing Items (2023-23049)", "2023-10-25", "https://www.govinfo.gov/content/pkg/FR-2023-10-25/pdf/2023-23049.pdf", S+"2023-10-25_bis-fr_rule-SME-Oct2023.pdf"),
 "FR24": ("Federal Register 89 FR 96790, BIS IFR Foreign-Produced Direct Product Rule Additions... (2024-28270)", "2024-12-05", "https://www.govinfo.gov/content/pkg/FR-2024-12-05/html/2024-28270.htm", S+"2024-12-05_bis-fr_rule-FDPR-HBM-SME-Dec2024.html"),
 "FR25A": ("Federal Register 90 FR 47201, BIS IFR Expansion of End-User Controls to Cover Affiliates (2025-19001)", "2025-09-30", "https://www.govinfo.gov/content/pkg/FR-2025-09-30/pdf/2025-19001.pdf", S+"2025-09-30_bis-fr_rule-affiliates-50pct-Sep2025.pdf"),
 "FR25S": ("Federal Register 2025-19846, BIS final rule One-Year Suspension of Affiliates Rule", "2025-11-12", "https://www.govinfo.gov/content/pkg/FR-2025-11-12/html/2025-19846.htm", S+"2025-11-12_bis-fr_rule-affiliates-suspension-Nov2025.html"),
 "CALC4": ("calc a4_china_share.py (output a4_china_share_output.txt)", "2026-11-21", "", "research/out/kla/calc/a4_china_share.py"),
 "CALC4P": ("calc a4_region_parse.py / a4_segment_parse.py", "2026-11-21", "", "research/out/kla/calc/a4_region_parse.py"),
 "CALC5": ("calc a5_capital.py (output a5_capital_output.txt)", "2026-11-21", "", "research/out/kla/calc/a5_capital.py"),
}
QCAL = {"Q1 FY24":"Jul-Sep 2023","Q2 FY24":"Oct-Dec 2023","Q3 FY24":"Jan-Mar 2024","Q4 FY24":"Apr-Jun 2024",
 "Q1 FY25":"Jul-Sep 2024","Q2 FY25":"Oct-Dec 2024","Q3 FY25":"Jan-Mar 2025","Q4 FY25":"Apr-Jun 2025",
 "Q1 FY26":"Jul-Sep 2025","Q2 FY26":"Oct-Dec 2025","Q3 FY26":"Jan-Mar 2026","Q4 FY26":"Apr-Jun 2026","Q1 FY27":"Jul-Sep 2026",
 "FY21":"Jul 2020-Jun 2021","FY22":"Jul 2021-Jun 2022","FY23":"Jul 2022-Jun 2023","FY24":"Jul 2023-Jun 2024","FY25":"Jul 2024-Jun 2025","FY26":"Jul 2025-Jun 2026"}
A4, A5 = [], []
def row(lst, part, tag, claim, value, unit, pf, doc, sec, quote="", conf="", note="", pc=None):
    d = D[doc]
    lst.append([f"{part}-{len(lst)+1:03d}", tag, claim, value, unit, pf, pc or QCAL.get(pf, ""), d[0], d[1], sec, d[2], d[3], quote, conf, note])

GEO = "Note 'Segment Reporting and Geographic Information' (revenues by geographic region)"
# ---------- A4: China revenue as reported (F)
for q, doc, v, sh, tot in [
 ("Q1 FY24","10Q1FY24","1,025,944","43","2,396,956"),("Q2 FY24","10Q2FY24","1,027,780","41","2,486,726"),
 ("Q3 FY24","10Q3FY24","996,885","42","2,359,830"),("Q1 FY25","10Q1FY25","1,198,305","42","2,841,541"),
 ("Q2 FY25","10Q2FY25","1,092,525","36","3,076,851"),("Q3 FY25","10Q3FY25","792,884","26","3,063,029"),
 ("Q1 FY26","10Q1FY26","1,267,156","39.5","3,209,696"),("Q2 FY26","10Q2FY26","994,891","30.2","3,297,146"),
 ("Q3 FY26","10Q3FY26","829,583","24.3","3,415,078"),("Q1 FY27","10Q1FY27","1,425,744","34.5","4,136,015")]:
    dollar = "" if q in ("Q3 FY25","Q3 FY26") else "$ "
    row(A4,"A4","[F]",f"KLA revenue from customers in China (ship-to), {q}; reported share {sh}%", v, "$ thousands", q, doc, GEO,
        f"China {dollar}{v} {sh} %", "", f"Total revenue same table: ${tot}k. Share as printed by KLA (rounded).")
for fy, doc, v, sh, tot in [("FY24","10KFY24","4,196,727","43","9,812,247"),("FY25","10KFY25","4,042,567","33","12,156,162"),("FY26","10KFY26","4,048,358","29.8","13,579,476")]:
    row(A4,"A4","[F]",f"KLA fiscal-year revenue from customers in China, {fy}; reported share {sh}%", v, "$ thousands", fy, doc, GEO,
        f"China $ {v} {sh} %", "", f"Total revenue ${tot}k.")
row(A4,"A4","[F]","China revenue Q4 FY26 as reported directly in the QoQ table of the next 10-Q (26.2%)","956,728","$ thousands","Q4 FY26","10Q1FY27","Item 2 MD&A, Revenues by region (Q1 FY27 vs Q4 FY26)",
    "China $ 1,425,744 34.5 % $ 956,728 26.2 %","","Matches FY26 10-K minus 9M FY26 (calc). Q4 FY24 and Q4 FY25 are not printed as quarters; derived in calc.")
row(A4,"A4","[F]","China revenue +49% QoQ and +13% YoY in Q1 FY27","+49% QoQ / +13% YoY","%","Q1 FY27","10Q1FY27","Item 2 MD&A, Revenues by region",
    "Revenues from our customers in China increased 49% in the three months ended September 30, 2026 compared to","",
    "Same paragraph: 'and increased 13% compared to the same period in the prior year, primarily driven by increased demand from foundry/logic customers, particularly at mature technology nodes'.")
# ---------- A4: China share series (I)
series = [("Q1 FY24","42.8"),("Q2 FY24","41.3"),("Q3 FY24","42.2"),("Q4 FY24","44.6"),("Q1 FY25","42.2"),("Q2 FY25","35.5"),
          ("Q3 FY25","25.9"),("Q4 FY25","30.2"),("Q1 FY26","39.5"),("Q2 FY26","30.2"),("Q3 FY26","24.3"),("Q4 FY26","26.2"),("Q1 FY27","34.5")]
for q, s in series:
    extra = " Q4 derived as fiscal year (10-K) minus nine months (Q3 10-Q)." if q.startswith("Q4") else ""
    row(A4,"A4","[I]",f"China share of total revenue, {q}", s, "%", q, "CALC4", "output table quarter rows", "",
        "High", "Inputs: China and total revenue from the 10-Q/10-K geography note (rows above)." + extra)
for k, v, pc, n in [("CY2024","40.9","Jan-Dec 2024","China $4,433,833k / $10,846,957k"),("CY2025","31.5","Jan-Dec 2025","China $4,013,785k / $12,744,612k"),
                    ("CY2026 9M","28.7","Jan-Sep 2026","China $3,212,055k / $11,208,649k")]:
    row(A4,"A4","[I]",f"China share of revenue, calendar {k} (sum of fiscal quarters)", v, "%", k, "CALC4", "Calendar-year block", "", "High", n, pc=pc)
row(A4,"A4","[I]","China revenue change CY2025 vs CY2024","-9.5","%","CY2025","CALC4","Calendar-year block","","High",
    "KLA's Dec 2024 expectation (CFO at UBS, per TrendForce [S]) was ~20% decline; actual decline smaller.",pc="Jan-Dec 2025")
row(A4,"A4","[I]","China revenue change Jan-Sep 2026 vs Jan-Sep 2025 (total revenue +18.6% in same period)","+6.4","%","CY2026 9M","CALC4","Calendar-year block","","High",
    "China grows slower than total: consistent with CFO statement that China grows slower than WFE.",pc="Jan-Sep 2026")
row(A4,"A4","[I]","China share before the FY24-FY25 surge: FY21 26.5%, FY22 28.9%, FY23 27.3%","26.5 / 28.9 / 27.3","%","FY21-FY23","CALC4","Pre-surge baseline block","","High",
    "Inputs FY23 10-K geography note (2023/2022/2021 columns).",pc="Jul 2020-Jun 2023")
row(A4,"A4","[I]","CY2026 China share implied if Q2 FY27 China share is 25-29% on $4.70B guidance midpoint","27.6 to 28.8","%","CY2026","CALC4","Scenario block","","Medium",
    "Depends on Q2 FY27 actuals (not yet reported); consistent with KLA's 'high-20s' CY2026 statement.",pc="Jan-Dec 2026")
# last-4-quarter regional mix (I)
mix = {"Q2 FY26":"China 30.2; Taiwan 25.6; Korea 14.5; North America 12.0; Japan 6.9; Rest of Asia 5.9; Europe & Israel 4.9",
       "Q3 FY26":"Taiwan 25.4; China 24.3; Korea 19.9; North America 12.0; Europe & Israel 7.2; Rest of Asia 5.8; Japan 5.3",
       "Q4 FY26":"Taiwan 31.1; China 26.2; North America 17.9; Korea 10.2; Japan 5.8; Europe & Israel 4.6; Rest of Asia 4.3",
       "Q1 FY27":"China 34.5; Taiwan 24.7; North America 14.9; Korea 12.0; Rest of Asia 5.3; Europe & Israel 4.7; Japan 3.9"}
for q, m in mix.items():
    row(A4,"A4","[I]",f"Revenue by region, share of total, {q}", m, "%", q, "CALC4", "Region mix, last 4 quarters", "", "High",
        "Inputs: 10-Q geography notes; Q4 FY26 from FY26 10-K minus 9M (matches Q1 FY27 10-Q QoQ table within $1k rounding).")
row(A4,"A4","[I]","LTM (Q2 FY26-Q1 FY27) revenue by region share","China 29.0; Taiwan 26.7; North America 14.3; Korea 14.0; Japan 5.4; Rest of Asia 5.3; Europe & Israel 5.3","%","Q2 FY26-Q1 FY27","CALC4","LTM line","","High",
    "LTM total $14,505,795k.",pc="Oct 2025-Sep 2026")
row(A4,"A4","[F]","Q1 FY27 regional split per letter; KLA expects China to decline in Dec quarter and be ~high-20s% of CY2026 revenue","high-20s","% of CY2026 revenue","Q1 FY27","LQ1FY27","p. 5, regional revenue split",
    "China should decline as a percentage of total revenue in the December quarter and represent approximately the high-20s percent of total revenue for calendar 2026","",
    "Forward-looking: [C]-type company expectation recorded as [F] that KLA said it.")
# restatement checks
row(A4,"A4","[I]","Prior-period regional revenue: no unexplained changes. Q1-Q3 of FY24, FY25 and Q1 FY26 as first reported equal the prior-year column of the next year's 10-Q for all 7 regions and total; FY23/FY24/FY25 annual regions equal across later 10-Ks","0 differences","count","Q1 FY24-Q1 FY27","CALC4","Restatement check block","","High",
    "56 quarterly region-cells and 3 annual vintages compared. Q4 FY26 derived vs printed differs by $1k (NA, Europe) = rounding.",pc="Jul 2023-Sep 2026")
row(A4,"A4","[I]","Prior-period segment revenue: no unexplained changes. Segment revenue (SPC, SSP, PCB&CI) for Q1-Q3 FY24, Q1-Q3 FY25, Q1 FY26 and FY23-FY25 as first reported equals later comparatives","0 differences","count","Q1 FY24-Q1 FY27","CALC4P","a4_segment_parse.py output vs first-reported tables","","High",
    "Only change: segment renamed from 'PCB, Display and Component Inspection' (FY23-Q3 FY24) to 'PCB and Component Inspection' (FY24 10-K on); amounts unchanged.",pc="Jul 2023-Sep 2026")
row(A4,"A4","[I]","Q4 FY24 letter China share 44% vs 44.6% derived from 10-K minus 9M (rounded to make regions sum to 100%)","44.6 vs 44","%","Q4 FY24","CALC4","Q4FY24 rounding check","","Medium",
    "Presentation rounding in letter, not a restatement; letter regions sum to 100%.")
row(A4,"A4","[F]","Q4 FY24 letter regional split: China 44%","44","%","Q4 FY24","LQ4FY24","p. 7, regional revenue split",
    "The June quarter regional revenue split in descending order was: China at 44%, Taiwan at 20%, and North America at 12% of total revenue.","","")
# ---------- A4: customers
row(A4,"A4","[F]","Customers >10% of revenue named in FY26 10-K: TSMC only, for FY26, FY25 and FY24","TSMC","name","FY24-FY26","10KFY26","Item 1 Business (customers table); Note 17",
    "The following customer accounted for more than 10% of our total revenues, primarily in our Semiconductor Process Control segment, for the indicated periods:","",
    "Table lists Taiwan Semiconductor Manufacturing Company Limited under 2026, 2025 and 2024.",pc="Jul 2023-Jun 2026")
row(A4,"A4","[F]","Largest customer (TSMC) share of revenue FY26 and FY25","19","% of revenue","FY26","10KFY26","Note 17 Segment Reporting and Geographic Information",
    "In each of the fiscal years ended June 30, 2026 and 2025, one customer accounted for approximately 19 % of total revenues.","","Customer unnamed in the % sentence; named TSMC in Item 1 table.",pc="Jul 2024-Jun 2026")
row(A4,"A4","[F]","Largest customer share FY24","13","% of revenue","FY24","10KFY24","Note 19 Segment Reporting and Geographic Information",
    "In the fiscal year ended June 30, 2024, one customer accounted for approximately 13 % of total revenues.","","")
row(A4,"A4","[F]","FY23: two customers >10% (TSMC and Samsung named in FY24/FY25 10-K tables)","18 and 15","% of revenue","FY23","10KFY25","Note 16 Segment Reporting and Geographic Information",
    "In the fiscal year ended June 30, 2023, two customers accounted for approximately 18 % and 15 % of total revenues.","","FY22: 20% and 12% (FY24 10-K).")
row(A4,"A4","[F]","FY24 10-K names TSMC and Samsung as >10% customers (FY23, FY22 for Samsung); FY24 only TSMC","TSMC; Samsung","name","FY22-FY24","10KFY24","Item 1 Business, customers",
    "the following customers each accounted for more than 10% of total revenues, primarily in the Semiconductor Process Control segment:","",
    "Table: 2024 TSMC; 2023 TSMC; 2022 TSMC; Samsung listed twice (2023, 2022). FY25 10-K lists Samsung once (2023).",pc="Jul 2021-Jun 2024")
row(A4,"A4","[F]","Q1 FY27: two unnamed customers >10% of revenue","21 and 13","% of revenue","Q1 FY27","10Q1FY27","Note 16 Segment Reporting and Geographic Information",
    "In the three months ended September 30, 2026, two customers accounted for approximately 21 % and 13 % of total revenues each.","","Quarterly customers are not named.")
row(A4,"A4","[F]","Q1 FY26: three unnamed customers >10% of revenue","15, 11 and 10","% of revenue","Q1 FY26","10Q1FY26","Note 16",
    "In the three months ended September 30, 2025, three customers accounted for approximately 15 %, 11 %, and 10 % of total revenues each.","","")
row(A4,"A4","[F]","Q2 FY26: two unnamed customers >10% of revenue","17 and 11","% of revenue","Q2 FY26","10Q2FY26","Note 16",
    "In the three months ended December 31, 2025, two customers accounted for approximately 17 % and 11 % of total revenues each.","","")
row(A4,"A4","[F]","Q3 FY26: two unnamed customers >10% of revenue","19 and 11","% of revenue","Q3 FY26","10Q3FY26","Note 16",
    "In the three months ended March 31, 2026, two customers accounted for approximately 19 % and 11 % of total revenues each.","","Q3 FY25 comparative: one customer 23%.")
row(A4,"A4","[F]","Receivables: three customers >10% of AR at Mar 31, 2026 (two at Jun 30, 2025; two at Dec 31, 2025; three at Sep 30, 2025)","3","customers","Q3 FY26","10Q3FY26","Note 16",
    "Three customers and two customers on an individual basis accounted for greater than 10 % of accounts receivable, net, at March 31, 2026","",
    "AR concentration not stated in FY26 10-K or Q1 FY27 10-Q: NOT DISCLOSED.")
row(A4,"A4","[F]","Receivables: TSMC >10% of AR at Jun 30, 2024 (TSMC and Samsung at Jun 30, 2023)","TSMC","name","FY24","10KFY24","Note 1 Concentration of credit risk",
    "The following customers each accounted for more than 10% of net accounts receivable as of the dates indicated below:","",
    "Names listed in table; FY25 10-K confirms one customer at Jun 30, 2024 and two at Jun 30, 2025 (unnamed).")
# ---------- A4: export rules and KLA statements
row(A4,"A4","[F]","Oct 2022 BIS rules: KLA preliminary estimate of gross direct CY2023 revenue impact $500M-$900M (based on backlog)","500-900","$ million","Q1 FY23","10Q1FY23","Item 2 MD&A",
    "potential combined gross direct impact on revenue, based on existing backlog, in the range of approximately $500 million to $900 million in calendar year 2023","",
    "KLA added the estimate excludes reallocation of systems to other customers.",pc="Jan-Dec 2023")
row(A4,"A4","[F]","Oct 2022 rules: KLA said by FY23 10-K they had not significantly impacted operations to date","not significant","qualitative","FY23","10KFY23","Item 7 MD&A",
    "while they have not significantly impacted our operations to date","","")
row(A4,"A4","[F]","Oct 2022 rules scope as KLA describes: licences for effectively all KLA products/services to China fabs making non-planar or <=16/14nm logic, >=128L NAND, <=18nm hp DRAM","scope","qualitative","Q2 FY25","10Q2FY25","Item 2 MD&A",
    "the 2022 BIS Rules impose export license requirements effectively on all KLA products and services to customers located in China that fabricate:","",
    "Oct 7, 2022 IFR (87 FR 62186) itself NOT RETRIEVED (govinfo 502). Date Oct 7, 2022 confirmed in 88 FR 73424 summary.")
row(A4,"A4","[F]","Oct 2023 BIS SME rule (published Oct 25, 2023, 88 FR 73424) revises the Oct 7, 2022 IFR","2023-10-25","date","Q2 FY24","FR23","p. 1 (88 FR 73424), SUMMARY",
    "SUMMARY: On October 7, 2022, the","","",pc="Oct 2023")
row(A4,"A4","[F]","Oct 2023 rules: KLA gave no quantified impact; still evaluating","not quantified","qualitative","Q1 FY24","10Q1FY24","Item 2 MD&A",
    "The 2023 BIS Rules are very complex and we are still evaluating these rules and assessing their impact on our business and operations.","","")
row(A4,"A4","[F]","Dec 2024 BIS IFR (effective Dec 2, 2024): new SME controls, new FDP rules, HBM controls; published with Entity List rule","2024-12-02","effective date","Q2 FY25","FR24","SUMMARY and DATES",
    "adding new controls for certain high bandwidth memory important for advanced computing","","Same summary: 'creating new Foreign Direct Product (FDP) rules'; 'Effective date: This rule is effective December 2, 2024.'",pc="Dec 2024")
row(A4,"A4","[F]","Dec 2024/Jan 2025 rules: KLA estimate of CY2025 revenue impact ~$500M +/- $100M, ~70% systems","500 +/- 100","$ million","Q2 FY25","LQ2FY25","p. 11, CY2025 market outlook",
    "impact on KLA’s revenue in calendar 2025 from recent export controls in China to be approximately $500 million, plus or minus $100 million","",
    "Same sentence continues: 'with roughly 70% of the impact affecting our systems business'. First communicated early Dec 2024 (UBS conference, see TrendForce [S]).",pc="Jan-Dec 2025")
row(A4,"A4","[F]","Dec 2024/Jan 2025 rules: KLA cut RPO (backlog) by ~$430M; ~50% was due within 12 months","430","$ million","Q2 FY25","10Q2FY25","Note 2 Revenue (RPO) and Item 2 MD&A",
    "we reduced our RPO by an aggregate of approximately $430 million because we are currently unable to ship the products ordered by affected customers","","")
row(A4,"A4","[S]","CFO at UBS conference (Dec 4, 2024): ~$500M CY2025 impact, 70% systems / 30% services; China revenue to fall ~20% in 2025; China high-20s% of 2025 sales","500","$ million","Q2 FY25","TF","Article body",
    "the curbs would have roughly a USD 500 million incremental impact to the company’s 2025 revenue","",
    "Article also: China revenue 'projected to decline by about 20% year-over-year in 2025'. Actual CY2025 China -9.5% (calc).",pc="Jan-Dec 2025")
row(A4,"A4","[F]","Dec 2024 restrictions hit Services growth in March 2025 quarter","qualitative","qualitative","Q3 FY25","LQ3FY25","p. 3, Services paragraph",
    "Newly announced market access restrictions in early December 2024 from the U.S. government export controls impacted service revenue growth in the March quarter.","","")
row(A4,"A4","[F]","Affiliates Rule IFR effective Sep 29, 2025: Entity List restrictions extended to entities >=50% owned by listed parties","2025-09-29","effective date","Q1 FY26","FR25A","p. 1 (90 FR 47201), DATES and SUMMARY",
    "Effective date: This rule is effective","","Layout text: next line reads 'September 29, 2025.' Summary: 'any entity that is at least 50 percent owned by one or more entities on the Entity List' is covered.",pc="Sep 2025")
row(A4,"A4","[F]","KLA estimate of revenue lost to extended export controls (Affiliates Rule period): ~$300-350M across Dec 2025 quarter and CY2026","300-350","$ million","Q1 FY26","LQ1FY26","p. 9, CY2026 outlook",
    "We estimate the revenue impact on the December quarter and calendar 2026 to be approximately $300 to $350 million for KLA.","",
    "KLA did not name the Affiliates Rule in the letter: 'additional market access loss related to certain customers in China resulting from extended export controls'. Period is Oct 2025-Dec 2026, not FY26.",pc="Oct 2025-Dec 2026")
row(A4,"A4","[S]","CFO: impact on December 2025 quarter fairly immaterial (slots reallocated); ~$300-350M through end of 2026","300-350","$ million","Q1 FY26","TQ1FY26","Q&A (Vivek Arya)",
    "we think that's about $300 million to $350 million between now and the end of 2026","","Also: 'the impact on December is fairly immaterial to the company overall'.",pc="Oct 2025-Dec 2026")
row(A4,"A4","[F]","BIS suspended the Affiliates Rule from Nov 10, 2025 to Nov 9, 2026","2025-11-10 to 2026-11-09","dates","Q2 FY26","FR25S","SUMMARY and DATES",
    "The suspension is set to end November 9, 2026, absent a future extension.","","",pc="Nov 2025-Nov 2026")
row(A4,"A4","[F]","KLA FY26 10-K risk factor records the Affiliates Rule and its one-year suspension","suspended","qualitative","FY26","10KFY26","Item 1A Risk Factors",
    "In November 2025, the BIS suspended the Affiliates Rule for one year until November 2026.","","")
row(A4,"A4","[S]","After the suspension CFO said China would be up in CY2026 vs modestly down expected 3 months earlier; affiliate revenue 'feathered' back into forecast; 'that ballpark' ($300-350M)","up","qualitative","Q2 FY26","TQ2FY26","Q&A (Stacy Rasgon)",
    "three months ago, we thought China would be, you know, modestly down and now I think it's it's going to be up for us.","",
    "Next line: 'So that business has come back in and feathered through within our forecast.' KLA gave no new $ figure for recovered revenue.",pc="Jan-Dec 2026")
row(A4,"A4","[S]","BIS extended the Affiliates Rule suspension to Jan 10, 2027 (final rule published Nov 9, 2026)","2027-01-10","date","Q2 FY27","SPB","Alert body",
    "The final rule extends the suspension of the BIS Affiliates Rule, which was set to expire on November 9, 2026 through January 10, 2027.","",
    "Federal Register text of the Nov 2026 extension NOT RETRIEVED (federalregister.gov returns CAPTCHA; govinfo document number not found).",pc="Nov 2026")
row(A4,"A4","[F]","Q1 FY27 10-Q: no new export-rule risk factor; refers back to FY26 10-K","no change","qualitative","Q1 FY27","10Q1FY27","Part II Item 1A Risk Factors",
    "Other than the risk factor listed below, there have been no material changes in our risk factors since our Annual Report on Form 10-K","",
    "The one changed risk factor concerns IP protection, not export controls. No 2026 SME rule named by KLA.")
# normalisation statements
row(A4,"A4","[S]","CFO (Oct 2025): China share likely settles mid-20s in 2026, partly export restrictions, partly 'general normalization'","mid-20s","% of revenue","Q1 FY26","TQ1FY26","Q&A",
    "some of that is driven by the export restrictions, but also some general normalization that we've been talking about that would be coming","",pc="Jan-Dec 2026")
row(A4,"A4","[S]","CFO (Jan 2026): China mid-to-high 20s % of KLA revenue in 2026; China WFE flattish to slightly up","mid-to-high 20s","% of revenue","Q2 FY26","TQ2FY26","Q&A",
    "we think it'll be somewhere in the mid 20% to high 20% range","",pc="Jan-Dec 2026")
row(A4,"A4","[S]","CFO (Apr 2026): China growth rate expected below overall WFE growth","qualitative","qualitative","Q3 FY26","TQ3FY26","Q&A",
    "I would expect that the China growth rate is probably lower than where the overall WFE growth rate is projected to be here moving forward.","")
row(A4,"A4","[S]","CFO (Oct 2026): China 27-29% of CY2026 revenue; low-20s% in 2027","27-29 (CY26); low 20s (CY27)","% of revenue","Q1 FY27","TQ1FY27","Q&A (Chris Caso)",
    "So we are probably operating somewhere, I would say, in the low 20s percentile in 2027.","",
    "Same answer: 'So, we will call it somewhere between 27% to 29%'.",pc="Jan 2026-Dec 2027")
row(A4,"A4","[S]","CFO: KLA's China total includes non-semi-PC (PCB, component inspection) business that skews the China % up slightly; no separate semi PC systems China share given","qualitative","qualitative","Q1 FY27","TQ1FY27","Q&A (Chris Caso)",
    "Now within our numbers, there is also our non semi PC that also has business in China.","",
    "A 'China share of Semi PC systems' figure: NOT DISCLOSED (read: shareholder letters and slides Q4 FY24-Q1 FY27, Investor Day 2026 slides/transcripts).")

# ---------- A5
row(A5,"A5","[F]","Cash, cash equivalents and marketable securities at Sep 30, 2026 ($4.90B at Jun 30, 2026)","4,741,191","$ thousands","Q1 FY27","10Q1FY27","Item 2 MD&A, Liquidity",
    "As of September 30, 2026, our cash, cash equivalents and marketable securities totaled $4.74 billion","","Cash $1,531,950k + marketable securities $3,209,241k. $785.7M held abroad.")
for q, doc, v in [("Q1 FY26","10Q1FY26","4,683,591"),("Q2 FY26","10Q2FY26","5,207,464"),("Q3 FY26","10Q3FY26","4,957,938"),("Q4 FY26","10Q1FY27","4,902,408")]:
    row(A5,"A5","[F]",f"Cash, cash equivalents and marketable securities, end of {q}", v, "$ thousands", q, doc, "Item 2 MD&A, Liquidity table",
        (f"Total cash, cash equivalents and marketable securities $ 4,741,191 $ {v}" if q=="Q4 FY26" else f"Total cash, cash equivalents and marketable securities $ {v}"),"","Quarter-end balance.")
notes = [("4.100","March 15, 2029","800,000","4.159"),("4.650","July 15, 2032","1,000,000","4.657"),("4.700","February 1, 2034","500,000","4.777"),
         ("5.650","November 1, 2034","250,000","5.670"),("5.000","March 15, 2049","400,000","5.047"),("3.300","March 1, 2050","750,000","3.302"),
         ("4.950","July 15, 2052","1,450,000","5.023"),("5.250","July 15, 2062","800,000","5.259")]
for c, m, p, e in notes:
    sp = " " if m in ("March 15, 2029","March 15, 2049","March 1, 2050") else ""
    row(A5,"A5","[F]",f"Senior unsecured note {c}% due {m}: principal (effective rate {e}%)", p, "$ thousands", "Q1 FY27", "10Q1FY27", "Note 7 Debt",
        f"{c} % Senior Notes due on {m}{sp} $ {p}" if c=="4.100" else f"{c} % Senior Notes due on {m}{sp} {p}", "", "Fixed rate; interest semi-annual.")
row(A5,"A5","[F]","Total senior notes principal; carrying value $5,723,289k after swaps fair value, discount and issuance costs","5,950,000","$ thousands","Q1 FY27","10Q1FY27","Note 7 Debt",
    "Total 5,950,000 5,950,000","","No other borrowings; 10-Q shows long-term debt only (no current portion).")
row(A5,"A5","[F]","Interest-rate swaps on $2.00B of 2022 Senior Notes convert fixed to floating (SOFR)","2.00","$ billion","FY26","10Q1FY27","Note 7 Debt",
    "In fiscal 2026, we entered into interest rate swaps on $2.00 billion principal amount of the senior, unsecured long-term notes issued in June 2022","","Fair value hedge; swaps fair value -$165.6M at Sep 30, 2026.")
row(A5,"A5","[F]","Fair value of senior notes Sep 30, 2026 ($5.48B Jun 30, 2026)","5.08","$ billion","Q1 FY27","10Q1FY27","Note 7 Debt",
    "the fair value of the Senior Notes as of September 30, 2026 and June 30, 2026 was $5.08 billion and $5.48 billion, respectively","","Level 2.")
row(A5,"A5","[F]","Revolving credit facility $1.50B (Credit Agreement Jul 3, 2025, matures Jul 3, 2030, two 1-yr extensions, +$500M accordion); undrawn","1.50","$ billion","Q1 FY27","10Q1FY27","Note 7 Debt, Revolving Credit Facility",
    "As of September 30, 2026, we had no outstanding borrowings under the Revolving Credit Facility.","","Pricing Term SOFR + 62.5-100.0 bps; commitment fee 5.5 bps at Sep 30, 2026.")
row(A5,"A5","[F]","Covenant: maximum net leverage ratio 3.25x (up to 3.75x after material acquisition); in compliance","3.25","x net leverage","Q1 FY27","10Q1FY27","Note 7 Debt",
    "Under the Revolving Credit Facility, the maximum net leverage ratio on a quarterly basis is 3.25 to 1.00","",
    "Indenture covenants limit liens and sale-leasebacks; 101% change-of-control put (with two-agency downgrade). Compliance stated for both.")
row(A5,"A5","[F]","Indenture covenant compliance at Sep 30, 2026","in compliance","qualitative","Q1 FY27","10Q1FY27","Note 7 Debt",
    "As of September 30, 2026, we were in compliance with all of our covenants under the Indenture associated with the Senior Notes.","","")
row(A5,"A5","[F]","$750M senior notes due Nov 1, 2024 repaid; principal fell from $6.70B (Jun 2024) to $5.95B","750","$ million","Q2 FY25","10KFY25","Note 8 Debt",
    "In November 2024, we repaid $ 750.0 million of the Senior Notes that were due on November 1, 2024.","","No new notes issued since Feb 2024 ($500M 4.700% 2034 + $250M add-on 4.950% 2052).")
row(A5,"A5","[F]","Credit ratings Moody's A2, S&P A-, Fitch A- (as of Q1 FY27 slides)","A2 / A- / A-","rating","Q1 FY27","SQ1FY27","p. 7, Strong Investment Grade Balance Sheet",
    "Moody’s A2","","Slide also: weighted average interest rate 4.67% excl. swaps; weighted average maturity 17.8 years.")
for q, doc, v, quote in [("Q2 FY26","10Q2FY26","69,668","Interest expense 69,668 74,981"),("Q3 FY26","10Q3FY26","70,423","Interest expense 70,423 71,889"),
                         ("Q1 FY27","10Q1FY27","67,927","Interest expense 67,927 71,075")]:
    row(A5,"A5","[F]",f"Interest expense, {q}", v, "$ thousands", q, doc, "Condensed Consolidated Statements of Operations", quote, "", "")
row(A5,"A5","[F]","Interest expense FY26 (FY25 $302,166k)","284,440","$ thousands","FY26","10KFY26","Item 7 MD&A, Interest expense table","Interest expense $ 284,440 $ 302,166","","")
row(A5,"A5","[I]","Interest expense Q4 FY26 = FY26 - 9M FY26; LTM (Q2 FY26-Q1 FY27) $281,292k","73,274","$ thousands","Q4 FY26","CALC5","Interest expense block","","High","Inputs: FY26 10-K $284,440k; Q3 FY26 10-Q nine months $211,166k.")
row(A5,"A5","[I]","Principal-weighted coupon 4.629%; principal-weighted effective rate 4.668% (matches slide 4.67%); weighted maturity 17.8 years","4.668","%","Q1 FY27","CALC5","Debt ladder block","","High","Inputs: Note 7 table. Next maturity $800M 4.100% Mar 15, 2029.")
row(A5,"A5","[I]","Net debt at Sep 30, 2026 = $5.95B notes principal - $4.74B cash and securities","1,208,809","$ thousands (net debt)","Q1 FY27","CALC5","Net cash block","","High","Net debt vs carrying value $982,098k. Net debt Q2 FY26 $742.5M, Q3 FY26 $992.1M, Q4 FY26 $1,047.6M.")
row(A5,"A5","[I]","Commercial paper: no programme or borrowing mentioned","NOT DISCLOSED","","Q1 FY27","10Q1FY27","Note 7 Debt; Item 2 Liquidity",
    "","High","NOT DISCLOSED (read: Q1 FY27 10-Q Note 7 and Liquidity; FY26 10-K Note 8, Item 7): no commercial paper programme mentioned.")
row(A5,"A5","[I]","Convertible debt: none; all debt is fixed-rate senior unsecured notes","none","","Q1 FY27","10Q1FY27","Note 7 Debt",
    "","High","Note 7 lists only eight fixed-rate senior notes; the word 'convertible' does not occur in FY26 10-K or Q1 FY27 10-Q.")
# buybacks
row(A5,"A5","[F]","Share repurchases Q1 FY27: 4,914k shares (post-split), $942.9M (trade date)","942,918","$ thousands","Q1 FY27","10Q1FY27","Note 10 Stock Repurchase Program",
    "Number of shares of common stock repurchased 4,914 6,225 Total cost of repurchases $ 942,918 $ 564,400","","Cash-basis repurchases $935.8M (MD&A). Q1 FY26 comparative restated post-split 6,225k.")
row(A5,"A5","[F]","Share repurchases Q1 FY26: 623k shares (pre-split), $564.4M","564,400","$ thousands","Q1 FY26","10Q1FY26","Note 10",
    "Number of shares of common stock repurchased 623 740 Total cost of repurchases $ 564,400 $ 570,936","","Pre-split share count.")
row(A5,"A5","[F]","Share repurchases Q2 FY26: 460k shares (pre-split), $537.6M","537,553","$ thousands","Q2 FY26","10Q2FY26","Note 10",
    "Number of shares of common stock repurchased 460 979 1,083 1,719 Total cost of repurchases $ 537,553","","Pre-split share count.")
row(A5,"A5","[F]","Share repurchases Q3 FY26: 440k shares (pre-split), $631.9M; 9M FY26 1,523k shares, $1,733.9M","631,913","$ thousands","Q3 FY26","10Q3FY26","Note 10",
    "Number of shares of common stock repurchased 440 711 1,523 2,430 Total cost of repurchases $ 631,913 $ 511,703 $ 1,733,866","","Pre-split share count.")
row(A5,"A5","[F]","Share repurchases FY26: 18,241k shares (post-split), $2,303.9M","2,303,935","$ thousands","FY26","10KFY26","Note 10 Stock Repurchase Program",
    "Number of shares of common stock repurchased 18,241 30,057 30,320 Total cost of repurchases $ 2,303,935","","Post-split (retroactive) share counts.")
row(A5,"A5","[I]","Share repurchases Q4 FY26 (FY26 minus 9M): 3,011k shares post-split, $570.1M","570,069","$ thousands","Q4 FY26","CALC5","Buybacks block","","High","Shares = 18,241k - 1,523k x10.")
row(A5,"A5","[I]","Share repurchases last 4 quarters (Q2 FY26-Q1 FY27): 16,925k post-split shares, $2,682.5M","2,682,453","$ thousands","Q2 FY26-Q1 FY27","CALC5","Buybacks block","","High","Pre-split counts x10.",pc="Oct 2025-Sep 2026")
row(A5,"A5","[F]","Remaining repurchase authorisation at Sep 30, 2026","8.81","$ billion","Q1 FY27","10Q1FY27","Part II Item 2",
    "As of September 30, 2026, $8.81 billion remained available for repurchases under our repurchase program.","","Prior: $9.74B Jun 30, 2026; $10.31B Mar 31, 2026; $3.94B Dec 31, 2025; $4.47B Sep 30, 2025; $5.03B Jun 30, 2025.")
row(A5,"A5","[F]","Board authorisations: +$5.00B in Q4 FY25 and +$7.00B in Q3 FY26","5.00; 7.00","$ billion","FY25-FY26","10KFY26","Note 10 Stock Repurchase Program",
    "$ 5.00 billion in the fourth quarter of fiscal 2025 and $ 7.00 billion in the third quarter of fiscal 2026","",
    "$5B announced Apr 30, 2025 (Q4 FY25 letter); $7B announced with Q3 FY26 results Apr 29, 2026 though booked in Q3 FY26 (Jan-Mar 2026). Earlier: +$2B announced Sep 5, 2023 (Q1 FY24 release).",pc="Apr 2025-Mar 2026")
row(A5,"A5","[F]","Q3 FY26 release: dividend raised to $2.30/qtr (pre-split) and additional $7B buyback","2.30","$ per share per quarter (pre-split)","Q3 FY26","RQ3FY26","p. 1, highlights",
    "The Board of Directors approved an increase to the quarterly dividend level to $2.30 per share","","Dividend from May 2026 declaration; = $0.23 post-split.")
row(A5,"A5","[F]","Apr 30, 2025: dividend raised 12% to $1.90/qtr (pre-split) and new $5B authorisation","1.90","$ per share per quarter (pre-split)","Q4 FY25","LQ4FY25","p. 6, capital returns",
    "we also announced a new $5 billion share repurchase authorization.","","Same paragraph: '16th consecutive annual dividend increase, up 12% to $1.90 per share per quarter'.")
row(A5,"A5","[F]","Q1 FY27 dividend declared $0.230 per share (post-split), paid Sep 1, 2026; dividends paid $305.1M","0.230","$ per share (post-split)","Q1 FY27","10Q1FY27","Item 2 MD&A, Cash Dividends",
    "declared a regular quarterly cash dividend of $0.230 per share on our outstanding common stock, which was paid on September 1, 2026","","")
row(A5,"A5","[I]","Buyback authorisation roll-forward reconciles to reported remaining within rounding ($10M) each quarter Q1 FY26-Q1 FY27","<= $12.9M gap","$ thousands","Q1 FY26-Q1 FY27","CALC5","Authorisation roll-forward block","","Medium","Largest gap Q1 FY27 $12.9M (trade vs settlement timing or excise tax likely; not stated).",pc="Jul 2025-Sep 2026")
# split
row(A5,"A5","[F]","10-for-1 stock split effected June 11, 2026; 10-Q share and per-share data retroactively adjusted","10:1","ratio","Q4 FY26","10Q1FY27","Note 1 Basis of Presentation",
    "Share and per share information throughout this Quarterly Report on Form 10-Q have been retroactively adjusted to reflect the stock split.","","Split FAQ: first split-adjusted trading Jun 12, 2026. 10-Qs dated before June 2026 show pre-split counts.")
row(A5,"A5","[F]","Shares outstanding Oct 26, 2026 (post-split)","1,302,962,435","shares","Q1 FY27","10Q1FY27","Cover page",
    "As of October 26, 2026, there were 1,302,962,435 shares of the registrant’s Common Stock","","Apr 27, 2026: 130,627,521 pre-split (Q3 FY26 10-Q cover).")
row(A5,"A5","[I]","Share count change Apr 27, 2026 (x10) to Oct 26, 2026","-0.25","%","Q4 FY26-Q1 FY27","CALC5","Share count block","","High","1,302,962,435 vs 1,306,275,210.",pc="Apr-Oct 2026")
# M&A and impairments
row(A5,"A5","[F]","Anchor Semiconductor acquired Jul 1, 2021 for $81.7M (+ up to $35M contingent)","81.7","$ million","Q1 FY22","10KFY23","Note 6 Business Combinations and Dispositions",
    "On July 1, 2021, we acquired Anchor Semiconductor Inc., a privately held company, primarily to expand our products and services offerings","","Same sentence: 'total purchase consideration of $ 81.7 million'.",pc="Jul 2021")
row(A5,"A5","[F]","ECI Technology acquired Feb 28, 2022 for $431.5M cash; $266.4M goodwill, $208.4M intangibles","431.5","$ million","Q3 FY22","10KFY24","Note 6 Business Combinations and Dispositions",
    "for aggregate purchase consideration of $ 431.5 million, paid in cash","","",pc="Feb 2022")
row(A5,"A5","[F]","Private company acquired May 1, 2022 for $8.6M","8.6","$ million","Q4 FY22","10KFY24","Note 6",
    "On May 1, 2022, we acquired the outstanding shares of a privately held company for total purchase consideration of $ 8.6 million, paid in cash.","",pc="May 2022")
row(A5,"A5","[F]","Private materials-supply company acquired Aug 9, 2022 for $32.7M; Orbograph sold Aug 11, 2022 for $110.0M (gain $29.7M)","32.7","$ million","Q1 FY23","10KFY25","Note 6 Business Combinations and Dispositions",
    "primarily to secure the supply of materials for existing products, for aggregate purchase consideration of $ 32.7 million payable in cash","",
    "No business acquisitions FY25, FY26, Q1 FY27 (cash-flow line 'Business acquisitions, net of cash acquired' nil in FY25-FY26; $3.7M in FY24 = holdback).",pc="Aug 2022")
row(A5,"A5","[F]","Q2 FY24 goodwill and intangibles impairment, PCB and Display reporting unit","219.0","$ million","Q2 FY24","10KFY24","Item 7 MD&A, Impairment of Goodwill and Purchased Intangible Assets",
    "we recorded a $219.0 million goodwill and purchased intangible asset impairment charge for the PCB and Display reporting unit","","Goodwill $192.6M + intangibles $26.4M.")
row(A5,"A5","[F]","Q3 FY24 Display goodwill impairment after March 2024 exit decision","70.5","$ million","Q3 FY24","10KFY24","Item 7 MD&A",
    "we recorded a $70.5 million goodwill impairment charge and an immaterial amount of purchased intangible assets were abandoned in the third quarter of fiscal 2024","","")
row(A5,"A5","[F]","Display exit: planned end of manufacturing of most Display products by Dec 31, 2024; services continue","2024-12-31","planned date","Q3 FY24","10KFY24","Item 1 Business",
    "announcing the end of manufacturing of most Display products by December 31, 2024","","Actual completion date not stated in later filings; FY26 10-K: 'absence of revenue from our Display business following our exit'.")
row(A5,"A5","[F]","Display exit was triggered by a major Display customer cancelling a technology project; settlement received Q2 FY25","qualitative","qualitative","Q2 FY25","10KFY25","Item 7 MD&A, segment revenue",
    "cancellation of a technology project by a major Display customer that resulted in our decision to exit the Display business","","Settlement amount NOT DISCLOSED (read: FY25 10-K Item 7).")
row(A5,"A5","[F]","Q2 FY25 PCB goodwill and intangibles impairment (PCB and Component Inspection segment)","239.1","$ million","Q2 FY25","10KFY26","Item 7 MD&A",
    "which resulted in a $239.1 million goodwill and purchased intangible assets impairment charge in the PCB and Component Inspection reportable segment","","Goodwill $230.4M + intangibles $8.7M.")
row(A5,"A5","[F]","FY26 annual goodwill test (Dec 31, 2025): no impairment","none","qualitative","Q2 FY26","10KFY26","Note 6 Goodwill and Purchased Intangible Assets",
    "We performed the required annual goodwill impairment test as of December 31, 2025 and concluded that goodwill was not impaired.","","Goodwill $1,788.8M at Jun 30, 2026.")

hdr = ["id","tag","claim","value","unit","period_fiscal","period_calendar","document","date","page_or_section","url","local_file","quote","confidence","note"]
for name, rows_ in [("A4", A4), ("A5", A5)]:
    with open(os.path.join(ROOT, f"research/out/kla/parts/{name}.csv"), "w", newline="") as f:
        w = csv.writer(f); w.writerow(hdr); w.writerows(rows_)
    print(name, len(rows_), {t: sum(r[1]==t for r in rows_) for t in ["[F]","[C]","[S]","[I]"]})
