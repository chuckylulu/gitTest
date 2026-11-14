# Shared Supply Chain and Independent Technical Evidence for AI Processors (NVIDIA, AMD, Broadcom XPUs, Google TPU, Amazon Trainium/Inferentia, Huawei Ascend, Cerebras), as of 14 November 2026

How to read these notes:
- "Today" is 14 November 2026. Each item gives the period covered or the as-of date, plus the source (publisher, title, publication date, URL).
- Provenance tags:
  - **[SUPPLIER]**: stated by a supplier (foundry, memory maker, OSAT, substrate or optics vendor).
  - **[CHIP-CO]**: a claim by one of the seven chip companies. These are included only as claims to be tested.
  - **[INDEPENDENT: who]**: measured or observed by a party the chip company does not control. MLPerf results are run by vendors but peer-reviewed by MLCommons; for SemiAnalysis InferenceX, vendor assistance is noted where SemiAnalysis disclosed it.
  - **[ESTIMATE: who]**: an analyst or industry estimate.
  - **[PRESS-UNNAMED]**: a press report citing unnamed sources.
  - **[CUSTOMER]**: a statement or paper by a buyer of the chips, such as Meta.
  - **[COMPANY-AUTHORED]**: a paper written by one of the seven chip companies.
  - **[UNOPENED]**: the figure comes from a search-result summary of the cited page and I did not open the page, so its exact wording and attribution are unverified.
- Process limitation: partway through this task the shared web-search budget for the session ran out (limit reached). After that I only fetched pages whose URLs I already had and ran no new searches. Some items below are therefore marked [UNOPENED] or listed under Gaps. A follow-up session could close them.

---

## 1A. TSMC: advanced-node and advanced-packaging capacity, 2024–2027

### Takeaway
None of the sources found give TSMC's CoWoS or N3/N2 capacity in wafers. Analyst and press estimates put CoWoS at about 35k wafers/month (wpm) in 2024 and about 70k in 2025. For end-2026 they cluster at about 115–140k wpm, with 170–200k targeted for 2027. TSMC's own statements give a CoWoS capacity CAGR above 80% for 2022–2027. In July 2026 TSMC said packaging capacity is "so tight that now it's limiting my customers' growth". N2 entered high-volume manufacturing in Q4 2025 and was 8% of wafer revenue in Q3 2026.

### Cited Findings
- **[SUPPLIER] TSMC Q3 2026 results (quarter ended 30 Sep 2026):**
  - Revenue was NT$1,494.24B (US$46.72B), up 50.9% YoY and 17.6% QoQ on an NT$ basis. Gross margin was 66.4%.
  - Wafer revenue by node: N2 8%, N3 33%, N5 28%, N7 10%. 7nm and below was 79%.
  - Q4 2026 guidance: revenue US$52.3–54.3B, gross margin 65–67%.
  - Source: [TSMC Form 6-K Exhibit 99.1, press release dated 2026-10-15 (SEC EDGAR)](https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000726/a3q26e_withguidancexfinal.htm)
- **[SUPPLIER] TSMC Q3 2026 earnings call (15 Oct 2026), as paraphrased by CRN Asia:**
  - HPC was 68% of Q3 revenue, up 22% QoQ.
  - Full-year 2026 revenue growth is now about 44% in USD.
  - 2026 capex stays at US$60–64B, of which US$13.8B was spent in Q3. Capex for 2026–2028 will be "significantly higher" than in the prior three years.
  - Annual 2nm-family capacity is expected to more than double in 2027. The 1.3-point QoQ gross-margin decline was attributed mainly to 2nm ramp dilution.
  - C.C. Wei said TSMC is already producing advanced packages at five times the reticle size. He called CoWoS customers' first choice while acknowledging a competitor with "a very competitive solution", and said demand remains well above supply.
  - TSMC is planning 2027 "prudently" because of pressure in consumer segments.
  - Source: [CRN Asia, "TSMC third quarter revenue tops guidance as CEO says AI demand still exceeds supply," 2026-10-15](https://www.crnasia.com/news/2026/components-and-peripherals/tsmc-third-quarter-revenue-tops-guidance-as-ceo-says-ai-dema). Most of the article paraphrases; its only direct quote is from CFO Wendell Huang.
- **[SUPPLIER] TSMC Q2 2026 call (16 Jul 2026), from an auto-generated transcript that contains errors:**
  - Wei: "our packaging capacity is so tight that now it's limiting my customers' growth"; "We welcome that additional flexibility in the market" (on alternative packaging suppliers); a glass-based alternative needs "about another one year to be mature".
  - N2 was 3% of Q2 wafer revenue and will dilute gross margin by about 3–4 points in 2H26. TSMC is adding three more 3nm fabs, in Taiwan, Arizona and Japan. A14 pre-production starts in 2027, with volume in 2028.
  - Capex was raised to US$60–64B from US$52–56B. Reasons given were customer demand and tool-price inflation ("Now we buy the tools with inflation price"). About 10–20% of capex goes to advanced packaging, testing, masks and other items.
  - On the supply gap, Wei said "the gap is so big" but declined to quantify it: "No, we don't have a number to share".
  - Source: [The Motley Fool, "TSM Q2 2026 Earnings Call Transcript," 2026-07-16](https://www.fool.com/earnings/call-transcripts/2026/07/16/tsm-tsm-q2-2026-earnings-call-transcript/)
- **[SUPPLIER via Reuters]** TSMC forecasts a CoWoS capacity CAGR above 80% for 2022–2027. Reuters cited TSMC's May 2026 Taiwan Technology Symposium; TrendForce relayed it. Source: [TrendForce, "TSMC CoWoS Supply-Demand Gap Reportedly Seen Narrowing from 20% to 10% by End-2026 as Capacity Expands," 2026-06-15](https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-reportedly-seen-narrowing-from-20-to-10-by-end-2026-as-capacity-expands/)
- **[SUPPLIER] TSMC Q4 2025 call (15 Jan 2026), from a translated third-party compilation (not official):**
  - "Capacity is extremely tight."
  - Advanced packaging was about 8–10% of 2025 revenue (the page gives both figures) and is expected to be "slightly above 10%" in 2026.
  - 2026 capex was set at US$52–56B: 70–80% for advanced process, 10–20% for packaging, testing, masks and other items.
  - Source: [iTiger / Guohai Securities, "TSMC (TSM.US) Q4 2025 Earnings Call Full Transcript," Jan 2026](https://www.itiger.com/news/1163623376)
- **[SUPPLIER, as cited by Next Platform]** TSMC capex was US$29.8B in 2024 and US$40.9B in 2025. Source: [The Next Platform, "AI chips drive around a third of TSMC revenues," 2026-07-16](https://www.nextplatform.com/ai/2026/07/16/ai-chips-drive-around-a-third-of-tsmc-revenues/5273929)
- **CoWoS capacity estimates.** None of these is a TSMC disclosure.
  - **[ESTIMATE: institutional investors via Commercial Times]** About 35,000 wpm "this year" (2024). Projected about 70,000 by end-2025 and about 90,000 by end-2026. Source: [TrendForce, "TSMC Ramps up CoWoS Capacity across Taiwan, Projected to Nearly Triple by 2026," 2024-12-13](https://www.trendforce.com/news/2024/12/13/news-tsmc-ramps-up-cowos-capacity-across-taiwan-projected-to-nearly-triple-by-2026/)
  - **[ESTIMATE: institutional investors via TechNews]** About 115,000–140,000 wpm by end-2026 and about 170,000 in 2027, mainly in Tainan and Chiayi. Source: [TrendForce, "TSMC Says CoWoS Offers Industry's Largest Reticle-Size Packaging amid Intel EMIB Rivalry; CoPoS Advances," 2026-04-16](https://www.trendforce.com/news/2026/04/16/news-tsmc-says-cowos-offers-industrys-largest-reticle-size-packaging-amid-intel-emib-rivalry-copos-advances/)
  - **[ESTIMATE: institutional investors via Economic Daily News]** TSMC at 120,000–140,000 wpm in 2026. OSAT partners add 50,000–60,000 wpm, so the industry approaches about 200,000 wpm. The supply–demand gap of about 20% narrows to about 10% by end-2026. TrendForce adds that TSMC plans to expand CoWoS by more than 60% in 2027. Source: [TrendForce, 2026-06-15](https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-reportedly-seen-narrowing-from-20-to-10-by-end-2026-as-capacity-expands/)
  - **[ESTIMATE: unnamed report relayed via ETNews/Mydrivers]** About 70,000 wpm in 2025 and 130,000–140,000 wpm by end-2026, with a gap of about 20% in 2026.
    - TSMC is expanding outsourcing of the CoW (chip-on-wafer) step to OSATs, with ASE named. ASE, Amkor and SPIL already perform WoS under TSMC licences.
    - Mirror Daily (June 2026) reported that ASE and SPIL, with AMD's backing, are putting 2026 capex into their own CoW lines.
    - Source: [TrendForce, "TSMC Reportedly Expands Outsourcing of Key CoWoS Front-End Step to OSATs Amid Rising NVIDIA, ASIC Demand," 2026-08-05](https://www.trendforce.com/news/2026/08/05/news-tsmc-reportedly-expands-outsourcing-of-key-cowos-front-end-step-to-osats-amid-rising-nvidia-asic-demand/)
  - **[ESTIMATE: Commercial Times analysts; Goldman Sachs]**
    - Commercial Times analysts: more than 130,000 wpm in 2026 and a 200,000 wpm target for 2027.
    - Goldman Sachs: 1.275M wafers in 2026 (about 106k/month on average), 2.73M in 2027 (+114%) and 3.48M in 2028 (+27%).
    - Also reported: TSMC is weighing CoWoS price increases of up to 20%. Liberty Times reports wafer prices rising 3–6% from January 2027. Equipment lead times are now 6–8 months, up from 3–6.
    - Source: [TrendForce, "TSMC Reportedly Eyes 20% CoWoS Price Hike, Skips Equipment Price Renegotiations Amid AI Demand Surge," 2026-10-27](https://www.trendforce.com/news/2026/10/27/news-tsmc-reportedly-eyes-20-cowos-price-hike-skips-equipment-price-renegotiations-amid-ai-demand-surge/)
  - **[PRESS] [UNOPENED]** A TrendForce headline says CoWoS-L and CoWoS-S are "reportedly fully booked". Source: [TrendForce, "TSMC's CoWoS-L/S Reportedly Fully Booked, OSAT Partners Step up with ASE's CoWoP in Focus," 2025-12-08](https://www.trendforce.com/news/2025/12/08/news-tsmcs-cowos-l-s-reportedly-fully-booked-osat-partners-step-up-with-ases-cowop-in-focus/)

### Inferences
- Four separate press relays published between April and October 2026 put TSMC's end-2026 CoWoS exit capacity at about 115–140k wpm, roughly 3.3–4x the 2024 level. Goldman's annual figure of about 106k/month on average is consistent with an exit rate in that range if capacity ramps through the year.
- TSMC's statements in July and October 2026 name packaging capacity, not front-end wafers, as the constraint on customers' growth. Its willingness to outsource CoW and its welcome of "additional flexibility" (Intel EMIB-T) point the same way.

### Gaps
- I found no TSMC capacity figures in wafers per month for N4, N3 or N2 for 2024–2027, from TSMC or from labeled analyst estimates. Only revenue shares and qualitative statements were found.
- I found no capacity split across CoWoS-S, CoWoS-L and CoWoS-R, and no SoIC capacity figures.
- Morgan Stanley's own CoWoS capacity series could not be checked directly. The only Morgan Stanley figures found are demand and allocation estimates (see 1B).

---

## 1B. CoWoS allocation estimates by customer

### Takeaway
Only analyst and press estimates exist, and they disagree. Morgan Stanley, as relayed in December 2025, put NVIDIA at about 595k of roughly 1M 2026 CoWoS wafers (about 60%). It put Broadcom at about 150k, including about 90k for Google TPU; AMD at about 105k; Amazon via Alchip at about 50k; Marvell at about 55k; and MediaTek (Google TPU) at about 20k. A Mydrivers report relayed in August 2026 put NVIDIA at 800–850k wafers of TSMC's 2026 capacity.

### Cited Findings
- **[ESTIMATE: Morgan Stanley, via a 36Kr republication of the WeChat account "Semiconductor Industry Insights"] 2026 CoWoS demand by customer:**
  - NVIDIA: about 595k wafers, about 60%. Roughly 510k are at TSMC, mainly for Rubin, and roughly 80k at Amkor and ASE/SPIL for the Vera CPU and automotive chips.
  - Broadcom: about 150k, about 15%. This comprises Google TPU about 90k (85k at TSMC plus 5k at ASE/SPIL), Meta about 50k and OpenAI about 10k.
  - AMD: about 105k, about 11%, of which roughly 80k are at TSMC for MI355 and MI400.
  - Amazon via Alchip: about 50k.
  - Marvell: about 55k, for AWS and Microsoft custom chips.
  - MediaTek: about 20k, for the Google TPU project.
  - Global demand was about 370k wafers in 2024, about 670k in 2025 and about 1M in 2026. The top customers hold more than 85% of TSMC's CoWoS.
  - Source: [36Kr, "Who Will Divide Up the CoWoS Production Capacity in 2026?," 2025-12-04](https://eu.36kr.com/en/p/3580962946874242)
- **[PRESS/ESTIMATE: Mydrivers via TrendForce]** NVIDIA reportedly reserved about 800,000–850,000 wafers of TSMC's 2026 CoWoS capacity, more than 50%. Source: [TrendForce, 2026-08-05](https://www.trendforce.com/news/2026/08/05/news-tsmc-reportedly-expands-outsourcing-of-key-cowos-front-end-step-to-osats-amid-rising-nvidia-asic-demand/)
- **[ESTIMATE: Morgan Stanley via secondary coverage] [UNOPENED]** A later Morgan Stanley share split of about 59% NVIDIA, 20% Broadcom and 9% AMD (reference year unclear). Morgan Stanley also expects AMD's CoWoS share to reach about 20% in 2027 because of the agentic CPU ramp. Sources: [Wccftech, "NVIDIA's CoWoS AI Chip Packaging Demand To Be Foreshadowed In 2027 By AMD...," date not verified](https://wccftech.com/nvidias-cowos-ai-chip-packaging-demand-to-be-foreshadowed-in-2027-by-amd-due-to-agentic-ai-cpu-ramp-says-morgan-stanley/); [Jukan on X, relaying the Morgan Stanley CoWoS allocation report, c. July 2025](https://x.com/Jukanlosreve/status/1950102624164073553)
- **[ESTIMATE: Morgan Stanley, TPU units] [UNOPENED]** 3.2M TPUs in 2026 and 5M in 2027. Morgan Stanley says Broadcom keeps the majority of high-performance TPU work, with MediaTek and possibly Marvell involved in some. Source: [KuCoin News, "Morgan Stanley Defends Broadcom's Role in Google's TPU Supply Chain, Forecasts 5M Shipments by 2027," date not verified](https://www.kucoin.com/news/flash/morgan-stanley-defends-broadcom-s-role-in-google-s-tpu-supply-chain-forecasts-5m-shipments-by-2027)
- **[PRESS] [UNOPENED]** A Taiwanese report says analysts favor MediaTek over Broadcom in the TPU supply chain and that Broadcom's "TPU v8AX" shipments have been cut. Source: [TechNews (finance), 2026-08-25](https://finance.technews.tw/2026/08/25/analysts-expect-the-semiconductor-asic-market-to-reach-a-certain-level-in-2026/)
- **[SUPPLIER]** TSMC names no customers. In October 2026 Wei said only that "all AI players" work with TSMC. Source: [CRN Asia, 2026-10-15](https://www.crnasia.com/news/2026/components-and-peripherals/tsmc-third-quarter-revenue-tops-guidance-as-ceo-says-ai-dema)

### Inferences
- In the Morgan Stanley estimate, Google TPU programs total about 110k wafers for 2026 (Broadcom-designed TPU about 90k plus MediaTek about 20k), or about 11% of 2026 demand. Amazon-linked demand runs through Alchip (about 50k) and part of Marvell's about 55k. This is my arithmetic on the estimate.
- The 800–850k NVIDIA figure would equal about 63–67% of Goldman's 1.275M-wafer 2026 capacity estimate. These numbers come from different sources and dates, so the comparison is only indicative.

### Gaps
- No supplier has confirmed any customer allocation.
- Search summaries also showed other TPU and Trainium unit estimates that I could not tie to a page I opened, so they are not cited here: JPMorgan, about 3.7M TPUs in 2026 and about 2.1M Trainium in 2026 (1.5M Trn3 plus 0.6M Trn2); GF Securities, 4.5M TPUs in 2026 and 7.9M in 2027; TrendForce, 5M TPUs in 2027 and 7M in 2028; Counterpoint, about 400k "TPU v8" units in 2026. Their definitions clearly differ.

---

## 1C. TSMC's own statements on AI-accelerator revenue share and growth

### Takeaway
In January 2026 TSMC raised its AI-accelerator revenue CAGR to the "mid-to-high 50s" percent, from the mid-40s. Secondary accounts disagree on whether AI accelerators were a "high-teens" percent or 15% of 2025 revenue. In July and October 2026 TSMC gave no updated figure; in July Wei said only that the trajectory is getting "stronger and stronger". The Next Platform estimates that AI chips were about a third of TSMC's revenue in Q2 2026.

### Cited Findings
- **[SUPPLIER via secondary summaries] [UNOPENED]** On 15 Jan 2026 TSMC raised its AI-accelerator revenue CAGR to "mid-to-high 50%" for 2024–2029, up from the previous mid-40%. AI accelerators were described as a "high-teens percent" of 2025 total revenue. Sources: [Futurum Group, "TSMC Q4 FY 2025 Results and FY 2026 Outlook Signal AI-Led Growth," Jan 2026](https://futurumgroup.com/insights/tsmc-q4-fy-2025-results-and-fy-2026-outlook-signal-ai-led-growth); [Creative Strategies, "The Reordering To AI/HPC: TSMC's 2026 Outlook and Beyond," Jan 2026](https://creativestrategies.com/?p=10415)
  - Conflicting account: the Guohai editor's summary says AI accelerators "accounted for 15% of TSMC's total revenue in 2025". Source: [iTiger/Guohai, Jan 2026](https://www.itiger.com/news/1163623376)
  - Conflicting base period: The Next Platform describes the January guidance as a mid-to-high 50% CAGR "for 2026–2030". Source: [The Next Platform, 2026-07-16](https://www.nextplatform.com/ai/2026/07/16/ai-chips-drive-around-a-third-of-tsmc-revenues/5273929)
- **[SUPPLIER]** 2026 revenue-growth guidance was "approaching 30%" in USD in January 2026, with a long-term revenue CAGR of about 25% for 2024–2029 ([iTiger/Guohai, Jan 2026](https://www.itiger.com/news/1163623376)). By October 2026 it was about 44% ([CRN Asia, 2026-10-15](https://www.crnasia.com/news/2026/components-and-peripherals/tsmc-third-quarter-revenue-tops-guidance-as-ceo-says-ai-dema)).
- **[SUPPLIER] 16 Jul 2026 call:**
  - Wei declined to give a new CAGR: "let me give you not a number, but it's stronger and stronger".
  - He expects demand to stay strong "all the way to probably 2029, 2030", though he was unsure whether there would be a dip in between.
  - On agentic AI lifting CPU demand: "they are almost all TSMC's customers". TSMC is working to "balance the CPU, GPU, XPUs ratio".
  - Source: [The Motley Fool transcript, 2026-07-16](https://www.fool.com/earnings/call-transcripts/2026/07/16/tsm-tsm-q2-2026-earnings-call-transcript/)
- **[SUPPLIER] 15 Oct 2026 call:** No AI-accelerator share or CAGR was disclosed. Demand was described as supported by AI accelerators, plus agentic-AI CPUs and networking chips. Source: [CRN Asia, 2026-10-15](https://www.crnasia.com/news/2026/components-and-peripherals/tsmc-third-quarter-revenue-tops-guidance-as-ceo-says-ai-dema)
- **[ESTIMATE: The Next Platform]** Q2 2026 AI-chip revenue was about US$13.31B (+68.3% YoY), roughly one-third of Q2 revenue of US$40.2B and about half of HPC revenue (US$26.53B, +47.1% YoY). The article says TSMC stopped disclosing this figure "several quarters ago". Source: [The Next Platform, 2026-07-16](https://www.nextplatform.com/ai/2026/07/16/ai-chips-drive-around-a-third-of-tsmc-revenues/5273929)
- Source conflict: Q2 2026 revenue appears as US$40.2B (The Next Platform) and as US$39.62B in some other summaries [UNOPENED].

### Inferences
- From the second half of 2026 TSMC has shifted from quantified AI-accelerator guidance to qualitative statements. Any company claim that cites a TSMC AI percentage should be checked against the January 2026 statement, which is the latest quantified one found.

### Gaps
- I did not retrieve TSMC's January 2025 statement on AI accelerators' share of 2024 revenue or its original mid-40% CAGR statement; only the "prior mid-40%" reference above was found.
- I could not open TSMC's official transcripts. Third-party transcripts and compilations were used, and they contain errors.

---

## 1D. TSMC Arizona (fabs and packaging) and what TSMC said about customers and demand

### Takeaway
TSMC's second Arizona fab is due for volume production in Q3 2027. In July 2026 TSMC announced an additional US$100B for Arizona, including advanced-packaging fabs. TSMC's own Arizona packaging is reported to start in 2028 by one account and 2029 by another. Until then, US packaging runs through a 10-year Amkor agreement signed in June 2026. TSMC did not name customers on its 2026 calls.

### Cited Findings
- **[SUPPLIER] Jan 2026 (Guohai compilation):** Construction of Arizona phase 2 is complete, tool installation follows in 2026, and mass production is targeted for 2H 2027. Permits are being sought for a fourth fab, which will also be the first advanced-packaging facility. Wei: "we must accelerate our fab expansion in Arizona". Source: [iTiger/Guohai, Jan 2026](https://www.itiger.com/news/1163623376)
- **[SUPPLIER] 16 Jul 2026:** TSMC will "announce an additional $100 billion investment in Arizona" for "several more semiconductor logical wafer fab for 2 nm and below technologies" plus advanced-packaging fabs. "It probably additional four more fabs will be built", front-end and back-end; the schedule "will depend on the market situation". Source: [The Motley Fool transcript, 2026-07-16](https://www.fool.com/earnings/call-transcripts/2026/07/16/tsm-tsm-q2-2026-earnings-call-transcript/)
- **[SUPPLIER] 15 Oct 2026:** The second Arizona fab is to start volume production in Q3 2027, slightly ahead of schedule. Overseas-fab gross-margin dilution is now expected to be closer to 2%, widening to 3–4% later in the five-year period. Source: [CRN Asia, 2026-10-15](https://www.crnasia.com/news/2026/components-and-peripherals/tsmc-third-quarter-revenue-tops-guidance-as-ceo-says-ai-dema)
- **[SUPPLIER/OSAT] [UNOPENED]** June 2026: TSMC and Amkor signed a 10-year agreement under which TSMC buys advanced packaging and test services from Amkor, focused on Arizona. It builds on an October 2024 MOU under which Amkor's Peoria facility packages for customers of TSMC's Phoenix fab, covering technologies including InFO and CoWoS. Reports disagree on when TSMC's own Arizona packaging campus starts production: 2028 (Reuters, via TrendForce) or 2029 (another report). Sources: [TrendForce, "TSMC, Amkor Forge 10-Year Arizona Advanced Packaging Partnership...," 2026-06-17](https://www.trendforce.com/news/2026/06/17/news-tsmc-amkor-forge-10-year-arizona-advanced-packaging-partnership-to-complete-the-u-s-chip-supply-chain/); [RCR Wireless, "TSMC, Amkor strike chip packaging deal at planned US plant," 2024-10-04](https://www.rcrwireless.com/20241004/featured/tsmc-amkor-strike-chip-packaging-deal-at-planned-us-plant)
- **[SUPPLIER] Demand statements:**
  - July 2026: strong demand signals come from "Our customers and customers' customer, who are mainly the cloud service provider". TSMC is also "checking the AI data centers of progress, the building, the location, the demand" to avoid chips ending up in inventory. Source: [The Motley Fool transcript, 2026-07-16](https://www.fool.com/earnings/call-transcripts/2026/07/16/tsm-tsm-q2-2026-earnings-call-transcript/)
  - October 2026: "all AI players" work with TSMC. Source: [CRN Asia, 2026-10-15](https://www.crnasia.com/news/2026/components-and-peripherals/tsmc-third-quarter-revenue-tops-guidance-as-ceo-says-ai-dema)

### Inferences
- Any AI accelerator front-end-fabbed in Arizona before about 2028 would still need CoWoS-class packaging in Taiwan or at Amkor Arizona. This follows from the timelines above.

### Gaps
- I found no statement from TSMC about any named AI customer in 2026.
- I could not confirm the reported total US investment of US$265B from a page I opened.

---

## 1E. TSMC's exposure to Huawei via Sophgo, and the potential penalty

### Takeaway
In April 2025 Reuters reported, citing two people familiar with the matter, that TSMC could face a US penalty of US$1B or more. The case concerns a TSMC-made die that reached Huawei via Sophgo. I found no public resolution. TechInsights later (October 2025) found TSMC dies in several Ascend 910C samples, and SemiAnalysis estimated that more than 2.9M TSMC-fabricated Ascend dies reached Huawei.

### Cited Findings
- **[PRESS-UNNAMED: Reuters] [UNOPENED]** April 2025:
  - TSMC "could face a penalty of $1 billion or more" to settle a Commerce Department export-control probe over a chip it made that ended up in a Huawei AI processor. The figure reflects rules allowing fines of up to twice the value of the violating transactions.
  - Commerce has been examining TSMC's work for Sophgo, which was entity-listed in January 2025.
  - TSMC said it is committed to complying with the law and has not supplied Huawei since mid-September 2020.
  - The precedent cited is BIS's US$300M penalty on Seagate in 2023.
  - Sources: [BusinessWorld (Reuters), "TSMC could face $1 billion or more fine from US probe, sources say," Apr 2025](https://www.bworldonline.com/?p=664911); [Korea JoongAng Daily, "TSMC may face $1B fine in U.S. after chip found in Huawei AI processor," Apr 2025](https://www.koreajoongangdaily.com/world/tsmc-may-face-1b-fine-in-us-after-chip-found-in-huawei-ai-processor/12281548)
- **[INDEPENDENT: TechInsights teardown, reported by Bloomberg]** 3 Oct 2025: TechInsights found components from TSMC, Samsung and SK hynix in "multiple samples" of the Ascend 910C. It concluded that TSMC manufactured the dies and found an older generation of HBM. Source: [Bloomberg (Bloomberg Law), "Huawei Used TSMC, Samsung, SK Hynix Components in Top AI Chips," 2025-10-03](https://news.bloomberglaw.com/international-trade/huawei-used-tsmc-samsung-sk-hynix-components-in-top-ai-chips)
- **[ESTIMATE: SemiAnalysis]** 8 Sep 2025:
  - Huawei received more than 2.9M Ascend dies fabricated at TSMC, usable for both the 910B and 910C. SemiAnalysis expected this die bank to run out within about 9 months.
  - A Kunpeng 930 CPU was reportedly made on TSMC 5nm through shell-company access.
  - The article does not name Sophgo.
  - Source: [SemiAnalysis, "Huawei Ascend Production Ramp," 2025-09-08](https://newsletter.semianalysis.com/p/huawei-ascend-production-ramp)

### Inferences
- Both the teardown and SemiAnalysis's die-bank estimate imply that Ascend output in 2024–2025 depended partly on pre-existing or diverted TSMC dies. This is consistent with TSMC's statement that it has not supplied Huawei directly since September 2020, with supply reaching Huawei indirectly.

### Gaps
- I found no outcome of the Commerce investigation (settlement, charging letter or penalty) as of 14 Nov 2026. The search budget ran out before a targeted search could be made.
- I did not open a primary TechInsights page on the October 2024 Ascend 910B finding.

---

## 2A. HBM supply and "sold-out" status (SK hynix, Samsung, Micron)

### Takeaway
- SK hynix (28 Oct 2026) says its DRAM and HBM volumes are "effectively sold out" through 2029. Long-term agreements cover more than 50% of its 2027–28 capacity, and customers want more than twice what it can supply.
- Micron (late Sept 2026) says it has agreements covering the "vast majority" of its calendar 2027 HBM bit supply.
- I found no "sold-out" statement from Samsung.

### Cited Findings
- **[SUPPLIER] SK hynix 3Q25 results (29 Oct 2025):**
  - SK hynix had "completed discussions with key customers regarding HBM supply for next year" (2026) and "already secured full customer demand for its entire DRAM and NAND production for next year".
  - HBM4 completed development in September 2025 and entered mass production, with shipments from Q4 2025 and "full-scale sales expansion planned for next year".
  - Source: [SK hynix Newsroom, "SK hynix Announces 3Q25 Financial Results," 2025-10-29](https://news.skhynix.com/sk-hynix-announces-3q25-financial-results/)
- **[SUPPLIER] SK hynix Q3 2026 call (28 Oct 2026):**
  - "our DRAM and HBM volumes for the next 3 years through 2029 are effectively sold out". This combines LTA volume with volume still under discussion that is "highly likely to come through".
  - "we have signed LTAs with 14 key customers, including major global CSPs". LTA volume is "more than 50% of our total capacity for 2027 and 2028". Customer deposits act as safeguards.
  - "Customers' volume requirement is more than double that of what we can supply today."
  - The supply constraint is "projected to continue through 2030".
  - M15X is ramping toward full capacity by end-2026; Yongin and M17 cleanrooms will open in phases. 2027 capex will rise significantly.
  - Source: [The Motley Fool, "SK hynix (SKHY) Q3 2026 Earnings Call Transcript," 2026-10-28](https://www.fool.com/earnings/call-transcripts/2026/10/28/sk-hynix-skhy-q3-2026-earnings-call-transcript/)
  - Financials [UNOPENED, secondary]: Q3 2026 revenue of about KRW 104.6T and an operating margin of about 80%. Source: [Hardware Busters, "SK hynix Earnings Hit an 80% Margin, and It Says the Memory Shortage Runs to 2030," Oct 2026](https://hwbusters.com/news/sk-hynix-earnings-hit-an-80-margin-and-it-says-the-memory-shortage-runs-to-2030/)
- **[SUPPLIER] Micron FQ4 2026 call (fiscal quarter ended early Sept 2026; transcript published 30 Sep 2026):**
  - Micron has "completed agreements for the vast majority of our calendar 2027 HBM bit supply" with significant YoY price increases.
  - "a large part of the volume is already sold out for 2027 for HBM, and the prices are much higher than 2026 prices".
  - On 2026: 2026 HBM prices "were negotiated with our customers last year".
  - More than 75% of fiscal-2027 output is committed. This covers all products, not HBM specifically.
  - Micron is "working with NVIDIA on the industry's first custom HBM4E implementation, NV-HBM".
  - The Singapore HBM packaging plant has "initial output expected in early calendar 2027". Idaho ID1 wafer output is expected in mid-CY2027.
  - Industry HBM bit shipments are expected to grow faster than conventional DRAM through CY2028.
  - Source: [Investing.com, "Earnings call transcript: Micron tops Q4 2026 estimates as demand stays hot," 2026-09-30](https://www.investing.com/news/transcripts/earnings-call-transcript-micron-tops-q4-2026-estimates-as-demand-stays-hot-93CH-4925992)
- **[SUPPLIER]** Micron's FQ1 2026 press release (17 Dec 2025) does not mention HBM. Source: [Micron Investor Relations, "Micron Technology, Inc. Reports Results for the First Quarter of Fiscal 2026," 2025-12-17](https://investors.micron.com/news-releases/news-release-details/micron-technology-inc-reports-results-first-quarter-fiscal-2026)
- **[ESTIMATE: TrendForce]** Global HBM bit-output share: SK hynix 59% in 2025 falling to 50% in 2026; Samsung 20% rising to 28%. Source: [TrendForce, "Samsung, SK hynix Reportedly Tapped as NVIDIA Rubin HBM4 Suppliers; Shipments Could Start in March," 2026-03-09](https://www.trendforce.com/news/2026/03/09/news-samsung-sk%E2%80%AFhynix-reportedly-tapped-as-nvidia-rubin-hbm4-suppliers-shipments-could-start-in-march/)

### Inferences
- "Sold out" is a supplier characterization that includes volumes still under negotiation. In SK hynix's case the hard, contracted coverage is ">50%" of 2027–28 capacity.

### Gaps
- I found no Samsung statement on whether its HBM is sold out for 2026 or 2027. Samsung's Q3 2026 call was not retrieved.
- I could not verify from an opened primary source Micron's December 2025 wording on 2026 HBM; its prepared remarks were not retrieved. See Section 6.

---

## 2B. HBM qualification with NVIDIA (HBM4 for Rubin), AMD (MI450) and Google/Amazon/Broadcom

### Takeaway
On 5 June 2026 NVIDIA's CEO said in public that Samsung, SK hynix and Micron were all qualified and in production for Vera Rubin HBM4. Earlier press reports (March 2026) had Micron supplying only the mid-tier Rubin CPX. SK hynix says full-scale HBM4 shipments began in Q3 2026. Samsung's 2025 HBM3E 12-high "pass" was reported through unnamed sources and was disputed at the time. I found no named qualification information for AMD MI450 or for Google, Amazon or Broadcom.

### Cited Findings
- **[CHIP-CO: NVIDIA, reported by Reuters, relayed by TechTimes]** 5 Jun 2026, Jensen Huang: "All three vendors have been qualified... All three vendors are in production, and they're all racing to support Vera Rubin." Separately, analysts (unnamed) estimate SK hynix at about 60–70% of Vera Rubin HBM4 and Samsung at about 25–30% [ESTIMATE]. Source: [TechTimes, "Nvidia Vera Rubin HBM4: Jensen Huang Confirms All Three Suppliers in Production for Q3 Ship," 2026-06-05](https://www.techtimes.com/articles/317855/20260605/nvidia-vera-rubin-hbm4-jensen-huang-confirms-all-three-suppliers-production-q3-ship.htm)
- **[PRESS-UNNAMED: Hankyung, via TrendForce]** 9 Mar 2026:
  - Samsung has "effectively passed" NVIDIA's HBM4 qualification, which is run at 10 Gb/s and 11 Gb/s tiers. SK hynix was still optimizing to pass the 11 Gb/s test.
  - Micron was expected to supply HBM4 for mid-tier parts such as Rubin CPX rather than flagship Vera Rubin.
  - Samsung began HBM4 shipments in February (per Global Economic).
  - Source: [TrendForce, 2026-03-09](https://www.trendforce.com/news/2026/03/09/news-samsung-sk%E2%80%AFhynix-reportedly-tapped-as-nvidia-rubin-hbm4-suppliers-shipments-could-start-in-march/)
- **[SUPPLIER] [UNOPENED]** Samsung announced commercial HBM4 shipments on 12 Feb 2026, using a 4nm logic base die and 12-high stacks. This date is from a search-result summary; the Samsung release was not opened.
- **[SUPPLIER] SK hynix (28 Oct 2026):**
  - "full-scale mass production and shipments of HBM4 commenced in the third quarter"; "Our shipments of 12-high HBM4 are proceeding smoothly according to the schedule agreed with our major customers"; "HBM4 already exceeded its planned yield".
  - HBM4 will surpass HBM3E in share of HBM volume and revenue in Q4 2026.
  - HBM4E samples shipped in Q2 2026.
  - No customer is named.
  - Source: [The Motley Fool transcript, 2026-10-28](https://www.fool.com/earnings/call-transcripts/2026/10/28/sk-hynix-skhy-q3-2026-earnings-call-transcript/)
- **[PRESS-UNNAMED: ZDNet Korea, via Wccftech]** 26 Oct 2026:
  - NVIDIA reportedly began talks in Q3 2026 with Samsung and SK hynix about 8-high HBM4 for Rubin Ultra, citing heat and declining yields in 12-high HBM4 and HBM4E.
  - 8-high parts would need separate certification, and volume would rise in Q2 2027.
  - No on-record company statements were given. Wccftech rated the report 35%, "Questionable".
  - Source: [Wccftech, "Samsung & SK hynix Reportedly Set To Ramp 8-Layer HBM4 Shipments For NVIDIA's Rubin Ultra In Q2 2027...," 2026-10-26](https://wccftech.com/samsung-sk-hynix-downgraded-hbm4-q2-2027-nvidia-rubin-ultra/)
- **[PRESS-UNNAMED] Samsung HBM3E 12-high (September 2025):**
  - The Korean Economic Daily and Business Korea reported that Samsung had cleared NVIDIA's validation.
  - Aju News reported that Samsung had completed internal wafer acceptance tests but had "not yet received NVIDIA's formal approval".
  - The article describes "a year and a half of setbacks", resolved by fixing a heat issue and redesigning the 1a DRAM.
  - Source: [TrendForce, "Samsung 12H HBM3E Reportedly Clears NVIDIA Tests After 18-Month Setback; HBM4 Reaches Final Phase," 2025-09-22](https://www.trendforce.com/news/2025/09/22/news-samsung-12h-hbm3e-reportedly-clears-nvidia-tests-after-18-month-setback-hbm4-reaches-final-phase/)
  - Also: [RCR Wireless, "Samsung secures Nvidia approval for HBM3E chips," 2025-09-25](https://rcrwireless.com/20250925/ai-infrastructure/samsung-nvidia-chips) [UNOPENED]
  - Earlier context: [TrendForce, "Samsung Reportedly Nears NVIDIA HBM3E Approval but Order Outlook Remains in Doubt," 2025-05-23](https://www.trendforce.com/news/2025/05/23/news-samsung-reportedly-nears-nvidia-hbm3e-approval-but-order-outlook-remains-in-doubt/) [headline only]
- **[SUPPLIER]** Micron is co-developing custom HBM4E ("NV-HBM") with NVIDIA (30 Sep 2026). Source: [Investing.com, 2026-09-30](https://www.investing.com/news/transcripts/earnings-call-transcript-micron-tops-q4-2026-estimates-as-demand-stays-hot-93CH-4925992)

### Inferences
- From suppliers' public statements one can verify that HBM4 was shipping in volume by Q3 2026. One cannot verify which supplier feeds which NVIDIA SKU, or anything about AMD or the ASIC programs.

### Gaps
- I found no source on HBM4 qualification for AMD MI450/MI455X.
- I found no source on HBM supplier qualification for Google TPU, AWS Trainium or Broadcom-designed XPUs by name. SK hynix refers only to "major global CSPs" among its 14 LTA customers.

---

## 2C. HBM4 specifications and bandwidth

### Takeaway
The JEDEC HBM4 standard (JESD270-4, April 2025) specifies a 2,048-bit interface at up to 8 Gb/s per pin, about 2 TB/s and up to 64 GB per stack. NVIDIA's Rubin qualification reportedly tests at 10–11 Gb/s.

### Cited Findings
- **[INDEPENDENT: standards body JEDEC; via press coverage] [UNOPENED]** Released 16 Apr 2025:
  - Up to 8 Gb/s across a 2,048-bit interface, giving about 2 TB/s per stack.
  - 4-, 8-, 12- and 16-high stacks with 24 Gb or 32 Gb dies, up to 64 GB per stack.
  - 32 channels per stack, up from 16.
  - Vendor-specific VDDQ of 0.7–0.9 V and VDDC of 1.0 or 1.05 V.
  - Controllers can support both HBM3 and HBM4.
  - Sources: [Business Wire (JEDEC press release), "JEDEC and Industry Leaders Collaborate to Release JESD270-4 HBM4 Standard...," 2025-04-16](https://businesswire.com/news/home/20250416843598/en/JEDEC-and-Industry-Leaders-Collaborate-to-Release-JESD270-4-HBM4-Standard-Advancing-Bandwidth-Efficiency-and-Capacity-for-AI-and-HPC); [TrendForce, "JEDEC Finalizes HBM4 Standard...," 2025-04-21](https://www.trendforce.com/news/2025/04/21/news-jedec-finalizes-hbm4-standard-potentially-easing-pressure-on-hybrid-bonding-adoption/)
- **[PRESS-UNNAMED via TrendForce]** NVIDIA wants HBM4 above 10 Gb/s for Vera Rubin, and qualification uses 10 and 11 Gb/s tiers (March 2026). Source: [TrendForce, 2026-03-09](https://www.trendforce.com/news/2026/03/09/news-samsung-sk%E2%80%AFhynix-reportedly-tapped-as-nvidia-rubin-hbm4-suppliers-shipments-could-start-in-march/)
- **[SUPPLIER]** SK hynix says lower stack counts (8-high) require more cubes and base dies for the same capacity, and that it has built this into its supply plan (Oct 2026). Source: [The Motley Fool transcript, 2026-10-28](https://www.fool.com/earnings/call-transcripts/2026/10/28/sk-hynix-skhy-q3-2026-earnings-call-transcript/)

### Inferences
- At 11 Gb/s per pin on a 2,048-bit interface, one stack would carry about 2.8 TB/s (11 × 2048 / 8 GB/s). That is about 38% above the roughly 2.05 TB/s JEDEC 8 Gb/s baseline. This is my arithmetic.

### Gaps
- I did not verify Rubin's per-GPU HBM4 capacity or bandwidth (NVIDIA-stated figures) in this pass.

---

## 2D. China's HBM (CXMT, Huawei in-house) and the US HBM export controls of December 2024

### Takeaway
The BIS rules of 2 December 2024 control HBM above 2 GB/s/mm² memory-bandwidth density, which covers all HBM in production. China's domestic HBM is lagging: Reuters reported in October 2026 that CXMT's HBM3E yields were 20–30%. Huawei uses its in-house HiBL 1.0 in the Ascend 950PR. Estimates say foreign stockpiles of roughly 10–13M stacks filled the gap in 2025 and run out in 2026. The Information reported in November 2026 that Huawei's next chip will depend heavily on Korean HBM, including smuggled parts.

### Cited Findings
- **[LEGAL SUMMARY of a government rule] [UNOPENED]** The 2 Dec 2024 BIS interim final rules created ECCN 3A090.c for HBM with memory-bandwidth density greater than 2 GB/s/mm². BIS notes "all HBM stacks currently in production" exceed this threshold. The rule covers HBM stacks and chips containing them, and created a License Exception HBM. Sources: [Morrison Foerster, "Biden Administration Export Controls Restrict China Advanced Semiconductors," 2024-12-18](https://www.mofo.com/resources/insights/241218-biden-administration-export-controls-restrict-china-advanced-semiconductors); [Federal Register 2024-28270, 2024-12-05](https://govinfo.gov/content/pkg/FR-2024-12-05/pdf/2024-28270.pdf)
- **[PRESS-UNNAMED: The Information; Reuters, via TrendForce]** 3 Nov 2026:
  - Smugglers pack HBM with low-end processors, because export rules assess a package by its compute. In China the HBM is removed and the processors discarded.
  - The Huawei 960DT (expected Q1 2027) will rely heavily on Samsung and SK hynix HBM.
  - Huawei has asked some customers to source memory themselves.
  - The suggested price of the 950DT was raised to above RMB 250,000 (about US$37k). The report says it delivers about half the H100's raw compute.
  - Reuters (28 Oct 2026): CXMT's HBM3E yields are 20–30%, against about 70% at SK hynix.
  - Source: [TrendForce, Huawei 960DT HBM shortage / smuggled HBM report, 2026-11-03](https://www.trendforce.com/news/?p=66148)
- **[CHIP-CO: Huawei; via TrendForce/Mydrivers/SCMP]** Roadmap from Huawei Connect 2025: Ascend 950PR in Q1 2026, 950DT in Q4 2026, 960 in Q4 2027 and 970 in Q4 2028. The Atlas 350 card (950PR) offers 1.56 PFLOPS FP4 (about 2.8x the H20, per Huawei), 112 GB of HBM, 1.4 TB/s and 600 W. The 950PR is the first chip with Huawei's self-developed HBM, HiBL 1.0. Source: [TrendForce, Huawei Ascend 950PR / Atlas 350 launch article, 2026-03-23](https://www.trendforce.com/news/?p=54956)
- **[ESTIMATE: Epoch AI]** 24 Sep 2026:
  - Before December 2024 China stockpiled more than 10M foreign HBM stacks, which filled the 2025 gap and are expected to run out in 2026.
  - CXMT and XMC are "only beginning to ramp".
  - Using only domestic HBM, Huawei could reach about 1.5M H100-equivalents a year by 2028, about 1.5% of NVIDIA's output.
  - Source: [Epoch AI, "How far behind Nvidia is Huawei?," 2026-09-24](https://epochai.substack.com/p/how-far-behind-nvidia-is-huawei)
- **[ESTIMATE: SemiAnalysis]** 8 Sep 2025:
  - Samsung directly supplied 11.4M HBM stacks to China, about 7M of them "in the one-month gap between control announcement and enforcement".
  - About 13M stacks in total, enough for about 1.6M 910C packages.
  - CXMT capacity is about 250k wspm, with about 2M HBM stacks expected the next year (2026), enough to support roughly 250–300k 910C.
  - Source: [SemiAnalysis, 2025-09-08](https://newsletter.semianalysis.com/p/huawei-ascend-production-ramp)
- **[PRESS] [UNOPENED]**
  - CXMT reportedly sampled HBM to Huawei, while the Ascend 950 uses HiBL 1.0 and HiZQ 2.0. Source: [Tom's Hardware, "Chinese semiconductor industry gears up for domestic HBM3 production by the end of 2026...," date not verified](https://www.tomshardware.com/pc-components/dram/chinese-semiconductor-industry-gears-up-for-domestic-hbm3-production-by-the-end-of-2026-cxmt-to-produce-chips-while-naura-maxwell-and-u-preseason-design-tools-for-assembly)
  - A July 2026 Japanese analysis says CXMT's HBM3 mass production slipped from 1H26 and volume in 2026 looks difficult. Source: [semi-connect.net, "CXMT HBM3: China AI memory challenge 2026," Jul 2026](https://semi-connect.net/cxmt-hbm3-china-ai-memory-challenge-2026/)

### Inferences
- SemiAnalysis's "one-month gap between control announcement and enforcement" sits uneasily with a BIS summary document that reportedly gave the HBM controls no delayed compliance date. I saw that only in a search summary and did not open the document. Other Category 3 changes in the same package had a 31 Dec 2024 compliance date, which may explain the discrepancy. This should be checked against the Federal Register text.

### Gaps
- I found no official production figures for CXMT HBM or Huawei HiBL.
- I found no independent measurement of HiBL 1.0 bandwidth or capacity.

---

## 3. Other bottlenecks: substrates (ABF, T-glass), power and grid, liquid cooling, optics/CPO, SMIC 7/5nm

### Takeaway
Documented constraints in 2026, beyond CoWoS and HBM:
- T-glass cloth, concentrated at Nittobo, with a reported shortfall of 10–20% or more.
- InP lasers for optics and CPO, with demand about 30% above supply per Lumentum and LightCounting.
- Grid interconnection and transformer lead times.
- CoWoS price increases and 6–8-month equipment lead times.

SMIC's N+3 is DUV-only, and TechInsights judges it not viable for data-center AI chips. I found no liquid-cooling supply data.

### Cited Findings
- **Substrates / T-glass [ESTIMATE/PRESS] [UNOPENED]:**
  - Nittobo is reported to hold about 90% of specialty glass cloth. A Digitimes summary says "just over half".
  - Nittobo's Fukushima expansion roughly triples capacity, but new supply is expected around mid-2027.
  - Sources: [Tom's Hardware, "Shortages of crucial chip packaging material threatens AI accelerator supply chains...," 2026](https://www.tomshardware.com/tech-industry/shortages-of-crucial-chip-packaging-material-threatens-ai-accelerator-supply-chains-nittobos-fukushima-plant-is-tripling-capacity-but-itll-take-years-before-market); [Heise, 2026](https://heise.de/-11174896); [iTiger/Digitimes summary](https://www.itiger.com/news/1190744010)
  - Larger AI substrates need more T-glass in core layers. Goldman Sachs, as cited by TrendForce, expects double-digit percentage T-glass shortages for BT substrate makers. Source: [TrendForce, "What Is Glass Fiber Fabric and Why Is T-Glass Critical for AI Servers?," 2025-11-24](https://www.trendforce.com/news/2025/11/24/news-what-is-glass-fiber-fabric-and-why-is-t-glass-critical-for-ai-servers-a-deep-dive/)
  - Taiwanese substrate makers reportedly expect a 10–20% T-glass gap in 2026, above 40% for high-end cloth in 2H26. The Digitimes summary cites more than 40% for 2026 and about 25% for 2027, and also flags an HVLP4 copper-foil shortfall of about 1,500 tonnes in 2H26. Source: [Borecraft, "The AI bottleneck is spreading from chips to substrates, glass, and power," 2026-06-09](https://borecraft.com/2026/06/09/the-ai-bottleneck-is-spreading-from-chips-to-substrates-glass-and-power/)
- **Optics / CPO [SUPPLIER and ESTIMATE] [UNOPENED]:**
  - Lumentum's CEO said the InP supply–demand gap has surpassed DRAM and NAND. In its fiscal Q2 2026 call Lumentum said photonics demand outstrips supply by about 30%.
  - LightCounting (April 2026) estimated transceiver demand exceeds supply by 30% and could resolve by end-2026. Other analysts expect it to persist beyond 2027, and CPO-driven InP laser tightness may last until 2028.
  - Sumitomo Electric plans to roughly triple InP substrate capacity between 2024 and 2028.
  - NVIDIA committed US$2B each to two key optics suppliers in March 2026.
  - Source: [TrendForce/LEDinside, "InP Shortage Emerges as AI Optical Interconnect Bottleneck," 2026-08-06](https://trendforce.com/news/2026/08/06/news-inp-shortage-emerges-as-ai-optical-interconnect-bottleneck/)
  - Yole argues "InP shortage" is imprecise: pressure moves from EML capacity to CW lasers, silicon-photonics yield and packaging. Source: [Yole Group, "Opinion: Optical transceivers at the chokepoint of AI growth and supply chain constraints," 2026](https://www.yolegroup.com/strategy-insights/opinion-optical-transceivers-at-the-chokepoint-of-ai-growth-and-supply-chain-constraints/)
  - A TrendForce-based report says NVIDIA effectively locked up EML capacity, with lead times stretching past 2027. Source: [TechNews, 2025-12-08](https://technews.tw/2025/12/08/ai-data-centers-trigger-shortages-of-optical-communication-lasers/)
- **Power and grid [ESTIMATE, via secondary aggregators] [UNOPENED; I could not verify which page carries which figure]:** Search summaries relayed the following:
  - Sightline Climate: about 12 GW of US data-center capacity slated for 2026 across about 140 projects, with only about 5 GW under construction.
  - Morgan Stanley (Feb 2026): US data-center demand of 74 GW by 2028 against a 49 GW power-access shortfall.
  - LBNL 2025 queue report: about 2,061 GW of generation and storage seeking interconnection.
  - ERCOT large-load queue: about 410 GW (April 2026), about 87% of it data centers.
  - PJM waits for large loads exceed 8 years in some cases.
  - High-voltage transformer lead times of 3–4 years by 2025.
  - Candidate sources: [Enterprise DNA, 2026](https://enterprisedna.co/resources/news/ai-data-center-power-crisis-half-builds-delayed-2026); [Introl, "PJM Grid Crisis...," 2026](https://introl.com/blog/pjm-grid-crisis-6gw-shortfall-data-center-power-2027); [Data Center Frontier](https://www.datacenterfrontier.com/energy/article/55365067/project-stalled-grid-bottlenecks-threaten-the-fifth-industrial-revolution); [Network World, "Google warns transmission delays are now the biggest threat to data center expansion"](https://www.networkworld.com/article/4117329/google-warns-transmission-delays-are-now-the-biggest-threat-to-data-center-expansion.html)
- **SMIC 7/5nm [INDEPENDENT: TechInsights]:**
  - The Kirin 9030 (Mate 80 Pro Max) is made on SMIC N+3, "a scaled evolution of its 7nm-class technology". It is "significantly less scaled" than TSMC and Samsung 5nm. Source: [TechInsights, "SMIC N+3 Confirmed: Kirin 9030 Analysis Reveals How Close SMIC Is to 5nm," 2025-12-11](https://www.techinsights.com/blog/smic-n3-confirmed-kirin-9030-analysis-reveals-how-close-smic-5nm)
  - TechInsights calls it a "production quality smartphone chip" but does not expect the process to be viable for data-center AI chips. It cites DUV limitations and process immaturity, which it expects to cause low yields on large AI dies. Source: [TechInsights, "Can China even build data center AI chips?," 2026-03-17](https://www.techinsights.com/ja/node/61228)
  - [UNOPENED] A TechInsights briefing summary reports N+3 gate pitch of 57 nm, fin pitch of 32 nm, density of about 120 MTr/mm², and DUV multi-patterning rather than EUV.
- **SMIC capacity [ESTIMATE: SemiAnalysis, 2025-09-08]:**
  - Advanced-node (7nm and below) capacity of 45k wspm at end-2025, 60k in 2026 and 80k in 2027. Ascend needs at most about 20k wspm.
  - 7nm-class yields are "poor". SemiAnalysis's yield estimates are below those of TSMC, Intel and Samsung.
  - Source: [SemiAnalysis](https://newsletter.semianalysis.com/p/huawei-ascend-production-ramp)
- **Packaging cost and lead time [PRESS via TrendForce, 2026-10-27]:** CoWoS price increases of up to 20% are reported, with equipment lead times of 6–8 months. Nomura estimates final-test time for Blackwell at about 4x Hopper, and possibly 7x for Rubin. Source: [TrendForce](https://www.trendforce.com/news/2026/10/27/news-tsmc-reportedly-eyes-20-cowos-price-hike-skips-equipment-price-renegotiations-amid-ai-demand-surge/)

### Inferences
- The constraints have spread from logic and packaging to materials (T-glass, InP) and site power, and all of these have multi-year lead times. Any company's shipment claims for 2027 also depend on these inputs.

### Gaps
- Liquid cooling: I found no supply-constraint or penetration data from cooling vendors or analysts. The search budget ran out first.
- ABF (as distinct from T-glass): no capacity or price data found.
- I found no TechInsights figures on SMIC yield or wafer capacity; they are paywalled.

---

## 4A. MLPerf Training and Inference, 2024 to the latest 2026 round

### Takeaway
MLCommons published three rounds in 2026: Inference v6.0 (1 Apr), Training v6.0 (16 Jun) and Inference v6.1 (16 Sep).
- NVIDIA, AMD and Google are submitters in all three.
- NVIDIA's Vera Rubin NVL72 appeared only in the "preview" category of v6.1.
- AMD's largest result was a 512-GPU MI355X run by Crusoe.
- AWS (Trainium), Broadcom, Huawei and Cerebras do not appear in any 2026 submitter list.
- Google did not submit Ironwood to Inference v6.0 and gave no reason.
- Training v6.1 (October 2026 submission round) results were not found published as of 14 Nov 2026.

### Cited Findings
- **[INDEPENDENT: MLCommons] Inference v6.1 (16 Sep 2026):**
  - 30 submitters: AMD, ASUSTeK, Atlas Inference, Cisco, CoreWeave, Crusoe, Dell, Fujitsu, GigaComputing, Google, HPE, Intel, Inventec, KRAI, Lambda, MangoBoost, Microsoft Azure, MiTAC, Nebius, NVIDIA, Oracle, Orrick, Quanta Cloud Technology, Red Hat, ScitiX, Supermicro, TTA, VibeHPC, Wiwynn, and Naeem Khoshnevis.
  - Hardware highlights: AMD Ryzen AI Max+ 395 and Instinct MI350P (available); NVIDIA Rubin and Vera Rubin NVL72 (preview); Intel Arc Pro B70.
  - Largest system: 512 accelerators. Two heterogeneous systems were submitted, one spanning the Pacific.
  - The best per-accelerator DeepSeek-R1 server result was up to 5.7x v5.1; VLM was up 2.99x versus v6.0.
  - New tests: end-to-end RAG and edge agentic inference.
  - Source: [MLCommons, "MLCommons Sets Participation Record with New MLPerf Inference v6.1 Benchmark Results," 2026-09-16](https://mlcommons.org/2026/09/mlperf-inference-v6-1-results/)
- **[INDEPENDENT: MLPerf results as reported by StorageReview] v6.1:**
  - 486 results in total.
  - Crusoe, 512 MI355X GPUs over RoCE: gpt-oss-120b 5.75M tok/s offline and 5.39M server; DeepSeek-R1 2.90M offline and 2.41M server.
  - A 72-GPU gpt-oss run reached about 1M tok/s at 95% scaling.
  - CoreWeave GB300 NVL72: 1.16M tok/s aggregate, per-GPU offline +17% versus v6.0.
  - HPE Blackwell Ultra: 8,500 tok/s per GPU on DeepSeek-R1.
  - Google submitted, focusing on DeepSeek-R1; the hardware is not stated.
  - [CHIP-CO: NVIDIA] Vera Rubin NVL72 (preview) delivered up to 2.5x GB300 NVL72 on DeepSeek-R1 and 3.7x on a Qwen3 VLM.
  - Source: [StorageReview, "MLPerf Inference v6.1: 5.7x Per-Accelerator Gains, a 512-GPU Run, and Vera Rubin's First Peer-Reviewed Numbers," 2026-09-16](https://www.storagereview.com/news/mlperf-inference-v6-1-5-7x-per-accelerator-gains-a-512-gpu-run-and-vera-rubins-first-peer-reviewed-numbers)
- **[CHIP-CO: AMD] [UNOPENED]** In v6.1 the MI355X delivered 18% higher Offline and 11% higher SingleStream performance than "the selected NVIDIA B300 submission". Source: [AMD blog, "AMD Delivers Its Broadest MLPerf Inference 6.1 Submission," Sep 2026](https://www.amd.com/en/blogs/2026/amd-delivers-its-broadest-mlperf-inference-6-1-submission.html)
  - **[INDEPENDENT recomputation] [UNOPENED]** The best 8-GPU GB300 row on gpt-oss-120b Server is 16,022 tok/s per GPU against 14,155 for MI355X. Source: [GPU Insights, "MLPerf Inference v6.1: Per-GPU Results Recomputed," 2026](https://gpuinsights.net/mlperf-inference-v6-1-per-gpu-results-2026/)
- **[INDEPENDENT: MLCommons] Training v6.0 (16 Jun 2026):**
  - 24 submitters: AMD, ASUSTeK, Azure, Cisco, CoreWeave, Dell, Fujitsu, GigaComputing, Google, HPE, Inventec, Krai, Lambda, MiTAC, Nebius, Netweb, NVIDIA, Oracle, QCT, ScitiX, Supermicro, tinycorp, TTA, Vultr.
  - 95 systems and 13 accelerator types; 60% of systems were multi-node.
  - New benchmarks: DeepSeek V3 (671B MoE) and GPT-OSS 20B.
  - Source: [MLCommons, Training v6.0 results announcement, 2026-06-16](https://mlcommons.org/2026/06/mlperf-training-v6-0-results/)
  - Secondary claims [UNOPENED]: the fastest DeepSeek-V3 time was 2.02 min on 8,192 GB300 GPUs; eight teams submitted GB300 NVL72 results; AMD made its first multi-node training submission (MI355X). [CHIP-CO: AMD] MI355X within 5% of B200 on Llama 2-70B LoRA and within 6% on Llama 3.1-8B pretraining, at FP4. [CHIP-CO: NVIDIA] GB300 NVL72 up to 1.6x GB200 NVL72 at the same scale. Sources: [Digital Applied, "MLPerf Training v6.0: Reading the 2026 Hardware Race," 2026-06-21](https://www.digitalapplied.com/blog/mlperf-training-v6-2026-results-hardware-leaderboard); [AMD blog, 2026](https://www.amd.com/en/blogs/2026/amd-delivers-breakthrough-mlperf-training-6-0-results.html) (HTTP 503 when fetched)
- **[INDEPENDENT: MLCommons] Inference v6.0 (1 Apr 2026):**
  - 24 submitters: AMD, ASUSTeK, Cisco, CoreWeave, Dell, GATEOverflow, GigaComputing, Google, HPE, Intel, Inventec, KRAI, Lambda, Lenovo, MangoBoost, MiTAC, Nebius, Netweb, NVIDIA, Oracle, Quanta Cloud Technology, Red Hat, Stevens Institute of Technology, Supermicro.
  - Largest system: 72 nodes and 288 accelerators.
  - New tests: GPT-OSS 120B, interactive DeepSeek-R1, DLRMv3, text-to-video, VLM and YOLOv11.
  - Source: [MLCommons, Inference v6.0 results announcement, 2026-04-01](https://mlcommons.org/2026/04/mlperf-inference-v6-0-results/)
- **[INDEPENDENT commentary on MLPerf] Google TPU history (published 1 Apr 2026):**
  - Google submitted TPU Trillium (v6e) to Inference v5.0 (April 2025), submitted no TPU to v5.1 (September 2025), and did not submit TPU v7 Ironwood to v6.0. No official reason was given.
  - NVIDIA was the only platform with results on every test. AMD had not yet submitted DeepSeek-R1 and said it intends to.
  - Source: [Tae Kim, "Nvidia Wins MLPerf AI Inference Benchmarks While Google Is a No-Show Again," 2026-04-01](https://taekim.substack.com/p/nvidia-wins-mlperf-ai-inference-benchmarks)
- **[INDEPENDENT: MLCommons] Training v6.1:**
  - Adds a post-training, agentic-RL benchmark (Qwen 3.5 397B, R2E-Gym subset, OpenHands harness, pass@4 target of 0.69). The reference run took about 140–160 min on 256 GB300 GPUs.
  - It starts with the October 2026 submission round. No publication date is stated.
  - Source: [MLCommons, "MLPerf Training v6.1: First LLM Post-Training Benchmark," 2026-09-24](https://mlcommons.org/2026/09/mlperf-training-llm-post-training/)
- **[INDEPENDENT: IEEE Spectrum on MLPerf Training, June 2025]:**
  - NVIDIA submitted to all six benchmarks and was fastest on each; the largest pretraining run used 8,192 GPUs at about 90% scaling.
  - AMD made its first MLPerf training submission (MI325X), matching H200 on LLM fine-tuning.
  - Google submitted to one benchmark, image generation, on Trillium.
  - Only Lenovo submitted power measurements.
  - Source: [IEEE Spectrum, "Nvidia's Blackwell Conquers Largest LLM Training Benchmark," 2025-06-04](https://spectrum.ieee.org/nvidia-blackwell-mlperf-training-5)
- **Non-submitters and stated reasons:**
  - AWS, Broadcom, Huawei and Cerebras are absent from all three 2026 submitter lists (my reading of the official lists above).
  - [PRESS] [UNOPENED] Cerebras "has consistently expressed disinterest in MLPerf participation". Source: [HPCwire, "The Mainstreaming of MLPerf? Nvidia Dominates Training v2.0 but Challengers Are Rising," 2022-06-29](https://www.hpcwire.com/2022/06/29/the-mainstreaming-of-mlperf-nvidia-dominates-training-v2-0-but-challengers-are-rising/)
  - [PRESS] [UNOPENED] Huawei's Ascend 910 appeared in MLPerf Training v0.7 (2020) only in the R&D/Internal category, on ResNet. Source: [ServeTheHome, "MLPerf 0.7 results...," 2020](https://www.servethehome.com/mlperf-0-7-results-when-winners-only-apply-nvidia-google-intel-huawei-inspur/)
  - I found no stated reason from AWS or Broadcom.

### Inferences
- From 2025 through 2026, only NVIDIA- and AMD-based systems have given audited, broad MLPerf coverage. Google's TPU presence fell from Trillium entries in 2025 to no confirmed TPU entries in 2026. Trainium, Ascend, Cerebras WSE and Broadcom-designed XPUs (other than Google TPUs) have no audited MLPerf data in the period.
- Vera Rubin's MLPerf numbers (v6.1) are "preview": under MLPerf rules the system was not yet commercially available at submission time.

### Gaps
- I did not verify MLPerf 2024 rounds (Inference v4.0/v4.1, Training v4.0/v4.1) or Inference v5.1 and Training v5.1 (2025) in this pass. Unverified recollections, not facts: AMD's first Inference submission (MI300X) was in v4.1 in August 2024; Google submitted TPU v5p and Trillium preview in 2024 rounds.
- I could not confirm which hardware Google used in its 2026 submissions; the supplemental PDF was not machine-readable.
- Publication status of Training v6.1 results as of 14 Nov 2026 is unconfirmed.

---

## 4B. SemiAnalysis InferenceMAX / InferenceX (NVIDIA vs AMD; TPU/Trainium)

### Takeaway
SemiAnalysis's open benchmark (InferenceMAX, renamed InferenceX) finds NVIDIA leading most configurations. The MI355X is competitive in specific ranges, such as single-node FP8 and some latency bands, and its standing moves with software releases. Neither the February nor the August 2026 article benchmarked TPU or Trainium. NVIDIA and AMD both supported the project; SemiAnalysis discloses this.

### Cited Findings
- **[INDEPENDENT: SemiAnalysis InferenceX v2, vendor-assisted] 16 Feb 2026:**
  - Covers H100, H200, B200, B300, GB200 NVL72, GB300 NVL72, MI300X, MI325X and MI355X. TPU v7 and Trainium3 were to be added "later this year".
  - MI355X SGLang is "competitive" with B200 SGLang on FP8 disaggregated + wideEP perf per TCO; Dynamo TRT-LLM on B200 still leads.
  - In FP4 disaggregated serving the MI355X "falls well behind".
  - GB200 NVL72 shows "nearly no advantage" at about 130 tok/s/user and costs more per million tokens.
  - Blackwell is up to about 98–100x better than an H100 disaggregated FP8 baseline at 116 tok/s/user. The article says this exceeds NVIDIA's GTC 2024 claim of up to 30x, though the comparison spans different precisions.
  - NVIDIA GPUs "dominate" energy efficiency (provisioned pJ/token), a qualitative statement.
  - SemiAnalysis projects MI455X mass production by Q2 2027.
  - Disclosure: NVIDIA provided GB300 NVL72 and other hardware plus engineering validation; AMD engineers contributed.
  - Sources: [SemiAnalysis InferenceX blog (mirror), "InferenceX v2: NVIDIA Blackwell Vs AMD vs Hopper," 2026-02-16](https://inferencex.semianalysis.com/blog/inferencex-v2-nvidia-blackwell-vs-amd-vs-hopper); [SemiAnalysis newsletter](https://newsletter.semianalysis.com/p/inferencex-v2-nvidia-blackwell-vs)
- **[INDEPENDENT: SemiAnalysis InferenceX] 9 Jun 2026, DeepSeek V4:**
  - Huawei Ascend 950DT profiler traces were shown, with no throughput numbers; a head-to-head was promised. CANN and CUDA were the only stacks with Day-0 DeepSeek V4 support, and AMD's stack "did not work well" on Day 0.
  - MI355X interactivity was 1–2 tok/s/user on Day 0 and improved more than 100x by late May.
  - B200 throughput at 50 tok/s/user rose from about 300k to about 500k tok/s per provisioned MW (Day 0 to 5 June).
  - GB300 NVL72: US$0.156 per M output tokens at 50 tok/s/user (8K input / 1K output).
  - Source: [SemiAnalysis, "DeepSeekV4 1.6T Day 0 to Day 43 Performance Over Time — Huawei, GB300 NVL72, MI355X, B200," 2026-06-09](https://inferencex.semianalysis.com/blog/deepseekv4-16t-day-0-to-day-43-performance)
- **[INDEPENDENT: SemiAnalysis AgentX / InferenceXv3] 24 Aug 2026:**
  - On DeepSeek V4 Pro, B200 overtook MI355X on end-to-end perf/$ after vLLM optimizations on 21 Aug 2026.
  - On Kimi K3, MI355X with ATOM beat GB300 NVL72 vLLM on perf/$ in the 40–60 s latency band.
  - On Qwen3.5 397B, NVIDIA SGLang delivered more than 20x AMD at 90 tok/s/user.
  - On MiniMax M3, B200 and B300 beat GB200 and GB300 on TCO-normalized throughput.
  - AMD weaknesses noted: p90 TTFT spikes in disaggregated mode, KV-offload inefficiency (`hipMemcpyBatchAsync` missing until ROCm 7.14) and no context parallelism.
  - Rubin "arrives later this month"; TPUs and MI455X "arrive later this year".
  - Source: [SemiAnalysis, "AgentX - InferenceXv3: Does CUDA Moat Hold up in Agentic Inferencing?," 2026-08-24](https://newsletter.semianalysis.com/p/agentx-inferencexv3-does-cuda-moat)
- **[INDEPENDENT: SemiAnalysis InferenceX] [UNOPENED; from search summary]**
  - Vera Rubin NVL72 leads GB300 NVL72 by 1.8–2.0x in tokens per $ of TCO at 100 tok/s/user (October 2026).
  - At 200 tok/s/user on Qwen3.5-397B, TPU v7 FP8 delivers 1.85x (external TCO) and 2.17x (internal TCO) the tokens per $ of GB300 NVL72 FP8. GB300 NVL72 FP4 with Dynamo TRT-LLM leads at every matched point.
  - Source: [InferenceX hardware results](https://inferencex.semianalysis.com/hardware)
  - [PRESS relaying a SemiAnalysis social post] MI355X with TileRT ran about 1.42x faster per user than GB300 NVL72 (November 2026). Source: [FourWeekMBA, 2026-11](https://fourweekmba.com/ai-amd-mi355x-runs-1-42x-faster-per-user-than-gb300-with-tilert/)

### Inferences
- InferenceX results move with software releases, sometimes within days. Any vendor claim citing InferenceX needs the result's date, model, precision, framework and interactivity point to be testable.

### Gaps
- InferenceMAX's launch date and initial results (October 2025) were not verified.
- I found no InferenceX data for Trainium (any generation) and no numeric results for Huawei 950DT.

---

## 4C. Artificial Analysis hardware and speed benchmarks

### Takeaway
Artificial Analysis (AA) measures API endpoints, meaning provider deployments, rather than chips under controlled settings. Relayed AA figures show Cerebras at about 1,700–2,700+ output tok/s on gpt-oss-120B, varying by date. A Cerebras blog citing AA put B200 at about 900 tok/s in September 2025. Cerebras's "~21x" headline uses a different metric, which Cerebras derived from SemiAnalysis data.

### Cited Findings
- **[INDEPENDENT: Artificial Analysis]** The hardware benchmark page says AA benchmarks systems on throughput, latency, cost and power across three tiers: datacenter nodes, racks and clusters; laptops and workstations; and phones. The landing page gives no figures or as-of date (accessed 14 Nov 2026). Source: [Artificial Analysis, "Hardware benchmarks"](https://artificialanalysis.ai/benchmarks/hardware)
- **[CHIP-CO: Cerebras, citing AA and SemiAnalysis] 19 Sep 2025:**
  - gpt-oss-120B: 2,700+ tok/s against 900 tok/s on DGX B200, citing AA. A B200 figure of 580 tok/s with 10 parallel requests is also cited to AA.
  - Llama 4 Maverick: 2,500+ against about 1,000 tok/s.
  - "~21x faster" end-to-end on a Llama 3 70B reasoning scenario (1,024 input / 4,096 output tokens), "derived from a SemiAnalysis report, recalculated by Cerebras".
  - The footer says comparisons are "based on third-party benchmarking or internal testing", and that B200 figures come from benchmark-optimized configurations while Cerebras figures come from production systems.
  - Source: [Cerebras, "Cerebras CS-3 vs. Nvidia DGX B200 Blackwell," 2025-09-19](https://www.cerebras.ai/blog/cerebras-cs-3-vs-nvidia-dgx-b200-blackwell)
- **[INDEPENDENT: AA figures, relayed by secondary sources] [UNOPENED]**
  - Cerebras led AA's gpt-oss-120B ranking at about 1,753 output tok/s as of June 2026. Another post gives 1,705.8 tok/s, more than 2.4x the next-fastest API. Source: [Fast.io, "Fastest AI in 2026," 2026](https://fast.io/resources/fastest-ai-2026/)
  - An AA run on 8x B200 with gpt-oss-120B gave 403 output tok/s per query and 92,909 tok/s peak system throughput. Source: [Cerebrium, "NVIDIA B200 Inference: Measured Throughput and TTFT"](https://cerebrium.ai/resources/nvidia-b200-inference-throughput-ttft)
- **[INDEPENDENT commentary]** IEEE Spectrum (June 2025) notes that Cerebras's claim to beat Blackwell came from AA, which "doesn't control how workloads run", so it is not apples-to-apples in the way MLPerf is. Source: [IEEE Spectrum, 2025-06-04](https://spectrum.ieee.org/nvidia-blackwell-mlperf-training-5)

### Inferences
- AA's per-query speed numbers compare service deployments, which differ in batch size, quantization and parallelism. They are evidence about providers' endpoints rather than about chip capability.

### Gaps
- I could not access AA's datacenter hardware result tables. The page gave no figures or as-of dates.
- I found no AA data on TPU, Trainium or Ascend hardware.

---

## 4D. Peer-reviewed papers and technical disclosures (ISCA, MICRO, HPCA, Hot Chips, ISSCC, arXiv)

### Takeaway
Most 2026 technical disclosures were presented by the vendors themselves. At Hot Chips 2026 these were NVIDIA's Vera Rubin, AMD's MI455X/Helios, Google's TPU 8t/8i and Cerebras's CS-4; there was no Trainium3 or Huawei talk. The non-vendor peer-reviewed evidence found is limited to customer and academic papers: Meta's Llama 3 reliability data and Gholami et al. on the memory wall.

### Cited Findings
- **[CHIP-CO technical disclosures, summarized by an independent outlet] Hot Chips 2026 (Palo Alto, 23–25 Aug 2026):**
  - NVIDIA compared Vera Rubin NVL72 with GB300 on DeepSeek-v4-PRO: about 2x at lower interactivity and up to 30x at high interactivity. It said Vera Rubin is "already ramping" at CoreWeave, Google Cloud, Azure, OCI and Nebius. It also presented a Groq-derived LPU ("Groq 3 LPX") alongside Rubin.
  - AMD presented the MI455X and Helios: a 72-GPU scale-up domain over Broadcom Ethernet switches, with no AI performance chart.
  - Google presented TPU 8t (training) and 8i (inference). The 8i uses "Boardfly" across 1,152 chips with at most 7 hops via OCS; the 8t uses a 3D torus with superpods of up to 9,600 chips and the Virgo network scaling to 134,400 TPUs. Google cited about 2x prior TPUs and said the 8i is 1.4x the size of the 8t because of more HBM.
  - Cerebras presented the CS-4 (2x tokens/user versus CS-3, up to 10x throughput per watt), with a roadmap to CS-5 and to CS-6 with 3D-stacked DRAM.
  - [CUSTOMER: OpenAI] OpenAI's "Jalapeño" uses Broadcom Tomahawk 6 switches (128-chip domain, 2,048-chip global domain) and was claimed to beat GB300.
  - The article does not describe a Trainium or Huawei presentation.
  - Source: [Semiconductor Engineering, Geoff Tate, "Can GPUs Continue To Dominate AI Compute?," 2026-09-09](https://semiengineering.com/can-gpus-continue-to-dominate-ai-compute/); conference site: [Hot Chips 2026](https://hc2026.hotchips.org/)
- **[COMPANY-AUTHORED: Google, peer-reviewed]** "Resiliency at Scale: Managing Google's TPUv4 Machine Learning Supercomputer", Zu et al., NSDI '24 (April 2024). It describes a 4,096-node 3D torus with optical circuit switching, 99.98% system availability, and hardware outages affecting about 1% of training jobs. Source: [USENIX NSDI '24](https://www.usenix.org/conference/nsdi24/presentation/zu)
- **[CUSTOMER: Meta, arXiv]** "The Llama 3 Herd of Models" (July 2024). Over a 54-day snapshot on 16,384 H100s there were 466 job interruptions, 419 of them unexpected. GPU issues accounted for 58.7% of unexpected interruptions: faulty GPUs 148 (30.1%) and HBM3 72 (17.2%). Effective training time was above 90%. Sources: [arXiv 2407.21783](https://arxiv.org/pdf/2407.21783); [Tom's Hardware coverage, 2024-07](https://www.tomshardware.com/tech-industry/artificial-intelligence/faulty-nvidia-h100-gpus-and-hbm3-memory-caused-half-of-the-failures-during-llama-3-training-one-failure-every-three-hours-for-metas-16384-gpu-training-cluster)
- **[INDEPENDENT: academic, IEEE Micro]** Gholami et al., "AI and Memory Wall" (arXiv March 2024; published in IEEE Micro). Over 20 years, peak server FLOPS grew 3.0x every 2 years, DRAM bandwidth 1.6x and interconnect bandwidth 1.4x, making memory "the primary bottleneck" for decoder serving. Source: [arXiv 2403.14123](https://arxiv.org/abs/2403.14123)
- **[COMPANY-AUTHORED: Google, arXiv]** "Measuring the environmental impact of delivering AI at Google Scale" (21 Aug 2025). A median Gemini Apps text prompt uses 0.24 Wh and 0.26 mL of water. Energy per prompt fell 33x and carbon 44x over 12 months. The measurement includes accelerators, host, idle capacity and data-center overhead. Source: [arXiv 2508.15734](https://arxiv.org/abs/2508.15734)

### Inferences
- Outside MLPerf, InferenceX, AA and teardowns, no peer-reviewed work by non-vendor authors directly measuring Ironwood, Trainium2/3, Ascend 950 or WSE-3 was found in this pass.

### Gaps
- No ISCA, MICRO, HPCA or ISSCC 2025–2026 papers on these seven companies' chips were retrieved; the search budget ran out.
- Huawei's CloudMatrix384 arXiv paper (2025) was not retrieved.
- The Hot Chips 2026 slide decks were not opened; only the press summary was used.

---

## 5. Physical and engineering limits across the sector

### Takeaway
- Packages are growing far past the single-reticle die limit: TSMC is producing about 5–5.5-reticle CoWoS now, with 14-reticle planned for 2028 and 40-reticle system-on-wafer for 2029.
- Memory bandwidth has historically grown much more slowly than compute.
- Rack power is moving toward 800 V DC and MW-class racks from 2027 (NVIDIA-stated).
- Leading-edge cost and yield pressure is visible in TSMC's N2 margin dilution and price increases.
- China's SMIC is DUV-limited.
- At scale, GPU and HBM faults are the leading cause of interruptions (Meta).

### Cited Findings
- **Die and packaging**
  - [SUPPLIER] Wei (October 2026): TSMC is producing advanced packages at five times the reticle size. Source: [CRN Asia, 2026-10-15](https://www.crnasia.com/news/2026/components-and-peripherals/tsmc-third-quarter-revenue-tops-guidance-as-ceo-says-ai-dema)
  - [SUPPLIER] [UNOPENED, from search summaries of TSMC's 2026 symposia]
    - 5.5-reticle CoWoS in production with yields above 98% (Europe symposium). Source: [cnyes, 2026](https://hao.cnyes.com/post/268520)
    - A 14-reticle CoWoS integrating about 10 large compute dies and 20 HBM stacks, slated for 2028; a 40-reticle SoW-X system-on-wafer expected in 2029 (North America symposium, April 2026). Source: [HPCwire (TSMC release), "TSMC Debuts A13 Tech at 2026 North America Technology Symposium," 2026-04-22](https://www.hpcwire.com/off-the-wire/tsmc-debuts-a13-tech-at-2026-north-america-technology-symposium/)
    - Tom's Hardware's reading of the roadmap slide: a 9.5-reticle interposer in 2027 supporting 12 HBM5 stacks and needing a 120 × 150 mm substrate, and more than 14 reticles with up to 24 HBM5E by 2029. Source: [Tom's Hardware, "TSMC details next-gen CoWoS roadmap: over 14-reticle packages and 48x leap in compute power expected by 2029...," 2026](https://www.tomshardware.com/tech-industry/semiconductors/tsmcs-details-next-gen-cowos-roadmap-over-14-reticle-packages-and-48x-leap-in-compute-power-expected-by-2029-massive-size-enables-24-hbm5e-stacks-and-additional-memory-bandwidth-jump) (headline opened only)
  - [PRESS via TrendForce] CoPoS (panel-level): pilot-line equipment installed February 2026, full line by June 2026, mass production as early as 2028–2029. Source: [TrendForce, 2026-04-16](https://www.trendforce.com/news/2026/04/16/news-tsmc-says-cowos-offers-industrys-largest-reticle-size-packaging-amid-intel-emib-rivalry-copos-advances/)
  - [CHIP-CO: Cerebras] Wafer-scale roadmap: CS-4 (2026), then CS-5, then CS-6 with 3D-stacked DRAM. Source: [Semiconductor Engineering, 2026-09-09](https://semiengineering.com/can-gpus-continue-to-dominate-ai-compute/)
- **Memory**
  - [INDEPENDENT: academic] Compute 3.0x / DRAM bandwidth 1.6x / interconnect 1.4x per 2 years. Source: [Gholami et al., arXiv 2403.14123](https://arxiv.org/abs/2403.14123)
  - [STANDARD] HBM4: about 2 TB/s and up to 64 GB per stack at JEDEC 8 Gb/s (see 2C).
  - [PRESS-UNNAMED] 12-high HBM4 and HBM4E heat and yield issues reportedly drove talks on 8-high stacks for Rubin Ultra (October 2026; rated "questionable"). Source: [Wccftech, 2026-10-26](https://wccftech.com/samsung-sk-hynix-downgraded-hbm4-q2-2027-nvidia-rubin-ultra/)
- **Power and cooling**
  - [CHIP-CO: NVIDIA, 20 May 2025]
    - 54 V rack distribution "starts hitting physical limits" above 200 kW. A MW-scale Kyber rack at 54 V would need up to 64U of power shelves and up to 200 kg of copper busbar per 1 MW rack (200,000 kg per 1 GW).
    - 800 VDC supports 1 MW IT racks starting in 2027, coinciding with Kyber.
    - The 800 V sidecar can power 576 Rubin Ultra GPUs in one Kyber rack.
    - Source: [NVIDIA Technical Blog, "NVIDIA 800 V HVDC Architecture Will Power the Next Generation of AI Factories," 2025-05-20](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/)
  - [CHIP-CO: Huawei, via Mydrivers] The Atlas 350 card draws 600 W, about 1.5x the H20. Source: [TrendForce, 2026-03-23](https://www.trendforce.com/news/?p=54956)
  - [INDEPENDENT: IEEE Spectrum] Power data is sparse in MLPerf: only Lenovo submitted power in Training (June 2025). Source: [IEEE Spectrum, 2025-06-04](https://spectrum.ieee.org/nvidia-blackwell-mlperf-training-5)
- **Interconnect (scale-up domains)**
  - [CHIP-CO disclosures at Hot Chips 2026] Google TPU 8i: 1,152 chips via OCS. TPU 8t: 9,600-chip superpods and up to 134,400 TPUs. AMD Helios: 72 GPUs over Ethernet. OpenAI Jalapeño: 128-chip domain. Source: [Semiconductor Engineering, 2026-09-09](https://semiengineering.com/can-gpus-continue-to-dominate-ai-compute/)
  - [CHIP-CO: NVIDIA] Kyber: 576 GPUs per rack (2027). Source: [NVIDIA, 2025-05-20](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/)
  - [COMPANY-AUTHORED: Google] TPU v4: 4,096-node 3D torus, routing around failures by OCS. Source: [NSDI '24](https://www.usenix.org/conference/nsdi24/presentation/zu)
  - [INDEPENDENT: MLCommons] A heterogeneous inference system spanning the Pacific was submitted in v6.1. Source: [MLCommons, 2026-09-16](https://mlcommons.org/2026/09/mlperf-inference-v6-1-results/)
- **Manufacturing: yields, costs, EUV vs DUV**
  - [SUPPLIER] TSMC N2 dilutes gross margin by about 3–4 points in 2H26 (July 2026). N2 rose from 3% of wafer revenue (Q2 2026) to 8% (Q3 2026). TSMC cites tool-price inflation. Sources: [The Motley Fool, 2026-07-16](https://www.fool.com/earnings/call-transcripts/2026/07/16/tsm-tsm-q2-2026-earnings-call-transcript/); [TSMC 6-K, 2026-10-15](https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000726/a3q26e_withguidancexfinal.htm)
  - [PRESS] TSMC wafer prices rise 3–6% from January 2027, with the steepest increases on 2nm and 3nm (Liberty Times). CoWoS rises up to 20% (Commercial Times). Source: [TrendForce, 2026-10-27](https://www.trendforce.com/news/2026/10/27/news-tsmc-reportedly-eyes-20-cowos-price-hike-skips-equipment-price-renegotiations-amid-ai-demand-surge/)
  - [INDEPENDENT: TechInsights] SMIC N+3 is DUV-based and less scaled than 5nm; low yields are expected on large AI dies (December 2025 and March 2026). Sources: [TechInsights, 2025-12-11](https://www.techinsights.com/blog/smic-n3-confirmed-kirin-9030-analysis-reveals-how-close-smic-5nm); [TechInsights, 2026-03-17](https://www.techinsights.com/ja/node/61228)
- **Efficiency and reliability**
  - [COMPANY-AUTHORED: Google] 0.24 Wh per median Gemini text prompt, down 33x over the preceding 12 months (paper dated 21 Aug 2025). Source: [arXiv 2508.15734, 2025-08-21](https://arxiv.org/abs/2508.15734)
  - [INDEPENDENT: SemiAnalysis] Throughput per provisioned MW is software-dependent: B200 rose from about 300k to about 500k tok/s per MW at 50 tok/s/user in about six weeks (April to June 2026). Source: [InferenceX, 2026-06-09](https://inferencex.semianalysis.com/blog/deepseekv4-16t-day-0-to-day-43-performance)
  - [CUSTOMER: Meta] On 16,384 H100s there was one unexpected interruption about every 3 hours (419 in 54 days); GPUs and HBM3 together accounted for 47.3%. Source: [arXiv 2407.21783](https://arxiv.org/pdf/2407.21783)
  - [COMPANY-AUTHORED: Google] TPU v4: 99.98% availability; about 1% of jobs affected by hardware outages. Source: [NSDI '24](https://www.usenix.org/conference/nsdi24/presentation/zu)
  - [COMPANY doc: Google Cloud] Using more TPUs raises the chance of a maintenance event, and Google recommends checkpointing about every hour. Source: [Google Cloud, "Prepare for maintenance events"](https://docs.cloud.google.com/tpu/docs/maintenance-events)

### Inferences
- A 14-reticle CoWoS package (2028) would be roughly 12,000 mm² of interposer if one reticle is about 858 mm². That is still about a quarter of a ~46,000 mm² wafer-scale die. Both the 858 mm² and the WSE area are commonly cited figures that I did not re-source here (see Gaps).
- The Llama 3 interruption rate (419 in 54 days, about 7.8 per day) implies about 0.00047 unexpected interruptions per GPU per day. This is my arithmetic.

### Gaps
- Not re-sourced in this pass: the reticle field of 26 × 33 mm ≈ 858 mm²; Cerebras WSE-3 die area and transistor count.
- Rack power: no source opened for GB200/GB300 NVL72 at about 120–140 kW, Vera Rubin NVL144 power, or Rubin Ultra Kyber at about 600 kW. NVIDIA's blog gives only the >200 kW limit and the 1 MW target.
- Liquid-cooling limits and supply: not found.
- Copper versus optical scale-up reach in meters, and any supplier statements on it: not found.
- N3/N2 yields and wafer prices in US$: not found.

---

## 6. Check of the three unverified leads supplied with the assignment

### Takeaway
- Lead 1 (CoWoS about 35k → 70–75k → 100k+) is broadly confirmed as analyst/press estimates. The 75k upper bound was not found. TSMC itself publishes no wpm figures.
- Lead 2 is confirmed for SK hynix in substance, though its wording was "completed discussions" rather than "sold out". It is not verified for Micron's 2026 supply from an opened primary source.
- Lead 3 is confirmed for HBM4, by NVIDIA's CEO in June 2026. The HBM3E 12-high "pass" in late 2025 was only a press report from unnamed sources and was disputed at the time.

### Cited Findings
- **Lead 1: TSMC CoWoS about 35k wpm (end-2024) → about 70–75k (end-2025) → 100k+ (end-2026).**
  - 35k (2024), about 70k (end-2025 projection) and 90k (end-2026 projection). Source: [TrendForce, citing Commercial Times / institutional investors, 2024-12-13](https://www.trendforce.com/news/2024/12/13/news-tsmc-ramps-up-cowos-capacity-across-taiwan-projected-to-nearly-triple-by-2026/)
  - About 70k wpm in 2025. Source: [TrendForce, 2026-08-05](https://www.trendforce.com/news/2026/08/05/news-tsmc-reportedly-expands-outsourcing-of-key-cowos-front-end-step-to-osats-amid-rising-nvidia-asic-demand/)
  - End-2026 estimates of 115–140k ([TrendForce, 2026-04-16](https://www.trendforce.com/news/2026/04/16/news-tsmc-says-cowos-offers-industrys-largest-reticle-size-packaging-amid-intel-emib-rivalry-copos-advances/)), 120–140k ([TrendForce, 2026-06-15](https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-reportedly-seen-narrowing-from-20-to-10-by-end-2026-as-capacity-expands/)), 130–140k ([TrendForce, 2026-08-05](https://www.trendforce.com/news/2026/08/05/news-tsmc-reportedly-expands-outsourcing-of-key-cowos-front-end-step-to-osats-amid-rising-nvidia-asic-demand/)) and more than 130k ([TrendForce, 2026-10-27](https://www.trendforce.com/news/2026/10/27/news-tsmc-reportedly-eyes-20-cowos-price-hike-skips-equipment-price-renegotiations-amid-ai-demand-surge/)).
  - **Verdict:** Confirmed as estimates, and the end-2026 figure exceeds "100k+". The "75k" end-2025 upper bound was not found. Morgan Stanley's own capacity series was not found; only its demand and allocation estimates were.
- **Lead 2: SK hynix and Micron said their 2026 HBM supply was sold out.**
  - SK hynix (29 Oct 2025): "completed discussions with key customers regarding HBM supply for next year". Source: [SK hynix Newsroom](https://news.skhynix.com/sk-hynix-announces-3q25-financial-results/)
  - SK hynix (28 Oct 2026): DRAM and HBM "effectively sold out" through 2029. Source: [The Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/10/28/sk-hynix-skhy-q3-2026-earnings-call-transcript/)
  - Micron: the FQ1 2026 press release (17 Dec 2025) does not mention HBM ([Micron IR](https://investors.micron.com/news-releases/news-release-details/micron-technology-inc-reports-results-first-quarter-fiscal-2026)). The FQ4 2026 call (September 2026) says 2026 HBM prices "were negotiated with our customers last year" and that the "vast majority" of CY2027 HBM bit supply is under agreement ([Investing.com, 2026-09-30](https://www.investing.com/news/transcripts/earnings-call-transcript-micron-tops-q4-2026-estimates-as-demand-stays-hot-93CH-4925992)).
  - **Verdict:** SK hynix is confirmed in substance, though its exact words were "completed discussions" rather than "sold out". Micron's 2026 sold-out status is not verified from an opened primary source. Its 2027 status is "vast majority" under agreement.
- **Lead 3: Samsung passed NVIDIA qualification for HBM3E 12-high in late 2025 and for HBM4 in 2026.**
  - HBM3E 12-high: reported in September 2025 by the Korean Economic Daily and Business Korea from unnamed sources. Aju News said Samsung had "not yet received NVIDIA's formal approval". Neither company confirmed. Source: [TrendForce, 2025-09-22](https://www.trendforce.com/news/2025/09/22/news-samsung-12h-hbm3e-reportedly-clears-nvidia-tests-after-18-month-setback-hbm4-reaches-final-phase/)
  - HBM4: Hankyung reported (March 2026) that Samsung had "effectively passed" ([TrendForce, 2026-03-09](https://www.trendforce.com/news/2026/03/09/news-samsung-sk%E2%80%AFhynix-reportedly-tapped-as-nvidia-rubin-hbm4-suppliers-shipments-could-start-in-march/)). NVIDIA's CEO said on 5 Jun 2026 that all three vendors were "qualified" and "in production" ([TechTimes, relaying Reuters, 2026-06-05](https://www.techtimes.com/articles/317855/20260605/nvidia-vera-rubin-hbm4-jensen-huang-confirms-all-three-suppliers-production-q3-ship.htm)).
  - **Verdict:** The HBM4 part is confirmed by an NVIDIA on-record statement (June 2026). The HBM3E 12-high part is reported, not confirmed. The ZDNet Korea report (October 2026) adds that 8-high HBM4 for Rubin Ultra would need separate certification.

### Inferences
- None beyond the verdicts above.

### Gaps
- I did not retrieve Micron's December 2025 prepared remarks, which may contain the "entire CY2026 HBM supply" wording.
- I found no Samsung on-record confirmation of HBM3E 12-high qualification.

---

## 7. Contradictions found: where supplier statements or independent measurements contradict the seven companies' claims (with dates)

### Takeaway
Ten items are recorded below, numbered C1 to C10.
- **Hard contradictions:** C1 (Huawei / TechInsights) and C9 (Huawei HBM self-sufficiency versus reported foreign-HBM dependence).
- **Contradictions with earlier press reports:** C2 (NVIDIA "all three qualified" versus the March 2026 press account of Micron's role).
- **Rumor against an on-record supplier statement:** C3 (12-high HBM4 yields).
- **Claims that depend on the operating point, contradicted under some independent conditions:** C5 (AMD versus InferenceX), C6 (NVIDIA rack-scale versus InferenceX) and C7 (Cerebras multiples).
- **Timing or status tensions:** C4 (Vera Rubin) and C10 (Ascend 960 timing).
- **Claims not independently tested:** C8 (Google, AWS and Cerebras next-generation claims).

### Cited Findings
- **C1. Huawei Ascend supply chain: an independent teardown contradicts a purely domestic build.** In October 2025 TechInsights found TSMC-made dies and older Samsung/SK hynix HBM in multiple Ascend 910C samples ([Bloomberg, 2025-10-03](https://news.bloomberglaw.com/international-trade/huawei-used-tsmc-samsung-sk-hynix-components-in-top-ai-chips)). SemiAnalysis estimated more than 2.9M TSMC-fabricated Ascend dies and about 11.4M Samsung HBM stacks shipped to China ([SemiAnalysis, 2025-09-08](https://newsletter.semianalysis.com/p/huawei-ascend-production-ramp)). Supplier side: TSMC says it has not supplied Huawei since mid-September 2020 ([Reuters via BusinessWorld, April 2025](https://www.bworldonline.com/?p=664911), [UNOPENED]). This points to indirect diversion (the Sophgo case) rather than direct supply. I found no Huawei statement disclosing its foundry or HBM sources.
- **C2. NVIDIA HBM4 statement versus earlier press.** On 5 Jun 2026 Jensen Huang said all three vendors were qualified and in production for Vera Rubin ([TechTimes, 2026-06-05](https://www.techtimes.com/articles/317855/20260605/nvidia-vera-rubin-hbm4-jensen-huang-confirms-all-three-suppliers-production-q3-ship.htm)). Earlier, Hankyung reported (9 Mar 2026) that Micron would supply only mid-tier Rubin CPX and that SK hynix had not yet passed the 11 Gb/s tier ([TrendForce, 2026-03-09](https://www.trendforce.com/news/2026/03/09/news-samsung-sk%E2%80%AFhynix-reportedly-tapped-as-nvidia-rubin-hbm4-suppliers-shipments-could-start-in-march/)). The later on-record statement supersedes the press report. Which supplier feeds which SKU remains undisclosed.
- **C3. HBM4 12-high yield: rumor against a supplier statement.** On 28 Oct 2026 SK hynix said "HBM4 already exceeded its planned yield" and that 12-high shipments were "proceeding smoothly" ([The Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/10/28/sk-hynix-skhy-q3-2026-earnings-call-transcript/)). Two days earlier (26 Oct 2026), ZDNet Korea via Wccftech reported heat and declining yields in 12-high HBM4/HBM4E and NVIDIA talks on 8-high stacks for Rubin Ultra; the report is from unnamed sources and was rated "questionable" ([Wccftech](https://wccftech.com/samsung-sk-hynix-downgraded-hbm4-q2-2027-nvidia-rubin-ultra/)). Unresolved.
- **C4. Vera Rubin availability: a tension, not a direct contradiction.**
  - NVIDIA side: customer shipments start in Q3 2026 (NVIDIA position after GTC Taipei, June 2026, per [TechTimes](https://www.techtimes.com/articles/317855/20260605/nvidia-vera-rubin-hbm4-jensen-huang-confirms-all-three-suppliers-production-q3-ship.htm)). At Hot Chips (late August 2026) NVIDIA said it was "already ramping" at five clouds ([Semiconductor Engineering, 2026-09-09](https://semiengineering.com/can-gpus-continue-to-dominate-ai-compute/)).
  - Independent side: SemiAnalysis said on 24 Aug 2026 that Rubin "arrives later this month" ([SemiAnalysis](https://newsletter.semianalysis.com/p/agentx-inferencexv3-does-cuda-moat)). MLPerf Inference v6.1 (16 Sep 2026) listed Vera Rubin NVL72 only as "preview", meaning not commercially available at submission ([MLCommons](https://mlcommons.org/2026/09/mlperf-inference-v6-1-results/)).
  - A search summary also mentioned "reports" that volume Rubin shipments slipped into 2027; this could not be sourced and is unverified.
- **C5. AMD MI355X performance claims versus independent InferenceX results (dates matter).**
  - AMD side: in September 2026 AMD claimed +18% Offline and +11% SingleStream over "the selected NVIDIA B300 submission" in MLPerf v6.1 ([AMD blog](https://www.amd.com/en/blogs/2026/amd-delivers-its-broadest-mlperf-inference-6-1-submission.html), [UNOPENED]). An AMD technical article from March 2026 reportedly argued that the MI355X "often delivers comparable or better results than GB300 NVL72" using SemiAnalysis data ([AMD](https://www.amd.com/en/developer/resources/technical-articles/2026/the-many-aspects-of-inference-performance.html), [UNOPENED]; HTTP 503 when fetched).
  - Independent side: SemiAnalysis found the MI355X "falls well behind" in FP4 disaggregated serving (16 Feb 2026) ([InferenceX v2](https://inferencex.semianalysis.com/blog/inferencex-v2-nvidia-blackwell-vs-amd-vs-hopper)). It found NVIDIA leading most AgentX comparisons, B200 overtaking MI355X on perf/$ after 21 Aug 2026, and NVIDIA SGLang delivering more than 20x AMD on Qwen3.5 397B at 90 tok/s/user (24 Aug 2026) ([AgentX](https://newsletter.semianalysis.com/p/agentx-inferencexv3-does-cuda-moat)).
  - A third-party recomputation of MLPerf v6.1 gpt-oss-120b Server gives about 16,022 tok/s per GPU for GB300 against 14,155 for MI355X ([GPU Insights](https://gpuinsights.net/mlperf-inference-v6-1-per-gpu-results-2026/), [UNOPENED]).
  - AMD's claims hold only for selected scenarios and dates.
- **C6. NVIDIA rack-scale (NVL72) advantage versus InferenceX.** SemiAnalysis found GB200 NVL72 has "nearly no advantage" at about 130 tok/s/user and costs more per million tokens (February 2026). It found B200 and B300 beat GB200 and GB300 on TCO-normalized throughput for MiniMax M3 (August 2026). Sources: [InferenceX v2](https://inferencex.semianalysis.com/blog/inferencex-v2-nvidia-blackwell-vs-amd-vs-hopper); [AgentX](https://newsletter.semianalysis.com/p/agentx-inferencexv3-does-cuda-moat). In the other direction, InferenceX measured Blackwell gains of up to about 98–100x over an H100 baseline in one configuration, more than NVIDIA's GTC 2024 "up to 30x" claim. Separately, NVIDIA's Hot Chips 2026 claim of Vera Rubin NVL72 at "up to 30X" GB300 at high interactivity ([Semiconductor Engineering](https://semiengineering.com/can-gpus-continue-to-dominate-ai-compute/)) compares with 2.5–3.7x in NVIDIA's own MLPerf v6.1 preview entries ([StorageReview](https://www.storagereview.com/news/mlperf-inference-v6-1-5-7x-per-accelerator-gains-a-512-gpu-run-and-vera-rubins-first-peer-reviewed-numbers)) and 1.8–2.0x tokens per $ of TCO on InferenceX at 100 tok/s/user ([UNOPENED]). These are different metrics and operating points, not like-for-like.
- **C7. Cerebras speed multiples versus independent per-token measurements.** Cerebras (19 Sep 2025) claimed "~21x faster" than DGX B200 (end-to-end Llama 3 70B reasoning, "recalculated by Cerebras" from SemiAnalysis data) and 2,700+ against 900 tok/s on gpt-oss-120B citing AA ([Cerebras](https://www.cerebras.ai/blog/cerebras-cs-3-vs-nvidia-dgx-b200-blackwell)). AA-relayed figures for June 2026 show Cerebras at about 1,705–1,753 tok/s on gpt-oss-120B, about 2.4x the next-fastest API ([Fast.io](https://fast.io/resources/fastest-ai-2026/), [UNOPENED]). IEEE Spectrum (4 Jun 2025) called AA-based comparisons not apples-to-apples ([IEEE Spectrum](https://spectrum.ieee.org/nvidia-blackwell-mlperf-training-5)). The 21x figure is not reproduced by any independent per-token measurement found; it uses a different metric.
- **C8. Claims not independently tested.**
  - Google: TPU 8t/8i at "about 2x prior TPUs" (Hot Chips 2026). Ironwood was not submitted to MLPerf Inference v6.0 ([Tae Kim, 2026-04-01](https://taekim.substack.com/p/nvidia-wins-mlperf-ai-inference-benchmarks)). The only independent Ironwood data point found is a later InferenceX result I did not open: TPU v7 FP8 at 1.85–2.17x the tokens per $ of GB300 NVL72 FP8 on Qwen3.5-397B at 200 tok/s/user, with GB300 NVL72 FP4 leading at every matched point.
  - AWS [CHIP-CO, via secondary] [UNOPENED]: AWS says Trainium offers 30–40% better price-performance than GPU-based EC2 P5e/P5en ([Introl blog relaying the AWS claim](https://introl.com/blog/ai-accelerators-beyond-gpus-tpu-trainium-gaudi-cerebras)). There is no MLPerf or InferenceX Trainium data through August 2026 ([InferenceX v2](https://inferencex.semianalysis.com/blog/inferencex-v2-nvidia-blackwell-vs-amd-vs-hopper); [AgentX](https://newsletter.semianalysis.com/p/agentx-inferencexv3-does-cuda-moat)).
  - Cerebras: CS-4 "up to 10x throughput/W" (Hot Chips 2026).
  - None of these is contradicted; except for the unopened Ironwood result, all are unverified by independent measurement as of 14 Nov 2026.
- **C9. Huawei HBM self-sufficiency versus reported foreign dependence.**
  - Huawei side: Huawei presents the 950 series with self-developed HBM (HiBL 1.0) ([TrendForce, 2026-03-23](https://www.trendforce.com/news/?p=54956)).
  - Other side: The Information (via TrendForce, 3 Nov 2026) reports that Huawei's next chip will rely heavily on Samsung and SK hynix HBM and that customers are being asked to source memory, alongside smuggling ([TrendForce](https://www.trendforce.com/news/?p=66148)). Epoch AI (24 Sep 2026) estimates the 2025 gap was filled by more than 10M foreign stockpiled stacks ([Epoch AI](https://epochai.substack.com/p/how-far-behind-nvidia-is-huawei)).
  - These are press and estimate sources, not supplier statements.
- **C10. Ascend 960 timing.** Huawei's roadmap gives Q4 2027 for the Ascend 960 ([TrendForce, 2026-03-23](https://www.trendforce.com/news/?p=54956)). The Information (via TrendForce, 3 Nov 2026) says the "960DT" is expected in Q1 2027 ([TrendForce](https://www.trendforce.com/news/?p=66148)). Not resolved.
- **Also: Huawei performance positioning versus independent estimates (not a contradiction of a specific Huawei claim).** Huawei compares the Atlas 350 with the H20 (2.8x FP4). Epoch puts the Ascend 950 at about 7x below the B300 and about half the H100 on an H100-equivalent basis, and estimates Huawei's 2026 compute at about 25x less than NVIDIA's ([Epoch AI](https://epochai.substack.com/p/how-far-behind-nvidia-is-huawei)).
- **Conflicts among independent sources** (not claims of the seven, but they affect any test):
  - TSMC's 2025 AI share: "high-teens" against "15%"; base period 2024–2029 against 2026–2030 (see 1C).
  - NVIDIA's 2026 CoWoS: 595k wafers (Morgan Stanley, December 2025) against 800–850k (Mydrivers, August 2026) (see 1B).
  - TSMC Arizona packaging start: 2028 or 2029 (see 1D).
  - Samsung HBM3E 12-high: Korean Economic Daily/Business Korea against Aju News, September 2025 (see 2B).
  - Nittobo T-glass share: about 90% or "just over half" (see 3).
  - Optics shortage end: end-2026 (LightCounting) or 2028 (see 3).
  - SemiAnalysis's "one-month" HBM enforcement gap against a law-firm summary reporting no delayed compliance date (see 2D).

### Inferences
- The most consequential independent contradiction found concerns supply-chain provenance: Huawei's Ascend 910C is built on TSMC dies and Korean HBM. Performance claims by NVIDIA, AMD and Cerebras are mostly true under some conditions and contradicted under others. Testing them needs date-, model- and operating-point-matched comparisons.

### Gaps
- I found no supplier statement directly contradicting a capacity or shipment claim by NVIDIA, AMD, Broadcom, Google, Amazon or Cerebras.
- Specific company shipment claims (for example, NVIDIA's bookings figures or AMD's MI450 launch timing) were not retrieved, so they could not be tested against supplier data.

---

## 8. What could not be found or verified (consolidated)

### Takeaway
The main unverified areas are: TSMC node capacity in wafers; CoWoS variant and SoIC splits; supplier-confirmed customer allocations; Samsung's sold-out status; HBM qualification for AMD, Google, AWS and Broadcom; the 2024–2025 MLPerf rounds; Trainium and Ascend independent benchmarks; liquid cooling; rack-power figures; and N2 yields and prices. The shared web-search budget ran out mid-task, so several of these may be findable in a follow-up.

### Cited Findings
- None. This section lists gaps only.

### Inferences
- None.

### Gaps
- **TSMC**
  - N4, N3 and N2 capacity in wafers/month for 2024–2027.
  - Split across CoWoS-S, CoWoS-L and CoWoS-R; SoIC capacity.
  - TSMC's January 2025 statement on AI accelerators' share of 2024 revenue.
  - Official TSMC transcripts; third-party ones were used.
  - Outcome of the US Commerce probe into TSMC and Sophgo, and any penalty, as of 14 Nov 2026.
  - TSMC's own Arizona packaging start date (2028 or 2029).
- **Allocation**
  - Supplier-confirmed CoWoS allocation by customer: none exists publicly.
  - Opened sources for the JPMorgan, GF Securities, TrendForce and Counterpoint TPU and Trainium unit estimates.
- **HBM**
  - Samsung's 2026/2027 sold-out status and its Q3 2026 earnings remarks.
  - Micron's December 2025 wording on CY2026 HBM supply.
  - HBM4 qualification for AMD MI450/MI455X and for Google, Amazon and Broadcom programs by name.
  - Rubin per-GPU HBM capacity and bandwidth from an opened source.
  - Samsung's on-record confirmation of HBM3E 12-high qualification.
- **China**
  - The US Commerce estimate that Huawei can make about 200k AI chips in 2025, attributed to Jeffrey Kessler in June 2025 testimony: not found in this pass.
  - TechInsights' paywalled SMIC yield and capacity figures.
  - CXMT HBM production volumes.
  - Huawei's CloudMatrix384 paper and independent performance data for Ascend 950 (InferenceX showed traces only, June 2026).
- **Benchmarks**
  - MLPerf 2024 rounds (Inference v4.0/v4.1, Training v4.0/v4.1) and the 2025 rounds Inference v5.1 and Training v5.1, including which of the seven submitted. I have only unverified recollection that AMD first submitted to Inference v4.1 (August 2024).
  - Which hardware Google used in its 2026 MLPerf submissions.
  - Whether Training v6.1 results have been published by 14 Nov 2026.
  - InferenceMAX launch date and details.
  - Any independent Trainium benchmark.
  - AA hardware result tables.
- **Papers**
  - ISCA, MICRO, HPCA and ISSCC 2025–2026 papers on these seven companies' chips.
  - Hot Chips 2026 slide decks (only press summaries were used).
  - Any non-Google peer-reviewed study of TPU reliability.
- **Physical limits**
  - A source for the reticle field (26 × 33 mm ≈ 858 mm²) and for Cerebras WSE die area.
  - GB200/GB300 NVL72 rack power (about 120–140 kW) and Rubin Ultra Kyber (about 600 kW).
  - Liquid-cooling supply constraints.
  - Copper versus optical scale-up reach.
  - N3/N2 yields and wafer prices.
  - ABF capacity and pricing.
- **Scheduled events that had not happened as of 14 Nov 2026** (status per sources above):
  - TSMC Arizona fab 2 volume production: Q3 2027.
  - TSMC 2027 wafer price increases: January 2027.
  - Micron Singapore HBM packaging output: early CY2027.
  - Ascend 960: Q1 or Q4 2027, sources disagree.
  - Rubin Ultra 8-high HBM4 volume: Q2 2027 (rumored).
  - NVIDIA Kyber/800 VDC and 1 MW racks: 2027 (NVIDIA-stated).
  - TSMC 9.5-reticle CoWoS: 2027 (slide reading). 14-reticle CoWoS: 2028. CoPoS: 2028–29. SoW-X: 2029. A14 volume: 2028.
  - InferenceX coverage of Trainium3: announced in February 2026 for "later this year" but not found.
