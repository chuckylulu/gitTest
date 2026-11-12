# Onto Innovation, Nova, Camtek and the advanced-packaging inspection/metrology landscape

Research date: **12 November 2026**. Latest quarter for all three = Jul-Sep 2026 (Q3 2026), reported 4 Nov (Camtek), 5 Nov (Nova), 9 Nov (Onto) 2026. Prices = close 11 Nov 2026 (stockanalysis.com, checked 12 Nov 2026). Non-GAAP unless marked GAAP. **CC-U** = company claim, unconfirmed by any outside party I found. **Derived** = my arithmetic from cited figures. Status: v2 (final). Remaining gaps are in section 6.

Changes versus the brief's background:
- Onto's Semilab deal closed 17 Nov 2025 at ~$495M for **three** product lines, not the four announced (one line excluded after a US DOJ second request).
- New since the brief: Onto bought **27% of Rigaku** (Japan, X-ray) for $719.5M on 10 Aug 2026, funded by $1.5B of 0% converts due 2031. Camtek bought **Visual Layer** (visual AI, Apr 2026). Nova announced a $200M buyback (Sep 2026).
- Camtek's "controlling shareholder" is a pair: Priortech 20.66% + Chroma ATE 16.79% under a voting agreement (38.04%, Mar 2026).
- The 2024-25 Onto-to-Camtek share shift is **not confirmed** by any outside source found. The only outside commentary found blames KLA, not Camtek, and is unsourced (section 2.1).
- The US BIS "Affiliates Rule" suspension, due to end 9 Nov 2026, was **extended to 10 Jan 2027** (announced 5 Nov 2026).

---

## 0. Evidence tables

### 0.1 Onto Innovation (NYSE: ONTO) - quality tests and transitions

| Test | Evidence (sources in sections 1-3) |
|---|---|
| (a) Position | Owns several wafer-release measurements: OCD (Atlas G6, "several nodes below 2 nm" and DRAM, CC-U), 2D package inspection (Dragonfly G5) and 3D bump metrology (3Di) in 2.5D and HBM; film/charge/contamination metrology (Semilab lines FAaST, CnCV, MBIR). Also sells a process tool (JetStep panel lithography). No disclosed access to customers' cross-section reference data. Rigaku stake adds X-ray physics for buried features. |
| (b) Lead | **Outside:** SK hynix Best Partner Award (technology), 28 Sep 2026, for Dragonfly's hidden-defect detection in HBM production (reported in an Onto release); Samsung reportedly validating Onto laser-ultrasound inspection of hybrid-bond interfaces on production lines (TheElec, Mar-Apr 2026; Samsung has not confirmed). No third-party share data. **CC-U:** an HBM maker chose G5 and 3Di, "displacing the previously established tool of record" (16 Mar 2026); G5 qualified for 2.5D (16 Apr 2026); >10 G5 customers (Nov 2026); one OSAT >$200M Dragonfly orders (Aug 2026). |
| (c) Revenue model | FY2025: systems+software 84%, parts 8%, services 8% ($73.2M). Q3 2026 software+services ~ $60M (~15% of revenue). Software (Discover yield, AI Diffract OCD modelling) not reported separately. 739 of ~1,615 staff in sales, applications and service. |
| (d) Financials | Q3 2026: GM 57.6% (GAAP 54.8%), op margin 32.6% (GAAP 23.3%). FY2025: GAAP GM 49.7%, GAAP op margin 13.2%, FCF ~ $300M (derived). Cash $1.25B vs converts $1.47B (net debt ~ $222M) plus Rigaku stake carried at $678.7M. ROIC 12.7% TTM. Top three customers 49% (20/15/14%, FY2025, unnamed). China 7% (FY2025) vs 17% (FY2023). |
| (e) Resilience | Backlog >$1.3B covering 2027 and some 2028. AP is ~half of revenue, split ~evenly 2.5D logic/HBM, so high beta to AI capex. Low China share. Tariff response: >60% of output from Asian contract factories by end-2026 (target). Rigaku stake marked to market each quarter (-$40.8M in Q3 2026). |
| T1 imaging -> inference | Did: OCD modelling; Rigaku X-ray stake ($719.5M); picosecond-ultrasonic sub-surface inspection. No published measurement uncertainty. |
| T2 AI recipes | Said: G5 machine-learning die-to-die detection "reduces recipe setup time" (CC-U, Mar 2026). No figures on applications-engineering revenue. |
| T3 bonded stacks | Did: G5 for CMP and hybrid bonding, sub-surface defects; 3Di sub-surface applications (Aug 2026); laser ultrasound at Samsung (reported). No electrical-test product. |
| T4 / T5 / T6 | Software not reported separately; PDF Solutions named as software rival. Nothing found on on-premises AI or on tool intensity after 2030. |

### 0.2 Nova Ltd. (Nasdaq/TASE: NVMI) - quality tests and transitions

| Test | Evidence |
|---|---|
| (a) Position | Owns wafer-release measurements in OCD (integrated in process tools, and stand-alone), films, materials (XPS VeraFlex, SIMS Metrion, Raman Elipson) and plating-bath chemistry (Ancolyzer, AncoScene: a physical-constraint measurement). Inference by design: optical/X-ray signal + MARS physical models + Nova FIT machine learning. Filings do not say how training reference data are obtained. |
| (b) Lead | **Partly outside:** product revenue CAGR 27.5% (2020-25) vs Gartner process-control CAGR 16.0% (Gartner, Dec 2025, cited in the 20-F). SemiAnalysis (undated) calls Nova high-share in integrated OCD and materials metrology. No third-party share figure found. **CC-U:** WMC tool of record at a leading foundry for multi-layer AP measurement (2 Jul 2026); AncoScene released to volume production at a leading foundry (Q3 2026); Metrion at 4 of 5 target customers; GAA revenue on track for $500M cumulative 2024-26; Nova's share "higher in GAA". |
| (c) Revenue model | FY2025: products 80% ($705.6M), services 20% ($175.0M, +31%). Service GM 47% vs product 60%. Services include "time and material" work (labour-linked) and value-added services (+~50% YoY in Q3 2026). Q3 2026 services $56.0M (19%). Software not reported separately. |
| (d) Financials | FY2025: revenue $880.6M (+31%), GM 57%, GAAP op income $253.5M (28.8%), net income $259.2M, FCF ~ $218M (derived). Q3 2026: GM 59.1% (GAAP 57.7%), op margin 35.5% (GAAP 32%), FCF $132M. Cash+investments ~$1.79B vs converts $734.6M. ROIC 20.4% TTM. FY2025 customers A 23%, B 10%, top five 51%. Q3 2026: four customers each >=10% of product revenue. China 33% (2025), 39% (2024). |
| (e) Resilience | Q3 2026 product mix ~61% logic/foundry, 39% memory; AP ~ one quarter of product revenue (Q2 2026). Front-end GAA/DRAM work diversifies away from AI packaging alone. Some Chinese customers need US licences for the US subsidiary's shipments. New XPS competitor expected 2H 2027 (CC). |
| T1 | Core business is inference (OCD, XPS models). No published uncertainty budget found. |
| T2 | Said (2022): physical + ML modelling to "reduce time to solution"; Nova FIT "data-driven ML" adoption growing. No figures on reduced applications work. |
| T3 | Did: Sentronics ($60.2M, 30 Jan 2025) -> WMC for 2.5D/3D AP; >10 WMC customers (Nov 2026); plating chemistry for TSV/packaging; HBM-driven AP records. No hybrid-bonding tool-of-record claim found. |
| T4 | Software suite (MARS, FIT, HPC, Fleet Management) sold "coupled" with hardware; no separate revenue. |
| T5 | Said (2022): "cloud-based Fleet Management connectivity with big-data analytics" across Nova tools in a fab. Whether this runs on customer premises: not stated. |
| T6 | Nothing found. |

### 0.3 Camtek Ltd. (Nasdaq/TASE: CAMT) - quality tests and transitions

| Test | Evidence |
|---|---|
| (a) Position | Optical 2D inspection and 3D bump metrology of packaging wafers (HBM, CoWoS-like at OSATs, chiplets) plus FRT surface metrology. Mostly imaging, not inference. No access to reference data disclosed. Hawk: 150 nm defects, 500M micro-bumps at <12 um pitch (CC-U). |
| (b) Lead | **CC-U:** "tool of record for all the 3D metrology for HBM4 at all the HBM manufacturers" and for several 2D steps; "we have not lost any market share" (Nov 2025). This conflicts with Onto's Mar 2026 claim of displacing an established 3D-metrology tool of record at an HBM maker. **Outside:** Intel 2025 EPIC Supplier Award (Apr 2025); an independent analyst cut his target in May 2025 on a Samsung HBM capex pause. Orders: $25M Hawk from a tier-1 IDM (Feb 2026; $45M with repeats), $31M from an OSAT for CoWoS-like flows (Mar 2026), $55M tier-1 OSAT + >$50M Hawk from a leading HBM maker (Jun 2026). No third-party share data. |
| (c) Revenue model | Overwhelmingly systems. Services ~ $40M in 2026 (~7%, CC), target ~ $100M in ~3 years. AI software sales from 2027 (double-digit $M), ~ $40M of software in the long-term model. 216 sales-support + 99 sales staff of 709. |
| (d) Financials | FY2025: revenue $496.1M (+16%), GM 51.6% (GAAP 50.5%), op margin 30.0% (GAAP 25.8%), FCF ~ $120M (derived). Q3 2026: GM 51.1%, op margin 29.5%, CFO $71.1M. Cash $877.1M vs converts $489.2M (net cash $387.9M). ROIC 18.8% TTM. One customer at 11% (2025). China 49.2% (2025), 30.9% (2024), 47.4% (2023); Korea fell to 7.4% (2025) from 27.3% (2024). |
| (e) Resilience | ~80% of Q3 2026 revenue from AP, mostly AI; OSATs more than half of 2026 orders; China ~half of revenue (entity-list risk named in filings). One main plant (Migdal HaEmek, Israel) plus a German FRT site; Middle East/Strait of Hormuz risk cited. Gross margin squeezed by component costs and a stronger shekel. |
| T1 | Direct optical 3D measurement; no inference-with-uncertainty product disclosed. |
| T2 | AI inspection and automatic defect classification offered from 2026 (20-F). Visual Layer bought 13-14 Apr 2026, terms undisclosed; goodwill +$38.4M in 2026 (derived). |
| T3 | Hawk marketed for hybrid bonding; activity "low", meaningful from 2028 (Nov 2026). |
| T4 | Software as an "additional and recurring revenue stream" (CC, Apr 2026); first sales expected Q1 2027. |
| T5 / T6 | Nothing found. |

### 0.4 Entry-point snapshot (separate from quality; detail in section 5)

| Item (close 11 Nov 2026) | ONTO | NVMI | CAMT |
|---|---|---|---|
| Price / market cap / EV | $215.06 / $10.56B / $10.78B | $340.62 / $10.83B / $9.84B | $107.05 / $5.00B / $4.61B |
| P/E trailing GAAP / forward (next 12 months) / on FY2027 consensus (derived) | 70.6 / 17.9 / 16.7 | 39.0 / 25.7 / 24.9 | 40.4 / 21.6 / 20.9 |
| Own FY2021-25 average forward P/E (derived) | 26.0 | 28.5 | 26.2 |
| EV/Sales; EV/EBITDA (trailing) | 8.2; 27.3 | 9.8; 30.2 | 8.5; 31.8 |
| FY2021-25 range: EV/Sales; EV/EBITDA | 2.8-8.5; 9.4-35.6 | 3.7-10.6; 12.7-33.6 | 2.4-9.3; 9.1-40.0 |
| Consensus revenue FY2026 / FY2027 | $1.49B (+48%) / $2.02B (+36%) | $1.08B (+22%) / $1.36B (+26%) | $596M (+20%) / $804M (+35%) |
| Latest guidance | Q4 $430-450M; 2026 growth >45% | Q4 $305-315M; 2026 > $1B | Q4 ~ $180M; 2027 > $800M; $1.2B in ~3 years |
| Moves | 52-week +52%; market cap ~ $15.1B on 11 Aug 2026 | 52-week +7%; high $615.99 (15 Jun 2026) | 52-week -4%; high $210.20 (24 Apr 2026) |
| Convert conversion price | $381.80 (capped call to $509.06): out of the money | $320.16 (cap $415.03): in the money | ~$109.34: at the money |
| Next dated events | Q4 results ~Feb 2027 (date not found) | Investor Day 9 Mar 2027 | Software launch Q1 2027; Q4 results ~Feb 2027 |

---

## 1. Key question: 2025 and Q3 2026 results, mix, margins, cash, customers, China, guidance

### Takeaway
All three posted records in Q3 2026, driven by AI packaging and AI-linked memory/logic. Onto grew fastest (+88% YoY) but has net debt after the Rigaku purchase. Nova has the highest margins, net cash and the most front-end diversification. Camtek is the most packaging- and China-concentrated and has the lowest gross margin.

### Cited findings - Onto
- Q3 2026 (to 30 Sep, released 9 Nov 2026): revenue $409.7M (+87.8% YoY; +19% QoQ); GAAP GM 54.8%, non-GAAP 57.6%; GAAP op income $95.4M (23.3%), non-GAAP $133.5M (32.6%); GAAP EPS $0.95, non-GAAP $2.44; 9M revenue $1.045B (+41.5%); cash and securities $1,251.5M; "2031 Notes, net" $1,473.2M; inventories $424.2M; operating cash flow ~ $79M; backlog >$1.3B; records in Advanced Nodes (Atlas G6) and AP/specialty (Dragonfly G5, Firefly); Q4 guidance revenue $430-450M, GM 57.7-58.3%, non-GAAP op margin 33.5-34.5%, non-GAAP EPS $2.59-2.79; 2026 growth >45% - [Onto 8-K Ex.99.1](https://www.sec.gov/Archives/edgar/data/0000704532/000119312526453582/onto-ex99_1.htm)
- Q3 2026 call: Advanced Nodes ~ $135M (~60% memory); software+services ~ $60M; AP/specialty +35% QoQ, "a little over half" of revenue (~ $215M derived); 2026: AP >80% growth (even 2.5D logic/HBM split), Advanced Nodes >35%, panel revenue doubling, 3Di Q4 revenue > Q1-Q3 combined; 2027: AP >35%, Advanced Nodes faster than 2026, panel >40%; FCF "about $80M"; Rigaku price $720M - [MarketBeat call summary](https://www.marketbeat.com/instant-alerts/transcript-onto-innovation-q3-earnings-call-highlights-2026-11-09/)
- 10-Q: Rigaku cash cost $719.5M, carrying value $678.7M (Level 2); 2031-note net proceeds $1,471.0M; capped call $89.0M; 9M buybacks $205.0M; 9M operating cash flow $166.6M, capex $8.8M; goodwill $625.8M - [Onto 10-Q, 9 Nov 2026](https://www.sec.gov/Archives/edgar/data/704532/000119312526453859/onto-20260930.htm)
- FY2025 (to 3 Jan 2026): revenue $1,005.3M (FY2024 $987.3M); GAAP GM 49.7% (52.2%); GAAP op margin 13.2% (19.0%); R&D $132.0M; net income $136.8M; operating cash flow $328.3M; capex $28.5M; buybacks $75.0M; systems revenue fell mainly on "fewer inspection units shipped for advanced packaging for AI chips"; Taiwan 32%, S. Korea 28%, US 12%, Japan 10%, China 7%, SE Asia 6%, Europe 5%; customers A 20% (23% in FY2024), B 15% (17%), C 14% (12%); risk factors cite TSMC and Samsung as large revenue sources - [Onto 10-K FY2025](https://www.sec.gov/Archives/edgar/data/704532/000119312526066937/onto-20260103.htm)
- Q3 2025 baseline: Advanced Nodes $54M, specialty+AP $113M, software+services $51M - [Onto Q3 2025 call, 7 Nov 2025](https://www.fool.com/earnings/call-transcripts/2025/11/07/onto-innovation-onto-q3-2025-earnings-transcript/)
- Third-party summaries (flagged): four customers ~57% of 1H/9M 2026 revenue - [Finsee](https://finsee.ai/earnings/onto/2026/q3/en/); [Panabee (AI-generated)](https://www.panabee.com/news/onto-innovation-earnings-q3-2026).

### Cited findings - Nova
- Q3 2026 (released 5 Nov 2026): revenue $287.8M (products $231.9M, services $56.0M; +28% YoY); GAAP GM 57.7%; GAAP op income $92.8M, non-GAAP $102.2M; GAAP EPS $2.64, non-GAAP $2.86; cash $188.2M + deposits $395.9M + securities $1,205.1M; converts, net $734.6M; equity $1,511.7M; Q3 operating cash flow $138.1M, capex $6.4M; Q4 guidance $305-315M, non-GAAP EPS $3.03-3.18; records in AP (HBM and advanced-logic capacity) and memory - [Nova 6-K](https://www.sec.gov/Archives/edgar/data/0001109345/000117891326005034/zk2636340.htm)
- Call: ~61% logic/foundry, 39% memory (product revenue); four customers and four territories each >=10%; FCF $132M (9M ~ $206M); buyback $38.5M; trailing revenue passed $1B, 2026 > $1B "a year ahead" of plan - [MarketBeat, 6 Nov 2026](https://www.marketbeat.com/instant-alerts/transcript-nova-q3-earnings-call-highlights-2026-11-06/); China share in 2026 "lower than 2025, but still nominally grow" - [TradingKey transcript](https://www.tradingkey.com/news/transcripts/262284988-)
- FY2025: revenue $880.6M (2024 $672.4M); GM 57%; GAAP op income $253.5M; net income $259.2M; operating cash flow $245.6M; capex $27.7M; China 33%, Taiwan 29%, Korea 16%, USA 9%, other 13%; Customer A 23% (18%), B 10% (14%); top five 51% - [Nova 20-F FY2025](https://www.sec.gov/Archives/edgar/data/0001109345/000117891326000504/zk2634307.htm)
- Q2 2026: revenue $255M; AP "nearly one-quarter of product revenue" - [CMC Markets, 1 Oct 2026](https://www.cmcmarkets.com/en-au/opto/camt-vs-nvmi-vs-onto-the-chip-packaging-arms-race)

### Cited findings - Camtek
- Q3 2026 (released 4 Nov 2026): revenue $161.3M (+28% YoY, +21% QoQ); GAAP GM 50.0%, non-GAAP 51.1%; GAAP op income $39.8M, non-GAAP $47.5M (29.5%); GAAP EPS $0.84, non-GAAP $0.99; operating cash flow $71.1M; cash $877.1M; converts $489.2M (Dec 2025: $519.8M); goodwill $112.7M (Dec 2025: $74.3M); Q4 ~ $180M, FY2026 ~ $595M, 2027 > $800M - [Camtek 6-K](https://www.sec.gov/Archives/edgar/data/0001109138/000117891326005000/zk2636329.htm)
- Call: AP ~80% of sales, mostly AI; Eagle G5 + Hawk ~57% of systems revenue; >$800M orders YTD (~80% AP; OSATs > half); customers "including China" booking slots through 2027; $1.2B target ~3 years out at 34-36% op margin - [MarketBeat, 4 Nov 2026](https://www.marketbeat.com/instant-alerts/transcript-camtek-q3-earnings-call-highlights-2026-11-04/)
- FY2025: revenue $496.1M; GM 51.6%; op income $149.0M (30.0%); GAAP net income $50.7M after a convert-repurchase loss; operating cash flow $142.6M - [Camtek release, 18 Feb 2026](https://www.camtek.com/news-and-events/camtek-announces-record-results-for-the-fourth-quarter-full-year-2025/). China $243.9M (49.2%), Korea $36.9M (7.4%; 2024: $117.1M), US 5.8%; one customer 11%; ~50% of revenue from AI-related products; capex $22.5M - [Camtek 20-F FY2025](https://www.sec.gov/Archives/edgar/data/0001109138/000117891326001561/zk2634678.htm)
- Q2 2026: AP ~75% of revenue; Asia 92% - [Allmind, 10 Aug 2026](https://allmind.ai/earnings/event/2953780). H1 2026 orders included ~ $260M from HBM makers, mixing firm orders and non-binding forecasts (third-party) - [Finsee](https://finsee.ai/earnings/camt/2026/q3/en/)

### Inferences
- Nova earns 6-8 points more gross margin than Camtek and has a service line ~3x Camtek's share of revenue. Onto's GAAP margins are depressed by amortisation and the Rigaku mark-to-market.
- Concentration is rising at Nova: two >=10% customers in FY2025, four (of product revenue) in Q3 2026. Camtek has the most spread customer list but the highest country exposure.

### Gaps
- 2026 China shares and named >=10% customers for all three (Onto 10-Q tables could not be read; the online text was partial).

---

## 2. Key question: tool-of-record positions and the competitive landscape

### 2.1 Onto vs Camtek in 2.5D/CoWoS and HBM

**Takeaway.** Filings support an Onto setback in AI-packaging inspection in 2025 and a 2026 rebound on Dragonfly G5 and 3Di. The SK hynix award is the only outside confirmation of an Onto position in HBM. No outside share data exist in what I found, and the only outside commentary on the 2025 setback blames KLA, without evidence.

Cited findings:
- Onto FY2025 systems revenue fell on "fewer inspection units shipped for advanced packaging for AI chips" - [Onto 10-K](https://www.sec.gov/Archives/edgar/data/704532/000119312526066937/onto-20260103.htm)
- Pseudonymous analyst (11 May 2025) speculated Onto failed TSMC CoWoS-L qualification and that KLA displaced it; no data cited, author holds KLA - [Irrational Analysis](https://irrationalanalysis.substack.com/p/onto-innovation-implosion)
- Q3 2025: 3Di qualified at "two high bandwidth memory customers"; a leading OSAT ordered 3Di for 2.5D AI packaging - [Onto Q3 2025 call](https://www.fool.com/earnings/call-transcripts/2025/11/07/onto-innovation-onto-q3-2025-earnings-transcript/)
- 16 Mar 2026: a leading HBM maker picked G5 for most 2D inspection (double-digit systems) and a similar number of 3Di, "displacing the previously established tool of record" (CC-U) - [Onto release](https://investors.ontoinnovation.com/news/news-details/2026/Onto-Innovation-Launches-Dragonfly-G5-Inspection-System/)
- 16 Apr 2026: G5 qualified for "new and existing applications in 2.5D advanced packaging"; Dragonfly to grow >50% in 2026 (CC-U) - [Onto release](https://s24.q4cdn.com/480160064/files/doc_news/Onto-Innovations-Dragonfly-G5-System-Qualified-for-Applications-in-2-5D-AI-Packaging-2026.pdf)
- 6 Aug 2026: inspection +30% QoQ from 2.5D and HBM, "a mix of both" market growth and share gain; one OSAT >$200M Dragonfly orders; Onto offers inspection/metrology for TSMC CoWoS panels (310 x 310 mm) (CC-U) - [Allmind Q2 2026 call](https://allmind.ai/earnings/event/2943270)
- 28 Sep 2026: SK hynix Best Partner Award for technology achievement (25th Partners Day) for Dragonfly's detection of hidden HBM defects; the award goes to several suppliers each year - [BriefGlance summary of Onto release](https://briefglance.com/companies/onto-innovation-inc/pulses/88449); [Webull syndication](https://www.webull.com/news/15737073705559040); FormFactor won one in 2024 - [FormFactor](https://formfactor.com/?p=87908)
- Camtek, Nov 2025: tool of record for "all the 3D metrology for HBM4 at all the HBM manufacturers"; "we have not lost any market share"; CoWoS-like production shifting to OSATs (CC-U) - [Allmind Camtek Q3 2025 call](https://allmind.ai/earnings/event/bt_CAMT_2025_Q3)
- Independent analyst (8 May 2025): cut Camtek target $107 -> $57 on a Samsung HBM capex pause; Camtek tools used at RDL, microbump and interposer steps - [Castellano Substack](https://drrobertcastellano.substack.com/p/camtek-faces-hbm-cycle-reset-but)
- Camtek orders: ~$25M Hawk from a tier-1 IDM (10 Feb 2026) - [Camtek](https://www.camtek.com/news-and-events/camtek-receives-multiple-hawk-systems-order-of-approximately-25-million-from-an-idm-for-ai-applications/); $31M OSAT order for CoWoS-like flows (30 Mar 2026) - [iConnect007](https://iconnect007.com/article/149438/camtek-receives-31-million-multisystem-order-from-a-leading-osat/149435/aep); $55M tier-1 OSAT + >$50M Hawk from a leading HBM maker, delivery 2027 (2 Jun 2026) - [Camtek 6-K](https://www.sec.gov/Archives/edgar/data/0001109138/000117891326003033/zk2635474.htm)

Inferences:
- The two companies' claims conflict for HBM 3D bump metrology from 2026; which maker and which incumbent is unverified. The Samsung reports and the Mar 2026 G5 order coincide in timing (a trade-press observation, not proof).
- Camtek's Korea revenue fell 69% in 2025 while China rose 84%, consistent with the Samsung HBM pause the analyst described. Camtek's 2025 growth did not come from Korean HBM makers, which does not fit a simple "Camtek took HBM share from Onto in 2025" story.
- Onto's "leading 2.5D logic customer" is unnamed; Taiwan = 32% of revenue and Customer A = 20% point to TSMC, unconfirmed.

### 2.2 Nova in packaging
- WMC chosen as tool of record after a competitive evaluation at a leading global foundry for multi-layer measurement in the most advanced packaging; deployments at several memory and foundry customers (CC-U) - [Nova release, 2 Jul 2026](https://www.novami.com/investors/press-releases/nova-wmc-expanding-adoption-across-the-most-advanced-packaging-processes/); >10 WMC customers (Nov 2026) - [MarketBeat](https://www.marketbeat.com/instant-alerts/transcript-nova-q3-earnings-call-highlights-2026-11-06/)
- Nova says Sentronics puts it "in direct competition with companies such as Merck and Camtek" - [Nova 20-F](https://www.sec.gov/Archives/edgar/data/0001109345/000117891326000504/zk2634307.htm)

### 2.3 Market size and other participants
- Yole: back-end equipment $9.5B in 2026, 6.3% CAGR to 2031; inspection/metrology and hybrid bonding named as key areas (no shares) - [Silicon Semiconductor, 13 Jul 2026](https://siliconsemiconductor.net/article/124687/AI_reshapes_back-end_equipment). Yole Metrology & Inspection 2026: "record year after almost 16% growth in 2025" (search snippet; page blocked) - [Yole](https://www.yolegroup.com/product/report/metrology--inspection-equipment-2026/)
- Paid aggregators (low quality): AP inspection+metrology $925M in 2025, 8.7% CAGR (QYResearch) - [GII](https://www.gii.tw/report/qyr2000365-advanced-packaging-inspection-metrology-equipment.html); HBM inspection equipment ~ $1.0B in 2026 - [Meticulous Research](https://meticulousresearch.com/reports/hbm-inspection-equipment-market-6830)
- Bloomberg Intelligence: 2.5D/3D packaging 37% CAGR 2025-30 - [CMC Markets](https://www.cmcmarkets.com/en-au/opto/camt-vs-nvmi-vs-onto-the-chip-packaging-arms-race)
- **KLA:** 58% of process control in 2025 per Gartner (KLA management) - [Finsee KLA review](https://finsee.ai/earnings/klac/2026/q3/en/). Its AP revenue is reported as ~ $635M (2025) rising to a ~ $1B 2026 target, with a 14-point share gain in wafer-level packaging (call summary, ~Apr 2026, page not opened) - [Pulse.bot KLA transcript](https://www.pulse.bot/earnings-calls/news/kla-corp-klac-q3-2026-earnings-call-transcript-4cc07942-ec73-4c3d-8e71-0296a55af40a/); a Substack gives ~ $830M -> $1.3-1.4B for fiscal 2026 - [HandsOff](https://handsoff.substack.com/p/kla-beat-across-the-board-process). Conflicting; not verified against KLA filings.
- **Samsung hybrid-bond inspection:** Samsung is validating Onto's laser-ultrasound (picosecond ultrasonic) tool on production lines under joint development, and is also talking to other ultrasonic and X-ray vendors, including unnamed Korean groups; Samsung has not confirmed - [Cloud News, from TheElec, ~Apr 2026](https://cloudnews.tech/samsung-accelerates-inspection-of-hybrid-bonding-for-future-hbm/); [OneStopNDT, 1 Apr 2026](https://www.onestopndt.com/ndt-news/samsung-hybrid-bonding-advanced-ndt-semiconductor-inspection)
- **Chipmakers building their own capacity:** Samsung and SK hynix are expanding microscope purchases for HBM testing and failure analysis (paywalled; lead only) - [DigiTimes, 27 Mar 2026](https://www.digitimes.com/news/a20260326PD215.html); SK hynix co-developed in-house HBM4 system-level test equipment (TheElec via TrendForce, Jan 2026) - [TrendForce](https://www.trendforce.com/news/?p=53622)
- **Korean X-ray/CT:** Techvalley supplied custom CT inspection systems to Samsung and SK hynix (TheElec via Pulse.bot, Apr 2026; not opened) - [Pulse.bot](https://www.pulse.bot/manufacturing/news/techvalley-supplies-hbm-inspection-equipment-to-samsung-electronics-and-sk-hynix-354d0453-6d5a-4af2-ada4-528dee7754a4/)
- **Koh Young:** markets a True3D advanced-packaging metrology/inspection portfolio (release, 26 Aug 2026) - [Koh Young](https://www.circuitnet.com/press-files/20260826-koh-young-advances-the-measurement-conversation-at-electronics-packaging-symposium-2026.pdf)
- **In filings:** Onto names KLA and Camtek (AP inspection), KLA and Nova (films/OCD), Nova (integrated metrology), Ushio and Canon (AP lithography), GigaVis (panel inspection), PDF Solutions (software) - [Onto 10-K](https://www.sec.gov/Archives/edgar/data/704532/000119312526066937/onto-20260103.htm). Nova "compete[s] mainly with Onto Innovation Inc., and KLA Corp.", plus process-tool makers' in-situ sensors and new Chinese entrants - [Nova 20-F](https://www.sec.gov/Archives/edgar/data/0001109345/000117891326000504/zk2634307.htm). Chroma ATE owns 16.79% of Camtek - [Camtek 20-F](https://www.sec.gov/Archives/edgar/data/0001109138/000117891326001561/zk2634678.htm)
- Not gathered (out of scope, covered elsewhere): Intekplus, Unity-SC/Merck detail, Confovis, Nordson, Toray Engineering, Cohu, Cheng Mei, Chinese suppliers.

---

## 3. Key question: company-specific items

### 3.1 Onto
- Semilab: agreed 30 Jun 2025 ($475M cash + 706,215 shares, four lines); after a DOJ second request it excluded "a relatively small product line"; final $432.3M cash + 641,771 shares (~ $495M) - [Onto Q3 2025 call](https://www.fool.com/earnings/call-transcripts/2025/11/07/onto-innovation-onto-q3-2025-earnings-transcript/); closed 17 Nov 2025 with FAaST, CnCV, MBIR (contamination, materials and surface-charge metrology) - [BusinessWire](https://www.businesswire.com/news/home/20251117149029/en/Onto-Innovation-Completes-Acquisition-of-Unique-Materials-Composition-and-Electrical-Analysis-Product-Lines-from-Semilab-International). Expected ~ $120M of 2026 revenue (company, via search summary; not opened). Third-party estimates: ~ $21M in Q3 2026 and an H1 run-rate of ~ $92M/yr against a $130M original target - [Finsee](https://finsee.ai/earnings/onto/2026/q3/en/).
- Converts and Rigaku: 0% notes due 1 Jun 2031, upsized pricing 19 May 2026, conversion price $381.80 - [Placera](https://www.placera.se/telegram/onto-innovation-onto-innovation-prices-upsized-1-3-billion-convertible-notes-due-2031-20260519); $1.5B total, capped call raises the dilution strike to $509.06, ~ $200M buybacks; X-ray chip market ~ $1B - [Allmind Q2 2026](https://allmind.ai/earnings/event/2943270)
- Front end: Atlas G6 at "several nodes below 2 nm"; multiple Atlas tools to a major DRAM customer in 2H 2026; Iris G2 qualifications take 6-12 months (CC-U) - [Allmind Q2 2026](https://allmind.ai/earnings/event/2943270)
- Manufacturing and tariffs: >30% of Q3 2025 shipments from Asian extended factories, >60% targeted by end-2026, ~1 point of GM lost to tariffs in Q3 2025 - [Q3 2025 call](https://www.fool.com/earnings/call-transcripts/2025/11/07/onto-innovation-onto-q3-2025-earnings-transcript/); Asian factories add capacity roughly equal to US in-house plants (~ $2B) - [Q2 2026](https://allmind.ai/earnings/event/2943270)
- Panel and photonics: panel revenue to double in 2026; silicon-photonics orders >$50M (CC-U) - [Q2 2026](https://allmind.ai/earnings/event/2943270)

### 3.2 Nova
- GAA: cumulative $500M 2024-26 on track; metrology intensity ~30% above FinFET; Metrion at 4 of 5 targets; significant XPS order from a major memory customer; new XPS entrants ~2H 2027; AncoScene released to volume production at a leading foundry; KLA named as front-end chemical-metrology rival (CC-U) - [TradingKey transcript](https://www.tradingkey.com/news/transcripts/262284988-)
- Deals: Sentronics, Mannheim, 30 Jan 2025, $60.2M cash; ancosys Jan 2022; no 2026 acquisition found - [Nova 20-F](https://www.sec.gov/Archives/edgar/data/0001109345/000117891326000504/zk2634307.htm)
- Converts: $750M 0% due 15 Sep 2030, conversion ~ $320.16, capped-call cap ~ $415.03; 2025 notes fully converted in 2025 - [Nova 20-F](https://www.sec.gov/Archives/edgar/data/0001109345/000117891326000504/zk2634307.htm)
- Machine learning: MARS (physical modelling), Nova FIT (ML for films/CD and VeraFlex), HPC, Fleet Management - [Nova 20-F](https://www.sec.gov/Archives/edgar/data/0001109345/000117891326000504/zk2634307.htm). 2022: physical + ML to "reduce time to solution", "cloud-based Fleet Management connectivity with big-data analytics" - [Nova Investor Day 2022 transcript](https://novami.com/wp-content/uploads/2023/04/investor-day-2022-all-transcripts-final.pdf). Neither document says how reference data for training are obtained.

### 3.3 Camtek
- Products: Hawk (Feb 2025; chiplets, HBM, hybrid bonding), Eagle G5 (Sep 2024), MicroProf AP (FRT, bought 1 Nov 2023 for $100M), Golden Eagle (panel); installed base >3,000 (Dec 2025) - [Camtek 20-F](https://www.sec.gov/Archives/edgar/data/0001109138/000117891326001561/zk2634678.htm); ~4,000 (Nov 2026) - [MarketBeat](https://www.marketbeat.com/instant-alerts/transcript-camtek-q3-earnings-call-highlights-2026-11-04/)
- Converts: $500M 0% due 15 Sep 2030, conversion ~ $109.34; ~ $267.0M used to repurchase ~ $167.1M of 2026 notes - [Camtek 20-F](https://www.sec.gov/Archives/edgar/data/0001109138/000117891326001561/zk2634678.htm)
- Shareholders (5 Mar 2026): Priortech 20.66%, Chroma 16.79% (joint control), Wasatch 6.80%, Harel 5.3%, Migdal 5.09% - [Camtek 20-F](https://www.sec.gov/Archives/edgar/data/0001109138/000117891326001561/zk2634678.htm)
- Visual Layer: Tel Aviv visual-AI firm; terms not disclosed; deployment location (tool, customer site or cloud) not stated - [Camtek release, 13 Apr 2026](https://www.camtek.com/news-and-events/camtek-announces-acquisition-of-visual-layer-to-deepen-its-visual-ai-capabilities-in-its-inspection-and-metrology-offering/)
- Competition: "does not see smaller Chinese competitors as a significant threat"; hybrid bonding meaningful from 2028 (CC) - [MarketBeat](https://www.marketbeat.com/instant-alerts/transcript-camtek-q3-earnings-call-highlights-2026-11-04/)

---

## 4. Key question: resilience to 2030 and export controls

Cited: BIS extended the Affiliates Rule suspension to 10 Jan 2027 (announced 5 Nov 2026), matching the US-China agreement extension to the same date. Absent a permanent deal, the rule and China's rare-earth controls could take effect in January - [Thompson Hine, Nov 2026](https://www.thompsonhinesmartrade.com/2026/11/bis-extends-affiliates-rule-until-january-2027/); [GlobalSanctions, Nov 2026](https://globalsanctions.com/2026/11/us-bis-extends-suspension-50-rule-coming-into-force-until-10-january-2027/). Nova's 20-F says China's gallium/germanium export ban is suspended until 27 Nov 2026 - [Nova 20-F](https://www.sec.gov/Archives/edgar/data/0001109345/000117891326000504/zk2634307.htm).

Inferences (scenarios):
- **Steady growth (compute supply ~2x/yr):** all three are limited by capacity, not demand, in 2026-27 (Onto backlog >$1.3B; Camtek "visibility a year ahead" for the first time; Nova supply-chain strain and a new Asian clean room). Camtek's single Israeli plant and memory/CPU component shortages are the tightest constraints named.
- **Financing-led pause ~2028:** exposure follows AI-packaging share: Camtek ~80% AP (OSATs >50% of orders, part of 2027 outlook resting on non-binding forecasts), Onto ~50% AP, Nova ~25% of product revenue AP with GAA/DRAM drivers. Balance sheets: Nova net cash ~ $1.05B (derived), Camtek ~ $388M, Onto net debt ~ $222M against a ~ $679M listed Rigaku stake.
- **Acceleration:** Onto's Asian contract capacity roughly doubles output potential; Camtek's hybrid-bonding revenue only from 2028.
- **China/export controls:** China = Camtek 49%, Nova 33%, Onto 7% (FY2025). The January 2027 deadline is a live risk for Camtek and Nova.

---

## 5. Entry-point data (separate from quality)

- **ONTO** ($215.06, +8.9% on 11 Nov): market cap $10.56B, EV $10.78B, trailing P/E 70.6, forward 17.9, EV/Sales 8.2, EV/EBITDA 27.3, EV/FCF 43.5, beta 1.68; consensus (12 analysts) revenue $1.49B (FY2026) and $2.02B (FY2027), EPS $8.48 / $12.86, mean target $336 - [statistics](https://stockanalysis.com/stocks/onto/statistics/), [forecast](https://stockanalysis.com/stocks/onto/forecast/). FY2021-25 forward P/E 22.6, 15.5, 34.4, 27.4, 30.1 - [ratios](https://stockanalysis.com/stocks/onto/financials/ratios/). Market cap ~ $15.14B on 11 Aug 2026 (search snippet) - [247WallSt](https://247wallst.com/investing/2026/08/11/onto-innovation-jumps-6-tuesday-following-camtek-earnings-and-nvidias-500-billion-partnership/).
- **NVMI** ($340.62, +4.6%): market cap $10.83B, EV $9.84B, trailing P/E 39.0, forward 25.7, EV/Sales 9.8, EV/EBITDA 30.2, beta 1.88; consensus (8) revenue $1.08B / $1.36B, EPS $10.67 / $13.66, mean target $406 - [statistics](https://stockanalysis.com/stocks/nvmi/statistics/), [forecast](https://stockanalysis.com/stocks/nvmi/forecast/). FY2021-25 forward P/E 34.1, 18.7, 27.1, 26.2, 36.4 - [ratios](https://stockanalysis.com/stocks/nvmi/financials/ratios/). High $615.99 (15 Jun 2026); $385.12 on 29 Sep 2026 - [CMC](https://www.cmcmarkets.com/en-au/opto/camt-vs-nvmi-vs-onto-the-chip-packaging-arms-race). A report of a fall to $277.80 after Q3 results conflicts with later prices (could not verify) - [Webull](https://www.webull.com/news/15871592738612224).
- **CAMT** ($107.05, +4.8%): market cap $5.00B, EV $4.61B, trailing P/E 40.4, forward 21.6, EV/Sales 8.5, EV/EBITDA 31.8, beta 1.73, shares outstanding +3.9% YoY; consensus (11; one Strong Sell) revenue $596M / $804M, EPS $3.60 / $5.13, mean target $153 - [statistics](https://stockanalysis.com/stocks/camt/statistics/), [forecast](https://stockanalysis.com/stocks/camt/forecast/). FY2021-25 forward P/E 27.3, 13.1, 31.0, 26.2, 33.6 - [ratios](https://stockanalysis.com/stocks/camt/financials/ratios/). High $210.20 (24 Apr 2026); +43.7% YTD at 29 Sep 2026 - [CMC](https://www.cmcmarkets.com/en-au/opto/camt-vs-nvmi-vs-onto-the-chip-packaging-arms-race).
- **Cycle position:** all three at record revenue and order books; consensus 2027 growth 26-36%; Gartner WFE +12% in 2026 (via Nova 20-F); SEMI equipment record $145B in 2026 (via Camtek 20-F).
- **Near-term events:** BIS Affiliates Rule / US-China deadline 10 Jan 2027; Q4 2026 results for all three ~Feb 2027 (dates not found); Nova Investor Day 9 Mar 2027 and $200M buyback from 2 Sep 2026 - [Nova releases](https://www.novami.com/investors/press-releases/), [buyback](https://www.novami.com/investors/press-releases/nova-announces-200m-share-repurchase-program/); Onto's quarterly Rigaku mark; Camtek software launch Q1 2027 and its Q4 gross-margin test (~52.5% needed for the year-end target, per Finsee); Nova XPS competition 2H 2027.
- **Inference:** on trailing EV/Sales all three sit near the top of their FY2021-25 range, but on forward P/E all three are below their own 5-year average, on consensus that assumes 26-36% growth in 2027. The October-November 2026 sell-off (Onto ~-30% from August, Nova ~-45% and Camtek ~-49% from 2026 highs) came while estimates rose; its cause was not verified.

---

## 6. Could not verify
- Third-party (Yole, TechInsights, Gartner, broker) market shares for AP inspection, OCD, XPS, or HBM/CoWoS steps; Yole and TheElec pages were blocked or paywalled.
- Named tool-of-record holders by step at TSMC CoWoS/SoIC, SK hynix, Samsung and Micron; which HBM maker and incumbent Onto displaced.
- Outside confirmation of a 2024-25 Onto-to-Camtek share shift (the only outside view blames KLA, unsourced).
- How Nova or Onto obtain reference cross-section data to train models; any published measurement uncertainty.
- Software revenue for any of the three; Camtek product vs service split.
- 2026 China shares and named >=10% customers; date of Onto's SK hynix award release (~Oct 2026 by URL); date of an Onto TSMC supplier honour (headline only) - [Barchart](https://www.barchart.com/story/news/15487589/onto-innovation-receives-tsmc-honor-for-unique-advanced-node-and-packaging-technologies).
- KLA's advanced-packaging revenue (two conflicting figures).
- Local-language coverage is thin: TheElec only via secondary sites; no DigiTimes body text, Globes, Calcalist or TASE filings.

## 7. Sources (document date; all accessed 12 Nov 2026)
Primary filings and releases:
- Onto 8-K Ex.99.1, Q3 2026 results, 9 Nov 2026 - https://www.sec.gov/Archives/edgar/data/0000704532/000119312526453582/onto-ex99_1.htm
- Onto 10-Q, Q3 2026, 9 Nov 2026 - https://www.sec.gov/Archives/edgar/data/704532/000119312526453859/onto-20260930.htm
- Onto 10-K, FY ended 3 Jan 2026 - https://www.sec.gov/Archives/edgar/data/704532/000119312526066937/onto-20260103.htm
- Onto Dragonfly G5 launch, 16 Mar 2026 - https://investors.ontoinnovation.com/news/news-details/2026/Onto-Innovation-Launches-Dragonfly-G5-Inspection-System/
- Onto G5 2.5D qualification, 16 Apr 2026 - https://s24.q4cdn.com/480160064/files/doc_news/Onto-Innovations-Dragonfly-G5-System-Qualified-for-Applications-in-2-5D-AI-Packaging-2026.pdf
- Onto Semilab closing, 17 Nov 2025 - https://www.businesswire.com/news/home/20251117149029/en/Onto-Innovation-Completes-Acquisition-of-Unique-Materials-Composition-and-Electrical-Analysis-Product-Lines-from-Semilab-International
- Nova 6-K, Q3 2026 results, 5 Nov 2026 - https://www.sec.gov/Archives/edgar/data/0001109345/000117891326005034/zk2636340.htm
- Nova 20-F FY2025, Feb 2026 - https://www.sec.gov/Archives/edgar/data/0001109345/000117891326000504/zk2634307.htm
- Nova WMC release, 2 Jul 2026 - https://www.novami.com/investors/press-releases/nova-wmc-expanding-adoption-across-the-most-advanced-packaging-processes/
- Nova $200M buyback, 2 Sep 2026 - https://www.novami.com/investors/press-releases/nova-announces-200m-share-repurchase-program/
- Nova Investor Day 2022 transcript (published Apr 2023) - https://novami.com/wp-content/uploads/2023/04/investor-day-2022-all-transcripts-final.pdf
- Camtek 6-K, Q3 2026 results, 4 Nov 2026 - https://www.sec.gov/Archives/edgar/data/0001109138/000117891326005000/zk2636329.htm
- Camtek pre-announcement, 14 Oct 2026 - https://www.prnewswire.com/il/news-releases/camtek-pre-announces-record-q3-revenues-above-guidance-provides-record-q4-guidance-and-initial-revenue-outlook-for-2027-302908515.html
- Camtek 20-F FY2025, Mar 2026 - https://www.sec.gov/Archives/edgar/data/0001109138/000117891326001561/zk2634678.htm
- Camtek FY2025 results, 18 Feb 2026 - https://www.camtek.com/news-and-events/camtek-announces-record-results-for-the-fourth-quarter-full-year-2025/
- Camtek order releases, 10 Feb 2026 and 2 Jun 2026 (6-K), Visual Layer 13 Apr 2026; newsroom index incl. Intel EPIC award 9 Apr 2025 - https://www.camtek.com/newsroom/

Call summaries and transcripts: MarketBeat (Camtek 4 Nov, Nova 6 Nov, Onto Nov 2026); TradingKey Nova transcript (Nov 2026); Allmind (Camtek Q3 2025, Onto Q2 2026, Camtek Q2 2026); Motley Fool Onto Q3 2025 (7 Nov 2025). URLs inline above.

Third-party: Finsee reviews of Onto, Nova, Camtek (Nov 2026) and KLA (~Apr 2026); CMC Markets (1 Oct 2026); Silicon Semiconductor/Yole (13 Jul 2026); Castellano Substack (8 May 2025; 12 May 2026); Irrational Analysis (11 May 2025); Cloud News/TheElec (~Apr 2026); OneStopNDT (1 Apr 2026); DigiTimes (27 Mar 2026); BriefGlance and Webull on the SK hynix award (Sep-Oct 2026); Thompson Hine and GlobalSanctions on BIS (Nov 2026); stockanalysis.com statistics, forecasts and ratios (12 Nov 2026). URLs inline above.
