# AMD data-center AI accelerators (Instinct GPUs, Helios rack-scale systems): fact base as of 14 November 2026

**Provenance tags (on every bullet):**
- **[CO]**: stated by AMD in a press release, at an event, on an earnings call or in a blog.
- **[CO-SEC]**: stated by AMD in an SEC filing (8-K, 10-Q, 10-K or proxy).
- **[CO+CUST]**: a joint AMD–customer statement, or a customer speaking in an AMD release or on AMD's stage.
- **[3P-CO]**: another company's statement about its own products, for example NVIDIA.
- **[IND: who]**: measured or verified independently by the named party.
- **[EST: who]**: an estimate by an analyst, an industry source or a journalist.
- **[PRESS-UNNAMED]**: a press report citing unnamed sources or rumors.
- **[SECONDARY]**: seen only in secondary coverage or a search-result summary. The primary text was not retrieved, so confidence is lower.

**Method notes:**
- The session's shared web-search quota ran out partway through. After that, items were collected by fetching known primary URLs: SEC EDGAR filings and AMD IR pages.
- Anything that could not be retrieved is listed under Gaps and in section 10(b).
- **Disclosure:** these notes were compiled by Claude, a model made by Anthropic. Anthropic is an AMD customer (up to 2 GW) and the prospective recipient of an AMD equity investment (up to $5B). Facts about Anthropic below come only from AMD materials.

**AMD fiscal calendar:**
- FY2024 ended 28 Dec 2024.
- FY2025 ended 27 Dec 2025.
- Q1'26 ended 28 Mar 2026, Q2'26 ended 27 Jun 2026 and Q3'26 ended 26 Sep 2026.
- Source: [AMD Form 10-Q for Q3 2026, filed 2026-11-04](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm).

---

## 1. Products and their stage (as of 14 Nov 2026), including whether MI450/Helios shipped in H2 2026 and to whom

### Takeaway
- **Shipping in volume:** MI300X, MI325X, MI350X and MI355X are in customer production. Per AMD, the MI455X (MI450 Series) began shipping in volume in Q3 2026.
- **First Helios racks:** AMD says Anthropic, Meta, Microsoft, OpenAI and Oracle each brought their first Helios racks online. OEM Helios shipments are due to start in Q4 2026.
- **Not yet shipping:** the MI430X ships in H1 2027. MI500 (2027) and MI600 (2028) are announced only.
- **No independent confirmation:** I found no confirmation of Helios production deployments from anyone other than AMD or its customers. The latest AMD–Meta release (27 Oct 2026) describes Helios at Meta as "installed and being tested."

### Cited Findings

**Product stage table (each row dated)**

| Product | Stage / status (date) | Provenance | Source |
|---|---|---|---|
| MI300X | In production at customers as of 12 Jun 2025: Meta (Llama 3 and Llama 4 inference), Microsoft Azure (proprietary and open models), OpenAI (research and GPT models on Azure), Cohere (Command models) | [CO+CUST] | [AMD, "AMD Unveils Vision for an Open AI Ecosystem… at Advancing AI 2025," 2025-06-12](https://ir.amd.com/news-events/press-releases/detail/1255/amd-unveils-vision-for-an-open-ai-ecosystem-detailing-new-silicon-software-and-systems-at-advancing-ai-2025) |
| MI300X | Zyphra pretrained ZAYA1 (8.3B total / 760M active MoE) on 128 nodes × 8 MI300X (1,024 GPUs; the total is my arithmetic), with Pensando Pollara 400, ROCm 6.4 and IBM Cloud (announced 24 Nov 2025) | [CO+CUST] | [AMD, "AMD Powers Frontier AI Training for Zyphra," 2025-11-24](https://ir.amd.com/news-events/press-releases/detail/1268/amd-powers-frontier-ai-training-for-zyphra) |
| MI308 (China-market part) | Needed a US license from Apr 2025. AMD got some licenses and "began shipping products at the end of fiscal 2025" to certain China-based customers | [CO-SEC] | [AMD 10-Q Q3'26, filed 2026-11-04](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm) |
| MI325X (256 GB HBM3E, 6 TB/s) | Su said volume production began in Q4 2024 (Q4'24 call, 4 Feb 2025). In H1 2026 AMD received licenses to ship MI325 to certain China customers (details in §7) | [CO] via press; [CO-SEC] | [The Next Platform, "AMD Moves Up Instinct MI355X Launch…," 2025-02-05](https://www.nextplatform.com/compute/2025/02/05/amd-moves-up-instinct-mi355x-launch-as-datacenter-biz-hits-records/1646757); [AMD 10-Q Q3'26](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm) |
| MI350X / MI355X (CDNA 4, 3 nm, 288 GB HBM3E, 8 TB/s) | Launched 12 Jun 2025, "already rolling out" at OCI, "broad availability in 2H 2025." Submitted to MLPerf Inference 6.0 (Apr 2026) with 9 partner submitters. HUMAIN MI355X GPU-as-a-service live 31 Aug 2026. Anthropic using MI355X racks (Nov 2026 call) | [CO]; [IND: MLCommons-published results]; [CO+CUST] | [AMD Advancing AI 2025 release, 2025-06-12](https://ir.amd.com/news-events/press-releases/detail/1255/amd-unveils-vision-for-an-open-ai-ecosystem-detailing-new-silicon-software-and-systems-at-advancing-ai-2025); [The Decoder, 2026-04-02](https://the-decoder.com/nvidia-sets-new-mlperf-records-with-288-gpus-while-amd-and-intel-focus-on-different-battles/); [AMD/Cisco/HUMAIN release, 2026-08-31](https://ir.amd.com/news-events/press-releases/detail/1298/amd-cisco-and-humain-expand-saudi-arabias-ai-infrastructure-as-amd-instinct-systems-go-live); [Motley Fool, AMD Q3 2026 call transcript, 2026-11-04](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/) |
| MI350P | "Launched to add AI acceleration to existing infrastructure" (Q2'26) | [CO-SEC] (8-K exhibit) | [AMD Q2 2026 results (8-K Ex. 99.1), 2026-08-04](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000121/q22026991.htm) |
| MI455X (MI450 Series, CDNA 5) | Launched at Advancing AI 2026 (23 Jul 2026). Su on the Q3'26 call: "We started shipping MI455X in volume in the quarter" | [CO] | [AMD, "AAI 2026: AMD Delivers Full-Stack Compute…," 2026-07-23](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era); [Motley Fool Q3 2026 transcript, 2026-11-04](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/) |
| Custom MI450-based GPU (Meta) | 24 Feb 2026: shipments for Meta's first GW "scheduled to begin in the second half of 2026." 27 Oct 2026: Helios racks "installed and being tested" at Meta. No volume disclosed for the custom GPU | [CO+CUST] | [AMD–Meta release, 2026-02-24](https://ir.amd.com/news-events/press-releases/detail/1279/amd-and-meta-announce-expanded-strategic-partnership-to-deploy-6-gigawatts-of-amd-gpus); [AMD–Meta release, 2026-10-27](https://ir.amd.com/news-events/press-releases/detail/1302/amd-and-meta-advance-strategic-partnership-to-power-metas-superintelligence-infrastructure) |
| MI430X (HPC / sovereign AI) | Up to 288 TFLOPS hardware FP64. Ships H1 2027 (per iTWire's report of AAI 2026). EuroHPC LUMI-AI comes online 2H 2027; ORNL Discovery delivery 2028; also Alice Recoque (France) and HPE "Herder" | [CO] | [AAI 2026 release, 2026-07-23](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era); [iTWire, 2026-07-24](https://itwire.com/business-it-news/data/astounding-massive-dominant-ai-innovation-amd-launches-helios-against-nvidia-tips-up-to-us-5-billion-into-anthropic-and-books-roughly-14-gigawatts-of-customer-ai-compute-at-advanci); [Q3'26 call](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/); [CES 2026 release, 2026-01-05](https://ir.amd.com/news-events/press-releases/detail/1272/amd-and-its-partners-share-their-vision-for-ai-everywhere-for-everyone-at-ces-2026); [Q4/FY2025 release, 2026-02-03](https://ir.amd.com/news-events/press-releases/detail/1276/amd-reports-fourth-quarter-and-full-year-2025-financial) |
| MI440X | Announced 5 Jan 2026 for eight-GPU on-premises enterprise systems. Shipping status not found | [CO] | [AMD CES 2026 release, 2026-01-05](https://ir.amd.com/news-events/press-releases/detail/1272/amd-and-its-partners-share-their-vision-for-ai-everywhere-for-everyone-at-ces-2026) |
| Helios rack | "Now in production" (23 Jul 2026). Q3'26 was the first quarter of revenue shipments. First racks online at Anthropic, Meta, Microsoft, OpenAI and OCI. HPE, Dell, Lenovo, Supermicro and others to begin shipping Helios systems in Q4'26. AMD "do[es] not manufacture or sell the completed Helios rack-scale solutions" | [CO]; [CO-SEC] | [AAI 2026 release](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era); [Q3'26 8-K Ex. 99.1, 2026-11-03](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000188/q32026991.htm); [Q3'26 call](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/); [10-Q Q3'26](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm) |
| "Helion" | Reference architecture for rack-scale agentic-AI systems with configurable CPU/GPU mixes (released 12 Oct 2026) | [CO] | [Q3'26 8-K Ex. 99.1](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000188/q32026991.htm); [AMD IR release list](https://ir.amd.com/news-events/press-releases) |
| MI500 (CDNA 6, 2 nm, HBM4E) | Announced for 2027. "Helios 500" pairs it with EPYC "Verano" and Pensando "Como"/"Monza" | [CO] | [CES 2026 release](https://ir.amd.com/news-events/press-releases/detail/1272/amd-and-its-partners-share-their-vision-for-ai-everywhere-for-everyone-at-ces-2026); [AAI 2026 release](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era) |
| MI600 | Announced for 2028. "Helios 600" pairs it with EPYC "Ferrara" and Pensando "Palma"/"Levanzo" | [CO] | [AAI 2026 release](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era) |
| 6th Gen EPYC "Venice" (Zen 6, TSMC 2 nm) | Production ramp announced 21 May 2026. Up to 256 cores (EPYC 9996) and up to 203B transistors. Venice-HF is the Helios host CPU, 18 per rack | [CO] | [AMD IR release, 2026-05-21 (title)](https://ir.amd.com/news-events/press-releases/detail/1287/amd-announces-production-ramp-of-next-generation-amd-epyc-processor-venice-on-tsmc-2nm-process-technology); [AAI 2026 release](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era); [iTWire, 2026-07-24](https://itwire.com/business-it-news/data/astounding-massive-dominant-ai-innovation-amd-launches-helios-against-nvidia-tips-up-to-us-5-billion-into-anthropic-and-books-roughly-14-gigawatts-of-customer-ai-compute-at-advanci) |
| Pensando "Vulcano" AI NIC | Named as Helios's scale-out NIC (CES 2026 and AAI 2026). No separate shipping data | [CO] | [CES 2026 release](https://ir.amd.com/news-events/press-releases/detail/1272/amd-and-its-partners-share-their-vision-for-ai-everywhere-for-everyone-at-ces-2026); [iTWire](https://itwire.com/business-it-news/data/astounding-massive-dominant-ai-innovation-amd-launches-helios-against-nvidia-tips-up-to-us-5-billion-into-anthropic-and-books-roughly-14-gigawatts-of-customer-ai-compute-at-advanci) |

**MI455X and Helios specifications** (AMD claims unless noted)
- **MI455X silicon:** 320B transistors, built on TSMC 2 nm and 3 nm across 12 compute and I/O chiplets, with 432 GB of HBM4 (AMD at AAI 2026). [CO] reported by press. — [iTWire, 2026-07-24](https://itwire.com/business-it-news/data/astounding-massive-dominant-ai-innovation-amd-launches-helios-against-nvidia-tips-up-to-us-5-billion-into-anthropic-and-books-roughly-14-gigawatts-of-customer-ai-compute-at-advanci)
- **MI455X memory bandwidth (disputed):** 19.6 TB/s per GPU, per AMD's Helios brochure and TensorWave's MI455X page. Other outlets cite about 23.3 TB/s. See §9 CX-8. [SECONDARY] — [AMD Helios brochure (PDF; returned 503 on fetch)](https://www.amd.com/content/dam/amd/en/documents/solutions/ai/amd-helios-bro.pdf); [TensorWave MI455X page](https://tensorwave.com/products/accelerators/amd-mi455x); [Digital Citizen](https://www.digitalcitizen.life/amd-instinct-mi455x-brings-432gb-of-hbm4-and-40-pflops-of-ai-compute-to-helios/); [Flopper](https://flopper.io/gpu/amd-instinct-mi455x)
- **MI455X compute:** about 40 PFLOPS dense FP4 and about 20 PFLOPS FP8 ("expected performance," TensorWave listing). [SECONDARY] — [TensorWave](https://tensorwave.com/products/accelerators/amd-mi455x)
- **Helios rack (AMD at AAI 2026):** 72 MI455X GPUs across 18 compute trays, 6th Gen EPYC CPUs, Pensando Vulcano AI NICs, 2.9 exaflops FP4, 31 TB HBM4 and 1.7 PB/s memory bandwidth. Scale-up runs "over UALink and Ethernet, not NVLink." [CO] reported by press. — [iTWire, 2026-07-24](https://itwire.com/business-it-news/data/astounding-massive-dominant-ai-innovation-amd-launches-helios-against-nvidia-tips-up-to-us-5-billion-into-anthropic-and-books-roughly-14-gigawatts-of-customer-ai-compute-at-advanci)
- **Helios at CES (5 Jan 2026):** "up to 3 AI exaflops of performance in a single rack." [CO] — [AMD CES 2026 release](https://ir.amd.com/news-events/press-releases/detail/1272/amd-and-its-partners-share-their-vision-for-ai-everywhere-for-everyone-at-ces-2026)
- **Helios networking (AAI 2026 release):** the official wording is "AMD Pensando™ front-end, scale-up and scale-out networking." The release does not name UALink or Ultra Ethernet. [CO] — [AAI 2026 release, 2026-07-23](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era)
- **Scale-up label:** SemiAnalysis calls AMD's first rack "MI455X UALoE72", meaning UALink over Ethernet. [IND/EST: SemiAnalysis] — [SemiAnalysis, "InferenceX v2," 2026-02-16](https://newsletter.semianalysis.com/p/inferencex-v2-nvidia-blackwell-vs)
- **Scale-up bandwidth and scale-out spec:** 260 TB/s of scale-up bandwidth per rack, with scale-out using Ultra Ethernet Consortium specifications, per a summary of Hot Chips coverage. [SECONDARY] — [ai2.work, "AMD Helios at Hot Chips…"](https://ai2.work/blog/amd-helios-at-hot-chips-2-9-exaflops-and-31tb-hbm4-in-one-rack)
- **Rack form factor:** Helios is a double-wide rack built to the Open Rack Wide v3 spec, developed with Meta. It can hold 64, 72 or 128 GPUs; Next Platform as of 23 Feb 2026. [press] — [The Next Platform, 2026-02-23](https://www.nextplatform.com/compute/2026/02/23/amd-says-helios-racks-and-mi400-series-gpus-on-track-for-2h-2026/4092199)
- **Helios showcase (14 Oct 2025):** AMD showcased Helios on the OCP "Open Rack for AI" introduced by Meta (release title). [CO] — [AMD IR release list, page 5](https://ir.amd.com/news-events/press-releases?page=5)
- **Power:** I found no AMD-published MI455X board power or Helios rack power. Flopper lists "no verified data." Introl estimates about 140 kW per rack, which AMD has not confirmed. [EST: Introl; SECONDARY] — [Introl blog](https://introl.com/blog/amd-helios-mi455x-nvidia-competition-ces-2026); [Flopper](https://flopper.io/gpu/amd-instinct-mi455x)

**ROCm software versions**
- **ROCm 6.4:** the version Zyphra used for ZAYA1 training (footnote, Nov 2025). [CO+CUST] — [AMD Zyphra release, 2025-11-24](https://ir.amd.com/news-events/press-releases/detail/1268/amd-powers-frontier-ai-training-for-zyphra)
- **ROCm 7:** announced 12 Jun 2025. [CO] — [AMD Advancing AI 2025 release](https://ir.amd.com/news-events/press-releases/detail/1255/amd-unveils-vision-for-an-open-ai-ecosystem-detailing-new-silicon-software-and-systems-at-advancing-ai-2025)
- **ROCm.ai (Q2/Q3 2026):** released as an "AI-native developer experience."
  - It includes HyperLoom, a kernel-writing and kernel-testing engine.
  - ROCm releases now ship every 6 weeks, previously every 4 months.
  - AMD claims average gains over ROCm 7 on the same hardware of 3.3x for inference and 2.4x for training.
  - [CO] — [AMD Q2'26 8-K Ex. 99.1](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000121/q22026991.htm); [iTWire, 2026-07-24](https://itwire.com/business-it-news/data/astounding-massive-dominant-ai-innovation-amd-launches-helios-against-nvidia-tips-up-to-us-5-billion-into-anthropic-and-books-roughly-14-gigawatts-of-customer-ai-compute-at-advanci)
- **ROCm 10 (released by Q3'26):** adds the ROCm.AI developer experience. Su says its agentic tuning turns "weeks of engineering optimization into hours." [CO] — [Q3'26 8-K Ex. 99.1](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000188/q32026991.htm); [Q3'26 call](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/)

**Did MI450/Helios ship in H2 2026, and to whom?**
- **Q3'26 results (3 Nov 2026):**
  - Data Center growth was driven partly by "the launch of AMD Instinct™ MI450 Series GPUs."
  - The 27% sequential Data Center increase was "primarily driven by initial MI450 Series sales" and server growth.
  - Anthropic, Meta, Microsoft, OpenAI and OCI are "running models and workloads on the first Helios rack-scale systems."
  - [CO-SEC] — [AMD Q3 2026 results, 8-K Ex. 99.1, 2026-11-03](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000188/q32026991.htm)
- **Su on the Q3'26 call:**
  - "We started shipping MI455X in volume in the quarter." Q3 was the first quarter of MI455/Helios revenue, and a "big step up" is expected in Q4.
  - Lead customers "including Anthropic, Meta, Microsoft, OpenAI and Oracle, brought their first Helios racks online quickly."
  - HPE, Dell, Lenovo, Supermicro and other OEM/ODM partners are to begin shipping Helios systems in Q4.
  - No unit or dollar figures were given.
  - [CO] — [Motley Fool, AMD Q3 2026 call transcript, 2026-11-04](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/)
- **Vultr via HPE:** "HPE said Vultr will deploy the first Helios by HPE systems." [CO, citing HPE] — [Q3'26 8-K Ex. 99.1](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000188/q32026991.htm)
- **OpenAI timing (AAI 2026, 23 Jul 2026):** OpenAI "expects to bring Helios online beginning in the fourth quarter of 2026," with deployments accelerating through 2027. [CO+CUST] — [AAI 2026 release](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era)
- **OpenAI early racks:** OpenAI said it received Helios racks about three months before 23 Jul 2026 (roughly April 2026) and was running frontier-class workloads on them. [CO+CUST] reported by press. — [iTWire, 2026-07-24](https://itwire.com/business-it-news/data/astounding-massive-dominant-ai-innovation-amd-launches-helios-against-nvidia-tips-up-to-us-5-billion-into-anthropic-and-books-roughly-14-gigawatts-of-customer-ai-compute-at-advanci)
- **Meta (27 Oct 2026):** Helios systems "are installed and being tested by Meta," with a "broader deployment in the near future." [CO+CUST] — [AMD–Meta release, 2026-10-27](https://ir.amd.com/news-events/press-releases/detail/1302/amd-and-meta-advance-strategic-partnership-to-power-metas-superintelligence-infrastructure)
- **Warrant vesting:** as of 26 Sep 2026, "no warrant shares had vested or become exercisable" under the OpenAI or Meta warrants. The first tranche of each vests on the initial 1 GW. [CO-SEC] — [AMD 10-Q Q3'26](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm)

### Inferences
- On AMD's own account, MI450-series revenue shipments began in Q3 2026. That falls inside the "2H 2026" window AMD promised in Oct 2025 and matches the "begin in Q3 2026" promise from Nov 2025.
- The evidence as of 14 Nov 2026 shows first racks and testing, not gigawatt-scale operation. Three things point that way: no warrant tranche had vested by 26 Sep 2026, OpenAI's own guide is "beginning Q4 2026," and Meta described its racks as "being tested."
- "Shipping Helios racks for revenue" should be read as AMD selling GPUs, CPUs and NICs that go into racks built by ODMs and OEMs. The 10-Q says AMD does not sell completed Helios racks.

### Gaps
- No independent confirmation, in volume terms, of Helios deployments: no named-source press reporting, no teardown, no third-party benchmark. AMD disclosed no units or dollars.
- Not researched or not found:
  - MI300A status.
  - MI308 specifications.
  - MI440X shipping status.
  - Official MI455X board power, Helios rack power and cooling specification.
  - An official AMD primary source for scale-up bandwidth and whether Ultra Ethernet is used.

---

## 2. Technology, roadmap and milestones: each commitment, its date, and whether it was met, slipped or is pending; reported delays

### Takeaway
- **Met on AMD's account:**
  - The MI325X production start in Q4 2024.
  - The MI350 pull-in to mid-2025.
  - The "Helios/MI450 begins Q3 2026" commitment, with first revenue shipments in Q3 2026.
- **Pending:** gigawatt-scale deployments (OpenAI from Q4 2026; Anthropic in H1 2027), MI430X (H1 2027), MI500 (2027) and MI600 (2028).
- **Delay reports:** by 16 Feb 2026, SemiAnalysis reported that MI455X mass production and "first production tokens" would slip to Q2 2027. AMD denied it.
- **Status of that dispute:** AMD then reported volume shipments in Q3 2026. No independent evidence settles the gigawatt-scale timing yet.

### Cited Findings

**Commitment-by-commitment status table**

| # | Commitment (date made, venue) | Status as of 14 Nov 2026 | Provenance | Sources |
|---|---|---|---|---|
| 1 | Annual Instinct cadence: MI325X in Q4 2024, MI350 in 2025, MI400 in 2026 (Computex, Jun 2024; Advancing AI, Oct 2024) | Source texts not retrieved (see Gaps). Outcomes are in rows 2–5 | n/a | n/a |
| 2 | MI325X production in Q4 2024 | **Met per AMD.** Su said volume production began in Q4 2024 (call of 4 Feb 2025). Customer availability timing and demand not verified | [CO] via press | [The Next Platform, 2025-02-05](https://www.nextplatform.com/compute/2025/02/05/amd-moves-up-instinct-mi355x-launch-as-datacenter-biz-hits-records/1646757) |
| 3 | MI350/MI355X moved from "some time in the second half of 2025" to "mid year" (Q4'24 call, 4 Feb 2025) | **Met.** Launched 12 Jun 2025, "already rolling out in hyperscaler deployments such as Oracle Cloud Infrastructure," "broad availability in 2H 2025." MLPerf submissions followed (Apr 2026 round documented) | [CO]; [IND: MLCommons results] | [The Next Platform, 2025-02-05](https://www.nextplatform.com/compute/2025/02/05/amd-moves-up-instinct-mi355x-launch-as-datacenter-biz-hits-records/1646757); [AMD Advancing AI 2025 release, 2025-06-12](https://ir.amd.com/news-events/press-releases/detail/1255/amd-unveils-vision-for-an-open-ai-ecosystem-detailing-new-silicon-software-and-systems-at-advancing-ai-2025); [The Decoder, 2026-04-02](https://the-decoder.com/nvidia-sets-new-mlperf-records-with-288-gpus-while-amd-and-intel-focus-on-different-battles/) |
| 4 | Helios named as the "next generation AI rack" on MI400, Venice and Vulcano (12 Jun 2025; no date in the release). MI400 projected at "up to 10x" MoE inference over the prior generation | Superseded by rows 5–6 | [CO] | [AMD Advancing AI 2025 release](https://ir.amd.com/news-events/press-releases/detail/1255/amd-unveils-vision-for-an-open-ai-ecosystem-detailing-new-silicon-software-and-systems-at-advancing-ai-2025) |
| 5 | OpenAI: "The first 1 gigawatt deployment of AMD Instinct MI450 GPUs is set to begin in the second half of 2026" (6 Oct 2025) | **Started, not complete.** First racks are online (Q3'26 call). OpenAI expects Helios online "beginning in the fourth quarter of 2026" (Jul 2026). No tranche vested at 26 Sep 2026 | [CO]; [CO+CUST]; [CO-SEC] | [AMD–OpenAI release, 2025-10-06](https://ir.amd.com/news-events/press-releases/detail/1260/amd-and-openai-announce-strategic-partnership-to-deploy-6-gigawatts-of-amd-gpus); [AAI 2026 release](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era); [10-Q Q3'26](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm) |
| 6 | Financial Analyst Day (11 Nov 2025): Helios with MI450 "expected to begin in Q3 2026"; MI500 "planned launch in 2027" | **Helios: met on AMD's account** (first MI450 revenue in Q3'26). **MI500: pending** | [CO]; [CO-SEC] | [AMD FAD release, 2025-11-11](https://ir.amd.com/news-events/press-releases/detail/1266/amd-unveils-strategy-to-lead-the-1-trillion-compute-market-and-accelerate-next-phase-of-growth); [Q3'26 8-K Ex. 99.1](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000188/q32026991.htm) |
| 7 | CES 2026 (5 Jan 2026): Helios "early look" (no ship date); MI440X announced; MI500 in 2027 on CDNA 6, 2 nm and HBM4E, "up to a 1,000x increase in AI performance" vs MI300X | **Pending.** The 1,000x figure is an engineering projection of peak theoretical rack performance made in Dec 2025, "subject to change" | [CO] | [AMD CES 2026 release](https://ir.amd.com/news-events/press-releases/detail/1272/amd-and-its-partners-share-their-vision-for-ai-everywhere-for-everyone-at-ces-2026) |
| 8 | Forrest Norrod (New Street Research call, week before 23 Feb 2026): "highly confident of ramping Helios in high volume in the second half of the year"; first silicon shown; "right on track" | **Partly evidenced.** Volume MI455X shipments began in Q3. OEM Helios shipments start in Q4. Scale undisclosed | [CO] via press | [The Next Platform, 2026-02-23](https://www.nextplatform.com/compute/2026/02/23/amd-says-helios-racks-and-mi400-series-gpus-on-track-for-2h-2026/4092199) |
| 9 | Meta: shipments for the first GW "scheduled to begin in the second half of 2026" (24 Feb 2026) | **In progress.** Helios at Meta "installed and being tested" (27 Oct 2026). Custom-GPU shipment volume not disclosed | [CO+CUST] | [AMD–Meta release, 2026-02-24](https://ir.amd.com/news-events/press-releases/detail/1279/amd-and-meta-announce-expanded-strategic-partnership-to-deploy-6-gigawatts-of-amd-gpus); [AMD–Meta release, 2026-10-27](https://ir.amd.com/news-events/press-releases/detail/1302/amd-and-meta-advance-strategic-partnership-to-power-metas-superintelligence-infrastructure) |
| 10 | Helios "on track for multi-gigawatt deployments beginning in 2H 2026" (21 May 2026, Taiwan release) | **Pending.** Only first racks are confirmed so far | [CO] | [AMD Taiwan investments release, 2026-05-21](https://ir.amd.com/news-events/press-releases/detail/1286/amd-announces-more-than-10-billion-in-taiwan-ecosystem-investments-to-accelerate-ai-infrastructure) |
| 11 | Microsoft: "AMD begins shipping Helios to customers, including Microsoft, in the second half of 2026" (20 Jul 2026) | **Initial step met.** Microsoft is named among customers with first Helios racks online (Q3 call) | [CO+CUST]; [CO] | [AMD–Microsoft release, 2026-07-20](https://ir.amd.com/news-events/press-releases/detail/1291/microsoft-to-deploy-next-gen-amd-instinct-and-amd-epyc-processors-as-the-companies-expand-their-long-term-strategic-partnership); [Q3'26 call](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/) |
| 12 | Advancing AI 2026 (23 Jul 2026): Helios "now in production"; MI430X ships H1 2027 (per iTWire); MI500 2027; MI600 2028; Zen 7 EPYC ("Florence", "Ferrara", "Fidenza") 2028; Zen 8 "Ravenna" 2030 | **Pending** (all future dates). Coverage says shipments start "at the end of the third quarter" and ramp into 2027 [SECONDARY] | [CO] | [AAI 2026 release](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era); [iTWire](https://itwire.com/business-it-news/data/astounding-massive-dominant-ai-innovation-amd-launches-helios-against-nvidia-tips-up-to-us-5-billion-into-anthropic-and-books-roughly-14-gigawatts-of-customer-ai-compute-at-advanci); [TechWire Asia summary](https://techwireasia.com/2026/07/amd-advancing-ai-2026-helios-openai-meta-anthropic/) |
| 13 | Anthropic: "deployment of the first gigawatt beginning in the first half of 2027" (22 Jul 2026) | **Pending** | [CO] | [AMD–Anthropic release, 2026-07-22](https://ir.amd.com/news-events/press-releases/detail/1292/amd-and-anthropic-announce-strategic-partnership-to-deploy-up-to-2-gigawatts-of-amd-instinct-mi450-series-gpus) |
| 14 | HUMAIN: next phase of up to 250 MW of MI400 begins deploying in 2027 with capacity in 2H 2027; JV "up to 1 GW" by 2030 (31 Aug 2026) | **Pending** | [CO+CUST] | [AMD/Cisco/HUMAIN release, 2026-08-31](https://ir.amd.com/news-events/press-releases/detail/1298/amd-cisco-and-humain-expand-saudi-arabias-ai-infrastructure-as-amd-instinct-systems-go-live) |
| 15 | DOE / ORNL (27 Oct 2025): Lux (MI355X) deploys "early 2026"; Discovery (MI430X + Venice) delivered 2028 with user operations in 2029 | **Lux status not verified this session. Discovery pending** | [CO+CUST] | [AMD–DOE release, 2025-10-27](https://ir.amd.com/news-events/press-releases/detail/1264/amd-powers-u-s-sovereign-ai-factory-supercomputers-accelerating-an-open-american-ai-stack) |
| 16 | 2030 goal: 20x rack-scale energy efficiency from a 2024 base (12 Jun 2025). AMD says MI350 beat its earlier 30x node goal, reaching 38x | **Pending** (the 38x is company-stated) | [CO] | [AMD Advancing AI 2025 release](https://ir.amd.com/news-events/press-releases/detail/1255/amd-unveils-vision-for-an-open-ai-ecosystem-detailing-new-silicon-software-and-systems-at-advancing-ai-2025) |
| 17 | Q3'26 call (3 Nov 2026): Q4 growth from scaling Helios and Venice; 2027 revenue growth above 80%; data-center AI "significantly more than double" in 2027 | **Pending** | [CO] | [Q3'26 call](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/) |

**Reported delays to MI455X/Helios, and HBM4/N2 issues**
- **SemiAnalysis claim (16 Feb 2026):** "first production tokens will only be generated on an MI455X UALoE72 by Q2 2027." The same piece says Google TPU, AWS Trainium and Nvidia are the only AI chips with rack-scale designs deployed today. [EST: SemiAnalysis] — [SemiAnalysis, "InferenceX v2: NVIDIA Blackwell Vs AMD vs Hopper," 2026-02-16](https://newsletter.semianalysis.com/p/inferencex-v2-nvidia-blackwell-vs)
- **Next Platform's relay (23 Feb 2026):**
  - SemiAnalysis's view: engineering samples and low-volume production of the MI455X UALoE72 system come in H2 2026, but "manufacturing delays" push the mass-production ramp and first production tokens to Q2 2027.
  - Next Platform also mentions "unconfirmed street rumors of a thermal design issue."
  - AMD did not mention any delays in its early-February results.
  - [EST: SemiAnalysis]; [PRESS-UNNAMED] for the rumor — [The Next Platform, 2026-02-23](https://www.nextplatform.com/compute/2026/02/23/amd-says-helios-racks-and-mi400-series-gpus-on-track-for-2h-2026/4092199)
- **AMD's response:**
  - Norrod denied the thermal rumor: "I have no idea where that's coming from."
  - Doug Huang (ZT Systems co-founder, now AMD SVP of Data Center Platform Engineering) described validation using dummy hot plates as "early risk retirement."
  - [CO] — [The Next Platform, 2026-02-23](https://www.nextplatform.com/compute/2026/02/23/amd-says-helios-racks-and-mi400-series-gpus-on-track-for-2h-2026/4092199)
- **Other press coverage of the denial:**
  - AMD software VP Anush Elangovan reportedly called the report "BS. Right on target for H2 2026."
  - Tom's Hardware's headline quotes AMD saying Helios systems are "on target for 2H 2026."
  - TechPowerUp's headline: "AMD Instinct MI455X Reportedly Facing Delays, Only Low-Volume Production This Year."
  - [SECONDARY]; article bodies not retrieved — [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/amd-denies-report-of-mi455x-delays-as-nvidia-vr200-systems-are-rumored-to-arrive-early-company-says-helios-systems-on-target-for-2h-2026); [HotHardware](https://hothardware.com/news/amd-naysays-mi400-delay); [OC3D](https://overclock3d.net/news/gpu-displays/bs-amd-engineer-refutes-claims-of-instinct-mi455x-delays/); [TipRanks](https://www.tipranks.com/news/your-assessment-is-still-wrong-says-amd-in-response-to-an-instinct-mi455x-delay-report); [TechPowerUp](https://www.techpowerup.com/346461/amd-instinct-mi455x-reportedly-facing-delays-only-low-volume-production-this-year)
- **NVIDIA timing rumor:** the Tom's Hardware headline also says NVIDIA's VR200 systems are "rumored to arrive early." [PRESS-UNNAMED]; body not retrieved — [Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/amd-denies-report-of-mi455x-delays-as-nvidia-vr200-systems-are-rumored-to-arrive-early-company-says-helios-systems-on-target-for-2h-2026)
- **HBM4 and N2:** I found no report attributing a delay specifically to HBM4 or TSMC N2. SemiAnalysis's quoted wording is "manufacturing delays." See Gaps.

### Inferences
- **The disputed milestones differ.** SemiAnalysis's claim concerns mass production and "production tokens" on the UALoE72 rack by Q2 2027. AMD's reported milestone is volume chip shipments and first racks in Q3 2026. Both can be true at once.
- **Customer schedules point to a 2027 volume ramp.** OpenAI expects Helios online from Q4 2026, accelerating through 2027. Anthropic's first GW starts in H1 2027, and HUMAIN's MI400 phase in 2027. None of this, by itself, shows a slip against AMD's "begin in Q3 2026" commitment.
- **MI500 claims keep escalating:** "1,000x" peak AI compute vs MI300X (CES, Jan 2026), then "more than 2,000x higher inference throughput in just 4 years" (AAI, Jul 2026). These are projections using different metrics, not measured milestones.

### Gaps
- Primary text for the Computex 2024 and Oct 2024 Advancing AI commitments was not retrieved, so I could not check the original MI325X shipping and "systems from Q1 2025" wording.
- I found no evidence on reported weak MI325X demand.
- Computex 2026 (June 2026): no AMD data-center press release was identified. The 21 May 2026 Taiwan releases (Venice ramp; $10B+ investments) are the nearest dated items.
- Q1 and Q2 2026 earnings-call transcripts were not retrievable (404), so management's verbal responses to the delay report on those calls are not captured.
- I found no reported HBM4- or N2-specific problems, and no NVIDIA VR200 timing details.

---

## 3. Financials (FY2024, FY2025, Q1–Q3 2026, Q4 2026 guidance), AI GPU revenue, MI308/China, cash/debt/buybacks, ZT/Sanmina, FAD targets and progress, warrant accounting

### Takeaway
- **Data Center has nearly doubled year on year:** $8.55B in Q3'26 vs $4.34B in Q3'25. AMD guides about $17B total revenue for Q4'26, with Data Center up about 50% quarter on quarter, and expects data-center AI revenue to exceed server-CPU revenue in Q4'26.
- **No Instinct revenue figure since 2024:** AMD disclosed "just above $5B" for 2024 and has disclosed no figure for 2025 or 2026.
- **MI308 charges:** about $800M in Q2'25 and about $440M net for FY2025.
- **Warrants:** the OpenAI and Meta warrants caused a $1.1B non-cash GAAP charge in Q3'26.
- **Balance sheet and deals:** debt rose to $7.1B after a $4.75B bond issue (Aug 2026), and AMD agreed two large acquisitions (Taalas, World Labs).

### Cited Findings

**Income statement (US$ millions)**

| Period | Revenue | GAAP GM | Non-GAAP GM | GAAP op. income | Non-GAAP op. income | Data Center revenue | Data Center op. income | Source / provenance |
|---|---|---|---|---|---|---|---|---|
| FY2024 (to 28 Dec 2024) | 25,785 | 49% | 53% | 1,900 | 6,138 | 12,579 | 3,482 | [CO] [AMD Q4/FY2025 release, 2026-02-03](https://ir.amd.com/news-events/press-releases/detail/1276/amd-reports-fourth-quarter-and-full-year-2025-financial) |
| FY2025 (to 27 Dec 2025) | 34,639 | 50% | 52% | 3,694 | 7,768 | 16,635 | 3,603 | [CO] same release |
| Q1'25 | 7,438 | 50% | 54% | n/c | n/c | 3,674 | 932 | [CO] [AMD Q1'26 release PDF, 2026-05-05](https://d1io3yog0oux5.cloudfront.net/_f017709bc11ca6ccc9a2fe1928b56a11/amd/news/2026-05-05_AMD_Reports_First_Quarter_2026_Financial_1284.pdf) |
| Q2'25 | 7,685 (sum of segments) | 40% | 43% | (134) | 897 | 3,240 | (155) | [CO-SEC] [AMD Q2'26 8-K Ex. 99.1, 2026-08-04](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000121/q22026991.htm) |
| Q3'25 | 9,246 | 52% | 54% | 1,270 | 2,238 | 4,341 | 1,074 | [CO-SEC] [AMD Q3'26 8-K Ex. 99.1, 2026-11-03](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000188/q32026991.htm) |
| Q4'25 | 10,270 | 54% | 57% | n/c | n/c | 5,380 | 1,752 | [CO] [AMD Q4/FY2025 release](https://ir.amd.com/news-events/press-releases/detail/1276/amd-reports-fourth-quarter-and-full-year-2025-financial) |
| Q1'26 (to 28 Mar 2026) | 10,253 (+38% y/y) | 53% | 55% | 1,476 | 2,540 | 5,775 (+57%) | 1,599 | [CO] [AMD Q1'26 release, 2026-05-05](https://ir.amd.com/news-events/press-releases/detail/1284/amd-reports-first-quarter-2026-financial-results) |
| Q2'26 (to 27 Jun 2026) | 11,536 (+50%) | 54% | 56% | 1,990 | 3,094 | 6,718 | 2,103 | [CO-SEC] [AMD Q2'26 8-K Ex. 99.1](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000121/q22026991.htm) |
| Q3'26 (to 26 Sep 2026) | 13,377 (+45%) | 54% | 56% | 2,832 | 3,923 | 8,546 (+97% y/y; +27% q/q) | 2,882 (34% margin) | [CO-SEC] [AMD Q3'26 8-K Ex. 99.1](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000188/q32026991.htm) |
| Q4'26 guidance (given 3 Nov 2026) | ~17,000 ±3% (~66% y/y, ~27% q/q) | n/g | ~55% | n/g | non-GAAP opex ~3,750 | ~+50% q/q | n/g | [CO] [Q3'26 8-K](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000188/q32026991.htm); [Q3'26 call](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/) |

(n/c = not captured in the retrieved text; n/g = not guided.)

**Net income and EPS**
- **FY2024:** GAAP net income $1,641M; non-GAAP $5,420M. GAAP diluted EPS $1.00; non-GAAP $3.31. [CO] — [AMD Q4/FY2025 release, 2026-02-03](https://ir.amd.com/news-events/press-releases/detail/1276/amd-reports-fourth-quarter-and-full-year-2025-financial)
- **FY2025:** GAAP net income $4,335M; non-GAAP $6,831M. GAAP EPS $2.65; non-GAAP $4.17. [CO] — same source.
- **Q1'26:** GAAP net income $1,383M; non-GAAP $2,265M. EPS $0.84 / $1.37. [CO] — [AMD Q1'26 release](https://ir.amd.com/news-events/press-releases/detail/1284/amd-reports-first-quarter-2026-financial-results)
- **Q2'26:** GAAP net income $2,297M; non-GAAP $2,760M. EPS $1.38 / $1.66. [CO-SEC] — [Q2'26 8-K Ex. 99.1](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000121/q22026991.htm)
- **Q3'26:** GAAP net income $2,428M; non-GAAP $3,471M. EPS $1.46 / $2.09. [CO-SEC] — [Q3'26 8-K Ex. 99.1](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000188/q32026991.htm)
- **Nine months 2026 Data Center:** revenue $21.0B, up 87% from $11.3B, "primarily driven by strong demand for our AMD EPYC processors and AMD Instinct GPUs." [CO-SEC] — [10-Q Q3'26](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm)
- **Guidance vs actuals (2026):**
  - Q1'26: guided about $9.8B ±$300M, including about $100M of MI308 sales to China, with non-GAAP GM about 55%. Actual: $10.253B.
  - Q2'26: guided $11.2B ±$300M at about 56%. Actual: $11.536B.
  - Q3'26: guided about $13B ±$300M at about 56%. Actual: $13.377B.
  - [CO] — [Q4/FY2025 release](https://ir.amd.com/news-events/press-releases/detail/1276/amd-reports-fourth-quarter-and-full-year-2025-financial); [Q1'26 release](https://ir.amd.com/news-events/press-releases/detail/1284/amd-reports-first-quarter-2026-financial-results); [Q2'26 8-K](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000121/q22026991.htm)

**AI GPU revenue disclosed or bounded**
- **2024:** Instinct GPU sales were "just above $5 billion," up from initial guidance of "more than $2 billion." Su also called the Instinct business worth "tens of billions of dollars of annual revenue over the coming years" (Q4'24 call, 4 Feb 2025). [CO] via press — [The Next Platform, 2025-02-05](https://www.nextplatform.com/compute/2025/02/05/amd-moves-up-instinct-mi355x-launch-as-datacenter-biz-hits-records/1646757)
- **Next Platform author estimates (Feb 2025):** Q4'24 Instinct revenue about $1.75B, and 2025 Instinct revenue about $8.44B (projection). [EST: Timothy Prickett Morgan, The Next Platform] — same source.
- **Q4'26 bound:** Jean Hu said Q4'26 will be "the quarter data center AI business surpassed server business." [CO] — [Q3'26 call](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/)
- **2027 outlook (Su, 3 Nov 2026):**
  - Data-center AI will "significantly more than double."
  - Server CPU revenue will about double.
  - Data Center will be more than 80% of revenue.
  - Total revenue growth will exceed 80%.
  - [CO] — same source.
- **OpenAI deal:** "expected to deliver tens of billions of dollars in revenue for AMD" and to be "highly accretive" to non-GAAP EPS (6 Oct 2025). [CO] — [AMD–OpenAI release, 2025-10-06](https://ir.amd.com/news-events/press-releases/detail/1260/amd-and-openai-announce-strategic-partnership-to-deploy-6-gigawatts-of-amd-gpus)
- **Meta deal:** expected to "drive substantial multi-year revenue growth and be accretive to our non-GAAP earnings per share" (Jean Hu, 24 Feb 2026). No dollar value given. [CO] — [AMD–Meta release, 2026-02-24](https://ir.amd.com/news-events/press-releases/detail/1279/amd-and-meta-announce-expanded-strategic-partnership-to-deploy-6-gigawatts-of-amd-gpus)

**MI308 export charges, reversals, China sales and the "15%" arrangement**
- **Q2'25 charge:** "$800M in inventory and related charges from the U.S. government's export control on MI308 GPUs." [CO-SEC] — [Q2'26 8-K Ex. 99.1 (prior-year comparison)](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000121/q22026991.htm)
- **Q4'25 and FY2025:**
  - Q4'25 included about $390M of MI308 sales to China and an inventory-reserve release of about $360M.
  - FY2025 net MI308-related inventory and related charges were about $440M.
  - [CO] — [AMD Q4/FY2025 release, 2026-02-03](https://ir.amd.com/news-events/press-releases/detail/1276/amd-reports-fourth-quarter-and-full-year-2025-financial)
- **Q1'26:** the guidance included about $100M of MI308 sales to China. Actual China revenue for 2026 is not disclosed in the sources reviewed. [CO] — same release.
- **The "15%":**
  - The 10-Q says: "In August 2025, U.S. government officials expressed an expectation that the U.S. government will receive 15% of the revenue generated from licensed MI308 sales to China. However, to date, the U.S. government has not published a regulation establishing such requirement."
  - AMD warns that such a request "could subject us to litigation, increase our costs."
  - [CO-SEC] — [10-Q Q3'26](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm)
- **Gross margin:** 9M 2026 GAAP gross margin was 54%, vs 47% in 9M 2025. The increase was "driven by the absence of inventory and related charges associated with the U.S. government export control on AMD Instinct MI308." [CO-SEC] — same 10-Q.
- **Q3'26:** the release and call contain no China or MI308 items. [CO] — [Q3'26 8-K Ex. 99.1](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000188/q32026991.htm); [Q3'26 call](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/)

**Cash, debt, free cash flow and buybacks**
- **Cash, cash equivalents and short-term investments:**
  - $10.55B at 27 Dec 2025 ($5,539M + $5,013M).
  - $12,347M at 28 Mar 2026.
  - $13,111M at 27 Jun 2026.
  - $15,776M at 26 Sep 2026.
  - [CO]/[CO-SEC] — [Q4/FY2025 release](https://ir.amd.com/news-events/press-releases/detail/1276/amd-reports-fourth-quarter-and-full-year-2025-financial); [Q1'26 release](https://ir.amd.com/news-events/press-releases/detail/1284/amd-reports-first-quarter-2026-financial-results); [Q2'26 8-K](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000121/q22026991.htm); [Q3'26 8-K](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000188/q32026991.htm)
- **Total debt (net):** $3,222M at 27 Dec 2025 and $7,079M at 26 Sep 2026 (principal $7,125M). [CO-SEC] — [10-Q Q3'26](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm)
- **New notes (17 Aug 2026):** $4.75B of senior notes:
  - $1.25B at 4.600% due 2029.
  - $1.5B at 5.000% due 2031.
  - $1.0B at 5.250% due 2033.
  - $1.0B at 5.500% due 2036.
  - [CO-SEC] — same 10-Q.
- **Repayment and facilities:**
  - The $875M 4.212% notes were repaid at maturity in Sep 2026.
  - A new 5-year, $5.0B revolving credit facility replaced the $3.0B facility (May 2026).
  - The commercial-paper limit rose to $5.5B (May 2026).
  - [CO-SEC] — same 10-Q.
- **Free cash flow:**
  - FY2024 $2,405M; FY2025 $5,519M.
  - Q1'26 $2,566M; Q2'26 $1,558M; Q3'26 $554M (4% margin, vs $1,530M in Q3'25).
  - 9M 2026 $4,678M.
  - [CO]/[CO-SEC] — [Q4/FY2025 release](https://ir.amd.com/news-events/press-releases/detail/1276/amd-reports-fourth-quarter-and-full-year-2025-financial); [Q1'26 release](https://ir.amd.com/news-events/press-releases/detail/1284/amd-reports-first-quarter-2026-financial-results); [Q2'26 8-K](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000121/q22026991.htm); [Q3'26 8-K](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000188/q32026991.htm)
- **Working-capital drivers (9M 2026):**
  - Inventory rose $3.5B "to support the continued ramp of Data Center products in advanced process technology nodes."
  - Prepaid expenses rose $2.1B, "primarily due to prepayments of supply agreements."
  - Inventory was $11,463M at 26 Sep 2026, vs $7,920M at 27 Dec 2025.
  - [CO-SEC] — [10-Q Q3'26](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm); [Q3'26 8-K](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000188/q32026991.htm)
- **Buybacks:**
  - FY2025: $1,316M.
  - 9M 2026: $221M (1.1M shares, all in Q1'26); none in Q2 or Q3'26.
  - Remaining authorization: $9.2B of $14B total.
  - Q3'26 share repurchases for employee tax withholding were $1,495M.
  - A $6B authorization was added on 14 May 2025 (release title).
  - [CO-SEC] — [10-Q Q3'26](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm); [Q3'26 8-K](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000188/q32026991.htm); [AMD IR release list, page 6](https://ir.amd.com/news-events/press-releases?page=6)

**Customer-warrant accounting (OpenAI and Meta)**
- **Accounting treatment:** the warrants count as "consideration payable to a customer." The grant-date fair value of warrant shares probable of vesting is recorded as a reduction of revenue as qualifying revenue is recognized. The liability is then remeasured each period, with fair-value changes recorded in other income (expense), until each tranche becomes exercisable. [CO-SEC] — [10-Q Q3'26](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm)
- **Position at 26 Sep 2026:**
  - Warrant liability of $1.2B.
  - A $1.2B non-cash charge for the three and nine months, mainly from remeasuring the liability.
  - $4.5B of unrecognized grant-date fair value still to be booked as contra-revenue.
  - Weighted-average grant-date fair value: $14.25 per share. Fair value at 26 Sep 2026: $178.58 per share, "primarily on its closing stock price as most market conditions had been met."
  - "No warrant shares had vested or become exercisable, or been exercised, forfeited or expired."
  - [CO-SEC] — same 10-Q.
- **Q3'26 detail:** the non-GAAP adjustment for the warrant fair-value change was $1,097M. The cash-flow statement shows a $1,179M "non-cash impact of warrants issued to customers, net." Hu said the fair-value adjustments "are expected to increase" as the agreements progress and do not affect non-GAAP results or free cash flow. [CO-SEC]/[CO] — [Q3'26 8-K](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000188/q32026991.htm); [Q3'26 call](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/)

**ZT Systems and Sanmina**
- **ZT purchase:** AMD bought ZT Systems for $4.9B, announced in 2024. [press] — [The Next Platform, 2026-02-23](https://www.nextplatform.com/compute/2026/02/23/amd-says-helios-racks-and-mi400-series-gpus-on-track-for-2h-2026/4092199)
- **Shares issued:** 8M AMD shares were issued "in the acquisition of ZT Systems" during 9M 2025. [CO-SEC] — [10-Q Q3'26](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm)
- **Sale of manufacturing to Sanmina:** agreement announced 19 May 2025 and completed 27 Oct 2025 (release titles). [CO] — [AMD IR release list, page 6](https://ir.amd.com/news-events/press-releases?page=6); [page 5](https://ir.amd.com/news-events/press-releases?page=5)
- **Sanmina sale terms (10-Q):**
  - $2.4B cash, subject to adjustments, plus 1,151,052 Sanmina shares.
  - At close AMD received $1.4B cash (net of cash divested and adjustments) and Sanmina shares valued at $154M.
  - AMD paid $243M in 2026 for working-capital adjustments.
  - An earn-out of up to $450M runs through 2028; a $348M receivable is recorded.
  - A 5-year Manufacturing Services Agreement was signed with Sanmina.
  - ZT's manufacturing results are reported as discontinued operations.
  - [CO-SEC] — same 10-Q.
- **Headline value:** Next Platform describes the sale as "$3 billion." [press] — [The Next Platform, 2026-02-23](https://www.nextplatform.com/compute/2026/02/23/amd-says-helios-racks-and-mi400-series-gpus-on-track-for-2h-2026/4092199)

**2026 acquisitions and investments (AI-related)**
- **MEXT:** acquired in Q2'26 for "AI memory technology." [CO-SEC] — [Q2'26 8-K](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000121/q22026991.htm)
- **Taalas:** definitive agreement in Aug 2026, cash and stock, about $2.9B including up to about $1.4B contingent. Taalas makes specialized inference silicon. [CO-SEC] — [10-Q Q3'26](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm)
- **World Labs:** definitive agreement in Sep 2026, all stock, about $8.2B; a model-research lab focused on spatial intelligence.
  - Both deals are expected to close by year-end 2026, subject to regulatory approvals.
  - The 10-Q ties them to "development of future super intelligence (SI) hardware, software and systems."
  - [CO-SEC] — same 10-Q.
- **Investments in customers:**
  - AMD "has committed to make a strategic equity investment of up to $5 billion in Anthropic in the future" (22 Jul 2026). [CO] — [AMD–Anthropic release](https://ir.amd.com/news-events/press-releases/detail/1292/amd-and-anthropic-announce-strategic-partnership-to-deploy-up-to-2-gigawatts-of-amd-instinct-mi450-series-gpus)
  - AMD "will invest $1 billion in Meta's equity offering" (27 Oct 2026). [CO] — [AMD–Meta release, 2026-10-27](https://ir.amd.com/news-events/press-releases/detail/1302/amd-and-meta-advance-strategic-partnership-to-power-metas-superintelligence-infrastructure)
- **Country investments:** more than $10B in the Taiwan ecosystem (21 May 2026) and up to £2B in the UK (8 Jun 2026, release title). [CO] — [Taiwan release](https://ir.amd.com/news-events/press-releases/detail/1286/amd-announces-more-than-10-billion-in-taiwan-ecosystem-investments-to-accelerate-ai-infrastructure); [AMD IR release list, page 2](https://ir.amd.com/news-events/press-releases?page=2)

**Financial Analyst Day targets (11 Nov 2025) and progress**
- **Targets for the next 3–5 years:**
  - Revenue CAGR "greater than 35%."
  - Non-GAAP operating margin above 35%.
  - Non-GAAP EPS "exceeding $20."
  - Data-center revenue CAGR above 60%.
  - Data-center AI revenue CAGR above 80%.
  - Embedded plus client and gaming CAGR above 10%.
  - Market share: server CPU above 50%, client above 40%, adaptive above 70%.
  - The release gives no gross-margin or free-cash-flow targets.
  - [CO] — [AMD FAD release, 2025-11-11](https://ir.amd.com/news-events/press-releases/detail/1266/amd-unveils-strategy-to-lead-the-1-trillion-compute-market-and-accelerate-next-phase-of-growth)
- **"Tens of billions" of data-center AI revenue in 2027:** this phrase from the research brief does **not** appear in the FAD press release. The FAD presentation and transcript were not retrieved; see Gaps. [n/a]

### Inferences
These are my calculations from the figures above.
- **2026 revenue:** if Q4'26 lands at the $17.0B midpoint, FY2026 revenue would be about $52.2B, about +51% on FY2025. That is above the FAD's ">35% CAGR" pace in year one.
- **2026 Data Center revenue:** about $33.9B ($21.04B for 9M plus about $12.8B for Q4 at +50% q/q), roughly +104% on FY2025.
- **Q4'26 data-center AI floor:** if data-center AI exceeds server revenue in Q4'26, and the two make up most of a roughly $12.8B segment, data-center AI would be above roughly $6B in that quarter. This is a loose bound, because the segment also includes DPUs, NICs and FPGAs.
- **Non-GAAP operating margin trend:** 24.8% (Q1'26), 26.8% (Q2'26) and 29.3% (Q3'26), still below the >35% FAD target. Q4 guidance implies about 33% (55% × $17.0B − $3.75B opex), before other items.
- **Margin effect of MI308 items:**
  - Excluding the ~$360M reserve release, Q4'25 non-GAAP gross margin would be about 3.5 points lower (about 53.5%).
  - Excluding the ~$800M charge, Q2'25 non-GAAP gross margin would be about 10 points higher.
  - The FY2025 net ~$440M equals the $800M charge less the $360M release.
- **Warrant contra-revenue to date:** the gap between $1,179M (total non-cash warrant impact) and $1,097M (fair-value change) is $82M. That may be the contra-revenue recognized so far, which is consistent with about $4.5B still unrecognized out of about $4.56B total grant-date value (320M × $14.25). This is unconfirmed.
- **Warrants and the stock price:** the 10-Q says "most market conditions had been met" as of 26 Sep 2026. That implies AMD's share price had cleared many of the warrants' price hurdles, though the hurdle schedule itself is redacted (§4).

### Gaps
- AMD's Instinct or data-center-AI revenue for 2025 and for any 2026 quarter was not disclosed in the sources reviewed.
- The FAD "tens of billions in 2027" statement could not be verified; the FAD transcript and slides were not retrieved.
- Actual MI308 and MI325 China revenue in 2026 is not disclosed. I found no evidence that any 15% payment was made.
- The ZT Systems close date (reportedly 31 Mar 2025) was not verified this session.
- The status of the Anthropic investment (not reflected in the 10-Q as of 26 Sep 2026) and of the $1B Meta investment is unknown.

---

## 4. Customers and contracts: terms, binding status, vesting, concentration

### Takeaway
- **Binding volume per SEC filings:** 2 GW in total, the initial 1 GW each from OpenAI (MI450) and Meta. The rest of their 6 GW each, and all of Anthropic's "up to 2 GW," is non-binding or unstated.
- **Warrants:** each of OpenAI and Meta holds a warrant for up to 160M AMD shares at $0.01. No tranche had vested as of 26 Sep 2026.
- **Other named customers:** Microsoft, Oracle, HUMAIN, DOE/ORNL, EuroHPC, TensorWave, Vultr, Cirrascale, TCS, Cerebras and others.
- **Concentration:** AMD discloses dependence on "a small number of customers" but no revenue percentages.

### Cited Findings

**OpenAI**
- **Deal (6 Oct 2025):**
  - Multi-year, multi-generation agreement for 6 GW, starting with MI450 and rack-scale systems.
  - The first 1 GW "set to begin in the second half of 2026."
  - [CO] — [AMD–OpenAI release, 2025-10-06](https://ir.amd.com/news-events/press-releases/detail/1260/amd-and-openai-announce-strategic-partnership-to-deploy-6-gigawatts-of-amd-gpus)
- **8-K binding commitment:** OpenAI "agreed to a binding commitment to purchase … the initial one (1) gigawatt of AMD Instinct MI450 Series GPU products." [CO-SEC] — [AMD 8-K, 2025-10-06 (event date 2025-10-05)](https://ir.amd.com/financial-information/sec-filings/content/0001193125-25-230895/0001193125-25-230895.pdf)
- **Warrant terms (8-K):**
  - Up to 160M shares at $0.01, issued to OpenAI OpCo, LLC on 5 Oct 2025.
  - The first tranche vests "after the delivery of the initial one (1) gigawatt"; full vesting needs 6 GW of purchases.
  - Vesting also depends on "specified Company stock price targets that escalate to $600 per share for the final tranche and stock performance thresholds."
  - Exercise requires "certain other technical and commercial conditions."
  - Expires 5:00 p.m. ET on 5 Oct 2030; cash or cashless exercise.
  - Transfer only to affiliates, with limited exceptions; demand and piggyback registration rights.
  - The vesting schedule (Exhibit E) and exercise conditions (Exhibit F) are redacted ("[****]").
  - Unvested shares are cancelled if AMD terminates the supply agreement early for cause.
  - Share issuance may await Hart-Scott-Rodino or other antitrust approvals.
  - [CO-SEC] — same 8-K.
- **Status:**
  - Per AMD (3 Nov 2026), OpenAI is running models and workloads on its first Helios racks. [CO] — [Q3'26 8-K](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000188/q32026991.htm)
  - OpenAI expects Helios online "beginning in the fourth quarter of 2026." [CO+CUST] — [AAI 2026 release](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era)
  - No warrant shares had vested by 26 Sep 2026. [CO-SEC] — [10-Q Q3'26](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm)
- **OpenAI's statement on stage (Jul 2026):** Sachin Katti said: "We were first to bet on AMD, and we are really thrilled with how that bet is turning out for us." [CO+CUST] via press — [iTWire, 2026-07-24](https://itwire.com/business-it-news/data/astounding-massive-dominant-ai-innovation-amd-launches-helios-against-nvidia-tips-up-to-us-5-billion-into-anthropic-and-books-roughly-14-gigawatts-of-customer-ai-compute-at-advanci)

**Meta (confirms the "early-2026 multi-GW deal with a warrant" lead)**
- **Deal (24 Feb 2026):**
  - Up to 6 GW of Instinct GPUs across generations.
  - The first GW uses a custom MI450-based GPU on Helios, with shipments to begin in 2H 2026.
  - Meta is lead customer for EPYC "Venice" and "Verano."
  - [CO+CUST] — [AMD–Meta release, 2026-02-24](https://ir.amd.com/news-events/press-releases/detail/1279/amd-and-meta-announce-expanded-strategic-partnership-to-deploy-6-gigawatts-of-amd-gpus)
- **8-K terms (dated 23 Feb 2026):**
  - Amends the Master Purchase Agreement of 23 May 2023.
  - "binding commitment to purchase the initial one (1) gigawatt equivalent."
  - Warrant for up to 160M shares at $0.01, exercisable until 23 Feb 2031.
  - The first tranche vests on shipment of the initial 1 GW equivalent; full vesting needs 6 GW.
  - Price thresholds "escalate to $600 per share for the final tranche," plus technical and commercial conditions.
  - Transfer only to controlled affiliates without AMD's consent; registration rights.
  - [CO-SEC] — [AMD 8-K, 2026-02-23](https://www.sec.gov/Archives/edgar/data/2488/000000248826000045/amd-20260223.htm)
- **10-Q description of both warrants:** some tranches use "stock price performance relative to a market index"; each warrant expires five years after issue and cannot be settled in cash. [CO-SEC] — [10-Q Q3'26](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm)
- **Deal value and context (CNBC, 24 Feb 2026):**
  - Terms were not disclosed. Analyst Ben Bajarin estimated the deal at "tens of billions of dollars" over at least four years. [EST: Bajarin, via CNBC]
  - AMD shares rose about 7% that day. [press]
  - Meta had committed to "millions" of NVIDIA processors one week earlier. [press]
  - [CNBC, Katie Tarasov, 2026-02-24](https://www.cnbc.com/2026/02/24/meta-to-use-6gw-of-amd-gpus-days-after-expanded-nvidia-ai-chip-deal.html)
- **Other valuations seen:** Jon Peddie headlined "$60B"; Introl claimed over $100B. [SECONDARY]; not verified — [Jon Peddie Research](https://www.jonpeddie.com/news/amd-and-meta-announce-60b-6-gw-ai-partnership/); [Introl](https://introl.com/blog/meta-amd-100-billion-gpu-deal-nvidia-exclusivity)
- **Update (27 Oct 2026):**
  - Helios "installed and being tested by Meta."
  - Instinct GPUs are "in production at Meta for training, ranking and recommendation."
  - Meta is an "early definition customer" for MI450.
  - Meta and AMD are collaborating on MI500 and "Verano."
  - AMD will invest $1B in Meta's equity offering.
  - No new gigawatt figure or warrant change.
  - [CO+CUST] — [AMD–Meta release, 2026-10-27](https://ir.amd.com/news-events/press-releases/detail/1302/amd-and-meta-advance-strategic-partnership-to-power-metas-superintelligence-infrastructure)

**Anthropic**
- **Deal (22 Jul 2026):**
  - "Up to 2 gigawatts" of MI450-series (MI455X) GPUs in Helios, with the first GW starting in H1 2027.
  - AMD "has committed to make a strategic equity investment of up to $5 billion in Anthropic in the future." No structure is given.
  - No warrant is mentioned, and the release does not say whether purchases are binding.
  - Engineering collaboration uses Claude for ROCm and workload optimization, and AMD will adopt Claude internally.
  - [CO] — [AMD–Anthropic release, 2026-07-22](https://ir.amd.com/news-events/press-releases/detail/1292/amd-and-anthropic-announce-strategic-partnership-to-deploy-up-to-2-gigawatts-of-amd-instinct-mi450-series-gpus)
- **Q3'26 call:** Anthropic is among customers with first Helios racks online. Per Su, one Anthropic engineer "used Claude to bring up their latest model on Instinct MI355X racks" over a weekend. [CO] — [Q3'26 call](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/)

**Microsoft**
- **Earlier use (Jun 2025):** MI300X powered models in production on Azure. [CO+CUST] — [AMD Advancing AI 2025 release](https://ir.amd.com/news-events/press-releases/detail/1255/amd-unveils-vision-for-an-open-ai-ecosystem-detailing-new-silicon-software-and-systems-at-advancing-ai-2025)
- **Expanded deal (20 Jul 2026):**
  - Azure will deploy Helios (MI455X plus Venice) mainly for frontier-model inference.
  - Shipping begins in 2H 2026.
  - New Venice VM series: HDv2 and HXv2.
  - Broader use of Pensando DPUs.
  - No GW, MW or unit figures.
  - [CO+CUST] — [AMD–Microsoft release, 2026-07-20](https://ir.amd.com/news-events/press-releases/detail/1291/microsoft-to-deploy-next-gen-amd-instinct-and-amd-epyc-processors-as-the-companies-expand-their-long-term-strategic-partnership)

**Oracle (OCI)**
- **MI355X:** OCI plans zettascale clusters of "up to 131,072 MI355X GPUs" (Jun 2025). By 11 Nov 2025, MI350 was "deployed at scale" including at OCI. [CO+CUST]/[CO] — [AMD Advancing AI 2025 release](https://ir.amd.com/news-events/press-releases/detail/1255/amd-unveils-vision-for-an-open-ai-ecosystem-detailing-new-silicon-software-and-systems-at-advancing-ai-2025); [AMD FAD release](https://ir.amd.com/news-events/press-releases/detail/1266/amd-unveils-strategy-to-lead-the-1-trillion-compute-market-and-accelerate-next-phase-of-growth)
- **Helios and Venice:** OCI is running workloads on the first Helios systems, and its OCI Compute E7 instances use Venice (3 Nov 2026). [CO] — [Q3'26 8-K](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000188/q32026991.htm)
- **50,000 MI450 from Q3 2026 (announced 14 Oct 2025): not verified.** Oracle's release returned 403, and the AMD releases reviewed do not state the 50,000 figure. See Gaps.

**DOE / ORNL**
- **Announcement (27 Oct 2025):**
  - **Lux:** MI355X, EPYC and Pensando, built with ORNL, OCI and HPE; deployment "early 2026."
  - **Discovery:** MI430X plus Venice on HPE Cray GX5000; delivery 2028, user operations 2029.
  - Combined "$1 billion in private and public funding."
  - Discovery was procured competitively; Lux follows a new partnership model.
  - [CO+CUST] — [AMD–DOE release, 2025-10-27](https://ir.amd.com/news-events/press-releases/detail/1264/amd-powers-u-s-sovereign-ai-factory-supercomputers-accelerating-an-open-american-ai-stack)

**HUMAIN (Saudi Arabia, a PIF company)**
- **Collaboration:** a $10B collaboration (13 May 2025, release title). [CO] — [AMD IR release list, page 6](https://ir.amd.com/news-events/press-releases?page=6)
- **JV:** AMD, Cisco and HUMAIN plan a joint venture to deliver 1 GW of AI infrastructure by 2030 (Q4'25 highlight). [CO] — [AMD Q4/FY2025 release](https://ir.amd.com/news-events/press-releases/detail/1276/amd-reports-fourth-quarter-and-full-year-2025-financial)
- **Go-live (31 Aug 2026):**
  - MI355X systems are live with Cisco networking, offered as GPU-as-a-service. No GPU count is given.
  - The next phase is up to 250 MW of MI400, deploying from 2027.
  - [CO+CUST] — [AMD/Cisco/HUMAIN release, 2026-08-31](https://ir.amd.com/news-events/press-releases/detail/1298/amd-cisco-and-humain-expand-saudi-arabias-ai-infrastructure-as-amd-instinct-systems-go-live)

**Other customers and partners named in 2025–2026** (all [CO] or [CO+CUST])
- **Named as "choosing Helios" (AAI 2026):** TensorWave, Vultr and Cirrascale. Partners named at the same event: Cerebras (a combined low-latency inference offering), AT&T and Cisco. — [AAI 2026 release](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era); [Q2'26 8-K](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000121/q22026991.htm)
- **Vultr:** HPE says Vultr gets the first "Helios by HPE." — [Q3'26 8-K](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000188/q32026991.htm)
- **TCS:** Helios-based infrastructure for India (16 Feb 2026); an earlier strategic collaboration on 14 Jan 2026. — [AMD Q1'26 release](https://ir.amd.com/news-events/press-releases/detail/1284/amd-reports-first-quarter-2026-financial-results); [AMD IR release list, pages 3–4](https://ir.amd.com/news-events/press-releases?page=4)
- **Korea:** NAVER Cloud and Upstage. — [AMD Q1'26 release](https://ir.amd.com/news-events/press-releases/detail/1284/amd-reports-first-quarter-2026-financial-results)
- **EuroHPC LUMI-AI:** MI430X plus Venice, online 2H 2027. — [Q3'26 call](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/)
- **HPE "Herder" and Eviden "Alice Recoque":** both MI430X. — [Q4/FY2025 release](https://ir.amd.com/news-events/press-releases/detail/1276/amd-reports-fourth-quarter-and-full-year-2025-financial); [CES 2026 release](https://ir.amd.com/news-events/press-releases/detail/1272/amd-and-its-partners-share-their-vision-for-ai-everywhere-for-everyone-at-ces-2026)
- **Zyphra:** see §1. — [AMD Zyphra release](https://ir.amd.com/news-events/press-releases/detail/1268/amd-powers-frontier-ai-training-for-zyphra)
- **Cohere:** expanded collaboration (24 Sep 2025, title); Command models on MI300X (Jun 2025). — [AMD IR release list, page 5](https://ir.amd.com/news-events/press-releases?page=5); [AMD Advancing AI 2025 release](https://ir.amd.com/news-events/press-releases/detail/1255/amd-unveils-vision-for-an-open-ai-ecosystem-detailing-new-silicon-software-and-systems-at-advancing-ai-2025)
- **xAI:** named among Advancing AI 2025 participants. The body text mentions only "Grok" as a developer-cloud collaborator; no xAI–AMD deal was found. — [AMD Advancing AI 2025 release](https://ir.amd.com/news-events/press-releases/detail/1255/amd-unveils-vision-for-an-open-ai-ecosystem-detailing-new-silicon-software-and-systems-at-advancing-ai-2025)

**The "14 GW" headline vs binding volume**
- iTWire's headline says AMD "books roughly 14 gigawatts of customer AI compute": OpenAI 6, Meta up to 6 and Anthropic up to 2. The article itself calls the Meta and Anthropic figures ceilings. [press] — [iTWire, 2026-07-24](https://itwire.com/business-it-news/data/astounding-massive-dominant-ai-innovation-amd-launches-helios-against-nvidia-tips-up-to-us-5-billion-into-anthropic-and-books-roughly-14-gigawatts-of-customer-ai-compute-at-advanci)

**Customer concentration and contract terms**
- **Risk factor:** AMD says it "depend[s] on a small number of customers for a substantial portion of our business." No customer revenue percentage appears in the FY2025 10-K or Q3'26 10-Q text reviewed. [CO-SEC] — [10-K FY2025, filed 2026-02-04](https://www.sec.gov/Archives/edgar/data/2488/000000248826000018/amd-20251227.htm); [10-Q Q3'26](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm)
- **Receivables:** one customer was about 11% of accounts receivable at 27 Dec 2025, and another was 24% at 28 Dec 2024. [CO-SEC] — [10-K FY2025](https://www.sec.gov/Archives/edgar/data/2488/000000248826000018/amd-20251227.htm)
- **Order terms:** AMD sells mainly on purchase orders and "generally do[es] not have long-term supply arrangements with our customers or minimum purchase requirements." Customers can generally cancel standard orders more than 30 days before shipment. [CO-SEC] — [10-Q Q3'26](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm)

### Inferences
- The SEC-filed binding volume is 2 GW (OpenAI's 1 GW of MI450 plus Meta's 1 GW-equivalent). Everything above that is conditional ("up to") or tied to milestones.
- The boilerplate that AMD generally lacks minimum-purchase contracts sits alongside these specific 1 GW binding commitments. The large GPU deals are the exception.
- AMD is now an investor in two Helios customers: up to $5B in Anthropic (future) and $1B in Meta's offering. On top of that it has granted warrants to two customers worth up to 320M shares. Supplier-financed or equity-linked demand is now a material part of the contract base.

### Gaps
- Oracle's 50,000-MI450 commitment and timing.
- Status of the Crusoe deal.
- Any xAI agreement.
- TensorWave and Vultr volumes.
- DOE Lux go-live.
- The terms of the Microsoft Helios deployment (scale).
- Revenue concentration by customer.

---

## 5. Capacity: TSMC nodes and packaging, HBM suppliers, rack manufacturing partners

### Takeaway
- **Foundry:** TSMC makes all of AMD's GPU wafers at 7 nm and below. The MI455X uses TSMC 2 nm plus 3 nm chiplets, and Venice is ramping on 2 nm.
- **HBM4:** Samsung is the only HBM4 supplier AMD has publicly named, for the MI455X.
- **Rack partners:** Sanmina, Wiwynn, Wistron and Inventec build Helios systems as ODMs; HPE, Dell, Lenovo, Supermicro and Bull ship them as OEMs.
- **Supply vs demand:** AMD says demand exceeds supply, that it has secured 2027 supply, and that memory is in industry-wide shortage.
- **Not found:** CoWoS allocation figures and other HBM suppliers.

### Cited Findings
- **Foundry dependence:** "We rely on Taiwan Semiconductor Manufacturing Company Limited (TSMC) for the production of all wafers for microprocessor and GPU products at 7 nanometer (nm) or smaller nodes." [CO-SEC] — [10-Q Q3'26](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm)
- **MI455X nodes:** TSMC 2 nm and 3 nm, 12 chiplets, 320B transistors (AAI 2026). [CO] via press — [iTWire, 2026-07-24](https://itwire.com/business-it-news/data/astounding-massive-dominant-ai-innovation-amd-launches-helios-against-nvidia-tips-up-to-us-5-billion-into-anthropic-and-books-roughly-14-gigawatts-of-customer-ai-compute-at-advanci)
- **MI500:** 2 nm and HBM4E. [CO] — [AMD CES 2026 release](https://ir.amd.com/news-events/press-releases/detail/1272/amd-and-its-partners-share-their-vision-for-ai-everywhere-for-everyone-at-ces-2026)
- **Venice:** production ramp on TSMC 2 nm (21 May 2026, release title). [CO] — [AMD release 1287](https://ir.amd.com/news-events/press-releases/detail/1287/amd-announces-production-ramp-of-next-generation-amd-epyc-processor-venice-on-tsmc-2nm-process-technology)
- **HBM4:** AMD is "collaborating on HBM4 supply for MI455X GPUs" with Samsung (Q1'26 highlight). [CO] — [AMD Q1'26 release, 2026-05-05](https://ir.amd.com/news-events/press-releases/detail/1284/amd-reports-first-quarter-2026-financial-results)
- **Packaging and substrates (21 May 2026 release):**
  - Over $10B of Taiwan ecosystem investments, not broken down.
  - With ASE and SPIL, AMD is developing and qualifying a 2.5D wafer-based bridge interconnect ("EFB") for Venice.
  - With PTI, it qualified a "2.5D panel-based EFB interconnect."
  - Substrate suppliers: Unimicron, Nan Ya PCB and Kinsus.
  - No TSMC CoWoS/SoIC figures and no HBM supplier are named.
  - [CO] — [AMD Taiwan investments release, 2026-05-21](https://ir.amd.com/news-events/press-releases/detail/1286/amd-announces-more-than-10-billion-in-taiwan-ecosystem-investments-to-accelerate-ai-infrastructure)
- **Rack partners:**
  - ODMs "helping build Helios-based systems": Sanmina, Wiwynn, Wistron and Inventec. AIC handles Helios mechanical design (May 2026). [CO] — same release.
  - OEM systems from Bull, HPE, Lenovo and Supermicro; Sanmina and Wiwynn are infrastructure partners (Jul 2026). [CO] — [AAI 2026 release](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era)
  - HPE, Dell, Lenovo, Supermicro and others begin shipping Helios in Q4'26. [CO] — [Q3'26 call](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/)
  - Sanmina holds a 5-year Manufacturing Services Agreement with AMD. [CO-SEC] — [10-Q Q3'26](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm)
  - Next Platform infers Sanmina is Helios's initial NPI partner. [EST: The Next Platform] — [The Next Platform, 2026-02-23](https://www.nextplatform.com/compute/2026/02/23/amd-says-helios-racks-and-mi400-series-gpus-on-track-for-2h-2026/4092199)
- **Supply statements (Su, 3 Nov 2026):**
  - "It is true that demand is higher than supply."
  - AMD has secured wafers, substrates, advanced packaging, memory and other components for 2027.
  - Component costs face "inflationary pressures," which AMD is sharing with customers.
  - [CO] — [Q3'26 call](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/)
- **Risk disclosures (10-Q):**
  - "There is currently an industry-wide memory shortage… The price of memory has also increased."
  - Helios racks include networking, memory, power, cooling and mechanical parts AMD does not supply, and shortages of these could delay deployments.
  - Supply-agreement prepayments raised prepaid assets by $2.1B in 9M 2026.
  - [CO-SEC] — [10-Q Q3'26](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm)
- **Historical view (Feb 2025):** HBM and CoWoS supply was the main constraint on Instinct growth. [EST: The Next Platform] — [The Next Platform, 2025-02-05](https://www.nextplatform.com/compute/2025/02/05/amd-moves-up-instinct-mi355x-launch-as-datacenter-biz-hits-records/1646757)

### Inferences
- **Advanced-node exposure:** MI455X compute dies and Venice are both on TSMC N2, and TSMC is the sole source at 7 nm and below. AMD's AI ramp therefore depends on one foundry's N2 and advanced-packaging capacity, plus HBM4 availability.
- **Supply build:** the $2.1B of supply prepayments and $3.5B inventory build in 9M 2026 point to capacity being secured ahead of the Q4'26–2027 ramp. This fits Su's statement about 2027 supply.

### Gaps
- TSMC CoWoS, CoWoS-L or SoIC allocation for AMD (no figures found).
- Whether SK hynix or Micron supply HBM4 for MI455X, and HBM4 qualification status.
- Celestica's role (not found).
- Who packages MI455X (TSMC CoWoS vs other).
- Per-rack ODM volumes.

---

## 6. Ownership and key people

### Takeaway
- **Largest holders:** Vanguard (8.8%) and BlackRock (7.7%) as of 19 Mar 2026. Insiders together hold less than 1%.
- **Potential new large holders:** the OpenAI and Meta warrants could each deliver up to 160M shares, about 8.9% each post-issuance against 1,640M shares outstanding. No tranche had vested as of 26 Sep 2026.
- **Leadership:** Lisa Su (Chair, President and CEO) and Jean Hu (CFO) lead the company. Data-center figures cited here include Forrest Norrod, Doug Huang and Anush Elangovan; Fei-Fei Li is due to join as Chief Scientist.

### Cited Findings
- **Principal holders (as of 19 Mar 2026):**
  - The Vanguard Group: 142,442,745 shares (8.8%).
  - BlackRock: 124,945,206 (7.7%).
  - Lisa Su: 4,305,973; Mark Papermaster: 1,834,807; Forrest Norrod: 424,965; Jean Hu: 148,364; Darren Grasby: 184,596.
  - All 16 directors and executive officers as a group: 8,107,566 shares (under 1%).
  - [CO-SEC] — [AMD 2026 Proxy Statement (DEF 14A), filed 2026-03-27](https://www.sec.gov/Archives/edgar/data/2488/000119312526129057/d85856ddef14a.htm)
- **Named Executive Officers in the 2026 proxy:** Su, Hu, Grasby, Norrod and Papermaster. Ava Hahn is SVP, General Counsel and Corporate Secretary. [CO-SEC] — same proxy.
- **Shares outstanding:** 1,640M at 26 Sep 2026, up from 1,630M at the start of FY2026. [CO-SEC] — [10-Q Q3'26](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm)
- **Q4'26 diluted share count:** guided at about 1.67B, including the Taalas and World Labs acquisitions. Customer warrants are not expected to affect it. [CO] — [Q3'26 call](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/)
- **Signatories of the FY2025 10-K (3 Feb 2026):**
  - Lisa T. Su: "President and Chief Executive Officer…, Director." AMD releases style her "Chair and CEO."
  - Jean Hu: "Executive Vice President, Chief Financial Officer and Treasurer."
  - Emily Ellis: Corporate Vice President and Chief Accounting Officer.
  - Directors: Nora M. Denzel (Lead Independent Director), Mike P. Gregoire, Joe A. Householder, John W. Marren, KC McClure, Jon A. Olson, Abhi Y. Talwalkar and Beth W. Vanderslice.
  - [CO-SEC] — [AMD 10-K FY2025](https://www.sec.gov/Archives/edgar/data/2488/000000248826000018/amd-20251227.htm)
- **2026 board and executive changes:**
  - KC McClure appointed to the board (20 Jan 2026).
  - Tim Ryan appointed to the board (19 Aug 2026).
  - Ariel Kelman hired as Chief Marketing Officer (9 Feb 2026).
  - Alan Smith named Corporate Fellow (16 Jul 2026).
  - [CO] (release titles) — [AMD IR release list](https://ir.amd.com/news-events/press-releases); [page 2](https://ir.amd.com/news-events/press-releases?page=2); [page 3](https://ir.amd.com/news-events/press-releases?page=3); [page 4](https://ir.amd.com/news-events/press-releases?page=4)
- **Data-center figures:**
  - Forrest Norrod: "general manager of AMD's Data Center Solutions group." [press]
  - Doug Huang: ZT Systems co-founder, now "senior vice president of Data Center Platform Engineering." [press]
  - [The Next Platform, 2026-02-23](https://www.nextplatform.com/compute/2026/02/23/amd-says-helios-racks-and-mi400-series-gpus-on-track-for-2h-2026/4092199)
- **Anush Elangovan:** identified as AMD's VP of software development in coverage of the delay-report rebuttal. [SECONDARY] — [HotHardware](https://hothardware.com/news/amd-naysays-mi400-delay)
- **Fei-Fei Li:** "Fei-Fei will join AMD as Chief Scientist," leading model research, once the World Labs deal closes (expected by year-end 2026). [CO] — [Q3'26 call](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/)
- **Market value context:** AMD was valued at about $320B on 24 Feb 2026. [press] — [CNBC, 2026-02-24](https://www.cnbc.com/2026/02/24/meta-to-use-6gw-of-amd-gpus-days-after-expanded-nvidia-ai-chip-deal.html)

### Inferences
These are my calculations against 1,640M shares outstanding at 26 Sep 2026.
- **One warrant fully vested and exercised:** 160M shares would be about 9.8% of today's count, or about 8.9% of the enlarged count. That would be comparable to Vanguard's 8.8% as of Mar 2026.
- **Both warrants fully vested:** 320M shares would be about 16.3% of the enlarged count.
- **Price-target caveat:** full vesting also needs a $600 share price for the final tranche, plus 6 GW of purchases per customer.

### Gaps
- Vamsi Boppana's current title and role (not found in the filings or releases retrieved).
- Mark Papermaster's and Darren Grasby's current titles (not captured in the retrieved text).
- An up-to-date list of 13F holders after Mar 2026.
- Tim Ryan's background.

---

## 7. Legal and regulatory: export controls and China, litigation, antitrust, new in 2026

### Takeaway
- **Export controls:** these set AMD's China access. MI308 needs licenses; some were granted, and shipments began at the end of FY2025.
- **The 15% expectation:** US officials floated a 15% revenue share in Aug 2025, but no regulation has been published.
- **MI325 to China:** licensed in H1 2026, with mandatory US inspection that triggers a 25% tariff.
- **Litigation:** AMD reported no material legal proceedings in Q3'26.
- **Pending regulatory items:** approvals for the Taalas and World Labs deals, and possible antitrust (HSR) filings when warrants are exercised.

### Cited Findings
- **MI308 licensing:**
  - "In April 2025, the U.S. government implemented a new license requirement for the export of certain semiconductor products to a D5 Country… This restriction impacts our AMD Instinct™ MI308 products."
  - AMD "applied for and were granted some licenses… and we began shipping products at the end of fiscal 2025."
  - Sales "depend on customer demand, China's import control rules and our ability to obtain licenses."
  - [CO-SEC] — [10-Q Q3'26](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm)
- **MI325 licensing:** "During the first half of 2026, the U.S. government granted us some export licenses authorizing us to ship our AMD Instinct MI325 products to certain China-based customers… required… to first undergo an inspection process in the United States… [and] will be subject to a 25% tariff upon importation into the United States for the inspection." [CO-SEC] — same 10-Q.
- **The 15% revenue share:** officials expressed the expectation in Aug 2025, and no regulation has been published "to date" (10-Q filed 4 Nov 2026). [CO-SEC] — same 10-Q.
- **AI Diffusion Rule:** issued Jan 2025 and rescinded in May 2025, with replacement rules pending. [CO-SEC] — same 10-Q.
- **THATIC:** AMD holds equity in the THATIC joint ventures with a Chinese entity, some of which were added to the Entity List in Jun 2019. Also cited: Treasury's outbound-investment rules as a constraint. [CO-SEC] — same 10-Q.
- **Litigation:**
  - "During the quarter ended September 26, 2026, there were no material legal proceedings."
  - Risk factors mention past "claims concerning federal securities laws and corporate governance" and IP suits "from time to time."
  - Q3'26 non-GAAP reconciliation includes a $7M "loss contingency on legal matters."
  - [CO-SEC] — [10-Q Q3'26](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm); [Q3'26 8-K](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000188/q32026991.htm)
- **Antitrust and regulatory:**
  - Warrant shares are delivered after any required Hart-Scott-Rodino or other antitrust approval, and the parties must cooperate on filings. [CO-SEC] — [AMD 8-K (OpenAI warrant), 2025-10-06](https://ir.amd.com/financial-information/sec-filings/content/0001193125-25-230895/0001193125-25-230895.pdf)
  - The Taalas and World Labs acquisitions are "subject to regulatory approvals." [CO-SEC] — [10-Q Q3'26](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm)

### Inferences
- AMD's China channel for AI GPUs in 2026 runs through licensed older parts (MI308, MI325) under extra costs: the 25% tariff on inspected MI325, and an unlegislated 15% expectation on MI308. MI355X and MI400 are not described as licensed for China in any source reviewed.

### Gaps
- The Federal Register or BIS documents behind the MI325 inspection and tariff regime were not retrieved.
- Patent suits naming AMD in 2025–2026, including any suit over hybrid-bonding or 3D-stacking patents: none were verified this session. The 10-Q says no material proceedings.
- Securities class actions in 2026: none found.
- Any antitrust investigation of AMD's warrants or customer investments: none found.
- 2026 MI308 and MI325 China revenue.

---

## 8. Science and engineering: what is demonstrated, who verified it, what is unproven, which limits apply, and how solid the ground is

### Takeaway
- **Demonstrated, with independent corroboration:**
  - MI300X and MI355X serve production inference for large customers.
  - On the workloads AMD chose to submit, the MI355X lands roughly at parity with NVIDIA B200 in MLPerf Inference 6.0, and partner submissions reproduce AMD's numbers within about 4%.
- **Contested:** SemiAnalysis's independent testing (Feb and Aug 2026) shows AMD competitive on single-node FP8 serving but behind once distributed-inference optimizations are combined, with software maturity the main gap.
- **Unproven as of 14 Nov 2026:**
  - MI455X/Helios performance claims, including those against Vera Rubin, which are AMD projections.
  - Gigawatt-scale Helios operation.
  - UALink-over-Ethernet scale-up at 72 GPUs.
  - Frontier-scale pretraining on AMD.

### Cited Findings

**A. Demonstrated, and by whom**
- **MLPerf Inference v6.0 (published 1 Apr 2026)** — [IND: MLCommons-published results]; percentages are AMD's [CO]:
  - MI355X passed 1M tokens/s in multi-node runs of up to 94 GPUs, on Llama 2 70B and GPT-OSS-120B.
  - Scaling across 11 nodes was 93–98% efficient.
  - 8-GPU MI355X vs B200 on Llama 2 70B: about equal offline, 97% in server mode, 119% in interactive mode.
  - Vs B300 on the same benchmark: 92%, 93% and 104%.
  - GPT-OSS-120B: 11% (offline) and 15% (server) ahead of B200, but 91% and 82% of B300.
  - 3.1x the MI325X on Llama 2 70B server.
  - Nine partners submitted results on AMD hardware, within 4% of AMD's own figures.
  - Dell and MangoBoost submitted the first heterogeneous entry (MI300X + MI325X + MI355X), reaching about 142,000 tokens/s.
  - AMD submitted nothing for DeepSeek-R1 or Qwen3-VL, and its Wan-2.2 entry was in the Open division.
  - Post-deadline results at 108% of B200 are "not verified by MLCommons."
  - Source: [The Decoder, Maximilian Schreiner, 2026-04-02](https://the-decoder.com/nvidia-sets-new-mlperf-records-with-288-gpus-while-amd-and-intel-focus-on-different-battles/); [AMD blog, "MLPerf 6.0: AMD Instinct MI355X GPUs Surpass 1M Tokens/Sec…," Apr 2026](https://amd.com/en/blogs/2026/amd-delivers-breakthrough-mlperf-inference-6-0-results.html)
- **NVIDIA in the same round:**
  - GB300 NVL72 had the highest throughput on every new workload.
  - A 288-GPU configuration reached about 2.49M tokens/s on DeepSeek-R1 offline.
  - Fourteen partners submitted on NVIDIA, and NVIDIA was the only vendor to submit every new model and scenario.
  - The Decoder: results are "only partially comparable." [3P-CO]; [press analysis] — [The Decoder, 2026-04-02](https://the-decoder.com/nvidia-sets-new-mlperf-records-with-288-gpus-while-amd-and-intel-focus-on-different-battles/)
- **MLPerf Training v6.0 (Jun 2026):**
  - MI355X Llama 3.1-8B pretraining in MXFP4 came within 6% of B200 using NVFP4.
  - 13% faster than AMD's previous round.
  - AMD's first own multi-server training submission; partner submissions within 6%.
  - [CO]; [SECONDARY]. The primary blog returned 503, and MLCommons tables were not retrieved. — [AMD blog (MLPerf Training 6.0)](https://www.amd.com/en/blogs/2026/amd-delivers-breakthrough-mlperf-training-6-0-results.html); [igor'sLAB](https://www.igorslab.de/en/amd-mlperf-training-6-0-instinct-mi355x-approaches-blackwell-scales-multiple-servers/)
- **SemiAnalysis InferenceX v2 (16 Feb 2026), [IND: SemiAnalysis]:**
  - "AMD's SGLang delivers better perf per TCO than NVIDIA's SGLang for FP8" in single-node serving.
  - MI355X with disaggregated prefill "is quite competitive with B200 (Dynamo SGLang)" at FP8.
  - MI355X vs MI325X: nearly 4x per-GPU throughput and nearly 3x lower cost. Up to 10x vs MI300X.
  - "AMD has almost doubled the amount of throughput in the span of less than 2 months" on DeepSeek R1 FP4 SGLang.
  - [SemiAnalysis, 2026-02-16](https://newsletter.semianalysis.com/p/inferencex-v2-nvidia-blackwell-vs)
- **Customers training or serving on AMD** (all company-stated or customer-stated):
  - Meta Llama 3/4 inference on MI300X (Jun 2025).
  - Meta "training, ranking and recommendation" on Instinct (Oct 2026).
  - OpenAI GPT-class research on MI300X via Azure (Jun 2025).
  - Zyphra ZAYA1 (8.3B total / 760M active MoE) trained on 1,024 MI300X. Zyphra and AMD call it "the first large-scale MoE… trained using an AMD GPU and networking platform," with no independent verification.
  - Anthropic model bring-up on MI355X (Nov 2026).
  - HUMAIN GPU-as-a-service on MI355X (Aug 2026).
  - [CO+CUST] — [AMD Advancing AI 2025 release](https://ir.amd.com/news-events/press-releases/detail/1255/amd-unveils-vision-for-an-open-ai-ecosystem-detailing-new-silicon-software-and-systems-at-advancing-ai-2025); [AMD–Meta release, 2026-10-27](https://ir.amd.com/news-events/press-releases/detail/1302/amd-and-meta-advance-strategic-partnership-to-power-metas-superintelligence-infrastructure); [AMD Zyphra release](https://ir.amd.com/news-events/press-releases/detail/1268/amd-powers-frontier-ai-training-for-zyphra); [Q3'26 call](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/); [HUMAIN release](https://ir.amd.com/news-events/press-releases/detail/1298/amd-cisco-and-humain-expand-saudi-arabias-ai-infrastructure-as-amd-instinct-systems-go-live)

**B. Independent critiques and what remains unproven**
- **SemiAnalysis, Dec 2024 (MI300X training)**, [IND: SemiAnalysis; via secondary coverage]:
  - MI300X had lower total cost of ownership, but worse training performance per TCO "on public stable releases of AMD software." The picture changed with custom development builds.
  - H100 was about 10–25% faster in multi-node training, "and the difference widens as more nodes" join.
  - SemiAnalysis cited "a lack within AMD public release software stack and the lack of testing."
  - [SemiAnalysis, "MI300X vs H100 vs H200 Benchmark Part 1: Training – CUDA Moat Still Alive," 2024-12-22](https://newsletter.semianalysis.com/p/mi300x-vs-h100-vs-h200-benchmark-part-1-training); [TechPowerUp, 2024-12-23](https://techpowerup.com/330155/amds-pain-point-is-rocm-software-nvidias-cuda-software-is-still-superior-for-ai-development-report); [The Decoder](https://the-decoder.com/amds-software-woes-leave-nvidia-unchallenged-in-ai-chip-market-study-finds/)
- **SemiAnalysis, Feb 2026 (InferenceX v2)**, [IND: SemiAnalysis]:
  - "The composability of disagg prefill, wideEP and FP4 inference optimizations needs significant improvement." AMD is "not competitive with Nvidia's" when all three are combined.
  - AMD is "more than six months behind" on distributed inference.
  - The ATOM engine "is completely lacking on a lot of features that makes it unusable for real workloads."
  - "There are currently zero Mi355X tests on vLLM." The MI355X "still uses a fork of the vLLM 0.10.1 build," and vLLM maintainers "cannot support day 0 vLLM support for ROCm" because they lack machines.
  - "The current subpar software is due to lack of focus and incorrect prioritization."
  - [SemiAnalysis, 2026-02-16](https://newsletter.semianalysis.com/p/inferencex-v2-nvidia-blackwell-vs)
- **SemiAnalysis, 25 Aug 2026 (AgentX, DeepSeek V4 Pro)**, [IND: SemiAnalysis]:
  - Before 21 Aug 2026, MI355X (AMD's SGLang team) matched B200 vLLM on performance per dollar.
  - After vLLM optimizations by Inferact and NVIDIA, B200 moved ahead.
  - MI355X is most comparable at low throughput, and the gap widens at high throughput "despite MI355X having 1.5x the HBM of B200."
  - AMD's ATOM beats B200 vLLM but not B300 or B200 SGLang. Most labs "do not want to run" ATOM in production, and open-source vLLM on MI355X still trails ATOM.
  - The page calls itself an unofficial InferenceX mirror whose data "may be modified or out of date."
  - [SemiAnalysis InferenceX blog, 2026-08-25](https://inferencex.semianalysis.com/blog/deepseek-v4-pro-agentx-mi355x-vs-b200-august)
- **Unproven: rack-scale MI455X.**
  - AMD claims 34x the token throughput of MI355X (DeepSeek V4 Flash, FP4 serving, AMD Performance Labs, Jul 2026, "system configurations may vary"). [CO] — [AAI 2026 release](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era)
  - "Up to 18x tokens per dollar." [CO] via press — [iTWire](https://itwire.com/business-it-news/data/astounding-massive-dominant-ai-innovation-amd-launches-helios-against-nvidia-tips-up-to-us-5-billion-into-anthropic-and-books-roughly-14-gigawatts-of-customer-ai-compute-at-advanci)
  - I found no MLPerf entry for MI455X or Helios in the rounds reviewed (Inference 6.0, Apr 2026; Training 6.0, Jun 2026). [IND: absence in MLCommons rounds as reported] — [The Decoder](https://the-decoder.com/nvidia-sets-new-mlperf-records-with-288-gpus-while-amd-and-intel-focus-on-different-battles/)
- **Unproven: Helios vs Vera Rubin.**
  - AMD claims 15% more FP4, 50% more HBM capacity, 50% more scale-out bandwidth and "up to 30% more tokens per dollar." [CO]
  - The basis is estimated throughput on Kimi K2 Thinking (32K input / 8K output) across interactivity points, with "projected hourly GPU pricing," estimated by AMD Performance Labs as of Jul 2026. [CO]
  - [AAI 2026 release, footnote 1](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era); [iTWire](https://itwire.com/business-it-news/data/astounding-massive-dominant-ai-innovation-amd-launches-helios-against-nvidia-tips-up-to-us-5-billion-into-anthropic-and-books-roughly-14-gigawatts-of-customer-ai-compute-at-advanci)
- **Unproven: gigawatt scale and frontier training.** No source reviewed documents gigawatt-scale Helios operation or a frontier-scale LLM pretraining run on AMD. The largest documented AMD training in these sources is Zyphra's 1,024-GPU MI300X run of an 8.3B-parameter MoE, and MLPerf's Llama 3.1-8B. [n/a]
- **Rack-scale deployment base:** "Google TPU, AWS Trainium, and Nvidia are the only AI chips with rack-scale designs deployed today" (as of Feb 2026). [IND/EST: SemiAnalysis] — [SemiAnalysis, 2026-02-16](https://newsletter.semianalysis.com/p/inferencex-v2-nvidia-blackwell-vs)

**C. Physical and engineering limits that apply**
- **Memory capacity:** 432 GB of HBM4 per MI455X vs 288 GB per Rubin GPU, so 31 TB vs 20.7 TB per 72-GPU rack (+50%).
  - [CO] — [iTWire](https://itwire.com/business-it-news/data/astounding-massive-dominant-ai-innovation-amd-launches-helios-against-nvidia-tips-up-to-us-5-billion-into-anthropic-and-books-roughly-14-gigawatts-of-customer-ai-compute-at-advanci)
  - [3P-CO] — [NVIDIA, Vera Rubin NVL72 page (accessed 2026-11-14)](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)
  - SemiAnalysis found the MI355X's 1.5x HBM advantage over B200 did not prevent a throughput gap at high load. [IND: SemiAnalysis] — [SemiAnalysis, 2026-08-25](https://inferencex.semianalysis.com/blog/deepseek-v4-pro-agentx-mi355x-vs-b200-august)
- **Memory bandwidth:**
  - NVIDIA lists Rubin at 19.2 TB/s per GPU and 1,400 TB/s per rack. [3P-CO] — [NVIDIA](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)
  - MI455X: 19.6 TB/s (AMD brochure) vs about 1.7 PB/s per rack (AMD at AAI 2026). [CO]/[SECONDARY] — see §9 CX-8.
- **FP4 compute:**
  - NVIDIA lists Rubin NVL72 at 2,520 PFLOPS dense NVFP4 (training) and 3,600 PFLOPS sparse NVFP4 (inference). [3P-CO] — [NVIDIA](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)
  - AMD lists Helios at 2.9 EF FP4. [CO] — [iTWire](https://itwire.com/business-it-news/data/astounding-massive-dominant-ai-innovation-amd-launches-helios-against-nvidia-tips-up-to-us-5-billion-into-anthropic-and-books-roughly-14-gigawatts-of-customer-ai-compute-at-advanci)
- **Scale-up without NVLink:**
  - NVLink 6 is 3 TB/s per GPU and 216 TB/s per rack. [3P-CO] — [NVIDIA](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)
  - Helios scale-up runs over "UALink and Ethernet" ([CO] via [iTWire](https://itwire.com/business-it-news/data/astounding-massive-dominant-ai-innovation-amd-launches-helios-against-nvidia-tips-up-to-us-5-billion-into-anthropic-and-books-roughly-14-gigawatts-of-customer-ai-compute-at-advanci)), and SemiAnalysis names the system "UALoE72" ([SemiAnalysis](https://newsletter.semianalysis.com/p/inferencex-v2-nvidia-blackwell-vs)).
  - 260 TB/s for Helios scale-up is reported only in secondary coverage. [SECONDARY] — [ai2.work](https://ai2.work/blog/amd-helios-at-hot-chips-2-9-exaflops-and-31tb-hbm4-in-one-rack)
  - I found no independent latency or bandwidth measurement of Ethernet-based scale-up at 72 GPUs.
- **Chiplets, packaging and yield:** the MI455X has 12 compute and I/O chiplets across N2 and N3 and 320B transistors. [CO] — [iTWire](https://itwire.com/business-it-news/data/astounding-massive-dominant-ai-innovation-amd-launches-helios-against-nvidia-tips-up-to-us-5-billion-into-anthropic-and-books-roughly-14-gigawatts-of-customer-ai-compute-at-advanci)
  - AMD itself flags yield risks from "design failures, packaging technology failures, process technology failures," and limited suppliers of interposers, substrates and memory. [CO-SEC] — [10-Q Q3'26](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm)
  - AMD claims leadership in "3D hybrid bonding" and HBM integration, and is qualifying 2.5D EFB bridges with ASE, SPIL and PTI for Venice. [CO] — [Taiwan release, 2026-05-21](https://ir.amd.com/news-events/press-releases/detail/1286/amd-announces-more-than-10-billion-in-taiwan-ecosystem-investments-to-accelerate-ai-infrastructure)
- **Power and cooling:**
  - AMD has not published MI455X board power or Helios rack power in the sources reviewed. [n/a]
  - NVIDIA's page also omits rack power and lists a 45°C inlet temperature. [3P-CO] — [NVIDIA](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)
  - AMD lists power and cooling among the third-party rack components whose shortage or defects could delay Helios. Defects may be "discovered after a product… has been shipped." [CO-SEC] — [10-Q Q3'26](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm)
  - Norrod denied a rumored thermal design issue in Feb 2026. [CO] — [The Next Platform](https://www.nextplatform.com/compute/2026/02/23/amd-says-helios-racks-and-mi400-series-gpus-on-track-for-2h-2026/4092199)

**D. Evidence status ("solid ground?")**

| Claim area | Evidence status as of 14 Nov 2026 | Basis |
|---|---|---|
| MI300X/MI355X usable in production inference | **Corroborated** | Customer statements (Meta, Microsoft, OpenAI, Cohere, HUMAIN); MLPerf with 9 partner submitters within 4%; SemiAnalysis single-node findings |
| MI355X ≈ B200 on selected inference benchmarks | **Corroborated for AMD-chosen workloads only** | MLPerf 6.0 percentages; no AMD DeepSeek-R1 or Qwen3-VL submissions; SemiAnalysis shows B200 ahead once fully optimized |
| AMD tokens-per-dollar advantage | **Contested / workload-dependent** | AMD's Jun 2025 "up to 40%" claim vs SemiAnalysis Feb and Aug 2026 results (§9 CX-4) |
| ROCm parity with CUDA for distributed inference and training | **Not demonstrated** | SemiAnalysis Feb 2026 ("more than six months behind"); Aug 2026 ATOM-vs-vLLM gap; rapid improvement acknowledged |
| MI455X/Helios performance and vs Vera Rubin | **Company projections only** | AMD Performance Labs estimates with projected pricing; no third-party benchmarks or MLPerf entries |
| Helios at gigawatt scale | **Untested** | First racks only; Meta "being tested"; OpenAI online "beginning Q4 2026"; no warrant vesting at 26 Sep 2026 |
| Frontier-model pretraining at scale on AMD | **Not documented** | Largest documented: Zyphra (1,024 MI300X, 8.3B MoE); MLPerf Llama 3.1-8B |

### Inferences
- **Arithmetic checks:**
  - 72 × 432 GB = 31.1 TB, matching AMD's "31 TB."
  - 72 × 40 PF = 2.88 EF, matching "2.9 EF."
  - 2.9 / 2.52 ≈ 1.15. So AMD's "+15% FP4" compares dense to dense. Against NVIDIA's headline 3.6 EF sparse figure, Helios would be about 19% lower.
- **Possible explanation for the bandwidth discrepancy** (unsourced background; verify):
  - HBM4 uses a 2048-bit interface per stack.
  - 432 GB is consistent with 12 stacks of 36 GB each.
  - At about 6.4 Gb/s per pin, 12 stacks give about 19.7 TB/s. At about 7.7 Gb/s per pin, they give about 23.6 TB/s, matching 1.7 PB/s across 72 GPUs.
  - So the two figures may reflect a pin-speed change between CES-era and July-2026 specifications.
- **Where AMD's position rests:** on capacity and peak-compute specifications plus improving software. NVIDIA's lead in independent testing is in fully optimized, distributed, multi-technique serving, which is where SemiAnalysis locates AMD's weakness. The physical specs (HBM capacity) are verifiable from vendor spec sheets. Delivered throughput depends on software composability that independent testers had not yet seen match NVIDIA as of Aug 2026.

### Gaps
- Earlier MLPerf rounds (Inference v4.1/v5.0/v5.1; Training v5.0/v5.1) and Inference v6.1 (if published Sep 2026) were not retrieved.
- SemiAnalysis's full Dec 2024 article and InferenceMAX v1 (Oct 2025) were not retrieved directly.
- No independent UALink/UALoE latency data.
- No MI455X or Helios power figures.
- No independent reliability or failure-rate data for Helios.
- No public documentation of any frontier lab pretraining a flagship model on AMD.

---

## 9. Cross-examination log: AMD claims vs independent benchmarks, customers, suppliers and NVIDIA

### Takeaway
- **Mixed record:** AMD's chip-level claims for MI355X largely hold on the workloads AMD selected (MLPerf). Its broad tokens-per-dollar and ROCm-progress claims are partly contradicted by SemiAnalysis's independent testing.
- **Rack-scale claims:** readiness and Vera Rubin comparisons rest only on AMD and customer statements and projections.
- **Wording to watch:** several items in AMD's own materials (rack sales wording, deployment status, bandwidth specs) do not line up exactly.

### Cited Findings
- **CX-1 Helios/MI455X timing.**
  - Claim: "on target for 2H 2026" (AMD, Feb 2026). Norrod: "highly confident of ramping Helios in high volume in the second half of the year." [CO]
  - Counter-evidence: SemiAnalysis (Feb 2026) says first production tokens on MI455X UALoE72 arrive by Q2 2027, with mass production also in 2027. [EST: SemiAnalysis]
  - Outcome so far: AMD reports volume MI455X shipments and first racks online in Q3'26 [CO]; OpenAI targets Helios online "beginning Q4 2026" [CO+CUST]; Meta's racks are "being tested" [CO+CUST]; no warrant had vested by 26 Sep 2026 [CO-SEC].
  - Status: **partly resolved in AMD's favor on the start date. Gigawatt-scale timing has not been independently verified.**
  - Sources: [The Next Platform, 2026-02-23](https://www.nextplatform.com/compute/2026/02/23/amd-says-helios-racks-and-mi400-series-gpus-on-track-for-2h-2026/4092199); [SemiAnalysis, 2026-02-16](https://newsletter.semianalysis.com/p/inferencex-v2-nvidia-blackwell-vs); [Q3'26 call](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/); [AAI 2026 release](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era); [AMD–Meta, 2026-10-27](https://ir.amd.com/news-events/press-releases/detail/1302/amd-and-meta-advance-strategic-partnership-to-power-metas-superintelligence-infrastructure); [10-Q](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm)
- **CX-2 Who sells Helios.**
  - Call wording: Q3 was the first quarter AMD "shipped MI455 and Helios racks for revenue" (as summarized from the transcript). [CO]
  - 10-Q wording: "we do not manufacture or sell the completed Helios rack-scale solutions." [CO-SEC]
  - Status: **a wording tension.** AMD's revenue is from components; racks are built and sold by ODMs and OEMs.
  - Sources: [Q3'26 call](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/); [10-Q Q3'26](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm)
- **CX-3 Meta deployment status.**
  - AMD's Q3 release (3 Nov 2026) says Meta is "running models and workloads on the first Helios rack-scale systems." [CO]
  - The joint AMD–Meta release a week earlier (27 Oct 2026) says Helios is "installed and being tested," with broader deployment "in the near future." [CO+CUST]
  - Status: **consistent with testing, not production.**
  - Sources: [Q3'26 8-K](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000188/q32026991.htm); [AMD–Meta release, 2026-10-27](https://ir.amd.com/news-events/press-releases/detail/1302/amd-and-meta-advance-strategic-partnership-to-power-metas-superintelligence-infrastructure)
- **CX-4 Tokens per dollar, MI355X vs B200.**
  - Claim (Jun 2025): "up to 40% more tokens-per-dollar." The basis: Llama 3.1-405B FP4, using CoreWeave's published B200 pricing vs *expected* MI355X cloud pricing. [CO]
  - Counter-evidence:
    - SemiAnalysis (Feb 2026): AMD has better perf/TCO than NVIDIA SGLang on single-node FP8, but TensorRT-LLM "continues to framemog" AMD, and AMD is not competitive once disaggregation, wide expert parallelism and FP4 are combined. [IND]
    - SemiAnalysis (Aug 2026): B200 overtook MI355X on perf/$ for DeepSeek V4 Pro after the 21 Aug vLLM optimizations. [IND]
  - Status: **contradicted as a general claim; holds only for some workloads and software stacks.**
  - Sources: [AMD Advancing AI 2025 release](https://ir.amd.com/news-events/press-releases/detail/1255/amd-unveils-vision-for-an-open-ai-ecosystem-detailing-new-silicon-software-and-systems-at-advancing-ai-2025); [SemiAnalysis, 2026-02-16](https://newsletter.semianalysis.com/p/inferencex-v2-nvidia-blackwell-vs); [SemiAnalysis, 2026-08-25](https://inferencex.semianalysis.com/blog/deepseek-v4-pro-agentx-mi355x-vs-b200-august)
- **CX-5 MI355X vs B200 in MLPerf.**
  - AMD's percentages show parity to a lead on Llama 2 70B and GPT-OSS-120B, but a deficit vs B300 except in interactive mode. [CO from MLCommons data]
  - AMD skipped DeepSeek-R1 (MoE reasoning) and Qwen3-VL; NVIDIA submitted every new workload. [IND: MLCommons participation record, via The Decoder]
  - Status: **verified only for AMD's chosen workloads.**
  - Source: [The Decoder, 2026-04-02](https://the-decoder.com/nvidia-sets-new-mlperf-records-with-288-gpus-while-amd-and-intel-focus-on-different-battles/)
- **CX-6 Training parity.**
  - AMD says it is within 6% of B200 on MLPerf Training 6.0 Llama 3.1-8B (MXFP4 vs NVFP4). [CO; SECONDARY]
  - This is a small model and says nothing about frontier-scale multi-node training. SemiAnalysis's Dec 2024 multi-node training finding (H100 10–25% faster, with a widening gap) has no newer independent counterpart in the sources reviewed.
  - Status: **unresolved at scale.**
  - Sources: [AMD blog](https://www.amd.com/en/blogs/2026/amd-delivers-breakthrough-mlperf-training-6-0-results.html); [igor'sLAB](https://www.igorslab.de/en/amd-mlperf-training-6-0-instinct-mi355x-approaches-blackwell-scales-multiple-servers/); [TechPowerUp, 2024-12-23](https://techpowerup.com/330155/amds-pain-point-is-rocm-software-nvidias-cuda-software-is-still-superior-for-ai-development-report)
- **CX-7 Helios vs Vera Rubin.**
  - AMD's claims: +15% FP4, +50% HBM capacity, +50% scale-out bandwidth, "up to 30%" more tokens per dollar. These are projections with projected pricing. [CO]
  - NVIDIA's page lists:
    - 2.52 EF dense / 3.6 EF sparse NVFP4.
    - 20.7 TB HBM4 and 1.4 PB/s.
    - NVLink 3 TB/s per GPU (216 TB/s per rack).
    - "Networking" of 0.45 TB/s per GPU and 32.4 TB/s per rack, bidirectional.
    - It claims Vera Rubin delivers "one-tenth the cost per million tokens compared to NVIDIA GB200 NVL72" on the same Kimi-K2-Thinking 32K/8K workload AMD used, marked "projected… subject to change." [3P-CO]
  - Checks:
    - HBM +50% holds (31 / 20.7).
    - FP4 +15% holds only dense-to-dense. Against NVIDIA's headline sparse 3.6 EF, Helios is about 19% lower.
    - The +50% scale-out claim cannot be checked, because no primary Helios scale-out figure was retrieved. Against NVIDIA's listed 32.4 TB/s, +50% would imply about 48.6 TB/s for Helios.
  - Status: **no independent measurement of either rack; both vendors' cost-per-token claims are projections.**
  - Sources: [AAI 2026 release](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era); [iTWire](https://itwire.com/business-it-news/data/astounding-massive-dominant-ai-innovation-amd-launches-helios-against-nvidia-tips-up-to-us-5-billion-into-anthropic-and-books-roughly-14-gigawatts-of-customer-ai-compute-at-advanci); [NVIDIA Vera Rubin NVL72](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/)
- **CX-8 MI455X memory bandwidth specification.**
  - 19.6 TB/s per GPU appears in AMD's Helios brochure and TensorWave's listing. [SECONDARY]
  - AMD at AAI 2026 gave 1.7 PB/s per rack, which implies about 23.6 TB/s per GPU. [CO via press]
  - Other outlets cite 23.3 TB/s, and some coverage cites 1.4 PB/s per rack. [SECONDARY]
  - Status: **unresolved; possibly a specification update.**
  - Sources: [TensorWave](https://tensorwave.com/products/accelerators/amd-mi455x); [iTWire](https://itwire.com/business-it-news/data/astounding-massive-dominant-ai-innovation-amd-launches-helios-against-nvidia-tips-up-to-us-5-billion-into-anthropic-and-books-roughly-14-gigawatts-of-customer-ai-compute-at-advanci); [Digital Citizen](https://www.digitalcitizen.life/amd-instinct-mi455x-brings-432gb-of-hbm4-and-40-pflops-of-ai-compute-to-helios/); [Flopper](https://flopper.io/gpu/amd-instinct-mi455x)
- **CX-9 ROCm progress.**
  - AMD's claims: ROCm.ai averages 3.3x inference and 2.4x training over ROCm 7; ROCm 10 "weeks… into hours"; releases every 6 weeks. [CO]
  - Counter-evidence:
    - SemiAnalysis (Feb 2026): zero MI355X vLLM CI tests; a vLLM 0.10.1 fork; ATOM "unusable for real workloads"; "more than six months behind." [IND]
    - SemiAnalysis (Aug 2026): open-source vLLM on MI355X still trails AMD's own ATOM engine, and labs avoid ATOM in production. [IND]
    - SemiAnalysis also credits AMD with nearly doubling DeepSeek R1 FP4 throughput in under two months. [IND]
  - Status: **independently observed progress, but parity contradicted as of Aug 2026.**
  - Sources: [iTWire](https://itwire.com/business-it-news/data/astounding-massive-dominant-ai-innovation-amd-launches-helios-against-nvidia-tips-up-to-us-5-billion-into-anthropic-and-books-roughly-14-gigawatts-of-customer-ai-compute-at-advanci); [Q3'26 call](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/); [SemiAnalysis, 2026-02-16](https://newsletter.semianalysis.com/p/inferencex-v2-nvidia-blackwell-vs); [SemiAnalysis, 2026-08-25](https://inferencex.semianalysis.com/blog/deepseek-v4-pro-agentx-mi355x-vs-b200-august)
- **CX-10 Gigawatts "booked" vs binding.**
  - iTWire's headline: about 14 GW "booked." [press]
  - The 8-Ks show binding volume of only the initial 1 GW each from OpenAI and Meta, 2 GW in total. [CO-SEC]
  - Anthropic's 2 GW is "up to," with no binding statement. [CO]
  - Status: **headline overstates the firm commitments.**
  - Sources: [iTWire](https://itwire.com/business-it-news/data/astounding-massive-dominant-ai-innovation-amd-launches-helios-against-nvidia-tips-up-to-us-5-billion-into-anthropic-and-books-roughly-14-gigawatts-of-customer-ai-compute-at-advanci); [OpenAI 8-K](https://ir.amd.com/financial-information/sec-filings/content/0001193125-25-230895/0001193125-25-230895.pdf); [Meta 8-K](https://www.sec.gov/Archives/edgar/data/2488/000000248826000045/amd-20260223.htm); [Anthropic release](https://ir.amd.com/news-events/press-releases/detail/1292/amd-and-anthropic-announce-strategic-partnership-to-deploy-up-to-2-gigawatts-of-amd-instinct-mi450-series-gpus)
- **CX-11 Meta deal value.**
  - AMD: undisclosed. [CO]
  - Bajarin: "tens of billions" over at least four years. [EST]
  - Jon Peddie: "$60B." Introl: over "$100B." [SECONDARY]
  - Status: **estimates conflict; no primary value exists.**
  - Sources: [AMD–Meta release](https://ir.amd.com/news-events/press-releases/detail/1279/amd-and-meta-announce-expanded-strategic-partnership-to-deploy-6-gigawatts-of-amd-gpus); [CNBC](https://www.cnbc.com/2026/02/24/meta-to-use-6gw-of-amd-gpus-days-after-expanded-nvidia-ai-chip-deal.html); [JPR](https://www.jonpeddie.com/news/amd-and-meta-announce-60b-6-gw-ai-partnership/); [Introl](https://introl.com/blog/meta-amd-100-billion-gpu-deal-nvidia-exclusivity)
- **CX-12 MI500 performance claims.**
  - CES 2026: "up to a 1,000x increase in AI performance" vs MI300X, based on peak theoretical rack performance projected in Dec 2025. [CO]
  - AAI 2026: "more than 2,000 times higher inference throughput in just 4 years." [CO via press]
  - Status: **the metric changed and the number doubled within six months; both are projections.**
  - Sources: [CES 2026 release](https://ir.amd.com/news-events/press-releases/detail/1272/amd-and-its-partners-share-their-vision-for-ai-everywhere-for-everyone-at-ces-2026); [iTWire](https://itwire.com/business-it-news/data/astounding-massive-dominant-ai-innovation-amd-launches-helios-against-nvidia-tips-up-to-us-5-billion-into-anthropic-and-books-roughly-14-gigawatts-of-customer-ai-compute-at-advanci)
- **CX-13 Date of the delay report.**
  - One search-result summary placed the SemiAnalysis delay report in May 2026. [SECONDARY]
  - The primary SemiAnalysis piece is dated 16 Feb 2026, and Next Platform's relay is dated 23 Feb 2026.
  - Status: **the May dating is wrong.**
  - Sources: [SemiAnalysis](https://newsletter.semianalysis.com/p/inferencex-v2-nvidia-blackwell-vs); [The Next Platform](https://www.nextplatform.com/compute/2026/02/23/amd-says-helios-racks-and-mi400-series-gpus-on-track-for-2h-2026/4092199)
- **CX-14 InferenceX cost comparisons in secondary coverage.**
  - AI Weekly reports MI355X "up to 46% cheaper than GB200 NVL72" on Kimi K3 2.8T, citing pricing of GB200 at $1.86/hr and MI355X at $1.50/hr from SemiAnalysis's Jul 2026 surveys. Its own figures are internally inconsistent. [SECONDARY]
  - The InferenceX GLM 5.3 comparison page shows GB200 NVL72 ahead by about 48–82% in tokens/s per chip and lower in cost per token at most points, though its table and text disagree on some values. [IND: SemiAnalysis, low confidence]
  - Status: **workload-dependent; low confidence.**
  - Sources: [AI Weekly](https://aiweekly.co/alerts/amd-mi355x-up-to-46-cheaper-than-gb200-nvl72-on-kimi-k3-28t); [InferenceX GLM 5.3](https://inferencex.semianalysis.com/compare/glm-5-3-gb200-vs-mi355x)
- **CX-15 "Tens of billions" of data-center AI revenue in 2027 (from the research brief).**
  - Not found in the FAD press release.
  - AMD's 3 Nov 2026 guidance ("significantly more than double" in 2027) points the same way, but the exact FAD wording is unverified.
  - Sources: [FAD release](https://ir.amd.com/news-events/press-releases/detail/1266/amd-unveils-strategy-to-lead-the-1-trillion-compute-market-and-accelerate-next-phase-of-growth); [Q3'26 call](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/)
- **CX-16 Market context from customers.**
  - Meta committed to "millions" of NVIDIA processors one week before its AMD deal, and has been in talks with Google about TPUs (The Information, late 2025, via CNBC). [press]
  - Zuckerberg called the AMD deal a step "as we diversify our compute." [CO+CUST]
  - Status: **AMD's position at Meta is described by Meta as one of diversification.**
  - Sources: [CNBC](https://www.cnbc.com/2026/02/24/meta-to-use-6gw-of-amd-gpus-days-after-expanded-nvidia-ai-chip-deal.html); [AMD–Meta release](https://ir.amd.com/news-events/press-releases/detail/1279/amd-and-meta-announce-expanded-strategic-partnership-to-deploy-6-gigawatts-of-amd-gpus)
- **CX-17 Comparability of Q4'25 margin.** Non-GAAP gross margin of 57% in Q4'25 included a ~$360M MI308 reserve release, so a like-for-like comparison is about 53.5% (§3 inference). [CO] — [Q4/FY2025 release](https://ir.amd.com/news-events/press-releases/detail/1276/amd-reports-fourth-quarter-and-full-year-2025-financial)

### Inferences
- **What independent evidence supports:** AMD's single-chip competitiveness with B200-class parts on chosen workloads.
- **Where the claims run ahead of the evidence:** (a) broad cost-efficiency claims, which hold on some stacks only, (b) software maturity at multi-node scale, and (c) anything about MI455X or Helios performance, which has no third-party data yet.
- **Customer schedules and the Q2 2027 projection:** customer-stated schedules (OpenAI from Q4 2026; Anthropic H1 2027) leave room for SemiAnalysis's Q2 2027 "production tokens" projection to prove right without AMD having missed its own Q3 2026 start commitment.

### Gaps
- Not retrieved or not found:
  - NVIDIA's direct public response to AMD's Helios comparisons.
  - Supplier statements (HBM vendors, TSMC) on AMD volumes.
  - Independent customer-reported Helios performance.
  - The Tom's Hardware article body on the VR200 timing rumor.

---

## 10. Closing lists: (a) contradictions found; (b) what could not be found or verified, with verdicts on the two memory leads

### Takeaway
- **Contradictions:** 11 are recorded below. They cluster in four areas: rack-scale timing and status, cost-efficiency and software claims, specification consistency, and how deal sizes are headlined.
- **Unverified items:** the largest are Oracle's 50,000-MI450 commitment, AMD's actual AI GPU revenue for 2025–2026, HBM4 and CoWoS supply detail, MI455X power, and any independent Helios performance data.
- **Lead 1 (Meta warrant deal):** confirmed.
- **Lead 2 (MI455X/Helios slip to 2027):** confirmed as a report, which AMD disputes. AMD's own Q3 shipments partly contradict it; gigawatt-scale timing remains open.

### Cited Findings
**(a) Contradictions found** (details and sources in §9)
1. **Timing (CX-1):** SemiAnalysis (16 Feb 2026) says production tokens on MI455X UALoE72 come by Q2 2027. AMD says "on target for 2H 2026" and reports Q3'26 volume shipments. — [SemiAnalysis](https://newsletter.semianalysis.com/p/inferencex-v2-nvidia-blackwell-vs); [Q3'26 call](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/)
2. **Who sells Helios (CX-2):** the call wording "shipped… Helios racks for revenue" vs the 10-Q's "we do not manufacture or sell the completed Helios rack-scale solutions." — [Q3'26 call](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/); [10-Q](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm)
3. **Meta status (CX-3):** "running models and workloads" (AMD Q3 release, 3 Nov 2026) vs "installed and being tested" (AMD–Meta release, 27 Oct 2026). — [Q3'26 8-K](https://www.sec.gov/Archives/edgar/data/0000002488/000000248826000188/q32026991.htm); [AMD–Meta](https://ir.amd.com/news-events/press-releases/detail/1302/amd-and-meta-advance-strategic-partnership-to-power-metas-superintelligence-infrastructure)
4. **Tokens per dollar (CX-4):** AMD's "up to 40% more tokens-per-dollar vs B200" vs SemiAnalysis's results (not competitive with full optimizations; B200 overtook on perf/$ in Aug 2026). — [AMD 2025-06-12](https://ir.amd.com/news-events/press-releases/detail/1255/amd-unveils-vision-for-an-open-ai-ecosystem-detailing-new-silicon-software-and-systems-at-advancing-ai-2025); [SemiAnalysis Feb](https://newsletter.semianalysis.com/p/inferencex-v2-nvidia-blackwell-vs); [SemiAnalysis Aug](https://inferencex.semianalysis.com/blog/deepseek-v4-pro-agentx-mi355x-vs-b200-august)
5. **ROCm (CX-9):** AMD's ROCm speedup claims vs SemiAnalysis's "more than six months behind," the vLLM CI gap and the ATOM limitations. — [iTWire](https://itwire.com/business-it-news/data/astounding-massive-dominant-ai-innovation-amd-launches-helios-against-nvidia-tips-up-to-us-5-billion-into-anthropic-and-books-roughly-14-gigawatts-of-customer-ai-compute-at-advanci); [SemiAnalysis](https://newsletter.semianalysis.com/p/inferencex-v2-nvidia-blackwell-vs)
6. **FP4 framing (CX-7):** AMD's "+15% FP4 vs Vera Rubin" holds dense-to-dense, but Helios trails NVIDIA's headline sparse 3.6 EF by about 19%. — [NVIDIA](https://www.nvidia.com/en-us/data-center/vera-rubin-nvl72/); [iTWire](https://itwire.com/business-it-news/data/astounding-massive-dominant-ai-innovation-amd-launches-helios-against-nvidia-tips-up-to-us-5-billion-into-anthropic-and-books-roughly-14-gigawatts-of-customer-ai-compute-at-advanci)
7. **Bandwidth spec (CX-8):** MI455X at 19.6 TB/s vs about 23.3–23.6 TB/s (1.7 PB/s per rack). Rack bandwidth is given as 1.4 PB/s in some coverage and 1.7 PB/s in others. — [TensorWave](https://tensorwave.com/products/accelerators/amd-mi455x); [iTWire](https://itwire.com/business-it-news/data/astounding-massive-dominant-ai-innovation-amd-launches-helios-against-nvidia-tips-up-to-us-5-billion-into-anthropic-and-books-roughly-14-gigawatts-of-customer-ai-compute-at-advanci)
8. **Gigawatts (CX-10):** "~14 GW booked" (iTWire headline) vs 2 GW binding in the SEC filings. — [iTWire](https://itwire.com/business-it-news/data/astounding-massive-dominant-ai-innovation-amd-launches-helios-against-nvidia-tips-up-to-us-5-billion-into-anthropic-and-books-roughly-14-gigawatts-of-customer-ai-compute-at-advanci); [Meta 8-K](https://www.sec.gov/Archives/edgar/data/2488/000000248826000045/amd-20260223.htm); [OpenAI 8-K](https://ir.amd.com/financial-information/sec-filings/content/0001193125-25-230895/0001193125-25-230895.pdf)
9. **Meta deal value (CX-11):** undisclosed by AMD vs "tens of billions" (Bajarin), "$60B" (JPR) and ">$100B" (Introl). — [CNBC](https://www.cnbc.com/2026/02/24/meta-to-use-6gw-of-amd-gpus-days-after-expanded-nvidia-ai-chip-deal.html); [JPR](https://www.jonpeddie.com/news/amd-and-meta-announce-60b-6-gw-ai-partnership/); [Introl](https://introl.com/blog/meta-amd-100-billion-gpu-deal-nvidia-exclusivity)
10. **MI500 claims (CX-12):** "up to 1,000x" (Jan 2026) became ">2,000x" (Jul 2026), with a different metric. — [CES 2026 release](https://ir.amd.com/news-events/press-releases/detail/1272/amd-and-its-partners-share-their-vision-for-ai-everywhere-for-everyone-at-ces-2026); [iTWire](https://itwire.com/business-it-news/data/astounding-massive-dominant-ai-innovation-amd-launches-helios-against-nvidia-tips-up-to-us-5-billion-into-anthropic-and-books-roughly-14-gigawatts-of-customer-ai-compute-at-advanci)
11. **Delay-report date (CX-13):** May 2026 (one search summary) vs Feb 2026 (primary sources). Separately, AI Weekly's InferenceX cost figures conflict with the InferenceX GLM 5.3 page (CX-14). — [SemiAnalysis](https://newsletter.semianalysis.com/p/inferencex-v2-nvidia-blackwell-vs); [AI Weekly](https://aiweekly.co/alerts/amd-mi355x-up-to-46-cheaper-than-gb200-nvl72-on-kimi-k3-28t); [InferenceX GLM 5.3](https://inferencex.semianalysis.com/compare/glm-5-3-gb200-vs-mi355x)

**Verdicts on the two memory leads**
- **Lead 1: a Meta–AMD multi-GW agreement in early 2026, possibly with a warrant like OpenAI's — CONFIRMED.**
  - Announced 24 Feb 2026 (8-K dated 23 Feb 2026).
  - Up to 6 GW; the first GW uses a custom MI450-based GPU on Helios, shipping from 2H 2026.
  - Warrant for up to 160M shares at $0.01, expiring 23 Feb 2031. The first tranche vests on shipment of the initial 1 GW-equivalent; full vesting needs 6 GW and a $600 final-tranche price threshold.
  - Only the initial 1 GW is binding.
  - [CO-SEC]/[CO+CUST] — [AMD 8-K, 2026-02-23](https://www.sec.gov/Archives/edgar/data/2488/000000248826000045/amd-20260223.htm); [AMD–Meta release, 2026-02-24](https://ir.amd.com/news-events/press-releases/detail/1279/amd-and-meta-announce-expanded-strategic-partnership-to-deploy-6-gigawatts-of-amd-gpus)
- **Lead 2: reports that MI455X/Helios volume timing slipped toward 2027 — CONFIRMED THAT SUCH REPORTS EXIST; DISPUTED BY AMD; OUTCOME PARTLY RESOLVED.**
  - SemiAnalysis (16 Feb 2026) projected mass production and first production tokens on MI455X UALoE72 by Q2 2027. [EST: SemiAnalysis]
  - AMD denied it (Norrod; Elangovan's "BS," per press). [CO]
  - AMD later reported volume MI455X shipments and first racks in Q3'26. [CO]
  - Customer schedules extend the gigawatt ramp into 2027: OpenAI online from Q4 2026, accelerating through 2027; Anthropic's first GW in H1 2027. [CO+CUST]
  - No independent confirmation of AMD's production volumes exists as of 14 Nov 2026.
  - [SemiAnalysis](https://newsletter.semianalysis.com/p/inferencex-v2-nvidia-blackwell-vs); [The Next Platform](https://www.nextplatform.com/compute/2026/02/23/amd-says-helios-racks-and-mi400-series-gpus-on-track-for-2h-2026/4092199); [Q3'26 call](https://www.fool.com/earnings/call-transcripts/2026/11/04/amd-amd-q3-2026-earnings-call-transcript/); [AAI 2026 release](https://ir.amd.com/news-events/press-releases/detail/1294/aai-2026-amd-delivers-full-stack-compute-for-the-agentic-ai-era); [Anthropic release](https://ir.amd.com/news-events/press-releases/detail/1292/amd-and-anthropic-announce-strategic-partnership-to-deploy-up-to-2-gigawatts-of-amd-instinct-mi450-series-gpus)

### Inferences
- Many of the unverifiable items share one cause: AMD discloses deal ceilings, product launches and qualitative customer milestones, but not unit volumes, AI GPU revenue, power specifications or supplier allocations. Customer schedules and warrant vesting, which AMD must report in its 10-Q, are currently the best external markers of real deployment scale.

### Gaps
**(b) What could not be found or verified**
1. **Oracle's 50,000-MI450 commitment** "from Q3 2026" (14 Oct 2025): Oracle's page returned 403, and AMD releases reviewed don't state the number.
2. **Original roadmap texts:** Computex 2024 and Oct 2024 Advancing AI (MI325X shipping and system-availability wording). Any reporting on weak MI325X demand.
3. **Computex 2026:** no AMD data-center announcement identified.
4. **Earnings calls:** Q1 and Q2 2026 transcripts (404). The FAD transcript and slides, and with them the "tens of billions in 2027" statement.
5. **Revenue disclosures:** AMD Instinct or data-center-AI revenue for 2025 and for each 2026 quarter. Revenue concentration by customer (only receivables concentration is disclosed).
6. **Supply chain:** HBM4 suppliers beyond Samsung (SK hynix, Micron) and qualification status. TSMC CoWoS/SoIC allocation. MI455X packaging flow. Celestica's role.
7. **Physical specifications:** MI455X board power, Helios rack power and cooling. An authoritative per-GPU memory-bandwidth figure. A primary-source Helios scale-up bandwidth figure. UALink-vs-UALoE details, Ultra Ethernet use, and Ethernet scale-up latency.
8. **Independent performance data:** none for MI455X or Helios. MLPerf rounds other than Inference 6.0 and Training 6.0 (Training 6.0 seen only via secondary coverage). Inference v6.1 not checked.
9. **SemiAnalysis primary texts:** Dec 2024 (seen via secondary coverage) and InferenceMAX v1 (Oct 2025).
10. **Deals:** Crusoe (no AMD confirmation found). xAI (no deal found). Volumes for TensorWave, Vultr and Cirrascale. DOE Lux go-live (planned early 2026). Scale of the Microsoft Helios deployment.
11. **China:** 2026 MI308 and MI325 China revenue. Whether any 15% payment was made. The BIS or Federal Register text for the MI325 inspection regime.
12. **Litigation and antitrust:** patent litigation (e.g., hybrid bonding) and securities class actions in 2025–2026. Any antitrust review of the warrants or customer investments.
13. **People and holders:** Vamsi Boppana's role; titles for Papermaster and Grasby; post-Mar-2026 13F holders; Tim Ryan's background.
14. **Deal mechanics:** the ZT Systems closing date. The structure and status of the Anthropic $5B investment and the $1B Meta investment. The warrants' intermediate price hurdles and tranche sizes (redacted in the 8-K exhibits).
15. **NVIDIA:** any direct NVIDIA rebuttal of AMD's Helios claims. VR200 timing rumors (Tom's Hardware body not retrieved).
16. **Method limit:** the session's web-search quota was exhausted partway through research. Items above may be findable with further searching.
