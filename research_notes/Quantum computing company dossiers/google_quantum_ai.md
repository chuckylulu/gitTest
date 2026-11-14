# Google Quantum AI (Alphabet): organization, roadmap, finances, partners, people, legal, and the science, fact file as of 14 November 2026

Conventions used below:
- **[CC]** means a company-controlled source: a Google or Alphabet blog, website, filing, or a Google-authored paper, including papers with some outside co-authors.
- **[IND]** means a source independent of Google: journalists, outside scientists, government agencies, or counterparties. Counterparties are labelled as such.
- A leading date **[YYYY-MM-DD]** is the date of the source or event. Anything dated before 2026-01-01 is older information and may have been superseded.
- **"Via search summary"** means the detail was seen only in a search-engine result summary, not in a page I fetched and read. Treat it as lower confidence.
- **Research constraint:** the shared web-search quota for this session ran out partway through. Items that could not be checked are listed under each section's Gaps.

---

## 1. Organization and stage: where Quantum AI sits, hardware, access, software

### Takeaway
Google Quantum AI is a research division of Google, based in Goleta/Santa Barbara, California. Hartmut Neven founded it in 2012, and Google's own 2026 bylines place it inside Google Research. Alphabet does not name it in any reporting segment.

Its flagship processor is still Willow, a 105-qubit superconducting transmon chip announced 2024-12-09. I found no Google announcement of a successor chip as of 2026-11-14. In 2025–26 Google acquired Atlantic Quantum (Oct 2025) and started a neutral-atom hardware program in Boulder, Colorado (Mar 2026).

I found no commercial sale or rental of Google's processors. The only external access found is grant-style research access through the UK's National Quantum Computing Centre (NQCC).

### Cited Findings
**Placement and organization**
- [accessed 2026-11-14] Wikipedia's description of the organization:
  - Google Quantum AI is a "research division of Google" (parent Google LLC), headquartered in Goleta, California.
  - It has three divisions: quantum hardware, quantum algorithms and quantum error correction.
  - It was founded in 2012 by Hartmut Neven.
  - The Santa Barbara-area site was chosen in 2013, and Google recruited UCSB professor John Martinis and his team in 2014.
  - Source: [Wikipedia, "Google Quantum AI"](https://en.wikipedia.org/wiki/Google_Quantum_AI) [IND, secondary].
- [2026-01-13] Google's own byline describes Quantum AI staff as "Research Scientists, Google Research, Google Quantum AI team" — [Google Research blog, Eickbusch & Morvan, "Dynamic surface codes open new avenues for quantum error correction", 2026-01-13](https://research.google/blog/dynamic-surface-codes-open-new-avenues-for-quantum-error-correction/) [CC]
- [2024-12-09] Neven states he founded Google Quantum AI in 2012. Willow was built in Google's "new" fabrication facility in Santa Barbara, "one of only a few facilities in the world built from the ground up for this purpose" — [Google blog, Neven, "Meet Willow, our state-of-the-art quantum chip", 2024-12-09, page shows last updated 2025-06-12](https://blog.google/technology/research/google-willow-quantum-chip/) [CC]
- [2021-05-18, older] The Santa Barbara campus houses Google's "first quantum data center", quantum processor chip fabrication facilities and hardware research labs — [Google blog, Erik Lucero (Lead Engineer), "Unveiling our new Quantum AI campus", 2021-05-18](https://blog.google/technology/ai/unveiling-our-new-quantum-ai-campus/) [CC]

**2025–26 structural changes**
- [2026-03-24] Neutral-atom expansion, announced by Google:
  - Google Quantum AI is adding neutral-atom quantum computing to its superconducting program.
  - Adam Kaufman (JILA Fellow; CU Boulder physics faculty) will lead "a growing neutral atoms hardware team at Google" in Boulder, Colorado.
  - Stated rationale: neutral atoms are "easier to scale in qubit count", while superconducting processors are "easier to scale in circuit depth".
  - Google says neutral-atom arrays have reached about 10,000 qubits but have cycle times measured in milliseconds.
  - The program has three pillars: QEC, modeling and simulation, and experimental hardware.
  - Headcount and investment were not disclosed.
  - Source: [Google blog, Neven, "Building superconducting and neutral atom quantum computers", 2026-03-24](https://blog.google/innovation-and-ai/technology/research/neutral-atom-quantum-computers/) [CC]
- [2025-10-02] Gunderson Dettmer says it "represented client Atlantic Quantum in its acquisition by Google". Terms were not disclosed. Atlantic Quantum is an MIT-founded startup whose modular chip stack puts qubits and superconducting control electronics together in the cold stage — [Gunderson Dettmer, "Gunderson Dettmer Represented Atlantic Quantum in its Acquisition by Google", 2025-10-02](https://www.gunder.com/en/news-insights/client-news/gunderson-dettmer-represented-atlantic-quantum-in-its-acquisition-by-google) [IND, seller's counsel]
- [2025-10-03] Trade-press account of the Atlantic Quantum deal:
  - Google's announcement said Atlantic Quantum "joins" Google Quantum AI and did not use the word "acquisition".
  - Neven said the chip stack "will help Google Quantum AI more effectively scale our superconducting qubit hardware".
  - The company was founded in 2021 out of MIT.
  - CEO Bharath Kannan and co-founder/CTO Simon Gustavsson are joining. Listed founders include Will Oliver, Simon Gustavsson and Jonas Bylander.
  - Source: [The Quantum Insider, "Atlantic Quantum Joins Google Quantum AI", 2025-10-03](https://thequantuminsider.com/2025/10/03/atlantic-quantum-joins-google-quantum-ai/) [IND]
  - **Contradiction (wording):** Google says the company "joins"; the seller's counsel says "acquisition by Google".

**Hardware and published specifications**
- [2019, older] Sycamore figures:
  - The 2019 supremacy experiment used a 53-qubit, depth-20 random circuit with a predicted total fidelity of 0.2% — [IBM Research blog, Pednault, Maslov, Gunnels, Gambetta, "On 'Quantum Supremacy'", 2019-10-22](https://www.ibm.com/quantum/blog/on-quantum-supremacy) [IND, competitor]
  - The Sycamore processor had 54 qubits and 88 tunable couplers. The cryostats were "about the size of three household refrigerators" and ran at about 10 mK — [Google blog, 2021-05-18](https://blog.google/technology/ai/unveiling-our-new-quantum-ai-campus/) [CC]
- [2024-12-09] The Willow spec sheet (two different chips) gives:

  | Metric | Chip 1 (QEC) | Chip 2 (RCS) |
  |---|---|---|
  | Qubits (system) | 105 | 105 |
  | Average connectivity (system) | 3.47 (4-way typical) | 3.47 (4-way typical) |
  | Single-qubit gate error | 0.035% ± 0.029% | 0.036% ± 0.013% |
  | Two-qubit gate error | 0.33% ± 0.18% (CZ) | 0.14% ± 0.052% (iSWAP-like) |
  | Measurement error | 0.77% ± 0.21% | 0.67% ± 0.51% |
  | Reset options | Multi-level reset; leakage removal (\|2⟩ only) | Multi-level reset; leakage removal (\|2⟩ only) |
  | T1 | 68 ± 13 µs | 98 ± 32 µs |
  | Throughput | 909,000 QEC cycles/s (surface-code cycle 1.1 µs) | 63,000 circuit repetitions/s |
  | Application performance | Λ3,5,7 = 2.14 ± 0.02 | 103 qubits, depth 40, XEB fidelity 0.1% |
  | Time vs classical | — | "5 minutes vs. 10^25 years" |

  - Errors are from randomized benchmarking ("average error").
  - The chips' T1 values differ because of a tradeoff between shielding-optimized qubit geometry and coherence.
  - Source: [Google Quantum AI, "Willow Spec Sheet", published 2024-12-09](https://quantumai.google/static/site-assets/downloads/willow-spec-sheet.pdf) [CC]
- [2024-12-09] The Willow blog says T1 times are "approaching 100 µs", about 5x the previous generation — [Google blog, 2024-12-09](https://blog.google/technology/research/google-willow-quantum-chip/) [CC]
  - **Nuance:** this matches the RCS chip (98 µs). The QEC chip was 68 µs, per the spec sheet above.
- [2026-03-24] Google says its superconducting circuits have run "millions of gate and measurement cycles" at about 1 µs per cycle. Its next superconducting goal is "computing architectures with tens of thousands of qubits" — [Google blog, 2026-03-24](https://blog.google/innovation-and-ai/technology/research/neutral-atom-quantum-computers/) [CC]
- [2026] I found no Google-announced successor to Willow.
  - One secondary site, via search summary, mentions a rumored 500–1,000-qubit successor "by late 2026 or early 2027" without a primary source — [Tech-Insider, "Google Quantum Computing 2026: Neutral Atom Pivot and $3B Market"](https://tech-insider.org/google-quantum-computing-neutral-atom-willow-2026/) [IND, low reliability, unverified].
  - **Contradiction (Willow date):** Wikipedia dates Willow's announcement to 2025 ([Wikipedia](https://en.wikipedia.org/wiki/Google_Quantum_AI)). Google's post is dated 2024-12-09 and shows "last updated 2025-06-12" ([Google blog](https://blog.google/technology/research/google-willow-quantum-chip/)).

**Access: who gets processor time, on what terms**
- [2025-12-12] NQCC–Google call for Willow access:
  - "UK researchers and research consortia" may propose experiments on Willow.
  - Selected teams design and run experiments with Google and NQCC experts.
  - The NQCC offers research grants to fund researcher time.
  - Proposals are assessed on technical feasibility on Willow and potential for high impact, for example a path to beyond-classical applications.
  - The program builds on the UK–US Technology Prosperity Deal and a Google Cloud–DSIT collaboration agreement.
  - Cost to researchers and number of projects are not stated.
  - Source: [NQCC, "NQCC and Google Quantum AI launch new initiative to accelerate quantum science in the UK", 2025-12-12](https://www.nqcc.ac.uk/updates/nqcc-and-google-quantum-ai-launch-new-initiative-to-accelerate-quantum-science-in-the-uk/) [IND, partner government lab]
- [2026-05-28] First award (via search summary):
  - King's College London won, for a project on quantum analogues of neurons with UCL's Dr Chris Timmermann.
  - The NQCC called it the first time Google has partnered with a British government institution to give researchers Willow access.
  - Industry partners may join, but receive no grant funding.
  - Sources: [NQCC press release, 2026-05-28](https://www.nqcc.ac.uk/wp-content/uploads/2026/05/Press-release_NQCC-and-Google-Quantum-AI-award-Kings-College-London_28May2026_Final.pdf); [The Quantum Insider, 2026-05-28](https://thequantuminsider.com/2026/05/28/kings-college-london-awarded-access-to-googles-willow-processor-through-nqcc-initiative/) [IND]

**Software**
- [accessed 2026-11-14] The quantumlib GitHub organization lists these repositories, all with commits in Oct–Nov 2026 — [GitHub, quantumlib organization page](https://github.com/quantumlib) [CC]:

  | Repository | Description | Language | Stars | Last updated |
  |---|---|---|---|---|
  | Cirq | Python framework for creating, editing and running NISQ circuits | Python | 5,101 | 2026-11-11 |
  | Stim | Fast stabilizer circuit library | C++ | 848 | 2026-10-29 |
  | qsim | State-vector simulator | C++ | 716 | 2026-11-03 |
  | OpenFermion | Electronic-structure algorithms | Python | 1,751 | 2026-11-11 |
  | Qualtran | Expressing and analyzing fault-tolerant algorithms | Python | 450 | 2026-11-12 |
  | ReCirq | Applications and experiments built on Cirq | Python | 309 | — |
  | tesseract-decoder | Decoder | C++ | 122 | — |
  | chromobius | Decoder | Python | 48 | — |

- [2026-10-23] kickmix, part of Qualtran, is a randomized fuzz-testing verifier for circuits. Google claims it checks 60 billion gates per second on one CPU core and says it gives approximate correctness with high confidence, not exact equivalence — [The Quantum Insider, "Google Launches $150,000 AI Competition to Reduce Quantum Computing Demands", 2026-10-23](https://thequantuminsider.com/2026/10/23/google-launches-150000-ai-competition-to-reduce-quantum-computing-demands/) [IND, reporting company claims]

### Inferences
- Organizationally, Quantum AI sits in Google (Google Research per 2026 bylines), not in the Other Bets legal entities. Its cost placement in Alphabet's segments still cannot be determined; see Section 4.
- Since Willow, Google's hardware news has come from an acquisition (Atlantic Quantum: cryogenic integration of control electronics) and a second modality (neutral atoms), not from a larger published chip. The largest Google processor with published specs is still 105 qubits as of 2026-11-14.

### Gaps
- Not found:
  - The number of Willow-class chips or systems in operation, and their uptime or availability.
  - Specs or timing of any Willow successor.
  - Atlantic Quantum's deal value.
  - Total headcount of Google Quantum AI, and the size of the Boulder team.
- Not verified this session:
  - Whether Google's Quantum Computing Service (historically an allow-list access channel via Google Cloud) still operates, and on what terms.
  - Specs of earlier chips such as Bristlecone and Foxtail; the Wikipedia infobox lists them but they were not checked.

---

## 2. Roadmap: six milestones, what Google has declared achieved, and executive timelines

### Takeaway
Google has declared two milestones achieved:
- Milestone 1, beyond-classical (2019).
- Milestone 2, the QEC prototype (Feb 2023), strengthened by Willow's below-threshold result (Dec 2024).

As recently as 2025-10-22 and 2026-01-13, Google described Milestone 3 (a long-lived logical qubit, under 1 error per 10^6 QEC cycles) as the next milestone. I found no Google announcement through 2026-11-14 that Milestone 3 has been reached.

Executive timelines in 2025–26:
- Neven and Julian Kelly: real-world applications "within five years" (said in 2025).
- Neven (Mar 2026): "commercially relevant" superconducting quantum computers "by the end of this decade".
- Pichai (Feb 2025): "useful" quantum computers 5 to 10 years away.

### Cited Findings
**Roadmap structure**
- [2021-05-18, older] Google's 2021 description of the path:
  - Build an error-corrected logical qubit, encoding one logical qubit using "1,000 physical qubits".
  - Build a "quantum transistor" from two error-corrected logical qubits.
  - Tile hundreds to thousands of these into "1,000,000 physical qubits that work in concert inside a room-sized error-corrected quantum computer".
  - Goal: "Within the decade, Google aims to build a useful, error-corrected quantum computer". The post does not say "2029".
  - Source: [Google blog, Lucero, 2021-05-18](https://blog.google/technology/ai/unveiling-our-new-quantum-ai-campus/) [CC]
- [2023-02-22, older] Milestone 2 declared:
  - Google said it had reached the "second milestone", a prototype logical qubit.
  - Results: distance-3 (17 qubits) ε3 = 3.028% per cycle; distance-5 (49 qubits) ε5 = 2.914%; Λ3,5 = 1.04, about a 4% improvement at 5σ.
  - Stated target for the next era: logical error ≤1 in 10^6 per QEC cycle, described as "still a few years out".
  - Projection: Λ = 4 with distance-17 (577 physical qubits of sufficient quality) would reach 10^-6.
  - Sources: [Google Research blog, Neven (VP of Engineering) & Kelly (Director of Quantum Hardware), "Suppressing quantum errors by scaling a surface code logical qubit", 2023-02-22](https://research.google/blog/suppressing-quantum-errors-by-scaling-a-surface-code-logical-qubit/) [CC]; [Google Quantum AI, "Milestone 2" page, undated](https://quantumai.google/qecmilestone) [CC]
- [2024-12-09] After Willow, Google named the next challenge as "a first 'useful, beyond-classical' computation" on today's chips, with no target date — [Google blog, 2024-12-09](https://blog.google/technology/research/google-willow-quantum-chip/) [CC]
- [2025-10-22] Google named "Milestone 3 on our quantum hardware roadmap, a long-lived logical qubit" as the next goal — [Google blog, Neven & Smelyanskiy, "Our Quantum Echoes algorithm is a big step toward real-world applications for quantum computing", 2025-10-22](https://blog.google/innovation-and-ai/technology/research/quantum-echoes-willow-verifiable-quantum-advantage/) [CC]
- [2026-01-13] Google again named the next milestone as "a long-lived logical qubit" with "an error rate below one error per million QEC cycles" — [Google Research blog, 2026-01-13](https://research.google/blog/dynamic-surface-codes-open-new-avenues-for-quantum-error-correction/) [CC]
- [2026-03-24] Achievements Google cites: beyond-classical performance, error correction and "verifiable quantum advantage". Statement: "We are now increasingly confident that commercially relevant quantum computers based on superconducting technology will become available by the end of this decade" — [Google blog, 2026-03-24](https://blog.google/innovation-and-ai/technology/research/neutral-atom-quantum-computers/) [CC]
- [2026-10-15] The magic-state-cultivation post names no roadmap milestone. It refers only to "building a useful, error-corrected quantum computer" — [Google blog, Rosenfeld & Gidney, "Bringing the magic: Google breaks open a bottleneck in quantum computing", 2026-10-15](https://blog.google/innovation-and-ai/models-and-research/quantum-computing/magic-state-cultivation-quantum-computing/) [CC]
- [2026-09-22] **Unverified, low reliability:** an article claims Google "achieves new milestone in logical qubit stability", published in Physical Review Letters. It gives no logical error rate, code distance, chip name, DOI or quotes — [Science World Report, Peter Smith, 2026-09-22](http://www.scienceworldreport.com/articles/62276/20260922/google-quantum-ai-achieves-new-milestone-in-logical-qubit-stability.htm) [IND, low reliability]. No Google source found corroborates a Milestone 3 claim.

**Executive timelines (chronological)**

| Date | Who | Statement | Source |
|---|---|---|---|
| 2019-10 (older) | Pichai | Useful applications "a decade away" | Via search summary; not fetched: [MIT Technology Review interview](https://www.technologyreview.com/s/614608/google-ceo-quantum-supremacy-interview-with-sundar-pichai/) [IND] |
| 2025-02-05 | Neven (to Reuters) | "We're optimistic that within five years we'll see real-world applications that are possible only on quantum computers" | [The Quantum Insider, "Google Quantum AI Head Sees Commercial Quantum Within Five Years", 2025-02-05](https://thequantuminsider.com/2025/02/05/google-quantum-ai-head-sees-commercial-quantum-within-five-years/) [IND, reporting] |
| 2025-02-12 | Pichai | "Useful" quantum computers 5 to 10 years away (headline). Via search summary, at the World Governments Summit in Dubai he likened quantum to "AI in the 2010s" | [Bloomberg, "Google CEO Sees 'Useful' Quantum Computers 5 to 10 Years Away", 2025-02-12](https://www.bloomberg.com/news/articles/2025-02-12/google-ceo-sees-useful-quantum-computers-5-to-10-years-away) [IND] |
| 2025-03-25 | Julian Kelly, director of hardware (to CNBC) | "We think we're about five years out from a real breakout" | [The Quantum Insider, "Google Executive Says Quantum Applications Could Arrive in Five Years", 2025-03-26](https://thequantuminsider.com/2025/03/26/google-executive-says-quantum-applications-could-arrive-in-five-years/) [IND, reporting] |
| 2025-10-22 | Neven | "optimistic that within five years, we will see real-world applications" | [IEEE Spectrum, Charles Q. Choi, "Google's New Quantum Algorithm May Actually Be Useful", 2025-10-22](https://spectrum.ieee.org/quantum-echoes) [IND] |
| 2025, date unverified | Pichai | Commercially viable quantum computing "a few years" away (headline only). Search summary attributes it to Dreamforce 2025, with a remark that cryptography must adapt within 3–5 years | [ITPro, Rory Bathgate](https://www.itpro.com/technology/sundar-pichai-thinks-commercially-viable-quantum-computing-is-just-a-few-years-away) [IND] |
| Late 2025, unverified | Pichai (BBC Newsnight) | Quantum is "roughly at the stage AI was five years ago"; fully error-corrected large-scale machines "a decade or more" away | Via search summary; page returned 403: [DatacenterDynamics](https://datacenterdynamics.com/en/news/google-ceo-practical-quantum-computers-likely-still-a-decade-away) [IND] |
| 2026-03-24 | Neven | "commercially relevant" superconducting quantum computers "by the end of this decade" | [Google blog, 2026-03-24](https://blog.google/innovation-and-ai/technology/research/neutral-atom-quantum-computers/) [CC] |
| 2026-10-28 | Pichai (Q3 2026 earnings remarks) | Says "We demonstrated 'magic state cultivation' for the first time in quantum computing"; no timeline given | [Google blog, "Q3 2026 earnings call: Remarks from our CEO", 2026-10-28](https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q3-2026/) [CC] |

**External yardstick: DARPA QBI**
- [2025-09-09] Google says it was selected for DARPA's Quantum Benchmarking Initiative, which aims to determine whether any approach "can lead to a utility-scale, fault-tolerant computer by the year 2033". The post does not state the stage — [Google blog, Neven, post on DARPA QBI selection, 2025-09-09](https://blog.google/innovation-and-ai/technology/research/google-quantum-ai-selected-darpa-qbi/) [CC]
- [list current as of 2026-10-08] DARPA lists Google Quantum AI in Stage A only — [DARPA, Quantum Benchmarking Initiative program page](https://www.darpa.mil/research/programs/quantum-benchmarking-initiative) [IND]

### Inferences
- Gap to Milestone 3 (my arithmetic, assuming constant Λ and no error floor):
  - Willow's best logical error per cycle (distance-7: 1.43×10^-3) is about 1,430× above the Milestone 3 target of 10^-6.
  - At the measured Λ = 2.14, closing that gap takes about 9.5 more distance steps of +2, i.e. distance ≈ 27.
  - A rotated surface code at distance 27 needs about 2d²−1 ≈ 1,457 physical qubits per logical qubit.
  - Google's 2023 projection was distance 17 and 577 qubits, assuming Λ = 4.
- Since Feb 2025, the "about five years" statements point to roughly 2030. Neven's Mar 2026 "end of this decade" is consistent with the 2021 "within the decade" goal.
- The wording has shifted: 2021 said a "useful, error-corrected quantum computer"; 2026 says "commercially relevant quantum computers based on superconducting technology".

### Gaps
- The official roadmap page ([quantumai.google/roadmap](https://quantumai.google/roadmap)) could not be machine-read; its content appears to be JavaScript- or image-rendered. The formal names and targets of Milestones 4–6 (logical gate; engineering scale-up; large error-corrected computer) were not verified this session beyond the 2021 blog's narrative.
- I found no Google statement giving a date for Milestone 3.
- The Sept 2026 "logical qubit stability" claim has no primary source.
- Exact Pichai quotes and venues from late 2025 are unverified.

---

## 3. Milestones met or missed versus earlier stated timelines

### Takeaway
Google has mostly avoided hard dated interim milestones, so few explicit "misses" can be documented. The closest dated interim target is from the Feb 2023 post: 10^-6 logical error was "still a few years out". As of 2026-11-14, about 3 years 9 months later, it has not been announced as achieved.

The end-of-decade goal (2021) is still the stated target and has not lapsed. Measured Λ values (1.56–2.15) sit below the Λ = 4 that Google's 2023 projection assumed. Google's own researchers said the Quantum Echoes molecular application was "not beyond classical yet".

### Cited Findings
| Stated goal (date stated) | Status as of 2026-11-14 | Sources |
|---|---|---|
| Beyond-classical computation (Milestone 1) | Claimed Oct 2019 (200 s vs ~10,000 years on Summit). Later challenged and classically simulated; see Section 8. | [IEEE Spectrum, 2025-10-22](https://spectrum.ieee.org/quantum-echoes) [IND]; [IBM, 2019-10-22](https://www.ibm.com/quantum/blog/on-quantum-supremacy) [IND]; [Pan, Chen & Zhang, PRL 129, 090502 (2022), arXiv:2111.03011](https://arxiv.org/abs/2111.03011) [IND] |
| QEC prototype (Milestone 2) | Declared Feb 2023 (Λ3,5 = 1.04). Below threshold with Willow, Dec 2024 (Λ = 2.14 ± 0.02). | [Google Research blog, 2023-02-22](https://research.google/blog/suppressing-quantum-errors-by-scaling-a-surface-code-logical-qubit/) [CC]; [Acharya et al. / Google Quantum AI, "Quantum error correction below the surface code threshold", arXiv:2408.13687 (submitted 2024-08-24), Nature 638, 920–926 (2025)](https://arxiv.org/abs/2408.13687) [CC] |
| 10^-6 logical error, "still a few years out" (Feb 2023) | Still called "next" on 2025-10-22 and 2026-01-13. No achievement announcement found. | [Google blog, 2025-10-22](https://blog.google/innovation-and-ai/technology/research/quantum-echoes-willow-verifiable-quantum-advantage/) [CC]; [Google Research blog, 2026-01-13](https://research.google/blog/dynamic-surface-codes-open-new-avenues-for-quantum-error-correction/) [CC] |
| Projected Λ = 4 for a distance-17 path to 10^-6 (Feb 2023) | Measured: Λ3,5,7 = 2.14 (Willow surface code, 2024); color code Λ3/5 = 1.56(4) (2025); hexagonal surface code Λ ≈ 2.15 and iSWAP circuit Λ ≈ 1.56 (2026). | [Willow spec sheet, 2024-12-09](https://quantumai.google/static/site-assets/downloads/willow-spec-sheet.pdf) [CC]; [Lacroix et al., arXiv:2412.14256, Nature 645, 614–619 (2025)](https://arxiv.org/abs/2412.14256) [CC]; [Google Research blog, 2026-01-13](https://research.google/blog/dynamic-surface-codes-open-new-avenues-for-quantum-error-correction/) [CC] |
| "A first 'useful, beyond-classical' computation" (Dec 2024) | Google claimed "verifiable quantum advantage" (Quantum Echoes, Oct 2025) as a step toward applications. Google's Thomas O'Brien said the NMR-application results "aren't beyond classical yet". | [Google blog, 2024-12-09](https://blog.google/technology/research/google-willow-quantum-chip/) [CC]; [Google blog, 2025-10-22](https://blog.google/innovation-and-ai/technology/research/quantum-echoes-willow-verifiable-quantum-advantage/) [CC]; [IEEE Spectrum, 2025-10-22](https://spectrum.ieee.org/quantum-echoes) [IND] |
| "Within the decade … a useful, error-corrected quantum computer" (May 2021) | Reaffirmed in Mar 2026 as "commercially relevant … by the end of this decade". Not lapsed. | [Google blog, 2021-05-18](https://blog.google/technology/ai/unveiling-our-new-quantum-ai-campus/) [CC]; [Google blog, 2026-03-24](https://blog.google/innovation-and-ai/technology/research/neutral-atom-quantum-computers/) [CC] |
| ~1,000,000 physical qubits in a room-sized machine (May 2021) | Largest published Google processor is 105 qubits (Dec 2024). Next stated superconducting goal (Mar 2026) is "tens of thousands of qubits". | [Google blog, 2021-05-18](https://blog.google/technology/ai/unveiling-our-new-quantum-ai-campus/) [CC]; [Google blog, 2026-03-24](https://blog.google/innovation-and-ai/technology/research/neutral-atom-quantum-computers/) [CC] |
| Neven: applications "within five years" (Feb 2025) | Window runs to about Feb 2030; not yet testable. | [The Quantum Insider, 2025-02-05](https://thequantuminsider.com/2025/02/05/google-quantum-ai-head-sees-commercial-quantum-within-five-years/) [IND] |

- **External benchmark progress:** DARPA lists IBM, IonQ, Atom Computing, Diraq, Microsoft and PsiQuantum in QBI Stage C, and seven companies in Stage B. Google is in Stage A, list as of 2026-10-08 — [DARPA QBI page](https://www.darpa.mil/research/programs/quantum-benchmarking-initiative) [IND].
  - Via search summary, DARPA's Stage B cohort announced 2025-11-06 (11 companies) did not include Google — [DARPA, "Stage B Selection"](https://www.darpa.mil/research/programs/quantum-benchmarking-initiative/stage-b-selection) [IND].
  - DARPA says companies may advance at different times — [DARPA QBI page](https://www.darpa.mil/research/programs/quantum-benchmarking-initiative) [IND].
- **Contradiction ("2029"):** Google's 2021 post says "within the decade", not 2029 ([Google blog, 2021-05-18](https://blog.google/technology/ai/unveiling-our-new-quantum-ai-campus/)). Some secondary 2026 outlets assert a "million-qubit machine by 2029" target (via search summary, unsourced). I could not verify a Google primary source using "2029" for the hardware goal. Google does use 2029 for its post-quantum cryptography (PQC) migration; see Section 7.

### Inferences
- Read as about 3 years, the Feb 2023 "few years" for 10^-6 would be overdue. Because "few" is undefined, this is not a clear miss.
- Google's December 2024 goal of "useful AND beyond-classical" has not been shown in a single experiment, by Google's own researchers' description. Quantum Echoes' beyond-classical claim and its molecular application were separate experiments.
- Google's position in DARPA's public QBI listing (Stage A while competitors are in B and C) is a documented status, not a performance verdict. DARPA does not publish reasons for stage placement.

### Gaps
- 2020–2021 statements to media (e.g., Reuters or WSJ) quoting a specific "2029" year were not verified this session.
- No Google document found that sets dated interim milestones beyond the 2023 "few years".
- DARPA's reasons for Google's stage placement, and whether Google applied for Stage B, are not public in the sources reviewed.

---

## 4. Finances: what Alphabet discloses (and does not), investments, facilities

### Takeaway
Alphabet discloses no quantum-specific figure: no revenue, cost, capex, headcount or segment. The FY2025 10-K (filed 2026-02-05) mentions "quantum computing" once, under "Moonshots" in the Business section.

Pichai's Q3 2026 remarks put the quantum sentence under an "Other Bets" heading. The 10-K, however, defines Other Bets as non-Google businesses, and Quantum AI is a Google division, so its accounting placement is undetermined.

Quantum-related capital moves:
- Co-led QuEra's $230M round (Feb 2025).
- Acquired Atlantic Quantum (Oct 2025, terms undisclosed).
- SandboxAQ was spun out in March 2022.

### Cited Findings
**What the FY2025 10-K says** — [Alphabet Inc., Form 10-K for fiscal year 2025, filed 2026-02-05](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm) [CC, regulated filing]
- [2026-02-05] Item 1 (Business, Overview), "Moonshots" paragraph: Alphabet will keep investing for the long term in AI and "other frontier technologies such as quantum computing". The paragraph names Waymo and Isomorphic Labs, not Google Research or Quantum AI. No mention of "Willow", "Quantum AI" or "Santa Barbara" was found in the portions read.
- Segments:
  - Google Services: ads, Android, Chrome, Search, YouTube, devices.
  - Google Cloud.
  - Other Bets: "all non-Google businesses", e.g. Waymo and X.
  - Alphabet-level activities "primarily reflect expenses related to our shared AI research and development".
- Alphabet-wide context figures:

  | Item | 2025 | 2024 |
  |---|---|---|
  | R&D expense | $61,087M | $49,326M |
  | Employees (at 2025-12-31) | 190,820 | — |
  | Other Bets revenue | $1,537M | — |
  | Other Bets operating loss | $(7,515)M | $(4,444)M |

**Other filing evidence**
- [queried 2026-11-14] SEC EDGAR full-text search shows "quantum computing" in Alphabet's 10-Ks filed 2020-02-04, 2021-02-03, 2022-02-02, 2024-01-31, 2025-02-05 and 2026-02-05. There is no hit for the 10-K filed in 2023 (FY2022) — [SEC EDGAR full-text search, "quantum computing", Alphabet CIK 0001652044](https://efts.sec.gov/LATEST/search-index?q=%22quantum%20computing%22&ciks=0001652044&forms=10-K,10-Q) [IND tool over CC filings]
- [2026-04-24] "Quantum AI" appears in Alphabet's Annual Report to Security Holders filed 2026-04-24 (accession 0001308179-26-000344) — [SEC EDGAR full-text search, "Quantum AI"](https://efts.sec.gov/LATEST/search-index?q=%22Quantum%20AI%22&ciks=0001652044) [IND tool over CC filing]. Via search summary, the passage refers to "Quantum AI's Nobel-winning chief scientist of quantum hardware". The exact text was not retrieved because the mirrored PDF exceeded the fetch limit — [annual report mirror](https://pdf.dfcfw.com/pdf/H2_AN202604251821579697_1.pdf).
- [2026-10-28] Pichai's Q3 2026 remarks place "We demonstrated 'magic state cultivation' for the first time in quantum computing" under the heading "Other Bets". It sits in a paragraph on "other long-term initiatives", alongside Isomorphic and Project Suncatcher (TPUs in space) — [Google blog, Q3 2026 earnings call remarks, 2026-10-28](https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q3-2026/) [CC]
- **Contradictory, unsourced spending figures (via search summary):** one stock-news site claims Alphabet quantum R&D of "$1.8 billion for fiscal 2025, up 62%"; another says "$1.2 billion". Neither figure appears in the 10-K portions read — [rallies.ai, Alphabet/Willow article A](https://rallies.ai/news/alphabets-willow-quantum-chip-outperforms-supercomputers-trades-at-29x-earnings); [rallies.ai, article B](https://rallies.ai/news/alphabets-willow-quantum-chip-surpasses-supercomputers-buoyed-by-29x-forward-earnings-and-ackman-stake) [IND, unreliable]

**Investments and acquisitions**
- [2025-02-11] QuEra raised a $230M Series B, structured as a convertible note at about $1B post-money. Co-leads were SoftBank Vision Fund and Google Quantum AI; Valor Equity Partners, QVT Family Office and Safar Partners also took part — [Wikipedia, "QuEra Computing"](https://en.wikipedia.org/wiki/QuEra_Computing) [IND, secondary]
- [2026-03-24] Google calls QuEra "a Google portfolio company" and expects "continued collaboration" with it — [Google blog, 2026-03-24](https://blog.google/innovation-and-ai/technology/research/neutral-atom-quantum-computers/) [CC]
- [2025-10-02] Atlantic Quantum acquisition; terms undisclosed — [Gunderson Dettmer, 2025-10-02](https://www.gunder.com/en/news-insights/client-news/gunderson-dettmer-represented-atlantic-quantum-in-its-acquisition-by-google) [IND, counterparty counsel]
- [2022-03-22, older] SandboxAQ was spun out of Alphabet as a standalone company (CEO Jack Hidary; chair Eric Schmidt). Hidary had started the quantum group inside Alphabet in 2016. Reuters reported $500M raised (2023-02-14). Wikipedia does not state any stake Alphabet retained — [Wikipedia, "SandboxAQ", citing The Register 2022-03-22 and Reuters 2023-02-14](https://en.wikipedia.org/wiki/SandboxAQ) [IND, secondary]

**Facilities**
- [2021-05-18, older] Santa Barbara campus with quantum data center, fab and labs; cost not disclosed — [Google blog, 2021-05-18](https://blog.google/technology/ai/unveiling-our-new-quantum-ai-campus/) [CC]
- [2026-03-24] Boulder, Colorado neutral-atom team; investment not disclosed — [Google blog, 2026-03-24](https://blog.google/innovation-and-ai/technology/research/neutral-atom-quantum-computers/) [CC]

### Inferences
- Alphabet treats quantum as immaterial for segment reporting: it gets one generic 10-K mention and no figures.
- Where the costs sit cannot be determined from filings:
  - Google Quantum AI is a Google division, which points to Google Services or, if treated as shared research, Alphabet-level activities.
  - Pichai's "Other Bets" heading in a speech is not an accounting disclosure.
- The R&D growth of about $11.8B in 2025 cannot be attributed to quantum on the available evidence.

### Gaps
- **Not disclosed anywhere found:** quantum budget, capex, facility cost, Quantum AI headcount, any revenue from access programs, the dollar amount of Google's QuEra investment, Atlantic Quantum's price, and any SandboxAQ stake.
- Whether the 10-K risk factors mention quantum was not determined; the risk-factor text was only partly read.
- GV's (Alphabet's venture arm) quantum investments, such as early IonQ rounds, were not verified this session.

---

## 5. Partners, customers, contracts, government programs, capacity

### Takeaway
Programs and partners found:
- DARPA QBI participant, Stage A (≤$1M tier).
- Sponsor of the $5M XPRIZE Quantum Applications.
- Partner in the UK NQCC Willow-access program.
- Science collaborators include UC Berkeley (the NMR study), and Stanford and the Ethereum Foundation (ECC resource paper).
- Boulder ecosystem ties: JILA, CU Boulder, NIST Boulder, Elevate Quantum.

I found no paying customers or commercial contracts for Google quantum hardware.

### Cited Findings
**DARPA QBI**
- [2025-09-09] Google says it was selected to take part in DARPA QBI. It calls DARPA a "trusted validator" providing "rigorous, third-party benchmarking" and says "We're confident in our approach" — [Google blog, Neven, 2025-09-09](https://blog.google/innovation-and-ai/technology/research/google-quantum-ai-selected-darpa-qbi/) [CC]
- [list as of 2026-10-08] DARPA's QBI listing:

  | Stage (funding cap) | Companies listed |
  |---|---|
  | Stage A (up to $1M) | Google Quantum AI (superconducting transmon qubits); Quandela |
  | Stage B (up to $15M) | Nord Quantique, Photonic Inc., Quantinuum, Quantum Motion, QuEra, Silicon Quantum Computing, Xanadu |
  | Stage C (up to $300M) | Atom Computing, Diraq, IBM, IonQ, Microsoft, PsiQuantum |

  - QBI is "not a winner-take-all competition".
  - DARPA judges it more likely than not that at least one company will succeed by 2033.
  - Source: [DARPA, Quantum Benchmarking Initiative program page](https://www.darpa.mil/research/programs/quantum-benchmarking-initiative) [IND]

**XPRIZE Quantum Applications**
- [2025-12-10] Structure and Google's role:
  - A three-year competition with a $5M purse. Google, Google.org and GESDA back it, and Google Quantum AI supports it.
  - 133 submissions were received. Seven Phase I finalists share $1M.
  - The remaining $4M, including a $3M grand prize, is to be awarded in March 2027.
  - The seven finalists:

    | Team | Lead (affiliation) |
    |---|---|
    | Calbee Quantum | Garnet Chan (Caltech) |
    | Gibbs Samplers | András Gilyén (HUN-REN Rényi Institute) |
    | Phasecraft Materials Team | Toby Cubitt |
    | The QuMIT | Alexander Schmidhuber (MIT) |
    | Xanadu | Juan Miguel Arrazola |
    | Q4Proteins | Markus Reiher (ETH Zurich) |
    | QuantumForGraphproblem | Jianqiang Li (Rice) |

  - Source: [Google blog, Ryan Babbush, "The 7 finalists in the XPRIZE Quantum Applications competition", 2025-12-10](https://blog.google/innovation-and-ai/technology/research/google-gesda-xprize-quantum-applications-finalists/) [CC]
- [2026] Via search summary: wildcard registration ran 2026-01-14 to 2026-03-04, and five wildcard finalists joined Phase II — [XPRIZE, "From wildcard entry to impact…"](https://annualreport.xprize.org/news/from-wildcard-entry-to-impact-xprize-quantum-applications-wildcard-finalists-advancing-to-next-phase) [IND]

**UK NQCC**
- [2025-12-12 and 2026-05-28] Willow access call and first award (King's College London); see Section 1 — [NQCC, 2025-12-12](https://www.nqcc.ac.uk/updates/nqcc-and-google-quantum-ai-launch-new-initiative-to-accelerate-quantum-science-in-the-uk/) [IND, partner]

**Research collaborators**
- [2025-10-22] UC Berkeley ran a "proof-of-principle" NMR experiment with Google on molecules of 15 and 28 atoms. The companion preprint was to be posted to arXiv the same day — [Google blog, 2025-10-22](https://blog.google/innovation-and-ai/technology/research/quantum-echoes-willow-verifiable-quantum-advantage/) [CC]. IEEE Spectrum quotes Ashok Ajoy (UC Berkeley chemistry), who is connected to the work — [IEEE Spectrum, 2025-10-22](https://spectrum.ieee.org/quantum-echoes) [IND]
- [2026-03-30] The ECC resource-estimate paper's co-authors include Justin Drake (Ethereum Foundation) and Dan Boneh (Stanford) — [Babbush et al., arXiv:2603.28846](https://arxiv.org/abs/2603.28846) [CC]; [The Quantum Insider, 2026-03-31](https://thequantuminsider.com/2026/03/31/q-day-just-got-closer-three-papers-in-three-months-are-rewriting-the-quantum-threat-timeline/) [IND]
- [2026-03-24] Boulder ecosystem partners named: CU Boulder, JILA, NIST Boulder, Elevate Quantum. NIST's James Kushmerick: "It is always sad having a researcher with the creativity and impact of Adam leave [NIST]" — [Google blog, 2026-03-24](https://blog.google/innovation-and-ai/technology/research/neutral-atom-quantum-computers/) [CC]

**Open competitions**
- [2026-10-23] Kaggle "Google Verifiable Quantum Circuit Compilation" competition:
  - Prizes total $150,000: 1st $50k, 2nd $25k, 3rd $10k, 4th–6th $5k each, plus $50k in special prizes.
  - Three tasks: fusion (quantum fast inverse square root for inertial-confinement-fusion targets), optimization (a Decoded Quantum Interferometry decoder for Optimal Polynomial Intersection, i.e. Reed–Solomon decoding in superposition), and chemistry (FeMoCo Hamiltonian factorization).
  - Google says internal Gemini-model experiments already beat the reported circuits on all three. The companion paper is arXiv 2610.23832.
  - Source: [The Quantum Insider, 2026-10-23](https://thequantuminsider.com/2026/10/23/google-launches-150000-ai-competition-to-reduce-quantum-computing-demands/) [IND, reporting company claims]

**Capacity**
- [2024-12-09] The Willow QEC chip runs 909,000 error-correction cycles per second; the RCS chip runs 63,000 circuit repetitions per second — [Willow spec sheet](https://quantumai.google/static/site-assets/downloads/willow-spec-sheet.pdf) [CC]
- [2021-05-18, older] Cryostat size and temperature: about three household refrigerators, about 10 mK — [Google blog, 2021-05-18](https://blog.google/technology/ai/unveiling-our-new-quantum-ai-campus/) [CC]

### Inferences
- Google's external engagements are research access, prizes, co-authorship and a government benchmarking program, not sales.
- QBI Stage A carries a cap of up to $1M per DARPA's tiering. That is small relative to Alphabet's scale, which suggests QBI matters to Google mainly as third-party validation, as Google itself frames it.

### Gaps
- Not verified this session (no primary source fetched):
  - NVIDIA collaboration (believed to be a Nov 2024 announcement on simulating quantum device physics; the NVIDIA newsroom URL attempted redirected to the news archive).
  - Pharma partnerships (e.g., Boehringer Ingelheim, 2021).
  - National-lab agreements.
  - Any federal contracts beyond QBI.
- The dollar amount DARPA paid Google in QBI is not disclosed in the sources reviewed.
- I found no evidence of paying customers. The terms of Google's historical cloud access channel are unverified.

---

## 6. Key people and current roles (dated)

### Takeaway
- Neven remains Founder and Lead.
- Michel Devoret, a 2025 Nobel laureate, is Chief Scientist of quantum hardware.
- Julian Kelly is director of (quantum) hardware.
- Ryan Babbush is Director of Research, Quantum Algorithms and Applications.
- Craig Gidney (title: Quantum Software Engineer) is the lead author of Google's cryptanalysis resource estimates and co-inventor of magic state cultivation.
- John Martinis, a 2025 Nobel laureate who led Google's hardware effort after 2014, is CTO and co-founder of Qolab.
- Adam Kaufman leads the new neutral-atom team.

### Cited Findings
| Person | Role and dated facts | Sources |
|---|---|---|
| Hartmut Neven | "Founder and Lead, Google Quantum AI" (2024-12-09; 2025-09-09; 2025-10-22; 2026-03-24). Titled "VP of Engineering" on 2023-02-22. Co-author of the 2026 ECC paper. | [Google blog, 2026-03-24](https://blog.google/innovation-and-ai/technology/research/neutral-atom-quantum-computers/) [CC]; [Google Research blog, 2023-02-22](https://research.google/blog/suppressing-quantum-errors-by-scaling-a-surface-code-logical-qubit/) [CC]; [arXiv:2603.28846](https://arxiv.org/abs/2603.28846) [CC] |
| Michel Devoret | "Nobel laureate and Google Quantum AI chief scientist of quantum hardware" (2025-10-22). The 2026 annual report reportedly refers to "Quantum AI's Nobel-winning chief scientist of quantum hardware" (via search summary). | [IEEE Spectrum, 2025-10-22](https://spectrum.ieee.org/quantum-echoes) [IND]; [annual report mirror](https://pdf.dfcfw.com/pdf/H2_AN202604251821579697_1.pdf) [CC, via search summary] |
| Julian Kelly | "Director of Quantum Hardware" (2023-02-22). "Director of hardware at Google Quantum AI" (CNBC interview, 2025-03-25). | [Google Research blog, 2023-02-22](https://research.google/blog/suppressing-quantum-errors-by-scaling-a-surface-code-logical-qubit/) [CC]; [The Quantum Insider, 2025-03-26](https://thequantuminsider.com/2025/03/26/google-executive-says-quantum-applications-could-arrive-in-five-years/) [IND] |
| Ryan Babbush | "Director of Research, Quantum Algorithms and Applications" (2025-12-10). Lead author of the ECC paper (2026-03-30). | [Google blog, 2025-12-10](https://blog.google/innovation-and-ai/technology/research/google-gesda-xprize-quantum-applications-finalists/) [CC]; [arXiv:2603.28846](https://arxiv.org/abs/2603.28846) [CC] |
| Craig Gidney | "Quantum Software Engineer, Google Quantum AI" (2026-10-15). Sole author of the RSA-2048 estimate (2025-05-21). Co-author of the ECC paper (2026). The 2024 magic-state-cultivation theory is credited to Gidney, Noah Shutty and Cody Jones. | [Google blog, 2026-10-15](https://blog.google/innovation-and-ai/models-and-research/quantum-computing/magic-state-cultivation-quantum-computing/) [CC]; [arXiv:2505.15917](https://arxiv.org/abs/2505.15917) [CC] |
| Vadim Smelyanskiy | "Director, Quantum Pathfinding" (2025-10-22). | [Google blog, 2025-10-22](https://blog.google/innovation-and-ai/technology/research/quantum-echoes-willow-verifiable-quantum-advantage/) [CC] |
| Adam Kaufman | Leads the Boulder neutral-atom hardware team (2026-03-24). Remains a JILA Fellow and CU Boulder faculty member. Quote: "I am thrilled to join Google's world-leading program in quantum computing". | [Google blog, 2026-03-24](https://blog.google/innovation-and-ai/technology/research/neutral-atom-quantum-computers/) [CC] |
| Heather Adkins; Sophie Schmieg | VP, Security Engineering; Senior Staff Cryptography Engineer. Authors of Google's 2029 PQC timeline post (2026-03-25). | [Google blog, 2026-03-25](https://blog.google/innovation-and-ai/technology/safety-security/cryptography-migration-timeline/) [CC] |
| Other named staff | Emma Rosenfeld, Research Scientist (2026-10-15). Thomas O'Brien, staff research scientist (2025-10-22). Alec Eickbusch, Alexis Morvan and Matt McEwen (dynamic codes, 2026-01-13). Erik Lucero, "Lead Engineer" as of 2021-05-18 (current role unverified). | [Google blog, 2026-10-15](https://blog.google/innovation-and-ai/models-and-research/quantum-computing/magic-state-cultivation-quantum-computing/) [CC]; [IEEE Spectrum, 2025-10-22](https://spectrum.ieee.org/quantum-echoes) [IND]; [Google Research blog, 2026-01-13](https://research.google/blog/dynamic-surface-codes-open-new-avenues-for-quantum-error-correction/) [CC] |
| Atlantic Quantum team | CEO Bharath Kannan and CTO Simon Gustavsson joined Google Quantum AI (2025-10-03). | [The Quantum Insider, 2025-10-03](https://thequantuminsider.com/2025/10/03/atlantic-quantum-joins-google-quantum-ai/) [IND] |
| John Martinis (alumnus) | Recruited by Google with his UCSB team in 2014 ([Wikipedia](https://en.wikipedia.org/wiki/Google_Quantum_AI) [IND, secondary]). Now "CTO and co-founder" of Qolab and "2025 Nobel laureate in Physics" ([Qolab website, accessed 2026-11-14](https://qolab.ai/) [IND of Google; company-controlled by Qolab]). Qolab details from the same site: CEO and co-founder Alan Ho is a former Head of Product at Google Quantum AI; co-founder Robert McDermott (UW–Madison) is Head of Hardware; office in Los Angeles and lab in Madison, WI; headline "$54.2 million Series B" led by UC Investments (date not on page); listed partners include Applied Materials, HPE, Synopsys, KLA, Western Digital, Quantum Machines, Riverlane and DARPA. | As cited in this row |

### Inferences
- Senior leadership has been stable from 2023 to 2026: Neven leads throughout, and Kelly runs hardware throughout.
- Two of the three 2025 physics Nobel laureates have Google Quantum AI ties: Devoret currently, Martinis formerly.

### Gaps
- Sergio Boixo's current title and role could not be verified this session (no source retrieved).
- The official Nobel citation could not be fetched (nobelprize.org returned 403). The prize motivation and the third laureate (John Clarke) are background knowledge, not verified here. Devoret's and Martinis's laureate status is corroborated by IEEE Spectrum and Qolab.
- The date Martinis left Google (background knowledge: 2020) was not verified.
- Charina Chou's and other leaders' current titles were not checked.

---

## 7. Legal and regulatory: export controls, patents/litigation, post-quantum cryptography and "Q-Day"

### Takeaway
Google's main public regulatory-adjacent position is its PQC timeline. On 2026-03-25 it set 2029 as its own target for completing its PQC migration and prioritized authentication and signatures. It did not predict a date for a cryptographically relevant quantum computer (CRQC).

Google researchers have repeatedly lowered public attack-cost estimates:
- RSA-2048: under 1M noisy qubits (May 2025).
- 256-bit elliptic-curve discrete log: under 500k physical qubits, running in minutes (Mar 2026), published with a zero-knowledge proof instead of the circuits.

I found nothing on Google-specific export-control actions or quantum patent litigation; these were not searched once the quota ran out.

### Cited Findings
**Google's PQC timeline (2026-03-25)** — [Google blog, Heather Adkins (VP, Security Engineering) & Sophie Schmieg (Senior Staff Cryptography Engineer), "Quantum frontiers may be closer than they appear", 2026-03-25](https://blog.google/innovation-and-ai/technology/safety-security/cryptography-migration-timeline/) [CC]
- "We're setting a timeline for post-quantum cryptography migration to 2029."
- Rationale: progress in quantum hardware, quantum error correction and quantum factoring resource estimates.
- "The threat to encryption is relevant today with store-now-decrypt-later attacks". Digital signatures "are a future threat that require the transition to PQC prior to a Cryptographically Relevant Quantum Computer (CRQC)".
- Google has "adjusted our threat model to prioritize PQC migration for authentication services" and recommends other teams do the same.
- "Android 17 is integrating PQC digital signature protection using ML-DSA."
- The post cites existing Chrome PQC support and Google Cloud PQC offerings.
- It gives no CRQC or "Q-Day" date.
- **Date discrepancy (via search summary):** Dark Reading reportedly referenced a February post. The blog.google page and other outlets date it 2026-03-25.

**Attack-cost estimates published by Google researchers**
- [2025-05-21] Gidney's RSA-2048 estimate, arXiv:2505.15917 (no journal reference listed as of fetch):
  - A 2048-bit RSA integer could be factored "in under a week with fewer than one million noisy qubits". The 2019 Gidney–Ekerå estimate was about 8 hours with 20 million noisy qubits: about 20x fewer qubits for about 20x longer runtime.
  - Assumptions: square grid with nearest-neighbour connectivity, uniform 0.1% gate error, 1 µs surface-code cycle, 10 µs control-system reaction time.
  - Sources of the reduction: approximate residue arithmetic (Chevignard–Fouque–Schrottenloher 2024), yoked surface codes, and magic state cultivation.
  - Toffoli count is more than 100x lower than Chevignard et al. (2024).
  - Source: [Craig Gidney, "How to factor 2048 bit RSA integers with less than a million noisy qubits", arXiv:2505.15917, 2025-05-21](https://arxiv.org/abs/2505.15917) [CC]
- [2026-03-30, v2 2026-04-15] Google-led ECC estimate, arXiv:2603.28846:
  - Shor's algorithm for 256-bit ECDLP needs either under 1,200 logical qubits and under 90M Toffoli gates, or under 1,450 logical qubits and under 70M Toffoli gates.
  - On superconducting hardware with 10^-3 physical error and planar connectivity, it would run "in minutes" with "fewer than half a million physical qubits".
  - The authors validated results with a zero-knowledge proof instead of disclosing attack circuits.
  - "Fast-clock" platforms (superconducting, photonic) could enable "on-spend" attacks on public-mempool transactions before "slow-clock" platforms (neutral atom, ion trap) could.
  - The paper urges vulnerable cryptocurrency communities to migrate promptly.
  - Source: [Babbush, Zalcman, Gidney, Broughton, Khattar, Neven, Bergamaschi, Drake, Boneh, "Securing Elliptic Curve Cryptocurrencies against Quantum Vulnerabilities: Resource Estimates and Mitigations", arXiv:2603.28846](https://arxiv.org/abs/2603.28846) [CC]

**Reactions** — [The Quantum Insider, "Q-Day Just Got Closer: Three Papers in Three Months Are Rewriting the Quantum Threat Timeline", 2026-03-31](https://thequantuminsider.com/2026/03/31/q-day-just-got-closer-three-papers-in-three-months-are-rewriting-the-quantum-threat-timeline/) [IND]
- Justin Drake (co-author): "a monumentous day for quantum computing and cryptography".
- Nic Carter (Castle Island Ventures): "very sobering".
- Haseeb Qureshi (Dragonfly) called the findings "serious".
- Eli Ben-Sasson urged Bitcoin to speed up BIP 360.
- Prior ECC-256 estimate for comparison: about 9M physical qubits (Litinski 2023, photonic).
- Caveat: the reported ~41% chance of deriving a key before a Bitcoin transaction confirms holds only under idealized conditions.
- The zero-knowledge proof relies on BLS12-381, which a powerful quantum computer could itself threaten.
- Competing estimate: Iceberg Quantum (Feb 2026, "Pinnacle", QLDPC codes) claims RSA-2048 with under 100,000 physical qubits. This is validated by simulation only, requires beyond-nearest-neighbour connectivity, and leaves decoder latency unresolved.
- Gidney noted that QLDPC decoder reaction-time assumptions are harder to meet, and said he sees no further 10x reduction without changing assumptions.

**Executive statement**
- [2025, unverified] Pichai reportedly said the world will need to adapt cryptography within 3–5 years. This is via search summary of [ITPro](https://www.itpro.com/technology/sundar-pichai-thinks-commercially-viable-quantum-computing-is-just-a-few-years-away) [IND]; the quote was not verified in fetched text.

**Filings**
- [2026-02-05] No quantum-specific risk factor was found in the portions of the FY2025 10-K read — [Alphabet 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm) [CC]

### Inferences
- Google simultaneously publishes cheaper attack estimates and sets an aggressive internal migration date (2029). Its own security leadership cites these estimates as a reason for the timeline.
- The 2029 date is a migration deadline, not a forecast of when a CRQC will exist; the post states no CRQC date.

### Gaps
- Export controls not verified this session:
  - The September 2024 US BIS rule on quantum items, believed to add ECCN 4A906 with qubit and error thresholds. A Federal Register fetch was blocked.
  - Any licensing affecting Google's hardware or collaborations.
  - Any 2025–26 changes.
- Patents and litigation: not searched; no finding either way.
- Regulatory filings or comments by Google on NIST, NSA or OMB PQC deadlines: not verified.

---

## 8. Science: what has been demonstrated, who verified or challenged it, what remains unproven

### Takeaway
Google's QEC record is peer-reviewed and quantitatively specific:
- Below-threshold surface-code memory, Λ = 2.14.
- Colour codes, Λ = 1.56.
- Dynamic surface codes.
- Magic state cultivation, ≥99.99% T-state fidelity.

All of these are at small code distances (3–7), mostly for memory or a single logical qubit, with post-selection in the magic-state work. No below-threshold two-logical-qubit gate (Milestone 4 territory) was found.

Google's "beyond-classical" claims have a mixed record:
- The 2019 Sycamore claim was overtaken by classical simulation.
- The 2024 Willow random circuit sampling (RCS) claim stands unrefuted in the sources found, but cannot be directly verified (Aaronson).
- The 2025 Quantum Echoes "verifiable advantage" is peer-reviewed, but the referees were split. There has been no independent replication on non-Google hardware, and the main published classical-simulation rebuttal was authored by Google-affiliated researchers.

### Cited Findings
#### A. Willow below-threshold QEC (Nature 638, 920–926, 2025)
- [2024-08-24 preprint; announced 2024-12-09] Results — [Google Quantum AI and collaborators, "Quantum error correction below the surface code threshold", arXiv:2408.13687; Nature 638, 920–926 (2025), DOI 10.1038/s41586-024-08449-y](https://arxiv.org/abs/2408.13687) [CC]:
  - Two below-threshold surface-code memories: distance-7 (101 qubits) and distance-5 with a real-time decoder.
  - Λ = 2.14 ± 0.02 per +2 in distance.
  - Distance-7 logical error 0.143% ± 0.003% per cycle.
  - Logical memory lifetime exceeds its best physical qubit by 2.4 ± 0.3x ("beyond break-even").
  - Real-time decoding at distance-5: average latency 63 µs, sustained up to 1 million cycles, at a 1.1 µs cycle time.
  - Repetition codes up to distance-29 show logical performance limited by "rare correlated error events", about once per hour or about 3×10^9 cycles.
  - The authors argue the device performance, if scaled, could meet requirements of large-scale fault-tolerant algorithms.
- [2024-12-09] Google's lay description: going from 3x3 to 5x5 to 7x7 encoded grids cut the error rate "in half" each step — [Google blog, 2024-12-09](https://blog.google/technology/research/google-willow-quantum-chip/) [CC]
- [2024-12-10] Scott Aaronson (independent):
  - "this is a very important threshold that's now been crossed"; "after 30 years we're now finally tickling the tail of the dragon of quantum fault-tolerance".
  - Willow encoded one logical qubit and did not run operations on encoded qubits.
  - A "true" fault-tolerant qubit would need about 10^-6 two-qubit gate error.
  - "No serious person expected 105 physical qubits to be useful in themselves."
  - Source: [Scott Aaronson, Shtetl-Optimized, "The Google Willow thing", 2024-12-10](https://scottaaronson.blog/?p=8525) [IND]
- [Dec 2024] Other independent criticism, via Wikipedia:
  - Results cover "quantum memory", not below-threshold logical gates (APS *Physics* 17, 176, Rini & Schirber, 2024-12-09).
  - Logical error is "orders of magnitude above the 10^-6 levels" needed (Sogeti Labs, van Velzen, 2024-12-24).
  - Google said the chip cannot break modern cryptography (The Verge, Hollister, 2024-12-12).
  - Neven's remark that Willow "lends credence to the notion that quantum computation occurs in many parallel universes" drew criticism (The Quantum Insider, 2024-12-16; NY Post, 2024-12-15).
  - Source: [Wikipedia, "Willow processor"](https://en.wikipedia.org/wiki/Willow_processor) [IND, secondary; original APS page returned 403]

#### B. Random circuit sampling (RCS): 2019 Sycamore, IBM rebuttal, classical simulations, 2024 Willow
- [2019-10, older] Claim: 53-qubit Sycamore did in 200 s a task estimated to need 10,000 years on Summit — [IEEE Spectrum, 2025-10-22](https://spectrum.ieee.org/quantum-echoes) [IND]
- [2019-10-22, older] IBM rebuttal:
  - "an ideal simulation of the same task can be performed on a classical system in 2.5 days", using RAM plus hard-drive storage for the state vector.
  - Google's estimate "failed to fully account for plentiful disk storage".
  - IBM argued its simulation has "far greater fidelity" than the device's predicted 0.2%.
  - IBM urged treating such claims "with a large dose of skepticism".
  - This was an estimate, not an executed run.
  - Source: [IBM Research blog, Pednault, Maslov, Gunnels, Gambetta, "On 'Quantum Supremacy'", 2019-10-22](https://www.ibm.com/quantum/blog/on-quantum-supremacy) [IND, competitor]
- [2021-11-04 preprint; PRL 2022, older] Executed classical simulation by Pan, Chen and Zhang (CAS):
  - Generated 1 million uncorrelated bitstrings for the 53-qubit, 20-cycle Sycamore circuit at fidelity about 0.0037.
  - Took about 15 hours on 512 GPUs.
  - They estimated "a few dozen seconds" on an exascale machine, "faster than Google's quantum hardware".
  - Source: [Feng Pan, Keyang Chen, Pan Zhang, "Solving the sampling problem of the Sycamore quantum circuits", arXiv:2111.03011, PRL 129, 090502 (2022)](https://arxiv.org/abs/2111.03011) [IND]
- [2025-10-22/23] Scientific American notes that earlier advantage claims, "including Google's 2019 one", were overtaken as classical algorithms improved — [Scientific American, Dan Garisto, 2025-10-22/23](https://www.scientificamerican.com/article/google-measures-quantum-echoes-on-willow-quantum-computer-chip/) [IND]
- [2023-04-21 preprint; Nature 634, 328–333 (2024)] Google's follow-up: an RCS experiment with 67 qubits at 32 cycles, which Google says is beyond existing supercomputers even accounting for noise. It also identifies noise-driven phase transitions in RCS — [Morvan et al., "Phase transition in Random Circuit Sampling", arXiv:2304.11119](https://arxiv.org/abs/2304.11119) [CC]
- [2024-12-09] Willow RCS: 103 qubits, depth 40, XEB fidelity 0.1%, "5 minutes vs. 10^25 years" — [Willow spec sheet](https://quantumai.google/static/site-assets/downloads/willow-spec-sheet.pdf) [CC]
- [2024-12-10] Aaronson on the Willow RCS claim (independent):
  - Accepts the numbers "with the caveats stated".
  - Notes it would also take about 10^25 years to directly verify the output classically, so "all validation … is indirect, based on extrapolations from smaller circuits"; "We're now deeply into the unverifiable regime".
  - Notes better classical methods could still appear.
  - Relays Google's reply that cross-entropy scores were checked three ways on smaller patches.
  - Source: [Shtetl-Optimized, 2024-12-10](https://scottaaronson.blog/?p=8525) [IND]

#### C. Quantum Echoes / OTOC "verifiable quantum advantage" (Nature 646, 825–830, 2025)
- [2025-06-11 preprint] Measured second-order out-of-time-order correlators (OTOC(2)) on a superconducting processor with 103 qubits. The signal is attributed to "constructive interference between Pauli strings that form large loops in configuration space". Large-scale measurements are claimed to exceed known classical algorithms. The paper includes a Hamiltonian-learning example. Data are released for 95, 40 and 31 qubits, with exact simulation at ≤40 qubits — [Abanin, Acharya and a large Google Quantum AI author list, "Constructive interference at the edge of quantum ergodic dynamics", arXiv:2506.10191](https://arxiv.org/abs/2506.10191) [CC]. The published Nature version is titled "Observation of constructive interference at the edge of quantum ergodicity", Nature 646, 825–830, DOI 10.1038/s41586-025-09526-6 (per Wikipedia references) — [Wikipedia](https://en.wikipedia.org/wiki/Google_Quantum_AI) [IND, secondary]
- [2025-10-22] Google's claims:
  - "13,000 times faster on Willow than the best classical algorithm" on a top supercomputer.
  - Verifiability is defined as: "the result can be repeated on our quantum computer — or any other of the same caliber".
  - The UC Berkeley NMR proof-of-principle used molecules with 15 and 28 atoms (preprint).
  - Source: [Google blog, Neven & Smelyanskiy, 2025-10-22](https://blog.google/innovation-and-ai/technology/research/quantum-echoes-willow-verifiable-quantum-advantage/) [CC]
- [2025-10-22] IEEE Spectrum's account:
  - Ran on 65 qubits of the 105-qubit chip.
  - NMR-related experiments used up to 15 qubits.
  - Google's Thomas O'Brien said the molecular results "aren't beyond classical yet" and that error correction will be needed for practical applications.
  - Source: [IEEE Spectrum, 2025-10-22](https://spectrum.ieee.org/quantum-echoes) [IND]
- [2025-10-22/23] Scientific American's account:
  - Google estimates about 3 years on a classical supercomputer vs about 2 hours on Willow.
  - Shenglong Xu (Texas A&M, not involved): the result "seems like it is beyond what we can do right now using classical methods".
  - Three Nature referees were broadly positive (one: "truly impressive"), but "split over" how fully genuine quantum advantage was shown.
  - The molecular preprint is not yet faster than classical approaches.
  - Source: [Scientific American, Dan Garisto, 2025-10-22/23](https://www.scientificamerican.com/article/google-measures-quantum-echoes-on-willow-quantum-computer-chip/) [IND]
- [2025-10-22] Via search summary of Nature's news story (Elizabeth Gibney, "Google claims 'quantum advantage' again — but researchers are sceptical"): Dries Sels (NYU) said "The burden of proof should be high". Some scientists argue there is no proof that no efficient classical algorithm exists. The nature.com page was not retrieved; a syndicated copy is at [newsar.codejungle.org/articles/1390](https://newsar.codejungle.org/articles/1390) [IND, via search summary]
- [2026-04-16] Rebuttal of one classical method, by authors who include Google-affiliated researchers (per search summary; the paper also appears on Google Research's publications page; individual affiliations were not shown on the arXiv abstract page):
  - Argues tensor networks with belief propagation (TNBP) cannot feasibly simulate the experiment.
  - The OTOC circuits generate highly entangled, "largely incompressible" states on Willow's dense 2D connectivity.
  - TNBP had earlier been used to challenge other companies' advantage claims (via search summary).
  - Sources: [Bermejo, Villalonga, Ware, Vidal, Szasz, "Tensor Networks with Belief Propagation Cannot Feasibly Simulate Google's Quantum Echoes Experiment", arXiv:2604.15427, 2026-04-16](https://arxiv.org/abs/2604.15427) [CC-affiliated]; [Google Research publication page](https://research.google/pubs/belief-propagation-study-of-googles-quantum-echoes-experiment/) [CC]
- [2026-03] Via search summary, a tensor-network review gives about 3.2 years per circuit on Frontier vs 2.1 hours on Willow — [arXiv:2603.18825, "Quantum Advantage: a Tensor Network Perspective"](https://arxiv.org/pdf/2603.18825) [IND, not fetched]
- **Contradiction (qubit counts):** 65 qubits (IEEE Spectrum), 103 qubits (arXiv abstract) and a "105-qubit array" (Google blog). These appear to describe different subsets or experiments within the same work.

#### D. Colour codes, dynamic surface codes, logical operations, lattice surgery
- [2024-12-18 preprint; Nature 645, 614–619 (2025)] Colour code results — [Lacroix, Bourassa, Heras, Zhang, Bausch et al., "Scaling and logic in the color code on a superconducting quantum processor", arXiv:2412.14256](https://arxiv.org/abs/2412.14256) [CC]:
  - Distance 3 to 5 gives Λ3/5 = 1.56(4).
  - Transversal Clifford gates add error 0.0027(3) per gate (logical randomized benchmarking).
  - Magic-state injection fidelity exceeds 99% with post-selection, keeping about 75% of data.
  - Logical-state teleportation between distance-3 colour codes via lattice surgery reaches 86.5(1)%–90.7(1)% fidelity.
- [2026-01-13] Dynamic surface codes, published in Nature Physics as "Demonstration of dynamic surface codes" — [Google Research blog, 2026-01-13](https://research.google/blog/dynamic-surface-codes-open-new-avenues-for-quantum-error-correction/) [CC]:
  - Hexagonal circuit (3 couplers per qubit): Λ ≈ 2.15 from distance 3 to 5.
  - "Walking" circuit: cuts time-correlated errors by over 10x. These persist up to 40 cycles in the standard circuit.
  - iSWAP-based circuit: Λ ≈ 1.56.

#### E. Magic state cultivation on hardware (Science, 2026-10-15)
- [2026-10-15] Google's account — [Google blog, Emma Rosenfeld & Craig Gidney, "Bringing the magic: Google breaks open a bottleneck in quantum computing", 2026-10-15](https://blog.google/innovation-and-ai/models-and-research/quantum-computing/magic-state-cultivation-quantum-computing/) [CC]:
  - First hardware demonstration, on Willow, published in Science (DOI 10.1126/science.aee7961).
  - About 40x error reduction vs un-cultivated states.
  - "Record" logical T-state fidelity of 99.99%.
  - A distance-3 colour-code state was grafted into a distance-5 surface code.
  - Background claim: "some estimates" say up to 95% of a quantum computer's capacity could go to magic states.
  - Google's caveats: "we still need to demonstrate magic state cultivation at a larger scale"; "plenty of technical challenges remain".
- [2026-10-15] Trade-press account — [Quantum Computing Report, "Google Quantum AI demonstrates magic state cultivation on Willow processor in Science milestone", 2026-10-15](https://quantumcomputingreport.com/google-quantum-ai-demonstrates-magic-state-cultivation-on-willow-processor-in-science-milestone/) [IND]:
  - Paper title: "Magic state cultivation on a superconducting quantum processor".
  - Fidelity 99.99(1)%, i.e. error ≤10^-4.
  - About 8% state retention via fault-tolerant measurement filtering.
  - Fidelity is bounded by a "self-referential" benchmarking protocol, citing drift and low-frequency measurement noise.
  - No outside experts are quoted.
  - Via search summary, about 8% of attempts are retained at θ = π/4; next steps named are real-time T-gate implementation, larger distances and decoder work.

#### F. Resource estimates (Gidney 2025; Google ECC 2026)
- See Section 7. In short: RSA-2048 needs under 1M noisy qubits for under a week at 0.1% error, 1 µs cycle and 10 µs reaction time — [arXiv:2505.15917](https://arxiv.org/abs/2505.15917) [CC]. ECDLP-256 needs under 500k physical qubits and runs in minutes, at 10^-3 error — [arXiv:2603.28846](https://arxiv.org/abs/2603.28846) [CC].
- Outside reaction and competing estimates — [The Quantum Insider, 2026-03-31](https://thequantuminsider.com/2026/03/31/q-day-just-got-closer-three-papers-in-three-months-are-rewriting-the-quantum-threat-timeline/) [IND].

#### G. 2026 results timeline (Google)

| Date | Result | Source |
|---|---|---|
| 2026-01-13 | Dynamic surface codes (Nature Physics) | [Google Research blog](https://research.google/blog/dynamic-surface-codes-open-new-avenues-for-quantum-error-correction/) [CC] |
| 2026-03-24 | Neutral-atom program launched | [Google blog](https://blog.google/innovation-and-ai/technology/research/neutral-atom-quantum-computers/) [CC] |
| 2026-03-25 | 2029 PQC migration timeline | [Google blog](https://blog.google/innovation-and-ai/technology/safety-security/cryptography-migration-timeline/) [CC] |
| 2026-03-30 | ECC resource estimate | [arXiv:2603.28846](https://arxiv.org/abs/2603.28846) [CC] |
| 2026-04-16 | Preprint arguing TNBP cannot simulate Quantum Echoes | [arXiv:2604.15427](https://arxiv.org/abs/2604.15427) [CC-affiliated] |
| 2026-10-15 | Magic state cultivation (Science) | [Google blog](https://blog.google/innovation-and-ai/models-and-research/quantum-computing/magic-state-cultivation-quantum-computing/) [CC] |
| 2026-10-23 | AI-agent circuit-compilation competition and paper (arXiv 2610.23832) | [The Quantum Insider](https://thequantuminsider.com/2026/10/23/google-launches-150000-ai-competition-to-reduce-quantum-computing-demands/) [IND] |

- No 2026 primary source was found announcing the long-lived logical qubit (Milestone 3).

### Inferences
- Every Google QEC demonstration found operates at distances 3–7 on one chip of at most 105 qubits.
- Lattice-surgery teleportation (86.5–90.7% fidelity, colour code, 2024–25) is far below the reliability implied by Milestone 4 (a logical gate at about 10^-6). I found no below-threshold two-logical-qubit gate.
- Cultivation needs repeated attempts: at about 8% retention, roughly 12.5 attempts per accepted magic state.
- The demonstrated T-state error (≤10^-4) is about 100x above the 10^-6 per-operation level Google cites for Milestone 3.
- "Verifiable" in Google's Quantum Echoes framing means verifiable by another quantum computer of equal calibre. As of 2026-11-14 I found no non-Google hardware reported as having reproduced the result, so this verification route is untested.
- Google has the most recent published classical-simulation analysis of its own advantage claims (TNBP). Independent classical attempts, if any, were not found in this research.

### Gaps
- No independent replication of Quantum Echoes on other hardware was found.
- No published independent classical simulation of the 65-qubit OTOC experiment was found.
- A 2026 Duke hackathon posted a classical-OTOC challenge (via search summary), with no published result found.
- No classical simulation challenging the 2024 Willow RCS "10^25 years" figure was found; the search was not exhaustive because of quota.
- Further 2019-Sycamore classical simulations (e.g., Sunway 2021; "Leapfrogging Sycamore" 2024; any Google-acknowledged seconds-scale Frontier estimate) were not verified this session.
- No Google demonstration of lattice surgery between surface-code logical qubits, or of a below-threshold logical two-qubit gate, was found.
- AlphaQubit (Google DeepMind and Google Quantum AI neural decoder, Nature 2024) and any 2025–26 successor were not verified.
- Unverified claims not to rely on:
  - A secondary site (mylistingo.com, via search summary) claims a March 2026 result of 12 logical qubits with gate fidelities above 99.99%. It is uncorroborated by any Google source.
  - The Science World Report PRL "logical qubit stability" claim (Sept 2026) is likewise uncorroborated.

---

## 9. Physical and engineering limits on Google's superconducting path (with numbers)

### Takeaway
Google's own target, about 1,000,000 physical qubits in a "room-sized" machine (2021), is about 9,500x Willow's 105 qubits. The main published constraints are:
- Decoder speed: 63 µs average latency against a 1.1 µs cycle.
- Correlated error bursts: about once per hour on Willow; cosmic rays.
- Time-correlated errors lasting up to 40 cycles.
- Leakage.
- Two-qubit gate error variability: CZ 0.33% ± 0.18%, about 3x the 0.1% assumed in the RSA-2048 estimate.
- Wiring and cryogenic integration, which motivated the Atlantic Quantum acquisition.

Google's addition of neutral atoms in 2026 explicitly cites the difficulty of scaling superconducting qubit count.

### Cited Findings
**Scale and footprint**
- [2021-05-18, older] Target is "1,000,000 physical qubits" in a "room-sized" error-corrected computer, about 1,000 physical qubits per logical qubit. Cryostats are about the size of three household refrigerators at about 10 mK — [Google blog, 2021-05-18](https://blog.google/technology/ai/unveiling-our-new-quantum-ai-campus/) [CC]
- [2026-03-24] Next superconducting goal is "tens of thousands of qubits". Superconducting processors are "easier to scale in circuit depth" while neutral atoms are "easier to scale in qubit count" — about 10,000 atoms, with millisecond cycles vs about 1 µs superconducting cycles — [Google blog, 2026-03-24](https://blog.google/innovation-and-ai/technology/research/neutral-atom-quantum-computers/) [CC]

**Wiring and control integration**
- [2025-10-02/03] Atlantic Quantum's approach puts qubits and superconducting control electronics in the same cold stage. This is reported to reduce complexity and noise and enable modular scaling, and Neven tied it to scaling Google's superconducting hardware — [Gunderson Dettmer, 2025-10-02](https://www.gunder.com/en/news-insights/client-news/gunderson-dettmer-represented-atlantic-quantum-in-its-acquisition-by-google) [IND]; [The Quantum Insider, 2025-10-03](https://thequantuminsider.com/2025/10/03/atlantic-quantum-joins-google-quantum-ai/) [IND]

**Decoder latency and reaction time**
- [2024] Willow real-time decoder: 63 µs average latency at distance-5, 1.1 µs cycle, sustained for up to 1M cycles — [arXiv:2408.13687 / Nature 638](https://arxiv.org/abs/2408.13687) [CC]
- [2025-05-21] The RSA-2048 estimate assumes a 10 µs control-system reaction time and a 1 µs cycle — [arXiv:2505.15917](https://arxiv.org/abs/2505.15917) [CC]
- [2026-03-31] Gidney notes QLDPC-code decoder reaction-time assumptions are harder to meet than surface-code ones — [The Quantum Insider, 2026-03-31](https://thequantuminsider.com/2026/03/31/q-day-just-got-closer-three-papers-in-three-months-are-rewriting-the-quantum-threat-timeline/) [IND]

**Correlated errors and cosmic rays**
- [2024] Repetition codes to distance-29 are limited by rare correlated events, about once per hour or about 3×10^9 cycles — [arXiv:2408.13687](https://arxiv.org/abs/2408.13687) [CC]
- [2021 preprint; Nature Physics 18, 107–111 (2022), older] Cosmic-ray-induced error bursts "simultaneously and severely limit the energy coherence of all qubits". They violate the small, uncorrelated-error assumption that QEC's exponential suppression relies on, so mitigation is needed to scale — [McEwen et al., "Resolving catastrophic error bursts from cosmic rays in large arrays of superconducting qubits", arXiv:2104.05219](https://arxiv.org/abs/2104.05219) [CC]
- [2026-01-13] In the standard surface-code circuit, time-correlated errors persist up to 40 cycles. The "walking" circuit cuts them by over 10x and is paired with data-qubit leakage removal (DQLR) — [Google Research blog, 2026-01-13](https://research.google/blog/dynamic-surface-codes-open-new-avenues-for-quantum-error-correction/) [CC]
- [2023-02-22, older] At very low error rates, new error mechanisms appear that are not yet observable in surface codes — [Google Research blog, 2023-02-22](https://research.google/blog/suppressing-quantum-errors-by-scaling-a-surface-code-logical-qubit/) [CC]

**Leakage, error rates and variability**
- [2024-12-09] Willow reset options include leakage removal for the |2⟩ state only — [Willow spec sheet](https://quantumai.google/static/site-assets/downloads/willow-spec-sheet.pdf) [CC]
- [2024-12-09] Error and coherence spreads (spec sheet, [CC]):
  - QEC chip CZ error 0.33% ± 0.18%; measurement error 0.77% ± 0.21%; T1 68 ± 13 µs.
  - RCS chip T1 98 ± 32 µs.
  - The two chips trade qubit geometry for EM shielding against coherence.

**Magic-state overhead**
- [2026-10-15] "Some estimates" put magic-state overhead at up to 95% of machine capacity — [Google blog, 2026-10-15](https://blog.google/innovation-and-ai/models-and-research/quantum-computing/magic-state-cultivation-quantum-computing/) [CC]. Traditional distillation is projected at 90–95% of physical qubits, and the cultivation demonstration retained about 8% of attempts — [Quantum Computing Report, 2026-10-15](https://quantumcomputingreport.com/google-quantum-ai-demonstrates-magic-state-cultivation-on-willow-processor-in-science-milestone/) [IND]

**Physical-error requirements**
- [2023-02-22, older] Sycamore physical errors were about 1 in 10^4 to 1 in 10^2. Industrially relevant circuits need about 1 in 10^6 to 1 in 10^9. Squeezing three to six orders of magnitude from physical qubits alone is "unlikely", so QEC is required — [Google Research blog, 2023-02-22](https://research.google/blog/suppressing-quantum-errors-by-scaling-a-surface-code-logical-qubit/) [CC]

### Inferences
All arithmetic below is mine, from the cited figures.
- Scale-up: 1,000,000 / 105 ≈ 9,500x more physical qubits than Willow.
- Decoder latency: 63 µs ≈ 57 surface-code cycles at 1.1 µs, about 6x the 10 µs reaction time assumed in Google's RSA-2048 estimate. Average latency and reaction time are not identical metrics, so this comparison is approximate.
- Gate error: Willow's QEC-chip CZ error (0.33%) is about 3.3x the uniform 0.1% assumed in the RSA-2048 and ECC estimates. The RCS chip's iSWAP-like error (0.14%) is closer, but that chip was not the one used for QEC.
- Correlated events: at 909,000 cycles/s, 3×10^9 cycles ≈ 55 minutes, consistent with "about once per hour". Unless mitigated, the rate of chip-wide events per unit time would be expected to grow with total chip area. This is a qualitative inference; no scaling figure was found.
- Strategy signal: buying a cryo-integrated control-electronics team and starting a neutral-atom program both address qubit-count scaling, which Google itself names as superconducting qubits' weaker axis.

### Gaps
- Not found:
  - Google figures for wiring count per qubit, cryostat cooling power, or fridge count for a 1M-qubit machine.
  - Data on fabrication yield or wafer-to-wafer variability.
  - A Google figure for the rate of correlated bursts after mitigation on Willow-class chips at larger scale.
- Not verified this session:
  - Leakage-mitigation results beyond the spec-sheet reset option and DQLR (e.g., Google's 2023 Nature Physics leakage paper).
  - Decoder hardware roadmap (Google's open-source Tesseract and Chromobius decoders exist on GitHub, but their performance was not reviewed).

---

## 10. Evidence assessment: how solid is each major claim, and why

### Takeaway
Ranked by evidential strength:
1. **Strongest:** Google's peer-reviewed, narrowly scoped QEC measurements (Willow memory, colour codes, dynamic codes, magic state cultivation). They come with quantified uncertainties and independent experts accept them as genuine, but they are small-scale and largely memory or single-logical-qubit results.
2. **Weaker:** Beyond-classical claims. The 2019 claim was overtaken; the 2024 claim is unrefuted but not directly verifiable; the 2025 Quantum Echoes claim is peer-reviewed but contested, with no outside replication.
3. **Not evidence of capability:** Resource estimates and executive timelines. These are theoretical or forecast statements.

### Cited Findings
| Claim | Assessment | Basis |
|---|---|---|
| Below-threshold surface-code memory (Willow, Λ = 2.14 ± 0.02; 0.143% per cycle at distance 7; 2.4x beyond break-even) | Solid for what is claimed | Peer-reviewed in Nature with quantified uncertainties ([arXiv:2408.13687](https://arxiv.org/abs/2408.13687) [CC]). An independent theorist called it "a very important threshold that's now been crossed" ([Aaronson, 2024-12-10](https://scottaaronson.blog/?p=8525) [IND]). Limits: one logical qubit, memory only, no below-threshold logical gates ([Wikipedia summary of APS Physics 17, 176](https://en.wikipedia.org/wiki/Willow_processor) [IND]); about 10^3 above the 10^-6 target; correlated-event floor about hourly ([arXiv:2408.13687](https://arxiv.org/abs/2408.13687) [CC]). |
| 2019 "quantum supremacy" (200 s vs 10,000 years) | Superseded as a speed claim | IBM estimated 2.5 days classically ([IBM, 2019-10-22](https://www.ibm.com/quantum/blog/on-quantum-supremacy) [IND]). An executed tensor-network simulation took 15 hours on 512 GPUs, with seconds projected on exascale ([Pan et al., PRL 2022](https://arxiv.org/abs/2111.03011) [IND]). Scientific American describes it as overtaken ([Scientific American, 2025-10-22/23](https://www.scientificamerican.com/article/google-measures-quantum-echoes-on-willow-quantum-computer-chip/) [IND]). |
| 2024 Willow RCS: "5 minutes vs 10^25 years" | Unrefuted in sources found, but unverifiable by construction; only as strong as the extrapolation and current best classical algorithms | Validation is indirect, by extrapolation from smaller circuits ([Aaronson, 2024-12-10](https://scottaaronson.blog/?p=8525) [IND]). XEB fidelity is only 0.1% ([Willow spec sheet](https://quantumai.google/static/site-assets/downloads/willow-spec-sheet.pdf) [CC]). RCS has no known practical application, a point Google makes itself when it calls the next challenge a "useful, beyond-classical" computation ([Google blog, 2024-12-09](https://blog.google/technology/research/google-willow-quantum-chip/) [CC]). |
| Quantum Echoes "verifiable quantum advantage" (13,000x) | Plausible but contested; not independently replicated | Peer-reviewed, but referees "split" on the degree of advantage ([Scientific American](https://www.scientificamerican.com/article/google-measures-quantum-echoes-on-willow-quantum-computer-chip/) [IND]). One independent theorist calls it beyond current classical methods (Xu, same source). Nature news quotes skepticism (Sels, via search summary). "Verifiable" means repeatable on another quantum computer of the same calibre, which has not been done outside Google ([Google blog, 2025-10-22](https://blog.google/innovation-and-ai/technology/research/quantum-echoes-willow-verifiable-quantum-advantage/) [CC]). The main TNBP rebuttal's authors include Google-affiliated researchers ([arXiv:2604.15427](https://arxiv.org/abs/2604.15427)). Google states the molecular application is not yet beyond classical ([IEEE Spectrum](https://spectrum.ieee.org/quantum-echoes) [IND]). |
| Colour code / lattice-surgery logic | Solid as early-stage demonstrations; performance modest | Peer-reviewed in Nature: Λ = 1.56 (below the surface code's 2.14); teleportation fidelity 86.5–90.7%; magic injection above 99% only with post-selection ([arXiv:2412.14256](https://arxiv.org/abs/2412.14256) [CC]). |
| Magic state cultivation (99.99%, about 40x) | Solid as a first demonstration; scalability unproven | Peer-reviewed in Science. Only about 8% of attempts retained; fidelity bounded by a self-referential protocol; small distances (3 grafted into 5) ([Quantum Computing Report, 2026-10-15](https://quantumcomputingreport.com/google-quantum-ai-demonstrates-magic-state-cultivation-on-willow-processor-in-science-milestone/) [IND]). Google says larger-scale demonstration is still needed ([Google blog, 2026-10-15](https://blog.google/innovation-and-ai/models-and-research/quantum-computing/magic-state-cultivation-quantum-computing/) [CC]). |
| RSA-2048 in under 1M qubits; ECDLP-256 in under 500k qubits | Credible as theory, conditional on assumptions not yet met at scale | Preprints: the RSA paper had no journal reference at fetch time ([arXiv:2505.15917](https://arxiv.org/abs/2505.15917) [CC]); the ECC paper withholds circuits and is validated by a zero-knowledge proof ([arXiv:2603.28846](https://arxiv.org/abs/2603.28846) [CC]). They assume a uniform 0.1% (10^-3) error, 1 µs cycle and 10 µs reaction time. Google's own security team treats them as reason enough to accelerate PQC ([Google blog, 2026-03-25](https://blog.google/innovation-and-ai/technology/safety-security/cryptography-migration-timeline/) [CC]). Outside commentators called them "serious" and "sobering"; a competing estimate (Iceberg, under 100k qubits) depends on unproven QLDPC decoding ([The Quantum Insider, 2026-03-31](https://thequantuminsider.com/2026/03/31/q-day-just-got-closer-three-papers-in-three-months-are-rewriting-the-quantum-threat-timeline/) [IND]). |
| "Commercially relevant … by the end of this decade" / "within five years" | Forecasts, not evidence | Stated by Google executives ([Google blog, 2026-03-24](https://blog.google/innovation-and-ai/technology/research/neutral-atom-quantum-computers/) [CC]; [The Quantum Insider, 2025-02-05](https://thequantuminsider.com/2025/02/05/google-quantum-ai-head-sees-commercial-quantum-within-five-years/) [IND]). Google's own 2023 projection of the M3 era as "a few years" out has not yet been met ([Google Research blog, 2023-02-22](https://research.google/blog/suppressing-quantum-errors-by-scaling-a-surface-code-logical-qubit/) [CC]; [Google Research blog, 2026-01-13](https://research.google/blog/dynamic-surface-codes-open-new-avenues-for-quantum-error-correction/) [CC]). DARPA's QBI lists Google at Stage A ([DARPA](https://www.darpa.mil/research/programs/quantum-benchmarking-initiative) [IND]). |

### Inferences
- The consistent pattern is that Google's measured, peer-reviewed results are specific, while their framing in Google's own announcements is broader. For example, the "verifiable quantum advantage" framing contrasts with Google's own researcher saying the application "aren't beyond classical yet".
- Independent scrutiny is strongest for the 2019 and 2024 RCS claims and Willow QEC (Aaronson, IBM, CAS group) and thinnest for the 2025–26 results:
  - Quantum Echoes: referee split, no replication.
  - Magic state cultivation: no outside commentary found.
  - ECC estimate: commentary mostly from the crypto industry.

### Gaps
- No independent technical review was found of:
  - the October 2026 Science magic-state paper;
  - the January 2026 dynamic-surface-code paper;
  - the Atlantic Quantum or neutral-atom strategy.
- No independent verification of DARPA QBI Stage A evaluation outcomes for Google is public.
- Because the search quota ran out, independent 2026 commentary (e.g., Aaronson posts after 2024; Physics World, Quanta, Nature News & Views on 2025–26 Google results; Reuters, FT or Bloomberg coverage of the neutral-atom move or PQC timeline) could not be sought systematically.
