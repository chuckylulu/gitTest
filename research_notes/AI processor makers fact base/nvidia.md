# NVIDIA — Data-center AI processor business: fact base as of 14 November 2026

Conventions used throughout. Every item carries a date (period covered or as-of date) and a provenance tag:
- **[CO]** company-stated (NVIDIA SEC filings, press releases, CFO commentary, earnings-call remarks, product pages, keynotes). SEC financial statements are audited (10-K) or reviewed (10-Q) but remain company-reported.
- **[IND: who]** independently verified or independently measured, naming the verifier.
- **[EST]** analyst or industry estimate (named where possible).
- **[PRESS-ANON]** press report relying on unnamed sources.
- **[PRESS]** press or secondary-source report (named sourcing, or a secondary summary of company statements).
- **[DERIVED]** my own arithmetic from cited figures; not a company figure.

Research-process note: the shared web-search budget for this session ran out partway through. After that, I only fetched known URLs (SEC EDGAR filings, NVIDIA pages, MLCommons, Wikipedia, and pages already found in earlier searches). Several topics therefore rest on fewer sources than intended; these are listed under "Gaps" and in the final section. No figures were invented. Where only memory suggested a fact, it is either left out or explicitly labeled unverified.

Headline status as of 14 Nov 2026 (detailed below):
- Jensen Huang **resigned** as President, CEO and director on **11 Nov 2026** (announced 12 Nov 2026). CFO Colette Kress is interim CEO (and still CFO), and Harvey C. Jones is the first-ever Board Chair. [CO] [8-K, 12 Nov 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000082/nvda-20261111.htm)
- **Q3 FY2027 results are NOT out.** NVIDIA has scheduled them for **Tuesday 17 Nov 2026**, around 1:20 p.m. PT, with the call at 2 p.m. PT. This is not 19 Nov. [CO] [NVIDIA, "NVIDIA Announces CEO Transition," 12 Nov 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000082/nvidiaannouncesceotransiti.htm); [NVIDIA, "NVIDIA Sets Conference Call for Third-Quarter Financial Results," 28 Oct 2026](https://nvidianews.nvidia.com/news/nvidia-sets-conference-call-for-third-quarter-financial-results-6928873)
- **Vera Rubin production shipments began in August 2026** (fiscal Q3 FY2027), according to NVIDIA. [CO] [Q2 FY27 earnings call transcript, 26 Aug 2026](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf)

---

## 1. Products and stage (what NVIDIA ships for AI data centers, and at what stage)

### Takeaway
As of 14 Nov 2026, Blackwell and Blackwell Ultra (GB200/GB300 NVL72, B200/B300) are the volume products and still the "vast majority" of revenue. Vera Rubin NVL72 entered production shipments in August 2026, and NVIDIA expected it to be about 20% of Q3 FY27 data-center revenue. The Vera CPU and the Groq-derived Groq 3 LPX are described as "in full production," with first shipments under way or expected in Aug–Oct 2026. Rubin Ultra (Kyber NVL144, formerly called "NVL576") is a 2027 roadmap item and Feynman a 2028 item. Rubin CPX's status is unclear. Hopper persists mainly as H200, with China licenses that have yielded little revenue.

### Cited Findings
**Hopper (H100 / H200 / H20)**
- H100 and H200 remain in use and benchmarked. H200-SXM5, H200-NVL, GH200 and H100 systems appear in MLPerf Training v6.0 submissions from Cisco, Krai, Dell and Fujitsu (2026 round). [IND: MLCommons results] [MLCommons, MLPerf Training v6.0 results sheet](https://docs.google.com/spreadsheets/d/17Mek7pd_bKzfoA_ZiPt4E0jMcCZVE_dYbmsS8SUsJhw/edit) (linked from [mlcommons.org/benchmarks/training](https://mlcommons.org/benchmarks/training/))
- H20 (China-specific): in April 2025 the U.S. government required a license to export H20 to China. NVIDIA took a $4.5B charge in Q1 FY26 for H20 excess inventory and purchase obligations. In August 2025 licenses were granted, but only "approximately $60 million in H20 revenue" was generated under them. [CO] [NVIDIA FY2026 10-K, filed 25 Feb 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)
- In August 2025, NVIDIA reportedly told suppliers (TSMC, Samsung, Amkor) to halt H20 production after Chinese directives warned firms against buying it. [PRESS] Reuters, as cited in [Wikipedia, "Nvidia" (accessed 14 Nov 2026)](https://en.wikipedia.org/wiki/Nvidia)
- H200 for China: "Beginning in February 2026, the USG granted licenses that would allow us to ship small amounts of H200 products to specific China-based customers, but such sales were restricted by the PRC government." NVIDIA took a $0.4B H200 charge in H1 FY27. Shipments made under the program were "less than 1% of Data Center revenue" in Q2 FY27 (quarter ended 26 Jul 2026). [CO] [NVIDIA Q2 FY27 10-Q, filed 26 Aug 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)

**Blackwell (B200, GB200 NVL72)**
- "We began shipping production systems of the Blackwell architecture in the fourth quarter of fiscal year 2025" (Nov 2024–Jan 2025). Blackwell revenue in Q4 FY25 was $11.0B, "the fastest product ramp in our company's history." [CO] [NVIDIA FY2025 10-K, filed 26 Feb 2025](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/nvda-20250126.htm); [Q4 FY25 CFO commentary, 26 Feb 2025](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000021/q4fy25cfocommentary.htm)
- "Our Blackwell architectures represented the majority of our Data Center revenue" in FY2026 (Feb 2025–Jan 2026). [CO] [FY2026 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)
- Package design: GB100 die about 104B transistors; dual-die B100/B200 package about 208B transistors. [CO via PRESS] NVIDIA/AnandTech as cited in [Wikipedia, "Blackwell (microarchitecture)"](https://en.wikipedia.org/wiki/Blackwell_(microarchitecture))

**Blackwell Ultra (B300, GB300 NVL72)**
- "We began shipping production units of our new Blackwell Ultra platforms including GB300 in the second quarter of fiscal year 2026" (May–Jul 2025). [CO] [FY2026 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)
- Q2 FY27 (quarter to 26 Jul 2026): data-center growth was "driven by the ramp of our Blackwell Ultra infrastructure," and "our Blackwell architecture remains the vast majority of our revenue." [CO] [Q2 FY27 CFO commentary, 26 Aug 2026](https://s201.q4cdn.com/141608511/files/doc_financials/2027/Q227/Q2FY27-CFO-Commentary.pdf)
- GB300 NVL72 product page (accessed 14 Nov 2026):
  - System: 72 Blackwell Ultra GPUs and 36 Grace CPUs.
  - Memory: 20 TB GPU memory, up to 576 TB/s GPU memory bandwidth.
  - Interconnect: 130 TB/s NVLink.
  - Compute: FP4 1,440 PF sparse and about 1,080 PF dense.
  - No rack power figure is given.
  [CO] [NVIDIA GB300 NVL72 page](https://www.nvidia.com/en-us/data-center/gb300-nvl72/)

**Vera Rubin (Rubin GPU; "VR200" in analyst shorthand; Vera Rubin NVL72)**
- CES, 5 Jan 2026: "NVIDIA Rubin is in full production, and Rubin-based products will be available from partners the second half of 2026." The platform comprises six chips: Vera CPU, Rubin GPU, NVLink 6 Switch, ConnectX-9, BlueField-4 and Spectrum-6. [CO] [NVIDIA newsroom, "Rubin platform" release, 5 Jan 2026](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer)
- About 31 May 2026 (Computex period), NVIDIA said Vera Rubin was "ramping into full production." On 21 Jul 2026 it said NVL72 racks were "already running" at CoreWeave, Google Cloud, Microsoft Azure and OCI. [PRESS summary of CO statements] [Startup Fortune, "Nvidia Confirms Vera Rubin Is Shipping but Not the $630 Billion Number," 22 Jul 2026](https://startupfortune.com/nvidia-confirms-vera-rubin-is-shipping-but-not-the-630-billion-number/)
- 26 Aug 2026: "We commenced production shipments of Vera Rubin earlier this month." NVIDIA said it had received purchase orders "from every major hyperscaler, AI cloud, and system OEM." On the same call: "We see Vera Rubin accounting for about 20% of data center revenue in Q3." [CO] [Q2 FY27 call transcript, 26 Aug 2026](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf)
- 10-Q, filed 26 Aug 2026: "Vera Rubin, began production shipments in the third quarter of fiscal year 2027" (that quarter started 27 Jul 2026). Inventory rose to $31.6B "as we prepare for the introduction of Vera Rubin in the third quarter." [CO] [Q2 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm); [Q2 FY27 CFO commentary](https://s201.q4cdn.com/141608511/files/doc_financials/2027/Q227/Q2FY27-CFO-Commentary.pdf)
- Wikipedia's Rubin article says Rubin "entered deployment in September," citing an NVIDIA blog dated 30 Sep 2026. [PRESS] [Wikipedia, "Rubin (microarchitecture)"](https://en.wikipedia.org/wiki/Rubin_(microarchitecture))
- Current specs on NVIDIA's NVL72 product page (accessed 14 Nov 2026):

  | Spec | Per Rubin GPU | Per NVL72 rack |
  |---|---|---|
  | NVFP4 inference (sparse) | 50 PF | 3,600 PF |
  | NVFP4 training (dense) | 35 PF | 2,520 PF |
  | HBM4 capacity | 288 GB | 20.7 TB |
  | HBM4 bandwidth | 19.2 TB/s | 1,400 TB/s |
  | NVLink | 3 TB/s | 216 TB/s |
  | LPDDR5X (CPU memory) | — | up to 54 TB |

  - The page says "Available Now" and that Vera Rubin is "ramping into full production."
  - No rack power figure is given.
  [CO] [NVIDIA Vera Rubin NVL72 page](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)
- Earlier NVIDIA figures differed. The CES release (5 Jan 2026) gave NVLink 6 at 3.6 TB/s per GPU and 260 TB/s per rack. GTC 2026 recaps gave HBM4 at 22 TB/s and 336B transistors (see the cross-examination log). [CO] [CES release](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer); [PRESS] [thegpu.ai, "NVIDIA GTC 2026 full breakdown," Mar 2026](https://thegpu.ai/p/nvidia-gtc-2026-full-breakdown); [Tech Insider, "NVIDIA GTC 2026 Rubin GPU analysis," dated 16 Mar 2026, updated later](https://tech-insider.org/nvidia-gtc-2026-rubin-gpu-analysis/)
- Rack price estimates [EST]:
  - VR200 NVL72 about $7.8M, of which memory about $2M (Morgan Stanley via Tom's Hardware), as reported by [Startup Fortune, 22 Jul 2026](https://startupfortune.com/nvidia-confirms-vera-rubin-is-shipping-but-not-the-630-billion-number/).
  - VR200 NVL72 $5–7M for OEM customers; Rubin Ultra NVL144 ("VR300") $7–8.8M (Tom's Hardware, 24 Mar 2026), as reported by [network-switch.com, 30 Apr 2026](https://network-switch.com/blogs/news/what-comes-next-ai-hardware-outlook-april-2026). NVIDIA has not confirmed list prices.
- Volume estimate: Ming-Chi Kuo expected VR200 NVL72 rack mass production by end-Q3 2026, with about 5,000–7,000 racks shipped in H2 2026. [EST] [Startup Fortune, 22 Jul 2026](https://startupfortune.com/nvidia-confirms-vera-rubin-is-shipping-but-not-the-630-billion-number/)

**Rubin CPX (long-context prefill GPU)**
- Announced at NVIDIA's AI Infra Summit appearance (Sept 2025) as a prefill processor for end-2026. A GTC 2026 recap says it "appears to have been set aside" in favor of the Groq decode architecture. That is the author's inference, not an NVIDIA statement. [PRESS] [thegpu.ai, Mar 2026](https://thegpu.ai/p/nvidia-gtc-2026-full-breakdown)
- "CPX" does not appear in the Q2 FY27 call transcript (26 Aug 2026), nor in the data-center highlights of the Q4 FY26, Q1 FY27 or Q2 FY27 releases. [CO, absence noted] [Q2 FY27 PR](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27pr.htm)

**Rubin Ultra / Vera Rubin Ultra (Kyber rack; NVL144, earlier "NVL576")**
- GTC 2025 framing: "an 800 V sidecar powering 576 Rubin Ultra GPUs in a single Kyber rack," with 800 VDC to coincide with Kyber in 2027. [CO] [NVIDIA Technical Blog, "NVIDIA 800 V HVDC Architecture Will Power the Next Generation of AI Factories," 20 May 2025 (updated 31 Jul 2025)](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/)
- GTC 2026 (16 Mar 2026): a Kyber prototype was shown. It "will hold 144 GPUs in vertically oriented compute trays" and "will debut in Vera Rubin Ultra, expected to ship in 2027." [CO via PRESS] [CNBC, 16 Mar 2026](https://www.cnbc.com/2026/03/16/nvidia-gtc-2026-ceo-jensen-huang-keynote-blackwell-vera-rubin.html)
- As of late March 2026, Rubin Ultra was "not yet in silicon production." [PRESS] [network-switch.com, 30 Apr 2026](https://network-switch.com/blogs/news/what-comes-next-ai-hardware-outlook-april-2026)

**Feynman (2028)**
- GTC 2026 preview items, reported by Jon Peddie Research (17 Mar 2026) and thegpu.ai: TSMC A16, 3D die stacking, custom HBM, a new "Rosa" CPU, an "LP40" LPU built with the Groq team, BlueField-5, ConnectX-10, Kyber scaling to "NVL1152," and Intel EMIB packaging for the I/O die. JPR flags some of these details as speculative. [CO via PRESS] [Jon Peddie Research, "Nvidia GTC 2026 keynote," 17 Mar 2026](https://www.jonpeddie.com/news/nvidia-gtc-2026-keynote/); [thegpu.ai](https://thegpu.ai/p/nvidia-gtc-2026-full-breakdown)

**CPUs: Grace and Vera**
- Grace CPU revenue on a trailing-12-month basis is "exceeding $5 billion" (26 Aug 2026). [CO] [Q2 FY27 call](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf)
- Vera on the same call:
  - "Today, we are in full production of our next-generation Vera CPU."
  - Shipments are "already underway to our lead partners, including OCI, SpaceXAI, and starting this quarter, AWS."
  - NVIDIA's "preliminary expectation is for CPU revenue to more than double in fiscal 2028."
  [CO] [Q2 FY27 call](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf)
- Vera specs: 88 custom Olympus cores (Armv9.2), up to 1.5 TB LPDDR5X, 1.8 TB/s NVLink-C2C. [CO] [CES release, 5 Jan 2026](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer); [Vera Rubin NVL72 page](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)
- Meta is running Grace-only CPU deployments ("first large-scale Grace-only deployment"). Vera is under collaboration, with "potential" large-scale deployment in 2027. [CO] [NVIDIA, "Meta Builds AI Infrastructure With NVIDIA," 17 Feb 2026](https://nvidianews.nvidia.com/news/meta-builds-ai-infrastructure-with-nvidia)

**NVLink and NVLink Fusion**
- Q1 FY27 (Feb–Apr 2026): strategic partnership with Marvell via NVLink Fusion. [CO] [Q1 FY27 PR, 20 May 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000051/q1fy27pr.htm)
- 8–9 Nov 2026: collaboration with Rebellions and SK Telecom on sovereign AI infrastructure using NVLink Fusion. [CO] [NVIDIA newsroom RSS, 9 Nov 2026](https://nvidianews.nvidia.com/news/nvidia-rebellions-and-sk-telecom-announce-collaboration-to-advance-sovereign-ai-infrastructure-with-nvidia-nvlink-fusion)

**Networking: Spectrum-X, Quantum and co-packaged optics (CPO)**
- Spectrum-6 is described as built on 200G SerDes with co-packaged optics. NVIDIA claims 5x power efficiency and 5x longer uptime (CES); GTC recaps quote 10x resiliency. [CO] [CES release](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer); [thegpu.ai](https://thegpu.ai/p/nvidia-gtc-2026-full-breakdown)
- Q2 FY27 release: Spectrum-6 switch systems "supporting both pluggable and co-packaged optics … are arriving across the world's gigascale AI factories." [CO] [Q2 FY27 PR, 26 Aug 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27pr.htm)
- Networking revenue grew 18% sequentially in Q2 FY27. "Spectrum-X Ethernet … grew 2.6x on a year-over-year basis." [CO] [Q2 FY27 call](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf)
- Q1 FY27: NVIDIA signed multi-year strategic agreements with Coherent, Corning and Lumentum on optics. [CO] [Q1 FY27 PR](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000051/q1fy27pr.htm)

**Products from the December 2025 Groq deal**
- GTC, 16 Mar 2026:
  - Groq 3 LPU: 1.2 PFLOPS FP8, 500 MB SRAM at 150 TB/s.
  - Groq 3 LPX rack: 256 LPUs, said to sit beside Vera Rubin racks. Shipping was stated for Q3 2026.
  - Claimed "up to 35x" tokens/s per MW when paired with Vera Rubin.
  - Ian Buck: the LPU "does not yet support CUDA natively."
  [CO via PRESS] [CNBC, 16 Mar 2026](https://www.cnbc.com/2026/03/16/nvidia-gtc-2026-ceo-jensen-huang-keynote-blackwell-vera-rubin.html); [thegpu.ai](https://thegpu.ai/p/nvidia-gtc-2026-full-breakdown)
- 26 Aug 2026: "At Hot Chips earlier this week, we announced that Groq 3 LPX … is in full production … We expect to ship Groq 3 LPX in volume later this quarter to early adopters, Nebius will be the first." [CO] [Q2 FY27 call](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf)

**Other platform items**
- DSX AI-factory platform launched (Q2 FY27). [CO] [Q2 FY27 PR](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27pr.htm)
- DGX Rubin NVL8 spec table: about 24 kW system power, 400 PF NVFP4 inference (sparse). [CO via PRESS] [Tech Insider](https://tech-insider.org/nvidia-gtc-2026-rubin-gpu-analysis/)

### Inferences
- "Full production" has been used for three different stages:
  - Rubin silicon in January 2026.
  - Rubin "ramping into full production" from May to August 2026.
  - Groq 3 LPX in August 2026, with volume shipments still pending.

  For dating volume, NVIDIA's own "production shipments" wording is the most precise. It puts the start in August 2026.
- Rubin's first revenue quantification will come in the Q3 FY27 report on 17 Nov 2026 (guided at about 20% of Q3 data-center revenue). As of 14 Nov 2026 there is no reported Rubin revenue figure.

### Gaps
- No GB200 or GB300 NVL72 rack power figure on NVIDIA's pages; the commonly cited ~120–132 kW could not be sourced in this session. No Vera Rubin NVL72 rack power figure was found.
- I could not verify secondary claims that OCI announced general availability of Vera Rubin NVL72 on 27 Oct 2026, or that CoreWeave's customer deployment began on 30 Sep 2026. They appeared only in a search-engine summary of aggregator sites.
- No NVIDIA statement confirming cancellation or continuation of Rubin CPX was found.
- No confirmation was found that Groq 3 LPX volume shipments to Nebius happened by the end of Q3 FY27 (25 Oct 2026).
- No dated ship status was found for the Quantum-X Photonics CPO InfiniBand switch.

---

## 2. Roadmap commitments and milestones (met / slipped / pending)

### Takeaway
NVIDIA's annual-cadence promises have been broadly met at the platform level. Blackwell Ultra arrived in H2 2025, and Rubin production shipments began in August 2026, inside the "2026" and "H2 2026" commitments. The two clear blemishes are both documented:
- The 2024 Blackwell mask change for yield, which pushed the production ramp to Nov 2024–Jan 2025.
- The use of "full production" in January 2026 for a product that began production shipments seven months later.

Rubin specifications on NVIDIA's product page were revised downward by September 2026. Rubin Ultra/Kyber (2027), 800 VDC (2027) and Feynman (2028) are pending. I could not source the late-2024/early-2025 GB200 NVL72 rack problems in this session.

### Cited Findings
Roadmap tracker:

| Date and venue of commitment | Commitment | Status as of 14 Nov 2026 | Source |
|---|---|---|---|
| GTC, 18 Mar 2024 | Blackwell B100/B200/GB200 NVL72 announced | **Slipped, then met.** Customer samples shipped in Q2 FY25. "We executed a change to the Blackwell GPU mask to improve production yield. Blackwell production ramp is scheduled to begin in the fourth quarter" (10-Q, 28 Aug 2024). Q2 FY25 gross margin was hit by "inventory provisions for low-yielding Blackwell material" ($908M of provisions). Huang (Oct 2024): the flaw was "functional" and "caused the yield[s] to be low." Production systems shipped in Q4 FY25; Q4 FY25 Blackwell revenue was $11.0B against August 2024 guidance of "several billion dollars." | [CO] [Q2 FY25 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581024000264/nvda-20240728.htm); [PRESS] Reuters (23 Oct 2024) via [Wikipedia "Blackwell"](https://en.wikipedia.org/wiki/Blackwell_(microarchitecture)); [CO] [Q4 FY25 CFO commentary](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000021/q4fy25cfocommentary.htm) |
| Late 2024 / early 2025 | GB200 NVL72 rack ramp (overheating, liquid-cooling and interconnect issues reported by The Information and Reuters) | **Not verified in this session.** Reuters was unreachable. A Jan 2026 article recalls "a design flaw that caused overheating in server racks" but conflates it with the yield issue (see cross-examination). | [PRESS] [The Decoder, 6 Jan 2026](https://the-decoder.com/ces-2026-nvidia-promises-five-times-the-ai-performance-and-ten-times-cheaper-inference-with-vera-rubin/) |
| Computex, Jun 2024 | Rubin for 2026 | **Met.** Production shipments began Aug 2026. | [PRESS] [Wikipedia "Rubin"](https://en.wikipedia.org/wiki/Rubin_(microarchitecture)); [CO] [Q2 FY27 call](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf) |
| GTC, Mar 2025 | Blackwell Ultra H2 2025 | **Met.** GB300 production units shipped in Q2 FY26 (May–Jul 2025). | [CO] [FY26 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm) |
| GTC, Mar 2025 | Rubin Ultra in Kyber, 576 GPUs per rack (die count), 2027; 800 VDC with Kyber in 2027; 1 MW racks from 2027 | **Pending.** The name changed to 144 GPUs (package count) at GTC 2026. Target is still 2027 per CNBC (Mar 2026). Not yet in silicon production as of late Mar 2026. | [CO] [NVIDIA 800 V blog, 20 May 2025](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/); [CNBC, 16 Mar 2026](https://www.cnbc.com/2026/03/16/nvidia-gtc-2026-ceo-jensen-huang-keynote-blackwell-vera-rubin.html); [network-switch.com, 30 Apr 2026](https://network-switch.com/blogs/news/what-comes-next-ai-hardware-outlook-april-2026) |
| GTC, Mar 2025 | Feynman 2028 | **Pending.** Previewed again at GTC 2026. | [Wikipedia "Rubin"](https://en.wikipedia.org/wiki/Rubin_(microarchitecture)); [JPR, 17 Mar 2026](https://www.jonpeddie.com/news/nvidia-gtc-2026-keynote/) |
| AI Infra Summit, Sept 2025 | Rubin CPX for end-2026 | **Unclear / possibly set aside** (third-party inference). | [thegpu.ai](https://thegpu.ai/p/nvidia-gtc-2026-full-breakdown) |
| OpenAI LOI, 22 Sep 2025 | "The first gigawatt of NVIDIA systems will be deployed in the second half of 2026 on the NVIDIA Vera Rubin platform" | **Unverified / pending.** No confirmation found. The PORTS-Pike site that now anchors the relationship comes online "in phases beginning in 2028." | [CO] [NVIDIA–OpenAI LOI release, 22 Sep 2025](https://nvidianews.nvidia.com/news/openai-and-nvidia-announce-strategic-partnership-to-deploy-10gw-of-nvidia-systems); [CO] [SB Energy release, 17 Aug 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/sbeoainvidia-portsrelease.htm) |
| GTC DC, 28 Oct 2025 | "We're preparing Rubin to be in production this time next year, maybe slightly earlier." | **Met** (Aug 2026). | [PRESS] [Next Platform, 29 Oct 2025](https://www.nextplatform.com/ai/2025/10/29/as-rackscale-gpu-systems-boom-big-green-is-emphatically-red-white-and-blue/1640768) |
| CES, 5 Jan 2026 | "Rubin is in full production"; partner availability H2 2026 | **Availability met** (racks running at CSPs by 21 Jul 2026; production shipments Aug 2026). **The "full production" wording was contradicted** by NVIDIA's later "ramping into full production" (May–Aug 2026). | [CO] [CES release](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer); [Startup Fortune, 22 Jul 2026](https://startupfortune.com/nvidia-confirms-vera-rubin-is-shipping-but-not-the-630-billion-number/) |
| GTC, 16 Mar 2026 | Groq 3 LPX ships Q3 2026 | **Partly met.** "Full production" was announced at Hot Chips (Aug 2026); volume shipments were expected "later this quarter" (by 25 Oct 2026), with Nebius first. Not yet confirmed. | [CO] [Q2 FY27 call](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf) |
| GTC, 16 Mar 2026 | Vera Rubin Ultra (Kyber NVL144) in 2027; Feynman in 2028 with Rosa CPU and LP40 | **Pending.** | [CNBC](https://www.cnbc.com/2026/03/16/nvidia-gtc-2026-ceo-jensen-huang-keynote-blackwell-vera-rubin.html); [JPR](https://www.jonpeddie.com/news/nvidia-gtc-2026-keynote/) |
| Computex, ~31 May 2026 | Vera Rubin "ramping into full production" | Production shipments began Aug 2026. | [Startup Fortune](https://startupfortune.com/nvidia-confirms-vera-rubin-is-shipping-but-not-the-630-billion-number/) |

- Rubin spec changes, documented:
  - **Naming:** Rubin Ultra was "576 … GPUs in a single Kyber rack" (May 2025 framing, counting dies) and became "144 GPUs" in Kyber (Mar 2026, counting packages). Next Platform noted in Oct 2025 that Huang counts "GPU chiplets per socket under his own naming scheme for 2026 and beyond." [CO/PRESS] [NVIDIA 800 V blog](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/); [CNBC](https://www.cnbc.com/2026/03/16/nvidia-gtc-2026-ceo-jensen-huang-keynote-blackwell-vera-rubin.html); [Next Platform](https://www.nextplatform.com/ai/2025/10/29/as-rackscale-gpu-systems-boom-big-green-is-emphatically-red-white-and-blue/1640768)
  - **Bandwidth:** HBM4 per GPU was 22 TB/s (GTC 2026 recaps) and is 19.2 TB/s on the current product page. NVLink per GPU went from 3.6 TB/s and 260 TB/s per rack (CES 2026) to 3 TB/s and 216 TB/s (current page). The bandwidth change was dated "early September 2026" by a third party (Understanding Machine), as cited by Tech Insider. [CO] [Vera Rubin NVL72 page](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/); [PRESS] [Tech Insider](https://tech-insider.org/nvidia-gtc-2026-rubin-gpu-analysis/)
- Reported Rubin ramp issues:
  - KeyBanc's John Vinh flagged "thermal lid issues"; Barron's reported the problem was resolved and the ramp would begin in July 2026.
  - SemiAnalysis pointed to manufacturing difficulty with advanced rack components.
  [EST/PRESS] [Startup Fortune, 22 Jul 2026](https://startupfortune.com/nvidia-confirms-vera-rubin-is-shipping-but-not-the-630-billion-number/)
- Before CES 2026, "Wall Street had been buzzing with rumors of Rubin GPU delays." [PRESS] [The Decoder citing Wired, 6 Jan 2026](https://the-decoder.com/ces-2026-nvidia-promises-five-times-the-ai-performance-and-ten-times-cheaper-inference-with-vera-rubin/)
- TrendForce forecast (18 Mar 2026): HBM4 supply from Q2 2026, chip shipments around Q3 2026, and VR200 racks ramping late in that quarter. [EST] via [Tech Insider](https://tech-insider.org/nvidia-gtc-2026-rubin-gpu-analysis/)
- Earlier, TrendForce (29 Oct 2025) put Rubin mass production in Q3 or Q4 2026. [EST] [TrendForce, 29 Oct 2025](https://www.trendforce.com/news/2025/10/29/news-nvidia-dismisses-ai-bubble-concerns-reportedly-projects-500b-in-gpu-sales-from-blackwell-and-rubin/)

### Inferences
- NVIDIA's own statements about when Rubin would be "in production" moved forward by about nine months between Oct 2025 ("this time next year, maybe slightly earlier") and Jan 2026 ("in full production"). Actual production shipments (Aug 2026) landed close to the Oct 2025 framing. This suggests the CES statement described wafer and early production status, not volume system shipments.
- The downward revision of headline HBM4 and NVLink bandwidth on the product page is consistent with either a binning or spec choice for volume parts, or with HBM4 pin-speed limits. NVIDIA has not given a reason (see Science section for the arithmetic).

### Gaps
- Contemporaneous primary sources on the GB200 NVL72 rack problems of late 2024–early 2025 (overheating reports, order changes by hyperscalers) were unavailable: Reuters could not be fetched and the search budget was exhausted.
- I did not find NVIDIA's exact GTC 2024 wording for Blackwell's original availability date, so the slip cannot be measured precisely.
- The exact GTC 2025 Vera Rubin "NVL144" naming and specs (e.g., the original HBM4 bandwidth target) could not be re-fetched.
- I found no NVIDIA statement explaining the September 2026 change from 22 to 19.2 TB/s.
- I found no source confirming or denying a Rubin Ultra delay beyond the 2027 target.
- Computex 2025 (NVLink Fusion launch) and Computex 2026 materials could not be retrieved directly.

---

## 3. Financials (FY2025, FY2026, Q1–Q2 FY2027; Q3 status; guidance; China; customer concentration)

### Takeaway
Revenue went from $130.5B (FY25) to $215.9B (FY26). Two FY27 quarters have been reported: $81.6B (Q1) and $96.2B (Q2). Data Center was $89.0B in Q2 FY27 (about 93% of revenue). Gross margins recovered to about 75% after the H20 charge depressed FY26 to 71.1% GAAP.

The balance sheet changed character in 2026:
- $25B of new notes issued in June 2026.
- Supply commitments rose to $279B, primarily memory.
- $99B of equity investments and $25B of further commitments.
- New AI-cloud capacity agreements of $36B.
- Credit-support guarantees with maximum exposure of $108.5B, mostly the SB Energy/OpenAI site.

Q3 FY27 (quarter ended 25 Oct 2026) results are scheduled for 17 Nov 2026 and were not out on 14 Nov 2026. Guidance is $108.0B ±2%, with gross margin of 74.0% falling to a 71–72% trough in Q4 because of memory costs.

### Cited Findings
**Q3 FY2027 status**
- Quarter ended 25 Oct 2026. Results scheduled for Tue 17 Nov 2026 at about 1:20 p.m. PT. The date was reaffirmed in the 12 Nov 2026 CEO-transition release. **Not released as of 14 Nov 2026.** [CO] [NVIDIA, 28 Oct 2026](https://nvidianews.nvidia.com/news/nvidia-sets-conference-call-for-third-quarter-financial-results-6928873); [CEO-transition release, 12 Nov 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000082/nvidiaannouncesceotransiti.htm)

**Summary table [CO]** (US$ millions unless noted; GAAP unless noted)

| Item | FY2025 (to 26 Jan 2025) | FY2026 (to 25 Jan 2026) | Q4 FY26 (to 25 Jan 2026) | Q1 FY27 (to 26 Apr 2026) | Q2 FY27 (to 26 Jul 2026) |
|---|---|---|---|---|---|
| Revenue | 130,497 | 215,938 | 68,127 | 81,615 | 96,221 |
| Data Center revenue | 115,186 | 193,737 | 62,314 | 75,215 (recast to 75,246 in Aug) | 89,023 |
| DC compute / networking | Q4 FY25: 32.6B / 3.0B; FY: compute +162%, networking +51% y/y | FY: compute +59%, networking +142% y/y | 51.3B / 11.0B | 60.4B / 14.8B | Not disclosed (new Hyperscale/ACIE split; networking +18% q/q) |
| Hyperscale / ACIE | — | — | — | 37,869 originally; recast 43,050 / remainder ACIE | 48,710 / 40,313 |
| Gross margin GAAP / non-GAAP | 75.0% / 75.5% | 71.1% / 71.3% | 75.0% / 75.2% | 74.9% / 75.0% | 75.0% / 75.0% |
| Operating income (GAAP) | 81,453 | 130,387 | 44,299 (non-GAAP 46,107) | 53,536 (non-GAAP 53,783) | 63,734 (non-GAAP 63,956) |
| Net income (GAAP) | 72,880 | 120,067 | 42,960 (non-GAAP 39,552) | 58,321 (non-GAAP 45,548) | 59,688 (non-GAAP 53,954) |
| Diluted EPS GAAP / non-GAAP | 2.94 / — | 4.90 / 4.77 | 1.76 / 1.62 (restated 1.59 incl. SBC) | 2.39 / 1.87 | 2.46 / 2.22 |
| Gains on equity securities | — | — | 5,491 | 15,936 | 7,771 |
| Cash + marketable (debt) securities | 43,210 | 62,556 | — | 50,335 (cash 13,237 + mkt debt 37,098); mkt equity 30,237; non-mkt 43,364 | 56,586 (cash 22,443 + mkt debt 34,143); mkt equity 42,783; non-mkt 51,157 |
| Debt (ST / LT) | — / 8,463 | 999 / 7,469 | — | 1,000 / 7,470 | 1,000 / 32,366 |
| Inventory | 10,080 | 21,403 | 21,403 | 25,797 | 31,575 |
| Supply / capacity commitments | 30.8B (+14.3B other incl. cloud) | 95.2B | 95.2B | 119B | 279B ("primarily … memory") |
| Multi-year cloud service agreements | 10.9B | 27.0B | 27.0B | 30.0B | 29B, plus 36B "AI cloud agreements" |
| Buybacks / returns | 310M shares for $34.0B (10-K); $33.7B repurchases + $834M dividends (CFO) | 282M shares for $40.4B; $41.1B returned incl. $974M dividends; $58.5B authorization left | $3.8B buybacks + $243M dividends | ~$20.0B returned; $38.5B left plus $80B new authorization (18 May 2026); dividend raised to $0.25/qtr | ~$26.0B returned (~$19.7B buybacks + ~$6.0B dividends); ~$99.0B authorization left |

Sources for the table:
- FY25: [FY25 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000023/nvda-20250126.htm); [Q4 FY25 CFO commentary, 26 Feb 2025](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000021/q4fy25cfocommentary.htm)
- FY26 and Q4 FY26: [Q4 FY26 release, 25 Feb 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000019/q4fy26pr.htm); [Q4 FY26 CFO commentary](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000019/q4fy26cfocommentary.htm); [FY26 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)
- Q1 FY27: [Q1 FY27 release, 20 May 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000051/q1fy27pr.htm); [Q1 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000052/nvda-20260426.htm); [Q1 FY27 CFO commentary](https://s201.q4cdn.com/141608511/files/doc_financials/2027/Q127/Q1FY27-CFO-Commentary.pdf)
- Q2 FY27: [Q2 FY27 release, 26 Aug 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27pr.htm); [Q2 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm); [Q2 FY27 CFO commentary](https://s201.q4cdn.com/141608511/files/doc_financials/2027/Q227/Q2FY27-CFO-Commentary.pdf)

**Notes on the figures**
- Non-GAAP basis changed in Q1 FY27: it now includes stock-based compensation, and prior periods were restated. Q4 FY26 non-GAAP EPS was shown as $1.59 in the Q1 FY27 release versus $1.62 originally. [CO] [Q1 FY27 release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000051/q1fy27pr.htm)
- New reporting framework from Q1 FY27: "Data Center" (split into Hyperscale and ACIE) and "Edge Computing." [CO] [Q1 FY27 CFO commentary](https://s201.q4cdn.com/141608511/files/doc_financials/2027/Q127/Q1FY27-CFO-Commentary.pdf)
- In Q2, "we reclassified a company from AI Clouds, Industrial, & Enterprise (ACIE) to Hyperscale due to a change in their business model and recast the prior period revenue." [CO] [Q2 FY27 CFO commentary](https://s201.q4cdn.com/141608511/files/doc_financials/2027/Q227/Q2FY27-CFO-Commentary.pdf)
- Q2 FY27 other balance-sheet items:
  - Accounts receivable $63.1B; DSO 60 days, up from 45, "due to extended payment terms on large, multi-quarter agreements with certain investment-grade customers."
  - Operating cash flow $24.1B; free cash flow $21.3B.
  - Total assets $320.3B.
  [CO] [Q2 FY27 CFO commentary](https://s201.q4cdn.com/141608511/files/doc_financials/2027/Q227/Q2FY27-CFO-Commentary.pdf); [Q2 FY27 release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27pr.htm)
- Notes issued 18 Jun 2026, totaling **$25.0B**:
  - 4.250% due 2028: $3.5B
  - 4.350% due 2029: $3.5B
  - 4.500% due 2031: $4.0B
  - 4.750% due 2033: $3.5B
  - 4.950% due 2036: $4.0B
  - 5.550% due 2046: $3.0B
  - 5.625% due 2056: $3.5B
  
  Underwriters were led by Goldman Sachs, J.P. Morgan and Morgan Stanley. The commercial-paper program was raised to $25.0B in Jan 2026, with nothing outstanding. [CO] [8-K, 18 Jun 2026](https://www.sec.gov/Archives/edgar/data/1045810/000119312526275783/d48176d8k.htm); [FY26 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)
- Full commitment table as of 26 Jul 2026, totaling $366B:
  - Supply and capacity: $279B.
  - Cloud service agreements: $29B.
  - Data-center leases not yet commenced: $25B.
  - Equity investments: $25B.
  - Capex: $8B.

  Additional commitments: AI cloud agreements $36B ("typically six years," and the AI clouds "can unilaterally stop providing to us and sell to third-party customers") and data-center leases for third parties $20B.

  Guarantees: maximum gross exposure of $3.5B for land, power and shell guarantees to AI clouds, plus $105.0B for SB Energy, for a total of $108.5B.

  "Equity investments of $99 billion and equity investment commitments of $25 billion as of July 26, 2026." [CO] [Q2 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- Earlier investment figures: in FY26 NVIDIA "invested $17.5 billion in private companies and infrastructure funds." Q1 FY27 investments were $18.6B, including "AI model makers that may indirectly purchase or use our products." [CO] [FY26 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm); [Q1 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000052/nvda-20260426.htm)

**Guidance and track record [CO]**
- Q1 FY27 guide (25 Feb 2026): $78.0B ±2%. Actual: $81.6B.
- Q2 FY27 guide (20 May 2026): $91.0B ±2%. Actual: $96.2B.
- Q3 FY27 guide (26 Aug 2026):
  - Revenue $108.0B ±2%, assuming no data-center compute revenue from China.
  - Gross margin 74.0% ±50 bp (GAAP and non-GAAP).
  - Opex about $9.2B GAAP and $9.0B non-GAAP.
  - Full-year FY27 tax rate 16–18%.
  - Full-year FY27 opex growth "in the low-50s."
- Further remarks on the 26 Aug 2026 call:
  - "We expect margins to bottom in Q4 in the 71% to 72% range before settling at 72% to 73% in fiscal year 2028 as executed price increases take effect in Q1."
  - "Preliminary expectation is for fiscal year 2028 revenue to grow approximately 70% … supply-constrained."
  - "We expect supply to remain a bottleneck at least through the end of fiscal year 2028."

Sources: [Q4 FY26 release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000019/q4fy26pr.htm); [Q1 FY27 release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000051/q1fy27pr.htm); [Q2 FY27 release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27pr.htm); [Q2 FY27 call](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf)

**China revenue (by customer headquarters, including Hong Kong) [CO]**

| Period | China incl. HK revenue |
|---|---|
| FY24 | $12,330M |
| FY25 | $25,048M |
| FY26 | $19,677M |
| Q1 FY27 | $4,550M (vs $9,659M a year earlier) |
| Q2 FY27 | $7,880M (vs $3,985M a year earlier) |
| H1 FY27 | $12,430M |

- Q1 FY27: "No shipments of Data Center Hopper products to China occurred during the quarter."
- Q2 FY27: Hopper data-center shipments to China were less than 1% of Data Center revenue.
- In FY26, NVIDIA estimates that 76% of Data Center revenue from Taiwan-headquartered customers was attributed to end customers in the US and Europe.

Sources: [FY26 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm); [Q1 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000052/nvda-20260426.htm); [Q2 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm); [Q1 FY27 CFO commentary](https://s201.q4cdn.com/141608511/files/doc_financials/2027/Q127/Q1FY27-CFO-Commentary.pdf)

**Other geography [CO]**
- FY26: US $149,617M; Taiwan $42,345M; Other $4,299M.
- Q2 FY27: US $60,074M; Taiwan $26,985M. Non-US customers were 38% of Q2 revenue.

**Customer concentration (direct customers ≥10%, all primarily Compute & Networking) [CO]**

| Period | Direct customers at ≥10% of revenue |
|---|---|
| FY2024 | One at 13% |
| FY2025 | 12%, 11%, 11% |
| FY2026 | 22% and 14% |
| Q1 FY27 | 21%, 17%, 16% |
| Q2 FY27 | One at 16% |
| H1 FY27 | 16%, 15%, 13% |

- Accounts receivable on 26 Jul 2026: five direct customers held 22%, 14%, 13%, 11% and 10%.
- Indirect customers: "some individually representing 10% or more of our revenue." NVIDIA estimates "one AI research and deployment company contributed a meaningful amount of our revenue by purchasing cloud services from our customers" (FY26 and H1 FY27).

Sources: [FY26 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm); [Q1 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000052/nvda-20260426.htm); [Q2 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)

**Groq accounting [CO]**
- Groq license (Dec 2025): "$13.0 billion paid at closing and $4 billion, inclusive of imputed interest, payable within one year." NVIDIA recorded $14.4B of goodwill and a $2.5B developed-technology intangible asset.
- Q1 FY27: $3.96B of accrued purchase consideration related to the Groq license.
- H1 FY27: cash flow shows a $2,944M Groq payment.

Sources: [FY26 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm); [Q1 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000052/nvda-20260426.htm); [Q2 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)

### Inferences
- [DERIVED] Q2 FY27 networking revenue was not disclosed. If networking grew 18% q/q from Q1's $14.8B (per the call), it would be about $17.5B, implying about $71.5B of DC compute. This is an approximation, and the Q1 base was later recast.
- [DERIVED] Data Center was 92.5% of Q2 FY27 revenue (89,023 / 96,221).
- [DERIVED] China (incl. HK) revenue of $7.9B in Q2 FY27 coexists with "less than 1%" Hopper DC shipments to China. The China figure must therefore consist mostly of non-data-center products (e.g., gaming/RTX) and/or Chinese-headquartered customers whose products ship elsewhere. NVIDIA does not break this out.
- The direct-customer list is mostly ODMs, OEMs and distributors (NVIDIA's definition). The large Taiwan-HQ revenue ($27.0B in Q2 FY27) and the 76% US/Europe end-customer attribution suggest the ≥10% direct customers are largely Taiwanese ODMs building for US hyperscalers. NVIDIA does not name them.
- The unnamed "AI research and deployment company" buying through clouds is most plausibly OpenAI, but NVIDIA does not name it.

### Gaps
- Absolute full-year DC compute and networking splits for FY25 and FY26 were not found in the documents read (only growth rates and Q4 values).
- Non-GAAP operating income and net income for full FY25 and FY26 were not extracted.
- Prepaid supply agreements: amounts not found in the sections read.

---

## 4. Bookings and visibility claims ($500B, $1T, and later)

### Takeaway
At GTC Washington (28 Oct 2025), Huang claimed "visibility into half a trillion dollars of cumulative Blackwell and early ramps of Rubin through 2026." At GTC (16 Mar 2026), he said he expected "purchase orders between Blackwell and Vera Rubin to reach $1 trillion through 2027." On 26 Aug 2026, NVIDIA replaced dollar-backlog talk with a "supply-constrained" guide of about 70% FY28 revenue growth. Bernstein's analyst estimated that implied about $200B more than the prior "$1 trillion over the three years." Neither the $500B nor the $1T figure is a GAAP backlog or RPO disclosure, and neither has been independently audited.

### Cited Findings
- **28 Oct 2025, GTC Washington DC** [CO via PRESS] ([Next Platform, 29 Oct 2025](https://www.nextplatform.com/ai/2025/10/29/as-rackscale-gpu-systems-boom-big-green-is-emphatically-red-white-and-blue/1640768)):
  - Huang: "We now have visibility, and … visibility into half a trillion dollars of cumulative Blackwell and early ramps of Rubin through 2026."
  - He described the window as "the next five quarters" (the rest of 2025 plus four quarters of 2026).
  - "We've already shipped 6 million of the Blackwells in the first several quarters."
  - A chart showed about 4M Hopper GPUs versus about 20M Blackwell+Rubin GPUs "on the books."
  - Next Platform's caveat: counts are per GPU chiplet (two dies per Blackwell package), the chart appears to include NVL8 and 4-GPU systems, and "five times the dollars roughly equals five times the chiplets."
- **Feb 2026:** CFO Kress said after the February earnings that 2026 growth should exceed the $500B estimate. [CO via PRESS] [CNBC, 16 Mar 2026](https://www.cnbc.com/2026/03/16/nvidia-gtc-2026-ceo-jensen-huang-keynote-blackwell-vera-rubin.html)
- **16 Mar 2026, GTC San Jose:**
  - CNBC: Huang "expects purchase orders between Blackwell and Vera Rubin to reach $1 trillion through 2027." [CO via PRESS] [CNBC, 16 Mar 2026](https://www.cnbc.com/2026/03/16/nvidia-gtc-2026-ceo-jensen-huang-keynote-blackwell-vera-rubin.html)
  - JPR: a pipeline that "now targets $1 trillion through 2027," which it calls "double" the $500B. [PRESS] [JPR, 17 Mar 2026](https://www.jonpeddie.com/news/nvidia-gtc-2026-keynote/)
  - A secondary summary of WSJ coverage framed it as "sell $1 trillion worth … by the end of 2027." Wording varies across outlets between orders, sales and backlog. [PRESS] [thegpu.ai](https://thegpu.ai/p/nvidia-gtc-2026-full-breakdown)
- **Same period, H200 orders:** Huang said ByteDance, Alibaba and Tencent had placed H200 orders of more than 400,000 units, which had not cleared. [CO via PRESS] [network-switch.com, 30 Apr 2026](https://network-switch.com/blogs/news/what-comes-next-ai-hardware-outlook-april-2026)
- **26 Aug 2026, Q2 FY27 call** [CO] ([transcript](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf)):
  - Kress: "We expect to grow revenue by approximately 70% in fiscal 2028. This is a supply-constrained outlook … Customers' forecasts point to our growth doubling next year."
  - Huang on the unconstrained figure: "a lot higher."
  - Stacy Rasgon (Bernstein): "the 70% growth in fiscal 2028 … that's something like … a $200 billion uptick versus the prior outlook … The prior outlook was $1 trillion over the three years." [EST, analyst reconciliation on the call]
  - Vivek Arya (BofA): adding up commitments in the CFO commentary gives "about $500 billion or so … over the next several years." [EST]
  - Kress: "Each generation of NVIDIA infrastructure deployed at PORTS-Pike could represent approximately 1.5 million NVIDIA GPUs, or approximately $150 billion to $200 billion in NVIDIA revenue." [CO] [Q2 FY27 CFO commentary](https://s201.q4cdn.com/141608511/files/doc_financials/2027/Q227/Q2FY27-CFO-Commentary.pdf)
  - "Demand from the AI labs for which we expect to leverage our balance sheet [will] contribute toward roughly a quarter of our business next year."
  - "We know some will call this circular financing. We see it differently."
  - Revenue per gigawatt: about $18B for Hopper, $25B for Blackwell and $40B for Vera Rubin.
- **Unverified viral figures:** "1,000 racks a day" and "$630 billion" in quarterly revenue trace to no NVIDIA statement and no named analyst. [PRESS] [Startup Fortune, 22 Jul 2026](https://startupfortune.com/nvidia-confirms-vera-rubin-is-shipping-but-not-the-630-billion-number/)

### Inferences
- [DERIVED] Recognized Data Center revenue from Q4 FY26 through Q2 FY27 (roughly Oct 2025–Jul 2026) was about $226.6B (62.3 + 75.2 + 89.0). Adding the Q3 FY27 revenue guide ($108B total, of which Data Center is not separately guided) still leaves a large remainder for Nov 2026–Jan 2027 if the $500B "next five quarters" figure covers DC revenue only. If "cumulative" also counts Blackwell revenue from early 2025, the target is easier. The window's start date is ambiguous in the sources read, so the figure cannot be cleanly reconciled.
- The $1T figure doubled the dollar amount but also extended the window by one year (through 2027) and added Vera Rubin. It is not like-for-like growth.

### Gaps
- No transcript was obtained for the Q3 FY26 (19 Nov 2025), Q4 FY26 (25 Feb 2026) or Q1 FY27 (20 May 2026) calls, where Kress likely restated or updated the $500B figure. Exact later wording is therefore unavailable.
- No customer-side confirmation of the $500B or $1T totals was found.
- The full GTC 2026 keynote transcript wording was not obtained.

---

## 5. Customers and contracts (which are binding, which are LOIs or MOUs)

### Takeaway
NVIDIA's largest relationships have moved from "up to" letters of intent toward equity stakes, guarantees and capacity backstops.
- **OpenAI:** the Sept 2025 LOI for up to $100B was never disclosed as finalized. NVIDIA reportedly invested $30B in OpenAI's Feb 2026 round. In Aug 2026, NVIDIA signed definitive guarantees of up to $105B for an OpenAI-leased Ohio site.
- **Anthropic:** an "up to $10B" agreement (Nov 2025), and a reported $10B purchase at Anthropic's IPO (expected 19 Nov 2026).
- **CoreWeave:** a binding $6.3B residual-capacity order to April 2032, plus a $2B equity purchase in Jan 2026.
- **Public strategic stakes** (13F, 30 Jun 2026): Intel, SpaceX, CoreWeave, Nokia, Synopsys, Coherent and Nebius.
- **Other partnerships:** Meta, HUMAIN and the financing platforms are partnerships or MOU-like announcements with no disclosed binding terms.

### Cited Findings
**OpenAI**
- 22 Sep 2025 LOI: "letter of intent for a landmark strategic partnership" to deploy at least 10 GW. "NVIDIA intends to invest up to $100 billion in OpenAI progressively as each gigawatt is deployed." First GW in H2 2026 on Vera Rubin. Details to be finalized "in the coming weeks." [CO] [NVIDIA release, 22 Sep 2025](https://nvidianews.nvidia.com/news/openai-and-nvidia-announce-strategic-partnership-to-deploy-10gw-of-nvidia-systems)
- 19 Nov 2025 (Q3 FY26 10-Q): "We entered into a letter of intent with an opportunity to invest in OpenAI … There is no assurance that we will enter into definitive agreements with respect to the OpenAI opportunity." [CO] [Q3 FY26 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000230/nvda-20251026.htm)
- Jan 2026: negotiations "had not progressed beyond early stages, and the structure was being reconsidered." [PRESS] [Wikipedia "Nvidia"](https://en.wikipedia.org/wiki/Nvidia)
- 25 Feb 2026 (FY26 10-K): "We are finalizing an investment and partnership agreement with OpenAI. There is no assurance that we will enter into an investment and partnership agreement with OpenAI or that a transaction will be completed." [CO] [FY26 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)
- OpenAI's 2026 funding rounds: Feb 2026, $110B at a $730B valuation led by Amazon ($50B), SoftBank ($30B) and **NVIDIA ($30B)**; extended to $120B in Mar 2026; $122B committed at an $852B post-money valuation in Apr 2026. The original 10 GW/$100B plan was "first scaled back." [PRESS] [Wikipedia "OpenAI"](https://en.wikipedia.org/wiki/OpenAI)
- 12 Nov 2026: "Nvidia has invested at least $30 billion" in OpenAI. OpenAI raised $15B at a $1.25T valuation. [PRESS] [CNBC live updates, 12 Nov 2026](https://www.cnbc.com/2026/11/12/nvidia-jensen-huang-ceo-live-updates.html)
- **SB Energy / PORTS-Pike, 17 Aug 2026 (binding; 8-K Item 1.01)** [CO] ([8-K, 17 Aug 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/nvda-20260817.htm); [joint release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/sbeoainvidia-portsrelease.htm)):
  - NVIDIA entered residual value guaranties for about 4.25 GW of IT load in Pike County, Ohio, leased to an OpenAI affiliate under 20-year leases.
  - Aggregate obligation "cumulatively capped at $105 billion."
  - Payment obligations start after ready-for-service, "expected beginning in 2028"; the 10-Q says the first phase is in FY2029.
  - OpenAI "agreed to reimburse and indemnify NVIDIA."
  - NVIDIA holds an option on about 3.8 GW more (the release says 3.75 IT-GW).
  - NVIDIA invests $1.5B in SB Energy.
  - OpenAI will be the customer for 8 IT-GW.
- 26 Aug 2026: "OpenAI's existing and planned commitments represent approximately 12 gigawatts of NVIDIA Compute." [CO] [Q2 FY27 call](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf)
- OpenAI alternatives:
  - AMD agreement, Oct 2025: 6 GW starting with MI450, plus an option to buy up to 160M AMD shares.
  - "Jalapeño" custom chip with Broadcom, announced 24 Jun 2026.
  - OpenAI IPO filing confirmed 8 Jun 2026; Altman said in Sept 2026 that the IPO was delayed to 2027.
  [PRESS] [Wikipedia "OpenAI"](https://en.wikipedia.org/wiki/OpenAI)

**Anthropic**
- 18 Nov 2025: "Anthropic has committed to purchase $30 billion of Azure compute capacity." Its initial compute commitment is "up to one gigawatt" on Grace Blackwell and Vera Rubin. NVIDIA will invest "up to $10 billion" and Microsoft "up to $5 billion." [CO] [Microsoft blog, 18 Nov 2025](https://blogs.microsoft.com/blog/2025/11/18/microsoft-nvidia-and-anthropic-announce-strategic-partnerships/)
- NVIDIA 10-Q: "In November 2025, we entered into an agreement, subject to certain closing conditions, to invest up to $10 billion in Anthropic." [CO] [Q3 FY26 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000230/nvda-20251026.htm)
- 12 Nov 2026: "Nvidia agreed to buy $10 billion of Anthropic stock immediately after the IPO, which is expected to begin trading Nov. 19." [PRESS] [CNBC live, 12 Nov 2026](https://www.cnbc.com/2026/11/12/nvidia-jensen-huang-ceo-live-updates.html)
- Anthropic IPO and compute deals [PRESS] [Wikipedia "Anthropic"](https://en.wikipedia.org/wiki/Anthropic):
  - Public S-1 filed 26 Oct 2026.
  - Bloomberg (Nov 2026): seeking up to $90B at a $1.4T fully diluted valuation.
  - Nscale deal reported at about $45B (Aug 2026) for about 460 MW in West Virginia, expected to use Vera Rubin.
  - Google TPU deal: up to 1M TPUs (Oct 2025).
- 26 Aug 2026: "For another frontier AI lab, we will provide selective credit enhancement for nearly 2 gigawatts of compute." The lab is not named. [CO] [Q2 FY27 call](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf)

**xAI / SpaceX ("SpaceXAI")**
- NVIDIA 13F as of 30 Jun 2026: 122,764,805 shares of Space Exploration Technologies Corp, valued at $20.98B. [CO] [NVIDIA 13F information table, filed 14 Aug 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000065/information_table.xml)
- "SpaceXAI will deploy NVIDIA Vera CPUs" (Q2 FY27); Vera is shipping to SpaceXAI. [CO] [Q2 FY27 release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27pr.htm); [call](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf)
- SpaceX is "a large Nvidia customer." [PRESS] [CNBC live, 12 Nov 2026](https://www.cnbc.com/2026/11/12/nvidia-jensen-huang-ceo-live-updates.html)

**Meta**
- 17 Feb 2026: "multiyear, multigenerational strategic partnership" covering "millions" of Blackwell and Rubin GPUs, Grace-only CPU deployment, potential Vera at scale in 2027, and Spectrum-X. No dollar value. Binding status is not stated. [CO] [NVIDIA, 17 Feb 2026](https://nvidianews.nvidia.com/news/meta-builds-ai-infrastructure-with-nvidia)
- Oct 2026: NVIDIA "floated a non-binding possibility of investing $3 billion in Meta's equity offering." [PRESS] [Wikipedia "Nvidia"](https://en.wikipedia.org/wiki/Nvidia) (not otherwise verified)

**Microsoft, AWS, Google, Oracle**
- Microsoft (CES, 5 Jan 2026): NVL72 systems in Fairwater AI superfactory sites, scaling to "hundreds of thousands of Vera Rubin Superchips." [CO] [CES release](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer)
- Microsoft Azure ran an independent MLPerf Training v6.0 submission on 8,192 GB200 GPUs. [IND: MLCommons] [results sheet](https://docs.google.com/spreadsheets/d/17Mek7pd_bKzfoA_ZiPt4E0jMcCZVE_dYbmsS8SUsJhw/edit)
- AWS (26 Aug 2026): "AWS is deploying an additional 2 million GPUs starting this quarter through the second quarter of fiscal 2029." Vera CPUs at AWS. [CO] [Q2 FY27 call](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf). No AWS-side confirmation was found.
- Google Cloud (Q1 FY27): Vera Rubin-powered A5X instances, and a Gemini preview on Google Distributed Cloud running on Blackwell. [CO] [Q1 FY27 release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000051/q1fy27pr.htm)
- Oracle: OCI NVL72 racks running (21 Jul 2026) and Vera at OCI (Aug 2026). OpenAI–Oracle contract of $300B over five years (Sept 2025). [CO/PRESS] [Startup Fortune](https://startupfortune.com/nvidia-confirms-vera-rubin-is-shipping-but-not-the-630-billion-number/); [Wikipedia "OpenAI"](https://en.wikipedia.org/wiki/OpenAI)

**CoreWeave**
- 9 Sep 2025, binding order form ($6.3B) under the MSA dated 10 Apr 2023: "NVIDIA is obligated to purchase the residual unsold capacity through April 13, 2032." [CO, CoreWeave] [CoreWeave 8-K, 15 Sep 2025](https://www.sec.gov/Archives/edgar/data/1769628/000176962825000047/crwv-20250909.htm)
- 23 Jan 2026: NVIDIA bought 22,935,780 Class A shares at $87.20, for $2B. The parties set a collaboration framework for CoreWeave's ">5 gigawatts of AI factories by 2030." [CO, CoreWeave] [CoreWeave 8-K, 26 Jan 2026](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000044/crwv-20260123.htm)
- NVIDIA Schedule 13G: 11.5% of CoreWeave Class A (event date 23 Jan 2026). [CO] [13G](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000008/primary_doc.xml)
- 13F at 30 Jun 2026: 47,213,353 shares, $4.70B. [CO] [13F](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000065/information_table.xml)

**Other strategic equity [CO]** ([13F as of 30 Jun 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000065/information_table.xml); [Nebius 13G](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000062/primary_doc.xml); [Q3 FY26 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000230/nvda-20251026.htm); [Wikipedia "Nvidia"](https://en.wikipedia.org/wiki/Nvidia))

| Holding | Position at 30 Jun 2026 (13F) | Notes |
|---|---|---|
| Intel | 214,776,632 shares, $29.99B | Committed $5B subject to regulatory approval (Q3 FY26 10-Q). Announced 18 Sep 2025 for ~4% (Wikipedia). [DERIVED] $5B / 214.78M = $23.28 per share. |
| Nokia | 166,389,351 shares, $2.21B | — |
| Synopsys | 4,821,717 shares, $2.15B | — |
| Coherent | 7,788,161 shares, $3.07B | — |
| Nebius | 1,190,476 shares, $329M | A 13G (event 13 Jul 2026) reports 9.3% of Class A. Wikipedia reports a $2B investment announced 11 Mar 2026. |

**Hugging Face (definitive agreement, 2 Sep 2026)**
- About $11.9B purchase price plus up to about $1.0B retention equity. NVIDIA committed to keep the platform open and supporting other silicon vendors. [CO] [8-K, 3 Sep 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000078/nvda-20260902.htm)
- Closing expected in H1 2027. DOJ inquiry (see Legal). [PRESS-ANON] Reuters via [Let's Data Science, 28 Oct 2026](https://letsdatascience.com/news/doj-reportedly-opens-inquiry-into-nvidias-hugging-face-acqui-b6f36063)

**Sovereign**
- HUMAIN (Saudi PIF), 13 May 2025: initial 18,000 GB300 supercomputer; "several hundred thousand" GPUs over five years; up to 500 MW. Forward-looking language; no binding terms disclosed. [CO] [NVIDIA, 13 May 2025](https://nvidianews.nvidia.com/news/saudi-arabia-and-nvidia-to-build-ai-factories-to-power-next-wave-of-intelligence-for-the-age-of-reasoning)
- Q2 FY27 (Aug 2026):
  - Korea: SK Telecom, NAVER and Brookfield, at gigawatt scale.
  - Japan: national AI infrastructure.
  - Europe: 35 new AI HPC supercomputers in development.
  [CO] [Q2 FY27 release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27pr.htm)

**Financing platforms (non-binding)**
- Apollo, BlackRock, Blackstone, Brookfield, Goldman Sachs and KKR, "to mobilize over $500 billion of third-party capital … over time, subject to definitive agreements." [CO] [Q2 FY27 release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27pr.htm)

**Binding vs non-binding summary** (classification is inference based on the wording cited above)

| Classification | Arrangements |
|---|---|
| **Binding / definitive** | CoreWeave $6.3B order form and $2B share purchase; SB Energy guarantees ($105B cap) and $1.5B investment; Groq license (consideration paid); Hugging Face merger agreement (pending regulatory review); Intel, Nokia and Synopsys equity (held per 13F); the $25B notes |
| **Agreement subject to conditions** | Anthropic "up to $10B" (Nov 2025) |
| **LOI / MOU / partnership language** | OpenAI 10 GW / $100B LOI (Sept 2025; superseded in practice); Meta partnership; HUMAIN; Apollo/BlackRock financing platforms ("subject to definitive agreements"); AWS 2M GPUs (company-stated only) |

### Inferences
- The OpenAI relationship was restructured. A $30B equity investment (press-reported) and a capped $105B lease guarantee replaced the per-gigawatt "up to $100B" investment model. No NVIDIA filing states the LOI was terminated.
- NVIDIA's balance sheet is now an instrument of demand. Examples: guarantees ($108.5B maximum exposure), AI-cloud capacity commitments ($36B), equity in customers (SpaceX, CoreWeave, Nebius, OpenAI, Anthropic), and "extended payment terms" (DSO 60 days). Management itself acknowledged the "circular financing" criticism on 26 Aug 2026.

### Gaps
- The xAI–SpaceX combination and NVIDIA's xAI equity history (late-2025 reports) were not sourced. Only the 13F holding of SpaceX shares is confirmed.
- UAE / Stargate UAE: details and export licenses not sourced.
- European sovereign deal specifics (e.g., Mistral, Deutsche Telekom) not sourced.
- Original terms of the Nokia (Oct 2025) and Synopsys (Dec 2025) investments were not re-verified. The 13F share counts are consistent with publicly reported $1B and $2B investments, but I did not fetch the announcements.
- Whether the Anthropic IPO purchase is the same "up to $10B" commitment or additional is unclear.
- The size of NVIDIA's Coherent investment was not found.
- HUMAIN's Nov 2025 expansion (reported 600,000 GPUs) was not verified.

---

## 6. Manufacturing capacity and supply (TSMC, CoWoS, US production, HBM, bottlenecks)

### Takeaway
NVIDIA describes itself as supply-constrained through at least FY2028, with memory (HBM and DRAM) as the dominant constraint and cost driver. Supply commitments jumped to $279B by July 2026, mostly memory. Gross margin is guided to a 71–72% trough in Q4 FY27 because of "extreme pricing conditions in memory." The first US-made Blackwell wafer came out of TSMC Arizona on 17 Oct 2025. CoWoS allocation and HBM4 supplier-qualification details could not be sourced in this session.

### Cited Findings
- Supply commitments rose "from $119 billion last quarter to $279 billion, primarily related to the procurement of memory." They are "for our data center infrastructure systems, primarily memory and manufacturing facilities." [CO] [Q2 FY27 CFO commentary, 26 Aug 2026](https://s201.q4cdn.com/141608511/files/doc_financials/2027/Q227/Q2FY27-CFO-Commentary.pdf); [Q2 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- 26 Aug 2026 call [CO] ([transcript](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf)):
  - "We are experiencing extreme pricing conditions in memory. The magnitude of the price increase has exceeded our prior expectations and are headed even higher into next year."
  - "We have long-standing deep relationships with all three major memory suppliers."
  - Huang: "Our entire supply chain is challenged, and everybody is really running flat out."
  - "We expect supply to remain a bottleneck at least through the end of fiscal year 2028."
- SK hynix: "multiyear technology partnership … to advance next-generation memory" (Q2 FY27). [CO] [Q2 FY27 release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27pr.htm)
- Memory spillover into other segments [CO]:
  - Edge Computing growth was "tempered by elevated memory and systems prices" (Q2 FY27). [Q2 FY27 CFO commentary](https://s201.q4cdn.com/141608511/files/doc_financials/2027/Q227/Q2FY27-CFO-Commentary.pdf)
  - "Supply constraints to be a headwind to Gaming in the first quarter of fiscal 2027 and beyond" (Feb 2026). [Q4 FY26 CFO commentary](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000019/q4fy26cfocommentary.htm)
- HBM4 standard (JEDEC, Apr 2025): up to 8 Gb/s across a 2048-bit interface, up to 2 TB/s per stack, 4–16-high stacks, up to 64 GB. [PRESS] JEDEC/Tom's Hardware via [Wikipedia "High Bandwidth Memory"](https://en.wikipedia.org/wiki/High_Bandwidth_Memory)
- Samsung HBM4: an "80% golden yield" headline (Wccftech, 18 Aug 2026). Samsung delivered 12-layer HBM4E samples in May 2026. [PRESS, weak] via [Wikipedia "High Bandwidth Memory"](https://en.wikipedia.org/wiki/High_Bandwidth_Memory)
- DRAM prices: "compounded increases, some exceeding 200%, since early 2025." Micron cites a "3-to-1 conversion ratio between HBM and DDR5 wafer capacity." [PRESS] Sourceability via [Wikipedia "High Bandwidth Memory"](https://en.wikipedia.org/wiki/High_Bandwidth_Memory)
- Dell'Oro (7 Jan 2026): memory shortages are a primary 2026 deployment risk; chip and optical shortages too. [EST] via [network-switch.com, 30 Apr 2026](https://network-switch.com/blogs/news/what-comes-next-ai-hardware-outlook-april-2026)
- Memory accounts for about $2M of an estimated $7.8M VR200 NVL72 rack (Morgan Stanley). [EST] via [Startup Fortune, 22 Jul 2026](https://startupfortune.com/nvidia-confirms-vera-rubin-is-shipping-but-not-the-630-billion-number/)
- US wafers, 17 Oct 2025: first NVIDIA Blackwell wafer made on US soil, at TSMC's Phoenix, Arizona facility. The blog says Blackwell "has reached volume production." It does not say where CoWoS packaging occurs. [CO] [NVIDIA blog, 17 Oct 2025](https://blogs.nvidia.com/blog/tsmc-blackwell-manufacturing/)
- Corning (May 2026): partnership with up to $3.2B of investment for three US manufacturing facilities. [PRESS] [Wikipedia "Nvidia"](https://en.wikipedia.org/wiki/Nvidia)
- Rubin system assembly: NVIDIA cites "hundreds of partners," including 150 in Taiwan, across 350+ factory sites in 30 countries. Named builders: Dell, HPE, Lenovo, Supermicro, Foxconn, ASUS. [CO via PRESS] [Startup Fortune, 22 Jul 2026](https://startupfortune.com/nvidia-confirms-vera-rubin-is-shipping-but-not-the-630-billion-number/)
- Neocloud partners "are expected to exit the year with 8 gigawatts in total installed capacity, up from approximately 3 gigawatts at the end of 2025." [CO] [Q2 FY27 call](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf)
- Power at the PORTS-Pike campus: "SB Energy and SoftBank will build at least 10 GW of new energy generation, which results in 8 IT-GW of AI factory capacity," plus at least $4.2B in grid infrastructure. [CO] [SB Energy/NVIDIA release, 17 Aug 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/sbeoainvidia-portsrelease.htm)

### Inferences
- [DERIVED] NVIDIA's NVL72 page gives 288 GB of HBM4 per Rubin GPU. If that is eight 36 GB (12-high) stacks, then 22 TB/s implies about 10.7 Gb/s per pin and 19.2 TB/s implies about 9.4 Gb/s per pin. Both exceed JEDEC's 8 Gb/s baseline. The later, lower figure is consistent with HBM4 speed bins being a practical limit. This is an inference; NVIDIA has not stated stack count or pin speed in the sources read.
- The scale-up of commitments ($95B → $119B → $279B in two quarters) while guiding supply-constrained growth indicates NVIDIA is pre-buying memory for multiple years. That shifts inventory and price risk onto NVIDIA if demand or memory prices turn.

### Gaps
- TSMC CoWoS capacity and NVIDIA's allocation (2025–2026 estimates by TrendForce or Morgan Stanley) were not obtained.
- TSMC N3 wafer allocation for Rubin was not obtained.
- Whether Arizona-made Blackwell wafers are packaged in Taiwan or in the US (Amkor/SPIL Arizona) was not found.
- Foxconn (Houston) and Wistron (Fort Worth) US supercomputer assembly status was not sourced.
- HBM4 qualification status by supplier for Rubin (SK hynix lead, Samsung, Micron) was not sourced from primary or reliable trade sources.
- No 2026 Micron or SK hynix statements on NVIDIA allocation were found.

---

## 7. Ownership and key people (including the November 2026 CEO resignation)

### Takeaway
Jensen Huang, co-founder and CEO for 33 years, resigned as President, CEO and director on 11 Nov 2026. This followed reports of extramarital affairs, including one with Alice Huang of Singapore-based Megaspeed, whom US officials reportedly suspect of working for Chinese intelligence. The board says it has no reason to believe national security or NVIDIA secrets were compromised.

As of 23 Mar 2026, Huang beneficially owned 870.6M shares (3.58%), held largely through trusts with his wife. He made no open-market sales in 2026 after selling 6.0M shares (about $1.05B) under a 10b5-1 plan between June and October 2025. CFO Colette Kress is interim CEO, and Harvey Jones is the first independent Chair. The largest reported holders are BlackRock (7.43%) and Vanguard Capital Management (7.31%).

### Cited Findings
**CEO resignation timeline (Nov 2026)**
- 8 Nov 2026 [CO]:
  - The board announced an independent investigation after "recent reports that CEO Jensen Huang was 'the target of a foreign intelligence effort'." It "has no reason to believe national security or NVIDIA's secrets were compromised." [NVIDIA board statement, 8 Nov 2026](https://nvidianews.nvidia.com/news/statement-from-nvidia-board-of-directors)
  - Huang's email to employees admitted he was "unfaithful to my wife." He said he would cooperate fully with the investigation. [NVIDIA, "A Message to Our Company," 8 Nov 2026](https://nvidianews.nvidia.com/news/a-message-to-our-company)
- 10 Nov 2026: independent directors hired former acting US Attorney Joon H. Kim and Wachtell, Lipton, Rosen & Katz. [CO] [Statement of independent directors, 10 Nov 2026](https://nvidianews.nvidia.com/news/statement-from-the-independent-members-of-the-nvidia-board)
- 11 Nov 2026 [CO] ([8-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000082/nvda-20261111.htm); [release, 12 Nov 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000082/nvidiaannouncesceotransiti.htm)):
  - The board "accepted the resignation of Jen-Hsun Huang, as NVIDIA's President, Chief Executive Officer and member of the Board, effective immediately."
  - Colette M. Kress (59), EVP and CFO since 2013, is interim CEO and remains CFO.
  - Harvey C. Jones (73), director since 1993, is the "first-ever Chair."
  - The search for a CEO "will consider internal and external candidates."
  - No reason for the resignation was given.
- Reported reasons [PRESS / PRESS-ANON]:
  - Alleged relationship with Megaspeed businesswoman Alice Huang, whom US intelligence reportedly believes is a Chinese spy. CNBC notes that "the U.S. government has not presented proof of espionage."
  - NYT (11 Nov 2026): affair with Kimberly Powell, NVIDIA VP of healthcare.
  - Reuters, citing two sources: an intimate relationship with a second NVIDIA employee.
  - Huang denies compromising national security or secrets.
  [CNBC live, 12 Nov 2026](https://www.cnbc.com/2026/11/12/nvidia-jensen-huang-ceo-live-updates.html); [Al Jazeera, 12 Nov 2026](https://www.aljazeera.com/news/2026/11/12/why-did-nvidia-ceo-jensen-huang-resign-and-who-is-colette-kress); Washington Post headline, 12 Nov 2026, ["Jensen Huang resigns as Nvidia CEO after affair with alleged spy"](https://www.washingtonpost.com/technology/2026/11/12/nvidia-board-weighs-jensen-huangs-future-after-affair-with-allege-chinese-spy/) (headline only; not fetched)
- Political and market reaction [PRESS] ([CNBC live, 12 Nov 2026](https://www.cnbc.com/2026/11/12/nvidia-jensen-huang-ceo-live-updates.html)):
  - Sen. Tim Scott requested Huang testify on 3 Dec and Commerce Secretary Lutnick on 10 Dec 2026.
  - Sen. Wyden and Rep. Neal opened an investigation into export approvals for NVIDIA chips to China-linked companies.
  - Rep. Mast said Huang agreed to testify.
  - Trump defended Huang and posted that Tim Cook should replace him.
  - Stock: closed at $173.73 on 11 Nov (closing high $239.24 on 6 Oct 2026); fell more than 13% at the open on 12 Nov; closed down 4.3%, with market cap "just above $4 trillion."
  - Huang's stake was put at about $140B, "largely held through trusts co-owned with his wife, Lori."

**Ownership (2026 proxy; table as of 23 Mar 2026; 24,312,141,810 shares outstanding)** [CO] ([DEF 14A, filed 12 May 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000036/nvda-20260512.htm))
- Huang: 870,604,104 shares (3.58%), including 528,531,547 in the Jen-Hsun and Lori Huang Living Trust and 109,040,602 in the Huang Irrevocable Remainder Trust.
- Directors and executive officers as a group (14 persons): 957,313,517 shares (3.94%).
- BlackRock: 1,805,935,550 shares (7.43%). This is based on BlackRock's 13G/A as of 31 Dec 2023, split-adjusted, so it is stale.
- Vanguard Capital Management: 1,777,408,252 shares (7.31%), per its 13G as of 31 Mar 2026.
- Other holdings:
  - Mark Stevens: 34.07M shares.
  - Tench Coxe: 30.56M shares.
  - Harvey Jones: 7.0M shares.
  - Kress: 4.44M shares.

**Huang's insider transactions** [DERIVED from SEC Form 4s] ([EDGAR insider filings for CIK 1045810](https://www.sec.gov/cgi-bin/own-disp?action=getissuer&CIK=0001045810); e.g., [Form 4 filed 31 Oct 2025](https://www.sec.gov/Archives/edgar/data/1045810/000119764925000056/), [Form 4 filed 20 Mar 2026](https://www.sec.gov/Archives/edgar/data/1045810/000119764926000005/), [Form 4 filed 18 Sep 2026](https://www.sec.gov/Archives/edgar/data/1045810/000119764926000012/))
- 377 sale transactions totaling 6,000,000 shares between 20 Jun 2025 and 29 Oct 2025, at roughly $1.05B in aggregate. The Rule 10b5-1 plan was adopted 20 Mar 2025.
- No open-market sales in 2026 through the latest Form 4s on EDGAR (12 Nov 2026). 2026 transactions were tax withholding (F), equity awards (A, 2 Mar 2026) and gifts or intra-trust transfers (G), e.g.:
  - 18 Mar 2026: 58.96M shares moved from GRATs to the Irrevocable Remainder Trust.
  - 16 Jun 2026: 400,000-share gift.
  - 17 Sep 2026: 438,000-share gift.

**Other insider sales, Jun 2025 – Sep 2026** [DERIVED from Form 4s]

| Insider | Shares sold | Approx. value |
|---|---|---|
| Mark Stevens | ~9.79M | ~$1.93B |
| Ajay Puri | ~1.17M | ~$209M |
| Tench Coxe | 1.0M | ~$143M |
| Brooke Seawell | ~0.78M | ~$122M |
| Colette Kress (10b5-1 plans adopted 4 Mar 2025 and 16 Jun 2026) | ~0.53M | ~$96M |
| Harvey Jones | 0.5M | ~$88M |
| Debora Shoquist | ~0.31M | ~$56M |

**Other executive and board changes in 2026 [CO]**
- FY2026 named executive officers: Huang (President and CEO); Kress (EVP and CFO); Ajay K. Puri (EVP, Worldwide Field Operations); Debora Shoquist (EVP, Operations); Timothy S. Teter (EVP, General Counsel and Secretary). [DEF 14A](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000036/nvda-20260512.htm)
- 20 Jan 2026: director Persis Drell resigned. [8-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000003/nvda-20260120.htm)
- 4 May 2026: CAO Donald Robertson retired and Scott Gawel became VP and CAO. [8-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000026/nvda-20260424.htm)
- 13 Jul 2026: Suzanne Nora Johnson joined the board and Audit Committee; board size went from 10 to 11. [8-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000028/nvda-20260507.htm)
- 24 Jun 2026 annual meeting: all ten nominees elected (Huang 16.65B for, 166M against; Coxe 15.41B for, 1.40B against). [8-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000056/nvda-20260624.htm)
- 28 Jun 2026: Puri announced his retirement. Nicholas Parker (55) was appointed EVP, Worldwide Field Operations, starting about 24 Aug 2026. [8-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000060/nvda-20260628.htm)
- Ian Buck (VP Hyperscale and HPC) was named by Ben Bajarin (Creative Strategies) as "the most logical internal candidate." [EST] [CNBC live](https://www.cnbc.com/2026/11/12/nvidia-jensen-huang-ceo-live-updates.html)

### Inferences
- [DERIVED] After Huang's departure, the board has 10 members (11 minus Huang), with Jones as Chair.
- Huang remains a roughly 3.6% holder. His shares sit largely in joint trusts with his wife, so any future sale program would require new 10b5-1 arrangements. No plan for 2026 is visible in the Form 4s.

### Gaps
- Other top-10 institutional holders (FMR, State Street, etc.) and current-dated BlackRock holdings were not obtained.
- Whether Huang retains any advisory or employee role, and any separation terms, was not disclosed in the 8-K.
- No evidence was found either way on whether US authorities have charged anyone in connection with the alleged intelligence approach.

---

## 8. Legal and regulatory matters

### Takeaway
China remains effectively closed to NVIDIA data-center compute.
- **US side:** H20 was license-restricted (April 2025, $4.5B charge). The H20 licensing deal brought only about $60M of revenue despite an informal 15% expectation. H200 licenses (Feb 2026) come with US inspection and a 25% import tariff that NVIDIA absorbs, and shipments are under 1% of DC revenue.
- **China side:** the Chinese government restricted H20, RTX Pro 6000D and H200 purchases.
- **Antitrust:** China's SAMR issued a preliminary finding (Sept 2025) that NVIDIA breached its Mellanox conditions, with no final penalty disclosed as of Aug 2026. The DOJ's long-running probe now covers the Groq, SchedMD and Hugging Face deals.
- **Courts:** the 2018 crypto-era securities class action was certified on 25 Mar 2026. NVIDIA and Supermicro employees were indicted for alleged smuggling in Aug 2026.
- **Congress:** after Huang's resignation, Congress opened inquiries into export approvals.

### Cited Findings
**US export controls on China [CO unless noted]** ([FY26 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm); [Q2 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm))
- **April 2025:** "The USG informed us that it requires a license for export to China (including Hong Kong and Macau) and D:5 countries … of our H20." This led to a $4.5B charge in Q1 FY26.
- **August 2025:**
  - Licenses were granted, but only "approximately $60 million in H20 revenue" was generated under them.
  - "USG officials expressed an expectation that the USG will receive 15% or more of the revenue generated from licensed sales of our products, but the USG did not publish a regulation codifying such requirement."
  - The 15% arrangement covered NVIDIA and AMD China sales. [PRESS] [Wikipedia "Nvidia"](https://en.wikipedia.org/wiki/Nvidia)
- **December 2025 – February 2026 (H200):**
  - December 2025: Trump approved H200 exports to China, subject to US inspections, shipment limits, military-use restrictions and a 25% tariff. [PRESS] [Al Jazeera, 12 Nov 2026](https://www.aljazeera.com/news/2026/11/12/why-did-nvidia-ceo-jensen-huang-resign-and-who-is-colette-kress)
  - Late January 2026: the US cleared sales to vetted Chinese customers, with third-party security testing of each unit. [PRESS] [network-switch.com](https://network-switch.com/blogs/news/what-comes-next-ai-hardware-outlook-april-2026)
  - February 2026, NVIDIA's filing: the USG "granted licenses … small amounts of H200 products to specific China-based customers … The licenses require that the H200s go through an inspection process in the United States … As a result, any H200s shipped … are subject to a 25% tariff upon importation into the United States. We have been unable to pass along any of the tariff to our customers."
- **Status at 26 Aug 2026:**
  - NVIDIA says it has "made a fraction of the allowed shipments," equal to less than 1% of DC revenue.
  - It took a $0.4B H200 charge "as the demand for H200 products diminished."
  - "We were effectively foreclosed from competing in China's data center computing/compute market."
  - Its outlook assumes no China DC compute revenue.
- **Other regulatory exposure:**
  - The 10-Q references the GAIN AI Act, passed by the Senate in the NDAA in October 2025, which "would restrict the Trump Administration's ability to adapt" export rules. It also cites the Remote Access Security Act (RASA), still under consideration, which could bar cloud services to China-parented firms.
  - The 10-K warns of possible mandates for "chip tracking and throttling mechanisms." [CO] [FY26 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)
- BIS reportedly lost about 101 staff since 2024 (19%). [PRESS] Bloomberg via Tom's Hardware, 13 Apr 2026, via [network-switch.com](https://network-switch.com/blogs/news/what-comes-next-ai-hardware-outlook-april-2026)

**China's own measures**
- "The Chinese government has encouraged customers to purchase from our China-based competitors and discouraged customers from purchasing, importing, or using our data center products, including any China-specific product." China's government "publicly questioned whether our H20 products have built-in vulnerabilities." A Chinese agency's Action Plan sets compute-per-watt and per-memory-bandwidth standards for data-center accelerators. [CO] [FY26 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)
- 17 Sep 2025: China's CAC reportedly told ByteDance and Alibaba not to buy the RTX Pro 6000D. [PRESS] [Wikipedia "Nvidia"](https://en.wikipedia.org/wiki/Nvidia)
- 2026: Beijing reportedly directed customs to restrict H200 imports and steered firms toward Huawei Ascend. [PRESS-ANON] [network-switch.com](https://network-switch.com/blogs/news/what-comes-next-ai-hardware-outlook-april-2026)
- Sales "were restricted by the PRC government, and we have been unable to sell all the products for which we have licenses" (26 Aug 2026). [CO] [Q2 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)

**China SAMR (Mellanox conditions)**
- 15 Sep 2025: "China's antitrust regulators published their preliminary finding that our compliance with applicable U.S. export controls … discriminated unfairly against customers in the China market and therefore violated the terms of China's approval of our Mellanox acquisition."
- As of 26 Aug 2026 the 10-Q still describes possible "financial penalties [or] restrictions." No final decision or penalty is disclosed.
[CO] [Q2 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)

**US DOJ antitrust**
- DOJ took the NVIDIA antitrust investigation in June 2024 under the FTC/DOJ split. [PRESS] [Wikipedia "Nvidia"](https://en.wikipedia.org/wiki/Nvidia)
- 28 Oct 2026, Reuters (two sources): the DOJ is asking questions about the about $12.9B Hugging Face deal (e.g., "a fundamental distribution point for AI"). The broader probe "began under the Biden administration" and has examined the Run:ai, SchedMD and Groq deals. DOJ and NVIDIA declined to comment. [PRESS-ANON] [Let's Data Science, 28 Oct 2026](https://letsdatascience.com/news/doj-reportedly-opens-inquiry-into-nvidias-hugging-face-acqui-b6f36063)
- Post-resignation (Nov 2026): Semafor reported a DOJ probe involving Alice Huang-linked organizations. Supermicro shares fell 12%, and Alibaba was reported to be a Megaspeed customer. [PRESS-ANON] [CNBC live, 12 Nov 2026](https://www.cnbc.com/2026/11/12/nvidia-jensen-huang-ceo-live-updates.html); [Wikipedia "Nvidia"](https://en.wikipedia.org/wiki/Nvidia)

**EU and France**
- French Competition Authority:
  - Searched NVIDIA's French offices on 26 Sep 2023. [PRESS] [Wikipedia "Nvidia"](https://en.wikipedia.org/wiki/Nvidia)
  - As of Aug 2026, NVIDIA says "the French Competition Authority (FCA) is questioning whether gaming GPUs and data center GPUs are separate product categories." [CO] [Q2 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)

**Smuggling prosecutions**
- April 2024: Reuters reported China obtained banned NVIDIA chips via Supermicro and Dell servers through tenders. [PRESS] [Wikipedia "Nvidia"](https://en.wikipedia.org/wiki/Nvidia)
- August 2026: employees of NVIDIA and Supermicro were indicted over alleged smuggling of AI servers to China. A senior NVIDIA manager was reportedly accused of forging documents. [PRESS] Ars Technica via [Wikipedia "Nvidia"](https://en.wikipedia.org/wiki/Nvidia)

**Securities and derivative litigation (crypto-mining disclosures, 2017–2018)** [CO] ([Q1 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000052/nvda-20260426.htm); [Q2 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm))
- In re NVIDIA Corp. Securities Litigation, 4:18-cv-07669-HSG:
  - Supreme Court dismissed certiorari as improvidently granted on 11 Dec 2024.
  - On 25 Mar 2026 the district court certified a class of purchasers from 10 Aug 2017 to 15 Nov 2018.
  - On 8 Apr 2026 NVIDIA petitioned the Ninth Circuit for permission to appeal.
- Derivative suits (N.D. Cal.; D. Del. Lipchitz and Nelson; Del. Ch. Horanic) remain stayed or closed.
- No liabilities accrued.
- The SEC settled the crypto disclosure matter for $5.5M in May 2022. [PRESS] [Wikipedia "Nvidia"](https://en.wikipedia.org/wiki/Nvidia)

**Other 2026 litigation and regulatory items**
- January 2026: a court filing in the authors' copyright case alleged NVIDIA staff contacted the shadow library Anna's Archive about pirated training data with management approval. NVIDIA denied this and moved to dismiss. [PRESS] [Wikipedia "Nvidia"](https://en.wikipedia.org/wiki/Nvidia)
- The IRS is examining FY2023–FY2024. [CO] [Q1 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000052/nvda-20260426.htm)
- Congressional inquiries opened in Nov 2026 (see Section 7).

### Inferences
- The "25% fee" widely reported in Dec 2025 was implemented, per NVIDIA's filings, as a 25% US import tariff on H200s routed through US inspection. NVIDIA bears it, so it reduces NVIDIA's margin on any China H200 sales.
- The combination of PRC purchase restrictions, the 25% cost and diminished H200 demand means the H200 policy has produced negligible revenue to date. NVIDIA describes "Hopper 200" shipments as dilutive to gross margin.

### Gaps
- Final status of the GAIN AI Act (whether it was dropped from the enacted FY2026 NDAA) and of the Chip Security Act / location-verification bills was not confirmed from primary sources.
- No SAMR final decision or penalty was found, and no developments after Aug 2026.
- No EU Commission matter for 2025–2026 was found (e.g., EU review of Hugging Face).
- Patent suits (e.g., Xockets, filed 2024) were not tracked; status unknown.
- Court docket for the Aug 2026 smuggling indictment (district, case number, defendants) was not obtained.
- Earlier 2025 DOJ smuggling cases were not sourced.
- Any shareholder suits filed after the Nov 2026 resignation were not found.

---

## 9. Science and engineering: what is demonstrated, verified, unproven; physical limits; is it on solid ground?

### Takeaway
**Verified:** Blackwell-generation performance is independently demonstrated at scale. MLPerf Training v6.0 results come from many non-NVIDIA submitters (Azure, CoreWeave, Oracle, Nebius, Dell, HPE and others), and SemiAnalysis's open InferenceMAX benchmark also measures it. At equal 8-GPU scale, AMD's MI355X is within roughly 5–6% of B200 on two MLPerf training tasks, while GB300 leads.

**Unproven as of 14 Nov 2026:** every headline Rubin claim. These include:
- 10x lower token cost and 4x fewer GPUs for MoE training.
- 35x per MW with LPX.
- NVFP4 training at frontier scale.
- Kyber 600 kW–1 MW racks, 800 VDC benefits and CPO reliability.
- "Revenue per gigawatt" economics.

**Binding physical limits:** reticle size (forcing multi-die packages), HBM bandwidth and supply, rack power and cooling density, copper NVLink reach, and failure rates at scale.

### Cited Findings
**Demonstrated and independently verified**
- MLPerf Training v6.0 (published by Aug 2026):
  - 119 results from 24 submitters.
  - Accelerators: GB300 (38 entries), B300 (20), GB200 (15), B200 (10), AMD MI355X (9), MI350X (7), MI325X (2), MI300X (3), and H100/H200/GH200.
  - No Google TPU, AWS Trainium or Rubin entries.
  [IND: MLCommons] [results sheet](https://docs.google.com/spreadsheets/d/17Mek7pd_bKzfoA_ZiPt4E0jMcCZVE_dYbmsS8SUsJhw/edit); [MLCommons Training page](https://mlcommons.org/benchmarks/training/)
- Largest-scale results (closed division) [IND: MLCommons]:
  - Llama 3.1 405B: 7.07 min on 8,192 GB200 (Azure); 9.77 min on 4,096 GB300 (CoreWeave).
  - DeepSeek-V3 671B: 2.02 min on 8,192 GB300 (CoreWeave); 3.34 min on 8,192 GB200 (NVIDIA).
  - Llama 2 70B LoRA: 0.40 min on 512 GB300 (NVIDIA).
- Equal-scale (8 GPUs) results [IND: MLCommons; DERIVED comparison]:

  | Benchmark | GB300 | B300 | B200 | AMD MI355X | GB200 (8 GPUs) |
  |---|---|---|---|---|---|
  | Llama 2 70B LoRA | 5.61 min (Oracle) | 6.58 min (ASUS) | 7.86 min (Supermicro) | 8.27 min (AMD) | 9.57 min (HPE) |
  | Llama 3.1 8B | 63.5 min (HPE) | 72.0 min (Nebius) | 82.2 min (Dell) | 86.8 min (AMD) | — |

  Source: [results sheet](https://docs.google.com/spreadsheets/d/17Mek7pd_bKzfoA_ZiPt4E0jMcCZVE_dYbmsS8SUsJhw/edit)
- NVIDIA's claim: "Blackwell led across every category in the MLPerf Training 6.0 benchmarks" (26 Aug 2026). [CO] [Q2 FY27 release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27pr.htm). This is consistent with the sheet. However, AMD submitted only in some benchmarks (none in the 405B, DeepSeek-V3 or GPT-OSS 20B tasks), and Google and AWS custom silicon did not submit.
- MLPerf Inference Datacenter v6.1 was released around September 2026. [IND: MLCommons] [supplemental PDF](https://mlcommons.org/wp-content/uploads/2026/09/Supplemental-MLCommons-MLPerf-Inference-v6.1-1.pdf). Results could not be parsed in this session.
- SemiAnalysis InferenceMAX v1 (9 Oct 2025) [IND: SemiAnalysis, with vendor-supplied hardware/configs] ([SemiAnalysis, 9 Oct 2025](https://newsletter.semianalysis.com/p/inferencemax-open-source-inference)):
  - Open-source and run nightly on GB200 NVL72, B200, H100/H200 and AMD MI300X/MI325X/MI355X. AMD and NVIDIA both supplied hardware, and vendors submitted their own server configs.
  - B200 clearly beats MI355X on Llama 3 70B FP4.
  - MI355X has lower cost per million tokens than B200 on GPT-OSS 120B (vLLM) and beats B200 on TRT-LLM below about 225 tok/s/user.
  - B200 is about 20% more energy-efficient than MI355X.
  - GB200 NVL72 has about 4x better TCO than single-node systems at about 35 tok/s/user on DeepSeek FP8, but single-node B200 wins on TCO above about 90 tok/s/user on DeepSeek R1 FP4.
  - Caveats: power is TDP-based, not measured; TCO uses SemiAnalysis assumptions.
- NVIDIA cites "SemiAnalysis InferenceX" results: Blackwell Ultra "up to 50x better performance and 35x lower cost for agentic AI compared with the NVIDIA Hopper platform" (Feb 2026). [CO citing third party] [Q4 FY26 release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000019/q4fy26pr.htm)
- Customer evidence at scale, Meta Llama 3 405B pretraining on up to 16K H100s (700 W each) [IND: Meta, customer paper] ([Llama 3 paper, arXiv 2407.21783, Jul 2024](https://arxiv.org/abs/2407.21783)):
  - "During a 54-day snapshot … 466 job interruptions," of which 419 were unexpected.
  - "Approximately 78% … attributed to confirmed hardware issues"; "GPU issues … 58.7% of all unexpected issues."
  - ">90% effective training time."
  - "Diurnal 1–2% throughput variation."
  - Power swings "on the order of tens of megawatts, stretching the limits of the power grid."

**Claims not yet independently verified (as of 14 Nov 2026)**
- Rubin vs Blackwell [CO] ([CES release](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer); [NVL72 page](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)):
  - "Up to 10x lower inference cost per token" and 10x tokens per MW vs GB200 NVL72, footnoted to Kimi-K2-Thinking at 32K/8K.
  - "4x fewer GPUs" for MoE training, a projection for a 10T-parameter MoE trained on 100T tokens in one month.
  - Up to 35x throughput per MW with Groq 3 LPX, a projection.
  - No Rubin MLPerf results were found.
- Q2 FY27 call: Vera Rubin delivers "30x higher throughput per megawatt and 35x lower token cost relative to Grace Blackwell Ultra." [CO] [transcript](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf). This is inconsistent with the product-page baselines (see Section 11).
- NVFP4 training: NVIDIA's own paper reports a 12B model trained on 10T tokens with loss and accuracy "comparable to an FP8 baseline," using Hadamard transforms, 2D quantization, stochastic rounding and some higher-precision layers. All authors are NVIDIA. [CO] [arXiv 2509.25149, 29 Sep 2025, rev. 4 Mar 2026](https://arxiv.org/abs/2509.25149). No independent frontier-scale replication was found.
- Groq 3 LPX: "nearly 4x the number of tokens per second against the next best alternative on our Artificial Analysis benchmark." [CO citing third party] [Q2 FY27 call](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf). Not independently checked here.
- Vera CPU: "1.8x faster on the spec benchmark" and "five times the bandwidth per watt than any other data center CPU." [CO] [Q2 FY27 call](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf)
- CPO switches: "5x power efficiency," "5x longer uptime" or "10x resiliency." [CO] [CES release](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer); [thegpu.ai](https://thegpu.ai/p/nvidia-gtc-2026-full-breakdown)
- 800 VDC: up to 5% end-to-end efficiency gain, up to 70% lower maintenance and up to 30% lower TCO. [CO] [NVIDIA 800 V blog](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/)
- AI-factory economics: revenue opportunity of $18B/GW (Hopper), $25B/GW (Blackwell) and $40B/GW (Vera Rubin); "Now, compute is revenue." [CO] [Q2 FY27 call](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf); [Q2 FY27 release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27pr.htm)
- GB300 vs Hopper: "50x AI factory output" is projected for DeepSeek-R1 with GB300 at FP4 versus H100 at FP8. [CO] [GB300 NVL72 page](https://www.nvidia.com/en-us/data-center/gb300-nvl72/)

**Physical and engineering limits**
- **Reticle limit and multi-die packaging:**
  - Blackwell joins two reticle-limited dies (about 104B transistors each; 208B per package) with the NV-HBI die-to-die link. Huang said about $10B of R&D went into NV-HBI. [PRESS] [Wikipedia "Blackwell"](https://en.wikipedia.org/wiki/Blackwell_(microarchitecture))
  - Next Platform notes growth comes partly from "two reticle-limited chiplets per socket." [PRESS] [Next Platform](https://www.nextplatform.com/ai/2025/10/29/as-rackscale-gpu-systems-boom-big-green-is-emphatically-red-white-and-blue/1640768)
  - Rubin GPU: 336B transistors, multi-chip on TSMC 3 nm-class. [CO via PRESS] [Tech Insider](https://tech-insider.org/nvidia-gtc-2026-rubin-gpu-analysis/); [thegpu.ai](https://thegpu.ai/p/nvidia-gtc-2026-full-breakdown)
- **HBM:**
  - 288 GB per Rubin GPU, with bandwidth revised to 19.2 TB/s (see Sections 2 and 6).
  - The JEDEC HBM4 baseline is 2 TB/s per stack at 8 Gb/s. [PRESS] [Wikipedia "HBM"](https://en.wikipedia.org/wiki/High_Bandwidth_Memory)
  - Memory is about 25% of an estimated VR200 rack's cost. [EST] [Startup Fortune](https://startupfortune.com/nvidia-confirms-vera-rubin-is-shipping-but-not-the-630-billion-number/)
- **Rack power and distribution** [CO] ([NVIDIA 800 V blog, 20 May 2025](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/)):
  - 54 VDC distribution "begins to hit physical limits" above 200 kW.
  - A 1 MW rack on 54 VDC "may need as much as 200 kg of copper busbar."
  - NVIDIA targets 1 MW IT racks from 2027, with 800 VDC to "coincide with NVIDIA Kyber rack-scale systems in 2027."
  - A Tom's Hardware headline (Mar 2025) refers to "600,000-Watt Kyber racks"; the article body was not verified. [PRESS] via [Wikipedia "Rubin"](https://en.wikipedia.org/wiki/Rubin_(microarchitecture))
  - DGX Rubin NVL8 is listed at about 24 kW. [CO via PRESS] [Tech Insider](https://tech-insider.org/nvidia-gtc-2026-rubin-gpu-analysis/)
- **Cooling:** Vera Rubin NVL72 is liquid-cooled. [PRESS] [thegpu.ai](https://thegpu.ai/p/nvidia-gtc-2026-full-breakdown). NVIDIA's page lists a 45°C inlet temperature without saying which system it applies to. [CO] [NVL72 page](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)
- **Copper NVLink reach:** NVL72 is a single-rack copper NVLink domain. For Vera Rubin Ultra, NVIDIA plans "optical scale-up via NVLink 576 using CPO switches." Feynman Kyber is planned with "both copper and CPO scale-up." [CO via PRESS] [thegpu.ai](https://thegpu.ai/p/nvidia-gtc-2026-full-breakdown)
- **Yields:** Blackwell's 2024 low yields required a mask change. [CO] [Q2 FY25 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581024000264/nvda-20240728.htm). Rubin thermal-lid issues were reported in 2026 and later said to be resolved. [EST/PRESS] [Startup Fortune](https://startupfortune.com/nvidia-confirms-vera-rubin-is-shipping-but-not-the-630-billion-number/)
- **Grid power:** PORTS-Pike requires at least 10 GW of new generation for 8 IT-GW. [CO] [SB Energy release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/sbeoainvidia-portsrelease.htm)

### Inferences
- **Solid ground for the current generation:** Blackwell/GB200/GB300 performance claims at the system level are supported by MLCommons-audited results from multiple independent cloud and OEM submitters. Customers' revenue and capacity behavior supports the same conclusion: NVIDIA reports "NVIDIA Compute is fully utilized across every cloud we serve" [CO], and neocloud capacity is going from 3 to 8 GW.
- **Weaker for the next generation:** Rubin's multiples are vendor projections on chosen workloads, and headline memory and NVLink bandwidth figures have been revised down. Kyber, CPO scale-up and 800 VDC are 2027 engineering programs with no field data yet.
- **Economic layer:** "AI factory" token economics depend on utilization and pricing that NVIDIA increasingly underwrites. Examples are the guarantees, AI-cloud agreements and the roughly 25% of next-year business from balance-sheet-supported labs. The technical claims are better grounded than the financial-durability claims.
- **Energy per token:** this is not independently measured at scale in the sources found. InferenceMAX uses TDP-based power, and NVIDIA's tokens-per-MW figures are projections.

### Gaps
- MLPerf Inference v6.0 (spring 2026) and v6.1 (Sept 2026) per-system results, including any Rubin preview submissions, were not obtained.
- Published Hot Chips 2026 papers (Groq 3 LPX, Vera, Rubin) were not obtained.
- Measured rack power for GB300 NVL72 and Vera Rubin NVL72 was not found.
- Independent NVFP4 training replication was not found.
- No outside verification of CPO switch reliability in production was found.
- CoWoS-L interposer size limits (TSMC roadmap) were not sourced.
- Customers' 2025–2026 papers on GB200/GB300-scale training reliability were not found.

---

## 10. Verification of the four memory-based leads supplied in the assignment

### Takeaway
All four leads are substantially confirmed. Each comes with nuances: the Groq figure, the precise OpenAI sequence, the wording of "$1T," and what "full production" meant.

### Cited Findings
- **Lead 1: Groq, Dec 2025, about $20B, non-exclusive license plus hiring of leaders.** Confirmed, with an amount discrepancy.
  - Announced 24 Dec 2025. Groq called it "non-exclusive licensing." Jonathan Ross and Sunny Madra joined NVIDIA, and Groq "would continue to operate as an independent company." CNBC (David Faber) reported about $20B. [PRESS] [Wikipedia "Groq"](https://en.wikipedia.org/wiki/Groq), citing Reuters, TechCrunch, CNBC and Groq's release of 24 Dec 2025.
  - NVIDIA's 10-K: "non-exclusive license agreement … for its language processing unit technology and hired certain Groq employees. No customer contracts, existing products, or equity interests were purchased." Consideration was $13.0B at closing plus $4B within a year, i.e. **about $17B, not $20B.** [CO] [FY26 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)
  - Groq later raised $650M to pivot to an inference cloud (May 2026). [PRESS] [Wikipedia "Groq"](https://en.wikipedia.org/wiki/Groq)
- **Lead 2: early-2026 reports that the $100B OpenAI LOI was not finalized and that NVIDIA instead invested in OpenAI's 2026 round.** Confirmed by secondary sources, consistent with filings.
  - Not finalized: "no assurance … definitive agreements" (Nov 2025 10-Q) and "finalizing" (Feb 2026 10-K). Jan 2026 reports of early-stage talks and a reconsidered structure.
  - NVIDIA was a $30B participant in the Feb 2026 round. [PRESS] [Wikipedia "OpenAI"](https://en.wikipedia.org/wiki/OpenAI); "at least $30 billion" per [CNBC, 12 Nov 2026](https://www.cnbc.com/2026/11/12/nvidia-jensen-huang-ceo-live-updates.html)
  - NVIDIA's 10-Qs do not name the amount.
- **Lead 3: GTC 2026, about $1T of Blackwell+Rubin demand through 2027.** Confirmed: "expects purchase orders between Blackwell and Vera Rubin to reach $1 trillion through 2027" (16 Mar 2026). [CO via PRESS] [CNBC](https://www.cnbc.com/2026/03/16/nvidia-gtc-2026-ceo-jensen-huang-keynote-blackwell-vera-rubin.html)
- **Lead 4: CES 2026, Rubin "in full production."** Confirmed: "NVIDIA Rubin is in full production, and Rubin-based products will be available from partners the second half of 2026" (5 Jan 2026). [CO] [NVIDIA release](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer). Production shipments began in Aug 2026. [CO] [Q2 FY27 call](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf)

### Inferences
- The Groq gap (about $17B recorded vs about $20B reported) may reflect press rounding, or elements outside the license consideration such as employee retention equity. That is not shown in the sources read.

### Gaps
- No primary OpenAI or NVIDIA document stating the $30B amount and its closing date was found. The 10-Qs aggregate private investments.

---

## 11. Cross-examination log (NVIDIA claims vs outside sources)

### Takeaway
The most material contradictions are:
- **Timing language:** "full production" in Jan 2026 versus production shipments from Aug 2026.
- **Spec revisions:** Rubin HBM4 and NVLink bandwidth cut on the product page.
- **Inconsistent baselines:** Rubin performance multiples are stated against different Blackwell baselines.
- **Deal values:** Groq at about $20B (press) versus about $17B in NVIDIA's accounts.
- **Superseded promises:** the OpenAI "$100B / first GW in H2 2026" LOI versus a 2028-onward Ohio site and a $30B equity check.
- **Inflated or shifting demand claims:** China H200 order counts versus negligible shipments and a write-down.

Competitor and customer counter-claims (AMD MI355X near B200 in MLPerf and InferenceMAX; OpenAI's "Jalapeño" claims) narrow NVIDIA's lead claims but do not contradict NVIDIA's published MLPerf results.

### Cited Findings
Each entry gives the claim (who, when), then the contradicting or qualifying source (who, when).

1. **"Rubin is in full production"** — NVIDIA, 5 Jan 2026 ([release](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer)).
   - Contradicting/qualifying:
     - NVIDIA's own "ramping into full production" (about 31 May 2026; Q2 FY27 release, 26 Aug 2026).
     - "We commenced production shipments of Vera Rubin earlier this month" (call, 26 Aug 2026).
     - 10-Q: production shipments began in Q3 FY27.
     - Wired (via The Decoder, 6 Jan 2026): "it's unclear what Nvidia means by 'full production'."
   - Sources: [Q2 FY27 release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27pr.htm); [call](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf); [The Decoder](https://the-decoder.com/ces-2026-nvidia-promises-five-times-the-ai-performance-and-ten-times-cheaper-inference-with-vera-rubin/)
2. **Rubin timing (internal)** — Huang, 28 Oct 2025: "preparing Rubin to be in production this time next year, maybe slightly earlier" ([Next Platform](https://www.nextplatform.com/ai/2025/10/29/as-rackscale-gpu-systems-boom-big-green-is-emphatically-red-white-and-blue/1640768)).
   - Contradicting: NVIDIA, 5 Jan 2026, "in full production." Two company statements ten weeks apart imply production dates about nine months apart.
3. **Rubin HBM4 bandwidth of 22 TB/s per GPU** — NVIDIA GTC 2026 materials, Mar 2026, as recapped by [thegpu.ai](https://thegpu.ai/p/nvidia-gtc-2026-full-breakdown).
   - Contradicting: NVIDIA's NVL72 product page lists 19.2 TB/s (accessed 14 Nov 2026; change dated early Sept 2026 by Understanding Machine via [Tech Insider](https://tech-insider.org/nvidia-gtc-2026-rubin-gpu-analysis/)). [NVL72 page](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)
4. **NVLink 6 at 3.6 TB/s per GPU and 260 TB/s per rack** — NVIDIA, 5 Jan 2026 ([release](https://nvidianews.nvidia.com/news/rubin-platform-ai-supercomputer)).
   - Contradicting: NVIDIA NVL72 page lists 3 TB/s and 216 TB/s (accessed 14 Nov 2026). Tech Insider also notes NVIDIA's NVLink page and NVLink blog conflict. [NVL72 page](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)
5. **Vera Rubin performance multiple (internal)** — NVIDIA product page: up to 10x tokens/MW and one-tenth the cost per million tokens vs **GB200** NVL72 ([page](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)).
   - Contradicting: Kress, 26 Aug 2026: "30x higher throughput per megawatt and 35x lower token cost relative to Grace Blackwell **Ultra**" ([call](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf)).
   - A larger multiple over the faster GB300 baseline is inconsistent with a smaller multiple over GB200, unless the call figure includes Groq LPX pairing (the page's "35x … when paired with Groq 3 LPX").
6. **Groq deal "about $20 billion"** — CNBC, 24 Dec 2025 (via [Wikipedia "Groq"](https://en.wikipedia.org/wiki/Groq)); CNBC, 16 Mar 2026: "mostly acquired in a $20 billion asset deal" ([CNBC](https://www.cnbc.com/2026/03/16/nvidia-gtc-2026-ceo-jensen-huang-keynote-blackwell-vera-rubin.html)).
   - Contradicting: NVIDIA 10-K, 25 Feb 2026: non-exclusive license; "no … equity interests were purchased"; consideration $13.0B plus $4B, about $17B ([10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)).
7. **OpenAI: "invest up to $100 billion … progressively as each gigawatt is deployed"; "first gigawatt … second half of 2026 on … Vera Rubin"** — NVIDIA/OpenAI, 22 Sep 2025 ([release](https://nvidianews.nvidia.com/news/openai-and-nvidia-announce-strategic-partnership-to-deploy-10gw-of-nvidia-systems)).
   - Contradicting/qualifying:
     - NVIDIA 10-Q, 19 Nov 2025: "no assurance … definitive agreements."
     - Jan 2026: talks early-stage, structure reconsidered ([Wikipedia "Nvidia"](https://en.wikipedia.org/wiki/Nvidia)).
     - Feb 2026: NVIDIA $30B in OpenAI's equity round; plan "first scaled back" ([Wikipedia "OpenAI"](https://en.wikipedia.org/wiki/OpenAI)).
     - 17 Aug 2026: the restructured Ohio site comes online "in phases beginning in 2028" ([SB Energy release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/sbeoainvidia-portsrelease.htm)).
8. **China H200 demand: ByteDance, Alibaba and Tencent ordered >400,000 H200s** — Huang, Mar 2026 ([network-switch.com](https://network-switch.com/blogs/news/what-comes-next-ai-hardware-outlook-april-2026)). Also: Chinese firms "reportedly ordered over two million H200 chips, potentially worth $54bn" — [Al Jazeera, 12 Nov 2026](https://www.aljazeera.com/news/2026/11/12/why-did-nvidia-ceo-jensen-huang-resign-and-who-is-colette-kress).
   - Contradicting: NVIDIA 10-Q, 26 Aug 2026: sales "restricted by the PRC government"; "a fraction of the allowed shipments," under 1% of DC revenue; a $0.4B charge "as the demand for H200 products diminished" ([10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)).
   - The two press figures (400k vs 2M) also conflict with each other.
9. **"25% fee/cut" to the US government on H200 sales** — press framing of the Dec 2025 decision, e.g. [Al Jazeera](https://www.aljazeera.com/news/2026/11/12/why-did-nvidia-ceo-jensen-huang-resign-and-who-is-colette-kress).
   - Qualifying: NVIDIA 10-K and 10-Q describe a 25% **import tariff** triggered by US inspection, which NVIDIA cannot pass on ([Q2 FY27 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)).
   - Similarly for H20: officials "expressed an expectation" of 15% or more, but "the USG did not publish a regulation" ([FY26 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)).
10. **Cause of the 2024 Blackwell delay** — The Decoder, 6 Jan 2026: "Nvidia delayed Blackwell shipments in 2024 because of a design flaw that caused overheating in server racks" ([The Decoder](https://the-decoder.com/ces-2026-nvidia-promises-five-times-the-ai-performance-and-ten-times-cheaper-inference-with-vera-rubin/)).
    - Contradicting: NVIDIA 10-Q, 28 Aug 2024: mask change "to improve production yield" ([10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581024000264/nvda-20240728.htm)). Huang via Reuters, 23 Oct 2024: the flaw was "functional" and "caused the yield[s] to be low" ([Wikipedia "Blackwell"](https://en.wikipedia.org/wiki/Blackwell_(microarchitecture))).
    - The rack-overheating reports were a separate, later (Nov 2024) issue.
11. **"20 million" Blackwell+Rubin GPUs vs 4 million Hopper GPUs** — Huang/NVIDIA chart, 28 Oct 2025.
    - Qualifying: Next Platform, 29 Oct 2025: counts are per chiplet (two per Blackwell package), the chart includes NVL8 and 4-GPU systems, and the dollar multiple equals the chiplet multiple, implying little per-GPU price premium ([Next Platform](https://www.nextplatform.com/ai/2025/10/29/as-rackscale-gpu-systems-boom-big-green-is-emphatically-red-white-and-blue/1640768)).
12. **"$1 trillion" is "double" the $500B** — JPR, 17 Mar 2026 ([JPR](https://www.jonpeddie.com/news/nvidia-gtc-2026-keynote/)).
    - Qualifying: the window extended by a year (through 2027 instead of 2026) and Vera Rubin was added. Bernstein's Rasgon on 26 Aug 2026 described the prior outlook as "$1 trillion over the three years" ([call](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf)).
13. **"Blackwell led across every category in the MLPerf Training 6.0 benchmarks"** — NVIDIA, 26 Aug 2026 ([release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27pr.htm)).
    - Qualifying (not contradicting) [IND: MLCommons] ([results sheet](https://docs.google.com/spreadsheets/d/17Mek7pd_bKzfoA_ZiPt4E0jMcCZVE_dYbmsS8SUsJhw/edit)):
      - No Google TPU or AWS Trainium submissions.
      - AMD absent from the 405B, DeepSeek-V3 and GPT-OSS tasks.
      - Where AMD did submit at 8 GPUs, MI355X was about 5% slower than B200 on Llama 2 70B LoRA (8.27 vs 7.86 min) and about 6% slower on Llama 3.1 8B (86.8 vs 82.2 min).
14. **Blackwell superiority in inference cost** — NVIDIA cites InferenceX ("50x … 35x lower cost" vs Hopper, Feb 2026).
    - Qualifying: SemiAnalysis InferenceMAX v1 (9 Oct 2025) found AMD MI355X had lower TCO per million tokens than B200 on GPT-OSS 120B with vLLM, and beat B200 on TRT-LLM below about 225 tok/s/user. It also found single-node B200 beats GB200 NVL72 on TCO above about 90 tok/s/user on DeepSeek R1 FP4 ([SemiAnalysis](https://newsletter.semianalysis.com/p/inferencemax-open-source-inference)).
15. **NVIDIA's platform vs customers' custom silicon** — Huang, 26 Aug 2026: "XPUs are inference-specific chips for one cloud or one service."
    - Counter-claim: OpenAI's "Jalapeño" (Broadcom) is claimed by OpenAI to be "better than Blackwell," as relayed by BofA's Vivek Arya on the 26 Aug 2026 call ([call](https://s201.q4cdn.com/141608511/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf)). The original OpenAI claim was not read; the announcement date was 24 Jun 2026 ([Wikipedia "OpenAI"](https://en.wikipedia.org/wiki/OpenAI)).
    - TrendForce forecasts ASIC-based AI servers at 27.8% of 2026 AI server shipments. [EST] via [Tech Insider](https://tech-insider.org/nvidia-gtc-2026-rubin-gpu-analysis/)
16. **"Vera Rubin … now shipping"** — JPR subtitle, 17 Mar 2026.
    - Contradicting: the same JPR article body ("ships to customers later in 2026"); CNBC, 16 Mar 2026 ("scheduled to roll out later in 2026"); NVIDIA (production shipments Aug 2026). [JPR](https://www.jonpeddie.com/news/nvidia-gtc-2026-keynote/); [CNBC](https://www.cnbc.com/2026/03/16/nvidia-gtc-2026-ceo-jensen-huang-keynote-blackwell-vera-rubin.html)
17. **Board confidence in Huang** — NVIDIA board, 8 Nov 2026: expressed confidence in Huang and his leadership team ([statement](https://nvidianews.nvidia.com/news/statement-from-nvidia-board-of-directors)).
    - Reversed: board accepted his resignation on 11 Nov 2026 ([8-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000082/nvda-20261111.htm)). CNBC reports board sentiment "turned quickly" after the second affair report ([CNBC live](https://www.cnbc.com/2026/11/12/nvidia-jensen-huang-ceo-live-updates.html)).
18. **Q1 FY27 segment figures (internal recast)** — NVIDIA, 20 May 2026: Hyperscale Q1 FY27 $37.9B; Data Center $75,215M.
    - Recast: NVIDIA, 26 Aug 2026: Hyperscale Q1 $43.05B and DC $75,246M after reclassifying a company from ACIE to Hyperscale "due to a change in their business model." [Q1 FY27 CFO commentary](https://s201.q4cdn.com/141608511/files/doc_financials/2027/Q127/Q1FY27-CFO-Commentary.pdf); [Q2 FY27 CFO commentary](https://s201.q4cdn.com/141608511/files/doc_financials/2027/Q227/Q2FY27-CFO-Commentary.pdf)
19. **SB Energy option size** — NVIDIA 8-K, 17 Aug 2026: "approximately an additional 3.8 gigawatts."
    - Joint release, same day: "the remaining 3.75 IT-GW." Minor rounding inconsistency. [8-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/nvda-20260817.htm); [release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/sbeoainvidia-portsrelease.htm)
20. **Hyperscaler spending outlook** — Kress, 26 Aug 2026: top-five hyperscaler capex "nearly $800 billion in 2026 and $1.3 trillion in 2027."
    - Contrasting estimate: Goldman Sachs Research put 2026 hyperscaler AI capex at $527B (date not given; reported 22 Jul 2026 by [Startup Fortune](https://startupfortune.com/nvidia-confirms-vera-rubin-is-shipping-but-not-the-630-billion-number/)). The definitions (total capex vs AI capex; top-5 vs all hyperscalers) differ, so this is a framing gap rather than a direct contradiction.

### Inferences
- Most contradictions concern NVIDIA's forward-looking or marketing language (production status, multiples, demand pipelines, deal sizes). Audited financial results are consistent with external benchmark evidence for the shipping generation.

### Gaps
- No TSMC, SK hynix, Micron or Foxconn statements contradicting or confirming NVIDIA's supply claims were obtained in this session.
- No Huawei, Cerebras, Google or Amazon published comparisons were obtained.
- No regulator statement (BIS or MOFCOM) for 2026 was read directly.

---

## 12. Summary lists: (a) contradictions found; (b) what could not be found or verified

### Takeaway
There are 20 logged contradictions or qualifications (Section 11). The main unverifiable areas are supply-chain specifics (CoWoS, HBM4 qualification), the 2024–25 GB200 rack issues, regulatory end-states (GAIN AI Act, SAMR penalty), and per-system MLPerf Inference results, because web search was exhausted mid-session.

### Cited Findings
**(a) Contradictions found** (detail and sources in Section 11)
1. CES "full production" (5 Jan 2026) vs production shipments from Aug 2026 and "ramping into full production" (May–Aug 2026).
2. "Production this time next year" (28 Oct 2025) vs "in full production" (5 Jan 2026), both NVIDIA.
3. Rubin HBM4 22 TB/s (GTC 2026) vs 19.2 TB/s (product page, Sept–Nov 2026).
4. NVLink 6 at 3.6 TB/s / 260 TB/s (CES 2026) vs 3 TB/s / 216 TB/s (product page).
5. Rubin multiple: 10x vs GB200 (product page) vs 30x/35x vs GB300 (26 Aug 2026 call).
6. Groq deal: about $20B "asset deal" (CNBC, Dec 2025 and Mar 2026) vs about $17B license with no equity (NVIDIA 10-K, Feb 2026).
7. OpenAI "up to $100B" / first GW in H2 2026 (Sept 2025) vs no definitive agreement, a $30B equity round (Feb 2026) and an Ohio site from 2028 (Aug 2026).
8. China H200 orders (>400k per Huang, Mar 2026; >2M per Al Jazeera, Nov 2026) vs "a fraction" shipped, <1% of DC revenue and a $0.4B charge (10-Q, Aug 2026).
9. "25% fee" (press, Dec 2025) vs a 25% US import tariff borne by NVIDIA (10-K and 10-Q); the 15% H20 "expectation" was never codified.
10. Press attributing the 2024 Blackwell delay to rack overheating (The Decoder, Jan 2026) vs the yield/mask fix (NVIDIA 10-Q, Aug 2024; Huang, Oct 2024).
11. "20 million GPUs" (Oct 2025) counted per die (Next Platform, Oct 2025).
12. "$1T = double $500B" (JPR, Mar 2026) vs a longer window and different scope (Rasgon, Aug 2026).
13. "Led every MLPerf Training 6.0 category" (NVIDIA, Aug 2026): accurate within submissions, but with no TPU/Trainium entries and limited AMD coverage (MLCommons).
14. InferenceX "35x lower cost vs Hopper" (NVIDIA, Feb 2026) vs mixed NVIDIA–AMD TCO results in InferenceMAX (SemiAnalysis, Oct 2025).
15. NVIDIA vs XPUs (Huang, Aug 2026) vs OpenAI "Jalapeño" claims (as relayed on the call; Jun–Aug 2026).
16. JPR "now shipping" (Mar 2026) vs "later in 2026" (JPR body, CNBC) and Aug 2026 (NVIDIA).
17. Board "confidence" in Huang (8 Nov 2026) vs resignation accepted (11 Nov 2026).
18. Q1 FY27 Hyperscale $37.9B (May 2026) vs recast $43.05B (Aug 2026).
19. SB Energy option of 3.8 GW (8-K) vs 3.75 IT-GW (release), both 17 Aug 2026.
20. Hyperscaler capex framing: about $800B for the top 5 in 2026 (Kress, Aug 2026) vs $527B AI capex (Goldman, via Jul 2026 report).

**(b) Could not find or verify**
- Contemporaneous sources on the GB200 NVL72 rack ramp problems (late 2024–early 2025), including customer order changes.
- Exact GTC 2024 Blackwell availability wording; GTC 2025 Vera Rubin "NVL144" spec sheet, including the original HBM4 target.
- NVIDIA's reason for the September 2026 Rubin bandwidth and NVLink spec changes.
- Rubin CPX status; Groq 3 LPX volume shipment confirmation (Q3 FY27); Quantum-X Photonics ship status.
- OCI general availability (27 Oct 2026) and CoreWeave deployment (30 Sep 2026) claims (aggregator-only).
- TSMC CoWoS capacity and NVIDIA's share; N3 allocation; where Arizona Blackwell wafers are packaged; Foxconn/Wistron Texas status.
- HBM4 qualification status by supplier (SK hynix, Samsung, Micron) for Rubin.
- Transcripts for the Q3 FY26, Q4 FY26 and Q1 FY27 calls (later wording of the $500B figure).
- Primary confirmation of NVIDIA's $30B OpenAI investment (amount and closing date).
- xAI–SpaceX combination details and NVIDIA's xAI equity history; UAE/Stargate UAE terms; European sovereign deal specifics; HUMAIN's Nov 2025 expansion.
- Original Nokia and Synopsys investment terms (only 13F holdings verified); size of the Coherent stake.
- Whether the reported $10B Anthropic IPO purchase is incremental to the Nov 2025 "up to $10B."
- Final status of the GAIN AI Act, Chip Security Act and location-verification proposals.
- SAMR final decision or penalty.
- EU matters; patent suits; docket details of the Aug 2026 smuggling indictment; earlier 2025 smuggling cases; post-resignation shareholder litigation.
- MLPerf Inference v6.0 and v6.1 per-system results; Hot Chips 2026 papers; measured rack power for GB300 and Vera Rubin NVL72; independent NVFP4 replication; field reliability of CPO.
- Institutional holders beyond BlackRock (stale 2023 data) and Vanguard; Huang's separation terms.

### Inferences
- The highest-value follow-ups after 14 Nov 2026 are:
  - The Q3 FY27 release and call on 17 Nov 2026: first Vera Rubin revenue, Groq 3 LPX shipments, and any guidance change after the CEO transition.
  - Anthropic's IPO on 19 Nov 2026 and NVIDIA's $10B purchase.
  - Congressional hearings (3 Dec and 10 Dec 2026 requested).
  - The DOJ review of Hugging Face.

### Gaps
- See list (b) above. All of these result from the session's search budget being exhausted, inaccessible sites (Reuters, GitHub raw files), or no disclosure found in NVIDIA's filings.
