# Automatic test equipment (ATE) for chip electrical test: Advantest, Teradyne and the wider tester field

**Research date: 12 November 2026.** Every figure carries its date and source.
- **"company claim, unconfirmed"** marks a statement no outside party has confirmed.
- **"secondary"** marks figures taken from aggregators or press summaries rather than filings.
- Quality evidence (A1-A3 and sections 1-6) is kept separate from entry-point data (A4 and section 7).

**Coverage**
- **Advantest, read in full:**
  - English 決算短信 for FY2025 (year to March 2026) and H1 FY2026.
  - Results notes, slides and Q&A for April, July and October 2026.
  - April 2026 sell-side meeting Q&A.
  - Fireside-chat scripts for 17 November 2025 and 12 November 2026.
  - Integrated Annual Report 2026 and the October 2025 revision of the MTP3 targets.
  - Sixteen product and partner releases.
- **Teradyne, read in full:**
  - Q3 2026 8-K, 10-Q, earnings slides and CEO/CFO prepared remarks.
  - 2025 10-K and Q4 2025 release.
  - 11 March 2025 Analyst Day deck.
  - Ten product and deal releases.
  - Q&A content is from third-party summaries only.
- **Where coverage is thin:**
  - Chroma, Cohu, AEM and the Korean suppliers rest on secondary summaries, with Korean figures from Korean-press summaries not checked against DART.
  - No Japanese 有価証券報告書, Taiwanese MOPS or SEMI/TechInsights primary data was opened.
  - Japanese niche testers and Emerson/NI were not researched beyond partner releases.

**Change from the brief's background:** Advantest **no longer holds an equity stake in PDF Solutions**. It sold all 3,306,924 shares in a PDF Solutions offering that closed in May 2026 (details in section 6).

---

## A. Evidence tables

### A1. Advantest (6857.T) — quality tests a-e

| Test | Dated evidence |
|---|---|
| (a) Position | **Test platform:** owns the production test that decides ship or scrap for most AI compute. The V93000 covers GPU, custom ASIC, CPU, networking and silicon photonics. Advantest says V93000 is "increasingly regarded as an industry standard in HPC" (Q&A 28 Oct 2026; company claim, unconfirmed). **Full test cell:** testers, handlers (M5241 memory handler), device interfaces, SLT (7038), and a die-level prober in co-development with Tokyo Seimitsu (16 Dec 2025). **Data:** ACS RTDI is a real-time data infrastructure at the tester. Advantest says NVIDIA "selected ACS RTDI for high-volume production" for Blackwell and later parts (6 Oct 2025; Advantest announcement). |
| (b) Lead | **Share (company estimates):** SoC 59% (CY23), 56% (CY24), 66% (CY25); memory 56%, 63%, 61%; overall 58%, 58%, 65% (slides 27 Apr 2026). Also "majority share of the global AI accelerator business" and "a path to above 70%" (company claims, unconfirmed). **Outside evidence:** TechInsights 2026 customer-satisfaction survey, global #1 for the 7th year running (14 May 2026); TSMC 2025 Excellent Performance Award (24 Dec 2025); R&I rating raised to AA- (23 Jul 2026). **Filing cross-check:** in Jul-Sep 2026, Advantest SoC sales were ≈$2.19bn (¥353.3bn at ¥161/$) against Teradyne SoC revenue of $676.5m. That is about 76% of the two firms combined; in compute alone it is higher, because Teradyne compute was only about 20% of its Q3 sales (see section 3). No third-party share figure (TechInsights, Gartner, Yole) was found. |
| (c) Revenue model | **FY2025 Test Systems ¥1,019.4bn (90.3%):** SoC ¥767.4bn, memory ¥171.5bn, other systems ¥80.5bn. **Services & Others ¥109.2bn (9.7%):** support services ¥65.0bn (5.8%) and other ¥44.2bn (interface boards, mask CD-SEM). **FY26 forecast:** Services & Others ¥148.5bn (8.0%), of which support ¥86.0bn (4.6%). **Licensing:** tester software licensing is cited as a margin driver (Apr and Oct 2026) but not disclosed. **No hours or seat billing.** Employees: 7,241, of whom 1,085 are system or application engineers (FY2025, IAR 2026). |
| (d) Financial strength | **FY2025:** sales ¥1,128.6bn (+44.7%); gross margin ≈64.3%; operating margin 44.2%; ROE 57.6%; ROIC 54.4% (company definition); FCF ≈¥300.6bn. **H1 FY26:** sales ¥845.2bn (+60.5%); gross margin 70.4%; operating margin 54.0% (Q2: 71.1% and 55.9%). **Balance sheet, 30 Sep 2026:** cash ¥401.8bn; ¥89.5bn convertible bonds; net cash ≈¥294.5bn; investment securities ¥432.6bn; equity ratio 66.1%. **Customers:** "a small number of top customers account for a substantial portion of net sales"; no names or percentages (IAR 2026). **Ship-to:** FY2025 Taiwan 50.5%, China 18.9%, Korea 16.0%; H1 FY26 Taiwan 52.0%, China 18.9%, Korea 15.6%. Management puts China at "≈19%… consistent around 20%" (29 Jul 2026). |
| (e) Resilience | **Cycle:** tester market CY23 $4.4bn, CY24 $6.0bn, CY25 $9.0bn, CY26e ≈$14.25bn (company estimates); management calls this a "megacycle". **Buffers:** EMS-based variable costs; "strategic inventory is gold" (inventory ¥352.4bn, against ¥231.7bn at March 2026); platforms that last 10-15 years (12 Nov 2026). **Overbuild risk:** SoC capacity is above 5,000 a year, the target is 10,000 a year "well ahead" of plan, and 20,000 is under discussion. **Cost risk:** DRAM components. **Sensitivities:** operating profit moves ¥5.8bn per ¥1 move against the dollar; China ≈19% of sales. As a Japanese company it is not under the US military-end-user rule that Teradyne's 10-K cites. |

### A2. Teradyne (TER) — quality tests a-e

| Test | Dated evidence |
|---|---|
| (a) Position | **Number two in SoC:** UltraFLEXplus and J750. **Strong in memory and HBM:** Magnum 7H, "the industry de facto standard" (Analyst Day 11 Mar 2025; company claim, unconfirmed). **Also sells:** SLT and burn-in (Titan HP), HDD test, board, optical and interconnect test (Product Test), and robotics. **Probe-layer stakes:** 10% of Technoprobe with a board seat (May 2024); a $300m minority stake in FormFactor agreed 6 Oct 2026. **Strategy:** a "wafer to AI data center" model sold through an open ecosystem of partners. |
| (b) Lead | **Memory:** a record $300.8m in Q3'26 (+135% YoY), the fourth quarter running above $200m. That roughly equals Advantest's memory-tester sales of ¥53.4bn (≈$332m) in the same quarter. Teradyne claims "higher share" in HBM performance test (28 Oct 2026; company claim, unconfirmed). Advantest itself expects its memory share "may experience a decline this year" (29 Jul 2026). **Compute:** dual-vendor wins. The first hyperscaler is a "mature" dual source, a merchant GPU customer is a "fast follower", a second hyperscaler has passed qualification and a third is in qualification (28 Oct 2026; company claims, unconfirmed). **Outside evidence:** TSMC 2025 OIP Partner of the Year for 3DFabric testing, with a TSMC director quoted (Sep 2025). |
| (c) Revenue model | **Q3'26 by product:** SoC $676.5m, memory $300.8m, IST $94.7m, Product Test $138.1m, Robotics $95.8m. **Service revenue:** $141.8m (10.9%; Semi Test service $105m), with services gross margin ≈65%. Revenue is 91% point-in-time. No hours or seat billing. TestInsight test-conversion software (bought 16 Apr 2026) is also sold for other vendors' platforms. |
| (d) Financial strength | **Q3'26:** revenue $1,306.0m (+70%); GAAP gross margin 59.1%; non-GAAP operating margin 31.6%; non-GAAP EPS $2.29. **2025:** revenue $3,190m; non-GAAP gross margin 58.3%; operating margin 22.3%; EPS $3.96; FCF $450m. **9M'26:** FCF $806.1m. **Balance sheet:** cash and investments $625m; no debt; $1.0bn revolver to 2031; trailing ROIC 42.4% (stockanalysis). **Concentration:** the five largest direct customers were 44% of 2025 revenue (36% in 2024, 32% in 2023). One direct customer was 19%; two specifiers drove 12% and 10%. **Country:** Q3'26 Korea 32%, China 21%, Taiwan 14%, Singapore 9%, US 8%; 9M'26 Taiwan 32%, Korea 24%, China 15%. |
| (e) Resilience | **Cycle:** 2026e revenue ≈$5.2bn (+60%+), close to the target model's ≈$6.0bn already. **Buffers:** >80% of revenue goes through contract manufacturing; 100% of employees have variable pay; 35% work in low-cost regions (Analyst Day 2025). **Diversifiers:** auto and industrial >$600m in 2026 (<$400m in 2025), HDD test, Product Test, and robotics, now back in profit. **Weak spot:** mobile is below historical levels. **Exports:** the US military-end-user rule "has impacted our ability to sell… in China", and trade rules limit competitiveness "where some competitors are not subjected to the same restrictions" (10-K 2025). **Inventory:** $575m, against $403m in Q2'26. |

### A3. Six transitions — what each said versus did (dated)

| Transition | Advantest | Teradyne |
|---|---|---|
| (1) Pass/fail to inference with stated uncertainty | **Said:** ACS RTDI moves "testing from validation to prediction" (6 Oct 2025). CTO: the job is "not just go, no go… trim and calibrate every device"; chiplet "power pairing" (17 Nov 2025). **Did:** ACS RTDI with NVIDIA ML in high-volume production (Oct 2025). Emerson partnership for edge analytics, re-binning and adaptive test (19 Mar 2025). Pin Scale 5000B adds vector memory "for analytics of failure data" (22 Apr 2026). **Reversed:** sold its PDF Solutions stake (May 2026). No product with a stated-uncertainty output found. | **Did:** Titan HP burn-in keeps "full stress-and-test history" per device "on a single record" (6 Oct 2026). Teradyne slides list an NVIDIA "AI-defined fabs" collaboration (title only). No analytics or inference product found (could not verify). |
| (2) Hand-written to AI-built test programs | **Said:** SmarTest 8 has "AI-enabled tools for test program development" (13 Oct 2026). "Automation of Test" is an MTP3 theme. **Did:** acquired AllianceATE in Sep 2025. Its Velocity tool streams design files to V93000 for "first-time-right" patterns, replacing "weeks of developing custom code" (18 May 2026, Arm quoted). SiConic bench ecosystem launched Feb 2025 and extended to DFT on 16 Jul 2026. | **Did:** acquired TestInsight, a maker of "test development, validation, and conversion software", for "pre-silicon validation and automated pattern generation". It keeps serving "all ATE platforms" (16 Apr 2026). Atlas SLT software imports and ports programs. No AI-agent claim found. |
| (3) Single die to bonded stacks | **Said:** "test times increase by multiples from one generation to the next" (12 Nov 2026). "Die level probing will need to come" (Nov 2025). Plans memory test "beyond HBM4" (Apr 2026). **Did:** Tokyo Seimitsu die-level prober (Dec 2025). Minority stakes in Technoprobe (2.5%), FormFactor and MJC (Jan-Feb 2025). M5241 handler shipping from Q2 CY2026. T5801 DRAM tester. Applied Materials EPIC (21 Apr 2026). | **Said:** "today's wafer probes are not suitable" for large CoW modules; access at chip-on-wafer stage is "limited to C4 bump interfaces" (blog 27 Jul 2026). **Did:** Magnum 7H for HBM2E-HBM4E, wafer to KGSD to burn-in (4 Aug 2025). UltraFLEXplus with TEL Prexa singulated-die prober for KGD (8 Jun 2026). UCIe streaming-scan test (TSMC award, Sep 2025). Titan HP burn-in (Oct 2026). Technoprobe and FormFactor stakes. |
| (4) Hardware to software and data | **Said:** evolving "from a test equipment company into a comprehensive solutions provider" (29 Jul 2026). **Did:** Services & Others under 10% of sales; ¥364.7bn of undisclosed "strategic investment" securities bought in H1 FY26. | Service ≈11% of revenue; TestInsight software revenue undisclosed. |
| (5) AI on the chipmaker's premises | **Said:** Emerson partnership "pushing… compute and analysis capabilities to the edge" (Mar 2025). **Did:** ACS RTDI at "high-volume production sites worldwide" (company claim, unconfirmed). | No evidence found. |
| (6) Fewer insertions or testers after 2030 | **Said:** test-time cuts from new modules won't "impact overall demand" (27 Apr 2026). New-system demand "at least next two to three years", then possibly an upgrade cycle (27 Apr 2026). "Distribution of test" lets customers move content between insertions (IAR 2026). No post-2030 view. | **Said:** chiplets are a trend "with growth potential for the next decade" (Jul 2026). Lower HBM stack heights mean more stacks to test (Oct 2026). No post-2030 view. |

### A4. Entry-point snapshot (separate from quality)

| Item | Advantest (6857.T) | Teradyne (TER) |
|---|---|---|
| Price and date | ¥29,985, close 12 Nov 2026 (−4.6% on the day) | $265.78, close 11 Nov 2026 (+8.3% on the day) |
| Market cap / EV | ¥21.65tn / ¥21.35tn (≈$140bn at ¥155/$) | $41.49bn / $41.01bn |
| P/E (trailing / forward) | 38.1 / 24.5; 29.2 on company FY26 EPS guidance of ¥1,027 | 30.5 / 25.1; 28.2 on 2026 non-GAAP EPS midpoint of $9.41 |
| EV/sales; EV/EBITDA; EV/FCF | 15.3; 29.6; 47.5 | 8.2; 23.2; 40.0 |
| 52-week change; dividend yield | +50.9%; 0.33% | +44.4%; ≈0.2% (my calculation) |
| Consensus | Buy (21 analysts); mean target ¥46,624 | Buy (18 analysts); mean target $415.88 |
| Guidance | FY26 (to Mar 2027): sales ¥1,863bn; operating profit ¥967bn (51.9%); 2H operating margin 50.1%. Raised twice (April ¥1,420bn, July ¥1,714bn). | Q4'26 revenue $1.25-1.35bn; gross margin 57.5-58.5%; non-GAAP EPS $1.95-2.25; FY ≈$5.2bn; "2027 another year of healthy growth" |
| Next events | Half-year 有報 13 Nov; interim dividend 1 Dec; late Jan 2027 Q3 results with the first numeric CY2027 TAM and timing of 10,000 a year; ~May 2027 MTP4 (outlook to CY2028-29); ¥280bn buyback to 24 Mar 2027 | Ex-dividend 23 Nov; UBS conference 30 Nov; quiet period from 18 Dec; FormFactor closing in Q4; Q4 results (early Feb 2027 on last year's timing) with an **updated target earnings model**; dual-vendor ramps mid and 2H 2027 |

Sources for A4: [stockanalysis 6857, 12 Nov 2026][S1]; [stockanalysis TER, 12 Nov 2026][S2]; the company documents cited in sections 2, 3 and 7. The yen conversion and the P/E on guidance are my calculations.

---

## 1. Market: tester market size, shares, test intensity, bottleneck

### Takeaway
Both leaders put the 2025 ATE market at about **$9.0bn**. Advantest's CY26 estimate is **≈$14.25bn**: SoC about $11.5bn and memory about $2.75bn. Advantest expects CY27 growth near the recent ~50% a year. SEMI billings data show test's share of chip-equipment spending rising from 6.4% (2025) to 8.1% (Jan-Aug 2026). The driver is test content per device in advanced packaging. Test capacity and DRAM components are stated constraints.

### Cited Findings
- **Advantest's tester-market series (company estimates; unconfirmed)** ([slides 27 Apr 2026][S3]):

  | Year | Total | SoC | Memory |
  |---|---|---|---|
  | CY23 | $4.4bn | $3.3bn | $1.1bn |
  | CY24 | $6.0bn | $4.1bn | $1.9bn |
  | CY25 | $9.0bn | $6.9bn | $2.1bn |

- **Teradyne puts the 2025 ATE TAM at "~$9.0B"** and targets $12-14bn ([Q3'26 slides, 28 Oct 2026][S4]). In March 2025 it had forecast only a "9% CAGR" for ATE ([Analyst Day][S5]).
- **Advantest's CY26 forecast through 2026:**

  | Date | SoC | Memory | Total |
  |---|---|---|---|
  | Jan 2026 | $8.5-9.5bn | $2.2-2.7bn | — |
  | Apr 2026 | $8.7-9.5bn | $2.2-2.7bn | — |
  | Jul 2026 | $10.5-11.5bn | $2.5-3.0bn | $13.0-14.5bn (+19% at midpoint) |
  | Oct 2026 | ≈$11.5bn ("near the upper end") | midpoint | unchanged |

  Sources: [Jul note][S6]; [Oct note][S7].
- **CY27:** numbers will come in January 2027. "Tester TAM has grown at an annual average of about 50% or slightly above… we anticipate that tester TAM growth will be in line with that of recent years or potentially higher." The industry is expected to "remain supply constrained in CY2027" ([Q&A 28 Oct 2026][S8]).
- **Test's share of capex (third-party SEMI data, quoted by Teradyne):** test is 6.4% of semiconductor capex in 2025 and 8.1% in Jan-Aug 2026. The source is "SEMI, Product Buy Rate Data… SEMS ATE product billings / SEMS total IC equipment" ([remarks 28 Oct 2026][S9]; [slides][S4]).
- **Market structure (Teradyne):** compute was 35% of ATE TAM in 2024, against 15% in 2016; mobile fell from 37% to 14%. Teradyne's own SoC mix was 20% compute in 2024 ([Analyst Day, 11 Mar 2025][S5]).
- **Co-packaged optics:** the CPO tester market should "double or triple annually… reach about 1 billion USD", against an SoC tester market that "exceeds 11 billion USD and is growing at more than 50% annually" ([Q&A 28 Oct 2026][S8]). Teradyne calls CPO "preseason" ([StockStory, Oct 2026][S10]; secondary).
- **Test intensity (company claims; unconfirmed):**
  - "In some cases… test times increase by multiples from one generation to the next. No one really predicted the extent of the increase in test content" ([fireside 12 Nov 2026][S11]).
  - Accelerators get "longer test times and additional insertions… where 3D packaging is driving greater device complexity". CPU wafer sort is "broadly similar and may be slightly higher" than for accelerators; final test needs less ([Q&A 29 Jul 2026][S12]).
  - FY26 upside came mostly from agentic-AI CPUs, "a third layer of growth" ([Q&A 28 Oct 2026][S8]).
  - On packaging cost: "too expensive to throw away these expensive packages" ([fireside 17 Nov 2025][S13]).
  - Test menus are fixed after customer evaluation in early volume production, and extra quality tests may be added ([sell-side Q&A 27 Apr 2026][S14]).
- **HBM (Teradyne):** memory shortages are so severe that "AI accelerators are turning to lower stack heights of HBM… This will tend to increase the TAM for HBM performance test" ([remarks 28 Oct 2026][S9]).
- **Bottleneck evidence:**
  - Advantest: "We never want to be the critical path" (Jul 2026). Testers share "a similar component mix to data-center racks… competing for components with the very customers we serve" (12 Nov 2026). Visibility is now 18-month and sometimes multi-year forecasts, against six months before ([Q&A 29 Jul 2026][S12]).
  - Teradyne: "There is no current ATE solution for the most complex next generation AI and data center devices that are coming to market in 2027", which its new instruments are meant to address ([remarks][S9]; company claim, unconfirmed).

### Inferences
- **Size of the move:** a ≈$14.25bn CY26 would be more than 3x CY23 ($4.4bn) in three years. Teradyne's target model ($12-14bn), set in February 2026, has already been overtaken on Advantest's numbers.
- **What growth depends on:** growth rests mainly on test content per device. Transition (6), inference replacing measured insertions, would bite exactly there.
- **Market-research reports:** reports such as Mordor and LP Information give about $7.5bn for SoC plus memory in 2026. Their scope or data look stale; do not mix them with the company series.

### Gaps
- No independent 2024-27 tester market series or vendor-share table from SEMI, TechInsights/VLSI, Yole or Gartner was obtained. One newsletter cites VLSI for Advantest ≈50% and Teradyne ≈30% in 2023 ([Wing VC][S15]); this is weak.
- No third-party test time per device for accelerators or HBM.

---

## 2. Advantest (6857.T): results, segments, guidance, plan

### Takeaway
Advantest is highly profitable and net-cash: Q2 FY26 gross margin was 71% and operating margin 56%. It is at a record point in its cycle. Revenue comes overwhelmingly from AI compute shipped via Taiwan. Recurring support services are about 5% of sales, and the new ¥433bn securities book is opaque.

### Cited Findings
- **FY2025 (to 31 Mar 2026; reported 27 Apr 2026)** ([決算短信][S16]):
  - Sales ¥1,128.6bn (+44.7%); operating profit ¥499.1bn (44.2%); net income ¥375.4bn; EPS ¥515.15; overseas share 97.8%.
  - Test System ¥1,019.4bn (segment profit ¥518.8bn); Services & Others ¥109.2bn (¥8.8bn, including a ¥2.5bn divestiture gain).
  - FY2024 included a ¥21.4bn impairment on Essai (SLT).
  - Cash flow: operating ¥335.2bn; investing −¥34.6bn; buybacks ¥114.3bn. Dividend ¥59 ([FY25 slides][S3]).
- **FY2025 ship-to regions** (chart labels; these reconcile to the 決算短信 geography for Japan, Americas and Europe) ([FY25 slides][S3]):
  - FY2025: Taiwan ¥569.5bn, China ¥213.3bn, Korea ¥180.3bn, Others ¥72.8bn, Americas ¥44.5bn, Japan ¥25.1bn, Europe ¥23.1bn.
  - FY2024: Taiwan ¥326.5bn, China ¥175.1bn, Korea ¥157.0bn.
  - Taiwan grew on "strengthened quality assurance requirements for high-end SoC semiconductors from several U.S. fabless companies" ([FY25 note][S17]).
- **Quarterly results, Jun-25 to Sep-26** ([Oct slides][S18]):

  | Quarter end | Sales | Gross margin | Operating margin |
  |---|---|---|---|
  | Jun-25 | ¥263.8bn | 65.1% | 47.0% |
  | Sep-25 | ¥262.9bn | 62.2% | 41.3% |
  | Dec-25 | ¥273.8bn | 62.0% | 41.5% |
  | Mar-26 | ¥328.1bn | 67.4% | 46.7% |
  | Jun-26 | ¥367.5bn | 69.5% | 51.7% |
  | Sep-26 | ¥477.7bn | 71.1% | 55.9% |

- **Q2 FY26 detail** ([Oct note][S7]):
  - Segments: SoC ¥353.3bn; memory ¥53.4bn; other systems ≈¥29.9bn; services ¥41.1bn.
  - R&D ¥23.4bn (4.9% of sales); FCF ¥61.5bn after securities purchases.
  - Ship-to: Taiwan ¥261.3bn, China ¥90.1bn, Korea ¥64.6bn.
- **H1 FY26 (reported 28 Oct 2026)** ([決算短信 H1][S19]):
  - Sales ¥845.2bn; operating profit ¥456.8bn; financial income ¥57.0bn, of which ¥54.2bn is gains on strategic investments; net income ¥368.1bn.
  - Cash flow: operating ¥307.0bn; investing −¥210.9bn, including ¥184.4bn of debt-instrument purchases and ¥21.5bn of capex.
  - ¥100bn zero-coupon convertible bond due 2031 issued in April 2026.
  - Investment securities rose from ¥67.9bn to ¥432.6bn; inventories from ¥231.7bn to ¥352.4bn.
- **FY26 guidance (28 Oct 2026)** ([note][S7]; [slides][S18]):
  - Sales ¥1,863bn; operating profit ¥967bn; net income ¥741.5bn; gross margin ≈68%.
  - 2H sales ¥1,017.8bn (+20% on 1H); 2H operating margin 50.1%. 1H was helped by cheaper DRAM in inventory and a write-down reversal.
  - Segments: SoC ¥1,375.0bn; memory ¥229.0bn; other systems ¥110.5bn; services ¥148.5bn.
  - SoC mix: compute and communications 90% (95% in FY25). Memory mix: DRAM 85%, non-volatile memory 15%.
  - R&D ¥114bn; capex ¥60bn.
  - Component costs are to be offset via "higher-specification tester configurations, licensing, and new instrumentation" ([Q&A][S8]).
- **MTP3 targets (FY24-26 averages, revised 28 Oct 2025)** ([release][S20]):
  - Targets: sales ¥835-930bn; operating margin 33-36%; ROIC 34-39%; EPS ¥284-341.
  - Actual and forecast sales average ≈¥1,257bn.
  - MTP4 is due around May 2027 with an outlook through CY2028-29 ([Q&A 28 Oct 2026][S8]).
- **Capacity:**
  - SoC tester capacity is above 5,000 systems a year. The 10,000 target, originally end FY2028 or CY2029, is to be reached "well ahead", and 20,000 is under discussion ([Q&A 28 Oct 2026][S8]).
  - 10,000 of today's systems equal about 20,000 in 2020 configuration; 2020 output was about 1,000. A second EMS plant is ramping in Southeast Asia ([Q&A 29 Jul 2026][S12]).
  - Convertible-bond use: ≈¥50bn for capacity by March 2029, ¥20bn for inventory, ¥30bn for next-generation test ([決算短信 FY2025][S16]).
- **Returns:** interim dividend ¥49; buyback up to ¥280bn (11m shares) between 29 Oct 2026 and 24 Mar 2027; MTP3 total return ratio of 50% or more ([note][S7]).
- **China:** "approximately 19% of total sales". The China mix is 80-85% SoC. New fabs there could add business "around 2028-2029"; until then China stays at "20% level or lower" ([Q&A 29 Jul 2026][S12]).
- **Memory:** share "may experience a decline this year". Advantest is not the NAND incumbent, and speed and bandwidth transitions create "insertion opportunities that we have not fully captured" (same source).
- **Dual sourcing:** "we are staying ahead of that" ([Q&A 27 Apr 2026][S21]). Customers "prefer… a single supplier… efficient in terms of engineering resources and managing their installed base" ([fireside 12 Nov 2026][S11]).
- **Other:** a cybersecurity incident in February 2026 ([FY25 note][S17]).

### Inferences
- **2H margin:** about 50% points to margin normalising, driven by DRAM costs, before any volume slowdown.
- **Revenue concentration:** about 90% of SoC revenue is compute and communications, and over half of all revenue ships to Taiwan. Advantest's revenue therefore tracks a handful of US fabless AI programmes built at TSMC and its OSATs.

### Gaps
- No orders or backlog figure appears in any FY2025-26 document read. I could not verify when disclosure stopped.
- The identities of the ¥364.7bn of new "strategic investments" and the "investment fund" are not disclosed.
- No named customer shares.
- No Japanese 有報 was read.

---

## 3. Teradyne (TER): results, segments, position

### Takeaway
Teradyne is a smaller, lower-margin number two that has caught up with Advantest in memory and HBM. Its quarterly memory revenue is now about equal to Advantest's, and Korea is 32% of its revenue. It is broadening beyond compute, which was only about 20% of Q3'26 sales. Its compute share gains are company claims that depend on dual-vendor ramps in 2027.

### Cited Findings
- **Q3'26 (to 27 Sep 2026; reported 27-28 Oct 2026)** ([8-K][S22]; [10-Q][S23]; [slides][S4]):
  - Revenue $1,306.0m (Q2'26 $1,329.0m; Q3'25 $769.2m).
  - SoC $676.5m (+54%), memory $300.8m (+135%), IST $94.7m (+152%), Product Test $138.1m (+56%), Robotics $95.8m (+28%).
  - Non-GAAP: gross margin 59.1%; R&D 12.5%; SG&A 15.0%; operating margin 31.6%; EPS $2.29.
  - Inventory $575m; Q3 FCF $227m.
- **Prepared remarks (CFO Turner, CEO Smith, 28 Oct 2026)** ([remarks][S9]):
  - By segment: compute "grew nearly 50%"; auto and industrial up "nearly 90%" on data-centre power; mobile up 60% "from a low base".
  - Memory was driven by "HBM and DRAM… and a resurgence in NAND". IST's record came from HDD test at "all three major suppliers".
  - Product Test book-to-bill was 1.4x.
  - Mix: AI-driven revenue is ">60% of total revenue". "Outside of compute, the rest of our portfolio delivered close to 80%" of sales.
  - Investment: R&D plus capex "close to $1B" in 2026.
  - Q4 guidance: non-GAAP operating margin 28-30%.
  - Outlook: "2027… another year of healthy growth… strengthening backlog". An "updated target earnings model" comes on the Q4 call.
- **Dual vendor (company claims, unconfirmed):** the slides put a mature second vendor's "expected share range" at 30-70% ([slides][S4]). The status of each programme ([remarks][S9]):

  | Customer | Stage | Expected next step |
  |---|---|---|
  | First hyperscaler | Mature | Next major ramp mid-2027 |
  | Merchant GPU | Fast follower | More revenue in 2027 |
  | Second hyperscaler | Fast follower | Capacity buys 2H 2027 |
  | Third hyperscaler | Initial qualification | — |

- **Target earnings model (updated 3 Feb 2026; originally 2028)** ([slides][S4]; [Analyst Day][S5]):

  | Metric | 2025 actual | Target |
  |---|---|---|
  | ATE TAM | ~$9.0bn | $12-14bn |
  | Teradyne revenue | $3.2bn | ≈$6.0bn |
  | Gross margin | 58.3% | 59-61% |
  | Operating expenses | 36.0% | 27-29% |
  | Operating margin | 22.3% | 30-34% |
  | Non-GAAP EPS | $3.96 | $9.50-11.00 |

  The 2026 midpoint is already $5.2bn of revenue and $9.41 of EPS.
- **2025 (10-K; Q4 release 2 Feb 2026)** ([10-K][S24]; [Q4 release][S25]):
  - Revenue $3,190m (+13%): SoC $1,890m, memory $505m, IST $129m, Product Test $358m, Robotics $308m.
  - Semi Test was 79% of revenue. Q4'25 revenue was $1,083m.
  - FCF $450m; buybacks $709m ([slides][S4]).
- **Concentration:** five largest direct customers 44% (2025), 36% (2024), 32% (2023). One direct customer was 19%; specifiers drove 12% and 10% ([10-K][S24]).
- **Country** ([10-Q][S23]):
  - Q3'26: Korea 32%, China 21%, Taiwan 14%, Singapore 9%, US 8%.
  - Q3'25: Korea 12%, China 17%, Taiwan 37%.
  - 9M'26: Taiwan 32%, Korea 24%, China 15%.
- **Balance sheet and returns** ([10-Q][S23]):
  - Cash $460.7m plus securities $164.1m; the $200m drawn at end-2025 has been repaid; new $1.0bn revolver from 7 Aug 2026.
  - 9M'26 buybacks $173.5m (average price $349.62); dividends $61.0m; 156.12m shares outstanding.
- **Deals** ([10-Q][S23]):
  - Technoprobe: 10% for €483.1m (27 May 2024). Carrying value $518.6m against a fair value of $2,242.4m (27 Sep 2026).
  - FormFactor: $300m minority stake plus collaboration on "silicon photonics, high-performance compute, advanced packaging, and high-bandwidth memory", agreed 6 Oct 2026 and closing in Q4'26.
  - MultiLane JV: 75% for $157.8m (8 Apr 2026).
  - Quantifi Photonics: $127.2m (31 May 2025), "not material".
  - Infineon ATE team: €17.6m (31 Jan 2025).
  - TestInsight: 16 Apr 2026, price undisclosed ([release][S26]).
- **Exports:** compliance with the military-end-user rule "has impacted our ability to sell products to certain customers in China" ([10-K][S24]).
- **Memory share claim (Analyst Day, 11 Mar 2025):** Magnum is the "de facto standard". The memory slide shows "$500M" revenue, "$1.6B" memory ATE TAM and "50%" share, but the period is ambiguous in the extracted text. This **conflicts** with Advantest's own claim of a 63% memory share of a $1.9bn market in CY24. Both are company claims; definitions differ.

### Inferences
- **Memory:** Teradyne has reached about parity with Advantest in memory test, and Korea, which means HBM, is the swing factor.
- **Compute:** Teradyne compute was about $260m in Q3'26 (≈20% of $1,306m; derived), against Advantest SoC of ≈$2.2bn, about 90% of it compute. That suggests Advantest held well above 80% of the two firms' compute test revenue that quarter. Teradyne itself flags weak "second-half program timing in compute", so one quarter overstates the gap.

### Gaps
- No full Q&A transcript was available.
- Teradyne's own 2026 and 2027 TAM figures, beyond its slide on test's share of capex, were not found.

---

## 4. Stacked chips: how HBM and hybrid-bonded dies are tested

### Takeaway
Hybrid bonding in HBM has been **postponed**. JEDEC's 775 µm height limit lets 16-high HBM4 use microbumps, so each DRAM layer can still be tested before stacking. The access problem moves to HBM4E/HBM5 (18-20-high) at about 10 µm pitch, where probing damages bond pads ("testing is a particle source"). For logic chip-on-wafer modules, access is through C4 bumps only, with tens to hundreds of thousands of buried interconnects. Coverage therefore relies on DFT standards such as IEEE 1838 and on extra known-good insertions.

### Cited Findings
- **JEDEC and HBM4:** the HBM height limit rose from 720 to 775 µm. That allows 16-high HBM4 on microbumps; hybrid bonding is "postponed, not canceled", expected for HBM5 at the end of the decade (≥16-high, 4,096-bit, 4 TB/s) or perhaps 18-20-high HBM4E ([Semiconductor Engineering, 13 Jan 2026][S27]).
- **Pitch:** microbump pitch moves from about 40 µm toward about 10 µm for HBM4; hybrid bonding works to about 10 µm pad pitch.
- **Test under hybrid bonding:** UMC says it makes the flow "very difficult" and that "testing is a particle source"; probes can damage the pristine pad (same source).
- **SK hynix:** has reportedly completed validation of 12-high hybrid-bonded HBM (TrendForce, 29 Apr 2026, via search summary; not opened: [link][S28]).
- **Teradyne on chiplet modules** ([blog, 27 Jul 2026][S29]; company view):
  - Insertions now span "wafer level, singulated die, CoW module on interposer wafer tests, singulated CoW module tests, and final assembly".
  - At CoW, "electrical access is typically limited to C4 bump interfaces".
  - Interconnects number "tens or even hundreds of thousands", so "full coverage" is hard. UCIe links are "sensitive to signal integrity and electrostatic effects".
  - The industry needs IEEE 1838 DFT and new probe architectures.
- **Teradyne HBM tester:** Magnum 7H covers HBM2E to HBM4E, "from base-die wafer test to memory core test and burn-in". It tests at KGSD or chip-on-wafer level with probe cards, and post-singulation with bare-die handlers. Teradyne says it is "ramping at the largest HBM manufacturers" ([4 Aug 2025][S30]; company claim, unconfirmed). Magnum E2 for LPDDR6, DDR6, GDDR7 and NAND with PAM3 followed ([29 Sep 2026][S31]).
- **Teradyne known-good-die cell:** UltraFLEXplus with TEL's Prexa SDP singulated-device prober for 2.5D/3D packages, because "a single defective die can compromise the entire high-value package" ([8 Jun 2026][S32]).
- **Teradyne UCIe test:** UCIe streaming-scan test at wafer sort, behind the TSMC 3DFabric award ([Sep 2025][S33]).
- **Teradyne burn-in:** Titan HP holds each device at its target junction temperature under real workload ([6 Oct 2026][S34]).
- **Advantest memory hardware:**
  - T5801 DRAM tester: up to 36 Gbps PAM3 and 18 Gbps NRZ; "in use by strategic memory customers" ([12 Feb 2025][S35]).
  - M5241 handler with active thermal control: shipping from Q2 CY2026; "multiple major memory manufacturers are preparing for adoption" ([10 Dec 2025][S36]; company claims, unconfirmed).
  - Solutions "beyond HBM4" are planned ([27 Apr 2026][S14]).
- **Advantest die-level probing:** co-developing a die-level prober with Tokyo Seimitsu for heat in 2.5D/3D packages ([16 Dec 2025][S37]).
- **Advantest at ITC 2026:** ran a panel on "Test Flow Optimization End-to-End for 3D Advanced Packaging" ([13 Oct 2026][S38]).

### Inferences
- **Before HBM5:** until HBM5 or hybrid-bonded HBM4E, HBM test is pre-stack wafer and core test plus a post-stack KGSD performance test, not an untestable buried interface. Teradyne's "more stacks" argument and Korean suppliers' wafer and burn-in wins (section 5) sit in this regime.
- **At about 10 µm pitch:** the buried-interface problem shifts value toward DFT and BIST IP, metrology and inspection, and known-good-die insertions. That favours suppliers that own the full cell, including probing and handling.

### Gaps
- No roadmap statement from either firm specifically on test access below 25 µm hybrid-bond pitch.
- No quantified escape rate or untested-coverage figure.

---

## 5. Other tester suppliers (field scan; mostly secondary sources)

### Takeaway
On revenue scale, Chroma, Cohu and AEM plausibly matter at global top-15 level for "measure, inspect and test", though not all of their revenue is semiconductor test. Aehr and the Korean memory-test makers are niche but strategically placed. The Korean makers are capturing SK hynix's and Samsung's HBM4 and DRAM wafer-test and burn-in insertions. This is a comparison of scale, not a ranking.

### Cited Findings
- **Chroma ATE (2360.TW)** ([Quartr Q3 2026][S39]; [Quartr Q2 2026][S40]; [2Slides][S41]; secondary):
  - Q3 2026 (reported 29 Oct): sales NT$17.93bn; gross profit NT$10.31bn (≈57.5%); operating profit NT$7.17bn (≈40%); net income NT$5.78bn; EPS NT$13.34. 9M sales NT$43.3bn (+120%).
  - Q2: sales NT$13.53bn (+110%). Test Instruments & ATS +136%; Semiconductor +62%.
  - Legacy tester demand is guided up 10-20% for 2026. SLT and photonics are named growth drivers. Order visibility runs into 2027, and "orders… from Google and Nvidia" were cited, segment unclear.
  - Growth rates conflict across summaries. Digitimes linked the Q1 record to AI-server power supplies, SLT and photonics ([4 May 2026][S42]).
  - The semiconductor share of revenue could not be verified.
- **Cohu (COHU)** ([Ariva copy of release][S43]; [Quartr][S44]; [Panabee][S45]; secondary):
  - Q3 2026: revenue $173.0m (+37%); GAAP EPS $0.22; non-GAAP $0.43; non-GAAP gross margin 45.7%; bookings +126%.
  - Q4 guidance about $178m ±$7m. FY26 revenue +38%.
  - Products: handlers, interface and contactors, testers, AI-based HBM inspection, and the first volume licence for prescriptive-maintenance software.
  - A $330m HBM and advanced-packaging inspection SAM comes from a single summary (unverified). Demo systems go to a US IDM in Q1 2027.
- **Aehr Test Systems (AEHR)** ([8-K Ex. 99.1, 2 Nov 2026][S46]; [release copy][S47]):
  - Q1 FY27 (to 25 Sep 2026): revenue $33.0m (+200%); GAAP net income $7.2m; bookings $46.7m.
  - Effective backlog $109.3m (1 Nov). FY27 guidance raised to $150m, with non-GAAP net income of at least 20%.
  - Sonoma burn-in shipments run at 12 systems a month for a lead hyperscaler's AI processor. Its second AI processor is qualified, with a ramp in CY2027.
  - This is a burn-in niche (wafer-level for silicon carbide, package-level for AI).
- **AEM Holdings (AWX.SI)** ([Quartr H1 2026][S48]; [Quartr Q1 2026][S49]; [iTiger FY2025][S50]; secondary):
  - 1H26 revenue S$247.2m (+30%); net profit S$30.8m. FY26 guidance raised to S$630-680m (from S$550-600m; S$460-510m in February). FY25: S$399.3m revenue, S$17.1m profit.
  - Test Cell Solutions (SLT and burn-in) was 75% of Q1 revenue. A second, fabless AI/HPC customer is expected to be the largest in FY26; a memory ramp begins 2H26.
- **Emerson (NI)** ([19 Mar 2025][S51]):
  - Its Test & Measurement arm partners with Advantest on "semiconductor product analytics, algorithm development, and data management" for edge decisions.
  - NI's own semiconductor test revenue could not be verified.
- **Korean memory test** (Korean-press summaries via search: [dealsite 170288][S52], [167256][S53], [166024][S54], [165257][S55], [167793][S56], [SPTA Times 25 Aug 2026][S57]; individual figures not mapped to articles and **not verified against DART**):
  - **DI and its subsidiary Digital Frontier:** SK hynix HBM4 wafer-tester contracts of ₩99.8bn (Jan 2026) and ₩96.3bn (Mar 2026); Samsung DDR5 and NAND burn-in tester orders.
  - **UniTest:** passed SK hynix's HBM4 burn-in mass-production qualification (Feb 2026); ₩29.2bn HBM4 wafer burn-in contract (May 2026); Q2 operating profit ₩7.9bn. Reported combined SK hynix HBM4 wafer-test orders for Digital Frontier and UniTest in 2026: ₩283.9bn.
  - **YC:** Samsung wafer-tester contracts of ₩174.6bn in H1 2026, DRAM-led.
  - **Exicon:** Samsung CLT and SSD tester contracts of ₩30.2bn (Mar) and ₩49.85bn (Jul); HBM inspection gear in development.
  - **Neosem:** ₩8.6bn CLT tester contract with Samsung.
- **Other context:** Teradyne's 10-K names SPEA (Italy) and Cohu as competitors, plus "emerging Asian companies" and in-house supply at customers.

### Inferences
- **Insertion split:** Korean suppliers cluster in wafer test, burn-in and SSD/CLT insertions at domestic memory makers. Advantest and Teradyne keep high-speed core and final performance test. That fits Advantest's admission that it has not captured some memory insertions.

### Gaps
- Japanese niche testers (for example TESEC and Shibasoku) were not researched.
- DART and MOPS primary filings were not opened.
- No Korean supplier's full-year revenue was verified.

---

## 6. Path-forward detail (supporting A3)

- **PDF Solutions: Advantest has exited.**
  - Advantest America sold 3,306,924 PDF Solutions shares at $44 in an upsized offering that closed around 15 May 2026. A Schedule 13G/A shows Advantest at 0% (event date 15 May 2026). These details come from search summaries of the [PDF Solutions pricing release][S58] and the [SEC 13G/A][S59].
  - Before the sale the stake was ≈8.4% ([Simply Wall St][S60]; undated).
  - This is consistent with Advantest's ¥22.1bn "proceeds from the sale of held shares", "made in light of our broader strategic priorities" ([Jul 2026 note][S6]).
  - Whether the Exensio-based cloud partnership of July 2020 continues could not be verified ([2020 release][S61]).
- **Advantest software and automation:** [ACS RTDI/NVIDIA, 6 Oct 2025][S62]; [Velocity/AllianceATE, 18 May 2026][S63]; [SiConic DFT, 16 Jul 2026][S64]; [SmarTest 8 and ITC, 13 Oct 2026][S38]; [Pin Scale 5000B, 22 Apr 2026][S65].
- **Advantest probe-card partners:** [Technoprobe and FormFactor stakes, 9 Jan 2025][S66]; [MJC, 27 Feb 2025][S67].
- **Advantest: "Distribution of test"** across engineering, sort, hot and cold package test, burn-in and SLT ([fireside 17 Nov 2025][S13]).
- **Advantest silicon photonics:** first large high-volume ATE order received ([Apr 2026 slides][S3]). The market should "more than double" next year ([Q&A 27 Apr 2026][S21]). OpenLight partnership (23 Jun 2026; title only).
- **Teradyne silicon photonics:** Photon 100 opto-electric platform for wafer, optical engine and CPO module insertions ([17 Mar 2026][S68]). Quantifi photonic-IC test ([10 Mar 2025][S69]).
- **Teradyne compute instruments:** UltraPin5000-EM ("up to 80 times more vector memory than other market offerings" in the [1 Sep 2026 release][S70], but "than our current instrument" in the 28 Oct prepared remarks, an internal inconsistency); UltraVS64-HP (up to 15,000 A); UltraPort-PCIe6.

---

## 7. Entry-point data (separate from quality)

- **Snapshot:** see table A4 for prices and multiples.
- **Implied forward EPS (my calculation from stockanalysis forward P/E; period basis not stated):**
  - Advantest ≈¥1,226, about +19% on FY26 guidance of ¥1,027.
  - Teradyne ≈$10.61, about +13% on the 2026 midpoint of $9.41.
- **Price path:**
  - Teradyne fell from $324.95 before its results to $303.65 after ([StockStory][S10]) and now stands at $265.78. That is about 24% below the $349.62 average price of its own 2026 buybacks ([10-Q][S23]).
  - Advantest fell 4.6% on 12 Nov 2026, the day of its supply-chain fireside chat ([stockanalysis][S1]).
- **Cycle position:**
  - Both companies are at record revenue.
  - Advantest's tester market is up about 50% a year for three years. Teradyne has held $1.3bn quarters three times running ("high watermark").
  - On SEMI data, test's share of capex is 8.1% so far in 2026, against 6.4% in 2025.
  - Teradyne's 2026 results already approach its target model.
  - Advantest says "There will be downward cycles, and we know how to manage them" ([12 Nov 2026][S11]).
- **Near-term catalysts:**
  - Advantest: January 2027 CY27 TAM and capacity update; MTP4 around May 2027.
  - Teradyne: new target model in early 2027 and dual-vendor capacity buys in 2H 2027.
  - Either: DRAM-cost pass-through, and any US or Japanese export-control change on China, where Advantest has ≈19% of sales and Teradyne 15-21%. No pending decision was found.
- **Gaps:** I could not verify each company's 5-10 year valuation range or any consensus revenue growth series.

## 8. Could not verify
- **Advantest:** orders and backlog; named customers and their shares; what the ¥433bn of "strategic investment" securities are; whether the PDF Solutions partnership continues after the share sale; any 有報 customer disclosure.
- **Independent market data:** third-party (TechInsights, Gartner, Yole, SEMI) tester market sizes and vendor shares for 2024-27.
- **Teradyne:** its memory-share claim (period ambiguous; it conflicts with Advantest's claim); TestInsight's price; any analytics or inference product; full call Q&A.
- **Product and roadmap claims:** any ATE product that reports a stated uncertainty; roadmap statements on test access below 25 µm pitch; post-2030 views on insertions.
- **Other suppliers:**
  - Chroma's semiconductor share of revenue and its exact growth rates.
  - Cohu's $330m SAM.
  - AEM figures against SGX filings.
  - All Korean contract amounts against DART.
  - Japanese niche testers and Emerson/NI test revenue.
- **Valuation:** 5-10 year valuation history; consensus growth beyond the implied forward EPS.


## 9. Sources (numbered; each citation [..][Sn] in the text points here; title gives publisher, document and date)

Primary company documents dominate; "secondary" marks aggregators and press summaries, and "via search summary" marks pages I did not open myself.

[S1]: https://stockanalysis.com/quote/tyo/6857/statistics/ "stockanalysis.com, Advantest (TYO:6857) statistics, data as of 12 Nov 2026 close"
[S2]: https://stockanalysis.com/stocks/ter/statistics/ "stockanalysis.com, Teradyne statistics, price at 11 Nov 2026 close (page updated 12 Nov 2026)"
[S3]: https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_260427_slide.pdf "Advantest FY2025 results presentation slides, 27 Apr 2026"
[S4]: https://d1io3yog0oux5.cloudfront.net/_63807b868d65ded682f4017b286091b2/teradyne/db/938/9658/presentation/Teradyne_Q3%2726_Earnings_Presentation.pdf "Teradyne Q3 2026 earnings presentation, 28 Oct 2026"
[S5]: https://d1io3yog0oux5.cloudfront.net/_63807b868d65ded682f4017b286091b2/teradyne/db/919/9566/pdf/ALL_Analyst_Day_2025_IR_SITE_NEW.pdf "Teradyne Financial Analyst Day deck, 11 Mar 2025"
[S6]: https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_260729_note.pdf "Advantest Q1 FY2026 briefing note, 29 Jul 2026"
[S7]: https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_261028_note.pdf "Advantest Q2 FY2026 briefing note, 28 Oct 2026"
[S8]: https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_261028_QA.pdf "Advantest Q2 FY2026 briefing Q&A summary, 28 Oct 2026"
[S9]: https://d1io3yog0oux5.cloudfront.net/_63807b868d65ded682f4017b286091b2/teradyne/db/938/9658/webcast_transcript/Teradyne_Q3%2726_Earnings_Prepared_Remarks.pdf "Teradyne Q3 2026 earnings call prepared remarks (Smith, Turner), 28 Oct 2026"
[S10]: https://stockstory.org/us/stocks/nasdaq/ter/news/earnings-call/teradynes-q3-earnings-call-our-top-5-analyst-questions "StockStory, Teradyne Q3 2026 call: top 5 analyst questions, late Oct 2026 (secondary)"
[S11]: https://www.advantest.com/document/en/investors/ir-library/briefing/JE_IR%20Fireside_Chat_Script_20261112.pdf "Advantest IR Fireside Chat script (Lefever, Junger), 12 Nov 2026"
[S12]: https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_260729_QA.pdf "Advantest Q1 FY2026 briefing Q&A summary, 29 Jul 2026"
[S13]: https://www.advantest.com/document/en/investors/ir-library/briefing/JE_IR%20Fireside_Chat_Script_20251117.pdf "Advantest IR Fireside Chat script (Lefever, Serrer), 17 Nov 2025"
[S14]: https://www.advantest.com/document/en/investors/ir-library/result/JE_Sell-Side%20Analyst%20Small%20Group%20Meeting_260427_QA.pdf "Advantest sell-side analyst small group meeting Q&A, 27 Apr 2026"
[S15]: https://docs.wing.vc/content/the-chip-testing-bottleneck "Wing VC newsletter, 'The Chip Testing Bottleneck', undated (weak secondary)"
[S16]: https://www.advantest.com/document/en/investors/ir-library/result/E_FR_FY2025_FN.pdf "Advantest FY2025 consolidated financial results (English 決算短信), 27 Apr 2026"
[S17]: https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_260427_note.pdf "Advantest FY2025 briefing note, 27 Apr 2026"
[S18]: https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_261028_slide.pdf "Advantest Q2 FY2026 briefing slides, 28 Oct 2026"
[S19]: https://www.advantest.com/en/news/2026/mpd9kn0000000gii-att/E_FR_FY2026_2Q.pdf "Advantest FY2026 Q2 (semi-annual) consolidated financial results (English 決算短信), 28 Oct 2026"
[S20]: https://www.advantest.com/en/news/2025/g2l53r0000000ofm-att/E_Info_20251028_01.pdf "Advantest, revision of MTP3 targeted management metrics, 28 Oct 2025"
[S21]: https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_260427_QA.pdf "Advantest FY2025 briefing Q&A summary, 27 Apr 2026"
[S22]: https://www.sec.gov/Archives/edgar/data/0000097210/000119312526434981/ter-ex99_1.htm "Teradyne Q3 2026 results press release, Form 8-K Ex. 99.1, 27 Oct 2026"
[S23]: https://investors.teradyne.com/sec-filings/all-sec-filings/content/0001193125-26-441091/ter-20260927.htm "Teradyne Form 10-Q for the quarter ended 27 Sep 2026"
[S24]: https://investors.teradyne.com/sec-filings/all-sec-filings/content/0001193125-26-059002/ter-20251231.htm "Teradyne Form 10-K for the fiscal year ended 31 Dec 2025"
[S25]: https://investors.teradyne.com/news-events/press-releases/detail/433/teradyne-reports-fourth-quarter-and-full-year-2025-results "Teradyne Q4 and full-year 2025 results release, 2 Feb 2026"
[S26]: https://investors.teradyne.com/news-events/press-releases/detail/439/teradyne-acquires-testinsight-accelerating-time-to-market-for-ai-and-data-center-devices "Teradyne acquires TestInsight, release, 16 Apr 2026"
[S27]: https://semiengineering.com/hbm4-sticks-with-microbumps-postponing-hybrid-bonding/ "Semiconductor Engineering (B. Moyer), 'HBM4 Sticks With Microbumps, Postponing Hybrid Bonding', 13 Jan 2026"
[S28]: https://www.trendforce.com/news/2026/04/29/news-sk-hynix-reportedly-completes-12-high-hybrid-bonding-hbm-validation-works-to-raise-yields-for-mass-production/ "TrendForce, SK hynix reportedly completes 12-high hybrid-bonding HBM validation, 29 Apr 2026 (seen via search summary only)"
[S29]: https://www.teradyne.com/2026/07/27/ai-chiplet-architectures-redefining-test-insertions/ "Teradyne blog (J. Hurtarte), 'AI Chiplet Architectures Redefining Test Insertions', 27 Jul 2026"
[S30]: https://investors.teradyne.com/news-events/press-releases/detail/419/teradyne-unveils-magnum-7h---the-next-generation-memory-tester-for-high-bandwidth-memory-devices "Teradyne Magnum 7H HBM tester release, 4 Aug 2025"
[S31]: https://investors.teradyne.com/news-events/press-releases/detail/451/teradyne-announces-magnum-e2-to-address-next-generation-memory-test-demands-driven-by-ai-and-high-performance-computing "Teradyne Magnum E2 release, 29 Sep 2026"
[S32]: https://investors.teradyne.com/news-events/press-releases/detail/443/teradyne-introduces-integrated-test-solution-for-ai-and-data-center-devices-in-collaboration-with-tokyo-electron "Teradyne and Tokyo Electron integrated KGD test cell release, 8 Jun 2026"
[S33]: https://investors.teradyne.com/news-events/press-releases/detail/422/teradyne-awarded-2025-tsmc-open-innovation-platform-oip-partner-of-the-year-for-tsmc-3dfabric-testing "Teradyne 2025 TSMC OIP Partner of the Year (3DFabric testing) release, Sep 2025 (forum 24 Sep 2025)"
[S34]: https://investors.teradyne.com/news-events/press-releases/detail/452/teradyne-introduces-titan-hp-platform-with-burn-in-capabilities-for-advanced-ai-data-center-devices "Teradyne Titan HP burn-in release, 6 Oct 2026"
[S35]: https://www.advantest.com/en/news/2025/20250212.html "Advantest T5801 DRAM test system release, 12 Feb 2025"
[S36]: https://www.advantest.com/en/news/2025/20251210.html "Advantest M5241 memory handler release, 10 Dec 2025"
[S37]: https://www.advantest.com/en/news/2025/20251216.html "Advantest and Tokyo Seimitsu die-level prober release, 16 Dec 2025"
[S38]: https://www.advantest.com/en/news/2026/20261013.html "Advantest ITC 2026 showcase release (SmarTest 8, SiConic, Velocity), 13 Oct 2026"
[S39]: https://quartr.com/events/chroma-ate-inc-2360-q3-2026_F9Dy1A80 "Quartr, Chroma ATE Q3 2026 earnings summary, ~29 Oct 2026 (secondary, AI-generated)"
[S40]: https://quartr.com/events/chroma-ate-inc-2360-q2-2026_F9Dy1LPA "Quartr, Chroma ATE Q2 2026 earnings summary, 2026 (secondary)"
[S41]: https://2slides.com/et/gallery/chroma-ate-q3-2026-earnings-presentation "2Slides, Chroma ATE Q3 2026 earnings presentation summary, Oct 2026 (secondary)"
[S42]: https://www.digitimes.com/news/a20260504PD202.html "Digitimes, Chroma record revenue on SLT and photonics demand, 4 May 2026 (paywalled; headline only)"
[S43]: https://www.ariva.de/news/cohu-reports-third-quarter-2026-results-12185729 "Ariva, copy of 'Cohu Reports Third Quarter 2026 Results', late Oct 2026"
[S44]: https://quartr.com/events/cohu-cohu-q3-2026_3sZvAMqA "Quartr, Cohu Q3 2026 earnings summary, late Oct 2026 (secondary)"
[S45]: https://www.panabee.com/news/cohu-earnings-q3-2026 "Panabee, Cohu Q3 2026 results, late Oct 2026 (secondary)"
[S46]: https://www.sec.gov/Archives/edgar/data/0001040470/000165495426009385/aehr_ex991.htm "Aehr Test Systems Form 8-K Ex. 99.1, Q1 FY2027 results, 2 Nov 2026"
[S47]: https://finviz.com/news/413485/aehr-test-systems-reports-record-first-quarter-fiscal-2027-revenue-of-330-million-raises-full-year-revenue-outlook-to-150-million-triple-fiscal-2026-revenue "Finviz, copy of Aehr Q1 FY2027 results release, Nov 2026"
[S48]: https://quartr.com/events/aem-holdings-awx-h1-2026_F1UnzA2V "Quartr, AEM Holdings H1 2026 summary, ~12 Aug 2026 (secondary)"
[S49]: https://quartr.com/events/aem-holdings-ltd-awx-q1-2026_F1UnzADz "Quartr, AEM Holdings Q1 2026 summary, 2026 (secondary)"
[S50]: https://www.itiger.com/news/1160016247 "iTiger, AEM FY2025 revenue and profit, early 2026 (secondary)"
[S51]: https://www.advantest.com/en/news/2025/20250319.html "Advantest and Emerson AI-driven test ecosystem partnership release, 19 Mar 2025"
[S52]: https://dealsite.co.kr/articles/170288 "dealsite.co.kr article 170288, 2026 (Korean; via search summary)"
[S53]: https://dealsite.co.kr/articles/167256 "dealsite.co.kr article 167256, 2026 (Korean; via search summary)"
[S54]: https://dealsite.co.kr/articles/166024 "dealsite.co.kr article 166024, 2026 (Korean; via search summary)"
[S55]: https://dealsite.co.kr/articles/165257 "dealsite.co.kr article 165257, 2026 (Korean; via search summary)"
[S56]: https://dealsite.co.kr/articles/167793 "dealsite.co.kr article 167793, 2026 (Korean; via search summary)"
[S57]: https://www.sptatimeskorea.com/post/%EC%A0%9C20260825-te-01%ED%98%B8-2026%EB%85%84-8%EC%9B%94-25%EC%9D%BC-%EB%B0%98%EB%8F%84%EC%B2%B4-%EC%9E%A5%EB%B9%84-%EA%B4%80%EB%A0%A8-%EC%A3%BC%EC%9A%94-%EB%89%B4%EC%8A%A4-%EC%9A%94%EC%95%BD "SPTA Times Korea, semiconductor equipment news digest, 25 Aug 2026 (Korean; via search summary)"
[S58]: https://www.pdf.com/resources/pdf-solutions-announces-pricing-of-an-upsized-public-offering-of-common-stock/ "PDF Solutions, pricing of upsized public offering (Advantest America selling 3,306,924 shares at $44), May 2026 (via search summary)"
[S59]: https://www.sec.gov/Archives/edgar/data/0001120914/000119312526242623/primary_doc.xml "SEC Schedule 13G/A on PDF Solutions filed for Advantest, event date 15 May 2026 (via search summary)"
[S60]: https://simplywall.st/stocks/us/semiconductors/nasdaq-pdfs/pdf-solutions/ownership "Simply Wall St, PDF Solutions ownership page, undated"
[S61]: https://www.advantest.com/en/news/2020/20200730.html "Advantest and PDF Solutions partnership / private placement release, 30 Jul 2020"
[S62]: https://www.advantest.com/en/news/2025/2025100602.html "Advantest ACS RTDI with NVIDIA machine learning release, 6 Oct 2025"
[S63]: https://www.advantest.com/en/news/2026/20260518.html "Advantest Velocity (AllianceATE) and V93000 integration release, 18 May 2026"
[S64]: https://www.advantest.com/en/news/2026/20260716.html "Advantest SiConic DFT engineering environment release, 16 Jul 2026"
[S65]: https://www.advantest.com/en/news/2026/20260422.html "Advantest Pin Scale 5000B release, 22 Apr 2026"
[S66]: https://www.advantest.com/en/news/2025/20250109.html "Advantest minority investments in Technoprobe and FormFactor release, 9 Jan 2025"
[S67]: https://www.advantest.com/en/news/2025/20250227.html "Advantest and Micronics Japan partnership release, 27 Feb 2025"
[S68]: https://investors.teradyne.com/news-events/press-releases/detail/436/teradyne-introduces-photon-100 "Teradyne Photon 100 release, 17 Mar 2026"
[S69]: https://investors.teradyne.com/news-events/press-releases/detail/10/teradyne-to-acquire-quantifi-photonics "Teradyne to acquire Quantifi Photonics release, 10 Mar 2025"
[S70]: https://investors.teradyne.com/news-events/press-releases/detail/447/teradyne-launches-advanced-ultraflexplus-instruments-engineered-for-ai-and-data-center-computing-devices "Teradyne UltraFLEXplus AI instruments release, 1 Sep 2026"
[S71]: https://www.advantest.com/en/news/2026/20260514.html "Advantest release on TechInsights 2026 Customer Satisfaction Survey results, 14 May 2026"
[S72]: https://www.advantest.com/en/news/2025/20251224.html "Advantest wins TSMC 2025 Supply Chain Management Forum Excellent Performance Award (title seen in news index), 24 Dec 2025"
[S73]: https://www.advantest.com/en/news/2026/20260723.html "Advantest: R&I upgrades issuer rating to AA- (title seen in news index), 23 Jul 2026"
[S74]: https://www.advantest.com/en/news/2026/20260623.html "Advantest partners with OpenLight on silicon photonics test (title seen in news index), 23 Jun 2026"
[S75]: https://www.advantest.com/en/news/2026/20260421.html "Advantest strategic partnership with Applied Materials, joins EPIC (title seen in news index), 21 Apr 2026"

Tooling note: the Firecrawl scraping tool ran out of credits during this research (allowance resets 13 Nov 2026).
