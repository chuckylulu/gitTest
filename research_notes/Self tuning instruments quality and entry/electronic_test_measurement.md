# Electronic test and measurement: self-tuning instruments (as of 12 November 2026)

Scope: electronic test and measurement (T&M) in which set-up, calibration and operation could be run by software or AI agents. Quality evidence only; no share prices, multiples or recommendations. Listed-company financial statements are covered by another researcher; China/Korea/Taiwan/India companies are covered in depth by a regional researcher. Segment-level facts are recorded here.

Evidence labels: [primary] = company filing or official release read directly; [independently confirmed: by whom]; [company claim, not independently confirmed]; [secondary report] = trade press, broker note, aggregator or search-engine summary; "could not verify" = tried and failed (reason given). Arithmetic marked "(my arithmetic)" is derived from cited figures.

Method note (important for the report writer): about 35 web searches and about 45 page fetches were made. The shared web-search budget for this turn ran out part-way through. After that, only URLs already surfaced by earlier searches were fetched; no new search-engine queries were made. As a result, the following were NOT researched in this session and carry no verified facts here: Chroma ATE, Good Will Instrument, Yokogawa, Hioki, Kikusui, Iwatsu, Advantest, Teradyne, EXFO, Ceyear, Uni-Trend, Pico Technology, Signal Hound, Tabor Electronics, Scientech, Aplab, and Emerson's T&M segment figures. Coverage of South Korea, Taiwan, India and Israel is therefore nil, and Japan is covered only through Anritsu. A follow-up session with a fresh search budget is needed for those.

---

## (1) Segment map

### Takeaway
Electronic T&M is a concentrated, mostly hardware-led market led by Keysight, Rohde & Schwarz, Tektronix (Ralliant), Anritsu and NI (Emerson), with Chinese makers (Rigol, Siglent) gaining share in their home market and moving into high-end products. The 2025-26 demand cycle is driven by AI data-centre interconnect (800G/1.6T optics, high-speed digital, data-centre power) and defence. Mobile/wireless is flat. Consolidation continued: Keysight bought Spirent and sold parts of it to Viavi, and Anritsu bought DEWETRON.

### Cited findings
**Market size and ranking (third party, commissioned for an IPO prospectus)**
- Frost & Sullivan figures in Rigol's Hong Kong prospectus (dated 30 Jun 2026) put the global electronic T&M instrument market at RMB 57.1bn in 2024, with an estimated 5.0% CAGR for 2025-2029 [secondary report of prospectus] — [itiger/gmt8 summaries via search](https://www.itiger.com/news/1102640746). Another report of the same IPO says the global "measurement instruments and solutions" market was above RMB 110bn in 2025, with a 9.6% CAGR for 2026-2030 to about RMB 180bn [secondary report; the definition is wider, so the two figures conflict] — [QQ News, 30 Jun 2026](https://news.qq.com/rain/a/20260630A01Y5600).
- Frost & Sullivan (2025 revenue) ranks Rigol 8th in the world in electronic measurement instruments and 1st among PRC providers. It ranks Rigol 5th globally (1st in China) in digital oscilloscopes and 3rd globally (1st in China) in waveform generators [third-party data commissioned by the company; reported in a company-issued release] — [ACN Newswire, 13 Jul 2026](https://www.financialcontent.com/article/acnnewswire-2026-7-13-ai-computing-optical-communication-pcb-resonance-rigol-debuts-on-hkex-ushering-in-a-new-ah-era). Rigol's global share is about 1.2% (2025) and 1.1% (2024). One source gives Rigol 1.9% of the China market and 6th place there, which sits awkwardly with "largest PRC provider": the likely reading is 6th including foreign brands [secondary report; conflict noted] — [itiger summary](https://www.itiger.com/news/1102640746).
- Category-level market shares (oscilloscopes, spectrum/network analysers, signal generators, protocol test, PXI) for Keysight, R&S, Tektronix, Anritsu or NI: **could not verify.** No independent share table was found before the search budget ran out. The prospectus "Industry Overview" chapter on HKEXnews is the place to look.

**Who is who (identity facts verified in this session)**
| Company | Home; listing or owner | Main T&M lines (verified in this session) | Latest size datapoint |
|---|---|---|---|
| Keysight | US; NYSE KEYS | Signal/network analysers, signal generators, oscilloscopes (Infiniium UXR/MXR/EXR), BERT (M8000), wireless test (UXM), power, semiconductor characterisation (B1500/B2900), PXIe VXT, network test and assurance (ex-Spirent), RF EDA (ADS, Nexus) — [KMSIC supported instruments](https://helpfiles.keysight.com/kmsic/English/keysight_mcp_for_instrument_control/Content/supported-instruments.html) | FY2025 (to 31 Oct 2025) revenue $5,375M [primary] — [2025 Annual Report](https://s22.q4cdn.com/444849635/files/doc_financials/2025/ar/2025-Annual-Report.pdf) |
| Rohde & Schwarz | Germany; "privately owned company" | Divisions: Test & Measurement, Aerospace & Defense, Critical Infrastructure & Networks; parent of Zurich Instruments — [R&S release 28 Nov 2025](https://www.rohde-schwarz.com/us/about/news-press/all-news/rohde-schwarz-shows-resilience-in-a-challenging-environment-revenue-exceeds-three-billion-euros-for-the-first-time_229356-1598656.html); [ZQCS release](https://www.zhinst.com/de/news/zurich-instruments-launches-zqcs-quantum-control-system-master-long-lived-logical-qubit/) | FY2025/26 (Jul 2025-Jun 2026) net revenue EUR 3.6bn [primary boilerplate] — [R&S release 27 Oct 2026](https://www.rohde-schwarz.com/jp/_229356-1706630.html) |
| Anritsu | Japan; TSE 6754 | T&M (comms and optical transceiver test, service assurance), PQA, Environmental Measurement (incl. DEWETRON GmbH, newly consolidated) — [tanshin 27 Apr 2026](https://dl.cdn-anritsu.com/en-en/about-anritsu/ir/financial-materials/fy2025/260427-01e.pdf) | FY2025 (to 31 Mar 2026) revenue JPY 117,462M; T&M JPY 68,774M [primary] |
| Ralliant (Tektronix) | US; NYSE RAL; separated from Fortive in 2025 [secondary report of 8-K] | T&M segment; Sensors & Safety Systems — [8-K Q3 2026](https://www.sec.gov/Archives/edgar/data/0002041385/000204138526000070/ralq32026-ex991.htm) | Q3 2026 T&M revenue $244.2M [primary] |
| Teledyne (LeCroy) | US; NYSE TDY | Electronic T&M inside the Instrumentation segment — [8-K Q3 2026](https://www.sec.gov/Archives/edgar/data/0001094285/000109428526000055/q3-2026earningsrelease.htm) | Q3 2026 Instrumentation $370.5M; electronic T&M not broken out [primary] |
| Viavi | US; Nasdaq VIAV | Network & Service Enablement, incl. ex-Spirent high-speed Ethernet, network security and channel emulation lines — [Q1 FY27 release](https://finviz.com/news/415958/viavi-announces-first-quarter-fiscal-2027-results) | Q1 FY2027 (to 3 Oct 2026) NSE $376.1M [primary] |
| NI | US; part of Emerson (NYSE EMR) | LabVIEW+ Suite, TestStand, FlexLogger, InstrumentStudio, SystemLink, PXI/modular hardware — [NI Connect release 13 May 2026](https://www.emerson.com/is/content/emerson/ni-connect-2026-dotcom-release-final) | Segment revenue: could not verify |
| Rigol 普源精电 | China; SSE STAR 688337 + HKEX 00537 (H shares listed 9 Jul 2026) | Digital oscilloscopes, waveform generators, RF (incl. VNA), DC precision, modular, "solutions" — [ACN Newswire](https://www.financialcontent.com/article/acnnewswire-2026-7-13-ai-computing-optical-communication-pcb-resonance-rigol-debuts-on-hkex-ushering-in-a-new-ah-era) | 2025 revenue RMB 900M [secondary: broker table] — [Huaan Securities 28 Oct 2026](https://pdf.dfcfw.com/pdf/H3_AP202610301831252523_1.pdf) |
| Siglent 鼎阳科技 | China; SSE STAR 688112 | Oscilloscopes (incl. high-resolution), VNA (SNA6000A), source meters (SMM3000X), power supplies (SPD4000X) — [Q3 2026 report](https://static.cninfo.com.cn/finalpage/2026-10-27/1225626059.PDF) | 9M 2026 revenue RMB 573.3M [primary] |
| Liquid Instruments | Australia (ANU spin-out); private | FPGA-based, software-defined Moku instruments — [SiliconANGLE 28 Apr 2026](https://siliconangle.com/?p=741861) | Revenue not disclosed |
| Spirent | UK; acquired by Keysight 15 Oct 2025 for $1,564M; high-speed Ethernet, network security and channel emulation lines sold to Viavi for $399M on 16 Oct 2025 [primary] — [Keysight 2025 AR](https://s22.q4cdn.com/444849635/files/doc_financials/2025/ar/2025-Annual-Report.pdf) | — | — |

**Cycle signals by end market (2025-26)**
- AI data centre and wireline:
  - Keysight's commercial communications revenue grew 56% to $1,006M in Q3 FY2026 (quarter to 31 Jul 2026) [primary] — [Keysight 8-K](https://www.sec.gov/Archives/edgar/data/0001601046/000160104626000029/exhibit991-q326pressrelease.htm).
  - Anritsu says "Orders exceeded our expectations due to strong data center-related demand" and that it has orders for both 800GE and 1.6TE products, with 800GE still the larger share [primary] — [Anritsu Q1 FY2026 Q&A](https://dl.cdn-anritsu.com/en-en/about-anritsu/ir/financial-materials/fy2026/260731-01e.pdf).
  - Siglent's combined VNA, source-meter and power-supply revenue rose 507.03% YoY in Q3 2026. The company attributes this to test demand from high-speed communication data-centre build-out [primary] — [Siglent Q3 2026](https://static.cninfo.com.cn/finalpage/2026-10-27/1225626059.PDF).
  - Revenue from Rigol's optical-communication customers rose 70.45% in 2025 and 147.71% in Q1 2026 [company claim] — [ACN Newswire](https://www.financialcontent.com/article/acnnewswire-2026-7-13-ai-computing-optical-communication-pcb-resonance-rigol-debuts-on-hkex-ushering-in-a-new-ah-era).
- Mobile: Anritsu expects the mobile market "to remain weak and largely flat", with a pick-up before pre-6G services around the 2028 Los Angeles Olympics [primary] — [Anritsu Q1 FY2026 Q&A](https://dl.cdn-anritsu.com/en-en/about-anritsu/ir/financial-materials/fy2026/260731-01e.pdf).
- Defence:
  - Keysight's aerospace, defence and government revenue was $339M in Q3 FY2026, up 14% [primary].
  - Ralliant says that in defence "orders outpaced shipments" [secondary: transcript] — [TradingKey transcript, 4 Nov 2026](https://www.tradingkey.com/news/transcripts/262275228-).
  - R&S had a record order backlog above EUR 5bn (FY2024/25) [primary].
- Semiconductors:
  - Ralliant's semiconductor revenue fell 7% in Q3 2026 against a large customer project in Q3 2025; it grew in the high teens excluding that project [secondary: transcript].
  - Keysight's EISG grew 21% in Q3 FY2026 [primary].
- Teledyne is the outlier: "electronic test and measurement instrumentation sales decreased $4.8 million" in Q3 2026 [primary] — [Teledyne 8-K](https://www.sec.gov/Archives/edgar/data/0001094285/000109428526000055/q3-2026earningsrelease.htm).

**Automated test equipment for chips (summary level only):** Advantest and Teradyne were not researched in this session (search budget). No verified facts.

### Inferences
- The top tier is US/European/Japanese. The Chinese makers are still small globally (Rigol is about 1.2% of the world market and 8th) but are scaling high-end lines and their data-centre exposure. Even inside China, Rigol's roughly 1.9% share suggests foreign brands still hold most of the market [inference from secondary F&S data].
- The current cycle rewards measurement hardware at new speed nodes: 800G and 1.6T, 12-bit oscilloscopes for AI server PCBs, and high-voltage data-centre power test. This is not a cycle in which software layers capture most of the value (see section 5).

### Gaps
- No independent category share data (e.g. oscilloscopes by vendor). Not found before the search budget ran out.
- No verified segment data for NI/Emerson, Yokogawa, Chroma ATE, Hioki, Kikusui, Iwatsu, Good Will, Ceyear or Uni-Trend.

---

## (2) What is already open and automated versus what is new

### Takeaway
The control layer in electronic T&M has been open for decades: SCPI over VISA (GPIB, USB, LAN/HiSLIP/VXI-11), IVI drivers and vendor Python packages. Agents could therefore be bolted on quickly, and they were. Between July 2025 and October 2026 the main vendors shipped:
- chat and code assistants (NI Nigel);
- local MCP servers that execute SCPI on instruments (Keysight, May 2026 [secondary date]; R&S MXO AI Connect, 29 Oct 2026);
- AI-generated FPGA instruments (Liquid Instruments GenInst Studio, 14 Jul 2026);
- MCP servers for RF design software (Keysight ADS/Nexus, 6 Oct 2026).

Community MCP servers exist for Rigol, Siglent, Keysight, Owon, PicoScope and Digilent hardware. None of the vendor products claims autonomous, unattended closing of the loop on instrument readings. All of them keep a human approving actions, or leave that to the AI client. The vendor MCP servers are free (R&S) or carry no stated price (Keysight). So far, value is not being charged for at the agent layer.

### Cited findings
**What was already open**
- IVI Generation 2026 (document dated 15 Apr 2025):
  - The IVI Foundation "updated its driver specifications to provide a simpler version of the standards and add support for Microsoft .NET 6+".
  - It split the requirements into a language-agnostic IVI Driver Core and language-specific specifications.
  - It moved the specifications to GitHub in markdown, which "enhances the open nature of the specifications".
  - It says nothing about AI, agents or MCP [primary] — [IVI 2026](https://www.ivifoundation.org/downloads/IVI%20Generations/IVI%202026.pdf).
  - An IVI ANSI-C specification was completed in Feb 2026 [secondary: page title only, not opened] — [IVI news 17 Feb 2026](https://ivifoundation.org/2026/02/17/AnsiCComplete.html).
  - No IVI Foundation initiative on AI agents or MCP was found [searched 12 Nov 2026].
- Cross-vendor VISA interoperability is a fact:
  - Keysight's MCP server connects through "Keysight IO Libraries Suite 2026 or later, National Instruments VISA, or Rohde & Schwarz VISA"; LAN instruments need no VISA [primary] — [KMSIC getting started](https://helpfiles.keysight.com/kmsic/English/keysight_mcp_for_instrument_control/Content/getting-started.html).
  - R&S's server uses "standard VISA connections (HiSLIP, VXI-11, or TCP/IP)" [primary] — [R&S release 29 Oct 2026](https://www.rohde-schwarz.com/jp/about-us/news-press/all-news/rohde-schwarz-introduces-mxo-ai-connect-for-ai-assisted-oscilloscope-workflows_229356-1709313.html).
- Tektronix publishes tm_devices, an open-source (Apache-2.0) Python driver package built on PyVISA [secondary: PyPI/GitHub listing via search] — [github.com/tektronix/tm_devices](https://www.github.com/tektronix/tm_devices).

**What is new (2024-2026): shipped products**

Types: A = chat/code assistant; B = agent tool that executes on the instrument with human approval; C = claims to close the loop on instrument readings.

| Product | Vendor | Date | Type | What it does (evidence) |
|---|---|---|---|---|
| Nigel AI Advisor | NI/Emerson | Launched 22 Jul 2025 in LabVIEW and TestStand 2025 Q3 (tech preview late 2024) | A | Analyses code, answers questions, "Built on state-of-the-art large language models" [primary] — [Emerson 22 Jul 2025](https://www.emerson.com/en/corporate/news/2025/07-emerson-expands-ai-capabilities-into-test-and-measurement-software-portfolio); [Emerson blog 4 Sep 2026](https://www.emersonautomationexperts.com/2026/test-measurement/how-nigel-ai-accelerates-labview-suite-development/) |
| Nigel code and sequence generation | NI/Emerson | Announced 13 May 2026 ("later in 2026"); available per 4 Sep 2026 blog | A | "Nigel now generates LabVIEW code from a prompt, producing runnable programs (VIs)". Imports a specification to build TestStand sequences. "Can see connected hardware". The blog does not say it executes on hardware or reads measurements. "Agentic capabilities" are coming "soon" [primary] |
| Keysight MCP Server for Instrument Control (KMSIC) | Keysight | v0.1 released May 2026 [secondary report; no date on vendor pages] | B | SCPI commands drawn from Keysight instrument definition files: "The AI doesn't invent the commands". "Nothing runs without approval". Audit trail; runs locally. Includes procedures such as SOLT calibration (1-port only; "2-port SOLT is not yet available") and power-supply set-up [primary] — [product page](https://www.keysight.com/find/kmsic); [release notes](https://helpfiles.keysight.com/kmsic/English/keysight_mcp_for_instrument_control/Content/release-notes.html); [overview](https://helpfiles.keysight.com/kmsic/English/keysight_mcp_for_instrument_control/Content/overview.html) |
| ADS 2027 / Nexus MCP servers | Keysight | Announced 6 Oct 2026 | B in simulation only | Agents run Python in ADS, modify projects, run simulations and read results. "The ADS MCP server contains no language model". Nexus uses token licensing. No link to lab instruments [secondary report] — [Wevolver](https://www.wevolver.com/article/keysight-mcp-servers-ai-agents-rf-design); [HPCwire 6 Oct 2026](https://www.hpcwire.com/aiwire/2026/10/06/keysight-advances-its-design-software-with-agentic-ai/) |
| MXO AI Connect | Rohde & Schwarz | 29 Oct 2026 (shown at electronica, 10-13 Nov 2026) | B, with a C claim | Local MCP server for MXO 3/4/5/5C and ScopeStudio. Clients: Cursor, Claude Desktop, Claude Code, GitHub Copilot. "Retrieve measurement results". Claim: "AI agents can coordinate instrument control and analysis, making repeated setup and code adjustments until the measurement goal is reached" [company claim]. "Available free of charge... No license key is required" [primary] — [release](https://www.rohde-schwarz.com/jp/about-us/news-press/all-news/rohde-schwarz-introduces-mxo-ai-connect-for-ai-assisted-oscilloscope-workflows_229356-1709313.html); [product page](https://www.rohde-schwarz.com/au/_258817.html) |
| GenInst Studio | Liquid Instruments | 14 Jul 2026 | AI-generated instrument (T4) | Natural-language request becomes a "validated, application-specific instrument" on Moku FPGA hardware through an "agentic AI workflow". No claim of tuning against measurements [secondary report] — [SiliconANGLE 14 Jul 2026](https://siliconangle.com/?p=788048) |
| LabOne Q on ZQCS | Zurich Instruments (R&S) | ZQCS launched 9 Mar 2026 | Automated calibration (quantum control) | ZQCS is "powered by LabOne Q, which provides automation for calibration and tune-up"; no AI claim [primary] — [ZI release](https://www.zhinst.com/de/news/zurich-instruments-launches-zqcs-quantum-control-system-master-long-lived-logical-qubit/) |
| Community MCP servers | Third parties | 2025-26 | B | rigol-mcp (DS1000Z; pyvisa-py), a Rigol DHO824 MCP (PyVISA), pyMSO5000 (Rigol MSO5000), labmcp-scpi (generic IEEE 488.2/SCPI over PyVISA; the agent writes raw SCPI), keyscope-mcp (Keysight EDUX1052G), ScopeMCP (Owon), oscilloscope-mcp, siglent-sds-mcp / siglent-sdg-mcp, picoscope_mcp, TekAutomate MCP (uses tm_devices; the listing claims a 40/40 benchmark pass on 18 Mar 2026), an MCP server for Digilent Analog Discovery [secondary: directory listings, not checked on GitHub] — [glama.ai](https://glama.ai/mcp/servers/armchairdeity/mcp-server-scpi); [socket.dev labmcp-scpi](https://socket.dev/pypi/package/labmcp-scpi); [lobehub siglent-sds-mcp](https://lobehub.com/fr/mcp/magnusjohansson-siglent-sds-mcp); [Altium](https://resources.altium.com/p/building-mcp-server-analog-discovery) |

**Closing the loop: independent user evidence**
- A Microsoft Tech Community post (11 Sep 2026) describes GitHub Copilot driving a Rigol DHO814 through the open-source rigol-mcp server [independent user report, not a vendor]:
  - The agent configures the scope, captures and measures, and compares measured values with expected ones.
  - "Invalid readings prompt investigation, not invented results"; a human reviews each step.
  - Limits noted by the author: "Not all 897 catalog query/write forms have been hardware-tested", "An assistant cannot check your physical wiring for you", "Meter tool use is not a calibration certificate".
  - Source: [Microsoft Tech Community](https://techcommunity.microsoft.com/blog/EducatorDeveloperBlog/connecting-github-copilot-to-my-oscilloscope/4555545)

**Openness and value capture (pricing evidence)**
- R&S MXO AI Connect is free. It "does not require an AI model hosted by Rohde & Schwarz", and AI client and model costs depend on the provider the user chooses [primary] — [R&S product page](https://www.rohde-schwarz.com/au/_258817.html).
- Keysight's MCP server has no stated price or licence on its product page [primary, absence noted] — [keysight.com/find/kmsic](https://www.keysight.com/find/kmsic).
- Keysight's ADS MCP needs a minimum licence version of 2026.02. Nexus MCP checks out a licence token [secondary report] — [Wevolver](https://www.wevolver.com/article/keysight-mcp-servers-ai-agents-rf-design). This is software-seat monetisation of agents in design tools, not in instruments.
- NI Nigel needs an ni.com login tied to an active licence or subscription, with a daily request limit. It is powered by Microsoft Azure OpenAI [secondary report: search summary of NI docs; the direct fetch returned a navigation page] — [NI docs](https://www.ni.com/docs/en-US/bundle/teststand/page/nigel-ai.html). EE Times Japan (19 Sep 2025) reports that Nigel is built on an OpenAI model [secondary report] — [EE Times Japan](https://eetimes.itmedia.co.jp/ee/spv/2509/19/news055_2.html).
- Keysight, FY2025: "software and services accounted for approximately 37 percent of Keysight revenue, while annual recurring revenue was 29 percent of the total" [primary] — [Q4 FY2025 prepared remarks](https://s22.q4cdn.com/444849635/files/doc_earnings/2025/q4/transcript/Q4-FY2025-Prepared-Remarks.pdf).

### Inferences
- In this segment the interface was never the barrier. Within about 15 months of NI's Nigel launch (Jul 2025), three of the five leading makers had shipped AI products: NI an assistant, Keysight and R&S MCP agent connectors. None was found for Tektronix or Anritsu. Open-source servers already existed for the low-cost Chinese brands. The remaining barriers are guardrails (validated command sets, approval gates), the physical set-up (probing and wiring) and trust in traceable calibration, not access.
- The value has not moved to the agent layer yet: the vendor MCP servers are given away, and LLM costs go to model providers. Where agents are monetised it is through existing software seats (NI subscriptions, Keysight ADS/Nexus licences). Keysight's server talks to NI-VISA and R&S VISA and accepts "bring-your-own SCPI" for instruments without a Keysight definition file (release notes). That makes it a potential cross-vendor agent gateway, though validated guardrails exist only for Keysight models.
- "Self-tuning" in the strict sense (an agent tuning against the instrument's own reading on a known standard) is closest to shipping in (a) Zurich Instruments' automated qubit calibration and tune-up (deterministic automation, not marketed as AI), and (b) R&S's company claim of agents iterating "until the measurement goal is reached". Neither has been independently confirmed.

### Gaps
- No vendor agent/MCP product was found for Tektronix, Teledyne LeCroy, Anritsu, Rigol, Siglent, Yokogawa or Chroma. Searches for Tektronix and R&S were run. Searches for LeCroy, Anritsu, Rigol and Siglent vendor tools were not run before the budget ran out, so absence is not proven.
- Keysight MCP server release date: "May 2026, v0.1, eighteen tools" comes from a search-engine summary. The vendor pages fetched show no date. Could not verify.
- No adoption or usage numbers for any agent product (downloads, active users, paying seats).

---

## (3) Company sections

### 3.1 Keysight Technologies

**Takeaway:** Keysight has the strongest outside evidence of commercial lead in the AI-interconnect cycle and the highest disclosed software/recurring share of the hardware makers. It has shipped an instrument MCP server and agentic design tools, and it has hedged T4 through an investment in Liquid Instruments. Its exposure to an AI-capex pause is high (commercial communications was 54.5% of Q3 FY2026 revenue).

**Identity**
- US; NYSE: KEYS; fiscal year ends 31 October.
- About 16,800 employees at 31 Oct 2025 (7,400 in Asia Pacific) [primary] — [2025 AR](https://s22.q4cdn.com/444849635/files/doc_financials/2025/ar/2025-Annual-Report.pdf).

**How much of the business the theme touches**
- Essentially all of it: electronic T&M plus design/EDA software.
- FY2025 revenue by end market: commercial communications $2,488M (46.3%), aerospace/defence/government $1,238M (23.0%), electronic industrial $1,649M (30.7%) (my arithmetic from the AR table) [primary].

**Test a: position, judge, openness, value capture**
- Owns the judge: its installed base of instruments and their calibration and service.
- Services revenue (repair, calibration, extended warranties, technical support, software updates, professional services) was $1,312M in FY2025 (24.4% of revenue) at a 66.9% gross margin. "Product support services deliver comprehensive support that includes parts, repair, and accredited calibrations" [primary] — [2025 AR](https://s22.q4cdn.com/444849635/files/doc_financials/2025/ar/2025-Annual-Report.pdf).
- Openness: KMSIC works with any MCP client ("Microsoft Copilot, Claude Code, Cursor, Windsurf, Gemini and with agents running automated test sequences"). It connects through Keysight, NI or R&S VISA. Commands come from Keysight definition files with "Built-in guardrails" [primary] — [product page](https://www.keysight.com/find/kmsic).
- Value capture: no price disclosed for KMSIC. Monetisation stays with hardware and with ADS/Nexus licences.

**Test b: outside evidence of lead**
- Filed results show record demand:
  - Orders were $2,091M in Q3 FY2026 against revenue of $1,846M (book-to-bill 1.13, my arithmetic); 9M orders were $5,787M against 9M revenue of $5,163M.
  - The Q3 FY2026 deck calls it a "Second consecutive record quarter with orders over $2 billion" [primary] — [8-K](https://www.sec.gov/Archives/edgar/data/0001601046/000160104626000029/exhibit991-q326pressrelease.htm); [Q3 deck](https://s22.q4cdn.com/444849635/files/doc_earnings/2026/q3/earnings-result/Q3-26-Earnings-Results.pdf).
- Outside award: "Keysight AI Data Center Builder won the Data Center Innovation best product award at the European Conference on Connectivity in October of 2025" [outside award, reported by Keysight; the award body's own listing was not checked] — [Q4 FY2025 remarks](https://s22.q4cdn.com/444849635/files/doc_earnings/2025/q4/transcript/Q4-FY2025-Prepared-Remarks.pdf).
- Named-partner work: "collaborated with Broadcom to validate next-generation 1.6T networking silicon", and with Meta at OCP on "large-scale validation of GPUs and networking prior to deployment into clusters" [company claim naming partners; not independently confirmed] — same source.
- Investor signal: Keysight co-led Liquid Instruments' $50M Series C (Apr 2026) [secondary report] — [SiliconANGLE](https://siliconangle.com/?p=741861).

**Test c: revenue model**
- FY2025: software and services about 37% of revenue; ARR 29% [primary] — [Q4 FY2025 remarks](https://s22.q4cdn.com/444849635/files/doc_earnings/2025/q4/transcript/Q4-FY2025-Prepared-Remarks.pdf).
- Revenue recognised over time was $1,038M (19.3%); point-in-time revenue was $4,337M (80.7%), largely hardware and perpetual or term software delivered up front [primary] — [2025 AR](https://s22.q4cdn.com/444849635/files/doc_financials/2025/ar/2025-Annual-Report.pdf).
- Q3 FY2026: software and services about 33% of revenue and ARR 24% of the mix [secondary report: MarketBeat call summary, 21 Aug 2026; the page returned 403 when fetched; definitions may differ from FY2025] — [MarketBeat](https://www.marketbeat.com/instant-alerts/keysight-technologies-q3-earnings-call-highlights-2026-08-21/). A search summary of a call aggregator says management guided the software and services share up about 300bp with M&A, to about 40% [secondary report; could not verify] — [alphaspread](https://www.alphaspread.com/security/nyse/keys/investor-relations/earnings-call/q4-2025).
- The acquisitions of Spirent, Synopsys OSG and PowerArtist are expected to add about $375M of FY2026 revenue [primary] — [Q4 FY2025 remarks](https://s22.q4cdn.com/444849635/files/doc_earnings/2025/q4/transcript/Q4-FY2025-Prepared-Remarks.pdf).

**Test d (pointer only):**
- Cash, cash equivalents and restricted cash were $2.62bn at 31 Jul 2026; Q3 FY2026 free cash flow was $403M [primary] — [8-K](https://www.sec.gov/Archives/edgar/data/0001601046/000160104626000029/exhibit991-q326pressrelease.htm).
- Full analysis belongs to the listed-company researcher.

**Test e: resilience**
- China exposure: China revenue (by customer location) was $938M in FY2025, 17.5% of revenue (FY2024 17.8%; FY2023 18.4%) [primary] — [2025 AR](https://s22.q4cdn.com/444849635/files/doc_financials/2025/ar/2025-Annual-Report.pdf).
- Risk factors cite US tariffs "including significantly higher rates on imports from China", Chinese retaliatory measures, and China-Taiwan tension that "could limit or prohibit our ability to transfer certain technologies" [primary].
- The US BIS Affiliates (50%) rule was due to snap back when its suspension ended on 9 Nov 2026 [secondary report: law firms] — [Willkie, 21 Sep 2026](https://www.willkie.com/publications/2026/09/time-for-exporters-to-evaluate-their-screening-capabilities-reimposition-of-50-percent-rule). Whether it took effect: could not verify.
- Scenario exposure: commercial communications was $1,006M of Q3 FY2026 revenue (54.5%, +56% YoY) [primary; share is my arithmetic]. That is high gearing to AI data-centre and wireline capex, which helps in an acceleration and hurts in a 2028 financing-led pause. Cushions are aerospace/defence/government (18.4% of Q3 revenue, +14%) and recurring revenue (29% of FY2025).

**Transitions**
- **T1 (expert to agent-run set-up)**
  - Said: "describe what you want in natural language instead of writing SCPI commands or scripts" (KMSIC docs, 2026). The 6 Oct 2026 design-software release covers agents directing ADS/Nexus tasks. The AR says "We have used AI capability, such as machine learning and neural network models, across many Keysight solutions" [company claim].
  - Done: KMSIC shipped (v0.1, May 2026 [secondary date]) for nine instrument categories, with 1-port SOLT calibration and power-supply set-up procedures. Every command sequence needs engineer approval [primary].
  - Funded: inside company R&D; no separate figure.
  - Timing: 2026 first release. 2-port calibration "not yet available"; several families "Coming Soon" [primary] — [supported instruments](https://helpfiles.keysight.com/kmsic/English/keysight_mcp_for_instrument_control/Content/supported-instruments.html).
  - What must go right: definition-file coverage across the installed base; customers allowing agents to execute; the approval gates loosening as trust builds.
- **T2 (closed to open interfaces)**
  - Done: open MCP over open VISA, including competitors' VISA; bring-your-own SCPI with "unchecked" marking for instruments without a definition file [primary] — [release notes](https://helpfiles.keysight.com/kmsic/English/keysight_mcp_for_instrument_control/Content/release-notes.html).
  - Value capture if open: not priced, so value accrues through hardware pull-through and support contracts. This is an inference.
- **T3 (one-off hardware to software and subscription)**
  - Said: the FY2025 AR aims to "grow the software and services content of our business... increasing recurring revenue" [primary].
  - Done: Spirent ($1,564M), OSG ($578M), PowerArtist; 37% software and services / 29% ARR in FY2025.
  - Risk: the hardware boom dilutes the share (about 33% in Q3 FY2026, secondary).
- **T4 (cheaper hardware plus heavier computation; FPGA and software-defined)**
  - Done: co-led Liquid Instruments' $50M Series C and entered a "commercial arrangement... for joint development of AI-driven instrumentation" (Apr 2026; terms undisclosed) [secondary report] — [SiliconANGLE](https://siliconangle.com/?p=741861).
  - The PXIe VXT vector transceivers are in the KMSIC support list [primary].
- **T5 (instruments as data sources for customers' AI)**
  - KMSIC is a "Locally run executable so development stays on-premise" with a "Complete audit trail for every run" [primary]. The data stays with the user.
  - AI Data Center Builder is emulation and validation software [company claim].
  - No evidence of Keysight monetising customer measurement data.

**Unverified claims**
- The "up to 40%" software and services guidance (secondary).
- The ARR definition change between 29% and 24% (could not verify).
- The KMSIC release date and the "18 tools" count (secondary).
- Keysight Q4 FY2026 results were not found and are probably due in late November 2026 (inference from timing; could not verify).

### 3.2 Rohde & Schwarz (private; owns Zurich Instruments)

**Takeaway:** R&S is a large private group whose defence and critical-infrastructure weight makes it less dependent on AI capex than Keysight. It has shipped the most "loop-closing" agent claim among the instrument majors (MXO AI Connect, free) and owns the quantum-control leader whose software automates calibration and tune-up. Financial disclosure is thin: revenue, employees and backlog only.

**Identity**
- Munich, Germany; "privately owned company" [primary] — [R&S 28 Nov 2025](https://www.rohde-schwarz.com/us/about/news-press/all-news/rohde-schwarz-shows-resilience-in-a-challenging-environment-revenue-exceeds-three-billion-euros-for-the-first-time_229356-1598656.html).
- Fiscal year ends 30 June.
- Family or foundation ownership details: could not verify in this session (the Bundesanzeiger accounts were not accessed).
- No IPO, listed bond or other route to investor exposure was found (could not verify; not searched after the budget ran out).

**Disclosed financials (private)**
- FY2025/26 (Jul 2025-Jun 2026): net revenue EUR 3.6bn; more than 16,500 employees at 30 Jun 2026 [primary: boilerplate in releases of 10 Sep 2026 and 27 Oct 2026] — [R&S 27 Oct 2026](https://www.rohde-schwarz.com/jp/_229356-1706630.html); [R&S 10 Sep 2026](https://www.rohde-schwarz.com/se/_229356-1677312.html).
- Implied growth is about +13.9% on FY2024/25 (my arithmetic; EUR 3.6bn is rounded).
- FY2024/25: revenue EUR 3.16bn (+7.8%), "a record high of over EUR 5 billion" order backlog, "the operating result was positive" (no amount), R&D "a double-digit percentage of its revenue", more than 15,000 employees [primary] — [R&S 28 Nov 2025](https://www.rohde-schwarz.com/us/about/news-press/all-news/rohde-schwarz-shows-resilience-in-a-challenging-environment-revenue-exceeds-three-billion-euros-for-the-first-time_229356-1598656.html).
- FY2023/24: revenue EUR 2.93bn (+5.3%), order intake EUR 3.87bn (+22.77%) [secondary: search snippet of an R&S release].
- The full FY2025/26 results release (order intake, profit) was not found. The prior year's came on 28 Nov 2025, so it is probably due in late Nov 2026 (inference).
- Acquisitions of NEOSAT and PHYTRONIC announced 23 Sep 2026 [secondary: search summary; not opened].

**How much of the business the theme touches**
- The Test & Measurement division plus Zurich Instruments.
- The division split of revenue is not disclosed (could not verify).

**Test a: position and openness**
- Owns the judge: instruments and installed base.
- MXO AI Connect opens its oscilloscopes to any MCP client, free and local, with the user's choice of LLM and data policy [primary] — [product page](https://www.rohde-schwarz.com/au/_258817.html).
- Zurich Instruments owns quantum-control hardware plus the LabOne Q software layer, which "provides automation for calibration and tune-up" [primary] — [ZI release 9 Mar 2026](https://www.zhinst.com/de/news/zurich-instruments-launches-zqcs-quantum-control-system-master-long-lived-logical-qubit/).

**Test b: outside evidence of lead**
- Record backlog above EUR 5bn (FY2024/25) [primary, company-reported].
- Zurich Instruments calls QCCS (2018) the "world's first commercially available quantum computing control system" [company claim].
- Named customers and partners: Photonic Inc., QuantrolOx integration (Mar 2024), Australia's National Quantum Computing Testbed partner (2025), and an IQM and NVIDIA NVQLink error-correction demonstrator [secondary: trade press and company news via search] — [The Quantum Insider 9 Mar 2026](https://thequantuminsider.com/2026/03/09/zurich-instruments-zqcs-quantum-control-system-logical-qubits/).
- First ZQCS installations "come online" (no customers named) [primary].
- Market share in oscilloscopes or analysers: could not verify.

**Test c:** No breakdown of hardware against software and services; not disclosed. MXO AI Connect is free, so there is no direct software revenue from it [primary].

**Test e**
- The divisions are weighted to defence and critical infrastructure (names only; no split).
- The FY2024/25 release cites "strong business performance, particularly in Germany, Europe and North America" and a high order intake from security and defence projects [primary].
- No China figure disclosed (could not verify).

**Transitions**
- **T1**
  - Said: "AI offers engineers a new way to work with increasingly capable test instruments" (Philip Diegmann, VP). MXO AI Connect is "part of the Rohde & Schwarz instrument intelligence initiative and the R&S AI Workplace platform" [primary, 29 Oct 2026].
  - Done: MXO AI Connect shipped for MXO 3/4/5/5C and ScopeStudio.
  - Claim: agents make "repeated setup and code adjustments until the measurement goal is reached" [company claim, not independently confirmed].
  - Quantum: automated calibration and tune-up through LabOne Q [primary].
- **T2**
  - Done: free, local, standard VISA, any MCP client [primary].
  - Scope is limited to MXO; there is no stated plan for other instrument families (the release is silent).
- **T3:** No evidence.
- **T4:** The ZQCS design is FPGA-based and scalable ("more than a thousand channels per 19-inch rack") with low-latency links to GPUs and CPUs [primary]. That is computation-heavy control, but specialised hardware.
- **T5:** The user chooses the LLM and data handling; "does not require an AI model hosted by Rohde & Schwarz" [primary]. The data stays with the user.
- Funded: R&D is "a double-digit percentage of its revenue" [primary].
- What must go right: extension beyond MXO to signal and network analysers; proof that agent loops work on real measurement tasks; Zurich Instruments keeping its quantum-control lead as qubit counts scale.

**Unverified claims**
- The agent "until the measurement goal is reached" claim.
- Zurich Instruments' "first commercial" claim.
- Zurich Instruments part of R&S "since 2021" (secondary snippet; the ZQCS release confirms R&S is the parent).

### 3.3 Anritsu

**Takeaway:** Anritsu is a focused communications and optical test maker riding the 800G/1.6T data-centre transceiver ramp, with weak mobile demand. No agent or MCP product was found (the search was incomplete). Disclosure of software or recurring revenue is absent.

**Identity**
- Japan; TSE Prime 6754; fiscal year ends 31 March.

**Theme exposure**
- T&M was 58.5% of FY2025 revenue (JPY 68,774M of 117,462M; my arithmetic) [primary] — [tanshin 27 Apr 2026](https://dl.cdn-anritsu.com/en-en/about-anritsu/ir/financial-materials/fy2025/260427-01e.pdf).

**Test a**
- Owns the judge in protocol and optical transceiver test (company description of the segment: "measuring instruments and systems for a variety of communication applications, and service assurance").
- Interface openness for agents: could not verify.

**Test b**
- Orders for 800GE and 1.6TE products ("800GE still represents the larger share") [primary] — [Q1 FY2026 Q&A](https://dl.cdn-anritsu.com/en-en/about-anritsu/ir/financial-materials/fy2026/260731-01e.pdf).
- T&M operating profit rose 28.7% to JPY 10,782M (margin 15.7%, my arithmetic) despite revenue falling 1.9%, helped by "a reduction in inventories and the implementation of cost control" [primary].
- Q1 FY2026 (Apr-Jun 2026): revenue +38.0%, operating profit +219.5%, orders +95.0% to JPY 49,065M, backlog JPY 60,416M [secondary report; the source attributes the orders to T&M, but the size suggests a group figure — could not verify] — [gyokaidigest](https://www.gyokaidigest.com/companies/anritsu/report/2027-Q1).
- Outside share data: could not verify.

**Test c:** No software, services or recurring split was found in the tanshin [primary, absence noted].

**Test e**
- FY2025 revenue by region (customer location): Japan 39,885; Americas 28,627; EMEA 17,348; Asia & Others 31,601 (26.9%, my arithmetic). No China split [primary].
- FY2025 Q1 revenue was hit by customers deferring investment because of US tariff policy [primary].
- FY2026 forecast: revenue JPY 140,000M (+19.2%); T&M JPY 85,000M (+23.6%); T&M operating profit JPY 16,500M (+53.0%; margin 19.4%, my arithmetic); Americas JPY 39,000M (+36.2%) [primary].
- Cycle: data centre up, mobile flat; pre-6G pick-up expected around 2028 [primary].
- The tanshin dividend note mentions uncertainty about the Middle East situation [primary].
- Q2 FY2026 results (Jul-Sep 2026): not retrieved (could not verify).

**Transitions T1-T5:** No said or done evidence found for AI set-up, agent interfaces, subscriptions, software-defined instruments or data products (could not verify; the search budget ran out before Anritsu-specific AI searches).

**Unverified:** The Q1 FY2026 order figure and its attribution (group versus T&M).

### 3.4 Tektronix (Ralliant)

**Takeaway:** Tektronix is growing again (T&M +20.7% organic in Q3 2026) on AI data-centre and power demand, with a hardware-led product cadence. Its open Python driver package (tm_devices) makes it agent-accessible through third parties, but no official AI agent or MCP product was found.

**Identity**
- US; NYSE: RAL; separated from Fortive in 2025 [secondary report of 8-K].

**Theme exposure**
- T&M was 39.4% of Q3 2026 revenue ($244.2M of $620.1M; my arithmetic) [primary] — [8-K](https://www.sec.gov/Archives/edgar/data/0002041385/000204138526000070/ralq32026-ex991.htm).

**Test a**
- Owns an installed base of instruments (oscilloscopes and other T&M); the product range was not verified in this session.
- Openness: tm_devices, Apache-2.0, on PyVISA [secondary listing].

**Test b**
- T&M revenue $244.2M (+20.2%, organic +20.7%); book-to-bill above 1.1 in both segments; T&M operating profit $21.7M (8.9%) [primary].
- Diversified electronics +48% (company level) [secondary: transcript] — [TradingKey, 4 Nov 2026](https://www.tradingkey.com/news/transcripts/262275228-).
- "The world's first 8-channel oscilloscope" [company claim].
- Share data: could not verify.

**Test c**
- T&M adjusted EBITDA margin was 19.3% (+550bp) [primary].
- Management talks of a 2027 T&M margin "with the 2 handle on it" [secondary: transcript].
- No software or recurring disclosure (absence noted).

**Test e**
- China grew 39% company-wide, driven by data centres and the power grid [secondary: transcript].
- Tariff refunds under IEEPA: $2M (Q2), $7M (Q3), $5M (Q4) at company level, minimal in T&M [primary and secondary].
- Semiconductor revenue fell 7% against the project comparison [secondary].
- FY2026 company guidance: revenue $2.340-2.360bn [primary].
- Cycle view from management: "the cycles in T&M being unique and individual every time" [secondary].

**Transitions**
- **T1:** No AI set-up product found. Management mentioned AI used internally for customer engagement and software development only [secondary: transcript].
- **T2:** tm_devices is open source; the third-party TekAutomate MCP uses it [secondary].
- **T3:** No evidence.
- **T4:** Product launches are dedicated hardware: the 8-channel oscilloscope, a regenerative high-capacity test system for higher-voltage data centres, and an NP5000 automated test platform extension for higher-voltage semiconductor characterisation and optical devices [secondary: transcript].
- **T5:** No evidence.
- Capital allocation: "a technology tuck-in would be right up the middle of the fairway", with a focus on electrification and defence [secondary].
- What must go right: sustaining growth after the semiconductor project comparison; any software or AI layer would have to be built or acquired.

### 3.5 NI (Emerson)

**Takeaway:** NI shipped the first branded AI assistant in mainstream test software (Nigel, Jul 2025), and by Sep 2026 it generates LabVIEW code and TestStand sequences. Its documentation describes it as a developer accelerant behind a subscription login, not an agent that runs instruments. NI frames its moat as hardware, software and data integration.

**Identity**
- NI is Emerson's test and measurement business (NYSE: EMR). President: Ritu Favre [primary] — [NI Connect 13 May 2026](https://www.emerson.com/is/content/emerson/ni-connect-2026-dotcom-release-final).
- Segment revenue, orders, software share and China share: could not verify (not retrieved before the search budget ran out).

**Test a**
- Owns PXI and modular hardware and the LabVIEW/TestStand/SystemLink software layer.
- NI-VISA is an interoperability layer that even Keysight's MCP server uses [primary, Keysight docs].
- Electronic Design (11 May 2026) argues that graphical LabVIEW development "requires a more intimate AI interaction" than general tools like Claude and ChatGPT provide [secondary opinion] — [Electronic Design](https://www.electronicdesign.com/blogs/altembedded/blog/55376688/electronic-design-ai-and-ni-connect-2026). This suggests the AI value sits inside NI's own environment.

**Test b**
- At NI Connect 2026, NVIDIA, Alstom, Valeo, Zap Energy and Cyth Systems presented their use of NI technology [primary, company-curated].
- Archer Aviation used LabVIEW, VeriStand, PXI and SLSC for its Midnight eVTOL; no AI role is stated [secondary].
- Share data: could not verify.

**Test c**
- Nigel needs an active licence or subscription [secondary: NI docs summary].
- NI's subscription share of revenue: could not verify.

**Transitions**
- **T1**
  - Said: "NI Nigel AI to expand into code generation and cross-platform intelligence" (13 May 2026). "Up to 50%" cut in test development time (28 Jul 2026) [secondary report of company claim] — [automation.com](https://www.automation.com/article/emerson-ai-software-portfolio-accelerating-test-productivity-up-to-50-percent). In internal testing, Nigel cut test development and troubleshooting "from days or hours to minutes" [company claim].
  - Done: Nigel in LabVIEW and TestStand from 2025 Q3. Prompt-based VI generation, TestStand sequences from a specification, and awareness of connected hardware (by 4 Sep 2026) [primary] — [Emerson blog](https://www.emersonautomationexperts.com/2026/test-measurement/how-nigel-ai-accelerates-labview-suite-development/).
  - Not done: execution on hardware or reading of measurements (not stated); "agentic capabilities" "soon"; private cloud or local models are only customer-driven directions [primary].
  - Stance: "Nigel is an accelerant that keeps the engineer in the loop, not a replacement for engineering judgment" [primary].
- **T2:** Proprietary graphical language plus open drivers. No NI MCP server found (could not verify).
- **T3:** Subscription-gated AI [secondary].
- **T4:** "the NI platform unifies modular hardware, open software and a data foundation designed for scale" [company claim, primary].
- **T5:** "A shared data foundation simplifies the capture, management and reuse of measurement data" [company claim, primary]. NI "should be" a key player in AI and data use (EE Times Japan, 19 Sep 2025) [secondary].
- What must go right: trust in AI-generated test code in regulated aerospace, automotive and semiconductor test; moving from an assistant to agents that run sequences.

### 3.6 Teledyne LeCroy (Teledyne Technologies)

**Takeaway:** This is the weakest current datapoint among the Western majors (electronic T&M sales fell in Q3 2026), and no AI or agent product was found.

**Identity:** US; NYSE: TDY. LeCroy sits within the Instrumentation segment.

**Evidence**
- Q3 2026: Instrumentation sales $370.5M (+1.9%), operating income $99.6M; "electronic test and measurement instrumentation sales decreased $4.8 million" [primary] — [8-K 21 Oct 2026](https://www.sec.gov/Archives/edgar/data/0001094285/000109428526000055/q3-2026earningsrelease.htm).
- One summary puts the decline at 6.3%, partly due to order timing [secondary] — [panabee](https://www.panabee.com/news/teledyne-earnings-q3-2026-report).
- Instrumentation is 22.0% of Teledyne's sales (my arithmetic). Electronic T&M is a smaller unquantified part.

**Gaps:** Tests a-e and T1-T5 could not be verified: no LeCroy-specific disclosure, and the search budget ran out before LeCroy AI and protocol-analyser searches.

### 3.7 Viavi (short entry; network and optical test)

- Q1 FY2027 (to 3 Oct 2026): revenue $469.3M (+56.9%); NSE $376.1M (+74.1%; 80.1% of revenue, my arithmetic); GAAP gross margin 61.2%. CEO cites "expanding opportunities in data center and aerospace and defense end markets"; Q2 guidance $505-515M [primary] — [Viavi release, 4 Nov 2026](https://finviz.com/news/415958/viavi-announces-first-quarter-fiscal-2027-results).
- Ex-Spirent lines contributed $52.7M. The quarter had a 14th week, and tariff refunds added about 1pt of margin [secondary report] — [panabee](https://www.panabee.com/news/viavi-earnings-q1-2027).
- AI and agent products, and software share: could not verify.

### 3.8 Rigol 普源精电

**Takeaway:** Rigol is China's largest domestic T&M maker. It is building its own acquisition ASICs and moving from selling boxes to selling test lines ("solutions"), and it raised HK$1.14bn in a July 2026 Hong Kong IPO. Its open SCPI has attracted several community MCP servers, but no vendor agent product was found. Profitability is under pressure from component costs.

**Identity**
- China; SSE STAR 688337 and HKEX 00537 (listed 9 Jul 2026 at HK$45.98, the top of the range; 24,802,200 H shares; gross proceeds about HK$1.14bn; sole sponsor CITIC Securities) [company-issued release] — [ACN Newswire 13 Jul 2026](https://www.financialcontent.com/article/acnnewswire-2026-7-13-ai-computing-optical-communication-pcb-resonance-rigol-debuts-on-hkex-ushering-in-a-new-ah-era); [itiger](https://www.itiger.com/news/1102640746).
- Seven cornerstone investors committed HK$480M (about 42.11% of the offering), including HHLR Advisors (Hillhouse), CPE Hemlock, a Suzhou High-tech Zone government fund, Sungrow Power HK and CITIC Prudential [company-issued release].

**Test a**
- Owns the judge (instruments).
- Self-developed platform: products on its in-house core technology made up 88.2% of digital-oscilloscope revenue in 9M 2026 [secondary: broker] — [Huaan Securities 28 Oct 2026](https://pdf.dfcfw.com/pdf/H3_AP202610301831252523_1.pdf).
- In-house ASICs: Phoenix (2017) and Aquila (April 2026). It claims to be "the only Chinese company to commercialize digital oscilloscopes with self-developed ASIC chips" [company claim].
- Openness: several third-party MCP servers drive Rigol scopes, including the one used in the Microsoft blog [independent user report].

**Test b**
- Frost & Sullivan rankings (section 1) [third-party data commissioned by the company].
- 9M 2026 [secondary: broker, Huaan]:
  - Revenue RMB 760M (+27.5%); net profit attributable RMB 58M (+43.5%).
  - Q3 revenue RMB 270M (+13.4%); Q3 net profit RMB 21M (-13.4%).
  - High-resolution (12-bit) MHO/DHO oscilloscopes +33.8%; high-end oscilloscopes (2GHz and above) +30.3%; RF products +23.5%; VNA revenue about RMB 19.16M.
  - Large-customer revenue +79.3%; core optical-communication large customers +246.1%.
- The Q3 figures match a news report of the filing (Q3 revenue RMB 275M, +13.36%; net profit RMB 21.182M, -13.35%) [secondary] — [10jqka 29 Oct 2026](https://stock.10jqka.com.cn/20261029/c681229200.shtml).
- New products: DHO50000 for AI server PCB signal inspection and DS/MSO9000 for 1.6T optical-module mass production (Apr 2026) [company claim].

**Test c**
- "Solutions" revenue was RMB 161.51M in 9M 2026 (+45.7%), about 21% of revenue (my arithmetic). SPQ digital array measurement-and-control systems: RMB 53.36M (+58.8%) [secondary: broker].
- The broker frames the shift as moving from "selling equipment" to "building test lines" and credits system-level software capability from 耐数电子 (Naishu Electronics) [secondary opinion].

**Test d (pointer):**
- 2025 revenue RMB 900M (+16.0%); net profit RMB 86M (-6.7%); gross margin 55.1% [secondary: broker table].
- 9M 2026 gross margin 53.2% (-1.82pp); R&D 22.7% of revenue; operating cash flow -RMB 39M (inventory build) [secondary].
- R&D spend: RMB 143M / 207M / 226M in 2023 / 2024 / 2025 [company-issued release].

**Test e**
- Overseas revenue was RMB 317M in 2025, 35.2% of total [company-issued release; consistent with 2025 revenue of RMB 900M, my arithmetic].
- The Q3 profit decline is variously explained:
  - by component price increases and FX losses (Soochow Securities) [secondary: search summary of the broker note];
  - by a high base plus higher R&D and marketing spend (Huaan) [secondary]. Conflict noted.
- The broker lists price competition from overseas brands as a risk [secondary].
- Export-control exposure (US components, Entity List): could not verify.

**Transitions**
- **T1/T2:** No vendor agent product found (could not verify). Community MCP servers exist [secondary].
- **T3:** Solutions growth, as above.
- **T4:** Vertical integration into ASICs, which runs against "cheaper commodity hardware" and towards custom silicon. IPO proceeds go to ASIC iterations, specialised AI and optical instruments, capacity in China and overseas, and "global channel mergers and acquisitions" [company-issued release].
- **T5:** No evidence.

### 3.9 Siglent 鼎阳科技

**Takeaway:** Siglent has the fastest verified growth and the highest margins among the Chinese makers. Its high-end mix is rising and it is getting a direct data-centre boost (VNA, source meters, power). It is a hardware business with no agent or software-revenue evidence.

**Identity:** Shenzhen, China; SSE STAR 688112.

**Test b and financials, Q3 2026 report** (unaudited, filed 27 Oct 2026) [primary] — [cninfo](https://static.cninfo.com.cn/finalpage/2026-10-27/1225626059.PDF)
- Q3 revenue RMB 215.51M (+41.17% YoY, +10.05% QoQ); Q3 net profit attributable RMB 62.17M (+80.36%; net margin 28.8%, my arithmetic).
- 9M revenue RMB 573.26M (+32.86%); 9M net profit RMB 153.96M (+38.27%); 9M gross margin 63.04% (+1.91pp).
- 9M R&D RMB 112.56M (+16.00%), 19.63% of revenue.
- High-end product revenue +67.96% in 9M; high-end share 40% (+10pp).
- Products priced above RMB 30k +61.07%; above RMB 50k +73.50%.
- Q3 high-resolution oscilloscope domestic revenue +51.68%.
- SNA6000A VNA + SMM3000X source meter + SPD4000X power supply: +507.03% YoY in Q3, "受益于高速通信数据中心建设带动测试需求" (benefiting from test demand driven by high-speed communication data-centre construction).
- Direct sales +58.69%.
- Total assets RMB 1,869M; equity RMB 1,660M at 30 Sep 2026; 9M operating cash flow RMB 85.5M (-32.10%).

**Test a / T1-T5**
- Community MCP servers exist (siglent-sds-mcp, siglent-sdg-mcp) [secondary listing].
- No vendor AI product, software revenue or export-control disclosure found (could not verify).
- Hardware business; the shift to direct sales suggests deeper key-account relationships (inference).

### 3.10 Chroma ATE (Taiwan; listing details not re-verified this session)
- **Could not verify anything in this session.** The first Chroma search hit the exhausted search budget.
- Needed: 2025 annual report and 2026 monthly revenue (MOPS), segment split (power electronics/battery test, semiconductor and SLT test, optical inspection), China share, AI-server power-test demand, any software and AI features.

### 3.11 Yokogawa (Japan; test and measurement subsidiary)
- **Could not verify anything in this session** (search budget exhausted). No facts recorded.
- Needed: whether the Yokogawa Test & Measurement business is still owned or has been sold, its segment revenue, its optical spectrum analyser position and its AI features.

### 3.12 Liquid Instruments (private)

**Takeaway:** Liquid Instruments is the clearest T4 company: FPGA-based, software-defined instruments that "collapse" a rack of boxes into one device, now with AI-generated instruments. It is backed by Keysight.

**Identity and funding**
- Spun out of the Australian National University; private.
- $50M Series C announced 28 Apr 2026, co-led by Keysight Technologies and Australia's National Reconstruction Fund Corporation; total raised more than $100M. Valuation and revenue were not disclosed [secondary report of company announcement] — [SiliconANGLE 28 Apr 2026](https://siliconangle.com/?p=741861).
- The ANU headline says "$70 million" (probably AUD; conflict noted) — [ANU](https://www.anu.edu.au/news/all-news/anu-spin-out-liquid-instruments-secures-70-million-to-advance-ai-driven-tech).
- The NRFC release title mentions a 28.45 million investment (currency presumably AUD; the page returned 503) — [NRFC](https://www.nrf.gov.au/news-and-media-releases/national-reconstruction-fund-corporation-builds-australias-advanced-manufacturing-capability-2845-million-investment-liquid-instruments).
- IPO status: none found. Route to investor exposure: indirect and immaterial through Keysight (inference).

**Evidence**
- "Thousands of users globally", including national labs, university physics departments and electronics manufacturers in production test [company claim].
- GenInst Studio (14 Jul 2026): named users NASA, NIST, Stanford and US defence companies; early user Apex Photonics [company claim, secondary report] — [SiliconANGLE 14 Jul 2026](https://siliconangle.com/?p=788048).
- What must go right: FPGA instruments matching dedicated-box performance at the high end; accuracy and validation of AI-generated instruments; channel reach (Keysight arrangement).

### 3.13 Other private companies named in the brief (Pico Technology, Ceyear 中电科思仪, Signal Hound, Tabor Electronics, EXFO)
- **Could not verify** revenue, profit, R&D, ownership, funding or IPO status for any of them in this session (search budget exhausted before these searches).
- A community "picoscope_mcp" project exists [secondary listing] — [glama](https://glama.ai/mcp/servers/@markuskreitzer/picoscope_mcp/blob/450249997e8ff80728b98892b4f67072491b51e5/PROJECT_PLAN.md).

---

## (4) Companies considered and left out (with reasons)

- **Spirent:** no longer independent. Acquired by Keysight on 15 Oct 2025; the high-speed Ethernet, network security and channel emulation lines went to Viavi on 16 Oct 2025 [primary] — [Keysight 2025 AR](https://s22.q4cdn.com/444849635/files/doc_financials/2025/ar/2025-Annual-Report.pdf).
- **DEWETRON:** now consolidated into Anritsu's Environmental Measurement segment [primary] — [Anritsu tanshin](https://dl.cdn-anritsu.com/en-en/about-anritsu/ir/financial-materials/fy2025/260427-01e.pdf).
- **Advantest and Teradyne (chip ATE):** summary-level only per the brief; not researched (search budget). The other researcher covers listed financials.
- **Not researched because the search budget ran out (no verified facts; not excluded on merit):** Chroma ATE, Good Will Instrument (GW Instek), Yokogawa, Hioki, Kikusui, Iwatsu, EXFO, Ceyear, Uni-Trend, Pico Technology, Signal Hound, Tabor Electronics, Scientech, Aplab and any South Korean makers. The regional researcher covers China, Korea, Taiwan and India in depth.
- **Viavi:** kept only as a short entry; it is network and optical test, adjacent to the bench and RF instrument theme.

---

## (5) Where the evidence contradicts the thesis

1. **"Closed control interfaces" are not the obstacle in this segment.**
   - SCPI, VISA and IVI have been open for decades. IVI moved its specifications to GitHub in 2025 [primary].
   - Vendors shipped agent connectors within months (Keysight May 2026 [secondary date]; R&S 29 Oct 2026 [primary]), and community MCP servers already drive Rigol, Siglent, Keysight, Owon and Pico hardware [secondary].
   - The binding constraints are elsewhere:
     - guardrails and liability ("Every command sequence requires explicit engineer approval", Keysight) [primary];
     - the physical set-up ("An assistant cannot check your physical wiring for you") [independent user report];
     - traceability ("Meter tool use is not a calibration certificate") [independent user report].
2. **The value is not (yet) moving to a software layer through openness.**
   - The agent connectors are free (R&S) or unpriced (Keysight), and LLM costs go to model providers [primary].
   - The AI cycle's money is flowing to measurement hardware at new speed nodes: Keysight commercial communications +56%; Siglent VNA, source-meter and power-supply +507%; Anritsu 1.6TE orders [primary].
   - Keysight's software and services share appears to have fallen from about 37% (FY2025) to about 33% (Q3 FY2026) as hardware surged [the 33% is a secondary report].
3. **The "expert set-up" being automated is mainly test-code writing, not instrument tuning.**
   - NI's Nigel generates LabVIEW code and TestStand sequences. It "keeps the engineer in the loop" and does not, by its documentation, run hardware [primary].
   - Keysight's and R&S's servers translate intent into SCPI.
   - Only R&S claims iterative adjustment until the measurement goal is reached [company claim].
   - True self-calibration against a standard remains limited, for example Keysight's 1-port SOLT procedure with 2-port "not yet available" [primary].
4. **The "fast unambiguous judge" exists, but calibration's commercial value rests on accredited traceability, not on the judge.**
   - Keysight sells "accredited calibrations" in services ($1,312M services and other revenue in FY2025 at 66.9% gross margin, no calibration-only split) [primary].
   - The standards bodies' digital push is machine-readable certificates (PTB's DCC, an XML schema under ISO/IEC 17025; Boehringer Ingelheim to use DCCs for about 150,000 annual calibrations from 2027) [primary] — [PTB DCC](https://www.dmet.ptb.de/dcc). This is not AI-run calibration.
   - No standards-body statement on AI in calibration was found (PTB's DCC page does not mention AI; IVI is silent) [primary, absence noted].
5. **The cost of damaging hardware is lower for bench T&M than for synchrotrons or electron microscopes, yet vendors still gate every action.** This suggests customer trust and liability, not the cost of damage, set the pace (inference).
6. **T4 cuts both ways.**
   - Liquid Instruments shows FPGA software-defined instruments plus AI generation, which supports T4 [secondary].
   - Rigol is moving to custom ASICs [company claim], and Tektronix is launching dedicated high-end boxes (8-channel oscilloscope) [secondary: transcript]. At the leading edge, dedicated silicon still wins.

**Where the evidence supports the thesis:**
- Zurich Instruments' LabOne Q automates qubit "calibration and tune-up" [primary]. Quantum control is the most self-tuning-like part of this segment.
- R&S's loop-closing claim [company claim].
- The Microsoft blog shows an agent measuring and comparing readings with expected values on real hardware [independent user report].

---

## (6) What could not be verified (and what was tried)

- **Search budget:** the shared web-search budget ran out after about 35 searches. No new search queries were made afterwards; only URLs already surfaced were fetched. This is the main reason for the gaps below.
- **Category market shares** (oscilloscopes, spectrum and network analysers, signal generators, PXI) for the Western leaders: not found. Only Rigol's F&S rankings were obtained.
- **Keysight:**
  - the MCP server release date and tool count (vendor pages show no date);
  - the Q3 FY2026 software and services share (about 33%) and ARR (24%) — the MarketBeat page returned 403;
  - the "about 40%" guidance (secondary);
  - Q4 FY2026 results, probably not yet released as of 12 Nov 2026.
- **Rohde & Schwarz:**
  - FY2025/26 order intake, profit, R&D amount and division split (full release probably due late Nov 2026);
  - ownership structure details;
  - Bundesanzeiger accounts (not accessed);
  - the NEOSAT/PHYTRONIC acquisition terms;
  - any investor route.
- **Anritsu:** the Q2 FY2026 results (late Oct 2026; not found); AI and agent products; software share; the attribution of the Q1 FY2026 order figure.
- **NI/Emerson:** T&M segment revenue, orders and software share (FY2025 and FY2026); direct confirmation of Nigel's licence requirement and Azure OpenAI backing (the NI docs page fetched as navigation only; claim from a search summary).
- **Teledyne LeCroy:** any LeCroy-specific figure; AI products; PCIe/CXL protocol-test position.
- **Tektronix:** official AI or MCP products (none found in one search); software and recurring revenue; China share of T&M.
- **Not researched:** Chroma ATE, Yokogawa, Good Will, Hioki, Kikusui, Iwatsu, Advantest, Teradyne, EXFO, Ceyear, Uni-Trend, Pico, Signal Hound, Tabor, Scientech, Aplab.
- **Export controls:**
  - whether the BIS Affiliates rule took effect on 9-10 Nov 2026 or was suspended again;
  - EU and Japanese restrictions on high-end instruments to China;
  - Chinese countermeasures affecting instrument makers;
  - specific CCL thresholds (e.g. 3A002) for general-purpose instruments.
- **Standards bodies:** BIPM, IEEE and NIST statements on AI in calibration or on DCCs; whether IVI or LXI has any agent initiative (none found).
- **Calibration as a business:** the calibration share of revenue at R&S, Anritsu and Tektronix; third-party calibration market size.
- **Adoption metrics** for any agent product (Nigel users, KMSIC downloads, MXO AI Connect users).

---

## (7) Sources with dates

**Company primary documents**
- Keysight 2025 Annual Report / 10-K (FY ended 31 Oct 2025) — https://s22.q4cdn.com/444849635/files/doc_financials/2025/ar/2025-Annual-Report.pdf
- Keysight Q4 FY2025 prepared remarks (call 24 Nov 2025) — https://s22.q4cdn.com/444849635/files/doc_earnings/2025/q4/transcript/Q4-FY2025-Prepared-Remarks.pdf
- Keysight Q3 FY2026 8-K Ex.99.1 (18 Aug 2026) — https://www.sec.gov/Archives/edgar/data/0001601046/000160104626000029/exhibit991-q326pressrelease.htm
- Keysight Q3 FY2026 earnings deck (Aug 2026) — https://s22.q4cdn.com/444849635/files/doc_earnings/2026/q3/earnings-result/Q3-26-Earnings-Results.pdf
- Keysight MCP Server for Instrument Control:
  - product page ((c) 2000-2026, accessed 12 Nov 2026) — https://www.keysight.com/find/kmsic
  - release notes — https://helpfiles.keysight.com/kmsic/English/keysight_mcp_for_instrument_control/Content/release-notes.html
  - overview — https://helpfiles.keysight.com/kmsic/English/keysight_mcp_for_instrument_control/Content/overview.html
  - getting started — https://helpfiles.keysight.com/kmsic/English/keysight_mcp_for_instrument_control/Content/getting-started.html
  - supported instruments (all (c) 2026) — https://helpfiles.keysight.com/kmsic/English/keysight_mcp_for_instrument_control/Content/supported-instruments.html
- Rohde & Schwarz:
  - FY2024/25 results release (28 Nov 2025) — https://www.rohde-schwarz.com/us/about/news-press/all-news/rohde-schwarz-shows-resilience-in-a-challenging-environment-revenue-exceeds-three-billion-euros-for-the-first-time_229356-1598656.html
  - EuMW 2026 release (10 Sep 2026) — https://www.rohde-schwarz.com/se/_229356-1677312.html
  - electronica 2026 release (27 Oct 2026) — https://www.rohde-schwarz.com/jp/_229356-1706630.html
  - MXO AI Connect release (29 Oct 2026) — https://www.rohde-schwarz.com/jp/about-us/news-press/all-news/rohde-schwarz-introduces-mxo-ai-connect-for-ai-assisted-oscilloscope-workflows_229356-1709313.html
  - MXO AI Connect product page ((c) 2026) — https://www.rohde-schwarz.com/au/_258817.html
- Zurich Instruments ZQCS release (9 Mar 2026) — https://www.zhinst.com/de/news/zurich-instruments-launches-zqcs-quantum-control-system-master-long-lived-logical-qubit/
- Anritsu:
  - FY2025 consolidated results (27 Apr 2026) — https://dl.cdn-anritsu.com/en-en/about-anritsu/ir/financial-materials/fy2025/260427-01e.pdf
  - Q1 FY2026 Q&A (Jul 2026) — https://dl.cdn-anritsu.com/en-en/about-anritsu/ir/financial-materials/fy2026/260731-01e.pdf
- Ralliant Q3 2026 8-K Ex.99.1 (4 Nov 2026) — https://www.sec.gov/Archives/edgar/data/0002041385/000204138526000070/ralq32026-ex991.htm
- Teledyne Q3 2026 8-K (21 Oct 2026) — https://www.sec.gov/Archives/edgar/data/0001094285/000109428526000055/q3-2026earningsrelease.htm
- Viavi Q1 FY2027 release (4 Nov 2026; PR Newswire via Finviz) — https://finviz.com/news/415958/viavi-announces-first-quarter-fiscal-2027-results
- Emerson/NI:
  - Nigel launch (22 Jul 2025) — https://www.emerson.com/en/corporate/news/2025/07-emerson-expands-ai-capabilities-into-test-and-measurement-software-portfolio
  - NI Connect release (13 May 2026) — https://www.emerson.com/is/content/emerson/ni-connect-2026-dotcom-release-final
  - Emerson Automation Experts blog (4 Sep 2026) — https://www.emersonautomationexperts.com/2026/test-measurement/how-nigel-ai-accelerates-labview-suite-development/
  - NI docs, Nigel AI (undated; content via search summary) — https://www.ni.com/docs/en-US/bundle/teststand/page/nigel-ai.html
- Siglent Q3 2026 report (27 Oct 2026) — https://static.cninfo.com.cn/finalpage/2026-10-27/1225626059.PDF
- Rigol HKEX debut release (ACN Newswire, company-issued, 13 Jul 2026) — https://www.financialcontent.com/article/acnnewswire-2026-7-13-ai-computing-optical-communication-pcb-resonance-rigol-debuts-on-hkex-ushering-in-a-new-ah-era

**Standards and metrology bodies**
- IVI Foundation, "IVI 2026" (dated 15 Apr 2025) — https://www.ivifoundation.org/downloads/IVI%20Generations/IVI%202026.pdf
- IVI ANSI-C completion notice (17 Feb 2026; title only) — https://ivifoundation.org/2026/02/17/AnsiCComplete.html
- PTB DCC page (accessed 12 Nov 2026) — https://www.dmet.ptb.de/dcc
- 6th International DCC Conference (24-26 Feb 2026) — https://dcc-conference-2026.ptb.de/
- DAkkS/PTB press release (14 Dec 2022) — https://dakks.de/en/pressrelease/calibration-certificates-and-national-emblems-the-digital-future.html

**Law firms (export controls)**
- Miller & Chevalier, BIS 2025 review and 2026 mid-year update (12 Aug 2026) — https://www.millerchevalier.com/publication/bis-export-controls-2025-year-review-and-2026-mid-year-update
- Willkie Farr & Gallagher (21 Sep 2026) — https://www.willkie.com/publications/2026/09/time-for-exporters-to-evaluate-their-screening-capabilities-reimposition-of-50-percent-rule

**Secondary reports (trade press, broker notes, aggregators, transcripts)**
- SiliconANGLE:
  - Liquid Instruments Series C (28 Apr 2026) — https://siliconangle.com/?p=741861
  - GenInst Studio (14 Jul 2026) — https://siliconangle.com/?p=788048
- ANU news (2026; "$70 million") — https://www.anu.edu.au/news/all-news/anu-spin-out-liquid-instruments-secures-70-million-to-advance-ai-driven-tech
- NRFC release (title only; 503 on fetch) — https://www.nrf.gov.au/news-and-media-releases/national-reconstruction-fund-corporation-builds-australias-advanced-manufacturing-capability-2845-million-investment-liquid-instruments
- Wevolver, Keysight MCP servers for RF design (Oct 2026) — https://www.wevolver.com/article/keysight-mcp-servers-ai-agents-rf-design
- HPCwire (6 Oct 2026) — https://www.hpcwire.com/aiwire/2026/10/06/keysight-advances-its-design-software-with-agentic-ai/
- Microsoft Tech Community, "Connecting GitHub Copilot to my oscilloscope" (11 Sep 2026) — https://techcommunity.microsoft.com/blog/EducatorDeveloperBlog/connecting-github-copilot-to-my-oscilloscope/4555545
- Electronic Design, AI and NI Connect 2026 (11 May 2026) — https://www.electronicdesign.com/blogs/altembedded/blog/55376688/electronic-design-ai-and-ni-connect-2026
- EE Times Japan on LabVIEW AI (19 Sep 2025) — https://eetimes.itmedia.co.jp/ee/spv/2509/19/news055_2.html
- automation.com reproduction of the Emerson release, "up to 50 percent" (28 Jul 2026; 403 on fetch) — https://www.automation.com/article/emerson-ai-software-portfolio-accelerating-test-productivity-up-to-50-percent
- TradingKey, Ralliant Q3 2026 call transcript (4 Nov 2026) — https://www.tradingkey.com/news/transcripts/262275228-
- MarketBeat, Keysight Q3 FY2026 call highlights (21 Aug 2026; 403 on fetch) — https://www.marketbeat.com/instant-alerts/keysight-technologies-q3-earnings-call-highlights-2026-08-21/
- alphaspread, Keysight Q4 2025 call summary (search snippet only) — https://www.alphaspread.com/security/nyse/keys/investor-relations/earnings-call/q4-2025
- Huaan Securities 华安证券, Rigol Q3 2026 note (28 Oct 2026) — https://pdf.dfcfw.com/pdf/H3_AP202610301831252523_1.pdf
- 10jqka, Rigol Q3 2026 (29 Oct 2026) — https://stock.10jqka.com.cn/20261029/c681229200.shtml
- itiger, Rigol IPO (Jul 2026) — https://www.itiger.com/news/1102640746
- QQ News, Rigol IPO (30 Jun 2026) — https://news.qq.com/rain/a/20260630A01Y5600
- gelonghui, Rigol H1 2026 (Aug 2026) — https://m.gelonghui.com/news/5305844
- gyokaidigest, Anritsu Q1 FY2026 (2026; 429 on fetch) — https://www.gyokaidigest.com/companies/anritsu/report/2027-Q1
- panabee:
  - Teledyne Q3 2026 — https://www.panabee.com/news/teledyne-earnings-q3-2026-report
  - Viavi Q1 FY2027 — https://www.panabee.com/news/viavi-earnings-q1-2027
- The Quantum Insider, ZQCS (9 Mar 2026) — https://thequantuminsider.com/2026/03/09/zurich-instruments-zqcs-quantum-control-system-logical-qubits/
- Microwave Journal, R&S FY2024/25 (Nov 2025) — https://www.microwavejournal.com/articles/45085-rohde-and-schwarz-shows-resilience-in-a-challenging-environment-revenue-exceeds-three-billion-euros-for-the-first-time
- MCP directory listings (undated, accessed 12 Nov 2026):
  - https://glama.ai/mcp/servers/armchairdeity/mcp-server-scpi
  - https://socket.dev/pypi/package/labmcp-scpi
  - https://lobehub.com/fr/mcp/magnusjohansson-siglent-sds-mcp
  - https://glama.ai/mcp/servers/masahiro-999/oscilloscope-mcp
  - https://glama.ai/mcp/servers/mabl/pyMSO5000
  - https://resources.altium.com/p/building-mcp-server-analog-discovery
  - https://www.github.com/tektronix/tm_devices
