# Huawei Ascend AI processor business: fact base (state of affairs as of 14 November 2026)

**How to read this file.** Every item has a date, a source link and a provenance tag. "d:" is the period covered or the as-of date. "pub:" is the publication date.

Provenance tags:
- **[CO]**: stated by Huawei (press release, keynote or executive interview).
- **[CUST]**: stated by a customer or partner.
- **[IND: X]**: examined or measured independently by X.
- **[AN]**: analyst or industry estimate.
- **[GOV]**: government document, statement or estimate.
- **[PR-U]**: press report citing unnamed sources.
- **[PR]**: press report, either on the record or the reporter's own description.
- **[2ND]**: seen only through a secondary relay; the original was not opened.
- **(excerpt)**: seen only in search-result excerpts, because the page was paywalled or blocked or I did not open it.

Arithmetic I did myself appears only under "Inferences". The session's web-search quota ran out before every check could be made; those items are listed under Gaps.

---

## 1. Products and their stage: chips, systems, memory and software. What shipped on schedule, and what is pending?

### Takeaway
As of 14 Nov 2026, Huawei is shipping systems based on the Ascend 910B and 910C. Huawei says more than 1,000 Atlas 900 A3 SuperPoDs had been deployed by Sept 2026.

The Ascend 950PR launched with the Atlas 350 card in late March 2026, inside its Q1 2026 window. Reuters sources say mass production started in April and full-scale shipments come in H2 2026.

The 950DT and the 8,192-chip Atlas 950 SuperPoD are both due in Q4 2026. On 17 Sept 2026, Eric Xu said the 950DT SuperPoDs were "still under testing", with large-scale supply expected "at the end of this year or early next year". The same day, David Wang said the Atlas 950 SuperPoD was "seeing large-scale commercial use".

In Sept 2026 Huawei moved the 960 earlier (960DT in Q1 2027, 960PR in Q3 2027) and added a 980 for 2029. No source I found has independently measured any 950-series specification.

### Cited Findings

**A. Roadmap as announced at Huawei Connect 2025 (Shanghai; Eric Xu keynote, 18 Sept 2025)**
- **Shared die.** The 950PR and 950DT use the same Ascend 950 die. Each delivers 1 PFLOPS in FP8/MXFP8/HiF8 and 2 PFLOPS in MXFP4, with 2 TB/s interconnect, which Huawei says is 2.5x the 910C. [CO] (d: plan as of 18 Sept 2025) — [Huawei, "Groundbreaking SuperPoD Interconnect…", Eric Xu keynote, pub 18 Sept 2025](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech)
- **950PR:** "available Q1 2026", for prefill and recommendation. It uses HiBL 1.0 HBM, which Huawei describes as lower-cost than HBM3E/HBM4E. Huawei gave no capacity or bandwidth figure in the keynote. [CO] — [Huawei keynote, 18 Sept 2025](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech)
- **950DT:** "Q4 2026", for decode and training. It uses HiZQ 2.0 HBM with 144 GB and 4 TB/s. [CO] — [Huawei keynote, 18 Sept 2025](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech)
- **960:** Q4 2027. 2 PFLOPS FP8 and 4 PFLOPS FP4, adding the HiF4 format. It doubles the 950's compute, memory bandwidth, memory capacity and interconnect ports.
- **970:** targeted for Q4 2028, with specs "still being finalized". Planned at 4 PFLOPS FP8 and 8 PFLOPS FP4, 4 TB/s interconnect, and at least 1.5x the 960's memory bandwidth.
- **Cadence:** one release a year, with compute doubling each release. [CO] — [Huawei keynote, 18 Sept 2025](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech)
- **Atlas 900 A3 SuperPoD** (CloudMatrix 384 class): launched March 2025, with up to 384 Ascend 910C and up to 300 PFLOPS. Huawei said more than 300 units had been deployed to more than 20 customers in ISP, telecom and manufacturing (d: 18 Sept 2025). [CO] — [Huawei keynote](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech)
- **Atlas 950 SuperPoD (Q4 2026), as announced:**
  - Up to 8,192 Ascend 950DT in 160 cabinets (128 compute, 32 communications) over 1,000 m².
  - 8 EFLOPS FP8 and 16 EFLOPS FP4, 1,152 TB of memory and 16.3 PB/s of interconnect.
  - Claimed 4.91M tokens/s in training (17x the A3) and 19.6M tokens/s in FP4 inference (26.5x).
  - Claimed versus NVIDIA's NVL144 (H2 2026): 56.8x the NPUs, 6.7x the compute, 15x the memory and 62x the interconnect bandwidth.

  [CO] — [Huawei keynote](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech)
- **Atlas 960 SuperPoD (Q4 2027):** up to 15,488 Ascend 960 in 220 cabinets, 30 EFLOPS FP8 and 60 EFLOPS FP4, 4,460 TB of memory and 34 PB/s. [CO] — [Huawei keynote](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech)
- **SuperClusters:**
  - Atlas 950 SuperCluster (Q4 2026): 64 Atlas 950 SuperPoDs, more than 520,000 950DT in more than 10,000 cabinets, 524 EFLOPS FP8.
  - Atlas 960 SuperCluster (Q4 2027): more than 1M NPUs, 2 ZFLOPS FP8 and 4 ZFLOPS FP4.

  [CO] — [Huawei keynote](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech); see also [Huawei, "World's Most Powerful SuperPoDs and SuperClusters", Sept 2025](https://www.huawei.com/en/news/2025/9/hc-lingqu-ai-superpod) (excerpt)
- **UnifiedBus ("Lingqu"):** Huawei published the 2.0 specification. UB 1.0 is used in the Atlas 900 A3, with deliveries from March 2025. Huawei claims 2.1 µs latency, 100 ns optical fault detection and "optical reliability 100x higher". [CO] — [Huawei keynote](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech)
- **Huawei's own statement on process:** the keynote says the Chinese mainland "will lag in process nodes for a long time". Huawei therefore pursues gains by combining chips and scaling interconnect. [CO] — [Huawei keynote](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech)
- **Independent relays** reported the same dates (950PR Q1 2026, 950DT Q4 2026, 960 Q4 2027, 970 Q4 2028). [PR] (excerpt) — [DCD](https://www.datacenterdynamics.com/en/news/huawei-announces-annual-release-cadence-for-three-new-ascend-ai-chips-unveils-supernode-offering-company-says-will-outperform-nvidias-nvl144/); [RCR Wireless, pub 22 Sept 2025](https://rcrwireless.com/20250922/ai-infrastructure/huawei-ai-chips)

**B. Roadmap as updated at Huawei Connect 2026 (Shanghai, 17–19 Sept 2026)**
- **David Wang keynote** (Deputy Chairman and Rotating Chairman, 17 Sept 2026):
  - Ascend 960DT in Q1 2027, "three quarters ahead of the original roadmap".
  - 960PR in Q3 2027, "one quarter ahead of schedule".
  - 970 in 2028 and 980 in 2029.
  - "Atlas 950 SuperPoD is seeing large-scale commercial use".
  - More than 1,000 Atlas 900 A3 SuperPoDs deployed.

  [CO] — [Huawei, "Advancing the Agentic World, Building a Solid Silicon Foundation", pub 17 Sept 2026](https://www.huawei.com/en/news/2026/9/hc-wang-keynote)
- **Atlas 960E SuperPoD**, which Huawei calls the first based on near-packaged optics (NPO):
  - Up to 4,096 NPUs, 8 EFLOPS FP8 and up to 1 PB of HBM.
  - 5,500 "Hi-ONE" NPO engines at 7.2 Tbit/s each replace 48,000 800G pluggable modules.
  - Claimed to cut power by more than 550 kW and to reach 99.8% availability.
  - No launch date was given.

  [CO] — [Huawei, 17 Sept 2026](https://www.huawei.com/en/news/2026/9/hc-wang-keynote). A Huawei roundtable page says the NPO-based Atlas 960 system "is currently under testing" (excerpt; the page returned HTTP 503 when opened) — [Huawei](https://huawei.com/en/news/2026/9/new-computing-architecture-peerium)
- **SuperCluster topology:** a two-tier, four-plane Clos links up to 512,000 NPUs, and a multi-rail topology reaches up to 1M NPUs. [CO] — [Huawei, 17 Sept 2026](https://www.huawei.com/en/news/2026/9/hc-wang-keynote). The Register called the 1M configuration theoretical, as relayed by TheNextWeb. [PR] — [TheNextWeb, Ana Maria Constantin, pub 18 Sept 2026](https://thenextweb.com/news/huawei-connect-2026-ascend-960-superpod-unifiedbus)
- **The Register on the 960DT** (as relayed): up to 288 GB of memory and 4 PFLOPS FP4, about half the FP8 and one-third of the FP4 compute of NVIDIA's B300, which NVIDIA cannot sell in China. [PR] — [TheNextWeb, 18 Sept 2026](https://thenextweb.com/news/huawei-connect-2026-ascend-960-superpod-unifiedbus)
- **Analyst Rui Ma** pointed out that the new pod holds 4,096 NPUs, against the 15,488-chip Atlas 960 SuperPoD announced in 2025. [PR] — [TheNextWeb, 18 Sept 2026](https://thenextweb.com/news/huawei-connect-2026-ascend-960-superpod-unifiedbus)
- **Epoch AI's reading of the later roadmap** [AN, citing Huawei as reported]:
  - 960PR (late 2027): 8 PFLOPS FP4 and 2.4 TB/s, "likely LPDDR".
  - 970: FP4 "raised from 8 to 14 PFLOPS", with 14.4 TB/s of memory bandwidth.
  - 980 (late 2029): 28 PFLOPS FP4 and about 38 TB/s.
  - 990 (2030): the first Ascend with "LogicFolding".

  (pub 4 Sept 2026, updated 24 Sept 2026) — [Epoch AI, Venkat Somala, "Will Huawei catch up to Nvidia by 2030?"](https://epoch.ai/publications/huaweis-roadmap-to-2031)

**C. Status of each chip (as of 14 Nov 2026)**
- **Ascend 910B and 910C:** in production and deployed. The Atlas 900 A3 SuperPoD uses the 910C. [CO] — [Huawei keynote, 18 Sept 2025](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech). BIS's 13 May 2025 guidance names the 910B, 910C and 910D. [GOV] (excerpt) — [Arnold & Porter, May 2025](https://www.arnoldporter.com/en/perspectives/advisories/2025/05/commerce-new-guidance-curb-adversaries-access-to-advanced-ai-tech)
- **Ascend 950PR (launch):** "Huawei officially launched the Ascend 950PR processor and introduced the Atlas 350 AI accelerator card." [PR] (pub 24 Mar 2026; article paywalled beyond the lead) — [DIGITIMES](https://www.digitimes.com/news/a20260324PD210/huawei-ascend-performance-2026.html)
- **Atlas 350 launch details,** relayed in press (excerpt). These are company claims as reported and are not independently measured.
  - Launched at Huawei's China Partner Conference 2026 in Shenzhen in late March 2026.
  - 1.56 PFLOPS FP4 and up to 112 GB of HiBL 1.0.
  - Claimed about 2.8–2.87x the H20.
  - Outlets disagree on memory bandwidth (1.4 vs 1.6 TB/s) and power (600 W card vs about 900 W module).
  - A price of about RMB 111,000 appears in press only and is not an official list price.
  - Seven partners, including Kunlun and Huakun, released Atlas 350 servers.

  [CO via PR] — [TechRadar](https://www.techradar.com/pro/huawei-reveals-its-latest-nvidia-h20-killer-packing-a-frankly-ridiculous-1-56-pflops-of-fp4-compute-and-up-to-112gb-of-hbm); [Huawei Central](https://www.huaweicentral.com/ascend-950pr-ai-chip-everything-you-need-to-know/); [Tech Edition](https://www.techedt.com/huawei-unveils-atlas-350-accelerator-with-high-performance-ai-compute-capabilities)
- **Ascend 950PR (shipments, per Reuters sources):**
  - Samples went to customers in January 2026, mass production was expected from April, and full-scale shipments in H2 2026.
  - About 750,000 950PR units are planned for 2026.
  - ByteDance and Alibaba are planning orders after testing went well.
  - The chip's draw is better compatibility with NVIDIA's CUDA.

  [PR-U] (Reuters 27 Mar 2026, relayed) — [TrendForce, pub 1 Apr 2026](https://www.trendforce.com/news/2026/04/01/news-huawei-2025-r-cloud-revenue-slips/)
- **Ascend 950PR (Huawei, 17 Sept 2026):** Eric Xu said the 950PR has launched to market and is "primarily used for AI inference". He added: "the total volume of supply available in the market is not very big." [CO] — [Huawei roundtable summary, Media OutReach release, pub 30 Sept 2026](https://www.manilatimes.net/2026/09/30/tmt-newswire/media-outreach-newswire/huawei-pioneers-a-new-computing-architecture-for-the-ai-era-making-one-million-processors-work-as-one-computer-summary-of-roundtable-meeting-between-eric-xu-and-international-media-outlets-on-september-17/2436416)
- **Ascend 950DT and Atlas 950 SuperPoD (Huawei, 17 Sept 2026):**
  - Eric Xu said SuperPoDs based on the 950DT are "mainly used for AI training" and are "still under testing".
  - He expects large-scale supply "at the end of this year or early next year", and called test results "pretty good" without giving figures.
  - "A SuperCluster with 256,000 computing cards is currently being deployed and tested."

  [CO] — [Huawei roundtable summary, pub 30 Sept 2026](https://www.manilatimes.net/2026/09/30/tmt-newswire/media-outreach-newswire/huawei-pioneers-a-new-computing-architecture-for-the-ai-era-making-one-million-processors-work-as-one-computer-summary-of-roundtable-meeting-between-eric-xu-and-international-media-outlets-on-september-17/2436416). Huawei has publicly said the 950DT will be available in 4Q26. [CO via PR] — [TrendForce, pub 10 Sept 2026](https://www.trendforce.com/news/2026/09/10/news-chinese-ai-chipmakers-reportedly-hike-prices-on-hbm-costs-huawei-950dt-up-as-much-as-50/)
- **Atlas 950 SuperPoD (MWC):** its "first global debut" was at MWC Barcelona (2 Mar 2026), presented by Seaway Zhang, President of the Computing Product Line. Huawei described 64 NPUs per cabinet, scaling to 8,192, and gave no availability or pricing outside China. [CO] — [Huawei, pub 2 Mar 2026](https://www.huawei.com/en/news/2026/3/mwc-superpod-ai)
- **Huawei Cloud's Ascend 950 cluster service,** per Huawei Cloud CEO Zhou Yuefeng at Connect 2026:
  - A 1,024-card UB cluster with up to 1 EFLOPS FP8 and 2 EFLOPS FP4, and 256 TB of globally addressable memory.
  - Commercial operation in China from 30 Sept 2026, and overseas from 30 Nov 2026. **The overseas date has not yet arrived as of 14 Nov 2026.**
  - More than 1,000 Ascend supernodes deployed; "Ascend 950 supernodes have entered commercial use".

  [CO] — [TechNode, pub 18 Sept 2026](https://technode.com/2026/09/18/huawei-sets-commercial-launch-dates-for-ascend-950-ai-cluster-cloud-service/)

**D. Memory: HiBL 1.0 and HiZQ 2.0**
- Huawei says the 950PR uses HiBL 1.0 and the 950DT uses HiZQ 2.0 (144 GB, 4 TB/s). [CO] — [Huawei keynote, 18 Sept 2025](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech). Huawei "has not disclosed where or how this memory is made" (d: Sept 2026). [PR] — [TrendForce, 10 Sept 2026](https://www.trendforce.com/news/2026/09/10/news-chinese-ai-chipmakers-reportedly-hike-prices-on-hbm-costs-huawei-950dt-up-as-much-as-50/)
- Epoch lists the 950PR at 128 GB and 1.6 TB/s but classifies it as using "non-HBM memory". For 2026 it models the 950DT with a 96 GB variant rather than 144 GB. [AN] — [Epoch AI](https://epoch.ai/publications/huaweis-roadmap-to-2031)

**E. Software: CANN and MindSpore**
- **Open-source pledge,** made at the Ascend Computing Industry Development Summit in Beijing on 5 Aug 2025:
  - CANN open source and open access, based on the 910B/910C design, by 31 Dec 2025.
  - Mind-series kits and toolchains fully open source by 31 Dec 2025.
  - openPangu to be open-sourced, with no date given.

  [CO] — [Huawei keynote, 18 Sept 2025](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech)
- **Zhang Dixuan** (President, Ascend Computing Business), 20 Sept 2025:
  - "By late September, all CANN operators will be open-sourced on GitCode".
  - Domain libraries, GE, Ascend C and MindIE by Dec 2025.
  - A CANN Technical Steering Committee was set up.
  - The Atlas 350 card, Atlas 550 module and Blade are planned for 2026.
  - Huawei will put 1,500 PFLOPS of compute and 30,000 development boards a year into the ecosystem.

  [CO] — [Huawei, pub 20 Sept 2025](https://www.huawei.com/en/news/2025/9/hc-shengten-opensource)
- **CANN community, Sept 2026:**
  - CANN "has moved to sustained, community-driven open-source development".
  - External developers make up 61% of CANN developers, and there are more than 5,200 monthly active developers.
  - More than 40 models were "natively pre-trained on Ascend and CANN".
  - Ascend supports more than 90 third-party projects, including PyTorch, Triton, vLLM and veRL.
  - Ascend is an official PyTorch accelerator backend and "the first official Chinese compute platform on PyTorch's website".

  [CO] — [Huawei, 17 Sept 2026](https://www.huawei.com/en/news/2026/9/hc-wang-keynote)
- **MindSpore:** Zhipu says GLM-Image (14 Jan 2026) was trained on Ascend (Atlas 800T A2) with MindSpore. [CUST] (excerpt) — [InfoWorld](https://www.infoworld.com/article/4116787/chinese-ai-firm-trains-state-of-the-art-model-entirely-on-huawei-chips.html)

### Inferences
- **950PR** met its Q1 2026 target as a launch event (late March 2026). Volume came later: mass production from April and full-scale shipments in H2 2026, according to Reuters sources and Eric Xu's Sept 2026 statement that supply is "not very big".
- **950DT and Atlas 950 SuperPoD:** as of 14 Nov 2026 their Q4 2026 date is still pending. I found no independent confirmation of volume deliveries, and Huawei's own executives described the status differently on the same day (see §9, C2).
- **Huawei's system figures are internally consistent with its chip figures** (my arithmetic):
  - Atlas 950: 8 EFLOPS ÷ 8,192 ≈ 0.98 PFLOPS FP8 per chip, and 1,152 TB ≈ 8,192 × 144 GB.
  - Atlas 960: 30 EFLOPS ÷ 15,488 ≈ 1.94 PFLOPS FP8 per chip, and 4,460 TB ÷ 15,488 ≈ 288 GB per chip, which matches The Register's 288 GB for the 960DT.
  - Atlas 960E: 8 EFLOPS ÷ 4,096 ≈ 1.95 PFLOPS FP8.
  - Huawei Cloud's 1,024-card cluster: 1 EFLOPS ÷ 1,024 ≈ 0.98 PFLOPS FP8 per card.
- **The NVL144 comparison** gets 6.7x the compute from 56.8x the chips, which implies about 0.12x of the per-GPU-die compute of NVIDIA's part (my arithmetic on Huawei's own numbers). The strategy is to compete at system scale, not at chip level.
- **The launched Atlas 350's reported 1.56 PFLOPS FP4** is about 78% of the 2 PFLOPS MXFP4 that the 2025 roadmap gave for the 950 die. The source of the gap (clock, power or binning) is not explained in any source I saw.

### Gaps
- Ascend 310 (inference chip): no current information was gathered in this session.
- Ascend 910D: the only source naming it is BIS's May 2025 guidance. I found no Huawei launch or status.
- I did not open an official Atlas 350 or 950PR datasheet. Power and bandwidth figures conflict across outlets.
- Who manufactures HiBL 1.0 and HiZQ 2.0, and whether HiBL 1.0 is true HBM (Huawei says HBM; Epoch says "non-HBM").
- Whether all of the CANN open-sourcing promised for 31 Dec 2025 was done. Only Huawei's 2026 claims exist, with no third-party audit.
- Whether Huawei Cloud's "Ascend 950" service runs on the 950PR or the 950DT.
- Any confirmed customer delivery of an Atlas 950 SuperPoD or 950DT in volume by 14 Nov 2026.
- The 960PR spec (Epoch's 8 PFLOPS FP4 against the 2025 roadmap's 4 PFLOPS FP4 for the 960): I did not find Huawei's 2026 disclosure that would reconcile them.

---

## 2. Milestones met or missed: yields, volume targets against output, reported problems, and 2026 shipments

### Takeaway
Reported yields improved from about 20% to about 40% for the 910C between 2024 and early 2025, according to FT sources, with a 60% target. No yield figures exist for the 950 series. TechInsights (Mar 2026) expects "low yields" for data-center AI dies on SMIC N+3.

Volume estimates for 2025 range from 200,000 or fewer (US Commerce, June 2025) to about 800,000 (SemiAnalysis, Epoch). IDC counts 572,000 Huawei accelerators shipped in China in H1 2026 alone. Targets for 2026 are about 750,000 950PR (Reuters sources) and 1.5M Ascend units in total (WSJ via Epoch).

Problems on record:
- DeepSeek's failed R2 training runs on Ascend (FT, Aug 2025).
- HBM-driven price increases of 20–60% in 2026.
- Huawei's own statement that it cannot meet demand in China.

### Cited Findings

**Yields**
- FT, as relayed in Feb 2025: the 910C line yield was about 40%, up from about 20% a year earlier, and the Ascend line became profitable for the first time. Huawei and SMIC were targeting 60%. [PR-U] (excerpt) — [TrendForce, pub 25 Feb 2025](https://www.trendforce.com/news/2025/02/25/news-china-advances-in-ai-chips-huawei-reportedly-boosts-yield-to-40-making-ascend-line-profitable/); [DIGITIMES, pub 25 Feb 2025](https://www.digitimes.com/news/a20250225PD224.html)
- CSIS (Mar 2025), citing industry sources: about 75% of 910Cs survive advanced packaging. [AN] (excerpt) — [TechPowerUp, pub 10 Mar 2025](https://techpowerup.com/333877/huawei-obtained-two-million-ascend-910b-dies-from-tsmc-via-shell-companies-to-circumvent-us-sanctions); [CSIS](https://www.csis.org/analysis/limits-chip-export-controls-meeting-china-challenge)
- TechInsights (17 Mar 2026): DUV limitations combined with the newness of N+3 will lead to "low yields for data center AI chips". N+3 "will not be a viable solution for data center AI chips". [IND: TechInsights analysis; public summary only] — [TechInsights, "Can China even build data center AI chips?"](https://www.techinsights.com/ko/node/61228)

**Volume targets against reported output**
- **2025 plan (FT, Feb 2025):** about 100,000 910C and about 300,000 910B in 2025. 2024 output was about 200,000 910B and no 910C. [PR-U] (excerpt) — [TrendForce, 25 Feb 2025](https://www.trendforce.com/news/2025/02/25/news-china-advances-in-ai-chips-huawei-reportedly-boosts-yield-to-40-making-ascend-line-profitable/)
- **US Commerce, 12 June 2025.** Under Secretary Jeffrey Kessler told a House Foreign Affairs subcommittee: "Our assessment is that Huawei Ascend chip production capacity for 2025 will be at or below 200,000 and we project that most or all of that will be delivered to companies within China." [GOV] (excerpt) — [Bloomberg, pub 12 June 2025](https://www.bloomberg.com/news/articles/2025-06-12/us-says-huawei-s-2025-output-is-no-more-than-200-000-ai-chips); [SCMP](https://www.scmp.com/tech/tech-war/article/3314356/huaweis-ai-semiconductor-output-limited-200000-2025-us-commerce-official-says)
- **SemiAnalysis (8 Sept 2025; Dylan Patel, AJ, Myron Xie):** 507k Ascend units shipped in 2024, mostly 910B, and 805k in 2025, of which 653k were 910C. It called the 200k figure "significantly off the mark". [AN] — [SemiAnalysis, "Huawei Ascend Production Ramp"](https://newsletter.semianalysis.com/p/huawei-ascend-production-ramp)
- **Bloomberg (29 Sept 2025):** about 600,000 910C planned for 2026, "roughly twice" the 2025 output, and up to 1.6M Ascend dies across the line in 2026. [PR-U] — [RCR Wireless, pub 30 Sept 2025](https://rcrwireless.com/20250930/ai-infrastructure/huawei-ai-chips-2); [Invezz, pub 29 Sept 2025](https://invezz.com/news/2025/09/29/huawei-to-double-ai-chip-output-in-2026-targeting-1-6-million-dies/)
- **Epoch AI (Sept 2026):**
  - About 800,000 Ascend units in 2025, against about 4.5M NVIDIA units.
  - A 2026 median of about 1.5M Ascend: about 750k 950PR, 430k 910C, 240k 950DT using CXMT/XMC HBM, and 80k 950DT using smuggled HBM.
  - It cites "a report from the Wall Street Journal that Huawei expects to ship 1.5 million Ascend units in 2026".

  [AN; WSJ claim = PR-U, not opened] — [Epoch AI](https://epoch.ai/publications/huaweis-roadmap-to-2031)
- **IDC (relayed by Reuters, 13 Oct 2026):**
  - Huawei shipped 572,000 AI accelerators in China in H1 2026, up from "just over 300,000" a year earlier, a 28% share.
  - NVIDIA shipped 678,000 (down 44% YoY), a 34% share.
  - The total market was 2.008M units. Non-GPU accelerators (1.016M) overtook GPUs (991k) for the first time.

  [AN] (excerpt) — [TradingView/Seeking Alpha](https://www.tradingview.com/news/seekingalpha:62d1b5de5094b:0-nvidia-s-china-ai-chip-market-share-falls-to-34-as-huawei-gains-ground-idc/); [36Kr](https://eu.36kr.com/en/p/4024302190728839); [Benzinga](https://www.benzinga.com/markets/tech/26/10/62319484/nvidia-loses-ground-in-china-as-huaweis-ai-chip-shipments-nearly-double-capturing-28-market-share-report)
- **Huawei, 17 Sept 2026.** Eric Xu: "we don't have enough capacity to even satisfy the demand in China". [CO] — [Huawei roundtable summary](https://www.manilatimes.net/2026/09/30/tmt-newswire/media-outreach-newswire/huawei-pioneers-a-new-computing-architecture-for-the-ai-era-making-one-million-processors-work-as-one-computer-summary-of-roundtable-meeting-between-eric-xu-and-international-media-outlets-on-september-17/2436416). TheNextWeb relays Xu as saying China catches up with its own hardware demand around 2030. [CO via PR] — [TheNextWeb](https://thenextweb.com/news/huawei-connect-2026-ascend-960-superpod-unifiedbus)

**Reported problems**
- **DeepSeek R2 (FT, 14 Aug 2025).**
  - DeepSeek delayed R2 after "unsuccessful attempts to train it on Huawei's chips".
  - Huawei sent engineers on site, yet no successful training run on Ascend was completed.
  - DeepSeek uses NVIDIA for training and Ascend for inference.
  - Authorities had urged the switch to Ascend after R1.

  [PR-U, relayed] — [TrendForce, pub 14 Aug 2025](https://www.trendforce.com/news/2025/08/14/news-deepseek-r2-model-launch-reportedly-delayed-amid-huawei-ascend-chip-hurdles/). Secondary relays add stability problems, slower chip-to-chip connectivity and weaker software. (excerpt) — [The Decoder](https://the-decoder.com/deepseek-reportedly-delayed-its-latest-ai-model-after-technical-issues-with-huaweis-ascend-chips/); [eWeek](https://www.eweek.com/news/deepseek-ai-model-launch-delayed-chips-nvidia/)
- **Price increases (Reuters sources, 10 Sept 2026):**
  - The 950DT's indicated price rose to more than RMB 250,000 per card, 20–50% above prices quoted two months earlier, depending on contract terms.
  - The 950PR rose from about RMB 60k at the start of 2026 to more than RMB 80k.
  - The 910C board rose from about RMB 90k to more than RMB 110k.
  - The cause given is the HBM shortage.

  [PR-U] — [TrendForce, 10 Sept 2026](https://www.trendforce.com/news/2026/09/10/news-chinese-ai-chipmakers-reportedly-hike-prices-on-hbm-costs-huawei-950dt-up-as-much-as-50/). A Bloomberg-sourced report put the 950DT increase at 60% over three months, from about RMB 150,653 to RMB 250,000. [PR-U] (excerpt) — [Huawei Central](https://www.huaweicentral.com/huawei-ascend-950dt-price-jumped-60-over-past-three-months/); [Seeking Alpha](https://seekingalpha.com/news/4641552-huawei-raises-advanced-ai-chip-prices-60-as-demand-outpaces-supply-report)
- **Memory shortfall (The Information, Nov 2026):** Huawei asked some customers to source memory themselves. The 960DT is expected to rely heavily on Samsung and SK hynix HBM, and domestic supplier Fujian Jinhua lacks the capacity Huawei needs. [PR-U] — [TrendForce, pub 3 Nov 2026](https://www.trendforce.com/news/2026/11/03/news-china-reportedly-obtains-smuggled-hbm-via-server-packages-huawei-960dt-faces-domestic-hbm-shortage/)
- **Huawei's own admission:** Eric Xu acknowledged gaps with NVIDIA "in terms of individual chips and ecosystems" (Sept 2025). [CO] — [RCR Wireless, 30 Sept 2025](https://rcrwireless.com/20250930/ai-infrastructure/huawei-ai-chips-2)

**Milestones Huawei says it met**
- Atlas 900 A3 deliveries began in March 2025. More than 300 units were deployed by Sept 2025 and more than 1,000 by Sept 2026. [CO] — [Huawei, 18 Sept 2025](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech); [Huawei, 17 Sept 2026](https://www.huawei.com/en/news/2026/9/hc-wang-keynote)
- The 950PR launched in late March 2026, against its Q1 2026 target. [PR] — [DIGITIMES, 24 Mar 2026](https://www.digitimes.com/news/a20260324PD210/huawei-ascend-performance-2026.html)
- The 960DT and 960PR were moved earlier (claimed). [CO] — [Huawei, 17 Sept 2026](https://www.huawei.com/en/news/2026/9/hc-wang-keynote)

### Inferences
- **Why the 2025 volume figures differ.** The 200k (Commerce) figure and the about 800k (SemiAnalysis, Epoch) figure probably measure different things. Commerce spoke of "production capacity", apparently for domestically fabricated dies. The analysts count shipments that include TSMC-made dies drawn from a stockpile. No source reconciles the two. IDC's count of more than 300k Huawei units in H1 2025 alone already exceeds the 200k full-year figure.
- **2026 run-rate.** IDC's H1 2026 count of 572k annualizes to about 1.1M. Reaching the reported 1.5M for 2026 would require about 0.93M units in H2 (my arithmetic).
- **2025 plan against estimates.** The FT-reported plan of about 100k 910C for 2025 is far below SemiAnalysis's estimate of 653k 910C shipped. Either the plan was raised or the estimates count differently. The sources do not say.

### Gaps
- No reported yield for the 950PR or 950DT, and no 2026 yield report for SMIC N+2 or N+3 on Ascend.
- I did not see the WSJ article (claimed figure: 1.5M in 2026) or the original Bloomberg article (Sept 2025). I saw both only through relays.
- I found no estimates from Morgan Stanley or TrendForce research on Ascend shipments; the search quota ran out.
- I found no reported shipment total for 2026 to date beyond IDC's H1 figure.

---

## 3. Financials: Huawei group (2024, 2025, H1 2026) and labeled estimates for Ascend

### Takeaway
- **2025 (audited by KPMG):** revenue CNY 880.9B (+2.2%), net profit CNY 68B (+8.6%), R&D CNY 192.3B (21.8% of revenue).
- **H1 2026:** revenue CNY 467.82B (+9.55%), net profit about CNY 23.4–23.8B (about -36%), R&D CNY 121.38B (25.9%).
- **Segments, 2025:** ICT infrastructure CNY 375.0B, consumer CNY 344.5B, intelligent automotive CNY 45B, cloud (external) CNY 32.16B.

Huawei discloses no Ascend revenue or shipments. Third-party data points are shipment and share estimates (SemiAnalysis, Epoch, IDC, Bernstein) and reported card prices. I found no credible Ascend revenue estimate.

### Cited Findings
- **2025 annual report** (published 31 Mar 2026; all statements audited by KPMG):
  - Revenue CNY 880.9B (about US$126.0B at CNY 6.9906 per US$) and net profit CNY 68B.
  - R&D CNY 192.3B, or 21.8% of revenue; CNY 1.382T of R&D over ten years.
  - The narrative says computing "continued to seize AI opportunities" and that Huawei will build ecosystems around Ascend, Kunpeng and HarmonyOS.
  - Sabrina Meng (rotating chair): "In 2025, Huawei's overall performance remained steady."

  [CO, audited] — [Huawei, "Huawei Releases 2025 Annual Report", pub 31 Mar 2026](https://www.huawei.com/en/news/2026/3/annual-report-2025)
- **2025 growth rates:** revenue +2.2%, against +22.4% in 2024; Reuters noted this was the second-highest revenue on record. Net profit +8.6%; R&D about 22% of revenue (SCMP). [PR, citing the report] — [TrendForce, pub 1 Apr 2026](https://www.trendforce.com/news/2026/04/01/news-huawei-2025-r-cloud-revenue-slips/)
- **2025 segments** (from the annual report, via TrendForce):

  | Segment | 2025 revenue | YoY |
  |---|---|---|
  | ICT infrastructure | CNY 375.0B | +2.6% |
  | Consumer | CNY 344.5B | +1.6% |
  | Intelligent automotive solutions | CNY 45B | +72.1% |
  | Cloud computing (external customers) | CNY 32.16B | -3.5% |

  The digital power figure is not in that source. [CO via PR] — [TrendForce, 1 Apr 2026](https://www.trendforce.com/news/2026/04/01/news-huawei-2025-r-cloud-revenue-slips/)
- **2024 net profit:** CNY 62.6B, with 2025 profit up 8.6%. [PR] (excerpt) — [XtendedView](https://xtendedview.com/huawei-statistics/); [BigGo Finance](https://finance.biggo.com/news/5HmJRJ0B5edQG9E4UX8Z)
- **H1 2026** (semi-annual report released at the end of Aug 2026): revenue CNY 467.82B (+9.55%); net profit CNY 23.43B against CNY 37.05B a year earlier; R&D CNY 121.38B (+~25%, 25.9% of revenue). [CO via PR] — [TechNode, pub 1 Sept 2026](https://technode.com/2026/09/01/huawei-h1-revenue-rd-spending/). Reports based on Reuters give net profit as CNY 23.81B (-36%). [PR] (excerpt) — [TelecomLead](https://telecomlead.com/telecom-equipment/huawei-h1-2026-revenue-rises-9-6-to-69-6-billion-as-rd-spending-surges-25-2-127518)
- **Reported H1 2026 profit drivers:** costs rose faster than revenue, and memory-chip price increases squeezed the consumer business. [PR] (excerpt) — [BigGo Finance](https://finance.biggo.com/news/1126b4da-59ed-4a0b-add2-354ca642374e)
- **AP comparison:** AP compared Huawei revenue of "$126 billion" with NVIDIA's latest annual revenue of almost $216 billion (pub 29 June 2026). [PR] — [AP via WTOP](https://wtop.com/world/2026/06/nvidias-ai-chip-sales-in-china-stall-as-local-chipmakers-like-huawei-take-the-lead/)

**Ascend-specific data points (not disclosed by Huawei; labeled)**
- Shipment estimates: see §2 (SemiAnalysis, Epoch, IDC, Bloomberg, Reuters, WSJ, US Commerce).
- **China market-share estimates:**
  - Bernstein (via AP, 29 June 2026): in 2025 NVIDIA held about 40% of China's AI-chip market, "roughly matched by Huawei". The 2026 forecast is NVIDIA about 8% and Huawei about 50%. [AN] — [AP via WTOP](https://wtop.com/world/2026/06/nvidias-ai-chip-sales-in-china-stall-as-local-chipmakers-like-huawei-take-the-lead/)
  - IDC, H1 2026 by units: NVIDIA 34%, Huawei 28%. [AN] (excerpt) — [TradingView/Seeking Alpha](https://www.tradingview.com/news/seekingalpha:62d1b5de5094b:0-nvidia-s-china-ai-chip-market-share-falls-to-34-as-huawei-gains-ground-idc/)
- **Compute-share estimate (Epoch):**
  - 2026: Huawei about 0.88M H100-equivalents against NVIDIA about 23M, which is under 4%.
  - Memory-bandwidth-equivalent share: about 1.4% in 2026 and 3.5% in 2028.

  [AN] — [Epoch AI](https://epoch.ai/publications/huaweis-roadmap-to-2031)
- **Price data points:** the Reuters-sourced card prices for 2026 are listed in §2. Epoch uses a 950DT price of US$37,000. [PR-U]/[AN] — [TrendForce, 10 Sept 2026](https://www.trendforce.com/news/2026/09/10/news-chinese-ai-chipmakers-reportedly-hike-prices-on-hbm-costs-huawei-950dt-up-as-much-as-50/); [Epoch AI](https://epoch.ai/publications/huaweis-roadmap-to-2031)
- **Revenue:** I found no agency or analyst estimate of Ascend revenue. Some low-quality websites assert "US$12B" of Huawei AI-chip revenue in 2026 without a traceable primary source. Treat this as **unverified**, not as data. (excerpt) — [beri.net](https://www.beri.net/article/huawei-ai-chip-revenue-12-billion-nvidia-alternative); [aitechnews.in](https://aitechnews.in/huawei-ai-chip-2026-revenue-12-billion-nvidia-india/)

### Inferences
These are my own arithmetic, not sourced figures.
- **2024 revenue and profit implied by 2025 growth:** revenue ≈ CNY 862B (880.9 ÷ 1.022) and net profit ≈ CNY 62.6B (68 ÷ 1.086). H1 2025 revenue ≈ CNY 427.1B (467.82 ÷ 1.0955).
- **2024 segments implied by 2025 growth:** consumer ≈ CNY 339B, automotive ≈ CNY 26B, cloud (external) ≈ CNY 33.3B, ICT ≈ CNY 365.5B. These may differ from figures in the 2024 annual report if segments were restated, which I could not check.
- **Order-of-magnitude illustration only, not an estimate.** I multiplied Epoch's modeled 2026 mix by Reuters-reported card prices:
  - 750k × RMB 60–80k
  - 430k × RMB 90–110k
  - 320k × RMB 150–250k

  This gives a gross card value of very roughly RMB 130–190B. List prices are not realized revenue. System pricing, discounts and revenue recognition are unknown, and the volumes are themselves estimates. Do not present this as an Ascend revenue estimate.

### Gaps
- Cash and short-term investments, borrowings, operating cash flow and liability ratio for 2024 and 2025. The 2025 annual report PDF I found could not be parsed, and the press release omits them.
- 2024 R&D in absolute terms, and the 2024 segment figures as originally reported (not opened this session).
- Q1–Q3 2026 results: none found. Whether Huawei published any is unknown because the search quota ran out.
- Segment data for H1 2026 and 2025 digital power revenue.
- Any analyst estimate of Ascend revenue from Bernstein, Morgan Stanley or TrendForce.

---

## 4. Customers and contracts: hyperscalers and AI labs, telecom operators and state centers, domestic-chip policy, overseas

### Takeaway
- **Demand from Chinese hyperscalers and labs is documented, mostly through unnamed-source reports:**
  - ByteDance and Alibaba planning 950PR orders (Reuters, Mar 2026).
  - Huawei is ByteDance's largest domestic chip supplier (Reuters, Sept 2026).
  - DeepSeek plans to deploy at least 160k 950DT (Bloomberg, Sept 2026).
- **On-the-record customer claims:**
  - Zhipu's GLM-Image was trained on Ascend (Jan 2026).
  - DeepSeek V4 had day-0 Ascend support (Apr 2026).
- **China Mobile:** Ascend-based partners won some packages in China Mobile's 2025–26 AI-equipment tender, according to secondary reports.
- **Policy:** Beijing requires state-funded data centers to use domestic AI chips (Reuters, Nov 2025).
- **Overseas sales are small:**
  - Malaysia's Ascend announcement was retracted in May 2025.
  - Middle-East outreach (2025) produced no reported closed deal.
  - Eric Xu (Sept 2026): overseas supply is "quite limited".
  - Huawei Cloud's overseas launch of its Ascend 950 cluster service is scheduled for 30 Nov 2026.

### Cited Findings

**Chinese hyperscalers and AI labs**
- **ByteDance and Alibaba:** both are planning 950PR orders after customer testing went well. CUDA compatibility is the draw, and the raw-compute gain over the 910C is modest. Huawei, ByteDance and Alibaba did not comment. [PR-U] (Reuters 27 Mar 2026, relayed) — [TrendForce, 1 Apr 2026](https://www.trendforce.com/news/2026/04/01/news-huawei-2025-r-cloud-revenue-slips/)
- **ByteDance's suppliers:** Huawei "remains ByteDance's largest domestic chip supplier, followed by Cambricon and Iluvatar CoreX". [PR-U] (Reuters 10 Sept 2026) — [TrendForce, 10 Sept 2026](https://www.trendforce.com/news/2026/09/10/news-chinese-ai-chipmakers-reportedly-hike-prices-on-hbm-costs-huawei-950dt-up-as-much-as-50/)
- **After DeepSeek V4 (Reuters, 29 Apr 2026):** ByteDance, Tencent and Alibaba reopened talks with Huawei about new orders. [PR-U] (excerpt) — [Technology.org, pub 29 Apr 2026](https://www.technology.org/2026/04/29/huawei-ascend-950-orders-surge-as-deepseek-v4-drives-chinese-cloud-giants-to-buy/). Secondary sites claim ByteDance will spend more than US$5.6B on Ascend in 2026. **Unverified:** I found no primary Reuters or CNBC text. (excerpt) — [The AI Consulting Network](https://www.theaiconsultingnetwork.com/blog/huawei-950pr-cuda-ai-chip-china-data-center-cre-investors-2026)
- **DeepSeek:**
  - Huawei announced "day zero" support for DeepSeek V4 on its Ascend supernode platform on 24 Apr 2026. [CO] (excerpt; the date comes from search-result summaries of V4 coverage, and the outlet that originated it was not confirmed). Tom's Hardware's headline reads "DeepSeek launches 1.6 trillion parameter V4 on Huawei chips"; only the headline was readable. — [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/deepseek-launches-1-6-trillion-parameter-v4-on-huawei-chips-as-us-escalates-ai-theft-accusations); [Tech Insider](https://tech-insider.org/deepseek-v4-huawei-ascend-1-6-trillion-parameter-moe-2026/) (not opened)
  - AP: V4, rolled out in April 2026, "was adapted for Huawei's Ascend chips". [PR] — [AP via WTOP, 29 June 2026](https://wtop.com/world/2026/06/nvidias-ai-chip-sales-in-china-stall-as-local-chipmakers-like-huawei-take-the-lead/)
  - Bloomberg (4 Sept 2026): DeepSeek plans to deploy at least 160,000 Ascend 950DT, mainly for inference, at a data center under construction in Inner Mongolia. [PR-U] — [TrendForce, 10 Sept 2026](https://www.trendforce.com/news/2026/09/10/news-chinese-ai-chipmakers-reportedly-hike-prices-on-hbm-costs-huawei-950dt-up-as-much-as-50/); [Channel Insider](https://www.channelinsider.com/ai/news-deepseek-huawei-ai-chips-data-center-apac-china/)
  - The Information (Nov 2026): Huawei is working with DeepSeek to optimize the 960DT for pre-training. [PR-U] — [TrendForce, 3 Nov 2026](https://www.trendforce.com/news/2026/11/03/news-china-reportedly-obtains-smuggled-hbm-via-server-packages-huawei-960dt-faces-domestic-hbm-shortage/)
- **Zhipu (Z.ai), GLM-Image (14 Jan 2026):**
  - Zhipu says the full pipeline, from data preparation to the final run, ran on Huawei Ascend Atlas 800T A2 servers with MindSpore.
  - It did not disclose the chip count or training time.
  - The weights are released on Hugging Face, GitHub and ModelScope.

  [CUST] (excerpt) — [InfoWorld](https://www.infoworld.com/article/4116787/chinese-ai-firm-trains-state-of-the-art-model-entirely-on-huawei-chips.html); [Network World](https://www.networkworld.com/article/4116791/chinese-ai-firm-trains-state-of-the-art-model-entirely-on-huawei-chips-3.html); [SCMP](https://www.scmp.com/tech/tech-war/article/3339869/zhipu-ai-breaks-us-chip-reliance-first-major-model-trained-huawei-stack). Model size: 16B total, per Decrypt; or a 9B autoregressive model plus a 7B diffusion decoder, per InfoWorld. (excerpt) — [Decrypt](https://decrypt.co/354590/china-zai-releases-ai-image-generation-model-trained-without-american-chips?amp=1)
- **NVIDIA's China position (AP, 29 June 2026):** Jensen Huang said NVIDIA had "about 95% market share" in China before export controls. He described Chinese competitors as having become "giants". NVIDIA had "yet to generate any revenue" from H200 sales in China. [PR, on-record] — [AP via WTOP](https://wtop.com/world/2026/06/nvidias-ai-chip-sales-in-china-stall-as-local-chipmakers-like-huawei-take-the-lead/)

**Telecom operators and state computing centers**
- **China Mobile 2025–26 AI computing-equipment tender:**
  - The first four packages went to ZTE, H3C and Inspur.
  - The last two went to Ascend-based Huawei partners, including Henan Kunlun, Huakun and (in one report) Wuhan Yangtze Computing.
  - The tender included a CANN-ecosystem package tied to Ascend.

  [PR] (excerpt) — [Huawei Central](https://www.huaweicentral.com/?p=144690)
- **Separate China Mobile Ascend purchase:** reported as about US$22M of chips and servers for provincial computing centers and 5G-A inference nodes. Reports disagree on whether these are 910B or 910C chips. A Russian outlet put a related figure at "CNY 1.55 billion", which is inconsistent with the US$22M figure. [PR] (excerpt) — [LAVX News](https://news.lavx.hu/article/china-mobile-invests-22m-in-domestic-compute-platform-powered-by-huawei-ascend); [Rutab, pub 7 Feb 2026](https://rutab.net/b/hardware/2026/02/07/kitayskiy-operator-china-mobile-zakupit-oborudovanie-huawei-na-155-mlrd-yuaney-otkazavshis-ot-resheniy-nvidia.html)
- **Larger China Mobile procurement:** a separate procurement worth more than CNY 5B went mainly to ZTE and H3C. [PR] (excerpt) — same search set; [MLex, "China's telecom giants step up AI chip push", pub 22 Oct 2025](https://www.mlex.com/mlex/articles/2402297/china-s-telecom-giants-step-up-ai-chip-push-as-beijing-seeks-tech-independence) (headline only; paywalled)

**Chinese government policy on domestic chips**
- **State-funded data centers (Reuters, 5 Nov 2025):**
  - Beijing guidance requires state-funded data-center projects to use only domestic AI chips.
  - Projects less than 30% complete must remove foreign chips.
  - Domestic beneficiaries named include Huawei, Cambricon, MetaX, Moore Threads and Enflame.
  - Since 2021, more than US$100B of state funding has gone to AI data-center projects.

  [PR-U] (excerpt) — [Tom's Hardware](https://www.tomshardware.com/tech-industry/semiconductors/china-bans-foreign-ai-chips-from-state-funded-data-centers); [Business Standard](https://www.business-standard.com/world-news/china-bans-restricts-nvidia-foreign-ai-chips-data-centres-125110501115_1.html)
- **NVIDIA purchase restrictions** (CAC summons in Aug 2025; customs block on the H200 in Jan 2026): see §7.

**Overseas**
- **Malaysia (May 2025):**
  - Deputy Communications Minister Teo Nie Ching announced a deployment of 3,000 Huawei Ascend-powered AI servers by 2026, with an initial cloud run by Skyvast.
  - The remarks were retracted within about a day, with no reason given.
  - A Huawei spokesman said no Ascend chips had been sold in Malaysia and the government had not bought any.

  [PR] — [Malay Mail, pub 21 May 2025](https://www.malaymail.com/news/malaysia/2025/05/21/malaysia-walks-back-huawei-ai-project-amid-us-china-tech-tensions/177551); [SCMP](https://www.scmp.com/tech/big-tech/article/3311363/tech-war-malaysia-walks-back-ai-project-huawei-tech-giant-denies-chip-exports) (excerpt)
- **Middle East and Southeast Asia (mid-2025):**
  - Huawei approached potential buyers in the UAE, Saudi Arabia and Thailand about the 910B.
  - No deals were finalized, and UAE parties had shown no interest.
  - One person described talks with Saudi Arabia's SDAIA as advanced; SDAIA declined to comment.
  - Huawei also offered remote access to CloudMatrix 384.

  [PR-U] (excerpt; secondary sources differ on whether Bloomberg or Reuters was the original) — [SCMP](https://www.scmp.com/tech/big-tech/article/3317966/huawei-eyes-export-ai-chips-middle-east-southeast-asia-rival-nvidia); [DealStreetAsia, pub 11 July 2025](https://media.dealstreetasia.com/stories/huawei-seeks-ai-chip-deals-in-middle-east-se-asia-448903)
- **Huawei, 17 Sept 2026:** no plan "to expand to the international market in a fully-fledged way". Some countries have strong demand, and Huawei is "providing some supply to those countries", but "the volume is quite limited". [CO] — [Huawei roundtable summary](https://www.manilatimes.net/2026/09/30/tmt-newswire/media-outreach-newswire/huawei-pioneers-a-new-computing-architecture-for-the-ai-era-making-one-million-processors-work-as-one-computer-summary-of-roundtable-meeting-between-eric-xu-and-international-media-outlets-on-september-17/2436416)
- **Huawei Cloud:** the Ascend 950 cluster service launches overseas on 30 Nov 2026 (**pending** as of 14 Nov 2026). [CO] — [TechNode, 18 Sept 2026](https://technode.com/2026/09/18/huawei-sets-commercial-launch-dates-for-ascend-950-ai-cluster-cloud-service/). TheNextWeb reports that Pakistan's Sky47 built a national AI cloud on Huawei Cloud Stack, without specifying the chips. [PR] — [TheNextWeb](https://thenextweb.com/news/huawei-connect-2026-ascend-960-superpod-unifiedbus)

### Inferences
- Most evidence of customer volumes comes from reports citing unnamed sources (Reuters, Bloomberg, The Information). On-the-record confirmations are limited to Huawei, Zhipu, AP's description of DeepSeek V4, and procurement-portal relays.
- China's policy (domestic chips in state-funded data centers) and its restrictions on NVIDIA purchases are consistent with the reported demand pull toward Ascend. Eric Xu's capacity statement and the price increases indicate that supply, not demand, was the binding limit in 2026.

### Gaps
- iFlytek, Baidu, SiliconFlow and Tencent: no details of Ascend contracts were verified in this session.
- China Telecom and China Unicom tenders for Ascend: not found.
- The Ascend share of China Mobile tender values (package values were not obtained).
- Signed contract values for any hyperscaler: none found.
- Any Middle-East Ascend deployment actually completed by Nov 2026: none found.
- Whether Huawei's Europe push in Oct 2026 includes Ascend: not verified.

---

## 5. Capacity: SMIC, Huawei-affiliated fabs, TSMC dies via Sophgo, HBM and packaging, and US estimates of output

### Takeaway
Huawei's 2024–25 output relied heavily on a stock of TSMC-made Ascend dies obtained through intermediaries:
- More than 2M, per CSIS citing officials (Mar 2025).
- More than 2.9M, per SemiAnalysis (Sept 2025).
- TechInsights teardowns found TSMC dies in the 910B (Oct 2024) and in 910C samples, alongside Samsung and SK hynix HBM (Oct 2025).

SMIC's 7nm-class N+2 and N+3 are the domestic route. TechInsights says N+3 is not viable for large data-center AI dies. HBM is the binding constraint: a stockpile of about 13M foreign stacks is running down in 2026, CXMT's HBM3E yields are reported at 20–30%, and smuggling is reported.

### Cited Findings

**SMIC and process technology**
- **SemiAnalysis (Sept 2025):**
  - SMIC advanced-node (7nm and below) capacity of about 45k wafers per month by the end of 2025, about 60k in 2026 and about 80k in 2027.
  - Ascend needs at most about 20k wafers per month.
  - In 2025 SMIC produced about 1M 910C and "almost half a million" 910B. The report does not reconcile this with its 805k shipment figure.

  [AN] — [SemiAnalysis](https://newsletter.semianalysis.com/p/huawei-ascend-production-ramp)
- **TechInsights (11 Dec 2025):** the Kirin 9030 is made on SMIC N+3, "a scaled evolution of its 7nm-class technology". N+3 "remains significantly less scaled" than TSMC's and Samsung's 5nm. [IND: TechInsights teardown] — [TechInsights](https://www.techinsights.com/blog/smic-n3-confirmed-kirin-9030-analysis-reveals-how-close-smic-5nm); [Tom's Hardware](https://www.tomshardware.com/tech-industry/semiconductors/huaweis-latest-mobile-is-chinas-most-advanced-process-node-to-date-despite-using-blacklisted-chipmaker-huawei-kirin-9030-mobile-soc-made-on-smic-n-3-process-but-cant-compete-with-5nm-nodes) (excerpt)
- **TechInsights (17 Mar 2026):** N+3 "will not be a viable solution for data center AI chips" because of low yields. [IND: TechInsights analysis] — [TechInsights](https://www.techinsights.com/ko/node/61228)
- **Epoch AI:**
  - SMIC is limited to a 5–7nm-class process through about 2030.
  - N+3 is about 113 MTr/mm², against TSMC N3P at about 224. N+4 is expected to add about 20%.
  - Huawei's "LogicFolding" plan (two stacked 5nm-class layers, aiming at about 1.4nm-equivalent density by 2031) depends on unproven advances.

  [AN] — [Epoch AI](https://epoch.ai/publications/huaweis-roadmap-to-2031)
- **Which process the 950 uses:** a Taiwanese outlet's headline says the Ascend 950 uses SMIC N+3 and self-developed HBM. Huawei has not named the foundry. [PR, unconfirmed] (excerpt) — [TechNews (Taiwan)](https://technews.tw/?p=1483821)
- **The 910C process:** widely reported as SMIC 7nm N+2. [PR] (excerpt) — [TrendForce, 25 Feb 2025](https://www.trendforce.com/news/2025/02/25/news-china-advances-in-ai-chips-huawei-reportedly-boosts-yield-to-40-making-ascend-line-profitable/)

**Huawei-affiliated fabs and equipment**
- **SemiAnalysis:** Huawei's wafer-fab equipment spending was US$7.3B in 2024 (+27%). Huawei has bought more than US$9B of tools, and SiCarrier raised US$2.8B. [AN] — [SemiAnalysis](https://newsletter.semianalysis.com/p/huawei-ascend-production-ramp)
- **Entity List, Dec 2024:** BIS added 140 entities, among them Shenzhen SiCarrier, SwaySure and Si'En Qingdao, with a presumption of denial. A compliance database lists SiCarrier's aliases as including "Huawei Starlight Department" and "Shenzhen Xinkailai". [GOV] (excerpt) — [Federal Register, pub 5 Dec 2024, doc 2024-28267](https://www.federalregister.gov/documents/2024/12/05/2024-28267/additions-and-modifications-to-the-entity-list-removals-from-the-validated-end-user-veu-program); [FEOC database entry](https://feoc-platform.vercel.app/entity/d9b7705b-13c8-426c-839e-dffd992abf0d)

**TSMC-made dies via Sophgo**
- **CSIS (Mar 2025)**, citing government officials: TSMC manufactured more than 2M Ascend 910B logic dies, "all of these are now with Huawei". That is enough for about 1M 910C. [AN citing GOV officials] (excerpt) — [TechPowerUp, 10 Mar 2025](https://techpowerup.com/333877/huawei-obtained-two-million-ascend-910b-dies-from-tsmc-via-shell-companies-to-circumvent-us-sanctions); [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/huawei-reportedly-acquired-two-million-ascend-910-ai-chips-from-tsmc-last-year-through-shell-companies)
- **SemiAnalysis (Sept 2025):** Huawei "received more than 2.9M Ascend die" made at TSMC, usable for the 910B or 910C. This "die bank" was expected to run out "within the next 9 months". [AN] — [SemiAnalysis](https://newsletter.semianalysis.com/p/huawei-ascend-production-ramp)
- **Epoch:** Huawei reportedly bought about US$500M of 7nm wafers from TSMC in 2024 through the shell company Sophgo. [AN, citing reports] — [Epoch AI](https://epoch.ai/publications/huaweis-roadmap-to-2031)
- **Reuters (8 Apr 2025):** TSMC could face a penalty of US$1B or more in a Commerce investigation of its work for Sophgo. TSMC said it has not supplied Huawei since mid-Sept 2020 and is cooperating. Sophgo said the probe does not involve it. [PR-U] (excerpt) — [Taipei Times, pub 9 Apr 2025](https://www.taipeitimes.com/News/taiwan/archives/2025/04/09/2003834894); [SCMP](https://www.scmp.com/tech/big-tech/article/3305763/tsmc-could-face-us1-billion-fine-over-chip-found-huawei-ai-processor-sources-say)
- **Sophgo on the Entity List (16 Jan 2025):** BIS added Sophgo Technologies Ltd. (China) and Sophgo Technologies Pte. Ltd. (Singapore). The stated reasons are "supporting or directly contributing to the development of advanced computing integrated circuits" and posing "a risk of diversion to Huawei". [GOV] — [Federal Register, 90 FR, doc 2025-00480, pub 16 Jan 2025](https://www.govinfo.gov/content/pkg/FR-2025-01-16/html/2025-00480.htm)
- **TechInsights 910C teardown (Bloomberg, 3 Oct 2025):** found TSMC dies packaged with "last-gen" HBM from Samsung and SK hynix. TSMC said the die was the same one "analyzed by this organization in October 2024", and that production and sales "have been halted since then". [IND: TechInsights; via PR] — [Notebookcheck, pub 3 Oct 2025](https://www.notebookcheck.net/TSMC-die-and-Samsung-memory-confirmed-in-Huawei-910C-set-to-replace-Nvidia-AI-chips.1130790.0.html); [Bloomberg Government](https://news.bgov.com/tech-and-telecom-law/huawei-used-tsmc-samsung-sk-hynix-components-in-top-ai-chips) (headline)

**HBM and packaging**
- **SemiAnalysis:**
  - Samsung supplied 11.4M HBM stacks to China, 7M of them in the month between the announcement of the US control (2 Dec 2024) and its enforcement.
  - China procured 13M stacks in total, enough for 1.6M 910C packages.
  - CXMT is expected to make about 2M HBM stacks in 2026, enough for 250–300k 910C.
  - Chinese assembly and test firms (JCET, Tong Fu) are building through-silicon-via (TSV) capacity.

  [AN] — [SemiAnalysis](https://newsletter.semianalysis.com/p/huawei-ascend-production-ramp)
- **Epoch:**
  - About 13M HBM stacks were stockpiled in late 2024, enough for roughly 1–2M Ascend chips. The stockpile is expected to run out in 2026.
  - CXMT's HBM wafer starts are projected to grow from 5k per month (end-2025) to 30k (2026), 55k (2027) and 100k (2028).

  [AN] — [Epoch AI](https://epoch.ai/publications/huaweis-roadmap-to-2031)
- **Reuters (Nov 2026):** CXMT's HBM3E yields are about 20–30%, against about 70% at SK hynix. [PR-U] — [TrendForce, 3 Nov 2026](https://www.trendforce.com/news/2026/11/03/news-china-reportedly-obtains-smuggled-hbm-via-server-packages-huawei-960dt-faces-domestic-hbm-shortage/)
- **The Information (Nov 2026):**
  - Smugglers ship HBM packaged with low-end processors. In China, the stacks are removed by heating the solder, and the processors are discarded.
  - This memory "often ends up with Huawei customers".

  [PR-U] — [TrendForce, 3 Nov 2026](https://www.trendforce.com/news/2026/11/03/news-china-reportedly-obtains-smuggled-hbm-via-server-packages-huawei-960dt-faces-domestic-hbm-shortage/)
- **Packaging yield:** CSIS reports about 75% of 910C packages survive (see §2). Epoch assumes 80% packaging yield. [AN] — [Epoch AI](https://epoch.ai/publications/huaweis-roadmap-to-2031)

**US government estimates of output**
- **Kessler (12 June 2025):** 200,000 or fewer in 2025 (§2). [GOV] — [Bloomberg](https://www.bloomberg.com/news/articles/2025-06-12/us-says-huawei-s-2025-output-is-no-more-than-200-000-ai-chips). EE Times linked the testimony to a proposed 133% increase in BIS's enforcement budget. [PR] (excerpt) — [EE Times](https://www.eetimes.com/ai-chip-controls-smuggling-and-geopolitics/)

### Inferences
- The TSMC dies (about 2–2.9M) roughly match the volumes analysts estimate for 2024–25 (507k + 805k units, with the 910C using two dies). For 2024–25 output, the binding inputs therefore appear to have been foreign dies and foreign HBM. From 2026, domestic N+2/N+3 dies and domestic or smuggled HBM must carry production.
- Logic capacity, at 20k or fewer of SMIC's 45–60k wafers per month (SemiAnalysis), looks less binding than HBM. That is consistent with Huawei citing memory when it raised prices in 2026.

### Gaps
- Status of Pengxinwei (PXW) and other suspected Huawei fabs on the Entity List: not confirmed in this session.
- I found no Entity List additions in 2026 that target Huawei fabs.
- Any measured SMIC N+3 yield or Ascend wafer allocation for 2026.
- The original CSIS text: I relied on relays.
- Any US government estimate of Huawei output for 2026: none found.

---

## 6. Ownership and key people

### Takeaway
Huawei Investment & Holding is owned through an employee shareholding scheme. Huawei says founder Ren Zhengfei's stake is about 0.59% as of 31 Dec 2025. The rotating chair moved from Sabrina Meng (Oct 2025–Mar 2026) to David Wang (Apr–Sept 2026), and Eric Xu holds it from 1 Oct 2026 to 31 Mar 2027.

The operating leaders named in 2025–26 sources are:
- Zhang Dixuan: Ascend Computing Business.
- Seaway Zhang: Computing Product Line.
- Zhou Yuefeng: Huawei Cloud CEO.
- He Tingbo: semiconductor business.

### Cited Findings
- **Ren Zhengfei's stake:** his investment is "nearly 0.59%" of total share capital as of 31 Dec 2025. [CO] (excerpt) — [Huawei, Company facts](https://www.huawei.com/br/media-center/company-facts/)
- **Rotating chairs:**
  - Sabrina Meng (Meng Wanzhou): 1 Oct 2025 to 31 Mar 2026. [CO] (excerpt) — [Huawei notice, Sept 2025](https://www.huawei.com/en/news/2025/9/rotating-chair-tenure)
  - David Wang (Wang Tao): 1 Apr to 30 Sept 2026. He joined Huawei in 1997 and previously chaired the ICT infrastructure board. 2026 reporting described the three deputy and rotating chairs as Eric Xu, Sabrina Meng and David Wang. [CO] (excerpt) — [Huawei notice, Mar 2026](https://www.huawei.com/en/news/2026/3/rotating-chair-tenure); [Converge Digest](https://convergedigest.com/huawei-names-david-wang-as-rotating-chair-succeeding-sabrina-meng/); [Huawei Central](https://www.huaweicentral.com/huawei-rotates-chairman-for-2026-after-posting-annual-profit-jump/)
  - Eric Xu (Xu Zhijun): rotating and acting chairman from 1 Oct 2026 to 31 Mar 2027. He heads the Board and its Executive Committee during the term, is Deputy Chairman, and joined Huawei in 1993. [CO] — [Huawei notice](https://www.huawei.com/en/news/2026/9/rotating-chairman)
- **Zhang Dixuan:** "President of Huawei's Ascend Computing Business" (d: 20 Sept 2025). [CO] — [Huawei](https://www.huawei.com/en/news/2025/9/hc-shengten-opensource)
- **Seaway Zhang:** "President of Huawei's Computing Product Line" (d: 2 Mar 2026). [CO] — [Huawei, MWC 2026](https://www.huawei.com/en/news/2026/3/mwc-superpod-ai)
- **Zhou Yuefeng:** Huawei Cloud CEO (d: 17–18 Sept 2026). He succeeded Zhang Ping'an; the date of the change was not captured. [PR] — [TechNode, 18 Sept 2026](https://technode.com/2026/09/18/huawei-sets-commercial-launch-dates-for-ascend-950-ai-cluster-cloud-service/)
- **He Tingbo:** head of Huawei's semiconductor business (d: June 2026). She said: "We have found pretty good solutions." [PR] — [AP via WTOP](https://wtop.com/world/2026/06/nvidias-ai-chip-sales-in-china-stall-as-local-chipmakers-like-huawei-take-the-lead/)
- **Yang Chaobin:** runs Huawei's ICT business group (d: Sept 2026). [PR] — [TheNextWeb](https://thenextweb.com/news/huawei-connect-2026-ascend-960-superpod-unifiedbus)
- **Liao Heng:** spoke for Huawei on SuperCluster scale at the 17 Sept 2026 roundtable; his title is not given in the source. He is also the last author of the CloudMatrix384 paper. [CO] — [Huawei roundtable summary](https://www.manilatimes.net/2026/09/30/tmt-newswire/media-outreach-newswire/huawei-pioneers-a-new-computing-architecture-for-the-ai-era-making-one-million-processors-work-as-one-computer-summary-of-roundtable-meeting-between-eric-xu-and-international-media-outlets-on-september-17/2436416); [arXiv 2506.12708](https://arxiv.org/abs/2506.12708)

### Inferences
- If Ren holds about 0.59%, the employee scheme through the Union holds the remaining roughly 99.4%. This is my arithmetic; I did not see the annual report's statement of the Union's stake.
- Ken Hu does not appear among the three rotating chairs named in 2026 reporting. I did not find when or whether that changed.

### Gaps
- The Union of Huawei Investment & Holding's exact percentage and the number of employee shareholders at year-end 2025: not obtained.
- Chairman of the board (Liang Hua, per my memory): not verified.
- When and whether Ken Hu left the rotating-chair rotation.
- Whether Zhang Dixuan still holds the Ascend role in late 2026.

---

## 7. Legal and regulatory: US and China measures, and developments in 2026

### Takeaway
- **US measures:** the Entity List (effective 16 May 2019), the foreign direct product rule (May 2020, expanded 17/20 Aug 2020), listings of Huawei-linked fabs (Dec 2024) and of Sophgo (16 Jan 2025), and BIS's 13 May 2025 guidance. That guidance created a presumption that any activity involving the Ascend 910B, 910C or 910D violates General Prohibition 10. The TSMC/Sophgo probe has no public resolution that I could find.
- **The Brooklyn trial:** the US criminal case against Huawei (racketeering, Iran sanctions, bank fraud, trade secrets) went to trial on 8 Sept 2026. It was in the defense case in early Nov 2026, with no verdict reported as of 10 Nov 2026.
- **China:** restricted NVIDIA purchases (CAC summonses in Aug 2025; customs block on the H200 in Jan 2026) and required domestic chips in state-funded data centers (Nov 2025).

### Cited Findings

**United States**
- **Entity List (2019):** "Addition of Entities to the Entity List" (84 FR 22961, published 21 May 2019, effective 16 May 2019). It added Huawei Technologies Co., Ltd. and 68 non-US affiliates in 26 destinations. The license requirement covers all items subject to the EAR, with a presumption of denial. [GOV, primary] — [Federal Register via govinfo](https://www.govinfo.gov/content/pkg/FR-2019-05-21/html/2019-10616.htm)
- **Foreign direct product rule (2020):** 85 FR 51596 (published 20 Aug 2020, effective 17 Aug 2020).
  - It added 38 more Huawei non-US affiliates.
  - It expanded the footnote-1 foreign direct product rule beyond the 15 May 2020 rule, to cover items destined to be incorporated into parts, components or equipment ordered by listed Huawei entities, and transactions in which they are a party.
  - It removed the requirement that the item be produced from a Huawei design.
  - It stated that foreign-produced wafers, finished or unfinished, are controlled.

  [GOV, primary] — [Federal Register via govinfo](https://www.govinfo.gov/content/pkg/FR-2020-08-20/html/2020-18213.htm)
- **Dec 2024:** 140 entities added, including SiCarrier, SwaySure and Si'En Qingdao; see §5. [GOV] — [Federal Register, 5 Dec 2024](https://www.federalregister.gov/documents/2024/12/05/2024-28267/additions-and-modifications-to-the-entity-list-removals-from-the-validated-end-user-veu-program)
- **16 Jan 2025:** Sophgo added, citing "risk of diversion to Huawei". [GOV, primary] — [Federal Register](https://www.govinfo.gov/content/pkg/FR-2025-01-16/html/2025-00480.htm)
- **13 May 2025 BIS guidance** (issued with the rescission of the AI Diffusion Rule):
  - The Ascend 910B, 910C and 910D are presumed subject to General Prohibition 10. Any activity involving them that lacked prior authorization is presumed to violate it, because the chips were likely developed or produced in violation of US controls.
  - The list is "illustrative".
  - BIS language says use "risks violating" US controls.

  [GOV] (excerpt; BIS PDF not machine-readable in this session) — [Arnold & Porter](https://www.arnoldporter.com/en/perspectives/advisories/2025/05/commerce-new-guidance-curb-adversaries-access-to-advanced-ai-tech); [Crowell & Moring](https://www.crowell.com/en/insights/client-alerts/us-department-of-commerce-rescinds-biden-administrations-ai-diffusion-export-control-rule-and-issues-new-guidance-on-huawei-chips-for-ai-purposes-and-diligence-expectations); [Gibson Dunn](https://www.gibsondunn.com/bis-initiates-rescission-of-ai-diffusion-framework-issues-strong-ai-and-advanced-ic-guidance-and-warnings-more-to-come/); [BIS](https://www.bis.gov/media/1575)

  The initial "anywhere in the world" wording "later softened". [PR] — [Malay Mail, 21 May 2025](https://www.malaymail.com/news/malaysia/2025/05/21/malaysia-walks-back-huawei-ai-project-amid-us-china-tech-tensions/177551)
- **TSMC/Sophgo probe:** Reuters (Apr 2025) reported a potential penalty of US$1B or more (§5). I found no BIS charging letter or settlement in the sources I could reach. Notebookcheck's updated page (dated 5 Oct 2026 in metadata) asserts that "TSMC was fined $1 billion". That claim is **unverified and uncorroborated** by any government or Reuters source I saw. — [Notebookcheck](https://www.notebookcheck.net/TSMC-die-and-Samsung-memory-confirmed-in-Huawei-910C-set-to-replace-Nvidia-AI-chips.1130790.0.html)
- **US v. Huawei** (US District Court, EDNY, Brooklyn; Judge Ann M. Donnelly):
  - Jury selection began on 8 Sept 2026. [PR] (excerpt) — [TechTimes, pub 7 Sept 2026](https://www.techtimes.com/articles/326904/20260907/huawei-rico-trial-opens-tuesday-us-makes-telecom-giant-answer-criminal-enterprise.htm); [China Strategy, pub 8 Sept 2026](https://www.chinastrategy.org/2026/09/08/huawei-goes-on-trial-in-us-for-racketeering-after-nearly-decade-of-litigation/); [Ruibao](https://ruibao.news/huawei-us-criminal-trial-jury-selection-september-8-2026-en/)
  - The charges include racketeering, bank fraud, trade-secret theft, Iran sanctions evasion (the Skycom allegations), money laundering and obstruction. Huawei pleaded not guilty and called the government's narrative "demonstrably false". Donnelly rejected Huawei's 2025 bid to dismiss the main charges. [PR] (excerpt) — same sources.
  - Trial Day 31 was 3 Nov 2026. Donnelly demoted five government exhibits linked to FBI forensic accountant Jennifer Moon to "demonstratives". In June 2026 she ruled Meng Wanzhou's 2021 deferred-prosecution-agreement statements admissible. The defense "may rest the week of November 9", with possibly one day of rebuttal. No verdict was reported as of the post date. The writer counts "12 felony counts". [PR] — [Strategic Narratives, "Huawei on trial, #6", pub 10 Nov 2026](https://www.strategicnarratives.org/p/huawei-on-trial-6)
  - One outlet in the search results reported 14 counts, but the excerpt did not identify which outlet, so this is unverified. Quartz's trial story returned HTTP 403 when opened. — [Quartz](https://qz.com/huawei-racketeering-trial-brooklyn-iran-sanctions-090826) (not read)
  - None of the trial coverage I saw mentions Ascend or export-control charges. [PR] — [Strategic Narratives](https://www.strategicnarratives.org/p/huawei-on-trial-6)
- **2026 US AI-chip policy on China** (bears on the competition Ascend faces):
  - The administration formally approved H200 sales to China with conditions: third-party lab review, China volumes capped at 50% of US-customer volumes, a certification of US supply, and customer security requirements. [PR-U/PR] — [Taipei Times (Reuters), pub 15 Jan 2026](https://www.taipeitimes.com/News/biz/archives/2026/01/15/2003850605)
  - NVIDIA said it had not sold H200s in China (d: June 2026). [PR] — [AP via WTOP](https://wtop.com/world/2026/06/nvidias-ai-chip-sales-in-china-stall-as-local-chipmakers-like-huawei-take-the-lead/)
  - A senior Trump administration official claimed DeepSeek V4 was trained on smuggled Blackwell chips. DeepSeek denied it, and NVIDIA called it "far-fetched". [PR, relayed] — [Implicator.ai](https://www.implicator.ai/deepseeks-huawei-chip-training-claim-finally-gets-its-benchmarks-and-its-doubters/). Tom's Hardware's headline says "U.S. gov't alleges IP theft by DeepSeek and other Chinese AI firms". [PR] The publication date was not captured; it coincides with V4's launch in Apr 2026. — [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/deepseek-launches-1-6-trillion-parameter-v4-on-huawei-chips-as-us-escalates-ai-theft-accusations)

**China**
- **Aug 2025:** the Cyberspace Administration of China (CAC) summoned Tencent, ByteDance, Baidu and others over H20 purchases, asking them to justify the transactions. [PR-U] (Reuters, relayed) — [TrendForce, 14 Aug 2025](https://www.trendforce.com/news/2025/08/14/news-deepseek-r2-model-launch-reportedly-delayed-amid-huawei-ascend-chip-hurdles/)
- **Nov 2025:** state-funded data centers must use domestic AI chips (§4). [PR-U] — [Tom's Hardware](https://www.tomshardware.com/tech-industry/semiconductors/china-bans-foreign-ai-chips-from-state-funded-data-centers)
- **Jan 2026:**
  - Chinese customs told agents that H200 chips "are not permitted to enter China".
  - Officials told tech firms not to buy them unless necessary ("basically a ban for now").
  - Exemptions for university research and development were being discussed.
  - Chinese firms had reportedly ordered more than 3M H200s at about US$27k each.

  [PR-U] — [Taipei Times (Reuters), 15 Jan 2026](https://www.taipeitimes.com/News/biz/archives/2026/01/15/2003850605); [Tom's Hardware](https://www.tomshardware.com/tech-industry/chinese-customs-told-to-block-h200-imports-report-claims-directive-would-effectively-ban-the-nvidia-ai-chip-from-china) (excerpt)
- **June 2026:** Beijing "switched to encouraging domestically designed chips", and its public stance on H200 imports was unclear. [PR] — [AP via WTOP](https://wtop.com/world/2026/06/nvidias-ai-chip-sales-in-china-stall-as-local-chipmakers-like-huawei-take-the-lead/)
- **Nov 2026 (FT):** NVIDIA told cloud partners that at least 51% of their services must be sold to non-Chinese companies. This is NVIDIA's own policy, not a Chinese rule. [PR-U] — [TrendForce, 3 Nov 2026](https://www.trendforce.com/news/2026/11/03/news-china-reportedly-obtains-smuggled-hbm-via-server-packages-huawei-960dt-faces-domestic-hbm-shortage/)

### Inferences
- The BIS guidance raises legal risk for any user of Ascend outside China. The withdrawn Malaysian announcement (May 2025) and Huawei's limited overseas supply (Sept 2026) are consistent with that risk shaping overseas uptake. No source states the causation.

### Gaps
- Trial status after 10 Nov 2026, including any verdict or jury deliberation as of 14 Nov 2026. The search quota ran out.
- The original 2024 scheduling of the trial (an early-2026 date was reported) and why it moved to Sept 2026: not verified.
- Final status of the TSMC/Sophgo probe: no BIS charging letter or settlement found.
- Text of BIS's 13 May 2025 guidance: the PDF was not readable here. Any later amendment: not checked.
- Any 2026 BIS rule or entity listing specific to Ascend.
- Status of the "affiliates rule" and related suspensions.
- China's RTX Pro 6000D purchase ban and the SAMR antitrust finding against NVIDIA in 2025: not verified this session.
- The content of the House Select Committee's 18 July 2025 letter to Commerce: seen in search results only.

---

## 8. Science and engineering: what has been demonstrated, who verified it, what is unproven, which limits apply, and whether it stands on solid ground

### Takeaway
**Demonstrated, with independent corroboration:**
- Huawei can field large scale-up systems: the CloudMatrix 384 / Atlas 900 A3 (384 × 910C, about 300 PFLOPS BF16), whose system-level specs SemiAnalysis's analysis accepts.
- Production LLM inference on Ascend at scale: DeepSeek V4 day-0 support, customer deployments, and Huawei's CloudMatrix384 serving paper (company-authored).
- Post-training of DeepSeek V4-Pro on at least 1,000 910C. This is Huawei-led, with an MFU of 34.22% self-reported.

**Not demonstrated independently:**
- Frontier pre-training on Ascend. FT reported R2 failures in 2025, and a Tsinghua expert in 2026 doubted that V4's pre-training ran on Ascend.
- Any 950-series spec (FP8/FP4 throughput, HiBL/HiZQ memory performance).
- Domestic HBM performance and yield.
- Yields on N+3.

**Physical limits:**
- DUV-only SMIC nodes, at roughly half TSMC N3P density, with yield penalties on large dies.
- About 2.3x worse FLOPs per watt at system level.
- Thousands of optical transceivers per pod.
- HBM supply and bandwidth.

On the evidence, the strategy (scale-out over many weaker chips with optical interconnect) is on solid ground for inference and mid-scale training. Its cost is power and supply. Frontier-scale training and per-chip parity rest on unverified claims and constrained inputs.

### Cited Findings

**Evidence published by Huawei**
- **arXiv 2506.12708,** "Serving Large Language Models on Huawei CloudMatrix384":
  - v1 15 June 2025, v3 19 June 2025; 46 authors, last author Heng Liao. The abstract page lists no affiliations.
  - Hardware: 384 Ascend 910 NPUs and 192 Kunpeng CPUs on a UB network.
  - Serving DeepSeek-R1 with INT8 and expert parallelism at EP320:
    - prefill of 6,688 tokens/s per NPU;
    - decode of 1,943 tokens/s per NPU at a time per output token (TPOT) under 50 ms;
    - 538 tokens/s per NPU under a 15 ms TPOT.

  [CO, technical paper; not independently replicated in any source I found] — [arXiv](https://arxiv.org/abs/2506.12708)
- **Huawei-led post-training of DeepSeek V4:**
  - Full-parameter post-training of V4-Flash and V4-Pro (1.6T parameters) on an Ascend SuperPOD, reported in a technical report dated 22 July 2026.
  - MFU of 34.22% and a "2.93-fold" efficiency gain over an open-source baseline recipe, both the authors' own measurements; training described as stable.
  - The baseline was not NVIDIA hardware.
  - The Shenzhen government (via SCMP, June 2026) said the cluster had at least 1,000 Ascend 910C.

  [CO/GOV-China via PR] — [Implicator.ai](https://www.implicator.ai/deepseeks-huawei-chip-training-claim-finally-gets-its-benchmarks-and-its-doubters/); [SCMP](https://www.scmp.com/tech/article/3356117/huawei-chips-refine-deepseek-model-major-leap-chinas-ai-self-reliance) (excerpt); [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/huawei-led-team-claims-it-post-trained-deepseeks-1-6-trillion-parameter-models-on-ascend-910c-chips) (headline)
- **Huawei's UnifiedBus and optics claims:**
  - 2.1 µs latency, 100 ns optical fault detection, "optical reliability 100x higher" (Sept 2025).
  - Atlas 960E: 5,500 NPO engines replacing 48,000 800G modules, saving more than 550 kW, 99.8% availability (Sept 2026).
  - A simulation by Huawei's Markov Lab gives 2.75x the MFU for 4k-NPU SuperPoDs against 8-NPU servers.

  [CO] — [Huawei, 18 Sept 2025](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech); [Huawei, 17 Sept 2026](https://www.huawei.com/en/news/2026/9/hc-wang-keynote)
- **Claimed number formats:** the 950 supports FP8, MXFP8, HiF8 and MXFP4, and the 960 adds HiF4. [CO] — [Huawei, 18 Sept 2025](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech)

**Independent checks (teardowns, analyses, user results)**
- **TechInsights teardowns:**
  - The 910B (Oct 2024) and 910C samples (Oct 2025) contain TSMC-made dies, and the 910C samples contain Samsung and SK hynix HBM. This establishes provenance, not performance.
  - Kirin 9030 on N+3 (Dec 2025).
  - Assessment that N+3 is not viable for data-center AI chips (Mar 2026).

  [IND: TechInsights] — [Notebookcheck](https://www.notebookcheck.net/TSMC-die-and-Samsung-memory-confirmed-in-Huawei-910C-set-to-replace-Nvidia-AI-chips.1130790.0.html); [TechInsights](https://www.techinsights.com/blog/smic-n3-confirmed-kirin-9030-analysis-reveals-how-close-smic-5nm); [TechInsights](https://www.techinsights.com/ko/node/61228)
- **SemiAnalysis on CloudMatrix 384 against GB200 NVL72 (Apr 2025):**
  - About 300 PFLOPS dense BF16 against about 180 (1.7x).
  - All-in power about 559 kW against about 145 kW (about 3.9x), which is about 2.3x worse FLOPs per watt.
  - About 6,912 linear-drive (LPO) optical transceivers across 16 racks (12 compute, 4 network). Outlets differ on whether they are 800G or 400G.

  [AN] (excerpt; article mostly paywalled) — [SemiAnalysis](https://newsletter.semianalysis.com/p/huawei-ai-cloudmatrix-384-chinas-answer-to-nvidia-gb200-nvl72); [Tom's Hardware](https://tomshardware.com/tech-industry/artificial-intelligence/huaweis-new-ai-cloudmatrix-cluster-beats-nvidias-gb200-by-brute-force-uses-4x-the-power); [The Register, pub 29 July 2025](https://www.theregister.com/2025/07/29/huawei_rackscale_boogeyman/)
- **User results and claims:**
  - **DeepSeek V4:** Huawei announced day-0 Ascend inference support (24 Apr 2026, per search-result summaries; the originating outlet was not confirmed). [CO] (excerpt) — [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/deepseek-launches-1-6-trillion-parameter-v4-on-huawei-chips-as-us-escalates-ai-theft-accusations) (headline only)
  - **V4 validation:** V4 was reportedly validated on NVIDIA GPUs and Ascend, and ran on CUDA at launch. [PR, relayed] — [Implicator.ai](https://www.implicator.ai/deepseeks-huawei-chip-training-claim-finally-gets-its-benchmarks-and-its-doubters/)
  - **DeepSeek's own description of V4 training hardware:** relayed as citing H800 GPUs and Ascend 910C. [PR, relayed; not seen first-hand] — [Implicator.ai](https://www.implicator.ai/deepseeks-huawei-chip-training-claim-finally-gets-its-benchmarks-and-its-doubters/)
  - **Zhipu GLM-Image:** trained end to end on Ascend (company claim; chip count undisclosed). [CUST] — [InfoWorld](https://www.infoworld.com/article/4116787/chinese-ai-firm-trains-state-of-the-art-model-entirely-on-huawei-chips.html)
  - **Huawei's count:** "Over 40 models natively pre-trained on Ascend and CANN". [CO] — [Huawei, 17 Sept 2026](https://www.huawei.com/en/news/2026/9/hc-wang-keynote)
- **Skeptical expert views:**
  - Liu Zhiyuan (Tsinghua), to MIT Technology Review: DeepSeek "appears to have adapted only part of V4's training process for Chinese chips", and may have trained mainly on NVIDIA.
  - Anonymous sources: Chinese processors remain better suited to inference.
  - Phelix Lee (Morningstar): "We don't expect an abrupt switch toward (Huawei's) Ascend." Analysts cited by AP say cutting-edge training still relies on NVIDIA.

  [PR] — [Implicator.ai](https://www.implicator.ai/deepseeks-huawei-chip-training-claim-finally-gets-its-benchmarks-and-its-doubters/); [AP via WTOP](https://wtop.com/world/2026/06/nvidias-ai-chip-sales-in-china-stall-as-local-chipmakers-like-huawei-take-the-lead/)
- **Early DeepSeek testing of the 910C:** reportedly about 60% of an H100's inference performance (inference only). [PR, relayed] — [Implicator.ai](https://www.implicator.ai/deepseeks-huawei-chip-training-claim-finally-gets-its-benchmarks-and-its-doubters/)
- **NVIDIA's same-day V4-Pro demonstration:** on Blackwell at more than 150 tokens/s per user. [PR, relayed] — [Implicator.ai](https://www.implicator.ai/deepseeks-huawei-chip-training-claim-finally-gets-its-benchmarks-and-its-doubters/)

**Unproven items (as of 14 Nov 2026)**
- **950-series specs:** no independent measurement or teardown of the 950PR or 950DT was found. The reported Atlas 350 numbers vary by outlet (§1).
- **HiBL 1.0 and HiZQ 2.0:** maker undisclosed. Epoch calls the 950PR's memory "non-HBM". There are no third-party bandwidth, latency or yield data. [PR]/[AN] — [TrendForce, 10 Sept 2026](https://www.trendforce.com/news/2026/09/10/news-chinese-ai-chipmakers-reportedly-hike-prices-on-hbm-costs-huawei-950dt-up-as-much-as-50/); [Epoch AI](https://epoch.ai/publications/huaweis-roadmap-to-2031)
- **Domestic HBM:** CXMT HBM3E yields are reported at 20–30%. The 960DT reportedly faces a shortage of domestic HBM. [PR-U] — [TrendForce, 3 Nov 2026](https://www.trendforce.com/news/2026/11/03/news-china-reportedly-obtains-smuggled-hbm-via-server-packages-huawei-960dt-faces-domestic-hbm-shortage/)
- **FP8 and FP4 training at scale on Ascend:** I found no independent report.
- **Yields:** the last numeric report is FT's early-2025 figure of about 40% for the 910C.
- **Atlas 950 SuperPoD performance claims** (4.91M and 19.6M tokens/s), the 256,000-card SuperCluster, and the 1M-NPU topology. The Register calls the 1M configuration theoretical. — [TheNextWeb](https://thenextweb.com/news/huawei-connect-2026-ascend-960-superpod-unifiedbus)

**Physical and engineering limits**
- **DUV multi-patterning:**
  - SMIC is confined to 5–7nm-class density through about 2030. N+3 is about 113 MTr/mm², against TSMC N3P at about 224.
  - Multi-patterning lowers throughput and raises cost.
  - Epoch's yield illustration: a 137 mm² die at 70% yield implies about 12% yield for an 800 mm² die at the same defect density.

  [AN] — [Epoch AI](https://epoch.ai/publications/huaweis-roadmap-to-2031). TechInsights expects low yields for data-center AI dies on N+3. [IND] — [TechInsights](https://www.techinsights.com/ko/node/61228)
- **Huawei's own acknowledgment:** the mainland "will lag in process nodes for a long time". [CO] — [Huawei, 18 Sept 2025](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech)
- **Power efficiency:** CloudMatrix 384 at about 559 kW against about 145 kW, about 2.3x worse FLOPs per watt. [AN] — [Tom's Hardware](https://tomshardware.com/tech-industry/artificial-intelligence/huaweis-new-ai-cloudmatrix-cluster-beats-nvidias-gb200-by-brute-force-uses-4x-the-power)
- **Optical interconnect count and reliability:**
  - About 6,912 transceivers in a CloudMatrix 384. [AN]
  - Huawei's own Atlas 960E figure: 48,000 800G modules would be needed in the pluggable design. [CO]
  - Reliability claims (100x; 99.8% availability) are Huawei's only. I found no independent failure-rate data. — [Huawei, 17 Sept 2026](https://www.huawei.com/en/news/2026/9/hc-wang-keynote)
- **Memory bandwidth and capacity gap (Epoch):**
  - Usable HBM gap with NVIDIA of 73x in 2026, narrowing to 11x in 2028.
  - Huawei's memory-bandwidth-equivalent share of NVIDIA's: 1.4% in 2026.
  - Per-chip FP4: B300 at 13.5 PFLOPS against 2 PFLOPS for the 950, about 6.75x.

  [AN] — [Epoch AI](https://epoch.ai/publications/huaweis-roadmap-to-2031)
- **Supply-chain dependence:** shown by the teardown finding of TSMC dies and Korean HBM in 910C samples. [IND: TechInsights] — [Notebookcheck](https://www.notebookcheck.net/TSMC-die-and-Samsung-memory-confirmed-in-Huawei-910C-set-to-replace-Nvidia-AI-chips.1130790.0.html)

### Inferences
**Does it stand on solid ground? A mixed, evidence-based answer.**
- **Solid:**
  - The system-level approach is real and deployed at scale: more than 1,000 A3 SuperPoDs per Huawei. Independent analysts' system specs match Huawei's (about 300 PFLOPS).
  - Inference on Ascend is in production for leading Chinese models.
- **Weak or unproven:**
  - Frontier pre-training on Ascend lacks independent evidence: FT 2025, the Tsinghua expert in 2026, and DeepSeek's silence or mixed statements.
  - Every 950/960 claim is unmeasured.
  - Output depends on dwindling or smuggled foreign HBM and on a 7nm-class DUV process with yield and density ceilings. Efficiency per watt is materially worse.
- **On the roadmap:** Huawei says it will close per-chip gaps through packaging, number formats (FP4/HiF4) and scale. Epoch judges the roadmap "ambitious but insufficient" to catch NVIDIA by 2030. That is an analyst view, noted here as such.

### Gaps
- No independent benchmark (MLPerf or equivalent) of any Ascend product was found.
- No independent replication of the CloudMatrix384 paper's throughput numbers.
- No independent power measurement of the Atlas 350, 950DT or Atlas 950.
- No TechInsights or other teardown of the 950PR was found.
- DeepSeek's own statement on V4 training hardware was not seen first-hand.
- iFlytek's and Huawei Pangu's training-on-Ascend claims were not verified this session.

---

## 9. Cross-examination log: Huawei's claims against US government statements, Chinese customers, teardowns, NVIDIA and others

### Takeaway
The largest conflicts are:
- **Volume:** US Commerce's 2025 cap of 200k or fewer, against analyst and IDC counts several times higher.
- **Market share:** Huawei says it has "surpassed NVIDIA" in China, against IDC's H1 2026 unit data showing NVIDIA ahead (a Bernstein forecast sides with Huawei).
- **Status of Huawei's own systems:** "large-scale commercial use" against "still under testing" for the Atlas 950/950DT, said the same day.
- **Training capability:** the FT's account of DeepSeek R2 and expert doubts, against Huawei-led training claims.
- **Specification drift:** the Atlas 960 shrinking from 15,488 to 4,096 NPUs per pod, and the 950PR card at 1.56 rather than 2 PFLOPS FP4.

### Cited Findings

| # | Claim (who, date) | Counter-evidence (who, date, provenance) | Status |
|---|---|---|---|
| C1 | US Commerce: Huawei 2025 Ascend production capacity "at or below 200,000" ([Bloomberg, 12 June 2025](https://www.bloomberg.com/news/articles/2025-06-12/us-says-huawei-s-2025-output-is-no-more-than-200-000-ai-chips)) [GOV] | SemiAnalysis: 805k shipped in 2025, calling 200k "significantly off the mark" ([SemiAnalysis, 8 Sept 2025](https://newsletter.semianalysis.com/p/huawei-ascend-production-ramp)) [AN]. Epoch: about 800k ([Epoch](https://epoch.ai/publications/huaweis-roadmap-to-2031)) [AN]. IDC: "just over 300,000" in H1 2025 alone ([TradingView/SA](https://www.tradingview.com/news/seekingalpha:62d1b5de5094b:0-nvidia-s-china-ai-chip-market-share-falls-to-34-as-huawei-gains-ground-idc/)) [AN] | Unresolved; possibly definitional (capacity of domestic dies vs shipments that include TSMC stock) |
| C2 | David Wang (Huawei, 17 Sept 2026): Atlas 950 SuperPoD "seeing large-scale commercial use" ([Huawei](https://www.huawei.com/en/news/2026/9/hc-wang-keynote)); Zhou Yuefeng: "Ascend 950 supernodes have entered commercial use" ([TechNode](https://technode.com/2026/09/18/huawei-sets-commercial-launch-dates-for-ascend-950-ai-cluster-cloud-service/)) [CO] | Eric Xu (Huawei, same day): 950DT SuperPoDs "still under testing"; large-scale supply "end of this year or early next year" ([roundtable](https://www.manilatimes.net/2026/09/30/tmt-newswire/media-outreach-newswire/huawei-pioneers-a-new-computing-architecture-for-the-ai-era-making-one-million-processors-work-as-one-computer-summary-of-roundtable-meeting-between-eric-xu-and-international-media-outlets-on-september-17/2436416)) [CO] | Internal contradiction. Possibly 950PR-based vs 950DT-based pods, which no source clarifies |
| C3 | Eric Xu (Sept 2026): "Ascend has surpassed NVIDIA" in China on Huawei's data; executives told Bloomberg that Huawei's share exceeds NVIDIA's ([roundtable](https://www.manilatimes.net/2026/09/30/tmt-newswire/media-outreach-newswire/huawei-pioneers-a-new-computing-architecture-for-the-ai-era-making-one-million-processors-work-as-one-computer-summary-of-roundtable-meeting-between-eric-xu-and-international-media-outlets-on-september-17/2436416); [TheNextWeb](https://thenextweb.com/news/huawei-connect-2026-ascend-960-superpod-unifiedbus)) [CO] | IDC H1 2026 by units: NVIDIA 34%, Huawei 28% ([36Kr](https://eu.36kr.com/en/p/4024302190728839)) [AN]. Supporting Huawei: Bernstein 2026 forecast of Huawei about 50% and NVIDIA about 8% ([AP](https://wtop.com/world/2026/06/nvidias-ai-chip-sales-in-china-stall-as-local-chipmakers-like-huawei-take-the-lead/)) [AN] | Contested; depends on period, unit vs value, and forecast vs actual |
| C4 | Huawei 2025 roadmap: Atlas 960 SuperPoD with 15,488 chips in Q4 2027 ([Huawei](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech)) [CO] | Huawei 2026: Atlas 960E at 4,096 NPUs; Rui Ma flagged the reduction ([TheNextWeb](https://thenextweb.com/news/huawei-connect-2026-ascend-960-superpod-unifiedbus)) [CO/PR] | Spec change; whether a 15,488-chip pod remains planned is not stated |
| C5 | Huawei 2025: Ascend 950 die at 2 PFLOPS MXFP4 ([Huawei](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech)) [CO] | Atlas 350 (950PR) reported at 1.56 PFLOPS FP4 ([TechRadar](https://www.techradar.com/pro/huawei-reveals-its-latest-nvidia-h20-killer-packing-a-frankly-ridiculous-1-56-pflops-of-fp4-compute-and-up-to-112gb-of-hbm)) [PR] | Discrepancy unexplained |
| C6 | 950PR memory: Huawei calls HiBL 1.0 self-developed HBM ([Huawei](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech)) [CO]; Epoch lists 128 GB and 1.6 TB/s | Epoch calls the 950PR "non-HBM memory" ([Epoch](https://epoch.ai/publications/huaweis-roadmap-to-2031)) [AN]; Atlas 350 reported at 112 GB and 1.4 or 1.6 TB/s, 600 W or about 900 W (excerpt) [PR] | Unresolved |
| C7 | Huawei 2025: 960 at 4 PFLOPS FP4 ([Huawei](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech)) [CO] | Epoch: 960PR at 8 PFLOPS FP4 (LPDDR); 970 FP4 "raised from 8 to 14" ([Epoch](https://epoch.ai/publications/huaweis-roadmap-to-2031)) [AN] | Likely a roadmap update that I did not see in Huawei's own text |
| C8 | Huawei 2026: 960DT moved forward to Q1 2027 ([Huawei](https://www.huawei.com/en/news/2026/9/hc-wang-keynote)) [CO] | The Information: the 960DT faces a domestic HBM shortage and relies on Samsung/SK hynix HBM, which US controls restrict ([TrendForce, 3 Nov 2026](https://www.trendforce.com/news/2026/11/03/news-china-reportedly-obtains-smuggled-hbm-via-server-packages-huawei-960dt-faces-domestic-hbm-shortage/)) [PR-U] | Schedule risk reported; not yet testable (Q1 2027) |
| C9 | Huawei says more than 40 models were "natively pre-trained on Ascend and CANN"; Huawei-led V4 post-training reached 34.22% MFU ([Huawei](https://www.huawei.com/en/news/2026/9/hc-wang-keynote); [Implicator](https://www.implicator.ai/deepseeks-huawei-chip-training-claim-finally-gets-its-benchmarks-and-its-doubters/)) [CO] | FT (Aug 2025): R2 had no successful training run on Ascend ([TrendForce](https://www.trendforce.com/news/2025/08/14/news-deepseek-r2-model-launch-reportedly-delayed-amid-huawei-ascend-chip-hurdles/)) [PR-U]. Liu Zhiyuan (2026): only part of V4's training was adapted ([Implicator](https://www.implicator.ai/deepseeks-huawei-chip-training-claim-finally-gets-its-benchmarks-and-its-doubters/)) [PR] | Frontier pre-training on Ascend not independently shown |
| C10 | DeepSeek (as relayed) cited H800 and Ascend 910C for V4 training | A senior US official claimed smuggled Blackwell chips; NVIDIA called this "far-fetched" ([Implicator](https://www.implicator.ai/deepseeks-huawei-chip-training-claim-finally-gets-its-benchmarks-and-its-doubters/)) [PR] | Three-way conflict; none verified |
| C11 | Huawei's implied position that Ascend is a domestic supply chain (no Huawei statement found) | TechInsights: TSMC dies plus Samsung/SK hynix HBM inside the 910C ([Notebookcheck](https://www.notebookcheck.net/TSMC-die-and-Samsung-memory-confirmed-in-Huawei-910C-set-to-replace-Nvidia-AI-chips.1130790.0.html)) [IND]. BIS presumes Ascend chips violate General Prohibition 10 ([Arnold & Porter](https://www.arnoldporter.com/en/perspectives/advisories/2025/05/commerce-new-guidance-curb-adversaries-access-to-advanced-ai-tech)) [GOV] | Teardown evidence stands; Huawei had not commented (per Notebookcheck) |
| C12 | TSMC die count: CSIS more than 2M ([TechPowerUp](https://techpowerup.com/333877/huawei-obtained-two-million-ascend-910b-dies-from-tsmc-via-shell-companies-to-circumvent-us-sanctions)) [AN/GOV officials] | SemiAnalysis more than 2.9M ([SemiAnalysis](https://newsletter.semianalysis.com/p/huawei-ascend-production-ramp)) [AN]; TSMC says the die found was the one analyzed in Oct 2024 and production has halted ([Notebookcheck](https://www.notebookcheck.net/TSMC-die-and-Samsung-memory-confirmed-in-Huawei-910C-set-to-replace-Nvidia-AI-chips.1130790.0.html)) | Range of 2–2.9M; neither number confirmed by TSMC |
| C13 | Reuters (Apr 2025): TSMC "could face" a fine of US$1B or more ([Taipei Times](https://www.taipeitimes.com/News/taiwan/archives/2025/04/09/2003834894)) [PR-U] | Notebookcheck: "TSMC was fined $1 billion" ([Notebookcheck](https://www.notebookcheck.net/TSMC-die-and-Samsung-memory-confirmed-in-Huawei-910C-set-to-replace-Nvidia-AI-chips.1130790.0.html)) [PR, unsourced] | Unverified; no BIS record found |
| C14 | 950DT price increase: Bloomberg-sourced 60% ([Huawei Central](https://www.huaweicentral.com/huawei-ascend-950dt-price-jumped-60-over-past-three-months/)) | Reuters sources: 20–50% depending on contract ([TrendForce](https://www.trendforce.com/news/2026/09/10/news-chinese-ai-chipmakers-reportedly-hike-prices-on-hbm-costs-huawei-950dt-up-as-much-as-50/)) | Different baselines and periods |
| C15 | 2026 volume: WSJ, 1.5M units ([Epoch](https://epoch.ai/publications/huaweis-roadmap-to-2031)) | Reuters, about 750k 950PR ([TrendForce](https://www.trendforce.com/news/2026/04/01/news-huawei-2025-r-cloud-revenue-slips/)); Bloomberg 2025 report, 600k 910C and 1.6M dies ([RCR](https://rcrwireless.com/20250930/ai-infrastructure/huawei-ai-chips-2)); Xu: 950PR supply "not very big" ([roundtable](https://www.manilatimes.net/2026/09/30/tmt-newswire/media-outreach-newswire/huawei-pioneers-a-new-computing-architecture-for-the-ai-era-making-one-million-processors-work-as-one-computer-summary-of-roundtable-meeting-between-eric-xu-and-international-media-outlets-on-september-17/2436416)) | Units (chips vs dies) and scopes differ |
| C16 | FT plan for 2025: about 100k 910C and 300k 910B ([TrendForce](https://www.trendforce.com/news/2025/02/25/news-china-advances-in-ai-chips-huawei-reportedly-boosts-yield-to-40-making-ascend-line-profitable/)) [PR-U] | SemiAnalysis: 653k 910C shipped in 2025 ([SemiAnalysis](https://newsletter.semianalysis.com/p/huawei-ascend-production-ramp)) [AN] | Large gap; unexplained |
| C17 | SemiAnalysis internal: SMIC made about 1M 910C plus about 0.5M 910B in 2025 | The same report: 805k shipped in 2025 ([SemiAnalysis](https://newsletter.semianalysis.com/p/huawei-ascend-production-ramp)) | Not reconciled in the source |
| C18 | Malaysian Deputy Minister (19–20 May 2025): 3,000 Ascend servers by 2026 | Huawei: no Ascend sold in Malaysia, and the government ordered none; the government retracted ([Malay Mail](https://www.malaymail.com/news/malaysia/2025/05/21/malaysia-walks-back-huawei-ai-project-amid-us-china-tech-tensions/177551)) | Retracted |
| C19 | BIS press framing (May 2025): using Ascend "anywhere in the world" violates controls | BIS text: use "risks violating"; wording "later softened" ([Arnold & Porter](https://www.arnoldporter.com/en/perspectives/advisories/2025/05/commerce-new-guidance-curb-adversaries-access-to-advanced-ai-tech); [Malay Mail](https://www.malaymail.com/news/malaysia/2025/05/21/malaysia-walks-back-huawei-ai-project-amid-us-china-tech-tensions/177551)) | The US revised its own wording |
| C20 | Huawei (Sept 2025): Atlas 950 SuperPoD gives 6.7x the compute of NVL144 ([Huawei](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech)) | Per chip, NVIDIA's B300 delivers about 6.75x the 950's FP4 ([Epoch](https://epoch.ai/publications/huaweis-roadmap-to-2031)); Huawei's system compares 8,192 chips with 144 GPU dies | Both true; they measure different levels (system vs chip) |
| C21 | Huawei: CloudMatrix 384 at 300 PFLOPS | SemiAnalysis agrees on about 300 PFLOPS BF16 but puts power at about 3.9x and FLOPs per watt about 2.3x worse than GB200 NVL72 ([Tom's Hardware](https://tomshardware.com/tech-industry/artificial-intelligence/huaweis-new-ai-cloudmatrix-cluster-beats-nvidias-gb200-by-brute-force-uses-4x-the-power)) | Compute claim corroborated; the efficiency cost is not stated by Huawei |
| C22 | IDC's 34% (NVIDIA) and 28% (Huawei) are described in some coverage as having different denominators | My arithmetic: 678k ÷ 2.008M ≈ 33.8% and 572k ÷ 2.008M ≈ 28.5%, so both fit the same total | The coverage caveat appears mistaken (§2 sources) |
| C23 | H1 2026 net profit of CNY 23.43B ([TechNode](https://technode.com/2026/09/01/huawei-h1-revenue-rd-spending/)) | CNY 23.81B in Reuters-based reports ([TelecomLead](https://telecomlead.com/telecom-equipment/huawei-h1-2026-revenue-rises-9-6-to-69-6-billion-as-rd-spending-surges-25-2-127518)) | Probably attributable vs total profit; unconfirmed |
| C24 | US v. Huawei: "12 felony counts" ([Strategic Narratives](https://www.strategicnarratives.org/p/huawei-on-trial-6)) | An unidentified outlet in the search excerpts: 14 counts | Unresolved; check the docket |
| C25 | Mirror websites quote Jensen Huang as having "largely conceded" China to Huawei | Reliable coverage (AP) quotes "giants" and "about 95%" share before controls ([AP](https://wtop.com/world/2026/06/nvidias-ai-chip-sales-in-china-stall-as-local-chipmakers-like-huawei-take-the-lead/)) | The "largely conceded" quote is unverified; do not use it |
| C26 | A secondary article says the 910C has a single compute chiplet (excerpt; [SemiWiki thread](https://semiwiki.com/forum/threads/techinsights-teardown-huawei-ascend-910c-still-contains-cpu-dies-from-tsmc-from-2020.23737/)) | Notebookcheck and SemiAnalysis: two TSMC dies per 910C ([Notebookcheck](https://www.notebookcheck.net/TSMC-die-and-Samsung-memory-confirmed-in-Huawei-910C-set-to-replace-Nvidia-AI-chips.1130790.0.html)) | Two-die design is the majority report |
| C27 | China Mobile Ascend purchase reported as about US$22M ([LAVX](https://news.lavx.hu/article/china-mobile-invests-22m-in-domestic-compute-platform-powered-by-huawei-ascend)) | A related report gives "CNY 1.55 billion" ([Rutab](https://rutab.net/b/hardware/2026/02/07/kitayskiy-operator-china-mobile-zakupit-oborudovanie-huawei-na-155-mlrd-yuaney-otkazavshis-ot-resheniy-nvidia.html)); chip model 910B vs 910C also differs | Inconsistent; likely a unit error |

### Inferences
- Where Huawei's claims can be checked against independent material, the system-level compute claims hold up (C21). Supply-chain provenance does not: teardowns show foreign parts (C11).
- Huawei's market-share and commercial-status claims conflict with third-party data or with other Huawei executives (C2, C3).
- The US government's 2025 volume estimate is the outlier against all other estimates (C1).

### Gaps
- I could not open the Bloomberg article of 16 Sept 2026 (market share), the WSJ article (1.5M) or the full IDC release, so the definitions behind C3 and C15 remain unclear.

---

## 10. Verification of the five leads supplied from memory

### Takeaway
All five leads are confirmed in substance. Two need corrections of detail:
- The count of TSMC dies is "more than 2M" (CSIS, citing officials) or "more than 2.9M" (SemiAnalysis). The Sophgo link rests on Reuters reporting on the probe, Epoch's citation, and BIS's Jan 2025 listing of Sophgo for "risk of diversion to Huawei".
- The Brooklyn trial did not start early in 2026. Jury selection began on 8 Sept 2026, and the trial was ongoing in Nov 2026.

### Cited Findings
- **Lead 1: Huawei Connect roadmap (Sept 2025). CONFIRMED** by Huawei's keynote page: 950PR Q1 2026, 950DT Q4 2026, 960 Q4 2027, 970 Q4 2028, and the Atlas 950 SuperPoD (8,192 chips) in Q4 2026. The 2026 update moved the 960 earlier (960DT Q1 2027, 960PR Q3 2027) and added the 980 (2029). [CO] — [Huawei, 18 Sept 2025](https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech); [Huawei, 17 Sept 2026](https://www.huawei.com/en/news/2026/9/hc-wang-keynote)
- **Lead 2: US Commerce estimate of about 200,000 for 2025. CONFIRMED.** Jeffrey Kessler told a House Foreign Affairs subcommittee on 12 June 2025: "at or below 200,000". [GOV] — [Bloomberg](https://www.bloomberg.com/news/articles/2025-06-12/us-says-huawei-s-2025-output-is-no-more-than-200-000-ai-chips); [SCMP](https://www.scmp.com/tech/tech-war/article/3314356/huaweis-ai-semiconductor-output-limited-200000-2025-us-commerce-official-says)
- **Lead 3: TechInsights found a TSMC die in the 910B, and 2–3M dies came via Sophgo. CONFIRMED with qualifications.**
  - TSMC refers to the die "analyzed by this organization in October 2024". [IND/PR] — [Notebookcheck](https://www.notebookcheck.net/TSMC-die-and-Samsung-memory-confirmed-in-Huawei-910C-set-to-replace-Nvidia-AI-chips.1130790.0.html)
  - CSIS credits TechInsights with uncovering the scheme. (excerpt) — [TechPowerUp](https://techpowerup.com/333877/huawei-obtained-two-million-ascend-910b-dies-from-tsmc-via-shell-companies-to-circumvent-us-sanctions)
  - The counts are more than 2M (CSIS) and more than 2.9M (SemiAnalysis). [AN] — [SemiAnalysis](https://newsletter.semianalysis.com/p/huawei-ascend-production-ramp)
  - The Sophgo route: about US$500M of wafers per Epoch [AN] — [Epoch](https://epoch.ai/publications/huaweis-roadmap-to-2031); the Reuters probe report [PR-U] — [Taipei Times](https://www.taipeitimes.com/News/taiwan/archives/2025/04/09/2003834894); and BIS's listing [GOV] — [Federal Register](https://www.govinfo.gov/content/pkg/FR-2025-01-16/html/2025-00480.htm)
  - The potential TSMC penalty of US$1B or more is reported; no outcome was found.
- **Lead 4: FT, Aug 2025, on DeepSeek R2 problems on Ascend. CONFIRMED** via relay of the FT's 14 Aug 2025 report. [PR-U] — [TrendForce](https://www.trendforce.com/news/2025/08/14/news-deepseek-r2-model-launch-reportedly-delayed-amid-huawei-ascend-chip-hurdles/)
- **Lead 5: US criminal trial in Brooklyn in 2026. CONFIRMED.**
  - Jury selection began on 8 Sept 2026 before Judge Ann Donnelly, EDNY. (excerpt) — [TechTimes](https://www.techtimes.com/articles/326904/20260907/huawei-rico-trial-opens-tuesday-us-makes-telecom-giant-answer-criminal-enterprise.htm)
  - Trial Day 31 was 3 Nov 2026, with no verdict reported as of 10 Nov 2026. [PR] — [Strategic Narratives](https://www.strategicnarratives.org/p/huawei-on-trial-6)

### Inferences
- None beyond the qualifications above.

### Gaps
- The original TechInsights 910B report (Oct 2024) and the original FT article were not opened. I relied on relays.

---

## 11. Closing lists: (a) contradictions found; (b) what I could not find or verify

### Takeaway
Twenty-seven contradictions or inconsistencies are logged in §9. The main items I could not find or verify:
- Huawei's cash and debt.
- Results for Q1–Q3 2026.
- Any credible estimate of Ascend revenue.
- Independent measurements of the 950 series.
- Who makes the HBM.
- Trial status after 10 Nov 2026.
- The outcome of the TSMC probe.

### Cited Findings
**(a) Contradictions found** (details and sources in §9):
1. C1: US Commerce's 2025 figure of 200k or fewer, against SemiAnalysis and Epoch at about 800k and IDC at more than 300k in H1 2025 alone.
2. C2: Huawei executives on the same day: Atlas 950 SuperPoD in "large-scale commercial use" against 950DT SuperPoDs "still under testing".
3. C3: Huawei says it has "surpassed NVIDIA" in China, against IDC's H1 2026 unit shares (NVIDIA 34%, Huawei 28%) and Bernstein's 2026 forecast (Huawei about 50%).
4. C4: Atlas 960 SuperPoD at 15,488 chips (2025) against the Atlas 960E at 4,096 NPUs (2026).
5. C5: 950 die at 2 PFLOPS MXFP4 (roadmap) against the Atlas 350 at 1.56 PFLOPS FP4 (launch reporting).
6. C6: HiBL 1.0 described as HBM (Huawei) against "non-HBM memory" (Epoch); conflicting reports of the Atlas 350's memory, bandwidth and power.
7. C7: 960 at 4 PFLOPS FP4 (2025 roadmap) against the 960PR at 8 PFLOPS FP4 and the 970 at 14 (Epoch's reading).
8. C8: 960DT moved forward against reports of a domestic HBM shortage and reliance on Korean HBM.
9. C9: Huawei's pre-training and post-training claims against the FT's R2 report and the Tsinghua expert's doubts.
10. C10: Three accounts of V4's training hardware: DeepSeek (H800 and 910C), a US official (smuggled Blackwell), and NVIDIA ("far-fetched").
11. C11: An implied domestic supply chain against teardowns showing TSMC dies and Korean HBM.
12. C12: TSMC dies: more than 2M (CSIS) against more than 2.9M (SemiAnalysis).
13. C13: TSMC "could face" a fine of US$1B or more (Reuters) against "was fined" (Notebookcheck, unsourced).
14. C14: 950DT price increase of 60% (Bloomberg relay) against 20–50% (Reuters).
15. C15: 2026 volume: 1.5M (WSJ) against about 750k 950PR (Reuters) against 1.6M dies (Bloomberg 2025), plus Xu's "not very big".
16. C16: FT's 2025 plan (about 100k 910C) against SemiAnalysis (653k 910C shipped).
17. C17: SemiAnalysis's own production (about 1.5M) against its shipment figure (805k) for 2025.
18. C18: Malaysia's announcement against Huawei's denial and the retraction.
19. C19: BIS's "anywhere in the world" framing against the softened text.
20. C20: System-level against chip-level comparisons with NVIDIA (6.7x against about 1/6.75).
21. C21: CloudMatrix 384 compute claim corroborated, but the efficiency cost of about 2.3x worse FLOPs per watt is not stated by Huawei.
22. C22: Coverage says IDC's shares have different denominators; the arithmetic says the same total.
23. C23: H1 2026 net profit of CNY 23.43B against CNY 23.81B.
24. C24: Trial counts of 12 against 14.
25. C25: Huang's "largely conceded" quote, from mirror sites only, against AP's verified quotes.
26. C26: 910C described as one compute chiplet against two dies.
27. C27: China Mobile purchase of US$22M against CNY 1.55B.

### Inferences
- The contradictions cluster in three areas: volume (C1, C15–C17), Huawei's description of its own status and specs (C2, C4–C7), and training capability (C9–C10). These are the areas where independent data is thinnest.

### Gaps
**(b) What I could not find or verify** (web-search quota exhausted mid-session; some items are blocked by paywalls):
- **Financials:** Huawei's cash and short-term investments, borrowings and operating cash flow for 2024 and 2025. Q1–Q3 2026 results, if published. H1 2026 segment data. 2024 R&D as reported. Segment restatements.
- **Ascend economics:** any credible agency or analyst estimate of Ascend revenue. Morgan Stanley and TrendForce research figures on Ascend shipments. The original Bloomberg article (16 Sept 2026) on share, the WSJ article (1.5M) and the full IDC release.
- **Products:**
  - Ascend 310 status; 910D status beyond its naming by BIS.
  - The official Atlas 350 datasheet and any independent test or teardown of the 950PR or 950DT.
  - Whether Atlas 950 SuperPoD or 950DT volume deliveries began before 14 Nov 2026.
  - Who makes HiBL 1.0 and HiZQ 2.0.
  - Whether the CANN open-sourcing promised for 31 Dec 2025 was completed in full.
  - The 960PR and 970 spec updates in Huawei's own text.
- **Customers:** iFlytek, Baidu, SiliconFlow and Tencent Ascend details. China Telecom and China Unicom tenders. China Mobile package values. Any signed hyperscaler contract values. The US$5.6B ByteDance figure. Any completed Middle-East deployment.
- **Capacity:** SMIC yield and allocation for Ascend in 2026; listing status of Pengxinwei (PXW) and other fabs; any US government output estimate for 2026; the original CSIS text.
- **People and ownership:** the Union's exact stake; the number of employee shareholders; the board chair; when Ken Hu left the rotating chairs; whether Zhang Dixuan was still in her role in late 2026; the date Zhou Yuefeng became Huawei Cloud CEO.
- **Legal:**
  - Trial status after 10 Nov 2026 (verdict or deliberations), the exact count list, and the history of the original trial date.
  - The final outcome of the TSMC/Sophgo probe.
  - The full text of BIS's May 2025 guidance and any amendment.
  - Any 2026 US rule specific to Ascend.
  - China's 2025 RTX Pro 6000D ban and SAMR's finding against NVIDIA.
  - The status of the affiliates rule.
- **Science:**
  - Any independent benchmark (MLPerf or equivalent) of an Ascend product.
  - Independent replication of the CloudMatrix384 paper's numbers.
  - Independent measurements of power or optical reliability.
  - DeepSeek's first-hand statement on V4 training hardware.
  - Claims of training on Ascend by Huawei Pangu and iFlytek.
- **Pending events after 14 Nov 2026:**
  - Huawei Cloud's overseas launch of the Ascend 950 cluster service (30 Nov 2026).
  - 950DT and Atlas 950 SuperPoD Q4 2026 availability.
  - 960DT (Q1 2027) and 960PR (Q3 2027).
  - 970 (2028) and 980 (2029).
  - The verdict in US v. Huawei.
