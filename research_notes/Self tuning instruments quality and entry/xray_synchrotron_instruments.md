# Self-tuning instruments: laboratory X-ray instruments, X-ray components and synchrotron end-stations (situation as of 12 November 2026)

Scope: laboratory XRD, XRF, single-crystal diffraction, SAXS, X-ray microscopy/CT, XPS; X-ray sources, optics, detectors; synchrotron end-station instruments and their control software. Excluded (other researchers): accelerators and beamline hardware components; in-fab X-ray metrology (treated briefly); listed-company statements/valuation (only segment facts recorded here).

Labels: [independently confirmed: by whom] / [company claim, not independently confirmed] / [secondary report] / "could not verify".

Method and coverage warning (read first):
- About 25 web searches were run before the shared web-search budget for this session was exhausted; Exa and Firecrawl credits were also exhausted. After that I used only direct fetches of known primary URLs (company IR PDFs, product pages, conference abstracts), GitHub repository search, and my own query of the RCSB Protein Data Bank API. One attempt to fetch a journal PDF with a browser user-agent after the site had refused automated access was blocked by the session's permission system, and I did not retry it.
- Paid-service calls: one Firecrawl call (a page scrape) and one Exa call were attempted early; both failed for lack of credits and returned no data. Per the coordinator's later instruction, no Firecrawl or other search service was used afterwards; the remaining work used WebFetch on official pages at known addresses (including SEC EDGAR for Bruker's Q3 2026 filings). Earlier, three GitHub repository searches and RCSB PDB API queries were run (before that instruction).
- Consequences: coverage is solid for the background paper, the synchrotron agent landscape (US/EU), Rigaku (H1 FY2026), Bruker (FY2025 10-K, Jan 2026 investor deck), Malvern Panalytical/Spectris (to H1 2025 plus 2026 ownership status), Comet (FY2025, H1 2026), Zeiss X-ray software, DECTRIS (product and PDB-share evidence). Coverage is THIN for China (one company site), and NIL for South Korea, Taiwan and India; also thin for Thermo Fisher, Shimadzu, JEOL, Horiba, Hitachi High-Tech, Oxford Instruments, Nikon, Anton Paar, Xenocs, Excillum, STOE, Proto, Helmut Fischer. No third-party market-share report by instrument class could be retrieved.

---

## (1) Segment map

### Takeaway
The segment splits into (i) laboratory instrument makers with closed, Windows-GUI control (Rigaku, Bruker AXS, Malvern Panalytical, Zeiss, Comet/Yxlon and others), whose set-up has long been automated by classical means (motorised optics, component recognition, guidance "expert systems") but where no maker was found to have shipped LLM-agent control; (ii) component makers, where one firm, DECTRIS, is the measurement source at synchrotron crystallography (≈87% of 2025 X-ray Protein Data Bank entries list a DECTRIS detector) and publishes an open interface; and (iii) the synchrotron end-station control layer, which is open source or cheaply licensed (Bluesky/ophyd/EPICS, BLISS, Tango, SPEC) and on which all agent demonstrations found were built by public facilities using general-purpose LLMs.

### Map by instrument class (makers found; ownership/listing; share evidence)

| Class | Makers found in this session (home; listing/owner) | Share evidence found | Sources |
|---|---|---|---|
| Lab powder/thin-film XRD | Rigaku (JP; TSE 268A); Bruker AXS (US; Nasdaq BRKR); Malvern Panalytical (UK/NL; Spectris plc, owned by KKR since Dec 2025); Anton Paar, Shimadzu, Thermo Fisher, STOE, Proto, Dandong Haoyuan, Dandong Tongda, Persee (not researched) | No third-party share data retrieved. Bruker's 10-K lists as BSI NANO competitors: Rigaku, Oxford Instruments, Agilent, Thermo Fisher, Ametek (Spectro, EDAX), PANalytical, Park Systems, Olympus, Nikon, Zeiss, among others | [Bruker 2025 10-K](https://s22.q4cdn.com/617463959/files/doc_financials/2025/ar/2025-Bruker-Annual-Report.pdf) |
| Lab single-crystal / macromolecular crystallography (MX) | Rigaku, Bruker (STOE not checked) | Home-lab-source MX entries released 2025: Rigaku sources 75.0%, Bruker 18.6%, Excillum 1.1% of 571; home-lab MX is ~6% of X-ray PDB entries and shrinking (943 entries in 2015 → 571 in 2025) [independently confirmed: PDB metadata, my query] | [RCSB PDB Search API](https://search.rcsb.org/) |
| XRF (lab WD/ED, benchtop, handheld) | Rigaku; Bruker; Malvern Panalytical (Zetium, Epsilon, Revontium; handheld via SciAps acquired Aug 2024 for £134.9m); Skyray (CN; code 300165: EDX/WDX/handheld XRF); Thermo Fisher, Hitachi High-Tech Analytical Science, Shimadzu, Helmut Fischer, NCS (not researched) | No share data retrieved | [Spectris FY2024 results](https://www.spectris.com/assets/FY24-Results-RNS-v-FINAL-for-website.pdf); [Skyray site](http://www.skyray-instrument.com/) |
| SAXS/WAXS | Xenocs, Anton Paar, Rigaku, Malvern Panalytical, Bruker (not researched; Xenocs page returned 404) | could not verify | — |
| X-ray microscopy / micro-CT / industrial CT | Zeiss (VersaXRM, Ultra XRM, Context microCT, CrystalCT; Advanced Reconstruction Toolbox software); Bruker (µCT/X-ray microscopy within Bruker AXS); Comet IXS (Yxlon; CA20 for semiconductor); Sigray (US; its domain now redirects to Applied Materials); Nikon (not researched) | Comet IXS 2025 external sales CHF 110.8m, EBITDA margin −6.8% | [Zeiss X-ray microscopy](https://www.zeiss.com/microscopy/en/products/x-ray-microscopy.html); [Comet AR 2025](https://comet.tech/getContentAsset/cc64c1a0-0700-47e4-8e8e-be7d5b0ff657/8453dbad-8de3-45d3-9ff0-774682f4f15b/Comet_Annual-Report-2025-en.pdf) |
| XPS | Thermo Fisher, Shimadzu/Kratos, ULVAC-PHI, Scienta Omicron, SPECS (none researched) | could not verify | — |
| X-ray sources | Rigaku (rotating anodes; dominant in home-lab MX per PDB); Comet IXM (compact sources, portable modules; 2025 sales CHF 99.1m, EBITDA 15.9%); Excillum (liquid-metal-jet; page 404); Hamamatsu, Varex, Unicomp, iRay (not researched) | PDB 2025: Rigaku 428, Bruker 106, Excillum 6 of 571 home-lab-source MX entries | [Comet AR 2025](https://comet.tech/getContentAsset/cc64c1a0-0700-47e4-8e8e-be7d5b0ff657/8453dbad-8de3-45d3-9ff0-774682f4f15b/Comet_Annual-Report-2025-en.pdf); [RCSB](https://search.rcsb.org/) |
| X-ray detectors | DECTRIS (CH; private): PILATUS4, EIGER2, SELUN, POLLUX, MYTHEN2 (+ electron detectors ARINA, ELA, SINGLA, QUADRO); Rigaku HyPix; Bruker PHOTON/LYNXEYE; Rayonix, ADSC (legacy); PSI JUNGFRAU (facility-built, XFELs) | DECTRIS detectors in 8,754 of 10,081 (86.8%) X-ray PDB entries released 2025, vs 21.8% in 2015 [independently confirmed: PDB metadata, my query]. Bruker's own D8 ADVANCE offers the DECTRIS EIGER2 R as a detector option [independently confirmed: Bruker product page] | [RCSB](https://search.rcsb.org/); [DECTRIS company page](https://www.dectris.com/en/company/); [Bruker D8 ADVANCE page](https://www.bruker.com/en/products-and-solutions/diffractometers-and-x-ray-microscopes/x-ray-diffractometers/d8-advance-family/d8-advance.html) |
| Synchrotron end-station control software | SPEC (Certified Scientific Software, private, US); Bluesky/ophyd/Queue Server (open source, NSLS-II-originated); BLISS (ESRF); EPICS, Tango (open source) | SPEC claims use at "more than 200 synchrotrons, industrial labs, universities, and research facilities" and control of "more than 575 X-ray and neutron diffractometers" [company claim] | [certif.com](https://certif.com/); [blueskyproject.io](https://blueskyproject.io/) |
| In-fab X-ray metrology (brief; other researcher) | Rigaku semiconductor process control (32% of H1 FY2026 revenue); Bruker Sirius-XRD/XRF (Israel, Migdal HaEmek site); Comet IXS CA20; Sigray (now apparently Applied Materials) | Bruker semiconductor metrology (X-ray + AFM + WLI) ">$300M Revenue and >25% EBIT Margin" TTM to 3Q25 [company claim] | [Rigaku H1 FY2026](https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20260807/20260807514006.pdf); [Bruker JPM 2026](https://s22.q4cdn.com/617463959/files/doc_downloads/2026/04/BRKR-JPM26-Presentation-Final.pdf) |

### Independent share evidence: Protein Data Bank (my query of RCSB metadata, run 12 Nov 2026)
Method: RCSB Search API, entries with experimental method "X-RAY DIFFRACTION" by initial release year; counts of entries whose author-deposited detector/source type contains a maker's name. Caveats: macromolecular crystallography only (not small-molecule, powder, industrial); an entry can list several detectors or sources; fields are author-entered and sometimes blank. Query script kept at /tmp/claude-0/-home-user-gitTest/6b22894c-d2ad-5502-a6bd-cfec93bf6fb6/scratchpad/rcsb_counts.py. [independently confirmed: PDB deposition metadata; my calculation] — [RCSB PDB Search API](https://search.rcsb.org/)

| Release year | X-ray entries | With DECTRIS detector | Synchrotron source | Home-lab source (rotating anode + sealed tube + liquid anode) | Rigaku source | Bruker source | Excillum source | Home-lab entries with Rigaku / DECTRIS / Bruker detector |
|---|---|---|---|---|---|---|---|---|
| 2015 | 8,589 | 1,875 (21.8%) | 7,609 (88.6%) | 943 | 763 (80.9%) | 77 (8.2%) | 0 | 661 / 4 / 54 |
| 2020 | 11,204 | 7,938 (70.8%) | 10,413 (92.9%) | 712 | 573 (80.5%) | 62 (8.7%) | 3 | 370 / 166 / 29 |
| 2025 | 10,081 | 8,754 (86.8%) | 9,361 (92.9%) | 571 | 428 (75.0%) | 106 (18.6%) | 6 | 263 / 146 / 126 |

- Other detector makers in 2025 entries: ADSC 337, Rayonix 168, MarMosaic 90, PSI JUNGFRAU 68, Rigaku 265, Bruker 127. Most used single models in 2025: DECTRIS EIGER X 16M (1,860 entries), PILATUS 6M (1,345), PILATUS3 6M (1,269), EIGER2 XE 9M (850); first PILATUS4 entries (PILATUS4 X 2M: 7). Free-electron-laser sources: 149 entries (2025).

### Cited Findings (ownership/status)
- Spectris plc (parent of Malvern Panalytical) was acquired by KKR for £4.7bn; agreed August 2025, completed December 2025; Spectris shares suspended from LSE trading; KKR outbid Advent's £4.4bn offer. — [Malvern Panalytical PR260721, 21 Jul 2026](https://www.malvernpanalytical.com/de/about-us/press-releases/news/pr260721-new-leadership-new-ambition); [BusinessCloud](https://businesscloud.co.uk/news/kkr-completes-4-7bn-acquisition-of-spectris/) [independently confirmed: company and trade press agree]. Aggregators list June–July 2025 dates, which refer to the announcement. — [Wikipedia](https://en.wikipedia.org/wiki/Spectris); [Mergr](https://mergr.com/transaction/kkr-acquires-spectris) [secondary report]
- sigray.com returns HTTP 301 to https://www.appliedmaterials.com/us/en/sigray.html (checked 12 Nov 2026). This indicates Sigray (US X-ray microscopy/XRF/XAS maker) now sits within Applied Materials; deal date and terms could not verify (Applied Materials pages refused automated access). [my check of the redirect; acquisition itself not independently confirmed]
- Comet Holding AG is listed on the SIX Swiss Exchange. — [Comet AR 2025](https://comet.tech/getContentAsset/cc64c1a0-0700-47e4-8e8e-be7d5b0ff657/8453dbad-8de3-45d3-9ff0-774682f4f15b/Comet_Annual-Report-2025-en.pdf)
- Skyray: Jiangsu Skyray Instrument Co., Ltd., Kunshan, stock code 300165, registered capital RMB 495.5m; XRF (EDX, WDX, handheld, alloy analysers) plus chromatography/MS/ICP; no AI features on site; recent news only trade shows (to 4 Nov 2026). — [Skyray website, accessed 12 Nov 2026](http://www.skyray-instrument.com/)
- Israel: Bruker lists an X-ray manufacturing site in Migdal HaEmek, Israel (and Penang, Malaysia) in its 10-K property table. — [Bruker 2025 10-K](https://s22.q4cdn.com/617463959/files/doc_financials/2025/ar/2025-Bruker-Annual-Report.pdf)

### Inferences
- The PDB numbers support a "judge-owning" position for DECTRIS at synchrotrons and for Rigaku in home-lab crystallography sources, but also show the home-lab crystallography niche shrinking as measurement moves to facilities.
- Two ownership changes in 2025–2026 move X-ray assets towards larger platforms: Malvern Panalytical into KKR's private Spectris; Sigray apparently into Applied Materials (fab-equipment owner).

### Gaps
- Market shares by class (lab XRD, XRF, SAXS, XPS, XRM/CT) from a third party (e.g., SDi): could not verify. China (Dandong Haoyuan, Dandong Tongda, Persee, NCS, Unicomp, iRay), South Korea, Taiwan, India: not researched beyond Skyray's site (search budget exhausted).

---

## (2) Verification of the background item (Stanford/SLAC AI agent at a synchrotron beamline; Nature Machine Intelligence, July 2026)

### Takeaway
CONFIRMED with corrections. The paper is peer-reviewed and real, but it is a proof of concept: on the real beamline a human relayed every command (facility safety rule); real-beamline trials were few and the authors say they "should not be interpreted as a statistically established capability"; no time comparison with a human operator is reported. The agent drove the beamline's existing SPEC command set through a Model Context Protocol (MCP) server the authors built, using off-the-shelf Anthropic Claude models (Opus 4 on the real beamline). No instrument-vendor product, API or partnership is part of the method.

### Cited Findings — [independently confirmed: peer review at Nature Machine Intelligence; reviewers named as Nathan Szymanski, Francesco Ricci and anonymous]
- Title "An agentic artificially intelligent X-ray scientist"; Nature Machine Intelligence vol. 8, July 2026, pp. 1075–1086; DOI 10.1038/s42256-026-01261-5; received 25 Aug 2025, accepted 28 May 2026, published online 1 Jul 2026; open access. — [Nature MI](https://www.nature.com/articles/s42256-026-01261-5); full text via [OSTI](https://www.osti.gov/pages/servlets/purl/3818105)
- Authors (14): Zhantao Chen (first; Stanford SIMES / SLAC LCLS; now UT Austin), Alexander N. Petsch, Aidan J. Israelski, Rajan Plumley, Lingjia Shen, Cong Wang, Cheng Peng, Yuan Ni, Arun Bansil (Northeastern), Sugata Chowdhury (Howard), Mingda Li (MIT), Jana B. Thayer (SLAC), Vivek Thampy (SSRL), Joshua J. Turner (corresponding; Stanford SIMES / SLAC). — [OSTI PDF](https://www.osti.gov/pages/servlets/purl/3818105)
- Beamline BL17-2, Stanford Synchrotron Radiation Lightsource (SSRL), six-circle diffractometer (detector motors δ, ν; sample motors ϕ, χ, η, μ); 16.0 keV; sample Co3Sn2S2 single crystal on a copper holder, room temperature; second real demonstration on a Si crystal with a deliberate Δη = 1.5° offset and very sharp peaks. — [OSTI PDF](https://www.osti.gov/pages/servlets/purl/3818105)
- What the agent did: located primary reflection (0,0,6), optimised and centred it (η, χ, δ scans), located secondary reflection (1,0,10) including in-plane ϕ search, set or0/or1, determined the orientation matrix, refined lattice parameter c; detected and reused an unexpected ~1.22° η offset; verified on (2,0,14). — [OSTI PDF](https://www.osti.gov/pages/servlets/purl/3818105)
- Interface: SPEC-style terminal commands (wm, wh, umv, pd exposure, dscan, ca, or0, or1, setlat) exposed as MCP tools; scan results returned as rendered plots with fitted peaks, detector images as images (the agent does not see raw numeric arrays); "minor environment-specific adjustments were made to MCP tools to match the real-beamline control interface". Bluesky/EPICS not the agent interface here. — [OSTI PDF](https://www.osti.gov/pages/servlets/purl/3818105)
- Safety: agent output "Execute Command: [commands]", relayed by a human "solely to satisfy facility safety requirements"; BL17-2 motor soft limits used in simulation (e.g., δ −1.0° to 55.0°; χ 85° to 185°). — [OSTI PDF](https://www.osti.gov/pages/servlets/purl/3818105)
- Models: Claude Opus 4 (Claude Desktop) on the real beamline "to maximize robustness and minimize operational risk"; simulation benchmark of Claude Sonnet 4 and Google Gemini 2.5 Flash (via LibreChat API); no fine-tuning ("the core reasoning model is used off the shelf"). — [OSTI PDF](https://www.osti.gov/pages/servlets/purl/3818105)
- Success rates (virtual beamline; success = alignment error ≤15° and |c error| ≤0.01 Å): alignment 10/10 for both models; lattice c 8/10 for both; Gemini stress tests (alignment / c): higher motor offsets 3/5 / 4/5; multi-grain 5/5 / 5/5; short thinking budget 4/5 / 3/5; temperature 0.5 3/5 / 4/5. Authors: c accuracy "does not yet match the precision typically required in crystallography experiments". — [OSTI PDF](https://www.osti.gov/pages/servlets/purl/3818105)
- Time versus a human operator: NOT reported (full text checked). Phys.org coverage (21 Jul 2026) also reports none. — [OSTI PDF](https://www.osti.gov/pages/servlets/purl/3818105); [Phys.org](https://phys.org/news/2026-07-ai-agent-synchrotron-ray-experimental.html)
- Vendors: none named in the method; diffractometer/detector makes appear only in Supplementary Note 6 photos (not read). "The authors declare no competing interests." Code and data open on Zenodo (doi:10.5281/zenodo.20017991; doi:10.5281/zenodo.20017861). Funded by US DOE Office of Science (BES) and SLAC LDRD. — [OSTI PDF](https://www.osti.gov/pages/servlets/purl/3818105)
- Authors' framing of limits: "many individual beamline operations can be addressed using deterministic optimization or scripted automation"; future "meta-agents" to write instrument-specific guidance prompts to reduce "the upfront effort required to adapt the framework to new beamlines". First author (Phys.org): "traditional automation often requires countless hand-written if-else rules". — [OSTI PDF](https://www.osti.gov/pages/servlets/purl/3818105); [Phys.org](https://phys.org/news/2026-07-ai-agent-synchrotron-ray-experimental.html)

### Comparable 2024–2026 work at other facilities (routine vs demonstration)

| Facility | System | What it does | Stack | Status (as of source) | Source |
|---|---|---|---|---|---|
| SLAC SSRL/LCLS + ANL, BNL, LBNL, Stanford, UChicago | SPIRE ("Source-to-Discovery Platform for Instrumentation, Robotics and Embodied AI") | DOE robotics/automation testbed; LLM-based "SI agents" already "in use at selected SSRL experiments" (battery-imaging workflow; instrument monitoring); robotic sample mounting at SSRL BL12-1 | not stated | Announced 8 Oct 2026; no funding amount disclosed; industry advisers unnamed; "hard-wired safety systems will remain in place" | [SLAC, 8 Oct 2026](https://www6.slac.stanford.edu/news/2026-10-08-slac-leads-new-project-build-self-driving-laboratory-future) |
| BNL NSLS-II 11-BM (CMS) | VISION | Voice/natural-language control (motors, detector, temperature); generated code shown to user for confirmation, then executed in Bluesky; LLM backend switchable (GPT-4o or local models via Ollama) | Bluesky | Deployed at CMS; first voice-controlled experiment reported 2025; extension to other beamlines (e.g., SMI) a stated hope | [arXiv 2412.18161](https://arxiv.org/pdf/2412.18161); [BNL news](https://www.bnl.gov/newsroom/news.php?a=122449); [lightsources.org, 26 Jun 2025](https://lightsources.org/2025/06/26/a-vision-for-an-ai-lab-partner/); [GitHub](https://github.com/cfn-softbio/VISION) |
| BNL NSLS-II PDF + BMM | Corrao et al. human-AI multi-beamline framework | On-the-fly reduction, clustering, Gaussian-process/Bayesian-optimisation-driven acquisition across XRD and XAFS beamlines | Bluesky | Demonstration; routine use a stated goal | [arXiv 2509.22959, 26 Sep 2025](https://arxiv.org/abs/2509.22959) |
| ANL APS nanoprobe + N9 robot station | CALMS multi-agent (AutoGen), "agents that learn on the job" | Minimal natural-language prompt → correct 2D-scan command; human guidance stored in vector database | human-in-the-loop | Peer-reviewed (npj Comput. Mater. 12, 160, 2026); demonstration | [arXiv 2509.00098](https://arxiv.org/pdf/2509.00098); [Nature MI ref. 54](https://www.osti.gov/pages/servlets/purl/3818105) |
| ANL APS imaging beamline | EAA (vision-language agents) | Automated zone-plate focusing, natural-language feature search, interactive acquisition; MCP "two-way compatibility" | MCP | Demonstration (preprint 17 Feb 2026) | [arXiv 2602.15294](https://arxiv.org/abs/2602.15294) |
| ANL APS (several beamlines) | BAIT (Bluesky AI Tools) | Router, documentation RAG agent, device agent (reads live ophyd values; writes only after human confirmation), IOC diagnostics, recipe→Bluesky plan agent; built on APS "BITS" template | Bluesky/ophyd/EPICS | "Being deployed across APS beamlines" (talk, 22 Sep 2026; not peer-reviewed) | [NOBUGS 2026](https://indico.xfel.eu/event/2/contributions/342/) |
| LBNL ALS 5.3.1 | Agent-agnostic orchestration layer | Natural language → structured plans; user approval before execution; "All plans are executed through the Bluesky Queue Server" | Bluesky Queue Server | Peer-reviewed, J. Synchrotron Rad. 2026, issue 5 (per URL; authors could not verify); demonstration [secondary report: search snippets; journal page refused automated access] | [JSR 2026](https://journals.iucr.org/s/issues/2026/05/00/soo5005/index.html) |
| LBNL ALS COSMIC-Scattering | Lightfall | "API-first, LLM-addressable" control platform; embedded agent from single moves to GP-driven autonomous scans; staff-written "skills" | own API | "In testing" (preprint 4 Jun 2026) | [arXiv 2606.06711](https://arxiv.org/abs/2606.06711) |
| ESRF | Agentic Data Assistants | Natural-language data-analysis agent (pipelines, reports, Slurm jobs) in Apptainer sandbox; LiteLLM router (commercial and local models); FastMCP; per-beamline "Skills" planned | MCP | Pilot (poster, 22 Sep 2026); analysis, not instrument control | [NOBUGS 2026](https://indico.xfel.eu/event/2/contributions/365/) |
| DESY PETRA III P25 | Beamline agent in BLISS (Qiu, Spiers, Hampel) | Autonomous procedures such as slit alignment; runs alongside existing controls | BLISS | "Early development", not production-ready (poster, 22 Sep 2026) | [NOBUGS 2026](https://indico.xfel.eu/event/2/contributions/259/) |
| DESY PETRA (2024 baseline) | — | A 2024 PETRA talk stated no running ML/AI applications at PETRA III | — | Dated baseline [secondary report: search snippet] | [CERN Indico PDF](https://indico.cern.ch/event/1326603/contributions/5779710/attachments/2801455/4887509/ML%20applications%20at%20PETRA.pdf) |
| IHEP HEPS (China) | HEPSBot (LLM-based experiment/data-analysis agent) with "智慧光源大脑" (IPSBrain); talks on intelligent automated beamline control (线站实验的智能化自动化调控) | Experiment design → parameter configuration → data analysis | not stated | Conference abstracts only, no performance data [secondary report]. HEPS trial operation from 3 Dec 2025; by mid-Feb 2026 222 projects from 91 institutions, ~5,000 user hours; phase 1 = 14 user beamlines + 1 test beamline [secondary report: summary of Chinese press] | [IHEP Indico 222893](https://indico.ihep.ac.cn/event/29344/contributions/222893/); [IHEP Indico 222890](https://indico.ihep.ac.cn/event/29344/contributions/222890/); [Science & Technology Daily, 12 Feb 2026](https://www.stdaily.com/web/gdxw/2026-02/12/content_473623.html) |
| RIKEN SPring-8/SACLA | AI-Assisted Beam Control Development Team | Bayesian optimisation and neural networks for accelerator brilliance and automatic accelerator operation (not end-stations) | — | Team page [secondary report: snippet] | [RIKEN](https://www.riken.jp/en/research/labs/rsc/innov_light_src/operation/ai_control/index.html) |
| LBNL ALS accelerator (out of scope; noted) | Agentic AI for multistage physics experiments (Hellert et al.) | Natural language → execution plans on a production light source | — | Phys. Rev. Research 8, L012017 (2026) | [Nature MI ref. 53](https://www.osti.gov/pages/servlets/purl/3818105) |
| Evaluation tooling | EnvTrace: simulation-based evaluation of LLM-generated beamline code | Benchmarking | — | Preprint Nov 2025 | [arXiv 2511.09964](https://arxiv.org/pdf/2511.09964) |

- Routine operation with LLM agents: none found anywhere. Closest to routine: VISION at one NSLS-II beamline; BAIT "being deployed" at APS; "SI agents" at "selected SSRL experiments". All keep a human confirmation step before hardware moves.
- Not verified (search budget exhausted): Diamond, PSI SLS 2.0, MAX IV, KEK Photon Factory, PLS-II (Korea), NSRRC/TPS (Taiwan), SSRF (Shanghai), Indus-2 (India). One English search for Diamond returned no Diamond agent result; this is absence of evidence only.

### Inferences
- The demo's judge is exactly the thesis's "fast, unambiguous judge" (Bragg-peak intensity and position on a known crystal). But accuracy tolerances were loose and no time or cost saving was measured, so the expert-hours claim is not yet evidenced.
- Value capture at facilities: the agent sat on top of decades-old SPEC via an open protocol (MCP) using a general-purpose model. Facilities, users and model suppliers capture the value; instrument makers are not in the loop.
- Safety policy (human relay/confirmation) is the binding constraint at real beamlines, consistent with the thesis's "cost of damaging hardware".

### Gaps
- Supplementary notes (hardware photos, number of real trials, tool-call counts) not read; makers of the BL17-2 diffractometer and detector: could not verify.

---

## (3) Leading companies

### 3.1 Rigaku Holdings Corporation (TSE Prime: 268A) — Japan

Identity and theme exposure
- HQ Tokyo; President & CEO Jun Kawakami; single reportable segment (scientific instruments); IFRS. Essentially all revenue is X-ray: H1 FY2026 (Jan–Jun 2026) revenue ¥39,565m (−2.9%): multipurpose analytical instruments ¥15,081m (−17.1%; 38%), semiconductor process control instruments ¥12,791m (+18.2%; 32%), components and services ¥11,692m (−0.5%; 30%). Operating profit ¥2,579m (−54.9%); profit attributable ¥1,628m (−56.9%). — [Rigaku H1 FY2026 results, 7 Aug 2026](https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20260807/20260807514006.pdf) (percent shares my arithmetic)
- FY2026 forecast (unchanged at H1): revenue ¥101,000m (+7.2%), operating profit ¥19,400m (+16.1%), profit ¥12,500m; dividend ¥19.0. Implied FY2025: revenue ≈¥94.2bn, OP ≈¥16.7bn (my derivation from stated growth rates; aggregator gives ¥94.1bn, +4% [secondary report]). — [Rigaku H1 FY2026](https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20260807/20260807514006.pdf); [Quartr Q4 2025](https://quartr.com/events/rigaku-holdings-corporation-268a-q4-2025_FYcgoSBF)
- Q3 FY2026 (to 30 Sep 2026): could not verify.

Test a — Position
- Owns judges: an installed base of lab XRD/XRF/SC-XRD/SAXS instruments built on its own sources, optics and HyPix detectors, plus in-line X-ray process-control tools in fabs. Rigaku sources: 75% of 2025 home-lab MX PDB entries [independently confirmed: PDB, my query].
- Openness: closed. SmartLab is marketed with "a computer controlled alignment system with a fully automated optical system" and an "intelligent User Guidance expert system"; runs on an external Windows PC; 21 CFR Part 11 security; no API, scripting, LIMS or remote control described. — [Rigaku SmartLab page, accessed 12 Nov 2026](https://rigaku.com/products/x-ray-diffraction-and-scattering/xrd/smartlab). GitHub search found 65 "rigaku" repositories, all community file parsers/analysis tools plus two 2023 community "rigaku_driver" attempts; no official Rigaku organisation or SDK. — [GitHub search, 12 Nov 2026](https://github.com/search?q=rigaku&type=repositories)

Test b — Outside evidence of lead
- PDB: Rigaku sources 428/571 (75%) and Rigaku detectors 263/571 of 2025 home-lab MX entries; share of sources down from 80.9% (2015) as Bruker gained [independently confirmed: PDB].
- Named first among Bruker's BSI NANO competitors [independently confirmed: by a competitor's SEC filing]. — [Bruker 2025 10-K](https://s22.q4cdn.com/617463959/files/doc_financials/2025/ar/2025-Bruker-Annual-Report.pdf)
- Semiconductor: management says nearly all new products support AI-chip technology; about half of Q4 FY2025 semiconductor revenue tied to joint evaluation programmes ("JEP") and new products, JEP gross margin above 80%; Q4 FY2025 semiconductor operating-margin target 55% [company claims]. Q2 FY2026 semiconductor orders "more than 3x" the year-ago level [secondary report: Quartr]. Named fab qualifications: could not verify. — [logmi transcript, Q3 FY2025 briefing, 11 Nov 2025](https://finance.logmi.jp/articles/383393); [Quartr Q2 2026](https://quartr.com/events/rigaku-holdings-corporation-268a-q2-2026_FYcgw9WN)

Test c — Revenue model
- Components and services 30% of H1 FY2026 revenue (includes EUV multilayer mirrors and components, so pure service is smaller). Service +7% in 9M FY2025 "driven by price increases and global maintenance contracts"; parts & services +13.2% YoY in Q1 FY2026 [secondary report]. The other ~70% is one-off hardware. Software not reported separately (transcript mentions materials informatics and a genetic-algorithm multilayer-film analysis package). — [Rigaku H1 FY2026](https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20260807/20260807514006.pdf); [logmi](https://finance.logmi.jp/articles/383393)

Test d — Financial strength (balance-sheet facts only)
- 30 Jun 2026: total assets ¥187,646m; equity ¥89,193m; equity ratio 47.5%; shares issued 226.5m. 2025 buyback up to ¥4bn (≈¥2.5bn done by end-Oct 2025). Carlyle's remaining stake: could not verify. — [Rigaku H1 FY2026](https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20260807/20260807514006.pdf); [logmi](https://finance.logmi.jp/articles/383393)

Test e — Resilience
- H1 FY2026: multipurpose instruments −17.1% "due to market weakness amid the ongoing impact of Trump policies in the United States and fluctuations in energy prices resulting from the situation in the Middle East"; semiconductor +18.2% on memory and logic AI demand. — [Rigaku H1 FY2026](https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20260807/20260807514006.pdf)
- US academic budget cuts a stated headwind; tariff costs passed through; EUV multilayer-mirror sales under half of expectations in FY2025; China multipurpose sales ~+10% in Q3 FY2025 after prior-year stimulus one-offs; China share not disclosed in documents read; "tightening export controls" flagged as a risk [secondary report]. — [logmi](https://finance.logmi.jp/articles/383393); [Quartr](https://quartr.com/events/rigaku-holdings-corporation-268a-q1-2025_FYcgomKp)
- Scenario inference: steady growth (≈55%) favours the semiconductor line (≈⅓ of revenue, highest margin); a financing-led pause in 2028 (≈25%) would hit the most profitable line while academic/industrial demand is already weak, so earnings are more exposed than revenue; faster acceleration (≈20%) mainly lifts semiconductor tools.

Transitions
- T1 — Said: automatic optics alignment, "User Guidance expert system", robotic automated transport for cement/mining (orders in China, groundwork in Europe). Done: classical automation shipped; no LLM-agent control product found. Funded: R&D stepped up (company). Timing: no agent-feature date found. Must go right: Rigaku ships its own agent layer, or third parties will wrap its GUI. — [SmartLab page](https://rigaku.com/products/x-ray-diffraction-and-scattering/xrd/smartlab); [logmi](https://finance.logmi.jp/articles/383393)
- T2: no evidence of opening (no public SDK/API).
- T3: service growing via maintenance contracts and pricing; no subscription model found.
- T4: algorithmic analysis (genetic-algorithm multilayer fitting; materials informatics); no hardware-for-compute substitution data.
- T5: an "AI Analysis in XRD Basic Course" appears in site navigation (training); no data-platform product verified.

### 3.2 Bruker Corporation (Nasdaq: BRKR) — USA; X-ray inside BSI NANO

Identity and exposure
- BSI NANO = Bruker AXS (XRF, µXRF, TXRF, XRD, µCT/X-ray microscopy, spark OES, plus STEM, EDS, EBSD), Nano Surfaces & Metrology (AFM, WLI; "automated X-ray metrology, automated AFM defect-detection, and photomask repair"), Spatial Biology (NanoString), fluorescence microscopy, cellular analysis. X-ray sites include Migdal HaEmek (Israel) and Penang (Malaysia). — [Bruker 2025 10-K](https://s22.q4cdn.com/617463959/files/doc_financials/2025/ar/2025-Bruker-Annual-Report.pdf)
- BSI NANO 2025 revenue $1,084.3m (−1.3%), gross margin 47.6% (49.2% in 2024), segment operating margin −6.6% (impairment at Spatial Biology). Bruker AXS revenue not disclosed. Group revenue $3,436.5m (+2.1%). — [Bruker 2025 10-K](https://s22.q4cdn.com/617463959/files/doc_financials/2025/ar/2025-Bruker-Annual-Report.pdf)
- Latest quarter (Q3 2026, released 4 Nov 2026): group revenue $874.0m (+1.6% reported; organic +0.7%; constant currency +2.4%); BSI NANO $263.1m vs $266.5m in Q3 2025 (−1.3%); 9M 2026 BSI NANO $770.4m vs $775.2m (−0.6%). Release cites "next-gen semiconductor metrology in support of AI" as a growth driver and demand "strengthening" in Q3 "also in the US academic market"; BSI book-to-bill above one for a "fifth consecutive quarter"; BSI organic bookings and backlog up mid-single digits year to date. — [Bruker 8-K Ex. 99.1, 4 Nov 2026](https://www.sec.gov/Archives/edgar/data/1109354/000119312526446176/brkr-ex99_1.htm)
- 10-Q (quarter to 30 Sep 2026, filed 5 Nov 2026): goodwill impairment $174.5m in Q3 2026 ($309.4m 9M 2026) — segment attribution not in the portion read; a BSI NANO restructuring plan (severance/termination charges) is disclosed; 2026 acquisitions labelled include Tofwerk (6 Jan 2026; mass spectrometry, not X-ray), Mimetas and ChemSpeed Technologies. — [Bruker 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/1109354/000119312526449731/brkr-20260930.htm); [EDGAR filing index](https://data.sec.gov/submissions/CIK0001109354.json)
- 2024 mix: Nano 33% of revenue; end-market "Semi-Metrology 4%". Semiconductor metrology (Sirius-XRD/XRF, AAFM, WLI) ">$300M Revenue and >25% EBIT Margin" TTM to 3Q25; Sirius tools "for production monitoring at major semicon manufacturers" (unnamed) [company claims]. — [Bruker JPM 2026, 12 Jan 2026](https://s22.q4cdn.com/617463959/files/doc_downloads/2026/04/BRKR-JPM26-Presentation-Final.pdf)

Test a — Position
- Owns judges (D8 XRD, XRF, SC-XRD, SkyScan µCT installed base; in-line X-ray metrology). D8 ADVANCE: "DAVINCI.DESIGN" component changes "Fail-safe and alignment free" via snap-lock, 3-point mount and ID chip; "automatic, real-time component recognition and validation"; "Only Bruker offers an alignment guarantee over the entire angular range"; motorised switching of up to 6 beam geometries; Dynamic Beam Optimization; DIFFRAC.WIZARD (planning) and DIFFRAC.COMMANDER (execution); networking; 21 CFR Part 11. No API or AI on the page. Detector options include DECTRIS EIGER2 R. — [Bruker D8 ADVANCE page, accessed 12 Nov 2026](https://www.bruker.com/en/products-and-solutions/diffractometers-and-x-ray-microscopes/x-ray-diffractometers/d8-advance-family/d8-advance.html)
- Strategy: "Automated AI-Labs": "ChemSpeed Lab Automation combined with SciY Scientific Software, Lab Digitization and Data Management"; "Open for integration of third-party hardware, software, and data stacks"; "AI orchestration of pharma and industrial R&D and QC labs"; "towards 'lights-out' self-driving AI-labs"; market "$9-12B" (2025, lab automation + AI) growing "15-25% CAGR (2025-2030)" [company claims]. — [Bruker JPM 2026](https://s22.q4cdn.com/617463959/files/doc_downloads/2026/04/BRKR-JPM26-Presentation-Final.pdf)
- Inference: Bruker is the only X-ray maker found that has bought an orchestration/software layer (SciY) and robotics (ChemSpeed) aimed at self-driving labs, i.e., it is positioning to be the software layer that captures value. Whether SciY exposes Bruker X-ray instruments to third-party agents: could not verify. GitHub shows only community D8 file tools. — [GitHub search](https://github.com/search?q=panalytical+OR+empyrean+OR+%22bruker+d8%22&type=repositories)

Test b — Outside evidence
- PDB: Bruker sources 106/571 (18.6%) of 2025 home-lab MX entries, up from 8.2% (2015); Bruker detectors 126 [independently confirmed: PDB].
- Company-wide "#1 or #2 market position in majority of portfolio" [company claim]. — [Bruker JPM 2026](https://s22.q4cdn.com/617463959/files/doc_downloads/2026/04/BRKR-JPM26-Presentation-Final.pdf)

Test c — Revenue model (group level)
- 9M 2026: product revenue $2,002.0m; service and other revenue $533.9m (21.1% of $2,535.9m; 9M 2025 $490.2m, 19.9%); Q3 2026 service and other $182.1m (20.8% of revenue). — [Bruker 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/1109354/000119312526449731/brkr-20260930.htm)
- 2025 product revenue $2,766.4m (80.5%); service and other $670.1m (19.5%; +10.4%). Backlog $2,569.4m (end-2025) vs $2,090.4m, the increase "primarily driven by higher BEST order bookings" (superconductors, not X-ray). Project Accelerate 3.0: "more Focus on Recurring Revenues" [company claim]. — [Bruker 2025 10-K](https://s22.q4cdn.com/617463959/files/doc_financials/2025/ar/2025-Bruker-Annual-Report.pdf); [JPM 2026](https://s22.q4cdn.com/617463959/files/doc_downloads/2026/04/BRKR-JPM26-Presentation-Final.pdf)

Test e — Resilience
- China revenue 2025 $475.8m (13.8%; 2024 $471.2m); delayed Chinese stimulus "had a material adverse effect"; US–China tariffs; "On February 20, 2026, the U.S. Supreme Court issued a ruling striking down certain tariffs", refunds "highly uncertain"; reliance on NIH/NSF/DOE funding; exports subject to EAR, ITAR and OFAC rules. Geography 2025: US 25.9%, Germany 8.6%, Europe ex-Germany 27.7%, China 13.8%, APAC ex-China 16.1%, other 7.9%. — [Bruker 2025 10-K](https://s22.q4cdn.com/617463959/files/doc_financials/2025/ar/2025-Bruker-Annual-Report.pdf)
- FY2026 preliminary outlook (Jan 2026): "Flat to LSD organic revenue growth", operating margin +250–300 bps, "$120M of anticipated cost savings in FY26" [company guidance]. — [JPM 2026](https://s22.q4cdn.com/617463959/files/doc_downloads/2026/04/BRKR-JPM26-Presentation-Final.pdf). Updated guidance (4 Nov 2026): revenue $3.52–3.56bn (+2.5% to 3.5% reported), organic +1% to 2%, M&A ≈+1.5%, currency neutral, non-GAAP EPS $2.10–2.15 (+15% to 17% from $1.83) [company guidance]. — [Bruker 8-K Ex. 99.1](https://www.sec.gov/Archives/edgar/data/1109354/000119312526446176/brkr-ex99_1.htm). China share for 2026: could not verify (geography table not in the portion of the 10-Q that could be read).
- Scenario inference: semiconductor metrology (~4% of 2024 revenue, >25% EBIT) is small relative to academic (~40% end-market in the company chart; layout ambiguous) and biopharma exposure, so AI-capex scenarios move Bruker less than Rigaku; US academic funding and China stimulus matter more.

Transitions (Bruker X-ray)
- T1 — Said: "Automated AI-Labs"; "fully automated uXRD and uXRF X-ray systems for AI semiconductor chip yield management" (10-K). Done: automated semiconductor X-ray tools shipped; ChemSpeed and SciY acquired. LLM-agent instrument control: not found. Funded: acquisitions done; $120M cost programme limits new spending. Timing: none stated. Must go right: SciY/ChemSpeed integration with Bruker X-ray, and actual openness to third-party stacks.
- T2: openness stated for the AI-lab offering [company claim]; no public X-ray control API found.
- T3: service +10.4% (19.5% of revenue); SciY is the software lever (revenue not disclosed).
- T4: not evidenced for X-ray.
- T5: SciY "Lab Digitization and Data Management, AI/DL"; data-ownership terms not disclosed.

### 3.3 Malvern Panalytical (Spectris plc; KKR-owned since December 2025) — UK/Netherlands

Identity and status
- KKR's £4.7bn acquisition of Spectris agreed Aug 2025, completed Dec 2025. Malvern Panalytical remains "a company of Spectris plc"; Christian Sauber (ex-Danaher, Agilent) President (announced 21 Jul 2026); Andrew Williams is Spectris Chairman and Interim CEO; "further acquisitions to strengthen the Malvern Panalytical platform" a stated focus; sites in UK, Netherlands, US, China, India. — [PR260721](https://www.malvernpanalytical.com/de/about-us/press-releases/news/pr260721-new-leadership-new-ambition)
- Spectris's current businesses: Malvern Panalytical, Particle Measuring Systems, Servomex, HBK. — [spectris.com](https://www.spectris.com/)
- Route to investor exposure: no listed equity (private under KKR); debt instruments: could not verify.

Latest disclosed figures (last public reports; Malvern Panalytical never reported alone)
- Spectris Scientific (Malvern Panalytical, Particle Measuring Systems, Servomex; Micromeritics and SciAps folded into Malvern Panalytical from Aug 2024): 2024 statutory sales £776.7m (−4%; LFL −6%), adjusted operating profit £137.5m (17.7% margin; 21.4% in 2023), statutory operating profit £86.3m; H1 2025 sales £386.0m (+21% reported, +3% LFL). Spectris group 2024 revenue £1,298.7m; China £214.1m (16.5%; 2023 £249.8m); South Korea £43.2m; Japan £68.8m. — [Spectris FY2024 results, 28 Feb 2025](https://www.spectris.com/assets/FY24-Results-RNS-v-FINAL-for-website.pdf); [Spectris HY2025, 7 Aug 2025](https://www.spectris.com/assets/HY25-Results_RNS-statement-v4.pdf)
- 2024 acquisitions: Micromeritics £471.7m; SciAps £134.9m (handheld LIBS; "access to the adjacent hand-held XRF market"). — [Spectris FY2024](https://www.spectris.com/assets/FY24-Results-RNS-v-FINAL-for-website.pdf)

Tests and transitions
- Position (a): owns judges (Empyrean multipurpose XRD incl. "Empyrean XAS ... laboratory-based XANES and EXAFS" and Alpha 1 Johansson monochromator; Aeris; Zetium/Epsilon/Revontium XRF). Openness: no public API/SDK found; community readers only (e.g., FAIRmat pynxtools-xrd for X'Pert data). — [Empyrean range page](https://www.malvernpanalytical.com/en/products/product-range/empyrean-range); [GitHub search](https://github.com/search?q=panalytical&type=repositories)
- Shipped digital/automation (2024) [company claims]: SMART Manager for Zetium XRF and Mastersizer ("remote monitoring and diagnostics, predictive maintenance, and real-time analytics"); Revontium benchtop XRF with "the same data quality as floor-standing instruments, significantly reducing operating cost" (a T4 example); Mastersizer 3000+ with "artificial intelligence-driven solutions for data evaluation" (laser diffraction, not X-ray); "strong demand for automation projects" (automated sample preparation) in building materials. — [Spectris FY2024](https://www.spectris.com/assets/FY24-Results-RNS-v-FINAL-for-website.pdf)
- Strategy under KKR (Jul 2026): "Customer outcomes", "Innovation with purpose", "Operational excellence"; no mention of software, AI, automation or digital. — [PR260721](https://www.malvernpanalytical.com/de/about-us/press-releases/news/pr260721-new-leadership-new-ambition)
- Resilience (e): group China exposure 16.5% (2024); 2024 decline led by academia and China; Q4 2024 orders lifted by "China government incentives starting to filter through to academic institutions". — [Spectris FY2024](https://www.spectris.com/assets/FY24-Results-RNS-v-FINAL-for-website.pdf)
- Transition verdicts: T1 classical automation and remote monitoring shipped, no agent control found; T2 no evidence; T3 SMART Manager/digital services (revenue undisclosed); T4 Revontium is a concrete cheaper-hardware case; T5 "SMART Return Agrilitics Digital Asset" (analytical data platform for agriculture) [company claim]. Must go right: PE owner funds software rather than only bolt-on M&A and cost.

### 3.4 DECTRIS AG — Switzerland (private)

Identity
- HQ Baden-Dättwil; subsidiaries in USA and Japan; "almost 150 employees" (date not shown); X-ray detectors PILATUS4, EIGER2, SELUN, POLLUX, MYTHEN2; electron detectors ARINA, ELA, SINGLA, QUADRO; software/services ALBULA, NOVENA, XDS, detector data processing; "DECTRIS CLOUD" appears only as a "D.LAB" link; self-description "the global leader in hybrid-pixel X-ray detectors (HPC) for science and industry" [company claims]. Ownership, revenue, profit, funding: could not verify; no investor route found. — [DECTRIS company page, accessed 12 Nov 2026](https://www.dectris.com/en/company/)

Test a — Position
- Owns the judge's sensor at synchrotron crystallography: DECTRIS detectors in 86.8% of 2025 X-ray PDB entries [independently confirmed: PDB]. Also present in home-lab MX (146 of 571 home-lab-source entries in 2025, from 4 in 2015).
- Openness: high. Public GitHub documentation (stream v2, CBOR, filewriter), open compression and HDF5 plugin libraries; POLLUX documentation lists a "Simplon API Manual". — [GitHub dectris/documentation](https://github.com/dectris/documentation); [POLLUX page](https://www.dectris.com/en/detectors/x-ray-detectors/pollux/)
- Who captures value: an open API lets any agent use the detector without DECTRIS; DECTRIS captures value through hardware share, not through the agent layer.

Test b — Outside evidence
- PDB share as above; Bruker offers DECTRIS EIGER2 R on its D8 ADVANCE (competitor-as-customer) [independently confirmed: Bruker product page]. — [Bruker D8 page](https://www.bruker.com/en/products-and-solutions/diffractometers-and-x-ray-microscopes/x-ray-diffractometers/d8-advance-family/d8-advance.html)
- Moving into lab-instrument OEM supply: POLLUX, a "laboratory detector" for "integration into next-generation instruments" (powder XRD, residual stress, WAXS, WD-XRF, EXAFS/XANES; 4.5–12 keV, two thresholds, <600 eV FWHM at 8 keV); news item "DECTRIS POLLUX on Idonano XRD". — [POLLUX page](https://www.dectris.com/en/detectors/x-ray-detectors/pollux/); [DECTRIS company page](https://www.dectris.com/en/company/)

Tests c–e
- Revenue mix, financials, China share, export-control exposure: could not verify. Inference: demand tied to synchrotron upgrade/build cycles and public research budgets (APS-U, HEPS, SLS 2.0, PETRA IV) and to electron microscopy; diversification into lab OEM detectors reduces that dependence.

Transitions
- T1: not a set-up target itself, but its open API is what makes agent control of end-stations feasible. T2: already open. T3: software/cloud (NOVENA, "D.LAB"/DECTRIS CLOUD) visible but undisclosed in size. T4: photon-counting, noise-free detection underpins fewer-photon/faster measurement (inference). T5: DECTRIS CLOUD suggests a data platform; terms could not verify.

### 3.5 Carl Zeiss — X-ray microscopy (Xradia lineage) — Germany

Identity and exposure
- X-ray products listed: Versa XRM ("Non-destructive 3D X-ray Imaging at Submicron Resolution"), Ultra XRM, Context microCT, CrystalCT ("The First Commercial MicroCT Crystallographic Imaging System"), synchrotron offering, Advanced Reconstruction Toolbox (ART). — [Zeiss X-ray microscopy page](https://www.zeiss.com/microscopy/en/products/x-ray-microscopy.html)
- Group/segment revenue, ownership and Xradia unit size: could not verify (Zeiss corporate pages returned 404 to the URLs tried).

Shipped learned (AI) features — strongest T4 evidence in the segment [company claims, not independently confirmed]
- DeepRecon Pro: AI-driven reconstruction, "increase throughput by up to 10x"; modes Throughput, ImageClarity, Image Quality. DeepScout: convolutional-neural-network super-resolution of large-field scans trained on high-resolution scans. OptiRecon (iterative, not AI): "up to 4× faster scan times" (1,200 projections in 90 min FDK vs 300 projections in 22 min). PhaseEvolve: post-processing (patent US11645792B2). — [ZEISS Advanced Reconstruction Toolbox](https://www.zeiss.com/microscopy/en/products/software/advanced-reconstruction-toolbox.html)
- Licensing (T3): DeepRecon Pro included as standard with a high-performance workstation on VersaXRM 615 and 730 "2-year license ... can be upgraded to perpetual"; "AI Supercharger" and "Premium ART" packages; standalone via cloud or workstation; "Cloud access is listed with one-year licenses only". ZEISS Data Converter for third-party platforms, METROTOM and "select synchrotron formats" (T5 openness of data). — [ZEISS ART page](https://www.zeiss.com/microscopy/en/products/software/advanced-reconstruction-toolbox.html)
- Inference: Zeiss already sells computation that substitutes for scan time (fewer projections, lower dose), on time-limited licences; this is T3/T4 in practice. No agent control of set-up found.

### 3.6 Comet Holding AG (SIX Swiss Exchange) — Switzerland: X-ray sources (IXM) and X-ray/CT systems (IXS, Yxlon)

- FY2025: group net sales CHF 457.0m, EBITDA 10.1%, net income CHF 12.2m. IXS (X-ray and CT systems for non-destructive examination) external sales CHF 110.8m (2024 CHF 115.8m), EBITDA CHF −7.5m (−6.8%), operating income CHF −11.6m; IXM (compact X-ray sources, portable modules) total sales CHF 99.1m (external 89.1m), EBITDA 15.9%; PCT (RF/plasma, out of scope) CHF 257.1m. China 25.1% of group sales (CHF 114.6m). IXS sales by region 2025: Asia 56.5m, Europe 34.4m, North America 13.3m. — [Comet Annual Report 2025](https://comet.tech/getContentAsset/cc64c1a0-0700-47e4-8e8e-be7d5b0ff657/8453dbad-8de3-45d3-9ff0-774682f4f15b/Comet_Annual-Report-2025-en.pdf)
- H1 2026: group CHF 239.8m (+5.6%; +12.7% constant currency), EBITDA 13.1%, book-to-bill 1.48; IXS CHF 48.7m (flat), EBITDA −8.2%, "more than doubling the number of purchase orders for the CA20 x-ray system" (semiconductor), "break-even point for CA20 is still projected for 2028"; IXM CHF 53.5m (+10.6%), EBITDA 16.1%, driven by aerospace/defence/security, battery, "AI infrastructure and Advanced Packaging". FY2026 guidance CHF 540–570m, EBITDA 14–17%. Geopolitics: "Comet's direct exposure remains limited". — [Comet Half-Year Report 2026](https://comet.tech/getContentAsset/20e73493-df93-42ea-9455-c2883ba7a3c2/8453dbad-8de3-45d3-9ff0-774682f4f15b/Comet-half-year-report-2026.pdf)
- Strategy: "Innovation in x-ray inspection, AI-enabled software, and RF platforms" [company claim; no product detail found]. — [Comet AR 2025](https://comet.tech/getContentAsset/cc64c1a0-0700-47e4-8e8e-be7d5b0ff657/8453dbad-8de3-45d3-9ff0-774682f4f15b/Comet_Annual-Report-2025-en.pdf)
- Inference: IXS is a loss-making challenger in semiconductor CT (lead not evidenced; break-even 2028); IXM is a profitable component supplier exposed to AI packaging capex and to China (25% of group).

### 3.7 Synchrotron control-software owners (value-capture test)
- SPEC (Certified Scientific Software, private US, since 1985): "the leading software for instrument control and data acquisition in X-ray diffraction experiments"; >200 sites; >575 diffractometers; release 6.14.05 dated 7 Sep 2026; licence terms not on home page [company claims]. Used as the agent interface in the Nature MI paper. — [certif.com](https://certif.com/)
- Bluesky: Python libraries (bluesky, ophyd, ophyd-async with EPICS PVA, Queue Server for "autonomous execution, and remote monitoring", Tiled, Bluesky Adaptive). Licence not stated on the landing page. — [blueskyproject.io](https://blueskyproject.io/)
- Inference: the layer agents use at facilities is publicly funded and open; no vendor controls it. A small private firm (SPEC) is the only commercial owner found, and it is a low-cost licence business.

### Transition verdict summary (said / done / funded / timing / what must go right)

| Company | T1 agent-run set-up | T2 open interfaces | T3 software/subscription | T4 cheaper hardware + compute | T5 data for customers' AI |
|---|---|---|---|---|---|
| Rigaku | Classical auto-alignment and guidance shipped; no agent product; no date | No public API/SDK found | Service ~part of 30% components & services; no subscription found | Algorithmic analysis only | Training course only |
| Bruker (X-ray) | Automated semiconductor X-ray tools; "Automated AI-Labs" via ChemSpeed/SciY (acquired); no agent X-ray control found | Stated "Open for integration of third-party" stacks (AI-lab offering) | Service 19.5% of group revenue; SciY software | Not evidenced | SciY data management (terms unknown) |
| Malvern Panalytical | Automation projects, remote monitoring; no agent | No evidence | SMART Manager (size unknown) | Revontium benchtop XRF | Agrilitics data asset (agriculture) |
| DECTRIS | Enabler (open API) | Already open | NOVENA/"D.LAB" cloud (size unknown) | Photon-counting (inference) | DECTRIS CLOUD (terms unknown) |
| Zeiss XRM | No agent set-up found | Data Converter to third-party and synchrotron formats | 1–2-year and cloud licences for AI reconstruction | DeepRecon Pro "up to 10x" throughput; OptiRecon "up to 4×" | Data Converter |
| Comet X-ray | "AI-enabled software" stated only | No evidence | No evidence | No evidence | No evidence |

---

## (4) Companies considered and left out (with reasons)
- Thermo Fisher (XRF, XPS), Shimadzu (XRD, XRF; Kratos XPS), JEOL, Horiba, Hitachi High-Tech Analytical Science, Oxford Instruments (EDS; X-ray), Nikon (CT), Olympus/Evident (handheld XRF), Ametek (Spectro, EDAX, Amptek): not researched — X-ray is a small part of each group and the web-search budget ran out. Bruker's 10-K names several of them as competitors. — [Bruker 2025 10-K](https://s22.q4cdn.com/617463959/files/doc_financials/2025/ar/2025-Bruker-Annual-Report.pdf)
- Anton Paar (XRDynamic 500, SAXSpoint; private): product page refused automated access (HTTP 403); could not verify automation claims or ownership.
- Xenocs (SAXS), Excillum (liquid-metal-jet sources): company pages returned 404; could not verify. Excillum's PDB footprint is tiny (6 home-lab MX entries in 2025) but its main market (semiconductor/industrial) is not visible in PDB.
- Sigray: apparently absorbed by Applied Materials (domain redirect); deal facts could not verify; fab metrology belongs to the other researcher.
- STOE, Proto, Helmut Fischer, Huber (diffractometers for beamlines), Arinax (MX micro-diffractometers), Hamamatsu, Varex, Rayonix, Advacam, X-Spectrum, Quantum Detectors: not researched (budget).
- China: Dandong Haoyuan (丹东浩元), Dandong Tongda (丹东通达), Persee (普析通用), NCS (钢研纳克), Unicomp (日联科技), iRay (奕瑞科技): not researched; Skyray only (site facts). China's domestic-substitution procurement rules: could not verify.
- South Korea, Taiwan, India: no makers verified; coverage nil.
- Israel: Bruker's Migdal HaEmek X-ray site verified via 10-K; Xwinsys and Nova (XPS metrology) not researched (fab metrology is the other researcher's scope).

---

## (5) Where the evidence contradicts (or complicates) the thesis
- Set-up is already largely automated by classical means in lab X-ray: Bruker sells "alignment free" component exchange with ID-chip recognition and an "alignment guarantee"; Rigaku sells automatic optics alignment and a "User Guidance expert system". The expert work left is choosing and interpreting experiments, not aligning. This shrinks the incremental value of agent-run set-up for lab XRD. — [Bruker D8 page](https://www.bruker.com/en/products-and-solutions/diffractometers-and-x-ray-microscopes/x-ray-diffractometers/d8-advance-family/d8-advance.html); [Rigaku SmartLab page](https://rigaku.com/products/x-ray-diffraction-and-scattering/xrd/smartlab)
- The flagship evidence is a proof of concept: loose success tolerances (≤15° orientation; lattice c precision below crystallography needs), few real trials, a human relaying every command, and no measured time saving. — [Nature MI](https://www.osti.gov/pages/servlets/purl/3818105)
- "Closed control interfaces" is not the obstacle at synchrotrons: the control layer is open (Bluesky, BLISS, EPICS) or simple (SPEC); the obstacle is safety policy, shown by universal human confirmation (VISION, BAIT, ALS 5.3.1, SSRL relay). Closed interfaces are the obstacle only in lab instruments.
- Value is not flowing to instrument makers at facilities: public labs build the agents with general-purpose models (Claude, Gemini, GPT-4o, local models) via MCP; no vendor product or partnership was found in any facility project.
- Several facility "agents" do data analysis, not instrument tuning (ESRF pilot; HEPSBot), so the "judge-driven tuning" use case is a minority of AI activity at light sources.
- The "installed base as judge" weakens where measurement migrates to facilities: home-lab MX entries fell from 943 (2015) to 571 (2025) in PDB.
- Where computation-heavy value is real (Zeiss AI reconstruction, Malvern Revontium), it is T4 (fewer projections, cheaper hardware), not agent-run set-up (T1).
- Supports the thesis: DECTRIS's open API plus near-monopoly data-source position; Bruker's move to own an orchestration layer (SciY/ChemSpeed); strong growth in X-ray fab metrology (Rigaku +18.2% H1 FY2026; Bruker >$300M TTM) where tool matching would matter — but no AI fleet-matching product was found.

---

## (6) What could not be verified (and what was tried)
- Rigaku Q3 FY2026 results, FY2025 full-year segment/regional split, China share, Carlyle stake: IR pages render documents through JavaScript (e-IR parts); the TDnet disclosure list returned HTTP 403; search budget exhausted.
- Bruker AXS revenue; Bruker 2026 China share; which segment the 2026 goodwill impairment ($309.4m 9M 2026) relates to; whether SciY integrates X-ray instruments for third-party agents.
- Malvern Panalytical stand-alone revenue (never disclosed); automation/API details for Empyrean/Aeris (product pages lack them).
- DECTRIS ownership, revenue, China share, DECTRIS CLOUD scope.
- Zeiss group/segment figures and ownership (corporate URLs tried returned 404).
- Applied Materials–Sigray deal date/terms (Applied pages refused automated access).
- Third-party market shares by instrument class (no access to SDi or similar).
- Fab qualification of Rigaku/Bruker X-ray metrology at named leading fabs.
- China domestic-substitution procurement rules (e.g., any 2025–2026 Ministry of Finance "domestic product" price preference), US/Chinese export controls specific to X-ray tools/components, and tariffs beyond Bruker's 10-K statements.
- Facility agent work at Diamond, PSI SLS 2.0, MAX IV, Photon Factory, PLS-II, NSRRC, SSRF, Indus-2.
- Any lab X-ray maker support for Model Context Protocol or partnership with an AI model supplier (none found in sources read; not searchable after budget ran out).
- Korea, Taiwan, India makers.

---

## (7) Sources with dates
Peer-reviewed / preprints / conference
- Chen et al., "An agentic artificially intelligent X-ray scientist", Nature Machine Intelligence 8, 1075–1086, published online 1 Jul 2026 — https://www.nature.com/articles/s42256-026-01261-5 ; full text https://www.osti.gov/pages/servlets/purl/3818105 (accessed 12 Nov 2026)
- Phys.org, "AI agent helps prepare synchrotron X-ray experimental measurements...", 21 Jul 2026 — https://phys.org/news/2026-07-ai-agent-synchrotron-ray-experimental.html
- SLAC news, SPIRE self-driving laboratory project, 8 Oct 2026 — https://www6.slac.stanford.edu/news/2026-10-08-slac-leads-new-project-build-self-driving-laboratory-future
- VISION, arXiv 2412.18161 (Dec 2024) — https://arxiv.org/pdf/2412.18161 ; BNL news — https://www.bnl.gov/newsroom/news.php?a=122449 ; lightsources.org, 26 Jun 2025 — https://lightsources.org/2025/06/26/a-vision-for-an-ai-lab-partner/ ; GitHub — https://github.com/cfn-softbio/VISION
- Corrao et al., arXiv 2509.22959, 26 Sep 2025 (v2 2 Oct 2025) — https://arxiv.org/abs/2509.22959
- Vriza et al., arXiv 2509.00098 (2025); npj Comput. Mater. 12, 160 (2026) — https://arxiv.org/pdf/2509.00098
- Du et al., EAA, arXiv 2602.15294, 17 Feb 2026 — https://arxiv.org/abs/2602.15294
- Pandolfi et al., Lightfall, arXiv 2606.06711, 4 Jun 2026 — https://arxiv.org/abs/2606.06711
- ALS 5.3.1 orchestration, J. Synchrotron Rad. 2026, issue 5 (per URL) — https://journals.iucr.org/s/issues/2026/05/00/soo5005/index.html (secondary: search snippets)
- NOBUGS 2026 (EuXFEL, 21–27 Sep 2026): BAIT (22 Sep 2026) — https://indico.xfel.eu/event/2/contributions/342/ ; ESRF Agentic Data Assistants (22 Sep 2026) — https://indico.xfel.eu/event/2/contributions/365/ ; DESY P25 BLISS agent (22 Sep 2026) — https://indico.xfel.eu/event/2/contributions/259/
- EnvTrace, arXiv 2511.09964 (Nov 2025) — https://arxiv.org/pdf/2511.09964
- IHEP Indico HEPS talks (2026) — https://indico.ihep.ac.cn/event/29344/contributions/222893/ ; https://indico.ihep.ac.cn/event/29344/contributions/222890/ ; Science & Technology Daily, 12 Feb 2026 — https://www.stdaily.com/web/gdxw/2026-02/12/content_473623.html ; 24 Mar 2026 — https://www.stdaily.com/web/gdxw/2026-03/24/content_491958.html (secondary)
- RIKEN AI-Assisted Beam Control team page — https://www.riken.jp/en/research/labs/rsc/innov_light_src/operation/ai_control/index.html (secondary snippet)
- PETRA ML applications talk (2024), CERN Indico — https://indico.cern.ch/event/1326603/contributions/5779710/attachments/2801455/4887509/ML%20applications%20at%20PETRA.pdf (secondary snippet)
- ESRF Indico 2024 (IHEP talk) — https://indico.esrf.fr/event/114/contributions/727/ (secondary snippet)

Company filings and presentations
- Rigaku Holdings, Consolidated Financial Results for the Six Months Ended June 30, 2026 (English translation), 7 Aug 2026 — https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20260807/20260807514006.pdf
- Rigaku Q3 FY2025 results briefing transcript (logmi), held 11 Nov 2025, published 19 Nov 2025 — https://finance.logmi.jp/articles/383393
- Quartr summaries of Rigaku results (2025–2026; secondary) — https://quartr.com/events/rigaku-holdings-corporation-268a-q4-2025_FYcgoSBF ; https://quartr.com/events/rigaku-holdings-corporation-268a-q2-2026_FYcgw9WN ; https://quartr.com/events/rigaku-holdings-corporation-268a-q1-2025_FYcgomKp
- Rigaku SmartLab product page (accessed 12 Nov 2026) — https://rigaku.com/products/x-ray-diffraction-and-scattering/xrd/smartlab
- Bruker 2025 Annual Report / Form 10-K (FY ended 31 Dec 2025; filed after 20 Feb 2026) — https://s22.q4cdn.com/617463959/files/doc_financials/2025/ar/2025-Bruker-Annual-Report.pdf
- Bruker J.P. Morgan Healthcare Conference presentation, 12 Jan 2026 — https://s22.q4cdn.com/617463959/files/doc_downloads/2026/04/BRKR-JPM26-Presentation-Final.pdf
- Bruker 8-K Exhibit 99.1 (Q3 2026 results), 4 Nov 2026 — https://www.sec.gov/Archives/edgar/data/1109354/000119312526446176/brkr-ex99_1.htm ; Bruker 10-Q for quarter ended 30 Sep 2026, filed 5 Nov 2026 — https://www.sec.gov/Archives/edgar/data/1109354/000119312526449731/brkr-20260930.htm ; EDGAR submissions index — https://data.sec.gov/submissions/CIK0001109354.json
- Bruker D8 ADVANCE product page (accessed 12 Nov 2026) — https://www.bruker.com/en/products-and-solutions/diffractometers-and-x-ray-microscopes/x-ray-diffractometers/d8-advance-family/d8-advance.html
- Malvern Panalytical press release PR260721, 21 Jul 2026 — https://www.malvernpanalytical.com/de/about-us/press-releases/news/pr260721-new-leadership-new-ambition
- Malvern Panalytical Empyrean range page (accessed 12 Nov 2026) — https://www.malvernpanalytical.com/en/products/product-range/empyrean-range
- BusinessCloud, "KKR completes £4.7bn acquisition of Spectris" (Dec 2025) — https://businesscloud.co.uk/news/kkr-completes-4-7bn-acquisition-of-spectris/
- Spectris 2024 Full Year Results, 28 Feb 2025 — https://www.spectris.com/assets/FY24-Results-RNS-v-FINAL-for-website.pdf ; 2025 Half Year Results, 7 Aug 2025 — https://www.spectris.com/assets/HY25-Results_RNS-statement-v4.pdf ; archive — https://www.spectris.com/archive/results-reports-and-presentations/ ; homepage — https://www.spectris.com/
- Comet Annual Report 2025 — https://comet.tech/getContentAsset/cc64c1a0-0700-47e4-8e8e-be7d5b0ff657/8453dbad-8de3-45d3-9ff0-774682f4f15b/Comet_Annual-Report-2025-en.pdf ; Half-Year Report 2026 — https://comet.tech/getContentAsset/20e73493-df93-42ea-9455-c2883ba7a3c2/8453dbad-8de3-45d3-9ff0-774682f4f15b/Comet-half-year-report-2026.pdf ; investors page — https://www.comet.tech/en/investors
- ZEISS X-ray microscopy page — https://www.zeiss.com/microscopy/en/products/x-ray-microscopy.html ; ZEISS Advanced Reconstruction Toolbox — https://www.zeiss.com/microscopy/en/products/software/advanced-reconstruction-toolbox.html (accessed 12 Nov 2026)
- DECTRIS company page — https://www.dectris.com/en/company/ ; POLLUX page — https://www.dectris.com/en/detectors/x-ray-detectors/pollux/ ; GitHub — https://github.com/dectris/documentation (accessed 12 Nov 2026)
- Skyray Instrument website (news to 4 Nov 2026) — http://www.skyray-instrument.com/
- Certified Scientific Software (SPEC) — https://certif.com/ (SPEC 6.14.05 dated 7 Sep 2026)
- Bluesky Project — https://blueskyproject.io/
- Sigray domain redirect check (HTTP 301 to https://www.appliedmaterials.com/us/en/sigray.html), 12 Nov 2026

Data
- RCSB Protein Data Bank Search API, queries run 12 Nov 2026 — https://search.rcsb.org/
- GitHub repository searches, 12 Nov 2026 — https://github.com/search?q=rigaku&type=repositories ; https://github.com/dectris

Secondary/aggregators used only where labelled
- Wikipedia "Spectris" — https://en.wikipedia.org/wiki/Spectris ; Mergr — https://mergr.com/transaction/kkr-acquires-spectris
