# Newer entrants in AI-for-physics and next-generation engineering simulation (as of 12 Nov 2026)

**Summary for the report writer (draft v1, 12 Nov 2026; being updated)**

- Money has concentrated in a few names. PhysicsX raised $300M at about $2.4B (8 Jun 2026). Vinci raised $250M at $1.5B post-money (Oct 2026). Neural Concept raised $100M (18 Dec 2025; valuation undisclosed). Luminary Cloud raised a $72M Series B (15 Sep 2025). Flexcompute took an undisclosed strategic investment from Samsung Ventures and Applied Ventures (12 Oct 2026). Applied Intuition is far larger, at $15B (Jun 2025) with reported offers of at least $30B, but it is autonomy and vehicle software rather than engineering physics.
- Consolidation has started: CoreWeave agreed to buy Monolith (6 Oct 2025, terms undisclosed), Mistral AI bought Emmi AI (19 May 2026, undisclosed), nTop bought cloudfluid (Feb 2025) and Pasteur Labs bought FOSAI (Sep 2025).
- Only two of the leading entrants own a "judge", a validated solver of their own: Flexcompute (Flow360 for CFD, Tidy3D for EM) and Luminary (a GPU-native CFD solver). PhysicsX and Neural Concept sell learned models plus a workflow and delivery layer that is trained on data from customers' or incumbents' solvers (PhysicsX's LGM-Aero was trained on Siemens Simcenter STAR-CCM+/Nastran data). Their models can be replaced by incumbents' tools (Ansys SimAI, Siemens/Altair PhysicsAI), by NVIDIA's open models or by customers' own models.
- Outside evidence is thin. Workshop entries are self-reported: Luminary and Flexcompute at AutoCFD4 (2024), and Luminary at AIAA HLPW5 (2024). The benchmark "records" (Neural Concept on DrivAerNet++, PhysicsX on the PLAID Tensile2D leaderboard) are self-published, and McGreivy and Hakim (NMI 2024) found 79% of ML-for-fluids papers used weak baselines. The Dallara/IBM preprint (arXiv 2604.18491) is an IBM model, not a start-up's. Its surrogate met Dallara's pre-set "usability" threshold on all 20 parts and the stricter "CFD-replacement" threshold on 18 of 20, so the prior framing ("met concept threshold, not replacement threshold") is only partly right. The authors still say the aim is not to replace solvers.
- Sign-off: I found no public case of a regulator or customer accepting an entrant's learned model for certification. Company material frames use as design exploration (Neural Concept's CEO: "If you think of it only as a replacement for simulation, you will be disappointed"; Luminary on DARPA work: "predictions, not permission").
- Investor exposure: private rounds only. The routes are listed strategic holders (Siemens, Applied Materials, NVIDIA, Samsung Electronics, AMD, CoreWeave) and secondary platforms for the largest names. No IPO has been announced (to be checked).

## 1. Who the entrants are: profiles, funding, customers, partnerships, acquisitions

### Takeaway
(draft) Four companies with real scale (PhysicsX, Neural Concept, Luminary, Flexcompute) plus one semiconductor-focused unicorn (Vinci) form the core. Applied Intuition is adjacent. Most other names are seed-stage or have been acquired.

### Cited Findings
**PhysicsX (London; PhysicsX Limited, company no. 12134466, incorporated 1 Aug 2019)** — [Companies House](https://find-and-update.company-information.service.gov.uk/search/companies?q=physicsx)
- Series C: $300M, oversubscribed, at about $2.4B, announced 8 Jun 2026 and led by Temasek. New investors: M&G and Intrepid Growth Partners. Existing investors: Applied Materials, Atomico, General Catalyst, July Fund, NGP, NVIDIA, Radius and Siemens. Company claims, unconfirmed: recognised revenue doubled year on year, booked revenue tripled, customer count more than doubled, headcount over 300 (doubled in 12 months). — [PhysicsX](https://physicsx.ai/newsroom/physicsx-announces-300m-series-c-to-accelerate-physics-ai-for-industrial-engineering). Tech.eu reports about 350 staff, about $500M raised in total and a valuation more than double the Series B. — [Tech.eu, 8 Jun 2026](https://tech.eu/2026/06/08/physicsx-raises-300m-at-24bn-valuation/)
- Series B: $135M, 22 Jun 2025, led by Atomico, with Temasek, Siemens, Applied Materials and July Fund joining. Total raised was then nearly $170M, the team was over 150, and the company says revenue more than quadrupled in two years (company claim). — [PhysicsX](https://physicsx.ai/newsroom/physicsx-raises-135m-series-b-to-usher-in-a-new-era-of-ai-native-engineering-and-manufacturing). The extension on 19 Nov 2025 added NVentures, taking the Series B above $155M at "nearly $1B" — [PhysicsX](https://www.physicsx.ai/newsroom/physicsx-announces-extension-to-series-b-round). Pulse 2.0 puts NVentures' cheque at $20M — [Pulse 2.0](https://pulse2.com/physicsx-series-b-extended/). The Series A was $32M in Nov 2023 — [PhysicsX newsroom](https://physicsx.ai/newsroom)
- FY2024 group accounts (filed 29 Oct 2025, audited by Saffery, unqualified):
  - Loss before tax £8.15M (2023: £4.28M); loss after the R&D tax credit £7.22M.
  - Cash £13.19M (2023: £21.46M); net assets £18.76M; average employees 74 (2023: 28).
  - The income statement was omitted under the small-companies regime, so turnover is not public.
  - Directors' stress test: a 20% revenue miss would still leave the company "cash positive".
  - Post-balance-sheet event: on 18 Jun 2025, Series B-1/B-2 preference shares were allotted for $123,999,788, plus $9,999,995.70 by stock transfer.
  - Source: [Companies House filing](https://find-and-update.company-information.service.gov.uk/company/12134466/filing-history)
- Share allotments in 2026: 5 Feb, 20 Apr, 8 Jun (Series C) and 3 Aug. Russel Tham was appointed director on 8 Jun 2026. — [Companies House](https://find-and-update.company-information.service.gov.uk/company/12134466/filing-history)
- Partnerships:
  - Siemens: LGM-Aero, trained on more than 25M geometries using Simcenter STAR-CCM+ and Nastran data (4 Dec 2024) — [Siemens](https://news.siemens.com/en-us/siemens-physicsx/). Extended to Simcenter X (23 Jul 2025); data-centre power work with Siemens and NVIDIA (17 Mar 2026).
  - Microsoft Discovery (19 May 2025).
  - Deutsche Telekom and NVIDIA sovereign cloud (4 and 18 Nov 2025; live 4 Feb 2026).
  - CoreWeave (11 Mar 2026); GB1 America's Cup (Mar 2026); Singapore hub (8 Oct 2026).
  - Fortescue: a multi-year expansion of a collaboration more than two years old, value undisclosed and with no production/pilot status given (27 Oct 2026).
  - Sources: [PhysicsX newsroom](https://physicsx.ai/newsroom); [Fortescue release](https://physicsx.ai/newsroom/physicsx-and-fortescue-expand-partnership-to-accelerate-industrial-innovation-with-ai)
- Resilience Media names Leonardo as a partner and customer. It says pricing is unclear and that the platform is optimised for NVIDIA chips. — [Resilience Media, 8 Jun 2026](https://resiliencemedia.co/physicsx-raises-300m-at-a-2-4b-valuation-for-ai-to-create-and-test-defence-and-other-hardware/)
- Engagement model: jointly scoped pilots of 1 to 3 months, with embedded data-science, simulation and ML teams. Early delivery is services-heavy. — [PhysicsX](https://physicsx.ai/newsroom/why-we-do-pilots-and-how-to-choose-a-good-one)

**Neural Concept (Lausanne; EPFL spin-off; founded 2018 or 2019 — its own releases conflict)**
- Series C: $100M, 18 Dec 2025, led by Goldman Sachs Alternatives Growth Equity, with Forestay, Alven, HTGF, D. E. Shaw Ventures and Aster. Valuation undisclosed. Company claims, unconfirmed: enterprise revenue up fourfold in 18 months; more than 50 customers, including GM, GE Vernova, Leonardo, Eaton, Safran, Renault Group and "multiple F1 teams". — [Neural Concept](https://www.neuralconcept.com/press-release/neural-concept-closes-100m-funding-round); [Tech.eu](https://tech.eu/2025/12/18/neural-concept-raises-100m-to-scale-ai-native-engineering/)
- Earlier rounds: $27M Series B (Jun 2024, led by Forestay) and $9.1M Series A (Jun 2022). — [Neural Concept press list](https://www.neuralconcept.com/newsroom/press-releases)
- Release of 29 Sep 2025 (company claims): enterprise adoption doubled since Jan 2025; upsells +40%; ARR growth "significantly outpaces burn rate"; partners with more than 70% of the largest OEMs and 40% of the top-100 tier-1 suppliers. — [Neural Concept](https://www.neuralconcept.com/press-release/neural-concept-100-percent-enterprise-growth)
- Products and offices: an AI design copilot (Jan 2026); MCP Bridge (19 Oct 2026), which lets agents drive CATIA, NX, ANSA, HyperMesh and Abaqus; offices in Seoul (Jun 2026) and India (Sep 2026). — [MCP Bridge](https://www.neuralconcept.com/press-release/neural-concept-launches-mcp-bridge)
- JLR (GTC, Mar 2026): runs on more than 20,000 simulations; design evaluations rose from about 50 to about 1,500 a day; the page says the platform "does not replace simulation". — [Neural Concept/JLR](https://www.neuralconcept.com/industry-stories/jlr-nvidia-gtc-aerodynamic-engineering)

**Luminary Cloud (San Mateo; domain now luminary.ai; CEO Pete Schlampp since Aug 2024)**
- Series B: $72M, 15 Sep 2025, led by N47, with Sutter Hill and NVentures. No valuation disclosed. — [Luminary](https://luminary.ai/resources/luminary-cloud-secures-dollar72m-series-b-to-lead-the-physics-ai-era); [SiliconANGLE](https://siliconangle.com/2025/09/15/luminary-cloud-raises-72m-advance-ai-driven-physical-product-design/)
- Owns a GPU-native CFD solver and sells SHIFT models: SUV (with Honda and NVIDIA; DoMINO architecture on PhysicsNeMo; trained on more than 1,000 DES runs at about 1.2 h each on H100s; open sample on Hugging Face), Wing (Otto), CCA, Submarine, Pump, Missile, Crash, Battery, Truck and NVH (27 Oct 2026). — [Luminary SHIFT](https://luminary.ai/resources/introducing-luminary-shift-models-a-suite-of-physics-ai-foundation-models-to-transform-engineering-design/); [Luminary resources](https://luminary.ai/resources)
- Named customers: Northrop Grumman (spacecraft thruster-nozzle surrogate), Joby and Otto. — [Luminary](https://luminary.ai/resources/luminary-cloud-secures-dollar72m-series-b-to-lead-the-physics-ai-era)

**Flexcompute (Boston; Stanford/MIT founders; more than 70 PhDs)**
- 12 Oct 2026: strategic investment from Samsung Ventures and Applied Ventures (the Applied Materials arm) plus unnamed others, amount undisclosed. — [Pulse 2.0](https://pulse2.com/flexcompute-raises-strategic-investment-from-samsung-ventures-and-applied-ventures/); [RuntimeWire](https://runtimewire.com/article/flexcompute-samsung-applied-ventures-physics-world-model)
- The last confirmed earlier round is a $22M Series B led by Coatue (29 Nov 2021). A $53M Series C in Jul 2024 appears only in databases (unverified). — [CB Insights](https://www.cbinsights.com/company/flexcompute/financials)
- Own GPU-native solvers: Flow360 (CFD, usage-based pricing) and Tidy3D (FDTD EM), plus PhotonForge, RF, GeometryAI and FlexAgent. Claims more than 250 companies and academic institutions as customers. Logos: Anduril, Beta, Coherent, Hermeus, Joby, Northrop Grumman, Samsung and Xanadu. — [Flexcompute](https://www.flexcompute.com/); [Flow360](https://www.flexcompute.com/flow360/)

**Vinci (Vinci4D; Palo Alto; founded 2023 by Hardik Kabaria and Sarah Osentoski)**
- $46M in seed and Series A (2 Dec 2025: Series A led by Xora, seed led by Eclipse, plus Khosla). — [SiliconANGLE](https://siliconangle.com/2025/12/03/vinci-nabs-46m-speed-chip-simulations-ai/)
- $250M Series B at $1.5B post-money (6–7 Oct 2026), co-led by Advent, Temasek and Xora, with AMD Ventures, Eclipse, Khosla and Madrona. — [Silicon Valley Invest Club](https://siliconvalleyinvestclub.com/2026/10/07/vinci-raises-250-million-and-hits-unicorn-status-at-a-1-5-billion-valuation/)
- Company claims (unconfirmed): three unnamed chipmakers have deployed it and more than 10 have benchmarked it; no customer training data is needed.

**Applied Intuition (adjacent: autonomy and vehicle software)**
- $600M Series F at $15B post-money (Jun 2025), of which about $400M was secondary. The Information (Oct 2026) reports offers of at least $30B (reported, not closed). Sacra estimates ARR of $830M in 2025 (estimate). — [Applied Intuition](https://appliedintuition.com/news/series-f); [Sacra](https://sacra.com/c/applied-intuition/)

**Acquired entrants**
- Monolith: CoreWeave (Nasdaq: CRWV) agreed to acquire it on 6 Oct 2025, terms undisclosed. Customers named: Nissan, BMW, Honeywell. — [CoreWeave](https://coreweave.com/news/coreweave-to-acquire-monolith-expanding-ai-cloud-platform-into-industrial-innovation)
- Emmi AI: acquired by Mistral AI on 19 May 2026, terms undisclosed, with more than 30 staff. It had raised a €15M seed in Apr 2025. — [Emmi AI](https://www.emmi.ai/news/mistral-ai-acquires-emmi-ai)

### Inferences
- (to be completed)

### Gaps
- (to be completed)

## 2. Independent validation
### Cited Findings
- Dallara/IBM preprint, arXiv 2604.18491 v2 (27 Apr 2026). It uses 625 RANS (k-ω SST) samples of a parametric LMP2 car, each about 2.4M cells.
  - Errors on drag (Cd) and downforce (Cl): GIST 0.6%/0.7%, GAOT 0.9%/1.0%, Transolver 1.2%/1.2%.
  - Dallara "established specific absolute error thresholds in advance" (values redacted). The "usability threshold is met for every part, while the CFD replacement threshold is met by 18/20 parts".
  - The authors state: "The objective is not to replace classical numerical solvers entirely."
  - Source: [arXiv](https://arxiv.org/html/2604.18491v2)
- McGreivy and Hakim (Nature Machine Intelligence 6, Oct 2024) found that 79% (60/76) of ML-for-fluid-PDE papers claiming to beat standard methods compared against a weak baseline, and that reporting biases are widespread. — [OSTI](https://www.osti.gov/pages/biblio/2475825-weak-baselines-reporting-biases-lead-overoptimism-machine-learning-fluid-related-partial-differential-equations); [arXiv 2407.07218](https://arxiv.org/abs/2407.07218)

## 3. Sign-off
- (to be completed)

## 4. Scoring the leaders
- (to be completed)

## 5. Threats and durable assets
- (to be completed)

## 6. Regional coverage
- (to be completed)

## 7. Investor exposure
- (to be completed)

## Interim findings v2 (12 Nov 2026), to merge into the sections above
- PhysicsX revenue: Bloomberg (Jun 2026) reported that the CEO expects about $50M of revenue in 2026 and aims to more than double it in 2027. It also reported about six months of unserved demand. This comes from Bloomberg via The Business Times (page not fetchable) and is cited by [New Market Pitch](https://newmarketpitch.com/blogs/news/digital-twin-physicsx-overvalued), which works out about 48x expected sales. Status: reported, not confirmed by company filings.
- Luminary's launch funding of "$115M" (13 Mar 2024) was $15M of equity plus $100M of debt, both from Sutter Hill. Other details from the same article:
  - Founded 2019 by Jason Lango and Juan Alonso (Stanford).
  - Pricing is per GPU-minute with no licence fee; a quick conceptual aircraft run costs under $90.
  - 73 staff and 33+ customer organisations at the time.
  - Source: [TechCrunch](https://techcrunch.com/?p=2677477)
- Flexcompute was founded in about 2016 by Zongfu Yu, Qiqi Wang (MIT) and Shanhui Fan (Stanford). Its Series A (Nov 2020) was led by WI Harper. Its $22M Series B (29 Nov 2021) was led by Coatue, with GGV, 3W, WI Harper and River Delta. — [Flexcompute blog](https://www.flexcompute.com/blog/2021/11/19/flexcompute-secures-22m); [WI Harper](https://wiharper.com/wi-harper-group-backed-flexcompute-raises-22m-to-accelerate-industrial-rd-with-advanced-engineering-computing)
- Dufour Aerospace case study (12 Feb 2024, co-written by Flexcompute): Flow360 is used for aero databases and structural loads; "Many certification authorities are now allowing" CFD data. No regulator acceptance of Flow360 is stated. — [Flexcompute](https://flexcompute.com/blog/the-dufour-aerospace-aero2-uav-optimal-design-through-high-fidelity-cfd)
- FIA and AWS (The Race, 28 Oct 2026): the FIA may use "surrogate approaches trained off our CFD data to shortcut the simulations" when writing rules for about 2030. Design is still "human-driven, engineer-driven". The ATR (aerodynamic testing restrictions) are not discussed. — [The Race](https://www.the-race.com/formula-1/ai-will-help-design-future-f1-cars-in-new-fia-aws-deal/)
- AutoCFD5 (Bologna, 8–9 Oct 2026) AI/ML talks came from Mistral (DrivAerML results using AB-UPT), Cadence, IngeniAI, KIT, Luminary ("Trustworthy AI Surrogates for DrivAerML… calibrated UQ"), Pasteur Labs, PhysicsX and Siemens. Neural Concept and NVIDIA were not listed. — [AutoCFD presentations](https://autocfd.org/presentations/)
- CarBench (arXiv 2512.07847, v3 14 Oct 2026; Elrefaie, Shu, Klenk, Ahmed) benchmarks 11 surrogates on DrivAerNet++, including Transolver, Transolver++ and AB-UPT. No commercial vendor models are included. — [arXiv](https://arxiv.org/abs/2512.07847)
- AIAA DPW-8 and AePW-4 were held on 6–7 Jun 2026 in San Diego. I found no results naming Flow360 or Luminary. — [AIAA](https://aiaa.org/courses/aiaa-drag-prediction-workshop/)
- Vinci (Advent release, 6 Oct 2026). Its "Continuous Physics Reasoning" combines automated design preparation, agentic orchestration, a "Foundation Model for Physics" and "GPU-native physics kernels". The company claims, unconfirmed: "deterministic, solver-accurate" results; zero-shot use with no customer training; 15B+ degrees of freedom in minutes; deployment on "flagship production engineering programs" with no customers named. — [Advent](https://www.adventinternational.com/vinci-raises-250m-series-b-at-1-5b-valuation/)
- Mistral/Emmi: the price is undisclosed. Unnamed sources put it "close to €300M in a mix of cash and stock". — [French Tech Journal](https://frenchtechjournal.com/mistral-ai-buys-viennas-emmi-ai-in-eur300m-bid-to-own-europes-factory-floor/)
- CoreWeave/Monolith: Davis Polk expected the deal to close by early Nov 2025. I found no closing release, though Sacra lists Monolith among CoreWeave's acquisitions. — [Davis Polk](https://www.davispolk.com/index%2Ephp/experience/coreweave-acquisition-monolith-ai)
- Project Prometheus: launched Nov 2025 with $6.2B; Bezos and Vik Bajaj are co-CEOs. Sacra reports a $12B round at about $41B (Jun 2026) and says the company is pre-revenue. It acquired General Agents (Nov 2025) and says it runs stress, heat and vibration simulations. — [Sacra](https://sacra.com/c/project-prometheus)
- Secondary platforms: EquityZen (ticker "PHYX"), Hiive (no bids or asks shown) and Caplight list PhysicsX; no prices are public. — [EquityZen](https://equityzen.com/company/physicsx/); [Hiive](https://www.hiive.com/securities/physicsx-stock)
- Regional:
  - RICOS (Japan): about ¥600M raised Jul 2025 (XTech Ventures and others, plus bank loans); about ¥300M Series A in Oct 2021 (UTEC, DG). NEDO listed a valuation of ¥1.2B in Apr 2024. An ML racing-aero contract with Toyota Gazoo Racing Development was signed in Apr 2026. — [kepple](https://kepple.co.jp/articles/mf2gxo8ef4su); [NEDO](https://www.nedo.go.jp/activities/startups/company45.html)
  - Narnia Labs (Korea): KAIST spin-off founded Apr 2022 (CEO 강남우/Kang Namwoo); Pre-A round Apr 2025; Hyundai Mobis brake-part case (2022). — [THEVC](https://thevc.kr/narnialabs); [MT](https://www.mt.co.kr/future/2022/10/11/2022100815564064481)
  - Tianfu Software 天洑 (China, AICFD): founded 2011; C round of "数亿元" (several hundred million yuan) in Jul 2022, led by GGV and Legend Capital. — [36Kr](https://www.36kr.com/p/1831315772563713)
  - BQP, formerly BosonQ Psi (US/India): IBM Ventures invested (3 Sep 2026), taking total funding to $8M. Company claims contracted revenue is up 8x since 2025. — [AIM](https://analyticsindiamag.com/ai-news/ibm-ventures-invests-in-bqp-as-physics-platform-enters-production)
  - Israel: Limitless Labs raised a $20M Series A (Jun 2026, Dell Technologies Capital and Square Peg). It does CAD/CAM manufacturing AI, not simulation. — [TNW](https://thenextweb.com/news/limitless-labs-20m-series-a-physical-ai-cnc-manufacturing)
