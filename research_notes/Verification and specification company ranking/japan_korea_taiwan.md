# Japan, South Korea and Taiwan: verification and specification companies, and foundries (TSMC, Samsung, Rapidus) as certifiers of sign-off tools

Research date: 12 November 2026 (final notes; continuation of an earlier partial pass). Share prices are delayed quotes or closes of 12 November 2026.

Scope: Japan, South Korea and Taiwan only. US vendors, Siemens, China, India, Europe/Israel and the Asian valuation table belong to other researchers. Items marked [CROSS-REF] come from their notes in this folder, with the original source as given there.

Tag key: [PRIMARY] filing or official document (including a company's own results release or presentation); [INDEPENDENT] confirmed by an outside party; [COMPANY CLAIM] stated by the company only; [SECONDARY] press, analyst or data-aggregator report only; [UNVERIFIED] could not be verified; [CALC] my arithmetic on the cited figures; [INFERENCE] my reasoning.

Coverage warning: the shared web-search budget ran out part-way through this pass, after the Korean, Taiwanese design-house, Rapidus and certification searches. I did not route around the limit through other search services. Later items rely on pages already surfaced plus a few direct fetches of official or data pages. Japan's secondary names, Korean start-ups, Taiwan's IP houses, MediaTek and investor-access rules are therefore thin (see the lists at the end).

Corrections:
- CORRECTION (my own checkpoint wording): ASICLAND was labelled a "TSMC value-chain aggregator" and Gaonchips a "Samsung design solution partner". No source opened in this pass confirms either label (the Dealsite article carries TSMC only as a tag). Both are now [UNVERIFIED].
- CORRECTION: StockAnalysis trailing figures for Jedat (revenue JPY 1.59bn, net 97m, P/E 42.8) contradict Jedat's filings. Use the filings (Q7).
- Unresolved discrepancy: Siemens (23 Apr 2026) says Solido is certified on "N3A"; Futurum (24 Sep 2026) says "N3C"; TSMC's grid covers N3C. Both may be true.

## Q1. How do TSMC, Samsung and Rapidus certify sign-off tools, and is certification a barrier to entry?

### Takeaway
TSMC is the decisive "judge of the judges". As of 1 Oct 2026 its public certification grids for A14, A16, N2P, N3C and 3DFabric list only Cadence, Synopsys and Siemens EDA, and the test method, fees and design-kit terms sit behind a customer login. Samsung certifies a slightly wider field (a Chinese SPICE vendor at 3-8 nm). Rapidus has no public certification regime yet; it relies on the same three vendors while open-sourcing AI prediction tools that sit before sign-off.

### Cited Findings
TSMC (Open Innovation Platform, EDA Alliance)
- EDA Alliance members "as of 09/23/2026": Cadence, iROC Technologies, Jedat, Keysight, Lorentz Solution, Primarius, Siemens EDA, Silvaco, SkillCAD, Synopsys, Zuken. Certification grids "As of 10/01/2026" for A14, A16, N2P, N3C and 3DFabric have only three vendor columns: Cadence, Synopsys, Siemens EDA. Text: "TSMC has been conducting full-line EDA Tool Certification Program with major partners including Cadence, Siemens EDA and Synopsys." Categories: physical implementation (APR, custom design), timing and power sign-off, EMIR, physical verification (DRC, LVS, dummy fill), RC extraction, simulators, thermal. Ansys no longer appears (absorbed into Synopsys). [PRIMARY] https://www.tsmc.com/english/dedicatedFoundry/oip/eda_alliance (fetched 12 Nov 2026)
- Same page: no test method, cost or timeline is published; readers are told to log in to TSMC-Online "for more information and download". Status legend: "Certified", "Work in Progress" and, for 3DFabric only, "Certified for Technology Requirement". Reference flows: A14 Mobile/HPC and Custom, 3DFabric design enablement, Analog and RF Design Migration. No public grid for N3, N5, N7 or older; no vendor other than the three appears in any grid; partners such as iROC, Jedat and Silvaco appear only in the member list; per-cell status cannot be read reliably from the page text. [PRIMARY] same URL
- 2026 North America OIP Ecosystem Forum, 23 Sep 2026, Santa Clara: Cadence digital full flow, sign-off and custom/analog flows certified for A16 and A14. Synopsys: A14-certified flows from implementation to sign-off; agentic-AI collaboration with TSMC. Siemens: A14 certification for Calibre nmDRC, nmLVS, xACT and PERC; Solido certified for N3C/A16/A14; Aprisa and mPower A14 work under way; AI DRC-fix agent enabled jointly with TSMC. IC-Link by imec joined the OIP Cloud Alliance (managed cloud, controlled access to advanced TSMC PDKs). Analyst remark: TSMC certifies tools against its rules, but no regime certifies what an autonomous agent did. [SECONDARY] Futurum, 24 Sep 2026 https://futurumgroup.com/insights/tsmcs-oip-forum-turns-agentic-chip-design-demos-into-production-flows/
- Synopsys, 23 Sep 2026: "Certified EDA flows on TSMC A14", with a quote from TSMC's Aveek Sarkar. Synopsys, 22 Apr 2026: RedHawk-SC and Totem expanded from A16 to A14; Totem-SC analog power-integrity sign-off for N2; PathFinder-SC multi-die ESD sign-off for N2; IC Validator enablement "on-going". [PRIMARY company releases with foundry quote; CROSS-REF synopsys.md] https://news.synopsys.com/2026-09-23-Synopsys-and-TSMC-Partner-to-Accelerate-AI-Systems-Innovation-with-Agentic-AI-and-Advanced-Design ; https://news.synopsys.com/2026-04-22-Synopsys-Partners-with-TSMC-to-Power-Next-Generation-AI-Systems-with-Silicon-Proven-IP-and-Certified-EDA-Flows
- Siemens, 22 Apr 2026: Calibre nmPlatform certified for N3, N2, A16 and A14. [CROSS-REF siemens_eda.md]
- What certification means, according to a vendor: tool outputs "match the behavior of real silicon at that node". Solido Simulation Suite is certified for SPICE accuracy on N3A, N2P, A16 and A14, validated against TSMC's own models, and sits in TSMC's A14 Custom Design Reference Flow (reliability-aware simulation: aging, self-heating, safe operating area). No test details or timing are given. [COMPANY CLAIM] Siemens blog, Emma-Jane Crozier, 23 Apr 2026 https://blogs.sw.siemens.com/cicv/2026/04/23/solido-and-ai-powered-eda-tsmc-certification-reference-flows-and-advanced-node-design/
- Cadence FY2025 10-K: Cadence works with foundries on PDKs "to ensure our core EDA products and solutions meet manufacturing sign-off requirements"; named competitors include Altium (Renesas) and Zuken. [PRIMARY; CROSS-REF cadence.md] https://s206.q4cdn.com/597110084/files/doc_downloads/2026/Mar/CDNS-FY-2025-Form-10-K.pdf
- Open tools: Moonshot's Kimi K3 demo (17 Jul 2026) was a single autonomous 48-hour run producing a 4 mm², 100 MHz design on the open Nangate 45 nm cell library with open-source EDA, simulated only. Commentary of 27 Jul 2026: TSMC certifies the three vendors via OIP, and open tools lack advanced PDKs. [SECONDARY; CROSS-REF synopsys.md] https://stockti.com/synopsys-shares-plunge-8-as-moonshot-ai-s-chip-demo-raises-eda-moat-concerns ; https://www.techinvestments.io/p/the-eda-crash-and-the-massive-ai
- Earlier cycles (dates not re-checked in this pass): Synopsys digital and analog flows certified for TSMC N2 (release 25 Sep 2023) [PRIMARY company release] https://news.synopsys.com/2023-09-25-Synopsys-and-TSMC-Collaborate-to-Accelerate-2nm-Innovation-for-Advanced-SoC-Design-with-Certified-Digital-and-Analog-Design-Flows?asPDF=1 ; Synopsys first-pass silicon on N2 and flows certified for A16 and N2P [SECONDARY] https://www.datacenterdynamics.com/en/news/synopsys-announces-first-pass-silicon-success-using-tsmc-n2-process-certifies-eda-flows-for-a16-and-n2p-technologies ; TSMC certified Siemens EDA tools running on AWS for N2/N3 [SECONDARY] https://aws.amazon.com/blogs/industries/tsmc-certifies-siemens-eda-tools-on-aws-for-n2-n3-process-node-technology
- Searches on 12 Nov 2026 found no TSMC N2-or-later certification announced by Keysight, Silvaco or Primarius. [UNVERIFIED as a negative; search results only]

Samsung Foundry (SAFE)
- SAFE Forum US, 28 May 2026: Synopsys, Cadence and Siemens made same-day 2nm announcements. Synopsys: AI-powered digital and analog flows "production-ready" for Samsung's third-generation 2nm-class process. Siemens: Aprisa "fully certified" for Samsung leading-edge nodes; certification under way for the next 2nm generation. Cadence: multi-year collaboration; GPU-accelerated flows certified. [SECONDARY] Futurum https://futurumgroup.com/insights/samsungs-2nm-advance-draws-on-eda-innovation-from-cadence-siemens-and-synopsys/
- Synopsys, 28 May 2026: Totem-SC newly certified on second-generation 2nm and 4nm; quote from Samsung VP Hyung-Ock Kim. [PRIMARY company release with foundry quote; CROSS-REF synopsys.md] https://news.synopsys.com/2026-05-28-Synopsys-Advances-Power-and-Performance-for-AI-and-Multi-Die-Designs-on-Latest-Samsung-Foundry-Processes-at-SAFE-Forum-2026 . Siemens Calibre nmPlatform "fully qualified" by SAFE, 28 May 2026. [CROSS-REF siemens_eda.md]
- SAFE Forum Seoul, 1 Jul 2026, Seocho headquarters, closed event, ~400 attendees. 21 partner booths across EDA, IP, design solution partners (DSP), virtual design partners (VDP) and multi-die (MDI), none named. Speakers: Rebellions (Rebel 100 NPU on Samsung 4nm) and Siemens EDA (Jean-Marie Brunet: "comprehensive support in the areas of yield, design verification, reliability, and packaging"). Also a DTCO strategy, SRAM, Samsung's membership of MOTIE's M.AX Alliance, and an MPW programme for domestic fabless firms. No Korean EDA company named. [SECONDARY] Edaily, 1 Jul 2026 https://en.edaily.co.kr/news/eda202607015207/
- Samsung certifies a vendor that TSMC's grids do not show: Primarius (China) NanoSpice certified for Samsung 3nm/4nm (June 2024), 5nm (Oct 2022) and 8nm (Dec 2021). No TSMC certification found for Primarius, although it is a TSMC EDA Alliance member (23 Sep 2026). [COMPANY CLAIM] https://www.primarius-tech.com/en/aboutus/news/Primarius-NanoSpice-Simulator-Certified-for-Samsung-Foundry-3nm-4nm-Process-Technology.html ; https://www.primarius-tech.com/en/aboutus/news/Primarius-NanoSpice-Simulator-Certified-for-Samsung-Foundry-5nm-Process-Technology.html ; https://www.primarius-tech.com/en/aboutus/news/Primarius-NanoSpice-Simulator-Certified-for-Samsung-Foundry-8nm-Process-Technology.html
- Samsung Catalyst Fund led a US$50m strategic round in the AI-native EDA entrant Normal Computing (25 Mar 2026). [CROSS-REF ai_native_chip_verification_open_source.md]

Rapidus (Japan, private)
- Raads (announced at SEMICON Japan, Dec 2025): seven tools in three groups matching Rapidus's reference flow, released in sequence from FY2026. Rapidus claims 50% shorter design time and 30% lower design cost (an expectation, not a measurement). Raads Generator: LLM-based, specification to RTL optimised for Rapidus 2nm; open source. Raads Predictor: fast PPA estimate from RTL, can produce placement; open source, free, usable with OpenROAD. Raads Manager, Compiler, Optimizer: ML/AI plug-ins for Cadence and Synopsys tools. Raads Navigator and Indicator: LLM-based quality-assurance assistants, also plug-ins for Cadence and Synopsys. Planned: Raads SynthCast System. Models shared through Rapidus's RUMS community. No verification or sign-off tool claimed. [SECONDARY, page text partly garbled] MONOist, 18 Dec 2025 https://monoist.itmedia.co.jp/mn/spv/2512/18/news057_2.html
- Futurum (Brendan Burke, 31 Aug 2026): IIM-1 fab construction complete, tooling installed, process testing under way, wafers moving to build the PDK data set; the PDK "does not yet exist in shippable form". The RAADS predictor, with Cadence's InnoStack AI Super Agent as orchestration core and Rapidus QA agents Navigator and Indicator, would translate a customer's 7/5/4nm design to Rapidus 2nm and forecast PPA; it is slated to launch with the production PDK. "Up to 2X" faster design turnaround is a target the analyst calls unproven. No customer named; no EDA flow certification for Rapidus 2nm mentioned. Futurum calls Rapidus "the first foundry to productize agentic prediction as a design flow" and expects that exclusivity to erode. [SECONDARY] https://futurumgroup.com/?p=95024
- PDK timing conflict: one report says the first 2nm PDK reached early-access customers by Feb 2026 [SECONDARY, low-reliability aggregator] https://business.mammothtimes.com/mammothtimes/article/tokenring-2026-2-6-japans-2nm-moonshot-rapidus-secures-billion-dollar-backing-as-hokkaido-factory-hits-critical-milestones ; Futurum (31 Aug 2026) says not yet shippable; a related headline on a garbled MONOist page (Oct 2026) says about 10 companies have signed PDK licences [UNVERIFIED]. Treat PDK release status as unresolved.
- Funding and customers (MONOist, 2 Mar 2026, on the 27 Feb 2026 announcement): ~JPY 267.6bn new private funding from 32 companies (including the 8 founders) plus ~JPY 100bn government subsidy for FY2025; more than 60 companies and organisations in discussion, mostly overseas (edge, HPC, AI); ~10 had received preliminary design support; PDK licence negotiations progressing; volume production target 2027. [SECONDARY] https://monoist.itmedia.co.jp/mn/spv/2603/02/news062.html
- Rapidus CORE (Collaborative Open Rapid Ecosystem), announced 5 Oct 2026. First initiative: 17 "Design Solution Associates", including AION Silicon, Cadence, GreatAsic, HCLTech, Infinecs, Infosys, MosChip, NSW, Oppstar, Quest Global, SkyeChip, Synopsys, TOPPAN, Wipro and Toshiba Information Systems (three names unreadable on the Japanese page; Toshiba Information Systems per other reports). Expansion to EDA, IP and other categories planned. [SECONDARY] MONOist, 6 Oct 2026 https://monoist.itmedia.co.jp/mn/articles/2610/06/news040.html ; DCD https://datacenterdynamics.com/en/news/japanese-chipmaker-rapidus-to-establish-core-initiative-to-support-semiconductor-design-and-manufacturing ; "17 design partners, zero signed contracts" [SECONDARY, opinion] https://ecosistemastartup.com/rapidus-la-fabrica-japonesa-de-2nm-busca-clientes/
- EDA tie-ups: Synopsys and Cadence 2nm GAA flow deals (2024); Cadence memory and interface IP for backside power delivery; Siemens (June 2025) front-to-back reference flow plus a Calibre-based PDK; Keysight (Aug 2025) for PDK accuracy and fab analytics. [SECONDARY] https://www.eenewseurope.com/en/rapidus-signs-2nm-deals-with-synopsys-cadence/ ; https://evertiq.com/design/2025-06-24-rapidus-partners-with-siemens-to-advance-2nm-semiconductor-design ; https://convergedigest.com/rapidus-taps-keysight-to-sharpen-2nm-pdk-and-boost-yield-at-iim-1/ . No 2026 announcement of a vendor flow "certified" for Rapidus 2nm was found.

### Inferences
- How the barrier works [INFERENCE]: certification is granted tool by tool, node by node and category by category, against silicon data only the foundry holds. A newcomer therefore needs the foundry to spend engineering time on it before customers will trust its verdict. TSMC's own wording ("full-line ... with major partners") and the absence of a fourth vendor from every advanced grid indicate that, for sign-off categories at TSMC's leading nodes, the barrier is closed in practice. Alliance membership (11 firms) is not certification.
- Even within the three, certification is uneven: Siemens Calibre is certified N3 to A14 while Synopsys IC Validator's A14 enablement was still "on-going" in April 2026. This suggests physical-verification sign-off at TSMC remains a Calibre stronghold [INFERENCE from the CROSS-REF items].
- Samsung is more open at the margin (Primarius SPICE), consistent with a challenger foundry that needs ecosystem breadth. Rapidus depends on the incumbents (Calibre-based PDK, Cadence InnoStack inside RAADS) and open-sources only steps before sign-off. Transition (5), foundry certification as a barrier to entry, therefore holds strongly at TSMC, moderately at Samsung, and cannot yet be judged at Rapidus [INFERENCE].
- AI is entering inside the certified incumbents rather than around them: the DRC-fix agent was enabled with TSMC and agentic flows were announced with TSMC. Certification still covers tool outputs, not agent behaviour, which leaves an open question about who certifies an agent's work [INFERENCE from Futurum].
- Customers' sign-off choices follow certification because tape-out risk at N2/A16 falls on them. This is not stated in the sources found [INFERENCE].

### Gaps
- TSMC's test method, duration, fees, and PDK and rule-deck licence terms (behind TSMC-Online). No source found on whether TSMC charges for design kits or rule decks.
- A full list of SAFE-certified tools at SF2/SF2P and below, and Samsung's certification procedure.
- TSMC OIP 2025 forum announcements were not gathered in this pass.
- No evidence found of any Japanese, Korean or Taiwanese EDA vendor holding TSMC certification at any advanced node.

## Q2. Japan: who matters, by sub-segment?

### Takeaway
Japan's listed verification-adjacent companies are small and mostly domestic. Zuken sells PCB and system design plus GENESYS model-based systems engineering (MBSE) for specification. Jedat sells custom and analog layout tools and is a TSMC EDA Alliance member without certification marks. Socionext sells custom SoCs, with NRE at about 20-22% of sales. None owns a sign-off judge. Rapidus is the most consequential Japanese actor for the certification question but is pre-production. The software-verification vendors found (Gaio, TOOL) are private and small; Fixstars does not sell verification.

### Cited Findings
- Market context, ESD Alliance Q2 2026: Japan region revenue US$303.1m (+9.3%; Q1 2026 283.1, -9.9%; Q4 2025 258.5, -18.8%; Q3 2025 264.0, -11.5%). Q2 2026 Japan by category: CAE 100.0, IC physical design and verification 127.0, PCB and MCM 39.7, semiconductor IP 21.9, services 14.5 (US$m). Americas for comparison: CAE 921.5, IC physical design and verification 339.1. [PRIMARY industry association; CROSS-REF market_structure_emulation_vip.md] https://www.prnewswire.com/news-releases/electronic-system-design-industry-posts-5-7-billion-in-revenue-in-q2-2026--esd-alliance-reports-302912151.html
- Chip sign-off and formal tools: no Japanese vendor appears in any TSMC advanced-node certification grid (Q1). Jedat and Zuken are EDA Alliance members only. [PRIMARY] https://www.tsmc.com/english/dedicatedFoundry/oip/eda_alliance
- Zuken (TSE Prime 6947), H1 FY2027/3 (Apr-Sep 2026), published 9 Nov 2026: revenue JPY 23,714m (+21.9%), operating profit 3,687m (+55.5%), net 3,143m. FY forecast raised to revenue 48,500m, OP 7,300m, net 6,100m. H1 product mix: PCB design solutions 11.1%, circuit design solutions 19.5%, IT solutions 28.1% (includes GENESYS MBSE and resale of network-security products by a domestic subsidiary), client services 41.3%. External sales by region: Japan 16,508m, Europe 4,464m, US 1,715m (segment loss 162m), Asia 1,027m. Cash and deposits 29,910m plus securities 6,700m at 30 Sep 2026; net assets 43,188m; total assets 70,488m. [PRIMARY] https://pdf.irpocket.com/C6947/xoA3/DnNg/ah0Z/kwJh.pdf
- Zuken FY2026/3 (published 14 May 2026): revenue 43,101m, OP 5,865m, net 5,400m, R&D 5,445m, operating cash flow 6,131m, equity ratio 61.0%. [PRIMARY] https://pdf.irpocket.com/C6947/WUpy/WHpD/IKZa.pdf
- Zuken: cyberattack on German subsidiary Zuken GmbH found 23 Oct 2026, disclosed 28 Oct 2026; impact under review and not in the forecast. [PRIMARY] https://pdf.irpocket.com/C6947/xoA3/f6yw/FD7E/jvg8.pdf
- Zuken: chairman Makoto Kaneko gifted 200,000 shares to relatives on 19 Oct 2026; his voting stake fell from 10.58% to 9.63%, still the second-largest holder. [PRIMARY] https://pdf.irpocket.com/C6947/xoA3/IjHJ/Jfr8/Bu5L.pdf
- Jedat (TSE Standard 3841), FY2026/3 (non-consolidated): revenue JPY 2,041m (-1.0%), OP 260m, ordinary profit 251m, net 172m; cash 2,744m; no interest-bearing debt. [PRIMARY] https://www2.jpx.co.jp/disc/38410/140120260511521234.pdf
- Jedat H1 FY2027/3 (published 6 Nov 2026): revenue 1,143m (+11.4%), OP 236m (+131.7%), net 164m; gross margin 69.5%; equity ratio 84.2%. FY forecast: revenue 2,200m, OP 290m, net 210m, DPS 40. H1 mix: products 733m, services 220m, solutions 189m; own products 880m vs resale 263m; semiconductor 801m vs flat-panel display 342m; Japan 979m vs overseas 164m. Topics: SX-Meister V21.0; SX-Meister/CTGEN circuit-topology generator shown at DAC (July 2026); exhibited at DVCon Japan 2026. [PRIMARY] https://www.jedat.co.jp/wp-content/uploads/2026/10/Jedat_NewsRelease261106_1JE11-EP-26007.pdf and https://www.jedat.co.jp/wp-content/uploads/2026/11/Kessansetumeikai_Nov202625th_half.pdf (11 Nov 2026)
- Socionext (TSE Prime 6526), H1 FY2027/3 (Apr-Sep 2026), published 28 Oct 2026: net sales JPY 99,423m (+14.0%), operating income 1,668m (-55.7%), net 1,526m; product revenue 77.6bn; NRE revenue 21.8bn (21.9% of sales, +32.9%); R&D 33.8bn; product cost ratio 69.9%; equity ratio 72.8%. FY2026/3: net sales 200.8bn, OI 12.4bn (6.2%), product 161.8bn, NRE 38.3bn (19.1%). FY2027/3 forecast raised to sales 225.0bn, OI 15.5bn, net 10.5bn. Design-win balance JPY 1.51 trillion at FY2026/3. Note in the filing: "R&D cost associated with NRE revenue is recorded as an expense". [PRIMARY] https://www.socionext.com/en/ir/pdf/sn_ir20261028_02e.pdf and https://www.socionext.com/en/ir/pdf/sn_ir20261028_03e.pdf
- Socionext abroad: India's C-DAC 5nm HPC processor programme is "in consortium with Socionext". [CROSS-REF india_and_verification_services.md]
- Gaio Technology (private): sells embedded-software development and verification tools, its own and partners' (unit testing, static analysis, code analysis, shared-variable analysis, virtual-ECU verification, HILS); engineering services (MBD adoption, CI/CD, HILS operation) and outsourcing (in-vehicle security, test-data creation); AI-assisted design review and AI-based test-data creation. 2026 news: SharedVariableChecker2 upgrade (13 Oct 2026); PLAS-Qlite and PLAS-Qlite/V2 upgrades (5 Oct 2026). Functional-safety test reports are offered; ISO 26262 is not named on the page. No financials. [COMPANY CLAIM] https://www.gaio.co.jp/ (fetched 12 Nov 2026)
- TOOL Corporation (private, Tokyo): LAVIS-plus (visual verification, layout viewer, 3D display, schematic display, similar-shape search, image-difference extraction), OASIS-Utility, RSCALC (resistance calculation), MaskStudio (fracturing), plus custom development services. 2026 news: Photomask Japan (19 Feb 2026), PHP-vulnerability notice (23 Oct 2026), Nano Testing Symposium (1 Nov 2026), JEVeC DAY 2026 (9 Nov 2026). No DRC/LVS sign-off claim; no financials. [COMPANY CLAIM] https://www.tool.co.jp/ (fetched 12 Nov 2026)
- Fixstars: performance-engineering services and products (AIBooster, Vega on-premises AI appliance, Amplify quantum platform, Inference Cloud); FPGA, flash-firmware and quantum services; claims "100+ clients with a 99% repeat rate". 2026 news: Macnica partnership on Tenstorrent products (2 Oct 2026); FastMetal GPU inference service (5 Nov 2026). No chip-verification or formal-verification product on the page; listing details not shown. [COMPANY CLAIM] https://www.fixstars.com/en (fetched 12 Nov 2026)

### Inferences
- Japan matters to verification mainly as a buyer (about 5.3% of global ESD revenue in Q2 2026 [CALC: 303.1 / 5,710.9 for the four regions]) and, through Rapidus, as a would-be certifier. Its listed vendors sell mainly at home: Zuken 69.6% of H1 external sales in Japan, Jedat 85.7% [CALC].
- In Japan, IC physical design and verification (US$127.0m) exceeds CAE (US$100.0m), the reverse of the Americas. This is consistent with a Japanese design base weighted toward analog, custom and layout work [CALC; INFERENCE].
- Zuken's GENESYS is the only Japanese product found in the specification and requirements sub-segment; its revenue is not separated from the 28.1% "IT solutions" line [INFERENCE].

### Gaps
- Renesas/Altium in 2026; Japanese formal-methods specialists; Japanese AI-native chip-verification start-ups; other requirements-tool vendors; Japanese software-testing service houses. None was researched because of the search budget.
- Socionext customer concentration, node mix and data-centre share: the presentation PDF returned HTTP 503 twice on 12 Nov 2026. Earlier figures come from the first researcher's reading of it.
- Gaio and TOOL financials and ownership (private; websites give no figures). Fixstars listing and financials not checked.

## Q3. South Korea: who matters, by sub-segment?

### Takeaway
Korea's relevant listed names are design-service houses that sell design labour plus turnkey production at thin or negative margins: Semifive, ASICLAND, Gaonchips and ADTechnology (CoAsia not retrieved). The other is Suresoft Tech, a profitable mid-sized vendor of software testing and verification tools and services for safety-critical industries. No Korean company owns a chip sign-off judge. Samsung's SAFE certifications in 2026 went to the three large vendors (Q1). No dedicated Korean EDA-localisation programme with a budget was found.

### Cited Findings
- Semifive (KOSDAQ 490470), H1 2026 results release dated 14 Aug 2026: revenue KRW 94.7bn (+97% y/y; 78% of FY2025 revenue of KRW 120.9bn); bookings KRW 118.9bn (FY2025 168.4bn); gross margin 30.6% (from 11.9%); operating margin -11.5% (improved 47.0 points). ASIC development (turnkey) revenue KRW 54.1bn; IP revenue (Analog Bits subsidiary) KRW 32.5bn (FY2025 IP 30.5bn); mass-production bookings KRW 42.3bn (Q2 26.7bn, Q1 15.6bn); IP bookings 32.1bn; ~45% of Q2 mass-production bookings from overseas customers. No customers or foundry named; no verification line item; no numeric guidance. [PRIMARY company results release; qualitative statements COMPANY CLAIM] https://en.prnasia.com/releases/global/semifive-accelerates-growth-with-97-yoy-revenue-surge-in-h1-2026-powered-by-asic-turnkey-mass-production-and-ip-544059.shtml
- Semifive Q1 2026: revenue KRW 47.9bn, new orders 55.4bn. [COMPANY CLAIM] https://technode.global/?p=122950 . Broker estimate (Shinhan, 28 Aug 2026): Q3 2026 revenue KRW 51.2bn and OP 1.1bn; Q4 71.0bn and OP 6.4bn. [UNVERIFIED: seen in a search summary only, article not opened]
- ASICLAND (KOSDAQ 445090): Q1 2026 revenue KRW 54.0bn, a quarterly record [SECONDARY] https://www.ddaily.co.kr/page/view/2026051513485783992 . Q2 2026 revenue 59.7bn, of which development (NRE/design services) 43.2bn and mass production ~16.5bn (analyst-derived); Q2 OP 8.0bn including a one-off settlement gain of ~5.0bn (Shinhan estimate; ~3.0bn excluding it); H1 2026 revenue 113.7bn, OP 5.0bn. The CXL development project ended in Q2; loss-making edge-AI projects from 2025 mostly ended. SK hynix eSSD controller design contract raised from ~31.9bn to 41.0bn in Aug 2026 (56.2% of last year's revenue); SD-card controller contract 26.5bn a year; eMMC controller mass supply began in 2026; next-generation eSSD controller expected in mass production in H2 2027, but the contract is "not yet confirmed". Mass-production forecasts: Hana ~30.0bn in H2 2026; BNK 5.4bn (2025), 59.2bn (2026), 129.5bn (2027, ~52% of 2027 revenue). FnGuide 2026 consensus revenue 189.5bn, OP 7.0bn. Q3 2026 broker estimate: revenue ~38.0bn, OP 0.7-1.0bn. [SECONDARY] Dealsite, Kim Ju-yeon, 6 Nov 2026 https://dealsite.co.kr/articles/172222 . Q3 2025: revenue 16.2bn, operating loss 4.5bn. [SECONDARY] https://www.ddaily.co.kr/page/view/2025111709300945080
- Gaonchips (KOSDAQ 399720): H1 2026 report filed 14 Aug 2026. Broker (alphadistill, 28 Jul 2026): a Q3 2026 turnaround is "highly likely" according to the company; 2026E revenue KRW 107.8bn (+78%) after a 37% fall in 2025; 2025 loss-making. [SECONDARY, estimate] https://alphadistill.com/report/2626 . Synopsys Korea page: "Gaonchips strengthens strategic collaboration with Synopsys". [COMPANY CLAIM; date not checked] https://www.synopsys.com/ko-kr/korean/press-releases/gaonchips-strategic-collaboration-with-synopsys.html . Samsung partner status [UNVERIFIED, see corrections].
- ADTechnology (KOSDAQ 200710): trailing revenue KRW 179.82bn, net 2.30bn, gross margin 18.3%, operating margin 2.2%, net debt 9.40bn (12 Nov 2026). [SECONDARY aggregator] https://stockanalysis.com/quote/kosdaq/200710/statistics/
- Suresoft Tech (KOSDAQ 298830): sells software testing and verification automation tools and third-party verification services to automotive, defence, nuclear, rail and aviation customers, using in-house tools and ~20 years' experience. Tools are sold under licence, maintenance and subscription. In automotive it is moving from verification into development, including some next-generation vehicle control software. VERIFAI-A, for automatic testing of AI agents and chatbots, launched April 2026; MOU with Youngchang Robotech on physical-AI robots, July 2026. Revenue: 2023 KRW 63.29bn, 2024 88.80bn, 2025 93.94bn. H1 2026: revenue 46.67bn (+21.5%), OP 2.34bn (H1 2025: loss 1.90bn), net 2.10bn. H1 2026 segments: Vertical AI 16.61bn (+36.8%), Trustworthy AI (AI reliability verification) 1.87bn (+176.4%), Physical AI 1.052bn (from 0.124bn), mission-critical software development 1.817bn. Cash ~24.0bn plus short-term financial products ~17.5bn at 30 Jun 2026; 2025 operating cash flow 17.9bn (2024: 9.5bn); debt ratio ~38.4% (end-2025: 46.8%); no dividends yet; no tools/services split disclosed. [SECONDARY] Economist Korea, 19 Oct 2026 https://economist.co.kr/article/view/ecn202610120051 . Q2 2026 revenue 26.4bn (+23.0%), OP 2.8bn; Q1 2026 revenue 20.2bn, operating loss 0.4bn; FY2025 OP 12.6bn, net 9.6bn. [SECONDARY aggregator] https://etfshopping.com/stock/298830/earnings
- Baum Design Systems (private; PowerBaum power modelling from RTL and netlists): no 2026 news and no Samsung SAFE certification found. DVCon Taiwan 2025 slides claim ~1-2 hours of runtime against 24 hours for a conventional flow, and that "30% error is common" in the conventional approach. [COMPANY CLAIM] https://dvcon-proceedings.org/wp-content/uploads/2.2-20250909_session2.2_baum_DvTw2025.pdf
- Government: the MOTIE M.AX Alliance AI-semiconductor subcommittee met on 15 Jun 2026 (~150 attendees: fabless, foundry, IP, KSIA, KEIT); no EDA-specific item found. [SECONDARY] https://view.asiae.co.kr/article/2026061517051630038 . MOTIE on-device AI chip joint development, KRW 1tn over 5 years (headline, 11 Feb 2026). [SECONDARY, headline only] https://v.daum.net/v/20260211164800551 . KRW 5tn semiconductor fund for materials, equipment and fabless firms. [SECONDARY] https://anysilicon.com/news/south-korea-launches-3-5-billion-semiconductor-fund-to-strengthen-materials-equipment-and-fabless-ecosystem/
- Korea as an EDA buyer: Korea was 13% of Synopsys FY2025 revenue. [PRIMARY; CROSS-REF synopsys.md] https://s201.q4cdn.com/778493406/files/doc_earnings/2025/q4/supplemental-info/Synopsys-Q4-FY2025-Financial-Supplement.pdf
- Filing calendar: Korean Q3 2026 quarterly reports are due by about 14 Nov 2026 (45 days after quarter end), so H1 2026 is the latest filed period on 12 Nov 2026. [INFERENCE from the filing rule]

### Inferences
- Korea's verification relevance sits in services (design houses) and in safety-critical software testing (Suresoft). Samsung Foundry's SAFE is the only Korean "judge", and its 2026 advanced-node marks went to foreign vendors [INFERENCE].
- Suresoft's results are strongly second-half weighted: an H1 2025 loss of 1.90bn against FY2025 OP of 12.6bn implies H2 2025 OP of ~14.5bn [CALC from mixed sources]. Half-year margins understate full-year economics.
- Semifive's H1 2026 mix by the release's lines: development 57.1%, IP 34.3%, remainder ~8.6% (8.1bn, presumably mass production) [CALC; assumes the three lines are exhaustive, which the release does not state].

### Gaps
- Alsemy, Sparrow (Fasoo), CoAsia (aggregator page returned 404), Korean AI-native EDA start-ups: not researched because of the search budget.
- DART/KIND primary filings: a KIND page returned HTTP 403. Q3 2026 results (due 13-14 Nov 2026) not yet available.
- Suresoft's split between tool licences and verification services; its customers; ownership.

## Q4. Taiwan: who matters beyond TSMC?

### Takeaway
Beyond TSMC (the certifier, Q1), Taiwan matters for verification through three design-service houses whose revenue is now dominated by production turnkey: GUC (turnkey ~90% of Q3 2026 revenue), Alchip (production-led; NRE below expectations in Q3 2026) and Faraday (NRE ~8% of Q3 2026). None sells verification tools, and no disclosure found prices verification separately. Andes is loss-making RISC-V IP. eMemory and M31 were not retrieved. No Taiwanese EDA or AI-verification start-up, and no MediaTek AI-verification publication, was found before the search budget ran out.

### Cited Findings
- GUC (TWSE 3443), Q3 2026: revenue NT$18,755m (+117.7% y/y, +35% q/q); gross profit 3,860m (20.58%); operating income 2,551m (13.60%); net income 2,272m; diluted EPS NT$16.93. Q2 2026: 13,897m / GM 21.55% / OPM 12.06% / net 1,555m / EPS 11.59. Q1 2026: 11,448m / 27.20% / 15.93% / net 1,646m / EPS 12.25. Q4 2025: 12,400m / 19.04% / 10.13% / net 1,160m. Q3 2025: 8,613m / 24.22% / 12.25% / net 866.88m. [SECONDARY aggregator, S&P data] https://stockanalysis.com/quote/tpe/3443/financials/income-statement/?p=quarterly . Nine-month 2026 revenue NT$44.099bn [SECONDARY] https://uanalyze.com.tw/articles/7762156585 . Foreign broker: Q3 turnkey revenue +44% q/q, ~90% of revenue (Q2: 83%); gross margin held above 20% thanks to high-margin NRE milestones; the company had guided Q3 NRE down by double digits. [SECONDARY] https://wantrich.chinatimes.com/news/20261102900280-420101 . Q2 2026 summary: turnkey +188% y/y; NRE and IP +11% y/y; H1 2026 revenue NT$25,344m, net NT$3,201m. [SECONDARY] https://quartr.com/events/global-unichip-corp-3443-q2-2026_F9x6NJQY . Analyst 2027 view: Google Axion 4m units, Microsoft Cobalt 200 1.3m units, Tesla AI5 and Horizon automotive; revenue could grow more than 200%; AWS Graviton, Meta and Microsoft Maia 400 accelerators in 2H28. [SECONDARY, analyst estimates] Economic Daily News, 30 Oct 2026 https://money.udn.com/money/story/5607/9846972
- Alchip (TWSE 3661, listed as 世芯-KY), Q3 2026 (call c. 6 Nov 2026): revenue US$819.3m (+~238.9% q/q, +267% y/y); net income ~US$102m (first quarter above US$100m); EPS NT$37.68 (record). Gross margin below 20% (analyst on the call: 18%; Q1 50.18%, Q2 34.84%), attributed to a higher production share and delayed NRE recognition on some projects; the CFO said Q3 NRE was slightly below expectations. Operating income ~US$113.9m (~13.9% margin). HPC 87% of revenue; North America 84% (Q2: 51%); 3nm plus 2nm 80% (Q2: 47%). Q4 2026: another revenue record expected, gross margin close to Q3, full-year gross margin target above 20%. 2027: N3 project revenue "noticeably higher" than 2026; the current chip generation should stay in production for about two years. No NRE amount disclosed. [SECONDARY] UAnalyze, 7 Nov 2026 https://uanalyze.com.tw/articles/4032658624
- Faraday (TWSE 3035), Q3 2026 (investor conference 27 Oct 2026): revenue NT$3.664bn (+10.6% q/q, +13.2% y/y); NRE NT$0.309bn (-31.3% q/q, -37.1% y/y; ~8% of revenue); mass production NT$2.907bn (+19.6% q/q; ~79%); IP NT$0.448bn (~12%). Gross margin 42.5% (Q2 45.2%; Q3 2025 33.2%); operating margin 5.8%; net income to parent NT$0.279bn; EPS NT$1.07. Its first 2nm project is also its largest single NRE award ("tens of millions of USD"): a US customer, Samsung as foundry, 3D DRAM stacking and hybrid bonding, originally planned on 4nm. Design-phase revenue is recognised by milestone, possibly from 1H27. Q4 2026 guide: revenue roughly flat q/q, IP at a record, NRE up, mass production slightly down, gross margin ~45%. 2027: double-digit growth target; CXL controller tape-out Dec 2026. Orders outside China are ~80% of design-win value; the US was the largest NRE contributor in 2026. Intel 18HP design capability with some service orders (not a confirmed major project); UMC at 14/12nm. Broker targets: Japanese broker Buy NT$220, US broker Underweight NT$120, European broker Neutral NT$200. [SECONDARY] StockFeel, 28 Oct 2026 https://www.stockfeel.com.tw/?p=278285 ; Chinatimes, 28 Oct 2026 https://wantrich.chinatimes.com/news/20261028900128-420101
- Andes (TWSE 6533): trailing revenue NT$1.82bn, net loss NT$251.76m, operating margin -21.4%, net debt NT$460.7m; next results 13 Nov 2026. [SECONDARY aggregator] https://stockanalysis.com/quote/tpe/6533/statistics/

### Inferences
- The three Taiwanese houses have become production pass-through businesses for hyperscaler and AI programmes. NRE, where verification labour sits, is now a small, lumpy share of revenue (GUC NRE and IP ~10%, about NT$1.9bn in Q3 [CALC]; Faraday 8.4% [CALC]) [INFERENCE].
- Taiwan's verification "judge" is TSMC itself. The design houses are among the largest users of TSMC-certified flows [INFERENCE].

### Gaps
- eMemory (aggregator page 404), M31, Taiwanese EDA start-ups, AI-native verification start-ups, MediaTek's published AI-for-verification work: not researched because of the search budget.
- MOPS primary filings for GUC, Alchip and Faraday were not opened; Q3 figures are from press and aggregators. GUC's ownership (including any TSMC stake) [UNVERIFIED].

## Q5. Design-service houses: how much revenue is design labour (NRE) against production turnkey, and is verification priced separately?

### Takeaway
At the Taiwanese houses NRE has fallen to about 8-10% of revenue as AI programmes ramp. At Socionext it is about 20%; at the Korean houses it is still most of revenue (ASICLAND ~72% in Q2 2026; Semifive ~57% "ASIC development"). No company found reports verification as a separately priced line: it is bundled into NRE, recognised by project milestone.

### Cited Findings
| Company | Period | NRE / design share | Production / turnkey share | IP | Tag, source |
|---|---|---|---|---|---|
| GUC | Q3 2026 | ~10% ("NRE & IP") | ~90% | inside NRE line | [SECONDARY] https://wantrich.chinatimes.com/news/20261102900280-420101 |
| GUC | Q2 2026 | ~17% | 83% | inside NRE line | [SECONDARY] same |
| Alchip | Q3 2026 | not disclosed; "slightly below expectations" | majority | n/a | [SECONDARY] https://uanalyze.com.tw/articles/4032658624 |
| Faraday | Q3 2026 | 8.4% (NT$0.309bn) | 79.3% (NT$2.907bn) | 12.2% | [SECONDARY; CALC] https://www.stockfeel.com.tw/?p=278285 |
| Socionext | H1 FY2027/3 | 21.9% (JPY 21.8bn) | 78% product (77.6bn) | n/a | [PRIMARY] https://www.socionext.com/en/ir/pdf/sn_ir20261028_02e.pdf |
| Socionext | FY2026/3 | 19.1% (38.3bn) | 161.8bn product | n/a | [PRIMARY] same |
| Semifive | H1 2026 | 57.1% "ASIC development (turnkey)" | ~8.6% implied remainder | 34.3% | [PRIMARY release; CALC] |
| ASICLAND | Q2 2026 | 72.4% (43.2bn) | ~27.6% (~16.5bn, analyst-derived) | n/a | [SECONDARY] https://dealsite.co.kr/articles/172222 |
| Gaonchips | - | not found | not found | - | gap |

- Alchip's NRE share in Q3 2025 was 30-40%, which lifted margins. [UNVERIFIED: search summary only]
- GUC: NRE is recognised by project milestone and carries higher gross margin than turnkey; in Q3 2026 NRE gross margin improved. [SECONDARY] https://money.udn.com/money/story/5607/9846972 ; https://wantrich.chinatimes.com/news/20261102900280-420101
- Socionext expenses the R&D cost associated with NRE revenue, so NRE margins are not visible. [PRIMARY]

### Inferences
- Verification labour is not priced separately at any house examined. It is part of NRE, which buyers pay per project and milestone [INFERENCE from disclosures].
- Per-project NRE pricing at the leading edge is rising even as NRE's share falls. Faraday's largest-ever NRE award came on 2nm, GUC's NRE gross margin improved, and SK hynix raised ASICLAND's design contract by ~29% [CALC: 41.0/31.9]. This complicates the view that verification labour is losing pricing power (see the contradictions list) [INFERENCE].
- Mix shift toward turnkey lowers gross margin (Alchip 50% to 18% in two quarters; GUC 27.2% to 20.6%) but raises operating leverage and absolute profit [CALC; INFERENCE].

### Gaps
- Exact NRE amounts for GUC and Alchip (MOPS filings and investor slides not opened); any house's internal verification headcount or cost; Gaonchips' and ADTechnology's mix.

## Q6. In-depth assessments (quality evidence only, judged independently of share price)

### Takeaway
Of nine companies assessed, none owns a verification judge. The strongest positions are production-volume businesses tied to TSMC-certified flows (GUC, Alchip), small profitable tool vendors with domestic franchises (Zuken, Jedat, Suresoft), and labour-heavy Korean design houses with weak margins (ASICLAND, Semifive). All verdicts below are my provisional judgments.

### Cited Findings and assessments (facts are sourced in Q2 to Q5; repeated only where needed)

#### Socionext (TSE Prime 6526): custom SoC design and supply. Ownership not checked.
- a. Position: sells chips plus design (and implicit verification) labour; owns no judge and uses certified third-party flows. Its asset is a JPY 1.51tn design-win balance [PRIMARY]. Medium-weak.
- b. Lead: no outside share data found. India's C-DAC chose it as consortium partner for a 5nm HPC processor [CROSS-REF].
- c. Revenue model: product revenue (78% in H1) recurs while programmes ship; NRE (21.9%) is milestone labour [PRIMARY].
- d. Financial strength: H1 operating margin 1.7%. The FY forecast implies H2 OI of ~13.8bn on ~125.6bn sales (11.0%) [CALC], a back-end-loaded year. R&D was 34% of H1 sales [CALC]. Equity ratio 72.8% [PRIMARY].
- e. Resilience: steady-growth case, design wins convert; 2028 pause, NRE and new starts fall first; acceleration, constrained by its own R&D capacity [INFERENCE]. Export-control exposure not checked.
- Path forward: transition (5) applies indirectly (it depends on TSMC-certified flows); (7) AI model makers designing their own chips are potential customers [INFERENCE].
- Provisional verdict: partly coherent as a business; not a verification-ranking candidate.

#### Zuken (TSE Prime 6947): PCB, circuit and harness design, GENESYS MBSE. Chairman holds 9.63% (second-largest holder) [PRIMARY].
- a. Position: no chip sign-off judge. GENESYS is a specification tool but its revenue is not separated [PRIMARY]. Medium-weak.
- b. Lead: Cadence's 10-K names Zuken as a competitor [PRIMARY, outside party]. No share data.
- c. Revenue model: client services (largely support and maintenance) are 41.3% of H1 revenue [PRIMARY], indicating a recurring base. Seat-based licensing assumed; not verified.
- d. Financial strength: H1 operating margin 15.5%; FY2026/3 13.6%; R&D 12.6% of revenue; operating cash flow 1.14x net profit [CALC]; JPY 36.6bn cash and securities, no debt [PRIMARY]. The US segment is loss-making [PRIMARY].
- e. Resilience: low exposure to AI capex; Japan 69.6% of external sales [CALC]; the cyberattack at Zuken GmbH is an open risk [PRIMARY].
- Path forward: (6) specification and MBSE could gain if requirements become machine-checkable; no evidence of AI or usage pricing found.
- Provisional verdict: coherent as a niche system-design vendor; not globally significant in verification.

#### Jedat (TSE Standard 3841): custom and analog IC layout tools (SX-Meister), CTGEN circuit-topology generator, display design.
- a. Position: no judge; TSMC Alliance member without certification marks [PRIMARY]. Weak.
- b. Lead: none independent; DAC and DVCon Japan exhibits are company events [COMPANY CLAIM].
- c. Revenue model: own products 77.0% of H1 revenue; resale 23% [CALC].
- d. Financial strength: gross margin 69.5%; H1 operating margin 20.6%; FY2026/3 12.7% [CALC]; equity ratio 84.2%; no debt [PRIMARY].
- e. Resilience: 85.7% Japan; 30% exposure to flat-panel displays [CALC]; micro-cap.
- Path forward: CTGEN (topology generation) is an automation step, transition (1) in miniature.
- Provisional verdict: coherent at micro scale; globally irrelevant.

#### Semifive (KOSDAQ 490470): Korean ASIC design services plus Analog Bits IP. Ownership and listing date not checked.
- a. Position: sells labour and turnkey; Analog Bits IP is silicon-proven IP rather than a judge. Weak-medium.
- b. Lead: revenue +97% in H1 2026 [PRIMARY]; no outside qualification evidence found.
- c. Revenue model: development 57%, IP 34% (recurring-like), production ~9% [CALC].
- d. Financial strength: H1 operating margin -11.5% [PRIMARY]; trailing net loss KRW 39.0bn; net cash 92.5bn [SECONDARY].
- e. Resilience: depends on AI-ASIC starts converting to mass production. A 2028 pause would hit development bookings [INFERENCE].
- Path forward: (1) no tool products; IP is its route out of pure labour.
- Provisional verdict: partly coherent, with an unproven path to profit.

#### ASICLAND (KOSDAQ 445090): Korean design services, controller ASICs for SK hynix and others.
- a. Position: labour-dominant (72% development in Q2) [SECONDARY]. Weak.
- b. Lead: contract raised by SK hynix (a customer's own vote) [SECONDARY].
- c. Revenue model: project revenue; production expected to rise to ~52% of revenue in 2027 (BNK estimate) [SECONDARY].
- d. Financial strength: trailing gross margin 12.2%, operating margin -6.1%, net debt KRW 22.4bn [SECONDARY]; Q2 profit flattered by a one-off ~5bn gain [SECONDARY].
- e. Resilience: high customer concentration (one SK hynix contract equals 56% of 2025 revenue) [SECONDARY]. Memory-cycle exposure.
- Path forward: none toward tools.
- Provisional verdict: not coherent as a verification business; partly coherent as a contract designer if mass production lands.

#### Suresoft Tech (KOSDAQ 298830): Korean software testing and verification tools plus services.
- a. Position: sells compliance-driven testing tools to regulated industries. Safety standards that require verification evidence are a constraint AI cannot remove. No evidence of sound static analysis or machine-checked proof products [INFERENCE]. Medium.
- b. Lead: no independent share or customer evidence found.
- c. Revenue model: licence, maintenance and subscription plus services; no split disclosed [SECONDARY].
- d. Financial strength: trailing operating margin 16.5%, net cash KRW 18.7bn [SECONDARY]; 2025 operating cash flow 17.9bn [SECONDARY]; H2-heavy seasonality.
- e. Resilience: Korean automotive and defence budgets matter more than AI capex [INFERENCE].
- Path forward: (6) its buyer is the regulated OEM or defence agency. (7) It is repositioning to test AI agents (VERIFAI-A), a defence against model makers offering verification themselves. Funded from operating cash; scale small.
- Provisional verdict: partly coherent.

#### GUC (TWSE 3443): Taiwanese ASIC design services and turnkey production. Ownership not verified.
- a. Position: no judge; sells NRE labour plus production. Close TSMC alignment is plausible but unverified.
- b. Lead: Q3 2026 revenue +117.7% y/y [SECONDARY]; analysts name Google, Microsoft, Tesla, Horizon, AWS and Meta programmes [SECONDARY, estimates].
- c. Revenue model: ~90% turnkey (volume-linked) [SECONDARY].
- d. Financial strength: Q3 operating margin 13.6%, net margin 12.1% [CALC]; trailing ROE 48%; net cash NT$9.1bn [SECONDARY].
- e. Resilience: the steady-growth case favours it (CPU and accelerator programmes); a 2028 financing pause would cut turnkey volumes sharply; acceleration is limited by CoWoS and wafer allocation [INFERENCE]. Horizon (China) is an export-control exposure [INFERENCE]. The US "affiliates" rule suspension was set to expire 9 Nov 2026 [CROSS-REF cadence.md]; status not checked.
- Path forward: (5) it benefits from the certification barrier as an incumbent user; (7) model makers' own chips (Microsoft Maia) are its customers.
- Provisional verdict: coherent as a production business; not a verification vendor.

#### Alchip (TWSE 3661): Taiwanese (foreign-incorporated) ASIC design services and production.
- a. Position: as GUC; no judge.
- b. Lead: 3nm plus 2nm is 80% of revenue [SECONDARY]; no named customer.
- c. Revenue model: production-dominant; NRE lumpy [SECONDARY].
- d. Financial strength: Q3 net margin ~12.4% [CALC]; trailing ROE 15.3%; net cash NT$36.9bn [SECONDARY].
- e. Resilience: North America 84% of revenue implies heavy dependence on one or a few programmes [INFERENCE]. Generation life of ~2 years is the company's own estimate [SECONDARY].
- Path forward: as GUC.
- Provisional verdict: partly coherent, because of concentration.

#### Faraday (TWSE 3035): Taiwanese ASIC services, IP and production, working with several foundries (UMC, Samsung, Intel).
- a. Position: owns IP libraries (recurring); NRE labour; no judge. Medium-weak.
- b. Lead: largest-ever NRE award on Samsung 2nm [SECONDARY].
- c. Revenue model: production 79%, IP 12%, NRE 8% [CALC].
- d. Financial strength: operating margin 5.8%; trailing ROE 6.3%; net cash NT$8.7bn [SECONDARY]. Analysts attribute part of the profit to non-operating gains [SECONDARY].
- e. Resilience: falling China share; multi-foundry, so it depends on Samsung's and Intel's certified flows [INFERENCE].
- Path forward: (5) exposed to non-TSMC certification ecosystems.
- Provisional verdict: partly coherent.

### Inferences
- The "labour to tools" transition (1) is not visible at any company assessed. The design houses are instead moving from labour to production volume, which is a different escape from labour pricing [INFERENCE].
- Usage-based pricing (2), formal proof (3) and open-source threats (4) had no company-specific evidence in this region [INFERENCE].

### Gaps
- Return on capital from filings (only aggregator ROE/ROIC used); customer-concentration disclosures from annual reports; ownership for most names.

## Q7. Entry point (valuation and access evidence only, kept separate from quality)

### Takeaway
Taiwan's GUC trades at extreme multiples after a 311% one-year rise (EV/sales ~20x, trailing P/E ~159). Alchip and Faraday are far cheaper per unit of sales, and Korean design houses have fallen 25-47% over a year. Japanese tool vendors trade at mid-teens to high-teens earnings multiples with net cash. Investor-access rules were not verified in this pass.

### Cited Findings (StockAnalysis.com statistics pages, prices delayed, fetched 12 Nov 2026; fundamentals from S&P Global Market Intelligence per the site) [SECONDARY]
| Company (ticker) | Price (12 Nov 2026) | Mkt cap | Trailing P/E | Fwd P/E | EV/sales TTM | 52-week change | Net cash (debt) | URL |
|---|---|---|---|---|---|---|---|---|
| GUC (TPE 3443) | TWD 7,860 | TWD 1.05tn | 159.0 | 63.6 | 19.8 | +311.5% | TWD 9.07bn | https://stockanalysis.com/quote/tpe/3443/statistics/ |
| Alchip (TPE 3661) | TWD 3,675 | TWD 316.8bn | 40.8 | 18.2 | 6.96 | +1.1% | TWD 36.94bn | https://stockanalysis.com/quote/tpe/3661/statistics/ |
| Faraday (TPE 3035) | TWD 178.5 | TWD 46.51bn | 59.1 | 34.0 | 3.13 | +6.9% | TWD 8.71bn | https://stockanalysis.com/quote/tpe/3035/statistics/ |
| Andes (TPE 6533) | TWD 227.0 | TWD 11.50bn | n/a (loss) | 46.1 | 6.57 | -11.8% | (TWD 0.46bn) | https://stockanalysis.com/quote/tpe/6533/statistics/ |
| Socionext (TYO 6526) | JPY 1,809.5 | JPY 317.45bn | 38.9 | 19.0 | 1.42 | -22.2% | JPY 14.66bn | https://stockanalysis.com/quote/tyo/6526/statistics/ |
| Zuken (TYO 6947) | JPY 5,140 | JPY 108.33bn | 16.8 | n/a | 1.51 | +9.6% | JPY 36.61bn | https://stockanalysis.com/quote/tyo/6947/statistics/ |
| Jedat (TYO 3841) | JPY 1,081 | JPY 4.16bn | see note | n/a | see note | -16.3% | JPY 2.25bn (aggregator) | https://stockanalysis.com/quote/tyo/3841/statistics/ |
| Semifive (KOSDAQ 490470) | KRW 12,030 | KRW 409.33bn | n/a (loss) | n/a | 1.95 | n/a | KRW 92.49bn | https://stockanalysis.com/quote/kosdaq/490470/statistics/ |
| ASICLAND (KOSDAQ 445090) | KRW 15,430 | KRW 168.58bn | n/a (loss) | 22.2 | 1.22 | -46.6% | (KRW 22.35bn) | https://stockanalysis.com/quote/kosdaq/445090/statistics/ |
| Gaonchips (KOSDAQ 399720) | KRW 29,750 | KRW 352.80bn | n/a (loss) | n/a | 3.73 | -39.1% | KRW 37.61bn | https://stockanalysis.com/quote/kosdaq/399720/statistics/ |
| ADTechnology (KOSDAQ 200710) | KRW 16,830 | KRW 218.38bn | 95.4 | 7.47 | 1.27 | -25.5% | (KRW 9.40bn) | https://stockanalysis.com/quote/kosdaq/200710/statistics/ |
| Suresoft Tech (KOSDAQ 298830) | KRW 3,390 | KRW 179.78bn | 15.7 | n/a | 1.71 | -28.6% | KRW 18.71bn | https://stockanalysis.com/quote/kosdaq/298830/statistics/ |

- Other aggregator figures (12 Nov 2026). GUC: EV TWD 1.04tn, P/S 19.9, trailing revenue 56.50bn, net 6.63bn, gross margin 21.8%, operating margin 12.9%, ROE 48.4%, yield 0.25%, beta 1.78. Alchip: EV 279.9bn, trailing revenue 42.60bn, net 7.80bn, gross margin 26.9%, operating margin 18.5%, ROE 15.3%, yield 0.94%. Faraday: EV 38.71bn, trailing revenue 12.37bn, net 0.789bn, gross margin 44.2%, operating margin 5.3%, ROE 6.3%, yield 1.01%, -2.99% on the day. Socionext: EV 302.79bn, trailing revenue 213.05bn, net 8.20bn, gross margin 43.7%, operating margin 4.8%, ROE 6.3%, yield 2.76% (JPY 50). Zuken: EV 71.72bn, trailing revenue 47.36bn (consistent with filings), net 6.45bn, gross margin 67.0%, operating margin 15.2%, ROE 15.6%, no debt, yield 2.92%, beta 0.22. Semifive: EV 316.83bn, P/S 2.50, trailing revenue 167.57bn, net -39.04bn, gross margin 25.9%, operating margin -21.6%. ASICLAND: EV 190.93bn, trailing revenue 156.12bn, net -6.80bn, gross margin 12.2%, operating margin -6.1%. Gaonchips: EV 315.19bn, trailing revenue 86.05bn, net -5.47bn, gross margin 2.7%, operating margin -10.6%. ADTechnology: EV 228.21bn. Suresoft: EV 175.20bn, trailing revenue 102.19bn, net 11.40bn, operating margin 16.5%, ROE 11.7%; the aggregator's 99.8% gross margin is an artefact (no cost-of-sales split). Andes: EV 11.96bn, trailing revenue 1.82bn. [SECONDARY] URLs as in the table.
- Jedat note: aggregator trailing revenue 1.59bn, net 97m and P/E 42.8 are inconsistent with the filings and should not be used. Own calculation from filings: market cap / FY2027/3 forecast net 210m = ~19.8x; market cap minus cash of 2,744m (31 Mar 2026) gives EV of ~1.4bn, ~0.65x forecast revenue of 2,200m [CALC]. 3.85m shares; yield 2.78% (JPY 30) [SECONDARY].
- Zuken own calculation: market cap / FY2027/3 forecast net 6,100m = ~17.8x [CALC].
- Near-term events: Semifive Q3 results 13 Nov 2026 and Andes 13 Nov 2026 [SECONDARY, StockAnalysis]; other Korean Q3 reports by ~14 Nov 2026 [INFERENCE]; Zuken GmbH cyberattack impact pending [PRIMARY]; Socionext's H2-loaded forecast [CALC]; Faraday Q4 guide flat and CXL tape-out Dec 2026 [SECONDARY]; Alchip record Q4 expected [SECONDARY]; GUC Q4 revenue +35-40% q/q expected by brokers [UNVERIFIED: search summary only]; the US BIS "affiliates" rule suspension was "currently set to expire on November 9, 2026" [PRIMARY Cadence 10-K; CROSS-REF cadence.md]; status after that date not checked.

### Inferences
- Cycle position: GUC is priced for the 2027-28 hyperscaler programme ramps that analysts describe. Alchip is flat over a year despite a record quarter, which suggests the market discounts its margin compression and concentration. Korean houses are priced for doubt about mass-production conversion. Socionext is down 22% on weak H1 profit [INFERENCE; not a recommendation].
- Peer spread on EV/sales: GUC 19.8x against Alchip 7.0x and Faraday 3.1x for similar business models [SECONDARY data; INFERENCE].

### Gaps
- Multiples against each company's own history (only 52-week change available); ADRs, OTC lines and foreign-ownership limits (Taiwan, Korea, Japan) not verified in this pass and left to the valuation researcher; CoAsia, eMemory and M31 data not retrieved.

## Q8. Conclusion: does any company from these countries belong among the 8-15 that matter most globally, and where is coverage thin?

### Takeaway
Provisionally, no Japanese, Korean or Taiwanese company belongs among the 8-15 most important verification and specification vendors. The one exception to consider is TSMC: it is not a vendor, but it is the certifier whose verdict decides which sign-off tools can be used at the leading edge.

### Cited Findings
- TSMC's grids carry only three vendors (Q1) [PRIMARY]. No regional vendor holds an advanced-node mark (Q1, Q2) [PRIMARY]. The design houses report verification only inside NRE (Q5) [PRIMARY/SECONDARY]. Suresoft (trailing revenue KRW 102bn), Zuken (JPY 47bn) and Jedat (JPY 2bn) are small (Q7) [SECONDARY/PRIMARY].

### Inferences (provisional judgment)
- TSMC: if the ranking includes "who controls the verdict", TSMC qualifies on position (test a: it owns the judge) and on lead (test b: three certified vendors, an Alliance of 11 members). Its financials lie outside this note. Samsung's SAFE is the second certifier, but more permissive and less decisive. Rapidus is not yet a certifier.
- GUC and Alchip matter as large buyers and integrators of certified flows and verification labour, not as verification vendors.
- Zuken's GENESYS is a candidate only for a long list in specification and MBSE. Suresoft is a regional software-verification vendor without outside evidence of a global lead.

### Gaps
- See the three lists below.

### List 1: What I could not verify
- TSMC certification test method, fees, timing, and PDK and rule-deck access terms; whether any non-big-three vendor holds a TSMC advanced-node certification (none found).
- The full Samsung SAFE certified-tool list for SF2 and below; the Seoul SAFE partner names.
- Rapidus PDK release status (conflicting reports); identities of three of the 17 CORE associates.
- Korean Q3 2026 results; DART/KIND filings (HTTP 403); a Korean EDA-localisation programme; Alsemy, Sparrow, CoAsia and Korean AI-EDA start-ups.
- ASICLAND's TSMC status and Gaonchips' Samsung status (corrected to UNVERIFIED).
- Taiwan: MOPS filings; GUC ownership; eMemory, M31, MediaTek AI verification, Taiwanese EDA start-ups.
- Japan: Renesas/Altium 2026, formal-methods specialists, AI-native start-ups; Socionext customer and node detail (PDF HTTP 503).
- Investor-access rules and historical valuation ranges.
- Broker estimates seen only in search summaries (Semifive Q3/Q4, GUC Q4, Alchip Q3 2025 NRE share).

### List 2: Where current evidence contradicts the background view (that tools owning a verdict keep their position while verification labour loses pricing power)
- Per-project prices for labour at the leading edge are rising: Faraday's largest-ever NRE award came on 2nm; GUC's NRE gross margin improved in Q3 2026; SK hynix raised ASICLAND's design contract by ~29% (Q5).
- Labour-plus-production businesses command premium valuations (GUC EV/sales ~20x, ROE ~48%), though the value lies in production, not verification labour (Q7).
- The judge position is less absolute outside TSMC: Samsung certifies Primarius, and Rapidus open-sources pre-sign-off prediction tools usable with OpenROAD (Q1).
- Consistent with the view rather than contradicting it: Korean labour-heavy houses have thin or negative margins (ASICLAND 12% gross; Gaonchips 2.7% gross, possibly an artefact), and NRE's share of revenue is falling at the Taiwanese houses.

### List 3: Sources with dates (publication date; period)
- TSMC EDA Alliance page (members as of 23 Sep 2026; grids as of 1 Oct 2026; fetched 12 Nov 2026) https://www.tsmc.com/english/dedicatedFoundry/oip/eda_alliance
- Futurum, OIP 2026 (24 Sep 2026) https://futurumgroup.com/insights/tsmcs-oip-forum-turns-agentic-chip-design-demos-into-production-flows/
- Futurum, Samsung SAFE 2026 (c. 28 May 2026) https://futurumgroup.com/insights/samsungs-2nm-advance-draws-on-eda-innovation-from-cadence-siemens-and-synopsys/
- Futurum, Rapidus IIM-1 (31 Aug 2026) https://futurumgroup.com/?p=95024
- Siemens blog, Solido and TSMC (23 Apr 2026) https://blogs.sw.siemens.com/cicv/2026/04/23/solido-and-ai-powered-eda-tsmc-certification-reference-flows-and-advanced-node-design/
- Synopsys releases (22 Apr, 28 May, 23 Sep 2026; 25 Sep 2023), URLs in Q1
- Cadence FY2025 10-K (filed early 2026) https://s206.q4cdn.com/597110084/files/doc_downloads/2026/Mar/CDNS-FY-2025-Form-10-K.pdf
- Edaily, SAFE Seoul (1 Jul 2026) https://en.edaily.co.kr/news/eda202607015207/
- Primarius releases (Dec 2021, Oct 2022, Jun 2024), URLs in Q1
- MONOist: Raads (18 Dec 2025), funding (2 Mar 2026), CORE (6 Oct 2026), URLs in Q1
- ESD Alliance Q2 2026 (period Q2 2026) https://www.prnewswire.com/news-releases/electronic-system-design-industry-posts-5-7-billion-in-revenue-in-q2-2026--esd-alliance-reports-302912151.html
- Zuken H1 FY2027/3 (9 Nov 2026), FY2026/3 (14 May 2026), cyberattack (28 Oct 2026), shareholding (Oct 2026), URLs in Q2
- Jedat FY2026/3 (May 2026), H1 FY2027/3 (6 and 11 Nov 2026), URLs in Q2
- Socionext H1 FY2027/3 (28 Oct 2026), URLs in Q2
- Gaio, TOOL, Fixstars websites (fetched 12 Nov 2026)
- Semifive H1 2026 release (14 Aug 2026) https://en.prnasia.com/releases/global/semifive-accelerates-growth-with-97-yoy-revenue-surge-in-h1-2026-powered-by-asic-turnkey-mass-production-and-ip-544059.shtml
- Dealsite, ASICLAND (6 Nov 2026) https://dealsite.co.kr/articles/172222 ; ddaily (15 May 2026; 17 Nov 2025)
- alphadistill, Gaonchips (28 Jul 2026) https://alphadistill.com/report/2626
- Economist Korea, Suresoft (19 Oct 2026) https://economist.co.kr/article/view/ecn202610120051
- UAnalyze, Alchip Q3 2026 (7 Nov 2026) https://uanalyze.com.tw/articles/4032658624 ; GUC https://uanalyze.com.tw/articles/7762156585
- StockFeel, Faraday Q3 2026 (28 Oct 2026) https://www.stockfeel.com.tw/?p=278285
- Economic Daily News, GUC (30 Oct 2026) https://money.udn.com/money/story/5607/9846972 ; Chinatimes (2 Nov 2026) https://wantrich.chinatimes.com/news/20261102900280-420101
- StockAnalysis.com statistics and quarterly pages (fetched 12 Nov 2026), URLs in Q7
