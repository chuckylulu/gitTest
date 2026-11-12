# Siemens (DI Software incl. Altair and Siemens EDA) and Dassault Systemes (SIMULIA, BIOVIA): business quality and forward path, as of 12 Nov 2026

Scope note: business facts only; no share prices or valuation multiples. "Company claim, unconfirmed" marks statements no outside party has confirmed. WebSearch budget ran out midway on 12 Nov 2026; later items came from direct fetches of known URLs and primary PDFs (Siemens and Dassault releases, Altair 10-K on SEC EDGAR, CST GPU guide).

## 0. Summary for the report writer

### Takeaway
- Siemens published FY2026 (to 30 Sep 2026) on 12 Nov 2026. DI software revenue ~EUR 7.2bn (+13% comparable), ARR EUR 6.1bn (+12%), led by EDA. Software is ~37% of Digital Industries and ~8.6% of the group. Simulation and EDA are not reported separately. SemiAnalysis puts Siemens EDA at USD 2.2-2.5bn (under 5% of Siemens). Altair had USD 666m revenue in 2024. DI margin was 19.1% (before PPA amortisation), but return on DI capital roughly halved after Altair/Dotmatics. Group industrial net debt/EBITDA was 0.3x.
- Siemens' strongest "judge" is Calibre. SemiAnalysis (May 2026) gives it an 85%+ share of physical verification and says TSMC, Samsung and Intel require "Calibre-clean" DRC/LVS. TSMC certified Calibre for A14 (Sep 2026) and Samsung "fully qualified" it (May 2026). The evidence that Simcenter/Altair are sign-off judges is much weaker (vendor material only).
- Siemens GPU lithography (14 Oct 2026, Calibre + NVIDIA cuLitho): "up to 12x" full-chip OPC and "at least 10x to 17x" on key simulation workloads. No hardware baseline, accuracy-equivalence data, customer confirmation or availability date was given. This is a company claim, unconfirmed.
- Siemens pricing: CFO says the named-user subscription stays, AI comes as add-on fees, and an "agentic surcharge" is planned; credits/usage may follow. Altair Units (pooled, value-based) already exist. Siemens is retiring the OpenRadioss website for a "managed shared source" model, and the GitHub repo was not found on 12 Nov 2026. That is a step back from open source.
- Dassault FY2025: revenue EUR 6.24bn (+4% cc, low end after an Oct-2025 cut from 6-8%). Non-IFRS margin 32.0% vs IFRS 21.7%; net cash EUR 1.53bn; R&D 21% of revenue; recurring 82% of software. In 2026 growth recovered to 5% in Q3 and the FY guide was raised to 4-5%. SIMULIA is not disclosed; it sits in Industrial Innovation (EUR 3.13bn, 56% of software) and is cited as a growth contributor. Charles left as chairman (Feb 2026); Daloz is chairman and CEO; CMD is on 17 Nov 2026.
- Dassault AI: Virtual Companions and 3D UNIV+RSES. The agentic platform stays "user-based" for humans and agents, with units of work and tokens measured. First meaningful revenue is expected in 2027 (company statements). SIMULIA already sells SimUnit tokens/credits; CST needs FP64-class GPUs. Regulator evidence is mostly old or vendor-sourced: the FDA Living Heart collaboration (2019), the Medidata SCA precedent (2020), and PowerFLOW WLTP claims.
- Priors: the 70% "vendors keep growing" prior fits Siemens (double-digit software, FY2027 guide) better than Dassault (repeated cuts, EPS-doubling target moved to 2029). For the 50% "seat-priced front ends lose pricing power" prior, there is no price-erosion evidence yet. Both vendors are pre-emptively adding agent and token fees, which suggests they see the risk.

## A1. Siemens: scope, size and financials of the software business

### Takeaway
Software is a fast-growing but minority part of a EUR 83bn conglomerate. EDA drove FY2026 software growth. The simulation/EDA split is not disclosed, and outside estimates exist only for EDA.

### Cited Findings
- DI FY2026: orders EUR 20,880m (+12% comp); revenue EUR 19,677m (+9% comp); profit EUR 3,753m; margin 19.1% (FY2025 14.9%); net capital employed (NCE) EUR 23,320m; FCF EUR 3,982m. Amortisation of acquired intangibles was EUR 451m (FY2025 281m), so EBIT was EUR 3,302m. Q4 DI software revenue EUR 2,144m (+12% comp; Q4 FY2025 EUR 1,900m); "Revenue growth in the software business was led by the EDA business". Software orders included large PLM and EDA contracts. Q4 Altair/Dotmatics integration cost was EUR 36m (-0.6pt margin). — [Siemens Earnings Release Q4 FY2026, 12 Nov 2026](https://assets.new.siemens.com/siemens/assets/api/uuid:11b1a70b-f540-45bb-824f-0b3fbb927e1b/dHQCOPR202611097494EN.pdf)
- FY2026 DI software revenue EUR 7.2bn (+13% comp); ARR EUR 6.1bn (+12%); digital business EUR 10.9bn (+16%) — [Siemens press release, 12 Nov 2026](https://press.siemens.com/global/en/pressrelease/outstanding-fiscal-2026-performance-industrial-ai-drive-future-growth)
- Quarterly path: Q2 software EUR 1.6bn (+14%), organic ARR EUR 5.5bn (+11%) — [Siemens, 13 May 2026](https://press.siemens.com/global/en/pressrelease/siemens-continues-path-profitable-growth). Q3 software EUR 1.8bn (+15%), ARR EUR 5.7bn (+11%) — [Siemens, 6 Aug 2026](https://press.siemens.com/global/en/pressrelease/record-third-quarter-outlook-raised). Q3 growth was "driven largely by EDA (+30%+)" — [Schnitger Corp, 26 Aug 2026](https://schnitgercorp.com/2026/08/26/plmish-earnings-check-what-have-we-learned/)
- Q4 FY2025: software +8% (PLM +11%, EDA +3% "on tough comps"). Cloud ARR was EUR 2.3bn, "close to 50 percent" of ARR excluding Altair/Dotmatics (target was 40%). Integration was expected to cost ~120bp of DI margin in FY2026 — [CFO speech, Siemens CMD, 13 Nov 2025](https://assets.new.siemens.com/siemens/assets/api/uuid:74aedb6a-c07d-472b-a6a5-07832e3804ff/ONE%20Tech%20-%20Speech%20Ralf%20P.%20Thomas_CFO_EN.pdf)
- Nov 2025: ARR EUR 5.3bn; 24,000 SaaS customers (70% new, ~90% SMEs); target to double digital business by 2030; EUR 1bn AI investment over 3 years; 1,500 AI experts — [Siemens press release, 13 Nov 2025](https://assets.new.siemens.com/siemens/assets/api/uuid:4f2a7444-211a-4f8c-b01c-16f4e4cbe3b9/251113-press-release-en.pdf)
- Call, 12 Nov 2026 (AI-assisted transcript; quotes approximate):
  - CFO Bienert: "In software, the SaaS transition has now been completed". Q4 software orders were a record EUR 2.9bn. FY2027 is "a strong renewal year for our EDA business", with the funnel concentrated in Q4.
  - CEO Busch: the software market is growing ~10%. AI is "trending to around 5% of DI software" (~EUR 350m; company claim, unconfirmed). Altair met its FY2026 revenue targets, with "first revenue synergies".
  - Source: [Investing.com transcript, 12 Nov 2026](https://in.investing.com/news/stock-market-news/earnings-call-transcript-siemens-posts-record-orders-in-q4-2026-as-growth-quickens-93CH-5698664)
- DI backlog was EUR 11.0bn, of which EUR 7.3bn software — [Investing.com slides summary, 12 Nov 2026](https://in.investing.com/news/stock-market-news/siemens-fy26-slides-industrial-ai-drives-record-orders-raised-targets-93CH-5698681) (AI-generated article)
- Outlook FY2027: DI +8-12% comparable revenue, margin 20-22%; "double-digit growth in software will lead". Q1 FY2027 software is expected to grow only "moderately" — release and call above.
- Siemens EDA revenue is estimated at USD 2.2-2.5bn in CY2025. "EDA is under 5% of Siemens revenue", and EDA R&D intensity is estimated at 25-28% (vs 34% Synopsys, 30% Cadence) — [SemiAnalysis EDA primer, 21 May 2026](https://newsletter.semianalysis.com/p/eda-market-primer) (paywalled preview)
- Altair FY2024 (last 10-K):
  - Revenue USD 665.8m.
  - Term licences USD 388.8m, perpetual USD 46.5m, maintenance USD 164.4m, software-related services USD 25.4m, client engineering services USD 25.0m.
  - R&D USD 221.2m (33%); adj. EBITDA USD 149.9m; FCF USD 140.0m; net income USD 14.2m.
  - Source: [Altair 10-K, filed 20 Feb 2025](https://www.sec.gov/Archives/edgar/data/1701732/000095017025024197/altr-20241231.htm)
- My calculations: software = ~37% of DI revenue and ~8.6% of group revenue (EUR 83.4bn). EDA = ~2.3-2.6% of group at ~1.15 USD/EUR. Altair (2024) was ~0.7% of Siemens FY2026 revenue.

### Inferences
- PLM + simulation + MES + low-code + Dotmatics is roughly EUR 5bn of the EUR 7.2bn. Simulation (Simcenter + Altair) is probably low single-digit % of group revenue. EDA's large, lumpy term renewals mean software growth will swing quarter to quarter.

### Gaps
- No disclosure, and no outside estimate found, for Simcenter or post-merger Altair revenue. No software-only margin is disclosed. Cloud ARR share including Altair/Dotmatics at FY2026 end is not disclosed.

## A2. Siemens: five quality tests

### Takeaway
Calibre is a genuine sign-off "judge" with outside confirmation. Simcenter/Altair look like strong but contestable tools with weaker sign-off evidence. Finances are robust at group level, but acquisitions diluted returns on capital.

### Cited Findings
- (a) Position, EDA:
  - SemiAnalysis: Calibre has an "85%+ share" in physical verification. "TSMC specifies 'Calibre-clean' DRC/LVS for tape-out", and Samsung and Intel do the same — [SemiAnalysis, 21 May 2026](https://newsletter.semianalysis.com/p/eda-market-primer)
  - Older outside-attributed figure: an all-node DRC share of ~72% for Mentor in 2016 (Gary Smith EDA, Dec 2017, shown on a Mentor slide). It is dated and vendor-relayed — [search summary of Siemens/Mentor material](https://semiengineering.com/calibre-evolves-constantly/)
  - Vendor blog: foundries "develop decks for Calibre before ... competing DRC tools" — [SemiEngineering sponsored post by Mentor, 11 May 2017](https://semiengineering.com/calibre-evolves-constantly/) (vendor-authored)
- TSMC (Sep 2026):
  - Calibre nmDRC/nmLVS/xACT/PERC certified for TSMC A14.
  - Solido certified for SPICE accuracy on N3C/A16/A14; mPower certified on N2P.
  - Calibre 3DThermal certified for 3DFabric and A16; CoWoS-L certification of Calibre 3DStack "underway".
  - TSMC's Aveek Sarkar is quoted.
  - Source: [Siemens release, 23 Sep 2026](https://news.siemens.com/en-us/siemens-tsmc-oip-ecosystem-forum-2026/)
- Samsung (May 2026):
  - Calibre nmDRC/nmLVS/PERC/xACT are "fully qualified for Samsung Foundry processes"; Aprisa is "fully certified".
  - Solido gained first automotive qualifications on 4nm and 2nm; Samsung adopted Siemens tools for its 2.3D Cube-E package.
  - A Samsung VP (Hyung-Ock Kim) is quoted.
  - Source: [Siemens release, 28 May 2026](https://news.siemens.com/en-us/siemens-safe-forum-2026/)
- NVIDIA's GTC release names Samsung and SK hynix as Calibre users for computational lithography and physical verification. The same release says JLR and Mercedes-Benz use STAR-CCM+ for GPU-accelerated engineering — [NVIDIA, 16 Mar 2026](https://nvidianews.nvidia.com/news/nvidia-and-global-industrial-software-giants-bring-design-engineering-and-manufacturing-into-the-ai-era)
- (b) Lead, EDA overall: TrendForce gives Synopsys 31%, Cadence 30%, Siemens 13% (2024); a 2025 forecast has Cadence 32%, Synopsys 30%, Siemens 13% — [TrendForce via search summary](https://www.trendforce.com/news/?p=48281)
- Lead, simulation:
  - CIMdata puts the S&A market at USD 11.67bn in 2025 (+8.5%, below its >USD 12bn forecast); vendor shares are paywalled — [CIMdata](https://www.cimdata.com/en/news/item/30365-cimdata-publishes-simulation-and-analysis-market-report)
  - CIMdata's 2025 report (covering 2024) profiled Altair among "market leaders" — [CIMdata store](https://www.cimdata.com/en/online-store/market-analysis-reports/product/351-2025-simulation-analysis-market-analysis-report)
  - Cambashi puts CAE at USD 11.6bn in 2025 — [Digital Engineering 24/7, 10 Feb 2026](https://www.digitalengineering247.com/article/gpu-acceleration-expands)
  - No third-party simulation share for Siemens was found.
- (c) Revenue model, Siemens:
  - ARR EUR 6.1bn ≈ 85% of software revenue (my calc).
  - The CFO describes "the existing user-based, named user subscription foundation" (call, 12 Nov 2026).
  - EDA renewals are lumpy term deals (call).
- Revenue model, Altair:
  - Recurring software licence rate was 93% in 2024, and perpetual licences were 7% of revenue.
  - Services were 7.6% of revenue (software-related plus client engineering; my calc).
  - Altair Units is a "patented units-based subscription licensing model" covering 150+ partner products — [Altair 10-K](https://www.sec.gov/Archives/edgar/data/1701732/000095017025024197/altr-20241231.htm)
  - Siemens' Altair Units page now says "more than 180 Altair and partner products". Units are "sharable", "return to the pool after use", and are drawn only for "the most valuable product" — [Siemens Altair Units page, live 12 Nov 2026](https://www.siemens.com/en-us/company/about/businesses/digital-industries/altair/altair-units/)
- (d) Financial strength:
  - Group FY2026: revenue EUR 83,372m; Industrial Business profit EUR 13,292m (16.3%); FCF EUR 12.1bn; R&D EUR 6,909m (8.3% of revenue, my calc).
  - Industrial net debt was EUR 4,782m (0.3x EBITDA), down from EUR 12,160m (0.9x) a year earlier. ROCE was 14.1% (FY2025 17.8%; target band 15-20%).
  - China revenue was EUR 7,426m (8.9% of group, +5% comp).
  - Source: [Earnings Release Q4 FY2026](https://assets.new.siemens.com/siemens/assets/api/uuid:11b1a70b-f540-45bb-824f-0b3fbb927e1b/dHQCOPR202611097494EN.pdf)
- DI NCE rose from EUR 10,476m (Sep 2024) to EUR 22,885m (Sep 2025) on Altair/Dotmatics. Dotmatics cash outflow was EUR 4.2bn — [Earnings Release Q4 FY2025, 13 Nov 2025](https://assets.new.siemens.com/siemens/assets/api/uuid:3948cdd4-35e0-4c1d-8412-9aed4097b3d0/HQCOPR202511117277EN.pdf)
- Altair price: USD 113/share, EV ~USD 10bn, closed 26 Mar 2025 — [Siemens, 26 Mar 2025](https://news.siemens.com/en-us/siemens-altair-engineering-closing/); [design-reuse copy of 30 Oct 2024 announcement](https://design-reuse.com/news/57011/siemens-saltair-engineering-acquisition.html). A USD 10.5bn bridge loan was arranged — [BNN Bloomberg, 26 Nov 2024](https://bnnbloomberg.ca/investing/2024/11/26/siemens-secures-105-billion-bridge-loan-for-altair-buyout)
- Concentration: at Altair, no customer exceeded 2% of 2024 software billings. Billings were Americas 32%, EMEA 31%, APAC 37%; US revenue was 49% — [Altair 10-K](https://www.sec.gov/Archives/edgar/data/1701732/000095017025024197/altr-20241231.htm). Siemens does not disclose DI customer concentration.
- (e) Export controls: the US required licences for EDA exports to China from late May 2025; Siemens said the industry was informed on 23 May — [The Register, 30 May 2025](https://www.theregister.com/2025/05/30/eda_us_china/). The curbs were rescinded in early July 2025, and Siemens, Synopsys and Cadence resumed sales — [Business Standard, 3 Jul 2025](https://www.business-standard.com/world-news/us-rolls-back-chip-software-export-curbs-china-siemens-synopsys-cadence-resume-ops-125070300801_1.html)
- No new 2026 EDA-specific BIS rule was found (China-strand digest search, 12 Nov 2026). Synopsys' China share fell from 16% (FY24) to 12% (FY25) as barred customers turned to local EDA — [SemiAnalysis](https://newsletter.semianalysis.com/p/eda-market-primer)
- Cycle: in China, DI order intake was +8% in Q4 and local-for-local revenue +25% in FY2026 (call). Automation recovered after the FY2025 severance programme, and Q4 DI orders were +15% (release).

### Inferences
- **Provisional assessment, (a) Position:** owns a judge in Calibre (foundry-mandated physical verification) and near-judge positions in Solido SPICE, mPower and 3DThermal. Simcenter/Altair solvers are respected but not shown here to be mandated sign-off tools. HyperMesh-type pre-processing is a gap-filler exposed to agents.
- **Provisional assessment, (b) Lead:** strong, outside-confirmed lead in physical verification. In EDA overall Siemens is a distant #3 (~13%). In simulation, the lead is plausible but unquantified.
- **Provisional assessment, (c) Revenue model:** mostly recurring. Named-user seats remain the core metric, while Altair Units and EDA term licences scale more with usage and compute. Services exposure is small, but Siemens group hardware exposure is large outside software.
- **Provisional assessment, (d) Financial strength:** very strong group (0.3x leverage, EUR 12bn FCF). DI pre-tax return on NCE fell from ~33% (FY2024) to ~16% (FY2026) after the acquisitions (my calc from the releases).
- **Provisional assessment, (e) Resilience:**
  - Steady scenario: favourable. AI chips, 3D-IC thermal sign-off and High-NA OPC compute support EDA, and SI/DI also sell into data centres.
  - Financing-led pause (~2028): EDA renewals and data-centre hardware would both soften. The group balance sheet cushions this.
  - Faster acceleration: Calibre gains from more tape-outs. Seat-based front ends are pressured.
  - Export-control risk is concentrated in US-domiciled Siemens EDA; the 2025 episode showed licences can be imposed at days' notice.

### Gaps
- No Intel Foundry certification document was retrieved (SemiAnalysis asserts Calibre-clean at Intel). No third-party OPC share was found (the search budget was exhausted). Siemens EDA's China revenue share is not disclosed.

## A3. Siemens: six transitions (said vs done)

### Takeaway
GPU and agent work is shipped in parts and well funded. Pricing stays seat-based with planned surcharges. On open source Siemens is retreating, not adapting.

### Cited Findings
- (1) Seats to use/result:
  - SAID: named-user subscription "we continue"; human-led AI via add-on AI subscription fees; "we plan and we will introduce an agentic surcharge"; credit/usage models may follow; the Eigen agent is "license fee-based" (call, 12 Nov 2026). In Aug 2026, Busch said Siemens "isn't tokenizing software yet" — [Schnitger, 26 Aug 2026](https://schnitgercorp.com/2026/08/26/plmish-earnings-check-what-have-we-learned/)
  - DONE: Altair Units pooled/value-based licensing continues under Siemens (page above). No outcome-based pricing was found.
  - Contrast: Synopsys prices GPU CFD "on the speedup delivered" — [Schnitger, 16 Sep 2026](https://schnitgercorp.com/2026/09/16/cae-earnings-recap-no-hallucinations-here/)
- (2) CPU to GPU / low precision:
  - SAID: Siemens will "complete GPU acceleration across its entire simulation portfolio", and EDA targets "2-10x speedups in key workflows" (verification, layout, process optimisation). No dates or money were given — [NVIDIA/Siemens, 6 Jan 2026](https://nvidianews.nvidia.com/news/siemens-and-nvidia-expand-partnership-industrial-ai-operating-system)
  - DONE (STAR-CCM+ 2602): GPU-native multiphase solvers (VOF, MMP, phase change) and better multi-GPU scaling. A reseller case ran on 2 A100s in ~9 min vs 80 Xeon cores in ~46 min — [Siemens blog, Feb 2026](https://blogs.sw.siemens.com/simcenter/simcenter-star-ccm-2602-released/); [Volupe](https://volupe.com/?p=28840)
  - DONE (STAR-CCM+ 2606): multi-GPU PhysicsAI training and a GPU Lagrangian/spray solver (same search, Siemens blog).
  - DONE (Altair): Altair CFD/EDEM ran 5-6x faster scaling from 1 to 8 GPUs on Azure — [DE247, 10 Feb 2026](https://www.digitalengineering247.com/article/gpu-acceleration-expands)
  - DONE (Calibre rasterizer): the Calibre GPU rasterizer is up to 290x (Manhattan) and 45x (curvilinear) faster than optimised CPU code on H100, with <1% absolute error, and "Siemens EDA's GPU-powered OPC solution is available now". Company claim, unconfirmed — [Calibre blog, 13 Apr 2026](https://blogs.sw.siemens.com/calibre/2026/04/13/why-a-gpu-rasterizer-matters-for-computational-lithography-in-both-performance-and-precision-at-scale/)
- The October 2026 lithography statement:
  - What was announced: Calibre + NVIDIA cuLitho, "up to 12x acceleration for full-chip optical proximity correction (OPC)", and "Verified engineering data supports simulation speed-ups ranging from at least 10x to 17x for key workloads". The release names no Calibre module, CPU/GPU baseline, accuracy-equivalence data, customer or GA date — [Siemens, 14 Oct 2026](https://news.siemens.com/en-us/siemens-calibre-nvidia-culitho/); [Calibre blog, 14 Oct 2026](https://blogs.sw.siemens.com/calibre/2026/10/14/the-virtuous-cycle-of-silicon-how-siemens-is-accelerating-the-era-of-physical-ai-with-nvidia-culitho/)
  - NVIDIA repeats "up to 17x" — [NVIDIA blog, 3 Nov 2026](https://blogs.nvidia.com/blog/ai-semiconductor-fabs/)
  - Trade press only relays the claims; no independent commentary — [Engineering.com, 23 Oct 2026](https://www.engineering.com/siemens-and-nvidia-accelerate-computational-lithography/)
  - Customer confirmation: none found.
- (3) Agents via programming interfaces:
  - Eigen Engineering Agent (automation engineering, TIA Portal): GA at Hannover Messe on 20 Apr 2026, piloted with 100+ companies in 19 countries; available in China from 18 Jul 2026. Claimed 2-5x faster workflows (company claim, unconfirmed) — [CIMdata summary](https://www.cimdata.com/en/industry-summary-articles/item/29883-siemens-launches-the-eigen-engineering-agent-bringing-purpose-built-ai-to-industrial-automation-engineering); [ARC, Jul 2026](https://www.arcweb.com/blog/industrial-ai-comes-reality-siemens-eigen-engineering-agent-makes-china-debut-waic-2026)
  - Fuse EDA AI Agent: agents "continuously validate decisions against deterministic, physics-based EDA engines". Capabilities ship "in forthcoming releases"; no pricing and no API/MCP detail. STMicro is quoted on Solido Layout Analyzer — [Siemens, 26 Jul 2026](https://news.siemens.com/en-us/siemens-nvidia-dac-2026/)
  - At DAC 2025 Siemens launched Aprisa AI, Calibre Vision AI and Solido AI — [SemiAnalysis](https://newsletter.semianalysis.com/p/eda-market-primer)
  - TSMC collaborations on an AI DRC-fix flow (Calibre + Aprisa AI + Solido Fuse) — TSMC release above.
- (4) Open source:
  - Altair open-sourced Radioss as OpenRadioss in 2022.
  - The Siemens page now says "The OpenRadioss website is being retired". Future R&D moves to a "managed 'Shared Source' environment", and visitors are pointed to "Simcenter Radioss, our flagship commercial solution" — [Siemens transition page, live 12 Nov 2026](https://www.siemens.com/en-us/products/simcenter/mechanical-simulation/radioss/rd/)
  - On 12 Nov 2026, github.com/OpenRadioss/OpenRadioss returned 404 to WebFetch, and the repository attach tool reported it "not found ... or [no] access".
  - Separately, Siemens bought Precision Innovations (Jul 2026), which Schnitger tentatively links to the open-source OpenROAD framework (her hedge: "not [an] EDA person") — [Schnitger, 20 Jul 2026](https://schnitgercorp.com/2026/07/20/siemens-to-acquire-precision-innovations-for-ai-powered-chip-planning/)
- (5) Learned models inside solvers:
  - Simcenter PhysicsAI (geometric deep learning on mesh/CAD) claims "up to 1000x faster". Kinetic Vision reports "up to 4,000x faster than traditional FEA at up to 97.5% accuracy" (vendor-hosted customer claim).
  - Siemens' own guidance: "critical designs should still be validated with a traditional CAE, CFD solver"; a similarity check flags out-of-distribution designs — [Siemens PhysicsAI page, live 12 Nov 2026](https://www.siemens.com/en-us/products/simcenter/engineering-data-science-ai/physicsai/)
  - Jul 2026 release: "the first to bring together Siemens and Altair simulation technologies in a unified simulation portfolio", adding PhysicsAI Generate and Intelligence Center X — [HPCwire copy of Siemens release, 29 Jul 2026](https://www.hpcwire.com/off-the-wire/siemens-accelerates-engineering-simulation-with-a-unified-ai-powered-simcenter-portfolio/)
- (6) Acceptance by regulators and customers' sign-off: foundry acceptance of Calibre is documented (A2). No regulator document naming Simcenter/Altair for automotive or aerospace certification was found.
- Funding and M&A:
  - Altair: ~USD 10bn.
  - Dotmatics: EUR 4.2bn cash.
  - 2026 EDA bolt-ons Precision Innovations (20 Jul) and Defacto (21 Jul): terms undisclosed — [Schnitger, 21 Jul 2026](https://schnitgercorp.com/2026/07/21/2-days-2-deals-siemens-to-acquire-defacto-technologies/)
  - Lauterbach (TRACE32 debug/trace): signed 10 Nov 2026; ~EUR 60m revenue (2025), ~170 staff; price undisclosed; close in H1 2027 — [Siemens, 10 Nov 2026](https://press.siemens.com/global/en/pressrelease/siemens-expand-portfolio-semiconductor-design-and-verification-planned-acquisition)
  - Group R&D was EUR 6.9bn. "Hundreds of industrial AI experts" were committed to NVIDIA work (Jan 2026 release).

### Inferences
- (1) Defensive. Surcharges on top of seats preserve revenue only if agent usage stays tied to licensed users. Altair Units is a ready consumption mechanism Siemens could scale. Timing is plausible; the plan is not yet priced.
- (2) Funded and partly shipped (CFD, DEM, OPC rasterizer). Sign-off use needs proof that GPU output matches golden CPU results, plus foundry requalification. Neither is published for the cuLitho claims. Nothing indicates sign-off solvers moving to low-precision AI arithmetic.
- (3) Shipped where Siemens owns the workflow (TIA Portal, EDA). Interface openness to third-party agents is undocumented, so ease-of-use moats are exposed if outside agents can drive the solvers directly.
- (4) Retreat from an open-source solver. This protects commercial Radioss pricing but cedes community goodwill. AGPL code already released can still be forked (inference).
- (5) Reasonable design: AI surrogates sit beside solvers, and the solver remains the judge.
- What must go right: Calibre GPU results requalified at TSMC/Samsung/Intel; agent surcharges accepted by customers; Altair integration synergies; no new EDA export curbs.

### Gaps
- No GA date or customer confirmation for cuLitho-in-Calibre. No Simcenter Nastran or Calibre DRC GPU status was found. The PhysicsX partnership and Simcenter X licensing were not verified (search budget exhausted). The exact date OpenRadioss closed is unknown.

## B1. Dassault Systemes: financials, mix, guidance and management

### Takeaway
A high-margin, net-cash, ~83% recurring business. Growth fell to 3-5% in 2025-26 and has started to re-accelerate. SIMULIA and BIOVIA sizes are undisclosed.

### Cited Findings
- FY2025 (published 11 Feb 2026):
  - Revenue EUR 6,235.8m (+4% cc); software EUR 5,641m.
  - Subscription & support EUR 4,624m (+6%); recurring 82% of software (80% in 2024); licences & other EUR 1,020.7m (-6%); services EUR 594.7m (+2%; 9.5% of revenue).
  - Software by line: Industrial Innovation EUR 3.13bn (+6%, 56%; "CATIA, SIMULIA and ENOVIA were the strongest contributors"); Life Sciences EUR 1.08bn (-2%, 19%); Mainstream EUR 1.43bn (+2%, 25%).
  - Geography: Americas 39% (+5%), Europe 38% (+2%), Asia 22% (+5%). Q4 had "softness in China" and Q4 Life Sciences was -4% as "MEDIDATA continued to face headwinds".
  - Margins: non-IFRS operating margin 32.0%; IFRS 21.7%.
  - R&D EUR 1,323m (21.2% of revenue, my calc). OCF EUR 1.63bn.
  - Net financial position EUR 1.53bn; cash EUR 4.13bn; borrowings EUR 2.60bn.
  - Headcount 25,967.
  - The CFO plans "value-based monetization models". ARR was EUR 4.50bn (+6%).
  - Source: [Dassault Q4/FY2025 press release PDF, 11 Feb 2026](https://www.3ds.com/assets/invest/2026-02/dassault-systemes-25q4-earnings_pr_va.pdf)
- 9M/Q3 2026 (published 28 Oct 2026):
  - Revenue: Q3 EUR 1,551.9m (+5% cc); 9M EUR 4,617m (+4% cc); recurring 83-84% of software.
  - Margins: Q3 non-IFRS 31.6%, 9M non-IFRS 30.6%, 9M IFRS 22.3%.
  - Cash: 9M OCF EUR 1,567m (+20%); cash EUR 3,814m; borrowings EUR 2,765m; net cash ~EUR 1.05bn after ArisGlobal.
  - 9M by line: Industrial Innovation +3%, Life Sciences -2%, Mainstream +10%.
  - Q3 by region: Asia +12% (China double-digit), Europe +9%, Americas -3%.
  - Cloud was 28% of Q3 software; 3DEXPERIENCE +25%.
  - Headcount 26,999.
  - Source: [Dassault release via Yahoo Finance, 28 Oct 2026](https://finance.yahoo.com/healthcare/articles/dassault-syst-mes-strong-q3-055900413.html)
  - Subscription is ~half of ARR (46% a year earlier) — [Investing.com transcript, 28 Oct 2026](https://www.investing.com/news/transcripts/earnings-call-transcript-dassault-systemes-beats-q3-2026-estimates-shares-fall-93CH-4978361) (machine transcript)
- Guidance history:
  - Apr 2025: margin outlook cut on tariff volatility, revenue 6-8% kept — [Reuters via AOL](https://www.aol.com/software-firm-dassault-systemes-cuts-050306724.html)
  - Jun 2025: EPS-doubling target (EUR 2.20-2.40) moved from 2028 to 2029, citing autos and tariffs — [Reuters via The Star, 6 Jun 2025](https://www.thestar.com.my/tech/tech-news/2025/06/06/france039s-dassault-systemes-delays-earnings-target-timeline-until-2029)
  - 23 Oct 2025: FY2025 revenue growth cut to "4-6% (previously 6-8%)", EPS 7-10% kept — [Dassault, 23 Oct 2025](https://www.3ds.com/newsroom/press-releases/dassault-systemes-solid-third-quarter-strong-operational-performance-confirming-full-year-eps-growth-adjusted-revenue-outlook). Reuters cited Life Sciences and CENTRIC (search summary)
  - FY2025 delivered +4%. FY2026 was guided 3-5%, then raised on 28 Oct 2026 to 4-5% (EUR 6.399-6.459bn). The CFO said the raise reflects ArisGlobal and FX, with organic growth at the midpoint (transcript).
- Management:
  - 21 Feb 2026: Bernard Charles stepped down as chairman "with immediate effect"; CEO Pascal Daloz became chairman and CEO — [Dassault, 21 Feb 2026](https://www.3ds.com/newsroom/press-releases/dassault-systemes-ceo-pascal-daloz-becomes-also-chairman-board-directors-dassault-systemes)
  - "Aligning the organization" (Feb 2026).
  - Ashwini Zenooz became CEO, Life Sciences & Healthcare (Oct 2026).
  - CMD on 17 Nov 2026.
- M&A: ArisGlobal, USD 1.8bn cash plus up to USD 200m AI milestones, closed Sep 2026 — [Schnitger, 3 Aug 2026](https://schnitgercorp.com/2026/08/03/5-on-a-monday-dassault-procore-autodesk-deal-updates-uk-antitrust-and-do-founders-ever-really-retire/). In 2025, Contentserv cost EUR 189m and the Centric stake increase EUR 252m (FY2025 PR).

### Inferences
- The gap of roughly 10 points between IFRS and non-IFRS margin (mainly acquisition amortisation and share-based pay) matters for return on capital. Medidata's 2019 purchase still weighs on reported returns.

### Gaps
- SIMULIA and BIOVIA revenue and growth are not disclosed and no outside estimate was found. China share of revenue is not obtained (the URD was not accessible: 403). Customer concentration is not obtained.

## B2. Dassault: five quality tests

### Takeaway
SIMULIA has credible judge-like positions (Abaqus nonlinear structures, CST, PowerFLOW), but outside proof of formal sign-off acceptance is thin and old. The finances are excellent; growth is the weak point.

### Cited Findings
- (a) Position:
  - PowerFLOW and WLTP: SIMULIA says "multiple vehicle manufacturers have already received approval for digital certification under WLTP" using PowerFLOW, but names no OEM or authority (company claim, unconfirmed; search summary of 3DS material). A 2020 SIMULIA blog says "regulations do not clearly explain how that validation should be carried out", and SIMULIA "in most cases" performs the simulations as a service — [3DS blog, 21 Aug 2020](https://blog.3ds.com/brands/simulia/working-with-wltp-simulation-solutions-for-lower-vehicle-emissions/) (old). An EU CFD sub-group proposal was submitted on 21 Oct 2019, outcome unverified — [ESI Group blog](https://esi-group.com/blog/driving-change-for-vehicle-emission-policies)
  - Living Heart and the FDA: a 5-year FDA collaboration (2019) including an in-silico trial — [BioSpace, 2019](https://www.biospace.com/dassault-systemes-and-the-fda-extend-collaboration-to-inform-cardiovascular-device-review-process-and-accelerate-access-to-new-treatments). The coalition "published with the FDA" an in-silico trial guide based on ASME V&V40 (Fast Company 2025 honour, per 3DS blog) — [3DS blog](https://blog.3ds.com/industries/life-sciences-healthcare/fast-company-honors-healthcare-innovation/). The FDA CM&S credibility guidance (final Nov 2023) covers "physics-based, mechanistic, or other first principles-based models" — [FDA](https://www.fda.gov/regulatory-information/search-fda-guidance-documents/assessing-credibility-computational-modeling-and-simulation-medical-device-submissions)
  - Medidata synthetic control arms: the FDA "supported" (case study: "agreed to consider") an SCA in Medicenna's Phase 3 rGBM trial (Oct 2020) — [3DS release](https://www.3ds.com/newsroom/press-releases/medidata-synthetic-control-arm-supported-us-food-and-drug-administration-use-medicenna-therapeutics-corp-phase-3-registrational-trial-recurrent-glioblastoma); a PMDA white paper followed (Jan 2026) — [Medidata](https://www.medidata.com/wp-content/uploads/2026/01/Medidata_SCA-PMDA-Whitepaper_EN_Jan-2026.pdf)
  - CEO framing: "AI can describe very easily an aircraft wings, but cannot design it, and more importantly, cannot certify the wing" (Q3 2026 call).
- (b) Lead: CIMdata's 2025 S&A report profiles "Dassault Systemes (Simulia)" among market leaders (CIMdata store, above). NVIDIA says Rivian uses Abaqus and PowerFLOW on NVIDIA infrastructure (NVIDIA, 16 Mar 2026). No third-party share data was found.
- (c) Revenue model:
  - Recurring 82-84% of software; licences 18%; services ~9.5-9.7% of revenue.
  - Cloud 25-28% of software; subscription ~50% of ARR (B1).
  - CST GPU computing is "licensed either by Acceleration Tokens ... or by SimUnit tokens or credits with the SIMULIA Unified License model" — [CST Studio Suite 2026 GPU Computing Guide](https://updates.cst.com/downloads/GPU_Computing_Guide.pdf)
- (d) Financial strength: non-IFRS margin ~32%, net cash EUR 1.05-1.53bn, OCF EUR 1.6bn, 2027 cash conversion guided at 85-90% (call). Europe is 38-42% of software, with exposure to European autos.
- (e) Resilience and cycle: European autos are "particularly challenged" (Q2 2026). Medidata fell on 2025 bookings and the loss of a large Moderna contract — [Schnitger, 26 Aug 2026](https://schnitgercorp.com/2026/08/26/plmish-earnings-check-what-have-we-learned/). Medidata is expected back to growth in Q4 2026 (release). China (incl. COMAC) is growing double digits (Q3 2026).

### Inferences
- **Provisional assessment, (a) Position:** Abaqus, CST and PowerFLOW are plausibly judges within customers' own sign-off processes. Formal regulator acceptance is evidenced only by vendor material (WLTP) or old collaborations (FDA 2019, SCA 2020). CATIA/SOLIDWORKS seats are front-end tools exposed to agents.
- **Provisional assessment, (b) Lead:** reputational lead in nonlinear FEA and lattice-Boltzmann CFD, without quantified outside share.
- **Provisional assessment, (c) Revenue model:** recurring but still largely user/seat-defined, with token-based SIMULIA licensing a partial hedge. About half of ARR is still maintenance/support rather than subscription.
- **Provisional assessment, (d) Financial strength:** excellent margins and net cash. Growth (4-5%) is well below Siemens software.
- **Provisional assessment, (e) Resilience:** less tied to AI-capex swings than Siemens (smaller semis exposure). It is more tied to the auto, pharma and industrial cycle; Asia/China is rising.
- Export controls: not researched as a specific exposure. COMAC is a showcased customer, so US or EU aerospace-related restrictions are a latent risk (inference).

### Gaps
- No primary regulator document names PowerFLOW, Abaqus, CST or Simpack. Simpack/EN 14363 was not checked. BIOVIA outside evidence: only that Schrodinger names BIOVIA as a competitor (materials-strand digest).

## B3. Dassault: six transitions (said vs done)

### Takeaway
The strategy is articulated (3D UNIV+RSES, Virtual Companions, the NVIDIA partnership). Monetisation is deferred to 2027, and little solver-level GPU or ML evidence has been published.

### Cited Findings
- (1) Pricing:
  - SAID: "The 3DEXPERIENCE agentic platform continues to be user-based ... It can be humans, it is the agent"; usage is "measured based on the units of work, the tokens consumption"; 3D UNIV+RSES revenue: "2027 would be the first year" (CFO Bergmann, Q3 2026 call — [transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-dassault-systemes-beats-q3-2026-estimates-shares-fall-93CH-4978361)).
  - DONE: SimUnit token/credit licensing (CST guide); ARR reporting introduced in 2026.
- (2) GPU:
  - SAID: the NVIDIA partnership brings "AI-based Virtual Twin physics to SIMULIA" via CUDA-X, plus OUTSCALE AI factories on three continents; NVIDIA adopts DS MBSE for Rubin AI-factory design; no money or dates — [Dassault, 3 Feb 2026](https://www.3ds.com/newsroom/press-releases/dassault-systemes-and-nvidia-partner-build-industrial-ai-platform-powering-virtual-twins)
  - DONE: CST 2026 supports NVIDIA and AMD GPUs. Several solvers need "GPUs with good double precision performance (e.g. B200 or H100)" (CST guide). Abaqus/PowerFLOW are used on GPUs at Rivian (NVIDIA).
  - An "8 to 10x" Abaqus speedup via cuDSS appears in search summaries only (unverified).
- (3) Agents/APIs:
  - Virtual Companions (AURA, LEO, MARIE...): 100% of cloud customers have them; 12-14% of the on-prem base is enabled; ~100 strategic customers; companion skills cover ~50% of the portfolio, with a target above 80% (call; company claims, unconfirmed).
  - Daloz "rejected 'frontier model + MCP' approaches" and said a general model is "useless" for advanced design exploration (Schnitger, 26 Aug 2026).
  - Internally, ~12,000 engineers use Cursor (garbled transcript).
- (4) Open source: no Dassault statement or action found.
- (5) Learned models with solver verification: SAID "science-validated Industry World Models" and AI "grounded" in physics (NVIDIA release; call). DONE: no specific shipped ML-in-solver product with verification metrics was found.
- (6) Regulators: see B2 (FDA collaboration 2019, ASME V&V40 guide, Medidata SCA 2020, WLTP vendor claims).

### Inferences
- (1) The user-based model stretched to agents with token metering is coherent and funded (net cash, 21% R&D). It depends on customers accepting agents as "users", and revenue proof is pushed to 2027.
- (2) The FP64 dependence in CST and Abaqus means the low-precision AI-hardware transition helps the surrogates, not the sign-off solvers.
- (3) Rejecting the frontier-model-plus-MCP approach is a bet that third-party agents will not drive DS tools from outside. That is the main execution risk if customers prefer open interfaces.
- What must go right: Medidata recovery, a European auto rebound, 3D UNIV+RSES conversion in 2027, and credible GPU/ML solver releases (CMD on 17 Nov 2026 should clarify).

### Gaps
- PowerFLOW GPU product status/date, Abaqus GPU figures from a primary source, API/MCP availability, and any open-source competitive impact (OpenFOAM, Code_Aster) were not verified.

## C. Testing the priors (70%: big vendors keep growing to 2029; 50%: seat-priced front ends and mid-market solvers lose pricing power after 2029)

### Takeaway
The evidence is mixed. It supports the 70% prior for Siemens and weakens it for Dassault. On the 50% prior there is no observed price erosion, but both vendors are pre-emptively re-engineering pricing.

### Cited Findings
- For the 70% prior: Siemens DI software +13% FY2026 with double-digit software growth guided for FY2027 (releases). CIMdata S&A market +8.5% in 2025. Schnitger concludes AI is raising demand for physics-based tools ("No hallucinations here", 16 Sep 2026). Dassault re-accelerated to +5% in Q3 2026 and raised guidance.
- Against the 70% prior: Dassault cut 2025 growth from 6-8% to 4-6%, delivered 4%, guided 3-5% for 2026 and moved its EPS-doubling goal to 2029. CIMdata's 2025 growth (8.5%) missed its own 10.7% forecast. Siemens EDA showed tough-comp quarters (+3% in Q4 FY2025).
- On the 50% prior (pressure signals): Siemens plans agent surcharges, and Dassault meters agent tokens. Synopsys prices GPU CFD by speedup. Siemens' 24,000 SaaS customers are ~90% SMEs (the mid-market most exposed). Siemens closed OpenRadioss.
- Against the 50% prior: SOLIDWORKS grew 6%+ with double-digit unit growth (Q3 2026 call). Mainstream Innovation was +10% in 9M 2026. Altair met its targets under Siemens.

### Inferences
- Large vendors' growth looks driven more by EDA, 3D-IC and AI-chip sign-off (Siemens) than by seat expansion. Vendors without that exposure (Dassault) show slower growth, so the 70% prior may be too generous for seat-heavy portfolios.

### Gaps
- No pricing or discounting data on seats and no churn data were found for either vendor.

## D. Could not verify

### Takeaway
These items remain open and should not be stated as fact.

### Cited Findings
- None beyond the sections above.

### Inferences
- None.

### Gaps
- Simcenter/Altair revenue since the merger; Siemens EDA revenue (estimates only); SIMULIA and BIOVIA revenue.
- Dotmatics enterprise value (reported around USD 5.1bn at announcement in Apr 2025, not re-verified; EUR 4.2bn cash outflow confirmed).
- Intel Foundry certification of Calibre (only SemiAnalysis's assertion).
- Third-party OPC/computational-lithography share.
- Any customer confirmation, GA date, hardware baseline or accuracy data for the Calibre-cuLitho 10-17x claim.
- PhysicsX-Siemens partnership; Simcenter X licensing terms; STAR-CCM+ GPU licensing.
- Exact date and form of the OpenRadioss closure (the repo was not found; the site is retired).
- Dassault China revenue share, customer concentration and URD risk factors (investor.3ds.com returned 403).
- Abaqus 8-10x cuDSS figure.
- Any named regulator acceptance of PowerFLOW for WLTP.
- Status of the 2019 FDA Living Heart collaboration after 2024.
- Dassault June 2025 revenue CAGR target: a search summary said 7-8% for 2024-29, but the fetched Reuters/The Star article says the revenue target was not updated. This conflict is unresolved.
- AI revenue figures (Siemens ~5% of DI software) are management claims.

## E. Dated source list

### Takeaway
Primary sources are Siemens and Dassault filings and releases. Secondary sources are trade press and analysts.

### Cited Findings
- Siemens Earnings Release Q4 FY2026, 12 Nov 2026 — https://assets.new.siemens.com/siemens/assets/api/uuid:11b1a70b-f540-45bb-824f-0b3fbb927e1b/dHQCOPR202611097494EN.pdf
- Siemens press release FY2026, 12 Nov 2026 — https://press.siemens.com/global/en/pressrelease/outstanding-fiscal-2026-performance-industrial-ai-drive-future-growth
- Siemens Q4 FY2026 call transcript (Investing.com), 12 Nov 2026 — https://in.investing.com/news/stock-market-news/earnings-call-transcript-siemens-posts-record-orders-in-q4-2026-as-growth-quickens-93CH-5698664
- Siemens Earnings Release Q4 FY2025, 13 Nov 2025 — https://assets.new.siemens.com/siemens/assets/api/uuid:3948cdd4-35e0-4c1d-8412-9aed4097b3d0/HQCOPR202511117277EN.pdf
- Siemens CMD press release, 13 Nov 2025 — https://assets.new.siemens.com/siemens/assets/api/uuid:4f2a7444-211a-4f8c-b01c-16f4e4cbe3b9/251113-press-release-en.pdf ; CFO speech, 13 Nov 2025 — https://assets.new.siemens.com/siemens/assets/api/uuid:74aedb6a-c07d-472b-a6a5-07832e3804ff/ONE%20Tech%20-%20Speech%20Ralf%20P.%20Thomas_CFO_EN.pdf
- Siemens Q2 FY2026, 13 May 2026; Q3 FY2026, 6 Aug 2026 (press.siemens.com links above)
- Siemens/NVIDIA partnership, 6 Jan 2026 — https://nvidianews.nvidia.com/news/siemens-and-nvidia-expand-partnership-industrial-ai-operating-system ; NVIDIA GTC partners, 16 Mar 2026 — https://nvidianews.nvidia.com/news/nvidia-and-global-industrial-software-giants-bring-design-engineering-and-manufacturing-into-the-ai-era
- Siemens cuLitho release, 14 Oct 2026 — https://news.siemens.com/en-us/siemens-calibre-nvidia-culitho/ ; Calibre blog, 14 Oct 2026 and 13 Apr 2026 (links above); NVIDIA blog, 3 Nov 2026 — https://blogs.nvidia.com/blog/ai-semiconductor-fabs/
- Siemens TSMC OIP, 23 Sep 2026; Samsung SAFE, 28 May 2026; DAC/Fuse, 26 Jul 2026; Lauterbach, 10 Nov 2026 (links above)
- Altair 10-K FY2024, filed 20 Feb 2025 — https://www.sec.gov/Archives/edgar/data/1701732/000095017025024197/altr-20241231.htm ; Altair closing, 26 Mar 2025 — https://news.siemens.com/en-us/siemens-altair-engineering-closing/
- Siemens Altair Units page, PhysicsAI page, Radioss transition page (live 12 Nov 2026; links above); HPCwire (Siemens release), 29 Jul 2026
- SemiAnalysis EDA primer, 21 May 2026 — https://newsletter.semianalysis.com/p/eda-market-primer
- Schnitger Corp: 20-21 Jul, 3 Aug, 26 Aug, 16 Sep, 5 Oct, 10 Nov 2026 (links above)
- Dassault Q4/FY2025 PR, 11 Feb 2026 — https://www.3ds.com/assets/invest/2026-02/dassault-systemes-25q4-earnings_pr_va.pdf ; Q3 2026 release, 28 Oct 2026 (Yahoo copy, link above); Q3 2026 call transcript, 28 Oct 2026 (Investing.com); Q3 2025 PR, 23 Oct 2025; chairman change, 21 Feb 2026; NVIDIA partnership, 3 Feb 2026 (3ds.com links above)
- Reuters via The Star, 6 Jun 2025; Reuters via Yahoo, 11 Feb 2026 (links above)
- CST Studio Suite 2026 GPU Computing Guide (copyright 2025) — https://updates.cst.com/downloads/GPU_Computing_Guide.pdf
- FDA CM&S guidance (final Nov 2023); Medidata/Medicenna (Oct 2020); Medidata PMDA white paper (Jan 2026); 3DS WLTP blog (Aug 2020); BioSpace FDA-Living Heart (2019) — links above
- CIMdata S&A reports 2025-2026; DE247, 10 Feb 2026; The Register, 30 May 2025; Business Standard, 3 Jul 2025 — links above

### Inferences
- Items older than 2025 (WLTP blog 2020, FDA collaboration 2019, Medicenna 2020, DRC share 2016) are flagged as dated.

### Gaps
- See D.
