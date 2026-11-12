# AI-native chip-verification entrants and the open-source threat to proprietary verification and sign-off tools (worldwide)

Date of research: 12 November 2026 (position as of that date). Status: FINAL (continuation pass completing an earlier partial pass; all earlier facts, tags and URLs kept, corrections marked "CORRECTION").

Tag legend: [PRIMARY] filing, paper or official document; [INDEPENDENT] confirmed by an outside party; [COMPANY CLAIM] stated by the company, not confirmed outside; [SECONDARY] press or analyst report only; [UNVERIFIED] could not be verified.

Method note: the earlier pass used about 35 web searches before the shared search budget ran out, then direct fetches only. This pass ran about 25 searches until the shared budget (200 per turn, all agents) was exhausted again, then direct fetches of known URLs only. Firecrawl credits were exhausted (12 Nov 2026); Cadence's licence-term PDFs are behind a Cloudflare check, so their wording comes from search excerpts. Some earlier-pass facts carry no URL; they are kept and marked "(URL not recorded in earlier pass)". Facts taken from other researchers' notes in this folder are marked "(cross-ref)".

## 1. Who are the AI-native chip-verification entrants? (global map: funding, product, customers, engine ownership)

### Takeaway
About 20 AI-native entrants are active. They are concentrated in the US, with a thin layer in Israel, Switzerland, the UK, Canada and China, and none with a disclosed round was found in Japan or Korea. Only ChipAgents has many named customers and large funding focused on verification; Ricursive ($4B) and Cognichip are design-model bets. Every entrant whose tool integration is documented drives the incumbents' or open-source engines; the exceptions are Hiveware (a new simulator) and the proof firms. None owns a verdict engine.

### Cited Findings
**United States**
- ChipAgents (Alpha Design AI). Founded 2024 by UCSB professor William Wang. HQ Santa Clara, CA per the company newsroom; some coverage says Santa Barbara [SECONDARY], which is unresolved. Rounds: Series A $21M (21 Oct 2025, Bessemer lead; total $24M); A1 $50M (17 Feb 2026, Matter Venture Partners lead; total $74M); A2 $60M (29 Jul 2026, B Capital new lead; total ">$134M"). Other investors: Micron, MediaTek, Ericsson, ScOp. Rambus became a strategic investor on 22 Oct 2026 (amount undisclosed). Valuation undisclosed. Company claims: 6x ARR growth in H1 2026; 120+ semiconductor companies (Jul); 200+ "enterprise deployments" (Oct). Named customers and case studies: MediaTek, Micron, Ambiq, Whalechip, Andes, eMemory, Analog Devices, Rambus. Product IC-star (27 Oct 2026). Integrates with customers' existing tools; no own engines named [COMPANY CLAIM] — https://chipagents.ai/newsroom
  - A2 release: Bessemer, Micron, MediaTek, Ericsson and ScOp joined. No valuation appears in the release, Dealroom or HPCwire. One aggregator's "$250M valuation" (Feb 2026) is [UNVERIFIED] and inconsistent with the round history [PRIMARY release; SECONDARY] — https://www.businesswire.com/news/home/20260729819576/en/ ; https://dealroom.co/news/141848-chipagents-adds-60m-to-series-a-as-micron-mediatek-back-ai-chip-design/ ; https://qz.com/chipagents-series-a2-funding-nvidia-partnership-072926
  - CORRECTION/reconciliation: the three Series A tranches sum to $131M, and pre-A money of about $3M makes the $134M total. Crypto Briefing's "$131–134M" range is consistent with this.
  - Homepage (12 Nov 2026): no pricing and no tool integrations named. IC-star is described as "Full-flow autonomy for digital and analog chip design". SOC 2 Type II. "Backed by" logos include Samsung, in addition to the investors above. Claims: 200+ enterprise deployments, 50% design-cycle reduction, 20,000+ users, "40% annual LLM spending savings" [COMPANY CLAIM] — https://chipagents.ai/
  - "In production at several chipmakers" (unnamed); terms of the Nvidia partnership not specified; no revenue disclosed [SECONDARY, TheNextWeb, 29 Jul 2026] — https://thenextweb.com/news/nvidia-partner-chipagents-raises-60m-for-agentic-chip-design
  - Own model, Renoir: covers RTL generation, verification plans, assertions, simulations and IP protection. Fine-tuned on semiconductor data. Running cost claimed to be as low as 22% of "Claude Fable 5". Nvidia is evaluating it. VerilogEval-v2 score of 97.4% (152/156, Jan 2025) [SECONDARY / COMPANY CLAIM, Crypto Briefing, 14 Oct 2026] — https://cryptobriefing.com/nvidia-chipagents-ai-chip-design-evaluation/
  - Joint paper with STMicroelectronics on AI agents across the IC-verification lifecycle (DAC 2026) [SECONDARY, SemiWiki] — https://semiwiki.com/events/372079-chipagents-leads-the-ai-revolution-at-dac-2026/
- Normal Computing. New York, founded 2022. $50M strategic round led by Samsung Catalyst Fund (25 Mar 2026); total raised >$85M. Product Normal EDA. Claims ">half of top-10 semis" as users (unnamed) [COMPANY CLAIM]. The earlier pass gave no URL; round coverage added here — https://www.vcaonline.com/news/2026032512/normal-computing-raises-50m-led-by-samsung-catalyst-to-accelerate-silicon-design-and-solve-ai-hardware-energy-crisis/
  - Normal EDA autoformalises specifications. It "integrates with VCS and Xcelium and relies on these tools to run simulations and update coverage", so it drives the incumbents' simulators [COMPANY CLAIM] — https://normalcomputing.com/solutions
  - Blog, 2 Mar 2026: an open-source Verilog simulator built by AI agents in 43 days. About 580K lines on a CIRCT fork, with an event-driven simulator and VPI/cocotb support. Code attribution: 40% Claude Opus 4.5, 14% Claude Opus 4.6, 46% Codex. The company says no other open-source simulator could compile its test benches [COMPANY CLAIM] — https://normalcomputing.com/blog/building-an-open-source-verilog-simulator-with-ai-580k-lines-in-43-days
- Cognichip. Redwood City. $33M seed (2025). $60M Series A (1 Apr 2026, Seligman Ventures lead; Lip-Bu Tan on board). Total $93M. ACI is a "physics-informed" foundation model for chip design. In April 2026 it claimed ">30 semiconductor companies engaged", "declined to name any of its customers" and named no chip designed with ACI. Claims up to 50% less design effort [COMPANY CLAIM; SECONDARY] — https://siliconangle.com/2026/04/01/cognichip-raises-60m-reinvent-chip-design-physics-inspired-ai-models/
  - Update: ACI Enterprise launched Sep 2026. CEO Faraj Aalaei said in a Sep 2026 theCUBE interview that it is "engaged with 40 customers" [COMPANY CLAIM] — https://dealroom.co/news/talk-T0neZchFnc4-cognichip-launches-aci-enterprise-to-compress-chip-design-by-10x/ ; Lux Capital lists it as a portfolio company — https://www.luxcapital.com/companies/cognichip
- Ricursive Intelligence. Palo Alto. $35M seed (Sequoia, late 2025). $300M Series A at a $4B valuation (26 Jan 2026), led by Lightspeed, with DST, NVentures, Felicis, 49 Palms, Radical AI and Sequoia. No named customers. Building an end-to-end AI model for chip design, not verification-specific [SECONDARY] — https://convergedigest.com/ricursive-intelligence-raises-300m-series-a-for-ai-driven-chip-design/ ; total raised $335M at $4B "in 4 months" — https://www.pulse.bot/venture-capital/news/how-ricursive-intelligence-raised-335m-at-a-4b-valuation-in-4-months-10b304b1-a937-4325-8408-c41a6bcc954f
  - CORRECTION: one aggregator dates a "$335M round" to June 2026. That figure is the total of the two rounds above, not a new round.
- Agentrys. San Jose. $24.5M announced 26–27 Aug 2026: an oversubscribed $19.1M seed led by Etna Labs plus a $5.4M pre-seed led by MediaTek, its first strategic backer. Founder Mark Ren (ex-NVIDIA Research, ChipNeMo lead). Pitched as an "open platform" for building agentic workflows. Claims >90% on CVDP [COMPANY CLAIM] — https://siliconsemiconductor.net/article/125240/Agentrys_raises_245_million_to_build_agentic_design_automation_for_chipmakers ; DAC 2026 launch — https://semiwiki.com/events/372043-agentrys-launches-agentic-design-automation-at-dac-2026/
- Bronco AI. Automates DV debug, root-cause analysis and regression triage, plus spec review, RTL and assertion writing, testbench bring-up and coverage closure. Pricing: "No hourly billing. No per-seat math. One fee for a service that keeps working." Investors named on its site: 8VC, Elad Gil, SV Angel. Runs on-premises with bring-your-own-model; it "drive[s] your EDA tools" via Slurm/LSF. Claims: 15-minute root cause, 10x faster UVM stimulus, 96% coverage, 100GB+ waveforms. No customers named [COMPANY CLAIM] — https://www.bronco.ai/
  - Funding amounts unverified. A database profile shows about $500K pre-seed or convertible note from YC, Glasswing and FJOR, but it may be a different Bronco AI. SemiWiki says a pre-seed closed on 6 Sep 2023 and there is no public record of later funding. Webinar on 1 May 2026, "Full-chip SoC debug in 15 minutes"; at DAC 2026 [SECONDARY/UNVERIFIED] — https://semiwiki.com/wikis/company-wikis/bronco-ai-wiki
- MooresLabAI. Austin, TX, founded 2025 by Shelly Henry, Shashank Chaurasia and Sirish Munipalli. Product families MooreIP and MooreSoC. Agents: VerifAgent (UVM testbench generation; "up to 86%" verification-cost reduction), DebugAgent and CoverageAgent. Sold three ways: floating tool licences; tool plus forward-deployed engineers; tool plus FDEs plus DV engineers. Also a "Verification-as-a-Service" option that delivers UVM in under 45 days. Integrates with "all major EDA tools including Synopsys, Cadence, and Siemens". On-prem, with an on-prem LLM (MooreLLM). Partnership with Breker. The "backed by" logos (NVIDIA, Microsoft, OpenAI, Google, Foundation Capital and others) are labelled "industry partners", not investors. No funding amounts given [COMPANY CLAIM] — https://www.mooreslab.ai/ ; earlier pass: "15+ chip companies"; 93% on CVDP v1.1 agentic verification track (56 of 62 problems scored) [COMPANY CLAIM] (URL not recorded in earlier pass)
- Architect Labs. Palo Alto. $24M seed (Jun 2026, Kindred Ventures) to "design and provably verify custom chips" [SECONDARY] — https://siliconangle.com/2026/06/18/architect-labs-nabs-24m-speed-chip-design-projects-ai/
- VerifAIX. Cupertino, with teams in the US, India and Israel. $5M seed (30 Sep 2026), co-led by Bluehill VC and Endiya Partners. Spec-first agentic verification plus formal. Founders Madhulima Tewari, Avner Landver and Kenneth Roe; adviser Aarti Gupta [COMPANY CLAIM] (cross-ref) — https://verifaix.com/verifaix-raises-5m-seed-funding-co-led-by-bluehill-vc-and-endiya-partners/ ; https://inc42.com/?p=572648
- Voltai (Menlo Park). Recruiting pages describe it as Sequoia-backed and building "agentic systems and frontier foundation models for semiconductor and electronics design". No round size found. One listing says "founded 2016", which is probably wrong [UNVERIFIED] — https://www.hirebase.org/company/voltai/jobs/solution-architect-caabff67
- Silimate. YC S23, San Francisco, founder Ann Wu. $2M seed (27 Sep 2023); about $2.5M over 3 rounds. No 2026 round found [SECONDARY databases] — https://www.cbinsights.com/company/silimate/financials
- PrimisAI. RapidGPT for FPGA engineers. $1.5M seed (Oct 2023, Raptor Group). No 2026 funding or customers found [SECONDARY database] — https://www.cbinsights.com/company/primisai/financials
- Rise Design Automation (CEO Badru Agarwala). IPCreate and IPTransform for spec/HLS-to-RTL, shown at DAC 2026. Claims about 1M gates per engineer per week. Verification uses "trusted SystemVerilog". No funding disclosed [COMPANY CLAIM; SECONDARY] — https://semiwiki.com/wikis/company-wikis/rise-design-automation
- SigmanticAI (YC). AI-generated RTL plus testbenches and assertions [SECONDARY, search excerpt; no URL fetched].
- ChipStack (Seattle). Acquisition by Cadence announced 10 Nov 2025, terms undisclosed. ChipStack AI Super Agent launched 10 Feb 2026 (launch URL not recorded in earlier pass). Acquisition coverage, "Cadence Welcomes ChipStack" — https://www.edge-ai-vision.com/?p=55880

**Israel, Europe, Canada**
- Hiveware (Tel Aviv). Emerged from stealth 27 Jul 2026 with a $24M Series A led by RTP Global. Builds a clean-sheet SystemVerilog simulator on standard servers: "up to 10x faster full-chip simulation", roadmap to 100x, aimed at replacing some emulation. 30 staff, founders ex-Hailo. Pilots with "three of the world's largest semiconductor companies" (unnamed) [COMPANY CLAIM] (cross-ref) — https://hiveware.io/hiveware-emerges-from-stealth-with-24-million-in-rtp-global-led-series-a/
- Chipmind (Zurich; Chipmind AG, Technoparkstrasse 1). $2.5M pre-seed (Oct 2025, Founderful). CHF 1.37M Innosuisse grant (2026) (URL not recorded in earlier pass). Its site lists ETH Zurich, NVIDIA Inception, Chips JU, Innosuisse and Founderful as "backed by & featured in". Agents run lint, simulation and synthesis, read logs and waveforms, and write RTL. Supports Synopsys, Cadence and Siemens tools plus Yosys, Verilator and OpenLane. Sponsors DVCon Europe. No customers named [COMPANY CLAIM] — https://www.chipmind.ai/
- Tattvam AI (UK): $1.7M pre-seed, Feb 2026 — https://semiengineering.com/startup-funding-q1-2026/ ; siliXon (UK): $1.5M pre-seed, Apr 2026 (URL not recorded; whether it is in verification is unverified); Mach42 (Oxford): $9.5M, 21 Jul 2026, IP Group lead with BGF and Foresight; surrogate models for analog verification, "up to 2,500x faster", Cadence Virtuoso integration [COMPANY CLAIM] (cross-ref) — https://mach42.ai/resource-Mach42Secures9.5MilliontoAccelerateAgentic-.html ; Astrus (Toronto): $12M Series A, Sep 2026, analog layout — https://semiengineering.com/startup-funding-q3-2026/

**China, India, Japan/Korea/Taiwan**
- China (light coverage; the China researcher covers the region). 智维创芯 makes ChatDV, an agent for digital-chip verification. Angel round "数千万元" (tens of millions of RMB) led by 国中资本 with 石溪资本 and 奇绩创坛. Claims >10x efficiency [SECONDARY/COMPANY CLAIM] — https://inforcapital.com/news/智维创芯完成数千万元天使轮融资致力于实现芯片设计验证自动化/ . IC Coder (Chengdu Pengye Jiantu) builds an FPGA/IC front-end and verification agent on its own model; seeking funding (May 2026) [SECONDARY] — https://eu.36kr.com/en/p/3794744102296840 . 芯流微蓝 (Zhejiang University Prof. Sun Qi): first round closed, size unknown [SECONDARY].
- India. MulticoreWare acquired Simulus Automation (DV services for advanced SoCs, about 100 engineers), announced 2 Sep 2026 [SECONDARY] — https://quantumzeitgeist.com/multicoreware-buys-simulus-automation-chips/ . VerifAIX has teams in India.
- Japan/Korea/Taiwan. No AI-native DV start-up with a disclosed round was found (searches on 12 Nov 2026). The Taiwan link runs through MediaTek's strategic stakes (Agentrys pre-seed lead; ChipAgents investor and customer).

### Inferences
- Money is concentrated: Ricursive ($335M) and ChipAgents ($134M) together exceed all other entrants combined among those found.
- Strategic chip-company investors (MediaTek, Micron, Samsung, Rambus, Ericsson) are mostly also customers. This signals real demand, but it is not neutral validation.
- Coverage of Japan, Korea and India-domiciled AI-native DV products is thin, possibly because searches were English-heavy.

### Gaps
- No valuation for ChipAgents, Normal, Cognichip, Agentrys, Bronco, MooresLab or Hiveware.
- Bronco's and Voltai's funding.
- Founding dates for Bronco, Chipmind and Voltai.
- No named customer for Cognichip, Ricursive, Normal, Bronco, MooresLab or Hiveware.

## 2. Does any entrant own a verdict? Incumbents' licence responses, acquisitions, Nvidia, Arm and the model makers

### Takeaway
No AI-native chip-verification entrant owns a sign-off-grade verdict engine. They drive VCS, Xcelium, Questa, Jasper or open-source tools, and the incumbents present their own engines as "ground truth". No evidence was found that incumbents have restricted third-party agents. Instead they have opened interfaces (MCP, customer-hosted LLMs) and added agent-specific charges: Cadence coins and a Siemens "agentic surcharge". The one acquisition of an entrant, Cadence buying ChipStack, shows the absorption path.

### Cited Findings
**Engine ownership**
- Normal relies on VCS and Xcelium [COMPANY CLAIM] — https://normalcomputing.com/solutions . Bronco "drive[s] your EDA tools" — https://www.bronco.ai/ . MooresLab integrates with Synopsys, Cadence and Siemens — https://www.mooreslab.ai/ . Chipmind supports both incumbent and open-source tools — https://www.chipmind.ai/ . ChipAgents integrates with existing tools — https://chipagents.ai/newsroom
- Exceptions: Hiveware's own simulator (cross-ref, URL above), and Normal's AI-built open-source simulator (company claim, URL above).
- Synopsys calls its tools "the underlying, ground-truth engineering tools" in GPT-Synopsys (30 Sep 2026) [PRIMARY] — https://news.synopsys.com/2026-09-30-OpenAI-and-Synopsys-Announce-GPT-Synopsys-Frontier-Intelligence-to-Revolutionize-Chip-Design (cross-ref)
- Cadence CFO, 27 Apr 2026: agentic AI "doesn't replace the core EDA engines. It calls them more often" [PRIMARY transcript] — https://www.fool.com/earnings/call-transcripts/2026/04/27/cadence-cdns-q1-2026-earnings-transcript/ (cross-ref)
- Estimated engine shares: VCS 45–50%, Xcelium 40–45%, PrimeTime 90%+, Calibre 85%+, Palladium 55–60%, ZeBu 35–40% [SECONDARY estimates, SemiAnalysis, 21 May 2026] — https://newsletter.semianalysis.com/p/eda-market-primer (cross-ref)

**Licence terms and agent access**
- Cadence agentic AI card terms (versions 2026Jul and 2026Sep): "Cadence super agent products are licensed on a coin-based basis, and Coins are required for access to and Use of Super Agent Software. Such usage metrics are processed locally within the Super Agent Software's license management system deployed by Customer and are not transmitted to Cadence." The Jul 2026 version adds: "Customer is solely responsible for managing its Authorized Users" [PRIMARY document, text seen as search excerpt only] — https://www.cadence.com/content/dam/cadence-www/global/en_US/documents/terms-and-conditions/Cadence-agenticaicard-2026Sep.pdf ; https://www.cadence.com/content/dam/cadence-www/global/en_US/documents/terms-and-conditions/Cadence-agenticaicard-2026Jul.pdf
- Siemens EDA supplemental terms define an "Authorized Agent" as an individual "excluding any EDA Competitor personnel, who is working on Customer's premises". This covers human contractors, not AI agents. Third-party hosting needs SISW's prior written consent [PRIMARY via search excerpt].
- No published Synopsys, Cadence or Siemens clause was found that bars third-party AI agents from driving their tools (search, 12 Nov 2026).
- Opening rather than restricting:
  - Siemens Questa One Agentic Toolkit (27 Feb 2026) has MCP interfaces and works with GitHub Copilot, Claude Code, Cursor and Cline. At DAC 2026 it was "not positioned as a path to fully autonomous IC verification" (URL not recorded in earlier pass).
  - Cadence CFO, 26 Oct 2026: "Our model allows customers to use their own LLM infrastructure ... And can license the underlying design agents" [PRIMARY transcript] — https://www.webull.com/news/15818016766808064 (cross-ref)
  - Synopsys Investor Day (30 Sep 2026) set out three adoption routes: the Autopilot platform, Synopsys agents inside customer AI platforms, and frontier models — https://news.synopsys.com/2026-09-30-Synopsys-Details-Growth-Strategy-and-Long-term-Financial-Model-at-2026-Investor-Day (cross-ref)
- Pricing changes for agents:
  - Siemens CFO (12 Nov 2026): "we will introduce an agentic surcharge on really this underlying software subscription" [SECONDARY transcript] — https://in.investing.com/news/stock-market-news/earnings-call-transcript-siemens-posts-record-orders-in-q4-2026-as-growth-quickens-93CH-5698664 (cross-ref)
  - Cadence (17 Feb 2026): "we will price it as like a virtual engineer or agent" — https://www.fool.com/earnings/call-transcripts/2026/02/17/cadence-cdns-q4-2025-earnings-transcript/ (cross-ref)
  - Synopsys (26 Aug 2026): "subscription of our agents, subscription of our workflow as well as a consumption measure" — https://www.webull.com/news/15497781661541376 (cross-ref)

**Incumbent agent products and evidence**
- Cadence: >100 active AI Super Agent engagements (26 Oct 2026) — https://www.webull.com/news/15818016766808064 . MediaTek runs ChipStack in production, with 50–70% coverage improvement and 1.4–2x effort reduction (URL not recorded in earlier pass; customer-named, not audited). "Nvidia is the first customer using ChipStack to autonomously verify its chip designs" [SECONDARY, ITBrief, 2 Jun 2026] — https://itbrief.co.uk/story/nvidia-unveils-tools-for-enterprise-ai-agents
- Synopsys: an autonomous DV workflow with NVIDIA (26 Jul 2026), "up to 50X faster time-to-validated RTL" and +20% coverage; no customer named, "Customers are currently evaluating", availability H2 2026 [COMPANY CLAIM] — https://news.synopsys.com/2026-07-26-Synopsys-Showcases-Comprehensive-Autonomous-Engineering-Workflows-from-Silicon-to-Systems,-Developed-with-NVIDIA-Technology . 25–40% debug-cycle cut in "early evaluations" with AMD and Microsoft, where AMD is only "actively evaluating" — https://news.synopsys.com/2026-07-27-Synopsys-Advances-Agentic-AI-Chip-Design-with-AMD-and-Microsoft . More than 30 active engagements for the verification agent — https://www.webull.com/news/15497781661541376 (all cross-ref)
- Siemens: "self-verifying" long-running EDA agents with NVIDIA at DAC 2026 [PRIMARY title] — https://blogs.sw.siemens.com/cicv/2026/07/29/self-verifying-eda-ai-agents/ ; Futurum [SECONDARY] — https://futurumgroup.com/insights/synopsys-cadence-and-siemens-take-agentic-chip-design-autonomous-at-dac/

**Acquisitions, shutdowns, large rounds (2025–2026)**
- Bought:
  - ChipStack, by Cadence (Nov 2025).
  - Precision Innovations (San Diego), by Siemens. Announced 20 Jul 2026, close expected Q3, terms undisclosed. Precision Innovations "since 2019 has provided the bulk of software engineering and user support for OpenROAD"; its technology goes into Siemens's Digital Design Creation portfolio [PRIMARY via release copies] — https://schnitgercorp.com/2026/07/20/siemens-to-acquire-precision-innovations-for-ai-powered-chip-planning/ ; https://news.siemens.com/pl-pl/siemens-to-acquire-precision-innovations/ . Channel Insider (22 Jul 2026) says the deal is completed; closing is unconfirmed — https://www.channelinsider.com/channel-business/mergers-and-acquisitions/siemens-precision-innovations-defacto/
  - Defacto, by Siemens (21 Jul 2026) (cross-ref).
  - Simulus Automation, by MulticoreWare (2 Sep 2026).
  - Adjacent deals: Teradyne bought TestInsight (Apr 2026, pre-silicon test validation); Siemens bought Canopus AI (metrology, closed 12 Jan 2026) [SECONDARY] — https://www.pulse.bot/cio-pulse/news/teradyne-acquires-testinsight-to-speed-ai-and-datacenter-chip-testing-a40a8caa-46ba-4293-b7bd-f559688ccfa5/ ; https://itbrief.news/story/siemens-buys-canopus-ai-to-boost-chip-metrology-tools
- Shut down: no AI-native verification start-up shutdown found. Efabless (open-silicon shuttle provider) shut down in early 2025 (section 4).
- Large rounds: Ricursive $300M (Jan 2026); ChipAgents $50M + $60M (Feb and Jul 2026); Cognichip $60M (Apr 2026); Normal $50M (Mar 2026); Agentrys $24.5M, Architect Labs $24M and Hiveware $24M (Jun–Aug 2026).

**Nvidia, Arm and the model makers**
- Nvidia release (26 Jul 2026) [PRIMARY / COMPANY CLAIM] — https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Expands-NVIDIA-Agent-Toolkit-With-NVIDIA-PhysicsNeMo-and-CUDA-X-Libraries-to-Transform-How-the-World-Engineers-Designs-and-Builds/default.aspx
  - "NVIDIA Nemotron 3 Ultra leads among open models in agentic RTL coding on the comprehensive verilog design problems benchmark".
  - ACE-RTL is "an agent for designing hardware from NVIDIA Research".
  - "ChipAgents is using NVIDIA Agent Toolkit to build domain-specific AI agents" and is "fine-tuning NVIDIA Nemotron models ... including debug, formal verification, coverage and more".
  - Cadence's harness, Synopsys's long-running DV agents, and Siemens's Questa One toolkit and Fuse EDA AI Agent are all named.
- Nvidia's other ties: NVentures invested in Ricursive and Harmonic (cross-ref). Nvidia put $2B into Synopsys stock at $414.79 per share (1 Dec 2025, "not exclusive") [PRIMARY] — https://news.synopsys.com/2025-12-01-NVIDIA-and-Synopsys-Announce-Strategic-Partnership-to-Revolutionize-Engineering-and-Design (cross-ref)
- Model makers:
  - OpenAI: GPT-Synopsys (30 Sep 2026) is multi-year. OpenAI licenses Synopsys tools, with a revenue share (URL above).
  - Anthropic: The Information (3 Nov 2026) reported a roughly 15-person chip team using Claude; SNPS and CDNS fell up to about 4% [SECONDARY] (URL not recorded in earlier pass).
  - Moonshot: the Kimi K3 demo (section 4).
- Arm: the only Arm item found is an Arm employee's independent study (section 3). No Arm product or acquisition in AI verification was found.
- Foundry certification (transition 5): TSMC's certification grids (as of 1 Oct 2026, for A14, A16, N2P and N3C) have columns only for Cadence, Synopsys and Siemens EDA [PRIMARY] — https://www.tsmc.com/english/dedicatedFoundry/oip/eda_alliance (cross-ref). Futurum (24 Sep 2026): TSMC certifies tools against its rules, but "no regime certifies what an autonomous agent did" [SECONDARY] — https://futurumgroup.com/insights/tsmcs-oip-forum-turns-agentic-chip-design-demos-into-production-flows/ (cross-ref)

### Inferences
- The incumbents are monetising agent traffic (coins, surcharges, consumption) rather than blocking it. The entrants' bargaining position therefore depends on incumbent goodwill and pricing. A surcharge on every agent-driven run taxes the entrants' value proposition.
- Siemens buying the main OpenROAD maintainer concentrates the most important open-source physical-design project's engineering capacity inside an incumbent. Whether OpenROAD support continues at the same level is unknown.

### Gaps
- Full text of the Cadence, Synopsys and Siemens agent licence terms.
- Whether any incumbent prices third-party agent calls differently from human use.
- Arm's own agent tooling.
- Nvidia's internal verification agents beyond ACE-RTL and ChipStack use.

## 3. How well does AI actually do verification? (background claim check and evidence)

### Takeaway
The best published evidence shows frontier models miss about 21–37% of seeded bugs while declaring sign-off. LLM-written assertions break under meaning-preserving rewrites, and agentic formal verification completes only about 40% of tasks (Infineon). Benchmark gains are real but mostly self-reported. CORRECTION: the background claim merges two different sources.

### Cited Findings
- CORRECTION to the brief: the "806 bugs / up to 300 missed" figure and arXiv 2609.05658 are different works, and neither is an official "Arm study".
- (a) Bugs study (Brian Bailey, "Putting AI To The Test", Semiconductor Engineering, 2 Nov 2026) [SECONDARY report of unpublished work] — https://semiengineering.com/putting-ai-to-the-test/
  - Author: Vikash Kumar, "senior verification architect at Arm"; the article calls it "his independent work".
  - Set-up: 25 hand-coded designs (bus protocols, DMA engines, ECC memory). "Into those he inserted 806 bugs."
  - Results: "Claude Opus 5 detected 79.2% of seeded defects, GPT-5.4 detected 76.2%, and GLM-5.2 detected 62.8%." The best model missed 20.8%, "approximately 168 bugs"; GPT-5.4 missed "about 192"; GLM-5.2 missed "close to 300".
  - "All three models reached 100% of their self-defined verification goals and declared sign-off". Each model was run three times and "each run produced different results".
  - "The RTL has never been made public." No paper or arXiv ID is cited. The work is linked to his book "AI-Assisted Hardware Verification: Cognitive Verification Architecture with the VEGA Framework" (Springer per the earlier pass).
  - So "up to 300 missed" is true only of the weakest model (GLM-5.2).
- (b) arXiv 2609.05658: "Robustness of LLM-Generated SystemVerilog Assertions to Semantics-Preserving RTL Transformations" [PRIMARY] — https://arxiv.org/abs/2609.05658
  - Sole author FNU Aditi (no affiliation given); submitted 4 Sep 2026; cs.LG; 10 pages.
  - Tests small open code models (Qwen2.5-Coder-7B, DeepSeek-Coder-V2-Lite), not frontier models, on 40 programs and 295 assignment behaviours from the VERT dataset.
  - Three meaning-preserving transformations: operand reordering, identifier renaming and redundant parenthesisation.
  - 9.7%–27.0% of behaviours that were correct on the original RTL become incorrect after a transformation. DeepSeek's accuracy rose from 53.9% to 63.7% under renaming, yet 19.5% of its originally correct behaviours failed. No "806" or "300" appears in the paper.
- Benchmarks:
  - CVDP (NVIDIA, arXiv 2506.14074, Jun 2025): 783 problems in 13 categories, agentic and non-agentic. The best models scored ≤34% pass@1 on code generation (Claude 3.7 Sonnet, GPT-4.1, Llama 3.1 405B) [PRIMARY] — https://arxiv.org/html/2506.14074v1
  - Wizwand tracker (May 2026, CVDP cid03): GPT-5.5 44% pass@1, Claude Opus 4.7 42.8% [SECONDARY tracker, UNVERIFIED] — https://www.wizwand.com/sota/verilog-generation-on-cvdp-cid03
  - Nemotron 3 Ultra "leads among open models" on CVDP agentic RTL (Nvidia, 26 Jul 2026, URL above) [COMPANY CLAIM]. Entrant claims (Agentrys >90%; MooresLab 93% on 56 of 62 problems; ChipAgents VerilogEval-v2 97.4%) have no independent reproduction found [COMPANY CLAIM].
  - FVEval: arXiv 2410.23299, 15 Oct 2024, by Minwoo Kang, Mingjie Liu, Ghaith Bany Hamad, Syed Suhaib and Haoxing Ren (code at github.com/NVlabs/FVEval). Scores are not on the abstract page [PRIMARY] — https://arxiv.org/abs/2410.23299
- Infineon Saarthi:
  - Original paper (arXiv 2502.16662, Feb 2025; DVCon): about 40% overall efficacy for end-to-end formal verification [PRIMARY] — https://arxiv.org/html/2502.16662v2
  - "Saarthi for AGI" (arXiv 2603.03175, 3 Mar 2026, DVCon U.S. 2026), by Aman Kumar, Deepak Narayan Gadde, Luu Danh Minh, Vaisakh Naduvodi Viswambharan, Keerthan Kopparam Radhakrishna and Sivaram Pothireddypalli: "70% improvement in the accuracy of generated assertions" and "50% reduction in the number of iterations" to coverage closure, on CVDP formal tasks. The abstract does not say whether the 70% is relative or absolute [PRIMARY] — https://arxiv.org/abs/2603.03175
  - SemiWiki (Feb 2026): proof rates and coverage stay below 50% on simple designs, and a human in the loop is essential [SECONDARY] — https://www.pulse.bot/hardware/news/an-agentic-formal-verifier-innovation-in-verification-686cdf19-a424-470d-9b3f-3b552be94e5f/
- Field survey: Wilson/Siemens 2026 study (published 8 Sep 2026; 604 respondents). 82.8% of respondents are using AI beyond pilot but only 9.0% have it broadly integrated. IC/ASIC first-silicon success was 5%, against 14.4% in 2024, after a methodology change. Verification takes 49% of IC/ASIC project time [INDEPENDENT survey, vendor-sponsored] — https://verificationacademy.com/topics/planning-measurement-and-analysis/2026-siemens-eda-and-wilson-research-group-functional-verification-study/ (cross-ref)

### Inferences
- The failure that matters most is false confidence: models "declared sign-off" while missing bugs. This argues for an external judge (simulation coverage measured by a trusted engine, or proof) above any agent. That favours whoever owns the judge.
- Results vary from run to run and are sensitive to how a design is rewritten. Today, AI checks therefore cannot serve as regression oracles without a deterministic engine underneath.

### Gaps
- Kumar's RTL and seeded-bug set are unpublished, so his results cannot be reproduced.
- No independent reproduction found of any entrant's benchmark claim.
- FVEval scores were not retrieved.
- No published vendor-independent field study of agentic DV in production.

## 4. The open-source threat (transition 4): the Kimi K3 episode and the state of open-source engines

### Takeaway
The Kimi K3 "chip" was a pre-layout, simulation-only demo on an open 45 nm library, with no place-and-route, sign-off or fabrication. It moved the share prices (SNPS about −8%, CDNS about −9.5% on 17 Jul 2026) but not the vendors' revenues. Open-source verification engines are active and improving. But open sign-off stops at 130–180 nm, where IHP's open PDK is "not yet intended for production use", and no foundry accepts open-source sign-off at 28 nm or below. No commercial chip company was found replacing proprietary front-end verification with AI-driven open tools.

### Cited Findings
**Kimi K3 (Moonshot AI, China)**
- What Moonshot reported:
  - Moonshot AI's own blog; results "current as of July 16, 2026"; announced 16 Jul 2026 [PRIMARY] — https://www.kimi.com/blog/kimi-k3
  - In a single 48-hour autonomous run, K3 "designed a chip to serve a nano model" using "open-source EDA tools on the Nangate 45nm library"; the tools are not named.
  - Within 4 mm², timing closes at 100 MHz, 1.46M standard cells, 0.277 MB SRAM, an INT4 MAC array.
  - 8,700+ tokens/s decode "in simulation". Described as "an early proof of concept". No place-and-route, sign-off or fabrication is mentioned.
- Repository MoonshotAI/nano-kpu [PRIMARY] — https://github.com/MoonshotAI/nano-kpu
  - Tools: Verilator 5.x, Yosys (≥0.64) and the Nangate45 library.
  - Area and timing are pre-layout estimates from yosys/abc mapping, "not validated through backend place & route" and "not sign-off values". No tape-out.
  - "a demonstration of Kimi K3, not an official project by Moonshot AI".
  - So the chip was neither manufactured nor proven working in silicon. No foundry design kit was used.
- Share moves on Friday 17 Jul 2026 [SECONDARY]:
  - Investing.com: CDNS and SNPS fell "roughly 9%" — https://www.investing.com/news/stock-market-news/cadence--synopsys-slide-as-kimi-k3-designs-chip-in-48h-using-no-proprietary-eda-4798775
  - TIKR: CDNS closed at $330.11, −9.47% — https://www.tikr.com/blog/cadence-stock-fell-9-in-a-day-on-a-chinese-ai-chip-demo-heres-where-the-stock-could-go-in-2026
  - ts2.tech, intraday at 13:07 EDT: CDNS $329.50 (−9.64%), SNPS $382.98 (−8.17%) — https://ts2.tech/en/synopsys-nasdaqsnps-stock-sinks-as-kimi-chip-demo-tests-the-eda-moat/
  - Other reports give SNPS −7.8% to −8.2%. CORRECTION: one later summary calls the ts2 intraday figures "closes".
  - Tech Fund (27 Jul 2026): shares down "around 14%" since the news; TSMC certifies the three vendors via OIP; open tools lack advanced PDKs — https://www.techinvestments.io/p/the-eda-crash-and-the-massive-ai (cross-ref)
- Analysts [SECONDARY]:
  - Bloomberg Intelligence (Niraj Patel): "We see no immediate threat to Cadence and Synopsys' revenue bases"; leading-edge chips are "entrenched on Cadence and Synopsys' proprietary engines" (URL not recorded in earlier pass).
  - BNP Paribas (Andrew DeGasperi): the reaction was overdone or unwarranted; "buy the dip" — https://seekingalpha.com/news/4615018-cadence-synopsys-sink-as-moonshot-brings-eda-disruption-risks-bnp-says-buy-the-dip
  - Bernstein (Robin Zhu): K3 is "confirmatory" and the reaction sensible. Morgan Stanley (Gary Yu) commented on K3 generally. Mizuho said K3 strengthens its positive stance on SNPS and CDNS — https://stockti.com/synopsys-shares-plunge-8-as-moonshot-ai-s-chip-demo-raises-eda-moat-concerns
  - Taiwanese press: experts call the sell-off a buying opportunity — https://finance.technews.tw/2026/07/20/kimi-driven-selloff-makes-cadence-synopsys-buying-opportunities/
- Context: closes on 11 Nov 2026 were CDNS $329.26 and SNPS $462.12 [SECONDARY aggregator] — https://stockanalysis.com/stocks/cdns/statistics/ ; https://stockanalysis.com/stocks/snps/statistics/ (cross-ref). My computation: CDNS is about flat against its 17 Jul close and SNPS about +21% above its 17 Jul intraday quote of $382.98. Cadence Q3 2026 revenue rose 22% (cross-ref, cadence notes).

**State of open-source engines (2026)**
- Yosys releases monthly: 0.69 (9 Sep), 0.70 (13 Oct), 0.71 (12 Nov). The page shows no year; 2026 is inferred from the cadence [PRIMARY] — https://github.com/YosysHQ/yosys/releases
- YosysHQ (Vienna) also sells the Tabby CAD Suite (monthly releases Apr–Oct 2026) and published an "Interim YosysHQ LLM Policy" (26 Aug 2026) — https://blog.yosyshq.com/ . It is a partner in an Austrian FFG open-EDA project (Jun 2026–May 2029, €153,095) — https://projekte.ffg.at/projekt/b9e4453e-f36b-1410-864f-00d3c07d99bb/pdf (cross-ref)
- cocotb: 2.0.0 (15 Sep), 2.0.1 (15 Nov), 2.1.0 (30 Aug); years not shown [PRIMARY] — https://github.com/cocotb/cocotb/releases
- Verilator has no X/Z four-state logic, encrypted IP, mixed Verilog/VHDL or SDF timing back-annotation, so commercial tools remain necessary for sign-off simulation [SECONDARY] — https://pyshine.com/Verilator-Fastest-Open-Source-Verilog-Simulator/
- OpenROAD: its main engineering supporter, Precision Innovations, is being bought by Siemens (section 2). LibreLane succeeds OpenLane — https://www.crowdsupply.com/wafer-space/gf180mcu-run-1/updates/librelane-template
- iEDA (China; Peng Cheng Laboratory with ICT-CAS) takes blocks and SoCs from netlist to GDSII "at 28nm". Tape-outs on 110 nm and 28 nm: three chips in the 2023 paper; five chips of 700k–100M gates per COSCUP 2025 [PRIMARY academic] — https://arxiv.org/pdf/2308.01857 ; https://pretalx.coscup.org/coscup-2025/talk/UFGPUX/ . No foundry statement found that accepts iEDA output as sign-off.

**Open PDKs, shuttles and funders**
- IHP open PDK [PRIMARY] — https://github.com/IHP-GmbH/IHP-Open-PDK
  - SG13G2 (130 nm) is "early access" and SG13CMOS5L "preview only"; both are "not yet intended for production use".
  - Ships KLayout and Magic DRC/LVS decks.
  - Funded by German projects IHP Open130-G2 (16ME0852) and FMD-QNC (16ME0831).
- No foundry-backed open PDK at 28 or 22 nm was found. OpenRPDK28 (RIOS Lab) is an academic 28 nm kit "under construction" [PRIMARY repo] — https://github.com/mfkiwl/OpenRPDK28 . A May/June 2026 EuroCDP (EU) report on open EDA tools exists, but its text could not be retrieved — https://eurocdp.eu/wp-content/uploads/2026/06/Open_EDA_Tools_general_version.pdf
- Shuttles:
  - Efabless shut down in early 2025 [SECONDARY] — https://tinytapeout.com/news/efabless-shutsdown/
  - wafer.space (Singapore, Tim Ansell) offers GF180MCU runs at $7,000 for 1,000 dies [COMPANY CLAIM] — https://www.crowdsupply.com/wafer-space/gf180mcu-run-1/updates/were-live
  - Tiny Tapeout plans quarterly 2026 shuttles with IHP, GF or SkyWater [PRIMARY project docs] — https://docs.google.com/document/d/12KPutDPBst7FF0ncB1qyxErDYeATmXoQLGjRq38dfjU/mobilebasic
  - Cadence is launching a SKY130 MPW service with 40 dies per slot and no packaging (same FAQ).
- Funders found: Google (open PDKs moved to the CHIPS Alliance, Nov 2023 [PRIMARY title only]) — https://opensource.googleblog.com/2023/11/open-source-pdks-joining-linux-foundation-chips-alliance.html ; the German federal government (IHP); Austria's FFG (YosysHQ); the EU (EuroCDP; Chips JU appears as a backer of Chipmind); China (iEDA); NVIDIA Inception (Chipmind).
- Market mix: Cadence's DVCon 2026 slide (IBS data) shows about three-quarters of design starts at 28 nm or above by 2030 [SECONDARY data in vendor slides] — https://dvcon-proceedings.org/wp-content/uploads/Broadening-the-Adoption-of-Hardware-Assisted-Verification-with-Next-Generation-Emulation-Appliance.pdf (cross-ref)
- Commercial replacement: no documented case of a chip company replacing VCS, Xcelium or Questa with open tools driven by agents (searches on 12 Nov 2026). Normal's AI-built simulator is the closest (company claim). Chipmind and MooresLab drive both open and proprietary tools.

### Inferences
- The threat is real in the mature-node, front-end slice: Verilator, cocotb and Yosys plus agents. That slice is large by design starts but small by EDA revenue.
- At sign-off, open tools lack foundry-certified decks below 130 nm. TSMC certifies only the three vendors. Both are structural barriers that agents do not remove.
- Precision Innovations moving into Siemens weakens the open physical-design stack's independence.

### Gaps
- DARPA's and the EU's current open-EDA funding levels.
- The EuroCDP report's findings.
- Verilator's 2026 release status.
- Whether any foundry (including Chinese foundries with iEDA) accepts open-source sign-off at any node below 130 nm.

## 5. Proof-AI moving into hardware, and machine-proved regression checks

### Takeaway
Harmonic shipped real Verilog proving (27 Oct 2026) with one customer-quoted case study (Tensordyne) and an Ibex result. Academic Lean-based RTL proof is moving fast. Machine-proved regression checks between revisions of AI-edited RTL are not yet standard practice: 2026 papers say simulation "is still the norm".

### Cited Findings
- Harmonic, "Aristotle Expands Into Formal Verification for Software and Hardware, Starting With C and Verilog" (27 Oct 2026) [PRIMARY/COMPANY CLAIM] — https://harmonic.fun/news/aristotle-software-hardware-verification/
  - Covers Verilog control-path properties (liveness, safety) and mathematical data-path properties.
  - Aristotle proposes properties; engineers review and commit them; it runs in CI on every commit.
  - Self-serve consumption pricing (no rates published) plus enterprise and on-prem plans (cross-ref).
- Reuters, 27 Oct 2026: usage-based pricing; the DIII-D fusion lab is a user; no chip-design customer named [SECONDARY] — https://1027wbow.com/2026/10/27/robinhood-ceos-ai-startup-harmonic-expands-into-software-chip-design-verification/
- Docs: "Behaviors not listed as properties are not verified" [COMPANY CLAIM] — https://aristotle.harmonic.fun/docs/overview (cross-ref)
- Tensordyne case study [COMPANY CLAIM, customer-quoted; payment status not stated] — https://harmonic.fun/aristotle/case-studies/tensordyne/ (cross-ref)
  - Block of 12.2M gate equivalents.
  - 241 properties: 185 proved and 56 refuted with counterexamples.
  - Bugs found 25,000–110,000 cycles after reset.
  - Quote from Tensordyne engineer Jonathan Ko.
- Ibex RISC-V MUL/DIV (3 Nov 2026): 9 properties proved against the Sail RISC-V model, run from a coding agent (Claude Code or Codex) with Aristotle over MCP. Aristotle compiles SystemVerilog plus SVA into Lean 4 against a hand-built model of digital circuits [COMPANY CLAIM] — https://harmonic.fun/news/ibex-mul-div-verification (cross-ref)
- Other proof moves:
  - Normal (autoformalisation, URL above) and Architect Labs ("provably verify") make related claims.
  - VerifAIX: spec-first agentic verification plus formal.
  - Axiom reports unnamed customers in hardware development [SECONDARY] — https://fortune.com/2026/06/01/axiom-math-econlib-antitrust-economic-theory-verified/ (cross-ref)
  - LUBIS EDA FormalOS (Germany, formal services) — https://www.generation-nt.com/communiques-presse/lubis-eda-launches-formalos-infrastructure-for-systematic-scalable-2082294 (cross-ref)
  - &Truth (US$70M seed, Lean-based) is not hardware-specific (cross-ref).
- Academic work:
  - InfiniVerif (NeurIPS 2026): Verilog to Lean 4, LLM-built invariants checked by Lean's kernel. Validated on a 5-stage MIPS, the lowRISC Ibex instruction cache and the Spatz vector processor [PRIMARY] — https://neurips.cc/virtual/2026/161609
  - Rtl2lean (arXiv 2607.16855, Jul 2026) — https://arxiv.org/abs/2607.16855
  - CKTLean (HKU, open source) extends Sparkle HDL — https://github.com/Verilean/sparkle
- Regression proofs:
  - No industry standard found.
  - "Equivalence Checking Reveals, Assertions Clarify" (NeurIPS 2026): simulation testbenches "are still the norm" for LLM-generated RTL, and the field is "moving towards" logical equivalence checking [PRIMARY] — https://neurips.cc/virtual/2026/161616
  - FormalRTL (arXiv 2603.08738) couples synthesis with equivalence checking — https://arxiv.org/abs/2603.08738v1
  - Commercial equivalence checkers exist: Synopsys HECTOR, Cadence Jasper C Apps, Siemens SLEC. The last is described as needing extensive setup [SECONDARY, paper excerpt].

### Inferences
- Proof-based judges are the one route by which an entrant could own a verdict outside EDA engines. Harmonic is closest, but its trusted base includes a hand-built circuit model and only the stated properties.
- Expecting regression proofs to be standard by 2028 is plausible in direction (CI-per-commit products, research momentum), but there is no adoption data yet.

### Gaps
- Harmonic's paying chip customers.
- Usage figures for incumbent equivalence checkers on AI-edited RTL.
- Any foundry or customer requirement for proof-based regression.

## 6. Assessment of the most credible entrants (quality tests a–e; path forward)

### Takeaway
Four entrants are assessed in depth (ChipAgents, Normal Computing, Cognichip, Ricursive), plus Harmonic's hardware line as the one entrant that owns a judge. On present evidence none clearly belongs among the 8–15 companies that matter most globally in verification. ChipAgents is the strongest "watch" candidate, but it is an agent layer exposed to absorption, as ChipStack's sale to Cadence shows. Verdicts below are my provisional judgments.

### Cited Findings
Facts and sources are in sections 1–5; only new evidence carries a URL here. Tests: a position, b lead, c revenue model, d financial strength (e resilience is under Inferences).
- **ChipAgents.** a: an agent layer with its own model (Renoir) and Nemotron fine-tunes on customers' engines; no verdict engine. b: customers named on its own pages [COMPANY CLAIM]; NVIDIA partner [PRIMARY]; ST co-authored paper [SECONDARY]; benchmarks not reproduced. c: unpublished; pitches "40% annual LLM spending savings". d: about $134M raised; strategic investors Micron, MediaTek, Ericsson, Rambus, Samsung (logo); revenue only as "6x ARR growth" [COMPANY CLAIM].
- **Normal Computing.** a: autoformalisation on top of VCS/Xcelium; its AI-built simulator could become an owned engine but is unproven. b: Samsung Catalyst lead; ">half of top-10" users unnamed. c: undisclosed; hires forward-deployed engineers [SECONDARY] — https://jobs.drivecapital.com/companies/normal-computing-2-dc61d412-1057-4f1d-bfec-c34ac239d7db/jobs/80871094-forward-deployed-engineer . d: >$85M raised; also a thermodynamic-computing hardware programme [SECONDARY] — https://www.tamradar.com/funding-rounds/normal-computing-strategic-50m
- **Cognichip.** a: a design foundation model, no verdict engine. b: 40 "engaged", none named, no chip shown. c: ACI Enterprise, pricing unknown. d: $93M (Seligman lead; Lux).
- **Ricursive.** a: an end-to-end design model; verification not core; no engine. b: no named customers. c: unknown. d: $335M at $4B (Lightspeed, DST, NVentures, Sequoia).
- **Harmonic, hardware line only** (company profile covered elsewhere). a: owns a judge, in that Lean's kernel checks the proofs; the trusted base includes a hand-built circuit model, and unstated behaviours are unverified. b: Tensordyne case study with a named engineer quote, and DIII-D as a user; no paying chip customer confirmed. c: consumption-based, "no seats or licenses" [COMPANY CLAIM] — https://harmonic.fun/ (cross-ref). d: $120M Series C at $1.45B (25 Nov 2025), about $295M total, NVentures [PRIMARY/SECONDARY] — https://harmonic.fun/news/series-c (cross-ref)

### Inferences
Scenario weights: steady growth 55%, financing pause around 2028 25%, acceleration 20%. All verdicts are my provisional judgments.
- **ChipAgents.**
  - e (resilience): grows in the steady case, as DV labour is scarce and it is multi-vendor. Its recent $134M likely covers a 2028 pause (inference; burn undisclosed). Acceleration brings both absorption risk and acquisition upside. It depends on customers' incumbent licences and on incumbent pricing (coins, surcharges); the Siemens "EDA Competitor" and hosting-consent clauses are a latent lever.
  - Path forward: (2) pricing undisclosed; (3) formal claimed, not shown; (4) neutral; (5) no barrier, no moat; (7) Renoir is a hedge. Funded; timing plausible.
  - Must go right: it stays the neutral layer and publishes customer-verified outcomes.
  - Verdict: partly coherent, with traction but no owned verdict.
- **Normal.**
  - e: its formal approach aligns with transitions (3) and (4). A pause risks its split hardware/EDA focus. It depends on VCS and Xcelium.
  - Done: the simulator and a strategic round. Said only: customer outcomes.
  - Verdict: partly coherent; direction right, evidence thin.
- **Cognichip.**
  - e: collides with transition (7); a foundation-model strategy is the most exposed to a pause.
  - Verdict: not coherent on present evidence; no named customer or output after $93M.
- **Ricursive.**
  - e: a $4B mark without customers is the most pause-sensitive and gains most in acceleration.
  - Verdict: not assessable for verification; partly coherent as a design-AI bet.
- **Harmonic (hardware).**
  - Fits (2) and (3); complements (4) via MCP; (5) not relevant; (7) DeepMind's AlphaProof Code shows labs can enter (cross-ref).
  - Verdict: coherent in direction, early; hardware revenue unproven.
- **8–15 global list:** no chip-verification entrant qualifies yet. ChipAgents is a "watch". Harmonic qualifies only if proof-based verification as a whole is counted. Most others look like features the incumbents and model makers will absorb.

### Gaps
- Pricing and revenue of every entrant.
- Burn and runway.
- Customer concentration.
- Independently confirmed outcomes.

## 7. Exposure (valuations, investors, listed vehicles), kept separate from the quality evidence

### Takeaway
Private marks exist only for Ricursive ($4B, Jan 2026) and Harmonic ($1.45B, Nov 2025). All others are undisclosed. Listed exposure exists only as negligible stakes or acquisitions inside large companies. No buy or sell view is given.

### Cited Findings
- Ricursive: $4B (Series A, 26 Jan 2026) [SECONDARY]; NVentures (NVIDIA, listed) among investors (URLs in section 1).
- Harmonic: $1.45B post-money (25 Nov 2025); NVentures [PRIMARY] — https://harmonic.fun/news/series-c (cross-ref)
- ChipAgents: valuation undisclosed. An aggregator's $250M is [UNVERIFIED]. A Sacra profile exists but was not read — https://sacra.com/c/chipagents . Listed investors: Micron, MediaTek, Ericsson, Rambus, and Samsung (logo only).
- Normal (Samsung Catalyst Fund, Samsung's venture arm), Agentrys (MediaTek), Mach42 (IP Group; its London listing is [UNVERIFIED] in this pass), Cognichip, Hiveware, VerifAIX, Architect Labs, Chipmind and Bronco: all undisclosed.
- Acquired entrants sit inside CDNS (ChipStack) and Siemens AG (Precision Innovations); terms undisclosed.
- Listed-company price data are covered elsewhere (cross-ref: CDNS $329.26, SNPS $462.12 at the 11 Nov 2026 close).

### Inferences
- For every private entrant, the entry point "cannot be assessed": there is no price data beyond the round marks above.
- For listed vehicles, the entrant exposure is immaterial to the parent's value. The entry point for gaining exposure to these entrants through them therefore also "cannot be assessed".

### Gaps
- Secondary-market prices.
- Any 2026 down-rounds.
- Valuations for ChipAgents, Cognichip and Normal.

## 8. Closing lists

### What I could not verify
- Bronco's, Voltai's, Rise's and MooresLab's funding.
- ChipAgents' and Cognichip's valuations.
- Siemens–Precision Innovations closing.
- The full text of the Cadence, Synopsys and Siemens agent licence terms.
- The URLs for Siemens's Questa One Agentic Toolkit, The Information's Anthropic report, the Bloomberg Intelligence quote and the MediaTek ChipStack figures.
- Any entrant benchmark claim, independently.
- Harmonic's paying chip customers.
- Open-source sign-off acceptance by any foundry below 130 nm.
- The EuroCDP report's contents.
- DARPA and EU funding levels.
- Japan, Korea and India AI-native DV start-ups.
- The status of ChipAgents' evaluation by Nvidia; the roic.ai account attributing it to Reuters could not be opened.

### Where current evidence contradicts the background views
- "Verification tools own the verdict": largely supported, since entrants drive the incumbents' engines. Two caveats:
  - Agents "declared sign-off" while missing 21–37% of bugs, so the verdict is only as good as the checks given.
  - Proof judges (Harmonic, Lean-based research) and new engines (Hiveware) are emerging outside the incumbents.
- "Seat-priced tools face pressure once agents can drive open-source alternatives": not yet seen in revenue.
  - Cadence grew 22% in Q3 2026.
  - Incumbents are adding consumption charges for agents rather than losing seats.
  - Open-source alternatives lack production PDKs and sign-off below 130 nm.
  - The pressure so far is on share prices (17 Jul 2026), and among entrants that avoid seats: Bronco and Harmonic do, while MooresLab still sells floating licences.
- "The three large vendors keep growing through 2029": no contradiction to date (cross-ref: Cadence FY2026 about +21%; Synopsys FY2027 guide $11.1–11.2B; Siemens EDA led DI software growth).
- "Machine-proved regression checks standard by 2028": no evidence of standard practice as of Nov 2026. Simulation "is still the norm". Only research frameworks and early products (Harmonic CI per commit) exist.

### Sources with dates (full URLs inline above)
- Papers: SE "Putting AI To The Test" (2 Nov 2026); arXiv 2609.05658 (4 Sep 2026), 2603.03175 (3 Mar 2026), 2502.16662 (Feb 2025), 2506.14074 (Jun 2025), 2410.23299 (15 Oct 2024), 2607.16855 (Jul 2026), 2603.08738 (2026); NeurIPS 2026 entries 161609 and 161616.
- Kimi K3: blog (16 Jul 2026); nano-kpu repository (read 12 Nov 2026); Investing.com, TIKR, ts2.tech, Seeking Alpha (17–21 Jul 2026).
- Entrants: ChipAgents (BusinessWire and TheNextWeb, 29 Jul 2026; Crypto Briefing, 14 Oct 2026; site read 12 Nov 2026); Cognichip (SiliconANGLE, 1 Apr 2026; Dealroom, Sep 2026); Bronco, MooresLab and Chipmind sites (read 12 Nov 2026).
- Incumbents and partners: NVIDIA release (26 Jul 2026); ITBrief (2 Jun 2026); Cadence card terms (Jul and Sep 2026); Siemens–Precision Innovations (20 Jul 2026).
- Proof and open source: Harmonic (27 Oct and 3 Nov 2026); IHP PDK, Yosys and cocotb pages (read 12 Nov 2026).
- Cross-ref: Wilson study (8 Sep 2026); TSMC grids (1 Oct 2026); Cadence and Synopsys calls (Feb–Oct 2026).
