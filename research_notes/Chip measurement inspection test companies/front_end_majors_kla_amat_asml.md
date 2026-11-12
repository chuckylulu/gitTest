# Front-end process-control majors: KLA, Applied Materials (process diagnostics & control), ASML (metrology & inspection)

**Research date: 12 November 2026.** Final version (written after an interruption; gaps that remain are in §4).

Conventions: "co. claim" = company statement no outside party has confirmed. "derived" = my arithmetic from cited figures. "secondary" = press, aggregator or AI-generated summary, not a filing. Tags [K..] KLA, [A..] Applied Materials (AMAT), [M..] ASML, [X..] third party, [E..] market data; all map to §5. KLA fiscal year ends 30 Jun (Q1 FY27 = Jul-Sep 2026); KLA per-share data are after the 10-for-1 split of 11 Jun 2026 [K2]. AMAT Q3 FY26 ended 26 Jul 2026. ASML Q3 2026 ended 27 Sep 2026.

Latest-period status: KLA Q1 FY27 published 28 Oct 2026 [K1]. ASML Q3 2026 published 14 Oct 2026 [M1]. **AMAT Q4 FY26 is due after the US close on 12 Nov 2026 (call 4:30 pm ET) and was not available when these notes were compiled** (no release found by search; newest AMAT 8-K on EDGAR dated 26 Oct 2026) [A9]. AMAT figures therefore use Q3 FY26 plus Q4 guidance.

## 1. Quality evidence tables

### 1.1 KLA

| Item | Evidence |
|---|---|
| (a) Position | Sells the inspection and metrology measurements fabs use to gate wafers: FY26 Wafer Inspection $6.63B (49% of revenue), Patterning (metrology + reticle inspection) $2.71B (20%) [K3]; Q1 FY27 51% and 21% [K8]. 1,500 applications engineers decide sampling per fab ("It's a competitive advantage for us") [K10]. Data platform is open and vendor-agnostic: "we will take competitors' data also"; "Customer can write their own algorithms" [K12]. Reference data: no evidence KLA holds customers' TEM cross-sections; its own e-beam is used to set up optical tools [K10]. Named tool-of-record wins: could not verify. |
| (b) Lead | Third party: 73.8% of 2025 metrology & inspection (72.6% in 2024); AMAT next at 9.8% (The Information Network) [X1]. Co. claims (Investor Day, 12 Mar 2026): 56.5% of process control, +2 pts since 2021, "6.5x versus the nearest competitor"; e-beam revenue ~$400M vs $75-100M earlier; advanced packaging (AP) from ~10% share and "number four" in 2020 to number one [K10][K12]. AP process control growing "nearly twice the growth rate of the advanced packaging market" (co. claim) [K8]. No Gartner/TechInsights/Yole sub-segment data found. |
| (c) Revenue model | Service $3.13B = 23% of FY26 (+16%) [K3]; $850M = 20% of Q1 FY27 (+14%) [K8]. Over 80% of service revenue on multi-year (>3 yr) contracts (60% in 2005); >57,000 installed tools; each tool earns revenue "95% of the time" over two years; median tool retirement >24 years; service model 13-15%/yr growth (co. claims) [K11]. Software & data analytics ~"$250 million" (co. claim) [K10]. Labour: 1,500 applications engineers [K10]; >3,500 service engineers [K11]; "70% of our OpEx is technical investments. It's R&D or apps." [K9]. Applications work is bundled into tool sales, not billed separately (no disclosure found). |
| (d) Financial strength | FY26 GAAP gross margin 61.3% [K3]; GAAP op. margin ~41.7% (derived) [K2]; FCF $3.77B = 27.7% of revenue (derived) [K2]. Q1 FY27 non-GAAP GM 62.7%, non-GAAP op. margin 46.1% (a record) [K8]. FY26 capital returns $3.35B (~89% of FCF, derived) [K2]; target >90% of FCF [K9]. Debt $5.95B vs cash + securities $4.7B (30 Sep 2026) [K8]; ratings A / A2 / A- [K3]. ROIC 69% (stockanalysis calc.) [E1]. TSMC the only >10% customer, FY24-26 [K3] (19% in FY26, secondary [X5]). China 29.8% of FY26 revenue (33.3% FY25, 43% FY24) [K3]; 34% in Q1 FY27; "high-20s" % expected for CY2026 [K8]; "low-20s" in 2027 (secondary) [X6]. |
| (e) Resilience | Backlog $12.57B at 30 Jun 2026 vs $7.86B [K3]. WFE "mid-$150 billion" in CY2026, ">$200 billion" in CY2027 [K8]; memory ~40% of semi process-control systems in the Dec-2026 quarter vs 28% in Sep [K8]. 2030 model assumes WFE (incl. packaging) ~$215B +/- $20B [K9][K13]. 10-K: sustainability of elevated AI capex "cannot be assured" [K3]. Affiliates Rule suspension extended to 10 Jan 2027 [X16]; China-bound products "held up by U.S. Customs and Border Protection" [K3]. DRAM cost for on-tool image computers weighs on gross margin [K3][K8]. |
| T1 imaging -> inference | X-ray (Axion) and optical CD (SpectraShape) in portfolio [K3]; buried 3D defects: Gen4 optical "can penetrate, but Electron Beam helps" [K10]. Sceptical of inference replacing sensors: "Hybrid metrology 10 years ago was going to just take over everything but nothing. It doesn't work. You need sensors on the problem." [K12]. Products with a published measurement uncertainty: could not verify. |
| T2 AI-built recipes | E-beam "provides intelligence for the setup of our Gen 4 and Gen 5 system" [K10]; AI algorithms in products since 2018, now on GPUs [K13]; models re-used across product lines (e-beam -> packaging) [K10]; predictive tool health and "autonomous synchronization" in service [K11]. No evidence AI-built recipes are reducing paid applications work. |
| T3 bonded stacks/packaging | AP process control ~$635M (2025) -> ~$1.1B (2026), >70% growth [K6][K8]; broader AP revenue "950 million" in 2025 [K10]; "a whole suite of systems for hybrid bonding" (co. claim) [K10]; AP service revenue ~8x 2022-25 [K11]; die-to-wafer traceability software for AP (co. claim) [K12]. Customer qualifications: could not verify. |
| T4 HW -> software/data | Services 20-23% plus ~$250M software [K3][K10]; open data platform [K12]. Access to customers' reference data: not evidenced. |
| T5 on-premise AI | Already in the tool: a bright-field system captures "78 trillion pixels of images in an hour", data "we cannot store" [K10]; "we have to process it locally" [K12]; on-tool compute about $1M of cost in one product [K13]. |
| T6 tools per wafer | 10-K risk: customers may cut "inspection and metrology sampling rates"; AI may "accelerate vertical integration or insourcing by customers" [K3]. Mgmt: "Sampling in general is going up"; overlay points per wafer ~250 -> ">3,000" on many layers [K10]; process control 5.3% -> 7.4% of WFE, ~9% assumed for 2030 [K10]. |

### 1.2 Applied Materials - process diagnostics & control (PDC) unit and parent

| Item | Evidence |
|---|---|
| Unit size | PDC revenue NOT disclosed. Estimate ~$1.26B in 2025 (derived: 9.8% x $12.9B metrology & inspection market) [X1]. Co.: cold-field-emission (CFE) e-beam revenue to "double to more than $1.0 billion in calendar 2026" (Q1 FY26 call, Feb 2026) [A10]; PDC to grow ">50% in calendar 2026" (13 Aug 2026) [A5]. Implied CY2026 PDC >= ~$1.9B, ~5.5% of FY26 parent revenue (~$34.3B = 9M $24.04B + Q4 guide $10.25B) (derived). |
| Products (verified this session) | VeritySEM 7AP (CD e-beam metrology for thick, warped HBM/chiplet substrates) and SEMVision G7AP (packaging defect review), launched around Q3 FY26 [A7]; VeritySEM 10, "2x better resolution ... at lower landing energies" (unattributed claim) [A11]. |
| (a) Position | 10-K: "Our process control systems employ optical and eBeam technologies that allow customers to inspect and review critical semiconductor architectures" [A3]. Strength in e-beam review/metrology; optical inspection far behind KLA (overall share 9.8%) [X1]. Reference data: not evidenced. |
| (b) Lead | CFE e-beam (>$1B in CY26, co.) looks larger than KLA's e-beam (~$400M, co.) - scopes differ (derived) [A10][K10]. Dec 2022 co. claim of "number-one supplier of eBeam systems" with >50% share, disputed by The Information Network [X2]. Third-party M&I share 11.1% -> 9.8% (2024 -> 2025) [X1]. Mgmt expects share gains "across deposition, conductor etch, and eBeam" (Feb 2026) [A10]. |
| (c) Revenue model (parent) | AGS (services) $1.78B = 19.5% of Q3 FY26 revenue (+22%) [A1]; shift of services/spares to subscriptions [A3]; AIx connected chambers >30,000 (Feb 2026) -> >37,000 (Aug 2026) [A10][A7]. PDC services/software: not disclosed. |
| (d) Financials (parent) | Q3 FY26 revenue $9.12B (+25%), non-GAAP GM 50.4%, non-GAAP op. margin 34.0% [A1]; 9M FCF $3.58B [A1]; net cash ~$7.96B (cash + investments $14.50B, debt $6.54B) [A1][A2]. FY25: two customers ~19% and ~15% (unnamed) [A3]. China 28% of Q3 FY26 revenue (~27% Q2; 30% FY25; 37% FY24) [A1][A11][A3]. ROIC 35.6% (stockanalysis calc.) [E2]. |
| (e) Resilience | Q4 FY26 guide $10.25B +/- $0.5B [A1]; "another strong growth year ... in 2027" [A1]; preparing to double quarterly system output by 2028 [A7]. Export controls: ~$600M FY26 revenue hit expected (co., via LongYield) [A11]; $252.5M BIS settlement 11 Feb 2026 [A4] ($253M "Legal settlement" in 9M opex [A2]); Affiliates Rule suspension to 10 Jan 2027 [X16]. |
| T1 | Leading logic/DRAM need more e-beam steps with "sub-nanometer resolution for high-aspect-ratio structures" (13 Aug 2026 remarks; search snippet) [A8]. |
| T2, T4-T6 | No PDC-specific evidence on AI recipes, software revenue, on-premise AI or tools per wafer (AIx covers process chambers). |
| T3 | Packaging metrology/review tools above [A7]; total packaging revenue >70% growth CY2026 (co.) [A5]; raising stake in Besi (hybrid bonding) to ~20% (26 Oct 2026) [A12]. |

### 1.3 ASML - metrology & inspection (M&I) unit and parent

| Item | Evidence |
|---|---|
| Unit size | M&I net system sales EUR 824.6M (208 units) 2025; 645.5M (165) 2024; 536.1M (151) 2023 [M2]. = 2.5% of 2025 total sales, 3.4% of system sales; +27.7% in 2025; ~EUR 4.0M per unit (derived). 2026 M&I not disclosed in quarterly materials [M1][M3][M4]. |
| Products | YieldStar optical (diffraction) metrology: 550B shipped Q3 2026 for 14-angstrom logic and 1D DRAM, ">60%" more productive (co. claim; several press reports) [X7][X15]. HMI e-beam: single-beam; multibeam eScan1000 (9 beams, shipped May 2020) and eScan1100 (25 beams, first installed Apr 2022, "up to 15 times" single-beam throughput, co.) [X13]; R&D on "e-beam inspection, e-beam metrology and YieldStar optical metrology" and the "multibeam inspection roadmap" [M2]. |
| (a) Position | YieldStar sits inside the lithography control loop; parent owns the physical constraint (~94% of 2025 lithography, JPMorgan est. via Reuters) [X4]. Reference data: not evidenced. |
| (b) Lead | No third-party M&I share found; ASML gained served-market share in 2025 (Information Network) [X2]. YieldStar demand to "more than double" vs 2025 - single AI-generated summary, could not verify [X7]. Multibeam customer adoption in 2026: could not verify. |
| (c) Revenue model (parent) | Installed Base Management (service + upgrades) EUR 8.19B = 25.1% of 2025 sales (+26.2%) [M2]; 28.2% of Q3 2026 sales [M3]. |
| (d) Financials (parent) | 2025: sales EUR 32.67B (+15.6%), GM 52.8%, op. margin 34.6%, net income EUR 9.61B, FCF EUR 11.03B [M2]. Q3 2026: sales EUR 11.66B, GM 57.5%, op. margin 44.4%, net income EUR 4.96B incl. EUR 509.7M equity-investment gain [M3]. Cash + short-term investments EUR 12.74B, long-term debt EUR 1.96B [M3]. Four customers >10% = 61.2% of 2025 sales [M2]. China 29.1% of 2025 sales [M2]; 14% -> 23% of system sales Q2 -> Q3 2026 (secondary) [X8]; ~20% of 2026 (CFO, secondary) [X8]. ROIC 92% (stockanalysis calc.) [E3]. |
| (e) Resilience | Backlog EUR 46.5B at end-2025, 65% within 12 months [M2]; non-current contract liabilities EUR 3.57B -> 9.30B in Q3 2026 (prepayments) [M3]; 2027-28 supply "will not fully meet the demand" [M1]; 2026 guide EUR 44-45B vs initial EUR 34-39B [M1][M2]. Dutch national licence requirement for M&I tools (Jan 2025) [X9]; Dutch government opposing US MATCH Act on servicing in China (May 2026) [X10]. |
| T1 | Plan to "extend holistic lithography into supporting 3D front end integration" [M2]. |
| T2 | Mistral AI: ~11% stake for EUR 1.3B (Sep 2025) [M2][X11]; CFO: AI models "can drive the performance of our lithography, metrology and inspection systems" [M2]; ~EUR 0.5B revaluation gain Q3 2026 [M3][X7]. No AI-recipe evidence. |
| T3-T6 | Packaging spend is lithography (XT:260) [M2]; "continuously expanding our investment in the holistic software applications space", software revenue not disclosed [M2]; nothing on on-premise AI or tools per wafer. |

## 1B. Entry-point snapshot (separate from quality evidence)

| | KLA (KLAC) | AMAT | ASML (Nasdaq ADR) |
|---|---|---|---|
| Price, date | $161.01, close 11 Nov 2026 [E1] | $395.08, close 11 Nov 2026 (+6.05% that day; pre-market 12 Nov $385.70) [E2] | $1,534.42, close 11 Nov 2026 [E3] |
| Market cap / EV | $209.8B / $211.0B [E1] | $313.5B / $311.7B [E2] | $595.6B / $583.6B [E3] |
| P/E trailing / forward | 40.4 / 25.9 [E1] | 34.1 / 22.3 [E2] | 39.6 / 24.6 [E3] |
| Implied forward EPS growth (derived from the two P/Es; basis of "forward" not verified) | ~+56% | ~+53% | ~+61% |
| EV/sales; EV/EBITDA; EV/FCF | 14.6; 32.1; 52.3 [E1] | 10.1; 30.7; 55.4 [E2] | 13.0; 31.7; 24.9 [E3] |
| Analyst mean target; 52-week change | $219.62; +32.2% [E1] | $623.31; +68.1% [E2] | $2,138; +47.7% [E3] |
| Recent moves | $153.66 on 27 Oct 2026; low $144.82; 28.5% below 13 Aug high of $214.80 [X6] | $507.03 on 9 Oct 2026 (mkt cap $402B) [A4] -> $395 on 11 Nov (-22%, derived) | not collected |
| Latest guidance | Dec-26 qtr revenue $4.7B +/- $0.2B, non-GAAP EPS $1.44 +/- $0.11, non-GAAP GM 62.5% +/- 1 pt [K8] | Q4 FY26 revenue $10.25B +/- $0.5B, non-GAAP EPS $4.02 +/- $0.20, non-GAAP GM ~50.4% [A1][A7] | Q4 2026 sales EUR 14.2-15.2B, GM ~57%; FY26 EUR 44-45B, GM ~56% [M1] |
| Own 5-10 yr multiple range; consensus revenue growth | could not verify | could not verify | could not verify |
| Near-term events | Affiliates Rule decision by 10 Jan 2027 [X16]; Dec-qtr results and CY2027 detail "in late January" [K8] | Q4 FY26 results 12 Nov 2026 after close [A9]; Besi stake closing after HSR clearance [A12] | Q4 2026 results (Jan 2027, date not verified); NXE:3800F launch early 2027 [X7]; Capital Markets Day 10 Jun 2027 [M4] |

## 2. Supporting detail (quality)

### 2.1 KLA results FY26 and Q1 FY27; check of the two background claims

**Takeaway:** Both background claims are confirmed with wording caveats; the packaging figure has since risen to ~$1.1B, and the "$635M" uses a narrower scope than KLA's "$950M" advanced-packaging revenue.

Cited findings
- FY26 (release 28 Jul 2026): revenue $13,579.5M vs $12,156.2M (+11.7% unrounded); GAAP net income $4,830.8M; GAAP / non-GAAP diluted EPS $3.66 / $3.76; operating cash flow $4,143.1M; FCF $3,767.1M; dividends $1,057.8M + buybacks $2,289.8M [K2].
- FY26 product groups: Wafer Inspection $6,630.8M (+7%), Patterning $2,706.8M (+23%), Specialty Semiconductor Process $502.5M (-3%), PCB & Component Inspection $460.3M (+29%), Services $3,125.9M (+16%), Other $153.1M (-25%). Regions: China $4,048.4M (29.8%), Taiwan 26.8%, Korea 13.5%, North America 13.0%, Japan 6.7%, Europe & Israel 5.4%, Rest of Asia 4.8%. R&D $1,532.1M (11%); ~17,000 employees [K3].
- Q1 FY27 (28 Oct 2026): revenue $4,136.0M (+29% YoY, +13% QoQ); Wafer Inspection $2,111M (+37%); Patterning $862M (+29%); Specialty $114M; PCB & Component Inspection systems $168M (+43%); Services $850M (+14%); semi process-control systems 72% foundry/logic, 28% memory; regions China 34%, Taiwan 25%, North America 15%, Korea 12%, Rest of Asia 5%, Europe 5%, Japan 4%; FCF $1.34B (a record); returns $1.24B ($936M buybacks) [K8][K14]. GAAP EPS $1.18, non-GAAP $1.22; inventories $4,090.4M [K1]. ~$8.81B buyback authorisation left [K4]. Dividend raised 21% to $0.23/share on 12 Mar 2026, 17th consecutive increase [K14].
- Outlook (letter, 28 Oct 2026): H2-2026 revenue ~25% above H1; "significant growth in calendar 2027"; services growth at the top of the 13-15% model; five-year FCF CAGR ~20% vs revenue ~15% [K8]. Call (secondary): CY2026 WFE framing mid-$130B (Jan) -> >$140B (Apr) -> low-$150B (Jul) -> mid-$150B (Oct); capex $600-800M a year incl. an India campus; ~12-month lead times; some deliveries waiting on customer cleanroom/power [X6].
- **Claim 1:** 10-K (filed 6 Aug 2026): "The 12% increase in total revenues in the fiscal year ended June 30, 2026 ... was primarily driven by higher product revenues resulting from increased leading-edge customer investments in foundry/logic, memory and advanced packaging technologies, supported by strong demand associated with AI and HPC applications." Separately: "Demand for advanced semiconductor technologies, particularly at leading-edge nodes such as 2-nanometer, is increasing process complexity and process control intensity, which in turn is driving incremental demand for our solutions." [K3]. The 28 Jul release does not use "process control intensity" [K2]. Verdict: $13.58B and 12% confirmed. The intensity language is in the 10-K MD&A, not in the sentence explaining the 12%. (Quotes extracted by an automated reader; spot-check advised.)
- **Claim 2:** Wallace, 29 Apr 2026: advanced packaging "will grow from approximately $635 million in 2025 to approximately $1 billion in 2026" [K6]. Updated 28 Oct 2026: "Advanced Packaging process control systems revenue remains on track to hit approximately $1.1 billion, or more than 70% year-over-year growth" [K8]. Scope note: at the Investor Day, "950 million in advanced packaging revenue in 2025" [K10] - a broader measure than the $635M process-control figure.

Inferences
- FY26 growth was led by patterning; wafer inspection re-accelerated to +37% in Q1 FY27.
- China rose to 34% in Q1 FY27 although management guides it down; the 2027 "low-20s" figure is secondary only.

### 2.2 KLA market share by segment and against rivals

**Takeaway:** Only one free third-party series exists (The Information Network: ~74% of metrology & inspection, gaining). KLA's own figure (56.5% of "process control") uses a wider market. No free sub-segment data.

Cited findings
- 72.6% (2024) -> 73.8% (2025); AMAT 11.1% -> 9.8%; market $6.0B (2020) -> $12.9B (2025) [X1] (4 May 2026). AMAT and TEL lost served-market share in 2025; KLA, Lam and ASML gained (tables paywalled) [X2].
- Co. claims, 12 Mar 2026: 56.5% share, +2 pts since 2021, commitment since 2019 to gain 0.5 pt a year; gains in optical, e-beam, AP and reticle inspection [K10]. KLA's e-beam (~$400M) covers single-beam inspection (1-4 nm resolution), voltage contrast incl. a multibeam system, review and a little metrology; mask e-beam excluded [K12]. KLA says it would be ">50%" of process control in 2025 in the context of packaging, without naming a share target [K12].
- GM Insights (low quality): KLA 53%, AMAT 15%, ASML 11% of 2025 "inspection systems" [X3].

Gaps: overlay share (KLA Archer vs ASML YieldStar); e-beam share among KLA, AMAT, ASML and Hitachi; packaging vs Camtek/Onto; China vs domestic suppliers - none found free.

### 2.3 KLA buried 3D, bonded stacks, AI, software, intensity (Investor Day, 12 Mar 2026, unless stated)

Cited findings
- Intensity series (process control as % of WFE): 5.3% when WFE was ~$60B, then 5.8, 6.4, 6.7, 7.1, 7.4%; "~9%" assumed for 2030 [K10]. Logic: N-2 -> N-1 and N-1 -> N each +30% intensity; "Incremental value versus N minus two for KLA is one billion in logic" [K10]. DRAM "is becoming more like logic"; DRAM WFE 2x while KLA DRAM revenue 3x; incremental memory intensity gain "$450 million in calendar 25" [K10]. CFO, 29 Apr 2026: "The 2-nanometer node has higher intensity than 3-nanometer node" [K6].
- E-beam entered for buried 3D defects; KLA "took ... six years, seven years" to do e-beam and "only just needed to change the microscope" [K10].
- AI stance: "in AI you can create models easily and replicate somebody else's performance. That is not the case for KLA systems. We build very complex systems to reach to very pure signals" [K10]; "if you don't have a pure signal, then the chances of you being able to do defect detection is very low" [K10]. Fab-wide slow-variability AI (temperature, humidity, overlay drift) is the customer's job, "I don't think this is in conflict for process control" [K12].
- Hybrid bonding: logic SoIC moving to hybrid bonding; four next systems "already developed" [K10]; KLA grows intensity "no matter what, because hybrid bonding will drive intensity. But even the TCNF bonding drives intensity up" [K12].
- Products (10-K): Archer, ATL, Axion, SpectraShape (metrology); Teron, TeraScan (reticle); eDRX, eDR7xxx (review); Kronos, Micro-SR, CIRCL-AP, irArcher, PWG5 with XT, eDR7xxxAP (packaging); Klarity, 5D Analyzer, OVALiS, aiSIGHT, Anchor (software) [K3].
- 2030 target model (CFO, 12 Mar 2026): revenue $26B +/- $2.5B (bridge: CY2025 $12.7B + $10.6B systems + $2.7B service); GM 63.5% +/- 0.5 pt; op. margin 45-47%; R&D ~11%, SG&A ~7%; non-GAAP EPS "$84" +/- $8 pre-split (= $8.40 +/- $0.80 post-split, derived); semi PC systems CAGR 16.5% vs industry 12%; WFE ~15% of a ~$1.4T semi market [K9][K13]. Prior 2026 model ($14B, $38 EPS pre-split) has been exceeded [K9]. Oct 2026: 2030 model assumptions "will be exceeded before 2030" (secondary) [X6].

### 2.4 Applied Materials PDC and parent

Cited findings
- FY25 (10-K, 12 Dec 2025): revenue $28,368M (+4%); Semiconductor Systems $20,798M (op. margin 35.5%); AGS $6,385M (28.1%); GM 48.7%; R&D $3,570M; China $8,529M (30%) vs $10,117M (37%); backlog $15,002M; ~36,500 employees; ~4% workforce cut ($181M) [A3].
- Q3 FY26 (13 Aug 2026): Semiconductor Systems $7,040M (GAAP op. margin 37.7%; foundry/logic/other 67%, DRAM 26%, flash 7%); AGS $1,781M (30.1%); China $2,506M (28%), Taiwan 22%, Korea 17%, US 15%, Japan 9%; OCF $3,037M, capex $707M, FCF $2,330M [A1]. Q4 guide by segment: Semiconductor Systems ~$7.9B, AGS ~$1.84B, Other ~$510M; AGS >20% growth in CY2026 [A7].
- Feb 2026: semiconductor equipment business to grow "over 20 percent this calendar year"; HBM needs "3x-4x more DRAM wafer starts per delivered bit" [A10]. Aug 2026: PDC >50% and packaging >70% growth in CY2026; "strong pipeline of new products" for 2027 [A5].
- Besi (26 Oct 2026): accelerated share purchase to ~20% of Besi; first invested Apr 2025; "no intention to increase its investment in Besi beyond approximately 20 percent"; no board seat; rationale "hybrid bonding technology and next-generation interconnect architectures" [A12].

Inference: PDC is ~5-6% of AMAT; its growth (>50%) is about twice the parent's FY26 growth (~21%, derived from $34.3B vs $28.4B).

### 2.5 ASML M&I and parent

Cited findings
- 2025 system sales by technology (EUR M, units): EXE 1,156.9 (4); NXE 10,445.8 (44); ArFi 10,311.4 (131); ArF dry 427.0 (16); KrF 1,001.3 (78); i-line 307.3 (54); M&I 824.6 (208); total 24,474.3 (535) [M2]. 2025 sales by region: China EUR 9,519.7M (29.1%), Taiwan 25.5%, Korea 25.0%, US 12.5%, Japan 4.3% [M2].
- 2030 opportunity (Investor Day Nov 2024, restated in AR2025): EUR 44-60B revenue, GM ~56-60%; "non-EUV sales (lithography and M&I)" EUR 11-15B across the scenarios [M2].
- Q3 2026: system sales EUR 8,373.2M; 9M sales EUR 29,755.4M; 121 litho units (excl. M&I) [M3]; EUV EUR 4.1B / non-EUV EUR 4.3B; logic 54% / memory 46%; FY26 EUV >+45%, installed base ~+50% (secondary) [X7]; EUV 46%, ArFi 36% of Q3 system sales (secondary) [X8].

## 3. Resilience across AI-spending scenarios (inferences from cited data)
- Steady growth: all three are supply-constrained into 2027 (KLA lead times ~12 months [X6]; ASML short of demand in 2027-28 [M1]; AMAT doubling output by 2028 [A7]); KLA's own model assumes 11-13% WFE CAGR to 2030 [K10].
- Pause around 2028: ASML holds the largest cushion (backlog EUR 46.5B; EUR 9.3B non-current prepayments) [M2][M3]. KLA's services (>80% contracted, 24-year tool lives) are the most annuity-like buffer [K11]; AMAT's AGS ~20% of revenue [A1]. All three are adding capacity now (KLA capex $600-800M/yr [X6]; AMAT capex 9% of TTM revenue vs 4.4% in FY24 [A4]; ASML +30% capacity in 2027 [M1]), a typical late-upcycle exposure.
- Acceleration: the three bind on supply rather than demand; KLA says memory intensity is converging on logic [X6][K10], which raises KLA's leverage to a memory-led 2027 (memory ~60% of 2027 WFE, secondary [X6]).
- Export controls: China is 28-34% of recent revenue at KLA and AMAT and ~20-23% at ASML [K8][A1][X8]. The Affiliates Rule cliff moved to 10 Jan 2027 [X16].

## 4. Could not verify
- Third-party sub-segment shares (optical patterned, overlay, e-beam, reticle, packaging, China) - Gartner/TechInsights/Yole paywalled.
- AMAT PDC revenue (not disclosed; estimate only); claims about SEMVision H20 (CFE, "up to 50%" resolution, "up to 10X" speed, deep-learning defect classification), PROVision and Enlight appeared only in search summaries; GAA/backside-power qualifications at named customers.
- ASML M&I sales in 2026; YieldStar "more than double" demand claim; multibeam customer adoption; overlay share vs KLA.
- KLA tool-of-record wins and hybrid-bonding qualifications at named customers; software pricing; any product with a published measurement uncertainty.
- Whether any of the three has access to customers' destructive reference data: no evidence found.
- KLA "record close of $301.71" on 30 Jun 2026 (sec-api) [X5] conflicts with other price data; 5-10-year valuation ranges; consensus revenue growth.
- ASML's Q4 2026 and KLA's Q2 FY27 report dates; status of the US MATCH Act; effective date of the Dutch M&I licence rule.

## 5. Sources (accessed 12 Nov 2026; publication date given)
- [K1] KLA Q1 FY27 release (8-K Ex.99.1), 28 Oct 2026 - https://www.sec.gov/Archives/edgar/data/0000319201/000031920126000032/exhibit991earningsrelease0.htm
- [K2] KLA Q4/FY26 release (8-K Ex.99.1), 28 Jul 2026 - https://www.sec.gov/Archives/edgar/data/0000319201/000031920126000024/exhibit991earningsrelease7.htm
- [K3] KLA 10-K, FY to 30 Jun 2026, filed 6 Aug 2026 - https://www.sec.gov/Archives/edgar/data/319201/000031920126000027/klac-20260630.htm
- [K4] KLA 10-Q, quarter to 30 Sep 2026 - https://ir.kla.com/sec-filings/all-sec-filings/content/0000319201-26-000034/klac-20260930.htm
- [K5] KLA IR release page, 28 Oct 2026 - https://ir.kla.com/news-events/press-releases/detail/523/kla-corporation-reports-fiscal-2027-first-quarter-results
- [K6] KLA March-quarter call transcript, 29 Apr 2026 (Motley Fool) - https://www.fool.com/earnings/call-transcripts/2026/04/29/kla-klac-q3-2026-earnings-call-transcript/
- [K7] KLA Investor Day 2026 page (event 12 Mar 2026) - https://ir.kla.com/news-events/investor-day-2026
- [K8] KLA Letter to Shareholders Q1 FY27, 28 Oct 2026 - https://d1io3yog0oux5.cloudfront.net/_50d63f16d5350a23b8ec3131256a9548/klatencor/db/1117/10679/letter_to_shareholders/KLA_Earnings_Shareholder_Letter_-_Q1_FY27.pdf
- [K9] KLA Investor Day transcript, Higgins "Path to 2030 Target Model", 12 Mar 2026 - https://d1io3yog0oux5.cloudfront.net/_50d63f16d5350a23b8ec3131256a9548/klatencor/db/1167/10643/transcript/KLA+Presentation+Transcripts+-+05.pdf
- [K10] KLA Investor Day transcript, Khan "Process Control for the AI Era", 12 Mar 2026 - https://d1io3yog0oux5.cloudfront.net/_50d63f16d5350a23b8ec3131256a9548/klatencor/db/1167/10630/transcript/KLA+Presentation+Transcripts+-+03.pdf
- [K11] KLA Investor Day transcript, Lorig (services), 12 Mar 2026 - https://d1io3yog0oux5.cloudfront.net/_50d63f16d5350a23b8ec3131256a9548/klatencor/db/1167/10632/transcript/KLA+Presentation+Transcripts+-+04.pdf
- [K12] KLA Investor Day Q&A transcript, 12 Mar 2026 - https://d1io3yog0oux5.cloudfront.net/_50d63f16d5350a23b8ec3131256a9548/klatencor/db/1167/10644/transcript/KLA+Presentation+Transcripts+-+06+QA.pdf
- [K13] KLA Investor Day transcript, Wallace, 12 Mar 2026 - https://d1io3yog0oux5.cloudfront.net/_50d63f16d5350a23b8ec3131256a9548/klatencor/db/1167/10629/transcript/KLA+Presentation+Transcripts+-+02.pdf
- [K14] KLA earnings slides Q1 FY27, 28 Oct 2026 - https://d1io3yog0oux5.cloudfront.net/_50d63f16d5350a23b8ec3131256a9548/klatencor/db/1117/10679/earnings_slide_presentation/KLA_Earnings_Slides_-_Q1_FY27.pdf
- [A1] AMAT Q3 FY26 release (8-K Ex.99.1), 13 Aug 2026 - https://www.sec.gov/Archives/edgar/data/6951/000162828026056699/exhibit991q32026earningsre.htm
- [A2] AMAT 10-Q, quarter to 26 Jul 2026, filed 20 Aug 2026 - https://www.sec.gov/Archives/edgar/data/6951/000162828026058235/amat-20260726.htm
- [A3] AMAT 10-K, FY to 26 Oct 2025, filed 12 Dec 2025 - https://www.sec.gov/Archives/edgar/data/6951/000162828025056742/amat-20251026.htm
- [A4] sec-api.io AMAT analysis (secondary), 12 Oct 2026 - https://sec-api.io/insights/applied-materials-amat-financial-analysis-q3-fy2026-china-revenue-share-export-control-settlement-wafer-equipment-peers-and-scenarios-to-fy2029
- [A5] Newsquawk headline, 13 Aug 2026 - https://www.newsquawk.com/headlines/applied-materials-amat-ceo-comments-that-the-company-now-expects-overall-packaging-revenues-to-grow-more-than-70-and-expects-to-grow-process-diagnostics-and-control-business-over-50-in-calendar-2026
- [A7] Futurum, "Applied Materials Q3 FY 2026", 17 Aug 2026 - https://futurumgroup.com/insights/applied-materials-q3-fy-2026-advanced-packaging-and-dram-accelerate-growth/
- [A8] AMAT Q3 FY26 call transcript (Seeking Alpha; partial, snippet only) - https://seekingalpha.com/article/4936471-applied-materials-inc-amat-q3-2026-earnings-call-transcript
- [A9] AMAT Q4 FY26 call event page - https://ir.appliedmaterials.com/events/event-details/q4-2026-applied-materials-earnings-conference-call ; EDGAR 8-K list - https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000006951&type=8-K
- [A10] Futurum, "Applied Materials Q1 FY 2026", 17 Feb 2026 - https://futurumgroup.com/insights/applied-materials-q1-fy-2026-ai-demand-lifts-outlook/
- [A11] LongYield (Substack, partly paywalled), 15 May 2026 - https://longyield.substack.com/p/applied-materials-and-the-angstrom
- [A12] AMAT 8-K Ex.99.1, Besi investment, 26 Oct 2026 - https://www.sec.gov/Archives/edgar/data/6951/000162828026067303/ex991prforprojectbasil.htm
- [M1] ASML Q3 2026 release (6-K Ex.99.1), 14 Oct 2026 - https://www.sec.gov/Archives/edgar/data/0000937966/000162828026065813/pressreleasefinancialresul.htm
- [M2] ASML 20-F / Annual Report 2025, filed 25 Feb 2026: revenue note https://www.sec.gov/Archives/edgar/data/937966/000162828026011378/R13.htm ; segment note https://www.sec.gov/Archives/edgar/data/937966/000162828026011378/R14.htm ; financial performance section https://ourbrand.asml.com/m/419103cb23dfeaa4/original/asml-2025-annual-report-financial-performance-section.pdf
- [M3] ASML Q3 2026 US GAAP statements (6-K Ex.99.3), 14 Oct 2026 - https://www.sec.gov/Archives/edgar/data/937966/000162828026065813/financial_statementsxusx.htm
- [M4] ASML Q3 2026 presentation (6-K Ex.99.2), 14 Oct 2026 - https://www.sec.gov/Archives/edgar/data/937966/000162828026065813/a2026_10x14xpresentation.htm
- [X1] 247wallst (R. Castellano, The Information Network data), 4 May 2026 - https://247wallst.com/technology-3/2026/05/04/kla-is-gaining-share-as-ai-chip-complexity-drives-up-yield-costs/
- [X2] Castellano, Semiconductor Deep Dive (partly paywalled), 10 May 2026 - https://drrobertcastellano.substack.com/p/applied-materials-lost-share-across
- [X3] GM Insights market pages (undated; low quality) - https://www.gminsights.com/industry-analysis/semiconductor-inspection-systems-market ; https://www.gminsights.com/industry-analysis/semiconductor-process-control-equipment-market
- [X4] Reuters analysis via The Star, 14 Sep 2026 - https://www.thestar.com.my/tech/tech-news/2026/09/14/analysis-asml-extends-chipmaking-dominance-as-customers-embrace-high-na
- [X5] sec-api.io KLA Q1 FY27 analysis (secondary), 2 Nov 2026 - https://sec-api.io/insights/kla-klac-q1-fy27-earnings-sec-filing-analysis
- [X6] Earnings Whispers, KLA Q1 FY27, 28 Oct 2026 - https://www.earningswhispers.com/article/KLAC/r679
- [X7] AlphaSense ASML Q3 2026 summary (AI-generated, secondary) - https://alpha-sense.com/earnings/asml
- [X8] xenospectrum, ASML China Q3 2026 (Oct 2026) - https://xenospectrum.com/en/asml-china-sales-q3-2026/ ; Zacks (snippet only; page blocked) - https://zacks.com/stock/news/3006983/asml-q3-earnings-beat-on-strong-upgrade-demand-revenues-miss
- [X9] Tom's Hardware and NL Times, Dutch M&I licensing, 15 Jan 2025 - https://www.tomshardware.com/tech-industry/netherlands-tightens-export-controls-on-sanctioned-semiconductor-equipment-move-made-in-line-with-u-s-limitations-asml-will-apply-for-licenses-from-the-dutch-government ; https://nltimes.nl/2025/01/15/restrictions-chip-machine-exportations-dutch-companies-asml-asmi
- [X10] ioplus.nl, Dutch government vs US MATCH Act (May 2026; snippet only) - https://ioplus.nl/en/posts/government-clashes-with-us-over-strict-asml-export-rules
- [X11] evertiq, ASML-Mistral, 9 Sep 2025 - https://evertiq.com/design/2025-09-09-asml-invests-13b-in-mistral-ai-forms-strategic-partnership
- [X13] ASML release, first eScan1100, 2022 - https://www.asml.com/en/news/press-releases/2022/asml-announces-installation-of-first-hmi-escan-1100-multibeam-system ; AnandTech - https://www.anandtech.com/show/15822
- [X15] YieldStar 550B press reports, Oct 2026 (search snippets; which outlet said what not verified) - https://www.eenewseurope.com/en/asml-hits-record-e11-7-billion-sales-as-ai-chip-demand-surges/ ; https://letsdatascience.com/news/asml-reports-record-q3-sales-and-raises-outlook-c553b961
- [X16] Thompson Hine SmarTrade, "BIS Extends Affiliates Rule Until January 2027", 6 Nov 2026 - https://www.thompsonhinesmartrade.com/2026/11/bis-extends-affiliates-rule-until-january-2027/
- [E1] stockanalysis.com KLAC statistics, close 11 Nov 2026 - https://stockanalysis.com/stocks/klac/statistics/
- [E2] stockanalysis.com AMAT statistics, close 11 Nov 2026 - https://stockanalysis.com/stocks/amat/statistics/
- [E3] stockanalysis.com ASML statistics, close 11 Nov 2026 - https://stockanalysis.com/stocks/asml/statistics/
