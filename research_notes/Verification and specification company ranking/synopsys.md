# Synopsys, Inc. (NASDAQ: SNPS) as a chip verification and sign-off company

Research date: 12 November 2026 (position as of that date). STATUS: FINAL (continuation pass complete; the earlier interim evidence log is merged below with every sourced fact, tag and URL kept; corrections are flagged "CORRECTION").

Tag legend: [PRIMARY] filing or official document; [INDEPENDENT] confirmed by an outside party; [COMPANY CLAIM] stated by the company only; [SECONDARY] press or analyst report only; [UNVERIFIED] could not be verified.

Fiscal calendar: fiscal year ends about 31 October (FY2026 = Nov 2025 to Oct 2026). Ansys consolidated from 17 July 2025.

Process notes: (1) The earlier researcher's WebSearch budget ran out after about 20 searches; it then fetched known primary URLs directly (news.synopsys.com, sec.gov, stockanalysis.com). (2) In this continuation the shared WebSearch budget ran out again at about 12:50 on 12 Nov 2026 after ~12 searches, and Firecrawl credits were exhausted; after that only known URLs were fetched directly, and no searches were routed through other services. (3) WebFetch reads only ~92-100k characters of long SEC documents, and SEC refuses direct downloads without a contact user agent, so 10-Q Part II (legal proceedings, risk factors) was not read; XBRL note pages (R-files) were used instead. (4) Items marked "cross-ref" come from other researchers' notes in this folder, cited to their original URLs and not re-checked by me.

---

## A. Quality tests (judged independently of share price)

### a. Position: does Synopsys own a "judge"?

#### Takeaway
Yes, in timing sign-off. PrimeTime (estimated 90%+ share) and the foundry-certified extraction and power-integrity tools around it (StarRC; RedHawk-SC and Totem from Ansys) are "judges" whose verdicts designs must pass before tape-out. Synopsys does not own every judge: physical verification belongs to Siemens Calibre (estimated 85%+), emulation is led by Cadence Palladium, and I found no share evidence for its formal and equivalence tools. Simulation, debug, hardware and IP are strong businesses but are not judges.

#### Cited findings: product by product

| Product | What it decides | Judge status and evidence | Tag |
|---|---|---|---|
| PrimeTime (static timing sign-off) | whether the chip meets timing at foundry corners | SemiAnalysis estimate "Synopsys PrimeTime 90%+ share"; foundries "specify which tools their customers must use for tape-out" | [SECONDARY] — [SemiAnalysis EDA Market Primer, 21 May 2026](https://newsletter.semianalysis.com/p/eda-market-primer) |
| StarRC (parasitic extraction) | the RC values timing and power sign-off use | named in sign-off lists, no share figure; TSMC certifies an "RC extraction" category | [UNVERIFIED share] — same; [TSMC OIP page](https://www.tsmc.com/english/dedicatedFoundry/oip/eda_alliance) |
| IC Validator (physical verification: DRC/LVS) | whether layout obeys foundry rules | challenger: Siemens Calibre estimated 85%+; IC Validator A14 enablement "on-going" as of 22 Apr 2026 | [SECONDARY] / [COMPANY CLAIM] — [SemiAnalysis](https://newsletter.semianalysis.com/p/eda-market-primer); [Synopsys-TSMC, 22 Apr 2026](https://news.synopsys.com/2026-04-22-Synopsys-Partners-with-TSMC-to-Power-Next-Generation-AI-Systems-with-Silicon-Proven-IP-and-Certified-EDA-Flows) |
| RedHawk-SC, Totem, Totem-SC, PathFinder-SC (power integrity, EM/IR, ESD; from Ansys) | whether the power grid, EM and ESD limits hold | foundry-certified (see table below); no share figure found | [PRIMARY with foundry quotes] |
| Formality (equivalence checking) | whether the netlist is logically identical to the RTL; the natural gate for machine-edited designs | no share or adoption data found | [UNVERIFIED] |
| VC Formal (formal property checking) | proves properties hold | no share data found; not mentioned in the SemiAnalysis primer or on the Q3 FY2026 call | [UNVERIFIED] |
| VCS (simulation) | runs tests; evidence, not a verdict | estimated 45-50% share vs Cadence Xcelium 40-45% | [SECONDARY] — [SemiAnalysis](https://newsletter.semianalysis.com/p/eda-market-primer) |
| Verdi (debug) | helps engineers find bugs; saves labour | 25-40% debug-cycle claim (see B) is Synopsys's; no share data | [COMPANY CLAIM] |
| VC SpyGlass (lint/CDC) | RTL-level static checks | no share data found | [UNVERIFIED] |
| ZeBu, HAPS (emulation, prototyping hardware) | speeds pre-silicon verification; not a judge | ZeBu estimated 35-40% vs Palladium 55-60%; "remains well behind Cadence's Palladium in both market share and revenue scale"; hardware recognised at shipment | [SECONDARY] / [PRIMARY] |
| Verification IP | protocol checkers | not covered in this pass (another researcher covers VIP) | — |
| Design IP (interface, foundation) | silicon-proven building blocks, not a judge | IPnest via SemiWiki: Synopsys 18.5% of design IP in 2025 (#2 after Arm 49.4%); interface IP ~57% | [SECONDARY] |
| SCADE (Ansys; safety-critical software) | qualified code generator plus formal checker; output usable in certified software | KCG "DO-178C/DO-330 at TQL-1", "certified for IEC 61508 at SIL 3", "EN 50716 at SIL 3/4", "qualified for ISO 26262 software up to ASIL D"; Design Verifier "formally expresses and assesses safety requirements", powered by Prover Technology; customers shown: Subaru, Airbus, ZeroAvia, Vestas, Mecalac, Skydweller | [COMPANY CLAIM] — [SCADE Suite page, read 12 Nov 2026](https://ansys.synopsys.com/products/embedded-software/ansys-scade-suite) |

#### Cited findings: foundry certification at leading nodes (as of 12 Nov 2026)

| Foundry / node | What was announced | Date | Source / tag |
|---|---|---|---|
| TSMC N2 | "Certified Digital and Analog Design Flows" for 2nm (headline only; not re-read) | 25 Sep 2023 | [COMPANY CLAIM] [release](https://news.synopsys.com/2023-09-25-Synopsys-and-TSMC-Collaborate-to-Accelerate-2nm-Innovation-for-Advanced-SoC-Design-with-Certified-Digital-and-Analog-Design-Flows) |
| TSMC N2 | Totem-SC analog power-integrity sign-off; PathFinder-SC multi-die ESD sign-off | 22 Apr 2026 | [PRIMARY] [release](https://news.synopsys.com/2026-04-22-Synopsys-Partners-with-TSMC-to-Power-Next-Generation-AI-Systems-with-Silicon-Proven-IP-and-Certified-EDA-Flows) |
| TSMC A16 to A14 | RedHawk-SC and Totem expanded from A16 to A14; IC Validator enablement "on-going" | 22 Apr 2026 | same |
| TSMC A14 | "Certified EDA flows on TSMC A14", "A14 certification across digital, analog flows"; TSMC's Aveek Sarkar cites "certified EDA solutions and silicon-proven IP portfolio from Synopsys" | 23 Sep 2026 | [PRIMARY; TSMC quote = INDEPENDENT in part] [release](https://news.synopsys.com/2026-09-23-Synopsys-and-TSMC-Partner-to-Accelerate-AI-Systems-Innovation-with-Agentic-AI-and-Advanced-Design) |
| Intel 18A, 18A-P | "certified and production-ready EDA flows and IP portfolio" | 27 Jul 2026 | [PRIMARY; quote from Intel SVP Shawn Han] [release](https://news.synopsys.com/2026-07-27-Synopsys-and-Intel-Foundry-Fast-Track-Customer-Readiness-from-Silicon-to-Systems-on-Intel-14A) |
| Intel 14A | "certification of AI-powered EDA flows on Intel 14A" | 27 Jul 2026 | same |
| Samsung, third-generation 2nm-class | flows "production-ready" | 28 May 2026 | [PRIMARY; quote from Samsung VP Hyung-Ock Kim] [release](https://news.synopsys.com/2026-05-28-Synopsys-Advances-Power-and-Performance-for-AI-and-Multi-Die-Designs-on-Latest-Samsung-Foundry-Processes-at-SAFE-Forum-2026) |
| Samsung, second-generation 2nm and 4nm | Totem-SC newly certified | 28 May 2026 | same |
| Rapidus 2nm GAA | collaboration only: Synopsys "will develop advanced design flows leveraging its AI-driven EDA suite" and enable "a broad IP portfolio"; also uses Rapidus manufacturing data; no certification milestone or timeline found | 10 Dec 2024 (Tokyo); Rapidus CEO Atsuyoshi Koike quoted | [COMPANY CLAIM] [PR Newswire](https://prnewswire.com/news-releases/rapidus-collaborates-with-synopsys-to-shorten-semiconductor-design-cycles-302327894.html); [eeNews Europe](https://www.eenewseurope.com/en/rapidus-signs-2nm-deals-with-synopsys-cadence/) [SECONDARY] |

- What certification involves, per TSMC itself: a "full-line EDA Tool Certification Program" run with Cadence, Siemens EDA and Synopsys, covering A14, A16, N2P, N3C and 3DFabric. Categories: physical implementation, timing and power sign-off, EM/IR drop, physical verification, RC extraction, simulators and thermal. Statuses are "Certified" or "Work in Progress" ("Certified for Technology Requirement" for 3DFabric). EDA solutions are made "compliant to TSMC technology requirements", partners "gain access to TSMC's technical insights to validate their tools and methodologies", and TSMC's design methodology is implemented in "Reference Flows". The EDA Alliance has 11 members (Cadence, iROC, Jedat, Keysight, Lorentz, Primarius, Siemens EDA, Silvaco, SkillCAD, Synopsys, Zuken), but only the big three are named in the full-line programme. The page does not say how certification is tested (accuracy or correlation criteria). [PRIMARY - TSMC, read 12 Nov 2026] — [TSMC OIP EDA Alliance](https://www.tsmc.com/english/dedicatedFoundry/oip/eda_alliance)
- Ghazi, Q3 FY2026 call (26 Aug 2026): "The portfolio we have with the sign-off leadership is essential to building these autonomous workflows"; "As you start looking at autonomous workflow, the most important thing is accuracy and determinism." [PRIMARY transcript, third-party transcription] — [Webull/Motley Fool](https://www.webull.com/news/15497781661541376)
- OpenAI's GPT-Synopsys release (30 Sep 2026) calls Synopsys tools "the underlying, ground-truth engineering tools" and says OpenAI licenses them for development. [PRIMARY/COMPANY CLAIM] — [release](https://news.synopsys.com/2026-09-30-OpenAI-and-Synopsys-Announce-GPT-Synopsys-Frontier-Intelligence-to-Revolutionize-Chip-Design)
- The Kimi K3 open-source chip demo stopped short of sign-off. Its README says area and timing were "not validated through backend place & route" and are "not sign-off values". [PRIMARY; cross-ref] — [MoonshotAI/nano-kpu](https://github.com/MoonshotAI/nano-kpu)

#### Inferences
- Synopsys's strongest "judge" is timing sign-off. Foundry certification at every leading-node foundry protects it, and the flow is sequential: per SemiAnalysis, "The flow itself is the lock-in". Power-integrity sign-off (from Ansys) adds a second certified judge. On the position test it ranks near the top. It is not uniquely positioned: Cadence and Siemens hold the same certifications, and Siemens owns the physical-verification judge.
- The judges that matter most for AI-edited designs are equivalence checking (Formality) and formal proof (VC Formal). They are the least evidenced part of the portfolio in public sources.

#### Gaps
- No share data for StarRC, RedHawk-SC/Totem, Formality, VC Formal, SpyGlass, Verdi or VIP. No tool-by-node certification map, so I cannot say whether IC Validator is certified at A14. No description of certification test criteria. No Rapidus certification.

### b. Lead: outside evidence

#### Takeaway
Outside evidence shows a real lead in timing sign-off, synthesis and interface IP, and parity in simulation. Synopsys trails in emulation and physical verification. In 2026 its core EDA growth (about 8-9%) lagged both the industry (about 12%) and Cadence (about 20%), which is the main counter-signal to its lead.

#### Cited findings
- SemiAnalysis estimates (21 May 2026): PrimeTime 90%+; Design Compiler "84-85% share"; VCS 45-50% vs Xcelium 40-45%; ZeBu 35-40% vs Palladium 55-60%; Calibre 85%+. Cadence Innovus "gained 10-15pp against Synopsys ICC2" in 2015-2020, then share stabilised "as Synopsys launched Fusion Compiler". Emulation market $1.5bn+. Synopsys ~$8B CY2025 revenue including Ansys, Cadence $5.30B, Siemens EDA ~$2.2-2.5B; big three >85% combined. [SECONDARY, analyst estimates] — [SemiAnalysis](https://newsletter.semianalysis.com/p/eda-market-primer)
- Other total-EDA share estimates (Synopsys 25-30%, Cadence 20-25%, Siemens 10-15%) vary by definition. I found no authoritative 2025 split. [SECONDARY] — [MarketResearch.com summary](https://marketresearch.com/Prof-Research-v4036/Electronic-Design-Automation-EDA-Global-39562423)
- IPnest via SemiWiki: 2025 design IP market ~$9.45B (+12.7%); Arm 49.4%, Synopsys 18.5%, Cadence 6.4%; Synopsys ~23% in 2024. In 2024 licence revenue, Synopsys led with 32% vs Arm 30% (Arm holds 66.7% of royalties). Interface IP: Synopsys ~57% in 2025. [SECONDARY; IPnest report paywalled] — [SemiWiki design IP](https://semiwiki.com/ip/373010-the-9-5-billion-design-ip-market-shifting-boundaries-arms-monopoly-and-the-risc-v-response/); [SemiWiki interface IP](https://semiwiki.com/ip/370809-consolidation-and-competition-who-is-winning-the-4-5-billion-interface-ip-race/). Cross-check (my arithmetic): 18.5% of $9.45B ≈ $1.75B, which matches Synopsys's FY2025 Design IP revenue of $1,751.8M, so the share drop reflects Synopsys's own IP decline.
- Company claims quoted by SemiAnalysis: "100% of the 10nm and 7nm tape-outs completed thus far utilized Synopsys design tools" (2016); "100% market share at 12nm and below" (2019); "roughly two-thirds of designs exclusively using Synopsys flows" (2023). [COMPANY CLAIM]
- Industry growth: SEMI ESD Alliance industry revenue was $5,747.8M in Q1 2026 (+12.7%) and $5,710.8M in Q2 2026 (+12.2%, released 19 Oct 2026). [PRIMARY industry data; cross-ref] — [ESD Alliance Q2 2026](https://www.prnewswire.com/news-releases/electronic-system-design-industry-posts-5-7-billion-in-revenue-in-q2-2026--esd-alliance-reports-302912151.html)
- Synopsys EDA growth: "slightly over 8%" y/y in Q2 FY2026 and 8.5% in Q3 FY2026. Management expects "double-digit organic EDA revenue growth in Q4 and for the full year 2026". [PRIMARY transcript / SECONDARY] — [Q2 call](https://www.fool.com/earnings/call-transcripts/2026/05/27/synopsys-snps-q2-2026-earnings-transcript/); [Q3 call](https://www.webull.com/news/15497781661541376); [TIKR](https://www.tikr.com/blog/synopsys-q3-earnings-call-just-promised-double-digit-eda-growth-heres-the-math-behind-it). Cadence Q3 2026 (quarter to 30 Sep): core EDA +20%, IP +24%, SD&A +30%, hardware "another record quarter". [PRIMARY; cross-ref] — [Cadence Q3 call](https://www.webull.com/news/15818016766808064)
- Hardware: launched 11 Mar 2026 as software-defined hardware-assisted verification (HAV); HAPS-200 12-FPGA available, ZeBu-200 12-FPGA due in Q3 2026; ZeBu Server 5 up to 2x performance; uses the AMD VP1902. Customer quotes from AMD (Salil Raje; Alex Starr) and NVIDIA (Narendra Konda). Q3 FY2026: "another record quarter for hardware-assisted verification solutions", "12 new and 66 repeat HAV customer wins", "record hardware revenue". Q4 FY2025: "Our HAV business ended a record year with 12 competitive wins in the fourth quarter." [PRIMARY; customer quotes = INDEPENDENT in part; win counts = COMPANY CLAIM] — [HAV release](https://news.synopsys.com/2026-03-11-Synopsys-Introduces-Software-Defined-Hardware-Assisted-Verification-to-Enable-AI-Proliferation); [Q3 call](https://www.webull.com/news/15497781661541376); [Q4 FY2025 call](https://www.fool.com/earnings/call-transcripts/2025/12/10/synopsys-snps-q4-2025-earnings-call-transcript/)
- Named counterparties: Amazon (a $1B+ deal, confirmed by Amazon's quote); OpenAI; Microsoft and AMD (Microsoft Discovery workflows); NVIDIA; Infineon (Virtualizer Development Kit for AURIX RC1, 10 Nov 2026). [PRIMARY] — [newsroom](https://news.synopsys.com/)
- Demand context: the Wilson/Siemens 2026 study (604 participants, published 8 Sep 2026) found verification takes 49% of IC/ASIC project time, first-silicon success fell to 5% (from 14.4% in 2024; note a methodology break), and ~3 of 4 projects run late. [PRIMARY industry study sponsored by competitor Siemens; cross-ref] — [Siemens blog](https://blogs.sw.siemens.com/verificationhorizons/2026/09/08/the-2026-functional-verification-study/)

#### Inferences
- The lead is real where independent estimates exist: timing sign-off, synthesis and interface IP. Foundry quotes from TSMC, Intel and Samsung confirm certification status. The 2026 growth gap with Cadence (8.5% vs 20% in core EDA) may reflect China (Synopsys's China share fell to ~10% of revenue while Cadence's was 16% in its Q3 2026), the timing of time-based recognition, or real share loss. I cannot tell which, so treat it as an open warning.

#### Gaps
- No independent share data for formal, equivalence, power integrity, VIP or prototyping. No independent benchmark of Synopsys AI tools.

### c. Revenue model

#### Takeaway
Most revenue is recurring time-based licences of about two to three years plus maintenance; Synopsys reports 78% recurring for FY2025. Hardware and perpetual IP are upfront and lumpier. There is almost no labour-hour revenue. Pricing for AI agents is announced as "subscription plus consumption", with royalty and revenue-share elements in IP and the OpenAI deal, but no consumption revenue has been disclosed yet.

#### Cited findings
- FY2025 (year to 31 Oct 2025; supplement dated 10 Dec 2025): revenue $7,054.2M (FY2024 $6,127.4M; FY2023 $5,318.0M). Product groups: EDA $4,369.7M (62.0%), Design IP $1,751.8M (24.8%), Ansys $756.6M (10.7%, from 17 Jul 2025), Other $176.1M. Segments: Design Automation $5,302.4M, Design IP $1,751.8M. By type: time-based $3,489.6M (49.5%), upfront $2,010.6M (28.5%), maintenance and service $1,554.0M (22.0%); shares are my arithmetic. Recurring revenue 78% of total (company definition, evidently broader than time-based plus maintenance). [PRIMARY] — [FY2025 supplement](https://s201.q4cdn.com/778493406/files/doc_earnings/2025/q4/supplemental-info/Synopsys-Q4-FY2025-Financial-Supplement.pdf)
- 10-K FY2025: licence terms "typically approximates two to three years". Hardware ("primarily consist of prototyping and emulation systems") is "generally recognized as revenue at the time of shipment", so it sits in upfront. S&A (Ansys) products are part of Design Automation, which "includes the EDA, Ansys and Other revenue groups". [PRIMARY] — [10-K](https://www.sec.gov/Archives/edgar/data/883241/000088324125000028/snps-20251031.htm)
- Q1 FY2026 (quarter to 31 Jan 2026): time-based $951.5M (39.5%), upfront $741.5M (30.8%), maintenance and service $715.7M (29.7%) of $2,408.8M. Q3 FY2026 (quarter to 31 Jul 2026): time-based $1,002.8M (40.5%), upfront $665.2M (26.9%), maintenance and service $808.8M (32.7%) of $2,476.8M. Percentages are my arithmetic; maintenance rose with Ansys. [PRIMARY] — [Q1 release](https://news.synopsys.com/2026-02-25-Synopsys-Posts-Financial-Results-for-First-Quarter-Fiscal-Year-2026); [Q3 release](https://news.synopsys.com/2026-08-26-Synopsys-Posts-Financial-Results-for-Third-Quarter-Fiscal-Year-2026)
- Q3 FY2026 product-group mix (10-Q): EDA 51.8% (Q3 FY25 68.0%), Design IP 19.1% (24.6%), Ansys 28.7% (5.1%; implies ~$711M), Other 0.4% (2.3%). Nine-month mix: EDA 49.5%, IP 18.6%, Ansys 31.4%, Other 0.5%. [PRIMARY] — [10-Q](https://www.sec.gov/Archives/edgar/data/883241/000088324126000025/snps-20260731.htm)
- Pricing statements, in date order:
  - 10 Dec 2025, Ghazi on IP: "we need to change the business model from an NRE plus a use fee to NRE plus use fee plus royalty and upside". On agents: "rethink how do we sell our solution for the value and impact"; "there is a challenge in terms of the inflection point of monetization". [PRIMARY transcript] — [Q4 FY2025 call](https://www.fool.com/earnings/call-transcripts/2025/12/10/synopsys-snps-q4-2025-earnings-call-transcript/)
  - 27 May 2026: 20 customers evaluating agentic EDA across more than 25 agents; exploring "subscription plus consumption for the agents to utilize our products". [PRIMARY/SECONDARY transcript] — [Q2 call](https://www.fool.com/earnings/call-transcripts/2026/05/27/synopsys-snps-q2-2026-earnings-transcript/)
  - 26 Aug 2026: defining "subscription of our agents, subscription of our workflow as well as a consumption measure" ("as these agents and the new workflow is consuming more software"); "more than 30 active customer engagements"; Factory 2 IP "moves us up the value chain from licensing alone to licensing plus royalties". [PRIMARY transcript] — [Q3 call](https://www.webull.com/news/15497781661541376)
  - 30 Sep 2026 Investor Day: monetisation "through subscription and consumption-based models across tools, agents, and its platform". Three adoption routes: the Synopsys Autopilot platform, Synopsys agents inside customers' AI platforms, or frontier models optimised for engineering. [PRIMARY] — [Investor Day release](https://news.synopsys.com/2026-09-30-Synopsys-Details-Growth-Strategy-and-Long-term-Financial-Model-at-2026-Investor-Day) (text read via [finviz copy](https://finviz.com/news/397287/synopsys-details-growth-strategy-and-long-term-financial-model-at-2026-investor-day)). Futurum describes GPT-Synopsys as subscription plus consumption plus an outcome-based revenue share. [SECONDARY] — [Futurum](https://futurumgroup.com/insights/synopsys-investor-day-2026-turns-eda-into-a-royalty-and-ai-model-revenue-share-business/)
  - GPT-Synopsys (30 Sep 2026): bundles compute, model and licences; "revenue sharing arrangement"; runs on OpenAI-hosted infrastructure. [PRIMARY] — [release](https://news.synopsys.com/2026-09-30-OpenAI-and-Synopsys-Announce-GPT-Synopsys-Frontier-Intelligence-to-Revolutionize-Chip-Design)
  - Amazon (30 Sep 2026): Synopsys is "evolving to a license-plus-royalty business model". [PRIMARY] — [release](https://news.synopsys.com/2026-09-30-Synopsys-and-Amazon-Announce-Strategic,-Multi-year-IP-Agreement-for-Custom-Silicon-Collaboration-Also-Extends-to-Cloud-and-AI-Powered-Engineering)
- SemiAnalysis: "One license equals one engineer running one tool at a time"; "Tokens decouple licensing from individual seats"; "Seat-based pricing scales linearly with headcount". It reports "AI-enhanced tool renewals generate ~20% revenue uplift over baseline contract values" (a Synopsys 2024 Investor Day claim). On lock-in: "Leaving an ELA means disaggregating a bundle and re-negotiating 20+ individual tools." [SECONDARY / COMPANY CLAIM] — [SemiAnalysis](https://newsletter.semianalysis.com/p/eda-market-primer)

#### Inferences
- Labour-hour revenue is negligible. The exposure to the seat-to-usage transition sits in the ~40-50% of revenue that is time-based licences, many of which are sized by engineer seats or token pools. Hardware, which is one-off, is at record levels and is the most cyclical line.

#### Gaps
- Hardware revenue and services revenue are not disclosed separately, nor is the share of licences sized by seats versus tokens. No consumption revenue figure exists yet.

### d. Financial strength

#### Takeaway
On non-GAAP measures the business is highly profitable (operating margin ~42% in Q3 FY2026, guided ~44% for FY2027) and cash-generative (FCF ~$2.6B in FY2026, ~$3.1B guided for FY2027). GAAP margins and returns are low because of Ansys amortisation. Deleveraging is ahead of plan: the term loans are repaid, about $10B of notes remain and buybacks have restarted. Concentration risk is moderate: about 42% of revenue is from the US, 13% Korea and ~10% China.

#### Cited findings
- FY2025: GAAP operating margin 13.0%, non-GAAP 37.3%; GAAP operating income $914.9M; R&D $2,479.3M (35.1% of revenue, my arithmetic); GAAP effective tax rate 4.0%; OCF $1,519M, capex $169M (FCF ~$1,350M, 19% margin, my arithmetic); debt $13,485M; cash and short-term investments $2,961M; ~28,135 staff. Segment adjusted operating margins: Design Automation 41.7%, Design IP 23.9% (38.3% in FY2024). [PRIMARY] — [supplement](https://s201.q4cdn.com/778493406/files/doc_earnings/2025/q4/supplemental-info/Synopsys-Q4-FY2025-Financial-Supplement.pdf); [10-K](https://www.sec.gov/Archives/edgar/data/883241/000088324125000028/snps-20251031.htm)
- Long-term objectives as of 10 Dec 2025: double-digit revenue growth, Design IP mid-teens, non-GAAP operating margin mid-40s, unlevered FCF margin mid-30s, non-GAAP EPS growth high-teens. [PRIMARY] — supplement above
- Q1 FY2026 (released 25 Feb 2026): revenue $2,408.8M (Q1 FY25 $1,455.3M); GAAP EPS $0.34, non-GAAP $3.77; Design Automation $2,001.8M (47.3% margin); Design IP $407.0M (16.2% margin; -6.5% y/y); OCF $856.8M; debt repayment $3,451.3M; restructuring $118.3M; $2,000.0M private placement; buyback authorisation replenished to $2.0B. [PRIMARY] — [Q1 release](https://news.synopsys.com/2026-02-25-Synopsys-Posts-Financial-Results-for-First-Quarter-Fiscal-Year-2026)
- Q2 FY2026 (released 27 May 2026): revenue $2.276B; non-GAAP operating margin 39.5%; non-GAAP EPS $3.35, GAAP $0.09; backlog $11B; Design Automation $1.822B (43.3%); Design IP $454M (-6% y/y, +12% q/q, 24.4% margin); Ansys ~$652M; long-term debt $10,013.8M at 30 Apr 2026. [PRIMARY] — [8-K Ex. 99.1](https://www.sec.gov/Archives/edgar/data/0000883241/000119312526241911/d126227dex991.htm)
- Q3 FY2026 (released 26 Aug 2026): revenue $2,476.8M vs $1,739.7M (+42%); Design Automation $2,003.0M (80.9%; 45.2% adjusted margin); Design IP $473.8M (19.1%; 26.5% margin; ~+11% y/y); GAAP operating margin 14.4%, non-GAAP 41.6%; GAAP EPS $2.84, non-GAAP $3.91; cash and short-term investments $3,607.7M; debt $1,020.2M short-term plus $9,017.1M long-term; 9M OCF $2,298.6M; 9M debt repayment $3,463.7M. Backlog ~$10.9B (incl. $1.9B non-cancellable FSA), with ~49% of non-FSA backlog to be recognised within 12 months and "The majority of the remaining backlog is expected to be recognized in the following three years"; at FY2025 year-end it was $11.4B incl. $2.0B FSA with ~45% within 12 months, and $8.1B incl. $1.2B FSA at 31 Oct 2024. [PRIMARY] — [Q3 release](https://news.synopsys.com/2026-08-26-Synopsys-Posts-Financial-Results-for-Third-Quarter-Fiscal-Year-2026); [10-Q](https://www.sec.gov/Archives/edgar/data/883241/000088324126000025/snps-20260731.htm); [TIKR](https://www.tikr.com/blog/synopsys-q3-earnings-call-just-promised-double-digit-eda-growth-heres-the-math-behind-it) [SECONDARY]
- Guidance path for FY2026. Initial (10 Dec 2025): revenue $9.56-9.66B; Ansys ~$2.9B at the midpoint, "growing double digits"; excludes ~$110M from the divested optical and PowerArtist businesses; non-GAAP operating margin 40.5% at the midpoint; non-GAAP EPS $14.32-14.40. As of 26 Aug 2026: revenue $9,690-9,740M; non-GAAP EPS $15.04-15.10; GAAP EPS $3.84-4.08; OCF ~$2,800M; FCF ~$2,600M with capex cut to ~$225M; Ansys ~$2.98B. Q4 guidance: revenue $2,530-2,580M, non-GAAP EPS $4.10-4.16. [PRIMARY] — [Q4 FY2025 call](https://www.fool.com/earnings/call-transcripts/2025/12/10/synopsys-snps-q4-2025-earnings-call-transcript/); [Q3 release](https://news.synopsys.com/2026-08-26-Synopsys-Posts-Financial-Results-for-Third-Quarter-Fiscal-Year-2026)
- FY2027 guidance (Investor Day, 30 Sep 2026): revenue $11.10-11.20B; non-GAAP operating margin ~44.0% (GAAP ~20.7%); non-GAAP EPS $19.04-19.12 (GAAP $8.16-8.61); OCF ~$3,600M; capex ~$500M; FCF ~$3,100M; diluted shares 190-192M. Long-term FY2026E to FY2030E: revenue ~15% CAGR (Design Automation/EDA 13%+, S&A 10%+, Design IP 17%+); non-GAAP operating margin ~50% by FY2030; FCF and non-GAAP EPS mid-20% CAGR; up to 50% of FCF returned via buybacks, with ~$1B of buybacks "over the coming months". The Investor Day was held in New York. [PRIMARY] — [Investor Day release](https://news.synopsys.com/2026-09-30-Synopsys-Details-Growth-Strategy-and-Long-term-Financial-Model-at-2026-Investor-Day)
- Debt and deleveraging:
  - Original structure (10-K FY2025): term loan $4.3B, in tranches of $1.45B due 17 Jul 2027 and $2.85B due 17 Jul 2028; senior notes $10.0B issued March 2025 ($1.0B due 2027, $1.0B due 2028, $8.0B in 2030 and later; listed average rates 4.84%, 4.85%, 5.31%, 5.22%); $850M revolver undrawn. The buyback was "suspended ... until we reduce our expected debt levels", with ~$194.3M left at 31 Oct 2025. [PRIMARY] — [10-K](https://www.sec.gov/Archives/edgar/data/883241/000088324125000028/snps-20251031.htm)
  - Plan (10 Dec 2025): term loans cut by ~$850M in Q4 FY2025 and ~$900M in November 2025, with a "plan to prepay the balance of $2.55 billion in 2026". [PRIMARY transcript] — [Q4 FY2025 call](https://www.fool.com/earnings/call-transcripts/2025/12/10/synopsys-snps-q4-2025-earnings-call-transcript/)
  - Outcome (26 Aug 2026): "have repaid the term loans earlier than planned"; "Total debt at the end of Q3 was approximately $10 billion". [PRIMARY transcript] — [Q3 call](https://www.webull.com/news/15497781661541376)
  - The 10-Q debt note records $3.5B of term-loan repayments (including $850M on Tranche 1, due 2027) out of $4.3B borrowed. Balance-sheet debt: short-term $1,020.2M (vs $22.1M at 31 Oct 2025); long-term $9,017.1M (vs $13,462.4M). [PRIMARY] — [R72](https://www.sec.gov/Archives/edgar/data/883241/000088324126000025/R72.htm); [10-Q](https://www.sec.gov/Archives/edgar/data/883241/000088324126000025/snps-20260731.htm) (accession 0000883241-26-000025)
  - Future principal payments at 31 Jul 2026 ($K): remainder of FY2026 11,057; FY2027 1,024,848; FY2028 1,024,848; FY2029 24,848; FY2030 2,024,848; FY2031 and later 6,000,000; total 10,110,449. The total is the $10B of notes plus a deferred 2025 rate-lock settlement paid semi-annually over 5.5 years at an implied 3.45%. Fair value of long-term debt ~$9.7B; revolver $850M committed (plus $150M uncommitted), $0 drawn; $16B bridge never drawn; $2.0B notional rate swaps. [PRIMARY] — [R73](https://www.sec.gov/Archives/edgar/data/883241/000088324126000025/R73.htm); [R72](https://www.sec.gov/Archives/edgar/data/883241/000088324126000025/R72.htm)
  - CORRECTION to the earlier log: the July 2027 and July 2028 term-loan tranches are no longer outstanding. The $1.02B of short-term debt at 31 Jul 2026 is mainly the notes due in fiscal 2027.
  - Net debt on book values ≈ $10.04B - $3.61B = ~$6.43B (my arithmetic). StockAnalysis shows $7.23B, which includes leases. Gross debt is about 2.5x FY2026E non-GAAP operating income and about 2.0x FY2027E (net about 1.6x and 1.3x); these are my approximations from guidance midpoints. [SECONDARY] — [StockAnalysis statistics](https://stockanalysis.com/stocks/snps/statistics/)
- Capital: NVIDIA bought $2B of common stock at $414.79 per share (1 Dec 2025; "This partnership is not exclusive"), about 4.8M shares or ~2.5% of 191.64M shares (my arithmetic). Ghazi: "we welcome the $2 billion investment"; the deal was expected to be net accretive to FY2026 EPS. On 5 Oct 2026 Synopsys signed a $1 billion accelerated share repurchase agreement with JPMorgan Chase Bank. [PRIMARY] — [NVIDIA release](https://news.synopsys.com/2025-12-01-NVIDIA-and-Synopsys-Announce-Strategic-Partnership-to-Revolutionize-Engineering-and-Design); [Q4 FY2025 call](https://www.fool.com/earnings/call-transcripts/2025/12/10/synopsys-snps-q4-2025-earnings-call-transcript/); [newsroom](https://news.synopsys.com/)
- Returns (GAAP, StockAnalysis, at fiscal year-ends): ROIC 16.53% (FY21), 22.43% (FY22), 24.88% (FY23), 24.08% (FY24), 3.88% (FY25), 2.23% TTM; ROE 14.81%, 17.76%, 20.70%, 18.60%, 7.16%, 3.66% TTM. Cash paid for acquisitions, net, was $16.5B, mainly Ansys. [SECONDARY / PRIMARY] — [StockAnalysis ratios](https://stockanalysis.com/stocks/snps/financials/ratios/); [10-K](https://www.sec.gov/Archives/edgar/data/883241/000088324125000028/snps-20251031.htm)
- Customer concentration: "we depend on a relatively small number of large customers for a large portion of our revenues". XBRL tags reference a "OneCustomer" concentration for FY2023 and FY2024, but the values are not visible, and the 10-Q discloses no customer percentage. [PRIMARY; percentages UNVERIFIED] — [10-K](https://www.sec.gov/Archives/edgar/data/883241/000088324125000028/snps-20251031.htm); [R90](https://www.sec.gov/Archives/edgar/data/883241/000088324126000025/R90.htm)
- Geography, FY2025: North America 45%, Europe 13%, Korea 13%, China 12% ($814.3M, vs $989.5M or 16% in FY2024), Other 18%. [PRIMARY] — [supplement](https://s201.q4cdn.com/778493406/files/doc_earnings/2025/q4/supplemental-info/Synopsys-Q4-FY2025-Financial-Supplement.pdf)
- Geography, 10-Q ($K):

| Region | Q3 FY26 | Q3 FY25 | 9M FY26 | 9M FY25 |
|---|---|---|---|---|
| US | 1,051,925 | 816,194 | 3,122,432 | 2,076,203 |
| Europe | 370,921 | 178,595 | 1,216,031 | 527,109 |
| Korea | 325,600 | 202,117 | 837,634 | 710,097 |
| China | 255,466 | 247,288 | 706,951 | 578,742 |
| Other | 472,910 | 295,543 | 1,278,557 | 907,167 |
| Total | 2,476,822 | 1,739,737 | 7,161,605 | 4,799,318 |

  China share (my arithmetic): Q3 FY26 10.3% (Q3 FY25 14.2%); 9M FY26 9.9% (9M FY25 12.1%); China +3.3% y/y in Q3 despite Ansys consolidation. US 42.5% and Korea 13.1% of Q3 FY26. [PRIMARY] — [R93](https://www.sec.gov/Archives/edgar/data/883241/000088324126000025/R93.htm)
- The IP problem (September 2025) and its course:
  - Q3 FY2025 (reported 9 Sep 2025): revenue $1.74B and non-GAAP EPS $3.39, against consensus of about $1.77B and $3.74; Design IP $427.6M vs $463.1M a year earlier. Ghazi cited export restrictions disrupting China design starts, a major foundry customer (unnamed; press speculated Intel), and "Some decisions made on our roadmap and resource allocations did not deliver the expected results." Shares fell ~34-35% intraday on 10 Sep 2025 (Barron's: to $401.50 in morning trading; Reuters headline: "nearly 35%"). [SECONDARY] — [SiliconANGLE](https://siliconangle.com/2025/09/09/shares-synopsys-crater-export-restrictions-derail-china-sales/); [TIKR](https://www.tikr.com/blog/synopsys-stock-sinks-22-as-revenue-and-earnings-miss-estimates-in-q3); [Barron's via iTiger](https://www.itiger.com/news/2566006396)
  - The 10-K adds: "challenges with a major foundry customer negatively impacted our financial results for fiscal year 2025". [PRIMARY]
  - Course since: FY2025 Design IP $1.75bn (-8%); Q1 FY2026 -6.5%; Q2 -6% (+12% q/q); Q3 +11% ("Design IP has returned to growth", "we've repositioned the portfolio to focus on the highest value opportunities", "The higher growth opportunity in IP lies with a growing set of AI customers"). Segment margin went from 16.2% in Q1 to 24.4% in Q2 and 26.5% in Q3. Growth targets moved from "mid-teens" (Aug 2026) to 17%+ CAGR (Investor Day). [PRIMARY] — [Q3 call](https://www.webull.com/news/15497781661541376)
- Divestitures:
  - Software Integrity business sold to funds affiliated with Clearlake Capital and Francisco Partners, closed 30 Sep 2024; total pre-tax gain $860.5M. [PRIMARY] — [10-Q R11](https://www.sec.gov/Archives/edgar/data/883241/000088324126000025/R11.htm)
  - Keysight completed its purchase of the Optical Solutions Group and Ansys PowerArtist, the remedies required for the Ansys approval, on 17 Oct 2025; FY2025 gain on divestitures $548.9M, mainly the optical business. [INDEPENDENT counterparty release; PRIMARY] — [Business Wire](https://www.businesswire.com/news/home/20251017434407/en/Keysight-Completes-Acquisition-of-Synopsys-Optical-Solutions-Group-and-Ansys-PowerArtist)
  - ARC Processor IP Solutions sale to GlobalFoundries completed 2 Jun 2026. [INDEPENDENT] — [GlobalFoundries release](https://www.nasdaq.com/press-release/globalfoundries-completes-acquisition-synopsys-processor-ip-solutions-business)

#### Inferences
- The financial strength is high on cash measures and improving fast. Leverage is no longer a binding constraint, as the early term-loan payoff and the buyback restart show. GAAP returns on capital will stay depressed for years by the ~$16.5B cash outlay and the Ansys intangibles. Investors should judge Synopsys on cash returns, not GAAP ROIC.

#### Gaps
- Exact customer-concentration percentages. The status of the BIS subpoenas (the Q3 10-Q contingencies note is generic; Part II was not read). Exact maturity dates of the 2027 and 2028 notes. A non-GAAP ROIC (I did not capture invested capital).

### e. Resilience

#### Takeaway
Historically Synopsys has been resilient to industry downturns: revenue was roughly flat in 2009 and grew through 2022-23. Its sharpest drawdowns have been self-inflicted or policy-driven (the IP and China shock of FY2025). The main future vulnerabilities are hardware and IP royalties in a financing-led pause, export controls (China ~10% of revenue, with a policy cliff on 10 Jan 2027), and AI-native challengers.

#### Cited findings
- Long revenue history (companiesmarketcap; appears to be calendar-year aggregation, e.g. "2025 $8.00B" vs fiscal $7.05B): 1999 $0.84B; 2000 $0.72B (-14.1%); 2001 $0.69B (-3.5%); 2002 $0.99B (+43.0%, includes the Avant! acquisition); 2003 $1.19B (+19.5%); 2004 $1.04B (-12.2%); 2005 $1.01B (-3.6%); 2007 $1.22B; 2008 $1.36B (+10.9%); 2009 $1.35B (-0.8%); 2010 $1.41B (+4.8%); 2021 $4.50B; 2022 $5.17B (+14.8%); 2023 $5.72B (+10.7%); 2024 $6.07B (+6.0%). [SECONDARY aggregator] — [companiesmarketcap](https://companiesmarketcap.com/synopsys/revenue/). Causes of the FY2000 and FY2004-05 declines were not checked [UNVERIFIED].
- FY2025 company-specific shock: China revenue fell 22% vs FY2024 excluding Ansys (-18% including it, per the call); the "Q3 2025 BIS Restrictions" "disrupted customer design starts in China"; Design IP fell 8%. Non-GAAP operating margin still held at 37.3%. [PRIMARY] — [10-K](https://www.sec.gov/Archives/edgar/data/883241/000088324125000028/snps-20251031.htm); [Q4 FY2025 call](https://www.fool.com/earnings/call-transcripts/2025/12/10/synopsys-snps-q4-2025-earnings-call-transcript/)
- Export controls:
  - The BIS licence requirement on EDA to China dated 23 May 2025 was rescinded on 2 July 2025. [PRIMARY, from the Cadence 10-K; cross-ref] — [Cadence FY2025 10-K](https://s206.q4cdn.com/597110084/files/doc_downloads/2026/Mar/CDNS-FY-2025-Form-10-K.pdf)
  - Synopsys has received BIS administrative subpoenas about transactions with certain Chinese entities. [PRIMARY] — [10-K](https://www.sec.gov/Archives/edgar/data/883241/000088324125000028/snps-20251031.htm)
  - Ghazi (10 Dec 2025): "we expect the environment to remain challenging in China"; "derisking it in our guide for FY '26"; "our inability to sell to the market that needs the most advanced solution"; "not only with entity list, but with technology restrictions". [PRIMARY transcript]
  - The BIS Affiliates (50%) rule was suspended from 10 Nov 2025 to 9 Nov 2026 under the US-China deal. On 28 Oct 2026 Dechert said reimposition on 10 Nov remained scheduled. BIS then extended the suspension to 10 Jan 2027 (announced 5 Nov 2026 per Thompson Hine; final rule 9 Nov 2026 per Squire Patton Boggs, FR doc 2026-22793, not read directly). [SECONDARY, law-firm summaries] — [Squire Patton Boggs](https://www.squirepattonboggs.com/insights/publications/bis-extends-suspension-of-affiliates-rule/); [Thompson Hine](https://www.thompsonhinesmartrade.com/2026/11/bis-extends-affiliates-rule-until-january-2027/); [Dechert](https://www.dechert.com/knowledge/onpoint/2026/10/bis-affiliates-rule--november-10-reimposition-remains-scheduled-.html)
  - China and export controls were not discussed on the Q3 FY2026 call (per the transcript).
- China localisation (cross-ref): Empyrean nine-month 2026 revenue RMB 960.13M (+19.3%); Primarius nine-month RMB 417.77M (+32.8%). Empyrean's figure is roughly $135M at ~7.1 RMB/$ (my conversion), against Synopsys's $707M of China revenue over a similar nine months. [PRIMARY; cross-ref] — [Empyrean Q3 report](https://static.cninfo.com.cn/finalpage/2026-10-30/1225641220.PDF); [Primarius Q3 report](https://static.cninfo.com.cn/finalpage/2026-10-31/1225648713.PDF)
- Hyperscaler and custom-chip exposure:
  - Amazon "Multi-year, $1B+ agreement" as lead customer for application-optimised IP (Nitro, Graviton, Trainium), with a quote from Amazon's Peter DeSantis; Synopsys will use Amazon Bedrock. [PRIMARY, counterparty-confirmed] — [release](https://news.synopsys.com/2026-09-30-Synopsys-and-Amazon-Announce-Strategic,-Multi-year-IP-Agreement-for-Custom-Silicon-Collaboration-Also-Extends-to-Cloud-and-AI-Powered-Engineering)
  - TrendForce (3 Aug 2026): capex at nine cloud providers up ~90% to more than $886.7bn in 2026 and ~$1.3tn in 2027. [SECONDARY; cross-ref] — [TrendForce](https://www.trendforce.com/presscenter/news/20260803-13161.html)
- Restructuring: the 2026 Plan (approved around 30 Nov 2025) brings a "10% workforce reduction ... largely complete ... in 2026", with ~$225M of restructuring cash costs in the FY2026 cash flow guide. Expected charges were $300-350M and were raised on 26 Aug 2026 to $425-500M; $236.3M was incurred in 9M FY2026 and $64.9M of liability remained at 31 Jul 2026. [PRIMARY] — [R70](https://www.sec.gov/Archives/edgar/data/883241/000088324126000025/R70.htm); [Q4 FY2025 call](https://www.fool.com/earnings/call-transcripts/2025/12/10/synopsys-snps-q4-2025-earnings-call-transcript/)
- 2026 governance and strategy:
  - Elliott took a multibillion-dollar stake (reported 23-24 Mar 2026). A cooperation agreement followed on 27 May 2026, and Elliott's Jesse Cohn joined the board on 1 Jun 2026. [SECONDARY / PRIMARY] — [The Star/Bloomberg](https://www.thestar.com.my/business/business-news/2026/03/24/elliott-said-to-take-multibillion-dollar-stake-in-synopsys); [release](https://news.synopsys.com/2026-05-27-Synopsys-Appoints-Jesse-Cohn-to-Board-of-Directors)
  - Long-term model set at the Investor Day.
  - Ansys integration: "ahead of the schedule on the cost synergy commitments", "committed ... to the $400 million synergy in year 4". [PRIMARY transcript] — [Q3 call](https://www.webull.com/news/15497781661541376)
  - The newsroom shows no executive appointments or departures in Oct-Nov 2026 listings; earlier months were not systematically checked. [PRIMARY] — [newsroom](https://news.synopsys.com/)

#### Inferences: scenarios to 2030 (my provisional judgement, not forecasts)
- Steady growth (~55%): the plan (~15% revenue CAGR, ~50% margin) looks achievable if IP holds 17%+ and EDA returns to double digits. Record HAV and AI-customer IP are the swing factors.
- Financing-led pause around 2028 (~25%): time-based licences (2-3 year terms; backlog of ~$10.9B, ~1.1x FY2026 revenue) cushion EDA, as in 2009. Hardware (upfront) and IP royalties tied to AI-chip volumes would fall first. Buybacks would be cut, but the notes due in FY2027 and FY2028 ($1B each) are small against ~$3B of FCF. Royalty-based IP (Amazon) makes Synopsys more cyclical than before.
- Faster acceleration (~20%): more design starts, emulation demand and agent consumption favour Synopsys. The risk is that agents compress seat counts faster than consumption pricing replaces them.
- Cycle position: EDA industry growth is ~12%, hardware is at record, IP is early in recovery, Ansys is in year one of integration, and leverage is falling. Synopsys looks mid-to-late cycle in hardware and early in IP.
- Revenue is driven by customers' design and R&D budgets, not fab capex. The 10-K links China weakness to "design starts".

#### Gaps
- Fiscal-year primary data for 2001-03 and 2008-09. Hardware revenue size. SAMR conditions on the Ansys deal (not read). The share of revenue from hyperscalers and systems companies (Cadence says 45% of its revenue comes from system companies; Synopsys gave no comparable figure in what I read).

---

## B. Path forward through the industry transitions

### Transition by transition (said versus done)

1. **Verification labour to tools.**
   - Said: "delivering agent engineers to our customers" (Q3 FY2026).
   - Done: AgentEngineer-based autonomous verification workflow showcased at DAC (26 Jul 2026), with availability "planned for the second half of 2026" and "Customers are currently evaluating". Engagements grew from 20 customers and 25+ agents (May 2026) to more than 30 active engagements (Aug 2026). Workflows with Microsoft and AMD on Microsoft Discovery (27 Jul 2026). [COMPANY CLAIM / PRIMARY] — [DAC release](https://news.synopsys.com/2026-07-26-Synopsys-Showcases-Comprehensive-Autonomous-Engineering-Workflows-from-Silicon-to-Systems,-Developed-with-NVIDIA-Technology); [AMD/Microsoft release](https://news.synopsys.com/2026-07-27-Synopsys-Advances-Agentic-AI-Chip-Design-with-AMD-and-Microsoft)
   - No paid, generally available deployment had been disclosed by 12 Nov 2026 [UNVERIFIED].
   - Synopsys benefits only if agents are priced as capacity, not as fewer seats.
2. **Seats to usage.**
   - Said: subscription plus consumption (May, Aug, Sep 2026); revenue share with OpenAI; licence-plus-royalty in IP.
   - Done: OpenAI and Amazon contracts signed (30 Sep 2026); no consumption revenue disclosed.
   - Funded: yes.
   - Timing: plausible for FY2027 to FY2028 renewals.
   - Must go right: customers accept a consumption layer on top of existing enterprise licence agreements rather than renegotiating them down.
3. **Simulation toward formal proof.**
   - Said: little in public. Formal was not mentioned on the Q3 FY2026 call, and the DAC claim is framed as coverage and "time-to-validated RTL", which is simulation-centred.
   - Done: Synopsys owns VC Formal and Formality; SCADE Design Verifier offers formal proof for safety software.
   - Evidence of a formal-first strategy for AI-edited chips: none found. This is the least coherent leg.
4. **Proprietary engines against open source plus AI.**
   - The Kimi K3 demo (17 Jul 2026) used open-source tools at 45nm with no sign-off; analysts saw no near-term revenue threat (details under (iii)).
   - Synopsys's answer is to make its engines the ground truth that models call: GPT-Synopsys; agents inside customer AI platforms; GPU acceleration with NVIDIA (20+ GPU-enabled products shown at GTC Berlin, 21 Oct 2026).
   - Done: the NVIDIA $2B equity stake and partnership (1 Dec 2025); the OpenAI agreement.
   - Must go right: foundries keep advanced PDKs and certification with the incumbents.
5. **Foundry certification as a barrier.**
   - Done: certified flows at TSMC (N2, A16, A14), Intel (18A, 18A-P, 14A) and Samsung 2nm generations; Rapidus is a collaboration only.
   - TSMC names only the big three in its full-line certification programme, although its EDA Alliance has 11 members, including China's Primarius.
   - This is the strongest and best-evidenced leg.
6. **A paying market for verified software.**
   - Synopsys sold its Software Integrity business on 30 Sep 2024, exiting general application-security testing.
   - It kept the Ansys SCADE qualified code generator and formal verifier, whose buyers are regulated system makers (aerospace, automotive, rail, energy, defence; Airbus, Subaru, Vestas among named users), and virtual prototypes (Infineon VDK, 10 Nov 2026).
   - Inference: Synopsys participates only in the certification-driven niche; the buyer there is the safety-regulated OEM, not general software teams.
7. **Model makers offering verification themselves.**
   - OpenAI chose to license Synopsys tools under a "preferred partners" multi-year deal (not stated as exclusive), with a revenue share and no GA date.
   - Anthropic reportedly runs a ~15-person chip team using Claude and approached EDA companies about chip-design data (The Information, 3 Nov 2026). SNPS fell 2.5% and CDNS 4.5% that day per an Investing.com-sourced report; The Information's briefing headline says 4%. [SECONDARY] — [The Information](https://www.theinformation.com/briefings/synopsys-cadence-shares-drop-4-information-report); [Dealroom summary](https://dealroom.co/news/169588-anthropic-tells-ipo-investors-its-15-person-chip-team-designs-custom-sil)
   - Ghazi on AI models: they "will absolutely participate and contribute to that reengineering of engineering". He was "not worried at all" about end-to-end AI design bypassing Synopsys.
   - No Synopsys partnership with Anthropic or Google was found; the search for Google ran after the budget was exhausted [UNVERIFIED].

### Background items checked
- (i) DAC 2026 claim. The exact wording is "up to 50X faster time-to-validated RTL" with "an additional 20% improvement in coverage". The footnote reads "Compared to traditional verification workflows not powered by AgentEngineer technology". The product is the autonomous design-verification workflow (AgentEngineer technology, developed with NVIDIA technology), presented at the 26 Jul 2026 DAC showcase. No customer is named; "Customers are currently evaluating"; availability "planned for the second half of 2026". Ghazi repeated "up to 50x faster time to validated RTL" on 26 Aug 2026. The brief's "validated design" overstates the scope, which is RTL only. [COMPANY CLAIM] — [DAC release](https://news.synopsys.com/2026-07-26-Synopsys-Showcases-Comprehensive-Autonomous-Engineering-Workflows-from-Silicon-to-Systems,-Developed-with-NVIDIA-Technology)
- (ii) AMD debugging figure. The source is the Synopsys release of 27 Jul 2026 with AMD and Microsoft: "Early evaluations show reductions of 25–40% in debug cycle time", headlined as "up to 40% reduction in cycle time". AMD (Alex Starr, Corporate Fellow) says only that AMD is "actively evaluating". AMD does not confirm the figures. [COMPANY CLAIM] — [release](https://news.synopsys.com/2026-07-27-Synopsys-Advances-Agentic-AI-Chip-Design-with-AMD-and-Microsoft)
- (iii) The Kimi K3 sell-off.
  - The demo: Moonshot blog (results "current as of July 16, 2026"); a single autonomous 48-hour run; 4 mm², 100 MHz, 1.46M cells; Nangate 45nm library; open-source tools; simulated only; no tape-out; weights not yet released at the time. [PRIMARY] — [Kimi blog](https://www.kimi.com/blog/kimi-k3); [nano-kpu](https://github.com/MoonshotAI/nano-kpu)
  - Share moves on Friday 17 Jul 2026: SNPS about -8.2% intraday (-8.17% to $382.98) and CLOSED $384.28, -7.85% (~$6.3B of value). CDNS -9.64% intraday ($329.50), closed $330.11 (-9.47%). Investing.com reported "roughly 9%" for both. [SECONDARY] — [ts2.tech 17 Jul](https://ts2.tech/en/synopsys-nasdaqsnps-stock-sinks-as-kimi-chip-demo-tests-the-eda-moat/); [stockti close](https://stockti.com/synopsys-plunges-7-85-as-moonshot-ai-s-open-source-chip-demo-rattles-eda-sector); [stockti intraday](https://stockti.com/synopsys-shares-plunge-8-as-moonshot-ai-s-chip-demo-raises-eda-moat-concerns); [ts2.tech 18 Jul](https://ts2.tech/en/synopsys-nasdaqsnps-loses-6-3-billion-following-kimi-k3-chip-design-demonstration/); [Investing.com](https://www.investing.com/news/stock-market-news/cadence--synopsys-slide-as-kimi-k3-designs-chip-in-48h-using-no-proprietary-eda-4798775); [TIKR on CDNS](https://www.tikr.com/blog/cadence-stock-fell-9-in-a-day-on-a-chinese-ai-chip-demo-heres-where-the-stock-could-go-in-2026)
  - Following days: on 22 Jul SNPS closed $389.07 (+2.8% that day), with the 30-day return still -14.6%. Tech Fund (27 Jul 2026) put the fall since the news at "around 14%", which does not match the closes above unless measured from an earlier high. [SECONDARY] — [Sahm Capital](https://www.sahmcapital.com/news/content/synopsys-snps-rebounds-as-mizuho-calms-ai-design-fears-and-value-debate-returns-2026-07-22); [Tech Fund](https://www.techinvestments.io/p/the-eda-crash-and-the-massive-ai)
  - Analysts:
    - Bloomberg Intelligence (Niraj Patel): "We see no immediate threat to Cadence and Synopsys' revenue bases"; leading-edge chips are "entrenched on Cadence and Synopsys' proprietary engines".
    - BNP Paribas (Andrew DeGasperi): overdone, because a 45nm demo cannot be compared with sub-5nm nodes.
    - Mizuho: Kimi K3 "strengthens rather than weakens" its thesis.
    - Bernstein's Robin Zhu was also quoted.
    - Tech Fund: TSMC certifies the three vendors via OIP; open tools lack advanced PDKs.
    - [SECONDARY]
  - Management did not discuss Kimi on the Q3 call; the "not worried at all" remark above was the closest response.
  - By 11 Nov 2026 the shares ($462.12) were about 20% above the 17 Jul close (my arithmetic).

### Provisional verdict (my provisional judgement)
**Partly coherent, leaning coherent.**
- The plan rests on Synopsys's real moat: certified sign-off engines as the ground truth that agents and frontier models must call.
- It is funded: ~$2.6-3.1B of annual FCF, the $2B NVIDIA placement, term loans repaid early and buybacks restarted.
- Headline counterparties are signed: OpenAI, Amazon, Microsoft/AMD and NVIDIA.
- What keeps it from "coherent":
  - Agent monetisation is announced, not demonstrated (no GA, no consumption revenue, no customer-confirmed metrics).
  - Core EDA growth lagged Cadence and the industry in 2026.
  - There is no visible formal-proof strategy for AI-edited designs.
  - The IP turnaround is two quarters old.
- What must go right:
  - Paid agent deployments and a consumption line in FY2027.
  - EDA back to double digits.
  - IP at 17%+ with royalties.
  - S&A at 10%+ and $400M of synergies.
  - Certification maintained at A14, 14A and next-generation 2nm.
  - No escalation of export controls when the Affiliates-rule suspension ends on 10 Jan 2027.

---

## C. Entry point (valuation and timing only; separate from quality)

### Takeaway
At $462.12 (close 11 Nov 2026), Synopsys trades at about 24-25x FY2027 non-GAAP EPS, 26x forward on StockAnalysis's measure (below its five-year range of 31.7-45.3x) and 10.2x trailing EV/sales. That is a clear discount to Cadence (forward P/E 34.9x, EV/sales 14.9x). The price roughly capitalises the FY2027 guidance but gives little credit for the FY2030 targets, consistent with market doubts about AI disintermediation and Synopsys's growth gap with Cadence.

### Cited findings
- Snapshot (close 11 Nov 2026; page updated 12 Nov): price $462.12; market cap $88.56B; EV $95.79B; 191.64M shares; trailing GAAP P/E 81.94; forward P/E 26.26; P/S 9.40 (forward 8.31); P/FCF 32.23; EV/sales 10.17; EV/EBITDA 46.15 (TTM GAAP EBITDA $2.08B); EV/FCF 34.86; debt/EBITDA 4.78 (GAAP); ROIC 2.23%; ROE 3.66%; TTM revenue $9.42B; TTM FCF $2.75B (FCF yield 3.10%); cash $3.61B; total debt $10.84B; net debt $7.23B; 52-week change +15.31%. [SECONDARY aggregator] — [StockAnalysis statistics](https://stockanalysis.com/stocks/snps/statistics/)
- My arithmetic from primary guidance:
  - P/E: 30.5x FY2026 consensus non-GAAP EPS ($15.14); 24.8x FY2027 consensus ($18.65); 24.2x the FY2027 guidance midpoint ($19.08); ~55x FY2027 GAAP EPS guidance midpoint ($8.39).
  - EV/sales: 9.9x FY2026E revenue ($9.715B midpoint); 8.6x FY2027E ($11.15B).
  - EV/FY2027E non-GAAP operating income (~$4.9B): ~19.5x.
  - FCF yield on FY2027E FCF ($3.1B): ~3.5% on market cap, ~3.2% on EV.
- Five-year history (StockAnalysis fiscal-year-end snapshots FY2021 to FY2025, then 11 Nov 2026), with five-year medians in brackets (my arithmetic):
  - Trailing P/E: 67.08 / 45.43 / 58.05 / 34.86 / 63.28, now 81.94 [58.05]
  - Forward P/E: 45.34 / 31.66 / 38.14 / 36.44 / 35.09, now 26.26 [36.44]
  - EV/sales: 11.88 / 9.52 / 13.22 / 12.67 / 13.73, now 10.17 [12.67]
  - EV/EBITDA: 54.20 / 32.70 / 46.07 / 48.52 / 72.92, now 46.15 [48.52]
  - P/FCF: 36.32 / 27.92 / 47.17 / 62.25 / 62.48, now 32.23 [47.17]
  - FCF yield: 2.75% / 3.58% / 2.12% / 1.61% / 1.60%, now 3.10% [2.12%]
  - Market cap ($M): 50,811 / 44,734 / 71,394 / 78,898 / 84,296, now 88,559
  - EV ($M): 49,959 / 43,920 / 70,290 / 77,613 / 96,843, now 95,793
  - Debt/EBITDA: 0.65 / 0.46 / 0.41 / 0.40 / 9.67, now 4.78
  - Buyback yield/dilution: -1.05% / 0.54% / 0.82% / -0.48% / -6.23%, now -21.14%
  - [SECONDARY] — [StockAnalysis ratios](https://stockanalysis.com/stocks/snps/financials/ratios/)
- Ten-year history (companiesmarketcap, year-end, TTM):
  - P/E: 2014 26.0, 2015 31.2, 2016 33.4, 2017 94.7, 2018 28.9, 2019 41.3, 2020 59.1, 2021 74.3, 2022 49.6, 2023 63.7, 2024 32.9, 2025 58.2; now 81.1. The 2016-2025 range is 28.9-94.7, median ~53.9 (my arithmetic).
  - P/S: 2014 3.11, 2015 3.48, 2016 3.71, 2017 4.78, 2018 4.28, 2019 6.07, 2020 8.81, 2021 12.1, 2022 8.80, 2023 12.5, 2024 13.0, 2025 11.9. The 2016-2025 median is ~8.8 (my arithmetic), against the current 9.40. The page's 2026 row is internally inconsistent (7.91 vs 2.84 vs 9.40).
  - Ten-year EV/EBITDA, forward P/E and FCF yield were not found.
  - [SECONDARY] — [P/E](https://companiesmarketcap.com/synopsys/pe-ratio/); [P/S](https://companiesmarketcap.com/synopsys/ps-ratio/)
- Cadence comparison (11 Nov 2026, StockAnalysis; cross-ref): price $329.26; market cap $90.34B; EV $91.61B; trailing P/E 65.47; forward P/E 34.94; EV/sales 14.94; EV/EBITDA 41.26; EV/FCF 51.94; FCF yield 1.95%; ROIC 17.09%. Cadence guides FY2026 revenue $6.387-6.417B (~21% growth) and a non-GAAP operating margin of 44.2-45.2%. [SECONDARY / PRIMARY] — [CDNS statistics](https://stockanalysis.com/stocks/cdns/statistics/); [Cadence CFO commentary](https://www.sec.gov/Archives/edgar/data/0000813672/000081367226000116/cfocommentary10262026ex9902.htm)
- Consensus (S&P Global via StockAnalysis, updated 9 Nov 2026): FY2026 revenue $9.72B (+37.8%) and non-GAAP EPS $15.14 (range $15.03-15.31); FY2027 revenue $11.00B (+13.2%) and EPS $18.65 (+23.2%). FY2028 is paywalled. Average target $589.55 (median $600; range $475-700; 25 analysts: 20 Strong Buy, 3 Buy, 2 Hold, 0 Sell). The FY2027 consensus sits BELOW management's guidance ($11.10-11.20B; $19.04-19.12). [SECONDARY] — [StockAnalysis forecast](https://stockanalysis.com/stocks/snps/forecast/)
- Seat and time-based exposure: time-based licences were 49.5% of FY2025 revenue and 40.5% of Q3 FY2026; maintenance and service 22.0% and 32.7%; upfront 28.5% and 26.9%. Services are not separated. [PRIMARY; my arithmetic]
- Near-term events:
  - Q4/FY2026 results and FY2027 outlook: Tuesday 8 Dec 2026, after market close (announced 5 Nov 2026). [PRIMARY via newswire] — [finviz](https://finviz.com/news/417651/synopsys-announces-earnings-release-date-for-fourth-quarter-and-fiscal-year-2026)
  - BIS Affiliates-rule suspension ends 10 Jan 2027 unless extended again.
  - $1.0B of notes due in fiscal 2027 (date not captured).
  - The $1B accelerated buyback (from 5 Oct 2026) and the policy of returning up to 50% of FCF.
  - Elliott cooperation agreement (Jesse Cohn on the board).
  - AgentEngineer workflow availability (H2 2026) and GPT-Synopsys launch (no date).
  - Model-maker news flow: Anthropic's reported IPO and chip team; Moonshot weight release [UNVERIFIED date].

### Inferences
- What the price assumes (my arithmetic, not a forecast): if management's mid-20s EPS CAGR from the FY2026 midpoint ($15.07) were achieved, FY2030 non-GAAP EPS would be roughly $36-38, putting today's price at ~12-13x. Consensus sits below even the FY2027 guidance. The market is therefore pricing a substantial chance that the long-term model, especially agent monetisation and margin expansion to ~50%, falls short, or that AI erodes the franchise.
- Cycle position for entry:
  - Hardware at record and IP in early recovery.
  - Backlog has drifted down: $11.4B, then $11B, then $10.9B.
  - Ansys synergies are ahead of schedule.
  - Leverage is falling and buybacks have resumed.
- Conditions under which entry would look more attractive:
  - Evidence of paid agent or consumption revenue.
  - Organic EDA growth converging with Cadence's.
  - Two or more further quarters of IP growth at mid-teens or better.
  - Net leverage below ~1x.
  - Clarity on export rules after 10 Jan 2027.
  - A sentiment-driven drawdown (as in July 2026) that compresses multiples further without damage to the sign-off franchise.
- This is analysis, not a recommendation.

### Gaps
- FY2028 consensus; ten-year medians for EV/EBITDA, forward P/E and FCF yield; Investor Day slides not read (FY2030 revenue mix, systems-company share).

---

## Closing lists

### 1. What I could not verify
- A Rapidus certification of Synopsys tools (only the 10 Dec 2024 collaboration was found).
- A tool-by-node certification map, including whether IC Validator is certified at A14.
- TSMC's certification test criteria.
- Market shares for StarRC, IC Validator, RedHawk-SC/Totem, Formality, VC Formal (vs Jasper), SpyGlass, Verdi and VIP.
- Hardware and services revenue; seat vs token licence mix.
- Customer-concentration percentages.
- Current status of the BIS subpoenas; SAMR conditions on Ansys.
- Exact maturity dates of the 2027 and 2028 notes.
- Fiscal-year primary revenue for the 2001-03 and 2008-09 downturns, and the causes of the FY2000 and FY2004-05 declines.
- Any Synopsys partnership with Google or Anthropic.
- Synopsys.ai Copilot pricing; the GA status of AgentEngineer workflows and GPT-Synopsys.
- FY2028 consensus; ten-year EV/EBITDA, forward P/E and FCF yield.
- Executive changes before Oct 2026, other than the board appointment.
- The Moonshot K3 weight-release date and the share reaction to it.

### 2. Where current evidence contradicts the background views or the brief
- The "about 9%" fall on the Kimi K3 news is right for Cadence (-9.47% close), but Synopsys closed -7.85% (-8.17% intraday).
- "Up to 50 times faster time to a validated design" is in fact "time-to-validated RTL", measured against workflows without AgentEngineer, with no customer named. The 25-40% debug figure is Synopsys's; AMD says only that it is "actively evaluating".
- CORRECTION to the earlier log: the term loans (tranches due July 2027 and July 2028) were fully repaid by 31 Jul 2026; ~$10B of notes remain. The restructuring cost is now $425-500M, not $300-350M. Design IP returned to growth (+11%) in Q3 FY2026.
- Prior "value moves to the judge": broadly supported. OpenAI licenses Synopsys tools as "ground truth", and analysts call the engines entrenched. But Synopsys does not own every judge (Calibre, Palladium), and each AI headline (Kimi, -7.85%; Anthropic, -2.5%) shows investors doubt how durable it is.
- Prior "seat-priced tools face pressure once agents drive open-source tools": I found no evidence of price pressure at Synopsys yet. It reports AI-enhanced renewal uplift (a claim) and is adding consumption layers. Its 2026 EDA growth gap with Cadence is unexplained and not evidence of open-source substitution.
- Prior "machine-proved regression checks standard by 2028 (60%)": the leading vendor's public agent story is coverage and simulation-centred, and formal was not mentioned on its latest call. This does not refute the prior, but nothing from Synopsys supports it.
- Prior "the big three keep growing through 2029": consistent with guidance of ~15% revenue CAGR to FY2030. No contradiction.
- Prior "final sign-off stays with people": Synopsys markets "autonomous" workflows, but no autonomous sign-off in production was found. Consistent with the prior.

### 3. Sources with dates
Primary, Synopsys:
- FY2025 supplement, 10 Dec 2025: https://s201.q4cdn.com/778493406/files/doc_earnings/2025/q4/supplemental-info/Synopsys-Q4-FY2025-Financial-Supplement.pdf
- 10-K FY2025, filed Dec 2025: https://www.sec.gov/Archives/edgar/data/883241/000088324125000028/snps-20251031.htm
- Q1 FY2026 release, 25 Feb 2026: https://news.synopsys.com/2026-02-25-Synopsys-Posts-Financial-Results-for-First-Quarter-Fiscal-Year-2026
- Q2 FY2026 8-K, 27 May 2026: https://www.sec.gov/Archives/edgar/data/0000883241/000119312526241911/d126227dex991.htm
- Q3 FY2026 release, 26 Aug 2026: https://news.synopsys.com/2026-08-26-Synopsys-Posts-Financial-Results-for-Third-Quarter-Fiscal-Year-2026
- Q3 FY2026 10-Q, 26 Aug 2026: https://www.sec.gov/Archives/edgar/data/883241/000088324126000025/0000883241-26-000025-index.htm ; https://www.sec.gov/Archives/edgar/data/883241/000088324126000025/snps-20260731.htm
- 10-Q XBRL note pages: R11, R28, R70, R72, R73, R90, R93 (same folder)
- Investor Day, 30 Sep 2026: https://news.synopsys.com/2026-09-30-Synopsys-Details-Growth-Strategy-and-Long-term-Financial-Model-at-2026-Investor-Day (finviz copy https://finviz.com/news/397287/synopsys-details-growth-strategy-and-long-term-financial-model-at-2026-investor-day)
- GPT-Synopsys, 30 Sep 2026: https://news.synopsys.com/2026-09-30-OpenAI-and-Synopsys-Announce-GPT-Synopsys-Frontier-Intelligence-to-Revolutionize-Chip-Design
- Amazon, 30 Sep 2026: https://news.synopsys.com/2026-09-30-Synopsys-and-Amazon-Announce-Strategic,-Multi-year-IP-Agreement-for-Custom-Silicon-Collaboration-Also-Extends-to-Cloud-and-AI-Powered-Engineering
- TSMC, 23 Sep 2026: https://news.synopsys.com/2026-09-23-Synopsys-and-TSMC-Partner-to-Accelerate-AI-Systems-Innovation-with-Agentic-AI-and-Advanced-Design
- TSMC, 22 Apr 2026: https://news.synopsys.com/2026-04-22-Synopsys-Partners-with-TSMC-to-Power-Next-Generation-AI-Systems-with-Silicon-Proven-IP-and-Certified-EDA-Flows
- TSMC, 25 Sep 2023: https://news.synopsys.com/2023-09-25-Synopsys-and-TSMC-Collaborate-to-Accelerate-2nm-Innovation-for-Advanced-SoC-Design-with-Certified-Digital-and-Analog-Design-Flows
- Intel, 27 Jul 2026: https://news.synopsys.com/2026-07-27-Synopsys-and-Intel-Foundry-Fast-Track-Customer-Readiness-from-Silicon-to-Systems-on-Intel-14A
- Samsung, 28 May 2026: https://news.synopsys.com/2026-05-28-Synopsys-Advances-Power-and-Performance-for-AI-and-Multi-Die-Designs-on-Latest-Samsung-Foundry-Processes-at-SAFE-Forum-2026
- DAC, 26 Jul 2026: https://news.synopsys.com/2026-07-26-Synopsys-Showcases-Comprehensive-Autonomous-Engineering-Workflows-from-Silicon-to-Systems,-Developed-with-NVIDIA-Technology
- AMD/Microsoft, 27 Jul 2026: https://news.synopsys.com/2026-07-27-Synopsys-Advances-Agentic-AI-Chip-Design-with-AMD-and-Microsoft
- HAV launch, 11 Mar 2026: https://news.synopsys.com/2026-03-11-Synopsys-Introduces-Software-Defined-Hardware-Assisted-Verification-to-Enable-AI-Proliferation
- NVIDIA, 1 Dec 2025: https://news.synopsys.com/2025-12-01-NVIDIA-and-Synopsys-Announce-Strategic-Partnership-to-Revolutionize-Engineering-and-Design
- Jesse Cohn appointment, 27 May 2026: https://news.synopsys.com/2026-05-27-Synopsys-Appoints-Jesse-Cohn-to-Board-of-Directors
- Newsroom, read 12 Nov 2026: https://news.synopsys.com/
- Q4 results date, 5 Nov 2026: https://finviz.com/news/417651/synopsys-announces-earnings-release-date-for-fourth-quarter-and-fiscal-year-2026
- SCADE page, read 12 Nov 2026: https://ansys.synopsys.com/products/embedded-software/ansys-scade-suite

Transcripts (third-party transcription of primary calls):
- Q4 FY2025, 10 Dec 2025: https://www.fool.com/earnings/call-transcripts/2025/12/10/synopsys-snps-q4-2025-earnings-call-transcript/
- Q2 FY2026, 27 May 2026: https://www.fool.com/earnings/call-transcripts/2026/05/27/synopsys-snps-q2-2026-earnings-transcript/
- Q3 FY2026, 26 Aug 2026: https://www.webull.com/news/15497781661541376

Counterparties and other primary documents:
- TSMC OIP page, read 12 Nov 2026: https://www.tsmc.com/english/dedicatedFoundry/oip/eda_alliance
- Keysight, 17 Oct 2025: https://www.businesswire.com/news/home/20251017434407/en/Keysight-Completes-Acquisition-of-Synopsys-Optical-Solutions-Group-and-Ansys-PowerArtist
- GlobalFoundries, 2 Jun 2026: https://www.nasdaq.com/press-release/globalfoundries-completes-acquisition-synopsys-processor-ip-solutions-business
- Rapidus, 10 Dec 2024: https://prnewswire.com/news-releases/rapidus-collaborates-with-synopsys-to-shorten-semiconductor-design-cycles-302327894.html
- Kimi blog, Jul 2026: https://www.kimi.com/blog/kimi-k3
- nano-kpu repository: https://github.com/MoonshotAI/nano-kpu
- ESD Alliance Q2 2026, 19 Oct 2026: https://www.prnewswire.com/news-releases/electronic-system-design-industry-posts-5-7-billion-in-revenue-in-q2-2026--esd-alliance-reports-302912151.html
- Wilson study, 8 Sep 2026: https://blogs.sw.siemens.com/verificationhorizons/2026/09/08/the-2026-functional-verification-study/
- Cadence 10-K FY2025, Mar 2026: https://s206.q4cdn.com/597110084/files/doc_downloads/2026/Mar/CDNS-FY-2025-Form-10-K.pdf
- Cadence CFO commentary, 26 Oct 2026: https://www.sec.gov/Archives/edgar/data/0000813672/000081367226000116/cfocommentary10262026ex9902.htm
- Cadence Q3 2026 call, 26 Oct 2026: https://www.webull.com/news/15818016766808064
- Empyrean Q3 report, 30 Oct 2026: https://static.cninfo.com.cn/finalpage/2026-10-30/1225641220.PDF
- Primarius Q3 report, 31 Oct 2026: https://static.cninfo.com.cn/finalpage/2026-10-31/1225648713.PDF

Secondary:
- SemiAnalysis, 21 May 2026: https://newsletter.semianalysis.com/p/eda-market-primer
- MarketResearch.com (undated summary): https://marketresearch.com/Prof-Research-v4036/Electronic-Design-Automation-EDA-Global-39562423
- SemiWiki/IPnest, 2026: https://semiwiki.com/ip/373010-the-9-5-billion-design-ip-market-shifting-boundaries-arms-monopoly-and-the-risc-v-response/ ; https://semiwiki.com/ip/370809-consolidation-and-competition-who-is-winning-the-4-5-billion-interface-ip-race/
- Futurum, Sep/Oct 2026: https://futurumgroup.com/insights/synopsys-investor-day-2026-turns-eda-into-a-royalty-and-ai-model-revenue-share-business/
- TIKR on Q3 FY2026, Aug 2026: https://www.tikr.com/blog/synopsys-q3-earnings-call-just-promised-double-digit-eda-growth-heres-the-math-behind-it
- TIKR on Q3 FY2025, Sep 2025: https://www.tikr.com/blog/synopsys-stock-sinks-22-as-revenue-and-earnings-miss-estimates-in-q3
- SiliconANGLE, 9 Sep 2025: https://siliconangle.com/2025/09/09/shares-synopsys-crater-export-restrictions-derail-china-sales/
- Barron's via iTiger, 10 Sep 2025: https://www.itiger.com/news/2566006396
- ts2.tech, 17 Jul 2026: https://ts2.tech/en/synopsys-nasdaqsnps-stock-sinks-as-kimi-chip-demo-tests-the-eda-moat/
- ts2.tech, 18 Jul 2026: https://ts2.tech/en/synopsys-nasdaqsnps-loses-6-3-billion-following-kimi-k3-chip-design-demonstration/
- stockti, 17 Jul 2026: https://stockti.com/synopsys-shares-plunge-8-as-moonshot-ai-s-chip-demo-raises-eda-moat-concerns ; https://stockti.com/synopsys-plunges-7-85-as-moonshot-ai-s-open-source-chip-demo-rattles-eda-sector
- Investing.com, 17 Jul 2026: https://www.investing.com/news/stock-market-news/cadence--synopsys-slide-as-kimi-k3-designs-chip-in-48h-using-no-proprietary-eda-4798775
- TIKR on Cadence, Jul 2026: https://www.tikr.com/blog/cadence-stock-fell-9-in-a-day-on-a-chinese-ai-chip-demo-heres-where-the-stock-could-go-in-2026
- Sahm Capital, 22 Jul 2026: https://www.sahmcapital.com/news/content/synopsys-snps-rebounds-as-mizuho-calms-ai-design-fears-and-value-debate-returns-2026-07-22
- Tech Fund, 27 Jul 2026: https://www.techinvestments.io/p/the-eda-crash-and-the-massive-ai
- The Information, 3 Nov 2026: https://www.theinformation.com/briefings/synopsys-cadence-shares-drop-4-information-report
- Dealroom, Nov 2026: https://dealroom.co/news/169588-anthropic-tells-ipo-investors-its-15-person-chip-team-designs-custom-sil
- The Star/Bloomberg, 24 Mar 2026: https://www.thestar.com.my/business/business-news/2026/03/24/elliott-said-to-take-multibillion-dollar-stake-in-synopsys
- eeNews Europe, Dec 2024: https://www.eenewseurope.com/en/rapidus-signs-2nm-deals-with-synopsys-cadence/
- Squire Patton Boggs, Nov 2026: https://www.squirepattonboggs.com/insights/publications/bis-extends-suspension-of-affiliates-rule/
- Thompson Hine, Nov 2026: https://www.thompsonhinesmartrade.com/2026/11/bis-extends-affiliates-rule-until-january-2027/
- Dechert, 28 Oct 2026: https://www.dechert.com/knowledge/onpoint/2026/10/bis-affiliates-rule--november-10-reimposition-remains-scheduled-.html
- TrendForce, 3 Aug 2026: https://www.trendforce.com/presscenter/news/20260803-13161.html

Market data (secondary aggregators, read 12 Nov 2026 unless stated):
- StockAnalysis SNPS statistics: https://stockanalysis.com/stocks/snps/statistics/
- StockAnalysis SNPS ratios: https://stockanalysis.com/stocks/snps/financials/ratios/
- StockAnalysis SNPS forecast (updated 9 Nov 2026): https://stockanalysis.com/stocks/snps/forecast/
- StockAnalysis CDNS statistics: https://stockanalysis.com/stocks/cdns/statistics/
- companiesmarketcap revenue: https://companiesmarketcap.com/synopsys/revenue/
- companiesmarketcap P/E: https://companiesmarketcap.com/synopsys/pe-ratio/
- companiesmarketcap P/S: https://companiesmarketcap.com/synopsys/ps-ratio/
