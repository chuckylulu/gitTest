# Newer entrants in AI-for-physics and next-generation engineering simulation (status at 12 Nov 2026)

**Summary for the report writer**

1. **Shortlist.** At most two newer entrants plausibly belong among the 8–15 companies that matter most in physical simulation, and only as "emerging" slots.
   - PhysicsX is the best-funded pure play: $300M Series C at about $2.4B (8 Jun 2026), about 350 staff, about $50M of 2026 revenue (Bloomberg, reported), with Siemens, NVIDIA and Applied Materials as investors.
   - The second slot would go to one of the two owners of GPU-native solvers:
     - Flexcompute: Flow360 for CFD and Tidy3D for EM; claims 250+ customers; strategic investment from Samsung and Applied Materials (Oct 2026).
     - Luminary Cloud: its own GPU CFD solver plus SHIFT models; $72M Series B (Sep 2025) with NVentures.
   - Neural Concept ($100M, Dec 2025) is the most widely deployed surrogate and workflow layer in automotive, but it owns no solver.
   - Vinci ($250M at $1.5B, Oct 2026) is too new to rank and has no named customers.
   - Applied Intuition ($15B; Sacra estimates ARR of $830M in 2025) outweighs them all, but it sells autonomy and vehicle software. Rank it only if the list counts AV simulation.
2. **Judges versus layers.** Only Flexcompute and Luminary own a solver whose results customers could accept for sign-off (a "judge"). PhysicsX and Neural Concept sell learned models plus delivery and workflow, trained on data from other companies' solvers; PhysicsX's LGM-Aero was trained on Siemens STAR-CCM+ and Nastran data. That layer is the most exposed to Ansys SimAI, Siemens (now owner of Altair PhysicsAI), NVIDIA's PhysicsNeMo and Apollo, and customers' own models.
3. **Evidence is thin.**
   - No neutral benchmark tests the start-ups' commercial models head to head. Their workshop entries (AutoCFD4/5, HLPW5) and benchmark "records" are self-reported.
   - McGreivy and Hakim (2024) found that 79% of ML-for-fluids papers claiming to beat standard methods used weak baselines.
   - The best customer test is the Dallara/IBM preprint (arXiv 2604.18491). Its thresholds were set in advance; the surrogate met the usability threshold on 20 of 20 parts and the CFD-replacement threshold on 18 of 20. The prior is therefore roughly right but overstated, and the model is IBM's, not a start-up's.
4. **Sign-off.** I found no public case of a regulator or customer accepting an entrant's learned model for certification. Flow360 results feed eVTOL aero databases and loads work alongside wind tunnels. The FIA plans to use surrogates only for writing rules.
5. **Resilience.** Capital is concentrated: PhysicsX has raised about $500M and Vinci about $296M. Luminary's 2024 "$115M" was $15M of equity and $100M of debt. Consolidation has begun: CoreWeave bought Monolith (Oct 2025) and Mistral bought Emmi (May 2026; about €300M reported). In a financing pause around 2028, the likeliest to be sold are sub-scale or debt-funded firms and those priced at high revenue multiples (PhysicsX is at about 48x 2026E revenue).
6. **Exposure.** There is no listed pure play and no announced IPO. The routes are thin secondary markets (EquityZen, Hiive and Caplight list PhysicsX; no public prices) and listed strategic holders (Siemens, Applied Materials, NVIDIA, Samsung Electronics, AMD, CoreWeave, IBM) whose stakes are immaterial to them.

## 1. Profiles, funding, customers, partnerships and acquisitions (2024–2026)

### Takeaway
Four entrants have meaningful scale. Funding rose sharply in 2025–26 at high multiples of revenue. Strategic investors recur across cap tables: Siemens, NVIDIA, Applied Materials, Samsung, AMD and Temasek. Smaller players are being bought by AI-model and AI-cloud companies.

### Cited Findings
**PhysicsX** (London; PhysicsX Limited, no. 12134466, incorporated 1 Aug 2019 — [Companies House](https://find-and-update.company-information.service.gov.uk/search/companies?q=physicsx); founded by ex-F1 engineers Robin Tuluie and Jacomo Corbo, CEO)
- **Rounds:**
  - $32M Series A, Nov 2023 — [newsroom](https://physicsx.ai/newsroom)
  - $135M Series B, 22 Jun 2025, led by Atomico; Temasek, Siemens, Applied Materials and July Fund came in as new investors; total raised then nearly $170M — [PhysicsX](https://physicsx.ai/newsroom/physicsx-raises-135m-series-b-to-usher-in-a-new-era-of-ai-native-engineering-and-manufacturing)
  - Extension adding NVentures, 19 Nov 2025, taking the Series B above $155M at "nearly $1B" — [PhysicsX](https://www.physicsx.ai/newsroom/physicsx-announces-extension-to-series-b-round)
  - $300M Series C, 8 Jun 2026, at about $2.4B, led by Temasek. New investors: M&G and Intrepid. Existing: Applied Materials, Atomico, General Catalyst, July Fund, NGP, NVIDIA, Radius and Siemens — [PhysicsX](https://physicsx.ai/newsroom/physicsx-announces-300m-series-c-to-accelerate-physics-ai-for-industrial-engineering)
  - Tech.eu reports about $500M raised in total and about 350 staff — [Tech.eu](https://tech.eu/2026/06/08/physicsx-raises-300m-at-24bn-valuation/)
- **Revenue:**
  - Company claim, unconfirmed: recognised revenue doubled, booked revenue tripled and customer numbers more than doubled in the year to Jun 2026 (Series C release above).
  - Reported: Bloomberg (Jun 2026) says the CEO expects about $50M of revenue in 2026 and more than double that in 2027, and that about six months of demand could not be served. Bloomberg's piece was seen only via [New Market Pitch](https://newmarketpitch.com/blogs/news/digital-twin-physicsx-overvalued), which works out about 48x expected sales.
- **FY2024 group accounts** (filed 29 Oct 2025; auditor Saffery, opinion unqualified):
  - Loss before tax £8.15M (2023: £4.28M).
  - Cash £13.19M (2023: £21.46M).
  - Average staff 74 (2023: 28).
  - Income statement omitted under the small-companies regime, so turnover is not public.
  - The directors' going-concern note says that even with a 20% revenue miss the group "would still be in a cash positive position".
  - Series B-1/B-2 shares were allotted on 18 Jun 2025 for $124.0M, plus $10.0M by share transfer.
  - Source: [filing history](https://find-and-update.company-information.service.gov.uk/company/12134466/filing-history)
- **Board:** Russel Tham was appointed director on 8 Jun 2026 (Companies House). Temasek's Head of Emerging Technologies is a "Russell Tham" — [PhysicsX](https://www.physicsx.ai/newsroom/physicsx-launches-asia-pacific-hub-in-singapore-to-scale-ai-powered-industrial-engineering-across-the-region). That they are the same person is an inference from the name.
- **Customers and partners:**
  - Fortescue: a multi-year expansion of a collaboration more than two years old (27 Oct 2026). Value and production status not given — [PhysicsX](https://physicsx.ai/newsroom/physicsx-and-fortescue-expand-partnership-to-accelerate-industrial-innovation-with-ai)
  - Singapore hub (8 Oct 2026): 20 staff now, more than 100 planned within three years; a five-year partnership with A*STAR backed by a joint S$40M commitment; Seatrium as customer (Singapore release above).
  - An unnamed "leading aerospace manufacturer" uses PhysicsX models on live casting lines, running on AWS (Sep 2025) — [PhysicsX](https://www.physicsx.ai/newsroom/real-time-intelligence-in-the-foundry-ai-for-casting-quality-and-efficiency)
  - Leonardo is named as a partner and customer — [Resilience Media](https://resiliencemedia.co/physicsx-raises-300m-at-a-2-4b-valuation-for-ai-to-create-and-test-defence-and-other-hardware/)
  - Siemens: LGM-Aero, trained on more than 25M geometries using Simcenter STAR-CCM+ and Nastran data (4 Dec 2024) — [Siemens](https://news.siemens.com/en-us/siemens-physicsx/). Later: Simcenter X integration (Jul 2025) and data-centre power work with NVIDIA (Mar 2026).
  - Others: Microsoft Discovery (May 2025), Deutsche Telekom's industrial AI cloud (live Feb 2026), America's Cup team GB1 (2026) — [newsroom](https://physicsx.ai/newsroom)
  - CoreWeave (11 Mar 2026): both the PhysicsX platform and the training of its pre-trained models run on CoreWeave — [PhysicsX](https://www.physicsx.ai/newsroom/physicsx-and-coreweave-partner-to-deliver-high-performance-physics-ai-for-advanced-industrials)
- **Selling model:** jointly scoped pilots of 1–3 months; embedded data-science, simulation and ML "delivery" teams, with early engagements services-heavy — [PhysicsX](https://physicsx.ai/newsroom/why-we-do-pilots-and-how-to-choose-a-good-one)

**Neural Concept** (Lausanne; EPFL spin-off; its own releases give 2018 and 2019 as the founding year; CEO Pierre Baqué)
- **Rounds:**
  - $9.1M Series A (Jun 2022) and $27M Series B (Jun 2024, led by Forestay) — [press list](https://www.neuralconcept.com/newsroom/press-releases)
  - $100M Series C (18 Dec 2025), led by Goldman Sachs Alternatives Growth Equity, with Forestay, Alven, HTGF, D. E. Shaw and Aster. Valuation not disclosed, and no reported figure found — [Neural Concept](https://www.neuralconcept.com/press-release/neural-concept-closes-100m-funding-round)
- **Company claims, unconfirmed:**
  - Enterprise revenue up fourfold in 18 months. More than 50 customers, including GM, GE Vernova, Leonardo, Eaton, Safran, Renault and "multiple Formula 1 teams" (Dec 2025 release above).
  - ARR growth "significantly outpaces burn rate"; partners with more than 70% of the largest OEMs and 40% of the top-100 tier-1 suppliers; upsells up 40% — [Sep 2025](https://www.neuralconcept.com/press-release/neural-concept-100-percent-enterprise-growth)
  - A Jan 2024 release slug cites "60 customers", so the company's customer definitions vary.
- **Customer evidence (all on vendor pages):**
  - JLR (NVIDIA GTC, Mar 2026): design evaluations rose from about 50 to about 1,500 a day; the platform "does not replace simulation" — [NC](https://www.neuralconcept.com/industry-stories/jlr-nvidia-gtc-aerodynamic-engineering)
  - GM (Aug 2025): a pedestrian-safety head-injury (HIC) co-pilot trained on crash data from 11 vehicle programmes, used by safety specialists "without relying solely on" finite-element analysis. No accuracy figures given — [NC](https://www.neuralconcept.com/industry-stories/general-motors-pedestrian-safety)
  - Hanwha Ocean: "promising capabilities", at the Seoul office opening (Jun 2026) — [NC](https://www.neuralconcept.com/press-release/neural-concept-opens-seoul-office)
- **Products:**
  - AI design copilot (Jan 2026).
  - MCP Bridge (19 Oct 2026), through which AI agents drive CATIA, NX, ANSA, HyperMesh and Abaqus. Volvo Cars, TRATON and OPmobility are quoted — [NC](https://www.neuralconcept.com/press-release/neural-concept-launches-mcp-bridge)

**Luminary Cloud** (San Mateo; founded 2019 by Jason Lango and Juan Alonso, now CTO; incubated by Sutter Hill; CEO Pete Schlampp)
- **Launch (13 Mar 2024):** $15M of equity and $100M of debt, both from Sutter Hill; 73 staff and 33+ customers at the time — [TechCrunch](https://techcrunch.com/?p=2677477)
- **Pricing:** per GPU-minute with no licence fee; a quick conceptual aircraft run costs under $90 (TechCrunch, above).
- **Series B:** $72M (15 Sep 2025), led by N47, with Sutter Hill and NVentures. Valuation not disclosed — [Luminary](https://luminary.ai/resources/luminary-cloud-secures-dollar72m-series-b-to-lead-the-physics-ai-era)
- **Product:** its own GPU-native CFD solver, a Physics AI "model factory", an MCP server and SHIFT models:
  - SUV, with Honda: more than 1,000 DES runs on H100s, built on NVIDIA's DoMINO/PhysicsNeMo — [Luminary](https://luminary.ai/resources/introducing-luminary-shift-models-a-suite-of-physics-ai-foundation-models-to-transform-engineering-design/)
  - Wing (with Otto), CCA, Submarine, Pump, Missile, Crash, Battery, Truck and NVH — [resources](https://luminary.ai/resources); [Washington Technology, 14 Jan 2026](https://washingtontechnology.com/companies/2026/01/luminary-cloud-expands-physics-ai-toolkit-defense-focused-models/410679/)
  - The SUV sample on Hugging Face is gated and licensed CC-BY-NC-4.0 (non-commercial) — [HF](https://huggingface.co/datasets/luminary-shift/SUV-sample)
- **Deployment:** Luminary Private Cloud for on-premises and air-gapped sites (24 Feb 2026), building on its ITAR-compliant options. Customers named: Northrop Grumman, Joby and Otto — [Luminary](https://luminary.ai/resources/luminary-introduces-luminary-private-cloud-to-bring-physics-ai-into-secure-air-gapped-defense-and-aerospace-environments)

**Flexcompute** (Boston; founded about 2016 by Zongfu Yu, Qiqi Wang of MIT and Shanhui Fan of Stanford; more than 70 PhDs)
- **Funding:**
  - Series A (Nov 2020, led by WI Harper) and a $22M Series B (29 Nov 2021, led by Coatue, with GGV, 3W, WI Harper and River Delta) — [Flexcompute](https://www.flexcompute.com/blog/2021/11/19/flexcompute-secures-22m); [WI Harper](https://wiharper.com/wi-harper-group-backed-flexcompute-raises-22m-to-accelerate-industrial-rd-with-advanced-engineering-computing)
  - Strategic investment from Samsung Ventures and Applied Ventures (12 Oct 2026), amount undisclosed — [Pulse 2.0](https://pulse2.com/flexcompute-raises-strategic-investment-from-samsung-ventures-and-applied-ventures/)
  - A $53M Series C (Jul 2024) appears only in CB Insights and is unverified — [CB Insights](https://www.cbinsights.com/company/flexcompute/financials)
- **Products:** its own GPU-native Flow360 (CFD, with "usage-based pricing") and Tidy3D (FDTD electromagnetics), plus PhotonForge, RF, GeometryAI, FlexAgent and Nexus (on-premises) — [Flexcompute](https://www.flexcompute.com/); [Flow360](https://www.flexcompute.com/flow360/)
- **Company claims, unconfirmed:** more than 250 companies and institutions as customers; logos shown include Anduril, Beta, Joby, Northrop Grumman and Samsung; a 5-billion-degree-of-freedom warpage model solved within 2% of commercial FE results (Pulse 2.0, above).
- **Customer cases (vendor-published):**
  - Vertical Aerospace, Valo (15 Jun 2026): turnaround fell from two weeks to one day, and results matched the wind tunnel "well within the required error margins". The wind tunnel was still used — [Flexcompute](https://flexcompute.com/blog/vertical-aerospace-10x-more-designs)
  - BETA Technologies, A250 (27 May 2025): aero databases for its flight-controls and simulation teams; CFD described as "complementary" to the wind tunnel — [Flexcompute](https://flexcompute.com/blog/designing-the-a250-in-the-age-of-instant-aerodynamics)
  - Others: Electra (says it "cut 9 months" from its design timeline), Wisk, Joby, NIO and Regent — [Flow360](https://www.flexcompute.com/flow360/); [blog](https://www.flexcompute.com/blog/)

**Vinci** (Palo Alto; founded 2023 by Hardik Kabaria and Sarah Osentoski)
- **Funding:**
  - $46M seed and Series A (2 Dec 2025; Xora, Eclipse, Khosla) — [SiliconANGLE](https://siliconangle.com/2025/12/03/vinci-nabs-46m-speed-chip-simulations-ai/)
  - $250M Series B at $1.5B (6 Oct 2026), co-led by Advent, Temasek and Xora, with AMD Ventures, Eclipse, Khosla and Madrona — [Advent](https://www.adventinternational.com/vinci-raises-250m-series-b-at-1-5b-valuation/)
- **Company claims, unconfirmed:**
  - "Deterministic, solver-accurate" results from "GPU-native physics kernels" plus a "Foundation Model for Physics"; works zero-shot, with no training on customer data; handles 15B+ degrees of freedom in minutes.
  - Runs on "flagship production engineering programs", but no customers are named. In Dec 2025 it said three chipmakers had deployed it and more than 10 were benchmarking it.

**Applied Intuition** (adjacent: autonomy and vehicle software)
- **Valuation:** $600M Series F at $15B post-money (Jun 2025), of which about $400M was secondary — [Applied Intuition](https://appliedintuition.com/news/series-f); [Sacra](https://sacra.com/c/applied-intuition/). Reported, not closed: offers of at least $30B (13 Oct 2026) — [Crypto Briefing](https://cryptobriefing.com/applied-intuition-30-billion-valuation-offers/)
- **Revenue (Sacra estimate):** ARR of $830M in 2025.
- **Business model:** annual licences priced by seats, simulation workload and modules (Sacra, above).

**Other entrants**

| Company (HQ, founded) | What it sells; own solver? | Funding (date) | Status, customers |
|---|---|---|---|
| Monolith (London, 2016) | ML on test data; no solver | £1.9M seed 2019, £8.5M A 2021, £21M B 2025 | Bought by CoreWeave (announced 6 Oct 2025, terms undisclosed); Imperial says "acquired" (23 Oct 2025); customers Nissan, BMW, Honeywell — [CoreWeave](https://coreweave.com/news/coreweave-to-acquire-monolith-expanding-ai-cloud-platform-into-industrial-innovation); [Imperial](https://www.imperial.ac.uk/news/articles/engineering/aeronautics/2025/aeronautics-spinout-monolith-ai-acquired-by-us-cloud-computing-company/) |
| Emmi AI (Linz, 2024) | AB-UPT surrogates (published in TMLR); no solver | €15M seed (Apr 2025) | Mistral deal 19–23 May 2026, terms undisclosed; more than 30 staff; "close to €300M" per unnamed sources — [Emmi](https://www.emmi.ai/news/mistral-ai-acquires-emmi-ai); [Mistral](https://mistral.ai/news/accelerate-ai-native-industry); [FTJ](https://frenchtechjournal.com/mistral-ai-buys-viennas-emmi-ai-in-eur300m-bid-to-own-europes-factory-floor/) |
| BeyondMath (London, 2022) | "Generative physics model" trained on first-principles physics | $18.5M seed incl. $10M extension led by CIC (25 Feb 2026) | Company claims: Honeywell STRATA ($19M, 3-year project) and an F1 team — [CIC](https://www.cic.vc/beyondmath-completes-18-5-million-seed-round-to-scale-worlds-largest-foundational-physics-ai-model/) |
| Navier (San Francisco) | Agents that set up and run CFD (OpenFOAM-based per a tracker, unverified) | $5.6M seed (Dec 2025; GV, HCVC, YC) | No named customers — [Pulse 2.0](https://pulse2.com/navier-5-6-million-seed/) |
| Pasteur Labs (New York, PBC) | "Simulation Intelligence" platform | About $10.5–13.7M (2023, per trackers) | Bought FOSAI (21 Aug 2025); presented its neural surrogate at AutoCFD5 — [PR Newswire](https://www.prnewswire.com/news-releases/pasteur-labs-acquires-ai-startup-fosai-to-accelerate-adoption-of-ai-driven-physics-simulation-for-space--defense-applications-302535200.html) |
| nTop (New York) | Implicit-geometry design; bought GPU-native CFD maker cloudfluid (19 Feb 2025) | n/a | Partner of Luminary — [Develop3D](https://develop3d.com/cad/ntop-acquires-cloudfluid-gpu-native-cfd-software/) |
| Quanscient (Tampere, 2021) | Cloud multiphysics plus quantum algorithms | €10M Series A (26 May 2026; 55 North, B&C); Dealroom estimates valuation at $44M | Unnamed Fortune 100 customers — [Tech.eu](https://tech.eu/2026/05/26/quanscient-lands-eur10m-to-advance-ai-and-quantum-native-hardware-engineering/) |
| Project Prometheus (San Francisco, 2025) | AI and agents for engineering and manufacturing; pre-revenue | $6.2B (Nov 2025); then $12B at ~$41B (Jun 2026, Sacra) or $10B at ~$38B (other outlets) | Bought General Agents — [Sacra](https://sacra.com/c/project-prometheus) |
| Zenithon (n/a) | ML for "physics-heavy engineering" | $10M (about Sep–Oct 2026) | Details paywalled — [RuntimeWire](https://runtimewire.com/article/zenithon-raises-10m-extreme-physics-world-models) |

### Inferences
- Valuations rest on growth, not scale. PhysicsX is at about 48x reported 2026E revenue. The reported offers for Applied Intuition are about 36x its estimated 2025 ARR. Rankings should weigh revenue and evidence above valuation.
- Cap tables hedge. Siemens backs PhysicsX while owning Altair PhysicsAI. Applied Materials backs both PhysicsX and Flexcompute. NVIDIA backs PhysicsX and Luminary while giving away PhysicsNeMo.
- Cash burn:
  - PhysicsX's cash fell £8.3M in 2024 with little new equity, on 74 staff. With about 350 staff in 2026 the burn must be far higher, but it is undisclosed.
  - If "recognised revenue doubled" compares 2025 with 2024, then about $50M in 2026E implies roughly $25M in 2025. This is a rough inference.
- Luminary's $100M of venture debt from its incubator is unusual. Its terms, and whether it has been converted, are unknown.
- Total funding (inferred from the rounds above):
  - Neural Concept: at least about $136M.
  - Luminary: about $87M of equity plus $100M of debt.
  - Vinci: about $296M.

### Gaps
- Headcount for Neural Concept, Flexcompute, Vinci and Luminary (2026).
- Valuations for Neural Concept, Luminary and Flexcompute.
- Revenue for every entrant except PhysicsX (and its figure is reported, not filed).
- Customer concentration, for every entrant.

## 2. Independent validation (benchmarks, workshops, peer review)

### Takeaway
No neutral body has published a head-to-head test of the start-ups' commercial models, and most "records" are self-published. The most rigorous customer test with thresholds set in advance (Dallara) used IBM's model, and it nearly met the bar for replacing CFD.

### Cited Findings
- **Dallara/IBM, arXiv 2604.18491 v2** (27 Apr 2026; 7-page preprint, not peer-reviewed) — [arXiv](https://arxiv.org/html/2604.18491v2)
  - Data: 625 RANS (k-ω SST) samples of a parametric LMP2 car at about 2.4M cells each. Each was "reviewed and aero-verified by Dallara aerodynamic engineers".
  - Errors on drag/downforce: IBM's GIST model 0.6%/0.7%; GAOT 0.9%/1.0%; Transolver 1.2%/1.2%; FNO 4.0%/3.6%.
  - Thresholds: "Dallara established specific absolute error thresholds in advance", with the values redacted. "The usability threshold is met for every part, while the CFD replacement threshold is met by 18/20 parts."
  - Stated aim: "The objective is not to replace classical numerical solvers entirely."
  - Limitations it acknowledges: the model smooths sharp gradients; a 4° diffuser angle was outside the training data; the ground truth is RANS CFD, not wind-tunnel data.
- **McGreivy and Hakim** (Nature Machine Intelligence 6, Oct 2024) — [OSTI](https://www.osti.gov/pages/biblio/2475825-weak-baselines-reporting-biases-lead-overoptimism-machine-learning-fluid-related-partial-differential-equations); [arXiv](https://arxiv.org/abs/2407.07218)
  - 79% (60/76) of articles that claim ML beats standard numerical methods for fluid PDEs compared against weak baselines.
  - Reporting biases are "widespread".
- **Open datasets (CC-BY-SA):**
  - DrivAerML: 500 variants, hybrid RANS-LES — [arXiv](https://arxiv.org/abs/2408.11969)
  - AhmedML: 500 variants, OpenFOAM — [arXiv](https://arxiv.org/abs/2407.20801)
  - WindsorML: 355 variants, GPU wall-modelled LES with more than 280M cells — [arXiv](https://arxiv.org/abs/2407.19320)
- **CarBench** (Elrefaie, Shu, Klenk and Ahmed; arXiv 2512.07847, v3 dated 14 Oct 2026): benchmarks 11 architectures, including Transolver, Transolver++ and AB-UPT, on DrivAerNet++. It includes no commercial vendor models — [arXiv](https://arxiv.org/abs/2512.07847)
- **AutoCFD5** (Bologna, 8–9 Oct 2026; DrivAerML was the reference ML dataset) — [AutoCFD](https://autocfd.org/presentations/)
  - AI/ML talks came from Mistral (AB-UPT), Cadence, Luminary ("cross-architecture evaluation… calibrated uncertainty quantification"), Pasteur Labs, PhysicsX, Siemens, KIT and IngeniAI.
  - Neural Concept and NVIDIA are not listed.
  - The AI/ML technology focus group's conclusions are not stated on the page.
- **AutoCFD4** (2024) — [Luminary](https://luminary.ai/resources/luminary-cloud-highlighted-as-the-fastest-cfd-solver-at-autocfd4/)
  - Luminary cites the workshop summary as calling it "the fastest GPU-based entry": 157M cells, 93 minutes on 48 A100s.
  - Its own table shows the lift change (Cl delta) with the opposite sign to experiment.
- **Other AIAA workshops:**
  - HLPW5 (2024): Luminary's validation case is gated and presented by its own staff (SciTech 2025) — [Luminary](https://vv.luminary.ai/aerospace-and-defense-hlpw5)
  - DPW-8 (6–7 Jun 2026): I found no entrant results — [AIAA](https://aiaa.org/courses/aiaa-drag-prediction-workshop/)
- **Self-reported "records":**
  - Neural Concept on DrivAerNet++ (11 Sep 2025): no numbers published — [NC](https://www.neuralconcept.com/press-release/neural-concept-aerodynamics-benchmark-record)
  - PhysicsX's PX-Car-Aero-v1 (7 Aug 2026): "competitive with the best published results", with no comparison table — [PhysicsX](https://physicsx.ai/newsroom/scaling-physics-ai-for-automotive-aerodynamics-part-ii-meet-px-car-aero-v1)
  - PhysicsX topped Safran's PLAID Tensile2D leaderboard for about nine months. An AI agent then reverse-engineered the hidden simulator to about 1e-8 error (11 Aug 2026; the benchmark is "relatively simple") — [PhysicsX](https://physicsx.ai/newsroom/how-an-ai-agent-cracked-an-industry-benchmark)
- **A vendor's own caution:** Neural Concept's CEO: "If you think of it only as a replacement for simulation, you will be disappointed" (18 Sep 2025) — [NC](https://www.neuralconcept.com/post/finding-the-path-to-value-in-engineering-ai-why-we-need-to-rethink-benchmarking)

### Inferences
- The prior is partly contradicted. Within a parametric family the learned model came close to the bar for replacing CFD (18 of 20 parts). The study tests neither out-of-distribution designs nor correlation with track or flight data.
- The PLAID episode shows that a leaderboard backed by a hidden solver can be distilled, so leaderboard rank is weak evidence of a commercial lead.
- Luminary is the only leading entrant presenting uncertainty-calibrated evaluations at a neutral workshop. That matters for transition (5), learned models inside solvers that still certify.

### Gaps
- Not read: the AutoCFD5 focus-group slides, Luminary's AutoCFD5 paper, and any comparative study by an OEM consortium. The search budget ran out.

## 3. Sign-off and acceptance by regulators and customers

### Takeaway
I found no public evidence that a regulator or customer has accepted an entrant's learned model for certification or formal sign-off. GPU-native solvers already produce production engineering data, but alongside physical tests.

### Cited Findings
- **Flow360 (Flexcompute):**
  - BETA uses it for aero databases for flight controls (May 2025).
  - Dufour uses it for aero databases and structural loads (12 Feb 2024). The article says "Many certification authorities are now allowing" CFD data, but claims no acceptance of Flow360 results — [Flexcompute](https://flexcompute.com/blog/the-dufour-aerospace-aero2-uav-optimal-design-through-high-fidelity-cfd)
  - Vertical checked results against the wind tunnel (Jun 2026).
  - I found no FAA or EASA acceptance of Flow360.
- **Luminary on DARPA's CyPhER Forge** (10 Sep 2026): the aim is a 10x cut in flight-test points. "The model supplies predictions, not permission to act" — [Luminary](https://luminary.ai/resources/how-darpa-is-using-physics-ai-to-cut-flight-tests-by-10x/)
- **Neural Concept:** at JLR it "does not replace simulation"; at GM it is a co-pilot. Neither page claims sign-off (Section 1).
- **PhysicsX:** in casting it guides operators on the line; sign-off is not mentioned.
- **FIA** (28 Oct 2026): it may use "surrogate approaches trained off our CFD data" to write rules for about 2030. Design remains "human-driven, engineer-driven". The aerodynamic testing restrictions (ATR) are not discussed — [The Race](https://www.the-race.com/formula-1/ai-will-help-design-future-f1-cars-in-new-fia-aws-deal/)
- **EASA:** AI Concept Paper Issue 2 (6 Mar 2024), with a new issue out for comment on 3 Jun 2026. No approved ML application is listed — [EASA](https://www.easa.europa.eu/en/domains/research-innovation/ai)
- **NRC gap assessment:** AI models within the scope of RG 1.157 and RG 1.203 are "practically not allowed" under Part 50 Appendix K — [NRC](https://www.nrc.gov/docs/ML2429/ML24290A059.pdf)

### Inferences
- Learned models are entering decision support and test-point reduction, not certification. GPU-native solvers can follow the existing path by which regulators accept CFD evidence; learned models cannot yet. This supports the prior that solver owners hold the stronger position.

### Gaps
- I found no programme-level certification document (FAA, EASA, CAA or FIA) naming any entrant.

## 4. Scoring the leaders: five tests, six transitions, said versus done, scenarios

### Takeaway
Flexcompute and Luminary lead on position, PhysicsX on financial strength and Neural Concept on adoption. None passes the test of independently evidenced lead.

### Cited Findings
- **Revenue models:**
  - Luminary: per GPU-minute (2024; TechCrunch). Flexcompute: usage-based (Flow360 page).
  - Neural Concept: ARR plus upsells (Sep 2025). PhysicsX: pilots, platform and delivery teams, with bookings tripled. Applied Intuition: seat, workload and module licences (Sacra).
  - I found no pricing by result.
- **GPU and cloud dependence:**
  - PhysicsX runs on CoreWeave, Deutsche Telekom's industrial AI cloud and AWS, and is "optimised for Nvidia chips" (Resilience Media).
  - Neural Concept used Azure NC H100 virtual machines (benchmark release).
  - Flexcompute cases ran on B200 GPUs: 8 B200s for BETA; under 20 minutes per case for Dufour.
  - Luminary uses H100s.
- **Agents and programming interfaces:** Neural Concept's MCP Bridge (Oct 2026); Luminary's MCP server (2025); Flexcompute's FlexAgent and Python API; PhysicsX's work with Microsoft Discovery.
- **Export controls:** the US BIS "affiliates rule" (extending Entity List controls to 50%-owned subsidiaries) is suspended until 10 Jan 2027 — [Reed Smith](https://www.reedsmith.com/our-insights/blogs/trade-compliance-resource-hub/5272/bis-further-suspends-affiliates-rule-until-january-2027/)
  - Flexcompute publishes a case study with Chinese carmaker NIO (Jun 2025; blog).
  - Luminary sells ITAR-compliant and air-gapped deployments.

### Inferences
**Scores** (S = strong, M = medium, W = weak; judgements from the evidence above)

| Test | PhysicsX | Neural Concept | Luminary | Flexcompute | Vinci |
|---|---|---|---|---|---|
| (a) Position | W–M: no judge; data factory plus delivery teams | W–M: no judge; embedded workflow and agent bridge | M–S: own GPU CFD plus models | S: own GPU CFD and EM solvers | Unclear: claims "solver-accurate" kernels |
| (b) Lead (outside evidence) | W–M: casting in production, Fortescue | M: most named users | W–M: named users; self-reported workshop entries | M: many named eVTOL users | W: no customers named |
| (c) Revenue model | Services-heavy platform | Subscription/ARR | Usage | Usage | Unknown |
| (d) Financial strength | S: about $500M raised; ~48x sales | M–S: $100M fresh; says ARR growth beats burn | W–M: $87M equity plus $100M debt | W–M: small disclosed equity; strategic backers | S on cash; W on proof |
| (e) Resilience | M | M | W–M | M | M |

**Six transitions: said versus done**

| Transition | PhysicsX | Neural Concept | Luminary | Flexcompute |
|---|---|---|---|---|
| (1) Seats to use or result | Bookings model; result pricing not seen | ARR | Done: usage | Done: usage |
| (2) CPU to GPU | Done; NVIDIA-dependent | Done | Done: GPU-native | Done: GPU-native |
| (3) Agents via programming interfaces | Said; agent benchmark | Done: MCP Bridge | Done: MCP server | Done: FlexAgent |
| (4) Open codes and models | Said: "open standards" with NVIDIA | Not seen | Done: non-commercial SUV sample; builds on PhysicsNeMo | Not seen |
| (5) Learned models in certifying solvers | Not seen | Said: "aligned with" CFD and wind tunnel (JLR) | Said: uncertainty and out-of-distribution flags; AutoCFD5 talk | Said: "traceable to GPU-native simulation" |
| (6) Regulator and customer sign-off | Not done | Not done | Not done | Not done (CFD feeds aero databases and loads) |

**What must go right**
- PhysicsX: turn embedded delivery work into repeatable software revenue at software margins; show that its large pre-trained models generalise; keep Siemens a partner rather than a rival.
- Neural Concept: stay the neutral layer as Siemens and Synopsys bundle their own AI; get customers to pay for agent orchestration.
- Luminary: win acceptance of its solver results beyond defence and eVTOL; service or refinance its debt.
- Flexcompute: get Flow360 into OEM sign-off processes; fund growth from customer revenue plus strategic money.
- Vinci: name customers and publish validation against incumbent thermal tools.

**Scenarios to 2030**
- Steady growth (about 55%): consolidation continues. Solver owners and the best-funded grow, while incumbents' AI features cap what surrogates can charge.
- Financing-led pause around 2028 (about 25%):
  - Firms that need new money at high multiples (PhysicsX, Vinci) or carry debt (Luminary) face down-rounds or sales.
  - Precedents show who buys: clouds (CoreWeave and Monolith) and AI labs (Mistral and Emmi).
  - Usage-priced solver vendors with real customer revenue (Flexcompute) should hold up best.
  - All are exposed to the price and availability of NVIDIA GPUs.
- Faster acceleration (about 20%): agents multiply simulation runs, which favours GPU-native judges and data factories. Valuations would re-rate, but NVIDIA and incumbents would gain at least as much.

### Gaps
- No entrant discloses gross margin, retention, burn or customer concentration. PhysicsX's FY2024 accounts are the only exception, and only partly.

## 5. Threats and durable assets

### Takeaway
Few assets are durable. They are validated GPU-native solvers (Flexcompute, Luminary), proprietary simulation corpora (PhysicsX, Luminary) and embedded workflows (Neural Concept). Learned models alone are not durable.

### Cited Findings
- **Ansys 2026 R1** (11 Mar 2026): SimAI comes as a Premium SaaS edition and a Pro desktop edition, with optiSLang connectors, GeomAI and agents — [Synopsys](https://news.synopsys.com/2026-03-11-Synopsys-Launches-Ansys-2026-R1-to-Re-Engineer-Engineering-with-Joint-Solutions-and-AI-Powered-Products). Company claim: the Synopsys CEO cited an automaker using SimAI at about 98% prediction accuracy (Q3 FY26 call, 26 Aug 2026) — [transcript](https://www.webull.com/news/15497781661541376)
- **Siemens:** altair.com/physicsai now redirects to Siemens' Simcenter PhysicsAI page — [Siemens](https://www.siemens.com/en-us/products/simcenter/engineering-data-science-ai/physicsai/)
- **NVIDIA:**
  - PhysicsNeMo is open source (Apache 2.0) and includes a DoMINO external-aerodynamics NIM — [NVIDIA](https://developer.nvidia.com/physicsnemo)
  - Apollo open models were unveiled at SC25 and are "coming soon". Early adopters include Luminary, PhysicsX, Siemens and Synopsys — [NVIDIA](https://blogs.nvidia.com/blog/apollo-open-models)
- **Well-funded AI-for-science ventures:**
  - Prometheus: see the Section 1 table.
  - Periodic Labs: $300M seed (Sep 2025); talks at $7.5B reported but unconfirmed — [Contrary](https://research.contrary.com/company/periodic-labs/quick-facts)
  - Lila Sciences: talks at $8.5B (Bloomberg, 3 Jun 2026) — [Bloomberg Law](https://news.bloomberglaw.com/private-equity/lila-sciences-said-in-talks-for-funds-at-8-5-billion-valuation)
  - Mistral bought Emmi. Neil Ashton, lead author of DrivAerML, now works at Mistral and co-leads AutoCFD's AI/ML focus group — [AutoCFD](https://autocfd.org/)
- **Customers' own data and models:**
  - GM's model was trained on GM crash data.
  - PhysicsX on CoreWeave offers to train private models on customers' own data.
  - MCP Bridge keeps customers in "control and ownership of their programs and data".

### Inferences
- The asset that customers' own models and NVIDIA's open stack cannot easily replace is a trusted judge plus the data pipeline it feeds. Learned-model vendors depend on someone else's solver for training data: PhysicsX on Siemens tools, Neural Concept on customers' solvers. That is a structural dependency.
- General AI labs (Mistral, Prometheus) are bundling physics models with agents, which squeezes standalone surrogate vendors.

### Gaps
- How often customers replace vendor surrogates with in-house models.
- When Apollo checkpoints will actually ship.

## 6. Regional coverage

### Takeaway
Outside the US, UK, Switzerland and Austria I found only small, early entrants. Western entrants are moving into Asia directly.

### Cited Findings
- **Japan, RICOS:**
  - Products: RICOS Lightning (built on its IsoGCN algorithm) and Generative CAE.
  - Funding: about ¥600M (Jul 2025) from XTech Ventures, mint, DRONE FUND and others, plus a Hokkoku Bank loan; Daikin uses Lightning for compressor design — [kepple](https://kepple.co.jp/articles/mf2gxo8ef4su). NEDO listed a ¥1.2B valuation (Apr 2024) — [NEDO](https://www.nedo.go.jp/activities/startups/company45.html)
  - An aggregator reports an ML race-aerodynamics contract with Toyota Gazoo Racing Development (Apr 2026), unverified.
  - Neural Concept sells in Japan through Cybernet and SCSK (press list).
- **South Korea:**
  - Narnia Labs: KAIST spin-off founded Apr 2022 (CEO 강남우), raised a pre-Series-A round in Apr 2025 — [THEVC](https://thevc.kr/narnialabs). A 2022 report says it cut a Hyundai Mobis brake-part design from a month to a minute — [MT](https://www.mt.co.kr/future/2022/10/11/2022100815564064481)
  - Neural Concept opened its Seoul office in Jun 2026.
- **China:**
  - Tianfu Software 天洑 (Nanjing, 2011): products AICFD, AIFEM and AIPOD; a Series C of "数亿元" (several hundred million yuan) in Jul 2022, led by GGV and Legend Capital; claims more than 400 customers — [36Kr](https://www.36kr.com/p/1831315772563713)
  - DP Technology (AI for science): Series C of more than RMB 800M (Dec 2025); a Hong Kong IPO plan has been reported but not confirmed (materials researcher).
- **India:**
  - BQP (formerly BosonQ Psi; Syracuse, NY and Bengaluru): IBM Ventures invested (3 Sep 2026), taking total funding to $8M — [AIM](https://analyticsindiamag.com/ai-news/ibm-ventures-invests-in-bqp-as-physics-platform-enters-production)
  - Neural Concept set up in India (10 Sep 2026) — [NC](https://www.neuralconcept.com/press-release/neural-concept-expands-in-india)
- **Israel:** Limitless Labs raised a $20M Series A (Jun 2026). It makes AI for CAD/CAM in CNC manufacturing, not simulation — [TNW](https://thenextweb.com/news/limitless-labs-20m-series-a-physical-ai-cnc-manufacturing). I found no Israeli physics-simulation start-up of any scale.
- **Taiwan:** I found nothing.

### Gaps
- Not verified: 云道智造 (Simright) and 十沣科技 in China, and start-ups in Korea, Taiwan and Israel beyond those above. The search budget ran out.

## 7. Investor exposure

### Takeaway
Exposure is limited to private rounds, thin secondary markets and listed strategic holders.

### Cited Findings
- **Secondary platforms:** PhysicsX appears on EquityZen (ticker "PHYX") and Hiive (no bids or asks shown) — [EquityZen](https://equityzen.com/company/physicsx/); [Hiive](https://www.hiive.com/securities/physicsx-stock)
- **Listed investor:** M&G, a listed asset manager, invested in PhysicsX's Series C.
- **Applied Intuition:** about $400M of secondary sales in the 2025 tender (Sacra).
- **Listed strategic holders:**
  - Siemens, Applied Materials and NVIDIA in PhysicsX.
  - NVIDIA in Luminary.
  - Samsung Electronics (via Samsung Ventures) and Applied Materials in Flexcompute.
  - AMD in Vinci.
  - CoreWeave owns Monolith.
  - IBM in BQP.

### Inferences
- **Realistic routes:**
  - Listed strategic holders, though each stake is immaterial to its parent.
  - Listed incumbents that may buy entrants (Siemens, Synopsys, Cadence, Dassault). This is speculative.
  - Growth funds that hold these names.
- I found no announced IPO for any entrant.

### Gaps
**Could not verify**
- PhysicsX:
  - The ~$50M 2026 revenue figure: I could not open Bloomberg or The Business Times directly.
  - Total funding: $487M versus about $500M.
  - The British Business Bank's reported $25M investment: the page was blocked.
- Valuations for Neural Concept, Luminary and Flexcompute; whether Flexcompute raised a $53M Series C in 2024.
- Vinci's customers and its accuracy claims.
- The Mistral/Emmi price (about €300M, from unnamed sources).
- When the CoreWeave/Monolith deal closed, and at what price.
- Whether Applied Intuition has closed a round at $30B or more.
- Project Prometheus round sizes (sources conflict).
- Any sign-off or certification acceptance of an entrant's results.
- Entrant results at AIAA DPW-8 or HLPW-6.
- The AutoCFD5 conclusions.
- Zenithon's headquarters.
- Chinese, Taiwanese and Israeli start-ups beyond those listed.

### Dated source list (all accessed 12 Nov 2026)
**PhysicsX**
- 2026-06-08: [PhysicsX Series C](https://physicsx.ai/newsroom/physicsx-announces-300m-series-c-to-accelerate-physics-ai-for-industrial-engineering); [Tech.eu](https://tech.eu/2026/06/08/physicsx-raises-300m-at-24bn-valuation/); [Resilience Media](https://resiliencemedia.co/physicsx-raises-300m-at-a-2-4b-valuation-for-ai-to-create-and-test-defence-and-other-hardware/)
- 2026-06 (date approximate): [New Market Pitch, citing Bloomberg](https://newmarketpitch.com/blogs/news/digital-twin-physicsx-overvalued)
- 2025-10-29 (filing date): [PhysicsX FY2024 accounts, Companies House](https://find-and-update.company-information.service.gov.uk/company/12134466/filing-history)
- 2026-10-27: [PhysicsX–Fortescue](https://physicsx.ai/newsroom/physicsx-and-fortescue-expand-partnership-to-accelerate-industrial-innovation-with-ai)
- 2026-10-08: [PhysicsX Singapore](https://www.physicsx.ai/newsroom/physicsx-launches-asia-pacific-hub-in-singapore-to-scale-ai-powered-industrial-engineering-across-the-region)
- 2026-03-11: [PhysicsX–CoreWeave](https://www.physicsx.ai/newsroom/physicsx-and-coreweave-partner-to-deliver-high-performance-physics-ai-for-advanced-industrials)
- 2026-08-07: [PX-Car-Aero-v1](https://physicsx.ai/newsroom/scaling-physics-ai-for-automotive-aerodynamics-part-ii-meet-px-car-aero-v1)
- 2026-08-11: [PLAID agent post](https://physicsx.ai/newsroom/how-an-ai-agent-cracked-an-industry-benchmark)
- 2024-12-04: [Siemens–PhysicsX](https://news.siemens.com/en-us/siemens-physicsx/)

**Neural Concept**
- 2025-12-18: [Series C](https://www.neuralconcept.com/press-release/neural-concept-closes-100m-funding-round)
- 2025-09-29: [Growth release](https://www.neuralconcept.com/press-release/neural-concept-100-percent-enterprise-growth)
- 2026-10-19: [MCP Bridge](https://www.neuralconcept.com/press-release/neural-concept-launches-mcp-bridge)
- 2026-03-25: [JLR](https://www.neuralconcept.com/industry-stories/jlr-nvidia-gtc-aerodynamic-engineering)
- 2025-08-05: [GM](https://www.neuralconcept.com/industry-stories/general-motors-pedestrian-safety)
- 2026-06: [Seoul office](https://www.neuralconcept.com/press-release/neural-concept-opens-seoul-office)
- 2026-09-10: [India](https://www.neuralconcept.com/press-release/neural-concept-expands-in-india)
- 2025-09-18: [CEO on benchmarking](https://www.neuralconcept.com/post/finding-the-path-to-value-in-engineering-ai-why-we-need-to-rethink-benchmarking)

**Luminary**
- 2024-03-13: [TechCrunch](https://techcrunch.com/?p=2677477)
- 2025-09-15: [Series B](https://luminary.ai/resources/luminary-cloud-secures-dollar72m-series-b-to-lead-the-physics-ai-era)
- 2025-04-09: [SHIFT models](https://luminary.ai/resources/introducing-luminary-shift-models-a-suite-of-physics-ai-foundation-models-to-transform-engineering-design/)
- 2026-02-24: [Private Cloud](https://luminary.ai/resources/luminary-introduces-luminary-private-cloud-to-bring-physics-ai-into-secure-air-gapped-defense-and-aerospace-environments)
- 2026-09-10: [DARPA](https://luminary.ai/resources/how-darpa-is-using-physics-ai-to-cut-flight-tests-by-10x/)
- 2025-04-03: [AutoCFD4](https://luminary.ai/resources/luminary-cloud-highlighted-as-the-fastest-cfd-solver-at-autocfd4/)
- 2026-01-14: [Washington Technology](https://washingtontechnology.com/companies/2026/01/luminary-cloud-expands-physics-ai-toolkit-defense-focused-models/410679/)

**Flexcompute**
- 2026-10-12: [Pulse 2.0](https://pulse2.com/flexcompute-raises-strategic-investment-from-samsung-ventures-and-applied-ventures/)
- 2021-11 (older): [Series B](https://www.flexcompute.com/blog/2021/11/19/flexcompute-secures-22m)
- 2026-06-15: [Vertical](https://flexcompute.com/blog/vertical-aerospace-10x-more-designs)
- 2025-05-27: [BETA](https://flexcompute.com/blog/designing-the-a250-in-the-age-of-instant-aerodynamics)
- 2024-02-12 (older): [Dufour](https://flexcompute.com/blog/the-dufour-aerospace-aero2-uav-optimal-design-through-high-fidelity-cfd)

**Other entrants**
- Vinci: 2026-10-06 [Advent](https://www.adventinternational.com/vinci-raises-250m-series-b-at-1-5b-valuation/); 2025-12-03 [SiliconANGLE](https://siliconangle.com/2025/12/03/vinci-nabs-46m-speed-chip-simulations-ai/)
- Applied Intuition: 2025-06 [Series F](https://appliedintuition.com/news/series-f); [Sacra](https://sacra.com/c/applied-intuition/); 2026-10-13 [Crypto Briefing](https://cryptobriefing.com/applied-intuition-30-billion-valuation-offers/)
- Monolith: 2025-10-06 [CoreWeave](https://coreweave.com/news/coreweave-to-acquire-monolith-expanding-ai-cloud-platform-into-industrial-innovation); 2025-10-23 [Imperial](https://www.imperial.ac.uk/news/articles/engineering/aeronautics/2025/aeronautics-spinout-monolith-ai-acquired-by-us-cloud-computing-company/)
- Emmi AI: 2026-05-19 [Emmi](https://www.emmi.ai/news/mistral-ai-acquires-emmi-ai); [Mistral](https://mistral.ai/news/accelerate-ai-native-industry); [French Tech Journal](https://frenchtechjournal.com/mistral-ai-buys-viennas-emmi-ai-in-eur300m-bid-to-own-europes-factory-floor/)
- 2026-02-25: [CIC/BeyondMath](https://www.cic.vc/beyondmath-completes-18-5-million-seed-round-to-scale-worlds-largest-foundational-physics-ai-model/)
- 2025-12-16: [Navier](https://pulse2.com/navier-5-6-million-seed/)
- 2025-08-21: [Pasteur Labs](https://www.prnewswire.com/news-releases/pasteur-labs-acquires-ai-startup-fosai-to-accelerate-adoption-of-ai-driven-physics-simulation-for-space--defense-applications-302535200.html)
- 2025-02-19: [nTop](https://develop3d.com/cad/ntop-acquires-cloudfluid-gpu-native-cfd-software/)
- 2026-05-26: [Quanscient](https://tech.eu/2026/05/26/quanscient-lands-eur10m-to-advance-ai-and-quantum-native-hardware-engineering/)
- [Sacra/Prometheus](https://sacra.com/c/project-prometheus)

**Validation, rules and regulators**
- 2026-04-27: [arXiv 2604.18491](https://arxiv.org/html/2604.18491v2)
- 2024-10: [McGreivy and Hakim](https://www.osti.gov/pages/biblio/2475825-weak-baselines-reporting-biases-lead-overoptimism-machine-learning-fluid-related-partial-differential-equations)
- 2026-10-14: [CarBench](https://arxiv.org/abs/2512.07847)
- 2026-10: [AutoCFD5](https://autocfd.org/presentations/)
- 2026-10-28: [The Race on FIA–AWS](https://www.the-race.com/formula-1/ai-will-help-design-future-f1-cars-in-new-fia-aws-deal/)
- [EASA AI](https://www.easa.europa.eu/en/domains/research-innovation/ai); [NRC ML24290A059](https://www.nrc.gov/docs/ML2429/ML24290A059.pdf)

**Incumbents and NVIDIA**
- 2026-03-11: [Ansys 2026 R1](https://news.synopsys.com/2026-03-11-Synopsys-Launches-Ansys-2026-R1-to-Re-Engineer-Engineering-with-Joint-Solutions-and-AI-Powered-Products)
- 2025-11: [NVIDIA Apollo](https://blogs.nvidia.com/blog/apollo-open-models); [PhysicsNeMo](https://developer.nvidia.com/physicsnemo)

**Regional**
- 2025-08-01: [kepple/RICOS](https://kepple.co.jp/articles/mf2gxo8ef4su)
- 2022-07-19 (older): [36Kr/Tianfu](https://www.36kr.com/p/1831315772563713)
- 2026-09-03: [AIM/BQP](https://analyticsindiamag.com/ai-news/ibm-ventures-invests-in-bqp-as-physics-platform-enters-production)
- [THEVC/Narnia Labs](https://thevc.kr/narnialabs)
