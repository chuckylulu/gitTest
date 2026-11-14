# Science and engineering limits by modality (superconducting, trapped-ion, neutral-atom, photonic) — independent record as of 14 Nov 2026

Conventions used throughout. Source labels: **[IND]** = independent of the named companies (academic group, government, national lab, independent press or commentary); **[ACAD+CO]** = academic paper with company co-authors; **[CO]** = company-controlled (company authors, press releases, spec sheets, roadmaps, earnings calls). "Trade press" (The Quantum Insider, Quantum Computing Report) and commentary sites (PostQuantum.com, run by consultant Marin Ivezic) are labelled [IND] but often relay company claims; where they do, the claim itself is labelled [CO]. Items marked "(search summary)" come from a search-engine summary of the page, not a full fetch. Items marked "(prior knowledge)" are older bibliographic facts not re-fetched in this session. "Older" = published before 2025. arXiv preprints are not peer reviewed unless a journal reference is given. The session's web-search budget ran out partway through (shared limit of 200 searches per turn), so some planned checks were not made; see each Gaps section.

## 1. Best published metrics per modality, main scaling limits, and how independent bodies assess them

### Takeaway
As of Nov 2026, almost every headline hardware metric is company-reported. The best physical gate fidelities are in trapped ions (Quantinuum Helios: mean two-qubit infidelity 7.9×10⁻⁴). Superconducting chips are the fastest (about 1 µs per error-correction cycle) but have mean two-qubit errors of about 0.1–0.4%. Neutral atoms lead on qubit count (6,100–11,000 trapped atoms), but published two-qubit fidelity is still below 99.9% and operations take milliseconds. Photonics (PsiQuantum) reports high component fidelities, but only after excluding photon loss, and has shown no logical qubit. The main government programme that tests hardware independently, DARPA's Quantum Benchmarking Initiative (QBI), only began its hardware-testing stage (Stage C) in Oct 2026.

### Cited Findings

**Superconducting (Google, IBM, IQM; competitor USTC)**
- Google Willow spec sheet (published 9 Dec 2024, older) [CO]: 105 qubits, average connectivity 3.47. On the error-correction chip: single-qubit error 0.035% ± 0.029%, CZ error 0.33% ± 0.18% (mean, measured with all qubits running at once), measurement error 0.77% ± 0.21%, mean T1 68 ± 13 µs, 909,000 error-correction cycles per second (1.1 µs cycle). On the random-circuit-sampling (RCS) chip: two-qubit (iSWAP-like) error 0.14% ± 0.052%, measurement error 0.67% ± 0.51%, T1 98 ± 32 µs, 63,000 circuit repetitions per second. The sheet says the two chips have different T1 because of a trade-off between electromagnetic shielding and coherence — [Google Willow spec sheet](https://quantumai.google/static/site-assets/downloads/willow-spec-sheet.pdf)
- Google, "Quantum error correction below the surface code threshold" (arXiv 24 Aug 2024; *Nature* 638, 920–926 (2025)) [CO]: the 101-qubit distance-7 code had a logical error of 0.143% ± 0.003% per cycle. Each distance step of 2 cut errors by Λ = 2.14 ± 0.02. The logical memory outlived the best physical qubit by 2.4 ± 0.3×. Real-time decoding had a mean latency of 63 µs at distance 5, sustained for up to 1 million cycles at a 1.1 µs cycle. Repetition codes up to distance 29 were limited by rare correlated error events, about once an hour (~3×10⁹ cycles) — [arXiv:2408.13687](https://arxiv.org/abs/2408.13687); [DOI 10.1038/s41586-024-08449-y](https://doi.org/10.1038/s41586-024-08449-y)
- IBM Nighthawk, announced 12 Nov 2025 [CO, reported by IND commentary dated 13 Nov 2025]: 120 qubits on a square lattice with 218 tunable couplers (4 neighbours per qubit). Runs circuits of up to 5,000 two-qubit gates; roadmap of ~7,500 gates in 2026, ~10,000 in 2027, and 15,000 gates on 1,000+ qubits by 2028. The experimental Loon chip has long-range "c-couplers" and fast reset; its qubit count is unconfirmed (reports say ~112). An FPGA running the Relay-BP decoder has latency under 480 ns, which IBM calls ~10× faster than other recent approaches; this is IBM's own comparison, not an independent benchmark. Fabrication moved to 300 mm wafers at Albany NanoTech. IBM targets quantum advantage by end-2026 and a fault-tolerant computer by 2029 — [PostQuantum, IBM Loon/Nighthawk](https://postquantum.com/industry-news/ibm-loon-nighthawk/)
- Third-party error correction on IBM's cloud Nighthawk r2 (arXiv 16 Oct 2026; author affiliations not verified) [IND/third party]:
  - Performance varied across chip placements, attributed to differences in qubit quality.
  - Going from protected distance 3 to 6 cut the per-round logical error from 0.53% to 0.24% (Z memory) and 0.52% to 0.22% (X memory), i.e. Λ = 1.68 and 1.85 with maximum-likelihood decoding.
  - Over memory runs of up to 150 rounds, "the distance advantage weakens", with long-lived correlations that may reflect a persistent error component.
  - [arXiv:2610.23840](https://arxiv.org/abs/2610.23840)
- 156-qubit heavy-hex IBM-class processor (arXiv 8 Oct 2026; academic, may include an IBM co-author — unverified) [IND/ACAD+CO]: states that "fabrication of monolithic superconducting devices produces unavoidable heterogeneity", so underperforming qubits and couplers had to be excluded from the schedule — [arXiv:2610.11658](https://arxiv.org/abs/2610.11658)
- USTC Zuchongzhi 3.0 (arXiv 16 Dec 2024, older) [IND competitor academic]: 105 qubits; single-qubit fidelity 99.90%, two-qubit 99.62%, readout 99.18% — [arXiv:2412.11924](https://arxiv.org/abs/2412.11924)
- USTC Zuchongzhi 3.2 (*Phys. Rev. Lett.*, 22 Dec 2025) [IND competitor academic, via trade press]: 107 qubits; readout error 0.95% within a 300 ns window — [Quantum Computing Report](https://quantumcomputingreport.com/ustcs-zuchongzhi-3-2-achieves-below-threshold-qec-milestone/)
- IQM: no metrics could be retrieved or verified this session (see Gaps).

**Trapped ions (Quantinuum, IonQ)**
- Quantinuum Helios (arXiv 7 Nov 2025) [CO]: 98 ¹³⁷Ba⁺ hyperfine qubits in a quantum charge-coupled device (QCCD, ions shuttled between zones). All-to-all connectivity comes from a rotatable ion-storage ring joined to two operation regions through a junction. Average infidelities across all zones: single-qubit 2.5(1)×10⁻⁵, two-qubit 7.9(2)×10⁻⁴, state preparation and measurement (SPAM) 4.8(6)×10⁻⁴. The authors say none of these errors is fundamentally limited — [arXiv:2511.05465](https://arxiv.org/abs/2511.05465)
- IonQ [CO, reported by IND commentary, 7 May 2026]:
  - Claims a 99.99% two-qubit gate fidelity "world record".
  - "Walking Cat" architecture paper (22 Apr 2026): 110 logical qubits from 2,514 physical qubits.
  - Targets 2 million physical and 80,000 logical qubits by 2030; the June 2025 roadmap had ~1,600 logical qubits in 2028.
  - On the Q1 2026 earnings call, the CEO said IonQ expects the logical-qubit count "required to challenge RSA 2048" in 2028–2029. The commentator argues this conflicts with IonQ's own 2030 full-fault-tolerance timeline.
  - [PostQuantum on IonQ](https://postquantum.com/security-pqc/ionq-q-day-claim-rsa-2048-earnings/)
- One analysis notes that IonQ's >99.99% claim "is not the same as proving logical execution" [IND, search summary] — [ThesisCheck teardown, Jul 2026](https://thesischeck.io/teardown/ionq-quantum-advantage-premium-2026-07)
- Speed is the ion bottleneck in resource models. A third-party (Iceberg Quantum) estimate assumes trapped ions at a 1 ms cycle and 0.01% error. Under that assumption RSA-2048 within one month needs 3.1 million physical qubits (Feb 2026 version) or 2.7 million (May 2026 version), against ~98,000 / ~94,000 for superconducting qubits at 1 µs and 0.1% [CO estimate; IND commentary] — [PostQuantum Pinnacle critique](https://postquantum.com/post-quantum/pinnacle-architecture-break-rsa-2048-critical/)
- Single-ion coherence above one hour (Wang et al., *Nat. Commun.* 12, 233 (2021); older, prior knowledge) [IND] — [DOI 10.1038/s41467-020-20330-w](https://doi.org/10.1038/s41467-020-20330-w)

**Neutral atoms (QuEra; competitors Atom Computing, Caltech, Harvard, USTC, Tsinghua, Infleqtion)**
- Review "Neutral Atom Quantum Computing: Principles, Routes, Progress, and Challenges" (arXiv Aug 2026; Information Engineering University, China) [IND]:
  - Two-qubit (CZ) fidelity: 99.5% (Harvard/QuEra/MIT, Oct 2023, 60 atoms) and 99.84% (USTC 2025, Lin et al. *PRL*, per the review's Table 1). States that >99.9% "is not achieved".
  - Error budget: Rydberg spontaneous emission 0.05–0.1%, laser phase noise 0.1–0.2%, thermal motion ~0.1%.
  - Single-qubit fidelity 99.97% (USTC 2025) and 99.98% (Caltech, Sept 2025); readout fidelity 99.92% (USTC 2025).
  - Coherence: T2 of 12.6 s (caesium, Caltech), 40 s echo T2 (strontium nuclear spin, Atom Computing), 300 ms (rubidium).
  - Arrays: ~6,100 caesium atoms in 12,000 sites (Caltech, Sept 2025); an average of 11,022 atoms in an 18,225-site array, 60.5% filled (Tsinghua, Jun 2026 arXiv); >3,000 atoms run continuously (Harvard) with 300,000 atoms/s replenished.
  - Trap lifetime ~60 s in optical tweezers vs 6,000 s in a cryogenic setup. Loss below 1% per parallel move (Fudan). A defect-free 2,024-atom array assembled in 60 ms (USTC); a 10,000-atom rearrangement algorithm runs in 20 ms (Tsinghua).
  - "No measured QEC cycle time" is reported; a typical full experimental cycle is ~100 ms (Fig. 3 caption).
  - Overhead: ~100–200 physical qubits per logical qubit at 99% fidelity vs 20–50 at 99.9%.
  - Hanyuan 2 cabinet draws less than 7 kW.
  - [arXiv:2608.05010](https://arxiv.org/abs/2608.05010)
- Harvard/MIT/QuEra (arXiv 25 Jun 2025; *Nature* 649, 39–46 (2026)) [ACAD+CO]: reconfigurable arrays of up to 448 atoms used to build all key elements of a fault-tolerant architecture (error-correction details in Section 2). Mid-circuit qubit re-use "raises experimental cycle rates by two orders of magnitude" — [arXiv:2506.20661](https://arxiv.org/abs/2506.20661); [Nature DOI 10.1038/s41586-025-09848-5](https://www.nature.com/articles/s41586-025-09848-5)
- Atom Computing [CO]: 1,180+ qubits (2023). Its "Magne" plan is 50 logical qubits from 1,225 physical qubits in 2027 (company plan, as listed in the review) — [arXiv:2608.05010](https://arxiv.org/abs/2608.05010)
- Resource-estimate assumptions for atoms: 1 ms measurement time (Xue & Covey, May 2026) [IND] — [arXiv:2605.03951](https://arxiv.org/abs/2605.03951). 1 ms cycle at 0.1% error (Pinnacle critique) [IND commentary] — [PostQuantum](https://postquantum.com/post-quantum/pinnacle-architecture-break-rsa-2048-critical/)

**Photonics (PsiQuantum)**
- PsiQuantum, "A manufacturable platform for photonic quantum computing" (arXiv 26 Apr 2024; *Nature*, Feb 2025) [CO]:
  - Dual-rail qubit SPAM fidelity 99.98% ± 0.01%.
  - Hong-Ou-Mandel visibility (indistinguishability of photons) between independent sources 99.50% ± 0.25%.
  - Two-qubit fusion fidelity 99.22% ± 0.12%; chip-to-chip interconnect fidelity 99.72% ± 0.04%.
  - All fidelities are stated as "not accounting for loss". Next-generation low-loss components are previewed without numbers.
  - [arXiv:2404.17570](https://arxiv.org/abs/2404.17570)
- Further figures from the same paper as reported by PostQuantum (28 Feb 2025) [IND commentary on CO data]:
  - Built at GlobalFoundries on 300 mm wafers; interconnect measured over 42 m of fibre.
  - Silicon-nitride waveguide loss 0.5 ± 0.3 dB/m (multimode).
  - Photon-number-resolving (PNR) detectors: median efficiency 98.9%, resolving up to 4 photons.
  - Barium titanate (BTO) phase shifter 0.33 dB·V; edge-coupler loss 52 ± 12 mdB.
  - Cryostat: 2 K base temperature, up to 20 W cooling, >1,000 electrical connections, up to 200 optical inputs/outputs.
  - Commentator: fusion-based quantum computing (FBQC) tolerates "roughly 10% total optical loss"; silicon waveguides at ~0.1 dB/cm exceed this budget on a large chip, and the system "is not yet within budget".
  - [PostQuantum](https://postquantum.com/quantum-research/psiquantum-photonic-platform-nature/)
- Loss thresholds from PsiQuantum's 2025 modelling [CO study, IND trade press, 17 Jun 2025]: the original FBQC design tolerates 10.4% loss per fusion, equal to 2.7% per photon. "Exposure-based adaptivity" raises thresholds to 18.8%, and a 4-qubit code with adaptivity reaches 5.7%. These use different threshold definitions and are not directly comparable — [The Quantum Insider](https://thequantuminsider.com/2025/06/17/psiquantum-study-maps-path-to-loss-tolerant-photonic-quantum-computing/)
- PsiQuantum status at the Cisco Quantum Summit (talk 7 Oct 2026; write-up 18 Oct 2026) [CO statements; writer's critique IND]:
  - Chip-to-fibre loss below 0.2 dB is "fairly routine", ~0.1 dB in good conditions; the best 0.06 dB was not a complete glued package. An on-chip polarisation controller loses ~15 mdB.
  - A 250 m link reached 99.7% fidelity, but its optical loss was admitted to be poor.
  - Source chip with 24 single-photon sources; a 48-source chip has been taped out. A 64×64 switch has been taped out, 72×72 is in development, and 128×128 is planned for the first utility-scale system. BTO devices have a 10 GHz electro-optic response.
  - Detectors resolve 0–8 photons. "One or two" components remain below fault-tolerance spec, which Shadbolt hopes to fix within ~1 year.
  - Chips run at ~2.3 K, eventually ~4 K.
  - Writer's critique: multiplexing gains are not error-correction break-even, and component test volumes are not logical qubits.
  - [Cisco Quantum Summit 2026 write-up](https://netcreat.substack.com/p/cisco-quantum-summit-2026-day-2-psiquantum)
- A 2026 search found no PsiQuantum result measuring loss at system level, and no PsiQuantum logical-qubit demonstration (search summary). Same write-up: PsiQuantum must link its manufactured components into a large system that performs stable error-corrected operations despite photon loss and probabilistic fusion — [Cisco write-up](https://netcreat.substack.com/p/cisco-quantum-summit-2026-day-2-psiquantum)

**Independent and government assessments**
- DARPA QBI Stage C (7 Oct 2026) [IND government; IBM statement CO]:
  - Atom Computing, Diraq, IBM and IonQ advanced to Stage C. Microsoft and PsiQuantum were already there through the earlier US2QC programme, so six firms are now in Stage C.
  - Not yet promoted from Stage B: Nord Quantique, Photonic Inc., Quantinuum, Quantum Motion, QuEra, Silicon Quantum Computing, Xanadu.
  - In Stage C "independent experts extensively test and measure quantum hardware" (IBM's description). DARPA aims to find whether any approach can reach utility scale by 2033.
  - IonQ says its Stage C agreement is worth up to $300M through 2029 (search summary).
  - Sources: [DCD](https://www.datacenterdynamics.com/en/news/darpa-announces-four-companies-advancing-to-final-stage-of-its-quantum-benchmarking-initiative/); [Quantum Computing Report](https://quantumcomputingreport.com/darpa-selects-atom-computing-diraq-ibm-and-ionq-for-final-stage-c-verification-under-quantum-benchmarking-initiative/); [IBM newsroom](https://newsroom.ibm.com/2026-10-07-ibm-advances-to-stage-c-of-darpa-quantum-benchmarking-initiative); [DARPA QBI page](https://www.darpa.mil/research/programs/quantum-benchmarking-initiative). Contradicted only by an outdated explainer placing IBM in Stage B — [qntonsol](https://www.qntonsol.com/learn/darpa-quantum-benchmarking-initiative-explained.html)
- GAO-27-108740 (public release 7 Oct 2026) [IND government]: none of the 24 CFO Act agencies has fully prepared to move to post-quantum cryptography. Most industry experts expect a cryptographically relevant quantum computer "possibly as soon as the 2030s"; some give a 10–20 year window — [ExecutiveGov](https://www.executivegov.com/articles/gao-federal-agencies-quantum-cryptography-readiness)
- NERSC / Lawrence Berkeley National Lab, report LBNL-2001699 (arXiv 11 Sep 2025) [IND national lab]: public roadmaps of 10 companies predict a "dramatic increase in capabilities over the next five to ten years". A "significant overlap" is emerging with the algorithmic requirements of materials science, chemistry and high-energy physics, which make up >50% of NERSC's workload — [arXiv:2509.09882](https://arxiv.org/abs/2509.09882)
- Eisert & Preskill, "Mind the gaps" (arXiv 22 Oct 2025; v3 21 May 2026) [IND academic]: four transitions are still needed — error mitigation → active detection and correction; rudimentary correction → scalable fault tolerance; heuristic → verifiable algorithms; exploratory simulators → credible simulation advantage — [arXiv:2510.19928](https://arxiv.org/abs/2510.19928)
- Scale gap (PostQuantum, 1 Mar 2026, updated 29 Oct 2026) [IND commentary]: current systems have ~100–160 qubits, a 100–1,000× gap to architectures needing ~10⁵–10⁶ qubits — [PostQuantum](https://postquantum.com/post-quantum/pinnacle-architecture-break-rsa-2048-critical/)

### Inferences
- Two-qubit error on current flagships (company or competitor figures): ions are lowest (Helios ~7.9×10⁻⁴). Superconducting (Willow CZ ~3.3×10⁻³ for error correction, ~1.4×10⁻³ for iSWAP-like RCS gates; Zuchongzhi 3.0 ~3.8×10⁻³) and neutral atoms (~1.6×10⁻³ if the unverified 99.84% is accepted, 5×10⁻³ for Harvard's 99.5%) overlap. Clock speed runs the other way: superconducting about 1 µs per cycle against ms-scale cycles assumed for ions and atoms, roughly 10³× slower.
- Independent measurements of the named companies' hardware are rare. The examples found are third parties running error correction on IBM cloud devices and Sandia running on Quantinuum Helios (Section 2). DARPA Stage C is the first systematic independent test, and only IBM, IonQ and PsiQuantum among the named companies are in it as of Nov 2026.
- For photonics, high conditional fidelities (99.2–99.98%) do not address the binding constraint, which is total photon loss against a threshold of about 2.7% per photon in the original FBQC model.

### Gaps
- Search budget ran out before I could retrieve IBM Heron r3 / Nighthawk median two-qubit error, T1/T2 or EPLG numbers (company or independent); IQM figures (CZ fidelity, coherence — I recall IQM press claims of ~99.9% CZ and ms-scale T1 in 2025, unverified); IonQ's primary 99.99% paper; Oxford Ionics or academic ion records; IonQ Tempo or #AQ figures; and qubit counts of IonQ systems.
- The ion QEC cycle duration on Helios was not found; the 1 ms used in resource estimates is an assumption, not a measurement.
- I could not verify the 99.84% neutral-atom CZ figure the review attributes to USTC (2025), or 2025–2026 two-qubit records from Atom Computing, Infleqtion, Caltech or Princeton.
- I recall, but did not verify, superconducting coherence records such as 2D tantalum-on-silicon transmons with T1 > 1 ms (Princeton, 2025) and fluxonium two-qubit fidelity ~99.9% (MIT).
- I found no 2025–2026 formal review articles (Nature Reviews Physics, Reviews of Modern Physics, PRX Quantum) or 2025–2026 NASEM, DOE, NIST, UK NQCC or RAND hardware assessments. The NASEM 2019 report is the last National Academies assessment surfaced.

## 2. Error correction: below-threshold and logical-qubit status, logical gates, magic states, real-time decoding, and what is still undemonstrated

### Takeaway
Λ (lambda) is the factor by which logical errors fall at each code-distance step; Λ > 1 means the hardware is below threshold. Error suppression with growing code distance has now been shown in three modalities:
- **Superconducting:** Google Λ = 2.14 at distance 7; USTC Λ = 1.40 at distance 7; third parties on IBM Λ ≈ 1.7–1.9 from distance 3 to 6.
- **Neutral atoms:** Harvard/QuEra "2.14× below threshold" in a four-round circuit.
- **Trapped ions:** Quantinuum color code with Λ = 12 and logical error as low as 5×10⁻⁶ (company preprint, Oct 2026).

Small-distance logical gates (lattice surgery, transversal gates) and magic-state cultivation and distillation exist. Still undemonstrated: long, deep logical algorithms with real-time decoding and a steady supply of non-Clifford (magic) states; logical error ≤10⁻⁶–10⁻⁸ sustained inside a computation; large quantum LDPC (qLDPC) codes with real-time decoding; month-scale operation; and any photonic logical qubit. Many trapped-ion "logical qubit" headline counts use error detection with postselection.

### Cited Findings

**Superconducting**
- Google Willow, distance-7 below threshold (*Nature* 638, 2025): Λ = 2.14 ± 0.02; 0.143% ± 0.003% logical error per cycle; 2.4× beyond break-even; real-time decoding at distance 5 with 63 µs mean latency [CO] — [arXiv:2408.13687](https://arxiv.org/abs/2408.13687)
- Google magic-state cultivation on a superconducting processor (arXiv 15 Dec 2025) [CO]: includes code-switching into a surface code. Magic-state error fell 40× to a state fidelity of 0.9999(1), keeping 8% of attempts after postselection — [arXiv:2512.13908](https://arxiv.org/abs/2512.13908)
- USTC Zuchongzhi 3.2 (*PRL*, 22 Dec 2025) [IND competitor academic, via trade press]: distance-7 surface code with Λ = 1.40(6) using 97 of 107 qubits. An all-microwave leakage-reduction unit plus fast ancilla reset cut average leakage 72× after 40 cycles. Commentators note it does not yet show interacting logical qubits or logical operations — [Quantum Computing Report](https://quantumcomputingreport.com/ustcs-zuchongzhi-3-2-achieves-below-threshold-qec-milestone/); [PostQuantum](https://postquantum.com/quantum-research/zuchongzhi-3-2-belowthreshold/); [Geo News](https://www.geo.tv/latest/641797)
- Chinese superconducting lattice surgery (arXiv 4 Jun 2026) [IND academic, affiliations not verified]: lattice surgery between two distance-3 surface codes, with per-cycle logical errors of 0.0365(2) and 0.0282(1) after rejecting leakage events. Deterministic logical Bell state; logical Deutsch-Jozsa. Magic-state injection gives a logical RX(π/4) fidelity of 0.943, conditioned on no detected errors — [arXiv:2606.06598](https://arxiv.org/abs/2606.06598)
- 107-qubit superconducting processor (arXiv 1 Jul 2026) [IND academic, affiliations not verified]: merge/split, patch deformation, logical CNOT, Hadamard and S gates (a Clifford-generating set) on distance-3 patches, with neural-network decoding "without post-selection" — [arXiv:2607.01473](https://arxiv.org/abs/2607.01473)
- ETH Zurich-led (PMC, 30 Jan 2026) [IND academic]: lattice surgery between two distance-3 repetition codes, made by splitting one distance-3 surface code; decoded ZZ improved over an unencoded circuit — [PMC12904781](https://pmc.ncbi.nlm.nih.gov/articles/PMC12904781/)
- IBM hardware run by third parties:
  - Nighthawk r2 surface-code memory, Λ = 1.68 / 1.85 from distance 3 to 6; the distance advantage weakens over 150 rounds [IND/third party] — [arXiv:2610.23840](https://arxiv.org/abs/2610.23840)
  - "ibmphoenix" 120-qubit square lattice (arXiv 23 Oct 2026; University of Sydney-led, possible IBM co-author) [ACAD(+CO?)]: distance-3 and 5 surface codes with logical error per round below 1%. Lattice-surgery logical Bell fidelity above 93%; logical teleportation 78–93% — [arXiv:2610.32347](https://arxiv.org/abs/2610.32347)
  - 156-qubit heavy-hex dynamic compass code: lattice-surgery Bell fidelity >77% with pre-selection filtering, >97% with extra postselection — [arXiv:2610.11658](https://arxiv.org/abs/2610.11658)
- IBM real-time decoding: Relay-BP on FPGA in under 480 ns (company claim, Nov 2025) [CO] — [PostQuantum](https://postquantum.com/industry-news/ibm-loon-nighthawk/). IBM's gross qLDPC code [[144,12,12]] (Bravyi et al., *Nature* 627, 778 (2024); older, prior knowledge) [CO] — [DOI 10.1038/s41586-024-07107-7](https://doi.org/10.1038/s41586-024-07107-7)

**Trapped ions**
- Quantinuum color codes on Helios at distances 3, 5, 7 (arXiv 16 Oct 2026; not peer reviewed) [CO]: uses leakage reduction. Logical error as low as 5 (+4/−2)×10⁻⁶ with Λ = 12 (+3/−2). Encoded two-qubit Clifford randomized benchmarking reaches 7 (±3)×10⁻⁵ per logical two-qubit Clifford at distance 5 (Λ = 9, +8/−3). Neural-network decoders run "an order of magnitude faster than the syndrome extraction rate" — [arXiv:2610.24077](https://arxiv.org/abs/2610.24077). Trade press reports this as "99.9995% logical fidelity" and a factor-12 reduction per distance step — [The Quantum Insider, 19 Oct 2026](https://thequantuminsider.com/2026/10/19/quantinuum-reports-a-10x-reduction-in-logical-error-rate-on-helios/)
- Quantinuum [[20,2,6]] C₄-Helix code on Helios (arXiv 2 Sep 2026) [CO], all "without relying on postselection":
  - Repeated error correction: 4.6 (+6.2/−2.6)×10⁻⁵ error per logical qubit per cycle.
  - Full Clifford group on two logical qubits: 2.8 (+1.0/−1.6)×10⁻⁴ per two-qubit logical Clifford.
  - Fault-tolerant interface to a distance-5 surface code; three-logical-qubit GHZ state fidelity ≥ 99.925%.
  - Simulations suggest 10⁻⁶–10⁻⁸ logical error with better physical fidelity.
  - [arXiv:2609.03194](https://arxiv.org/abs/2609.03194)
- Quantinuum, 48–94 logical qubits "beyond break-even" (arXiv 25 Feb 2026) [CO]: iceberg error-detection code [[k+2,k,2]] and a two-level concatenated code [[(k₂+2)(k₁+2), k₂k₁, 4]], "with reasonable postselection rates" — [arXiv:2602.22211](https://arxiv.org/abs/2602.22211). Commentary: the counts rely on error-detecting codes with postselection, and the 48 error-corrected qubits use a distance-4 concatenated code [IND] — [PostQuantum](https://postquantum.com/quantum-research/quantinuum-94-logical-qubits/)
- Microsoft + Quantinuum (*Nature* 654, 349–355, 10 Jun 2026) [CO], per PubMed: logical error rates 11× to 800× better than physical baselines on a QCCD ion trap. Uses a 12-qubit code encoding 2 qubits (Knill-inspired) and a 16-qubit "tesseract" color code encoding 4, "combined with a scalable method of error detection and post-selection" — [DOI 10.1038/s41586-026-10628-y](https://doi.org/10.1038/s41586-026-10628-y)
- Sandia National Laboratories on Helios-1 (arXiv 9 Oct 2026) [IND national lab]: [[8,3,2]] and [[4,2,2]] error-detecting codes on ripple-carry adders. One-bit addition had an estimated logical failure rate of (6.0 ± 5.9)×10⁻⁵ after filtering burst errors, vs (3.5 ± 1.3)×10⁻³ unencoded. Two- and three-bit adders improved; four- and five-bit adders ran "just above threshold" — [arXiv:2610.14202](https://arxiv.org/abs/2610.14202)
- qLDPC "surgery" on Quantinuum H2-2 with a [[10,2,3]] generalised bicycle code (arXiv 28 Oct 2026) [affiliations not verified]: single-round logical X measurement error 0.72% (credible interval 0.32–1.41%), below 0.26% with three rounds; untouched (spectator) qubit error 0.21% — [arXiv:2610.39067](https://arxiv.org/abs/2610.39067)
- Innsbruck (PMC, 26 Jan 2026) [IND academic; senior author Monz co-founded AQT, to my knowledge]: measurement-free universal logical gate set; Grover search on 3 logical qubits encoded in 8 physical — [PMC12848042](https://pmc.ncbi.nlm.nih.gov/articles/PMC12848042/)

**Neutral atoms**
- Harvard/MIT/QuEra (*Nature* 649, 39–46 (2026); arXiv 25 Jun 2025) [ACAD+CO], with up to 448 atoms:
  - Surface codes: "2.14(13)× below-threshold performance in a four-round characterization circuit", using atom-loss detection and machine-learning decoding.
  - Logical entanglement via transversal gates and lattice surgery.
  - Transversal teleportation with 3D [[15,1,3]] codes for arbitrary-angle synthesis.
  - "Deep circuits with dozens of logical qubits and hundreds of logical teleportations" using [[7,1,3]] and [[16,6,4]] codes.
  - [arXiv:2506.20661](https://arxiv.org/abs/2506.20661)
- QuEra/Harvard/MIT, Apr 2026 [ACAD+CO, search summary]: about 2:1 physical-to-logical encoding with qLDPC codes, memory only. A Jan 2026 follow-up reportedly reached 96 logical qubits from 448 atoms (~5:1). These come from different architectures and should not be compared — [Quantum Computing Report](https://quantumcomputingreport.com/quera-harvard-and-mit-demonstrate-21-physical-to-logical-qubit-ratio/)
- Atom Computing toric code (arXiv 2 Jun 2026) [CO]: states that in neutral atoms "to date there has been no demonstration of repeated error correction scalable to arbitrary depth". Shows many cycles of syndrome extraction, replacing lost qubits mid-circuit and reloading a reservoir. Logical error characterized up to 90 cycles; the larger code has lower absolute logical error over up to 8 rounds — [arXiv:2606.04079](https://arxiv.org/abs/2606.04079)
- Earlier neutral-atom logical milestones (review) [IND]:
  - 48 logical qubits from 280 atoms (Harvard, 2023–24).
  - 24 entangled logical qubits on >1,200 physical, and 28 logical in a Bernstein-Vazirani run (Atom Computing/Microsoft, Nov 2024).
  - 8 and 12 logical qubits (Infleqtion, Sept 2025).
  - [arXiv:2608.05010](https://arxiv.org/abs/2608.05010)
- Metastable ¹⁷¹Yb erasure-biased logical qubits (arXiv 2506.13724, first posted Jun 2025, updated Jun 2026) [IND academic]: [[4,2,2]] encoding, erasure-informed decoding, and logical teleportation between code blocks — [arXiv:2506.13724](https://arxiv.org/abs/2506.13724)

**Decoders and qLDPC (theory and simulation)**
- Harvard convolutional-neural-network decoder (arXiv 9 Apr 2026) [ACAD+CO: Lukin is a QuEra co-founder, to my knowledge]: in simulation, logical error ~10⁻¹⁰ on the [144,12,12] gross code at 0.1% physical error, up to ~17× below existing decoders, with 3–5 orders of magnitude higher throughput — [arXiv:2604.08358](https://arxiv.org/abs/2604.08358)
- High-rate atom-array codes (simulation only):
  - [[2304,1156,≤14]] code: 1.3×10⁻¹³ per logical qubit per round at p = 0.1% (arXiv 2604.16209) [IND/ACAD+CO] — [arXiv:2604.16209](https://arxiv.org/abs/2604.16209)
  - [[2844,1426,18]] code, extrapolated: 2.6×10⁻¹⁶ (arXiv 3 Aug 2026) [IND academic] — [arXiv:2608.02773](https://arxiv.org/abs/2608.02773)

**What remains undemonstrated (as stated by sources)**
- Month-scale fault-tolerant operation: none; the longest runs last hours. The largest qLDPC code demonstrated is Bring's [[30,8,3]], while the Pinnacle design needs codes ~17× larger at higher distance. Real-time qLDPC decoding at distance 24 has not been shown [IND commentary] — [PostQuantum Pinnacle critique](https://postquantum.com/post-quantum/pinnacle-architecture-break-rsa-2048-critical/)
- IBM's 2026 "advantage" circuits used 468 T rotations applied as virtual frame updates, not magic-state logical T gates. The "70 logical qubits" are error-detected data qubits, not fault-tolerant logical qubits [IND commentary] — [PostQuantum fact-check](https://postquantum.com/industry-news/ibm-three-quantum-advantage-papers/)

### Inferences
- Reported Λ values are not like-for-like:
  - Google and USTC report Λ per distance step of 2 in symmetric surface codes.
  - The IBM third-party Λ covers distance 3 → 6 in one direction only.
  - Quantinuum's Λ = 12 is for color codes, and its 5×10⁻⁶ figure is per logical operation or cycle on a platform whose cycles are far slower than 1.1 µs.
  - Per-wall-clock-second comparisons across modalities cannot be made from the abstracts.
- Many trapped-ion and neutral-atom milestones with dozens of logical qubits rely on distance-2–4 codes and postselection or error detection. These are steps toward fault tolerance, not sustained fault-tolerant computation.
- No source found shows a complete algorithm combining real-time decoding, logical non-Clifford gates fed by a magic-state factory, and many rounds at logical error ≤10⁻⁶ on any modality.

### Gaps
- Not verified this session:
  - Google color-code result (*Nature* 2025; I recall Λ ≈ 1.56 from distance 3 to 5).
  - QuEra/Harvard logical magic-state distillation (*Nature*, Jul 2025; search summary only).
  - AWS Ocelot cat-qubit and Yale GKP results.
  - Riverlane real-time decoder papers.
  - Google lattice-surgery results on Willow, if any.
- The QuEra 2:1 (Apr 2026) and 96-logical-qubit (Jan 2026) results are known only from search summaries; primary preprints not read.
- No PsiQuantum, Xanadu or other photonic logical-qubit or error-correction demonstration was found.
- The Quantinuum color-code abstract does not say whether 5×10⁻⁶ is per QEC round or per logical operation; the full paper was not read.

## 3. Resource estimates for useful tasks (RSA/ECC, chemistry), and fast vs slow platforms

### Takeaway
Published estimates for breaking RSA-2048 have fallen from 20 million qubits / 8 hours (2019) to under 1 million qubits / under a week (Gidney, May 2025). With qLDPC codes or reconfigurable atoms they fall further, to ~72,000–100,000 qubits (Iceberg's Pinnacle, 2026) and ~10,000–26,000 atoms (Cain et al., Mar 2026; P-256 in "a few days"). Google estimates fewer than 500,000 qubits and minutes for 256-bit ECDLP (Mar 2026). All rest on undemonstrated assumptions: 10⁻³ physical error, 1 µs cycles, 10 µs reaction time, non-local connectivity, real-time decoding. At ~1 ms cycles, ions and atoms need 10–100× more qubits, or much longer runtimes, under the same code (Pinnacle: 2.7–13 million qubits for a one-month run). The best-known chemistry benchmark, FeMoco, is estimated at ~4 million qubits and under 4 days (2021).

### Cited Findings
- Gidney (Google), arXiv 21 May 2025 [CO]: RSA-2048 in under a week with fewer than 1 million noisy qubits.
  - Assumes a nearest-neighbour square grid, 0.1% uniform gate error, 1 µs surface-code cycle and 10 µs control reaction time.
  - 2019 baseline (Gidney & Ekerå): ~8 hours with 20 million qubits.
  - Gains come from approximate residue arithmetic, yoked surface codes and magic-state cultivation.
  - [arXiv:2505.15917](https://arxiv.org/abs/2505.15917)
- Iceberg Quantum, "Pinnacle Architecture" (arXiv 12 Feb 2026, v2 5 May 2026) [CO, third-party startup]: RSA-2048 with fewer than 100,000 physical qubits using qLDPC codes, at 10⁻³ error, 1 µs cycle and 10 µs reaction time — [arXiv:2602.11457](https://arxiv.org/abs/2602.11457)
- Pinnacle in detail (PostQuantum, 1 Mar 2026, updated 29 Oct 2026) [IND commentary]:
  - Runtime trade-off: ~97,000 qubits for ~1 year; ~98,000 for ~1 month; ~151,000 for ~1 week; ~471,000 for ~1 day.
  - "Pinnacle 1.2" (22 Oct 2026, no paper): ~72,000 qubits for 3.7 days.
  - Codes: generalized-bicycle [[254,14,16]] and [[510,16,24]], ~101 physical qubits per logical qubit.
  - Platform dependence (one-month run):

    | Platform (assumptions) | Feb 2026 | May 2026 |
    |---|---|---|
    | Superconducting (1 µs, 0.1%) | ~98,000 | ~94,000 |
    | Superconducting, fixed couplers | — | ~120,000 |
    | Trapped ions (1 ms, 0.01%) | 3.1 million | 2.7 million |
    | Neutral atoms (1 ms, 0.1%) | 13 million | 9.5 million |

  - Caveats: simulation only; not peer reviewed; no real-time decoder; the "one month" is an expected total across repeated attempts; ~75,000 of ~98,000 qubits are memory.
  - [PostQuantum](https://postquantum.com/post-quantum/pinnacle-architecture-break-rsa-2048-critical/)
- Expert reactions to Pinnacle (The Quantum Insider, 31 Mar 2026) [IND trade press]: Scott Aaronson distinguished what is shown "in simulation" from what "remains to be proven in hardware". Gidney said qLDPC reaction-time assumptions are "harder to meet than for surface codes" — [The Quantum Insider](https://thequantuminsider.com/2026/03/31/q-day-just-got-closer-three-papers-in-three-months-are-rewriting-the-quantum-threat-timeline/)
- Cain, Xu, King, Picard, Levine, Endres, Preskill, Huang, Bluvstein, "Shor's algorithm is possible with as few as 10,000 reconfigurable atomic qubits" (arXiv 30 Mar 2026; Caltech/Oratomic per trade press) [ACAD+CO]: P-256 discrete log in "a few days" with 26,000 physical qubits; RSA-2048 takes "one to two orders of magnitude longer". The authors note "substantial engineering challenges remain" — [arXiv:2603.28627](https://arxiv.org/abs/2603.28627). A secondary summary gives ~11,000–13,300 qubits for space-efficient designs and ~102,000 for a time-efficient design, with weeks to months of runtime (search summary).
- Xue & Covey (UIUC; arXiv 5 May 2026) [IND academic]: a ~500,000-qubit modular atomic processor with 10⁵ Bell pairs per second between modules and 1 ms measurement factors RSA-2048 in ~16% more time than a single module would — [arXiv:2605.03951](https://arxiv.org/abs/2605.03951)
- Google Quantum AI elliptic-curve whitepaper (31 Mar 2026; co-authors include Dan Boneh of Stanford and Justin Drake of the Ethereum Foundation) [CO with academic co-author, via IND trade press]:
  - Fewer than 500,000 physical qubits for 256-bit ECDLP.
  - ~70–90 million Toffoli gates, vs ~6.5 billion for RSA-2048.
  - Runtime in minutes: ~9 minutes after a public key is revealed, giving an estimated ~41% chance (idealized) of deriving a Bitcoin key before the transaction confirms.
  - Released with a zero-knowledge proof instead of the circuits.
  - [The Quantum Insider](https://thequantuminsider.com/2026/03/31/q-day-just-got-closer-three-papers-in-three-months-are-rewriting-the-quantum-threat-timeline/)
- Google's 25 Mar 2026 post set an internal migration target ("we want to be defended by 2029"), which the commentator calls a preparedness date, not a forecast of a cryptographically relevant machine [IND commentary on CO statement] — [PostQuantum](https://postquantum.com/security-pqc/ionq-q-day-claim-rsa-2048-earnings/)
- Chemistry, FeMoco (Lee et al., *PRX Quantum* 2, 030305 (2021), older) [ACAD+CO, Google with academics]: ~4 million physical qubits and under 4 days, assuming 1 µs cycles and ≤0.1% gate error (tensor hypercontraction plus qubitization) — [arXiv:2011.03494](https://arxiv.org/abs/2011.03494)
- Chemistry, cytochrome P450 (Goings et al., arXiv 2 Feb 2022; PNAS DOI 10.1073/pnas.2203533119, older) [ACAD+CO, Google/Boehringer Ingelheim/QSimulate]: concludes that P450 models large enough to balance dynamic and multiconfigurational correlation "could be a quantum advantage problem". No numbers retrieved from the abstract — [arXiv:2202.01244](https://arxiv.org/abs/2202.01244)
- Beverland et al., "Assessing requirements to scale to practical quantum advantage" (arXiv 14 Nov 2022, older) [ACAD+CO, Microsoft with ETH]: "hundreds of thousands to millions of physical qubits" are needed for practical advantage across three applications. Qubit size, speed and controllability are the critical parameters — [arXiv:2211.07629](https://arxiv.org/abs/2211.07629)
- Energy (Parker & Vermeer, arXiv 27 Apr 2023, older; RAND researchers per prior knowledge) [IND]: ~6 W per qubit, extrapolated from transmon systems, gives ~125 MW for a superconducting cryptographically relevant machine and ~$64,000 of electricity per broken key. Assumes a spacetime volume of 5.9×10⁶ qubit-days taken from older estimates — [arXiv:2304.14344](https://arxiv.org/abs/2304.14344)

### Inferences
- Platform speed sets the trade-off. Within one cost model (Pinnacle, Feb–May 2026), moving from 1 µs to 1 ms cycles at equal runtime raises qubit counts ~30× for ions (2.7–3.1M vs ~94–98k) and ~100–130× for atoms (9.5–13M). The atom-specific design of Cain et al. instead uses high-rate codes and reconfigurability to reach 10⁴ qubits at weeks-to-months runtime. Estimates for the same platform therefore differ by about 3 orders of magnitude depending on code family and assumptions (see contradiction below).
- RAND's 125 MW (2023) rests on a 5.9×10⁶ qubit-day spacetime volume from older estimates. Scaling it linearly to Gidney 2025's < 1M qubits at the same 6 W/qubit would give single-digit MW (my extrapolation, not a published figure).
- Every 2025–2026 estimate assumes about 10⁻³ physical error across 10⁴–10⁶ qubits, plus real-time decoding and reaction times of about 10 µs. None of these has been shown at scale (Section 2).

### Gaps
- Contradiction, not resolved: neutral-atom RSA-2048 estimates span ~10⁴ (Cain et al.) to ~5×10⁵ (Xue & Covey) to 9.5–13 million (Pinnacle's neutral-atom table). They use different codes, connectivity, runtimes and per-operation times, and I could not read the full papers to reconcile them.
- Beverland et al.'s per-platform runtimes (ns vs µs operation times) and Goings et al.'s P450 qubit counts and runtimes were not extracted (abstract pages only).
- No 2025–2026 independent chemistry resource estimates (e.g., updated FeMoco/P450 figures) were retrieved.
- No published trapped-ion-specific RSA estimate beyond Pinnacle's ion table was found. Pinnacle 1.2 (Oct 2026) has no paper.
- I could not verify the exact title or author list of the Google ECDLP whitepaper.

## 4. Quantum advantage claims and classical rebuttals; how "verifiable" and "useful" advantage are judged; any independent evidence of commercial advantage

### Takeaway
Independent researchers broadly accept that random-circuit-sampling (RCS) results after 2019 (Google 2024, USTC 2024–25, Quantinuum 2024) have not been classically reproduced, though they are judged "nearly useless". Physics-simulation and "utility" claims keep being matched or undercut by classical methods within about 18 months:
- IBM 2023, matched by Flatiron and Caltech.
- D-Wave 2025, matched by Flatiron, published in *Science* 2026.
- Quantinuum H2 / BlueQubit-style peaked circuits, simulated on one GPU in ~1 hour in Apr 2026.

IBM's three July 2026 claims are unrefereed preprints still being challenged; one was reportedly reproduced in 37.3 minutes on 256 GPUs. Google's Quantum Echoes (Oct 2025) has not been reproduced; the main rebuttal-of-rebuttals appears to be Google-co-authored. I found no independent evidence of commercially useful quantum advantage as of 14 Nov 2026.

### Cited Findings

**Google RCS (2019 onward)**
- Google 2019 (Arute et al., *Nature* 574, 505; older, prior knowledge) [CO]: 53 qubits, linear cross-entropy benchmark (XEB) of ~0.002; claimed 10,000 years classically. IBM proposed ~2.5 days on the Summit supercomputer — [DOI 10.1038/s41586-019-1666-5](https://doi.org/10.1038/s41586-019-1666-5); [PostQuantum summary](https://postquantum.com/industry-news/ibm-three-quantum-advantage-papers/)
- Pan, Chen & Zhang (Chinese Academy of Sciences), *PRL* 129, 090502 (2022, older) [IND]: one million samples of the 53-qubit, 20-cycle Sycamore circuits at fidelity ~0.0037 in ~15 h on 512 GPUs; projected tens of seconds on an exaflop machine — [arXiv:2111.03011](https://arxiv.org/abs/2111.03011)
- Willow RCS (9 Dec 2024) [CO]: 103 qubits, depth 40, XEB 0.1%; "5 minutes vs 10^25 years" (company estimate) — [Willow spec sheet](https://quantumai.google/static/site-assets/downloads/willow-spec-sheet.pdf)

**USTC RCS**
- Zuchongzhi 3.0 (arXiv 16 Dec 2024) [IND competitor academic]: 83-qubit, 32-cycle RCS producing 1 million samples in "a few hundred seconds"; estimates ~6.4×10⁹ years on the Frontier supercomputer, six orders of magnitude beyond Google's SYC-67/70 (*Nature* 634, 328 (2024)) — [arXiv:2412.11924](https://arxiv.org/abs/2412.11924)

**Expert judgement on RCS**
- Hangleiter (Quantum Frontiers blog, 6 Jan 2026) [IND academic]:
  - Proposes three criteria: a pre-specified programmable task, a scaling separation, and no classical machine can currently do it.
  - Only the 2019 experiment "may actually have been simulated". Later Google (70 qubits), USTC (83 qubits) and Quantinuum (56 qubits) RCS stand; even 56-qubit runs may not be feasibly simulated.
  - The claims rest on "a proxy of a proxy of the quantum fidelity".
  - Fewer than half of an expert audience he polled thought advantage had been achieved.
  - [Quantum Frontiers](https://quantumfrontiers.com/2026/01/06/has-quantum-advantage-been-achieved/). Trade press summary — [The Quantum Insider, 12 Jan 2026](https://thequantuminsider.com/2026/01/12/quantum-advantage-has-likely-been-achieved-the-debate-is-over-what-counts/)

**IBM 2023 "utility" (*Nature* 618, 500 (2023); older)** [CO]: 127-qubit Eagle, kicked Ising model, zero-noise extrapolation (ZNE) error mitigation. Rebuttals:
- Tindall, Fishman, Stoudenmire, Sels (Flatiron/NYU; *PRX Quantum* 5, 010308 (2024)) [IND]: tensor network with belief propagation is "significantly more accurate and precise" than the processor — [arXiv:2306.14887](https://arxiv.org/abs/2306.14887)
- Begušić & Chan (Caltech; arXiv 28 Jun 2023) [IND]: sparse Pauli dynamics on a single laptop core, "orders of magnitude faster" than the quantum walltime and in good agreement with the ZNE results — [arXiv:2306.16372](https://arxiv.org/abs/2306.16372)
- Kechedzhi et al. (Google; *Future Gener. Comput. Syst.* 153, 431–441 (2024)) [CO, a competitor]: reproduces a Floquet-circuit experiment "in less than one second per data point using one GPU". The abstract does not name IBM — [arXiv:2306.15970](https://arxiv.org/abs/2306.15970)

**IBM 2026 claims (three preprints posted 27–28 Jul 2026; IBM announcement 30 Jul 2026)** [CO / ACAD+CO / third-party companies]. Jay Gambetta: "We are now firmly in the quantum advantage era." Details from the PostQuantum fact-check (1 Aug 2026) [IND commentary]:
- **IBM / University of Chicago (Fefferman), doped Clifford sampling, Heron** [ACAD+CO]:
  - 97 physical qubits (70 data + 27 syndrome); 2,869 CZ gates; 468 T rotations applied as virtual frame updates.
  - ~3.5 million raw shots kept at a 0.059% acceptance rate gave 2,051 accepted samples in 16.1 min of quantum-processor time.
  - Certified fidelity lower bound 0.284, holding only under the stated noise assumptions. No classical runtime given.
  - [arXiv:2607.25941](https://arxiv.org/abs/2607.25941)
- **Qedma (with RIKEN, BlueQubit), Floquet Ising model, Heron r3, up to 74 qubits** [CO, third-party companies]:
  - At 51 qubits, sparse Pauli-path runs on 12,888 Fugaku nodes (~10¹² Pauli strings) diverged after ~7 cycles. At 74 qubits no classical method reproduced late-time results.
  - Late-time 74-qubit results rely on a heuristic extrapolation that may bias them. Selected 51-qubit points were cross-checked on Quantinuum H2 and Helios.
  - [arXiv:2607.24937](https://arxiv.org/abs/2607.24937)
- **Algorithmiq, operator Loschmidt echo, 56 qubits** [CO, third-party company]: mitigated results agreed within 0.03 across five variants. Classical methods disagreed with each other and with the quantum data — [arXiv:2607.25998](https://arxiv.org/abs/2607.25998)
- Fact-check caveats: none is peer reviewed. IBM's community quantum-advantage tracker (launched Nov 2025 with Algorithmiq, the Flatiron Institute and BlueQubit) lists them as "active candidates", not adjudicated. "No paper demonstrates an end-to-end production workload or a commercially useful speedup." Hangleiter said the Qedma and Algorithmiq results "seem hard to simulate classically"; Eisert called advantage "an ongoing confidence-building process" — [PostQuantum fact-check](https://postquantum.com/industry-news/ibm-three-quantum-advantage-papers/)
- Challenges:
  - Oh (arXiv Jul 2026) [IND]: a "frozen-tree" algorithm reproduces ensemble-level statistics, questioning whether sample-only statistics can certify RCS-type claims. It does not directly address doped-Clifford sampling — [arXiv:2607.04054](https://arxiv.org/abs/2607.04054)
  - A preprint reportedly reproduced all 2,051 amplitude batches of the IBM–UChicago experiment in 37.3 minutes on 256 NVIDIA H100 GPUs [IND, search summary; page returned 403, preprint not identified] — [Technology.org, 7 Sep 2026](https://www.technology.org/2026/09/07/ibm-quantum-advantage-verified-classical-response/)
  - Earlier BlueQubit peaked-circuit speedups were later overtaken by classical methods (search summary).

**Peaked circuits on Quantinuum H2** — Gharibyan et al. (arXiv:2510.25838) claimed heuristic advantage on the 56-qubit H2 [CO]. Kremer & Dupuis (arXiv 23 Apr 2026; affiliations not listed) [IND of the claimants] fully contract the largest circuit and extract its peak in ~1 hour on a single GPU, about half the original hardware runtime — [arXiv:2604.21908](https://arxiv.org/abs/2604.21908)

**Quantinuum Helios RCS** — the authors present RCS results as "beyond the reach of classical simulation" (company claim; no independent check found) [CO] — [arXiv:2511.05465](https://arxiv.org/abs/2511.05465)

**Google Quantum Echoes (*Nature*, 22–23 Oct 2025)** [CO]
- Scientific American (23 Oct 2025) [IND press]: OTOC (out-of-time-order correlator) experiment on the 105-qubit Willow. Google estimates ~3 years classically vs ~2 hours on Willow. Peer reviewers "split" on whether advantage was shown. A separate molecule-geometry preprint is not peer reviewed and "not faster than classical methods". Shenglong Xu (Texas A&M): the result "seems like it is beyond what we can do right now using classical methods" — [Scientific American](https://www.scientificamerican.com/article/google-measures-quantum-echoes-on-willow-quantum-computer-chip/)
- Other reported figures (search summaries) [CO / IND commentary]: ~13,000× faster than the best known classical simulation. For 65 qubits, ~3.2 years on Frontier vs 2.1 hours on the chip. The headline is measured against a specific tensor-network contraction method — [PostQuantum](https://postquantum.com/quantum-research/googles-quantum-advantage/); [Kshetrimayum, Jahromi, Singh, Orús, "Quantum Advantage: a Tensor Network Perspective", arXiv Mar 2026](https://arxiv.org/abs/2603.18825)
- Bermejo, Villalonga, Ware, Vidal, Szasz (arXiv 16 Apr 2026): tensor networks with belief propagation "cannot feasibly simulate" Quantum Echoes, and OTOC circuits are largely incompressible. Arguments for the 65- and 95-qubit runs are scaling-based, not direct simulations. Affiliations are not listed on arXiv; to my knowledge Villalonga, Vidal and Szasz are Google Quantum AI researchers, so this should not be treated as independent [likely CO] — [arXiv:2604.15427](https://arxiv.org/abs/2604.15427)

**D-Wave 2025 annealing claim (King et al., *Science* 388, 199 (2025); prior knowledge)** [CO]: claimed "beyond the reach of classical computation".
- Tindall, Mello, Fishman, Stoudenmire, Sels, *Science* 392, 868–872 (2026) [IND]: 2D and 3D tensor networks with belief propagation reproduce the dynamics for "hundreds of qubits" with "modest computational resources" — [arXiv:2503.05693](https://arxiv.org/abs/2503.05693); [DOI 10.1126/science.adx2728](https://doi.org/10.1126/science.adx2728)
- Mauron & Carleo (EPFL, arXiv 11 Mar 2025) [IND]: time-dependent variational Monte Carlo on up to 128 spins (3D diamond lattice), correlation errors below 7% — [arXiv:2503.08247](https://arxiv.org/abs/2503.08247)

**Meta-analyses and definitions**
- Hagar, "The NISQ Trap" (arXiv 8 Jul 2026, v3 14 Jul 2026) [IND]: with one exception, every NISQ flagship advantage demonstration was classically reproduced, shown to have tractable structure, or closed by a simulability theorem within ~18 months. Counts more than 30 advantage-class announcements; argues the exit is fault tolerance — [arXiv:2607.07530](https://arxiv.org/abs/2607.07530)
- Huang, Choi, McClean, Preskill, "The vast world of quantum advantage" (arXiv 7 Aug 2025) [ACAD+CO; McClean is at Google]: defines five properties of an ideal advantage — predictability, typicality, robustness, verifiability, usefulness. Proves some advantages cannot be predicted classically. The "Huang et al., PRX 16, 030501 (2026)" cited in Hagar v3 may be its published version (unverified) — [arXiv:2508.05720](https://arxiv.org/abs/2508.05720)
- Trade press summary of the field (Jan 2026) [IND]: Preskill's 2012 definition required no usefulness. Proposed newer criteria are programmable, scalable, verifiable, robust to classical attack, and ideally economically relevant. Practical advantage is "a separate, higher bar that is still ahead" — [The Quantum Insider](https://thequantuminsider.com/2026/01/12/quantum-advantage-has-likely-been-achieved-the-debate-is-over-what-counts/)
- US National Quantum Initiative joint algorithms workshop report (arXiv 2508.13973) [IND government/academic, search summary]: establishing advantage is "inherently adversarial"; classical and quantum realisations should be done by different groups — [arXiv:2508.13973](https://arxiv.org/abs/2508.13973)

**IonQ** — no independent verdict on an IonQ-specific advantage claim in 2026 was found. IonQ itself states that broad advantage requires error-correcting codes (search summary) — [ThesisCheck](https://thesischeck.io/teardown/ionq-quantum-advantage-premium-2026-07)

### Inferences
- The field's own adjudication process is now explicit but slow and partly company-run: IBM's tracker, preprint-versus-preprint exchanges, and DARPA's separate engineering verification. Claims based on error-mitigated expectation values (IBM 2023, IBM/Qedma/Algorithmiq 2026) remain the most exposed to classical tensor-network and Pauli-path methods. RCS-style claims are harder to refute but also hard to verify, because the fidelity proxy (XEB) can only be checked by extrapolating from smaller circuits.
- Hagar's "~18 months" pattern holds for IBM 2023 → 2023/24, D-Wave Mar 2025 → Mar 2025 preprints and a 2026 *Science* paper, and H2 peaked circuits Oct 2025 → Apr 2026. The IBM 2026 claims are still inside that window.
- On these sources, the "verifiable and useful" bar (Huang et al.; trade press criteria) has not been met independently by any company as of 14 Nov 2026.

### Gaps
- Quantinuum/JPMorgan certified randomness (*Nature*, Mar 2025): I recall a 56-qubit H2, ~71,313 certified bits, ~1.1 exaflop/s of classical verification, and security that rests on assumptions about an adversary's classical computing power. None of this was verified this session, and no independent critique was retrieved.
- Quantinuum H2 56-qubit RCS (2024; DeCross et al.) figures and Helios RCS numbers were not retrieved.
- The C&EN article "IBM claims its quantum computers outperform classical ones" (Aug 2026) returned HTTP 406. The 37.3-minute rebuttal preprint was not identified.
- Contradiction: Hangleiter is described as at ETH Zurich (PostQuantum) and at the Simons Institute, UC Berkeley (The Quantum Insider).
- IBM–UChicago described as "70 logical qubits" (some press) vs "70 error-detected data qubits + 27 ancillas" (fact-check).
- QuEra claims of advantage in 2025–2026: none found (the search did not reach this).
- Google's March 2026 NMR/molecular follow-up: peer-review status after Oct 2025 unknown.
- No independent study of commercially useful advantage (finance, chemistry or optimization in production) was found. "No evidence found" is the finding, subject to the search-budget limit.

## 5. Supply-chain and infrastructure limits (cryogenics, helium-3, lasers/optics, materials, detectors, foundries, power, footprint)

### Takeaway
Cryogenics is the clearest bottleneck for superconducting qubits, and for photonics at ~2–4 K because of its superconducting detectors. Global helium-3 output is roughly 22,000–30,000 L/yr, priced at about $2,500–3,000/L, and each dilution refrigerator needs 10–100 L. The dilution-refrigerator market is concentrated in a few suppliers with 6–9 month lead times. Ion and atom systems depend on lasers and optics whose rare-earth and lithium-niobate supply is concentrated in China and Japan. Energy and footprint estimates for fault-tolerant machines are sparse: about 125 MW for an older-generation superconducting code-breaking design (RAND, 2023), a "building-sized" photonic facility, and <7 kW for one neutral-atom cabinet.

### Cited Findings
- Narang (UCLA, DCVC) & Levine, War on the Rocks, 20 Oct 2025 [IND, though one author is a VC partner]:
  - **Dilution refrigerators:** market "dominated by three suppliers". Vendors: Bluefors (Finland, plus US manufacturing in Syracuse), Oxford Instruments (UK), Janis (US), Maybell (emerging). Bluefors has shipped >1,500 dilution refrigerators and 15,000 cryocoolers; Syracuse expanded in 2024 to 20 systems/yr plus 50 assembly bays in Europe; lead times 6–9 months; ~1 system/day; 18 systems delivered to Japan's AIST in 6 weeks (2024).
  - **Cryo components:** pulse-tube coolers from Cryomech, SunPower, Sumitomo and others. Ion pumps and photodetectors are flagged as single points of failure.
  - **Rare earths:** China holds 69% of reserves and ~90% of processing; China's export controls apply at 0.1% Chinese-origin content. Erbium and ytterbium are needed for photonics, neodymium for 1064 nm lasers, rubidium and strontium for atom systems.
  - **Lithium niobate:** wafers from Sumitomo Metal Mining (Japan) and CASTECH (China); China has ~60–70% of high-quality boule production; no US supplier at scale; $100–300M estimated for meaningful US capacity.
  - **Foundries:** no dedicated quantum 300 mm line.
  - **Not covered by the article:** coax cables, HEMT and TWPA amplifiers, superconducting nanowire detectors.
  - [War on the Rocks](https://warontherocks.com/cogs-of-war/the-supply-chain-chokepoints-in-quantum/)
- MP-IDSA issue brief, 21 May 2026 [IND, Indian government-funded think tank]:
  - **Helium-3:** supply dominated by the US, Russia and Canada, from tritium decay, "capped at 22,000–30,000 litres per year"; price $2,500–3,000/L with 6–12 month lead times; 10–100 L per dilution refrigerator; He-3 can be up to a quarter of a fridge's cost, which can exceed $600,000. Bluefors–Interlune: 10,000 L/yr from 2028 for a decade. The US DOE bought 3 L.
  - **Helium-4:** Qatar supplies ~1/3 of world helium. Iranian drone strikes shut a Qatari LNG/helium facility in Mar 2026, and Qatar's output is expected to fall 14% over five years. The last of the US National Helium Reserve was sold in 2024.
  - [MP-IDSA](https://idsa.in/publisher/issuebrief/a-helium-shock-to-indias-quantum-technology-ambitions)
- Interlune (The Quantum Insider, 20 Jul 2026) [CO claims via IND trade press]: "Cold Capture" yields 99% pure He-3 from Grade A helium. Potential of up to 2.5 kg/yr from US helium plants, which would roughly triple current US domestic production (company projection). Nearly $500M of binding purchase agreements, mainly with Maybell and Bluefors — [The Quantum Insider](https://thequantuminsider.com/2026/07/20/interlune-produces-pure-helium-3-from-domestic-helium-using-novel-cryogenic-technology/). A separate source puts the Bluefors contract at >$300M for up to 10,000 L/yr from 2028 to 2037 (search summary) — [Quantum Academy](https://quantumacademy.com/quantum-engineering/helium-3/)
- He-3 price contradiction: "as much as $20,000 per liter" (finance site, search summary) — [BigGo Finance](https://finance.biggo.com/news/d24D0J0BX0tZvRTvNT_v) — vs $2,500–3,000/L (MP-IDSA, above). Science magazine also reports He-3 is "running scarce" (page returned 403; not read) — [Science](https://www.science.org/content/article/helium-3-runs-scarce-researchers-seek-new-ways-chill-quantum-computers)
- Photonic infrastructure (PsiQuantum) [CO statements via IND]:
  - 2025: GlobalFoundries 300 mm fab; cryostat at 2 K with up to 20 W cooling — [PostQuantum](https://postquantum.com/quantum-research/psiquantum-photonic-platform-nature/)
  - 2026: three cryostats plus a 2×180 W, 2.3 K cryoplant in California; Chicago building constructed with major cooling equipment on site; Australia site slipped from its 2025 target, work since Jul 2026.
  - The writer concludes the utility-scale design needs "a building-sized facility and a large refrigeration plant" — [Cisco write-up](https://netcreat.substack.com/p/cisco-quantum-summit-2026-day-2-psiquantum)
- IBM fabrication [CO]: 300 mm wafers at Albany NanoTech; build time per processor cut at least in half — [PostQuantum](https://postquantum.com/industry-news/ibm-loon-nighthawk/)
- Power estimates:
  - Superconducting code-breaking machine ~125 MW at ~6 W/qubit (RAND authors, 2023, older) [IND] — [arXiv:2304.14344](https://arxiv.org/abs/2304.14344)
  - Hanyuan 2 neutral-atom cabinet below 7 kW [IND review reporting system specs] — [arXiv:2608.05010](https://arxiv.org/abs/2608.05010)
- Isotopes: Helios uses ¹³⁷Ba⁺ [CO] — [arXiv:2511.05465](https://arxiv.org/abs/2511.05465). ¹⁷¹Yb is used in metastable-qubit neutral-atom work [IND] — [arXiv:2506.13724](https://arxiv.org/abs/2506.13724). Silicon-28 enrichment is flagged as a specialized process for spin qubits [IND] — [War on the Rocks](https://warontherocks.com/cogs-of-war/the-supply-chain-chokepoints-in-quantum/)

### Inferences
- At 10–100 L per refrigerator, global He-3 output of 22,000–30,000 L/yr could supply only ~220–3,000 new dilution refrigerators a year, even if all of it went to fridges. Bluefors alone ships about one system a day (~365/yr). The Bluefors–Interlune contract (10,000 L/yr) would equal about a third to a half of today's stated global output, if delivered. All of this is my arithmetic on the cited figures.
- Interlune's projected 2.5 kg/yr would be ~18,700 L at standard temperature and pressure (He-3 density ≈ 0.134 g/L — standard physical constant, my conversion). If that triples US output, current US output is about 6,000 L/yr, consistent with the 22,000–30,000 L/yr multi-country range.
- A fault-tolerant superconducting machine of ~10⁵–10⁶ qubits would, per MP-IDSA, need "dozens or hundreds" of interconnected refrigerators. That makes He-3 supply, fridge lead times, and dense cryogenic wiring (not quantified in sources found) first-order constraints. Photonic machines avoid millikelvin cooling but need multi-hundred-watt 2–4 K plants.

### Gaps
- Not found:
  - Dilution-refrigerator cooling power at the mixing chamber.
  - Wiring heat-load per qubit and the status of cryo-CMOS or cryogenic multiplexing (IBM, Google, Intel and others).
  - Superconducting nanowire detector vendors and capacity.
  - Laser system counts and costs per ion or atom machine.
  - Enrichment supply for ¹³⁷Ba, ¹⁷¹Yb and ⁸⁷Sr.
  - Foundry access terms (GlobalFoundries/PsiQuantum, IQM's own fab).
- Recalled but unverified: Oxford Instruments' 2025 sale of its NanoScience (dilution refrigerator) business to Quantum Design.
- No independent 2025–2026 power or footprint estimates for fault-tolerant ion, atom or photonic machines. The RAND figure predates the 2025 qubit-count reductions.

## 6. Does each approach stand on solid scientific ground, and why?

### Takeaway
All four modalities rest on established physics. None of the sources found claims a fundamental physical barrier; the open questions are engineering, scale and speed:
- **Superconducting:** has shown error correction that improves with code size at µs cycles. Must contain correlated errors, leakage and fabrication spread, and scale cryogenics and wiring 100–1,000×.
- **Trapped ions:** have the best fidelities and strongest small-code results. Must overcome slow (ms-scale) operations and scaling of the QCCD architecture.
- **Neutral atoms:** have scale and reconfigurability. Need two-qubit fidelity above 99.9%, faster cycles, and long-duration loss management.
- **Photonics:** has a manufacturing base and high conditional fidelities. Has not yet shown the loss budget or any error-corrected logical qubit, which is the central unproven element.

### Cited Findings
- **Superconducting — demonstrated:**
  - Exponential suppression with distance and beyond-break-even memory at 1.1 µs cycles (Google, *Nature* 2025) [CO] — [arXiv:2408.13687](https://arxiv.org/abs/2408.13687)
  - Reproduced by an independent competitor (USTC Λ = 1.40, Dec 2025) [IND] — [Quantum Computing Report](https://quantumcomputingreport.com/ustcs-zuchongzhi-3-2-achieves-below-threshold-qec-milestone/)
  - Reproduced by third parties on IBM cloud hardware (Λ ≈ 1.7–1.9, Oct 2026) [IND] — [arXiv:2610.23840](https://arxiv.org/abs/2610.23840)
- **Superconducting — limits:**
  - Correlated error bursts about once an hour set a floor (Google) [CO] — [arXiv:2408.13687](https://arxiv.org/abs/2408.13687)
  - Leakage required dedicated suppression (USTC, 72× reduction) [IND] — [PostQuantum](https://postquantum.com/quantum-research/zuchongzhi-3-2-belowthreshold/)
  - Distance advantage weakens over 150 rounds with long-lived correlations (IBM Nighthawk r2, third party) [IND] — [arXiv:2610.23840](https://arxiv.org/abs/2610.23840)
  - Fabrication heterogeneity forces component exclusion [IND/ACAD] — [arXiv:2610.11658](https://arxiv.org/abs/2610.11658)
  - 100–1,000× qubit-scale gap [IND commentary] — [PostQuantum](https://postquantum.com/post-quantum/pinnacle-architecture-break-rsa-2048-critical/)
  - He-3 and dilution-refrigerator supply (Section 5).
- **Trapped ions — demonstrated:**
  - Physical two-qubit infidelity 7.9×10⁻⁴ at 98 qubits with all-to-all connectivity [CO] — [arXiv:2511.05465](https://arxiv.org/abs/2511.05465)
  - Color-code Λ = 12 at distances 3–7 [CO, preprint] — [arXiv:2610.24077](https://arxiv.org/abs/2610.24077)
  - Independent national-lab use showing encoded arithmetic beating unencoded runs [IND] — [arXiv:2610.14202](https://arxiv.org/abs/2610.14202)
- **Trapped ions — limits:**
  - At assumed 1 ms cycles, RSA-scale tasks need ~2.7–3.1M qubits for a one-month run [IND commentary on CO estimate] — [PostQuantum](https://postquantum.com/post-quantum/pinnacle-architecture-break-rsa-2048-critical/)
  - Many logical-qubit headlines use error detection and postselection [IND commentary] — [PostQuantum](https://postquantum.com/quantum-research/quantinuum-94-logical-qubits/)
  - Not in DARPA Stage C as of Oct 2026: Quantinuum (IonQ is in) [IND] — [DCD](https://www.datacenterdynamics.com/en/news/darpa-announces-four-companies-advancing-to-final-stage-of-its-quantum-benchmarking-initiative/)
- **Neutral atoms — demonstrated:**
  - Up to 448-atom fault-tolerance architecture elements at 2.14× below threshold [ACAD+CO] — [arXiv:2506.20661](https://arxiv.org/abs/2506.20661)
  - 6,100-atom coherent arrays and >3,000-atom continuous operation [IND review] — [arXiv:2608.05010](https://arxiv.org/abs/2608.05010)
  - 90-cycle toric-code operation with reloading [CO] — [arXiv:2606.04079](https://arxiv.org/abs/2606.04079)
- **Neutral atoms — limits (review [IND]):**
  - Two-qubit fidelity below 99.9%, with an error budget of Rydberg decay, laser phase noise and thermal motion.
  - Tweezer lifetimes of ~60 s.
  - No measured QEC cycle time.
  - Overhead of 100–200 physical qubits per logical qubit at 99% fidelity.
  - [arXiv:2608.05010](https://arxiv.org/abs/2608.05010)
  - Ms-scale cycles drive 9.5–13M-qubit estimates under surface-code-like qLDPC assumptions (Pinnacle), versus ~10⁴ under atom-specific high-rate designs [ACAD+CO] — [arXiv:2603.28627](https://arxiv.org/abs/2603.28627)
- **Photonics — demonstrated:** fidelities of 99.22–99.98% from a commercial 300 mm foundry, all conditional on detection [CO] — [arXiv:2404.17570](https://arxiv.org/abs/2404.17570)
- **Photonics — limits:**
  - Thresholds require low per-photon loss (2.7% per photon in the original FBQC model) [CO study via IND] — [The Quantum Insider](https://thequantuminsider.com/2025/06/17/psiquantum-study-maps-path-to-loss-tolerant-photonic-quantum-computing/)
  - The system is "not yet within budget" [IND commentary] — [PostQuantum](https://postquantum.com/quantum-research/psiquantum-photonic-platform-nature/)
  - Some components still below spec; no error-correction break-even (Oct 2026) [CO / IND critique] — [Cisco write-up](https://netcreat.substack.com/p/cisco-quantum-summit-2026-day-2-psiquantum)
  - Nonetheless in DARPA Stage C via US2QC [IND] — [Quantum Computing Report](https://quantumcomputingreport.com/darpa-selects-atom-computing-diraq-ibm-and-ionq-for-final-stage-c-verification-under-quantum-benchmarking-initiative/)
- **Cross-cutting:**
  - Eisert & Preskill: the gaps from error mitigation to scalable fault tolerance and to verifiable algorithms remain open [IND] — [arXiv:2510.19928](https://arxiv.org/abs/2510.19928)
  - GAO: a cryptographically relevant machine possibly "as soon as the 2030s", with expert estimates varying widely [IND] — [ExecutiveGov](https://www.executivegov.com/articles/gao-federal-agencies-quantum-cryptography-readiness)

### Inferences
- The evidence base is uneven across modalities:
  - Superconducting below-threshold behaviour is the only one replicated by groups independent of the leading company (USTC; third parties on IBM).
  - Trapped-ion error correction is the most precise but is almost entirely company-run, apart from Sandia as a user.
  - Neutral-atom error correction is academic-plus-company (Harvard/QuEra; Atom Computing).
  - Photonic fault-tolerance elements are entirely company-reported and have no logical-level result.
- The four modalities' binding constraints differ in kind: superconducting is limited by wiring, cryogenics and correlated noise; ions by clock speed and trap scaling; atoms by gate fidelity, clock speed and loss; photonics by optical loss and switching/multiplexing. Comparing them by qubit count alone is therefore misleading. Resource estimates (Section 3) show speed and connectivity can matter as much as count.

### Gaps
- No formal independent peer-reviewed comparative assessment across modalities dated 2025–2026 was found; DARPA QBI Stage C results are not public yet.
- No independent measurements (outside company papers) were found for IonQ, IQM, QuEra hardware or PsiQuantum hardware.
- The search budget was exhausted before targeted searches on IQM, IonQ primary data, IBM Heron r3 metrics, certified-randomness critiques, recent government reports (NASEM/DOE/NIST/NQCC/RAND), and cryo-CMOS/wiring. Absence of evidence on these points reflects that limit, not a confirmed absence.
