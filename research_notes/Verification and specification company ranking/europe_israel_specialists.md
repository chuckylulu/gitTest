# European (ex-Siemens), Israeli, Australian, New Zealand and Canadian companies in chip and software verification and specification

Date of research: 12 November 2026. Status: FINAL. This continues an earlier partial pass made the same day; every sourced fact from that pass is kept, and corrections are flagged "CORRECTION".

Tag legend: [PRIMARY] filing or official document; [INDEPENDENT] confirmed by an outside party; [COMPANY CLAIM] stated by the company only; [SECONDARY] press or analyst report only; [UNVERIFIED] could not be verified.

Method note: in the first pass the shared built-in web-search budget (200 calls across all agents) ran out after about 37 searches. In this pass the built-in search worked for about 17 more queries before the shared budget ran out again. Firecrawl and Exa search returned out-of-credit errors. All other evidence came from fetching known primary, registry, regulator and company URLs directly. "(search summary)" marks a fact taken from a search-engine summary of a page that was not fetched. Quality evidence (sections 1 to 5) is kept separate from exposure evidence (section 6). This is analysis, not investment advice.

## 1. Map: who matters, by country and sub-segment

### Takeaway
Europe's distinctive strength is software "judges": sound analysers and proof tools that certification accepts. The main ones are AbsInt (Astrée, CompCert), AdaCore (SPARK), TrustInSoft, and the rail formal-methods cluster of Prover Technology, ClearSy and Systerel. Israel adds the leading smart-contract prover (Certora), autonomous-vehicle verification (Foretellix), chip-verification services (Veriest, Vtool) and one new simulator start-up (Hiveware). Australia and New Zealand matter through the seL4 proof ecosystem (Proofcraft, Kry10, UNSW). In chip formal verification, Europe has mainly small, services-led specialists (LUBIS EDA, Axiomise) and one owner of an open-source engine (YosysHQ). Independent European tool vendors keep being absorbed: in 2026 Siemens bought Defacto and agreed to buy Lauterbach, and Codasip sold part of its business.

### Cited Findings
**Chip formal-verification and sign-off specialists**
- UK, Axiomise Ltd: Companies House no. 11016128, incorporated 17 Oct 2017 [PRIMARY] https://find-and-update.company-information.service.gov.uk/company/11016128/filing-history ; formal-verification consulting, training and apps (formalISA, footprint launched 6 Feb 2025, floatrix); "over twenty customers in eight years"; 1,600+ engineers trained; no AI features on its site [COMPANY CLAIM] https://www.axiomise.com/ ; partnerships with Akeana (Feb 2026) and Bluespec (Jul 2025) (first pass, URL not recorded) [UNVERIFIED]. Financials in 2.5.
- Germany, LUBIS EDA GmbH (Kaiserslautern): formal sign-off services; FormalOS launched 6 Oct 2026. Details in 2.5.
- Austria/Germany, YosysHQ GmbH (Vienna): maintains the open-source Yosys toolchain and sells the commercial Tabby CAD Suite (monthly releases Apr-Oct 2026, latest 13 Oct 2026). It published an "Interim YosysHQ LLM Policy" on 26 Aug 2026 [PRIMARY company blog] https://blog.yosyshq.com/ . Details in 2.5.
- France, Defacto Technologies: acquired by Siemens on 21 Jul 2026 (cross-reference: Siemens researcher's notes in this folder). I dropped it from in-depth work because it is no longer independent.
- Germany, Lauterbach (debug and trace tools): on 12 Nov 2026 Siemens said it had signed an agreement to acquire Lauterbach [PRIMARY, Siemens speech, via the Siemens researcher's notes] https://assets.new.siemens.com/siemens/assets/api/uuid:b0adfeab-2c49-4993-9319-7b7169cff52d/Presserede-Q4-2026-Presseformat-EN.pdf . Siemens also bought ASTER in Jan 2026 (same notes).
- Czechia/Germany, Codasip (RISC-V processor IP and the Codasip Studio tool; not mainly a verification company): announced an accelerated sale process on 1 Jul 2025, having raised more than EUR 119M in grants and equity (first pass, URL not recorded) [UNVERIFIED]. onsemi bought its low-end RISC-V business for a reported US$14.5M (reported 26 Oct 2026). 27 of about 260 employees transfer, and onsemi gets a licence to Studio. Codasip keeps the Studio IP and is concentrating on CHERI for defence and critical national infrastructure; CEO Ron Black [SECONDARY, Jon Peddie Research citing e15] https://www.jonpeddie.com/news/onsemi-picks-up-codasips-low-end-risc-v-business-for-14-5-million/
- Aldec (Polish operations), AMIQ EDA (Romania), Sigasi (Belgium) and Verifyter (Sweden) were not checked in either pass because the search budget ran out. I make no claim about their current status [UNVERIFIED].

**Emulation, prototyping and simulation**
- Israel, Hiveware (Tel Aviv): came out of stealth on 27 Jul 2026 with a US$24M Series A led by RTP Global. Product: a clean-sheet SystemVerilog digital simulator on standard servers, "up to 10x faster full-chip simulation", with a roadmap to 100x, meant to replace some hardware emulation. Founders Ohad Agami (CEO) and Yaniv Pascal (CTO), both ex-Hailo verification; VP Product Ronen Laviv (ex-Cadence/AWS); 30 people. Pilots with "three of the world's largest semiconductor companies" (unnamed); Intel Ignite alumnus [COMPANY CLAIM] https://hiveware.io/hiveware-emerges-from-stealth-with-24-million-in-rtp-global-led-series-a/ . The round, US$24.0M led by RTP Global per the link slug, also appears in SemiEngineering's Q3 2026 round-up [SECONDARY] https://semiengineering.com/startup-funding-q3-2026/
- No independent European emulation or prototyping hardware vendor was found (not searched exhaustively).

**Verification IP**: no independent European or Israeli verification-IP vendor was found in either pass (gap).

**AI-native chip-verification entrants founded or funded in 2025-2026**
- UK, Mach42 (Oxford and Palo Alto): US$9.5M pre-Series A on 21 Jul 2026, led by IP Group with BGF and Foresight. Builds surrogate models for analog verification, claimed "up to 2,500x faster"; integrates with Cadence Virtuoso [COMPANY CLAIM] https://mach42.ai/resource-Mach42Secures9.5MilliontoAccelerateAgentic-.html . The same round appears as "Mach42 Completes £7M Funding Round, Led by IP Group" (Business Wire, 21 Jul 2026, listed on IP Group's quote page) [SECONDARY] https://stockanalysis.com/quote/lon/IPO/
- UK, Tattvam AI: US$1.7M pre-seed, Feb 2026 [SECONDARY] https://semiengineering.com/startup-funding-q1-2026/
- Switzerland, Chipmind (Zurich): pre-seed of about US$2.5M in Oct 2025, led by Founderful. Builds AI agents that plug into existing chip-design tools for design and verification tasks; CEO Harald Kroell, CTO Sandro Belfanti [SECONDARY] https://tech.eu/2025/10/21/chipmind-exits-stealth-with-25m-to-launch-ai-agents-for-faster-chip-design/ . CORRECTION: a startuphub.ai profile placing Chipmind in Tel Aviv with US$25M raised appears to be wrong, probably a misreading of US$2.5M https://www.startuphub.ai/startups/chipmind
- US/India/Israel, VerifAIX (Cupertino): US$5M seed announced 30 Sep 2026, co-led by Bluehill VC and Endiya Partners. Founders Madhulima Tewari, Avner Landver and Kenneth Roe; teams in the US, India and Israel; adviser Aarti Gupta [COMPANY CLAIM] https://verifaix.com/verifaix-raises-5m-seed-funding-co-led-by-bluehill-vc-and-endiya-partners/
- Germany, sci2sci (Berlin): EUR 1.2M pre-seed, Sep 2026 (first pass, URL not recorded) [UNVERIFIED].
- SemiEngineering's Q2 2026 round-up lists no European or Israeli verification entrants; Quanscient (Finland, US$11.6M Series A) does simulation [SECONDARY] https://semiengineering.com/startup-funding-q2-2026/
- Outside these regions, for context:
  - Normal Computing (New York) raised US$50M strategic in Mar 2026, led by Samsung Catalyst Fund, for auto-formalisation in design verification and RTL plus formal proofs [SECONDARY] https://semiengineering.com/startup-funding-q1-2026/
  - &Truth (US/Singapore) raised a US$70M seed on 29 Oct 2026. It is Lean-based, with co-founders Clark Barrett and Ilya Sergey. Its demo verified part of Signal's encryption code "in under half a day for under $500", against "five months with three engineers" [SECONDARY] https://dealroom.co/news/168019-truth-emerges-from-stealth-with-70m-seed-to-mathematically-prove-code-is/
- Canada: Astrus (Toronto) raised a US$12M Series A for analog layout, which is not verification [SECONDARY] https://semiengineering.com/startup-funding-q3-2026/ . No notable Canadian verification specialist was found; coverage here is thin.

**AI-verification and AI-security start-ups (not chip verification)**
- UK, Safe Intelligence: GBP 4.15M seed, Feb 2025 (verification of AI models).
- Israel:
  - Attestable (Israel/California): US$20M seed from TLV Partners and Altimeter; cryptographic verification of AI behaviour.
  - Arato: US$10M seed, June 2026; AI application testing.
  - These were found in the first pass, URLs not recorded [UNVERIFIED].
  - Irregular (AI security): emerged with US$80M (search summary) [SECONDARY].

**Software proof and sound static analysis**
- Certora (Israel/US) is assessed in 2.1, AdaCore with CodeSecure (France/US) in 2.2, AbsInt (Germany) in 2.3 and TrustInSoft (France) in 2.4.
- France, Cryspen SAS (Paris; formal verification of cryptographic code): SIREN 908684848, created 21 Dec 2021, staff band 3-5 (2024), President Kiefer. FY2024 revenue is reported as 0 with a net result of EUR +707,846. That is unusual, possibly grants or other income; the registry gives no explanation [PRIMARY] https://annuaire-entreprises.data.gouv.fr/entreprise/908684848
- Sweden, Prover Technology AB (Stockholm): products Prover Studio, iLock, Certifier and Trident. Customer logos include Trafikverket, Alstom, MTA NYCT, Siemens, Thales, SL, Infrabel, RATP, Hitachi Rail STS and Canadian Pacific. On 23 Sep 2026 Prover, RATP and Systerel published a unified HLL 4.0 specification. Also a webinar, "Signaling Design Automation, accelerated by AI" [COMPANY CLAIM] https://www.prover.com/
- France, ClearSy (Aix-en-Provence, founded 2001): Atelier B (the B method), the CLEARSY Safety Platform, and SIL1-SIL4 systems. Says it has worked 25 years with Alstom on automated metros (27 Oct 2026) and won SIL2 certification for a driver-machine interface (5 Oct 2026) [COMPANY CLAIM] https://www.clearsy.com/en/ . Registry: SIREN 433901402, staff band 100-199 (2024); latest published accounts FY2017, revenue EUR 10,277,884, net income EUR 673,913 [PRIMARY] https://annuaire-entreprises.data.gouv.fr/entreprise/433901402
- France, Systerel (Aix-en-Provence): S2OPC (open-source certified OPC UA), Smart Solver (formal verification for SCADE, C and Ada) and OVADO2 data validation [COMPANY CLAIM] https://www.systerel.fr/en/ . Registry: SIREN 440146504, staff band 100-199, owned by Groupe Systerel; FY2024 revenue EUR 11,589,545, net income EUR 508,357 [PRIMARY] https://annuaire-entreprises.data.gouv.fr/entreprise/440146504
- UK, Diffblue Limited (AI-written unit tests for Java; testing, not proof): Companies House no. 09958102, incorporated 19 Jan 2016 (first pass; registry page URL not recorded).
- UK/US, Imandra: CodeLogician (Mar 2025); paper arXiv 2601.11840 (Jan 2026) https://arxiv.org/abs/2601.11840 ; US$5M seed in 2019 from Live Oak, IQ Capital and AlbionVC (first pass, URL not recorded) [UNVERIFIED].
- Australia, Proofcraft (seL4 proof engineering) [COMPANY CLAIM] https://proofcraft.systems/ :
  - quoted in WIRED on AI-generated proofs, 5 Nov 2026;
  - reported a "Significant improvement in the maintainability of seL4 proofs", 21 Sep 2026;
  - gave the FDL keynote, 10 Sep 2026;
  - INSPECTA team member in DARPA PROVERS, led by Collins Aerospace, and at the seL4 Summit 2026 (first pass, URL not recorded) [UNVERIFIED].
- New Zealand, Kry10 (seL4-based KOS operating system): offices in Wellington, Pyrmont NSW, Seattle and Thames Ditton. Products are KOS, guard devices (OT Network Guard, Medical Network Guard) and workload security [COMPANY CLAIM] https://www.kry10.com/ . A database lists a US$6M pre-Series A in Jan 2024 [UNVERIFIED].
- seL4 Foundation members (page fetched 12 Nov 2026; it says the list "will be updated once the transition is completed") [PRIMARY] https://sel4.systems/Foundation/Membership/ :
  - Premium: NIO.
  - General: Apple, DornerWorks (founding member; endorsed service provider), Gapfruit, Kry10 (endorsed service provider), MEP, Neutrality, Proofcraft (endorsed service provider), RTX Corporation, Skykraft Pty Ltd.
  - Associate: ANU, Autoware Foundation, Cyberagentur, ETH Zurich, Fraunhofer AISEC, Kansas State University, Lewis & Clark College, NCSC, Riverside Research Institute, Trusted Computing Center of Excellence, TU Munich, University of Kansas, UNSW Sydney (founding member; endorsed service provider).

**Requirements, safety and test-tool vendors**
- Germany, QA Systems GmbH (Waiblingen; "since 1996"): sells its own Cantata, Cantata Hybrid, Adatest 95 and QA-MISRA, plus AbsInt's Astrée ("Sound analysis proving absence of runtime errors & data races for C/C++"). Covers ISO 26262, IEC 61508, IEC 62304, IEC 60880, EN 50716 and DO-178C. Also offers an "AI Controller" gateway. The site makes no ownership statement [COMPANY CLAIM] https://www.qa-systems.com/
- UK, LDRA: LDRA tool suite, LDRAvault, LDRArules, LDRAcover, LDRAunit and Tool Qualification Support Packs. Covers DO-178C, ISO 26262, IEC 61508 and EN 50716; lists AI/ML among its capabilities; no formal verification. The header logo file is named "ldra-tasking-teal.png", which hints at TASKING ownership but does not state it [COMPANY CLAIM; ownership UNVERIFIED] https://ldra.com/
- UK/Spain/US, Rapita Systems (York, Barcelona, Novi MI): Rapita Verification Suite (RapiTest, RapiCover, RapiTime, RapiTask) and MACH178 for multicore verification. Covers DO-178C, A(M)C 20-193 and ISO 26262. Named customers: Collins Aerospace, Leonardo, Embraer, Cobham, BAE Systems, Triumph, Airbus Defence & Space, Kappa, OHB Sweden and GMV. No formal methods; a webinar on AI-driven requirements traceability is set for 1 Dec 2026; ownership not stated [COMPANY CLAIM] https://www.rapitasystems.com/
- Germany, Vector Informatik: not verified (its company page returned 404).
- Israel, Foretellix (autonomous-vehicle verification): see 2.6.

**Chip verification services**
- Israel, Veriest Solutions: founded 2007; more than 100 engineers; subsidiary of Aman Group since 2013. A release dated 20 May 2026 announces Eli Dagan as CEO, with Moshe Zalcberg moving to chairman [COMPANY CLAIM] https://www.design-reuse.com/news/202530540-veriest-solutions-appoints-eli-dagan-as-chief-executive-officer-moshe-zalcberg-transitions-to-chairman/
- Israel, Vtool: ASIC/FPGA verification firm since 2014, spun off from Veriest. Its only recorded round is undisclosed (Nov 2016), with IXYS Corporation listed as investor. PitchBook shows a 21 Nov 2022 M&A deal involving "P&C Tech Consultants", direction unclear. No acquisition of Vtool is confirmed [SECONDARY, database profiles] https://startupim.com/company/vtool ; https://pitchbook.com/profiles/company/139330-81
- UK, Sondrel: sondrel.com now permanently redirects (HTTP 301) to aionsilicon.com/sondrel, which says only "Sondrel is now Aion Silicon". Whether this was a rebrand or an acquisition, and Sondrel's AIM status, are not stated [PRIMARY company page; details UNVERIFIED] https://aionsilicon.com/sondrel
- UK, EnSilica plc (AIM: ENSI; Companies House 04220106): its investor page is gated by a disclaimer; no financial data retrieved https://www.ensilica.com/investors/
- France, Alten (listed engineering services): see section 6.

**Certification bodies and national schemes**
- UL Solutions, Bureau Veritas and SGS are listed (data in section 6). TÜV SÜD, TÜV Rheinland, DEKRA, SGS-TÜV Saar and exida were not researched (gap). The UK NCSC is an associate member of the seL4 Foundation [PRIMARY] https://sel4.systems/Foundation/Membership/

### Inferences
- The strongest positions in these regions are software tools that certification accepts (CompCert, Astrée, SPARK, the rail B-method chain), not chip formal verification, where European firms mainly sell expert labour.
- Consolidation into the three big EDA vendors continues. Independent European chip-tool vendors look more likely to end up as acquisition targets than as large independent companies.
- Israel's verification strength lies in people and services (Veriest, Vtool, and Foretellix's verification-veteran founders). Hiveware is the only new Israeli verification-tool start-up found.

### Gaps
- Not checked because the search budget ran out: Aldec, AMIQ EDA, Sigasi, Verifyter, Vector Informatik, TÜV, DEKRA and exida.
- No notable Canadian verification specialist was found.

## 2. In-depth company assessments: tests a to e and path forward

### Takeaway
- AbsInt and AdaCore hold the clearest "judge" positions: proof tools that certification accepts, sold to regulated buyers.
- Certora leads its niche but still depends on audit labour and on the crypto cycle.
- TrustInSoft has a sound-analysis judge but is small and loss-making.
- The chip formal-verification group (YosysHQ, LUBIS EDA, Axiomise) is healthy but sells mostly labour.
- Foretellix has strong NVIDIA ties, but its last round was in 2023 and it cut staff in 2026.
- All verdicts below are my provisional judgment.

### Cited Findings

#### 2.1 Certora (Israel/US; smart-contract formal verification)
**a. Position**
- Certora owns the Certora Prover and its specification language, CVL. It open-sourced the Prover on 24 Feb 2025 under GPL v3 (per Chainwire/The Defiant). The announcement names Aave, MakerDAO, Uniswap, Lido, EigenLayer and the Solana Foundation, and claims ">$100bn TVL" (total value locked) and ">70,000 rules" [COMPANY CLAIM] https://certora.com/blog/certora-goes-open-source ; https://thedefiant.io/news/press-releases/certora-open-sources-the-certora-prover-bringing-industrial-grade-formal-verification-to-the-web3-community . The Prover covers EVM, Solana (sBPF) and Stellar (WASM) (search summary).
- On GitHub, CertoraProver has 342 stars and 53 forks (12 Nov 2026) [PRIMARY] https://github.com/Certora/CertoraProver
- AutoProver beta, 15 Jul 2026: reads code and documentation, generates specifications (CVL rules, Foundry tests) and verifies them; "integrates with existing LLMs"; Solidity now, Rust next [COMPANY CLAIM] https://certora.com/blog/autoprover-agentic-formal-verification . An AI Composer alpha came out on 4 Dec 2025 (first pass, URL not recorded) [UNVERIFIED].
- Assessment: Certora's verdict is accepted by the market, not required by any regulator. Open-sourcing moved the engine into the commons. What it can defend now is its specification libraries, its expert team, its hosted compute and its AI agent.

**b. Lead**
- Commissioned press release, 21 Jan 2026, with figures for 2025 [COMPANY CLAIM; Crypto Briefing labels it commissioned] https://cryptobriefing.com/certora-secures-nearly-200-billion-in-defi-value-in-2025-preventing-over-700-vulnerabilities-across-leading-protocols :
  - US$196.5bn of DeFi TVL secured, of which more than US$90bn "by design" through formal verification;
  - more than 720 vulnerabilities stopped before production;
  - 14 of the top 20 DeFi protocols by TVL worked with Certora, and 7 of the top 10 are on continuous engagements;
  - about 150 audits, finding 80 critical and 180 high-severity issues, 99% fixed before deployment;
  - 11 launches delayed or halted on its advice;
  - research team doubled to about 40, including 25 PhDs;
  - CEO Seth Hallem; founder and chief scientist Mooly Sagiv; founded 2018.
- Aave:
  - The Aave DAO approved a proposal in Oct 2025 for US$2.39M over 12 months of continuous security: formal verification, manual audits and fuzzing (as reported in Certora's blog, 10 Nov 2026) [COMPANY CLAIM; on-chain record not fetched].
  - An Aave V4 security-framework release cites 800+ rules and 28 vulnerabilities prevented [COMPANY CLAIM] https://yellow.com/press-releases/certora-and-aave-reveal-security-framework-behind-aave-v4-following-six-year-collaboration ; https://cryptobriefing.com/certora-and-aave-reveal-security-framework-behind-aave-v4-following-six-year-collaboration
- Outside validation:
  - Ethereum Foundation grant, Feb 2026, amount undisclosed. The search summary says it funds work with Powdr Labs on proving that autoprecompile generation is correct [SECONDARY] https://www.chaincatcher.com/en/article/2243764
  - Canton grant of about US$300K, 21 May 2026 (first pass, URL not recorded) [UNVERIFIED].
  - ethereum.org lists Certora Prover and AutoProver among its developer tools (search-result listing) [SECONDARY] https://ethereum.org/ta/developers/tools/certora-prover/ ; https://ethereum.org/ta/developers/tools/certora-autoprover/
- AutoProver self-test on the Aave V4 Hub [COMPANY CLAIM] https://www.certora.com/blog/ai-formal-verification-smart-contracts-costs-use-cases :
  - it generated 104 rules and matched properties P-04 and P-05 from Certora's manual audit;
  - P-06 was half proved and half inconclusive within the compute budget;
  - it would have caught issue M-02 but not M-01;
  - Certora admits that AI-written specifications may omit requirements and that experts must review solvency properties.

**c. Revenue model**
- Prover pricing [PRIMARY company page] https://www.certora.com/pricing :
  - Basic: free, up to 2,000 minutes of runtime a month.
  - Premium (on request): unlimited Prover access, up to 10 team members, specification review.
  - Enterprise (on request): audit plus formal-verification retainer, experts write the rules, incident response.
- AutoProver pricing, 10 Nov 2026 [COMPANY CLAIM] https://www.certora.com/blog/ai-formal-verification-smart-contracts-costs-use-cases :
  - Free: US$0 a month, 1 seat, runs billed at standard rates.
  - Pro: US$120 a month, up to 5 seats, 10% off runs.
  - Enterprise: from US$3,000 a month, unlimited seats, committed credits.
  - Runs are paid from organisation credits, and an estimate is shown before the agents start.
- Inference: revenue today is probably dominated by audits and retainers, that is labour (about 150 audits in 2025, a 40-person research team), with a new usage-based layer on top. Certora does not disclose revenue.

**d. Financial strength**
- Last priced round: US$36M Series B in May 2022, led by Jump Crypto with Tiger Global and Galaxy Digital [SECONDARY] https://www.theblock.co/amp/post/147066/certora-announces-36-million-series-b-funding-round-led-by-jump-crypto ; https://www.theblock.co/post/147066/certora-announces-36-million-series-b-funding-round-led-by-jump-crypto . Jump Crypto's investment note, 17 May 2022: https://jumpcrypto.com/writing/scaling-smart-contract-security-why-we-invested-in-certora/
- No 2026 equity round was found. Hebrew-language search returned no Hebrew-press results.
- Hiring continues, including a "Web2 & Mobile Security Researcher" role, which points to moves beyond Web3 https://careers.certora.com/jobs/7663150-web2-mobile-security-researcher , and a Web3 role posted 29 Mar 2026 (search summary) https://careers.certora.com/jobs/7247521-web3-security-researcher-est-to-gmt-4
- Customers are DeFi protocols and DAOs; Aave, Lido, Uniswap and Compound recur. Revenue, margins and runway are not disclosed.

**e. Resilience**
- Certora's own cycle is crypto (DeFi TVL, DAO treasuries), which matters more to it than AI spending.
- Steady AI growth (55%): more AI-written contracts need checking, but AI-written specifications push audit prices down.
- Financing-led pause around 2028 (25%): probably coincides with a fall in crypto and other risky assets, which cuts DAO budgets; a labour-heavy cost base is then a weakness.
- Faster acceleration (20%): well-funded proof start-ups and the AI model makers (covered by other researchers) could commoditise both proofs and specifications. Certora's defence is its rule libraries and installed base.
- No cross-border restriction specific to Certora was found [UNVERIFIED].

**Path forward**
- Transitions it must get through:
  - (1) verification labour to tools;
  - (2) seat licences to pricing by use;
  - (4) proprietary against open-source engines; it has already chosen open source;
  - (6) a paying market for verified software, which already exists in DeFi, where the buyer is the protocol or DAO treasury;
  - (7) model makers offering verification themselves.
- Said versus done:
  - Said: specification first, and agentic verification.
  - Done: open-sourced the Prover (Feb 2025), shipped AutoProver beta (Jul 2026) and usage pricing (Nov 2026), and published its agent's limits.
  - At a Devcon India panel on 3 Nov 2026 (Mooly Sagiv, Vitalik Buterin, Fredrik Svantes of the Ethereum Foundation, Josselin Feist of Aave) the message was "specification before implementation", and "A tool can reason correctly about a specification that describes the wrong behavior" https://www.certora.com/blog/devcon-india-2026-ai-formal-verification
- Funding and timing: 2022 capital plus grants and service cash. Support for Rust, C/C++, Go and Java is still "in development".
- What must go right: protocols must buy verification as credits rather than audits, and Certora must reach beyond Solidity and beyond crypto before AI-native rivals arrive in DeFi.
- Provisional verdict: partly coherent. The plan makes sense and is partly delivered, but revenue still looks labour-based and tied to one cyclical market.

#### 2.2 AdaCore with CodeSecure (France/US; SPARK proof, qualified compilers, static analysis)
**a. Position**
- Products: SPARK Pro (formal proof for a subset of Ada), GNAT Pro (Ada, C/C++, Rust), CodeSonar static analysis (from CodeSecure) and the GNAT Dynamic Analysis Suite [PRIMARY] https://www.adacore.com/press/adacore-and-codesecure-merge
- SPARK acts as a judge where customers adopt it. In NVIDIA's DRIVE OS, critical components are written in Ada/SPARK, and an ISO 26262 process with NVIDIA was announced on 2 Jun 2025 [COMPANY CLAIM] https://www.adacore.com/press/ada-and-spark-enter-the-automotive-iso-26262-market-with-nvidia . NVIDIA published that reference process as open source [INDEPENDENT] https://github.com/NVIDIA/spark-process
- CodeSonar is sold as defect-finding static analysis rather than proof, so it is a weaker judge than SPARK (inference; not checked against CodeSonar documentation in this pass).
- Language risk: Rust plus open verifiers could erode the Ada/SPARK niche. AdaCore is hedging with GNAT Pro for Rust and, from 3 Nov 2026, a collaboration with CMU's Verus team (Bryan Parno) on formally proven Rust [COMPANY CLAIM] https://www.adacore.com/press/adacore-and-cmu-researchers-announce-collaboration-around-formal-verification-of-rust-for-high-integrity-systems

**b. Lead**
- Named adopters: NVIDIA (above). In company releases, Cimarron selected SPARK Pro for its AURORA space middleware (11 Nov 2026) and Renishaw Neuro Solutions uses CodeSonar for neurosurgical robot software (29 Sep 2026) [COMPANY CLAIM] https://www.adacore.com/press . CodeSecure's customers include BMW, Hyundai, Rivian, Denso and LeddarTech [SECONDARY, eeNews Europe] https://www.eenewseurope.com/en/adacore-expands-with-codesecure-merger/
- AdaCore reports a "significant increase" in memory-safe-language design wins in US aerospace and defence, without numbers (30 Jul 2026) [SECONDARY] https://www.militarysystems-tech.com/articles/adacore-reports-growth-memory-safe-language-design-wins-across-us-aerospace-and-defense
- A VDC study commissioned by AdaCore (27 Jul 2026; more than 500 respondents) says memory-safe languages cut costs [COMPANY-SPONSORED] https://www.adacore.com/press/new-vdc-strategy-research-finds-memory-safe-languages-cut-costs-and-strengthen-software-quality
- Other 2026 activity: joined SOAFEE (27 Jan 2026) https://www.adacore.com/press/adacore-joins-the-soafee-initiative-to-advance-high-integrity-software-for-automotive-systems ; exhibited at Embedded World (25 Feb 2026); released a demonstrator for trustworthy AI-assisted development (14 Sep 2026) https://www.adacore.com/press/adacore-releases-demonstrator-for-trustworthy-development-with-ai ; co-organised the High Integrity Software Conference (7 Oct 2026). Cimarron release: https://www.adacore.com/press/cimarron-selects-adacores-spark-pro-for-aurora-resilient-space-middleware

**c. Revenue model**
- Pricing is not published and was not verified. The French entity's high margin (below) fits a licence or subscription business better than a labour business, but it could also reflect transfer pricing within the group.

**d. Financial strength**
- AdaCore SAS, the French entity only; the US entity is not included [PRIMARY] https://annuaire-entreprises.data.gouv.fr/entreprise/403325657 :
  - Paris; SIREN 403325657; created 1 Feb 1996; staff band 50-99 (2024); President Gasperoni, managing director Berrendonner.
  - Latest published accounts, FY2022: revenue EUR 15,623,133, net income EUR 7,146,575, a net margin of about 46%.
- Ownership:
  - Battery Ventures invested on 28 Mar 2024 (amount undisclosed) [PRIMARY] https://www.businesswire.com/news/home/20240328498013/en . GovInfoSecurity says Battery took a majority stake [SECONDARY, not fetched] https://www.govinfosecurity.com/adacore-merges-codesecure-for-unified-developer-tools-a-28772
  - Battery bought GrammaTech in 2023; CodeSecure is GrammaTech's former products division. The merger was agreed on 18 Jun 2025, value undisclosed; headquarters in Paris and New York [SECONDARY] https://www.eenewseurope.com/en/adacore-expands-with-codesecure-merger/
  - Merger release on Business Wire (403 when fetched): https://www.businesswire.com/news/home/20250618194395/en ; French version: https://www.businesswire.com/news/home/20250618146408/fr
- Completion of the merger:
  - The CodeSonar distributor VerifySoft (DACH) said on 18 Jan 2026 that the companies "have merged" [SECONDARY] https://www.verifysoft.com/en_codesonar_news.html
  - AdaCore's 10 Aug 2026 release refers to its "2025 expansion through its merger with CodeSecure" [PRIMARY] https://www.adacore.com/press/adacore-appoints-radhika-holowko-as-chief-revenue-officer-to-drive-next-stage-of-growth
- CORRECTION on leadership: AdaCore's own 10 Aug 2026 release names Franco Gasperoni as CEO and Radhika Holowko as the new Chief Revenue Officer, and the 3 Nov 2026 release calls Quentin Ochem "Chief Product Officer". The 30 Jul 2026 trade article that calls Ochem "President and CEO" appears to be wrong.
- Not disclosed: debt from the Battery-backed merger, group revenue, group headcount.

**e. Resilience**
- AdaCore's own cycle is defence, aerospace, automotive and medical budgets plus memory-safety policy, not AI spending.
- Steady AI growth: AI-written code makes proof-backed languages, and the NVIDIA reference, more valuable.
- Financing-led pause around 2028: customers' safety programmes depend less on AI capital spending, so revenue should hold up better than at chip-tool peers (inference).
- Faster acceleration: AI that writes proofs for mainstream languages (Rust with Verus, or C) is the main threat to a franchise built on one language.
- Export-control exposure was not verified.

**Path forward**
- Transitions: (3) toward formal proof, where it already is; (4) proprietary against open-source plus AI, hedged through Rust and Verus; (6) a paying market for verified software, where the buyers are safety-critical OEMs and prime contractors; (7) model makers.
- Said versus done: it said it would broaden from Ada to Rust and to AI-assisted development. It has delivered GNAT Pro for Rust, the CMU Verus collaboration, the AI demonstrator, a new CRO and the completed merger.
- Funding and timing: owned by a large growth investor and, on the latest French accounts, very profitable; the timing is plausible.
- What must go right: SPARK-style proof must carry over to Rust and to AI-written code before open tools do it for free, and CodeSonar must hold up against AI code reviewers.
- Provisional verdict: coherent.

#### 2.3 AbsInt (Germany; Astrée, aiT, CompCert)
**a. Position**
- Products: Astrée (sound static analyser), aiT (worst-case execution-time analyser) and CompCert (a formally verified C compiler).
- On 20 Mar 2026 AbsInt said CompCert had been qualified for the ATR 42/72 MFC_NG. It called this the first time certification credit had been claimed for using a compiler under DO-178C/DO-333/DO-330; no certifying authority is named [COMPANY CLAIM] https://www.absint.com/releases/260320.htm
- The CompCert project site says the same and states that AbsInt developed CompCert with guidance from Airbus [PRIMARY project site] https://compcert.org/ . CompCert 3.18 came out in 08/2026.
- Also on the company site: an ERTS 2026 paper, "Qualifying CompCert for Safety-Critical Avionics Software", and product release 26.10 https://www.absint.com/
- This is the strongest judge position found in these regions: a qualified tool whose output certification accepts, and that AI does not remove, since AI-written code still needs a sound check and a trusted compiler.

**b. Lead**
- Customers named on its site: Airbus (two decades; A380 flight control), ATR, Honda (FADEC), Daimler (Actros), Bosch Automotive Steering, Continental/Aumovio, OHB, ESA, Framatome (TELEPERM XS), MTU, Vestas and u-blox; customers in 40+ countries [COMPANY CLAIM] https://www.absint.com/
- Third-party channel: QA Systems, a German tool vendor, resells Astrée alongside its own tools [INDEPENDENT] https://www.qa-systems.com/
- The DO-178C credit is the strongest evidence, but the certifying authority is not named publicly.

**c. Revenue model**
- Licence and maintenance terms are not published (not verified).

**d. Financial strength**
- AbsInt Angewandte Informatik GmbH: HRB 11234, Amtsgericht Saarbruecken; LEI 39120010X9VSHSNMEC26. Founded 1998 and privately held [COMPANY CLAIM] https://www.absint.com/releases/260320.htm
- Accounts are filed for FY2006 to FY2025 (FY2025 published 2 Jul 2026), but the figures sit behind North Data's paywall and were not retrieved from the Bundesanzeiger [PRIMARY-derived] https://www.northdata.com/AbsInt+Angewandte+Informatik+GmbH,+Saarbr%C3%BCcken
- No outside investors were found.

**e. Resilience**
- AbsInt's own cycle is aerospace, automotive, energy and nuclear programmes. It depends little on AI spending in any of the three scenarios; a 2028 financing pause would reach it mainly through customers' programme budgets.
- It exports to customers in 40+ countries; cross-border restrictions were not verified.

**Path forward**
- Transitions: (3) it is already formal; (5) certification as a barrier works in its favour, as foundry certification does for chip sign-off tools; (4) open tools and (7) model makers are the long-run risks.
- Said versus done: it claimed and delivered the CompCert qualification (Mar 2026).
- Funding and timing: self-funded; scale unknown.
- What must go right: further qualifications (other aircraft programmes, ISO 26262, EN 50716), and a channel into AI-assisted development flows.
- Provisional verdict: coherent. The position is strong, but the company is small and opaque.

#### 2.4 TrustInSoft (France/US; sound static analysis for C, C++ and Rust)
**a. Position**
- TrustInSoft Analyzer (TISA) aims to prove the absence of undefined behaviour. Offices in San Francisco and Paris. Products: Analyzer, Formal Verification Services and Rust Code Analysis Services. Claims "AI automates up to 90% of the setup" [COMPANY CLAIM] https://www.trust-in-soft.com/
- It is a judge-type tool for memory safety, but no certification standard names it yet.

**b. Lead**
- TISA 26.10 (Oct 2026) adds AI-assisted setup. CEO Caroline Guillaume was quoted by Embedded Computing Design (22 Sep 2026), which also gave TrustInSoft an "embedded world Best in Show" award [SECONDARY] https://embeddedcomputing.com/application/industrial/automation-robotics/embedded-computing-design-announces-trustinsoft-wins-embedded-world-best-in-show-award
- The April 2026 release added AI-generated drivers and stubs, Rust support and better MC/DC coverage (press release, 10 Mar 2026) [COMPANY CLAIM] https://lifestyle.xpr.media/story/3705/trustinsoft-announces-ai-powered-advancements-in-april-2026-release/ ; Embedded World 2026 recap: https://www.trust-in-soft.com/resources/blogs/recapping-embedded-world-nuremberg-2026
- Partnership with Ferrous Systems on Rust, 25 Feb 2025 (first pass, URL not recorded).
- The company says NIST recognised it for its formal methods (search summary) [COMPANY CLAIM].
- No named customers were verified (gap).

**c. Revenue model**
- Licences plus formal-verification services (labour); the split is not disclosed. AI setup automation is meant to move work from services into the tool.

**d. Financial strength**
- TrustInSoft SAS [PRIMARY] https://annuaire-entreprises.data.gouv.fr/entreprise/793371907 : SIREN 793371907; created 2 May 2013; staff band 20-49 (2024); President Guillaume, managing director Monate. FY2024 revenue EUR 5,892,618, net loss EUR 1,578,984 (a margin of about -27%).
- Last disclosed round: EUR 5M in Nov 2019, led by ACE Management (Brienne III fund), with Idinvest an earlier investor [SECONDARY, CFNEWS] https://www.cfnews.net/L-actualite/Capital-innovation/Operations/2nd-tour/TrustInSoft-securise-un-deuxieme-tour-313617
- No later round was found; runway is unknown.

**e. Resilience**
- TrustInSoft's own cycle is regulation-driven memory-safety demand (CRA, Product Liability Directive, US memory-safety roadmaps).
- Steady AI growth helps: there is more C/C++ and AI-written code to check.
- A financing pause exposes a loss-making firm with no recent disclosed round.
- Faster acceleration brings AI-driven provers aimed at C into direct competition (covered by other researchers).

**Path forward**
- Transitions: (1) services to tools; (6) a market created by regulation; (4) and (7) AI competition.
- Said versus done: the AI-assisted releases shipped on schedule (April and October 2026).
- Funding and timing: unclear; it needs either profitability or new capital.
- What must go right: a certification or regulatory hook that makes sound analysis mandatory (for example in automotive or rail), and growth that outruns the losses.
- Provisional verdict: partly coherent. The technology is strong but funding visibility is weak; a plausible acquisition target (inference).

#### 2.5 Open-source and formal chip-verification group (YosysHQ, LUBIS EDA, Axiomise)
**a. Position**
- YosysHQ owns an open engine (Yosys and related formal tooling) that others build on. For example, the MoonshotAI nano-kpu demonstration uses Yosys (>=0.64) (cross-reference: the AI-native researcher's notes) https://github.com/MoonshotAI/nano-kpu . It is not a sign-off judge.
- LUBIS EDA and Axiomise sell formal sign-off as expert services, training and apps. In this framework that is the weakest position (labour), with some tooling on top.

**b. Lead**
- LUBIS EDA:
  - more than 350 projects, more than 900 bugs found after UVM, 87%+ delivered on time, 15+ repeat customers, 5 "Fortune 25" clients, 55+ staff all in Germany [COMPANY CLAIM] https://lubis-eda.com/
  - 2025 review: 80% team growth, 73% repeat engagements, expansion to Austin and Japan [COMPANY CLAIM] https://semiwiki.com/forum/threads/2025-a-defining-year-for-lubis-eda.24667/
  - FormalOS infrastructure launched 6 Oct 2026 and deployed within LUBIS service engagements; release cites ">325 sign-off projects, >900 bugs" [COMPANY CLAIM] https://www.generation-nt.com/communiques-presse/lubis-eda-launches-formalos-infrastructure-for-systematic-scalable-2082294
  - EU EIC Accelerator award of EUR 2.5M (announced 12 Oct 2023, from 2024), when it had 10 staff and planned more than 30; founder and CEO Dr Tobias Ludwig [PRIMARY, CISPA] https://cispa.de/en/eic-lubis . Selection by the EIC is outside validation.
- Axiomise: more than 20 customers in eight years; 1,600+ engineers trained [COMPANY CLAIM] https://www.axiomise.com/
- YosysHQ: partner in an Austrian FFG project (Jun 2026 to May 2029) on an open-source EDA suite covering design productivity, interoperability and scalable verification; funding present value EUR 153,095 [PRIMARY] https://projekte.ffg.at/projekt/b9e4453e-f36b-1410-864f-00d3c07d99bb/pdf ; https://projekte.ffg.at/projekt/b9e4453e-f36b-1410-864f-00d3c07d99bb . This matches stream (iii) of the EU open-source EDA call (section 4), so YosysHQ is probably in that consortium (inference, not confirmed).

**c. Revenue model**
- LUBIS: fixed-scope or subscription (time-based) engagements, typically 10 to 50 days, so labour [COMPANY CLAIM] https://lubis-eda.com/
- Axiomise: consulting, training and apps; its profit and loss account is not filed.
- YosysHQ: commercial Tabby CAD Suite on top of open source; pricing not verified.

**d. Financial strength**
- Axiomise Ltd, unaudited accounts for 1 Nov 2024 to 30 Apr 2026 (period extended from 31 Oct 2025); small-companies regime, profit and loss not filed; approved 18 Sep 2026 by director Dr Ashish Darbari; filed 21 Sep 2026 [PRIMARY] https://find-and-update.company-information.service.gov.uk/company/11016128/filing-history/MzU0NjAzNjgyM2FkaXF6a2N4/document?format=pdf&download=0 . Comparatives are at 31 Oct 2024:
  - cash GBP 1,556,897 (1,088,732);
  - trade debtors GBP 413,469 (350,698);
  - net current assets GBP 1,641,010 (1,216,603);
  - finance-lease creditors due after one year GBP 76,689 (134,355);
  - net assets GBP 1,719,272 (1,228,796);
  - profit and loss reserve GBP 1,737,397 (1,210,471);
  - share capital GBP 100 (18,325) after a buyback: purchase of own shares filed 8 Jan 2025, cancellation of shares filed 15 May 2025;
  - average employees including directors 25 (2024: 25).
  - Earlier accounts to 31 Oct 2024: https://find-and-update.company-information.service.gov.uk/company/11016128/filing-history/MzQ3NDY2MTk0OGFkaXF6a2N4/document?format=pdf&download=0
  - Inference: self-funded and profitable. Reserves rose by about GBP 0.53M over 18 months after any dividends, and there is no outside equity.
- LUBIS: EIC funding above; accounts not retrieved. YosysHQ: Austrian registry figures not available.

**e. Resilience**
- The group's own cycle is the number of chip design starts, currently lifted by AI chips.
- Steady AI growth: demand for formal sign-off grows.
- Financing-led pause around 2028: services firms lose work first.
- Faster acceleration: AI agents (Chipmind, VerifAIX and others) automate assertion writing and formal set-up, cutting the hours these firms sell.
- Open engines such as Yosys gain if capable AI models make open tools easier to use (transition 4). YosysHQ's interim LLM policy (Aug 2026) shows it is already managing AI-written contributions.

**Path forward**
- Transitions: (1) labour to tools (LUBIS FormalOS, Axiomise apps); (3) simulation to formal proof, their core thesis; (4) open source plus AI, where YosysHQ gains and the service firms could lose. (5) Foundry certification does not cover formal tools, so there is no regulatory moat here.
- Said versus done: LUBIS launched FormalOS but deploys it inside its services, not as a standalone product. Axiomise shows no AI features. YosysHQ ships monthly.
- Funding: modest (EIC EUR 2.5M; Axiomise self-funded; FFG EUR 153K).
- Provisional verdict: partly coherent for LUBIS and Axiomise, which are healthy service firms without a judge-type product. Coherent for YosysHQ as an open-source steward, though its commercial scale is unknown.

#### 2.6 Foretellix (Israel; autonomous-vehicle verification), with Veriest as the services comparator
**a. Position**
- Foretify toolchain (Toolchain, Evaluate, Generate) for coverage-driven scenario testing. Founders: Yoav Hollander (CTO and founder), Ziv Binyamini (CEO and co-founder) and Gil Amid (chief regulatory affairs officer and co-founder). The site links an OpenSCENARIO DSL resource but does not describe Foretellix's role in the standard [COMPANY CLAIM] https://www.foretellix.com/about/
- It sells a method and a tool, not a verdict anyone is required to pass. NVIDIA is both a partner and a potential competitor.

**b. Lead**
- NVIDIA integrations: DRIVE AV (Oct 2025) https://www.foretellix.com/foretellix-foretify-physical-ai-toolchain-integrates-with-nvidia-drive-av ; a reference solution with NVIDIA Alpamayo (31 May 2026); NVIDIA Halos SAFE (21 Oct 2026) [COMPANY CLAIM] https://www.foretellix.com/news-and-events/
- 2025 partnerships: Voxel51, Inverted AI, Parallel Domain, and MathWorks/Mazda (6 Feb 2025) [COMPANY CLAIM] https://www.foretellix.com/news-and-events/ ; Parallel Domain release: https://prnewswire.com/il/news-releases/foretellix-and-parallel-domain-partner-to-bring-hyper-realistic-digital-twins-to-av-simulation-302606979.html
- Won "Autonomous Vehicle Innovation of the Year", 16 Oct 2025 https://www.foretellix.com/?p=35822
- S&P AutoTechInsight reports that Foretify has been extended to train AV software stacks [SECONDARY] https://autotechinsight.spglobal.com/news/5282089/foretellix-expands-foretify-platform-to-train-autonomous-vehicle-stacks
- The About page names no OEM production customers. The main outside validation is its strategic investors (Toyota's Woven Capital, Isuzu, NVIDIA).

**c. Revenue model**
- Not disclosed (gap).

**d. Financial strength**
- Series C of US$85M in total (first close US$43M in May 2023, extension in Dec 2023), bringing total raised to US$135M. Led by 83North with Temasek, Isuzu, Woven Capital and NVIDIA [SECONDARY] https://theaiinsider.tech/?p=21573 ; TechCrunch, 5 Dec 2023: https://techcrunch.com/2023/12/05/foretellix-raises-85m-to-build-and-test-scenarios-for-self-driving-systems
- Funding history (first pass): 2018 US$1.5M; 2019 US$14M; 2021 US$32M; May 2023 US$43M; Dec 2023 US$42M.
- Caplight lists the Dec 2023 Series C as the latest round [SECONDARY] https://www.caplight.com/company/foretellix . No 2026 round was found.
- Laid off 29 people (about 18% of staff) on 8 Jan 2026 "as AI adoption reshapes operations" [SECONDARY, CTech] https://www.calcalistech.com/tags/Foretellix . Inference: about 160 staff before the cut.

**e. Resilience**
- Foretellix's own cycle is funding for autonomous-driving and robotaxi programmes.
- Steady AI growth helps demand for "physical AI" tooling.
- A 2028 financing pause would hit a company whose last round closed in 2023.
- Faster acceleration would favour NVIDIA's own tools.
- Cross-border restrictions were not verified.

**Path forward**
- Transitions: (7) platform owners such as NVIDIA offering verification themselves; (1) AI used internally, as the layoffs suggest.
- Said versus done: repositioned as a "Physical AI toolchain" and delivered the NVIDIA integrations, but raised no new money.
- Provisional verdict: partly coherent, with funding risk.

**Veriest as the services comparator**: Veriest sells verification labour (founded 2007, 100+ engineers, Aman Group subsidiary since 2013, new CEO in May 2026; sources in section 1). That is the weakest position in the framework. Provisional verdict: partly coherent as a services business, not a judge.

### Inferences
- AbsInt and AdaCore, the companies whose verdicts certification already relies on (AdaCore through SPARK), are the most robust across the three AI scenarios because their buyers' budgets are not AI capital spending.
- Certora shows both sides of the AI shift: it built the agent (AutoProver) that will eat into its own audit revenue.

### Gaps
- No revenue data for Certora, AbsInt, LUBIS EDA, YosysHQ, Foretellix or Veriest. No AdaCore group figures. No customer-concentration data for any of them.

## 3. Regulation as a demand driver (transition 6)

### Takeaway
Regulation creates a paying market for verified software mainly where sector safety standards already name formal methods: rail (EN 50716), avionics (DO-178C with DO-333) and Common Criteria EAL6-7. The horizontal EU laws (Cyber Resilience Act, Product Liability Directive) raise liability and process duties for software, but on the evidence found they do not name formal verification or memory safety. The buyer is the product maker that carries the certification or the liability: aircraft and rail suppliers, automotive OEMs, and chip firms such as NVIDIA. In DeFi the buyer is the protocol treasury.

### Cited Findings
- EU Cyber Resilience Act [SECONDARY, Orrick law-firm summary, Sep 2026] https://www.orrick.com/en/Insights/2026/09/EU-Cyber-Resilience-Act-New-Guidance-Clarifies-Scope-Reporting :
  - Article 14 reporting obligations apply from 11 Sep 2026; the main obligations from 11 Dec 2027.
  - Commission guidance: draft 3 Mar 2026, final 27 Jul 2026, non-binding.
  - Free and open-source software is in scope only when placed on the market.
  - Products need a support period of at least five years.
  - The summary does not mention formal verification or memory safety.
- EU Product Liability Directive (EU) 2024/2853 [SECONDARY, law-firm commentary via search summary: CMS; Covington InsidePrivacy, updated 19 Jun 2026; Sidley, Oct 2026] https://cms.law/en/int/publication/the-new-eu-product-liability-directive-eu-2024-2853 ; https://www.insideprivacy.com/uncategorized/eu-member-states-begin-rolling-out-new-product-liability-rules/ ; https://www.sidley.com/en/insights/newsupdates/2026/10/revised-eu-product-liability-directive ; official text, not fetched: https://eur-lex.europa.eu/eli/dir/2024/2853/oj :
  - Member states must transpose it by 9 Dec 2026; it applies to products placed on the market after that date.
  - "Product" expressly includes software (Art. 4), including standalone software.
  - It is maximum harmonisation.
  - As of June 2026, Germany's draft reportedly leaves out Art. 12(2), which limits recourse against small makers of software components.
- Aerospace (DO-178C/DO-333): the CompCert qualification is the first claimed certification credit for compiler use (2.3). Rapita (A(M)C 20-193 multicore) and LDRA (tool-qualification packs) show the DO-178C test-tool market (section 1).
- Automotive (ISO 26262): AdaCore and NVIDIA's Ada/SPARK process (2 Jun 2025), which NVIDIA open-sourced [INDEPENDENT] https://github.com/NVIDIA/spark-process . AdaCore joined SOAFEE (27 Jan 2026). UNECE R155/R156 were not verified.
- Rail (EN 50716:2023), standard text not seen [SECONDARY, vendor pages: MathWorks, Ansys, Verifysoft] https://www.mathworks.com/company/technical-articles/build-railway-applications-en-50716.html ; https://www.verifysoft.com/en_EN_50716_Railway_Applications.html :
  - it replaces EN 50128:2011 and EN 50657:2017;
  - the vendors say it makes formal methods "highly recommended" at all SILs, where earlier standards did so only at SIL 3-4.
  - In practice: the unified HLL 4.0 specification from Prover, RATP and Systerel (23 Sep 2026), ClearSy's SIL2 certificate (5 Oct 2026), and Prover's operator customers (section 1).
- Common Criteria and the EU scheme EUCC (Implementing Regulation (EU) 2024/482) [SECONDARY, certification-lab blogs] https://www.qima.com/blog/due-cybersecurity/mapping-eucc-to-common-criteria-a-technical-overview-of-assurance-levels-and-evaluation-requirements ; https://www.cclab.com/news/implementing-eucc-what-high-assurance-certification-requires-beyond-traditional-common-criteria-approaches :
  - two levels: "substantial" (about EAL1-3) and "high" (about EAL4-7, AVA_VAN.3 and above);
  - EAL6 requires a formal security-policy model, and EAL7 formal verification of the design;
  - the labs disagree on the exact AVA_VAN mapping;
  - protection profiles must be certified or endorsed by the ECCG;
  - no 2026 change to the formal-model requirements was found.
- Memory safety and formal verification guidance:
  - No 2026 UK NCSC publication naming formal verification was found.
  - Joint memory-safety guidance from CISA, NCSC and other agencies is dated Dec 2023 https://ic3.gov/CSA/2023/231206.pdf
  - CISA expects vendors to publish a memory-safety roadmap by 1 Jan 2026 (US; cited in search results, not fetched) [SECONDARY].
  - NCSC New Zealand pages on memory safety and memory-safe roadmaps (dates not verified) https://www.ncsc.govt.nz/news/securing-products-through-memory-safety ; https://www.ncsc.govt.nz/news/advice-for-software-manufacturers-on-creating-memory-safe-roadmaps/
  - A UK NCSC blog lists "formal verification of code" among resilience techniques; this is a blog post, not guidance https://www.ncsc.gov.uk/blog-post/sausages-incentives-rewarding-resilient-technology-future
- Demand-side cost evidence: the AdaCore-commissioned VDC study (27 Jul 2026) and &Truth's claimed cost of under US$500 for a proof (section 1).

### Inferences
- The CRA and the Product Liability Directive raise the cost of shipping defective software from Dec 2026 to Dec 2027 onwards. That favours sound analysers and proof tools (AbsInt, TrustInSoft, AdaCore) as evidence of due care, but nothing found makes them mandatory.
- Sector standards (rail, avionics, high-assurance Common Criteria) remain the real "judges". European rail is the clearest region-specific pull (Prover, ClearSy, Systerel).

### Gaps
- Not seen: the text of UNECE R155/R156, the ISO 26262 tables and EN 50716. No 2026 guidance from ANSSI, BSI or NCSC naming formal verification was found.

## 4. Public funding and open source (transition 4)

### Takeaway
Public money in 2025-2026 does favour open-source design and verification engines, but at small scale. The EU's open-source EDA call totals EUR 20M, and only one of its three streams covers verification. Meanwhile the same Chips Act design platform has signed Siemens to supply commercial tools at preset prices. The UK's ARIA programme has narrowed from building AI-for-proof systems to cybersecurity. Israel and France fund semiconductors broadly, but not verification specifically.

### Cited Findings
- EU Chips Design Platform (EuroCDP): coordinated by imec with a 12-partner consortium; start-ups and SMEs onboarding from early 2026, with access to commercial tools, IP and open-source repositories [SECONDARY] https://itdaily.com/news/business/eu-chips-design-platform ; https://anysilicon.com/imec-coordinates-eu-chips-design-platform/
- Siemens signed a framework agreement with the Chips JU in May 2026 giving platform users access to Siemens EDA at preset prices [SECONDARY] https://www.digitalengineering247.com/article/siemens-opens-up-eda-software-access-for-european-electronics-industry/news
- A Commission document of May 2026 says negotiations to secure significant EDA vendors were expected to conclude by autumn 2026 [SECONDARY, search summary] https://www.cdep.ro/afaceri_europene/CE/2026/COM_2026_504_FR_annexe_proposition_part1_v2.pdf
- Chips JU call HORIZON-JU-CHIPS-2025-IA-EDA-two-stage, "Open-source EDA tools development" (EU Funding & Tenders portal record, fetched 12 Nov 2026) [PRIMARY] https://ec.europa.eu/info/funding-tenders/opportunities/data/topicDetails/horizon-ju-chips-2025-ia-eda-two-stage.json ; secondary listing (403 when fetched): https://fasi.eu/en/grants/a79559f1-f6e2-30f8-9bf8-5279835f4e39
  - Innovation Action; opened 4 Mar 2025; two-stage deadlines 30 Apr 2025 and 17 Sep 2025; now closed.
  - EU budget EUR 20,000,000 (2025). The record expects 4 grants, but the text says "three selected consortia"; EUR 1M-20M each.
  - Three streams: (i) a digital SoC flow for 65-28nm; (ii) an analogue and mixed-signal flow; (iii) "Productivity, interoperability, and verification", including "development of robust verification processes".
  - OSI-approved licences are required, consortia must integrate with the Design Platform's flows, and they must engage foundries for PDKs.
  - A French grants page lists the call as open on 6 May 2026, which conflicts with the portal's "Closed" status [SECONDARY] https://www.grantbite.com/fr/funding/developpement-outils-eda-open-source-horizon-chips
- Austria: projects in the ODE4EC family, funded by the FFG, started 1 Jun 2026 for 36 months. They cover parasitic extraction, hierarchical flows, timing and power, and PDKs for mature nodes, with JKU Linz as a partner [PRIMARY] https://projekte.ffg.at/projekt/5145599/pdf ; https://projekte.ffg.at/projekt/dce4453e-f36b-1410-864f-00d3c07d99bb/pdf . YosysHQ's project is in 2.5.
- IHP open PDK SG13G2 (130nm SiGe BiCMOS) [PRIMARY project pages]:
  - Tiny Tapeout IHP 25b shuttle: submissions closed 1 Sep 2025, chips expected May 2026 https://tinytapeout.com/chips/ttihp25b/
  - IHP slides set out a concept for open-source multi-project wafer runs from 2026, with a minimum price of EUR 2,400-3,500 per open-source or Tiny Tapeout user https://www.mos-ak.org/munich_2025/presentations/W2_1_Melik_MOS-AK_Munich2025.pdf
  - A JKU Linz analog/mixed-signal tutorial (13 May 2026) bundles the open-source tools in the IIC-OSIC-TOOLS container https://iic-jku.github.io/ihp-sg13g2-ams-chip-template/index.html
- UK ARIA Safeguarded AI [PRIMARY] https://www.aria.org.uk/programme-safeguarded-ai :
  - budget GBP 59M;
  - Nov 2025: pivoted away from building specialised AI systems;
  - Feb 2026: cancelled the planned Phase 2 cyber-physical call and refocused on cybersecurity;
  - Apr 2026: Nora Ammann became programme director; davidad is technical adviser;
  - May 2026: thesis v2.0, moving away from TA2 and focusing on TA1 tooling and cybersecurity;
  - eight cybersecurity projects share GBP 22M;
  - the cybersecurity call offers GBP 2.5-3.5M per "Blue Team", cut-off 31 Oct 2026.
- France 2030: a EUR 550M call to select French participants in a future IPCEI on advanced semiconductor technologies (PIIEC AST). Its scope includes design tools, IP blocks and cybersecurity; applications through Bpifrance until 1 Sep 2026 [PRIMARY] https://www.entreprises.gouv.fr/espace-presse/souverainete-europeenne-la-france-investit-550-millions-deuros-dans-les-semi ; https://www.info.gouv.fr/actualite/france-2030-lancement-d-un-appel-a-projets-pour-selectionner-les-acteurs-francais-du-futur-piiec-sur-les-technologies-avancees-du-semiconducteur . No France 2030 call dedicated to EDA or verification was found.
- Israel Innovation Authority:
  - Joint Israel-Chips JU 2026 call: EUR 3.5M for Israeli participants, funding up to 66% for companies and 80% for academia, deadline 23 Sep 2026 [PRIMARY] https://innovationisrael.org.il/en/calls_for_proposal/chips-ju-2026/
  - NIS 150M integrated-photonics pilot line with MAFAT, June 2026 [PRIMARY] https://innovationisrael.org.il/en/press_release/integrated-photonics-rnd/
  - No IIA programme specific to verification was found.

### Inferences
- Funding helps open-source verification engines at the margin (YosysHQ). But because the platform procures commercial tools (Siemens), public money does not displace the incumbents' sign-off tools. Transition 4 is being pushed by AI models and open PDKs more than by subsidy.
- ARIA's retreat from building formal-proof AI systems removes one potential public anchor customer for UK proof start-ups.

### Gaps
- The winners of the open-source EDA call were not found, nor YosysHQ's role or share.

## 5. Israel specifically

### Takeaway
Israel's verification firms are a globally leading smart-contract prover (Certora), an AV-verification platform under funding pressure (Foretellix), two services firms (Veriest and its spin-off Vtool) and one newly funded simulator (Hiveware). No Israeli AI-native chip-verification start-up beyond Hiveware was confirmed. Hebrew-language press could not be confirmed as a source.

### Cited Findings
- Certora (assessed in 2.1): last round US$36M in 2022; usage pricing and AutoProver in 2026; diversifying into Web2 and mobile security research.
- Foretellix (assessed in 2.6): US$135M raised, last round in 2023; 18% layoff in Jan 2026; NVIDIA-centred partnerships through Oct 2026.
- Veriest and Vtool (section 1): Veriest has 100+ engineers and a new CEO from May 2026. Vtool has no confirmed acquisition.
- Hiveware (section 1): US$24M Series A, Jul 2026.
- VerifAIX has an Israeli team (section 1). Attestable, Arato and Irregular work on AI security and testing, not chips.
- Unconventional AI is buying the Israeli chip start-up NeuReality (Oct 2026), a chip maker rather than a verification firm [SECONDARY] https://algemeiner.com/2026/10/26/unconventional-ai-buys-israeli-chip-startup-neureality-speed-product-development
- Innovation Authority programmes are in section 4.

### Inferences
- The Israeli verification talent pool (Verisity heritage, ex-Hailo and ex-Cadence engineers at Hiveware) mainly feeds new tool start-ups and multinational R&D centres rather than independent tool vendors of scale. This is an inference; the R&D centres were not researched.

### Gaps
- Not researched in this pass: the Israeli R&D centres of Cadence (Verisity heritage), Synopsys, Siemens and NVIDIA. The Hebrew-language search returned no Hebrew-press results; Globes, Calcalist, TheMarker and Geektime coverage could not be confirmed.

## 6. Exposure: how an investor could get exposure (kept separate from quality)

### Takeaway
None of the six companies assessed in depth can be bought directly. The listed routes are either diversified groups in which verification is immaterial (Alten, UL Solutions, Bureau Veritas, SGS, Siemens for Defacto and Lauterbach) or a small listed venture investor (IP Group, for Mach42). This is analysis, not a recommendation.

### Cited Findings
**Private companies: latest funding, valuation and investors**
- Certora: last priced round US$36M Series B (May 2022), led by Jump Crypto with Tiger Global and Galaxy Digital; valuation not disclosed (sources in 2.1). No listed vehicle gives meaningful exposure; whether Galaxy Digital's holding is significant was not verified. A Galaxy portfolio page lists Certora [SECONDARY] https://venturecareers.galaxy.com/companies/certora
- AdaCore: Battery Ventures investment (Mar 2024; reportedly a majority stake); value undisclosed; no listed vehicle (2.2).
- AbsInt: privately held, no outside investors found (2.3).
- TrustInSoft: last disclosed round EUR 5M (Nov 2019), led by ACE Management (Brienne III), with Idinvest earlier. Whether a listed asset manager still holds Idinvest's stake was not verified (2.4).
- LUBIS EDA: EIC Accelerator EUR 2.5M (2023-2024); no listed vehicle. Axiomise: founder-owned after the 2024-2025 buyback; no outside equity. YosysHQ: public grant funding only (FFG EUR 153K).
- Foretellix: US$135M raised to Dec 2023 from 83North, Temasek, Isuzu, Woven Capital (Toyota), NVIDIA and others (2.6). Logos on its About page, inferred from image file names and unverified, also include Volvo, NVG, MoreTech Ventures, 57Stars, OurCrowd and others https://www.foretellix.com/about/ . Exposure through its large listed strategic investors is immaterial.
- Hiveware: RTP Global (private), Series A US$24M (Jul 2026).
- Mach42: IP Group led the round (Jul 2026), which is a real but small listed route (below).
- Veriest: subsidiary of Aman Group. TASE ticker AMAN belongs to Amanet Management & Systems Ltd ("multidisciplinary systems house in Israel", 1,065 employees, share price ILA 1,176 on 12 Nov 2026), whose profile does not mention Veriest. A link between Aman Group and Amanet is NOT confirmed [UNVERIFIED] https://stockanalysis.com/quote/tlv/AMAN/company
- Codasip: onsemi bought its low-end RISC-V business for a reported US$14.5M (Oct 2026). Defacto (acquired Jul 2026) and Lauterbach (agreement Nov 2026) go into Siemens (covered by the Siemens researcher).

**Listed companies.** Data from stockanalysis.com quote pages fetched 12 Nov 2026; delayed prices [SECONDARY data aggregator].
- Alten SA (EPA: ATE) https://stockanalysis.com/quote/epa/ATE/ : EUR 86.95 (12 Nov 2026, 13:10 CET); market cap EUR 2.94bn; revenue ttm EUR 4.12bn (+0.1%); net income ttm EUR 138.1M; P/E 21.8, forward P/E 10.4; dividend EUR 1.50. H1 2026 revenue was EUR 2.01bn with an operating margin of 8.9%, and FY2026 guidance was raised (25 Sep 2026); revenue fell 1.1% in 2025; Q3 2026 release on 27 Oct 2026, figures not shown. Registry: SIREN 348607417; French entity staff band 5,000-9,999 (2024) [PRIMARY] https://annuaire-entreprises.data.gouv.fr/entreprise/348607417
- UL Solutions (NYSE: ULS) https://stockanalysis.com/stocks/uls/ : US$81.58 (close 11 Nov 2026); market cap US$16.47bn; revenue ttm US$3.19bn; net income ttm US$514M; P/E 32.4. Q3 2026 revenue US$823M with 7% organic growth (3 Nov 2026).
- Bureau Veritas (EPA: BVI) https://stockanalysis.com/quote/epa/BVI/ : EUR 30.33 (12 Nov 2026); market cap EUR 13.39bn; revenue ttm EUR 6.75bn; P/E 26.9; Q3 2026 revenue up 10.1% to EUR 1.57bn.
- SGS (SWX: SGSN) https://stockanalysis.com/quote/swx/SGSN/ : CHF 102.90 (12 Nov 2026); market cap CHF 20.33bn; revenue ttm CHF 7.21bn; P/E 30.3; Q3 2026 sales up 14.6% to CHF 1.98bn.
- IP Group plc (LON: IPO), lead investor in Mach42 https://stockanalysis.com/quote/lon/IPO/ : 76.30p (12 Nov 2026); market cap GBP 674M. It rebuffed a 71.3p proposal from its top investor Railpen (20 Jul 2026); Railpen walked away (27 Jul 2026).
- EnSilica plc (AIM: ENSI): no valuation retrieved (gap). Sondrel: now "Aion Silicon"; listing status unknown.

### Inferences
- The investable quality names in these regions (AbsInt, AdaCore, Certora) are reachable only privately or through a future deal. The most likely public route is an acquisition by a listed EDA, testing or security vendor, as with Defacto and Lauterbach going into Siemens.
- In the listed TIC groups (UL Solutions, Bureau Veritas, SGS), software-safety certification is too small a share of revenue to count as verification exposure (inference; segment data not checked).

### Gaps
- No valuation for EnSilica; no AIM status for Sondrel/Aion Silicon; no private valuations for any company.

## 7. Conclusion: which belong among the 8 to 15 that matter most globally, and where coverage is thin

### Takeaway
- AdaCore and AbsInt belong in the global 8-15. They own judge-type proof tools that certification accepts, sold to regulated buyers whose budgets are not tied to AI spending: AdaCore through SPARK, NVIDIA's adoption, a Rust hedge and a growth-investor owner; AbsInt through CompCert's first DO-178C compiler credit and Astrée.
- Certora is the borderline candidate. It leads the one clearly paying non-regulated market for verified code (DeFi) and has an early AI specification agent, but it depends on labour and on the crypto cycle.
- Everyone else in these regions belongs on a watch list rather than in the core list. That includes TrustInSoft, the YosysHQ/LUBIS EDA/Axiomise group, Foretellix, Veriest/Vtool, Hiveware and the seL4 companies.
- All of this is my provisional judgment.

### Cited Findings
- Evidence for the above is in sections 2.1 to 2.6. TrustInSoft is sub-scale and loss-making (EUR 5.9M revenue, EUR -1.6M result in 2024).
- LUBIS EDA and Axiomise are profitable or growing labour businesses with no product that acts as a judge.
- Foretellix's last round was in 2023 and it cut 18% of staff in Jan 2026.
- Hiveware is pre-revenue as far as is known: pilots only, unnamed.
- The seL4 ecosystem has tier-one members (Apple, NIO, RTX) but small service companies (Proofcraft, Kry10).

### Inferences
- These regions add two "judge" companies to the global ranking, both small. Their importance is out of proportion to their size because they sit where certification requires proof.
- If the ranking needs a representative for "who pays for verified software outside regulation", Certora is the evidence-backed choice.

### Gaps
Coverage is thin in the following areas:
- company accounts for AbsInt (paywalled), LUBIS EDA, YosysHQ (Austrian registry), Veriest and Foretellix;
- Certora's revenue mix;
- Hebrew-language press;
- the Israeli R&D centres of Cadence, Synopsys, Siemens and NVIDIA;
- Aldec, AMIQ EDA, Sigasi, Verifyter, Vector Informatik and the TÜV, DEKRA and exida bodies;
- Canada.

## 8. Closing lists

### Takeaway
The three lists below record what remains unverified, where the evidence cuts against the background views, and the main dated sources.

### Cited Findings
**What I could not verify**
- Certora: revenue, revenue mix, runway, the Canton grant URL, the AI Composer launch URL.
- AdaCore: group revenue, debt and headcount; its pricing model; the merger completion date (only "2025" from AdaCore, and the distributor notice of Jan 2026).
- AbsInt: financial figures; the authority that granted the CompCert credit.
- TrustInSoft: customers; any funding after 2019; the NIST recognition.
- Ownership of LDRA (TASKING?), Rapita and QA Systems. Status of Sondrel/Aion Silicon, Vtool, Aldec, AMIQ EDA, Sigasi and Verifyter.
- Any link between Veriest and the TASE-listed Amanet. EnSilica's valuation.
- Who won the Chips JU open-source EDA call. The ISO 26262, EN 50716 and UNECE R155/R156 texts.
- Any 2026 ANSSI, BSI or NCSC guidance naming formal verification.
- First-pass items without URLs: Axiomise partnerships, sci2sci, Attestable, Arato, Safe Intelligence, Imandra's seed round, Kry10's round, Proofcraft/DARPA PROVERS, Codasip's EUR 119M, TrustInSoft/Ferrous Systems, Diffblue's registry page.

**Where current evidence contradicts the background views**
- "Tools that own a verdict keep their position": partly contradicted.
  - Certora gave its prover away (GPL v3, Feb 2025) and now earns from specifications, compute and audits.
  - Independent European tool owners did not stay independent: Defacto went to Siemens and Codasip was split.
  - Supporting evidence: the CompCert DO-178C credit (Mar 2026) and NVIDIA's open-sourced SPARK process.
- "Verification labour loses pricing power": contradicted for now.
  - In 2025 LUBIS EDA grew its team 80% with 73% repeat engagements, and Certora doubled its research team and ran about 150 audits.
  - From Nov 2024 to Apr 2026 Axiomise's cash and reserves rose.
  - Aave still pays US$2.39M a year for a retainer that includes manual audits.
  - Supporting evidence: &Truth's "under $500" claim, Foretellix's AI-linked layoffs and Certora's US$120-a-month AutoProver tier.
- "Value moves from writing proofs to writing specifications": broadly supported, with a twist.
  - Supporting: the Devcon panel, Certora's admission that AI specifications miss requirements, and the unified rail HLL 4.0 specification.
  - The twist: AutoProver auto-generated 104 rules, so writing specifications is itself being automated. The CRA guidance does not require formal specifications, so regulation is not yet pulling value toward them.

**Main sources with dates** (all others are inline)
- French registry API, data to FY2024, queried 12 Nov 2026: https://annuaire-entreprises.data.gouv.fr/entreprise/793371907
- Axiomise accounts to 30 Apr 2026, filed 21 Sep 2026: https://find-and-update.company-information.service.gov.uk/company/11016128/filing-history
- AbsInt CompCert release, 20 Mar 2026: https://www.absint.com/releases/260320.htm
- CompCert site, 2026: https://compcert.org/
- AdaCore press releases, Jun 2025 to 11 Nov 2026: https://www.adacore.com/press
- AdaCore CRO release, 10 Aug 2026: https://www.adacore.com/press/adacore-appoints-radhika-holowko-as-chief-revenue-officer-to-drive-next-stage-of-growth
- NVIDIA SPARK process, 2025: https://github.com/NVIDIA/spark-process
- Certora 2025 figures, 21 Jan 2026: https://cryptobriefing.com/certora-secures-nearly-200-billion-in-defi-value-in-2025-preventing-over-700-vulnerabilities-across-leading-protocols
- Certora pricing and AutoProver posts, Jul to 10 Nov 2026: https://www.certora.com/pricing ; https://www.certora.com/blog/ai-formal-verification-smart-contracts-costs-use-cases
- Certora Series B, May 2022: https://www.theblock.co/post/147066/certora-announces-36-million-series-b-funding-round-led-by-jump-crypto
- LUBIS EDA site and FormalOS, Oct to Nov 2026: https://lubis-eda.com/
- YosysHQ FFG project, Jun 2026: https://projekte.ffg.at/projekt/b9e4453e-f36b-1410-864f-00d3c07d99bb/pdf
- Foretellix news, to 21 Oct 2026: https://www.foretellix.com/news-and-events/
- CTech on Foretellix layoffs, 8 Jan 2026: https://www.calcalistech.com/tags/Foretellix
- Hiveware, 27 Jul 2026: https://hiveware.io/hiveware-emerges-from-stealth-with-24-million-in-rtp-global-led-series-a/
- SemiEngineering funding round-ups, Q1 to Q3 2026: https://semiengineering.com/startup-funding-q3-2026/
- Chips JU open-source EDA call record, 2025, fetched 12 Nov 2026: https://ec.europa.eu/info/funding-tenders/opportunities/data/topicDetails/horizon-ju-chips-2025-ia-eda-two-stage.json
- ARIA Safeguarded AI, to May 2026: https://www.aria.org.uk/programme-safeguarded-ai
- Orrick on the CRA, Sep 2026: https://www.orrick.com/en/Insights/2026/09/EU-Cyber-Resilience-Act-New-Guidance-Clarifies-Scope-Reporting
- Sidley on the PLD, Oct 2026: https://www.sidley.com/en/insights/newsupdates/2026/10/revised-eu-product-liability-directive
- seL4 Foundation members, page as of 12 Nov 2026: https://sel4.systems/Foundation/Membership/
- Quote pages, 12 Nov 2026: https://stockanalysis.com/quote/epa/ATE/ ; https://stockanalysis.com/stocks/uls/
- Innovation Authority Chips JU call, 2026: https://innovationisrael.org.il/en/calls_for_proposal/chips-ju-2026/
- France 2030 semiconductor call, 2026: https://www.entreprises.gouv.fr/espace-presse/souverainete-europeenne-la-france-investit-550-millions-deuros-dans-les-semi

### Inferences
- The gaps lie mainly in private-company financials, which no public source in these regions fills except the French and UK registries.

### Gaps
- Two further pages appeared in search results and were not fetched: a16z's "spec is law" article on formal verification in DeFi (Mar 2026, via a blog summary) https://blockeden.xyz/blog/2026/03/14/a16z-spec-is-law-formal-verification-defi-smart-contract-exploits/ , and an AutoProver-related secondary page https://tryethernal.com/blog/formal-verification-property-specification-gap
