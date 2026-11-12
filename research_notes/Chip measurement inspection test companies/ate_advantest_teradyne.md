# Automatic test equipment (ATE) for chip electrical test: Advantest, Teradyne and the wider tester field

Research date: **12 November 2026**. Every figure carries its date and source. Statements no outside party has confirmed are marked **"company claim, unconfirmed"**. Quality evidence (sections A1-A3, 1-6) is kept apart from entry-point data (A4, section 7).

**Status: v1, written after an interruption.** Sections marked **[INCOMPLETE]** are still being filled.

**Coverage.** I read these primary documents in full:
- Advantest: the English 決算短信 for FY2025 (year to March 2026) and H1 FY2026; the results notes, slides and Q&A for April, July and October 2026; the April 2026 sell-side meeting Q&A; the fireside-chat scripts of 17 November 2025 and 12 November 2026; Integrated Annual Report 2026; and the revision of the MTP3 targets.
- Teradyne: the Q3 2026 earnings release (8-K Ex. 99.1), the Q3 2026 10-Q and the 2025 10-K.

I could not open a full Teradyne Q3 2026 call transcript. The call commentary below comes from third-party summaries and is labelled as such. I did not read the Japanese 有価証券報告書.

---

## A. Evidence tables

### A1. Advantest (6857.T, Tokyo Prime) — quality tests a-e

| Test | Dated evidence | Source |
|---|---|---|
| (a) Position | Supplies the production test that decides ship or scrap for most AI compute. The V93000 platform covers GPU, custom ASIC, CPU, networking and silicon photonics. Advantest calls V93000 "increasingly regarded as an industry standard in HPC" (company claim, unconfirmed; 28 Oct 2026). It sells the whole test cell: testers, handlers (M5241 for memory), device interfaces, system-level test (7038) and die-level probing in development. **Data access:** ACS RTDI real-time data infrastructure, which NVIDIA "selected for high-volume production" for Blackwell and later parts (announced by Advantest, 6 Oct 2025). | Q&A 28 Oct 2026; news 6 Oct 2025, 10 Dec 2025 |
| (b) Lead | **Market share (company estimate):** SoC tester share 59% (CY23), 56% (CY24), 66% (CY25); memory 56%, 63%, 61%; overall 58%, 58%, 65%. Advantest also claims a "majority share of the global AI accelerator business" and sees "a path to above 70%" (company claim, unconfirmed). **Outside evidence:** TechInsights 2026 customer-satisfaction survey, global #1 for the 7th year running (14 May 2026); TSMC "Excellent Performance Award", 2025 Supply Chain Management Forum (24 Dec 2025); R&I raised its rating to AA- (23 Jul 2026). Cross-check from filings: in Jul-Sep 2026, Advantest SoC sales of ¥353.3bn (≈$2.19bn at ¥161) were about 3.2x Teradyne's SoC revenue of $676.5m, about 76% of the two firms combined. No Gartner, TechInsights or Yole share figure found yet [INCOMPLETE]. | FY25 slides 27 Apr 2026; Q&A 28 Oct 2026; TER 10-Q Q3'26 |
| (c) Revenue model | **FY2025:** Test Systems ¥1,019.4bn (90.3%), of which SoC ¥767.4bn, memory ¥171.5bn and other systems (handlers, interfaces, SLT) ¥80.5bn. Services & Others ¥109.2bn (9.7%): support services plus consumables (test interface boards) plus mask CD-SEM. **FY2026 forecast:** Services & Others ¥148.5bn, 8.0% of ¥1,863bn. Licensing revenue on testers exists and was cited as a margin driver (Apr and Oct 2026), but is not disclosed separately. No revenue line depends on labour hours or seats. Of 7,241 employees (FY2025), 1,085 are system or application engineers. | 決算短信 FY2025; slides 28 Oct 2026; IAR 2026 |
| (d) Financial strength | **FY2025:** sales ¥1,128.6bn (+44.7%); gross margin ≈64.3%; operating margin 44.2%; ROE 57.6%; ROIC 54.4% (company definition); operating cash flow ¥335.2bn; FCF ≈¥300.6bn. **H1 FY2026:** sales ¥845.2bn (+60.5%); gross margin 70.4%; operating margin 54.0% (Q2: 71.1% and 55.9%). Cash ¥401.8bn against ¥89.5bn of convertible bonds; investment securities ¥432.6bn; equity ratio 66.1% (30 Sep 2026). **Customers:** "a small number of top customers account for a substantial portion of net sales"; no names or shares disclosed. **Country (ship-to), FY2025:** Taiwan 50.5%, China 18.9%, Korea 16.0%. **H1 FY2026** (read from chart labels): Taiwan ≈52%, China ≈19%, Korea ≈16%. Management puts China at "approximately 19%… consistent around 20%" (29 Jul 2026). | 決算短信 FY25 & H1 FY26; slides; IAR 2026; Q&A 29 Jul 2026 |
| (e) Resilience | **Cycle:** tester market CY23 $4.4bn, CY24 $6.0bn, CY25 $9.0bn, CY26e ≈$14.25bn (company estimates); management calls it a "megacycle". **Shock absorbers:** EMS-based "variable-cost model"; strategic inventory (¥352.4bn, up from ¥231.7bn in March 2026); platforms that last 10-15 years. **Exposure:** SoC capacity going from 5,000 to 10,000 a year (possibly 20,000), which risks overbuild if demand pauses; DRAM component costs. **Sensitivities:** operating profit moves ¥5.8bn per ¥1 change against the dollar; China ≈19% of sales. Advantest is not a US company; contrast Teradyne's 10-K statement that rivals are "not subjected to the same restrictions". | slides/Q&A Oct 2026; fireside 12 Nov 2026 |

### A2. Teradyne (TER, Nasdaq) — quality tests a-e

| Test | Dated evidence | Source |
|---|---|---|
| (a) Position | Number-two SoC tester (UltraFLEXplus, J750) and HBM/DRAM tester (Magnum 7H), plus system-level test and burn-in (Titan HP), HDD/SSD test, board test (Product Test) and robotics. Teradyne holds a 10% equity-method stake in Technoprobe (probe cards; board seat) and agreed a $300m minority stake in FormFactor (6 Oct 2026), so it is positioning at the wafer and probe interface. | 10-Q Q3'26; 10-K 2025 |
| (b) Lead | The memory lead is real in the current quarter: Q3'26 memory revenue was a record $300.8m, the fourth quarter running above $200m. That roughly equals Advantest's memory-tester sales of ¥53.4bn (≈$332m) in the same quarter. Advantest itself warned on 29 Jul 2026 that its memory share "may experience a decline this year". In compute, Teradyne says it is gaining share (Q3 call, StockStory summary; company claim, unconfirmed). **Outside evidence:** TSMC 2025 OIP Partner of the Year for 3DFabric testing (2025, as announced by Teradyne). No third-party share figure found [INCOMPLETE]. | 10-Q Q3'26; Advantest Q&A Jul 2026 |
| (c) Revenue model | **Q3'26 product mix:** SoC $676.5m, memory $300.8m, IST (SLT/storage) $94.7m, Product Test $138.1m, Robotics $95.8m. Services revenue $141.8m (10.9%); 9M'26 $419.0m (10.7%), with services gross margin ≈65%. Of revenue, 91.4% is recognised at a point in time. No seat or hours model. | 10-Q Q3'26 |
| (d) Financial strength | **Q3'26:** revenue $1,306.0m (+70%); GAAP gross margin 59.1%; operating margin 30.8% GAAP, 31.6% non-GAAP; non-GAAP EPS $2.29. **9M'26:** operating cash flow $1,047.9m, capex $241.8m, FCF $806.1m. Cash plus securities $624.8m; debt $0 (it was $200m at year-end 2025); new $1.0bn revolver. **Concentration:** the five largest direct customers were 44% of 2025 revenue (36% in 2024, 32% in 2023). One direct customer was 19%; two "specifying" customers drove 12% and 10%. **Country, Q3'26:** Korea 32%, China 21%, Taiwan 14%, Singapore 9%, US 8%. **9M'26:** Taiwan 32%, Korea 24%, China 15%. | 8-K 27 Oct 2026; 10-Q; 10-K |
| (e) Resilience | **Cycle:** 2025 revenue ≈$3.19bn (derived from 10-K growth rates) and 2026 ≈$5.22bn (9M plus Q4 guidance midpoint), about +63%. Management guides 2027 growth (each quarter above the same quarter of 2026, per Quartr summary). **Exports:** the US military-end-user rule has curbed China sales. **Diversifiers:** robotics, now back in profit, at 7% of revenue, and Product Test at 11%. Mobile is "under pressure". Inventory days rose to 98 from 69 on longer component lead times (StockStory). | 10-K 2025; 10-Q; StockStory |

### A3. Six transitions — what each company said versus did (dated)

| Transition | Advantest: said | Advantest: did | Teradyne: said / did |
|---|---|---|---|
| (1) Pass/fail to inference from data with stated uncertainty | "ACS RTDI moves testing from validation to prediction" (6 Oct 2025). CTO: the job is "not just go, no go… trim and calibrate every device"; chiplet "power pairing" (17 Nov 2025). | ACS RTDI with NVIDIA ML in high-volume production (Oct 2025). Emerson partnership for edge AI analytics, re-binning and adaptive test (19 Mar 2025). PDF Solutions Exensio-powered cloud and equity stake (Jul 2020). Pin Scale 5000B adds vector memory "for analytics of failure data" (22 Apr 2026). No product found that outputs a stated uncertainty. | [INCOMPLETE]: no analytics or inference product evidence read yet |
| (2) Hand-written programs to AI-built programs | SmarTest 8 "AI-enabled tools for test program development" (13 Oct 2026). "Automation of Test" is an MTP3 theme. Agentic AI in internal use (Jul 2026). | Acquired AllianceATE in Sep 2025. Its Velocity tool streams design files into V93000 for "first-time-right" patterns, cutting "weeks of developing custom code" (18 May 2026; Arm quoted). SiConic bench ecosystem (Feb 2025), extended to DFT on 16 Jul 2026. | Acquired TestInsight in 2026 (press release #439) [INCOMPLETE: details] |
| (3) Single die to bonded stacks and packages | Test content rises with 3D packaging: "test times increase by multiples from one generation to the next" (12 Nov 2026; company claim, unconfirmed). "Die level probing will need to come" (CTO, Nov 2025). Plans memory test "beyond HBM4" (Apr 2026). | Die-level prober co-developed with Tokyo Seimitsu (16 Dec 2025). Minority stakes and partnerships with Technoprobe (2.5%), FormFactor and MJC (Jan-Feb 2025). M5241 memory handler shipping Q2 CY2026. T5801 DRAM tester (36 Gbps PAM3). Applied Materials EPIC (21 Apr 2026). | Magnum 7H for HBM (2025). TSMC 3DFabric award (2025). Titan HP with burn-in (2026). Integrated solution with Tokyo Electron (2026). Technoprobe 10% (May 2024). FormFactor $300m (Oct 2026). [INCOMPLETE: details] |
| (4) Hardware to software and data | Goal is to "evolve from a test equipment company into a comprehensive solutions provider" (29 Jul 2026). | Services & Others is still under 10% of sales (FY2025 9.7%; FY26e 8.0%). Software and analytics revenue is not disclosed. Investment securities rose ¥364.7bn in H1 FY26 as "strategic investments", target undisclosed. | Services ≈11% of revenue (Q3'26). |
| (5) AI on the chipmaker's premises | Emerson/ACS: "pushing… compute and analysis capabilities to the edge, closer to the equipment" (Mar 2025). ACS RTDI "securely supporting AI/ML-driven test automation" at HVM sites (Oct 2025). | Deployed at "high-volume production sites worldwide" (company claim, unconfirmed). | [INCOMPLETE] |
| (6) Fewer insertions or testers per device after 2030 | New modules can cut some test items' time, but "we do not believe that these reductions… will impact overall demand" (27 Apr 2026). After 2-3 years of new-system demand an upgrade cycle may follow (27 Apr 2026). "Distribution of test" lets customers move content between insertions (Nov 2025, IAR 2026). | No post-2030 statement found. | No statement found |

### A4. Entry-point snapshot (separate from quality)

| Item | Advantest (6857.T) | Teradyne (TER) |
|---|---|---|
| Price, market cap, date | [INCOMPLETE] | $265.78 (close 11 Nov 2026); market cap $41.49bn; EV $41.01bn (stockanalysis.com, updated 12 Nov 2026) |
| P/E, EV multiples | [INCOMPLETE] | Trailing P/E 30.5; forward P/E 25.1; EV/sales 8.2; EV/EBITDA 23.2; EV/FCF 40.0 |
| Guidance | FY2026 (to Mar 2027) sales ¥1,863bn, operating profit ¥967bn (51.9%), net income ¥741.5bn, EPS ¥1,027.08. Raised twice: April ¥1,420bn, July ¥1,714bn, October ¥1,863bn. | Q4'26 revenue $1.25-1.35bn; non-GAAP EPS $1.95-2.25 |
| Events | 13 Nov 2026 half-year 有報; late Jan 2027 Q3 results with first CY2027 TAM figures; ~May 2027 MTP4 with outlook to CY2028-29; buyback of ¥280bn running to 24 Mar 2027 | 23 Nov 2026 ex-dividend; 30 Nov 2026 UBS conference; FormFactor deal close in Q4'26; Q4 results late Jan 2027 (date not announced) |

---

## 1. Market: tester market size, shares, test intensity, bottleneck

### Takeaway
On Advantest's own estimates, the SoC-plus-memory tester market went from $6.0bn (CY24) to $9.0bn (CY25) and ≈$14.25bn (CY26e). SoC testers make up about 80% of that. Advantest says CY27 growth will be "in line with that of recent years or potentially higher", which is about 50% a year. The drivers are test time and insertions per device in advanced packaging, more than unit volume. Test capacity and DRAM components are now a stated industry constraint.

### Cited Findings
- **Tester market, all company estimates (company claim, unconfirmed):**
  - CY23: $4.4bn (SoC $3.3bn, memory $1.1bn).
  - CY24: $6.0bn (+36%; SoC $4.1bn, memory $1.9bn).
  - CY25: $9.0bn (+50%; SoC $6.9bn, +68%; memory $2.1bn).
  - Source: [Advantest FY25 slides, 27 Apr 2026](https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_260427_slide.pdf).
- **CY26 forecast path:**
  - January 2026: SoC $8.5-9.5bn, memory $2.2-2.7bn.
  - April 2026: SoC $8.7-9.5bn, memory $2.2-2.7bn ([Apr 2026 slides](https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_260427_slide.pdf)).
  - July 2026: SoC $10.5-11.5bn, memory $2.5-3.0bn, total $13.0-14.5bn, up about 19% at the midpoint, driven by "inference AI… ASICs, CPUs, and DRAM" ([Jul 2026 note](https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_260729_note.pdf)).
  - October 2026: unchanged. SoC "approximately 11.5 billion USD, near the upper end"; memory "around the midpoint of 2.5 to 3.0" ([Oct 2026 note](https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_261028_note.pdf)).
- **CY27:** a quantitative outlook is due at the Q3 briefing in January 2027. "Tester TAM has grown at an annual average of about 50% or slightly above over the past few years… we do not see that slowing" ([Q&A 28 Oct 2026](https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_261028_QA.pdf)).
- **Supply:** "we expect the industry to remain supply constrained in CY2027, including… semiconductor and advanced packaging capacity" ([Oct 2026 note](https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_261028_note.pdf)).
- **Co-packaged optics:** the CPO tester market should "double or triple annually over the next couple of years and reach about 1 billion USD". That is small next to an SoC tester market that "exceeds 11 billion USD and is growing at more than 50% annually" ([Q&A 28 Oct 2026](https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_261028_QA.pdf)).
- **Test intensity (company claims, unconfirmed):**
  - "In some cases, we are seeing test times increase by multiples from one generation to the next… No one really predicted the extent of the increase in test content" ([fireside 12 Nov 2026](https://www.advantest.com/document/en/investors/ir-library/briefing/JE_IR%20Fireside_Chat_Script_20261112.pdf)).
  - Accelerators see "longer test times and additional insertions… where 3D packaging is driving greater device complexity". CPU wafer sort is "broadly similar and may be slightly higher" than for accelerators, but accelerators need more at final test ([Q&A 29 Jul 2026](https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_260729_QA.pdf)).
  - The biggest FY26 driver is CPU test for agentic AI, "a third layer of growth on top of GPUs and custom ASICs" ([Q&A 28 Oct 2026](https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_261028_QA.pdf)).
  - Packaging cost drives test content: "it's just too expensive to throw away these expensive packages" ([fireside 17 Nov 2025](https://www.advantest.com/document/en/investors/ir-library/briefing/JE_IR%20Fireside_Chat_Script_20251117.pdf)).
- **How test menus are set:** they are fixed only after customers' evaluation in early volume production, and extra quality tests can be added, which is upside for tester demand ([sell-side Q&A 27 Apr 2026](https://www.advantest.com/document/en/investors/ir-library/result/JE_Sell-Side%20Analyst%20Small%20Group%20Meeting_260427_QA.pdf)).
- **Visibility:** "we now have conversations with our close customers… based on an 18-month forecast", against six months historically ([Q&A 29 Jul 2026](https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_260729_QA.pdf)). Some customers now give multi-year forecasts ([fireside 12 Nov 2026](https://www.advantest.com/document/en/investors/ir-library/briefing/JE_IR%20Fireside_Chat_Script_20261112.pdf)).
- **Components:** testers use "a similar component mix to data-center racks… we sometimes find ourselves competing for components with the very customers we serve" ([fireside 12 Nov 2026](https://www.advantest.com/document/en/investors/ir-library/briefing/JE_IR%20Fireside_Chat_Script_20261112.pdf)).
- **Teradyne on HBM (press summaries of the call, not verified against a transcript):**
  - HBM will be "the largest driver of memory-market growth" in 2027.
  - Supply constraints are leading some accelerator makers to use lower HBM stack heights, which could raise the number of stacks needing performance test ([Zacks summary, ~28 Oct 2026](https://www.zacks.com/stock/news/3018941/teradyne-q3-earnings-call-highlights-ai-demand-and-2027-growth-plans); [StockStory](https://stockstory.org/us/stocks/nasdaq/ter/news/earnings-call/teradynes-q3-earnings-call-our-top-5-analyst-questions)).

### Inferences
- If CY26 lands near ≈$14.25bn, the tester market will have more than tripled from CY23 ($4.4bn) in three years. The 2027 call rests on test content per device more than on units. That is the variable a report must stress-test, because inference-based test reduction (transition 6) would act on exactly this.
- Market reports from Mordor, LP Information and others give much lower numbers (for example $7.5bn for SoC and memory in 2026). They appear to use stale or differently scoped figures and should not be mixed with Advantest's series.

### Gaps
- No independent estimate of the tester market for 2024-2027 (SEMI, TechInsights/VLSI, Yole or Gartner) has been retrieved yet [INCOMPLETE].
- No quantified test time per device for AI accelerators or HBM from a third party.
- Teradyne's own 2026 and 2027 TAM figures are not yet retrieved [INCOMPLETE].

---

## 2. Advantest (6857.T): results, segments, guidance and plan

### Takeaway
Advantest is an unusually profitable, net-cash monopoly-like supplier at the top of its cycle. Quarterly gross margin is above 70% and operating margin 56% (Q2 FY26). Growth comes from AI compute shipped through Taiwan. Recurring services stay below 10% of revenue, and the large new pile of "strategic investment" securities is opaque.

### Cited Findings
- **FY2025 (year to 31 Mar 2026), reported 27 Apr 2026** ([決算短信 FY2025](https://www.advantest.com/document/en/investors/ir-library/result/E_FR_FY2025_FN.pdf)):
  - Net sales ¥1,128.6bn (+44.7%); operating income ¥499.1bn (+118.8%, 44.2%); net income ¥375.4bn (+132.9%); basic EPS ¥515.15; ROE 57.6%.
  - Overseas sales 97.8%.
  - Test System segment ¥1,019.4bn, segment income ¥518.8bn. Services & Others ¥109.2bn, income ¥8.8bn, which includes a ¥2.5bn divestiture gain. FY2024 had a ¥21.4bn impairment on Essai (SLT).
  - Operating cash flow ¥335.2bn; investing −¥34.6bn; financing −¥230.6bn, including ¥114.3bn of buybacks and ¥75.4bn of debt repayment. Cash ¥340.0bn.
  - Dividend ¥59; total return ratio 42% ([FY25 slides](https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_260427_slide.pdf)).
- **FY2025 segments and regions** ([FY25 slides](https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_260427_slide.pdf)):
  - SoC ¥767.4bn (FY24 ¥440.4bn); memory ¥171.5bn (¥157.7bn); other systems ¥80.5bn (¥84.7bn).
  - Ship-to region: Taiwan ¥569.5bn, China ¥213.3bn, Korea ¥180.3bn, Others ¥72.8bn, Americas ¥44.5bn, Japan ¥25.1bn, Europe ¥23.1bn.
  - FY24 for comparison: Taiwan ¥326.5bn, China ¥175.1bn, Korea ¥157.0bn.
  - I read the region values from chart labels; they reconcile to the totals and to the 決算短信 geography for Japan, Americas and Europe.
- **Why Taiwan grew:** "strengthened quality assurance requirements for high-end SoC semiconductors from several U.S. fabless companies, resulting in increased sales to the related foundries and OSATs" ([FY25 note](https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_260427_note.pdf)).
- **Quarterly results (ends Jun-25, Sep-25, Dec-25, Mar-26, Jun-26, Sep-26)** ([Oct 2026 slides](https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_261028_slide.pdf)):
  - Sales ¥263.8bn, ¥262.9bn, ¥273.8bn, ¥328.1bn, ¥367.5bn, ¥477.7bn.
  - Gross margin 65.1%, 62.2%, 62.0%, 67.4%, 69.5%, 71.1%.
  - Operating margin 47.0%, 41.3%, 41.5%, 46.7%, 51.7%, 55.9%.
- **Q2 FY26 (Jul-Sep 2026):**
  - SoC ¥353.3bn ("GPU… ASIC and CPU applications grew"); memory ¥53.4bn; other systems ≈¥29.9bn; services & others ¥41.1bn.
  - R&D ¥23.4bn (4.9% of sales); capex ¥12.1bn; operating cash flow ¥169.8bn; FCF ¥61.5bn after strategic security purchases ([Oct 2026 note](https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_261028_note.pdf)).
  - Ship-to (chart labels): Taiwan ¥261.3bn (54.7%), China ¥90.1bn (18.9%), Korea ¥64.6bn (13.5%), Others ¥38.1bn, Americas ¥15.7bn, Europe ¥6.1bn, Japan ¥1.8bn.
  - Q1 FY26 for comparison: Taiwan ¥178.6bn, China ¥69.4bn, Korea ¥67.4bn of ¥367.5bn.
- **H1 FY26 (Apr-Sep 2026), reported 28 Oct 2026** ([決算短信 H1 FY2026](https://www.advantest.com/en/news/2026/mpd9kn0000000gii-att/E_FR_FY2026_2Q.pdf)):
  - Sales ¥845.2bn (+60.5%); gross profit ¥595.4bn; operating income ¥456.8bn (+96.5%); financial income ¥57.0bn, of which ¥54.2bn is valuation gains on strategic investments; net income ¥368.1bn.
  - Test System ¥770.2bn, segment income ¥455.6bn; Services & Others ¥75.0bn, income ¥20.9bn.
  - Operating cash flow ¥307.0bn. Investing −¥210.9bn, including ¥184.4bn of debt-instrument purchases, ¥26.1bn of equity purchases and ¥21.5bn of capex. Buybacks ¥105.9bn.
  - In April 2026 Advantest issued ¥100bn of zero-coupon convertible bonds due 2031.
  - Investment securities went from ¥67.9bn to ¥432.6bn. Inventories went from ¥231.7bn to ¥352.4bn.
  - Average FX: ¥160/$.
- **FY2026 guidance (28 Oct 2026)** ([note](https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_261028_note.pdf), [slides](https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_261028_slide.pdf)):
  - Sales ¥1,863bn (+65.1%); operating income ¥967bn (51.9%); gross margin ≈68%.
  - 2H sales ¥1,017.8bn, about +20% on 1H; 2H operating margin 50.1%. The 1H margin was helped by low-cost DRAM inventory and an inventory write-down reversal.
  - Segments: SoC ¥1,375.0bn (July: ¥1,243.5bn); memory ¥229.0bn (¥227.0bn); other systems ¥110.5bn; Services & Others ¥148.5bn.
  - SoC mix: compute and communications 90%, against 95% in FY25. Memory mix: DRAM 85%, non-volatile memory 15%.
  - R&D ¥114.0bn; capex ¥60.0bn; 2H FX ¥150/$.
- **Margin defence:** rising DRAM and other component costs will be offset "through pricing enabled by higher-specification tester configurations, licensing, and new instrumentation", keeping 2H operating margin "in the low 50% range" ([Q&A 28 Oct 2026](https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_261028_QA.pdf)).
- **Plan targets:** MTP3 (FY24-26 three-year averages) were raised on 28 Oct 2025 to sales ¥835-930bn, operating margin 33-36%, net income ¥207-248bn, ROIC 34-39% and EPS ¥284-341 ([release](https://www.advantest.com/en/news/2025/g2l53r0000000ofm-att/E_Info_20251028_01.pdf)). Actual and forecast sales average ≈¥1,257bn (¥779.7bn, ¥1,128.6bn, ¥1,863bn), well above the range. MTP4 is due "around May 2027" with an outlook through CY2028-29 ([Q&A 28 Oct 2026](https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_261028_QA.pdf)).
- **Capacity:**
  - SoC capacity is already above 5,000 systems a year. The 10,000 target is to come "well ahead of" the original end-FY2028 or CY2029 date, and 20,000 is "under active internal discussion" ([Q&A 28 Oct 2026](https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_261028_QA.pdf)).
  - 10,000 of today's systems equal about 20,000 in 2020 configuration; 2020 output was about 1,000. A second EMS factory in Southeast Asia is ramping ([Q&A 29 Jul 2026](https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_260729_QA.pdf)).
  - Use of convertible-bond proceeds: ≈¥50bn for capacity by March 2029, ¥20bn for inventory and ¥30bn for next-generation test ([決算短信 FY2025](https://www.advantest.com/document/en/investors/ir-library/result/E_FR_FY2025_FN.pdf)).
- **Returns:** interim dividend ¥49; buyback of up to ¥280bn or 11m shares between 29 Oct 2026 and 24 Mar 2027; MTP3 total return ratio of 50% or more ([note 28 Oct 2026](https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_261028_note.pdf)).
- **China:** "approximately 19% of total sales… relatively consistent around 20%". The China mix is about 80-85% SoC and 15% memory. New fabs in China may add business "around the 2028-2029 timeframe"; until then China stays "around the current 20% level or lower" ([Q&A 29 Jul 2026](https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_260729_QA.pdf)).
- **Memory share outlook:** "memory market share may experience a decline this year". Advantest is not the NAND incumbent, and "device speed and bandwidth transitions are also creating insertion opportunities that we have not fully captured". It has new products with customer commitments ([Q&A 29 Jul 2026](https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_260729_QA.pdf)).
- **Competition and dual sourcing:** "customers may consider dual-vendor strategies… we are staying ahead of that" ([Q&A 27 Apr 2026](https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_260427_QA.pdf)). Customers "prefer to work with a single supplier because it is more efficient in terms of engineering resources and managing their installed base" ([fireside 12 Nov 2026](https://www.advantest.com/document/en/investors/ir-library/briefing/JE_IR%20Fireside_Chat_Script_20261112.pdf)).
- **Other:** cybersecurity incident in February 2026 ([FY25 note](https://www.advantest.com/document/en/investors/ir-library/result/JE_BIZ_260427_note.pdf)). Customer concentration disclosed only qualitatively ([IAR 2026](https://www.advantest.com/document/en/investors/ir-library/annual/E_all_IAR2026.pdf)).

### Inferences
- **2H operating margin:** ≈50% looks set to normalise downward as DRAM costs flow through, before any volume slowdown.
- **Revenue mix:** about 90% of SoC revenue is compute and communications, and over half of all revenue ships to Taiwan. Revenue therefore tracks a handful of US fabless AI programmes built at TSMC and its OSATs.
- **Free cash flow:** H1 FY26 FCF of ¥96.1bn mixes operations with securities purchases. Underlying operating cash flow less capex was ≈¥284bn.
- **Orders:** none of the FY2025-FY2026 documents read reports orders or backlog.

### Gaps
- Orders and backlog are not disclosed in any document read. I could not verify whether disclosure was discontinued, or when.
- The identity of the ¥364.7bn of new "strategic investment" securities and the "investment fund" contribution is not disclosed.
- Named customer shares are not disclosed.
- The split of Services & Others between support services and other is to be confirmed [INCOMPLETE].

---

## 3. Teradyne (TER): results, segments, position

### Takeaway
Teradyne is a smaller, lower-margin number two in SoC test. It has gained ground in memory and HBM test (Korea was 32% of Q3'26 revenue) and is buying into the probe and interface layer (Technoprobe, FormFactor). Its customer concentration is higher and disclosed. China is 15-21% of revenue under US export rules.

### Cited Findings
- **Q3 2026** (quarter to 27 Sep 2026, reported 27 Oct 2026) ([8-K Ex. 99.1](https://www.sec.gov/Archives/edgar/data/0000097210/000119312526434981/ter-ex99_1.htm); [10-Q](https://investors.teradyne.com/sec-filings/all-sec-filings/content/0001193125-26-441091/ter-20260927.htm)):
  - Revenue $1,306.0m (+70%; Q2'26 $1,329.0m). Semiconductor Test $1,072.0m (+76.9%): SoC $676.5m, memory $300.8m, IST $94.7m. Product Test $138.1m (+56.4%); Robotics $95.8m (+27.6%).
  - GAAP gross margin 59.1%; engineering and development $163.1m (12.5%); GAAP operating income $402.0m (30.8%).
  - GAAP EPS $2.17; non-GAAP $2.29.
- **Q4 2026 guidance:** revenue $1,250-1,350m; non-GAAP EPS $1.95-2.25 ([8-K](https://www.sec.gov/Archives/edgar/data/0000097210/000119312526434981/ter-ex99_1.htm)). Quartr's summary adds a gross-margin guide of 57.5-58.5% and an FY26 midpoint of about $5.2bn; Quartr is a third-party AI summary ([Quartr](https://quartr.com/events/teradyne-ter-q3-2026_3sxG0RzK)).
- **CEO quote:** "Demand extended across the AI value chain, from memory and hard disk drive test to high-speed interconnect and robotics" (Greg Smith, [8-K](https://www.sec.gov/Archives/edgar/data/0000097210/000119312526434981/ter-ex99_1.htm)).
- **Memory:** a record $301m, the fourth consecutive quarter above $200m ([10-Q](https://investors.teradyne.com/sec-filings/all-sec-filings/content/0001193125-26-441091/ter-20260927.htm)).
- **Call commentary (not verified against a transcript):**
  - Compute revenue up "nearly 50%" year on year (CFO Michelle Turner); customers' dual-vendor strategies should add compute opportunities in 2027 ([Zacks](https://www.zacks.com/stock/news/3018941/teradyne-q3-earnings-call-highlights-ai-demand-and-2027-growth-plans)).
  - "Compute is exceeding expectations and share is rising" (company claim, unconfirmed). Major ASIC ramps in 2027 are "more back-end loaded". CPO is "preseason" ([StockStory](https://stockstory.org/us/stocks/nasdaq/ter/news/earnings-call/teradynes-q3-earnings-call-our-top-5-analyst-questions)).
  - AI-related revenue was above 60% of sales ([Quartr](https://quartr.com/events/teradyne-ter-q3-2026_3sxG0RzK)).
- **Revenue by country:**
  - Q3'26: Korea 32%, China 21%, Taiwan 14%, Singapore 9%, US 8%, Europe 5%. Q3'25: Korea 12%, China 17%, Taiwan 37%.
  - 9M'26: Taiwan 32%, Korea 24%, China 15%, US 7%, Singapore 6% ([10-Q](https://investors.teradyne.com/sec-filings/all-sec-filings/content/0001193125-26-441091/ter-20260927.htm)).
- **Balance sheet and cash flow** ([8-K](https://www.sec.gov/Archives/edgar/data/0000097210/000119312526434981/ter-ex99_1.htm); [10-Q](https://investors.teradyne.com/sec-filings/all-sec-filings/content/0001193125-26-441091/ter-20260927.htm)):
  - Cash $460.7m plus marketable securities $164.1m; no borrowings. The $200m drawn at 31 Dec 2025 was repaid, and a $1.0bn revolver signed on 7 Aug 2026 runs to 2031.
  - 9M'26 operating cash flow $1,047.9m, capex $241.8m, FCF $806.1m.
  - Buybacks $173.5m, or 0.5m shares at an average $349.62; dividends $61.0m.
  - 156.12m shares outstanding (26 Oct 2026).
- **Deals** ([10-Q](https://investors.teradyne.com/sec-filings/all-sec-filings/content/0001193125-26-441091/ter-20260927.htm)):
  - Technoprobe: 10% for €483.1m ($524.1m) on 27 May 2024, with a board seat. Carrying value $518.6m against a fair value of $2,242.4m at 27 Sep 2026.
  - FormFactor: $300m minority stake plus collaboration ("silicon photonics, high-performance compute, advanced packaging, and high-bandwidth memory"), agreed 6 Oct 2026, closing in Q4'26.
  - MultiLane Test Products: 75% for $157.8m on 8 Apr 2026.
  - Quantifi Photonics (New Zealand, photonic IC test): acquired 31 May 2025 for $127.2m; "not material".
  - Infineon ATE team in Regensburg: 31 Jan 2025, €17.6m.
- **2025 10-K** ([10-K FY2025](https://investors.teradyne.com/sec-filings/all-sec-filings/content/0001193125-26-059002/ter-20251231.htm)):
  - Segment mix: Semi Test 79%, Product Test 11%, Robotics 10%.
  - Semi Test +$399.8m (+18.8%) "driven primarily by higher sales in compute related to artificial intelligence applications and… system level testers".
  - Concentration: five largest direct customers 44% (2024 36%, 2023 32%). Two specifiers drove 12% and 10%; one direct customer 19%.
  - Named competitors: Advantest, SPEA, Cohu, "emerging Asian companies and… internal supply at several of our customers". About 6,600 employees.
  - Exports: "Compliance with the military end user rule has impacted our ability to sell products to certain customers in China". "Current trade restrictions are limiting our ability to be competitive, particularly in certain markets, where some competitors are not subjected to the same restrictions."

### Inferences
- In Jul-Sep 2026 Teradyne's memory revenue ($300.8m) and Advantest's memory-tester sales (≈$332m) were close to parity. Korea's jump to 32% of Teradyne revenue fits HBM test wins at Korean memory makers, but the customers are not named.
- In SoC, Advantest's quarterly sales were about 3.2x Teradyne's. Teradyne's "share rising" claim is plausible only from a low base.

### Gaps
- Teradyne's 2026 and 2027 TAM statements, its long-term target model and its exact 2025 revenue (≈$3.19bn derived) are still to be confirmed from its own documents [INCOMPLETE].

---

## 4. Stacked chips: HBM and hybrid-bonded die test [INCOMPLETE]

- **Advantest products:** T5801 DRAM tester (GDDR7, LPDDR6, DDR6; up to 36 Gbps PAM3 and 18 Gbps NRZ), "already in use by strategic memory customers" ([12 Feb 2025](https://www.advantest.com/en/news/2025/20250212.html)). M5241 memory handler with active thermal control, first shipments Q2 CY2026; "multiple major memory manufacturers are preparing for adoption" (company claim, unconfirmed) ([10 Dec 2025](https://www.advantest.com/en/news/2025/20251210.html)). Memory solutions "beyond HBM4" are planned ([sell-side Q&A 27 Apr 2026](https://www.advantest.com/document/en/investors/ir-library/result/JE_Sell-Side%20Analyst%20Small%20Group%20Meeting_260427_QA.pdf)). The die-level prober with Tokyo Seimitsu addresses heat in 2.5D/3D-packaged devices ([16 Dec 2025](https://www.advantest.com/en/news/2025/20251216.html)).
- **Teradyne:** Magnum 7H for HBM (2025), Magnum E2 (2026), Titan HP with burn-in (2026) and TSMC 3DFabric testing award (2025), per its press-release list ([Teradyne press releases](https://investors.teradyne.com/news-events/press-releases)) [details INCOMPLETE].
- **Test flow for HBM:** wafer sort, then known-good-stack test, then post-stack and final test. What stays untestable at hybrid-bond pitches below about 25 µm: [INCOMPLETE].

## 5. Other tester suppliers (field scan) [INCOMPLETE]
Chroma ATE, Cohu, Aehr, Emerson/NI, AEM, the Korean memory-test suppliers (YC, UniTest, Exicon, Neosem, DI) and Japanese niche suppliers are not yet researched. The only context so far: Teradyne's 10-K names SPEA and Cohu as competitors, and Advantest partners with Emerson (formerly NI) on test analytics ([19 Mar 2025](https://www.advantest.com/en/news/2025/20250319.html)).

## 6. Path-forward detail
See table A3. Sources: [ACS RTDI/NVIDIA, 6 Oct 2025](https://www.advantest.com/en/news/2025/2025100602.html); [Emerson, 19 Mar 2025](https://www.advantest.com/en/news/2025/20250319.html); [PDF Solutions, 30 Jul 2020](https://www.advantest.com/en/news/2020/20200730.html); [Velocity/AllianceATE, 18 May 2026](https://www.advantest.com/en/news/2026/20260518.html); [SiConic DFT, 16 Jul 2026](https://www.advantest.com/en/news/2026/20260716.html); [ITC 2026 and SmarTest 8, 13 Oct 2026](https://www.advantest.com/en/news/2026/20261013.html); [Technoprobe/FormFactor, 9 Jan 2025](https://www.advantest.com/en/news/2025/20250109.html); [MJC, 27 Feb 2025](https://www.advantest.com/en/news/2025/20250227.html).

## 7. Entry-point data [INCOMPLETE]
For Teradyne see table A4 ([stockanalysis.com, 12 Nov 2026](https://stockanalysis.com/stocks/ter/statistics/)): 52-week change +44%; 18 analysts rate it Buy on average, with a mean target of $415.88. On StockStory's figures the stock fell from $324.95 before the results to $303.65 after ([StockStory](https://stockstory.org/us/stocks/nasdaq/ter/news/earnings-call/teradynes-q3-earnings-call-our-top-5-analyst-questions)). Advantest valuation data is still to be collected.

## 8. Could not verify (so far)
- Advantest orders and backlog.
- Advantest named customers and their shares.
- Independent (third-party) tester market shares.
- Teradyne TAM figures and long-term model.
- The current size of Advantest's PDF Solutions stake.
- Any ATE product that reports a stated uncertainty.
- Roadmap statements on test access below 25 µm bond pitch.
- The Advantest share price and valuation.
- All suppliers in section 5.

## 9. Sources (dates as published)
See inline links. Advantest documents are dated 30 Jul 2020 to 12 Nov 2026; Teradyne filings 2025 10-K (FY ended 31 Dec 2025), Q3'26 8-K (27 Oct 2026) and 10-Q (quarter to 27 Sep 2026); stockanalysis.com (12 Nov 2026).
