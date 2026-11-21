#!/usr/bin/env python3
"""Builds research/out/comet/parts/A.csv (Module A, group level, Comet Holding AG).
Each row is written with the csv module. Page numbers are located automatically with the same
normalisation that research/tools/quote_check.py uses; HTML sources get a section label.
Rows are keyed; [I] rows list the ids of their inputs (resolved from keys).
Run: python3 -I research/out/comet/calc/A_build_evidence.py
"""
import csv, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
SRC = "research/sources/comet/"
F = {  # key: (file stem, document label)
    "H126": ("2026-07-30_comet_half-year-report-H1-2026.pdf", "Half-Year Report 2026"),
    "P126": ("2026-07-30_comet_results-presentation-H1-2026.pdf", "H1 2026 results presentation"),
    "PR126": ("2026-07_comet_press-release-H1-2026-results.html", "Press release H1 2026 results"),
    "Q326": ("2026-10_comet_press-release-Q3-2026-trading-update.html", "Trading update Q3 2026"),
    "Q126": ("2026-04_comet_press-release-Q1-2026-trading-update.html", "Trading update Q1 2026"),
    "AR25": ("2026-03-05_comet_annual-report-FY2025.pdf", "Annual Report 2025"),
    "P25": ("2026-03-06_comet_results-presentation-FY2025.pdf", "FY2025 results presentation"),
    "PR25": ("2026-03_comet_press-release-FY2025-results.html", "Press release FY2025 results"),
    "CMDPR": ("2025-11_comet_press-release-CMD-2025.html", "Press release Capital Markets Day 2025"),
    "Q325": ("2025-10_comet_press-release-Q3-2025-trading-update.html", "Trading update Q3 2025"),
    "H125": ("2025-07-30_comet_half-year-report-H1-2025.pdf", "Half-Year Report 2025"),
    "PRH125": ("2025-07_comet_press-release-H1-2025-results.html", "Press release H1 2025 results"),
    "Q125": ("2025-04_comet_press-release-Q1-2025-trading-update.html", "Trading update Q1 2025"),
    "PR24": ("2025-03_comet_press-release-FY2024-results.html", "Press release FY2024 results"),
    "Q424": ("2025-01_comet_press-release-Q4-2024-trading-update.html", "Trading update Q4 2024 (preliminary FY2024)"),
    "AR24": ("2025-03-05_comet_annual-report-FY2024.pdf", "Annual Report 2024"),
    "P24": ("2025-03-05_comet_results-presentation-FY2024.pdf", "FY2024 results presentation"),
    "Q324": ("2024-10-18_webdisclosure_newswire-Comet-Q3-2024-trading-update.html", "Trading update Q3 2024 (WebDisclosure newswire copy)"),
    "H124": ("2024-07-30_comet_half-year-report-H1-2024.pdf", "Half-Year Report 2024"),
    "Q124": ("2024-04_webdisclosure_newswire-Comet-Q1-2024-trading-update.html", "Trading update Q1 2024 (WebDisclosure newswire copy)"),
    "AR23": ("2024-03-03_comet_annual-report-FY2023.pdf", "Annual Report 2023"),
    "P23": ("2024-03-03_comet_results-presentation-FY2023.pdf", "FY2023 results presentation"),
    "CMD23": ("2023-11-08_comet_capital-markets-day-2023.pdf", "Capital Markets Day 2023 presentation"),
    "Q323": ("2023-10-19_webdisclosure_newswire-Comet-Q3-2023-trading-update.html", "Trading update Q3 2023 (WebDisclosure newswire copy)"),
    "H123": ("2023-07-27_comet_half-year-report-H1-2023.pdf", "Half-Year Report 2023"),
    "Q123": ("2023-04-14_webdisclosure_newswire-Comet-Q1-2023-trading-update.html", "Trading update Q1 2023 (WebDisclosure newswire copy)"),
    "AR22": ("2023-03-01_comet_annual-report-FY2022.pdf", "Annual Report 2022"),
    "P22": ("2023-03-01_comet_results-presentation-FY2022.pdf", "FY2022 results presentation"),
    "Q322": ("2022-10-20_boerse-online_newswire-Comet-Q3-2022-trading-update-DE.html", "Trading update Q3 2022 (German dpa-AFX/EQS newswire copy)"),
    "H122": ("2022-07-27_comet_half-year-report-H1-2022.pdf", "Half-Year Report 2022"),
    "P21": ("2022-03-03_comet_results-presentation-FY2021.pdf", "FY2021 results presentation"),
    "AR21": ("2022-03-03_comet_annual-report-FY2021.pdf", "Annual Report 2021"),
    "H121": ("2021-08-11_comet_half-year-report-H1-2021.pdf", "Half-Year Report 2021"),
    "H120": ("2020-08-13_comet_half-year-report-H1-2020.pdf", "Half-Year Report 2020"),
    "P19": ("2020-03-19_comet_results-presentation-FY2019.pdf", "FY2019 results presentation"),
    "H119": ("2019-08-14_comet_half-year-report-H1-2019.pdf", "Half-Year Report 2019"),
    "H118": ("2018-08-15_comet_half-year-report-H1-2018.pdf", "Half-Year Report 2018"),
    "XPPR": ("2026-07_comet_press-release-XP-Power-appeal.html", "Press release XP Power appeal decision"),
    "BOND": ("2026-11-21_comet_press-release-bond-2026.html", "Web page 'Bond' (comet.tech)"),
}
NEWSWIRE = {"Q324", "Q124", "Q323", "Q123", "Q322"}

# ---------------------------------------------------------------------------------------------
# rows: (key, tag, claim, value, unit, period_fiscal, period_calendar, filekey, quote, confidence, note)
R = []
def r(*a):
    R.append(a)

# ===================== A1 results =====================
r("h126_is_sales", "[F]", "Consolidated net sales H1 2026 vs H1 2025 (income statement)", "239,834 / 227,154", "CHF k", "H1 FY2026; H1 FY2025", "Jan-Jun 2026; Jan-Jun 2025", "H126",
  "Net sales 239,834 227,154", "High", "")
r("h126_gp", "[F]", "Gross profit H1 2026 vs H1 2025 restated", "99,362 / 89,755", "CHF k", "H1 FY2026; H1 FY2025", "Jan-Jun 2026; Jan-Jun 2025", "H126",
  "Gross profit 99,362 89,755", "High", "H1 2025 restated (note 01.1)")
r("h126_ebit", "[F]", "Operating income (EBIT) H1 2026 vs H1 2025 restated", "20,391 / 12,245", "CHF k", "H1 FY2026; H1 FY2025", "Jan-Jun 2026; Jan-Jun 2025", "H126",
  "Operating income 20,391 12,245", "High", "")
r("h126_ebitda", "[F]", "EBITDA H1 2026 vs H1 2025 restated", "31,367 / 22,978", "CHF k", "H1 FY2026; H1 FY2025", "Jan-Jun 2026; Jan-Jun 2025", "H126",
  "EBITDA 31,367 22,978", "High", "Comet EBITDA = operating income before D&A and impairment")
r("h126_oneoff", "[F]", "H1 2026 EBITDA includes one-time costs (Penang ramp-up and efficiency program) named by management", "4.5", "CHF m", "H1 FY2026", "Jan-Jun 2026", "H126",
  "The EBITDA includes one-time costs of CHF 4.5 million related to the ramp", "High", "one-off named by management")
r("h126_gm", "[F]", "Gross profit margin H1 2026 vs H1 2025 restated (deck)", "41.4% (HY25: 39.5%)", "%", "H1 FY2026", "Jan-Jun 2026", "P126",
  "239.8 41.4% 31.4", "High", "")
r("h126_fcf", "[F]", "Free cash flow (OCF + investing CF) H1 2026 vs H1 2025", "-19,306 / 1,344", "CHF k", "H1 FY2026; H1 FY2025", "Jan-Jun 2026; Jan-Jun 2025", "H126",
  "Free cash flow (19,306) 1,344", "High", "")
r("h126_capex", "[F]", "Capex H1 2026 vs H1 2025 (Penang building, inventory build)", "29.4 (H1 2025: 12.1)", "CHF m", "H1 FY2026", "Jan-Jun 2026", "H126",
  "reflecting capital expenditures of CHF 29.4 million (H1/25 CHF 12.1 million)", "High", "")
r("h126_sbc", "[F]", "Share-based payments (cash-flow add-back) H1 2026 vs H1 2025", "666 / 370", "CHF k", "H1 FY2026; H1 FY2025", "Jan-Jun 2026; Jan-Jun 2025", "H126",
  "Share-based payments 666 370", "High", "")
r("ar25_is_sales", "[F]", "Net sales FY2025 vs FY2024", "457,044 / 445,362", "CHF k", "FY2025; FY2024", "Jan-Dec 2025; Jan-Dec 2024", "AR25",
  "Net sales 3 457,044 445,362", "High", "")
r("ar25_gp", "[F]", "Gross profit and gross margin FY2025 vs FY2024 restated", "173,677 (38.0%) / 190,731 (42.8%)", "CHF k", "FY2025; FY2024", "Jan-Dec 2025; Jan-Dec 2024", "AR25",
  "Gross profit 173,677 38.0% 190,731 42.8%", "High", "")
r("ar25_ebit", "[F]", "Operating income FY2025 vs FY2024 restated", "24,556 (5.4%) / 35,861 (8.1%)", "CHF k", "FY2025; FY2024", "Jan-Dec 2025; Jan-Dec 2024", "AR25",
  "Operating income 24,556 5.4% 35,861 8.1%", "High", "")
r("ar25is_ebitda", "[F]", "EBITDA and margin FY2025 vs FY2024 restated", "46,335 (10.1%) / 58,011 (13.0%)", "CHF k", "FY2025; FY2024", "Jan-Dec 2025; Jan-Dec 2024", "AR25",
  "EBITDA 46,335 10.1% 58,011 13.0%", "High", "")
r("ar25_ocf", "[F]", "Net cash from operating activities FY2025 vs FY2024", "48,217 / 49,963", "CHF k", "FY2025; FY2024", "Jan-Dec 2025; Jan-Dec 2024", "AR25",
  "Net cash provided by operating activities 48,217 49,963", "High", "")
r("ar25_icf", "[F]", "Net cash used in investing activities FY2025 vs FY2024", "-39,715 / -8,549", "CHF k", "FY2025; FY2024", "Jan-Dec 2025; Jan-Dec 2024", "AR25",
  "Net cash (used in) investing activities (39,715) (8,549)", "High", "")
r("ar25five", "[F]", "Five-year FCF: 2025, 2024, 2023, 2022, 2021", "8,502 / 41,414 / (584) / 42,173 / 57,767", "CHF k", "FY2025-FY2021", "Jan-Dec 2021-2025", "AR25",
  "Free cash flow 1 8,502 41,414 (584) 42,173 57,767", "High", "2024 restated")
r("ar25five_sales", "[F]", "Five-year net sales 2025, 2024, 2023, 2022, 2021", "457,044 / 445,362 / 397,453 / 586,395 / 513,721", "CHF k", "FY2025-FY2021", "Jan-Dec 2021-2025", "AR25",
  "Net sales 457,044 445,362 397,453 586,395 513,721", "High", "")
r("ar25five_ebitda", "[F]", "Five-year EBITDA 2025, 2024, 2023, 2022, 2021", "46,335 / 58,011 / 44,996 / 118,913 / 102,749", "CHF k", "FY2025-FY2021", "Jan-Dec 2021-2025", "AR25",
  "EBITDA 46,335 58,011 44,996 118,913 102,749", "High", "")
r("ar25five_margin", "[F]", "Five-year EBITDA margin 2025, 2024, 2023, 2022, 2021", "10.1% / 13.0% / 11.3% / 20.3% / 20.0%", "%", "FY2025-FY2021", "Jan-Dec 2021-2025", "AR25",
  "In % of net sales 10.1% 13.0% 11.3% 20.3% 20.0%", "High", "")
r("ar25_sbc", "[F]", "Share-based payments (cash-flow add-back) FY2025 vs FY2024", "1,415 / 1,034", "CHF k", "FY2025; FY2024", "Jan-Dec 2025; Jan-Dec 2024", "AR25",
  "Share-based payments 30 1,415 1,034", "High", "")
r("ar25_sbc_note", "[F]", "Share-based payment expense is for Executive Committee and Board only (no broad employee plan disclosed)", "1.4 (prior year 1.0); Board 0.4", "CHF m", "FY2025", "Jan-Dec 2025", "AR25",
  "The expenses recognized for share-based payments to the Executive Committee and Board of Directors", "High", "")
r("ar25_fire", "[F]", "Other operating income FY2025 includes insurance recoveries for a Q4 2025 fire at Flamatt (one-off named in notes)", "2.1", "CHF m", "FY2025 (Q4)", "Oct-Dec 2025", "AR25",
  "included insurance recoveries of approximately CHF 2.1 million", "High", "fixed assets of CHF 0.3m impaired (below EBITDA)")
r("ar25_restate_is", "[F]", "FY2024 EBITDA restated for prior-period errors: as reported / adjustment / restated", "60,380 / -2,369 / 58,011", "CHF k", "FY2024", "Jan-Dec 2024", "AR25",
  "EBITDA 60,380 (2,369) 58,011", "High", "AR 2025 note 2.3")
r("ar25_restate_gp", "[F]", "FY2024 gross profit restated: as reported / adjustment / restated", "193,100 / -2,369 / 190,731", "CHF k", "FY2024", "Jan-Dec 2024", "AR25",
  "Gross profit 193,100 (2,369) 190,731", "High", "")
r("h126_restate_ebitda", "[F]", "H1 2025 EBITDA restated in H1 2026 report: as first reported / adjustment / restated", "20,708 / +2,270 / 22,978", "CHF k", "H1 FY2025", "Jan-Jun 2025", "H126",
  "EBITDA 20,708 2,270 22,978", "High", "note 01.1")
r("h126_restate_cogs", "[F]", "H1 2025 cost of sales restated (write-down booked in H1 2025 moved back to FY2024)", "-139,669 / +2,270 / -137,399", "CHF k", "H1 FY2025", "Jan-Jun 2025", "H126",
  "Cost of sales (139,669) 2,270 (137,399)", "High", "")
r("h126_restate_why1", "[F]", "Restatement cause 1: inventory items excluded from YE2024 write-down assessment (manual reversal of a write-off)", "2.1", "CHF m", "FY2024", "Dec 2024", "H126",
  "stock items totaling CHF 2.1 million were erroneously excluded", "High", "")
r("h126_restate_why2", "[F]", "Restatement cause 2: expenses and liabilities not recognised at YE2024", "0.3", "CHF m", "FY2024", "Dec 2024", "H126",
  "expenses and related liabilities totaling CHF 0.3", "High", "")
r("h126_restate_carry", "[F]", "Company explanation why H1 2025 comparatives changed: effects of FY2024 errors carried into FY2025", "", "", "H1 FY2025", "Jan-Jun 2025", "H126",
  "As the effects of these errors also carried forward into fiscal year 2025", "High", "")
r("h125_orig", "[F]", "H1 2025 as first reported: EBITDA 20.7m, margin 9.1%", "9.1%", "%", "H1 FY2025", "Jan-Jun 2025", "PRH125",
  "margin of 9.1%, compared to 6.9% in HY24", "High", "superseded by restated 10.1%")
r("p25_h2", "[F]", "FY2025 deck shows H1/25 9.1% and H2/25 11.1% EBITDA margin (H1 not restated in this slide)", "9.1% / 11.1% / 10.1%", "%", "H1, H2, FY2025", "Jan-Jun, Jul-Dec, Jan-Dec 2025", "P25",
  "EBITDA margin 9.1% 11.1% 10.1%", "High", "see [I] on consistent basis")
r("pr25_why", "[C]", "Management explanation of FY2025 EBITDA decline: weaker USD vs CHF and unfavourable regional/product mix", "", "", "FY2025", "Jan-Dec 2025", "PR25",
  "EBITDA declined year on year, primarily due to the weaker U.S. dollar against the Swiss franc", "High", "")
r("ar25_fx", "[F]", "FX reduced FY2025 group net sales", "20.8 (4.7%)", "CHF m", "FY2025", "Jan-Dec 2025", "AR25",
  "reduced Group net sales by a total of CHF 20.8", "High", "")
r("ar25_seg", "[F]", "Net sales by division FY2025 (PCT / IXS / IXM total incl. intersegment)", "257,102 / 110,816 / 99,078", "CHF k", "FY2025", "Jan-Dec 2025", "AR25",
  "Total net sales 257,102 110,816 99,078 (9,953) — 457,044", "High", "segment detail: DV agent")
r("h126_seg", "[F]", "Net sales by division H1 2026 (PCT / IXS / IXM total incl. intersegment)", "143,570 / 48,739 / 53,539", "CHF k", "H1 FY2026", "Jan-Jun 2026", "H126",
  "Total net sales 143,570 48,739 53,539 (6,014) - 239,834", "High", "segment detail: DV agent")
r("ar25_semi", "[F]", "PCT net sales to 'Semiconductor' market sector FY2025 vs FY2024 (company sector split)", "241,522 / 226,719", "CHF k", "FY2025; FY2024", "Jan-Dec 2025; Jan-Dec 2024", "AR25",
  "Semiconductor 241,522 226,719", "High", "the only group sector line named 'Semiconductor'")
r("ar25_elec", "[F]", "IXS net sales to 'Electronics' sector FY2025 vs FY2024", "39,942 / 47,702", "CHF k", "FY2025; FY2024", "Jan-Dec 2025; Jan-Dec 2024", "AR25",
  "Electronics 39,942 47,702", "High", "includes semiconductor/advanced-packaging inspection but not separated")
r("cmd23_semi", "[C]", "Company-stated share of group net sales 'into semi' (Semi / Electronics) FY2022 and target at next cycle peak", "57% FY2022; >80% target", "%", "FY2022", "Jan-Dec 2022", "CMD23",
  "57% FY22 net sales", "Medium", "definition: 'Semi / Electronics' end markets; no AI/HBM/advanced-packaging share disclosed")
r("pr126_ai", "[C]", "H1 2026: AI infrastructure, Advanced Packaging and leading-edge grew fastest (qualitative only)", "", "", "H1 FY2026", "Jan-Jun 2026", "PR126",
  "AI infrastructure, Advanced Packaging, and leading-edge technologies experienced accelerated growth", "High", "")
r("pr126_q2", "[F]", "Q2 2026 net sales and Q1 2026 net sales", "133.5 / 106.3", "CHF m", "Q2 FY2026; Q1 FY2026", "Apr-Jun 2026; Jan-Mar 2026", "PR126",
  "In the second quarter, net sales reached CHF 133.5 million", "High", "")
r("q326_sales", "[F]", "Q3 2026 net sales vs Q3 2025 (+51.9%, +49.9% cc)", "155.6 / 102.5", "CHF m", "Q3 FY2026", "Jul-Sep 2026", "Q326",
  "Net sales of CHF 155.6 million in Q3/26 (Q3/25: CHF 102.5 million), +51.9%", "High", "")
r("q326_9m", "[F]", "9M 2026 net sales vs 9M 2025 (+20.0%)", "395.5 / 329.6", "CHF m", "9M FY2026", "Jan-Sep 2026", "Q326",
  "155.6 102.5 +51.9% (+49.9%) 395.5 329.6", "High", "")
r("q126_sales", "[F]", "Q1 2026 net sales vs Q1 2025 (-4.5%, +5.8% cc)", "106.3 / 111.2", "CHF m", "Q1 FY2026", "Jan-Mar 2026", "Q126",
  "Net sales of CHF 106.3 million in Q1/26 (Q1/25: CHF 111.2 million)", "High", "")
r("q325_sales", "[F]", "Q3 2025 net sales vs Q3 2024 (-9.4%)", "102.5 / 113.2", "CHF m", "Q3 FY2025", "Jul-Sep 2025", "Q325",
  "Net sales of CHF 102.5 million in Q3/25 (Q3/24: CHF 113.2 million)", "High", "")
r("q325_9m", "[F]", "9M 2025 net sales", "329.6", "CHF m", "9M FY2025", "Jan-Sep 2025", "Q325",
  "Comet recorded net sales of CHF 329.6 million", "High", "")
r("q125_sales", "[F]", "Q1 2025 net sales vs Q1 2024", "111.2 / 80.9", "CHF m", "Q1 FY2025", "Jan-Mar 2025", "Q125",
  "Net sales of CHF 111.2 million in Q1/25 (Q1/24: CHF 80.9 million)", "High", "")

# ===================== A2 leading signals =====================
r("h126_orders", "[F]", "Incoming orders H1 2026 vs H1 2025 (book-to-bill 1.48 vs 0.98)", "354,843 / 222,947", "CHF k", "H1 FY2026; H1 FY2025", "Jan-Jun 2026; Jan-Jun 2025", "H126",
  "Incoming orders 354,843 222,947", "High", "")
r("h126_b2b", "[F]", "Book-to-bill H1 2026 vs H1 2025", "1.48 / 0.98", "ratio", "H1 FY2026", "Jan-Jun 2026", "H126",
  "Book-to-bill ratio 1.48 0.98", "High", "")
r("h126_q1b2b", "[F]", "Book-to-bill Q1 2026 (ytd 3M) as restated precision in H1 report", "1.36", "ratio", "Q1 FY2026", "Jan-Mar 2026", "H126",
  "(Q1/26 ytd 3M: 1.36)", "High", "trading update had said 1.4")
r("q126_orders", "[F]", "Order intake Q1 2026 vs Q4 2025 and Q1 2025", "144.9 / 129.9 / 118.5", "CHF m", "Q1 FY2026; Q4 FY2025", "Jan-Mar 2026; Oct-Dec 2025", "Q126",
  "Order intake reached CHF 144.9 million, compared to CHF 129.9 million in Q4/25", "High", "")
r("q326_orders", "[F]", "Incoming orders Q3 2026 vs Q3 2025", "275.6 / 102.1", "CHF m", "Q3 FY2026", "Jul-Sep 2026", "Q326",
  "Incoming orders: CHF 275.6 million in Q3/26 (Q3/25: CHF 102.1 million)", "High", "")
r("q326_b2b", "[F]", "Book-to-bill Q3 2026", "1.77", "ratio", "Q3 FY2026", "Jul-Sep 2026", "Q326",
  "Book-to-bill of 1.77 in Q3/26", "High", "")
r("q326_backlog", "[C]", "Order book: significant share scheduled for delivery well into 2027 (backlog CHF amount not given)", "", "", "Q3 FY2026", "Sep 2026", "Q326",
  "a significant share of our order book already scheduled for delivery well into 2027", "High", "")
r("q325_orders", "[F]", "Incoming orders 9M 2025 and book-to-bill 0.98 YTD", "327.4", "CHF m", "9M FY2025", "Jan-Sep 2025", "Q325",
  "Incoming orders of CHF 327.4 million YTD September", "High", "")
r("q125_orders", "[F]", "Incoming orders Q1 2025 vs Q1 2024", "118.5 / 91.0", "CHF m", "Q1 FY2025", "Jan-Mar 2025", "Q125",
  "Incoming orders of CHF 118.5 million in Q1/25 (Q1/24: 91.0 million)", "High", "")
r("h125_orders", "[F]", "Incoming orders H1 2025 vs H1 2024", "222,947 / 207,562", "CHF k", "H1 FY2025", "Jan-Jun 2025", "H125",
  "Incoming orders 222,947 207,562", "High", "")
r("h124_orders", "[F]", "Incoming orders H1 2024 vs H1 2023", "207,562 / 170,311", "CHF k", "H1 FY2024", "Jan-Jun 2024", "H124",
  "Incoming orders 207,562 170,311", "High", "")
r("h123_orders", "[F]", "Incoming orders H1 2023 vs H1 2022; book-to-bill 0.82 vs 1.23", "170,311 / 329,556", "CHF k", "H1 FY2023", "Jan-Jun 2023", "H123",
  "Incoming orders 170,311 329,556", "High", "")
r("q124_b2b", "[S]", "Book-to-bill Q1 2024 as first stated", "1.09", "ratio", "Q1 FY2024", "Jan-Mar 2024", "Q124",
  "Book-to-bill of 1.09 at the end of Q1/24", "Medium", "newswire copy of company release; comet.tech page not retrievable")
r("q424_b2b", "[F]", "Book-to-bill at year-end 2024 (preliminary)", "1.0", "ratio", "FY2024", "Jan-Dec 2024", "Q424",
  "Book-to-bill of 1.0 at year-end 2024", "High", "")
r("p22_b2b", "[F]", "Book-to-bill at year-end 2022", "0.92", "ratio", "FY2022", "Jan-Dec 2022", "P22",
  "book-to-bill of 0.92", "High", "")
r("ar25_backlog", "[F]", "Order backlog (unsatisfied performance obligations) YE2025 vs YE2024", "125.4 / 140.7", "CHF m", "FY2025", "31 Dec 2025", "AR25",
  "CHF 125.4 million (prior year: CHF 140.7 million)", "High", "expected to be realised generally within 12 months")
r("ar24_backlog", "[F]", "Order backlog YE2024 vs YE2023", "141 / 131", "CHF m", "FY2024", "31 Dec 2024", "AR24",
  "amounted to CHF 141 million (prior year: CHF 131 million)", "High", "")
r("ar23_backlog", "[F]", "Order backlog YE2023 vs YE2022", "131 / 200", "CHF m", "FY2023", "31 Dec 2023", "AR23",
  "amounted to CHF 131 million (prior year: CHF 200 million)", "High", "")
r("ar21_backlog", "[F]", "Order backlog YE2021 vs YE2020", "255 / 166", "CHF m", "FY2021", "31 Dec 2021", "AR21",
  "amounted to CHF 255 million (prior year: CHF 166 million)", "High", "")
r("p19_backlog", "[F]", "Order backlog YE2019 vs YE2018", "137.4 / 113.9", "CHF m", "FY2019", "31 Dec 2019", "P19",
  "Order backlog 137.4 113.9 23.5 20.6%", "High", "")
r("p19_orders", "[F]", "New orders FY2019 vs FY2018", "402.3 / 436.5", "CHF m", "FY2019", "Jan-Dec 2019", "P19",
  "New orders 402.3 436.5 -34.2 -7.8%", "High", "")
r("ar25_inv_raw", "[F]", "Inventories: raw materials and semi-finished YE2025 vs YE2024 restated", "57,942 / 63,409", "CHF k", "FY2025", "31 Dec 2025", "AR25",
  "Raw materials and semi-finished products 57,942 63,409", "High", "")
r("ar25_inv_wip", "[F]", "Inventories: work in process YE2025 vs YE2024", "11,877 / 13,469", "CHF k", "FY2025", "31 Dec 2025", "AR25",
  "Work in process 11,877 13,469", "High", "")
r("ar25_inv_fg", "[F]", "Inventories: finished goods YE2025 vs YE2024", "19,662 / 27,870", "CHF k", "FY2025", "31 Dec 2025", "AR25",
  "Finished goods 19,662 27,870", "High", "")
r("ar25_inv_wd", "[F]", "Inventory write-down expense FY2025 vs FY2024", "4.3 / 8.5", "CHF m", "FY2025", "Jan-Dec 2025", "AR25",
  "inventory write-downs was CHF 4.3 million (prior year: CHF 8.5 million)", "High", "")
r("ar24_inv_raw", "[F]", "Inventories raw materials YE2024 (as first reported) vs YE2023", "65,459 / 66,028", "CHF k", "FY2024", "31 Dec 2024", "AR24",
  "Raw materials and semi-finished products 65,459 66,028", "High", "YE2024 restated to 63,409 in AR25 (-2,050)")
r("ar23_inv", "[F]", "Inventories WIP / finished goods YE2023 vs YE2022", "9,929 / 27,473 (YE2022: 12,364 / 36,355)", "CHF k", "FY2023", "31 Dec 2023", "AR23",
  "Finished goods 27,473 36,355", "High", "")
r("h126_inv", "[F]", "Total inventories 30 Jun 2026 vs 31 Dec 2025 (no split in half-year report)", "113,699 / 89,481", "CHF k", "H1 FY2026", "30 Jun 2026", "H126",
  "Inventories 113,699 89,481", "High", "")
r("h125_inv", "[F]", "Total inventories 30 Jun 2025 (vs YE2024 as first reported and 30 Jun 2024)", "102,733 / 106,798 / 107,811", "CHF k", "H1 FY2025", "30 Jun 2025", "H125",
  "Inventories 102,733 106,798 107,811", "High", "")
r("h126_cogs", "[F]", "Cost of sales H1 2026 vs H1 2025 restated", "140,472 / 137,399", "CHF k", "H1 FY2026", "Jan-Jun 2026", "H126",
  "Cost of sales (140,472) (137,399)", "High", "")
r("h126_cl", "[F]", "Contract liabilities (customer prepayments) 30 Jun 2026 vs 31 Dec 2025", "21,232 / 14,311", "CHF k", "H1 FY2026", "30 Jun 2026", "H126",
  "Contract liabilities 21,232 14,311", "High", "")
r("h125_cl", "[F]", "Contract liabilities 30 Jun 2025 / 31 Dec 2024 / 30 Jun 2024", "21,542 / 16,228 / 20,332", "CHF k", "H1 FY2025", "30 Jun 2025", "H125",
  "Contract liabilities 21,542 16,228 20,332", "High", "")
r("ar25_cl_rev", "[F]", "Revenue recognised in FY2025 from opening contract liabilities", "13.1 (prior year 12.8)", "CHF m", "FY2025", "Jan-Dec 2025", "AR25",
  "the reporting period amounted to CHF 13.1 million", "High", "")
r("ar25_tr", "[F]", "Trade receivables, net YE2025 vs YE2024", "63,169 / 77,347", "CHF k", "FY2025", "31 Dec 2025", "AR25",
  "Trade receivables, net 63,169 77,347", "High", "")
r("h126_tr", "[F]", "Trade and other receivables, net (financial assets) 30 Jun 2026", "78,605", "CHF k", "H1 FY2026", "30 Jun 2026", "H126",
  "Trade and other receivables, net — 78,605", "High", "used for half-year DSO; YE2025 equivalent 65,838")
r("h126_tr25", "[F]", "Trade and other receivables, net (financial assets) 31 Dec 2025", "65,838", "CHF k", "FY2025", "31 Dec 2025", "H126",
  "Trade and other receivables, net — 65,838", "High", "")
r("h125_tr", "[F]", "Trade and other receivables, net (financial assets) 30 Jun 2025 and 31 Dec 2024", "63,349 / 79,977", "CHF k", "H1 FY2025", "30 Jun 2025", "H125",
  "Trade and other receivables, net — 63,349", "High", "")
r("ar25_po", "[F]", "Off-balance purchase obligations YE2025 (YE2024: 43.3)", "33.4", "CHF m", "FY2025", "31 Dec 2025", "AR25",
  "obligations at the balance sheet date totaling CHF 33.4 million", "High", "CHF 23.1m current")
r("ar23_po", "[F]", "Purchase obligations YE2023 vs YE2022", "42.8 / 63.2", "CHF m", "FY2023", "31 Dec 2023", "AR23",
  "the balance sheet date totaling CHF 42.8 million (prior year: CHF 63.2 million)", "High", "")
r("ar21_po", "[F]", "Purchase obligations YE2021 vs YE2020", "37.9 / 17.5", "CHF m", "FY2021", "31 Dec 2021", "AR21",
  "the balance sheet date totaling CHF 37.9 million (prior year: CHF 17.5 million)", "High", "")
r("ar25_capcom", "[F]", "No investment or capital commitments at YE2025", "0", "CHF m", "FY2025", "31 Dec 2025", "AR25",
  "There were no investment or capital commitments at December 31,", "High", "")

# ===================== A3 guidance =====================
r("g18", "[F]", "FY2018 guidance reiterated in Aug 2018: net sales CHF 440-460m, EBITDA margin 10-12%", "440-460; 10-12%", "CHF m; %", "FY2018", "Jan-Dec 2018", "H118",
  "Reiterating the expectations for 2018 of CHF 440-460 million in sales", "High", "described as 'recently revised' guidance")
r("g19", "[F]", "FY2019 guidance in Aug 2019: net sales CHF 350-370m, EBITDA margin 7.0-8.5%", "350-370; 7.0-8.5%", "CHF m; %", "FY2019", "Jan-Dec 2019", "H119",
  "the Group expects sales of between CHF 350 million and CHF 370 million and an EBITDA margin of 7.0% to 8.5%", "High", "")
r("g21", "[F]", "FY2021 guidance in Aug 2021: net sales CHF 480-500m, EBITDA margin 18-20%", "480-500; 18.0-20.0%", "CHF m; %", "FY2021", "Jan-Dec 2021", "H121",
  "Guidance for FY2021: net sales in the range of CHF 480 million to CHF 500 million, EBITDA margin between 18.0% and 20.0%", "High", "")
r("g22ini", "[F]", "FY2022 initial guidance (Mar 2022): revenue CHF 570-610m, EBITDA margin 21.0-23.0%", "570-610; 21.0-23.0%", "CHF m; %", "FY2022", "Jan-Dec 2022", "P21",
  "570 to 610", "High", "slide 'Guidance FY22'; margin range on same slide")
r("g22jul", "[F]", "FY2022 guidance narrowed (Jul 2022): net sales CHF 580-610m, EBITDA margin 21-23%", "580-610; 21-23%", "CHF m; %", "FY2022", "Jan-Dec 2022", "H122",
  "net sales in the range of CHF 580 million to CHF 610 million and an EBITDA margin of 21% to 23%", "High", "")
r("g22oct", "[S]", "FY2022 guidance confirmed in Q3 2022 trading update (Oct 2022): CHF 580-610m, EBITDA margin 21-23%", "580-610; 21-23%", "CHF m; %", "FY2022", "Jan-Dec 2022", "Q322",
  "Nettoumsatz in der Bandbreite von CHF 580 bis 610 Mio. und eine EBITDA-Marge zwischen 21% und 23%", "Medium", "German newswire copy; comet.tech and web.archive.org copies not retrievable")
r("ar22adj", "[F]", "FY2022 EBITDA margin 20.3%; company-adjusted ex XP Power litigation legal expense 21.8%", "20.3% / 21.8%", "%", "FY2022", "Jan-Dec 2022", "AR22",
  "the adjusted EBITDA margin was 21.8%", "High", "one-off named by management")
r("h122adj", "[F]", "H1 2022 adjusted EBITDA excluding one-time XP Power trial cost", "46.7 (17.4%) vs reported 37.7 (14.1%)", "CHF m", "H1 FY2022", "Jan-Jun 2022", "H122",
  "CHF 46.7 million and 17.4% margin", "High", "one-off named by management")
r("p22_noguid", "[F]", "No FY2023 guidance given in Mar 2023 ('no reasonable and reliable forecast')", "", "", "FY2023", "Jan-Dec 2023", "P22",
  "No reasonable and reliable forecast", "High", "")
r("g23apr", "[S]", "FY2023 first numeric guidance (Q1 2023 update, Apr 2023): net sales CHF 440-480m, EBITDA margin 13-15%", "440-480; 13-15%", "CHF m; %", "FY2023", "Jan-Dec 2023", "Q123",
  "Comet expects net sales of between CHF 440 million and CHF 480 million and an EBITDA margin of 13% to 15%", "Medium", "newswire copy of company release")
r("g23jul", "[F]", "FY2023 guidance Jul 2023: lower end of CHF 440-480m and 13-15%", "lower end of 440-480; 13-15%", "CHF m; %", "FY2023", "Jan-Dec 2023", "H123",
  "Net sales and EBITDA margin are now expected to be at the lower end of the previous guidance range", "High", "")
r("g23oct", "[S]", "FY2023 guidance cut (Q3 2023 update, 19 Oct 2023): net sales CHF 380-400m, EBITDA margin 7.0-9.0%", "380-400; 7.0-9.0%", "CHF m; %", "FY2023", "Jan-Dec 2023", "Q323",
  "It is now targeting net sales between CHF 380 million and CHF 400 million and an EBITDA margin of 7.0% to 9.0%", "Medium", "newswire copy; same range shown in CMD 2023 deck")
r("cmd23_fy23", "[F]", "CMD Nov 2023 deck shows FY2023 targets CHF 380-400m and 7.0-9.0%", "380-400", "CHF m", "FY2023", "Jan-Dec 2023", "CMD23",
  "CHF 380 million to 400 million", "High", "")
r("q323_sales", "[S]", "Q3 2023 net sales (trough quarter) vs Q3 2022; 9M 2023 vs 9M 2022", "77.7 vs 164.8; 284.8 vs 432.3", "CHF m", "Q3 FY2023", "Jul-Sep 2023", "Q323",
  "Comet reported net sales of CHF 77.7 million in Q3/23, down 52.9% year-on-year (Q3/22: CHF 164.8 million)", "Medium", "newswire copy")
r("g24ini", "[F]", "FY2024 initial guidance (Mar 2024 deck): revenue CHF 440-480m; EBITDA margin 15.0-17.0%", "440-480; 15.0-17.0%", "CHF m; %", "FY2024", "Jan-Dec 2024", "P23",
  "440 to 480", "High", "slide 'Guidance FY24'")
r("g24apr", "[S]", "FY2024 guidance confirmed Apr 2024", "440-480; 15.0-17.0%", "CHF m; %", "FY2024", "Jan-Dec 2024", "Q124",
  "net sales in the range of CHF 440 million to CHF 480 million and an EBITDA margin in the range of 15.0% to 17.0%", "Medium", "newswire copy")
r("g24jul", "[F]", "FY2024 guidance confirmed Jul 2024", "440-480; 15-17%", "CHF m; %", "FY2024", "Jan-Dec 2024", "H124",
  "confirms its guidance of net sales in the range of CHF 440 million to CHF 480 million", "High", "")
r("g24oct", "[S]", "FY2024 guidance Oct 2024: lower end of CHF 440-480m and 15.0-17.0% ('exacerbated by currency headwinds')", "lower end", "CHF m; %", "FY2024", "Jan-Dec 2024", "Q324",
  "to the lower end of the range of CHF 440 million to CHF 480 million and 15.0% to 17.0% respectively", "Medium", "newswire copy")
r("q424", "[F]", "Jan 2025 preliminary FY2024: margin ~13.8%, 'slightly below its latest expectations'", "~13.8%", "%", "FY2024", "Jan-Dec 2024", "Q424",
  "EBITDA margin slightly below its latest expectations", "High", "")
r("pr24", "[F]", "FY2024 as first reported (Mar 2025): net sales 445.4, EBITDA 60.4, margin 13.6%", "445.4; 13.6%", "CHF m; %", "FY2024", "Jan-Dec 2024", "PR24",
  "EBITDA margin of 13.6% compared to 11.3% in FY23", "High", "later restated to 13.0%")
r("g25ini", "[F]", "FY2025 initial guidance (Mar 2025): net sales CHF 480-520m, EBITDA margin 17.0-20.0%", "480-520; 17.0-20.0%", "CHF m; %", "FY2025", "Jan-Dec 2025", "PR24",
  "projected net sales of CHF 480 million to CHF 520 million and an EBITDA margin of 17.0% to 20.0%", "High", "")
r("g25apr", "[F]", "FY2025 guidance confirmed Apr 2025", "confirmed", "", "FY2025", "Jan-Dec 2025", "Q125",
  "While Comet confirms its guidance the company will continue to assess", "High", "")
r("g25jul", "[F]", "FY2025 guidance lowered Jul 2025: net sales CHF 460-500m, EBITDA margin 10.0-14.0%", "460-500; 10.0-14.0%", "CHF m; %", "FY2025", "Jan-Dec 2025", "PRH125",
  "Guidance for FY25 lowered: net sales of CHF 460 million to CHF 500 million and an EBITDA margin in a range of 10.0% to 14.0%", "High", "")
r("g25oct", "[F]", "FY2025 guidance Oct 2025: lower end of CHF 460-500m and 10.0-14.0%", "lower end", "CHF m; %", "FY2025", "Jan-Dec 2025", "Q325",
  "refines its guidance for net sales and EBITDA margin to the lower end of the range of CHF 460 million to CHF 500 million", "High", "")
r("g26mar", "[F]", "FY2026 initial guidance (Mar 2026): net sales and adjusted EBITDA margin to 'significantly exceed' 2025; ~3pp one-offs excluded", "qualitative", "", "FY2026", "Jan-Dec 2026", "PR25",
  "excludes one-off items of approximately 3 percentage points", "High", "no numeric range")
r("g26apr", "[F]", "FY2026 guidance confirmed Apr 2026 (still qualitative)", "confirmed", "", "FY2026", "Jan-Dec 2026", "Q126",
  "Comet confirms its guidance for 2026", "High", "")
r("g26jul", "[F]", "FY2026 guidance Jul 2026: net sales CHF 540-570m, reported EBITDA margin 14.0-17.0% (incl. ~3pp one-offs)", "540-570; 14.0-17.0%", "CHF m; %", "FY2026", "Jan-Dec 2026", "PR126",
  "net sales of CHF 540–570 million and an EBITDA margin in the range of 14.0% to 17.0%", "High", "")
r("g26jul_adj", "[F]", "FY2026 EBITDA margin excluding one-offs per Jul 2026 deck", "17.0-20.0%", "%", "FY2026", "Jan-Dec 2026", "P126",
  "(excluding one-offs: 17.0% to 20.0%)", "High", "")
r("g26oct", "[F]", "FY2026 guidance raised Oct 2026: net sales CHF 570-590m, reported EBITDA margin 17.0-19.0%", "570-590; 17.0-19.0%", "CHF m; %", "FY2026", "Jan-Dec 2026", "Q326",
  "FY26 guidance increased: net sales of CHF 570 – 590 million and an EBITDA margin of 17.0% – 19.0%", "High", "")
r("g26oct_oneoff", "[F]", "FY2026 reported margin guidance includes one-time costs of up to 3pp (Penang ramp-up, efficiency)", "up to 3", "pp", "FY2026", "Jan-Dec 2026", "Q326",
  "includes one-time costs totaling up to 3 percentage points", "High", "")
r("h126_eff", "[C]", "Efficiency program: sustainable EBITDA improvement target from 2028", "20-30 per year", "CHF m", "FY2028", "Jan-Dec 2028", "H126",
  "sustainable EBITDA improvement of CHF 20-30 million per", "High", "company target, untestable")
r("cmdpr_targets", "[C]", "Mid-term (next cycle peak, now 2028) targets cut Nov 2025: net sales CHF 670-770m (was 800-900), EBITDA margin 22-27% (was 25-30%)", "670-770; 22-27%", "CHF m; %", "FY2028", "Jan-Dec 2028", "CMDPR",
  "Net sales of CHF 670 million to CHF 770 million (from CHF 800 million to CHF 900 million)", "High", "DV agent covers CMD detail")

# ===================== A4 concentration / geography =====================
r("ar25_cust", "[F]", "Largest customer (PCT) share of group sales FY2025 (FY2024: CHF 106.2m, 23.8%)", "104.4; 22.8%", "CHF m; %", "FY2025", "Jan-Dec 2025", "AR25",
  "CHF 104.4 million with its largest customer, which represented 22.8% of Group sales", "High", "only one customer disclosed")
r("ar24_cust", "[F]", "Largest customer share FY2024 vs FY2023", "23.8% / 17.7% (CHF 71m)", "%", "FY2024", "Jan-Dec 2024", "AR24",
  "resented 23.8% of Group sales (prior year: CHF 71 million and 17.7%", "High", "")
r("ar23_cust", "[F]", "Largest customer share FY2023 vs FY2022", "17.7% / 36.1% (CHF 211m)", "%", "FY2023", "Jan-Dec 2023", "AR23",
  "sented 17.7% of Group sales (prior year: CHF 211 million and 36.1%", "High", "")
r("ar21_cust", "[F]", "Largest customer share FY2021 vs FY2020", "30.4% (CHF 156m) / 32.4% (CHF 128m)", "%", "FY2021", "Jan-Dec 2021", "AR21",
  "resented 30.4% of Group sales (prior year: CHF 128 million and 32.4%", "High", "")
r("ar25_loc", "[F]", "Region split is by customer location", "", "", "FY2025", "Jan-Dec 2025", "AR25",
  "Net sales are allo- cated to countries on the basis of customer location.", "High", "")
r("ar25_china", "[F]", "Net sales to China FY2025 vs FY2024", "114,604 / 120,152", "CHF k", "FY2025", "Jan-Dec 2025", "AR25",
  "China 114,604 120,152", "High", "Korea and Taiwan not shown separately (in 'Rest of Asia')")
r("ar25_asia", "[F]", "Net sales Asia total FY2025 vs FY2024", "289,842 / 277,920", "CHF k", "FY2025", "Jan-Dec 2025", "AR25",
  "Total, Asia 289,842 277,920", "High", "")
r("ar25_mal", "[F]", "Net sales Malaysia FY2025 vs FY2024", "71,204 / 56,319", "CHF k", "FY2025", "Jan-Dec 2025", "AR25",
  "Malaysia 71,204 56,319", "High", "")
r("ar25_jp", "[F]", "Net sales Japan FY2025 vs FY2024", "18,718 / 18,228", "CHF k", "FY2025", "Jan-Dec 2025", "AR25",
  "Japan 18,718 18,228", "High", "")
r("ar25_roa", "[F]", "Net sales Rest of Asia (incl. Korea, Taiwan) FY2025 vs FY2024", "85,316 / 83,222", "CHF k", "FY2025", "Jan-Dec 2025", "AR25",
  "Rest of Asia 85,316 83,222", "High", "")
r("ar25_na", "[F]", "Net sales North America FY2025 vs FY2024", "81,578 / 88,319", "CHF k", "FY2025", "Jan-Dec 2025", "AR25",
  "Total, North America 81,578 88,319", "High", "")
r("ar25_eu", "[F]", "Net sales Europe FY2025 vs FY2024", "78,174 / 71,411", "CHF k", "FY2025", "Jan-Dec 2025", "AR25",
  "Total, Europe 78,174 71,411", "High", "")
r("ar24_china", "[F]", "Net sales to China FY2024 vs FY2023; Malaysia shown separately from FY2023", "120,152 / 108,040", "CHF k", "FY2024", "Jan-Dec 2024", "AR24",
  "China 120,152 108,040", "High", "")
r("ar24_mal", "[F]", "Net sales Malaysia FY2024 vs FY2023", "56,319 / 28,002", "CHF k", "FY2024", "Jan-Dec 2024", "AR24",
  "Malaysia 56,319 28,002", "High", "")
r("ar23_na", "[F]", "North America net sales FY2023 vs FY2022", "92,736 / 221,944", "CHF k", "FY2023", "Jan-Dec 2023", "AR23",
  "Total, North America 92,736 221,944", "High", "")
r("ar23_china", "[F]", "Net sales to China FY2023 vs FY2022", "108,040 / 105,848", "CHF k", "FY2023", "Jan-Dec 2023", "AR23",
  "China 108,040 105,848", "High", "")
r("ar21_china", "[F]", "Net sales to China FY2021 vs FY2020", "98,561 / 55,101", "CHF k", "FY2021", "Jan-Dec 2021", "AR21",
  "China 98,561 55,101", "High", "")
r("h126_asia", "[F]", "Net sales Asia H1 2026 vs H1 2025", "161,828 / 144,990", "CHF k", "H1 FY2026", "Jan-Jun 2026", "H126",
  "Asia 161,828 144,990", "High", "half-year report gives no country split (no China figure)")
r("h126_na", "[F]", "Net sales North America H1 2026 vs H1 2025", "41,456 / 41,212", "CHF k", "H1 FY2026", "Jan-Jun 2026", "H126",
  "North America 41,456 41,212", "High", "")
r("h126_eu", "[F]", "Net sales Europe H1 2026 vs H1 2025", "32,424 / 37,651", "CHF k", "H1 FY2026", "Jan-Jun 2026", "H126",
  "Europe 32,424 37,651", "High", "")
r("ar22_export", "[F]", "Company flags US export restrictions on semiconductor equipment to certain Chinese customers as a 2023 risk", "", "", "FY2022", "Mar 2023", "AR22",
  "monitor the US export restrictions on the supply of semiconductor", "High", "")
r("ar22_invrisk", "[F]", "Trade restrictions identified as inventory risk for items with US technology destined for China; no impact at YE2022", "", "", "FY2022", "31 Dec 2022", "AR22",
  "Trade restrictions are identified as an additional risk for inventory in", "High", "")
r("ar24_tc", "[F]", "Comet runs a Trade Compliance Policy covering export controls and sanctions", "", "", "FY2024", "Jan-Dec 2024", "AR24",
  "including customs regulations, export controls,", "High", "")
r("q326_geo", "[C]", "Company: affected 'only to a limited extent' by geopolitical tensions (Oct 2026)", "", "", "Q3 FY2026", "Oct 2026", "Q326",
  "Comet is only affected to a limited extent", "High", "")
r("ar22_restate", "[F]", "YE2021 contract liabilities and receivables restated in AR 2022 (netting of IXS prepayments with contract assets)", "8.1", "CHF m", "FY2021", "31 Dec 2021", "AR22",
  "The adjustment amounts to CHF 8.1 million in prior year.", "High", "explained; no P&L effect")
r("h123_restate", "[F]", "30 Jun 2022 receivables and contract liabilities restated in H1 2023 report (same netting)", "4.0", "CHF m", "H1 FY2022", "30 Jun 2022", "H123",
  "The adjustment amounts to CHF 4.0 million as of June 30,", "High", "explained")
r("h119_restate", "[F]", "H1 2018 EBITDA restated for IFRS 16 adoption in H1 2019 report", "29,527 / +2,580 / 32,107", "CHF k", "H1 FY2018", "Jan-Jun 2018", "H119",
  "EBITDA 29,527 2,580 32,107", "High", "explained (IFRS 16 full retrospective)")
r("p19ifrs16", "[F]", "FY2018 EBITDA margin: restated IFRS16 9.8% vs as reported 8.7%", "9.8% / 8.7%", "%", "FY2018", "Jan-Dec 2018", "P19",
  "In % of sales 10.8% 9.8% 1.1% 8.7%", "High", "")

# ===================== A5 balance sheet / capital =====================
r("h126_cash", "[F]", "Cash and cash equivalents 30 Jun 2026 vs 31 Dec 2025", "69,792 / 96,587", "CHF k", "H1 FY2026", "30 Jun 2026", "H126",
  "Cash and cash equivalents 69,792 96,587", "High", "")
r("h126_debt", "[F]", "Non-current interest-bearing debt 30 Jun 2026 (the 2026-2031 bond)", "59,660", "CHF k", "H1 FY2026", "30 Jun 2026", "H126",
  "Non-current debt (interest-bearing) 59,660 -", "High", "")
r("h126_lease_c", "[F]", "Current lease liabilities 30 Jun 2026 vs 31 Dec 2025", "5,326 / 5,485", "CHF k", "H1 FY2026", "30 Jun 2026", "H126",
  "Current lease liabilities 5,326 5,485", "High", "")
r("h126_lease_nc", "[F]", "Non-current lease liabilities 30 Jun 2026 vs 31 Dec 2025", "24,112 / 25,845", "CHF k", "H1 FY2026", "30 Jun 2026", "H126",
  "Non-current lease liabilities 24,112 25,845", "High", "")
r("h126_bond", "[F]", "New bond: CHF 60m, issued 20 Apr 2026 at 100.11%, 5-year, matures 18 Apr 2031", "60", "CHF m", "H1 FY2026", "Apr 2026", "H126",
  "It has a term of five years and matures on April 18, 2031.", "High", "ticker COT26")
r("h126_coupon", "[F]", "New bond fixed annual coupon", "2.00", "%", "H1 FY2026", "Apr 2026", "H126",
  "carries a fixed annual coupon of 2.00%", "High", "")
r("h126_repaid", "[F]", "2021-2026 bond repaid at maturity 20 Apr 2026 and refinanced", "60", "CHF m", "H1 FY2026", "Apr 2026", "H126",
  "The bond maturing on April 20, 2026 was repaid on its maturity date", "High", "")
r("ar25_oldbond", "[F]", "2021 bond: CHF 60m, coupon 1.30%, matured 20 Apr 2026", "1.30", "%", "FY2025", "31 Dec 2025", "AR25",
  "1.30%, payable annually on April 20.", "High", "")
r("h126_bondfv", "[F]", "Fair value of the new bond at 30 Jun 2026 (carrying 59,660)", "61,440", "CHF k", "H1 FY2026", "30 Jun 2026", "H126",
  "Non-current debt, fixed rate — — — 59,660 61,440", "High", "")
r("h126_rcf", "[F]", "Syndicated committed RCF: CHF 60m from Apr 2023 (5-year), accordion exercised Jun 2025 -> CHF 100m; undrawn at 30 Jun 2026", "100", "CHF m", "H1 FY2026", "30 Jun 2026", "H126",
  "The facility remained undrawn as of June 30, 2026.", "High", "")
r("ar25_cov", "[F]", "RCF financial covenant: maximum leverage ratio; in compliance FY2025", "3:1", "ratio", "FY2025", "31 Dec 2025", "AR25",
  "maximum leverage ratio of 3:1", "High", "")
r("ar25_uncom", "[F]", "Uncommitted credit facilities CHF 26.6m, of which utilised (guarantees/working capital)", "8.8", "CHF m", "FY2025", "31 Dec 2025", "AR25",
  "CHF 8.8 million was utilized as of December 31, 2025", "High", "")
r("ar25_netdebt", "[F]", "Net debt (negative = net cash) YE2025 vs YE2024 restated; debt factor -0.1 / -0.3", "(5,287) / (16,132)", "CHF k", "FY2025", "31 Dec 2025", "AR25",
  "Net debt (5,287) (16,132)", "High", "net debt includes lease liabilities")
r("ar25_leasemat", "[F]", "Undiscounted contractual payments YE2025: debt 60,238 due 2026; leases 34,929 (6,382 in 2026)", "60,238 / 34,929", "CHF k", "FY2025", "31 Dec 2025", "AR25",
  "Lease liabilities 17 31,330 34,929 6,382 18,730 9,817", "High", "")
r("p126_netdebt", "[F]", "Deck describes a 'temporary net debt position' at 30 Jun 2026 (higher capex)", "", "", "H1 FY2026", "30 Jun 2026", "P126",
  "Temporary net debt position", "High", "")
r("h126_div", "[F]", "Dividend CHF 0.50/share paid 20 Apr 2026, total CHF 3.9m (prior year CHF 1.50)", "3.9", "CHF m", "FY2026", "Apr 2026", "H126",
  "Comet Holding AG paid the dividend, which totaled CHF 3.9 million", "High", "")
r("ar25_divhist", "[F]", "Distribution per share for FY2025, 2024, 2023, 2022, 2021", "0.50 / 1.50 / 1.00 / 3.70 / 3.50", "CHF", "FY2025-FY2021", "Jan-Dec 2021-2025", "AR25",
  "Distribution per share 1 CHF 0.50 1.50 1.00 3.70 3.50", "High", "")
r("ar25_divcash", "[F]", "Dividends paid in cash FY2025 vs FY2024", "11,654 / 7,772", "CHF k", "FY2025", "Jan-Dec 2025", "AR25",
  "Dividend payment to shareholders of Comet Holding AG 33 (11,654) (7,772)", "High", "")
r("ar25_tsy", "[F]", "Repurchase of treasury shares (for share-based compensation; no buyback programme disclosed) FY2025 vs FY2024", "439 / 1,257", "CHF k", "FY2025", "Jan-Dec 2025", "AR25",
  "Repurchase of treasury shares (439) (1,257)", "High", "")
r("h126_tsy", "[F]", "No treasury shares bought on the market in H1 2026", "0", "", "H1 FY2026", "Jan-Jun 2026", "H126",
  "No treasury shares were purchased on the market during the period.", "High", "")
r("ar25_noma", "[F]", "No change in the basis of consolidation in 2025 (no acquisitions/disposals)", "", "", "FY2025", "Jan-Dec 2025", "AR25",
  "In 2025, there were no changes in the basis of consolidation from the prior year.", "High", "same statement in AR 2022-2024")
r("ar24_noma", "[F]", "No change in the basis of consolidation in 2024", "", "", "FY2024", "Jan-Dec 2024", "AR24",
  "In 2024, there were no changes in the basis of consolidation from the", "High", "")
r("ar23_noma", "[F]", "No change in the basis of consolidation in 2023", "", "", "FY2023", "Jan-Dec 2023", "AR23",
  "In 2023, there were no changes in the basis of consolidation from the", "High", "")
r("ar22_noma", "[F]", "No change in the basis of consolidation in 2022", "", "", "FY2022", "Jan-Dec 2022", "AR22",
  "In 2022, there were no changes in the basis of consolidation from the", "High", "")
r("ar21_ors", "[F]", "ORS (Object Research Systems, Montreal; Dragonfly software) acquired effective 31 Dec 2020", "", "", "FY2020", "31 Dec 2020", "AR21",
  "effective December 31, 2020, Comet acquired sole", "High", "renamed Comet Technologies Canada Inc.; integrated into IXS in 2023")
r("ar21_ors_price", "[F]", "ORS total consideration transferred", "8,978", "CHF k", "FY2020", "Dec 2020", "AR21",
  "Total consideration transferred 1 8,978", "High", "incl. CHF 1.4m holdback; plus CHF 1.5m post-combination compensation (expensed)")
r("ar21_ors_gw", "[F]", "ORS goodwill capitalised (IXS)", "4,710", "CHF k", "FY2020", "Dec 2020", "AR21",
  "Goodwill, capitalized 1 4,710", "High", "")
r("ar23_ors", "[F]", "ORS integrated into IXS in 2023", "", "", "FY2023", "Jan-Dec 2023", "AR23",
  "we successfully integrated the acquired Canadian company", "High", "")
r("ar21_ebeam", "[F]", "ebeam lamp business sold to Tetra Pak eBeam Systems SA effective 30 Nov 2020", "", "", "FY2020", "30 Nov 2020", "AR21",
  "Comet sold the ebeam lamp business to Tetra Pak eBeam Systems SA", "High", "")
r("ar21_ebeam_cash", "[F]", "ebeam disposal: cash from buyer / gain on disposal", "7,542 / 3,986", "CHF k", "FY2020", "Nov 2020", "AR21",
  "Gain on disposal of businesses 3,986", "High", "cash payment 7,542")
r("p19_ebt", "[F]", "FY2018 loss on disposal of businesses (EBT US systems manufacturer) inside EBITDA", "6.6", "CHF m", "FY2018", "Jan-Dec 2018", "P19",
  "Loss on disposal of businesses - -6.6 6.6", "High", "one-off named by management")
r("ar25_gw", "[F]", "Goodwill YE2025 (YE2024): IXS CGU 19,869 (20,377), IXT CGU 6,873 (6,873)", "26,742", "CHF k", "FY2025", "31 Dec 2025", "AR25",
  "Goodwill 19,869 20,377 6,873 6,873 26,742 27,250", "High", "IXS goodwill includes ORS")
r("ar25_imptest", "[F]", "Goodwill impairment test FY2025 passed; pre-tax WACC IXS 11.4% (2024: 8.8%)", "", "", "FY2025", "30 Sep 2025 test date", "AR25",
  "For each CGU, the recoverable amount exceeds its carrying amount.", "High", "no goodwill impairment recorded")
r("ar25_imp", "[F]", "Impairment charges FY2025 (fire damage, PCT) vs FY2024", "354 / 46", "CHF k", "FY2025", "Jan-Dec 2025", "AR25",
  "Impairment of property, plant and equipment 354 46", "High", "")
r("ar25_xp", "[F]", "XP Power trade-secret case: jury award 2022", "USD 40m (20 compensatory + 20 punitive)", "USD m", "FY2022", "Mar 2022", "AR25",
  "USD 20 million in punitive damages for a total of USD 40 million", "High", "")
r("ar25_xpfees", "[F]", "XP Power: court awarded legal fees and pre-judgement interest (Jan 2025)", "~19", "USD m", "FY2025", "Jan 2025", "AR25",
  "pre-judgement interest totaling approximately USD 19 million", "High", "")
r("ar25_xpbond", "[F]", "XP Power posted appeal bond", "48.4", "USD m", "FY2022", "Dec 2022", "AR25",
  "XP secured a USD 48.4 million bond to stay enforcement", "High", "")
r("ar25_xpca", "[F]", "Award treated as contingent asset at YE2025 (not recognised)", "", "", "FY2025", "31 Dec 2025", "AR25",
  "classified as a contingent asset as of December 31, 2025", "High", "contingent success fee to lawyers = contingent liability")
r("h126_xp", "[F]", "Ninth Circuit vacated the judgment on 14 Jul 2026 and remanded; damages, injunction and fees not enforceable", "", "", "FY2026", "14 Jul 2026", "H126",
  "vacated the prior judgment in the litigation", "High", "")
r("h126_xp2", "[F]", "No receivable or income recognised for the XP judgment at 30 Jun 2026", "0", "CHF", "H1 FY2026", "30 Jun 2026", "H126",
  "no receivable or income had been recog", "High", "")
r("xppr", "[C]", "Company: remand not expected to have a material impact", "", "", "FY2026", "Jul 2026", "XPPR",
  "The remand is not expected to have a material impact", "High", "")
r("bondpage", "[F]", "Bond pricing announced on comet.tech 'Bond' page dated 18 Mar 2026 (page carries no terms)", "", "", "FY2026", "18 Mar 2026", "BOND",
  "March 18, 2026", "Medium", "terms taken from H1 2026 report note 06.1")

# ===================== A6 cycle =====================
r("ar21five_sales", "[F]", "Net sales 2021, 2020, 2019, 2018, 2017", "513,721 / 395,816 / 371,606 / 436,356 / 443,370", "CHF k", "FY2021-FY2017", "Jan-Dec 2017-2021", "AR21",
  "Net sales 513,721 395,816 371,606 436,356 443,370", "High", "")
r("ar21five", "[F]", "EBITDA 2021, 2020, 2019, 2018, 2017", "102,749 / 58,616 / 39,974 / 42,966 / 63,203", "CHF k", "FY2021-FY2017", "Jan-Dec 2017-2021", "AR21",
  "EBITDA 102,749 58,616 39,974 42,966 63,203", "High", "2018 IFRS16-restated; 2017 not")
r("h118_sales", "[F]", "Net sales H1 2018 vs H1 2017 (IFRS15-restated)", "232,381 / 222,624", "CHF k", "H1 FY2018", "Jan-Jun 2018", "H118",
  "Net sales 232,381 222,624 9,757 4.4%", "High", "")
r("h118_ebitda", "[F]", "EBITDA H1 2018 (pre-IFRS16) vs H1 2017", "29,527 / 33,819", "CHF k", "H1 FY2018", "Jan-Jun 2018", "H118",
  "EBITDA 29,527 33,819 (4,293) – 12.7%", "High", "")
r("h119_sales", "[F]", "Net sales H1 2019 vs H1 2018 (-23.8%)", "176,959 / 232,381", "CHF k", "H1 FY2019", "Jan-Jun 2019", "H119",
  "Net sales 176,959 232,381 (55,422) – 23.8%", "High", "")
r("h119_ebitda", "[F]", "EBITDA H1 2019 vs H1 2018 restated (-73.5%)", "8,513 / 32,107", "CHF k", "H1 FY2019", "Jan-Jun 2019", "H119",
  "EBITDA 8,513 32,107 (23,595) – 73.5%", "High", "")
r("h120", "[F]", "Net sales and EBITDA H1 2020", "182,309 / 18,753", "CHF k", "H1 FY2020", "Jan-Jun 2020", "H120",
  "EBITDA 18,753 8,513 10,240 120.3%", "High", "net sales 182,309 on same page")
r("h120_sales", "[F]", "Net sales H1 2020 vs H1 2019", "182,309 / 176,959", "CHF k", "H1 FY2020", "Jan-Jun 2020", "H120",
  "Net sales 182,309 176,959 5,351 3.0%", "High", "")
r("h121", "[F]", "Net sales and EBITDA H1 2021 vs H1 2020", "248,302 / 44,252", "CHF k", "H1 FY2021", "Jan-Jun 2021", "H121",
  "Net sales 248,302 182,309 65,993 36.2%", "High", "EBITDA 44,252")
r("h121_ebitda", "[F]", "EBITDA H1 2021 vs H1 2020", "44,252 / 18,753", "CHF k", "H1 FY2021", "Jan-Jun 2021", "H121",
  "EBITDA 44,252 18,753 25,499 136.0%", "High", "")
r("h122", "[F]", "Net sales H1 2022 vs H1 2021", "267,498 / 248,302", "CHF k", "H1 FY2022", "Jan-Jun 2022", "H122",
  "Net sales 267,498 248,302 19,196 7.7%", "High", "")
r("h122_ebitda", "[F]", "EBITDA H1 2022 vs H1 2021", "37,681 / 44,252", "CHF k", "H1 FY2022", "Jan-Jun 2022", "H122",
  "EBITDA 37,681 44,252 (6,571) – 14.8%", "High", "includes ~CHF 9m XP trial cost")
r("h123", "[F]", "Net sales H1 2023 vs H1 2022", "207,025 / 267,498", "CHF k", "H1 FY2023", "Jan-Jun 2023", "H123",
  "Net sales 207,025 267,498 (60,473) – 22.6%", "High", "")
r("h123_ebitda", "[F]", "EBITDA H1 2023 vs H1 2022", "14,275 / 37,681", "CHF k", "H1 FY2023", "Jan-Jun 2023", "H123",
  "EBITDA 14,275 37,681 (23,406) – 62.1%", "High", "")
r("h123_oneoff", "[F]", "H1 2023 PCT EBITDA includes one-time expenses for cost reduction (amount not disclosed)", "", "", "H1 FY2023", "Jan-Jun 2023", "H123",
  "This includes one-time expenses for cost reduction", "High", "one-off named, unquantified")
r("ar23_sj", "[F]", "FY2023: closure of matchbox volume production in San Jose reduced H1 2023 EBITDA (amount not disclosed)", "", "", "FY2023", "Jan-Jun 2023", "AR23",
  "of matchboxes in San Jose, California, reduced EBITDA in the first half", "High", "one-off named, unquantified")
r("h124", "[F]", "Net sales H1 2024 vs H1 2023", "189,315 / 207,025", "CHF k", "H1 FY2024", "Jan-Jun 2024", "H124",
  "Net sales 189,315 207,025 (17,710) – 8.6%", "High", "")
r("h124_ebitda", "[F]", "EBITDA H1 2024 vs H1 2023", "12,980 / 14,275", "CHF k", "H1 FY2024", "Jan-Jun 2024", "H124",
  "EBITDA 12,980 14,275 (1,295) – 9.1%", "High", "")
r("p23_q", "[F]", "Quarterly net sales Q4/22, Q1/23, Q2/23, Q3/23, Q4/23 and H1/23, H2/23 (deck, rounded)", "154 / 107 / 100 / 78 / 113; 207 / 191", "CHF m", "Q4 FY2022-Q4 FY2023", "Oct 2022-Dec 2023", "P23",
  "154 107 100 78 113 207 191", "High", "")
r("p24_q", "[F]", "Quarterly net sales Q1-Q4 2024 (deck, rounded); H2/24 margin 18.7% as first reported", "81 / 108 / 113 / 143", "CHF m", "FY2024 quarters", "Jan-Dec 2024", "P24",
  "81 108 113 143", "High", "")
r("q123_q122", "[S]", "Q1 2023 net sales vs Q1 2022", "107.5 / 124.8", "CHF m", "Q1 FY2023", "Jan-Mar 2023", "Q123",
  "down 13.9% year-over-year (Q1/22: CHF 124.8 million)", "Medium", "newswire copy")
r("q324_q", "[S]", "Q3 2024 net sales vs Q2 2024; 9M 2024", "113.2 / 108.4; 302.5", "CHF m", "Q3 FY2024", "Jul-Sep 2024", "Q324",
  "(Q2/24: CHF 108.4 million)", "Medium", "newswire copy")
r("q124_q423", "[S]", "Q1 2024 net sales; Q4 2023 net sales", "80.9 / 112.7", "CHF m", "Q1 FY2024", "Jan-Mar 2024", "Q124",
  "(Q4/23: CHF 112.7 million)", "Medium", "newswire copy")
r("p19_h2", "[F]", "FY2019 deck: half-year sales fell 12% in H2 2018 and 13% in H1 2019; rose 10% in H2 2019", "", "", "FY2018-FY2019", "Jul 2018-Dec 2019", "P19",
  "In H2_18 and again in", "High", "")

# ---- late additions (numbered after the [I] rows so earlier ids stay stable) ----
RX_START = len(R)
r("ar25_eps", "[F]", "No dilutive instruments (no convertibles/options): diluted EPS = basic EPS", "", "", "FY2025", "31 Dec 2025", "AR25",
  "As Comet Holding AG has no such instruments, diluted earnings per share is identical to basic earnings per share.", "High", "")
r("ar25_yxlon", "[F]", "Yxlon (Beijing) X-Ray Equipment Trading in liquidation (started Nov 2025, completion expected Q2 2026)", "", "", "FY2025", "Nov 2025", "AR25",
  "The full deregistration and liquidation process is expected to be completed by the second quarter of 2026.", "High", "")
r("ar25_legal", "[F]", "Legal risk paragraph lists export regulations among risks", "", "", "FY2025", "31 Dec 2025", "AR25",
  "misappropriation, patent law, export regulations, tax law and competi", "High", "")
r("h118_dav", "[F]", "2018: closure of the ebeam systems site in Davenport, Iowa (USA)", "", "", "FY2018", "2018", "H118",
  "Closure of the Davenport site in Iowa, USA", "High", "")
r("p19_b2b", "[F]", "Book-to-bill FY2019 vs FY2018", "1.08 / 1.00", "ratio", "FY2019", "Jan-Dec 2019", "P19",
  "Book-to-bill ratio 1.08 1.00 0.08 8.0%", "High", "")
r("ar22_fcfpct", "[F]", "AR 2022 five-year table shows FCF % of sales 7.2/11.2/10.5/13.1/6.4 for 2022-2018 (2019 FCF 30,112 on sales 371,606 = 8.1%: presentation slip)", "13.1% shown", "%", "FY2019", "Jan-Dec 2019", "AR22",
  "In % of net sales 7.2% 11.2% 10.5% 13.1% 6.4%", "High", "percentages appear copied from operating-cash-flow ratios")
r("ar25_capex", "[F]", "Purchases of PPE FY2025 vs FY2024 (Penang building)", "41,479 / 10,327", "CHF k", "FY2025", "Jan-Dec 2025", "AR25",
  "Purchases of property, plant and equipment 16 (41,479) (10,327)", "High", "")

# ===================== [I] rows =====================
I = []
def ii(key, claim, value, unit, pf, pc, inputs, script, conf, reason):
    I.append((key, claim, value, unit, pf, pc, inputs, script, conf, reason))

S1, S2, S3 = "research/out/comet/calc/A_periods.py", "research/out/comet/calc/A_guidance.py", "research/out/comet/calc/A_cycle.py"
ii("i_h225", "H2 2025 derived (FY2025 - H1 2025 restated): net sales; gross margin; EBITDA; EBITDA margin; EBIT margin", "229,890; 36.5%; 23,357; 10.2%; 5.4%", "CHF k; %",
   "H2 FY2025", "Jul-Dec 2025", ["ar25_is_sales", "ar25_gp", "ar25is_ebitda", "ar25_ebit", "h126_is_sales", "h126_gp", "h126_ebitda", "h126_ebit"], S1, "High", "simple subtraction of audited FY and restated H1")
ii("i_h225_cons", "H2 2025 EBITDA margin on a consistent basis is 10.2% (vs 10.1% restated H1 2025), not 11.1% vs 9.1% as in the FY2025 deck: the deck's H2 absorbs the CHF 2.27m H1 restatement", "10.2% vs 11.1%", "%",
   "H2 FY2025", "Jul-Dec 2025", ["p25_h2", "h126_restate_ebitda", "ar25is_ebitda"], S1, "High", "deck H2 = FY (restated basis) minus H1 as first reported")
ii("i_h225_sales_yoy", "H2 2025 net sales YoY vs H2 2024 (256,047)", "-10.2%", "%", "H2 FY2025", "Jul-Dec 2025", ["ar25_is_sales", "h124", "h126_is_sales"], S1, "High", "H2 2024 = FY2024 - H1 2024")
ii("i_fcf", "FCF: H2 2025 7,158; LTM to Jun-2026 -12,148; SBC/FCF FY2025 16.6%", "7,158; -12,148; 16.6%", "CHF k; %", "H2 FY2025; LTM Jun-2026", "Jul 2025-Jun 2026",
   ["ar25_ocf", "ar25_icf", "h126_fcf", "ar25_sbc", "h126_sbc"], S1, "High", "FCF definition = OCF + investing CF (company APM)")
ii("i_sbc", "SBC as % of sales: FY2025 0.31%, H1 2026 0.28%; LTM SBC CHF 1.7m", "0.31% / 0.28%", "%", "FY2025; H1 FY2026", "2025; Jan-Jun 2026", ["ar25_sbc", "h126_sbc", "ar25_is_sales", "h126_is_sales"], S1, "High", "direct ratio")
ii("i_h126_ex", "H1 2026 EBITDA margin ex CHF 4.5m one-time costs: 15.0% (reported 13.1%); EBIT margin 10.4% (8.5%)", "15.0% / 10.4%", "%", "H1 FY2026", "Jan-Jun 2026",
   ["h126_ebitda", "h126_oneoff", "h126_ebit", "h126_is_sales"], S1, "High", "company quantified the one-off")
ii("i_fy25_ex", "FY2025 EBITDA margin ex CHF 2.1m fire insurance recovery: 9.7% (reported 10.1%); H2 2025 9.2% (10.2%)", "9.7% / 9.2%", "%", "FY2025; H2 FY2025", "Jan-Dec 2025",
   ["ar25is_ebitda", "ar25_fire", "ar25_is_sales"], S1, "Medium", "management did not present an adjusted figure; recovery is the only quantified non-recurring item")
ii("i_restate", "Restatement effects: FY2024 EBITDA margin 13.6% -> 13.0%, gross margin 43.4% -> 42.8%; H1 2025 EBITDA margin 9.1% -> 10.1%", "13.6->13.0; 9.1->10.1", "%",
   "FY2024; H1 FY2025", "2024; Jan-Jun 2025", ["ar25_restate_is", "ar25_restate_gp", "h126_restate_ebitda", "h125_orig"], S1, "High", "same CHF 2.27-2.37m inventory write-down moved from H1 2025 to FY2024")
ii("i_fy22_adj", "XP Power litigation one-off: H1 2022 ~CHF 9.0m (EBITDA margin 14.1% -> 17.5% ex); FY2022 20.3% -> 21.8% company-adjusted", "9.0", "CHF m",
   "H1 FY2022; FY2022", "2022", ["h122adj", "h122_ebitda", "ar22adj"], S1, "High", "difference between company adjusted and reported")
ii("i_fy18_ex", "FY2018 EBITDA margin ex CHF 6.6m loss on disposal: 11.4% (restated reported 9.8%)", "11.4%", "%", "FY2018", "Jan-Dec 2018", ["ar21five", "ar21five_sales", "p19_ebt"], S1, "High", "direct")
ii("i_fy26_ex", "FY2026 guided EBITDA margin ex one-offs: Jul-2026 17-20%; Oct-2026 ~20-22% (one-offs 'up to' 3pp)", "17-20 / 20-22", "%", "FY2026", "Jan-Dec 2026",
   ["g26jul", "g26jul_adj", "g26oct", "g26oct_oneoff"], S1, "Medium", "Oct one-off stated as 'up to' 3pp, so ex-one-off range is an upper bound")
ii("i_q4_25", "Q4 2025 net sales (FY2025 - 9M 2025): 127.4; YoY vs Q4 2024 (142.9) -10.8%", "127.4", "CHF m", "Q4 FY2025", "Oct-Dec 2025", ["ar25_is_sales", "q325_9m", "q324_q"], S1, "High", "subtraction of reported figures")
ii("i_q2_26yoy", "Q2 2026 net sales YoY vs Q2 2025 (116.0): +15.1%; LTM to Sep-2026 net sales 522.8 (+10.6%)", "+15.1%; 522.8", "%; CHF m", "Q2 FY2026; LTM Sep-2026", "Apr-Jun 2026",
   ["pr126_q2", "q125_sales", "h126_is_sales", "q326_sales", "q326_9m"], S1, "High", "subtraction of reported figures")
ii("i_orders", "Orders per quarter: Q1 2025 b2b 1.07; Q2 2025 104.4 (b2b 0.90); Q4 2025 129.9 (b2b 1.02); Q2 2026 209.9 (b2b 1.57); FY2025 ~457.3 (b2b ~1.00)", "see value list", "CHF m",
   "Q2 FY2025-Q2 FY2026", "Apr 2025-Jun 2026", ["q125_orders", "h125_orders", "q325_orders", "q126_orders", "h126_orders", "q326_orders"], S1, "High", "subtraction of YTD orders")
ii("i_q3orders", "Q3 2025 orders implied by Oct-2025 release (327.4 - 222.9 = 104.5) differ from the 102.1 stated in the Oct-2026 release; no explanation found", "104.5 vs 102.1", "CHF m",
   "Q3 FY2025", "Jul-Sep 2025", ["q325_orders", "h125_orders", "q326_orders"], S1, "Medium", "could be an order cancellation/FX or definition change; not explained by the company")
ii("i_q1_24", "Q1 2024 book-to-bill 1.09 (Apr-2024) vs 91.0/80.9 = 1.12 implied by Apr-2025 comparative; small unexplained change", "1.09 vs 1.12", "ratio",
   "Q1 FY2024", "Jan-Mar 2024", ["q124_b2b", "q125_orders", "q125_sales"], S1, "Low", "first figure from a newswire copy; could be rounding of a ratio or a later order revision")
ii("i_inv_mix", "Inventory mix YE2025: raw 65% / WIP 13% / FG 22% (YE2024r: 61/13/27); finished goods -29% YoY; inventory days 115 (FY COGS)", "65/13/22", "%",
   "FY2025", "31 Dec 2025", ["ar25_inv_raw", "ar25_inv_wip", "ar25_inv_fg", "ar25_gp", "ar25_is_sales"], S1, "High", "direct ratios; COGS = sales - gross profit")
ii("i_inv_h1", "Inventory days H1 2026 148 vs H1 2025 136 (H1 COGS x2); total inventories +27% in H1 2026", "148 / 136", "days", "H1 FY2026", "30 Jun 2026",
   ["h126_inv", "h126_cogs", "h125_inv"], S1, "Medium", "annualising half-year COGS")
ii("i_dso", "DSO on trade & other receivables (net, financial assets) / half-year sales: YE2024 57, H1 2025 50, YE2025 53, H1 2026 59 days", "57/50/53/59", "days",
   "YE2024-H1 FY2026", "Dec 2024-Jun 2026", ["h125_tr", "h126_tr25", "h126_tr", "h126_is_sales", "ar25_is_sales"], S1, "Medium", "half-year sales x days; receivable line includes small sundry items")
ii("i_dso_fy", "DSO on trade receivables net / FY sales: FY2025 50 days, FY2024 63 days", "50 / 63", "days", "FY2025; FY2024", "2025; 2024", ["ar25_tr", "ar25_is_sales"], S1, "High", "direct")
ii("i_cl", "Contract liabilities / LTM sales: YE2025 3.1%, 30 Jun 2026 4.5%", "3.1% / 4.5%", "%", "FY2025; H1 FY2026", "Dec 2025; Jun 2026", ["h126_cl", "ar25_is_sales", "h126_is_sales"], S1, "High", "direct")
ii("i_china", "China share of group net sales: 2020 13.9%, 2021 19.2%, 2022 18.1%, 2023 27.2%, 2024 27.0%, 2025 25.1%", "25.1% (FY2025)", "%", "FY2020-FY2025", "2020-2025",
   ["ar25_china", "ar24_china", "ar23_china", "ar21_china", "ar25five_sales", "ar21five_sales"], S1, "High", "customer-location basis; Korea/Taiwan not split out")
ii("i_geo", "FY2025: Asia 63.4%, Malaysia 15.6%, North America 17.8%, Europe 17.1%; North America fell from 37.8% (FY2022) to 23.3% (FY2023) as Malaysia appeared", "63.4% Asia", "%",
   "FY2025", "Jan-Dec 2025", ["ar25_asia", "ar25_mal", "ar25_na", "ar25_eu", "ar23_na", "ar24_mal"], S1, "High", "direct ratios")
ii("i_geo_h1", "Asia share H1 2026 67.5% vs H1 2025 63.8% and H2 2025 63.0%", "67.5%", "%", "H1 FY2026", "Jan-Jun 2026", ["h126_asia", "h126_is_sales", "ar25_asia"], S1, "High", "direct")
ii("i_semi", "Semiconductor share by company sector labels: PCT 'Semiconductor' 52.8% of group sales FY2025 (50.9% FY2024); with IXS 'Electronics' 61.6%", "52.8% / 61.6%", "%",
   "FY2025", "Jan-Dec 2025", ["ar25_semi", "ar25_elec", "ar25_is_sales"], S1, "Medium", "company does not publish a group semi or AI share for FY2025; IXM semi sales not split")
ii("i_netdebt", "Net debt incl. leases 30 Jun 2026: +19.3m (net debt) vs YE2025 -5.3m (net cash); ex leases net cash 10.1m; net debt / LTM EBITDA 0.35x vs 3:1 covenant", "19.3", "CHF m",
   "H1 FY2026", "30 Jun 2026", ["h126_cash", "h126_debt", "h126_lease_c", "h126_lease_nc", "ar25_netdebt", "ar25_cov"], S1, "Medium", "covenant definition of leverage not disclosed; company debt factor +0.6 likely on H1 EBITDA")
ii("i_ors", "ORS: goodwill 52% of the CHF 9.0m price; no goodwill impairment since (IXS CGU passes FY2025 test)", "52%", "%", "FY2020-FY2025", "2020-2025", ["ar21_ors_price", "ar21_ors_gw", "ar25_imptest"], S1, "High", "direct")
ii("i_xp", "XP Power amounts at stake before success fee: USD 40m damages + ~USD 19m fees/interest = ~USD 59m (~CHF 48m at 0.809) - none recognised; judgment vacated Jul 2026", "~59", "USD m",
   "FY2026", "Jul 2026", ["ar25_xp", "ar25_xpfees", "h126_xp", "h126_xp2"], S1, "Medium", "post-judgment interest and success fee % not disclosed")
ii("i_guid", "Guidance record FY2022-FY2025 (8 items): vs initial numeric guidance 0 beat / 2 in-line / 6 miss; vs last guidance before results 1 beat / 4 in-line / 3 miss", "0/2/6; 1/4/3", "count",
   "FY2022-FY2025", "2022-2025", ["g22ini", "g22jul", "g22oct", "ar25five_margin", "g23apr", "g23jul", "g23oct", "g24ini", "g24oct", "pr24", "g25ini", "g25jul", "g25oct", "ar25_is_sales", "ar25is_ebitda"], S2, "High", "range test, reported basis")
ii("i_late", "Guidance maintained late in the period then missed: FY2022 margin (21-23% confirmed Oct 2022, 20.3%); FY2024 margin (lower end of 15-17% Oct 2024, 13.6%); FY2025 sales (lower end of 460-500 Oct 2025, 457.0); FY2018 (Aug 2018, both)", "4 cases", "count",
   "FY2018-FY2025", "2018-2025", ["g22oct", "ar22adj", "g24oct", "q424", "pr24", "g25oct", "ar25_is_sales", "g18", "p19ifrs16"], S2, "High", "range test; FY2022 margin in-line only on company-adjusted basis")
ii("i_fy26_q4", "FY2026 Oct guidance implies Q4 2026 net sales CHF 174.5-194.5m (Q3 2026: 155.6; Q4 2025: 127.4)", "174.5-194.5", "CHF m", "Q4 FY2026", "Oct-Dec 2026", ["g26oct", "q326_9m"], S2, "High", "subtraction")
ii("i_cyc1", "2018-19 downturn: half-year net sales H1 2018 -> H1 2019 -23.8%; EBITDA margin 13.8% -> 4.8% (-9.0pp); annual FY2017 -> FY2019 -16.2%", "-23.8%; -9.0pp", "%",
   "H1 FY2018-H1 FY2019", "Jan 2018-Jun 2019", ["h119_sales", "h119_ebitda", "ar21five_sales", "ar21five"], S3, "High", "IFRS16 basis both ends")
ii("i_cyc2", "2022-24 downturn: H2 2022 -> H1 2024 net sales -40.6%; EBITDA margin 25.5% -> 6.9% (-18.6pp); quarterly Q3 2022 -> Q3 2023 -52.9%; FY2022 -> FY2023 -32.2%", "-40.6%; -18.6pp", "%",
   "H2 FY2022-H1 FY2024", "Jul 2022-Jun 2024", ["ar25five_sales", "ar25five_ebitda", "h122", "h122_ebitda", "h124", "h124_ebitda", "q323_sales"], S3, "High", "H2 2022 derived = FY - H1")
ii("i_cyc3", "2024-25 soft patch: H2 2024 -> H1 2025 net sales -11.3%, EBITDA margin 17.6% -> 10.1% (restated); Q4 2024 -> Q3 2025 -28.3%", "-11.3%; -7.5pp", "%",
   "H2 FY2024-H1 FY2025", "Jul 2024-Jun 2025", ["ar25_is_sales", "ar25is_ebitda", "h124", "h124_ebitda", "h126_restate_ebitda", "q325_sales"], S3, "Medium", "H2 2024 absorbs the FY2024 restatement (H1 2024 not restated)")
ii("i_recov", "Q3 2026 net sales (155.6) still 5.6% below the Q3 2022 peak quarter (164.8)", "-5.6%", "%", "Q3 FY2026", "Jul-Sep 2026", ["q326_sales", "q323_sales"], S3, "High", "direct")

# ---------------------------------------------------------------------------------------------
def norm(s):
    s = s.replace("­", "").replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"').replace("–", "-").replace("—", "-")
    s = s.replace("ﬁ", "fi").replace("ﬂ", "fl")
    return re.sub(r"\s+", " ", s).strip().lower()

def squash(s):
    return re.sub(r"[^a-z0-9%.]", "", norm(s))

manifest = {}
with open(os.path.join(ROOT, SRC, "_manifest.csv"), encoding="utf-8") as f:
    for m in csv.DictReader(f):
        if m.get("status") == "RETRIEVED":
            manifest[m["local_file"]] = m

def pages_for(local, quote):
    tp = os.path.join(ROOT, SRC, "_text", os.path.splitext(os.path.basename(local))[0] + ".txt")
    texts = open(tp, encoding="utf-8", errors="replace").read().split("\f")
    nq, sq = norm(quote), squash(quote)
    p = [i for i, t in enumerate(texts, 1) if nq in norm(t)]
    if not p and len(sq) >= 12:
        p = [i for i, t in enumerate(texts, 1) if sq in squash(t)]
    return p

ids, out, missing = {}, [], []
n = 0
for row in R[:RX_START]:
    n += 1
    ids[row[0]] = f"A-{n:03d}"
for it in I:
    n += 1
    ids[it[0]] = f"A-{n:03d}"
for row in R[RX_START:]:
    n += 1
    ids[row[0]] = f"A-{n:03d}"

for (key, tag, claim, value, unit, pf, pc, fk, quote, conf, note) in R:
    stem, doc = F[fk]
    local = SRC + stem
    m = manifest.get(local, {})
    url = m.get("url", "")
    date = m.get("date", "")
    if local.endswith(".html"):
        pg = pages_for(local, quote)
        pos = "web page text" if pg else "NOT FOUND"
    else:
        pg = pages_for(local, quote)
        pos = f"p{pg[0]}" if pg else "NOT FOUND"
    if not pg:
        missing.append((key, fk, quote))
    if fk in NEWSWIRE and tag == "[F]":
        tag = "[S]"
    if "web.archive" in url:
        note = (note + "; " if note else "") + "archived copy"
    out.append([ids[key], tag, claim, value, unit, pf, pc, doc, date, pos, url, local, quote, conf, note])

for (key, claim, value, unit, pf, pc, inputs, script, conf, reason) in I:
    bad = [k for k in inputs if k not in ids]
    if bad:
        missing.append((key, "INPUT", ",".join(bad)))
    inp = " ".join(ids[k] for k in inputs if k in ids)
    out.append([ids[key], "[I]", claim, value, unit, pf, pc, "calculation", "2026-11-21", script.split("/")[-1], "", "", "",
                conf, f"inputs: {inp}; script: {script}; {conf}: {reason}"])

out.sort(key=lambda o: o[0])
dst = os.path.join(ROOT, "research/out/comet/parts/A.csv")
with open(dst, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["id", "tag", "claim", "value", "unit", "period_fiscal", "period_calendar", "document", "date", "page_or_section",
                "url", "local_file", "quote", "confidence", "note"])
    w.writerows(out)
tags = {}
for o in out:
    tags[o[1]] = tags.get(o[1], 0) + 1
print(f"wrote {len(out)} rows to {dst}: {tags}")
for mm in missing:
    print("MISSING:", mm)
with open(os.path.join(ROOT, "research/out/comet/calc/A_idmap.txt"), "w") as f:
    for k, v in ids.items():
        f.write(f"{k}\t{v}\n")
