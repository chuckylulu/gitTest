# Specification and requirements tools worldwide: who writes and owns the specifications, and can AI write them well enough to be trusted?

Research date: 12 November 2026 (all web checks on this date unless stated). STATUS: FINAL (continuation of an earlier partial pass; all facts from that pass are kept below, reorganised).

Tag key: [PRIMARY] filing, paper or official document; [INDEPENDENT] confirmed by an outside party; [COMPANY CLAIM] stated by the company and not confirmed by any outside party; [SECONDARY] press or analyst report only; [UNVERIFIED] could not verify; [CALC] my arithmetic from cited figures; [JUDGMENT] my provisional judgment.

Method note: the earlier pass found the shared WebSearch budget (200 calls across all agents) exhausted and then used only direct fetches of known URLs. In this pass Firecrawl and Exa were out of credits. WebSearch worked for about 20 queries and then hit the same shared limit again. After that, only direct fetches of known primary URLs were used, with no search-engine queries. Coverage of September to November 2026 news is therefore thinner than intended, especially for interface standards bodies, Asian requirements vendors and private-company financials. Synopsys, Cadence, Siemens (including Polarion and Defacto's integration), Ansys SCADE inside Synopsys, the model makers (including AWS Kiro in depth), proof start-ups and regional specialists are covered by sibling notes in this folder and appear here only briefly.

## 1. Map of the specification and requirements segment worldwide

### Takeaway
The segment splits into two parts. The first is owners of "judges": architecture specifications with compliance suites (Arm's ACK, RISC-V's Sail model and emerging certification), interface compliance programmes (USB-IF and others), and foundry rule decks backed by foundry tool certification. The second is seat- or time-licensed authoring tools: register and SoC specification automation (Arteris, Agnisys, and Defacto, now owned by Siemens); requirements and ALM tools (IBM DOORS, PTC Codebeamer, Jama, Dassault, Altium/Renesas Valispace, Flow Engineering); and model-based design (MathWorks, dSPACE, Vector). AI-era spec-driven development is arriving mostly as free or open-source workflows (GitHub Spec Kit, P/PeasyAI, TLA+ tools) or usage-priced services (Kiro, Harmonic, Certora), not as new seat-priced tools.

### Cited Findings

**(i) Hardware specification automation and the Accellera/IEEE formats**
- Arteris (NASDAQ: AIP) has three businesses. It sells network-on-chip interconnect IP on 2-3 year licences recognised rateably, plus per-unit or percent-of-revenue royalties. It sells SoC integration automation software (for example CSRCompiler) on 1-3 year time-based licences. It sells hardware-security verification software (from Cycuity) on 1-3 year time-based licences [PRIMARY] — [Arteris 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0001667011/000162828026071154/aip-20260930.htm). Arteris acquired Cycuity on 14 Jan 2026 [PRIMARY] — same 10-Q.
- Agnisys (private, US/India) has these recent news items:
  - 14 Oct 2026: partnership with Axiomise pairing IDS-NoC NoC generation with nocProve formal verification.
  - 23 Jul 2026: DAC 2026 showcase of IDS-AI, IDS-NoC and DFT automation ("Agentic AI").
  - 19 Jun 2025: IDesignSpec Suite v9 and IDS-FPGA.
  - Named customers: iCatch (Jun 2025), Etched (Dec 2024), Wacom (Nov 2023), The Six Semiconductor and IDEX Biometrics. It joined the Arm Partner Program in Aug 2024.
  - The news page gives no funding, ownership or headcount [COMPANY CLAIM] — [Agnisys news](https://www.agnisys.com/news/).
  - An undated blog says iSpec.ai turns English assertions into SystemVerilog Assertions, and that uploaded specs are processed on Agnisys's private servers, not public AI back ends [COMPANY CLAIM] — [Agnisys blog](https://www.agnisys.com/blog/ai-fuels-the-next-generation-of-specification-automation/).
  - It exhibited at VLSID 2026 in Pune, 5-7 Jan 2026 — [Agnisys](https://www.agnisys.com/agnisys-at-vlsid-conference-2026/).
- Defacto Technologies (France) is now part of Siemens. Siemens announced the acquisition in a blog dated 21 Jul 2026, covering SoC Compiler, IP-XACT plus RTL assembly, and Arm and RISC-V SoCs [PRIMARY, acquirer] — [Siemens blog](https://blogs.sw.siemens.com/digital-design-creation-platform/2026/07/21/siemens-acquires-defacto-technologies-transforming-soc-design-with-powerful-re-use-and-assembly-automation-technology/).
  - Customer case: L&T Semiconductor Technologies (16 Jul 2026) [COMPANY CLAIM] — [Defacto](https://defactotech.com/news/503-defacto-s-soc-compiler-drastically-improved-productivity-of-l-t-semiconductor-technologies).
  - Its AI layer is "in production for over a year" and "used daily by thousands of designers across many of the top 20 semiconductor companies" [SECONDARY, company-sourced] — [SemiWiki, 12 Aug 2026](https://semiwiki.com/eda/defacto-technologies/372101-boost-front-end-soc-design-with-defactos-ai-powered-tool/).
- Accellera standards are the shared specification formats:
  - The Clock and Reset Domain Crossing (CDC/RDC) Standard 1.0 was approved for release; press release 2 Mar 2026 [PRIMARY] — [Accellera](https://www.accellera.org/news/press-releases/427-accellera-approves-clock-and-reset-domain-crossing-standard-1-0-for).
  - Functional Safety Language 1.0 was approved [SECONDARY] — [SemiWiki, 26 Oct 2026](https://semiwiki.com/semiconductor-services/accellera/375280-accelleras-fsl-1-0-gives-functional-safety-data-a-common-language/).
  - The PSS 3.1 draft will "soon" be available for public review [PRIMARY] — [Accellera newsletter, Aug 2026](https://accellera.org/news/newsletters/2026-august).
  - Earlier releases: PSS 3.0 [PRIMARY] — [Accellera](https://accellera.org/news/press-releases/402-accellera-unveils-portable-test-and-stimulus-standard-3-0-ushering-in-a-new-era-of-verification-efficiency); UVM-MS 1.0 approved in 2025 [SECONDARY] — [Design & Reuse](https://www.design-reuse.com/news/news57371.html).
  - The downloads page lists CDC, FSL 1.0, IP Security Assurance (SA-EDI), IP-XACT, OCP 3.0, OVL 2.8.1, PSS, SCE-MI 2.4, Soft IP Tagging 1.0, SystemC, SystemRDL 2.0, UCIS 1.0, UVM (IEEE 1800.2 reference implementation), UVM-MS and Verilog-AMS [PRIMARY] — [Accellera downloads](https://www.accellera.org/downloads/standards).
  - The board page returned 404, so governance (who controls Accellera) was not verified this pass.

**(ii) Machine-readable architecture specifications and compliance suites (the "judges")**
- Arm's machine-readable specification:
  - The ASL Readers' Guide, first issue A.a, is dated 29 Oct 2025 [PRIMARY] — [Arm](https://documentation-service.arm.com/static/6901ca9402789941c1920b3a).
  - aslref, "Arm's reference implementation and documentation for the Architecture Specification Language" (parsing, type-checking, interpretation), v1.0 was published on opam on 3 Apr 2026 [PRIMARY] — [opam](https://ocaml.org/p/aslref).
  - The open-source AARCHMRS package (Features.json, Instructions.json) is "a subset of the proprietary releases" that omits descriptive content. Its schema is "subject to change". Release tags include FAT-2026-03, FAT-2026-06 and FAT-2026-09 [PRIMARY, mirror] — [AARCHMRS](https://kernel.googlesource.com/pub/scm/linux/kernel/git/maz/AARCHMRS/+/HEAD). See also [Arm blog "Working with MRS data"](https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/working-with-mrs-data).
- Arm's Architecture Compliance Kit (ACK) as a contractual judge:
  - Architecture licensees (Apple, Qualcomm and Nvidia are named) may design their own cores, but must match the architecture "down to obscure corner cases".
  - "Qualcomm's filing says its engineers run roughly 48,000 ACK tests."
  - The jury found that Arm breached Qualcomm's architecture licence (ALA) by withholding ACK patches and out-of-band (OOB) packages, which identify which tests apply. Qualcomm alleged the withholding ran from late 2022 into 2025. Arm argued these were "not mandatory deliverables" [SECONDARY, columnist is Veriest chairman] — [EE Times, M. Zalcberg, 23 Oct 2026](https://www.eetimes.com/two-dollars-and-a-test-suite/).
- Arm v. Qualcomm:
  - On 30 Sep 2025 the judge rejected Arm's remaining Nuvia-licence claims [SECONDARY] — [The Register, 1 Oct 2025](https://www.theregister.com/2025/10/01/arms_last_legal_claim_against/).
  - On 13 Oct 2026 a Delaware jury awarded $2 damages; Qualcomm won 2 of 6 claims [SECONDARY] — [Techzine](https://www.techzine.eu/news/privacy-compliance/144989/arm-violated-qualcomms-license-but-will-pay-only-2/).
  - Under Section 8.3, an uncured breach after 30 days' notice could take royalties on qualifying products to zero for five years. Judge Maryellen Noreika decides; bench-trial closings were heard on 20 Oct 2026; the ruling date is "not yet known" [SECONDARY] — [EE Times](https://www.eetimes.com/two-dollars-and-a-test-suite/).
  - One estimate puts the remedy at about $300M a year (about $1.5B in total) [SECONDARY, UNVERIFIED estimate] — [Futurum](https://futurumgroup.com/?p=97135); [Xenospectrum](https://xenospectrum.com/en/qualcomm-arm-verdict-royalty-suspension/).
  - No remedy ruling was found as of 12 Nov 2026. The FTC reportedly opened an antitrust inquiry into Arm licensing [SECONDARY] — EE Times, same.
- RISC-V International:
  - The Sail model README says the formal specification "has been adopted by RISC-V International". It generates a C++ emulator, documentation, and "theorem-prover definitions for interactive proof (in Isabelle, Rocq, and Lean)". BSD-2 licence; 807 stars on 12 Nov 2026 [PRIMARY] — [sail-riscv](https://github.com/riscv/sail-riscv).
  - Certification: the RVI certificate class for the Unprivileged ISA has a Certification Requirements Document "voted on and approved by the CSC Requirements WG on Mar 10, 2026". The programme (RVCP) is overseen by the Certification Steering Committee, which issued a call for chair and vice-chair candidates in Jan 2026 [PRIMARY wiki, seen only as a search excerpt; a direct fetch returned no content] — [RISC-V wiki](https://riscv.atlassian.net/wiki/spaces/HOME/pages/771424332). The RVI20 CRD URL returned 404 on fetch — [riscv-arch-test](https://riscv.github.io/riscv-arch-test/crd/rvi20_crd.html).
  - Breker donated test-suite components for future compliance activities [COMPANY CLAIM] — [Design & Reuse](https://www.design-reuse.com/news/202529524-breker-donates-advanced-test-suite-components-to-risc-v-international-for-use-in-future-compliance-activities). RVI has ISO/IEC JTC 1 PAS Submitter status [SECONDARY].
- Interface standards bodies:
  - USB-IF: Vendor ID US$6,000; annual membership US$5,000 (includes a vendor ID); logo licence US$3,500 for two years (waived for members). The logo is allowed only for products that "pass USB-IF compliance testing" [PRIMARY] — [USB-IF](https://www.usb.org/getting-vendor-id).
  - UCIe has 12 promoters: AMD, ASE, Alibaba Cloud, Arm, Google Cloud, Intel, Meta, Microsoft, NVIDIA, Qualcomm, Samsung and TSMC. The membership page shows no fees and no compliance programme [PRIMARY] — [UCIe](https://www.uciexpress.org/membership).
  - The PCI-SIG site refused fetch. JEDEC, MIPI and CXL were not reached.

**(iii) Foundry design rules as specifications**
- TSMC's EDA Alliance page shows certification grids "as of 10/01/2026" for A14, A16, N2P, N3C and 3DFabric with only three vendor columns: Cadence, Synopsys and Siemens EDA [PRIMARY, cross-ref sibling note japan_korea_taiwan.md] — [TSMC](https://www.tsmc.com/english/dedicatedFoundry/oip/eda_alliance).
- An analyst remark: TSMC certifies tools against its rules, but no regime certifies what an autonomous agent did [SECONDARY] — [Futurum, 24 Sep 2026](https://futurumgroup.com/insights/tsmcs-oip-forum-turns-agentic-chip-design-demos-into-production-flows/).

**(iv) Systems and software requirements management; model-based design**
- IBM DOORS / Engineering Lifecycle Management (ELM):
  - CVE-2026-14979 (a DOORS XML entity-expansion denial of service) affects ELM 7.0.3-7.2.0; published 17 Jul 2026 [PRIMARY, vulnerability database] — [stack.watch](https://stack.watch/vuln/CVE-2026-14979/).
  - IBM continues to support DOORS 9.7.x "because the version still has a significant user base". The release notes were modified 29 Jan 2026 [PRIMARY] — [IBM](https://www.ibm.com/support/pages/release-notes-doors-and-doors-web-access).
  - DOORS Next is marketed as "powered by AI agentic automations" [COMPANY CLAIM, partner page] — [SodiusWillert](https://www.sodiuswillert.com/en/ibm-elm/doors-next).
  - No 2026 divestiture or licensing change was found. The pricing page fetch showed no DOORS pricing.
- PTC Codebeamer:
  - Codebeamer 3.2, Codebeamer AI 1.0 and pure::variants 7.2 were released on 15 Jan 2026. The "Requirements Assistant" is aligned with INCOSE and ISTQB guidance and detects requirement-quality issues; the "Test Case Assistant" generates tests from requirements. AI 1.1 adds regional data residency and AI 1.2 adds semantic search. The PTC NEXT roadmap (June 2026) covers testability and coverage checks and MCP integration with AI agents [COMPANY CLAIM/SECONDARY] — [CIMdata](https://www.cimdata.com/en/industry-summary-articles/item/29186-ptc-delivers-new-ai-functionality-for-software-driven-product-development-with-new-alm-releases); [PTC community](https://community.ptc.com/codebeamer-445/codebeamer-ai-1-1-has-released-173736); [MONOist, Jun 2026](https://monoist.itmedia.co.jp/mn/articles/2606/24/news060_2.html).
  - BMW Group adopted Codebeamer [COMPANY CLAIM] — [PTC news 2026](https://www.ptc.com/it/news/2026/ptc-codebeamer-adopted-by-bmw-group).
- Jama Software:
  - Francisco Partners agreed to buy Jama for about $1.2B (announced 18 Mar 2024) from Insight Partners and Madrona [SECONDARY] — [CIMdata](https://www.cimdata.com/en/industry-summary-articles/item/24350-francisco-partners-to-acquire-jama-software-for-1-2b).
  - An MCP server was announced in May 2026, keeping permissions, workflows and audit [SECONDARY, single source] — [yespress](https://yespress.io/jama). Jama Connect Advisor, an AI requirement-writing assistant, has existed since 2022.
  - The pricing page returned 404.
- Dassault Systèmes (CATIA Magic/Cameo MBSE, Reqtify): see section 4. No product-level requirements or MBSE revenue is disclosed.
- Valispace: Altium announced the acquisition in Feb 2024 [COMPANY CLAIM] — [Valispace](https://www.valispace.com/valispace-joins-forces-with-altium/). It is now sold as Altium's "Requirements & Systems Portal" — [Altium](https://www.altium.com/documentation/requirements-systems-portal/new). Renesas bought Altium, and Renesas 365 is built on Altium 365 [SECONDARY] — [DE247](https://www.digitalengineering247.com/article/renesas-to-buy-pcb-design-software-leader-altium/news). A Japanese chipmaker therefore now owns a requirements tool.
- Flow Engineering:
  - Raised a $50M Series B (announced 30 Sep 2026) at a $750M valuation [SECONDARY] — [SiliconANGLE, 1 Oct 2026](https://siliconangle.com/2026/10/01/flow-engineering-raises-50m-to-bring-the-power-of-ai-to-hardware-engineering/). Co-leads: Antonio Gracias (Valor) and Gavin Baker (Atreides). Also participating: Sequoia (which led the Series A), Human Capital, Evantic, SV Angel, Odyssey and EQT.
  - Product: an "agentic artificial intelligence-powered hardware systems design platform" whose agents work in CAD, Git, simulations and docs to run impact analysis, flag conflicts and detect requirements failures.
  - Customers named: GM Performance Power Units, Rivian, RV Tech (a VW joint venture), Anduril, Stoke Space, Intuitive Machines, Pacific Fusion, Joby, Astranis and Radiant. CEO Pari Singh. Revenue not stated [SECONDARY] — same.
- Model-based design as executable specification:
  - MathWorks fact sheet (dated 03/26): "$1.5 billion in annual revenue"; "profitable every year since founding"; privately held; over 6,500 staff in 34 offices; 5 million MATLAB users; 100,000+ installations [COMPANY CLAIM] — [MathWorks fact sheet](https://ch.mathworks.com/content/dam/mathworks/fact-sheet/2026-company-factsheet-8-5x11-8282v27.pdf).
  - MathWorks 2026 releases (headlines only; the release pages returned 404): "MathWorks Provides TÜV SÜD-Certified Guidance for Using Agentic AI in Engineering Workflows" (14 Oct 2026); "MathWorks Introduces Release 2026b" (24 Sep 2026); "MathWorks Enables AI Agents to Execute and Validate Engineering Workflows within MATLAB" (15 Jul 2026) [PRIMARY headline] — [MathWorks newsroom](https://www.mathworks.com/company/newsroom.html).
  - dSPACE: sales up 14% in 2024 to about EUR 460M, with over 2,800 staff, about 1,700 of them in Paderborn [SECONDARY] — [aeemobility](https://aeemobility.de/?p=10014). Over 2,900 staff in early-2026 releases [COMPANY CLAIM] — [Business Wire](https://www.businesswire.com/news/home/20260224396140/en).
  - Vector Informatik: more than EUR 1B revenue in 2024 and more than 4,500 staff in 32 locations [COMPANY CLAIM] — [Testing Expo profile](https://testingexpo-europe.com/exhibitors/vector-informatik-gmbh-1). It acquired RocqStat (timing analysis and software verification) [SECONDARY] — [Automotive World](https://www.automotiveworld.com/news/vector-buys-rocqstat-to-boost-software-verification/).
  - No 2025 figures were found for dSPACE or Vector. ETAS was not reached.

**(v) Spec-driven development for AI coding, specification languages and 2026 entrants**
- GitHub Spec Kit is an open-source (MIT) toolkit that gives "AI coding agents structured processes, reusable templates, and documented outcomes". Its flow is constitution, specify, plan, tasks, implement, converge. 149.5k stars and 13.4k forks on 12 Nov 2026 [PRIMARY] — [GitHub](https://github.com/github/spec-kit).
- Tessl:
  - Raised $125M in Nov 2024 (a $100M Series A plus a $25M seed) at a reported $750M valuation; investors Index, Accel, GV and boldstart [SECONDARY] — [tech.eu](https://tech.eu/2024/11/14/snyk-founders-new-venture-tessl-raises-125m-for-ai-software-development/).
  - Its Spec Registry entered open beta on 16 Sep 2025. A reviewer says the regeneration engine is closed beta, JavaScript-only and "demonstrably non-deterministic", and describes an enterprise pivot in Jan 2026 [SECONDARY, reviewer opinion] — [codemyspec](https://codemyspec.com/blog/tessl-review).
  - Its site now promotes "Tessl Agent" and AI DevCon (2-4 Nov) — [Tessl](https://tessl.io/blog/announcing-our-series-a-for-ai-native-software-development). No 2026 round was found.
- AWS Kiro (brief; covered in depth elsewhere): per-user plans are Free $0 (50 credits), Pro $20 (1,000), Pro+ $40 (2,000), Pro Max $100 (5,000) and Power $200 (10,000). Add-on credits cost $0.04. Teams pay $20 per seat per month, with 500 pooled credits per seat. "A credit is a unit of work", and spec prompts, spec refinement and task execution all consume credits. Enterprise is billed through AWS [PRIMARY] — [Kiro pricing](https://kiro.dev/pricing/).
- Antithesis:
  - Raised a $105M Series A led by Jane Street (Dec 2025) [SECONDARY] — [Fortune, 23 Mar 2026](https://fortune.com/2026/03/23/antithesis-janestreet-ethereum-will-wilson-foundationdb-software/).
  - Product: deterministic simulation testing ("autonomous verification") that runs in CI or "as an agent skill". Its agent skills help agents "build a specification of its behavior".
  - Users named include Jane Street, etcd/Kubernetes maintainers, Mysten (Sui), ParadeDB, Formance, Tigris and PingThings. Blog posts: 15 Oct 2026, "Your agent can now ship reliable distributed systems"; 2 Nov 2026, streaming test results. The homepage shows no pricing [COMPANY CLAIM] — [Antithesis](https://antithesis.com/).
- TLA+ Foundation (Linux Foundation): member logos are AWS, Oracle and NVIDIA. Its GenAI-accelerated TLA+ challenge (deadline 3 Jul 2025, sponsored by NVIDIA) required AI-generated specs and invariants to be checked with TLA+ tools. First place went to "Specula", which derives TLA+ specs from source code and checks them against the implementation, shown on etcd Raft (Go) and the Asterinas SpinLock (Rust) [PRIMARY] — [TLA+ Foundation](https://foundation.tlapl.us/); [challenge](https://foundation.tlapl.us/challenge/index.html).
- AWS P language: "a state machine based programming language for formally modeling and specifying complex distributed systems". AWS teams using it: S3, EBS, DynamoDB, MemoryDB, Aurora, EC2 and IoT. PeasyAI generates P state machines, specifications and test drivers from design documents, and "Integrates with Cursor and Claude Code via MCP". MIT licence; 3.7k stars [PRIMARY] — [p-org/P](https://github.com/p-org/P).
- 2026 entrants whose product includes specification authoring or review for formal methods (all cross-referenced from sibling notes):
  - Harmonic Aristotle proposes properties; engineers review and commit them; consumption pricing [COMPANY CLAIM] — [Harmonic](https://harmonic.fun/news/aristotle-software-hardware-verification).
  - Certora AutoProver generates specs (CVL rules) [COMPANY CLAIM] — [Certora](https://certora.com/blog/autoprover-agentic-formal-verification).
  - Normal Computing raised $50M (led by Samsung Catalyst) for auto-formalisation in design verification and RTL [SECONDARY] — [SemiEngineering Q1 2026](https://semiengineering.com/startup-funding-q1-2026/).
  - VerifAIX (US/India/Israel) raised a $5M seed (30 Sep 2026) — [VerifAIX](https://verifaix.com/verifaix-raises-5m-seed-funding-co-led-by-bluehill-vc-and-endiya-partners/).
  - Also: Theorem, &Truth and Axiom (see software_proof_startups_market.md).
- Quint and Alloy were not reached this pass.

**Regional coverage**
- Japan: Zuken's "IT solutions" line (28.1% of H1 FY2027/3 sales) includes GENESYS MBSE [PRIMARY, cross-ref] — [Zuken](https://pdf.irpocket.com/C6947/xoA3/DnNg/ah0Z/kwJh.pdf). Renesas owns Valispace through Altium.
- India: Agnisys (development presence not verified this pass); L&T Semiconductor Technologies is a Defacto user.
- Europe: Dassault; Defacto (now Siemens); dSPACE; Vector; Valispace (now Altium/Renesas). Also Prover, RATP and Systerel, which published the unified HLL 4.0 railway-signalling specification on 23 Sep 2026 [COMPANY CLAIM, cross-ref] — [Prover](https://www.prover.com/).
- Israel: no requirements or specification vendor found. VerifAIX has an Israeli team.
- Korea and China: no requirements or specification-tool vendor found this pass (coverage thin).

### Inferences
- [JUDGMENT] The owners of specifications that have contractual or market force behind them are Arm (the ACK in licences), USB-IF (the logo) and the foundries (tool certification). Authoring-tool vendors own neither the format (Accellera/IEEE, OMG, TLA+, P and Sail are open or consortium-owned) nor the verdict.
- [JUDGMENT] Consolidation is under way: Defacto went to Siemens, Valispace to Altium/Renesas, Jama to private equity, and PTC is going to Schneider. Independent specification-tool vendors look like acquisition targets rather than stand-alone winners.
- [JUDGMENT] The AI-native specification layer is being given away (Spec Kit, P/PeasyAI and TLA+ tools are all open source) or bundled into usage pricing (Kiro, Harmonic). That squeezes any business built only on authoring seats.

### Gaps
- Not reached this pass: Perforce, Visure, ETAS, Quint and Alloy; Korean, Chinese and Israeli requirements vendors; PCI-SIG, JEDEC, MIPI and CXL compliance fees; RISC-V certification fees, first certificates and the RVA23 profile status.
- Agnisys ownership, revenue and headcount; the Defacto price; Accellera board composition.

## 2. Who writes and owns the specifications, and can AI write them well enough to be trusted?

### Takeaway
Humans still write, and above all sign off, the specifications that matter: architects and architecture owners (Arm, RISC-V International), standards committees, OEM and prime systems engineers, and independent assessors (FAA/EASA, TÜV, Common Criteria labs).

Between 2024 and 2026, AI became good at drafting formal specifications and assertions for bounded problems. On some benchmarks it even beats the human reference specifications, which are themselves often wrong. It is not yet reliable enough to be trusted as an unsupervised author or reviewer:
- It misses about half of expert-found requirement defects.
- Its assertion correctness changes when code is rewritten without changing meaning.
- Provers have certified proofs of the wrong (weaker) statements.
- The largest 2026 project, AlphaProof Code, still had humans review every line of its roughly 26,000-line trusted specification.

### Cited Findings

**(a) Research results, 2023-2026**
- Earlier baselines:
  - nl2spec (Cosler et al., arXiv 2303.04864, 8 Mar 2023): LLM translation of natural language to temporal logic, with interactive human correction of sub-translations. The abstract gives no accuracy figure [PRIMARY] — [arXiv](https://arxiv.org/abs/2303.04864).
  - SpecGen (Ma et al., arXiv 2401.08807, v5 25 Feb 2025): verifiable specifications for 279 of 385 programs, beating Houdini, Daikon and pure-LLM baselines [PRIMARY] — [arXiv](https://arxiv.org/abs/2401.08807).
  - AssertLLM (Fang et al., arXiv 2402.00386, v4 25 Feb 2026): on one design with 23 I/O signals, "89% of the generated assertions are both syntactically and functionally accurate" [PRIMARY] — [arXiv](https://arxiv.org/abs/2402.00386).
- VERINA (arXiv 2505.23135, v3 16 Mar 2026): 189 Lean tasks. The best model (OpenAI o3) scored 72.6% code correctness, 52.3% specification soundness and completeness, and 4.9% proof success (one trial) [PRIMARY] — [arXiv](https://arxiv.org/abs/2505.23135). Harmonic claims 96.8% on VERINA (3 Dec 2025) [COMPANY CLAIM, cross-ref] — [Harmonic](https://harmonic.fun/news/verina-benchmark/).
- CLEVER (arXiv 2505.13938, v4 23 Oct 2025): 161 problems; "These methods all struggle to achieve full verification" [PRIMARY] — [arXiv](https://arxiv.org/abs/2505.13938).
- Vericoding (arXiv 2509.22908, 26 Sep 2025; Beneficial AI Foundation and MIT): 12,504 formal specifications. Success was 27% in Lean, 44% in Verus/Rust and 82% in Dafny; pure Dafny verification rose from 68% to 96% in a year. Adding natural-language descriptions does not significantly improve performance [PRIMARY] — [arXiv](https://arxiv.org/abs/2509.22908).
- Sosso, Arora and Spitters, "Isomorphism Is Not Enough" (arXiv 2605.23772, v2 30 Oct 2026): they find "arguably erroneous reference specifications in 80 of 161 entries" of CLEVER, while agentic stacks produce arguably valid specs for up to 98.8% of entries [PRIMARY] — [arXiv](https://arxiv.org/abs/2605.23772).
- Ground False (An, Min, Si, Bastani; ICML 2026): of 367 ProofNet formalisations, 104 (28%) are mathematically false and 100 (27%) are true but unfaithful, so 204 (56%) are unfaithful in total. Across six other benchmarks, unfaithful ground-truth rates range from 4.8% to 60.0%. A corrected ProofNet-Verified was released [PRIMARY] — [ICML](https://icml.cc/virtual/2026/82611); [NeurIPS 2026 poster](https://neurips.cc/virtual/2026/poster/139101).
- "The Faithfulness Gap" (arXiv 2606.16541, Jun 2026): DriftBench has 2,183 natural-language/Lean 4 pairs; its detector catches 89.6% of drifted formalisations at a 3.0% false-positive rate [PRIMARY, abstract excerpt] — [arXiv](https://arxiv.org/pdf/2606.16541).
- Hardware assertions in 2026:
  - AssertLLM2 (arXiv 2605.27472, 26 May 2026): 83 real designs in 13 categories; the first benchmark to feed in buggy RTL. Metrics are syntax, provability, coverage and mutation-based bug detection; the abstract gives no numbers [PRIMARY] — [arXiv](https://arxiv.org/abs/2605.27472).
  - HierSVA (arXiv 2606.13706): six axes including vacuity and specification faithfulness; aggregate recall 0.87 for flagging buggy RTL [PRIMARY, excerpt] — [alphaXiv](https://www.alphaxiv.org/abs/2606.13706).
  - arXiv 2604.11044: most failures come from "semantic drift at higher depths" [PRIMARY, excerpt] — [arXiv](https://arxiv.org/html/2604.11044v1).
  - FVRuleLearner: 1,000 NL-to-SVA pairs — [alphaXiv](https://www.alphaxiv.org/abs/2604.03245). FIXME (AAAI 2026): 747 tasks — [AAAI](https://ojs.aaai.org/index.php/AAAI/article/view/37079).
- arXiv 2609.05658 ("Robustness of LLM-Generated SystemVerilog Assertions to Semantics-Preserving RTL Transformations", submitted 4 Sep 2026) [PRIMARY] — [arXiv abstract](https://arxiv.org/abs/2609.05658); [full text](https://arxiv.org/html/2609.05658):
  - Sole author "FNU Aditi", with no affiliation line; Arm is not mentioned.
  - Models: Qwen2.5-Coder-7B and DeepSeek-Coder-V2-Lite (4-bit, run locally).
  - Test set: 40 RTL programs from the VERT dataset, with 295 behaviours.
  - Finding: "9.7%-27.0% of behaviors that were correct on the original RTL become incorrect".
  - Under renaming, DeepSeek's accuracy rose from 53.9% to 63.7% "while 19.5% of its originally correct behaviors fail".
  - Conditional robustness: Qwen 90.3%, 89.8% and 78.2%; DeepSeek 83.9%, 80.5% and 73.0% (for operand reordering, renaming and parentheses respectively).
- Requirements quality (independent evaluations):
  - Shefa, Salado, Wach and Topcu (arXiv 2609.03230, 3 Sep 2026) tested ten OpenAI and Anthropic models over 100 runs against an expert ground truth on INCOSE criteria. "The best-performing Anthropic model detects a median of only 47% of expert-identified issues while false-flagging 11%." Also: "necessity and correctness issues are almost always missed"; "newer models cannot be assumed better"; "Off-the-shelf LLMs are therefore not yet trustworthy autonomous evaluators" [PRIMARY] — [arXiv](https://arxiv.org/abs/2609.03230).
  - Levy et al. (arXiv 2604.15222): AI is quick and consistent on structural and syntactic qualities; "Correct" and "Conforming" were excluded because they need context AI cannot reliably measure [PRIMARY, excerpt] — [arXiv](https://arxiv.org/pdf/2604.15222).
  - MARQ (arXiv 2610.36234): adding INCOSE knowledge improves reliability, but human review is still recommended — [papers.cool](https://papers.cool/arxiv/2610.36234).
  - RE2026 paper (Plösch): naive LLM rewriting introduced new issues and hallucinations, while a rule-guided tool cut the mean number of violated INCOSE rules per requirement by 59% across 75 requirements [SECONDARY excerpt] — [JKU](https://se.jku.at/?p=16290).
- Provers proving the wrong statement (mathematics):
  - Erdős #124: Aristotle proved a weaker variant that was "significantly easier" than the original [SECONDARY; erdosproblems.com returned 403] — [The Decoder](https://the-decoder.com/?p=31101).
  - Erdős #707: the Lean statement in the Formal Conjectures repository "was in fact incorrect for a subtle reason" [PRIMARY community archive] — [Lean Zulip](https://leanprover-community.github.io/archive/stream/113488-general/topic/Erdos.20707.html).
  - Erdős #728: the problem statement was ambiguous [PRIMARY] — [arXiv 2601.07421](https://arxiv.org/pdf/2601.07421).
- Large 2026 projects (human share of specification):
  - DeepMind AlphaProof Code (announced 10 Nov 2026) produced about 6.5M lines of Lean proof. The trusted specification is about 18,000 lines of statements and definitions plus about 8,000 lines of AArch64 semantics and symbol names, about 26,000 in total, and human experts reviewed every specification [PRIMARY] — [project page](https://google-deepmind.github.io/code-verification/); [blog](https://deepmind.google/blog/introducing-alphaproof-code/); [paper PDF, cross-ref](https://deepmind.google/documents/36/Formal_Verification_of_Signal_4.pdf). The blog says "over six million lines" (cross-ref sibling note model_makers_hyperscalers.md).
  - Anthropic Frontier Red Team with Theorem (22 Oct 2026): specs were generated automatically from fuzz tests across 123 libraries; "'Formally verified' does not mean 'bug-free.'" [PRIMARY, cross-ref] — [Anthropic](https://www.anthropic.com/research/formal-verification).
  - Harmonic/Tensordyne: of 241 properties, 100 were written by Aristotle from 312 pages of specs; 185 were proved and 56 refuted. Harmonic's docs say: "Behaviors not listed as properties are not verified" [COMPANY CLAIM, cross-ref] — [case study](https://harmonic.fun/aristotle/case-studies/tensordyne/); [docs](https://aristotle.harmonic.fun/docs/overview).
  - Certora: AI specs may omit requirements, and experts must review solvency properties [COMPANY CLAIM, cross-ref] — [Certora](https://www.certora.com/blog/ai-formal-verification-smart-contracts-costs-use-cases). From its Devcon panel: "A tool can reason correctly about a specification that describes the wrong behavior" — [Certora](https://www.certora.com/blog/devcon-india-2026-ai-formal-verification).

**(b) Practice: who signs off, and what regulation requires**
- Chips:
  - The architecture owner's judge decides compliance: the Arm ACK under the architecture licence (48,000 tests at Qualcomm; section 1).
  - RISC-V certification is run by RVI's Certification Steering Committee (CRD approved 10 Mar 2026).
  - Interface logos require passing compliance testing (USB-IF).
  - The foundry certifies sign-off tools per node (TSMC grid, section 1).
- Aviation:
  - Under DO-178C, 30 of 71 objectives at Level A must be met with independence (the verifier may not be the author); Level B has 18 of 69.
  - FAA, EASA and Transport Canada approve. AC 20-115D (21 Jul 2017) recognises DO-178C as "an acceptable means, but not the only means".
  - DO-330 is a domain-independent tool-qualification document also usable for ISO 26262. DO-331 covers model-based development; DO-333 covers formal methods "to complement (but not replace) testing" [SECONDARY] — [Wikipedia DO-178C](https://en.wikipedia.org/wiki/DO-178C).
  - First certification credit for a compiler: CompCert was qualified in March 2026 for the ATR 42/72 MFC_NG under DO-178C/DO-333/DO-330. No authority is named [PRIMARY, cross-ref] — [AbsInt, 20 Mar 2026](https://www.absint.com/releases/260320.htm).
  - EASA AI Concept Paper Issue 2 (6 Mar 2024) covers Level 1 (enhancing human capabilities) and Level 2 (human-AI teaming under human oversight). Its landing page says nothing on AI in development tools [PRIMARY] — [EASA](https://www.easa.europa.eu/en/document-library/general-publications/easa-artificial-intelligence-concept-paper-issue-2). The FAA AI roadmap page returned 403.
- Automotive and functional safety:
  - ISO 26262 Part 8 requires "Confidence in software tools (qualification of software tools for the intended and actual use)". The second edition (Dec 2018) added Part 11 (semiconductors) [SECONDARY] — [Wikipedia ISO 26262](https://en.wikipedia.org/wiki/ISO_26262).
  - MathWorks announced "TÜV SÜD-Certified Guidance for Using Agentic AI in Engineering Workflows" (14 Oct 2026; headline only) [PRIMARY headline] — [MathWorks](https://www.mathworks.com/company/newsroom.html).
- Security:
  - Common Criteria testing labs must comply with ISO/IEC 17025; national schemes certify; at EAL5 and above the host government's requirements tend to apply; CC:2022 is ISO/IEC 15408:2022 [SECONDARY] — [Wikipedia](https://en.wikipedia.org/wiki/Common_Criteria).
  - EU Cyber Resilience Act: Article 14 reporting applies from 11 Sep 2026 and the main obligations from 11 Dec 2027. Final non-binding guidance was published 27 Jul 2026, and the law-firm summary does not mention formal verification [SECONDARY, cross-ref] — [Orrick](https://www.orrick.com/en/Insights/2026/09/EU-Cyber-Resilience-Act-New-Guidance-Clarifies-Scope-Reporting).
- EU AI Act "AI Omnibus": high-risk obligations moved from 2 Aug 2026 to 2 Dec 2027 (stand-alone, Annex III) and 2 Aug 2028 (embedded in products, Annex I). It is reported as Regulation (EU) 2026/1744, published in the OJ 24 Jul 2026 and in force 27 Jul 2026; sources differ on the dates. Most transparency duties were not delayed [SECONDARY, law firms] — [Addleshaw Goddard](https://www.addleshawgoddard.com/en/insights/insights-briefings/2026/technology/eu-ai-act-ai-omnibus-formally-adopted/); [Loyens & Loeff](https://www.loyensloeff.com/insights/news--events/news/eu-ai-act-key-amendments-adopted-under-digital-omnibus-package/).
- Context: only 5% of IC/ASIC respondents reported first-silicon success in 2026, against 14.4% in 2024; the methodology changed [INDEPENDENT survey, vendor-sponsored, cross-ref] — [Siemens/Wilson 2026](https://blogs.sw.siemens.com/verificationhorizons/2026/09/08/the-2026-functional-verification-study/).

**(c) Vendor claims about AI-generated specifications and requirements, and any independent evaluation**
- The claims:
  - PTC: Codebeamer AI Requirements Assistant (INCOSE/ISTQB) and Test Case Assistant [COMPANY CLAIM].
  - Jama: Connect Advisor and an MCP server [SECONDARY].
  - IBM: DOORS Next "AI agentic automations" [COMPANY CLAIM].
  - Agnisys: iSpec.ai English-to-SVA and IDS-AI [COMPANY CLAIM].
  - Defacto/Siemens: AI layer in SoC Compiler [SECONDARY, company-sourced].
  - Arteris: the Q3 2026 release makes no AI-specification claim [PRIMARY].
  - Dassault: the Q3 release page carried no AI-specification claim.
  - Synopsys, Cadence and Siemens are covered in sibling notes.
- The independent evaluation closest to these vendor features is arXiv 2609.03230. It found off-the-shelf models catch a median of 47% of expert-identified INCOSE issues at best and "almost always" miss necessity and correctness issues.
- No independent evaluation of any named vendor's requirement or specification AI was found [UNVERIFIED].

### Inferences
- [JUDGMENT] **Reasoned answer.** Specifications that carry commercial or legal weight are owned by whoever controls the judge: the architecture owner and its compliance suite, the standards body and its logo test, the foundry and its certified deck, the certification authority and its accepted means. They are signed off by accountable humans. AI can now draft formal specifications well enough to shift labour. Examples: agentic stacks produce arguably valid specs for up to 98.8% of CLEVER entries; Aristotle wrote 100 of 241 properties at Tensordyne; P/PeasyAI and Specula derive specs from documents and code. But the evidence does not support trusting AI-written specifications without human sign-off:
  - About 47% recall on expert-found requirement defects.
  - 9.7-27% instability of assertion correctness under semantics-preserving rewrites.
  - Semantic drift and wrong-statement proofs (Erdős #124 and #707).
  - The flagship 2026 project still had humans review all of its roughly 26,000 trusted lines: about 250 lines of proof per line of reviewed specification [CALC: 6.5M / 26,000].
  - No regulator or certifier was found that accepts AI as the signatory or reviewer of record. DO-178C independence, ISO 26262 tool confidence and Common Criteria labs all place accountability on humans and accredited bodies.
- [JUDGMENT] **The surprise in the evidence.** Human-written reference specifications are also frequently wrong: 80 of 161 CLEVER entries and 56% of ProofNet. So "trust" cannot mean "humans wrote it". It means an accountable party reviewed it against an independent judge. AI faithfulness checkers (DriftBench detector: 89.6% at 3% false positives) and human review together beat either alone.
- [JUDGMENT] **Confidence.** High that AI-written specifications will not be trusted without human sign-off in regulated and safety-critical uses through at least 2028. The EU AI Act high-risk duties start December 2027 / August 2028, and the CRA's main obligations December 2027. Moderate that AI drafts most new formal-specification text in leading chip and software teams by 2028. Low on the timing of regulatory acceptance of AI reviewers.
- [JUDGMENT] **What would change it:**
  - An independent, replicated benchmark on industrial designs with checked ground truth (a ProofNet-Verified for hardware or requirements) showing AI specifications above about 95% faithful, with low variance across semantics-preserving rewrites.
  - A certification authority or TÜV accepting AI-generated requirements or specifications with reduced human review, or qualifying an LLM-based specification tool under DO-330 or ISO 26262 Part 8.
  - Conversely, a publicised field failure of a "verified" product traced to a specification error would harden the human-sign-off requirement.
  - The Arm–Qualcomm Section 8.3 ruling and any FTC action would shape who controls compliance suites.
- [JUDGMENT] **Test of the prior** ("value moves from writing proofs to writing specifications"):
  - Partly supported. Proof is now cheap and abundant (millions of lines), while the reviewed specification is the bottleneck (about 26,000 lines, all human-reviewed).
  - But writing specifications is itself becoming cheap (98.8% arguably valid on CLEVER).
  - The scarce and monetisable items are the judge (compliance suite, golden model, certification mark) and the accountable sign-off, more than specification authoring.

### Gaps
- No independent evaluation of Codebeamer AI, Jama Advisor, DOORS AI, IDS-AI or the Defacto AI layer was found.
- Not found: the content of the MathWorks/TÜV SÜD guidance; the FAA roadmap; any EASA rulemaking after Concept Paper Issue 2; DO-330 TQL and ISO 26262 TCL details; ISO/PAS 8800; any regulator statement on AI-generated requirements.
- No numeric results for AssertLLM2 (the abstract gives none).

## 3. Value capture: who gets paid for owning specifications, and is seat pricing under pressure?

### Takeaway
The money for owning a specification goes mainly to Arm, through licences and royalties tied to compliance with its specification. Standards bodies collect modest membership and logo fees (for example USB-IF's US$5,000 membership and US$3,500 logo licence). Foundries' design-kit and rule-deck control is monetised inside wafer prices (no fee data found). Requirements-tool vendors collect seat or subscription fees.

Incumbent requirements and ALM vendors show no visible seat erosion yet (PTC has 95.9% recurring revenue and ARR up 9.7% in constant currency; Dassault's ARR is up 6%). AI-era entrants mostly price by usage (Harmonic consumption, Kiro credits, Certora credits plus seats).

### Cited Findings
- Arm Q2 FYE27 (quarter ended 30 Sep 2026, released 4 Nov 2026) [PRIMARY] — [Arm](https://newsroom.arm.com/news/arm-q2-fye27-results):
  - Revenue $1.44B (+27%): licence and other $773M (+50%), royalty $670M. The royalty share is about 46% [CALC].
  - Data-centre royalties doubled year on year.
- Arm's specification leverage over licensees:
  - The ACK is required to show conformance (48,000 tests at Qualcomm).
  - Under Section 8.3, the remedy could cut Qualcomm royalties on qualifying products to zero for five years [SECONDARY] — [EE Times](https://www.eetimes.com/two-dollars-and-a-test-suite/).
  - Arm keeps the full machine-readable specification proprietary; the open AARCHMRS is "a subset" [PRIMARY] — [AARCHMRS](https://kernel.googlesource.com/pub/scm/linux/kernel/git/maz/AARCHMRS/+/HEAD).
- Standards bodies: USB-IF charges a US$5,000 annual membership, a US$6,000 Vendor ID and a US$3,500 two-year logo licence [PRIMARY] — [USB-IF](https://www.usb.org/getting-vendor-id). UCIe publishes no fees [PRIMARY] — [UCIe](https://www.uciexpress.org/membership). Sail is BSD-2 (free) [PRIMARY] — [sail-riscv](https://github.com/riscv/sail-riscv).
- Requirements and ALM tools:
  - PTC FY2026: recurring revenue $2,621.9M of $2,733.4M (about 95.9%) [CALC from PRIMARY] — [PTC FY2026 release via Finviz](https://finviz.com/news/415751/ptc-announces-fourth-fiscal-quarter-and-full-fiscal-year-2026-results). Licence plus support and cloud total $2,639.0M against $2,621.9M recurring, which implies only about $17M of non-recurring licence [CALC]. No usage pricing was disclosed.
  - Dassault: ARR +6%, cloud +14% (Q3 2026) [PRIMARY] — [Dassault](https://www.3ds.com/newsroom/press-releases/dassault-systemes-strong-q3-performance-improved-fy26-objectives-and-step-change-life-sciences.md).
  - Jama and IBM pricing pages showed no pricing (404 or none).
- Arteris (royalty plus licence):
  - Q3 2026 revenue mix: licensing, support and maintenance $22.4M; variable royalties $2.3M; professional services and other $1.1M.
  - TTM variable royalties were $9.4M (+71%) [PRIMARY] — [Arteris Q3 release](https://www.sec.gov/Archives/edgar/data/0001667011/000162828026071063/exhibit991q3fy268-k.htm).
- AI-era pricing:
  - Kiro charges per seat plus metered credits (above) [PRIMARY].
  - Harmonic is "Consumption-based, with no seats or licenses" [COMPANY CLAIM, cross-ref] — [Harmonic](https://harmonic.fun/).
  - Certora AutoProver: Free (1 seat), Pro US$120 a month for up to 5 seats, Enterprise from US$3,000 a month; runs are paid with credits [COMPANY CLAIM, cross-ref] — [Certora](https://www.certora.com/blog/ai-formal-verification-smart-contracts-costs-use-cases).
  - Paid demand for verified code: the Aave DAO approved US$2.39M for 12 months of security work including formal verification [cross-ref, same source].

### Inferences
- [JUDGMENT] Arm is the only company in this segment that clearly gets paid for owning a specification at scale. Its royalties scale with units, which is a usage-like model. The Qualcomm verdict shows that control of the compliance suite is commercially material, enough that withholding test deliverables breached a contract with a remedy that could be worth billions.
- [JUDGMENT] Seat pressure on requirements tools does not yet show in reported numbers. It shows in valuation: Dassault's EV/sales fell from 14.4x (FY2021) to about 5x (section 5). It also shows in new entrants pricing by usage, and in incumbents adding MCP servers so that AI agents (priced by usage elsewhere) read and write the requirements record.

### Gaps
- Not found: fees for PCI-SIG, JEDEC, MIPI, CXL and RISC-V; foundry design-kit access terms; revenue for Jama, IBM ELM, Codebeamer, Cameo/Reqtify and Agnisys.
- No evidence of any incumbent moving requirements tools from seats to usage pricing.

## 4. In-depth assessments (quality evidence only; valuation is in section 5)

### Takeaway
Arm passes the "owns the judge" test and has a usage-like royalty model, but its move into selling chips puts the neutrality of its compliance role under legal and antitrust pressure. Arteris has a royalty-bearing IP core but is small and loss-making, and its specification-automation tools are time-licensed and replaceable. PTC and Dassault are high-margin seat and subscription franchises for which requirements tools are a minor part. Agnisys cannot be assessed financially.

### Cited Findings

#### Arteris (NASDAQ: AIP)
- **a. Position.** It sells interconnect IP with royalties (embedded in customers' silicon) and time-licensed SoC specification and integration software (CSRCompiler, Magillem) [PRIMARY, 10-Q]. It owns no industry judge.
- **b. Lead.**
  - Company claims: "the milestone of 1,000 confirmed design starts since inception"; deals with "a top US hyperscaler and two market-leading semiconductor companies" and "a leading automotive OEM"; one-third of licence wins by value from "top 30 global technology companies" [COMPANY CLAIM] — [Q3 release](https://www.sec.gov/Archives/edgar/data/0001667011/000162828026071063/exhibit991q3fy268-k.htm).
  - Filed figures: RPO $135.5M (+29%) in the release and $131.3M non-cancellable in the 10-Q [PRIMARY].
  - No independent share data was found.
  - It expanded third-party IP security assurance through the Trusted and Assured Microelectronics programme with BAE Systems and SiFive [COMPANY CLAIM].
- **c. Revenue model** (Q3 2026, quarter ended 30 Sep, released 5 Nov 2026):
  - Revenue $25.8M (+48% y/y): licensing, support and maintenance $22.4M; variable royalties $2.3M; professional services and other $1.1M. ACV plus royalties $103.8M (+39%). TTM variable royalties $9.4M (+71%) [PRIMARY] — [Q3 release](https://www.sec.gov/Archives/edgar/data/0001667011/000162828026071063/exhibit991q3fy268-k.htm).
  - Interconnect IP licences run 2-3 years, recognised rateably; royalties are per unit or a percentage of revenue. Integration software and security verification software are on 1-3 year time-based licences.
  - Deferred revenue $112.1M; RPO $131.3M non-cancellable (the release says $135.5M) [PRIMARY] — [10-Q](https://www.sec.gov/Archives/edgar/data/0001667011/000162828026071154/aip-20260930.htm).
- **d. Financial strength.**
  - Margins and cash flow: GAAP gross margin 87% (89% non-GAAP); GAAP operating loss $11.3M (about -44% of revenue [CALC]); non-GAAP operating loss $1.2M; free cash flow -$2.1M; cash and investments about $120.3M.
  - Debt and goodwill: no bank debt (vendor financing $4.3M); goodwill $35.2M, up from $4.2M; net cash paid for the business combination $11.2M over nine months.
  - FY2026 guidance: revenue $98.5-99.5M; ACV plus royalties $103-107M; non-GAAP operating loss $7.2-9.2M; free cash flow $5-9M. Q4 guidance: revenue $25.7-26.7M; non-GAAP operating result -$0.9M to +$1.1M [PRIMARY] — [Q3 release](https://www.sec.gov/Archives/edgar/data/0001667011/000162828026071063/exhibit991q3fy268-k.htm).
  - Cycuity deal: total consideration $43.126M, made up of cash $14.121M, 1,096,280 shares worth $19.016M, $0.971M of vested awards, and contingent consideration of $9.018M (an earn-out of up to $12.0M on bookings to 31 Dec 2026). Goodwill $30.978M; intangibles $18.07M.
  - Concentration: no customer above 10% of revenue in Q3 or the first nine months of 2026, but accounts receivable are concentrated (customer A 21%, customer B 14%). 49,735,064 shares outstanding at 29 Oct 2026 [PRIMARY] — [10-Q](https://www.sec.gov/Archives/edgar/data/0001667011/000162828026071154/aip-20260930.htm).
  - ROCE -29.5% (TTM) against -79.2% (FY2025) [SECONDARY] — [stockanalysis](https://stockanalysis.com/stocks/aip/financials/ratios/).
  - China and export rules appear only as risk factors [PRIMARY].
- **e. Resilience** [JUDGMENT]:
  - Steady growth (55%): AI and chiplet design starts lift licences and royalties.
  - Pause around 2028 (25%): rateable licences and $135.5M RPO cushion revenue for about a year, but design-start slippage hits ACV, and losses plus a small scale leave little margin. Cash of $120M and no bank debt make it survivable.
  - Acceleration (20%): multi-die NoC demand gives upside.
  - Own cycle: early profitability, with growth stronger than the market. Exposure to China is a stated risk.
- **Transitions:**
  - (2) Already part usage (royalties +71%); the software remains time-licensed.
  - (4) The SystemRDL/IP-XACT formats are consortium standards, so AI agents could generate registers and assertions [JUDGMENT].
  - (6) The buyer of hardware-security verification is defence and microelectronics assurance (the TAM programme) [COMPANY CLAIM].
  - (7) Little direct model-maker overlap; hyperscalers are customers.
- **Said vs done:** it said "AI infrastructure, edge, physical AI". It has done the Cycuity close, 29% RPO growth and 71% royalty growth. It is funded (cash, positive free-cash-flow guidance), so the timing is plausible.
- **What must go right:** royalties compounding, a move to GAAP profit, and the NoC holding off Arm's own interconnect and the larger EDA vendors.
- **Provisional verdict:** partly coherent [JUDGMENT]. The royalty-bearing IP is durable; the specification tools are exposed to AI substitution; scale is small.

#### Arm Holdings (NASDAQ: ARM)
- **a. Position.** It owns the most valuable machine-readable chip specification (ASL, aslref, MRS; the open subset is partial) and the ACK judge that architecture licensees must pass [PRIMARY/SECONDARY above]. Its AArch64 semantics form part of the trusted base of DeepMind's AlphaProof Code (about 8,000 lines of AArch64 semantics and symbol names) [PRIMARY] — [DeepMind](https://google-deepmind.github.io/code-verification/).
- **b. Lead.**
  - Partners shipped more than 10B Arm-based chips in the quarter. Arm-based server share at top hyperscalers was "more than 50%" in calendar 2025 and is expected above 60% by the end of 2026. Arm-based PCs are about 20% of shipments [COMPANY CLAIM] — [Arm Q2](https://newsroom.arm.com/news/arm-q2-fye27-results).
  - Outside evidence of the judge's power: a jury finding that withholding ACK deliverables breached Qualcomm's licence [SECONDARY] — [EE Times](https://www.eetimes.com/two-dollars-and-a-test-suite/).
- **c. Revenue model.**
  - Q2 FYE27: royalty $670M, licence and other $773M [PRIMARY]. Royalties scale with units and chip prices.
  - Arm now sells its own silicon, the "Arm AGI CPU". It is confident of "up to $2B" of AGI CPU revenue over FYE27-FYE28, with purchase orders from multiple customers through 2027 and first commercial deliveries in Q4 FYE27. Oracle Cloud will offer instances in 2027. Revenue growth has been above 20% y/y for five consecutive quarters [COMPANY CLAIM] — [Arm Q2](https://newsroom.arm.com/news/arm-q2-fye27-results).
  - At trial, CEO Rene Haas agreed that about two-thirds of Arm's revenue would come from chips by 2030, describing it as "adding to our business a chip business" [SECONDARY] — [EE Times](https://www.eetimes.com/two-dollars-and-a-test-suite/).
- **d. Financial strength.**
  - Revenue (FYE March): $3,233M (FY24), $4,007M (FY25), $4,920M (FY26) and $5,464M (TTM to Sep 2026) [SECONDARY aggregator] — [stockanalysis](https://stockanalysis.com/stocks/arm/financials/).
  - Margins and cash flow (FY24 / FY25 / FY26 / TTM, same source): gross margin 95.2% / 97.0% / 97.5% / 97.4%; operating margin 2.4% / 20.7% / 18.5% / 17.0%; net income $306M / $792M / $904M / $936M; free cash flow $998M / $178M / $979M / $1,212M (FCF margin 30.9% / 4.4% / 19.9% / 22.2%).
  - Q2 FYE27: GAAP operating income $201M (about 14% [CALC]); non-GAAP $638M (about 44%) [PRIMARY].
  - Balance sheet and returns: cash $3.62B, debt $0.5B [SECONDARY] — [stockanalysis](https://stockanalysis.com/stocks/arm/); ROIC 14.8% (FY26) — [stockanalysis](https://stockanalysis.com/stocks/arm/financials/ratios/).
  - Concentration (FY2026 Form 20-F, read via a search excerpt, not fetched in full): three customers made up 42% of revenue (16%, 14% and 12%), against four customers at 49% in FY2025. PRC revenue was $874M (FY2025 $749M), about 18% of $4.92B; PRC includes Hong Kong and Macau, while Taiwan was separately $695M [PRIMARY] — [20-F](https://www.sec.gov/Archives/edgar/data/0001973239/000197323926000097/arm-20260331.htm).
  - A third-party estimate puts related-party revenue (Arm China, about 48% held by SoftBank-controlled Acetone) at $1,499M, or 30.5% [SECONDARY, UNVERIFIED] — [axis-intelligence](https://axis-intelligence.com/?p=46111).
- **e. Resilience** [JUDGMENT]:
  - Steady growth: data-centre royalties (doubling) and AGI CPU orders drive growth.
  - Pause: the chip business brings inventory and cycle exposure that pure royalties lacked.
  - Acceleration: upside.
  - Specific risks: the Section 8.3 remedy (one estimate about $300M a year [UNVERIFIED]); the reported FTC inquiry; China at about 18% of revenue plus Arm China; export controls.
- **Transitions:**
  - (2) Already usage-like (royalties).
  - (4) The open RISC-V alternative has an adopted Sail golden model and a certification programme still forming (CRD approved Mar 2026; first certificates not found).
  - (6) Arm's specification is an input to verified software (AlphaProof Code), but Arm does not monetise it directly [JUDGMENT].
  - (7) Model makers use Arm's semantics rather than replace them.
- **Said vs done:** chips said and now being done (purchase orders, deliveries due Q4 FYE27). Funded.
- **What must go right:** the chip pivot must not alienate licensees or invite antitrust remedies that neutralise the ACK.
- **Provisional verdict:** coherent as a specification-and-judge franchise; partly coherent as a strategy [JUDGMENT]. Becoming a chip competitor while controlling licensees' compliance toolchain is exactly what the Qualcomm case and the reported FTC inquiry target.

#### PTC (NASDAQ: PTC), owner of Codebeamer ALM
- **a. Position.** It sells subscription authoring and system-of-record tools (Creo, Windchill, Codebeamer). It owns no judge [JUDGMENT].
- **b. Lead.** BMW adoption of Codebeamer [COMPANY CLAIM]. Schneider Electric is paying $205 a share in cash (equity about $22.6B, EV $23.7B, a 42.3% premium; announced 5 Oct 2026; merger agreement dated 4 Oct; close expected by Q3 2027; needs a majority of outstanding shares and regulatory approvals) [PRIMARY] — [8-K exhibit](https://www.sec.gov/Archives/edgar/data/0000857005/000119312526413124/d174191dex991.htm); [PREM14A](https://www.sec.gov/Archives/edgar/data/0000857005/000114036126041824/ny20084401x1_prem14a.htm).
- **c. Revenue model.** FY2026 (FYE 30 Sep 2026, released 4 Nov 2026) [PRIMARY via mirror] — [Finviz](https://finviz.com/news/415751/ptc-announces-fourth-fiscal-quarter-and-full-fiscal-year-2026-results):
  - Revenue $2,733.4M (flat): licence $1,105.2M; support and cloud $1,533.8M; professional services $94.4M (3.5% [CALC]). Recurring revenue is about 95.9%.
  - ARR excluding divested businesses $2,508M (+8% reported, +9.7% in constant currency; +1% as reported including the divested business). Q4 revenue $673.3M (-25% y/y).
  - No ARR by product and no Codebeamer figure.
- **d. Financial strength.**
  - Margins and cash flow: GAAP operating margin 32.8%; non-GAAP 46.7%; operating cash flow $898.6M; free cash flow $872.7M (about 31.9% [CALC]).
  - Balance sheet: cash $232.9M; debt $1,609.8M; buybacks $1,624.9M.
  - EPS: GAAP diluted $8.93, including a $463.9M gain on selling ThingWorx and Kepware in Q2 FY26; non-GAAP $8.24 (+4%). Diluted shares 115.7M for the year, 109.4M in Q4.
  - Guidance and earnings calls are suspended pending the deal [PRIMARY] (same source). ROIC 15.5% [SECONDARY] — [stockanalysis](https://stockanalysis.com/stocks/ptc/financials/ratios/).
- **e. Resilience** [JUDGMENT]: industrial software with low sensitivity to the AI-capex scenarios. The deal needs regulatory approvals, with a French acquirer.
- **Transitions:**
  - (2) No usage pricing found.
  - (4) and (7) Responding with AI assistants and MCP integration, connecting to agents rather than competing with them [COMPANY CLAIM/SECONDARY].
  - (6) Not a verified-software player.
- **Provisional verdict:** partly coherent; its standalone path is now moot [JUDGMENT].

#### Dassault Systèmes (Euronext Paris: DSY), owner of CATIA Magic/Cameo MBSE and Reqtify
- **a. Position.** It sells seat and subscription authoring tools. It owns no judge [JUDGMENT].
- **b. Lead.** Q3 2026 (released 28 Oct 2026): 3DEXPERIENCE software +25%; cloud +14% [PRIMARY]. No MBSE share data was found.
- **c. Revenue model.** Q3 IFRS revenue EUR 1.55B (EUR 1.46B a year earlier); total and software revenue +5% in constant currency; ARR +6% [PRIMARY] — [Dassault Q3](https://www.3ds.com/newsroom/press-releases/dassault-systemes-strong-q3-performance-improved-fy26-objectives-and-step-change-life-sciences.md). The licence and subscription split was not obtained.
- **d. Financial strength.**
  - Q3 margins and EPS: non-IFRS operating margin 31.6% (+150 bps); IFRS 20.9%; non-IFRS diluted EPS EUR 0.32 (+8%); IFRS EPS EUR 0.22.
  - Cash: operating cash flow +20% year to date; cash conversion 111%.
  - FY2026 objectives raised: revenue EUR 6.399-6.459B (+4-5%), operating margin 32.5-32.7%, EPS +6-7% [PRIMARY].
  - The $1.8B ArisGlobal acquisition is complete [PRIMARY]. Net cash (net debt/equity -0.11); ROIC 16.9% [SECONDARY] — [stockanalysis](https://stockanalysis.com/quote/epa/DSY/financials/ratios/).
- **e. Resilience** [JUDGMENT]: diversified (industry plus life sciences) and only weakly tied to the AI-capex scenarios. China exposure was not obtained.
- **Transitions:** no usage-pricing or AI-specification evidence was found this pass.
- **Provisional verdict:** partly coherent as a company; immaterial to specification and verification [JUDGMENT].

#### Agnisys (private, US/India)
- **a. Position.** It sells "golden executable specification" authoring tools (IDesignSpec, IDS-NoC, IDS-AI, iSpec.ai) built on consortium formats. It owns no judge [JUDGMENT].
- **b. Lead.** Named customers and the Axiomise partnership only [COMPANY CLAIM] — [Agnisys](https://www.agnisys.com/news/).
- **c-e.** Revenue, ownership and financials were not found [UNVERIFIED].
- **Provisional verdict:** partly coherent at best. AI features have shipped, but there is no evidence of scale or pricing change. The Defacto-to-Siemens precedent suggests an exit through acquisition [JUDGMENT].

#### MathWorks (private; brief)
- $1.5B revenue; profitable every year; 5M users; TÜV SÜD-certified agentic-AI guidance (14 Oct 2026) [COMPANY CLAIM / PRIMARY headline]. The Simulink model is the executable specification in regulated model-based design (DO-331 covers model-based development). That is the closest any tool vendor comes to owning the specification of record.
- **Provisional verdict:** coherent, but not investable [JUDGMENT].

### Inferences
- [JUDGMENT] Arm belongs among the 8-15 companies that matter most globally in verification and specification: it owns the dominant machine-readable architecture specification and its judge. MathWorks matters, but as a private company. Arteris is a watch-list name: its royalty model is right, but it is small, loss-making and owns no judge. PTC, Dassault, Jama and Agnisys do not belong there; their specification tools are seat- or time-licensed authoring layers. The non-profit judges (RISC-V International, Accellera/IEEE, USB-IF) and the foundries matter institutionally (TSMC is covered elsewhere).

### Gaps
- Not obtained: the full Arm 20-F (gross margin and China detail), Dassault's licence and subscription split, Codebeamer revenue, and Agnisys financials.

## 5. Entry point (listed companies; separate from quality evidence; not advice)

### Takeaway
On closes of 11 Nov 2026:
- Arm trades at about 39x sales and about 180x free cash flow, a price that assumes years of very fast growth.
- Arteris trades at about 9.9x sales, near the top of its post-2022 range, while still loss-making.
- PTC is pinned to Schneider's $205 cash offer.
- Dassault, at about 5.2x sales, is near the bottom of its five-year range.

### Cited Findings
- Prices on closes of 11 Nov 2026 [SECONDARY aggregator] — [AIP](https://stockanalysis.com/stocks/aip/); [ARM](https://stockanalysis.com/stocks/arm/); [PTC](https://stockanalysis.com/stocks/ptc/); [DSY](https://stockanalysis.com/quote/epa/DSY/); [IBM](https://stockanalysis.com/stocks/ibm/):
  - Arteris: $20.32; market cap $1.01B; EV $915.6M; 49.74M shares; 52-week range $12.06-$50.26; TTM revenue $92.98M; P/S 10.87; EV/sales 9.85; forward P/S 9.24.
  - Arm: $203.36; market cap $217.6B; EV $214.5B; 52-week range $100.02-$452.70; TTM revenue $5.46B; P/E 231.5; forward P/E 78.99; P/S 39.8; EV/sales 39.25; cash $3.62B; debt $0.5B.
  - PTC: $196.14; market cap $21.28B; EV $22.85B; P/E 21.96; EV/sales 8.36; EV/EBITDA 21.9; 52-week range $108.50-$196.79 (deal price $205).
  - Dassault: EUR 25.33 (12 Nov 2026 at 12:50 CET, delayed); market cap EUR 33.53B; EV EUR 32.49B; P/E 25.59; forward P/E 17.81; EV/sales 5.16; EV/EBITDA 16.85; 52-week range EUR 15.83-26.39.
  - IBM: $248.22; market cap $234.6B; P/E 21.17; forward P/E 18.99; 52-week range $199.19-$332.46.
- Against own history [SECONDARY]:
  - Arteris EV/sales: 9.85 now; 9.14 (FY2025); 6.36 (FY2024); 3.27 (FY2023); 1.49 (FY2022); 17.39 (FY2021). P/S: 10.87 now; 9.59, 7.09, 4.05, 2.85, 17.43. P/FCF 466 (FY2025: 127) — [ratios](https://stockanalysis.com/stocks/aip/financials/ratios/).
  - Arm (FYE March): EV/sales 39.25 now; 32.03 (FY26); 27.49 (FY25); 39.07 (FY24). P/E 231.5 against 177.7, 142.1 and 419.9. EV/EBITDA 190 against 148, 118 and 767. P/FCF 180 against 164, 632 and 129. ROIC 13.3% now against 14.8% (FY26) and 23.8% (FY25) — [ratios](https://stockanalysis.com/stocks/arm/financials/ratios/).
  - PTC (FYE Sep): EV/sales 8.36 now; 6.03 at FY2026 year-end (pre-deal); 9.32 (FY25); 10.20 (FY24); 8.82 (FY23); 7.03 (FY22). P/E 21.96 against 14.73, 33.13, 57.67, 68.57 and 39.24. EV/EBITDA 21.9 against 15.8, 23.0, 33.5, 31.7 and 23.2. P/FCF 24.4 against 17.5, 28.4, 29.5, 28.7 and 29.6. Debt/equity 0.53 — [ratios](https://stockanalysis.com/stocks/ptc/financials/ratios/).
  - Dassault: EV/sales 5.16 now; 4.81 (FY25); 6.91 (FY24); 9.71 (FY23); 7.81 (FY22); 14.40 (FY21). P/E 25.6 against 26.2, 36.6, 55.4, 47.3 and 88.9. EV/EBITDA 16.9 against 18.4, 26.8, 39.1, 28.7 and 55.6. P/FCF 19.5 against 21.3, 30.0, 41.0, 31.6 and 45.6. Market cap EUR 33.5B against EUR 68.8B at end-2021 — [ratios](https://stockanalysis.com/quote/epa/DSY/financials/ratios/).
- Peers (sibling-note snapshots) [SECONDARY]:
  - Cadence: EV/sales 14.94; forward P/E 34.94; trailing P/E 65.47 — [stockanalysis CDNS](https://stockanalysis.com/stocks/cdns/statistics/).
  - Synopsys: EV/sales 10.17; forward P/E 26.26; net debt $7.23B (cross-ref sector_valuation_cycle.md) — [stockanalysis SNPS](https://stockanalysis.com/stocks/snps/statistics/).
- Recent path (the visible history covers only Sep-Nov 2026) [SECONDARY]:
  - Arm: $333.20 on 22 Sep 2026 → $166.72 on 5 Nov (-13.1% that day) → $203.36 on 11 Nov (+12.1%) — [history](https://stockanalysis.com/stocks/arm/history/).
  - Arteris: $24.78 on 22 Sep → $15.93 on 5 Nov (-12.0%) → +11.7% on 6 Nov → $20.32 — [history](https://stockanalysis.com/stocks/aip/history/).
  - Dassault: EUR 20.17 on 9 Sep → EUR 26.19 on 5 Nov; -4.5% on 28 Oct, then +6.3% on 29 Oct — [history](https://stockanalysis.com/quote/epa/DSY/history/).
  - The aggregator's 52-week extremes ($452.70 for Arm, $50.26 for Arteris, EUR 15.83 for Dassault) could not be checked against the visible history.
- Share of revenue from seats or licences and services:
  - Arteris Q3: licensing, support and maintenance 87%; royalties 9%; services 4% [CALC from PRIMARY].
  - Arm Q2: licence and other 54%; royalties 46% [CALC].
  - PTC: licence 40.4% (almost all recurring subscription); support and cloud 56.1%; services 3.5% [CALC].
  - Dassault: split not obtained.
- Near-term events:
  - Arteris: the Cycuity earn-out is measured on bookings to 31 Dec 2026 [PRIMARY]; Q4 and FY2026 results (date not verified).
  - Arm: Judge Noreika's Section 8.3 ruling (date "not yet known") [SECONDARY]; first AGI CPU deliveries in Q4 FYE27 [COMPANY CLAIM]; Q3 FYE27 results (date not verified).
  - PTC: the special-meeting date is still blank in the PREM14A; close expected by Q3 2027 [PRIMARY].
  - Dassault: FY2026 results (date not verified).
- Private companies:
  - Jama: about $1.2B buyout by Francisco Partners (2024).
  - Flow Engineering: $750M post-money (Sep/Oct 2026).
  - Tessl: about $750M reported (Nov 2024).
  - Antithesis: $105M Series A (Dec 2025); valuation not found.
  - MathWorks: privately held. dSPACE and Vector: private.
  - Agnisys: ownership not found.
  - Defacto: now Siemens (price not found). Valispace: now Altium/Renesas.
- IBM (one line): DOORS and ELM are not disclosed separately and are immaterial to IBM's $234.6B valuation [JUDGMENT].

### Inferences
- [CALC/JUDGMENT] Arm's EV is about 177x TTM free cash flow ($214.5B / $1.212B). To reach a 20x free-cash-flow multiple in five years, free cash flow would have to grow about 55% a year [CALC, illustrative]. So the price assumes the AGI CPU business scales and royalties keep compounding without lasting damage from the Qualcomm remedy. A more attractive entry would require that remedy risk be resolved, or EV/sales returning toward the FY2025 level of about 27x.
- [CALC/JUDGMENT] Arteris's EV is about 8.7x the midpoint of FY2026 ACV-plus-royalty guidance ($915.6M / $105M). That prices in continued growth of more than 20% and a move to GAAP profit. Entry would look more attractive near the FY2024 multiple of about 6.4x sales with royalties still compounding, or after a demonstrated GAAP operating profit.
- [CALC] PTC's spread to $205 is 4.5%, about 5-7% annualised if the deal closes between mid-2027 and Q3 2027. That is merger arbitrage, not a quality call.
- [JUDGMENT] Dassault's price assumes mid-single-digit growth at about 32% margins. It sits at the low end of its five-year EV/sales range (4.8-14.4x), below Synopsys (10.2x) and Cadence (14.9x).

### Gaps
- Not verified: next earnings dates (Arteris, Arm, Dassault); the 52-week extremes; Arm's related-party revenue; PTC's special-meeting date; Dassault's licence and subscription mix.

## 6. Closing lists

### What I could not verify
- Agnisys ownership, revenue and headcount. Revenue for Jama, IBM ELM, Codebeamer and Cameo/Reqtify. Pricing pages for Jama and IBM.
- Fees or compliance programmes for PCI-SIG, JEDEC, MIPI, CXL and UCIe. RISC-V certification fees, labs and first certificates. RVA23 status. Foundry design-kit access terms.
- Perforce, Visure, ETAS, Quint, Alloy. Korean, Chinese and Israeli requirements vendors.
- The date of the Section 8.3 ruling; the $300M-a-year remedy estimate; Arm's 30.5% related-party estimate; the 52-week extremes; next earnings dates.
- The content of the MathWorks/TÜV SÜD guidance; the FAA AI roadmap; post-2024 EASA rulemaking; DO-330 TQL and ISO 26262 TCL details; ISO/PAS 8800.
- Erdős #124 at the primary source; the exact OJ dates of the AI Omnibus; the Defacto price; Tessl's 2026 status; Antithesis pricing and valuation.
- Any independent evaluation of a named vendor's requirement or specification AI. Any regulator accepting AI-written specifications.

### Where current evidence contradicts the background views
- Defacto is not an independent French vendor: Siemens announced its acquisition on 21 Jul 2026.
- arXiv 2609.05658 is not shown to be an Arm study. It has a single author with no stated affiliation and tests two small open models.
- The AlphaProof Code figure of about 26,000 lines is confirmed, but about 8,000 of those lines are AArch64 semantics and symbol names, not hand-written properties. Note also the blog's "over six million" against the paper's "about 6.5 million" lines.
- The prior that value moves to writing specifications is only partly supported. Writing specifications is also becoming cheap. The scarce, paid items are the judge (Arm's ACK, compliance logos, foundry certification) and accountable sign-off.
- The expectation that seat-priced requirements tools are under pressure does not show in incumbents' reported numbers (PTC ARR +9.7% in constant currency with 95.9% recurring revenue; Dassault ARR +6%). PTC was bought at a 42.3% premium. The pressure is visible in valuation multiples and in entrants' usage pricing.
- RISC-V certification is still forming (CRD approved Mar 2026), not yet an established judge.
- The EU AI Act high-risk duties are not in force from Aug 2026; they now start 2 Dec 2027 and 2 Aug 2028.

### Sources with dates
- 2026-11-10: DeepMind AlphaProof Code (project page, blog, paper); see section 2.
- 2026-11-05 / 2026-11-04: Arteris Q3 release and 10-Q; Arm Q2 FYE27; PTC FY2026.
- 2026-11-12 (pages accessed): stockanalysis quotes, ratios and histories; Antithesis; Spec Kit; Sail; Kiro; USB-IF; UCIe; Agnisys; MathWorks newsroom; P; TLA+ Foundation.
- 2026-10-30: Sosso et al., arXiv 2605.23772 v2.
- 2026-10-28: Dassault Q3.
- 2026-10-26: SemiWiki on FSL 1.0.
- 2026-10-23: EE Times, "Two Dollars and a Test Suite".
- 2026-10-22: Anthropic/Theorem formal verification.
- 2026-10-05 / 2026-10-04: Schneider-PTC 8-K and merger agreement; later PREM14A.
- 2026-10-01: SiliconANGLE on Flow Engineering.
- 2026-09: arXiv 2609.03230 (3 Sep) and 2609.05658 (4 Sep); Siemens/Wilson study (8 Sep); Futurum on TSMC OIP (24 Sep); Orrick on the CRA.
- 2026-08-12: SemiWiki on Defacto. 2026-08: Accellera newsletter.
- 2026-07-21: Siemens acquires Defacto. 2026-07-17: CVE-2026-14979. 2026-07: AI Omnibus law-firm notes.
- 2026-06: Ground False (ICML 2026); arXiv 2606.16541; HierSVA; MONOist on PTC NEXT.
- 2026-05-26: AssertLLM2. 2026-05: Jama MCP (yespress).
- 2026-04-03: aslref v1.0. 2026-04: arXiv 2604.15222 and 2604.11044.
- 2026-03-20: AbsInt CompCert. 2026-03-16: VERINA v3. 2026-03-10: RISC-V CRD approval (wiki). 2026-03-02: Accellera CDC/RDC 1.0. 2026-03 (dated 03/26): MathWorks fact sheet. 2026-03-23: Fortune on Antithesis.
- 2026-02-25: AssertLLM v4. 2026-01-29: IBM DOORS release notes. 2026-01-15: Codebeamer AI 1.0. 2026-01-14: Cycuity acquisition closed (10-Q).
- 2025: Vericoding (26 Sep); The Register (1 Oct); ASL Readers' Guide (29 Oct); CLEVER v4 (23 Oct); SpecGen v5 (25 Feb); Tessl Spec Registry beta (16 Sep).
- 2024: Jama-Francisco Partners (18 Mar); Valispace-Altium (Feb); Tessl $125M (Nov); EASA Concept Paper Issue 2 (6 Mar).
- 2023: nl2spec (8 Mar).
- Undated reference pages: Wikipedia (DO-178C, ISO 26262, Common Criteria); Accellera downloads.
