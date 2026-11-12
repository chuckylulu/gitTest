# Chip-equipment cycle, AI-capex scenarios and export controls: cross-cutting notes for measurement, inspection and test suppliers

**Research date: 12 November 2026.** Status: v1, saved after a research interruption. Sections marked INCOMPLETE were still being filled when this version was saved.

Provenance tags: **[P]** = primary document read (filing, Federal Register text, company release); **[R]** = news report or reprint read; **[S]** = search-result snippet/summary only, page not read in full (lower confidence). Forecasts carry their publication date. semi.org, Applied Materials' and KLA's IR pages and most transcript sites refused automated reading, so several primary figures come via reprints.

---

## 1. One-page summary

**Cycle position (Nov 2026): strong upcycle, still accelerating, supply-constrained, no sign yet of a turn in orders.**
- WFE (wafer-fab equipment) 2025 actual: record **$116.9B** (SEMI, 15 Jul 2026). 2026: SEMI mid-year forecast **$143.9B (+23.1%)**. The equipment makers are higher: in late October 2026 KLA and Lam both put CY2026 at the **"mid-$150B" range** (KLA includes advanced packaging). 2027: KLA and Lam say **>$200B (~+30%)**, against SEMI's July path of about $175B (+21.8%). 2028: SEMI about $200B (+14.1%). Definitions differ between sources, so the gap is not exact.
- SEMI's 300mm Fab Outlook (14-15 Oct 2026) puts 2026 300mm fab equipment at **$149B (+31%)**, with double-digit growth every year to **$227B in 2029**. The October 2025 edition had $116B for 2026, so the 2026 figure has been raised about 28% in a year.
- Mix is shifting to memory. Memory was **46%** of Lam's equipment revenue in the September 2026 quarter (34% a year earlier). KLA models memory at about 40% of process-control systems in the December 2026 quarter. SEMI forecasts DRAM equipment **+39%** in 2026.
- Back end: SEMI forecasts test equipment at **$15.3B in 2026 (+31%)** after +55.3% in 2025, and assembly/packaging equipment at **$6.7B (+9.6%)**. Advantest raised its FY2026 guidance again on 28 Oct 2026, and Teradyne's Q3 2026 revenue was up 70% year on year.
- Supply is the constraint, not demand. ASML says its planned 2027 and 2028 supply "will not fully meet" demand, and some customers want 2029-2030 slots. Lam cites cleanroom space and component supply. SK hynix says DRAM and HBM are effectively sold out through 2029.

**Scenario tracking (priors: steady 55% / financing-led pause around 2028 25% / acceleration 20%)**
- *Acceleration:* the 2026-27 data run above a "steady" path. Evidence: four straight WFE raises at KLA, about 30% growth in both 2026 and 2027, sold-out memory, ASML orders reaching 2029-30, and SK hynix projecting cloud-provider capex up at least 60% in 2027.
- *Financing-led pause:* the evidence is building in **how capex is funded**, not yet in equipment orders.
  - Alphabet sold about $12.4B of stock through at-the-market programmes, issued $28.7B of notes, bought back no stock and had negative free cash flow in Q3 2026.
  - Meta launched an equity raise on 26 Oct 2026 and plans an at-the-market programme of about $60B from 19 Jan 2027.
  - Amazon's trailing-twelve-month free cash flow was -$42.4B.
  - Microsoft has $364.6B of datacentre leases that have not yet started, guides CY2026 capex at about $170B, and reports delays in third-party capacity.
  - Oracle plans capex of up to $95B in FY27 and is raising about $40B of debt and equity.
  - S&P (Sept 2026) says hyperscaler credit quality is "gradually weakening".
  - I found no WFE order cancellations, only minor push-outs (for example Bruker's $20M of semiconductor revenue moved into Q4 2026).
- *Steady:* still the central case for the averages, but the timing is front-loaded.
- *Net inference (mine, not sourced):* move probability from "steady" toward "acceleration" for 2026-27, and do **not** lower the 2028 financing-pause weight, because funding is shifting to equity, leases and off-balance-sheet vehicles. Add **cleanroom and tool supply** to the 2026-2028 binding constraints, alongside memory, power and financing.

**Export-control status (12 Nov 2026)**
- US "Affiliates" 50% rule (interim final rule, 30 Sep 2025): stayed for one year from 10 Nov 2025. On 9 Nov 2026 the stay was **extended to 10 Jan 2027** (Federal Register doc 2026-22793). No decision has been published on what happens after that date.
- Entity List: BIS made no additions from Oct 2025 to June 2026. In June 2026 Reuters reported that 75+ chip, chip-equipment and AI entities (including CXMT) had been cleared for listing but were held back.
- On 15 Jan 2026 BIS moved some §744.23 end-use licence reviews to case-by-case. On 11 Feb 2026 Applied Materials paid a **$252.5M** BIS settlement.
- The MATCH Act (H.R. 8170 / S. 4281) would extend controls to servicing, parts and DUV. It passed the House Foreign Affairs Committee on 22 Apr 2026; I could not verify any floor action as of November.
- The Netherlands has required a national licence for certain measurement and inspection equipment since 1 Apr 2025.
- Section 232 tariffs: a 25% tariff on a narrow set of advanced chips has applied since 15 Jan 2026. Chip-making equipment is **not** tariffed in Phase 1, and I could not verify the Phase 2 status.
- China: it extended the rare-earth suspension to **10 Jan 2027** on 9 Nov 2026, while the April 2025 controls stay in force. Reuters (Dec 2025) reported an unpublished rule that new capacity must use at least 50% domestic equipment. The gallium/germanium ban was suspended **until 27 Nov 2026**.

**Events in the next six months (to May 2027)**
- Mid-Nov 2026: Trump-Xi meeting at APEC in Shenzhen.
- Mid/late Nov 2026: Applied Materials FQ4 results (exact date not verified).
- 27 Nov 2026: expiry of the gallium/germanium suspension (check whether it was extended).
- Early Dec 2026: SEMI Q3 billings.
- Mid-Dec 2026: SEMI year-end equipment forecast (last year's came on 16 Dec 2025).
- **10 Jan 2027: the Affiliates Rule stay, China's rare-earth suspension and the tariff truce all lapse unless extended.**
- Mid-Jan 2027: TSMC gives its 2027 capex guidance. Brokers expect $83-90B, against $60-64B for 2026.
- Late Jan to early Feb 2027: ASML, Lam and KLA December-quarter results, and hyperscalers' 2027 capex guidance.
- 19 Jan 2027: Meta's planned at-the-market programme can begin.
- H1 2027, timing unknown: the pending Entity List package (CXMT and others), the MATCH Act, Section 232 Phase 2, and SEMI's 2026 actuals (usually April).

---

## 2. Exposure table

China share = the latest disclosed share of company revenue. "Lost to controls" = revenue a company has disclosed as lost or deferred because of export rules. The last two columns are **my inferences** from the sourced facts, not company statements.

| Company | Latest China share of revenue (date, source) | Disclosed revenue lost to controls | Main end-market exposure (sourced where cited) | AI-pause exposure (inference) | Export-control exposure (inference) |
|---|---|---|---|---|---|
| KLA | **34%** of Sep-Q 2026 revenue; expects "high-20s" % for CY2026 and a lower share in the Dec quarter ([securities.io, 28 Oct 2026](https://www.securities.io/kla-posts-fiscal-q1-revenue-of-4-14-billion-above-guidance-midpoint/)) [R]. 24% in Mar-Q 2026 ([Handsoff, 31 May 2026](https://handsoff.substack.com/p/kla-beat-across-the-board-process)) [R]. "Low-20s" expected for 2027 ([Earnings Whispers, 28 Oct 2026](https://www.earningswhispers.com/article/KLAC/r679), paraphrase) [R] | None quantified found | Sep-Q process-control systems about 72% foundry/logic and 28% memory; Dec-Q model 60/40, with memory 84% DRAM; advanced-packaging (AP) process control about **$1.1B in CY2026 (>+70%)** ([securities.io](https://www.securities.io/kla-posts-fiscal-q1-revenue-of-4-14-billion-above-guidance-midpoint/)) [R] | Medium. Broad base plus services. Contract liabilities $1.71B at 30 Sep 2026 ([10-Q](https://www.sec.gov/Archives/edgar/data/319201/000031920126000034/klac-20260930.htm)) [P] | High. China a third of the latest quarter |
| Applied Materials | About **28%** of FQ3 2026 revenue (Jul-Q; $2.51B) vs about 35% a year earlier; 37% in FY2024 ([sec-api.io, 12 Oct 2026](https://sec-api.io/insights/applied-materials-amat-financial-analysis-q3-fy2026-china-revenue-share-export-control-settlement-wafer-equipment-peers-and-scenarios-to-fy2029)) [R] | About $110M not shipped in FQ4 2025 because of the Affiliates Rule. About $600M FY2026 hit expected, reported as reversed by the suspension ([Yahoo/Reuters, Nov 2025](https://finance.yahoo.com/news/applied-materials-shares-drop-stringent-111350305.html)) [S]. $252.5M BIS penalty paid 11 Feb 2026 [R] | Broad front end, including process diagnostics and control (e-beam). Foundry-logic, DRAM and AP said to be about 80% of WFE growth in 2026-27 ([Statementdog](https://statementdog.com/analysis/AMAT/earnings_calls/318002)) [S] | Medium | High |
| ASML | **23%** of Q3 2026 system sales (14% Q2, 19% Q1); about 20% for FY2026 ([AI Weekly citing SCMP, 15 Oct 2026](https://aiweekly.co/alerts/asml-q3-china-equipment-sales-soar-109-qoq-to-23-of-system-shipments-as-memory); [TrendForce, 22 Jun 2026](https://www.trendforce.com/news/2026/06/22/news-top-five-japanese-chip-toolmakers-reportedly-see-10-china-sales-drop-in-fy25-led-by-front-end-weakness/)) [R]. About 33% in 2025 ([TrendForce DataTrack, 22 Jul 2026](https://datatrack.trendforce.com/blog/content/61356/u-s-seeks-to-extend-chip-equipment-controls-to-maintenance-as-u-s-japanese-and-dutch-equipment-suppliers-reassess-china-exposure)) [R] | Up to $8B of China revenue at risk under the MATCH Act (Capstone estimate, [27 Apr 2026](https://capstonedc.com/insights/the-us-unprecedented-threat-to-foreign-semiconductor-firms/)) [R]. No realised loss disclosed in what I read | Lithography (EUV/DUV) plus metrology/inspection (YieldStar, HMI e-beam). Supply sold out for 2027-28 ([ASML Q3 release via StorageNewsletter](https://www.storagenewsletter.com/?p=306155)) [R] | Low-medium near term; backlog and supply limits cushion | High (MATCH Act, Dutch licensing) |
| Hitachi High-Tech | Could not verify | Could not verify | CD-SEM / metrology SEM, about 70% CD-SEM share ([Business Journal](https://biz-journal.jp/tag/%e6%97%a5%e7%ab%8b%e3%83%8f%e3%82%a4%e3%83%86%e3%82%af)) [S]. Exposed to leading-edge logic and DRAM (inference) | Medium | Medium (Japan list controls) |
| Lasertec | Could not verify | Could not verify | EUV mask and blank inspection. FY6/2026 sales ¥230.5B (-8.3%), orders ¥237.5B, backlog a record **¥322.9B** ([Gyokai Digest](https://www.gyokaidigest.com/en/companies/lasertec/report/2026-FY)) [S] | Medium-high (concentrated on EUV); backlog cushions | Low-medium. Inference: EUV tools cannot ship to China, which limits China revenue |
| Advantest | About 20-25% ("quite healthy", CEO, Jan 2026 call; [RCR Wireless, 30 Jan 2026](https://www.rcrwireless.com/20260130/test-measurement/advantest-rises-with-the-ai-tide)) [S] | None found | SoC testers for AI accelerators (66% SoC-tester share in 2025, per [FourWeekMBA](https://fourweekmba.com/ai-advantest-raises-profit-forecast-14-after-a-record-quarter/) [S]) and memory/HBM testers ([H1 FY2026 tanshin, 28 Oct 2026](https://www.advantest.com/en/news/2026/mpd9kn0000000gii-att/E_FR_FY2026_2Q.pdf)) [P] | High | Medium |
| Teradyne | Could not verify (the 10-Q text I could read had no geographic split) | None found | Compute (AI) and memory test. Memory test revenue a record **$301M** in Q3 2026 ([Zacks](https://www.zacks.com/stock/news/3018941/teradyne-q3-earnings-call-highlights-ai-demand-and-2027-growth-plans)) [S] | High | Medium |
| Onto Innovation | Could not verify (not in the release; the 10-Q text I could read was truncated) | None found | AP inspection (Dragonfly G5, Firefly) and advanced-node optical CD (Atlas G6). Backlog >$1.3B ([8-K, 9 Nov 2026](https://www.sec.gov/Archives/edgar/data/0000704532/000119312526453582/onto-ex99_1.htm)) [P] | High (AP) | Medium |
| Nova | About 30% "in prior periods" ([finsee](https://finsee.ai/earnings/nvmi/2026/q3/en/)) [S]. Not verified | None | Q3 2026 product revenue **61% logic/foundry, 39% memory**; record AP and DRAM ([MarketBeat, 6 Nov 2026](https://www.marketbeat.com/instant-alerts/transcript-nova-q3-earnings-call-highlights-2026-11-06/)) [R] | Medium-high | Medium-high (US subsidiary needs licences for listed Chinese customers, per [20-F](https://www.sec.gov/Archives/edgar/data/1109345/000117891326000504/zk2634307.htm)) [P] |
| Camtek | **49% of 2025 revenue**; Asia-Pacific 91% ([20-F, 19 Mar 2026](https://www.sec.gov/Archives/edgar/data/1109138/000117891326001561/zk2634678.htm)) [P] | None disclosed | About **80% advanced packaging** in Q3 2026, mostly AI ([MarketBeat, 4 Nov 2026](https://www.marketbeat.com/instant-alerts/transcript-camtek-q3-earnings-call-highlights-2026-11-04/)) [R] | High | High (China half of revenue) |
| Bruker | Share not found. China revenue rose by low double digits in Q3 2026 after falling more than 20% in Q1 ([MarketBeat, 4 Nov 2026](https://www.marketbeat.com/instant-alerts/transcript-bruker-q3-earnings-call-highlights-2026-11-04/)) [S] | None | Semiconductor metrology is a small part of the group. Semiconductor revenue fell by double digits in Q3 on a **$20M push-out**; semiconductor-metrology bookings up >30% year to date [S] | Low at group level | Low-medium |
| Rigaku | About 13% in FY2025 (¥12.5B of ¥94.1B), down from about 17% ([envalith segments](https://envalith.com/en/companies/268A/segments)) [S] | None | X-ray semiconductor process control; memory demand strong ([Quartr](https://quartr.com/events/rigaku-holdings-corporation-268a-q3-2025_FYcgoW2w)) [S] | Medium | Low-medium |
| JEOL | Could not verify | Q1 revenue fall attributed partly to "delays in export-control renewal procedures for China" ([Quartr](https://quartr.com/events/jeol-ltd-6951-q2-2026_FsIayRbL)) [S]. Quarter labels inconsistent | Mask writers (single-beam doing well, multi-beam delayed) plus scientific instruments [S] | Low-medium | Medium (licence timing) |
| FormFactor | Could not verify. An aggregator gives Q1 2026 China revenue of $11.36M ([opencapital](https://www.opencapital.sh/stocks/form/metrics/form_segment_china_revenues)) [S] | Export controls limited DRAM probe-card shipments to China in Q3 2025 ([fintool](https://fintool.com/app/research/companies/FORM/earnings/Q3%202025)) [S] | SK hynix **20.7%** and TSMC 12.8% of Q3 2026 revenue ([10-Q](https://www.sec.gov/Archives/edgar/data/1039399/000103939926000043/form-20260926.htm)) [P]. HBM/DRAM, foundry/logic, co-packaged-optics systems ([release](https://finviz.com/news/410470/formfactor-inc-reports-2026-third-quarter-results)) [S] | High | Medium |
| Technoprobe | Could not verify | None found | Probe cards; about 38% of 2025 revenue AI-related ([Quartr](https://quartr.com/events/technoprobe-s-p-a-tpro-q3-2025_FGoKyd2b)) [S] | Medium-high | Could not verify |
| Park Systems | China and Taiwan together 41% of 2025 revenue ([Quartr Q4 2025](https://quartr.com/events/park-systems-corp-140860-q4-2025_FYdERgHw)) [S] | None | AFM; industrial equipment 65% of H1 2026 revenue ([Quartr Q2 2026](https://quartr.com/events/park-systems-corp-140860-q2-2026_FYdETtU3)) [S] | Low-medium | Medium |
| PDF Solutions | **16%** of Q3 2026 revenue ($11.1M; 10% a year earlier); 15% of 9M 2026 ([10-Q, 5 Nov 2026](https://www.sec.gov/Archives/edgar/data/1120914/000143774926035296/pdfs20260930_10q.htm)) [P] | None | Yield-analytics software and e-beam probe; US 33%, Japan 32% of Q3 [P] | Low-medium | Medium |

---

## 3. Supporting detail

### 3.1 WFE spending: actuals, forecasts, mix, process control, test and packaging equipment

**Takeaway:** 2025 WFE was a record $116.9B. 2026 is tracking at roughly $144-155B depending on source and definition, and the companies' first views of 2027 (>$200B) sit well above SEMI's July 2026 path. Test equipment is growing faster than WFE in 2025-26; assembly/packaging equipment is growing slower (SEMI), although AP *inspection* is growing much faster (KLA, Camtek, Onto).

**Cited findings**
- **SEMI mid-year forecast** (published 15 Jul 2026; [SEMI](https://www.semi.org/en/semi-press-release/global-semiconductor-equipment-sales-forecast-to-reach-a-record-229-billion-dollars-in-2028-semi-reports), read via [I-Connect007 reprint](https://iconnect007.com/article/150797/global-semiconductor-equipment-sales-forecast-to-reach-a-record-229-billion-in-2028/150794/ein)) [R]
  - Total equipment: $165.9B in 2026 (+23.2%), $229.5B in 2028.
  - WFE: $116.9B in 2025, $143.9B in 2026 (+23.1%), +21.8% in 2027, +14.1% in 2028 to about $200B.
  - Foundry/logic: $78.0B in 2026 (+18.9%), +18.1% in 2027, $104.7B in 2028.
  - DRAM: $38.8B in 2026 (+39.0%), +27.4% in 2027, $56.9B in 2028.
  - NAND: $13.9B in 2026 (+30.7%), +31.1% in 2027, $20.8B in 2028.
  - Test: +55.3% in 2025, $15.3B in 2026 (+31.0%), $20.8B in 2028.
  - Assembly and packaging: +20.8% in 2025, $6.7B in 2026 (+9.6%), $8.6B in 2028.
  - China, Taiwan and Korea remain the top three regions through 2028; China's growth "is expected to moderate in 2026".
  - Implied values (my arithmetic from SEMI's growth rates): 2027 WFE about $175B, test about $11.7B in 2025, assembly/packaging about $6.1B in 2025.
- **SEMI December 2025 year-end forecast** (16 Dec 2025): headline "Global Semiconductor Equipment Sales Projected to Reach a Record of $156 Billion in 2027" ([PR Newswire](https://tools.prnewswire.com/en-us/live/20813/release/20251216EN45080)) [S]. The July 2026 forecast already has 2026 at $165.9B, so 2026-27 has been revised up sharply within seven months.
- **SEMI 300mm Fab Outlook** (14-15 Oct 2026; [Evertiq, 15 Oct 2026](https://evertiq.com/news/2026-10-15-300mm-fab-equipment-spending-set-to-reach-227-billion-by-2029); [The Star, 14 Oct 2026](https://www.thestar.com.my/business/business-news/2026/10/14/global-300mm-fab-equipment-spending-to-hit-us227bil-by-2029-says-semi)) [R]
  - 300mm front-end equipment +31% to $149B in 2026, double-digit growth every year, $227B in 2029.
  - 300mm construction spending $47.5B in 2026 (+23%), $63.3B in 2027 (+33%), $68.4B in 2028.
  - Americas equipment $18.1B in 2026 rising to $40.6B in 2029.
  - The prior edition (Oct 2025) had 2026 $116B, 2027 $120B, 2028 $138B ($374B over three years) ([SEMI, Oct 2025](https://www.semi.org/en/semi-press-release/semi-reports-global-300mm-fab-equipment-spending-expected-to-total-374-billion-dollars-over-next-three-years)) [S].
- **SEMI billings, Q2 2026** (4 Sep 2026): global $40.53B (+23% YoY, +11% QoQ), a second straight record quarter. By region: China $11.91B (+5% YoY), Taiwan $10.89B (+24%), Korea $9.08B (+54%), Europe +70%, rest of world +69% ([SEMI](https://www.semi.org/en/semi-press-release/global-semiconductor-equipment-billings-increased-23-percent-year-over-year-in-q2-2026-semi-reports); [The Star, 4 Sep 2026](https://www.thestar.com.my/business/business-news/2026/09/04/global-semiconductor-equipment-billings-jump-23-in-2q26-on-ai-demand)) [S]. That puts China at about 29% of Q2 billings (my arithmetic).
- **KLA** (FQ1 FY27, quarter ended 30 Sep 2026, reported 28 Oct 2026)
  - Revenue $4.14B; December-quarter guidance $4.7B ±$0.2B.
  - CY2026 WFE including advanced packaging raised to "the mid-$150 billion range"; CY2027 expected to exceed $200B ([securities.io](https://www.securities.io/kla-posts-fiscal-q1-revenue-of-4-14-billion-above-guidance-midpoint/)) [R].
  - [Earnings Whispers](https://www.earningswhispers.com/article/KLAC/r679) [R] describes this as the fourth straight raise and calls the 2027 framework "WFE above $200 billion, growth of roughly 30% or more". It also says memory is about 60% of 2027 WFE; this looks garbled (it may refer to share of *growth*) and is not verified.
  - In April 2026 KLA had CY2026 at "over $140B", up from "$130B+" ([Handsoff](https://handsoff.substack.com/p/kla-beat-across-the-board-process)) [R].
- **Lam Research**
  - 10-Q for the quarter ended 27 Sep 2026 (filed 22 Oct 2026) [P]: revenue $8.219B. By region: China 35% ($2.886B; 43% a year earlier), Korea 20%, Taiwan 18%, Japan 9%, US 8%, Southeast Asia 6%, Europe 4%. Equipment mix: memory 46% (34%), foundry 46% (60%), logic/IDM 8% (6%) ([10-Q](https://www.sec.gov/Archives/edgar/data/707549/000070754926000054/lrcx-20260927.htm)).
  - Call (21 Oct 2026): CY2026 WFE in the mid-$150B range. Preliminary 2027 view above $200B, led by DRAM, then leading-edge foundry/logic, then NAND. Cleanroom space and some components limit how much of 2027 demand the industry can meet ([Benzinga transcript](https://www.benzinga.com/node/62514820); [Bullfincher](https://bullfincher.io/companies/lam-research-corporation/earnings-call/fy2027-q1)) [S].
  - In July 2026 Lam raised its 2026 view to the low-$150B range from $140B ([Briefing.com, 30 Jul 2026](https://www.briefing.com/story-stocks/archive/2026/7/30/lam-research-surges-as-sepq-guide-and-2027-demand-outlook-reinforce-ai-equipment-cycle-(lrcx))) [S].
- **ASML** (Q3 2026, mid-Oct 2026; [StorageNewsletter repost of release, 27 Oct 2026](https://www.storagenewsletter.com/?p=306155)) [R]
  - Results: net sales €11.7B (+55% YoY); Q4 guidance €14.2-15.2B; FY2026 €44-45B; installed-base management €3.3B.
  - Demand: "Our customers continue to increase their short- and medium-term equipment demand forecasts... driven primarily by their views on the size and duration of AI-related investments." "Some customers are expressing an interest in placing orders with us for 2029 and even 2030." "Our supply as currently planned for both 2027 and 2028 will not fully meet the demand of our customers."
  - Capacity: low-NA EUV and DUV immersion capacity +30% in 2027; looking at more than +30% for 2028.
  - The release gives no bookings figure.
- **Tokyo Electron**
  - 30 Oct 2026: H1 FY3/2027 revenue ¥1.67T (+41.3%); first full-year FY3/2027 forecast of revenue ¥3.7T and operating profit ¥1.169T; buyback of up to ¥150B ([Tiger/itiger, 30 Oct 2026](https://www.itiger.com/news/1157765943)) [R].
  - 30 Apr 2026 briefing: CY2026-27 WFE $150-170B a year (>+20% vs CY2025), leading-edge >+30%. DRAM+NAND rising from 35% to 40% of WFE in CY2026. China's share of WFE falling from the upper-30s % (CY2025) to the mid-30s % (CY2026) ([Envalith, 30 Apr 2026](https://envalith.com/en/companies/8035/reports/019dde03-c63a-77c7-a8e9-f02d1a486536)) [R].
  - I did not obtain the October 2026 WFE update.
- **Applied Materials** (FQ3 2026, quarter ended 26 Jul 2026, reported 13 Aug 2026): record revenue $9.12B (+25%); FQ4 guidance $10.25B ±$0.5B ([247 Wall St](https://247wallst.com/cards/applied-materials-q3-2026-earnings-amat-01kzybvthd5qqamwrtqk59k25x); [sec-api.io](https://sec-api.io/insights/applied-materials-amat-financial-analysis-q3-fy2026-china-revenue-share-export-control-settlement-wafer-equipment-peers-and-scenarios-to-fy2029)) [R]. FQ4 FY2026 results were not yet out on 12 Nov 2026.
- **Process-control intensity** (company/broker claims via a newsletter, [Handsoff, May 2026](https://handsoff.substack.com/p/kla-beat-across-the-board-process)) [R]: gate-all-around needs an estimated 40-50% more process-control steps than FinFET; DRAM 1c/1d needs 35-45% more; HBM4 needs 2-3x the inspection intensity of standard DRAM. The same page gives inconsistent KLA share figures (22.9% vs 58%), so do not use its share numbers.
- **Test-equipment share of semiconductor capex:** rose from 6.4% in 2025 to 8.1% in the first eight months of 2026 (Teradyne Q3 2026 call, via [Zacks](https://www.zacks.com/stock/news/3018941/teradyne-q3-earnings-call-highlights-ai-demand-and-2027-growth-plans)) [S].
- **Advantest** (28 Oct 2026; [tanshin](https://www.advantest.com/en/news/2026/mpd9kn0000000gii-att/E_FR_FY2026_2Q.pdf)) [P]
  - H1 FY2026 net sales ¥845.2B (+60.5%); operating income ¥456.8B (+96.5%).
  - Full-year forecast raised to sales ¥1,863.0B (from ¥1,714.0B) and operating income ¥967.0B (from ¥846.0B).
  - Expects the tester market to "reach a new record high in CY2026".
  - Secondary report: SoC tester market near the top of its range (about $11.5B) and the memory tester market around the midpoint; strength expected to continue into CY2027 ([FourWeekMBA](https://fourweekmba.com/ai-advantest-raises-profit-forecast-14-after-a-record-quarter/)) [S].

**Inferences**
- WFE growth of about 30% in both 2026 and 2027, set against SEMI's July 2026 path of +23% and +22%, is the clearest sign the cycle is running hotter than the "steady" prior. Part of the gap is definitional: KLA counts advanced packaging, and SEMI's WFE includes fab facilities and masks.
- Process control and AP inspection are gaining share within WFE. The evidence is KLA's AP growth of more than 70%, Camtek's 80% AP mix, Onto's 88% revenue growth, and the intensity claims above. I have no time series of process control's share of WFE (see Gaps).

**Gaps**
- The 2024 WFE actual and TechInsights and Gartner figures were not retrieved. **INCOMPLETE.**
- No sourced time series for process control as a share of WFE. **INCOMPLETE.**
- Applied Materials' and Tokyo Electron's October/November 2026 WFE views were not obtained.

### 3.2 Demand drivers

**Takeaway:** Every large buyer's capex guidance points up into 2027: TSMC, the memory makers, the hyperscalers and Oracle. The constraints are cleanroom timing, tool supply and financing structure, not stated demand.

**Cited findings**
- **TSMC** (15 Oct 2026)
  - 2026 capex unchanged at $60-64B. CFO: "TSMC will spend more on capex from 2026 to 2028 than in the previous three years." It will "ensure sufficient CoWoS capacity to meet [customers'] demand" ([Focus Taiwan, 15 Oct 2026](https://focustaiwan.tw/business/202610150018)) [R].
  - 2nm was 8% of Q3 revenue (3% in Q2). 2026 revenue-growth outlook raised to about 44%. "Tool inflation is real." N2 capacity to more than double in 2027 (brokers citing management).
  - Broker 2027 capex forecasts: UBS $90B (+45%, then $105B in 2028), Morgan Stanley $83B ($92B in 2028; expects 2027 EUV bookings to double), Goldman Sachs and BofA $85B.
  - Goldman CoWoS estimates: 1.275M wafers in 2026, 2.73M in 2027 (+114%), 3.48M in 2028 ([TrendForce, 16 Oct 2026](https://www.trendforce.com/news/2026/10/16/news-after-tsmcs-3q26-earnings-key-brokerage-takeaways-as-2028-capex-forecasts-reach-us105b/)) [R].
  - Press report: CoWoS about 130k wafers/month at end-2026, doubling to about 260k by end-2028 ([TrendForce, 14 Sep 2026](https://www.trendforce.com/news/2026/09/14/news-tsmc-reportedly-targets-22-2nm-16-3nm-capacity-boost-by-mid-2027-cowos-to-double-by-2028/)) [S]. These are broker and press estimates, not company guidance.
- **SK hynix** (28 Oct 2026) [R]
  - Q3 revenue ₩104.6T, operating profit ₩83.3T ([TechNews, 28 Oct 2026](https://finance.technews.tw/2026/10/28/sk-hynixs-third-quarter-revenue-hit-a-record-high-of-over-100-trillion-won/)).
  - No 2026 or 2027 capex amount disclosed; 2027 capex "to increase significantly". M15X to be at maximum capacity by end-2026. Building shells for Yongin and M17 pulled forward, with cleanrooms opened in phases.
  - HBM4 to pass HBM3E in Q4. Long-term agreements with 14 customers cover at least 50% of 2027-28 capacity. DRAM and HBM "effectively sold out through 2029". Supply constraints through 2030.
  - 2027 demand growth: DRAM mid-20s %, NAND high-teens %. Global cloud-provider capex projected up at least 60% in 2027.
  - "customers are adjusting pace to verify business viability and timing rather than halting demand" ([StockHub call summary](https://stockhub.kr/en/insights/view_1793152574975_d6cb11f87d-20261028-000660-cy26q3-earnings-call)).
  - One outlet reported 2026 capex in the "high-40 trillion won" range; this conflicts with the statement that no figure was disclosed. Not verified.
- **Samsung** (29 Oct 2026)
  - Q3 revenue ₩195.3T, operating profit ₩107.4T (₩106.5T from the chip division).
  - Capex ₩57T in the first nine months (+77%); full year about **₩84.4T (+60%)**.
  - 2027 AI capex expected at a "historic level". HBM supply for 2027 fully sold; HBM4 is 60% of HBM sales. Supply tightness could last into 2028. Foundry has 2nm HPC wins ([Light Reading](https://lightreading.com/finance/memory-boom-carries-samsung-to-another-bumper-quarter); [Sammyfans, 28 Oct 2026](https://www.sammyfans.com/2026/10/28/samsung-foresees-historic-ai-semiconductor-demand-through-2027/)) [S].
- **Micron** (FQ4 2026, quarter ended 3 Sep 2026, reported late Sep 2026)
  - Revenue about $54.2B (+379%); non-GAAP gross margin about 87%; FQ1 FY27 guidance $61.5B ±$1.5B ([XTB](https://www.xtb.com/en/market-analysis/record-after-record-micron-smashes-q4-results-server-overload-crashes-website-stock-surges-post-market); [hwbusters](https://hwbusters.com/?p=117879)) [S].
  - FY2026 capex $27.37B; first-half FY2027 capex about $25B with the second half higher, mostly construction for cleanrooms in late 2028 and beyond ([Blocks & Files, 1 Oct 2026](https://www.blocksandfiles.com/flash/2026/10/01/memory-gold-rush-bonanza-makes-billions-for-micron/5300445)) [S].
  - Idaho ID1 wafers mid-2027, ID2 end-2028, New York 2030. Most CY2027 HBM supply already contracted [S].
- **Intel** (29 Oct 2026)
  - 2026 gross capex about $20B; 2027 to rise strongly, with negative free cash flow expected. 18A is ramping and the 14A 0.9 PDK has been released ([Quartr](https://quartr.com/events/intel-intc-q3-2026_3sbE6kpM); [Business Insider Japan](https://www.businessinsider.jp/article/2611-earnings-intel-corporation-q3-2026-earnings-call-summary/)) [S].
  - Q4 guidance missed and the shares fell more than 20% after hours ([TechNews, 30 Oct 2026](https://finance.technews.tw/2026/10/30/intels-fourth-quarter-earnings-forecast-missed-market-expectations-causing-its-stock-price-to-plunge-by-more-than-20-at-one-point/)) [S].
- **Hyperscalers, Q3 2026** (28-29 Oct 2026; [Universal Asset Owners, 1 Nov 2026](https://www.universalassetowners.com/newsroom/hyperscaler-q3-capex-debt-equity-leases/)) [R]

  | Company | Q3 2026 capex | 2026 guidance | Funding notes |
  |---|---|---|---|
  | Microsoft | $45.2B incl. finance leases | CY2026 "should be approximately $170 billion" (CFO); Oct-Dec quarter over $50B | Third-party capacity deliveries delayed; $364.6B of leases "primarily for datacenters" not yet started |
  | Alphabet | $51.4B | Reported unchanged at $195-205B, capex to "increase significantly" in 2027 [S, not verified] | $28.7B senior notes; $12.4B of ATM share sales; no buybacks; quarterly FCF -$9.1B |
  | Amazon | $77.3B | 2026 cash capex about $220B | TTM FCF -$42.4B. Jassy projects "revenue growth rates of over 40% both in 2027 and in 2028" |
  | Meta | not given | $135-145B | Equity raise launched 26 Oct 2026; about $60B ATM planned from 19 Jan 2027 |

- **Oracle** (FQ4 FY26, 10-11 Jun 2026): FY27 capex up to $95B ($70B of its own plus $20-25B repaid by customers); FY26 capex about $55.7B against a $50B target; about $40B of debt and equity planned, including a $20B ATM; remaining performance obligations $638B; shares fell 8.9% after hours ([The Star/Reuters, 11 Jun 2026](https://www.thestar.com.my/tech/tech-news/2026/06/11/oracle-beats-fourth-quarter-revenue-estimates-amid-ai-spending-worries)) [R].
- **AI-lab commitments:** not covered. **INCOMPLETE.**

**Inferences**
- The four largest hyperscalers' 2026 capex is roughly $720-740B (my sum of the guidance above; Alphabet's figure is unverified). SK hynix's "+60% in 2027" would imply more than $1.1T in 2027.
- The demand that feeds measurement and test is concentrated in DRAM/HBM (SK hynix, Samsung, Micron), TSMC N2 and CoWoS, and AP inspection.

**Gaps**
- Rapidus, Samsung foundry capex, OpenAI/Anthropic/xAI commitments, and Oracle's September 2026 quarter.

### 3.3 Scenario tracking and behaviour in past pauses

**Takeaway:** Orders and backlogs support steady-to-accelerating growth through 2027. The funding mix (equity issuance, leases, negative free cash flow, Oracle leverage) is the main evidence for the 2028 financing-pause risk. *Past-pause behaviour: INCOMPLETE.*

**Cited findings: evidence for steady or acceleration**
- Repeated WFE upgrades at KLA and Lam; ASML customers seeking 2029-2030 slots; memory sold out through 2029; SEMI 300mm 2026 forecast raised from $116B to $149B (see 3.1 and 3.2).
- Backlogs: Onto >$1.3B ([8-K](https://www.sec.gov/Archives/edgar/data/0000704532/000119312526453582/onto-ex99_1.htm)) [P]; Lasertec ¥322.9B [S]; Camtek's initial 2027 outlook >$800M (>+35%) ([Finviz](https://finviz.com/news/415190/camtek-announces-results-for-the-third-quarter-of-2026)) [S].

**Cited findings: evidence for a financing-led pause**
- S&P: "The credit quality of hyperscalers is gradually weakening"; it warns that hyperscalers are lending their ratings to riskier borrowers ([Axios, 11 Sep 2026](https://axios.com/2026/09/11/ai-debt-hyperscalers-sp)) [S].
- Hyperscaler equity raising, leases and negative free cash flow (table in 3.2). Hyperscaler bonds of 10 years or longer were about 24% of corporate issuance at those maturities in 2026 (BIS, cited by [UAO](https://www.universalassetowners.com/newsroom/hyperscaler-q3-capex-debt-equity-leases/)) [R].
- Oracle: Moody's Baa2 rating on negative outlook; about $248B of lease commitments ([Cybernews, undated](https://cybernews.com/ai-news/five-debt-hotspots-ai-data-centre-boom/)) [S].
- Push-outs and softness in 2026:
  - Bruker moved $20M of semiconductor revenue into Q4 2026 [S].
  - PDF Solutions' backlog fell to $247.2M from $292.0M a year earlier ([10-Q](https://www.sec.gov/Archives/edgar/data/1120914/000143774926035296/pdfs20260930_10q.htm)) [P].
  - Microsoft's third-party capacity delays [R].
  - Intel's Q4 guidance miss [S].
- I found no cancellations at the large WFE makers.

**Gaps**
- Process-control, test and packaging revenue versus WFE in 2019 and 2022-23. **INCOMPLETE.**
- Evidence on power constraints and on credit spreads in Oct-Nov 2026. **INCOMPLETE.**

### 3.4 China

**Takeaway:** China's share is normalising from the 40%+ of 2024 to about 30% of WFE in 2026, with a temporary Q3 2026 spike that ASML attributes to memory-maker stockpiling. Domestic-substitution rules point to further share loss for foreign toolmakers in mature nodes.

**Cited findings**
- **Share of WFE:** upper-30s % in CY2025, mid-30s % in CY2026 (Tokyo Electron, 30 Apr 2026 [R]). About 29% of Q2 2026 SEMI billings, with China growing only 5% year on year [S].
- **Supplier shares over time**
  - ASML: nearly half of 2024 sales and about a third of 2025 ([Yahoo/Reuters, 15 Oct 2025](https://finance.yahoo.com/news/asmls-third-quarter-bookings-above-051227435.html)) [R]; 19% in Q1 2026, 14% in Q2, 23% in Q3, about 20% for FY2026. Q3 China shipments rose 109% quarter on quarter as memory makers stockpiled "enough lithography equipment to support three years of expansion" (SCMP via [AI Weekly](https://aiweekly.co/alerts/asml-q3-china-equipment-sales-soar-109-qoq-to-23-of-system-shipments-as-memory)) [R].
  - Lam: 43% (Sep-Q 2025) to 35% (Sep-Q 2026) [P].
  - KLA: 24% (Mar-Q 2026), 34% (Sep-Q 2026), high-20s for CY2026 [R].
  - Applied Materials: 37% (FY2024), about 35% (FQ3 2025), about 28% (FQ3 2026) [R].
  - Tokyo Electron: 34.1% in FY3/2026 [R].
  - Camtek: 49% in 2025 [P].
  - PDF Solutions: 16% (Q3 2026) [P].
- **Japanese toolmakers:** China sales of the top five fell about 12% to ¥1.47T in FY3/2026, the first-ever drop; front-end (TEL, Screen, Kokusai) China sales fell nearly 20%. China's localisation target is reportedly about 70% for mature processes by 2027 ([TrendForce, 22 Jun 2026](https://www.trendforce.com/news/2026/06/22/news-top-five-japanese-chip-toolmakers-reportedly-see-10-china-sales-drop-in-fy25-led-by-front-end-weakness/)) [R].
- **50% domestic-equipment rule:** an unpublished rule requires fabs adding capacity to show at least 50% of equipment spending goes to domestic suppliers. 50% is "a baseline"; officials "eventually... are aiming for plants to use 100% domestic equipment" ([Reuters via Yahoo, 30 Dec 2025](https://finance.yahoo.com/news/exclusive-china-mandates-50-domestic-090850539.html)) [S].

**Inferences**
- For measurement and inspection, the Q3 2026 China spike (KLA 34%, ASML 23%) looks like pull-forward. KLA itself expects a lower share in the December quarter and the low-20s % in 2027, so expect China's share to fall in H1 2027.

**Gaps**
- The China share is unverified for Onto, Teradyne, FormFactor, Hitachi High-Tech, Lasertec, JEOL and Technoprobe.

### 3.5 Export controls and trade restrictions

**Takeaway:** US-China relations are in a managed truce. The rules that bite on measurement and inspection (Oct 2022, Oct 2023 and Dec 2024 packages, the Entity List, the Dutch inspection licence and the Japanese list controls) stay in force. The rule changes that are scheduled cluster at **10 Jan 2027**.

**Cited findings**
- **Affiliates Rule**
  - Interim final rule published 30 Sep 2025 (90 FR 47201); it extends Entity List and Military End-User restrictions to entities 50% or more owned by listed parties.
  - Stayed on 10 Nov 2025 (90 FR 50857).
  - Stay extended by FR Doc 2026-22793: filed 5 Nov 2026, published and effective 9 Nov 2026. The amendments are "further stayed until January 10, 2027". Comments on the rule "will be considered for future, subsequent rulemakings" ([Federal Register](https://www.federalregister.gov/d/2026-22793); [public-inspection PDF](https://public-inspection.federalregister.gov/2026-22793.pdf)) [P].
  - The extension follows the September 2026 US-China agreement to extend the Busan arrangement to 10 Jan 2027 ([Cassidy Levy, 9 Nov 2026](https://www.cassidylevy.com/?p=3267); [Thompson Hine, 6 Nov 2026](https://www.thompsonhinesmartrade.com/2026/11/bis-extends-affiliates-rule-until-january-2027/)) [R].
  - Applied Materials said in Oct/Nov 2025 that the rule would cut FY2026 revenue by about $600M [S].
- **Earlier packages:** the 2 Dec 2024 package added 140 entities, including toolmakers such as Naura ([TechNode, 3 Dec 2024](https://technode.com/2024/12/03/us-adds-140-chinese-semiconductor-firms-to-entity-list-targeting-key-equipment-makers/); [FR, 5 Dec 2024](https://downloads.regulations.gov/BIS-2024-0056-0002/content.htm)) [S]. *Details of the measurement/inspection ECCNs in the Oct 2022, Oct 2023 and Dec 2024 rules: INCOMPLETE.*
- **2026 BIS actions**
  - 15 Jan 2026: revisions to the §744.23 end-use controls introducing case-by-case licence review ([FR 2026-00789](https://www.govinfo.gov/content/pkg/FR-2026-01-15/html/2026-00789.htm)) [S].
  - 13 Jan 2026: case-by-case review for certain advanced chips to China ([BIS](https://bis.gov/press-release/department-commerce-revises-license-review-policy-semiconductors-exported-china)) [S].
  - 11 Feb 2026: Applied Materials' $252.5M BIS settlement; DOJ and SEC closed their inquiries with no action [R].
- **Entity List**
  - No additions from Oct 2025 to Jun 2026 ([CSIS, 29 Jun 2026](https://www.csis.org/analysis/entity-list-additions-cool-their-slowest-pace-2008)) [S].
  - Reuters (Jun 2026): at least 75 entities in advanced chips, chip-equipment production and AI were slated for listing but held off, including DeepSeek and CXMT ([Malay Mail, 18 Jun 2026](https://www.malaymail.com/news/world/2026/06/18/deepseek-cxmt-among-chinese-firms-awaiting-us-entity-list-action-as-washington-weighs-trade-risks/224127)) [S].
  - A 21 Jul 2026 addition of 52 Chinese CNC-machine-tool entities is single-sourced ([Model Diplomat](https://modeldiplomat.com/story/us-restarts-china-export-controls-with-52-ent)) [R]. Not verified.
- **MATCH Act** (H.R. 8170, introduced 2 Apr 2026; Senate companion S. 4281)
  - Would extend controls to servicing and components and press allies on DUV immersion and servicing, using the foreign direct product rule ([govinfo](https://www.govinfo.gov/content/pkg/BILLS-119hr8170ih/html/BILLS-119hr8170ih.htm); [Capstone, 27 Apr 2026](https://capstonedc.com/insights/the-us-unprecedented-threat-to-foreign-semiconductor-firms/)) [R].
  - House Foreign Affairs Committee advanced it on 22 Apr 2026; no floor vote as of 22 Jul 2026; facilities targeted include SMIC, CXMT, YMTC, Hua Hong and Huawei ([TrendForce DataTrack](https://datatrack.trendforce.com/blog/content/61356/u-s-seeks-to-extend-chip-equipment-controls-to-maintenance-as-u-s-japanese-and-dutch-equipment-suppliers-reassess-china-exposure)) [R].
- **Netherlands:** a national licence requirement for certain measurement and inspection equipment, decided case by case; announced 15 Jan 2025, effective 1 Apr 2025. ASML expected no extra sales impact ([NL Times, 15 Jan 2025](https://nltimes.nl/2025/01/15/restrictions-chip-machine-exportations-dutch-companies-asml-asmi); [Tom's Hardware](https://www.tomshardware.com/tech-industry/netherlands-tightens-export-controls-on-sanctioned-semiconductor-equipment-move-made-in-line-with-u-s-limitations-asml-will-apply-for-licenses-from-the-dutch-government)) [S].
- **Japan**
  - 23 chip-equipment items controlled from 23 Jul 2023; a further 21 items added on 28 May 2025 ([TimeWell](https://timewell.jp/en/columns/japan-semiconductor-21-items-control)) [S].
  - 2026 debate on extending controls to maintenance and parts [S].
  - China placed 40 Japanese companies on export-control and watch lists on 24 Feb 2026 [S].
- **Section 232**
  - Proclamation of 14 Jan 2026: 25% on a narrow set of advanced computing chips from 15 Jan 2026, with broad carve-outs, including chips for US datacentres ([White & Case](https://www.whitecase.com/insight-alert/president-trump-orders-narrowly-targeted-25-section-232-tariff-certain-advanced); [EY](https://taxnews.ey.com/news/2026-0209-us-section-232-proclamation-imposes-25-percent-tariff-on-certain-semiconductors)) [S].
  - Chip-making equipment is not tariffed in Phase 1. A Commerce update was due by 1 Jul 2026; a Phase 2 with broader tariffs and an offset programme is possible ([TariffLens](https://www.tarifflens.ai/blog/section-232-semiconductor-tariff-july-2026-phase-2-guide)) [S].
- **China counter-measures**
  - On 9 Nov 2026 MOFCOM extended the suspension of the expanded rare-earth controls for two months to 10 Jan 2027. China's 24% extra tariff is also suspended two months while a 10% rate remains ([The National, 9 Nov 2026](https://www.thenationalnews.com/news/us/2026/11/09/china-extends-pause-on-rare-earth-export-curbs-for-two-months/); [The Star, 9 Nov 2026](https://www.thestar.com.my/aseanplus/aseanplus-news/2026/11/09/china-extends-suspension-of-rare-earth-export-controls-until-january)) [R].
  - The April 2025 licensing of seven medium and heavy rare earths remains in force ([Mining Technology](https://www.mining-technology.com/news/china-rare-earth-export-pause-nears-expiry-amid-persistent-supply-concentration/)) [S].
  - Gallium/germanium export ban suspended "until November 27, 2026" ([Nova 20-F](https://www.sec.gov/Archives/edgar/data/1109345/000117891326000504/zk2634307.htm)) [P].
  - The 24 Sep 2026 White House summit extended the truce, but the US "declined to negotiate its semiconductor embargoes" ([Cyprus Mail, 18 Oct 2026](https://cyprus-mail.com/2026/10/18/trump-xi-meeting-just-kicked-can-down-the-road)) [S].
  - Trump and Xi are expected to meet at APEC in Shenzhen in mid-November ([The National](https://www.thenationalnews.com/news/us/2026/11/09/china-extends-pause-on-rare-earth-export-curbs-for-two-months/)) [R].
- **Servicing restrictions:** *details INCOMPLETE.*

---

## 4. Could not verify (as of v1)
- China shares for Onto, Teradyne, FormFactor, Hitachi High-Tech, Lasertec, JEOL and Technoprobe; Nova's ~30% figure.
- Alphabet's October 2026 capex guidance; Lam's December-quarter guidance ($8.6B per Statementdog); S&P's 2027 capex projections (Alphabet $357B, Amazon $319B, Meta $164B, Microsoft $189B, search snippet only).
- Section 232 Phase 2 outcome; MATCH Act status after July 2026; the 21 Jul 2026 Entity List additions.
- Whether the gallium/germanium suspension was extended past 27 Nov 2026.
- 2019 and 2022-23 pause behaviour; process-control share of WFE; 2024 WFE actual; TechInsights and Gartner figures.

## 5. Sources with dates
(See the inline links above. Consolidated list to follow in v2.)
