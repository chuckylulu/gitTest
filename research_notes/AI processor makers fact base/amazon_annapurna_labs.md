# Amazon / Annapurna Labs AI chips (Inferentia, Trainium): fact base as of 14 November 2026

As of 14 Nov 2026. AWS re:Invent 2026 is scheduled for early December 2026 and has not happened yet. I did not verify its exact dates. Anything announced there is outside this note.

Provenance tags used on every item:
- [CS] Company-stated (Amazon/AWS executives, releases, product pages, blog posts).
- [CS-SEC] Company-stated in an SEC filing.
- [CS-3PT] Company-stated words taken from a third-party transcript. Transcription errors are possible.
- [CUST] / [SUPP] Stated by a customer or partner / by a supplier. Amazon holds equity stakes in Anthropic and OpenAI, so their statements are not independent of Amazon.
- [IV: who] Independently verified, with the verifier named.
- [EST: who] Analyst or industry estimate.
- [PRESS-U] Press report citing unnamed sources or leaked documents.
- [PRESS] Press or analyst characterization without unnamed sourcing.
- [COMP] Assertion by a competitor or another interested party.

Method limits: the shared WebSearch budget ran out partway through. After that, verification relied only on fetching pages already found. Items I could not confirm are in the last section. Quotes were extracted by a fetch tool, which may shorten long sentences; quotes from third-party transcripts are marked [CS-3PT].

---

## Q0. Verification of the four leads supplied from memory

### Takeaway
Leads 1–3 are confirmed by primary sources, with date nuances: the "Q4 2025" call took place on 5 Feb 2026. Lead 4 is confirmed only through secondary coverage that cites Business Insider. I could not retrieve the original BI article.

### Cited Findings
- **Lead 1 (Q3/Q4 2025 calls: multibillion-dollar run rate, Trainium2 fully subscribed): CONFIRMED.**
  - Q3 2025 call, 30 Oct 2025. Jassy on Trainium2: "is now a multibillion-dollar business that grew 150% quarter-over-quarter." [CS-3PT] — [Motley Fool, "Amazon (AMZN) Q3 2025 Earnings Call Transcript", 31 Oct 2025](https://www.fool.com/earnings/call-transcripts/2025/10/31/amazon-amzn-q3-2025-earnings-call-transcript/)
  - Q3 2025 press release, 30 Oct 2025, as quoted in a search excerpt (I did not fetch the page): "Saw continued strong adoption of Trainium2, its custom AI chip, which is fully subscribed and a multi-billion-dollar business that grew 150% quarter over quarter." [CS] — [Business Wire, Amazon Q3 2025 results, 30 Oct 2025](https://www.businesswire.com/news/home/20251029099339/en)
  - Q4 2025 call, held 5 Feb 2026. Jassy: "Trainium is a multibillion-dollar annualized run rate business at this point and it's fully subscribed." [CS-3PT; the transcript is garbled elsewhere, e.g. "Tranium"] — [TickerTrends, AMZN Q4 2025 earnings call transcript, call of 5 Feb 2026](https://tickertrends.io/transcripts/AMZN/Q4-earnings-transcript-2025)
  - Q4 2025 release, 5 Feb 2026: "Trainium2 is fully subscribed with 1.4 million chips landed." [CS] — [Amazon 8-K Ex. 99.1, Q4 2025 results, 5 Feb 2026](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000002/amzn-20251231xex991.htm)
- **Lead 2 (Dec 2025 reorganization under Peter DeSantis): CONFIRMED.**
  - Jassy memo of 17 Dec 2025. DeSantis leads a new organization that combines the AGI team and Nova models, silicon (Graviton, Trainium, Nitro) and quantum computing. Jassy wrote: "Peter will report directly to me." Rohit Prasad leaves Amazon at the end of 2025. Pieter Abbeel leads base-model research within AGI. [CS via press] — [PYMNTS, "Amazon Reorganization Combines AI, Silicon and Quantum Computing", 17 Dec 2025](https://www.pymnts.com/amazon/2025/amazon-reorganization-combines-ai-silicon-and-quantum-computing/); [The Star (Reuters), "Amazon shakes up AI team as veteran Prasad leaves, DeSantis promoted", 18 Dec 2025](https://www.thestar.com.my/tech/tech-news/2025/12/18/amazon-shakes-up-ai-team-as-veteran-prasad-leaves-desantis-promoted)
  - Title as of 31 Jul 2026: "SVP, Amazon AI Models, Chips, & Quantum Computing." [CS] — [About Amazon, "How Amazon's AI chip business reached a $25B revenue run rate", 31 Jul 2026](https://www.aboutamazon.com/news/aws/amazon-ai-chips-business-history)
- **Lead 3 (early-2026 Amazon investment in OpenAI tied to Trainium): CONFIRMED.** Announced 27 Feb 2026.
  - Amazon invests $50B: $15B upfront, then $35B "in the coming months when certain conditions are met." OpenAI will consume about 2 GW of Trainium capacity across Trainium3 and Trainium4. [CS] — [Amazon press release, "OpenAI and Amazon Announce Strategic Partnership", 27 Feb 2026](https://press.aboutamazon.com/2026/2/openai-and-amazon-announce-strategic-partnership)
  - Funding followed the SEC filing: $15.0B in Q1 2026, $13.7B in Q2 and the remaining $21.3B in Q3 2026. [CS-SEC] — [Amazon Form 10-Q for Q3 2026, filed 30 Oct 2026](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm)
- **Lead 4 (2025 Business Insider report on an internal document about startup complaints): PARTLY CONFIRMED, via secondary sources only.**
  - An X post dated 8 Nov 2025 (date decoded from the post ID) cites BI: "AI startup Cohere found that $AMZN Trainium 1 and Trainium 2 chips were underperforming $NVDA H100 GPUs According to an internal confidential Amazon document from July obtained by Business Insider. Cohere reported that access to Trainium 2 was extremely limited and affected by…" [PRESS-U, secondary relay] — [X post by @HyperTechInvest, 8 Nov 2025](https://x.com/HyperTechInvest/status/1987131006315270522)
  - Search excerpts of secondary coverage add the following. Stability AI found Trainium2 "less competitive" on latency and cost. An Amazon spokesperson called the Cohere case "not current," cited good results at Ricoh and Datadog, and said Amazon expects to serve more customers starting with Trainium3. Startup Typhoon found NVIDIA A100s up to 3x more cost-efficient than Inferentia2 for certain workloads. [PRESS-U] — [Financial World, "Startups say Amazon's Trainium chips trail Nvidia in real workloads" (page did not render when fetched; content from search excerpt)](https://www.financial-world.org/news/news/financial/29473/startups-say-amazons-trainium-chips-trail-nvidia-in-real-workloads/); [Substack, "Amazon Trainium: The Strategic Silicon Moat…"](https://iamfabian.substack.com/p/amazon-trainium-the-strategic-silicon)
  - Earlier BI reporting, as cited by Semafor on 14 Mar 2025: among AWS's largest customers in 2024, Trainium adoption was "just 0.5% of Nvidia's GPUs" and Inferentia was 2.7%. [PRESS-U] — [Semafor, "The tiny chips behind Amazon's big AI investment", 14 Mar 2025](https://www.semafor.com/article/03/14/2025/amazons-trainium-chips-to-be-tested-by-anthropic)

### Inferences
- The wording changed between the two calls. On 30 Oct 2025 the "multibillion-dollar business" referred to Trainium2. On 5 Feb 2026 it referred to "Trainium" and was framed as an "annualized run rate." Neither call gave a precise figure.

### Gaps
- I could not retrieve the original BI article (headline, URL, exact date, full text, and Cohere and Stability AI responses). Its early-Nov 2025 date is inferred from the X post's timestamp.

---

## Q1. Products and stage: Inferentia1/2, Trainium1–4, Neuron/NKI, Project Rainier; Trainium3 ramp and Trainium4 dates as of Nov 2026

### Takeaway
As of 14 Nov 2026:
- Trainium2 is deployed at scale: 1.4M chips "landed" by Feb 2026, and the chip is "largely sold out."
- Trainium3 was declared generally available on 2 Dec 2025 but only began shipping in early 2026. Volume is ramping through 2026.
- Trainium4 is in development, with deliveries guided to 2027. It will use NVLink Fusion, and NVIDIA NVHBM was added in Aug 2026.
- Inferentia2 has no announced successor.
- Amazon says it intends to sell Trainium chips outside AWS from late 2027.

### Cited Findings
**Inferentia (inference ASICs)**
- **Inferentia1 (Inf1 instances):**
  - 4 NeuronCores per chip, up to 16 chips per instance, 8 GB DDR4.
  - AWS claim: "up to 2.3x higher throughput and up to 70% lower cost per inference than comparable Amazon EC2 instances."
  - [CS] — [AWS Inferentia product page, accessed 14 Nov 2026](https://aws.amazon.com/ai/machine-learning/inferentia/)
- **Inferentia2 (Inf2 instances):**
  - 32 GB HBM per chip, up to 190 TFLOPS FP16, up to 12 chips per instance.
  - Versus Inferentia1: "up to 4x higher throughput and up to 10x lower latency."
  - "up to 50% better performance/watt over comparable Amazon EC2 instances."
  - The page mentions no Inferentia3 or other successor.
  - [CS] — [AWS Inferentia product page, accessed 14 Nov 2026](https://aws.amazon.com/ai/machine-learning/inferentia/)

**Trainium1 (Trn1)**
- The Nov 2023 release lists Trainium customers Helixon, Money Forward and Amazon Search. Databricks' Naveen Rao said: "AWS Trainium gives us the scale and high performance needed to train our Mosaic MPT models, and at a low cost." [CS/CUST] — [Amazon press release, "AWS Unveils Next Generation AWS-Designed Chips", 28 Nov 2023](https://press.aboutamazon.com/2023/11/aws-unveils-next-generation-aws-designed-chips)
- SemiAnalysis judged Trainium1 and Inferentia2 weak for generative-AI training and inference. [EST: SemiAnalysis] — [SemiAnalysis, "Amazon's AI Self Sufficiency | Trainium2 Architecture & Networking", 3 Dec 2024](https://newsletter.semianalysis.com/p/amazons-ai-self-sufficiency-trainium2-architecture-networking)

**Trainium2 (Trn2 instances and Trn2 UltraServers)**
- **Announced 28 Nov 2023** [CS] — [Amazon press release, 28 Nov 2023](https://press.aboutamazon.com/2023/11/aws-unveils-next-generation-aws-designed-chips)
  - Versus Trainium1: "up to 4x faster training," 3x the memory and up to 2x the performance per watt.
  - Trn2 instances carry 16 chips. UltraClusters scale to 100,000 chips and "up to 65 exaflops."
  - Availability was given only as "will be available," with no date.
- **Generally available 3 Dec 2024:** "Amazon announced on December 3, 2024, that Trainium2 was generally available to rent." [CS via PRESS] — [CNBC, "Apple says it uses Amazon's custom AI chips…", 3 Dec 2024](https://www.cnbc.com/2024/12/03/apple-says-it-uses-amazons-custom-ai-chips-.html)
- **Specs as reported by SemiAnalysis, Dec 2024** [EST: SemiAnalysis] — [SemiAnalysis, 3 Dec 2024](https://newsletter.semianalysis.com/p/amazons-ai-self-sufficiency-trainium2-architecture-networking)
  - Chip: about 500 W, 667 TFLOP/s dense BF16, 96 GB HBM3e in 4 stacks, 2.9 TB/s (firmware-limited to HBM3 speeds).
  - Trn2 server: 16 chips in a 4x4 2D torus.
  - Trn2 UltraServer: 64 chips in a 4x4x4 3D torus across two racks.
  - NeuronLink v3: 640 GB/s per chip.
- **Process node: 5 nm.** [PRESS] — [Semafor, 14 Mar 2025](https://www.semafor.com/article/03/14/2025/amazons-trainium-chips-to-be-tested-by-anthropic); [SemiAnalysis Trainium3 deep dive, 4 Dec 2025](https://newsletter.semianalysis.com/p/aws-trainium3-deep-dive-a-potential)
- **Deployment, 5 Feb 2026:** "We've landed over 1.4 million Tranium two chips our fastest ramping chip launch ever." [CS-3PT] — [TickerTrends Q4 2025 transcript](https://tickertrends.io/transcripts/AMZN/Q4-earnings-transcript-2025)
- **Supply status, 29 Apr 2026:** "Our Trainium2 chip has about 30% better price performance than comparable GPUs and is largely sold out." [CS-3PT] — [TickerTrends, AMZN Q1 2026 transcript, call of 29 Apr 2026](https://tickertrends.io/transcripts/AMZN/Q1-earnings-transcript-2026)

**Trainium3 (3 nm; Trn3 UltraServers)**
- **"General availability" announced 2 Dec 2025 at re:Invent 2025** [CS] — [Amazon/Business Wire, "Trainium3 UltraServers Now Available…", 2 Dec 2025](https://press.aboutamazon.com/2025/12/trainium3-ultraservers-now-available-enabling-customers-to-train-and-deploy-ai-models-faster-at-lower-cost)
  - Described as "AWS's first 3nm AI chip."
  - "Trn3 UltraServers scale up to 144 Trainium3 chips, delivering up to 362 FP8 PFLOPs with 4x lower latency."
  - Versus Trn2 UltraServers: "up to 4.4x more compute performance, 4x greater energy efficiency, and almost 4x more memory bandwidth."
  - "Amazon Bedrock is already serving production workloads on Trainium3."
- **AWS product page specs** [CS] — [AWS Trainium product page, accessed 14 Nov 2026](https://aws.amazon.com/ai/machine-learning/trainium/)
  - Memory: "144 GB HBM3e per chip, 4.9 TB/s bandwidth - 1.7x higher than Trainium2."
  - Compute: "Up to 2x MXFP8 compute throughput compared to Trainium2."
  - Hardware W4A8 quantization.
  - UltraServer: "up to 362 MXFP8 PFLOPs, 20.7 TB of HBM3e, and 706 TB/s"; scale-out EFA "Up to 28.8 Tbps of aggregate scale-out bandwidth per UltraServer."
  - UltraClusters 3.0 scale to "hundreds of thousands of chips."
- **TechCrunch's report of AWS claims, 2 Dec 2025** [PRESS of CS] — [TechCrunch, "Amazon releases an impressive new AI chip and teases an Nvidia-friendly roadmap", 2 Dec 2025](https://techcrunch.com/2025/12/02/amazon-releases-an-impressive-new-ai-chip-and-teases-a-nvidia-friendly-roadmap/)
  - Clusters of "up to 1 million Trainium3 chips."
  - Chips and systems "40% more energy efficient than the previous generation."
  - The author presents no independent verification.
- **SemiAnalysis architecture detail, 4 Dec 2025** [EST: SemiAnalysis] — [SemiAnalysis, "AWS Trainium3 Deep Dive | A Potential Challenger Approaching", 4 Dec 2025](https://newsletter.semianalysis.com/p/aws-trainium3-deep-dive-a-potential)
  - Process: TSMC N3P.
  - Compute: 8 NeuronCores. MXFP8 throughput doubles versus Trn2, and MXFP4 runs at the same rate as MXFP8. BF16/FP16/FP32 are unchanged from Trn2.
  - Memory: 4 stacks of 12-high HBM3E, from SK Hynix and Micron (Trn2 used Samsung).
  - Rack SKUs: "NL32x2 Switched" (air-cooled, 64 chips) and "NL72x2 Switched" (liquid-cooled, 144 chips, 36 Graviton4 CPUs per 144-chip domain).
- **Bring-up and manufacturing** [PRESS] — [TechCrunch, "An exclusive tour of Amazon's Trainium lab…", 22 Mar 2026](https://techcrunch.com/2026/03/22/an-exclusive-tour-of-amazons-trainium-lab-the-chip-thats-won-over-anthropic-openai-even-apple/)
  - The prototype was air-cooled; the production version is liquid-cooled.
  - TSMC manufactures the chip.
  - During bring-up, a heat-sink dimension mismatch had to be fixed by grinding.
- **Shipping status** [CS-3PT] — [TickerTrends Q1 2026 transcript](https://tickertrends.io/transcripts/AMZN/Q1-earnings-transcript-2026)
  - 29 Apr 2026, Jassy: "Trainium3, which just started shipping at the start of 2026" … "is nearly fully subscribed."
  - Jassy's shareholder letter of 9 Apr 2026 contains the same "just started shipping at the start of 2026" phrasing, as cited by Epoch. [CS via EST] — [Epoch AI, AI chip sales documentation/methodology (accessed 14 Nov 2026)](https://epoch.ai/data/ai-chip-sales-documentation/methodology)
- **Ramp evidence as of Nov 2026:**
  - Amazon has not published a Trainium3 unit count.
  - 29 Oct 2026, Jassy: "We're installing an AI accelerator about every 14 seconds." This covers all accelerators, not Trainium only. [CS-3PT] — [Motley Fool, "Amazon (AMZN) Q3 2026 Earnings Call Transcript", 30 Oct 2026](https://www.fool.com/earnings/call-transcripts/2026/10/30/amazon-amzn-q3-2026-earnings-call-transcript/)
  - Anthropic targets "nearly 1GW total of Trainium2 and Trainium3 capacity" online by end-2026. [CUST] — [Anthropic, "Anthropic and Amazon expand compute collaboration", 20 Apr 2026](https://www.anthropic.com/news/anthropic-amazon-compute)
  - Alchip, 14 Aug 2026: guided to record Q3 revenue and another sequential increase in Q4 from its N3 program for an unnamed North American hyperscaler. [SUPP] — [BigGo Finance, Alchip Q2 2026 call summary, 14 Aug 2026](https://finance.biggo.com/news/TW_3661.TW_2026-08-14)

**Trainium4 (in development; NVLink Fusion)**
- **2 Dec 2025:** "already in development"; will support NVIDIA NVLink Fusion; "No timeline was announced." [PRESS of CS] — [TechCrunch, 2 Dec 2025](https://techcrunch.com/2025/12/02/amazon-releases-an-impressive-new-ai-chip-and-teases-a-nvidia-friendly-roadmap/)
- **5 Feb 2026:**
  - Call: "There's very substantial interest in training four which is coming in 2027." [CS-3PT] — [TickerTrends Q4 2025 transcript](https://tickertrends.io/transcripts/AMZN/Q4-earnings-transcript-2025)
  - Release: "Trainium4 is expected to begin delivering in 2027." [CS] — [Amazon 8-K Ex. 99.1, 5 Feb 2026](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000002/amzn-20251231xex991.htm)
- **27 Feb 2026:** Trainium4 is "expected to begin delivery in 2027." [CS] — [Amazon/OpenAI press release, 27 Feb 2026](https://press.aboutamazon.com/2026/2/openai-and-amazon-announce-strategic-partnership)
- **29 Apr 2026:** "much of Trainium4, which is still about 18 months from broad availability" has already been reserved. [CS-3PT] — [TickerTrends Q1 2026 transcript](https://tickertrends.io/transcripts/AMZN/Q1-earnings-transcript-2026)
- **26–27 Aug 2026 (AWS–NVIDIA):** [CS (joint release) via PRESS] — [StorageReview, "AWS and NVIDIA to Deploy 2 Million More GPUs in 2027-2028, Bringing Vera CPUs and Custom NVHBM to Trainium", 27 Aug 2026](https://www.storagereview.com/news/aws-and-nvidia-to-deploy-2-million-more-gpus-in-2027-2028-bringing-vera-cpus-and-custom-nvhbm-to-trainium); release title per [GlobeNewswire, 26 Aug 2026 (page returned 403 when fetched)](https://www.globenewswire.com/news-release/2026/08/26/3351716/0/en/aws-and-nvidia-to-deliver-2-million-additional-gpus-and-next-generation-infrastructure-for-agentic-and-physical-ai.html)
  - "NVLink Fusion is now being paired with NVIDIA's custom high-bandwidth memory (NVHBM) technology."
  - The goal is to let Annapurna "combine Trainium silicon and NVIDIA GPUs within a shared, scale-up rack architecture."
  - No Trainium4 timing was given.
- **SemiAnalysis, Dec 2025** [EST: SemiAnalysis] — [SemiAnalysis, 4 Dec 2025](https://newsletter.semianalysis.com/p/aws-trainium3-deep-dive-a-potential)
  - Memory: 8 stacks of HBM4, giving 4x Trn3's memory bandwidth and 2x its capacity.
  - Two scale-up tracks: UALink 224G and NVLink 448G (NVLink Fusion).
  - Alchip leads back-end design on both tracks.
- **Status on 14 Nov 2026:** pending. There is no general availability and no public delivery date beyond "2027."

**Neuron SDK, NKI, TorchNeuron**
- **AWS product page** [CS] — [AWS Trainium page, accessed 14 Nov 2026](https://aws.amazon.com/ai/machine-learning/trainium/)
  - PyTorch, vLLM, Hugging Face and Ray "work without modification."
  - Native eager mode, FSDP and TorchTitan are supported.
  - NKI gives instruction-set-level access (NKI.isa, NKI.lang).
  - "The open-source NKI Library offers production-ready optimized kernels."
- **29 Oct 2026:** AWS "Made it even easier to adopt its custom AI accelerator, Trainium, with TorchNeuron," which lets developers "run existing PyTorch code… on Trainium." [CS] — [Amazon 8-K Ex. 99.1, Q3 2026 results, 29 Oct 2026](https://www.sec.gov/Archives/edgar/data/0001018724/000101872426000038/amzn-20260930xex991.htm)
- **SemiAnalysis, Dec 2025** [EST: SemiAnalysis; AWS claims as reported] — [SemiAnalysis, 4 Dec 2025](https://newsletter.semianalysis.com/p/aws-trainium3-deep-dive-a-potential)
  - Open-source plan, phase 1: native PyTorch backend, NKI compiler, kernel and communication libraries.
  - Open-source plan, phase 2: XLA graph compiler and the JAX stack.
  - Bedrock runs on a private vLLM v1 fork. Anthropic uses its own inference engine and custom NKI kernels.
  - Logical NeuronCore setting LNC=8 was not expected until mid-2026.
  - AWS-claimed Day-0 utilization (MFU): 43% BF16 on dense models via torch.compile; about 60% on dense models and more than 40% on DeepSeek-670B-class MoE with hand-written NKI kernels.

**Project Rainier (Anthropic) and the Indiana site**
- **Dec 2024:**
  - "400k Trainium2 chips for Anthropic" in Indiana.
  - Phase 1 is seven 65 MW buildings (455 MW). Phase 2 adds nine more, for 1,040 MW.
  - SemiAnalysis noted that 400k Trainium2 chips have less raw FLOPS than a 100k-GPU GB200 cluster.
  - [EST: SemiAnalysis] — [SemiAnalysis, 3 Dec 2024](https://newsletter.semianalysis.com/p/amazons-ai-self-sufficiency-trainium2-architecture-networking)
- **14 Mar 2025:**
  - Gadi Hutt (Annapurna Labs): Rainier spans multiple buildings linked by "Elastic Fiber," and "The architecture will allow customers like Anthropic to train across the entire cluster."
  - Anthropic "has agreed to use Rainier to train the next version of Claude."
  - [PRESS/CS] — [Semafor, 14 Mar 2025](https://www.semafor.com/article/03/14/2025/amazons-trainium-chips-to-be-tested-by-anthropic)
- **17 Oct 2025:** the AWS CEO said in an interview, as cited by Epoch: "they're already running…about 500,000 [Trainium2] chips in Indiana today." [CS via EST] — [Epoch AI, "Anthropic-Amazon New Carlisle" data-center entry, updated 19 Oct 2026](https://epoch.ai/data/ai-data-centers/directory/anthropic-amazon-new-carlisle)
- **29 Oct 2025 activation:**
  - Nearly 500,000 Trainium2 chips across seven buildings.
  - Site: 1,200 acres in New Carlisle, Indiana. Investment: $11B.
  - "capacity expected to exceed one million Trainium2 chips by the end of 2025."
  - [CS via PRESS] — [Converge Digest, "AWS activates Project Rainier data center campus", 29 Oct 2025](https://convergedigest.com/aws-activates-project-rainier-data-center-campus/)
- **30 Oct 2025:** Jassy described the cluster as "spanning multiple U.S. data centers and containing nearly 500,000 of our Trainium2 chips." [CS-3PT] — [Motley Fool Q3 2025 transcript](https://www.fool.com/earnings/call-transcripts/2025/10/31/amazon-amzn-q3-2025-earnings-call-transcript/)
- **Epoch status as of 19 Oct 2026** [EST: Epoch AI; construction progress IV: Epoch via satellite imagery and air permits] — [Epoch AI, updated 19 Oct 2026](https://epoch.ai/data/ai-data-centers/directory/anthropic-amazon-new-carlisle)
  - Buildings 1–18 operational.
  - IT power 1,037 MW, 818k H100-equivalents, capital cost $39.3B. All three are Epoch estimates.
  - Buildings 19–32 are planned, reaching 1,925 MW by Mar 2028 (Epoch projection).
  - An air permit implies 2.3 GW of total facility power.
  - Epoch estimates the chip type as Trainium2 and assumes Trainium3 for the 2028 build.

**Selling Trainium outside AWS**
- 30 Jul 2026, Jassy: "We do have an increasing number of customers who are interested in us providing the Trainium chips to them" … "I expect there's a real chance we'll do that in the future." [CS-3PT] — [StockAnalysis, AMZN Q2 2026 call transcript, 30 Jul 2026](https://stockanalysis.com/stocks/amzn/transcripts/657334-q2-2026/)
- 29 Oct 2026, Jassy: "We intend to do so late in 2027." … "Selling external chips really is a very different business than your cloud infrastructure business." [CS-3PT] — [Motley Fool Q3 2026 transcript](https://www.fool.com/earnings/call-transcripts/2026/10/30/amazon-amzn-q3-2026-earnings-call-transcript/)

**Context: Graviton, Nitro, Cerebras**
- 5 Feb 2026: "Graviton itself is a multibillion-dollar annualized run rate business growing more than 50% year over year." [CS-3PT] — [TickerTrends Q4 2025](https://tickertrends.io/transcripts/AMZN/Q4-earnings-transcript-2025)
- 30 Jul 2026: Graviton is used by 98% of the top 1,000 EC2 customers. [CS-3PT] — [StockAnalysis Q2 2026](https://stockanalysis.com/stocks/amzn/transcripts/657334-q2-2026/)
- Nitro was included in the "chips business" run rate from Q1 2026 (details under Q3 below). [CS] — [Amazon 8-K Ex. 99.1, Q1 2026, 29 Apr 2026](https://www.sec.gov/Archives/edgar/data/0001018724/000101872426000012/amzn-20260331xex991.htm)
- Mar 2026: TechCrunch reported an AWS–Cerebras partnership to integrate Cerebras' inference chip with Trainium-based servers. [PRESS] — [TechCrunch, 22 Mar 2026](https://techcrunch.com/2026/03/22/an-exclusive-tour-of-amazons-trainium-lab-the-chip-thats-won-over-anthropic-openai-even-apple/)

### Inferences
- Implied Trainium3 per-chip compute is about 2.5 PFLOPS FP8 (362 PFLOPS ÷ 144 chips). Derived, not stated per chip by AWS.
- The UltraServer grew from 64 to 144 chips, a 2.25x increase in chip count. The claimed 4.4x UltraServer compute therefore implies about 2x per chip, which matches AWS's "up to 2x MXFP8" per-chip claim.
- The 4.9 TB/s ÷ 2.9 TB/s ratio of about 1.7x matches AWS's stated memory-bandwidth gain over Trainium2.
- The "GA" label on 2 Dec 2025 came before volume shipments in early-to-mid 2026 (see Q2). Volume in 2026 appears weighted to the second half (estimates under Q3).
- Trainium4's adoption of NVLink Fusion and NVHBM (both NVIDIA technologies) means the 2027 generation will depend partly on NVIDIA IP for scale-up and memory, while keeping a UALink track (per SemiAnalysis).

### Gaps
- I did not retrieve primary sources for the launch dates of Inf1, Inf2 and Trn1. My unverified recollection is Inf1 GA Dec 2019, Trn1 GA Oct 2022 and Inf2 GA Apr 2023; these need checking.
- I did not retrieve the Trn2 UltraServer GA date, or AWS's own Trn2 FP8 figures and UltraServer PFLOPS.
- Trainium3 per-chip TDP and rack power sit behind a SemiAnalysis paywall and were not retrieved.
- AWS's primary wording for the Trainium4 performance multiples (≥3x FP8, ≥6x FP4, 4x memory bandwidth) was seen only in search summaries of secondary outlets.
- I found no confirmation that LNC=8 shipped in mid-2026 as planned.
- I could not identify Project Rainier sites outside Indiana; Amazon says it spans "multiple U.S. data centers."

---

## Q2. Roadmap and milestones: commitments, dates, met / slipped / pending

### Takeaway
Most dated Annapurna commitments were met on Amazon's own terms: Trainium2 GA, Project Rainier activation and Trainium3 "GA." Two qualifications apply:
- Trainium3's "GA" came well ahead of volume.
- The ">1M Trainium2 chips at Rainier by end-2025" target is unconfirmed; later statements count Anthropic's chips across all sites.

Trainium4 (2027), OpenAI's Trainium ramp (2027), external chip sales (late 2027) and Anthropic's roughly 1 GW (end-2026) are pending.

### Cited Findings
| Commitment (date made) | Stated target | Outcome as of 14 Nov 2026 | Sources |
|---|---|---|---|
| Trainium2 announced, 28 Nov 2023 [CS] | "will be available" (no date) | GA 3 Dec 2024. **Met** (no dated target existed to slip against) | [Amazon PR, 28 Nov 2023](https://press.aboutamazon.com/2023/11/aws-unveils-next-generation-aws-designed-chips); [CNBC, 3 Dec 2024](https://www.cnbc.com/2024/12/03/apple-says-it-uses-amazons-custom-ai-chips-.html) |
| Project Rainier: "hundreds of thousands" of Trainium2 (Mar 2025) [PRESS/CS] | Multi-building cluster for Anthropic | Activated 29 Oct 2025 with about 500k Trainium2. **Met** | [Semafor, 14 Mar 2025](https://www.semafor.com/article/03/14/2025/amazons-trainium-chips-to-be-tested-by-anthropic); [Converge Digest, 29 Oct 2025](https://convergedigest.com/aws-activates-project-rainier-data-center-campus/) |
| Rainier ">1M Trainium2 chips by end of 2025" (29 Oct 2025) [CS via PRESS] | 1M by YE2025 | **Unconfirmed for Rainier.** On 5 Feb 2026 Jassy still said "We talked about 500,000 chips there." On 20 Apr 2026 Anthropic said it uses ">1M Trainium2" across its fleet | [Converge Digest](https://convergedigest.com/aws-activates-project-rainier-data-center-campus/); [TickerTrends Q4 2025](https://tickertrends.io/transcripts/AMZN/Q4-earnings-transcript-2025); [Anthropic, 20 Apr 2026](https://www.anthropic.com/news/anthropic-amazon-compute) |
| Trainium3 timing, as stated 30 Oct 2025 [CS-3PT] | "preview at the end of this year with much fuller volumes coming in the beginning of '26" | "GA" announced 2 Dec 2025; "just started shipping at the start of 2026"; supplier N3 mass production for an unnamed North American customer in May 2026. **Met on paper; volume ramp through 2026** | [Motley Fool Q3 2025](https://www.fool.com/earnings/call-transcripts/2025/10/31/amazon-amzn-q3-2025-earnings-call-transcript/); [Amazon PR, 2 Dec 2025](https://press.aboutamazon.com/2025/12/trainium3-ultraservers-now-available-enabling-customers-to-train-and-deploy-ai-models-faster-at-lower-cost); [TickerTrends Q1 2026](https://tickertrends.io/transcripts/AMZN/Q1-earnings-transcript-2026); [TrendForce, 26 May 2026](https://www.trendforce.com/news/2026/05/26/news-alchip-says-key-customers-ai-chip-enters-mass-production-in-may-asics-seen-outpacing-gpu-cagr/) |
| Trainium3 supply "nearly all… committed by mid-2026" (5 Feb 2026) [CS-3PT] | Mid-2026 | "nearly fully subscribed" (29 Apr 2026). **Met (company-stated)** | [TickerTrends Q4 2025](https://tickertrends.io/transcripts/AMZN/Q4-earnings-transcript-2025); [TickerTrends Q1 2026](https://tickertrends.io/transcripts/AMZN/Q1-earnings-transcript-2026) |
| Trainium4 (2 Dec 2025: no timeline) [PRESS of CS] | 5 Feb 2026: "coming in 2027"; 27 Feb 2026: "begin delivery in 2027"; 29 Apr 2026: "about 18 months from broad availability" | **Pending.** No GA; re:Invent 2026 not yet held | [TechCrunch, 2 Dec 2025](https://techcrunch.com/2025/12/02/amazon-releases-an-impressive-new-ai-chip-and-teases-a-nvidia-friendly-roadmap/); [Amazon 8-K, 5 Feb 2026](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000002/amzn-20251231xex991.htm); [Amazon/OpenAI PR, 27 Feb 2026](https://press.aboutamazon.com/2026/2/openai-and-amazon-announce-strategic-partnership); [TickerTrends Q1 2026](https://tickertrends.io/transcripts/AMZN/Q1-earnings-transcript-2026) |
| OpenAI 2 GW of Trainium (27 Feb 2026) [CS] | "begins ramping in 2027" | **Pending** | [Amazon 8-K, Q1 2026](https://www.sec.gov/Archives/edgar/data/0001018724/000101872426000012/amzn-20260331xex991.htm) |
| Anthropic "nearly 1GW" of Trainium2 + Trainium3 by end-2026 (20 Apr 2026) [CUST] | End-2026 | **Pending** (no update found) | [Anthropic, 20 Apr 2026](https://www.anthropic.com/news/anthropic-amazon-compute) |
| External Trainium sales [CS-3PT] | 30 Jul 2026: "real chance"; 29 Oct 2026: "late in 2027" | **Pending** | [StockAnalysis Q2 2026](https://stockanalysis.com/stocks/amzn/transcripts/657334-q2-2026/); [Motley Fool Q3 2026](https://www.fool.com/earnings/call-transcripts/2026/10/30/amazon-amzn-q3-2026-earnings-call-transcript/) |
| AWS power (30 Oct 2025: "on track to double again by 2027"; 30 Jul 2026: "double the power capacity by the end of 2027 that we had in 2025") [CS-3PT] | 2x the 2025 level by end-2027 | **Pending**: 3.8 GW added in the 12 months to Q3 2025; about 3.9 GW in 2025 (transcript reads "3.99"); 1.2 GW in Q4 2025 | [Motley Fool Q3 2025](https://www.fool.com/earnings/call-transcripts/2025/10/31/amazon-amzn-q3-2025-earnings-call-transcript/); [TickerTrends Q4 2025](https://tickertrends.io/transcripts/AMZN/Q4-earnings-transcript-2025); [StockAnalysis Q2 2026](https://stockanalysis.com/stocks/amzn/transcripts/657334-q2-2026/) |
| 2025 cash capex "approximately $125 billion" (30 Oct 2025) [CS-3PT] | ~$125B | Actual purchases of property and equipment $131.8B gross; $128.3B net of proceeds and incentives (TTM). **Exceeded guidance** | [Motley Fool Q3 2025](https://www.fool.com/earnings/call-transcripts/2025/10/31/amazon-amzn-q3-2025-earnings-call-transcript/); [Amazon 8-K, Q4 2025](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000002/amzn-20251231xex991.htm) |
| 2026 capex "about $200 billion" (5 Feb 2026) [CS-3PT] | ~$200B | Raised to "approximately $220 billion" on 30 Jul 2026 ("higher cost of memory"); reaffirmed 29 Oct 2026. **Revised up** | [TickerTrends Q4 2025](https://tickertrends.io/transcripts/AMZN/Q4-earnings-transcript-2025); [StockAnalysis Q2 2026](https://stockanalysis.com/stocks/amzn/transcripts/657334-q2-2026/); [Motley Fool Q3 2026](https://www.fool.com/earnings/call-transcripts/2026/10/30/amazon-amzn-q3-2026-earnings-call-transcript/) |

### Inferences
- Trainium4's guidance tightened over time: "coming in 2027," then "begin delivery in 2027," then "about 18 months from broad availability" as of late Apr 2026. Together these point to first deliveries in 2027 and broad availability around late 2027. Alchip's next-generation N2 chiplet (customer unnamed) targets tape-out by end-2026 and production by end-2027, a consistent window if it is Trainium4. That link is unconfirmed.

### Gaps
- I did not confirm from a fetched primary source that Trainium3 was first announced in Dec 2024 (re:Invent 2024), or the timing originally promised then (my recollection: "late 2025"). The BI-reported Amazon statement (2025) refers to "Trainium 3, previewing later this year."

---

## Q3. Financials: AWS segment, backlog, Trainium-specific management numbers, capex, cash/debt, Annapurna price, analyst volume estimates

### Takeaway
Amazon does not report Trainium revenue. The closest disclosures are:
- A "chips business" run rate: >$10B (Graviton and Trainium, Feb 2026), then >$20B (Graviton, Trainium and Nitro, Apr 2026), then >$25B (Jul 2026). Nitro joined the definition in Q1 2026, so the figures are not like-for-like.
- ">$225B in revenue commitments for Trainium" (Apr 2026).
- Graviton and Trainium revenue commitments "each increased more than 20x" year over year (Oct 2026).

Over the same period, AWS growth accelerated from 17% to 39% and backlog reached $578B. Capex is guided to about $220B for 2026, funded partly by about $115B of new 2026 borrowing.

### Cited Findings
**AWS segment results.** Sources: [Amazon 8-K Ex. 99.1, Q4 2025, 5 Feb 2026](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000002/amzn-20251231xex991.htm) and [Amazon 8-K Ex. 99.1, Q3 2026, 29 Oct 2026](https://www.sec.gov/Archives/edgar/data/0001018724/000101872426000038/amzn-20260930xex991.htm) [CS-SEC]. Backlog is from the earnings-call transcripts cited per row.

| Quarter | AWS net sales ($M) | YoY | AWS operating income ($M) | Op. margin | Backlog (as stated on call) |
|---|---|---|---|---|---|
| Q4 2024 | 28,786 | 19% | 10,632 | 36.9% | n/r |
| Q1 2025 | 29,267 | 17% | 11,547 | 39.5% | n/r |
| Q2 2025 | 30,873 | 17% | 10,160 | 32.9% | n/r |
| Q3 2025 | 33,006 | 20% (20.2%) | 11,434 | 34.6% | $200B, "doesn't include several unannounced new deals in October" ([Motley Fool](https://www.fool.com/earnings/call-transcripts/2025/10/31/amazon-amzn-q3-2025-earnings-call-transcript/)) |
| Q4 2025 | 35,579 | 24% | 12,465 | 35.0% | $244B, "up 40% year over year" ([TickerTrends](https://tickertrends.io/transcripts/AMZN/Q4-earnings-transcript-2025)) |
| Q1 2026 | 37,587 | 28% | 14,161 | 37.7% | $364B, excluding the Anthropic deal of more than $100B ([TickerTrends](https://tickertrends.io/transcripts/AMZN/Q1-earnings-transcript-2026)) |
| Q2 2026 | 42,232 | 37% (36.7%) | 16,621 | 39.4% | $496B, "growing triple digits" ([StockAnalysis](https://stockanalysis.com/stocks/amzn/transcripts/657334-q2-2026/)) |
| Q3 2026 | 45,984 | 39% (39.3%) | 17,773 | 38.7% | $578B, "growing triple digits year-over-year and well-diversified" ([Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/10/30/amazon-amzn-q3-2026-earnings-call-transcript/)) |
| FY2025 | 128,725 | 20% | 45,606 | 35.4% | — |

(n/r = not retrieved.)

**AWS margin and growth commentary**
- Q2 2026, Olsavsky: AWS margin was "up 650 basis points year-over-year," or "520 basis points if you exclude the derivative accounting gain." [CS-3PT] — [StockAnalysis Q2 2026](https://stockanalysis.com/stocks/amzn/transcripts/657334-q2-2026/)
- Q3 2026, Olsavsky: "the outsized growth of AI puts margin pressure on the business as a whole because the margins are lower there," with "headwinds from component pricing." [CS-3PT] — [Motley Fool Q3 2026](https://www.fool.com/earnings/call-transcripts/2026/10/30/amazon-amzn-q3-2026-earnings-call-transcript/)
- The Q4 2026 guidance assumes no "energy derivative remeasurement impacts." [CS] — [Amazon 8-K, Q3 2026](https://www.sec.gov/Archives/edgar/data/0001018724/000101872426000038/amzn-20260930xex991.htm)
- Forward view, 29 Oct 2026, Jassy: "we believe that AWS can grow north of 40% in each of 2027 and in 2028." The release says "projected revenue growth rates of over 40% both in 2027 and in 2028." [CS] — [Motley Fool Q3 2026](https://www.fool.com/earnings/call-transcripts/2026/10/30/amazon-amzn-q3-2026-earnings-call-transcript/); [Amazon 8-K, Q3 2026](https://www.sec.gov/Archives/edgar/data/0001018724/000101872426000038/amzn-20260930xex991.htm)

**Every management statement that puts a number on Trainium or the chips business (chronological)**
- **28 Nov 2023:** Trainium2 offers "up to 4x faster training" than Trainium1; UltraClusters of "up to 100,000" chips. [CS] — [Amazon PR](https://press.aboutamazon.com/2023/11/aws-unveils-next-generation-aws-designed-chips)
- **14 Mar 2025, Rami Sinno (Annapurna):** "Every single chip that we build and deliver has customers waiting for it." [CS] — [Semafor](https://www.semafor.com/article/03/14/2025/amazons-trainium-chips-to-be-tested-by-anthropic)
- **30 Oct 2025 (Q3 2025)** [CS-3PT/CS] — [Motley Fool Q3 2025](https://www.fool.com/earnings/call-transcripts/2025/10/31/amazon-amzn-q3-2025-earnings-call-transcript/)
  - Trainium2 "is now a multibillion-dollar business that grew 150% quarter-over-quarter"; "fully subscribed."
  - "Trainium is 30% to 40% more price performance than other options out there."
  - "the majority of token usage in Amazon Bedrock is already running on Trainium."
  - "Today, Trainium is being used by a small number of very large customers."
  - "I expect Trainium3 will be about 40% better than Trainium2."
  - Rainier: "nearly 500,000 of our Trainium2 chips."
- **2 Dec 2025:** Trn3 UltraServers deliver "up to 4.4x more compute performance, 4x greater energy efficiency" than Trn2 UltraServers; customers are "reducing training and inference costs by up to 50%." [CS] — [Amazon PR](https://press.aboutamazon.com/2025/12/trainium3-ultraservers-now-available-enabling-customers-to-train-and-deploy-ai-models-faster-at-lower-cost)
- **5 Feb 2026 (Q4 2025)** [CS-3PT/CS] — [TickerTrends Q4 2025](https://tickertrends.io/transcripts/AMZN/Q4-earnings-transcript-2025); [Amazon 8-K](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000002/amzn-20251231xex991.htm)
  - "our chips business, inclusive of Graviton and Tranium, is now over $10 billion in annual revenue run rate," growing triple digits.
  - "We've landed over 1.4 million Tranium two chips."
  - "Tranium two is 30 to 40% more price performance than comparable GPUs."
  - "Trainium is a multibillion-dollar annualized run rate business at this point and it's fully subscribed."
  - "nearly all of our Tranium three supply … committed by mid-2026."
- **29 Apr 2026 (Q1 2026)**
  - Call [CS-3PT] — [TickerTrends Q1 2026](https://tickertrends.io/transcripts/AMZN/Q1-earnings-transcript-2026)
    - "over $225 billion in revenue commitments for Trainium."
    - Trainium2 has "about 30% better price performance than comparable GPUs and is largely sold out."
    - Trainium3 is "nearly fully subscribed."
    - "we expect Trainium will save us tens of billions of dollars of CapEx each year."
    - Bedrock, used by over 125,000 customers, "runs most of its inference on Trainium."
  - Release [CS-SEC exhibit] — [Amazon 8-K, Q1 2026](https://www.sec.gov/Archives/edgar/data/0001018724/000101872426000012/amzn-20260331xex991.htm)
    - "Exceeded $20 billion annual revenue run rate for Amazon's chips business."
    - The release says this figure includes Graviton, Trainium and Nitro, growing triple digits.
- **30 Jul 2026 (Q2 2026)**
  - Call [CS-3PT] — [StockAnalysis Q2 2026](https://stockanalysis.com/stocks/amzn/transcripts/657334-q2-2026/)
    - "Our chips business now has an annual revenue run rate of over $25 billion, growing triple-digit percentages year-over-year."
    - "Anthropic and OpenAI, making multi-year, multi-gigawatt commitments to Trainium."
    - "Our AI revenue run rate … is now also over $25 billion."
  - About Amazon follow-up [CS] — [About Amazon, 31 Jul 2026](https://www.aboutamazon.com/news/aws/amazon-ai-chips-business-history)
    - The $25B covers Trainium, Graviton and Nitro.
    - "Trainium3 delivers over five times the output tokens per megawatt of Trainium2."
    - Trainium3 has "up to 40% better price-performance" than Trainium2.
    - Anthropic's Claude runs on more than one million Trainium2 chips.
- **29 Oct 2026 (Q3 2026):** [CS-3PT] — [Motley Fool Q3 2026](https://www.fool.com/earnings/call-transcripts/2026/10/30/amazon-amzn-q3-2026-earnings-call-transcript/)
  - "revenue commitments for Graviton and Trainium have each increased more than 20x year-over-year."
  - "Customers using our custom silicon saved more than $2 billion in Q3 alone."
  - "the majority and most of Bedrock today is being run on top of Trainium."
- **AI revenue context:**
  - 29 Apr 2026: "AWS' AI revenue run rate is over $15 billion." [CS-3PT] — [TickerTrends Q1 2026](https://tickertrends.io/transcripts/AMZN/Q1-earnings-transcript-2026)
  - 5 Feb 2026: "Bedrock is now a multibillion-dollar annualized run rate business." [CS-3PT] — [TickerTrends Q4 2025](https://tickertrends.io/transcripts/AMZN/Q4-earnings-transcript-2025)

**Capex**
- **2025:**
  - Purchases of property and equipment $131,819M gross for FY2025, of which $39,522M in Q4 2025.
  - Net of proceeds and incentives (TTM): $128,320M.
  - [CS-SEC exhibit] — [Amazon 8-K, Q4 2025](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000002/amzn-20251231xex991.htm)
  - Cash capex by quarter: Q3 2025 $34.2B; $89.9B for 9M 2025. [CS-3PT] — [Motley Fool Q3 2025](https://www.fool.com/earnings/call-transcripts/2025/10/31/amazon-amzn-q3-2025-earnings-call-transcript/)
- **2026 cash capex by quarter:**
  - Q1 $43.2B [CS-3PT] — [TickerTrends Q1 2026](https://tickertrends.io/transcripts/AMZN/Q1-earnings-transcript-2026)
  - Q2 $53.1B [CS-3PT] — [StockAnalysis Q2 2026](https://stockanalysis.com/stocks/amzn/transcripts/657334-q2-2026/)
  - Q3 $75.9B, with gross purchases of $77,259M in Q3 2026 [CS-3PT/CS-SEC exhibit] — [Motley Fool Q3 2026](https://www.fool.com/earnings/call-transcripts/2026/10/30/amazon-amzn-q3-2026-earnings-call-transcript/); [Amazon 8-K, Q3 2026](https://www.sec.gov/Archives/edgar/data/0001018724/000101872426000038/amzn-20260930xex991.htm)
  - TTM net capex: $210,657M at Q3 2026, up 82% YoY. [CS-SEC exhibit] — [Amazon 8-K, Q3 2026](https://www.sec.gov/Archives/edgar/data/0001018724/000101872426000038/amzn-20260930xex991.htm)
- **2026 guidance path** [CS-3PT] — [TickerTrends Q4 2025](https://tickertrends.io/transcripts/AMZN/Q4-earnings-transcript-2025); [StockAnalysis Q2 2026](https://stockanalysis.com/stocks/amzn/transcripts/657334-q2-2026/); [Motley Fool Q3 2026](https://www.fool.com/earnings/call-transcripts/2026/10/30/amazon-amzn-q3-2026-earnings-call-transcript/)
  - 5 Feb 2026: "about $200 billion."
  - 30 Jul 2026: "approximately $220 billion," with "The higher cost of memory pushing this number up."
  - 29 Oct 2026: "approximately $220 billion, the majority for AWS"; "We can fund this plan."

**Cash, debt and bond issuance**
- **Balance sheet** [CS-SEC exhibit] — [Amazon 8-K, Q4 2025](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000002/amzn-20251231xex991.htm); [Amazon 8-K, Q3 2026](https://www.sec.gov/Archives/edgar/data/0001018724/000101872426000038/amzn-20260930xex991.htm)

  | Item ($M) | 31 Dec 2024 | 31 Dec 2025 | 30 Sep 2026 |
  |---|---|---|---|
  | Cash and equivalents | 78,779 | 86,810 | 55,783 |
  | Marketable securities | 22,423 | 36,219 | 58,443 |
  | Long-term debt (carrying) | 52,623 | 65,648 | 173,125 |

- **Long-term debt face value:** $68,836M at 31 Dec 2025, rising to $180,887M at 30 Sep 2026. [CS-SEC] — [Amazon 10-Q, Q3 2026](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm)
- **2026 issuance, per the 10-Q** [CS-SEC] — [Amazon 10-Q, Q3 2026](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm)
  - March 2026 Notes: $37.0B, including $2.8B of floating-rate notes.
  - March 2026 Euro Notes: €14.5B ($16.4B).
  - May 2026 Swiss franc Notes: CHF 2.8B ($3.4B).
  - June 2026 Canadian dollar Notes: C$14.0B ($9.8B).
  - July 2026 Notes: $25.0B.
  - September 2026 Sterling Notes: £4.3B ($5.6B).
  - 2026 Term Loan: $17.5B, drawn Sep 2026, maturing Sep 2029.
  - No commercial paper was outstanding at either date.
- **CNBC on the July 2026 sale** [PRESS-U for the "no more debt" point] — [CNBC, "Amazon raising at least $25 billion in bond sale, won't issue more debt in 2026", 7 Jul 2026](https://www.cnbc.com/2026/07/07/amazon-bond-sale-ai-debt.html)
  - Eight-part sale of at least $25B.
  - Earlier in 2026, about $54B raised in the US and Europe, plus $10B in Canada in June.
  - Prior offering: $15B from a US bond sale in November (context indicates Nov 2025).
  - Per people familiar, Amazon told underwriters it "won't issue any more debt this year."
- Bloomberg reported an 11-part US bond offering on 10 Mar 2026 (headline only). [PRESS] — [Bloomberg, "Amazon Launches 11-Part US Bond Sale to Fund AI Infrastructure Investments", 10 Mar 2026](https://www.bloomberg.com/news/articles/2026-03-10/amazon-kicks-off-11-part-us-high-grade-bond-offering)

**Investments tied to Trainium customers (SEC 10-Q, 30 Sep 2026)** [CS-SEC] — [Amazon 10-Q, Q3 2026](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm)
- **Anthropic:**
  - Nonvoting preferred stock carried at about $92.5B, up from about $14.8B at 31 Dec 2025.
  - Convertible notes at fair value of about $146.2B, with $140.3B of unrealized gain in other comprehensive income.
  - Upward price adjustments of $62.8B in the nine months of 2026, of which $39M in Q3.
  - Q2 2026 investments: $5.0B in Series G and $5.0B in Series H.
  - Financing facility of up to $20.0B, reduced to $15.0B after the Series H. Amounts become drawable "as we reach certain delivery milestones of compute capacity under the amended commercial arrangement."
- **Pre-tax gains on the Anthropic stake:** $9.5B in Q3 2025 and $16.8B in Q1 2026. [CS] — [Motley Fool Q3 2025](https://www.fool.com/earnings/call-transcripts/2025/10/31/amazon-amzn-q3-2025-earnings-call-transcript/); [Amazon 8-K, Q1 2026](https://www.sec.gov/Archives/edgar/data/0001018724/000101872426000012/amzn-20260331xex991.htm)
- **OpenAI:** Series C Preferred carried at $50.0B at 30 Sep 2026, fully funded by Q3 2026.

**2015 Annapurna acquisition price (never disclosed by Amazon)**
- Globes (Jan 2015): about $350M, per sources. [PRESS-U] — [Globes, "Amazon acquires Annapurna Labs for $350m", Jan 2015](https://en.globes.co.il/en/article-amazon-acquires-annapurna-labs-for-350m-1001003315)
- Global Venturing, citing Calcalist: up to $370M. [PRESS-U] — [Global Venturing, "ARM exits Annapurna Labs in $370m acquisition", 23 Jan 2015](https://globalventuring.com/blog/2015/01/23/arm-exits-annapurna-labs-in-370m-acquisition/)
- Later outlets repeat "$350 million." [PRESS] — [Semafor, 14 Mar 2025](https://www.semafor.com/article/03/14/2025/amazons-trainium-chips-to-be-tested-by-anthropic); [TechCrunch, 22 Mar 2026](https://techcrunch.com/2026/03/22/an-exclusive-tour-of-amazons-trainium-lab-the-chip-thats-won-over-anthropic-openai-even-apple/)
- The deal closed in January 2015. [PRESS] — [Wikipedia, Annapurna Labs](https://en.wikipedia.org/wiki/Annapurna_Labs)

**Analyst and industry estimates of Trainium volumes (labeled; not company data)**
- **Morgan Stanley (T. Yeh), 8 Jul 2025, relayed on X 10 Jul 2025** [EST: Morgan Stanley via relay] — [X post by @Jukanlosreve, 10 Jul 2025](https://x.com/Jukanlosreve/status/1943316885434663204)
  - About 1.1M Trainium2/2.5 units shipped in 2025.
  - A gap between chip output and system installation, attributed to PCB yield issues.
- **Morgan Stanley, per Epoch:** 500k Trainium2 produced in 1H26 and 1.9M Trainium2 over the product's life. [EST via EST] — [Epoch AI methodology](https://epoch.ai/data/ai-chip-sales-documentation/methodology)
- **JPMorgan, via a Jan 2026 media report cited by Epoch:** 600k Trainium2 and 1.5M Trainium3 shipped in 2026. [EST: JPMorgan] — [Epoch AI methodology](https://epoch.ai/data/ai-chip-sales-documentation/methodology)
- **KGI and Yuanta, per Epoch:** KGI 2.4–2.5M total Trainium; Yuanta 2M. [EST] — [Epoch AI methodology](https://epoch.ai/data/ai-chip-sales-documentation/methodology)
- **Omdia, per Epoch:** 1.3M Trainium plus Inferentia deployed in 2024. [EST: Omdia] — [Epoch AI methodology](https://epoch.ai/data/ai-chip-sales-documentation/methodology)
- **Epoch AI's own model** [EST: Epoch] — [Epoch AI methodology](https://epoch.ai/data/ai-chip-sales-documentation/methodology); [GitHub, epoch-research/ai-chip-counts PR #8](https://github.com/epoch-research/ai-chip-counts/pull/8)
  - Trainium2: about 300k in 2024, ~450k in 1H25 and ~650k in 2H25.
  - 1H26: Trainium2 median 600k (90% CI 400k–900k); Trainium3 median just under 100k (90% CI 30k–300k).
  - Cumulative Trainium output of about 2.6M through Q2 2026.
- **SemiAnalysis, per Epoch:** Trainium2 unit cost about $4k; 2025 Trainium2 production about 4x 2024; Trainium3 wafer-in in early 2026 "for a large H2 ramp." [EST: SemiAnalysis] — [Epoch AI methodology](https://epoch.ai/data/ai-chip-sales-documentation/methodology)
- **Rumor:** an unverified X post (21 Oct 2025) claimed Alchip had at least 1M confirmed Trainium3 units for 2026 at $3,000 each. Unverified; listed only as a data point. — [X post by @The_AI_Investor, 21 Oct 2025](https://x.com/The_AI_Investor/status/1980667197753290835)

### Inferences
- 9M 2026 cash capex is $172.2B ($43.2B + $53.1B + $75.9B). Hitting the about $220B full-year guide implies about $48B in Q4 2026, below Q3's $75.9B. This is arithmetic on company figures; the timing of payments is not explained.
- Disclosed 2026 issuance sums to about $114.7B, which roughly matches the +$112B rise in long-term debt face value between Dec 2025 and Sep 2026.
- Backlog rose $132B from Q1 2026 ($364B) to Q2 2026 ($496B). That is consistent with the Anthropic deal of more than $100B (excluded from Q1 by Amazon's statement) entering backlog in Q2. Amazon did not state this explicitly in the extracted text.
- Trainium-only revenue cannot be isolated from the disclosures. The run rate is reported only with Graviton, and later Nitro; "revenue commitments" are a forward contractual measure, not recognized revenue.

### Gaps
- AWS backlog for Q1 and Q2 2025 was not retrieved.
- I found no Trainium-only revenue figure. Amazon does not disclose one.
- I did not verify a Yahoo-summary claim that capex will rise "meaningfully" in 2027.
- I did not see primary research notes for the analyst estimates; they come via X relays and Epoch.

---

## Q4. Customers and contracts: which are binding and which are only announced

### Takeaway
Two customers dominate Trainium demand: Anthropic and, from 2027, OpenAI. Amazon is an investor in both. The 10-Q confirms their AWS commitments as contractual and states that they include "contractual obligations related to the performance of AWS chips." The gigawatt figures ("up to 5 GW," "approximately 2 GW") appear only in press releases. Most other customers appear only in AWS-curated testimonials. Apple was evaluating Trainium2 in Dec 2024, and I found no later confirmation of use.

### Cited Findings
**Anthropic**
- **Prior investment:** Amazon "previously invested" $8B. [CUST] — [Anthropic, 20 Apr 2026](https://www.anthropic.com/news/anthropic-amazon-compute)
- **20 Apr 2026 expansion** [CUST/CS; PRESS] — [Anthropic, 20 Apr 2026](https://www.anthropic.com/news/anthropic-amazon-compute); [CNBC, 20 Apr 2026](https://www.cnbc.com/2026/04/20/amazon-invest-up-to-25-billion-in-anthropic-part-of-ai-infrastructure.html); [Amazon on X, 20 Apr 2026](https://x.com/amazon/status/2046327632782913952)
  - Amazon invests $5B now at Anthropic's $380B valuation, plus up to $20B tied to "certain commercial milestones."
  - Anthropic commits more than $100B over 10 years to AWS technologies.
  - "up to 5 gigawatts (GW) of capacity," spanning Graviton and Trainium2 through Trainium4, with options on future generations.
  - "Nearly 1GW total of Trainium2 and Trainium3 capacity" online by end-2026.
  - Anthropic "currently uses over one million Trainium2 chips to train and serve Claude."
  - Anthropic continues "to choose AWS as our primary training and cloud provider for mission-critical workloads."
- **Binding status per the 10-Q** [CS-SEC] — [Amazon 10-Q, Q3 2026](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm)
  - The commitment expansion ("more than $100.0 billion over 10.0 years") "includes contractual obligations related to the performance of AWS chips."
  - The equity and the facility are as described under Q3.
- **Earlier statements:**
  - 28 Nov 2023, Tom Brown: "We are working closely with AWS to develop our future foundation models using Trainium chips." [CUST] — [Amazon PR](https://press.aboutamazon.com/2023/11/aws-unveils-next-generation-aws-designed-chips)
  - James Bradbury, Anthropic Head of Compute (undated customer page, accessed 14 Nov 2026): "With almost a million Trainium2 chips training and serving Claude today, we're excited about Trainium3." [CUST] — [AWS Trainium customers page](https://aws.amazon.com/machine-learning/trainium/customers/)
- **Parallel deals**
  - Google, 23 Oct 2025: up to one million TPUs, "tens of billions of dollars," "well over a gigawatt" online in 2026. Anthropic described "three chip platforms" (TPU, Trainium, NVIDIA GPU) and said it remains committed to Amazon as "primary training partner and cloud provider." [CUST] — [Anthropic, "Expanding our use of Google Cloud TPUs and Services", 23 Oct 2025](https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services)
  - Microsoft and NVIDIA, 18 Nov 2025: Anthropic commits to "purchase $30 billion of Azure compute capacity" and "up to one gigawatt" on NVIDIA Grace Blackwell and Vera Rubin systems. NVIDIA invests up to $10B and Microsoft up to $5B. "Amazon remains Anthropic's primary cloud provider and training partner." [CUST] — [Anthropic, "Microsoft, NVIDIA and Anthropic announce strategic partnerships", 18 Nov 2025](https://www.anthropic.com/news/microsoft-nvidia-anthropic-announce-strategic-partnerships)
  - Google and Broadcom, Apr 2026: expanded partnerships for "multiple gigawatts" of capacity (no dollar figure). [PRESS] — [CNBC, 20 Apr 2026](https://www.cnbc.com/2026/04/20/amazon-invest-up-to-25-billion-in-anthropic-part-of-ai-infrastructure.html)
- **The Information, via The Decoder, 8 Nov 2024:** Amazon conditioned its second Anthropic investment on Anthropic using "servers with Amazon's own Trainium chips more extensively." [PRESS-U] — [The Decoder, "Amazon wants Anthropic to switch from Nvidia to Amazon chips", 8 Nov 2024](https://the-decoder.com/amazon-wants-anthropic-to-switch-from-nvidia-to-amazon-chips/)
- **Semafor, 14 Mar 2025:** two unnamed people said Anthropic's chip agreement is separate from Amazon's investment decision. [PRESS-U] — [Semafor](https://www.semafor.com/article/03/14/2025/amazons-trainium-chips-to-be-tested-by-anthropic)

**OpenAI**
- **Nov 2025 GPU deal:** Jassy referred on 5 Feb 2026 to "an agreement with OpenAI in November." [CS-3PT] — [TickerTrends Q4 2025](https://tickertrends.io/transcripts/AMZN/Q4-earnings-transcript-2025) The 10-Q describes it as the "$38.0 billion multi-year commitment." [CS-SEC] — [Amazon 10-Q, Q3 2026](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm) SemiAnalysis says OpenAI's AWS cluster uses GB300s with ConnectX-8, not EFA. [EST: SemiAnalysis] — [SemiAnalysis, 4 Dec 2025](https://newsletter.semianalysis.com/p/aws-trainium3-deep-dive-a-potential)
- **27 Feb 2026 deal:** $50B equity; about 2 GW of Trainium (Trainium3 and Trainium4); $100B added over 8 years to the $38B agreement; AWS "exclusive third-party cloud distribution provider for OpenAI Frontier"; a jointly built Stateful Runtime Environment on Bedrock. [CS] — [Amazon PR, 27 Feb 2026](https://press.aboutamazon.com/2026/2/openai-and-amazon-announce-strategic-partnership)
- **Binding status:** the 10-Q says the $100B expansion "includes contractual obligations related to the performance of AWS chips," and the equity was fully funded by Q3 2026. [CS-SEC] — [Amazon 10-Q](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm)
- **Q3 2026 release:** a new AWS agreement with OpenAI, GPT-6 models added to Bedrock, and "Bedrock Managed Agents," described as "powered by OpenAI." [CS] — [Amazon 8-K, Q3 2026](https://www.sec.gov/Archives/edgar/data/0001018724/000101872426000038/amzn-20260930xex991.htm)
- **Work to date:** as of Mar 2026, the Annapurna engineers had done little work with OpenAI, focusing on Anthropic and Amazon. [PRESS] — [TechCrunch, 22 Mar 2026](https://techcrunch.com/2026/03/22/an-exclusive-tour-of-amazons-trainium-lab-the-chip-thats-won-over-anthropic-openai-even-apple/)

**Other customers (AWS-curated unless noted)**
- **Decart** (Dean Leitersdorf): "up to 4x higher frame throughput and 2x better cost efficiency compared to top GPUs"; latency cut from 40 ms to 10 ms. [CUST] — [AWS Trainium customers page](https://aws.amazon.com/machine-learning/trainium/customers/) The Dec 2025 release says "4x faster inference for real-time generative video at half the cost of GPUs." [CS] — [Amazon PR, 2 Dec 2025](https://press.aboutamazon.com/2025/12/trainium3-ultraservers-now-available-enabling-customers-to-train-and-deploy-ai-models-faster-at-lower-cost)
- **Karakuri** (Tomofumi Nakayama): "reduced our LLM training costs by over 50 percent." [CUST] — [AWS customers page](https://aws.amazon.com/machine-learning/trainium/customers/)
- **Poolside** (Joe Rowell): "a price performance ratio unlike other AI accelerators." [CUST] — [AWS customers page](https://aws.amazon.com/machine-learning/trainium/customers/)
- **Ricoh, Metagenomi, NetoAI, Splash Music** (named with Anthropic and Karakuri): "reducing training and inference costs by up to 50% with Trainium" (no per-customer figures). [CS] — [Amazon PR, 2 Dec 2025](https://press.aboutamazon.com/2025/12/trainium3-ultraservers-now-available-enabling-customers-to-train-and-deploy-ai-models-faster-at-lower-cost)
- **Databricks:** 2023 quote on Trainium for Mosaic MPT (see Q1); listed on the AWS Trainium page in Nov 2026. [CUST/CS] — [Amazon PR, 28 Nov 2023](https://press.aboutamazon.com/2023/11/aws-unveils-next-generation-aws-designed-chips); [AWS Trainium page](https://aws.amazon.com/ai/machine-learning/trainium/)
- **Uber:**
  - Q1 2026 release: "leveraging Trainium3 to train the AI models that make every ride smarter over time." [CS] — [Amazon 8-K, Q1 2026](https://www.sec.gov/Archives/edgar/data/0001018724/000101872426000012/amzn-20260331xex991.htm)
  - Jul 2026: "piloting Trainium3." [CS] — [About Amazon, 31 Jul 2026](https://www.aboutamazon.com/news/aws/amazon-ai-chips-business-history)
- **Also named in Jul 2026:** Neura Robotics, Odyssey ("nearly twice the useful compute per dollar"), TwelveLabs, Pinterest. [CS] — [About Amazon, 31 Jul 2026](https://www.aboutamazon.com/news/aws/amazon-ai-chips-business-history)
- **Apple:**
  - 3 Dec 2024, Benoit Dupin (Apple senior director of ML and AI): "In early stages of evaluating Trainium2 we expect early numbers up to 50% improvement in efficiency with pretraining." Apple reported a 40% efficiency gain from Inferentia and Graviton for search. Garman called Apple an early adopter and beta tester. [CUST/CS via PRESS] — [CNBC, 3 Dec 2024](https://www.cnbc.com/2024/12/03/apple-says-it-uses-amazons-custom-ai-chips-.html)
  - TechCrunch's Mar 2026 headline says Trainium "won over… even Apple," but the body cites only the 2024 remarks. [PRESS] — [TechCrunch, 22 Mar 2026](https://techcrunch.com/2026/03/22/an-exclusive-tour-of-amazons-trainium-lab-the-chip-thats-won-over-anthropic-openai-even-apple/)
- **Negative reports (BI, 2025):** Cohere, Stability AI, Typhoon (see Q0). [PRESS-U]

**Binding versus announced**

| Item | Status | Evidence |
|---|---|---|
| OpenAI $50B equity | Executed and fully funded (Q1–Q3 2026) | 10-Q [CS-SEC] |
| OpenAI $38B + $100B / 8-year AWS commitment, with AWS-chip performance obligations | Contractual | 10-Q [CS-SEC] |
| OpenAI "approximately 2 GW" of Trainium | Announced quantity; ramps from 2027 | Press release [CS] |
| Anthropic AWS commitment of more than $100B over 10 years, with AWS-chip performance obligations | Contractual | 10-Q [CS-SEC] |
| Anthropic "up to 5 GW" | Ceiling, announced | Press releases [CS/CUST] |
| Amazon equity in Anthropic: $5B + $5B, plus $15B facility drawable on compute-delivery milestones | Executed / conditional | 10-Q [CS-SEC] |
| Decart, Karakuri, Poolside, Ricoh, Uber, etc. | Testimonials and pilots; no contract terms disclosed | AWS pages [CS/CUST] |
| Apple | Evaluation (Dec 2024); no later confirmation found | CNBC [PRESS] |

### Inferences
- Amazon is both a large equity holder in, and the chip and cloud supplier to, the two labs that account for the multi-gigawatt Trainium commitments. That makes those labs' statements about Trainium non-independent.
- The 10-Q language on "contractual obligations related to the performance of AWS chips" suggests that performance terms are written into the Anthropic and OpenAI contracts. Amazon does not disclose the terms or any penalties.
- In 2025–2026, Trainium usage appears concentrated in Anthropic and Amazon's own Bedrock service; OpenAI's Trainium ramp starts only in 2027. (See the concentration dispute under Q9.)

### Gaps
- I did not retrieve a primary source for the 3 Nov 2025 OpenAI–AWS $38B deal: date, my recollection of a 7-year term, and the GB200/GB300 details.
- The conditions on the $35B OpenAI tranche were not described in the extracted 10-Q text.
- Financial details of Anthropic's Apr 2026 Google/Broadcom expansion were not retrieved.
- I found no evidence of Apple production use of Trainium after Dec 2024.
- I did not verify which specific Claude models were trained mainly on Trainium.

---

## Q5. Capacity: TSMC, design partners (Marvell, Alchip), HBM, data-center power

### Takeaway
- Trainium3 is fabricated at TSMC on N3P, with CoWoS-R packaging.
- Back-end design moved from Marvell (Trainium2) to Alchip (Trainium3 and, reportedly, Trainium4). Marvell disputes reports that it lost AWS business.
- Alchip's North American 3nm customer, widely but not officially identified as AWS, entered mass production in May 2026.
- Rising memory costs pushed Amazon's 2026 capex guidance up $20B.
- Power is the binding constraint Amazon names. It plans to double AWS power from the 2025 level by end-2027.

### Cited Findings
**TSMC**
- Trainium3 is on TSMC N3P with CoWoS-R packaging (organic RDL interposer, 20-layer ABF substrate). SemiAnalysis reported slower-than-expected defect-density improvement on N3P. Trainium2 used N5. [EST: SemiAnalysis] — [SemiAnalysis, 4 Dec 2025](https://newsletter.semianalysis.com/p/aws-trainium3-deep-dive-a-potential)
- "It is a 3-nanometer chip manufactured by TSMC." [PRESS] — [TechCrunch, 22 Mar 2026](https://techcrunch.com/2026/03/22/an-exclusive-tour-of-amazons-trainium-lab-the-chip-thats-won-over-anthropic-openai-even-apple/)
- I retrieved no TSMC statements about AWS.

**Design partners** [EST: SemiAnalysis] — [SemiAnalysis, 4 Dec 2025](https://newsletter.semianalysis.com/p/aws-trainium3-deep-dive-a-potential)
- Annapurna does the front-end design.
- Alchip does back-end physical and package design for Trainium3, with two tapeouts: "Anita" (Alchip-procured) and "Mariana" (Annapurna-procured, carrying most of the volume).
- Marvell "Lost the Trn3 design competition after poor Trn2 execution and interposer problems."
- Alchip leads both Trainium4 tracks.
- Other suppliers: Synopsys (PCIe SerDes license), Astera Labs (PCIe switches and retimers; AWS holds warrants at a $20.34 strike) and Credo (AECs).

**Marvell (supplier statements)** [SUPP via PRESS] — [The Next Platform, "Custom Compute Engine Biz Growing More Than Marvell Ever Hoped", 6 Mar 2026](https://www.nextplatform.com/connect/2026/03/06/custom-compute-engine-biz-growing-more-than-marvell-ever-hoped/4093772)
- Fiscal Q4 2026 call (early Mar 2026): custom AI XPU revenue was about $1.5B in FY2026, will grow at least 20% in FY2027 and then double in FY2028.
- The article reports Marvell's position: "There has been a lot of chatter about Marvell losing the contract to Amazon Web Services … but that has not happened and, based on the forecast, it doesn't look like it is going to happen."
- A search summary attributes to Murphy the line "I have the bookings, the backlog, the orders" (not seen in a fetched page).

**Alchip (supplier statements; Alchip never names Amazon)**
- **26 May 2026:** a major customer's chip "entered mass production in May," described as "its North American customer's 3nm AI accelerator." Alchip expected "strong quarter-over-quarter gains in revenue beginning in the third quarter." Chairman Johnny Shen said 3nm capacity demand is "extremely tight." TrendForce separately said "Amazon's Trainium 3 is expected to begin ramping in 2Q26." [SUPP via PRESS; the Amazon link is TrendForce's] — [TrendForce, 26 May 2026](https://www.trendforce.com/news/2026/05/26/news-alchip-says-key-customers-ai-chip-enters-mass-production-in-may-asics-seen-outpacing-gpu-cagr/)
- **Q2 2026 results (article dated 14 Aug 2026)** [SUPP via PRESS] — [BigGo Finance, 14 Aug 2026](https://finance.biggo.com/news/TW_3661.TW_2026-08-14)
  - Revenue US$241.7M: +82.6% QoQ, −18.7% YoY.
  - Gross margin about 34.9%, down from 50.2% in Q1.
  - North America 51% of revenue (23% in Q1); N3 47% (21% in Q1).
  - Record Q3 expected, with another sequential rise in Q4; H2 gross margin "about 20-something percent."
  - Next-generation N2 chiplet: tape-out by end-2026, production by end-2027. CEO: "the sole design partner for this design."
  - The customer is called "a North American hyperscaler," not named.
- **Epoch's link to Trainium3:** Epoch identifies the May 2026 shipments as Trainium3. It infers 10k–100k units from the more-than-$100M rise in Alchip's Q2 North American revenue. [EST: Epoch] — [Epoch AI methodology](https://epoch.ai/data/ai-chip-sales-documentation/methodology)
- **Q3 2026:** Alchip's newsroom showed the Q2 2026 release (dated 26 Aug 2026) as the latest; no Q3 2026 results were posted. [SUPP] — [Alchip newsroom (accessed 14 Nov 2026)](https://www.alchip.com/en/Newsroom/Alchip_2026_Q3_financial_results)

**HBM**
- Trainium2 used Samsung HBM. Trainium3 uses 4 stacks of 12-high HBM3E (144 GB) from SK Hynix and Micron, with pin speed raised from 5.7 to 9.6 Gbps. Trainium4 is planned with 8 HBM4 stacks. [EST: SemiAnalysis] — [SemiAnalysis, 4 Dec 2025](https://newsletter.semianalysis.com/p/aws-trainium3-deep-dive-a-potential)
- Aug 2026: NVIDIA NVHBM, developed "in partnership with memory suppliers," is planned for Trainium. [CS via PRESS] — [StorageReview, 27 Aug 2026](https://www.storagereview.com/news/aws-and-nvidia-to-deploy-2-million-more-gpus-in-2027-2028-bringing-vera-cpus-and-custom-nvhbm-to-trainium)
- Memory cost:
  - 29 Apr 2026, Jassy: "the cost of these components, particularly memory has skyrocketed." [CS-3PT] — [TickerTrends Q1 2026](https://tickertrends.io/transcripts/AMZN/Q1-earnings-transcript-2026)
  - 30 Jul 2026: capex guidance raised $20B on "The higher cost of memory," and "there are inflated prices right now on some of the components like memory and hard drives and SSDs." [CS-3PT] — [StockAnalysis Q2 2026](https://stockanalysis.com/stocks/amzn/transcripts/657334-q2-2026/)
  - The Q3 2026 release's forward-looking statements cite "resource and supply volatility, including for memory chips." [CS] — [Amazon 8-K, Q3 2026](https://www.sec.gov/Archives/edgar/data/0001018724/000101872426000038/amzn-20260930xex991.htm)

**Supply versus demand**
- Anthropic and Bedrock "are already consuming Trainium chips faster than Amazon can produce them." [PRESS] — [TechCrunch, 22 Mar 2026](https://techcrunch.com/2026/03/22/an-exclusive-tour-of-amazons-trainium-lab-the-chip-thats-won-over-anthropic-openai-even-apple/)
- Anthropic said demand caused "inevitable strain" on its infrastructure, affecting reliability and performance. [CUST via PRESS] — [CNBC, 20 Apr 2026](https://www.cnbc.com/2026/04/20/amazon-invest-up-to-25-billion-in-anthropic-part-of-ai-infrastructure.html)

**Power**
- 30 Oct 2025: "maybe the bottleneck is power"; more than 3.8 GW added in 12 months; "at least another 1 gigawatt" expected in Q4 2025. [CS-3PT] — [Motley Fool Q3 2025](https://www.fool.com/earnings/call-transcripts/2025/10/31/amazon-amzn-q3-2025-earnings-call-transcript/)
- 5 Feb 2026: "We added 1.2 gigawatts of power in Q4." [CS-3PT] — [TickerTrends Q4 2025](https://tickertrends.io/transcripts/AMZN/Q4-earnings-transcript-2025)
- 30 Jul 2026: double the 2025 power capacity by end-2027, and "we will still not have enough capacity to meet all the demand we have in 2026." [CS-3PT] — [StockAnalysis Q2 2026](https://stockanalysis.com/stocks/amzn/transcripts/657334-q2-2026/)
- Customers take "hundreds of megawatts or sometimes up to a gigawatt of capacity" (29 Oct 2026). [CS-3PT] — [Motley Fool Q3 2026](https://www.fool.com/earnings/call-transcripts/2026/10/30/amazon-amzn-q3-2026-earnings-call-transcript/)
- Rainier site: 1,037 MW of IT power (Epoch estimate, Oct 2026); an air permit implies 2.3 GW of facility power. [EST: Epoch] — [Epoch AI](https://epoch.ai/data/ai-data-centers/directory/anthropic-amazon-new-carlisle)

### Inferences
- Alchip's falling gross margin (50.2% in Q1 to about 35% in Q2, guided to "20-something" in H2) while N3 revenue rises fits a high-volume, pass-through-heavy ASIC program. It also fits Epoch's view that the Annapurna-procured "Mariana" variant takes most of the volume, so Alchip's revenue understates unit volume. Both are inferences.

### Gaps
- I found no statements from SK Hynix, Micron, Samsung or TSMC naming AWS or Trainium.
- Marvell's later (Aug–Nov 2026) remarks on AWS were not retrieved.
- Alchip's Q3 2026 results were not available.
- I found no CoWoS capacity allocation to AWS, either company-disclosed or as an estimate.

---

## Q6. Key people (and departures)

### Takeaway
Since 17 Dec 2025, Peter DeSantis leads a combined AI models, chips and quantum organization reporting to Jassy. Rohit Prasad left at end-2025. The other named Annapurna figures in the record are Rami Sinno, Gadi Hutt, Kristopher King and Mark Carroll. I could not verify current roles for Ron Diamant, Dave Brown or Nafea Bshara, or any 2026 departures.

### Cited Findings
- **Andy Jassy (Amazon CEO):** made all the call statements quoted above and wrote the Dec 2025 memo. [CS] — [PYMNTS, 17 Dec 2025](https://www.pymnts.com/amazon/2025/amazon-reorganization-combines-ai-silicon-and-quantum-computing/)
- **Matt Garman (AWS CEO):**
  - Dec 2024: called Apple an early adopter and beta tester of Trainium. [CS via PRESS] — [CNBC, 3 Dec 2024](https://www.cnbc.com/2024/12/03/apple-says-it-uses-amazons-custom-ai-chips-.html)
  - Aug 2026: "Customers want the freedom to choose the best tools for their AI workloads." [CS] — [StorageReview, 27 Aug 2026](https://www.storagereview.com/news/aws-and-nvidia-to-deploy-2-million-more-gpus-in-2027-2028-bringing-vera-cpus-and-custom-nvhbm-to-trainium)
- **Peter DeSantis:**
  - 27 years at Amazon; most recently led AWS Utility Computing.
  - From 17 Dec 2025, leads the AGI team, Nova, silicon (Graviton, Trainium, Nitro) and quantum, reporting to Jassy.
  - [CS via PRESS] — [PYMNTS, 17 Dec 2025](https://www.pymnts.com/amazon/2025/amazon-reorganization-combines-ai-silicon-and-quantum-computing/)
  - Title Jul 2026: "SVP, Amazon AI Models, Chips, & Quantum Computing." [CS] — [About Amazon, 31 Jul 2026](https://www.aboutamazon.com/news/aws/amazon-ai-chips-business-history)
  - Reuters-syndicated coverage says he spearheaded the 2015 Annapurna acquisition. [PRESS] — [The Star (Reuters), 18 Dec 2025](https://www.thestar.com.my/tech/tech-news/2025/12/18/amazon-shakes-up-ai-team-as-veteran-prasad-leaves-desantis-promoted)
- **Rohit Prasad (AGI head):** left at the end of 2025, "of his own accord" per Jassy. [CS via PRESS] — [PYMNTS](https://www.pymnts.com/amazon/2025/amazon-reorganization-combines-ai-silicon-and-quantum-computing/); [The Star (Reuters)](https://www.thestar.com.my/tech/tech-news/2025/12/18/amazon-shakes-up-ai-team-as-veteran-prasad-leaves-desantis-promoted)
- **Pieter Abbeel:** leads base-model (frontier) research within AGI and continues in robotics. [CS via PRESS] — [PYMNTS](https://www.pymnts.com/amazon/2025/amazon-reorganization-combines-ai-silicon-and-quantum-computing/)
- **Founders and board:** Annapurna was co-founded in 2011 by Hrvoje Bilic, Nafea Bshara and Ronen Boneh. Avigdor Willenz is described as an investor and board member; Lip-Bu Tan and Manuel Alba are also listed as board members. [PRESS] — [Wikipedia, Annapurna Labs](https://en.wikipedia.org/wiki/Annapurna_Labs)
- **Rami Sinno (director of engineering, Annapurna Labs, Mar 2025):** "We take vertical integration to an extreme." [CS] — [Semafor, 14 Mar 2025](https://www.semafor.com/article/03/14/2025/amazons-trainium-chips-to-be-tested-by-anthropic)
- **Gadi Hutt (Annapurna Labs, Mar 2025):** described Rainier's multi-building design, and an early-2020s compiler flaw found by an Anthropic engineer on first-generation Trainium. [CS] — [Semafor](https://www.semafor.com/article/03/14/2025/amazons-trainium-chips-to-be-tested-by-anthropic)
- **Kristopher King (director of the Austin Trainium lab) and Mark Carroll (director of engineering), Mar 2026:** King said "Our customer base is just expanding as fast as we can get capacity out there." Carroll said Trainium3 "is breaking all kinds of records" in "price per power." [CS] — [TechCrunch, 22 Mar 2026](https://techcrunch.com/2026/03/22/an-exclusive-tour-of-amazons-trainium-lab-the-chip-thats-won-over-anthropic-openai-even-apple/)
- **Anthropic side:** Tom Brown (co-founder, chief compute officer) said Trainium "required a learning curve" and that Amazon opened its instruction set. [CUST] — [Semafor](https://www.semafor.com/article/03/14/2025/amazons-trainium-chips-to-be-tested-by-anthropic) James Bradbury is Head of Compute. [CUST] — [AWS customers page](https://aws.amazon.com/machine-learning/trainium/customers/)

### Inferences
- The Dec 2025 reorganization put model development (Nova/AGI) and chip development (Annapurna) under one executive, the same person credited with the Annapurna acquisition.

### Gaps
- Not verified (search budget exhausted): current titles of Ron Diamant (recalled as Trainium chief architect), Dave Brown (recalled as VP of Compute and ML Services), Nafea Bshara (recalled as VP and Distinguished Engineer) and Gadi Hutt's exact title. Any Annapurna departures in 2026 were also not checked.

---

## Q7. Legal and regulatory

### Takeaway
- **Chip-specific:** Xockets patent litigation targets AWS Nitro in W.D. Tex. (filed Jun 2025). An ITC investigation instituted in Jun 2026 names Annapurna Labs along with AWS, NVIDIA and Microsoft, over GB200/GB300-based AWS products, not Trainium.
- **Group-level:** a new Aug 2026 FTC and 22-state complaint concerns ad-auction reserve prices. The UK CMA closed its Amazon/Anthropic review in Sep 2024 without investigation.
- **Export controls:** I found no Trainium-specific action.

### Cited Findings
- **Xockets** [CS-SEC] — [Amazon 10-Q, Q3 2026, filed 30 Oct 2026](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm)
  - June 2025: two complaints in W.D. Tex. allege that certain versions of the AWS Nitro System infringe seven patents.
  - "In May 2026, Xockets filed a complaint against Amazon.com, Inc., Amazon Web Services, Inc.," … "at the U.S. International Trade Commission alleging … that EC2 P6e-GB200 UltraServers…" infringe. Respondents also include Annapurna Labs, NVIDIA and Microsoft.
  - "In June 2026, the International Trade Commission instituted an investigation," and Xockets "has also alleged that AWS products with GB300 servers infringe."
  - Amazon: "We dispute the allegations of wrongdoing and intend to defend ourselves vigorously."
- **FTC** [CS-SEC] — [Amazon 10-Q, Q3 2026](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm)
  - "In August 2026, the Federal Trade Commission and 22 state Attorneys General filed a complaint against Amazon.com, Inc.," "involving the use of reserve prices in Amazon's sponsored ad auctions."
  - On the broader antitrust cases: "In the U.S., most of Amazon's motions to dismiss were granted in part, but in each case, at least some of the claims survived."
- **UK CMA (Amazon/Anthropic)** [regulator record] — [UK CMA case page, "Amazon / Anthropic partnership merger inquiry" (accessed 14 Nov 2026)](https://www.gov.uk/cma-cases/amazon-slash-anthropic-partnership-merger-inquiry)
  - Invitation to comment 24 Apr 2024; inquiry launched 8 Aug 2024.
  - Phase 1 decision 27 Sep 2024: "Amazon's partnership with Anthropic does not qualify for investigation under the merger provisions of the Enterprise Act 2002."
  - Full text published 17 Oct 2024; the case is closed, with no later updates covering the 2026 investments.
- **Microsoft and the OpenAI–Amazon deal:** the Financial Times reported that Microsoft may believe the OpenAI–Amazon deal, including Frontier exclusivity, violates its agreement with OpenAI. Unresolved in the reporting. [PRESS-U, FT via TechCrunch] — [TechCrunch, 22 Mar 2026](https://techcrunch.com/2026/03/22/an-exclusive-tour-of-amazons-trainium-lab-the-chip-thats-won-over-anthropic-openai-even-apple/)
- **Anthropic classifier report:** a Tech Times item (24 Sep 2026, citing WCCFTech testing) says Anthropic's export-restriction classifier for "Opus 5.5" also flagged Trainium3 topics. Neither company had commented. Single-source; not verified (seen only as a search excerpt). — [Tech Times, 24 Sep 2026](https://www.techtimes.com/articles/327994/20260924/anthropic-builds-own-ai-export-restriction-opus-55-amazons-chip-caught-too.htm)

### Inferences
- Trainium has so far been offered only as an AWS cloud service, not sold as chips. Export-control exposure would therefore run through cloud access rules. Planned external chip sales from late 2027 would bring hardware export rules directly into play. This is an inference; I found no source discussing it.

### Gaps
- I did not retrieve the trial date or status of the 2023 FTC monopolization case (my unverified recollection: trial set for Feb 2027) or of the Sep 2025 Prime settlement.
- The CMA decision's reasoning (e.g., a turnover threshold) is not on the case page and was not retrieved.
- I found no Trainium- or Inferentia-specific patent case or export-control action.
- The 10-Q's Item 1A risk factors and Part II legal section were truncated in my fetch.

---

## Q8. Science and engineering: what is demonstrated, who verified it, what is unproven, physical limits, and whether it stands on solid ground

### Takeaway
Trainium's existence, production and large-scale use are established by several independent lines of evidence:
- supplier shipments (Alchip);
- satellite and permit data on Project Rainier (Epoch);
- Anthropic's own statements, though Anthropic is not independent of Amazon.

Its performance and efficiency claims are not established:
- There is no MLPerf submission or third-party benchmark of Trainium2/3 in the record.
- NVIDIA's CEO publicly challenged the "40%" claim.
- The 2025 BI documents recorded customer reports of underperformance against H100s.

The engineering limits are documented mainly by SemiAnalysis: scale-up topology, cross-rack bandwidth, software maturity, HBM supply and cost, and power.

### Cited Findings
**Demonstrated, and by whom**
- **Production and deployment at scale:**
  - Amazon states 1.4M Trainium2 "landed" (Feb 2026). [CS] — [Amazon 8-K, Q4 2025](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000002/amzn-20251231xex991.htm)
  - Anthropic states it uses "over one million Trainium2 chips to train and serve Claude" (20 Apr 2026). [CUST; not independent: Amazon is an investor] — [Anthropic](https://www.anthropic.com/news/anthropic-amazon-compute)
  - Epoch's satellite and permit analysis independently shows the Rainier campus buildings operational and estimates about 1 GW of IT power (Oct 2026). Epoch's chip-type and chip-count figures rely on Amazon statements. [IV: Epoch AI for construction and power] — [Epoch AI](https://epoch.ai/data/ai-data-centers/directory/anthropic-amazon-new-carlisle)
- **Trainium3 manufacturing:** Alchip's May 2026 N3 mass production for a North American customer is consistent with Trainium3. Epoch and TrendForce make the identification; Alchip does not. [IV: partial; supplier data] — [TrendForce](https://www.trendforce.com/news/2026/05/26/news-alchip-says-key-customers-ai-chip-enters-mass-production-in-may-asics-seen-outpacing-gpu-cagr/); [Epoch AI](https://epoch.ai/data/ai-chip-sales-documentation/methodology)
- **Training and serving Claude:**
  - Amazon, 5 Feb 2026: "they're training the next Claude model on top of Tranium two." [CS-3PT] — [TickerTrends Q4 2025](https://tickertrends.io/transcripts/AMZN/Q4-earnings-transcript-2025)
  - Anthropic says it trains and serves on Trainium2 [CUST]. Anthropic describes a three-platform strategy (TPU, Trainium, GPU). [CUST] — [Anthropic, 23 Oct 2025](https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services)
  - The Dwarkesh podcast host said Claude and Gemini "were trained on TPU" (15 Apr 2026). This is an interviewer assertion. [PRESS] — [Dwarkesh Podcast, Jensen Huang episode, 15 Apr 2026](https://www.dwarkesh.com/p/jensen-huang)
- **Bedrock on Trainium:** "majority of token usage" (Oct 2025), "most of its inference" (Apr 2026), "the majority and most of Bedrock" (Oct 2026). Amazon is serving its own production traffic on Trainium; this is self-reported. [CS] — [Motley Fool Q3 2025](https://www.fool.com/earnings/call-transcripts/2025/10/31/amazon-amzn-q3-2025-earnings-call-transcript/); [TickerTrends Q1 2026](https://tickertrends.io/transcripts/AMZN/Q1-earnings-transcript-2026); [Motley Fool Q3 2026](https://www.fool.com/earnings/call-transcripts/2026/10/30/amazon-amzn-q3-2026-earnings-call-transcript/)
- **MLPerf and InferenceMAX/InferenceX:**
  - I found no Trainium or Inferentia MLPerf submission.
  - Jensen Huang, 15 Apr 2026: competitors avoid MLPerf ("Nobody wants to show up"); TPUs and Trainium have not appeared on SemiAnalysis's InferenceMAX. [COMP] — [Dwarkesh Podcast, 15 Apr 2026](https://www.dwarkesh.com/p/jensen-huang)
  - SemiAnalysis had said it planned Trainium backends, per search excerpts; I found no published Trainium3 InferenceX result. — [SemiAnalysis, "InferenceX v2: NVIDIA Blackwell Vs AMD vs Hopper - Formerly InferenceMAX"](https://newsletter.semianalysis.com/p/inferencex-v2-nvidia-blackwell-vs); [SemiAnalysis, "InferenceMAX: Open Source Inference Benchmarking"](https://newsletter.semianalysis.com/p/inferencemax-open-source-inference)
- **Amazon Nova:** I found no source confirming Nova training on Trainium (see Gaps).

**Reported problems**
- **BI, ~Nov 2025, on a July 2025 internal document:** Cohere found Trainium1/2 underperforming H100s, with "extremely limited" Trainium2 access and service disruptions. Stability AI found Trainium2 "less competitive" on latency and cost. Typhoon found A100s up to 3x more cost-efficient than Inferentia2 for certain workloads. Amazon said the Cohere case was "not current." [PRESS-U] — [X relay, 8 Nov 2025](https://x.com/HyperTechInvest/status/1987131006315270522); [Financial World](https://www.financial-world.org/news/news/financial/29473/startups-say-amazons-trainium-chips-trail-nvidia-in-real-workloads/)
- **BI (cited by Semafor, Mar 2025):** 2024 Trainium usage among top AWS customers was 0.5% of Nvidia GPU usage. [PRESS-U] — [Semafor](https://www.semafor.com/article/03/14/2025/amazons-trainium-chips-to-be-tested-by-anthropic)
- **SemiAnalysis, Dec 2024** [EST: SemiAnalysis] — [SemiAnalysis, 3 Dec 2024](https://newsletter.semianalysis.com/p/amazons-ai-self-sufficiency-trainium2-architecture-networking)
  - PyTorch XLA is "buggy"; JAX support is in beta.
  - Anthropic engineers write assembly to work around software gaps.
  - Scale-out bandwidth is 6.4x (Trn2) to 25.6x (Trn2 UltraServer) lower than scale-up.
  - One failed chip can take down a 64-chip domain, and fault-tolerant routing is not implemented.
  - Arithmetic intensity is 225.9 BF16 FLOP/byte, against 300–560 for TPUv6e, GB200 and H100.
- **SemiAnalysis, Dec 2025** [EST: SemiAnalysis] — [SemiAnalysis, 4 Dec 2025](https://newsletter.semianalysis.com/p/aws-trainium3-deep-dive-a-potential)
  - Poor Trn2 execution and interposer problems at Marvell; N3P leakage and defect-density risk.
  - No native NVFP4, and MXFP4 runs no faster than MXFP8.
  - The E8M0 block scale is less accurate, so more advanced quantization-aware training is needed.
  - LNC=8 delayed to mid-2026.
  - "Not convinced" EFA beats Spectrum-X or InfiniBand.
- **Morgan Stanley (Jul 2025):** a gap between Trn2/2.5 output and system installs due to PCB yields. [EST via relay] — [X relay, 10 Jul 2025](https://x.com/Jukanlosreve/status/1943316885434663204)
- **Bring-up:** a heat-sink dimension mismatch, fixed by grinding (TechCrunch, Mar 2026). [PRESS] — [TechCrunch](https://techcrunch.com/2026/03/22/an-exclusive-tour-of-amazons-trainium-lab-the-chip-thats-won-over-anthropic-openai-even-apple/)
- **Learning curve:** Anthropic's Tom Brown said Trainium "required a learning curve" (Mar 2025). [CUST] — [Semafor](https://www.semafor.com/article/03/14/2025/amazons-trainium-chips-to-be-tested-by-anthropic)

**Unproven claims (company-stated, no independent verification found)**
- **Trainium3 multiples:** 4.4x compute, "4x greater energy efficiency," "4x lower latency," "almost 4x more memory bandwidth" (UltraServer level, Dec 2025). Also "over five times the output tokens per megawatt" (Jul 2026), "up to 40% better price-performance" (Jul 2026), and customer cost reductions "up to 50%." [CS] — [Amazon PR, 2 Dec 2025](https://press.aboutamazon.com/2025/12/trainium3-ultraservers-now-available-enabling-customers-to-train-and-deploy-ai-models-faster-at-lower-cost); [About Amazon, 31 Jul 2026](https://www.aboutamazon.com/news/aws/amazon-ai-chips-business-history)
- **Trainium4:** ≥3x FP8, ≥6x FP4, 4x memory bandwidth (secondary reports of AWS claims); 2x capacity (SemiAnalysis). [CS via PRESS / EST]
- **Price-performance and savings:**
  - Trainium2 is "30 to 40%" (Feb 2026) or "about 30%" (Apr 2026) better on price-performance than comparable GPUs.
  - "save us tens of billions of dollars of CapEx each year" (Apr 2026).
  - Customers "saved more than $2 billion in Q3 alone" (Oct 2026).
  - [CS-3PT] — [TickerTrends Q4 2025](https://tickertrends.io/transcripts/AMZN/Q4-earnings-transcript-2025); [TickerTrends Q1 2026](https://tickertrends.io/transcripts/AMZN/Q1-earnings-transcript-2026); [Motley Fool Q3 2026](https://www.fool.com/earnings/call-transcripts/2026/10/30/amazon-amzn-q3-2026-earnings-call-transcript/)
  - Challenged by Huang: "I would welcome Trainium to demonstrate their 40% that they claim all the time." [COMP] — [Dwarkesh, 15 Apr 2026](https://www.dwarkesh.com/p/jensen-huang)
- **AWS-claimed utilization (MFU) on Trainium3:** 43% via torch.compile and about 60% with NKI on dense models. Reported by SemiAnalysis; not independently measured. [CS via EST] — [SemiAnalysis, 4 Dec 2025](https://newsletter.semianalysis.com/p/aws-trainium3-deep-dive-a-potential)
- **Migration effort:** Carroll's claim that moving from Nvidia is a "one-line change," then recompile. [CS] — [TechCrunch, 22 Mar 2026](https://techcrunch.com/2026/03/22/an-exclusive-tour-of-amazons-trainium-lab-the-chip-thats-won-over-anthropic-openai-even-apple/)

**Physical and engineering limits**
- **Power and cooling:**
  - Trainium2 runs at about 500 W per chip in air-cooled racks. [EST: SemiAnalysis] — [SemiAnalysis, 3 Dec 2024](https://newsletter.semianalysis.com/p/amazons-ai-self-sufficiency-trainium2-architecture-networking)
  - The 144-chip Trn3 "NL72x2" is liquid-cooled. The 64-chip "NL32x2" is the only switched SKU deployable in air-cooled halls, and SemiAnalysis expects most 2026 Trn3 shipments to be NL32x2. [EST: SemiAnalysis] — [SemiAnalysis, 4 Dec 2025](https://newsletter.semianalysis.com/p/aws-trainium3-deep-dive-a-potential)
  - SemiAnalysis estimates a peak PUE of about 1.2 for air-optimized halls versus about 1.5 for central-pipe designs. [EST: SemiAnalysis] — [same](https://newsletter.semianalysis.com/p/aws-trainium3-deep-dive-a-potential)
  - Jassy: "maybe the bottleneck is power" (Oct 2025). [CS-3PT] — [Motley Fool Q3 2025](https://www.fool.com/earnings/call-transcripts/2025/10/31/amazon-amzn-q3-2025-earnings-call-transcript/)
- **NeuronLink scale-up domain:** [EST: SemiAnalysis] — [SemiAnalysis, 3 Dec 2024](https://newsletter.semianalysis.com/p/amazons-ai-self-sufficiency-trainium2-architecture-networking); [SemiAnalysis, 4 Dec 2025](https://newsletter.semianalysis.com/p/aws-trainium3-deep-dive-a-potential)
  - Trn2: a 64-chip 3D torus.
  - Trn3: a switched 144-chip domain. The Gen1 160-lane PCIe switch (Astera Scorpio X) "is not all-to-all."
  - Cross-rack bandwidth is under 10% of in-rack backplane bandwidth.
  - NL72x2 Gen1 needs 368 switches and 11,520 copper cables per 144-chip domain.
  - Gen2 (320-lane) and Gen3 (UALink) switches are planned.
  - With NVLink Fusion, Trainium4 may reach coherent domains of 144+ (SemiAnalysis estimate).
- **EFA scale-out:**
  - 200 Gb/s per chip by default, 400 Gb/s optional (EFAv4 / Nitro-v6). [EST: SemiAnalysis] — [SemiAnalysis, 4 Dec 2025](https://newsletter.semianalysis.com/p/aws-trainium3-deep-dive-a-potential)
  - AWS: up to 28.8 Tbps per UltraServer. [CS] — [AWS Trainium page](https://aws.amazon.com/ai/machine-learning/trainium/)
  - OpenAI's AWS GPU cluster uses ConnectX-8, not EFA. [EST: SemiAnalysis] — [same](https://newsletter.semianalysis.com/p/aws-trainium3-deep-dive-a-potential)
- **HBM:** Trainium3 has 144 GB and 4.9 TB/s per chip. [CS] Each LNC=2 logical device sees only 36 GB until LNC=8 arrives. [EST: SemiAnalysis] Memory price inflation raised Amazon's capex guide. [CS-3PT] — [AWS Trainium page](https://aws.amazon.com/ai/machine-learning/trainium/); [SemiAnalysis](https://newsletter.semianalysis.com/p/aws-trainium3-deep-dive-a-potential); [StockAnalysis Q2 2026](https://stockanalysis.com/stocks/amzn/transcripts/657334-q2-2026/)
- **Numerics:** BF16, FP16 and FP32 throughput are unchanged from Trn2 to Trn3; only MXFP8/MXFP4 doubled. [EST: SemiAnalysis] — [SemiAnalysis, 4 Dec 2025](https://newsletter.semianalysis.com/p/aws-trainium3-deep-dive-a-potential)

### Inferences (evidence assessment, not a recommendation)
- **Solid ground: existence, scale and use.** Three partly independent sources converge: Amazon's 1.4M figure, Anthropic's ">1M Trainium2," and Epoch's satellite and permit data for Rainier. Alchip's N3 ramp supports Trainium3 production, though its identity as Trainium3 is not confirmed by Alchip.
- **Weak ground: performance and efficiency multiples, price-performance percentages, and savings figures.**
  - All of them come from Amazon or from customers Amazon selects or invests in.
  - No standardized third-party benchmark (MLPerf, InferenceX) was found.
  - The only documented negative evidence (BI's 2025 internal documents) dates from the Trainium1/2 era, and Amazon calls it "not current."
- **Engineering risk concentrates in:**
  1. software maturity (Neuron/NKI, LNC=8, PyTorch-native support);
  2. scale-up topology and cross-rack bandwidth;
  3. dependence on NVIDIA IP for Trainium4's scale-up and memory (NVLink Fusion, NVHBM);
  4. HBM cost and supply;
  5. power availability.

### Gaps
- I found no MLPerf submission, independent benchmark or peer-reviewed paper measuring Trainium2/3 performance.
- I found no Anthropic statement naming a specific Claude model trained mainly on Trainium.
- I found no confirmation that Amazon Nova models were trained on Trainium.
- Trainium3 chip TDP was not retrieved (paywalled).
- I did not review a Spheron blog (2026) comparing Trainium3 with H200 and B200; its methodology is unknown. — [Spheron](https://www.spheron.network/blog/aws-trainium-3-vs-nvidia-h200-b200-llm-training-inference-2026/)

---

## Q9. Cross-examination log: contradictions and tensions recorded

### Takeaway
I recorded 18 contradictions or tensions:
- Amazon's own numbers are inconsistent across releases on energy efficiency, chip counts and the "chips business" definition.
- The "GA" label for Trainium3 preceded volume.
- Customer concentration is disputed between Jassy and NVIDIA's CEO.
- The Marvell–SemiAnalysis accounts of the Trainium3 contract conflict.
- An unnamed-source "no more debt in 2026" report conflicts with later borrowing.

### Cited Findings
1. **Trainium3 energy-efficiency claim (three different numbers).**
   - "4x greater energy efficiency" (UltraServer vs Trn2 UltraServer): [Amazon PR, 2 Dec 2025](https://press.aboutamazon.com/2025/12/trainium3-ultraservers-now-available-enabling-customers-to-train-and-deploy-ai-models-faster-at-lower-cost).
   - "40% more energy efficient than the previous generation" (AWS claim as reported): [TechCrunch, 2 Dec 2025](https://techcrunch.com/2025/12/02/amazon-releases-an-impressive-new-ai-chip-and-teases-a-nvidia-friendly-roadmap/).
   - "over five times the output tokens per megawatt of Trainium2": [About Amazon, 31 Jul 2026](https://www.aboutamazon.com/news/aws/amazon-ai-chips-business-history).
   - The metrics and system levels differ, and Amazon has not reconciled them.
2. **Trainium3 gain: price-performance vs raw compute.**
   - Price-performance: "about 40% better than Trainium2" (Jassy, 30 Oct 2025) and "up to 40% better price-performance" (Jul 2026).
   - Raw compute: 4.4x at UltraServer level and up to 2x MXFP8 per chip.
   - The modest price-performance gain against large raw-compute gains is not explained (pricing or cost per chip not disclosed). — [Motley Fool Q3 2025](https://www.fool.com/earnings/call-transcripts/2025/10/31/amazon-amzn-q3-2025-earnings-call-transcript/); [About Amazon](https://www.aboutamazon.com/news/aws/amazon-ai-chips-business-history); [AWS Trainium page](https://aws.amazon.com/ai/machine-learning/trainium/)
3. **Trainium2 price-performance vs GPUs.**
   - Amazon: "30% to 40%" (30 Oct 2025; 5 Feb 2026), narrowed to "about 30%" (29 Apr 2026).
   - NVIDIA's Huang: "I would welcome Trainium to demonstrate their 40%" (15 Apr 2026).
   - BI-reported July 2025 internal document: Cohere found Trainium1/2 underperforming H100; Stability AI found Trainium2 "less competitive." Amazon replied the Cohere case was "not current."
   - Sources: [Motley Fool Q3 2025](https://www.fool.com/earnings/call-transcripts/2025/10/31/amazon-amzn-q3-2025-earnings-call-transcript/); [TickerTrends Q1 2026](https://tickertrends.io/transcripts/AMZN/Q1-earnings-transcript-2026); [Dwarkesh](https://www.dwarkesh.com/p/jensen-huang); [X relay of BI](https://x.com/HyperTechInvest/status/1987131006315270522)
4. **Trainium3 "generally available" vs actual volume.**
   - "GA" was announced 2 Dec 2025.
   - Amazon itself expected "preview at the end of this year" with "fuller volumes" in early 2026 (30 Oct 2025) and said Trainium3 "just started shipping at the start of 2026" (29 Apr 2026).
   - The supplier's N3 mass production started in May 2026 (customer unnamed). Epoch's median estimate is under 100k Trainium3 units in 1H26.
   - Sources: [Amazon PR](https://press.aboutamazon.com/2025/12/trainium3-ultraservers-now-available-enabling-customers-to-train-and-deploy-ai-models-faster-at-lower-cost); [Motley Fool Q3 2025](https://www.fool.com/earnings/call-transcripts/2025/10/31/amazon-amzn-q3-2025-earnings-call-transcript/); [TickerTrends Q1 2026](https://tickertrends.io/transcripts/AMZN/Q1-earnings-transcript-2026); [TrendForce](https://www.trendforce.com/news/2026/05/26/news-alchip-says-key-customers-ai-chip-enters-mass-production-in-may-asics-seen-outpacing-gpu-cagr/); [Epoch](https://epoch.ai/data/ai-chip-sales-documentation/methodology)
5. **"1.4 million" chip count.**
   - Amazon: "landed over 1.4 million" Trainium2 chips; "Trainium2 is fully subscribed with 1.4 million chips landed" (5 Feb 2026).
   - TechCrunch: "1.4 million Trainium chips are deployed across three generations" (22 Mar 2026).
   - Sources: [Amazon 8-K](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000002/amzn-20251231xex991.htm); [TechCrunch](https://techcrunch.com/2026/03/22/an-exclusive-tour-of-amazons-trainium-lab-the-chip-thats-won-over-anthropic-openai-even-apple/)
6. **Project Rainier "1 million by end-2025" vs later statements.**
   - Activation coverage: capacity "expected to exceed one million Trainium2 chips by the end of 2025" (29 Oct 2025). Jassy: "500,000 plus chips going to 1 million" (30 Oct 2025).
   - On 5 Feb 2026 Jassy still cited "500,000 chips there."
   - Anthropic's ">1M Trainium2" (Apr 2026) is fleet-wide. Amazon says Rainier spans "multiple U.S. data centers."
   - Whether Rainier itself reached 1M is unconfirmed.
   - Sources: [Converge Digest](https://convergedigest.com/aws-activates-project-rainier-data-center-campus/); [Motley Fool Q3 2025](https://www.fool.com/earnings/call-transcripts/2025/10/31/amazon-amzn-q3-2025-earnings-call-transcript/); [TickerTrends Q4 2025](https://tickertrends.io/transcripts/AMZN/Q4-earnings-transcript-2025); [Anthropic](https://www.anthropic.com/news/anthropic-amazon-compute)
7. **Anthropic Trainium2 count on two Amazon/Anthropic surfaces.**
   - "almost a million Trainium2 chips" (Bradbury, AWS customer page, undated).
   - "over one million" (Anthropic, 20 Apr 2026; About Amazon, 31 Jul 2026).
   - Probably a timing difference; the AWS page is undated.
   - Sources: [AWS customers page](https://aws.amazon.com/machine-learning/trainium/customers/); [Anthropic](https://www.anthropic.com/news/anthropic-amazon-compute)
8. **Definition of the "chips business" run rate changed.**
   - ">$10 billion," "inclusive of Graviton and Tranium" (5 Feb 2026).
   - ">$20 billion," including Graviton, Trainium and Nitro (29 Apr 2026).
   - ">$25 billion" for Trainium, Graviton and Nitro (30–31 Jul 2026).
   - Nitro was added to the definition, so the jump from $10B to $20B is not like-for-like.
   - Sources: [TickerTrends Q4 2025](https://tickertrends.io/transcripts/AMZN/Q4-earnings-transcript-2025); [Amazon 8-K, Q1 2026](https://www.sec.gov/Archives/edgar/data/0001018724/000101872426000012/amzn-20260331xex991.htm); [About Amazon](https://www.aboutamazon.com/news/aws/amazon-ai-chips-business-history)
9. **Customer concentration.**
   - Jassy (30 Oct 2025): "Trainium is being used by a small number of very large customers."
   - Huang (15 Apr 2026): "It's 100% Anthropic." [COMP]
   - Amazon names Bedrock (internal), OpenAI (ramps 2027), Uber (pilot), Decart and others.
   - Sources: [Motley Fool Q3 2025](https://www.fool.com/earnings/call-transcripts/2025/10/31/amazon-amzn-q3-2025-earnings-call-transcript/); [Dwarkesh](https://www.dwarkesh.com/p/jensen-huang); [About Amazon](https://www.aboutamazon.com/news/aws/amazon-ai-chips-business-history)
10. **Marvell and the Trainium3 contract.**
    - SemiAnalysis (4 Dec 2025): Marvell "Lost the Trn3 design competition after poor Trn2 execution and interposer problems."
    - Next Platform, reporting Marvell's position (6 Mar 2026): the reported loss of the AWS contract "has not happened."
    - Sources: [SemiAnalysis](https://newsletter.semianalysis.com/p/aws-trainium3-deep-dive-a-potential); [The Next Platform](https://www.nextplatform.com/connect/2026/03/06/custom-compute-engine-biz-growing-more-than-marvell-ever-hoped/4093772)
11. **Alchip customer identity.**
    - Media and Epoch identify Alchip's North American 3nm customer as Trainium3.
    - Alchip names only "a North American hyperscaler" (May and Aug 2026).
    - A search summary claimed Alchip management said "Trainium 3 is pretty much the contribution from N3." The fetched BigGo summary does not support that. Unconfirmed.
    - Sources: [TrendForce](https://www.trendforce.com/news/2026/05/26/news-alchip-says-key-customers-ai-chip-enters-mass-production-in-may-asics-seen-outpacing-gpu-cagr/); [BigGo](https://finance.biggo.com/news/TW_3661.TW_2026-08-14); [Epoch](https://epoch.ai/data/ai-chip-sales-documentation/methodology)
12. **Debt: "won't issue any more debt this year" vs later borrowing.**
    - CNBC (7 Jul 2026, people familiar): Amazon told underwriters it "won't issue any more debt this year."
    - The 10-Q shows September 2026 Sterling Notes (£4.3B, about $5.6B) and a $17.5B term loan drawn in Sep 2026.
    - The CNBC statement may have referred only to USD bonds; this is not clarified.
    - Sources: [CNBC](https://www.cnbc.com/2026/07/07/amazon-bond-sale-ai-debt.html); [Amazon 10-Q](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm)
13. **UltraCluster scale.**
    - "up to 1 million Trainium3 chips" (AWS claim per TechCrunch, 2 Dec 2025).
    - AWS product page (accessed Nov 2026): UltraClusters 3.0 scale to "hundreds of thousands of chips."
    - Sources: [TechCrunch](https://techcrunch.com/2025/12/02/amazon-releases-an-impressive-new-ai-chip-and-teases-a-nvidia-friendly-roadmap/); [AWS Trainium page](https://aws.amazon.com/ai/machine-learning/trainium/)
14. **Apple.**
    - TechCrunch headline (22 Mar 2026): Trainium "won over… even Apple."
    - The article body and the only primary evidence (Dupin, 3 Dec 2024) describe only an evaluation of Trainium2 ("early stages of evaluating").
    - Sources: [TechCrunch](https://techcrunch.com/2026/03/22/an-exclusive-tour-of-amazons-trainium-lab-the-chip-thats-won-over-anthropic-openai-even-apple/); [CNBC](https://www.cnbc.com/2024/12/03/apple-says-it-uses-amazons-custom-ai-chips-.html)
15. **Self-sufficiency vs NVIDIA dependence.**
    - Jassy: "We are not constrained in any way in buying NVIDIA" (Oct 2025); NVIDIA: "continue to order substantial quantities" (Apr 2026).
    - Aug 2026: 2 million more NVIDIA GPUs for 2027–28, with Trainium4's scale-up and memory built on NVIDIA NVLink Fusion and NVHBM.
    - SemiAnalysis titled its 2024 piece "Amazon's AI Self Sufficiency."
    - A tension rather than a contradiction: Trainium4 adopts NVIDIA IP.
    - Sources: [Motley Fool Q3 2025](https://www.fool.com/earnings/call-transcripts/2025/10/31/amazon-amzn-q3-2025-earnings-call-transcript/); [TickerTrends Q1 2026](https://tickertrends.io/transcripts/AMZN/Q1-earnings-transcript-2026); [StorageReview](https://www.storagereview.com/news/aws-and-nvidia-to-deploy-2-million-more-gpus-in-2027-2028-bringing-vera-cpus-and-custom-nvhbm-to-trainium)
16. **Investment tied to chip use.**
    - The Information (via The Decoder, Nov 2024): Amazon conditioned its second Anthropic investment on more Trainium use.
    - Semafor (Mar 2025, two unnamed people): the chip agreement is separate from the investment decision.
    - The 2026 10-Q shows Amazon's Anthropic financing facility unlocks on "delivery milestones of compute capacity."
    - Sources: [The Decoder](https://the-decoder.com/amazon-wants-anthropic-to-switch-from-nvidia-to-amazon-chips/); [Semafor](https://www.semafor.com/article/03/14/2025/amazons-trainium-chips-to-be-tested-by-anthropic); [Amazon 10-Q](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm)
17. **Project Rainier cost.**
    - $11B (Amazon, Indiana activation coverage, Oct 2025).
    - Epoch's estimated current capital cost: $39.3B (Oct 2026), including IT equipment and later buildings.
    - Different scope (phase 1 buildings vs full IT build-out and later phases).
    - Sources: [Converge Digest](https://convergedigest.com/aws-activates-project-rainier-data-center-campus/); [Epoch AI](https://epoch.ai/data/ai-data-centers/directory/anthropic-amazon-new-carlisle)
18. **Where Claude is trained.**
    - Amazon (5 Feb 2026): Anthropic is "training the next Claude model on top of Tranium two."
    - Dwarkesh host (15 Apr 2026): Claude was "trained on TPU."
    - Anthropic's own statements describe a three-platform strategy: it trains and serves on Trainium2 alongside TPUs and GPUs.
    - Not necessarily contradictory, but unresolved for any specific model.
    - Sources: [TickerTrends Q4 2025](https://tickertrends.io/transcripts/AMZN/Q4-earnings-transcript-2025); [Dwarkesh](https://www.dwarkesh.com/p/jensen-huang); [Anthropic, 23 Oct 2025](https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services)

### Inferences
- Most contradictions arise because Amazon's numeric claims shift in metric, scope and baseline (system vs chip, Trainium-only vs "chips business," Rainier vs the Anthropic fleet). Independent sources rarely measure the same quantity, so most claims cannot be tested directly.

### Gaps
- I did not obtain responses from Cohere, Stability AI or Typhoon to the BI report. One secondary source says Cohere and Stability AI did not respond to requests for comment.

---

## Q10. Consolidated list: what could not be found or verified

### Takeaway
The main unverifiable areas are:
- Trainium-only revenue;
- independent performance benchmarks;
- the original BI article;
- chip-specific legal and export-control matters;
- current roles of several Annapurna executives;
- launch dates of first-generation products;
- supplier (TSMC, HBM makers) statements.

Part of this is due to the exhausted search budget.

### Cited Findings
- No Trainium-only revenue or unit disclosure by Amazon was found, and no Trainium3 unit count as of 14 Nov 2026. The disclosures available are the "chips business" run rate and revenue commitments. — [Amazon 8-K, Q3 2026](https://www.sec.gov/Archives/edgar/data/0001018724/000101872426000038/amzn-20260930xex991.htm)
- Alchip's Q3 2026 results were not posted on its newsroom when checked on 14 Nov 2026. — [Alchip newsroom](https://www.alchip.com/en/Newsroom/Alchip_2026_Q3_financial_results)

### Inferences
- None beyond those stated in the sections above.

### Gaps (not found or not verified)
1. Original Business Insider article on the July 2025 internal document (URL, headline, date). Only secondary relays were found. I also found no specific 2025–2026 Information report on Trainium underperformance, capacity or latency beyond the Nov 2024 investment-condition report.
2. Any MLPerf Training or Inference submission for Trainium or Inferentia; any published Trainium3 InferenceX result; any peer-reviewed or third-party benchmark paper.
3. Primary-source dates for Inf1 GA, Trn1 GA, Inf2 GA and Trn2 UltraServer GA. The Dec 2024 Trainium3 announcement and its original promised timing were also not confirmed from a fetched primary source.
4. AWS's own wording for the Trainium4 multiples (FP8/FP4/bandwidth) and any Trainium4 date more precise than "2027" or "about 18 months from broad availability" (as of Apr 2026).
5. Trainium3 chip TDP and rack power (paywalled at SemiAnalysis).
6. AWS backlog for Q1 and Q2 2025, and the claim that 2027 capex will rise "meaningfully" (seen only in a Yahoo summary).
7. Primary details of the Nov 2025 OpenAI–AWS $38B deal (exact date, term, GPU types), and the conditions on the $35B OpenAI tranche.
8. Financial terms of Anthropic's Apr 2026 Google/Broadcom expansion.
9. Statements by TSMC, SK Hynix, Micron or Samsung naming AWS or Trainium; CoWoS allocation to AWS.
10. Marvell's Aug–Nov 2026 statements on AWS; whether Murphy said "I have the bookings, the backlog, the orders" (search summary only).
11. Current titles of Ron Diamant, Dave Brown and Nafea Bshara, and Gadi Hutt's exact title. Any 2026 Annapurna departures.
12. Status and trial date of the 2023 FTC monopolization case and details of the Sep 2025 Prime settlement (not retrieved). The CMA decision's reasoning.
13. Any export-control action specific to Trainium. The Tech Times Sep 2026 report about Anthropic's classifier flagging Trainium3 is single-source and unverified.
14. Confirmation that Project Rainier reached 1M Trainium2 chips, and identification of Rainier sites outside Indiana. Amazon's reported additional $15B Northwest Indiana investment (Nov 2025) was seen only in a search excerpt.
15. Confirmation that Amazon Nova models were trained on Trainium, and identification of specific Claude models trained mainly on Trainium.
16. Apple's use of Trainium after the Dec 2024 evaluation.
17. Whether the LNC=8 software milestone (mid-2026) shipped.
18. Exact dates of re:Invent 2026. It is scheduled for early Dec 2026 and had not taken place as of 14 Nov 2026.
