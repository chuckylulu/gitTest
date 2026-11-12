# Self-tuning instruments: software layer, AI-model suppliers, control interfaces and value capture (as of 12 November 2026)

Status: OUTLINE - research in progress. Sections are filled as findings are verified.

Labels used: [independently confirmed: by whom] / [company claim, not independently confirmed] / [secondary report] / "could not verify".
Each section uses the sub-headings Takeaway / Cited Findings / Inferences / Gaps.

## 1. Map of the software layer and model suppliers
(pending)

## 2. Interface-openness table
(pending)

## 3. Value-capture evidence
(pending)

## 4. Government programmes
(pending)

## 5. Test of the priors
(pending)

## 6. Leading software-layer companies and NVIDIA (tests a, b, c, e; T1-T5)
(pending)

## 7. Companies considered and left out
(pending)

## 8. Where the evidence contradicts the thesis
(pending)

## 9. What could not be verified
(pending)

## 10. Sources with dates
(pending)

---
## INTERIM FINDINGS LOG (raw, to be merged into sections above)

### Thermo Fisher x NVIDIA (12 Jan 2026)
- Business Wire release dated 2026-01-12: "Thermo Fisher Scientific announces strategic collaboration with NVIDIA leveraging AI to advance scientific instrumentation and accelerate laboratory performance". Thermo Fisher pairs instrument/lab-software expertise with NVIDIA AI infrastructure "including NVIDIA DGX Spark", NeMo, BioNeMo. Kimberly Powell (NVIDIA VP Healthcare): "era of 'lab-in-the-loop' science where the trinity of AI, agents and instruments will be able to scale scientific discovery at industrial pace." [company claim] Sources: https://www.businesswire.com/news/home/20260112999582/en/ (403 on fetch); syndicated https://business.mammothtimes.com/mammothtimes/article/bizwire-2026-1-12-thermo-fisher-scientific-announces-strategic-collaboration-with-nvidia-leveraging-ai-to-advance-scientific-instrumentation-and-accelerate-laboratory-performance ; https://www.chemeurope.com/en/news/1187881/
- "150 DGX Spark units at Thermo Fisher sites" appears only on rallies.ai -> could not verify.

### Thermo Fisher x OpenAI (16 Oct 2025)
- Strategic collaboration; first focus PPD clinical research; OpenAI APIs into product development, service delivery, customer engagement; ChatGPT Enterprise to workforce. Instrument control not mentioned. Source: https://ir.thermofisher.com/investors/news-events/news/news-details/2025/Thermo-Fisher-Scientific-to-Accelerate-Life-Science-Breakthroughs-with-OpenAI/default.aspx

### NVIDIA instrument products (ISC Hamburg, 22-26 Jun 2026)
- DAQIRI (Data Acquisition for Integrated Real-time Instruments), networking library within Holoscan; used by CERN/UChicago/UCL A-GHOST project on ATLAS data. cuPhoton (upcoming; telescope/laser/X-ray data; Rubin LSST tests; Princeton co-developed): "accelerated the ingestion of FITS files by 14,900x". ALCHEMI NIM (BGR, BMD released Mar 2026), ALCHEMI VASP microservice early access. Lila Sciences integrated full NVIDIA stack (Megatron-LM, Nemotron 3, NeMo RL, BioNeMo, Triton, Omniverse). [company claims] Source: https://usa-automation.net/news/112167-nvidia-introduces-ai-software-libraries-for-scientific-research (syndicated NVIDIA release, 24 Jun 2026)
- GTC Berlin healthcare release: Automata, Benchling, Danaher and others using BioNeMo to build scientific agents linking autonomous labs. Source: https://nvidianews.nvidia.com/news/healthcare-and-life-sciences-leaders-build-on-nvidia-to-advance-drug-discovery-and-expand-patient-care
- NVIDIA blog (Jan 2026): ALS Accelerator Assistant LLM multi-agent on EPICS. https://blogs.nvidia.com/blog/ai-copilot-berkeley-x-ray-particle-accelerator ; HPCwire 2026-01-09

### Genesis Mission
- EO 14363 signed 24 Nov 2025. Platform = "American Science and Security Platform"; "connects and integrates infrastructure (computing infrastructure together with other scientific instrumentation and DOE assets), data, and models". American Science Cloud APIs (AmSC APIs) include "Core agentic framework: Orchestration, Reasoning models, Telemetry & control". Consortium working groups incl. "data integration and standards" and "robotics and automation". 26 challenges incl. "Achieving AI-Driven Autonomous Laboratories", "Enhancing Particle Accelerators for Discovery" ("Deploying AI to make accelerators adaptive and autonomous"). Early projects: MOAT (Multi-Office Accelerator Operations & Controls), SYNAPS-I (Light and Neutron Imaging FM), OPAL-OMAHA (Bio/Autonomous Labs), Autonomous Microelectronics Consortium. RFA $293M; Phase I $0.5-0.75M/9 months; Phase II $6-15M/3 yrs. Source: DOE SC SCAC slides 2026-03-27 https://science.osti.gov/-/media/About/pdf/scac/meetings/2026/DOE-Genesis-Mission-Launched---2026-03-27.pdf
- 22 Jul 2026: 278 projects selected (87 lab-led, 168 university, 19 company, 4 nonprofit); 342 institutions incl. 157 companies; largest $60M nuclear; "Awardees will gain access to the Genesis Mission Platform, including AI agent frameworks, advanced AI models". No open-interface requirement stated. https://www.energy.gov/articles/secretary-energy-chris-wright-announces-first-genesis-mission-projects-selected-accelerate
- Feb 2026: MOUs with 24 initial partners incl. NVIDIA, Anthropic, OpenAI, Google, Microsoft, IBM, AWS, AMD... [secondary report] https://techinformed.com/doe-and-24-organizations-sign-ai-collaboration-deal/ ; consortium >$800M commitments from 40 orgs by July [secondary] https://fedscoop.com/energy-department-demo-genesis-mission-platform-rfa-awards/

### Lila Sciences / Periodic Labs funding
- Lila: Series A $350M total incl. $115M extension led by NVentures -> valuation >$1.3B, total raised $550M [Reuters via Yahoo] https://finance.yahoo.com/news/exclusive-ai-lab-lila-sciences-101645837.html ; Jun 2026 Bloomberg: talks to raise ~$2B at ~$8.5B pre-money [secondary report] https://news.bloomberglaw.com/private-equity/lila-sciences-said-in-talks-for-funds-at-8-5-billion-valuation ; not confirmed closed as of Jul 2026.
- Periodic Labs: $300M seed Sept 2025 (~$1.3B val per some aggregators, conflicting); May 2026 Forbes: advanced talks to raise >=$500M at $7.5B [secondary] https://dealroom.co/news/127042-periodic-labs-eyes-7b-valuation-fivefold-jump-in-six-months/

### Anthropic Model Hardware Standard (27 Aug 2026) - PRIMARY
- https://www.anthropic.com/news/model-hardware-standard-research-preview : "a shared specification for AI agents to safely operate physical devices"; research preview, by application (waitlist modelhardwarestandard.com); began with HHMI Janelia; driver with read/write primitives, discovery format, reference file incl. "what safety limits will be enforced"; control via MCP, CLI, code files; "MHS works with any device that has a programmable interface"; model-agnostic; plan to open-source after preview. Pilots: Genentech (BCA assay), UW Baker/Pinglay labs, CMU (~3x faster serial dilution), Janelia (rig with "seven different vendor programs without a shared interface"), QuEra (laser relock recovered 99.3% without human), Tetsuwan Scientific. Companies: AWS (Strands Robots), Automata (LINQ), Danaher (exploring), Doosan Robotics, MBF Bioscience (ScanImage driver), QIAGEN (QIAsymphony Connect PoC), Tecan (Fluent), Universal Robots, Hugging Face (LeRobot), Raspberry Pi. Limits: does not work with hardware lacking a programming interface; Genentech had to show Claude foaming was physical failure. [company claim; partner-reported results]
- Fortune 2026-08-27: Jonah Cool (Anthropic): scientific equipment "suffers from proprietary solutions that are very brittle"; "We want to avoid vendor lock-in for scientists." Kemeny: "In the future, scientists can buy these devices and out of the box it works." No pricing disclosed. https://fortune.com/2026/08/27/anthropic-makes-first-move-into-physical-ai-with-universal-standard-for-scientists-manufacturing/
- noze.it 2026-08-29: spec text, licence, conformance suite not yet public. https://www.noze.it/en/insights/model-hardware-standard-agents-lab-instruments/

### Keysight MCP Server for Instrument Control (2026)
- Connects MCP clients (Claude Code, Claude Desktop, GitHub Copilot) to Keysight signal/network analyzers, oscilloscopes, power supplies, precision & semiconductor measurement instruments; "no SCPI experience required"; commands only from Instrument Definition Files ("It never invents a command"); "Every command sequence requires explicit engineer approval before execution"; built-in procedures incl. S-parameter sweeps and SOLT calibration; mock mode; pricing not stated. https://helpfiles.keysight.com/kmsic/English/keysight_mcp_for_instrument_control/Content/overview.html
- Keysight ADS 2027 (6 Oct 2026) adds MCP servers for RF design. https://www.hpcwire.com/aiwire/2026/10/06/keysight-advances-its-design-software-with-agentic-ai/

### Thermo Fisher AutoScript (EM API) - paid, "Request A Quote"; Python 3.5-based; offline simulation mode. https://www.thermofisher.com/order/catalog/product/AUTOSCRIPT-TEM ; https://assets.thermofisher.com/TFS-Assets/MSD/Datasheets/autoscript-4-datasheet.pdf

### Open-source MCP / agent frameworks for instruments
- InstrMCP (QCoDeS/JupyterLab, MIT) https://pypi.org/project/instrmcp/ ; PyLabRobot plr-mcp (Hamilton STAR, Opentrons OT-2, Tecan EVO) https://glama.ai/mcp/servers/di-omics/plr-mcp ; labmcp https://pypi.org/project/labmcp/ ; NIMO MCP SDL orchestrator (arXiv May 2026) https://arxiv.org/html/2605.15227 ; LAP agent-instrument protocol (arXiv Jun 2026) https://arxiv.org/html/2606.03755 ; Lightfall API-first LLM-addressable beamline control (arXiv 2606.06711) https://arxiv.org/pdf/2606.06711 ; ALS beamline 5.3.1 Osprey+Bluesky (J. Synchrotron Rad. 2026) https://journals.iucr.org/s/issues/2026/05/00/soo5005/index.html
- OPC UA LADS released Dec 2023/Jan 2024; SLAS lists vendor support as low. https://www.slas.org/resources/standards/opc-ua-lads

### Waters (AI Link + MHS, Oct 2026)
- Waters AI Link brings MCP to waters_connect Software; lets customers link waters_connect to Claude "and other LLMs and agents"; audit trails carried into Empower; early access now, GA "in November" 2026 for waters_connect customers; claims connection time cut "from weeks to hours" [company claim]. Waters joined Anthropic MHS research program "effective immediately". Dave Leitham (VP Informatics): "AI can generate hypotheses faster than any lab can test them, so the bottleneck has moved from computation to the bench." Release says AI-directed workflows "already generating new demand for Waters instruments and consumables" (unquantified). Release dated ~13-15 Oct 2026 (PR Newswire 302906439). https://biopharmaapac.com/news/97/8561/waters-partners-with-anthropic-to-advance-ai-driven-autonomous-laboratory-workflows.html ; https://www.webull.com/news/15740820817863680
- waters_connect API: "secure, restful API" for sample lists, acquisition, data retrieval; developer hub; access via local Waters service team (one page says intended for Waters Professional Services). https://www.waters.com/nextgen/no/en/products/informatics-and-software/waters_connect/waters-connect-api.html

### Anthropic Claude Science (30 Jun 2026)
- Beta app (not new model) for Pro/Max/Team/Enterprise; 60+ scientific skills; reviewer agent; up to 50 projects x $30k credits; launch partners incl. Novartis, Allen Institute [secondary reports]. https://thenextweb.com/news/anthropic-claude-science-ai-workbench-scientists ; https://the-decoder.com/anthropic-launches-claude-science-an-ai-workspace-built-specifically-for-researchers/

### Rohde & Schwarz MXO AI Connect (30 Oct 2026)
- "locally installed Model Context Protocol (MCP) server that runs on a user's PC or on a shared lab host"; MXO 3/4/5/5C + ScopeStudio; clients Cursor, Claude Desktop, Claude Code, GitHub Copilot; user picks LLM; part of "R&S AI Workplace platform"; pricing not stated. Quote Philip Diegmann (VP): "AI offers engineers a new way to work with increasingly capable test instruments." https://www.bisinfotech.com/rohde-schwarz-introduces-mxo-ai-connect-for-ai-assisted-oscilloscope-workflows/ ; R&S AI Workplace / TechAssist (CMX500, extending to other classes) https://www.rohde-schwarz.com/au/_258801.html
- NI (Emerson) Nigel AI in LabVIEW 2026 Q3 creates VIs from prompts; no NI MCP server found. https://www.electronicdesign.com/technologies/embedded/machine-learning/video/55396195/electronic-design-whats-new-with-nigel-and-labview-2026

### Agilent 2026 AI launches (classical/assistive, not agent control)
- GC Assist on 8890B/8860B GC (26 May 2026): monitoring, built-in troubleshooting, remote connectivity https://www.investor.agilent.com/news-and-events/news/news-details/2026/Agilent-Launches-New-GC-Systems-with-GC-Assist-to-Improve-Laboratory-Efficiency-and-Data-Quality/default.aspx ; OpenLab Sync AI features (28 May 2026) https://www.businesswire.com/news/home/20260528098940/en/ ; CrossLab Connect AI lab optimisation via Sigsense (SLAS Feb 2026) https://www.businesswire.com/news/home/20260204034151/en/ ; xCELLigence eSight AI module (1 Jul 2026); Gen5 AI Cell ID (29 Sep 2026).

### Bruker
- Chemspeed + SciY open Self-Driving Lab platform (SLAS, 9 Feb 2026), SciY "AI-ready open data backbone", "vendor-agnostic". https://ir.bruker.com/press-releases/press-release-details/2026/Chemspeed-and-SciY-Announce-SelfDriving-Laboratory-Platform-Integrating-Automation-Analytics-and-AI-Orchestration/default.aspx
- Bruker strategic collaboration + minority investment in Atinary (11 Aug 2026): Chemspeed + Fourier 80 FT-NMR + Atinary SDLabs agentic closed loop. https://ir.bruker.com/press-releases/press-release-details/2026/Bruker-Announces-Strategic-Collaboration-with-Atinary-Technologies-to-Advance-Self-Driving-Laboratories/default.aspx

### Thermo Fisher Investor Day (20 May 2026) - deck (primary)
- LTM Q1 2026 revenue $45B; Services & Consumables 84%, Instruments 16%; "exiting 2026" >85% services & consumables. Slide 39 "AI in drug discovery": Design/Setup/Test/Analyze incl. "AI-driven orchestration of lab workflows", "Automated instruments and lab workflows" around "Thermo Fisher Connect Enterprise software platform", three "In collaboration with" partner logos (trademark notes list NVIDIA, OpenAI, TetraScience). Vulcan Automated Lab: "AI-enhanced transmission electron microscopes with integrated robotic handling". PPI: AI "Augmenting technical support, field service engineers and application specialists". Krios 5 / Orbitrap Astral Zoom "Enhanced with AI and automation capabilities". Deck: https://s25.q4cdn.com/974941731/files/doc_downloads/Downloads/2026-Investor-Day-Presentation-Distribution.pdf
- TIKR summary: Gianluca Pettiti said first "fully autonomous instruments" reach customers in H2 2026; CFO sized AI productivity at ~$80-100M incremental annual savings [secondary report; not in deck text] https://www.tikr.com/blog/what-thermo-fisher-ceo-said-at-investor-day-that-the-market-is-still-processing
- TetraScience-Thermo Fisher collaboration 12-13 Jan 2026 (Tetra AI + Thermo Fisher AI; financials undisclosed) https://www.tetrascience.com/news/tetrascience-announces-collaboration-with-thermo-fisher-scientific-to-accelerate-scientific-data-and-ai-enablement-across-the-laboratory ; https://www.fiercebiotech.com/medtech/thermo-fisher-scientific-teams-nvidia-tetrascience-next-gen-ai-workflow-projects

### Software-layer funding
- Automata: $45M Series C 29 Jan 2026 led by Dimension; Danaher Ventures, Tru Arrow, Octopus, EF; Danaher joins board; Beckman Coulter partnership integrating instruments with LINQ. Total raised $152M (Dealroom) vs $180M (other) - conflicting. https://www.businesswire.com/news/home/20260129548625/en/Automata-Raises-$45M-Series-C-to-Build-the-Operating-System-for-AI-Ready-Labs
- Opentrons: $40M Series E 29 Oct 2026 led by Avego + BroadOak; existing SoftBank VF, Khosla [secondary: SiliconANGLE]; >10,000 robots deployed [company claim]; HighRes partnership Feb 2026; BD collaboration Oct 2025. https://siliconangle.com/?p=852385
- Benchling: Benchling AI (Oct 2025), Benchling Agents (27 Aug 2026); last primary valuation $6.1B (2021 Series F); secondary estimate $0.9B (May 2026, TrueUp) - conflicting; S-1 filing claim (12 May 2026) unverified. https://sacra.com/c/benchling/ ; https://api.trueup.io/co/benchling
- Emerald Cloud Lab: no 2025-2026 funding found; ~$49.4M total raised (aggregator); 30 job cuts & SF office closure (Mercury News, date unclear) https://beckershospitalreview.com/digital-health/digital-biotech-company-cuts-jobs-shuts-down-san-francisco-offices.html
- BICO: kept Biosero (bought 2021 at EV $169.7M); sold MatTek/Visikol to Sartorius $80M (Apr 2025) to reduce debt before Mar 2026 convertible. https://mfn.se/a/bico-group/bico-has-entered-into-an-agreement-to-divest-mattek-to-sartorius-for-usd-80m

### China
- XtalPi (02228.HK) FY2025: revenue RMB 803M (+201%); drug discovery solutions RMB 537.9M (+419%); AI4S smart solutions RMB 264.7M (+62.6%); first full-year profit RMB 134.6M (adj. RMB 258.2M); cash RMB 7,068.6M at 31 Dec 2025; profit reliant on non-recurring items (DoveTree upfront, FV gains) per 锦缎研究院; GM fell to 43.5% from ~46%. [secondary reports of filings] https://m.huanqiu.com/article/4QuAKm3FeNr ; IR deck https://ir.xtalpi.com/media/u0gcv5md/2025-annual-investor-pre-cn-final-1.pdf
- State Council 《关于深入实施"人工智能+"行动的意见》(Aug 2025): "人工智能+"科学技术 action, AI-based new research paradigm. https://www.news.cn/tech/20250828/5af2930138044797909cf407e7ba119b/c.html
- Beijing plan (Jul 2026): 18 tasks incl. building autonomous laboratories, "推动重大科技基础设施和科研仪器智能化升级", science agents; six fields incl. high-energy physics, materials, quantum. https://www.ncsti.gov.cn/zcfg/zcjd/202607/t20260702_250678.html ; Aug 2026 cases: Tsinghua chemistry automated platform 10-30x efficiency; report notes full closed-loop autonomous labs still have "技术瓶颈" in autonomous decisions. https://news.bjd.com.cn/2026/08/21/11926168.shtml
- DP Technology (深势科技): no HK IPO/valuation found in Chinese search - pending.

### Japan
- MEXT FY2027 budget request: AI4S JPY 378.9bn (request, not final) [secondary: newswitch] https://newswitch.jp/p/50165 ; "大規模スマートクラウドラボ" FY2026-2029, total ~JPY 9.5bn, FY2026 budget JPY 4.36bn. https://www.mext.go.jp/content/20260221-mxt_nanozai-000046621_8.pdf ; MEXT "AI for Science による科学研究革新プログラム" FY2025-2028.

### South Korea
- MSIT launched "자율실험실 산·학·연 협의체" 11 Aug 2026 with ~80 institutions [secondary]; K-Moonshot strategy (Mar 2026) PDF https://smartcity.go.kr/wp-content/uploads/2026/03/안건4AI시대과학기술경쟁력대도약을위한K-문샷추진전략안.pdf ; AI materials autonomous lab centres 24h (Apr 2026) https://v.daum.net/v/20260430101533808 ; bio autonomous lab (Jun 2026) https://www.heraldk.com/article/2026061118413174490 ; KRW 13.5bn new for AI autonomous lab programme (blog only - could not verify).

### Batch C findings (fetched full text)
- Thermo Fisher corporate "AI ecosystem" page: NVIDIA "accelerated computing and AI infrastructure will be integrated into Thermo Fisher's scientific instrumentation and laboratory software"; Powell: "Working with Thermo Fisher, we are building the fundamental infrastructure of autonomous labs"; TetraScience "organizes and prepares scientific data across disparate equipment and vendors"; OpenAI initially in clinical research; BenchSci (30 Sep). No statements on open interfaces, data ownership or pricing. https://corporate.thermofisher.com/us/en/index/newsroom/Our-stories/AI-ecosystem.html
- TIKR (secondary, quoting management at 20 May 2026 Investor Day): Pettiti: "the first version of fully autonomous instruments being deployed to our customers in the second half of the year"; CFO Jim Meyer ~$80-100M incremental annual AI-enabled productivity (paraphrase). https://www.tikr.com/blog/what-thermo-fisher-ceo-said-at-investor-day-that-the-market-is-still-processing
- Thermo Fisher Q1 2026 call (23 Apr 2026, via Lab Manager): Casper: "You're seeing very wide-scale, large volume labs that are just trying to build biology models"; customers want instruments "automated-ready"; A&G revenue down low single digits, instrument demand "particularly soft". https://www.labmanager.com/thermo-fisher-kicks-off-2026-with-new-instruments-ai-push-and-a-warning-on-rising-lab-costs-35274
- NVIDIA GTC Berlin (21 Oct 2026): Automata "connecting scientific agents with automated laboratory infrastructure so they can initiate experiments"; Benchling grounding agents; Danaher autonomous lab hosting protein design foundry where Genedata AI co-scientist "will coordinate protein design and testing"; Boltz, Biolevate, Hologen, Therna. https://nvidianews.nvidia.com/news/healthcare-and-life-sciences-leaders-build-on-nvidia-to-advance-drug-discovery-and-expand-patient-care
- NVIDIA BioNeMo Agent Toolkit (23 Jun 2026); Claude Science reaches Evo 2, Boltz-2, OpenFold3 via BioNeMo skills. https://campustechnology.com/articles/2026/07/01/anthropic-nvidia-move-ai-agents-deeper-into-scientific-workflows.aspx
- NVIDIA Q2 FY2027 (qtr ended 26 Jul 2026): revenue $96,221M (+106% y/y); Data Center $89.0B (+117%); Edge Computing $7.2B (+27%); Q3 outlook $108.0B +/-2%, no China DC compute assumed. No separate disclosure for healthcare/science/instruments. https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
- NVQLink (28 Oct 2025, GTC DC): "open system architecture for tightly coupling ... GPU computing with quantum processors"; 17 QPU builders; control-system builders Keysight, Quantum Machines, Qblox, QubiC, Zurich Instruments; qubits need "complex calibration, quantum error correction and other control algorithms". No AI calibration model named. https://nvidianews.nvidia.com/news/nvidia-nvqlink-quantum-gpu-computing ; "NVIDIA Ising" -> could not verify (search budget exhausted).
- EU Machinery Regulation 2023/1230 applies 20 Jan 2027: covers AI-based safety functions/self-evolving behaviour; MHS safety-limit file may count as safety function requiring notified body (TNW analysis). Jonah Cool: "In many cases, the science doesn't happen because you can't use the equipment." Kemeny: "What MCP did for software, MHS will do for the hardware world." https://thenextweb.com/news/anthropic-model-hardware-standard-mhs-eu-machinery-regulation-2027
- LAP paper (Shiyanjia Lab, China; arXiv 2606.03755, 2 Jun 2026): "every such system rebuilds the link between the reasoning agent and the physical instrument from scratch"; "instruments expose diverse vendor APIs with inconsistent command interfaces, telemetry formats, and safety semantics"; ops "can injure people or destroy equipment"; ECL "remaining a closed, proprietary ecosystem"; Allotrope full tooling requires consortium membership; Bluesky/Ophyd on 26 of 28 NSLS-II beamlines; A-Lab 28 device instances/16 types each hand-coded adapter. https://arxiv.org/html/2606.03755
- elmerdata (Elmer Yglesias, 30 Aug 2026): governance/delegation is the binding issue; CMU plate reader driven through GUI; Genentech agent retried BCA in same well after bubble error, worsening it; CMU agent reduced top concentration 200->100 ug/mL without human input; QuEra 695/700. https://elmerdata.bearblog.dev/who-gave-the-ai-control-of-the-laboratory/
- IntuitionLabs (19 Sep 2026): MHS "not ... an independently certified GxP standard"; "A conversational transcript alone does not satisfy this record model" (Part 11); "Authorization is OPTIONAL for MCP implementations"; agent "should initially recommend or parameterize actions, not become the safety controller"; Universal Robots: "nothing is generally available yet". https://intuitionlabs.ai/articles/anthropic-hardware-standard-pharma-labs
- Genesis demo (22 Jul 2026, FedScoop): pre-recorded demo; Model Access Gateway; "DOE-developed model context protocol tools"; users connect own tools via open protocols; ~$250M of $293M allocated; phase-two awards expected Sept; teaser: NVIDIA, AMD, OpenAI, Anthropic, Google investing "$2.4B in AI tools and compute credits" (teaser, not article body). https://fedscoop.com/energy-department-demo-genesis-mission-platform-rfa-awards/
- Bruker-Atinary (11 Aug 2026): minority investment, "Financial details were not disclosed"; Atinary Boston lab (opened early 2026) with Chemspeed + Bruker benchtop NMR; Atinary ecosystem partners ABB Robotics, Agilent, AWS, Bruker, Chemspeed, Mettler-Toledo. Gleixner: "Our strategic investment in Atinary advances Bruker's goal to combine differentiated analytical technologies". https://ir.bruker.com/press-releases/press-release-details/2026/Bruker-Announces-Strategic-Collaboration-with-Atinary-Technologies-to-Advance-Self-Driving-Laboratories/default.aspx
- Lila (Startup Fortune 3 Jun 2026): investors Flagship, Braidwell, Collective Global, General Catalyst, ARK Venture, March Capital, NVentures; "AI Science Factories"; no revenue disclosed; commercialisation depends on partners. https://startupfortune.com/lila-sciences-is-testing-how-much-investors-will-pay-for-automated-labs/
- Periodic Labs (Dealroom 26 Mar 2026): founded May 2025 (Liam Fedus ex-OpenAI VP research; Ekin Dogus Cubuk ex-Google DeepMind); $300M seed Sept 2025 from a16z, Felicis, Accel at $1.3B; Bloomberg: talks ~$7B; "paying customers in the semiconductor industry". https://dealroom.co/news/127042-periodic-labs-eyes-7b-valuation-fivefold-jump-in-six-months/
- Opentrons (SiliconANGLE 29 Oct 2026): $40M Series E led by Avego + BroadOak; >11,000 robots in 80+ countries; 90% of top-20 pharma; CEO James Atwood: "our systems are built for AI to run experiments directly." Valuation/revenue undisclosed. https://siliconangle.com/?p=852385
- Keysight MCP getting-started: Windows 10/11 or Linux (Ubuntu 24.04); VISA providers ks/ni/rs/socket/mock; licence/pricing not stated; download from Keysight. https://helpfiles.keysight.com/kmsic/English/keysight_mcp_for_instrument_control/Content/getting-started.html
- Korea MSIT "AI-네이티브 첨단바이오 자율실험실" (11-12 Jun 2026): KRW 49.5bn through 2028; 1 general + 5 specialised labs; Catholic Univ. of Korea leads K-Cell platform; K-Moonshot drug-development mission. https://www.heraldk.com/article/2026061118413174490 ; MSIT AI materials R&D platform strategy 2026-30 (30 Apr 2026): 4 autonomous lab centres (batteries, hydrogen/energy, aerospace/mobility metals, organic semiconductors/display); budget not stated. https://v.daum.net/v/20260430101533808
- UniteLabs blog (Jamie Beach, 21 Jul 2026; interested party - SiLA 2 software vendor): Letter of Intent signed by Roche, Bayer, Takeda, BioNTech, Lonza, Novo Nordisk, Botnar Institute calling for open connectivity in all new hardware procurement; open APIs required by 2027; "if a vendor sells robots, their 'open' platform is really a sales funnel." [secondary/interested-party report; primary LOI text not verified] https://unitelabs.io/resources/blog/end-times-fragmentation-tax-sila/
