# Gaps - Advantest

Advantest Corporation, TSE Prime 6857. The fiscal year ends 31 March and is named by its start year (FY2026 = Apr 2026-Mar 2027). Every NOT DISCLOSED and NOT RETRIEVED item from the module parts, their verify logs, B3 and the source manifest, one line each and deduplicated; merged lines say which modules logged them. Built by `calc/B4_gaps_merge.py` (log in `calc/B4_gaps_merge.out.txt`).

## Files the user can save by hand

These documents were refused to scripts, paywalled or not found by script. A person can open each in a browser and save it to `research/sources/advantest/` under the name shown (use the date printed in the document where the name says so).

- Advantest, Notice Regarding Issuance of Zero Coupon Convertible Bonds Due 2031 (1 Apr 2026): https://www.advantest.com/document/en/investors/aad/E_Info_20260401_02.pdf -> `2026-04-01_advantest_press-release-E-Info-20260401-02-CB-issuance.pdf` (CB early-redemption terms, lock-up)
- Advantest, Supplemental Materials regarding the CB issuance (1 Apr 2026): https://www.advantest.com/document/en/investors/aad/E_Info_20260401_03.pdf -> `2026-04-01_advantest_press-release-E-Info-20260401-03-CB-supplemental.pdf`
- Advantest, Notice on Determination of Terms of Issue of the CB (1 Apr 2026): https://www.advantest.com/document/en/investors/aad/E_Info_20260401_04.pdf -> `2026-04-01_advantest_press-release-E-Info-20260401-04-CB-terms.pdf` (lock-up terms)
- BIS, updated FAQs for the Oct 7 advanced computing and SME rule (25 Jan 2023), FAQ II.A.1 on the back-end exclusion: https://www.bis.doc.gov/index.php/documents/product-guidance/3211-2023-1-25-updated-faqs-for-oct-7-advanced-computing-and-semiconductor-manufacturing-equipment-rule/file -> `2023-01-25_bis_FAQ-Oct7-advanced-computing-SME-rule.pdf`
- METI originals of Japan's export-list amendment adding advanced semiconductor manufacturing equipment (in force 23 Jul 2023) and any later METI semiconductor list changes: URL not identified (meti.go.jp refused scripts; start from METI's security export control pages) -> `<printed date>_meti_export-control-list-amendment-SME.pdf`
- sec.gov (no contact User-Agent this run): Teradyne annual report 10-K for 2025, https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=TER&type=10-K -> `<filing date>_teradyne_annual-report-10-K-2025.htm`
- sec.gov: customer filings that may name Advantest as a supplier, NVIDIA 10-K https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=NVDA&type=10-K and TSMC 20-F https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=TSM&type=20-F -> `<filing date>_nvidia_annual-report-10-K.htm`, `<filing date>_tsmc_annual-report-20-F.htm`
- sec.gov: Advantest's own 20-F for FY2007 (Apr 2007-Mar 2008), which carries FY2006 comparatives (the issuer's site returns HTTP 404 for E_FR_FY2007_FN.pdf): https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=advantest&type=20-F -> `<filing date>_advantest_annual-report-20-F-FY2007.htm`
- Bloomberg, 28 Apr 2026 (subscription): https://www.bloomberg.com/news/articles/2026-04-28/advantest-shares-decline-after-outlook-misses-on-tight-capacity -> `2026-04-28_bloomberg_press-Advantest-outlook-capacity.html` (FY2026 outlook and tight capacity)
- Bloomberg, 28 Jan 2026 (subscription): https://www.bloomberg.com/news/articles/2026-01-28/advantest-rushes-to-boost-ai-chip-tester-capacity-to-meet-demand -> `2026-01-28_bloomberg_press-Advantest-boost-AI-chip-tester-capacity.html`
- StreetInsider, UBS note on NVIDIA test dual sourcing (test-sourcing content only): https://streetinsider.com/Basic+Content/Nvidia+test+slot+could+send+this+stock+soaring%2C+UBS+says/25021163.html -> `<printed date>_streetinsider_press-UBS-note-NVIDIA-test-sourcing.html`
- TipRanks / Investing.com, Bernstein research note on Advantest (stated demand and margin arguments only): https://www.tipranks.com/news/the-fly/advantest-downgraded-to-market-perform-from-outperform-at-bernstein and https://ng.investing.com/news/analyst-ratings/bernstein-cuts-advantest-stock-rating-to-market-perform-slashes-target-93CH-1828631 -> `<printed date>_tipranks_press-Bernstein-note-Advantest.html` (one of the two is enough)
- XenoSpectrum, Teradyne Q3 2026 revenue plateau: https://xenospectrum.com/en/teradyne-q3-2026-revenue-plateau/ -> `<printed date>_xenospectrum_press-Teradyne-Q3-2026-revenue-plateau.html`
- XenoSpectrum, China memory / HBM test equipment: https://xenospectrum.com/en/china-memory-testing-hbm-equipment/ -> `<printed date>_xenospectrum_press-China-memory-testing-HBM-equipment.html`
- Nasdaq (Zacks), Teradyne semiconductor test segment: https://www.nasdaq.com/articles/ter-rides-strong-semiconductor-test-segment-more-upside-ahead-0 -> `<printed date>_nasdaq-zacks_press-TER-semiconductor-test-segment.html`
- In Practise and Seeking Alpha (paywalled): https://inpractise.com/articles/advantest-vs-teradyne-gpu-test-market-share-and-power-supply-advantage and https://seekingalpha.com/article/4837312-advantest-teradyne-market-share-shifts-in-this-duopoly -> `<printed date>_inpractise_press-Advantest-vs-Teradyne-GPU-test-share.html`, `<printed date>_seekingalpha_press-Advantest-Teradyne-share-shifts.html`
- PMC / MDPI Micromachines, Do et al. 2026 HBM packaging review (the script got a reCAPTCHA page): https://pmc.ncbi.nlm.nih.gov/articles/PMC13609547/ -> `<printed date>_mdpi-micromachines_paper-HBM-thermal-reliability-hybrid-bonding-review.pdf`
- Samsung Newsroom (HTTP 403 to the script): any Samsung release on HBM4 hybrid bonding and its test steps, starting from https://news.samsung.com/global/?s=HBM4+hybrid+bonding -> `<printed date>_samsung_press-release-HBM4-hybrid-bonding.html`
- TDnet (Japanese filings): the public list (https://www.release.tdnet.info/inbs/I_main_00.html) covers only the last month; 28 Oct-21 Nov 2026 was read by script (no Advantest forecast revision, A3-322). Advantest's Japanese filings of Jan 2024-Mar 2025 are outside it; a person can look for forecast-revision notices of that period on Advantest's Japanese-language IR news pages and save any found -> `<filing date>_advantest_tdnet-<title>.pdf`
- Not saveable from a known URL: the FY2022 Q1 Q&A summary (E_BIZ_220728_QA.pdf) and the FY2007 results release (E_FR_FY2007_FN.pdf) return HTTP 404; FormFactor (investors.formfactor.com) and TSMC (investor.tsmc.com) refused scripts but no specific document was identified; IEEE Xplore papers are paywalled.

## A1

NOT DISCLOSED (read: Q2 FY26 / Q1 FY26 / FY25 / Q3 FY25 earnings-briefing slides and notes; Q&A summaries FY2025 Q1-FY2026 Q2; Integrated Annual Report 2026 full text; Investors' Guide Oct 2026 Ch.1; Annual Securities Report 84th and Semi-Annual Securities Report 85th, business overview and Note 22 Revenue) - share of Advantest revenue tied to AI / HPC (the company gives only the "Computing / Communications" share of SoC tester sales, rounded to the nearest 5%, which also includes smartphone application processors, and says it does not disclose further; HBM and advanced packaging are logged separately below) (logged in: A1, TH)

NOT DISCLOSED (read: Q2 FY26 / Q1 FY26 / FY25 / Q3 FY25 earnings-briefing slides and notes, incl. the memory-tester application table on Q2 FY26 slide 16 and the FY2025 Tester Market Share Report; Investors' Guide Oct 2026 p.7; Q&A summaries FY2023 Q4 to FY2026 Q2; Integrated Annual Report 2026 full text; Annual Securities Report 84th and Semi-Annual Securities Report 85th, business overview and Note 22 Revenue) - HBM tester sales, HBM share of memory tester sales or of revenue, and an HBM-specific tester market share (HBM is named only qualitatively within high-performance DRAM; memory tester sales are split only into DRAM and non-volatile, rounded to 5%) (logged in: A1, TH, CL/B)

NOT DISCLOSED (read: Q2 FY26 / Q1 FY26 / FY25 / Q3 FY25 earnings-briefing slides and notes; Q&A summaries FY2024 Q3 to FY2026 Q2; MTP3 slides; Integrated Annual Report 2026 full text; Investors' Guide Oct 2026 Ch.1; Annual Securities Report 84th and Semi-Annual Securities Report 85th, business overview and Note 22 Revenue) - revenue or share of revenue tied to advanced packaging, including die-level / known-good-die or known-good-stack test (logged in: A1, TH)

NOT DISCLOSED (read: Q2 FY26 slide 15; Investors' Guide Oct 2026 p.5; FY2025 Q1 Q&A summary A6; Q3 FY2025 Q&A summary A4) - split of "Computing / Communications" SoC tester sales between HPC/AI and smartphone application processors, and of SoC tester sales between GPU, custom ASIC and CPU customers (logged in: A1, TH)

NOT DISCLOSED (read: Q2 FY26 slides 15-16, Investors' Guide p.5 and p.7) - application split of SoC and memory tester sales for individual quarters or LTM (only fiscal-year splits, rounded to the nearest 5%)

NOT DISCLOSED (read: Annual Securities Report 84th, Business Risks p.38 and Note 22 Revenue; Semi-Annual Securities Report 85th, segment and revenue notes; Integrated Annual Report 2026 p.35; MTP3 slides p.20; Q2 FY26 slides 6 and 17; FY2025 and FY2026 Q2 tanshin segment notes) - recurring revenue amount, share or definition (the company names "recurring revenue offerings" and "Boost Recurring" business only qualitatively)

NOT DISCLOSED (read: FY25 and FY24 Q4 summary slides p.5; Q2 FY26, Q1 FY26 and Q3 FY25 summary slides; tanshin FY2025, FY2026 Q1 and FY2026 Q2; Annual Securities Report 84th MD&A) - company-adjusted (non-IFRS) gross margin (the only adjusted measure published is core operating income, full years only)

NOT DISCLOSED (read: quarterly summary tables in Q2 FY26, Q1 FY26 and Q3 FY25 slides; tanshin FY2025 Q3, FY2026 Q1, FY2026 Q2) - company "core operating income" for single quarters or half years (published only in full-year summary slides FY24, FY25)

NOT DISCLOSED (read: all tanshin, slides, notes and securities reports listed in A1.csv) - adjusted (non-IFRS) EPS or adjusted net income

NOT DISCLOSED (read: FY2025 Q4 slides p.7 quarterly table, FY26 forecast table p.20; FY2025 tanshin overview p.19; FY2024 Q4 slides) - single-quarter basic EPS for FY2025 Q4 (Jan-Mar 2026) and FY2024 Q4 (Jan-Mar 2025; derived by YTD difference in calc only)

NOT DISCLOSED (read: FY2025 Q4 briefing notes p.6 and Q&A; FY2025 Q4 slides; FY2025 tanshin; Annual Securities Report 84th MD&A and Note 23 SG&A p.161) - amount of the "one-off expenses related to business operations" in FY2025 Q4 (Jan-Mar 2026) SG&A (logged in: A1, A3, A5)

NOT DISCLOSED (read: Q1 FY2026 briefing notes p.5 and Q&A summary A9; Q2 FY2026 briefing notes and Q&A summary A5; Q1 and Q2 FY2026 briefing slides; FY2026 Q1 and Q2 Consolidated Financial Results (tanshin); Semi-Annual Securities Report 85th, notes 1-13 (no inventories note); Integrated Annual Report 2026; IR Fireside Chat script and Q&A 2026-11-12) - amount of the reversal of inventory write-down / obsolescence that management named for FY2026 Q1 (Apr-Jun 2026) and for 1H FY2026 (Apr-Sep 2026), the line it was booked in, and whether any part fell in FY2026 Q2 (Jul-Sep 2026); margins without it cannot be computed for FY2026 Q1, Q2, 1H and the LTM (logged in: A1, A2, A3, A5, CL/B)

NOT DISCLOSED (read: FY2025 tanshin notes; Annual Securities Report 84th, Note 15(3) tax-rate reconciliation p.146 and MD&A p.50; FY2026 Q1 and Q2 tanshin; Semi-Annual Securities Report 85th) - tax effect of the named one-off items (impairment, divestiture gain, call-option gain, valuation gains), so net income and the total return ratio cannot be shown without them (logged in: A1, A5)

NOT DISCLOSED (read: FY2026 Q1 and Q2 tanshin cash flow statements; Semi-Annual Securities Report 85th cash flow statement) - share-based compensation expense as a separate cash-flow line for interim periods (taken from the segment reconciliation instead)

NOT DISCLOSED (read: Annual Securities Report 84th, Non-Consolidated Financial Statements pp.185-193 incl. balance sheet, significant accounting policies (5) and statement-of-operations note *1, and Note 24 Share-Based Compensation pp.161-165) - reconciliation of parent-only J-GAAP "share-based compensation expense" of JPY 26,134 million (FY2025, Apr 2025-Mar 2026) to the consolidated IFRS expense of JPY 4,450 million

NOT DISCLOSED (read: Q2 FY26 slides p.9 and p.14; FY25 Q4 slides; briefing notes) - basis of the company's "Capital Expenditure" figure (differs from cash purchases of PP&E and intangibles)

NOT DISCLOSED (read: FY2025 Q4 notes p.7; Q2 FY26 slide 9; FY25 Q4 slide 11; FY2025 tanshin) - reason for the JPY 0.1 bn difference between the company's FY2025 Q4 (Jan-Mar 2026) FCF (106.3 bn; investing CF -10.3 bn) and FCF derived from YTD cash flow statements (106.4 bn; investing CF -10.2 bn)

NOT DISCLOSED (read: FY2025 Q3, FY2025 tanshin and FY2026 Q2 tanshin segment notes) - single-quarter segment income (published only YTD; single quarters derived by differencing in calc)

NOT DISCLOSED (read: all A1 sources) - a separate Mechatronics System segment for any period from FY2025 Q1 (Apr-Jun 2025) onward, including restated comparatives (segment abolished; handlers sit in Test System "Other Systems")

NOT DISCLOSED (read: Q3 FY2025 briefing notes and Q&A summary; FY2025 Q3 tanshin segment notes) - any management-named one-off item in FY2025 Q3 (Oct-Dec 2025); none named

NOT DISCLOSED (read: FY2025 Q2 earnings briefing notes p.3 Summary and p.9; FY2025 Q2 Q&A summary; FY2025 Q2 slides; FY2025 Q2 tanshin) - an amount printed expressly for the FY2025 Q2 (Jul-Sep 2025) "one time charge related to a growth investment" (logged in: A1, A3)

NOT DISCLOSED (read: IR library report index 2026-11-21; Semi-Annual Securities Report 83rd (1H FY2024), Basis of Preparation (cites only Article 24-5 of the Financial Instruments and Exchange Act for the semi-annual report)) - reason the company files no Quarterly Securities Reports from FY2024 (Apr 2024-Mar 2025; Q1 and Q3 figures come from tanshin and briefing materials)


## A2

NOT DISCLOSED (read: FY2025 Q1 financial briefing slides, notes and Q&A summary 2025-07-29; financial results FY2025 Q1) - orders received, total, FY2025 Q1 (Apr-Jun 2025)

NOT DISCLOSED (read: FY2025 Q2 financial briefing slides, notes and Q&A summary 2025-10-28; financial results FY2025 Q2; semi-annual securities report 84th) - orders received, total, FY2025 Q2 (Jul-Sep 2025)

NOT DISCLOSED (read: FY2025 Q3 financial briefing slides, notes and Q&A summary 2026-01-28; financial results FY2025 Q3) - orders received, total, FY2025 Q3 (Oct-Dec 2025)

NOT DISCLOSED (read: FY2025 Q4 financial briefing slides, notes and Q&A summary 2026-04-27; financial results FY2025; annual securities report 84th, "Results of Production, Orders Received and Sales") - orders received, total, FY2025 Q4 (Jan-Mar 2026) and FY2025 (Apr 2025-Mar 2026) full year

NOT DISCLOSED (read: FY2026 Q1 financial briefing slides, notes and Q&A summary 2026-07-29; financial results FY2026 Q1) - orders received, total, FY2026 Q1 (Apr-Jun 2026)

NOT DISCLOSED (read: FY2026 Q2 financial briefing slides, notes and Q&A summary 2026-10-28; financial results FY2026 Q2; semi-annual securities report 85th) - orders received, total, FY2026 Q2 (Jul-Sep 2026)

NOT DISCLOSED (read: financial results FY2025 Q1, briefing slides FY2025 Q1) - order backlog at 30 Jun 2025 (FY2025 Q1 end)

NOT DISCLOSED (read: financial results FY2025 Q2, briefing slides FY2025 Q2, semi-annual securities report 84th) - order backlog at 30 Sep 2025 (FY2025 Q2 end)

NOT DISCLOSED (read: financial results FY2025 Q3, briefing slides FY2025 Q3) - order backlog at 31 Dec 2025 (FY2025 Q3 end)

NOT DISCLOSED (read: financial results FY2025, briefing slides FY2025 Q4, annual securities report 84th) - order backlog at 31 Mar 2026 (FY2025 end)

NOT DISCLOSED (read: financial results FY2026 Q1, briefing slides FY2026 Q1) - order backlog at 30 Jun 2026 (FY2026 Q1 end)

NOT DISCLOSED (read: financial results FY2026 Q2, briefing slides FY2026 Q2, semi-annual securities report 85th) - order backlog at 30 Sep 2026 (FY2026 Q2 end)

NOT DISCLOSED (read: briefing slides and Q&A summaries FY2025 Q1 to FY2026 Q2) - company-stated book-to-bill ratio, any quarter FY2025 Q1 to FY2026 Q2 (Apr 2025-Sep 2026; cannot be computed because orders are not disclosed)

NOT DISCLOSED (read: annual securities report 84th, sales results by segment and note 6; briefing slides FY2025 Q1 to FY2026 Q2, segment pages) - orders received by segment (SoC test systems, memory test systems, other systems incl. handlers, services and others), FY2025 Q1 to FY2026 Q2 (Apr 2025-Sep 2026)

NOT DISCLOSED (read: annual securities report 84th; briefing slides FY2025 Q1 to FY2026 Q2) - order backlog by segment, any quarter-end 30 Jun 2025 (FY2025 Q1 end) to 30 Sep 2026 (FY2026 Q2 end)

NOT DISCLOSED (read: annual securities report 84th, note 22 item 3 Transaction Price Allocated to the Remaining Performance Obligations) - amount of remaining performance obligations at 31 Mar 2026 (FY2025 end) (practical expedient used)

NOT DISCLOSED (read: Q&A summaries FY2025 Q3, FY2025 Q4, FY2026 Q1, FY2026 Q2; briefing notes FY2025 Q1 to FY2026 Q2; IR fireside chat script and Q&A 2026-11-12; annual securities report 84th, business risks) - current product lead time in months (latest figure found is about six months, Jul 2023)

NOT DISCLOSED (read: Q&A summaries FY2025 Q3, FY2025 Q4, FY2026 Q1, FY2026 Q2; briefing notes FY2025 Q3 to FY2026 Q2) - any statement on order cancellations or customer-requested delivery postponements, FY2025 Q3 to FY2026 Q2 (Oct 2025-Sep 2026)

NOT DISCLOSED (read: financial results FY2025 Q1 balance sheet) - inventory split raw materials / work in process / finished goods at 30 Jun 2025 (FY2025 Q1 end)

NOT DISCLOSED (read: financial results FY2025 Q2 balance sheet; semi-annual securities report 84th, condensed statements and notes) - inventory split raw materials / work in process / finished goods at 30 Sep 2025 (FY2025 Q2 end)

NOT DISCLOSED (read: financial results FY2025 Q3 balance sheet) - inventory split raw materials / work in process / finished goods at 31 Dec 2025 (FY2025 Q3 end)

NOT DISCLOSED (read: financial results FY2026 Q1 balance sheet) - inventory split raw materials / work in process / finished goods at 30 Jun 2026 (FY2026 Q1 end)

NOT DISCLOSED (read: financial results FY2026 Q2 balance sheet; semi-annual securities report 85th, condensed statements and notes 1-13, note 8 Revenue has no contract balances) - inventory split raw materials / work in process / finished goods at 30 Sep 2026 (FY2026 Q2 end)

NOT DISCLOSED (read: semi-annual securities report 85th, notes 1-13; financial results FY2026 Q1 and Q2) - inventory valuation losses for 1H FY2026 (Apr-Sep 2026) or for any single quarter

NOT DISCLOSED (read: Integrated Annual Report 2026, 11-Year Financial Highlights p.77 and footnotes *1-*5, p.35; annual securities report 84th, p.38; MTP3 slides 2024-06-25 p.33) - definition and formula of the company-reported cash conversion cycle

NOT DISCLOSED (read: annual securities report 84th, note 4 item 1 Valuation of Inventories p.128 and key audit matter p.205) - share of raw materials with a particularly long turnover period at 31 Mar 2026 (FY2025 end) (the 83rd report gave about 9% at 31 Mar 2025 (FY2024 end))

NOT DISCLOSED (read: annual securities report 84th, business risks and note 9; Integrated Annual Report 2026, CFO message and supply-chain section; IR fireside chat script and Q&A 2026-11-12) - amount of strategic inventory, DDR4 DRAM stock or die-bank wafers within inventories

NOT DISCLOSED (read: financial results FY2025 Q1, balance sheet and cash flows) - contract liabilities (advance receipts) balance at 30 Jun 2025 (FY2025 Q1 end)

NOT DISCLOSED (read: financial results FY2025 Q2; semi-annual securities report 84th) - contract liabilities (advance receipts) balance at 30 Sep 2025 (FY2025 Q2 end)

NOT DISCLOSED (read: financial results FY2025 Q3) - contract liabilities (advance receipts) balance at 31 Dec 2025 (FY2025 Q3 end)

NOT DISCLOSED (read: financial results FY2026 Q1) - contract liabilities (advance receipts) balance at 30 Jun 2026 (FY2026 Q1 end)

NOT DISCLOSED (read: financial results FY2026 Q2; semi-annual securities report 85th, condensed statements and notes 1-13, note 8 Revenue has no contract balances) - contract liabilities (advance receipts) balance at 30 Sep 2026 (FY2026 Q2 end)

NOT DISCLOSED (read: annual securities report 84th, note 22 Revenue) - split of contract liabilities between equipment prepayments and service/maintenance prepayments

NOT DISCLOSED (read: financial results FY2025 Q1 to FY2026 Q2; semi-annual securities reports 84th and 85th) - trade receivables excluding other receivables at quarter-ends other than 31 Mar

NOT DISCLOSED (read: financial results, briefing slides FY2025 Q1 to FY2026 Q2; Integrated Annual Report 2026) - company-stated days sales outstanding

NOT DISCLOSED (read: annual securities report 84th, notes 9, 11, 13, 16, 22 and 30, business risks p.42; full-text search for 'commitment' and 'purchase obligation') - purchase commitments / purchase obligations for materials and components (amount and maturity); capex commitments are the only commitments quantified

NOT DISCLOSED (read: annual securities report 84th, business risks, supply chain risk mitigation) - amounts and durations of long-term procurement contracts

NOT DISCLOSED (read: Q&A summary FY2026 Q1 A6; IR fireside chat script and Q&A 2026-11-12; annual securities report 84th) - purchase or capacity commitments to the contract manufacturer (EMS partner)

NOT DISCLOSED (read: semi-annual securities report 84th, condensed statements and notes) - commitments related to acquisition of fixed assets at 30 Sep 2025 (FY2025 Q2 end)

NOT DISCLOSED (read: semi-annual securities report 85th, condensed statements and notes 1-13, note 8 Revenue has no contract balances) - commitments related to acquisition of fixed assets at 30 Sep 2026 (FY2026 Q2 end)

NOT DISCLOSED (read: Q&A summary FY2026 Q2 A1) - quantitative CY2027 tester market outlook (company said it will give one at the FY2026 Q3 (Oct-Dec 2026) briefing, Jan 2027)

NOT DISCLOSED (read: briefing slides FY2026 Q2 p.14; Q&A summary FY2026 Q2 A4) - separate FY2026 Q3 and Q4 (Oct-Dec 2026 and Jan-Mar 2027) sales forecasts (only the 2H total is given)

NOT RETRIEVED (tried: https://www3.advantest.com/investors/pdf/E_BIZ_220728_QA.pdf - HTTP 404) - FY2022 Q1 (Apr-Jun 2022) Q&A summary (context only: first quarter after orders disclosure ended) (logged in: A2, manifest)

NOT DISCLOSED (read: FY2025 Consolidated Financial Results (tanshin), financial position and cash-flow overview; FY2025 Q4 briefing slides, notes and Q&A summary; FY2026 Q1 Consolidated Financial Results and briefing notes) - reason for the peak in trade and other receivables at 31 Mar 2026 (FY2025 end; JPY 228,731 m [F] (A2-093), DSO 63.6 days [I] Medium (A2-104)); the documents state only the increase and the following decrease


## A3

NOT DISCLOSED (read: FY2024 Q1-FY2026 Q2 earnings briefing slides, forecast slides; FY2024 Q4 slides p.19 and FY2025 Q4 slides p.20 (full-year forecast only); FY2025 Q3 briefing notes, Summary) - Q1 or Q3 single-quarter guidance

NOT DISCLOSED (read: tanshin "Earnings Forecast" tables of 2023-04-26, 2023-07-26, 2023-10-31, 2024-01-31, 2024-04-26, 2024-07-31) - basic EPS guidance before 2024-10-30 (none for FY2023 (Apr 2023-Mar 2024), none in the FY2024 (Apr 2024-Mar 2025) initial or Q1 versions)

NOT DISCLOSED (read: FY2021 Q4-FY2026 Q2 earnings briefing slides, forecast slides; FY2022 Q2 Q&A, per A2-001/A2-007) - orders or backlog guidance (orders not disclosed since FY2021 Q4 (Jan-Mar 2022))

NOT DISCLOSED (read: FY2024 Q4 slides p.4; FY2025 Q4 slides p.5, forecast column) - guidance for core operating income (the forecast column shows "-")

NOT DISCLOSED (read: FY2023 Consolidated Financial Results, 1.(1) Overview and Segment information note 6; 82nd Annual Securities Report, Income taxes) - after-tax effect of the FY2023 Q4 (Jan-Mar 2024) goodwill impairment of 8,998 million (no fully adjusted FY2023 (Apr 2023-Mar 2024) net income)

NOT DISCLOSED (read: FY2024 Consolidated Financial Results, 1.(1) Overview and Segment information note 2; FY2024 Q4 slides and Q&A; 83rd Annual Securities Report, Income taxes p.49 and note 15 p.146) - exact after-tax effect of the FY2024 Q4 (Jan-Mar 2025) impairment of 21,393 million (company says the losses were not tax-deductible, A3-316; adjusted FY2024 (Apr 2024-Mar 2025) NI is shown only as a bound, A3-317)

NOT DISCLOSED (read: FY2024 Q3 tanshin 1.(4) Outlook; Revision of Earnings Forecast notice 2025-01-29) - whether the January 2025 FY2024 (Apr 2024-Mar 2025) guidance included the Q4 impairment

NOT DISCLOSED (read: FY2023 Q3 tanshin 1.(4) Outlook) - whether the January 2024 FY2023 (Apr 2023-Mar 2024) guidance included the Q4 goodwill impairment

NOT DISCLOSED (read: MTP3 press release 2024-06-25; MTP3 target revision 2025-10-28; Integrated Annual Report 2026, p.22) - FY2026 (Apr 2026-Mar 2027) ROIC forecast and the averaging method for the three-year OPM/ROIC targets (mean of annual figures vs pooled)

NOT DISCLOSED (read: FY2025 Q4 slides, MTP3 progress pages; Integrated Annual Report 2026, p.21-22; FY2026 Q2 slides) - company-computed MTP3 three-year average status (only FY2024 (Apr 2024-Mar 2025) and FY2025 (Apr 2025-Mar 2026) annual results are shown)

NOT DISCLOSED (read: MTP3 press release 2024-06-25 p.3; MTP3 slides 2024-06-25 p.31; 82nd Annual Securities Report p.18; FY2024 Q4 slides p.16; Integrated Annual Report 2026 p.77) - reconciliation of the MTP2 (FY2021-FY2023, Apr 2021-Mar 2024) average ROIC figure (21.2% in the press release and securities report vs 25.5% in both slide decks; the IAR annual series averages 25.5%)

NOT DISCLOSED (read: FY2026 Q2 tanshin 1.(4) Outlook; FY2026 Q2 briefing notes, FY2026 Forecast) - breakdown of the financial income assumed in the FY2026 2H (Oct 2026-Mar 2027) guidance

NOT RETRIEVED (tried: https://www.release.tdnet.info/inbs/I_main_00.html and the public daily lists https://www.release.tdnet.info/inbs/I_list_<page>_<YYYYMMDD>.html for 28 Oct-21 Nov 2026 - 121 plain GET requests 2026-11-21, all HTTP 200, read by calc/A3_tdnet_scan.py (no Advantest forecast revision in that window, A3-322); the public list covers only 22 Oct-21 Nov 2026, so earlier filings are outside it, and its company search is a form, not used) - Advantest's Japanese TDnet filings for FY2023 Q4 to FY2024 Q4 (Jan 2024-Mar 2025), to check for forecast revisions not listed on the English IR news indexes


## A4

NOT DISCLOSED (read: Semi-Annual Securities Report 85th term, 1H FY2026, notes 5 Segment Information and 8 Revenue) - customers above 10% of net sales (names, amounts), 1H FY2026 (Apr-Sep 2026)

NOT DISCLOSED (read: Semi-Annual Securities Report 84th term, 1H FY2025, notes 5 Segment Information and 8 Revenue) - customers above 10% of net sales (names, amounts), 1H FY2025 (Apr-Sep 2025)

NOT DISCLOSED (read: Q1 FY26 and Q2 FY26 financial results, briefing slides, notes and Q&A summaries) - customers above 10% of net sales for any single quarter, FY2025 Q3 to FY2026 Q2 (Oct 2025-Sep 2026)

NOT DISCLOSED (read: Annual Securities Report 84th term, note 6(6) Information of Main Customers, Item 2 note 2 sales by major counterparties, and risk factor e. Customer Portfolio) - names and amounts of the three other top-five customers, FY2025 (Apr 2025-Mar 2026; only "approximately 50%" for the top five as a group)

NOT DISCLOSED (read: Annual Securities Report 84th term, risk factor e. Customer Portfolio) - whether the top-five customer share counts customer groups or single legal entities

NOT DISCLOSED (read: Annual Securities Report 84th term, note 6(6) Information of Main Customers and Item 2 note 2) - FY2024 (Apr 2024-Mar 2025) net sales to the NVIDIA Group or NVIDIA International, Inc. (below 10%, not named for FY2024)

NOT DISCLOSED (read: Annual Securities Report 84th term, note 6(6) and Item 2 note 2; Annual Securities Report 83rd term, note 6(6)) - net sales to the Samsung Group or Samsung Electronics Co., Ltd. in FY2025 (Apr 2025-Mar 2026; below the 10% threshold, amount not given)

NOT DISCLOSED (read: FY2026 Q2, FY2026 Q1, FY2025 Q3 financial results (tanshin), all sections) - quarterly net sales by region on the customer-location basis (quarterly releases carry no region table; only the ship-to slide chart)

NOT DISCLOSED (read: Semi-Annual Securities Reports 85th and 84th terms, note 8 Revenue) - the basis (ship-to or customer location) of the semi-annual "main regions" table

NOT DISCLOSED (read: Semi-Annual Securities Report 85th term, note 8 Revenue) - Taiwan, China and South Korea split of Asia net sales for 1H FY2026 (Apr-Sep 2026; only Japan / Americas / Europe / Asia given)

NOT DISCLOSED (read: Q2 FY26, Q1 FY26, FY25, Q3 FY25 briefing slides p.6-9 and briefing notes) - quarterly sales by region split by segment or by SoC / memory tester

NOT DISCLOSED (read: Annual Securities Report 84th term, risk factors c. Politics & Geopolitics and d. Trade Compliance; IR Business Risks web page 2026-11-21; Integrated Annual Report 2026 risk table; Semi-Annual Securities Report 85th term, Risk Factors) - which specific export rules bind Advantest (US EAR Entity List, foreign direct product rules, advanced-computing / semiconductor-manufacturing-item rules), the ECCN classification of its testers and their US-origin content

NOT DISCLOSED (read: all 179 saved Advantest documents 2009-2026, term search in calc/A4_rule_scan.py for "Foreign Exchange and Foreign Trade", "FEFTA", "METI", "Ministry of Economy") - any company statement on Japan's Foreign Exchange and Foreign Trade Act or METI export-list changes (METI appears only in "White 500" certification news titles)

NOT DISCLOSED (read: all 179 saved Advantest documents 2009-2026, term search in calc/A4_rule_scan.py for "MOFCOM", "unreliable entity", "gallium", "germanium", "rare earth") - any company statement on Chinese export controls or counter-measures

NOT DISCLOSED (read: Annual Securities Reports 83rd and 84th terms, risk factors; earnings-call Q&A summaries FY2022 Q2 to FY2026 Q2) - sales to Entity List / Footnote 5 entities, export licences applied for, granted or denied, and revenue affected by export controls

NOT DISCLOSED (read: Q1 FY26 earnings-call Q&A summary, A10) - period and basis (ship-to or customer location) of the "approximately 19%" China share

NOT DISCLOSED (read: Annual Securities Report 84th term, note 6(1) Overview of Reportable Segments; FY2025 financial results, Segment Information) - explanation of the change in the "Elimination and Corporate" adjustment in restated FY2024 (Apr 2024-Mar 2025) segment income ((18,839) to (14,941) JPY million)

NOT DISCLOSED (read: FY2025 Q1-Q4 and FY2026 Q1-Q2 financial results and briefing slides; Annual Securities Report 84th term, Item 2 a. Results of Production and Orders received) - orders received and backlog, so the requested orders restatement check cannot be run (see A2)

NOT RETRIEVED (tried: no request from module A4; meti.go.jp returned HTTP 403 to scripted requests earlier in this run (run_log.md, 403 list), not retried) - METI originals: 23 Jul 2023 amendment adding advanced semiconductor manufacturing equipment to Japan's export control list, and any later METI semiconductor list changes (only BIS's description saved, A4-331)

NOT RETRIEVED (tried: https://www.bis.doc.gov/index.php/documents/product-guidance/3211-2023-1-25-updated-faqs-for-oct-7-advanced-computing-and-semiconductor-manufacturing-equipment-rule/file (URL cited in 88 FR 73424 p.7) - one attempt 2026-11-21, the response was an HTML page, not the PDF; no BIS advisory opinions searched) - BIS FAQ II.A.1 of 25 Jan 2023 on the back-end exclusion, and any BIS advisory opinion on whether wafer-level test counts as back-end (logged in: A4, manifest)

NOT RETRIEVED (tried: sec.gov - no contact User-Agent configured this run) - any SEC filings of customers (e.g. NVIDIA, TSMC 20-F) naming Advantest as a supplier


## A5

NOT RETRIEVED (tried: https://www.advantest.com/document/en/investors/aad/E_Info_20260401_02.pdf - HTTP 403 to scripted request, not retried) - Notice Regarding Issuance of Zero Coupon Convertible Bonds Due 2031 (1 Apr 2026) (logged in: A5, manifest)

NOT RETRIEVED (tried: https://www.advantest.com/document/en/investors/aad/E_Info_20260401_03.pdf - HTTP 403 to scripted request, not retried) - Supplemental Materials regarding Issuance of Zero Coupon Convertible Bonds Due 2031 (1 Apr 2026) (logged in: A5, manifest)

NOT RETRIEVED (tried: https://www.advantest.com/document/en/investors/aad/E_Info_20260401_04.pdf - HTTP 403 to scripted request, not retried) - Notice on Determination of Terms of Issue of Zero Coupon Convertible Bonds Due 2031 (1 Apr 2026) (logged in: A5, manifest)

NOT DISCLOSED (read: Semi-Annual Securities Report 85th, Item3 1.(2) sub-item 2 and Notes 1-6; Annual Securities Report 84th, Item4 stock acquisition rights pp.60-61 and Note 33) - CB early-redemption terms (issuer call, clean-up call threshold, bondholder put dates) and events of default; only references to "early redemption", "Clean-up Redemption Notice" and "Events of Default" appear

NOT DISCLOSED (read: Semi-Annual Securities Report 85th, Note 11; FY2026 Q1 and Q2 briefing notes) - effective interest rate of the CB liability component, initial liability amount at issue and transaction costs

NOT DISCLOSED (read: Annual Securities Report 84th, Note 17 Borrowings, Note 30 Financial Instruments, MD&A Liquidity and Capital Resources, Note 33 Subsequent Events; Semi-Annual Securities Report 85th, Item2 (2) Liquidity, Item3 CB terms, Note 11) - financial covenants on loans, the committed line of credit, the overdraft or the CB

NOT DISCLOSED (read: Annual Securities Report 84th, Note 17(3) and MD&A Liquidity; Semi-Annual Securities Report 85th, Item2 (2)) - expiry dates, interest margins and commitment fees of the JPY 40bn committed line and JPY 100bn overdraft facilities (logged in: A5, CL/B)

NOT DISCLOSED (read: Annual Securities Report 84th, statement of financial position, Notes 17 and 30; Semi-Annual Securities Report 85th, statement of financial position) - commercial paper programme or commercial paper outstanding (no such line appears)

NOT DISCLOSED (read: Semi-Annual Securities Report 85th, full notes) - company-computed net interest-bearing debt at 30 Sep 2026 (FY2026 Q2 end) (the capital-management table is annual only)

NOT DISCLOSED (read: Semi-Annual Securities Report 85th, Note 11) - lease liability maturity profile at 30 Sep 2026 (FY2026 Q2 end) (maturity table is only in the annual report, at 31 Mar 2026 (FY2025 end))

NOT DISCLOSED (read: IR web page Bonds and Ratings, 2026-11-21) - credit ratings from agencies other than R&I (Moody's, S&P, JCR)

NOT DISCLOSED (read: Annual Securities Report 84th, Notes 26 Other Income and 32 Business Combinations, Item2 5. Material Contracts; Semi-Annual Securities Report 85th, Note 5) - name of the Services and Others business partially divested in FY2025 (Apr 2025-Mar 2026) and the buyer

NOT DISCLOSED (read: Annual Securities Report 84th, Note 12(2) goodwill by CGU and Note 32 (6)) - CGU to which Salland goodwill (3,004) is allocated (only the Test System segment is named)

NOT DISCLOSED (read: Annual Securities Reports 82nd and 83rd, Note 12(2) goodwill by CGU) - CGU to which Shin Puu goodwill (2,522) is allocated

NOT DISCLOSED (read: Semi-Annual Securities Report 85th, full notes) - goodwill by CGU and any impairment-test update at 30 Sep 2026 (FY2026 Q2 end)

NOT DISCLOSED (read: Annual Securities Reports 80th-84th, Business Combinations notes (8)) - revenue and profit contribution of R&D Altanova, CREA, Shin Puu and Salland after acquisition (omitted as immaterial)

NOT DISCLOSED (read: Annual Securities Report 80th, Note 12(2) Impairment Losses) - quarter in FY2021 (Apr 2021-Mar 2022) in which the 398 dormitory impairment was recognised

NOT RETRIEVED (tried: advantest.com news index pages 2023 and 2024 parsed for a Salland item; none listed) - press release announcing the Salland Engineering acquisition

NOT DISCLOSED (read: Semi-Annual Securities Report 85th, Note 11; FY2026 Q1 and Q2 briefing notes) - names and amounts of equity instruments bought in 1H FY2026 (Apr-Sep 2026; equity instruments at FVTOCI rose from 67,927 to 203,670)

NOT DISCLOSED (read: Semi-Annual Securities Report 85th, Note 12 Structured Entities; Annual Securities Report 84th, Note 33) - name and manager of the investment fund(s) holding JPY 228,916 m at 30 Sep 2026 (FY2026 Q2 end)

NOT DISCLOSED (read: News 2025-01-09 Strategic Partnerships with FormFactor and Technoprobe; Annual Securities Report 84th, Item4 (5) Status of Shareholdings pp.107-108 and Note 30(7)) - size of the FormFactor minority stake (subsidiaries' other listed holdings are shown only as "Other", 2 companies, JPY 5,337 m at 31 Mar 2026 (FY2025 end) [F] (A5-240))

NOT DISCLOSED (read: interim dividend notice E_Info_20261028_03 p.1, dividend table; FY2026 Q2 Consolidated Financial Results p.1, 2. Dividends; IR web page IR Calendar 2026-11-21, FY2026 Yearly Calendar) - FY2026 (Apr 2026-Mar 2027) year-end dividend per share (printed as "TBD" in the interim dividend notice and "-" in the tanshin forecast row) (logged in: A5, CL/B)

NOT DISCLOSED (read: Annual Securities Report 84th, Item4 3. Dividend Policy; FY2025 Q4 briefing slides p.5; FY2026 Q2 briefing slides and notes, Shareholder Return) - company-computed cumulative MTP3 total return ratio to date, and the dividend-timing convention in words (the annual ratios of 49% and 42% are printed, A5-225)

NOT DISCLOSED (read: Annual Securities Report 84th, Note 12(1) Increase or Decrease Table and Note 12(2) Impairment Test for Goodwill pp.134-136) - goodwill roll-forward by CGU (acquisitions and exchange differences are given only for total goodwill), so the bridge from R&D Altanova's acquisition goodwill (18,946 million) to the R&D Altanova CGU's 29,383 million at 31 Mar 2026 (FY2025 end) cannot be shown


## A6

NOT RETRIEVED (tried: advantest.com E_FR_FY2007_FN.pdf - HTTP 404; the saved IR result index lists results only from FY2008 and the report index only from the 74th term; sec.gov 20-F unavailable this run; retried in the A6 verification pass, nothing new) - FY2006 (Apr 2006-Mar 2007) and FY2007 (Apr 2007-Mar 2008) full-year results releases (FY2006 net sales and operating income, the peak year of the 2007-09 cycle) (logged in: A6, manifest)

NOT DISCLOSED (read: FY2019 Third Quarter Consolidated Financial Results, Services, Support and Others segment; FY2019 Consolidated Financial Results, segment section; Annual Financial Report FY2019 (78th term), MD&A p.81 and segment D&A note) - amount of the one-time amortisation expense on the transferred system-level test business (FY2019 Q3 (Oct-Dec 2019) / FY2019 (Apr 2019-Mar 2020))

NOT DISCLOSED (read: FY2018 Consolidated Financial Results, Overview of Business Results and quarterly overview p.18; FY2019 Second Quarter Consolidated Financial Results, p.4; FY2019 Third Quarter Consolidated Financial Results, p.4) - quarter in which the ~1.0 bn fixed-asset sale gain of 1H FY2018 (Apr-Sep 2018) was booked (placed in FY2018 Q2 (Jul-Sep 2018) by inference; the FY2019 Q3 (Oct-Dec 2019) release states only that it fell inside Apr-Dec 2018)

NOT DISCLOSED (read: FY2020 Consolidated Financial Results, Segment Information note 5 and Overview p.5; FY2020 Third Quarter Consolidated Financial Results, overview) - quarter in which the 5,569 million Advantest Europe GmbH pension income was booked (placed in FY2020 Q4 (Jan-Mar 2021) by inference)

NOT DISCLOSED (read: FY2023 Second Quarter Consolidated Financial Results, Segment Information note and p.7; FY2023 First Quarter Consolidated Financial Results, overview) - quarter in which the 3,179 million settlement income of 1H FY2023 (Apr-Sep 2023) was booked (placed in FY2023 Q2 (Jul-Sep 2023) by inference)

NOT DISCLOSED (read: FY2022 Q4 earnings call Q&A p.4; FY2022 Consolidated Financial Results, Services, Support and Others segment; Annual Securities Report 81st term, Notes - Inventories p.123) - exact amount and P&L line of the FY2022 Q4 (Jan-Mar 2023) inventory valuation losses (only "roughly ¥3 billion"; the annual total is 6,344 million)

NOT DISCLOSED (read: FY2018 Information Meeting Q&A p.1; FY2018 Consolidated Financial Results, Overview of Business Results; Annual Financial Report FY2019 (78th term), Notes - Inventories p.21) - exact amount and P&L line of the FY2018 Q4 (Jan-Mar 2019) inventory valuation loss (only "approximately 2 billion yen"; the annual total is 6,324 million)

NOT DISCLOSED (read: FY2019 1Q Information Meeting Q&A p.3; FY2019 First Quarter Consolidated Financial Results, Overview of Business Results) - amount of the FY2019 Q1 (Apr-Jun 2019) inventory valuation losses that management named as a gross-margin factor

NOT DISCLOSED (read: FY2023 Q1-Q4 earnings call Q&A summaries; FY2023 Consolidated Financial Results; Annual Securities Report 82nd term, Notes - Inventories p.133) - quarterly split of the FY2023 (Apr 2023-Mar 2024) inventory valuation losses (annual total 7,347 million)

NOT DISCLOSED (read: FY2018 First Quarter Consolidated Financial Results and FY2018 Consolidated Financial Results, Changes in accounting policies) - effect of IFRS 15 on FY2018 (Apr 2018-Mar 2019) quarterly net sales and operating income (only the 1.1 bn opening retained-earnings adjustment is given)

NOT DISCLOSED (read: FY2019 First Quarter Consolidated Financial Results, Changes in accounting policies) - effect of IFRS 16 on FY2019 (Apr 2019-Mar 2020) operating income (only the 10,344 million right-of-use assets at initial application are given)

NOT DISCLOSED (read: FY2008 Consolidated Financial Results, Overview of Business Results p.4 and Consolidated Statements of Operations p.12) - P&L line carrying the 5.1 bn FY2008 (Apr 2008-Mar 2009) restructuring cost (income statement shows only "Restructuring and impairment charges" 13,788)

NOT DISCLOSED (read: FY2015 Consolidated Financial Results (IFRS voluntary disclosure, 2016-06-29), all sections) - IFRS quarterly figures for FY2014 (Apr 2014-Mar 2015; only the FY2014 annual IFRS comparative is given), so IFRS T4Q values before FY2015 Q4 (Jan-Mar 2016) cannot be computed

NOT DISCLOSED (read: FY2015 Q1-Q3 and full-year releases (U.S. GAAP); FY2016 Q1-Q3 and full-year releases (IFRS)) - company-printed single-quarter figures for FY2015-FY2016 (Apr 2015-Mar 2017; no quarterly overview page in those releases; quarters derived by differencing)


## TH

NOT DISCLOSED (read: IR Technical Briefing slides p.13-14 and Q&A; Q&A summaries FY2024 Q2 to FY2026 Q2; IR Fireside Chats 2025-11-17 and 2026-11-12) - any quantified test time, test-intensity or test-insertion count per device or per device generation (only qualitative statements such as "multiples")

NOT DISCLOSED (read: Q2 FY2026 briefing notes p.5; Investors Guide 2610 p.8; FY2024 Q2 Q&A A9) - system-level test and burn-in revenue (reported only inside Other Systems)

NOT DISCLOSED (read: FY25 Financial Briefing slides p.18 "Source: Advantest"; FY2025 briefing notes p.13; Q2 FY2026 Q&A A2) - method behind the tester TAM and market-share estimates (revenue vs shipments basis, sources), which would explain why reported memory tester sales give about 54% of the company's own memory TAM against a claimed 61% (CY2025) and 54.3% against 63% (CY2024) (logged in: TH, CL/B)

NOT DISCLOSED (read: MTP3 follow-up FAQs A1, 2024-07-23) - breakdown of the "Core market" TAM by product area (company cites third-party research data)

NOT DISCLOSED (read: Integrated Annual Report 2026; Annual Securities Report 84th term, R&D section; keyword scan in English and Japanese of 164 Advantest-issued documents, calc/TH_keyword_scan.out.txt) - any hybrid-bonding-specific test product, programme or revenue

NOT DISCLOSED (read: Investors Guide 2610 p.8; Q2 FY2025 briefing notes p.7; Integrated Annual Report 2026 p.15) - revenue of nanotechnology products (photomask CD-SEM metrology)

NOT DISCLOSED (read: Q2 FY2026 Financial Briefing Q&A A7; Q1 FY2026 Financial Briefing Q&A A6; IR Fireside Chat Q&A 2026-11-12 A5) - committed date for 10,000 SoC tester systems a year and the scale and timing of the next step (only "roughly a year in advance" of end FY2028, Mar 2029; the company says the schedule is not final) (logged in: TH, CL/B)

NOT DISCLOSED (read: IR Fireside Chat Q&A 2025-11-17 A1; Q&A summaries FY2025 Q3 to FY2026 Q2; news release 2025-12-16) - die-level probe revenue, customer count or qualification status

NOT DISCLOSED (read: news releases T5801 2025-02-12 and M5241 2025-12-10; Q1 FY2026 Q&A A4) - number of customers qualified or committed for new memory testers and handlers ("strategic memory customers", "multiple major memory manufacturers" only)

NOT DISCLOSED (read: Q2 FY2026 Financial Briefing Q&A A11; FY2025 Q&A A4) - silicon photonics / CPO tester revenue and Advantest share in that segment

NOT DISCLOSED (read: Micron Fiscal Q4 2026 Earnings Call Prepared Remarks) - any Micron statement on HBM test time, test intensity or tester suppliers

NOT DISCLOSED (read: Teradyne Q3 2026 Earnings Call Prepared Remarks and presentation) - Teradyne's numeric HBM test market share (only "an area where we have higher share")

NOT DISCLOSED (read: Teradyne Analyst Day 2025 presentation p.36) - numeric Teradyne memory market share by segment (chart has no data labels)

NOT DISCLOSED (read: SK hynix Hot Chips 28 HBM tutorial; SK hynix/FormFactor SWTest 2021) - SK hynix test time or tester share figures for HBM

NOT RETRIEVED (tried: fetch.py on pmc.ncbi.nlm.nih.gov/articles/PMC13609547 - a reCAPTCHA page was returned and deleted; not worked around) - Do et al. 2026, "Thermal Management and Reliability Engineering of Advanced HBM Packages" (Micromachines), open-access review covering hybrid bonding in HBM (logged in: TH, manifest)

NOT RETRIEVED (tried: Firecrawl paper search and WebSearch; IEEE Xplore is paywalled) - peer-reviewed ITC / VTS / ECTC papers on HBM known-good-stack test, pre-bond test of 3D stacks and hybrid-bond interconnect test (only arXiv preprints and SWTest workshop slides were open)

NOT RETRIEVED (tried: Firecrawl search - account credits exhausted during this run) - further web discovery of open-access test papers and customer statements

NOT RETRIEVED (tried: tsmc.com and investor.tsmc.com refuse scripts in this run, not attempted again) - TSMC statements on CoWoS/SoIC test needs or tester capacity

NOT RETRIEVED (tried: investors.formfactor.com refuses scripts (403) per run log) - FormFactor investor materials on HBM and die-level probe demand

NOT RETRIEVED (tried: sec.gov - no contact User-Agent configured this run) - Teradyne 10-K and 8-K exhibits (full-year 2025 SoC and memory revenue, customer concentration)

NOT RETRIEVED (tried: investors.teradyne.com presentations page lists only Q4 2025 slides and Analyst Day 2025, no Q4 2025 prepared remarks) - Teradyne full-year 2025 SoC and memory revenue needed for a CY2025 two-vendor share check

NOT RETRIEVED (tried: WebSearch for an SK hynix newsroom article on HBM test; only conference slides and press found) - SK hynix own newsroom or IR statement on HBM test intensity or tester suppliers

NOT RETRIEVED (tried: WebSearch only; no primary NVIDIA or Broadcom document on tester demand found) - NVIDIA or Broadcom statements on test demand, test intensity or test suppliers

NOT RETRIEVED (tried: https://news.samsung.com/global/?s=HBM4+hybrid+bonding - one request 2026-11-21, HTTP 403 Access Denied, not retried) - Samsung statements on HBM4 hybrid bonding and associated test steps

NOT DISCLOSED (read: first pages of the six saved arXiv PDFs; arXiv API record research/sources/advantest/2026-11-21_arxiv_api-metadata-TH-papers.xml, fields comment and journal_ref) - a peer-reviewed or conference venue for arXiv 2508.01786, 2503.15753, 2511.05506, 2611.19544, 2606.22149 and 2006.04798; their rows are therefore tagged [S]


## CL/B

NOT RETRIEVED (tried: https://www.bloomberg.com/news/articles/2026-04-28/advantest-shares-decline-after-outlook-misses-on-tight-capacity - HTTP 403 to scripted request, not retried) - Bloomberg article of 28 Apr 2026 on the FY2026 (Apr 2026-Mar 2027) outlook and tight capacity (claim C7) (logged in: CL/B, manifest)

NOT RETRIEVED (tried: web search found https://www.bloomberg.com/news/articles/2026-01-28/advantest-rushes-to-boost-ai-chip-tester-capacity-to-meet-demand; not fetched because bloomberg.com refused scripted access in this run) - Bloomberg article of 28 Jan 2026 on capacity acceleration (claim C7)

NOT RETRIEVED (tried: https://streetinsider.com/Basic+Content/Nvidia+test+slot+could+send+this+stock+soaring%2C+UBS+says/25021163.html - HTTP 403, not retried) - UBS note on NVIDIA test dual-sourcing and its estimate of NVIDIA test spend through Advantest: test-sourcing content only (claim C2) (logged in: CL/B, manifest)

NOT RETRIEVED (tried: https://www.tipranks.com/news/the-fly/advantest-downgraded-to-market-perform-from-outperform-at-bernstein - HTTP 403; https://ng.investing.com/news/analyst-ratings/bernstein-cuts-advantest-stock-rating-to-market-perform-slashes-target-93CH-1828631 - HTTP 403; not retried) - Bernstein research note on Advantest: stated demand and margin arguments only (claim C1) (logged in: CL/B, manifest)

NOT RETRIEVED (tried: https://xenospectrum.com/en/teradyne-q3-2026-revenue-plateau/ - HTTP 403, not retried) - press analysis of Teradyne's flat Q4 2026 guide (claims C1, C2); the underlying guidance itself is now taken from Teradyne's own release (CL-136, CL-139) (logged in: CL/B, manifest)

NOT RETRIEVED (tried: https://xenospectrum.com/en/china-memory-testing-hbm-equipment/ - HTTP 403, not retried) - press article on Chinese HBM/memory test equipment (claims C3, C4) (logged in: CL/B, manifest)

NOT RETRIEVED (tried: https://www.nasdaq.com/articles/ter-rides-strong-semiconductor-test-segment-more-upside-ahead-0 - HTTP 403, not retried) - Zacks article on Teradyne's semiconductor test segment (claim C2) (logged in: CL/B, manifest)

NOT RETRIEVED (tried: web search found https://inpractise.com/articles/advantest-vs-teradyne-gpu-test-market-share-and-power-supply-advantage and https://seekingalpha.com/article/4837312-advantest-teradyne-market-share-shifts-in-this-duopoly, both behind a paywall; not fetched) - expert-interview and analyst content on Advantest vs Teradyne GPU test share (claim C2)

NOT RETRIEVED (tried: https://www.advantest.com/document/en/investors/aad/E_Info_20260401_02.pdf, _03.pdf, _04.pdf - HTTP 403 to the A5 module's scripted request in this run, not retried; verifier full-text search of the saved 84th annual securities report and 85th semi-annual securities report found no lock-up wording) - lock-up terms of the April 2026 Zero Coupon CB offering (catalyst B3: lock-up expiry)

NOT RETRIEVED (tried: web search Nov 2026 for any Section 232 proclamation after Proclamation 11002 of 14 Jan 2026 that sets tariffs on semiconductor manufacturing equipment or starts phase 2; none found; federalregister.gov not queried by script) - any dated Section 232 tariff on semiconductor manufacturing equipment or phase-2 semiconductor tariff (catalyst B3)

NOT DISCLOSED (read: IR web page IR Calendar, FY2026 Yearly Calendar, 2026-11-21; IR news index 2026, 2026-11-21) - day of the Q3 FY2026 (Oct-Dec 2026) results announcement (only "Jan" 2027 is given)

NOT DISCLOSED (read: IR web page IR Calendar 2026-11-21, FY2025 and FY2026 Yearly Calendars; IR news index 2026, 2026-11-21; IR web page Share Information; 84th annual securities report, p.199 Stock-related administration) - dates of the FY2026 (Apr 2026-Mar 2027) full-year results, the Q1 and Q2 FY2027 (Apr-Jun 2027 and Jul-Sep 2027) results, the 85th Ordinary General Meeting and the FY2026 year-end dividend payment (no FY2027 (Apr 2027-Mar 2028) calendar published; only the 15 May record date and 'within three months' are given)

NOT DISCLOSED (read: Q2 FY2026 Financial Briefing Q&A Summary, A7 and A11) - exact release date of the Fourth Mid-Term Management Plan (only "around May 2027")

NOT DISCLOSED (read: Q2 FY2026 Financial Briefing Q&A Summary, A2 and A9; Q1 FY2026 Q&A Summary, A1-A4; FY2025 briefing notes, tester market share section) - Advantest's tester share split by GPU, custom ASIC and CPU (only "majority share" in AI accelerators)

NOT DISCLOSED (read: Q2 FY2026 Financial Briefing Q&A Summary, Q10/A10) - direction and size of the divergence between Taiwan/Malaysia trade statistics and SoC tester sales raised by analysts

NOT DISCLOSED (read: Teradyne Q3 2026 Earnings Call Prepared Remarks; Teradyne Q3 2026 Earnings Presentation p.18; Teradyne Q3 2026 results press release) - Teradyne compute revenue in USD, its HBM performance-test share, and the target year of its Target Earnings Model

NOT DISCLOSED (read: Teradyne Q3 2026 Earnings Call Prepared Remarks, closing remarks; Teradyne IR home page 2026-11-21, Upcoming Event) - date of Teradyne's Q4 2026 earnings call (where the updated target model will be shared)

NOT DISCLOSED (read: FY2026 Q2 Consolidated Financial Results, 1.(4) Outlook; Q2 FY2026 briefing notes and Q&A Summary; IR Fireside Chat script and Q&A 2026-11-12) - any Advantest statement on the 19 Nov 2026 BIS remote-access rule or on Section 232 actions after January 2026

NOT DISCLOSED (read: TechNews article 2026-01-15; Advantest Q3 FY2025 briefing slides p.12 and notes p.9) - the Advantest document behind the "USD 8 bn 2026 ATE peak" and "watch for double ordering" statements relayed by TechNews (the company's own 28 Jan 2026 estimate differs)


## Sources

NOT RETRIEVED (tried: https://investors.teradyne.com/news-releases - HTTP 404 to scripted request, not retried (manifest row)) - Teradyne IR news-releases index page (the Q3 2026 results release itself was saved from investors.teradyne.com/news-events/press-releases/detail/455/teradyne-reports-third-quarter-2026-results)

