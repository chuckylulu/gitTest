# Camtek Ltd. (CAMT): completeness critique, gap fill and cross-file consistency

**Scope:** A completeness and consistency review of every notes and ledger file in `research/camtek/notes/` (01–08, ledger_C1–C4) against the brief: Q1–Q6, Module A (with the four user additions) and Module B (four claims plus the micro-bump handoff cell). It lists what is missing, thin, unsourced, inconsistent between files or resting only on [CO] sources. It fills the most important gaps with new research. It corrects inconsistencies at primary source, and it records what remains unfillable. Fiscal year = calendar year. The latest reported quarter is **Q3 2026** (release and call on 4 Nov 2026, 6-K) [1]. Research date 21 Nov 2026. Data only: no recommendations, price targets or investment opinions.

**Conventions:** [CO] = company-controlled; [IND] = independent; [CO-relayed] = a third party repeating Camtek. QUANTIFIED / QUALITATIVE marks each company statement. DERIVED = my arithmetic, shown. ESTIMATE = method and inputs shown. INFERENCE = premises shown. Downloads are in `/tmp/claude-0/-home-user-gitTest/ddd608d2-d311-5bff-84be-e57c9e3b9881/scratchpad/camtek_dl/critic/`.

---

## Sources used (new in this file, or re-opened at primary source)

1. [CO] Camtek Q3 2026 results release, 4 Nov 2026 (re-downloaded and text-extracted, `critic/Q32026.txt`). https://cdn.camtek.com/wp-content/uploads/Q32026.pdf
2. [CO] Camtek Q2 2026 results release, 10 Aug 2026 (re-downloaded, `critic/Q22026.txt`). https://cdn.camtek.com/wp-content/uploads/Q22026.pdf
3. [CO] Camtek Q1 2026 results release, 12 May 2026 (re-downloaded, `critic/Q12026.txt`). https://cdn.camtek.com/wp-content/uploads/Q12026.pdf
4. [CO] Camtek Q1 2026 earnings call, 12 May 2026, StockAnalysis transcript (re-fetched 21 Nov 2026). https://stockanalysis.com/stocks/camt/transcripts/559247-q1-2026/
5. [CO] Camtek Q2 2024 earnings call, 1 Aug 2024, StockAnalysis transcript (fetched 21 Nov 2026). https://stockanalysis.com/stocks/camt/transcripts/192672-q2-2024/
6. [IND] SEC EDGAR, Camtek (CIK 1109138) filing index, retrieved 21 Nov 2026. https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001109138&type=&dateb=&owner=include&count=40 ; Schedule 13G list: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001109138&type=SCHEDULE+13G&dateb=&owner=include&count=40
7. [IND] Schedule 13G, Menora Mivtachim Holdings Ltd., event date 14 Oct 2026, signed 18 Oct 2026, filed 19 Oct 2026. https://www.sec.gov/Archives/edgar/data/1109138/000117891326004782/xslSCHEDULE_13G_X02/primary_doc.xml (filed by the holder, so [IND] with respect to Camtek)
8. [IND] Schedule 13G/A, Migdal Insurance & Financial Holdings Ltd. and Migdal Sal Domestic Equities, event date 30 Sep 2026, signed 19 Oct 2026. https://www.sec.gov/Archives/edgar/data/1109138/000117891326004788/xslSCHEDULE_13G_X02/primary_doc.xml
9. [IND] Schedule 13G/A, Migdal (same reporting persons), event date 15 Oct 2026, signed 20 Oct 2026. https://www.sec.gov/Archives/edgar/data/1109138/000117891326004806/xslSCHEDULE_13G_X02/primary_doc.xml
10. [IND] Schedule 13G/A, Migdal, event date 30 Jun 2026, signed 22 Jul 2026. https://www.sec.gov/Archives/edgar/data/1109138/000117891326003570/xslSCHEDULE_13G_X02/primary_doc.xml
11. [IND] Schedule 13G, Phoenix Financial Ltd., event date 6 Aug 2026, signed 11 Aug 2026. https://www.sec.gov/Archives/edgar/data/1109138/000117891326004038/xslSCHEDULE_13G_X02/primary_doc.xml
12. [IND] Schedule 13G/A, Wasatch Advisors LP, event date 30 Jun 2026, signed 9 Jul 2026. https://www.sec.gov/Archives/edgar/data/1109138/000081413326000073/xslSCHEDULE_13G_X02/primary_doc.xml
13. [IND] Schedule 13G/A, Harel Insurance Investments & Financial Services Ltd., event date 31 Mar 2026, signed 4 May 2026. https://www.sec.gov/Archives/edgar/data/1109138/000117891326002368/xslSCHEDULE_13G_X02/primary_doc.xml
14. [CO] Insider Forms 3 and 4 filed by Camtek officers and directors (the filers are company insiders, so [CO]), as tabulated by EDGAR's ownership display, retrieved 21 Nov 2026. https://www.sec.gov/cgi-bin/own-disp?action=getissuer&CIK=0001109138 ; Form 4 list: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001109138&type=4&dateb=&owner=include&count=40
15. [IND] FinancialContent, CAMT daily historical closing prices, 21 Aug – 20 Nov 2026, retrieved 21 Nov 2026. https://www.financialcontent.com/quote/NQ:CAMT/historical
16. [IND] StockAnalysis, CAMT price history, 14 Sep – 20 Nov 2026, retrieved 21 Nov 2026 (cross-check of [15]; identical closes on all overlapping days). https://stockanalysis.com/stocks/camt/history/
17. [IND] Federal Reserve Bank of St. Louis (FRED), series DEXTAUS (Taiwan dollars to one US dollar, noon buying rates, H.10), observations Jun–Jul 2026, retrieved 21 Nov 2026. https://fred.stlouisfed.org/data/DEXTAUS.txt
18. [IND, SECONDHAND] Investing.com, "Stifel raises Camtek stock price target to $120 on strong AI demand", 10 Nov 2025 (paraphrase of a Stifel note). https://ng.investing.com/news/analyst-ratings/stifel-raises-camtek-stock-price-target-to-120-on-strong-ai-demand-93CH-2199799
19. [CO] SEMICON Taiwan 2026 exhibitor news sheet by Camtek, "Camtek_news_semiconTW2026_V2.pdf", Aug 2026. Content seen through a search-engine summary only (the PDF returned HTTP 403 to file 01). https://semicontaiwan.org/sites/semicontaiwan.org/files/2026-08/Camtek_news_semiconTW2026_V2.pdf ; exhibitor page https://semicontaiwan.org/en/News/Camtek_Inspection_Technology_Limited
20. [IND] Hyundai Motor Securities (현대차증권), "반도체 장비: 타오르는 시장에 솟구치는 투자", 13 May 2026 (Naver-hosted PDF), checked for Camtek/Onto mentions: none found. https://stock.pstatic.net/stock-research/industry/38/20260527_industry_545981000.pdf
21. Cross-references to the files under review: `01_products.md`, `02_quarterly_revenue_mix_margin_china.md`, `03_module_a_financials_customers_converts.md`, `04_module_a_china_export_rules.md`, `05_hbm_inspection_steps.md`, `06_hybrid_bonding.md`, `07_competition_onto_kla_china.md`, `08_orders_backlog_capacity.md`, `ledger_C1.md` to `ledger_C4.md`. Where a source number below is written "file 07 [27]", it refers to that file's own source list.

---

## 1. Gap list against the brief

Status key: **OK** = covered with primary sources; **THIN** = covered but weak or partly unsourced; **CO-ONLY** = rests only on [CO] sources; **MISSING** = not covered; **FILLED** = closed or improved in §2 of this file; **INCONSISTENT** = files disagree (settled in §3).

### Q1 Product map (file 01)
| Item | Status | Note |
|---|---|---|
| Products, status, launch dates, what each measures | OK, CO-ONLY | All specs come from Camtek's website, releases, 20-F and deck. No independent technical evaluation exists (file 01, "Not found"). |
| Throughput | THIN, CO-ONLY | Only relative "2×" claims plus one Hawk IR figure (10 WPH at 1 µm). No WPH for Eagle G5 or Hawk 2D/3D. Not fillable from public sources. |
| Resolution | OK, CO-ONLY; internal contradictions (100 nm vs 150 nm Hawk; <10 vs <12 µm pitch) are logged in file 01. |
| NanoProf | THIN → partly FILLED (§2.9) | Measurement list found; numeric specs still not found. |
| Software / AI classification | OK, CO-ONLY | ADC, AiDC, EDC, 2D AI detection, Compass, Visual Layer. "pretty much 0" separately sold software until 2027 (file 01). |
| 2026 inspection vs metrology unit split | INCONSISTENT (file 01 says the slide numbers did not extract; files 02 and 06 give 60/25/15) | Settled in §3, item 9. |
| Error in file 01, Contradiction 11 (Q3 2026 highlights "GAAP operating income of $8 million") | INCONSISTENT | Wrong reading of the release. Settled in §3, item 3. |

### Q2 Revenue by application (file 02)
| Item | Status | Note |
|---|---|---|
| Definitions and label changes | OK, CO-ONLY | Five label regimes 2023–2026, with quotes. |
| 8-quarter trend | OK, CO-ONLY | Q4 2024–Q3 2026 covered, plus 2023–Q3 2024. All approximate verbal percentages; Q4 2024 and Q4 2025 given only as full-year figures; Q3 2026 AI share is DERIVED (~65%, low precision). |
| HBM vs CoWoS-type split | MISSING by disclosure | Only Q1 2024 (HBM 40%, chiplets 20%) and H2 2023 (~20% HBM). Camtek states it does not split. Unfillable. |
| CIS, compound, front-end separately | MISSING by disclosure | Only occasional verbal ranges (2023–2024). Unfillable. |
| Independent check on the application split | MISSING | No independent dataset. Unfillable. |

### Q3 Inspection steps per HBM generation (files 05, ledger_C1)
| Item | Status | Note |
|---|---|---|
| Camtek statements, quantified vs not | OK, CO-ONLY | No step count was ever given; the only "tens of steps" (Feb 2024) is not tied to HBM. |
| Q2 2024 call | MISSING in file 05 ("Not retrieved") → FILLED (§2.7) | |
| Independent per-generation step count | MISSING | None from memory makers, competitors, analysts or papers. Unfillable on public sources. |

### Q4 Hybrid bonding (files 06, ledger_C2)
| Item | Status | Note |
|---|---|---|
| Tools by step, roadmap, post-bond voids | OK, CO-ONLY | No post-bond void product (roadmap 2027–28). |
| Systems shipped, revenue, customers | MISSING by disclosure | "several sites", "a few machines", "low magnitude". Unfillable. |
| Independent naming of Camtek as an HB supplier | MISSING | None found (file 06). Not found again here. |
| Reverse question / handoff cell | OK as ESTIMATE | M1 34.5% / 48.5% / 57.3% and M2 5.4% / 10.0% / 25.8% (LTM to Q3 2026). Consistent between file 06 and ledger_C2. Inputs rest on [CO] percentages and on assumptions; see §4. |

### Q5 Head-to-head (files 07, ledger_C3)
| Item | Status | Note |
|---|---|---|
| SK hynix, Samsung, Micron | THIN | Firsthand: Onto releases (interested party) and the SK hynix award; Korean disclosures on Nextin/Pemtron. Nothing customer-issued naming Camtek. Samsung and Micron rest on unsourced newsletters. |
| TSMC | THIN | Onto/KLA statements; Ta Liang press claim; no TSMC document naming Camtek. |
| Large OSATs | OK for ASE/SPIL (MOPS filing naming Camtek) → USD conversion FILLED (§2.4); MISSING for Amkor, JCET, Tongfu, Powertech. |
| Chinese vendors | OK (Skyverse, CETC Fenghua, Changchuan, from Chinese press/brokers; secondhand). |
| Korea revenue drop 2025 unexplained | THIN → partly FILLED (§2.6) with a secondhand analyst attribution. |
| "Announcement yesterday" (13 Oct 2026) by a larger 2D entrant | MISSING; searched again, not found. |

### Q6 Orders (files 08, ledger_C4)
| Item | Status | Note |
|---|---|---|
| Definitions, periods, delivery buckets | OK, CO-ONLY | No backlog $ figure, no RPO, no definition. |
| Cancellation terms | MISSING by disclosure | Only risk-factor language; no fees or deposit terms. Unfillable. |
| Capacity expansion | OK, CO-ONLY | Stated "capacity" in $ moved $500M → $600–660M → $500M → $700M → $1.2B; Israeli manufacturing floor doubled (20-F). German expansion not visible. |
| Independent corroboration of any 2026 order | MISSING in files 08/ledger_C4 ("No independent source … sizes or names any Camtek order") → partly FILLED (§2.4): the SPIL MOPS filing size matches the $55M tier-1 OSAT order. |

### Module A (files 02, 03, 04)
| Item | Status | Note |
|---|---|---|
| Financials FY2021–9M 2026, cash flow, cash, debt | OK (audited 20-F + releases) | |
| China share by quarter since 2023 | MISSING by disclosure | Only annual (20-F) and verbal FY estimates. Quarterly Asia vs RoW only. Q1 2026 Asia split was "Not found" → confirmed not given (§2.8). Independent proxy (China customs HS 9031.41 imports from Israel) searched, not obtained (§5). |
| Export rules for an Israeli supplier, company statements | OK (file 04, primary regulatory text) | Camtek's ECCNs, US content, licences: not disclosed. |
| Customers >10%, top-three share | OK for >10%; top-three MISSING by disclosure → DERIVED bounds FILLED (§2.5). |
| Convertible notes: series, maturity, conversion price, nearest-maturity settlement | OK; Q1 2026 settlement method INFERRED (shares). Residual $63k maturing 1 Dec 2026: no notice. 2030 Notes 130% conversion test "Not verified" → FILLED for Q3 2026 (§2.2). |
| Gross margin by quarter with mix effects | OK, CO-ONLY | Releases agree with file 02 (re-checked Q2 and Q3 2026). One inconsistency on the tax item (§3, item 1). |
| Ownership | THIN (stale) → FILLED (§2.1): five 13G/13G-A filings after the 18 Jun 2026 proxy were not in file 03. |
| People | OK. Insider holdings and sales verified on EDGAR (§2.3). |
| Legal | OK (no material proceedings; no BIS enforcement found). |
| Guidance track record | OK (11 quarters; 10 beats, 1 met). |

### Module B (ledgers)
| Claim | Verdict in ledger | Status of evidence |
|---|---|---|
| C1 HBM4/4E add steps per stack | Partly supported, medium | Independent evidence on "more steps per stack" = 0%. |
| C2 HB expands TAM | (see ledger_C2) | Timing and net effect rest on [CO] for Camtek-specific parts. |
| C3 Holds/gains share vs Onto at HBM makers | Not supported, medium | Independent firsthand evidence for the claim = 0 items. §2.6 adds one secondhand analyst item (Stifel) consistent with Korea/Samsung weakness. |
| C4 2026 orders convert on schedule | Partly supported, medium | §2.4 adds the first independent corroboration of a 2026 order's size; it does not test conversion. §2.2 adds a market-data item relevant to dilution, not to conversion. |
| Handoff cell: share of revenue that depends on micro-bump inspection | ESTIMATE only (file 06 §6.3) | No Camtek disclosure. See §4. |

---

## 2. Gaps filled (new research, sourced)

### 2.1 Ownership after the June 2026 proxy (Module A) — FILLED

File 03 §d.1 stops at the proxy table "as of 18 Jun 2026" [file 03, 25]. EDGAR shows seven Schedule 13G/13G-A filings dated after that table [6]. All are QUANTIFIED, filed by the holders.

| Holder | Event date | Shares | % of class | Filed | Source |
|---|---|---|---|---|---|
| Harel Insurance Investments & Financial Services | 31 Mar 2026 | 3,632,087 | 7.8% | 4–5 May 2026 | [13] |
| Wasatch Advisors LP | 30 Jun 2026 | 2,121,920 | **4.5%** (below the 5% line) | 9 Jul 2026 | [12] |
| Migdal Insurance & Financial Holdings (of which Migdal Sal Domestic Equities) | 30 Jun 2026 | 3,886,580 (3,411,665) | 8.33% (7.31%) | 23 Jul 2026 | [10] |
| Phoenix Financial Ltd. | 6 Aug 2026 | 2,386,573 | 5.12% | 11 Aug 2026 | [11] |
| Migdal (same) | 30 Sep 2026 | 4,446,770 (3,983,965) | 9.53% (8.54%) | 19 Oct 2026 | [8] |
| Menora Mivtachim Holdings | 14 Oct 2026 | 2,369,026 | 5.08% | 19 Oct 2026 | [7] |
| Migdal (same) | 15 Oct 2026 | **4,692,885** (4,225,218) | **10.06%** (9.05%) | 20 Oct 2026 | [9] |

- Unchanged from file 03 (no new filing found): Priortech 9,617,787 (20.61%) and Chroma ATE 7,817,440 (16.75%) at 18 Jun 2026 [file 03, 25].
- DERIVED: holders above 5% on the latest filings = Priortech 20.61% + Chroma 16.75% + Migdal 10.06% + Harel 7.8% (as of 31 Mar) + Phoenix 5.12% + Menora 5.08% = **65.4%** of the class. The dates differ (31 Mar to 15 Oct 2026), and holdings of Israeli insurers' managed funds may overlap in method of counting; this is an indicative sum only.
- DERIVED: four Israeli institutional groups (Migdal, Harel, Phoenix, Menora) together ≈ 28.1% on these filings (10.06 + 7.8 + 5.12 + 5.08).
- Migdal's stake rose from 3.89M shares (30 Jun) to 4.69M (15 Oct 2026), +806,305 shares (DERIVED).

### 2.2 2030 Notes: was the 130% stock-price conversion condition met? (Module A, convertible notes) — FILLED for Q3 2026

Terms (file 03 §c.1, [CO]): initial conversion price ~$109.34; before 15 Jun 2030 holders may convert in a calendar quarter if the stock was ≥130% of the conversion price on ≥20 of the 30 consecutive trading days ending on the last trading day of the prior quarter (testable from Q1 2026). Trigger = 1.30 × 109.34 = **$142.14** (DERIVED, file 03).

Test window for Q3 2026 = the 30 trading days ending 30 Sep 2026 = 19 Aug – 30 Sep 2026 (DERIVED: 21 September trading days, Labor Day 7 Sep excluded, plus 9 August days).

Closing prices [15], cross-checked against [16] on the overlapping September dates (identical):
- September days at or above $142.14 (15): 4 Sep 145.72; 8 Sep 147.01; 9 Sep 148.66; 10 Sep 144.25; 11 Sep 147.97; 17 Sep 144.21; 18 Sep 149.12; 21 Sep 149.63; 22 Sep 151.36; 23 Sep 147.06; 24 Sep 145.12; 25 Sep 147.05; 28 Sep 142.61; 29 Sep 152.82; 30 Sep 155.25.
- September days below (6): 1 Sep 128.14; 2 Sep 131.91; 3 Sep 138.90; 14 Sep 133.84; 15 Sep 134.66; 16 Sep 138.59.
- August days at or above (5): 21 Aug 146.81; 24 Aug 142.33; 25 Aug 146.66; 26 Aug 143.25; 27 Aug 144.81. Below (2): 28 Aug 135.57; 31 Aug 134.00. 19 and 20 Aug: not retrieved.
- **DERIVED: at least 20 of the 30 days closed at or above $142.14.** On closing prices from [15]/[16], the condition appears to have been met at 30 Sep 2026, which would allow holder conversion during Q4 2026 (1 Oct – 31 Dec 2026). The margin is thin: the 20th qualifying day (28 Sep, $142.61) is $0.47 above the trigger. The indenture uses the "last reported sale price"; the exact indenture definition was not re-read here.
- **Not disclosed by Camtek:** the Q3 2026 release does not mention convertibility [1]. The notes remain in long-term liabilities at 30 Sep 2026 ($489.184M) [1]. Camtek can settle conversions in cash, shares or a combination (file 03 §c.1).
- DERIVED economics at the latest price: conversion value per $1,000 note = 9.1455 × $89.20 (close, 20 Nov 2026 [15]) = **$815.78**, i.e. ~18% below par. Conversion during Q4 2026 would therefore be below par value at current prices.
- The Q2 2026 test (window ending 30 Jun 2026) could not be checked: daily prices for May–June 2026 were not retrieved. The 52-week range quoted by Motley Fool's quote page was $91.91–$215.99 (date of high not given; search summary only).

**Nearest maturity (2026 Notes, 1 Dec 2026):** no new information. EDGAR shows no Camtek filing about the notes between 10 Aug and 21 Nov 2026; the only Camtek 6-Ks are 14 Oct (two) and 4 Nov 2026 [6]. Residual principal remains $63,000 as of 4 Mar 2026 (file 03). DERIVED observation: the 30 Sep 2026 balance sheet shows a single "Convertible notes" line of $489.184M under long-term liabilities and no current portion [1]; the $63k residual due 1 Dec 2026 is immaterial and is not shown separately.

### 2.3 Insider holdings and 2026 sales verified on EDGAR (Module A, people/ownership) — FILLED

File 03 used a MarketBeat aggregator for the August 2026 sales ("not verified"). EDGAR now carries Forms 3 (initial statements, filed around 30 Jul 2026) and Forms 4 for Camtek officers and directors [14]. Transactions, QUANTIFIED (prices are not shown on the EDGAR summary):

| Date | Insider | Role | Transaction | Shares | Held after |
|---|---|---|---|---|---|
| 11 Aug 2026 | Moshe Eisenberg | CFO | Sale | 3,759 | 16,884 |
| 12 Aug 2026 | Moshe Eisenberg | CFO | Sale | 645 | 16,239 |
| 11–12 Aug 2026 | Lior Aviram | Director (Executive Chairman) | Four sales | 6,694 total (1,658 + 1,689 + 1,666 + 1,681) | 12,518 |
| 12 and 17 Aug 2026 | Orit Geva-Dvash | VP HR (Chief People Officer per file 03) | Sales | 923 total | 5,205 |
| 13 Aug 2026 | Rafi Amit | CEO | Sale | 6,250 | 55,350 |
| 13 Aug 2026 | Ramy Langer | COO | Sale | 6,387 | 17,532 |
| 13–14 Aug 2026 | Yael Andorn | Director | Option exercises and sales | 5,532 sold (880 + 1,476 + 3,176) | 1,343 |
| 29 Jul 2026 | Directors Stav, Shacham-Diamand, Andorn, Ben-Arie | Directors | Awards (254 shares + 571 options each) | — | — |

- DERIVED: officers' and directors' open-market sales 11–17 Aug 2026 total **30,190 shares** (3,759 + 645 + 6,694 + 923 + 6,250 + 6,387 + 5,532). At ~$150–160 per share (closes not retrieved for those dates; MarketBeat's CFO figure implies $160.06), that is roughly $4.5–4.8M (ESTIMATE; price range assumed).
- The CFO figure (3,759 shares) matches MarketBeat [file 03, 42]. The MarketBeat-reported CEO sale (6,250 shares, 13 Aug) also matches. File 03's "not verified" is now verified on EDGAR.
- No Form 3/4 filings by Camtek insiders appear on EDGAR before July 2026 [14]. The reason (a rule change for foreign private issuers or a voluntary change) was not researched. **Not verified.**

### 2.4 Independent corroboration of a 2026 order's size (Q6, Q5, ledger_C4) — FILLED (partly)

File 07 [35] found an ASE MOPS filing: SPIL bought **6 batches** of equipment from **Camtek Ltd.**, total **NT$1,749,615,253**, average NT$291,602,542 per batch, transactions 22 Jun – 16 Jul 2026, decided by price comparison/negotiation [IND, FIRSTHAND procurement filing]. File 07 converted it with an assumed NT$29–33/US$ rate ("rate not verified").

FRED DEXTAUS (noon buying rates, H.10) [17]: 22 Jun 2026 31.63; 30 Jun 31.85; 16 Jul 32.25 NT$/US$.
- DERIVED: 1,749.615 / 31.63 = **US$55.3M**; 1,749.615 / 32.25 = **US$54.3M**. Per batch: US$9.0–9.2M.
- Camtek's 2 Jun 2026 release announced "a multi-system order totaling $55 million from a tier-1 OSAT supporting AI applications", for delivery in 2027 [file 08, 36] [CO].
- INFERENCE (moderate confidence): the SPIL purchase (US$54.3–55.3M, contracted 22 Jun – 16 Jul 2026) matches the $55M tier-1 OSAT order in size and timing (the MOPS filing date follows the 2 Jun announcement by 3–6 weeks). Premises: same size within ~1%; SPIL is an ASE subsidiary and ASE is a tier-1 OSAT; no other Camtek order of that size was announced in mid-2026. The filing does not name the order, give delivery dates or tool types.
- What this does and does not show for ledger C4: it is the first independent document that sizes a Camtek 2026 order. It says nothing about delivery timing or revenue conversion (delivery is stated as 2027 by Camtek).
- The secondhand "~$63M ASE orders from Camtek" (Longbridge, citing "Chips & Wafers") [file 07, 39] remains **not verified**; it is ~$8M above the SPIL filing.

### 2.5 Top-three customer share bounds (Module A, customer concentration) — FILLED as DERIVED

Camtek discloses only customers above 10% (20-F) [file 03 §b.1]. Since every other customer is at or below ~10%, the top-three share has an upper bound as well as the lower bound file 03 gives.

| Year | Customers >10% (20-F) [CO] | Top-three, DERIVED range | Arithmetic |
|---|---|---|---|
| 2021 | none | ≤ ~30% | 3 × ≤10% |
| 2022 | one at 11% | 11% to ≤ ~31% | 11 + 10 + 10 |
| 2023 | one at 15% ("more than 15%" in the FY2023 20-F) | 15% to ≤ ~35% | 15 + 10 + 10 |
| 2024 | three at 15%, 10%, 10% | **~35%** (both bounds, subject to rounding of the "10%" figures) | 15 + 10 + 10 |
| 2025 | one at 11% | 11% to ≤ ~31% | 11 + 10 + 10 |
| 9M 2026 | not disclosed | — | — |

Caveat: the 20-F figures are rounded; "10%" customers in 2024 could each be between 10.0% and 10.5%. The upper bounds assume no fourth customer above 10%, which is what the 20-F states.

### 2.6 Korea revenue decline in 2025: an independent attribution (Q5, ledger_C3) — partly FILLED

- File 02/07: Korea revenue fell from $117.1M (2024) to $36.9M (2025), −68.5% (DERIVED from the 20-F); Camtek gave no explanation.
- [IND, SECONDHAND] Investing.com's paraphrase of a Stifel note, 10 Nov 2025 [18]: "Growth in China, logic/outsourced semiconductor assembly and test (OSAT) markets, and Micron has helped offset broader weakness in Korea this year, likely related to Samsung, according to Stifel's analysis." The same article relays Camtek management: "its 3D metrology market share in HBM4 … remains intact" [CO-relayed].
- This attributes the Korea weakness to Samsung (hedged "likely"), not to SK hynix or to share loss. It is an analyst inference, not data, and the note itself was not read.
- Search of Korean press for Camtek-specific HBM 2026 coverage (캠텍 HBM 검사장비) returned no Camtek item; a Hyundai Motor Securities equipment report (13 May 2026) [20] contains no Camtek or Onto mention. **Not found:** any Korean report on Camtek's position at SK hynix or Samsung in 2026.

### 2.7 Q2 2024 call (Q3, Q6): verified — FILLED

File 05 could not retrieve the Q2 2024 transcript. Read on StockAnalysis [5]:
- Rafi Amit: "receiving multiple systems order of over $25 million from a global Tier 1 customer to inspect HBM wafers … this customer added $6 million, bringing the entire order to over $31 million." QUANTIFIED. Verifies the summary-only "$25M → $31M" in file 05.
- Rafi Amit, on inspection intensity: customers "use more inspection steps to maintain high yield"; asked how much intensity would rise: "a little bit too early at this stage to really pinpoint the steps." QUALITATIVE. A further instance of "more steps" with no count (Q3 / ledger C1).
- HPC (HBM + chiplets) "over 50% of our sales" in Q2 2024; full-year HPC expected "anywhere between 50%-60%". QUANTIFIED. Matches file 02.
- CFO: "Asia 92%, US and Europe accounted for 8%"; HBM "is currently manufactured in Korea and Taiwan." QUANTIFIED. Matches file 02.
- Stack height (8/12/16-high): not mentioned on this call.

### 2.8 Q1 2026 Asia vs rest-of-world split (Module A, China by quarter) — confirmed not given

File 02 recorded the Q1 2026 Asia split as "Not found". Re-reading the Q1 2026 transcript [4]: the CFO's remarks contain **no geographic split** and no China percentage; China came up only in the COO's Q&A. The Q1 2026 release has no geographic data [3]. Status: **Not disclosed by Camtek for Q1 2026** (the only quarter since Q1 2023 without an Asia figure).

CFO's gross-margin wording on that call [4], consistent with file 02: "The gross margin for the quarter was 51%, similar to the previous quarter"; "I expect the gross margin to improve in the second half of the year, in line with our strong revenue forecast … the contribution of the Hawk and the Eagle G5, which are expected to double in revenues versus last year." QUANTIFIED (double).

### 2.9 NanoProf measurement scope (Q1) — partly FILLED

Camtek's SEMICON Taiwan 2026 news sheet [19] (seen through a search summary; [CO]): NanoProf is a "next-generation multi-sensor metrology platform for advanced packaging", combining optical metrology sensors with "AI-enhanced analytics", for **wafer geometry, post-CMP nano-topography, TSV, thin-film and overlay measurement**. QUALITATIVE. This adds overlay and thin-film to file 01's list (warp, RDL, TSV, pre-bond, post-CMP). **Still not found:** any NanoProf numeric resolution, repeatability or throughput.

---

## 3. Inconsistencies between files, and the settled values

| # | Item | File A says | File B says | Settled value | Settling source |
|---|---|---|---|---|---|
| 1 | Quarter of the $7.7M one-time tax expense | File 02 §3.1: **Q1 2026** | File 03 §a.1 and Contradiction 9: **Q2 2026** | **Q2 2026.** The Q2 2026 reconciliation lists "One-time Tax expenses 7,700" in both the six-month and the three-month columns ended 30 Jun 2026; the Q1 2026 reconciliation has no tax item [2], [3]. Q2 2026 GAAP tax expense was $10.899M vs $3.221M in Q2 2025 [2]. The nature of the item is still not disclosed. | [2], [3] [CO] |
| 2 | Q2 2026 acquisition-related adjustments | File 02: "$3.9M in operating income" (Visual Layer) | File 03: "6-month total $4.7M, including $2.6M one-time M&A" | Operating-income adjustment: **$3.928M (Q2 2026), $4.620M (6M 2026)**. Net-income adjustment: $3.570M (Q2), $4.059M (6M). Gross-profit adjustment: $1.097M (Q2). The $2.6M one-time M&A expense sits in G&A. The adjustments include FRT amortisation as well as Visual Layer items, so "Visual Layer $3.9M" overstates the Visual Layer part. File 03's "$4.7M" should read $4.6M (operating) or $4.1M (net). | [2] [CO] |
| 3 | Q3 2026 release highlights | File 01, Contradiction 11: highlights say "GAAP operating income of $8 million" and "GAAP net income of $8 million" | Files 02/03: GAAP OI $39.8M, NI $42.8M | **No such inconsistency in the release.** The highlights read "GAAP operating income of $39.8 million and non-GAAP operating income of $47.5 million … GAAP net income of $42.8 million and non-GAAP net income of $50.3 million" [1]. File 01's Contradiction 11 is an extraction error and should be deleted. | [1] [CO] |
| 4 | Ownership table at mid-2026 | File 03 §d.1: Migdal 2,332,037 (5.00%) and Wasatch 2,728,318 (5.85%) "as of 18 Jun 2026" (proxy) | Holders' own 13G/A: Migdal 3,886,580 (8.33%) at 30 Jun 2026; Wasatch 2,121,920 (4.5%) at 30 Jun 2026 | The proxy figures for Migdal reproduce the 20-F (March 2026) figure. **Latest values: Migdal 10.06% (15 Oct 2026); Wasatch 4.5% (30 Jun 2026); Harel 7.8% (31 Mar 2026); Phoenix 5.12% (6 Aug 2026); Menora 5.08% (14 Oct 2026).** | [7]–[13] [IND] |
| 5 | CEO shareholding | File 03 §d.1: Rafi Amit holds 34,128 shares incl. 8,546 RSUs (20-F / proxy) | EDGAR Form 3/4: seven holding lines summing to 61,600 ordinary shares before the 13 Aug 2026 sale; 55,350 after | Not reconciled by Camtek. DERIVED sum of Form 3 lines: 7,467 + 10,008 + 15,145 + 8,336 + 5,558 + 10,431 + 4,655 = 61,600; minus 6,250 sold = 55,350 [14]. The Form 3 lines may include unvested RSUs reported as share lines, or vesting between March and July 2026. Recorded as an open difference. | [14] |
| 6 | Onto Q2 2026 figures (>$200M single-OSAT order; backlog) | File 08 §10.5: "NOT VERIFIED (summaries only)" | File 07 [27]: read in the Benzinga/Webull transcript of Onto's Q2 2026 call | **Verified by file 07's transcript reading** (>$200M Dragonfly orders from a single OSAT, majority for 2027). Onto's Q3 2026 backlog: record $1.3B (file 07 [28]). File 08's "not verified" flag is superseded. | file 07 [27], [28] [IND] |
| 7 | Onto Feb 2026 HBM VPA and SK hynix award | File 05 [32], [33]: "Not opened (HTTP 403)", summary only | File 07 [22], [23], [21]: read in Onto's 8-K Ex. 99.1, the call transcript and Onto's PDF release | **Verified by file 07**: VPA "estimated at over $240 million" with a leading HBM manufacturer for Dragonfly 2D and 3D bump metrology through 2027, including ">$60 million" of 3D bump metrology; the SK hynix Best Partner Award release dated 12 Oct 2026. | file 07 [21]–[23] [IND] |
| 8 | Origin of the "$650M capacity" figure | File 03 §h.2: Camtek's original statement "not located"; only an analyst's reference | File 08 §9.1: Q3 2024 call (12 Nov 2024): "we can go over $600 million … adding at least 10% in this European location … closer to $660 million" | **Located by file 08** ([CO], 12 Nov 2024). The analyst's "$650M" is a rounding of Camtek's "closer to $660 million". | file 08 [48] [CO] |
| 9 | 2026 tool split, inspection vs bump metrology | File 01 "Not found": slide numbers did not extract | Files 02 §1.2 and 06 §4.2: 60% 2D inspection / 25% inspection + 3D sensor / 15% dedicated 3D bump metrology (units, 2026); transcript: "85% … inspection … about 15% … solely for bump height metrology" | **60 / 25 / 15 (unit shares, 2026)**, from the Analyst Day transcript and the slide image read in file 06. | file 06 [1], [2] [CO] |
| 10 | Pointer to the main export-rules treatment | File 03 §f.4: "the main Module A treatment of China is in file 02" | File 04 is the dedicated export-rules file | **File 04** holds the export-rule analysis; file 02 holds China share figures. Both agree on the China numbers (2022 44.2%, 2023 47%, 2024 31%, 2025 49%; FY2026 "~45%"). | files 02, 04 |
| 11 | Q4 2025 call prepared remarks speaker | File 02 Contradiction 12: attributed to Ramy Langer (COO) | File 05 §2.4: "Rafi Amit (prepared)" for the same call | Transcripts differ; not material to any figure. Unresolved; recorded. | files 02, 05 |
| 12 | Onto Q3 2026 call date | File 05/07: 9 Nov 2026 | Ledger C2 [19]: 10 Nov 2026 | The Motley Fool page is dated 10 Nov 2026; the call itself is given as 9 Nov in files 05 and 07. Not material. | file 07 [28] |
| 13 | China share figures, all years | Files 02 and 04 | — | **Consistent**: identical $ figures 2022–2025 and identical stated percentages. No correction needed. | files 02, 04 |
| 14 | Gross margin by quarter | File 02 table | Releases re-checked for Q1–Q3 2026 | **Consistent**: Q1 2026 51.0%, Q2 51.4%, Q3 51.1% non-GAAP; 9M 2026 51.1% (212,822 / 416,196 = 51.1%, DERIVED); Q3 2025 comparative 51.5% [1], [2]. | [1], [2] [CO] |
| 15 | Handoff cell | File 06 §6.3 | Ledger C2 §4 and handoff | **Consistent**: M1 34.5 / 48.5 / 57.3%; M2 5.4 / 10.0 / 25.8% (LTM Q4 2025–Q3 2026, $544.3M). | files 06, ledger_C2 |
| 16 | KLA advanced-packaging process-control revenue 2026 | File 06: "~$1B in 2026" (Apr 2026 call) | File 07: "approximately $1.1 billion" (Oct 2026 call) | Not a conflict: the later KLA call raised the figure. **Latest: ~$1.1B (CY2026, KLA, 28 Oct 2026).** | file 07 [34] [IND] |

---

## 4. Items resting only on [CO] sources (no independent check exists)

These are the load-bearing figures for the final report that have **no** independent corroboration after this review:

1. Revenue by application, every quarter (Q2). Camtek's verbal approximate percentages only.
2. Every statement about inspection or metrology steps per HBM generation (Q3, ledger C1).
3. Hybrid-bonding shipments, customers and revenue (Q4, ledger C2): "several sites", "a few machines", "low magnitude".
4. "Tool of record for all 3D metrology for HBM4 at all HBM manufacturers" and "have not lost share" (Q5, ledger C3).
5. The YTD order totals (>$600M, >$800M), the >$260M HBM "order and forecast" and the 2027 >$800M outlook (Q6, ledger C4). Exception: the size of one order ($55M tier-1 OSAT) now matches an independent SPIL filing (§2.4).
6. Quarterly Asia vs RoW split and the FY2026 China "~45%" (Module A).
7. Gross-margin mix effects named by management (Module A). The quarterly margins themselves come from Camtek's releases; the annual ones are audited.
8. Product specifications, throughput and resolution (Q1).
9. Stated manufacturing capacity in $ (Q6).
10. **Handoff cell** (share of revenue that depends on micro-bump inspection): an ESTIMATE whose inputs are Camtek's 2026 unit split (60/25/15), Camtek's verbal AI/AP percentages and the analyst's assumptions (file 06 §6). No independent input exists. The base case M1 (all bump-linked revenue) is 48.5%; M2 (die-to-die micro-bumps that hybrid bonding would remove) is 10.0%.

---

## 5. What remains unfillable, and why

- **China share by quarter since 2023:** Not disclosed by Camtek (annual 20-F only; quarterly Asia vs RoW only, and none for Q1 2026). An independent proxy would be China Customs imports from Israel under HS 9031.41 (optical inspection instruments for semiconductor wafers/devices), monthly; a search found no published 2025–2026 bilateral figure, and the series would mix Camtek with Nova and others. **Not obtained.**
- **HBM vs CoWoS-type revenue split** after Q1 2024; **CIS, compound and front-end revenue** by quarter: Not disclosed by Camtek.
- **Step counts per HBM generation:** not given by Camtek, memory makers, competitors or analysts in any public source found.
- **Hybrid-bonding systems shipped, revenue and customers:** Not disclosed by Camtek; no independent source names Camtek as an HB supplier.
- **Customer identities** for any 10% customer or announced order: Not disclosed. The SPIL filing (§2.4) identifies one purchase, not a 10% customer.
- **Top-three customer share:** Not disclosed; only the DERIVED bounds in §2.5.
- **Backlog $, RPO, book-to-bill, order definition, cancellation fees, deposit terms:** Not disclosed by Camtek.
- **2030 Notes, Q2 2026 conversion test:** daily prices for May–June 2026 not retrieved. Q3 2026 test: met on closing prices (§2.2), but the indenture's exact price definition and 19–20 Aug 2026 prices were not checked.
- **Settlement of the $63k residual 2026 Notes at 1 Dec 2026:** no notice; the event falls after the research date.
- **Settlement method of the ~$32.9M of 2026 Notes converted in Q1 2026:** not stated; share settlement remains INFERRED (file 03).
- **ECCNs, US-origin content, BIS licences, Israeli export licences** for Camtek tools: Not disclosed (file 04).
- **Independent technical specifications** (throughput, resolution) for Hawk, Eagle G5 and NanoProf: not found.
- **The 13 Oct 2026 "announcement" by a larger 2D-inspection entrant** referred to by Camtek's COO: not identified (searched again; Koh Young and Nordson pre-show items found, neither matches).
- **Samsung, Micron and TSMC customer-issued documents naming Camtek, Onto or KLA** for HBM or CoWoS inspection: not found.
- **Nature of the $7.7M one-time tax expense (Q2 2026):** not disclosed.
- **FY2025 20-F revenue-recognition note (F-pages):** not read; whether the wording change in MD&A reflects a policy change is unresolved (file 08).
- **Why Camtek insiders began filing Forms 3/4 in July 2026:** not researched.

---

## Contradictions (new in this review)

1. **Release vs proxy on holdings.** The 2026 proxy table "as of 18 Jun 2026" shows Migdal at 2,332,037 shares (5.00%) and Wasatch at 2,728,318 (5.85%) [file 03, 25]. Twelve days later Migdal reported 3,886,580 (8.33%) [10] and Wasatch 2,121,920 (4.5%) [12]. The proxy appears to carry earlier (March 2026) figures for these holders.
2. **CEO shareholding.** Proxy/20-F: 34,128 shares including 8,546 RSUs [file 03]. EDGAR Form 3/4: 61,600 shares before, 55,350 after the 13 Aug 2026 sale (DERIVED from [14]). Not explained.
3. **File 01's Q3 2026 "$8 million" contradiction** is not in the release; the release gives $39.8M GAAP operating income and $42.8M GAAP net income [1]. Recorded so the final report does not repeat it.
4. **One-time tax expense quarter.** File 02 (Q1 2026) vs the Q2 2026 release (Q2 2026) [2]; the release governs.
5. **Unverified ASE figure vs filing.** "~$63M" (Longbridge citing "Chips & Wafers") vs US$54.3–55.3M (SPIL MOPS filing at FRED rates) [file 07, 35], [17]. The secondhand figure may include other ASE entities or orders; not resolved.
6. **2030 Notes classification vs conversion condition.** The notes stayed in long-term liabilities at 30 Sep 2026 [1] while closing prices met the 130% condition for the Q3 2026 window on [15]/[16] (DERIVED, §2.2). Camtek may settle in shares, so long-term classification is not necessarily inconsistent; Camtek has not commented.

---

## Not found / not verified (this review)

- Not found: CAMT daily closing prices for 19–20 Aug 2026 and for May–June 2026.
- Not verified: the 2030 Notes indenture definition of the price condition (re-read not done; terms taken from file 03).
- Not found: any Camtek 6-K or notice on the 2026 Notes after 4 Mar 2026.
- Not found: Korean, Taiwanese or Chinese trade-press items in 2026 naming Camtek at SK hynix, Samsung, Micron or TSMC (search of 캠텍 HBM 검사장비 2026 and the Hyundai Motor Securities report [20]).
- Not found: China customs HS 9031.41 imports from Israel for 2025–2026.
- Not found: NanoProf numeric specifications.
- Not verified: the full text of the Stifel note behind [18] (paraphrase only).
- Not read: the Motley Fool quote page cited by search for the $215.99 52-week high (date of high unknown).
