# Siemens EDA (inside Siemens AG, XETRA: SIE) as a chip verification and sign-off company

Research date: 12 November 2026 (continuation pass that completes an earlier partial pass). Every figure carries its own period and publication date. Status: FINAL.

Tag key: [PRIMARY] filing or official document; [INDEPENDENT] confirmed by an outside party (customer, foundry, regulator, third-party study or share data); [COMPANY CLAIM] stated by Siemens only; [SECONDARY] press, analyst or data-aggregator report only; [UNVERIFIED] could not be verified. [calc] = my arithmetic on cited figures; "Inference" = my judgment.

Process note: the shared web-search budget ran out part-way through this pass (about 25 searches in). After that, findings come only from direct fetches of known URLs (mostly Siemens IR and newsroom, TSMC) and from other researchers' notes in this folder (marked "cross-ref"). I did not use other search services to get round the limit. The FY26 earnings-release PDF is encrypted for the fetch tool, so I extracted its text locally from the downloaded copy. Coverage is thin on: Mentor's downturn history, segment shares other than Calibre, Siemens EDA's China exposure, Microsoft and Arm tie-ups, and 2026 German-language press (one German search found nothing on an EDA separation).

**Summary.** Siemens EDA owns one clear "judge": Calibre physical verification. A data provider estimates its share at 85%+ (SemiAnalysis, May 2026). It is certified for the leading nodes of TSMC, Intel and Samsung, and Rapidus built its 2nm PDK on it (no Rapidus certification found). TSMC's public certification grids list only three vendors. Solido (foundry-certified circuit simulation) and Tessent (Samsung-certified test) are close to that sign-off role. In simulation, formal and emulation, Siemens is a smaller challenger whose engines can be swapped out. Siemens does not disclose EDA's revenue or margin. Outside estimates put it at about $2.2-2.5bn (CY2025), under 5% of Siemens AG's revenue. Siemens's own statements say EDA led software growth in FY26. The AI and pricing path is funded and has started, but so far it adds charges on top of named-user subscriptions (an "agentic surcharge"); it is not yet pricing by use. The CEO left for Synopsys in November 2025, and I found no named successor. At EUR 277 (close, 11 Nov 2026), Siemens AG trades at about 25x trailing earnings. That is above its own 5- and 10-year averages (about 18x and 16.5x), roughly in line with industrial-automation peers, and at a discount to the pure EDA vendors. EDA probably accounts for only about 4-16% of the market value.

---

## A. Quality tests (judged independently of share price; no valuation data in this part)

### a. Position: which products are the "judge"?

**Takeaway.** Calibre is a judge that others must pass, and foundries write and certify their rule decks for it. Solido (SPICE accuracy certified at TSMC and Intel) and Tessent (test, Samsung-certified at next-gen 2nm) sit close to sign-off. Questa One, Veloce/proFPGA, Avery VIP, Catapult and Polarion are productivity tools in contested markets. Excellicon adds timing-constraint (specification) checking, but timing sign-off itself is Synopsys PrimeTime's.

| Product | Role | Judge or gap-filler? | Key evidence |
|---|---|---|---|
| Calibre nmPlatform (nmDRC, nmLVS, PERC, xACT, YieldEnhancer, 3DStack, 3DThermal) | Physical verification sign-off; foundry rule decks | **Judge** | 85%+ share est.; certified TSMC A14/A16/N2/N3, Intel 14A/18A-P, Samsung next-gen 2nm; Rapidus PDK built on Calibre (below) |
| Solido (SPICE, Analog FastSPICE, variation-aware) | Custom/analog sign-off simulation | Near-judge | TSMC SPICE-accuracy certification N3A/N2P/A16/A14; Intel 14A/18A-P |
| Tessent | DFT / test | Near-judge (test quality) | Samsung certified for DFT on next-gen 2nm (May 2026) |
| Questa One (Sim, SFV/formal incl. OneSpin technology, Lint, Verification IQ) | Front-end functional verification | Contested tool | Simulation share est. implies Questa ≤ ~5-15% (calc from VCS/Xcelium ests.) |
| Veloce CS (Strato CS, Primo CS, proFPGA CS) | Emulation, prototyping (hardware) | Gap-filler; one-off hardware | Emulation est. Palladium 55-60%, ZeBu 35-40% ⇒ Veloce ≤ ~10% (calc) |
| Avery VIP | Verification IP | Gap-filler | No share data found |
| Catapult | High-level synthesis/verification | Tool | No data gathered |
| Excellicon (agreement May 2025) | Timing-constraint (SDC) development/verification | Spec checker, not timing judge | PrimeTime 90%+ of timing sign-off (est.) |
| Polarion | Requirements/ALM | Generic spec tool, not a chip judge | Product page names no standards or semiconductor use |

**Cited findings**
- TSMC EDA Alliance page (fetched 12 Nov 2026 by another researcher): certification grids "As of 10/01/2026" for A14, A16, N2P, N3C and 3DFabric have only three vendor columns, Cadence, Synopsys and Siemens EDA; TSMC: "full-line EDA Tool Certification Program with major partners including Cadence, Siemens EDA and Synopsys"; categories include physical verification, timing/power sign-off, EMIR, RC extraction, simulators, thermal; status legend "Certified" / "Work in Progress" / (3DFabric) "Certified for Technology Requirement"; test method, cost and timeline sit behind a TSMC-Online login. [PRIMARY, cross-ref] https://www.tsmc.com/english/dedicatedFoundry/oip/eda_alliance
- SemiAnalysis EDA Market Primer (21 May 2026, estimates, paywalled; visible part): Calibre physical verification 85%+ share and installed base; "TSMC requires 'Calibre-clean' DRC/LVS for tape-out", and Samsung and Intel do the same; Calibre is a "blocking position". [SECONDARY] https://newsletter.semianalysis.com/p/eda-market-primer
- Siemens: Calibre nmDRC "adopted as the internal sign-off design rule checking solution for all major foundries for over 25 years". [COMPANY CLAIM] https://eda.sw.siemens.com/en-US/ic/calibre-design/physical-verification/nmdrc ; commentary: foundries wrote rules for Calibre first from the late 1990s, and customers still benchmark alternatives at each node. [SECONDARY] https://semiengineering.com/calibre-evolves-constantly/
- TrendForce (2 Jun 2025) repeats, via 36Kr, that Calibre is 40% of [Siemens EDA] revenue, used by >90% of IC designers, 70%+ share. [UNVERIFIED, origin unclear] https://www.trendforce.com/news/2025/06/02/news-china-revenue-at-risk-as-u-s-curbs-slam-eda-giants-impact-on-synopsys-cadence-and-more/
- No independent figure was found for the share of leading-node tape-outs signed off with Calibre.
- **Foundry certification, by foundry:**
  - TSMC: Calibre nmPlatform certified for N3, N2, A16 and A14 (TSMC Technology Symposium, 22 Apr 2026 per earlier pass; coverage dated 23 Apr 2026). [COMPANY CLAIM, foundry grid confirms vendor status] https://news.siemens.com/fr-ca/siemens-eda-tsmc-technology-symposium-2026/ ; https://evertiq.com/design/2026-04-23-siemens-collaborates-with-tsmc-to-advance-ai-for-chip-design ; https://iconnect007.com/article/149730/siemens-collaborates-with-tsmc-to-advance-ai-for-semiconductor-design/149727/aep
  - TSMC NA OIP forum (23 Sep 2026; Futurum 24 Sep 2026): Calibre nmDRC, nmLVS, xACT, PERC certified for A14; Solido certified N3C/A16/A14; Aprisa and mPower A14 "underway"; CoWoS-L certification "underway"; COUPE flow "in progress"; Calibre 3DThermal certified A16; 3DStack multi-machine support for SoIC; AI DRC-fix agent (Calibre + Aprisa AI + Solido Fuse) co-enabled with TSMC; TSMC's Aveek Sarkar quoted. [SECONDARY] https://futurumgroup.com/insights/tsmcs-oip-forum-turns-agentic-chip-design-demos-into-production-flows/ ; https://www.crnasia.com/news/2026/components-and-peripherals/siemens-and-tsmc-add-ai-agent-to-automate-chip-design-rule-f
  - Siemens blog (23 Apr 2026): TSMC certification means outputs "match the behavior of real silicon at that node", validated against TSMC's models; Solido certified N3A, N2P, A16, A14 and in the A14 Custom Design Reference Flow. [COMPANY CLAIM] https://blogs.sw.siemens.com/cicv/2026/04/23/solido-and-ai-powered-eda-tsmc-certification-reference-flows-and-advanced-node-design/
  - Intel Foundry (27 Jul 2026, DAC): Calibre nmDRC, nmLVS, PERC, YieldEnhancer and Solido SPICE / Analog FastSPICE certified for Intel 14A and 18A-P (plain 18A not named); AFS in Intel's Custom Reference Flow; EMIB/EMIB-T packaging workflow; Intel's Shawn Han (SVP & GM Foundry Services) quoted in the release. No separate Intel announcement found. [COMPANY CLAIM with Intel quote] https://news.siemens.com/en-us/siemens-intel-dac-2026 ; https://www.cimdata.com/en/industry-summary-articles/item/30511-siemens-ic-design-solutions-now-certified-for-intel-14a-and-intel-18a-p-process-technologies
  - Samsung (SAFE US, 28 May 2026; Futurum 1 Jun 2026): Calibre certified for Samsung's "next-generation 2nm process" for photonic IC verification, physical verification and layout optimisation; Tessent certified for DFT on the same node; Aprisa "certified for leading-edge process nodes"; Innovator3D IC for the 2.3D Cube-E platform (>2m pins); Samsung's Hyung-Ock Kim: "Samsung Foundry continues to work closely with Siemens". Analyst: photonic verification is a capability "neither Synopsys nor Cadence has announced", but Siemens may lack certification equivalent to Synopsys's for third-generation 2nm. [SECONDARY] https://futurumgroup.com/insights/samsungs-2nm-advance-draws-on-eda-innovation-from-cadence-siemens-and-synopsys/
  - **Correction:** the earlier pass recorded that SAFE (28 May 2026) "fully qualified" the Calibre nmPlatform, but gave no URL. The Futurum account says "certified" and never uses "fully qualified". Treat that wording as [UNVERIFIED]. Similarly, another researcher's summary of the same article says Aprisa is "fully certified"; the direct fetch reads "certified for leading-edge process nodes".
  - Siemens EDA's Jean-Marie Brunet spoke at SAFE Forum Seoul (1 Jul 2026). [SECONDARY, cross-ref] https://en.edaily.co.kr/news/eda202607015207/
  - Rapidus (announced by Rapidus, 23 Jun 2025): 2nm GAA PDK built on Calibre, plus a front-to-back reference flow using Calibre and Solido. No 2026 announcement of a vendor flow "certified" for Rapidus 2nm was found (cross-ref). [INDEPENDENT: foundry-announced] https://www.newelectronics.co.uk/content/news/rapidus-collaborating-with-siemens-on-2nm-semiconductor-designs ; https://news.siemens.com/it-it/rapidus-siemens-eda ; https://evertiq.com/design/2025-06-24-rapidus-partners-with-siemens-to-advance-2nm-semiconductor-design
- Questa One launched 12 May 2025 (GA June 2025); Siemens claims "the fastest functional, fault and formal verification engines available"; Property Assist uses generative AI to write SVA properties; MediaTek says it saved weeks of engineering time (quote supplied by Siemens). Launch coverage does not mention OneSpin. [COMPANY CLAIM] https://assets.new.siemens.com/siemens/assets/api/uuid:e7b489a9-7b73-4711-9a42-4996fab65b75/HQDIPR202505127161EN.pdf ; https://www.newelectronics.co.uk/content/news/siemens-deploys-ai-in-new-questa-one-smart-verification-solution
- Veloce CS launched 20 Feb 2024: Strato CS runs on Siemens's own Crystal accelerator chip; Primo CS and proFPGA CS run on AMD Versal VP1902; 40m to 40bn+ gates; Siemens claims up to 5x Veloce Strato. [COMPANY CLAIM, cross-ref] https://www.allaboutcircuits.com/news/siemens-unveils-3-piece-emulation-and-prototyping-solution/
- Excellicon (Laguna Hills, CA, founded 2009): agreement announced 19 May 2025, terms undisclosed, close expected "in a few weeks"; tools to develop, verify and manage timing constraints; complements Questa, Tessent, Aprisa, PowerPro. Completion not confirmed. [COMPANY CLAIM/SECONDARY] https://dallasinnovates.com/siemens-acquires-california-based-excellicon-for-its-timing-constraints-software/ ; https://itbrief.co.uk/story/siemens-to-acquire-excellicon-to-expand-eda-software-portfolio
- Polarion REQUIREMENTS product page: requirements authoring/approval, LiveDocs, ReqIF, e-signatures, Jira/Simulink/Azure DevOps connectors; names no safety standards, no SaaS model, no AI features, no semiconductor use; "10,000 members, 150 extensions" community. [COMPANY CLAIM] https://www.siemens.com/en-us/products/polarion/requirements/

**Inferences**
- Calibre's moat does not rest on certification being exclusive: TSMC also certifies Cadence and Synopsys for physical verification. It rests on the foundries using Calibre internally, on the rule decks themselves (a manufacturability specification in Calibre's format), and on what customers expect at tape-out. AI-generated designs raise the volume of DRC/LVS runs rather than removing the check.
- Siemens does not own timing sign-off (PrimeTime 90%+ est.), the market-leading simulator or the market-leading emulator, so most of its verification portfolio sits in the "contested tool" tier of the framework.

**Gaps:** Tessent, Avery, Catapult and formal shares; Calibre's tape-out share; the OneSpin and Avery acquisition details (not re-verified this pass); whether Excellicon closed.

### b. Lead: outside evidence of a technical and commercial lead

**Takeaway.** Outside evidence backs a clear lead only in physical verification. Total EDA share is a stable ~13% (third of three), and outside estimates in simulation and emulation leave Siemens a distant third. The independent customer evidence is a handful of named users (Nvidia, MediaTek, Tsavorite) and quotes from TSMC, Intel and Samsung.

**Cited findings**
- Total EDA share (TrendForce): 2024 Synopsys 31%, Cadence 30%, Siemens 13% (2 Jun 2025 article) https://www.trendforce.com/news/2025/06/02/news-china-revenue-at-risk-as-u-s-curbs-slam-eda-giants-impact-on-synopsys-cadence-and-more/ ; but 2024 Synopsys 32%, Cadence 29%, Siemens 13% in a 30 Dec 2025 article https://www.trendforce.com/news/2025/12/30/news-five-year-old-chinese-eda-firm-univista-sets-sights-on-ipo-led-by-ex-synopsys-and-cadence-team/ ; 2025 forecast Cadence 32%, Synopsys 30%, Siemens 13% (Nov 2025 item) https://www.trendforce.com/news/?p=48281 . [SECONDARY] (This sources and corrects the earlier pass's unsourced line "TrendForce 2024: 31/30/13". Siemens's 13% is the same in every version; the Synopsys/Cadence order is not.)
- MarketResearch.com summary: Siemens 10-15%. SemiAnalysis: Big-3 >85% combined; Siemens EDA ~$2.2-2.5bn CY2025 vs Synopsys ~$8bn (incl. Ansys) and Cadence $5.30bn. [SECONDARY estimates, cross-ref synopsys.md] https://marketresearch.com/Prof-Research-v4036/Electronic-Design-Automation-EDA-Global-39562423 ; https://newsletter.semianalysis.com/p/eda-market-primer
- Segment estimates (SemiAnalysis, 21 May 2026): Palladium 55-60%, ZeBu 35-40% of emulation (market $1.5bn+); VCS 45-50%, Xcelium 40-45% of simulation; PrimeTime 90%+; Design Compiler 84-85%; Calibre 85%+. Siemens's tool-level chart is not readable. [SECONDARY] same URL
- Named customers and partners:
  - Nvidia (9 Apr 2026): used Veloce proFPGA CS to capture "tens of trillions of cycles over a span of just a few days"; Nvidia VP Hardware Engineering Narendra Konda quoted. Only proFPGA CS is named. [COMPANY CLAIM with customer quote] https://news.siemens.com/en-us/siemens-nvidia-veloce/
  - MediaTek and Tsavorite (agentic formal, lint auto-fix) in the Questa One Agentic Toolkit release, 27 Feb 2026. [COMPANY CLAIM with customer quotes] https://news.siemens.com/fr-fr/questa-one-agentic-ai-toolkit/
  - Intel (Shawn Han), TSMC (Aveek Sarkar) and Samsung (Hyung-Ock Kim) quoted in or alongside Siemens releases (see a.).
- Independent analyst view (Futurum, 24 Sep 2026): all three vendors reached A14 at the same time, so "tool availability is no longer a differentiator"; Siemens's foundry-co-developed DRC-fix agent is "the clearest example" of foundry-endorsed agentic trust (a "materially higher trust bar"). [SECONDARY] https://futurumgroup.com/insights/tsmcs-oip-forum-turns-agentic-chip-design-demos-into-production-flows/
- Tom's Hardware (2026): the agentic pitches of Cadence, Synopsys and Siemens "all answer to older tools". [SECONDARY, cross-ref] https://www.tomshardware.com/tech-industry/semiconductors/the-state-of-agentic-ai-in-chip-design-tools-in-2026-cadence-synopsys-and-siemens-all-pitch-autonomous-engineers
- Public programmes route incumbent licences: an EU Chips JU framework agreement (May 2026) gives design-platform users preset-price access to Siemens EDA https://www.digitalengineering247.com/article/siemens-opens-up-eda-software-access-for-european-electronics-industry/news ; Veloce is available to Indian DLI/C2S firms at C-DAC (PIB, Jan 2026) https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/jan/doc2026118760301.pdf . [SECONDARY/PRIMARY, cross-ref]
- Company claims, not independently confirmed: "fastest" verification engines (Questa One); Calibre Vision AI halves DRC debug time (as repeated by SemiAnalysis). [COMPANY CLAIM]

**Inferences:** On outside evidence, Siemens leads in physical verification (and probably DFT; unverified) and is a niche challenger elsewhere. Foundry quotes and certifications show Siemens is a required ecosystem partner, but they are not head-to-head performance evidence.

**Gaps:** no independent benchmark results; no share data for formal, VIP, prototyping (proFPGA) or DFT.

### c. Revenue model, and what Siemens actually discloses about EDA

**Takeaway.** Siemens does not disclose EDA revenue, growth or margin. It discloses Digital Industries (DI) software revenue, ARR and qualitative statements about EDA. Software is mostly subscription or term licences priced by named user. EDA revenue is lumpy because large multi-year contracts are recognised around renewal. Veloce/proFPGA (and, once closed, Lauterbach) add one-off hardware. Pricing by use is only announced, as surcharges and possible "credit-based" models.

**Cited findings (disclosure) [PRIMARY]**
- DI software revenue by quarter (EUR m), FY26: Q1 1,663; Q2 1,614; Q3 1,790; Q4 2,144; total 7,211. FY25: 1,369; 1,364; 1,540; 1,900; total 6,173. Earnings releases: https://assets.new.siemens.com/siemens/assets/api/uuid:11b1a70b-f540-45bb-824f-0b3fbb927e1b/dHQCOPR202611097494EN.pdf (12 Nov 2026) and the quarterly releases below.
- FY26 presentation (12 Nov 2026): DI software revenue EUR 7.2bn (+13% comp.), ARR EUR 6.1bn (+12% comp.); DI backlog EUR 11.0bn, of which software EUR 7.3bn; "Electronics & Semiconductors" = 15% of DI revenue exposure; Q4 software +12% "driven by EDA and Simulation". https://assets.new.siemens.com/siemens/assets/api/uuid:9ae98ef3-c21e-4485-906c-6d4264960796/4-and-Full-Year-FY-2026-Presentation.pdf
- Q4 FY26 release: "Revenue growth in the software business was led by the EDA business"; software orders "included higher volume year-over-year from large contracts in the PLM and EDA businesses".
- Q3 FY26 (6 Aug 2026): "Revenue growth was strongest in the software business, due mainly to substantial growth in the electronic design automation business". https://assets.new.siemens.com/siemens/assets/api/uuid:bdf8b45d-34dc-4911-ad72-5aa2a03d1d40/HQCOPR202608037433EN.pdf
- Q2 FY26 (13 May 2026): software "won a higher volume year-over-year from larger contracts in the product-lifecycle-management and electronic-design-automation software businesses". https://assets.new.siemens.com/siemens/assets/api/uuid:d4072f41-f21d-4287-af75-0cb72c194262/HQCOPR202605117394EN.pdf
- Q3 FY25 (7 Aug 2025): software revenue EUR 1,540m vs 2,067m (-30% comp.) because Q3 FY24 included large licensed-software contracts. This shows how lumpy recognition can be. https://assets.new.siemens.com/siemens/assets/api/uuid:d1a425b2-b59d-401b-aebf-9c622e812f4d/HQCOPR202508017210EN.pdf
- Speech (12 Nov 2026): "Fiscal 2027 is a strong renewal year for our EDA business, with the sales funnel again concentrated in Q4"; the SaaS transition "has now been completed"; ~5% of DI software revenue attributable to AI; agreement signed to acquire Lauterbach. https://assets.new.siemens.com/siemens/assets/api/uuid:b0adfeab-2c49-4993-9319-7b7169cff52d/Presserede-Q4-2026-Presseformat-EN.pdf
- Analyst call (12 Nov 2026; investing.com transcript) [SECONDARY transcript]: Busch: DI software revenue now exceeds EUR 7bn, and the software market is growing ~10%. Q4 software orders a record EUR 2.9bn, "driven by several large PLM and EDA orders", with early renewals and "significant upselling" (semiconductors, electronics, aerospace & defence). AI revenue ~5% of DI software, "roughly EUR 350 million" (Busch). The named-user subscription model continues into FY27. Human-led AI (Copilot) is sold as add-on subscriptions. CFO Bienert: "we plan and we will introduce an agentic surcharge on really this underlying software subscription"; "other credit-based, user-based monetization will follow" (no specifics). The Eigen Engineering Agent is "license fee-based because it is an engineering tool", which "must not remain forever". No EDA growth rate, China share or export-control effect was given. https://in.investing.com/news/stock-market-news/earnings-call-transcript-siemens-posts-record-orders-in-q4-2026-as-growth-quickens-93CH-5698664
- Third-party estimates of EDA scale: ~$2.2-2.5bn CY2025; "EDA is under 5% of Siemens' revenue"; Q1 FY26 DI software +11%, "EDA and simulation growing at double-digit rates", PLM ex simulation +7%. [SECONDARY] https://newsletter.semianalysis.com/p/eda-market-primer

**Inferences**
- ARR is about 85% of DI software revenue [calc: 6.1/7.2]. The rest is mostly upfront licence recognition and services; the services share is not disclosed. EDA's reported revenue will swing with the renewal calendar: a "strong renewal year" concentrated in Q4 FY27 points to a strong second half of FY27. That reflects timing as well as demand.
- EDA is about a quarter to a third of DI software revenue and about 2-3% of group revenue [calc: $2.2-2.5bn at an assumed EUR/USD of 1.10-1.20 = EUR 1.8-2.3bn; the exchange rate is my assumption, not sourced].
- Revenue that depends on human seats is high: pricing is named-user, and agents so far add a surcharge on top of the seat. Hardware (Veloce Strato/Primo/proFPGA; Lauterbach probes once closed) is one-off.

**Gaps:** the EDA mix of term licences vs SaaS vs hardware vs services; EDA contract length; any EDA-specific token or credit scheme (none found).

### d. Financial strength (Siemens AG FY26, year to 30 Sep 2026, published 12 Nov 2026) [PRIMARY unless tagged]

**Takeaway.** The parent is strong: record free cash flow, low industrial leverage after Altair and Dotmatics, and DI margins back near 20%. EDA's own margin, return and concentration cannot be seen. Group China revenue is 8.9%. Siemens EDA's China share is undisclosed; its US peers report 12-16%.

**Cited findings** (earnings release unless noted; https://assets.new.siemens.com/siemens/assets/api/uuid:11b1a70b-f540-45bb-824f-0b3fbb927e1b/dHQCOPR202611097494EN.pdf)
- Group FY26:
  - Orders EUR 108,159m (+25% comp.); revenue EUR 83,372m (+8% comp.); book-to-bill 1.30; backlog EUR 143bn.
  - Industrial Business profit EUR 13,292m (16.3%); EBITDA (continuing operations) EUR 15,326m.
  - Net income EUR 9,474m (FY25 10,387m, which included EUR 2,059m from discontinued operations); attributable to shareholders EUR 8,488m (9,620m); non-controlling interests 986m.
  - Basic EPS 10.94 (continuing operations 10.84); diluted 10.82; EPS pre PPA 11.76.
  - FCF (all-in) EUR 12,096m; ROCE 14.1%; R&D EUR 6,909m (6,559m).
  - Dividend proposal EUR 5.50.
  - Q4: orders +58% to a record EUR 34.8bn (led by Mobility and Smart Infrastructure), revenue EUR 23.7bn, record FCF EUR 5.6bn.
- Balance sheet: Industrial net debt EUR 4,782m, 0.3x EBITDA (EUR 12,160m, 0.9x, a year earlier); equity EUR 76.4bn (attributable 69,240m); goodwill EUR 41.7bn; long-term debt EUR 39.4bn; short-term debt EUR 7.8bn; cash EUR 12.9bn; interest income 2,597m, interest expense 1,592m. A data aggregator shows total debt EUR 49.92bn, cash EUR 10.93bn and net debt EUR 38.99bn. That probably reflects an earlier date and includes Siemens Financial Services and lease debt. [SECONDARY] https://stockanalysis.com/quote/etr/SIE/statistics/
- Weighted basic shares: FY26 775,916k (FY25 785,093k); Q4 771,038k.
- DI FY26:
  - Orders 20,880 (+12% comp.); revenue 19,677 (+9% comp.); profit 3,753; margin 19.1% (FY25 14.9%).
  - FCF 3,982; net capital employed 23,320; PPA amortisation 451; EBITDA 4,075.
- DI Q4 FY26:
  - Orders 6,414 (+16% actual, +15% comp.); revenue 5,594 (+10% comp.); software 2,144 (+13% actual, +12% comp.).
  - Profit 1,170 (779); margin 20.9% (15.5%), 21.9% excluding severance (19.9%); severance EUR 53m (224m).
  - Altair/Dotmatics integration costs EUR 36m, which took 0.6pp off the margin; the call says these costs fade in FY27 and software will "strongly contribute" to FY27 margin improvement. The US contribution was "particularly strong".
- FY27 outlook (excludes all Healthineers effects):
  - DI comp. growth 8-12% (led by double-digit software, per the call), margin 20-22%.
  - Smart Infrastructure 11-13%, margin 19.5-20.5%; Mobility 6-8%, margin 8-10%.
  - Group comp. revenue growth 9-11%, book-to-bill above 1; EPS pre PPA EUR 10.20-10.80 (comparable FY26 excluding Healthineers EUR 9.27); "excludes burdens from legal and regulatory matters".
  - Call: FCF margin 14.5% in FY26, "no change" to the FCF ambition; capex to rise substantially in FY27, mainly for Smart Infrastructure capacity. [SECONDARY transcript]
- Acquisitions behind the goodwill:
  - Altair: announced 30 Oct 2024, $10.6bn, completed March 2025; 2024 revenue $665.8m. [SECONDARY] https://en.wikipedia.org/wiki/Altair_Engineering
  - Altair met its FY26 revenue targets; Dotmatics profitability is "even exceeding expectations" (call). [SECONDARY transcript]
  - Dotmatics price and date were not re-verified.
- Concentration by country:
  - China revenue FY26 EUR 7,426m (+4% actual, +5% comp.), 8.9% of the group [calc]; US EUR 23,865m (+13% comp.); Germany EUR 12,308m.
  - Q4 China revenue EUR 2,117m (+7% comp.), but Q4 China orders EUR 1,903m (-1% comp.).
  - Peers (FY2024): Synopsys China $989.5m (~16%), Cadence $550m (12%); Siemens EDA's China figure not given. [SECONDARY] https://www.trendforce.com/news/2025/06/02/news-china-revenue-at-risk-as-u-s-curbs-slam-eda-giants-impact-on-synopsys-cadence-and-more/
- Healthineers:
  - Nov 2025 plan: deconsolidate the ~67% stake, 30% by direct spin-off to Siemens shareholders, the remainder reduced to a financial asset over the medium term. https://www.cimdata.com/en/industry-summary-articles/item/28868-siemens-plans-to-deconsolidate-siemens-healthineers
  - 17 Apr 2026 update: vote at the ordinary AGM in Feb 2027. https://assets.new.siemens.com/siemens/assets/api/uuid:0b34deea-3a2a-48a1-b549-3242dc53016a/260417-press-release-en.pdf
  - 12 Nov 2026: CFO: "we plan to transfer 34.1 percent of our stake in Siemens Healthineers to our shareholders at a ratio of one Siemens Healthineers share for every two Siemens shares". This is a change from the earlier 30% plan. Healthineers becomes discontinued operations from Q1 FY27.
  - Call: spin-off report and AGM invitation 10 Dec 2026; approvals Feb 2027; effective late spring 2027; terminating intra-group loans adds cash.
  - Healthineers FY26 revenue EUR 23,630m, adjusted EBIT margin 15.0%.
- Returns [calc]: DI profit / DI net capital employed = 16.1% (pre-tax, goodwill-heavy); group ROE ≈ 12.3% (8,488/69,240).
- Customer concentration for EDA: not disclosed.

**Inferences:** Financial strength is high, but it belongs to the conglomerate. Siemens EDA cannot be scored on margin or ROIC from disclosed data. SemiAnalysis's lower R&D-intensity estimate for Siemens EDA (25-28%, vs Synopsys 34% and Cadence 30%) suggests healthy unit margins, or under-investment. [SECONDARY estimate]

**Gaps:** EDA margin, ROIC, customer concentration, China share; Dotmatics terms.

### e. Resilience (AI-spending scenarios, cycle position, export controls, conglomerate effect)

**Takeaway.** Calibre, Solido and Tessent are tied to tape-out volume and node transitions, which makes them among the more durable verification assets. Veloce/proFPGA hardware and new AI-start-up demand are the cyclical parts. Siemens EDA got the same US letter as its US peers in May 2025. The 2026 position (the BIS affiliates-rule suspension, extended to 10 Jan 2027) is a truce, not a resolution.

**Cited findings**
- Industry cycle (ESD Alliance, cross-ref): global EDA/ESD revenue grew year on year in every quarter from Q1 2024 to Q2 2026 (e.g. Q2 2026 $5,710.8m, +12.2%; APAC +22.4%; released 19 Oct 2026). [INDEPENDENT industry data] https://www.prnewswire.com/news-releases/electronic-system-design-industry-posts-5-7-billion-in-revenue-in-q2-2026--esd-alliance-reports-302912151.html
- AI demand (cross-ref): TrendForce 3 Aug 2026 put nine CSPs' capex up ~90% to >$886.7bn in 2026 and ~$1.3tn in 2027. [SECONDARY] https://www.trendforce.com/presscenter/news/20260803-13161.html
- Export controls:
  - BIS letter to Siemens dated 23 May 2025. Siemens was told in early July 2025 that the restrictions were lifted, restored access to ECCN 3D991/3E991 software and technology, and resumed sales and support in China. [SECONDARY] https://www.thestar.com.my/business/business-news/2025/07/04/key-chip-firms-say-us-export-ban-lifted ; https://www.scmp.com/tech/policy/article/3316742/tech-war-us-lifts-export-control-chip-design-software-china
  - BIS Affiliates (50%) Rule: suspended for a year from 10 Nov 2025. On 5 Nov 2026 BIS extended the suspension (due to end 9 Nov 2026) to 10 Jan 2027, after the US and China agreed in September 2026 to extend the "Busan Agreement" to the same date. [SECONDARY, law-firm briefings] https://www.thompsonhinesmartrade.com/2026/11/bis-extends-affiliates-rule-until-january-2027/ ; https://www.cliffordchance.com/briefings/2026/11/bis-suspends-affiliates-rule-until-january-10-2027.html ; https://www.cassidylevy.com/?p=3267
- Past downturns: Mentor was the largest EDA vendor in the late 1980s ($380m revenue in 1989) and lost money in 1991 after a failed software rewrite (15% job cuts) [SECONDARY] https://newsletter.semianalysis.com/p/eda-market-primer . Cadence's LBO approach (Jun-Aug 2008) was withdrawn; Icahn offered ~$1.86bn (Feb 2011); Siemens bought Mentor for $4.5bn ($37.25/share, 21% premium; agreed Nov 2016, closed Mar 2017); Mentor FY2017 revenue was $1.28bn, net income $155m, 5,968 employees; renamed Siemens EDA in Jan 2021. [SECONDARY] https://en.wikipedia.org/wiki/Mentor_Graphics . No revenue series for 2001-03 or 2008-09 was found.
- Conglomerate effect:
  - For investment capacity: group FCF EUR 12.1bn; >EUR 1bn over three years for AI (13 Nov 2025 event) [SECONDARY] https://www.cash.ch/news/top-news/siemens-nimmt-sich-fur-die-nachsten-jahre-hoheres-wachstum-vor-dividende-soll-mittelfristig-steigen-880793 ; seven EDA-related deals announced May 2025 to Nov 2026 (section B).
  - Against focus: EDA <5% of revenue, no standalone disclosure, parent capital competes with other businesses [SECONDARY, SemiAnalysis]; the CEO left for a direct rival (B).
  - The ability to bundle with Teamcenter/Opcenter and sell to automotive OEMs is cited as a strength. [SECONDARY, SemiAnalysis]

**Scenario reasoning (Inference)**
- Steady growth (~55%): more and larger AI tape-outs, chiplets and 3D-IC raise Calibre/3DStack/3DThermal and Solido runs, and FY27's renewal wave books multi-year terms (whether renewal terms are ~3 years is [UNVERIFIED]). Siemens gains least where it is weakest (simulation, emulation).
- Financing-led pause around 2028 (~25%): contracts renewed in FY27 cushion software revenue. Hardware (Veloce/proFPGA, Lauterbach probes) and AI-start-up licences would weaken first. Because revenue is recognised upfront, reported EDA revenue could fall y/y in a non-renewal year, as in Q3 FY25 (-30% software comp.), even if usage holds.
- Faster acceleration (~20%): the judge layer scales with tape-outs. Siemens's small share of emulation means it captures less of the hardware-verification boom than Cadence and Synopsys, both of which report record hardware (cross-ref).
- Cycle position: about ten consecutive quarters of industry growth points to a mid-to-late upcycle.
- Export-control exposure: the May 2025 episode shows Siemens EDA is treated like the US vendors, since its technology is US-developed. The suspension expires 10 Jan 2027 (a dated risk).

**Gaps:** Mentor's revenue through 2001-03 and 2008-09; Siemens EDA's China share and its customers on the Entity List.

---

## 2026 Siemens EDA / Wilson Research Group functional verification study (vendor-sponsored)

**Takeaway.** The background claim is broadly confirmed: only 5% of IC/ASIC participants reported first-silicon success in 2026, versus **14.4%** (not 14%) in 2024. But the study is sponsored by Siemens, which sells the remedy, and the panel's recruitment changed from 2024, so trends need care.

**Cited findings**
- Publication: 8 Sep 2026 (Verification Academy, author Harry Foster; blog the same day). Sample: 604 qualified participants (320 IC/ASIC, 284 FPGA). The split is in the blog and earlier notes; the Verification Academy page gives only the 604 total. Method: a reference paper "explains the recruitment-methodology transition between the historical 2007-2022 studies and the current 2024-2026 study period" (sample-provider recruitment from 2024, per cross-ref). Survey dates are not stated on the pages read. [PRIMARY, vendor-sponsored] https://verificationacademy.com/topics/planning-measurement-and-analysis/2026-siemens-eda-and-wilson-research-group-functional-verification-study/ ; https://blogs.sw.siemens.com/verificationhorizons/2026/09/08/the-2026-functional-verification-study/
- IC/ASIC: "Only 5% of IC/ASIC participants report achieving first-silicon success, down from 14.4% in 2024." Logic/functional errors "continue to be a major contributor to ASIC respins"; other named contributors are firmware, safety, security, power, clocking and timing. No percentages were accessible.
- FPGA: "98% of responding FPGA participants report one or more non-trivial bugs escaping into production" ("rising"), which implies ~2% with no escapes [calc].
- Both: 97% of IC/ASIC and 98% of FPGA projects have at least one embedded processor. Verification takes 49% (IC/ASIC) and 51% (FPGA) of project time. About three in four projects miss their original schedule (Foster, 28 Oct 2026). https://blogs.sw.siemens.com/verificationhorizons/2026/10/28/are-we-looking-beyond-the-numbers-in-the-2026-functional-verification-study/
- AI: 82.8% report use beyond evaluation or pilot, but only 9.0% describe AI as broadly integrated across the verification flow. The leading uses are debug/root-cause analysis, testbench/test generation and coverage. [PRIMARY] https://verificationacademy.com/resource/255f4023-866c-4205-be0c-2773b848e987 (adoption percentages behind a login)

**Inferences:** Verification's share of effort and the poor first-pass results support demand for verification tools and the "judge" layer. The jump from 14.4% to 5% (2024 to 2026) uses the same post-2024 method, so it is less affected by the 2024 break than comparisons with 2022.

**Gaps:** formal-adoption, emulation-adoption, respin-cause percentages and engineer headcounts sit in the "2026 Data Atlas" (not accessed).

---

## B. Path forward through the transitions

**Takeaway.** Siemens is not resisting AI agents or open source. It is wiring its engines into them (MCP toolkit for Claude Code, Copilot, Cursor and Cline) and buying OpenROAD's main commercial steward. It is also spending on foundry co-development, where it is strongest. Pricing is the laggard: named-user seats plus a planned surcharge.

| Transition | Must it get through? | Said | Done (dated) | Assessment |
|---|---|---|---|---|
| (1) Labour to tools | Beneficiary (sells tools, not labour) | Questa One targets the "verification productivity gap" | Questa One GA Jun 2025; Agentic Toolkit early access 27 Feb 2026 (RTL Code, Lint, Verification Planning, Debug agents; MediaTek, Tsavorite) | Tailwind; gains limited by small front-end share |
| (2) Seats to use | Yes | Named-user subscriptions continue FY27; "agentic surcharge"; credit-based "will follow" | SaaS transition "completed" (DI software); AI ≈ EUR 350m (~5% of DI software); no EDA token scheme found | Partly coherent: additive, not yet usage-based |
| (3) Simulation to formal | Yes (Questa) | "fastest formal engines"; GenAI SVA (Property Assist) | Questa One SFV; Tsavorite agentic formal property verification; OneSpin (2021, per brief; not re-verified) | Plausible, no outside share evidence |
| (4) Proprietary vs open source + AI | Yes, most exposed in front-end | Works with "GitHub Copilot, Claude Code, Cursor, Cline" via MCP; Nvidia Nemotron/NIM | Toolkit shipped (early access); Precision Innovations agreement 20 Jul 2026 (bulk of OpenROAD engineering and support since 2019) | Coherent "own the interface" hedge |
| (5) Foundry certification as barrier | Core strength | | TSMC grid (only 3 vendors, 1 Oct 2026); Calibre A14 (23 Sep 2026); Intel 14A/18A-P (27 Jul 2026); Samsung next-gen 2nm (28 May 2026); Rapidus PDK on Calibre (Jun 2025). Open: CoWoS-L, COUPE | Coherent; protects against entrants, not against Cadence/Synopsys |
| (6) Paying market for verified software | Adjacent, optional | System/automotive verification (PAVE360) | Lauterbach (agreement, week of 9 Nov 2026; debug/trace for embedded software, into hardware-assisted verification); Polarion; Altair (Mar 2025) | Partly coherent: tooling for regulated OEM buyers; no machine-checked-proof product found |
| (7) Model makers offering verification | Threat | Agents run on Siemens engines | Nvidia partnership (NIM/Nemotron; Fuse token efficiency, Sep 2026); toolkit open to third-party agents | Coherent if foundries keep certifying tools rather than agents |

**Cited findings**
- Agentic Toolkit (27 Feb 2026): MCP-based, works with GitHub Copilot, Claude Code, Cursor, Cline and Siemens Fuse; Llama Nemotron/NIM; early access, with broader rollout "as customers validate governance controls" [COMPANY CLAIM] https://news.siemens.com/fr-fr/questa-one-agentic-ai-toolkit/ ; https://itbrief.news/story/siemens-unveils-agentic-ai-toolkit-for-chip-verification . Human-oversight points are emphasised [SECONDARY, cross-ref] https://itbrief.co.uk/story/siemens-unveils-agentic-ai-toolkit-for-chip-verification . Siemens EDA's supplemental licence terms define an "Authorized Agent" as a human on customer premises; third-party hosting needs consent; no clause found that bars AI agents (cross-ref ai_native notes, URL not recorded there) [UNVERIFIED URL].
- Analyst framing (SemiAnalysis, 21 May 2026): Siemens is "catching up" on AI where Synopsys and Cadence led; PAVE360 (system-level automotive verification) targets a $0.8-1.2bn adjacent opportunity by 2030 [SECONDARY] https://newsletter.semianalysis.com/p/eda-market-primer
- EDA AI System, DAC 16 Jun 2025: early access across the portfolio; Aprisa AI, Calibre Vision AI, Solido; Nvidia NIM/Nemotron. [COMPANY CLAIM] https://assets.new.siemens.com/siemens/assets/api/uuid:4b47e806-a963-4d58-952d-02b5dee39a21/HQDIPR202506167185EN.pdf . Fuse EDA AI Agent (Mar 2026; orchestrates IC/3D-IC/PCB flows; Aprisa integration); DAC 2026 preview of a "self-verifying" long-running agent with no release date. [SECONDARY] https://www.all-about-industries.com/siemens-lets-eda-agents-check-their-own-work-a-92d15a25eed2ab9e5ccd2ab168c2b7a7/
- Acquisitions:
  - Excellicon (agreement 19 May 2025).
  - Canopus AI (Grenoble, AI wafer/mask metrology; completed 12 Jan 2026, announced early Feb; terms undisclosed; feeds Calibre computational lithography; followed a Dec 2025 Siemens-GlobalFoundries AI-manufacturing partnership). https://news.siemens.com/nl-nl/siemens-acquires-canopus-ai/ ; https://www.verdict.co.uk/siemens-acquisition-canopus-ai/ ; https://evertiq.com/summary/2026-02-06-siemens-ubernimmt-canopus-ai-zur-starkung-des-eda-portfolios
  - ASTER (Jan 2026; recorded by the earlier pass, details not re-verified) [UNVERIFIED].
  - Precision Innovations (San Diego; agreement 20 Jul 2026; terms undisclosed; close expected Q3; joins "Digital Design Creation"; Channel Insider, 22 Jul 2026, calls it completed, a conflict left unresolved). https://schnitgercorp.com/2026/07/20/siemens-to-acquire-precision-innovations-for-ai-powered-chip-planning/ ; https://www.designnews.com/electronics/siemens-acquires-precision-innovations-to-add-ai-chip-planning-to-eda ; https://evertiq.com/news/2026-08-07-siemens-to-acquire-eda-software-firm-precision-innovations ; https://www.channelinsider.com/channel-business/mergers-and-acquisitions/siemens-precision-innovations-defacto/
  - Defacto Technologies (Grenoble, founded 2003; RTL SoC integration/assembly, SoC Compiler; agreement 21 Jul 2026; terms undisclosed). https://www.eetasia.com/siemens-to-acquire-defacto-technologies/ ; https://blogs.sw.siemens.com/digital-design-creation-platform/2026/07/21/siemens-acquires-defacto-technologies-transforming-soc-design-with-powerful-re-use-and-assembly-automation-technology/
  - Lauterbach (agreement signed week of 9 Nov 2026; not closed; terms not given; no press coverage found on 12 Nov; earlier joint TRACE32 + Tessent Embedded Analytics webinars). https://webinars.sw.siemens.com/fi-FI/risc-v-system-debug-and-analysis-made-easy-with-lauterbach-trace32/
  - Altair ($10.6bn, Mar 2025) and Dotmatics: simulation and life-science software, not verification.
- Management: Mike Ellow (CEO, Siemens EDA) became Synopsys's Chief Revenue Officer on 20 Nov 2025. [PRIMARY] https://news.synopsys.com/2025-11-19-Synopsys-Appoints-Mike-Ellow-as-Chief-Revenue-Officer . No named successor was found. The 2026 public faces are Ankur Gupta (EVP, EDA IC Portfolio; quoted 27 Jul 2026 and on Precision Innovations), Juan C. Rey (CTO) and Jean-Marie Brunet (hardware-assisted verification). https://events.sw.siemens.com/en-US/u2uconference/north-america/speakers/
- Separation: no reporting found of an EDA spin-off, listing or sale (searched in German). The separations under way are Healthineers and Siemens Energy units. https://stock3.com/news/siemens-zahlen-und-healthineers-abspaltung-16789671 . The CFO says Siemens will focus externally on group targets, gave no DI-specific mid-term target, is "selective" in M&A (software plus hardware plus data) and does not rule out large deals. [SECONDARY transcript]
- Funding: group FCF EUR 12.1bn; Industrial net debt 0.3x; group mid-term revenue-growth target raised to 7-11% (from 6-9%), EPS growth "double digit"; R&D to grow moderately in FY27 (call). The 13 Nov 2025 ONE Tech event (combined CMD, annual press conference and FY25 call) set a DI mid-term margin range of 17-23% and FY26 DI guidance of 5-10% growth and 15-19% margin (FY26 came in at +9% and 19.1%). It reported DI software ARR of EUR 5.3bn at that point (13% average annual growth), set an aim to double the digital business by 2030, and expected digital markets to grow ~11% a year over FY25-30 (addressed markets ~6%). [SECONDARY summaries] https://www.siemens.com/en-us/company/about/strategy/siemens-one-tech-strategy-results-2025 ; https://www.cash.ch/news/top-news/siemens-nimmt-sich-fur-die-nachsten-jahre-hoheres-wachstum-vor-dividende-soll-mittelfristig-steigen-880793
- Integration (call, 12 Nov 2026): Altair integration "fully on track", with first revenue synergies. After the spin, the remaining Healthineers stake is equity-accounted and to be reduced over the medium term. [SECONDARY transcript]

**What must go right (Inference)**
1. Calibre keeps foundry primacy at A14 and beyond and in packaging sign-off; CoWoS-L and COUPE certifications are still open.
2. Questa One and the agentic toolkit win measurable share from VCS and Xcelium once agents choose tools. There is no evidence of such wins yet.
3. The surcharge and then credit pricing captures agent use without cutting into named-user revenue.
4. EDA leadership stabilises after the CEO's move to Synopsys.
5. US-China controls stay suspended after 10 Jan 2027.
6. Six or more tuck-ins (Excellicon, Canopus, ASTER, Precision Innovations, Defacto, Lauterbach) integrate well.

**Provisional verdict (my provisional judgment): PARTLY COHERENT.** It is coherent and funded at the judge layer: Calibre, Solido and Tessent foundry certification, the foundry co-developed AI agent, open-interface AI integration, and the OpenROAD hedge. It is only partly coherent in front-end verification and pricing, where announcements outrun proof: early-access agents, a surcharge rather than usage pricing, and no outside share evidence. It is unproven in emulation share. A leadership gap at the EDA unit adds execution risk.

---

## C. Entry point: Siemens AG as the vehicle (valuation and share price; kept separate from quality)

**Takeaway.** Siemens AG is a diluted and indirect way to own Siemens EDA. EDA is roughly 2-3% of revenue and plausibly 4-16% of market value. The stock trades well above its own multiple history but roughly in line with industrial-automation peers. The Healthineers spin-off (vote Feb 2027, effective late spring 2027) makes the "stub" cleaner but no more exposed to EDA.

**Cited findings**
- Price:
  - Latest close: Xetra, 11 Nov 2026, EUR 277.00 (earlier pass). This is consistent with the aggregator's EUR 282.30 (+5.30, +1.91%) at 13:30 CET on 12 Nov, and with MarketScreener's market cap of EUR 212,735m (= 767,995k shares x 277.00). [SECONDARY] https://stockanalysis.com/quote/etr/SIE/statistics/ ; https://www.marketscreener.com/quote/stock/SIEMENS-AG-56358595/valuation/
  - Intraday 12 Nov (results day): Tradegate EUR 282.00 at 13:41 CET (MarketScreener); ~EUR 286 (+3.3%) per the earlier pass (time and source not recorded) [UNVERIFIED].
- Size: market cap EUR 212.7bn at 277.00, EUR 216.8bn at 282.30; EV EUR 250.1bn (MarketScreener) / EUR 262.7bn (stockanalysis, which includes financial-services debt). 52-week change +14.25%; beta 1.34; consensus "Buy", average target EUR 305.18 (25 analysts). [SECONDARY]
- Own history (MarketScreener, FY Sept; 2026-28 consensus estimates) [SECONDARY]:

| FY | 2021 | 2022 | 2023 | 2024 | 2025 | 2026E | 2027E | 2028E |
|---|---|---|---|---|---|---|---|---|
| P/E | 18.7x | 22x | 13.7x | 17.5x | 18.9x | 25.5x | 22.5x | 19.7x |
| EV/EBITDA | 16.8x | 11.2x | 10.2x | 13.3x | 16.4x | 16.5x | 14.6x | 12.9x |
| EV/Sales | 2.45x | 1.67x | 1.85x | 2.37x | 2.78x | 3.01x | 2.73x | 2.51x |
| EV/EBIT | 23.5x | 12.9x | 14.9x | 18.8x | 22.8x | 20.9x | 18.2x | 15.8x |
| Div. yield | 2.82% | 4.2% | 3.46% | 2.87% | 2.33% | 2.02% | 2.12% | 2.31% |
| P/B | 2.56x | 1.68x | 2.24x | 2.79x | 2.87x | 3.25x | 3.04x | 2.77x |
| FCF yield | 5.49% | 7.02% | 6.96% | 5.32% | 4.93% | 3.95% | 4.3% | 5.03% |
| Mkt cap EURm | 113,299 | 79,905 | 107,367 | 141,274 | 177,700 | 212,735 | | |
| EV EURm | 152,454 | 120,076 | 143,879 | 180,037 | 219,220 | 250,124 | 247,659 | 244,273 |
| Shares (k) | 798,333 | 789,577 | 791,442 | 779,054 | 775,303 | 767,995 | | |

  - Sector average P/E 32.68x (weighted 29.49x).
  - Wisesheets (snapshot date unclear): 10-year average P/E 16.52, 5-year 18.14, 3-year 17.92 https://wisesheets.io/pe-ratio/SIE.DE ; YCharts SIEGY P/E 27.29 (29 Jun 2026) https://ycharts.com/companies/SIEGY/pe_ratio ; Macrotrends 20.99 (23 Jun 2025) https://m.macrotrends.net/stocks/charts/SIEGY/siemens-ag/pe-ratio . [SECONDARY]
- My multiples at EUR 277 [calc]:
  - Trailing P/E 25.3x on basic EPS 10.94; 23.6x on EPS pre PPA 11.76.
  - FCF yield 5.7% (12,096/212,735, includes Healthineers); dividend yield 2.0% (5.50/277).
  - The 2021-25 average P/E is 18.2x and average EV/EBITDA 13.6x.
  - The aggregator's trailing P/E of 27.95 and EV/EBITDA of 18.61 probably predate the Q4 results (implied EPS ~10.1).
- Peers (stockanalysis; prices 12 Nov 2026 ~13:30 CET or 11 Nov close) [SECONDARY]:
  - Schneider Electric: P/E 29.22, fwd 20.14, EV/EBITDA 17.87, EV/Sales 3.79, ROIC 13.96% https://stockanalysis.com/quote/epa/SU/statistics/
  - ABB: P/E 30.86, fwd 19.86, EV/EBITDA 20.21, EV/Sales 4.22, ROIC 25.42% https://stockanalysis.com/quote/swx/ABBN/statistics/
  - Siemens (same source): fwd P/E 21.96, ROIC 6.58%, P/FCF 17.95.
  - Dassault Systèmes: P/E 25.59, fwd 17.81, EV/EBITDA 16.85, EV/Sales 5.16; PTC: P/E 21.96, EV/Sales 8.36, EV/EBITDA 21.9 (deal price $205; Busch cited Schneider's purchase of PTC at a "EUR 22 billion" price, not independently checked).
  - Synopsys: fwd P/E 26.26, EV/Sales 10.17, EV/EBITDA 46.15 (GAAP); Cadence: fwd P/E 34.94, EV/Sales 14.94, EV/EBITDA 41.26 (cross-ref). https://stockanalysis.com/stocks/snps/statistics/ ; https://stockanalysis.com/stocks/cdns/statistics/ ; https://stockanalysis.com/quote/epa/DSY/ ; https://stockanalysis.com/stocks/ptc/
- Ex-Healthineers stub [calc]:
  - Healthineers price EUR 43.85, market cap EUR 48.81bn, 1.11bn shares (12 Nov 2026, 13:24 CET) [SECONDARY] https://stockanalysis.com/quote/etr/SHL/statistics/
  - Siemens's ~67% stake ≈ EUR 32.7bn ≈ EUR 42.6 per Siemens share. The spin delivers 0.5 Healthineers shares (≈ EUR 21.9) per Siemens share.
  - Stub ≈ EUR 234 at 277. That is 25.3x FY26 comparable EPS pre PPA excluding Healthineers (EUR 9.27), and 21.7-23.0x the FY27 guidance of EUR 10.20-10.80 (excludes all Healthineers effects). [PRIMARY inputs from the earnings release]
  - Other listed stakes (e.g. any remaining Siemens Energy holding) were not adjusted for [UNVERIFIED size].
- How much of the price rests on EDA [calc/Inference]:
  - DI is 23.6% of FY26 revenue and 28.2% of Industrial Business profit; DI software is 8.6% of revenue.
  - EDA is roughly 2-3% of revenue (SemiAnalysis: "under 5%").
  - At 5x sales (Dassault-like), EDA ≈ EUR 9-12bn, 4-6% of market cap. At 8-15x (PTC to Cadence), EUR 15-34bn, 7-16%.
- Seat licences and services: the named-user subscription model continues into FY27; ARR is ~85% of software revenue [calc]; a services split is not disclosed. Most of the software business therefore still rests on per-user subscriptions, with term-licence renewals (EDA) recognised in lumps.
- Near-term events:
  - 10 Dec 2026: spin-off report and AGM invitation.
  - Q1 FY27 (Oct-Dec 2026): Healthineers moves to discontinued operations (results date not verified).
  - 10 Jan 2027: affiliates-rule suspension and Busan Agreement extension expire.
  - Feb 2027: AGM (spin-off vote; EUR 5.50 dividend).
  - Late spring 2027: spin-off effective. The buyback (EUR 1.7bn bought "since the program began in July") is to continue "with rapid speed" after the spin.
  - Lauterbach closing.
  - Q4 FY27 (Jul-Sep 2027): EDA renewal funnel.
  - No new capital-markets day was announced in the sources read (the last was the 13 Nov 2025 ONE Tech event).
- Access for foreign investors:
  - Direct: XETRA/Frankfurt (also Tradegate).
  - US: sponsored Level I ADR, SIEGY (CUSIP 826197501), OTC only since the NYSE delisting in May 2014; 2 ADRs = 1 share (ratio changed 13 Mar 2017); depositary Deutsche Bank. [PRIMARY] https://www.siemens.com/global/en/company/investor-relations/share-bonds-rating/adr.html ; https://www.otcmarkets.com/stock/SIEGY/profile
  - A US OTC ordinary-share line, SMAWF, appears in data providers. [SECONDARY] https://www.wisesheets.io/pe-ratio/SMAWF

**Conditions under which entry would look more attractive (Inference, not advice)**
- At the 2021-25 average P/E of ~18x, the stub on FY27 guidance would be ~EUR 190, ~EUR 233 including the Healthineers stake at today's price. That is ~16% below the 11 Nov close.
- Siemens starts disclosing EDA separately.
- Evidence of usage-priced EDA revenue.
- Clean execution of the spin-off and the buyback.
- A drawdown driven by the AI-capex pause scenario, while renewals booked in FY27 protect EDA.
- Lower export-control risk after January 2027.
- For a pure EDA exposure, Siemens AG is not that vehicle: about 85-95% of its value rests on automation, infrastructure, mobility and other software.

**Gaps:** Siemens's 10-year EV/EBITDA series; consensus EPS by source; the value of Siemens's other listed stakes.

---

## Closing lists

### 1. What I could not verify
- Siemens EDA revenue, growth, margin, China share and customer concentration (not disclosed; only estimates).
- Calibre's share of leading-node tape-outs; Tessent, Avery, Catapult, formal and Veloce shares (only implied ceilings).
- The name of a CEO successor at Siemens EDA.
- Whether Excellicon, Precision Innovations and Defacto have closed; Lauterbach terms; ASTER details; Dotmatics price and date.
- Mentor's revenue in the 2001-03 and 2008-09 downturns.
- The Wilson Data Atlas figures (formal adoption, respin causes, engineer counts).
- 2026 Microsoft and Arm partnership items (the search budget ran out).
- The earlier pass's "fully qualified" (Samsung) wording and its ~EUR 286 intraday price.
- The "Calibre = 40% of revenue / >90% of designers" claims.
- The Siemens EDA licence "Authorized Agent" clause URL.

### 2. Where current evidence contradicts (or qualifies) the background views
- "Seat-priced tools face pressure once AI agents drive open-source alternatives": no sign of this yet at Siemens. Software orders hit a record (Q4 FY26), early renewals came with "significant upselling", and the named-user model continues. Siemens is making its proprietary engines the tools agents call (MCP) and buying OpenROAD's steward. Pricing pressure, if it comes, is not visible in 2026.
- "Value moves to the judge": supported for Calibre. But foundry certification is not exclusive (TSMC certifies all three vendors), and an independent analyst says A14 readiness "is no longer a differentiator" among them. The barrier protects against new entrants, not against Cadence or Synopsys.
- "Machine-proved regression checks standard for AI-edited designs by 2028 (60%)": the 2026 evidence argues for caution. AI is broadly integrated in only 9.0% of verification flows (Wilson), Siemens's agent toolkit is still early access with human-oversight points, and the Fuse "self-verifying" agent has no release date.
- "Final sign-off stays with people": consistent so far. TSMC certifies tools, not agents (Futurum remark), and Siemens's toolkit keeps humans in the loop.
- The Wilson figure: 14.4% (2024), not 14%. The 5% (2026) figure is confirmed but vendor-sponsored, with a 2024 method change.
- Facts in the brief needing update: the Healthineers transfer is now 34.1% (1-for-2 ratio), not the 30% planned in Nov 2025. Excellicon was announced as an acquisition in May 2025, but its completion is not confirmed. Intel's 2026 certification names 14A and 18A-P, not 18A. Defacto (France) is no longer independent.
- "The big three keep growing through 2029 (70%)": consistent to date (ESD Alliance growth every quarter through Q2 2026; Siemens says EDA led software growth in FY26).

### 3. Sources with dates (primary first)
- Siemens Q4 FY26 earnings release, 12 Nov 2026 https://assets.new.siemens.com/siemens/assets/api/uuid:11b1a70b-f540-45bb-824f-0b3fbb927e1b/dHQCOPR202611097494EN.pdf ; FY26 presentation, 12 Nov 2026 https://assets.new.siemens.com/siemens/assets/api/uuid:9ae98ef3-c21e-4485-906c-6d4264960796/4-and-Full-Year-FY-2026-Presentation.pdf ; press speech, 12 Nov 2026 https://assets.new.siemens.com/siemens/assets/api/uuid:b0adfeab-2c49-4993-9319-7b7169cff52d/Presserede-Q4-2026-Presseformat-EN.pdf ; Q3 FY26, 6 Aug 2026 https://assets.new.siemens.com/siemens/assets/api/uuid:bdf8b45d-34dc-4911-ad72-5aa2a03d1d40/HQCOPR202608037433EN.pdf ; Q2 FY26, 13 May 2026 https://assets.new.siemens.com/siemens/assets/api/uuid:d4072f41-f21d-4287-af75-0cb72c194262/HQCOPR202605117394EN.pdf ; Q3 FY25, 7 Aug 2025 https://assets.new.siemens.com/siemens/assets/api/uuid:d1a425b2-b59d-401b-aebf-9c622e812f4d/HQCOPR202508017210EN.pdf ; Healthineers update, 17 Apr 2026 https://assets.new.siemens.com/siemens/assets/api/uuid:0b34deea-3a2a-48a1-b549-3242dc53016a/260417-press-release-en.pdf ; ADR page (accessed 12 Nov 2026) https://www.siemens.com/global/en/company/investor-relations/share-bonds-rating/adr.html ; AGM 2026 key data, 12 Feb 2026 https://assets.new.siemens.com/siemens/assets/api/uuid:de1ea218-58e1-4b21-9f28-d73bc563a802/Keydata-Speech-RB-AGM2026.pdf
- TSMC EDA Alliance (grids as of 1 Oct 2026; fetched 12 Nov 2026) https://www.tsmc.com/english/dedicatedFoundry/oip/eda_alliance
- Siemens releases: Intel/DAC, 27 Jul 2026 https://news.siemens.com/en-us/siemens-intel-dac-2026 ; Nvidia/Veloce, 9 Apr 2026 https://news.siemens.com/en-us/siemens-nvidia-veloce/ ; Agentic Toolkit, 27 Feb 2026 https://news.siemens.com/fr-fr/questa-one-agentic-ai-toolkit/ ; Questa One, 12 May 2025 https://assets.new.siemens.com/siemens/assets/api/uuid:e7b489a9-7b73-4711-9a42-4996fab65b75/HQDIPR202505127161EN.pdf ; EDA AI System, 16 Jun 2025 https://assets.new.siemens.com/siemens/assets/api/uuid:4b47e806-a963-4d58-952d-02b5dee39a21/HQDIPR202506167185EN.pdf ; TSMC symposium, Apr 2026 https://news.siemens.com/fr-ca/siemens-eda-tsmc-technology-symposium-2026/ ; Canopus AI, Feb 2026 https://news.siemens.com/nl-nl/siemens-acquires-canopus-ai/ ; Rapidus, 23 Jun 2025 https://news.siemens.com/it-it/rapidus-siemens-eda ; Solido blog, 23 Apr 2026 https://blogs.sw.siemens.com/cicv/2026/04/23/solido-and-ai-powered-eda-tsmc-certification-reference-flows-and-advanced-node-design/ ; Defacto blog, 21 Jul 2026 https://blogs.sw.siemens.com/digital-design-creation-platform/2026/07/21/siemens-acquires-defacto-technologies-transforming-soc-design-with-powerful-re-use-and-assembly-automation-technology/ ; Polarion page (undated) https://www.siemens.com/en-us/products/polarion/requirements/ ; Calibre nmDRC page (undated) https://eda.sw.siemens.com/en-US/ic/calibre-design/physical-verification/nmdrc ; U2U 2026 speakers https://events.sw.siemens.com/en-US/u2uconference/north-america/speakers/ ; Lauterbach webinar (undated) https://webinars.sw.siemens.com/fi-FI/risc-v-system-debug-and-analysis-made-easy-with-lauterbach-trace32/
- Wilson 2026 study: Verification Academy, 8 Sep 2026 https://verificationacademy.com/topics/planning-measurement-and-analysis/2026-siemens-eda-and-wilson-research-group-functional-verification-study/ ; blog, 8 Sep 2026 https://blogs.sw.siemens.com/verificationhorizons/2026/09/08/the-2026-functional-verification-study/ ; Foster, 28 Oct 2026 https://blogs.sw.siemens.com/verificationhorizons/2026/10/28/are-we-looking-beyond-the-numbers-in-the-2026-functional-verification-study/ ; AI resource https://verificationacademy.com/resource/255f4023-866c-4205-be0c-2773b848e987
- Synopsys release (Ellow), 19 Nov 2025 https://news.synopsys.com/2025-11-19-Synopsys-Appoints-Mike-Ellow-as-Chief-Revenue-Officer ; ESD Alliance Q2 2026, 19 Oct 2026 https://www.prnewswire.com/news-releases/electronic-system-design-industry-posts-5-7-billion-in-revenue-in-q2-2026--esd-alliance-reports-302912151.html
- Analyst and press [SECONDARY]:
  - SemiAnalysis, 21 May 2026 https://newsletter.semianalysis.com/p/eda-market-primer
  - Futurum: OIP, 24 Sep 2026 https://futurumgroup.com/insights/tsmcs-oip-forum-turns-agentic-chip-design-demos-into-production-flows/ ; SAFE, 1 Jun 2026 https://futurumgroup.com/insights/samsungs-2nm-advance-draws-on-eda-innovation-from-cadence-siemens-and-synopsys/
  - TrendForce: 2 Jun 2025 https://www.trendforce.com/news/2025/06/02/news-china-revenue-at-risk-as-u-s-curbs-slam-eda-giants-impact-on-synopsys-cadence-and-more/ ; 30 Dec 2025 https://www.trendforce.com/news/2025/12/30/news-five-year-old-chinese-eda-firm-univista-sets-sights-on-ipo-led-by-ex-synopsys-and-cadence-team/ ; Nov 2025 https://www.trendforce.com/news/?p=48281 ; 3 Aug 2026 https://www.trendforce.com/presscenter/news/20260803-13161.html
  - Investing.com call transcript, 12 Nov 2026 https://in.investing.com/news/stock-market-news/earnings-call-transcript-siemens-posts-record-orders-in-q4-2026-as-growth-quickens-93CH-5698664
  - Law-firm briefings on the BIS rule: Thompson Hine (Nov 2026) https://www.thompsonhinesmartrade.com/2026/11/bis-extends-affiliates-rule-until-january-2027/ ; Clifford Chance (6 Nov 2026) https://www.cliffordchance.com/briefings/2026/11/bis-suspends-affiliates-rule-until-january-10-2027.html ; Cassidy Levy https://www.cassidylevy.com/?p=3267
  - Export-control press: The Star, 4 Jul 2025 https://www.thestar.com.my/business/business-news/2025/07/04/key-chip-firms-say-us-export-ban-lifted ; SCMP, Jul 2025 https://www.scmp.com/tech/policy/article/3316742/tech-war-us-lifts-export-control-chip-design-software-china
  - Market data (12 Nov 2026): MarketScreener https://www.marketscreener.com/quote/stock/SIEMENS-AG-56358595/valuation/ ; stockanalysis (SIE, SHL, SU, ABBN, SNPS, CDNS, DSY, PTC; URLs above)
  - Wikipedia (accessed 12 Nov 2026): https://en.wikipedia.org/wiki/Mentor_Graphics ; https://en.wikipedia.org/wiki/Altair_Engineering
  - Other press: New Electronics, Jun 2025 and May 2025 (URLs above); Schnitger, 20 Jul 2026; Design News, Jul 2026; Evertiq, 7 Aug 2026 and 6 Feb 2026; EE Times Asia, Jul 2026; Verdict, Feb 2026; Dallas Innovates and IT Brief, May 2025; iconnect007 and CRN Asia, Apr 2026; IT Brief, Feb 2026; All About Industries, 2026; Semiconductor Engineering (undated); Edaily, 1 Jul 2026; Digital Engineering 24/7, May 2026; stock3 (Healthineers); CIMdata (Healthineers, Nov 2025; Intel, Jul 2026); cash.ch, Nov 2025; Channel Insider, 22 Jul 2026; Tom's Hardware, 2026; All About Circuits, Feb 2024; OTC Markets SIEGY profile; Wisesheets, YCharts, Macrotrends (snapshot dates as stated above).
