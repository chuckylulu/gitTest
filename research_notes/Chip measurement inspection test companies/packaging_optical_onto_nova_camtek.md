# Onto Innovation, Nova, Camtek and the advanced-packaging inspection/metrology landscape

Research date: **12 November 2026**. Latest quarter for all three = Jul-Sep 2026 (Q3 2026), reported 4 Nov (Camtek), 5 Nov (Nova), 9 Nov (Onto) 2026. Prices = close 11 Nov 2026 (stockanalysis.com, checked 12 Nov 2026). Non-GAAP unless marked GAAP. **CC-U** = company claim, unconfirmed by any outside party I found. **Derived** = my arithmetic from cited figures. Status: **v1, written after an interruption; items marked [INCOMPLETE] were still being checked.**

Changes versus the brief's background: (1) Onto's Semilab deal closed 17 Nov 2025 at ~$495M for three product lines, not the four announced (one line excluded after a US DOJ second request); (2) new since the brief: Onto bought 27% of Rigaku (Japan, X-ray metrology) for $719.5M on 10 Aug 2026, funded by $1.5B of 0% converts due 2031; Camtek bought Visual Layer (visual AI, Apr 2026); (3) Camtek "controlling shareholder" is a pair, Priortech 20.66% + Chroma ATE 16.79% under a voting agreement (38.04%, Mar 2026); (4) the 2024-25 Onto-to-Camtek share shift could not be confirmed by any outside source (see section 2.1).

---

## 0. Evidence tables

### 0.1 Onto Innovation (NYSE: ONTO) - quality and transitions

| Test | Evidence (date, source in section 2/6) |
|---|---|
| (a) Position | Owns several wafer-release measurements: OCD (Atlas G6; "several nodes below 2 nm" and DRAM, CC-U, Aug 2026), 2D bump/package inspection (Dragonfly G5) and 3D bump metrology (3Di) in 2.5D and HBM; film/charge/contamination metrology (Semilab lines FAaST, CnCV, MBIR, Nov 2025). Also sells a process tool (JetStep panel lithography). Reference cross-sections sit with customers; no disclosure of access. 27% Rigaku stake adds X-ray (buried-feature) physics (Aug 2026). |
| (b) Lead | Outside evidence thin. 10-K names KLA and Camtek as AP-inspection rivals, KLA and Nova in OCD. TOR claims all CC-U: leading HBM maker picked G5 for most 2D inspection and 3Di "displacing the previously established tool of record" (16 Mar 2026); G5 qualified at 2.5D logic customer (16 Apr 2026); >10 G5 customers, 2027 G5 POs = 2x 2026 G5 revenue (9 Nov 2026); one OSAT >$200M Dragonfly orders (6 Aug 2026). No third-party share data found. |
| (c) Revenue model | FY2025: systems+software 84% ($847.8M), parts 8% ($84.2M), services 8% ($73.2M). Q3 2026: software+services ~ $60M of $409.7M (~15%, derived). Software (Discover yield, AI Diffract OCD modelling) not reported separately. No hours/seat revenue disclosed. |
| (d) Financials | Q3 2026: GM 57.6% (GAAP 54.8%), op margin 32.6% (GAAP 23.3%), FCF ~ $80M. FY2025 GAAP GM 49.7%, GAAP op margin 13.2%, CFO $328.3M, capex $28.5M (FCF ~ $300M derived). Cash $1.25B vs 2031 converts $1.47B (net debt ~ $222M) plus Rigaku stake carried at $678.7M. ROIC 12.7% TTM. Customers FY2025: A 20%, B 15%, C 14% (unnamed; 10-K cites TSMC, Samsung as large sources). China 7% FY2025 (12% FY2024, 17% FY2023); Taiwan 32%, Korea 28%. |
| (e) Resilience | Backlog >$1.3B (Nov 2026) with 2027 and some 2028 visibility; AP is ~half of revenue and split ~evenly 2.5D logic/HBM, so high beta to AI capex. Low China share limits export-control exposure. Tariffs: shifting >60% of production to Asian contract factories by end-2026 (target, Nov 2025). Rigaku stake is marked to market each quarter (-$40.8M Q3 2026). |
| T1 imaging -> inference | Did: OCD is model-based inference; AI Diffract; Rigaku X-ray stake ($719.5M). Stated measurement uncertainty: none published. |
| T2 AI recipes | Said: G5 ML die-to-die detection "reduces recipe setup time" (CC-U, Mar 2026). No disclosure of applications-engineering revenue. |
| T3 bonded stacks | Did: G5 targets CMP and hybrid bonding, sub-surface defect inspection; 3Di new sub-surface applications (Aug 2026); Semilab electrical/charge lines. No electrical-test product. |
| T4 HW -> software/data | Software exists but is not broken out; PDF Solutions named as software rival (10-K). Nothing further found. |
| T5 on-prem AI | Nothing found. |
| T6 fewer tools after 2030 | Nothing found. |

### 0.2 Nova Ltd. (Nasdaq/TASE: NVMI) - quality and transitions

| Test | Evidence |
|---|---|
| (a) Position | Owns wafer-release measurements in OCD (integrated inside process tools, and stand-alone), films, materials (XPS VeraFlex, SIMS Metrion, Raman Elipson) and plating-bath chemistry (Ancolyzer, AncoScene, a physical-constraint measurement). Inference-heavy by design (scatterometry + MARS physical models + Nova FIT ML). 20-F does not say how training/reference data are obtained. |
| (b) Lead | Partly outside: product revenue CAGR 27.5% (2020-25) vs Gartner process-control CAGR 16.0% (Gartner Dec 2025, cited in 20-F). No third-party OCD/XPS share figure found; SemiAnalysis (undated) calls Nova high-share in integrated OCD and materials metrology. TOR claims CC-U: WMC tool of record at a leading global foundry for multi-layer AP measurement (2 Jul 2026); AncoScene released to HVM at a leading foundry (Q3 2026); Metrion at 4 of 5 target customers; GAA revenue on track for $500M cumulative 2024-26. |
| (c) Revenue model | FY2025 products 80% ($705.6M) / services 20% ($175.0M, +31%); service GM 47% vs product 60%. Q3 2026 services $56.0M (19%). Services include "time and material" work (labour-linked). Software not separately disclosed. |
| (d) Financials | FY2025: revenue $880.6M (+31%), GM 57%, GAAP op income $253.5M (28.8%), net income $259.2M, CFO $245.6M, capex $27.7M (FCF ~ $218M derived). Q3 2026: GM 59.1% (GAAP 57.7%), op margin 35.5% (GAAP 32%), FCF $132M. Cash+investments ~$1.79B vs converts $734.6M (net cash $987M). ROIC 20.4% TTM. Customers FY2025: A 23%, B 10%, top-5 51%; Q3 2026: four customers each >=10% of product revenue. China 33% (2025), 39% (2024), 36% (2023). |
| (e) Resilience | Q3 2026 product mix: logic/foundry ~61%, memory ~39%; AP ~ one quarter of product revenue (Q2 2026, CC). Front-end GAA/DRAM drivers diversify away from pure AI packaging. Export controls: US subsidiary needs licences for some Chinese customers; BIS "Affiliates Rule" suspension was set to end 9 Nov 2026 (status after that: could not verify). New XPS competitor expected 2H 2027 (CC). |
| T1 | Core business is inference (OCD/XPS models). No published uncertainty budget found. |
| T2 | ML (Nova FIT) on top of physical modelling since ~2020 (20-F). No disclosure of effect on applications-engineering. [INCOMPLETE] |
| T3 | Sentronics ($60.2M cash, 30 Jan 2025) -> WMC platform for 2.5D/3D AP; >10 WMC customers (Nov 2026); chemical metrology for TSV/plating; HBM AP revenue records. Hybrid-bonding TOR: none disclosed. |
| T4 | Software suite (MARS, FIT, HPC, Fleet Management) sold "coupled" with hardware; no separate revenue. |
| T5 | Nova HPC "computational management layer" and centralised fleet management suggest on-premises compute (inference, not confirmed). |
| T6 | Nothing found. |

### 0.3 Camtek Ltd. (Nasdaq/TASE: CAMT) - quality and transitions

| Test | Evidence |
|---|---|
| (a) Position | Optical 2D inspection and 3D bump metrology for packaging wafers (HBM, CoWoS-like at OSATs, chiplets) plus FRT surface metrology. Mostly imaging; no access to reference data disclosed. Hawk: 150 nm defects, measures 500M micro-bumps at <12 um pitch (CC-U, 20-F). |
| (b) Lead | TOR claims CC-U: "tool of record for all the 3D metrology for HBM4 at all the HBM manufacturers" and several 2D steps (Q3 2025 call, Nov 2025); "we have not lost any market share" (same call). Partly contradicted by Onto's Mar 2026 claim of displacing an established 3D-metrology TOR at an HBM maker. Outside: Intel 2025 EPIC Supplier Award (9 Apr 2025). Orders: $25M Hawk from tier-1 IDM (Feb 2026, $45M with repeats), $31M OSAT (Mar 2026), $55M tier-1 OSAT + >$50M Hawk from a leading HBM maker (Jun 2026). No third-party share data found. |
| (c) Revenue model | Overwhelmingly systems. Services ~ $40M in 2026 (~7% of revenue, CC), target ~ $100M in ~3 years; AI software sales to start 2027 (double-digit $M), ~ $40M software in long-term model. |
| (d) Financials | FY2025: revenue $496.1M (+16%), GM 51.6% (GAAP 50.5%), op margin 30.0% (GAAP 25.8%), CFO $142.6M, capex $22.5M (FCF ~ $120M derived). Q3 2026: GM 51.1%, op margin 29.5%, CFO $71.1M. Cash $877.1M vs converts $489.2M (net cash $387.9M). ROIC 18.8% TTM. One customer 11% (2025). China 49.2% of 2025 revenue (30.9% 2024, 47.4% 2023); Korea fell to 7.4% (2025) from 27.3% (2024). |
| (e) Resilience | ~80% of Q3 2026 revenue = advanced packaging, mostly AI; OSATs > half of 2026 orders; China ~half of revenue (export-control exposure; entity-list risk named in filings). Single main plant (Migdal HaEmek, Israel) plus German FRT site; Strait of Hormuz/Middle East risk cited. GM pressured by component costs and a stronger shekel. Controlled jointly by Priortech + Chroma (38.04%). |
| T1 | Direct optical 3D measurement; no inference-with-uncertainty product disclosed. |
| T2 | AI inspection + automatic defect classification offered from 2026 (20-F); Visual Layer acquisition (13-14 Apr 2026, terms undisclosed); goodwill +$38.4M in 2026 (derived). |
| T3 | Hawk marketed for hybrid bonding; HB activity "low", meaningful from 2028 (Nov 2026). |
| T4 | Software as "additional and recurring revenue stream" (CC, Apr 2026); first sales expected Q1 2027. |
| T5 / T6 | Nothing found. |

### 0.4 Entry-point snapshot (kept separate from quality; detail in section 5)

| Item (close 11 Nov 2026) | ONTO | NVMI | CAMT |
|---|---|---|---|
| Price / market cap / EV | $215.06 / $10.56B / $10.78B | $340.62 / $10.83B / $9.84B | $107.05 / $5.00B / $4.61B |
| P/E trailing (GAAP) / forward (NTM) / on FY2026 consensus | 70.6 / 17.9 / 25.4 | 39.0 / 25.7 / 31.9 | 40.4 / 21.6 / 29.7 |
| EV/Sales / EV/EBITDA (TTM) | 8.2 / 27.3 | 9.8 / 30.2 | 8.5 / 31.8 |
| FY2021-25 range: P/E; EV/Sales; EV/EBITDA | 15.1-61.9; 2.8-8.5; 9.4-35.6 | 16.7-44.9; 3.7-10.6; 12.7-33.6 | 12.2-96.0; 2.4-9.3; 9.1-40.0 |
| Consensus revenue FY2026 / FY2027 | $1.49B (+48%) / $2.02B (+36%) | $1.08B (+22%) / $1.36B (+26%) | $596M (+20%) / $804M (+35%) |
| Consensus EPS FY2026 / FY2027 | $8.48 / $12.86 | $10.67 / $13.66 | $3.60 / $5.13 |
| Latest guidance | Q4 rev $430-450M; FY2026 >45% growth | Q4 rev $305-315M; 2026 > $1B | Q4 ~ $180M; FY2026 ~ $595M; 2027 > $800M; $1.2B in ~3 yrs |
| 52-week change / drawdown | +52%; Aug 11 cap ~$15.1B -> $10.6B | +7%; ATH $615.99 (15 Jun 2026) | -4%; ATH $210.20 (24 Apr 2026) |
| Convert conversion price vs price | $381.80 (cap $509.06) - out of the money | $320.16 (cap $415.03) - in the money | $109.34 - at the money |
| Next events | Q4 results ~Feb 2027 (date not found) | Investor Day 9 Mar 2027; Q4 ~Feb 2027 | Q4 ~Feb 2027; software launch Q1 2027 |

---

## 1. Key question: 2025 and Q3 2026 results, mix, margins, cash, customers, China, guidance

### Takeaway
All three posted records in Q3 2026 with AI packaging and front-end AI-linked memory/logic as the drivers. Onto grew fastest (+88% YoY) but carries net debt after the Rigaku purchase; Nova has the highest margins and net cash, with the most front-end diversification; Camtek is the most packaging- and China-concentrated and has the lowest gross margin.

### Cited findings - Onto
- Q3 2026 (quarter to 30 Sep 2026, released 9 Nov 2026): revenue $409.7M (+87.8% YoY from $218.2M; +19% QoQ); GAAP GM 54.8%, non-GAAP 57.6%; GAAP op income $95.4M (23.3%), non-GAAP $133.5M (32.6%); GAAP net income $46.8M ($0.95), non-GAAP $120.3M ($2.44); 9M revenue $1.045B (+41.5%); cash and securities $1,251.5M; "2031 Notes, net" $1,473.2M; inventories $424.2M; equity $1,979.3M; backlog >$1.3B; record Advanced Nodes on Atlas G6 adoption; record AP/specialty on Dragonfly G5 and Firefly; Rigaku 27% stake closed in August with a $40.8M unrealised loss - [Onto 8-K Ex.99.1, 9 Nov 2026](https://www.sec.gov/Archives/edgar/data/0000704532/000119312526453582/onto-ex99_1.htm)
- Q4 2026 guidance: revenue $430-450M, GM 57.7-58.3%, non-GAAP op margin 33.5-34.5%, non-GAAP EPS $2.59-2.79; CEO expects 2026 growth >45% - [same 8-K](https://www.sec.gov/Archives/edgar/data/0000704532/000119312526453582/onto-ex99_1.htm)
- Q3 2026 call: Advanced Nodes ~ $135M (~60% memory, 40% logic); software and services ~ $60M; AP/specialty up 35% QoQ, "a little over half" of revenue (~ $215M derived); 2026 AP growth >80%, split ~evenly 2.5D logic/HBM; Advanced Nodes >35%; panel (JetStep) revenue to double; 3Di Q4 revenue > Q1-Q3 combined; 2027: AP >35% growth, Advanced Nodes faster than 2026, panel >40%; Q3 FCF ~ $80M - [MarketBeat call summary, Nov 2026](https://www.marketbeat.com/instant-alerts/transcript-onto-innovation-q3-earnings-call-highlights-2026-11-09/)
- 10-Q Q3 2026: Rigaku cash cost $719.5M, carrying value $678.7M at 30 Sep 2026 (Level 2 fair value); 2031 notes net proceeds $1,471.0M; capped call $89.0M; 9M buybacks $205.0M; 9M CFO $166.6M, capex $8.8M; goodwill $625.8M - [Onto 10-Q, filed 9 Nov 2026](https://www.sec.gov/Archives/edgar/data/704532/000119312526453859/onto-20260930.htm)
- FY2025 (year to 3 Jan 2026): revenue $1,005.3M (FY2024 $987.3M); GAAP GM 49.7% (52.2%); GAAP op margin 13.2% (19.0%); R&D $132.0M; net income $136.8M; CFO $328.3M; capex $28.5M; buybacks $75.0M; cash $639.6M; systems revenue fell mainly on "fewer inspection units shipped for advanced packaging for AI chips"; geography Taiwan 32%, S. Korea 28%, US 12%, Japan 10%, China 7%, SE Asia 6%, Europe 5%; customers A 20% (23% FY2024), B 15% (17%), C 14% (12%); ~1,615 staff - [Onto 10-K FY2025](https://www.sec.gov/Archives/edgar/data/704532/000119312526066937/onto-20260103.htm)
- Q3 2025 baseline: AN $54M (25%), specialty+AP $113M (52%), software+services $51M (~23%) - [Onto Q3 2025 call, 7 Nov 2025](https://www.fool.com/earnings/call-transcripts/2025/11/07/onto-innovation-onto-q3-2025-earnings-transcript/)
- Third-party summaries (not primary, flagged): four customers = 57% of 1H/9M 2026 revenue - [Finsee, Nov 2026](https://finsee.ai/earnings/onto/2026/q3/en/); [Panabee (AI-generated), Nov 2026](https://www.panabee.com/news/onto-innovation-earnings-q3-2026). China share for 2026 not found.

### Cited findings - Nova
- Q3 2026 (released 5 Nov 2026): revenue $287.8M (products $231.9M, services $56.0M; +28% YoY, +13% QoQ); GAAP GM 57.7%, non-GAAP ~59%; GAAP op income $92.8M (32%), non-GAAP $102.2M; GAAP net income $90.0M ($2.64), non-GAAP $98.4M ($2.86); cash $188.2M + deposits $395.9M + securities $1,205.1M; convertible notes, net $734.6M; equity $1,511.7M; Q3 CFO $138.1M, capex $6.4M; Q4 guidance revenue $305-315M, GAAP EPS $2.78-2.93, non-GAAP $3.03-3.18; records in AP (HBM and advanced-logic capacity) and memory - [Nova 6-K, 5 Nov 2026](https://www.sec.gov/Archives/edgar/data/0001109345/000117891326005034/zk2636340.htm)
- Call: product revenue ~61% logic/foundry, 39% memory; four customers and four territories each >=10% of product revenue; FCF $132M (9M ~ $206M); buyback $38.5M in Q3; surpassed $1B TTM revenue, expects 2026 > $1B "a year ahead" of plan; 2H26 revenue >33% above 2H25 - [MarketBeat, 6 Nov 2026](https://www.marketbeat.com/instant-alerts/transcript-nova-q3-earnings-call-highlights-2026-11-06/); China share in 2026 "lower than 2025, but still nominally grow" - [TradingKey transcript, Nov 2026](https://www.tradingkey.com/news/transcripts/262284988-)
- FY2025: revenue $880.6M (2024 $672.4M; 2023 $517.9M); products $705.6M, services $175.0M; GM 57%; GAAP op income $253.5M; net income $259.2M; CFO $245.6M; capex $27.7M; cash+investments $1,646M; geography China 33% (39%, 36%), Taiwan 29%, Korea 16%, USA 9%, other 13%; Customer A 23% (18%, 19%), Customer B 10% (14%, 18%); top-5 51% - [Nova 20-F FY2025, filed Feb 2026](https://www.sec.gov/Archives/edgar/data/0001109345/000117891326000504/zk2634307.htm) ([PDF](https://www.novami.com/wp-content/uploads/2026/02/a2634307.pdf))
- Q2 2026: revenue $255M (+16%), AP "nearly one-quarter of product revenue", advanced-logic revenue more than doubled QoQ - [CMC Markets, 1 Oct 2026](https://www.cmcmarkets.com/en-au/opto/camt-vs-nvmi-vs-onto-the-chip-packaging-arms-race)

### Cited findings - Camtek
- Q3 2026 (released 4 Nov 2026): revenue $161.3M (+28% YoY, +21% QoQ); GAAP GM 50.0%, non-GAAP 51.1%; GAAP op income $39.8M (24.7%), non-GAAP $47.5M (29.5%); GAAP net income $42.8M ($0.84), non-GAAP $50.3M ($0.99); 9M revenue $416.2M; CFO $71.1M; cash, deposits and securities $877.1M; convertible notes $489.2M (Dec 2025: $519.8M); goodwill $112.7M (Dec 2025: $74.3M); Q4 ~ $180M; FY2026 ~ $595M; 2027 > $800M - [Camtek 6-K, 4 Nov 2026](https://www.sec.gov/Archives/edgar/data/0001109138/000117891326005000/zk2636329.htm)
- Call: AP ~80% of Q3 sales, mostly AI; Eagle G5 + Hawk ~57% of systems revenue; >$800M orders YTD (~80% AP; OSATs slightly more than half); customers "including China" booking slots through 2027; GM pressure from component costs/shortages and the shekel, improvement from Q1 2027; $1.2B revenue target ~3 years out at 34-36% op margin, organic - [MarketBeat, 4 Nov 2026](https://www.marketbeat.com/instant-alerts/transcript-camtek-q3-earnings-call-highlights-2026-11-04/)
- FY2025: revenue $496.1M (+16%); GAAP GM 50.5%, non-GAAP 51.6%; non-GAAP op income $149.0M (30.0%); GAAP net income $50.7M after convert-repurchase loss; CFO $142.6M; cash $851.1M - [Camtek FY2025 release, 18 Feb 2026](https://www.camtek.com/news-and-events/camtek-announces-record-results-for-the-fourth-quarter-full-year-2025/)
- 20-F: geography 2025 China $243.9M (49.2%), other Asia-Pacific 34.1%, Korea $36.9M (7.4%; 2024 $117.1M, 27.3%), US 5.8%, Europe 3.5%; one customer 11% in 2025 (2024: 15%, 10%, 10%); ~50% of revenue from AI-related products; capex $22.5M mainly capacity; 709 staff (193 R&D) - [Camtek 20-F FY2025](https://www.sec.gov/Archives/edgar/data/0001109138/000117891326001561/zk2634678.htm)
- Q2 2026: AP ~75% of revenue; Asia 92%; orders >$600M YTD, OSATs >50% - [Allmind Q2 2026 call, 10 Aug 2026](https://allmind.ai/earnings/event/2953780); H1 2026 orders included ~$260M from HBM makers, mixing firm POs and non-binding forecasts (third-party summary) - [Finsee, Nov 2026](https://finsee.ai/earnings/camt/2026/q3/en/)

### Inferences
- Mix and margins: Nova earns 6-8 points more gross margin than Camtek and has a services line nearly three times Camtek's share of revenue; Onto sits between them but its GAAP margins are depressed by acquisition amortisation and Rigaku mark-to-market.
- Concentration: Nova's count of >=10% product customers rose from two (FY2025, total revenue basis) to four (Q3 2026); Onto's top three = 49% (FY2025). Camtek's customer list is the most spread (one customer at 11%), but its country exposure (China 49%) is the highest.

### Gaps
- Onto China share and named-customer split for 2026 (10-Q tables not read) [INCOMPLETE]. Camtek and Nova 2026 China shares not disclosed for Q3.

---

## 2. Key question: tool-of-record positions and competitive landscape in advanced-packaging inspection/metrology

### 2.1 Onto vs Camtek at 2.5D/CoWoS and HBM

**Takeaway.** The record supports an Onto setback in AI-packaging inspection in 2025 and a 2026 rebound driven by Dragonfly G5 and 3Di, but every share statement comes from the companies themselves; no outside share data were found.

Cited findings:
- Onto FY2025 systems revenue fell "mainly from fewer inspection units shipped for advanced packaging for AI chips" - [Onto 10-K FY2025](https://www.sec.gov/Archives/edgar/data/704532/000119312526066937/onto-20260103.htm)
- Q3 2025: 3Di "completed the full qualification process at not one but two high bandwidth memory customers"; a leading OSAT ordered 3Di for 2.5D AI packaging; packaging customers flagged "up to 20% more tools" in 2026 - [Onto Q3 2025 call](https://www.fool.com/earnings/call-transcripts/2025/11/07/onto-innovation-onto-q3-2025-earnings-transcript/)
- 16 Mar 2026: a leading HBM manufacturer selected G5 for most 2D inspection (double-digit systems) and ordered a similar number of 3Di "displacing the previously established tool of record"; G5 claims 150 nm sensitivity, up to 5x throughput; targets 2.5D/3D, HBM4, CMP and hybrid bonding (CC-U) - [Onto press release](https://investors.ontoinnovation.com/news/news-details/2026/Onto-Innovation-Launches-Dragonfly-G5-Inspection-System/)
- 16 Apr 2026: G5 qualified for "new and existing applications in 2.5D advanced packaging", shipments from June; Dragonfly platforms to grow >50% in 2026 (CC-U) - [Onto release](https://s24.q4cdn.com/480160064/files/doc_news/Onto-Innovations-Dragonfly-G5-System-Qualified-for-Applications-in-2-5D-AI-Packaging-2026.pdf)
- 6 Aug 2026: inspection +30% QoQ from 2.5D and HBM; growth "a mix of both" market and share; one OSAT >$200M Dragonfly orders, mostly 2027; Onto offers inspection/metrology for TSMC CoWoS panels (310 x 310 mm) (CC-U) - [Allmind Q2 2026 call](https://allmind.ai/earnings/event/2943270)
- 9 Nov 2026: >10 G5 customers; 2027 G5 POs = 2x 2026 G5 revenue (CC-U) - [MarketBeat](https://www.marketbeat.com/instant-alerts/transcript-onto-innovation-q3-earnings-call-highlights-2026-11-09/)
- Camtek, Nov 2025: "tool of record for all the 3D metrology for HBM4 at all the HBM manufacturers"; "we have not lost any market share"; CoWoS-like production shifting to OSATs; Eagle G5 chosen over "main competitor" for 2D at a major IDM (CC-U) - [Allmind Camtek Q3 2025 call](https://allmind.ai/earnings/event/bt_CAMT_2025_Q3)
- Camtek orders: ~$25M Hawk from a tier-1 IDM (AI; $45M with repeats; 10 Feb 2026) - [Camtek](https://www.camtek.com/news-and-events/camtek-receives-multiple-hawk-systems-order-of-approximately-25-million-from-an-idm-for-ai-applications/); $55M tier-1 OSAT + >$50M Hawk from a leading HBM maker, delivery 2027 (2 Jun 2026) - [Camtek 6-K](https://www.sec.gov/Archives/edgar/data/0001109138/000117891326003033/zk2635474.htm)

Inferences:
- The two companies' claims conflict for HBM 3D bump metrology: Camtek claimed TOR at all HBM makers (Nov 2025); Onto claims it displaced an established TOR at one HBM maker (Mar 2026). Both cannot be fully true from 2026 on; which maker and which incumbent is unverified.
- Camtek's Korea revenue fell 69% in 2025 ($117.1M -> $36.9M) while China rose 84%: its 2025 growth did not come from Korean HBM makers. This does not fit a simple "Camtek took HBM share from Onto in 2025" story (inference from 20-F geography; Korea also hosts OSATs and non-HBM customers).
- Onto's "leading 2.5D logic customer" is unnamed; Taiwan = 32% of Onto revenue and Customer A = 20% suggest TSMC, but this is not confirmed.

Gaps: TSMC CoWoS/SoIC TOR by step; SK hynix/Samsung/Micron supplier splits; any outside share data (Yole, TechInsights, TheElec, DigiTimes). [INCOMPLETE]

### 2.2 Market size and other participants

Cited findings:
- Yole: back-end equipment $9.5B in 2026, 6.3% CAGR to 2031; inspection/metrology and hybrid bonding named as key areas (no shares given) - [Silicon Semiconductor, 13 Jul 2026](https://siliconsemiconductor.net/article/124687/AI_reshapes_back-end_equipment)
- Yole Metrology & Inspection Equipment 2026: "record year after almost 16% growth in 2025" (search snippet; page returned 403) - [Yole product page](https://www.yolegroup.com/product/report/metrology--inspection-equipment-2026/)
- QYResearch (low-quality paid aggregator): AP inspection+metrology equipment $925M in 2025, 8.7% CAGR 2026-32; players KLA, Onto, Camtek, Lasertec, Nova, Bruker, Intekplus (snippet only) - [GII listing](https://www.gii.tw/report/qyr2000365-advanced-packaging-inspection-metrology-equipment.html)
- Bloomberg Intelligence: 2.5D/3D packaging 37% CAGR 2025-30 - [CMC Markets, 1 Oct 2026](https://www.cmcmarkets.com/en-au/opto/camt-vs-nvmi-vs-onto-the-chip-packaging-arms-race)
- KLA: 58% of process control in 2025 per Gartner (cited by KLA management, quarter to Mar 2026) - [Finsee KLA review](https://finsee.ai/earnings/klac/2026/q3/en/)
- The Information Network (May 2026) has a table of AP inspection revenue by company and a section "Camtek: Saturation in Packaging Inspection", paywalled - [Castellano Substack, 12 May 2026](https://drrobertcastellano.substack.com/p/semiconductor-metrologyinspection)
- Competitor lists in filings: Onto names KLA and Camtek (AP inspection), KLA and Nova (film/OCD), Nova (integrated metrology), Ushio and Canon (AP lithography), GigaVis (panel inspection), PDF Solutions (software) - [Onto 10-K](https://www.sec.gov/Archives/edgar/data/704532/000119312526066937/onto-20260103.htm). Nova "compete[s] mainly with Onto Innovation Inc., and KLA Corp."; process-tool makers ASML, Lam, Applied (in-situ sensors); local Chinese entrants; via Sentronics "direct competition with companies such as Merck and Camtek" - [Nova 20-F](https://www.sec.gov/Archives/edgar/data/0001109345/000117891326000504/zk2634307.htm). Chroma ATE owns 16.79% of Camtek - [Camtek 20-F](https://www.sec.gov/Archives/edgar/data/0001109138/000117891326001561/zk2634678.htm)

Gaps: one-line evidence for Koh Young, Intekplus, Unity-SC/Merck, Confovis, Nordson, Toray Engineering, Cohu, Cheng Mei and Chinese suppliers was not gathered (out of scope; covered by other researchers). [INCOMPLETE]

---

## 3. Key question: company-specific items

### 3.1 Onto
- Semilab: agreement 30 Jun 2025 ($475M cash + 706,215 shares, four lines); amended after DOJ second request to exclude "a relatively small product line"; final $432.3M cash + 641,771 shares (~ $495M, ~ $50M below original) - [Onto Q3 2025 call](https://www.fool.com/earnings/call-transcripts/2025/11/07/onto-innovation-onto-q3-2025-earnings-transcript/); closed 17 Nov 2025, lines FAaST, CnCV, MBIR (contamination monitoring, materials and surface-charge metrology) - [BusinessWire, 17 Nov 2025](https://www.businesswire.com/news/home/20251117149029/en/Onto-Innovation-Completes-Acquisition-of-Unique-Materials-Composition-and-Electrical-Analysis-Product-Lines-from-Semilab-International); [10-K](https://www.sec.gov/Archives/edgar/data/704532/000119312526066937/onto-20260103.htm). Expected ~ $120M 2026 revenue (company, via search summary of Onto releases; not opened). Third-party estimates: ~ $21M Q3 2026 revenue, H1 run-rate ~ $92M/yr vs $130M original target - [Finsee](https://finsee.ai/earnings/onto/2026/q3/en/); Q3 operating loss $2.8M, 9M $11.8M - [Panabee, AI-generated, flagged](https://www.panabee.com/news/onto-innovation-earnings-q3-2026).
- Rigaku: $1.5B 0% converts due 1 Jun 2031, initial conversion price $381.80 (priced 19 May 2026, upsized) - [Placera/press wire, 19 May 2026](https://www.placera.se/telegram/onto-innovation-onto-innovation-prices-upsized-1-3-billion-convertible-notes-due-2031-20260519); ~ $1.2B net cash for Rigaku, ~ $200M buybacks, capped call raising dilution strike to $509.06; X-ray semiconductor market ~ $1B - [Allmind Q2 2026](https://allmind.ai/earnings/event/2943270)
- OCD and films: Atlas G6 at "several nodes below 2 nm"; multiple Atlas to a major DRAM customer in 2H 2026; Iris G2 qualifications take 6-12 months (CC-U) - [Allmind Q2 2026](https://allmind.ai/earnings/event/2943270)
- Manufacturing/tariffs: >30% of Q3 2025 tool shipments from extended Asian factories; >60% targeted by end-2026; ~1 point GM tariff hit in Q3 2025 - [Q3 2025 call](https://www.fool.com/earnings/call-transcripts/2025/11/07/onto-innovation-onto-q3-2025-earnings-transcript/); Asian factories add capacity roughly equal to US in-house (~ $2B) - [Q2 2026](https://allmind.ai/earnings/event/2943270); contract manufacturers in Japan, Taiwan, Vietnam, Malaysia, Singapore, US - [10-K](https://www.sec.gov/Archives/edgar/data/704532/000119312526066937/onto-20260103.htm)
- Panel and photonics: panel revenue to double in 2026; silicon-photonics orders >$50M, SAM >$500M by 2030 (CC-U) - [Q2 2026](https://allmind.ai/earnings/event/2943270)

### 3.2 Nova
- GAA: cumulative $500M 2024-26 on track; GAA metrology intensity ~30% above FinFET; Nova's share "higher in GAA" (CC-U) - [TradingKey transcript](https://www.tradingkey.com/news/transcripts/262284988-)
- Materials: Metrion (SIMS) in HVM/proliferation/evaluation at 4 of 5 target customers; significant XPS order from a major memory customer; new XPS entrants expected ~2H 2027 (unnamed) (CC-U) - [TradingKey](https://www.tradingkey.com/news/transcripts/262284988-); [MarketBeat](https://www.marketbeat.com/instant-alerts/transcript-nova-q3-earnings-call-highlights-2026-11-06/)
- Chemical: AncoScene accepted and released to HVM at a leading foundry in Q3 2026; KLA named as front-end chemical-metrology rival (CC-U) - [TradingKey](https://www.tradingkey.com/news/transcripts/262284988-)
- AP: WMC tool of record at a leading global foundry after competitive evaluation (2 Jul 2026) - [Nova PR](https://www.novami.com/investors/press-releases/nova-wmc-expanding-adoption-across-the-most-advanced-packaging-processes/); >10 WMC customers (Nov 2026) - [MarketBeat](https://www.marketbeat.com/instant-alerts/transcript-nova-q3-earnings-call-highlights-2026-11-06/)
- Deals: Sentronics, Mannheim, 30 Jan 2025, $60.2M cash; ancosys (Jan 2022); no 2026 acquisition found - [Nova 20-F](https://www.sec.gov/Archives/edgar/data/0001109345/000117891326000504/zk2634307.htm)
- Converts: $750M 0% due 15 Sep 2030, conversion ~ $320.16, capped-call cap ~ $415.03; 2025 notes (conversion ~ $74.60) fully converted in 2025 - [20-F](https://www.sec.gov/Archives/edgar/data/0001109345/000117891326000504/zk2634307.htm)
- ML/software: Nova MARS (physical modelling), Nova FIT (ML for films/CD and for VeraFlex), Nova HPC, Fleet Management; "machine learning and AI capabilities to complement physical modeling"; the 20-F does not describe how reference data for training are obtained (CC-U) - [20-F](https://www.sec.gov/Archives/edgar/data/0001109345/000117891326000504/zk2634307.htm)

### 3.3 Camtek
- Products: Hawk (Feb 2025; chiplets, HBM, hybrid bonding), Eagle G5 (Sep 2024), Eagle-i/AP, MicroProf AP (FRT, bought 1 Nov 2023 for $100M), Golden Eagle (panel); installed base >3,000 (Dec 2025) - [20-F](https://www.sec.gov/Archives/edgar/data/0001109138/000117891326001561/zk2634678.htm); ~4,000 (Nov 2026) - [MarketBeat](https://www.marketbeat.com/instant-alerts/transcript-camtek-q3-earnings-call-highlights-2026-11-04/)
- Converts: $500M 0% due 15 Sep 2030, conversion ~ $109.34; ~ $267.0M used to repurchase ~ $167.1M of 2026 notes (GAAP loss ~ $89M) - [20-F](https://www.sec.gov/Archives/edgar/data/0001109138/000117891326001561/zk2634678.htm); [Q3 2025 call](https://allmind.ai/earnings/event/bt_CAMT_2025_Q3)
- Shareholders (5 Mar 2026): Priortech 20.66%, Chroma ATE 16.79% (joint control, 38.04%), Wasatch 6.80%, Harel 5.3%, Migdal 5.09% - [20-F](https://www.sec.gov/Archives/edgar/data/0001109138/000117891326001561/zk2634678.htm)
- Competition: "does not see smaller Chinese competitors as a significant threat" (CC) - [MarketBeat](https://www.marketbeat.com/instant-alerts/transcript-camtek-q3-earnings-call-highlights-2026-11-04/)

---

## 4. Resilience scenarios to 2030 (inferences from the evidence above)
- Steady growth (compute supply ~2x/yr): all three are capacity-bound rather than demand-bound in 2026-27 (Onto backlog >$1.3B; Camtek "visibility a year ahead" for the first time; Nova supply-chain strain, new Asian clean room). Camtek's single Israeli plant and memory/CPU component shortages are the tightest constraints named.
- Financing-led pause ~2028: exposure ranks by AI-packaging share - Camtek ~80% AP (OSATs >50% of orders), Onto ~50% AP, Nova ~25% of product revenue AP with front-end GAA/DRAM drivers. Camtek's 2027 outlook partly rests on non-binding forecasts (Finsee). Balance sheets: Nova net cash ~ $1B; Camtek net cash ~ $388M; Onto net debt ~ $222M offset by a ~ $679M listed Rigaku stake.
- Acceleration: Onto doubled manufacturing capacity via Asia contract factories; Nova and Camtek expanding; Camtek hybrid bonding meaningful only from 2028.
- Export controls: China = Camtek 49%, Nova 33%, Onto 7% (FY2025). BIS Affiliates Rule suspension end date 9 Nov 2026 and China's Ga/Ge ban suspension to 27 Nov 2026 (both per Nova 20-F) are live items; current status not verified. [INCOMPLETE]

---

## 5. Entry-point data (separate from quality)

- ONTO (11 Nov 2026 close $215.06, +8.9% on the day): market cap $10.56B, EV $10.78B, trailing P/E 70.6, forward P/E 17.9 (NTM), EV/Sales 8.2, EV/EBITDA 27.3, EV/FCF 43.5, beta 1.68, 52-week +52%; consensus (12 analysts) FY2026 revenue $1.49B (+48%), FY2027 $2.02B (+36%), EPS $8.48 / $12.86; mean target $336 - [stockanalysis statistics](https://stockanalysis.com/stocks/onto/statistics/), [forecast](https://stockanalysis.com/stocks/onto/forecast/). FY2021-25 forward P/E 22.6, 15.5, 34.4, 27.4, 30.1; P/E 15.1-61.9; EV/EBITDA 9.4-35.6 - [ratios](https://stockanalysis.com/stocks/onto/financials/ratios/). Market cap ~ $15.14B on 11 Aug 2026 (search snippet) - [247WallSt](https://247wallst.com/investing/2026/08/11/onto-innovation-jumps-6-tuesday-following-camtek-earnings-and-nvidias-500-billion-partnership/).
- NVMI ($340.62, +4.6%): market cap $10.83B, EV $9.84B, trailing P/E 39.0, forward 25.7, EV/Sales 9.8, EV/EBITDA 30.2, beta 1.88, 52-week +7%; consensus (8) FY2026 $1.08B (+22%), FY2027 $1.36B (+26%), EPS $10.67 / $13.66; mean target $406 - [statistics](https://stockanalysis.com/stocks/nvmi/statistics/), [forecast](https://stockanalysis.com/stocks/nvmi/forecast/). FY2021-25 forward P/E 34.1, 18.7, 27.1, 26.2, 36.4; EV/EBITDA 12.7-33.6 - [ratios](https://stockanalysis.com/stocks/nvmi/financials/ratios/). ATH $615.99 (15 Jun 2026); $385.12 on 29 Sep 2026 - [CMC](https://www.cmcmarkets.com/en-au/opto/camt-vs-nvmi-vs-onto-the-chip-packaging-arms-race). A report that shares fell 5.7% to $277.80 after Q3 results conflicts with later prices (could not verify) - [Webull](https://www.webull.com/news/15871592738612224).
- CAMT ($107.05, +4.8%): market cap $5.00B, EV $4.61B, trailing P/E 40.4, forward 21.6, EV/Sales 8.5, EV/EBITDA 31.8, beta 1.73, 52-week -4%, shares +3.9% YoY; consensus (11) FY2026 $596M (+20%), FY2027 $804M (+35%), EPS $3.60 / $5.13; mean target $153 (one Strong Sell) - [statistics](https://stockanalysis.com/stocks/camt/statistics/), [forecast](https://stockanalysis.com/stocks/camt/forecast/). FY2021-25 forward P/E 27.3, 13.1, 31.0, 26.2, 33.6; EV/EBITDA 9.1-40.0 - [ratios](https://stockanalysis.com/stocks/camt/financials/ratios/). ATH $210.20 (24 Apr 2026); +43.7% YTD at 29 Sep 2026 - [CMC](https://www.cmcmarkets.com/en-au/opto/camt-vs-nvmi-vs-onto-the-chip-packaging-arms-race).
- Cycle position: all three at record revenue and record backlog/orders; consensus 2027 growth 26-36%; WFE +12% 2026 (Gartner via Nova 20-F); SEMI equipment record $145B 2026 (via Camtek 20-F).
- Near-term events: Nova Investor Day 9 Mar 2027 (NYC) and $200M buyback (from 2 Sep 2026) - [Nova PR index](https://www.novami.com/investors/press-releases/), [buyback PR](https://www.novami.com/investors/press-releases/nova-announces-200m-share-repurchase-program/); Q4 2026 results for all three ~Feb 2027 (dates not yet found); Onto Rigaku mark-to-market each quarter; Camtek software launch Q1 2027 and Q4 GM test (needs ~52.5%); Nova XPS competition 2H 2027.
- Inference: all three trade near the top of their FY2021-25 EV/Sales and EV/EBITDA ranges on trailing data, but at or below their own 5-year average forward P/E on consensus that assumes 2027 growth of 26-36%; the October-November 2026 sell-off (Onto ~ -30% from August, Camtek ~ -49% from April high, Nova ~ -45% from June high) happened while estimates rose - the cause was not verified.

---

## 6. Could not verify
- Third-party (Yole/TechInsights/Gartner/broker) market shares in AP inspection, OCD, XPS, or HBM/CoWoS steps.
- Named TOR holders by step at TSMC CoWoS/SoIC, SK hynix, Samsung, Micron; whether Onto's displaced HBM incumbent was Camtek.
- Outside confirmation of the 2024-25 Onto-to-Camtek share shift.
- How Nova (or Onto) obtains reference TEM/cross-section data to train models; any published measurement uncertainty.
- Software revenue for any of the three; Camtek product vs service split in filings.
- Onto 2026 China share and named 10% customers; Camtek 2026 China share (a third party says ~45% plan).
- Status of BIS Affiliates Rule after 9 Nov 2026.
- Korean, Taiwanese and Israeli local-language press (TheElec, DigiTimes, Globes, Calcalist) and TASE filings were not consulted: coverage is thin there.

## 7. Sources (date of document; all accessed 12 Nov 2026)
Listed inline above. Primary: Onto 8-K Ex.99.1 (9 Nov 2026), 10-Q (9 Nov 2026), 10-K FY2025; Nova 6-K (5 Nov 2026), 20-F FY2025 (Feb 2026); Camtek 6-K (4 Nov 2026), 20-F FY2025, releases 10 Feb, 18 Feb, 13 Apr, 2 Jun, 14 Oct 2026. Call summaries: MarketBeat (4, 6, 9 Nov 2026), TradingKey (Nov 2026), Allmind (Nov 2025, Aug 2026), Motley Fool (7 Nov 2025). Third-party: Finsee (Nov 2026), CMC Markets (1 Oct 2026), Silicon Semiconductor/Yole (13 Jul 2026), stockanalysis.com (12 Nov 2026).
