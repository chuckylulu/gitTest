# Physical-simulation software in South Korea, Taiwan, India and Israel (as of 12 Nov 2026)

Method note: built on the interrupted first attempt's digest (all its fetched facts re-used with their URLs), then extended. Mid-run, every search tool ran out (shared WebSearch budget; Firecrawl and Exa credits), so later evidence comes from direct fetches of company pages, exchange data endpoints and filings. No Hebrew-language search was possible. "Company claim" = unconfirmed by any outside party.

**Summary for the report writer**
1. No vendor in these four countries owns a globally accepted sign-off "judge" for flow, structures, EM or thermal. The judges that matter here are gatekeepers certifying foreign tools (TSMC's OIP certification, run with Cadence, Siemens and Synopsys; Samsung Foundry's SAFE QEDA programme) and state codes (Korea's own weather model, run alone since Apr 2026; Korea's SPACE nuclear safety code).
2. Best home-grown solver owners are private, seat-licence niche leaders: MIDAS IT (Korea; civil, geotechnical and mechanical FEA; 2025 revenue KRW 68.9bn, ~33% operating margin, aggregator data), CoreTech System/Moldex3D (Taiwan; moulding simulation incl. chip encapsulation and warpage; no public financials), FunctionBay/RecurDyn (Korea; multibody dynamics; tiny on a low-reliability estimate). They belong in the lower tiers of a global ranking: real solvers and export reach, but no certification role, no disclosed GPU solvers or usage pricing, and thin outside evidence.
3. Israel's listed relevance is fab metrology that depends on physical modelling: Nova (Q3 2026 revenue USD 287.8m, +28% YoY, GAAP operating margin 32%) and Camtek (Q3 USD 161.3m, ~80% advanced packaging, 2027 outlook >USD 800m). Strong businesses, but hardware sales tied to AI capex; a ~2028 financing-led pause would hit Camtek hardest. Private names: Foretellix (AV verification, NVIDIA-linked), Cognata (now leaning to defence autonomy), NextSilicon (HPC accelerator for simulation codes), Tomorrow.io (weather).
4. India's scale is engineering labour (Tata Elxsi, KPIT, LTTS, Tata Technologies, Cyient; Quest Global private, India IPO planned). None discloses simulation revenue. All say they are building AI agents (KPIT: 12,000 agents, ~9% of revenue "AI-first"; Tata Technologies: ~1,000 staff building agents) while moving to fixed price (KPIT ~70%, Tata Elxsi 43%, LTTS 35.6%). The market has de-rated them: KPIT −54% and Tata Elxsi −27% over 52 weeks. Indian simulation products (CCTech/simulationHub, BQP ex-BosonQ Psi) are small and private.
5. Listed pure-play simulation exposure is almost nil: E8 (KOSDAQ 418620; 2025 revenue KRW 1.7bn, operating loss KRW 11.2bn; flagged as a management-designated issue on 12 Nov 2026) and, as a reseller, CADMEN (TPEx 6791; Ansys/Synopsys channel; P/E 18.6).
6. Weather: KMA designing an AI foundation model; Taiwan's CWA uses AI typhoon-track models in a hybrid with physics models; India's BharatFS (6 km physics model) plus AI pilots; Israel's IMS runs NVIDIA's CorrDiff downscaler operationally.
7. Thin coverage: private Korean and Taiwanese firms (no DART/MOPS filings reached), Hebrew press, Indian start-ups (SankhyaSutra site down; Zeus Numerix, Paanduv not reached), ISRO codes.

---

## 1. South Korea

### Takeaway
Two credible owned-solver vendors (MIDAS IT, FunctionBay), an AI-for-device-modelling start-up (Alsemy), heavy in-house simulation at Samsung on foreign tools plus NVIDIA GPU libraries, and one listed micro-cap (E8). Korean demand is large (Synopsys's third-biggest geography) but flows mostly to foreign vendors.

### Cited Findings
**Map: vendors, ownership, size**
- MIDAS IT (마이다스아이티), private, founded 1 Sep 2000, co-CEOs Jung Seon-tae and Jung Seung-sik. Standalone (NICE data): revenue KRW 53.79bn (2022), 59.69bn (2023), 58.97bn (2024), 68.93bn (2025, +17%); operating profit 10.01bn (2023), 13.12bn (2024), 22.64bn (2025, ~32.8% margin); net 24.91bn (2025); staff 260 (2025), 247 (30 Jun 2026). Aggregator data, not DART-checked. — [JobKorea/NICE](https://m.jobkorea.co.kr/company/1776019?tabType=I)
- MIDAS products: MIDAS Civil, GTS NX, GEN, FEA, NFX, MeshFree, SOILWORKS, CIM; group also sells HR software. Offices: China (8 cities), USA, India (Mumbai 2008, Chennai 2023), Japan, UK, Russia, Singapore, Dubai, Philippines, Poland, Mexico, Australia. Claims "No. 1" in Korea (2004), China (2007), overseas (2008) — company claims. — [MIDAS group site, 3 Sep 2026](https://group.midasit.com/)
- MIDAS sells NFX/MeshFree as perpetual licences ("MTS" bundle); 2026 SME programme: 20 firms, ~KRW 400m, incl. 50% off the MTS perpetual licence; CFD for battery/electronics cooling is a stated target; group announced "inAX" AI-agent work transformation (20 Jul 2026 headline). — [ZDNet Korea, 18 Sep 2026](https://zdnet.co.kr/view/?no=20260918101125)
- FunctionBay (펑션베이), private, Pangyo: RecurDyn (multibody, flexible bodies, contact; "RecurDyn 2027" out) and Particleworks (a Prometech, Japan, product it distributes); no AI/GPU features or news on site. — [FunctionBay](https://functionbay.com/en). Estimated 2024 revenue USD 5.1m, 34 staff, founded 2000, no outside funding (low-reliability estimate). — [Latka](https://getlatka.com/companies/functionbay.com)
- Tae Sung S&E (태성에스엔이), private CAE channel/services firm, Seoul, co-CEOs 심진욱/박인규: training academy, e-learning, consulting, "2026 R1" seminars (Ansys release naming); vendors not named on portal; no revenue found. — [Tae Sung portal](https://www.etsne.com/). Note: a "태성 2025 revenue" search result was a different company (Taesung, KOSDAQ 323280).
- Alsemy (알세미), founded 2019, spun off from SK hynix's HiGarage venture programme; products Alsis (device modelling), Alsphere (process modelling), "Large Physics Model"; annual licence/subscription plus projects; cumulative KRW 16.8bn incl. KRW 7.5bn bridge round (Laguna, Hyundai Investment Partners, Now IB, KODIT); no named customers; US/Taiwan push planned. — [Edaily via Daum, 25 May 2026](https://v.daum.net/v/20260525122307460); round dated 14 May 2026, amounts conflict across databases — [THEVC](https://thevc.kr/alsemy/fundings)
- Virtual Lab (Materials Square), founded Jan 2016; pre-Series A ~KRW 0.7bn from DSC Investment and a supply deal with ATI (US), both undated. — [THEVC](https://thevc.kr/virtuallab). Narnia Labs (generative-design AI): last round Pre-A, Apr 2025, amount undisclosed — [THEVC](https://thevc.kr/narnialabs/fundings); Hyundai Mobis brake-part design cut from a month to a minute (2022, company-reported) — [MT](https://www.mt.co.kr/future/2022/10/11/2022100815564064481). MetaRiver Technology: not found in any source reached.
- E8 (이에이트, ex-E8IGHT, KOSDAQ 418620): NFLOW particle CFD (2014), NDX PRO digital twin (2021), tech-special listing Feb 2024, renamed May 2025, "physical AI" pivot Feb 2026, NFLOW Ai Apr 2026. IFRS (KRW bn): revenue 3.7 (2023), 2.3 (2024), 1.7 (2025); operating loss −5.3, −10.6, −11.2; FCF −15.7 (2025); Q1 2026 revenue 0.4, operating loss 2.7; backlog 6.3. — [Hanwha note, 26 Jun 2026 (IPO lead manager; Not Rated)](https://stock.pstatic.net/stock-research/company/16/20260629_company_649249000.pdf). Samsung Electronics digital-twin contract ~KRW 0.8bn; Hyundai Motor ontology contract ~KRW 0.9bn — [TheBell, 25 Mar 2026](https://www.mt.co.kr/article/2026032515359627862). NFLOW Ai = web SaaS with GNN + U-Net surrogate — [Dealsite, 17 Apr 2026](https://dealsite.co.kr/articles/160371); plan to buy an unnamed manufacturer as a "proving plant" plus a third-party placement — [Dealsite, 10 Aug 2026](https://dealsite.co.kr/articles/166892).

**In-house users and national infrastructure**
- Samsung Electronics: uses NVIDIA cuDSS/cuISS for sparse solves in TCAD; pursuing GPU acceleration of process and optical simulation; sMOL quantum-chemistry runs up to 5x faster with cuEST; PhysicsNeMo chip-scale thermal/mechanical workflow cut one AI-homogenisation case from ~18 h (32-core CPU) to 41 s (GPU), ~1,600x (vendor-published). — [NVIDIA blog, 8 Nov 2026](https://blogs.nvidia.com/blog/korea-physical-ai-ecosystem/). Samsung AI factory with >50,000 NVIDIA GPUs; cuLitho in Samsung's OPC platform, "20x" (company claim, 31 Oct 2025). — [NVIDIA](https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-and-Samsung-Build-AI-Factory-to-Transform-Global-Intelligent-Manufacturing/)
- Korea = Synopsys's third-largest region: USD 325.6m in the quarter to 31 Jul 2026 (202.1m a year earlier, with ~2 weeks of Ansys), USD 837.6m over nine months. — [Synopsys 10-Q, quarter to 31 Jul 2026 (EDGAR)](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000883241&type=10-Q)
- Hyundai/Kia: Kakao Mobility plans Level 4 development on NVIDIA Hyperion/Halos around Kia purpose-built vehicles (plan) — [NVIDIA blog, 8 Nov 2026](https://blogs.nvidia.com/blog/korea-physical-ai-ecosystem/). Hyundai's own virtual-development stack: not verified.
- TOP500 (Jun 2026): Samsung SSC-24 #25 (106.2 PF, H100); NHN Cloud #20 (137.4 PF, B200) and #40; Kakao #39; NAVER #72; Kakao Enterprise #74. — [TOP500](https://www.top500.org/lists/top500/list/2026/06/). KISTI-6 "Hangang" inaugurated 2 Nov 2026: 8,496 GPUs, 9,936 CPUs, 614 PF peak, 205 PB; beta since 26 Oct, full service 16 Dec 2026; ~KRW 440bn. — [ETNews, 2 Nov 2026](https://etnews.com/20261102000300)
- KMA: Korean model (Apr 2020) ran alongside the UK Unified Model for six years and runs alone from Apr 2026; AI weather/climate foundation-model structure designed Dec 2025; 208 GPUs secured Apr 2026; only licensed forecasters may issue forecasts. — [News1 via Daum, 28 May 2026](https://v.daum.net/v/20260528142448171)
- Nuclear: SPACE safety-analysis code developed domestically since 1990 to replace Westinghouse/ABB-CE codes; KHNP's research institute marked licensing of SPACE-based LBLOCA, SBLOCA and non-LOCA methodologies (workshop 20 Sep 2017, older item); 2025 symposium covered SPACE-based methods under new regulatory requirements (search summary of KNS documents; regulator decision text not found). — [KNS SPACE document](https://www.kns.org/uploads/SPACE.pdf)

**Framework — MIDAS IT** (strongest Korean candidate)
- (a) Position: owns solvers, but in civil/structural work the judge is the engineer of record plus national design codes; no evidence of regulator certification of MIDAS tools. Ease-of-use pieces (MeshFree for non-specialists) are the part agents could replace; the solver and code-check library are stickier.
- (b) Lead: only company claims of No. 1 rank; the outside evidence is financial (aggregator margins). No independent share data found.
- (c) Revenue: own software, sold as perpetual licences plus support (Sep 2026); no subscription, cloud or usage pricing found.
- (d) Finance: ~33% operating margin and net profit above operating profit in 2024-25 (aggregator); balance sheet, customer and country mix unknown; large China office network.
- (e) Resilience: demand follows construction and manufacturing budgets, weakly linked to AI capex, so all three AI scenarios matter mainly through agent-driven price pressure on seats; export-control exposure not established (Russia office opened 2012-13).
- Transitions: T1 seats→usage: nothing said or done. T2 GPUs: nothing found. T3 agents/APIs: group-level "inAX" agent programme (said, HR side); no CAE agent API found. T4 open source: nothing found. T5 learned models: nothing found. T6 acceptance: relies on engineers' sign-off. Must go right: keep design-code coverage current abroad, expose APIs to agents, add GPU solvers before buyers re-tender seats.

**Framework — FunctionBay** (second candidate; data thin)
- (a) Owns a multibody-dynamics solver (a tool, not a judge) and resells Particleworks. (b) No outside evidence of lead; competitors are Hexagon, Siemens, Altair and Synopsys/Ansys motion tools (not verified here). (c) Seat licences. (d) Unknown beyond a ~USD 5m revenue estimate. (e) Manufacturing R&D cycle; no AI, GPU, cloud or API statements found (T1-T6: nothing said or done on site). Must go right: GPU particle/MBD coupling and partner integration before larger suites absorb MBD.

### Inferences
- MIDAS IT is the only Korean vendor likely to place in a global ranking; FunctionBay is a niche footnote; Alsemy is the Korean name most exposed to transition T5 (learned compact models), but with no named customers or foundry PDK adoption it is unproven.
- Samsung's own GPU work (TCAD, OPC, PhysicsNeMo) suggests in-house teams plus NVIDIA libraries, not Korean vendors, capture Korea's chip-simulation shift.

### Gaps
- No DART filings opened (KIND returned 403): MIDAS IT, FunctionBay, Tae Sung S&E figures unconfirmed; MetaRiver unidentified; Korean Register/MOLIT acceptance of simulation not checked; NSSC approval text for SPACE not found.

---

## 2. Taiwan

### Takeaway
CoreTech System (Moldex3D) is Taiwan's one solver owner of global standing, strong in moulding and growing in chip encapsulation, but private, undisclosed and not foundry-certified. Taiwan's real power in simulation is TSMC as certifier, where no Taiwanese tool vendor appears.

### Cited Findings
- CoreTech System (科盛科技股份有限公司): registered 20 Nov 1995, Zhubei; responsible person 許嘉翔 (David Hsu); paid-in capital NT$412.2m; last registration change 1 Oct 2026. — [GCIS registry API](https://data.gcis.nat.gov.tw/od/data/api/6BBA2268-1367-4B42-9CCA-BC17499EBE8C?$format=json&$filter=Company_Name%20like%20%E7%A7%91%E7%9B%9B%E7%A7%91%E6%8A%80%20and%20Company_Status%20eq%2001&$skip=0&$top=10). Not found in TWSE listed, TPEx OTC, TPEx emerging or public-company registers (queried 12 Nov 2026) — [TWSE OpenAPI](https://openapi.twse.com.tw/v1/opendata/t187ap03_L), [TPEx OpenAPI](https://www.tpex.org.tw/openapi/v1/mopsfin_t187ap03_R). So: private, no financials.
- Moldex3D semiconductor page: encapsulation defects (voids, wire sweep, paddle shift, package warpage), EMC/LMC, potting, thermal-cycling fatigue; "over 100" R&D experts, "15 direct offices", "300+ channel locations", ISO 17025 Material Center, >9,000 materials (company claims); one STMicroelectronics case linked. — [Moldex3D semiconductor](https://www.moldex3d.com/solutions/solutions-by-industry/semiconductor/). IC-packaging modules include flow, cure, warp, stress, wire sweep, paddle shift, underfill, compression moulding, post-mould cure and a Cadence interface. — [Moldex3D sitemap](https://www.moldex3d.com/page-sitemap.xml)
- Moldex3D 2026: iSLM AI Chat, AI "Discovery Suite", AI fibre calibration, Moldibot chatbot, expanded Studio API with automation examples, DOE constraints; IC packaging speed-ups (Hybrid Zone CUF ~1/3 time; EBG Zone ~1/15 of full 3D); no GPU or licensing change mentioned (company claims). — [Moldex3D 2026](https://www.moldex3d.com/products/moldex3d-2026/). Founders incl. Prof. Rong-Yeu Chang; "thousands of companies" (claim) — [About](https://www.moldex3d.com/about/). Described as "the world's largest independent mould-flow software supplier" by a magazine (secondary, older). — [GVM](https://www.gvm.com.tw/article/69531)
- CADMEN / Taiwan Auto-Design (虎門科技, TPEx 6791, listed 14 Nov 2022, incorporated 1980): resells Ansys and Synopsys software, Minitab and SAP, plus training and consulting; no own solver stated. — [TPEx company data](https://www.tpex.org.tw/openapi/v1/mopsfin_t187ap03_O); [CADMEN](https://www.cadmen.com/). TTM revenue NT$840.9m, gross margin 40.8%, operating margin 10.8%, ROE 19.8% (to 11 Nov 2026). — [StockAnalysis](https://stockanalysis.com/quote/tpex/6791/statistics/)
- AnaGlobe: IC layout tools (Thunder; Thunder SiP router for fan-out RDL/interposer/substrate; GOLF OpenAccess editor "adopted since 2007"); no TSMC certification mentioned; ownership not stated. — [AnaGlobe](https://www.anaglobe.com/)
- TSMC as certifier: EDA Alliance has 11 members as of 23 Sep 2026, none Taiwanese; certification programme run with Cadence, Siemens EDA and Synopsys across A14/A16/N2P/N3C/3DFabric incl. thermal. — [TSMC OIP](https://www.tsmc.com/english/dedicatedFoundry/oip/eda_alliance). At the 23 Sep 2026 forum: Siemens Calibre 3DThermal certified for A16 static/transient thermal; multiphysics/thermal sign-off for wafer-scale packages still unfinished; "no validation regime exists for agent outputs comparable to tool certification" (analyst view). — [Futurum, 24 Sep 2026](https://futurumgroup.com/insights/tsmcs-oip-forum-turns-agentic-chip-design-demos-into-production-flows/). TSMC runs cuLitho in production (since 2024) and expanded NVIDIA tools across its fabs in Jun 2026 (20-50% gains, NVIDIA claim). — [NVIDIA, Jun 2026](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-and-TSMC-Bring-AI-Into-Fabs-to-Advance-Semiconductor-Design-and-Manufacturing/default.aspx)
- Computing: NCHC "Nano 4" #33 (81.6 PF, H200); Ubilink #56; NVIDIA TAIPEI-1 #97. — [TOP500, Jun 2026](https://www.top500.org/lists/top500/list/2026/06/)
- CWA: AI typhoon-track models since 2024 in a hybrid with numerical models, forecasters integrate; Google FGN, GenCast and ECMWF AIFS beat physics global models on 2025 tracks and Typhoon Bavi (Jul 2026); AI weak on short heavy rain (~25 km grid); 6th-gen supercomputer added GPUs; AI downscaling 25→2 km with NVIDIA; regional AI models with NTU/NCU. — [PTS, 22 Jul 2026](https://news.pts.org.tw/article/818850)
- Taiwanese AI-for-physics start-ups: none identified (no search possible after budget ran out).

**Framework — CoreTech System (Moldex3D)**
- (a) Position: owns a 3D moulding solver plus a measured material database (ISO 17025 lab, claim) — a harder asset than a wrapper. Used for package encapsulation/warpage decisions, but not a foundry-certified judge (absent from TSMC's alliance list).
- (b) Lead: magazine and company claims only; no outside share data. Competitors (Autodesk Moldflow, Synopsys/Ansys and Cadence in package analysis) not benchmarked here.
- (c) Revenue: own licences plus material-testing and consulting services; Moldiverse cloud apps partly free; pricing model undisclosed.
- (d) Finance: private, no disclosure.
- (e) Resilience: plastics/automotive cycle plus advanced-packaging capex (AI-linked: helps in steady/accelerating scenarios, hurts in a 2028 pause). China exposure unknown.
- Transitions: T1 nothing disclosed. T2 no GPU solver claimed (2026 speed-ups are physics-based model reduction). T3 done: Studio API and automation; AI chat assistants. T4 none. T5 partly done: AI fibre calibration and AI defect "Discovery" (claims). T6 no foundry/OSAT certification found. Must go right: become a qualified step in OSAT/foundry package flows; keep the materials-data moat; GPU or cloud solves.

### Inferences
- Taiwan's listed exposure to simulation software is a reseller (CADMEN), whose value depends on Synopsys keeping its channel after absorbing Ansys (not verified).

### Gaps
- CoreTech revenue, staff and ownership split; MOPS not queried for private firms; CWA AI verification numbers beyond press; no Taiwanese start-up scan.

---

## 3. India

### Takeaway
India's weight is in labour-hour engineering services, which fill gaps that agents and better tools can close; all five listed firms say they are building agents and moving to fixed price, and investors have cut their multiples sharply. Product vendors are early-stage; government codes are not reachable in public sources found.

### Cited Findings
**Engineering-services firms (none discloses a simulation/CAE revenue line)**
- Tata Elxsi, Q2 FY27 (Jul-Sep 2026; released 13 Oct 2026): revenue ₹1,055.7 cr (+15.0% YoY), EBITDA 21.9%, PAT ₹170.3 cr; transportation 55.3% of the services segment; headcount 11,149 vs 11,951 a year earlier; utilisation ~78% (past peak 81-82%); offshore 74.0%; fixed price 43.1% vs time-and-material 56.9%; top-5 clients 48.9%, top-10 59.2%; Europe 40.7%, Americas 33.2%, India 16.6%. — [Press release](https://d1y69b020rytqm.cloudfront.net/PDF/Financial-Statements/October2026/Tata-Elxsi-Q2'27-Press-Release-Final-1.pdf); [Fact sheet](https://d1y69b020rytqm.cloudfront.net/PDF/Financial-Statements/October2026/Tata-Elxsi-Q2'27-Investor-Deck-1.pdf)
- Tata Elxsi said enterprise AI budgets "take away from what could otherwise be discretionary budgets"; plans "pyramid" rebalancing to more junior staff; "if there is AI required, we would build it into our costs"; invested in KAVIA AI (Sep 2026). — [Call transcript, 13 Oct 2026](https://d1y69b020rytqm.cloudfront.net/PDF/Financial-Statements/October2026/TataElxsi-Earnings-Oct13-2026-1.pdf)
- KPIT (call 28 Oct 2026): "more than 9,000 users" of its AI platform, "12,000 engineering agents have been built", "roughly around 9% of the revenues" from AI-first projects, fixed price "about 70%" (71%); European car makers "looking to further cut their costs dramatically". — [Transcript (BSE)](https://www.bseindia.com/stockinfo/AnnPdfOpen.aspx?Pname=a7331811-fe14-4c79-896d-f0a9df901335.pdf). Quarterly sales ₹1,588 cr (Sep 2025) → ₹1,691 cr (Sep 2026); operating margin 19% → 16%; net profit ₹169 cr → ₹121 cr; FY26 net ₹637 cr vs ₹840 cr FY25. — [Screener](https://www.screener.in/company/KPITTECH/consolidated/)
- LTTS (call 19 Oct 2026): fixed price 35.6%, offshore 55.9%, headcount 24,035, attrition 14.7%, EBIT "mid-16%"; management: "the context for training the AI agents is very, very important... one of the biggest moat[s]". — [Transcript (BSE)](https://www.bseindia.com/stockinfo/AnnPdfOpen.aspx?Pname=6cb9b4cd-73ce-492a-bba5-68842c2de890.pdf). FY26 sales ₹10,996 cr, net ₹1,281 cr; L&T owns 73.51%. — [Screener](https://www.screener.in/company/LTTS/consolidated/)
- Tata Technologies (call 14 Oct 2026): "nearly 1,000" associates "developing and deploying AI agents"; USD 138m full-vehicle programme won from a European luxury OEM; headcount 12,895; cites VW's plan to cut 100,000 jobs by 2030 and BMW's German voluntary-exit scheme; ES-Tec (Germany) acquisition faces 12-18 months of headwinds. — [Transcript (BSE)](https://www.bseindia.com/stockinfo/AnnPdfOpen.aspx?Pname=043e9a8c-acc0-45a3-9570-ffcc69fef87d.pdf)
- Cyient (call 22 Oct 2026): CYiNGINE "agentic AI enabled lifecycle engineering" platform measured on customers' KPIs "for long-term outcome-based engagements"; agentic MRO offer launched Q2; CTO office for physical AI. — [Transcript (BSE)](https://www.bseindia.com/stockinfo/AnnPdfOpen.aspx?Pname=5be3ce61-d13e-48e8-a2c6-0fd164bbcb54.pdf). DET revenue ₹1,664 cr (+15.7% YoY, 9.3% organic), EBIT 14.2%. — [Cyient investors](https://www.cyient.com/investors)
- Quest Global (private, Singapore HQ): FY2025 revenue USD 1.1bn, >23,000 staff; Hillhouse bought ~5% at ~USD 4.5bn (Feb 2026); India IPO announced Feb 2026 (banks invited Mar 2026 for ~USD 1bn issue, per cited reports). — [Wikipedia (secondary)](https://en.wikipedia.org/wiki/Quest_Global)

**Product firms and public codes**
- CCTech's simulationHub (Pune): Autonomous Valve CFD, AI-driven Autonomous HVAC CFD needing "no CFD expertise", Buildings AI; subscriptions with free credits; claims ~5x cheaper than conventional CFD; customer logos mainly valve makers; funding not stated. — [simulationHub](https://www.simulationhub.com/)
- BQP (ex-BosonQ Psi): BQPhy quantum-inspired optimisation and physics solvers via MATLAB, Python SDK and APIs; "USD 5M oversubscribed seed" (undated); IBM Ventures investment article dated 4 Sep 2026; logos incl. NVIDIA, Tech Mahindra, IBM Quantum, AFRL; claims 25x faster CFD training. — [BQP](https://www.bqpsim.com/)
- SankhyaSutra Labs (lattice-Boltzmann CFD): site returned HTTP 503 twice; nothing verified. Zeus Numerix, Paanduv: not reached.
- Weather: BharatFS (IITM) adopted by IMD May 2025, 6 km TCo grid, runs on Arka (11.77 PF) and Arunika (8.24 PF); claimed gains are official claims. IMD's first AI system (monsoon-advance forecast) launched 12 May 2026; Uttar Pradesh 1-km AI-downscaled rainfall is a pilot. — [Drishti IAS, 14 May 2026 (secondary)](https://www.drishtiias.com/daily-updates/daily-news-analysis/imds-new-ai-driven-weather-forecasting-systems/print_manually). NCMRWF runs Pangu-Weather, FourCastNet and GraphCast experimentally on Arunika (MoES material via search summary). — [MoES](https://www.moes.gov.in/sites/default/files/PIB2201542.pdf)
- Skymet (private, Noida, 2003): own meso/micro-scale NWP for renewables; Series B USD 4.5m (DMGT's Asia Pacific, Omnivore; undated); monsoon misses in 2015 and 2019. — [Wikipedia (secondary)](https://en.wikipedia.org/wiki/Skymet_Weather_Services)
- Compute: Yotta Shakti Cloud #32 (84.3 PF, H100) is India's highest TOP500 entry. — [TOP500](https://www.top500.org/lists/top500/list/2026/06/). ISRO PRAVAH page returned 404; FEAST, C-DAC/NSM not verified.

**Framework — Tata Elxsi and KPIT** (India's most relevant listed candidates; labour-hour model)
- (a) Position: fill gaps (engineering hours, integration); no judge. (b) No outside evidence of a simulation lead. (c) Labour: Tata Elxsi 57% T&M; KPIT 70% fixed price, which lets it keep AI productivity gains. (d) Tata Elxsi: ~22% EBITDA, ROIC ~43%, minimal debt, but top-10 clients 59%; KPIT: margins down 3 points in a year, ROE 15%. (e) Steady growth: agents compress hours, so revenue per head must rise (Tata Elxsi revenue +15% with 7% fewer staff); 2028 pause: discretionary ER&D cut first (both cite budget pressure); acceleration: fastest cannibalisation. Cycle: European autos weak.
- Transitions: T1 said (outcome/fixed price), done (KPIT 70%; Tata Elxsi flat at 43%). T3 said and partly done (agents, KAVIA stake). T2/T4-T6 not applicable. Must go right: price on outcomes before clients re-price hours.

### Inferences
- Rising fixed-price shares and "agents built" counts are management claims; the hard signal is the de-rating (Section 6) and KPIT's falling margins.

### Gaps
- Simulation share of ER&D revenue (not disclosed by any firm); ISRO/DRDO code status; DGCA/CEMILAC acceptance of simulation; SankhyaSutra, Zeus Numerix, Paanduv.

---

## 4. Israel

### Takeaway
Israel's simulation-adjacent strength is model-based fab metrology (Nova) and inspection (Camtek), plus private AV-verification and HPC-hardware firms. No Israeli company sells general engineering solvers.

### Cited Findings
- Nova, Q3 2026 (released 5 Nov 2026): revenue USD 287.8m (+28% YoY; third straight record), products 231.9m, services 56.0m; GAAP gross margin 57.7%, operating margin 32%; GAAP net 90.0m; nine-month operating cash flow 219.1m; convertible notes 734.6m; Q4 guide 305-315m; drivers: memory (dimensional and materials metrology) and HBM/advanced-logic packaging; AI/modelling not cited as drivers. — [Nova PR](https://www.prnewswire.com/il/news-releases/nova-reports-record-third-quarter-2026-financial-results-302930609.html). ROE 22.3%, ROIC 20.4%, net cash ~USD 987m. — [StockAnalysis](https://stockanalysis.com/stocks/nvmi/statistics/)
- Nova describes its metrology as "combined with proprietary modeling algorithms and machine learning software"; software products Nova Fit, Nova MARS, Nova QED; technologies listed: physical modelling, machine learning, hybrid metrology, scatterometry (company claims). — [Nova](https://www.novami.com/)
- Camtek, Q3 2026 (4 Nov 2026): revenue USD 161.3m (+28%); GAAP gross margin 50.0%, operating margin 24.7% (non-GAAP 29.5%); cash 877.1m; convertible notes 489.2m; Q4 guide ~180m (FY2026 ~595m); 2027 outlook >800m; CEO: "a year of visibility for the first time". — [Camtek PR](https://www.prnewswire.com/il/news-releases/camtek-announces-results-for-the-third-quarter-of-2026-302929209.html). Advanced packaging ~80% of sales (call summary, secondary) — [MarketBeat](https://www.marketbeat.com/instant-alerts/transcript-camtek-q3-earnings-call-highlights-2026-11-04/); gross margin "stalled" (analyst view) — [Finviz/Earnings Whispers](https://finviz.com/news/415731/camtek-misses-the-whisper-by-a-penny-as-a-stalled-gross-margin-shadows-a-record-quarter-and-an-800m-2027-outlook)
- Foretellix: Foretify Toolchain/Evaluate/Generate for AV data curation, validation and synthetic scenarios; claims 2x faster validation, "10x more efficient" corner-case coverage; quotes from NVIDIA, Torc, Woven, Mazda; NVIDIA Alpamayo reference (31 May 2026) and NVIDIA Halos safety-validation work (21 Oct 2026); funding/HQ not on site. — [Foretellix](https://www.foretellix.com/)
- Cognata: OneSim simulation (sensor, closed-loop, scenario generation, "ADAS Safety Regulations") plus AVBox autonomy retrofit for off-road/defence (Jan 2026 push); funding, HQ, certifications not on site. — [Cognata](https://www.cognata.com/)
- NextSilicon: Maverick-2 dataflow accelerator for HPC/AI, "4x GPU performance" and C/C++/Fortran/OpenMP/Kokkos without rewrites (company claims); placed in Sandia's Vanguard programme for NNSA simulation. — [NextSilicon](https://www.nextsilicon.com/)
- Tomorrow.io (Israel-specific only): co-founded 2016 by Shimon Elkabetz, Itai Zlotnik, Rei Goffer; 2019 report of an international operations centre in Tel Aviv; HQ Boston; ~218 staff (2026). — [Wikipedia (secondary)](https://en.wikipedia.org/wiki/Tomorrow.io)
- Israel Meteorological Service: runs NVIDIA Earth-2 CorrDiff, trained to emulate its ICON model from ECMWF IFS input; "90%" compute saving at 2.5 km (vendor case study). — [NVIDIA case study](https://www.nvidia.com/en-us/case-studies/israel-meteorological-service)
- Compute: NVIDIA Israel-1 #59 (41.5 PF); SDS AI clusters #70/#71 (B200). — [TOP500](https://www.top500.org/lists/top500/list/2026/06/)

**Framework — Nova**
- (a) Position: measurement hardware plus physical models whose results fabs use for in-line process control — a judge inside customers' process windows (qualified per fab, not by a regulator). Hard physical constraint: AI can improve the models but cannot measure.
- (b) Lead: record growth outpacing the fab-equipment cycle; share data not checked here.
- (c) Revenue: mostly one-off systems (~81% products), services ~19%; modelling software bundled.
- (d) Finance: 57-59% gross, ~30% operating margin, net cash ~USD 1bn, convertibles outstanding; customer and China concentration not checked.
- (e) Steady growth: tracks memory/HBM and advanced-logic capex; 2028 pause: memory and packaging orders fall; acceleration: upside. Export controls on China fab sales are a risk (exposure not checked).
- Transitions: T5 said (physics plus ML models) and done in product names; T2/T3 not disclosed. Must go right: keep model accuracy lead at gate-all-around and HBM nodes.

**Framework — Camtek**
- (a) Inspection/metrology for advanced packaging; judges yield, accepted by customers; less reliance on physical models than Nova. (b) Lead shown only by growth. (c) Systems sales. (d) 50% gross margin, net cash. (e) Most exposed to the AI-capex scenarios (~80% advanced packaging). Transitions largely not applicable.

### Inferences
- For a simulation ranking, Nova is the Israeli name with the clearest "physics model as judge" role; Foretellix aims to be a verification judge for AV safety but shows no regulator acceptance.

### Gaps
- Hebrew-language search (Globes, Calcalist) not done; Israeli R&D centres of Synopsys, Cadence, Siemens not verified; Foretellix/Cognata/NextSilicon funding not verified; no Israeli engineering-simulation or AI-for-physics start-up identified.

---

## 5. Boundary of trust: who certifies, by country

### Takeaway
Certification sits with foreign-tool gatekeepers (TSMC, Samsung) and national agencies; acceptance of learned models is emerging only in weather and inside fabs, always paired with physics models or human forecasters.

### Cited Findings
- Korea: Samsung SAFE QEDA certifies EDA tools to its process requirements — [Samsung](https://semiconductor.samsung.com/foundry/safe/); nuclear licensing via SPACE-based methodologies (2017, older) — [KNS](https://www.kns.org/uploads/SPACE.pdf); weather forecasts legally restricted to licensed forecasters; KMA's own model now sole operational model — [Daum, 28 May 2026](https://v.daum.net/v/20260528142448171).
- Taiwan: TSMC certifies tools with three EDA vendors; thermal/multiphysics sign-off for wafer-scale packages unfinished; no validation regime for agent outputs — [TSMC](https://www.tsmc.com/english/dedicatedFoundry/oip/eda_alliance), [Futurum](https://futurumgroup.com/insights/tsmcs-oip-forum-turns-agentic-chip-design-demos-into-production-flows/). CWA keeps forecasters integrating AI and physics tracks — [PTS](https://news.pts.org.tw/article/818850).
- India: IMD adopted a physics model (BharatFS); AI products remain pilots — [Drishti IAS](https://www.drishtiias.com/daily-updates/daily-news-analysis/imds-new-ai-driven-weather-forecasting-systems/print_manually).
- Israel: IMS operational use of an AI downscaler trained on its physics model — [NVIDIA](https://www.nvidia.com/en-us/case-studies/israel-meteorological-service).

### Gaps
- Not verified: Korean Register and Indian Register rules on simulation in lieu of tests; India's DGCA/CEMILAC/ARAI and Israel's aviation and transport regulators; any acceptance of learned models by a nuclear or aviation regulator in these countries.

---

## 6. Entry-point data (valuation and access) — separate from quality evidence

### Takeaway
Listed exposure is mostly indirect (metrology, services, a reseller). Israeli metrology trades near the top of its own multiple range; Indian services trade near the bottom of theirs.

### Cited Findings (prices at close 11-12 Nov 2026 unless stated)
- E8 (KOSDAQ 418620): ₩1,904 (12 Nov, +13.1%); market value ₩7.6bn (StockAnalysis, 3.97m shares) vs ₩11.7bn (Naver) vs ₩10.0bn (Stockhub) — share count unsettled after events; Naver 52-week high/low ₩11,700/₩1,200 adjusted vs ₩2,340/₩396 unadjusted, consistent with a ~5:1 consolidation (no trading rows 9 Oct-3 Nov); Naver flags it as a management-designated issue (관리종목); P/S ~3.6 on TTM revenue ₩1.88bn, P/B 0.7-0.8, no P/E; foreign holding ~1.7-1.9%; Q3 report due ~13-14 Nov 2026. — [StockAnalysis](https://stockanalysis.com/quote/kosdaq/418620/statistics), [history](https://stockanalysis.com/quote/kosdaq/418620/history/), [Naver API](https://m.stock.naver.com/api/stock/418620/integration), [Stockhub](https://www.stockhub.kr/en/stock/418620). Pre-event: ₩890 and ₩17.7bn on 25 Jun 2026; −76.7% over the 12 months to then — [Hanwha](https://stock.pstatic.net/stock-research/company/16/20260629_company_649249000.pdf)
- CADMEN (TPEx 6791): NT$88.00; market value NT$1.83bn; P/E 18.6 (FY21-25 range 13.4-32.7); P/S 2.18 (1.8-4.2); EV/EBITDA 12.6; yield 4.0%; 52-week −19.3%; ~15.7k shares/day; results 16 Nov 2026. — [Stats](https://stockanalysis.com/quote/tpex/6791/statistics/), [ratios](https://stockanalysis.com/quote/tpex/6791/financials/ratios/)
- Nova (Nasdaq NVMI; also reports on TASE): USD 340.62; market value USD 10.83bn; P/E 39.0, forward 25.7 (FY21-25: 16.7-44.9); P/S 10.8 (4.1-11.4); EV/EBITDA 30.2; 52-week +7.1%; next catalyst Q4 results vs 305-315m guide (date not confirmed). — [Stats](https://stockanalysis.com/stocks/nvmi/statistics/), [ratios](https://stockanalysis.com/stocks/nvmi/financials/ratios/), [TASE filing](https://mayafiles.tase.co.il/rpdf/1779001-1780000/P1779897-00.pdf)
- Camtek (Nasdaq CAMT): USD 107.05; market value USD 5.00bn; P/E 40.4, forward 21.6 (FY21-24: 12.2-39.6; FY25 96.0 distorted); P/S 9.2 (3.0-9.9); EV/EBITDA 31.8; 52-week −3.7%; catalysts: Q4 (~180m guide), 2027 >800m outlook. — [Stats](https://stockanalysis.com/stocks/camt/statistics/), [ratios](https://stockanalysis.com/stocks/camt/financials/ratios/)
- Tata Elxsi (NSE/BSE): ₹3,862; ₹240.4bn (~USD 2.5bn at ~₹96/USD, LTTS's realised Jul-Sep 2026 rate); P/E 35.9, forward 29.5 (FY22-26: 100.2, 49.1, 61.2, 41.4, 39.4); P/S 5.9 (22.2 in FY22); EV/EBITDA 24.2; 52-week −26.9%; yield 1.9%; next results 8 Jan 2027. — [Stats](https://stockanalysis.com/quote/nse/TATAELXSI/statistics/), [ratios](https://stockanalysis.com/quote/nse/TATAELXSI/financials/ratios/)
- KPIT: ₹558.05; ₹151.9bn; P/E 28.6, forward 21.3 (FY22-26: 59.0, 65.6, 67.8, 42.2, 27.1); P/S 2.2 (8.3 in FY24); EV/EBITDA 12.7; 52-week −54.0%; promoter sale 4 Nov 2026; investor conferences 16 and 18 Nov 2026. — [Stats](https://stockanalysis.com/quote/nse/KPITTECH/statistics/), [ratios](https://stockanalysis.com/quote/nse/KPITTECH/financials/ratios/), [Screener](https://www.screener.in/company/KPITTECH/consolidated/)
- LTTS: ₹4,265; ₹452.5bn; P/E 29.4 (FY22-26: 56.3, 29.4, 44.5, 37.6, 25.9); P/S 3.9; EV/EBITDA 19.7; 52-week +3.9%; float limited (L&T 73.5%). — [Stats](https://stockanalysis.com/quote/nse/LTTS/statistics/), [ratios](https://stockanalysis.com/quote/nse/LTTS/financials/ratios/)
- Tata Technologies: ₹683.60; ₹277.6bn; P/E 49.3, forward 32.2 (FY24-26: 60.9, 40.7, 37.8); P/S 4.4; EV/EBITDA 28.0; 52-week −0.2%; promoters 55.2%. — [Stats](https://stockanalysis.com/quote/nse/TATATECH/statistics/), [ratios](https://stockanalysis.com/quote/nse/TATATECH/financials/ratios/)
- Cyient: ₹1,088; ₹113.3bn; P/E 32.1, forward 16.7 (FY22-26: 19.6, 21.3, 32.4, 22.6, 19.4); P/S 1.4; EV/EBITDA 12.7; 52-week −6.1%; ROE 6.9%. — [Stats](https://stockanalysis.com/quote/nse/CYIENT/statistics/), [ratios](https://stockanalysis.com/quote/nse/CYIENT/financials/ratios/)
- Access: Nova and Camtek trade in USD on Nasdaq (deepest liquidity). Indian names trade on NSE/BSE; no ADR/GDR found for any of them. E8 and CADMEN are local-only and illiquid. No route for private firms (MIDAS IT, FunctionBay, CoreTech, Tae Sung, Alsemy, Foretellix, Cognata, NextSilicon, Tomorrow.io, CCTech, BQP, Skymet); Quest Global plans an Indian IPO.

### Gaps
- Foreign-investor rules (Korea's account registration regime, Taiwan's foreign-investor registration with TWSE, India's SEBI FPI registration and limits) were not re-verified in this session.

---

## 7. Could not verify; dated source list

**Could not verify**
- MIDAS IT, FunctionBay, Tae Sung S&E audited financials (DART not reachable); FunctionBay's revenue rests on a Latka estimate.
- CoreTech revenue, headcount, shareholders; whether any OSAT/foundry qualifies Moldex3D in sign-off flows.
- E8 share count, consolidation ratio and the reason for the management designation (inferred from Naver fields only).
- NSSC decision approving SPACE; Korean Register, MOLIT, DGCA, CEMILAC, ARAI, Israeli regulator positions on simulation.
- Alsemy customers or PDK use; Virtual Lab and Narnia Labs round sizes; MetaRiver Technology's identity.
- SankhyaSutra, Zeus Numerix, Paanduv; ISRO FEAST/PRAVAH status; C-DAC/NSM.
- Foretellix, Cognata, NextSilicon funding and HQ details; Israeli R&D centres of global vendors; any Hebrew-language coverage.
- Nova/Camtek China exposure and customer concentration; Q4 results dates.
- Foreign-investor access rules in all four markets.

**Dated sources (publication or data date)**
- 2026-11-12: StockAnalysis statistics/ratios pages (E8, CADMEN, Nova, Camtek, Tata Elxsi, KPIT, LTTS, Tata Technologies, Cyient); Naver mobile API (E8); TWSE/TPEx OpenAPI registers; Screener pages.
- 2026-11-08: [NVIDIA blog, Korea physical AI](https://blogs.nvidia.com/blog/korea-physical-ai-ecosystem/).
- 2026-11-05: [Nova Q3 2026](https://www.prnewswire.com/il/news-releases/nova-reports-record-third-quarter-2026-financial-results-302930609.html). 2026-11-04: [Camtek Q3 2026](https://www.prnewswire.com/il/news-releases/camtek-announces-results-for-the-third-quarter-of-2026-302929209.html).
- 2026-11-03/10-28/10-25/10-19: KPIT, Cyient, LTTS, Tata Technologies call transcripts (BSE links above). 2026-11-02: [ETNews KISTI-6](https://etnews.com/20261102000300).
- 2026-10-13: Tata Elxsi Q2 FY27 press release, fact sheet, transcript.
- 2026-10-01: GCIS CoreTech registration change. 2026-09-24: [Futurum on TSMC OIP](https://futurumgroup.com/insights/tsmcs-oip-forum-turns-agentic-chip-design-demos-into-production-flows/). 2026-09-23: [TSMC EDA Alliance list](https://www.tsmc.com/english/dedicatedFoundry/oip/eda_alliance).
- 2026-09-18: [ZDNet Korea on MIDAS IT](https://zdnet.co.kr/view/?no=20260918101125). 2026-09-03: [MIDAS group site](https://group.midasit.com/).
- 2026-08-10, 07-30, 04-17: Dealsite on E8. 2026-07-22: [PTS on CWA AI](https://news.pts.org.tw/article/818850). 2026-07-21, 03-25: TheBell on E8. 2026-06-26: [Hanwha E8 note](https://stock.pstatic.net/stock-research/company/16/20260629_company_649249000.pdf). 2026-06: [TOP500](https://www.top500.org/lists/top500/list/2026/06/).
- 2026-05-28: [KMA briefing](https://v.daum.net/v/20260528142448171). 2026-05-25: [Alsemy profile](https://v.daum.net/v/20260525122307460). 2026-05-14: [IMD AI systems](https://www.drishtiias.com/daily-updates/daily-news-analysis/imds-new-ai-driven-weather-forecasting-systems/print_manually).
- 2026 (undated pages): Moldex3D 2026 and semiconductor pages; Foretellix, Cognata, NextSilicon, Nova, BQP, simulationHub, CADMEN, AnaGlobe, FunctionBay, Tae Sung, Samsung SAFE sites; Wikipedia (Quest Global, Skymet, Tomorrow.io; last edits 2026).
- 2025-10-31: [NVIDIA–Samsung AI factory](https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-and-Samsung-Build-AI-Factory-to-Transform-Global-Intelligent-Manufacturing/). Older, flagged: SPACE licensing (2017), Narnia/Hyundai Mobis (2022), MIDAS buyback headline (2022), GVM magazine on Moldex3D (undated, older).
