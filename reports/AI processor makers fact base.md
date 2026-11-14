# Outside evidence tests seven AI chipmakers' claims

As of 14 November 2026, independent evidence for the seven AI-processor businesses covered here is far stronger for the chips they already ship than for the ones they are launching. MLPerf results from many non-vendor submitters measure NVIDIA's Blackwell and AMD's MI355X, customers such as Apple show Google's TPUs running at frontier scale, Epoch AI's site analysis confirms the scale of Amazon's Trainium2 deployment, Artificial Analysis measures Cerebras's per-user inference speed and SemiAnalysis accepts Huawei's CloudMatrix compute figures. By contrast, NVIDIA's Vera Rubin, AMD's MI455X/Helios, Google's TPU 8, Trainium3/4, Huawei's Ascend 950, Broadcom-built XPUs such as OpenAI's Jalapeño and Cerebras's CS-4 rest almost entirely on vendor claims, and in 2026 Broadcom-built XPUs, Trainium, Ascend and Cerebras made no MLPerf submissions, while Google's 2026 entries that could be checked ran on NVIDIA systems rather than TPUs. Buyers' filings confirm contracts larger than the vendors announced: Anthropic's S-1/A of 10 November 2026 shows **at least $121.3B with Google, $161.2B of rent on Broadcom-built TPU racks, at least $110B with Amazon, and NVIDIA-GPU compute commitments of up to about $254B** ([Anthropic S-1/A No. 2](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm)). Much of that demand is financed by the vendors themselves, through NVIDIA's **$108.5B** of guarantees, Broadcom's roughly **$72B** of residual-value backstops and AMD's warrants over 320M shares, a pattern the Federal Reserve described as a "circular financing" dynamic on 13 November 2026 ([Federal Reserve FSR](https://www.federalreserve.gov/publications/files/financial-stability-report-20261113.pdf)). Supply is the constraint all of them share: TSMC says packaging capacity is "limiting my customers' growth" and SK hynix says its HBM is "effectively sold out" through 2029. Governance and delivery events cut across all of this, since NVIDIA's chief executive resigned (event date 11 November 2026 in the 8-K, filed 12 November), Huawei awaits a verdict in its Brooklyn criminal trial, and Cerebras's own 10-Q discloses a capacity shortfall to OpenAI. Several of these facts will change within weeks, starting with NVIDIA's results on 17 November 2026.

**Disclosure.** An AI system made by Anthropic produced this report. Anthropic appears throughout the material as a customer, borrower, investee or counterparty of several of the companies covered (Google, Amazon, Broadcom, NVIDIA and AMD) and of others such as Microsoft, SpaceXAI, Nscale, Lambda and Fluidstack. Every fact about Anthropic is taken from the documents cited, chiefly its S-1 and S-1/A filings of October and November 2026, its public announcements, and the vendors' filings and calls; no other information about Anthropic was used. The report ranks no company, makes no recommendation and offers no investment opinion, and the company sections follow a fixed order (NVIDIA, AMD, Broadcom, Google, Amazon, Huawei, Cerebras) that implies nothing about merit.

## How this fact base was built, and where its evidence stops

**Sources.** The report synthesizes nine research-notes files: one for each company, one on the shared supply chain and independent technical evidence, and one on buyers, contracts, vendor financing and cross-company claims. Every research track hit the session's shared web-search limit partway through, after which the researchers relied on primary documents fetched directly. These were SEC filings (10-K, 10-Q, 8-K, S-1, S-1/A, 424B4, 13F and DEF 14A), earnings-call transcripts published by third parties (Motley Fool, Investing.com, TickerTrends and StockAnalysis, which may contain transcription errors), company pages, MLCommons results, the Federal Register and central-bank reports. Some sites blocked automated access, including Reuters, DCD, investors.broadcom.com and openai.com, so several items are known only from search-result summaries or secondary relays and are marked as such.

**Provenance labels.** Every figure carries its date or period and an inline source, and a label in square brackets gives its provenance.

| Label | Meaning |
|---|---|
| **[CS]** | Company-stated |
| **[IND: who]** | Independently measured or verified, with the verifier named |
| **[BUY]** | Stated by a buyer or customer, which is outside the vendor but an interested party |
| **[SUP]** | Stated by a supplier |
| **[REG]** | Stated by a regulator or government |
| **[EST: who]** | An analyst or industry estimate |
| **[PRESS]** | Press reporting with named or observable sourcing |
| **[PRESS-U]** | Press reporting that cites unnamed sources |
| **[UNOPENED]** | The page was seen only as a search-result summary |
| **(calc)** | Arithmetic performed on cited figures |

**Dates and fiscal years.** Fiscal calendars differ by company, which matters when comparing periods.

| Company | Fiscal year ends |
|---|---|
| NVIDIA | Late January (FY2027 ends January 2027) |
| Broadcom | Early November (FY2026 ended 1 November 2026) |
| AMD | Late December |
| Microsoft | June |
| Oracle | May |

**Allegations and assessments.** Where the press reports allegations about individuals that have not been adjudicated, the report attributes them to the named outlet, marks them unverified and does not name private individuals who are their subject. The "solid ground" assessment in each company section judges the technical and engineering evidence only, not business or investment merit.

## NVIDIA: audited Blackwell results, unaudited Rubin multiples, and a chief executive gone

### Facts: a $96B quarter, Rubin shipments from August 2026, and an 8-K dated 11 November

**What NVIDIA ships, and at what stage.** At 14 November 2026 the volume products are still Blackwell and Blackwell Ultra (B200, B300, GB200 NVL72, GB300 NVL72). NVIDIA said on 26 August 2026 that "our Blackwell architecture remains the vast majority of our revenue" [CS] ([NVIDIA Q2 FY27 CFO commentary, 26 Aug 2026](https://s201.q4cdn.com/141608511/files/doc_financials/2027/Q227/Q2FY27-CFO-Commentary.pdf)). Blackwell production systems first shipped in Q4 FY2025 (November 2024 to January 2025) and brought in **$11.0B** that quarter [CS] ([NVIDIA FY2025 10-K, filed 26 Feb 2025](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/nvda-20250126.htm); [Q4 FY25 CFO commentary, 26 Feb 2025](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000021/q4fy25cfocommentary.htm)). GB300 production units followed in May to July 2025 [CS] ([NVIDIA FY2026 10-K, filed 25 Feb 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)).

Vera Rubin is the successor. On 26 August 2026 NVIDIA said "we commenced production shipments of Vera Rubin earlier this month", that purchase orders had come "from every major hyperscaler, AI cloud, and system OEM", and that it expected Rubin to be **about 20% of Q3 FY27 data-center revenue** [CS] ([Q2 FY27 earnings call transcript, 26 Aug 2026](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf)). The 10-Q places the start of production shipments in Q3 FY27, the quarter that began on 27 July 2026 [CS] ([NVIDIA Q2 FY27 10-Q, filed 26 Aug 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)). The product page, accessed 14 November 2026, lists these figures per Rubin GPU: **50 PF NVFP4 inference (sparse), 35 PF NVFP4 training (dense), 288 GB of HBM4 at 19.2 TB/s, and 3 TB/s of NVLink**. Per NVL72 rack it lists 3,600 PF and 20.7 TB of HBM4. It gives no rack power figure [CS] ([NVIDIA Vera Rubin NVL72 page](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)).

The Vera CPU is "in full production", with shipments to OCI and SpaceXAI and, from Q3 FY27, to AWS. Grace CPU revenue exceeds **$5B on a trailing-twelve-month basis**. NVIDIA's "preliminary expectation" is for CPU revenue to more than double in FY2028 [CS] ([Q2 FY27 call, 26 Aug 2026](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf)).

The December 2025 Groq licence produced the Groq 3 LPX rack. It holds 256 LPUs, each with 1.2 PFLOPS FP8 and 500 MB of SRAM at 150 TB/s. NVIDIA's Ian Buck said in March 2026 that the LPU "does not yet support CUDA natively" [CS via press] ([CNBC, 16 Mar 2026](https://www.cnbc.com/2026/03/16/nvidia-gtc-2026-ceo-jensen-huang-keynote-blackwell-vera-rubin.html); [thegpu.ai, Mar 2026](https://thegpu.ai/p/nvidia-gtc-2026-full-breakdown)). NVIDIA declared the LPX "in full production" at Hot Chips in August 2026 and said volume shipments would follow "later this quarter", with Nebius first [CS] ([Q2 FY27 call](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf)). No confirmation that volume shipments occurred by the quarter's end on 25 October 2026 was found.

Rubin CPX, a prefill processor announced in September 2025 for end-2026, does not appear in NVIDIA's 2026 releases or on the 26 August call. One GTC recap called it "set aside", but that is the author's inference, not an NVIDIA statement [PRESS] ([thegpu.ai, Mar 2026](https://thegpu.ai/p/nvidia-gtc-2026-full-breakdown)). Rubin Ultra in the Kyber rack is a 2027 item. It was described as 576 GPUs per rack in May 2025, counting dies, and as 144 GPUs in March 2026, counting packages. Feynman is a 2028 item [CS] ([NVIDIA 800 V blog, 20 May 2025](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/); [CNBC, 16 Mar 2026](https://www.cnbc.com/2026/03/16/nvidia-gtc-2026-ceo-jensen-huang-keynote-blackwell-vera-rubin.html); [Jon Peddie Research, 17 Mar 2026](https://www.jonpeddie.com/news/nvidia-gtc-2026-keynote/)). Hopper survives mainly as the H200. US licences have allowed "small amounts" of it to go to China since February 2026, and those shipments were **under 1% of data-center revenue** in Q2 FY27 [CS] ([Q2 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)).

**Which milestones were met, which slipped, and which are pending.** The table below tracks each public commitment against the record.

| Commitment (date, venue) | Status at 14 Nov 2026 | Evidence |
|---|---|---|
| Blackwell B200/GB200 (GTC, 18 Mar 2024) | **Slipped, then met.** NVIDIA made a mask change "to improve production yield" and took $908M of provisions for low-yielding Blackwell material in Q2 FY25. The production ramp began in Q4 FY25. | [CS] [Q2 FY25 10-Q, 28 Aug 2024](https://www.sec.gov/Archives/edgar/data/1045810/000104581024000264/nvda-20240728.htm) |
| Blackwell Ultra in H2 2025 (GTC, Mar 2025) | **Met.** GB300 production units shipped May–Jul 2025. | [CS] [FY26 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm) |
| Rubin in 2026 (Computex, Jun 2024); "in production this time next year, maybe slightly earlier" (GTC DC, 28 Oct 2025) | **Met.** Production shipments began in August 2026. | [PRESS] [Next Platform, 29 Oct 2025](https://www.nextplatform.com/ai/2025/10/29/as-rackscale-gpu-systems-boom-big-green-is-emphatically-red-white-and-blue/1640768); [CS] [Q2 FY27 call](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf) |
| "Rubin is in full production" (CES, 5 Jan 2026) | **Wording contradicted** by NVIDIA's own later "ramping into full production" (May–Aug 2026) and by production shipments starting in August 2026. Partner availability in H2 2026 was met. | [CS] [CES release, 5 Jan 2026](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer); [PRESS] [Startup Fortune, 22 Jul 2026](https://startupfortune.com/nvidia-confirms-vera-rubin-is-shipping-but-not-the-630-billion-number/) |
| OpenAI's first gigawatt on Vera Rubin in H2 2026 (LOI, 22 Sep 2025) | **Not confirmed.** The Ohio campus that now anchors the relationship comes online "in phases beginning in 2028"; the 10-Q puts the first phase in FY2029. | [CS] [LOI release](https://nvidianews.nvidia.com/news/openai-and-nvidia-announce-strategic-partnership-to-deploy-10gw-of-nvidia-systems); [SB Energy release, 17 Aug 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/sbeoainvidia-portsrelease.htm) |
| Groq 3 LPX ships in Q3 2026 (GTC, 16 Mar 2026) | **Partly met.** "Full production" was declared in August 2026; volume shipments are unconfirmed. | [CS] [Q2 FY27 call](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf) |
| Rubin CPX for end-2026 (Sep 2025) | **Unclear.** | [PRESS] [thegpu.ai](https://thegpu.ai/p/nvidia-gtc-2026-full-breakdown) |
| Rubin Ultra/Kyber, 800 VDC and 1 MW racks (2027); Feynman (2028) | **Pending.** Rubin Ultra was "not yet in silicon production" as of late March 2026. | [CS] [800 V blog](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/); [PRESS] [network-switch.com, 30 Apr 2026](https://network-switch.com/blogs/news/what-comes-next-ai-hardware-outlook-april-2026) |

Two other episodes complete the record. The first is a downward revision of Rubin's specifications. GTC 2026 recaps gave per-GPU HBM4 bandwidth of **22 TB/s**; the product page now says **19.2 TB/s**. The CES release gave NVLink 6 at **3.6 TB/s per GPU and 260 TB/s per rack**; the page now says **3 TB/s and 216 TB/s**. A third party (Understanding Machine, as cited by Tech Insider) dated the change to early September 2026, and NVIDIA has given no reason [CS] ([product page](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/); [CES release](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer)); [PRESS] ([Tech Insider, Mar 2026, updated later](https://tech-insider.org/nvidia-gtc-2026-rubin-gpu-analysis/)). The second is a set of ramp problems reported in mid-2026. KeyBanc's John Vinh flagged "thermal lid issues", which Barron's later reported resolved, with the ramp starting in July 2026. SemiAnalysis pointed to difficulty manufacturing advanced rack components [EST/PRESS] ([Startup Fortune, 22 Jul 2026](https://startupfortune.com/nvidia-confirms-vera-rubin-is-shipping-but-not-the-630-billion-number/)).

The late-2024 GB200 NVL72 rack overheating reports could not be verified because Reuters could not be fetched. A January 2026 article conflated them with the 2024 yield fix ([The Decoder, 6 Jan 2026](https://the-decoder.com/ces-2026-nvidia-promises-five-times-the-ai-performance-and-ten-times-cheaper-inference-with-vera-rubin/)).

**Vera Rubin's timing, reconciled.** The four markers of Rubin's progress describe different stages, so read in order they mostly do not contradict each other. "Full production" at CES on 5 January 2026 described silicon status. NVIDIA used "ramping into full production" around 31 May 2026. On 21 July 2026 it said NVL72 racks were already running at CoreWeave, Google Cloud, Azure and OCI. Production shipments began in early August, and at Hot Chips in late August NVIDIA said Rubin was "already ramping" at five clouds ([Semiconductor Engineering, 9 Sep 2026](https://semiengineering.com/can-gpus-continue-to-dominate-ai-compute/)).

MLCommons published Inference v6.1 on 16 September 2026 with Vera Rubin NVL72 in the **"preview"** category. That means the system was not commercially available when it was submitted, which happened before publication [IND: MLCommons] ([MLCommons, 16 Sep 2026](https://mlcommons.org/2026/09/mlperf-inference-v6-1-results/)). The notes do not give the v6.1 submission deadline, so how preview status lines up with the August shipment date cannot be checked exactly.

Buyers then reported receiving the hardware. On 11 September 2026 Oracle said "NVIDIA Vera systems are performing better than expected" [BUY] ([Oracle Q1 FY27 call, 11 Sep 2026](https://www.fool.com/earnings/call-transcripts/2026/09/11/oracle-orcl-q1-2027-earnings-call-transcript/)). On 29 October 2026 Microsoft said it had "docked our first NVIDIA Vera Rubin GPUs" [BUY] ([Microsoft Q1 FY27 call, 29 Oct 2026](https://www.fool.com/earnings/call-transcripts/2026/10/29/microsoft-msft-q1-2027-earnings-call-transcript/)).

The only clear contradiction is therefore the January "full production" wording. A search-engine summary of "reports" that volume Rubin shipments slipped into 2027 could not be traced to any source and is unverified. For comparison, SemiAnalysis wrote on 24 August 2026 that Rubin "arrives later this month" ([SemiAnalysis, 24 Aug 2026](https://newsletter.semianalysis.com/p/agentx-inferencexv3-does-cuda-moat)). No reported Rubin revenue figure will exist until the Q3 FY27 report on **17 November 2026**.

**Revenue, margins, cash and debt.** All figures are company-reported. The 10-K figures are audited; the 10-Q figures are reviewed.

| US$ | FY2025 (to 26 Jan 2025) | FY2026 (to 25 Jan 2026) | Q1 FY27 (to 26 Apr 2026) | Q2 FY27 (to 26 Jul 2026) |
|---|---|---|---|---|
| Revenue | 130.5B | 215.9B | 81.6B | **96.2B** |
| Data Center revenue | 115.2B | 193.7B | 75.2B (recast 75.25B) | 89.0B (Hyperscale 48.7B; AI Clouds, Industrial & Enterprise 40.3B) |
| GAAP gross margin | 75.0% | 71.1% (H20 charge) | 74.9% | 75.0% |
| GAAP operating income | 81.5B | 130.4B | 53.5B | 63.7B |
| GAAP net income | 72.9B | 120.1B | 58.3B | 59.7B |
| Cash and marketable debt securities | 43.2B | 62.6B | 50.3B | 56.6B |
| Debt (short-term / long-term) | – / 8.5B | 1.0B / 7.5B | 1.0B / 7.5B | 1.0B / **32.4B** |
| Inventory | 10.1B | 21.4B | 25.8B | 31.6B |
| Supply and capacity commitments | 30.8B | 95.2B | 119B | **279B**, "primarily … memory" |

Sources: [FY25 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/nvda-20250126.htm); [Q4 FY26 release, 25 Feb 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000019/q4fy26pr.htm); [FY26 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm); [Q1 FY27 release, 20 May 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000051/q1fy27pr.htm); [Q1 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000052/nvda-20260426.htm); [Q2 FY27 release, 26 Aug 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27pr.htm); [Q2 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm).

Revenue has beaten NVIDIA's own guidance in each reported FY2027 quarter. Q1 FY27 guidance was $78.0B and the actual was $81.6B; Q2 guidance was $91.0B and the actual was $96.2B. Guidance for Q3 FY27 is **$108.0B ±2% with a 74.0% gross margin, "assum[ing] no China Data Center compute revenue"** [CS] ([Q2 FY27 CFO commentary](https://s201.q4cdn.com/141608511/files/doc_financials/2027/Q227/Q2FY27-CFO-Commentary.pdf)).

Management expects margins to "bottom in Q4 in the 71% to 72% range" because of "extreme pricing conditions in memory". It gave a "preliminary expectation" of about **70% revenue growth in FY2028**, calling that a "supply-constrained outlook". It also said "we expect supply to remain a bottleneck at least through the end of fiscal year 2028" [CS] ([Q2 FY27 call](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf)).

The balance sheet changed character in 2026. NVIDIA issued **$25.0B of notes on 18 June 2026**, in seven tranches due 2028–2056 at coupons of 4.250%–5.625% ([8-K, 18 Jun 2026](https://www.sec.gov/Archives/edgar/data/1045810/000119312526275783/d48176d8k.htm)). It reported "equity investments of $99 billion and equity investment commitments of $25 billion as of July 26, 2026". It also reported $36B of new six-year "AI cloud agreements" under which it buys back capacity, and credit-support guarantees with **maximum gross exposure of $108.5B**, of which $105B relates to an OpenAI-leased site in Ohio [CS] ([Q2 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)).

Days sales outstanding rose from 45 to **60 days** "due to extended payment terms on large, multi-quarter agreements with certain investment-grade customers". Operating cash flow was $24.1B in Q2 FY27 and free cash flow $21.3B [CS] ([Q2 FY27 CFO commentary](https://s201.q4cdn.com/141608511/files/doc_financials/2027/Q227/Q2FY27-CFO-Commentary.pdf)).

The non-GAAP basis changed in Q1 FY27 to include stock-based compensation. In Q2 one company was reclassified from AI Clouds to Hyperscale "due to a change in their business model", which recast Q1 Hyperscale from $37.9B to $43.05B [CS] ([Q1 FY27 CFO commentary](https://s201.q4cdn.com/141608511/files/doc_financials/2027/Q127/Q1FY27-CFO-Commentary.pdf); [Q2 FY27 CFO commentary](https://s201.q4cdn.com/141608511/files/doc_financials/2027/Q227/Q2FY27-CFO-Commentary.pdf)).

Customer concentration is high. Two direct customers took 22% and 14% of FY2026 revenue, and one took 16% in Q2 FY27. NVIDIA also estimates that "one AI research and deployment company contributed a meaningful amount of our revenue by purchasing cloud services from our customers" [CS] ([FY26 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm); [Q2 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)).

**China: two numbers that measure different things.** NVIDIA's 10-Q says "we were effectively foreclosed from competing in China's data center computing/compute market". H200 shipments under the February 2026 licences were "a fraction of the allowed shipments" and under 1% of data-center revenue. NVIDIA took a **$0.4B H200 charge "as the demand for H200 products diminished"**, and Q1 FY27 had "no shipments of Data Center Hopper products to China" [CS] ([Q2 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm); [Q1 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000052/nvda-20260426.htm)).

The same 10-Q reports China (including Hong Kong) revenue of **$7.88B in Q2 FY27**, against $3.99B a year earlier, and $12.43B for H1 FY27. That geographic line counts revenue by the headquarters location of the *direct* customer, and NVIDIA notes that "the end customer and shipping location may be different" [CS] ([Q2 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)). The first figure is data-center compute sold into China. The second covers all product lines, including gaming and other non-data-center products, booked to China-headquartered direct customers wherever the goods go.

The two coexist only if most of the $7.88B is non-data-center products and/or sales to China-headquartered customers for use elsewhere. NVIDIA does not break it out, so that composition is an inference, not a disclosed fact.

**Bookings and visibility claims are not backlog.** On 28 October 2025 Jensen Huang claimed "visibility into half a trillion dollars of cumulative Blackwell and early ramps of Rubin through 2026" over "the next five quarters" [CS via press] ([Next Platform, 29 Oct 2025](https://www.nextplatform.com/ai/2025/10/29/as-rackscale-gpu-systems-boom-big-green-is-emphatically-red-white-and-blue/1640768)). On 16 March 2026 CNBC reported that he expected "purchase orders between Blackwell and Vera Rubin to reach $1 trillion through 2027" [CS via press] ([CNBC, 16 Mar 2026](https://www.cnbc.com/2026/03/16/nvidia-gtc-2026-ceo-jensen-huang-keynote-blackwell-vera-rubin.html)).

On 26 August 2026 the CFO replaced dollar framing with the 70% FY2028 growth guide. On the same call Bernstein's Stacy Rasgon estimated that this implied about $200B more than "the prior outlook … $1 trillion over the three years" [EST]. Colette Kress also said: "each generation of NVIDIA infrastructure deployed at PORTS-Pike could represent approximately 1.5 million NVIDIA GPUs, or approximately $150 billion to $200 billion in NVIDIA revenue"; AI labs "for which we expect to leverage our balance sheet" would contribute "roughly a quarter of our business next year"; and "We know some will call this circular financing. We see it differently." [CS] ([Q2 FY27 call](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf))

Neither the $500B nor the $1T figure is a GAAP backlog or remaining-performance-obligation disclosure. Neither has been audited, and no customer-side confirmation of either total was found.

**Customers and contracts: binding versus announced.**

*OpenAI.* NVIDIA's 22 September 2025 letter of intent said NVIDIA "intends to invest up to $100 billion … progressively as each gigawatt is deployed" [CS] ([LOI release](https://nvidianews.nvidia.com/news/openai-and-nvidia-announce-strategic-partnership-to-deploy-10gw-of-nvidia-systems)). It was never disclosed as finalized. NVIDIA's 10-K of 25 February 2026 said "there is no assurance" of an agreement [CS] ([FY26 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)), and Huang said on 1 February 2026 that "it was never a commitment" [CS via press] ([Fortune, 2 Feb 2026](https://fortune.com/2026/02/02/jensen-huang-nvidia-ceo-on-openai-investment-never-a-commitment/)).

What replaced the LOI is a **$30B equity investment** in OpenAI's February 2026 round, which is press-reported and not itemized in NVIDIA's filings ([CNBC, 27 Feb 2026](https://www.cnbc.com/2026/02/27/open-ai-funding-round-amazon.html)). There is also a **binding residual-value guarantee capped at $105B** for about 4.25 IT-GW leased to an OpenAI affiliate for 20 years in Pike County, Ohio. NVIDIA holds an option on roughly 3.75 more IT-GW and is investing $1.5B in SB Energy [CS] ([8-K, Item 1.01, 17 Aug 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/nvda-20260817.htm); [SB Energy release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/sbeoainvidia-portsrelease.htm)). NVIDIA said on 26 August 2026 that "OpenAI's existing and planned commitments represent approximately 12 gigawatts of NVIDIA Compute" [CS] ([Q2 FY27 call](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf)).

*Anthropic.* In November 2025 NVIDIA agreed, "subject to certain closing conditions", to invest up to $10B in Anthropic [CS] ([Q3 FY26 10-Q, 19 Nov 2025](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000230/nvda-20251026.htm)). Anthropic's S-1/A of 10 November 2026 lists NVIDIA as a **$10.0B buyer in the concurrent private placement**, and it is not stated whether that amount is the same commitment. The S-1/A also shows NVIDIA-GPU compute commitments made through intermediaries [BUY] ([Anthropic S-1/A No. 2, 10 Nov 2026](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm)):

| Counterparty | Commitment |
|---|---|
| Microsoft | at least $47.2B, up to $49.2B, "regardless of actual usage" |
| SpaceXAI | up to $120.5B, cancellable on 90 days' notice after early 2027 |
| Nscale | about $44.6B, dependent on Nscale's financing |
| Lambda | about $41.3B, of which about $34.9B is currently terminable |

*CoreWeave.* A binding $6.3B order form obliges NVIDIA "to purchase the residual unsold capacity through April 13, 2032". NVIDIA also bought $2B of CoreWeave shares at $87.20 on 23 January 2026 [CS/BUY] ([CoreWeave 8-K, 15 Sep 2025](https://www.sec.gov/Archives/edgar/data/1769628/000176962825000047/crwv-20250909.htm); [CoreWeave 8-K, 26 Jan 2026](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000044/crwv-20260123.htm)).

*Announcements without disclosed binding terms.* Several large arrangements are announced but have no disclosed binding terms: **Meta:** a "multiyear, multigenerational" partnership for "millions" of GPUs with no dollar value ([NVIDIA, 17 Feb 2026](https://nvidianews.nvidia.com/news/meta-builds-ai-infrastructure-with-nvidia)). **AWS:** "deploying an additional 2 million GPUs … through the second quarter of fiscal 2029". This is company-stated only, with no AWS confirmation found ([Q2 FY27 call](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf)). **HUMAIN:** "several hundred thousand" GPUs over five years ([NVIDIA, 13 May 2025](https://nvidianews.nvidia.com/news/saudi-arabia-and-nvidia-to-build-ai-factories-to-power-next-wave-of-intelligence-for-the-age-of-reasoning)). **Financing platforms:** with Apollo, BlackRock, Blackstone, Brookfield, Goldman Sachs and KKR "to mobilize over $500 billion of third-party capital … subject to definitive agreements" ([Q2 FY27 release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27pr.htm)). **An unnamed "frontier AI lab":** NVIDIA will provide "selective credit enhancement for nearly 2 gigawatts of compute".

NVIDIA signed a definitive agreement on 2 September 2026 to buy **Hugging Face for about $11.9B**, plus up to about $1.0B of retention equity. Closing is expected in H1 2027 [CS] ([8-K, 3 Sep 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000078/nvda-20260902.htm)). On 30 June 2026 its 13F showed stakes in:

| Holding | Value at 30 Jun 2026 |
|---|---|
| Intel | $29.99B |
| SpaceX | $20.98B |
| CoreWeave | $4.70B |
| Coherent | $3.07B |
| Nokia | $2.21B |
| Synopsys | $2.15B |
| Nebius | $329M |

[CS] ([NVIDIA 13F, filed 14 Aug 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000065/information_table.xml))

**Capacity.** NVIDIA's supply commitments rose "from $119 billion last quarter to $279 billion, primarily related to the procurement of memory". Huang said "our entire supply chain is challenged, and everybody is really running flat out" [CS] ([Q2 FY27 CFO commentary](https://s201.q4cdn.com/141608511/files/doc_financials/2027/Q227/Q2FY27-CFO-Commentary.pdf); [Q2 FY27 call](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf)).

On 5 June 2026 Huang said all three HBM vendors (SK hynix, Samsung and Micron) "have been qualified" and "are in production" for Vera Rubin. Analysts put SK hynix at about 60–70% of Rubin's HBM4 [CS via Reuters; EST] ([TechTimes, 5 Jun 2026](https://www.techtimes.com/articles/317855/20260605/nvidia-vera-rubin-hbm4-jensen-huang-confirms-all-three-suppliers-production-q3-ship.htm)).

TSMC does not disclose allocations. Morgan Stanley estimated in December 2025 that NVIDIA would take about **595k of roughly 1M CoWoS wafers in 2026 (about 60%)** [EST: Morgan Stanley] ([36Kr, 4 Dec 2025](https://eu.36kr.com/en/p/3580962946874242)). A Mydrivers report relayed in August 2026 put NVIDIA's reservation at 800–850k wafers [EST/PRESS] ([TrendForce, 5 Aug 2026](https://www.trendforce.com/news/2026/08/05/news-tsmc-reportedly-expands-outsourcing-of-key-cowos-front-end-step-to-osats-amid-rising-nvidia-asic-demand/)).

The first US-made Blackwell wafer came out of TSMC Arizona on 17 October 2025. NVIDIA did not say where it is packaged [CS] ([NVIDIA blog, 17 Oct 2025](https://blogs.nvidia.com/blog/tsmc-blackwell-manufacturing/)). NVIDIA expects neocloud partners to end 2026 with **8 GW** installed, up from about 3 GW at end-2025 [CS] ([Q2 FY27 call](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf)).

**Ownership and key people, including the resignation.** The 2026 proxy reports holdings as of 23 March 2026 [CS] ([DEF 14A, filed 12 May 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000036/nvda-20260512.htm)):

| Holder | Shares | Stake |
|---|---|---|
| Jensen Huang | 870,604,104 | **3.58%** |
| Vanguard Capital Management | – | 7.31% (13G as of 31 Mar 2026) |
| BlackRock | – | 7.43% (13G/A as of 31 Dec 2023, stale) |

Form 4s show Huang sold 6.0M shares (about $1.05B) between 20 June and 29 October 2025 under a 10b5-1 plan, and made no open-market sales in 2026 through 12 November 2026 [derived from SEC Form 4s] ([EDGAR insider filings](https://www.sec.gov/cgi-bin/own-disp?action=getissuer&CIK=0001045810)).

The sequence of the leadership change, as the company's documents give it, is as follows.

**8 November 2026.** The board announced an independent investigation after "recent reports that CEO Jensen Huang was 'the target of a foreign intelligence effort'". It said it "has no reason to believe national security or NVIDIA's secrets were compromised" and expressed confidence in Huang [CS] ([NVIDIA board statement, 8 Nov 2026](https://nvidianews.nvidia.com/news/statement-from-nvidia-board-of-directors)). The same day NVIDIA published Huang's message to employees. In it he acknowledged personal misconduct ("unfaithful to my wife") and said he would cooperate fully [CS] ([NVIDIA, 8 Nov 2026](https://nvidianews.nvidia.com/news/a-message-to-our-company)). **10 November.** The independent directors retained former acting US Attorney Joon H. Kim and Wachtell, Lipton, Rosen & Katz [CS] ([statement, 10 Nov 2026](https://nvidianews.nvidia.com/news/statement-from-the-independent-members-of-the-nvidia-board)). **11 November.** The Form 8-K reports that the board "accepted the resignation of Jen-Hsun Huang, as NVIDIA's President, Chief Executive Officer and member of the Board, effective immediately". **The 8-K gives 11 November 2026 as the event date. It was filed on 12 November 2026** together with the release "NVIDIA Announces CEO Transition", which is dated 12 November. The two share one EDGAR accession number ([8-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000082/nvda-20261111.htm); [release, 12 Nov 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000082/nvidiaannouncesceotransiti.htm)). This explains the 11-versus-12 November difference between the notes files: one dates the resignation, the other the announcement. **What the filing says.** Colette Kress, 59, CFO since 2013, is interim CEO and remains CFO. Harvey C. Jones, 73, a director since 1993, becomes the "first-ever Chair". The search "will consider internal and external candidates". No reason is given. The release says customer commitments and the roadmap "continue without interruption" [CS] ([NVIDIA Newsroom, 12 Nov 2026](https://nvidianews.nvidia.com/news/nvidia-announces-ceo-transition)).

Press accounts of the reasons are unverified and are attributed here to their outlets: CNBC's live coverage relayed reports that Huang had a relationship with a Singapore-based businesswoman whom US intelligence reportedly suspects of working for Chinese intelligence. CNBC noted that "the U.S. government has not presented proof of espionage". The New York Times (11 November) reported a relationship with an NVIDIA vice president. Reuters, citing two unnamed sources, reported a relationship with a second NVIDIA employee. Huang denies compromising national security or company secrets. [PRESS/PRESS-U, unverified] ([CNBC live updates, 12 Nov 2026](https://www.cnbc.com/2026/11/12/nvidia-jensen-huang-ceo-live-updates.html); [Al Jazeera, 12 Nov 2026](https://www.aljazeera.com/news/2026/11/12/why-did-nvidia-ceo-jensen-huang-resign-and-who-is-colette-kress)). The Information reported, and CNBC said it had not verified, that Kress had opposed the $105B OpenAI guarantee [PRESS-U].

According to CNBC, Congress responded as follows: Senator Tim Scott requested that Huang testify on **3 December 2026** and that Commerce Secretary Lutnick testify on **10 December 2026**. Senator Wyden and Representative Neal opened an investigation into export approvals for NVIDIA chips to China-linked companies. Representative Mast said Huang had agreed to testify.

NVIDIA's shares closed down 4.3% on 12 November [PRESS] ([CNBC live updates, 12 Nov 2026](https://www.cnbc.com/2026/11/12/nvidia-jensen-huang-ceo-live-updates.html)). Earlier in 2026 there were other changes at the top: director Persis Drell resigned (20 January); Suzanne Nora Johnson joined the board (13 July); and Ajay Puri retired, with Nicholas Parker named EVP of Worldwide Field Operations from about 24 August [CS] ([DEF 14A](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000036/nvda-20260512.htm)).

**Legal and regulatory matters.** These run along five tracks.

*US export controls.* An April 2025 licence requirement on the H20 led to a **$4.5B charge**, and the licences granted in August 2025 produced only "approximately $60 million in H20 revenue". The US government's "expectation" of 15% or more of licensed revenue was never codified [CS] ([FY26 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)). The H200 licences of February 2026 require inspection in the US, so each unit carries a 25% import tariff that NVIDIA has been "unable to pass along" [CS] ([Q2 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)).

*China's measures.* NVIDIA's filings say China's government "encouraged customers to purchase from our China-based competitors" and "publicly questioned whether our H20 products have built-in vulnerabilities" [CS] ([FY26 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)). On 15 September 2025 China's market regulator (SAMR) issued a preliminary finding that NVIDIA had violated the conditions attached to its Mellanox approval. No final decision or penalty had been disclosed as of 26 August 2026 [CS] ([Q2 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)).

*US antitrust.* Reuters reported on 28 October 2026, citing two unnamed sources, that the US Justice Department is asking questions about the Hugging Face deal, within a broader antitrust probe that has examined the Run:ai, SchedMD and Groq deals [PRESS-U] ([Let's Data Science relaying Reuters, 28 Oct 2026](https://letsdatascience.com/news/doj-reportedly-opens-inquiry-into-nvidias-hugging-face-acqui-b6f36063)).

*France.* The French Competition Authority is "questioning whether gaming GPUs and data center GPUs are separate product categories" [CS] ([Q2 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)).

*US courts.* In the 2018 crypto-disclosure securities case (4:18-cv-07669-HSG), the court certified a class on 25 March 2026, and NVIDIA petitioned the Ninth Circuit on 8 April 2026 [CS] ([Q1 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000052/nvda-20260426.htm)). Employees of NVIDIA and Supermicro were reportedly indicted in August 2026 over alleged smuggling of AI servers to China. The docket was not obtained, and the charges are unadjudicated allegations [PRESS] ([Wikipedia, "Nvidia", citing Ars Technica](https://en.wikipedia.org/wiki/Nvidia)).

### Science: Blackwell stands on audited multi-party data; Rubin's headline multiples do not yet

**What is demonstrated and who verified it.** Blackwell-generation performance has been measured by parties NVIDIA does not control. MLPerf Training v6.0, published on 16 June 2026, contains 119 results from 24 submitters [IND: MLCommons] ([MLCommons, 16 Jun 2026](https://mlcommons.org/2026/06/mlperf-training-v6-0-results/); [MLCommons Training v6.0 results sheet](https://docs.google.com/spreadsheets/d/17Mek7pd_bKzfoA_ZiPt4E0jMcCZVE_dYbmsS8SUsJhw/edit)). They include 38 GB300, 20 B300, 15 GB200 and 10 B200 entries, many from Azure, CoreWeave, Oracle, Nebius, Dell, HPE and other non-NVIDIA submitters. MLPerf results are run by the submitting vendors and peer-reviewed by MLCommons.

The largest closed-division runs were: Llama 3.1 405B in **7.07 minutes on 8,192 GB200** (Azure); and DeepSeek-V3 671B in **2.02 minutes on 8,192 GB300** (CoreWeave).

At equal 8-GPU scale the results were as follows [IND: MLCommons].

| Benchmark | GB300 | B200 | AMD MI355X |
|---|---|---|---|
| Llama 2 70B LoRA | 5.61 min (Oracle) | 7.86 min (Supermicro) | 8.27 min (AMD) |
| Llama 3.1 8B | 63.5 min (HPE) | 82.2 min (Dell) | 86.8 min (AMD) |

The sheet has **no Google TPU, AWS Trainium or Rubin entries**.

In Inference v6.1 (16 September 2026), CoreWeave's GB300 NVL72 reached **1.16M tokens/s aggregate**. Vera Rubin NVL72 appeared only as a preview entry. On it NVIDIA reported up to **2.5x GB300 NVL72 on DeepSeek-R1 and 3.7x on a Qwen3 vision-language model**. These are NVIDIA-submitted numbers in the preview category, peer-reviewed by MLCommons [IND: MLCommons; CS for the multiples] ([StorageReview, 16 Sep 2026](https://www.storagereview.com/news/mlperf-inference-v6-1-5-7x-per-accelerator-gains-a-512-gpu-run-and-vera-rubins-first-peer-reviewed-numbers)).

SemiAnalysis's open InferenceMAX/InferenceX benchmark adds operating-point detail. Both NVIDIA and AMD supplied hardware or engineering help, which SemiAnalysis discloses.

**v1, 9 October 2025.** The B200 clearly beat the MI355X on Llama 3 70B at FP4. The MI355X had lower cost per million tokens on GPT-OSS 120B with vLLM. GB200 NVL72 had about 4x better total cost of ownership at about 35 tokens/s per user on DeepSeek FP8, but single-node B200 won above about 90 tokens/s per user on DeepSeek-R1 at FP4. Power was TDP-based, not measured [IND: SemiAnalysis] ([SemiAnalysis, 9 Oct 2025](https://newsletter.semianalysis.com/p/inferencemax-open-source-inference)). **v2, 16 February 2026.** GB200 NVL72 showed "nearly no advantage" at about 130 tokens/s per user. Blackwell reached up to about 98–100x an H100 disaggregated FP8 baseline at 116 tokens/s per user [IND: SemiAnalysis] ([InferenceX v2, 16 Feb 2026](https://inferencex.semianalysis.com/blog/inferencex-v2-nvidia-blackwell-vs-amd-vs-hopper)).

The largest customer-published reliability record is Meta's. Over a 54-day window on 16,384 H100s it saw 466 job interruptions, 419 of them unexpected. GPU issues caused 58.7% of the unexpected ones, and effective training time stayed above 90% [IND: Meta, customer paper] ([Llama 3 paper, arXiv 2407.21783, Jul 2024](https://arxiv.org/abs/2407.21783)).

**What remains unproven.** As of 14 November 2026, no independent measurement exists for Rubin's headline claims: "up to 10x lower inference cost per token" and 10x tokens per megawatt against GB200 NVL72, footnoted to Kimi-K2-Thinking at 32K/8K; "4x fewer GPUs" for training a projected 10-trillion-parameter mixture-of-experts model; up to 35x throughput per megawatt with Groq 3 LPX; and the "30x higher throughput per megawatt and 35x lower token cost relative to Grace Blackwell Ultra" given on the 26 August call. [CS] ([product page](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/); [CES release](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer); [Q2 FY27 call](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf))

Training at frontier scale in 4-bit NVFP4 rests on NVIDIA's own paper. It reports a 12B model trained on 10T tokens with loss "comparable to an FP8 baseline", with every author from NVIDIA, and no independent frontier-scale replication was found [CS] ([arXiv 2509.25149, rev. 4 Mar 2026](https://arxiv.org/abs/2509.25149)). Other claims are also unverified: co-packaged-optics switch reliability ("5x longer uptime"); the 800 VDC benefits (up to 5% efficiency, 30% lower TCO); and revenue-per-gigawatt figures of $18B for Hopper, $25B for Blackwell and $40B for Rubin. [CS] ([800 V blog](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/); [Q2 FY27 call](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf))

**Physical and engineering limits.**

*Reticle size.* Blackwell joins two reticle-limited dies of about 104B transistors each across the NV-HBI link [PRESS] ([Wikipedia, "Blackwell"](https://en.wikipedia.org/wiki/Blackwell_(microarchitecture))). Rubin is reported at 336B transistors on a TSMC 3nm-class process [CS via press] ([Tech Insider](https://tech-insider.org/nvidia-gtc-2026-rubin-gpu-analysis/)).

*Memory bandwidth.* JEDEC's HBM4 baseline is 8 Gb/s per pin across a 2,048-bit interface, about 2 TB/s per stack ([JEDEC via Business Wire, 16 Apr 2025](https://businesswire.com/news/home/20250416843598/en/JEDEC-and-Industry-Leaders-Collaborate-to-Release-JESD270-4-HBM4-Standard-Advancing-Bandwidth-Efficiency-and-Capacity-for-AI-and-HPC)). Assuming 288 GB comes from eight 36 GB stacks (an assumption; NVIDIA does not state stack count), 22 TB/s would need about 10.7 Gb/s per pin and 19.2 TB/s about 9.4 Gb/s. The downward revision is therefore consistent with HBM4 speed bins being a practical constraint. This arithmetic is from the notes; NVIDIA gives no reason for the revision. A Korean press report rated "questionable" by the outlet relaying it said NVIDIA was discussing 8-high HBM4 for Rubin Ultra because of heat and yield in 12-high stacks [PRESS-U] ([Wccftech, 26 Oct 2026](https://wccftech.com/samsung-sk-hynix-downgraded-hbm4-q2-2027-nvidia-rubin-ultra/)). Two days later SK hynix said on the record that "HBM4 already exceeded its planned yield" [SUP] ([SK hynix call, 28 Oct 2026](https://www.fool.com/earnings/call-transcripts/2026/10/28/sk-hynix-skhy-q3-2026-earnings-call-transcript/)).

*Power delivery.* NVIDIA itself states that 54 V rack distribution "begins to hit physical limits" above 200 kW, and that a 1 MW rack at 54 V could need up to 200 kg of copper busbar. That is why it plans 800 VDC with Kyber in 2027 [CS] ([800 V blog](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/)). No measured rack power for GB300 or Vera Rubin NVL72 was found.

*Interconnect reach.* NVL72 is a single-rack copper NVLink domain. Optical scale-up with co-packaged-optics switches is planned for Rubin Ultra [CS via press] ([thegpu.ai](https://thegpu.ai/p/nvidia-gtc-2026-full-breakdown)).

*Grid power.* The Ohio site needs at least 10 GW of new generation for 8 IT-GW [CS] ([SB Energy release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/sbeoainvidia-portsrelease.htm)).

*Test time.* Nomura estimates final-test time for Blackwell at about 4x Hopper's, and possibly 7x for Rubin [EST: Nomura] ([TrendForce, 27 Oct 2026](https://www.trendforce.com/news/2026/10/27/news-tsmc-reportedly-eyes-20-cowos-price-hike-skips-equipment-price-renegotiations-amid-ai-demand-surge/)).

**Whether it stands on solid ground.** For the shipping Blackwell generation, the technical evidence is solid. Many submitters NVIDIA does not control have produced MLCommons-reviewed results at up to 8,192 GPUs. Independent inference benchmarks reproduce Blackwell's advantages at many operating points and also show where they disappear. A customer has published reliability data at 16,384-GPU scale.

For Rubin the evidence is thinner. It consists of two preview MLPerf entries showing 2.5–3.7x, a set of vendor projections at 10–35x measured against inconsistent baselines, and memory and NVLink bandwidth figures that NVIDIA itself has revised down. Kyber, 800 VDC distribution and optical scale-up are 2027 engineering programmes with no field data. Energy per token at scale has not been independently measured: InferenceMAX uses TDP-based power, and NVIDIA's tokens-per-megawatt figures are projections.

### Cross-examination: twenty-plus tensions, most in forward-looking language

| NVIDIA claim (date) | Outside or later source (date) | Finding |
|---|---|---|
| "Rubin is in full production" (CES, 5 Jan 2026) | NVIDIA's own "ramping into full production" (May–Aug 2026); production shipments from Aug 2026 (10-Q); Vera Rubin NVL72 "preview" in MLPerf v6.1 (MLCommons, 16 Sep 2026) | Wording contradicted by the company's own later statements; availability in H2 2026 met |
| Rubin HBM4 22 TB/s; NVLink 3.6 TB/s per GPU (Mar and Jan 2026) | NVIDIA product page: 19.2 TB/s; 3 TB/s (accessed 14 Nov 2026) | Revised down by the company; no reason given |
| 10x vs GB200 NVL72 (product page) | 30x/35x vs the faster GB300 (CFO, 26 Aug 2026); 2.5–3.7x vs GB300 in MLPerf preview (16 Sep 2026); 1.8–2.0x tokens per $ of TCO vs GB300 at 100 tok/s/user ([InferenceX, Oct 2026, UNOPENED](https://inferencex.semianalysis.com/hardware)) | Baselines internally inconsistent; independent multiples far smaller and measured on different metrics |
| Groq deal "about $20 billion … asset deal" (CNBC, 24 Dec 2025 and 16 Mar 2026) | NVIDIA 10-K: non-exclusive licence, "no … equity interests were purchased", $13.0B + $4B (25 Feb 2026) | About $17B per company accounts, not $20B |
| OpenAI "up to $100 billion", first GW in H2 2026 (22 Sep 2025) | "No assurance" (10-Q, 19 Nov 2025); "never a commitment" (Huang, 1 Feb 2026); $30B equity (Feb 2026); Ohio site from 2028 (17 Aug 2026) | LOI superseded in practice; no filing says it was terminated |
| "We have not entered into any financing arrangements" (10-K, 25 Feb 2026) | $108.5B guarantees, $36B AI-cloud buybacks (10-Q, 26 Aug 2026); Federal Reserve on GPU makers' residual-value guarantees creating a "'circular financing' dynamic" [REG] ([Fed FSR, 13 Nov 2026](https://www.federalreserve.gov/publications/files/financial-stability-report-20261113.pdf)) | Tension; may be definitional, since "financing arrangements" is not defined in the filing |
| China H200 orders over 400,000 units (Huang, Mar 2026); "over two million" (Al Jazeera, 12 Nov 2026) | Under 1% of data-center revenue, $0.4B charge "as the demand for H200 products diminished" (10-Q, 26 Aug 2026) | Orders did not convert; the two press counts also conflict |
| "Effectively foreclosed" from China (10-Q) | China (incl. HK) revenue $7.88B in Q2 FY27 (same 10-Q) | Different measures (data-center compute into China vs all products by direct-customer HQ) |
| 2024 Blackwell delay blamed on rack overheating ([The Decoder, 6 Jan 2026](https://the-decoder.com/ces-2026-nvidia-promises-five-times-the-ai-performance-and-ten-times-cheaper-inference-with-vera-rubin/)) | Mask change for yield (10-Q, 28 Aug 2024); Huang: flaw "caused the yield[s] to be low" (Oct 2024) | Press conflated two issues |
| "Blackwell led across every category in the MLPerf Training 6.0 benchmarks" (26 Aug 2026) | MLCommons sheet: no TPU or Trainium entries; AMD absent from the 405B, DeepSeek-V3 and GPT-OSS tasks | Accurate within submissions; scope limited |
| "NVIDIA is a generation ahead … greater performance, versatility, and fungibility than ASICs" ([CNBC, 25 Nov 2025](https://www.cnbc.com/2025/11/25/nvidia-says-its-gpus-are-a-generation-ahead-of-googles-ai-chips.html)) | Google: TPU 8t/8i "up to 2.7 times better training performance and 80% better inference price performance"; Microsoft: Maia 300 "40% more tokens per watt compared to the leading GPU-based systems"; Amazon: Trainium's "meaningful advantage … in price performance" (28–30 Oct 2026) [BUY] | Opposing claims with undisclosed baselines; none independently testable |
| HBM4 suppliers "all three … qualified … in production" (5 Jun 2026) | Hankyung (9 Mar 2026): Micron for mid-tier Rubin CPX only [PRESS-U] ([TrendForce](https://www.trendforce.com/news/2026/03/09/news-samsung-sk%E2%80%AFhynix-reportedly-tapped-as-nvidia-rubin-hbm4-suppliers-shipments-could-start-in-march/)) | Later on-record statement supersedes; which supplier feeds which product is undisclosed |
| Rubin ramp on schedule | Microsoft: "some third-party capacity deliveries we expected in Q1 were delayed" (29 Oct 2026, supplier unnamed) [BUY] | Not attributable to NVIDIA from the transcript |
| Board "confidence" in Huang (8 Nov 2026) | Resignation accepted (8-K, event date 11 Nov 2026) | Reversal within three days |
| Q1 FY27 Hyperscale $37.9B (20 May 2026) | Recast to $43.05B (26 Aug 2026) | Reclassification of one customer |
| SB Energy option "approximately an additional 3.8 gigawatts" (8-K) | "the remaining 3.75 IT-GW" (joint release, same day) | Rounding |
| Top-5 hyperscaler capex "nearly $800 billion in 2026" (Kress, 26 Aug 2026) | Buyers' own 2026 guidance sums to about $720–740B for Alphabet, Amazon, Meta and Microsoft (calendar 2026) [BUY] ([Alphabet 10-Q](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm); [Amazon Q3 call](https://www.fool.com/earnings/call-transcripts/2026/10/30/amazon-amzn-q3-2026-earnings-call-transcript/); [Meta release](https://www.sec.gov/Archives/edgar/data/0001326801/000162828026066700/meta-09302026xexhibit991.htm); [Microsoft call](https://www.fool.com/earnings/call-transcripts/2026/10/29/microsoft-msft-q1-2027-earnings-call-transcript/)) | Close once a fifth company (Oracle) is added; definitions and fiscal years differ |

Buyers' filings support NVIDIA's demand claims in direction and scale: CoreWeave reports $132.3B of remaining performance obligations at 30 September 2026 and says "our current customers have contractually specified our use of NVIDIA GPUs" [BUY] ([CoreWeave 10-Q, filed 12 Nov 2026](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000465/crwv-20260930.htm)). Anthropic's filing shows NVIDIA-GPU compute commitments through intermediaries that sum to up to about $254B (calc: $47.2–49.2B Microsoft, up to $120.5B SpaceXAI, about $44.6B Nscale, about $41.3B Lambda) [BUY] ([Anthropic S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm)).

A share of that demand is underwritten by NVIDIA itself: through guarantees, capacity buybacks, and equity in OpenAI, Anthropic, CoreWeave, Nebius and SpaceX.

No supplier statement contradicting NVIDIA's capacity or shipment claims was found. TSMC said in July 2026 that packaging capacity "is so tight that now it's limiting my customers' growth", which is consistent with NVIDIA's "supply-constrained" framing [SUP] ([TSMC Q2 2026 call, 16 Jul 2026](https://www.fool.com/earnings/call-transcripts/2026/07/16/tsm-tsm-q2-2026-earnings-call-transcript/)).

## AMD: MI450 revenue began in Q3 2026; gigawatt-scale Helios is still a 2027 test

### Facts: data-center revenue up 97%, two gigawatts binding, and warrants for 320M shares

**Products and their stage.** Several Instinct GPUs are in customer production: the MI300X, MI325X, MI350X and MI355X.

**MI355X:** launched on 12 June 2025 (CDNA 4, 3 nm, 288 GB HBM3E, 8 TB/s) and "already rolling out" at Oracle Cloud Infrastructure [CS] ([AMD Advancing AI 2025 release, 12 Jun 2025](https://ir.amd.com/news-events/press-releases/detail/1255/amd-unveils-vision-for-an-open-ai-ecosystem-detailing-new-silicon-software-and-systems-at-advancing-ai-2025)). HUMAIN's MI355X GPU-as-a-service went live on 31 August 2026 [CS+BUY] ([AMD/Cisco/HUMAIN release, 31 Aug 2026](https://ir.amd.com/news-events/press-releases/detail/1298/amd-cisco-and-humain-expand-saudi-arabias-ai-infrastructure-as-amd-instinct-systems-go-live)). **MI455X:** the MI450-series part, launched at Advancing AI on 23 July 2026. On 3 November 2026 Lisa Su said "we started shipping MI455X in volume in the quarter". Q3 2026 was the first quarter of MI455X/Helios revenue, and she said a "big step up" is expected in Q4. No unit or dollar figures were given [CS] ([AMD Q3 2026 earnings call transcript, 4 Nov 2026](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/)). **MI455X specifications:** 320B transistors on TSMC 2 nm and 3 nm across 12 chiplets, with **432 GB of HBM4** [CS via press] ([iTWire, 24 Jul 2026](https://itwire.com/business-it-news/data/astounding-massive-dominant-ai-innovation-amd-launches-helios-against-nvidia-tips-up-to-us-5-billion-into-anthropic-and-books-roughly-14-gigawatts-of-customer-ai-compute-at-advanci)). **Helios rack:** pairs 72 MI455X GPUs with 6th-generation EPYC "Venice" CPUs and Pensando "Vulcano" NICs. AMD gives **2.9 exaflops FP4, 31 TB of HBM4 and 1.7 PB/s of memory bandwidth** per rack. Scale-up runs over "UALink and Ethernet, not NVLink" [CS via press] ([iTWire, 24 Jul 2026](https://itwire.com/business-it-news/data/astounding-massive-dominant-ai-innovation-amd-launches-helios-against-nvidia-tips-up-to-us-5-billion-into-anthropic-and-books-roughly-14-gigawatts-of-customer-ai-compute-at-advanci)). AMD's own release names only "AMD Pensando front-end, scale-up and scale-out networking" and does not mention UALink or Ultra Ethernet [CS] ([AAI 2026 release, 23 Jul 2026](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era)).

AMD has published no MI455X board power or Helios rack power. Introl estimates about 140 kW per rack, which AMD has not confirmed [EST: Introl] ([Introl](https://introl.com/blog/amd-helios-mi455x-nvidia-competition-ces-2026)).

AMD's 10-Q states that it does "not manufacture or sell the completed Helios rack-scale solutions". Its rack revenue is therefore component revenue, and ODMs and OEMs build and sell the racks [CS] ([AMD 10-Q Q3 2026, filed 4 Nov 2026](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm)). Helios systems from HPE, Dell, Lenovo and Supermicro are due to start shipping in Q4 2026.

Later products are announced but not shipping: MI430X for HPC and sovereign AI, shipping in H1 2027; MI500 (CDNA 6, 2 nm, HBM4E), planned for 2027; and MI600, planned for 2028. [CS] ([AMD CES 2026 release, 5 Jan 2026](https://ir.amd.com/news-events/press-releases/detail/1272/amd-and-its-partners-share-their-vision-for-ai-everywhere-for-everyone-at-ces-2026); [AAI 2026 release](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era))

AMD's software stack is ROCm. Under the ROCm.ai programme, releases now come every 6 weeks instead of every 4 months. AMD claims average gains over ROCm 7 on the same hardware of 3.3x in inference and 2.4x in training [CS] ([AMD Q2 2026 results, 8-K Ex. 99.1, 4 Aug 2026](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000121/q22026991.htm)).

**Milestones met, slipped and pending.**

| Commitment (date) | Status at 14 Nov 2026 | Source |
|---|---|---|
| MI325X production in Q4 2024 | **Met per AMD** (Su, 4 Feb 2025); customer timing not verified | [CS via press] [Next Platform, 5 Feb 2025](https://www.nextplatform.com/compute/2025/02/05/amd-moves-up-instinct-mi355x-launch-as-datacenter-biz-hits-records/1646757) |
| MI350 pulled in from H2 2025 to mid-2025 | **Met** (launched 12 Jun 2025) | [CS] [AMD, 12 Jun 2025](https://ir.amd.com/news-events/press-releases/detail/1255/amd-unveils-vision-for-an-open-ai-ecosystem-detailing-new-silicon-software-and-systems-at-advancing-ai-2025) |
| Helios with MI450 "expected to begin in Q3 2026" (Financial Analyst Day, 11 Nov 2025) | **Met on AMD's account**: first MI450 revenue in Q3 2026 | [CS] [FAD release](https://ir.amd.com/news-events/press-releases/detail/1266/amd-unveils-strategy-to-lead-the-1-trillion-compute-market-and-accelerate-next-phase-of-growth); [Q3 2026 release, 3 Nov 2026](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000188/q32026991.htm) |
| OpenAI's first 1 GW of MI450 "set to begin in the second half of 2026" (6 Oct 2025) | **Started, not complete.** OpenAI expects Helios online "beginning in the fourth quarter of 2026"; no warrant tranche had vested by 26 Sep 2026 | [CS] [AMD–OpenAI release](https://ir.amd.com/news-events/press-releases/detail/1260/amd-and-openai-announce-strategic-partnership-to-deploy-6-gigawatts-of-amd-gpus); [10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm) |
| Helios "on track for multi-gigawatt deployments beginning in 2H 2026" (21 May 2026) | **Pending**: only first racks confirmed | [CS] [AMD Taiwan release, 21 May 2026](https://ir.amd.com/news-events/press-releases/detail/1286/amd-announces-more-than-10-billion-in-taiwan-ecosystem-investments-to-accelerate-ai-infrastructure) |
| Meta's first GW: shipments "scheduled to begin in the second half of 2026" (24 Feb 2026) | **In progress**: Helios "installed and being tested by Meta" (27 Oct 2026) | [CS+BUY] [AMD–Meta, 24 Feb 2026](https://ir.amd.com/news-events/press-releases/detail/1279/amd-and-meta-announce-expanded-strategic-partnership-to-deploy-6-gigawatts-of-amd-gpus); [AMD–Meta, 27 Oct 2026](https://ir.amd.com/news-events/press-releases/detail/1302/amd-and-meta-advance-strategic-partnership-to-power-metas-superintelligence-infrastructure) |
| Anthropic's first GW "beginning in the first half of 2027" (22 Jul 2026) | **Pending** | [CS] [AMD–Anthropic release, 22 Jul 2026](https://ir.amd.com/news-events/press-releases/detail/1292/amd-and-anthropic-announce-strategic-partnership-to-deploy-up-to-2-gigawatts-of-amd-instinct-mi450-series-gpus) |
| MI430X H1 2027; MI500 2027; MI600 2028; 20x rack-scale energy efficiency by 2030 | **Pending** | [CS] [AAI 2026 release](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era) |

The one reported slip is disputed. On 16 February 2026 SemiAnalysis wrote that "first production tokens will only be generated on an MI455X UALoE72 by Q2 2027" because of "manufacturing delays", and that H2 2026 would see only engineering samples and low-volume production [EST: SemiAnalysis] ([SemiAnalysis, 16 Feb 2026](https://newsletter.semianalysis.com/p/inferencex-v2-nvidia-blackwell-vs)). The Next Platform relayed this along with "unconfirmed street rumors of a thermal design issue" ([Next Platform, 23 Feb 2026](https://www.nextplatform.com/compute/2026/02/23/amd-says-helios-racks-and-mi400-series-gpus-on-track-for-2h-2026/4092199)).

AMD's Forrest Norrod responded, "I have no idea where that's coming from". Press reported that software VP Anush Elangovan called the report "BS. Right on target for H2 2026" [CS via press] ([Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/amd-denies-report-of-mi455x-delays-as-nvidia-vr200-systems-are-rumored-to-arrive-early-company-says-helios-systems-on-target-for-2h-2026)).

The two positions concern different milestones, and both can be true: AMD's is volume chip shipments and first racks in Q3 2026, SemiAnalysis's is mass production and "production tokens" by Q2 2027. Customer schedules point to a 2027 volume ramp: OpenAI from Q4 2026, Anthropic in H1 2027 and HUMAIN's MI400 phase in 2027. Those dates leave room for SemiAnalysis's projection without AMD having missed its own Q3 2026 start commitment.

One search summary dated the SemiAnalysis report to May 2026. That is wrong: the primary piece is dated 16 February 2026.

**Revenue, margins, cash and debt.** All figures are company-reported.

| US$ millions | FY2024 | FY2025 | Q1 2026 | Q2 2026 | Q3 2026 (to 26 Sep 2026) |
|---|---|---|---|---|---|
| Revenue | 25,785 | 34,639 | 10,253 | 11,536 | **13,377** |
| GAAP / non-GAAP gross margin | 49% / 53% | 50% / 52% | 53% / 55% | 54% / 56% | 54% / 56% |
| Data Center revenue | 12,579 | 16,635 | 5,775 | 6,718 | **8,546** (+97% y/y) |
| Data Center operating income | 3,482 | 3,603 | 1,599 | 2,103 | 2,882 |
| GAAP net income | 1,641 | 4,335 | 1,383 | 2,297 | 2,428 |
| Free cash flow | 2,405 | 5,519 | 2,566 | 1,558 | 554 |

Sources: [AMD Q4/FY2025 release, 3 Feb 2026](https://ir.amd.com/news-events/press-releases/detail/1276/amd-reports-fourth-quarter-and-full-year-2025-financial); [Q1 2026 release, 5 May 2026](https://ir.amd.com/news-events/press-releases/detail/1284/amd-reports-first-quarter-2026-financial-results); [Q2 2026 8-K Ex. 99.1, 4 Aug 2026](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000121/q22026991.htm); [Q3 2026 8-K Ex. 99.1, 3 Nov 2026](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000188/q32026991.htm).

AMD's Q3 release says the 27% sequential rise in data-center revenue was "primarily driven by initial MI450 Series sales" and server growth. Each 2026 quarter beat its own guidance: Q1 $9.8B guided against $10.25B actual, Q2 $11.2B against $11.54B, and Q3 about $13B against $13.38B.

Guidance for Q4 2026 is about **$17.0B ±3%**, with data center up about 50% sequentially. CFO Jean Hu said Q4 2026 will be "the quarter data center AI business surpassed server business". For 2027 Su expects data-center AI revenue to "significantly more than double" and total revenue growth above 80% [CS] ([Q3 2026 call](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/)).

AMD has disclosed no Instinct revenue figure since 2024, when it was "just above $5 billion" [CS via press] ([Next Platform, 5 Feb 2025](https://www.nextplatform.com/compute/2025/02/05/amd-moves-up-instinct-mi355x-launch-as-datacenter-biz-hits-records/1646757)).

Export controls on the MI308 cost AMD **$800M in Q2 2025**. A reserve release of about $360M in Q4 2025 left a net FY2025 charge of about $440M [CS] ([Q4/FY2025 release](https://ir.amd.com/news-events/press-releases/detail/1276/amd-reports-fourth-quarter-and-full-year-2025-financial)).

The balance sheet at 26 September 2026 [CS] ([10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm)): **Cash and short-term investments:** $15.8B. **Debt:** $7.1B, up from $3.2B at year-end 2025, after **$4.75B of senior notes** issued on 17 August 2026. **Inventory:** $11.5B, up from $7.9B. **Prepaid expenses:** up $2.1B in nine months, "primarily due to prepayments of supply agreements". **Free cash flow:** $554M in Q3 2026, a 4% margin.

AMD has agreed two acquisitions, both expected to close by year-end 2026 subject to regulatory approval [CS] ([10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm)): **Taalas**, an inference-silicon company, for about $2.9B, including up to about $1.4B contingent; and **World Labs** for about $8.2B in stock.

The 10-Q ties both deals to "development of future super intelligence (SI) hardware, software and systems". Earlier, AMD sold ZT Systems' manufacturing business to Sanmina for $2.4B in cash plus shares, a deal completed in October 2025, and signed a 5-year manufacturing services agreement with Sanmina.

**Customer warrants and their accounting.** OpenAI (October 2025) and Meta (February 2026) each hold a warrant for up to **160M AMD shares at $0.01**, 320M combined. AMD accounts for the warrants as "consideration payable to a customer", so their grant-date fair value is booked as a reduction of revenue. At 26 September 2026 the position was [CS] ([10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm)): **Liability:** $1.2B, with a $1.2B non-cash remeasurement charge in Q3 2026. **Still to be recorded as contra-revenue:** $4.5B of unrecognized grant-date fair value. **Fair value:** $178.58 per share "as most market conditions had been met", against a $14.25 grant-date value. **Vesting:** "no warrant shares had vested or become exercisable".

Against 1,640M shares outstanding, one fully exercised warrant would equal about 8.9% of the enlarged share count; both together would be about 16.3% (calc).

**Customers and contracts.** AMD's 8-Ks contain two binding commitments, for **2 GW in total**: OpenAI's "binding commitment to purchase … the initial one (1) gigawatt of AMD Instinct MI450 Series GPU products" [CS] ([AMD 8-K, event date 5 Oct 2025](https://ir.amd.com/financial-information/sec-filings/content/0001193125-25-230895/0001193125-25-230895.pdf)); and Meta's "binding commitment to purchase the initial one (1) gigawatt equivalent" [CS] ([AMD 8-K, 23 Feb 2026](https://www.sec.gov/Archives/edgar/data/2488/000000248826000045/amd-20260223.htm)).

Everything beyond that is conditional or "up to". That includes the rest of the 6 GW each for OpenAI and Meta, which ties to warrant vesting with price hurdles escalating to $600 per share. It also includes Anthropic's "up to 2 gigawatts". iTWire's headline that AMD "books roughly 14 gigawatts" adds those ceilings together ([iTWire, 24 Jul 2026](https://itwire.com/business-it-news/data/astounding-massive-dominant-ai-innovation-amd-launches-helios-against-nvidia-tips-up-to-us-5-billion-into-anthropic-and-books-roughly-14-gigawatts-of-customer-ai-compute-at-advanci)).

AMD's own announcement with Anthropic (22 July 2026) gives "up to 2 gigawatts", with a "strategic equity investment of up to $5 billion in Anthropic in the future". It mentions no warrant and does not say whether the purchases are binding [CS] ([AMD–Anthropic release](https://ir.amd.com/news-events/press-releases/detail/1292/amd-and-anthropic-announce-strategic-partnership-to-deploy-up-to-2-gigawatts-of-amd-instinct-mi450-series-gpus)).

Anthropic's S-1/A is the buyer-side document. It describes a July 2026 Hardware Supply Agreement for MI450 Helios racks, with an initial tranche in 2027. Spend is expected to exceed **$20.0B** if the full initial capacity is procured, with an option for roughly the same amount again. It also describes AMD's commitment to buy up to $5.0B of Anthropic Class N stock, drawable on delivery milestones, and a further $2.5B AMD purchase in the IPO private placement [BUY] ([Anthropic S-1/A No. 2, 10 Nov 2026](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm)).

AMD has also agreed to invest $1B in Meta's equity offering [CS] ([AMD–Meta, 27 Oct 2026](https://ir.amd.com/news-events/press-releases/detail/1302/amd-and-meta-advance-strategic-partnership-to-power-metas-superintelligence-infrastructure)). AMD is therefore at once supplier, warrant issuer and investor to three of its Helios customers.

Other customers with dated, company-stated milestones are: **Microsoft:** Azure Helios deployment announced on 20 July 2026, with no gigawatt figure. **Oracle:** OCI clusters of "up to 131,072 MI355X GPUs". **US Department of Energy/ORNL:** the Lux and Discovery systems. **HUMAIN:** up to 250 MW of MI400 from 2027, within a 1 GW-by-2030 joint venture. **Others:** TensorWave, Vultr, Cirrascale, TCS, NAVER Cloud and EuroHPC's LUMI-AI. [CS/CS+BUY] ([AMD–Microsoft, 20 Jul 2026](https://ir.amd.com/news-events/press-releases/detail/1291/microsoft-to-deploy-next-gen-amd-instinct-and-amd-epyc-processors-as-the-companies-expand-their-long-term-strategic-partnership); [AMD–DOE, 27 Oct 2025](https://ir.amd.com/news-events/press-releases/detail/1264/amd-powers-u-s-sovereign-ai-factory-supercomputers-accelerating-an-open-american-ai-stack))

Oracle's reported 50,000-MI450 commitment from Q3 2026 could not be verified: Oracle's page returned 403. AMD says it "depend[s] on a small number of customers" and "generally do[es] not have long-term supply arrangements with our customers or minimum purchase requirements". It discloses only receivables concentration, with one customer at about 11% at 27 December 2025 [CS] ([AMD 10-K FY2025, filed 4 Feb 2026](https://www.sec.gov/Archives/edgar/data/2488/000000248826000018/amd-20251227.htm)).

**Capacity.** AMD relies on TSMC "for the production of all wafers for microprocessor and GPU products at 7 nanometer (nm) or smaller nodes" [CS] ([10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm)).

**Memory:** Samsung is the only HBM4 supplier AMD has named for the MI455X ("collaborating on HBM4 supply") [CS] ([Q1 2026 release](https://ir.amd.com/news-events/press-releases/detail/1284/amd-reports-first-quarter-2026-financial-results)). **Packaging, substrates and assembly:** AMD's Taiwan investments of more than $10B include work with ASE and SPIL on a 2.5D bridge interconnect and with PTI on a panel-based one. Unimicron, Nan Ya PCB and Kinsus supply substrates, and Sanmina, Wiwynn, Wistron and Inventec build Helios systems as ODMs [CS] ([Taiwan release, 21 May 2026](https://ir.amd.com/news-events/press-releases/detail/1286/amd-announces-more-than-10-billion-in-taiwan-ecosystem-investments-to-accelerate-ai-infrastructure)). **Supply position:** Su said on 3 November 2026 that "it is true that demand is higher than supply". She said AMD has secured wafers, substrates, advanced packaging and memory for 2027, and that it is sharing "inflationary pressures" with customers [CS] ([Q3 2026 call](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/)). **CoWoS estimates:** TSMC does not disclose allocations. Morgan Stanley estimated AMD at about **105k CoWoS wafers in 2026 (about 11%)** [EST: Morgan Stanley] ([36Kr, 4 Dec 2025](https://eu.36kr.com/en/p/3580962946874242)). An unopened secondary report says Morgan Stanley expects AMD's share to approach 20% in 2027 [EST, UNOPENED] ([Wccftech](https://wccftech.com/nvidias-cowos-ai-chip-packaging-demand-to-be-foreshadowed-in-2027-by-amd-due-to-agentic-ai-cpu-ramp-says-morgan-stanley/)).

**Ownership and key people.** As of 19 March 2026:

| Holder | Shares | Stake |
|---|---|---|
| Vanguard | 142.4M | 8.8% |
| BlackRock | 124.9M | 7.7% |
| Lisa Su | 4.3M | – |
| All directors and executive officers | – | under 1% |

[CS] ([AMD DEF 14A, filed 27 Mar 2026](https://www.sec.gov/Archives/edgar/data/2488/000119312526129057/d85856ddef14a.htm))

Lisa Su is Chair, President and CEO, and Jean Hu is EVP, CFO and Treasurer. Forrest Norrod runs data-center solutions, and ZT co-founder Doug Huang leads data-center platform engineering. Fei-Fei Li is to join as Chief Scientist when the World Labs deal closes [CS] ([Q3 2026 call](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/)).

**Legal and regulatory.** **China export licences.** The MI308 needed a US licence from April 2025. Some licences were granted, and AMD "began shipping products at the end of fiscal 2025". In H1 2026 the MI325 was licensed for certain China customers, subject to US inspection and therefore a **25% tariff** [CS] ([10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm)). **The 15% revenue share.** The 10-Q says US officials "expressed an expectation" in August 2025 of 15% of licensed MI308 revenue, but "to date, the U.S. government has not published a regulation establishing such requirement". No evidence that any payment was made was found. **Litigation and approvals.** AMD reported "no material legal proceedings" in Q3 2026. Pending regulatory items are approvals for Taalas and World Labs, and Hart-Scott-Rodino clearance on warrant exercise [CS] ([10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm); [OpenAI warrant 8-K](https://ir.amd.com/financial-information/sec-filings/content/0001193125-25-230895/0001193125-25-230895.pdf)).

### Science: MI355X verified on chosen workloads; ROCm composability and Helios at scale unproven

**What is demonstrated, and by whom.**

*MLPerf Inference v6.0 (1 April 2026).* On the workloads AMD submitted, the MI355X sits near the NVIDIA B200 in MLCommons-reviewed results. Nine partner submissions on AMD hardware came within 4% of AMD's own figures [IND: MLCommons results; percentages CS] ([The Decoder, 2 Apr 2026](https://the-decoder.com/nvidia-sets-new-mlperf-records-with-288-gpus-while-amd-and-intel-focus-on-different-battles/)). AMD's percentages for 8-GPU MI355X runs:

| Benchmark (mode) | vs B200 | vs B300 |
|---|---|---|
| Llama 2 70B (offline) | about equal | 92% |
| Llama 2 70B (server) | 97% | 93% |
| Llama 2 70B (interactive) | 119% | 104% |
| GPT-OSS-120B (offline) | 111% | 91% |
| GPT-OSS-120B (server) | 115% | 82% |

Multi-node MI355X runs of up to 94 GPUs passed **1M tokens/s**. AMD submitted nothing for DeepSeek-R1 or Qwen3-VL, while NVIDIA was the only vendor to submit every new model and scenario.

*MLPerf Inference v6.1 (16 September 2026).* Crusoe's **512-GPU MI355X** system reached 5.75M tokens/s offline on gpt-oss-120b, the largest system in the round [IND: MLCommons results via StorageReview] ([StorageReview, 16 Sep 2026](https://www.storagereview.com/news/mlperf-inference-v6-1-5-7x-per-accelerator-gains-a-512-gpu-run-and-vera-rubins-first-peer-reviewed-numbers)).

*MLPerf Training v6.0 (June 2026).* MI355X results on Llama 2 70B LoRA and Llama 3.1 8B were about 5% and 6% slower than B200 at 8 GPUs (8.27 vs 7.86 minutes; 86.8 vs 82.2 minutes) [IND: MLCommons] ([results sheet](https://docs.google.com/spreadsheets/d/17Mek7pd_bKzfoA_ZiPt4E0jMcCZVE_dYbmsS8SUsJhw/edit)). This was AMD's first multi-server training submission [CS] ([igor'sLAB](https://www.igorslab.de/en/amd-mlperf-training-6-0-instinct-mi355x-approaches-blackwell-scales-multiple-servers/)).

*Customer use.* Customers report running workloads on AMD, all company- or customer-stated: Meta and Microsoft: MI300X inference; Meta: "training, ranking and recommendation" on Instinct; Zyphra: pretrained an 8.3B-parameter mixture-of-experts model on 1,024 MI300X GPUs; and Anthropic: model bring-up on MI355X racks, per Su.

**What is contested.** SemiAnalysis's InferenceX testing, which AMD and NVIDIA engineers both supported, gives a mixed picture.

**February 2026.** It credited AMD's SGLang with better performance per TCO than NVIDIA's SGLang on single-node FP8. It also found AMD "not competitive" once disaggregated prefill, wide expert parallelism and FP4 are combined. It called AMD "more than six months behind" on distributed inference and found "zero Mi355X tests on vLLM" [IND: SemiAnalysis] ([SemiAnalysis, 16 Feb 2026](https://newsletter.semianalysis.com/p/inferencex-v2-nvidia-blackwell-vs)). **August 2026.** The B200 overtook the MI355X on performance per dollar for DeepSeek V4 Pro after vLLM optimizations on 21 August. The gap widened at high throughput "despite MI355X having 1.5x the HBM of B200" [IND: SemiAnalysis] ([InferenceX mirror, 25 Aug 2026](https://inferencex.semianalysis.com/blog/deepseek-v4-pro-agentx-mi355x-vs-b200-august)). The same series found the MI355X with AMD's ATOM engine ahead of GB300 NVL72 (vLLM) on performance per dollar for Kimi K3 in the 40–60 second latency band. On Qwen3.5 397B at 90 tokens/s per user, NVIDIA's SGLang delivered more than 20x AMD's throughput [IND: SemiAnalysis] ([SemiAnalysis, 24 Aug 2026](https://newsletter.semianalysis.com/p/agentx-inferencexv3-does-cuda-moat)).

Software matters as much as silicon here. MI355X interactivity on DeepSeek V4 went from 1–2 tokens/s per user on day zero to more than 100x that by late May 2026 ([InferenceX, 9 Jun 2026](https://inferencex.semianalysis.com/blog/deepseekv4-16t-day-0-to-day-43-performance)).

**What remains unproven.** None of the following has independent data as of 14 November 2026.

**MI455X throughput.** AMD claims **34x the token throughput of MI355X** (DeepSeek V4 Flash, FP4, AMD Performance Labs, July 2026) and "up to 18x tokens per dollar" [CS] ([AAI 2026 release](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era)). **Helios versus Vera Rubin.** AMD claims 15% more FP4, 50% more HBM, 50% more scale-out bandwidth and "up to 30% more tokens per dollar". These are AMD estimates on Kimi K2 Thinking with "projected hourly GPU pricing" [CS]. **Scale.** No MI455X or Helios entry exists in any MLPerf round reviewed. No gigawatt-scale Helios operation or frontier-scale pretraining run on AMD is documented. The largest documented AMD training run remains Zyphra's 1,024-GPU job.

**Physical and engineering limits.** **Memory capacity.** Each MI455X carries 432 GB of HBM4 against 288 GB per Rubin GPU, so Helios has 31.1 TB per rack against Vera Rubin NVL72's 20.7 TB, 50% more. SemiAnalysis's August finding shows memory capacity alone did not close the throughput gap at high load. **FP4 compute.** Helios's 2.9 EF FP4 is 15% above Vera Rubin's **dense** 2.52 EF but about 19% below NVIDIA's headline **sparse** 3.6 EF (calc from both vendors' pages). **Memory bandwidth.** The MI455X figure is disputed. AMD's brochure and TensorWave list 19.6 TB/s per GPU, while 1.7 PB/s per rack implies about 23.6 TB/s. If the part uses twelve 36 GB stacks (an assumption), those figures correspond to about 6.4 and about 7.7 Gb/s per pin, which would point to a change in specification (notes' arithmetic, unverified). **Scale-up without NVLink.** Scale-up over UALink and Ethernet across 72 GPUs has no independent latency or bandwidth measurement. **Yield.** The MI455X's 12 chiplets across N2 and N3 carry yield risks that AMD's own risk factors list as "design failures, packaging technology failures, process technology failures" [CS] ([10-Q](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm)).

**Whether it stands on solid ground.** For the MI300X and MI355X, the engineering ground is solid. Their usability in production inference is corroborated by multiple customers and by partner-reproduced MLPerf results within 4%, and their single-chip performance on selected workloads is near B200 under audited conditions.

Two claims rest on contested or absent evidence: **Broad cost-efficiency.** It holds on some stacks and contradicts SemiAnalysis's August 2026 results on others. **Software parity at multi-node scale.** It is not demonstrated.

MI455X and Helios performance rests only on AMD projections. Rack-scale Ethernet scale-up, gigawatt-scale deployment and frontier pretraining are untested in public. SemiAnalysis noted in February 2026 that "Google TPU, AWS Trainium, and Nvidia are the only AI chips with rack-scale designs deployed today" ([SemiAnalysis](https://newsletter.semianalysis.com/p/inferencex-v2-nvidia-blackwell-vs)).

### Cross-examination: chip-level claims hold on chosen tests; rack-level claims await data

| AMD claim (date) | Outside source (date) | Finding |
|---|---|---|
| Helios "on target for 2H 2026"; volume MI455X shipments in Q3 2026 (Feb and Nov 2026) | SemiAnalysis: production tokens by Q2 2027 (16 Feb 2026); OpenAI: Helios online "beginning in the fourth quarter of 2026" (Jul 2026); no warrant vesting at 26 Sep 2026 (10-Q) | Start date met on AMD's account; gigawatt-scale timing unverified |
| Meta "running models and workloads on the first Helios rack-scale systems" (AMD Q3 release, 3 Nov 2026) | Joint AMD–Meta release: Helios "installed and being tested" (27 Oct 2026) [BUY] | Consistent with testing, not production |
| Q3 was the first quarter AMD "shipped MI455 and Helios racks for revenue" (Q3 call summary) | 10-Q: "we do not manufacture or sell the completed Helios rack-scale solutions" | Wording tension; revenue is from components |
| "Up to 40% more tokens-per-dollar" than B200, using *expected* MI355X cloud pricing (12 Jun 2025) | SemiAnalysis: not competitive with full optimizations (Feb 2026); B200 ahead on perf/$ after 21 Aug 2026 | Contradicted as a general claim; holds for some stacks |
| MI355X beat "the selected NVIDIA B300 submission" by 18% offline in MLPerf v6.1 ([AMD blog, Sep 2026, UNOPENED](https://www.amd.com/en/blogs/2026/amd-delivers-its-broadest-mlperf-inference-6-1-submission.html)) | Third-party per-GPU recomputation: highest-throughput 8-GPU GB300 result at 16,022 tok/s per GPU vs MI355X 14,155 on gpt-oss-120b Server ([GPU Insights, UNOPENED](https://gpuinsights.net/mlperf-inference-v6-1-per-gpu-results-2026/)) | Holds against a *selected* comparator; not against the highest-throughput NVIDIA row |
| ROCm.ai 3.3x inference / 2.4x training gains; releases every 6 weeks (2026) | SemiAnalysis: "more than six months behind"; ATOM "unusable for real workloads" (Feb 2026); labs "do not want to run" ATOM in production (Aug 2026) | Progress independently observed; parity contradicted as of Aug 2026 |
| Helios +15% FP4 vs Vera Rubin (Jul 2026) | NVIDIA page: 2.52 EF dense, 3.6 EF sparse | Holds dense-to-dense only |
| MI455X 19.6 TB/s (brochure) | 1.7 PB/s per rack (AMD at AAI 2026) implies ~23.6 TB/s; some coverage cites 1.4 PB/s | Unresolved; possibly a specification update |
| "Roughly 14 gigawatts" booked (iTWire headline, 24 Jul 2026) | AMD 8-Ks: 2 GW binding | Headline sums ceilings |
| MI500 "up to a 1,000x increase in AI performance" vs MI300X (Jan 2026) | ">2,000x higher inference throughput in just 4 years" (Jul 2026) | Metric changed and the number doubled within six months; both projections |
| Meta deal value (undisclosed by AMD) | "Tens of billions" (Bajarin via [CNBC, 24 Feb 2026](https://www.cnbc.com/2026/02/24/meta-to-use-6gw-of-amd-gpus-days-after-expanded-nvidia-ai-chip-deal.html)); "$60B" (JPR); ">$100B" (Introl) [EST] | Estimates conflict; no primary value |

Buyers' own documents support AMD's customer claims in direction: Anthropic's filing confirms an MI450 agreement worth more than $20B if the initial capacity is fully procured [BUY]. Meta's binding 1 GW sits in AMD's 8-K. OpenAI's Sachin Katti said on AMD's stage that OpenAI is "really thrilled with how that bet is turning out" [CS+BUY via press] ([iTWire](https://itwire.com/business-it-news/data/astounding-massive-dominant-ai-innovation-amd-launches-helios-against-nvidia-tips-up-to-us-5-billion-into-anthropic-and-books-roughly-14-gigawatts-of-customer-ai-compute-at-advanci)).

Meta's framing is diversification: it committed to "millions" of NVIDIA processors a week before the AMD deal, and Mark Zuckerberg described the AMD deal as a step "as we diversify our compute" ([CNBC, 24 Feb 2026](https://www.cnbc.com/2026/02/24/meta-to-use-6gw-of-amd-gpus-days-after-expanded-nvidia-ai-chip-deal.html)).

No supplier statement about AMD volumes was found, and no HBM4 qualification information for the MI450 appears in any supplier source reviewed.

## Broadcom (custom-chip division): six XPU customers, $179B of obligations, and up to $72B of backstops

Broadcom does not report its custom-accelerator ("XPU") business as a separate segment. Its disclosures are the AI semiconductor revenue line, management percentages, and contract filings. Broadcom's fiscal 2026 ended on 1 November 2026, and **Q4 FY2026 results had not been released as of 14 November 2026**. The latest 8-K on EDGAR was dated 27 October 2026, and the prior-year Q4 was reported on 11 December 2025 ([SEC EDGAR filing index, CIK 1730168, accessed 14 Nov 2026](https://data.sec.gov/submissions/CIK0001730168.json)).

### Facts: XPUs were 73% of a $16.7B AI quarter, and the order book now runs to 2031

**What the division makes, and for whom.** Broadcom's 10-K describes custom silicon platforms that integrate "embedded logic, high-bandwidth memory, serializer/deserializer technology, IP cores and processor cores using advanced packaging technologies". The products are custom accelerators "for hyperscalers, companies with AI frontier models and system integrators", plus "switches, subsystems and, in some cases, racks" [CS] ([Broadcom 10-K FY2025, filed 18 Dec 2025](https://www.sec.gov/Archives/edgar/data/1730168/000173016825000121/avgo-20251102.htm)).

On 2 September 2026 Hock Tan said Broadcom has **six XPU customers**. Four are named: Google, Meta, Anthropic and OpenAI. Tan said four of the six fund themselves, while Anthropic and OpenAI receive financing support [CS] ([Broadcom Q3 FY2026 call transcript, Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/); [Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-broadcom-tops-q3-2026-estimates-as-ai-sales-surge-93CH-4886849)). In the quarter to 2 August 2026, XPU shipments rose more than 3.5x year on year and were **73% of AI revenue**, which works out to roughly $12.2B of $16.7B (calc).

*Google TPU.* An 8-K of 6 April 2026 records two agreements [CS] ([Broadcom 8-K, 6 Apr 2026](https://www.sec.gov/Archives/edgar/data/1730168/000119312526144028/d87999d8k.htm)): a "Long Term Agreement for Broadcom to develop and supply custom Tensor Processing Units … for Google's future generations of TPUs"; and a "Supply Assurance Agreement" for networking and other rack components "through up to 2031".

The sentence structure leaves it unclear whether the 2031 date also governs the TPU agreement. On 2 September 2026 Tan said Ironwood (TPU v7) had "shipped in high volume" and that production shipments of TPU v8i had begun. He said "Broadcom is now shipping the TPU version 8i ahead of the MediaTek version v8t", and that Broadcom plans "to deliver multi-tens of billions of dollars of TPUs annually over the next several years" [CS] ([Q3 FY2026 call](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/)).

*Anthropic.* Anthropic buys TPU racks through Broadcom. On 11 December 2025 Broadcom disclosed "a $10 billion order to sell the latest TPU Ironwood racks to Anthropic" and "an additional $11 billion order from this same customer for delivery in late 2026" [CS] ([Q4 FY2025 call, 11 Dec 2025](https://www.fool.com/earnings/call-transcripts/2025/12/12/broadcom-avgo-q4-2025-earnings-call-transcript/)). The 6 April 2026 8-K adds that "Anthropic, beginning in 2027, will access through Broadcom approximately 3.5 gigawatts", and that consumption "is dependent on Anthropic's continued commercial success" [CS] ([8-K](https://www.sec.gov/Archives/edgar/data/1730168/000119312526144028/d87999d8k.htm)).

By 2 September 2026 Broadcom's figures were: 1 GW of Ironwood deploying in 2026; "5 GW of TPU v8i in 2027"; and "an incremental 10 gigawatts" in 2028.

Tan said Anthropic "is on track to become our largest XPU customer in 2027" [CS] ([Q3 FY2026 call](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/)).

*Meta.* Broadcom said on 4 March 2026 that "Meta's custom accelerator MTIA roadmap is alive and well. We are shipping now" [CS] ([Q1 FY2026 call](https://www.fool.com/earnings/call-transcripts/2026/03/04/broadcom-avgo-q1-2026-earnings-call-transcript)). Meta announced on 14 April 2026 "a commitment that exceeds 1GW, which is the first phase of a sustained, multi-gigawatt rollout", with four new MTIA generations within two years [BUY] ([Meta Newsroom, 14 Apr 2026](https://about.fb.com/news/2026/04/meta-partners-with-broadcom-to-co-develop-custom-ai-silicon/)). CNBC reported that the partnership runs through 2029, and that Broadcom calls these "the first AI silicon built on a 2-nanometer process" ([CNBC, 14 Apr 2026](https://www.cnbc.com/2026/04/14/meta-commits-to-one-gigawatt-of-custom-chips-with-broadcom-as-hock-tan-agrees-to-leave-board.html)). Broadcom expects production shipments of a new MTIA generation in Q4 FY2026 and the first 1 GW order to deliver from H2 2027 [CS].

*OpenAI.* The 13 October 2025 announcement covered 10 GW of OpenAI-designed accelerators by 2029, with no financial terms [CS/BUY via press] ([Maginative, 13 Oct 2025](https://www.maginative.com/openai-and-broadcom-to-co-design-custom-ai-chips-deploy-10-gw-by-2029)). The first chip, "Jalapeño", was unveiled on 24 June 2026 [CS/BUY via press] ([CNBC, 24 Jun 2026](https://www.cnbc.com/2026/06/24/openai-and-broadcom-reveal-jalapeno-first-ai-chip-in-partnership.html)). Broadcom later said "Jalapeno is on track for the planned deployment of 1.3 gigawatts in 2027", with "line of sight" to more than 5 GW in 2028 [CS] ([Q3 FY2026 call](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/)).

*Other customers.* A fifth, unnamed customer placed "a $1 billion order … for delivery in late 2026" [CS] ([Q4 FY2025 call](https://www.fool.com/earnings/call-transcripts/2025/12/12/broadcom-avgo-q4-2025-earnings-call-transcript/)). The "other two" customers hold purchase orders totalling **$6 billion**, with shipments from late 2026 [CS] ([Q2 FY2026 call, 3 Jun 2026](https://www.fool.com/earnings/call-transcripts/2026/06/03/broadcom-avgo-q2-2026-earnings-transcript/)).

Apple signed long-term agreements through 2031 for custom ASICs "for use in multiple generations of Apple products". The 8-K does not mention AI or servers [CS] ([Broadcom 8-K, 6 Jul 2026](https://www.sec.gov/Archives/edgar/data/1730168/000119312526295589/d84378d8k.htm)). Microsoft's reported talks with Broadcom rest on The Information's unnamed sources [PRESS-U] ([Yahoo Finance/Investing.com, 8 Dec 2025](https://finance.yahoo.com/news/marvell-stock-falls-microsoft-broadcom-130457554.html)).

*Networking.* Broadcom said it has shipped Tomahawk 6 (102.4 Tb/s) "for over one year" (3 June 2026). Tomahawk 7 (200 Tb/s) "just taped out" (2 September 2026), and Tomahawk Ultra scale-up Ethernet is deploying from late FY2026 [CS] ([Q2](https://www.fool.com/earnings/call-transcripts/2026/06/03/broadcom-avgo-q2-2026-earnings-transcript/); [Q3](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/)).

**Milestones and the record against them.** Broadcom's quarterly AI-revenue guidance was met or beaten in each of the four quarters checked [CS] ([8-K exhibits](https://www.sec.gov/Archives/edgar/data/0001730168/000173016826000076/avgo-08022026x8kxex99.htm)):

| Quarter | Guided AI revenue | Actual AI revenue |
|---|---|---|
| Q4 FY2025 | $6.2B | $6.5B |
| Q1 FY2026 | $8.2B | $8.4B |
| Q2 FY2026 | $10.7B | $10.8B |
| Q3 FY2026 | $16.0B | $16.7B |

Longer-dated commitments are all pending: **FY2026:** AI revenue guidance rose from "$56 billion" (June 2026) to "$58 billion" (September). Q1–Q3 actuals plus the Q4 guide sum to $57.6B (calc). **FY2027:** the outlook moved from "in excess of $100 billion" in chips (March 2026) to "approximately $115 billion", for which Broadcom says it has "secured the supply". **FY2028:** Broadcom claims "line of sight" to "$230 billion". **Older market sizing:** in December 2024 Broadcom put the FY2027 serviceable market at "$60 billion to $90 billion" for three hyperscalers, adding that "this is not revenue". [CS] ([Q4 FY2024 call, 12 Dec 2024](https://www.fool.com/earnings/call-transcripts/2024/12/12/broadcom-avgo-q4-2024-earnings-call-transcript/); [Q3 FY2026 call](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/))

Tomahawk 7's tape-out "this quarter" (said 3 June) was met by 2 September. Several delivery dates are pending: the late-2026 deliveries for Anthropic's $11B order, customer five and the other two customers; Meta's Q4 FY2026 production shipments; and OpenAI's volume deployment, now dated 2027.

OpenAI's start slid in framing. The October 2025 announcement spoke of deployments starting in late 2026. In December 2025 Broadcom described "an agreement to be aligned on developing 10 gigawatts for OpenAI over 27 to 29 time frame". In June 2026 Tan spoke of a "small prototype" in late 2026 and "full tilt in first half '28". No third-party report of a Jalapeño delay was found.

**Revenue, margins, cash and debt.** All figures are company-reported.

| US$ millions | FY2025 (to 2 Nov 2025) | Q1 FY26 (to 1 Feb 2026) | Q2 FY26 (to 3 May 2026) | Q3 FY26 (to 2 Aug 2026) | Q4 FY26 guide (to 1 Nov 2026) |
|---|---|---|---|---|---|
| Revenue | 63,887 | 19,311 | 22,187 | **29,591** | ~34,800 |
| AI semiconductor revenue | ~20,200 (+65%) | 8,400 | 10,800 | **16,700** (+221%) | ~21,700 |
| Non-GAAP gross margin | ~78.6% | 77.0% | 77.1% | 75.0% | ~73% |
| Semiconductor segment operating margin | 57.6% | 60% | 62% | 61.3% | – |
| GAAP net income | 23,126 | 7,349 | 9,310 | 13,088 | – |
| Free cash flow | 26,914 | 8,010 | 10,262 | 13,665 | – |
| Cash / debt at period end | 16,178 / ~65,136 | 14,174 / 66,057 | 19,628 / 64,907 | 23,975 / 59,419 | – |

Sources: [8-K Ex. 99.1, 11 Dec 2025](https://www.sec.gov/Archives/edgar/data/1730168/000173016825000116/avgo-11022025x8kxex99.htm); [8-K, 4 Mar 2026](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000011/avgo-02012026x8kxex99.htm); [8-K, 3 Jun 2026](https://www.sec.gov/Archives/edgar/data/0001730168/000173016826000051/avgo-05032026x8kxex99.htm); [8-K, 2 Sep 2026](https://www.sec.gov/Archives/edgar/data/0001730168/000173016826000076/avgo-08022026x8kxex99.htm); [10-Q Q3 FY2026, filed 10 Sep 2026](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm); [DEF 14A, 2 Mar 2026](https://www.sec.gov/Archives/edgar/data/1730168/000119312526085691/d49254ddef14a.htm).

Broadcom attributes the Q4 gross-margin guide of about 73%, "down from 78% a year ago", to "the increasing mix of XPUs with their increasing memory content". Tan told investors to "stop focusing on gross margin". The 10-Q's risk factors say XPU and rack sales "will likely increase our operating margin but compress or lower future gross margin" [CS] ([10-Q](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm)).

**Remaining performance obligations** (RPO, firm amounts only) grew as follows [CS] ([10-Q Q2 FY2026](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000054/avgo-20260503.htm); [10-Q Q3 FY2026](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm)):

| Date | RPO | Share due within 12 months |
|---|---|---|
| 1 Feb 2026 | $45.0B | – |
| 3 May 2026 | $164.6B | – |
| 2 Aug 2026 | **$179.2B** | about 25% |

The jump to May includes "a long-term contract for custom AI accelerators" signed that quarter, the quarter in which the Google agreement was filed. The December 2025 "AI backlog >$73 billion" was a management order-backlog figure, not RPO. Tan said at the time, "do not take that $73 billion as … the revenue we ship".

Unconditional purchase commitments rose from $54M (1 February 2026) to **$126.8B** (2 August 2026), almost all falling due in FY2027–28.

Concentration rose through FY2026 [CS] ([10-K](https://www.sec.gov/Archives/edgar/data/1730168/000173016825000121/avgo-20251102.htm); [10-Q](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm)): **One distributor:** 32% of FY2025 revenue, rising to **50% of Q3 FY2026 revenue**. **Top five end customers:** about 40% of FY2025 revenue, rising to about 55% in Q3 FY2026. **China (including Hong Kong) shipments:** 17% of FY2025 revenue.

**Financing for customers.** In June 2026 Broadcom launched an "AI XPV platform". Its "initial tranche of $35 billion [was] led by a financial partner to facilitate the deployment of more than 1 gigawatt of compute infrastructure for our customer". The financial partner takes on agreements to buy Broadcom-XPU racks and the related five-year leases with that customer [CS] ([10-Q Q2 FY2026, subsequent event dated 8 Jun 2026](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000054/avgo-20260503.htm)).

Broadcom's backstop covers the difference between 85% of outstanding lease amounts and the racks' resale value, with a "maximum potential liability … approximately $29 billion". The filings also say that "our customer may … issue to us convertible promissory notes up to an aggregate principal amount of $42 billion"; none had been issued by 2 August 2026 [CS] ([10-Q Q3 FY2026](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm)). Apollo's release of 9 June 2026 names **Anthropic** as the beneficiary of the first $35B tranche [counterparty] ([Apollo, 9 Jun 2026](https://ir.apollo.com/news-events/press-releases/detail/629/apollo-leads-35-billion-capital-solution-for-broadcom-ai)).

On 26 October 2026 Broadcom entered a second arrangement, reported in an Item 2.03 8-K **filed 27 October 2026**. It provides "residual value support to a newly formed special purpose vehicle", covering the gap between 72.5% of outstanding lease amounts and rack value, with a "maximum potential liability … approximately **$43 billion**". That filing does not name the customer [CS] ([Broadcom 8-K, filed 27 Oct 2026](https://www.sec.gov/Archives/edgar/data/1730168/000119312526434271/d148323d8k.htm)). Anthropic's S-1/A of 10 November 2026 states that Broadcom "assigned portions" of Anthropic's rack leases "to a newly formed special-purpose financing entity in Oct 2026" [BUY] ([Anthropic S-1/A No. 2](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm)). The October date and SPV description match Broadcom's second backstop. The full reconciliation with Anthropic's $161.2B lease rents and a reported $63B vehicle is in the cross-company section.

Broadcom's 10-Q also describes a platform target of "more than 20 gigawatts in compute capacity … for the leading frontier AI labs through 2028". It says Broadcom "may provide residual value guarantees" [CS] ([10-Q Q3 FY2026](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm)).

**Capacity.** Broadcom says "approximately 95% of the wafers manufactured by our CMs were produced by … TSMC", and that its wafer needs "represent a meaningful portion of TSMC's total production capacity" [CS] ([10-Q](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm)). It names its constraints itself. On 4 March 2026 it cited "constrained capacity in leading-edge wafers, in high bandwidth memory, and substrates". It said it had "fully secured capacity of these components for 2026 through 2028". On 2 September 2026 Tan said "demand for lasers, whether it's EML lasers, CW lasers, is far surpassing supply", and that land, power and shell "dictates specific timing" of deployment. [CS] ([Q1 FY2026 call](https://www.fool.com/earnings/call-transcripts/2026/03/04/broadcom-avgo-q1-2026-earnings-call-transcript); [Q3 FY2026 call](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/))

Morgan Stanley estimated Broadcom's 2026 CoWoS demand at **about 150k wafers (about 15%)**: Google TPU about 90k, Meta about 50k and OpenAI about 10k [EST: Morgan Stanley] ([36Kr, 4 Dec 2025](https://eu.36kr.com/en/p/3580962946874242)). Celestica supplies boards and racks for OpenAI's Jalapeño platform ([ServeTheHome, 24 Jun 2026](https://www.servethehome.com/openai-jalapeno-intelligence-platform-shown-powered-by-broadcom/)). The integrator for Anthropic's Ironwood racks was not identified.

**Ownership and key people.** Hock Tan has been CEO since March 2006. A performance award granted on 3 September 2025 ties him to Broadcom through FY2030. It pays 0% at or below $60B of AI revenue in any four consecutive quarters of FY2028–2030, and 300% at or above $120B [CS] ([8-K, 9 Sep 2025](https://www.sec.gov/Archives/edgar/data/1730168/000119312525199281/d58273d8k.htm)). Management's own FY2027 and FY2028 outlooks exceed the award's maximum. Tan left Meta's board in April 2026.

Charlie Kawwas is President of the Semiconductor Solutions Group. CFO Kirsten Spears retired on 12 June 2026 and was succeeded by **Amie Thuener**, previously Alphabet's chief accounting officer [PRESS] ([The Star, 3 Apr 2026](https://www.thestar.com.my/tech/tech-news/2026/04/03/broadcom-taps-alphabet-executive-amie-thuener-as-next-cfo)). Henry Samueli is Chairman with 1.8% of shares. Vanguard (9.9%) and BlackRock (7.3%) are the largest disclosed holders, but both figures rest on 2024 13G filings [CS] ([DEF 14A, 2 Mar 2026](https://www.sec.gov/Archives/edgar/data/1730168/000119312526085691/d49254ddef14a.htm)). The head of the ASIC division could not be verified.

**Legal and regulatory.** Broadcom's filings describe: FTC oversight; "regulatory investigations or inquiries from regulatory authorities in Korea, Japan and the European Union into certain of our contracting and business practices"; and no material loss accruals. [CS] ([10-Q Q3 FY2026](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm))

The Q1 FY2026 10-Q, filed 11 March 2026, added two new risk factors: customers or suppliers "designated a 'supply chain risk'", in which case Broadcom "may be required to suspend … selling to such customers"; and "customer-owned tooling".

Neither appears in the FY2025 10-K. Whether the supply-chain-risk language relates to any US government designation of an AI customer could not be verified. Some contracts with "some of our largest customers" carry indemnification and liquidated damages that "are potentially unlimited" [CS] ([10-Q Q1 FY2026](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000016/avgo-20260201.htm)). VMware-related complaints, China SAMR conditions and ByteDance export issues could not be verified.

### Science: the XPU model is proven by customers' own chips, not by independent benchmarks of Broadcom's work

**What is demonstrated.** The strongest technical evidence for custom accelerators comes from Broadcom's customers. It is company-authored, sometimes peer-reviewed, never independent, and never names Broadcom.

**Google TPU v4 (ISCA 2023).** Google described a 4,096-chip TPU v4 supercomputer at ISCA 2023. Optical circuit switches were under 5% of system cost, and the system measured **1.2–1.7x faster than NVIDIA A100 while using 1.3–1.9x less power** [company-authored, peer-reviewed] ([Jouppi et al., arXiv 2304.01433, Apr 2023](https://arxiv.org/abs/2304.01433)). **Ironwood (TPU v7).** Google specifies 4,614 TFLOPs, 192 GB of HBM and 7.37 TB/s per chip. A 9,216-chip pod delivers 42.5 EF at "nearly 10 MW" [CS: Google] ([Google blog, 9 Apr 2025](https://blog.google/products/google-cloud/ironwood-tpu-age-of-inference/)). **Meta MTIA v2.** Meta's chip (TSMC 5 nm, 90 W) served production models in 16 regions within nine months of first silicon [BUY: Meta] ([Meta AI blog, 10 Apr 2024](https://ai.meta.com/blog/next-generation-meta-training-inference-accelerator-AI-MTIA/)).

Third-party observation of Broadcom-built silicon is limited to architecture analysis.

**TechInsights on Jalapeño.** Working from OpenAI's Hot Chips disclosures and patents, TechInsights reports TSMC 3 nm and a weight-stationary systolic array "in the same broad family as Google's TPU". It says the benchmarks are **not independently verified** and that software maturity is a weak point. It did no teardown [IND: TechInsights] ([TechInsights, 3 Sep 2026](https://www.techinsights.com/blog/openai-jalapeno-inference-chip-architecture)). **ServeTheHome.** It counted what it hedged as six HBM sites from photographs and ran no tests ([ServeTheHome, 24 Jun 2026](https://www.servethehome.com/openai-jalapeno-intelligence-platform-shown-powered-by-broadcom/)).

**What is unproven.** As of 14 November 2026 no independent evidence exists for any of the following.

**Jalapeño in production.** Only lab operation is claimed, and no MLPerf, InferenceX or Artificial Analysis data cover it. **Customer five and the other two customers.** No public specifications exist for their chips. **Broadcom's own engineering claims.** These cover 200G SerDes, Tomahawk 6 and 7, co-packaged-optics reliability, and the 3.5D XDSiP package (6,000 mm², up to 12 HBM stacks per [The Register, 5 Sep 2025](https://www.theregister.com/2025/09/05/openai_broadcom_ai_chips/)). None has independent verification. **XPU versus GPU total cost of ownership.** No independent study was found. Google's "80% better performance per dollar" for TPU 8i is measured against its own Ironwood, not against GPUs. **The rack-lease-and-backstop model.** It has no default or residual-value history. Broadcom describes the backstops' fair value as "not material".

Broadcom is absent from every 2026 MLPerf submitter list. Google's own TPU submissions are discussed in the Google section.

**Physical and engineering limits.** **Supply.** Broadcom names leading-edge wafers, HBM, substrates and lasers. Industry evidence corroborates the laser constraint: Lumentum reports photonics demand about 30% above supply [SUP, UNOPENED] ([TrendForce/LEDinside, 6 Aug 2026](https://trendforce.com/news/2026/08/06/news-inp-shortage-emerges-as-ai-optical-interconnect-bottleneck/)). **Reticle limits.** These push multi-die packages up to 6,000 mm². Jalapeño is described as "a massive reticle-sized ASIC" ([Tom's Hardware, Jun 2026](https://www.tomshardware.com/tech-industry/artificial-intelligence/broadcom-and-openai-unveil-custom-built-jalapeno-inference-processor-openais-first-chip-is-a-massive-reticle-sized-asic-built-in-an-ultra-fast-nine-month-development-cycle)). **Power.** A single Ironwood pod draws close to 10 MW. **Memory pass-through.** HBM bought into XPU racks visibly compresses gross margin. **Customer architecture control.** Google co-designs TPUs with DeepMind, OpenAI designs Jalapeño, and Meta "co-develops", so the customer can move work elsewhere. MediaTek began shipping AI accelerators in September 2026. It expects about $2.5B of related revenue in Q4 2026 and targets "around 20% of the total AI accelerator ASIC market" [competitor statement via press] ([BigGo, 30 Oct 2026](https://finance.biggo.com/news/TW_2454.TW_2026-10-30)).

**Whether it stands on solid ground.** The engineering evidence that the custom-XPU model works is strongest for Google's TPU line. It rests on published Google papers, multi-generation production use and a 2026 long-term agreement. For Meta MTIA it is moderate, resting on production use in 16 regions. For OpenAI and the three unnamed customers it is weakest: no independent performance or production data exist.

Broadcom's own networking and packaging claims are plausible extensions of shipping products, but none has been independently measured. The financed-rack model adds a non-technical dependency, residual-value exposure of up to about **$72B** across two backstops (calc). It has no operating history.

### Cross-examination: most tensions are Broadcom's own framing changes

| Broadcom statement (date) | Outside or later source (date) | Finding |
|---|---|---|
| "Broadcom is now shipping the TPU version 8i ahead of the MediaTek version v8t"; Anthropic gets "5 GW of TPU v8i in 2027" (2 Sep 2026, two transcripts) | Press: Broadcom builds 8t "Sunfish", MediaTek 8i "Zebrafish" (unnamed supply-chain sources, [Wccftech, 20 Apr 2026](https://wccftech.com/google-splits-tpuv8-strategy-two-chips-broadcom-training-mediatek-inference-duties/)); SemiAnalysis post calls Broadcom's part "v8AX" [UNOPENED]; Google names no partner ([Google, 22 Apr 2026](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/)); MediaTek names no customer | **Unresolved.** The CEO's on-record statement, confirmed by two independent transcripts, is the only attributable source. The press mapping relies on unnamed sources. Neither Google nor MediaTek confirms either version. |
| First "$10B" rack customer was Anthropic (11 Dec 2025) | FT (Sep 2025, unnamed sources): OpenAI ([The Register, 5 Sep 2025](https://www.theregister.com/2025/09/05/openai_broadcom_ai_chips/)) | Company's later on-record statement supersedes |
| Anthropic 2027 capacity: ">3 GW" (4 Mar 2026), "approximately 3.5 gigawatts" (8-K, 6 Apr 2026), "another 5 gigawatts" (3 Jun 2026), "5 GW of TPU v8i" (2 Sep 2026) | Anthropic: "multiple gigawatts … starting in 2027", no number ([Anthropic, 6 Apr 2026](https://www.anthropic.com/news/google-broadcom-partnership-compute)) [BUY] | Figure rose 43% across Broadcom's own statements; buyer gives no number |
| "It was not backstopped in that sense" (Tan, 3 Jun 2026); future guarantees would be "modest" (CFO, 2 Sep 2026) | Backstop of up to ~$29B entered 8 Jun 2026 (10-Q); second backstop up to ~$43B (8-K, filed 27 Oct 2026) | Contradicted within five days, then exceeded |
| "All a chip business only" (Tan, 3 Jun 2026) | Broadcom sells "TPU Ironwood racks" (Dec 2025) and its 10-Q describes rack purchase-and-lease structures | Contradicted by the company's own filings |
| Gross-margin impact of racks "not going to be substantial at all" (CFO, 4 Mar 2026) | Q4 guide ~73% vs 78% a year earlier (2 Sep 2026); Morgan Stanley and BofA flagged dilution in Dec 2025 [EST] ([Sherwood News, 11 Dec 2025](https://sherwood.news/markets/broadcom-q4-2025-earnings-report-guidance-asics-ai-boom-bubble/)) | About 5 points of dilution materialized |
| Customer-owned tooling an "overblown hypothesis" (11 Dec 2025); no competition "for many years" (4 Mar 2026) | Added as a risk factor in the 10-Q of 11 Mar 2026; MediaTek shipping AI accelerators from Sep 2026 | Calls and filings diverge |
| OpenAI deployments starting late 2026 (Oct 2025) | "Over 27 to 29" (Dec 2025); "small prototype" late 2026, volume 2027 (Jun 2026) | Volume moved to 2027; no third-party delay report found |
| Meta MTIA "we are shipping now" (4 Mar 2026) | "Production shipments" expected Q4 FY2026 and first 1 GW from H2 2027 (Jun and Sep 2026) | Different generations or stages; not a direct contradiction |
| AI backlog ">$73 billion" (Dec 2025) | RPO of $33.3B at 2 Nov 2025 (10-K) | Different measures (order backlog vs firm RPO) |
| TPU 8 GA "later this year" (Google, 22 Apr 2026); Broadcom v8i shipping (Sep 2026) | Social-media and press items: both v8 chips on TSMC 2 nm in late 2027 [UNOPENED] | Company and customer statements describe 2026 shipments |

Buyers' own filings confirm Broadcom's largest customer claim and exceed it in dollars: **Anthropic.** The S-1/A records five-year master equipment leases with rent of **about $161.2B** excluding interest. It also records a "Broadcom Infrastructure Partner 2026 NPA" for up to **$42.0B** of convertible notes to finance that rent, matching the $42B facility in Broadcom's 10-Q [BUY] ([Anthropic S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm)). **Meta.** Its own announcement confirms a commitment exceeding 1 GW. **Google.** Its posts confirm TPU 8 but name no silicon partner.

No supplier statement about Broadcom was found; TSMC does not name customers. Broadcom also bought **$1.0B** of Anthropic stock in Anthropic's IPO private placement [BUY]. As with NVIDIA and AMD, the supplier is also a financier and shareholder of its largest prospective XPU customer.

## Google's TPU unit (Alphabet): a decade of in-house use, now sold as hardware, and absent from MLPerf since 2025

Alphabet does not report TPU revenue. The business has to be read through four sources: Google Cloud's segment results; capital spending, inventory and contingent obligations; disclosures by counterparties: Anthropic, Broadcom, Blackstone and Oracle; and product posts and release notes.

### Facts: Ironwood reached GA four months after "coming weeks"; TPU systems became product revenue

**Products and their stage.** Google has run TPUs in its own data centers since 2015 [company-authored, peer-reviewed] ([Jouppi et al., ISCA 2017, arXiv 1704.04760](https://arxiv.org/abs/1704.04760)). The current generations are as follows.

| Generation | Status at 14 Nov 2026 | Key facts | Source |
|---|---|---|---|
| Trillium (v6e) | GA since 16 Dec 2024 | – | [CS] [Google Cloud TPU release notes](https://docs.cloud.google.com/tpu/docs/release-notes) |
| Ironwood (TPU7x) | Preview 24 Nov 2025; GA 31 Mar 2026 | Announced 9 Apr 2025. 4,614 TFLOPs (FP8), 192 GB HBM at 7.37 TB/s, 1.2 TBps interchip interconnect; 9,216-chip pods of 42.5 EF drawing "nearly 10 MW"; 2x Trillium's performance per watt | [CS] [Google blog, 9 Apr 2025](https://blog.google/products/google-cloud/ironwood-tpu-age-of-inference/); [release notes](https://docs.cloud.google.com/tpu/docs/release-notes) |
| TPU 8t (training) | Announced 22 Apr 2026; GA promised "later this year"; no GA confirmation found | 9,600-chip superpods at 121 EF with 2 PB of HBM; designed "in partnership with Google DeepMind" | [CS] [Google blog, 22 Apr 2026](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/) |
| TPU 8i (inference) | As 8t | 288 GB HBM, 384 MB on-chip SRAM, 19.2 Tb/s interconnect, "80% better performance-per-dollar" than the previous generation | [CS] same source |
| TPU 8tx | Announced 9 Nov 2026; no GA date | 8t silicon with AMD EPYC hosts | [CS] [Google blog, 9 Nov 2026](https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/tpu-8i-max-and-8tx/) |
| TPU 8i Max | Announced 9 Nov 2026; no GA date | Two 8i chips on one package | [CS] same source |

On Ironwood's timing: Google said on 6 November 2025 that GA would come "in the coming weeks" [CS] ([Google Cloud blog, 6 Nov 2025](https://cloud.google.com/blog/products/compute/ironwood-tpus-and-new-axion-based-vms-for-your-ai-workloads)). Google's own release notes date GA to 31 March 2026, so a premise that Ironwood reached GA in November 2025 is not supported.

Per-chip TPU 8 figures were published only as images. As read by a third party, they are: **8t:** 12.6 PFLOPs at FP4 and 216 GB of HBM; **8i:** 10.1 PFLOPs at FP4; and **both:** built on TSMC N3. [PRESS] ([Crypto Briefing, 9 Nov 2026](https://cryptobriefing.com/google-tpu-8t-8i-training-inference-chips/))

When fetched, the release notes had no TPU 8 entries; the newest was dated 1 June 2026. Broadcom said on 2 September 2026 that it had "began production shipments of the next generation TPU v8i for Google" [SUP: Broadcom] ([Broadcom Q3 FY2026 call, Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-broadcom-tops-q3-2026-estimates-as-ai-sales-surge-93CH-4886849)). The 9 November post claims "nearly 100 customers" and four TPU systems shipped in a single year.

**TPUs outside Google Cloud.** On 29 April 2026 Sundar Pichai said Google would "begin to deliver TPUs to a select group of customers in their own data centers" [CS] ([The Register, 30 Apr 2026](https://www.theregister.com/off-prem/2026/04/30/google-to-sell-its-tpus-to-some-customers/5220078)). CFO Anat Ashkenazi said in July that Google had "began to recognize revenues from TPU system sales", and that "the vast majority of the revenues from these agreements will be realized in 2027" [CS] ([Alphabet Q2 2026 call, 22 Jul 2026](https://www.investing.com/news/transcripts/earnings-call-transcript-alphabet-beats-q2-2026-estimates-shares-fall-on-capex-surge-93CH-4807140)).

Alphabet's Q2 2026 release says Google Cloud "generates product revenues primarily from the sale of TPU systems" ([Alphabet Q2 2026 release](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000066/googexhibit991q22026.htm)). Its Q3 10-Q accounts for certain repurchase obligations on assigned TPU systems "as a financial guarantee" [CS] ([Alphabet 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000084/goog-20260930.htm)).

Two partner channels sit alongside direct sales: **Crux AI.** A joint venture announced on 18 May 2026 in which Blackstone committed $5B of initial equity, with the first 500 MW targeted for 2027 ([Business Wire/Blackstone, 18 May 2026](https://www.businesswire.com/news/home/20260518367552/en/Blackstone-Announces-Joint-Venture-with-Google-to-Create-New-TPU-Cloud), search-summary only). Alphabet describes it as "an unconsolidated equity method joint venture and a related party". Its commercial agreement accounts for **$16.8B** of Alphabet's backlog. **Oracle Cloud Infrastructure.** TPUs are to be offered on OCI from calendar 2027 [CS/BUY] ([Google Cloud Press Corner, 27 Oct 2026](https://www.googlecloudpresscorner.com/2026-10-27-Oracle-Brings-Google-TPUs-to-Oracle-Cloud-Infrastructure)).

**Milestones met, slipped and pending.**

| Commitment (date made) | Status at 14 Nov 2026 |
|---|---|
| Ironwood available "later this year" (9 Apr 2025) | **Partly met**: Preview 24 Nov 2025 |
| Ironwood GA "in the coming weeks" (6 Nov 2025) | **Slipped**: GA 31 Mar 2026 |
| Anthropic: "well over a gigawatt of capacity online in 2026" (23 Oct 2025) | **In progress**: Broadcom says "1 gigawatt of Ironwood we are deploying in 2026"; Mizuho said "nearly a gigawatt" in October 2026 [EST] ([CNBC, 28 Oct 2026](https://www.cnbc.com/2026/10/28/google-alters-cloud-playbook-turning-to-partners-to-sell-more-ai-chips.html)) |
| TPU 8t/8i "generally available later this year" (22 Apr 2026) | **Pending**: no GA note found |
| TPUs delivered into customer data centers (29 Apr 2026) | **Met**: revenue recognized from Q2 2026 |
| TorchTPU (preview April 2026) | **Advanced**: open-sourced October 2026, per Google |
| Crux AI 500 MW; OCI TPUs | **Pending** (2027) |
| Project Suncatcher: two prototype TPU satellites with Planet "by early 2027" | **Pending** ([Google Research, 4 Nov 2025](https://research.google/blog/exploring-a-space-based-scalable-ai-infrastructure-system-design/)) |

**Revenue, margins, cash and debt.** All figures are company-reported.

| US$ millions | Q3 2025 | Q4 2025 | Q1 2026 | Q2 2026 | Q3 2026 |
|---|---|---|---|---|---|
| Google Cloud revenue | 15,157 | 17,664 | 20,028 (+63% y/y) | 24,768 (+82%) | **30,709** (+103%) |
| Google Cloud operating income | 3,594 | 5,313 | ≈6,600 | 8,814 | **11,121** (36.2% margin) |
| Alphabet capex (purchases of property and equipment) | – | 27,851 | ≈35,700 | 44,924 | 51,355 |
| Inventory (mainly TPU systems for sale) | – | 2,439 | – | 9,991 | **13,308** |
| Long-term debt | – | 46,547 | 77,501 | 98,165 | **125,102** |

Sources: [Alphabet Q3 2026 release, 28 Oct 2026](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000080/googexhibit991q32026.htm); [Q4 2025 release, 4 Feb 2026](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000012/googexhibit991q42025.htm); [Q1 2026 10-Q](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000048/goog-20260331.htm); [Q2 2026 10-Q](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000071/goog-20260630.htm); [Q3 2026 10-Q](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000084/goog-20260930.htm).

Alphabet says "TPU systems sales were also a meaningful contributor to revenue growth" in Q3 2026, but gives no figure. Its 10-Q says the rise in Cloud operating income was partly offset by "inventory and related costs associated with the sale of TPU systems", a wording seen in a search summary of the filing [CS].

Cloud backlog was **$560.8B** at 30 September 2026, out of $567.7B for Alphabet in total; "just over 55%" of it is expected to be recognized within 24 months. Ashkenazi declined to say how much of the backlog is TPU sales agreements.

Alphabet's 2026 capex guidance rose three times, from $175–185B (4 February) to **$195–205B** (22 July), and was held on 28 October. Management expects capex to "increase significantly" in 2027 [CS].

Free cash flow was negative $5.9B in Q2 2026 and negative $9.1B in Q3. Alphabet funded the build-out with: **$85.2B of net debt proceeds** in the first nine months of 2026, including a 100-year sterling tranche; an **$80B equity programme** launched on 1 June 2026, which included a $10B Berkshire Hathaway placement [CS] ([Alphabet FWP, 1 Jun 2026](https://www.sec.gov/Archives/edgar/data/0001652044/000119312526251733/d160205dfwp.htm)); and **data-center payment backstops**, which it books as credit derivatives. Their notional value rose from $16.9B at end-2025 to **$48.0B at 30 September 2026** [CS] ([Alphabet 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm)).

Analyst estimates of TPU sales vary widely [EST, relayed by CNBC] ([CNBC, 28 Oct 2026](https://www.cnbc.com/2026/10/28/google-alters-cloud-playbook-turning-to-partners-to-sell-more-ai-chips.html)):

| Analyst | Estimate |
|---|---|
| TD Cowen | $9.4B in H2 2026 and $62.5B in 2027, at about 20% operating margin against about 35% for the Cloud segment |
| Wells Fargo | about $9B in Q3 2026 and $99B in 2027 |

**Customers and contracts.**

*Anthropic* is the largest documented TPU customer, and the main facts come from its own filings. Two notes files quote two different minimum commitments; the cause is explained in the cross-company section.

**Google hosting agreement, S-1/A No. 2.** This is Anthropic's second amended registration statement, filed 10 November 2026 and read directly from EDGAR. It describes a cloud hosting agreement signed in March 2026 and amended between May and October 2026. Under it Anthropic must spend **at least about $121.3B between April 2026 and July 2033**, with a true-up if spending falls short, and it is non-cancelable except on Google's uncured breach. A further **$125–150B** of TPU compute for 2028–2031 is Anthropic's estimate and is excluded from its commitments table [BUY] ([Anthropic S-1/A No. 2, 10 Nov 2026](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm)). **Google hosting agreement, original S-1.** The S-1 filed on 26 October 2026, as relayed by Equibles and CNBC, gave the minimum as **$114.5B** for the same April 2026 to July 2033 period [BUY as relayed] ([Equibles, 27 Oct 2026, updated 3 Nov 2026](https://equibles.com/research/anthropics-s-1-checked-against-amazon-google-microsoft-and-broadcom-filings); [CNBC live updates, 26 Oct 2026](https://www.cnbc.com/2026/10/26/anthropic-ipo-live-updates-ai-s-1-filing.html)). **TPU racks through Broadcom.** Anthropic also buys TPU racks through Broadcom: the $10B and $11B orders, and five-year equipment leases with **$161.2B** of rent [BUY]. These are covered in the Broadcom section. **Google's investment.** Google invested about $10.0B in Series G-2 in March 2026 and $10.0B in Series H in May 2026. It is buying **$10.0B** in the IPO private placement, which reduces its remaining $20.0B note facility to $10.0B [BUY] ([Anthropic S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm)). Alphabet's own 10-Qs call the investee "a private company".

*Meta* reportedly signed a multibillion-dollar TPU rental in February 2026 and is reportedly in talks to buy TPUs from 2027. Neither company confirmed either report [PRESS-U: The Information] ([WinBuzzer, 3 Mar 2026](https://winbuzzer.com/2026/03/03/meta-signs-multibillion-dollar-deal-rent-google-tpus-xcxwbn/)). The only on-record link is Thomas Kurian's statement on 28 October 2026 that Google "worked closely with Meta to deliver TorchTPU" [CS] ([Alphabet Q3 2026 call, Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-alphabet-q3-2026-profit-miss-sparks-10-afterhours-drop-93CH-4981037)).

*OpenAI* said in 2025 that it had "no specific plans to use TPUs at present". On 27 October 2026 The Information reported, citing one person familiar with the matter, that OpenAI is pursuing a TPU purchase, and CNBC says it confirmed the report [PRESS-U/PRESS] ([Seoul Economic Daily, 28 Oct 2026](https://en.sedaily.com/international/2026/10/28/openai-weighs-buying-google-tpus-easing-nvidia-reliance)).

*Apple* published that it trained its server foundation model on 8,192 TPUv4 chips [BUY] ([Apple, arXiv 2407.21075, Jul 2024](https://arxiv.org/html/2407.21075v1)).

*Neocloud channel.* Google backstops part of the obligations of data centers that host TPUs [PRESS] ([Sacra, Fluidstack profile](https://sacra.com/c/fluidstack)): TeraWulf (via Fluidstack): $3.2B, for about 14% pro forma equity; Cipher Mining: $1.73B; and Hut 8 (River Bend, Louisiana).

Executives at Nebius, Lambda and CoreWeave told The Information they had no near-term TPU plans [PRESS, search summary only].

**Capacity.** Broadcom is the confirmed supplier for Ironwood and TPU v8i. It signed a long-term agreement for future TPU generations, plus supply assurance for rack components "through up to 2031" [SUP] ([Broadcom 8-K, 6 Apr 2026](https://www.sec.gov/Archives/edgar/data/1730168/000119312526144028/d87999d8k.htm)). MediaTek is linked to "v8t" only through Broadcom's CEO; neither Google nor MediaTek has named it.

Morgan Stanley estimated Google TPU programmes at about 110k CoWoS wafers in 2026, about 90k via Broadcom and about 20k via MediaTek [EST] ([36Kr, 4 Dec 2025](https://eu.36kr.com/en/p/3580962946874242)). An estimate of 3.2M TPUs in 2026 and 5M in 2027 is attributed to Morgan Stanley in a page that was not opened [EST, UNOPENED] ([KuCoin News](https://www.kucoin.com/news/flash/morgan-stanley-defends-broadcom-s-role-in-google-s-tpu-supply-chain-forecasts-5m-shipments-by-2027)). Shipment figures of 4.3M and 10M on one aggregator are attributed to an article that contains no such numbers, and should be disregarded.

Google says it is "supply constrained" and is using third-party capacity "as a bridging strategy" [CS] ([Q2 2026 call](https://www.investing.com/news/transcripts/earnings-call-transcript-alphabet-beats-q2-2026-estimates-shares-fall-on-capex-surge-93CH-4807140)). Fluidstack, which builds Anthropic's TPU sites, is "on track for 1.3 gigawatts across more than 10 sites" in 2026 [PRESS] ([Forbes Australia, 3 Sep 2026](https://www.forbes.com.au/news/innovation/fluidstack-is-now-worth-18-billion/)). HBM suppliers for any TPU generation, Ironwood's process node and Google's CoWoS allocation are unverified.

**Key people.** Sundar Pichai and CFO Anat Ashkenazi own the capex and TPU-sales disclosures. Thomas Kurian, Google Cloud's CEO, made his first earnings-call remarks on 28 October 2026. Amin Vahdat, Chief Technologist and SVP for AI and Infrastructure, fronts the TPU announcements. Norman Jouppi is first author of the TPU v1 and v4 papers. Benjamin Treynor Sloss, a long-time Google infrastructure executive, left to become CEO of Crux AI (18 May 2026) [CS].

**Legal and regulatory.** A former Google engineer, Linwei Ding, was convicted by a jury on 29 January 2026 on 7 counts of economic espionage and 7 counts of theft of trade secrets. The stolen material included TPU chip specifications [PRESS] ([Decrypt, Jan 2026](https://decrypt.co/356455/former-google-engineer-convicted-of-stealing-ai-secrets-for-china)). A June 2026 press report says the judge set aside the seven espionage counts while the theft convictions stand, with sentencing pending. That report was seen only in a search summary [PRESS, UNOPENED] ([Courthouse News](https://www.courthousenews.com/judge-acquits-ex-google-engineer-of-economic-espionage-in-ai-secrets-case/)).

Anthropic's S-1 lists its reliance on Google, Amazon, Microsoft and Broadcom for compute as creating "dependencies and potential vulnerabilities". It names Google as a competitor [BUY as relayed] ([CNBC live updates, 26 Oct 2026](https://www.cnbc.com/2026/10/26/anthropic-ipo-live-updates-ai-s-1-filing.html)).

The following could not be verified: the Singular Computing patent settlement; antitrust remedies touching AI investments; export-control rules on TPU sales; and the legal-proceedings sections of Alphabet's 2026 10-Qs, which were truncated when fetched.

### Science: frontier-scale use is established; Ironwood and TPU 8 multiples are not independently measured

**What is demonstrated.** That TPUs train and serve frontier models at scale rests on several kinds of evidence, mostly from Google or its customers: **Architecture papers.** Google's peer-reviewed papers describe TPU v1 (2017) and TPU v4 (2023). The v4 paper reports 4,096-chip optically switched systems measured at **1.2–1.7x an A100 system while using 1.3–1.9x less power** [company-authored, peer-reviewed] ([arXiv 2304.01433](https://arxiv.org/abs/2304.01433)). **Customer-published efficiency.** Apple reports sustained model-FLOPs utilization of "approximately 52%" on an 8,192-chip TPUv4 job. This is the cleanest efficiency figure published by a party Google does not control [IND: Apple, customer] ([arXiv 2407.21075](https://arxiv.org/html/2407.21075v1)). **Gemini 3.** Google says it trained Gemini 3 on TPUs [CS] ([CNBC, 25 Nov 2025](https://www.cnbc.com/2025/11/25/nvidia-says-its-gpus-are-a-generation-ahead-of-googles-ai-chips.html)). **Anthropic.** Anthropic is running a multi-gigawatt deployment. **Reliability.** Google's NSDI '24 paper reports **99.98% system availability** on TPU v4, with hardware outages affecting about 1% of jobs [company-authored, peer-reviewed] ([USENIX NSDI '24](https://www.usenix.org/conference/nsdi24/presentation/zu)).

**MLPerf: where Google's 2026 submissions ran.** MLCommons lists Google as a submitter in all three 2026 rounds (Inference v6.0, Training v6.0 and Inference v6.1) [IND: MLCommons] ([MLCommons, 1 Apr 2026](https://mlcommons.org/2026/04/mlperf-inference-v6-0-results/); [16 Jun 2026](https://mlcommons.org/2026/06/mlperf-training-v6-0-results/); [16 Sep 2026](https://mlcommons.org/2026/09/mlperf-inference-v6-1-results/)). Google's own system directories in the MLCommons results repositories list **no TPU systems** in the first two of those rounds:

| Round | Systems in Google's directory | Source |
|---|---|---|
| Inference v5.1 (Sep 2025) | B200 and H200 only | [repo](https://github.com/mlcommons/inference_results_v5.1/tree/main/closed/Google/systems) |
| Inference v6.0 (Apr 2026) | B200 and GB200 NVL72 only | [repo](https://github.com/mlcommons/inference_results_v6.0/tree/main/closed/Google/systems) |
| Training v6.0 (Jun 2026) | GB200 NVL72 only | [repo](https://github.com/mlcommons/training_results_v6.0/tree/main/Google/systems) |

The MLCommons Training v6.0 results sheet likewise has no TPU entries ([results sheet](https://docs.google.com/spreadsheets/d/17Mek7pd_bKzfoA_ZiPt4E0jMcCZVE_dYbmsS8SUsJhw/edit)). An independent commentator noted that Google did not submit Ironwood to Inference v6.0 and gave no reason ([Tae Kim, 1 Apr 2026](https://taekim.substack.com/p/nvidia-wins-mlperf-ai-inference-benchmarks)).

**Google's 2026 v6.0 submissions were therefore made on NVIDIA GPU systems, not TPUs.** For Inference v6.1 (September 2026), coverage says only that Google "focus[ed] on DeepSeek-R1" without naming the hardware ([StorageReview, 16 Sep 2026](https://www.storagereview.com/news/mlperf-inference-v6-1-5-7x-per-accelerator-gains-a-512-gpu-run-and-vera-rubins-first-peer-reviewed-numbers)). That round's machine-readable data was not parsed in any notes file, so whether Google's v6.1 entry used TPUs is **unconfirmed**. Google's last visible TPU entries are Trillium in Inference v5.0 and Training v5.0, both in 2025.

**What remains unproven.** None of the following has been independently measured: **Ironwood multiples.** Google claims 2x performance per watt over Trillium, 10x the peak of v5p, and more than 4x per-chip performance over v6e. **TPU 8 multiples.** Google claims "up to 2.7x better training performance" for 8t, "80% better inference price-performance" for 8i, up to 2x performance per watt, and a target of more than 97% "goodput". **Cost of ownership.** The TCO advantage over NVIDIA rests on SemiAnalysis's model, which uses Google's internal cost view. That model has Ironwood's all-in TCO per chip about **44% below a GB200 server** from Google's side, and up to about 30% below GB200 for external customers [EST: SemiAnalysis] ([SemiAnalysis, 28 Nov 2025](https://newsletter.semianalysis.com/p/tpuv7-google-takes-a-swing-at-the)). **Server payback.** Kurian's claim that Google-silicon servers pay back in roughly half the time of AI servers generally (under two years) is company-stated [CS] ([CNBC, 28 Oct 2026](https://www.cnbc.com/2026/10/28/google-alters-cloud-playbook-turning-to-partners-to-sell-more-ai-chips.html)).

The only independent Ironwood throughput datum found comes from a page that was not opened. On InferenceX, TPU v7 at FP8 delivers 1.85x (external TCO) and 2.17x (internal TCO) the tokens per dollar of GB300 NVL72 at FP8. It does so on Qwen3.5-397B at 200 tokens/s per user, while GB300 NVL72 at FP4 (Dynamo TRT-LLM) delivers more tokens per dollar at every matched point [IND: SemiAnalysis, UNOPENED] ([InferenceX hardware](https://inferencex.semianalysis.com/hardware)).

Two of Google's comparisons mix bases. The "nearly 3x per pod" claim for 8t may compare FP4 (8t) with FP8 (Ironwood). The "more than 24x El Capitan" claim compares Ironwood's FP8 peak with El Capitan's FP64 HPL result of 1.742 EF ([TOP500, Nov 2024](https://top500.org/lists/top500/2024/11/)).

The independent benchmark record on older TPUs also conflicts. SemiAnalysis disputes Artificial Analysis's finding that TPU v6e has about 5x worse performance per dollar than NVIDIA GPUs, arguing that the test used an immature vLLM path and list prices.

Software portability is the main engineering caveat. SemiAnalysis judged in November 2025 that TPU software is not as easy to use as CUDA, and that the XLA:TPU compiler and runtime are not open source. Google responded with TorchTPU, which it open-sourced in October 2026 [CS].

**Physical and engineering limits.** The main limits recorded in the notes are: **Power and cooling.** An Ironwood pod draws close to 10 MW, about 1.1 kW per chip including overheads (calc), and requires liquid cooling. **Memory capacity.** Ironwood's 192 GB of HBM compares with GB300's 288 GB. TPU 8i moved to 288 GB [CS; EST: SemiAnalysis]. **Package size.** TPU 8i Max reaches beyond a single die by putting two chips on one package. **Fault exposure.** Larger slices raise the chance of maintenance events, and Google advises checkpointing about every hour ([Google Cloud docs](https://docs.cloud.google.com/tpu/docs/maintenance-events)). **Radiation.** In Google's space tests, Trillium's HBM showed irregularities after 2 krad(Si), with no hard failures up to 15 krad(Si) ([Google Research, 4 Nov 2025](https://research.google/blog/exploring-a-space-based-scalable-ai-infrastructure-system-design/)).

**Whether it stands on solid ground.** The feasibility of TPUs at frontier scale is on solid engineering ground. The evidence comes from multiple independent users, with Apple's published 52% utilization the strongest, and from optically switched pods of about 9,000 chips that have served several generations.

The newest claims are not on equally solid ground: Ironwood's and TPU 8's generation-over-generation multiples are untested by third parties. Google has kept Ironwood and TPU 8 out of the MLPerf rounds it entered in 2026, using NVIDIA systems there instead. The TCO case rests on one analyst model.

### Cross-examination: scale confirmed by buyers; timing, attribution and cost claims contested

| Google claim (date) | Outside source (date) | Finding |
|---|---|---|
| Ironwood GA "in the coming weeks" (6 Nov 2025) | Google's own release notes: GA 31 Mar 2026 | Slipped about four months |
| TPU 8t/8i GA "later this year" (22 Apr 2026) | No GA note by 14 Nov 2026; Broadcom shipping v8i from Sep 2026 [SUP] | Pending; shipments under way |
| TPU 8 design partners unnamed by Google | Broadcom: ships "TPU v8i ahead of the MediaTek v8t, which in fact was initiated earlier" (2 Sep 2026, two transcripts) [SUP]; press: Broadcom 8t, MediaTek 8i (unnamed or unsourced; [Wccftech, 20 Apr 2026](https://wccftech.com/google-splits-tpuv8-strategy-two-chips-broadcom-training-mediatek-inference-duties/)) | Only attributable source is Broadcom's CEO; unconfirmed by Google or MediaTek |
| TPU price-performance advantage (Google and Kurian, 2025–2026) | Anthropic's contracted compute reported as NVIDIA 4.7 GW vs TPU 4.5 GW ([Wccftech, 27 Oct 2026](https://wccftech.com/nvidia-gpus-make-up-4-7-gw-of-anthropics-contracted-compute-topping-4-5-gw-of-cheaper-google-tpus-as-lenders-bet-on-nvidias-residual-value/), citing posts quoting the S-1); WSJ: TPU rack financing stalled until Broadcom offered higher rates and guarantees, as lenders favor NVIDIA residual values [PRESS] | Buyer and lender behavior does not contradict the claim but shows TPUs are not treated as interchangeable with GPUs |
| Anthropic "well over a gigawatt" in 2026 (Anthropic, Oct 2025) | Broadcom "1 gigawatt" (Sep 2026); Mizuho "nearly a gigawatt" (Oct 2026) [EST] | Close to target; "well over" not confirmed |
| TPU hardware sales and payback (Kurian, Sep 2026) | TD Cowen: about 20% operating margin on TPU sales [EST]; 10-Q: TPU inventory costs offset operating-income growth | Margin-dilutive at segment level per estimate; no Alphabet split |
| Same TPUs, different labels | Alphabet books "hardware sales"; Broadcom books a sale of custom accelerators; Anthropic books finance leases ([Equibles](https://equibles.com/research/anthropics-s-1-checked-against-amazon-google-microsoft-and-broadcom-filings)) | Accounting framing differs across the three filings |
| Google investment in "a private company" (Alphabet 10-Qs) | Anthropic's S-1 names Google; Amazon's 10-Q lists Google's facility at $20.0B "original" while the S-1 says $30.0B (per Equibles) | Identity confirmed; facility size labeled differently |
| "NVIDIA is a generation ahead … greater performance, versatility, and fungibility than ASICs" (NVIDIA, 25 Nov 2025) | Google the same day: "accelerating demand for both our custom TPUs and Nvidia GPUs"; SemiAnalysis: Ironwood ~10% below GB200 on peak FLOPs and bandwidth but lower TCO [EST] | Opposing vendor claims; no independent test settles them |
| OpenAI "no specific plans to use TPUs at present" (2025) | Purchase report (The Information, 27 Oct 2026; CNBC says confirmed) and TPU job posting | Reported shift; no agreement announced |

Buyers' disclosures confirm the scale of TPU demand. Anthropic's minimum commitment is at least $121.3B, its Broadcom rent is $161.2B, and it estimates a further $125–150B. Alphabet's own inventory rose more than fivefold in nine months, to $13.3B of mainly TPU systems, which Kurian says are tied to committed contracts.

No supplier statement was found from MediaTek or TSMC about TPU work, so their side could not be checked. Alphabet is now simultaneously Anthropic's supplier, investor, lender and competitor.

## Amazon's Annapurna Labs: 1.4M Trainium2 chips landed, but no independent performance test

Amazon does not report Trainium revenue or unit counts. The disclosures that exist are: a "chips business" run rate, whose definition has changed over time; forward revenue commitments; customer contracts, as described in Amazon's 10-Q and its counterparties' filings; and management statements on calls.

Amazon holds large equity stakes in Anthropic and OpenAI, the two labs behind Trainium's multi-gigawatt commitments. What those labs say about Trainium is therefore buyer-stated, but it is not independent of Amazon.

### Facts: Trainium2 at scale, Trainium3 shipping since early 2026, Trainium4 tied to NVIDIA IP in 2027

**Products and their stage.**

*Inferentia.* Inferentia2 (32 GB HBM, up to 190 TFLOPS FP16) has no announced successor [CS] ([AWS Inferentia page, accessed 14 Nov 2026](https://aws.amazon.com/ai/machine-learning/inferentia/)).

*Trainium2.* Announced on 28 November 2023 and generally available from 3 December 2024 [CS] ([Amazon, 28 Nov 2023](https://press.aboutamazon.com/2023/11/aws-unveils-next-generation-aws-designed-chips); [CNBC, 3 Dec 2024](https://www.cnbc.com/2024/12/03/apple-says-it-uses-amazons-custom-ai-chips-.html)). On 5 February 2026 Amazon reported **"1.4 million chips landed"** and said the chip was "fully subscribed" [CS] ([Amazon Q4 2025 results, 8-K Ex. 99.1, 5 Feb 2026](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000002/amzn-20251231xex991.htm)). By 29 April 2026 it was "largely sold out" [CS] ([Amazon Q1 2026 call transcript, TickerTrends](https://tickertrends.io/transcripts/AMZN/Q1-earnings-transcript-2026)). SemiAnalysis estimates the chip at about 500 W, 667 dense BF16 TFLOP/s and 96 GB of HBM3e on 5 nm [EST: SemiAnalysis] ([SemiAnalysis, 3 Dec 2024](https://newsletter.semianalysis.com/p/amazons-ai-self-sufficiency-trainium2-architecture-networking)).

*Trainium3.* Amazon calls it "AWS's first 3nm AI chip" and declared it "generally available" on 2 December 2025. The claims made at that point: UltraServers of up to 144 chips delivering 362 FP8 PFLOPs; and "up to 4.4x more compute performance, 4x greater energy efficiency, and almost 4x more memory bandwidth" than Trainium2 UltraServers. [CS] ([Amazon, 2 Dec 2025](https://press.aboutamazon.com/2025/12/trainium3-ultraservers-now-available-enabling-customers-to-train-and-deploy-ai-models-faster-at-lower-cost))

The product page lists **144 GB of HBM3e at 4.9 TB/s per chip** and "up to 2x MXFP8 compute throughput compared to Trainium2" [CS] ([AWS Trainium page](https://aws.amazon.com/ai/machine-learning/trainium/)). Volume came later. Andy Jassy said on 29 April 2026 that Trainium3 "just started shipping at the start of 2026" and was "nearly fully subscribed" [CS] ([TickerTrends Q1 2026](https://tickertrends.io/transcripts/AMZN/Q1-earnings-transcript-2026)). SemiAnalysis reports the chip on TSMC N3P with CoWoS-R packaging and HBM3E from SK hynix and Micron. It also reports that most 2026 shipments are expected in the 64-chip air-cooled configuration [EST: SemiAnalysis] ([SemiAnalysis, 4 Dec 2025](https://newsletter.semianalysis.com/p/aws-trainium3-deep-dive-a-potential)).

*Trainium4.* It is "expected to begin delivering in 2027" [CS] ([Amazon 8-K, 5 Feb 2026](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000002/amzn-20251231xex991.htm)). As of 29 April 2026 it was "still about 18 months from broad availability" [CS]. It will support NVIDIA's NVLink Fusion, which a joint AWS–NVIDIA announcement on 26–27 August 2026 said is "now being paired with NVIDIA's custom high-bandwidth memory (NVHBM) technology" [CS via press] ([StorageReview, 27 Aug 2026](https://www.storagereview.com/news/aws-and-nvidia-to-deploy-2-million-more-gpus-in-2027-2028-bringing-vera-cpus-and-custom-nvhbm-to-trainium)).

*Selling chips outside AWS.* Jassy said on 29 October 2026: "We intend to do so late in 2027" [CS] ([Amazon Q3 2026 call, Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/10/30/amazon-amzn-q3-2026-earnings-call-transcript/)).

*Project Rainier.* This is Anthropic's Trainium2 cluster in New Carlisle, Indiana. It was activated on 29 October 2025 with "nearly 500,000" chips, in an $11B site [CS via press] ([Converge Digest, 29 Oct 2025](https://convergedigest.com/aws-activates-project-rainier-data-center-campus/)). Epoch AI's satellite and permit analysis estimates the following as of 19 October 2026 [IV: Epoch AI for construction and power; EST for chip counts] ([Epoch AI, updated 19 Oct 2026](https://epoch.ai/data/ai-data-centers/directory/anthropic-amazon-new-carlisle)): buildings 1–18 operational; about **1,037 MW of IT power**; and an air permit implying 2.3 GW of facility power.

**Milestones met, slipped and pending.**

| Commitment (date) | Status at 14 Nov 2026 | Source |
|---|---|---|
| Trainium2 "will be available" (28 Nov 2023, no date given) | **Met**: GA 3 Dec 2024 | [CNBC](https://www.cnbc.com/2024/12/03/apple-says-it-uses-amazons-custom-ai-chips-.html) |
| Rainier "capacity expected to exceed one million Trainium2 chips by the end of 2025" (29 Oct 2025) | **Unconfirmed for Rainier**. On 5 Feb 2026 Jassy still cited "500,000 chips there". Anthropic's ">1M Trainium2" (20 Apr 2026) is fleet-wide | [Converge Digest](https://convergedigest.com/aws-activates-project-rainier-data-center-campus/); [TickerTrends Q4 2025](https://tickertrends.io/transcripts/AMZN/Q4-earnings-transcript-2025); [Anthropic, 20 Apr 2026](https://www.anthropic.com/news/anthropic-amazon-compute) |
| Trainium3 "preview at the end of this year with much fuller volumes coming in the beginning of '26" (30 Oct 2025) | **Met on paper.** "GA" was declared 2 Dec 2025, but shipping started early 2026. The supplier's N3 mass production for an unnamed North American customer began in May 2026 | [Motley Fool Q3 2025 call](https://www.fool.com/earnings/call-transcripts/2025/10/31/amazon-amzn-q3-2025-earnings-call-transcript/); [TrendForce, 26 May 2026](https://www.trendforce.com/news/2026/05/26/news-alchip-says-key-customers-ai-chip-enters-mass-production-in-may-asics-seen-outpacing-gpu-cagr/) |
| Trainium3 supply "nearly all … committed by mid-2026" (5 Feb 2026) | **Met (company-stated)**: "nearly fully subscribed" (29 Apr 2026) | [TickerTrends Q1 2026](https://tickertrends.io/transcripts/AMZN/Q1-earnings-transcript-2026) |
| Anthropic "nearly 1GW total of Trainium2 and Trainium3 capacity" by end-2026 (20 Apr 2026) | **Pending** | [Anthropic, 20 Apr 2026](https://www.anthropic.com/news/anthropic-amazon-compute) |
| Trainium4 deliveries in 2027; OpenAI's ~2 GW Trainium "begins ramping in 2027"; external chip sales "late in 2027" | **Pending** | [Amazon 8-K, Q1 2026](https://www.sec.gov/Archives/edgar/data/0001018724/000101872426000012/amzn-20260331xex991.htm) |
| AWS power capacity doubled from the 2025 level by end-2027 (30 Jul 2026) | **Pending**. Amazon also said: "we will still not have enough capacity to meet all the demand we have in 2026" | [StockAnalysis, Q2 2026 call transcript](https://stockanalysis.com/stocks/amzn/transcripts/657334-q2-2026/) |

**Revenue, margins, cash and debt.** All AWS segment figures are company-reported.

| Quarter | AWS net sales | Y/Y | AWS operating income | Backlog stated on call |
|---|---|---|---|---|
| Q3 2025 | $33.0B | 20% | $11.4B | $200B |
| Q4 2025 | $35.6B | 24% | $12.5B | $244B |
| Q1 2026 | $37.6B | 28% | $14.2B | $364B (excluding the >$100B Anthropic deal) |
| Q2 2026 | $42.2B | 37% | $16.6B | $496B |
| Q3 2026 | **$46.0B** | **39%** | **$17.8B** | **$578B** |

Sources: [Amazon 8-K Ex. 99.1, Q4 2025](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000002/amzn-20251231xex991.htm); [Amazon 8-K Ex. 99.1, Q3 2026, 29 Oct 2026](https://www.sec.gov/Archives/edgar/data/0001018724/000101872426000038/amzn-20260930xex991.htm); call transcripts as cited above.

The chips business, as Amazon defines it, grew as follows. Its definition changed partway through, so the series is not like-for-like.

| Date | Run rate | Products included | Source |
|---|---|---|---|
| 5 Feb 2026 | "over $10 billion" | Graviton and Trainium | [CS] [TickerTrends Q4 2025](https://tickertrends.io/transcripts/AMZN/Q4-earnings-transcript-2025) |
| 29 Apr 2026 | "exceeded $20 billion" | Graviton, Trainium and Nitro | [CS] [Amazon 8-K, Q1 2026](https://www.sec.gov/Archives/edgar/data/0001018724/000101872426000012/amzn-20260331xex991.htm) |
| 30 Jul 2026 | "over $25 billion" | Graviton, Trainium and Nitro | [CS] [About Amazon, 31 Jul 2026](https://www.aboutamazon.com/news/aws/amazon-ai-chips-business-history) |

Amazon has also quantified Trainium demand: "over $225 billion in revenue commitments for Trainium" (29 April 2026); and Graviton and Trainium revenue commitments "have each increased more than 20x year-over-year" (29 October 2026).

These commitments are a contractual forward measure, not recognized revenue [CS]. CFO Brian Olsavsky said on 29 October 2026 that "the outsized growth of AI puts margin pressure on the business as a whole because the margins are lower there".

Amazon's 2026 capex guidance rose from "about $200 billion" to "approximately $220 billion", with "the higher cost of memory pushing this number up" (30 July 2026) [CS] ([StockAnalysis Q2 2026](https://stockanalysis.com/stocks/amzn/transcripts/657334-q2-2026/)). Long-term debt at face value rose from $68.8B (31 December 2025) to **$180.9B** (30 September 2026). The increase came through about $115B of 2026 issuance in dollars, euros, Swiss francs, Canadian dollars and sterling, plus a $17.5B term loan [CS] ([Amazon 10-Q Q3 2026, filed 30 Oct 2026](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm)).

Amazon never disclosed the 2015 Annapurna purchase price. Globes reported about $350M, citing sources [PRESS-U] ([Globes, Jan 2015](https://en.globes.co.il/en/article-amazon-acquires-annapurna-labs-for-350m-1001003315)).

**Unit estimates.** None of the following is company data:

| Source | Estimate |
|---|---|
| Epoch AI (model) | Cumulative Trainium output of about **2.6M through Q2 2026**. For H1 2026: a median of 600k Trainium2 (90% interval 400k–900k) and under 100k Trainium3 (30k–300k) |
| JPMorgan (cited by Epoch) | 600k Trainium2 plus 1.5M Trainium3 shipped in 2026 |
| Morgan Stanley | About 1.1M Trainium2/2.5 shipped in 2025, with a gap to installations attributed to PCB yields |

[EST] ([Epoch AI methodology](https://epoch.ai/data/ai-chip-sales-documentation/methodology); [Morgan Stanley via X relay, 10 Jul 2025](https://x.com/Jukanlosreve/status/1943316885434663204))

**Customers and contracts.** Two contracts dominate, and both include, in the 10-Q's words, "contractual obligations related to the performance of AWS chips" [CS] ([Amazon 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm)).

*Anthropic.* Anthropic committed more than **$100B over ten years**. Its S-1/A states a minimum of at least **$110.0B between May 2026 and April 2036**, with a true-up [BUY] ([Anthropic S-1/A No. 2](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm)). Anthropic's announcement of 20 April 2026 describes [BUY] ([Anthropic, 20 Apr 2026](https://www.anthropic.com/news/anthropic-amazon-compute)): "up to 5 gigawatts" across Graviton and Trainium2 through Trainium4; current use of "over one million Trainium2 chips to train and serve Claude"; and AWS as Anthropic's "primary training and cloud provider for mission-critical workloads".

Amazon's 10-Q shows its investment in Anthropic: $5.0B each in Series G and Series H during Q2 2026; a financing facility of up to $20.0B, **reduced to $15.0B** after the Series H purchase, drawable "as we reach certain delivery milestones of compute capacity under the amended commercial arrangement"; Anthropic convertible notes carried at a fair value of about **$146.2B**; and nonvoting preferred stock carried at about $92.5B. [CS] ([Amazon 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm))

The $15.0B figure matches the "Amazon 2026 NPA" of $15.0B in Anthropic's S-1/A. That reconciles a $5B difference the customer-contracts notes had left open.

*OpenAI.* OpenAI's existing $38B commitment was expanded "by $100.0 billion over 8.0 years" [CS] ([Amazon 10-Q](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm)). The expansion includes about 2 GW of Trainium3 and Trainium4 ramping from 2027 [CS] ([Amazon, 27 Feb 2026](https://press.aboutamazon.com/2026/2/openai-and-amazon-announce-strategic-partnership)). Amazon's **$50B** equity investment in OpenAI was fully funded by Q3 2026.

*Others.* The remaining customers appear only in testimonials or pilots that AWS curates, with no contract terms: Decart, Karakuri, Poolside and Ricoh; Uber, described as "piloting Trainium3" in July 2026; and Apple, whose only primary statement, from December 2024, describes "early stages of evaluating Trainium2". [CS/BUY] ([About Amazon, 31 Jul 2026](https://www.aboutamazon.com/news/aws/amazon-ai-chips-business-history); [CNBC, 3 Dec 2024](https://www.cnbc.com/2024/12/03/apple-says-it-uses-amazons-custom-ai-chips-.html))

**Capacity.** Annapurna Labs does the front-end design. According to SemiAnalysis, Alchip took back-end design for Trainium3 and leads both Trainium4 tracks. SemiAnalysis says Marvell "lost the Trn3 design competition after poor Trn2 execution and interposer problems" [EST: SemiAnalysis] ([SemiAnalysis, 4 Dec 2025](https://newsletter.semianalysis.com/p/aws-trainium3-deep-dive-a-potential)). Marvell's position, as reported in March 2026, is that the reported loss of AWS business "has not happened" [SUP via press] ([Next Platform, 6 Mar 2026](https://www.nextplatform.com/connect/2026/03/06/custom-compute-engine-biz-growing-more-than-marvell-ever-hoped/4093772)).

Alchip, which never names Amazon, gave the following figures [SUP via press] ([BigGo Finance, 14 Aug 2026](https://finance.biggo.com/news/TW_3661.TW_2026-08-14)): a North American customer's 3 nm accelerator "entered mass production in May" 2026; Q2 2026 revenue of **US$241.7M**, up 82.6% quarter on quarter; gross margin falling from 50.2% to about 34.9%; and N3 at 47% of revenue.

Morgan Stanley estimated Amazon-linked 2026 CoWoS demand at about 50k wafers via Alchip [EST] ([36Kr, 4 Dec 2025](https://eu.36kr.com/en/p/3580962946874242)).

Amazon names power as the bottleneck. It added 1.2 GW in Q4 2025, and Jassy said on 30 October 2025 that "maybe the bottleneck is power" [CS]. TechCrunch reported that Anthropic and Bedrock "are already consuming Trainium chips faster than Amazon can produce them" [PRESS] ([TechCrunch, 22 Mar 2026](https://techcrunch.com/2026/03/22/an-exclusive-tour-of-amazons-trainium-lab-the-chip-thats-won-over-anthropic-openai-even-apple/)).

**Key people.** Since 17 December 2025 Peter DeSantis has led a combined organization covering AGI/Nova models, silicon (Graviton, Trainium, Nitro) and quantum computing, reporting to Jassy. His title is now "SVP, Amazon AI Models, Chips, & Quantum Computing". Rohit Prasad left at the end of 2025 [CS via press] ([PYMNTS, 17 Dec 2025](https://www.pymnts.com/amazon/2025/amazon-reorganization-combines-ai-silicon-and-quantum-computing/); [About Amazon, 31 Jul 2026](https://www.aboutamazon.com/news/aws/amazon-ai-chips-business-history)).

Matt Garman is AWS CEO. Named Annapurna engineering leaders include Rami Sinno, Gadi Hutt, Kristopher King and Mark Carroll. Current titles for Ron Diamant, Dave Brown and Nafea Bshara could not be verified.

**Legal and regulatory.**

*Xockets patent cases.* Xockets sued AWS in the Western District of Texas (June 2025) over Nitro. In May 2026 it filed an ITC complaint naming Amazon, AWS, **Annapurna Labs**, NVIDIA and Microsoft over EC2 P6e-GB200 UltraServers, and the ITC instituted an investigation in June 2026. Amazon disputes the allegations [CS] ([Amazon 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm)). The products at issue are GPU servers, not Trainium.

*UK competition review.* The CMA found on 27 September 2024 that the Amazon–Anthropic partnership "does not qualify for investigation". The case page shows no later updates covering the 2026 investments [REG] ([UK CMA case page](https://www.gov.uk/cma-cases/amazon-slash-anthropic-partnership-merger-inquiry)).

*Microsoft.* The FT reported, citing unnamed sources, that Microsoft may believe the OpenAI–Amazon deal violates its own OpenAI agreement [PRESS-U] ([TechCrunch citing FT, 22 Mar 2026](https://techcrunch.com/2026/03/22/an-exclusive-tour-of-amazons-trainium-lab-the-chip-thats-won-over-anthropic-openai-even-apple/)).

*Export controls.* No Trainium-specific export-control action was found. Because Trainium has so far been offered only as a cloud service, exposure runs through cloud-access rules until external chip sales begin; this is an inference.

### Science: deployment scale is corroborated; performance claims rest on Amazon and its investees

**What is demonstrated, and by whom.** Trainium's production and use at scale rest on three partly independent lines of evidence: Amazon's figure of 1.4M Trainium2 chips landed; Anthropic's statement that it uses more than one million Trainium2 chips (Amazon is an investor in Anthropic); and Epoch AI's satellite and permit analysis, which independently shows Rainier's buildings operational at about 1 GW of IT power.

Alchip's 3 nm mass production from May 2026 is consistent with Trainium3. The identification is Epoch's and TrendForce's, not Alchip's. Amazon says it serves "the majority and most of Bedrock" on Trainium (29 October 2026), which is self-reported [CS].

**What remains unproven.** Neither Trainium nor Inferentia appears in any 2025 or 2026 MLPerf round reviewed. SemiAnalysis said in February 2026 that it would add Trainium3 to InferenceX "later this year", but no result was found [IND: MLCommons submitter lists; SemiAnalysis] ([MLCommons, 16 Sep 2026](https://mlcommons.org/2026/09/mlperf-inference-v6-1-results/); [InferenceX v2](https://inferencex.semianalysis.com/blog/inferencex-v2-nvidia-blackwell-vs-amd-vs-hopper)). Every quantitative performance claim therefore comes from Amazon or from customers Amazon selects or invests in. The claims are: Trainium2 is "30 to 40%" better on price-performance than comparable GPUs (February 2026), later "about 30%" (April 2026); Trainium3 delivers "over five times the output tokens per megawatt of Trainium2" and "up to 40% better price-performance"; Trainium will "save us tens of billions of dollars of CapEx each year"; and customers "saved more than $2 billion in Q3 alone". [CS] ([About Amazon](https://www.aboutamazon.com/news/aws/amazon-ai-chips-business-history); [Motley Fool Q3 2026](https://www.fool.com/earnings/call-transcripts/2026/10/30/amazon-amzn-q3-2026-earnings-call-transcript/))

AWS-claimed day-zero utilization on Trainium3 (43% with torch.compile, about 60% with hand-written kernels) was reported by SemiAnalysis, not measured by it.

The only documented negative evidence dates from the Trainium1/2 era. A July 2025 internal Amazon document, reported by Business Insider and seen only via secondary relays, recorded three customer findings: Cohere found Trainium1/2 underperforming H100s; Stability AI found Trainium2 "less competitive"; and Typhoon found A100s up to 3x more cost-efficient than Inferentia2 for some workloads.

Amazon called the Cohere case "not current" [PRESS-U] ([X relay of BI, 8 Nov 2025](https://x.com/HyperTechInvest/status/1987131006315270522)).

**Physical and engineering limits.** SemiAnalysis's architecture work documents the main constraints [EST: SemiAnalysis] ([SemiAnalysis, 3 Dec 2024](https://newsletter.semianalysis.com/p/amazons-ai-self-sufficiency-trainium2-architecture-networking); [4 Dec 2025](https://newsletter.semianalysis.com/p/aws-trainium3-deep-dive-a-potential)).

*Trainium2.* Scale-out bandwidth is 6.4x to 25.6x below scale-up bandwidth. One failed chip could take down a 64-chip domain, and fault-tolerant routing was not implemented. Its arithmetic intensity (225.9 BF16 FLOP/byte) is lower than the 300–560 range of TPUv6e, GB200 and H100.

*Trainium3.* The switched 144-chip domain uses first-generation PCIe switches that are "not all-to-all". Cross-rack bandwidth is under 10% of in-rack bandwidth. The liquid-cooled configuration needs 368 switches and 11,520 copper cables per 144-chip domain. There is no native NVFP4 support, and MXFP4 runs no faster than MXFP8. BF16 throughput is unchanged from Trainium2.

*Trainium4.* It depends on NVIDIA's NVLink Fusion and NVHBM for scale-up and memory.

*Power.* Amazon itself names power as the binding constraint.

**Whether it stands on solid ground.** Trainium's existence, production volume and large-scale use stand on solid ground. Amazon's statements, Anthropic's statements, Epoch's independent site analysis and supplier data all converge.

The performance, efficiency and price-performance multiples do not stand on independent ground. No standardized third-party benchmark of Trainium2 or Trainium3 exists in the record, and NVIDIA's CEO has publicly challenged the headline price-performance claim. Engineering risk concentrates in five areas: software maturity; the scale-up topology; the next generation's reliance on NVIDIA intellectual property; HBM cost; and power.

### Cross-examination: Amazon's numbers shift in metric and scope; NVIDIA disputes concentration

| Amazon claim (date) | Outside or later source (date) | Finding |
|---|---|---|
| Trainium2 "30% to 40% more price performance than other options" (30 Oct 2025); "about 30%" (29 Apr 2026) | Jensen Huang: "I would welcome Trainium to demonstrate their 40% that they claim all the time" (15 Apr 2026) [competitor] ([Dwarkesh Podcast](https://www.dwarkesh.com/p/jensen-huang)); BI-reported internal document on Cohere and Stability AI (2025) [PRESS-U] | Untested by any standardized benchmark; claim narrowed over time |
| "Trainium is being used by a small number of very large customers" (Jassy, 30 Oct 2025) | Huang: "It's 100% Anthropic" (15 Apr 2026) [competitor] | Disputed. Amazon also names Bedrock (internal), OpenAI (from 2027) and pilot customers |
| Trainium3 "4x greater energy efficiency" (UltraServer, 2 Dec 2025) | "40% more energy efficient" (AWS claim per [TechCrunch, 2 Dec 2025](https://techcrunch.com/2025/12/02/amazon-releases-an-impressive-new-ai-chip-and-teases-a-nvidia-friendly-roadmap/)); "over five times the output tokens per megawatt" (31 Jul 2026) | Three figures on different metrics, not reconciled by Amazon |
| Trainium3 "generally available" (2 Dec 2025) | "Just started shipping at the start of 2026" (Amazon, 29 Apr 2026); supplier mass production May 2026; Epoch median under 100k Trainium3 units in H1 2026 [EST] | "GA" label preceded volume |
| Rainier to exceed 1M Trainium2 by end-2025 (29 Oct 2025) | Jassy: "500,000 chips there" (5 Feb 2026); Anthropic's ">1M" is fleet-wide | Unconfirmed for Rainier |
| "1.4 million" Trainium2 chips landed (5 Feb 2026) | TechCrunch: "1.4 million Trainium chips are deployed across three generations" (22 Mar 2026) | Press restated the figure with a different scope |
| Marvell lost Trainium3 to Alchip (SemiAnalysis, 4 Dec 2025) [EST] | Marvell: reported loss "has not happened" (Next Platform, 6 Mar 2026) [SUP] | Unresolved; Alchip does not name its customer |
| Amazon "won't issue any more debt this year" (to underwriters, per people familiar; [CNBC, 7 Jul 2026](https://www.cnbc.com/2026/07/07/amazon-bond-sale-ai-debt.html)) [PRESS-U] | 10-Q: £4.3B sterling notes and a $17.5B term loan, both September 2026 | Contradicted, unless the statement covered only US-dollar bonds |
| Self-sufficiency in AI silicon (2024 framing) | 2 million more NVIDIA GPUs for 2027–28; Trainium4 on NVLink Fusion and NVHBM (Aug 2026) | Tension: the next Trainium relies on NVIDIA intellectual property |
| Anthropic is "training the next Claude model on top of Trainium two" (Amazon, 5 Feb 2026) | Podcast host: Claude "trained on TPU" (15 Apr 2026, interviewer assertion); Anthropic describes three platforms | Unresolved for any specific model |
| Investment conditioned on chip use (The Information via The Decoder, Nov 2024) [PRESS-U] | Semafor (two unnamed people, Mar 2025): separate decisions; 10-Q: facility unlocks on "delivery milestones of compute capacity" | Current filing ties financing to compute delivery |

The buyers' own documents confirm the size of Amazon's two anchor contracts: **Anthropic:** at least $110.0B through April 2036 [BUY]. **OpenAI:** a $38B plus $100B commitment, as recorded in Amazon's 10-Q and in OpenAI's own announcement.

Both buyers received equity investment or financing from Amazon in the same period. No supplier (TSMC, SK hynix, Micron or Samsung) has named AWS or Trainium in any statement found.

## Huawei's Ascend unit: system-scale deployment confirmed, built partly on foreign dies and memory

Huawei discloses neither Ascend revenue nor Ascend shipments. The evidence available for the unit is: Huawei's roadmap keynotes and executive interviews; unnamed-source reporting by Reuters, Bloomberg, the FT and The Information; estimates by SemiAnalysis, Epoch AI, IDC and Bernstein; US government records; and one teardown firm, TechInsights, which checks physical provenance.

No Ascend product appears in any MLPerf round in the period, and no third party has measured the 950 series.

### Facts: 950PR launched in March 2026, 950DT due Q4 2026, and Huawei says demand exceeds supply

**Products and their stage.** Huawei ships systems built on the **Ascend 910B and 910C**. It said more than **1,000 Atlas 900 A3 SuperPoDs** had been deployed by September 2026; each holds up to 384 910C chips [CS] ([Huawei, David Wang keynote, 17 Sep 2026](https://www.huawei.com/en/news/2026/9/hc-wang-keynote)).

Huawei announced its roadmap at Huawei Connect on 18 September 2025 [CS] ([Huawei, Eric Xu keynote, 18 Sep 2025](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech)):

| Product | Planned date | Stated specification |
|---|---|---|
| Ascend 950PR | Q1 2026 | Shares the 950 die (1 PFLOPS FP8, 2 PFLOPS MXFP4); in-house "HiBL 1.0" memory |
| Ascend 950DT | Q4 2026 | 950 die; "HiZQ 2.0" memory with 144 GB at 4 TB/s |
| Ascend 960 | Q4 2027 | Double the 950 |
| Ascend 970 | Q4 2028 | – |
| Atlas 950 SuperPoD | Q4 2026 | Up to 8,192 Ascend 950DT; 8 EFLOPS FP8 |

The same keynote said the Chinese mainland "will lag in process nodes for a long time". Huawei therefore pursues performance by combining many chips over its UnifiedBus interconnect.

The 950PR launched with the Atlas 350 card in late March 2026, inside its Q1 window [PRESS] ([DIGITIMES, 24 Mar 2026](https://www.digitimes.com/news/a20260324PD210/huawei-ascend-performance-2026.html)). Huawei claims as relayed by press put the card at 1.56 PFLOPS FP4, with up to 112 GB of HiBL 1.0 and about 2.8x the H20 [CS via press] ([TechRadar](https://www.techradar.com/pro/huawei-reveals-its-latest-nvidia-h20-killer-packing-a-frankly-ridiculous-1-56-pflops-of-fp4-compute-and-up-to-112gb-of-hbm)). Outlets disagree on its bandwidth (1.4 or 1.6 TB/s) and power (a 600 W card or a module of about 900 W).

Reuters, citing unnamed sources, reported the following volume timeline for the 950PR [PRESS-U] ([TrendForce relaying Reuters, 1 Apr 2026](https://www.trendforce.com/news/2026/04/01/news-huawei-2025-r-cloud-revenue-slips/)): samples in January 2026; mass production from April; full-scale shipments in H2 2026; and about **750,000 units** planned for 2026.

On 17 September 2026 Eric Xu said "the total volume of supply available in the market is not very big". He said 950DT SuperPoDs were "still under testing", with large-scale supply expected "at the end of this year or early next year" [CS] ([Huawei roundtable summary, Media OutReach, 30 Sep 2026](https://www.manilatimes.net/2026/09/30/tmt-newswire/media-outreach-newswire/huawei-pioneers-a-new-computing-architecture-for-the-ai-era-making-one-million-processors-work-as-one-computer-summary-of-roundtable-meeting-between-eric-xu-and-international-media-outlets-on-september-17/2436416)).

Huawei Connect 2026 updated the roadmap [CS] ([Huawei, 17 Sep 2026](https://www.huawei.com/en/news/2026/9/hc-wang-keynote)): the **960DT moved to Q1 2027**, "three quarters ahead of the original roadmap"; the 960PR is due in Q3 2027; the 970 is due in 2028 and a new 980 in 2029; and a new Atlas 960E SuperPoD uses near-packaged optics and up to 4,096 NPUs, with no launch date.

Huawei Cloud's 1,024-card Ascend 950 cluster service began commercial operation in China on 30 September 2026. Its overseas start is **scheduled for 30 November 2026**, which had not arrived by 14 November [CS] ([TechNode, 18 Sep 2026](https://technode.com/2026/09/18/huawei-sets-commercial-launch-dates-for-ascend-950-ai-cluster-cloud-service/)). Huawei says its CANN software stack is now open-source and community-developed, with 61% external developers, and that Ascend is an official PyTorch backend [CS].

**Milestones met, missed and contested.**

*Met, on Huawei's account.* Atlas 900 A3 deliveries began in March 2025 and the 950PR launched in Q1 2026.

*Volume against plans.* The figures conflict:

| Source | Figure |
|---|---|
| FT, unnamed sources (Feb 2025) | Plan of about 100k 910C and 300k 910B for 2025 |
| SemiAnalysis (8 Sep 2025) | 507k Ascend units shipped in 2024 and **805k in 2025**, including 653k 910C |
| Epoch AI (Sep 2026) | About 800k in 2025; a 2026 median of about 1.5M |
| US Commerce (12 Jun 2025) | "At or below 200,000" for 2025 (see the cross-examination below) |

[PRESS-U; EST] ([TrendForce, 25 Feb 2025](https://www.trendforce.com/news/2025/02/25/news-china-advances-in-ai-chips-huawei-reportedly-boosts-yield-to-40-making-ascend-line-profitable/); [SemiAnalysis, 8 Sep 2025](https://newsletter.semianalysis.com/p/huawei-ascend-production-ramp); [Epoch AI, 4 Sep 2026, updated 24 Sep 2026](https://epoch.ai/publications/huaweis-roadmap-to-2031))

IDC, relayed by Reuters on 13 October 2026, counted **572,000 Huawei AI accelerators shipped in China in H1 2026**, a 28% unit share. NVIDIA shipped 678,000, a 34% share and down 44% year on year, out of a 2.008M-unit market [EST: IDC] ([TradingView/Seeking Alpha](https://www.tradingview.com/news/seekingalpha:62d1b5de5094b:0-nvidia-s-china-ai-chip-market-share-falls-to-34-as-huawei-gains-ground-idc/)).

*Yield.* The FT reported in February 2025, citing unnamed sources, that 910C yield had reached about 40%, with 60% targeted. No yield figure exists for the 950 series [PRESS-U].

*Problems on record.* **Training.** The FT reported (14 August 2025) that DeepSeek delayed its R2 model after "unsuccessful attempts to train it on Huawei's chips" [PRESS-U] ([TrendForce relaying FT, 14 Aug 2025](https://www.trendforce.com/news/2025/08/14/news-deepseek-r2-model-launch-reportedly-delayed-amid-huawei-ascend-chip-hurdles/)). **Prices.** Reuters sources reported 950DT card prices of more than RMB 250,000, 20–50% above prices two months earlier, with HBM costs given as the cause [PRESS-U] ([TrendForce, 10 Sep 2026](https://www.trendforce.com/news/2026/09/10/news-chinese-ai-chipmakers-reportedly-hike-prices-on-hbm-costs-huawei-950dt-up-as-much-as-50/)). **Capacity.** Eric Xu said "we don't have enough capacity to even satisfy the demand in China" [CS].

**Financials (Huawei group).** Huawei's 2025 annual report, audited by KPMG and published on 31 March 2026, gives the following [CS, audited] ([Huawei, 31 Mar 2026](https://www.huawei.com/en/news/2026/3/annual-report-2025)): revenue of **CNY 880.9B** (about US$126.0B), up 2.2%; net profit of CNY 68B, up 8.6%; and R&D spending of CNY 192.3B, 21.8% of revenue.

By segment, ICT infrastructure brought in CNY 375.0B, consumer CNY 344.5B and external cloud CNY 32.16B (down 3.5%) [CS via press] ([TrendForce, 1 Apr 2026](https://www.trendforce.com/news/2026/04/01/news-huawei-2025-r-cloud-revenue-slips/)).

H1 2026 revenue was CNY 467.82B, up 9.55%. Net profit was about CNY 23.4–23.8B, down about 36%, a decline press reports attribute partly to memory costs. R&D was CNY 121.38B, 25.9% of revenue [CS via press] ([TechNode, 1 Sep 2026](https://technode.com/2026/09/01/huawei-h1-revenue-rd-spending/)).

No credible estimate of Ascend revenue was found. Figures of "US$12B" circulating on low-quality websites trace to no primary source. Epoch estimates Huawei's 2026 output at about 0.88M H100-equivalents, against NVIDIA's roughly 23M, which is under 4% [EST: Epoch AI]. Huawei's cash and debt for 2024–2025 could not be extracted.

**Customers and contracts.** Customer evidence is mostly unnamed-source reporting.

*Reported by Reuters, citing unnamed sources:* ByteDance and Alibaba were planning 950PR orders after testing (27 March 2026). Huawei "remains ByteDance's largest domestic chip supplier" (10 September 2026). ([TrendForce relaying Reuters, 10 Sep 2026](https://www.trendforce.com/news/2026/09/10/news-chinese-ai-chipmakers-reportedly-hike-prices-on-hbm-costs-huawei-950dt-up-as-much-as-50/))

*Reported by Bloomberg, citing unnamed sources:* DeepSeek plans to deploy at least **160,000 Ascend 950DT**, mainly for inference, in Inner Mongolia (4 September 2026) [PRESS-U].

*On the record:* Zhipu said its GLM-Image model (14 January 2026) was trained end to end on Ascend Atlas 800T A2 servers. It did not give a chip count [BUY] ([InfoWorld](https://www.infoworld.com/article/4116787/chinese-ai-firm-trains-state-of-the-art-model-entirely-on-huawei-chips.html)). AP reported that DeepSeek V4 "was adapted for Huawei's Ascend chips" [PRESS] ([AP via WTOP, 29 Jun 2026](https://wtop.com/world/2026/06/nvidias-ai-chip-sales-in-china-stall-as-local-chipmakers-like-huawei-take-the-lead/)).

*Policy.* Beijing's guidance requires state-funded data centers to use only domestic AI chips, per Reuters, citing unnamed sources (5 November 2025) [PRESS-U] ([Tom's Hardware](https://www.tomshardware.com/tech-industry/semiconductors/china-bans-foreign-ai-chips-from-state-funded-data-centers)).

*Overseas.* Sales are small: **Malaysia.** A deputy minister announced 3,000 Ascend servers, and the announcement was retracted within a day in May 2025 ([Malay Mail, 21 May 2025](https://www.malaymail.com/news/malaysia/2025/05/21/malaysia-walks-back-huawei-ai-project-amid-us-china-tech-tensions/177551)). **Huawei's own account.** Eric Xu said in September 2026 that overseas supply "is quite limited" [CS].

**Capacity.** Huawei's 2024–2025 output relied heavily on a bank of logic dies made at TSMC and obtained through intermediaries. Estimates of its size: more than 2M dies (CSIS, March 2025, citing officials); and more than 2.9M dies (SemiAnalysis, September 2025), which SemiAnalysis expected to run out within about nine months. [EST] ([TechPowerUp relaying CSIS, 10 Mar 2025](https://techpowerup.com/333877/huawei-obtained-two-million-ascend-910b-dies-from-tsmc-via-shell-companies-to-circumvent-us-sanctions); [SemiAnalysis](https://newsletter.semianalysis.com/p/huawei-ascend-production-ramp))

The US added Sophgo to the Entity List on 16 January 2025, citing "a risk of diversion to Huawei" [REG] ([Federal Register 2025-00480](https://www.govinfo.gov/content/pkg/FR-2025-01-16/html/2025-00480.htm)).

The domestic route is SMIC's 7nm-class N+2 and N+3, which use DUV lithography only. TechInsights judges N+3 "will not be a viable solution for data center AI chips" because of low yields on large dies [IND: TechInsights] ([TechInsights, 17 Mar 2026](https://www.techinsights.com/ko/node/61228)). Huawei has not named the foundry for the 950.

HBM is the binding input: **Stockpile.** About 13M foreign stacks were stockpiled before the December 2024 US controls, enough for about 1.6M 910C, and are expected to run out in 2026 [EST: SemiAnalysis; Epoch]. **Domestic yields.** CXMT's HBM3E yields are reportedly 20–30%, against about 70% at SK hynix [PRESS-U: Reuters]. **The next chip.** The Information reported on 3 November 2026 that the next chip, the 960DT, will rely heavily on Samsung and SK hynix HBM. It said Huawei has asked some customers to source memory themselves, and described HBM smuggled inside low-end server packages [PRESS-U] ([TrendForce, 3 Nov 2026](https://www.trendforce.com/news/2026/11/03/news-china-reportedly-obtains-smuggled-hbm-via-server-packages-huawei-960dt-faces-domestic-hbm-shortage/)). **Huawei's own memory.** Huawei "has not disclosed where or how" HiBL and HiZQ memory is made ([TrendForce, 10 Sep 2026](https://www.trendforce.com/news/2026/09/10/news-chinese-ai-chipmakers-reportedly-hike-prices-on-hbm-costs-huawei-950dt-up-as-much-as-50/)).

**Ownership and key people.** Huawei Investment & Holding is owned through an employee shareholding scheme, and Huawei puts founder Ren Zhengfei's stake at "nearly 0.59%" as of 31 December 2025 [CS] ([Huawei company facts](https://www.huawei.com/br/media-center/company-facts/)). The rotating chair passed from Sabrina Meng (to 31 March 2026) to David Wang (April–September 2026). Eric Xu holds it from 1 October 2026 to 31 March 2027 [CS] ([Huawei notice](https://www.huawei.com/en/news/2026/9/rotating-chairman)).

Operating leaders named in 2025–26 sources: Zhang Dixuan, President of the Ascend Computing Business; Seaway Zhang, Computing Product Line; Zhou Yuefeng, Huawei Cloud CEO; and He Tingbo, semiconductor business.

**Legal and regulatory.**

*US export controls.* Huawei has been on the US Entity List since 16 May 2019. The foreign direct product rule was expanded in August 2020 [REG] ([84 FR 22961](https://www.govinfo.gov/content/pkg/FR-2019-05-21/html/2019-10616.htm); [85 FR 51596](https://www.govinfo.gov/content/pkg/FR-2020-08-20/html/2020-18213.htm)). BIS guidance of 13 May 2025 presumes that activity involving the Ascend 910B, 910C or 910D without authorization violates General Prohibition 10. Its initial "anywhere in the world" framing was later softened to use that "risks violating" controls [REG via law-firm summaries] ([Arnold & Porter, May 2025](https://www.arnoldporter.com/en/perspectives/advisories/2025/05/commerce-new-guidance-curb-adversaries-access-to-advanced-ai-tech)).

*TSMC's exposure.* Reuters reported in April 2025, citing unnamed sources, that TSMC "could face" a penalty of $1B or more over the Sophgo channel. No BIS charging letter or settlement was found. One web page's claim that "TSMC was fined $1 billion" is unsourced and unverified [PRESS-U] ([Taipei Times, 9 Apr 2025](https://www.taipeitimes.com/News/taiwan/archives/2025/04/09/2003834894)).

*US v. Huawei.* The US criminal case against Huawei in the Eastern District of New York, before Judge Ann M. Donnelly, went to trial with jury selection on **8 September 2026** [PRESS] ([TechTimes, 7 Sep 2026](https://www.techtimes.com/articles/326904/20260907/huawei-rico-trial-opens-tuesday-us-makes-telecom-giant-answer-criminal-enterprise.htm)).

**Charges:** racketeering, bank fraud, trade-secret theft, Iran sanctions evasion, money laundering and obstruction. **Huawei's position:** it pleaded not guilty and calls the government's narrative "demonstrably false". **Status as of 10 November 2026:** trial day 31 fell on 3 November, the defense "may rest the week of November 9", and no verdict had been reported ([Strategic Narratives, 10 Nov 2026](https://www.strategicnarratives.org/p/huawei-on-trial-6)). **Unresolved:** sources disagree on the number of counts (12 or 14).

These are unadjudicated charges, and **the verdict is pending**. None of the trial coverage reviewed mentions Ascend.

*China's own measures.* China restricted NVIDIA purchases: the CAC summoned buyers over H20 orders in August 2025, and customs blocked H200 imports in January 2026, which officials described as "basically a ban for now" [PRESS-U: Reuters] ([Taipei Times, 15 Jan 2026](https://www.taipeitimes.com/News/biz/archives/2026/01/15/2003850605)).

### Science: scale-out works for inference; frontier training and every 950-series number remain unmeasured

**What is demonstrated.** Huawei can field very large scale-up systems.

**CloudMatrix 384 against GB200 NVL72.** SemiAnalysis accepts the system's specification of about **300 PFLOPS dense BF16**, about 1.7x a GB200 NVL72. It also puts all-in power at about **559 kW against about 145 kW**, which makes FLOPs per watt about **2.3x worse** [EST: SemiAnalysis] ([SemiAnalysis, Apr 2025](https://newsletter.semianalysis.com/p/huawei-ai-cloudmatrix-384-chinas-answer-to-nvidia-gb200-nvl72); [Tom's Hardware](https://tomshardware.com/tech-industry/artificial-intelligence/huaweis-new-ai-cloudmatrix-cluster-beats-nvidias-gb200-by-brute-force-uses-4x-the-power)). **Serving throughput.** Huawei's own paper reports serving DeepSeek-R1 at 1,943 decode tokens/s per NPU under a 50 ms time-per-output-token. It has not been independently replicated [company-authored] ([arXiv 2506.12708, Jun 2025](https://arxiv.org/abs/2506.12708)). **Post-training.** A Huawei-led team reported full-parameter post-training of DeepSeek V4-Pro (1.6T parameters) on at least 1,000 910C chips at **34.22% MFU**. That figure is the authors' own measurement, against a non-NVIDIA baseline [CS via press] ([Implicator.ai](https://www.implicator.ai/deepseeks-huawei-chip-training-claim-finally-gets-its-benchmarks-and-its-doubters/)). **Inference support.** SemiAnalysis noted that Huawei's CANN and NVIDIA's CUDA were the only stacks with day-zero DeepSeek V4 support. It published Ascend 950DT profiler traces but no throughput numbers [IND: SemiAnalysis] ([InferenceX, 9 Jun 2026](https://inferencex.semianalysis.com/blog/deepseekv4-16t-day-0-to-day-43-performance)).

**Who outside Huawei verified what.** TechInsights' teardowns establish **provenance, not performance**. Ascend 910C samples contain **TSMC-made dies and Samsung/SK hynix HBM** (October 2025), as did a 910B (October 2024) [IND: TechInsights, via Bloomberg] ([Bloomberg Law, 3 Oct 2025](https://news.bloomberglaw.com/international-trade/huawei-used-tsmc-samsung-sk-hynix-components-in-top-ai-chips); [Notebookcheck, 3 Oct 2025](https://www.notebookcheck.net/TSMC-die-and-Samsung-memory-confirmed-in-Huawei-910C-set-to-replace-Nvidia-AI-chips.1130790.0.html)). TechInsights also confirmed that SMIC's N+3 (Kirin 9030) is "significantly less scaled" than 5 nm ([TechInsights, 11 Dec 2025](https://www.techinsights.com/blog/smic-n3-confirmed-kirin-9030-analysis-reveals-how-close-smic-5nm)).

**What remains unproven.** No independent evidence was found for the following: **Frontier-scale pre-training on Ascend.** The FT's R2 report and a Tsinghua expert stand against it; the expert told MIT Technology Review that DeepSeek "appears to have adapted only part of V4's training process for Chinese chips" [PRESS] ([Implicator.ai](https://www.implicator.ai/deepseeks-huawei-chip-training-claim-finally-gets-its-benchmarks-and-its-doubters/)). **Any 950-series specification.** There is no measurement or teardown. **HiBL and HiZQ memory performance.** Epoch even classifies the 950PR's memory as "non-HBM". **The Atlas 950 SuperPoD's claimed 4.91M training tokens/s.** **The 1M-NPU topology.** The Register called it theoretical.

**Physical and engineering limits.** **Process density.** SMIC's N+3 is about 113 MTr/mm², against about 224 for TSMC N3P. Epoch expects SMIC to stay at 5–7nm-class density through about 2030 [EST: Epoch AI]. **Yield on large dies.** Epoch illustrates the penalty: a die with 70% yield at 137 mm² implies about 12% at 800 mm² for the same defect density. **Power.** FLOPs per watt are about 2.3x worse at system level. **Optical links.** A CloudMatrix 384 needs about 6,912 transceivers, and Huawei's own Atlas 960E pitch counts 48,000 pluggable modules it aims to replace. **Memory.** Epoch estimates a usable-HBM gap with NVIDIA of 73x in 2026, narrowing to 11x in 2028. On FP4 per chip, NVIDIA's B300 is about 6.75x the 950.

**Whether it stands on solid ground.** The system-level approach stands on solid engineering ground for inference and mid-scale training: many weaker chips joined by optical scale-up. The evidence is SemiAnalysis's agreement on CloudMatrix's compute specification, production inference for Chinese models such as DeepSeek's, and more than 1,000 deployed pods (Huawei-stated).

It does not stand on solid ground for frontier pre-training or for per-chip parity. Both rest on Huawei's unmeasured claims. Every 950 and 960 specification is unmeasured. Output depends on depleting or smuggled foreign HBM and on a DUV process with density and yield ceilings. The efficiency cost, in power, is material and is not stated by Huawei.

### Cross-examination: volume, status and provenance are where Huawei's account and outside evidence diverge

| Claim (who, date) | Counter-evidence (who, date) | Finding |
|---|---|---|
| US Commerce: Huawei's 2025 Ascend "production capacity … at or below 200,000" (Under Secretary Jeffrey Kessler, House testimony, 12 Jun 2025) [REG] ([Bloomberg, 12 Jun 2025](https://www.bloomberg.com/news/articles/2025-06-12/us-says-huawei-s-2025-output-is-no-more-than-200-000-ai-chips); [SCMP](https://www.scmp.com/tech/tech-war/article/3314356/huaweis-ai-semiconductor-output-limited-200000-2025-us-commerce-official-says)) | SemiAnalysis: 805k shipped in 2025, calling 200k "significantly off the mark"; Epoch: about 800k; IDC: "just over 300,000" in H1 2025 alone [EST] | Unresolved. Probably definitional: capacity for domestic dies against shipments drawn from TSMC-made stock. The testimony was located only through press coverage; the supply-chain and customer notes could not find it |
| Atlas 950 SuperPoD "seeing large-scale commercial use" (David Wang, 17 Sep 2026); "Ascend 950 supernodes have entered commercial use" (Zhou Yuefeng, same week) [CS] | 950DT SuperPoDs "still under testing", large-scale supply "end of this year or early next year" (Eric Xu, 17 Sep 2026) [CS] | Contradiction between Huawei executives on the same day; possibly 950PR-based versus 950DT-based pods, which no source clarifies |
| "Ascend has surpassed NVIDIA" in China (Huawei, Sep 2026) [CS] | IDC H1 2026 units: NVIDIA 34%, Huawei 28% [EST]; Bernstein's 2026 forecast: Huawei about 50%, NVIDIA about 8% ([AP, 29 Jun 2026](https://wtop.com/world/2026/06/nvidias-ai-chip-sales-in-china-stall-as-local-chipmakers-like-huawei-take-the-lead/)) [EST] | Contested; depends on period, units against value, and forecast against actual |
| Self-developed HBM (HiBL 1.0) in the 950 series (Huawei, Sep 2025) [CS] | The Information: the next chip relies heavily on Samsung and SK hynix HBM, including smuggled parts (3 Nov 2026) [PRESS-U]; Epoch: 950PR uses "non-HBM memory" [EST]; TechInsights: Korean HBM inside 910C samples [IND] | Self-sufficiency in memory not shown; provenance evidence points to foreign HBM |
| 960 in Q4 2027 (2025 roadmap) | 960DT in Q1 2027 (The Information, Nov 2026) | **Resolved**: Huawei itself moved the 960DT to Q1 2027 on 17 Sep 2026. The supply-chain notes compared the press date with the 2025 roadmap |
| 950 die at 2 PFLOPS MXFP4 (Sep 2025) | Atlas 350 card at 1.56 PFLOPS FP4 (Mar 2026 launch reports) [PRESS] | Gap of 22%, unexplained |
| Atlas 960 SuperPoD with 15,488 chips (Sep 2025) | Atlas 960E with 4,096 NPUs (Sep 2026); flagged by analyst Rui Ma ([TheNextWeb, 18 Sep 2026](https://thenextweb.com/news/huawei-connect-2026-ascend-960-superpod-unifiedbus)) | Specification shrank; whether the larger pod remains planned is not stated |
| Atlas 950 SuperPoD at 6.7x the compute of NVIDIA's NVL144 (Sep 2025) | Per chip, NVIDIA's B300 has about 6.75x the 950's FP4 (Epoch) | Both true at different levels: system against chip |
| More than 40 models "natively pre-trained on Ascend and CANN" (Huawei, Sep 2026) | FT: no successful R2 training run on Ascend (Aug 2025) [PRESS-U]; Tsinghua expert's doubts on V4 [PRESS] | Frontier pre-training on Ascend not independently shown |
| DeepSeek, as relayed: V4 trained on H800 and Ascend 910C | A senior US official: smuggled Blackwell chips; NVIDIA: "far-fetched" ([Implicator.ai](https://www.implicator.ai/deepseeks-huawei-chip-training-claim-finally-gets-its-benchmarks-and-its-doubters/)) | Three-way conflict; none verified |
| TSMC "could face" a penalty of $1B or more (Reuters, Apr 2025) [PRESS-U] | A web page states "TSMC was fined $1 billion" (unsourced) | Unverified; no BIS record found |

The customer and contract record contains no buyer filing for Huawei comparable to those available for the US companies. Chinese buyers (ByteDance, Alibaba, Tencent, DeepSeek) have not disclosed Ascend purchase terms in any source found.

NVIDIA's own filings corroborate Huawei's competitive position in China: NVIDIA names Huawei as a competitor in GPUs and custom chips, CPUs and networking ([NVIDIA 10-K FY2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)). NVIDIA says it is "effectively foreclosed" from China's data-center compute market [CS: NVIDIA]. Jensen Huang told AP that Chinese competitors had become "giants" ([AP, 29 Jun 2026](https://wtop.com/world/2026/06/nvidias-ai-chip-sales-in-china-stall-as-local-chipmakers-like-huawei-take-the-lead/)).

## Cerebras: wafer-scale speed independently measured; delivery and margins strained in its own filings

Cerebras is the only one of the seven companies whose entire business is AI processors and that files its own SEC accounts as a standalone company. The research notes on it rest on primary EDGAR documents read in full: the 2024 and 2026 S-1s, the 424B4 prospectus, the 2026 earnings 8-Ks and the Q2 and Q3 2026 10-Qs.

### Facts: IPO in May 2026, revenue tripling guidance, and an OpenAI contract running behind

**Products and their stage.** Cerebras's production processor is the **WSE-3**, specified by the company in March 2024 as follows [CS] ([Cerebras, 13 Mar 2024](https://www.cerebras.ai/press-release/cerebras-announces-third-generation-wafer-scale-engine)): TSMC 5 nm process; 4 trillion transistors and 900,000 cores; **44 GB of on-wafer SRAM**; 46,225 mm² of silicon; and 125 PFLOPS peak AI compute.

The WSE-3 ships in the CS-3 system.

The **CS-4**, launched on 18 August 2026, is a rack of three "WSE-3 Turbo" wafers with direct liquid cooling. Cerebras said "first CS-4 shipments begin this quarter" and claimed: "up to 30x faster than GPU systems", with the stated basis "Artificial analysis and internal benchmarking (August 2026)"; up to 2x CS-3 performance; and up to 10x throughput per watt. [CS] ([Cerebras blog, 18 Aug 2026](https://www.cerebras.ai/blog/introducing-cerebras-cs-4))

Each CS-4 wafer keeps the WSE-3's transistor count, core count and 44 GB of SRAM ([DatacenterDynamics, Aug 2026](https://www.datacenterdynamics.com/en/news/cerebras-unveils-cs-4-rack-scale-solution-powered-by-four-trillion-transistor-wse-3t-chip/)). On 12 November 2026 Cerebras said "CS-4 will soon be in full production". It also said the **WSE-5**, for a CS-5 "targeted for early Summer 2027", was "back from the fab, completed bring up and is in system test" [CS] ([Cerebras Q3 2026 results, 12 Nov 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073366/cbrsannouncesfinancialresu.htm)). No product called "WSE-4" exists in Cerebras's materials, despite third-party pages describing one. A CS-6 with DRAM stacked on the wafer has been previewed without a date.

The business is now mainly an inference cloud. Cloud and services were 60% of revenue in the first nine months of 2026. Cerebras serves open and partner models (OpenAI, Moonshot's Kimi, Qwen, GLM, Llama) through its own data centers and through AWS Marketplace, Microsoft Marketplace, OpenRouter, Hugging Face and others [CS] ([424B4 prospectus, 14 May 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)).

Partnerships announced in 2026: **AWS** (from March 2026): AWS Trainium3 handles prefill and Cerebras CS-3 handles decode, expected on Amazon Bedrock in Q1 2027. **AMD:** pairing with AMD GPUs, "in production in Q4 2026". **Oracle:** availability in OCI "in 2027". **"A top three hyperscaler":** CNBC identifies it as Microsoft, signed in October 2026 with revenue from Q1 2027 [CS; PRESS] ([CNBC, 12 Nov 2026](https://www.cnbc.com/2026/11/12/cerebras-systems-cbrs-q3-earnings-report-2026.html)).

The G42 "Condor Galaxy" program, which the 2024 S-1 described, does not appear in the 2026 prospectus. No delivery confirmation was found for CG-3, which was announced in March 2024 as "available Q2 2024".

**Milestones met, slipped and pending.**

| Commitment (date) | Status at 14 Nov 2026 | Source |
|---|---|---|
| IPO (public S-1 of 30 Sep 2024) | **Slipped about 19.5 months.** Registration was withdrawn on 3 Oct 2025, refiled on 17 Apr 2026, and **priced 13 May 2026 at $185**, $25 above the top of a raised range, raising "$6.4 billion in gross proceeds" | [EDGAR index](https://data.sec.gov/submissions/CIK0002021728.json); [Cerebras, 13 May 2026](https://www.cerebras.ai/press-release/cerebras-systems-announces-pricing-of-initial-public-offering); [Q1 2026 release](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026044941/cbrsannouncesfinancialresu.htm) |
| G42's $1.43B purchase commitment and $335M share purchase (2024 S-1) | **Not met; terminated.** The share purchase was not consummated by 15 Apr 2025, and the commercial agreement was "terminated in its entirety" | [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm) |
| Six new data centers across North America and Europe by Q4 2025 (11 Mar 2025) | **Partly met.** As of May 2026, facilities are "in California, Oklahoma, and Canada"; Norway and Finland were contracted by Nov 2026 | [Cerebras, 11 Mar 2025](https://www.cerebras.ai/press-release/cerebras-announces-six-new-ai-datacenters-across-north-america-and-europe-to-deliver-industry-s); [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm) |
| OpenAI's 750 MW, delivered in tranches over 2026–2028 (Dec 2025) | **Behind contract.** "We delivered less capacity to OpenAI than the quantity contemplated by the MRA"; service credits have accrued since 1 Oct 2026; delays "may continue through a portion of 2027" | [10-Q Q3 2026, filed 12 Nov 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm) |
| CS-4 shipments in Q3 2026 (Aug 2026) | **Met per Cerebras**; "full production" pending | [Q3 2026 release](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073366/cbrsannouncesfinancialresu.htm) |
| CS-5 in early summer 2027; 700 gross MW by end-2027; revenue to "triple" in 2027 | **Pending** | same |

**Revenue, margins, cash and debt.** All figures are company-reported.

| US$ millions | FY2024 | FY2025 | Q1 2026 | Q2 2026 | Q3 2026 |
|---|---|---|---|---|---|
| Revenue (GAAP) | 290.3 | 510.0 | 193.4 | 180.1 | **210.8** (hardware 68.9; cloud 141.9) |
| GAAP gross margin | 42.3% | 39.0% | 45% | 14% | 20.0% |
| GAAP net income (loss) | (481.6) | 237.8 | (14.0) | (450.5) | (161.2) |
| "Core" revenue (non-GAAP) | – | – | 191.3 | 209.9 | 230.9 |
| Remaining performance obligations | – | 24,600 | – | 25,400 | **26,100** |

Sources: [424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm); [Q1 2026 release, 23 Jun 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026044941/cbrsannouncesfinancialresu.htm); [10-Q Q2 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056357/cbrs-20260630.htm); [10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm).

The GAAP swings come from large non-cash items: **FY2024:** a $401.3M charge on a G42 forward contract. **FY2025:** a $363.3M gain when that forward contract was extinguished. **2026:** $541.7M of stock compensation and amortization of warrants issued to customers.

"Core" revenue excludes pass-through data-center revenue and adds back the amortization of customer warrants.

Cerebras raised its FY2026 core revenue guidance from $855–865M (June) to $880–890M (August) and then to **$940–960M** (12 November 2026). It expects 2027 revenue to "triple" [CS].

The balance sheet and cash flow at 30 September 2026 [CS] ([10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)): liquidity of about **$7.8B** (cash $3.07B, investments $4.29B, restricted cash $0.44B); an OpenAI working-capital loan of **$829.1M** outstanding, at 6%, repaid through service credits; an undrawn $850M revolving credit facility; about **$8.5B** of data-center leases signed but not yet commenced; and operating cash flow of −$388.9M and capital expenditure of $1.05B in the nine months.

Cerebras disclosed **material weaknesses in internal control over financial reporting** for both 2024 and 2025.

Funding before the IPO: Series G of $1.1B at $36.23 per share (September–October 2025), at an $8.1B valuation [PRESS] ([Crunchbase News, 6 Oct 2025](https://news.crunchbase.com/public/ipo/cerebras-systems-halts-ipo-ai-semiconductors/)); and Series H of $1.0B at $89.02 per share (January–February 2026) [CS].

Shares closed their first trading day (14 May 2026) at $311.07, a market value of about $95B. By 2 October 2026 they had fallen to $166.43 [PRESS] ([CNBC, 14 May 2026](https://www.cnbc.com/2026/05/14/cerebras-cbrs-stock-trade-nasdaq-ipo.html); [CNBC, 2 Oct 2026](https://www.cnbc.com/2026/10/02/cerebras-stock-hits-post-ipo-low-on-nvidia-pressure-lockup-expiration.html)). Around the main lockup expiry they were about $98, rising to about $109 intraday on 13 November [PRESS, secondary].

**Customers and contracts.** Customer concentration has shifted between customers but has not fallen.

| Customer | FY2025 share of revenue | 9M 2026 share of revenue |
|---|---|---|
| MBZUAI | 62% | 45% |
| G42 | 24% | 9% |
| OpenAI | – | 25% |

Cerebras treats MBZUAI and G42 as related parties of each other. Two customers held 80% of receivables at 30 September 2026 [CS] ([424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm); [10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)).

*OpenAI.* The Master Relationship Agreement of December 2025 makes OpenAI "contractually committed to purchase" **750 MW**. The capacity is deployed in tranches over 2026–2028, each tranche lasting 3–4 years and extendable to 5. OpenAI holds an option on 1.25 GW more, for up to 2.0 GW. Shortfalls trigger service credits, day-for-day term reductions and termination rights after 90 days. The deal also includes: a **$1.0B loan from OpenAI** to Cerebras, funded in January 2026; and a **warrant for 33,445,026 non-voting Class N shares** at $0.00001, which vests with the loan, a market-value threshold and capacity delivery. By 30 September 2026, 10,033,508 shares had been exercised.

OpenAI generated $146.8M of Cerebras revenue in the nine months to 30 September 2026 [CS] ([10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)).

*Other warrant holders.* **AWS** received a warrant in June 2026 for 2,696,678 Class N shares at $100, which vests on AWS payment thresholds. **G42** received penny warrants for 3.5M Class N shares instead of its lapsed $335M investment.

*Customers announced without terms.* Cerebras has named the following with no contract values disclosed [CS] ([Q2 2026 release, 12 Aug 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm)): Cognition and Lovable, which hold capacity agreements; and Block, Figma, AlphaSense, GSK, CrowdStrike and Bilt.

**Capacity.** Cerebras says "we depend on one third-party foundry, … TSMC" and has "no formalized long-term supply or allocation commitments from TSMC" [CS] ([10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)). Its August 2026 release said: "We do not use HBM memory, CoWoS packaging or 3nm fabrication technology". The same release said contract-manufacturing lines at Flex, Sanmina and Rocket EMS would scale capacity more than 10x in 2026 [CS] ([Q2 2026 release](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026056186/cbrsannouncesfinancialresu.htm)).

Data-center capacity "secured for delivery by end-2027" is **700 gross MW** (November 2026). That is contracted capacity, not energized capacity. A Morgan Stanley note, seen only in a search summary, reportedly says most new capacity comes online from mid-2027 [EST, UNOPENED].

**Ownership and key people.** The founders and pre-IPO holders control Cerebras through Class B shares with 20 votes each, about 99.2% of the vote at the IPO. On the share counts of 5 November 2026, that is still about 89.6% (calc) [CS] ([424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)).

Before the IPO, the largest holders of total shares outstanding were:

| Holder | Share |
|---|---|
| Fidelity | 10.9% |
| Benchmark | 9.4% |
| Foundation Capital | 8.2% |
| Eclipse | 7.2% |
| Alpha Wave | 6.4% |
| CEO Andrew Feldman | 5.3% |

OpenAI, AWS and G42 hold or can acquire only non-voting Class N shares. Cerebras's executives are: Andrew Feldman, co-founder and CEO; Sean Lie, co-founder and CTO; Bob Komin, CFO; and Dhiraj Mallick, COO.

Feldman and Lie sold more than $240M of shares between 20 August and 25 September 2026 [PRESS] ([CNBC, 2 Oct 2026](https://www.cnbc.com/2026/10/02/cerebras-stock-hits-post-ipo-low-on-nvidia-pressure-lockup-expiration.html)).

**Legal and regulatory.** **CFIUS.** Cerebras announced in March 2025 that it had obtained "clearance" from CFIUS. Its prospectus records something narrower. CFIUS granted a request to **withdraw** the joint notice on 27 March 2025, after G42 was restructured into non-voting shares and its pricing and volume commitments were removed. G42's investment then lapsed [CS] ([424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm); [CNBC via NBC Los Angeles, 31 Mar 2025](https://www.nbclosangeles.com/news/business/money-report/ai-chipmaker-cerebras-announces-cfius-clearance-a-key-step-toward-ipo/3666820/)). **Export licences.** Cerebras holds revocable licences, with security conditions, to export CS-2, CS-3 and CS-4 systems to G42 and MBZUAI in the UAE. **Copyright.** A putative class action filed in October 2025 in the Northern District of California concerns "certain large language models and datasets". Cerebras denies the claims [CS]. **The CEO's disclosed history.** The prospectus discloses Feldman's December 2007 guilty plea to one count of circumventing accounting controls, and his 2008 SEC settlement over Riverstone Networks, both adjudicated [CS] ([424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)).

### Science: per-user decode speed is verified; cost per token, frontier-scale fit and reliability are not

**The engineering.** Cerebras stitches dies across reticle boundaries "at the wafer level, at the semiconductor fabrication plant". It handles defects through redundancy: flaws are "recognized, shut down, and routed around". The company names the physical challenges itself: yielding a chip "58 times larger than the leading GPU", and delivering power and cooling across it [CS] ([424B4](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026035214/cerebras-424b4.htm)). The CS-4's per-wafer power "backpack" holds up to 30 power supplies on 30 A breakers at up to 277 V AC. No kW figure has been published for the CS-3 or CS-4 ([ServeTheHome, 25 Aug 2026](https://www.servethehome.com/cerebras-talks-going-rack-scale-with-their-wses-at-hot-chips-2026/)).

**What is demonstrated, and by whom.**

*Inference speed.* Per-user decode speed is measured by Artificial Analysis, which benchmarks API endpoints rather than chips under controlled conditions: 981 output tokens/s on the 1-trillion-parameter Kimi K2.6, **6.7x the next-fastest GPU cloud** (May 2026) [IND: Artificial Analysis, via VentureBeat] ([VentureBeat, 20 May 2026](https://venturebeat.com/technology/cerebras-says-its-chips-run-a-trillion-parameter-ai-model-nearly-7-times-faster-than-gpu-clouds)); about **1,705–1,753 tokens/s on gpt-oss-120B in June 2026**, about 2.4x the next-fastest API (relayed, not opened) [IND: Artificial Analysis, UNOPENED] ([Fast.io](https://fast.io/resources/fastest-ai-2026/)); and a blended price of $0.39 per million tokens on gpt-oss-120b (provider page, 14 November 2026) [IND] ([Artificial Analysis](https://artificialanalysis.ai/providers/cerebras)).

Customers have published their own figures: Perplexity 1,200 tokens/s and Cognition up to 950 tokens/s [BUY] ([Perplexity, 11 Feb 2025](https://www.perplexity.ai/hub/blog/meet-new-sonar); [Cognition, 29 Oct 2025](https://cognition.com/blog/swe-1-5)).

*Scientific computing.* A team from Lawrence Livermore, Sandia and Los Alamos ran molecular dynamics on the WSE-2 at **more than 699,000 timesteps/s**, 457x Frontier's rate, and was a 2024 Gordon Bell Prize finalist. LLNL itself cautions that this does "not mean the WSE-2 is faster overall than exascale systems". It says the chip suits "smaller problems that need only one chip" [IND: LLNL] ([LLNL, 20 Nov 2024](https://www.llnl.gov/article/52081/nnsa-researchers-break-molecular-dynamics-timescale-barrier-worlds-largest-chip)). Peer-reviewed papers at SC24 and SC20 support the HPC results ([arXiv 2405.07898](https://arxiv.org/abs/2405.07898); [arXiv 2010.03660](https://arxiv.org/abs/2010.03660)).

**What remains unproven.** **Cost per token at scale.** GAAP cloud gross margin was 24.3% in Q3 2026 (core: 46.9%), and no per-token cost has been audited [CS] ([Q3 2026 release](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073366/cbrsannouncesfinancialresu.htm)). **Fitting frontier-size models in on-wafer memory.** Kimi K2.6 needed **about 20 CS-3 systems** even with 4-bit weights. At 4 bits a 1-trillion-parameter model needs about 500 GB for weights alone, roughly 11–12 wafers of 44 GB before cache (calc). The claim of more than 1,000 tokens/s on 10-trillion-parameter models is labelled an "extrapolation". **Training competitiveness.** No independent training benchmark was found, and Cerebras does not take part in MLPerf ([HPCwire, 2022, UNOPENED](https://www.hpcwire.com/2022/06/29/the-mainstreaming-of-mlperf-nvidia-dominates-training-v2-0-but-challengers-are-rising/)). **Fleet reliability.** Cerebras's 10-Q says it has "experienced … disruptions, outages, and other performance problems" and has "provided … service credits and/or refunds". **New-product multiples.** The CS-4's 10x throughput per watt and 30x speed multiples are company-only.

**Physical and engineering limits.** **Fixed on-wafer memory.** Each wafer has 44 GB of SRAM in both WSE-3 and WSE-3T, so large models must be pipelined across wafers. CS-6's stacked DRAM is the stated remedy. **Sole-source foundry.** TSMC is the only source, with no long-term allocation. **Custom packaging.** Power delivery and cooling at wafer scale require custom packaging. **Scope of the HPC advantage.** The national labs' caveats limit it to single-wafer problems.

**Whether it stands on solid ground.** The narrow technical claim, fast single-stream decode on the models Cerebras serves, stands on solid ground. Repeated independent measurement (Artificial Analysis, 2024–2026), customer-published figures and peer-reviewed HPC results support it.

The economic and scale claims do not yet stand on independent ground: **Cost.** Competitive cost per token has not been shown. **Delivery.** Reliable delivery of hundreds of megawatts is contradicted in part by Cerebras's own filings, which disclose delivery delays, service credits and low GAAP cloud margins. **Model size.** Efficient serving of frontier-size models within fixed SRAM per wafer is not shown.

### Cross-examination: marketing framings diverge most from Cerebras's own 10-Q

| Cerebras statement (date) | Outside or filed source (date) | Finding |
|---|---|---|
| "We exceeded our guidance across the board" (Q3 release, 12 Nov 2026) | 10-Q filed the same day: capacity delivered to OpenAI below the contract; service credits since 1 Oct 2026; delays into 2027 | Both true: guidance covers revenue and margin, the contract covers capacity. The release omits the shortfall |
| "Secured TSMC wafer supply needed for continued growth" (12 Aug 2026) | 10-Q: "no formalized long-term supply or allocation commitments from TSMC" (12 Nov 2026) | Different impressions of supply firmness |
| CFIUS "clearance" (31 Mar 2025) | Prospectus: notice withdrawal granted 27 Mar 2025 on representations; G42 investment never closed | Announcement overstated the outcome |
| OpenAI deal "more than $20 billion" (Cerebras, May 2026) | "Over $10 billion" (CNBC, people close to the company, 14 Jan 2026) [PRESS-U]; RPO $26.1B, of which about 67% falls after Sep 2028 | Bases differ; the press "through 2028" framing understates term length |
| "Up to 15x faster" than GPU clouds (prospectus) | The same chart: 15x on Llama-3.3 70B (2,457 vs 164 tokens/s), about 3.8x on gpt-oss-120B (1,735 vs about 458) | The multiple depends on the model chosen |
| gpt-oss-120B at more than 3,000 tokens/s (claim reported Oct 2025) | Prospectus chart 1,735 tokens/s (14 Apr 2026); Artificial Analysis relays about 1,705–1,753 | The higher claim is not reproduced |
| "Fastest inference platform on the market" | NVIDIA: 1.5M tokens/s on one GB200 NVL72 rack for gpt-oss-120b ([NVIDIA blog, 5 Aug 2025](https://blogs.nvidia.com/blog/openai-gpt-oss/)); NVIDIA licensed Groq's LPU technology and says Groq 3 LPX is "in full production" (Aug 2026) | Different metrics: aggregate rack throughput against per-user speed. No head-to-head published |
| OpenAI launch partner for GPT-5.6 Sol at 750 tokens/s (Q2 2026) | SemiAnalysis, via CNBC: OpenAI's "Ultrafast" mode for GPT-6.1 Sol runs on NVIDIA GPUs instead of Cerebras (2 Oct 2026) [PRESS]; Altman: "Cerebras is a close partner" | Unconfirmed by OpenAI beyond Altman's post |
| G42 concentration "24% of 2025 revenue, down from 85%" (CNBC, 14 May 2026) | MBZUAI, a G42 related party, was 62%, so UAE-related customers were 86% of 2025 revenue and 54% of 9M 2026 revenue (filings) | Concentration shifted between related parties |
| 2025 "net income $88 million" (CNBC, 14 May 2026) | GAAP net income $237.8M including a $363.3M non-cash gain; non-GAAP net loss $75.7M (424B4) | Different measures |
| Molecular dynamics: 748x Frontier (Cerebras, Nov 2024) | 457x with caveats (LLNL, Nov 2024); 179x (SC24 preprint, May 2024) | The lab-published figure is the conservative independent one |
| Perplexity Sonar "powered by Cerebras" | Perplexity's own footnote: the API Sonar "does not yet run on Cerebras" (11 Feb 2025) [BUY] | Partial |
| Six new data centers by end-2025 (Mar 2025) | May 2026 prospectus: facilities in California, Oklahoma and Canada only | Partly met |

The buyers' and partners' own disclosures confirm three relationships: **OpenAI:** a 750 MW commitment, recorded in Cerebras's filings; the customer-contracts notes classify it as definitive. **AWS:** a warrant tied to payments. **Microsoft:** a deal signed in October 2026, per CNBC.

TechCrunch reported the AWS–Cerebras disaggregated-inference partnership in March 2026 [PRESS] ([TechCrunch, 22 Mar 2026](https://techcrunch.com/2026/03/22/an-exclusive-tour-of-amazons-trainium-lab-the-chip-thats-won-over-anthropic-openai-even-apple/)). Cerebras's own 10-Q says it signed commercial agreements with Oracle and Microsoft "in the second half of 2026 for the sale of hardware" [CS] ([Cerebras 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm)). No Microsoft- or Oracle-side disclosure of terms was found. No supplier statement about Cerebras volumes was found.

## Cross-examination across the seven: what the notes disagreed on, and what outside sources contradict

This section does three things. It resolves the discrepancies between the research notes files, as far as the primary documents cited in them allow. It tests the companies' claims against each other and against parties none of them controls: buyers, suppliers, regulators, benchmark operators and published papers. It records the contradictions that remain.

### Twelve discrepancies between the notes files, and how far the primary sources settle them

| # | Discrepancy | What the primary sources show | Resolution |
|---|---|---|---|
| 1 | **Jensen Huang's resignation: 11 Nov 2026 (NVIDIA notes) or 12 Nov 2026 (customer-contracts notes)** | NVIDIA's Form 8-K reports that the board "accepted the resignation … effective immediately"; its date of report is **11 November 2026**. It was **filed on 12 November 2026** together with the release "NVIDIA Announces CEO Transition", dated 12 November, under the same EDGAR accession number ([8-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000082/nvda-20261111.htm); [release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000082/nvidiaannouncesceotransiti.htm)) | **Resolved.** Event date 11 November; filing and announcement 12 November. The customer-contracts notes cited the announcement date |
| 2 | **Google in MLPerf 2026.** The supply-chain notes say Google submitted to all three 2026 rounds, but not Ironwood; the NVIDIA notes say Training v6.0 had no Google TPU entries; the Google notes found no Ironwood or TPU 8 submissions | MLCommons lists Google as a submitter in Inference v6.0, Training v6.0 and Inference v6.1 ([1 Apr](https://mlcommons.org/2026/04/mlperf-inference-v6-0-results/); [16 Jun](https://mlcommons.org/2026/06/mlperf-training-v6-0-results/); [16 Sep 2026](https://mlcommons.org/2026/09/mlperf-inference-v6-1-results/)). Google's own system directories in the MLCommons results repositories list B200 and GB200 NVL72 only for Inference v6.0 ([repo](https://github.com/mlcommons/inference_results_v6.0/tree/main/closed/Google/systems)), and GB200 NVL72 only for Training v6.0 ([repo](https://github.com/mlcommons/training_results_v6.0/tree/main/Google/systems)) | **Resolved for v6.0.** Google's Inference v6.0 and Training v6.0 entries ran on **NVIDIA GPU systems**, not TPUs. **Unresolved for v6.1.** Coverage says only that Google focused on DeepSeek-R1 without naming hardware ([StorageReview](https://www.storagereview.com/news/mlperf-inference-v6-1-5-7x-per-accelerator-gains-a-512-gpu-run-and-vera-rubins-first-peer-reviewed-numbers)), and no notes file parsed the v6.1 data. Google's last visible TPU entries are Trillium in the 2025 v5.0 rounds |
| 3 | **Anthropic's commitment to Google: a "$114.5B binding minimum" (Google notes) or "at least $121.3B (plus an estimated $125–150B more)" (customer-contracts notes)** | The **original public S-1 (26 Oct 2026)**, as relayed by Equibles and CNBC, gave at least $114.5B for April 2026 to July 2033 ([Equibles](https://equibles.com/research/anthropics-s-1-checked-against-amazon-google-microsoft-and-broadcom-filings); [CNBC, 26 Oct 2026](https://www.cnbc.com/2026/10/26/anthropic-ipo-live-updates-ai-s-1-filing.html)). **S-1/A Amendment No. 2 (10 Nov 2026)**, read directly from EDGAR, describes a hosting agreement "signed Mar 2026 and amended May–Oct 2026" with a minimum of at least about $121.3B over the same period ([S-1/A No. 2](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm)). The Google notes had themselves flagged a search summary saying "an amendment raised the minimum to about $121.3B". Both files agree that the further $125–150B for 2028–2031 is Anthropic's estimate, excluded from its commitments table | **Largely resolved.** The **$121.3B in the latest filing supersedes the $114.5B**. The $6.8B difference is consistent with an amendment raising the minimum, but neither file quotes the amendment language, so the cause is inferred, not verified |
| 4 | **Broadcom–Anthropic rack financing.** Figures in the notes: a $35B vehicle with a ~$29B Broadcom guarantee; a ~$43B guarantee filed 27 Oct for an unnamed customer; a $63B vehicle closed 26 Oct; $161.2B of lease rent | See the reconciliation below the table | **Reconciled as two vehicles, two backstops and one note facility**, with the link of the October backstop to Anthropic strongly indicated but not stated in Broadcom's filing |
| 5 | **TPU v8 design partners.** Press: Broadcom builds 8t (training) and MediaTek 8i (inference). Broadcom's CEO on 2 Sep 2026: Broadcom ships v8i, MediaTek v8t | The CEO's statement appears in two independent transcripts: "Broadcom is now shipping the TPU v8i ahead of the MediaTek v8t, which in fact was initiated earlier" ([Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-broadcom-tops-q3-2026-estimates-as-ai-sales-surge-93CH-4886849); [Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/)). The opposite mapping traces to unnamed "media and supply-chain reports" ([Wccftech, 20 Apr 2026](https://wccftech.com/google-splits-tpuv8-strategy-two-chips-broadcom-training-mediatek-inference-duties/)) and an unsourced aggregator. Google names no partner, and MediaTek names no customer. Broadcom's 2027 Anthropic figure is "5 GW of TPU **v8i**", which is consistent with its own mapping | **Not resolvable by a third party.** The only attributable, on-record source says Broadcom ships v8i and MediaTek v8t. The press mapping rests on unnamed sources. A TechNews report that Broadcom's "TPU v8AX" shipments were cut was not opened |
| 6 | **Anthropic's compute by vendor.** NVIDIA 4.7 GW against TPU 4.5 GW (Google notes); Broadcom's 1 GW of Ironwood in 2026 and 3.5 GW, later 5 GW, in 2027; AMD's "up to 2 GW" | The GW-by-vendor split (NVIDIA 4.7, TPU 4.5, Trainium 1.2, AMD 0.8 GW "contracted") comes from Wccftech citing **social-media posts quoting the S-1** ([Wccftech, 27 Oct 2026](https://wccftech.com/nvidia-gpus-make-up-4-7-gw-of-anthropics-contracted-compute-topping-4-5-gw-of-cheaper-google-tpus-as-lenders-bet-on-nvidias-residual-value/)). No notes file verified it against the filing. On TPUs, 1 GW of Ironwood (2026) plus the 3.5 GW in Broadcom's April 8-K equals 4.5 GW (calc), so the "contracted" figure matches the April terms, not Broadcom's later expectation of 5 GW in 2027 or the 10 GW "line of sight" for 2028. AMD's "up to 2 GW" is a ceiling; the S-1/A describes an initial 2027 tranche worth more than $20B with an option for about the same again. The filing's **dollar** commitments, read directly, show the TPU-related total ahead of the NVIDIA-related total (see below the table) | **Partly reconciled.** GW figures and dollar figures measure different things at different dates. The "contracted" GW numbers are unverified relays, and the vendors' figures are expectations or ceilings |
| 7 | **Vera Rubin timing.** "Full production" (CES, Jan 2026); production shipments from Aug 2026; MLPerf "preview" in Sep 2026; downward spec revisions | NVIDIA's own sequence runs: "full production" (5 Jan), "ramping into full production" (~31 May), racks running at four clouds (21 Jul), production shipments "earlier this month" (26 Aug). MLPerf v6.1 lists Vera Rubin NVL72 only in the preview category, meaning not commercially available when submitted. The product page cut HBM4 bandwidth from 22 to 19.2 TB/s and NVLink from 3.6 to 3 TB/s per GPU (details in the NVIDIA section) | **Resolved as stages**, except the January "full production" wording, which NVIDIA's own later language contradicts. The specification cuts are documented and unexplained |
| 8 | **NVIDIA in China: "effectively foreclosed" against $7.88B of China revenue in Q2 FY27** | The first is data-center compute sold into China (H200 shipments under 1% of data-center revenue; outlook assumes none). The second counts **all products** by the **headquarters of the direct customer**, and NVIDIA notes "the end customer and shipping location may be different" ([NVIDIA 10-Q Q2 FY27](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)) | **Resolved as different measures.** The composition of the $7.88B is not disclosed |
| 9 | **US government estimate of Huawei's 2025 output.** The supply-chain and customer-contracts notes could not find the "≤200,000" figure; the Huawei notes found it | Under Secretary Jeffrey Kessler testified on 12 June 2025: "Huawei Ascend chip production capacity for 2025 will be at or below 200,000" ([Bloomberg, 12 Jun 2025](https://www.bloomberg.com/news/articles/2025-06-12/us-says-huawei-s-2025-output-is-no-more-than-200-000-ai-chips); [SCMP](https://www.scmp.com/tech/tech-war/article/3314356/huaweis-ai-semiconductor-output-limited-200000-2025-us-commerce-official-says)) | **Located via press coverage of the testimony.** The transcript itself was not opened |
| 10 | **Ascend 960 timing.** Q4 2027 (supply-chain notes, citing the 2025 roadmap) against a "960DT" in Q1 2027 (The Information) | Huawei moved the 960DT to Q1 2027 itself on 17 Sep 2026, "three quarters ahead of the original roadmap" ([Huawei, 17 Sep 2026](https://www.huawei.com/en/news/2026/9/hc-wang-keynote)) | **Resolved.** The supply-chain notes compared against a superseded roadmap |
| 11 | **Amazon's facility for Anthropic: "not to exceed $20.0B" (Amazon 10-Q) against a $15.0B "Amazon 2026 NPA" (Anthropic S-1/A).** The customer-contracts notes called this an unreconciled $5B difference | The Amazon notes read the 10-Q as saying the facility was **reduced to $15.0B after Amazon's $5.0B Series H purchase** ([Amazon 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm)) | **Resolved** |
| 12 | **Rubin in MLPerf.** "No Rubin MLPerf results were found" (NVIDIA notes) against preview results reported in Inference v6.1 (supply-chain notes) | MLPerf v6.1 contains Vera Rubin NVL72 **preview** entries. NVIDIA reported them as up to 2.5x GB300 NVL72 on DeepSeek-R1 and 3.7x on a Qwen3 vision-language model ([StorageReview, 16 Sep 2026](https://www.storagereview.com/news/mlperf-inference-v6-1-5-7x-per-accelerator-gains-a-512-gpu-run-and-vera-rubins-first-peer-reviewed-numbers)) | **Resolved.** The NVIDIA notes could not parse the v6.1 file; preview entries exist |

**The Broadcom–Anthropic financing, reconciled.** Anthropic's S-1/A describes five-year master equipment leases for TPU racks. They are dated 31 March 2026 and carry about **$161.2B of rent excluding interest**; the "2026 Lease" alone is about $125.2B. The leases are secured by the equipment and cross-defaulted. The filing says Broadcom assigned portions of them "to a third party in Q2 2026 and to a newly formed special-purpose financing entity in Oct 2026" [BUY] ([S-1/A No. 2](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm); [Equibles](https://equibles.com/research/anthropics-s-1-checked-against-amazon-google-microsoft-and-broadcom-filings)). Those two assignments match the two financing vehicles, and five instruments in all fit the figures in the notes:

| Instrument | Date | Size | Broadcom's exposure | What it is | Sources |
|---|---|---|---|---|---|
| **Vehicle 1** | June 2026 | **$35B** | Backstop with a "maximum potential liability … approximately $29 billion": 85% of outstanding lease amounts less rack resale value | Initial tranche led by Apollo, for Anthropic's first gigawatt | [Broadcom 10-Q Q2 FY2026](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000054/avgo-20260503.htm); [Apollo, 9 Jun 2026](https://ir.apollo.com/news-events/press-releases/detail/629/apollo-leads-35-billion-capital-solution-for-broadcom-ai) |
| **Vehicle 2** | 26 Oct 2026 | Reported at **$63B** | Second backstop to "a newly formed special purpose vehicle", with a "maximum potential liability … approximately $43 billion": 72.5% of lease amounts less rack value | Special-purpose vehicle that buys Broadcom TPU hardware and leases it to Anthropic. Bank of America, Citi and Morgan Stanley lend first-lien, Blackstone second-lien. Deliveries from 2027 | Size and structure: [Dealroom](https://dealroom.co/news/166809-blackstone-banks-line-up-63b-to-fund-broadcom-ai-chips-for-anthropic/); [Venture Atlas, 26 Oct 2026](https://www.ventureatlas.org/news/2026-10-26-broadcom-anthropic-compute-lease) (search summaries). Backstop: [Broadcom 8-K, filed 27 Oct 2026](https://www.sec.gov/Archives/edgar/data/1730168/000119312526434271/d148323d8k.htm), which does not name the customer |
| **Note facility** | – | Up to **$42B** of convertible notes | Broadcom is the lender | "Solely to finance quarterly rent obligations under the 2026 Lease Arrangement"; a financing line, not a guarantee | [Broadcom 10-Q](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm); [S-1/A No. 2](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm) |

The backstops are Broadcom's **maximum contingent exposures**, not the sizes of the vehicles, and four calculations tie the figures together. Backing out the formulas gives lease bases of roughly $34B (29 ÷ 0.85) and $59B (43 ÷ 0.725) (calc); the first matches the $35B tranche, and the second is in the vicinity of the reported $63B. The two vehicles total about **$98B against $161.2B** of five-year rent. Together the backstops cap Broadcom's exposure at about **$72B**. The convertible-note facility is the same $42B in both companies' filings.

The 26 October backstop's link to Anthropic is strongly indicated by four things: the same date, the same "newly formed" vehicle language, Anthropic's statement about an October assignment, and press reporting on the $63B vehicle. Broadcom's filing itself names no customer. The WSJ reported, as relayed by Wccftech, that this deal stalled until Broadcom offered banks a higher interest rate and loss guarantees. It also reported that lenders hold "higher conviction" in NVIDIA GPUs' residual value than in TPUs' [PRESS] ([Wccftech, 27 Oct 2026](https://wccftech.com/nvidia-gpus-make-up-4-7-gw-of-anthropics-contracted-compute-topping-4-5-gw-of-cheaper-google-tpus-as-lenders-bet-on-nvidias-residual-value/)).

**Anthropic's commitments by vendor, in dollars.** These are the figures from the latest filing, read directly [BUY] ([S-1/A No. 2](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm)):

| Vendor | Commitment |
|---|---|
| Google (TPU hosting) | at least $121.3B, plus an estimated $125–150B for 2028–2031 |
| Broadcom (TPU racks) | $161.2B of lease rent |
| Amazon (Trainium/AWS) | at least $110.0B through April 2036 |
| Microsoft (on NVIDIA systems) | $47.2–49.2B |
| SpaceXAI (NVIDIA GPUs) | up to $120.5B |
| Nscale (NVIDIA GPUs) | about $44.6B |
| Lambda (NVIDIA GPUs) | about $41.3B |
| AMD (MI450) | more than $20B for the initial tranche |

On these numbers the **TPU-related commitments (about $282.5B) exceed the NVIDIA-GPU-related ones (up to about $254B)**, calculated on contracted amounts and excluding the TPU estimate. The relayed GW figures show the opposite ordering. That difference is a matter of units and contract terms, not a contradiction of either source.

Several of these commitments are cancellable or contingent: SpaceXAI's can be cancelled on 90 days' notice after early 2027. Lambda's August 2026 contract is "currently terminable". Nscale's depends on financing.

The filing also shows Anthropic's aggregate commitments at about **$900.9B** (S-1/A No. 2). Earlier figures were $895.4B in S-1/A No. 1 (2 November) and "about $417B of future compute payments" in the original S-1, as relayed by Equibles. The scope behind the $417B figure is not stated, so the three cannot be fully reconciled.

**Anthropic's IPO size, reconciled.** Bloomberg reported that Anthropic was "seeking up to $90B" (via [Wikipedia, "Anthropic"](https://en.wikipedia.org/wiki/Anthropic)). The S-1/A offers 825M shares at $70–78. At the top of the range that is about $64.4B, which with the concurrent **$26.0B private placement** gives about $90.4B (calc). The $61.1B often quoted is the midpoint for the public offering alone.

### Independent verification is concentrated on NVIDIA and AMD

The seven companies differ sharply in how much of their technical record a party they do not control has measured. The table summarizes what the notes found for 2025–2026.

| Company | MLPerf (MLCommons-reviewed) 2026 | SemiAnalysis InferenceX (vendor-assisted, disclosed) | Artificial Analysis (endpoint speed) | Peer-reviewed or other independent technical evidence |
|---|---|---|---|---|
| NVIDIA | All three rounds, from many submitters; Blackwell GA entries; Vera Rubin NVL72 **preview** only | Extensive; NVIDIA systems ahead in most configurations SemiAnalysis tested (Feb–Aug 2026), with exceptions at specific operating points | Provider endpoints only | Customer reliability data (Meta, 16,384 H100s) |
| AMD | All three rounds; MI355X, including a 512-GPU Crusoe run; **no MI455X/Helios entries** | Extensive; competitive on some single-node FP8 points, behind on combined distributed techniques | – | – |
| Broadcom-built XPUs | **No submissions** | Jalapeño not tested | – | TechInsights architecture analysis of Jalapeño (no benchmark) |
| Google TPU | Listed as a submitter, but **2026 entries on NVIDIA systems**; last TPU entries 2025 (Trillium) | One unopened result for TPU v7 (FP8 tokens per dollar) | 2025 v6e result disputed by SemiAnalysis | Google-authored peer-reviewed papers (ISCA 2017, ISCA 2023, NSDI '24); Apple's 52% utilization on 8,192 TPUv4 |
| Amazon Trainium | **No submissions** | **None** | – | Epoch AI satellite and permit analysis of Rainier (construction and power only) |
| Huawei Ascend | **No submissions** | Ascend 950DT profiler traces only, no throughput | – | TechInsights teardowns (provenance); SemiAnalysis system-specification analysis |
| Cerebras | **No submissions** | – | Repeated per-user speed measurements, 2024–2026 | Peer-reviewed SC20/SC24 papers; LLNL and Sandia molecular-dynamics results |

Sources: MLCommons announcements for [Inference v6.0](https://mlcommons.org/2026/04/mlperf-inference-v6-0-results/), [Training v6.0](https://mlcommons.org/2026/06/mlperf-training-v6-0-results/) and [Inference v6.1](https://mlcommons.org/2026/09/mlperf-inference-v6-1-results/); [InferenceX v2](https://inferencex.semianalysis.com/blog/inferencex-v2-nvidia-blackwell-vs-amd-vs-hopper); [AgentX](https://newsletter.semianalysis.com/p/agentx-inferencexv3-does-cuda-moat); [Artificial Analysis hardware](https://artificialanalysis.ai/benchmarks/hardware); papers as cited in the company sections.

Three points follow from this distribution of evidence: **Most of the record is vendor-presented.** In 2026, Hot Chips presentations by NVIDIA (Vera Rubin), AMD (MI455X/Helios), Google (TPU 8t/8i) and Cerebras (CS-4) were all vendor disclosures. Trainium and Huawei gave no talk ([Semiconductor Engineering, 9 Sep 2026](https://semiengineering.com/can-gpus-continue-to-dominate-ai-compute/)). **Few non-vendor measurements exist for the newest chips.** No peer-reviewed work by non-vendor authors measuring Ironwood, Trainium2/3, Ascend 950 or WSE-3 was found. **The absences are not explained.** NVIDIA's CEO said competitors avoid MLPerf because "nobody wants to show up" [competitor] ([Dwarkesh Podcast, 15 Apr 2026](https://www.dwarkesh.com/p/jensen-huang)). Cerebras has long "expressed disinterest" in MLPerf ([HPCwire, 2022, UNOPENED](https://www.hpcwire.com/2022/06/29/the-mainstreaming-of-mlperf-nvidia-dominates-training-v2-0-but-challengers-are-rising/)). No reason was found for the absence of Google, AWS or Broadcom.

### Every vendor now finances part of its own demand, and the Federal Reserve calls it circular

The buyers' filings confirm that the large contracts are real, and in several cases bigger than the vendors announced. They also show that vendors are lenders, guarantors or shareholders of the same buyers.

| Vendor | Financing of its own customers | Sources |
|---|---|---|
| NVIDIA | Guarantees with maximum exposure of **$108.5B**; **$36B** of six-year capacity buybacks from "AI clouds"; equity investments of $99B plus $25B committed, including $30B in OpenAI (press-reported) and $10.0B in Anthropic's IPO placement | [NVIDIA 10-Q Q2 FY27](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm) |
| AMD | Penny warrants for up to **320M shares** to OpenAI and Meta; up to $5B of equity in Anthropic plus $2.5B in its IPO placement; $1B in Meta's equity offering | [AMD 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm); [Anthropic S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm) |
| Broadcom | Backstops of about **$72B** maximum; a $42B note facility; $1.0B in Anthropic's IPO placement | [Broadcom 10-Q](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm); [8-K, 27 Oct 2026](https://www.sec.gov/Archives/edgar/data/1730168/000119312526434271/d148323d8k.htm) |
| Alphabet | Data-center credit backstops of **$48.0B** notional (up from $16.9B at the start of 2026); a $20.0B funding facility for Anthropic, falling to $10.0B with a $10.0B IPO placement | [Alphabet 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm) |
| Amazon | **$143.7B** carrying value in Anthropic and OpenAI equity, plus a $15B Anthropic facility released on compute delivery | [Amazon 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm) |
| Cerebras | Receives rather than gives: a $1.0B loan from OpenAI; penny warrants to OpenAI, G42 and AWS | [Cerebras 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073494/cbrs-20260930.htm) |

The Federal Reserve's Financial Stability Report of **13 November 2026** describes this pattern. It says "GPU makers often provide a guaranteed residual value of the GPU collateral … supplemented with equity investments … which create a 'circular financing' dynamic". It estimates [REG] ([Federal Reserve FSR, 13 Nov 2026](https://www.federalreserve.gov/publications/files/financial-stability-report-20261113.pdf)): outstanding public advanced-computing debt above **$1.1T**; and more than **$2T** of undiscounted take-or-pay and residual-value-guarantee obligations across Amazon, Alphabet, Broadcom, Meta, Microsoft, NVIDIA and Oracle.

The Bank of England (July 2026) called the pace of AI investment "unprecedented historically". It warned that "increasing complexity and opacity in debt structures" could raise financial-stability risks [REG] ([Bank of England FSR, 7 Jul 2026](https://www.bankofengland.co.uk/financial-stability-report/2026/july-2026)).

NVIDIA's own statements on the subject have moved: **25 February 2026 (10-K):** "We have not entered into any financing arrangements." **26 August 2026 (call):** "We know some will call this circular financing. We see it differently."

Whether the guarantees fall within the 10-K's term "financing arrangements" is not stated.

### Opposing price-performance claims rest on undisclosed baselines

Between 25 November 2025 and 30 October 2026 four companies made efficiency claims that cannot all be tested against each other: **NVIDIA:** it is "a generation ahead of the industry", with "greater performance, versatility, and fungibility than ASICs" ([CNBC, 25 Nov 2025](https://www.cnbc.com/2025/11/25/nvidia-says-its-gpus-are-a-generation-ahead-of-googles-ai-chips.html)). **Google:** TPU 8t and 8i "offer up to 2.7 times better training performance and 80% better inference price performance". These are measured against Google's own previous generation, not against GPUs ([Alphabet Q3 2026 call](https://www.investing.com/news/transcripts/earnings-call-transcript-alphabet-q3-2026-profit-miss-sparks-10-afterhours-drop-93CH-4981037)). **Amazon:** Trainium has "a meaningful advantage … in price performance versus other alternatives" ([Amazon Q3 2026 call](https://www.fool.com/earnings/call-transcripts/2026/10/30/amazon-amzn-q3-2026-earnings-call-transcript/)). **Microsoft:** Maia 300 delivers "40% more tokens per watt compared to the leading GPU-based systems" ([Microsoft Q1 FY27 call](https://www.fool.com/earnings/call-transcripts/2026/10/29/microsoft-msft-q1-2027-earnings-call-transcript/)).

The baselines are undisclosed or differ. The few independent data points cut both ways: **For TPUs:** an unopened InferenceX result has TPU v7 at FP8 delivering 1.85–2.17x the tokens per dollar of GB300 NVL72 at FP8 at one operating point. **For GPUs:** in the same result, GB300 NVL72 at FP4 (Dynamo TRT-LLM) delivers more tokens per dollar at every matched point. **Lenders:** they treat GPUs as better collateral. **Buyers:** they keep multi-sourcing. Anthropic writes that it "can select chips based on the best price-performance and efficiency characteristics for each workload" ([S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm)).

Within the GPU field, AMD's claims hold on the workloads AMD chose for MLPerf and are contradicted under SemiAnalysis's combined optimizations. Cerebras's speed claims hold per user, but its multiples range from about 3.8x to 15x depending on the model chosen.

### Suppliers bound everyone's 2027 plans, and none contradicts a shipment claim

No supplier statement found directly contradicts a capacity or shipment claim by NVIDIA, AMD, Broadcom, Google, Amazon or Cerebras; this is a finding of the research, not a sourced statement. The suppliers name no customers. They do describe a shared constraint: **TSMC (July 2026):** packaging capacity "is so tight that now it's limiting my customers' growth" [SUP] ([TSMC Q2 2026 call, 16 Jul 2026](https://www.fool.com/earnings/call-transcripts/2026/07/16/tsm-tsm-q2-2026-earnings-call-transcript/)). **TSMC (October 2026):** demand "remains well above supply". TSMC's Q3 2026 revenue was **US$46.72B, up 50.9%** [SUP] ([TSMC 6-K, 15 Oct 2026](https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000726/a3q26e_withguidancexfinal.htm); [CRN Asia, 15 Oct 2026](https://www.crnasia.com/news/2026/components-and-peripherals/tsmc-third-quarter-revenue-tops-guidance-as-ceo-says-ai-dema)). **SK hynix (28 October 2026):** DRAM and HBM volumes "for the next 3 years through 2029 are effectively sold out". Long-term agreements cover more than 50% of its 2027–28 capacity [SUP] ([SK hynix Q3 2026 call](https://www.fool.com/earnings/call-transcripts/2026/10/28/sk-hynix-skhy-q3-2026-earnings-call-transcript/)). **Micron:** it has agreements for the "vast majority" of its calendar-2027 HBM supply [SUP] ([Micron FQ4 2026 call, 30 Sep 2026](https://www.investing.com/news/transcripts/earnings-call-transcript-micron-tops-q4-2026-estimates-as-demand-stays-hot-93CH-4925992)). **Samsung:** no statement on sold-out status was found.

The only customer-level allocation data are analyst estimates. Morgan Stanley's December 2025 estimate of 2026 CoWoS demand is the most complete [EST: Morgan Stanley] ([36Kr, 4 Dec 2025](https://eu.36kr.com/en/p/3580962946874242)):

| Customer | Estimated 2026 CoWoS wafers |
|---|---|
| NVIDIA | about 595k (about 60%) |
| Broadcom | about 150k (Google TPU about 90k, Meta about 50k, OpenAI about 10k) |
| AMD | about 105k |
| Marvell (AWS and Microsoft) | about 55k |
| Amazon via Alchip | about 50k |
| MediaTek (Google TPU) | about 20k |
| Global demand | about 1M |

A Mydrivers report later put NVIDIA at 800–850k wafers ([TrendForce, 5 Aug 2026](https://www.trendforce.com/news/2026/08/05/news-tsmc-reportedly-expands-outsourcing-of-key-cowos-front-end-step-to-osats-amid-rising-nvidia-asic-demand/)).

Two of the seven sit outside this picture: **Cerebras** says it uses no HBM, no CoWoS and no 3 nm, but relies solely on TSMC wafers. **Huawei** drew on TSMC dies obtained through intermediaries and on Korean HBM stockpiled before the December 2024 US controls. TechInsights' teardown showed both inside the 910C, and Epoch expects the stockpile to run out in 2026.

Other constraints on 2027 plans have multi-year lead times: **T-glass substrate cloth:** shortfall of 10–20% or more in 2026 [PRESS/EST, UNOPENED] ([Borecraft, 9 Jun 2026](https://borecraft.com/2026/06/09/the-ai-bottleneck-is-spreading-from-chips-to-substrates-glass-and-power/)). **Indium-phosphide lasers:** demand about 30% above supply, per Lumentum and LightCounting [SUP/EST, UNOPENED] ([TrendForce, 6 Aug 2026](https://trendforce.com/news/2026/08/06/news-inp-shortage-emerges-as-ai-optical-interconnect-bottleneck/)). Broadcom confirms the laser constraint on the record. **Grid power:** every company with a cloud names it.

## Events that had not happened by 14 November 2026

Several facts in this report will be overtaken within weeks. The table lists the scheduled or expected events the notes identified, with the source for each date. Items marked "press" rest on press reports, not company or court schedules.

| Date | Event | Source |
|---|---|---|
| 17 Nov 2026 | **NVIDIA Q3 FY2027 results** (quarter ended 25 Oct 2026): the first reported Vera Rubin revenue, guided at about 20% of data-center revenue; first results since the CEO change | [NVIDIA, 28 Oct 2026](https://nvidianews.nvidia.com/news/nvidia-sets-conference-call-for-third-quarter-financial-results-6928873); [CEO-transition release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000082/nvidiaannouncesceotransiti.htm) |
| 17 Nov 2026 | Cerebras TomorrowX Summit (investor event) | [Cerebras Q3 2026 release](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073366/cbrsannouncesfinancialresu.htm) |
| Not priced as of 14 Nov | **Anthropic IPO**: S-1/A No. 2 filed 10 Nov 2026 with a $70–78 range; press expected trading to begin on 19 Nov (press) | [S-1/A No. 2](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm); [CNBC live updates, 12 Nov 2026](https://www.cnbc.com/2026/11/12/nvidia-jensen-huang-ceo-live-updates.html) |
| Pending | **Verdict in US v. Huawei** (EDNY): the defense "may rest the week of November 9"; no verdict reported as of 10 Nov | [Strategic Narratives, 10 Nov 2026](https://www.strategicnarratives.org/p/huawei-on-trial-6) |
| 30 Nov 2026 | Huawei Cloud's overseas launch of its Ascend 950 cluster service | [TechNode, 18 Sep 2026](https://technode.com/2026/09/18/huawei-sets-commercial-launch-dates-for-ascend-950-ai-cluster-cloud-service/) |
| Early Dec 2026 | **AWS re:Invent 2026** (exact dates not verified); possible Trainium announcements | Amazon notes |
| 3 Dec 2026 (requested) | **Senate testimony requested from Jensen Huang** by Sen. Tim Scott (press) | [CNBC live updates, 12 Nov 2026](https://www.cnbc.com/2026/11/12/nvidia-jensen-huang-ceo-live-updates.html) |
| 9 Dec 2026 | Cerebras at the Barclays conference | [Cerebras Q3 2026 release](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073366/cbrsannouncesfinancialresu.htm) |
| 10 Dec 2026 (requested) | **Senate testimony requested from Commerce Secretary Lutnick** (press) | [CNBC live updates](https://www.cnbc.com/2026/11/12/nvidia-jensen-huang-ceo-live-updates.html) |
| About mid-Dec 2026 | **Broadcom Q4 FY2026 results** (quarter ended 1 Nov 2026), expected around mid-December by inference from the 11 Dec 2025 prior-year date. They will cover Meta MTIA production shipments, the late-2026 deliveries to Anthropic, customer five and the "other two", and the first FY2027 guide | [EDGAR filing index](https://data.sec.gov/submissions/CIK0001730168.json); [Broadcom Q3 FY2026 call](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/) |
| Q4 2026 | **Huawei**: Ascend 950DT and Atlas 950 SuperPoD large-scale supply ("end of this year or early next year") | [Huawei roundtable, 30 Sep 2026](https://www.manilatimes.net/2026/09/30/tmt-newswire/media-outreach-newswire/huawei-pioneers-a-new-computing-architecture-for-the-ai-era-making-one-million-processors-work-as-one-computer-summary-of-roundtable-meeting-between-eric-xu-and-international-media-outlets-on-september-17/2436416) |
| Q4 2026 | **Google**: TPU 8t/8i general availability "later this year", not yet confirmed. TPU 8tx and 8i Max have no dates | [Google, 22 Apr 2026](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/) |
| Q4 2026 | **AMD**: OEM Helios shipments; "big step up" in MI455X; Taalas and World Labs closings "by year-end", subject to approvals; Q4 revenue guidance of about $17.0B | [AMD Q3 2026 call](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/); [AMD 10-Q](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm) |
| Q4 2026 | **Cerebras**: AMD disaggregated inference in production; CS-4 "full production"; Q4 core revenue guidance $310–330M | [Cerebras Q3 2026 release](https://www.sec.gov/Archives/edgar/data/0002021728/000162828026073366/cbrsannouncesfinancialresu.htm) |
| End-2026 | **Anthropic**: "nearly 1GW" of Trainium2/3 capacity online; "well over a gigawatt" of TPU capacity in 2026 | [Anthropic, 20 Apr 2026](https://www.anthropic.com/news/anthropic-amazon-compute); [Anthropic, 23 Oct 2025](https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services) |
| Early 2027 | Alphabet and Meta give 2027 capex guidance on their Q4 calls; Alphabet expects a "significant" increase | [CNBC, 28 Oct 2026](https://www.cnbc.com/2026/10/28/alphabet-googl-earnings-q3-2026.html) |
| 2027 | **NVIDIA**: Rubin Ultra (Kyber NVL144), 800 VDC, 1 MW racks; Hugging Face closing (H1 2027). **AMD**: MI430X (H1), MI500, Anthropic's first gigawatt (H1). **Amazon**: Trainium4 deliveries, OpenAI's Trainium ramp, external chip sales "late in 2027". **Broadcom**: 5 GW of TPU v8i for Anthropic; 1.3 GW of Jalapeño for OpenAI. **Huawei**: 960DT (Q1), 960PR (Q3). **Cerebras**: AWS Bedrock (Q1), Microsoft revenue (Q1), OCI, CS-5 (early summer), 700 MW by year-end. **Google**: TPUs on OCI, Crux AI's first 500 MW, Project Suncatcher prototypes "by early 2027" | Company sections above |
| 2027 (suppliers) | TSMC wafer price increases from January; TSMC Arizona fab 2 volume production in Q3; Micron Singapore HBM packaging output; 8-high HBM4 for Rubin Ultra in Q2 (rumor, rated "questionable") | [TrendForce, 27 Oct 2026](https://www.trendforce.com/news/2026/10/27/news-tsmc-reportedly-eyes-20-cowos-price-hike-skips-equipment-price-renegotiations-amid-ai-demand-surge/); [CRN Asia, 15 Oct 2026](https://www.crnasia.com/news/2026/components-and-peripherals/tsmc-third-quarter-revenue-tops-guidance-as-ceo-says-ai-dema); [Micron call, 30 Sep 2026](https://www.investing.com/news/transcripts/earnings-call-transcript-micron-tops-q4-2026-estimates-as-demand-stays-hot-93CH-4925992); [Wccftech, 26 Oct 2026](https://wccftech.com/samsung-sk-hynix-downgraded-hbm4-q2-2027-nvidia-rubin-ultra/) |
| 2028 and later | NVIDIA Feynman (2028) and the first PORTS-Pike phase (FY2029); AMD MI600 (2028); Huawei 970 (2028) and 980 (2029); Broadcom's "line of sight" to an incremental 10 GW for Anthropic and more than 5 GW for OpenAI (2028); TSMC 14-reticle CoWoS and A14 (2028) | Company sections above |

Three further matters are pending without a fixed date: **NVIDIA:** the DOJ inquiry into the Hugging Face deal, the SAMR decision on Mellanox conditions, and the CEO search. **Google:** sentencing in the Linwei Ding trade-secret case. **TSMC:** the outcome of the Commerce investigation into TSMC's work for Sophgo.

## What could not be found or verified, by company

Each research track hit the session's shared web-search limit partway through. Several also ran out of credits on secondary search tools or were blocked by sites, including Reuters, DCD, Courthouse News, CACM, investors.broadcom.com, openai.com and dl.acm.org. The items below were not found, or were found only in search-result summaries, unnamed-source reports or secondary relays. They should be read as open questions, not as negative findings. Items later resolved by another notes file are marked as such.

**NVIDIA.**

*Engineering and product record.* No contemporaneous sources on the late-2024/early-2025 GB200 NVL72 rack overheating and order changes; Reuters was unreachable. Not found: NVIDIA's exact GTC 2024 Blackwell availability wording; the original GTC 2025 Vera Rubin specification sheet; any NVIDIA explanation for the September 2026 cuts to Rubin's HBM4 and NVLink bandwidth; the status of Rubin CPX; confirmation that Groq 3 LPX volume shipments occurred by 25 October 2026; and the shipping status of Quantum-X Photonics. Aggregator claims that OCI reached Vera Rubin general availability on 27 October 2026, and that CoreWeave deployed on 30 September 2026, are unverified. Measured rack power for GB300 and Vera Rubin NVL72 was not found. Nor were an independent replication of NVFP4 training at frontier scale, field reliability data for co-packaged optics, or the Hot Chips 2026 papers.

*Supply.* NVIDIA's actual CoWoS allocation is not public; only estimates exist. Not found: its N3 allocation, where Arizona-made Blackwell wafers are packaged, and the status of Foxconn and Wistron's Texas assembly. HBM4 qualification is resolved only at the level of "all three qualified". Which supplier feeds which product is undisclosed.

*Deals.* No primary document states the $30B OpenAI investment and its closing date. Not verified: NVIDIA's xAI equity history; the terms of the UAE, European sovereign and HUMAIN expansion deals; the original Nokia and Synopsys investment terms; the size of the Coherent stake; and the 2025 Lambda leaseback. Whether the $10B Anthropic IPO purchase is the same as the November 2025 "up to $10B" commitment is unknown. The 2025 CoreWeave $6.3B capacity backstop, which the customer-contracts notes could not verify, is confirmed in the NVIDIA notes by CoreWeave's 8-K.

*Legal and governance.* Not established: the final status of the GAIN AI Act, the Chip Security Act and location-verification proposals; any final SAMR decision; EU matters; patent suits; the docket of the August 2026 smuggling indictment; any shareholder suits after the resignation. The 8-K discloses no separation terms for Huang. No evidence was found either way on charges related to the alleged intelligence approach. Institutional holdings beyond the stale BlackRock figure and Vanguard were not obtained. No transcripts were obtained for the Q3 FY26, Q4 FY26 or Q1 FY27 calls. Q3 FY27 results are not yet reported.

**AMD.**

*Revenue and contracts.* AMD's Instinct and data-center AI revenue for 2025 and for each 2026 quarter is undisclosed, as is revenue concentration by customer. Only receivables concentration is disclosed. Not verified: Oracle's reported 50,000-MI450 commitment (Oracle's page returned 403); the Crusoe deal; any xAI agreement; TensorWave, Vultr and Cirrascale volumes; DOE Lux go-live; and the scale of Microsoft's Helios deployment. The structure and status of the $5B Anthropic and $1B Meta investments, the ZT Systems closing date, and the warrants' redacted price hurdles were not found.

*Engineering.* Not found: MI455X board power; Helios rack power and cooling; an authoritative per-GPU memory bandwidth (19.6 against about 23.6 TB/s); a primary-source Helios scale-up bandwidth; whether UALink or Ultra Ethernet is used; Ethernet scale-up latency. No independent MI455X or Helios performance data exist. Primary texts of SemiAnalysis's December 2024 study and InferenceMAX v1 were not retrieved.

*Supply.* Not found: HBM4 suppliers beyond Samsung and their qualification status; AMD's own CoWoS and SoIC allocation; the MI455X packaging flow; Celestica's role.

*Disclosures and legal.* Not retrieved: the Computex 2024 and October 2024 roadmap texts; any Computex 2026 data-center announcement; the Q1 and Q2 2026 call transcripts (404); the Financial Analyst Day transcript, where the "tens of billions in 2027" wording remains unverified. Not found: 2026 MI308 and MI325 China revenue; whether any 15% payment was made; the BIS text of the MI325 inspection regime; any patent suits, class actions or antitrust review of the warrants. Not verified: Vamsi Boppana's role, current titles for Papermaster and Grasby, post-March 2026 holders, and any NVIDIA rebuttal of the Helios comparisons.

**Broadcom (custom-chip division).**

*Results and disclosures.* Q4 FY2026 results are not released. Broadcom discloses no XPU dollar revenue, no per-customer revenue and no XPU or rack gross margin. No contract values are disclosed for Google, Meta or OpenAI. No AI backlog figure on the December 2025 basis has been updated. The Q3 FY2025 call transcript returned 404.

*Customers.* Not identified: customer five and the "other two" customers; the customer behind the 26 October 2026 backstop and the $42B note facility (strongly indicated as Anthropic, but not named in Broadcom's filings); and the Anthropic rack integrator. Not checked: ByteDance's status and its export-control constraints. No credible source was found for xAI or SoftBank/Arm links. Not retrieved: reports of Google moving TPU work and of OpenAI chip delays.

*Engineering.* Not verified: launch dates and specifications for Tomahawk 6, Tomahawk Ultra, Jericho3-AI/Jericho4, Thor Ultra and Tomahawk 6-Davisson CPO; whether 3.5D XDSiP or 2 nm XPUs ship in volume; Broadcom's role in TPU v1–v6. No independent verification of SerDes, CPO or 3.5D packaging, and no 2 nm yield or cost data. A reported Meta CPO reliability study is unverified. Not found: which party buys HBM for each programme, and Broadcom's own CoWoS allocation (only Morgan Stanley's estimate).

*Legal and people.* Not verified: China SAMR's VMware conditions; the EU (CISPE), US and UK VMware suits; any custom-silicon patent suits; whether the new "supply chain risk" risk factor relates to any US government designation of an AI customer. Not verified: the head of the ASIC division, current 13F holdings, and the April 2026 vote results.

**Google TPU unit (Alphabet).**

*Products.* General availability of TPU 8t and 8i is unconfirmed, and TPU 8tx and 8i Max have no dates. No FP8 or bf16 per-chip TPU 8 specifications are on a Google page that could be read. Original announcement and availability claims for TPU v4, v5e, v5p and Trillium were not re-verified.

*Benchmarks and science.* Not retrieved: MLPerf scores for any TPU entry; whether Ironwood or TPU 8 was entered in any division; Google's Inference v6.1 hardware; TPU papers from 2024–2026; independent critiques of AlphaChip (CACM blocked); academic TPU Research Cloud evaluations; the InferenceX and AgentX results Google cites; reticle data. Google did present TPU 8t and 8i at Hot Chips 2026 (via Semiconductor Engineering), but the slides were not opened.

*Financials.* Not obtained: exact Q1 2025 and Q1 2026 Cloud operating income; Cloud backlog at 30 September 2025 and 31 December 2025; backstop notionals at 30 June 2026; the details of 2025 bond issues and later 2026 non-dollar notes. Found elsewhere: the $48.0B backstop figure at 30 September 2026 and the $10.0B Crux AI backstop, both in the customer-contracts notes from the 10-Q.

*Customers and capacity.* Not verified: Meta's August 2025 Google Cloud deal; SSI, Midjourney and Salesforce usage; any confirmation of Meta's TPU rental or OpenAI's purchase plan; original 2025 neocloud backstop sizes; delivery status at the Cipher and Hut 8 sites. No credible TPU unit estimates from opened sources were found. Not found: Ironwood's process node, TPU HBM suppliers, Google's own CoWoS allocation, any MediaTek or TSMC statement on TPU work, and total TPU gigawatts deployed.

*Legal and people.* Not verified: the Singular Computing settlement, Ding's sentencing, DOJ search-case remedies touching AI investments, any 2026 antitrust or EU/UK matter on AI partnerships, and US export rules on TPU hardware or cloud access. The 10-Q legal-proceedings sections were truncated when fetched. Not found: Vahdat's promotion date, Jouppi's current role, TPU-team departures, and any NVIDIA statement on TPUs after November 2025.

**Amazon / Annapurna Labs.**

*Disclosure.* No Trainium-only revenue or unit disclosure exists, and there is no Trainium3 unit count. Alchip's Q3 2026 results were not posted. The original Business Insider article on the July 2025 internal document was found only through secondary relays.

*Benchmarks and engineering.* No MLPerf, InferenceX or peer-reviewed measurement of Trainium2 or Trainium3 exists in the record. Not found: Trainium3 chip TDP and rack power (paywalled); AWS's own wording for the Trainium4 multiples; a Trainium4 date more precise than "2027". Not confirmed: that the LNC=8 milestone shipped; that Nova models were trained on Trainium; which Claude models were trained mainly on Trainium.

*Dates and contracts.* Not confirmed from fetched primary sources: the GA dates of Inferentia1, Trainium1, Inferentia2 and Trainium2 UltraServer; the December 2024 Trainium3 announcement. Not found: the primary terms of the November 2025 $38B OpenAI deal and the conditions on the $35B equity tranche. The customer-contracts notes found it fully funded by Q3 2026 with no stated condition. Not confirmed: whether Project Rainier reached 1M Trainium2 chips; Rainier sites outside Indiana; Apple's use of Trainium after December 2024. AWS backlog for Q1 and Q2 2025 was not retrieved.

*Supply.* No statement by TSMC, SK hynix, Micron or Samsung naming AWS was found. Marvell's later 2026 remarks on AWS were not retrieved.

*Legal and people.* Not retrieved: the FTC monopolization trial date and the CMA's reasoning. No Trainium-specific export-control action was found. A single-source Tech Times item (24 September 2026) about an Anthropic export-classifier flagging Trainium3 topics could not be verified. Current titles for several Annapurna executives were not verified. The exact dates of re:Invent 2026 were not verified.

**Huawei Ascend.**

*Financials and volume.* Not obtained: Huawei's cash, borrowings and operating cash flow for 2024–2025 (the annual-report PDF could not be parsed); Q1–Q3 2026 results; H1 2026 segments. No credible Ascend revenue estimate exists. Not opened: the WSJ (1.5M units), Bloomberg (16 September 2026, market share) and full IDC releases.

*Products.* No status found for the Ascend 310, or for the 910D beyond its naming by BIS. No official Atlas 350 datasheet, and no independent test or teardown of the 950PR or 950DT. Not confirmed: Atlas 950 or 950DT volume deliveries; who makes HiBL 1.0 and HiZQ 2.0; whether the CANN open-sourcing promised for 31 December 2025 was completed; Huawei's own text for the 960PR and 970 specification updates.

*Customers and capacity.* Not found: Ascend contract details for iFlytek, Baidu, SiliconFlow and Tencent; China Telecom and China Unicom tenders; China Mobile package values; any signed contract values; any completed Middle-East deployment. The $5.6B ByteDance figure is unverified. Not found: SMIC yields and Ascend wafer allocation for 2026; whether Pengxinwei and other suspected fabs are on the Entity List; CXMT HBM volumes; any independent HiBL measurement; any 2026 US output estimate; the original CSIS text. Huawei has never disclosed its foundry or HBM sources.

*Legal and people.* Not known: trial status after 10 November 2026, including the verdict; the exact count list; the history of the original trial date. Not found: the outcome of the TSMC/Sophgo probe; the full BIS May 2025 guidance text; any 2026 Ascend-specific US rule; the status of the affiliates rule. Not found: the Union's exact stake, the board chair, and when Ken Hu left the rotating chairs.

*Science.* No independent benchmark exists of any Ascend product, and no replication of the CloudMatrix384 paper. No independent power or optical-reliability measurement was found. DeepSeek's own statement on V4 training hardware was not seen first-hand.

**Cerebras.**

*Contracts.* Not disclosed: Microsoft deal terms (value, MW, duration). Its identity as the "top three hyperscaler" rests on CNBC. Not found: Oracle terms; specifics for AstraZeneca, Mayo Clinic, Argonne, Notion and IBM; Mistral's confirmation; MBZUAI's contract form. OpenAI's own deal post returned 403, and OpenAI has not confirmed the reported GPT-6.1 Sol hardware choice.

*Delivery and engineering.* Not found: Condor Galaxy 1–3 delivery and status; energized, as opposed to contracted, megawatts; per-site megawatts and go-live dates. Not found: CS-3 and CS-4 power in kW, spare-core and redundancy percentages, wafer yield, and per-model list prices. The Artificial Analysis leaderboard figures against Groq, SambaNova and GPU clouds did not render, and Groq's and SambaNova's own claims were not retrieved. No independent training benchmark exists. Not checked: whether the 2024 Gordon Bell team won or was only a finalist, any SC25 finalist, and Cerebras's role in the 2022 GenSLM prize.

*Ownership and legal.* Not found: G42's total holding; Gary Lauterbach's role; whether co-founders Fricker and James are still employed; the Series H lead investor and Series G co-investors from primary sources. Not found: the copyright case's caption and docket, any CFIUS mitigation text, and any 2026 export-licence changes. The share price on 14 November 2026 was not captured (latest: about $109 intraday on 13 November).

**Cross-company: supply chain, benchmarks, buyers and regulators.**

*TSMC and packaging.* Not disclosed: TSMC's N4, N3 and N2 capacity in wafers per month; its CoWoS-S, CoWoS-L, CoWoS-R and SoIC splits; any supplier-confirmed customer allocation. Not opened: sources for the JPMorgan, GF Securities, TrendForce and Counterpoint TPU and Trainium unit estimates. Unresolved: TSMC's own Arizona packaging start (2028 or 2029). Official TSMC transcripts were not used; third-party ones were.

*Memory.* Not found: Samsung's sold-out status; Micron's December 2025 wording on 2026 HBM; HBM4 qualification for AMD, Google, Amazon and Broadcom programmes by name.

*Physical limits.* Not found: liquid-cooling supply data; ABF capacity; copper versus optical reach; N3/N2 yields and wafer prices; GB200/GB300 rack power from an opened source; a source for the 858 mm² reticle field and the WSE die area.

*Benchmarks and papers.* MLPerf's 2024 rounds and the 2025 v5.1 rounds were not fully checked, and the publication status of Training v6.1 is unconfirmed. Not retrieved: the InferenceMAX launch details and the Artificial Analysis hardware tables. No ISCA, MICRO, HPCA or ISSCC 2025–2026 papers on these chips were retrieved.

*Buyers and finance.* Not found: OpenAI's audited financials and commitment schedule; the Oracle contract value (reported at about $300B) and the Google Cloud value; the May 2025 CoreWeave tranche; the WSJ quarterly figures. Not found: Meta's February 2026 NVIDIA deal terms and Hyperion SPV terms; HUMAIN and Stargate UAE commitments and export licences. Not established: Amazon's and Google's ownership percentages in Anthropic; whether the November 2025 NVIDIA and Microsoft investments in Anthropic were funded before the IPO; which Fluidstack sites are live; the scope behind the "$417B" commitment figure. Not found: any Moody's or S&P rating actions; the IMF's October 2026 GFSR (not listed when fetched); academic work on circular financing.

*Export controls.* Not found: the BIS H200 rule text, the GAIN AI Act's final status, the Chip Security Act, the AI Diffusion replacement rule, and statements by CAC, MOFCOM, SAMR or Chinese customs. No disclosures by Chinese buyers (ByteDance, Alibaba, Tencent) were obtained.

## Conclusion

**Independent evidence lags each product cycle by about a year.** For every company, the claims that outsiders have measured concern chips that were already shipping by 2025 (Blackwell, MI355X, TPU v4 and Trillium, Trainium2, CloudMatrix 384 and the WSE-2/3), while the 2026–2027 generations rest mostly on vendor projections against shifting or undisclosed baselines; NVIDIA and Broadcom trimmed or reframed their own figures within months, and Google's 2026 MLPerf entries that could be checked ran on NVIDIA systems rather than TPUs. The most informative outside signals in 2026 were therefore not benchmarks but buyers' contracts, lenders' terms and disclosures of delivery shortfalls. Anthropic's filing priced its TPU commitments above its NVIDIA-GPU commitments; banks required extra Broadcom guarantees before financing TPU racks while preferring NVIDIA GPUs as collateral; and it was Cerebras's own 10-Q, not its press release, that disclosed the OpenAI capacity shortfall. The same filings show how far vendors now underwrite their own demand, which turns customer commitments into joint exposures that the Federal Reserve is now tracking.

**The tests that will separate claim from fact are dated and close.** NVIDIA's 17 November results will show whether Rubin reached about 20% of data-center revenue, the next MLPerf rounds will show whether TPU 8, MI455X/Helios or Trainium3 appear at all, and AMD's warrant vesting, Cerebras's service credits and Broadcom's December report on late-2026 deliveries will show whether announced gigawatts have become delivered ones. The physical limits bind every company in the same places: HBM supply and pin speed, packaging reticle multiples and rack power for most of them, DUV lithography and a depleting stockpile of foreign memory for Huawei, and fixed on-wafer SRAM for Cerebras. Because of these shared constraints, a shortfall at TSMC, at SK hynix or in grid interconnection would surface in several companies' 2027 schedules at once.
