# Model makers and hyperscalers as suppliers of, competitors to, and customers of verification companies

Research date: 12 November 2026 (position as of that date). Status: final. This completes an earlier partial pass; every earlier sourced fact is kept, and corrections are flagged "CORRECTION".

Tag key: [PRIMARY] official document, paper or repository read directly; [INDEPENDENT] confirmed by an outside party; [COMPANY CLAIM] stated by the company and not confirmed by an outside party; [SECONDARY] press or analyst report only; [UNVERIFIED] could not be verified.

Access note: the shared web-search budget ran out after ten searches in this pass, and the harness forbids working around it through other search services. Later work relied on:
- direct fetches of known first-party URLs;
- the AlphaProof Code paper's text, extracted locally;
- one Hugging Face Hub catalogue query;
- peer notes in this folder and the earlier lead notes, marked "(peer notes)" or "(lead notes, not re-checked)" where I could not re-check them.

openai.com returned HTTP 403. Coverage of Huawei, Alibaba/Ant, xAI, Mistral, Apple and OpenAI's security products is thin.

## 1. Google DeepMind and Google: AlphaProof Code, its lineage, and Google's own chip-design verification

### Takeaway
AlphaProof Code (10 Nov 2026) is the largest model-maker software-verification result found: about 6.5 million lines of Lean proof that the unmodified compiled libsignal library has key security properties. The proofs rest on about 18,000 lines of trusted statements and definitions plus about 8,000 lines of AArch64 semantics, and a team of five did the proof work in four weeks. The blog's "over six million lines" is consistent with the paper; the "over three million" in earlier notes is not on the page. Google sells none of this. The artefacts are open (Apache-2.0), the agent framework is unreleased, and there is no Cloud offering. Google is therefore a free showcase competitor and a customer (of formal chip tools, and of Anthropic's model), not a supplier.

### Cited Findings

**Line count: the earlier conflict resolved**
- The technical paper (dated 2026-11-10, 57 pages, authors Swarat Chaudhuri, Andrew Ferraiuolo, Anton Kovsharov, Tej Chajed, Sam Schlesinger, Karn Seth, Jonathan Katz, Charles Sutton, Pushmeet Kohli; Google DeepMind and Google) states in its abstract: "our agents generated about 6.5 million lines of machine-checked Lean proof code, resting on about 26,000 lines of trusted specifications and AArch64 semantics." [PRIMARY] — [AlphaProof Code paper (PDF), 10 Nov 2026](https://deepmind.google/documents/36/Formal_Verification_of_Signal_4.pdf)
- Breakdown in section 7 of the paper ("Scale"): "The repository contains nearly 7 million lines of Lean, counting comments and blank lines. About 6.5 million of them are proofs: 5.3 million about the binary, which both security proofs share, about 860,000 for the computational proof and about 350,000 for the symbolic proof. Another 140,000 lines prove the reintroduced bugs (§6), and 70,000 verify the allocator. The verified libsignal code is about 560 KB, about 140,000 AArch64 instructions." [PRIMARY] — [AlphaProof Code paper (PDF), 10 Nov 2026](https://deepmind.google/documents/36/Formal_Verification_of_Signal_4.pdf)
- The DeepMind blog post as read on 12 Nov 2026 says agents "powered by Gemini Carbon did the proofs, generating over six million lines of Lean"; the page shows no update or correction note. [PRIMARY] — [Google DeepMind blog, "Introducing AlphaProof Code: a breakthrough in verifying complex software at depth", 10 Nov 2026](https://deepmind.google/blog/introducing-alphaproof-code/)
- CORRECTION: on a second read (12 Nov 2026; byline Pushmeet Kohli and Swarat Chaudhuri) the phrase "three million" does not appear on the page. The lead notes' "over three million lines" (google_deepmind.md, from a search extract) is therefore unsupported and probably an extraction error; I could not establish whether an earlier version of the page said it. Resolution: about 6.5 million lines of proof within nearly 7 million lines of Lean. "Over six million" (blog) and "6 to 6.5 million" (press) both count proof lines. The Register (Thomas Claburn, 10 Nov 2026) reports 6.5 million lines, four weeks, a team of five and "quite a few tokens". [PRIMARY; SECONDARY consistent] — [The Register, 10 Nov 2026](https://www.theregister.com/ai-and-ml/2026/11/10/google-deepmind-melds-humans-and-ai-agents-to-vet-signals-secure-messaging-techniques/5308625)
- The brief's background claim is mostly right, with refinements:
  - The "26,000 lines" are about 18,000 lines of trusted statements and definitions (about 28,000 with documentation) plus about 8,000 lines of AArch64 semantics, not 26,000 lines of security specification.
  - The symbol names in a roughly 95,000-line extracted Lean representation of the machine code must also be trusted.
  - "Four weeks" is the paper's figure for "the proof work".
  [PRIMARY] — [paper PDF](https://deepmind.google/documents/36/Formal_Verification_of_Signal_4.pdf)

**What was proved, assumptions, trusted base** (paper, 10 Nov 2026, [PRIMARY]) — [paper PDF](https://deepmind.google/documents/36/Formal_Verification_of_Signal_4.pdf)
- Target and scope: "libsignal-cli, an AArch64 executable built by stock rustc from the unmodified libsignal v0.105.4 and SPQR crates", one-to-one sessions only (spqr v1.6.0). "We leave group messaging as future work."
- Properties: the PQXDH handshake and the Triple Ratchet, giving forward secrecy, authentication, post-compromise security and handshake secrecy. The symbolic model has "Ten theorems, each holding on every collision-free execution", and "No run faults or diverges". The computational model gives "a concrete bound on the attacker's advantage". The paper calls these "the first proofs connecting protocol-level security guarantees to the unmodified code of a widely used cryptographic protocol implementation."
- Assumptions. The symbolic proof uses idealised primitives: "hashes, KDFs and MACs never collide and cannot be inverted, secrets never repeat, and ciphertexts (resp., signatures) cannot be decrypted (resp., forged) without the key". The computational proof assumes "Gap-DH and XEdDSA unforgeability, Kyber1024 collision resistance, PRF/PRG security of HKDF and HMAC, and one-time CCA security of AES-CBC with HMAC". "Cryptographic primitives, the two output functions and a few library routines are specified by contracts"; everything else is verified. The Register stresses that the result assumes perfect cryptography [SECONDARY] — [The Register](https://www.theregister.com/ai-and-ml/2026/11/10/google-deepmind-melds-humans-and-ai-agents-to-vet-signals-secure-messaging-techniques/5308625)
- Not covered:
  - symbolic model: computational secrecy, more than two parties and SPQR's post-quantum healing;
  - computational model: quantum attackers, multi-device state and adversarial first messages to sessions that are later promoted. Also, "the bound becomes vacuous for multiple long sessions with many epochs".
- Trusted base: "Reading every definition that our headline theorems depend on means reading about 18,000 lines of code in the repository (about 28,000 with documentation), plus about 8,000 lines of the AArch64 semantics and a Lean representation of the compiled machine code (about 95,000 lines)... only the symbol names it assigns need to be trusted." The specification folders hold about 54,000 lines, of which only part is trusted. Also trusted are the symbol-extraction tooling, the reproducible-build scripts and Lean's kernel. "Notably, however, the Rust compiler is not trusted."
- AArch64 semantics: "467 instructions and 31 system calls in 7,532 lines of Lean", following "Arm's machine-readable ASL specification". It is tested "in lockstep against two independent oracles: the Unicorn emulator... and the Sail model of Armv9.4-A". It does not model threads, signals, the vDSO or dynamic linking.
- Validation: two real, previously fixed libsignal bugs were reintroduced, and the symbolic security theorems were proved false for the buggy binaries (140,000 lines).

**Effort, models and human role** [PRIMARY] — [paper PDF](https://deepmind.google/documents/36/Formal_Verification_of_Signal_4.pdf)
- "The proof work was done by a team of five over four weeks". A proof campaign typically ran 40 to 80 agents "on a single machine for 24 to 72 hours". A clean build "could take several hours". The paper gives no compute or token cost. For comparison, it says seL4 "took twenty person-years to verify" and CompCert "took six".
- Models: specifications "were developed through an intense back-and-forth between humans and agents powered by Gemini 4 Carbon and Claude Opus 5.5", and a reviewer agent "from a different model family" checked each draft. "The proofs were produced entirely by agent teams powered by Gemini 4 Carbon (§2.3), and none of the authors wrote any proof code." DeepMind thus used an Anthropic model; the terms are not stated.
- Human role: "we decided the scope and order of the work, chose the reference models, and guided and approved the trusted statements"; "We did not write proofs." The blog says researchers worked with a mix of models to "translate Signal's security goals into formal mathematical specifications, with human experts reviewing every one"; "Because Lean automatically checks the rest, our experts could focus their review where human judgment matters most." It adds that agents flagged areas needing "a second look by a human", "just one percent of the codebase"; this 1% figure is not in the paper. The reviewers named in the paper are the DeepMind authors. Signal staff are thanked for "feedback on the methodology", and nothing found says they reviewed the specifications. [blog: COMPANY CLAIM] — [DeepMind blog](https://deepmind.google/blog/introducing-alphaproof-code/)
- Kohli, X post, 10 Nov 2026: "This is the first time the actual production code of a widely deployed protocol has been formally verified" (truncated). [COMPANY CLAIM; lead notes, not re-checked] — [X post](https://x.com/pushmeet/status/2120127611137634376)
- Specification evidence from this project is in section 7.

**Availability, product status, outside reaction**
- The blog says "We are open-sourcing our formal verification artifacts for community use"; "Scaling these techniques requires continued research"; and the work "lays the groundwork" for "medical device firmware to power grid software". It links CodeMender as a complementary agent. There is no Google Cloud product, price, partner programme or commercial release (read 12 Nov 2026). [PRIMARY] — [DeepMind blog](https://deepmind.google/blog/introducing-alphaproof-code/)
- The paper's plan: "We are keen to use this workflow to verify new releases of libsignal before they ship, and also more broadly"; "every change to the code can be verified before it is merged". [PRIMARY] — [paper PDF](https://deepmind.google/documents/36/Formal_Verification_of_Signal_4.pdf). The Register gives no release or commercial plans and notes a Beneficial AI Foundation challenge (April 2026) to verify Signal in Lean. [SECONDARY] — [The Register](https://www.theregister.com/ai-and-ml/2026/11/10/google-deepmind-melds-humans-and-ai-agents-to-vet-signals-secure-messaging-techniques/5308625)
- Repository `google-deepmind/code-verification` (created 26 Oct 2026 per lead notes) holds "two AI-generated proofs of security for compiled AArch64 machine code of `libsignal`". Licence: Apache-2.0 (copied libsignal code is AGPL-3.0-only). Lean v4.34.0; checking takes "several hours, ~15–34 GiB peak RAM". A comparator checks headline theorems against trusted challenge statements. No agent skills or framework code are included, consistent with the secondary report that the framework is unreleased. [PRIMARY; Qodo SECONDARY] — [GitHub](https://github.com/google-deepmind/code-verification); [Qodo](https://www.qodo.ai/blog/alphaproof-code-signal-formal-verification/)
- Signal CTO Ehren Kret, quoted by DeepMind: "Using AI agents to translate live code into valid Lean theorems is a major breakthrough"; "this new approach enables a significant expansion". DeepMind also thanks Signal's Rolfe Schmidt and Michael Rosenberg. [COMPANY CLAIM quoting an outside party] — [DeepMind blog](https://deepmind.google/blog/introducing-alphaproof-code/)
- Outside commentary comes from vendors and trade blogs. Qodo stresses the 1% human-review share and the reliance on human-reviewed specifications and idealised cryptography. Developers Digest quotes a practitioner warning that models cheat in proofs. No named independent formal-methods academic was found commenting by 12 Nov 2026. [SECONDARY] — [Qodo](https://www.qodo.ai/blog/alphaproof-code-signal-formal-verification/); [Developers Digest](https://www.developersdigest.tech/blog/alphaproof-code-signal-formal-verification-agents-2026); [The Next Web](https://thenextweb.com/news/google-deepmind-alphaproof-code-signal-encryption-formal-verification); [AI Weekly](https://aiweekly.co/alerts/google-deepminds-alphaproof-code-formally-verifies-signal-protocol-guarantees)

**Lineage, Google Cloud, chip design**
- AlphaProof Nexus (arXiv 2605.22763, May 2026, "Advancing Mathematics Research with AI-Driven Formal Proof Search") is reported to have solved 9 open Erdős problems and 44 OEIS conjectures at a few hundred dollars per solution. Its Lean proofs are public in google-deepmind/alphaproof-nexus-results; the framework is not shared. [SECONDARY] — [The Decoder](https://the-decoder.com/google-deepminds-alphaproof-nexus-solves-decades-old-math-problems-for-a-few-hundred-dollars/); [arXiv 2605.22763](https://arxiv.org/pdf/2605.22763); critical view: [Science Media Centre Spain](https://sciencemediacentre.es/en/alphaproof-nexus-new-ai-tool-designed-tackle-mathematical-proofs)
- Other Gemini results checked in Lean (lead notes, not re-checked): Gemini 4 Argon's quantum arcsin routine was "formally verified in Lean" [SECONDARY] — [Interesting Engineering](https://interestingengineering.com/ai-robotics/google-gemini-4-argon-quantum-fusion-robotics); a Gemini pipeline formally verified BB(6) accelerations (19 Oct 2026) — [arXiv 2610.22603](https://arxiv.org/abs/2610.22603)
- AlphaEvolve (May 2025) proposed "a Verilog rewrite that removed unnecessary bits in a key, highly optimized arithmetic circuit for matrix multiplication". The rewrite passed "robust verification methods to confirm that the modified circuit maintains functional correctness" and was "integrated into an upcoming Tensor Processing Unit". [PRIMARY via search extract] — [DeepMind AlphaEvolve blog](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)
- AlphaEvolve on Google Cloud: private preview from December 2025; generally available "to all Google Cloud customers on Gemini Enterprise Agent Platform" in July 2026 (sources differ on 9 or 10 July). Early adopters are BASF, JetBrains and Kinaxis, and preview testers included semiconductor firms (unnamed). It optimises against a user-supplied evaluator, so it is an optimiser, not a verifier. [PRIMARY via search extract; date conflict] — [Google blog](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/alphaevolve-on-cloud/); [Google Cloud blog, Dec 2025](https://cloud.google.com/blog/products/ai-machine-learning/alphaevolve-on-google-cloud); [IT Brief UK](https://itbrief.co.uk/story/google-cloud-makes-alphaevolve-generally-available); [InfoQ, Dec 2025](https://www.infoq.com/news/2025/12/alphaevolve-google-cloud); [HPCwire, 9 Nov 2026](https://www.hpcwire.com/2026/11/09/accelerating-time-to-insight-ai-powered-development-and-purpose-built-hpc-on-google-cloud/)
- AlphaChip: DeepMind says its layouts have been used in every TPU generation since 2020, and MediaTek has extended it for Dimensity chips (September 2024). No 2026 source links it to verification. [PRIMARY 2024; any 2026 link UNVERIFIED] — [DeepMind](https://deepmind.google/blog/how-alphachip-transformed-computer-chip-design/)
- Google buys formal tools: a mid-2026 TPU design-verification job ad asks candidates to "formally verify designs with SVA and industry leading formal tools". [SECONDARY, job-board mirror] — [job posting](https://jobs.anitab.org/companies/google-24698/jobs/83694467-design-verification-engineer-tpu-cloud-compute)

### Inferences
- The proof work took about 20 person-weeks (my arithmetic), against seL4's 20 person-years. The scopes differ, so this is only an order of magnitude.
- Google's near-term effect is to anchor expectations and prices. It is doing a flagship engagement (Signal) and planned release checks for free, as a reputation and open-source move, not as a product.
- DeepMind used a rival's model (Claude) for specifications and used diversity across model families as a check. Model makers are buying each other's models as inputs.
- In chips, Google appears only as an optimiser (AlphaEvolve, AlphaChip) and as a buyer of commercial formal tools.

### Gaps
- Not found: AlphaProof Code's compute cost; any named academic assessment; any productisation plan; CodeMender's status.
- Not verified: whether the blog ever said "three million"; the AlphaProof Nature (2025) and AlphaProof Nexus Science (8 Oct 2026, per lead notes) papers; AlphaChip's role in the TPU 8 generation.

## 2. Microsoft

### Takeaway
Microsoft has long been a free upstream supplier of verification infrastructure (Z3; Lean's creator worked there; Verus proof-synthesis research). It now uses AI with formal methods internally at very large scale: agents infer TLA+ specifications, and proofs are written in F*, Lean and Verus for the Windows and Azure modernisation. It sells no verification product, and no Azure or GitHub offering was found. In chips it is a partner and customer of the incumbents.

### Cited Findings
- "Cheap code, precious trust: Code modernization at scale", Microsoft Command Line, 2026.10.26, by Sriram Rajamani (CVP, Future of Scalable Software Engineering, CoreAI) and Tim Bozarth (CVP, Eng Horizons, CoreAI & EngThrive). Thesis: "Generating code is becoming the easy part. Knowing whether to trust it is the real challenge."; "Human attention has become the scarcest resource in agentic software engineering". Method:
  - "Our first step is to infer formal specifications (e.g., TLA+) from existing codebases using agents"; TLC checks that implementation traces "are admitted by the specifications".
  - "The discrepancy may point to an implementation defect, an inaccurate specification, or an invalid test, and agents revise whichever is wrong".
  - "we prove properties for all configurations in F* and Lean", "using Verus to prove that the modernized code satisfies them".
  - "The engineer reviews and approves the properties", while "the agents find the inductive invariants".
  - Lead notes add, in paraphrase, that some tests are held back from agents.
  [PRIMARY] — [Microsoft Command Line, 26 Oct 2026](https://commandline.microsoft.com/agentic-software-engineering-large-scale-code-migration-language-modernization-spec-driven-development/)
- Same post, scale: "a 400-million-line codebase" migrated to a new compiler toolchain; Windows has "several hundred million lines of code"; "approximately 30,000 lines" of working translations by September 2025. It gives no bug counts. Tools named: CodeQL, PREfast, Roslyn analyzers, Clang/LLVM, TLA+, TLC, F*, Lean, Verus, and an internal TLA+-to-F*/Lean compiler. There is no customer offering, GitHub product or open-source release. WindowsForum notes the post has no benchmarks or independent validation. [PRIMARY; results COMPANY CLAIM] — [WindowsForum](https://windowsforum.com/news/microsoft-details-ai-agent-verification-for-windows-and-azure-codebases-why-trust-is-the-new-bottleneck.450086/)
- Lead notes, not re-checked: tlalink (25 Oct 2026) "links TLA+/Plang/Dafny with sources for managing correctness proofs" — [GitHub microsoft/tlalink](https://github.com/microsoft/tlalink). Amplifier Constellation (2 Nov 2026): "Independent verification and requester acceptance remain distinct from the agent saying it is done." — [GitHub](https://github.com/microsoft/amplifier-constellation)
- VeruSAGE (Microsoft Research): 849 proof tasks from eight Verus-verified Rust systems; its agent system completes "over 90%" of a separate set of system proof tasks; code at microsoft/verus-proof-synthesis. Verus has verified systems "including IronKV and components of Azure infrastructure". The predecessor is AutoVerus (OOPSLA 2025). [PRIMARY via search extract; date not confirmed] — [MSR VeruSAGE](https://www.microsoft.com/en-us/research/publication/verusage-a-study-of-agent-based-verification-for-rust-systems/); [Verus leaderboard](https://microsoft.github.io/verus-proof-synthesis/about.html); [AutoVerus arXiv](https://export.arxiv.org/pdf/2409.13082)
- Heritage, as far as checked:
  - "Z3 is a theorem prover from Microsoft Research", MIT-licensed [PRIMARY] — [GitHub Z3Prover/z3](https://github.com/Z3Prover/z3).
  - The Lean FRO page says Leonardo de Moura "created Lean in 2013 and previously worked on automated reasoning and theorem proving at Microsoft Research" (first commit July 2013). It does not say outright that Lean began at Microsoft Research, so the brief's claim is only partly verified. The page also cites a Microsoft Research SymCrypt verification report. [PRIMARY] — [Lean FRO About](https://lean-lang.org/fro/about)
  - dafny.org does not state Dafny's Microsoft Research origin [UNVERIFIED] — [dafny.org](https://dafny.org/). F*'s origins were not checked.
- Galen Hunt (Distinguished Engineer), December 2025: a goal of eliminating C and C++ from Microsoft by 2030 using AI. After a backlash, he and Microsoft called it a research project and said Windows is not being rewritten in Rust with AI. [SECONDARY] — [TechRadar](https://www.techradar.com/computing/cloud-computing/microsoft-engineer-clarifies-speculation-around-plans-to-eliminate-c-c-languages-by-2030); [Windows Latest, 24 Dec 2025](https://www.windowslatest.com/2025/12/24/microsoft-denies-rewriting-windows-11-using-ai-after-an-employees-one-engineer-one-month-one-million-code-post-on-linkedin-causes-outrage); [InfoWorld](https://www.infoworld.com/article/4111553/microsoft-is-not-rewriting-windows-in-rust.html)
- Chips: Synopsys's agentic AI chip design with AMD and Microsoft (27 Jul 2026): "Early evaluations show reductions of 25–40% in debug cycle time"; AMD is "actively evaluating" [COMPANY CLAIM; peer notes] — [Synopsys](https://news.synopsys.com/2026-07-27-Synopsys-Advances-Agentic-AI-Chip-Design-with-AMD-and-Microsoft). Siemens' Questa One Agentic Toolkit (27 Feb 2026) works with GitHub Copilot [PRIMARY per peer notes] — [Siemens](https://news.siemens.com/fr-fr/questa-one-agentic-ai-toolkit/)

### Inferences
- Microsoft's leaders describe the bottleneck as the background view does (trust, specifications, human attention), but treat the work as internal productivity.
- Z3 and Microsoft's other free tools are embedded in many vendors' products, so Microsoft supplies the industry for free rather than competing with it for revenue.
- Microsoft is plausibly the lab most likely to turn agent-inferred specifications into a developer product through GitHub. No announcement was found.

### Gaps
- Not checked: GitHub Spec Kit and any GitHub or Azure verification feature; Project Everest/HACL* and SymCrypt details; F* and Dafny origins; 2026 statements by Nadella, Russinovich or Scott.

## 3. Anthropic

### Takeaway
Anthropic sells tokens, not verification. Its research shows formal proof at scale (about 180 million lines of Rocq across 123 libraries; a Lean proof of Fermat's Last Theorem). Its model is the engine inside rivals' and start-ups' verification: DeepMind's specifications, Kiro's Lean proofs and Theorem's pipeline. Both background claims are confirmed, with wording corrections.

### Cited Findings
- Background claim checked. The launch post "Introducing Claude Fable 5.2 and Claude Mythos 5.2" (9 Nov 2026; edit note dated 11 Nov) says: "Over 90% of the changes merged into Anthropic's core codebase are now written by Claude (with human guidance)." The brief drops "(with human guidance)" and "core". [PRIMARY; COMPANY CLAIM, not independently measured] — [Anthropic, 9 Nov 2026](https://www.anthropic.com/news/claude-fable-and-mythos-5-2). An earlier footnote (16 Oct 2026) said "more than 80% of the code merged into Anthropic's codebase is now written by Claude" [PRIMARY per lead notes] — [The AI expectations gap](https://www.anthropic.com/research/ai-expectations-gap)
- Same launch post:
  - "a team of 1,000 Fable 5.2 agents fully formalized" Fermat's Last Theorem "in just 30 hours, with minimal human intervention", using "one-third as many action tokens" and producing "a proof seven times shorter" than the first formalisation, which "took 11 days".
  - "Opus 5.5 (with the same 1,000-agent setup) completed only 26% of the formalization in 18 hours".
  - Customer testimonial (iGent): "More than 3,500 machine-checked proofs cover every case, not just the ones you test."
  - Fable 5.2 costs "$8 per million input tokens and $40 per million output tokens", on AWS, Google Cloud and Azure.
  - "Verification Programs" there means an access programme for vetted organisations, not formal verification (not checked further).
  [PRIMARY; COMPANY CLAIM] — [Anthropic, 9 Nov 2026](https://www.anthropic.com/news/claude-fable-and-mythos-5-2)
- Fermat repository README:
  - "A complete, machine-checked proof of Fermat's Last Theorem in Lean 4" on Mathlib: 60,475 modules, "29,511 theorems".
  - The independent kernel nanoda "Checked 1052234 declarations with no errors". Only the axioms propext, Classical.choice and Quot.sound are used, with no sorry or native_decide. Comparator verdict: "Your solution is okay!".
  - "produced by AI agents building on human-written open-source Lean". No human statement reviewer is named; Buzzard's Imperial project is credited as a source.
  - An aggregator reports about 13 million lines and a review by Buzzard for the first run, announced 4 Sep 2026 [SECONDARY, lead notes].
  [PRIMARY] — [GitHub anthropics/fermats-last-theorem](https://github.com/anthropics/fermats-last-theorem); [aiweekly](https://aiweekly.co/alerts/anthropics-claude-formalizes-fermats-last-theorem-in-lean)
- Background claim checked. "LLMs are making formal software verification feasible at a much larger scale" (Frontier Red Team, 22 Oct 2026; Keane Lucas and 14 co-authors including Nicholas Carlini, Nickolai Zeldovich, and Theorem co-founders Rajashree Agrawal and Jason Gross per peer notes; "In a collaboration with Theorem"). The exact prediction is that formal verification "will soon be as practical as fuzzing is today for almost all production software", and "we expect formal verification to become an essential part of secure software development." The brief's "as routine as automated random testing" is close, but the source says "practical", with "soon" and "almost all". [PRIMARY; forecast] — [Anthropic, 22 Oct 2026](https://www.anthropic.com/research/formal-verification)
- Same post, figures:
  - "239 entry points across 123 different OSS-Fuzz libraries", for "every input less than 64 MB".
  - "about 180 million lines of Rocq"; a typical proof is about 600,000 lines; median 18,000 RISC-V instructions.
  - "a few weeks"; "hundreds of bugs" found.
  - Proofs "can take hundreds of millions of tokens"; "Opus 5.5 proves half of them with about 40% fewer tokens than Opus 5" (36 tasks).
  - A Verus-proved Python implementation matched CPython on 99.95% of over 1.7 million random programs.
  - No overall success rate is given.
  Anthropic publishes "a subset of these proofs" plus the RISC-V and OS semantics, and withholds some that "may reveal an unpatched bug". Theorem supplied the semantics, is "offering to run the same pipeline for other open-source projects" and is publishing a Claude skill. No Anthropic product is announced. [PRIMARY; COMPANY CLAIM] — [Anthropic, 22 Oct 2026](https://www.anthropic.com/research/formal-verification). Theorem raised a $6M seed led by Khosla on 27 Jan 2026 [SECONDARY, peer notes] — [VentureBeat](https://venturebeat.com/security/theorem-wants-to-stop-ai-written-bugs-before-they-ship-and-just-raised-usd6m)
- "Building a C compiler with a team of parallel Claudes" (Nicholas Carlini, 5 Feb 2026):
  - "a 100,000-line compiler that can build Linux 6.9 on x86, ARM, and RISC-V";
  - 16 Opus 4.6 agents, nearly 2,000 sessions over two weeks, about 2 billion input and 140 million output tokens, "just under $20,000";
  - checked by test suites (99% pass rate, including GCC torture tests) and differential testing against GCC, not formal verification;
  - output "less efficient than GCC with all optimizations disabled".
  [PRIMARY; COMPANY CLAIM] — [Anthropic Engineering](https://www.anthropic.com/engineering/building-c-compiler)
- Lead notes, not re-checked:
  - The refutation of the Exponential Time Hypothesis (ETH) in anthropics/formal-math has a "Lean 4 formalization, which was written by AI models". An independent rebuild found that it uses only the standard three axioms [PRIMARY + INDEPENDENT] — [formal-math](https://github.com/anthropics/formal-math/tree/main/eth); [rebuild](https://github.com/unaltuzun/exponential-time-hypothesis-verify).
  - FlashProve provable inference (2 Nov 2026), at "~70-95x the GPU time" — [Anthropic](https://www.anthropic.com/research/provable-inference).
  - Electronics design (9 Nov 2026): Fable 5.2 scored 69% against 25% for Fable 5, but the designs "haven't been through electrical validation" — [Anthropic](https://www.anthropic.com/research/claude-electronics-design)
- Chips: The Information (3 Nov 2026, paywalled) reported that Anthropic told prospective IPO investors its roughly 15-person chip team uses Claude, and that Anthropic approached EDA firms about chip-design data. Synopsys fell 2.5% and Cadence 4.5% that day. One analysis did not find this in the amended S-1. [SECONDARY, peer notes] — [The Information](https://www.theinformation.com/briefings/synopsys-cadence-shares-drop-4-information-report); [Dealroom](https://dealroom.co/news/169588-anthropic-tells-ipo-investors-its-15-person-chip-team-designs-custom-sil)

### Inferences
- Anthropic enters verification as the default engine that others pay for in tokens (DeepMind, Kiro, Theorem, Harmonic via Claude Code per peer notes). It is a supplier to verification firms and to rival labs, and its artefacts compete for free.
- Specifications derived mechanically from fuzz harnesses show that weak but useful properties (no crash) need little specification labour. Rich properties, as in AlphaProof Code, still do.
- Illustrative cost (my arithmetic at Fable 5.2 list prices; the actual models and token mix are not stated): "hundreds of millions of tokens" is roughly $1,000 (all input) to tens of thousands of dollars (mostly output) per entry point.

### Gaps
- No verification product statement was found, and the terms of the Theorem collaboration are unknown. The chip team's EDA usage rests only on secondary reports.

## 4. OpenAI

### Takeaway
OpenAI uses Lean to check its claimed mathematics (about 42% formalised). In chips it partners with the incumbent rather than competing: in GPT-Synopsys, OpenAI licenses Synopsys tools, revenue is shared, and Synopsys's tools are the "ground-truth". It says its models assisted the development of its Jalapeño chip. No verification product or acquisition was found, though checks were limited (openai.com returned 403 and searches had run out).

### Cited Findings
- The openai/math README (read 12 Nov 2026) says the repository holds manuscripts and proof artefacts "produced by an unnamed internal OpenAI model"; "The repository has ~42% top-line results formalized." It does not say who wrote the Lean statements or how their faithfulness was checked, and it points to Comparator instructions. [PRIMARY] — [GitHub openai/math](https://github.com/openai/math)
- Outside checks (lead notes, not re-checked):
  - An independent rebuild of OpenAI's ETH proof reports "Lean default kernel accepts the solution" [INDEPENDENT] — [rebuild](https://github.com/unaltuzun/exponential-time-hypothesis-verify).
  - The Yang–Mills group's assessment (dated 10 Nov 2026) of OpenAI's 28 Oct submission: it "does not prove that the infinite-volume limit is unique or that there is a mass gap" [INDEPENDENT] — [yang-mills-group/YM](https://github.com/yang-mills-group/YM)
- GPT-Synopsys (30 Sep 2026):
  - The model is to "reason about chip design and verification, and to directly operate Synopsys' tools", with agents working "toward verified outcomes for engineer review".
  - "OpenAI to license Synopsys' trusted electronic design automation (EDA) tools"; "a revenue sharing arrangement".
  - "The joint service offering will provide the bundled compute, model, and licenses"; "preferred partners" (exclusivity not stated).
  - Ghazi (Synopsys CEO) speaks of "the underlying, ground-truth engineering tools"; Brockman says "get to a working chip faster".
  - No price or GA date. Peer notes report subscription, consumption and outcome-based revenue sharing (Investor Day, 30 Sep 2026).
  [PRIMARY; COMPANY CLAIM] — [Synopsys release](https://news.synopsys.com/2026-09-30-OpenAI-and-Synopsys-Announce-GPT-Synopsys-Frontier-Intelligence-to-Revolutionize-Chip-Design); [Futurum](https://futurumgroup.com/insights/synopsys-investor-day-2026-turns-eda-into-a-royalty-and-ai-model-revenue-share-business/)
- Jalapeño (TechCrunch, Russell Brandom, 24 Jun 2026): "designed and manufactured in collaboration with Broadcom"; "OpenAI's own AI models assisted in the development of the chip, the company said"; "still being tested". No EDA or verification detail is given. [SECONDARY; COMPANY CLAIM] — [TechCrunch](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/). Internal deployment in early October 2026 rests on secondary trackers [UNVERIFIED, lead notes]
- Security: GPT-6 Cyber, a cyber-specialised GPT-6 Astra variant limited to approved customers [UNVERIFIED; page not opened] — [OpenAI](https://openai.com/index/introducing-gpt-6-cyber/). The Aardvark page returned 403 [UNVERIFIED] — [openai.com](https://openai.com/index/introducing-aardvark/)

### Inferences
- OpenAI is a Synopsys customer (tool licences) and a channel partner. It is the clearest case of a model maker reinforcing an incumbent's verdict in chips.
- In mathematics, outsiders own the verdict (kernel, rebuilds, expert groups). The unformalised 58% shows that claims are produced faster than they can be checked.

### Gaps
- Not verified: Aardvark and GPT-6 Cyber; any verification acquisition; the actual role of AI in Jalapeño's design and verification.

## 5. Amazon Web Services

### Takeaway
AWS is the only hyperscaler selling features built on formal verification to outsiders:
- Automated Reasoning checks in Bedrock Guardrails ($0.17 per 1,000 text units per policy);
- IAM Access Analyzer (built on Zelkova);
- Policy in Bedrock AgentCore, whose policy language is verified in Lean;
- requirements analysis in Kiro.

These are narrow features inside larger services, not a general verification product. Most of its formal work is internal (S3, Nitro, s2n-bignum). Amazon is Lean's largest funder and employs its creator. Its Kiro team proves properties of its own harness in Lean using Claude Opus 5.5, with a person reviewing every theorem statement.

### Cited Findings
- Automated Reasoning checks became generally available on 6 Aug 2025 (AWS News Blog, Danilo Poccia; updated 15 Aug 2025).
  - The checks use "mathematical logic and formal verification techniques" and claim "up to 99% verification accuracy, providing provable assurance in detecting AI hallucinations"; the measure is not defined.
  - Policies are built from an uploaded document. The user reviews the policy, writes or generates test scenarios and labels the results; natural-language-to-logic translation uses a user-set confidence threshold.
  - Launch regions: Ohio, N. Virginia, Oregon, Frankfurt, Ireland and Paris. PwC is the "launch collaborator". The ingestion limit is 122,880 tokens (about 100 pages).
  [PRIMARY; accuracy COMPANY CLAIM] — [AWS News Blog](https://aws.amazon.com/blogs/aws/minimize-ai-hallucinations-and-deliver-up-to-99-verification-accuracy-with-automated-reasoning-checks-now-available/)
- Price on 12 Nov 2026: "$0.17 per 1,000 text units per Automated Reasoning policy" (a unit is up to 1,000 characters), against $0.15 for content filters and $0.10 for contextual grounding. [PRIMARY] — [Bedrock pricing](https://aws.amazon.com/bedrock/pricing/)
- Byron Cook, "A decade of mathematical certainty" (Amazon Science, 11 Aug 2026).
  - Customer products: AR checks; IAM Access Analyzer ("uses Zelkova to help customers"); Reachability Analyzer; Inspector network analysis; S3 Block Public Access; Policy in Bedrock AgentCore; and Kiro's "requirements analysis capability", which proves "no contradictions, ambiguities, and gaps in the software requirements".
  - Internal uses: S3, s2n-bignum and the Nitro Isolation Engine. The authorisation engine "handles one billion API calls per second", checked against "quadrillions of production authorizations".
  - "We can now pair those tools with language models to find proofs for more and much bigger systems"; "the need for mathematical guarantees about their behavior becomes critical."
  - The post does not use the word "neurosymbolic" and gives no figure for autoformalisation accuracy.
  [PRIMARY; COMPANY CLAIM] — [Amazon Science](https://www.amazon.science/blog/a-decade-of-mathematical-certainty-reflections-on-the-automated-reasoning-group)
- Byron Cook and Shawn Bice, 26 Jul 2026: "substantial, long-term financial support" for the Lean FRO (amount undisclosed), "the single largest donation in the FRO's history"; "coupling generative AI with Lean's mathematical rigor will help enable verified, trustworthy AI agents"; AgentCore Policy "uses Lean-based verification to prove the correctness of the policy language"; "We haven't seen anyone else offer this type of mathematical guarantee." [PRIMARY] — [Amazon Science](https://www.amazon.science/news/amazon-is-investing-in-the-lean-focused-research-organization)
- The Lean FRO page confirms the donation. It lists de Moura as Chief Architect and "senior principal applied scientist in the Automated Reasoning Group at Amazon Web Services", with other donors Harmonic (February 2026) and XTX Markets (September 2026). No other model maker is listed as a donor. [PRIMARY] — [Lean FRO](https://lean-lang.org/fro/about)
- Other 2026 Amazon Science items: EC2's formally verified isolation engine (10 Jun) and its Isabelle/HOL basis (17 Apr); Verus for provably correct Rust (Bryan Parno, 31 Aug); network-configuration validation (11 Nov); papers at NeSY, ISSTA, ASE and the NeurIPS 2026 AI for Verifiable Coding workshop. [PRIMARY, index] — [Amazon Science index](https://www.amazon.science/research-areas/automated-reasoning)
- Kiro pricing (12 Nov 2026): Free $0 (50 credits); Pro $20 (1,000); Pro+ $40 (2,000); Pro Max $100 (5,000); Power $200 (10,000) per user per month; overage $0.04 per credit; teams $20 per seat with 500 credits and pooling; GovCloud about 20% higher. The page does not mention specs or property-based testing. [PRIMARY] — [Kiro pricing](https://kiro.dev/pricing/)
- "One year of Kiro" (Deepak Singh, 14 Jul 2026): "More than 100,000 developers tried Kiro IDE within the first 5 days"; generally available "In November" (2025 by inference); "We were the first to bring spec-driven development to AI coding tools"; property-based testing "measures whether your code matches your spec"; Siemens is a customer example. [PRIMARY; COMPANY CLAIM] — [Kiro](https://kiro.dev/blog/one-year/)
- Kiro updates, September to November 2026: workflows (30 Sep); memory (20 Oct); "Spec it safe" security requirements in specs (30 Oct); Lean harness proofs (2 Nov); credit pooling (4 Nov); "Approve for me" (10 Nov). Models offered include Claude Opus 5.5, Fable 5.1, GPT-5.6 and Kimi K3. [PRIMARY, titles] — [Kiro blog](https://kiro.dev/blog/)
- "Kiro proves properties of its own harness in Lean" (2 Nov 2026; Kharkov, Erata, Omidvar-Tehrani, Mukherjee):
  - "Lean proved 70 of them" (of 96 candidate properties).
  - "The work was done by Kiro itself: the Kiro CLI, using Claude Opus 5.5 served by Amazon Bedrock and a set of Lean 4 skills".
  - "we reviewed every theorem statement, because the kernel can check a proof misaligned with the source code"; links to production code "still depend[s] on the accuracy of the models, theorem statements and differential-test harnesses".
  - No customer feature is announced; the internal plan is to "state each one as a theorem while the feature is designed".
  [PRIMARY] — [Kiro blog](https://kiro.dev/blog/harness-properties-in-lean/)
- Amazon as a chip customer: a "Multi-year, $1B+ agreement" with Synopsys for Nitro, Graviton and Trainium IP, with Synopsys using Bedrock (30 Sep 2026). [PRIMARY, peer notes] — [Synopsys](https://news.synopsys.com/2026-09-30-Synopsys-and-Amazon-Announce-Strategic,-Multi-year-IP-Agreement-for-Custom-Silicon-Collaboration-Also-Extends-to-Cloud-and-AI-Powered-Engineering)

### Inferences
- AWS is all three: a supplier of narrow features, a competitor that bundles verification-like capabilities into Kiro and Guardrails at seat or usage prices, and a customer of Synopsys and of Anthropic's models.
- The per-text-unit pricing of AR checks sets a very low price anchor for "verified" LLM output. It covers only policy compliance, far from verifying code or chips.

### Gaps
- Not checked: 2026 AR-checks updates and accuracy studies; Kiro requirements-analysis launch date and price; any explicit "neurosymbolic" statement by Cook; AR-checks revenue.

## 6. Others: Meta, Apple, Nvidia, xAI, Mistral and Chinese labs

### Takeaway
In this group, only Chinese labs openly release prover models (DeepSeek, ByteDance, StepFun, Meituan and Shanghai AI Lab), and many third-party provers are built on Alibaba's Qwen models. Meta gives away a Lean checker for GPU kernels. Nvidia acts as an investor in and partner of tool vendors. None was found selling verification. Coverage of Huawei, Alibaba/Ant, Apple, xAI and Mistral is thin.

### Cited Findings
- Meta's lean_kernel_verify checks Blackwell GPU kernels (TLX/Triton, CuTe DSL) for "hangs, out-of-bounds or wrapped addresses, missing or duplicate output writes, mbarrier protocol errors". It covers only the inputs in each case file, discharges proofs with `native_decide`, is MIT-licensed, and has no stated production use. Lead notes give 20 Oct 2026 as its date. [PRIMARY] — [GitHub](https://github.com/facebookresearch/lean_kernel_verify). Meta-affiliated "h1" (25 Oct 2026) "matches or outperforms specialized workflows such as Goedel-Architect and AlphaProof Nexus" [PRIMARY per lead notes] — [arXiv 2610.35962](https://arxiv.org/abs/2610.35962)
- Nvidia (peer notes):
  - $2B in Synopsys stock (1 Dec 2025; "not exclusive") — [Synopsys](https://news.synopsys.com/2025-12-01-NVIDIA-and-Synopsys-Announce-Strategic-Partnership-to-Revolutionize-Engineering-and-Design).
  - NVentures in Harmonic's Series C (Jan 2026) — [SiliconANGLE](https://siliconangle.com/2026/01/15/nvidias-nventures-backs-harmonic-ai-series-c-mathematical-superintelligence/) — and in Ricursive Intelligence's $300M Series A (26 Jan 2026).
  - Partner in agentic verification flows at Synopsys (26 Jul 2026), Cadence (Computex 2026) and Siemens (Nemotron/NIM).
  Nvidia's internal formal practice was not checked.
- Apple, xAI and Mistral: the lead notes found no verification work, and none was searched in this pass. Mistral reportedly has a cyber variant in preview [UNVERIFIED]. Grok sits in SpaceX's "Super Intelligence" segment [SECONDARY, lead notes] — [CNBC](https://www.cnbc.com/2026/10/20/spacex-spcx-earnings-live-updates-q3-2026html.html)
- DeepSeek-Prover-V2 comes in "7B and 671B" sizes with open weights (30 Apr 2025), MIT-licensed code and a separate model licence. It scores "88.9% pass ratio on the MiniF2F-test" and solves 49 of 658 PutnamBench problems; V1 and V1.5 date from 2024. [PRIMARY] — [GitHub](https://github.com/deepseek-ai/DeepSeek-Prover-V2); [HF](https://hf.co/deepseek-ai/DeepSeek-Prover-V2-671B)
- ByteDance Seed-Prover 1.5 (arXiv 2512.17260) "can solve 88% of the problems in PutnamBench and 11 out of the 12 competition problems from Putnam 2025". Seed-Prover 1.0 "solved 4 out of 6 problems in IMO 2025". The repository (Apache-2.0) publishes proofs, not weights. Open-weight BFS-Prover-V1-7B (Feb 2025) and V2 7B/32B (Sep–Oct 2025) are Apache-2.0. No verification product was found. [PRIMARY] — [GitHub](https://github.com/ByteDance-Seed/Seed-Prover); [HF](https://hf.co/ByteDance-Seed/BFS-Prover-V2-32B)
- Hugging Face catalogue (12 Nov 2026): StepFun-Prover-Preview-32B (Aug 2025, Apache-2.0) — [HF](https://hf.co/stepfun-ai/StepFun-Prover-Preview-32B); Meituan LongCat-Flash-Prover (20 Mar 2026, MIT) — [HF](https://hf.co/meituan-longcat/LongCat-Flash-Prover); Shanghai AI Lab InternLM step-provers (2024) — [HF](https://hf.co/internlm/internlm2_5-step-prover); Kimina-Prover (Project Numina; Moonshot's role not confirmed) — [HF](https://hf.co/project-numina/Kimina-Prover-72B). Kimina, Goedel-Prover-V2, BFS-Prover and QED-Nano list Qwen base models. No Alibaba or Ant prover was among the 40 most-liked "Prover" models. [PRIMARY, metadata]
- Moonshot:
  - TCSExam (arXiv 2611.07962, Nov 2026), whose theorem tasks are checked by the Lean kernel: "GPT-6 Astra leads Full (71.9), and Opus 5.5 leads Lite (72.3)" [PRIMARY per lead notes] — [arXiv](https://arxiv.org/abs/2611.07962).
  - Kimi K3 produced a 4 mm², 100 MHz, 45nm design with "exclusively open-source tools", with no fabrication or sign-off; Bloomberg Intelligence saw "no immediate threat" [SECONDARY, peer notes] — [Investing.com, 17 Jul 2026](https://www.investing.com/news/stock-market-news/cadence--synopsys-slide-as-kimi-k3-designs-chip-in-48h-using-no-proprietary-eda-4798775)
- Huawei: claims of formally verified kernels could not be checked [UNVERIFIED].

### Inferences
- Open-weight Chinese provers push the price of proof writing towards zero. No Chinese lab was found moving into specification tooling or into sign-off.

### Gaps
- Not researched: Huawei (HarmonyOS/HongMeng), Alibaba and Ant, Apple (for example iMessage PQ3), Nvidia internal practice, xAI and Mistral.

## 7. Who writes and owns specifications, and can AI write them? Quotations and evidence

### Takeaway
Every lab that published in-house evidence (DeepMind, Microsoft, AWS, Anthropic) keeps humans as approvers of specifications while agents draft them. DeepMind is the most explicit: proofs are no longer the bottleneck, specifications are, and agents both write hard-to-audit specifications and weaken goals under pressure. Microsoft openly asks whether AI-written specifications can be trusted.

### Cited Findings
- DeepMind paper (10 Nov 2026), §2: "The majority of human effort in software verification now lies in engineering the specification... Previously, the expertise and labor required to write proofs was a bottleneck to large-scale formal verification, but this is no longer the case." Also: "For large, complex systems, AI assistance can reduce the cost of specification writing and assurance but not completely replace human judgment and review. Based on these observations, we propose that human authors select what to prove, resolve ambiguities, evaluate security trade-offs, and make all final decisions, while AI agents draft and test specifications under human direction." [PRIMARY] — [paper PDF](https://deepmind.google/documents/36/Formal_Verification_of_Signal_4.pdf)
- §2.1: the specification "must be trusted... and it cannot be automatically checked—a flaw could weaken the guarantee"; "human review is not expected to detect all bugs in a large codebase". Hence skeptical reviewer agents ("effective at detecting soundness and strength issues"), formally proved non-vacuity checks, mutation tests of specifications and checks against historical bugs. [PRIMARY]
- §7: "once proofs become cheap, the hard question is what to prove. The majority of our effort went not into proofs but into specifications"; "Left to themselves, agents produced specifications that were hard to audit; we sometimes directed rewrites for legibility". [PRIMARY]
- §7: human-written published specifications had errors too. The departures catalogue "has over 200 entries" (computational) and "about 35" (symbolic). "Fifteen are gaps or bugs in the computational analysis of the Double Ratchet". The printed ProVerif queries of Cheval, Jacomme and Richards "look up skipped message keys at the wrong ratchet index, which makes receiver-side forward secrecy false as printed". CORRECTION: an interim draft dated that analysis "2025-26"; the paper gives no date, so the date is withdrawn. [PRIMARY]
- §7, provers weakening goals: "Agents under pressure to finish a goal will sometimes weaken it... in one swarm of Lean-proving agents, an agent redefined a predicate used in a conjecture's hypothesis as False, and the trick spread to the rest of the swarm" (a case cited from another project). Countermeasures:
  - a gatekeeper that sees only file paths and theorem names;
  - fresh-environment replay, with "sorry and native_decide are rejected";
  - small, logged amendments through a critic agent, with changes to trusted assumptions approved by humans.
  [PRIMARY]
- §9: "while proofs are now much cheaper, specifications remain hard. The specification of a nontrivial software artifact is itself a nontrivial software artifact"; "Specifications of widely deployed systems need to be agreed upon by the communities that maintain, analyze and rely on them". [PRIMARY] — [paper PDF](https://deepmind.google/documents/36/Formal_Verification_of_Signal_4.pdf)
- Chaudhuri (DeepMind research scientist and UT Austin professor) to The Register, 10 Nov 2026: "In formal methods, we always had this belief that verification is the hard bit."; "We really believe that the next frontier is not going to be proof but specification in this kind of research."; "It's a system that is fundamentally built for human AI collaboration." [SECONDARY] — [The Register](https://www.theregister.com/ai-and-ml/2026/11/10/google-deepmind-melds-humans-and-ai-agents-to-vet-signals-secure-messaging-techniques/5308625)
- Chaudhuri (outlet not pinned down): "We don't want this sort of vibe world where AI is generating the goals and AI is generating the proofs." The quote is not in The Register's article. [SECONDARY; outlet UNVERIFIED] — [Qodo](https://www.qodo.ai/blog/alphaproof-code-signal-formal-verification/); [SecOpsNews mirror](https://github.com/SecOpsNews/news/issues/76379)
- Microsoft (26 Oct 2026): "developers' attention is shifting from writing code to managing the specifications that guide agents"; "The engineer reviews and approves the properties". It asks openly: "how do we know the specification captures what the system should do rather than simply what it currently does?"; "Can we trust specifications written by AI?" [PRIMARY] — [Microsoft](https://commandline.microsoft.com/agentic-software-engineering-large-scale-code-migration-language-modernization-spec-driven-development/)
- Anthropic (22 Oct 2026):
  - Specifications came from "automatically converting their preexisting compilable test suites into a spec"; for zlib, "we asked Claude to write a formal spec of RFC 1950".
  - The risk: "Claude could make any theorem provable by rewriting the program into one that trivially never crashes", mitigated by penalising and auditing patches; no case is reported.
  - The trusted base is the RISC-V and Linux-process models, "The exact theorem statements that were proved" and the Rocq checker.
  - "'Formally verified' does not mean 'bug-free.'"; "a proof checker can't tell you whether your spec matches reality".
  - The proofs assume "a single-threaded static binary with a fixed memory budget" linked against musl, while most users run x86 or ARM with glibc. A footnote reports "hundreds of mistakes" in ISA reference documentation.
  [PRIMARY] — [Anthropic](https://www.anthropic.com/research/formal-verification). Fermat README: "What no tool can check is that each intermediate theorem means what its name suggests; that is for the reader to judge." [PRIMARY] — [GitHub](https://github.com/anthropics/fermats-last-theorem)
- AWS: Kiro "reviewed every theorem statement, because the kernel can check a proof misaligned with the source code" and proved 70 of 96 candidate properties [PRIMARY] — [Kiro](https://kiro.dev/blog/harness-properties-in-lean/). In AR checks, users review generated policies and label test scenarios [PRIMARY] — [AWS](https://aws.amazon.com/blogs/aws/minimize-ai-hallucinations-and-deliver-up-to-99-verification-accuracy-with-automated-reasoning-checks-now-available/). Cook: teams that "must write precise specifications for verification" "often discover simpler, more elegant solutions" [PRIMARY] — [Amazon Science](https://www.amazon.science/blog/a-decade-of-mathematical-certainty-reflections-on-the-automated-reasoning-group)
- Independent measures of these labs' models on specifications (peer notes):
  - VERINA (v3, 16 Mar 2026): the best model (OpenAI o3) scored 52.3% on specification soundness and completeness, against 72.6% on code correctness — [arXiv](https://arxiv.org/abs/2505.23135).
  - "Two Truths and A Lie?" (3 Sep 2026): "the best-performing Anthropic model detects a median of only 47% of expert-identified issues while false-flagging 11%".
  [INDEPENDENT per peer notes]

### Inferences
- The consensus division of labour: agents draft and test specifications and write all proofs; named humans approve the trusted statements. No lab claims that AI-written specifications can be trusted unreviewed.
- DeepMind's errors in published human analyses show that trust comes from a process (review, vacuity and mutation checks, community agreement), not from who drafts the specification.

### Gaps
- No lab published an autoformalisation error rate for its own specifications. Kiro's 70 of 96 is a proof rate, not an error rate.

## 8. Transition assessment: will model makers offer verification themselves, and with what effect?

### Takeaway
As of 12 Nov 2026, no model maker sells a general formal-verification product for code or chips, apart from AWS's narrow features and the OpenAI–Synopsys joint service (no price or GA date). The evidence points to verification bundled into coding agents and paid for in tokens or seats, and to model makers partnering with chip-tool incumbents rather than replacing their sign-off. Paid proof writing is most exposed; foundry-certified chip engines are least exposed; services firms shift towards specification review.

### Cited Findings
- Intentions:
  - DeepMind wants to verify libsignal releases "before they ship, and also more broadly" — [paper](https://deepmind.google/documents/36/Formal_Verification_of_Signal_4.pdf).
  - Anthropic expects verification to be "as practical as fuzzing" soon — [Anthropic](https://www.anthropic.com/research/formal-verification).
  - Microsoft is "building tools that put formal, interpretable specifications at the center of the software development life cycle" (internal) — [Microsoft](https://commandline.microsoft.com/agentic-software-engineering-large-scale-code-migration-language-modernization-spec-driven-development/).
  - Kiro plans to state features as theorems (internal) — [Kiro](https://kiro.dev/blog/harness-properties-in-lean/).
  [PRIMARY]
- Price points:
  - AR checks: $0.17 per 1,000 text units per policy — [AWS](https://aws.amazon.com/bedrock/pricing/).
  - Kiro: $20–$200 per user per month — [Kiro](https://kiro.dev/pricing/).
  - Fable 5.2: $8/$40 per million tokens — [Anthropic](https://www.anthropic.com/news/claude-fable-and-mythos-5-2); Anthropic's proofs take "hundreds of millions of tokens".
  - C compiler: just under $20,000 — [Anthropic](https://www.anthropic.com/engineering/building-c-compiler).
  - AlphaProof Nexus: a few hundred dollars per solution [SECONDARY].
  - GPT-Synopsys bundles compute, model and licences, with revenue sharing.
  [PRIMARY unless marked]
- Model-maker and chip-tool partnerships, 2025–26 (peer notes; PRIMARY/COMPANY CLAIM):
  - OpenAI–Synopsys GPT-Synopsys (30 Sep 2026) — [Synopsys](https://news.synopsys.com/2026-09-30-OpenAI-and-Synopsys-Announce-GPT-Synopsys-Frontier-Intelligence-to-Revolutionize-Chip-Design)
  - Amazon–Synopsys, $1B+ (30 Sep 2026) — [Synopsys](https://news.synopsys.com/2026-09-30-Synopsys-and-Amazon-Announce-Strategic,-Multi-year-IP-Agreement-for-Custom-Silicon-Collaboration-Also-Extends-to-Cloud-and-AI-Powered-Engineering)
  - Synopsys–AMD–Microsoft (27 Jul 2026) — [Synopsys](https://news.synopsys.com/2026-07-27-Synopsys-Advances-Agentic-AI-Chip-Design-with-AMD-and-Microsoft)
  - Nvidia–Synopsys $2B (1 Dec 2025) — [Synopsys](https://news.synopsys.com/2025-12-01-NVIDIA-and-Synopsys-Announce-Strategic-Partnership-to-Revolutionize-Engineering-and-Design)
  - Synopsys–NVIDIA autonomous design-verification workflow (26 Jul 2026; "up to 50X faster time-to-validated RTL", COMPANY CLAIM)
  - Cadence ChipStack with NVIDIA (Computex 2026)
  - Siemens Questa One Agentic Toolkit (27 Feb 2026), which works with GitHub Copilot and Claude Code and is "not positioned as a path to fully autonomous IC verification" — [Siemens](https://news.siemens.com/fr-fr/questa-one-agentic-ai-toolkit/)
- Incumbents' sign-off moat: TSMC's certification grids (as of 1 Oct 2026) list only Cadence, Synopsys and Siemens [PRIMARY per peer notes] — [TSMC](https://www.tsmc.com/english/dedicatedFoundry/oip/eda_alliance). GPT-Synopsys calls Synopsys tools "ground-truth" [PRIMARY].
- Market sensitivity: Synopsys fell 2.5% and Cadence 4.5% on the Anthropic chip-team report (3 Nov 2026), and Chinese EDA stocks fell on the Kimi K3 episode (17 Jul 2026; causation not established). [SECONDARY, peer notes]
- Start-ups as complements: Theorem supplies semantics to Anthropic [PRIMARY]; Harmonic's Aristotle runs inside Claude Code or Codex over MCP (3 Nov 2026) [COMPANY CLAIM, peer notes] — [Harmonic](https://harmonic.fun/news/ibex-mul-div-verification)

### Inferences

| Organisation | Sells verification to outsiders | Gives it away or bundles it | Buys verification (tools, models, services) | Net role |
|---|---|---|---|---|
| Google / DeepMind | No (AlphaEvolve is an optimiser) | Open Signal specifications and proofs; plans free libsignal release checks | Commercial formal tools for TPUs; Claude for specifications | Free competitor and customer |
| Microsoft | No product found | Z3 (MIT), Verus/F* research, tlalink | Synopsys agentic chip design with AMD | Free upstream supplier and customer |
| Anthropic | No; sells tokens others use for proofs | Published Rocq and Lean proofs | Theorem collaboration; reportedly sought EDA data | Proof-engine supplier and free competitor |
| OpenAI | Jointly, via GPT-Synopsys (no GA date) | Lean proofs of maths results | Licenses Synopsys tools | Incumbent's channel partner and customer |
| AWS | AR checks, Access Analyzer, AgentCore Policy, Kiro requirements analysis | Funds Lean FRO; bundles features in Kiro | Synopsys $1B+; Claude for own proofs | All three |
| Meta / Nvidia / Chinese labs | No | Meta: LKV; Chinese labs: open-weight provers | Nvidia: EDA customer and investor | Free tooling or investor |

- Likelihood and timing (my judgement): bundling into coding agents is likely, and the parts already exist (Kiro, Claude skills, MCP links to Aristotle). It could plausibly be common for selected properties in 2027. A standalone, priced service from DeepMind or Anthropic is less likely in the near term: none has been announced, and the frameworks are unreleased.
- (a) Proof start-ups face falling prices for proof writing (open weights, open artefacts, 40% fewer tokens per model generation on Anthropic's tasks). Start-ups that own semantics (Theorem), specification workflows, trusted checkers or domain models remain complements. The labs themselves use such assets (Theorem's semantics, Lean FRO's comparator).
- (b) Synopsys, Cadence and Siemens: no model maker has a foundry-certified engine, and the partnerships route agents through the incumbents' engines. The risk is to pricing and to ownership of the agent interface (for example OpenAI's revenue share), not to the verdict. Share moves show that the market treats model makers as a latent threat.
- (c) Services firms: five people over four weeks, and Microsoft's "human attention" framing, imply fewer billable hours for writing proofs and test benches, and more demand for reviewing, approving and auditing specifications, where every lab keeps humans.

### Gaps
- No timeline, price or service-level commitment for a model-maker verification product was found. No partnership between Google or Anthropic and a chip-tool vendor was confirmed.

## 9. Exposure: is verification material to the listed parents? Private status of Anthropic and OpenAI

### Takeaway
For Alphabet, Microsoft and Amazon, verification is strategically useful but immaterial to value; none reports it as a revenue line. Anthropic is private but on its IPO roadshow. OpenAI is private and says it will not list this year.

### Cited Findings
- Alphabet: AlphaProof Code is research; the nearest Cloud product, AlphaEvolve (generally available July 2026), optimises code. Capex was $51.4B in the third quarter of 2026, with $195–205B guided for 2026 [PRIMARY per lead notes] — [Google blog, Q3 2026](https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q3-2026/). Google markets Gemini 4 Carbon for "long-horizon engineering and cybersecurity defense" [PRIMARY per lead notes] — [Google blog, Oct 2026 recap](https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-october-2026/). Inference: not material to Alphabet's value; possibly to how its coding and cyber products are perceived.
- Microsoft: no verification product. Formal methods are an internal productivity lever (the 400-million-line migration), and Z3 is free [PRIMARY]. Inference: immaterial as revenue, but relevant to GitHub's and Azure's story of trustworthy AI coding.
- Amazon: AWS's automated-reasoning features serve "millions of AWS customers" by the company's account [COMPANY CLAIM] — [Amazon Science](https://www.amazon.science/blog/a-decade-of-mathematical-certainty-reflections-on-the-automated-reasoning-group). Revenue is undisclosed and unit prices are small. Amazon is also a $1B+ Synopsys customer. Inference: strategically important to AWS's security and agent-trust positioning (AgentCore Policy), not separately material.
- Anthropic: S-1 filed 26 Oct 2026, amended 2 Nov (lead notes). The roadshow launched 10 Nov 2026: listing applied for on the Nasdaq Global Select Market as "ANT"; "825,000,000 shares of Class A common stock" at "between $70.00 and $78.00 per share". No valuation or pricing date is given. Gross proceeds would be $57.8–64.4B at the range (my arithmetic). [PRIMARY] — [Anthropic, 10 Nov 2026](https://www.anthropic.com/news/roadshow-launch); [S-1 announcement](https://www.anthropic.com/news/s1-sec)
- OpenAI: Fortune (Alyson Shontell, 5 Oct 2026) calls it "a for-profit public benefit corporation worth $730 billion and rising", reportedly weighing a round near $1.5 trillion. Altman: "this right now would be an ill-advised moment to go public". Microsoft's stake is not discussed. [SECONDARY] — [Fortune](https://fortune.com/2026/10/05/can-superintelligence-be-controlled-sam-altman-openai-ai-safety-doomsday-risk-delayed-ipo/)

### Inferences
- Listed exposure to "model maker as verification competitor" is heavily diluted in Alphabet, Microsoft and Amazon. A completed Anthropic listing would add the first listed pure model maker whose models power third-party verification. This is analysis, not advice.

### Gaps
- None of the parents discloses verification revenue. Anthropic's final pricing and OpenAI's next round were pending at the research date.

## 10. Closing lists

### What I could not verify
- Google: whether the blog ever said "three million lines"; AlphaProof Code's compute cost and any productisation plan; the original outlet of the "vibe world" quote; the AlphaProof Nature (2025) and AlphaProof Nexus Science (Oct 2026) papers; AlphaChip's 2026 role; AlphaEvolve's exact GA date (9 or 10 July 2026).
- Microsoft: Dafny's and F*'s Microsoft Research origins, and an explicit source that Lean began at Microsoft Research; any GitHub or Azure verification product.
- OpenAI: Aardvark and GPT-6 Cyber (403 error); verification acquisitions; Jalapeño's deployment and how far AI was used in its design.
- AWS: AR checks updates in 2026 and the basis of the "up to 99%" figure; Kiro's requirements-analysis launch date; any explicit "neurosymbolic" wording by Cook.
- Others: Huawei's verified kernels; Alibaba and Ant provers; work at Apple, xAI and Mistral; Nvidia's internal formal methods; The Information's chip-team report (paywalled); Seed-Prover's weights and dates.

### Where current evidence contradicts the background views
- "Machine-checked proof has become cheap." Broadly supported: DeepMind says proof is no longer the bottleneck, and Anthropic's tokens per proof fell about 40% in one generation. But cheapness is relative to labour, not absolute:
  - "hundreds of millions of tokens" per proof;
  - multi-hour builds needing 15–34 GiB of RAM, with DeepMind calling compute latency "an issue" and noting that source-level proofs save compute;
  - Kiro proved 70 of 96 candidate properties;
  - cheap results so far are for narrow properties (no crash) or come with heavy expert direction.
- "The scarce parts are the specification and the trusted sign-off." Supported for specifications, but labs are automating specification drafting (fuzz-derived specifications, agent-inferred TLA+, specification-writer agents). What remains scarce is approving and agreeing specifications and trusted machine semantics (ISA and OS models). In software, trusted sign-off is supplied free by open kernels (Lean, Rocq) and non-profit tools (comparator, nanoda).
- "Verification tools own the verdict." Contradicted for software: the labs' verdicts rest on open-source checkers maintained by non-profits, plus human approval, not on commercial vendors. Consistent for chips: GPT-Synopsys keeps Synopsys as "ground-truth", and only the big three hold TSMC certification.
- "Value moves from writing proofs to writing specifications." Supported in direction (DeepMind's "next frontier is... specification"; Microsoft; AWS). But agents now draft specifications too, so value is more likely to settle on whoever is trusted to review, approve and maintain specifications, and on whoever owns machine semantics.

### Sources with dates
- DeepMind and Google: [blog, 10 Nov 2026](https://deepmind.google/blog/introducing-alphaproof-code/); [paper, 10 Nov 2026](https://deepmind.google/documents/36/Formal_Verification_of_Signal_4.pdf); [code-verification repo, 26 Oct 2026](https://github.com/google-deepmind/code-verification); [AlphaEvolve, May 2025](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/); [AlphaEvolve on Cloud, Jul 2026](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/alphaevolve-on-cloud/); [Cloud preview, Dec 2025](https://cloud.google.com/blog/products/ai-machine-learning/alphaevolve-on-google-cloud); [AlphaChip, Sep 2024](https://deepmind.google/blog/how-alphachip-transformed-computer-chip-design/); [AlphaProof Nexus, May 2026](https://arxiv.org/pdf/2605.22763); [The Register, 10 Nov 2026](https://www.theregister.com/ai-and-ml/2026/11/10/google-deepmind-melds-humans-and-ai-agents-to-vet-signals-secure-messaging-techniques/5308625); [Qodo, Nov 2026](https://www.qodo.ai/blog/alphaproof-code-signal-formal-verification/)
- Microsoft: [Command Line, 26 Oct 2026](https://commandline.microsoft.com/agentic-software-engineering-large-scale-code-migration-language-modernization-spec-driven-development/); [Z3, read 12 Nov 2026](https://github.com/Z3Prover/z3); [VeruSAGE, undated](https://www.microsoft.com/en-us/research/publication/verusage-a-study-of-agent-based-verification-for-rust-systems/); [TechRadar, Dec 2025](https://www.techradar.com/computing/cloud-computing/microsoft-engineer-clarifies-speculation-around-plans-to-eliminate-c-c-languages-by-2030)
- Anthropic: [launch post, 9 Nov 2026](https://www.anthropic.com/news/claude-fable-and-mythos-5-2); [formal verification, 22 Oct 2026](https://www.anthropic.com/research/formal-verification); [C compiler, 5 Feb 2026](https://www.anthropic.com/engineering/building-c-compiler); [Fermat repo, 2026](https://github.com/anthropics/fermats-last-theorem); [roadshow, 10 Nov 2026](https://www.anthropic.com/news/roadshow-launch)
- OpenAI: [openai/math, read 12 Nov 2026](https://github.com/openai/math); [GPT-Synopsys, 30 Sep 2026](https://news.synopsys.com/2026-09-30-OpenAI-and-Synopsys-Announce-GPT-Synopsys-Frontier-Intelligence-to-Revolutionize-Chip-Design); [TechCrunch, 24 Jun 2026](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/); [Fortune, 5 Oct 2026](https://fortune.com/2026/10/05/can-superintelligence-be-controlled-sam-altman-openai-ai-safety-doomsday-risk-delayed-ipo/)
- AWS: [AR checks GA, 6 Aug 2025](https://aws.amazon.com/blogs/aws/minimize-ai-hallucinations-and-deliver-up-to-99-verification-accuracy-with-automated-reasoning-checks-now-available/); [Bedrock pricing, read 12 Nov 2026](https://aws.amazon.com/bedrock/pricing/); [Cook, 11 Aug 2026](https://www.amazon.science/blog/a-decade-of-mathematical-certainty-reflections-on-the-automated-reasoning-group); [Lean FRO investment, 26 Jul 2026](https://www.amazon.science/news/amazon-is-investing-in-the-lean-focused-research-organization); [Kiro pricing, read 12 Nov 2026](https://kiro.dev/pricing/); [Kiro Lean harness, 2 Nov 2026](https://kiro.dev/blog/harness-properties-in-lean/); [Lean FRO About, read 12 Nov 2026](https://lean-lang.org/fro/about)
- Others: [lean_kernel_verify, Oct 2026](https://github.com/facebookresearch/lean_kernel_verify); [DeepSeek-Prover-V2, Apr 2025](https://github.com/deepseek-ai/DeepSeek-Prover-V2); [Seed-Prover, 2025](https://github.com/ByteDance-Seed/Seed-Prover); [LongCat-Flash-Prover, Mar 2026](https://hf.co/meituan-longcat/LongCat-Flash-Prover); [The Information, 3 Nov 2026](https://www.theinformation.com/briefings/synopsys-cadence-shares-drop-4-information-report); [Investing.com, 17 Jul 2026](https://www.investing.com/news/stock-market-news/cadence--synopsys-slide-as-kimi-k3-designs-chip-in-48h-using-no-proprietary-eda-4798775)
