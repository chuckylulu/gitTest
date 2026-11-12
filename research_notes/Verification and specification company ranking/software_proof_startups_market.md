# Software-proof companies (North America focus) and whether a paying market for verified software is forming

Research date: 12 November 2026; all statements are the position as of that date. Final notes, merging a first partial pass (raw log) and a continuation pass (12 Nov 2026). Every sourced fact, tag and URL from the raw log is kept; corrections are marked CORRECTION.

Tag key: [PRIMARY] filing, paper or official document (including a company's own primary page when the fact is about what it published); [INDEPENDENT] confirmed by an outside party; [COMPANY CLAIM] stated by the company, not confirmed by an outside party; [SECONDARY] press or analyst report only; [UNVERIFIED] could not verify. "Cross-reference" marks facts taken from other researchers' notes in this folder, not re-fetched by me.

Access note: the shared WebSearch budget ran out in both passes (after about 33 searches in the first, and again mid-way through the second), and Firecrawl had no credits. After that, work used direct fetches of known primary pages only, with no search workarounds. Pages that could not be read: BusinessWire releases (HTTP 403), citybiz (403), DARPA expMath page (404), morph.so (empty), and the PutnamBench and MathArena leaderboard tables (loaded by script). Coverage is thin for Morph Labs, insurers, the White House Office of the National Cyber Director (ONCD), and Asia outside Singapore.

## 1. Company map: who sells machine-checked proof for software, and what has shipped

### Takeaway
About fifteen organisations matter. Few have shipped a priced product for proving properties of real code: Harmonic (Aristotle for C and SystemVerilog, usage-priced, from 27 Oct 2026) and Imandra (seat tiers from $25 to $799 a month). Certora (covered elsewhere) is another. The rest sell engagements (Galois, Runtime Verification, Veridise, CertiK), give the service away (Axiom's AXLE, Math Inc's OpenGauss), or have no product yet (Theorem in beta; &Truth and Pramaana with no customers). No AI-native proof company has disclosed revenue.

### Cited Findings

**Harmonic (Aristotle).** Details of the October launch, funding and customers are in sections 2 and 3.
- News index: first post "Introduces Harmonic" 10 Jun 2024; Series A 23 Sep 2024; Series B 9 Jul 2025; IMO 2025 "gold medal-level" result and iOS app beta 28 Jul 2025; Series C 25 Nov 2025; python-memtools open-sourced 19 Jan 2026; mathematician sponsorships 22 Jan 2026 [PRIMARY]. HQ and founding date were not re-verified. https://harmonic.fun/news
- Co-founded by Robinhood CEO Vlad Tenev; CEO Tudor Achim. As of Sep 2025 it "has raised $100 million" (superseded by the Series C) [SECONDARY]. https://www.upstartsmedia.com/p/math-ai-startups-push-new-models

**Axiom Math (AxiomProver, AXLE).** See section 2.

**Math Inc. (Gauss) and Morph Labs**
- Hack VC (18 Jun 2026): Jesse Han is CEO. The investor says "early procurement work through Galois/RAND and DARPA OTA vehicles", calls the public sector the "strongest near-term driver", and says Tao works with no other company [PRIMARY investor post; investor claim]. https://blog.hack.vc/why-we-invested-in-math-inc/
- Gauss page: funded by DARPA's expMath programme; partner Morph Labs [COMPANY CLAIM]. https://www.math.inc/gauss
- Archive (items undated, read 12 Nov 2026): "Introducing Gauss"; Veritas Fellowships naming Terry Tao (inaugural), Maryna Viazovska and Kevin Buzzard; "Fields Medal sphere packing proof formalized"; "OpenGauss: an open source, state of the art autoformalization harness"; "FormalQualBench: measuring a higher standard of correctness for autoformalization". The homepage has no product, pricing or customer information [COMPANY CLAIM]. https://www.math.inc/archive . Read Hack VC's Tao statement with this in mind: Tao is a named Math Inc. fellow.
- IEEE Spectrum: Math Inc. formalised the strong Prime Number Theorem in three weeks (Sep 2025; ~25,000 lines, more than 1,000 theorems and definitions). It announced 8-dimensional sphere packing on 23 Feb 2026, then 24-dimensional (200,000+ lines in two weeks). The human sphere-packing team, after about two years on the project, were "very surprised" [SECONDARY]. https://spectrum.ieee.org/ai-proof-verification
- Scientific American, 26 Mar 2026: muted reaction among mathematicians to the sphere-packing result; quotes from Hariharan [SECONDARY]. https://www.scientificamerican.com/article/what-happens-when-ai-starts-checking-mathematicians-work
- Funding: Caplight lists a seed round for "Math, Inc." dated 16 Sep 2024 (Khosla, Arben, Betaworks); this may be a different company [UNVERIFIED]. https://www.caplight.com/company/math . A wiki aggregator says Math Inc. was incubated at Morph Labs, with co-founders Christian Szegedy and Jesse Michael Han; Han is also CEO of Morph Labs [SECONDARY]. https://aiwiki.ai/wiki/math_inc_gauss . The morph.so page returned no content, so Morph Labs' 2026 status is not verified.

**Logical Intelligence (Aleph, Noa, Kona)**
- At launch, 19 Sep 2025: CEO Eve Bodnia; Michael Freedman (Fields Medal), chief science officer; Vlad Isenbaev, chief research officer; Mikhail Rubinchik, CTO. Staff of 16. Two agents: Aleph writes proofs and Noa audits code. Targets: blockchain wallets, health data, drones and aircraft, chip design. The company claims "100% accuracy". An unnamed AI investor: "I doubt that most AI generated code is going to end up formally verified." [SECONDARY]. https://www.upstartsmedia.com/p/math-ai-startups-push-new-models
- Release of 20 Jan 2026, as relayed on 26 Jan: San Francisco-based. Kona 1.0, an "energy-based reasoning" model. Yann LeCun is founding chair of the technical research board. Patrick Hillmann (ex-GE, ex-Binance) is Chief Strategy Officer. Pilots planned with unnamed partners in advanced manufacturing, energy and semiconductors. No funding disclosed. Bodnia: "We are seeing in Kona the first credible signs of AGI" [SECONDARY; COMPANY CLAIM]. https://iotm2mcouncil.org/iot-library/news/connected-industries-news/logical-unveils-energy-based-reasoning/ ; original release https://www.businesswire.com/news/home/20260120751310/en/ (403)
- Homepage, metadata dated 10 Nov 2026: now "a scientific reasoning platform for industrial R&D teams" ("Building Workbench"). Address: 1011 3rd Street, San Francisco. Team: Bodnia (CEO), Hillmann (Chief Strategy & Operating Officer), Anitha Kannan (Chief of AI), Alex Fetisov (CTO), Freedman (Chief Science Officer), Boris Hanin (head of scientific advisory board), LeCun. The homepage no longer mentions Aleph, Noa, Kona, or code or chip verification. Isenbaev is not listed [COMPANY CLAIM]. https://logicalintelligence.com/
- Benchmarks:
  - Company blog, 20 May 2026: Aleph 99.4% on PutnamBench; 94% on VeriSoftBench against Aristotle's 69%; 100% on Verina, "confirmed independently by benchmark authors"; enterprise customers run Aleph over proprietary Lean libraries [COMPANY CLAIM]. https://logicalintelligence.com/blog/aleph-prover-tops-leading-benchmarks
  - MathArena: AlephProver ranked first of 10 on ArXivLean in 03/2026 (34.15%) and first of 14 in 06/2026 (86.96%), at an expected $66.84 per problem [INDEPENDENT]. https://matharena.ai/models/logical_intelligence_aleph_prover
  - The site is said to report PutnamBench 672/672, published 25 Aug 2026 (search summary; not fetched) [COMPANY CLAIM, UNVERIFIED]. https://logicalintelligence.com/aleph-prover-final.html
  - The Dec 2025 release reportedly gave Aleph 76% on PutnamBench, and Bodnia called Aleph "an internal tool to test the mathematical rigor of the environment we are creating, not to be our core model" (search summary; release returned 403) [UNVERIFIED]. https://www.businesswire.com/news/home/20251202089385/en
- Funding: CB Insights lists an undisclosed round dated 1 Oct 2025, with Pebblebed among the investors (search snippet) [UNVERIFIED]. https://www.cbinsights.com/company/logical-intelligence/financials

**Theorem**
- $6M seed led by Khosla Ventures, announced 27–29 Jan 2026, with YC participating. Co-founders Jason Gross and Rajashree Agrawal; four people in San Francisco; YC Spring 2025. Pitch: program verification "10,000 times faster" [COMPANY CLAIM]. Its SFBench demo translated 1,276 Rocq problems to Lean with proofs of equivalence [COMPANY CLAIM]. https://venturebeat.com/security/theorem-wants-to-stop-ai-written-bugs-before-they-ship-and-just-raised-usd6m
- Its YC page invites companies to join the beta; no named customers found. https://www.ycombinator.com/companies/theorem-2/jobs
- Its main outside validation is Anthropic's Frontier Red Team collaboration of 22 Oct 2026, for which Theorem supplied the RISC-V and Linux process semantics [PRIMARY]; see section 5. https://www.anthropic.com/research/formal-verification

**&Truth**
- Emerged 29 Oct 2026 with a $70M seed. A public benefit corporation founded early 2026, based in Palo Alto and Singapore. Clark Barrett is co-CEO (Stanford; co-director, Stanford Center for AI Safety); Ilya Sergey is Chief Science Officer (NUS VERSE Lab); Chris Hsu is co-CEO and Executive Chairman. Investors and terms are not disclosed ("AI safety and venture capital leaders").
- Product: a "universal verification machine" for code in any language, built on Lean and the open-source CSLib, plus "specification factory" technology to turn business requirements into formal specifications. No customers or pricing.
- Demo: AI-assisted verification of part of Signal's encryption code took "under half a day and less than $500", against about five months for three engineers by hand [SECONDARY; COMPANY CLAIM]. https://dealroom.co/news/168019-truth-emerges-from-stealth-with-70m-seed-to-mathematically-prove-code-is/

**Pramaana Labs** (Palo Alto): $27M seed led by Khosla, June 2026. Applies Lean to AI outputs in law, tax, drug discovery, financial compliance and government policy, and is training formalisation and prover models [SECONDARY]. https://siliconangle.com/2026/06/17/pramaana-labs-raises-27m-make-ai-prove-answers/ ; https://thenextweb.com/news/pramaana-labs-27m-seed-formal-verification-ai

**Code Metal, Galois, Runtime Verification, Imandra.** See section 3.

**Veridise** (Austin per most sources; CB Insights says Singapore, unresolved)
- Only disclosed round: a $4.7M seed, 26 Jul 2022 (Polychain, Hack VC) [SECONDARY/aggregator].
- AuditHub (2025) bundles Vanguard, OrCa, Picus and ZK Vanguard. Picus verified 21 of 26 ZKsync Airbender circuits, and three critical soundness bugs were fixed [COMPANY CLAIM].
- RootData: Chief Security Officer Ben Sepanski left in Apr 2026; product integration work ran Mar–Sep 2026 [SECONDARY].
- https://veridise.com/blog/veridise-announcements/audithub-launches-platform-for-professional-blockchain-audit-firms/ ; https://www.rootdata.com/projects/detail/Veridise?k=NjA2Mg%3D%3D

**CertiK**
- Jan 2026 (Davos): IPO ambition at about a $2B valuation. That figure rests on the 2022 $88M Series B3 (Insight, Tiger Global, Advent). In a Feb 2026 interview the company had "no concrete plans" for an IPO [SECONDARY].
- Co-founder Ronghui Gu says audits remain the main revenue source. Dealroom gives a revenue range of $10–50M (an estimate, not a disclosure) [UNVERIFIED].
- https://www.crowdfundinsider.com/2026/01/258056-blockchain-security-firm-certik-maintains-ipo-plans-as-valuation-reaches-2-billion/ ; https://www.theblock.co/post/386882 ; https://dealroom.co/companies/certik/

**Other 2026 newcomers, any country**
- Cajal (YC W2026): multi-agent Lean 4 checking of mathematical proofs; aggregator write-up only [SECONDARY]. https://www.startuphub.ai/news/claudes-corner-cajal-yc-w2026
- Lanyon AI: $10.6M round for formally verified scientific computing [SECONDARY]. https://runtimewire.com/es/article/lanyon-ai-10-6m-formally-verified-scientific-computing
- VerifAIX (Cupertino; teams in the US, India and Israel): $5M seed, Sep 2026, co-led by Endiya Partners and Bluehill VC; AI plus formal methods for chip verification [SECONDARY]. https://www.finsmes.com/2026/09/verifaix-raises-usd5m-in-seed-funding.html
- Axiomatic AI ($18M seed, Mar 2026) and Midas ($10M, Feb 2026): recorded by the first pass with no URL [UNVERIFIED].
- Cross-reference (europe_israel_specialists.md): Normal Computing (New York), $50M strategic round, Mar 2026, led by Samsung Catalyst Fund, working on auto-formalisation for chip-design verification and RTL. https://semiengineering.com/startup-funding-q1-2026/

**Non-profits that steward the checkers and standards**
- Lean FRO:
  - A non-profit under Convergent Research, founded Jul 2023. Leonardo de Moura is Chief Architect; he created Lean and is also a senior principal applied scientist at AWS. Sebastian Ullrich is Head of Engineering.
  - Funders: Alex Gerko, Sloan, the Richard Merkin Foundation, Simons Foundation International, Convergent Research. Jul 2025: $10MM from Gerko ($5MM to a Mathlib Initiative, $5MM to the FRO). Feb 2026: Harmonic's "inaugural donation", which Harmonic puts at $300,000. Jul 2026: an Amazon donation, "the largest in FRO history" (amount not given). Sep 2026: further support from XTX Markets.
  - Shipped: Lean Kernel Arena, Apr 2026 ("public benchmarking of independent proof checkers"); Comparator, Jun 2026 ("a sandboxed judge for Lean proofs"); con-leche, Sep 2026 ("an external Lean checker proven in Lean to be consistent").
  - Goal: "long-term self-sustainability" [PRIMARY]. https://lean-lang.org/fro/about ; https://harmonic.fun/news/lean-fro-donation/
  - Roadmaps run Year 1 (Aug 2023–Jul 2024) to Year 3 (Aug 2025–Jul 2026), then Year 4 Part 1 (Sep 2026–Feb 2027). They are now six-monthly because "our field is changing too quickly to commit to a plan a year ahead" [PRIMARY]. https://lean-lang.org/fro/roadmap ; https://lean-lang.org/fro/roadmap/y4-1
- Atlas Computing: the Atlas Computing Institute, a 501(c)(3), "has found a new life with a new team as Sparrow Infrastructure". Its work continues at Atlas Ignota, "now housed under Convergent Research", including the FMxAI event series. Oath Technologies is named as a new FRO that Atlas helped start. No 2026 dates or programme details on the page [PRIMARY]. https://atlascomputing.org/
- Beneficial AI Foundation:
  - Funds and collaborates with researchers at MIT, UC Berkeley, Cambridge, Oxford, ETH Zurich, Max Planck, CMU and UM. No leadership or funders are shown [PRIMARY]. https://www.beneficialaifoundation.org/
  - Its "Signal Shot" aims to "formally verify the Signal protocol and Signal app with Lean" (repositories libsignal-verify, PQXDH, SPQR). Co-chairs: Rolfe Schmidt (Signal) and Leonardo de Moura (Lean FRO). Collaborators include Cryspen, CSlib, Stanford, VERSE/NUS, Galois, UC Berkeley, Google, Microsoft, CISPA, NYU, RAND, CMU, ETH Foundation, MPI-SP and the University of Florida.
  - Launched 20 Apr 2026 in Paris. A "Signal Shot milestone" post is dated 10 Nov 2026 (content not seen). No funding or prize is stated [PRIMARY]. https://www.beneficialaifoundation.org/signal-shot

### Inferences
- The field has three business types:
  - AI-native provers with large venture rounds and mathematics results: Harmonic, Axiom, Math Inc., Logical Intelligence.
  - Newer software-first proof start-ups: Theorem, &Truth, Pramaana.
  - Established formal-methods firms that mostly sell labour: Galois, Runtime Verification, Imandra, Veridise, CertiK.
- My arithmetic from the sourced rounds: AI-native proof companies have raised at least about $823M (Harmonic ~$295M, Axiom ~$264M, Code Metal ~$161M, &Truth $70M, Pramaana $27M, Theorem $6M). The three with published valuations total $4.3B (Harmonic $1.45B, Axiom $1.6B, Code Metal $1.25B).
- Logical Intelligence's November homepage no longer mentions code verification. That suggests at least a change of emphasis away from selling proof (my inference from company pages).

### Gaps
- Founding dates and headquarters were not verified for Harmonic, Axiom, Math Inc., Code Metal, Imandra or CertiK.
- Morph Labs' 2026 products and funding, and Logical Intelligence's and Math Inc.'s round sizes, were not found.
- No Chinese, Indian, Japanese or Korean software-proof start-up surfaced in the searches available; coverage outside North America and Singapore is thin.

## 2. Background items checked: Harmonic's C and Verilog launch; Harmonic's and Axiom's 2026 funding and traction; what "Axiom" means

### Takeaway
(i) Confirmed, with two refinements. Harmonic announced C and Verilog verification on 27 Oct 2026, and its documentation names SystemVerilog, not plain Verilog. What shipped is a usage-priced service (web app, command line, Python SDK, MCP server), not a seat licence. The only customer quoted by name is the chip start-up Tensordyne, plus a General Atomics fusion-lab user reported by Reuters.
(ii) Harmonic raised no new round in 2026: its Series C closed in Nov 2025, and Nvidia's NVentures joined it in Jan 2026. Axiom raised $200M at $1.6B+ in Mar 2026. Neither discloses revenue.
(iii) In this field "Axiom" means Axiom Math (legal name Axiom Quant Inc., prover AxiomProver). It should not be confused with axiom.xyz, a zero-knowledge proof company that also uses Lean.

### Cited Findings

**(i) Harmonic, 27 Oct 2026**
- Announcement, "Aristotle Expands Into Formal Verification for Software and Hardware, Starting With C and Verilog" [PRIMARY; COMPANY CLAIM]. https://harmonic.fun/news/aristotle-software-hardware-verification
  - C: verification "against specified requirements, including functional correctness and the absence of certain classes of undefined behavior".
  - Verilog: control-path properties (liveness, safety) and mathematical data-path properties.
  - Workflow: Aristotle proposes properties from the code and reports each as proved, not proved, or proved under stated assumptions. Engineers review and commit the properties, which then run in continuous integration on every commit.
  - Pricing: self-serve and consumption-based, with no rates published. Enterprise plans offer volume pricing, dedicated support, and on-premises or private-cloud deployment.
  - CEO Tudor Achim: "mathematically verifying critical systems provides a new way to identify defects and vulnerabilities".
- Homepage: "Consumption-based, with no seats or licenses"; "Verilog and C today, with more planned"; a Heartbleed demonstration on OpenSSL 1.0.1f and 1.0.1g. Investors listed: Sequoia, Kleiner Perkins, Index, Paradigm, Ribbit, ERA, Blossom, DST Global [COMPANY CLAIM]. https://harmonic.fun/
- Documentation [COMPANY CLAIM]. https://aristotle.harmonic.fun/docs/overview
  - Aristotle "proves properties of existing C and SystemVerilog code". Specifications are written "in plain English" in the prompt or a text file. Results are Proved or Refuted, with assumptions listed.
  - Limit: "Behaviors not listed as properties are not verified".
  - Interfaces: web app, MCP server, command line, Python SDK (aristotlelib). Usage is paid in credits; no rates are shown.
- Tensordyne case study (Verilog), quoting the customer's engineer; it does not say whether Tensordyne pays [COMPANY CLAIM]. https://harmonic.fun/aristotle/case-studies/tensordyne/
  - Scale: a block of 12.2M gate equivalents and 1.24M flip-flops, with 312 pages of specifications.
  - 241 properties were checked: 100 written by Aristotle from the specifications and 141 pre-existing assertions. 185 were proved and 56 refuted with counterexamples. The bugs appeared 25,000 to 110,000 cycles after reset, and 8 were found early in the design of the next chip.
  - Jonathan Ko, ASIC Verification Engineer: "Even sub-blocks a tenth this size are very difficult to formally verify with traditional tools."
  - A second project generated RTL from the specification, with 37 properties proved, about 26% less power and 19% less cell area.
- LibTomMath (C) [COMPANY CLAIM]. https://harmonic.fun/aristotle/case-studies/libtommath/
  - Three bugs found and repaired. Modular exponentiation 31–38% faster, with the optimised routines proved against the same specifications.
  - Limit: "Full modular exponentiation is benchmarked, not proved". The page does not say the changes were merged upstream.
- 3 Nov 2026: the multiply and divide unit of the Ibex RISC-V core was verified against the Sail RISC-V model, with nine properties proved [COMPANY CLAIM]. https://harmonic.fun/news/ibex-mul-div-verification
  - Aristotle was driven by a coding agent (Claude Code or Codex) over MCP.
  - Aristotle compiles SystemVerilog and SVA into Lean 4 against "a hand-built model of digital circuits".
- Reuters, 27 Oct 2026, via Investing.com [SECONDARY]. https://www.investing.com/news/economy-news/robinhood-ceos-ai-startup-harmonic-expands-into-software-chip-design-verification-4976694
  - Aristotle is "available with usage-based pricing".
  - DIII-D rebuilt part of its reactor-control software in four hours from one paper and a 254-word prompt.
  - Researchers recently used the technology to find critical bugs in PHP (not verified further).
  - Cross-reference (ai_native_chip_verification_open_source.md): Reuters named no chip-design customer. https://1027wbow.com/2026/10/27/robinhood-ceos-ai-startup-harmonic-expands-into-software-chip-design-verification/
- EconoTimes, syndicating Reuters, 27 Oct 2026 [SECONDARY]. https://econotimes.com/Harmonic-Adds-Formal-Checks-for-C-Software-and-Verilog-Hardware-1764657
  - Authors affiliated with General Atomics' DIII-D facility say Aristotle examined the Verilog in a Thomson-scattering diagnostic and found multiple rare errors.
  - Aristotle recreated the C code and its Verilog counterpart from a paper and a 254-word prompt in four hours.
  - The source is an abstract for the IAEA AI for Fusion workshop, with C. Mitchell Clark presenting on 9 Nov 2026.

**(ii) Funding and traction**
- Harmonic:
  - Series C, 25 Nov 2025: $120M at $1.45B post-money, led by Ribbit, with Sequoia, Index, Kleiner Perkins and Emerson Collective [PRIMARY]. https://harmonic.fun/news/series-c
  - NVentures joined, reported Jan 2026; total raised about $295M [SECONDARY]. https://siliconangle.com/2026/01/15/nvidias-nventures-backs-harmonic-ai-series-c-mathematical-superintelligence/
  - The 2026 news index lists no funding round and no named enterprise or government contract [PRIMARY]. https://harmonic.fun/news
- Axiom:
  - $200M Series A at $1.6B+ post-money, announced 12 Mar 2026, led by Menlo Ventures. Co-investors per the first pass: Madrona, Greycroft, B Capital, Toyota Ventures, Triatomic. Legal name Axiom Quant Inc. [SECONDARY]. https://siliconangle.com/2026/03/12/verifiable-ai-startup-axiom-raises-200m-prove-ai-generated-code-safe-use/
  - My re-read of that article showed no co-investors, so the list is kept but not re-confirmed. The re-read did give Carina Hong as CEO and founder (Stanford PhD student, MIT graduate), Ken Ono as "founding mathematician", Shubho Sengupta as CTO (ex-FAIR director) and François Charton. It also carries a claim of verifying an unnamed 20-year-old number-theory conjecture.
  - Seed: $64M in Oct 2025. CONFLICT: Madrona says "Madrona led the seed round"; Sacra says B Capital led, with Greycroft, Madrona and Menlo. https://www.madrona.com/axiom-math-carina-hong-ai-code-verification/ ; https://sacra.com/c/axiom-math
  - Sacra also reports a $1.50B valuation in a round of "more than $100 million" in Feb 2026, which conflicts with the announced March figures; I use the March figures. Its other points:
    - Mid-2025 reports had Axiom seeking $50M at $300–500M.
    - "despite generating no revenue".
    - Model: "annual core engine licenses combined with usage-based compute credits" (Sacra's description, not a company price list).
    - Target segments: quantitative finance, research institutions, industrial mathematics [SECONDARY].
  - Menlo, 12 Mar 2026: operating since July 2025; "over 30 employees". The round will fund bringing "initial products to market". It sizes the traditional formal-verification market at "low single-digit billions" [PRIMARY investor post; investor claim]. https://menlovc.com/perspective/ai-will-write-all-the-code-mathematics-will-prove-it-works/
  - Madrona, 12 Mar 2026: the money is to deliver "scalable verification solutions" by carrying the rigour of formal mathematical proof into code verification in Lean. It mentions the perfect Putnam score "in December" and says the skill carries over to code-verification benchmarks. No product, timing or customers named [PRIMARY investor post].
  - Fortune, 1 Jun 2026 (Nick Lichtenberg): about 40 people; customers in finance, cybersecurity and software and hardware development (unnamed, from the company); revenue not disclosed; EconLib with Scott Kominers (HBS) [SECONDARY]. https://fortune.com/2026/06/01/axiom-math-econlib-antitrust-economic-theory-verified/
  - AXLE (Axiom Lean Engine) released 5 Mar 2026 as "a free service" [PRIMARY]. https://axiommath.ai/research/releasing-axle
  - Homepage, read 12 Nov 2026 [PRIMARY]. https://axiommath.ai/
    - No product, API, pricing or customer listed. Navigation covers Mission, Research, Formalizations (Bounded Gaps, CFSG, Stacks Project), Engineering, Press, Careers.
    - Nov 2026 blog posts: Weil conjectures, cluster algebras, Stacks Project.
    - Oct 2026 publications: "An Asymptotic Jensen–Pólya Criterion for GRH", "The Unbalanced Group Theorem", "Explicit Positive Lower Density for the Collatz Conjecture".

**(iii) What "Axiom" refers to, and its 2026 results**
- Axiom Math's 2026 results, all company-reported:
  - Classification of Finite Simple Groups (post dated 26 Oct 2026): 43.1M lines of Lean in 24 days by "dozens" of agents using a "changing mix of models"; 34 noteworthy deviations from the published proof; Lyons and Solomon consulted [PRIMARY; COMPANY CLAIM]. https://axiommath.ai/research/the-enormous-theorem-formalized/
  - Stacks Project (4 Nov 2026): about 16M lines of Lean for the ~7,500-page work [COMPANY CLAIM]; see section 6.
  - IMO 2026: "solved all six problems, achieving a perfect score of 42/42", taking 24 to 869 minutes per problem. No official grading is claimed [COMPANY CLAIM]. https://github.com/AxiomMath/IMO2026
  - Erdős problems wiki: five AxiomProver entries as of 19 Jun 2026 [INDEPENDENT]; see section 3.
- Naming hazard: axiom.xyz is a different company, operated by Intrinsic Technologies [PRIMARY]. https://www.axiom.xyz/
  - It makes OpenVM, a zero-knowledge virtual machine, and an Axiom Proving API; OpenVM 2.0 went into production on 10 Jul 2026.
  - Its RV32IM extension was formally verified in Lean by Nethermind Research with an Ethereum Foundation grant (10 Feb 2026), and its Keccak and SHA-2 circuits were verified in Lean (19 Aug 2026).
  - "Axiom's AI auditor found a soundness vulnerability in Starknet's stwo proof system" (27 Jul 2026).
- Other names that clash: Axiomise, a UK chip formal-verification firm (cross-reference: europe_israel_specialists.md), and Axiomatic AI (see section 1).

### Inferences
- Harmonic's launch is real and documented. The product proves only the properties that are written down, and the most concrete outside evidence of use comes from a fusion laboratory and a customer quote in a company case study. It is not yet evidence of a paying base.
- Axiom has the capital and the mathematics results but, on its own pages, no shipped software-verification product as of 12 Nov 2026.

### Gaps
- Whether Tensordyne or DIII-D pays Harmonic; Harmonic's credit prices; whether the PHP bugs were confirmed.
- Axiom's actual revenue, its named customers, and when a code product will launch.

## 3. In-depth assessments: Harmonic, Axiom, Galois, Runtime Verification, Imandra, Code Metal

### Takeaway
Harmonic is the only independent North American company with a shipped, usage-priced proof product on real C and hardware code and an outside user. That makes it the strongest candidate for a place among the 8 to 15 that matter globally. Axiom and Galois are borderline: Axiom on capital and mathematical capability, Galois as the incumbent government formal-methods house. Runtime Verification, Imandra and Code Metal are niche or unproven as sellers of machine-checked proof. All verdicts below are my provisional judgments.

### Cited Findings and provisional assessments

#### Harmonic
- **a. Position.**
  - The verdict comes from the open-source Lean 4 kernel, which Harmonic does not own. Harmonic does fund its steward ($300,000, Feb 2026) [PRIMARY]. https://harmonic.fun/news/lean-fro-donation/
  - What Harmonic owns is the translation layer: it compiles SystemVerilog and SVA into Lean against "a hand-built model of digital circuits". It also owns the workflow in which Aristotle proposes properties and engineers commit them [COMPANY CLAIM]. https://harmonic.fun/news/ibex-mul-div-verification
  - Provisional judgment: Harmonic owns part of the judge, namely the trusted semantic models and the property workflow, but not the checker. Proof search alone is the part most exposed to general models.
- **b. Lead.**
  - Tao-hosted Erdős problems wiki, frozen 30 Jun 2026: Aristotle appears in about 20 full-solution entries and more than 100 formalisation entries, against five for AxiomProver, one for Gauss and three for Aleph. The page warns "This page is not a benchmark" [INDEPENDENT]. https://github.com/teorth/erdosproblems/wiki/AI-contributions-to-Erd%C5%91s-problems
  - VERINA, 3 Dec 2025: 160 of 189 proved and 23 disproved, 96.8%, run on the public API, with no outside replication stated [COMPANY CLAIM]. https://harmonic.fun/news/verina-benchmark/
  - A competitor reports Aristotle at 69% on VeriSoftBench, against Aleph's 94% [COMPANY CLAIM, competitor].
  - Users: Tensordyne (quoted customer) and DIII-D (outside authors) [COMPANY CLAIM / SECONDARY]. No revenue disclosed.
- **c. Revenue model.** Usage credits, "no seats or licenses", plus enterprise volume plans. This is the purest usage model in the group, and revenue scales with use. No figures disclosed [COMPANY CLAIM].
- **d. Financial strength.** About $295M raised; last valued at $1.45B in Nov 2025; investors Ribbit (lead), Sequoia, Index, Kleiner Perkins, Emerson Collective, NVentures, Paradigm, ERA, Blossom, DST Global [PRIMARY/SECONDARY]. Burn rate, runway and customer concentration are not disclosed.
- **e. Resilience (provisional).**
  - Steady growth (about 55%): favourable. More AI-written code raises demand for checks that are paid for by use.
  - Pause around 2028 (about 25%): the venture-dependent valuation is at risk, cushioned by about $295M raised. Chip-verification budgets may hold up better than budgets for software tools.
  - Acceleration (about 20%): demand rises, but proving becomes a commodity. Harmonic's edge then rests on its semantic models, its continuous-integration integration and customer trust.
  - Crypto exposure is low: Paradigm is an investor, but the product is not crypto-specific. Government exposure is small: the DIII-D facility is federally funded.
- **Path forward.**
  - (1) Already a tool, with no services arm seen.
  - (2) Already usage-priced.
  - (4) The engine is proprietary on top of open Lean. Harmonic open-sources peripheral tools only (python-memtools, pbcc).
  - (6) Buyers so far: chip designers, C library maintainers, a fusion lab.
  - (7) Harmonic positions Aristotle as a tool that coding agents call over MCP.
- **Said versus done.** Said: "mathematical superintelligence". Done: shipped C and SystemVerilog verification with documentation, an SDK and MCP, published case studies, and funded the checker.
- **What must go right.** Credit revenue must grow faster than the gap to general models narrows, and customers must accept Harmonic's semantic models as trustworthy.
- **Verdict (provisional): coherent.** The proviso is that there is no evidence yet of paid volume.

#### Axiom Math
- **a. Position.** The verdict comes from the Lean kernel. Axiom's distinctive assets are very large open formalisations (CFSG, Stacks Project, Weil conjectures), which others could come to depend on, and a free Lean engine. Its proof runs used a "changing mix of models" [COMPANY CLAIM]. Provisional judgment: this is mainly a gap-filler that rides on frontier models, plus a corpus that is a public good.
- **b. Lead.** Formalisation scale is unmatched among companies but rests on company claims checked only by the Lean kernel. I found no independent audit (section 6). The Putnam and IMO 2026 perfect scores are company claims. It has five entries on the Erdős wiki, and no named customers.
- **c. Revenue model.** None disclosed. Sacra reports no revenue and describes a licence-plus-credits model; AXLE is free [SECONDARY/PRIMARY].
- **d. Financial strength.** About $264M raised ($64M seed plus $200M Series A); $1.6B+ valuation; about 40 staff in June 2026. That implies a long runway, though burn is not disclosed (my inference).
- **e. Resilience (provisional).**
  - Steady growth: adequate.
  - Pause: weakest of the six. It has no revenue and a high valuation, but a large cash cushion.
  - Acceleration: most exposed, if labs verify code directly (section 5).
  - No crypto or government dependence seen.
- **Path forward.**
  - (1) Not applicable.
  - (2) Intended licence plus usage, per Sacra only.
  - (4) Open corpora and a free engine, so in effect an open-core approach.
  - (6) Buyer not public.
  - (7) High exposure.
- **Said versus done.** Said: prove that AI-generated code is safe. Done: record-scale mathematics formalisations and a free engine. No code product appears on its site.
- **Verdict (provisional): partly coherent.** The capital and capability are clear; the software commercial path is not yet shown.

#### Galois
- **a. Position.**
  - Galois is an integrator that owns widely used open-source verification tools: SAW, Cryptol, Crux, GREASE, C2Rust, CAMET, Swanky [PRIMARY]. https://www.galois.com/articles/2025-year-in-review ; https://www.galois.com/
  - Its scarce asset is trusted sign-off for the US government. It fills gaps that general models will not close for cleared, sector-specific work (provisional).
- **b. Lead.**
  - DARPA COOP award [SECONDARY]. https://www.militaryaerospace.com/trusted-computing/article/55238957/trusted-computing-design-and-development-tools
    - $12.6M, reported 30 Oct 2024: formal methods plus side-channel analysis ("HEIMDALLR"), due to finish by Apr 2026.
    - The award notice is HR001125C0300: $12.6M obligated against a $52.8M ceiling [SECONDARY/aggregated federal data]. https://www.highergov.com/contract/HR001125C0300/
    - CORRECTION/CONFLICT on the end date. The first pass recorded a period of 16 Oct 2024 to 11 Jun 2026. A later extract of the same page says it ends 16 Apr 2026, "shortened from 10/16/27 to 04/16/26". Either way the award was cut short of its original Oct 2027 end; the reason is unknown [UNVERIFIED].
  - SBIR Phase II "MAPACHE": $1,432,311, 29 Oct 2025 to 30 Oct 2026; scope not confirmed [SECONDARY]. https://www.inknowvation.com/sbir/awards/darpa-2026-mapache
  - Polymorph tools are "actively being transitioned to program offices across the DoD" [COMPANY CLAIM].
  - Galois built Galwagent ("LLM-based, multi-agent framework") under GAI4RDE. Its staff post on Claude Code, including Mike Dodds' "Claude Can (Sometimes) Prove It" and "Specifications Don't Exist" [PRIMARY].
  - It is a Signal Shot collaborator [PRIMARY]. Hack VC names Galois as one of the procurement vehicles for Math Inc. [investor claim].
  - Customer logos: NIST, DARPA, NASA, DoD, Army, Navy, Air Force, AFRL, IARPA, ARPA-H. Amazon Web Services is the only commercial logo; "Metron: AI Benchmarking for Advanced Formal Verification" is listed as a project [COMPANY CLAIM]. https://www.galois.com/
- **c. Revenue model.** Labour on government research contracts, with tools given away as open source. The AI-plus-formal-methods page lists sectors (aerospace and defence, automotive, fintech, healthcare, semiconductors) but no commercial prices [COMPANY CLAIM]. https://www.galois.com/ai-formal-methods
- **d. Financial strength.** Private. Revenue and headcount are not disclosed; it has operated "for more than 25 years" from offices in Portland, Arlington, Minneapolis and Dayton. No venture rounds were found. Customer concentration in federal agencies looks high (my inference from the logos).
- **e. Resilience (provisional).** Little exposure to venture conditions, so it is the most robust of the six in a 2028 financing pause. It is exposed to federal research budgets; note the shortened COOP award. In an acceleration, its labour becomes more productive but also more of a commodity.
- **Path forward.**
  - (1) Partial: Galwagent and Metron, but its tools are open source.
  - (4) Open by design.
  - (6) The government is its buyer.
  - (7) It uses lab models as complements.
- **Verdict (provisional): partly coherent.** It has a durable niche but no sign of turning into a tool business that scales with use.

#### Runtime Verification (RV)
- **a. Position.**
  - RV owns the K Framework, with executable semantics such as KEVM. Formal language semantics are close to a judge for its niche.
  - Products: Kontrol, Simbolik, Komet, KMIR, plus "Lean4 Proofs" [COMPANY CLAIM]. https://www.runtimeverification.com/about
- **b. Lead.** Company claims: "100+ security engagements" and "25+ senior engineers".
  - 2026 Linux work [COMPANY CLAIM]. https://www.runtimeverification.com/blog
    - Binder deserialiser proved never to panic, in Lean 4 (5 Aug).
    - Linux UVC parser: safe-Rust rewrite with Lean proofs tied to CVE-2024-53104, leading to an upstream integer-overflow fix (20 Aug).
    - io_uring sandbox filter bypass, fixed in mainline "within a day" (21 Oct).
    - KEQ semantic-equivalence proofs (6 Nov).
  - Other 2026 work: a Dafny model of Optimism's Supernode built in a 10-week audit extension (20 Oct); AI-assisted fuzzing of WAMR found a real bug "but also flagged valid behavior" (11 Sep).
  - Partnership with Assurea for medical devices and artificial organs (18 Aug).
  - The site names no customers.
- **c. Revenue model.** Labour: audits, formal verification, fuzzing, design review, formal modelling. No pricing.
- **d. Financial strength.**
  - Leadership: CEO Everett Hildenbrandt, COO Paul Len, CTO Palina Tolmach; founder Grigore Rosu (UIUC, 2010). Funding not disclosed.
  - Related company: Pi Squared (zero-knowledge proofs plus formal verification; founded 2023; Champaign, IL; Rosu as CEO) [SECONDARY/aggregator]. https://www.cbinsights.com/compare/pi-squared-vs-runtime-verification
- **e. Resilience (provisional).**
  - Crypto exposure has been high. RV posts on the KelpDAO bridge loss of 18 Apr 2026 ($292M drained even though the audited components "worked as specified"; posts of 5 May and 3 Jun) [COMPANY CLAIM].
  - Its shift to Linux and medical devices reduces that exposure.
  - A labour model rides out a financing pause if clients keep paying.
- **Path forward.**
  - (1) Partial: AI writes proofs (it used Claude Code on Linux namespaces), but RV sells engagements.
  - (4) K is open source.
  - (6) Buyers: blockchain foundations, and now medical-device makers.
  - (7) RV explicitly moves its value to specifications (section 6).
- **Verdict (provisional): partly coherent.** The thesis is clear, but the business is small and bound to labour.

#### Imandra
- **a. Position.** It runs ImandraX, a proprietary reasoning engine, and CodeLogician, which turns code into formal models (launched 26 Mar 2025, select partners, then a waitlist) [PRIMARY company release]. https://www.imandra.ai/articles/imandra-releases-codelogician . In trading-venue certification, Imandra's models can serve as a judge-like reference within a niche (provisional).
- **b. Lead.**
  - Customers and partners named on the homepage: Goldman Sachs, KPMG, Citi, OneChronos, Euronext, TMX, Broadridge, DARPA, US Navy, SRI [COMPANY CLAIM]. https://www.imandra.ai/
    - 30 Jun 2026: BLOX Markets selected Imandra for onboarding and certification on its Openpool US equities venue. The aggregator Simplify reported the same; still company-sourced [COMPANY CLAIM]. https://simplify.jobs/c/Imandra
    - 18 Aug 2026: an automated-reasoning framework for capital markets went on the Microsoft Azure Marketplace.
  - A Silicon Hills News article named Goldman Sachs as a customer (undated) [SECONDARY].
  - arXiv 2601.11840 (Jan 2026) reports a 41–47 percentage-point gain in accuracy from formal augmentation; it is self-reported and was not re-read [PRIMARY paper]. https://arxiv.org/abs/2601.11840v2
- **c. Revenue model.** Seats: Builder $25 a month, Pro $129 a month, Team $799 a month; enterprise unpriced; marketed as "Reasoning as a Service" [COMPANY CLAIM].
- **d. Financial strength.** $5M seed (AlbionVC, IQ Capital, LiveOak), dated Apr 2019 by c.parsers.vc. Totals conflict: $19.2M per Simplify against $9.0M per VCBacked (last round Apr 2024) [UNVERIFIED]. Small.
- **e. Resilience (provisional).** Tied to finance-sector IT budgets and only modestly to venture conditions. In an acceleration it gains as a tool that coding agents call; it has published demos with OpenAI Codex, Gemini/Antigravity and Cursor.
- **Path forward.**
  - (1) Already a tool.
  - (2) Seats today.
  - (4) A proprietary engine facing open Lean tools.
  - (6) Buyers: trading venues and banks, the clearest certification buyer in the set.
  - (7) A complement to lab models.
- **Verdict (provisional): partly coherent.** It has a real niche buyer but no evidence of scale.

#### Code Metal
- **a. Position.** It sells code translation for defence and edge hardware and says it is "mathematically proving code is correct" with a "neuro-symbolic approach". The verification method is not specified in any source found [SECONDARY]. https://pulse2.com/code-metal-125-million-series-b-raised-for-verifiable-code-translation-platform . Provisional judgment: not evidently a seller of machine-checked proof.
- **b. Lead.**
  - Site logos: Toshiba, U.S. Air Force, Raytheon, NVIDIA, L3Harris, Collins, Bosch, Boeing. The site claims an $80M OTA (Other Transaction Authority agreement, a flexible contracting route) for WarMatrix, dated 14 Aug 2026 [COMPANY CLAIM]. https://www.codemetal.ai/
  - Named users: Toshiba, RTX, L3Harris, the US Air Force. The company says it is in "programs of record across the U.S. Air Force, L3Harris" [COMPANY CLAIM]. https://www.eweek.com/news/code-metal-valuation-ai-code-translation/
  - No independent technical evidence was found.
- **c. Revenue model.** Defence contracts and enterprise sales; not disclosed.
- **d. Financial strength.**
  - Series B: $125M led by Salesforce Ventures, announced about 19 Feb 2026, at a $1.25B valuation (per EVP Growth Laura Shen). Accel, B Capital, Smith Point, J2, Shield Capital, Overmatch and RTX also invested.
  - Series A: about $36–36.5M, led by Accel.
  - CEO Peter Morales; HQ Boston; Ryan Aytay (ex-Tableau CEO) is President and COO.
  - Rob Keith (Salesforce Ventures): "mission-critical industries cannot deploy what they cannot verify" [SECONDARY]. Release: https://www.businesswire.com/news/home/20260219267824/en
- **e. Resilience (provisional).** Defence budgets steady it in a pause, but its valuation depends on venture conditions. AI translation is exactly what labs and DARPA's TRACTOR programme target, so it is exposed in an acceleration unless its verification really differentiates it.
- **Path forward.**
  - (4) Proprietary.
  - (6) The defence buyer is real.
  - (7) High exposure.
- **Verdict (provisional): partly coherent as a business; cannot assess as a proof company.**

**Watch list, not assessed in depth:**
- Math Inc.: strong formalisation results, DARPA-funded, an open-source harness, no product.
- Logical Intelligence: the only specialised prover with independent rankings (MathArena), but repositioning and with no customers named.
- Theorem: validated by Anthropic, four staff.
- &Truth: $70M seed, Barrett and Sergey, no product.
- Veridise and CertiK: crypto audit labour.

### Inferences (global ranking)
- Provisional judgment on the 8 to 15 that matter globally in verification and specification:
  - Harmonic: likely belongs.
  - Axiom and Galois: borderline.
  - Runtime Verification, Imandra, Code Metal, Math Inc., Logical Intelligence, Theorem, &Truth: probably not yet.
- The Lean FRO is not a company, but it stewards the judge most of these firms depend on (section 6). The report writer should treat it as infrastructure, not leave it out.
- Across the six, the lasting assets are trusted semantic models (Harmonic's circuit model, RV's K semantics, Theorem's RISC-V and Linux semantics), customer sign-off relationships (Galois with DoD, Imandra with trading venues) and integration into engineering workflows. Proof search is the least durable.

### Gaps
- No revenue, runway or burn figures for any of the six.
- No independent technical audit of Code Metal's verification.
- Galois headcount, and the reason COOP was cut short.

## 4. Is a paying market for verified software forming (transition 6), and who is the buyer?

### Takeaway
A market is forming but is still small and fragmented. Documented money comes mainly from US defence research (DARPA programmes, OTAs, SBIRs) and from crypto protocols' recurring security budgets, mostly spent on audit labour. Regulators have begun to grant credit for machine-checked evidence in avionics. Cloud providers and AI labs act as sponsors and collaborators, not yet as buyers or acquirers of proof start-ups. I found no evidence on insurers and no credible market-revenue figure for AI-native proof.

### Cited Findings
- **Government, defence research:**
  - DARPA PROVERS [PRIMARY]. https://www.darpa.mil/research/programs/pipelined-reasoning-of-verifiers-enabling-robust-systems
    - 42 months in three phases: proof engineering, platform development, a red team, and a federally funded R&D centre for evaluation.
    - Programme manager Xenofon Koutsoukos, Information Processing Techniques Office; solicitation HR001123S0020 (2023).
    - No performers or budget listed. Aim: "make formal methods accessible to non-experts".
    - BAE Systems FAST Labs holds a $6M PROVERS contract (date not given) [SECONDARY]. https://www.executivebiz.com/articles/bae-systems-books-darpa-contract-for-software-modernization
    - Cross-reference (europe_israel_specialists.md): Proofcraft sits in the INSPECTA team, led by Collins Aerospace.
  - DARPA TRACTOR (translating C to Rust):
    - MIT Lincoln Laboratory runs testing and evaluation and issues a benchmark every six months [PRIMARY]. https://www.ll.mit.edu/tractor
    - The ForCLift team (Illinois, UW–Madison, Berkeley, Edinburgh) received $5M for "Verified Lifting", which combines formal methods with large language models (15 Jul 2025) [PRIMARY university release]. https://www.cs.wisc.edu/2025/07/15/translating-legacy-code-for-a-safer-future
    - arXiv 2604.12048 (ORBIT, Apr 2026) cites a TRACTOR battery of 150 C programs, six performers and aggregated results only [PRIMARY paper]. https://arxiv.org/pdf/2604.12048
  - Other routes: COOP and MAPACHE (Galois, section 3); expMath (Math Inc., section 1); Code Metal's $80M OTA claim; Math Inc.'s "Galois/RAND and DARPA OTA vehicles" (investor claim).
- **Government, policy:** guidance rather than mandates.
  - CISA and NSA, "Memory Safe Languages", 24 Jun 2025: recommendations only, with no procurement or regulatory requirement. The page does not mention formal verification [PRIMARY]. https://www.cisa.gov/resources-tools/resources/memory-safe-languages-reducing-vulnerabilities-modern-software-development
  - Cross-reference (europe_israel_specialists.md):
    - EU Cyber Resilience Act guidance: draft 3 Mar 2026, final 27 Jul 2026, non-binding, with no mention of formal verification or memory safety in a law-firm summary. https://www.orrick.com/en/Insights/2026/09/EU-Cyber-Resilience-Act-New-Guidance-Clarifies-Scope-Reporting
    - UK ARIA Safeguarded AI: budget £59M; turned away from building specialised AI systems in Nov 2025; eight cybersecurity projects share £22M. https://www.aria.org.uk/programme-safeguarded-ai
  - Not checked (search budget): ONCD statements in 2026, and the DARPA expMath page (404).
- **Regulated sectors:**
  - Avionics. Cross-reference (europe_israel_specialists.md): in Mar 2026, AbsInt's CompCert compiler was qualified for the ATR 42/72 flight-control computer. It was the first time certification credit was claimed for compiler use under DO-178C/DO-333/DO-330. https://www.absint.com/releases/260320.htm
  - Medical devices: RV's partnership with Assurea (Aug 2026) [COMPANY CLAIM].
  - Capital markets: Imandra and BLOX Markets (Jun 2026) [COMPANY CLAIM].
  - Defence: Code Metal (company claims).
  - No 2026 evidence found for automotive (ISO 26262), rail or nuclear buyers of proof start-ups.
- **Cloud providers:**
  - Amazon made the largest donation in the Lean FRO's history (Jul 2026), and Lean's creator works at AWS [PRIMARY]. https://lean-lang.org/fro/about
  - AWS is Galois's only commercial logo [COMPANY CLAIM].
  - This is sponsorship of the judge, not purchases from start-ups.
- **Crypto and decentralised finance:**
  - Sherlock, "Smart Contract Audit Pricing: A Market Reference for 2026" (dated Feb 2026; page header 31 Oct 2026) [SECONDARY, vendor]. https://sherlock.xyz/post/smart-contract-audit-pricing-a-market-reference-for-2026
    - Audits: $5K to $250K+. ERC-20 tokens $5–20K; DeFi $25–100K; enterprise multi-chain over $150K; re-audits $5–20K per pass.
    - Annual security budget for protocols holding meaningful value: $150–500K. Zero-knowledge circuits cost 80–120% above the EVM baseline.
    - No price for formal verification. Web3 losses in H1 2025: about $3.1B.
  - Cross-reference (europe_israel_specialists.md):
    - Certora AutoProver: free tier ($0, one seat, runs billed); Pro $120 a month; Enterprise from $3,000 a month; runs paid from credits.
    - An Aave DAO proposal (Oct 2025) paid $2.39M for 12 months of continuous security (formal verification, manual audits, fuzzing).
    - https://www.certora.com/blog/ai-formal-verification-smart-contracts-costs-use-cases ; https://www.certora.com/pricing
  - A DEV Community post puts the audit market at "~$500M/year", rising to about $5B a year with AI, without sources [UNVERIFIED]. https://dev.to/ohmygod/how-ai-agents-can-audit-smart-contracts-in-2026-a-technical-deep-dive-5gl
  - Security firms: CertiK revenue range $10–50M per Dealroom [UNVERIFIED]; Veridise and RV as above. axiom.xyz is an example of formal verification bought by Ethereum infrastructure (an Ethereum Foundation grant) [PRIMARY].
- **AI labs as buyers or acquirers:**
  - Anthropic collaborated with Theorem (Oct 2026); no payment was disclosed [PRIMARY].
  - NVentures invested in Harmonic [SECONDARY].
  - No acquisition of a formal-verification start-up by an AI lab in 2025–2026 was found (search on 12 Nov 2026; absence of evidence) [SECONDARY].
- **Chip designers:** Tensordyne (Harmonic) [COMPANY CLAIM]; VerifAIX's seed [SECONDARY].
- **Insurers:** no evidence found. Not searched in depth because the budget ran out.
- **Investor scepticism:** an unnamed AI investor: "I doubt that most AI generated code is going to end up formally verified" (Sep 2025) [SECONDARY].

Pricing models observed:

| Model | Examples (as of 2026) | Source |
|---|---|---|
| Usage or credits, no seats | Harmonic Aristotle (rates unpublished) | https://harmonic.fun/ |
| Seats plus usage credits | Certora AutoProver $0 / $120 / $3,000+ a month plus runs (cross-reference) | https://www.certora.com/blog/ai-formal-verification-smart-contracts-costs-use-cases |
| Seats | Imandra $25 / $129 / $799 a month | https://www.imandra.ai/ |
| Free or open source | Axiom AXLE; Math Inc. OpenGauss; the Lean kernel itself | https://axiommath.ai/research/releasing-axle ; https://www.math.inc/archive |
| Indicative compute cost | Aleph about $66.84 per problem (MathArena) | https://matharena.ai/models/logical_intelligence_aleph_prover |
| Labour, audits | Audits $5K–$250K+; annual budgets $150–500K | https://sherlock.xyz/post/smart-contract-audit-pricing-a-market-reference-for-2026 |
| Retainer | Aave–Certora $2.39M for 12 months (cross-reference) | https://www.certora.com/blog/ai-formal-verification-smart-contracts-costs-use-cases |
| Government contracts | COOP $12.6M obligated; MAPACHE $1.43M; ForCLift $5M; BAE PROVERS $6M | sources above |

### Inferences
- Buyer, ranked by evidence of money (my provisional judgment):
  1. US defence and government research agencies, the only buyer with documented contract values for proof work.
  2. Crypto protocols, with recurring security budgets but mostly for audit labour, so proof is a premium add-on.
  3. Chip designers, an early but natural fit for property proofs.
  4. Regulated industries, where the CompCert avionics credit shows regulators can accept machine-checked evidence, though buyers are tool qualifiers rather than start-up customers.
  5. Cloud providers and AI labs, as sponsors and collaborators.
- Estimate, clearly labelled: I found no credible figure for AI-native proof revenue in 2025–2026. Code Metal is excluded: its proof component is unverified and its contract values are undisclosed apart from the $80M OTA claim. For the rest, the evidence is consistent with little recurring revenue: Axiom reportedly has none, Harmonic's paid software and hardware product launched on 27 Oct 2026, Theorem is in beta, and &Truth has no customers. The investor figure of "low single-digit billions" refers to traditional formal verification, much of it chip-design tools covered by other researchers. It does not measure this segment.

### Gaps
- Insurers; ONCD in 2026; automotive, rail and nuclear buyers.
- What price is charged for formal verification within smart-contract audits.
- Whether any DARPA PROVERS or TRACTOR performer is one of the start-ups named here.

## 5. Transition 7: are general models from AI labs making independent proof start-ups redundant?

### Takeaway
Not yet, but the gap is narrowing. In Oct–Nov 2026 two labs verified real software at scale themselves. Anthropic did so with a four-person start-up supplying the semantic models; DeepMind's AlphaProof Code did it unaided. A paper shows a simple agent loop on frontier models matching specialised proving workflows. The start-ups have responded by becoming tools that lab agents call, giving away engines and harnesses, and moving their value towards semantics and specifications.

### Cited Findings
- arXiv 2610.35962 ("h1", 25 Oct 2026): a simple agent loop matches or beats specialised workflows when the same models are used [PRIMARY paper]. https://arxiv.org/abs/2610.35962
- Anthropic Frontier Red Team with Theorem, 22 Oct 2026 [PRIMARY]. https://www.anthropic.com/research/formal-verification
  - Claude proved properties of compiled RISC-V binaries: 239 OSS-Fuzz entry points in 123 libraries, with no crash for inputs up to 64 MB. It used Rocq, and Verus for a Rust Python interpreter.
  - Scale: about 180M lines of Rocq in "a few weeks", with a typical proof of about 600,000 lines. Proofs "can take hundreds of millions of tokens". "Opus 5.5 proves half of them with about 40% fewer tokens than Opus 5". Shared workspaces cut tokens by 17%.
  - It found "hundreds of bugs", including a rediscovered CVE-2026-56132 in libexpat.
  - Theorem supplied the semantics, publishes a subset of the proofs, offers to run the pipeline for open-source projects, and has published a Claude skill.
  - "'Formally verified' does not mean 'bug-free.'"
- Cross-reference (model_makers_hyperscalers.md):
  - DeepMind's AlphaProof Code (10 Nov 2026) used agents "powered by Gemini Carbon". It generated "about 6.5 million lines of machine-checked Lean proof code, resting on about 26,000 lines of trusted specifications and AArch64 semantics" for libsignal.
  - https://deepmind.google/documents/36/Formal_Verification_of_Signal_4.pdf ; https://deepmind.google/blog/introducing-alphaproof-code/
- Start-ups' responses:
  - Harmonic drives Aristotle from Claude Code or Codex over MCP [COMPANY CLAIM].
  - Axiom used a "changing mix of models" [COMPANY CLAIM].
  - Imandra demonstrates its tools with Codex, Gemini and Cursor; RV builds proofs with Claude Code; Galois staff wrote "Claude Can (Sometimes) Prove It" [COMPANY CLAIM/PRIMARY].
  - Math Inc. open-sourced OpenGauss; Axiom made AXLE free [PRIMARY].
- Lean FRO: "AI-generated proofs are becoming a major source of grind and bv_decide usage". Its Tau Ceti project uses AI reviewers to judge pull requests against open rubrics [PRIMARY]. https://lean-lang.org/fro/roadmap/y4-1
- Independent ranking: the specialised AlephProver ranked first on MathArena's ArXivLean in Mar and Jun 2026 [INDEPENDENT]. Later rounds exist (LeanLean 10/2026, ArXivLean 09/2026), but the tables load by script and were not read. MathArena runs each model four times per problem and reports average score and cost per run [PRIMARY]. https://matharena.ai/
- Sep 2025 press: "some experts doubt formal math approaches will be widely needed as labs build better reasoning models" [SECONDARY]. https://www.upstartsmedia.com/p/math-ai-startups-push-new-models

### Inferences
- Proof search is becoming a commodity that labs can supply. What labs bought from a start-up in the Anthropic case was trusted semantics.
- Start-ups that own semantic models, customer workflows or sign-off are less exposed than those selling prover accuracy alone.
- No lab acquisition was found, so labs currently partner with start-ups or build their own rather than buy them.

### Gaps
- Head-to-head results in Oct–Nov 2026 between general models and Aristotle or AxiomProver on software benchmarks.
- Whether labs will price verification as a product.

## 6. From proofs to specifications: who writes the specifications, how they are reviewed, and how good AI-written ones are

### Takeaway
In every engagement found, AI writes most proofs. Specifications are drafted by AI or by the vendor's engineers and approved by the customer's engineers or maintainers. Two cases need little review, because the property is generic ("does not crash") or because the vendor's semantic model of the hardware or operating system is trusted. AI-written specifications are often wrong in quiet ways. Separately, the open-source judge itself had a soundness bug in July 2026.

### Cited Findings
- Harmonic: Aristotle proposes properties and engineers review and commit them. At Tensordyne, 100 of the 241 properties were written by Aristotle from 312 pages of specifications. "Behaviors not listed as properties are not verified" [COMPANY CLAIM].
- Runtime Verification, "The proof is in the spec", 30 Sep 2026 [COMPANY CLAIM]. https://www.runtimeverification.com/blog/the-proof-is-in-the-spec
  - Process: RV drafts a plain-English specification "written for the maintainer, not for a prover", and "The maintainer reviews it and tells us where we're wrong". RV checks proofs for vacuity.
  - Risk: autoformalisation "makes the model and specification much cheaper to produce, and makes them much easier to skip reviewing".
  - Examples: a formaliser "quietly made x a natural number"; a TLA+ specification of Etcd's Raft "passed every check and had little to do with Etcd", scoring "near 100% on syntax but around 46% on conformance to the actual code".
  - "Let AI write the proofs. Don't let it decide, unchecked, what they prove." The work between an agreed specification and full correctness "is engineering, and it's where most of the value is."
- RV on Linux user namespaces, 2 Oct 2026 [COMPANY CLAIM]. https://www.runtimeverification.com/blog/verifying-the-linux-kernel-isolation-code
  - Scope: a Rust reimplementation of `kernel/user_namespace.c`, translated to Lean 4 via Charon and Aeneas. 89 theorems are proved and seven lemmas remain open. The lock-free publication protocol was not verified.
  - Claude Code wrote most of the theorems but was wrong four times on the specification or the reasoning (e.g. large literals wrap modulo 2^64, they do not saturate).
  - Bug: `4294967296 1000 1` installs `0 1000 1`. A two-patch fix (kstrtou32) is under review on the kernel mailing list and not yet merged.
- Anthropic: specifications were generated automatically from fuzz tests, so "virtually none of it needs to be manually reviewed". Trust moves to the RISC-V and Linux models, the theorem statements and the Rocq checker. Claude wrote the zlib specification from RFC 1950 [PRIMARY].
- DeepMind (cross-reference): 26,000 lines of trusted specification and semantics under 6.5M lines of proof.
- Lean FRO, on its Hex project: "we write the specifications, and AI agents implement both the executable code and the formal proofs" [PRIMARY].
- &Truth is building a "specification factory" from business requirements [COMPANY CLAIM].
- Math Inc. published FormalQualBench to measure faithfulness [COMPANY CLAIM].
- Galois [COMPANY CLAIM]:
  - Example work includes "automated specification generation from documentation, policies, and vulnerability reports".
  - On AI proofs: "we don't have to trust AI-generated proofs: they can be automatically and independently checked".
  - Mike Dodds' post is titled "Specifications Don't Exist".
- Axiom, Stacks Project, 4 Nov 2026 [COMPANY CLAIM]. https://axiommath.ai/research/the-stacks-project-formalized/
  - Faithfulness "enforced automatically at scale through multi-agent auditing, semantic cross-checks against the source text", plus "targeted audits on foundational definitions and landmark theorems"; the auditors are not named.
  - Stacks Project founder Johan de Jong asked (21 Oct 2026) that AI-generated pull requests not go upstream "for the time being".
  - A lead note described a "StacksCore/StacksFrontier" split; it was not found in this reading [UNVERIFIED].
- Certora (cross-reference, 10 Nov 2026): admits AI-written specifications may omit requirements and that experts must review solvency properties. https://www.certora.com/blog/ai-formal-verification-smart-contracts-costs-use-cases
- Trust in the checker:
  - Lean kernel issue #14576 (28 Jul 2026): "Kernel accepts wrong-structure projections, allowing an axiom-free proof of False". A human found it while reviewing a Collatz proof; it was fixed the same day (PR #14577), with a further commit on 3 Aug. The issue page does not mention AI [PRIMARY]. https://github.com/leanprover/lean4/issues/14576
  - Thomas Hales, guest post on Terence Tao's blog, 9 Oct 2026 [PRIMARY, expert opinion]. https://terrytao.wordpress.com/2026/10/09/what-mathematicians-should-know-about-the-lean-theorem-proverquestions-of-reliability-and-ai/
    - "The summer bugs were detected by frontier model AI in the hands of security researchers".
    - About 25 alternative kernels exist, but "Cross-checking the proof by different kernels does not remove all doubt".
    - "a proof in Lean should not be accepted until a human audit is performed to ensure statement fidelity", which "is generally massively easier than checking the proof itself".
    - There is no complete public consistency proof of Lean's type theory "as of October, 2026".
  - The Lean FRO's response: `lake check <kernel>` and `--paranoid`, Comparator in the distribution, con-leche, and the Kernel Arena [PRIMARY].

### Inferences
- The scarce, billable work is threefold: drafting specifications that maintainers will sign; maintaining trusted semantic models (instruction sets, operating systems, circuits); and auditing statement fidelity. Proof generation is not.
- The verdict mechanism is now a public good, maintained by a donor-funded non-profit. Whoever owns the reviewed specification and the customer's sign-off owns the commercially valuable verdict.

### Gaps
- No priced "specification" product exists yet.
- No independent measure of how faithful specifications are in commercial engagements.

## 7. Exposure (kept separate from quality evidence; not investment advice)

### Takeaway
All the companies are private. Listed investors give only indirect, negligible exposure: Nvidia (via NVentures, in Harmonic), Toyota (via Toyota Ventures, in Axiom, if the first pass's investor list is right), and Salesforce (via Salesforce Ventures) and RTX (in Code Metal). Secondary-market price evidence exists only as Caplight profiles for CertiK and a possibly mismatched "Math, Inc."; for everything else I cannot assess.

### Cited Findings
- Harmonic:
  - Last round: $1.45B post-money, Series C, Nov 2025, led by Ribbit. Other investors: Sequoia, Index, Kleiner Perkins, Emerson Collective, NVentures (Nvidia), Paradigm, ERA, Blossom, DST Global.
  - Sources: https://harmonic.fun/news/series-c ; https://siliconangle.com/2026/01/15/nvidias-nventures-backs-harmonic-ai-series-c-mathematical-superintelligence/
  - Secondary market: cannot assess.
- Axiom:
  - Last round: $1.6B+, Series A, Mar 2026, led by Menlo. Toyota Ventures appears in the first pass's co-investor list.
  - Sacra's conflicting $1.50B figure. https://sacra.com/c/axiom-math
  - Secondary market: cannot assess.
- Code Metal:
  - Last round: $1.25B, Series B, Feb 2026, led by Salesforce Ventures; RTX also invested. https://www.eweek.com/news/code-metal-valuation-ai-code-translation/
  - Secondary market: cannot assess.
- CertiK:
  - Valued at about $2B on its 2022 round. Caplight estimates $2.0B and says there are no public IPO plans [SECONDARY]. https://www.caplight.com/company/certik
  - A headline says it plans a listing "following Binance investment"; I saw the headline only [UNVERIFIED]. https://ground.news/article/certik-outlines-plan-to-pursue-public-listing-following-binance-investment
- No price evidence; cannot assess:
  - Math Inc.: Hack VC invested; Caplight "Math, Inc." profile possibly mismatched.
  - Logical Intelligence: undisclosed; Pebblebed per CB Insights.
  - &Truth: $70M seed, investors undisclosed.
  - Pramaana: $27M seed, Khosla.
  - Theorem: $6M seed, Khosla and YC.
  - Veridise: $4.7M seed, Polychain and Hack VC.
  - Imandra: AlbionVC, IQ Capital, LiveOak.
  - Runtime Verification and Galois: no rounds found; ownership not verified.

### Inferences
- Exposure to this group is, in practice, through venture funds (Ribbit, Sequoia, Menlo, Khosla and others) or a future listing. CertiK's IPO talk in Jan 2026 is the only listing signal, and it was walked back in Feb 2026.

### Gaps
- Secondary-market prices for Harmonic, Axiom and Code Metal; whether employee tender offers have taken place.

## 8. Closing lists

### What could not be verified
- Payment status of Tensordyne and DIII-D; Harmonic's credit rates; the PHP bugs.
- Axiom's revenue, customers and code product; its seed lead (Madrona or B Capital); the co-investors in its Series A.
- Logical Intelligence's funding, its PutnamBench 672/672 and 76% figures, and its "Verina independently confirmed" claim.
- Math Inc.'s round sizes; Morph Labs' 2026 status.
- Code Metal's verification method and its $80M OTA.
- The end date of Galois's COOP award and the reason it was shortened; MAPACHE's scope.
- Imandra's total funding; Veridise's headquarters; CertiK's revenue and the Binance investment.
- Axiomatic AI and Midas rounds (no URL); the Stacks Project split described in the lead notes.
- Insurers; ONCD in 2026; DARPA expMath details; any Asian software-proof start-ups.

### Where current evidence contradicts the background views
- **"Machine-checked proof has become cheap"** holds only relative to human effort (&Truth: under $500 against about five engineer-months). In absolute terms, proofs remain costly and incomplete:
  - "hundreds of millions of tokens" per proof (Anthropic);
  - $66.84 per problem (Aleph on MathArena);
  - seven open lemmas and an unverified lock-free protocol (RV);
  - "Full modular exponentiation is benchmarked, not proved" (Harmonic).
- **"The trusted sign-off is scarce"** is supported, but sign-off covers the checker itself (Lean kernel bug, Jul 2026; Hales) and the semantic models, not only the specification.
- **"The specification is scarce"** is weakened for generic safety properties: Anthropic derived its specifications automatically from fuzz tests, so "virtually none" needed review. The view holds for functional correctness.
- **"Value moves from writing proofs to writing specifications"** is supported in what firms say (RV, Lean FRO's Hex, &Truth). But no one yet sells or prices specifications; value appears to go to whoever owns the customer's sign-off and the trusted models.

### Sources with dates
- Harmonic, from harmonic.fun unless noted:
  - 25 Nov 2025: Series C, https://harmonic.fun/news/series-c
  - 3 Dec 2025: VERINA, https://harmonic.fun/news/verina-benchmark/
  - 11 Feb 2026: Lean FRO donation, https://harmonic.fun/news/lean-fro-donation/
  - 27 Oct 2026: C and Verilog announcement, https://harmonic.fun/news/aristotle-software-hardware-verification
  - 3 Nov 2026: Ibex, https://harmonic.fun/news/ibex-mul-div-verification
  - Read 12 Nov 2026: https://harmonic.fun/news ; https://harmonic.fun/ ; https://aristotle.harmonic.fun/docs/overview ; https://harmonic.fun/aristotle/case-studies/tensordyne/ ; https://harmonic.fun/aristotle/case-studies/libtommath/
- Harmonic coverage:
  - 15 Jan 2026: SiliconANGLE, https://siliconangle.com/2026/01/15/nvidias-nventures-backs-harmonic-ai-series-c-mathematical-superintelligence/
  - 27 Oct 2026: Reuters via Investing.com, https://www.investing.com/news/economy-news/robinhood-ceos-ai-startup-harmonic-expands-into-software-chip-design-verification-4976694 ; EconoTimes, https://econotimes.com/Harmonic-Adds-Formal-Checks-for-C-Software-and-Verilog-Hardware-1764657 ; WBOW (Reuters), https://1027wbow.com/2026/10/27/robinhood-ceos-ai-startup-harmonic-expands-into-software-chip-design-verification/
- Erdős problems wiki, frozen 30 Jun 2026: https://github.com/teorth/erdosproblems/wiki/AI-contributions-to-Erd%C5%91s-problems
- Axiom:
  - 5 Mar 2026: AXLE, https://axiommath.ai/research/releasing-axle
  - 12 Mar 2026: SiliconANGLE, https://siliconangle.com/2026/03/12/verifiable-ai-startup-axiom-raises-200m-prove-ai-generated-code-safe-use/ ; Menlo, https://menlovc.com/perspective/ai-will-write-all-the-code-mathematics-will-prove-it-works/ ; Madrona, https://www.madrona.com/axiom-math-carina-hong-ai-code-verification/
  - 1 Jun 2026: Fortune, https://fortune.com/2026/06/01/axiom-math-econlib-antitrust-economic-theory-verified/
  - 2026: IMO 2026 repository, https://github.com/AxiomMath/IMO2026
  - 26 Oct 2026: CFSG, https://axiommath.ai/research/the-enormous-theorem-formalized/
  - 4 Nov 2026: Stacks Project, https://axiommath.ai/research/the-stacks-project-formalized/
  - Read 12 Nov 2026: https://axiommath.ai/ ; https://sacra.com/c/axiom-math ; https://www.axiom.xyz/
- Math Inc.:
  - 26 Mar 2026: Scientific American, https://www.scientificamerican.com/article/what-happens-when-ai-starts-checking-mathematicians-work
  - 18 Jun 2026: Hack VC, https://blog.hack.vc/why-we-invested-in-math-inc/
  - 2026: IEEE Spectrum, https://spectrum.ieee.org/ai-proof-verification
  - Undated or read 12 Nov 2026: https://www.math.inc/gauss ; https://www.math.inc/archive ; https://www.caplight.com/company/math ; https://aiwiki.ai/wiki/math_inc_gauss
- Logical Intelligence:
  - 19 Sep 2025: Upstarts, https://www.upstartsmedia.com/p/math-ai-startups-push-new-models
  - 2 Dec 2025: release (403), https://www.businesswire.com/news/home/20251202089385/en
  - 20 Jan 2026: release (403), https://www.businesswire.com/news/home/20260120751310/en/
  - 26 Jan 2026: IoT M2M Council, https://iotm2mcouncil.org/iot-library/news/connected-industries-news/logical-unveils-energy-based-reasoning/
  - 20 May 2026: blog, https://logicalintelligence.com/blog/aleph-prover-tops-leading-benchmarks
  - 25 Aug 2026 (claimed): https://logicalintelligence.com/aleph-prover-final.html
  - 10 Nov 2026: homepage, https://logicalintelligence.com/
  - Read Nov 2026: MathArena, https://matharena.ai/models/logical_intelligence_aleph_prover ; https://matharena.ai/ ; CB Insights, https://www.cbinsights.com/company/logical-intelligence/financials
- Theorem, &Truth, Pramaana, newcomers:
  - 27 Jan 2026: VentureBeat, https://venturebeat.com/security/theorem-wants-to-stop-ai-written-bugs-before-they-ship-and-just-raised-usd6m
  - Read 12 Nov 2026: YC, https://www.ycombinator.com/companies/theorem-2/jobs
  - 29 Oct 2026: Dealroom, https://dealroom.co/news/168019-truth-emerges-from-stealth-with-70m-seed-to-mathematically-prove-code-is/
  - 17 Jun 2026: SiliconANGLE, https://siliconangle.com/2026/06/17/pramaana-labs-raises-27m-make-ai-prove-answers/ ; The Next Web, https://thenextweb.com/news/pramaana-labs-27m-seed-formal-verification-ai
  - 2026: Cajal, https://www.startuphub.ai/news/claudes-corner-cajal-yc-w2026 ; Lanyon AI, https://runtimewire.com/es/article/lanyon-ai-10-6m-formally-verified-scientific-computing
  - Sep 2026: VerifAIX, https://www.finsmes.com/2026/09/verifaix-raises-usd5m-in-seed-funding.html
  - Q1 2026: SemiEngineering, https://semiengineering.com/startup-funding-q1-2026/
- Code Metal:
  - 19 Feb 2026: release, https://www.businesswire.com/news/home/20260219267824/en ; eWeek, https://www.eweek.com/news/code-metal-valuation-ai-code-translation/
  - 21 Feb 2026: Pulse2, https://pulse2.com/code-metal-125-million-series-b-raised-for-verifiable-code-translation-platform
  - Read Nov 2026: https://www.codemetal.ai/
- Galois:
  - 30 Oct 2024: Military & Aerospace, https://www.militaryaerospace.com/trusted-computing/article/55238957/trusted-computing-design-and-development-tools
  - 13 Jan 2026: Year in review, https://www.galois.com/articles/2025-year-in-review
  - Read Nov 2026: HigherGov, https://www.highergov.com/contract/HR001125C0300/ ; MAPACHE, https://www.inknowvation.com/sbir/awards/darpa-2026-mapache ; https://www.galois.com/ ; https://www.galois.com/ai-formal-methods
- Runtime Verification:
  - 30 Sep 2026: https://www.runtimeverification.com/blog/the-proof-is-in-the-spec
  - 2 Oct 2026: https://www.runtimeverification.com/blog/verifying-the-linux-kernel-isolation-code
  - Read 12 Nov 2026: https://www.runtimeverification.com/about ; https://www.runtimeverification.com/blog ; https://www.cbinsights.com/compare/pi-squared-vs-runtime-verification
- Imandra:
  - 26 Mar 2025: https://www.imandra.ai/articles/imandra-releases-codelogician
  - Jan 2026: https://arxiv.org/abs/2601.11840v2
  - Read 12 Nov 2026: https://www.imandra.ai/ ; https://simplify.jobs/c/Imandra
- Veridise and CertiK:
  - 2025: https://veridise.com/blog/veridise-announcements/audithub-launches-platform-for-professional-blockchain-audit-firms/
  - Read 12 Nov 2026: https://www.rootdata.com/projects/detail/Veridise?k=NjA2Mg%3D%3D
  - Jan 2026: https://www.crowdfundinsider.com/2026/01/258056-blockchain-security-firm-certik-maintains-ipo-plans-as-valuation-reaches-2-billion/ ; https://www.theblock.co/post/386882
  - Read 12 Nov 2026: https://www.caplight.com/company/certik ; https://dealroom.co/companies/certik/ ; https://ground.news/article/certik-outlines-plan-to-pursue-public-listing-following-binance-investment
- Government and policy:
  - Read 12 Nov 2026: DARPA PROVERS, https://www.darpa.mil/research/programs/pipelined-reasoning-of-verifiers-enabling-robust-systems ; BAE PROVERS contract (undated), https://www.executivebiz.com/articles/bae-systems-books-darpa-contract-for-software-modernization ; Lincoln Laboratory TRACTOR, https://www.ll.mit.edu/tractor
  - 15 Jul 2025: UW–Madison, https://www.cs.wisc.edu/2025/07/15/translating-legacy-code-for-a-safer-future
  - Apr 2026: ORBIT, https://arxiv.org/pdf/2604.12048
  - 24 Jun 2025: CISA and NSA, https://www.cisa.gov/resources-tools/resources/memory-safe-languages-reducing-vulnerabilities-modern-software-development
  - Sep 2026 (cross-reference): Orrick, https://www.orrick.com/en/Insights/2026/09/EU-Cyber-Resilience-Act-New-Guidance-Clarifies-Scope-Reporting
  - Read Nov 2026 (cross-reference): ARIA, https://www.aria.org.uk/programme-safeguarded-ai
  - 20 Mar 2026 (cross-reference): AbsInt, https://www.absint.com/releases/260320.htm
- Market and pricing:
  - Feb 2026 (page header 31 Oct 2026): Sherlock, https://sherlock.xyz/post/smart-contract-audit-pricing-a-market-reference-for-2026
  - 2026: DEV Community, https://dev.to/ohmygod/how-ai-agents-can-audit-smart-contracts-in-2026-a-technical-deep-dive-5gl
  - 10 Nov 2026 (cross-reference): Certora, https://www.certora.com/blog/ai-formal-verification-smart-contracts-costs-use-cases ; https://www.certora.com/pricing
- Labs and the checker:
  - 22 Oct 2026: Anthropic, https://www.anthropic.com/research/formal-verification
  - 25 Oct 2026: arXiv h1, https://arxiv.org/abs/2610.35962
  - 10 Nov 2026 (cross-reference): DeepMind, https://deepmind.google/documents/36/Formal_Verification_of_Signal_4.pdf ; https://deepmind.google/blog/introducing-alphaproof-code/
  - 28 Jul 2026: Lean kernel issue, https://github.com/leanprover/lean4/issues/14576
  - 9 Oct 2026: Hales on Tao's blog, https://terrytao.wordpress.com/2026/10/09/what-mathematicians-should-know-about-the-lean-theorem-proverquestions-of-reliability-and-ai/
- Non-profits:
  - Read 12 Nov 2026: https://lean-lang.org/fro/about ; https://lean-lang.org/fro/roadmap ; https://atlascomputing.org/ ; https://www.beneficialaifoundation.org/ ; https://www.beneficialaifoundation.org/signal-shot
  - Sep 2026: https://lean-lang.org/fro/roadmap/y4-1
