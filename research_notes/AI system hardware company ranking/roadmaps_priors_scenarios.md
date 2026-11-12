# Roadmaps, priors and spending scenarios for system-level AI hardware: cross-check as of 12 November 2026

Research date: 12 Nov 2026. Most sources are dated Apr-Nov 2026. Scope covers roadmap dates, slips, demand, financing and policy. Company profiles and valuation are out of scope; no share-price data is used.

**Source labels used below**
- **[P]** Primary: a company call, filing, prepared remarks, standards-body spec or government notice. A law-firm summary of a government notice is also marked [P] when it quotes the notice.
- **[S]** Secondary: trade press, analyst or aggregator.
- **[F]** The page was opened and read.
- **[SR]** Taken from a search-result summary of that page. The page itself was not opened, so confidence is lower.
- "Company claim, unconfirmed" marks statements no outside party has corroborated.

**Process limits (read before relying on coverage)**
- The session's shared web-search budget ran out about halfway through.
- The Exa and Firecrawl tools ran out of credits.
- After that, only pages already found could be read.
- No local-language searching (Korean, Japanese, Chinese, Taiwanese) was possible. Korean and Taiwanese press were seen only through TrendForce, The Elec and Chosun Biz relays.
- Huawei and other Chinese systems, Dutch, Japanese, Korean, Taiwanese, Israeli and Indian controls, and Chinese hyperscaler capex were **not** researched. See "What could not be verified".

**Verdict summary**

| # | Background claim | Verdict |
|---|---|---|
| 1 | Constraint sequence: memory, power, finance (2026-28), then packaging, optics, rack power, cooling (2028-30) | **Updated / partly contradicted.** Memory and power are binding now. Packaging back-end, optical engines and board-level manufacturing are *also* binding in 2026. Financing stress is visible but limited to the leveraged tier. Slips confirmed widely. |
| 2 | 55/25/20 scenarios | **Updated.** Base case is supported through 2027. Compute growth runs above "doubling". Financing stress appears earlier (Q4 2026) than "around 2028". Acceleration is capped by supply through at least Jan 2028. |
| 3 | TSMC packaging +80%/yr; 52-78 wk lead times; 12+ HBM package 2027; panel pilot 2026, volume 2028-29; glass 2027-28 | **Mixed.** CAGR confirmed (company claim). Lead times could not be verified. The 2027 large package is at risk because Rubin Ultra was reportedly cut to 8 stacks. Panel timing is roughly confirmed, but pilot *production* is reported for mid-2027. Glass is still targeted 2027-28 but slipping. |
| 4 | HBM sold out 2026, committed 2027, tight into 2028; Micron annual cadence to 2030; hybrid bonding at 16-high HBM4E earliest | **Confirmed and strengthened.** SK hynix says DRAM+HBM are "effectively sold out" through 2029. Micron says industry DRAM is supply-constrained in 2027 and 2028 with "no line of sight" to balance. Hybrid-bonding timing confirmed, with a risk of further deferral. |
| 5 | A16 slipped late-2026 to 2027; 600 kW rack reported delayed to 2028, NVIDIA disputes | **Confirmed.** New since: Rubin Ultra reportedly cut from 4 to 2 dies (unconfirmed). A 12 Nov 2026 claim that base Rubin volume slipped to 2027 (unconfirmed) contradicts NVIDIA's August statement. |
| 6 | 2.3 kW heading to 4 kW; cold plates 100-150 kW/rack; two-phase held by fluorinated-coolant rules; in-chip channels unproven | **Partly confirmed.** Power figures confirmed from secondary estimates (NVIDIA publishes none). The 100-150 kW cold-plate ceiling looks outdated because NVIDIA plans direct-to-chip liquid cooling for 600 kW Kyber. The PFAS hold-up is confirmed, but fluid qualification also matters. No production evidence of in-chip cooling. |
| 7 | CPO switches shipping 2026; NVIDIA and partner plan 15x optical-engine capacity by mid-2027; processor-to-processor optics 2028, may slip; copper stretched to 2027-28 | **Confirmed, with updates.** The 15x plan is with SPIL (NVIDIA, 21 Oct 2026). Copper stays as a scale-up option even in Feynman (2028), so copper is stretched *beyond* 2028. |
| 8 | Probabilities | See Claim 8. 70% "a 2028 technology misses" looks reasonable to low. 65% "600 kW in 2028" is reasonable. 50% "1 MW by 2030" is reasonable. 70% "memory tight through 2028" looks too low (evidence supports about 80-85%). "Memory first to turn" is weakened by take-or-pay contracts. "Bridges last longer" is supported. |

---

## Claim 1: The binding constraint moves in sequence, and successors slip

### Takeaway
**Verdict: UPDATED (partly contradicted).** In late 2026, memory and power or site readiness are clearly binding. Financing stress is showing at the leveraged edge (neoclouds) but not yet in hyperscaler budgets.

Advanced-packaging back-end capacity, optical engines and lasers, and board-level manufacturing (PCB midplanes, warpage) are already binding in 2026. They are not a 2028-2030 phenomenon. The claim that successors slip is strongly confirmed by at least eight 2026 slips.

### Cited Findings

**Memory (binding now)**
- NVIDIA's supply commitments rose from $119B to $279B in one quarter (period: quarter ended Jul 2026; reported 26 Aug 2026), "primarily related to the procurement of memory" — [NVIDIA Q2 FY27 press release](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027) [P][SR]
- Kress said the largest parts of those commitments fall "in the first three years" — [StockAnalysis transcript, 26 Aug 2026](https://stockanalysis.com/stocks/nvda/transcripts/676136-q2-2027/) [P][F]
- On memory, NVIDIA said "The magnitude of the price increase has exceeded our prior expectations" — [same transcript](https://stockanalysis.com/stocks/nvda/transcripts/676136-q2-2027/) [P][F]
- Micron expects memory supply-demand conditions "much tighter in calendar 2027 and 2028" than in 2026. It sees industry DRAM bit shipments growing in the low-20s % range in 2027 and 2028, "supply constrained in both years". Micron: "we do not have line of sight to when supply and demand will return to balance" (published 30 Sep 2026) — [Micron FQ4 FY26 prepared remarks](https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf) [P][F]
- SK hynix says DRAM and HBM output is "effectively sold out through 2029", combining long-term agreements (LTAs) with ongoing negotiations (published 28 Oct 2026) — [TrendForce relaying SK hynix Q3 2026](https://www.trendforce.com/news/2026/10/28/news-sk-hynix-3q26-opm-hits-record-80-says-dram-hbm-effectively-sold-out-to-2029-14-lta-customers-signed/) [S relaying company claim][F]

**Power, site and shell (binding now)**
- Huang on what customers must secure: "You have got to go secure the Land, Power, and Shell, which oftentimes is a couple, two, three years out" (26 Aug 2026) — [NVIDIA transcript](https://stockanalysis.com/stocks/nvda/transcripts/676136-q2-2027/) [P][F]
- AMD also described land, power and shells as a customer-side gating item (3 Nov 2026) — [Motley Fool AMD Q3 2026 transcript](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/) [P][F]
- US 2026 capacity: of 16 GW of data-centre capacity announced for 2026, only about 5 GW was under construction as of summer 2026 (TD Economics). SynMax says nearly 40% of US projects due in 2026 could miss targets by more than 3 months (published 5 Oct 2026) — [Power Engineering, 5 Oct 2026](https://www.power-eng.com/renewables/america-data-center-construction-delays/) [S][F]
- Same source: interconnection waits run 3-4 years in major US markets and up to 7 years in Northern Virginia. Texas has halted new data-centre grid connections pending an audit. Proposed US data-centre power requests exceed 700 GW — [Power Engineering, 5 Oct 2026](https://www.power-eng.com/renewables/america-data-center-construction-delays/) [S][F]
- Named delays (same source):
  - Oracle issued a force-majeure notice tied to the Stargate campus in New Mexico (Project Jupiter), whose gas pipeline slipped to Feb 2027.
  - Oracle/Vantage Project Lighthouse (Wisconsin) is listed by Oracle for 2H 2027, but Aterio estimates full 1.3 GW only by Oct 2028.
  - Stargate Abilene is ramping slower than early estimates.
  - [Power Engineering, 5 Oct 2026](https://www.power-eng.com/renewables/america-data-center-construction-delays/) [S][F]
- Microsoft lowered its capex outlook on 28 Oct 2026 because third-party (leased) capacity deliveries slipped into the second half of its fiscal year — [investingLive, 28 Oct 2026](https://investinglive.com/stocks/microsoft-sees-170bn-capex-in-fiscal-2027-but-says-it-will-stay-cash-flow-positive/) [S][F]; [Yield Theory](https://www.yieldtheory.app/research/hyperscaler-capex-2027-forecast) [S][F]
- Contrast from TSMC: it sent teams to check US build-outs and power, found "so far so good", and said cloud providers are "well-prepared" (15 Oct 2026) — [Investing.com TSMC Q3 2026 transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-tsmc-beats-q3-2026-estimates-as-stock-slips-93CH-4950695) [P][F]. Company claim, unconfirmed.

**Financing (stress at the margin)**
- Credit-market signals, early Nov 2026:
  - CoreWeave 2032 bond (9.625% coupon) yielding above 16%.
  - CoreWeave 5-year CDS above 1,289 bp on 5 Nov 2026 (Deutsche Bank), about 1,155 bp on 6 Nov.
  - Goldman Sachs: hyperscalers collectively had negative free cash flow in Q3 2026.
  - Goldman Sachs: moratoria could affect 45% of planned US data-centre capacity.
  - [CNBC, 6 Nov 2026](https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html) [S][F]
- More detail is under the spending-scenarios section.

**Packaging and back end (binding now, not only from 2028)**
- TSMC CEO Wei acknowledged "a little bit shortage on the back end", citing an interposer arrangement with GlobalFoundries. Demand is "far above our capability today to supply" (15 Oct 2026) — [TSMC Q3 2026 transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-tsmc-beats-q3-2026-estimates-as-stock-slips-93CH-4950695) [P][F]
- The CoWoS supply-demand gap was put at about 20% in Jun 2026, narrowing to about 10% by end-2026, according to institutional investors quoted by Economic Daily News — [TrendForce, 15 Jun 2026](https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-reportedly-seen-narrowing-from-20-to-10-by-end-2026-as-capacity-expands/) [S][F]
- TSMC reportedly plans a ~20% CoWoS price rise and is skipping equipment price renegotiation (27 Oct 2026) — [TrendForce](https://www.trendforce.com/news/2026/10/27/news-tsmc-reportedly-eyes-20-cowos-price-hike-skips-equipment-price-renegotiations-amid-ai-demand-surge/) [S][SR]
- AMD said it worked to "secure the wafers, substrates, advanced packaging, memory", and that "demand is higher than supply" (3 Nov 2026) — [AMD Q3 2026 transcript](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/) [P][F]
- NVIDIA: "we expect supply to remain a bottleneck at least through the end of fiscal year 2028" (FY28 ends late Jan 2028; said 26 Aug 2026) — [NVIDIA transcript](https://stockanalysis.com/stocks/nvda/transcripts/676136-q2-2027/) [P][F]

**Optical engines and lasers (binding now for CPO)**
- Huang: "Capacity is the constraint" (GTC Berlin coverage, 21 Oct 2026). The same article cites 2026 supply deals with Corning, Lumentum and Coherent linked to EML laser concerns — [SDxCentral, 21 Oct 2026](https://www.sdxcentral.com/news/nvidia-targets-15x-optics-capacity-expansion-by-2027-to-meet-cpo-demand/) [S][F]
- TrendForce names three CPO bottlenecks: optical engines, silicon-photonics wafer fabrication, and advanced packaging (27 Jul 2026) — [TrendForce press release](https://www.trendforce.com/presscenter/news/20260727-13151.html) [S][F]

**Board-level manufacturing**
- The reported Kyber delay was attributed to manufacturability of the PCB midplane (Jul 2026) — [WinBuzzer, 7 Jul 2026](https://winbuzzer.com/2026/07/07/reported-nvidia-kyber-delay-pushes-ai-rack-toward-2028-xcxwbn/) [S][F]
- An analyst claims a Rubin delay caused by motherboard warpage (12 Nov 2026, unconfirmed) — [Newsquawk](https://newsquawk.com/headlines/citrinis-jukan-says-that-one-thing-ive-been-able-to-confirm-is-that-nvidias-nvda-rubin-has-been-delayed-again-im-told-motherboard-warpage-caused-the-latest-delay-and-that-the-hbm-issue-was-resolved-in-october) [S][F]

**Slips logged during 2026 (supports "dates tend to slip")**
1. TSMC A16 moved from "late 2026" to 2027 — [SemiEngineering, 27 Apr 2026](https://semiengineering.com/tsmc-tech-symposium-2026-by-the-numbers/) [S][F]
2. Quantum-X Photonics CPO moved from late 2025 to early 2026 at low volume — [Longbridge](https://longbridge.com/en/topics/100000000858275) [S][SR]
3. Kyber NVL144 reportedly slipped more than 12 months toward 2028 — [WinBuzzer](https://winbuzzer.com/2026/07/07/reported-nvidia-kyber-delay-pushes-ai-rack-toward-2028-xcxwbn/) [S][F]
4. Rubin Ultra reportedly cut from 4 to 2 compute dies — [igor'sLAB, 1 Jul 2026](https://www.igorslab.de/en/nvidia-rubin-ultra-four-die-scrapped-reversal/) [S][F]
5. Samsung Electro-Mechanics glass-substrate equipment orders slipped three times (Dec 2025 to Mar to Jun 2026) — [TrendForce, 18 Aug 2026](https://www.trendforce.com/news/2026/08/18/news-glass-substrate-war-heats-up-shinko-electric-advances-22-layer-product-as-samsung-reportedly-faces-ramp-up-uncertainty/) [S][F]
6. SKC glass mass production reportedly pushed to 2027 — same TrendForce page, related headline dated 24 Jul 2026 [S][F, headline only]
7. CoPoS pilot *production* reportedly mid-2027 — [TrendForce, 15 Jun 2026](https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-reportedly-seen-narrowing-from-20-to-10-by-end-2026-as-capacity-expands/) [S][F]
8. US data-centre deliveries: 30-50% of 2026 projects expected to slip — [Power Engineering](https://www.power-eng.com/renewables/america-data-center-construction-delays/) [S][F]
9. Unconfirmed: base Rubin volume reportedly slipped to 2027 — [Newsquawk, 12 Nov 2026](https://newsquawk.com/headlines/citrinis-jukan-says-that-one-thing-ive-been-able-to-confirm-is-that-nvidias-nvda-rubin-has-been-delayed-again-im-told-motherboard-warpage-caused-the-latest-delay-and-that-the-hbm-issue-was-resolved-in-october) [S][F]

**Transistor architecture after 2030**
- TSMC targets A13 and A12 for 2029 without High-NA EUV. SemiEngineering calls A12 an "aggressive speedup" — [SemiEngineering, 27 Apr 2026](https://semiengineering.com/tsmc-tech-symposium-2026-by-the-numbers/) [S][F]; [TrendForce, 23 Apr 2026](https://www.trendforce.com/news/2026/04/23/news-tsmc-unveils-latest-roadmap-a12-a13-set-for-2029-without-high-na-euv-a16-volume-production-delayed-to-2027/) [S][F]
- No 2026 evidence was found that transistor architecture is binding before 2030.

### Inferences
- The constraints are concurrent, not sequential. In 2026, memory, power or shell readiness, CoWoS back-end, optical engines and lasers, and PCB or board assembly all bind at once.
- The sequence the claim proposes (packaging and optics only in 2028-30) understates how early packaging and optics bind. It also implies a hand-off that the evidence does not show.
- Reorder: (a) memory and power/shell are the hardest now. (b) Packaging, back-end, optics and board-level are binding now and are likely to stay binding into 2028 as Kyber, CPO scale-up and CoPoS arrive. (c) Financing is binding first for neoclouds and project-financed sites, not hyperscalers.
- Power behaves as a deferral mechanism rather than a demand destroyer. Microsoft cut near-term capex because leased capacity arrived late, not because demand fell.
- That converts spending pauses into timing shifts. It also strengthens bridging hardware, which ships into whatever capacity is ready.

### Gaps
- Generation and transmission constraints after 2030 were not researched (no IEA material retrieved).
- No primary data on transformer or gas-turbine lead times was retrieved this session.
- The underlying Sightline report was not retrieved; figures come via TD Economics, SynMax and press.

---

## Claim 2: Three spending scenarios to 2030 (55% steady, about 2x compute per year; 25% financing-led pause around 2028; 20% faster acceleration)

### Takeaway
**Verdict: UPDATED.** The steady-growth base case is supported through 2027: guidance points higher, and supply, not demand, caps growth through at least Jan 2028.

Measured compute growth (Epoch AI) has run at 2.2-3.3x a year, above "doubling". Financing stress is already visible in Q4 2026, earlier than "around 2028", but it sits in the leveraged tier. The probability assessment is in the spending-scenarios section below.

### Cited Findings

**Capex: company guidance and indications**

| Company | 2026 figure | Period | 2027 indication | Date and source |
|---|---|---|---|---|
| Alphabet | $195-205B (unchanged) | CY2026 | CFO: capex will "increase significantly in 2027" | Q3 call 28 Oct 2026 — [Yield Theory](https://www.yieldtheory.app/research/hyperscaler-capex-2027-forecast) [S][F] |
| Microsoft | About $170B, lowered on 28 Oct 2026 for late third-party capacity. **Period conflicts**: investingLive says fiscal 2027 (Jul 2026-Jun 2027); Yield Theory says calendar 2026. One summary says Q1 FY27 capex was $45.2B [SR]. Q2 FY27 expected above $50B. | Disputed | H2 FY27 (Jan-Jun 2027) spend to "accelerate". Microsoft would consider other ways to raise capital but says it has not needed to. | [investingLive, 28 Oct 2026](https://investinglive.com/stocks/microsoft-sees-170bn-capex-in-fiscal-2027-but-says-it-will-stay-cash-flow-positive/) [S][F]; [Yield Theory](https://www.yieldtheory.app/research/hyperscaler-capex-2027-forecast) [S][F]; [FourWeekMBA](https://fourweekmba.com/ai-microsoft-lowers-2026-capex-view-to-170b-eyes-new-funding/) [S][SR] |
| Amazon | About $220B cash capex | CY2026 | Jassy: "meaningfully more in 2027" | Q3 call 29 Oct 2026 — [Yield Theory](https://www.yieldtheory.app/research/hyperscaler-capex-2027-forecast) [S][F] |
| Meta | $135-145B (narrowed) | CY2026 | No 2027 figure until the Q4 call (about late Jan 2027) | Q3 results, dated 21 Oct 2026 by Yield Theory — [Yield Theory](https://www.yieldtheory.app/research/hyperscaler-capex-2027-forecast) [S][F] |
| Oracle | $90-95B; "not more than $70 billion in net cash CapEx" | FY2027 (Jun 2026-May 2027) | n/a | FQ1 FY27 call 10 Sep 2026 — [Yield Theory](https://www.yieldtheory.app/research/hyperscaler-capex-2027-forecast) [S][F] |
| Four US hyperscalers, total | About $730B guidance midpoint | CY2026 | Consensus about $934.5B (5 Aug 2026, about +28%). Goldman (25 Sep 2026): $1.2T for five companies including Oracle. | [Yield Theory](https://www.yieldtheory.app/research/hyperscaler-capex-2027-forecast) [S][F] |
| NVIDIA's view of hyperscaler capex | "Nearly $800 billion in 2026" | CY2026 | "$1.3 trillion in 2027" (company claim, unconfirmed) | 26 Aug 2026 — [NVIDIA transcript](https://stockanalysis.com/stocks/nvda/transcripts/676136-q2-2027/) [P][F] |
| TSMC (supplier capex) | $60-64B | CY2026 | 2026-28 capex "significantly higher than the past three years"; "tool price inflation is real" | 15 Oct 2026 — [TSMC transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-tsmc-beats-q3-2026-estimates-as-stock-slips-93CH-4950695) [P][F] |
| Micron (supplier capex) | FQ1 FY27 about $11.5B; 1H FY27 about $25B; higher in 2H; raised versus prior plans, mainly construction for cleanroom in late 2028 and beyond | FY2027 (Sep 2026-Aug 2027) | n/a | 30 Sep 2026 — [Micron remarks](https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf) [P][F] |

**Demand and supply outlook from the supply chain**
- NVIDIA guides about 70% revenue growth in FY2028 (Feb 2027-Jan 2028), limited by supply. Huang: supply covers about 70% growth while demand is "much higher". Q3 FY27 guide is $108B ±2% (26 Aug 2026) — [NVIDIA transcript](https://stockanalysis.com/stocks/nvda/transcripts/676136-q2-2027/) [P][F]
- NVIDIA's "cloud industry backlog now greater than $2 trillion" (26 Aug 2026) — [same](https://stockanalysis.com/stocks/nvda/transcripts/676136-q2-2027/) [P][F]. Company claim, unconfirmed.
- TSMC previously guided its AI-accelerator revenue CAGR for 2024-2029 at "mid to high 50s" %. Wei now says it "probably will be higher". TSMC expects FY2026 revenue growth of about 44% in USD and sees "no sign of slowdown" (15 Oct 2026) — [TSMC transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-tsmc-beats-q3-2026-estimates-as-stock-slips-93CH-4950695) [P][F]
- AMD says 2027 data-centre AI revenue "will significantly more than double" (3 Nov 2026) — [AMD transcript](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/) [P][F]

**Does compute double each year?**
- Epoch AI finds global AI computing capacity doubling about every 7 months (about 3.3x a year) — [Epoch AI data insight](https://epoch.ai/data-insights/ai-chip-production) [S, research org][SR]
- Epoch AI finds chips sold per quarter growing about 2.5x a year (doubling about every 9 months) — [Epoch trends](https://epoch.ai/trends/compute) [SR]
- Year-on-year growth in quarterly additions fell from 2.8x (Q2 2025) to 2.2x (Q2 2026). Epoch says the slowdown is not statistically significant (p = 0.26) — [Epoch AI](https://epoch.ai/data-insights/ai-computing-capacity-additions-doubling) [SR]
- Epoch's series track sales, not installations. Lags to deployment and depreciation are not netted out — [Epoch AI](https://epoch.ai/data-insights/ai-chip-production) [SR]
- About 27.6M H100-equivalents had been sold by Jun 2026, with a projection of about 140M by end-2028 (Epoch, as relayed) — [Crypto Briefing](https://cryptobriefing.com/epoch-ai-chips-billion-ai-agents/) [S][SR]
- NVIDIA's share of compute additions was about 62.5% in Epoch's Oct 2026 estimate, against 68.0% in Q1 2026. Google TPU compute reportedly grew 74% in one quarter — [FourWeekMBA](https://fourweekmba.com/ai-googles-tpu-compute-grew-74-in-a-quarter-4x-nvidias/) [S][SR]
- NVIDIA revenue per GW: "$18 billion... to $25 billion with Blackwell, to $40 billion with Vera Rubin" (26 Aug 2026) — [NVIDIA transcript](https://stockanalysis.com/stocks/nvda/transcripts/676136-q2-2027/) [P][F]. Company claim, unconfirmed.

### Inferences
- "Doubling each year" is conservative against Epoch's measured 2.2-3.3x a year. It is plausible as a forward base case if power delays bite, because installed compute lags sales.
- Spending dollars and compute units are decoupling. Memory and CoWoS price rises and tool inflation lift dollars per unit, while rising revenue per GW ($25B to $40B) and Rubin's performance gains lift compute per watt.
- So capex can rise about 30% while compute roughly doubles. A dollar pause could also coexist with continued compute growth for a while.
- The report should state which of the two (dollars or compute) each scenario refers to.

### Gaps
- No 2026 or 2027 capex figures were gathered for CoreWeave, Nebius, other neoclouds, sovereign programmes (Gulf, EU, India, Japan), or Chinese hyperscalers (Alibaba, Tencent, ByteDance, Baidu).
- Microsoft's figure needs checking against its 10-Q for the quarter ended 30 Sep 2026.
- The Meta Q3 date of 21 Oct 2026 is as given by Yield Theory and was not verified.

---

## Claim 3: TSMC advanced packaging (+80%/yr since 2022; 52-78 week lead times; 12+ HBM package in 2027; panel pilot 2026 with volume 2028-29; glass core 2027-28)

### Takeaway
**Verdict: MIXED.**
- The more-than-80% CAGR is TSMC's own stated figure for 2022-2027 (company claim, unconfirmed).
- The 52-78 week lead time **could not be verified**.
- The "12+ stack package in 2027" is **at risk or updated**. TSMC is in production at 5x reticle and only "working on" 9x and 14x. The main 2027 customer design (Rubin Ultra, 4 dies and 16 HBM4E) was reportedly cut to 2 dies and 8 stacks.
- Panel-level packaging is **roughly confirmed**: the pilot line was built in 2026, but pilot *production* is reported for mid-2027, and volume for 2028-29.
- Glass core is **confirmed as a target but slipping**.

### Cited Findings

**Capacity growth**
- TSMC forecast a CoWoS capacity CAGR above 80% for 2022-2027 at its May 2026 Taiwan Technology Symposium (as reported by Reuters). TrendForce says TSMC plans to expand CoWoS by more than 60% by 2027 — [TrendForce, 15 Jun 2026](https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-reportedly-seen-narrowing-from-20-to-10-by-end-2026-as-capacity-expands/) [S][F]. The CAGR is a company claim, unconfirmed.
- Analyst capacity estimates (all estimates):
  - TSMC CoWoS capacity in 2026 of 120-140k wafers per month, plus 50-60k from OSATs, for close to 200k industry-wide (Economic Daily News, Jun 2026) — [TrendForce, 15 Jun 2026](https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-reportedly-seen-narrowing-from-20-to-10-by-end-2026-as-capacity-expands/) [S][F]
  - JPM (Nov 2025): 105k wafers per month by end-2026 — [Jukan on X](https://x.com/jukan05/status/1989479922910597530) [S][SR]
  - UBS: 160k at end-2026 rising to 250k at end-2027; Goldman: 2.73M wafers in 2027 — as relayed in search results, sources not opened [SR]

**Package size**
- TSMC: "in the real-world production of 5X reticle size", "working on 9X and 14X reticle sizes". No date was given on the call (15 Oct 2026) — [TSMC transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-tsmc-beats-q3-2026-estimates-as-stock-slips-93CH-4950695) [P][F]
- CoWoS at 5.5 reticle had over 98% yield in 2026. SoW-X is projected to hold 64 HBM stacks, no year given (symposium, Apr 2026) — [SemiEngineering, 27 Apr 2026](https://semiengineering.com/tsmc-tech-symposium-2026-by-the-numbers/) [S][F]
- At GTC in Mar 2026, NVIDIA showed Rubin Ultra with 4 compute chiplets and 1 TB of HBM4E (16 stacks), about 7.5-8x reticle in package area. Commercial Times (via TrendForce, 1 Apr 2026) and SemiAnalysis (about 30 Jun 2026) reported a switch to 2 dies and 8 HBM4E stacks. NVIDIA has not confirmed — [igor'sLAB, 1 Jul 2026](https://www.igorslab.de/en/nvidia-rubin-ultra-four-die-scrapped-reversal/) [S][F]
- Market speculation that NVIDIA may favour 8-high HBM4 over 12-high HBM4E for Rubin Ultra (Oct 2026) — [TrendForce, 28 Oct 2026](https://www.trendforce.com/news/2026/10/28/news-sk-hynix-3q26-opm-hits-record-80-says-dram-hbm-effectively-sold-out-to-2029-14-lta-customers-signed/) [S][F]. Speculation.

**Panel (CoPoS)**
- One report said the pilot line would be complete by Jun 2026, with a ramp in 2028-29 — [TrendForce, 13 Apr 2026](https://www.trendforce.com/news/2026/04/13/news-tsmc-advances-panel-level-packaging-copos-pilot-line-reportedly-set-for-june-completion-2028-29-ramp-eyed/) [S][SR]
- A later report: materials and equipment qualification as early as Jun 2026, pilot production mid-2027, full-scale production 2028-29 (Chiayi and Arizona), with NVIDIA Feynman as first adopter — [TrendForce, 15 Jun 2026](https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-reportedly-seen-narrowing-from-20-to-10-by-end-2026-as-capacity-expands/) [S][F]
- C.C. Wei at the 4 Jun 2026 shareholder meeting: the pilot line exists, and volume will take about 2-3 more years to become very large — [BigGo Finance](https://finance.biggo.com/news/kLg0kp4BrX5PFN7BKrXD) [S][SR]
- Pilots use 310x310 mm panels. NVIDIA is expected to use the larger area for up to 12 HBM4 stacks. AMD and Broadcom are expected to stay on CoWoS-L/R — [TechPowerUp](https://www.techpowerup.com/337960/tsmc-prepares-copos-next-gen-310-x-310-mm-packages) [S][SR, older article]

**Glass core**
- Samsung Electro-Mechanics (SEMCO) targets glass-core material in 2H 2027 and finished substrates in 2028 (company claim). Its equipment-order schedule slipped three times (Dec 2025 to Mar to Jun 2026). The Elec reported a failed reliability qualification, which SEMCO denied on 19 Aug 2026. Mass production could slip to 2028 or later — [TrendForce, 18 Aug 2026](https://www.trendforce.com/news/2026/08/18/news-glass-substrate-war-heats-up-shinko-electric-advances-22-layer-product-as-samsung-reportedly-faces-ramp-up-uncertainty/) [S][F]
- DNP opened a pilot line in Dec 2025, targeting mass production in 2028. Shinko showed a 22-layer glass-core substrate in Jul 2026, with no production year given. SKC/Absolics reportedly pushed mass production to 2027 (headline dated 24 Jul 2026) — [same TrendForce](https://www.trendforce.com/news/2026/08/18/news-glass-substrate-war-heats-up-shinko-electric-advances-22-layer-product-as-samsung-reportedly-faces-ramp-up-uncertainty/) [S][F]
- Intel's glass timeline depends on customer commitments — [IRZ](https://irz.fr/en/articles/verre-remplace-pas-encore-organique-en/) [S][SR]

**Lead times**
- The only figures found: equipment lead times of 6-8 months and 12-18 months to qualify new lines, from an unidentified secondary source in search results [SR, unattributed]. NVIDIA's land, power and shell timeline of 2-3 years is cited above.

### Inferences
- If Rubin Ultra shipped as 2 dies with 8 stacks, the 2027 demand for a 9x-reticle package with 12+ stacks largely moves to Feynman in 2028. Feynman is CoPoS's expected first adopter, with volume in 2028-29.
- That makes "12+ stacks in 2027" more likely a 2028 event. The 2027 large-package date in the claim should be treated as at risk.
- On glass, "2027-28" holds only as company targets. Every named maker except DNP has shown slippage in 2026.

### Gaps
- No TSMC-published wafers-per-month figure. No primary source for the 52-78 week lead times.
- No 2026 TSMC statement dating 9.5x reticle CoWoS-L with 12 HBM4. The 2025 symposium target of 2027 is from memory and was not re-verified.
- No SoIC capacity figures.

---

## Claim 4: HBM sold out 2026, committed 2027, tight into 2028; Micron annual cadence to 2030; hybrid bonding no earlier than 16-high HBM4E

### Takeaway
**Verdict: CONFIRMED and STRENGTHENED.** Both Micron and SK hynix extend the tightness beyond 2028. SK hynix says it is effectively sold out through 2029; Micron sees DRAM supply-constrained in 2027 and 2028 with no visible balance point.

Micron's one-generation-a-year roadmap to 2030 is confirmed via secondary coverage of its 21 Oct 2026 webinar. Hybrid bonding remains out of volume HBM. The earliest insertion is 16-high HBM4E, and SK hynix points to HBM4E or HBM5.

### Cited Findings

**Micron (30 Sep 2026) [P][F]** — [prepared remarks](https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf)
- "completed agreements for the vast majority of our calendar 2027 HBM bit supply with significant price increases year over year".
- HBM4 ramp executing. Working with NVIDIA on "the industry's first custom-HBM4E implementation, NVHBM, to be adopted on next generation of GPUs and NVLink Fusion platforms".
- Industry HBM bit shipments to grow faster than conventional DRAM through 2028.
- 26 strategic customer agreements (SCAs), estimated at over 35% of revenue through 2030. Some extend into 2031. Three-quarters have defined pricing frameworks, mostly with floors and ceilings. Customer financial commitments total $32B, "the vast majority of which are cash deposits".
- Supply timing:
  - Singapore HBM advanced-packaging facility: initial output early 2027.
  - Idaho ID1 wafer output mid-2027; ID2 late 2028.
  - Japan DRAM expansion initial output late 2028.
  - New York initial output 2030.
  - Next DRAM node in volume production in 2H 2027.

**Micron roadmap webinar (21 Oct 2026)**
- HBM4 in 2026, HBM4E in 2027, HBM5 in 2028, HBM5E in 2029, HBM6 in 2030. "JEDEC + custom beginning with HBM4E".
- HBM4: 12-high, 36 GB, over 2.8 TB/s per stack. A 16-high, 48 GB HBM4 is sampling.
- The CEO expects supply tighter than demand through 2027 and 2028. No bonding method was disclosed.
- Micron rejects 4F² DRAM. CXMT is pursuing 4F² with vertical transistors, without EUV, and plans a DDR5 server product by end-2026.
- [TechTimes, 22 Oct 2026](https://www.techtimes.com/articles/329350/20261022/micron-maps-annual-hbm-advances-2030-rejects-chinese-density-workaround.htm) [S][F]

**SK hynix Q3 2026 (28 Oct 2026)**
- Revenue KRW104.6T, operating profit KRW83.3T, an operating margin of about 80%.
- DRAM and HBM "effectively sold out through 2029".
- LTAs cover more than 50% of planned 2027 and 2028 capacity. 14 LTA customers, up from 10 in Q2. Exploring terms longer than five years.
- 2027 HBM volumes and prices are finalised. HBM4 to pass HBM3E in Q4 2026. 12-high HBM4 deliveries on schedule. M15X ramping to full capacity by year-end.
- [TrendForce](https://www.trendforce.com/news/2026/10/28/news-sk-hynix-3q26-opm-hits-record-80-says-dram-hbm-effectively-sold-out-to-2029-14-lta-customers-signed/) [S relaying company][F]. Company claims, unconfirmed.

**NVIDIA as buyer**
- Memory drove the $279B supply commitments. Memory price increases "exceeded our prior expectations" (26 Aug 2026) — [NVIDIA transcript](https://stockanalysis.com/stocks/nvda/transcripts/676136-q2-2027/) [P][F]
- An analyst claims an HBM issue on Rubin was "resolved in October" (12 Nov 2026, unconfirmed) — [Newsquawk](https://newsquawk.com/headlines/citrinis-jukan-says-that-one-thing-ive-been-able-to-confirm-is-that-nvidias-nvda-rubin-has-been-delayed-again-im-told-motherboard-warpage-caused-the-latest-delay-and-that-the-hbm-issue-was-resolved-in-october) [S][F]

**Hybrid bonding**
- SK hynix says full-scale adoption is most likely at HBM4E or HBM5, where stacks are projected to exceed 20 layers — [SK hynix tech note](https://news.skhynix.com/en/tech-note-series-ep2/) [P][SR]
- JEDEC's HBM4 standard (JESD270-4, Apr 2025) allows 775 µm package height for 12-high and 16-high stacks. This lets 16-high HBM4 be built without hybrid bonding — relayed in search results (for example [VLSI.kr](https://www.vlsi.kr/en/hbm-stack-height-8hi-12hi-16hi-en/)) [S][SR]
- SK hynix showed a 16-high HBM4 sample built with MR-MUF at CES 2026, keeping hybrid bonding as backup. One analysis puts the earliest hybrid-bonding insertion at 16-high HBM4E, with 12-high HBM4E expected to stay mainstream — relayed in search results ([Tom's Hardware hybrid-bonding status 2026](https://www.tomshardware.com/tech-industry/semiconductors/hybrid-bonding-roadmap-examined), page body not retrievable; [Nomad Semi](https://www.nomadsemi.com/p/deep-dive-on-hbm)) [S][SR]

### Inferences
- "Tight into 2028" should be upgraded to "contracted and tight through at least 2028, with company claims to 2029".
- Take-or-pay SCAs with cash deposits, and LTAs covering more than half of 2027-28 capacity, change the cycle mechanics. A spending pause would hit spot DRAM and NAND and new-contract pricing first. Contracted HBM volumes would be hit later.
- This weakens the claim that memory is "the first area to turn".
- With JEDEC height relief, and if JEDEC relaxes further to about 900 µm (reported, unverified), hybrid bonding in HBM could slip to HBM5 (2028+). That would extend the life of thermo-compression and MR-MUF solder-bump stacking.

### Gaps
- Not verified: Samsung's HBM4 qualification status at NVIDIA, and the reported Samsung hybrid-bonded 16-high HBM4 samples with about 10% yield (low-tier sources only).
- Not verified: a TrendForce report of 1 Apr 2026 that JEDEC is considering about 900 µm from HBM4E.
- Not verified: Micron's bonding method for HBM4E/HBM5.
- No HBM equipment order data (BESI, Hanmi, Hanwha, ASMPT, Applied Materials).

---

## Claim 5: TSMC A16 slipped from late 2026 to 2027; NVIDIA's 600 kW rack reportedly delayed to 2028 (NVIDIA disputes)

### Takeaway
**Verdict: CONFIRMED on both points**, with important additions since mid-2026:
- Rubin Ultra was reportedly re-scoped from 4 dies and 16 stacks to 2 dies and 8 stacks (unconfirmed).
- A reported NVL72x2 fallback drew pushback from cloud customers.
- On 12 Nov 2026 an analyst claimed base Rubin *volume* slipped to 2027. This is unconfirmed and conflicts with NVIDIA's 26 Aug statement that production shipments began in Aug 2026.

### Cited Findings

**A16**
- TSMC's 2026 symposium roadmap shows A16 (first node with Super Power Rail backside power) in 2027, "slipped from 'late 2026' in last year's roadmap". No reason was given. A14 is targeted for 2028; A13 and A12 for 2029 — [SemiEngineering, 27 Apr 2026](https://semiengineering.com/tsmc-tech-symposium-2026-by-the-numbers/) [S][F]; [TrendForce, 23 Apr 2026](https://www.trendforce.com/news/2026/04/23/news-tsmc-unveils-latest-roadmap-a12-a13-set-for-2029-without-high-na-euv-a16-volume-production-delayed-to-2027/) [S][F]
- On the Q3 call (15 Oct 2026), A16 was not discussed. On A14: "Risk production is well on track for 2027, and volume production will start in 2028". N2 has been in high-volume manufacturing since Q4 2025, was 8% of Q3 2026 wafer revenue, and N2-family capacity is to "more than double in 2027" — [TSMC transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-tsmc-beats-q3-2026-estimates-as-stock-slips-93CH-4950695) [P][F]
- Some secondary blogs cite a VLSI 2026 paper for A16 *initial* production in Q4 2026, as distinct from volume in 2027 — [hw.dev](https://hw.dev/signal/tsmc-a16-superpower-rail-vlsi-production-2026/) [S][SR, unverified]

**600 kW rack (Kyber)**
- NVIDIA's 600 kW figure for Rubin Ultra Kyber racks dates from GTC 2025 — [Wikipedia: Rubin](https://en.wikipedia.org/wiki/Rubin_(microarchitecture)) [S][F, citing source headline]
- SemiAnalysis (post on X, about 6 Jul 2026) reported:
  - The Kyber NVL144 rack for Rubin Ultra slipped more than 12 months toward 2028, because the PCB midplane is hard to manufacture.
  - NVL576 (which depends on CPO) may also be affected.
  - A fallback NVL72x2 back-to-back design drew pushback from large cloud customers.
  - [WinBuzzer, 7 Jul 2026](https://winbuzzer.com/2026/07/07/reported-nvidia-kyber-delay-pushes-ai-rack-toward-2028-xcxwbn/) [S][F]
- NVIDIA's response (about 6-7 Jul 2026, relayed via a Walter Bloomberg post): its AI and chip roadmap "remains intact" and it disputes the report. No date was given for Rubin Ultra or Kyber. Rubin ships in Oberon racks; Rubin Ultra is "slated for Kyber" — [Wccftech, 7 Jul 2026](https://wccftech.com/nvidia-quashes-rubin-kyber-rack-delay-rumors-says-chip-roadmap-is-intact/) [S][F]
- Huang: "Vera Rubin is already in production. Giant amounts of production incoming." He did not address Kyber specifically — [Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/nvidia-ceo-jensen-huang-dismisses-233017030.html) [S][SR]; [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidias-huang-vows-to-deliver-giant-amounts-of-vera-rubin-company-says-that-our-roadmap-is-intact) [S][headline only]
- Rubin Ultra die count: reported shift from 4 to 2 compute dies (Commercial Times via TrendForce, 1 Apr 2026; SemiAnalysis about 30 Jun 2026; Tom's Hardware, 30 Jun 2026). SemiAnalysis estimates roughly half the original performance; Wccftech's sources expect board-level assembly to preserve compute per blade. NVIDIA has not confirmed or published a new spec — [igor'sLAB, 1 Jul 2026](https://www.igorslab.de/en/nvidia-rubin-ultra-four-die-scrapped-reversal/) [S][F]; [Tom's Hardware, 30 Jun 2026](https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-reportedly-cancels-quad-die-rubin-ultra-gpu-in-favor-of-dual-gpu-design-report-claims-complex-design-purportedly-scrapped-over-manufacturing-execution-concerns) [S][SR]

**Base Vera Rubin status**
- NVIDIA "commenced production shipments of Vera Rubin earlier this month" (Aug 2026). It has POs from "every major hyperscaler, AI cloud, and system OEM", and expects Vera Rubin to be about 20% of Q3 FY27 data-centre revenue (quarter ending late Oct 2026; said 26 Aug 2026) — [NVIDIA transcript](https://stockanalysis.com/stocks/nvda/transcripts/676136-q2-2027/) [P][F]
- The press release says racks are running at CoreWeave, Google Cloud, Microsoft Azure, OCI and Nebius — [NVIDIA press release](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027) [P][SR]
- Wikipedia: full production May 2026, deployment Sep 2026 (citing an NVIDIA blog of 30 Sep 2026) — [Wikipedia: Rubin](https://en.wikipedia.org/wiki/Rubin_(microarchitecture)) [S][F]
- Contrary claim (12 Nov 2026), not company-confirmed:
  - Rubin "delayed again" because of motherboard warpage.
  - Volume shipments slipped to 2027.
  - NVIDIA raised Blackwell orders in the meantime.
  - Newsquawk says to treat it as directional until corroborated.
  - [Newsquawk](https://newsquawk.com/headlines/citrinis-jukan-says-that-one-thing-ive-been-able-to-confirm-is-that-nvidias-nvda-rubin-has-been-delayed-again-im-told-motherboard-warpage-caused-the-latest-delay-and-that-the-hbm-issue-was-resolved-in-october) [S][F]

**Feynman (2028), as shown at GTC Mar 2026**
- A new GPU, the LP40 LPU (built with the Groq team), the Rosa CPU (successor to Vera), BlueField 5, and both copper and co-packaged optical scale-up. Kyber scales to NVL1152 (eight times the NVL144 density) — [HPCwire/AIwire, 18 Mar 2026](https://www.hpcwire.com/aiwire/2026/03/18/huang-shares-nvidia-roadmap-showing-more-chips-nvl1152-scale-up-cpo/) [S][SR]; [Atlan](https://atlan.com/know/nvidia-gtc-2026-keynote-recap/) [S][SR]; [Jon Peddie Research](https://www.jonpeddie.com/news/nvidia-gtc-2026-keynote/) [S][SR]
- Memory: Micron's NVHBM custom HBM4E "to be adopted on next generation of GPUs" — [Micron remarks](https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf) [P][F]
- Packaging: NVIDIA Feynman is reportedly the first CoPoS adopter (2028-29) — [TrendForce, 15 Jun 2026](https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-reportedly-seen-narrowing-from-20-to-10-by-end-2026-as-capacity-expands/) [S][F]
- Process node: **no 2026 source retrieved that names Feynman's node.** A16 is widely assumed but was not verified this session.

### Inferences
- NVIDIA's denial is general ("roadmap intact") and dateless. It is compatible with a Rubin Ultra launch in 2027 on a scaled-back package and copper scale-up, with the 600 kW Kyber in volume only in 2028.
- The specific 2027-vs-2028 question for Kyber remains open. NVIDIA's Q3 FY27 results (expected late Nov 2026, date not confirmed here) are the next test of both the base Rubin ramp and the 12 Nov slip claim.

### Gaps
- No Computex Jun 2026 or GTC DC Oct 2026 keynote material was retrieved.
- Feynman's process node, die stacking and HBM generation were not confirmed from a primary source.
- Rubin Ultra's 2027 rack form factor (Oberon or Kyber) is not confirmed.

---

## Claim 6: Processors up to 2.3 kW heading to 4 kW; cold plates about 100-150 kW per rack; two-phase held by fluorinated-coolant rules; in-chip channels unproven

### Takeaway
**Verdict: PARTLY CONFIRMED; partly outdated; partly could not verify.**
- **Power trajectory confirmed** from secondary estimates only. NVIDIA publishes no per-GPU TDP for Rubin or Rubin Ultra. Note that Rubin Ultra's reported shrink to 2 dies would lower its per-package power.
- **Cold-plate ceiling of 100-150 kW looks outdated.** Direct-to-chip liquid cooling is the baseline for Rubin Ultra and Kyber at up to 600 kW per rack, and cold plates are expected to dominate through at least 2028.
- **Two-phase hold-up confirmed**, but the cause is broader than regulation: PFAS-free two-phase fluids are not production-qualified.
- **In-chip cooling:** no production evidence found.

### Cited Findings

**Per-processor power (secondary estimates)**
- Rubin about 1.8 kW baseline and about 2.3 kW in a higher configuration (Ming-Chi Kuo). A Pegatron rating supports 2.3 kW. NVIDIA publishes no per-GPU Rubin TDP — relayed in search results ([AI Data Center Guide](https://aidatacenterguide.com/part-7-compute-silicon-and-system-integration/7-2-nvidia-accelerators-hopper-blackwell-vera-rubin-rubin-ultra-feynman); [Thunder Compute](https://www.thundercompute.com/blog/nvidia-rubin-architecture)) [S, low-tier][SR]
- KAIST TERA Lab projections: Rubin Ultra (2027) 3,600 W with direct-to-chip cooling; Feynman-class about 4,400 W. Other industry sources say Feynman Ultra could reach 6,000 W. Future modules up to 15,360 W would need immersion or embedded cooling — [Tom's Hardware](https://www.tomshardware.com/pc-components/cooling/future-ai-processors-said-to-consume-up-to-15-360w-massive-power-draw-will-demand-exotic-immersion-and-embedded-cooling-tech) [S][SR; body not retrievable]

**Cold plates**
- "Direct-to-chip cold plates will remain the dominant liquid cooling technology through at least 2028" — relayed in search results ([The Cooling Report](https://thecoolingreport.com/intel/data-center-cooling-systems-complete-guide-2026.html)) [S][SR]
- Rubin Ultra Kyber is planned at 600 kW per rack, with direct-to-chip cooling per the KAIST table cited above [S][SR]

**Two-phase cooling and fluorinated coolants**
- The EU's proposed PFAS restriction covers more than 10,000 substances. ECHA's final opinions are expected by end-2026, with a vote expected in early 2027.
- R1233zd, the leading two-phase direct-to-chip refrigerant, counts as PFAS under the broad OECD definition but not under the US EPA's narrower working definition.
- No hydrocarbon or ester two-phase fluid was production-qualified at data-centre scale as of mid-2026.
- [The Cooling Report](https://thecoolingreport.com/intel/pfas-two-phase-immersion-cooling-crisis.html) [S][SR]; [Jason Agee Substack](https://jasonagee.substack.com/p/two-phase-non-pfas-liquid-cooling) [S][SR]
- ZutaCore pledged a PFAS-free direct-on-chip two-phase product for 2026 — [DCD](https://www.datacenterdynamics.com/en/news/zutacores-two-phase-cooling-will-eliminate-pfas-in-2026/) [S][SR]. Company claim, unconfirmed.

**Heat warnings**
- The OCP Global Summit 2026 (San Jose, from 12 Oct 2026) included a "warning on heat" theme — [TechArena](https://techarena.ai/content/ocp-global-summit-2026-agents-800-volts-and-a-warning-on-heat) [S][SR]. Details not retrieved.

### Inferences
- Single-phase cold plates are being pushed far beyond the claim's 100-150 kW per rack. Today's limit is set by rack power and facility water temperature and flow, not by cold-plate physics alone.
- That extends the life of cold plates, one of the "bridging" technologies, and pushes two-phase toward niche use until PFAS rules settle (vote early 2027) and alternative fluids qualify.
- If Rubin Ultra is really 2 dies (about 1.8 kW-class each), the "4 kW per processor" step moves to Feynman (2028) or later.

### Gaps
- No primary rack-level kW figures for GB300 NVL72 or Vera Rubin NVL144 were retrieved this session.
- No primary data on microfluidic or in-chip cooling deployments (Microsoft, TSMC). The claim of "unproven in production" stands only for lack of contrary evidence.

---

## Claim 7: Optics in switches shipping in 2026; NVIDIA and its packaging partner plan 15x optical-engine capacity by mid-2027; processor-to-processor optics planned for 2028 (may slip to 2028-29); copper stretched to 2027-28

### Takeaway
**Verdict: CONFIRMED, with updates.**
- CPO switches are in production at NVIDIA and Broadcom in 2026, but at low volume (about 10-15k units). The volume ramp is expected in 2027-28.
- NVIDIA confirmed a 15x expansion of optical-engine capacity with **SPIL** (ASE group) by mid-2027 (21 Oct 2026).
- CPO between processors first appears in multi-rack NVL576 and Feynman NVL1152 systems. NVL576 is exposed to the Kyber slip.
- Copper is stretched further than the claim says: Rubin Ultra scale-up is copper-only, and Feynman keeps a copper scale-up option.

### Cited Findings

**CPO switches**
- NVIDIA Quantum-X Photonics (InfiniBand CPO) began shipping in early 2026 at low volume, after slipping from late 2025. Spectrum-X Ethernet Photonics was in production by 31 May 2026, with CoreWeave, Lambda and OCI named — [Longbridge](https://longbridge.com/en/topics/100000000858275) [S][SR]; [NVIDIA developer blog](https://developer.nvidia.com/blog/scaling-ai-factories-with-co-packaged-optics-for-better-power-efficiency/) [P][SR]
- TrendForce (27 Jul 2026):
  - NVIDIA's Spectrum-X CPO (TSMC COUPE packaging, up to 400 Tb/s) is shipping to select partners, with capacity expanding in 2H 2026.
  - Broadcom's 51.2T Bailly CPO is in volume manufacturing with Delta Electronics and Micas Networks, validated with Meta, and cuts power by up to 70% versus pluggables.
  - The CPO switch volume ramp is expected in 2027-2028.
  - Vertical integration is expected to become the default strategy.
  - [TrendForce press release](https://www.trendforce.com/presscenter/news/20260727-13151.html) [S][F]
- 2026 CPO switch units: SemiAnalysis estimates 10-15k. Foxconn's chairman reportedly said about 10k in 2026, with 2027 "several times" higher — relayed in search results ([SemiAnalysis CPO](https://newsletter.semianalysis.com/p/co-packaged-optics-cpo-book-scaling)) [S][SR]
- NVIDIA formally unveiled the Spectrum-6 line in Jul 2026. The optical version is reportedly 409.6 Tb/s across 512 ports at 800 Gb/s — [SDxCentral, 21 Oct 2026](https://www.sdxcentral.com/news/nvidia-targets-15x-optics-capacity-expansion-by-2027-to-meet-cpo-demand/) [S][F]

**15x optical-engine capacity**
- At GTC Berlin, NVIDIA confirmed a plan with SPIL to raise CPO optical-engine capacity 15x by mid-2027. A further doubling by end-2028 is attributed to the vendor. Other optics suppliers named: Amkor, Samsung Electro-Mechanics, Unimicron (21 Oct 2026) — [SDxCentral](https://www.sdxcentral.com/news/nvidia-targets-15x-optics-capacity-expansion-by-2027-to-meet-cpo-demand/) [S][F]. Company plan, unconfirmed by SPIL in the retrieved material.
- TSMC reportedly plans to expand photonic IC capacity more than 30x in three years — [iTiger](https://www.itiger.com/news/1131192118) [S][SR]

**Scale-up optics and copper**
- SemiAnalysis's reading of GTC 2026: NVL144 Kyber will not use CPO for scale-up. Rubin Ultra gets copper scale-up in both Oberon and Kyber. CPO scale-up debuts with Rubin Ultra NVL576 and Feynman NVL1152 — [SemiAnalysis](https://newsletter.semianalysis.com/p/nvidia-the-inference-kingdom-expands) [S][SR]. Some outlets instead said Kyber uses CPO ([DEV Community](https://dev.to/max_quimby/nvidia-gtc-2026-every-ai-announcement-developers-need-to-know-1njb), [SR]). SemiAnalysis is the more detailed source.
- Feynman bundles "both copper and co-packaged optical scale-up networking" — [Atlan](https://atlan.com/know/nvidia-gtc-2026-keynote-recap/) [S][SR]; [HPCwire, 18 Mar 2026](https://www.hpcwire.com/aiwire/2026/03/18/huang-shares-nvidia-roadmap-showing-more-chips-nvl1152-scale-up-cpo/) [S][SR]
- NVL576 "may also be affected" by the Kyber delay because it depends on CPO readiness (Jul 2026) — [WinBuzzer](https://winbuzzer.com/2026/07/07/reported-nvidia-kyber-delay-pushes-ai-rack-toward-2028-xcxwbn/) [S][F]
- Laser and component supply: CW lasers, fiber arrays and TSMC COUPE capacity are reportedly sold out into 2027. Taiwanese suppliers report order books full through 2027 and supply tight into 2028 — relayed in search results [S][SR, unattributed]
- NVIDIA's 2026 supply deals with Corning, Lumentum and Coherent are tied to EML laser concerns — [SDxCentral](https://www.sdxcentral.com/news/nvidia-targets-15x-optics-capacity-expansion-by-2027-to-meet-cpo-demand/) [S][F]

### Inferences
- CPO in scale-out switches is the first of the six successors in production. The volume inflection comes in 2027 as SPIL capacity scales.
- Optics between processors at volume is a 2028 event at the earliest. It is more likely 2028-29, given the Kyber and NVL576 exposure and Feynman's copper option.
- Copper scale-up (cables, backplanes, midplanes) is stretched beyond 2028 rather than ending in 2027-28.
- The midplane-PCB problem behind the Kyber report shows the copper bridge has its own manufacturing limits. That shifts value toward high-layer-count PCB and connector specialists in 2027-28.

### Gaps
- No primary NVIDIA statement dating NVL576 or the first CPO scale-up system after the July 2026 reports.
- No Broadcom primary material (for example Tomahawk 6 Davisson CPO) or Broadcom earnings commentary was retrieved.
- No data on pluggable 1.6T module volumes.

---

## Claim 8: Probabilities (treated as priors)

### Takeaway
Evidence supports most priors. It argues for raising the "memory supply-limited through 2028" probability, and for questioning "memory turns first in a pause". 70% "a 2028 technology misses" and 65% "600 kW in 2028, not 2027" look reasonable. 50% "1 MW in production by 2030" looks reasonable. "Bridging hardware lasts longer" is well supported.

### Cited Findings
- **(a) At least one 2028 technology (A16-class process, panel packaging, processor-to-processor optics) misses volume in 2028; prior 70%.**
  - A16 is now in volume in 2027, which helps the A16 component — [SemiEngineering](https://semiengineering.com/tsmc-tech-symposium-2026-by-the-numbers/)
  - CoPoS pilot production is mid-2027, with full-scale production in 2028-29, and Wei says "2-3 more years" — [TrendForce, 15 Jun 2026](https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-reportedly-seen-narrowing-from-20-to-10-by-end-2026-as-capacity-expands/); [BigGo](https://finance.biggo.com/news/kLg0kp4BrX5PFN7BKrXD)
  - Processor-to-processor CPO depends on NVL576 and Kyber, which are reportedly delayed. Feynman retains a copper option — [WinBuzzer](https://winbuzzer.com/2026/07/07/reported-nvidia-kyber-delay-pushes-ai-rack-toward-2028-xcxwbn/); [Atlan](https://atlan.com/know/nvidia-gtc-2026-keynote-recap/)
- **(b) 600 kW rack in volume in 2028 rather than 2027; prior 65%.**
  - SemiAnalysis reported a slip of more than 12 months; NVIDIA disputes without a date — [WinBuzzer](https://winbuzzer.com/2026/07/07/reported-nvidia-kyber-delay-pushes-ai-rack-toward-2028-xcxwbn/); [Wccftech](https://wccftech.com/nvidia-quashes-rubin-kyber-rack-delay-rumors-says-chip-roadmap-is-intact/)
  - Rubin Ultra reportedly re-scoped — [igor'sLAB](https://www.igorslab.de/en/nvidia-rubin-ultra-four-die-scrapped-reversal/)
  - Base Rubin may itself be slipping (unconfirmed) — [Newsquawk](https://newsquawk.com/headlines/citrinis-jukan-says-that-one-thing-ive-been-able-to-confirm-is-that-nvidias-nvda-rubin-has-been-delayed-again-im-told-motherboard-warpage-caused-the-latest-delay-and-that-the-hbm-issue-was-resolved-in-october)
  - Facility-side 800 VDC: rack-level in 2027, data hall in 2028 (Citi, as relayed) — [Converge Digest](https://convergedigest.com/ocp-800-vdc-standard-megawatt-ai-racks/) [SR]
- **(c) 1 MW racks in production use by end-2030; prior 50%.**
  - The OCP Mt. Diablo v1.0.0 spec (8 Oct 2026) supports ±400 VDC and 800 VDC power racks scalable from 800 kW to 1 MW+ — [OCP spec](https://www.opencompute.org/wp-content/uploads/2026/10/OCP-Specification-Mt.-Diablo-Disaggregated-Power-Rack-Specification-v1.0.0.pdf) [P][SR]
  - NVIDIA says 800 VDC support for 1 MW racks starts in 2027 (company claim, unconfirmed) — [Converge Digest](https://convergedigest.com/ocp-800-vdc-standard-megawatt-ai-racks/) [SR]
  - Feynman NVL1152 is a multi-rack system; no per-rack 1 MW NVIDIA product was confirmed — [HPCwire](https://www.hpcwire.com/aiwire/2026/03/18/huang-shares-nvidia-roadmap-showing-more-chips-nvl1152-scale-up-cpo/) [SR]
- **(d) Memory supply-limited through 2028; prior 70%.**
  - Micron: DRAM supply-constrained in 2027 and 2028, "no line of sight" to balance — [Micron](https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf)
  - SK hynix: sold out through 2029, with LTAs over 50% of 2027-28 capacity — [TrendForce](https://www.trendforce.com/news/2026/10/28/news-sk-hynix-3q26-opm-hits-record-80-says-dram-hbm-effectively-sold-out-to-2029-14-lta-customers-signed/)
  - NVIDIA: memory-led commitments of $279B — [NVIDIA](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027)
  - Against "first to turn": take-or-pay SCAs with $32B of mostly cash deposits — [Micron](https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf)
- **(e) Bridging hardware loses share in 2028-30 but lasts longer.**
  - Copper scale-up kept through Rubin Ultra and offered with Feynman — [SemiAnalysis](https://newsletter.semianalysis.com/p/nvidia-the-inference-kingdom-expands); [Atlan](https://atlan.com/know/nvidia-gtc-2026-keynote-recap/)
  - MR-MUF used for 16-high HBM4 and hybrid bonding deferred — [SK hynix tech note](https://news.skhynix.com/en/tech-note-series-ep2/)
  - Cold plates dominant through at least 2028 — [The Cooling Report](https://thecoolingreport.com/intel/data-center-cooling-systems-complete-guide-2026.html)
  - CPO volume ramp only in 2027-28 — [TrendForce](https://www.trendforce.com/presscenter/news/20260727-13151.html)

### Inferences (assessment of each prior)
- **(a) 70%: reasonable, arguably 75-80%.**
  - A16 has moved *earlier* relative to Feynman's needs, because volume in 2027 lowers that risk.
  - But CoPoS volume is 2028-29, and processor-to-processor CPO depends on a rack that is reportedly late.
  - Note a definitional risk: if Feynman launches on CoWoS-L with copper scale-up, NVIDIA can ship Feynman in 2028 while two of the three technologies miss. The report should define "miss" by technology, not by product.
- **(b) 65%: reasonable, perhaps 65-75%.** Several independent reports (die-count re-scope, midplane PCB, NVL72x2 fallback, base-Rubin warpage claim) point the same way. The only counter-evidence is NVIDIA's dateless denial. The Q3 FY27 call (late Nov 2026) could move this.
- **(c) 50%: reasonable.** The standards (OCP v1.0, Oct 2026) and vendor intent exist, and NVIDIA dates 1 MW-capable 800 VDC from 2027. However, no 1 MW rack product is named, and 600 kW itself is slipping.
- **(d) 70% looks too low; evidence supports about 80-85%.** The second half of the prior ("memory is the first area to turn in a pause") is weakened. Contracted take-or-pay and deposit structures mean neocloud capacity, leased shells and spot memory pricing would likely turn before contracted HBM volumes.
- **(e) Supported.** Every bridge examined (copper scale-up, pluggables, MR-MUF/TC bonding, cold plates) has a successor that slipped or is gated during 2026.

### Gaps
- No primary source for Feynman's process node. A clean test of (a) is not possible.
- No vendor statement on a 1 MW rack product date.

---

## Spending scenarios: evidence for and against, and whether 55/25/20 looks reasonable

### Takeaway
2027 spending intentions point up (Alphabet, Amazon and Microsoft all signal more), and suppliers see demand above supply. That supports the base case through 2027.

Financing stress is already visible in Q4 2026: CoreWeave credit, aggregate negative hyperscaler free cash flow in Q3, record debt issuance, political moratoria risk, and vendor financing. Forecasters see AI debt issuance *falling* in 2028, which is consistent with a pause around 2028.

Acceleration is capped by supply (NVIDIA through Jan 2028; memory through 2028; power interconnection), so faster growth in delivered compute before 2028 is unlikely. Dollar spending could still accelerate through price inflation.

### Cited Findings

**For steady growth (base case)**
- 2027 signals from the hyperscalers: Alphabet "increase significantly", Amazon "meaningfully more", Microsoft H2 FY27 to "accelerate" — [Yield Theory](https://www.yieldtheory.app/research/hyperscaler-capex-2027-forecast) [S][F]
- Supplier outlooks: NVIDIA FY28 about +70% and supply-limited; TSMC AI-accelerator CAGR "probably higher" than mid-to-high 50s %; AMD data-centre AI to "significantly more than double" in 2027 — [NVIDIA](https://stockanalysis.com/stocks/nvda/transcripts/676136-q2-2027/); [TSMC](https://www.investing.com/news/transcripts/earnings-call-transcript-tsmc-beats-q3-2026-estimates-as-stock-slips-93CH-4950695); [AMD](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/) [P][F]
- Compute growth of 2.2-3.3x a year — [Epoch AI](https://epoch.ai/data-insights/ai-computing-capacity-additions-doubling) [SR]
- Microsoft says it remains free-cash-flow positive in FY27 — [investingLive](https://investinglive.com/stocks/microsoft-sees-170bn-capex-in-fiscal-2027-but-says-it-will-stay-cash-flow-positive/) [S][F]

**For a financing-led pause (and its timing)**
- Credit and cash-flow signals:
  - CoreWeave bond yield above 16% and CDS above 1,289 bp on 5 Nov 2026.
  - NVIDIA CDS up 76% in a month to about 139 bp; Broadcom CDS up 49%; Amazon CDS up 44%; Oracle CDS about 298 bp. CNBC notes these remain low in absolute terms.
  - Hyperscalers collectively had negative free cash flow in Q3 2026.
  - Goldman: "Delayed monetization and growth in purchase commitments" are key risks.
  - Jefferies' Chris Wood: "The most plausible way the AI capex arms race will end is that the credit card will be taken away."
  - [CNBC, 6 Nov 2026](https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html) [S][F]
- Debt volumes:
  - Goldman: $296B of hyperscaler debt issued in 2026 to early Nov; five AI bond deals of $67B since 29 Oct 2026; 2027 forecast of $440B hyperscaler debt plus about $300B of project-level issuance.
  - BofA: AI-related credit issuance up 31% to $685B in 2027, then **down 23% to $531B in 2028**.
  - [CNBC, 6 Nov 2026](https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html) [S][F]
- Earlier 2026 estimates of total AI-related debt: Goldman about $489B (Jul), Morgan Stanley about $570B, later Goldman above $750B on a wider definition. Hyperscaler bond deal coverage reportedly fell from about 5x (Feb) to under 2x (Jul), with money moving to private credit and off-balance-sheet vehicles. Morgan Stanley sees about $800B of private-credit opportunity in data-centre finance through 2028 — [Forbes, 17 Jul 2026](https://www.forbes.com/sites/robertszczerba/2026/07/17/bond-investors-push-back-as-ai-debt-heads-toward-570-billion/) [S][SR]; [JPMorgan AM](https://am.jpmorgan.com/gb/en/asset-management/institutional/insights/market-insights/market-updates/on-the-minds-of-investors/hyperscaler-debt-issuance-ai-buildout/) [S][SR]
- Pimco anchored Meta's $27.3B Hyperion data-centre bond, buying $18B (as described in a late-Oct 2026 piece; the original deal date was not verified) — [Forbes, 22 Oct 2026](https://www.forbes.com/sites/mayrarodriguezvalladares/2026/10/22/the-half-trillion-dollar-silicon-gamble-inside-the-ai-debt-boom/) [S][SR; page returned 403]
- Political risk: investors fear delays under incoming Democratic governors in Ohio, Texas and Georgia. Texas governor-elect Gina Hinojosa wants a moratorium until community protections pass. Goldman says moratoria could affect 45% of planned US capacity — [CNBC, 6 Nov 2026](https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html) [S][F]
- Vendor financing and circularity (26 Aug 2026; company claims):
  - NVIDIA has invested "nearly $50 billion in the frontier AI labs".
  - Financing platforms with six capital providers to "raise over $500 billion of third-party capital".
  - "take or pay commitment on a portion of the facility's capacity" for neoclouds.
  - "selective credit enhancement for nearly 2 GW" for a frontier lab.
  - OpenAI about 12 GW of NVIDIA compute commitments.
  - [NVIDIA transcript](https://stockanalysis.com/stocks/nvda/transcripts/676136-q2-2027/) [P][F]
- AMD (3 Nov 2026): warrants issued to a customer as MI450 ships, with a $1.1B non-cash charge in Q3 2026 that is expected to grow; "selectively investing with our lead partners"; $4.75B senior notes in Aug 2026 — [AMD transcript](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/) [P][F]
- Deferrals and frictions:
  - Microsoft's capex shortfall from late third-party capacity — [investingLive](https://investinglive.com/stocks/microsoft-sees-170bn-capex-in-fiscal-2027-but-says-it-will-stay-cash-flow-positive/)
  - Oracle force majeure at the New Mexico Stargate campus — [Power Engineering](https://www.power-eng.com/renewables/america-data-center-construction-delays/)
  - Stargate partner disputes between OpenAI, Oracle and SoftBank over control (reported; date not pinned, likely 2025-26) — [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/stargate-ai-data-centers-for-openai-reportedly-delayed-by-squabbles-between-partners-sources-say-openai-oracle-and-softbank-disagreed-on-who-would-have-ultimate-control-of-the-planned-data-centers) [S][SR]
- Microsoft "would consider other ways of raising capital" if attractive — [investingLive](https://investinglive.com/stocks/microsoft-sees-170bn-capex-in-fiscal-2027-but-says-it-will-stay-cash-flow-positive/) [S][F]

**For faster acceleration**
- TSMC demand "far above our capability today to supply" — [TSMC](https://www.investing.com/news/transcripts/earnings-call-transcript-tsmc-beats-q3-2026-estimates-as-stock-slips-93CH-4950695) [P][F]
- NVIDIA: demand "much higher" than the 70% growth it can supply; cloud backlog above $2T (company claim) — [NVIDIA](https://stockanalysis.com/stocks/nvda/transcripts/676136-q2-2027/) [P][F]
- Memory customers lock supply to 2031 with $32B of deposits — [Micron](https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf) [P][F]
- SK hynix sold out through 2029 — [TrendForce](https://www.trendforce.com/news/2026/10/28/news-sk-hynix-3q26-opm-hits-record-80-says-dram-hbm-effectively-sold-out-to-2029-14-lta-customers-signed/) [S][F]
- Goldman's 2027 forecast of $1.2T for five companies is above the Street — [Yield Theory](https://www.yieldtheory.app/research/hyperscaler-capex-2027-forecast) [S][F]

### Inferences (probability check)
- **Steady growth (55%):** reasonable for 2027. The guidance is explicit and supply-limited.
- **Financing-led pause around 2028 (25%):** reasonable to somewhat low; a range of about 25-35% is defensible.
  - Stress has started in Q4 2026, but in the leveraged tier (neoclouds, project-financed campuses, vendor-financed labs).
  - BofA's projected 23% fall in AI credit issuance in 2028 lines up with the claimed timing.
  - A likely sequence: neocloud and lease pullback and project delays in 2027, then hyperscaler 2028 budgets set on Q4 2027 calls.
  - Political moratoria from Jan 2027 could act as a non-financial trigger with financial consequences.
- **Faster acceleration (20%):** looks somewhat high **for delivered compute** before 2028. Logic (TSMC), memory (Micron and SK hynix), packaging and power all cap supply through 2027-28; an estimate of about 15% is defensible. In **dollar** terms acceleration is more plausible, through memory, CoWoS and tool price inflation.
- The report should state whether its scenarios are in dollars or in compute units.

### Gaps
- No 2026 OpenAI financing primary data (funding rounds, total compute commitments).
- A single source claimed OpenAI projects about $750B of compute spending through 2030 and a funding round cut to about $20B. Both are unverified and excluded.
- No private-credit spread data. No GPU-backed loan default data.
- No neocloud capex figures (CoreWeave, Nebius, Lambda, Crusoe). No sovereign programme figures.
- Chinese hyperscaler capex not obtained.

---

## Timeline table: six transitions

### Takeaway
- The first successor in volume is **co-packaged optics in scale-out switches**: in production in 2026, volume ramp 2027-28.
- Next: **±400 VDC sidecar and 800 VDC rack power** (rack-level 2027, data hall 2028), then hybrid-bonded HBM (16-high HBM4E, 2027-28 at earliest, possibly HBM5 in 2028+), then panel and glass packaging (2028-29), then processor-to-processor optics (2028+).
- Two-phase cooling has no dated vendor roadmap.
- At least four of the six transitions slipped or were re-scoped during 2026.

### Table

| Transition | Original target (where found) | Current target (as of Nov 2026) | Slip in 2026 | Evidence |
|---|---|---|---|---|
| Copper to optical links between processors (scale-up CPO) | GTC 2026 roadmap (Mar 2026): CPO scale-up debuts with Rubin Ultra NVL576 (Kyber, 2027) and Feynman NVL1152 (2028) | NVL576 "may also be affected" by the reported Kyber slip to 2028. Feynman keeps a copper option. Volume CPO scale-up 2028-29 at the earliest. | About 1 year for the first system (reported; NVIDIA disputes) | [SemiAnalysis](https://newsletter.semianalysis.com/p/nvidia-the-inference-kingdom-expands) [SR]; [WinBuzzer, 7 Jul 2026](https://winbuzzer.com/2026/07/07/reported-nvidia-kyber-delay-pushes-ai-rack-toward-2028-xcxwbn/) [F]; [Atlan](https://atlan.com/know/nvidia-gtc-2026-keynote-recap/) [SR] |
| Pluggable modules to co-packaged optics (switches) | Quantum-X Photonics late 2025; Spectrum-X Photonics 2026 | Quantum-X early 2026 at low volume. Spectrum-X Photonics in production by 31 May 2026. Broadcom Bailly in volume manufacturing. About 10-15k units in 2026. Volume ramp 2027-28. Optical engines 15x by mid-2027 (SPIL). | About 1 quarter (Quantum-X) | [Longbridge](https://longbridge.com/en/topics/100000000858275) [SR]; [TrendForce, 27 Jul 2026](https://www.trendforce.com/presscenter/news/20260727-13151.html) [F]; [SDxCentral, 21 Oct 2026](https://www.sdxcentral.com/news/nvidia-targets-15x-optics-capacity-expansion-by-2027-to-meet-cpo-demand/) [F] |
| Solder-bump/TC/MR-MUF stacking to hybrid bonding (HBM) | Industry expectation for 16-high HBM4 (about 2026) before JEDEC set 775 µm (JESD270-4, Apr 2025) | 16-high HBM4 built with MR-MUF. Earliest hybrid bonding at 16-high HBM4E (2027-28). SK hynix points to HBM4E or HBM5 (2028). | At least one generation, about 1-2 years | [SK hynix tech note](https://news.skhynix.com/en/tech-note-series-ep2/) [SR]; [VLSI.kr](https://www.vlsi.kr/en/hbm-stack-height-8hi-12hi-16hi-en/) [SR]; [TechTimes, 22 Oct 2026](https://www.techtimes.com/articles/329350/20261022/micron-maps-annual-hbm-advances-2030-rejects-chinese-density-workaround.htm) [F] |
| Silicon interposers to panel (CoPoS) and glass | CoPoS: pilot line 2026, volume end-2028/2029. Glass: several makers targeting 2026-27. | CoPoS: line built and qualifying (Jun 2026); pilot production mid-2027; full-scale 2028-29 (Feynman first). Glass: SEMCO core 2H27 and substrates 2028 (orders slipped three times; possibly 2028+); SKC/Absolics to 2027; DNP 2028; Intel uncommitted. | CoPoS pilot production about 0.5-1 year (one report). Glass about 0.5-1+ years. | [TrendForce, 15 Jun 2026](https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-reportedly-seen-narrowing-from-20-to-10-by-end-2026-as-capacity-expands/) [F]; [TrendForce, 13 Apr 2026](https://www.trendforce.com/news/2026/04/13/news-tsmc-advances-panel-level-packaging-copos-pilot-line-reportedly-set-for-june-completion-2028-29-ramp-eyed/) [SR]; [TrendForce, 18 Aug 2026](https://www.trendforce.com/news/2026/08/18/news-glass-substrate-war-heats-up-shinko-electric-advances-22-layer-product-as-samsung-reportedly-faces-ramp-up-uncertainty/) [F] |
| Cold plates to two-phase cooling | No vendor-dated roadmap found. Two-phase was expected for 2 kW+ class chips. | Single-phase direct-to-chip is the baseline for Rubin Ultra and Kyber; cold plates dominant through at least 2028. EU PFAS: ECHA opinions end-2026, vote early 2027. No non-PFAS two-phase fluid production-qualified as of mid-2026. | Undated or indefinite | [The Cooling Report](https://thecoolingreport.com/intel/pfas-two-phase-immersion-cooling-crisis.html) [SR]; [DCD](https://www.datacenterdynamics.com/en/news/zutacores-two-phase-cooling-will-eliminate-pfas-in-2026/) [SR]; [Tom's Hardware/KAIST](https://www.tomshardware.com/pc-components/cooling/future-ai-processors-said-to-consume-up-to-15-360w-massive-power-draw-will-demand-exotic-immersion-and-embedded-cooling-tech) [SR] |
| Today's rack power to 600 kW and 1 MW on 800 VDC | Kyber 600 kW in 2H 2027 (GTC 2025). NVIDIA 800 VDC from 2027. | Kyber reportedly 2028 (NVIDIA: "roadmap intact"). OCP Mt. Diablo v1.0.0 (8 Oct 2026): ±400 VDC and 800 VDC, 800 kW-1 MW+. Citi: rack-level 800 VDC 2027, data hall 2028. No 1 MW rack product named. | About 12 months (reported) | [Wikipedia: Rubin](https://en.wikipedia.org/wiki/Rubin_(microarchitecture)) [F]; [Wccftech](https://wccftech.com/nvidia-quashes-rubin-kyber-rack-delay-rumors-says-chip-roadmap-is-intact/) [F]; [OCP spec](https://www.opencompute.org/wp-content/uploads/2026/10/OCP-Specification-Mt.-Diablo-Disaggregated-Power-Rack-Specification-v1.0.0.pdf) [P][SR]; [Converge Digest](https://convergedigest.com/ocp-800-vdc-standard-megawatt-ai-racks/) [SR] |

### Cited Findings: who captures the value (integrated firms vs specialists)
- **TSMC pricing power and control**
  - A reported ~20% CoWoS price rise (27 Oct 2026) — [TrendForce](https://www.trendforce.com/news/2026/10/27/news-tsmc-reportedly-eyes-20-cowos-price-hike-skips-equipment-price-renegotiations-amid-ai-demand-surge/) [SR]
  - TSMC does not "allow our customer to sublet or auction off the capacity" — [TSMC transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-tsmc-beats-q3-2026-estimates-as-stock-slips-93CH-4950695) [P][F]
  - TSMC is also outsourcing: interposers to GlobalFoundries (Q3 call), and OSATs add 50-60k wafers per month of CoWoS-type capacity — [TrendForce, 15 Jun 2026](https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-reportedly-seen-narrowing-from-20-to-10-by-end-2026-as-capacity-expands/) [F]
  - TSMC's COUPE is inside NVIDIA's Spectrum-X CPO switch — [TrendForce, 27 Jul 2026](https://www.trendforce.com/presscenter/news/20260727-13151.html) [F]
- **NVIDIA naming specialist suppliers**
  - SPIL is the 15x optical-engine partner. Amkor, SEMCO and Unimicron are named optics suppliers. Corning, Lumentum and Coherent have 2026 supply deals — [SDxCentral, 21 Oct 2026](https://www.sdxcentral.com/news/nvidia-targets-15x-optics-capacity-expansion-by-2027-to-meet-cpo-demand/) [F]
  - NVIDIA finances customers: about $50B in labs, take-or-pay, credit enhancement — [NVIDIA transcript](https://stockanalysis.com/stocks/nvda/transcripts/676136-q2-2027/) [P][F]
- **Broadcom CPO built by specialist ODMs** (Delta, Micas) — [TrendForce, 27 Jul 2026](https://www.trendforce.com/presscenter/news/20260727-13151.html) [F]
- **Memory makers capturing value**
  - SK hynix operating margin about 80% (Q3 2026) — [TrendForce](https://www.trendforce.com/news/2026/10/28/news-sk-hynix-3q26-opm-hits-record-80-says-dram-hbm-effectively-sold-out-to-2029-14-lta-customers-signed/) [F]
  - Micron SCAs with price floors and ceilings and $32B of deposits — [Micron](https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf) [P][F]
  - NVIDIA says memory price increases exceeded expectations — [NVIDIA transcript](https://stockanalysis.com/stocks/nvda/transcripts/676136-q2-2027/) [P][F]
- **Vertical integration expected to be the default in CPO** — [TrendForce, 27 Jul 2026](https://www.trendforce.com/presscenter/news/20260727-13151.html) [F]
- **Open standards in rack power**: Microsoft contributed its Mt. Diablo 800 V architecture to OCP — [Converge Digest](https://convergedigest.com/ocp-800-vdc-standard-megawatt-ai-racks/) [SR]

### Inferences
- In 2026, value is accruing most visibly to bottleneck owners with contract power: memory makers, through take-or-pay and deposits, and TSMC, through price rises and a ban on reselling capacity.
- NVIDIA is pulling specialists into its supply chain by naming them (SPIL, Amkor, SEMCO, Unimicron, lasers) while also financing demand. That favours named specialists on volume, while NVIDIA keeps system-level pricing.
- TrendForce's view that CPO will consolidate around vertically integrated players (NVIDIA plus TSMC, Broadcom) argues against independent pluggable-module makers capturing CPO value. Supporting evidence is limited to that one analyst view.
- In rack power, open OCP specs (Mt. Diablo) point to standardisation, which tends to cap specialists' pricing power over time. This is an inference only; no pricing data was found.

### Gaps
- No 2026 data on Samsung's integrated (memory plus foundry plus packaging) offer winning sockets.
- No primary evidence on Broadcom's reference designs naming suppliers.
- No supplier equity investments by NVIDIA in packaging or optics firms were verified this session.

---

## Export controls and tariffs (in force or pending, Nov 2026)

### Takeaway
- **US:** chip export policy to China moved in Jan 2026 to case-by-case licensing for H200/MI325X-class parts, under testing and volume conditions. China's customs first blocked these parts; NVIDIA's outlook assumes no China data-centre revenue.
- **Section 232 (Jan 2026):** only a narrow 25% tariff on certain advanced chips, with US data-centre use exempt. A threatened broader phase 2 is not confirmed as imposed.
- **Truce deadlines:** the BIS Affiliates Rule suspension was extended on 5 Nov 2026 to 10 Jan 2027. China's suspension of its Oct 2025 rare-earth package was due to lapse on 10 Nov 2026; a reported extension to 10 Jan 2027 rests on a single secondary source. China's Apr 2025 heavy-rare-earth licensing remains in force.
- **10 Jan 2027 is the key upcoming decision date.**

### Cited Findings

**US export controls**
- BIS rule effective 15 Jan 2026:
  - Licensing to China and Macau moves from a presumption of denial to case-by-case for chips with TPP below 21,000 and DRAM bandwidth below 6,500 GB/s (H200, MI325X class).
  - Chips must undergo independent third-party testing in the US. Imports for testing pay the 25% Section 232 tariff, which is the mechanism for the "25% of revenue" arrangement.
  - Exports are capped at 50% of US sales per chip (per CRS/CNAS summaries).
  - [Covington Global Policy Watch, Feb 2026](https://www.globalpolicywatch.com/2026/02/a-month-in-semiconductor-policy-section-232-measures-bis-rule-and-taiwan-deal-signal-strategic-push/) [P via law firm][F]; [CNAS](https://www.cnas.org/publications/cnas-insights/cnas-insights-unpacking-the-h200-export-policy) [S][SR]; [CRS R48642](https://www.congress.gov/crs-product/R48642) [P][SR; 403 when opened]
- China's response: Chinese customs initially blocked H200 imports, then issued conditional approvals to some AI companies (as of Feb 2026) — [Covington](https://www.globalpolicywatch.com/2026/02/a-month-in-semiconductor-policy-section-232-measures-bis-rule-and-taiwan-deal-signal-strategic-push/) [F]
- NVIDIA (26 Aug 2026): H200 shipments to China were under 1% of Q2 data-centre revenue, under US licences; "no China data center compute revenue in our forward outlook" — [NVIDIA transcript](https://stockanalysis.com/stocks/nvda/transcripts/676136-q2-2027/) [P][F]
- HBM: the Dec 2024 country-wide controls on advanced HBM to China (3A090.c, bandwidth density above 2 GB/s/mm²) remain the operative rule. No new HBM action was found for Nov 2026. Analysts flag that HBM already integrated into chips is not restricted — [AI Frontiers](https://ai-frontiers.org/articles/high-bandwidth-memory-critical-gaps-us-export-controls) [S][SR]; [CSIS](https://www.csis.org/analysis/understanding-biden-administrations-updated-export-controls) [S][SR]
- AI Diffusion Rule: BIS announced its rescission in May 2025. Whether a formal replacement exists was described as open — relayed in search results [S][SR]
- Affiliates (50%) Rule:
  - BIS final rule released 5 Nov 2026, published in the Federal Register 9 Nov 2026.
  - It extends the suspension from 9 Nov 2026 through **10 Jan 2027**, with no other changes and no reason given.
  - Entity List and MEU List parties remain restricted.
  - [Baker McKenzie](https://sanctionsnews.bakermckenzie.com/bis-extends-suspension-of-the-affiliates-rule-through-january-10-2027/) [P via law firm][SR]; [Kelley Drye](https://www.kelleydrye.com/viewpoints/blogs/trade-and-manufacturing-monitor/bis-extends-suspension-of-the-affiliates-rule-through-january-10-2027) [SR]; [AAEI](https://aaei.org/bis-extends-suspension-of-the-affiliates-rule/) [SR]

**US tariffs (Section 232)**
- Proclamation 11002, signed 14 Jan 2026, effective 15 Jan 2026:
  - 25% on a narrow set of advanced logic chips (HTSUS 8471.50, 8471.80, 8473.30, within the TPP and bandwidth bands).
  - Exempt end uses include **US data centres**, US R&D, start-ups, consumer, industrial and public sector.
  - No tariff on semiconductor equipment.
  - Covered goods are excluded from IEEPA and other Section 232 tariffs.
  - Commerce and USTR were to report on negotiations about 14 Apr 2026, after which the President may consider "significant" tariffs on chips, equipment and derivatives plus an offset programme.
  - Commerce was to update the President on the US data-centre chip market by 1 Jul 2026.
  - Lutnick warned Korean and Taiwanese chipmakers not investing in the US could face up to 100%.
  - Negotiating partners: Taiwan, Korea, Japan, Netherlands, Germany, **Israel**.
  - [Covington](https://www.globalpolicywatch.com/2026/02/a-month-in-semiconductor-policy-section-232-measures-bis-rule-and-taiwan-deal-signal-strategic-push/) [F]; [Sullivan & Cromwell, 16 Jan 2026](https://www.sullcrom.com/SullivanCromwell/_Assets/PDFs/Memos/Trade-Developments-Semiconductors-Critical-Minerals-Taiwan-Deal.pdf) [P via law firm][SR]
- Bilateral deals:
  - US-Taiwan (15 Jan 2026): at least $250B of direct investment plus $250B of credit guarantees. Firms building US capacity may import 2.5x planned US capacity duty-free during construction, and 1.5x after completion. A lower preferential rate applies above quota.
  - Korea: Section 232 chip rate "no less favorable" than a future comparable deal (understood as Taiwan's).
  - Japan: rate "no greater than" any other country's.
  - EU: MFN plus Section 232 capped at 15%.
  - [Covington](https://www.globalpolicywatch.com/2026/02/a-month-in-semiconductor-policy-section-232-measures-bis-rule-and-taiwan-deal-signal-strategic-push/) [F]
- Polysilicon Section 232 proclamation, signed 6 Aug 2026, **effective 4 Dec 2026**: 15% on wafers, cells and other derivatives; minimum import price of $21/kg for raw polysilicon; total duty capped at 15% for Japan, Korea, Taiwan, EU, Switzerland and Liechtenstein; additive 15% for others including China. Onshoring projects must start construction by 20 Jan 2029 — [Troutman Pepper Locke, 7 Aug 2026](https://www.troutman.com/insights/polysilicon-under-pressure-new-section-232-tariffs-reshape-solar-and-semiconductor-supply-chains/) [P via law firm][F]

**China's countermeasures**
- MOFCOM/GAC Announcement No. 70 of 2025 suspended the Oct 2025 rare-earth and technology package (Announcements 55-58, 61, 62) from 7 Nov 2025 to 10 Nov 2026 — [Carra Globe (published 5 May 2026; checked 14 Oct 2026)](https://carraglobe.com/china-rare-earth-export-controls-2026/) [S][F]; [Global Trade Alert](https://globaltradealert.org/state-act/95168-china-temporary-suspension-of-additional-export-controls-for-rare-earth-related-technologies/) [S][SR]
- MOFCOM (28 Sep 2026) said the wider US-China arrangement is extended to **10 Jan 2027**, without naming rare earths. As of 14 Oct 2026 no numbered notice had amended Announcement 70 — [Carra Globe](https://carraglobe.com/china-rare-earth-export-controls-2026/) [F]
- About 4 Nov 2026, MINING.COM noted no formal extension had been announced — [MINING.COM on X](https://x.com/mining/status/2118084012942000158) [S][SR]
- One secondary item dated 12 Nov 2026 says MOFCOM and GAC confirmed on 9 Nov 2026 that the suspension runs 11 Nov 2026 to 10 Jan 2027 — [relayed in search results; underlying page not identified] [SR, **unverified**]
- Apr 2025 licensing of seven heavy rare earths (Sm, Gd, Tb, Dy, Lu, Sc, Y; Announcement No. 18 of 2025) remains in force and was never suspended — [Carra Globe](https://carraglobe.com/china-rare-earth-export-controls-2026/) [F]
- Domestic substitution: CXMT is pursuing 4F² DRAM with a DDR5 server product by end-2026, without EUV access — [TechTimes, 22 Oct 2026](https://www.techtimes.com/articles/329350/20261022/micron-maps-annual-hbm-advances-2030-rejects-chinese-density-workaround.htm) [F]

**Upcoming decision dates**

| Date | Item |
|---|---|
| Late Nov 2026 (date not confirmed here) | NVIDIA Q3 FY27 results: Rubin ramp, any Rubin Ultra or Kyber timing |
| 4 Dec 2026 | Polysilicon Section 232 tariffs take effect |
| End-2026 | ECHA final opinions on EU PFAS restriction (affects two-phase coolants) [SR] |
| Jan 2027 | New governors in Ohio, Texas and Georgia; possible data-centre moratoria [CNBC] |
| **10 Jan 2027** | End of BIS Affiliates Rule suspension (unless extended); end of the US-China arrangement per MOFCOM; end of China's rare-earth suspension, if the reported extension holds |
| Late Jan/early Feb 2027 | Meta and Alphabet Q4 calls with 2027 capex guidance |
| Early 2027 | Expected EU PFAS vote [SR] |
| No date found | Section 232 semiconductor "phase 2" (significant tariffs, equipment) |

### Inferences
- The policy calendar concentrates risk on 10 Jan 2027. A lapse of either truce instrument would hit rare-earth-dependent inputs (magnets in cooling pumps and fans, power electronics) and US exporters' China affiliates at the same time.
- The Section 232 data-centre exemption means current US tariffs barely touch US AI build-outs. The live tariff risk is the unimposed phase 2 (equipment, broad chips) and its 100% threat against non-investing Korean and Taiwanese makers.

### Gaps
- **Not researched (search budget exhausted):**
  - China's gallium, germanium and antimony ban on the US (Announcement 46 of Dec 2024) and its suspension date.
  - Indium phosphide or other new Chinese controls.
  - China's antitrust case against NVIDIA (Mellanox), and customs actions after Feb 2026.
  - Domestic-chip mandates for state-funded data centres.
  - Nexperia.
  - Dutch (ASML DUV, servicing), Japanese (METI), Korean and Taiwanese export controls in 2026.
  - Israel- and India-specific items, beyond Israel being a Section 232 negotiating partner.
  - Any pending US legislation (chip security or location verification, GAIN AI-type provisions).
- These need a follow-up pass with primary government sources.

---

## What could not be verified
- **Lead times of 52-78 weeks** for advanced packaging (Claim 3). No source found.
- **Feynman's process node** (A16 or otherwise), die stacking and HBM generation from a primary source. Also the date of the 9.5x-reticle, 12-HBM CoWoS-L package.
- **Base Rubin volume slip to 2027** (Jukan, 12 Nov 2026). Unconfirmed and contradicted by NVIDIA's 26 Aug 2026 statements; NVIDIA's Q3 FY27 report should resolve it.
- **Rubin Ultra die count and rack form factor** for 2027. NVIDIA has published no new spec.
- **Microsoft's ~$170B capex period** (FY2027 vs calendar 2026) and the Q1 FY27 figure ($45.2B per one summary). Check against the 10-Q.
- **China's rare-earth suspension extension past 10 Nov 2026.** One secondary source only.
- **Huawei Ascend and SuperPoD roadmap status in 2026, and other Chinese systems.** Not researched. Pre-2026 public plans (Huawei Connect, Sep 2025) are not restated here because they were not re-verified.
- **Google TPU, Broadcom, Amazon Trainium, Meta MTIA, Microsoft Maia and OpenAI custom-chip roadmaps.** Not researched beyond NVIDIA's statement that Vera Rubin racks are running at Google Cloud and Azure, and AMD's naming of Helios customers.
- **Neocloud, sovereign and Chinese hyperscaler capex.** Not obtained.
- **OpenAI 2026 financing and commitment totals.** Only low-quality single-source claims, which are excluded. NVIDIA's "about 12 GW" OpenAI figure is a company claim.
- **Rack-level kW of current liquid-cooled racks** (GB300 NVL72, Vera Rubin NVL144) from a primary source.
- **In-chip or microfluidic cooling production status.**
- **JEDEC ~900 µm height for HBM4E** (reported, unverified), and Samsung hybrid-bonded HBM4 sample yields (low-tier sources).
- **Export-control items listed in the Gaps above** (Netherlands, Japan, Korea, Taiwan, Israel, India; gallium and germanium; NVIDIA antitrust; domestic-chip mandates).
- **Regional coverage is thin** for mainland China, Japan and Korea in local languages. Taiwanese and Korean information came only through English-language relays (TrendForce, The Elec, Chosun Biz).
- **Process note:** the session's web-search budget ran out, and Exa and Firecrawl credits ran out midway. The Hardware Signal Foxconn note (#225) returned 404 on re-check, and Forbes (22 Oct 2026), HPCwire and CRS returned 403.

---

## Sources
Format: title — URL — publication or event date — type. [F] means read in full; [SR] means search-summary only.

**Primary or near-primary**
- NVIDIA Q2 FY2027 earnings call transcript — https://stockanalysis.com/stocks/nvda/transcripts/676136-q2-2027/ — 26 Aug 2026 — [P, third-party transcript][F]
- NVIDIA Q2 FY2027 press release — https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027 — 26 Aug 2026 — [P][SR]
- TSMC Q3 2026 earnings call transcript (AI-assisted) — https://www.investing.com/news/transcripts/earnings-call-transcript-tsmc-beats-q3-2026-estimates-as-stock-slips-93CH-4950695 — 15 Oct 2026 — [P, third-party transcript][F]
- TSMC Q3 2026 presentation (Form 6-K) — https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000726/a3q26presentatione.htm — Oct 2026 — [P][not opened]
- Micron FQ4 FY2026 prepared remarks — https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf — 30 Sep 2026 — [P][F, text extracted]
- AMD Q3 2026 earnings call transcript (Motley Fool) — https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/ — call 3 Nov 2026, published 4 Nov 2026 — [P, third-party transcript][F]
- OCP Mt. Diablo Disaggregated Power Rack Specification v1.0.0 — https://www.opencompute.org/wp-content/uploads/2026/10/OCP-Specification-Mt.-Diablo-Disaggregated-Power-Rack-Specification-v1.0.0.pdf — 8 Oct 2026 — [P][SR]
- SK hynix Tech Note on hybrid bonding — https://news.skhynix.com/en/tech-note-series-ep2/ — date not captured — [P][SR]
- NVIDIA developer blog on CPO — https://developer.nvidia.com/blog/scaling-ai-factories-with-co-packaged-optics-for-better-power-efficiency/ — date not captured — [P][SR]

**Government notices via law-firm summaries**
- Baker McKenzie, BIS extends Affiliates Rule suspension — https://sanctionsnews.bakermckenzie.com/bis-extends-suspension-of-the-affiliates-rule-through-january-10-2027/ — Nov 2026 — [SR]
- Kelley Drye, same topic — https://www.kelleydrye.com/viewpoints/blogs/trade-and-manufacturing-monitor/bis-extends-suspension-of-the-affiliates-rule-through-january-10-2027 — Nov 2026 — [SR]
- AAEI, same topic — https://aaei.org/bis-extends-suspension-of-the-affiliates-rule/ — Nov 2026 — [SR]
- Covington Global Policy Watch, "A Month in Semiconductor Policy" — https://www.globalpolicywatch.com/2026/02/a-month-in-semiconductor-policy-section-232-measures-bis-rule-and-taiwan-deal-signal-strategic-push/ — Feb 2026 — [F]
- Sullivan & Cromwell memo — https://www.sullcrom.com/SullivanCromwell/_Assets/PDFs/Memos/Trade-Developments-Semiconductors-Critical-Minerals-Taiwan-Deal.pdf — 16 Jan 2026 — [SR]
- Troutman Pepper Locke, polysilicon Section 232 — https://www.troutman.com/insights/polysilicon-under-pressure-new-section-232-tariffs-reshape-solar-and-semiconductor-supply-chains/ — 7 Aug 2026 — [F]
- CRS R48642, US export controls and China — https://www.congress.gov/crs-product/R48642 — 2026 — [SR; 403]

**Secondary: roadmaps, packaging, optics, memory**
- SemiEngineering, "TSMC Tech Symposium 2026, By The Numbers" — https://semiengineering.com/tsmc-tech-symposium-2026-by-the-numbers/ — 27 Apr 2026 — [F]
- TrendForce, TSMC roadmap / A16 delayed to 2027 — https://www.trendforce.com/news/2026/04/23/news-tsmc-unveils-latest-roadmap-a12-a13-set-for-2029-without-high-na-euv-a16-volume-production-delayed-to-2027/ — 23 Apr 2026 — [F]
- TrendForce, CoWoS supply-demand gap — https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-reportedly-seen-narrowing-from-20-to-10-by-end-2026-as-capacity-expands/ — 15 Jun 2026 — [F]
- TrendForce, CoPoS pilot line — https://www.trendforce.com/news/2026/04/13/news-tsmc-advances-panel-level-packaging-copos-pilot-line-reportedly-set-for-june-completion-2028-29-ramp-eyed/ — 13 Apr 2026 — [SR]
- TrendForce, CoWoS price hike — https://www.trendforce.com/news/2026/10/27/news-tsmc-reportedly-eyes-20-cowos-price-hike-skips-equipment-price-renegotiations-amid-ai-demand-surge/ — 27 Oct 2026 — [SR]
- TrendForce, glass substrates — https://www.trendforce.com/news/2026/08/18/news-glass-substrate-war-heats-up-shinko-electric-advances-22-layer-product-as-samsung-reportedly-faces-ramp-up-uncertainty/ — 18 Aug 2026 — [F]
- TrendForce press release, CPO volume ramp — https://www.trendforce.com/presscenter/news/20260727-13151.html — 27 Jul 2026 — [F]
- TrendForce, SK hynix 3Q26 — https://www.trendforce.com/news/2026/10/28/news-sk-hynix-3q26-opm-hits-record-80-says-dram-hbm-effectively-sold-out-to-2029-14-lta-customers-signed/ — 28 Oct 2026 — [F]
- TechTimes, Micron HBM roadmap to 2030 — https://www.techtimes.com/articles/329350/20261022/micron-maps-annual-hbm-advances-2030-rejects-chinese-density-workaround.htm — 22 Oct 2026 — [F]
- SDxCentral, NVIDIA 15x optics capacity — https://www.sdxcentral.com/news/nvidia-targets-15x-optics-capacity-expansion-by-2027-to-meet-cpo-demand/ — 21 Oct 2026 — [F]
- WinBuzzer, Kyber delay report — https://winbuzzer.com/2026/07/07/reported-nvidia-kyber-delay-pushes-ai-rack-toward-2028-xcxwbn/ — 7 Jul 2026 — [F]
- Wccftech, NVIDIA says roadmap intact — https://wccftech.com/nvidia-quashes-rubin-kyber-rack-delay-rumors-says-chip-roadmap-is-intact/ — 7 Jul 2026 — [F]
- igor'sLAB, Rubin Ultra four-die design — https://www.igorslab.de/en/nvidia-rubin-ultra-four-die-scrapped-reversal/ — 1 Jul 2026 — [F]
- Tom's Hardware, quad-die Rubin Ultra cancelled — https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-reportedly-cancels-quad-die-rubin-ultra-gpu-in-favor-of-dual-gpu-design-report-claims-complex-design-purportedly-scrapped-over-manufacturing-execution-concerns — 30 Jun 2026 — [SR]
- Tom's Hardware, Huang on Vera Rubin volumes — https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidias-huang-vows-to-deliver-giant-amounts-of-vera-rubin-company-says-that-our-roadmap-is-intact — Jul 2026 — [headline only]
- Yahoo Finance, Huang dismisses delay report — https://finance.yahoo.com/technology/ai/articles/nvidia-ceo-jensen-huang-dismisses-233017030.html — Jul 2026 — [SR]
- Newsquawk, Jukan on Rubin delay — https://newsquawk.com/headlines/citrinis-jukan-says-that-one-thing-ive-been-able-to-confirm-is-that-nvidias-nvda-rubin-has-been-delayed-again-im-told-motherboard-warpage-caused-the-latest-delay-and-that-the-hbm-issue-was-resolved-in-october — 12 Nov 2026 — [F]
- Wikipedia, Rubin (microarchitecture) — https://en.wikipedia.org/wiki/Rubin_(microarchitecture) — last edited 17 Oct 2026 — [F]
- HPCwire/AIwire, GTC 2026 roadmap — https://www.hpcwire.com/aiwire/2026/03/18/huang-shares-nvidia-roadmap-showing-more-chips-nvl1152-scale-up-cpo/ — 18 Mar 2026 — [SR; 403]
- SemiAnalysis, GTC 2026 — https://newsletter.semianalysis.com/p/nvidia-the-inference-kingdom-expands — Mar 2026 — [SR]
- SemiAnalysis, CPO — https://newsletter.semianalysis.com/p/co-packaged-optics-cpo-book-scaling — 2026 — [SR]
- Atlan, GTC 2026 recap — https://atlan.com/know/nvidia-gtc-2026-keynote-recap/ — Mar 2026 — [SR]
- Jon Peddie Research, GTC 2026 keynote — https://www.jonpeddie.com/news/nvidia-gtc-2026-keynote/ — Mar 2026 — [SR]
- DEV Community, GTC 2026 summary — https://dev.to/max_quimby/nvidia-gtc-2026-every-ai-announcement-developers-need-to-know-1njb — Mar 2026 — [SR]
- Longbridge, CPO mass production note — https://longbridge.com/en/topics/100000000858275 — 2026 — [SR]
- iTiger, TSMC photonic IC capacity — https://www.itiger.com/news/1131192118 — 2026 — [SR]
- BigGo Finance, C.C. Wei on CoPoS — https://finance.biggo.com/news/kLg0kp4BrX5PFN7BKrXD — Jun 2026 — [SR]
- TechPowerUp, CoPoS — https://www.techpowerup.com/337960/tsmc-prepares-copos-next-gen-310-x-310-mm-packages — 2025 — [SR]
- IRZ, glass substrates — https://irz.fr/en/articles/verre-remplace-pas-encore-organique-en/ — 2026 — [SR]
- VLSI.kr, HBM stack heights — https://www.vlsi.kr/en/hbm-stack-height-8hi-12hi-16hi-en/ — 2026 — [SR]
- Nomad Semi, HBM deep dive — https://www.nomadsemi.com/p/deep-dive-on-hbm — date not captured — [SR]
- Tom's Hardware, hybrid bonding in 2026 — https://www.tomshardware.com/tech-industry/semiconductors/hybrid-bonding-roadmap-examined — 2026 — [title only]
- Tom's Hardware, future AI processors up to 15,360 W — https://www.tomshardware.com/pc-components/cooling/future-ai-processors-said-to-consume-up-to-15-360w-massive-power-draw-will-demand-exotic-immersion-and-embedded-cooling-tech — 2025/26 — [SR]
- AI Data Center Guide, NVIDIA accelerators — https://aidatacenterguide.com/part-7-compute-silicon-and-system-integration/7-2-nvidia-accelerators-hopper-blackwell-vera-rubin-rubin-ultra-feynman — 2026 — [SR, low-tier]
- Thunder Compute, Rubin architecture — https://www.thundercompute.com/blog/nvidia-rubin-architecture — Nov 2026 — [SR, low-tier]
- Converge Digest, OCP 800 VDC — https://convergedigest.com/ocp-800-vdc-standard-megawatt-ai-racks/ — Oct 2026 — [SR]
- TechArena, OCP Global Summit 2026 — https://techarena.ai/content/ocp-global-summit-2026-agents-800-volts-and-a-warning-on-heat — Oct 2026 — [SR]
- The Cooling Report, PFAS and two-phase — https://thecoolingreport.com/intel/pfas-two-phase-immersion-cooling-crisis.html — 2026 — [SR]
- The Cooling Report, cooling guide — https://thecoolingreport.com/intel/data-center-cooling-systems-complete-guide-2026.html — 2026 — [SR]
- DCD, ZutaCore PFAS-free two-phase — https://www.datacenterdynamics.com/en/news/zutacores-two-phase-cooling-will-eliminate-pfas-in-2026/ — date not captured — [SR]
- Jason Agee Substack, non-PFAS two-phase — https://jasonagee.substack.com/p/two-phase-non-pfas-liquid-cooling — 2026 — [SR]
- Jukan on X, JPM CoWoS note — https://x.com/jukan05/status/1989479922910597530 — Nov 2025 — [SR]

**Secondary: spending, financing, power, compute**
- Yield Theory, hyperscaler capex 2027 — https://www.yieldtheory.app/research/hyperscaler-capex-2027-forecast — Nov 2026 — [F]
- investingLive, Microsoft $170bn capex — https://investinglive.com/stocks/microsoft-sees-170bn-capex-in-fiscal-2027-but-says-it-will-stay-cash-flow-positive/ — 28 Oct 2026 — [F]
- FourWeekMBA, Microsoft lowers capex view — https://fourweekmba.com/ai-microsoft-lowers-2026-capex-view-to-170b-eyes-new-funding/ — Oct 2026 — [SR]
- CNBC, CoreWeave bond yield above 16% — https://www.cnbc.com/2026/11/06/coreweave-bond-yield-tops-16percent-as-ai-credit-stress-rises.html — 6 Nov 2026 — [F]
- Forbes, AI debt toward $570B — https://www.forbes.com/sites/robertszczerba/2026/07/17/bond-investors-push-back-as-ai-debt-heads-toward-570-billion/ — 17 Jul 2026 — [SR]
- Forbes, AI debt boom — https://www.forbes.com/sites/mayrarodriguezvalladares/2026/10/22/the-half-trillion-dollar-silicon-gamble-inside-the-ai-debt-boom/ — 22 Oct 2026 — [SR; 403]
- JPMorgan Asset Management, hyperscaler debt — https://am.jpmorgan.com/gb/en/asset-management/institutional/insights/market-insights/market-updates/on-the-minds-of-investors/hyperscaler-debt-issuance-ai-buildout/ — 2026 — [SR]
- Power Engineering, data-centre construction delays — https://www.power-eng.com/renewables/america-data-center-construction-delays/ — 5 Oct 2026 — [F]
- Tom's Hardware, Stargate partner disputes — https://www.tomshardware.com/tech-industry/artificial-intelligence/stargate-ai-data-centers-for-openai-reportedly-delayed-by-squabbles-between-partners-sources-say-openai-oracle-and-softbank-disagreed-on-who-would-have-ultimate-control-of-the-planned-data-centers — date not pinned — [SR]
- Epoch AI, AI chip production — https://epoch.ai/data-insights/ai-chip-production — 2026 — [SR]
- Epoch AI, computing capacity additions — https://epoch.ai/data-insights/ai-computing-capacity-additions-doubling — 2026 (data to Q2 2026) — [SR]
- Epoch AI, compute trends — https://epoch.ai/trends/compute — updated 5 Feb 2026 per snippet — [SR]
- Crypto Briefing, Epoch chip stock — https://cryptobriefing.com/epoch-ai-chips-billion-ai-agents/ — 2026 — [SR]
- FourWeekMBA, Google TPU compute growth — https://fourweekmba.com/ai-googles-tpu-compute-grew-74-in-a-quarter-4x-nvidias/ — Oct/Nov 2026 — [SR]

**Secondary: policy**
- Carra Globe, China rare-earth controls 2026 — https://carraglobe.com/china-rare-earth-export-controls-2026/ — published 5 May 2026, checked 14 Oct 2026 — [F]
- Global Trade Alert, China suspension of rare-earth controls — https://globaltradealert.org/state-act/95168-china-temporary-suspension-of-additional-export-controls-for-rare-earth-related-technologies/ — 2025/26 — [SR]
- MINING.COM on X — https://x.com/mining/status/2118084012942000158 — about 4 Nov 2026 — [SR]
- CNAS, H200 export policy — https://www.cnas.org/publications/cnas-insights/cnas-insights-unpacking-the-h200-export-policy — 2026 — [SR]
- AI Frontiers, HBM export-control gaps — https://ai-frontiers.org/articles/high-bandwidth-memory-critical-gaps-us-export-controls — 2025/26 — [SR]
- CSIS, updated export controls — https://www.csis.org/analysis/understanding-biden-administrations-updated-export-controls — Dec 2024 — [SR]
