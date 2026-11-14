# Google TPU business inside Alphabet — fact base as of 14 November 2026

**How to read these notes.** Every bullet gives a date (the period covered or an as-of date) and a source in the form [Publisher, "Title", publication date](URL).

Each item is tagged with where it comes from:
- **[CS]**: stated by Google or Alphabet.
- **[CS-X]**: stated by another named company X, such as Broadcom, Anthropic, Oracle, Blackstone or Apple.
- **[SEC]**: stated in an SEC filing.
- **[IV: who]**: checked by someone independent of Google, who is named.
- **[AE: who]**: an analyst or industry estimate, with the source named.
- **[PR]**: a press or third-party report that names its sources or gives its own analysis.
- **[PR-U]**: a press report that cites unnamed sources.
- **[SS]**: taken from a search-engine summary of the linked page. I did not open the page myself, so confidence is lower.
- **[INF]**: my own inference. These appear only under "Inferences".

**Research limits:**
- The WebSearch budget, which is shared across agents, ran out part-way through this research. After that I only opened pages I had already found or well-known primary pages, and did no new searching.
- The Exa search tool was unavailable because it was out of credits.
- These sites blocked access or returned errors: Reuters, DCD, Courthouse News, CACM, Blackstone.com, Benzinga and GuruFocus. The GitHub MCP could not access the MLCommons repositories, so I read their public web pages instead.
- Long SEC filings were cut off at about 100,000 characters. For the Q2 and Q3 2026 10-Qs I therefore could not read the segment, commitments (Note 10) or legal-proceedings sections.

---

## 1. Products and stage: TPU generations, pod sizes, OCS/networking, Axion CPUs, and TPUs outside Google Cloud

### Takeaway
As of 14 Nov 2026:
- **Ironwood (TPU7x)** went to Preview on 24 Nov 2025 and became generally available (GA) on 31 Mar 2026, not in Nov 2025.
- **The eighth generation** was announced on 22 Apr 2026 as two chips: TPU 8t for training and TPU 8i for inference. Two more systems, TPU 8tx and TPU 8i Max, were added on 9 Nov 2026. Google promised GA for 8t and 8i "later this year", but I found no confirmation that any TPU 8 system is GA yet. Broadcom says it began production shipments of TPU v8i by 2 Sep 2026.
- **TPUs outside Google Cloud.** Since Q2 2026 Google has sold TPU systems for customers' own data centers. It also set up a Blackstone joint venture, Crux AI, in May 2026, and in Oct 2026 announced an Oracle (OCI) offering that starts in calendar 2027.

### Cited Findings

#### TPU v1 (first generation)
- **Deployment and specs.** In Google data centers since 2015. Peak 92 TOPS from a 65,536-unit array of 8-bit multiply-accumulators, with 28 MiB of on-chip memory. [CS, peer-reviewed]
- **Google's comparison claims.** About 15–30x faster than the comparison inference platforms, an Intel Haswell CPU and an Nvidia K80 GPU, and about 30–80x better TOPS/Watt. [CS]
- Source for both bullets: [arXiv/ISCA 2017, Jouppi et al., "In-Datacenter Performance Analysis of a Tensor Processing Unit", submitted 16 Apr 2017](https://arxiv.org/abs/1704.04760).

#### TPU v4
- **Deployment and scale.** Deployed since 2020. The supercomputer has 4,096 chips: 4x larger than TPU v3 and about 10x faster overall. [CS, peer-reviewed]
- **Cost and power of optics.** Optical circuit switches (OCS) and related optics make up less than 5% of system cost and less than 3% of system power. [CS]
- **Performance claims.** Against TPU v3, v4 is 2.1x faster with 2.7x better performance per watt. Against an Nvidia A100 system of similar size, it is 1.2–1.7x faster and uses 1.3–1.9x less power. Against Graphcore IPU Bow, it is 4.3–4.5x faster. SparseCores give 5–7x on embedding-heavy models while using 5% of die area and power. [CS]
- Source for these three bullets: [arXiv/ISCA 2023, Jouppi et al., "TPU v4: An Optically Reconfigurable Supercomputer for Machine Learning with Hardware Support for Embeddings", 4 Apr 2023](https://arxiv.org/abs/2304.01433).
- **Topology.** v4 uses a 3D topology built from 4x4x4 cubes of 64 chips. [CS] — [Google Cloud docs, "TPU system architecture", accessed 14 Nov 2026](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm)

#### TPU v5e
- **Specs.** 128x128 matrix units (MXU) with int8 support. [CS] — [Google Cloud docs, accessed 14 Nov 2026](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm)
- **Earliest dated Google mention found.** A GKE support note dated 29 Aug 2023 covers v4 and v5e. [CS] — [Google Cloud TPU release notes, accessed 14 Nov 2026](https://docs.cloud.google.com/tpu/docs/release-notes)
- **MLPerf.** Submitted to MLPerf Training v3.1 as a 4,096-chip v5e system using PAX. [IV: MLCommons review process] — [MLCommons GitHub, training_results_v3.1/Google/systems, accessed 14 Nov 2026](https://github.com/mlcommons/training_results_v3.1/tree/main/Google/systems)

#### TPU v5p
- **Specs.** 128x128 MXUs, FP8, 4 SparseCores per chip, 3D topology. [CS] — [Google Cloud docs](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm)
- **Used by Apple.** Apple trained its on-device model (AFM-on-device) on one slice of 2,048 TPUv5p chips (report v1 dated 29 Jul 2024). [IV: Apple, as a customer] — [arXiv, Apple, "Apple Intelligence Foundation Language Models", v1 29 Jul 2024](https://arxiv.org/html/2407.21075v1)
- **MLPerf.** In MLPerf Training v4.1, Google listed v5p systems of 16–2,048 chips (MaxDiffusion) and 4,096, 8,192 and 12,288 chips (MaxText). [IV: MLCommons] — [MLCommons GitHub, training_results_v4.1/Google/systems](https://github.com/mlcommons/training_results_v4.1/tree/main/Google/systems)

#### TPU v6e (Trillium)
- **Specs.** 256x256 MXUs (128K bfloat16 multiply-accumulates per cycle per MXU), int8, 2 SparseCores per chip. [CS] — [Google Cloud docs](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm)
- **GA.** Google's release note for Trillium GA is dated 16 Dec 2024. [CS] — [Google Cloud TPU release notes](https://docs.cloud.google.com/tpu/docs/release-notes)
- **SemiAnalysis estimates.** Trillium doubled peak FLOPs on the same TSMC N5 node by moving to 256x256 systolic arrays, and has 2 HBM3 stacks. [AE: SemiAnalysis] — [SemiAnalysis, "TPUv7: Google Takes a Swing at the King", 28 Nov 2025](https://newsletter.semianalysis.com/p/tpuv7-google-takes-a-swing-at-the)

#### TPU7x (Ironwood), seventh generation

**Announcement (9 Apr 2025, Cloud Next '25)** [CS], from [Google blog, Amin Vahdat (then VP/GM, ML, Systems & Cloud AI), Ironwood announcement, 9 Apr 2025, updated 23 Apr 2025](https://blog.google/products/google-cloud/ironwood-tpu-age-of-inference/):
- **Per chip.** 4,614 TFLOPs peak; the figure captions refer to FP8. 192 GB of HBM (6x Trillium) at 7.37 TB/s (4.5x Trillium). Inter-chip interconnect (ICI) of 1.2 TBps bidirectional (1.5x Trillium).
- **Pods.** 256-chip and 9,216-chip configurations. The 9,216-chip pod gives 42.5 exaflops, which Google called more than 24x El Capitan's 1.7 exaflops. The 9,216-chip configuration spans nearly 10 MW.
- **Efficiency and cooling.** 2x performance per watt versus Trillium, and nearly 30x more power-efficient than Google's first Cloud TPU of 2018. Liquid cooled.
- **Availability.** "Later this year."

**Update (6 Nov 2025)** [CS], from [Google Cloud blog, Vahdat (now Chief Technologist & SVP, AI & Infrastructure) & Mark Lohmeyer, "Ironwood TPUs and new Axion-based VMs for your AI workloads", 6 Nov 2025](https://cloud.google.com/blog/products/compute/ironwood-tpus-and-new-axion-based-vms-for-your-ai-workloads):
- **Availability.** "Will be generally available in the coming weeks."
- **Performance claims.** Up to 10x peak performance versus TPU v5p, and more than 4x better per-chip performance versus v6e for both training and inference.
- **Scale.** ICI of 9.6 Tb/s, 1.77 PB of shared HBM per 9,216-chip superpod, and Jupiter-connected clusters of "hundreds of thousands" of TPUs.
- **Reliability.** OCS reroutes around faults. Google's liquid cooling is deployed at gigawatt scale with fleet-wide uptime of about 99.999% since 2020.

**Actual availability and specs:**
- **Release notes.** Preview on 24 Nov 2025 ("TPU7x is available in Preview"); GA on 31 Mar 2026 ("TPU7x is generally available (GA)"). [CS] — [Google Cloud TPU release notes, accessed 14 Nov 2026](https://docs.cloud.google.com/tpu/docs/release-notes)
- **Docs specs.** 256x256 MXUs, FP8, 4 SparseCores, 4 chips per host, 3D topology. [CS] — [Google Cloud docs](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm)

**SemiAnalysis estimates (28 Nov 2025)** [AE: SemiAnalysis], from [SemiAnalysis, 28 Nov 2025](https://newsletter.semianalysis.com/p/tpuv7-google-takes-a-swing-at-the):
- One 4x4x4 cube (64 TPUs) per rack.
- About 1.5 optical transceivers per TPU, on 800G links.
- 48 OCS units (144x144 ports) for the 9,216-chip build.
- 8-Hi HBM3E.
- About 10% below Nvidia GB200 on peak FLOPs and peak memory bandwidth.
- GA about one year after Nvidia's Blackwell.

**Supplier statement:** "we delivered Ironwood TPU v7 ... in high volume to both Anthropic and Google" (2 Sep 2026). [CS-Broadcom] — [Investing.com, Broadcom Q3 FY2026 earnings call transcript, 2 Sep 2026](https://www.investing.com/news/transcripts/earnings-call-transcript-broadcom-tops-q3-2026-estimates-as-ai-sales-surge-93CH-4886849)

#### Eighth generation: TPU 8t and TPU 8i (announced 22 Apr 2026 at Cloud Next '26)

**Google's announcement** [CS], from [Google blog, Amin Vahdat, "Our eighth generation TPUs: two chips for the agentic era", Cloud Next, 22 Apr 2026](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/) and [Google Cloud blog, Vahdat & Lohmeyer, "What's next in Google AI infrastructure", 22 Apr 2026](https://cloud.google.com/blog/products/compute/ai-infrastructure-at-next26):
- **First split generation.** This is the first TPU generation split into a training chip (8t) and an inference chip (8i). Both were designed with Google DeepMind.
- **TPU 8t.**
  - Nearly 3x compute performance per pod versus the previous generation.
  - Superpod of 9,600 chips with 121 ExaFlops and 2 PB of shared HBM.
  - Double the inter-chip bandwidth, and 10x faster storage access via TPUDirect.
  - Near-linear scaling to up to 1 million chips in one logical cluster using the Virgo network, JAX and Pathways.
  - Target of more than 97% "goodput", with OCS among the reliability features.
- **TPU 8i.**
  - 288 GB of HBM and 384 MB of on-chip SRAM (3x the previous generation).
  - ICI doubled to 19.2 Tb/s.
  - "Boardfly" topology that cuts network diameter by more than 50%.
  - A Collectives Acceleration Engine that cuts on-chip latency by up to 5x.
  - Pod structure: four fully connected chips per board, eight boards per group, 36 groups per pod.
  - "80% better performance-per-dollar" than the previous generation.
- **Both chips.**
  - Up to 2x better performance per watt than Ironwood.
  - Fourth-generation liquid cooling, and Axion Arm CPU hosts for the first time.
  - Software: JAX, MaxText, PyTorch, SGLang and vLLM, with bare-metal access.
  - Availability: "generally available later this year" (Google blog); "available to Cloud customers soon" (Cloud blog).
- **Virgo network.** 4x the bandwidth of the previous generation; 134,000 TPU 8t chips in a single fabric inside one data center, and more than 1 million TPUs across sites.
- **TorchTPU.** Native PyTorch support "now in preview with select customers".

**Per-chip figures reported from Google's spec tables** (the Google page shows them only as images) [PR], from [Crypto Briefing, "Google splits its eighth-generation TPU into two chips…", 9 Nov 2026](https://cryptobriefing.com/google-tpu-8t-8i-training-inference-chips/), which says Hot Chips 2026 (Aug 2026) would carry more detail:
- TPU 8t: 12.6 PFLOPs at FP4, 216 GB HBM, 128 MB SRAM.
- TPU 8i: 10.1 PFLOPs at FP4, 288 GB HBM, 384 MB SRAM.
- Both made on TSMC N3.

**Later statements:**
- Pichai on the Q2 2026 call (22 Jul 2026): Google offers "TPU 8t and 8i, which delivers strong price performance". He gave no GA date. [CS] — [Investing.com, Alphabet Q2 2026 call transcript, 22 Jul 2026](https://www.investing.com/news/transcripts/earnings-call-transcript-alphabet-beats-q2-2026-estimates-shares-fall-on-capex-surge-93CH-4807140)
- Broadcom (2 Sep 2026): "we began production shipments of the next generation TPU v8i for Google", and "Broadcom is now shipping the TPU v8i ahead of the MediaTek v8t, which in fact was initiated earlier." [CS-Broadcom] — [Investing.com transcript, 2 Sep 2026](https://www.investing.com/news/transcripts/earnings-call-transcript-broadcom-tops-q3-2026-estimates-as-ai-sales-surge-93CH-4886849); the same wording appears in [Motley Fool transcript, call 2 Sep 2026, posted 9 Sep 2026](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/)
- 9 Nov 2026 (Google, Vahdat): TPU 8t gives "up to 2.7x better training performance" and TPU 8i "80% better inference price-performance" versus the previous generation. The post does not say whether 8t or 8i is GA. [CS] — [Google blog, "Introducing TPU 8tx and TPU 8i Max", 9 Nov 2026](https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/tpu-8i-max-and-8tx/)
- When fetched, the Google Cloud TPU release-notes page had no TPU 8t or 8i entries; its newest entry was dated 1 Jun 2026. [CS] — [release notes](https://docs.cloud.google.com/tpu/docs/release-notes)

#### TPU 8tx and TPU 8i Max (announced 9 Nov 2026)
Source for all bullets: [Google blog, Vahdat, 9 Nov 2026](https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/tpu-8i-max-and-8tx/) [CS].
- **TPU 8tx.** Same silicon as 8t, paired with 5th-generation AMD EPYC host CPUs. Aimed at secure and confidential inference and small-scale training. Its Boardfly network gives "up to 2x lower latency compared to TPU 8t".
- **TPU 8i Max.** Two TPU 8i chips on one package, with "double the compute, double the SRAM and double the HBM bandwidth" of 8i.
- **Availability.** No GA dates given; as of 14 Nov 2026, availability is pending.
- **Other claims in the same post.** TPUs have "nearly 100 customers". Google has "shipped four TPU systems in a single year". TorchTPU was open-sourced "last month" (Oct 2026). Cloud Pathways is GA on GKE. Google claims "state-of-the-art price-performance" on the InferenceX and AgentX benchmarks.

#### Axion CPUs
- **6 Nov 2025:** N4A VMs in preview ("up to 2x better price-performance" than comparable x86 VMs; up to 64 vCPUs); C4A metal, the first Arm bare-metal instance, in preview "soon" (up to 96 vCPUs); C4A already available (up to 72 vCPUs). [CS] — [Google Cloud blog, 6 Nov 2025](https://cloud.google.com/blog/products/compute/ironwood-tpus-and-new-axion-based-vms-for-your-ai-workloads)
- **22 Apr 2026:** GKE Agent Sandbox on Axion N4A gives "up to 30% better price-performance" than agent workloads on other hyperscalers. TPU 8t and 8i are the first TPUs on Axion hosts. [CS] — [Google Cloud blog, 22 Apr 2026](https://cloud.google.com/blog/products/compute/ai-infrastructure-at-next26)
- **26 Sep 2024:** Google DeepMind says AlphaChip was also used for Axion layouts. [CS] — [Google DeepMind blog, "How AlphaChip transformed computer chip design", 26 Sep 2024](https://deepmind.google/discover/blog/how-alphachip-transformed-computer-chip-design/)

#### TPUs outside Google Cloud (status as of Nov 2026)

**Hardware sales into customer data centers:**
- **Q1 2026 call (29 Apr 2026).** Pichai said Google would "begin to deliver TPUs to a select group of customers in their own data centers", citing demand from "AI labs, capital markets firms and high-performance computing applications". Ashkenazi said "revenues from TPU hardware sales will fluctuate from quarter to quarter". [CS] — [The Register, Simon Sharwood, "Google to sell its TPUs to some customers", 30 Apr 2026](https://www.theregister.com/off-prem/2026/04/30/google-to-sell-its-tpus-to-some-customers/5220078)
- **Q2 2026 (22 Jul 2026).** Ashkenazi: "We also began to recognize revenues from TPU system sales", which were first delivered to customer data centers in Q2, and "We anticipate the vast majority of the revenues from these agreements will be realized in 2027." [CS] — [Investing.com, Alphabet Q2 2026 call transcript, 22 Jul 2026](https://www.investing.com/news/transcripts/earnings-call-transcript-alphabet-beats-q2-2026-estimates-shares-fall-on-capex-surge-93CH-4807140)
- **Revenue description.** "Google Cloud generates product revenues primarily from the sale of TPU systems" (Q2 2026 release, 22 Jul 2026). [SEC] — [Alphabet Q2 2026 earnings release](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000066/googexhibit991q22026.htm)
- **What a TPU-system sale includes.** "Hardware, software, installation, support, and extended warranty services". Customer options are accounted for as rights of return. [SEC] — [Alphabet 10-Q, quarter ended 30 Jun 2026](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000071/goog-20260630.htm)
- **Repurchase obligations.** Where a customer assigns TPU systems to another party but Alphabet can still be required to repurchase them, Alphabet accounts for this "as a financial guarantee". [SEC] — [Alphabet 10-Q, quarter ended 30 Sep 2026](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000084/goog-20260930.htm)
- **Scale of the agreements.** A search summary of the 10-Q says Alphabet has signed "a limited number of agreements" to supply TPU systems to customers who require or provide on-premises infrastructure; that the agreements cover multiple gigawatts of hardware; and that some include credit backstops for third-party data centers and power infrastructure. [SS; I did not retrieve the exact 10-Q wording] — [Alphabet 10-Q Q2 2026](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000071/goog-20260630.htm)

**Crux AI (joint venture with Blackstone):**
- **Announcement (18 May 2026).** Blackstone commits $5B of initial equity; Google contributes TPUs, hardware, software and services; the first 500 MW is targeted for 2027; the CEO is Benjamin Treynor Sloss, a long-time Google infrastructure executive. [CS-Blackstone via SS] — [Business Wire / Blackstone, "Blackstone Announces Joint Venture with Google to Create New TPU Cloud", 18 May 2026](https://www.businesswire.com/news/home/20260518367552/en/Blackstone-Announces-Joint-Venture-with-Google-to-Create-New-TPU-Cloud)
- **Ownership.** The Wall Street Journal reported that Blackstone holds a majority stake. [PR via SS] — [Yahoo Finance](https://finance.yahoo.com/sectors/technology/articles/blackstone-google-tpu-cloud-joint-114334905.html)
- **Financing (Sep 2026).** A $22B debt package from 10 banks (including Goldman Sachs, SMBC, Barclays, BNP Paribas and Bank of Nova Scotia), secured by the TPUs and by Crux AI's customer contracts. [PR: Bloomberg, as relayed] — [TipRanks, Ran Melamed, 17 Sep 2026](https://www.tipranks.com/news/alphabet-googl-and-blackstone-bx-secure-22b-for-crux-ai-google-tpu-buildout)
- **In Alphabet's accounts (as of 30 Sep 2026).** Crux AI is "an unconsolidated equity method joint venture and a related party". Its multi-year commercial agreement makes up $16.8B of Alphabet's revenue backlog. [SEC] — [Alphabet 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000084/goog-20260930.htm)
- **Unconfirmed items.** That Alphabet committed to data center and energy backstops of up to $10.0B for the JV, and that there were early delays in securing sites. [SS, unconfirmed]
- **Q3 2026 call (28 Oct 2026).** Kurian: "We're making TPU systems available in their data centers", and more partnerships like Oracle and Crux AI are "in the works". [CS] — [Asymmetric Curiosity (Substack), "Google is selling the TPU", 9 Nov 2026](https://asymmetriccuriosity.substack.com/p/google-is-selling-the-tpu)

**Oracle Cloud Infrastructure (announced 27 Oct 2026):**
- **What was announced.** The first time Google TPUs will be offered on a hyperscale cloud outside Google. Available in calendar 2027, ramping over several years. OCI provides power, cooling and networking. [CS-Oracle/Google] — [Google Cloud Press Corner, "Oracle Brings Google TPUs to Oracle Cloud Infrastructure", 27 Oct 2026](https://www.googlecloudpresscorner.com/2026-10-27-Oracle-Brings-Google-TPUs-to-Oracle-Cloud-Infrastructure)
- **Hardware ownership.** Oracle will buy the chips directly. [PR] — [Seoul Economic Daily, 28 Oct 2026](https://en.sedaily.com/international/2026/10/28/openai-weighs-buying-google-tpus-easing-nvidia-reliance)
- **Status as of 14 Nov 2026.** Not yet live; scheduled for 2027.

**Google's own framing (9 Nov 2026).** Its blog lists "allowing customers to deploy TPUs directly into their own data centers" as an expanding use case. [CS] — [Google blog, 9 Nov 2026](https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/tpu-8i-max-and-8tx/)

### Inferences
- **[INF] Ironwood arrived later than Google signalled.** On 6 Nov 2025 Google said GA was "in the coming weeks". The release notes show Preview on 24 Nov 2025 and GA on 31 Mar 2026, roughly four to five months after the Nov 2025 signal. The "GA about Nov 2025" premise in the brief does not match Google's own release notes.
- **[INF] Google's numbers are internally consistent:**
  - Ironwood: 9,216 chips x 192 GB is about 1.77 PB, matching Google's shared-HBM figure. 9.6 Tb/s equals 1.2 TB/s, so the two ICI figures agree.
  - TPU 8t: 121 EF / 9,600 chips is about 12.6 PF per chip (FP4), matching the reported per-chip figure. 9,600 x 216 GB is about 2.07 PB, close to Google's "two petabytes".
  - TPU 8i pod: 4 x 8 x 36 = 1,152 chips.
- **[INF] The "nearly 3x per pod" claim may compare different number formats.** If 8t's 121 EF is FP4, as reported, and Ironwood's 42.5 EF is FP8, the multiple mixes precisions. I did not find an FP8 figure for TPU 8t.
- **[INF] Ironwood power.** About 10 MW for a 9,216-chip pod works out to roughly 1.1 kW per chip, including system overheads.

### Gaps
- No confirmation found that TPU 8t or 8i is GA as of 14 Nov 2026. There is also no GA date for 8tx or 8i Max.
- No bf16 or FP8 per-chip figures for TPU 8t or 8i, and no HBM bandwidth for 8t, from a Google-controlled page I could read. Whether Google presented at Hot Chips 2026 was not verified.
- I did not verify the original announcement dates and Google's claims for v5e (Aug 2023), v5p (Dec 2023; pod of 8,960 chips) or Trillium (May 2024; 4.7x and 67% claims; 256-chip pods). The searches that would have confirmed them could not be run.

---

## 2. Roadmap and milestones: commitments, dates, and whether each was met, slipped, or is pending

### Takeaway
Google has delivered a new TPU generation about once a year. Ironwood's GA came about four months later than its Nov 2025 "coming weeks" guidance. The TPU 8 "GA later this year" promise is still unconfirmed with seven weeks of 2026 left. Several partner milestones for 2027 (Oracle, Crux AI, Anthropic's multi-gigawatt build-outs) have not been reached yet.

### Cited Findings

| Commitment (date made) | Due | Status as of 14 Nov 2026 | Source |
|---|---|---|---|
| Ironwood availability "later this year" (9 Apr 2025) | 2025 | **Partly met / slipped.** Preview 24 Nov 2025; GA 31 Mar 2026. | [Google blog 9 Apr 2025](https://blog.google/products/google-cloud/ironwood-tpu-age-of-inference/); [release notes](https://docs.cloud.google.com/tpu/docs/release-notes) [CS] |
| Ironwood "GA in the coming weeks" (6 Nov 2025) | late 2025 | **Slipped.** GA 31 Mar 2026. | [Google Cloud blog 6 Nov 2025](https://cloud.google.com/blog/products/compute/ironwood-tpus-and-new-axion-based-vms-for-your-ai-workloads); [release notes](https://docs.cloud.google.com/tpu/docs/release-notes) [CS] |
| Anthropic: "well over a gigawatt of capacity online in 2026" (23 Oct 2025) | 2026 | **In progress.** Broadcom: "the 1 gigawatt of Ironwood we are deploying in 2026" (2 Sep 2026). Mizuho: "nearly a gigawatt" online this year (Oct 2026). | [Anthropic 23 Oct 2025](https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services) [CS-Anthropic]; [Investing.com Broadcom transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-broadcom-tops-q3-2026-estimates-as-ai-sales-surge-93CH-4886849) [CS-Broadcom]; [CNBC 28 Oct 2026](https://www.cnbc.com/2026/10/28/google-alters-cloud-playbook-turning-to-partners-to-sell-more-ai-chips.html) [AE: Mizuho] |
| TPU 8t/8i "generally available later this year" (22 Apr 2026) | 2026 | **Pending / unconfirmed.** Broadcom began production shipments of v8i by 2 Sep 2026. No GA note found. | [Google blog 22 Apr 2026](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/) [CS]; [Broadcom transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-broadcom-tops-q3-2026-estimates-as-ai-sales-surge-93CH-4886849) [CS-Broadcom] |
| Deliver TPUs into select customers' data centers (29 Apr 2026) | 2026 | **Met.** First revenue recognized in Q2 2026; most revenue expected in 2027. | [The Register 30 Apr 2026](https://www.theregister.com/off-prem/2026/04/30/google-to-sell-its-tpus-to-some-customers/5220078); [Q2 transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-alphabet-beats-q2-2026-estimates-shares-fall-on-capex-surge-93CH-4807140) [CS] |
| TorchTPU (preview Apr 2026) | — | **Advanced.** Open-sourced Oct 2026, per Google. | [Cloud blog 22 Apr 2026](https://cloud.google.com/blog/products/compute/ai-infrastructure-at-next26); [Google blog 9 Nov 2026](https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/tpu-8i-max-and-8tx/) [CS] |
| Crux AI: first 500 MW online (18 May 2026) | 2027 | **Pending** (scheduled for 2027). | [Business Wire 18 May 2026](https://www.businesswire.com/news/home/20260518367552/en/Blackstone-Announces-Joint-Venture-with-Google-to-Create-New-TPU-Cloud) [CS-Blackstone, SS] |
| TPUs on Oracle OCI (27 Oct 2026) | calendar 2027 | **Pending.** | [Press release 27 Oct 2026](https://www.googlecloudpresscorner.com/2026-10-27-Oracle-Brings-Google-TPUs-to-Oracle-Cloud-Infrastructure) [CS-Oracle/Google] |
| Anthropic about 3.5 GW of next-generation TPU capacity via Broadcom (6 Apr 2026) | from 2027 | **Pending.** Conditional on "Anthropic's continued commercial success". | [Broadcom 8-K via StockTitan, 6 Apr 2026](https://www.stocktitan.net/sec-filings/AVGO/8-k-broadcom-inc-reports-material-event-35aab0650b17.html) [SEC] |
| Anthropic 5 GW of TPU v8i (2 Sep 2026) | 2027 | **Pending** (expectation stated by Broadcom). | [Broadcom transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-broadcom-tops-q3-2026-estimates-as-ai-sales-surge-93CH-4886849) [CS-Broadcom] |
| Further 10 GW for Anthropic (2 Sep 2026) | 2028 | **Not a commitment** ("clear line of sight"). | same [CS-Broadcom] |
| Project Suncatcher: two prototype TPU satellites with Planet (4 Nov 2025) | "by early 2027" | **Pending.** | [Google Research blog, 4 Nov 2025](https://research.google/blog/exploring-a-space-based-scalable-ai-infrastructure-system-design/) [CS] |
| 2027 capex details "on our Q4 call" (28 Oct 2026) | ~early 2027 | **Not yet happened.** | [CNBC 28 Oct 2026](https://www.cnbc.com/2026/10/28/alphabet-googl-earnings-q3-2026.html) [CS] |
| Broadcom long-term agreement: develop and supply future TPU generations; supply assurance for networking and rack components through 2031 (6 Apr 2026) | through 2031 | **In force** (signed). | [Broadcom 8-K via StockTitan](https://www.stocktitan.net/sec-filings/AVGO/8-k-broadcom-inc-reports-material-event-35aab0650b17.html) [SEC] |

### Inferences
- [INF] Google has met its yearly cadence of *announcements*: Trillium GA in Dec 2024, Ironwood announced Apr 2025 and GA Mar 2026, TPU 8 announced Apr 2026. The gap between announcement and GA, however, was about 12 months for Ironwood. By Google's own account the TPU 8 gap would be under 9 months if GA arrives in 2026, which is not confirmed.

### Gaps
- I did not verify announcement and GA dates for v5e and v5p, or Trillium's announcement date. See section 1.
- I did not check whether any Cipher or Fluidstack site met its "initial delivery by Sep 2026" target (Sacra).

---

## 3. Financials (Alphabet does not report TPU revenue separately)

### Takeaway
Google Cloud revenue roughly doubled year on year to $30.7B in Q3 2026, with a 36.2% operating margin. Cloud backlog reached $560.8B on 30 Sep 2026. Alphabet says sales of TPU systems for customer sites, which began in Q2 2026, were "a meaningful contributor" to growth in Q3, but it gives no figure for them.

Funding the build-out took:
- Capex of $91.4B in 2025, with 2026 guidance of $195–205B and a "significant" increase promised for 2027.
- Long-term debt up from $10.9B at end-2024 to $125.1B on 30 Sep 2026.
- An $80B equity program started in June 2026.
- Off-balance-sheet credit backstops for third-party data centers.

### Cited Findings

#### Google Cloud segment by quarter
Figures are $ millions; margins and growth rates are my own arithmetic.

| Quarter | Revenue | Operating income | Op. margin | Source |
|---|---|---|---|---|
| Q1 2025 | 12,260 | ≈2,200 (release says "$2.2 billion") | ≈18% | [Q1 2026 10-Q](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000048/goog-20260331.htm); [Q1 2026 release, 29 Apr 2026](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000043/googexhibit991q12026.htm) [SEC] |
| Q2 2025 | 13,624 | 2,826 | 20.7% | [Q2 2026 release, 22 Jul 2026](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000066/googexhibit991q22026.htm) [SEC] |
| Q3 2025 | 15,157 | 3,594 | 23.7% | [Q3 2026 release, 28 Oct 2026](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000080/googexhibit991q32026.htm) [SEC] |
| Q4 2025 | 17,664 (Q4 2024: 11,955) | 5,313 (Q4 2024: 2,093) | 30.1% | [Q4 2025 release, 4 Feb 2026](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000012/googexhibit991q42025.htm) [SEC] |
| Q1 2026 | 20,028 (+63% y/y) | ≈6,600 ("$6.6 billion") | ≈33% | [Q1 2026 10-Q](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000048/goog-20260331.htm); [Q1 2026 release](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000043/googexhibit991q12026.htm) [SEC] |
| Q2 2026 | 24,768 (+82% y/y) | 8,814 | 35.6% | [Q2 2026 release](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000066/googexhibit991q22026.htm) [SEC] |
| Q3 2026 | 30,709 (+103% y/y) | 11,121 | 36.2% | [Q3 2026 release](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000080/googexhibit991q32026.htm) [SEC] |

- **Nine-month total.** Cloud revenue was $75,505M for 9M 2026, against $41,041M for 9M 2025. [SEC] — [Q3 2026 10-Q](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000084/goog-20260930.htm)
- **Q3 2026 explanation.** Release: "TPU systems sales were also a meaningful contributor to revenue growth." 10-Q: the $7.5B rise in Cloud operating income was "partially offset by increases in inventory and related costs associated with the sale of TPU systems and usage costs for technical infrastructure." [SEC] — [Q3 2026 release](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000080/googexhibit991q32026.htm); [SS on 10-Q wording]
- **Market reaction (28 Oct 2026).** Cloud revenue of $30.7B compared with a $28.7B consensus. Alphabet's total operating income of $40.58B missed FactSet's $43.19B. It was the "first top-and-bottom-line miss in nearly four years", and the shares fell more than 10%. [PR] — [CNBC, Samantha Subin, 28 Oct 2026](https://www.cnbc.com/2026/10/28/alphabet-googl-earnings-q3-2026.html)
- **Wiz.** Since March 2026 the Cloud segment includes Wiz; the XBRL tag shows a 11 Mar 2026 acquisition date. [SS / PR] — [sec-api.io analysis of Q3 2026 10-Q](https://sec-api.io/insights/alphabet-googl-q3-2026-earnings-sec-filing-analysis); [Q1 2026 10-Q](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000048/goog-20260331.htm)

#### Backlog (remaining performance obligations)
- **Q3 2025.** SemiAnalysis attributed most of the $49B rise in Cloud backlog that quarter to Anthropic's rented TPUs. [AE: SemiAnalysis] — [SemiAnalysis, 28 Nov 2025](https://newsletter.semianalysis.com/p/tpuv7-google-takes-a-swing-at-the)
- **31 Mar 2026.** $467.6B total, of which $462.3B was Google Cloud. From Q1 2026 the definition includes contracts of one year or less, which added about $7.3B. Pichai described this as "backlog nearly doubling quarter on quarter to over $460 billion", which implies roughly $240B at end-2025. [SEC/CS] — [Q1 2026 10-Q](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000048/goog-20260331.htm); [Q1 2026 release](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000043/googexhibit991q12026.htm)
- **30 Jun 2026.** $519.5B total, of which $513.9B was Cloud; "just over 50%" is expected to be recognized within 24 months. Ashkenazi declined to say how much of the backlog is TPU sales agreements. [SEC] — [Q2 2026 10-Q](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000071/goog-20260630.htm); [SS: Yahoo Finance, "Alphabet Q2 earnings call highlights"](https://finance.yahoo.com/technology/ai/articles/alphabet-q2-earnings-call-highlights-220547983.html)
- **30 Sep 2026.** $567.7B total, of which $560.8B was Cloud; "just over 55%" is expected within 24 months. The total includes $16.8B from Crux AI, a related party. [SEC] — [Q3 2026 10-Q](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000084/goog-20260930.htm)

#### Capex and depreciation
**Capex** (purchases of property and equipment):
- **Full years.** FY2024 $52,535M; FY2025 $91,447M, of which Q4 2025 was $27,851M. [SEC] — [Q4 2025 release](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000012/googexhibit991q42025.htm)
- **2026 quarters.** Q1 about $35.7B, of which "approximately 60 percent" of technical-infrastructure spend went on servers. Q2 $44,924M. Q3 $51,355M. Nine months $131,953M, against $63,596M in 9M 2025. [SEC/CS] — [The Register](https://www.theregister.com/off-prem/2026/04/30/google-to-sell-its-tpus-to-some-customers/5220078); [Q2 release](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000066/googexhibit991q22026.htm); [Q3 release](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000080/googexhibit991q32026.htm); [Q3 10-Q](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000084/goog-20260930.htm)

**2026 capex guidance over time** [CS]:
- 4 Feb 2026: $175–185B. — [Q4 2025 release](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000012/googexhibit991q42025.htm)
- 29 Apr 2026: $180–190B; the increase reflects needs at Intersect, the energy and infrastructure company Google acquired earlier in 2026. — [The Register](https://www.theregister.com/off-prem/2026/04/30/google-to-sell-its-tpus-to-some-customers/5220078)
- 22 Jul 2026: $195–205B, attributed to faster capacity delivery. — [Q2 transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-alphabet-beats-q2-2026-estimates-shares-fall-on-capex-surge-93CH-4807140)
- 28 Oct 2026: held at $195–205B.

**2027 outlook** [CS]: "We continue to expect our capex to increase significantly in 2027, and will provide further details on our Q4 call" (Ashkenazi, 28 Oct 2026). CNBC separately wrote that capex is expected to exceed $300B in 2027; the article does not clearly attribute that figure. — [CNBC 28 Oct 2026](https://www.cnbc.com/2026/10/28/alphabet-googl-earnings-q3-2026.html)

**Depreciation** of property and equipment [SEC]:
- FY2024 $15,311M; FY2025 $21,136M.
- 6M 2026 $13,586M, against $9,485M for 6M 2025.
- 9M 2026 $21,955M, against $15,096M for 9M 2025.
- Ashkenazi (22 Jul 2026): this "will continue to put pressure on the P&L in the form of higher depreciation expense."
- Sources: [Q4 2025 release](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000012/googexhibit991q42025.htm); [Q2 10-Q](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000071/goog-20260630.htm); [Q3 10-Q](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000084/goog-20260930.htm); [Q2 transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-alphabet-beats-q2-2026-estimates-shares-fall-on-capex-surge-93CH-4807140)

**Inventory** [SEC]: $2,439M (31 Dec 2025), $9,991M (30 Jun 2026), $13,308M (30 Sep 2026). It "consists primarily of hardware related to TPU systems for sale to enterprise customers". Kurian (28 Oct 2026) said "all of the inventory" for TPU systems ties to committed contracts. — [Q2 10-Q](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000071/goog-20260630.htm); [Q3 10-Q](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000084/goog-20260930.htm); [Asymmetric Curiosity, 9 Nov 2026](https://asymmetriccuriosity.substack.com/p/google-is-selling-the-tpu)

**Free cash flow:**
- Q2 2026: −$5,855M. Q3 2026: −$9,065M. Trailing twelve months to Q3 2026: $19,747M. [SEC] — [Q2 release](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000066/googexhibit991q22026.htm); [Q3 release](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000080/googexhibit991q32026.htm)
- Q3 operating cash flow also absorbed the TPU inventory build and a one-time payment of about $5.2B tied to a 2018 European Commission fine. [PR] — [Vested Finance, 29 Oct 2026](https://vestedfinance.com/blog/us-stocks/alphabet-q3-2026-earnings-ai-boom-meets-a-cash-crunch/)

**Purchase commitments.** $811.0B (30 Jun 2026) and $924.4B (30 Sep 2026). [PR: third-party reading of 10-Qs] — [sec-api.io](https://sec-api.io/insights/alphabet-googl-q3-2026-earnings-sec-filing-analysis)

#### Cash, debt, equity and backstops

**Cash, cash equivalents and marketable securities** [SEC]:
- $95,657M (31 Dec 2024); $126,843M (31 Dec 2025); $242,474M (30 Jun 2026); $265,098M (30 Sep 2026).
- At 30 Sep 2026, marketable equity securities included $75.2B of SpaceX shares under short-term sale restrictions.
- Sources: [Q4 2025 release](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000012/googexhibit991q42025.htm); [Q2 release](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000066/googexhibit991q22026.htm); [Q3 10-Q](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000084/goog-20260930.htm)
- CNBC reported a $99.03B gain on equity holdings in Q2 2026 (SpaceX and Anthropic stakes) and an $8.66B loss in Q3. [PR] — [CNBC 28 Oct 2026](https://www.cnbc.com/2026/10/28/alphabet-googl-earnings-q3-2026.html)

**Long-term debt** [SEC]:
- $10,883M (31 Dec 2024); $46,547M (31 Dec 2025); $77,501M (31 Mar 2026); $98,165M (30 Jun 2026); $125,102M (30 Sep 2026). CNBC gives $21.6B a year earlier, at 30 Sep 2025.
- Debt raised in 9M 2026: net proceeds of $85,222M; repayments of $8,879M.
- Sources: [Q4 2025 release](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000012/googexhibit991q42025.htm); [Q1 10-Q](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000048/goog-20260331.htm); [Q2 10-Q](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000071/goog-20260630.htm); [Q3 10-Q](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000084/goog-20260930.htm)

**Notes outstanding by series at 31 Mar 2026** (face value), from [Q1 2026 10-Q](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000048/goog-20260331.htm) [SEC]:
- 2025 issues: US dollar notes $22.5B (maturing 2028–2075, coupons 3.88–5.70%, including $500M of floating-rate notes); euro notes $15.265B (2028–2064).
- 2026 issues: US dollar notes $20.0B (2029–2066; weighted-average coupon 4.80%); sterling notes £5.5B, or $7.31B (2029–2126, so including a tranche maturing in 2126; weighted-average coupon 5.31%); Swiss franc notes CHF 3.1B, or $3.833B.
- Commercial paper: a program of up to $25B, with nothing outstanding at 31 Dec 2025 or 31 Mar 2026.

**Further 2026 debt detail:**
- The 100-year sterling tranche was £1B at 6.125%, priced on 10 Feb 2026, within a global raise of about $31.5B. [PR via SS: Reuters] — [RTÉ/Reuters, 11 Feb 2026](https://www.rte.ie/news/business/2026/0211/1557832-alphabet-sells-rare-100-year-bond-to-fund-ai-expansion/)
- Later in 2026, Q2 XBRL tags refer to 2026 notes in euros, Canadian dollars and yen, but I did not retrieve the amounts. [SEC] — [Q2 10-Q](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000071/goog-20260630.htm)

**Equity program (1 Jun 2026)**, from [Alphabet FWP, 1 Jun 2026](https://www.sec.gov/Archives/edgar/data/0001652044/000119312526251733/d160205dfwp.htm) [SEC]: equity offerings "totaling $80 billion", made up of:
- $15B of mandatory convertible preferred (depositary shares), converting around 15 May 2029.
- $15B of Class A and Class C common stock.
- A $40B at-the-market (ATM) program; about $30B of its proceeds are earmarked for 2026 employee equity tax obligations.
- A $10B private placement to Berkshire Hathaway: $5B of Class A at $351.81 and $5B of Class C at $348.20.

**Equity actually raised.** About $62.0B of new equity in 9M 2026, including $12.4B through the ATM. [PR: sec-api.io] About $27.6B of the ATM remains, and no buybacks were made in Q3. [PR: Vested Finance] — [sec-api.io](https://sec-api.io/insights/alphabet-googl-q3-2026-earnings-sec-filing-analysis); [Vested Finance](https://vestedfinance.com/blog/us-stocks/alphabet-q3-2026-earnings-ai-boom-meets-a-cash-crunch/)

**Data-center backstops**, from [Q1 2026 10-Q](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000048/goog-20260331.htm) [SEC]:
- Alphabet backstops "certain payment obligations relating to data centers" and books them as credit derivatives. Gross notional was $16.9B at 31 Dec 2025 and $28.4B at 31 Mar 2026. In April 2026 it signed further backstops of about $15.3B notional. Remaining terms run up to 15 years.
- Backstops of energy-infrastructure VIEs are booked as financial guarantees.

**Anthropic investment commitments** [SEC]:
- Q1 2026 10-Q: a private investment with a $10.0B capital commitment, plus $30.0B contingent on milestones through 2030, booked as an equity derivative.
- Q2 and Q3 10-Qs: $20.0B of future funding with "a private company".
- The Anthropic S-1 identifies Google as that investor.
- Sources: [Q1 10-Q](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000048/goog-20260331.htm); [Equibles, 27 Oct 2026, updated 3 Nov 2026](https://equibles.com/research/anthropics-s-1-checked-against-amazon-google-microsoft-and-broadcom-filings)

#### Management statements on TPU demand and capacity
- **Nov 2025 (Google spokesperson):** "We are experiencing accelerating demand for both our custom TPUs and Nvidia GPUs." [CS] — [CNBC, Kif Leswing, 25 Nov 2025](https://www.cnbc.com/2025/11/25/nvidia-says-its-gpus-are-a-generation-ahead-of-googles-ai-chips.html)
- **22 Jul 2026.** Pichai: "we continue to be supply constrained." Ashkenazi: "We're still in a supply constraint environment" and "we plan to expand the use of third-party capacity in Q3 as a bridging strategy", which "will create modest margin pressure in the near term." [CS] — [Q2 transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-alphabet-beats-q2-2026-estimates-shares-fall-on-capex-surge-93CH-4807140)
- **Sep 2026, Goldman Sachs conference.** Kurian said Google's AI servers pay for themselves in under two years, and servers on Google's own silicon reach payback in roughly half that time: "It's because we can optimize that whole stack." [CS] — [CNBC, Sigalos & Novet, 28 Oct 2026](https://www.cnbc.com/2026/10/28/google-alters-cloud-playbook-turning-to-partners-to-sell-more-ai-chips.html)
- **28 Oct 2026.** Pichai: "We're also seeing strong demand for our TPU systems across a wide range of customers." [CS] — [Q3 release](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000080/googexhibit991q32026.htm). Kurian cited "extraordinary demand and strong growth from both AI labs" (his first public earnings-call remarks). [CS] — [CNBC 28 Oct 2026](https://www.cnbc.com/2026/10/28/alphabet-googl-earnings-q3-2026.html)

#### Analyst estimates (clearly labeled; all relayed by CNBC on 28 Oct 2026 unless noted)
Source for this subsection unless noted: [CNBC, 28 Oct 2026](https://www.cnbc.com/2026/10/28/google-alters-cloud-playbook-turning-to-partners-to-sell-more-ai-chips.html).
- [AE: TD Cowen] TPU sales of $9.4B in H2 2026 and $62.5B in 2027, at about 20% operating margin on TPU sales versus about 35% for the Cloud segment overall.
- [AE: Wells Fargo] About $9B of TPU sales in Q3 2026 and $99B "next year" (2027).
- [AE: SemiAnalysis] Ironwood costs about 44% less to own and operate than an Nvidia GB200 server.
- [AE: Mizuho] The Anthropic agreement brings "nearly a gigawatt" online this year. Mizuho described it as Google "arming its closest model competitor".
- [AE: William Blair] The Anthropic financing plan covers about half of Anthropic's 2027 needs.
- [AE: Mizuho, Vijay Rakesh] Broadcom AI revenue from Anthropic of $21B in 2026 and $42B in 2027 (estimate date not given). — [The Next Web, 7 Apr 2026](https://thenextweb.com/news/anthropic-google-broadcom-compute-deal)
- [AE: SemiAnalysis, 28 Nov 2025] Anthropic's 1M TPUs split into about 400k Ironwood bought as racks from Broadcom (about $10B) and about 600k rented through GCP (about $42B of RPO). Estimated price to Anthropic: about $1.60 per TPU-hour. — [SemiAnalysis](https://newsletter.semianalysis.com/p/tpuv7-google-takes-a-swing-at-the)

### Inferences
- [INF] The jump in Cloud margin (from 23.7% in Q3 2025 to 36.2% in Q3 2026) came while the TPU hardware business was ramping. The 10-Q says TPU-system inventory costs held back operating-income growth, and TD Cowen's estimate puts TPU-sale margins below the segment average. This points to TPU hardware sales being margin-dilutive at segment level, but Alphabet discloses no split.
- [INF] Quarterly depreciation was about $8.4B in Q3 2026 against about $5.6B in Q3 2025, roughly +49% year on year (derived from the 9M and 6M figures).
- [INF] The 9M 2026 equity raises (about $62B) roughly match the $80B program minus the unused ATM balance. The program was $80B, the ATM was $40B and $12.4B of it was used, which leaves $27.6B, consistent with Vested Finance.

### Gaps
- The exact Q1 2026 Cloud operating income (only "$6.6 billion" was retrieved), and the exact Q1 2025 figure.
- The year-end 2025 backlog figure (only implied as about $240B) and Q3 2025 backlog. The $155B figure I recall for Q3 2025 was not verified.
- Credit-backstop notionals at 30 Jun and 30 Sep 2026, and the Crux AI backstop terms. Both are in 10-Q notes I could not retrieve.
- Amounts of the 2025 bond deals by date, and of the later 2026 euro, Canadian-dollar and yen notes.
- Morgan Stanley, Jefferies or other TPU *unit* estimates: not found (search budget exhausted). The 4.3M / 10M / 35M shipment figures on tech-insider.org are attributed to The Next Web, but the TNW article contains no such numbers. Treat them as unsupported.

---

## 4. Customers and contracts: binding versus only announced

### Takeaway
Anthropic is by far the largest and best-documented TPU customer. Its S-1 shows a binding minimum of $114.5B of Google TPU spending from Apr 2026 to Jul 2033. Separately it has Broadcom-supplied TPU racks financed through five-year leases: $161.2B of rent excluding interest, financed partly by a $63B bank and Blackstone vehicle closed in Oct 2026.

Meta reportedly signed a TPU rental deal in Feb 2026, unconfirmed by either company. OpenAI's reported purchase plan (Oct 2026) is also unconfirmed. Oracle (Oct 2026) and Crux AI (May 2026) are announced channels. Google says TPUs have "nearly 100 customers".

### Cited Findings

#### Anthropic

**Oct 2025 announcement:**
- 23 Oct 2025: "up to one million TPUs", "worth tens of billions of dollars", expected to bring "well over a gigawatt of capacity online in 2026". Amazon remains the "primary training partner and cloud provider". [CS-Anthropic] — [Anthropic, "Expanding our use of Google Cloud TPUs and Services", 23 Oct 2025](https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services)
- Wording: "up to", a ceiling. The binding minimum appears later in the S-1, below.

**Broadcom rack orders:**
- Hock Tan, 11 Dec 2025: "We received a $10 billion order to sell the latest TPU Ironwood racks to Anthropic." Anthropic then placed an additional $11B order in Broadcom's fiscal Q4 2025, ordering directly from Broadcom. [CS-Broadcom] — [CNBC, Leswing & Sigalos, 11 Dec 2025](https://www.cnbc.com/2025/12/11/broadcom-reveals-its-mystery-10-billion-customer-is-anthropic.html)
- Status: firm orders.

**Apr 2026 expansion:**
- 6 Apr 2026: "multiple gigawatts of next-generation TPU capacity that we expect to come online starting in 2027". Anthropic called it "our most significant compute commitment to date" (CFO Krishna Rao). Run-rate revenue had "surpassed $30 billion". [CS-Anthropic] — [Anthropic, "Anthropic expands Google and Broadcom compute deal", 6 Apr 2026](https://www.anthropic.com/news/google-broadcom-partnership-compute)
- Broadcom 8-K, same day: Anthropic "will access through Broadcom approximately 3.5 gigawatts" from 2027, "dependent on Anthropic's continued commercial success". No financial terms. [SEC] — [StockTitan copy of Broadcom 8-K, 6 Apr 2026](https://www.stocktitan.net/sec-filings/AVGO/8-k-broadcom-inc-reports-material-event-35aab0650b17.html)
- Status: conditional.

**Broadcom's Sep 2026 call (2 Sep 2026)**, from [Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-broadcom-tops-q3-2026-estimates-as-ai-sales-surge-93CH-4886849) and [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/) [CS-Broadcom]:
- "1 gigawatt of Ironwood we are deploying in 2026", "another 5 gigawatts of TPU v8i in 2027", and "clear line of sight" to "an incremental 10 gigawatts" in 2028.
- Anthropic is "on track to become our largest XPU customer in 2027".
- On Anthropic's economics: "every gigawatt of compute they deploy, they could achieve $30 billion of ARR".
- CFO: "We closed the first $35 billion tranche in June for Anthropic's 1 gigawatt deployment", using third-party financial partners, and "we may provide modest residual value guarantees".

**Anthropic S-1** (filed 26 Oct 2026; amended 2 Nov 2026), via [Equibles, 27 Oct 2026, updated 3 Nov 2026](https://equibles.com/research/anthropics-s-1-checked-against-amazon-google-microsoft-and-broadcom-filings) and [CNBC live updates, 26 Oct 2026](https://www.cnbc.com/2026/10/26/anthropic-ipo-live-updates-ai-s-1-filing.html) [SEC as relayed]:
- **Google TPU minimum spend.** At least $114.5B from Apr 2026 to Jul 2033, with a true-up payment. Anthropic can exit only on Google's uncured breach. Status: binding.
- **Possible amendment.** One search-summarized source says an amendment raised the minimum to about $121.3B. [SS, unconfirmed]
- **Further TPU compute.** Anthropic estimates $125–150B more TPU compute from providers including Google in 2028–2031. Status: not fixed.
- **Broadcom master equipment leases.** Dated 31 Mar 2026, five-year terms, $161.2B of rent excluding interest; the "2026 Lease" alone is about $125.2B. Status: binding.
- **Broadcom convertible notes.** Up to $42.0B, "solely to finance quarterly rent obligations under the 2026 Lease Arrangement".
- **Google investment terms.** Google can still buy up to $10B of Class N stock at the IPO price; $20B of notes remain available to it; its stake is capped at 14.99%.
- **Aggregate compute obligations.** About $417B of future compute payments.

**Contracted compute by chip type** (reported from the S-1): Nvidia 4.7 GW, TPU 4.5 GW, Trainium 1.2 GW, AMD 0.8 GW. [PR, citing X posts that quote the S-1] — [Wccftech, Rohail Saleem, 27 Oct 2026](https://wccftech.com/nvidia-gpus-make-up-4-7-gw-of-anthropics-contracted-compute-topping-4-5-gw-of-cheaper-google-tpus-as-lenders-bet-on-nvidias-residual-value/)

**Financing of the Broadcom-supplied TPUs:**
- **Apollo arrangement.** Broadcom's 10-Q filed 9 Jun 2026 describes an 8 Jun deal with Apollo and a backstop with "maximum exposure of $29 billion". The S-1 does not name Apollo. [SEC as relayed] — [Equibles](https://equibles.com/research/anthropics-s-1-checked-against-amazon-google-microsoft-and-broadcom-filings)
- **$63B vehicle (26 Oct 2026).** A special-purpose vehicle buys Broadcom TPU hardware and leases it to Anthropic. Bank of America, Citi and Morgan Stanley provide first-lien financing and Blackstone the second lien; Broadcom provides residual-value support; deliveries start in 2027. [PR via SS] — [Dealroom](https://dealroom.co/news/166809-blackstone-banks-line-up-63b-to-fund-broadcom-ai-chips-for-anthropic/); [Venture Atlas, 26 Oct 2026](https://www.ventureatlas.org/news/2026-10-26-broadcom-anthropic-compute-lease)
- **Deal nearly stalled.** The WSJ reported the deal stalled until Broadcom's CEO offered banks a higher interest rate and guarantees against losses. Lenders hold "higher conviction" that Nvidia GPUs keep more residual value than TPUs. [PR, citing WSJ] — [Wccftech, 27 Oct 2026](https://wccftech.com/nvidia-gpus-make-up-4-7-gw-of-anthropics-contracted-compute-topping-4-5-gw-of-cheaper-google-tpus-as-lenders-bet-on-nvidias-residual-value/)
- **FT report.** Google reportedly arranged a $200B financing plan for the Anthropic roll-out, involving Blackstone, Apollo, Morgan Stanley and Broadcom. [PR, citing the FT] — [Forbes Australia, Iain Martin, 3 Sep 2026](https://www.forbes.com.au/news/innovation/fluidstack-is-now-worth-18-billion/)

**Google equity in Anthropic.** A 31 Mar 2026 note purchase covered about $10.0B of Series G-2 shares (38.6M at $259.1364) plus up to $30.0B more. Google's $10.0B Series H purchase in May 2026 cut the remaining amount to $20.0B. Equibles estimates Google's stake at about 12%; this is its own arithmetic, not a filed figure. [SEC as relayed / AE: Equibles] — [Equibles](https://equibles.com/research/anthropics-s-1-checked-against-amazon-google-microsoft-and-broadcom-filings)

#### Meta
- **Nov 2025 report.** The Information reported that Meta could use Google TPUs in its own data centers. Nvidia shares fell 3% on 25 Nov 2025. [PR-U, as relayed by CNBC] — [CNBC, 25 Nov 2025](https://www.cnbc.com/2025/11/25/nvidia-says-its-gpus-are-a-generation-ahead-of-googles-ai-chips.html). Tom's Hardware's headline describes "renting Google Cloud TPUs next year, outright purchases in 2027"; only the headline was retrievable. — [Tom's Hardware](https://www.tomshardware.com/tech-industry/billion-dollar-ai-chip-deal-between-google-and-meta-could-be-on-the-cards-would-involve-renting-google-cloud-tpus-next-year-outright-purchases-in-2027)
- **Feb 2026 deal.** The Information (26 Feb 2026): Meta signed a multi-year, multibillion-dollar agreement to rent TPUs through Google Cloud. The same report said Google formed a joint venture with an unnamed large investment firm to lease TPUs to outside clients, with Meta as an early customer, and that Meta was in talks to buy TPUs outright for its own data centers from 2027. Neither company commented. [PR-U] — [WinBuzzer, Markus Kasanmascheff, 3 Mar 2026](https://winbuzzer.com/2026/03/03/meta-signs-multibillion-dollar-deal-rent-google-tpus-xcxwbn/); [BISI, Carlotta Kozlowskyj, 9 Mar 2026](https://bisi.org.uk/reports/metas-multibillion-dollar-deal-with-google-a-strategic-shift-in-the-ai-chip-market)
- **Status as of 14 Nov 2026.** The rental deal is reported but not confirmed by either company. No direct-purchase agreement was found.

#### OpenAI
- **2025 rental and denial.** The Information reported in 2025 that OpenAI had begun renting Google TPUs. OpenAI then said it had "no specific plans to use TPUs at present". [PR-U; OpenAI statement as relayed] — [Seoul Economic Daily, 28 Oct 2026](https://en.sedaily.com/international/2026/10/28/openai-weighs-buying-google-tpus-easing-nvidia-reliance)
- **Oct 2026 purchase report.** The Information (27 Oct 2026), citing "a person familiar with the matter", reported that OpenAI is pursuing a purchase of Google TPUs; volume and value were not disclosed. CNBC says it confirmed the report. OpenAI is hiring engineers "to optimize OpenAI's cutting-edge frontier models on TPUs". [PR-U / PR] — [Seoul Economic Daily, 28 Oct 2026](https://en.sedaily.com/international/2026/10/28/openai-weighs-buying-google-tpus-easing-nvidia-reliance); [CNBC 28 Oct 2026](https://www.cnbc.com/2026/10/28/google-alters-cloud-playbook-turning-to-partners-to-sell-more-ai-chips.html)
- **Status.** Reported only; no agreement announced.

#### Apple
- Apple trained its server model, AFM-server, on 8,192 TPUv4 chips (eight slices of 1,024 joined over the data-center network) and AFM-on-device on 2,048 TPUv5p, using AXLearn (built on JAX). Apple reports sustained model-FLOPs utilization (MFU) of "approximately 52%". [CS-Apple, independent of Google] — [Apple, "Apple Intelligence Foundation Language Models", arXiv v1 29 Jul 2024](https://arxiv.org/html/2407.21075v1)
- Status: published usage. No contract terms are disclosed.

#### Other named customers and channels
- **Citadel Securities**, named as a customer choosing TPUs (22 Apr 2026). [CS] — [Google blog](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/)
- **Lightricks** (trained LTX-2 on TPUs) and **Essential AI**, quoted on Ironwood (6 Nov 2025). [CS, with customer quotes] — [Google Cloud blog](https://cloud.google.com/blog/products/compute/ironwood-tpus-and-new-axion-based-vms-for-your-ai-workloads)
- **Customer count.** "Nearly 100 customers", including frontier labs, trading firms, retailers and universities (9 Nov 2026). [CS] — [Google blog](https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/tpu-8i-max-and-8tx/)
- **Oracle OCI** (announced 27 Oct 2026; 2027) and **Crux AI** (announced 18 May 2026; $16.8B in Alphabet's backlog). See section 1.
- **SemiAnalysis's list (Nov 2025)** of actual or likely external TPU customers: Meta, SSI, xAI and, as a potential customer, OpenAI. [AE: SemiAnalysis] — [SemiAnalysis, 28 Nov 2025](https://newsletter.semianalysis.com/p/tpuv7-google-takes-a-swing-at-the)

#### Neoclouds and Google financial backstops
Source unless noted: [Sacra, Fluidstack profile, accessed 14 Nov 2026](https://sacra.com/c/fluidstack) [PR].
- **TeraWulf, Lake Mariner (New York).** Fluidstack hosting deals of 10 years. Google backstops $3.2B of Fluidstack's obligations and receives about 14% of TeraWulf's equity on a pro forma basis.
- **TeraWulf, Abernathy, Texas.** A joint venture announced Oct 2025, with Google backing about $1.3B of lease obligations.
- **Cipher Mining.** About 207 MW in Texas. Google's total backstop is $1.73B, for about 5.4% of Cipher's equity on a pro forma basis.
- **Hut 8, River Bend (Louisiana).** 15 years, 245 MW, $7B of base-term revenue, with a Google financial backstop.
- **Forbes summary.** Fluidstack builds the data centers for Anthropic's 1M-TPU roll-out. The TeraWulf, Cipher and Hut 8 power deals together come to just under 1 GW, with "billions of dollars in backstops" from Google, first surfaced in SEC filings from Aug 2025. Fluidstack was valued at more than $18B. [PR] — [Forbes Australia, 3 Sep 2026](https://www.forbes.com.au/news/innovation/fluidstack-is-now-worth-18-billion/)
- **Alphabet's aggregate exposure.** Credit-derivative backstops of $16.9B at 31 Dec 2025 and $28.4B at 31 Mar 2026, plus about $15.3B more in April 2026. [SEC] — [Q1 2026 10-Q](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000048/goog-20260331.htm)
- **Neocloud reluctance.** Executives at Nebius, Lambda and CoreWeave told The Information they were not planning to adopt TPUs soon. Date not determined; paywalled. [PR via SS] — [The Information](https://feature.theinformation.com/articles/nebius-lambda-coreweave-say-tpus-amid-googles-push)

### Inferences
- [INF] **Binding versus announced:**
  - **Binding:** Anthropic's $114.5B minimum with Google; the Broadcom rack orders ($10B + $11B) and master leases ($161.2B of rent); the TeraWulf, Cipher and Hut 8 leases with Google backstops; Crux AI's commercial agreement ($16.8B in backlog).
  - **Conditional or expected:** Anthropic's 3.5 GW from 2027 and 5 GW of v8i in 2027.
  - **Not committed:** 10 GW in 2028.
  - **Reported only:** Meta's rental deal and purchase talks; OpenAI's purchase plan.
  - **Announced channels, not yet live:** Oracle (2027) and Crux AI capacity (2027).
- [INF] The joint venture in The Information's Feb 2026 Meta report, "a large investment firm", matches the Blackstone JV announced on 18 May 2026. Neither company has confirmed the link.

### Gaps
- **Meta's Aug 2025 Google Cloud deal** (reported as more than $10B over six years): not verified this session.
- **SSI (Apr 2025 TPU partnership), Midjourney, Salesforce:** not verified this session.
- **Original backstop sizes** of $1.8B (TeraWulf, Aug 2025) and $1.4B (Cipher, Sep 2025) from the brief: not verified. Sacra gives later totals of $3.2B and $1.73B.
- **Anthropic IPO:** whether it has priced as of 14 Nov 2026 was not checked.

---

## 5. Capacity: foundry, Broadcom and MediaTek, HBM, unit volumes, power and data centers

### Takeaway
Broadcom is the confirmed supplier for Ironwood and TPU v8i. It has a long-term agreement to supply future TPU generations, with supply assurance through 2031, and says it plans "multi-tens of billions of dollars of TPUs annually". MediaTek is tied to "v8t" by Broadcom's CEO.

Foundry nodes, HBM suppliers and unit volumes are mostly unconfirmed by Google. Power is the binding constraint. Ironwood superpods draw about 10 MW each, Google says it is "supply constrained", and capacity outside Google's own buildings now comes through Fluidstack, Crux AI and Oracle.

### Cited Findings
- **Broadcom long-term agreement (6 Apr 2026).** A "Long Term Agreement for Broadcom to develop and supply custom Tensor Processing Units", plus a "Supply Assurance Agreement" for networking and other components for Google's next-generation AI racks through 2031. [SEC] — [Broadcom 8-K via StockTitan](https://www.stocktitan.net/sec-filings/AVGO/8-k-broadcom-inc-reports-material-event-35aab0650b17.html)
- **Broadcom on the Sep 2026 call (2 Sep 2026).** "Multi-tens of billions of dollars of TPUs annually over the next several years"; Ironwood delivered "in high volume to both Anthropic and Google"; v8i production shipments under way, "designed with more memory and bandwidth compared to Ironwood". Broadcom has 6 XPU customers. AI semiconductor revenue was $16.7B in fiscal Q3 2026; the targets are about $115B for FY2027 and $230B for FY2028. [CS-Broadcom] — [Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-broadcom-tops-q3-2026-estimates-as-ai-sales-surge-93CH-4886849); [Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/)
- **Broadcom backlog.** Remaining performance obligations rose from $45.0B to $164.6B in the quarter ended 3 May 2026, including "a long-term contract for custom AI accelerators". [SEC as relayed] — [Equibles](https://equibles.com/research/anthropics-s-1-checked-against-amazon-google-microsoft-and-broadcom-filings)
- **MediaTek.** The only first-party statement found is from Broadcom: "Broadcom is now shipping the TPU v8i ahead of the MediaTek v8t, which in fact was initiated earlier" (2 Sep 2026). [CS-Broadcom] — [Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-broadcom-tops-q3-2026-estimates-as-ai-sales-surge-93CH-4886849)
- **AlphaChip and MediaTek.** Google DeepMind says MediaTek "extended" AlphaChip (26 Sep 2024). [CS-DeepMind] — [DeepMind blog](https://deepmind.google/discover/blog/how-alphachip-transformed-computer-chip-design/)
- **TSMC nodes:**
  - Trillium on N5. [AE: SemiAnalysis, 28 Nov 2025] — [SemiAnalysis](https://newsletter.semianalysis.com/p/tpuv7-google-takes-a-swing-at-the)
  - TPU 8t and 8i on TSMC N3. [PR: Crypto Briefing, 9 Nov 2026, presented as Google's specs] — [Crypto Briefing](https://cryptobriefing.com/google-tpu-8t-8i-training-inference-chips/)
  - Contradicted by "2nm". [PR, unattributed, low reliability] — [Tech-Insider, 23 Apr 2026](https://tech-insider.org/google-tpu-8t-8i-broadcom-mediatek-nvidia-2026/)
- **HBM capacity.** Ironwood 192 GB per chip [CS], which SemiAnalysis says is 8-Hi HBM3E against GB300's 288 GB of 12-Hi HBM3E [AE]. TPU 8i 288 GB [CS]. TPU 8t 216 GB [PR]. — [Google blog 9 Apr 2025](https://blog.google/products/google-cloud/ironwood-tpu-age-of-inference/); [SemiAnalysis](https://newsletter.semianalysis.com/p/tpuv7-google-takes-a-swing-at-the); [Google blog 22 Apr 2026](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/); [Crypto Briefing](https://cryptobriefing.com/google-tpu-8t-8i-training-inference-chips/)
- **Unit volumes:**
  - Anthropic: "up to one million TPUs" (Oct 2025). [CS-Anthropic]
  - SemiAnalysis split: about 400k bought and about 600k rented. [AE: SemiAnalysis]
  - Pod-scale reference points: 9,216 (Ironwood) and 9,600 (TPU 8t) chips per superpod; 134,000 TPU 8t in one fabric. [CS]
- **Power and data centers:**
  - A 9,216-chip Ironwood pod spans "nearly 10 MW". [CS] — [Google blog 9 Apr 2025](https://blog.google/products/google-cloud/ironwood-tpu-age-of-inference/)
  - Google's data centers deliver "six times more computing power per unit of electricity than five years ago" (22 Apr 2026). [CS] — [Google blog](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/)
  - Supply constrained; third-party capacity used as a bridge in Q3 2026 (22 Jul 2026). [CS] — [Q2 transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-alphabet-beats-q2-2026-estimates-shares-fall-on-capex-surge-93CH-4807140)
  - 2026 capex guidance raised in Apr 2026 to reflect the Intersect energy and infrastructure acquisition (XBRL date 10 Mar 2026). [CS] — [The Register](https://www.theregister.com/off-prem/2026/04/30/google-to-sell-its-tpus-to-some-customers/5220078); [Q1 10-Q](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000048/goog-20260331.htm)
  - SemiAnalysis: "power is the main bottleneck", and master services agreements can take up to three years. [AE] — [SemiAnalysis](https://newsletter.semianalysis.com/p/tpuv7-google-takes-a-swing-at-the)
  - Fluidstack is "on track for 1.3 gigawatts across more than 10 sites this year" (2026), has taken on more than $15B of debt, and has sites in Texas (near Abilene) and Arizona (Glendale). [PR] — [Forbes Australia, 3 Sep 2026](https://www.forbes.com.au/news/innovation/fluidstack-is-now-worth-18-billion/)

### Inferences
- [INF] The design split is that Broadcom makes v8i, as stated, and MediaTek is linked to v8t by Broadcom's CEO. This reverses the mapping in the brief's lead and in Tech-Insider's unsourced report (Broadcom for 8t "Sunfish", MediaTek for 8i "Zebrafish"). See section 9.
- [INF] TPU 8i Max puts two dies on one package (Google). This is a packaging route to more compute per package rather than a bigger single die. Google does not say whether reticle size drove that choice.

### Gaps
- No statements from MediaTek or TSMC about TPU work were found this session.
- Ironwood's process node is unverified.
- HBM vendors (SK hynix, Samsung, Micron) for any TPU generation are unverified.
- Google's CoWoS allocation is unverified.
- No credible TPU shipment-unit estimates (for example Morgan Stanley's) were verified.
- No Google figure for total TPU power deployed or under contract was found.

---

## 6. Key people (including notable departures)

### Takeaway
TPU strategy is fronted publicly by Amin Vahdat, who was promoted to SVP and Chief Technologist for AI and Infrastructure in 2025, and by Thomas Kurian. Pichai and Ashkenazi own the capex and TPU-sales disclosures. Norm Jouppi is first author of the TPU v1 and v4 architecture papers. The one leadership move found in 2026 is Benjamin Treynor Sloss leaving to run the Blackstone joint venture.

### Cited Findings
- **Sundar Pichai** (Alphabet CEO). Announced TPU sales into customer data centers (29 Apr 2026). On 28 Oct 2026: "strong demand for our TPU systems across a wide range of customers". [CS] — [The Register](https://www.theregister.com/off-prem/2026/04/30/google-to-sell-its-tpus-to-some-customers/5220078); [Q3 2026 release](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000080/googexhibit991q32026.htm)
- **Anat Ashkenazi** (CFO). Capex guidance, TPU revenue timing ("vast majority … in 2027"), supply constraints. [CS] — [Q2 transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-alphabet-beats-q2-2026-estimates-shares-fall-on-capex-surge-93CH-4807140)
- **Thomas Kurian** (Google Cloud CEO). Previously spent more than 20 years at Oracle and joined Google in late 2018. His first public earnings-call remarks were on 28 Oct 2026. He made the TPU payback claims (Sep 2026) and the Crux AI and "more partnerships" remarks (28 Oct 2026). [CS] — [CNBC 28 Oct 2026](https://www.cnbc.com/2026/10/28/google-alters-cloud-playbook-turning-to-partners-to-sell-more-ai-chips.html); [CNBC 28 Oct 2026](https://www.cnbc.com/2026/10/28/alphabet-googl-earnings-q3-2026.html); [Asymmetric Curiosity](https://asymmetriccuriosity.substack.com/p/google-is-selling-the-tpu)
- **Amin Vahdat.** Bylined "VP/GM, ML, Systems & Cloud AI" on 9 Apr 2025, and "Chief Technologist & SVP, AI & Infrastructure" on 6 Nov 2025, 22 Apr 2026 and 9 Nov 2026. He is quoted in the Oracle release (27 Oct 2026). [CS] — [Google blog 9 Apr 2025](https://blog.google/products/google-cloud/ironwood-tpu-age-of-inference/); [Google Cloud blog 6 Nov 2025](https://cloud.google.com/blog/products/compute/ironwood-tpus-and-new-axion-based-vms-for-your-ai-workloads); [Google blog 9 Nov 2026](https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/tpu-8i-max-and-8tx/); [Oracle/Google release](https://www.googlecloudpresscorner.com/2026-10-27-Oracle-Brings-Google-TPUs-to-Oracle-Cloud-Infrastructure)
- **Mark Lohmeyer** (VP & GM, AI & Computing Infrastructure), co-author of the Nov 2025 and Apr 2026 Cloud posts. [CS] — [Google Cloud blog 22 Apr 2026](https://cloud.google.com/blog/products/compute/ai-infrastructure-at-next26)
- **Norman P. Jouppi**, first author of the ISCA 2017 (TPU v1) and ISCA 2023 (TPU v4) papers. [CS] — [arXiv 1704.04760](https://arxiv.org/abs/1704.04760); [arXiv 2304.01433](https://arxiv.org/abs/2304.01433)
- **Benjamin Treynor Sloss**, a long-time Google infrastructure executive, named CEO of the Blackstone–Google TPU joint venture (18 May 2026). This is a move out of Google into the joint venture. [CS-Blackstone via SS] — [Business Wire](https://www.businesswire.com/news/home/20260518367552/en/Blackstone-Announces-Joint-Venture-with-Google-to-Create-New-TPU-Cloud)
- **Anna Goldie and Azalia Mirhoseini**, authors of the AlphaChip post (26 Sep 2024). [CS] — [DeepMind blog](https://deepmind.google/discover/blog/how-alphachip-transformed-computer-chip-design/)
- **People outside Google:**
  - Hock Tan (Broadcom CEO).
  - Krishna Rao (Anthropic CFO).
  - James Bradbury (Anthropic Head of Compute), quoted on Ironwood on 6 Nov 2025.
  - Mahesh Thiagarajan (President, OCI).
  - Josh Woods (Citadel Securities CTO), quoted by Google on 22 Apr 2026; the quote text was not retrievable.
  - [CS] — sources as cited in sections 1 and 4.

### Inferences
- [INF] Vahdat's title change between 9 Apr 2025 and 6 Nov 2025 points to a promotion in that window. I could not confirm the exact date.

### Gaps
- No verified list of TPU-team departures in 2025–2026 (for example to OpenAI, Anthropic, Nvidia/Groq or start-ups). Historical departures such as Jonathan Ross, who founded Groq, were not re-verified this session.
- Norm Jouppi's current role and title were not verified.

---

## 7. Legal and regulatory

### Takeaway
The one TPU-specific legal matter verified this session is the criminal trade-secret case against ex-Google engineer Linwei Ding. A jury convicted him on all 14 counts on 29 Jan 2026. In June 2026, by press report, the judge set aside the 7 economic-espionage counts, leaving 7 trade-secret theft convictions. Sentencing was pending at last report.

I could not re-verify the Singular Computing patent settlement, antitrust remedies touching AI or TPUs, or export-control matters, because the search budget ran out.

### Cited Findings
- **Linwei Ding (also known as Leon Ding), N.D. Cal.**
  - Jury verdict 29 Jan 2026 after an 11-day trial: guilty on 7 counts of economic espionage and 7 counts of theft of trade secrets.
  - The material included specifications for Google's TPU chips, GPU systems, and software that orchestrates thousands of chips into supercomputers. He copied more than 2,000 pages between May 2022 and Apr 2023.
  - Maximum penalties: 15 years per espionage count and 10 years per theft count. A status conference was set for 3 Feb 2026.
  - [PR] — [Decrypt, Jan 2026](https://decrypt.co/356455/former-google-engineer-convicted-of-stealing-ai-secrets-for-china)
- **Post-trial ruling.** Judge Vince Chhabria set aside the seven economic-espionage convictions; the seven theft convictions stand. He found Ding was not a flight risk, and sentencing was pending. Reported date: June 2026. [PR via SS; page blocked to my fetch] — [Courthouse News, "Judge acquits ex-Google engineer of economic espionage in AI secrets case"](https://www.courthousenews.com/judge-acquits-ex-google-engineer-of-economic-espionage-in-ai-secrets-case/)
- **Anthropic S-1 risk factors (26 Oct 2026).** The filing says reliance on Microsoft, Amazon, Google and Broadcom for compute "create[s] dependencies and potential vulnerabilities". It names Google as a competitor and warns that cloud providers including Google could disadvantage Anthropic's models in promotion or pricing. [SEC as relayed] — [CNBC live updates, 26 Oct 2026](https://www.cnbc.com/2026/10/26/anthropic-ipo-live-updates-ai-s-1-filing.html)

### Inferences
- [INF] Alphabet's 10-Qs call Anthropic "a private company" rather than naming it. The S-1 names Google. Anyone tracking the regulatory treatment of the investment has to rely on the S-1 for identity.

### Gaps
- **Singular Computing v. Google (D. Mass.).** My recollection is that the case settled on about 24 Jan 2024, before a jury verdict, that Singular had sought about $1.67B, and that the terms were not disclosed. I could not confirm this: Reuters blocked my fetch and the search budget was exhausted. Status: unverified.
- **Ding sentencing.** Whether sentencing has taken place as of 14 Nov 2026 is unknown.
- **Antitrust.** The DOJ search-case remedies (Judge Mehta, Sep 2025) and any provisions on Google's AI investments (for example Anthropic) were not verified. Any 2026 antitrust inquiry into TPU bundling or AI partnerships was not found.
- **Export controls.** Not verified: whether US rules restrict TPU sales or TPU cloud access for Chinese entities, and whether new 2026 rules affect TPU hardware sales into customer data centers.
- **Alphabet's own disclosures.** Legal-proceedings sections of the 2026 10-Qs were not retrievable because the documents were truncated.

---

## 8. Science and engineering: what is demonstrated, who verified it, what is unproven, physical limits, and whether it stands on solid ground

### Takeaway
That TPUs work at frontier scale is well established. The evidence:
- Google's peer-reviewed architecture papers (2017, 2023).
- Customer-published evidence: Apple trained its models on TPUv4 and v5p and reports about 52% MFU.
- Google's statement that Gemini 3 was trained entirely on TPUs.
- Anthropic's gigawatt-scale deployment.
- MLPerf submissions through 2025.

What is not independently verified: Ironwood's and TPU 8's performance-per-watt and performance-per-dollar multiples, and Google's cost-of-ownership (TCO) advantage over Nvidia. These rest on Google claims and on analyst estimates, mainly SemiAnalysis. I found no visible MLPerf submission for Ironwood or any TPU 8 chip.

### Cited Findings

#### Published papers (Google-authored, peer-reviewed venues)
- **ISCA 2017 (TPU v1).** Claims as in section 1. [CS, peer-reviewed] — [arXiv 1704.04760](https://arxiv.org/abs/1704.04760)
- **ISCA 2023 (TPU v4, optical circuit switches).** OCS under 5% of cost and under 3% of power. Faster and lower-power than an A100 system of similar size. Google-run cloud v4s use about 3x less energy and produce about 20x less CO2e than "contemporary DSAs in a typical on-premise data center". [CS, peer-reviewed] — [arXiv 2304.01433](https://arxiv.org/abs/2304.01433)

#### Evidence from outside users
- **Apple (Jul 2024).** AFM-server trained on 8,192 TPUv4 and AFM-on-device on 2,048 TPUv5p, with AXLearn on JAX. "The sustained model-flop-utilization (MFU) for this training run was approximately 52%." [IV: Apple, customer-published] — [arXiv 2407.21075 (HTML v1)](https://arxiv.org/html/2407.21075v1)
- **Anthropic.** Uses TPUs alongside Trainium and Nvidia GPUs. Kurian cited the "strong price-performance and efficiency" Anthropic's teams had seen with TPUs "for several years" (23 Oct 2025). [CS-Anthropic, with Google quote] — [Anthropic](https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services). Anthropic's S-1 says it will "select chips based on the best price-performance and efficiency characteristics for each workload". [SEC as relayed] — [CNBC 28 Oct 2026](https://www.cnbc.com/2026/10/28/google-alters-cloud-playbook-turning-to-partners-to-sell-more-ai-chips.html)
- **Gemini 3** was trained on TPUs rather than Nvidia GPUs, per Google (Nov 2025). [CS] — [CNBC 25 Nov 2025](https://www.cnbc.com/2025/11/25/nvidia-says-its-gpus-are-a-generation-ahead-of-googles-ai-chips.html); [CNBC 11 Dec 2025](https://www.cnbc.com/2025/12/11/broadcom-reveals-its-mystery-10-billion-customer-is-anthropic.html)
- **Academic TRC users.** No independent academic evaluation was retrieved this session (see Gaps).

#### MLPerf submissions found (Google directories in MLCommons results repositories)
All results are [IV: MLCommons peer-review process]. These are submission listings only; scores were not retrieved. Repository listings can be truncated.

| Round | TPU systems listed | Source |
|---|---|---|
| Training v3.1 | TPU v5e, 4,096 chips (PAX) | [repo](https://github.com/mlcommons/training_results_v3.1/tree/main/Google/systems) |
| Inference v4.0 | TPU v5e, 4 chips (plus H100 GPU systems) | [repo](https://github.com/mlcommons/inference_results_v4.0/tree/main/closed/Google/systems) |
| Inference v4.1 | TPU v5e, 4 chips; "tpu_v6", 4 chips (plus Nvidia systems) | [repo](https://github.com/mlcommons/inference_results_v4.1/tree/main/closed/Google/systems) |
| Training v4.1 | Trillium at 512–3,072 chips (MaxText); v5p at 16–2,048 chips (MaxDiffusion) and 4,096–12,288 chips (MaxText) | [repo](https://github.com/mlcommons/training_results_v4.1/tree/main/Google/systems) |
| Inference v5.0 | Trillium, 4 chips (plus B200 and H200) | [repo](https://github.com/mlcommons/inference_results_v5.0/tree/main/closed/Google/systems) |
| Training v5.0 | Trillium, 256 chips (MaxDiffusion) (plus H200 NeMo) | [repo](https://github.com/mlcommons/training_results_v5.0/tree/main/Google/systems) |
| Inference v5.1 | No TPU system visible (B200 and H200 only) | [repo](https://github.com/mlcommons/inference_results_v5.1/tree/main/closed/Google/systems) |
| Training v5.1 | No Google directory | [repo](https://github.com/mlcommons/training_results_v5.1) |
| Inference v6.0 | No TPU system visible (B200 and GB200 NVL72 only) | [repo](https://github.com/mlcommons/inference_results_v6.0/tree/main/closed/Google/systems) |
| Training v6.0 | No TPU system visible (GB200 NVL72 only) | [repo](https://github.com/mlcommons/training_results_v6.0/tree/main/Google/systems) |

#### Claims that remain unverified (company- or analyst-sourced only)
- **Ironwood.** 2x performance per watt versus Trillium; about 30x power efficiency versus the 2018 Cloud TPU; 10x peak versus v5p; more than 4x per chip versus v6e. [CS] — [Google blog 9 Apr 2025](https://blog.google/products/google-cloud/ironwood-tpu-age-of-inference/); [Google Cloud blog 6 Nov 2025](https://cloud.google.com/blog/products/compute/ironwood-tpus-and-new-axion-based-vms-for-your-ai-workloads)
- **El Capitan comparison.** Google says an Ironwood pod has "more than 24x" El Capitan's compute, using 42.5 EF against 1.7 EF. [CS] On the Nov 2024 TOP500 list, El Capitan's 1.742 EF is its HPL Rmax result. — [TOP500, Nov 2024](https://top500.org/lists/top500/2024/11/)
- **TPU 8.** Up to 2x performance per watt versus Ironwood; 80% better performance per dollar (8i); "nearly 3x" compute per pod and "up to 2.7x" training performance (8t); greater than 97% goodput target; "state-of-the-art price-performance" on InferenceX and AgentX. [CS] — [Google blog 22 Apr 2026](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/); [Google blog 9 Nov 2026](https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/tpu-8i-max-and-8tx/)
- **TCO and cost per FLOP** [AE: SemiAnalysis], from [SemiAnalysis, 28 Nov 2025](https://newsletter.semianalysis.com/p/tpuv7-google-takes-a-swing-at-the):
  - Ironwood's all-in TCO per chip is "~44% lower" than a GB200 server, from Google's internal view.
  - For external customers, up to about 30% lower than GB200 and about 41% lower than GB300.
  - At 40% MFU, Anthropic's cost per effective PFLOP is about 52% below GB300 NVL72, with break-even at about 19% MFU.
- **Server payback.** Kurian's claim that Google-silicon servers pay back in about half the time of AI servers generally (under two years). [CS] — [CNBC 28 Oct 2026](https://www.cnbc.com/2026/10/28/google-alters-cloud-playbook-turning-to-partners-to-sell-more-ai-chips.html)
- **AlphaChip.** Google says AlphaChip generated layouts for "the last three generations" of TPU (v5e, v5p and Trillium) and every generation since 2020, described as "superhuman or comparable". Google's page cites no independent replication. [CS] — [DeepMind blog, 26 Sep 2024](https://deepmind.google/discover/blog/how-alphachip-transformed-computer-chip-design/)

#### Software portability (JAX/XLA versus PyTorch)
- **PyTorch/XLA.** Release note "general availability (GA)" for PyTorch/XLA 1.6 on Cloud TPU, dated 20 Aug 2020. [CS] — [release notes](https://docs.cloud.google.com/tpu/docs/release-notes)
- **TorchTPU.** Native PyTorch "in preview with select customers" (22 Apr 2026); open-sourced in Oct 2026. Google also claims "native PyTorch and Hugging Face model support". [CS] — [Google Cloud blog](https://cloud.google.com/blog/products/compute/ai-infrastructure-at-next26); [Google blog 9 Nov 2026](https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/tpu-8i-max-and-8tx/)
- **SemiAnalysis assessment (28 Nov 2025)** [AE/PR], from [SemiAnalysis](https://newsletter.semianalysis.com/p/tpuv7-google-takes-a-swing-at-the):
  - TPU software is not as easy to use as CUDA, and out-of-the-box performance for external users is weaker.
  - The XLA:TPU compiler, runtime and MegaScale are not open source.
  - Meta's earlier PyTorch-XLA use (2020–2023) was not widely adopted and its contracts were canceled in 2023.
  - vLLM and SGLang TPU support is in beta via TorchAX, with limited model coverage and no MLA-friendly kernels yet.
  - A native PyTorch TPU backend was announced in the XLA repository in Oct 2025.
- **OpenAI.** Its job posting seeks engineers "to optimize OpenAI's cutting-edge frontier models on TPUs". The Information describes this work as early-stage (Oct 2026). [PR] — [Seoul Economic Daily](https://en.sedaily.com/international/2026/10/28/openai-weighs-buying-google-tpus-easing-nvidia-reliance)

#### Physical and engineering limits
- **Cooling.**
  - Ironwood 9,216-chip pods are liquid cooled, which "can sustain up to twice the performance of standard air cooling under continuous heavy loads". [CS] — [Google blog 9 Apr 2025](https://blog.google/products/google-cloud/ironwood-tpu-age-of-inference/)
  - Fleet liquid cooling at gigawatt scale, about 99.999% uptime since 2020. [CS] — [Google Cloud blog 6 Nov 2025](https://cloud.google.com/blog/products/compute/ironwood-tpus-and-new-axion-based-vms-for-your-ai-workloads)
  - Fourth-generation liquid cooling for TPU 8. [CS]
- **Optical circuit switching.**
  - v4: OCS under 5% of cost and under 3% of power. [CS, peer-reviewed]
  - Ironwood build: 48 OCS units of 144x144 ports, and about 1.5 transceivers per chip. [AE: SemiAnalysis]
  - Ironwood and TPU 8t use OCS for fault rerouting. [CS]
- **Scale of a pod.** 9,216 (Ironwood) and 9,600 (TPU 8t) chips per ICI domain; about 10 MW per Ironwood pod. [CS]
- **HBM capacity.** Ironwood has 192 GB against GB300's 288 GB [AE: SemiAnalysis]. TPU 8i moved to 288 GB [CS].
- **Package and die limits.** TPU 8i Max puts two 8i chips on one package. [CS]
- **Radiation (Project Suncatcher, 4 Nov 2025)** [CS], from [Google Research blog](https://research.google/blog/exploring-a-space-based-scalable-ai-infrastructure-system-design/):
  - Trillium was tested in a 67 MeV proton beam. HBM was the most sensitive component, with irregularities only after 2 krad(Si), nearly 3x the expected shielded five-year mission dose of 750 rad(Si). No hard failures from total ionizing dose up to 15 krad(Si).
  - A bench optical link reached 800 Gbps each way.
  - Google lists thermal management, ground links and on-orbit reliability as unsolved.

### Inferences
- [INF] **On solid ground:**
  - **Feasibility at scale.** Gemini, Apple's models and Anthropic's production use show TPUs train and serve frontier models. Apple's 52% MFU on an 8,192-chip TPUv4 job is the cleanest independent efficiency number found.
  - **Interconnect.** Optical-circuit-switched 3D-torus pods of about 9,000 chips have been in service across generations.
- [INF] **Not on solid ground:**
  - **Generation-over-generation multiples.** These are vendor claims. "Per pod" and "per chip" figures may mix FP4 and FP8, and the El Capitan comparison mixes Ironwood's peak figure with El Capitan's HPL result.
  - **TCO advantage.** It rests on SemiAnalysis's model, which uses Google's internal view.
  - **Benchmarks.** Google has not put Ironwood or TPU 8 into the public MLPerf rounds I could inspect.
  - **Lenders' view.** Lenders' preference for Nvidia residual values (WSJ via Wccftech) shows outside capital does not yet treat TPU hardware as equally fungible.

### Gaps
- MLPerf *scores* for TPU entries, and whether Google entered Ironwood in any round (for example an open or preview division), were not retrieved. The listings I saw may be incomplete.
- Papers after 2023: any ISCA, MICRO, NSDI or Hot Chips papers or presentations on TPU v5, Trillium, Ironwood or TPU 8 (2024–2026) were not retrieved.
- Independent critiques of AlphaChip (for example the CACM article by Igor Markov, or Cheng and Kahng's ISPD 2023 replication) could not be opened: CACM returned 403.
- No academic TPU Research Cloud (TRC) evaluations were retrieved.
- The InferenceX and AgentX results that Google cites were not checked.
- Reticle-limit data for TPU dies was not found.

---

## 9. Cross-examination log: Google's claims tested against Anthropic, Meta, OpenAI, Broadcom, MediaTek, TSMC, Nvidia and independent analysts

### Takeaway
Most tensions are about timing (Ironwood GA, TPU 8 GA), attribution (who designs which TPU 8 chip), and economics (TPU cost claims against lenders' and customers' revealed choices). The anchoring documents — Anthropic's S-1, Broadcom's filings and calls, and Alphabet's 10-Qs — largely corroborate the scale of TPU commitments. They differ on how the deals are structured and labeled.

### Cited Findings
1. **Ironwood availability.**
   - Google, 6 Nov 2025: GA "in the coming weeks" [CS].
   - Google's own release notes: Preview 24 Nov 2025, GA 31 Mar 2026 [CS].
   - The brief's premise of "GA about Nov 2025" is not supported.
   - Sources: [Cloud blog](https://cloud.google.com/blog/products/compute/ironwood-tpus-and-new-axion-based-vms-for-your-ai-workloads); [release notes](https://docs.cloud.google.com/tpu/docs/release-notes)
2. **TPU 8 design partners.**
   - Tech-Insider (23 Apr 2026, unsourced) and the brief's lead: Broadcom designs 8t ("Sunfish"), MediaTek designs 8i ("Zebrafish").
   - Broadcom's CEO (2 Sep 2026, two independent transcripts): Broadcom ships "TPU v8i … ahead of the MediaTek v8t".
   - Google's announcements name neither partner.
   - Sources: [Tech-Insider](https://tech-insider.org/google-tpu-8t-8i-broadcom-mediatek-nvidia-2026/); [Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-broadcom-tops-q3-2026-estimates-as-ai-sales-surge-93CH-4886849); [Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/)
3. **TPU 8 process node.**
   - TSMC N3 (Crypto Briefing, presented as Google specs) versus 2nm (Tech-Insider, unattributed).
   - No TSMC or Google statement was found.
   - Sources: [Crypto Briefing](https://cryptobriefing.com/google-tpu-8t-8i-training-inference-chips/); [Tech-Insider](https://tech-insider.org/google-tpu-8t-8i-broadcom-mediatek-nvidia-2026/)
4. **TPU 8t performance multiples.**
   - "Nearly 3x compute performance per pod" (22 Apr 2026) versus "up to 2.7x better training performance" (9 Nov 2026), both [CS].
   - Tech-Insider separately attributes "2.8x training price-performance" to Google.
   - The metrics differ and no independent measurement exists.
   - Sources: [Google 22 Apr 2026](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/); [Google 9 Nov 2026](https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/tpu-8i-max-and-8tx/)
5. **TPU 8 availability.**
   - "Generally available later this year" (Google, 22 Apr 2026) versus no GA evidence as of 14 Nov 2026.
   - Tech-Insider claims "broader external availability targeted for late 2027", attributed to Google and CNBC; I did not verify this.
6. **Anthropic's 2026 capacity.**
   - Anthropic (Oct 2025): "well over a gigawatt … in 2026".
   - Broadcom (Sep 2026): "1 gigawatt of Ironwood we are deploying in 2026".
   - Mizuho (Oct 2026): "nearly a gigawatt" this year.
   - Sources: [Anthropic](https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services); [Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-broadcom-tops-q3-2026-estimates-as-ai-sales-surge-93CH-4886849); [CNBC](https://www.cnbc.com/2026/10/28/google-alters-cloud-playbook-turning-to-partners-to-sell-more-ai-chips.html)
7. **Price-performance claims versus Anthropic's revealed mix.**
   - Google and Anthropic cite TPU "price-performance".
   - Anthropic's S-1 contracted compute, as reported, has Nvidia at 4.7 GW above TPU at 4.5 GW. Anthropic says it selects chips per workload.
   - Lenders favour Nvidia residual values. The $63B TPU financing needed Broadcom's added guarantees and higher rates (WSJ).
   - Sources: [Wccftech](https://wccftech.com/nvidia-gpus-make-up-4-7-gw-of-anthropics-contracted-compute-topping-4-5-gw-of-cheaper-google-tpus-as-lenders-bet-on-nvidias-residual-value/); [CNBC](https://www.cnbc.com/2026/10/28/google-alters-cloud-playbook-turning-to-partners-to-sell-more-ai-chips.html)
8. **Same TPUs, different labels.**
   - Alphabet's 10-Qs describe TPU hardware sales for customers' on-premises infrastructure. Anthropic's S-1 describes TPU capacity through Broadcom leases in facilities run by others. Neither filing links the two.
   - Broadcom books a sale of custom accelerators; Anthropic books finance leases.
   - Source: [Equibles](https://equibles.com/research/anthropics-s-1-checked-against-amazon-google-microsoft-and-broadcom-filings)
9. **Investor identity and size.**
   - Alphabet's 10-Qs say "a private company"; the S-1 names Google.
   - Amazon's MD&A lists Google's facility as $20.0B "original", while the S-1 says $30.0B.
   - Source: [Equibles](https://equibles.com/research/anthropics-s-1-checked-against-amazon-google-microsoft-and-broadcom-filings)
10. **OpenAI.**
    - 2025 reports of TPU rental versus OpenAI's 2025 statement of "no specific plans to use TPUs at present".
    - Oct 2026: a reported purchase plan, which CNBC says it confirmed, and a job posting for TPU optimization.
    - Source: [Seoul Economic Daily](https://en.sedaily.com/international/2026/10/28/openai-weighs-buying-google-tpus-easing-nvidia-reliance)
11. **Meta.**
    - A signed TPU rental (The Information, 26 Feb 2026) and purchase talks for 2027 are reported.
    - Neither Meta nor Google has commented.
    - Nvidia's public response in Nov 2025 implicitly disputed the case for ASICs.
    - Sources: [WinBuzzer](https://winbuzzer.com/2026/03/03/meta-signs-multibillion-dollar-deal-rent-google-tpus-xcxwbn/); [BISI](https://bisi.org.uk/reports/metas-multibillion-dollar-deal-with-google-a-strategic-shift-in-the-ai-chip-market)
12. **Nvidia versus Google versus analysts.** Source: [CNBC 25 Nov 2025](https://www.cnbc.com/2025/11/25/nvidia-says-its-gpus-are-a-generation-ahead-of-googles-ai-chips.html); [SemiAnalysis](https://newsletter.semianalysis.com/p/tpuv7-google-takes-a-swing-at-the)
    - Nvidia (25 Nov 2025): "We're delighted by Google's success … we continue to supply to Google"; "NVIDIA is a generation ahead of the industry — it's the only platform that runs every AI model and does it everywhere computing is done"; "NVIDIA offers greater performance, versatility, and fungibility than ASICs." [CS-Nvidia]
    - Google's response the same day: accelerating demand for "both our custom TPUs and Nvidia GPUs". [CS]
    - SemiAnalysis: Ironwood is about 10% short of GB200 on peak FLOPs and memory bandwidth, but its TCO is lower. [AE]
13. **Margins.**
    - Kurian: Google-silicon servers pay back in about half the time [CS].
    - TD Cowen: about 20% operating margin on TPU sales versus about 35% for the segment [AE].
    - Alphabet's 10-Q: TPU-system inventory costs partly offset Q3 2026 operating-income growth [SEC].
    - Sources: [CNBC](https://www.cnbc.com/2026/10/28/google-alters-cloud-playbook-turning-to-partners-to-sell-more-ai-chips.html); [Q3 10-Q](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000084/goog-20260930.htm)
14. **Third-party benchmarks disagree.**
    - SemiAnalysis disputes Artificial Analysis's finding that TPU v6e has about 5x worse performance per dollar than Nvidia GPUs. SemiAnalysis argues the test used an immature vLLM path and a $2.7/hour list price that large customers do not pay.
    - Source: [SemiAnalysis](https://newsletter.semianalysis.com/p/tpuv7-google-takes-a-swing-at-the)
15. **El Capitan comparison.**
    - Google's "more than 24x El Capitan" compares an Ironwood pod's peak figure (the captions reference FP8) with El Capitan's 1.742 EF HPL Rmax on TOP500.
    - Sources: [Google blog](https://blog.google/products/google-cloud/ironwood-tpu-age-of-inference/); [TOP500](https://top500.org/lists/top500/2024/11/)
16. **Neocloud adoption.**
    - Google pushed TPU hosting at neoclouds. Executives at Nebius, Lambda and CoreWeave told The Information they had no near-term TPU plans [PR via SS].
    - The channels that did materialize are Fluidstack, crypto-miner sites, Crux AI and Oracle.
    - Sources: [The Information](https://feature.theinformation.com/articles/nebius-lambda-coreweave-say-tpus-amid-googles-push); [Sacra](https://sacra.com/c/fluidstack)
17. **Shipment figures.**
    - Tech-Insider attributes 4.3M TPU shipments in 2026 and about 10M in 2027 to The Next Web.
    - The Next Web article (7 Apr 2026) contains no shipment estimates.
    - Tech-Insider is also internally inconsistent (10M in text versus 12–15M in a table) and cites sources dated after its own publication date.
    - Sources: [Tech-Insider](https://tech-insider.org/google-tpu-8t-8i-broadcom-mediatek-nvidia-2026/); [TNW](https://thenextweb.com/news/anthropic-google-broadcom-compute-deal)
18. **Debt figures.**
    - Alphabet's 10-Q: $85.2B of net debt proceeds in 9M 2026. sec-api.io: "$80.8bn of notes". The likely cause is a different scope (other debt or commercial paper), which is not resolved.
    - Sources: [Q3 10-Q](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000084/goog-20260930.htm); [sec-api.io](https://sec-api.io/insights/alphabet-googl-q3-2026-earnings-sec-filing-analysis)
19. **2027 capex.**
    - Alphabet gives no number ("increase significantly"). CNBC's text says capex is expected to exceed $300B in 2027 without a clear attribution.
    - Source: [CNBC](https://www.cnbc.com/2026/10/28/alphabet-googl-earnings-q3-2026.html)
20. **Backlog growth.**
    - Pichai's "nearly doubling quarter on quarter" (Q1 2026) includes a definition change adding about $7.3B of short-term contracts.
    - Source: [Q1 2026 10-Q](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000048/goog-20260331.htm)
21. **MediaTek and TSMC.** No first-party statements by MediaTek or TSMC were found, so their side could not be cross-examined.

### Inferences
- [INF] None of the verified contradictions undermine the existence or scale of the TPU business. They bear on timing claims, unsourced supply-chain attributions, and the strength of cost-advantage claims.

### Gaps
- Nvidia's 2026 public statements about TPUs (for example at GTC 2026 or on earnings calls) were not retrieved.
- Anthropic's and Meta's own technical statements about TPU efficiency in 2026, beyond the S-1 language, were not retrieved.

---

## 10. Verification of the four unverified leads from memory

### Takeaway
- **Lead 1 (TPU v8 variants and design partners):** partly confirmed, partly contradicted.
- **Lead 2 (Nov 2025 Meta report):** confirmed as a report; the later status is reported but unconfirmed.
- **Lead 3 (Google backstops for Fluidstack/TeraWulf and Cipher):** confirmed, with later amounts.
- **Lead 4 (2026 expansion of the Anthropic deal):** confirmed, and larger than the lead implied.

### Cited Findings
- **Lead 1: "TPU v8 variants (training with Broadcom, inference with MediaTek), and whether Google has announced them."**
  - Google announced the split into TPU 8t (training) and TPU 8i (inference) on 22 Apr 2026 [CS], and added 8tx and 8i Max on 9 Nov 2026 [CS]. Google named no design partners. — [Google 22 Apr 2026](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/); [Google 9 Nov 2026](https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/tpu-8i-max-and-8tx/)
  - Partner mapping is contradicted. Broadcom's CEO said Broadcom is shipping "TPU v8i" (inference) and referred to "the MediaTek v8t" (2 Sep 2026). [CS-Broadcom] — [Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-broadcom-tops-q3-2026-estimates-as-ai-sales-surge-93CH-4886849); [Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/)
  - The lead's mapping (Broadcom = 8t "Sunfish"; MediaTek = 8i "Zebrafish") appears only in an unsourced Tech-Insider piece. — [Tech-Insider](https://tech-insider.org/google-tpu-8t-8i-broadcom-mediatek-nvidia-2026/)
- **Lead 2: "A Nov 2025 report (The Information) that Meta discussed using TPUs in its own data centers from 2027 and renting them from 2026."**
  - Confirmed as a report. CNBC (25 Nov 2025) relays The Information's report that Meta could use TPUs in its data centers. Tom's Hardware's headline states renting Google Cloud TPUs "next year" and "outright purchases in 2027". [PR-U] — [CNBC](https://www.cnbc.com/2025/11/25/nvidia-says-its-gpus-are-a-generation-ahead-of-googles-ai-chips.html); [Tom's Hardware](https://www.tomshardware.com/tech-industry/billion-dollar-ai-chip-deal-between-google-and-meta-could-be-on-the-cards-would-involve-renting-google-cloud-tpus-next-year-outright-purchases-in-2027)
  - Later status: a rental deal reported signed on 26 Feb 2026, and purchase talks from 2027. Neither is confirmed by Meta or Google. [PR-U] — [WinBuzzer](https://winbuzzer.com/2026/03/03/meta-signs-multibillion-dollar-deal-rent-google-tpus-xcxwbn/)
- **Lead 3: "Google financial backstops in the Fluidstack/TeraWulf and Cipher Mining deals."**
  - Confirmed: TeraWulf $3.2B backstop for about 14% pro forma equity; Abernathy joint venture about $1.3B; Cipher $1.73B for about 5.4%; Hut 8 River Bend backstop. [PR] — [Sacra](https://sacra.com/c/fluidstack); [Forbes Australia](https://www.forbes.com.au/news/innovation/fluidstack-is-now-worth-18-billion/)
  - Alphabet's aggregate data-center credit-derivative backstops: $16.9B (31 Dec 2025), $28.4B (31 Mar 2026), plus about $15.3B (Apr 2026). [SEC] — [Q1 2026 10-Q](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000048/goog-20260331.htm)
- **Lead 4: "Any 2026 expansion of the Anthropic TPU deal."**
  - Confirmed:
    - 6 Apr 2026: multiple gigawatts, with about 3.5 GW via Broadcom from 2027, conditional.
    - 2 Sep 2026: 5 GW of v8i expected in 2027, and "line of sight" to 10 GW in 2028.
    - 26 Oct 2026 S-1: a $114.5B minimum TPU commitment (Apr 2026–Jul 2033) and $161.2B of Broadcom lease rent.
  - Sources: [Anthropic](https://www.anthropic.com/news/google-broadcom-partnership-compute) [CS-Anthropic]; [Broadcom 8-K](https://www.stocktitan.net/sec-filings/AVGO/8-k-broadcom-inc-reports-material-event-35aab0650b17.html) [SEC]; [Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-broadcom-tops-q3-2026-estimates-as-ai-sales-surge-93CH-4886849) [CS-Broadcom]; [Equibles](https://equibles.com/research/anthropics-s-1-checked-against-amazon-google-microsoft-and-broadcom-filings) [SEC as relayed]

### Inferences
- [INF] Lead 1 should be restated as follows. The training/inference split is official. The partner mapping, according to Broadcom, is the reverse of the lead: Broadcom makes v8i and MediaTek makes v8t. Neither Google nor MediaTek has confirmed it.

### Gaps
- The original Aug–Sep 2025 backstop amounts ($1.8B TeraWulf; $1.4B Cipher) were not re-verified.
- No MediaTek confirmation of its TPU role was found.

---

## 11. (a) Contradictions found (summary list)

### Takeaway
Twelve material contradictions or tensions are recorded below. Each has sources on both sides in sections 1–10.

### Cited Findings
1. **Ironwood GA.** "Coming weeks" (6 Nov 2025) versus actual GA on 31 Mar 2026. [Cloud blog](https://cloud.google.com/blog/products/compute/ironwood-tpus-and-new-axion-based-vms-for-your-ai-workloads); [release notes](https://docs.cloud.google.com/tpu/docs/release-notes)
2. **TPU 8 partner mapping.** Broadcom = v8i and MediaTek = v8t (Broadcom CEO) versus Broadcom = 8t and MediaTek = 8i (Tech-Insider; the brief's lead). [Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-broadcom-tops-q3-2026-estimates-as-ai-sales-surge-93CH-4886849); [Tech-Insider](https://tech-insider.org/google-tpu-8t-8i-broadcom-mediatek-nvidia-2026/)
3. **TPU 8 node.** TSMC N3 versus 2nm. [Crypto Briefing](https://cryptobriefing.com/google-tpu-8t-8i-training-inference-chips/); [Tech-Insider](https://tech-insider.org/google-tpu-8t-8i-broadcom-mediatek-nvidia-2026/)
4. **TPU 8 GA.** "Later this year" (Apr 2026) versus no GA evidence by 14 Nov 2026. [Google](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/)
5. **Anthropic 2026 capacity.** "Well over a gigawatt" versus "1 gigawatt" versus "nearly a gigawatt". [Anthropic](https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services); [Broadcom](https://www.investing.com/news/transcripts/earnings-call-transcript-broadcom-tops-q3-2026-estimates-as-ai-sales-surge-93CH-4886849); [CNBC/Mizuho](https://www.cnbc.com/2026/10/28/google-alters-cloud-playbook-turning-to-partners-to-sell-more-ai-chips.html)
6. **TPU cost advantage versus revealed preferences.** Nvidia is the larger share of Anthropic's contracted GW, and lenders favour Nvidia residual values. [Wccftech](https://wccftech.com/nvidia-gpus-make-up-4-7-gw-of-anthropics-contracted-compute-topping-4-5-gw-of-cheaper-google-tpus-as-lenders-bet-on-nvidias-residual-value/)
7. **Deal labels.** Alphabet "hardware sales" versus Anthropic "leases via Broadcom"; Broadcom "sale" versus Anthropic "finance lease"; "private company" versus "Google"; Google facility of $20.0B versus $30.0B. [Equibles](https://equibles.com/research/anthropics-s-1-checked-against-amazon-google-microsoft-and-broadcom-filings)
8. **OpenAI.** 2025 "no specific plans to use TPUs at present" versus the Oct 2026 purchase report and TPU job posting. [Seoul Economic Daily](https://en.sedaily.com/international/2026/10/28/openai-weighs-buying-google-tpus-easing-nvidia-reliance)
9. **Nvidia's "generation ahead" claim** versus Google's demand statements and the SemiAnalysis TCO estimate. [CNBC](https://www.cnbc.com/2025/11/25/nvidia-says-its-gpus-are-a-generation-ahead-of-googles-ai-chips.html); [SemiAnalysis](https://newsletter.semianalysis.com/p/tpuv7-google-takes-a-swing-at-the)
10. **TPU sale economics.** Kurian's payback claims versus TD Cowen's estimate of about 20% TPU-sale margin and the 10-Q's note of an offsetting cost. [CNBC](https://www.cnbc.com/2026/10/28/google-alters-cloud-playbook-turning-to-partners-to-sell-more-ai-chips.html); [Q3 10-Q](https://www.sec.gov/Archives/edgar/data/0001652044/000165204426000084/goog-20260930.htm)
11. **Artificial Analysis versus SemiAnalysis** on TPU v6e performance per dollar. [SemiAnalysis](https://newsletter.semianalysis.com/p/tpuv7-google-takes-a-swing-at-the)
12. **El Capitan comparison basis** (Ironwood peak versus El Capitan HPL), and **Tech-Insider's shipment numbers falsely attributed to TNW**. [Google](https://blog.google/products/google-cloud/ironwood-tpu-age-of-inference/); [TOP500](https://top500.org/lists/top500/2024/11/); [TNW](https://thenextweb.com/news/anthropic-google-broadcom-compute-deal)

Minor discrepancies:
- 9M 2026 debt: $85.2B of proceeds versus $80.8B of notes.
- 2027 capex: CNBC's "exceeding $300B" is unattributed, while the company says only "significantly".
- Anthropic S-1 timing: Equibles gives the public S-1 filing date as 26 Oct 2026 (accession 0001628280-26-067168). One search-summarized outlet says the "IPO prospectus" revealed the $42B Broadcom convertible note "in early October". [SS] Possible explanations, such as an earlier confidential draft, are unverified. [Equibles](https://equibles.com/research/anthropics-s-1-checked-against-amazon-google-microsoft-and-broadcom-filings)

### Inferences
- [INF] Several of these contradictions trace back to low-reliability secondary sites, notably Tech-Insider. Those sites should not be used for supply-chain facts unless primary confirmation exists.

### Gaps
- None beyond those listed in section 12.

---

## 12. (b) What I could not find or verify

### Takeaway
The main gaps are TPU-specific legal and regulatory items (Singular, DOJ remedies, export controls), MLPerf scores and post-2023 TPU papers, supplier-side statements from MediaTek and TSMC, HBM vendors and nodes, and credible unit-shipment estimates. Much of this follows from the exhausted search budget and from sites that blocked access.

### Cited Findings
- No new findings in this section; it lists what remains unverified.

### Inferences
- [INF] For a final report, the items below should be shown as unverified, not omitted.

### Gaps
- **Status of the newest products.**
  - Not confirmed: GA of TPU 8t and 8i as of 14 Nov 2026.
  - Not found: GA dates for TPU 8tx and 8i Max; FP8 and bf16 specs for TPU 8; whether Google presented at Hot Chips 2026.
- **Original announcement and availability dates and claims** for v4 Cloud availability, v5e (Aug 2023), v5p (Dec 2023; 8,960-chip pod) and Trillium (May 2024 announcement; 4.7x and 67% claims; 256-chip pod).
- **Financials.**
  - Exact Q1 2025 and Q1 2026 Cloud operating income; Cloud backlog at 30 Sep 2025 ($155B from memory) and 31 Dec 2025 (about $240B implied).
  - Credit-backstop notionals at 30 Jun and 30 Sep 2026; Crux AI backstop terms (the "up to $10.0B" figure comes from a search summary only).
  - Amounts and dates of the 2025 bond issues, and of the later 2026 euro, Canadian-dollar and yen notes.
- **Analyst unit estimates.** No credible TPU shipment or unit estimates were found (for example Morgan Stanley's), with source and date. The Tech-Insider figures are unsupported.
- **Customers.**
  - Meta's Aug 2025 Google Cloud deal (more than $10B over six years) was not verified.
  - SSI, Midjourney and Salesforce TPU usage were not verified.
  - Whether the Meta TPU rental deal or OpenAI's purchase is confirmed by either party: no confirmation found.
  - Whether Anthropic's IPO priced: not checked.
- **Neoclouds.** The original 2025 backstop sizes ($1.8B TeraWulf; $1.4B Cipher) were not verified. Delivery status of the Cipher (Sep 2026) and Hut 8 (Q2 2027) sites was not checked.
- **Capacity.** Ironwood's foundry node; HBM suppliers; CoWoS allocations; MediaTek and TSMC statements; total TPU gigawatts deployed by Google.
- **People.** Exact date of Vahdat's promotion; Norm Jouppi's current role; verified 2025–2026 departures from the TPU team.
- **Legal and regulatory.**
  - Singular Computing v. Google: settlement in Jan 2024 recalled but not verified.
  - Ding sentencing status after Jun 2026.
  - DOJ search-case remedies insofar as they touch AI investments or TPUs.
  - Any 2026 antitrust, EU or UK matters on AI partnerships or TPU bundling.
  - US export-control rules applying to TPU hardware or cloud access.
  - Legal-proceedings sections of the 2026 10-Qs.
- **Science.**
  - MLPerf scores, and whether Ironwood or TPU 8 was submitted in any division.
  - TPU papers from 2024–2026 (ISCA, NSDI, Hot Chips).
  - Independent AlphaChip critiques (CACM blocked).
  - Academic TRC evaluations.
  - InferenceX and AgentX benchmark results.
  - Reticle-limit data for TPU dies.
- **Nvidia.** Any 2026 statements on TPUs after Nov 2025.
