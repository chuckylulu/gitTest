# Measurement and yield software, AI and reference-data ownership: PDF Solutions deep dive, field scan, prior checks

Research date: 12 November 2026. All "latest" figures are as of this date; PDF Solutions' July-September 2026 quarter was published on 5 November 2026 and is used throughout.
Status: INTERIM v1, written after an interruption. Sections marked [INCOMPLETE] are still being extended.
Scope: the software, data and AI layer. The hardware physics behind the priors and the individual tool makers are covered by other researchers.
Labels: "company claim, unconfirmed" means no outside party confirmed it. "Inference" marks my own reasoning. "Could not verify" marks a gap.

## Evidence tables

### Table 1: PDF Solutions (Nasdaq: PDFS), quality tests (a)-(e), transitions 1-6, entry point

| Item | Evidence (dated; sources in the detail sections) | Short read |
|---|---|---|
| (a) Position | eProbe/DirectScan e-beam electrical inspection tools placed in fabs: 6 at end-2025 (5 on subscription), about 12 targeted by end-2026 (company, May 2026). CV test chips with Gainshare royalties tied to customer yield and volume. secureWISE, the remote-access network equipment makers use to reach their tools inside fabs: 100+ vendors and 190+ fabs at acquisition, Feb 2025 (company claim, unconfirmed). Cimetrix connectivity SDK embedded in equipment. Exensio analytics running on customers' data. PDF does not own the customers' reference data. The 10-K names customers' in-house teams plus Tableau, Spotfire, Snowflake and Databricks as indirect competitors. | One network chokepoint (secureWISE), one small "judge" tool line (eProbe), and an analytics layer that is partly substitutable |
| (b) Lead | No third-party market-share data found. Samsung presented its eProbe use at PDF CONNECT in Oct 2026, and an Intel speaker said at PDF's Dec 2025 Users Conference that Intel is standardising on secureWISE. Both reach us only through PDF channels (company-reported, not independently confirmed). | Thin outside evidence |
| (c) Revenue model | FY2025 Platform revenue $181.0M (licences, SaaS, services, DirectScan, CV fixed fees) and Volume-based $38.0M (Cimetrix runtime per tool shipped, secureWISE fees per tool and per data volume, Gainshare). "Recurring" was 88% of Q3-26 revenue (95% in Q3-25), but the definition counts Gainshare, runtime licences and "other services". 180 of 600 staff are field application engineers. No per-seat pricing is described. | Mostly multi-year subscriptions plus usage and outcome tolls, with some services |
| (d) Financial strength | Q3-26 revenue $68.3M (+20% y/y); non-GAAP gross margin 77% and operating margin 28%; GAAP operating margin 12%. 9M-26 operating cash flow $31.8M against capex $39.7M, so free cash flow was negative (TTM about -$0.3M). Sep-26: cash $107.1M, debt principal $66.25M. Customer A was 20% and B 26% of Q3-26 revenue; three customers were 53% of FY2025; receivables A 35%, C 22%. Q3-26 geography: US 33%, Japan 32%, China 16%. GAAP ROIC 5.0%. | High gross margin, low GAAP returns, high concentration, heavy capex for a software firm |
| (e) Resilience | "Equipment business" about 20% of total (Cimetrix tracks WFE shipments; secureWISE tracks the installed base). Backlog $247.2M (-15% y/y), "majority" recognised within two years. China 15% of 9M-26 revenue. BIS 50%-affiliates rule suspended "until November 2026". SMIC unpaid since 2019 (award in PDF's favour; set-aside decision pending). | Moderately cyclical through the equipment piece; an export-control event falls due now |
| T1 Imaging to inference | eProbe voltage-contrast e-beam infers buried electrical defects. AI in Exensio Characterization (said Q1-26). No stated uncertainty metric found. | Done in hardware; uncertainty not stated |
| T2 AI agents | Exensio Aurora announced 9 Sep 2026, beta Sep 2026; LLM agents assemble analytics workflows as reviewable Python. CEO: too early to judge monetisation. The agents build analytics workflows, not tool measurement recipes. | Said, beta shipped, no results |
| T3 Stacks and packaging | Exensio Assembly Operations; secureWISE DEX OSAT network; Aurora pitched at 3D and advanced packaging. No named packaging customer. | Said; product exists |
| T4 Hardware to software and data | Already about 94% "analytics" (TTM Q3-25), but partly moving the other way: eProbe as hardware-as-a-service, capex 21% of 9M-26 revenue. Data is monetised as a toll (secureWISE per tool and data volume), not by owning reference data. | Toll on the data flow |
| T5 On-premises AI | Exensio sold on-prem or SaaS. Aurora: "on-premise options where cloud-hosted solutions are not preferred"; edge deployment to OSATs and test floors. CEO: on-prem to cloud migrations raised ARR 2-3x. | Supports both; economics favour cloud |
| T6 Fewer tools per wafer | No PDF statement found. Runtime licences (per tool shipped) and secureWISE (per connected tool) are tied to tool counts. | Exposed; not addressed |
| Entry point | $41.79 (close 11 Nov 2026); market cap $1.77B; EV $1.73B. Trailing GAAP P/E 108.5x, forward 27.0x, EV/sales 6.9x. 8 analysts, average target $56.25. 2026 growth guide about 20% (implies Q4 about $73M). May-26 offering priced at $44.00. Oct-26 range $38.63-$56.98. Own 5-10 year multiple range: not found. | Detail in the entry-point section |

### Table 2: Evidence on the priors and the open question (summary)

| Prior / question | Evidence for | Evidence against or missing | Status on evidence found |
|---|---|---|---|
| A (60%): agents make recipe set-up 5x+ faster at leading users by 2028 | Agent frameworks are shipping: PDF Aurora beta Sep 2026; Synopsys AgentEngineer in design (Oct 2026). Qualitative vendor claims, e.g. Nordson: prompting could "eliminate a lot of programming needs" (Jun 2026). | No measured metrology or inspection recipe speed-up from any party in the 2025-26 sources read. PDF: "too early", feedback "mostly demo-related" (Nov 2026). PDF estimate: over 70% of AI initiatives stall after pilots (Jun 2026). | Unsupported by measurement so far [INCOMPLETE] |
| B (70%): signal fusion becomes standard for nanosheet | Onto: "Hybrid ML/physics models are superior to ML only because they are inherently more robust" (Jun 2026). Nova sells OCD, XPS, SIMS and Raman tools with ML (Nova FIT) "to complement physical modeling" (20-F, Feb 2026). | IBM spectra-to-reference work and the SPIE AL 2026 X-ray plus optical papers were not yet retrieved. | Directionally supported [INCOMPLETE] |
| C: learned denoising safe for the expected, risky for the unexpected | SK hynix and Gauss Labs used a "universal denoiser" to raise metrology throughput (SPIE 2024), i.e. denoising applied to measuring known features. Inspection sources stress rare defects, biased customer datasets and reliance on synthetic data (Jun 2026). | No direct hallucination study retrieved yet. | Plausible, not yet evidenced [INCOMPLETE] |
| D (35%): fewer tools per wafer after 2030 | Gauss Labs and SK hynix: virtual metrology on "near-100%" of wafers versus 1-5% physical sampling (press, Feb 2026, company-supplied). Gauss VM sold to "reduce or expand sampling". ASU and Intel Foundry VM research (Jun 2026). | No measured fall in physical sampling or tool count found. Cohu: VM "may never be 100% perfect" and will not completely replace metrology tools (Sep 2025). SK hynix's published VM uses are tool matching and anomaly detection, which complement physical measurement. | Weak evidence for; qualified evidence against |
| Open question: who owns reference data and value | Data hierarchy: device data most protected, then process data, with equipment-health data least protected (Teradyne, Jan 2026). Sharing set "at the contractual stage" (Synopsys). Vendor pooling exists in narrow cases: Nordson's cross-customer bump-void model; NIST/NSF cross-factory VM pilot found cross-factory data "more robust". Neutral hubs: Athinia (Palantir Foundry; owners set permissions), PDF secureWISE and anonymisation. On-site deployment is the norm for start-ups (Gauss: "deployed in your environment... avoid IP issues"). | No evidence yet of a vendor holding or pooling TEM/SEM reference cross-sections across chipmakers. TSMC, Samsung and Micron in-house work not yet retrieved. | Leans to chipmakers holding the data while vendors take tolls and licences [INCOMPLETE] |

## Q1. PDF Solutions business quality (tests a-e)

### Takeaway
PDF is a high-gross-margin (77% non-GAAP), 20%-growth data and analytics vendor. Its most defensible assets are a network toll (secureWISE, Cimetrix) and outcome-linked contracts (Gainshare). Weak points: high customer concentration (two customers were 46% of Q3-26 revenue), thin GAAP profits and returns, capex-heavy eProbe hardware-as-a-service, and outside evidence of a lead that reaches us mostly through company channels.

### Cited Findings
**Results**
- Q3 2026 (quarter to 30 Sep, released 5 Nov 2026): revenue $68.334M versus $61.529M in Q2-26 and $57.115M in Q3-25 (+20% y/y). Platform $58.331M (+22% y/y); Volume-based $10.003M (+10% y/y, -19% q/q). GAAP/non-GAAP gross margin 73%/77%; GAAP/non-GAAP operating margin 12%/28%. GAAP net income $6.841M ($0.16 diluted); non-GAAP $17.161M ($0.40). Backlog $247.2M, down from $270.7M in Q2-26 and $292.0M in Q3-25 — [8-K Ex.99.1, 5 Nov 2026](https://www.sec.gov/Archives/edgar/data/0001120914/000143774926035288/ex_1002246.htm)
- 9M 2026: revenue $189.993M versus $156.621M (+21%); GAAP operating income $19.663M versus $2.389M; non-GAAP operating margin 25% versus 20% — [8-K Ex.99.1, 5 Nov 2026](https://www.sec.gov/Archives/edgar/data/0001120914/000143774926035288/ex_1002246.htm)
- FY2025 (released 12 Feb 2026): revenue $219.024M versus $179.465M (+22%); Q4-25 $62.403M (+25%). Platform $181.025M versus $157.166M; Volume-based $37.999M versus $22.299M. GAAP/non-GAAP gross margin 72%/76%; GAAP/non-GAAP operating margin 3%/21%. GAAP net loss $(0.64)M; non-GAAP EPS $0.94. Year-end backlog $254M — [8-K, 12 Feb 2026](https://www.sec.gov/Archives/edgar/data/1120914/000143774926003948/ex_892634.htm). FY2023 revenue was $165.835M — [10-K, 24 Feb 2026](https://www.sec.gov/Archives/edgar/data/1120914/000143774926005366/pdfs20251231d_10k.htm)

**Change versus the background: no Analytics/IYR split any more**
- From the Q4-25 results onward the company stopped reporting "Analytics" and "Integrated Yield Ramp" (IYR = all fees from contracts with yield-based performance incentives). The new categories are Platform (software licences other than Cimetrix runtime, maintenance, SaaS, engineering services, CV fixed fees, DirectScan licences and purchases) and Volume-based (Cimetrix runtime licences, secureWISE data, Gainshare). No dollar reconciliation of old to new is given — [8-K, 12 Feb 2026](https://www.sec.gov/Archives/edgar/data/1120914/000143774926003948/ex_892634.htm). The last old-basis figure: "Analytics" was about 94% of TTM-Q3-25 revenue — [Quartr Investor Day 2025 summary](https://quartr.com/events/pdf-solutions-inc-pdfs-investor-day-2025_ofDusilh)

**Recurring share, backlog, RPO**
- Recurring revenue was 88% in Q3-26, 80% in Q2-26 and 95% in Q3-25; upfront revenue 12%, 20% and 5% — [Q3-26 management report, 5 Nov 2026](https://www.sec.gov/Archives/edgar/data/0001120914/000143774926035288/ex_1002247.htm). Over 9M-26, recurring was 86% (92% in 9M-25) — [10-Q Q3-26](https://www.sec.gov/Archives/edgar/data/1120914/000143774926035296/pdfs20260930_10q.htm)
- How "recurring" is defined: SaaS, "other services" and time-based licences, plus streams that "often recurred in the past": Cimetrix runtime licences, secureWISE data and Gainshare. Upfront = Exensio perpetual licences, certain CV test-chip designs, sales-type leases and hardware sales — [10-K FY2025](https://www.sec.gov/Archives/edgar/data/1120914/000143774926005366/pdfs20251231d_10k.htm)
- Remaining performance obligations about $247.2M at 30 Sep 2026; "the majority... expected to be recognized as revenue over the next two years". Deferred revenue $36.7M (from $20.3M at Dec-25); current contract assets $27.7M (from $11.3M); unbilled receivables $39.5M current and $7.6M non-current — [10-Q Q3-26](https://www.sec.gov/Archives/edgar/data/1120914/000143774926035296/pdfs20260930_10q.htm)
- On the backlog dip, management cited the timing of large deals and expects eight- and nine-figure renewals in Q4-26/Q1-27 to lift backlog above $271M by year-end. Earnings Whispers calculates this implies about $100M of net Q4 bookings and notes management conceded some deals may slip into 2027 — [Earnings Whispers via Finviz, 5 Nov 2026](https://finviz.com/news/418173/pdf-solutions-posts-record-revenue-and-margin-breakout-but-a-backlog-dip-and-slower-implied-q4-growth-temper-a-narrow-miss); [Q3-26 call transcript](https://www.earningswhispers.com/transcript/PDFS/Q32026)

**Cash, debt, secureWISE**
- 30 Sep 2026: cash $107.131M (from $42.220M at Dec-25); long-term debt $63.096M plus $2.237M current; equity $383.0M — [8-K Ex.99.1](https://www.sec.gov/Archives/edgar/data/0001120914/000143774926035288/ex_1002246.htm). Debt principal $66.25M. 9M-26 operating cash flow $31.8M; capex $39.7M (Q3 $15.1M); no buybacks in 9M-26; stock comp $8.5M in Q3 (12% of revenue) — [management report](https://www.sec.gov/Archives/edgar/data/0001120914/000143774926035288/ex_1002247.htm)
- Credit facilities dated 7 Mar 2025: $25M term loan plus $45M revolver (Wells Fargo agent), due Mar 2030, SOFR +2.00-2.75%, 2025 weighted rate 6.47%. Covenants: net leverage ≤3.0x and fixed-charge cover ≥1.25x. $69.6M of debt was used to fund secureWISE — [10-K FY2025](https://www.sec.gov/Archives/edgar/data/1120914/000143774926005366/pdfs20251231d_10k.htm). First Amendment dated 23 Apr 2026 — [10-Q](https://www.sec.gov/Archives/edgar/data/1120914/000143774926035296/pdfs20260930_10q.htm). The revolver had $30M unused after the post-Q1 expansion — [Q1-26 call, 7 May 2026](https://www.fool.com/earnings/call-transcripts/2026/05/07/pdf-solutions-pdfs-q1-2026-earnings-transcript/)
- secureWISE: bought from Telit IoT Solutions (agreement 19 Feb 2025, closed 7 Mar 2025) for $130.0M cash. Allocation: goodwill $80.0M, customer relationships $28.9M (13 years), developed technology $11.6M (7 years), trademark $6.6M — [10-Q Note 14](https://www.sec.gov/Archives/edgar/data/1120914/000143774926035296/R21.htm)
- May 2026 equity offering at $44.00/share: the company sold 1,946,630 shares including the full greenshoe (about $85.7M gross; $81.8M net). Advantest America sold 3,306,924 shares. Closed 15 May 2026 — [PDF release](https://www.pdf.com/resources/pdf-solutions-announces-full-exercise-of-greenshoe-option-and-closing-of-upsized-public-offering-of-common-stock/); [10-Q cash flow](https://www.sec.gov/Archives/edgar/data/1120914/000143774926035296/pdfs20260930_10q.htm)
- Free cash flow: FY2025 operating cash flow $24.1M against about $32.8M of PP&E purchases and prepayments, about -$8.7M (my calculation from the 10-K cash-flow statement); FY2024 about -$8.1M — [10-K FY2025](https://www.sec.gov/Archives/edgar/data/1120914/000143774926005366/pdfs20251231d_10k.htm). TTM FCF -$0.27M — [StockAnalysis, accessed 12 Nov 2026](https://stockanalysis.com/stocks/pdfs/statistics/). CFO on the Q3-26 call: positive FCF is "the right direction to think about for the whole year" — [transcript](https://www.earningswhispers.com/transcript/PDFS/Q32026)
- GAAP ROIC 5.04%, ROE 4.90%, TTM GAAP operating margin 9.2% — [StockAnalysis, 12 Nov 2026](https://stockanalysis.com/stocks/pdfs/statistics/)

**Concentration**
- Customers at ≥10% of revenue: A was 20% in Q3-26 (38% in Q3-25) and 23% in 9M-26; B was 26% in Q3-26 (12% in Q3-25) and 14% in 9M-26; C was below 10% (11% in 9M-25). Receivables: A 35% and C 22% at 30 Sep 2026. Customers are not named — [10-Q Note 10](https://www.sec.gov/Archives/edgar/data/1120914/000143774926035296/R17.htm)
- Three customers were 53% of FY2025 revenue (two were 31% of FY2024; one was 35% of FY2023). Two customers held 64% of gross receivables at Dec-25 — [10-K FY2025](https://www.sec.gov/Archives/edgar/data/1120914/000143774926005366/pdfs20251231d_10k.htm). On the Q1-26 call management said the top 20% of customers drive most bookings and equipment companies have entered the top five — [Q1-26 call](https://www.fool.com/earnings/call-transcripts/2026/05/07/pdf-solutions-pdfs-q1-2026-earnings-transcript/)
- Geography by billing address: Q3-26 US $22.7M (33%), Japan $21.7M (32%), China $11.1M (16%), rest of world $12.9M (19%), against Q3-25 US 53%, Japan 18%, China 10%. 9M-26: US 43%, Japan 19%, China 15%, rest of world 23% — [10-Q](https://www.sec.gov/Archives/edgar/data/1120914/000143774926035296/pdfs20260930_10q.htm). CEO: Japan was once 75% of revenue and the mix will "bounce around" — [transcript](https://www.earningswhispers.com/transcript/PDFS/Q32026)

**Advantest (change versus the background)**
- Advantest bought 3,306,924 shares for $65.2M in July 2020 and was a related party (>5%) until 15 May 2026, when the offering ended that status. The Exensio cloud subscription expired in July 2025; the development and commercialization agreements remain in effect. Revenue from Advantest: none in Q3-26 and $0.7M in 9M-26, against $8.5M in 9M-25 — [10-Q Note 13](https://www.sec.gov/Archives/edgar/data/1120914/000143774926035296/R20.htm). The 10-K also lists Advantest among competitors in connectivity — [10-K](https://www.sec.gov/Archives/edgar/data/1120914/000143774926005366/pdfs20251231d_10k.htm)

**Position and lead**
- Platform reach: 370+ customers, 100+ OEMs, 250+ fabs/OSATs and 20M weekly data logs (company claim, unconfirmed); "largest software deployment to date" with an unnamed customer standardising on Exensio and secureWISE — [Quartr Investor Day summary](https://quartr.com/events/pdf-solutions-inc-pdfs-investor-day-2025_ofDusilh)
- secureWISE is used by 100+ equipment vendors to reach tools in 190+ fabs (company claim at acquisition, unconfirmed) — [eeNews Europe, Feb 2025](https://www.eenewseurope.com/en/130m-deal-for-semiconductor-equipment-network). A later PDF page cites 300+ fabs, "tens of thousands of tools" and 8 data hubs (company claim, unconfirmed) — [pdf.com secureWISE page](https://www.pdf.com/securewise-balancing-security-and-access-in-semiconductor-manufacturing/)
- Intel "standardized on SecureWise" for front-end, test and assembly. The CEO says about nine months of outreach to equipment makers is now producing wins; pilots are running with OSATs, fabless firms and foundries — [Q3-26 call](https://www.earningswhispers.com/transcript/PDFS/Q32026); [Q1-26 call](https://www.fool.com/earnings/call-transcripts/2026/05/07/pdf-solutions-pdfs-q1-2026-earnings-transcript/). The source is an Intel speaker's keynote at PDF's own Users Conference (Dec 2025) as reproduced in PDF material; no Intel press release was found.
- Samsung "presented its use of E-Probe on an advanced node" at PDF CONNECT (15-16 Oct 2026), as reported by PDF management. Q3-26 also included an "eight-figure E-Probe and CV test-chip contract with an existing leading-edge customer" (unnamed) — [Earnings Whispers via Finviz](https://finviz.com/news/418173/pdf-solutions-posts-record-revenue-and-margin-breakout-but-a-backlog-dip-and-slower-implied-q4-growth-temper-a-narrow-miss)
- Competitors named in the 10-K. Yield management: KLA, Onto, Synopsys. Manufacturing software: Applied Materials, Synopsys, Invantest, Emerson, Onto, Siemens. Inspection/metrology/test: ASML, Applied, KLA, Keysight. Connectivity: PEER Group, Kontron AIS, Yokogawa, Advantest, Kornic, Tracces (Capgemini). Indirect: customers' in-house teams, Tableau, Spotfire, Snowflake, Databricks. Risk factor: customers may build in-house — [10-K](https://www.sec.gov/Archives/edgar/data/1120914/000143774926005366/pdfs20251231d_10k.htm)
- Partnerships: SAP collaboration since July 2022 (Sapience Manufacturing Hub links fab data to S/4HANA; Sapience Operational Product Costing integrates with S/4HANA) — [SAP partner page](https://www.sap.com/spain/products/scm/partners/pdf-solutions-inc-sapience-manufacturing-hub-smh.html); [10-K](https://www.sec.gov/Archives/edgar/data/1120914/000143774926005366/pdfs20251231d_10k.htm). Siemens Tessent YieldInsight was integrated into Exensio Manufacturing Analytics in Dec 2025 — [SemiWiki](https://semiwiki.com/eda/364906-pdf-solutions-ai-driven-collaboration-smarter-decisions). IBM, AWS, Oracle and Microsoft are listed as alliances — [Quartr](https://quartr.com/events/pdf-solutions-inc-pdfs-investor-day-2025_ofDusilh). No named 2025-26 SAP-linked customer was found.

**Revenue model and labour**
- Pricing in the 10-K. Cimetrix: one-time fee per equipment product type plus a one-time runtime fee per tool shipped. secureWISE: fees per connected tool and per data transferred. DirectScan: licence/lease or sale. CV: fixed fees plus variable royalties (Gainshare). Exensio: on-prem licence or SaaS. Engineering services are recognised over time — [10-K](https://www.sec.gov/Archives/edgar/data/1120914/000143774926005366/pdfs20251231d_10k.htm)
- Employees at 31 Dec 2025: 600, of whom 180 are field application engineers, 225 in R&D, 135 in sales and marketing and 60 in G&A — [10-K](https://www.sec.gov/Archives/edgar/data/1120914/000143774926005366/pdfs20251231d_10k.htm)
- eProbe is mostly on subscription: 6 machines at end-2025 (5 subscribed); plan for 6 shipments in 2026; about 12 installed by end-2026 — [Q1-26 call](https://www.fool.com/earnings/call-transcripts/2026/05/07/pdf-solutions-pdfs-q1-2026-earnings-transcript/). Q2-26: three placements, two at new customers, one a five-year subscription (from search-result summaries of [MarketBeat, 7 Aug 2026](https://www.marketbeat.com/instant-alerts/pdf-solutions-q2-earnings-call-highlights-2026-08-07/); page not read in full)
- Q3-26: a large secureWISE contract moved from volume-based to platform (subscription) revenue, with data volumes "locked in". The equipment business (Cimetrix plus secureWISE) is about 20% of total — [Q3-26 call](https://www.earningswhispers.com/transcript/PDFS/Q32026)

**Resilience and export controls**
- Cimetrix runtime licences track WFE; secureWISE tracks the installed base and "does not move as fast" but "doesn't go down as fast" (CFO). One more eProbe ships in Q4; more tools are planned for 2027 than 2026; a China placement is targeted "early next year" — [Q3-26 call](https://www.earningswhispers.com/transcript/PDFS/Q32026). Rising memory and component costs for eProbe compute — [Earnings Whispers](https://finviz.com/news/418173/pdf-solutions-posts-record-revenue-and-margin-breakout-but-a-backlog-dip-and-slower-implied-q4-growth-temper-a-narrow-miss)
- The 10-K says BIS Entity List rules restrict some sales and that BIS licence policy on renewals "led the company to decline certain renewals". On the Fall-2025 rule extending restrictions to 50%-owned affiliates: "BIS has suspended this rule until November 2026" — [10-K](https://www.sec.gov/Archives/edgar/data/1120914/000143774926005366/pdfs20251231d_10k.htm)
- SMIC New Technology R&D (Shanghai) stopped paying fees in 2019. HKIAC award in PDF's favour Nov 2025 and costs award Aug 2026; SMIC's set-aside application was heard Sep 2026 with no decision yet; nothing recognised — [10-Q Note 12](https://www.sec.gov/Archives/edgar/data/1120914/000143774926035296/R19.htm)

### Inferences
- Two customers made 46% of Q3-26 revenue. The Q3 jump in Customer B (12% to 26%) coincides with Japan revenue doubling, so B is probably Japan-billed (inference; unnamed).
- The thesis's "weakest" model (per-seat software, engineering hours) describes PDF only partly. 30% of headcount are FAEs and engineering services sit in Platform, but most revenue is multi-year subscriptions, per-tool tolls and Gainshare. The strongest-position test (owning the judge and the reference data) is met only by eProbe, which is small (about 12 tools), and PDF does not hold the customers' TEM/SEM reference data.
- GAAP returns are low (ROIC about 5%) because of stock comp (about 11-12% of revenue), acquisition amortisation and eProbe capex. The non-GAAP model (77/28) and the GAAP economics diverge sharply.

### Gaps
- Customer identities (A, B, C); secureWISE and Cimetrix revenue sizes; eProbe installed base at Q3-26; Advantest's residual holding (probably zero, since it sold the same number of shares it bought in 2020; not confirmed).

## Q2. PDF Solutions path through the six transitions (said versus done)

### Takeaway
PDF has shipped products for transitions 3 and 5 and an e-beam inference tool (1). It has a beta agent architecture (2), so that transition is said but not proven. On 4 it is a toll-taker on data flows rather than an owner of reference data, and it is moving partly into hardware. It is silent on 6, even though part of its revenue is priced per tool.

### Cited Findings
- **T2 (AI agents)**: Exensio Aurora was announced 9 Sep 2026: "customized LLM-enabled agents designed to assemble full workflows". Workflows "act as guardrails that ensure repeatability and prevent AI hallucination" (company claim, unconfirmed). Supports bring-your-own-model. Beta in Sep 2026 for "a small number of early adopters"; no GA date; no customers named. "Approximately 25X faster performance at comparable hardware cost" and "less than 5%" of fab data analysed with conventional tools are company claims, unconfirmed — [PDF release, 9 Sep 2026](https://www.pdf.com/resources/introducing-exensio-aurora-pdf-solutions-unveils-highly-scalable-architecture-for-exensio-analytics/)
- CEO on Q3-26: agents generate workflows as "Python code" engineers can review; feedback "mostly demo-related"; "the proof is in the pudding". Pricing intent: charge "a portion of that value, but not even all of it" — [Q3-26 call](https://www.earningswhispers.com/transcript/PDFS/Q32026). Q2-26: "everyone in the semiconductor supply chain will need to use AI agents" (search summary of [MarketBeat](https://www.marketbeat.com/instant-alerts/pdf-solutions-q2-earnings-call-highlights-2026-08-07/))
- The FY2025 highlights list "License of Tiber AI Studio code" (licensor and terms not given in the material read) — [8-K, 12 Feb 2026](https://www.sec.gov/Archives/edgar/data/1120914/000143774926003948/ex_892634.htm)
- **T5 (on-premises)**: Aurora offers "on-premise options where cloud-hosted solutions are not preferred"; models are trained centrally and deployed to "OSATs, test floors, and edge boxes"; built on Kubernetes — [PDF release](https://www.pdf.com/resources/introducing-exensio-aurora-pdf-solutions-unveils-highly-scalable-architecture-for-exensio-analytics/). CEO: customers moving from on-prem to cloud raised ARR 2-3x — [Q3-26 call](https://www.earningswhispers.com/transcript/PDFS/Q32026)
- **T1 (inference)**: AI in Exensio Characterization interprets CV test data and links signals to layout; AI links eProbe findings to design/process interactions (said, Q1-26) — [Q1-26 call](https://www.fool.com/earnings/call-transcripts/2026/05/07/pdf-solutions-pdfs-q1-2026-earnings-transcript/). eProbe applications: leading-edge logic, 28nm, a DRAM pilot and a flash evaluation; utilisation above 80-90% — [Q3-26 call](https://www.earningswhispers.com/transcript/PDFS/Q32026). PDF cites unnamed third-party estimates of an e-beam market "over $1 billion" — [Q1-26 call](https://www.fool.com/earnings/call-transcripts/2026/05/07/pdf-solutions-pdfs-q1-2026-earnings-transcript/)
- **T3 (packaging)**: Exensio has Test and Assembly Operations modules — [10-K](https://www.sec.gov/Archives/edgar/data/1120914/000143774926005366/pdfs20251231d_10k.htm). Q1-26 included a double-digit-million Exensio Test Operations booking and an enterprise-wide Exensio Test rollout at a large IDM — [Q1-26 call](https://www.fool.com/earnings/call-transcripts/2026/05/07/pdf-solutions-pdfs-q1-2026-earnings-transcript/). The secureWISE deal was meant to expand the "DEX" OSAT network — [10-Q Note 14](https://www.sec.gov/Archives/edgar/data/1120914/000143774926035296/R21.htm). PDF's Ken Harris: chiplet assembly is "a massive data explosion" — [SemiEngineering, 9 Jun 2026](https://semiengineering.com/ai-models-transform-defect-inspection-and-review-but-can-fail-to-scale/)
- **T4 (data)**: PDF anonymises data during cleaning: "We are actually cleaning the data, and that is where we anonymize it" (Ranjan Chatterjee, PDF) — [SemiEngineering, 13 Jan 2026](https://semiengineering.com/secure-data-sharing-becoming-critical-for-chip-manufacturing/). Long-lived assets of $121.5M are booked in the US but "include assets deployed at customer sites" (i.e. PDF-owned eProbe tools) — [10-Q Note 10](https://www.sec.gov/Archives/edgar/data/1120914/000143774926035296/R17.htm)
- **T6**: no PDF statement found.

### Inferences
- The Aurora agents build analytics workflows and would compete with customers' internal data-science work and generic platforms (Databricks, Snowflake). They do not build measurement-tool recipes, so PDF's T2 bet is "agents replace analysts", not "agents replace metrology applications engineers".
- A fall in tools per wafer (T6) would cut Cimetrix runtime fees (per tool shipped) and secureWISE per-tool fees. Analytics could gain if inference replaces measurement.

### Gaps
- Aurora early-adopter names, measured outcomes, GA and pricing; whether any Exensio deployment runs LLM agents fully inside a fab. "Test model operations with Advantest": no 2025-26 source found.

## Q3. PDF Solutions entry-point data (kept separate from quality)

### Takeaway
At $41.79 (11 Nov 2026), PDFS trades at about 7x EV/TTM sales, 108x trailing GAAP earnings and 27x forward earnings, 27% below its 6 Oct 2026 high and 5% below the May 2026 offering price. The 20% growth guide implies Q4 deceleration to about 17%.

### Cited Findings
- Price $41.79 at close 11 Nov 2026 (+6.7% on the day); pre-market $41.08 on 12 Nov. Market cap $1.77B; EV $1.73B; 42.25M shares. Trailing P/E 108.54; forward P/E 26.99; P/S 7.00; EV/sales 6.86; EV/EBITDA 49.89. Net cash $33.5M (cash $107.1M less total debt including leases, $73.6M). Beta 1.79. Short interest 7.83% of shares. Insiders 10.48%; institutions 95.03%. Average analyst target $56.25 ("Buy", 8 analysts). 52-week change +54% — [StockAnalysis, accessed 12 Nov 2026](https://stockanalysis.com/stocks/pdfs/statistics/)
- My calculation: TTM non-GAAP EPS = Q4-25 $0.30 + 9M-26 $0.99 = $1.29, about 32x at $41.79 (sources: the two 8-Ks above).
- Before the Q3 report the stock was $39.79; Oct-26 high $56.98 (6 Oct) and low $38.63 (23 Oct). Q3 consensus was revenue $68.76M (actual $68.33M, -0.6%) and EPS $0.21 (versus Earnings Whispers' own measure of $0.20; the company reported $0.40 non-GAAP) — [Earnings Whispers via Finviz, 5 Nov 2026](https://finviz.com/news/418173/pdf-solutions-posts-record-revenue-and-margin-breakout-but-a-backlog-dip-and-slower-implied-q4-growth-temper-a-narrow-miss)
- Earlier marks: offering priced at $44.00 (13-14 May 2026) — [PDF release](https://www.pdf.com/resources/pdf-solutions-announces-pricing-of-an-upsized-public-offering-of-common-stock/); close $50.98 and market cap $2.13B on 24 Jul 2026 (Motley Fool quote page, from search result) — [Fool](https://www.fool.com/quote/nasdaq/pdf-solutions/pdfs)
- Guidance: 2026 revenue growth "consistent with" the 20% long-term target, reaffirmed 5 Nov 2026. That implies Q4 about $73M (about 17% y/y; CFO said the analyst was "in the right direction"). Q4 gross margin between 75% and 77%. Long-term model: 20% growth, >77% gross margin, >27% operating margin (set at Investor Day, Dec 2025; the operating target was raised from 20%) — [Q3-26 call](https://www.earningswhispers.com/transcript/PDFS/Q32026); [Quartr](https://quartr.com/events/pdf-solutions-inc-pdfs-investor-day-2025_ofDusilh). 2027: no guidance; CEO sees nothing pointing below typical targets.
- Near-term events: Q4/FY2026 results (FY2025 was reported on 12 Feb 2026, so expect about mid-Feb 2027; date not announced); Q4/Q1 renewals expected to lift backlog above $271M; the BIS affiliates-rule suspension ends in Nov 2026; SMIC set-aside decision; first eProbe in China "early next year"; Aurora GA (undated).

### Gaps
- The company's own 5-10 year P/E and EV/sales range and consensus 2027 growth [INCOMPLETE].

## Q4. Field scan: who sells measurement and yield software, and how they charge [INCOMPLETE]

### Takeaway (provisional)
Tool makers mostly bundle measurement software with hardware or sell it as one-off licences: Nova recognises software licences "at a point in time" and does not split them out. Independents sell analytics as subscriptions or on-site deployments. Separately priced, usage- or outcome-based software revenue is visible mainly at PDF (Gainshare, secureWISE). Sizes for most private players could not be verified.

### Cited Findings
- **Nova (Israel)**: software portfolio Nova MARS (physical modelling), Nova FIT (ML), Nova HPC and Nova FM (fleet management), coupled to OCD, XPS/XRF (VeraFlex), SIMS (Metrion) and Raman (Elipson) tools. Risk factor: AI "may change the balance between hardware capabilities and software or algorithms needs". Revenue recognition: "Revenue from software licenses is recognized at a point in time"; also earns "labor hours". FY2025 product revenue $705.6M and services $175.0M (services 22% of revenue) — [Nova 20-F FY2025, filed 17 Feb 2026](https://www.sec.gov/Archives/edgar/data/1109345/000117891326000504/0001178913-26-000504-index.htm)
- **Gauss Labs (US/Korea)**: Panoptes VM and Panoptes IM, deployed "in your environment to satisfy security compliance and avoid IP issues". Named customer/partner: SK hynix (in production since Dec 2022) — [gausslabs.ai](https://www.gausslabs.ai/); [VM page](https://www.gausslabs.ai/vm). Pricing not disclosed.
- **Athinia**: a secure collaboration platform on Palantir Foundry for device makers, material suppliers and equipment suppliers. Data owners set who receives data, for what use and for how long; it can "obfuscate and statistically normalize" data. No customers or pricing on the site — [athinia.com](https://www.athinia.com/). SemiEngineering describes it as a Merck-Palantir hub — [13 Jan 2026](https://semiengineering.com/secure-data-sharing-becoming-critical-for-chip-manufacturing/)
- **Others in the data-sharing debate** (Jan 2026): Synopsys SLM (Randy Fish), proteanTecs ("Models trained in the cloud are deployed at the tester"), Advantest ACS (data across test insertions), Teradyne Smart Manufacturing, Onto enterprise software, and NI SystemLink as a secure environment — [SemiEngineering, 13 Jan 2026](https://semiengineering.com/secure-data-sharing-becoming-critical-for-chip-manufacturing/)
- **Advantest ACS RTDI** (launched 12 Dec 2023) is a real-time data infrastructure with third-party analytics partners including PDF — [Advantest](https://www.advantest.com/en/news/2023/20231212.html)
- **Cohu**: Jon Herlocker is VP/GM of software analytics at Cohu (SemiEngineering tags these interviews "Tignis") — [SemiEngineering, 19 Sep 2025](https://semiengineering.com/virtual-metrology-in-semiconductor-manufacturing/)
- **Nordson Test & Inspection**: a generic X-ray bump-void model trained on pooled data from many customers, "90% accuracy" (company claim, unconfirmed) — [SemiEngineering, 9 Jun 2026](https://semiengineering.com/ai-models-transform-defect-inspection-and-review-but-can-fail-to-scale/)

### Gaps
- [INCOMPLETE] Sizes, adoption and pricing for KLA, Applied, Onto, ASML, Advantest and Teradyne software; Synopsys SLM and yield; Siemens; Emerson/NI; INFICON; proteanTecs; Lynceus; yieldHUB; DR Yield; Tignis; SandBox; Robovision; SixSense; Averroes; Semitronix; others in Japan, Korea, Taiwan and India.

## Q5. Prior A: agents make recipe set-up at least 5x faster at leading users by 2028 [INCOMPLETE]

### Takeaway (provisional)
No 2025-26 source read so far gives a measured speed-up in metrology or inspection recipe set-up from agents, by any measurer. Agent products are at beta or demo stage in manufacturing analytics.

### Cited Findings
- PDF Aurora agents: beta Sep 2026; feedback "mostly demo-related" (Nov 2026) — [PDF release](https://www.pdf.com/resources/introducing-exensio-aurora-pdf-solutions-unveils-highly-scalable-architecture-for-exensio-analytics/); [Q3-26 call](https://www.earningswhispers.com/transcript/PDFS/Q32026)
- Cohu's Herlocker calls agentic AI "the real game changer for AI in chip manufacturing" but gives no measured gains — [SemiEngineering, 28 Jan 2026](https://semiengineering.com/agentic-ai-in-chip-manufacturing/)
- Nordson: manual parameter addition is "tedious, time-consuming", and prompting such as "locate all the RDL" could "eliminate a lot of programming needs" (qualitative). PDF estimates "over 70%" of AI initiatives stall after pilots — [SemiEngineering, 9 Jun 2026](https://semiengineering.com/ai-models-transform-defect-inspection-and-review-but-can-fail-to-scale/)
- In chip design (not measurement), Synopsys markets AgentEngineer, moving from copilots to agents that execute full workflows — [SemiEngineering, 29 Oct 2026](https://semiengineering.com/long-horizon-agents-autonomous-engineering-from-silicon-to-systems/)

### Gaps
- [INCOMPLETE] Tool-maker agent or recipe-automation announcements with measured times; chipmaker papers.

## Q6. Prior B: combining signal types becomes standard for nanosheet devices [INCOMPLETE]

### Cited Findings
- Onto's Nick Keller: "Hybrid ML/physics models are superior to ML only because they are inherently more robust". Onto's Woo Young Han: AI can infer dimensions and overlay "from noisy or incomplete optical signals" — [SemiEngineering, 9 Jun 2026](https://semiengineering.com/ai-models-transform-defect-inspection-and-review-but-can-fail-to-scale/)
- Nova's strategy lists "Machine learning and AI capabilities to complement physical modeling" across dimensional, X-ray and SIMS metrology — [Nova 20-F](https://www.sec.gov/Archives/edgar/data/1109345/000117891326000504/0001178913-26-000504-index.htm)
- Multi-layer nanosheets push metrology "toward hybrid approaches" — [SemiEngineering, 9 Aug 2022](https://semiengineering.com/nanosheet-fets-drive-changes-in-metrology-and-inspection/)

### Gaps
- [INCOMPLETE] IBM Research, imec and chipmaker papers; SPIE AL 2026 fusion papers. SPIE Digital Library pages were not machine-readable (bot protection).

## Q7. Prior C: learned noise removal is safe for measuring the expected and risky for detecting the unexpected [INCOMPLETE]

### Cited Findings
- SK hynix and Gauss Labs: "Universal denoiser to improve metrology throughput" (SPIE AL 2024, vol. 12955) applies learned denoising to measurement throughput — [SPIE listing](https://www.spiedigitallibrary.org/conference-proceedings-of-spie/12955/1295536/Universal-denoiser-to-improve-metrology-throughput/10.1117/12.3010773.short) (title and venue only; abstract not read)
- Inspection AI depends on rare-defect data: "Because semiconductor wafer defects are generally rare, they are difficult to gather" (Microtronic). "Many datasets we got from our customers are biased" (Nordson). Synthetic data is "often essential". The article does not discuss hallucination risk — [SemiEngineering, 9 Jun 2026](https://semiengineering.com/ai-models-transform-defect-inspection-and-review-but-can-fail-to-scale/)

### Gaps
- [INCOMPLETE] Direct literature on hallucination in denoised SEM for inspection; vendor safeguards.

## Q8. Prior D: tools per wafer may fall after 2030 as inference replaces some measurement

### Takeaway
VM is in production (SK hynix since 2022) and vendors claim near-full virtual coverage. But the published uses complement physical metrology (APC, tool matching, anomaly detection), and no source quantifies a cut in physical sampling or tool purchases.

### Cited Findings
- Gauss Labs claims Panoptes VM runs "hundreds of thousands of models"; SK hynix deployment Dec 2022; "29% of process variability improvement" (company claim, unconfirmed) — [VM page](https://www.gausslabs.ai/vm). A Korean press report (Donga, 9 Feb 2026, as listed by Gauss) describes near-100% wafer coverage at one wafer per second versus 1-5% physical sampling and a 15% variation reduction, saying it removes "the need for costly, time-intensive physical measurements" (company-supplied figures) — [Gauss Labs news](https://www.gausslabs.ai/news)
- SK hynix's SPIE AL 2026 papers with Gauss cover VM-driven tool-to-tool matching (VM reveals tool differences hidden by "low sampling rates") and GRACE explainability for overlay VM, in production since 2025 — [SK hynix newsroom, 19 Feb 2026](https://news.skhynix.com/sk-hynix-and-gauss-labs-present-ai-based-semiconductor-virtual-metrology-research-at-spie-al-2026/)
- Against: VM "may never be 100% perfect" and will never completely replace metrology tools (Cohu) — [SemiEngineering, 19 Sep 2025](https://semiengineering.com/virtual-metrology-in-semiconductor-manufacturing/). ASU and Intel Foundry frame VM as an alternative where physical measurement is "limited" by latency, cost and sampling, with no reduction quantified — [SemiEngineering, 2 Jun 2026](https://semiengineering.com/using-graph-attention-for-virtual-metrology-in-semiconductor-manufacturing-asu-intel-foundry/) ([arXiv 2606.00923](https://arxiv.org/abs/2606.00923))
- The NIST/NSF workshop (2023-25) found that "training data from similar operations at different factories led to more robust modeling" in a VM use case — [NIST, Nov 2025](https://www.nist.gov/publications/artificial-intelligence-open-and-scaled-data-sharing-semiconductor-manufacturing)

### Gaps
- Measured before/after physical sampling rates at any fab; chipmaker statements on metrology tool counts.

## Q9. Open question: who ends up owning the reference data and the value? [INCOMPLETE]

### Cited Findings
- Data hierarchy: "It's tough to get device and process data out"; device data is most protected, process data second, equipment-health data least. "A lot of other people are treating ML models as trade secrets" (Eli Roth, Teradyne). "The level of data sharing amongst different parties is typically decided at the contractual stage" (Randy Fish, Synopsys). Standards "typically have a hard time keeping pace" — [SemiEngineering, 13 Jan 2026](https://semiengineering.com/secure-data-sharing-becoming-critical-for-chip-manufacturing/)
- Pooling by vendors: Nordson trained one model on bump data from many customers — [SemiEngineering, 9 Jun 2026](https://semiengineering.com/ai-models-transform-defect-inspection-and-review-but-can-fail-to-scale/). The NIST/NSF coalition showed competing manufacturers could agree a sharing process (Seagate/UCLA processing) — [NIST](https://www.nist.gov/publications/artificial-intelligence-open-and-scaled-data-sharing-semiconductor-manufacturing)
- On-site: Gauss deploys "in your environment... avoid IP issues"; PDF Aurora has an on-prem option; proteanTecs trains in the cloud and deploys at the tester (sources above).
- In-house plus captive start-up: SK hynix's AI Core Technology Team, SYLD Tech Team and Photo Technology Strategy Team co-author with Gauss — [SK hynix newsroom](https://news.skhynix.com/sk-hynix-and-gauss-labs-present-ai-based-semiconductor-virtual-metrology-research-at-spie-al-2026/). Gauss Labs blog title: "Build vs. Buy: The Real Question Behind Virtual Metrology" (18 Jun 2026) — [Gauss news](https://www.gausslabs.ai/news)

### Gaps
- [INCOMPLETE] TSMC, Samsung, Intel and Micron in-house measurement AI; SEMI standards (E187/E188, Smart Data-AI); separately priced measurement-AI revenue at tool makers.

## Could not verify (interim)
- PDFS: Customer A/B/C identities; Advantest residual stake (likely zero); secureWISE, Cimetrix and eProbe revenue; third-party market share; independent confirmation of Intel's secureWISE standardisation and of Samsung's eProbe use; Tiber AI Studio licensor and terms; "test model operations" with Advantest; Aurora customers, pricing and GA; own 5-10 year valuation range; consensus 2027 growth.
- Priors and field scan: see the [INCOMPLETE] markers.

## Sources (with dates)
- PDF Solutions Q3-26 press release, 5 Nov 2026: https://www.sec.gov/Archives/edgar/data/0001120914/000143774926035288/ex_1002246.htm
- PDF Solutions Q3-26 management report, 5 Nov 2026: https://www.sec.gov/Archives/edgar/data/0001120914/000143774926035288/ex_1002247.htm
- PDF Solutions 10-Q Q3-26, filed 5 Nov 2026: https://www.sec.gov/Archives/edgar/data/1120914/000143774926035296/pdfs20260930_10q.htm (Notes: R17, R18, R19, R20, R21)
- PDF Solutions FY2025 results, 12 Feb 2026: https://www.sec.gov/Archives/edgar/data/1120914/000143774926003948/ex_892634.htm
- PDF Solutions 10-K FY2025, filed 24 Feb 2026: https://www.sec.gov/Archives/edgar/data/1120914/000143774926005366/pdfs20251231d_10k.htm
- Q3-26 call transcript, 5 Nov 2026: https://www.earningswhispers.com/transcript/PDFS/Q32026
- Earnings Whispers via Finviz, 5 Nov 2026: https://finviz.com/news/418173/pdf-solutions-posts-record-revenue-and-margin-breakout-but-a-backlog-dip-and-slower-implied-q4-growth-temper-a-narrow-miss
- Q1-26 call transcript, 7 May 2026: https://www.fool.com/earnings/call-transcripts/2026/05/07/pdf-solutions-pdfs-q1-2026-earnings-transcript/
- Q2-26 call highlights, 7 Aug 2026 (search summary only): https://www.marketbeat.com/instant-alerts/pdf-solutions-q2-earnings-call-highlights-2026-08-07/
- Investor Day 2025 summary (Quartr, page dated 8 Jul 2026): https://quartr.com/events/pdf-solutions-inc-pdfs-investor-day-2025_ofDusilh
- Offering releases, 13-15 May 2026: https://www.pdf.com/resources/pdf-solutions-announces-pricing-of-an-upsized-public-offering-of-common-stock/ and https://www.pdf.com/resources/pdf-solutions-announces-full-exercise-of-greenshoe-option-and-closing-of-upsized-public-offering-of-common-stock/
- Exensio Aurora release, 9 Sep 2026: https://www.pdf.com/resources/introducing-exensio-aurora-pdf-solutions-unveils-highly-scalable-architecture-for-exensio-analytics/
- StockAnalysis PDFS statistics, accessed 12 Nov 2026: https://stockanalysis.com/stocks/pdfs/statistics/
- eeNews Europe, Feb 2025: https://www.eenewseurope.com/en/130m-deal-for-semiconductor-equipment-network
- SemiEngineering, 13 Jan 2026: https://semiengineering.com/secure-data-sharing-becoming-critical-for-chip-manufacturing/
- SemiEngineering, 9 Jun 2026: https://semiengineering.com/ai-models-transform-defect-inspection-and-review-but-can-fail-to-scale/
- SemiEngineering, 28 Jan 2026: https://semiengineering.com/agentic-ai-in-chip-manufacturing/
- SemiEngineering, 19 Sep 2025: https://semiengineering.com/virtual-metrology-in-semiconductor-manufacturing/
- SemiEngineering, 2 Jun 2026: https://semiengineering.com/using-graph-attention-for-virtual-metrology-in-semiconductor-manufacturing-asu-intel-foundry/
- NIST workshop report, Nov 2025: https://www.nist.gov/publications/artificial-intelligence-open-and-scaled-data-sharing-semiconductor-manufacturing
- SK hynix newsroom, 19 Feb 2026: https://news.skhynix.com/sk-hynix-and-gauss-labs-present-ai-based-semiconductor-virtual-metrology-research-at-spie-al-2026/
- Gauss Labs site, VM page and news (accessed 12 Nov 2026): https://www.gausslabs.ai/ ; https://www.gausslabs.ai/vm ; https://www.gausslabs.ai/news
- Athinia site (accessed 12 Nov 2026): https://www.athinia.com/
- Nova 20-F FY2025, filed 17 Feb 2026: https://www.sec.gov/Archives/edgar/data/1109345/000117891326000504/0001178913-26-000504-index.htm
