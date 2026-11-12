# Self-tuning instruments: the software layer, AI-model suppliers, control interfaces and value capture (as of 12 November 2026)

Scope: the cross-cutting layer between AI agents and measuring instruments (lab-automation and orchestration software, autonomous-lab companies, model and agent-platform suppliers), interface standards and openness, evidence on who captures value, government programmes, and tests of the two priors. Instrument classes themselves are covered by other researchers.

How to read the labels:
- [independently confirmed: by whom]: a party other than the company confirms it.
- [company claim]: from the company or its partner, not independently confirmed.
- [secondary report]: press or analyst report, not checked against a primary document.
- [search snippet]: text seen only in a search-result extract; the page itself was not opened.
- "could not verify": the item was checked for and not found; the reason is stated.

Method note: about 33 web searches and about 45 page reads, run on 12 November 2026. Midway through, the session's shared web-search budget ran out (a limit of 200 searches shared by all agents in the session). After that I did no more searching, and I did not switch to other search services to get around the limit. The rest of the work read the full text of pages already found, plus a few primary pages at their standard address (NVIDIA newsroom, Anthropic). So coverage is thin in some places, listed in section 9: Japan's companies, Taiwan, India, Israel, the UK and EU programmes, vendors' cloud data terms, service-revenue shares beyond Thermo Fisher, and funding for several private companies.

Follow-up pass (12 Nov 2026, same day): at the coordinator's request, about 30 further reads of official pages at known addresses, by direct fetch only. These were investor-relations results releases and decks, vendor policy and terms pages, the SiLA letter-of-intent PDF, and company websites. No web searches were run, and no Firecrawl or other search service was used (0 Firecrawl calls). Additions from this pass are marked "[added in follow-up]".

---

## 1. Map of the software layer and model suppliers

### Takeaway
By November 2026 the layer between agents and instruments has split into five groups:
1. Model and agent-platform suppliers are setting the agent-to-hardware protocol. Anthropic's Model Context Protocol (MCP) is one example. Anthropic's Model Hardware Standard (MHS) is another; it entered research preview on 27 August 2026 with Danaher, Tecan, QIAGEN, Automata and Waters taking part.
2. Instrument makers are wrapping their own command sets in MCP servers: Keysight, Rohde & Schwarz and Waters. Or they ally with a model supplier, as Thermo Fisher has with NVIDIA, OpenAI and TetraScience.
3. Independent orchestration and data layers: TetraScience, Benchling, Automata, Atinary, Opentrons, Biosero, UniteLabs.
4. Capital-heavy autonomous-lab operators: Lila Sciences, Periodic Labs and XtalPi.
5. National laboratories build their own open stacks on Bluesky, EPICS, Osprey and Lightfall for the hardest physics instruments.

No independent software company was found controlling high-value physics instruments (electron microscopes, beamlines, accelerators) commercially. There, users build the agents themselves, or the maker does.

### Cited Findings

**A. Model and agent-platform suppliers**

- **Anthropic, Model Hardware Standard (MHS), 27 Aug 2026**
  - Described as "a shared specification for AI agents to safely operate physical devices".
  - Status: research preview for "a first group of scientific research labs and advanced manufacturers", by application through a waitlist. It began as a collaboration with HHMI Janelia.
  - Design: a standardised driver with read/write primitives and a standard discovery format. The driver generates a reference file listing what the device can measure and adjust, and "what safety limits will be enforced". Control runs through MCP, a command-line interface, or code files.
  - Scope: "MHS works with any device that has a programmable interface". It is model-agnostic. Anthropic plans to open-source it after the preview.
  - Companies named: AWS (Strands Robots), Automata (LINQ), Danaher ("exploring"), Doosan Robotics, MBF Bioscience (ScanImage driver), QIAGEN (QIAsymphony Connect proof of concept), Tecan (Fluent), Universal Robots, Hugging Face (LeRobot), Raspberry Pi.
  - Pilots: Genentech, the University of Washington, Carnegie Mellon (about 3x faster serial dilution), Janelia (a rig with "seven different vendor programs without a shared interface"), QuEra (an agent-developed laser-relock controller recovered 99.3% of the time without a human), Tetsuwan Scientific.
  - [company claim; partner-reported results] — [Anthropic, 27 Aug 2026](https://www.anthropic.com/news/model-hardware-standard-research-preview)
- **MHS status and commercial terms.** No pricing or revenue model has been disclosed — [Fortune, 27 Aug 2026](https://fortune.com/2026/08/27/anthropic-makes-first-move-into-physical-ai-with-universal-standard-for-scientists-manufacturing/). The specification text, licence and conformance suite were not public as of 29 Aug 2026 — [noze, 29 Aug 2026](https://www.noze.it/en/insights/model-hardware-standard-agents-lab-instruments/). Universal Robots says "nothing is generally available yet" — [IntuitionLabs, 19 Sep 2026](https://intuitionlabs.ai/articles/anthropic-hardware-standard-pharma-labs).
- **Anthropic, Claude Science, 30 Jun 2026.** A beta app, not a new model, for Pro, Max, Team and Enterprise plans. It has more than 60 scientific skills and a reviewer agent, and reaches NVIDIA BioNeMo models (Evo 2, Boltz-2, OpenFold3). The coverage found does not mention instruments — [Campus Technology, 1 Jul 2026](https://campustechnology.com/articles/2026/07/01/anthropic-nvidia-move-ai-agents-deeper-into-scientific-workflows.aspx); [The Next Web, 30 Jun 2026](https://thenextweb.com/news/anthropic-claude-science-ai-workbench-scientists) [secondary report].
- **Anthropic in the Genesis Mission.** Claude is made available to DOE researchers, with "a dedicated team to build lab-specific tools, including AI agents, Model Context Protocol servers, and Claude Skills" — [TechInformed, 24 Dec 2025, citing the DOE list of 18 Dec 2025](https://techinformed.com/doe-and-24-organizations-sign-ai-collaboration-deal/) [secondary report].
- **NVIDIA, products that touch instruments:**
  - DAQIRI (Data Acquisition for Integrated Real-time Instruments): a networking library inside the Holoscan platform, used by CERN, the University of Chicago and UCL in the A-GHOST project on ATLAS data.
  - cuPhoton: upcoming code for telescope, laser and X-ray data. It was tested on Rubin Observatory images, with a claim of "accelerated the ingestion of FITS files by 14,900x".
  - ALCHEMI NIM microservices: Batched Geometry Relaxation and Batched Molecular Dynamics, both released March 2026. An ALCHEMI VASP microservice is in early access.
  - These were announced at ISC Hamburg, 22–26 Jun 2026. [company claim] — [syndicated NVIDIA release, 24 Jun 2026](https://usa-automation.net/news/112167-nvidia-introduces-ai-software-libraries-for-scientific-research)
  - BioNeMo Agent Toolkit, 23 Jun 2026 — [Campus Technology](https://campustechnology.com/articles/2026/07/01/anthropic-nvidia-move-ai-agents-deeper-into-scientific-workflows.aspx).
  - Holoscan Sensor Bridge is open-source software that streams sensor data directly into GPU memory — [Electronic Design GTC 2026 wrap-up](https://www.electronicdesign.com/technologies/embedded/machine-learning/article/55365277/electronic-design-latest-news-from-nvidias-gtc-2026) [search snippet].
- **NVIDIA NVQLink, 28 Oct 2025, GTC Washington.**
  - Described as an "open system architecture for tightly coupling the extreme performance of GPU computing with quantum processors", accessed through CUDA-Q.
  - Supported by 17 quantum-processor builders. The quantum control-system builders named are Keysight, Quantum Machines, Qblox, QubiC and Zurich Instruments. National laboratories guided its development.
  - The release says qubits need "complex calibration, quantum error correction and other control algorithms". No AI calibration model is named. [company claim] — [NVIDIA, 28 Oct 2025](https://nvidianews.nvidia.com/news/nvidia-nvqlink-quantum-gpu-computing)
- **NVIDIA partners, GTC Berlin, 21 Oct 2026.**
  - "Automata is connecting scientific agents with automated laboratory infrastructure so they can initiate experiments".
  - Benchling is "grounding agents in experimental data".
  - In Danaher's autonomous lab, Genedata's AI co-scientist "will coordinate protein design and testing in the protein design foundry". [company claim] — [NVIDIA, 21 Oct 2026](https://nvidianews.nvidia.com/news/healthcare-and-life-sciences-leaders-build-on-nvidia-to-advance-drug-discovery-and-expand-patient-care)
- **NVIDIA and Thermo Fisher, 12 Jan 2026.** Thermo Fisher will integrate NVIDIA AI infrastructure, "including NVIDIA DGX Spark", plus NeMo and BioNeMo, into its instruments and lab software. Kimberly Powell (NVIDIA): "Working with Thermo Fisher, we are building the fundamental infrastructure of autonomous labs". [company claim] — [Business Wire, 12 Jan 2026](https://www.businesswire.com/news/home/20260112999582/en/); [Thermo Fisher AI ecosystem page](https://corporate.thermofisher.com/us/en/index/newsroom/Our-stories/AI-ecosystem.html). A report of "150 DGX Spark units" at Thermo Fisher sites appears only at [rallies.ai](https://rallies.ai/news/thermo-fisher-wins-us-production-shift-contracts-partners-with-nvidia-on-ai-lab-infrastructure); could not verify.
- **NVIDIA at a national laboratory.** The Accelerator Assistant at the Advanced Light Source (ALS), Lawrence Berkeley National Laboratory, runs on an NVIDIA H100 in the control-room network. It uses LBNL's Osprey agent framework against EPICS, a database of more than 230,000 process variables. It routes requests to Gemini, Claude or ChatGPT through the lab's CBorg gateway, or to local models via Ollama. The team reports a 100x cut in set-up effort for a multistage experiment. [company claim by NVIDIA blog quoting LBNL] — [NVIDIA blog, 8 Jan 2026](https://blogs.nvidia.com/blog/ai-copilot-berkeley-x-ray-particle-accelerator)
- **OpenAI.**
  - Strategic collaboration with Thermo Fisher, 16 Oct 2025. The first deployment is in PPD clinical research. OpenAI APIs go into product development, service delivery and customer engagement, and ChatGPT Enterprise goes to Thermo Fisher staff. Instrument control is not mentioned — [Thermo Fisher IR, 16 Oct 2025](https://ir.thermofisher.com/investors/news-events/news/news-details/2025/Thermo-Fisher-Scientific-to-Accelerate-Life-Science-Breakthroughs-with-OpenAI/default.aspx).
  - Its Genesis MOU is "a framework for information sharing and future agreements" under OpenAI for Science, with no specific models, compute or credits committed — [TechInformed](https://techinformed.com/doe-and-24-organizations-sign-ai-collaboration-deal/) [secondary report].
- **Google DeepMind.** In the Genesis Mission it offers an "accelerated access program" for scientists at all 17 DOE national laboratories, "starting with 'AI co-scientist' on Google Cloud" — [TechInformed](https://techinformed.com/doe-and-24-organizations-sign-ai-collaboration-deal/) [secondary report]. Its automated laboratory in the UK: could not verify (search budget exhausted).
- **Microsoft.** A Genesis signatory with no commitment described — [TechInformed](https://techinformed.com/doe-and-24-organizations-sign-ai-collaboration-deal/). Listed as a TetraScience partner — [TetraScience, 12 Jan 2026](https://www.tetrascience.com/news/tetrascience-announces-collaboration-with-thermo-fisher-scientific-to-accelerate-scientific-data-and-ai-enablement-across-the-laboratory). Microsoft Discovery: could not verify.
- **Hugging Face.** Fortune notes, in passing, that "Nvidia is set to buy Hugging Face for $13 billion" — [Fortune, 27 Aug 2026](https://fortune.com/2026/08/27/anthropic-makes-first-move-into-physical-ai-with-universal-standard-for-scientists-manufacturing/) [secondary report; could not verify independently].

**B. Instrument makers' own agent layers.** Full detail is in the table in section 2.

- **Thermo Fisher.** Its 20 May 2026 Investor Day deck shows "AI-driven orchestration of lab workflows" and "Automated instruments and lab workflows" built around the "Thermo Fisher Connect Enterprise software platform". Three partner logos sit beside them; the deck's trademark notes list NVIDIA, OpenAI and TetraScience — [Thermo Fisher Investor Day deck, 20 May 2026](https://s25.q4cdn.com/974941731/files/doc_downloads/Downloads/2026-Investor-Day-Presentation-Distribution.pdf).
  - Q3 2026 results (21 Oct 2026) [added in follow-up]:
    - The company opened its first AI-Automation Innovation Center, in South Korea, combining analytical technologies, automation and AI.
    - The release describes no autonomous-instrument launch and does not mention NVIDIA.
    - Analytical Instruments revenue was $2,002M of $12.14B group revenue (16.5%).
    - Source: [Thermo Fisher IR, 21 Oct 2026](https://ir.thermofisher.com/investors/news-events/news/news-details/2026/Thermo-Fisher-Scientific-Reports-Third-Quarter-2026-Results/default.aspx) [primary]
- **Waters.** AI Link brings MCP to waters_connect, and Waters joined MHS. Waters' own release is dated 13 Oct 2026. It says "Agents can create methods, run acquisitions, and process results without custom integration", and "Waters' participation in the MHS research program is effective immediately" — [PR Newswire, Waters release, 13 Oct 2026](https://www.prnewswire.com/news-releases/waters-launches-ai-link-advancing-ai-enabled-lc-ms-workflows-from-research-to-release-302906439.html) [company claim; primary release] [added in follow-up]; also [BioPharma APAC](https://biopharmaapac.com/news/97/8561/waters-partners-with-anthropic-to-advance-ai-driven-autonomous-laboratory-workflows.html).
- **Keysight.** An MCP Server for Instrument Control — [Keysight help files](https://helpfiles.keysight.com/kmsic/English/keysight_mcp_for_instrument_control/Content/overview.html).
- **Rohde & Schwarz.** MXO AI Connect, 30 Oct 2026 — [Bisinfotech](https://www.bisinfotech.com/rohde-schwarz-introduces-mxo-ai-connect-for-ai-assisted-oscilloscope-workflows/).
- **NI (Emerson).** The Nigel assistant in LabVIEW 2026 Q3 generates measurement code; no NI MCP server was found — [Electronic Design](https://www.electronicdesign.com/technologies/embedded/machine-learning/video/55396195/electronic-design-whats-new-with-nigel-and-labview-2026) [search snippet].
- **Bruker.**
  - Chemspeed and SciY's "open" self-driving lab platform, 9 Feb 2026 — [Bruker IR](https://ir.bruker.com/press-releases/press-release-details/2026/Chemspeed-and-SciY-Announce-SelfDriving-Laboratory-Platform-Integrating-Automation-Analytics-and-AI-Orchestration/default.aspx).
  - A minority investment in Atinary, 11 Aug 2026 — [Bruker IR](https://ir.bruker.com/press-releases/press-release-details/2026/Bruker-Announces-Strategic-Collaboration-with-Atinary-Technologies-to-Advance-Self-Driving-Laboratories/default.aspx).
- **Danaher.**
  - Danaher Ventures took part in Automata's Series C and joined Automata's board.
  - Beckman Coulter is integrating its instruments with Automata's LINQ platform — [R&D World](https://www.rdworldonline.com/automata-raises-45m-to-scale-lab-automation-platform-adds-danaher-as-strategic-investor/); [SelectScience](https://www.selectscience.net/article/beckman-coulter-life-sciences-partners-with-automata-to-accelerate-ai-ready-laboratory-automation) [search snippets].
  - It runs an autonomous lab with a Genedata co-scientist — [NVIDIA, 21 Oct 2026](https://nvidianews.nvidia.com/news/healthcare-and-life-sciences-leaders-build-on-nvidia-to-advance-drug-discovery-and-expand-patient-care).
  - Collaboration with NVIDIA, 14 Oct 2026, "to Advance Autonomous Science" [added in follow-up]:
    - Covers "a select group of priority instruments", not named.
    - NVIDIA technologies: DGX Spark edge computing, RAPIDS, BioNeMo open models, and exploratory work on Cosmos world models and Omniverse digital twins.
    - Stated aim includes "preserving customer choice in models, standards and technology providers".
    - No agents, self-calibration or commercial terms are mentioned.
    - CEO Julie Sawyer Montgomery: "AI is reshaping how science is conducted, and Danaher is at the forefront of that transformation."
    - [company claim; primary] — [Danaher IR, 14 Oct 2026](https://investors.danaher.com/2026-10-14-Danaher-Collaborates-with-NVIDIA-to-Advance-Autonomous-Science)
- **Agilent.** Assistive AI only: GC Assist, OpenLab Sync, CrossLab Connect. No agent-control interface was found (section 2).

**C. Independent orchestration and data layers**

- **TetraScience** (private, Boston).
  - Collaboration with Thermo Fisher, 12 Jan 2026: Tetra AI provides "agentic capabilities that guide scientists through complex workflows"; TetraScience will integrate "Thermo Fisher's instrumentation and informatics solutions".
  - Its "vendor-agnostic Scientific Data Foundry"; partners NVIDIA, Databricks, Snowflake and Microsoft. Customers are not named; financial terms not disclosed. [company claim] — [TetraScience, 12 Jan 2026](https://www.tetrascience.com/news/tetrascience-announces-collaboration-with-thermo-fisher-scientific-to-accelerate-scientific-data-and-ai-enablement-across-the-laboratory); [Fierce Biotech](https://www.fiercebiotech.com/medtech/thermo-fisher-scientific-teams-nvidia-tetrascience-next-gen-ai-workflow-projects).
  - It publishes a "Tetra Empower Agent" connector for Waters Empower — [TetraScience developer docs](https://developers.tetrascience.com/docs/waters-empower) [search snippet].
  - Funding and valuation: could not verify.
- **Automata** (private, London).
  - $45M Series C on 29 Jan 2026, led by Dimension, with Danaher Ventures, Tru Arrow, Octopus Ventures and Entrepreneurs First — [Business Wire, 29 Jan 2026](https://www.businesswire.com/news/home/20260129548625/en/Automata-Raises-$45M-Series-C-to-Build-the-Operating-System-for-AI-Ready-Labs) [search snippet].
  - Total raised: $152M (Dealroom) versus $180M (another profile), conflicting — [Dealroom](https://dealroom.co/companies/automata/).
  - It is an MHS launch partner (LINQ) and an NVIDIA GTC Berlin partner (above).
- **Benchling** (private).
  - Launched Benchling AI in October 2025 and Benchling Agents on 27 Aug 2026; the agents register molecules, process results and update workflows [secondary report].
  - Last primary valuation: $6.1B (2021 Series F). A secondary-market estimate put it at $0.9B (May 2026). These conflict — [Sacra](https://sacra.com/c/benchling/); [TrueUp](https://api.trueup.io/co/benchling).
  - An S-1 filing reported for 12 May 2026: could not verify.
- **Opentrons** (private).
  - $40M Series E on 29 Oct 2026, led by Avego with BroadOak Capital Partners. Valuation and revenue undisclosed.
  - More than 11,000 robots in 80+ countries, including 90% of the top-20 pharma companies [company claim]. CEO James Atwood: "our systems are built for AI to run experiments directly." — [SiliconANGLE, 29 Oct 2026](https://siliconangle.com/?p=852385)
  - Partnership with HighRes, February 2026; collaboration with BD, October 2025 — [Remio summary](https://www.remio.ai/post/opentrons-series-e-funds-the-move-from-lab-robots-to-connected-experiments) [search snippet].
- **Biosero (part of BICO, listed in Stockholm).** BICO bought Biosero in 2021 at an enterprise value of USD 169.7M — [Biosero](https://biosero.com/news-and-media/bico-completes-the-acquisition-of-biosero/). BICO kept Biosero but sold MatTek and Visikol to Sartorius for USD 80M (April 2025), to cut debt before a convertible bond due in March 2026 — [MFN, BICO release](https://mfn.se/a/bico-group/bico-has-entered-into-an-agreement-to-divest-mattek-to-sartorius-for-usd-80m) [search snippet].
- **Atinary** (private, Switzerland and Boston).
  - Its SDLabs platform: "code-free" AI agents running closed-loop Design-Make-Test-Analyze-Learn workflows.
  - Its Boston lab opened in early 2026 with Chemspeed robotics and Bruker benchtop NMR.
  - Ecosystem partners: ABB Robotics, Agilent, AWS, Bruker, Chemspeed, Mettler-Toledo.
  - Bruker's minority investment: "Financial details were not disclosed". — [Bruker IR, 11 Aug 2026](https://ir.bruker.com/press-releases/press-release-details/2026/Bruker-Announces-Strategic-Collaboration-with-Atinary-Technologies-to-Advance-Self-Driving-Laboratories/default.aspx)
- **UniteLabs** (SiLA 2 software; sells no hardware). It names Novo Nordisk, J&J, DKMS, Roche, Argonne and TU Munich as users of its Connector Development Kit [company claim] — [UniteLabs blog, 21 Jul 2026](https://unitelabs.io/resources/blog/end-times-fragmentation-tax-sila/).
- **Laboperator.** Claims devices "automatically identify themselves via OPC UA LADS or SiLA" [company claim] — [Laboperator blog](https://laboperator.com/blog/how-opc-ua-lads-sila-and-laboperator-are-powering-the-ai-enabled-lab-of-the-future) [search snippet].
- **Emerald Cloud Lab.** The LAP paper describes it as "remaining a closed, proprietary ecosystem" — [arXiv 2606.03755](https://arxiv.org/html/2606.03755). It cut 30 jobs and closed its San Francisco offices; the date is unclear in the snippet — [Becker's](https://beckershospitalreview.com/digital-health/digital-biotech-company-cuts-jobs-shuts-down-san-francisco-offices.html) [search snippet]. No funding found for 2025–2026.
- **Small MCP vendors.** Scispot offers an MCP server (beta) — [Scispot](https://community.scispot.com/en/articles/13977073-scispot-mcp-server-beta) [search snippet].

**D. Autonomous-lab operators (capital-heavy)**

- **Lila Sciences** (private, Cambridge, Massachusetts; spun out of Flagship).
  - $115M Series A extension (October 2025) led by NVentures. Series A total $350M; total raised $550M; valuation "more than $1.3 billion" [secondary report: Reuters] — [Yahoo/Reuters](https://finance.yahoo.com/news/exclusive-ai-lab-lila-sciences-101645837.html).
  - June 2026: reported talks to raise about $2B at about $8.5B before the new money — [Bloomberg Law](https://news.bloomberglaw.com/private-equity/lila-sciences-said-in-talks-for-funds-at-8-5-billion-valuation) [secondary report]. Not publicly confirmed closed — [Startup Fortune, 3 Jun 2026](https://startupfortune.com/lila-sciences-is-testing-how-much-investors-will-pay-for-automated-labs/).
  - Investors: Flagship, Braidwell, Collective Global, General Catalyst, ARK Venture, March Capital, NVentures. No revenue disclosed.
  - Integrated the full NVIDIA stack; claims 50x faster materials screening [company claim] — [NVIDIA ISC release](https://usa-automation.net/news/112167-nvidia-introduces-ai-software-libraries-for-scientific-research).
- **Periodic Labs** (private, San Francisco; founded May 2025 by Liam Fedus, ex-OpenAI, and Ekin Dogus Cubuk, ex-Google DeepMind).
  - $300M seed in September 2025 from a16z, Felicis and Accel at a $1.3B valuation.
  - Bloomberg reported talks at about $7B; the company has "paying customers in the semiconductor industry" — [Dealroom, 26 Mar 2026](https://dealroom.co/news/127042-periodic-labs-eyes-7b-valuation-fivefold-jump-in-six-months/) [secondary report].
  - May 2026 reports: at least $500M at $7.5B — [Dev.to/Gentic summary](https://dev.to/gentic_news/periodic-labs-hits-75b-valuation-raises-500m-for-ai-science-4f5p) [search snippet; not confirmed closed].
- **XtalPi (晶泰控股, HKEX 2228).** From the company's own deck:
  - FY2025 revenue RMB 803M (2024: RMB 266M; up about 201%). R&D RMB 569M. Profit RMB 135M (2024: loss of RMB 1,515M); adjusted profit RMB 258M.
  - Cash RMB 7,068.6M at 31 Dec 2025, plus 2026 convertible bonds of net RMB 2,536.8M.
  - Robot-lab ("智能自主实验") systems delivered or being built in 2025 for BASF, Roche, Haleon, JW Pharma, Liangzhu Laboratory, "a global pharma headquartered in Indianapolis" and a central state-owned enterprise (a contract worth tens of millions of RMB).
  - Architecture: "大语言模型 + 垂直领域 AI 模型" (LLM plus domain AI models) driving a robot "调度中枢" (dispatch hub). — [XtalPi 2025 investor presentation](https://ir.xtalpi.com/media/u0gcv5md/2025-annual-investor-pre-cn-final-1.pdf) [company claim, from filing-based deck]
  - An analysis attributed to 锦缎研究院 says the profit relied on non-recurring gains (the DoveTree upfront payment and fair-value changes) and that gross margin fell to 43.5% from about 46% — [Huanqiu](https://m.huanqiu.com/article/4QuAKm3FeNr) / [Huxiu, 27 Mar 2026](https://m.huxiu.com/article/4845830.html) [secondary report; search snippet].

**E. User-built open stacks (national laboratories and academia)**

- **Bluesky/Ophyd** runs on 26 of 28 NSLS-II beamlines — [LAP paper, arXiv 2606.03755](https://arxiv.org/html/2606.03755).
- **ALS beamline 5.3.1.** An agent-agnostic orchestration layer in which "All plans are executed through the Bluesky Queue Server, ensuring deterministic operation within existing control and safety constraints" — [Journal of Synchrotron Radiation 2026](https://journals.iucr.org/s/issues/2026/05/00/soo5005/index.html) [search snippet].
- **Lightfall (LBNL).** An "API-first architecture" that "exposes every panel, device, and scan plan through a single uniform addressable interface". It has been in testing at the ALS COSMIC-Scattering beamline since early 2026. External agents such as Claude Code reach it through "lightfall-mcp-bridge", under Keycloak-gated permissions. Most ALS beamlines run on "LabVIEW-based tooling", the Beamline Control System: "facility-internal software with no standalone publication" — [Lightfall, arXiv 2606.06711, 4 Jun 2026](https://arxiv.org/pdf/2606.06711).
- **HANBIT.** A virtual-commissioning platform combining Monte Carlo ray tracing, a "standard EPICS/Bluesky control stack" and a multilingual natural-language interface — [Journal of Synchrotron Radiation 2026](https://journals.iucr.org/s/issues/2026/05/00/ok5168/) [search snippet].
- **Open-source MCP servers for instruments** [project documentation; search snippets]:
  - InstrMCP, MIT licence, built on QCoDeS and JupyterLab for physics instruments — [PyPI](https://pypi.org/project/instrmcp/).
  - plr-mcp (PyLabRobot): Hamilton STAR, Opentrons OT-2, Tecan Freedom EVO — [Glama](https://glama.ai/mcp/servers/di-omics/plr-mcp).
  - lab-mcp, which warns that support differs by model and that an assistant can switch instrument outputs on — [PyPI](https://pypi.org/project/labmcp/).
  - labwire-mcp — [PyPI](https://pypi.org/project/labwire-mcp/0.5.0/).
  - teasel-server — [PyPI](https://pypi.org/project/teasel-server/).
  - The NIMO MCP-based self-driving-lab orchestrator — [arXiv 2605.15227](https://arxiv.org/html/2605.15227).

**F. Japan and China, compact view [added in follow-up; from company websites and IR only]**

- **Preferred Networks (PFN, private, Japan).**
  - 16 Sep 2026: capital and business alliance with Mitsubishi Heavy Industries, aimed at AI for "the intelligence and autonomy of machinery and systems"; no amount given.
  - 18 Sep 2026: PFN and PFCI (the Matlantis operator) will run Matlantis on PFN's MN-Core 2 chips, claiming "up to 4x faster execution than GPUs for selected simulation tasks" [company claim].
  - 5 Nov 2026: open-weight PLaMo 3 Translate (0.8B to 31B parameters).
  - No funding, valuation or IPO item appeared on the news page read — [PFN news](https://www.preferred.jp/en/news/). The Matlantis news page did not render (dynamic content) — could not verify Matlantis user numbers or ownership.
- **Epistra (private, Tokyo).** Epistra Accelerate is an AI-driven automated experiment-optimisation system.
  - Customers and partners featured: Astellas (AI × robot cell-therapy manufacturing), EVIDENT (co-creation around the "FLUOVIEW Smart" microscope), Shimadzu (CellTune), VisionCare, Spiber. Spiber claims "2年かかっていた研究開発を数週間に" (R&D that took two years cut to weeks) [company claim].
  - Part of a JST "ARiSE" project on unmanned research facilities.
  - No funding data on the site — [Epistra](https://epistra.jp/).
- **Robotic Biology Institute (RBI, Tokyo).** LabDroid robots; a Robot Future Creation Center at the Institute of Science Tokyo (opening ceremony 15 Apr 2026). Maholo, Yaskawa and funding are not mentioned on the homepage — [RBI](https://rbi.co.jp/).
- **Shimadzu.**
  - Tescan, an electron-microscope and FIB-SEM maker, is now consolidated: "Intangible assets and short-term borrowings up on Tescan consolidation"; the forecast includes "6 months of Tescan".
  - Semiconductor-related FIB-SEM unit orders rose 30%+ year on year (Jan–Sep 2026).
  - Equity ratio fell to 66.8% on higher borrowings.
  - Source: [Shimadzu FY2026 H1 slides, 10 Nov 2026](https://www.shimadzu.com/sites/shimadzu.com/files/ir/r272/7zicbmkg9z2n0leo.pdf) [company IR]. Its recurring-revenue data is in section 3.
  - Shimadzu's own autonomous-laboratory work: nothing on the IR page — could not verify.
- **DP Technology (深势科技, private, founded 2018, Beijing).**
  - Its homepage lists: 深势·宇知 (described as a "科学发现智能引擎", a scientific-discovery engine), 玻尔·科学空间, Hermite, RiDYMO, Piloteye, 玻尔·跃迁实验室, SciMaster ("science intelligent agent") and 勒贝格智算 computing services.
  - No funding, valuation or IPO information appears on the site — [DP Technology](https://www.dp.tech/). Funding and IPO status: could not verify.

### Inferences
- Independent orchestration layers are being squeezed from two sides:
  - From above: model suppliers want to standardise the driver (MHS) and own the agent.
  - From below: instrument makers now ship their own MCP servers that encode their own command dictionaries. Keysight's server "never invents a command" and uses Keysight Instrument Definition Files.
- The independents that are holding up have tied themselves to a large maker: TetraScience to Thermo Fisher, Automata to Danaher, Atinary to Bruker.
- In physics instruments (beamlines, accelerators, quantum), the integrators are the users: DOE laboratories with Bluesky, EPICS, Osprey and Lightfall. Commercial software companies appear only as model suppliers (Claude, Gemini, ChatGPT through CBorg) and compute suppliers (NVIDIA H100).
- Lila, Periodic and XtalPi are labs, or sellers of robot labs, rather than layers that tune third-party instruments. Their valuations reflect a bet on owning experimental data, not on instrument control software.

### Gaps
- Funding and valuation could not be verified (search budget exhausted) for: Anthropic, OpenAI, TetraScience, Scitara, Ganymede, Sapio, Citrine, Chemify, Kebotix, Telescope Innovations, Strateos, HighRes Biosolutions, Hamilton, Unchained Labs, Dassault Systèmes BIOVIA's relevant revenue, Preferred Networks/Matlantis, Epistra, the Robotic Biology Institute and Yaskawa, Shimadzu's autonomous-lab work, and DP Technology (深势科技). A Chinese-language search on DP Technology returned nothing relevant.
- South Korean, Taiwanese, Indian and Israeli software-layer companies were not identified in this session.

---

## 2. Interface-openness table

### Takeaway
In 2026, openness came mostly from vendors wrapping their own instruments in MCP servers:
- Keysight: a downloadable server.
- Rohde & Schwarz: 30 Oct 2026.
- Waters: early access in October, general availability in November 2026, for waters_connect customers only.

Each keeps the vendor's own command definitions, and none states a price. Programming interfaces for the expensive physics instruments stay paid or gated: Thermo Fisher's AutoScript electron-microscope API is sold on quote, and Waters' REST API is reached through its service team. Open standards (SiLA 2, OPC UA LADS) exist but have low vendor uptake (SLAS rates LADS vendor support "low"). The specification of Anthropic's MHS was not yet public as of late August 2026.

### Cited Findings

| Maker | Interface | Open / closed / paid | Date of latest change | Source | Label |
|---|---|---|---|---|---|
| Keysight | MCP Server for Instrument Control. Plain-language requests become SCPI commands drawn from Instrument Definition Files. "Every command sequence requires explicit engineer approval before execution". Built-in procedures include S-parameter sweeps and SOLT calibration. VISA providers: Keysight (ks), NI, R&S, socket, mock. Windows and Linux | Open to any MCP client (Claude Code, Claude Desktop and GitHub Copilot named); vendor-defined command set; licence and price not stated; downloaded from Keysight | 2026 (copyright year; no release date stated) | [Overview](https://helpfiles.keysight.com/kmsic/English/keysight_mcp_for_instrument_control/Content/overview.html); [Getting started](https://helpfiles.keysight.com/kmsic/English/keysight_mcp_for_instrument_control/Content/getting-started.html) | company documentation |
| Keysight | ADS 2027 MCP servers (RF design software, not instruments) | Inside paid design software | 6 Oct 2026 | [HPCwire](https://www.hpcwire.com/aiwire/2026/10/06/keysight-advances-its-design-software-with-agentic-ai/) | company claim |
| Rohde & Schwarz | MXO AI Connect: a "locally installed Model Context Protocol (MCP) server" for MXO 3/4/5/5C oscilloscopes and ScopeStudio. Clients: Cursor, Claude Desktop, Claude Code, GitHub Copilot; the user picks the LLM. Part of the "R&S AI Workplace platform" | Open to the user's choice of model; price not stated | 30 Oct 2026 | [Bisinfotech](https://www.bisinfotech.com/rohde-schwarz-introduces-mxo-ai-connect-for-ai-assisted-oscilloscope-workflows/) | company claim |
| Rohde & Schwarz | AI Workplace / TechAssist (SCPI-centred; available on the CMX500, being extended to other instrument classes) | Vendor platform | 2026 | [R&S](https://www.rohde-schwarz.com/au/_258801.html) | search snippet |
| NI (Emerson) | Nigel AI in LabVIEW 2026 Q3 (writes code, not an agent interface) | Inside paid LabVIEW; no MCP server found | Q3 2026 | [Electronic Design](https://www.electronicdesign.com/technologies/embedded/machine-learning/video/55396195/electronic-design-whats-new-with-nigel-and-labview-2026) | search snippet |
| Waters | waters_connect REST API (sample lists, acquisition, data retrieval) | Gated: "contact your local Waters service team"; one page says it is intended for Waters Professional Services | Page undated | [Waters](https://www.waters.com/nextgen/no/en/products/informatics-and-software/waters_connect/waters-connect-api.html) | search snippet |
| Waters | AI Link: MCP for waters_connect, carrying audit trails into Empower. "Agents can create methods, run acquisitions, and process results without custom integration". Plus participation in MHS | Open protocol, limited to waters_connect customers; general availability "in November" 2026; no price; data handling not described | 13 Oct 2026 | [PR Newswire (Waters release)](https://www.prnewswire.com/news-releases/waters-launches-ai-link-advancing-ai-enabled-lc-ms-workflows-from-research-to-release-302906439.html); [BioPharma APAC](https://biopharmaapac.com/news/97/8561/waters-partners-with-anthropic-to-advance-ai-driven-autonomous-laboratory-workflows.html) | company claim (primary release, added in follow-up) |
| Thermo Fisher | AutoScript TEM / AutoScript 4 (Python API for electron microscopes; offline simulation mode; built on Python 3.5) | Paid, "Request A Quote" | Datasheet undated | [Catalogue](https://www.thermofisher.com/order/catalog/product/AUTOSCRIPT-TEM); [Datasheet](https://assets.thermofisher.com/TFS-Assets/MSD/Datasheets/autoscript-4-datasheet.pdf) | search snippet |
| Thermo Fisher | Connect Enterprise platform with NVIDIA integration; "fully autonomous instruments" said to reach customers in H2 2026 | Proprietary; no openness to third-party agents stated | 12 Jan 2026; 20 May 2026 | [Business Wire](https://www.businesswire.com/news/home/20260112999582/en/); [Deck](https://s25.q4cdn.com/974941731/files/doc_downloads/Downloads/2026-Investor-Day-Presentation-Distribution.pdf); [TIKR](https://www.tikr.com/blog/what-thermo-fisher-ceo-said-at-investor-day-that-the-market-is-still-processing) | company claim; timing is secondary |
| Agilent | OpenLab Sync (AI for instrument integration, workflow set-up, monitoring); GC Assist (monitoring, troubleshooting, remote connection "within the laboratory's secure network"); CrossLab Connect (Sigsense monitoring) | Proprietary; no third-party agent interface found | 26 May, 28 May and Feb 2026 | [GC Assist](https://www.investor.agilent.com/news-and-events/news/news-details/2026/Agilent-Launches-New-GC-Systems-with-GC-Assist-to-Improve-Laboratory-Efficiency-and-Data-Quality/default.aspx); [OpenLab Sync](https://www.businesswire.com/news/home/20260528098940/en/); [SLAS 2026](https://www.businesswire.com/news/home/20260204034151/en/) | search snippet |
| Bruker (Chemspeed / SciY) | "Open" self-driving lab platform with "vendor-agnostic integration"; no standard (SiLA, OPC UA) named; "We are delivering not only a platform, but a service engine" | Claimed open; no published standard | 9 Feb 2026 | [Bruker IR](https://ir.bruker.com/press-releases/press-release-details/2026/Chemspeed-and-SciY-Announce-SelfDriving-Laboratory-Platform-Integrating-Automation-Analytics-and-AI-Orchestration/default.aspx) | company claim |
| Bruker | Atinary integration: Chemspeed, Bruker instruments and SciY inside Atinary's agentic SDLabs; minority investment | Partner integration | 11 Aug 2026 | [Bruker IR](https://ir.bruker.com/press-releases/press-release-details/2026/Bruker-Announces-Strategic-Collaboration-with-Atinary-Technologies-to-Advance-Self-Driving-Laboratories/default.aspx) | company claim |
| Danaher | NVIDIA collaboration on "a select group of priority instruments" (DGX Spark at the edge, RAPIDS, BioNeMo; Cosmos and Omniverse exploratory). Aims at "preserving customer choice in models, standards and technology providers" | Partnership; openness to third-party agents not stated | 14 Oct 2026 | [Danaher IR](https://investors.danaher.com/2026-10-14-Danaher-Collaborates-with-NVIDIA-to-Advance-Autonomous-Science) | company claim (added in follow-up) |
| Danaher (Beckman Coulter) | Beckman Coulter instruments integrated with Automata LINQ; Danaher "exploring" MHS | Partner integration; pilot | Jan 2026; 27 Aug 2026 | [SelectScience](https://www.selectscience.net/article/beckman-coulter-life-sciences-partners-with-automata-to-accelerate-ai-ready-laboratory-automation); [Anthropic](https://www.anthropic.com/news/model-hardware-standard-research-preview) | company claim |
| Tecan | Fluent liquid handlers in the MHS research preview | Pilot (by application) | 27 Aug 2026 | [Anthropic](https://www.anthropic.com/news/model-hardware-standard-research-preview) | company claim |
| QIAGEN | QIAsymphony Connect MHS proof of concept | Pilot | 27 Aug 2026 | [Anthropic](https://www.anthropic.com/news/model-hardware-standard-research-preview) | company claim |
| Universal Robots, Doosan Robotics | MHS early access and testing | "nothing is generally available yet" (Universal Robots) | Aug–Sep 2026 | [Anthropic](https://www.anthropic.com/news/model-hardware-standard-research-preview); [IntuitionLabs](https://intuitionlabs.ai/articles/anthropic-hardware-standard-pharma-labs) | company claim |
| Hamilton, Opentrons, Tecan (EVO) | Third-party open-source PyLabRobot plr-mcp | Open source, unofficial | 2026 | [Glama](https://glama.ai/mcp/servers/di-omics/plr-mcp) | search snippet |
| Quantum control (Keysight, Quantum Machines, Qblox, QubiC, Zurich Instruments) | NVQLink "open system architecture" through CUDA-Q | Open architecture (NVIDIA's own term) | 28 Oct 2025 | [NVIDIA](https://nvidianews.nvidia.com/news/nvidia-nvqlink-quantum-gpu-computing) | company claim |
| DOE light sources | Bluesky/Ophyd/EPICS (open source); at ALS most beamlines use the internal LabVIEW-based Beamline Control System | Open (Bluesky, EPICS); facility-internal (ALS BCS) | 2026 | [LAP paper](https://arxiv.org/html/2606.03755); [Lightfall](https://arxiv.org/pdf/2606.06711) | independently confirmed: peer preprints by facility staff |
| Emerald Cloud Lab | Cloud lab platform | "closed, proprietary ecosystem" | as of Jun 2026 | [LAP paper](https://arxiv.org/html/2606.03755) | third-party assessment |

**Standards and protocols**

- **SiLA 2.** An open standard (on GitLab since 2018), with "typed, machine-readable capability descriptions and network discovery". One critique is that its capability descriptions are "fixed at design time" — [Intuition Labs summary of SiLA 2, Allotrope and LIMS integration](https://intuitionlabs.ai/pdfs/lab-instrument-integration-sila-2-allotrope-lims.pdf); [noze](https://www.noze.it/en/insights/model-hardware-standard-agents-lab-instruments/) [search snippet / secondary report]. No count of vendors or devices that support SiLA 2 was found.
- **OPC UA LADS.** Officially usable from 14 Dec 2023, with adoption free of charge. Developed by the OPC Foundation, SPECTARIS and VDMA — [SPECTARIS](https://www.spectaris.de/en/association/thespectarisindustries/networked-laboratory-equipment); [OPC Foundation](https://opcfoundation.org/?p=5692). SLAS rates its vendor support and user popularity "low" — [SLAS](https://www.slas.org/resources/standards/opc-ua-lads). One named adopter is VACUUBRAND (vacuum pumps) — [VACUUBRAND](https://www.vacuubrand.com/news/all-blog-posts/lads-opc-ua) [search snippets].
- **Allotrope.** "Full tooling requires consortium membership" (LAP paper's assessment) — [arXiv 2606.03755](https://arxiv.org/html/2606.03755).
- **MCP.** An open standard. "Authorization is OPTIONAL for MCP implementations" — [IntuitionLabs](https://intuitionlabs.ai/articles/anthropic-hardware-standard-pharma-labs).
- **MHS.** Research preview; the specification is not public; open-sourcing is promised after the preview — [noze](https://www.noze.it/en/insights/model-hardware-standard-agents-lab-instruments/). The MHS site says "MHS is starting as a limited research preview" and "Access is by application during the preview". It names no partners beyond Anthropic and HHMI Janelia, and states neither specification nor licence — [modelhardwarestandard.com](https://modelhardwarestandard.com) (read 12 Nov 2026) [added in follow-up]. The participant list therefore rests on Anthropic's own announcement plus Waters' own release; both are primary company sources.
- **LAP** (Shiyanjia Lab, China, arXiv 2 Jun 2026). A design proposal for agent-to-instrument control. It adds an InstrumentCard (capabilities and physical limits), reservations for exclusive access, a "safety-fence handshake" with operator tokens, and a MeasurementResult schema "with units, calibration, and uncertainty". It is "transport-compatible with the A2A/MCP ecosystem" and wraps existing standards such as SiLA 2 and OPC UA rather than replacing them — [arXiv 2606.03755](https://arxiv.org/html/2606.03755).
- **Buyer-side specification: "Letter of Intent on Open Standards for Life Sciences" [added in follow-up; primary].**
  - Published by SiLA on 6 Jul 2026 (post by Carmen Condrau). It is a 25-page DocuSign document, version 1.0.
  - Signatories on the first-signatures PDF:
    - Julia Heinrich, Roche Diagnostics GmbH (pRED)
    - Dietmar Krewer, Bayer AG CropScience
    - Geoffrey Pot, Takeda
    - Tore Karlsson and Roman Jansen, Novo Nordisk
    - François Clement Perrineau, BioNTech SE
    - Martin Clough, Syngenta Crop Protection AG
    - Andreas Essig, Lonza AG
    - Oskari Vinko, Botnar Institute of Immune Engineering
  - Signatories are lab-automation, operations and digital leads, not group executives. Syngenta was missing from the UniteLabs account.
  - Key text:
    - "Effective immediately, the undersigned organizations will prioritize and, where feasible, mandate the following capabilities in our evaluation of laboratory equipment and software".
    - Native SiLA 2 and/or OPC UA LADS "directly on the device firmware or embedded controller"; "wrapper" software is "considered a legacy solution and is strongly discouraged".
    - APIs for instrument control and data access "available through a one-time enablement fee. Recurring Fees are not an option".
    - APIs "fully and correctly documented, public".
    - "We explicitly reject 'walled garden' ecosystems".
    - "We anticipate initial progress and results to be evident by 2027".
    - The procurement mandate "applies strictly to new acquisitions"; vendors "must commit that all future product generations (released after 2027) will support native connectivity standards out-of-the-box".
    - On vendor business models: "vendors have viewed drivers, proprietary software interfaces, and closed data formats as 'competitive advantages' that create customer stickiness and generate revenue through licensing fees"; vendors without standard interfaces "will find themselves systematically excluded from Request for Proposals (RFPs)".
  - Legal force: binding status is not stated; the wording is "prioritize and, where feasible, mandate".
  - Sources: [SiLA post, 6 Jul 2026](https://sila-standard.com/letter-of-intent-on-open-standards-for-life-sciences/); [Letter PDF, first signatures](https://sila-standard.com/wp-content/uploads/2026/07/Letter-of-Intent-on-Open-Standards-for-Life-Sciences_firstSignatures.pdf)
- **SCPI and IVI.** Keysight's MCP server translates natural language into SCPI. An empty provider setting uses the "generic IVI VISA router" — [Keysight](https://helpfiles.keysight.com/kmsic/English/keysight_mcp_for_instrument_control/Content/getting-started.html). R&S MXO AI Connect uses VISA over HiSLIP, VXI-11 or TCP/IP — [Bisinfotech](https://www.bisinfotech.com/rohde-schwarz-introduces-mxo-ai-connect-for-ai-assisted-oscilloscope-workflows/).
- **EPICS, Bluesky, Tango.** EPICS and Bluesky: see the table. Tango: nothing gathered (gap).
- **SECS/GEM and SEMI EDA.** Not verified in this session (gap).

**What makers say about openness (quotes with dates)**

- Waters, Dave Leitham (VP Informatics), 13 Oct 2026: "AI can generate hypotheses faster than any lab can test them, so the bottleneck has moved from computation to the bench." Also: "In research, we connect AI agents to both the data and the instruments that generate it", and AI is "multiplying the sample volume running through our instruments and columns." — [PR Newswire (Waters release)](https://www.prnewswire.com/news-releases/waters-launches-ai-link-advancing-ai-enabled-lc-ms-workflows-from-research-to-release-302906439.html) [added in follow-up]; [BioPharma APAC](https://biopharmaapac.com/news/97/8561/waters-partners-with-anthropic-to-advance-ai-driven-autonomous-laboratory-workflows.html)
- Danaher, 14 Oct 2026: the NVIDIA collaboration aims at "preserving customer choice in models, standards and technology providers" — [Danaher IR](https://investors.danaher.com/2026-10-14-Danaher-Collaborates-with-NVIDIA-to-Advance-Autonomous-Science) [added in follow-up]
- Rohde & Schwarz, Philip Diegmann, 30 Oct 2026: "AI offers engineers a new way to work with increasingly capable test instruments." — [Bisinfotech](https://www.bisinfotech.com/rohde-schwarz-introduces-mxo-ai-connect-for-ai-assisted-oscilloscope-workflows/)
- Bruker/Chemspeed, Bernd Gleixner, 9 Feb 2026: "Vendor‑agnostic orchestration is key." SciY, Santi Dominguez: "customers are looking for open, readily deployable full stack SDLs" — [Bruker IR](https://ir.bruker.com/press-releases/press-release-details/2026/Chemspeed-and-SciY-Announce-SelfDriving-Laboratory-Platform-Integrating-Automation-Analytics-and-AI-Orchestration/default.aspx)
- TetraScience, Patrick Grady, 12 Jan 2026: "Scientific AI cannot be achieved on a foundation of fragmented systems and bespoke workflows." — [TetraScience](https://www.tetrascience.com/news/tetrascience-announces-collaboration-with-thermo-fisher-scientific-to-accelerate-scientific-data-and-ai-enablement-across-the-laboratory)
- Thermo Fisher, Gianluca Pettiti, January 2026: "Artificial intelligence coupled with laboratory automation will transform how scientific work is performed" — [Thermo Fisher AI ecosystem page](https://corporate.thermofisher.com/us/en/index/newsroom/Our-stories/AI-ecosystem.html)
- Anthropic, Jonah Cool, 27 Aug 2026: scientific equipment "suffers from proprietary solutions that are very brittle and often don't meet the need of scientists"; "We want to avoid vendor lock-in for scientists." — [Fortune](https://fortune.com/2026/08/27/anthropic-makes-first-move-into-physical-ai-with-universal-standard-for-scientists-manufacturing/). Cool also: "In many cases, the science doesn't happen because you can't use the equipment." — [The Next Web](https://thenextweb.com/news/anthropic-model-hardware-standard-mhs-eu-machinery-regulation-2027)

### Inferences
- The 2026 pattern is open protocol, closed dictionary. Makers adopt MCP, the open plumbing, but keep the command definitions, safety guardrails and procedures (Keysight's SOLT calibration, for example) inside their own server. Under MHS, "the vendor writes the file" ([The Next Web](https://thenextweb.com/news/anthropic-model-hardware-standard-mhs-eu-machinery-regulation-2027)). The maker therefore keeps its position as the authority on what the instrument can safely do.
- Openness falls with instrument price. Electronic test and LC-MS informatics opened first. Paid or gated APIs persist for electron microscopes (AutoScript, sold on quote), and no agent-interface announcement was found from the electron-microscope makers in this session's scope.

### Gaps
- No earnings-call quote was found in which a maker discusses opening control interfaces to third-party agents. The search budget ran out before transcripts could be searched.
- Not covered in this session: JEOL, Hitachi High-Tech, ZEISS (ZEN API), Tescan, Shimadzu, KLA, Applied Materials and Onto. Those makers' interface positions should come from the instrument-class researchers.
- Pricing and licence status of the Keysight and R&S MCP servers: not stated in their documentation.

---

## 3. Value-capture evidence

### Takeaway
None of the makers that shipped agent access in 2026 disclosed a price: Keysight, R&S, Waters, and Thermo Fisher with NVIDIA. All bundle it into their own software ecosystems (waters_connect, R&S AI Workplace, Thermo Fisher Connect Enterprise).

Makers present AI as a source of new demand for instruments and consumables, not as a threat to service revenue. Thermo Fisher's own revenue is 84% services and consumables, and it is using AI to "augment" its field-service engineers.

Users are pushing for open interfaces through procurement. A reported pharma letter of intent asks for open APIs by 2027, and DOE laboratories build their own agents. Third-party software layers show mixed results: growth funding where they are allied with a large maker (Automata, Atinary, TetraScience); pressure where they stand alone (Emerald Cloud Lab job cuts; a conflicting Benchling secondary-market mark).

### Cited Findings
- **No disclosed pricing.**
  - Keysight MCP server: not stated — [Keysight](https://helpfiles.keysight.com/kmsic/English/keysight_mcp_for_instrument_control/Content/getting-started.html).
  - R&S MXO AI Connect: not stated — [Bisinfotech](https://www.bisinfotech.com/rohde-schwarz-introduces-mxo-ai-connect-for-ai-assisted-oscilloscope-workflows/).
  - Waters AI Link: no pricing or deal value — [BioPharma APAC](https://biopharmaapac.com/news/97/8561/waters-partners-with-anthropic-to-advance-ai-driven-autonomous-laboratory-workflows.html).
  - MHS: no pricing or revenue model — [Fortune](https://fortune.com/2026/08/27/anthropic-makes-first-move-into-physical-ai-with-universal-standard-for-scientists-manufacturing/).
  - Thermo Fisher with NVIDIA and with TetraScience: financial terms undisclosed — [Fierce Biotech](https://www.fiercebiotech.com/medtech/thermo-fisher-scientific-teams-nvidia-tetrascience-next-gen-ai-workflow-projects).
  - Thermo Fisher AutoScript API: "Request A Quote" — [Thermo Fisher](https://www.thermofisher.com/order/catalog/product/AUTOSCRIPT-TEM).
- **Thermo Fisher's revenue mix.** LTM Q1 2026 revenue of $45B: services and consumables 84%, instruments 16%. ">85% services & consumables" is expected exiting 2026 — [Investor Day deck, 20 May 2026](https://s25.q4cdn.com/974941731/files/doc_downloads/Downloads/2026-Investor-Day-Presentation-Distribution.pdf) [company filing-based].
- **Service, aftermarket and recurring shares at other makers [added in follow-up; primary results documents].**
  - **KLA** (quarter ended 30 Sep 2026; letter dated 28 Oct 2026):
    - "Services revenue grew 4% sequentially and 14% year-over-year to $850 million in the quarter or 20% of" total revenue of $4.14B.
    - "the Services business remains on track for its 17th consecutive year of annual revenue growth. This recurring, subscription-like" business; services growth is expected "at the top end of the Services revenue growth rate model of 13 to 15%".
    - Revenue by region: China 34%, Taiwan 25%.
    - Source: [KLA Q1 FY27 shareholder letter](https://d1io3yog0oux5.cloudfront.net/_e2be8b99fd19637d99dedbc7b3bd0329/klatencor/db/1117/10679/letter_to_shareholders/KLA_Earnings_Shareholder_Letter_-_Q1_FY27.pdf)
  - **Waters**: ">70% of Revenue Annually Recurring", plus a 2025–30E outlook of "7% Revenue Growth CAGR" — [Waters IR homepage, read 12 Nov 2026](https://ir.waters.com/) [company claim]. The Q3 2026 results release could not be reached at known addresses (HTTP 404; newsroom renders dynamically) — could not verify the latest service and chemistry split.
  - **Agilent** (fiscal Q3 2026, quarter ended 31 Jul 2026; released 26 Aug 2026):
    - Agilent CrossLab Group revenue $786M (+6% reported, +5% core; operating margin 34.3%) of total revenue $1,878M. That is about 41.9% of revenue (my arithmetic from the release figures).
    - The release does not describe CrossLab's composition (service versus consumables).
    - Fiscal 2025 revenue was $6.95B — [Agilent IR](https://www.investor.agilent.com/).
    - Source: [Agilent Q3 FY2026 release](https://www.investor.agilent.com/news-and-events/news/news-details/2026/Agilent-Reports-Third-Quarter-Fiscal-Year-2026-Financial-Results/default.aspx)
  - **Shimadzu** (FY2026 H1, six months to 30 Sep 2026; slides dated 10 Nov 2026):
    - Analytical & Measuring Instruments "Recurring" sales of ¥77.5B (+17%), "Recurring sales ratio 44% (YoY +4pt)", where "*Recurring: Consumables, maintenance and services".
    - Recurring sales: FY2023 ¥122.3B, FY2024 ¥133.3B, FY2025 ¥142.5B; FY2028 plan ¥180.0B, ratio target 43%.
    - Medical systems recurring ratio 39%; turbomolecular-pump (semiconductor) recurring ratio 21%.
    - Stated strategy: "Maximize value via remote service using MVS business" and "Expand paid plans incl. analysis/data support globally".
    - Source: [Shimadzu H1 slides](https://www.shimadzu.com/sites/shimadzu.com/files/ir/r272/7zicbmkg9z2n0leo.pdf)
  - **Not disclosed in the latest releases read:**
    - Bruker Q3 2026 (4 Nov 2026; revenue $874.0M; by segment only) — [Bruker IR](https://ir.bruker.com/press-releases/press-release-details/2026/Bruker-Reports-Third-Quarter-2026-Financial-Results/default.aspx).
    - Keysight fiscal Q3 2026 (18 Aug 2026; revenue $1,846M; orders $2,091M; no software and services figure) — [Keysight IR](https://investor.keysight.com/investor-news-and-events/financial-press-releases/press-release-details/2026/Keysight-Technologies-Reports-Third-Quarter-2026-Results/default.aspx).
    - Danaher Q3 2026 (21 Oct 2026; sales $6,554M; no recurring share in the release or the deck text) — [Danaher IR](https://investors.danaher.com/2026-10-21-Danaher-Reports-Third-Quarter-2026-Results).
  - **Vendor statements on whether agents threaten or extend service:**
    - None found that call agent-run set-up a threat.
    - Waters frames agents as extending consumables and instrument use ("multiplying the sample volume running through our instruments and columns") — [Waters release](https://www.prnewswire.com/news-releases/waters-launches-ai-link-advancing-ai-enabled-lc-ms-workflows-from-research-to-release-302906439.html).
    - Shimadzu frames remote service and paid data plans as growth.
    - Thermo Fisher frames AI as augmenting its own field-service engineers (below).
- **Thermo Fisher's internal use of AI.**
  - "Augmenting technical support, field service engineers and application specialists" and "Faster software development for instrument product lines" — [deck slide 62](https://s25.q4cdn.com/974941731/files/doc_downloads/Downloads/2026-Investor-Day-Presentation-Distribution.pdf).
  - CFO Jim Meyer reportedly sized AI-enabled productivity at about $80–100M a year above historical norms — [TIKR](https://www.tikr.com/blog/what-thermo-fisher-ceo-said-at-investor-day-that-the-market-is-still-processing) [secondary report, paraphrase].
- **Makers frame AI as a demand driver.**
  - Thermo Fisher: "New demand for wet lab experiments to generate high-quality data for AI-based biology models"; AI "expected to expand industry demand" — [deck slides 25–27](https://s25.q4cdn.com/974941731/files/doc_downloads/Downloads/2026-Investor-Day-Presentation-Distribution.pdf).
  - Marc Casper, 23 Apr 2026: "You're seeing very wide-scale, large volume labs that are just trying to build biology models", and they want instruments that are "automated-ready" — [Lab Manager](https://www.labmanager.com/thermo-fisher-kicks-off-2026-with-new-instruments-ai-push-and-a-warning-on-rising-lab-costs-35274).
  - Waters: AI-directed workflows "already generating new demand for Waters instruments and consumables" (not quantified) — [BioPharma APAC](https://biopharmaapac.com/news/97/8561/waters-partners-with-anthropic-to-advance-ai-driven-autonomous-laboratory-workflows.html) [company claim].
- **Remote and predictive service sold by the maker.**
  - Agilent's CrossLab Connect added "AI-driven lab optimization tools ... enabled by Sigsense intelligent monitoring" (SLAS, Feb 2026) — [Business Wire](https://www.businesswire.com/news/home/20260204034151/en/).
  - GC Assist offers "built-in troubleshooting, and remote connectivity" (26 May 2026) — [Agilent IR](https://www.investor.agilent.com/news-and-events/news/news-details/2026/Agilent-Launches-New-GC-Systems-with-GC-Assist-to-Improve-Laboratory-Efficiency-and-Data-Quality/default.aspx) [search snippets].
  - Whether these are sold by subscription was not established.
- **Third-party layers: wins and setbacks.** Automata $45M (Danaher strategic); Opentrons $40M; Bruker investing in Atinary; Emerald Cloud Lab job cuts and a closed ecosystem; Benchling's secondary-market mark ($0.9B estimate versus $6.1B in 2021, conflicting); BICO selling assets to cut debt while keeping Biosero. Sources are in section 1.
- **Autonomous-lab operators: valuations without disclosed revenue.**
  - Lila: in talks at about $8.5B before new money; no revenue disclosed. Startup Fortune notes that commercialisation "may depend on partners for clinical trials, manufacturing, regulation" — [Startup Fortune](https://startupfortune.com/lila-sciences-is-testing-how-much-investors-will-pay-for-automated-labs/).
  - Periodic: "paying customers in the semiconductor industry", amount unknown — [Dealroom](https://dealroom.co/news/127042-periodic-labs-eyes-7b-valuation-fivefold-jump-in-six-months/).
  - XtalPi: revenue RMB 803M, including robot-lab systems sold as delivered solutions — [XtalPi deck](https://ir.xtalpi.com/media/u0gcv5md/2025-annual-investor-pre-cn-final-1.pdf).
- **Users building their own agents on open-source stacks.**
  - LBNL: the ALS Accelerator Assistant (Osprey on EPICS) — [NVIDIA blog](https://blogs.nvidia.com/blog/ai-copilot-berkeley-x-ray-particle-accelerator); Lightfall (Bluesky, Ophyd, NATS, MCP bridge) — [arXiv 2606.06711](https://arxiv.org/pdf/2606.06711).
  - Lightfall's economics: "the bottleneck moves from developer-hours-per-beamline to the design quality of the underlying API", and "the per-iteration cost of a scientist-driven change is then fixed in the scientist's own time rather than in developer hours the facility must supply" — [arXiv 2606.06711](https://arxiv.org/pdf/2606.06711).
  - Genentech, Carnegie Mellon, the University of Washington and Janelia on MHS — [Anthropic](https://www.anthropic.com/news/model-hardware-standard-research-preview).
  - Chip fabs building their own agents: no evidence found (gap).
- **Customer pushback (procurement).** UniteLabs reports a letter of intent signed by Roche, Bayer, Takeda, BioNTech, Lonza, Novo Nordisk and the Botnar Institute. It calls for open connectivity in all new hardware procurement agreements, with open APIs required by 2027. UniteLabs also writes: "if a vendor sells robots, their 'open' platform is really a sales funnel" — [UniteLabs blog, 21 Jul 2026](https://unitelabs.io/resources/blog/end-times-fragmentation-tax-sila/). [secondary report from an interested party, a SiLA 2 software vendor; the letter's own text could not be verified]
- **Data ownership and vendor intent.**
  - Thermo Fisher's deck cites "differentiated investments in large-scale datasets, AI and advanced analytics" and a "Rich set of customer purchasing and behavior data powering AI models" — [deck slides 26 and 64](https://s25.q4cdn.com/974941731/files/doc_downloads/Downloads/2026-Investor-Day-Presentation-Distribution.pdf).
  - Anthropic says API inputs and outputs are deleted from its backend within 30 days — [IntuitionLabs](https://intuitionlabs.ai/articles/anthropic-hardware-standard-pharma-labs) [secondary report].
  - Lila's thesis: "proprietary experimental data from closed-loop labs becomes a scarce asset" — [Startup Fortune](https://startupfortune.com/lila-sciences-is-testing-how-much-investors-will-pay-for-automated-labs/).
  - The R&S MXO AI Connect user chooses the "data handling policy", and instrument traffic stays "within the local environment" — [Bisinfotech](https://www.bisinfotech.com/rohde-schwarz-introduces-mxo-ai-connect-for-ai-assisted-oscilloscope-workflows/).

### Inferences
- Value capture so far favours the instrument maker.
  - The maker writes the command dictionary and the safety file and hosts the MCP server in its own software (waters_connect, R&S AI Workplace, Connect Enterprise).
  - The model supplier earns usage revenue on whichever model the customer picks; three of the four maker MCP launches name Claude clients as tested.
  - The independent orchestration layer captures value only where it is the maker's chosen data partner: TetraScience for Thermo Fisher.
- The threat to service revenue is real but indirect. MHS lets users "describe their hardware in natural language" to generate reference files, which bypasses the application-specialist labour that sits inside service contracts. Makers' 2026 response has been to take that labour saving themselves, as Thermo Fisher's AI-augmented field service shows, rather than to resist.
- Users capture value where they control procurement (the pharma letter of intent) or build their own stacks (DOE laboratories). These are the two places where open interfaces are being forced rather than granted.

### Gaps
- Terms on instrument data in vendor clouds could not be verified (search budget exhausted): Thermo Fisher Connect and Ardia, waters_connect, ZEISS arivis Cloud, Bruker SciY, Agilent. No customer pushback on data terms was found beyond the pharma letter of intent.
- Service-contract share of revenue for Agilent (CrossLab), Waters, Bruker, Mettler-Toledo, Keysight, KLA, Zeiss, JEOL, Shimadzu and Hitachi: not gathered here. The instrument-class researchers should supply these.
- No subscription price for any agent feature was found from any maker.

---

## 4. Government programmes

### Takeaway
The US Genesis Mission is the largest programme that shapes interfaces. Its platform's planned "American Science Cloud" APIs include a "core agentic framework" covering orchestration, reasoning models and "Telemetry & control". It is built with MCP tools and "open protocols". No open-interface requirement on instrument vendors was found in DOE documents. China (the State Council's AI+ opinion, Beijing's plan to upgrade research instruments with intelligence), South Korea (KRW 49.5bn for bio autonomous labs; four materials autonomous-lab centres) and Japan (the AI4S programme; a JPY 9.5bn shared smart cloud lab) all fund autonomous labs. None found mandates open instrument interfaces. EU coverage is thin; the EU Machinery Regulation (from 20 Jan 2027) is the main EU rule found that bears on agents controlling machinery.

### Cited Findings
- **United States: the Genesis Mission.**
  - Executive Order 14363, signed 24 Nov 2025. The platform, the "American Science and Security Platform", "connects and integrates infrastructure (computing infrastructure together with other scientific instrumentation and DOE assets), data, and models".
  - Its American Science Cloud APIs list "CORE AGENTIC FRAMEWORK: Orchestration, Reasoning models, Telemetry & control". The consortium has working groups on "data integration and standards" and "robotics and automation".
  - Challenges include "Achieving AI-Driven Autonomous Laboratories" and "Enhancing Particle Accelerators for Discovery: Deploying AI to make accelerators adaptive and autonomous".
  - Early projects: MOAT (Multi-Office Accelerator Operations & Controls), SYNAPS-I (Light and Neutron Imaging foundation model), OPAL-OMAHA (bio and autonomous labs), and the Autonomous Microelectronics Consortium.
  - The funding call totals $293M: Phase I awards of $0.5–0.75M over nine months; Phase II awards of $6–15M over three years.
  - Source: [DOE Office of Science advisory committee (SCAC) slides, 27 Mar 2026](https://science.osti.gov/-/media/About/pdf/scac/meetings/2026/DOE-Genesis-Mission-Launched---2026-03-27.pdf) [primary].
- **Genesis selections and platform demo, 22 Jul 2026.**
  - 278 projects (87 led by laboratories, 168 by universities, 19 by companies, 4 by nonprofits) across 342 institutions, 157 of them companies. The largest is $60M for nuclear energy. "Awardees will gain access to the Genesis Mission Platform, including AI agent frameworks, advanced AI models". No open-interface or open-data requirement is stated — [DOE, 22 Jul 2026](https://www.energy.gov/articles/secretary-energy-chris-wright-announces-first-genesis-mission-projects-selected-accelerate) [primary].
  - The demo was pre-recorded. It showed a Model Access Gateway, "DOE-developed model context protocol tools", and users connecting their own tools through open protocols. About $250M of the $293M was already allocated — [FedScoop, 22 Jul 2026](https://fedscoop.com/energy-department-demo-genesis-mission-platform-rfa-awards/) [secondary report].
- **Genesis MOUs with 24 organisations** (DOE list dated 18 Dec 2025). Named: Google DeepMind, Anthropic, OpenAI, NVIDIA (priorities: "open AI science models, robotics and autonomous labs, nuclear fission and fusion, and quantum computing"), Microsoft, AWS, Oracle, IBM, Intel, AMD, Dell, HPE, Palantir and xAI. No instrument maker is named — [TechInformed, 24 Dec 2025](https://techinformed.com/doe-and-24-organizations-sign-ai-collaboration-deal/) [secondary report]. Another search summary dated the MOUs to February 2026, which conflicts.
- **Europe and CERN.** CERN openlab's A-GHOST project uses NVIDIA DAQIRI on ATLAS data — [NVIDIA ISC release](https://usa-automation.net/news/112167-nvidia-introduces-ai-software-libraries-for-scientific-research).
- **EU Machinery Regulation 2023/1230.** It replaces the Machinery Directive on 20 Jan 2027. It is the first machinery rule to cover "AI-based safety functions" and machinery with self-evolving behaviour. An MHS safety-limit file could count as a safety function needing a notified body — [The Next Web analysis](https://thenextweb.com/news/anthropic-model-hardware-standard-mhs-eu-machinery-regulation-2027) [secondary report].
- **China.**
  - The State Council's 《关于深入实施"人工智能+"行动的意见》 (August 2025) sets an "人工智能+" science and technology action ("AI+ science"), aiming for a new AI-based research paradigm — [Xinhua, 28 Aug 2025](https://www.news.cn/tech/20250828/5af2930138044797909cf407e7ba119b/c.html).
  - Beijing's plan (July 2026) has 18 tasks. They include building autonomous labs, "推动重大科技基础设施和科研仪器智能化升级" (intelligent upgrading of major research infrastructure and instruments), and research agents. Its six fields include high-energy physics, materials and quantum — [NCSTI, 2 Jul 2026](https://www.ncsti.gov.cn/zcfg/zcjd/202607/t20260702_250678.html) [search snippet; page fetch failed with HTTP 503].
  - Beijing cases (21 Aug 2026): a Tsinghua chemistry platform ran unattended at 10–30x human efficiency. The same report says fully closed-loop autonomous labs still face "技术瓶颈" (technical bottlenecks) in autonomous decision-making in complex scenarios — [Beijing Daily](https://news.bjd.com.cn/2026/08/21/11926168.shtml) [search snippet].
- **Japan.**
  - MEXT's shared "大規模スマートクラウドラボ" (large-scale smart cloud lab) runs FY2026–2029 with a total budget of about JPY 9.5bn, of which JPY 4.36bn is in the FY2026 budget; 2026–2027 is for setting up automated synthesis and dispensing equipment — [MEXT, 21 Feb 2026](https://www.mext.go.jp/content/20260221-mxt_nanozai-000046621_8.pdf) [search snippet quoting the PDF].
  - The FY2027 budget request includes JPY 378.9bn for AI4S (a request, not final) — [Newswitch](https://newswitch.jp/p/50165) [secondary report].
  - MEXT's "AI for Scienceによる科学研究革新プログラム" (AI for Science research innovation programme) runs FY2025–2028. JST-CRDS distinguishes "自律系AI4S" (AI performing research) from "支援系AI4S" (AI supporting human researchers) [search snippet; source PDF not identified precisely].
- **South Korea.**
  - MSIT's "AI-네이티브 첨단바이오 자율실험실" (AI-native advanced bio autonomous lab) programme: KRW 49.5bn through 2028; one general-purpose lab and five specialised labs; the Catholic University of Korea leads the K-Cell platform; part of the K-Moonshot drug-development mission — [Herald Economy, 11 Jun 2026](https://www.heraldk.com/article/2026061118413174490).
  - MSIT's draft AI materials R&D platform strategy for 2026–2030 (30 Apr 2026) has four autonomous lab centres: batteries; hydrogen and energy; aerospace and mobility metals; organic semiconductors and display. No budget is stated — [Dong-A Science via Daum, 30 Apr 2026](https://v.daum.net/v/20260430101533808).
  - K-Moonshot strategy document (March 2026) — [PDF](https://smartcity.go.kr/wp-content/uploads/2026/03/안건4AI시대과학기술경쟁력대도약을위한K-문샷추진전략안.pdf).

### Inferences
- Genesis is building an agent-ready API layer on the facility side ("Telemetry & control" inside the American Science Cloud) and supplying MCP tools itself. If DOE facilities expose instruments through their own open APIs, as Bluesky and Lightfall do, the government-funded physics-instrument market will tend toward user-owned interfaces whatever vendors decide.
- Asian programmes fund autonomous labs, mostly in chemistry, materials and bio, and stress "standardised data". None was found that requires vendors to open control interfaces.

### Gaps
Could not verify (search budget exhausted):
- NSF and NIH programmes.
- The EU RAISE initiative and other EU AI-for-science instruments.
- UK programmes, including the Google DeepMind automated lab.
- Taiwan (NSTC), India (Anusandhan National Research Foundation and the IndiaAI Mission) and Israel.
- A reported "Autonomous Laboratory industry-academia-research council" in Korea (launched 11 Aug 2026 with about 80 institutions) and a reported KRW 13.5bn new budget line appeared only in a blog and a search summary.
- A reported Genesis consortium figure of more than $800M from 40 organisations could not be traced to a page read in full.

---

## 5. Test of the priors

### Takeaway
- **Prior (i)** ("at least two major instrument makers ship agent-run alignment and calibration as a standard feature by 2028", 65%):
  - Loosely read, it is close to met already in electronic test. Keysight's MCP server ships built-in calibration (SOLT) and sweep procedures that an LLM agent invokes with engineer approval. R&S ships LLM control of oscilloscopes.
  - Strictly read (autonomous alignment or calibration as a standard, included feature on complex instruments such as electron microscopes, synchrotrons or accelerators), no maker had shipped it by November 2026. The nearest candidate is Thermo Fisher's reported "first version of fully autonomous instruments" for H2 2026, and it is unverified.
- **Prior (ii)** ("closed interfaces and hardware-damage risk are the main obstacles"): partly supported. Fragmented and closed interfaces are the obstacle cited most often. Practitioners say damage risk is handled by hardware interlocks below the agent. The constraints they name as binding are:
  - agent reliability on novel situations and fault diagnosis;
  - governance and delegation;
  - GxP validation and audit trails;
  - certification (the EU Machinery Regulation from 2027);
  - cybersecurity.
- **"The field has received little attention"**: contradicted for autonomous labs broadly. Funding from 2025 to 2026 runs into billions, and many large companies made announcements. It is closer to true for agent-run tuning of physics instruments, which remains mainly national-laboratory work.

### Cited Findings

**Prior (i): shipped products and dated announcements by major makers, as of 12 Nov 2026**

LLM-agent control:

| Maker | Product | Status | Alignment or calibration? | Source |
|---|---|---|---|---|
| Keysight | MCP Server for Instrument Control | Downloadable (2026) | Yes, partly: built-in "SOLT calibration" and S-parameter sweep procedures, each sequence approved by an engineer | [Keysight](https://helpfiles.keysight.com/kmsic/English/keysight_mcp_for_instrument_control/Content/overview.html) [company documentation] |
| Rohde & Schwarz | MXO AI Connect | "now available" (30 Oct 2026) | No calibration-specific claim; general oscilloscope control | [Bisinfotech](https://www.bisinfotech.com/rohde-schwarz-introduces-mxo-ai-connect-for-ai-assisted-oscilloscope-workflows/) |
| Waters | AI Link | Early access October 2026, general availability November 2026 | No: sample lists, acquisition, data | [BioPharma APAC](https://biopharmaapac.com/news/97/8561/waters-partners-with-anthropic-to-advance-ai-driven-autonomous-laboratory-workflows.html) |
| Thermo Fisher | "the first version of fully autonomous instruments being deployed to our customers in the second half of the year" (Pettiti, 20 May 2026) | Announced; shipment not verified | Unknown | [TIKR](https://www.tikr.com/blog/what-thermo-fisher-ceo-said-at-investor-day-that-the-market-is-still-processing) [secondary report] |
| Danaher | Autonomous lab with Genedata AI co-scientist coordinating a protein-design foundry | Announced 21 Oct 2026 | Workflow, not instrument tuning | [NVIDIA](https://nvidianews.nvidia.com/news/healthcare-and-life-sciences-leaders-build-on-nvidia-to-advance-drug-discovery-and-expand-patient-care) |
| Bruker (with Atinary) | Agentic closed-loop self-driving lab (Chemspeed plus Fourier 80 NMR) | Demonstrated, 11 Aug 2026 | Workflow | [Bruker IR](https://ir.bruker.com/press-releases/press-release-details/2026/Bruker-Announces-Strategic-Collaboration-with-Atinary-Technologies-to-Advance-Self-Driving-Laboratories/default.aspx) |
| Tecan, QIAGEN (MHS) | Pilots | Research preview | Not stated | [Anthropic](https://www.anthropic.com/news/model-hardware-standard-research-preview) |
| QuEra (quantum computer maker, MHS pilot) | Agent-developed laser-relock recovery controller | Pilot; 695 of 700 trials succeeded (99.3%) | Yes: an alignment-type task (laser lock), partner-reported | [Anthropic](https://www.anthropic.com/news/model-hardware-standard-research-preview); [elmerdata](https://elmerdata.bearblog.dev/who-gave-the-ai-control-of-the-laboratory/) |
| NI (Emerson) | Nigel in LabVIEW 2026 Q3 | Shipped | No: writes code | [Electronic Design](https://www.electronicdesign.com/technologies/embedded/machine-learning/video/55396195/electronic-design-whats-new-with-nigel-and-labview-2026) |

Classical automatic or machine-learning routines (not LLM agents):

| Maker | Product | Date | Source |
|---|---|---|---|
| Thermo Fisher | Vulcan Automated Lab ("AI-enhanced transmission electron microscopes with integrated robotic handling") | Introduced 18 Mar 2025 | [Business Wire](https://www.businesswire.com/news/home/20250318064982/en/Thermo-Fisher-Scientific-Introduces-the-Vulcan-Automated-Lab-to-Transform-Semiconductor-Analysis); [deck slide 43](https://s25.q4cdn.com/974941731/files/doc_downloads/Downloads/2026-Investor-Day-Presentation-Distribution.pdf) |
| Thermo Fisher | Krios 5 cryo-TEM and Orbitrap Astral Zoom, "Enhanced with AI and automation capabilities" | — | [deck slide 36](https://s25.q4cdn.com/974941731/files/doc_downloads/Downloads/2026-Investor-Day-Presentation-Distribution.pdf) |
| Agilent | GC Assist (monitoring, built-in troubleshooting) | 26 May 2026 | Agilent release |
| Agilent | Gen5 AI Cell Identification module ("without requiring conventional threshold setting or parameter tuning") | 29 Sep 2026 | Agilent release |
| Agilent | xCELLigence eSight AI module (cuts "parameter tuning") | 1 Jul 2026 | Agilent release |

Agilent sources: [Agilent IR](https://www.investor.agilent.com/news-and-events/news/news-details/2026/Agilent-Launches-AI-Driven-Analysis-Module-for-Agilent-xCELLigence-RTCA-eSight/default.aspx); [Finviz](https://finviz.com/news/396436/agilent-introduces-gen5-ai-cell-identification-module-for-biotek-automated-cell-imagers) [search snippets].

**Prior (ii): obstacles that practitioners and vendors actually name**

- **Interfaces.**
  - Anthropic: "there is no common way for them to share data with an AI agent"; devices lack programming interfaces; device knowledge lives "in paper manuals, on local computers, or as tacit knowledge"; MHS "does not yet work with hardware lacking a programming interface" — [Anthropic](https://www.anthropic.com/news/model-hardware-standard-research-preview).
  - The LAP paper: "every such system rebuilds the link between the reasoning agent and the physical instrument from scratch", and "instruments expose diverse vendor APIs with inconsistent command interfaces, telemetry formats, and safety semantics" — [arXiv 2606.03755](https://arxiv.org/html/2606.03755).
  - A Carnegie Mellon plate reader had to be driven through its graphical interface — [elmerdata](https://elmerdata.bearblog.dev/who-gave-the-ai-control-of-the-laboratory/).
- **Damage and safety: named, but handled below the agent.**
  - The LAP paper says operations "can injure people or destroy equipment" — [arXiv 2606.03755](https://arxiv.org/html/2606.03755).
  - Lightfall: "Protection against hardware damage and operator injury is the responsibility of lower layers: the device controllers ... and the independent hardware safety systems ... Both refuse unsafe commands regardless of origin (LLM, human operator, or any other API client)" — [arXiv 2606.06711](https://arxiv.org/pdf/2606.06711).
  - Keysight requires approval before every command sequence and "stops the sequence as soon as one command fails" — [Keysight](https://helpfiles.keysight.com/kmsic/English/keysight_mcp_for_instrument_control/Content/overview.html).
  - lab-mcp warns that an assistant can switch outputs on — [PyPI](https://pypi.org/project/labmcp/).
- **Agent reliability and scientific validity.**
  - Lightfall: "Highly novel or open-ended experiment planning, and fault diagnosis under ambiguous conditions, remain beyond reliable agent performance today", and "What is not yet in place is a principled, adversarially evaluated policy that characterizes when the agent can be trusted to act unattended" — [arXiv 2606.06711](https://arxiv.org/pdf/2606.06711).
  - Genentech had to show Claude that foaming was a physical failure, not a software bug — [Anthropic](https://www.anthropic.com/news/model-hardware-standard-research-preview).
  - A Genentech agent retried a BCA assay in the same well after a bubble error, making it worse. A Carnegie Mellon agent cut the top concentration from 200 to 100 µg/mL without human input. Tetsuwan's data were partly distorted by plate-edge evaporation — [elmerdata](https://elmerdata.bearblog.dev/who-gave-the-ai-control-of-the-laboratory/).
  - Beijing: "技术瓶颈" (technical bottlenecks) in autonomous decisions in complex scenarios — [Beijing Daily](https://news.bjd.com.cn/2026/08/21/11926168.shtml) [search snippet].
- **Governance, validation and traceability.**
  - "The institution must be able to explain who authorised the action, what limits applied, and what actually happened" — [elmerdata](https://elmerdata.bearblog.dev/who-gave-the-ai-control-of-the-laboratory/).
  - "A conversational transcript alone does not satisfy this record model" (21 CFR Part 11), and "A lab unable to pin versions, deny unsafe calls, reproduce runs, and export complete audit evidence should wait" — [IntuitionLabs](https://intuitionlabs.ai/articles/anthropic-hardware-standard-pharma-labs).
  - Waters' AI Link explicitly carries audit trails into Empower for regulated settings — [BioPharma APAC](https://biopharmaapac.com/news/97/8561/waters-partners-with-anthropic-to-advance-ai-driven-autonomous-laboratory-workflows.html).
- **Certification.** The EU Machinery Regulation, from 20 Jan 2027, may require a notified body for AI-based safety functions — [The Next Web](https://thenextweb.com/news/anthropic-model-hardware-standard-mhs-eu-machinery-regulation-2027).
- **Cybersecurity.** "Authorization is OPTIONAL for MCP implementations" — [IntuitionLabs](https://intuitionlabs.ai/articles/anthropic-hardware-standard-pharma-labs). The Genesis funding call includes a topic on "Cybersecurity for AI-driven Science Workflows" — [DOE SCAC slides](https://science.osti.gov/-/media/About/pdf/scac/meetings/2026/DOE-Genesis-Mission-Launched---2026-03-27.pdf).
- **Commercial obstacles for physical AI generally.** "Unclear business models", "Immature support and service networks", "Uncertain ROI" — [ABI Research, 8 Apr 2026](https://www.abiresearch.com/market-research/insight/7787716-platform-progress-commercial-patience-nvid?hsLang=en).
- **Named by no source found:**
  - cannibalisation of service revenue;
  - liability and warranty;
  - metrological traceability as an obstacle. LAP does propose carrying "calibration, and uncertainty" in its result schema — [arXiv 2606.03755](https://arxiv.org/html/2606.03755).
  - Data rights appear only indirectly, in the pharma letter of intent and Lila's data thesis.

**Test of "little attention"**

- Autonomous-lab and agent-lab capital, 2025–2026:
  - Lila: $550M raised; talks at about $2B and $8.5B before new money.
  - Periodic Labs: $300M seed; talks at $7–7.5B.
  - Automata: $45M. Opentrons: $40M.
  - XtalPi: RMB 2.54bn net from 2026 convertible bonds.
  - Bruker's investment in Atinary.
  - Sources in section 1.
- Large-company announcements: Thermo Fisher with NVIDIA (January 2026), with OpenAI (October 2025) and with TetraScience (January 2026); Anthropic MHS (August 2026) and Claude Science (June 2026); NVIDIA BioNeMo Agent Toolkit, DAQIRI and NVQLink; Keysight, R&S and Waters MCP launches; Danaher's autonomous lab. Sources in sections 1 and 2.
- Government: Genesis ($293M funding call, 278 projects); Korea (KRW 49.5bn); Japan (JPY 9.5bn smart cloud lab); Beijing plan. Sources in section 4.

### Inferences
- On prior (i), the trajectory from zero to three makers shipping LLM-agent instrument control within about six months of 2026 (Keysight, R&S, Waters) supports the prior's direction. But each launch is human-approved, procedure-bound, and sits in mid-priced electronic test or LC-MS informatics.
- The 2028 test should be defined before the evidence is scored:
  - **"Agent can invoke the vendor's calibration routine"**: already met by Keysight. A second maker in electronic test looks plausible on 2026 momentum.
  - **"Agent autonomously aligns a complex instrument as a standard feature"**: no evidence yet. It depends on Thermo Fisher's H2 2026 "fully autonomous instruments" turning out to be a real product.
- On prior (ii), the evidence moves the main obstacle from "damage risk" to "trusted unattended operation". Interlocks already handle damage. What is missing is a validated, auditable policy for when an agent may act without a human. Interfaces remain the most-cited obstacle, but they are opening on vendor terms.

### Gaps
- Electron-microscopy, X-ray, accelerator, chip-metrology and quantum-control makers' own 2025–2026 auto-alignment launches, classical or agentic, beyond those listed: left to the instrument-class researchers. The search budget ran out before vendor-by-vendor checks.
- Thermo Fisher's "fully autonomous instruments": no product name, launch release or customer confirmation was found.

---

## 6. Leading software-layer companies and NVIDIA

Selection: NVIDIA (named by the user), Anthropic (sets the agent-to-hardware protocol), TetraScience (the vendor-agnostic data layer chosen by Thermo Fisher) and Automata (orchestration and robotics, backed by Danaher). Lila and Periodic are treated in section 7 as labs, not layers. Valuation and entry point are excluded throughout.

### 6.1 NVIDIA

**Identity.** US-based maker of GPUs and AI systems, listed. The listing (Nasdaq: NVDA) was not re-verified in this session.

**Funding and financial scale.**
- Q2 FY2027 (quarter ended 26 Jul 2026): revenue $96,221M, up 106% year on year. Data Center $89.0B, up 117%. Edge Computing $7.2B, up 27%.
- Q3 FY2027 outlook: $108.0B ±2%, with gross margin of 74.0%. "NVIDIA is not assuming any Data Center compute revenue from China in its outlook."
- Source: [NVIDIA, Q2 FY2027 results](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027) [primary].

**How much of its business the theme touches.**
- No disclosure lets the scientific-instrument theme be quantified. The Q2 release does not separate healthcare, science or instrument revenue — [NVIDIA](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027).
- The instrument-facing items are mostly software libraries (Holoscan with DAQIRI, cuPhoton, ALCHEMI NIMs, the BioNeMo Agent Toolkit), small systems (DGX Spark at Thermo Fisher), an open interconnect (NVQLink), and venture stakes (NVentures led Lila's $115M extension).
- No figure was found, and I make no estimate. Nothing seen suggests the theme is material to a company with $96.2B of quarterly revenue.

**Test (a), position.**
- NVIDIA owns no judge: no instrument, installed base or measurement data.
- Its constraint position is in low-latency compute coupled to the instrument. NVQLink exists because quantum-control algorithms "must run over an extremely demanding low-latency, high-throughput connection" — [NVIDIA](https://nvidianews.nvidia.com/news/nvidia-nvqlink-quantum-gpu-computing).
- Its interfaces are open by design (NVQLink "open system architecture"; Holoscan Sensor Bridge open source; BioNeMo "open development platform"). Value comes back to NVIDIA through hardware sales.

**Test (b), lead (outside evidence).**
- Five quantum control-system builders and 17 quantum-processor builders support NVQLink, and national laboratories guided it — [NVIDIA](https://nvidianews.nvidia.com/news/nvidia-nvqlink-quantum-gpu-computing) [company claim listing third parties].
- Thermo Fisher chose NVIDIA for instrument AI — [Business Wire](https://www.businesswire.com/news/home/20260112999582/en/).
- LBNL's ALS assistant runs on an H100 — [NVIDIA blog](https://blogs.nvidia.com/blog/ai-copilot-berkeley-x-ray-particle-accelerator).
- CERN's A-GHOST project uses DAQIRI — [NVIDIA ISC release](https://usa-automation.net/news/112167-nvidia-introduces-ai-software-libraries-for-scientific-research).
- Counter-evidence: ABI Research finds "still little evidence of large-scale, revenue-generating deployments built around GR00T or Cosmos" — [ABI Research](https://www.abiresearch.com/market-research/insight/7787716-platform-progress-commercial-patience-nvid?hsLang=en).

**Test (c), revenue model.** Revenue is dominated by data-centre hardware. The instrument libraries mostly serve to pull hardware demand; no revenue was disclosed for them. Little depends on labour hours or seats, but much depends on hardware cycles.

**Test (e), resilience.**
- NVIDIA's revenue is the AI-spending cycle itself:
  - Steady growth (about 55%): continued data-centre growth.
  - Financing-led pause around 2028 (about 25%): the most exposed of the companies in this note, through data-centre hardware.
  - Faster acceleration (about 20%): the largest beneficiary.
- The instrument theme is too small to buffer any of these scenarios.
- Export controls: the outlook already excludes China data-centre compute — [NVIDIA](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027).

**Transitions.**
- T1 (expert set-up to agent set-up): beneficiary, since more inference runs at the instrument (DGX Spark, H100 in control rooms).
- T2 (closed to open interfaces): beneficiary and promoter (NVQLink, Holoscan Sensor Bridge).
- T3 (hardware to software revenue): not applicable to its own model; its software is given away to sell hardware.
- T4 (cheaper hardware, heavier computation): the main beneficiary.
- T5 (instruments as data sources for customers' own AI): neutral. Data stays with customers; NVIDIA sells the compute.

**Verdict.** An essential enabler, but not a self-tuning-instrument company, and the theme is immaterial to its revenue. It belongs among the 8–15 most important companies only as the compute layer and the quantum-control interconnect, not on any evidence of instrument-specific revenue.

**Unverified.**
- "NVIDIA Ising" (named by the user): no source found; search budget exhausted.
- The 150 DGX Spark units at Thermo Fisher sites.
- A reported Hugging Face acquisition ($13B, mentioned in passing by Fortune).
- NVIDIA's healthcare or science revenue.

### 6.2 Anthropic

**Identity.** Private US AI developer (the Claude models).

**Funding.** Funding, last valuation and revenue: could not verify in this session (search budget exhausted).

**How much of its business the theme touches.**
- MHS (research preview); Claude Science (beta); a dedicated Genesis team building MCP servers and skills for DOE laboratories.
- Claude clients are named as tested in the Keysight, R&S and Lightfall integrations: Keysight's MCP documentation names Claude Code and Claude Desktop; R&S names Claude Desktop and Claude Code; Lightfall's external client is "an external Anthropic CLI agent".
- Sources: [Keysight](https://helpfiles.keysight.com/kmsic/English/keysight_mcp_for_instrument_control/Content/overview.html); [Bisinfotech](https://www.bisinfotech.com/rohde-schwarz-introduces-mxo-ai-connect-for-ai-assisted-oscilloscope-workflows/); [arXiv 2606.06711](https://arxiv.org/pdf/2606.06711).
- Theme revenue: not disclosed.

**Test (a), position.**
- Anthropic owns no judge. It owns the protocol layer (MCP, MHS) and a model.
- If MHS is open-sourced as promised, lock-in falls and value moves to model usage, which any model supplier can compete for, since MHS is "model-agnostic".
- The device knowledge (the reference file with its safety limits) is written by the vendor or the user, not by Anthropic — [The Next Web](https://thenextweb.com/news/anthropic-model-hardware-standard-mhs-eu-machinery-regulation-2027).

**Test (b), lead (outside evidence).**
- Third parties adopting its protocols: Waters joined MHS and built AI Link on MCP — [BioPharma APAC](https://biopharmaapac.com/news/97/8561/waters-partners-with-anthropic-to-advance-ai-driven-autonomous-laboratory-workflows.html). Tecan, QIAGEN, Danaher, Automata, Universal Robots, Doosan, AWS and Hugging Face are in the MHS programme — [Anthropic](https://www.anthropic.com/news/model-hardware-standard-research-preview). Keysight and R&S test with Claude clients.
- Limits: partner results are self-reported, and no conformance suite or independent security evaluation exists — [elmerdata](https://elmerdata.bearblog.dev/who-gave-the-ai-control-of-the-laboratory/); [IntuitionLabs](https://intuitionlabs.ai/articles/anthropic-hardware-standard-pharma-labs).

**Test (c), revenue model.** Subscriptions and usage-based API spending that grow with use [general model; theme revenue not disclosed]. How MHS will make money is not disclosed — [Fortune](https://fortune.com/2026/08/27/anthropic-makes-first-move-into-physical-ai-with-universal-standard-for-scientists-manufacturing/).

**Test (e), resilience.** Exposed to the financing cycle as a private AI developer. Financial strength could not be verified. Export-control exposure was not assessed in this session.

**Transitions.**
- T1: primary driver.
- T2: primary driver (MHS is aimed explicitly at "vendor lock-in").
- T3: beneficiary through usage.
- T4: beneficiary.
- T5: data stays with the customer. API inputs and outputs are deleted within 30 days, as stated via [IntuitionLabs](https://intuitionlabs.ai/articles/anthropic-hardware-standard-pharma-labs) [secondary report].

**Verdict.** The most influential protocol-setter seen in 2026 for agent control of instruments. Whether that converts into durable value capture is unproven, because the protocol is to be open and model-agnostic. It is a candidate for the top 8–15 only as "the agent and protocol layer". Its financial-strength test could not be completed.

**Unverified.** Valuation, revenue, MHS general-availability date and terms, and how the safety limits will be certified.

### 6.3 TetraScience

**Identity.** Private, Boston. A "vendor-agnostic Scientific Data Foundry", plus the agentic Tetra AI.

**Funding.** Could not verify.

**How much of its business the theme touches.** All of it: lab-instrument data and connectors, including the "Tetra Empower Agent" for Waters Empower — [TetraScience docs](https://developers.tetrascience.com/docs/waters-empower) [search snippet].

**Test (a), position.**
- It owns no judge or physical constraint. It fills the data-harmonisation gap.
- That gap is shrinking as makers ship native MCP and data access (Waters AI Link) and as MHS standardises device description.
- Its moat is the depth of its connectors and its regulated-data handling. Its status as Thermo Fisher's chosen partner is the strongest asset — [TetraScience, 12 Jan 2026](https://www.tetrascience.com/news/tetrascience-announces-collaboration-with-thermo-fisher-scientific-to-accelerate-scientific-data-and-ai-enablement-across-the-laboratory).

**Test (b), lead (outside evidence).** Thermo Fisher names TetraScience as a collaborator on its Investor Day AI slide (TetraScience appears in the deck's trademark notes) — [deck](https://s25.q4cdn.com/974941731/files/doc_downloads/Downloads/2026-Investor-Day-Presentation-Distribution.pdf). Customers are not named.

**Test (c), revenue model.** Presumed subscription software; not verified.

**Test (e), resilience.** Not assessable without financials.

**Transitions.**
- T1: neutral to positive.
- T2: negative risk. When makers open MCP natively, connector value falls.
- T3: aligned with its model.
- T4: neutral.
- T5: positive. It is a data layer for customers' own AI.

**Verdict.** It does not meet the bar for the top 8–15 on the evidence available: no judge, an unverified lead, and a gap that MCP and MHS are closing.

### 6.4 Automata

**Identity.** Private, London. LINQ: "intelligent robotics, unified scheduling software and an agile workflow design environment" — [SelectScience](https://www.selectscience.net/article/beckman-coulter-life-sciences-partners-with-automata-to-accelerate-ai-ready-laboratory-automation) [search snippet].

**Funding.**
- $45M Series C on 29 Jan 2026, led by Dimension, with Danaher Ventures (which took a board seat), Tru Arrow, Octopus Ventures and Entrepreneurs First.
- Total raised: $152M or $180M (conflicting).
- Sources: [Business Wire](https://www.businesswire.com/news/home/20260129548625/en/Automata-Raises-$45M-Series-C-to-Build-the-Operating-System-for-AI-Ready-Labs); [Dealroom](https://dealroom.co/companies/automata/) [search snippets].
- Revenue and valuation: undisclosed.

**How much of its business the theme touches.** All of it, but it is liquid-handling and bio workflows, not tuning of physics instruments.

**Test (a), position.**
- Owns physical integration (benches, scheduling) but no judge.
- Its value depends on Danaher (Beckman Coulter) instruments being integrated with it.
- It adopts open protocols (MHS partner) and NVIDIA agents ("connecting scientific agents with automated laboratory infrastructure").

**Test (b), lead (outside evidence).** Danaher's strategic investment and board seat; Beckman Coulter partnership; inclusion by both NVIDIA and Anthropic in their launches. No customer figures disclosed.

**Test (c), revenue model.** A mix of hardware systems and software; not disclosed.

**Test (e), resilience.** Venture-funded and exposed to biotech and pharma R&D capital cycles. Not otherwise assessable.

**Transitions.**
- T1: beneficiary.
- T2: beneficiary.
- T3: partial.
- T4: neutral.
- T5: neutral.

**Verdict.** Not in the top 8–15. A well-connected integrator whose strategic value accrues partly to Danaher.

### Honest view: does any software-layer company deserve a top 8–15 place?
- On the 2026 evidence, the strongest claims to the software layer belong to instrument makers that wrap their own command dictionaries, not to independent software companies:
  - Keysight, R&S and Waters: MCP servers with vendor-written command definitions and guardrails.
  - Thermo Fisher: an orchestration platform plus NVIDIA, OpenAI and TetraScience.
- Of the pure layer companies:
  - Anthropic is the only one with outside evidence of setting the standard (Waters, Tecan, QIAGEN, Danaher and others joining MHS). Its capture is uncertain because the protocol is meant to be open and model-agnostic, and its financials could not be verified.
  - NVIDIA matters as an enabler, but the theme is immaterial to its revenue.
  - TetraScience, Automata, Benchling, Opentrons, Atinary and Biosero do not show a judge, a physical constraint, or an outside-verified decisive lead.

---

## 7. Companies considered and left out

### Takeaway
Most named software-layer and autonomous-lab companies were left out of the leading group. Either they do not tune third-party instruments (they are labs, data or ELN tools, or liquid-handling robots), or their position depends on a larger maker, or this session could not obtain enough evidence.

### Cited Findings
- **Lila Sciences.** A capital-heavy lab ("AI Science Factories"), not an instrument-tuning layer. No revenue disclosed; valuation talks unconfirmed. — [Startup Fortune](https://startupfortune.com/lila-sciences-is-testing-how-much-investors-will-pay-for-automated-labs/)
- **Periodic Labs.** A materials autonomous lab with "paying customers in the semiconductor industry". Undisclosed revenue; reported round unconfirmed — [Dealroom](https://dealroom.co/news/127042-periodic-labs-eyes-7b-valuation-fivefold-jump-in-six-months/). Possibly relevant to chip metrology, but no evidence of instrument tuning.
- **XtalPi (HKEX 2228).** Drug-discovery services plus robot-lab systems sold to customers. Profit relied on non-recurring items (secondary report) — [XtalPi deck](https://ir.xtalpi.com/media/u0gcv5md/2025-annual-investor-pre-cn-final-1.pdf).
- **Benchling.** ELN, data and agents (Benchling Agents, 27 Aug 2026), with no evidence of instrument control. Valuation evidence conflicts — [Sacra](https://sacra.com/c/benchling/).
- **Opentrons.** Liquid-handling robots, more than 11,000 units; a robot vendor, not an instrument-tuning layer — [SiliconANGLE](https://siliconangle.com/?p=852385).
- **Biosero (BICO).** Small; the parent is selling assets to cut debt — [MFN, BICO release](https://mfn.se/a/bico-group/bico-has-entered-into-an-agreement-to-divest-mattek-to-sartorius-for-usd-80m).
- **Emerald Cloud Lab.** A closed ecosystem; job cuts; no 2025–2026 funding found — [arXiv 2606.03755](https://arxiv.org/html/2606.03755); [Becker's](https://beckershospitalreview.com/digital-health/digital-biotech-company-cuts-jobs-shuts-down-san-francisco-offices.html).
- **Atinary.** Small; its strategic value is tied to Bruker's minority stake — [Bruker IR](https://ir.bruker.com/press-releases/press-release-details/2026/Bruker-Announces-Strategic-Collaboration-with-Atinary-Technologies-to-Advance-Self-Driving-Laboratories/default.aspx).
- **Chemspeed and SciY.** Part of Bruker; covered under Bruker by the instrument researchers — [Bruker IR](https://ir.bruker.com/press-releases/press-release-details/2026/Chemspeed-and-SciY-Announce-SelfDriving-Laboratory-Platform-Integrating-Automation-Analytics-and-AI-Orchestration/default.aspx).
- **UniteLabs and Laboperator.** Small SiLA and OPC UA integration software vendors — [UniteLabs](https://unitelabs.io/resources/blog/end-times-fragmentation-tax-sila/).
- **Tecan, QIAGEN, Danaher, Mettler-Toledo, Hamilton.** Instrument and automation makers. Tecan, QIAGEN and Danaher are MHS participants. Mettler-Toledo appears only as an Atinary ecosystem partner. Hamilton appears only through third-party PyLabRobot support. These are for the instrument-class researchers.
- **Left out for lack of evidence in this session (search budget exhausted):**
  - Strateos, HighRes Biosolutions (beyond its Opentrons partnership), Kebotix, Telescope Innovations, Unchained Labs, Scitara, Ganymede, Dassault Systèmes BIOVIA, Sapio, Citrine, Chemify.
  - Japan: Preferred Networks/Matlantis, Epistra, the Robotic Biology Institute and Yaskawa, Shimadzu's autonomous-lab work.
  - China: DP Technology (深势科技).
  - South Korean, Taiwanese, Indian and Israeli companies.
  - Google DeepMind, OpenAI and Microsoft as instrument-specific suppliers: no instrument product verified.

### Inferences
- The list left out is long because the evidence pushes value toward instrument makers and model suppliers. That is itself a finding about the software layer.

### Gaps
- The exclusions above for lack of evidence should be revisited when search capacity is restored. Chemify, DP Technology and Preferred Networks/Matlantis are the most likely to change the picture regionally.

---

## 8. Where the evidence contradicts the thesis

### Takeaway
Five points cut against the thesis:
1. Interfaces are opening faster than "closed interfaces are the main obstacle" implies, but on vendor terms.
2. Practitioners do not treat damage risk as the binding constraint.
3. The instrument's own reading is not always an unambiguous judge in real workflows.
4. Makers are capturing the value so far, not users or software layers.
5. "Little attention" is wrong for autonomous labs, though closer to right for agent-run tuning of physics instruments.

### Cited Findings
- **Opening is fast.** Keysight (2026), R&S (30 Oct 2026) and Waters (October–November 2026) shipped MCP access, and Thermo Fisher partnered with NVIDIA (January 2026). In each case the vendor keeps the command dictionary: "It never invents a command" (Keysight); AI Link is for waters_connect customers. Sources in section 2.
- **Damage risk is not the binding constraint.** In Lightfall, hardware protection is handled by "device controllers ... and the independent hardware safety systems". The real limit is that "fault diagnosis under ambiguous conditions" and unattended trust policy are not solved — [arXiv 2606.06711](https://arxiv.org/pdf/2606.06711).
- **The judge can mislead.**
  - Tetsuwan's pipetting data were distorted by plate-edge evaporation while measurements kept looking orderly. The Genentech agent made a bubble error worse by retrying — [elmerdata](https://elmerdata.bearblog.dev/who-gave-the-ai-control-of-the-laboratory/).
  - Claude misread foaming as a software issue — [Anthropic](https://www.anthropic.com/news/model-hardware-standard-research-preview).
  - Anthropic itself says its models "still struggle with physical, chemical, and biological constraints" (paraphrased) — [IntuitionLabs](https://intuitionlabs.ai/articles/anthropic-hardware-standard-pharma-labs).
  - Implication: a fast, clean judge exists for calibration standards (SOLT, laser lock: QuEra 695 of 700), less so for complex wet workflows.
- **Value goes to makers, not users.** Agent access is bundled into vendor ecosystems at undisclosed prices. Makers present AI as a source of new instrument and consumables demand (Thermo Fisher, Waters) and are using AI to make their own field service more productive (Thermo Fisher). Sources in section 3.
- **Users push back.** A reported letter of intent from large pharma requires open APIs in procurement from 2027 [interested-party report] — [UniteLabs](https://unitelabs.io/resources/blog/end-times-fragmentation-tax-sila/). DOE builds its own MCP tools — [FedScoop](https://fedscoop.com/energy-department-demo-genesis-mission-platform-rfa-awards/).
- **Fleet matching of chip-measurement tools.** No evidence of agent-run fleet matching was found in this session's scope. Related signals:
  - Thermo Fisher's Vulcan Automated Lab claims "Integrated workflow and data connectivity between the semiconductor lab and fab" — [deck slide 43](https://s25.q4cdn.com/974941731/files/doc_downloads/Downloads/2026-Investor-Day-Presentation-Distribution.pdf).
  - Periodic Labs has unspecified semiconductor customers.
- **Attention is high.** Billions in capital and many big-company launches (section 5). For physics instruments, the work is mostly in national laboratories (LBNL's ALS: Osprey and Lightfall; NSLS-II: Bluesky), which fits "little commercial attention" for that niche.

### Inferences
- The thesis holds best for calibration against a known standard in electronic test and laser and quantum systems, where the judge is fast and unambiguous and the first agent products have shipped.
- It holds least for complex wet-lab workflows, where the judge can be fooled.
- The "who captures value" answer for 2026 is the maker, unless users force openness through procurement or build their own stacks.

### Gaps
- Evidence from chip fabs, electron-microscope users and quantum-computing operators on building their own agents is thin in this note and should come from the instrument-class researchers.

---

## 9. What could not be verified

### Takeaway
Many specific items could not be verified because the session's shared web-search budget ran out after about 33 searches. Each item below names what was tried.

### Cited Findings
None. This section lists gaps only.

### Inferences
- The regional picture (Japan, Taiwan, India, Israel) and vendors' data-term picture are the weakest parts of this note.

### Gaps
- **NVIDIA "Ising"** (named by the user): not found. A search was blocked by the budget, and the NVQLink release names no AI calibration model.
- **150 DGX Spark units at Thermo Fisher**: only one aggregator (rallies.ai) reports it.
- **Thermo Fisher "fully autonomous instruments" in H2 2026**: only a secondary quote (TIKR). The phrase is not in the deck text, and no launch release was found.
- **Waters AI Link general availability in November 2026**: the plan is stated; actual GA not confirmed as of 12 Nov 2026.
- **Keysight MCP server**: release date and licence or price not stated in its documentation. Same for R&S MXO AI Connect pricing.
- **MHS**: specification, licence, conformance suite and open-source date not public.
- **Valuations and funding**: Anthropic, OpenAI, TetraScience, Scitara, Ganymede, Sapio, Citrine, Chemify, Kebotix, Strateos, HighRes, Hamilton, Unchained Labs, Telescope Innovations, Preferred Networks/Matlantis, Epistra, DP Technology. A Chinese-language search on DP Technology returned nothing relevant.
- **Benchling**: the S-1 filing claim (12 May 2026) and the $0.9B secondary-market estimate.
- **Lila and Periodic**: whether the 2026 rounds closed.
- **Pharma letter of intent**: the primary text (Roche, Bayer, Takeda and others) was not found; only the UniteLabs account.
- **Google DeepMind's UK automated lab; OpenAI for Science details; Microsoft Discovery**: searches blocked.
- **Government programmes**: NSF, NIH, EU RAISE, UK, Taiwan, India and Israel; Korea's autonomous-lab council and KRW 13.5bn line (blog-only).
- **Genesis**: the consortium figure of more than $800M from 40 organisations, and whether the challenge list expanded from 26 to 33.
- **Standards**: SECS/GEM and SEMI EDA adoption and any agent use; Tango; IVI Foundation activity; SiLA 2 vendor counts.
- **Vendor cloud data terms**: Thermo Fisher Connect and Ardia, waters_connect, ZEISS arivis Cloud, Bruker SciY, Agilent.
- **Earnings-call quotes on interface openness**: Thermo Fisher Q3 2026, Danaher, Agilent, Waters, Bruker, Mettler-Toledo, Keysight, KLA, Zeiss, JEOL, Shimadzu, Hitachi. Not obtained beyond the Thermo Fisher Investor Day deck and the Q1 call coverage.
- **XtalPi**: the 锦缎研究院 analysis was seen only in a search summary.

---

## 10. Sources with dates

### Takeaway
Primary sources dominate for the central claims: NVIDIA newsroom, Anthropic, DOE and the Office of Science, Thermo Fisher's Investor Day deck, Bruker IR, Keysight documentation, the XtalPi IR deck, and arXiv papers. Trade press and aggregators are labelled where used.

### Cited Findings

**Primary and company sources**
- Anthropic, "Previewing the Model Hardware Standard", 27 Aug 2026 — https://www.anthropic.com/news/model-hardware-standard-research-preview
- NVIDIA, Q2 FY2027 results (quarter ended 26 Jul 2026), August 2026 — https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
- NVIDIA, NVQLink release, 28 Oct 2025 — https://nvidianews.nvidia.com/news/nvidia-nvqlink-quantum-gpu-computing
- NVIDIA, GTC Berlin healthcare and life sciences release, 21 Oct 2026 — https://nvidianews.nvidia.com/news/healthcare-and-life-sciences-leaders-build-on-nvidia-to-advance-drug-discovery-and-expand-patient-care
- NVIDIA ISC 2026 scientific software release (syndicated), 24 Jun 2026 — https://usa-automation.net/news/112167-nvidia-introduces-ai-software-libraries-for-scientific-research
- NVIDIA blog, ALS Accelerator Assistant, 8 Jan 2026 — https://blogs.nvidia.com/blog/ai-copilot-berkeley-x-ray-particle-accelerator
- Thermo Fisher and NVIDIA, Business Wire, 12 Jan 2026 — https://www.businesswire.com/news/home/20260112999582/en/
- Thermo Fisher and OpenAI, IR release, 16 Oct 2025 — https://ir.thermofisher.com/investors/news-events/news/news-details/2025/Thermo-Fisher-Scientific-to-Accelerate-Life-Science-Breakthroughs-with-OpenAI/default.aspx
- Thermo Fisher 2026 Investor Day presentation, 20 May 2026 — https://s25.q4cdn.com/974941731/files/doc_downloads/Downloads/2026-Investor-Day-Presentation-Distribution.pdf
- Thermo Fisher "AI ecosystem" story, January 2026 — https://corporate.thermofisher.com/us/en/index/newsroom/Our-stories/AI-ecosystem.html
- Thermo Fisher AutoScript TEM catalogue (undated) — https://www.thermofisher.com/order/catalog/product/AUTOSCRIPT-TEM ; AutoScript 4 datasheet — https://assets.thermofisher.com/TFS-Assets/MSD/Datasheets/autoscript-4-datasheet.pdf
- Thermo Fisher Vulcan Automated Lab, 18 Mar 2025 — https://www.businesswire.com/news/home/20250318064982/en/Thermo-Fisher-Scientific-Introduces-the-Vulcan-Automated-Lab-to-Transform-Semiconductor-Analysis
- TetraScience and Thermo Fisher, 12 Jan 2026 — https://www.tetrascience.com/news/tetrascience-announces-collaboration-with-thermo-fisher-scientific-to-accelerate-scientific-data-and-ai-enablement-across-the-laboratory
- Bruker and Atinary, 11 Aug 2026 — https://ir.bruker.com/press-releases/press-release-details/2026/Bruker-Announces-Strategic-Collaboration-with-Atinary-Technologies-to-Advance-Self-Driving-Laboratories/default.aspx
- Chemspeed and SciY self-driving lab platform, 9 Feb 2026 — https://ir.bruker.com/press-releases/press-release-details/2026/Chemspeed-and-SciY-Announce-SelfDriving-Laboratory-Platform-Integrating-Automation-Analytics-and-AI-Orchestration/default.aspx
- Keysight MCP Server for Instrument Control: overview and getting started (© 2026) — https://helpfiles.keysight.com/kmsic/English/keysight_mcp_for_instrument_control/Content/overview.html ; https://helpfiles.keysight.com/kmsic/English/keysight_mcp_for_instrument_control/Content/getting-started.html
- Keysight ADS 2027 agentic AI, 6 Oct 2026 — https://www.hpcwire.com/aiwire/2026/10/06/keysight-advances-its-design-software-with-agentic-ai/
- Rohde & Schwarz MXO AI Connect, 30 Oct 2026 — https://www.bisinfotech.com/rohde-schwarz-introduces-mxo-ai-connect-for-ai-assisted-oscilloscope-workflows/ ; R&S AI Workplace — https://www.rohde-schwarz.com/au/_258801.html
- Waters AI Link and MHS, about 13–15 Oct 2026 — https://biopharmaapac.com/news/97/8561/waters-partners-with-anthropic-to-advance-ai-driven-autonomous-laboratory-workflows.html ; https://www.webull.com/news/15740820817863680 ; waters_connect API page — https://www.waters.com/nextgen/no/en/products/informatics-and-software/waters_connect/waters-connect-api.html
- Agilent GC Assist, 26 May 2026 — https://www.investor.agilent.com/news-and-events/news/news-details/2026/Agilent-Launches-New-GC-Systems-with-GC-Assist-to-Improve-Laboratory-Efficiency-and-Data-Quality/default.aspx ; OpenLab Sync, 28 May 2026 — https://www.businesswire.com/news/home/20260528098940/en/ ; SLAS2026, 4 Feb 2026 — https://www.businesswire.com/news/home/20260204034151/en/ ; eSight AI module, 1 Jul 2026 — https://www.investor.agilent.com/news-and-events/news/news-details/2026/Agilent-Launches-AI-Driven-Analysis-Module-for-Agilent-xCELLigence-RTCA-eSight/default.aspx
- Automata Series C, 29 Jan 2026 — https://www.businesswire.com/news/home/20260129548625/en/Automata-Raises-$45M-Series-C-to-Build-the-Operating-System-for-AI-Ready-Labs
- XtalPi 2025 annual investor presentation (2026) — https://ir.xtalpi.com/media/u0gcv5md/2025-annual-investor-pre-cn-final-1.pdf
- BICO divestment of MatTek, April 2025 — https://mfn.se/a/bico-group/bico-has-entered-into-an-agreement-to-divest-mattek-to-sartorius-for-usd-80m ; Biosero acquisition, 2021 — https://biosero.com/news-and-media/bico-completes-the-acquisition-of-biosero/
- UniteLabs blog (interested party), 21 Jul 2026 — https://unitelabs.io/resources/blog/end-times-fragmentation-tax-sila/

**Government**
- DOE Office of Science SCAC slides, "The Genesis Mission Has Launched", 27 Mar 2026 — https://science.osti.gov/-/media/About/pdf/scac/meetings/2026/DOE-Genesis-Mission-Launched---2026-03-27.pdf
- DOE, first Genesis projects selected, 22 Jul 2026 — https://www.energy.gov/articles/secretary-energy-chris-wright-announces-first-genesis-mission-projects-selected-accelerate
- Xinhua, State Council AI+ opinion, 28 Aug 2025 — https://www.news.cn/tech/20250828/5af2930138044797909cf407e7ba119b/c.html
- NCSTI, Beijing AI-for-research plan, 2 Jul 2026 (fetch failed; search snippet) — https://www.ncsti.gov.cn/zcfg/zcjd/202607/t20260702_250678.html
- Beijing Daily, 2026 Science Intelligence Conference cases, 21 Aug 2026 — https://news.bjd.com.cn/2026/08/21/11926168.shtml
- MEXT smart cloud lab document, 21 Feb 2026 — https://www.mext.go.jp/content/20260221-mxt_nanozai-000046621_8.pdf ; Newswitch on the FY2027 AI4S request — https://newswitch.jp/p/50165
- Herald Economy, Korea MSIT bio autonomous lab, 11 Jun 2026 — https://www.heraldk.com/article/2026061118413174490 ; Dong-A Science via Daum, AI materials autonomous labs, 30 Apr 2026 — https://v.daum.net/v/20260430101533808 ; K-Moonshot strategy PDF, March 2026 — https://smartcity.go.kr/wp-content/uploads/2026/03/안건4AI시대과학기술경쟁력대도약을위한K-문샷추진전략안.pdf

**Papers and preprints**
- LAP: An Agent-to-Instrument Protocol for Autonomous Science (Shiyanjia Lab), arXiv 2606.03755, 2 Jun 2026 — https://arxiv.org/html/2606.03755
- Lightfall: An API-first, LLM-addressable control platform for synchrotron beamlines (LBNL), arXiv 2606.06711, 4 Jun 2026 — https://arxiv.org/pdf/2606.06711
- NIMO MCP self-driving-lab orchestrator, arXiv 2605.15227, May 2026 — https://arxiv.org/html/2605.15227
- J. Synchrotron Rad. 2026, ALS beamline 5.3.1 agent orchestration (search snippet) — https://journals.iucr.org/s/issues/2026/05/00/soo5005/index.html ; HANBIT — https://journals.iucr.org/s/issues/2026/05/00/ok5168/

**Press, analysts and aggregators (secondary)**
- Fortune, 27 Aug 2026 (MHS) — https://fortune.com/2026/08/27/anthropic-makes-first-move-into-physical-ai-with-universal-standard-for-scientists-manufacturing/
- The Next Web (MHS and EU Machinery Regulation), August 2026 — https://thenextweb.com/news/anthropic-model-hardware-standard-mhs-eu-machinery-regulation-2027
- noze, 29 Aug 2026 — https://www.noze.it/en/insights/model-hardware-standard-agents-lab-instruments/
- elmerdata (Elmer Yglesias), 30 Aug 2026 — https://elmerdata.bearblog.dev/who-gave-the-ai-control-of-the-laboratory/
- IntuitionLabs (Adrien Laurent), 19 Sep 2026 — https://intuitionlabs.ai/articles/anthropic-hardware-standard-pharma-labs
- Campus Technology, 1 Jul 2026 — https://campustechnology.com/articles/2026/07/01/anthropic-nvidia-move-ai-agents-deeper-into-scientific-workflows.aspx ; The Next Web on Claude Science, 30 Jun 2026 — https://thenextweb.com/news/anthropic-claude-science-ai-workbench-scientists
- TIKR on Thermo Fisher Investor Day (20 May 2026) — https://www.tikr.com/blog/what-thermo-fisher-ceo-said-at-investor-day-that-the-market-is-still-processing
- Lab Manager on the Thermo Fisher Q1 2026 call (23 Apr 2026) — https://www.labmanager.com/thermo-fisher-kicks-off-2026-with-new-instruments-ai-push-and-a-warning-on-rising-lab-costs-35274
- Fierce Biotech on Thermo Fisher with NVIDIA and TetraScience, January 2026 — https://www.fiercebiotech.com/medtech/thermo-fisher-scientific-teams-nvidia-tetrascience-next-gen-ai-workflow-projects
- FedScoop, Genesis demo, 22 Jul 2026 — https://fedscoop.com/energy-department-demo-genesis-mission-platform-rfa-awards/
- TechInformed, DOE and 24 organisations, 24 Dec 2025 — https://techinformed.com/doe-and-24-organizations-sign-ai-collaboration-deal/
- ABI Research, NVIDIA physical AI, 8 Apr 2026 — https://www.abiresearch.com/market-research/insight/7787716-platform-progress-commercial-patience-nvid?hsLang=en
- SiliconANGLE, Opentrons Series E, 29 Oct 2026 — https://siliconangle.com/?p=852385
- Startup Fortune, Lila, 3 Jun 2026 — https://startupfortune.com/lila-sciences-is-testing-how-much-investors-will-pay-for-automated-labs/ ; Yahoo/Reuters, Lila extension (October 2025) — https://finance.yahoo.com/news/exclusive-ai-lab-lila-sciences-101645837.html ; Bloomberg Law, Lila talks (June 2026) — https://news.bloomberglaw.com/private-equity/lila-sciences-said-in-talks-for-funds-at-8-5-billion-valuation
- Dealroom, Periodic Labs, 26 Mar 2026 — https://dealroom.co/news/127042-periodic-labs-eyes-7b-valuation-fivefold-jump-in-six-months/ ; Dealroom, Automata profile — https://dealroom.co/companies/automata/
- Sacra, Benchling — https://sacra.com/c/benchling/ ; TrueUp, Benchling — https://api.trueup.io/co/benchling
- Becker's, Emerald Cloud Lab job cuts (date unclear) — https://beckershospitalreview.com/digital-health/digital-biotech-company-cuts-jobs-shuts-down-san-francisco-offices.html
- SLAS, OPC UA LADS — https://www.slas.org/resources/standards/opc-ua-lads ; SPECTARIS, LADS — https://www.spectaris.de/en/association/thespectarisindustries/networked-laboratory-equipment
- Electronic Design, NI Nigel and LabVIEW 2026 — https://www.electronicdesign.com/technologies/embedded/machine-learning/video/55396195/electronic-design-whats-new-with-nigel-and-labview-2026
- Open-source MCP servers (PyPI and Glama pages, 2026): https://pypi.org/project/instrmcp/ ; https://glama.ai/mcp/servers/di-omics/plr-mcp ; https://pypi.org/project/labmcp/ ; https://pypi.org/project/labwire-mcp/0.5.0/ ; https://pypi.org/project/teasel-server/
- Huanqiu and Huxiu on XtalPi FY2025 (March 2026) — https://m.huanqiu.com/article/4QuAKm3FeNr ; https://m.huxiu.com/article/4845830.html

### Inferences
- Figures that rest only on secondary or snippet sources carry the labels shown in the sections above. They should not be promoted to confirmed status in the final report without a primary check: Lila and Periodic round sizes, Benchling's valuation, Thermo Fisher's H2 2026 autonomy timing, and the pharma letter of intent.

### Gaps
- See section 9.
