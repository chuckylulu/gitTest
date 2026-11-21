# Advantest Corporation (TSE Prime 6857, Japan) - evidence dossier

Date: 2026-11-21. Scope: one company, process-control theme "test" (automatic test equipment for AI chips, HBM and advanced packaging). No stock prices, valuation multiples or buy/sell views.

Fiscal year ends 31 March; fiscal years are named by their start year (FY2026 = Apr 2026-Mar 2027).

IFRS, Japanese yen. Latest quarter: FY2026 Q2 (Jul-Sep 2026), released 28 Oct 2026 [F] (TH-006, A3-217). Last four quarters: FY2025 Q3 (Oct-Dec 2025) to FY2026 Q2 (Jul-Sep 2026).

How to read: every claim carries one tag and the evidence ids behind it, e.g. "JPY 477.7 bn [F] (A1-060)". [F] = read in a saved primary document; [C] = company claim that cannot be tested, including every forecast, guidance figure, target, roadmap date, market share and TAM; [S] = secondary source; [I] = inference or calculation, with confidence and a script in `calc/`. Ids resolve in `evidence.csv` (module rows plus this dossier's DS rows; counts in section 11). Slide figures are JPY bn; tanshin (financial results), securities-report and calc figures are JPY million (JPY m) unless stated. "LTM" = FY2025 Q3-FY2026 Q2 (Oct 2025-Sep 2026).

---

## 1. Premise check

prior/ was empty: it holds only `.gitkeep`, so there were no exported chats to extract into `prior/text/` and no prior claims to test. The layout note in research/CLAUDE.md that describes prior/ as "the 12 files exported from AI Studio" does not match the repository [I] High (DS-002). The premises below therefore come from the project scope (research/CLAUDE.md), the run prompt and module briefs, the modules' own first drafts, and press sources.

| Premise (where it came from) | Correction | Tag and ids |
|---|---|---|
| Run facts: FY named by start year; latest quarter FY2026 Q2 (Jul-Sep 2026) released 28 Oct 2026; IFRS, JPY (run prompt) | Hold. "Q2 FY26" = three months ended 30 Sep 2026; FY2025 = Apr 2025-Mar 2026; the FY2026 Q2 tanshin is dated 28 Oct 2026 | [F] (TH-006, TH-007, A3-217) |
| The process-control set is "inspection, metrology, test", so Advantest supplies inspection or metrology for AI chips, HBM and hybrid bonding (project scope) | Advantest is a test (ATE) company. Its only metrology line is the photomask CD-SEM (latest model E3660, Sep 2025), inside Services and Others; it measures mask patterns, not wafers or packages | [F] (TH-011, TH-012, TH-013); premise correction [I] High (TH-194) |
| Advantest has hybrid-bonding exposure through its own products (project scope) | No hybrid-bonding product: hybrid-bonding terms (English and Japanese, incl. Cu-Cu, direct bond) appear in 0 of 164 Advantest-issued documents at the TH scan (180 files less 16 IR/news web pages, which also show 0); "CoWoS" and "wafer/defect inspection" also 0. The Apr 2024 Toray Engineering partnership is about microLED display production. Exposure is indirect: Advantest tests dies before stacking, stacks and packages | [I] High (TH-193); [F] (TH-016) |
| Probe cards and sockets for HBM and advanced-packaging test are in-house products (theme framing) | Probe cards are partnered: 2.5% stake in Technoprobe [F] (TH-018); a planned small minority stake bought from FormFactor (Jan 2025) [C] (A5-160); Micronics Japan partnership (Feb 2025) [F] (TH-019), 150,000 shares held at 31 Mar 2025 (FY2024 end) and 31 Mar 2026 (FY2025 end) [F] (A5-237). Sockets and interface boards come from Advantest Interconnect Solutions (Essai 2020, R&D Altanova 2021) [F] (TH-017) | as shown |
| Segments "Test System / Mechatronics System / Services, Support and Others" (run prompt) | From FY2025 Q1 (Apr-Jun 2025) there are two reportable segments, Test System Business and Services and Others, with comparatives restated. Handlers, device interfaces and system-level test sit in "Other Systems" inside Test System Business | [F] (A1-230, TH-009, TH-010) |
| Advantest has a US exchange listing and ticker (ticker check) | Listed on NYSE Sep 2001, delisted April 2016. An OTC ADR remains: ATEYY, 1 ADR = 1 share, depositary JPMorgan Chase Bank. Home listing TSE Prime, code 6857, since April 2022 | [F] (TH-004, TH-005, TH-002, TH-003); [I] High (TH-195) |
| Orders, backlog and book-to-bill can be tracked for four quarters (project rules A2) | FY2021 Q4 (Jan-Mar 2022) was the last disclosure of orders and backlog. Reasons given: longer lead times and short-term order swings. The FY2025 annual securities report omits orders; no remaining-performance-obligation amount (IFRS 15 practical expedient) | [F] (A2-001, A2-002, A2-008, A2-009) |
| Free cash flow = operating cash flow minus capex (standard definition) | The company defines FCF as operating CF plus investing CF. From FY2026 Q1 (Apr-Jun 2026) investing CF includes large purchases of fund and equity interests, so the two definitions diverge; both are shown in section 3 | [F] (A1-163) |
| Statutory quarterly securities reports exist for every quarter (working assumption) | The IR library lists Quarterly Securities Reports only up to FY2023 Q3 (dated 13 Feb 2024). From FY2024 it lists semi-annual and annual securities reports only, so Q1 and Q3 figures come from tanshin and briefing materials. NOT DISCLOSED (read: IR library report index 2026-11-21; Semi-Annual Securities Report 83rd (1H FY2024), Basis of Preparation (cites only Article 24-5 of the Financial Instruments and Exchange Act for the semi-annual report)) - reason the company files no Quarterly Securities Reports from FY2024 (Apr 2024-Mar 2025; Q1 and Q3 figures come from tanshin and briefing materials) | [I] High (DS-001) |
| Filing dates of the statutory reports = file metadata dates (working assumption) | The 84th Annual Securities Report (FY2025) is dated 26 Jun 2026 and the 85th Semi-Annual Securities Report (1H FY2026) 13 Nov 2026, and the saved file names now carry these dates. The two older semi-annual files (84th 1H FY2025, 83rd 1H FY2024) were renamed from 12 Nov PDF-metadata dates to the 13 Nov dates on the IR index. The Integrated Annual Report 2026 file carries 11 Nov 2026 (PDF metadata); the news index lists it on 16 Oct 2026; both fall in FY2026 Q3 (Oct-Dec 2026) | [I] High (DS-003) |
| E_Info_20261030 is a buyback notice (working assumption) | It is a restricted-stock notice: disposal of 40,198 treasury shares. The buyback decision is E_Info_20261028_02 and the progress report E_Info_20261102 | [F] (A5-109, A5-102, A5-104) |
| The AGM is held in June (working assumption) | The 84th AGM was held on 31 Jul 2026; the 27 Jun 2025 AGM amended the Articles to allow a July meeting | [F] (CL-096, CL-134, CL-098) |
| The voting-rights record date is 31 Mar (IR calendar) | The IR calendar prints 31 Mar for voting rights and the year-end dividend [F] (CL-095). The 84th annual securities report gives 15 May as the voting-rights record date, with dividend record dates 30 Sep and 31 Mar [F] (CL-133); the Integrated Annual Report and the Share Information page agree [F] (CL-134, CL-097). 15 May governs; the IR calendar line looks outdated | [I] Medium (CL-126) |
| A forecast revision always comes as a "Notice regarding revision of financial forecasts" (module brief) | Notices are titled "Revision of Earnings Forecast for the Fiscal Year Ending March 31, 20XX"; some revisions (e.g. 28 Oct 2026) appear only in the tanshin | [F] (A3-232, A3-233) |
| The annual report section is "Information about major customers", one basis (module brief) | The section is "(6) Information of Main Customers" and gives customer groups (NVIDIA Group JPY 243,735 m in FY2025, Apr 2025-Mar 2026). A separate Item 2 table gives single counterparties (NVIDIA International, Inc. JPY 228,273 m, 20.2% as printed) | [F] (A4-001, A4-406, A4-407); scope gap JPY 15,462 m [I] High (A4-434) |
| Regional sales have one basis | Quarterly slides split by ship-to region; the annual securities report and full-year results by customer location. FY2024 and FY2025 agree within rounding | [F] (A4-405, A4-050, A4-014); [I] High (A4-383) |
| Advantest has reported under IFRS since FY2014 (module first draft) | IFRS was adopted with the FY2015 annual securities report; transition date 1 Apr 2014, so FY2014 exists under IFRS only as a comparative | [F] (A6-329, A6-330) |
| The last two downturns are "2019 and 2022-2023" (module brief) | It depends on the definition. With trailing-four-quarter (T4Q) sales falling at least 5%, the last two are 2022-23 (T4Q to FY2022 Q4, Apr 2022-Mar 2023 -> T4Q to FY2023 Q4, Apr 2023-Mar 2024) and 2018-19 (T4Q to FY2018 Q3, Jan-Dec 2018 -> T4Q to FY2019 Q3, Jan-Dec 2019), but 2018-19 clears the threshold by 0.17 pp; above 5.17% the pair becomes 2022-23 and 2015-16 (T4Q to FY2016 Q1, Jul 2015-Jun 2016 -> T4Q to FY2016 Q2, Oct 2015-Sep 2016). A single-quarter >=15% rule does not select 2018-19 (-14.6%) | [I] High (A6-350); [I] Medium (A6-273); [I] High (A6-274) |
| No one-off was named in the 2018-19 trough quarter (module first draft) | Management named an inventory valuation loss of about JPY 2 bn in FY2018 Q4 (Jan-Mar 2019) | [F] (A6-314) |
| No one-off was named in FY2025 Q2 (Jul-Sep 2025) (module first draft) | Management named a one-time SG&A charge related to a growth investment [C] (A3-093); the same notes print about JPY 2 bn of Q2 expenses for competitiveness initiatives [F] (A1-511), which they do not tie to the charge; the charge's amount is the NOT DISCLOSED line in section 3.2 | [C] (A3-093); [F] (A1-511) |
| arXiv preprints count as papers ([F]) (module first draft) | None of the six arXiv papers prints a journal or conference venue; all are [S] | [S] (TH-150, TH-154, TH-155, TH-157, TH-158, TH-159) |
| Press: RCR Wireless (30 Jan 2026) presents the January 2026 guidance (sales JPY 1.07 trillion) as being for the fiscal year to 31 Mar 2027 [S] (CL-144) | It was the FY2025 (Apr 2025-Mar 2026) forecast, stated 28 Jan 2026 | [C] (CL-130) |
| Press: TechNews (15 Jan 2026) relays a "USD 8 bn 2026 ATE peak" attributed to Advantest [S] (CL-109) | The company's own estimate of 28 Jan 2026 was SoC USD 8.5-9.5 bn plus memory 2.2-2.7 bn for CY2026 [C] (CL-138), 10.7-12.2 bn combined [I] High (CL-129); the TechNews number is not traceable to a company document and is not used as evidence | [I] High (CL-129) |
| Press: Simply Wall St narrative read as an analyst view [S] (CL-023) | The page states an LLM tool wrote it; kept as context only, not used on any ledger side | [S] (CL-023, CL-091) |
| Company documents agree with each other on MTP2 ROIC (FY2021-FY2023, Apr 2021-Mar 2024 average) | Printed as 21.2% in the MTP3 press release and the 82nd securities report [F] (A3-240, A3-304) but 25.5% in the MTP3 slides and FY2024 Q4 slides [F] (A3-241, A3-305): a 4.3-point gap with the same definition [I] High (A3-303). The simple mean of the annual ROIC series matches 25.5% | [I] Medium (A3-307) |
| EPS figures in the Integrated Annual Report 2026 are yen per share | p.22 prints them with a "B" suffix ("JPY 284 - 341B", "JPY 218.67B", "JPY 515.15B") [F] (A3-251); they are yen per share, because the FY2024 (Apr 2024-Mar 2025) value equals basic EPS JPY 218.67 [F] (A3-062): reading [I] High, inputs A3-251 and A3-062 (one figure matches exactly) | as shown |

---

## 2. Snapshot

The handoff row (`handoff.md`), reproduced as fields:

| Field | Value |
|---|---|
| Company | Advantest Corporation |
| Ticker / country | 6857, Tokyo Stock Exchange Prime / Japan [F] (TH-002, TH-003) |
| FY end | as stated at the top of this file; handoff.md carries the full field |
| Latest quarter (fiscal + calendar) | FY2026 Q2 (Jul-Sep 2026), released 28 Oct 2026 [F] (TH-006, A1-060) |
| Theme share of revenue (company definition) | NOT DISCLOSED (read: Q2 FY26 slides p.15-16; Investors Guide 2610 p.5; Q3 FY25 Q&A A4; ASR 84th; SAR 85th) - AI, HBM or advanced-packaging share of revenue (see gaps.md). Nearest company category 'Computing / Communications' (HPC/AI plus smartphone APs) = 95% of FY2025 (Apr 2025-Mar 2026) SoC tester sales, rounded to 5% [F] (A1-295, A1-299); about 64.6% (62.9-66.3%) of FY2025 net sales [I] Low (A1-469); fiscal-year split only: NOT DISCLOSED (read: Q2 FY26 slides 15-16, Investors' Guide p.5 and p.7) - application split of SoC and memory tester sales for individual quarters or LTM (only fiscal-year splits, rounded to the nearest 5%) |
| LTM revenue and YoY | JPY 1,447,077m, LTM FY2025 Q3-FY2026 Q2 (Oct 2025-Sep 2026), +48.1% vs Oct 2024-Sep 2025 [I] High (A1-396, A1-397) |
| Gross margin reported / adjusted / ex one-offs | Reported 71.1% FY2026 Q2 (Jul-Sep 2026) [F] (A1-062), 68.2% LTM FY2025 Q3-FY2026 Q2 (Oct 2025-Sep 2026) [I] High (A1-398) / adjusted: NOT DISCLOSED (read: FY25 and FY24 Q4 summary slides p.5; Q2 FY26, Q1 FY26, Q3 FY25 slides; tanshin FY2025, FY2026 Q1-Q2; ASR 84th MD&A) - company-adjusted gross margin / ex one-offs: not computable; NOT DISCLOSED (read: Q1 FY26 notes p.5, Q&A A9; Q2 FY26 notes, Q&A A5; FY2026 Q1-Q2 tanshin; SAR 85th) - amount of the inventory write-down reversal management named for FY2026 Q1 (Apr-Jun 2026) and 1H FY2026 (Apr-Sep 2026) [C] (A1-315, A1-316) |
| LTM FCF and SBC/FCF | LTM FY2025 Q3-FY2026 Q2 (Oct 2025-Sep 2026): FCF JPY 273,933m, company definition (operating + investing CF) [I] High (A1-422); JPY 463,173m capex-based [I] High (A1-423); SBC JPY 4,968m = 1.81% of company FCF, 1.07% of capex-based [I] High (A1-427, A1-430) |
| Recurring revenue % | NOT DISCLOSED (read: ASR 84th Business Risks p.38, Note 22; SAR 85th; IAR 2026 p.35; MTP3 slides p.20; Q2 FY26 slides 6, 17; tanshin segment notes) - recurring revenue amount, share or definition (see gaps.md); proxies, not company definitions, are in dossier.md section 3.7 |
| China % | 18.9% of FY2026 Q2 (Jul-Sep 2026) sales [I] High (A4-357), JPY 90.1bn ship-to [F] (A4-134), +72.9% YoY [I] High (A4-369); LTM FY2025 Q3-FY2026 Q2 (Oct 2025-Sep 2026) 19.5% (JPY 281.7bn) [I] High (A4-370, A4-371); FY2025 (Apr 2025-Mar 2026) 18.9%, customer location [I] High (A4-373) |
| Inventory signal | Inventories JPY 231,718m (31 Mar 2026, FY2025 end) to 352,426m (30 Sep 2026, FY2026 Q2 end) [F] (A2-036, A2-038); +67.8% YoY at 30 Sep 2026 (FY2026 Q2 end) vs FY2026 Q2 (Jul-Sep 2026) cost of sales +38.9% YoY [I] High (A2-116, A2-188); days 195.0 (31 Dec 2025, FY2025 Q3 end) to 233.2 (30 Sep 2026, FY2026 Q2 end) [I] Medium (A2-112, A2-115); management calls the build deliberate strategic stock [C] (A2-179); NOT DISCLOSED (read: FY2026 Q2 tanshin balance sheet; SAR 85th notes 1-13) - raw / WIP / finished split at 30 Sep 2026 (FY2026 Q2 end) (see gaps.md) |
| Orders or backlog signal | NOT DISCLOSED (read: FY2025 Q1-FY2026 Q2 slides, notes, Q&A and tanshin; ASR 84th; SAR 85th) - orders and backlog (see gaps.md); the company stopped disclosing them after FY2021 Q4 (Jan-Mar 2022) [F] (A2-001). Proxy: advance-receipts inflow JPY 44,215m in 1H FY2026 (Apr-Sep 2026) [F] (A2-141), 4.54x full-year FY2025 (Apr 2025-Mar 2026) [I] High (A2-176) |
| Guidance record (beats / misses of 8) | 8 quarters FY2024 Q3-FY2026 Q2 (Oct 2024-Sep 2026), each vs guidance published at the prior release, band +/-2%: sales 7 beats / 0 in-line / 0 misses; OI 7 / 0 / 0; NI 6 / 0 / 1 (miss FY2024 Q4 (Jan-Mar 2025), -13.6%, impairment quarter); open slot FY2026 Q1 (Apr-Jun 2026), tracking a beat [I] Medium (A3-292, A3-290); [I] High (A3-284); the slots overlap (Q3 slots test 2H, Q1 slots the full year); independent single-quarter tests (FY2024 Q4, Jan-Mar 2025; FY2025 Q2, Jul-Sep 2025; FY2025 Q4, Jan-Mar 2026; FY2026 Q2, Jul-Sep 2026): sales 4/0/0, OI 4/0/0, NI 3/0/1 [I] Medium (A3-318). Annual (FY2023-FY2025, Apr 2023-Mar 2026), latest guidance (raised at Q3): sales 2/1/0, OI 1/1/1, NI 1/0/2 [I] High (A3-319); missed on NI in FY2023 (Apr 2023-Mar 2024) and FY2024 (Apr 2024-Mar 2025) [I] High (A3-278); FY2023 OI -4.0% [I] High (A3-265), +6.6% without the named Q4 impairment, +2.9% also without the named FY2023 Q2 (Jul-Sep 2023) settlement income [I] Medium (A3-267); FY2024 OI in line [I] High (A3-270), NI miss below IBT [I] High (A3-272) |
| Net cash or debt and next maturity | Net cash JPY 312.3bn at 30 Sep 2026 (FY2026 Q2 end; cash less CB carrying amount, leases excluded) [I] High (A5-202); JPY 284.0bn with CB at face value and leases [I] High (A5-205); no borrowings [F] (A5-043). Next maturity: JPY 100bn zero-coupon CB due 28 Mar 2031 (FY2030 Q4, Jan-Mar 2031) [F] (A5-061, A5-063) |
| Last downturn drawdown | FY2022 Q4 (Jan-Mar 2023) to FY2023 Q1 (Apr-Jun 2023): net sales -31.3% [I] High (A6-277); operating margin at the sales-peak quarter 26.2% to 14.1%, -12.1 pp reported [I] High (A6-279), -14.1 pp without the ~JPY 3bn inventory loss management named [I] Medium (A6-280); margin peak to trough FY2022 Q1 (Apr-Jun 2022) 32.9% -> FY2023 Q1 (Apr-Jun 2023) 14.1%, -18.8 pp, no one-off named in either quarter [I] High (A6-281) |
| Main strength [tag] | FY2026 Q2 (Jul-Sep 2026) net sales JPY 477.7bn, +81.7% YoY as printed [F] (A1-060, A1-067) |
| Main vulnerability [tag] | Customer concentration: top five customers about 50% of FY2025 (Apr 2025-Mar 2026) net sales; NVIDIA International, Inc. alone 20.2% as printed [F] (CL-070, CL-069) |

**What is solid**
- Reported results. FY2026 Q2 (Jul-Sep 2026) net sales JPY 477.7 bn [F] (A1-060), +81.7% YoY as printed [F] (A1-067), operating margin 55.9% [F] (A1-064) (may include part of the 1H reversal; ex-one-off figure not computable, NOT DISCLOSED line in section 3.2). Slide quarters agree with tanshin year-to-date differences [I] High (A1-391), and a restatement check found 0 of 195 statement line items changed between filings [I] High (A4-387).
- Balance sheet. No borrowings at 30 Sep 2026 (FY2026 Q2 end) [F] (A5-043); the only bond or borrowing is the JPY 100 bn zero-coupon CB due 28 Mar 2031 (FY2030 Q4, Jan-Mar 2031) [F] (A5-061, A5-063); net cash JPY 312,299 m at 30 Sep 2026 (FY2026 Q2 end) on the narrowest definition [I] High (A5-202).
- Concentration, from the statutory filing. NVIDIA International, Inc. 20.2% of FY2025 (Apr 2025-Mar 2026) net sales [F] (A4-407); top five customers about 50% [F] (CL-070).
- Guidance record. Every closed quarterly slot in FY2024 Q3-FY2026 Q2 (Oct 2024-Sep 2026) beat on sales and operating income [I] Medium (A3-292), of which four are independent single-quarter tests, all beats on sales and operating income [I] Medium (A3-318); the other closed slots are half-year and full-year tests that overlap them.

**What is not solid**
- Theme share. No AI, HBM or advanced-packaging revenue share is published (gap line in section 9.1). The nearest category mixes HPC/AI with smartphone application processors [F] (A1-299), and the derived 64.6% of FY2025 (Apr 2025-Mar 2026) sales is a proxy [I] Low (A1-469).
- Margins without one-offs for FY2026 Q1 (Apr-Jun 2026), 1H FY2026 (Apr-Sep 2026) and the LTM: the inventory write-down reversal management named [C] (A1-315, A1-316) has no amount; the NOT DISCLOSED line in section 3.2 covers the amount, the line it was booked in and whether any part fell in FY2026 Q2 (Jul-Sep 2026).
- Demand durability. Orders and backlog are not disclosed [F] (A2-001); the case for durability rests on company statements [C] (CL-002, CL-005) and on a cash proxy, advance receipts of JPY 44,215 m in 1H FY2026 (Apr-Sep 2026) [F] (A2-141). Inventories grew faster than cost of sales (+67.8% YoY to 30 Sep 2026 (FY2026 Q2 end) vs FY2026 Q2 (Jul-Sep 2026) cost of sales +38.9% YoY) [I] High (A2-116, A2-188).
- Market-share claims. The method behind them is not disclosed (gap line in section 9.3); the memory share claim (61% CY2025, 63% CY2024 [C] (TH-119)) is 7.0 and 8.7 points above memory sales over the company's own memory TAM [I] Medium (TH-181, TH-204).

---

## 3. A1 Results

### 3.1 Last four quarters and the last two fiscal years

Quarters are single-quarter slide figures (JPY bn); fiscal years are tanshin figures (JPY m). Net income attributable to owners equals net income (no non-controlling interests) [F] (A1-018, A1-101).

| Line | FY2025 Q3 (Oct-Dec 2025), JPY bn | FY2025 Q4 (Jan-Mar 2026), JPY bn | FY2026 Q1 (Apr-Jun 2026), JPY bn | FY2026 Q2 (Jul-Sep 2026), JPY bn | FY2025 (Apr 2025-Mar 2026), JPY m | FY2024 (Apr 2024-Mar 2025), JPY m |
|---|---|---|---|---|---|---|
| Net sales | 273.8 [F] (A1-039) | 328.1 [F] (A1-046) | 367.5 [F] (A1-053) | 477.7 [F] (A1-060) | 1,128,610 [F] (A1-001) | 779,707 [F] (A1-002) |
| Net sales YoY | +25.5% [I] High (A1-353) | +41.2% [I] High (A1-359) | +39.3% [I] High (A1-365) | +81.7% [F] (A1-067) | +44.7% [F] (A1-023) | +60.3% [F] (A1-518) |
| Gross profit | 169.7 [F] (A1-040) | 221.1 [F] (A1-047) | 255.6 [F] (A1-054) | 339.8 [F] (A1-061) | 726,107 [F] (A1-005) | 445,085 [F] (A1-006) |
| Gross margin, reported | 62.0% [F] (A1-041) | 67.4% [F] (A1-048) | 69.5% [F] (A1-055) | 71.1% [F] (A1-062) | 64.3% [I] High (A1-387) | 57.1% [I] High (A1-388) |
| Operating income | 113.6 [F] (A1-042) | 153.1 [F] (A1-049) | 190.0 [F] (A1-056) | 266.8 [F] (A1-063) | 499,120 [F] (A1-013) | 228,161 [F] (A1-014) |
| Operating income YoY | +64.0% [I] High (A1-356) | +139.1% [I] High (A1-362) | +53.3% [I] High (A1-368) | +146.0% [F] (A1-068) | +118.8% [I] High (A1-384) | +179.5% [F] (A1-519) |
| Operating margin, reported | 41.5% [F] (A1-043) | 46.7% [F] (A1-050) | 51.7% [F] (A1-057) | 55.9% [F] (A1-064) | 44.2% [F] (A1-024) | 29.3% [I] High (A1-389) |
| Income before tax | 113.8 [F] (A1-044) | 172.4 [F] (A1-051) | 234.1 [F] (A1-058) | 276.2 [F] (A1-065) | 516,720 [F] (A1-016) | 224,774 [F] (A1-017) |
| Net income | 78.7 [F] (A1-045) | 126.9 [F] (A1-052) | 174.8 [F] (A1-059) | 193.3 [F] (A1-066) | 375,353 [F] (A1-018) | 161,177 [F] (A1-019) |
| Net income YoY | +51.8% [I] High (A1-358) | +217.3% [I] High (A1-364) | +93.8% [I] High (A1-370) | +142.7% [I] High (A1-376) | +132.9% [I] High (A1-385) | +158.8% [F] (A1-520) |
| Basic EPS, JPY | 108.37 [F] (A1-088) | 174.55, derived [I] Medium (A1-377) | 241.27 [F] (A1-085) | 267.75 [F] (A1-084) | 515.15 [F] (A1-020) | 218.67 [F] (A1-021) |

- FY2024 (Apr 2024-Mar 2025) YoY rates are as printed in the FY2024 tanshin; recomputed from the FY2023 (Apr 2023-Mar 2024) actuals they agree [I] High (A1-521).
- Quarterly YoY is computed on JPY-million quarters from year-to-date tanshin differencing; the company's own printed YoY figures for FY2026 Q2 (Jul-Sep 2026: gross profit +107.7%, net income +142.7%) and FY2025 Q4 (Jan-Mar 2026: operating income +139.1%, net income +217.3%) are the same values [F] (A1-499, A1-500, A1-501, A1-502). Single quarters re-derived from the tanshin agree with the slides, e.g. FY2026 Q2 (Jul-Sep 2026) sales JPY 477,727 m [I] High (A1-391).
- LTM (Oct 2025-Sep 2026): net sales JPY 1,447,077 m [I] High (A1-396), +48.1% on Oct 2024-Sep 2025 [I] High (A1-397); gross margin 68.2% [I] High (A1-398); operating margin 50.0% [I] High (A1-399); income before tax JPY 796,437 m, 55.0% of sales [I] High (A1-505).
- Currency: the FY2025 (Apr 2025-Mar 2026) average was USD 1 = JPY 150 [F] (A1-321); 1H FY2026 (Apr-Sep 2026) averaged JPY 160, and management attributes part of the 1H result to yen depreciation [F] (A1-351).

### 3.2 Margins: reported, company-adjusted, and with and without the one-offs management named

**Company-adjusted measures.** The only adjusted profit measure Advantest publishes is core operating income = operating income excluding other income and expenses [F] (A1-122), in full-year slides only: JPY 496.5 bn in FY2025 (Apr 2025-Mar 2026) [F] (A1-123), a 44.0% margin [F] (A1-125); JPY 249.7 bn in FY2024 (Apr 2024-Mar 2025) [F] (A1-124), 32.0% [F] (A1-126). Applying the definition to quarters gives 41.5% (FY2025 Q3, Oct-Dec 2025), 46.8% (FY2025 Q4, Jan-Mar 2026), 51.5% (FY2026 Q1, Apr-Jun 2026) and 55.8% (FY2026 Q2, Jul-Sep 2026) [I] Medium (A1-392, A1-393, A1-394, A1-395). Segment income (the management measure) is operating income before share-based compensation [F] (A1-127): JPY 503,570 m in FY2025 (Apr 2025-Mar 2026) [F] (A1-128). NOT DISCLOSED (read: FY25 and FY24 Q4 summary slides p.5; Q2 FY26, Q1 FY26 and Q3 FY25 summary slides; tanshin FY2025, FY2026 Q1 and Q2; Annual Securities Report 84th MD&A) - a company-adjusted gross margin, adjusted net income or adjusted EPS.

**One-off items named by management, and the margin with and without each**

| Period | Item named (where) | Amount | Reported | Without the item | Tag and ids |
|---|---|---|---|---|---|
| FY2024 Q4 (Jan-Mar 2025) and FY2024 (Apr 2024-Mar 2025) | Impairment of Essai (system-level test) goodwill and intangibles, in other expenses | JPY 21,393 m [F] (A1-306); booked in Q4 per the slide note [F] (A1-307) | Q4 OM 27.6% [F] (A1-080); FY OM 29.3% [I] High (A1-389) | Q4 OM 36.8% [I] High (A1-471); FY OM 32.0% [I] High (A1-470) | as shown |
| FY2025 Q1 (Apr-Jun 2025) | Gain on partial divestiture of a business, in other income | JPY 2,504 m [F] (A1-308) | OM 47.0% [F] (A1-029) | OM 46.0% [I] High (A1-474) | as shown |
| FY2025 Q2 (Jul-Sep 2025) | One-time SG&A charge "related to a growth investment" [C] (A3-093) | NOT DISCLOSED (read: FY2025 Q2 earnings briefing notes p.3 Summary and p.9; FY2025 Q2 Q&A summary; FY2025 Q2 slides; FY2025 Q2 tanshin) - an amount printed expressly for the FY2025 Q2 (Jul-Sep 2025) "one time charge related to a growth investment"; the same notes print about JPY 2 bn of Q2 expenses for competitiveness initiatives [F] (A1-511) but do not tie them to the charge | OM 41.3% [F] (A1-036) | not computable - NOT DISCLOSED line in the Amount cell | as shown |
| FY2025 Q4 (Jan-Mar 2026) | Gain on the fair value of share call options, in financial income; management called it "a one-off item" [C] (A1-310) | JPY 17,312 m for FY2025 (Apr 2025-Mar 2026) [F] (A1-309), booked in Q4 [F] (A1-320) | Q4 income before tax JPY 172.4 bn [F] (A1-051) | JPY 155,059 m (47.3% of sales vs 52.5%) [I] High (A1-475) | as shown |
| FY2025 Q4 (Jan-Mar 2026) | "One-off expenses related to business operations" in SG&A [C] (A1-311) | NOT DISCLOSED (read: FY2025 Q4 briefing notes p.6 and Q&A; FY2025 Q4 slides; FY2025 tanshin; Annual Securities Report 84th MD&A and Note 23 SG&A p.161) - amount of the FY2025 Q4 one-off SG&A expenses | OM 46.7% [F] (A1-050) | not computable - NOT DISCLOSED line in the Amount cell | as shown |
| FY2025 (Apr 2025-Mar 2026) | Divestiture gain removed (the FY2025 Q2 charge and the FY2025 Q4 one-off SG&A have no disclosed amount) | JPY 2,504 m [F] (A1-308) | OM 44.2% [F] (A1-024) | 44.0% without the divestiture gain [I] High (A1-472); income before tax JPY 496,904 m without both gains, vs 516,720 [I] High (A1-473); the FY2025 Q4 (Jan-Mar 2026) one-off SG&A named by management [C] (A1-311) remains inside these figures; amount: NOT DISCLOSED (read: FY2025 Q4 briefing notes p.6 and Q&A; FY2025 Q4 slides; FY2025 tanshin; Annual Securities Report 84th MD&A and Note 23 SG&A p.161) - amount of the FY2025 Q4 one-off SG&A expenses; the FY2025 Q2 (Jul-Sep 2025) one-time SG&A charge named by management [C] (A3-093) also remains inside; amount: NOT DISCLOSED (read: FY2025 Q2 earnings briefing notes p.3 Summary and p.9; FY2025 Q2 Q&A summary; FY2025 Q2 slides; FY2025 Q2 tanshin) - an amount printed expressly for the FY2025 Q2 (Jul-Sep 2025) "one time charge related to a growth investment" | as shown |
| FY2026 Q1 (Apr-Jun 2026) | Reversal of inventory obsolescence, "not expected to occur on a recurring basis" [C] (A1-315); gross margin helped by "limited inventory valuation losses" [C] (A1-498) | NOT DISCLOSED (read: Q1 FY26 notes p.5 and Q&A A9; Q2 FY26 notes and Q&A A5; Q1 and Q2 FY26 slides; FY2026 Q1 and Q2 tanshin; Semi-Annual Securities Report 85th) - amount of the inventory write-down reversal | GM 69.5% [F] (A1-055); OM 51.7% [F] (A1-057) | not computable - NOT DISCLOSED line in the Amount cell | as shown |
| 1H FY2026 (Apr-Sep 2026) and FY2026 Q2 (Jul-Sep 2026) | "One-time benefit to the operating margin from a reversal of inventory write-down" in 1H [C] (A1-316) | Amount: same gap line as the row above. NOT DISCLOSED (read: Q2 FY26 Q&A A5 and notes; Q2 FY26 slides; FY2026 Q2 tanshin; Semi-Annual Securities Report 85th) - whether any of the reversal fell in FY2026 Q2 (Jul-Sep 2026) | 1H OM 54.0% [I] High (A1-516); Q2 GM 71.1% [F] (A1-062), OM 55.9% [F] (A1-064) | not computable - NOT DISCLOSED lines in the Amount cell and the row above | as shown |
| FY2026 Q1 (Apr-Jun 2026), Q2 (Jul-Sep 2026) and 1H (Apr-Sep 2026) | Valuation gains on strategic-investment financial instruments, in financial income; described as "period-end valuation gains", not called one-off [F] (A1-497, A1-314) | Q1 JPY 41,075 m [F] (A1-312); Q2 JPY 13,096 m [I] High (A1-477); 1H JPY 54,171 m [F] (A1-313) | IBT margin: Q2 57.8% [I] Medium (A1-478); 1H 60.4% [I] Medium (A1-479) | Q2 JPY 263,056 m, 55.1% [I] Medium (A1-478); 1H JPY 456,063 m, 54.0% [I] Medium (A1-479) | as shown |

- Gross margin: no named item with an amount sits in cost of sales, so reported gross margin is the only computable one. For FY2024 (Apr 2024-Mar 2025; GM 57.1% [I] High (A1-388)), FY2025 Q3 (Oct-Dec 2025), FY2025 Q4 (Jan-Mar 2026) and FY2025 (Apr 2025-Mar 2026) no item touching gross margin was named, so reported = ex one-offs there [I] High (A1-517); for FY2026 Q1 (Apr-Jun 2026), 1H FY2026 (Apr-Sep 2026) and the LTM the ex-one-off figure is not computable - NOT DISCLOSED line in the FY2026 Q1 (Apr-Jun 2026) row above.
- FY2025 Q3 (Oct-Dec 2025): no one-off named, so OM 41.5% [F] (A1-043) is also the ex-one-off figure; NOT DISCLOSED (read: Q3 FY2025 briefing notes and Q&A summary; FY2025 Q3 tanshin segment notes) - any management-named one-off item in FY2025 Q3 (Oct-Dec 2025); none named.
- LTM (Oct 2025-Sep 2026) operating margin 50.0% [I] High (A1-399); without one-offs: not computable - NOT DISCLOSED lines in the FY2025 Q4 (Jan-Mar 2026) and FY2026 Q1 (Apr-Jun 2026) rows above.
- LTM (Oct 2025-Sep 2026) income before tax without the call-option gain and the 1H FY2026 (Apr-Sep 2026) valuation gains: JPY 724,954 m, 50.1% of sales [I] Medium (A1-506), vs 796,437 m reported [I] High (A1-505).
- Year-on-year growth against bases without named items: FY2025 Q4 (Jan-Mar 2026) operating income +79.2% instead of +139.1% [I] Medium (A1-503); FY2026 Q1 (Apr-Jun 2026) +56.4% instead of +53.3% [I] Medium (A1-504); FY2026 Q2 (Jul-Sep 2026): not computable - the base quarter FY2025 Q2 (Jul-Sep 2025) holds the one-time SG&A charge, whose amount is the NOT DISCLOSED line in the FY2025 Q2 row above.
- Recurring inventory valuation losses, not named as one-offs: JPY 17,712 m in FY2024 (Apr 2024-Mar 2025) and 16,006 m in FY2025 (Apr 2025-Mar 2026) [F] (A1-319). Management said FY2025 Q1 (Apr-Jun 2025) had no one-time write-downs [C] (A1-317) and called the FY2024 Q4 (Jan-Mar 2025) gross margin "product mix driven" [C] (A1-318).
- Net income without the named items: NOT DISCLOSED (read: FY2025 tanshin notes; Annual Securities Report 84th, Note 15(3) tax-rate reconciliation p.146 and MD&A p.50; FY2026 Q1 and Q2 tanshin; Semi-Annual Securities Report 85th) - tax effect of the named one-off items (impairment, divestiture gain, call-option gain, valuation gains), so net income and the total return ratio cannot be shown without them.

### 3.3 Free cash flow, both definitions (JPY m)

Company definition: FCF = operating CF + investing CF [F] (A1-163). Capex-based FCF = operating CF - cash purchases of PP&E and intangibles; this is the dossier's definition, not the company's.

| Period | Operating CF | PP&E + intangibles (cash) | FCF, company definition | FCF, capex-based |
|---|---|---|---|---|
| FY2025 Q3 (Oct-Dec 2025) | 78,631 [I] High (A1-400) | 7,138 [I] High (A1-403) | 71,430 [I] High (A1-407); company 71.5 bn [F] (A1-170) | 71,493 [I] High (A1-411) |
| FY2025 Q4 (Jan-Mar 2026) | 116,628 [I] High (A1-401) | 9,294 [I] High (A1-404) | 106,418 [I] High (A1-408); company chart 106.3 bn [F] (A1-171) | 107,334 [I] High (A1-412) |
| FY2026 Q1 (Apr-Jun 2026) | 137,155 [F] (A1-152) | 10,884 [I] High (A1-405) | 34,607 [I] High (A1-409); company 34.7 bn [F] (A1-169) | 126,271 [I] High (A1-413) |
| FY2026 Q2 (Jul-Sep 2026) | 169,811 [I] High (A1-402) | 11,736 [I] High (A1-406) | 61,478 [I] High (A1-410); company 61.5 bn [F] (A1-168) | 158,075 [I] High (A1-414) |
| FY2025 (Apr 2025-Mar 2026) | 335,182 [F] (A1-144) | 33,012 + 3,018 [F] (A1-145, A1-146) | 300,630 [I] High (A1-415); slide 300.6 bn [F] (A1-164) | 299,152 [I] High (A1-416) |
| FY2024 (Apr 2024-Mar 2025) | 285,971 [F] (A1-148) | 17,414 + 2,017 [F] (A1-149, A1-150) | 243.8 bn [F] (A1-165) | 266,540 [I] High (A1-417) |
| 1H FY2026 (Apr-Sep 2026) | 306,966 [F] (A1-156) | 21,454 + 1,166 [F] (A1-157, A1-158) | 96,085 [I] High (A1-418) | 284,346 [I] High (A1-419) |
| LTM (Oct 2025-Sep 2026) | 502,225 [I] High (A1-421) | inside the capex-based figure (calc/A1_fcf_sbc.out.txt) | 273,933 [I] High (A1-422) | 463,173 [I] High (A1-423) |

- The two definitions diverge in FY2026 (Apr 2026-Mar 2027) because 1H FY2026 (Apr-Sep 2026) investing CF includes net purchases of debt and equity instruments of JPY 188,285 m [I] High (A1-420): fund-interest purchases JPY 184,365 m [F] (A1-160) and equity purchases JPY 26,053 m [F] (A1-161), less equity sales JPY 22,133 m [F] (A1-162). Management calls these strategic investments [C] (A1-350).
- FY2025 Q4 (Jan-Mar 2026): derived company-definition FCF JPY 106,418 m [I] High (A1-408) vs 106.3 bn on the company chart [F] (A1-171). NOT DISCLOSED (read: FY2025 Q4 notes p.7; Q2 FY26 slide 9; FY25 Q4 slide 11; FY2025 tanshin) - reason for the JPY 0.1 bn difference between the company's FY2025 Q4 (Jan-Mar 2026) FCF (106.3 bn; investing CF -10.3 bn) and FCF derived from YTD cash flow statements (106.4 bn; investing CF -10.2 bn).
- The company's "Capital Expenditure" (JPY 34.3 bn in FY2025, Apr 2025-Mar 2026 [F] (A1-172); 23.0 bn in 1H FY2026, Apr-Sep 2026 [F] (A1-173)) differs from the cash purchases above. NOT DISCLOSED (read: Q2 FY26 slides p.9 and p.14; FY25 Q4 slides; briefing notes) - basis of the company's "Capital Expenditure" figure (differs from cash purchases of PP&E and intangibles).

### 3.4 Stock-based compensation (JPY m)

- FY2025 (Apr 2025-Mar 2026): 4,450 [F] (A1-174), of which PSU 1,258 [F] (A1-177) and RS/RSU 3,189 [F] (A1-178); FY2024 (Apr 2024-Mar 2025): 2,893 [F] (A1-175). 1H FY2026 (Apr-Sep 2026): 2,635 [F] (A1-179); 1H FY2025 (Apr-Sep 2025): 2,117 [F] (A1-181). Mainly restricted stock [F] (A1-184).
- Quarters: FY2025 Q3 (Oct-Dec 2025) 1,164 [I] High (A1-424); FY2025 Q4 (Jan-Mar 2026) 1,169 [I] High (A1-425); FY2026 Q1 (Apr-Jun 2026) 1,351 [F] (A1-182); FY2026 Q2 (Jul-Sep 2026) 1,284 [I] High (A1-426). LTM 4,968 [I] High (A1-427).
- SBC as % of FCF (company definition / capex-based): FY2025 (Apr 2025-Mar 2026) 1.48% / 1.49% [I] High (A1-428); FY2024 (Apr 2024-Mar 2025) 1.19% / 1.09% [I] High (A1-431); 1H FY2026 (Apr-Sep 2026) 2.74% / 0.93% [I] High (A1-429); LTM (Oct 2025-Sep 2026) 1.81% / 1.07% [I] High (A1-430). FY2025 SBC = 0.39% of FY2025 net sales [I] High (A1-432).
- Open question: the parent-only (J-GAAP) statement of operations shows share-based compensation of JPY 26,134 m in FY2025 (Apr 2025-Mar 2026) [F] (A1-185), against the consolidated IFRS 4,450. The parent's "Provision for share-based remuneration" rose JPY 22,002 m in FY2025 [I] High (A1-507), while the consolidated plans are equity-settled [F] (A1-492, A1-493). NOT DISCLOSED (read: Annual Securities Report 84th, Non-Consolidated Financial Statements pp.185-193 incl. balance sheet, significant accounting policies (5) and statement-of-operations note *1, and Note 24 Share-Based Compensation pp.161-165) - reconciliation of parent-only J-GAAP "share-based compensation expense" of JPY 26,134 million (FY2025, Apr 2025-Mar 2026) to the consolidated IFRS expense of JPY 4,450 million. The consolidated figure is used here.

### 3.5 Revenue by reported segment

| JPY bn (slides) | FY2025 Q3 (Oct-Dec 2025) | FY2025 Q4 (Jan-Mar 2026) | FY2026 Q1 (Apr-Jun 2026) | FY2026 Q2 (Jul-Sep 2026) | YoY FY2026 Q2 |
|---|---|---|---|---|---|
| Test System Business | 245.1 [F] (A1-259) | 296.3 [F] (A1-266) | 333.6 [F] (A1-273) | 436.7 [F] (A1-280) | +84.0% [I] High (A1-455) |
| - SoC Test Systems | 165.2 [F] (A1-261) | 237.2 [F] (A1-268) | 259.6 [F] (A1-275) | 353.3 [F] (A1-282) | +103.4% [I] High (A1-457) |
| - Memory Test Systems | 57.3 [F] (A1-262) | 36.8 [F] (A1-269) | 48.0 [F] (A1-276) | 53.4 [F] (A1-283) | +21.6% [I] High (A1-458) |
| - Other Systems (handlers, device interfaces, SLT) | 22.6 [F] (A1-263) | 22.3 [F] (A1-270) | 26.0 [F] (A1-277) | 29.9 [F] (A1-284) | +51.0% [I] High (A1-522) |
| Services and Others | 28.7 [F] (A1-260) | 31.7 [F] (A1-267) | 33.9 [F] (A1-274) | 41.1 [F] (A1-281) | +60.5% [I] High (A1-456) |
| Test System segment margin | 47.8% [I] High (A1-433) | 54.4% [I] High (A1-434) | 57.2% [I] High (A1-436) | 60.7% [I] High (A1-435) | +12.8 pp [I] High (A1-523) |
| SoC share of net sales | 60.3% [I] High (A1-459) | 72.3% [I] High (A1-460) | 70.6% [I] High (A1-461) | 74.0% [I] High (A1-462) | +7.9 pp [I] High (A1-524) |

Test System segment margins: FY2025 Q4 (Jan-Mar 2026) may include the one-off SG&A and FY2026 Q1-Q2 (Apr-Sep 2026) the inventory write-down reversal, both named without amounts (the FY2025 Q4 SG&A and reversal NOT DISCLOSED lines in section 3.2), so ex-one-off segment margins are not computable - NOT DISCLOSED lines in section 3.2; FY2025 Q3 (Oct-Dec 2025) had no named item. The +12.8 pp change compares FY2025 Q2 (Jul-Sep 2025), which holds the one-time SG&A charge if it was booked in this segment, with FY2026 Q2 (Jul-Sep 2026), which may hold part of the reversal; neither amount is disclosed.

| JPY m (securities-report and tanshin segment notes) | FY2024 (Apr 2024-Mar 2025) | FY2025 (Apr 2025-Mar 2026) | 1H FY2025 (Apr-Sep 2025) | 1H FY2026 (Apr-Sep 2026) |
|---|---|---|---|---|
| Test System Business sales | 682,819 [F] (A1-191) | 1,019,390 [F] (A1-186) | 477,957 [F] (A1-201) | 770,231 [F] (A1-196) |
| - SoC | 440,452 [F] (A1-340) | 767,424 [F] (A1-337) | 364,978 [F] (A1-346) | 612,922 [F] (A1-343) |
| - Memory | 157,676 [F] (A1-341) | 171,504 [F] (A1-338) | 77,430 [F] (A1-347) | 101,385 [F] (A1-344) |
| - Others | 84,691 [F] (A1-342) | 80,462 [F] (A1-339) | 35,549 [F] (A1-348) | 55,924 [F] (A1-345) |
| Services and Others sales | 96,888 [F] (A1-192) | 109,230 [F] (A1-187) | 48,776 [F] (A1-202) | 74,969 [F] (A1-197) |
| Test System segment income | 262,120 [F] (A1-193) | 518,760 [F] (A1-188) | 240,556 [F] (A1-203) | 455,564 [F] (A1-198) |
| Services and Others segment income | (16,125) [F] (A1-194) | 8,758 [F] (A1-189) | 3,048 [F] (A1-204) | 20,866 [F] (A1-199) |

FY2025 (Apr 2025-Mar 2026) and 1H FY2026 (Apr-Sep 2026) segment income may hold the FY2025 Q2 (Jul-Sep 2025) and FY2025 Q4 (Jan-Mar 2026) one-off SG&A and the 1H FY2026 (Apr-Sep 2026) inventory write-down reversal named by management; amounts and segment: the NOT DISCLOSED lines in section 3.2.

- FY2025 (Apr 2025-Mar 2026) growth: SoC +74.2% [I] High (A1-464), memory +8.8% [I] High (A1-465); 1H FY2026 (Apr-Sep 2026): SoC +67.9% [I] High (A1-466), memory +30.9% [I] High (A1-467). SoC = 68.0% of FY2025 net sales [I] High (A1-463), 72.5% of 1H FY2026 sales [I] High (A1-468), 70.2% of LTM (Oct 2025-Sep 2026) sales [I] High (A1-510).
- Segment one-offs: Services and Others income without the divestiture gain is JPY 6,254 m in FY2025 (Apr 2025-Mar 2026) [I] High (A1-480); the FY2024 (Apr 2024-Mar 2025) Essai impairment sits in the same segment (section 6.5); FY2024 (Apr 2024-Mar 2025) Services and Others income without the JPY 21,393 m Essai impairment [F] (A4-425): JPY 5,268 m vs (16,125) reported [I] High (A4-429).

### 3.6 Theme share as the company defines it

- NOT DISCLOSED (read: Q2 FY26 / Q1 FY26 / FY25 / Q3 FY25 earnings-briefing slides and notes; Q&A summaries FY2025 Q1-FY2026 Q2; Integrated Annual Report 2026; Investors' Guide Oct 2026 Ch.1; Annual Securities Report 84th and Semi-Annual Securities Report 85th, business overview and revenue notes) - share of Advantest revenue tied to AI, HPC, HBM or advanced packaging. The company says it does not disclose beyond "Computing and Communications" [F] (A1-302, TH-126), and that the majority of that category is HPC/AI [C] (A1-303).
- Company metric: "Computing / Communications" = 95% of SoC Test Systems sales in FY2025 (Apr 2025-Mar 2026) and 90% in FY2024 (Apr 2024-Mar 2025) [F] (A1-295, A1-296), rounded to the nearest 5% [F] (A1-298); FY2026 (Apr 2026-Mar 2027) forecast 90% [C] (A1-297). Definition: "'Computing' ... includes leading-edge devices such as HPC (High Performance Computing) and AI, and 'Communications' include application processors (APs) for smartphones" [F] (A1-299). It covers SoC testers only.
- DRAM = 90% of FY2025 (Apr 2025-Mar 2026) Memory Test Systems sales (rounded) [F] (A1-301); HBM is not split out.
- Arithmetic proxy, not an AI share: about 64.6% of FY2025 (Apr 2025-Mar 2026) net sales (range 62.9-66.3%) [I] Low (A1-469). Section 9 has the full exposure table.

### 3.7 Recurring revenue

NOT DISCLOSED (read: Annual Securities Report 84th, Business Risks p.38 and Note 22 Revenue; Semi-Annual Securities Report 85th, segment and revenue notes; Integrated Annual Report 2026 p.35; MTP3 slides p.20; Q2 FY26 slides 6 and 17; FY2025 and FY2026 Q2 tanshin segment notes) - recurring revenue amount, share or definition. The company names "recurring revenue offerings" [C] (A1-494) and a "Boost Recurring" aim [C] (A1-495) without a figure. Proxies, not company definitions: Services and Others 9.4% of LTM (Oct 2025-Sep 2026) sales [I] Low (A1-508), a segment that also holds equipment such as the photomask CD-SEM and the partly divested business; Support Services 5.6% of LTM (Oct 2025-Sep 2026) sales [I] Low (A1-509).

---

## 4. A2 Leading signals

### 4.1 Orders, backlog, book-to-bill

| Item | Status | Tag and ids |
|---|---|---|
| Orders received, order backlog | Not disclosed since FY2021 Q4 (Jan-Mar 2022); "We no longer disclose order data" (Oct 2022); the FY2025 annual securities report omits orders | [F] (A2-001, A2-007, A2-008) |
| Remaining performance obligations | Omitted under the IFRS 15 practical expedient | [F] (A2-009) |
| Book-to-bill | NOT DISCLOSED (read: briefing slides and Q&A summaries FY2025 Q1 to FY2026 Q2) - company-stated book-to-bill ratio, any quarter FY2025 Q1 to FY2026 Q2 (Apr 2025-Sep 2026; cannot be computed because orders are not disclosed) | [F] (A2-001) for the orders gap |
| Last values (context only) | FY2021 Q4 (Jan-Mar 2022) orders JPY 199.0 bn [F] (A2-003) vs sales 116.8 bn [F] (A2-004), orders/sales 1.70 [I] High (A2-006); backlog JPY 394.7 bn at 31 Mar 2022 (FY2021 end) [F] (A2-005) | as shown |

NOT DISCLOSED (read: FY2025 Q1-FY2026 Q2 slides, notes, Q&A and tanshin; ASR 84th; SAR 85th) - orders and backlog for every quarter in the window (one line per quarter in gaps.md).

### 4.2 Inventories (JPY m)

Inventory days = ending inventories / single-quarter cost of sales x 91.25.

| Quarter-end | Inventories | Quarter cost of sales | Inventory days |
|---|---|---|---|
| 30 Sep 2025 (FY2025 Q2 end) | 210,038 [F] (A2-034) | 99,316 [I] High (A2-085) | 193.0 [I] Medium (A2-111) |
| 31 Dec 2025 (FY2025 Q3 end) | 222,464 [F] (A2-035) | 104,096 [I] High (A2-086) | 195.0 [I] Medium (A2-112) |
| 31 Mar 2026 (FY2025 end) | 231,718 [F] (A2-036) | 106,953 [I] High (A2-087) | 197.7 [I] Medium (A2-113) |
| 30 Jun 2026 (FY2026 Q1 end) | 273,654 [F] (A2-037) | 111,920 [F] (A2-076) | 223.1 [I] Medium (A2-114) |
| 30 Sep 2026 (FY2026 Q2 end) | 352,426 [F] (A2-038) | 137,902 [I] High (A2-088) | 233.2 [I] Medium (A2-115) |

- Inventories rose 67.8% YoY to 30 Sep 2026 (FY2026 Q2 end) [I] High (A2-116), while FY2026 Q2 (Jul-Sep 2026) cost of sales rose 38.9% [I] High (A2-188) and 1H FY2026 (Apr-Sep 2026) cost of sales 30.5% [I] High (A2-174). The 1H build was JPY 120,708 m [I] High (A2-117); the company's text says JPY 120.7 bn [F] (A2-182).
- One-off effect: the reversal of inventory write-down named for FY2026 Q1 (Apr-Jun 2026) and 1H FY2026 (Apr-Sep 2026) [C] (A2-052, A2-180) lowers cost of sales, so FY2026 Q1 (Apr-Jun 2026), and possibly FY2026 Q2 (Jul-Sep 2026), inventory days are overstated [I] Medium (A2-114). NOT DISCLOSED (read: Q1 FY2026 briefing notes p.5 and Q&A summary A9; Q2 FY2026 briefing notes and Q&A summary A5; Q1 and Q2 FY2026 briefing slides; FY2026 Q1 and Q2 Consolidated Financial Results (tanshin); Semi-Annual Securities Report 85th, notes 1-13 (no inventories note); Integrated Annual Report 2026; IR Fireside Chat script and Q&A 2026-11-12) - amount of the reversal of inventory write-down / obsolescence that management named for FY2026 Q1 (Apr-Jun 2026) and for 1H FY2026 (Apr-Sep 2026), the line it was booked in, and whether any part fell in FY2026 Q2 (Jul-Sep 2026); margins without it cannot be computed for FY2026 Q1, Q2, 1H and the LTM.
- Split (year-ends only): at 31 Mar 2026 (FY2025 end) finished goods 35,244 [F] (A2-045), work in process 69,240 [F] (A2-046), raw materials and supplies 127,234 [F] (A2-047); raw-material share 54.9% [I] High (A2-119), down from 61.4% at 31 Mar 2025 (FY2024 end) [I] High (A2-118). In FY2025 (Apr 2025-Mar 2026) work in process rose 30.1% [I] High (A2-120) and finished goods 27.1% [I] High (A2-121); raw materials fell 1.2% [I] High (A2-122). NOT DISCLOSED (read: FY2026 Q2 tanshin balance sheet; SAR 85th notes 1-13) - raw / WIP / finished split at 30 Sep 2026 (FY2026 Q2 end).
- Inventory valuation losses expensed: JPY 7,347 m (FY2023, Apr 2023-Mar 2024) [F] (A2-048), 17,712 m (FY2024, Apr 2024-Mar 2025) [F] (A2-049), 16,006 m (FY2025, Apr 2025-Mar 2026) [F] (A2-050). At 31 Mar 2026 (FY2025 end) inventories were about 20% of total assets, and the auditor notes "strategic inventory buffers" [F] (A2-183).
- Company stance: a "just-in-case" operating model [C] (A2-179); strategic inventory is "gold" [C] (A2-055); scarce DDR4 DRAM is being accumulated [C] (A2-056); JPY 70 bn of the Apr 2026 CB is planned for capacity and inventory [C] (A2-057); a Board-set buffer level with prompt action above it [C] (A2-058).
- Company-reported cash conversion cycle: 272 days (FY2023, Apr 2023-Mar 2024) [F] (A2-059), 207 (FY2024, Apr 2024-Mar 2025) [F] (A2-060), 177 (FY2025, Apr 2025-Mar 2026) [F] (A2-061). NOT DISCLOSED (read: Integrated Annual Report 2026, 11-Year Financial Highlights p.77 and footnotes *1-*5, p.35; annual securities report 84th, p.38; MTP3 slides 2024-06-25 p.33) - definition and formula of the company-reported cash conversion cycle.

### 4.3 Customer advances (contract liabilities), JPY m

Balances are disclosed at fiscal year-ends only: JPY 28,798 m at 31 Mar 2025 (FY2024 end) [F] (A2-124) and 40,143 m at 31 Mar 2026 (FY2025 end) [F] (A2-125), 3.56% of FY2025 (Apr 2025-Mar 2026) sales [I] High (A2-149). They sit in "Other current liabilities" [F] (A2-128), 93.9% of that line at 31 Mar 2026 (FY2025 end) [I] High (A2-159).

| Quarter | "Other current liabilities" at quarter-end | Advance-receipts cash-flow change in the quarter (a flow) |
|---|---|---|
| FY2025 Q2 (Jul-Sep 2025) | 42,619 [F] (A2-131) | +8,194 [I] High (A2-143) |
| FY2025 Q3 (Oct-Dec 2025) | 34,788 [F] (A2-132) | -7,402 [I] High (A2-144) |
| FY2025 Q4 (Jan-Mar 2026) | 42,756 [F] (A2-133) | +7,579 [I] High (A2-145) |
| FY2026 Q1 (Apr-Jun 2026) | 80,397 [F] (A2-134) | +36,984 [F] (A2-140) |
| FY2026 Q2 (Jul-Sep 2026) | 87,924 [F] (A2-135) | +7,231 [I] High (A2-146) |

- 1H FY2026 (Apr-Sep 2026) advance-receipts inflow JPY 44,215 m [F] (A2-141), against 9,571 m in 1H FY2025 (Apr-Sep 2025) [F] (A2-137) and 9,748 m in all of FY2025 (Apr 2025-Mar 2026) [F] (A2-139); 4.54x the FY2025 figure [I] High (A2-176). The FY2026 Q1 (Apr-Jun 2026) inflow equals 92.1% of the 31 Mar 2026 (FY2025 end) balance [I] Medium (A2-175), and "Other current liabilities" moved in the same direction as the flow in 6 of 6 quarters, FY2025 Q1-FY2026 Q2 (Apr 2025-Sep 2026) [I] Medium (A2-195).
- About 86% of opening contract liabilities became revenue within the following year: 85.5% in FY2024 (Apr 2024-Mar 2025), 86.3% in FY2025 (Apr 2025-Mar 2026) [I] High (A2-189, A2-190).
- NOT DISCLOSED (read: financial results FY2026 Q2; semi-annual securities report 85th, condensed statements and notes 1-13, note 8 Revenue has no contract balances) - contract liabilities (advance receipts) balance at 30 Sep 2026 (FY2026 Q2 end).

### 4.4 Receivables and DSO (JPY m)

DSO = ending trade and other receivables / single-quarter net sales x 91.25.

| Quarter-end | Trade and other receivables | DSO, days |
|---|---|---|
| 30 Sep 2025 (FY2025 Q2 end) | 163,652 [F] (A2-091) | 56.8 [I] Medium (A2-102) |
| 31 Dec 2025 (FY2025 Q3 end) | 143,318 [F] (A2-092) | 47.8 [I] Medium (A2-103) |
| 31 Mar 2026 (FY2025 end) | 228,731 [F] (A2-093) | 63.6 [I] Medium (A2-104) |
| 30 Jun 2026 (FY2026 Q1 end) | 178,497 [F] (A2-094) | 44.3 [I] Medium (A2-105) |
| 30 Sep 2026 (FY2026 Q2 end) | 239,468 [F] (A2-095) | 45.7 [I] Medium (A2-106) |

- Receivables rose 46.3% YoY to 30 Sep 2026 (FY2026 Q2 end) while FY2026 Q2 (Jul-Sep 2026) sales rose 81.7% [I] High (A2-163). NOT DISCLOSED (read: FY2025 Consolidated Financial Results (tanshin), financial position and cash-flow overview; FY2025 Q4 briefing slides, notes and Q&A summary; FY2026 Q1 Consolidated Financial Results and briefing notes) - reason for the peak in trade and other receivables at 31 Mar 2026 (FY2025 end; JPY 228,731 m [F] (A2-093), DSO 63.6 days [I] Medium (A2-104)); the documents state only the increase and the following decrease; the balance fell JPY 50,234 m in FY2026 Q1 (Apr-Jun 2026) [I] High (A2-194). Payment terms are generally within 3 months [F] (A2-099).

### 4.5 Purchase commitments

- Only capex commitments are quantified: JPY 460 m at 31 Mar 2024 (FY2023 end) [F] (A2-152), 368 m at 31 Mar 2025 (FY2024 end) [F] (A2-153), 612 m at 31 Mar 2026 (FY2025 end) [F] (A2-154).
- NOT DISCLOSED (read: annual securities report 84th, notes 9, 11 and 22, business risks p.42, full-text search for 'commitment' and 'purchase obligation') - purchase commitments for materials and components (amount and maturity). The company cites long-term procurement contracts, "die bank" wafer inventories [C] (A2-155) and long-term supplier agreements with a contract manufacturer ramping a second Southeast Asian factory [C] (A2-156).

### 4.6 What management says about demand (dated statements)

| Stated | Statement | Tag and ids |
|---|---|---|
| 29 Jul 2025 | FY2025 Q1 (Apr-Jun 2025) sales included demand pull-ins; a temporary digestion was expected in 2H FY2025 (Oct 2025-Mar 2026) | [C] (A2-013, A2-014) |
| 28 Oct 2025 | FY2025 Q2 (Jul-Sep 2025) SoC sales fell QoQ because HPC/AI deliveries were pulled into Q1; 2H digestion expected to be milder | [C] (A2-015, A2-016) |
| 28 Jan 2026 | The anticipated digestion did not occur, owing to pull-ins in FY2025 Q3 (Oct-Dec 2025); many customers say their own order books are full (the customers, not Advantest) | [C] (A2-017, A2-018, A2-020) |
| 27 Apr 2026 | Visibility improved; new-system demand expected for at least two to three more years | [C] (A2-021, A2-022) |
| 29 Jul 2026 | Customers share 18-month forecasts, versus about six months historically | [C] (A2-023) |
| 28 Oct 2026 | Supply-constrained industry in CY2027; sales to rise about 20% from 1H to 2H FY2026; 2H FY2026 (Oct 2026-Mar 2027) sales forecast JPY 1,017.8 bn, +20.4% on reported 1H | [C] (A2-025, A2-026, A2-027); [I] High (A2-191) |
| 28 Oct 2026 | SoC tester capacity of more than 5,000 systems a year reached; 10,000 to come "well ahead" of the original schedule; memory components tight | [C] (A2-030, A2-029) |
| 12 Nov 2026 | Some customers give 18-month and multiyear forecasts | [C] (A2-031) |

Lead times: nine to 12 months (stated Oct 2022) [C] (A2-010) and about six months (stated Jul 2023) [C] (A2-011); no current figure. NOT DISCLOSED (read: Q&A summaries FY2025 Q3, FY2025 Q4, FY2026 Q1, FY2026 Q2; briefing notes FY2025 Q1 to FY2026 Q2; IR fireside chat script and Q&A 2026-11-12; annual securities report 84th, business risks) - current product lead time in months. NOT DISCLOSED (read: Q&A summaries FY2025 Q3, FY2025 Q4, FY2026 Q1, FY2026 Q2; briefing notes FY2025 Q3 to FY2026 Q2) - any statement on order cancellations or customer-requested delivery postponements, FY2025 Q3 to FY2026 Q2.

---

## 5. A3 Guidance record

### 5.1 What guidance exists, and the test used

- Formal guidance is full-year only: net sales, operating income (OI), income before tax (IBT), net income (NI) and, from 30 Oct 2024, basic EPS [F] (A3-001, A3-002, A3-003). The slides split it: a Q2 and a 2H forecast at the Q1 release, e.g. [C] (A3-134); 2H = full year minus 1H at the Q2 release [F] (A3-004), e.g. [C] (A3-138); Q4 = full year minus 9M at the Q3 release [F] (A3-005, A3-006). NOT DISCLOSED (read: FY2024 Q1-FY2026 Q2 earnings briefing slides, forecast slides; FY2024 Q4 slides p.19 and FY2025 Q4 slides p.20 (full-year forecast only); FY2025 Q3 briefing notes, Summary) - Q1 or Q3 single-quarter guidance. There is no orders guidance [F] (A2-001) and no core-OI guidance (the forecast column shows "-") [F] (A3-308, A3-310).
- Management describes its approach as "cautious ... especially beyond 1H" [C] (A3-008), with FY2025 (Apr 2025-Mar 2026) guidance set at the midpoint of its TAM estimate [C] (A3-007).
- Test: each quarter is compared with the guidance published at the previous quarter's results release (about four weeks into the quarter). Q2 and Q4 slots use the printed Q2 or Q4 forecast; Q3 slots compare the 2H forecast with the 2H actual; Q1 slots compare the initial full-year guidance with the year's outcome. Band: beat > +2%, in-line within +/-2%, miss < -2%; diff = (actual - guidance) / guidance. Two of the eight slots are half-year tests and two are full-year tests [I] Medium (A3-292). The slots overlap: each Q3 slot's 2H test contains the next Q4, and the FY2025 Q1 slot's full-year test contains FY2025 Q2-Q4 (Jul 2025-Mar 2026) and repeats the FY2025 annual test (section 5.3). Only the four Q2 and Q4 slots are independent single-quarter tests [I] Medium (A3-318).

### 5.2 Eight quarters, FY2024 Q3 (Oct-Dec 2024) to FY2026 Q2 (Jul-Sep 2026)

Guidance figures are company forecasts [C]; actuals are [F]; differences and classes are [I]. JPY bn.

| Slot | Guidance used (published) | Sales: guidance -> actual, diff | OI: guidance -> actual, diff | NI diff | Class sales / OI / NI | Same test without named one-offs |
|---|---|---|---|---|---|---|
| FY2024 Q3 (Oct-Dec 2024) | 2H FY2024 (30 Oct 2024) | 310.8 [C] (A3-125) -> 450.5, +44.9% [I] High (A3-283) | 70.1 [C] (A3-126) -> 133.3, +90.2% [I] High (A3-283) | +74.3% [I] High (A3-283) | beat / beat / beat | 2H OI without the Q4 impairment +120.7% [I] High (A3-283) |
| FY2024 Q4 (Jan-Mar 2025) | Q4 FY2024 (29 Jan 2025) | 192.6 [C] (A3-129) -> 232.3 [F] (A3-166), +20.6% [I] High (A3-284) | 61.9 [C] (A3-130) -> 64.1 [F] (A3-167), +3.6% [I] High (A3-284) | -13.6% [I] High (A3-284) | beat / beat / **miss** | OI without the JPY 21.4 bn impairment +38.1%; OPM 27.6% reported, 36.8% without [I] Medium (A3-285). NI in line if the after-tax effect (NOT DISCLOSED line in gaps.md, A3) is at least 5.4 bn, a beat above 7.2 bn [I] Medium (A3-285); the company says the impairment was not tax-deductible [F] (A3-316) |
| FY2025 Q1 (Apr-Jun 2025) | FY2025 initial (25 Apr 2025) | full year 755.0 [C] (A3-066) -> 1,128.6 [F] (A3-086), +49.5% [I] High (A3-286) | 242.0 [C] (A3-067) -> 499.1 [F] (A3-087), +106.2% [I] High (A3-286) | +109.7% [I] High (A3-286) | beat / beat / beat | OI less the divestiture gain +105.2% [I] High (A3-286); the FY2025 Q2 (Jul-Sep 2025) charge and the FY2025 Q4 (Jan-Mar 2026) one-off SG&A (no amounts, section 3.2) stay inside; NI also includes the FY2025 Q4 call-option gain [F] (A1-309) |
| FY2025 Q2 (Jul-Sep 2025) | Q2 FY2025 (29 Jul 2025) | 237.2 [C] (A3-134) -> 262.9 [F] (A3-172), +10.8% [I] High (A3-287) | 96.3 [C] (A3-135) -> 108.4 [F] (A3-173), +12.6% [I] High (A3-287) | +10.9% [I] High (A3-287) | beat / beat / beat | The one-time SG&A charge [C] (A3-093) has no disclosed amount (NOT DISCLOSED line in section 3.2); removing an expense can only raise OI, so the beat stands [I] High (A3-287) |
| FY2025 Q3 (Oct-Dec 2025) | 2H FY2025 (28 Oct 2025) | 423.3 [C] (A3-138) -> 601.9, +42.2% [I] High (A3-288) | 141.6 [C] (A3-139) -> 266.7, +88.3% [I] High (A3-288) | +95.4% [I] High (A3-288) | beat / beat / beat | 2H NI less the Q4 call-option gain +78.9% [I] High (A3-288); 2H OI includes the FY2025 Q4 (Jan-Mar 2026) one-off SG&A (no amount, section 3.2) |
| FY2025 Q4 (Jan-Mar 2026) | Q4 FY2025 (28 Jan 2026) | 269.5 [C] (A3-142) -> 328.1 [F] (A3-178), +21.7% [I] High (A3-289) | 108.0 [C] (A3-143) -> 153.1 [F] (A3-179), +41.8% [I] High (A3-289) | +58.6% [I] High (A3-289) | beat / beat / beat | NI less the call-option gain +37.0% [I] High (A3-289); the Q4 one-off SG&A has no amount (section 3.2) |
| FY2026 Q1 (Apr-Jun 2026) | FY2026 initial (27 Apr 2026) | full year 1,420.0 [C] (A3-094); 1H actual already 59.5% of it [I] Medium (A3-290) | 627.5 [C] (A3-095) | open until the FY2026 (Apr 2026-Mar 2027) results | provisional beat | The slot fails to be a beat only if 2H FY2026 (Oct 2026-Mar 2027) sales are at or below JPY 603.2 bn, 40.7% under the current 2H guidance [I] Medium (A3-290) |
| FY2026 Q2 (Jul-Sep 2026) | Q2 FY2026 (29 Jul 2026) | 434.5 [C] (A3-146) -> 477.7 [F] (A3-184), +9.9% [I] High (A3-291) | 224.5 [C] (A3-147) -> 266.8 [F] (A3-185), +18.8% [I] High (A3-291) | +18.4% [I] High (A3-291) | beat / beat / beat | NI less the 13.1 bn Q2 valuation gains +10.4% [I] High (A3-291); OPM ex the inventory reversal not computable - NOT DISCLOSED line in section 3.2 |

**Count (8 slots, +/-2% band)** [I] Medium (A3-292):

| Metric | Beats | In-line | Misses | Open (FY2026 Q1, Apr-Jun 2026, tracking a beat) |
|---|---|---|---|---|
| Sales | 7 | 0 | 0 | 1 |
| OI | 7 | 0 | 0 | 1 |
| NI | 6 | 0 | 1 (FY2024 Q4, Jan-Mar 2025) | 1 |
| EPS | 6 | 0 | 1 (FY2024 Q4, Jan-Mar 2025) | 1 |
| Sales, 4 independent single-quarter slots only | 4 | 0 | 0 | 0 (none of the four is open) |
| OI, same 4 slots | 4 | 0 | 0 | 0 |
| NI, same 4 slots | 3 | 0 | 1 (FY2024 Q4, Jan-Mar 2025) | 0 |
| EPS, same 4 slots | 3 | 0 | 1 (FY2024 Q4, Jan-Mar 2025) | 0 |

The last four rows count only the Q2 and Q4 slots, FY2024 Q4 (Jan-Mar 2025), FY2025 Q2 (Jul-Sep 2025), FY2025 Q4 (Jan-Mar 2026) and FY2026 Q2 (Jul-Sep 2026), which do not overlap [I] Medium (A3-318).

- With a +/-5% band the only change is FY2024 Q4 (Jan-Mar 2025) OI, from beat to in-line [I] High (A3-293). Removing the named one-offs changes no OI class.
- Q3 alone covered 70.2% (FY2024 Q3, Oct-Dec 2024) and 64.7% (FY2025 Q3, Oct-Dec 2025) of the 2H sales guidance [I] High (A3-297).
- Management's own statements: FY2025 Q2 (Jul-Sep 2025) sales, OI and NI beat the July forecast [F] (A3-221, A3-222); FY2025 Q4 (Jan-Mar 2026) exceeded the January projections [F] (A3-225); FY2025 Q3 (Oct-Dec 2025) beat internal projections [C] (A3-223).

### 5.3 Annual record (last three fiscal years)

| FY | Version (published) | Net sales | OI | NI | EPS, JPY | Tag and ids |
|---|---|---|---|---|---|---|
| FY2023 (Apr 2023-Mar 2024) | initial (26 Apr 2023) | 480,000 | 105,000 | 78,000 | none | [C] (A3-018 to A3-021) |
| FY2023 (Apr 2023-Mar 2024) | cut at Q2 (31 Oct 2023) | 470,000 | 80,000 | 60,000 | none | [C] (A3-023 to A3-026) |
| FY2023 (Apr 2023-Mar 2024) | raised at Q3, latest (31 Jan 2024) | 480,000 | 85,000 | 64,500 | none | [C] (A3-028 to A3-031) |
| FY2023 (Apr 2023-Mar 2024) | actual | 486,507 | 81,628 | 62,290 | 84.45 (no EPS guidance that year) | [F] (A3-032 to A3-035, A3-323) |
| FY2024 (Apr 2024-Mar 2025) | initial (26 Apr 2024) | 525,000 | 90,000 | 67,000 | none | [C] (A3-040 to A3-043) |
| FY2024 (Apr 2024-Mar 2025) | raised at Q3, latest (29 Jan 2025) | 740,000 | 226,000 | 167,500 | 227.74 | [C] (A3-053 to A3-057) |
| FY2024 (Apr 2024-Mar 2025) | actual | 779,707 | 228,161 | 161,177 | 218.67 | [F] (A3-058 to A3-062) |
| FY2025 (Apr 2025-Mar 2026) | initial (25 Apr 2025) | 755,000 | 242,000 | 179,000 | 243.96 | [C] (A3-066 to A3-070) |
| FY2025 (Apr 2025-Mar 2026) | raised at Q3, latest (28 Jan 2026) | 1,070,000 | 454,000 | 328,500 | 452.34 | [C] (A3-081 to A3-085) |
| FY2025 (Apr 2025-Mar 2026) | actual | 1,128,610 | 499,120 | 375,353 | 515.15 | [F] (A3-086 to A3-090) |

JPY m. Intermediate versions (FY2023 Q1 maintained; FY2024 raised 31 Jul and 30 Oct 2024; FY2025 raised 29 Jul and 28 Oct 2025) are in A3 [C] (A3-022, A3-044 to A3-052, A3-071 to A3-080).

| FY | vs latest guidance | Without the one-offs management named | Tag and ids |
|---|---|---|---|
| FY2023 (Apr 2023-Mar 2024) | Sales +1.4% in-line [I] High (A3-264); OI -4.0% miss [I] High (A3-265); IBT -5.2% and NI -3.4% miss [I] High (A3-266) | OI without the Q4 goodwill impairment of JPY 8,998 m [F] (A3-036): +6.6%, OPM 18.6% vs 16.8% [I] Medium (A3-267); also without the FY2023 (Apr 2023-Mar 2024) settlement income of JPY 3,179 m named by management [F] (A3-038), absent from the Q1 results and first printed for 1H, so booked in FY2023 Q2 (Jul-Sep 2023) [F] (A3-315): OI 87,447, +2.9%, OPM 18.0% [I] Medium (A3-267); the settlement predates the Jan 2024 guidance, so the impairment-only figure is the like-for-like test; NI without the ~JPY 3.8 bn deferred-tax benefit [F] (A3-039): -9.3% [I] Medium (A3-268); company core OI JPY 87.1 bn [F] (A3-309) | as shown |
| FY2024 (Apr 2024-Mar 2025) | Sales +5.4% beat [I] High (A3-269); OI +1.0% in-line [I] High (A3-270); NI -3.8% and EPS -4.0% miss [I] High (A3-271) | OI without the JPY 21,393 m impairment: +10.4%, OPM 32.0% vs 29.3% [I] Medium (A3-273). Tax share 28.3% vs 25.6% implied by guidance [I] High (A3-272); the 83rd report says the rate "rose higher than expected" because the impairment was not deductible [F] (A3-316). NI without the impairment: at most +9.0% (upper bound) [I] Low (A3-317) | as shown |
| FY2025 (Apr 2025-Mar 2026) | Sales +5.5% [I] High (A3-274), OI +9.9% [I] High (A3-275), NI +14.3% and EPS +13.9% [I] High (A3-276): all beats | OI without the divestiture gain +9.4%; IBT without the divestiture and call-option gains +9.8% [I] High (A3-277); a beat either way; the FY2025 Q4 (Jan-Mar 2026) one-off SG&A named by management [C] (A1-311) remains inside these figures; amount: NOT DISCLOSED (read: FY2025 Q4 briefing notes p.6 and Q&A; FY2025 Q4 slides; FY2025 tanshin; Annual Securities Report 84th MD&A and Note 23 SG&A p.161) - amount of the FY2025 Q4 one-off SG&A expenses; the FY2025 Q2 (Jul-Sep 2025) one-time SG&A charge named by management [C] (A3-093) also remains inside; amount: NOT DISCLOSED (read: FY2025 Q2 earnings briefing notes p.3 Summary and p.9; FY2025 Q2 Q&A summary; FY2025 Q2 slides; FY2025 Q2 tanshin) - an amount printed expressly for the FY2025 Q2 (Jul-Sep 2025) "one time charge related to a growth investment" | as shown |

Count over FY2023-FY2025 (Apr 2023-Mar 2026) vs the latest guidance, +/-2% band: net sales 2 beats / 1 in-line / 0 misses, OI 1 / 1 / 1, NI 1 / 0 / 2, EPS 1 / 0 / 1 of 2 (no EPS guidance for FY2023, Apr 2023-Mar 2024) [I] High (A3-319); OI without the named one-offs inside OI: 3 / 0 / 0 [I] Medium (A3-320).

- FY2022 (Apr 2022-Mar 2023, context): guidance maintained at Q3, every line in-line [I] High (A3-262).
- **Guidance maintained late in the period and then missed.** In FY2023 (Apr 2023-Mar 2024) and FY2024 (Apr 2024-Mar 2025) the guidance set at the Q3 release (a raise in both years) was not revised again before the year-end results and was missed on profit lines [I] High (A3-278); the news indexes list no later notice [F] (A3-261, A3-254, A3-232). In both years the named Q4 impairment explains the operating-income miss: FY2023 OI without it beats [I] Medium (A3-267); FY2024 OI was in line [I] High (A3-270) and the NI miss sits below IBT [I] High (A3-272). FY2025 (Apr 2025-Mar 2026) had no miss [I] High (A3-278). Absence of later revisions rests on the English IR news indexes and forecast page [F] (A3-232, A3-233, A3-254, A3-261, A3-109); the public TDnet daily lists for 28 Oct-21 Nov 2026 hold 8 Advantest items, none titled as a forecast revision [I] High (A3-322); earlier Japanese filings were not checked: NOT RETRIEVED (tried: https://www.release.tdnet.info/inbs/I_main_00.html and the public daily lists https://www.release.tdnet.info/inbs/I_list_<page>_<YYYYMMDD>.html for 28 Oct-21 Nov 2026 - 121 plain GET requests 2026-11-21, all HTTP 200, read by calc/A3_tdnet_scan.py (no Advantest forecast revision in that window, A3-322); the public list covers only 22 Oct-21 Nov 2026, so earlier filings are outside it, and its company search is a form, not used) - Advantest's Japanese TDnet filings for FY2023 Q4 to FY2024 Q4 (Jan 2024-Mar 2025), to check for forecast revisions not listed on the English IR news indexes.
- **Revision direction.** FY guidance (sales and OI) was raised at 6 of 6 in-year releases in the window, and at 9 consecutive in-year releases from 31 Jan 2024; the last cut was 31 Oct 2023, -23.8% on OI [I] High (A3-294, A3-263).

### 5.4 FY2026 (Apr 2026-Mar 2027) guidance

| Version (published) | Sales | OI | IBT | NI | EPS, JPY | Tag and ids |
|---|---|---|---|---|---|---|
| Initial (27 Apr 2026) | 1,420,000 | 627,500 | 629,000 | 465,500 | 641.61 | [C] (A3-094 to A3-098) |
| Raised at Q1 (29 Jul 2026) | 1,714,000 | 846,000 | 891,000 | 660,000 | 911.64 | [C] (A3-099 to A3-103) |
| Raised at Q2 (28 Oct 2026), current | 1,863,000 | 967,000 | 1,021,500 | 741,500 | 1,027.08 | [C] (A3-104 to A3-108) |

JPY m.
- Still current on 21 Nov 2026: the IR forecast page is dated 28 Oct 2026 [F] (A3-109), and the 28 Oct 2026 raise came without a separate notice [F] (A3-233); the public TDnet lists for 28 Oct-21 Nov 2026 show no Advantest forecast revision [I] High (A3-322).
- Current vs initial: sales +31.2%, OI +54.1% [I] High (A3-279). Implied operating margin by version: 44.2%, 49.4%, 51.9% [I] High (A3-280). The July raise was attributed to inference-AI test demand above April projections [C] (A3-231). No FY2026 guidance document names a one-off item inside the forecast [I] Medium (A3-321).
- 1H FY2026 (Apr-Sep 2026) sales = 45.4% of the current FY guidance; implied 2H (Oct 2026-Mar 2027) sales JPY 1,017,800 m, +20.4% on 1H; implied 2H OPM 50.1% vs 54.0% in 1H [I] High (A3-281). The 1H OPM includes the inventory write-down reversal, so no ex-item 1H figure can be shown (section 3.2). Management expects about +20% 1H to 2H [C] (A3-111), 2H OPM above 50% [C] (A3-110) and FY gross margin about 68% [C] (A3-112). FX assumption for 2H: 150 JPY/USD, 170 JPY/EUR; OI +JPY 5.8 bn per yen of weakening against the USD [C] (A3-010, A3-011).
- Guidance implies about JPY 1,075 m of net financial items in 2H vs 53,425 m in 1H, when 1H held JPY 54,171 m of valuation gains [I] Medium (A3-282).

### 5.5 MTP3 (FY2024-FY2026 three-year averages)

| Metric | Original target (25 Jun 2024) | Revised target (28 Oct 2025) | FY2024 (Apr 2024-Mar 2025) actual | FY2025 (Apr 2025-Mar 2026) actual | 3-year average with FY2026 (Apr 2026-Mar 2027) guidance |
|---|---|---|---|---|---|
| Sales | JPY 560-700 bn [C] (A3-234) | JPY 835-930 bn [C] (A3-242) | JPY 779,707 m [F] (A3-058) | JPY 1,128,610 m [F] (A3-086) | JPY 1,257.1 bn, above range [I] Medium (A3-298) |
| Operating margin | 22-28% [C] (A3-235) | 33-36% [C] (A3-243) | 29.3% [I] High (A1-389); 32.0% without the impairment [I] Medium (A3-273) | 44.2% [F] (A1-024); 44.0% without the divestiture gain [I] High (A3-277), with the FY2025 Q2 and Q4 SG&A items inside (bullet below) | 41.8% (mean of years) or 44.9% (pooled) [I] Medium (A3-299); pooled 45.4% without named one-offs [I] Medium (CL-121), which keeps the FY2025 Q4 (Jan-Mar 2026) one-off SG&A; the FY2025 Q2 (Jul-Sep 2025) one-time SG&A charge named by management [C] (A3-093) also remains inside (amounts: bullet below) |
| Net income | JPY 93-147 bn [C] (A3-236) | JPY 207-248 bn [C] (A3-244) | JPY 161,177 m [F] (A3-061) | JPY 375,353 m [F] (A3-089) | JPY 426.0 bn [I] Medium (A3-300) |
| ROIC | 18-28% [C] (A3-237) | 34-39% [C] (A3-245) | 31.5% [F] (A3-249) | 54.4% [F] (A3-250) | average stays at or below 39% only if FY2026 ROIC is 31.1% or less [I] Medium (A3-301) |
| Basic EPS | JPY 127-202 [C] (A3-238) | JPY 284-341 [C] (A3-246) | JPY 218.67 [F] (A3-062) | JPY 515.15 [F] (A3-090) | JPY 586.97 [I] Medium (A3-300) |

- These averages use FY2026 (Apr 2026-Mar 2027) guidance, not actuals. The targets assume 140 JPY/USD and 155 JPY/EUR [C] (A3-239); the October 2025 revision was made because exceeding the targets had become "more likely than before" [C] (A3-247). If the targets are simple means, the revised ranges implied FY2026 sales of about JPY 775-1,060 bn; the April 2026 initial guidance was 34% above the top [I] Low (A3-302).
- NI and margin figures include the named one-offs (FY2024 impairment, Apr 2024-Mar 2025; FY2025 divestiture and call-option gains, Apr 2025-Mar 2026); FY2026 guidance names none [I] Medium (A3-321). NI, EPS and ROIC without the named items: NOT DISCLOSED (read: FY2025 tanshin notes; Annual Securities Report 84th, Note 15(3) tax-rate reconciliation p.146 and MD&A p.50; FY2026 Q1 and Q2 tanshin; Semi-Annual Securities Report 85th) - tax effect of the named one-off items (impairment, divestiture gain, call-option gain, valuation gains), so net income and the total return ratio cannot be shown without them. The operating-margin figures without one-offs keep the FY2025 Q4 (Jan-Mar 2026) one-off SG&A [C] (A1-311): NOT DISCLOSED (read: FY2025 Q4 briefing notes p.6 and Q&A; FY2025 Q4 slides; FY2025 tanshin; Annual Securities Report 84th MD&A and Note 23 SG&A p.161) - amount of the FY2025 Q4 one-off SG&A expenses; the FY2025 Q2 (Jul-Sep 2025) one-time SG&A charge named by management [C] (A3-093) also remains inside; amount: NOT DISCLOSED (read: FY2025 Q2 earnings briefing notes p.3 Summary and p.9; FY2025 Q2 Q&A summary; FY2025 Q2 slides; FY2025 Q2 tanshin) - an amount printed expressly for the FY2025 Q2 (Jul-Sep 2025) "one time charge related to a growth investment". NOT DISCLOSED (read: FY2025 Q4 slides, MTP3 progress pages; Integrated Annual Report 2026, p.21-22; FY2026 Q2 slides) - company-computed MTP3 three-year average status. The Fourth Mid-Term Plan is due around May 2027 [C] (A3-253).

---

## 6. A4 Concentration and geography

### 6.1 Customers above 10% of net sales

| Period | Customer (basis) | Net sales, JPY m | Share of net sales |
|---|---|---|---|
| FY2025 (Apr 2025-Mar 2026) | NVIDIA Group (customer group, note 6(6)) | 243,735 [F] (A4-001) | 21.6% [I] High (A4-339) |
| FY2025 (Apr 2025-Mar 2026) | NVIDIA International, Inc. (single counterparty, Item 2 table) | 228,273 [F] (A4-406) | 20.2% as printed [F] (A4-407) |
| FY2025 (Apr 2025-Mar 2026) | Taiwan Semiconductor Manufacturing Co. | 124,922 [F] (A4-002) | 11.1% [I] High (A4-340) |
| FY2025 (Apr 2025-Mar 2026) | NVIDIA Group + TSMC | 368,657 [I] High (A4-437) | 32.7% [I] High (A4-341) |
| FY2024 (Apr 2024-Mar 2025) | TSMC | 96,158 [F] (A4-003) | 12.3% [I] High (A4-342) |
| FY2024 (Apr 2024-Mar 2025) | Samsung Group (customer group) | 87,734 [F] (A4-004) | 11.3% [I] High (A4-343) |
| FY2024 (Apr 2024-Mar 2025) | Samsung Electronics Co., Ltd. (single counterparty) | 82,795 [F] (A4-410) | 10.6% as printed [F] (A4-411) |
| FY2023 (Apr 2023-Mar 2024) | Samsung Group (the only one) | 57,725 [F] (A4-007) | 11.9% [I] High (A4-345) |

- Top five customers: about 50% of FY2025 (Apr 2025-Mar 2026) net sales [F] (A4-010), about 48% in FY2024 (Apr 2024-Mar 2025) [F] (A4-009) and about 29% in FY2023 (Apr 2023-Mar 2024) [F] (A4-011). The report does not say whether the five are groups or single entities. On the group basis the three unnamed top-five customers took 17.3 points of FY2025 sales together, each below 10% [I] Medium (A4-346).
- NVIDIA was not a 10% customer in FY2024 (Apr 2024-Mar 2025) [F] (A4-008), so its FY2024 sales were below JPY 77,971 m [I] Medium (A4-348). Sales to TSMC rose 29.9% in FY2025 (Apr 2025-Mar 2026) [I] High (A4-349). Printed single-counterparty shares equal shares computed from printed amounts [I] High (A4-435).
- Risk text: "a small number of top customers account for a substantial portion of net sales" [F] (A4-013).
- NOT DISCLOSED (read: Semi-Annual Securities Reports 85th and 84th terms, notes 5 and 8; Q1 FY26 and Q2 FY26 results, slides, notes and Q&A) - customers above 10% of net sales for any half-year or quarter.

### 6.2 Revenue by region, last four quarters (ship-to basis, JPY bn)

| Region | FY2025 Q3 (Oct-Dec 2025) | FY2025 Q4 (Jan-Mar 2026) | FY2026 Q1 (Apr-Jun 2026) | FY2026 Q2 (Jul-Sep 2026) |
|---|---|---|---|---|
| Taiwan | 103.2 [F] (A4-109) | 188.8 [F] (A4-117) | 178.6 [F] (A4-125) | 261.3 [F] (A4-133) |
| China | 65.4 [F] (A4-110) | 56.8 [F] (A4-118) | 69.4 [F] (A4-126) | 90.1 [F] (A4-134) |
| South Korea | 57.0 [F] (A4-108) | 34.5 [F] (A4-116) | 67.4 [F] (A4-124) | 64.6 [F] (A4-132) |
| Japan | 8.5 [F] (A4-107) | 7.6 [F] (A4-115) | 3.3 [F] (A4-123) | 1.8 [F] (A4-131) |
| Americas | 12.0 [F] (A4-111) | 11.6 [F] (A4-119) | 13.2 [F] (A4-127) | 15.7 [F] (A4-135) |
| Europe | 5.9 [F] (A4-112) | 6.7 [F] (A4-120) | 6.1 [F] (A4-128) | 6.1 [F] (A4-136) |
| Others | 21.8 [F] (A4-113) | 22.1 [F] (A4-121) | 29.5 [F] (A4-129) | 38.1 [F] (A4-137) |
| Total | 273.8 [F] (A4-114) | 328.1 [F] (A4-122) | 367.5 [F] (A4-130) | 477.7 [F] (A4-138) |
| China share | 23.9% [I] High (A4-354) | 17.3% [I] High (A4-355) | 18.9% [I] High (A4-356) | 18.9% [I] High (A4-357) |
| Taiwan share | 37.7% [I] High (A4-358) | 57.5% [I] High (A4-360) | 48.6% [I] High (A4-362) | 54.7% [I] High (A4-364) |
| South Korea share | 20.8% [I] High (A4-359) | 10.5% [I] High (A4-361) | 18.3% [I] High (A4-363) | 13.5% [I] High (A4-365) |
| China YoY | +26.3% [I] High (A4-366) | +27.4% [I] High (A4-367) | +77.9% [I] High (A4-368) | +72.9% [I] High (A4-369) |

- Values are data labels on the Q2 FY26 deck p.7; in every quarter the regions sum to the printed total [I] High (A4-372). The slide split is by ship-to region, "the location of customers' facilities to which products were shipped" [F] (A4-050, A4-405).
- Full years, customer-location basis (annual securities report): FY2025 (Apr 2025-Mar 2026) Taiwan JPY 569,466 m [F] (A4-025), 50.5% [I] High (A4-374); China 213,293 m [F] (A4-027), 18.9% [I] High (A4-373); South Korea 180,340 m [F] (A4-029), 16.0% [I] High (A4-375); Americas 44,474 m [F] (A4-017); Japan 25,137 m [F] (A4-015); Europe 23,149 m [F] (A4-019). Overseas sales 97.8% of total [F] (A4-049).

### 6.3 China

- Latest quarter, FY2026 Q2 (Jul-Sep 2026): JPY 90.1 bn [F] (A4-134), 18.9% of sales [I] High (A4-357), +72.9% YoY [I] High (A4-369). LTM (Oct 2025-Sep 2026): JPY 281.7 bn, 19.5% [I] High (A4-371, A4-370), +50.2% on the prior four quarters [I] High (A4-432).
- Fiscal years, customer location: 32.3% (FY2023, Apr 2023-Mar 2024) [I] High (A4-381), 22.5% (FY2024, Apr 2024-Mar 2025) [I] High (A4-377), 18.9% (FY2025, Apr 2025-Mar 2026) [I] High (A4-373). FY2025 China sales grew 21.8%, less than total sales [I] High (A4-382).
- Management, 29 Jul 2026: China "approximately 19%" of sales and has stayed around 20% [F] (A4-312); NOT DISCLOSED (read: Q1 FY26 earnings-call Q&A summary, A10) - period and basis of the "approximately 19%". China mix about 80-85% SoC, about 15% memory testers, current mix, stated 29 Jul 2026 (FY2026 Q2, Jul-Sep 2026) [C] (A4-313); "around the current 20% level or lower" until new China fabs start around 2028-2029 [C] (A4-314). On 28 Jan 2026 (FY2025 Q4, Jan-Mar 2026) management had said 20-25%, share of overall revenue, period not stated [C] (CL-132).
- Chinese SoC testers are gaining at Chinese customers in low-end devices (stated 25 Apr 2025) [C] (A4-310); the 84th report names Chinese competitors, among them Beijing Huafeng (Accotest) and Hangzhou Changchuan (CCTech) [F] (A4-304).

### 6.4 Export rules: what the company says, what the regulator text says, and the reading

| | Content | Tag and ids |
|---|---|---|
| **Company says** | Risk "Politics & Geopolitics": restrictions on providing products, technologies or maintenance to specific countries; risk "Trade Compliance": breaches could suspend or restrict shipments; it monitors export controls and runs region-specific scenarios. 1H FY2026 (Apr-Sep 2026) report: no new risks | [F] (A4-297, A4-298, A4-299, A4-302) |
| | The 7 Oct 2022 US rules would have "little direct impact"; core products "make little use of US technology" (stated 27 Oct 2022) | [C] (A4-305, A4-306) |
| | Its testers "do not represent equipment involved in manufacturing at advanced process nodes"; China exposure "not that substantial" versus peers (stated 26 Apr 2024) | [C] (A4-307, A4-308) |
| | China is navigated "carefully" under regulatory and market conditions (stated 27 Apr 2026) | [C] (A4-311) |
| | None of the 179 Advantest documents saved at the time of the A4 scan names the EAR, BIS, an ECCN, a foreign direct product rule, or Japan's FEFTA/METI list | [I] High (A4-400) |
| **Regulator text says** | Oct 2023 (88 FR 73424): ATE is not "use" equipment because testing is part of "production" [F] (A4-322); new § 744.23(a)(5) back-end exclusion [F] (A4-323), answering a comment on 3B992.b.4 test equipment [F] (A4-415); screening test used only in back-end stages does not trigger § 744.23(a)(2) or § 744.6(c)(2) [F] (A4-416); § 744.23(a)(4) narrowed to front-end equipment [F] (A4-418, A4-419) | as shown |
| | Dec 2024 (89 FR 96790): IC testers above a 20 MHz pattern rate are ECCN 3B992.b.4.b [F] (A4-326), memory testers excluded by note [F] (A4-327); 3B002.a-b covers S-parameter and microwave-IC testing [F] (A4-325); the Footnote 5 Entity List FDP scope includes 3B992 and 3B002.a-b [F] (A4-328) but only for direct products of US-origin 3D/3E software or technology [F] (A4-420); the country-wide SME FDP scope lists no tester [F] (A4-329); Japan is in Supp. No. 4 to Part 742 [F] (A4-330) | as shown |
| | Jan 2025 (90 FR 5298): § 744.11 Footnote 5 licence scope widened to 3B002 (except .c) and 3B992 for exporters headquartered in Macau or D:5 [F] (A4-421); due diligence for foundries and OSATs [F] (A4-333) | as shown |
| | Customer-side rules: Entity List additions (Dec 2024) [F] (A4-332); Affiliates rule (Sep 2025) [F] (A4-334), stayed to 10 Jan 2027 [F] (A4-336); H200-class chips to China/Macau case-by-case (Jan 2026) [F] (A4-337); remote-access and data-centre rule, effective 19 Nov 2026 [F] (A4-338), whose reprinted 3D001/3E001 headings exclude 3B992 [F] (A4-422) | as shown |
| | Japan added advanced SME to its control list on 23 Jul 2023, as recorded by BIS [F] (A4-331). NOT RETRIEVED (tried: no request from module A4; meti.go.jp returned HTTP 403 to scripted requests earlier in this run (run_log.md, 403 list), not retried) - METI originals: 23 Jul 2023 amendment adding advanced semiconductor manufacturing equipment to Japan's export control list, and any later METI semiconductor list changes (only BIS's description saved, A4-331) | as shown |
| **Reading** | Back-end-only test use is outside these end-use controls; whether wafer-level test counts as back-end is not settled in the text | [I] Medium (A4-403) |
| | Testers appear only in 3B002.a-b and 3B992.b.4; any reach to Advantest through the Footnote 5 FDP rule depends on its ECCNs and US content; NOT DISCLOSED (read: Annual Securities Report 84th term, risk factors c. Politics & Geopolitics and d. Trade Compliance; IR Business Risks web page 2026-11-21; Integrated Annual Report 2026 risk table; Semi-Annual Securities Report 85th term, Risk Factors) - which specific export rules bind Advantest (US EAR Entity List, foreign direct product rules, advanced-computing / semiconductor-manufacturing-item rules), the ECCN classification of its testers and their US-origin content | [I] Medium (A4-401); [I] Low (A4-402) |
| | The Jan 2025 widening reaches China-headquartered tester makers rather than Advantest | [I] Low (A4-436) |
| | The 2025-2026 rules reach Advantest mainly through its customers, e.g. NVIDIA Group and TSMC (32.7% of FY2025, Apr 2025-Mar 2026, sales) [I] High (A4-341) and China-located customers (18.9%) [I] High (A4-373); no saved document quantifies any effect | [I] Medium (A4-404) |

### 6.5 Restatement check

- Within the compared set (0 of 102 region, customer and segment pairs [I] High (A4-386); 0 of 195 statement line items [I] High (A4-387); 0 of 65 quarter-items [I] High (A4-388)) no prior-period figure changed without an explanation [I] Medium (A4-399). Outside that set one did: MTP2 (FY2021-FY2023, Apr 2021-Mar 2024) average ROIC, 21.2% in the 82nd Annual Securities Report (26 Jun 2024) [F] (A3-304) vs 25.5% in the FY2024 Q4 slides (25 Apr 2025) [F] (A3-305), gap 4.3 pts [I] High (A3-303). The simple mean of the annual series matches 25.5% [I] Medium (A3-307). NOT DISCLOSED (read: MTP3 press release 2024-06-25 p.3; MTP3 slides 2024-06-25 p.31; 82nd Annual Securities Report p.18; FY2024 Q4 slides p.16; Integrated Annual Report 2026 p.77) - reconciliation of the MTP2 (FY2021-FY2023, Apr 2021-Mar 2024) average ROIC figure (21.2% in the press release and securities report vs 25.5% in both slide decks; the IAR annual series averages 25.5%).
- The explained change is the segment restatement from FY2025 Q1 (Apr-Jun 2025) ("after the changes of the reportable segments") [F] (A4-242): JPY 11,511 m of FY2024 (Apr 2024-Mar 2025) sales moved into Test System [I] High (A4-389); total segment income JPY 231,054 m is unchanged [F] (A4-241). Inside it, the Corporate adjustment shrank by 3,898 [I] Medium (A4-390), a second change that has no specific explanation. NOT DISCLOSED (read: Annual Securities Report 84th term, note 6(1) Overview of Reportable Segments; FY2025 financial results, Segment Information) - explanation of the change in the "Elimination and Corporate" adjustment in restated FY2024 (Apr 2024-Mar 2025) segment income ((18,839) to (14,941) JPY million).
- One-off inside these segment figures: the FY2024 (Apr 2024-Mar 2025) Essai impairment of JPY 21,393 m sits in the services segment on both bases [F] (A4-425); without it, FY2024 total segment income is JPY 252,447 m [I] High (A4-430). 1H FY2025 (Apr-Sep 2025) Services and Others income is JPY 544 m without the 2,504 m divestiture income [I] High (A4-431).
- Orders cannot be checked: NOT DISCLOSED (read: FY2025 Q1-Q4 and FY2026 Q1-Q2 financial results and briefing slides; Annual Securities Report 84th term, Item 2 a. Results of Production and Orders received) - orders received and backlog.

---

## 7. A5 Balance sheet and capital

### 7.1 Cash, debt and net cash (JPY m)

| Date | Cash and equivalents | Borrowings | CB liability (carrying) | Lease liabilities (current + non-current) |
|---|---|---|---|---|
| 31 Dec 2025 (FY2025 Q3 end) | 329,322 [F] (A5-008) | 75,651 [F] (A5-009) | none (CB issued 20 Apr 2026 [F] (A5-060)) | 4,403 + 11,149 [F] (A5-010, A5-011) |
| 31 Mar 2026 (FY2025 end) | 339,966 [F] (A5-001) | nil [F] (A5-003, A5-004) | none (CB issued 20 Apr 2026 [F] (A5-060)) | 4,966 + 15,226 [F] (A5-005, A5-006) |
| 30 Jun 2026 (FY2026 Q1 end) | 413,124 [F] (A5-012) | none shown on the statement [F] (A5-013) | 88,930 [F] (A5-013) | 4,977 + 14,259 [F] (A5-014, A5-015) |
| 30 Sep 2026 (FY2026 Q2 end) | 401,785 [F] (A5-017) | none; facilities undrawn [F] (A5-043) | 89,486 [F] (A5-018) | 4,820 + 12,940 [F] (A5-019, A5-020) |

| Net cash at 30 Sep 2026 (FY2026 Q2 end) | Value | Tag and ids |
|---|---|---|
| Cash less CB at carrying amount, leases excluded | 312,299 | [I] High (A5-202) |
| Same, leases included | 294,539 | [I] High (A5-203) |
| Cash less CB at face value 100,000, leases excluded | 301,785 | [I] High (A5-204) |
| Same, leases included | 284,025 | [I] High (A5-205) |

- Earlier points: 253,671 at 31 Dec 2025 (FY2025 Q3 end) [I] High (A5-207); 339,966 at 31 Mar 2026 (FY2025 end) [I] High (A5-200), equal to the company's own net interest-bearing debt of (339,966) [F] (A5-024); 324,194 at 30 Jun 2026 (FY2026 Q1 end) [I] High (A5-206). The company counts borrowings only as interest-bearing debt [F] (A5-025). The JPY 75,651 m loan outstanding at 31 Dec 2025 (FY2025 Q3 end) [F] (A5-009) was repaid in FY2025 (Apr 2025-Mar 2026), a financing outflow of (75,352) [F] (A5-044).
- Not in net cash: investment securities JPY 432,586 m at 30 Sep 2026 (FY2026 Q2 end) [F] (A5-021), up from 67,927 m at 31 Mar 2026 (FY2025 end) [F] (A5-239): equity stakes at FVTOCI 203,670 m [F] (A5-026) and investment-fund LP interests at FVTPL (Level 3) 228,916 m [F] (A5-027). Maximum loss exposure equals carrying amount [F] (A5-028); no obligation to contribute more [F] (A5-232). A USD 570 m contribution to a Delaware fund was made in FY2026 Q1 (Apr-Jun 2026) [F] (A5-029). Fund-interest purchases were JPY 184,365 m in 1H FY2026 (Apr-Sep 2026) [F] (A1-160); the USD 570 m is the one contribution identified, and management calls the FY2026 Q2 (Jul-Sep 2026) outflows "a substantial amount of strategic investments" [C] (A1-350). NOT DISCLOSED (read: Semi-Annual Securities Report 85th, Note 12 Structured Entities; Annual Securities Report 84th, Note 33) - name and manager of the investment fund(s) holding JPY 228,916 m at 30 Sep 2026 (FY2026 Q2 end). Named stakes at 31 Mar 2026 (FY2025 end): Technoprobe JPY 42,774 m [F] (A5-031), PDF Solutions 17,294 m [F] (A5-032), Micronics Japan 1,386 m [F] (A5-237).
- Liquidity: cash plus undrawn facilities JPY 541,785 m at 30 Sep 2026 (FY2026 Q2 end) [I] High (A5-208); committed line JPY 40.0 bn and overdraft JPY 100.0 bn [F] (A5-042). Equity JPY 1,145,135 m at 30 Sep 2026 (FY2026 Q2 end) [F] (A5-023).

### 7.2 Maturities, rates, covenants, ratings

- The only debt maturity is the CB principal of JPY 100 bn due 28 Mar 2031 (FY2030 Q4, Jan-Mar 2031) [F] (A5-063, A5-055). Lease contractual cash flows at 31 Mar 2026 (FY2025 end): JPY 21,622 m, of which 5,277 m within one year [F] (A5-050).
- The repaid loan carried an average rate of 1.24% at 31 Mar 2025 (FY2024 end) [F] (A5-045); no assets pledged [F] (A5-048). Interest expense FY2025 (Apr 2025-Mar 2026): JPY 1,271 m at amortised cost [F] (A5-051) plus 976 m on FVTPL liabilities [F] (A5-234).
- NOT DISCLOSED (read: Annual Securities Report 84th, Note 17 Borrowings, Note 30 Financial Instruments, MD&A Liquidity and Capital Resources, Note 33 Subsequent Events; Semi-Annual Securities Report 85th, Item2 (2) Liquidity, Item3 CB terms, Note 11) - financial covenants on loans, committed line of credit, overdraft or the CB. The CB is unsecured and unguaranteed [F] (A5-071).
- Rating: R&I issuer rating AA- [Stable] since 22 Jul 2026, A+ before; R&I is the only agency listed [F] (A5-053, A5-054).

**Zero Coupon Convertible Bonds due 2031**

| Term | Value | Tag and ids |
|---|---|---|
| Resolution / payment | 1 Apr 2026 / 20 Apr 2026 | [F] (A5-060) |
| Principal; offer price | JPY 100 bn, 10,000 bonds; offer 102.5%, paid-in 100.0% | [F] (A5-061, A5-062) |
| Coupon; maturity | none; 28 Mar 2031 | [F] (A5-064, A5-063) |
| Conversion price | JPY 36,000 at issue [F] (A5-065); JPY 35,946.5 from 1 Oct 2026 after the JPY 49 interim dividend triggered an adjustment [F] (A5-075, A5-076) | as shown |
| Conversion restriction | to 31 Mar 2030: share price above 150% of the conversion price over 20 trading days ending a calendar quarter [F] (A5-068); 1 Apr-28 Dec 2030: 130% [F] (A5-069); lifted if R&I rating is BBB- or lower [F] (A5-070) | as shown |
| Shares on full conversion | 2,780,000 to 2,781,912 shares, 0.380% of issued shares at 30 Sep 2026 (FY2026 Q2 end) | [I] Medium (A5-217) |
| IFRS split | liability JPY 88.9 bn at 30 Jun 2026 (FY2026 Q1 end) [F] (A5-077); equity component JPY 7,712 m [F] (A5-078); fair value JPY 88,610 m at 30 Sep 2026 (FY2026 Q2 end) [F] (A5-079); implied accretion about 2.50% a year [I] Low (A5-218); NOT DISCLOSED (read: Semi-Annual Securities Report 85th, Note 11; FY2026 Q1 and Q2 briefing notes) - effective interest rate of the CB liability component, initial liability amount at issue and transaction costs | as shown |
| Planned use of proceeds | about JPY 50 bn tester capacity by Mar 2029, JPY 20 bn inventory by Mar 2027, JPY 30 bn next-generation test development by Mar 2028 | [C] (A5-072, A5-073, A5-074) |
| CFO account (11 Nov 2026) | expected dilution about 0.4% [C] (A5-082); investor demand about eight times the issue [C] (A5-085); conversion premium 60% [F] (A5-081) | as shown |

NOT RETRIEVED (tried: https://www.advantest.com/document/en/investors/aad/E_Info_20260401_02.pdf, _03.pdf, _04.pdf - HTTP 403 to scripted request, not retried) - CB offering notices with early-redemption terms (issuer call, clean-up call, put) and lock-up terms (see gaps.md, "Files the user can save by hand").

NOT DISCLOSED (read: Semi-Annual Securities Report 85th, Item3 1.(2) sub-item 2 and Notes 1-6; Annual Securities Report 84th, Item4 stock acquisition rights pp.60-61 and Note 33) - CB early-redemption terms (issuer call, clean-up call threshold, bondholder put dates) and events of default; only references to "early redemption", "Clean-up Redemption Notice" and "Events of Default" appear

### 7.3 Shareholder returns

- MTP3 policy (FY2024-FY2026, Apr 2024-Mar 2027): minimum annual dividend JPY 30 per share [C] (A5-090); cumulative total return ratio of 50% or more [C] (A5-091); total return ratio = (dividend + share repurchase) / net income [F] (A5-092).

| Programme resolved | Cap (shares / yen) | Window | Executed | Tag and ids |
|---|---|---|---|---|
| 30 Oct 2024 | 9.0 m / JPY 50 bn | 1 Nov 2024-26 Feb 2025 (FY2024 Q3-Q4) | 5,711,000 shares, JPY 49,999,998,563, completed 28 Jan 2025 (FY2024 Q4) | [F] (A5-094, A5-095) |
| 25 Apr 2025 | 19.0 m / JPY 70 bn | 7 May-22 Sep 2025 (FY2025 Q1-Q2) | 6,643,900 shares, JPY 69,999,937,500 | [F] (A5-096, A5-097) |
| 28 Oct 2025 | 18.0 m / JPY 150 bn | 4 Nov 2025-28 Oct 2026 (FY2025 Q3-FY2026 Q3) | 5,759,000 shares, JPY 149,996,716,000, completed 19 Aug 2026 (FY2026 Q2) | [F] (A5-098, A5-101) |
| 28 Oct 2026 | 11.0 m (1.5%) / JPY 280 bn | 29 Oct 2026-24 Mar 2027 (FY2026 Q3-Q4) | 420,900 shares, JPY 14,563,326,000 by 31 Oct 2026 (FY2026 Q3) | [F] (A5-102, A5-104) |

- Each completed programme used 100.0% of its yen cap but only 32-64% of its share cap [I] High (A5-216). After 31 Oct 2026, JPY 265,436.7 m of the October 2026 authorisation remained, 66.1% of cash at 30 Sep 2026 (FY2026 Q2 end); it is a cap, not a commitment [I] High (A5-215). The stated reason was the FY2026 (Apr 2026-Mar 2027) forecast and cash on hand [C] (A5-127).
- Cancellation of 34,141,256 treasury shares on 6 Feb 2026 [F] (A5-105); issued shares 732,000,000 at 30 Sep 2026 (FY2026 Q2 end) [F] (A5-108), 721,952,905 outstanding [F] (A5-103).
- Dividends per share: FY2024 (Apr 2024-Mar 2025) JPY 39.00, payout 17.8% [F] (A5-116); FY2025 (Apr 2025-Mar 2026) JPY 59.00, payout 11.5% [F] (A5-115); FY2026 (Apr 2026-Mar 2027) interim JPY 49, total JPY 35,376 m [F] (A5-114); year-end: NOT DISCLOSED (read: interim dividend notice E_Info_20261028_03 p.1, dividend table; FY2026 Q2 Consolidated Financial Results p.1, 2. Dividends; IR web page IR Calendar 2026-11-21, FY2026 Yearly Calendar) - FY2026 (Apr 2026-Mar 2027) year-end dividend per share (printed as "TBD" in the interim dividend notice and "-" in the tanshin forecast row).
- Total return ratio as printed: 49% (FY2024, Apr 2024-Mar 2025), 42% (FY2025, Apr 2025-Mar 2026) [F] (A5-225); recomputed 48.8% and 41.9% with dividends by record date [I] High (A5-212, A5-213, A5-236). Cumulative FY2024 to 1H FY2026 (Apr 2024-Sep 2026): 41.7%, below the 50% target with 2H FY2026 (Oct 2026-Mar 2027) still to come [I] Medium (A5-214).
- One-offs inside the net income used: FY2024 (Apr 2024-Mar 2025) impairment (21,393) [F] (A5-167); FY2025 (Apr 2025-Mar 2026) call-option gain 17,312 [F] (A5-230) and divestiture gain 2,504 [F] (A5-156); 1H FY2026 (Apr-Sep 2026) valuation gains 54,171 [F] (A5-228) and the inventory write-down reversal [C] (A5-229). Ratios without them: NOT DISCLOSED (read: Annual Securities Report 84th, Note 15(3) tax-rate reconciliation p.146 and MD&A p.50; FY2025 tanshin notes; Semi-Annual Securities Report 85th) - tax effect of the named one-off items.

### 7.4 M&A since November 2021, and impairments

| Target (country, business) | Closed | Consideration, JPY m | Goodwill (final), JPY m | Tag and ids |
|---|---|---|---|---|
| R&D Altanova (US, test interface boards) | 17 Nov 2021 | 25,521 cash | 18,946 | [F] (A5-131, A5-132, A5-133) |
| CREA (Italy, power-device test) | 10 Aug 2022 | 4,167 | 1,449 | [F] (A5-139, A5-140, A5-141) |
| Shin Puu Technology (Taiwan, PCBs) | 28 Apr 2023 | 7,497 cash | 2,522 | [F] (A5-145, A5-146, A5-147) |
| Salland Engineering (Netherlands, test instruments and services) | 2 Apr 2024 | 4,818 | 3,004 | [F] (A5-150, A5-151, A5-152) |

- The four deals cost JPY 42,003 m, of which 25,921 m (61.7%) was goodwill [I] High (A5-219). No business combination in FY2025 (Apr 2025-Mar 2026) [F] (A5-155). A partial divestiture brought JPY 2,504 m of income in FY2025 [F] (A5-156).
- The 1H FY2026 (Apr-Sep 2026) strategic investments, fund interests of JPY 184,365 m [F] (A1-160) and equity instruments of 26,053 m [F] (A1-161), are not business combinations; they are covered in section 7.1.
- Impairments: Essai (acquired Jan 2020 for JPY 33,576 m [F] (A5-170)) goodwill JPY 8,998 m in FY2023 (Apr 2023-Mar 2024) [F] (A5-168) and goodwill and intangibles JPY 21,393 m in FY2024 (Apr 2024-Mar 2025) [F] (A5-167), for softer sales to a major customer [F] (A5-169). Goodwill and acquired-intangible impairments over FY2021-FY2025 (Apr 2021-Mar 2026) total JPY 30,391 m, all on Essai, 90.5% of its price; none on the four deals above [I] High (A5-220).
- Goodwill and intangibles JPY 82,520 m at 30 Sep 2026 (FY2026 Q2 end) [F] (A5-022), 7.2% of equity [I] High (A5-222). Largest CGU: R&D Altanova goodwill JPY 29,383 m at 31 Mar 2026 (FY2025 end) [F] (A5-171); at 31 Mar 2026 (FY2025 end) discount rate 20.2% vs break-even 22.5% [F] (A5-176, A5-177); headroom from 3.5 points at 31 Mar 2025 (FY2024 end) to 2.3 points at 31 Mar 2026 (FY2025 end) [I] High (A5-221). The CGU figure exceeds R&D Altanova's acquisition goodwill (18,946 m [F] (A5-133)); Shin Puu goodwill (2,522 m) is inferred to sit in the same CGU [I] Medium (A5-223); the rest of the bridge (exchange differences) cannot be shown: NOT DISCLOSED (read: Annual Securities Report 84th, Note 12(1) Increase or Decrease Table and Note 12(2) Impairment Test for Goodwill pp.134-136) - goodwill roll-forward by CGU (acquisitions and exchange differences are given only for total goodwill), so the bridge from R&D Altanova's acquisition goodwill (18,946 million) to the R&D Altanova CGU's 29,383 million at 31 Mar 2026 (FY2025 end) cannot be shown.
- Minority stakes (not business combinations): 2.5% of Technoprobe [F] (A5-159); a FormFactor stake, a plan at the announcement [C] (A5-160), NOT DISCLOSED (read: News 2025-01-09 Strategic Partnerships with FormFactor and Technoprobe; Annual Securities Report 84th, Item4 (5) Status of Shareholdings pp.107-108 and Note 30(7)) - size of the FormFactor minority stake (subsidiaries' other listed holdings are shown only as "Other", 2 companies, JPY 5,337 m at 31 Mar 2026 (FY2025 end) [F] (A5-240)); Micronics Japan, 150,000 shares held at 31 Mar 2025 (FY2024 end) and 31 Mar 2026 (FY2025 end), JPY 1,386 m at 31 Mar 2026 (FY2025 end) [F] (A5-237).
- Capital-allocation statements: growth investment first, debt used flexibly [C] (A5-185); MTP3 strategic investments of about JPY 100 bn [C] (A5-186); cash on hand of JPY 100-120 bn at end FY2026 (31 Mar 2027) [C] (A5-190), against JPY 401,785 m at 30 Sep 2026 (FY2026 Q2 end) [F] (A5-017).

---

## 8. A6 Cycle

### 8.1 Definition and its sensitivity

- Definition used: a downturn is a fall of trailing-four-quarter (T4Q) net sales at least 5% below its running peak; the peak quarter is the highest single quarter among the four in the T4Q peak, the trough the lowest single quarter after it. The quarterly series is IFRS only, FY2015 Q1 (Apr-Jun 2015) to FY2026 Q2 (Jul-Sep 2026) [I] High (A6-270); company-printed quarters agree with the derived ones in 37 of 37 cases [I] High (A6-271).
- Only three T4Q drawdowns of 1% or more exist since FY2015 Q4 (Jan-Mar 2016): -6.55% (T4Q to FY2016 Q1, Jul 2015-Jun 2016 -> T4Q to FY2016 Q2, Oct 2015-Sep 2016), -5.17% (T4Q to FY2018 Q3, Jan-Dec 2018 -> T4Q to FY2019 Q3, Jan-Dec 2019), -13.15% (T4Q to FY2022 Q4, Apr 2022-Mar 2023 -> T4Q to FY2023 Q4, Apr 2023-Mar 2024). With the 5% threshold the last two downturns are 2022-23 and 2018-19, but 2018-19 clears it by 0.17 pp; above 5.17% the pair becomes 2022-23 and 2015-16 [I] High (A6-350); [I] Medium (A6-273). A single-quarter >=15% rule selects FY2015 Q2->Q3 (Jul-Sep to Oct-Dec 2015, -35.3%), FY2016 Q4->FY2017 Q1 (Jan-Mar to Apr-Jun 2017, -15.8%) and FY2022 Q4->FY2023 Q1 (Jan-Mar to Apr-Jun 2023, -31.3%), not 2018-19 (-14.6%) [I] High (A6-274).

### 8.2 The two downturns, with and without one-offs

| Metric | 2022-23: FY2022 Q4 (Jan-Mar 2023) -> FY2023 Q1 (Apr-Jun 2023) | 2018-19: FY2018 Q3 (Oct-Dec 2018) -> FY2018 Q4 (Jan-Mar 2019) |
|---|---|---|
| Net sales, JPY m | 147,392 -> 101,251 [I] High (A6-275, A6-276) | 74,920 -> 63,959 [I] High (A6-287, A6-288) |
| Sales change | -31.3% [I] High (A6-277); printed -31.3% [F] (A6-326) | -14.6% [I] High (A6-289); printed -14.6% [F] (A6-323) |
| Operating income, JPY m | 38,547 -> 14,269 (-63.0%) [I] High (A6-278) | 20,703 -> 10,196 (-50.8%) [I] High (A6-290) |
| Operating margin, reported | 26.2% -> 14.1%, -12.1 pp [I] High (A6-279); printed 26.2% and 14.1% [F] (A6-170, A6-171) | 27.6% -> 15.9%, -11.7 pp [I] High (A6-291); printed [F] (A6-167, A6-168, A6-325) |
| One-offs named by management | ~JPY 3 bn inventory valuation losses in FY2022 Q4 (Jan-Mar 2023) [F] (A6-219); none in FY2023 Q1 (Apr-Jun 2023) | JPY 2.5 bn pension-transfer gain in FY2018 Q3 (Oct-Dec 2018) [F] (A6-208); ~JPY 2 bn inventory valuation loss in FY2018 Q4 (Jan-Mar 2019) [F] (A6-314) |
| Operating margin without all named one-offs | 28.2% -> 14.1%, -14.1 pp [I] Medium (A6-280) | 24.3% -> 19.1%, -5.2 pp [I] Medium (A6-292) |
| Without named items other than inventory losses | equals reported, -12.1 pp [I] High (A6-279) | 24.3% -> 15.9%, -8.4 pp [I] Medium (A6-351) |
| Duration | 1 quarter peak to trough; sales back above the peak in FY2024 Q2 (Jul-Sep 2024), 6 quarters after [I] High (A6-282) | 1 quarter; back above the peak in FY2020 Q2 (Jul-Sep 2020), 7 quarters after [I] High (A6-293) |
| T4Q view | T4Q to FY2022 Q4 (Apr 2022-Mar 2023) 560,191 -> T4Q to FY2023 Q4 (Apr 2023-Mar 2024) 486,507 (-13.2%) [I] High (A6-283); T4Q OM 29.9% -> 16.8% (-13.2 pp), without one-offs 30.5% -> 18.0% (-12.5 pp) [I] Medium (A6-284) | T4Q to FY2018 Q3 (Jan-Dec 2018) 286,432 -> T4Q to FY2019 Q3 (Jan-Dec 2019) 271,627 (-5.2%) [I] High (A6-294); T4Q OM 23.8% -> 21.1% (-2.7 pp), without one-offs 22.6% -> 21.8% (-0.8 pp) [I] Medium (A6-295) |
| Other one-offs in the window | 1H FY2023 (Apr-Sep 2023) settlement income JPY 3,179 m [F] (A6-220), placed in FY2023 Q2 (Jul-Sep 2023) by inference: OM 18.1% reported, 15.3% without [I] Medium (A6-286); FY2023 Q4 (Jan-Mar 2024) goodwill impairment JPY 8,998 m [F] (A6-221): OM 14.4% reported, 21.0% without [I] High (A6-285) | FY2018 (Apr 2018-Mar 2019) total one-off profit JPY 3.5 bn [F] (A6-209), incl. a 1H FY2018 (Apr-Sep 2018) ~1.0 bn fixed-asset gain [F] (A6-214), placed in FY2018 Q2 (Jul-Sep 2018) by inference: OM 24.7% reported, 23.3% without [I] Medium (A6-296); FY2019 Q1 (Apr-Jun 2019) inventory valuation losses [F] (A6-315) and a one-time amortisation on the transferred SLT business, named in the FY2019 Q3 release for 9M FY2019 (Apr-Dec 2019) [F] (A6-215), both named without amounts (lines below the table) |

- The FY2019 (Apr 2019-Mar 2020) ex-one-off figures (T4Q 21.8% to FY2019 Q3, Jan-Dec 2019 [I] Medium (A6-295); fiscal-year FY2018 (Apr 2018-Mar 2019) -> FY2019 (Apr 2019-Mar 2020) -1.1 pp [I] Medium (A6-303); and the window to FY2019 Q4 (Jan-Mar 2020) [I] Medium (A6-352)) still contain the two FY2019 items named without amounts: NOT DISCLOSED (read: FY2019 Third Quarter Consolidated Financial Results, Services, Support and Others segment; FY2019 Consolidated Financial Results, segment section; Annual Financial Report FY2019 (78th term), MD&A p.81 and segment D&A note) - amount of the one-time amortisation expense on the transferred system-level test business (FY2019 Q3 (Oct-Dec 2019) / FY2019 (Apr 2019-Mar 2020)); NOT DISCLOSED (read: FY2019 1Q Information Meeting Q&A p.3; FY2019 First Quarter Consolidated Financial Results, Overview of Business Results) - amount of the FY2019 Q1 (Apr-Jun 2019) inventory valuation losses that management named as a gross-margin factor.
- The judgement inside the ex-one-off figures: inventory valuation losses recur every year (JPY 2,728-7,347 m a year over FY2018-FY2023, Apr 2018-Mar 2024) [F] (A6-317, A6-318, A6-319, A6-320, A6-321, A6-322). The amounts management named for single quarters are about 32% (FY2018 Q4, Jan-Mar 2019) and 47% (FY2022 Q4, Jan-Mar 2023) of their years [I] Medium (A6-353). Treating them as one-offs narrows the 2018-19 margin drop from -8.4 pp to -5.2 pp [I] Medium (A6-351, A6-292) and widens the 2022-23 drop from -12.1 pp [I] High (A6-279) to -14.1 pp [I] Medium (A6-280).
- Highest to lowest quarterly margin: 2022-23, FY2022 Q1 (Apr-Jun 2022) 32.9% -> FY2023 Q1 (Apr-Jun 2023) 14.1% (-18.8 pp), no one-offs named in either quarter [I] High (A6-281); 2018-19 ex one-offs, FY2018 Q3 (Oct-Dec 2018) 24.3% -> FY2019 Q4 (Jan-Mar 2020) 17.0% (-7.3 pp) [I] Medium (A6-352).
- Fiscal-year view: FY2022 (Apr 2022-Mar 2023) -> FY2023 (Apr 2023-Mar 2024) sales -13.2%, OM -13.2 pp reported, -12.5 pp without one-offs [I] Medium (A6-302); FY2018 (Apr 2018-Mar 2019) -> FY2019 (Apr 2019-Mar 2020) sales -2.3%, OM -1.6 pp, -1.1 pp without [I] Medium (A6-303).
- Older cycles (U.S. GAAP, annual): FY2011 (Apr 2011-Mar 2012) -> FY2013 (Apr 2013-Mar 2014) sales -20.7%, OM 0.6% -> -32.5%, or -16.9% without the named inventory losses and impairment [I] Medium (A6-305); FY2007 (Apr 2007-Mar 2008) -> FY2009 (Apr 2009-Mar 2010) sales -70.9%, OM 12.4% -> -21.9% [I] Medium (A6-306); operating-margin trough FY2008 (Apr 2008-Mar 2009): -64.5% reported, -28.5% without the named inventory valuation, restructuring and PP&E impairment charges [I] Low (A6-307); no one-off named in FY2007 or FY2009, so their margins are the same with and without [I] Medium (A6-306).
- The 2018-19 fall was memory-led by the company's own market estimates: memory tester market USD 1,150 m -> 650 m from CY2018 to CY2019 [C] (A6-260, A6-261), SoC tester market USD 2,550 m -> 2,700 m [C] (A6-254, A6-255); -43.5% vs +5.9% [I] Medium (A6-308).
- Management's explanations: customers' inventory adjustments and capex cuts from 2H 2018 [C] (A6-241); in 2023, excess capacity built over the prior three years of customer investment [C] (A6-248), and a lower mix of higher-margin products at the trough [C] (A6-249).
- Accounting breaks: IFRS 15 from FY2018 Q1 (Apr-Jun 2018) and IFRS 16 from FY2019 Q1 (Apr-Jun 2019), both without restating prior years [F] (A6-331, A6-333). NOT DISCLOSED (read: FY2018 First Quarter Consolidated Financial Results and FY2018 Consolidated Financial Results, Changes in accounting policies) - effect of IFRS 15 on FY2018 quarterly net sales and operating income.
- For scale: FY2026 Q2 (Jul-Sep 2026) operating margin 55.9% [F] (A1-064) and LTM (Oct 2025-Sep 2026) 50.0% [I] High (A6-312), with the reversal named for FY2026 Q1 (Apr-Jun 2026) and 1H (Apr-Sep 2026) unquantified; the last two trough margins were 14.1% (FY2023 Q1, Apr-Jun 2023, no one-off named) [I] High (A6-279) and 15.9% (FY2018 Q4, Jan-Mar 2019) [I] High (A6-291), 19.1% without the named ~JPY 2 bn inventory loss [I] Medium (A6-292).

---

## 9. Theme and technology

### 9.1 Exposure: what the company discloses

NOT DISCLOSED (read: Q3 FY2025 Financial Briefing Q&A A4; Q2 FY26 Financial Briefing slides p.15-16; Investors Guide 2610 Ch.1 p.5; Annual Securities Report 84th term; Semi-Annual Securities Report 85th term) - AI, HBM or advanced-packaging share of revenue. The stated policy is no breakdown below "Computing and Communications" [F] (TH-126); management says the majority of that category is HPC/AI, with no number [C] (TH-205).

| Measure | FY2024 (Apr 2024-Mar 2025) | FY2025 (Apr 2025-Mar 2026) | FY2026e (Apr 2026-Mar 2027) |
|---|---|---|---|
| SoC tester sales, JPY bn | 440.4 [F] (TH-130) | 767.4 [F] (TH-129) | 1,375.0 forecast [C] (TH-131) |
| "Computing / Communications" share of SoC tester sales, rounded to 5% | 90% [F] (TH-127) | 95% [F] (TH-127) | 90% forecast [C] (A1-297) |
| Proxy, not an AI share: that category as % of net sales | 50.8% (49.4-52.2) [I] Low (TH-190) | 64.6% (62.9-66.3) [I] Low (TH-190, A1-469) | 66.4% (64.6-68.3) [I] Low (TH-190) |
| SoC test systems as % of net sales | 56.5% [I] High (TH-192) | 68.0% [I] High (TH-192) | 1H FY2026 (Apr-Sep 2026): 72.5% [I] High (TH-192) |
| DRAM share of memory tester sales, rounded to 5% | 95% [F] (TH-059) | 90% [F] (TH-059) | 85% forecast [C] (TH-207) |
| Proxy: DRAM tester sales (HBM inside, not split) as % of net sales | 19.2% (18.7-19.7) [I] Medium (TH-209) | 13.7% (13.3-14.1) [I] Medium (TH-191) | 10.4% (10.1-10.8), on forecasts: memory JPY 229.0 bn [C] (TH-208), DRAM 85% [C] (TH-207), sales [C] (TH-134) [I] Low (TH-210) |

- The category includes smartphone application processors [F] (TH-128), so the proxy overstates AI/HPC; modules A1 and TH both rate it Low [I] Low (A1-469, TH-190). At market level, Computing and Communications was about 80% of the CY2025 SoC tester TAM (the whole category, not HPC/AI alone) [C] (TH-124).
- Hybrid bonding, inspection and metrology: see the premise check (section 1). Exposure to HBM and 3D stacks runs through testing dies before stacking, the stacks and the packages [I] High (TH-193, TH-194).

### 9.2 The test-intensity thesis, and its limits, in the company's own words

| Statement | Tag and ids |
|---|---|
| Test volume growth is structural, driven by complexity (stated 28 Nov 2024); scan test volume grew "explosively" with transistor counts | [C] (TH-021, TH-027) |
| More dies per package lengthen test time; die-to-die interconnects add test items; 2020s flows add die-level insertions plus multi-temperature, burn-in and SLT | [C] (TH-025, TH-026, TH-029) |
| Test demand now driven more by test content than by production volume (stated 30 Oct 2024); high ASPs make customers test more rather than scrap | [C] (TH-031, TH-032) |
| "In some cases" test times rise "by multiples" from one generation to the next (CEO, stated 12 Nov 2026) | [C] (TH-034) |
| CPU test demand for agentic AI is the largest factor in the raised FY2026 (Apr 2026-Mar 2027) SoC forecast (stated 28 Oct 2026) | [C] (TH-041) |
| Tester TAM has grown about 50% a year or slightly above over the past few years; no slowdown seen (stated 28 Oct 2026) | [C] (TH-042) |
| Limits: test times, volume and insertions are "very difficult to predict" and stay uncertain until silicon; customers write more efficient patterns to cut scan test time | [C] (TH-022, TH-035, TH-023) |
| Limits: part of the ~30% CY2025 SoC TAM raise reflected earlier caution, and the rest leaned to unit volume; CY2026 TAM growth comes mainly from custom-ASIC unit volume | [C] (TH-038, TH-039) |

Advantest's growth explanation mixes test intensity and unit volume, and no test-time-per-device series is disclosed [I] Medium (TH-197).

### 9.3 Share claims against the company's own arithmetic

| Item | Value | Tag and ids |
|---|---|---|
| Overall tester share | 58% (CY2023), 58% (CY2024), 65% (CY2025) | [C] (TH-120, TH-115) |
| SoC tester share | 56% (CY2024), 66% (CY2025); "path to above 70%" | [C] (TH-116, TH-117) |
| Memory tester share | 63% (CY2024), 61% (CY2025); may decline in CY2026 | [C] (TH-119, TH-061) |
| AI accelerator test | "Captured a majority share of the market globally" (no number) | [C] (TH-118) |
| Check: SoC sales / own SoC TAM | 56.6% (CY2024), 66.0% (CY2025): in line with the claims | [I] Medium (TH-204, TH-180) |
| Check: memory sales / own memory TAM | 54.3% (CY2024), 54.0% (CY2025): 8.7 and 7.0 points below the claims | [I] Medium (TH-204, TH-181) |
| FY2026 Q2 (Jul-Sep 2026; Teradyne Q3 2026), Advantest vs Teradyne only | SoC 76.4% of the two-vendor total; memory 52.4% | [I] Low (TH-182, TH-183) |

- The two-vendor ratios exclude other vendors, Teradyne's segment revenue may include service, and Teradyne's quarter ended 27 Sep 2026, so they are not market shares [I] Low (TH-182, TH-183) (caveats in calc/TH_share_check.out.txt).
- The memory gap recurs in both years, which points to a definitional difference (e.g. handlers or interfaces counted, or a shipments basis) rather than FX or timing; no saved document states the definition [I] Medium (TH-181). NOT DISCLOSED (read: FY25 Financial Briefing slides p.18 "Source: Advantest"; FY2025 briefing notes p.13; Q2 FY2026 Q&A A2) - method behind the tester TAM and share estimates.
- TAM revisions (company estimates, USD bn): CY2024 SoC first 3.3-3.6 (Jan 2024), cut to 2.9-3.2 (Apr 2024), final 4.1 [C] (TH-104, TH-106, TH-099), +34.4% on the lowered midpoint [I] High (TH-186); CY2025 SoC first 4.2-4.8 (Jan 2025), final 6.9 [C] (TH-107, TH-096), +53.3% [I] High (TH-184); CY2026e SoC first 8.5-9.5 (Jan 2026), about 11.5 (Oct 2026) [C] (TH-111, TH-102), +27.8% [I] High (TH-185). Total tester market 4.4 (CY2023), 6.0 (CY2024), 9.0 (CY2025) [C] (TH-179) and 13.0-14.5 (CY2026e) [C] (TH-101); CY2023-26e CAGR 43.5-48.8%, a little below the ~50% management cites [I] High (TH-187). The CY2024-26 TAM now averages 58-67% [I] High (TH-188) above the USD 5.9 bn assumed in MTP3 [C] (TH-121).

### 9.4 HBM, die-level and roadmap claims (all company claims)

| Stated | Claim | Tag and ids |
|---|---|---|
| 26 Apr 2024 | Worked with HBM customers for more than 10 years; stricter HBM quality requirements drive rigorous testing | [C] (TH-048, TH-049) |
| 25 Jun 2024 | Memory testers carry lower average margins than the company mix | [C] (TH-052) |
| 30 Oct 2024 | HBM tester sales "not slowing"; profit gains from upgrades slower than planned | [C] (TH-054, TH-055) |
| 29 Jan 2025 | No significant die-level test revenue expected in CY2025 | [C] (TH-067) |
| 12 Feb 2025 | T5801 DRAM tester (36 Gbps PAM3), global release early 2026 | [C] (TH-082) |
| 29 Jul 2025 | HBM4/HBM4E and higher stacks are a key memory-tester growth driver; wafer sort to grow faster than final test | [C] (TH-057, TH-068) |
| 17 Nov 2025 | Die-level probe for KGD and known-good chip-on-wafer to ramp later in CY2026, then several years of high growth; SoC capacity of at least 5,000 systems by end FY2026 (Mar 2027), then 7,500, then 10,000 | [C] (TH-070, TH-091) |
| 10 Dec 2025 | M5241 AI-memory handler: first shipments Q2 CY2026 (Apr-Jun 2026) | [C] (TH-083) |
| 16 Dec 2025 | Joint development of an HPC die-level prober with Tokyo Seimitsu announced | [F] (TH-072) |
| 22 Apr 2026 | Pin Scale 5000B "now ramping with key customers" | [C] (TH-085) |
| 29 Jul 2026 | Memory share "may experience a decline" in CY2026; NAND not a traditional stronghold; new products with customer commitments coming | [C] (TH-061, TH-062, TH-063) |
| 28 Oct 2026 | More than 5,000 systems a year reached; 10,000 (originally end FY2028, Mar 2029) pulled in, no date; 20,000 under discussion; CPO tester market to reach about USD 1 bn | [C] (TH-093, TH-094, TH-090) |
| 17 Nov 2026 | V93000 EXA Scale QX (36 slots) available in FY2027 Q1 (Apr-Jun 2027) | [C] (TH-086) |

- FY2026 Q2 (Jul-Sep 2026) system-level test sales rose mainly on consumer electronics, not AI [F] (TH-081). FY2025 Q2 (Jul-Sep 2025) memory test sales JPY 43.9 bn, with high-performance DRAM including HBM up [F] (TH-058).

### 9.5 Competitor and customer-side evidence

| Source | What it states | Tag and ids |
|---|---|---|
| Teradyne Q3 2026 (quarter ended 27 Sep 2026) | Semi Test revenue: SoC USD 676 m, memory USD 301 m; memory a record [F] (TH-166, TH-167); Teradyne attributes it to HBM/DRAM and NAND [C] (TH-206) | as shown |
| Teradyne, 28 Oct 2026 | Dual-vendor programme: first hyperscaler in the mature phase, next ramp mid-2027; merchant GPU customer a fast follower with revenue in 2027; second hyperscaler capacity buys in 2H 2027; mature-vendor share range 30-70% (a lifecycle range with no period attached) | [C] (TH-170, TH-171, TH-172, TH-173) |
| Teradyne, 28 Oct 2026 | Higher share in HBM performance test; lower stack heights raise that TAM; "no current ATE solution" for the most complex 2027 AI devices | [C] (TH-168, TH-174) |
| Teradyne, 28 Oct 2026 | Test share of semiconductor capex 6.4% (CY2025, Jan-Dec 2025) to 8.1% (Jan-Aug 2026); ATE TAM about USD 9.0 bn in CY2025 (Jan-Dec 2025), USD 12-14 bn in its target model; NOT DISCLOSED (read: Teradyne Q3 2026 Earnings Call Prepared Remarks; Teradyne Q3 2026 Earnings Presentation p.18; Teradyne Q3 2026 results press release) - Teradyne compute revenue in USD, its HBM performance-test share, and the target year of its Target Earnings Model | [C] (TH-169, TH-175) |
| Teradyne | CY2025 (Jan-Dec 2025; Teradyne fiscal year = calendar year) compute revenue USD 753 m (USD 109 m in CY2023, Jan-Dec 2023) | [F] (TH-176) |
| SK hynix with FormFactor, SWTest 2021 (conference presentation, not peer-reviewed) | KGD/KGS test cuts advanced-packaging cost; three HBM test-insertion choices; KGS HBM2 probe cards built for Advantest T5503 HS2 testers | [F] (TH-160, TH-162, TH-161) |
| SK hynix, Hot Chips 28 tutorial (2016) | HBM carries IEEE1500 test/repair features; flow includes hot/cold test, repair and a KGSD speed test | [F] (TH-163) |
| TSMC award reported by Advantest (24 Dec 2025) | Recognised for flexibility in expanding production capacity | [F] (TH-164) |
| Micron, 30 Sep 2026 | Agreements done for most of its CY2027 HBM bit supply; nothing on test | [C] (TH-165) |

Teradyne reports dual-vendor wins with 2027 ramps while Advantest claims a path to SoC share above 70%; the saved documents cannot settle which prevails [I] Medium (TH-198).

### 9.6 Technical papers

None of the six arXiv papers saved prints a journal or conference venue, so all are [S].

| Paper | What it states | Tag and ids |
|---|---|---|
| Mitra et al., Google (arXiv 2508.01786, Aug 2025) | Data-centre compute chips escape manufacturing test at about 5,000 DPM vs 100-500 DPM expected; more than several minutes of per-chip test time is "often regarded as impractical"; proposes in-field test | [S] (TH-150, TH-151, TH-152, TH-153) |
| CATCH (arXiv 2503.15753) | 16-chiplet 2.5D case: low die-level fault coverage gives very high scrap cost; optimum at 95% coverage (immature node) | [S] (TH-154) |
| YAP+ (arXiv 2511.05506, under review) | Hybrid-bonded dies may carry hundreds of thousands to several million pads, 10,000 to 1 million connections per mm2 | [S] (TH-155, TH-156) |
| DT-MATCH (arXiv 2611.19544) | Chiplet packages make test and repair "a first-order concern" | [S] (TH-157) |
| FA industry survey (arXiv 2606.22149) | 54% of respondents rate hybrid bonding the hardest new architecture for failure analysis | [S] (TH-158) |
| Sadi and Guin (arXiv 2006.04798) | With 5% faulty processing elements, AI-accelerator accuracy degrades by less than 1%, so binning can cut scrap | [S] (TH-159) |

The open literature points to rising test pressure per chip, but also to a ceiling on ATE time per chip and to routes that move test out of ATE (in-field test, fault-tolerant binning); this rests on secondary-grade evidence [I] Medium (TH-196). NOT RETRIEVED (tried: Firecrawl paper search and WebSearch; IEEE Xplore is paywalled) - peer-reviewed ITC / VTS / ECTC papers on HBM known-good-stack test, pre-bond test of 3D stacks and hybrid-bond interconnect test.

---

## 10. Close: B1 ledger, B2 facts, B3 catalysts, B4 gaps, B5 handoff

### 10.1 B1 Disputed-claims ledger

No claims were supplied by the user; the candidates came from module CL. The ledger keeps CL's C1, C2, C6, C7 and C3 and replaces C4 (China) with the memory-share claim from module TH, because the company's own sales and market-size figures imply a share well below the claim [I] Medium (TH-181, TH-204). Dropped candidates and reasons are in `parts/B1.md`.

| Claim | Who said it, when | Evidence for | Evidence against | Strongest tag on each side |
|---|---|---|---|---|
| **B1-1 Demand durability.** Tester TAM has grown "about 50% or slightly above" a year, management sees no slowing, and the industry stays supply-constrained in CY2027 | Advantest management, 28 Oct 2026 [C] (CL-001, CL-002, CL-005); Teradyne CEO, 28 Oct 2026 [C] (CL-018, CL-020) | FY2026 Q2 (Jul-Sep 2026) sales JPY 477.7 bn, +81.7% YoY [F] (CL-024, A1-067); quarterly sales 262.9 (FY2025 Q2, Jul-Sep 2025) to 273.8, 328.1, 367.5 bn (to FY2026 Q1, Apr-Jun 2026) [F] (CL-030); CY2026 TAM estimate raised from SoC 8.5-9.5 + memory 2.2-2.7 USD bn (28 Jan 2026) [C] (CL-138) to 13.0-14.5 total, first stated 29 Jul 2026 [C] (TH-114) and kept 28 Oct 2026 [C] (CL-007, TH-101), +2.3 bn at both ends [I] High (CL-129); customers plan on 18-month forecasts [C] (CL-014); Teradyne: test share of capex 6.4% (CY2025, Jan-Dec 2025) to 8.1% (Jan-Aug 2026) [C] (CL-018) | Management credited FY2025 Q1 (Apr-Jun 2025) scale effects to "demand pull-ins" [C] (CL-009) and said pull-in was why the expected 2H FY2025 (Oct 2025-Mar 2026) digestion "did not occur" [C] (CL-011, CL-131); Teradyne total revenue (all segments) USD 1,306 m in Q3 2026 (quarter ended 27 Sep 2026) vs 1,329 m in Q2 2026 (Apr-Jun 2026) [F] (CL-137), Semiconductor Test revenue USD 1,072 m vs 1,122 m [F] (CL-145), Q4 2026 (Oct-Dec 2026) guide USD 1,250-1,350 m [C] (CL-136), midpoint -0.5% vs Q3 [I] High (CL-139), with 2H compute "program timing" [C] (CL-019); capex is "highly fluid" [F] (CL-012); analysts saw FY2026 Q2 SoC sales diverge from trade statistics [S] (CL-016), and Advantest declined to comment [F] (CL-017); orders and backlog not disclosed since FY2021 Q4 (Jan-Mar 2022) [F] (A2-001, A2-008); the company's own tester TAM grew +36.4% (CY2024) and +50.0% (CY2025), and its CY2023-26e CAGR of 43.5-48.8% is below "about 50% or slightly above" [I] High (TH-187), inputs [C] (TH-179, TH-101) | For: [F] for current demand; [C] for durability. Against: [C] (management's own pull-in attribution); the [F] items concern Teradyne or generic risk text. Without order data neither side can be tested beyond reported sales |
| **B1-2 SoC share.** SoC tester share rises from 56% (CY2024) to 66% (CY2025), with a "path to above 70%" and a majority of AI-accelerator test | Advantest management, 27 Apr 2026 [C] (CL-041); 28 Oct 2026 [C] (CL-039, CL-040) | Share 56% / 66%, "Source: Advantest" [C] (CL-039, TH-119); majority of AI-accelerator test (CY2025) [C] (CL-041); own SoC sales over own SoC TAM 56.6% (CY2024) and 66.0% (CY2025) [I] Medium (TH-204, TH-180); FY2026 Q2 (Jul-Sep 2026) SoC sales 3.25x Teradyne's Q3 2026 SoC revenue (other vendors excluded; Teradyne segment revenue may include service) [I] Low (TH-182); SoC sales JPY 353.3 bn in FY2026 Q2 (Jul-Sep 2026) vs 173.7 bn in FY2025 Q2 (Jul-Sep 2025) [F] (CL-027, CL-029) | Teradyne expects share gains from dual-vendor strategies [C] (CL-044): next ramp at its first hyperscaler mid-2027 [C] (CL-045), merchant GPU customer revenue in 2027 [C] (CL-046), second hyperscaler capacity buys in 2H 2027 [C] (CL-047), mature-vendor share 30-70% [C] (CL-048); Advantest: customers "may consider dual-vendor strategies" [C] (CL-043); Chinese SoC testers growing in low-end China [C] (TH-043) | For: [C]; the [I] check shows only that the company's own figures agree with each other, and the share method falls under the NOT DISCLOSED line in section 9.3. Against: [C]; Teradyne's dated 2027 milestones are the first test points |
| **B1-3 Margins.** Operating margin can be held around 50% or more despite DRAM costs: "low 50% range" in 2H FY2026 (Oct 2026-Mar 2027), 51.9% for FY2026 (Apr 2026-Mar 2027) | Advantest management, 28 Oct 2026 [C] (CL-075, CL-034) | FY2026 Q2 (Jul-Sep 2026) OPM 55.9% [F] (CL-025), GM 71.1% [F] (CL-026); 1H FY2026 (Apr-Sep 2026) OPM 54.0% [I] High (A1-516); 2H forecast raised about 3 points from 47.3% assumed in July 2026 [C] (CL-035); pricing, licensing and new instruments to offset costs [C] (CL-075) | Inventory write-down reversal lifted FY2026 Q1 (Apr-Jun 2026) [C] (A1-315) and 1H (Apr-Sep 2026) margins [C] (CL-073), amount: NOT DISCLOSED line in section 3.2; DRAM and component costs "a major reason" the 2H margin falls [C] (CL-074); FY2025 Q4 (Jan-Mar 2026) "optimal mix" may not recur [C] (CL-076); implied 2H OPM 50.1% vs 54.0% in 1H [I] High (CL-117); last downturn: OPM 26.2% (FY2022 Q4, Jan-Mar 2023) to 14.1% (FY2023 Q1, Apr-Jun 2023) [F] (A6-170, A6-171, A6-328) | For: [F] for the current quarter only (which may contain part of the reversal); [C] for 2H. Against: [C]; the company names both the one-off and the cost headwind |
| **B1-4 Supply-bound.** Supply capacity, not demand, is the binding constraint; demand "continues to exceed supply" into CY2027 | Advantest, 28 Oct 2026 [C] (CL-005) and 12 Nov 2026 [C] (CL-015); Wing VC, 18 Nov 2026 [S] (CL-092) | Capacity above 5,000 systems a year; 10,000 "well ahead of" end FY2028 (Mar 2029) [C] (CL-081, CL-082); 20,000 "under active internal discussion" [C] (CL-143); advance receipts +JPY 44,215 m in 1H FY2026 (Apr-Sep 2026) vs 9,571 m in 1H FY2025 (Apr-Sep 2025) [F] (A2-141, A2-137); Teradyne: compute demand "far greater than supply" [C] (CL-020) | Inventories JPY 231,718 m (31 Mar 2026, FY2025 end) to 352,426 m (30 Sep 2026, FY2026 Q2 end) [F] (CL-088), +52.1% [I] High (CL-120); risk factor on "excess inventory or obsolescence" [F] (CL-089); Teradyne total revenue (all segments) USD 1,306 m in Q3 2026 (quarter ended 27 Sep 2026) vs 1,329 m in Q2 2026 (Apr-Jun 2026) [F] (CL-137), Semiconductor Test revenue USD 1,072 m vs 1,122 m [F] (CL-145), and a flat Q4 2026 (Oct-Dec 2026) guide [I] High (CL-139) | For: [F] only for the advance-receipt inflow, which shows customers paying earlier but not why; [C] for the constraint. Against: [F] for the inventory level, which management calls deliberate stocking [C] (CL-087, CL-140) |
| **B1-5 HBM lifts memory testers.** Rising HBM/DRAM test intensity will lift Advantest's memory tester sales | Advantest, 29 Jul 2025 [C] (TH-057) and 28 Oct 2026 [C] (CL-053); TrendForce, 5 Oct 2026 [S] (CL-057) | Memory sales to "grow further" in FY2026 (Apr 2026-Mar 2027) [C] (CL-053); memory TAM USD 2.1 bn (CY2025) to 2.5-3.0 bn (CY2026e) [C] (CL-007); memory sales JPY 53.4 bn in FY2026 Q2 (Jul-Sep 2026) vs 43.9 bn in FY2025 Q2 (Jul-Sep 2025) [F] (CL-028, CL-029), +21.6% [I] High (CL-114); test equipment may outgrow HBM output [S] (CL-057) | FY2026 Q2 (Jul-Sep 2026) memory sales of JPY 53.4 bn below the 57.3 bn of FY2025 Q3 (Oct-Dec 2025) [F] (CL-028, A1-262); memory fell from 20.2% to 13.1% of SoC-plus-memory sales between FY2025 Q2 (Jul-Sep 2025) and FY2026 Q2 (Jul-Sep 2026) [I] High (CL-114); Teradyne record memory revenue USD 301 m in Q3 2026 (quarter ended 27 Sep 2026) [F] (CL-055); Teradyne claims the higher HBM performance-test share [C] (CL-054); Advantest memory share "may experience a decline" in CY2026 [C] (CL-052); SK hynix HBM4 wafer-tester orders went to Digital Frontier and UniTest [S] (CL-056) | For: [C]; the [F] YoY rise is measured against FY2025 Q2 (Jul-Sep 2025), not the FY2025 Q3 (Oct-Dec 2025) high. Against: [F], reported sales of both companies for the same months |
| **B1-6 Memory share.** Advantest holds about 60% of the memory tester market: 63% (CY2024), 61% (CY2025) | Advantest, 25 Apr 2025 and 27 Apr 2026 [C] (TH-119, TH-064, CL-051) | Share 56% / 63% / 61% (CY2023-CY2025), "Source: Advantest" [C] (TH-119); "remained at around 60%" [C] (TH-064); "market dominance, particularly in DRAM" [C] (TH-057) | Own memory sales over own memory TAM 54.3% (CY2024) and 54.0% (CY2025), 8.7 and 7.0 points below the claims [I] Medium (TH-204, TH-181), on reported sales [F] (TH-201) and the company's TAM [C] (TH-100, TH-097); FY2026 Q2 (Jul-Sep 2026) memory sales 1.10x Teradyne's Q3 2026 memory revenue (other vendors and service content not adjusted) [I] Low (TH-183); share method: NOT DISCLOSED line in section 9.3 | For: [C], method: NOT DISCLOSED line in section 9.3. Against: [I] Medium on [F] sales and [C] TAM; the gap recurs in both years, pointing to a definitional difference no document states |

Margins in this ledger with and without the one-offs management named are in section 3.2 (FY2026 Q1-Q2 and 1H, Apr-Sep 2026: not computable - NOT DISCLOSED line in section 3.2) and section 8.2 (FY2022 Q4, Jan-Mar 2023: 26.2% reported [F] (A6-170), 28.2% without the ~JPY 3 bn inventory losses [I] Medium (A6-280)).

### 10.2 B2 Facts that most weaken each reading

Reading tested: "AI-accelerator and HBM test demand drives durable growth and margins at Advantest."

**Facts that most weaken the optimistic reading**
1. Concentration. In FY2025 (Apr 2025-Mar 2026) NVIDIA International, Inc. alone took JPY 228,273 m, 20.2% of net sales [F] (CL-069), and the top five customers about 50% (about 48% in FY2024, Apr 2024-Mar 2025) [F] (CL-070); NVIDIA Group JPY 243,735 m [F] (CL-068). Teradyne names a merchant GPU customer as a "fast follower" with revenue in 2027 [C] (CL-046).
2. HBM leg. Memory test sales were JPY 53.4 bn in FY2026 Q2 (Jul-Sep 2026), below the 57.3 bn of FY2025 Q3 (Oct-Dec 2025) [F] (CL-028, A1-262), while Teradyne posted record memory revenue of USD 301 m in its Q3 2026 (quarter ended 27 Sep 2026) [F] (CL-055); Teradyne attributes it to HBM and DRAM test demand and a NAND resurgence [C] (TH-206), and Advantest says its memory share may decline in CY2026 [C] (CL-052).
3. Cycle. In the last downturn quarterly sales fell 31.3% QoQ, JPY 147.4 bn in FY2022 Q4 (Jan-Mar 2023) to 101.3 bn in FY2023 Q1 (Apr-Jun 2023) [F] (A6-326), and operating margin fell from 26.2% to 14.1% [F] (A6-328, A6-170, A6-171), with about JPY 3 bn of inventory valuation losses named in the peak quarter [F] (A6-219); the margin without them is in section 8.2. Inventories now stand at JPY 352,426 m at 30 Sep 2026 (FY2026 Q2 end) [F] (CL-088).

**Facts that most weaken the pessimistic reading**
1. The expected digestion did not come. As of October 2025 the company expected a 2H FY2025 (Oct 2025-Mar 2026) correction [C] (CL-131); single-quarter sales then rose four quarters in a row, from JPY 262.9 bn (FY2025 Q2, Jul-Sep 2025) to 273.8, 328.1, 367.5 bn [F] (CL-030) and 477.7 bn in FY2026 Q2 (Jul-Sep 2026) [F] (CL-024).
2. SoC scale and margin. SoC test sales JPY 353.3 bn in FY2026 Q2 (Jul-Sep 2026) vs 173.7 bn in FY2025 Q2 (Jul-Sep 2025) [F] (CL-027, CL-029); gross margin 71.1% [F] (CL-026) and operating margin 55.9% [F] (CL-025), far above the 26.2% of the last cycle's peak-sales quarter, FY2022 Q4 (Jan-Mar 2023) [F] (A6-170), a quarter with about JPY 3 bn of inventory valuation losses named [F] (A6-219); the margin without them is in section 8.2. The reversal named for FY2026 Q1 (Apr-Jun 2026) and 1H (Apr-Sep 2026) [C] (A1-315, CL-073) has no amount; the NOT DISCLOSED line in section 3.2 also covers whether any part fell in FY2026 Q2 (Jul-Sep 2026).
3. Customers paying ahead. Advance receipts rose JPY 44,215 m in 1H FY2026 (Apr-Sep 2026) [F] (A2-141), against 9,571 m in 1H FY2025 (Apr-Sep 2025) [F] (A2-137) and 9,748 m in all of FY2025 (Apr 2025-Mar 2026) [F] (A2-139). This does not show how far ahead orders run, because orders are not disclosed [F] (A2-001).

### 10.3 B3 Dated catalysts, 22 Nov 2026 - 21 Nov 2027

| Date | Event | Tag and ids |
|---|---|---|
| 30 Nov 2026 | Teradyne presents at the UBS Global Technology and AI Conference | [F] (CL-108) |
| 1 Dec 2026 | Interim dividend payment, JPY 49.00 per share (record date 30 Sep 2026) | [F] (CL-093) |
| Each calendar quarter-end (31 Dec 2026, 31 Mar, 30 Jun, 30 Sep 2027) | CB conversion test: holders may convert only if the share price exceeded 150% of the conversion price over the last 20 trading days of the prior calendar quarter (no price level computed here) | [F] (A5-068) |
| 10 Jan 2027 | End of the BIS stay of the Affiliates rule (90 FR 47201), unless extended again | [F] (CL-104) |
| 19 Jan 2027 | Comment deadline for the BIS remote-access interim final rule (effective 19 Nov 2026) | [F] (CL-105) |
| January 2027 [F] (CL-094) | Q3 FY2026 (Oct-Dec 2026) results; first quantitative CY2027 tester-market outlook promised [C] (CL-003); possibly more detail on the 10,000-system date [C] (CL-143); first test of the expected QoQ rise in SoC test sales in FY2026 Q3 (Oct-Dec 2026) [C] (A2-166). NOT DISCLOSED (read: IR web page IR Calendar, FY2026 Yearly Calendar, 2026-11-21; IR news index 2026, 2026-11-21) - day of the Q3 FY2026 (Oct-Dec 2026) results announcement (only "Jan" 2027 is given) | as shown |
| 17 Feb 2027 | Licence deadline for existing data-centre compute providers under the remote-access rule (90 days after 19 Nov 2026) | [I] Medium (CL-123) |
| NOT DISCLOSED (read: Teradyne Q3 2026 Earnings Call Prepared Remarks, closing remarks; Teradyne IR home page 2026-11-21, Upcoming Event) - date of Teradyne's Q4 2026 earnings call (where the updated target model will be shared) | Teradyne Q4 2026 (Oct-Dec 2026) call with an updated target earnings model [C] (CL-080); Q4 guide USD 1,250-1,350 m [C] (CL-136) | as shown |
| 24 Mar 2027 | End of the JPY 280 bn / 11 million-share buyback window [F] (CL-099); JPY 265,436,674,000 of headroom after 31 Oct 2026, a cap not a commitment [I] High (CL-124) | as shown |
| 31 Mar 2027 | FY2026 (Apr 2026-Mar 2027) and MTP3 end [F] (CL-101); MTP3 revised targets and the 50% cumulative return target are tested [C] (CL-077, A5-091); cash-on-hand concept JPY 100-120 bn [C] (A5-190); about JPY 20 bn of CB proceeds planned for inventory by this date [C] (A5-073); record date for the year-end dividend [F] (CL-133). NOT DISCLOSED (read: interim dividend notice E_Info_20261028_03 p.1, dividend table; FY2026 Q2 Consolidated Financial Results p.1, 2. Dividends; IR web page IR Calendar 2026-11-21, FY2026 Yearly Calendar) - FY2026 year-end dividend per share | as shown |
| NOT DISCLOSED (read: IR web page IR Calendar 2026-11-21, FY2025 and FY2026 Yearly Calendars; IR news index 2026, 2026-11-21) - date of the FY2026 full-year results announcement | FY2026 full-year results and FY2027 (Apr 2027-Mar 2028) guidance; the current FY2026 (Apr 2026-Mar 2027) guidance (sales JPY 1,863.0 bn, OI 967.0 bn, NI 741.5 bn) is tested [C] (A3-104, A3-105, A3-107), as are the 2H FY2026 (Oct 2026-Mar 2027) sales forecast of JPY 1,017.8 bn [C] (A2-027) and the expected further QoQ rise in SoC test sales in FY2026 Q4 (Jan-Mar 2027) [C] (A2-166) | as shown |
| 15 May 2027 | Record date for voting rights at the 85th AGM | [F] (CL-133, CL-134, CL-097) |
| Around May 2027 [C] (CL-102) | Fourth Mid-Term Management Plan, possibly with an outlook to CY2028-CY2029 [C] (CL-102); a doubling of SoC capacity to 20,000 a year is under internal discussion [C] (CL-143). NOT DISCLOSED (read: Q2 FY2026 Financial Briefing Q&A Summary, A7 and A11) - exact release date of the Fourth Mid-Term Management Plan (only "around May 2027") | as shown |
| NOT DISCLOSED (read: IR web page IR Calendar 2026-11-21; 84th annual securities report, p.199) - date of the 85th Ordinary General Meeting | 85th AGM, within the statutory window 15 May-15 Aug 2027 [I] Medium (CL-126); the 84th was held 31 Jul 2026 [F] (CL-096) | as shown |
| FY2027 Q1 (Apr-Jun 2027) | V93000 EXA Scale QX test head "expected to be available" | [C] (TH-086) |
| Mid-2027 | Teradyne: next major ramp at its first hyperscaler | [C] (CL-045) |
| 30 Sep 2027 | Record date for the FY2027 (Apr 2027-Mar 2028) interim dividend (standing rule) | [F] (CL-133) |
| None in window | Debt maturities: none; the only bond is the JPY 100 bn CB due 28 Mar 2031 | [I] High (CL-125); [F] (CL-103) |
| Lock-ups | NOT RETRIEVED (tried: https://www.advantest.com/document/en/investors/aad/E_Info_20260401_02.pdf, _03.pdf, _04.pdf - HTTP 403 to scripted request, not retried; full-text search of the saved 84th annual securities report and 85th semi-annual securities report found no lock-up wording) - lock-up terms of the April 2026 Zero Coupon CB offering | gap line, no evidence row |

Not in the table, because no date in the window is published:
- 10,000 SoC systems a year: original target end FY2028 (Mar 2029), now aimed about a year earlier; schedule not final; 20,000 needs "some additional time" [C] (CL-082, CL-083, CL-084). NOT DISCLOSED (read: Q2 FY2026 Financial Briefing Q&A A7; Q1 FY2026 Financial Briefing Q&A A6; IR Fireside Chat Q&A 2026-11-12 A5) - committed date for 10,000 SoC tester systems a year and the scale and timing of the next step (only "roughly a year in advance" of end FY2028, Mar 2029; the company says the schedule is not final).
- New memory tester products with customer commitments, aimed at recovering share [C] (CL-052).
- Teradyne: merchant GPU customer revenue in CY2027, no month given [C] (CL-046); capacity buys at a second hyperscaler in 2H 2027 (Jul-Dec 2027), partly after 21 Nov 2027 [C] (CL-047).
- Section 232 phase 2: broader semiconductor tariffs after trade negotiations; no tariff rate on semiconductor equipment set; a 25% duty on a narrow chip category since 15 Jan 2026 [F] (CL-107). NOT RETRIEVED (tried: web search Nov 2026 for any Section 232 proclamation after Proclamation 11002 of 14 Jan 2026 that sets tariffs on semiconductor manufacturing equipment or starts phase 2; none found; federalregister.gov not queried by script) - any dated Section 232 tariff on semiconductor manufacturing equipment or phase-2 semiconductor tariff (catalyst B3).

NOT DISCLOSED (read: IR web page IR Calendar 2026-11-21, FY2025 and FY2026 Yearly Calendars; IR news index 2026, 2026-11-21; IR web page Share Information; 84th annual securities report, p.199 Stock-related administration) - dates of the FY2026 (Apr 2026-Mar 2027) full-year results, the Q1 and Q2 FY2027 (Apr-Jun 2027 and Jul-Sep 2027) results, the 85th Ordinary General Meeting and the FY2026 year-end dividend payment (no FY2027 (Apr 2027-Mar 2028) calendar published; only the 15 May record date and 'within three months' are given).

### 10.4 B4 Gap log

`gaps.md` holds 183 gap lines: 152 NOT DISCLOSED and 31 NOT RETRIEVED, by module A1 22, A2 44, A3 13, A4 21, A5 24, A6 14, TH 25, CL/B 19 and Sources 1, plus 20 items listed under "Files the user can save by hand" [I] High (DS-004). The gaps that matter most for this dossier:
- AI / HBM / advanced-packaging share of revenue; recurring revenue (sections 3.6, 3.7, 9.1).
- Orders, backlog and book-to-bill for every quarter since FY2022 Q1 (Apr-Jun 2022) (section 4.1).
- Amounts of the FY2026 Q1/1H (Apr-Sep 2026) inventory write-down reversal and of the FY2025 Q4 (Jan-Mar 2026) one-off SG&A, and the tax effect of the named items, so no ex-one-off gross margin, operating margin or net income for those periods (section 3.2).
- Inventory split and contract-liability balance at 30 Sep 2026 (FY2026 Q2 end) (sections 4.2, 4.3).
- Method behind the TAM and market-share estimates (section 9.3).
- Name and manager of the investment fund(s) behind the JPY 184,365 m of fund-interest purchases in 1H FY2026 (Apr-Sep 2026) [F] (A1-160) (section 7.1).
- CB early-redemption terms and events of default (section 7.2).
- CB offering notices (early redemption, lock-up), METI originals, and anything on sec.gov (customers' filings, Teradyne 10-K, Advantest's FY2007 20-F): not retrieved; URLs and file names to save by hand are in `gaps.md`.

### 10.5 B5 Handoff

The handoff row is in `handoff.md` (schema per research/CLAUDE.md) and is reproduced field by field in section 2.

The independent-reviewer packet is `review_packet.md`: the 15 claims the conclusions use most, with public URLs and pages, the 5 inferences they lean on with their inputs, and 3 questions not settled; `calc/RP_check.py` checks its ids, tags, URLs, pages and values against `evidence.csv` and the source manifest (output in `calc/RP_check.out.txt`).

---

## 11. Method and limits

**Sources used.** The module parts merged in `evidence.csv` hold 2,410 rows: 1,487 [F], 438 [C], 30 [S] and 455 [I], plus this dossier's five DS rows. The source manifest lists 218 retrieved documents, 180 of them issued by Advantest, 27 NOT RETRIEVED and 6 superseded [I] High (DS-005). Counts of Advantest documents differ by scan time and by whether IR web pages are included: 164 at the TH keyword scan (180 files less 16 IR/news web pages) [I] High (TH-193), 179 at the A4 rule scan [I] High (A4-400), 180 in the final manifest [I] High (DS-005). Company documents: financial results (tanshin) and briefing slides, speaker notes and Q&A summaries for the quarters used; the 83rd and 84th Annual Securities Reports and the 84th and 85th Semi-Annual Securities Reports; the Integrated Annual Report 2026; MTP3 materials; the Investors' Guide (Oct 2026); IR fireside chats; IR web pages (forecast, calendar, share information, bonds, ratings, news indexes); revision, buyback, dividend and CB notices; older results releases back to FY2008 for the cycle module. The public TDnet daily disclosure lists for 28 Oct-21 Nov 2026 were read by script for Advantest items (121 requests, logged in `calc/A3_tdnet_fetch_log.tsv`; the pages roll off after a month and are not saved as sources) [I] High (A3-322). Third-party documents: Federal Register rules (BIS) and a White House proclamation; Teradyne and Micron releases and decks; SWTest and Hot Chips conference material; arXiv preprints; a few press items, all [S].

**What could not be retrieved** (details, URLs and file names to save by hand are in `gaps.md`):
- sec.gov: the session had no contact User-Agent to declare, so nothing on EDGAR was fetched (customer filings that might name Advantest, Teradyne's 10-K, Advantest's FY2007 20-F).
- advantest.com refused the three April 2026 CB offering notices (HTTP 403), so early-redemption and lock-up terms are missing; meti.go.jp, investors.formfactor.com and TSMC investor pages refuse scripts; the FY2007 results release and the FY2022 Q1 Q&A return HTTP 404; Bloomberg, In Practise and Seeking Alpha are paywalled; a PMC paper returned a reCAPTCHA page. None of these was worked around.
- prior/ held no exports [I] High (DS-002).

**Conventions.**
- Tags: guidance, forecasts, targets, FX assumptions, roadmap dates, market sizes and shares are company claims [C] even when printed in a filing; reported results are [F]; arXiv preprints and press are [S]; every calculation is [I] with a script under `calc/` and a confidence. Where a printed table row mixes actuals and forecasts, the actual cells are cited as [F] and forecast cells only through a [C] row.
- Periods: every figure carries its fiscal label and calendar months. Dated company statements are labelled in `evidence.csv` by the fiscal quarter containing the statement date, with "(stated D Mon YYYY)", e.g. a 28 Oct 2026 remark about 1H FY2026 sits in FY2026 Q3 (Oct-Dec 2026); statements about a forecast period carry that period; market sizes and shares are calendar years (CY). Teradyne reports calendar quarters (its Q3 2026 ended 27 Sep 2026). LTM = FY2025 + 1H FY2026 - 1H FY2025 = Oct 2025-Sep 2026.
- Numbers: quarterly slide figures are differences of rounded year-to-date figures and can differ by JPY 0.1 bn from tanshin million-level differences [I] High (A3-296); YoY rates are computed on JPY-million quarters. Values are quoted as printed or as computed by the cited script, without re-rounding.
- One-offs: only items management itself named are removed, and only when an amount is printed. Recurring inventory valuation losses are removed only where management named a quarterly amount, and both variants are shown (section 8.2). Valuation gains on strategic investments are not called one-off by the company and are removed only as a sensitivity.
- File names carry the printed document date. All statutory-report file names match the dates on the IR index (two semi-annual files were renamed from 12 Nov PDF-metadata dates to 13 Nov), and the Integrated Annual Report 2026 file carries 11 Nov 2026 (PDF metadata) although the news index lists it on 16 Oct 2026; both IAR dates fall in FY2026 Q3, so no period label changes [I] High (DS-003).

**Limits.**
- The theme share is a proxy built on a rounded company category that includes smartphone application processors; modules A1 and TH both rate it Low [I] Low (A1-469, TH-190).
- The guidance count depends on a slot method in which two of eight quarters are half-year tests and two are full-year tests [I] Medium (A3-292); the slots overlap, and only four are independent single-quarter tests [I] Medium (A3-318).
- Absence of later guidance revisions rests on the English IR news indexes and forecast page [F] (A3-232, A3-233, A3-254, A3-261, A3-109); TDnet lists for 28 Oct-21 Nov 2026 were read [I] High (A3-322); Japanese filings of Jan 2024-Mar 2025 are outside the public TDnet window (NOT RETRIEVED line in section 5.3).
- Regional quarterly data are chart labels read on rendered slides, which sum to the printed totals [I] High (A4-372); the 95% application split sits in an image table, read on the rendered page [F] (A1-300).
- The downturn selection depends on a threshold that 2018-19 clears by 0.17 pp [I] High (A6-350).
- The export-control reading rests on rule texts [I] Low (A4-402); Advantest's ECCNs and US-origin content fall under the NOT DISCLOSED line in section 6.4, and no BIS advisory opinion was retrieved (see the BIS FAQ entry in `gaps.md`).
- Cross-module consistency, quote checks and period-label rules are logged in `parts/XM_reconcile.md`; module verifier logs are `parts/<MOD>_verify.md`.
