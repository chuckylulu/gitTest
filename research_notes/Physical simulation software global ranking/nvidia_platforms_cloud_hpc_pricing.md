# NVIDIA and cloud platforms in physics AI, simulation cloud/HPC services, and the shift from seats to usage pricing (as of 12 Nov 2026)

**Summary for the report writer.**
- **NVIDIA belongs in the top group as owner of a hardware and programming-platform constraint, not a sign-off judge.**
  - Its physics software is free or open: PhysicsNeMo and Warp (Apache 2.0); Newton (Linux Foundation); Earth-2 models; Omniverse (free for production since May 2026). cuDSS is licensed "only for use in systems with NVIDIA GPUs". The Apollo models (announced Nov 2025) had not been publicly released by 12 Nov 2026.
  - Revenue comes from GPUs plus optional AI Enterprise support at US$4,500/GPU/yr. No software revenue is disclosed.
  - Leverage runs through partners whose solvers stay the judges. NVIDIA bought US$2B of Synopsys stock (1 Dec 2025).
- **NVIDIA's weak points.**
  - Native FP64 per rack fell from 2,880 TFLOPS (GB200 NVL72) to 100 TFLOPS (GB300 NVL72). Rubin's 200 "FP64" TFLOPS is emulation that helps only dense matrix maths; AMD says 60-70% of HPC workloads gain little.
  - Two customers were 22% and 14% of FY2026 revenue. China is closed in practice: H200 was under 1% of data-centre revenue.
  - cuDSS's own licence says it is not certified for critical applications such as avionics.
- **Simulation clouds fill a gap; none owns a judge.**
  - Rescale: US$115M Series D (Apr 2025; investors include NVIDIA, Applied, Foxconn, Hitachi, NEC). The US$750M valuation and US$35M revenue are aggregator figures, unconfirmed.
  - SimScale: last confirmed round was €27M in 2020; sells per-user plans with metered core-hours.
  - Paratera (China): 9M 2026 revenue +111%, 95% of it compute resale.
  - Vendor SaaS (Simcenter X, 3DEXPERIENCE cloud +46%, Synopsys FlexEDA) and hyperscaler HPC are eroding the gap.
- **Pricing: usage meters are spreading, but seats are still the base.**
  - Bentley E365: 46% of ARR (2025). Autodesk consumption: about 17% of revenue, of which Flex is about 2%. Also Altair Units, MSC One (now Cadence), Ansys Elastic, and FlexEDA (per-minute).
  - GPUs are licensed like cores. Ansys 2026 R1: Fluent charges 1 HPC task per GPU streaming multiprocessor beyond 40 included.
  - What vendors said in 2026:
    - Synopsys: "subscription and consumption-based models".
    - Cadence: agents are "a demand accelerator"; "more usage of our base tools".
    - Siemens: named-user licences plus an "agentic surcharge".
    - Dassault: user-based "covering both humans and agents", plus token metering.
    - Autodesk: cites outcome-based models but "we do not expect seats to go away anytime soon".
  - No vendor has disclosed result-based pricing.
- **Priors.**
  - Growth to 2029 (70%): supported. Synopsys targets about 15% CAGR to FY2030; Cadence core EDA grew 20%; Schneider's €22B bid for PTC assumes about 10% a year to 2029.
  - Loss of seat pricing power after 2029 (50%): unresolved. Vendors are hedging with meters, and the evidence that agents multiply runs comes from vendors.

## A1. NVIDIA's physics and simulation software: products or free enablers? How licensed and monetised

### Takeaway
Nearly all of it is open source, free, or tied by licence to NVIDIA GPUs. It exists to pull simulation onto GPUs. The only paid layer is optional enterprise support or NIM microservices, with no revenue disclosed.

### Cited Findings
- **PhysicsNeMo** (formerly Modulus):
  - "an open-source Python framework", Apache 2.0, on PyTorch; enterprise support via NVIDIA AI Enterprise.
  - External Aerodynamics (DoMINO) is offered as a NIM.
  - Claimed adopters (company claims, unconfirmed): Ansys SeaScape; Luminary/nTop ("weeks to mere hours"); Siemens Energy 10,000x; Shell 100,000x; Rescale; SimScale — [NVIDIA](https://developer.nvidia.com/physicsnemo) (accessed 12 Nov 2026).
  - Releases from v2.0.0 (10 Mar 2026) to v2.2.2 (11 Sep 2026) — [GitHub](https://github.com/NVIDIA/physicsnemo/releases).
- **Apollo** (SC25, 17 Nov 2025):
  - Open models for EDA, structures, weather, CFD, electromagnetics and multiphysics, "coming soon to build.nvidia.com, HuggingFace and as NIM microservices"; no licence stated.
  - Adopters: Applied Materials (35x), Cadence, Lam, KLA, Luminary/Northrop Grumman, PhysicsX, Rescale, Siemens, Synopsys ("up to 500x") — [NVIDIA](https://blogs.nvidia.com/blog/apollo-open-models).
  - Hugging Face Hub searches (12 Nov 2026) found no NVIDIA model repositories for "apollo" or "physicsnemo"; NVIDIA hosts PhysicsNeMo CFD datasets under Apache 2.0 — [HF dataset](https://hf.co/datasets/nvidia/PhysicsNeMo-CFD-Ahmed-Body).
  - Apollo is absent from NVIDIA's GTC 2026 open-model list — [NVIDIA, 16 Mar 2026](https://nvidianews.nvidia.com/news/nvidia-expands-open-model-families-to-power-the-next-wave-of-agentic-physical-and-healthcare-ai).
- **"500x" claim**: GPU Fluent (up to 50x) multiplied by AI initialisation (10x), against an undefined baseline; vendor blog — [NVIDIA, 28 Oct 2025](https://blogs.nvidia.com/blog/ai-physics-aerospace-automotive-design-engineering).
- **Omniverse Blueprint "Build a Digital Twin for Interactive Fluid Simulation"**: Omniverse plus PhysicsNeMo plus a DoMINO-Automotive-Aero NIM, trained on Luminary Cloud CFD data, under the NVIDIA Software License Agreement; updated 13 Feb 2026 — [build.nvidia.com](https://build.nvidia.com/nvidia/digital-twins-for-fluid-simulation).
- **Earth-2** (26 Jan 2026): Medium Range, Nowcasting, Data Assimilation (later in 2026), CorrDiff and FourCastNet3, "openly available" on Hugging Face and GitHub. Operational users include the Israel Meteorological Service, GCL and Southwest Power Pool/Hitachi. No paid tier — [NVIDIA](https://blogs.nvidia.com/blog/nvidia-earth-2-open-models).
- **ALCHEMI**: BGR and BMD NIMs released Mar 2026; VASP NIM in early access in Jun 2026; Lila Sciences claims 50x — [NVIDIA, 22 Jun 2026](https://blogs.nvidia.com/blog/ai-for-science-software-cuda/).
- **cuLitho and cuEST at TSMC** (2 Jun 2026): NVIDIA claims 20-50% cost or cycle-time gains and 50x faster chemistry. TSMC is "exploring" Omniverse for FabTwin — [IT Brief](https://itbrief.com.au/story/tsmc-uses-nvidia-ai-to-boost-chip-factory-efficiency).
- **Warp**: Apache License 2.0 — [GitHub](https://github.com/NVIDIA/warp/blob/main/LICENSE.md).
- **Newton** (built on Warp and OpenUSD): given to the Linux Foundation on 29 Sep 2025 by Disney Research, Google DeepMind and NVIDIA — [Linux Foundation](https://www.linuxfoundation.org/press/linux-foundation-announces-contribution-of-newton-by-disney-research-google-deepmind-and-nvidia-to-accelerate-open-robot-learning).
- **cuDSS**, under NVIDIA's Math Libraries SDK licence (v. 10 Feb 2022):
  - "The SDK is licensed for you to develop applications only for use in systems with NVIDIA GPUs."
  - Binaries may be redistributed inside applications. The SDK is not certified for "Critical Applications" (avionics, medical, autonomous vehicles). No price is stated — [NVIDIA docs](https://docs.nvidia.com/cuda/cudss/latest/license.html).
  - Used in COMSOL 6.4 ("up to 5X", COMSOL claim), Ansys HFSS, STAR-CCM+ fluid-structure interaction, and Abaqus (8-10x, Dassault claim) — [Digital Engineering, 10 Feb 2026](https://www.digitalengineering247.com/article/gpu-acceleration-expands).
- **Omniverse**: "As of May 2026, Omniverse is freely available for both development and production use" (earlier list price US$4,500/GPU/yr) — [NVIDIA](https://www.nvidia.com/en-us/omniverse/enterprise/).
- **AI Enterprise** (guide updated 2 Sep 2026): US$4,500/GPU/yr; US$22,500 perpetual; US$1/GPU-hour on cloud marketplaces; free for development; 5-year subscription bundled with H100 and H200 NVL — [NVIDIA](https://docs.nvidia.com/ai-enterprise/planning-resource/licensing-guide/latest/pricing.html).
- **10-K**: lists "paid licenses" to AI Enterprise and vGPU; no software revenue figure — [10-K FY2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm).
- **NemoClaw** (2 Jun 2026), "an open blueprint for building specialized, long-running agents" on the OpenShell runtime:
  - Builders: Cadence (RTL engineer), Dassault, Siemens (Fuse EDA), Synopsys (Icepak agent), Flexcompute, Luminary, Neural Concept, nTop, P-1 AI, PhysicsX (with Microsoft Discovery), SimScale, Synera (on Moldflow).
  - "Weeks to hours" claims are the companies' own; no pricing — [NVIDIA](https://blogs.nvidia.com/blog/industrial-software-leaders-secure-autonomous-ai-engineers-nemoclaw).

### Inferences
- These products are enablers for GPU sales, not revenue lines.
- Free distribution plus a licence that runs only on NVIDIA GPUs (cuDSS) is the lock-in. CUDA-X, which Huang calls the "crown jewels", is the moat.
- Open models and agent blueprints help start-ups and customers, while certified solvers stay with the vendors.

### Gaps
- Apollo's release, licence and checkpoints are unconfirmed.
- AI Enterprise attach rates in simulation are unknown.

## A2. NVIDIA and the simulation vendors: what shipped, equity stakes, compete or enable

### Takeaway
NVIDIA describes itself as "one click below" the solvers. Every major vendor signed deep partnerships in 2025-26, and GPU solvers have shipped widely. Equity ties: US$2B in Synopsys, plus NVentures stakes in PhysicsX, Luminary Cloud and Rescale. NVIDIA mostly enables vendors; its open models are the competitive edge because they help new entrants.

### Cited Findings
- **Synopsys** (1 Dec 2025): US$2B of stock at US$414.79/share; multiyear; "This partnership is not exclusive". Scope: CUDA-X/AI physics, AgentEngineer, digital twins, cloud and joint go-to-market — [NVIDIA](https://nvidianews.nvidia.com/news/nvidia-and-synopsys-announce-strategic-partnership-to-revolutionize-engineering-and-design). Synopsys's 10-Q shows a US$2.0B placement of 4.822M shares — [10-Q Q3 FY2026](https://www.sec.gov/Archives/edgar/data/883241/000088324126000025/snps-20260731.htm).
- **Synopsys at GTC Berlin** (21 Oct 2026): more than 20 GPU-enabled products; 50 CUDA-X libraries. Claims: Sentaurus+cuDSS 12x (Infineon); S-Litho 40x (imec); Speos >4.5 h to <19 min; Lumerical 13x on AWS H100, with a 20-point sweep cut from about 9 days to 18 h (iPronics) — [Synopsys](https://news.synopsys.com/2026-10-21-Synopsys-at-NVIDIA-GTC-Berlin-Delivering-Engineering-Precision-with-Speed).
- **GTC** (16 Mar 2026): Fluent 34x for Honda; Spectre 6x for MediaTek; STAR-CCM+ at JLR and Mercedes; Abaqus/PowerFLOW at Rivian; Cadence Fidelity at Solar Turbines; Siemens Digital Twin Composer on Omniverse. No commercial terms — [NVIDIA](https://nvidianews.nvidia.com/news/nvidia-and-global-industrial-software-giants-bring-design-engineering-and-manufacturing-into-the-ai-era).
- **Siemens** (CES, 6 Jan 2026): "will finish GPU acceleration across its simulation portfolio" — [Business Wire](https://www.businesswire.com/news/home/20260106355227/en/Siemens-and-NVIDIA-Expand-Partnership-to-Build-the-Industrial-AI-Operating-System).
- **Dassault** (3 Feb 2026): "science-validated Industry World Models"; NVIDIA AI factories on OUTSCALE — [NVIDIA](https://nvidianews.nvidia.com/news/dassault-systemes-nvidia-industrial-ai).
- **Altair/EDEM**: 5.31x on 8 H200 GPUs. Ansys: four GPUs "can outperform over a thousand CPU cores for certain CAE applications, at 16% of the cost". NVIDIA holds more than 90% of the relevant GPU market — [Digital Engineering](https://www.digitalengineering247.com/article/gpu-acceleration-expands).
- **Tim Costa** (NVIDIA): NVIDIA sits "one click below" vendors' solvers — [Digital Engineering, 15 May 2026](https://www.digitalengineering247.com/article/tim-costa-nvidia-discusses-enthusiasm-for-ai-integration-among-cae-vendors/cfd).
- **NVentures**:
  - PhysicsX Series B extension (19 Nov 2025): more than US$155M raised, valued at "nearly US$1B" — [PhysicsX](https://www.physicsx.ai/newsroom/physicsx-announces-extension-to-series-b-round). Then a US$300M Series C (8 Jun 2026, start-ups strand).
  - Luminary US$72M Series B (Sep 2025) — [Luminary](https://www.luminarycloud.com/resources/luminary-cloud-secures-dollar72m-series-b-to-lead-the-physics-ai-era).
  - Rescale Series D (B1).

### Inferences
- **Done**: GPU solvers have shipped (Fluent, HFSS, Lumerical, Speos, STAR-CCM+, Abaqus, COMSOL, Fidelity, EDEM, Spectre), and cuLitho is in TSMC production.
- **Said but not proven**: agentic engineers, "Industry World Models", and Apollo surrogates inside certified solvers.
- **Synopsys stake**: about 2.5% of shares (my estimate: 4.8M against roughly 190M diluted shares).

### Gaps
- No figure for GPU revenue from CAE.
- Terms of the Cadence, Siemens and Dassault partnerships are undisclosed.

## A3. Five tests and six transitions applied to NVIDIA (simulation lens)

### Takeaway
NVIDIA is strong on position (hardware plus CUDA), lead and financial strength. Its simulation-specific weaknesses are native FP64, customer concentration and China. It owns no judge, so its simulation fortunes follow GPU demand and the vendors' sign-off rules.

### Cited Findings
- **(a) Position.**
  - Rescale's CAE GPU criteria: FP64, ≥24 GB, >600 GB/s, and CUDA, "since most CAE software relies on CUDA" — [Digital Engineering](https://www.digitalengineering247.com/article/gpu-acceleration-expands).
  - GB200 NVL72 FP64: 2,880 TFLOPS per rack (80 TFLOPS per 2-GPU superchip) — [NVIDIA](https://www.nvidia.com/en-us/data-center/gb200-nvl72/).
  - GB300 NVL72 FP64: 100 TFLOPS per rack — [NVIDIA](https://www.nvidia.com/en-us/data-center/gb300-nvl72/). That is about 1.4 TFLOPS per GPU (my arithmetic); secondary sources give about 1.2 for B300 versus 37 for B200 — [Exxact](https://www.exxactcorp.com/blog/hpc/comparing-nvidia-tensor-core-gpus).
  - Rubin native FP64 is about 33 TFLOPS, "one TFLOP less than the H100". Ozaki emulation reaches 200 TFLOPS on DGEMM only.
  - Dan Ernst (NVIDIA): "it's still FP64. It's not mixed precision." Nicholas Malaya (AMD): 60-70% of HPC workloads see "little to no benefit", and emulation breaks down on ill-conditioned problems such as combustion and materials — [The Register, 18 Jan 2026](https://www.theregister.com/2026/01/18/nvidia_fp64_emulation/).
  - NVIDIA says it is "not abandoning" FP64 — [HPCwire, 9 Dec 2025](https://www.hpcwire.com/2025/12/09/nvidia-says-its-not-abandoning-64-bit-computing/) (headline only; page blocked).
- **(b) Lead.** FY2026 revenue US$215.9B (+65%), of which Compute & Networking US$193.5B — [10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm).
- **(c) Revenue model.** Mostly hardware to few buyers; software free or US$4,500/GPU/yr (A1).
- **(d) Financial strength.**
  - FY2026: direct customers 22% and 14% (FY2025: 12/11/11%); 31% of revenue from customers headquartered outside the US; cash and securities US$62.6B against debt US$8.5B; supply commitments US$95.2B — [10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm).
  - Q2 FY2027 (26 Jul 2026): revenue US$96.2B; gross profit US$72.1B (about 75%); five customers hold 22/14/13/11/10% of receivables; supply and capacity commitments US$279B (US$366B in all); debt US$33.4B after a US$25B issue; non-marketable stakes US$51.2B — [10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm).
  - One customer at 16% of quarterly revenue is a press figure — [Crypto Briefing (secondary)](https://cryptobriefing.com/nvidia-400m-charge-h200-inventory/).
- **(e) Export controls.**
  - H20: US$4.5B charge. The US government expects "15% or more" of licensed sales; H200 shipments face a 25% tariff; NVIDIA is "effectively foreclosed" from China's data-centre compute — [10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm).
  - H200 was under 1% of US$89B data-centre revenue; Q3 guidance of US$108B assumes no China data-centre compute — [The Next Web, 28 Aug 2026](https://thenextweb.com/news/nvidia-h200-china-zero-revenue-guidance-europe-gigafactories).

### Inferences
- **Scenarios.**
  - Steady (55%): CAE keeps moving to GPUs and the software stays free.
  - Financing pause around 2028 (25%): concentration and US$279B of commitments dominate; CAE is a small, stable cushion.
  - Acceleration (20%): surrogates and agents multiply GPU hours.
- **Transitions.**
  - (2) CPU to GPU is the main tailwind, but the FP64 retreat opens a door to AMD (MI430X) and CPUs for certification-grade FEA and CFD.
  - (4) NVIDIA backs AI-enhanced open source.
  - (5) Synopsys's AI-initialised Fluent is the first shipped case of a learned model inside a certifying solver.
  - (6) Sign-off belongs to vendors and regulators; cuDSS's licence explicitly disclaims critical applications.
- **What must go right**: vendors keep porting to GPUs; emulated or mixed precision is accepted for solvers; surrogates gain sign-off acceptance so GPU hours scale.

### Gaps
- Q2 FY2027 revenue concentration from the 10-Q text: the SEC blocked an anonymous download, and the WebFetch read did not show it.

## A4. Google/DeepMind, Microsoft, AWS, Huawei, Baidu, Alibaba

### Takeaway
The hyperscalers sell the compute and HPC services simulation runs on. Their own physics-AI products are weather and materials models or agent platforms. None is a material engineering-simulation software business. Weather is covered by its own strand.

### Cited Findings
- **Google**: WeatherNext 2 (17 Nov 2025) via Earth Engine, BigQuery and Vertex AI early access; no pricing — [Google](https://blog.google/technology/google-deepmind/weathernext-2/). WeatherNext 3 (3 Sep 2026): gated real-time access; older data under CC BY 4.0 — [XenoSpectrum (secondary)](https://xenospectrum.com/weathernext-3-hourly-satellite-forecast/).
- **Microsoft Discovery**: hosts Synopsys agentic EDA workflows for evaluation (27 Jul 2026) — [Synopsys](https://news.synopsys.com/2026-07-27-Synopsys-Advances-Agentic-AI-Chip-Design-with-AMD-and-Microsoft). PhysicsX is building a thermal agent on it (A1). Microsoft is a Rescale investor — [Rescale](https://rescale.com/news/rescale-introduces-agentic-digital-engineering/).
- **AWS**:
  - Parallel Computing Service (GA Aug 2024) targets tightly coupled workloads including CAE — [Amazon](https://press.aboutamazon.com/2024/8/aws-parallel-computing-service-is-now-generally-available-designed-to-accelerate-scientific-discovery).
  - Hpc8a instances for tightly coupled CAE (Feb 2026) — [HPCwire](https://www.hpcwire.com/2026/02/19/aws-targets-tightly-coupled-cloud-hpc-with-hpc8a-instances/).
  - The service added GB200/GB300 UltraServers (Jun 2026) — [AWS](https://aws.amazon.com/th/about-aws/whats-new/2026/06/aws-parallel-computing-service/).
  - "CAE in the Cloud 2026" roadshow in Japan with Ansys, Siemens and Rescale — [AWS](https://aws.amazon.com/jp/blogs/news/cae-in-the-cloud-2026-roadshow-japan/).
- **Huawei Cloud**: "Simulation Solution" is HPC infrastructure for crash, structure and fluid work. No Pangu CAE model was found — [Huawei Cloud](https://www.huaweicloud.com/intl/en-us/solution/cae.html).

### Inferences
- These are enablers, or adjacent competitors in weather. None owns an engineering judge; their pull is CPU and GPU capacity, which also feeds the independents.

### Gaps
- Baidu (PaddleScience) and Alibaba Cloud simulation offerings were not checked (search budget exhausted).
- No revenue data for any hyperscaler simulation business.

## B1. Simulation cloud and HPC providers worldwide

### Takeaway
The independents resell compute, often from hyperscalers or GPU clouds, and add ease of use, data management and now agents and surrogates. They depend on solver vendors' licence terms, none owns a judge, and all are small.

### Cited Findings
- **Rescale (USA).**
  - US$115M Series D, 7 Apr 2025 — [insideHPC](https://insidehpc.com/2025/04/rescale-secures-115m-series-d/). Reported investors: Applied Ventures, Atika, Foxconn, Hanwha, Hitachi Ventures, NEC, NVIDIA, SineWave, Peter Thiel — [Pulse 2.0](https://pulse2.com/rescale-115-million-series-d-raised-for-digital-engineering-platform); earlier backers include Bezos and Altman — [VentureBeat](https://venturebeat.com/ai/115-million-just-poured-into-this-startup-that-makes-engineering-1000x-faster-and-bezos-altman-and-nvidia-are-all-betting-on-its-success).
  - **Valuation US$750M: reported by aggregators, unconfirmed** — [Multiples.vc](https://multiples.vc/private-comps/rescale).
  - **Revenue US$35M: a CB Insights estimate for 2023**, while Multiples.vc puts about US$35M near 2021, so the estimates conflict — [CB Insights](https://www.cbinsights.com/company/rescale/financials).
  - 2026: agentic digital engineering (12 May; "1,000x" and "90%" cost cut are company claims, unconfirmed); DOE codes-to-industry initiative (9 Jun); DOE Genesis Mission award (23 Jul); Honda expansion (14 Oct); customisable agents (10 Nov). Customers include Applied Materials, GM Motorsports, Samsung, SLB, US DoD and Daikin — [Rescale](https://rescale.com/news/), [release](https://rescale.com/news/rescale-introduces-agentic-digital-engineering/).
- **SimScale (Germany).**
  - Last confirmed round: €27M Series C (Jan 2020), led by Insight Partners with Earlybird and USV — [Tech.eu](https://tech.eu/brief/simscale-snags-e27-million-series-c-to-expand-engineering-simulation-software-around-the-world) (older source). Trackers estimate US$60-86M raised in total; no 2025-26 round was found — [PitchBook](https://pitchbook.com/profiles/company/56157-04).
  - 2025-26: "Engineering AI" agent (community 18 Aug 2026; Onshape 15 Sep 2026); Hexagon Marc on its cloud; PhysicsNeMo pump model; PAMICS SPH solver (claims about 20x) — [SimScale press](https://www.simscale.com/press/), [GTC blog](https://www.simscale.com/blog/gtc-2026-what-we-announced-what-we-saw-and-whats-next/).
- **Simr (formerly UberCloud, USA)**: SimOps; runs Ansys, Abaqus, COMSOL and Siemens codes on AWS, Azure, GCP or on-premises — [Digital Engineering](https://www.digitalengineering247.com/article/simr-formerly-ubercloud-kicks-off-simops-for-product-development).
- **Gompute (Sweden)**: bare-metal HPC cloud founded 2002; reportedly acquired by Advania in Aug 2025 — [CB Insights (secondary)](https://www.cbinsights.com/compare/gompute-vs-theubercloud).
- **Inductiva (Portugal)**: API that runs open-source simulators (REEF3D, DualSPHysics, etc.) on cloud CPUs; funding not found — [GitHub](https://github.com/inductiva/inductiva).
- **GPU clouds moving up the stack**: CoreWeave agreed to buy Monolith AI (6 Oct 2025; undisclosed; Monolith customers include Nissan, BMW, Honeywell) — [CoreWeave](https://coreweave.com/news/coreweave-to-acquire-monolith-expanding-ai-cloud-platform-into-industrial-innovation). PhysicsX partnered with CoreWeave (11 Mar 2026) — [PhysicsX](https://www.physicsx.ai/newsroom).
- **China**: Paratera 并行科技 (920493.BJ), 9M 2026:
  - Revenue CNY1.547B (+110.75%); net profit CNY78.8M; operating cash flow CNY337M.
  - Compute services are 95% of revenue, of which AI compute was CNY1.049B (+144%).
  - Source: [Caiwen](https://www.caiwennews.com/article/1675896.shtml) (media report).
- **Japan, listed HPC specialists**: HPC Systems (6597), about ¥11.3B market cap; Fixstars (3687), about ¥54.9B — [Kabutan](https://s.kabutan.jp/stocks/6597/), [Kabutan](https://s.kabutan.jp/stocks/3687/). Japan strand covers them.
- **Korea and India GPU clouds on TOP500** (Jun 2026): NHN Cloud B200 systems (#20, #40), Kakao (#74), India's Yotta Shakti Cloud (#32). General GPU clouds, not simulation-specific — [TOP500](https://www.top500.org/lists/top500/list/2026/06/).

### Inferences
- **Rescale.**
  - (a) Fills a gap: licence and hardware brokerage plus agents.
  - (b) Largest independent by funding; no outside proof of a technical lead.
  - (c) Usage-based compute plus subscriptions, with costs passed through.
  - (d) Margins unknown; depends on ISVs and hyperscalers.
  - (e) Exposed to a 2028 financing pause.
  - Path: become the customer-data and agent layer (its "Data Intelligence" product), or be acquired.
- **SimScale.**
  - (a) Ease of use on open-source and partner solvers.
  - (c) Per-user plans with metered compute (C1).
  - (d) Last confirmed raise was in 2020, so its funding stamina is unknown.
  - (e) Exposed to agents that can drive open solvers directly.
- **Paratera.** A profitable reseller of AI compute, so it follows the AI-capex cycle and China's chip-access conditions.

### Gaps
- Rescale and SimScale revenue, margins and current valuations: no primary source.
- 2025-26 status of Eviden/Nimbix, TotalCAE and Parallel Works not verified.
- Japan (Xtreme-D, Fujitsu), Korea and India simulation clouds are left to the regional strands.

## B2. Vendor-run clouds and hyperscaler HPC: is there a durable role for independents?

### Takeaway
The vendors are folding cloud delivery into their own licensing: Simcenter X, the 3DEXPERIENCE cloud, Synopsys Cloud/FlexEDA, Ansys Elastic, Altair One, and MSC One (now Cadence). Hyperscalers also sell managed HPC directly. Independents keep a role mainly as multi-vendor, multi-cloud orchestration and agent layers, and that role is contestable.

### Cited Findings
- **Siemens**:
  - Simcenter X began in 2024 as SaaS STAR-CCM+, priced pay-as-you-go. Simcenter X Advanced (late 2025) adds Amesim, HEEDS, Simcenter 3D and Femap with cloud-managed entitlements and cloud HPC for CFD — [Siemens](https://news.siemens.com/cs-cz/siemens-simcenter-x-advanced-2025/), [Digital Engineering](https://www.digitalengineering247.com/article/siemens-brings-unified-multiphysics-with-simcenter-x).
  - On its Q4 FY2026 call Siemens said "the SaaS transition has now been completed" — [Investing.com](https://in.investing.com/news/stock-market-news/earnings-call-transcript-siemens-posts-record-orders-in-q4-2026-as-growth-quickens-93CH-5698664).
- **Dassault** Q3 2026: 3DEXPERIENCE cloud +46%; cloud overall +14% — [Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-dassault-systemes-beats-q3-2026-estimates-shares-fall-93CH-4978361).
- **Synopsys**: Synopsys Cloud, plus an EDA SaaS on Azure — [10-K FY2025](https://www.sec.gov/Archives/edgar/data/883241/000088324125000028/snps-20251031.htm). FlexEDA is pay-per-use "on a per-minute basis", available as bring-your-own-cloud or SaaS, with no minimum spend — [Synopsys](https://www.synopsys.com/blogs/chip-design/what-is-flexeda.html), [AWS](https://aws.amazon.com/blogs/industries/flexible-eda-licensing-in-aws-with-synopsys-cloud-byoc-with-flexeda).
- **Cadence**: Millennium (GPU) "had strong adoption" — [Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/10/26/cadence-cdns-q3-2026-earnings-call-transcript/).
- **Luminary Cloud** offers SaaS, Hybrid and Private Cloud deployment; prices are not public — [Luminary](https://luminary.ai/pricing).

### Inferences
- The independents' role is weak and contestable. Vendors that hold the licence keys can meter cloud use themselves, and agents calling solver APIs (Keysight MCP; Cadence and Synopsys agents) reduce the value of a separate front end.
- Their defences: multi-vendor neutrality, sovereign or regulated hosting, and holding customers' simulation data for surrogate training.

### Gaps
- No market-share data comparing independent and vendor clouds.
- Terms for Cadence OnCloud and Ansys Cloud Burst not verified.

## C1. Usage-based schemes, their size, and how GPUs are counted

### Takeaway
Usage meters are common but, outside Bentley, a minority of revenue. GPUs are licensed like CPU cores, either per streaming multiprocessor or as a set number of HPC tasks per card. Licence cost therefore scales with hardware, and moving to GPUs does not escape licence fees.

### Cited Findings
- **Bentley E365**: 46% of ARR in 2025 (45% in 2024, 41% in 2023). ARR from contracts with consumption periods under one year: 51%. E365 is an "all-inclusive global consumption-based plan" charged on daily usage, with floors and ceilings — [Bentley 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1031308/000103130826000007/bsy-20251231.htm). Q3 2026: ARR US$1.583B, +13% at constant currency; net retention 110% — [Bentley](https://www.bentley.com/en/news/bentley-systems-announces-third-quarter-2026-results/).
- **Autodesk**: enterprise agreements were "roughly 15%" of revenue and pure usage, "largely Flex", "roughly 2%", about 17% in FY2025, with FY2026 "roughly similar" — [Motley Fool, 26 Feb 2026](https://www.fool.com/earnings/call-transcripts/2026/02/26/autodesk-adsk-q4-2026-earnings-call-transcript). Flex charges a daily rate per product — [Autodesk](https://www.autodesk.com/benefits/flex). A token lists at about US$3.00, falling to US$2.40 at volume (third-party) — [Redress Compliance](https://redresscompliance.com/autodesk-flex-token-pricing-guide).
- **Altair Units** (now Siemens): "Customers purchase a pool of sharable Altair Units", covering "more than 180 Altair and partner products". Units "return to the pool after use"; the model is value-based (a user draws only for the most valuable product in use) — [Siemens](https://www.siemens.com/en-us/company/about/businesses/digital-industries/altair/altair-units/). No Simcenter products are listed.
- **MSC One** (part of the Hexagon D&E business, which Cadence took over on 23 Feb 2026): a token pool deducted at launch and returned afterwards, covering Nastran, Adams, Marc, Apex, scFlow and others — [Cadence](https://www.cadence.com/en_US/home/tools/msc-software/mscone.html), [Cadence 10-Q](https://www.sec.gov/Archives/edgar/data/813672/000081367226000121/cdns-20260930.htm).
- **Ansys Elastic**: a "flexible, pay-per-use licensing model" for software, compute and cloud hardware — [Ansys](https://ansys.synopsys.com/it-solutions/licensing).
- **Cloud-native vendors.**
  - SimScale: per-user plans with core-hour quotas ("CPU/GPU"): Community 2,000, Mechanical 3,000, Professional 10,000, Enterprise custom. "overage use will be billed monthly"; Physics AI is optional or included; the Engineering AI agent is Enterprise-only at a custom price — [SimScale](https://www.simscale.com/product/pricing/).
  - Flexcompute Flow360: "Flexible, usage-based pricing" — [Flexcompute](https://www.flexcompute.com/flow360/).
- **GPU counting, Ansys 2026 R1.** A GCU is the GPU's streaming multiprocessor ("In NVIDIA GPU cards these are called Streaming Multiprocessors"). Rules:
  - Fluent: 40 included, then "1 per GCU". Lumerical: 4 included, then 1 per GCU. Rocky: 112 included. Speos: 16 included, then 1 per 4 GCUs.
  - HFSS and Icepak: "8 per GPU". Mechanical APDL: 1 per GPU, and GPUs may use at most 50% of HPC tasks.
  - Source: [Ansys help](https://ansyshelp.ansys.com/public/Views/Secured/corp/v261/en/licensing/HPC_detail.html).
  - A reseller says one RTX 4090 running Fluent's GPU solver needs 3 HPC Packs — [DRD](https://www.drd.com/blog/what-are-licensing-requirements-for-ansys-gpu-solvers-blog/).
- **Cadence** (10-Q): 79% recurring; some licences let customers "remix among software products" — [10-Q](https://www.sec.gov/Archives/edgar/data/813672/000081367226000121/cdns-20260930.htm).
- **Synopsys** Q3 FY2026: time-based US$1.003B, up-front US$0.665B, maintenance and service US$0.809B — [10-Q](https://www.sec.gov/Archives/edgar/data/883241/000088324126000025/snps-20260731.htm).

### Inferences
- Per-SM counting keeps vendor revenue intact through the move to GPUs: a GPU with about 130 SMs counts like about 130 cores in Fluent (my arithmetic).
- Even cloud-native SimScale pairs seats with metered compute, a hybrid model rather than pure usage pricing.

### Gaps
- Dassault SIMULIA token or credit rules and STAR-CCM+ GPU licensing not verified.
- The revenue share of Altair Units, Ansys Elastic and FlexEDA is not disclosed.

## C2. What managements said in 2025-26 about agents, seats and monetisation

### Takeaway
Every large vendor says agents will raise usage. Each is adding meters or surcharges while keeping seat or user subscriptions. None reports losing seats to agents, and none has introduced result-based pricing in simulation.

### Cited Findings
- **Synopsys** (Investor Day, 30 Sep 2026): "subscription and consumption-based models across tools, agents and platform"; FY2027 revenue US$11.10-11.20B (about +15%); about 15% CAGR to FY2030; GPT-Synopsys built with OpenAI — [Finviz/PR Newswire](https://finviz.com/news/397287/synopsys-details-growth-strategy-and-long-term-financial-model-at-2026-investor-day).
- **Cadence** (26 Oct 2026), source [Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/10/26/cadence-cdns-q3-2026-earnings-call-transcript/):
  - CFO Wall: "we believe that Agentic AI is a demand accelerator for EDA". Agents "could perform much more design exploration than an individual engineer calling our underlying engines repeatedly". "greater customer usage should create greater value for Cadence".
  - CEO Devgan: recurring revenue grew 18%, partly on agentic AI "driving more usage of our base tools"; "we are always looking at different kinds of business models".
  - Growth: core EDA +20%, SD&A +30%. No agent pricing disclosed.
- **Siemens** (Q4 FY2026 call, Nov 2026), source [Investing.com](https://in.investing.com/news/stock-market-news/earnings-call-transcript-siemens-posts-record-orders-in-q4-2026-as-growth-quickens-93CH-5698664):
  - CFO Bienert: keeps "the existing user-based, named user subscription foundation"; adds AI subscription fees; "we will introduce an agentic surcharge"; credit- or usage-based models may follow.
  - The Eigen agent is "license fee-based".
  - AI is about 5% of DI software (about €350M); ARR +12%.
- **Dassault** (Q3 2026 call, Oct 2026): the agentic platform "remains user-based, covering both humans and agents", with usage also measured in units of work and token consumption. Subscription is about half of ARR — [Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-dassault-systemes-beats-q3-2026-estimates-shares-fall-93CH-4978361).
- **Autodesk** (26 Feb 2026), CEO Anagnost, source [Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/02/26/autodesk-adsk-q4-2026-earnings-call-transcript):
  - "capturing shared value through subscription, consumption, and outcome-based business models".
  - API monetisation "specifically targeting machine usage of our IP", but "there are not a lot of customers doing that yet".
  - "we absolutely want fewer people per project because we want our customers executing more projects"; "we do not expect seats to go away anytime soon"; "That seat is going to get more valuable".
- **Keysight** (6 Oct 2026): ADS 2027 adds MCP servers so customers' own LLM agents can drive ADS, with Keysight simulation validating the output; no licensing change — [Keysight](https://www.keysight.com/us/en/about/newsroom/catalog/news-release.2026.1006_pr26-095-keysight-advances-its-design-software-with-agentic-ai.html).
- **Schneider/PTC** (5 Oct 2026): about €22B cash for PTC (CY2025 revenue €2.4B; adjusted EBITA about 40%; about 10% a year expected through 2029) — [PTC 8-K exhibit](https://www.sec.gov/Archives/edgar/data/857005/000119312526413124/d174191dex991.htm).

### Inferences
- **Said**: agents will raise consumption.
- **Done**: surcharges and token meters on top of seats; Autodesk's API metering is live but small. Cadence's "more usage of our base tools" is the only claim linked to reported revenue, and it is not quantified.

### Gaps
- No quantified agent-driven licence consumption anywhere.
- PTC's and Bentley's own call statements on agents were not retrieved.

## C3. Customer-side evidence

### Takeaway
The evidence is thin and mostly from vendors. Agents and surrogates let customers explore far more designs. No independent evidence was found that licence cost is the bottleneck, or of large-scale moves to open-source codes on cloud GPUs.

### Cited Findings
- **Throughput claims** (unconfirmed):
  - iPronics: a sweep cut from about 9 days to 18 h (A2).
  - Flexcompute: "thousands of design variants overnight" — [NVIDIA](https://blogs.nvidia.com/blog/industrial-software-leaders-secure-autonomous-ai-engineers-nemoclaw).
  - Rescale: "thousands" of iterations instead of "a few dozen manual studies" — [Rescale](https://rescale.com/news/rescale-introduces-agentic-digital-engineering/).
  - Northrop/Luminary: "thousands of design options" — [NVIDIA](https://blogs.nvidia.com/blog/ai-physics-aerospace-automotive-design-engineering).
- **Costs and bottlenecks**:
  - RT Insights (Jul 2026) argues licence fees are usually the smallest total-cost item next to engineering time — [RT Insights](https://www.rtinsights.com/open-source-isnt-free-a-guide-to-real-tco-in-ai-accelerated-simulation/).
  - SimScale's own survey (2026) found fully autonomous agents in about 10% of organisations — [SimScale](https://www.simscale.com/blog/agentic-engineering-reshaping-simulation-driven-product-design/).
- **Open-source route**:
  - OpenFOAM carries no licence fee, but end-to-end GPU support is immature; mainly the linear solver is offloaded (PETSc4FOAM, AmgX) — [Hivenet](https://www.hivenet.com/post/openfoam-gpu-state-of-play).
  - Rescale's June 2026 initiative brings DOE lab codes to industry (details unverified; page blocked) — [Rescale](https://rescale.com/news/rescale-us-national-labs-initiative-doe-simulation-codes/).

### Inferences
- If agents multiply runs while vendors license per SM or core and add agent surcharges, licence spend per engineer rises. That raises the incentive to substitute open or government codes, and immature GPU support in open codes slows that substitution.

### Gaps
- No independent survey of licence cost as a constraint was found.
- No quantified case was found of a company moving certified work to open codes on GPUs.

## C4. Testing the priors

### Takeaway
The 70% prior (the large vendors keep growing through 2029) is supported. The 50% prior (seat-priced front-end tools lose pricing power after 2029) is neither confirmed nor refuted: vendors' hedging is consistent with it, but 2026 results and the PTC price argue against near-term erosion.

### Cited Findings
- **Supporting growth**:
  - Synopsys: about 15% CAGR target (C2).
  - Cadence: core EDA +20%, SD&A +30% (C2).
  - Siemens: DI software guided to double-digit growth in FY2027 — [Investing.com](https://in.investing.com/news/stock-market-news/earnings-call-transcript-siemens-posts-record-orders-in-q4-2026-as-growth-quickens-93CH-5698664).
  - Bentley: ARR +13% (C1).
  - PTC: buyer underwrites about 10% a year (C2).
- **Contradicting or cautionary**:
  - Dassault: 2026 growth guided to only 4-5%; Americas -3% in Q3 — [Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-dassault-systemes-beats-q3-2026-estimates-shares-fall-93CH-4978361).
  - Autodesk: RPO +2% in Q2 FY2027 — [Autodesk](https://adsknews.autodesk.com/en/?p=59775).
  - Kimi K3: an autonomous 48-hour chip flow on open-source EDA at 45nm (17 Jul 2026), after which Cadence fell 9.47% that day — [TIKR](https://www.tikr.com/blog/cadence-stock-fell-9-in-a-day-on-a-chinese-ai-chip-demo-heres-where-the-stock-could-go-in-2026).
- **Consistent with the seat-pricing prior**: Siemens' agentic surcharge; Dassault counting agents as users; Autodesk's "fewer people per project" and metering of machine API use (C2).

### Inferences
- Vendors are moving to protect value as seat counts decouple from work. Where usage meters already dominate (Bentley), growth is healthy. The open question is whether the meters keep pace with agent productivity after 2029. Evidence so far is management intent, not results.

### Gaps
- No vendor discloses seat counts, price per seat, or usage per seat.

## Consolidated: could not verify, and dated source list

### Takeaway
The largest gaps are the independents' financials and any quantified evidence that agents drive licence consumption.

### Cited Findings
- **Filings**:
  - NVIDIA: 10-K FY2026 (Feb 2026); 10-Q Q2 FY2027 (26 Aug 2026).
  - Synopsys: 10-K FY2025 (22 Dec 2025); 10-Q Q3 FY2026 (26 Aug 2026).
  - Cadence: 10-Q Q3 2026 (28 Oct 2026).
  - Bentley: 10-K FY2025 (26 Feb 2026).
  - PTC: 8-K exhibit (Oct 2026).
- **Company sources**:
  - NVIDIA: blogs and releases (17 Nov 2025; 26 Jan, 16 Mar, 2 Jun, 22 Jun 2026); spec pages; Omniverse FAQ; AI Enterprise guide (2 Sep 2026); cuDSS licence (v. Feb 2022); blueprint page (13 Feb 2026).
  - Synopsys (27 Jul, 30 Sep, 21 Oct 2026); Rescale (May-Nov 2026); SimScale (2025-26; pricing page accessed 12 Nov 2026); Keysight (6 Oct 2026); Autodesk (27 Aug 2026); Bentley (5 Nov 2026); Ansys help (2026 R1); Siemens Altair Units page.
- **Transcripts**: Autodesk (26 Feb 2026); Cadence (26 Oct 2026); Dassault (Oct 2026); Siemens (Nov 2026).
- **Trade and secondary press**: The Register (18 Jan 2026); Digital Engineering (10 Feb, 15 May 2026); The Next Web (28 Aug 2026); insideHPC (Apr 2025); Tech.eu (Jan 2020, older); Caiwen (Oct 2026); TOP500 (Jun 2026); Exxact; aggregators (CB Insights, Multiples.vc, PitchBook), all labelled where used.

### Inferences
- Lines resting only on a vendor or an aggregator are labelled as such in place.

### Gaps
- Apollo release.
- Q2 FY2027 revenue concentration (SEC blocked an anonymous download).
- Rescale and SimScale revenue, margins and valuation.
- Gompute's acquisition by Advania (single secondary source).
- Eviden/Nimbix, TotalCAE, Parallel Works.
- Dassault SIMULIA tokens; STAR-CCM+ GPU licensing.
- Baidu and Alibaba offerings.
- Revenue share of Altair Units, Ansys Elastic and FlexEDA.
- Quantified agent-driven consumption.
- The WebSearch budget ran out mid-task; the tool's notice asked not to work around it, so later checks used direct page fetches only.
