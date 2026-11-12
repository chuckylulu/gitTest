# Stacked high-bandwidth memory (HBM) for AI processors — makers, supply-demand, roadmaps and business quality (research date 12 Nov 2026)

Scope and method notes (read first):
- Research date 12 Nov 2026. Primary sources used where possible:
  - Samsung 3Q26 earnings deck (29 Oct 2026).
  - Micron FQ4 FY26 prepared remarks (30 Sep 2026) and FY2026 Form 10-K (fiscal year ended 3 Sep 2026).
  - SK hynix Q3 2026 preliminary-results Form 6-K (28 Oct 2026), H1 2026 6-K, and US IPO prospectus (424B4, July 2026; F-1 filed 24 Jun 2026).
  - BIS (US Bureau of Industry and Security) release of 2 Dec 2024.
  - CXMT's own website.
- SK hynix's Q3 call commentary (HBM, LTAs, capex) comes from an AI-assisted Investing.com transcript and VLSI.kr (secondary).
- Search tools ran out part-way through. The shared WebSearch budget was exhausted; at the coordinator's direction I tried Exa and Firecrawl, and both returned out-of-credit errors. Later work used pages already found, links followed from them, SEC EDGAR filings and a few constructed primary URLs.
- As a result, coverage is thin for: mainland China beyond CXMT; Japan; Taiwan's smaller makers; high-bandwidth flash at SanDisk and Kioxia; and Korean export-control texts. See section (7).
- No share prices, valuation multiples, market capitalisation or price targets are recorded (some sources contained them; they were deliberately dropped).
- "Company claim, unconfirmed" marks statements no outside party has confirmed. "Secondary" marks trade press/analyst sources.

---

## (1) Segment map — who makes, or wants to make, stacked memory

### Takeaway
Volume HBM is a three-company market (SK hynix, Samsung Electronics, Micron), all three qualified on NVIDIA's HBM4 platform (Vera Rubin) since June 2026. Mainland China's CXMT is now the fourth-largest DRAM maker by revenue (9-10% share) and is building HBM lines, but no confirmed HBM shipments were found. Base dies have become logic chips made by foundries (TSMC for SK hynix; Samsung Foundry in-house; Micron in-house). No HBM maker was found in Europe, Israel or India; Japan and India host Micron plants only.

### Cited Findings

| Company | Home | Listing / ticker | Role in segment | Why it matters / why left out |
|---|---|---|---|---|
| SK hynix | South Korea | KRX 000660; Nasdaq ADS "SKHY" (US IPO July 2026) | HBM #1 by revenue; HBM3E leader, HBM4 in volume from Q3 2026 | 50% HBM revenue share Q2 2026 (Counterpoint); 56.4% Q1 2026 (IDC); est. 60-70% of Vera Rubin HBM4 |
| Samsung Electronics | South Korea | KRX 005930 | HBM #2 and rising; first HBM4 mass production (Feb 2026); in-house 4nm base die | 33% HBM share Q2 2026 (Counterpoint); expected by Counterpoint to lead HBM in 2027 |
| Micron Technology | United States | Nasdaq MU | HBM #3; HBM4 36GB 12-high in volume (Mar 2026); in-house base die | 18-21% HBM share (Counterpoint); only maker with US DRAM fabs planned (Idaho, New York) |
| CXMT (ChangXin Memory) | Mainland China | Shanghai STAR Market, SSE 688825 (ticker on CXMT's site; listing date not verified) | #4 DRAM maker; HBM lines "in development" in Shanghai | 9% DRAM revenue share Q3 2026; TTM to Sep 2026 operating margin ~79%; no confirmed HBM shipments |
| TSMC | Taiwan | TWSE 2330 / NYSE TSM | Makes HBM4 logic base die for SK hynix (12nm on 16-high HBM4 per VLSI.kr); CoWoS packaging | Adjacent — captures base-die and packaging value |
| Samsung Foundry | South Korea | Part of Samsung Electronics | Makes Samsung's 4nm HBM4/HBM4E base die ("HBM B-Die") | Foundry recovery in 2026 attributed partly to base dies |
| Nanya Technology | Taiwan | TWSE 2408 | Conventional DRAM, ~2% revenue share | No HBM activity found; left out of key list |
| Powerchip (PSMC) | Taiwan | TWSE 6770 | Sold its Tongluo fab to Micron (US$1.8bn, Mar 2026) for DRAM/HBM | Capacity supplier, not an HBM maker |
| SanDisk | United States | Nasdaq SNDK | NAND maker; named by SK hynix as a NAND competitor | High-bandwidth flash (HBF) work not verified in this pass |
| Kioxia | Japan | TSE (ticker not re-verified) | NAND maker; SK hynix holds an investment that produced gains in 2026 | HBF work not verified in this pass |
| YMTC | Mainland China | Private | NAND maker; Micron names it as a state-backed competitor | Any HBM/DRAM activity not verified in this pass |
| Micron Hiroshima | Japan | (Micron subsidiary) | DRAM fab; new cleanroom (groundbreaking Jul 2026) for HBM and AI memory, output late 2028 | Japan's only HBM-relevant DRAM site found |
| Micron Sanand (Gujarat) | India | (Micron subsidiary) | Assembly and test; commercial shipments began 2026 | No evidence it handles HBM |

Sources for the table:
- Shares: Counterpoint HBM revenue share Q2-25 to Q2-26 (published 2 Sep 2026) — [Counterpoint](https://counterpointresearch.com/en/insights/global-dram-and-hbm-market-share); Q3 2026 DRAM shares (published 5 Nov 2026) — [Counterpoint](https://counterpointresearch.com/en/insights/dram-super-cycle-nears-dollar-200b); IDC figure — [SK hynix 424B4](https://www.sec.gov/Archives/edgar/data/0002120882/000119312526299963/d32785d424b4.htm)
- SK hynix Nasdaq ADS "SKHY" and KRX code 000660 — [SK hynix 424B4 prospectus (July 2026)](https://www.sec.gov/Archives/edgar/data/0002120882/000119312526299963/d32785d424b4.htm)
- NVIDIA qualification of all three (5 Jun 2026) and allocation estimates — [Yahoo/Investing.com](https://finance.yahoo.com/sectors/technology/articles/nvidia-certifies-samsung-sk-hynix-133001560.html); [VLSI.kr](https://www.vlsi.kr/en/hbm4-three-way-race-en/)
- Samsung first HBM4 mass production 12 Feb 2026; Micron HBM4 mass production 16 Mar 2026 — [Tech-Insider (secondary)](https://tech-insider.org/hbm4-memory-shortage-amd-samsung-sk-hynix-price-spike-2026/); [Silicon Analysts (secondary)](https://siliconanalysts.com/tools/hbm-analysis)
- **CXMT forecasts and Shanghai HBM lines (20 Oct 2026, pre-results):**
  - 9M 2026 revenue RMB 265-270bn (more than 7x YoY).
  - 9M 2026 net profit RMB 131-132.5bn, against a 9M 2025 net loss of RMB 5.3bn.
  - Q3 2026 revenue RMB 114.7-119.7bn; net profit RMB 53.4-54.9bn (+1-4% QoQ).
  - Two 12-inch DRAM fabs in Hefei and one in Beijing, each with capacity of up to 100k wafers/month.
  - New DRAM and HBM lines in development in Shanghai.
  - Source: [TrendForce news 20 Oct 2026](https://www.trendforce.com/news/2026/10/20/news-cxmts-earnings-boom-faces-test-as-3q-profit-growth-slows-to-1-4-qoq-whats-behind-the-slowdown/)
- **CXMT listing and products (primary):** the website header shows ticker "SSE:688825". On 20 Sep 2026 CXMT announced mass production of its 5th-generation (G5) DRAM platform (11.95nm half active-area pitch). It also announced 24Gb LPDDR5X products on G5, with die per wafer more than 50% above G4 (company claim). HBM is not mentioned on the page. Source: [CXMT news page](https://www.cxmt.com/en/news/info_22.html)
- **CXMT financial history (aggregator of company filings, secondary):**

  | Period | Revenue (CNY) | Net result (CNY) | Margins |
  |---|---|---|---|
  | FY2022 | 8.29bn | loss 8.33bn | n/a |
  | FY2023 | 9.09bn | loss 16.34bn | n/a |
  | FY2024 | 24.18bn | loss 7.15bn | n/a |
  | FY2025 | 61.80bn | profit 1.88bn | gross margin 40.2% |
  | TTM to 30 Sep 2026 | 298.74bn | profit 139.2bn | gross 83.9%, operating 79.5% |

  Source: [stockanalysis.com CXMT financials](https://stockanalysis.com/quote/sha/688825/financials/)
- TSMC 12nm base die on SK hynix 16-high HBM4 (CES 2026) — [VLSI.kr bonding article (secondary)](https://www.vlsi.kr/en/hbm4-bonding-battle-en/); Samsung 4nm base die — [TrendForce 23 Jun 2026](https://www.trendforce.com/news/2026/06/23/news-memory-giants-split-on-hbm4-strategy-samsung-hbm4-sales-reportedly-tops-1b-sk-hynix-slows-ramp/); "HBM B-Die" sales lifted Foundry — [Samsung 3Q26 deck](https://images.samsung.com/is/content/samsung/assets/global/ir/docs/2026_3Q_conference_eng.pdf); Micron in-house base logic die — [Micron FY2026 10-K](https://www.sec.gov/Archives/edgar/data/0000723125/000072312526000023/mu-20260903.htm)
- Nanya 2% DRAM share — [Counterpoint](https://counterpointresearch.com/en/insights/global-dram-and-hbm-market-share)
- Tongluo purchase from PSMC (US$1.8bn, Mar 2026), Hiroshima cleanroom (Jul 2026, output late 2028), Gujarat shipments in 2026, Micron naming CXMT and YMTC as state-backed competitors — [Micron FY2026 10-K](https://www.sec.gov/Archives/edgar/data/0000723125/000072312526000023/mu-20260903.htm)
- SK hynix names Samsung, Micron, CXMT (DRAM) and Samsung, Kioxia, Micron, Sandisk (NAND) as major competitors; Q3 2026 special dividend tied to a Kioxia gain — [SK hynix 424B4](https://www.sec.gov/Archives/edgar/data/0002120882/000119312526299963/d32785d424b4.htm); [VLSI.kr Q3 facts (secondary)](https://www.vlsi.kr/en/sk-hynix-q3-2026-earnings-14-facts-en/)

### Inferences
- The "makers" set is effectively closed at three for 2026-2028. CXMT is the only credible fourth entrant on the evidence gathered, and it serves China.
- Base-die logic is now a separate value pool. Samsung is the only maker that controls both DRAM and the base-die foundry in-house. SK hynix depends on TSMC. Micron makes its HBM4 base die in-house (10-K), but has not said who makes its custom HBM4E (NVHBM) die.

### Gaps (coverage thin — say so)
- **Mainland China beyond CXMT:** Huawei's in-house HBM, YMTC's or XMC's HBM efforts, and Tongfu/JCET packaging were not verified (search budget exhausted). One sourced fact: SK hynix stopped selling to Huawei in September 2020 ([424B4](https://www.sec.gov/Archives/edgar/data/0002120882/000119312526299963/d32785d424b4.htm)).
- **CXMT listing details:** the listing is confirmed by the "SSE:688825" ticker on CXMT's site; 688-codes are STAR Market. Not verified: the filing date (the brief's late-2025 lead), listing date, amount raised and prospectus figures. TrendForce reported IPO counselling began in July 2025 ([TrendForce 8 Jul 2025](https://www.trendforce.com/news/2025/07/08/news-chinas-cxmt-reportedly-begins-ipo-counselling-aims-to-be-first-memory-chip-firm-on-a-share/)).
- **CXMT HBM:** no HBM product, customer or shipment was confirmed. The only HBM evidence is "new DRAM and HBM production lines in development in Shanghai" (36Kr via TrendForce, Oct 2026).
- **Japan:** the SoftBank/Intel "Saimemory" stacked-DRAM venture and Kioxia's high-bandwidth flash were not verified.
- **Taiwan:** Winbond's CUBE and AP Memory's stacked DRAM were not checked.
- **Europe and Israel:** no HBM or DRAM maker was found in the sources reviewed. Absence was not confirmed in local-language sources.
- **India:** only Micron's Gujarat assembly/test plant was found.

---

## (2) Evidence on tests (a) to (e) — key companies

### Takeaway
All three key makers are in an unprecedented upcycle: Q3 2026 operating margins of about 80% (SK hynix), 82% (Micron, FQ4) and 72% (Samsung DS). All hold large net cash and have multi-year supply agreements. The quality differences are elsewhere:
- **SK hynix:** HBM share is eroding (64% → 50%) and it has the most China exposure.
- **Samsung:** the group's profit is almost entirely the memory cycle.
- **Micron:** the most contract-backed revenue and the least customer concentration, but the smallest HBM share.

### Cited Findings — SK hynix

**(a) Position**
- Owns process know-how (advanced MR-MUF stacking, TSV) and scarce DRAM cleanroom capacity. Customers' qualification gates act as the "judge". SK hynix says customers "often require HBM manufacturers to comply with rigorous testing and approval processes" ([424B4](https://www.sec.gov/Archives/edgar/data/0002120882/000119312526299963/d32785d424b4.htm)).
- **BRIDGE:** HBM3E, expected to be about two-thirds of 2026 HBM shipments per SK hynix's January 2026 outlook ([IntuitionLabs (secondary)](https://intuitionlabs.ai/articles/hbm-dram-ai-memory-demand)). Its successor, HBM4, began full-scale mass production in Q3 2026 and is expected to pass HBM3E in volume and revenue in Q4 2026 ([Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-sk-hynix-posts-record-q3-2026-results-shares-jump-after-hours-93CH-4977343)).
- **Slip recorded:** TrendForce said SK hynix's HBM4 mass-production timeline was "pushed back" to meaningful volume in 3Q26 and cut its 2026 HBM4 shipment forecast from 4.5bn Gb to 4bn Gb ([TrendForce 23 Jun 2026](https://www.trendforce.com/news/2026/06/23/news-memory-giants-split-on-hbm4-strategy-samsung-hbm4-sales-reportedly-tops-1b-sk-hynix-slows-ramp/)). A secondary summary attributes the slip to "HBM4 certification delays and interface synchronization issues", with some capacity shifted to DDR5/LPDDR5 ([VLSI.kr/Bernstein summary](https://www.vlsi.kr/en/bernstein-hbm-crossover-en/)). Chosun Biz framed it as a deliberate move toward more profitable commodity DRAM (via the TrendForce article above).
- **SUCCESSOR:** HBM4E 12-high samples shipped 18 Jun 2026, 16 Gb/s per pin ([VLSI.kr bonding](https://www.vlsi.kr/en/hbm4-bonding-battle-en/); [VLSI.kr HBM4E/HBF](https://www.vlsi.kr/en/hbm4e-post-hbm-memory-hierarchy-war-en/)).
- **New tier:** high-bandwidth flash, proposed at SEDEX on 14 Oct 2026 and called "medium to long term" (same sources). The H1 2026 6-K lists "AIN B (HBF)" in development ([6-K](https://www.sec.gov/Archives/edgar/data/0002120882/000119312526354777/d147827d6k.htm)).

**(b) Lead**
- **HBM revenue share (Counterpoint):** 64% Q2-25, 56% Q3-25, 57% Q4-25, 58% Q1-26, 50% Q2-26 ([Counterpoint](https://counterpointresearch.com/en/insights/global-dram-and-hbm-market-share)). IDC put it at 56.4% in Q1 2026 ([424B4](https://www.sec.gov/Archives/edgar/data/0002120882/000119312526299963/d32785d424b4.htm)).
- **Vera Rubin:** est. 60-70% of HBM4 volume. NVIDIA has published no official split ([Yahoo/Investing.com](https://finance.yahoo.com/sectors/technology/articles/nvidia-certifies-samsung-sk-hynix-133001560.html)).
- **Forecasts of decline:** JPMorgan sees HBM share falling 60% (2025) → 46% (2026E) → 41% (2027E). UBS puts 2027 HBM bit shipments at Samsung 41% vs SK hynix 39%. LS Securities cut SK hynix's 2027 HBM operating margin estimate from ~80% to ~60% (ChosunBiz, 21 Oct 2026) ([VLSI.kr (secondary)](https://www.vlsi.kr/en/bernstein-hbm-crossover-en/)).
- **Earlier qualifications:** HBM3 → NVIDIA H100 (Jun 2022); HBM3E 8-high → H200 (Mar 2024); dominant share of GB300 HBM3E 12-high orders (TrendForce, May 2025); AWS Trainium 3 (with Micron); Google TPU v7 (first supplier, with Samsung) ([Silicon Analysts (secondary)](https://siliconanalysts.com/tools/hbm-analysis)).
- **Yield:** HBM4 yield "in the 80% range" per Infostock Daily ([TrendForce 10 Aug 2026](https://www.trendforce.com/news/2026/08/10/news-samsungs-hbm4-yield-reportedly-hits-80-as-race-to-supply-vera-rubin-heats-up-sk-hynix-labor-talks-add-a-twist/)). SK hynix says HBM4 yield beat its target (company claim, unconfirmed).

**(c) Revenue model**
- All revenue is hardware: memory chips, modules and SSDs.
- **LTAs:** signed with 14 key customers covering more than 50% of 2027-2028 capacity. Typical term is five years, priced within agreed ranges, with deposits as safeguards. Combined with volume under discussion, management says DRAM and HBM are "effectively sold out through 2029" (company claim) ([Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-sk-hynix-posts-record-q3-2026-results-shares-jump-after-hours-93CH-4977343)).
- A three-year DDR5 supply agreement with Microsoft (Chosun Biz, via [TrendForce 23 Jun 2026](https://www.trendforce.com/news/2026/06/23/news-memory-giants-split-on-hbm4-strategy-samsung-hbm4-sales-reportedly-tops-1b-sk-hynix-slows-ramp/)).
- 2027 HBM volume and price negotiations are finalised, figures not disclosed. Press reports put SK hynix's HBM4 price to NVIDIA in the "mid-$500s per stack" (unconfirmed; [VLSI.kr daily 12 Nov 2026](https://www.vlsi.kr/en/daily-silicon-2026-11-12-en/)).
- HBM was more than 40% of revenue per Chosun Biz (mid-2026; [TrendForce 23 Jun 2026](https://www.trendforce.com/news/2026/06/23/news-memory-giants-split-on-hbm4-strategy-samsung-hbm4-sales-reportedly-tops-1b-sk-hynix-slows-ramp/)). The company does not disclose HBM revenue.

**(d) Financial strength (KRW, K-IFRS)**

| Period | Revenue | Operating profit | Op. margin | Net profit |
|---|---|---|---|---|
| FY2023 | n/a | n/a | n/a | net loss 9.14tn |
| FY2024 | 66.19tn | n/a | n/a | 19.80tn |
| FY2025 | 97.15tn (+46.8%) | 47.21tn | 48.6% | 42.95tn |
| Q1 2026 | 52.58tn | 37.61tn | 71.5% | 40.35tn |
| Q2 2026 | 79.32tn | 60.54tn | 76% | 93.92tn |
| Q3 2026 | 104.6tn (+32% QoQ, +328% YoY) | 83.3tn | 79.7% | 39.8tn |

- **Q3 2026 detail:** EBITDA KRW 87.7tn (84% margin); gross margin 86%. Net profit was reduced by KRW 32.6tn of non-operating losses (FX KRW 11.6tn, investment valuation KRW 22.9tn).
- **Earnings-quality flag:** Q2 net profit exceeded operating profit, and Q3 net profit fell far below it, both because of investment revaluations. Operating profit is the cleaner measure.
- **Balance sheet (30 Sep 2026):** cash KRW 114.5tn, borrowings KRW 15.8tn, net cash KRW 98.7tn, debt/equity 5%. Credit ratings: Moody's A3 (Aug 2026), S&P BBB+ (Feb 2026), Fitch BBB+ (Apr 2026). Return on capital was not disclosed in the sources reviewed.
- **Capex:** KRW 8.3tn (2023), 15.9tn (2024), 27.5tn (2025), 17.6tn in H1 2026. Capex for 2027 is to "rise significantly"; no figure given.
- **Shareholder returns:** FY2026 target about KRW 100tn.
- **Customer concentration:** largest customer 23.9% of 2025 revenue (not named); two largest 14.8% and 12.4% of Q1 2026 revenue.
- **Geography (by sales-subsidiary location):** US 47.0% (2023), 63.4% (2024), 68.8% (2025), 64.7% (Q1 2026). China 30.9%, 23.5%, 19.7%, 24.3% over the same periods. Asia 7.4% (2025).
- **Manufacturing footprint:** Icheon and Cheongju (Korea), Wuxi (China, DRAM), Dalian (China, NAND, ex-Intel), Chongqing (China, assembly/test).
- **Primary confirmation of Q3 2026 (preliminary, unaudited, 28 Oct 2026):**
  - Q3 revenue KRW 104,615.5bn; operating profit KRW 83,333.8bn; pre-tax profit KRW 50,708.5bn; profit for the period KRW 39,775.6bn.
  - 9M 2026 revenue KRW 236,510.5bn; 9M operating profit KRW 181,486.7bn (about 76.7% margin, my arithmetic).
  - Q3 2025 comparison: revenue KRW 24,448.9bn, operating profit KRW 11,383.4bn.
  - Source: [SK hynix 6-K, preliminary results, 28 Oct 2026](https://www.sec.gov/Archives/edgar/data/2120882/000119312526434994/d162547d6k.htm)
- **Solidigm (NAND subsidiary):** the pre-IPO raise and IPO plans were discontinued ([6-K 23 Oct 2026](https://www.sec.gov/Archives/edgar/data/2120882/000119312526429184/d159239d6k.htm)). SK hynix says Solidigm is "reviewing various measures" to expand capacity, but a reported ~KRW 60tn US NAND fab is "not determined" ([6-K 29 Oct 2026](https://www.sec.gov/Archives/edgar/data/2120882/000119312526436872/d183583d6k.htm)).
- Sources: [Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-sk-hynix-posts-record-q3-2026-results-shares-jump-after-hours-93CH-4977343); [VLSI.kr Q3 facts](https://www.vlsi.kr/en/sk-hynix-q3-2026-earnings-14-facts-en/); [6-K H1 2026](https://www.sec.gov/Archives/edgar/data/0002120882/000119312526354777/d147827d6k.htm); [424B4](https://www.sec.gov/Archives/edgar/data/0002120882/000119312526299963/d32785d424b4.htm)

**(e) Resilience**
- **Last downturn:** 2023 net loss of KRW 9.14tn ([424B4](https://www.sec.gov/Archives/edgar/data/0002120882/000119312526299963/d32785d424b4.htm)).
- **Export controls:** the Validated End-User status for the China fabs was revoked effective 31 Dec 2025. The BIS (US Bureau of Industry and Security) replaced it with an annual approval and granted a licence for 2026 in December 2025. "Failure to obtain the required licenses in a timely manner may materially impact our manufacturing operations in China" (same source).
- **Tariffs:** semiconductors were exempt from the IEEPA "reciprocal" tariffs (Korea rate 15%) and from the Section 122 surcharge (10% raised to 15%, effective 24 Feb 2026, for 150 days) that followed the February 2026 Supreme Court ruling. The US threatened a 100% semiconductor tariff in August 2025 and January 2026, with exemptions for firms investing in the US (same source).
- **Labour:** the 2026 union dispute over profit-sharing paid in treasury shares was unresolved in August 2026 ([TrendForce 10 Aug 2026](https://www.trendforce.com/news/2026/08/10/news-samsungs-hbm4-yield-reportedly-hits-80-as-race-to-supply-vera-rubin-heats-up-sk-hynix-labor-talks-add-a-twist/)).

### Cited Findings — Samsung Electronics (memory is now most of the group)

**How much of the group is memory**
- Q3 2026 (reported 29 Oct 2026): company revenue KRW 195.3tn (+127% YoY), OP KRW 107.4tn (55.0%).
- DS division: revenue KRW 147.1tn, OP KRW 106.5tn (72% margin).
- Memory revenue KRW 140.7tn (+427% YoY), about 72% of company revenue. Segment sales include intersegment sales, so this is approximate.
- DS was about 99% of company operating profit in Q3 2026 and 99.7% in Q2 2026 (DS OP KRW 89.2tn of 89.5tn).
- One year earlier (Q3 2025), memory was KRW 26.7tn of 86.1tn revenue (~31%) and DS OP was KRW 7.0tn of 12.2tn.
- Other segments in Q3 2026: DX (mobile, TV, appliances) OP −KRW 0.8tn on KRW 52.1tn revenue; Samsung Display OP KRW 1.1tn; Harman OP KRW 0.6tn (helped by US tariff refunds).
- Foundry/System LSI (in passing): Foundry improved on "HBM B-Die sales growth" and 2nm high-performance-computing orders; the first Taylor fab is starting operations.
- Source: [Samsung 3Q26 earnings deck (primary)](https://images.samsung.com/is/content/samsung/assets/global/ir/docs/2026_3Q_conference_eng.pdf)

**(a) Position**
- Largest DRAM capacity (38% DRAM revenue share Q3 2026, [Counterpoint](https://counterpointresearch.com/en/insights/dram-super-cycle-nears-dollar-200b)) plus an in-house 4nm logic base die. This is a physical-capacity and integration position, not a judge.
- **BRIDGE:** HBM3E 12-high, which reached NVIDIA GB300 only from Q3 2025 per Korea Economic Daily ([Silicon Analysts](https://siliconanalysts.com/tools/hbm-analysis)).
- **Current product:** HBM4, mass production from Feb 2026, 11.7 Gbps in testing ([TrendForce 29 May 2026](https://www.trendforce.com/news/2026/05/29/news-samsung-starts-shipping-industry-first-hbm4e-samples-three-months-after-hbm4-mass-production-performance-up-over-20/)). HBM4 was 60% of HBM sales in Q3 2026 ([Investing.com Samsung transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-samsung-electronics-posts-record-q3-2026-profit-93CH-4981365)).
- **SUCCESSOR:** HBM4E 12-high 48GB samples shipped in May 2026 (claimed industry-first; 14-16 Gbps, 3.6 TB/s, 1c DRAM, 4nm base die). Mass production is planned for H1 2027, with volume ramp in H2 2027 (same sources).

**(b) Lead**
- **HBM revenue share (Counterpoint):** 15% Q2-25, 23% Q3-25, 22% Q4-25, 21% Q1-26, 33% Q2-26 ([Counterpoint](https://counterpointresearch.com/en/insights/global-dram-and-hbm-market-share)). Samsung says HBM share reached parity with its DRAM share in Q3 2026 (company claim).
- **Outside forecasts:** Counterpoint (5 Nov 2026) says Samsung is "expected to take the top spot in HBM next year" ([Counterpoint](https://counterpointresearch.com/en/insights/dram-super-cycle-nears-dollar-200b)). TrendForce raised its 2026 HBM4 share forecast "on its lead in customer qualification" and raised Samsung's 2026 HBM4 shipments from 3.5bn Gb to 4bn Gb ([TrendForce 10 Aug](https://www.trendforce.com/news/2026/08/10/news-samsungs-hbm4-yield-reportedly-hits-80-as-race-to-supply-vera-rubin-heats-up-sk-hynix-labor-talks-add-a-twist/); [TrendForce 23 Jun](https://www.trendforce.com/news/2026/06/23/news-memory-giants-split-on-hbm4-strategy-samsung-hbm4-sales-reportedly-tops-1b-sk-hynix-slows-ramp/)).
- **HBM4 revenue passed US$1bn** by June 2026, the first maker to do so (Yonhap/ZDNet, same TrendForce 23 Jun article).
- **Qualifications:** NVIDIA Vera Rubin (5 Jun 2026). AMD MI455X HBM4 supplier per Korea Herald (24 Jul 2026) ([Silicon Analysts](https://siliconanalysts.com/tools/hbm-analysis)). AMD-Samsung three-year memorandum covering HBM4 ([Tech-Insider](https://tech-insider.org/hbm4-memory-shortage-amd-samsung-sk-hynix-price-spike-2026/)).
- **Historically primary at AMD:** MI300X (>60%), MI325X, MI355X; also Google TPU v5p, v6e and v7 ([Silicon Analysts (secondary)](https://siliconanalysts.com/tools/hbm-analysis)).
- **Yield:** HBM4 yield ~80%, up from <60% at the February start (Seoul Economic Daily via [TrendForce 10 Aug 2026](https://www.trendforce.com/news/2026/08/10/news-samsungs-hbm4-yield-reportedly-hits-80-as-race-to-supply-vera-rubin-heats-up-sk-hynix-labor-talks-add-a-twist/)).
- **Price gap:** press reports say Samsung sold HBM3E 12-high about 30% below SK hynix's price and seeks HBM4 price parity in NVIDIA talks still in their "final stage" in November 2026 (unconfirmed; [VLSI.kr daily 12 Nov 2026](https://www.vlsi.kr/en/daily-silicon-2026-11-12-en/)). Note: this VLSI daily item also repeats clearly stale 2025-era claims (e.g. HBM4 "qualification expected November 2026"), so treat it with caution.

**(c) Revenue model**
- Hardware sales.
- Ten multi-year supply contracts signed and ten more in talks. Samsung targets 60-70% of mid-to-long-term capacity under multi-year contracts.
- "2027 HBM supply volume is already sold out at an agreed target price" (company claim). No prepayment terms disclosed.
- Source: [Investing.com Samsung transcript (AI-assisted)](https://www.investing.com/news/transcripts/earnings-call-transcript-samsung-electronics-posts-record-q3-2026-profit-93CH-4981365)

**(d) Financial strength (group, 30 Sep 2026)**
- Cash KRW 214.8tn, debts KRW 17.2tn, net cash KRW 197.6tn.
- Q3 2026 operating cash flow KRW 98.6tn; PP&E purchases KRW 26.9tn.
- ROE 57% (as reported in the deck); EBITDA margin 62%.
- Total 2026 shareholder returns estimated at KRW 90-110tn ([Samsung 3Q26 deck](https://images.samsung.com/is/content/samsung/assets/global/ir/docs/2026_3Q_conference_eng.pdf)).
- **Capex:** Q3 2026 KRW 29tn (DS 27.2tn); 9M 2026 KRW 56.9tn; FY2026 guidance KRW 84.4tn (DS KRW 76.8tn, +29.3tn YoY) ([Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-samsung-electronics-posts-record-q3-2026-profit-93CH-4981365)).
- **Packaging site (secondary, unconfirmed):** Samsung reportedly broke ground on 12 Nov 2026 on a KRW 46tn HBM advanced-packaging site in Onyang, operating June 2028 and in mass production May 2029 (VLSI.kr research teaser; [VLSI.kr daily](https://www.vlsi.kr/en/daily-silicon-2026-11-12-en/)).
- Customer and geographic concentration were not found in the sources reviewed.

**(e) Resilience**
- The group's diversification cushioned the last cycle: Q3 2025 DS OP KRW 7.0tn vs DX OP KRW 3.5tn.
- That cushion is now small: DX lost money in Q3 2026 while DS made KRW 106.5tn.
- Samsung's own outlook: supply tight into 2028, and higher 2027 capex is unlikely to lift 2028 bit output much because of construction lead times (company view; [transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-samsung-electronics-posts-record-q3-2026-profit-93CH-4981365)).

### Cited Findings — Micron Technology

**(a) Position**
- Process know-how: 1-beta/1-gamma DRAM, in-house HBM4 base logic die "designed and manufactured in-house" ([10-K](https://www.sec.gov/Archives/edgar/data/0000723125/000072312526000023/mu-20260903.htm)). Also geographically diversified, US-based supply ("DRAM made in the U.S.") ([prepared remarks](https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf)).
- **BRIDGE:** HBM3E 12-high, the majority of 2026 HBM shipments.
- **Current product:** HBM4 36GB 12-high in volume during 2026; 48GB 16-high sampled.
- **SUCCESSOR:** HBM4E, expected to "ramp volume in calendar 2027" on 1-gamma ([10-K](https://www.sec.gov/Archives/edgar/data/0000723125/000072312526000023/mu-20260903.htm)). It includes NVHBM, a custom HBM4E co-developed with NVIDIA ([prepared remarks](https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf)). Its first HBM4E follows JEDEC standards, with ramp targeted for 2027 (J.P. Morgan conference, via [TrendForce 29 May 2026](https://www.trendforce.com/news/2026/05/29/news-samsung-starts-shipping-industry-first-hbm4e-samples-three-months-after-hbm4-mass-production-performance-up-over-20/)).
- Next DRAM/NAND nodes: volume production in H2 CY2027 ([prepared remarks](https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf)).

**(b) Lead**
- HBM revenue share 21% in each quarter Q2-25 to Q1-26, and 18% in Q2-26 ([Counterpoint](https://counterpointresearch.com/en/insights/global-dram-and-hbm-market-share)).
- TrendForce describes Micron as having "limited HBM4 exposure" ([TrendForce 10 Aug 2026](https://www.trendforce.com/news/2026/08/10/news-samsungs-hbm4-yield-reportedly-hits-80-as-race-to-supply-vera-rubin-heats-up-sk-hynix-labor-talks-add-a-twist/)).
- Qualified at NVIDIA Vera Rubin (5 Jun 2026), est. "high-single to low-double digits" share ([VLSI.kr](https://www.vlsi.kr/en/hbm4-three-way-race-en/)).
- Earlier: HBM3E in NVIDIA H200 (Feb 2024) and GB300 (Mar 2025), AMD MI350 (Q3 2025), AWS Trainium 3 ([Silicon Analysts](https://siliconanalysts.com/tools/hbm-analysis)).
- More than US$1bn of HBM4 revenue shipped, and the 12-high HBM4 ramp running at twice the pace of HBM3E (company claims reported by Zacks, 13 Oct 2026; [Yahoo](https://finance.yahoo.com/markets/stocks/articles/microns-hbm4-ramp-higher-pricing-123300062.html)).

**(c) Revenue model — the most contract-backed of the three**
- 26 strategic customer agreements (SCAs): multi-year take-or-pay, estimated at more than 35% of revenue through 2030, and possibly ~50% per the Q&A.
- Pricing: three-quarters of SCA revenue has a defined pricing framework, mostly bands with floor and ceiling prices; one quarter is repriced periodically at market.
- Remaining performance obligations about US$150bn. Customer financial commitments US$32bn, mostly cash deposits.
- Source: [prepared remarks](https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf)
- Deposits received in FY2026: US$12.75bn, "nearly all" repayable 2029-2031, and forfeitable if minimum purchases are missed. Letters of credit: US$7bn ([10-K](https://www.sec.gov/Archives/edgar/data/0000723125/000072312526000023/mu-20260903.htm)).
- "Vast majority" of CY2027 HBM bit supply is agreed at significant year-on-year price increases ([prepared remarks](https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf)).

**(d) Financial strength**
- **FY2026 (to 3 Sep 2026):** revenue US$133.2bn (+256%); DRAM US$100.68bn, NAND US$31.79bn. Business units: CMBU (cloud memory, incl. HBM) US$43.09bn, CDBU (core data center) US$37.59bn, MCBU (mobile and client) US$36.60bn, AEBU (automotive and embedded) US$15.89bn. Non-GAAP gross margin 81.1%; EPS US$75.52.
- **FQ4 2026:** revenue US$54.2bn (+379% YoY); gross margin 87.0%; operating income US$44.6bn (82.3%). Operating cash flow US$44.0bn, capex US$10.8bn, free cash flow US$33.2bn.
- **HBM margin below the rest of the company:** CMBU gross margin was 83% vs 90% at CDBU and MCBU, "offset by higher HBM mix".
- **Inventory:** US$10.4bn (129 days).
- **Balance sheet:** cash and investments US$73.5bn, debt US$5.2bn, net cash US$68.3bn; BBB+ at all three agencies.
- **FQ1 FY27 guidance:** US$61.5bn ± 1.5bn revenue, ~86.25% gross margin.
- Source: [prepared remarks](https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf)
- **FY2026 cash flow and capex:** operating cash flow US$89.675bn; PP&E spending US$30.71bn, less US$3.32bn of government incentives. FY2027 capex net of incentives is ~US$11.5bn in FQ1 and ~US$25bn in H1, "higher in the second half" ([10-K](https://www.sec.gov/Archives/edgar/data/0000723125/000072312526000023/mu-20260903.htm)).
- **Customer concentration:** no customer reached 10% of revenue in FY2026. One customer was 17% in FY2025 (mainly CMBU) and one was 10% in FY2024. The top ten are "approximately one-half" of revenue.
- **Revenue by customer headquarters, FY2026:** US US$91.3bn (68.6%), Taiwan US$16.95bn, mainland China US$8.34bn (6.3%), Hong Kong US$6.29bn (4.7%), other Asia-Pacific US$5.78bn, Japan US$2.07bn, Europe US$1.72bn.
- **Long-lived assets:** Taiwan US$27.6bn, US US$14.5bn, Singapore US$12.3bn, Japan US$7.2bn, Malaysia US$1.2bn, India US$0.6bn, China US$0.5bn. "A majority of our DRAM production output in 2026 was from our fabrication facilities in Taiwan."
- Employees: ~61,000. Source for this and the three bullets above: [10-K](https://www.sec.gov/Archives/edgar/data/0000723125/000072312526000023/mu-20260903.htm)

**(e) Resilience**
- **China:** the CAC (China's Cyberspace Administration) ban on purchases by critical-infrastructure operators, in place since May 2023, still constrains Micron in China.
- **Tariffs:** the Section 232 semiconductor investigation, opened 14 Apr 2025, had an unknown outcome at 10-K filing.
- **Competition:** Micron warns of state-backed competition from CXMT and YMTC. It also warns that if HBM demand weakens and suppliers shift capacity to conventional DRAM, "this could result in a significant increase in conventional DRAM supply".
- Source for the above: [10-K](https://www.sec.gov/Archives/edgar/data/0000723125/000072312526000023/mu-20260903.htm)
- Management: "even at floor prices, we expect margins meaningfully above any prior cycle peak margins" (company claim, unconfirmed; [Investing.com Micron transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-micron-tops-q4-2026-estimates-as-demand-stays-hot-93CH-4925992)).

### Cited Findings — cross-company export controls (China)
- **BIS rule of 2 Dec 2024 (primary):**
  - New controls on US-origin HBM and on foreign-produced HBM subject to US rules under the advanced-computing foreign direct product rule. This reaches Korean-made HBM.
  - "Certain HBM will be eligible for authorization under new License Exception HBM."
  - 140 Entity List additions, including Chinese fabs and tool makers.
  - Effective 2 Dec 2024; some compliance dates 31 Dec 2024.
  - The release does not state the technical thresholds.
  - Source: [BIS press release, 2 Dec 2024](https://www.bis.gov/press-release/commerce-strengthens-export-controls-restrict-chinas-capability-produce-advanced-semiconductors-military)
- **Korean makers' China fabs:**
  - VEU status ended 31 Dec 2025; SK hynix holds an annual BIS licence for 2026.
  - SK hynix halted sales to Huawei from Sept 2020.
  - BIS guidance (May 2025) warned that using Chinese-made advanced chips risks violating US controls.
  - Source: [SK hynix 424B4](https://www.sec.gov/Archives/edgar/data/0002120882/000119312526299963/d32785d424b4.htm)
- **Micron:** the CAC ban (May 2023) still constrains it; "the U.S. government has in the past and continues to restrict U.S. firms, including us, from selling products ... to certain of our customers" ([Micron 10-K](https://www.sec.gov/Archives/edgar/data/0000723125/000072312526000023/mu-20260903.htm)).

### Inferences
- **Position:** all three own a physical constraint AI cannot remove — DRAM cleanroom space. HBM needs about 3x the wafer area per bit of DDR5, and about 4x for HBM4 per one secondary estimate ([Luminix (secondary)](https://www.useluminix.com/reports/industry-analysis/dram-cycle-position-analysis-peak-timing-indicators)). New fabs take 2-4 years: Micron's New York fab outputs in 2030; ID1 in mid-2027.
- **Lead:** the "judge" is the customer's qualification gate, re-run every generation. Counterpoint's analyst says each generation is "resetting leadership". So SK hynix's HBM lead is generational, not structural, as its fall from 64% to 50% in four quarters shows.
- **Revenue model:** none has service-like recurring revenue. Micron's take-or-pay agreements with deposits and price floors are the closest to recurring and the best documented, with a US$150bn backlog-like obligation.
- **Customer concentration:** it fell sharply in FY2026 as commodity DRAM prices surged — Micron went from one 17% customer to none at 10%. Concentration on NVIDIA would likely rise again if commodity prices fell. This is an inference.
- **Profit composition:** all three are now mostly price-driven. Counterpoint's Q3 2026 figures show DRAM bits +4% against revenue +369% YoY.

### Gaps
- SK hynix's Q3 2026 preliminary figures are confirmed by 6-K. Its earnings presentation (HBM narrative) and 2026 capex total were not read. None of the three discloses HBM revenue.
- Return on invested capital was not found for any of the three. Samsung's ROE is the deck figure; others would have to be computed.
- Samsung's customer and geographic revenue split, the size of its China fabs (Xi'an NAND, Suzhou packaging), and its export-licence status were not verified.
- Micron's FY2023 downturn figures were not in the FY2026 10-K excerpts read.
- Samsung's ten multi-year contracts and SK hynix's LTAs have no disclosed deposit amounts.

---

## (3) Path forward — transitions, said vs done, funding, verdicts

### Takeaway
For memory makers, the transition that matters is (3), solder-bump/thermo-compression stacking to hybrid bonding, and it has slipped. All three shipped HBM4 without hybrid bonding. The earliest insertion is now 16-high HBM4E, around 2027-28, and possibly HBM5 around 2029-30. JEDEC's relaxed height limits remove the urgency. Transitions (4) and (5) (interposers/glass and cooling) affect HBM through packaging partners and stack thermals. Transitions (1), (2) and (6) are indirect. All three makers are fully funded through a one-to-two-year slip.

### Cited Findings
**Industry facts on bonding (transition 3)**
- Samsung and SK hynix kept thermo-compression bonding for HBM4, and 16-high HBM4E "may be earliest adoption".
- JEDEC package height rose from 720µm (up to HBM3E) to 775µm (HBM4). JEDEC is reportedly discussing ~900µm up to 1,000µm for 20-high HBM5.
- NVIDIA's 16-high discussions are "limited"; 12-high HBM4E is expected to be mainstream.
- Non-hybrid thermal fixes are being tested for HBM5: Samsung's Heat Path Block and SK hynix's iHBM.
- Source: [TrendForce 7 Jul 2026 (citing ZDNet, Newsis)](https://www.trendforce.com/news/2026/07/07/news-samsung-sk-hynix-reportedly-reconsider-hybrid-bonding-timeline-16-high-hbm4e-may-be-earliest-adoption/)
- The HBM4 height target reportedly moved to a proposed 825-900µm, with HBM5 around 1,000µm.
- An unnamed bonder maker's June 2026 deck names 16-high HBM4E as the first insertion, with "a leading customer preparing for volume production in 2027". Some forecasts put full adoption at 2029-2030 with HBM5.
- Source: [VLSI.kr bonding battle (secondary)](https://www.vlsi.kr/en/hbm4-bonding-battle-en/)

**SK hynix — must get through (3), plus custom base dies and HBF**
- **Said:** hybrid bonding "in earnest" at HBM4E or HBM5 above 20 layers; custom HBM with major customers; HBF "medium to long term"; supply constrained through 2030 ([VLSI.kr bonding](https://www.vlsi.kr/en/hbm4-bonding-battle-en/); [Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-sk-hynix-posts-record-q3-2026-results-shares-jump-after-hours-93CH-4977343)).
- **Done — technology:** 12-high hybrid-bonding validation completed (technical leader, Apr 2026); HBM4E 12-high samples (Jun 2026); 16-high 48GB HBM4 with a TSMC 12nm base die shown at CES 2026 (VLSI.kr bonding article).
- **Done — capacity:**
  - M15X cleanroom opened Oct 2025, wafer input Q1 2026, full capacity by end-2026.
  - Yongin fab 1 under construction since Feb 2025, phase-1 cleanroom Q1 2027.
  - P&T7 packaging plant by end-2027; Indiana packaging plant H2 2028.
  - Sources: [424B4](https://www.sec.gov/Archives/edgar/data/0002120882/000119312526299963/d32785d424b4.htm); [Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-sk-hynix-posts-record-q3-2026-results-shares-jump-after-hours-93CH-4977343)
  - Conflicting secondary dates — Indiana cleanroom Oct 2028 with HBM mass production H2 2029, Yongin first cleanroom June 2029 ([IntuitionLabs](https://intuitionlabs.ai/articles/hbm-dram-ai-memory-demand)). The prospectus dates are preferred.
- **Done — equipment and slips:** a KRW 44.2bn Hanmi thermo-compression bonder order (Jun 2026) to ramp HBM4 ([TrendForce HBM4 tag listing](https://www.trendforce.com/news/2026/06/09/news-sk-hynix-reportedly-places-44-2bn-won-tc-bonder-order-with-hanmi-accelerating-hbm4-ramp-up/), headline only). HBM4 volume slipped to Q3 2026 (TrendForce, above).
- **Funded:** yes — net cash KRW 98.7tn and a US equity raise in July 2026.

**Samsung — must get through (3) and custom base dies (already in-house)**
- **Said:** HBM4E mass production H1 2027; partial hybrid copper bonding (HCB) commercialisation at HBM4E; multi-year contracts covering 60-70% of capacity.
- **Done:** first HBM4 mass production (Feb 2026); first HBM4E samples (May 2026); HCB samples shipped before Jan 2026; GTC 2026 claim that HCB supports 16+ layers with >20% lower thermal resistance (company claim, unconfirmed); NVIDIA and AMD qualifications; 2026 capex KRW 84.4tn; reported Onyang packaging groundbreaking (Nov 2026, unconfirmed).
- Sources: [VLSI.kr bonding](https://www.vlsi.kr/en/hbm4-bonding-battle-en/); [IntuitionLabs](https://intuitionlabs.ai/articles/hbm-dram-ai-memory-demand); [TrendForce 29 May 2026](https://www.trendforce.com/news/2026/05/29/news-samsung-starts-shipping-industry-first-hbm4e-samples-three-months-after-hbm4-mass-production-performance-up-over-20/); [Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-samsung-electronics-posts-record-q3-2026-profit-93CH-4981365)
- **Funded:** yes — net cash KRW 197.6tn.

**Micron — must get through (3) and custom base dies**
- **Said:** HBM4E ramp in CY2027, including NVHBM with NVIDIA; next DRAM node in H2 2027; ID1 output mid-2027; ID2 late 2028; New York 2030; Japan expansion late 2028; Taiwan Tongluo mid-2027; Singapore HBM packaging early 2027 ([prepared remarks](https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf)).
- **Done:** HBM4 volume production (Mar 2026); HBM4 16-high samples; Tongluo fab bought (US$1.8bn, Mar 2026) with a second cleanroom under construction; Hiroshima cleanroom ground broken (Jul 2026); Singapore NAND fab ground broken (Jan 2026); India plant shipping (2026) ([10-K](https://www.sec.gov/Archives/edgar/data/0000723125/000072312526000023/mu-20260903.htm)).
- **Not found:** no hybrid-bonding plan or result disclosed in any source reviewed.
- **Funded:** yes — net cash US$68.3bn plus US$12.75bn of customer deposits.

### Inferences — suggested verdicts
- **SK hynix — coherent.** It has a credible successor (HBM4E samples on time; hybrid bonding validated), a funded capacity plan and LTAs. The weak point is execution timing: HBM4 slipped about a quarter and share is falling. What must go right: HBM4E qualification for NVIDIA Rubin Ultra (2027), keeping a majority of NVIDIA allocation, the TSMC base-die partnership for custom HBM, and labour peace.
- **Samsung (memory) — coherent; group — partly coherent.** The HBM turnaround is shown by outside data (share 15% → 33%; first to HBM4/HBM4E). The group remains a memory-cycle bet: DX lost money in Q3 2026 and Foundry depends on HBM base dies and 2nm wins. What must go right: HBM4E yield and qualification in H1 2027, HCB working at HBM4E, and pricing parity with SK hynix.
- **Micron — coherent.** It has a credible HBM4E/NVHBM successor in 2027 and the best-funded, most contract-backed expansion plan. Its HBM share is smallest and its hybrid-bonding path is undisclosed. What must go right: NVHBM qualification, the Singapore HBM packaging ramp (early 2027) and Tongluo shipments (mid-2027).
- **Slip tolerance:** the hybrid-bonding slip is a non-event for revenue in 2026-2028. All three meet HBM4/HBM4E specifications with incumbent bonding under the relaxed JEDEC heights. The risk is that a maker that bets early on hybrid bonding (Samsung's partial HCB at HBM4E) takes a yield hit. This is an inference.

### Gaps
- Each maker's bonding method for 16-high HBM4 was not confirmed.
- JEDEC's final decision on HBM4E/HBM5 package height was not found; only "under discussion" reports.
- Micron's hybrid-bonding plans were not found.
- Silicon-interposer-to-glass (4), two-phase cooling (5) and 800V power (6) have no maker-specific evidence in the sources reviewed. The KAIST/TERA roadmap places glass interposers at HBM6, around 2032 ([SourceBySpec (secondary)](https://www.sourcebyspec.com/news/hbm4-to-hbm8-demand-outlook-2026-2030-capacity-pricing-and-accelerator.html)).

---

## (4) Suggested ordering of key companies by quality alone

### Takeaway
1 (tie) SK hynix = Micron; 3 Samsung Electronics (group). Samsung's memory division on its own would tie with the other two. CXMT ranks well below, given state backing, export-control exposure and no confirmed HBM.

### Cited Findings (basis)
- SK hynix: highest operating margin (79.7% Q3 2026), HBM revenue leader (50% Q2 2026), LTAs over 50% of 2027-28 capacity. Against it: an eroding share and an HBM4 slip; the biggest China manufacturing footprint and China revenue (19.7-24.3%); the largest single customer (23.9% of 2025). Sources as in section (2).
- Micron: operating margin 82.3% (FQ4); 26 take-or-pay agreements with ~US$150bn of obligations and US$12.75bn of deposits; no customer at 10%; China long-lived assets only US$0.5bn. Against it: the smallest HBM share (18%), a majority of DRAM output in Taiwan, and the CAC ban. Sources as in section (2).
- Samsung: strongest HBM momentum (+18 points of share in a year) and in-house base die. Against it: the group outside memory was loss-making or marginal in Q3 2026 (DX −KRW 0.8tn), and its HBM3E history includes late qualification at NVIDIA. Sources as in section (2).

### Inferences
- SK hynix and Micron cannot be separated on current evidence. SK hynix wins on HBM position and margin; Micron wins on contract quality, customer and geographic diversification, and China exposure.
- Ranking Samsung's memory division alone, it would tie with them on position and lead and beat both on balance sheet. It ranks third only because the ranking unit is the listed group.

### Gaps
- No return-on-capital comparison was possible.
- Customer concentration for Samsung was not found.

---

## (5) Check of the background priors

### Takeaway
- Prior 1 (sold out 2026, committed 2027, tight into 2028): confirmed and strengthened.
- Prior 2 (Micron annual cadence to 2030): only verified to 2027.
- Prior 3 (bonding slipped to 16-high HBM4E at earliest): confirmed, with risk of further slip to HBM5.
- Prior 4 (memory binding 2026-2028): confirmed for 2026-27; 2028 rests on company and analyst forecasts.
- Prior 5 (70% supply-limited through 2028; memory turns first): supported on supply, but contract-price momentum is fading fast and new capacity lands in 2027-2029.

### Cited Findings
**Prior 1 — "HBM sold out for 2026, largely committed for 2027, tight into 2028": CONFIRMED, and updated upward by the makers**
- Samsung (29 Oct 2026): 2027 HBM "already sold out at an agreed target price"; tight supply into 2028 ([transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-samsung-electronics-posts-record-q3-2026-profit-93CH-4981365)).
- Micron (30 Sep 2026): "vast majority" of CY2027 HBM bits agreed; supply tighter in 2027 and 2028 than in 2026; "do not have line of sight to when supply and demand will return to balance" ([prepared remarks](https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf)).
- SK hynix (late Oct 2026): 2027 negotiations finalised; LTAs over 50% of 2027-28 capacity; "effectively sold out through 2029"; supply constrained through 2030 (company claims) ([transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-sk-hynix-posts-record-q3-2026-results-shares-jump-after-hours-93CH-4977343)).
- Third parties: TrendForce says the HBM market is supply-constrained in 2027 (29 Sep 2026) ([TrendForce](https://www.trendforce.com/presscenter/news/20260929-13255.html)). Counterpoint says supply is tight until major new fabs produce in 2028 (5 Nov 2026) ([Counterpoint](https://counterpointresearch.com/en/insights/dram-super-cycle-nears-dollar-200b)).
- Caveat: Samsung's HBM4 price talks with NVIDIA were still reported as unfinished on 12 Nov 2026, so "sold out" may mean volume frameworks rather than final prices ([VLSI.kr daily](https://www.vlsi.kr/en/daily-silicon-2026-11-12-en/)).
- An older April 2026 private estimate saw balance in late 2027 to mid-2028 ([ravikant.dev](https://ravikant.dev/research/investments/universe/hbm-capacity)). It is now contradicted by the makers' October 2026 statements.

**Prior 2 — "Micron has a new generation every year to 2030": NOT VERIFIED beyond 2027**
- Confirmed cadence: HBM3E (majority of 2026), HBM4 volume 2026, HBM4E ramp CY2027 ([10-K](https://www.sec.gov/Archives/edgar/data/0000723125/000072312526000023/mu-20260903.htm)), and next-generation DRAM node volume in H2 2027 ([prepared remarks](https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf)).
- No Micron HBM5 or later date was found in the sources reviewed.

**Prior 3 — "Hybrid copper-to-copper bonding slipped to 16-layer HBM4E at the earliest": CONFIRMED (July-August 2026), with risk of further slip**
- 16-high HBM4E is the earliest likely adoption and "could slip further" ([TrendForce 7 Jul 2026](https://www.trendforce.com/news/2026/07/07/news-samsung-sk-hynix-reportedly-reconsider-hybrid-bonding-timeline-16-high-hbm4e-may-be-earliest-adoption/)).
- Some forecasts put full adoption at 2029-2030 with HBM5. An August 2026 Hot Chips talk said hybrid bonding would "struggle to make HBM4E" ([VLSI.kr](https://www.vlsi.kr/en/hbm4-bonding-battle-en/)).

**Prior 4 — "Memory is a binding constraint on AI computing in 2026-2028": CONFIRMED for 2026-27**
- NVIDIA is evaluating 8-Hi HBM4E and 12/8-Hi HBM4 for Rubin Ultra instead of the 12-Hi HBM4E baseline, and CSPs are evaluating lower HBM capacity for in-house ASICs because of limited HBM supply and rising cost ([TrendForce 4 Aug 2026](https://www.trendforce.com/presscenter/news/20260804-13166.html); [TrendForce 29 Sep 2026](https://www.trendforce.com/presscenter/news/20260929-13255.html)).
- Huang urged SK hynix to produce more HBM (2 Jun 2026) ([Yahoo](https://finance.yahoo.com/sectors/technology/articles/nvidia-certifies-samsung-sk-hynix-133001560.html)). Lisa Su: "Memory supply is very tight" (Oct 2026) ([Tech-Insider](https://tech-insider.org/hbm4-memory-shortage-amd-samsung-sk-hynix-price-spike-2026/)).
- Micron: server unit growth in the high teens in 2026-27, "supported by a modestly lower rate of content growth than prior expectations, amid tight memory supply" ([prepared remarks](https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf)).
- Counterpoint to the prior: one secondary estimate calls TSMC CoWoS packaging, rather than HBM DRAM, the pacing bottleneck ([ravikant.dev (unsourced estimates)](https://ravikant.dev/research/investments/universe/hbm-capacity)).

**Prior 5 — "70% that memory stays supply-limited through 2028; memory is first to turn in a pause": SUPPORTED on supply; turn risk visible**
- All three makers and Counterpoint now say tight through 2028 or later (above).
- Contract-price momentum is decelerating sharply:
  - Q1 2026 conventional DRAM +90-98% QoQ.
  - Q2 2026 +58-63% (TrendForce) or ~80% (Commercial Times).
  - Q3 2026 +13-18% forecast; ~40% per Commercial Times.
  - Q4 2026 +10-15% (TrendForce, 30 Sep) or ~20% including HBM (Commercial Times, 20 Oct).
  - Sources: [TrendForce 30 Sep 2026](https://www.trendforce.com/presscenter/news/20260930-13258.html); [TrendForce 20 Oct 2026](https://www.trendforce.com/news/2026/10/20/news-dram-prices-seen-rising-20-qoq-in-4q26-despite-slower-gains-ai-demand-tight-supply-support-outlook/); [IntuitionLabs](https://intuitionlabs.ai/articles/hbm-dram-ai-memory-demand); [Luminix](https://www.useluminix.com/reports/industry-analysis/dram-cycle-position-analysis-peak-timing-indicators)
- The 128Gb MLC NAND contract price was flat at US$30.61 in October 2026, the first pause after 21 monthly rises. Consumer demand is weak: 2026 PCs −10% to −11%, smartphones −8% to −13% (IDC/Gartner/Counterpoint) ([Tech-Insider](https://tech-insider.org/dram-record-high-nand-flat-21-months-october-2026/)).
- Luminix's probability-weighted conventional DRAM peak is about Q2 2027, with HBM peaking later on locked contracts. Supplier inventory was estimated below 10 days in September 2026 (KB Securities) ([Luminix (secondary)](https://www.useluminix.com/reports/industry-analysis/dram-cycle-position-analysis-peak-timing-indicators)).

### Inferences
- **Prior 5, supply side:** a ≥70% probability of supply-limited conditions through 2028 is consistent with every maker's guidance. The main threats are capacity landing in 2027-2029 and a demand pause. Arriving capacity includes SK hynix Yongin and Indiana, Samsung P5 and Onyang, Micron ID1, ID2, Hiroshima and Tongluo, and CXMT Shanghai.
- **Prior 5, "memory turns first":** history and current data support that conventional DRAM and NAND pricing turns first — it is already decelerating. HBM, priced annually and under LTAs, would turn later. Take-or-pay terms, deposits and floors (Micron) now cushion revenue in a pause, but only for contracted volumes; a quarter of Micron's agreement revenue is market-priced.
- **New risk to the prior:** customers' de-speccing (8-Hi stacks) shows demand is price-elastic even in a shortage.

### Gaps
- No direct evidence was found on how memory behaved in an AI-specific spending pause; none has occurred.

---

## (6) Open question — which successor ships first; who captures the value

### Takeaway
- **Order of successors:**
  1. Logic base dies (already shipping in HBM4).
  2. Custom HBM4E base dies (2027).
  3. HBM4E itself (2027).
  4. Hybrid bonding — partial at 16-high HBM4E around 2027-28, mainstream perhaps HBM5 around 2029-30.
  5. High-bandwidth flash — no product dates found.
- **Value capture:** memory makers are capturing most of it in 2026, at 72-82% operating margins, but HBM itself earns less than commodity DRAM until 2027 repricing. The integrated giant (Samsung) regained the most HBM share in 2026, helped by its in-house base die and capacity. The specialist (SK hynix) keeps the margin and NVIDIA-allocation lead.

### Cited Findings
- **Base dies already shipping:**
  - HBM4 base dies are logic: Samsung 4nm in-house ([TrendForce 23 Jun 2026](https://www.trendforce.com/news/2026/06/23/news-memory-giants-split-on-hbm4-strategy-samsung-hbm4-sales-reportedly-tops-1b-sk-hynix-slows-ramp/)), SK hynix on TSMC 12nm ([VLSI.kr](https://www.vlsi.kr/en/hbm4-bonding-battle-en/)), Micron in-house CMOS ([10-K](https://www.sec.gov/Archives/edgar/data/0000723125/000072312526000023/mu-20260903.htm)).
  - Custom HBM4E: Micron's NVHBM with NVIDIA ([prepared remarks](https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf)); SK hynix and Samsung both announced custom HBM at SEDEX, 14 Oct 2026 ([VLSI.kr](https://www.vlsi.kr/en/hbm4e-post-hbm-memory-hierarchy-war-en/)).
- **HBM4E:** 2H27 ramp (TrendForce), mass production H1 2027 (Samsung), ramp CY2027 (Micron) (sources in sections 2 and 5).
- **HBM earns less than commodity DRAM in 2026:**
  - HBM per-wafer revenue fell below DDR5 64GB RDIMM in Q1 2026, and annual HBM pricing lagged quarterly DRAM rises (TrendForce, via [SourceBySpec](https://www.sourcebyspec.com/news/hbm4-to-hbm8-demand-outlook-2026-2030-capacity-pricing-and-accelerator.html)).
  - Micron's CMBU gross margin was 83% vs 90% elsewhere ([prepared remarks](https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf)).
  - The 2027 blended HBM ASP is forecast at +121% YoY ([TrendForce](https://www.trendforce.com/presscenter/news/20260929-13255.html)).
- **Foundry's share:** Samsung's Foundry utilisation recovery is attributed mainly to HBM base dies (Chosun Biz, 3 Aug 2026) ([TrendForce](https://www.trendforce.com/news/2026/08/03/news-samsung-foundry-eyes-2h26-full-utilization-as-hbm4-base-dies-and-u-s-orders-fuel-turnaround-hopes/)). Samsung's deck credits Foundry improvement to "HBM B-Die sales growth" ([deck](https://images.samsung.com/is/content/samsung/assets/global/ir/docs/2026_3Q_conference_eng.pdf)).
- **Integrated vs specialist:** Samsung HBM share 15% → 33% (Q2-25 → Q2-26); SK hynix 64% → 50%; Micron 21% → 18% ([Counterpoint](https://counterpointresearch.com/en/insights/global-dram-and-hbm-market-share)). UBS puts 2027 bits at Samsung 41% vs SK hynix 39% ([VLSI.kr](https://www.vlsi.kr/en/bernstein-hbm-crossover-en/)).
- **High-bandwidth flash:** SK hynix proposed it at SEDEX 2026 as a tier between HBM and server DRAM for KV-cache work; endurance and latency limits are unproven ([VLSI.kr](https://www.vlsi.kr/en/hbm4e-post-hbm-memory-hierarchy-war-en/)). SK hynix management calls it "medium to long term" ([transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-sk-hynix-posts-record-q3-2026-results-shares-jump-after-hours-93CH-4977343)).

### Inferences
- **2027 HBM revenue:** 50-60% bit growth ([TrendForce 4 Aug 2026](https://www.trendforce.com/presscenter/news/20260804-13166.html)) times a 121% blended ASP rise implies roughly 3.3-3.5x HBM revenue in 2027 versus 2026. This is my arithmetic, not a published forecast. It would move HBM margins back above commodity DRAM and favour whoever holds the most qualified HBM4/HBM4E capacity.
- **Base-die value:** the logic base die shifts some value to foundries. TSMC captures it from SK hynix and possibly Micron's custom HBM4E; Samsung keeps it in-house. This structurally favours the integrated maker if base dies grow more complex.

### Gaps
- No public 2026 or 2027 HBM market-size figure from TrendForce, Yole or Omdia was retrieved. TrendForce's figures are in a paid report: [TrendForce RP260805KC3](https://www.trendforce.com/research/download/RP260805KC3).
- SanDisk's and Kioxia's high-bandwidth-flash timelines were not verified.

---

## (7) What could not be verified

### Takeaway
The biggest gaps:
- China beyond CXMT's financials and listing: Huawei, YMTC and XMC HBM efforts; CXMT's HBM progress.
- The detailed text of US BIS HBM rules (only the 2 Dec 2024 release was read) and Korean trade-ministry statements.
- Japan (Saimemory, Kioxia high-bandwidth flash).
- Absolute HBM market size.
- SK hynix's Q3 2026 earnings presentation. The preliminary figures are confirmed by 6-K; the HBM narrative is secondary.

All were affected by search tools running out: the WebSearch budget, then Exa and Firecrawl credits.

### Cited Findings
- **Leads given in the brief:**
  - (1) SK hynix saying in October 2025 that 2026 output was sold out: not read directly. It is superseded by the October 2026 claim of "effectively sold out through 2029" ([transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-sk-hynix-posts-record-q3-2026-results-shares-jump-after-hours-93CH-4977343)).
  - (2) Samsung HBM4 shipments in early 2026: CONFIRMED — mass production and shipment on 12 Feb 2026 ([TrendForce 29 May 2026](https://www.trendforce.com/news/2026/05/29/news-samsung-starts-shipping-industry-first-hbm4e-samples-three-months-after-hbm4-mass-production-performance-up-over-20/); [Tech-Insider](https://tech-insider.org/hbm4-memory-shortage-amd-samsung-sk-hynix-price-spike-2026/)).
  - (3) Micron raising FY2026 capex to about US$20bn in December 2025: the December statement was not read. It is superseded by FY2026 actual PP&E spending of US$30.71bn gross, or about US$27.4bn after US$3.32bn of incentives (my arithmetic from the [10-K](https://www.sec.gov/Archives/edgar/data/0000723125/000072312526000023/mu-20260903.htm)).
  - (4) CXMT filing for a STAR Market listing in late 2025: PARTLY VERIFIED. CXMT is now listed — its website shows "SSE:688825" ([CXMT](https://www.cxmt.com/en/news/info_22.html)). The late-2025 filing date, listing date and amount raised were not verified. The July 2025 IPO-counselling report is the only dated step found ([TrendForce](https://www.trendforce.com/news/2025/07/08/news-chinas-cxmt-reportedly-begins-ipo-counselling-aims-to-be-first-memory-chip-firm-on-a-share/)).
- A May 2025 rumour that the US was weighing adding CXMT to the Entity List (headline only; [TrendForce](https://www.trendforce.com/news/2025/05/16/news-u-s-rumored-to-mull-adding-dram-giant-cxmt-and-more-chinese-tech-firms-to-entity-list/)). Its 2026 status is unknown.

### Gaps
- **Export controls:**
  - The technical thresholds of the December 2024 BIS HBM rule, and any 2025-26 amendments. The release itself is cited in section (2); the Federal Register text was not read.
  - Whether the BIS annual licence for Korean makers' China fabs has been renewed for 2027.
  - Samsung's China-fab licence status.
  - Korean trade-ministry statements.
- **Tariffs:** the outcome of the Section 232 semiconductor tariff.
- **Customer qualifications:** HBM4 qualification at Google (Broadcom-designed TPUs), AWS Trainium 4 and Microsoft Maia beyond secondary tables. The Samsung → Google HBM4 "qualified" entry is internally inconsistent ([Silicon Analysts](https://siliconanalysts.com/tools/hbm-analysis)).
- **Supplier shares:** HBM shares for Q3 2026; Counterpoint's public summary did not break them out.
- **Capacity:** TSV/stacking capacity by supplier from an outside source. Only an unsourced private estimate was found (SK hynix ~130-150k, Samsung ~90-110k, Micron ~50-60k wafers/month in Q1 2026; [ravikant.dev](https://ravikant.dev/research/investments/universe/hbm-capacity)).
- **Prepayments:** amounts at SK hynix and Samsung.
- **Bonding:** Micron's hybrid-bonding roadmap; JEDEC's final HBM4E/HBM5 height decisions.
- **Pricing:** 2027 HBM contract prices by supplier. Only press reports (SK hynix HBM4 "mid-$500s per stack" to NVIDIA) and analyst estimates (HBM4 12-high ~US$550-600 in 2026 → ~US$1,300 in 2027) were found ([VLSI.kr](https://www.vlsi.kr/en/daily-silicon-2026-11-12-en/); [Silicon Analysts](https://siliconanalysts.com/tools/hbm-analysis); [Tech-Insider](https://tech-insider.org/hbm4-memory-shortage-amd-samsung-sk-hynix-price-spike-2026/)).
- **Unchecked regions and companies:** Europe, Israel and India (beyond Micron); Taiwan's Winbond and AP Memory. These were not checked in local-language sources.

---

## (8) Sources (URL, date published or period covered)

### Cited Findings
**Primary**
- Samsung Electronics, 3Q 2026 earnings call deck, 29 Oct 2026 — https://images.samsung.com/is/content/samsung/assets/global/ir/docs/2026_3Q_conference_eng.pdf
- Micron, FQ4 FY26 prepared remarks, 30 Sep 2026 — https://s25.q4cdn.com/621799436/files/doc_financials/2026/q4/Q4-FY26-Prepared-Remarks.pdf
- Micron, Form 10-K, fiscal year ended 3 Sep 2026 (filed Oct 2026) — https://www.sec.gov/Archives/edgar/data/0000723125/000072312526000023/mu-20260903.htm
- SK hynix, Form 6-K preliminary results Q3 2026, 28 Oct 2026 — https://www.sec.gov/Archives/edgar/data/2120882/000119312526434994/d162547d6k.htm
- SK hynix, Form 6-K Solidigm clarifications, 23 Oct 2026 — https://www.sec.gov/Archives/edgar/data/2120882/000119312526429184/d159239d6k.htm — and 29 Oct 2026 — https://www.sec.gov/Archives/edgar/data/2120882/000119312526436872/d183583d6k.htm
- SK hynix, Form 6-K semi-annual report, H1 2026 — https://www.sec.gov/Archives/edgar/data/0002120882/000119312526354777/d147827d6k.htm
- US BIS press release on advanced-semiconductor and HBM controls, 2 Dec 2024 — https://www.bis.gov/press-release/commerce-strengthens-export-controls-restrict-chinas-capability-produce-advanced-semiconductors-military
- CXMT news page (G5 DRAM announcement, 20 Sep 2026; ticker SSE:688825) — https://www.cxmt.com/en/news/info_22.html
- stockanalysis.com, CXMT financials, annual to FY2025 and TTM to 30 Sep 2026 (secondary aggregator of filings; fundamentals only) — https://stockanalysis.com/quote/sha/688825/financials/
- SK hynix, Form F-1 (filed 24 Jun 2026) — https://www.sec.gov/Archives/edgar/data/0002120882/000119312526280172/d32785df1.htm
- SK hynix, Form 424B4 prospectus (July 2026; data to Q1 2026) — https://www.sec.gov/Archives/edgar/data/0002120882/000119312526299963/d32785d424b4.htm

**Market research (secondary)**
- Counterpoint, Global DRAM and HBM market share, 2 Sep 2026 — https://counterpointresearch.com/en/insights/global-dram-and-hbm-market-share
- Counterpoint, DRAM super-cycle nears $200B (Q3 2026), 5 Nov 2026 — https://counterpointresearch.com/en/insights/dram-super-cycle-nears-dollar-200b
- Electronics Weekly, Q3 DRAM revenue up 369%, Nov 2026 — https://www.electronicsweekly.com/news/business/q3-dram-revenue-up-369-yoy-2026-11/
- TrendForce press release, 2027 HBM blended ASP +121%, 29 Sep 2026 — https://www.trendforce.com/presscenter/news/20260929-13255.html
- TrendForce press release, 4Q26 contract prices, 30 Sep 2026 — https://www.trendforce.com/presscenter/news/20260930-13258.html
- TrendForce press release, HBM bit shipments 2027 / Rubin Ultra configs, 4 Aug 2026 — https://www.trendforce.com/presscenter/news/20260804-13166.html
- TrendForce HBM Industry Analysis 3Q26 (paid; summary only), 5 Aug 2026 — https://www.trendforce.com/research/download/RP260805KC3

**Trade press (secondary)**
- TrendForce news:
  - Hybrid bonding timeline, 7 Jul 2026 — https://www.trendforce.com/news/2026/07/07/news-samsung-sk-hynix-reportedly-reconsider-hybrid-bonding-timeline-16-high-hbm4e-may-be-earliest-adoption/
  - Samsung HBM4 yield, 10 Aug 2026 — https://www.trendforce.com/news/2026/08/10/news-samsungs-hbm4-yield-reportedly-hits-80-as-race-to-supply-vera-rubin-heats-up-sk-hynix-labor-talks-add-a-twist/
  - HBM4 strategy split, 23 Jun 2026 — https://www.trendforce.com/news/2026/06/23/news-memory-giants-split-on-hbm4-strategy-samsung-hbm4-sales-reportedly-tops-1b-sk-hynix-slows-ramp/
  - Samsung HBM4E samples, 29 May 2026 — https://www.trendforce.com/news/2026/05/29/news-samsung-starts-shipping-industry-first-hbm4e-samples-three-months-after-hbm4-mass-production-performance-up-over-20/
  - Samsung Foundry base dies, 3 Aug 2026 — https://www.trendforce.com/news/2026/08/03/news-samsung-foundry-eyes-2h26-full-utilization-as-hbm4-base-dies-and-u-s-orders-fuel-turnaround-hopes/
  - CXMT earnings, 20 Oct 2026 — https://www.trendforce.com/news/2026/10/20/news-cxmts-earnings-boom-faces-test-as-3q-profit-growth-slows-to-1-4-qoq-whats-behind-the-slowdown/
  - 4Q26 DRAM +20%, 20 Oct 2026 — https://www.trendforce.com/news/2026/10/20/news-dram-prices-seen-rising-20-qoq-in-4q26-despite-slower-gains-ai-demand-tight-supply-support-outlook/
  - CXMT IPO counselling, 8 Jul 2025 — https://www.trendforce.com/news/2025/07/08/news-chinas-cxmt-reportedly-begins-ipo-counselling-aims-to-be-first-memory-chip-firm-on-a-share/
  - CXMT Entity List rumour, 16 May 2025 — https://www.trendforce.com/news/2025/05/16/news-u-s-rumored-to-mull-adding-dram-giant-cxmt-and-more-chinese-tech-firms-to-entity-list/
  - SK hynix Hanmi order, 9 Jun 2026 (headline only) — https://www.trendforce.com/news/2026/06/09/news-sk-hynix-reportedly-places-44-2bn-won-tc-bonder-order-with-hanmi-accelerating-hbm4-ramp-up/
- Investing.com AI-assisted transcripts:
  - SK hynix Q3 2026 (late Oct 2026) — https://www.investing.com/news/transcripts/earnings-call-transcript-sk-hynix-posts-record-q3-2026-results-shares-jump-after-hours-93CH-4977343
  - Samsung Q3 2026 (29 Oct 2026) — https://www.investing.com/news/transcripts/earnings-call-transcript-samsung-electronics-posts-record-q3-2026-profit-93CH-4981365
  - Micron Q4 FY26 (30 Sep 2026) — https://www.investing.com/news/transcripts/earnings-call-transcript-micron-tops-q4-2026-estimates-as-demand-stays-hot-93CH-4925992
- VLSI.kr:
  - SK hynix Q3 facts, 28 Oct 2026 — https://www.vlsi.kr/en/sk-hynix-q3-2026-earnings-14-facts-en/
  - HBM4 three-way race, 2026 — https://www.vlsi.kr/en/hbm4-three-way-race-en/
  - HBM4 bonding battle, 2026 — https://www.vlsi.kr/en/hbm4-bonding-battle-en/
  - HBM4E/HBF hierarchy, 17 Oct 2026 — https://www.vlsi.kr/en/hbm4e-post-hbm-memory-hierarchy-war-en/
  - Bernstein crossover / analyst share forecasts, Oct 2026 — https://www.vlsi.kr/en/bernstein-hbm-crossover-en/
  - Daily Silicon, 12 Nov 2026 — https://www.vlsi.kr/en/daily-silicon-2026-11-12-en/
  - Samsung Q3 facts — https://www.vlsi.kr/en/samsung-q3-2026-earnings-11-facts-en/
- Yahoo/Investing.com, NVIDIA certifies all three for Vera Rubin, 5 Jun 2026 — https://finance.yahoo.com/sectors/technology/articles/nvidia-certifies-samsung-sk-hynix-133001560.html
- Yahoo/Zacks, Micron HBM4 ramp, 13 Oct 2026 (company claims only used) — https://finance.yahoo.com/markets/stocks/articles/microns-hbm4-ramp-higher-pricing-123300062.html
- Tech-Insider, HBM4 shortage / AMD, Oct 2026 — https://tech-insider.org/hbm4-memory-shortage-amd-samsung-sk-hynix-price-spike-2026/
- Tech-Insider, DRAM record / NAND flat, 31 Oct 2026 — https://tech-insider.org/dram-record-high-nand-flat-21-months-october-2026/
- XenoSpectrum, CXMT Q3 2026 share, 7 Nov 2026 — https://xenospectrum.com/en/cxmt-dram-share-q3-2026/
- Wccftech, CXMT Q3 2026, 6 Nov 2026 — https://wccftech.com/chinese-memory-chip-manufacturer-cxmt-struggles-in-q3-as-share-drops-to-9-amidst-aggressive-ramp-from-samsung-says-research/
- GuruFocus, Samsung Q3 2026 call highlights — https://www.gurufocus.com/news/9150265/samsung-electronics-co-ltd-wbossun-q3-2026-earnings-call-highlights-record-100-trillion-won-operating-profit-hbm4-sold-out-through-2027

**Analysts and aggregators (lower confidence)**
- Silicon Analysts HBM tracker, Oct 2026 — https://siliconanalysts.com/tools/hbm-analysis
- IntuitionLabs, HBM/DRAM demand, 2026 — https://intuitionlabs.ai/articles/hbm-dram-ai-memory-demand
- SourceBySpec, HBM4-HBM8 outlook, 28 Aug 2026 — https://www.sourcebyspec.com/news/hbm4-to-hbm8-demand-outlook-2026-2030-capacity-pricing-and-accelerator.html
- Luminix, DRAM cycle position, 30 Sep 2026 — https://www.useluminix.com/reports/industry-analysis/dram-cycle-position-analysis-peak-timing-indicators
- ravikant.dev, HBM capacity timeline, Apr 2026 (unsourced estimates) — https://ravikant.dev/research/investments/universe/hbm-capacity

### Gaps
- None of the market-research firms' underlying datasets were accessed. TrendForce, Yole and Omdia full reports are paid.
