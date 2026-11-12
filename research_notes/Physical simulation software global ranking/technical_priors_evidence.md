# Technical evidence on how AI is changing physical simulation software (as of 12 Nov 2026)

STATUS: v1 (draft saved after mining the salvage digest; being extended). All sources accessed 12 Nov 2026 unless stated.

## Summary for the report writer

(v1 placeholder — to be rewritten at the end.)
- Cited items: most exist and say roughly what was cited, but several need correcting. 2608.13122 (CReSS): 162 *kernels* (OpenMP regions executed in one typhoon scenario) validated element-wise against a single dumped snapshot at tolerance 1e-5; 5.1x is per-timestep on one GH200 superchip (H100 vs its own 72-core Grace CPU); authors call it "a scenario-specific validated GPU port, not a complete GPU port". 2608.04400: the >7-orders figure is the *median* residual ratio; the *mean* fell only ~3 orders and stayed above the solver's 1e-8 convergence threshold; 15.5x is per optimisation generation with an extra GPU and at most 6 Newton updates. 2605.08988: "often an order of magnitude", up to ~1000x for energies, on deliberately compositional splits of small H/C/N/O molecules. 2604.18491: the stricter CFD-replacement threshold was met for 18 of 20 car parts, so "not met" is too strong. Siemens/NVIDIA 10-17x: company claim, no baseline, no customer. Kimi K3 chip: Moonshot's own blog (company claim), 45 nm, simulated only. FugakuNEXT: RIKEN says ">600 EFLOPS FP8 (sparse)"; "zettascale" is only reached in sparse FP4 by a journalist's inference.

## Q1. Verification of the cited evidence

### Takeaway
(see Cited Findings; to be completed)

### Cited Findings

**(a) arXiv 2608.13122 (weather-code port)**
- Title "Validation-Centric AI-Assisted GPU Porting of a 250,000+ Line Legacy Weather Simulation Code"; authors Tetsuya Hoshino, Masaya Kato, Kazuhisa Tsuboki, Daichi Mukunoki, Takahiro Katagiri, Toshihiro Hanawa; v1 13 Aug 2026; "Submitted to AgenticAI4HPC 2026" (preprint, not peer-reviewed); cs.DC. — [arXiv abs](https://arxiv.org/abs/2608.13122)
- Code: CReSS (Cloud Resolving Storm Simulator), Fortran 90, MPI/OpenMP, 599 files, ~260,000 lines, 387 OpenMP regions, development since 1998. Agent: "Claude Code Opus 4.5–4.6" (Opus 4.6 fixed for controlled experiments). Target: OpenACC, nvfortran (NVIDIA HPC SDK 25.9), unified memory. — [arXiv HTML](https://arxiv.org/html/2608.13122)
- Validation: dump-based kernel benchmarks from the state at each kernel's last call in a 360-step run; element-wise relative error ≤1e-5 (single precision, not bitwise); application check on max/min pressure perturbation <1e-4 (achieved 1.0e-5 and 5.6e-5). 162 of the 387 OpenMP regions executed in the typhoon scenario were ported; five kernels had single-element discrepancies (ulp-level threshold flips, exp/log/sqrt differences, a zero reference) accepted by developers. — [arXiv HTML](https://arxiv.org/html/2608.13122)
- Speed: 5.1x = median time per timestep, 9.51 s on the 72-thread Grace CPU vs 1.88 s on the H100 of the same GH200 superchip (one Miyabi-G node, JCAHPC); typhoon case Sept 2022, 899×899×128 grid, ~2 km, 30 simulated minutes. Effort ~100 GPU-node hours over ~3 months. Limitations: snapshot validation "does not certify all control paths"; dumps >400 GB; one scenario, one node; "a scenario-specific validated GPU port, not a complete GPU port of all CReSS executions"; no production use stated. — [arXiv HTML](https://arxiv.org/html/2608.13122)
- Verdict: broadly accurate; correct "162 routines" to "162 kernels (OpenMP regions) exercised by one scenario", "element by element" to "element-wise within 1e-5 at one dumped state", and add that 5.1x is single-node, single-scenario.

**(b) arXiv 2608.04400 (surrogate + Newton–Krylov)**
- "Reliable and efficient steady CFD from surrogate predictions through Newton–Krylov correction"; Mingcheng Lei, Weishao Tang, Yufei Zhang, Haixin Chen (School of Aerospace Engineering, Tsinghua University); v1 5 Aug 2026; physics.flu-dyn; preprint. — [arXiv abs](https://arxiv.org/abs/2608.04400); full text read from the PDF
- Solver ADflow (steady RANS, Spalart–Allmaras); surrogates FSB-DiT and Direct DiT; convergence accepted at residual L2 ratio ≤1e-8. OOD benchmark: 20,052 flow states on 3,409 airfoils from optimisation trajectories; 98.1% of benchmark geometries lie beyond the 95th percentile of training distance. — [arXiv PDF](https://arxiv.org/pdf/2608.04400)
- Table 1 (FSB-DiT, 15 NK updates): median residual ratio 1.29e-3 → 9.46e-11 (≈7.1 orders); mean 1.73e-3 → 1.64e-6 (≈3 orders, still above the 1e-8 threshold); 90th percentile 3.26e-3 → 2.12e-9. — [arXiv PDF](https://arxiv.org/pdf/2608.04400)
- Control test: from the same surrogate state, NK converged in 14 updates / 5.6 s vs approximate NK 297 / 58.1 s vs pseudo-time 12,883 / 453.1 s; with NK fixed, uniform and pseudo-time starting states failed within budget. — [arXiv PDF](https://arxiv.org/pdf/2608.04400)
- 15.5x (Table 2): per generation of 32 candidates, CFD 1,080.15 s on 72 CPU cores vs surrogate + ≤6 NK updates 69.90 s on 1 GPU + 72 cores (surrogate alone 29.46 s). Online drag error vs converged CFD fell from 11.8 to 1.7 drag counts (RAE2822) and 10.0 to 0.4 (OAT15A). 3D flying wing, 48 planform-OOD cases: median residual 1.32e-2 → 1.36e-9. — [arXiv PDF](https://arxiv.org/pdf/2608.04400)
- Verdict: accurate in substance; the reduction is the solver's work starting from the surrogate guess, measured on the median; 2D structured meshes; speedup per optimisation generation.

**(c) arXiv 2605.08988 (interatomic potentials)**
- "Benchmarking Compositional Generalisation for Machine Learning Interatomic Potentials"; Amir Masoud Nourollah, Irtaza Khalid, Stefano Leoni, Steven Schockaert (Cardiff University); v1 9 May 2026, v2 22 Oct 2026; accepted at NeurIPS 2026 Evaluations & Datasets Track. — [arXiv abs](https://arxiv.org/abs/2605.08988)
- Wording is "often an order of magnitude higher than on in-distribution examples"; MACE energy errors up to "more than two" and "about three orders of magnitude" worse on some tasks; fine-tuned foundation models (UMA-small, MACE-MP-0) "do not consistently outperform from-scratch models"; scope small H/C/N/O molecules in vacuum (PBE/def2-TZVP+D3BJ). — [arXiv HTML](https://arxiv.org/html/2605.08988)
- Verdict: "about ten times" is the typical force-error gap on purpose-built compositional splits, not a general rate for all unseen molecules.

**(d) McGreivy and Hakim 2024**
- "Weak baselines and reporting biases lead to overoptimism in machine learning for fluid-related partial differential equations", Nick McGreivy and Ammar Hakim, Nature Machine Intelligence 6(10), Oct 2024, DOI 10.1038/s42256-024-00897-5 (arXiv 2407.07218, 9 Jul 2024). 79% (60/76) of articles claiming to outperform a standard numerical method "compare to a weak baseline"; outcome-reporting and publication bias "widespread". Peer-reviewed; older than 2025 (flag). — [arXiv](https://arxiv.org/abs/2407.07218); [OSTI](https://www.osti.gov/pages/biblio/2475825-weak-baselines-reporting-biases-lead-overoptimism-machine-learning-fluid-related-partial-differential-equations)

**(e) arXiv 2604.18491 (Dallara)**
- "Faster by Design: Interactive Aerodynamics via Neural Surrogates Trained on Expert-Validated CFD"; Thumiger, Bartezzaghi, Rigotti, Skura, Frick, Serioli, Arbucci, Malossi (IBM Research; Dallara Automobili); v1 20 Apr 2026, v2 27 Apr 2026; 7 pp; preprint. — [arXiv abs](https://arxiv.org/abs/2604.18491)
- "Dallara established specific absolute error thresholds in advance": a usability threshold (concept exploration) and a stricter CFD-replacement threshold, per-part absolute drag-coefficient errors (values redacted). GIST met usability for all 20 parts and CFD-replacement for 18 of 20; whole-car drag error 0.6%, downforce 0.7%; 625 samples, ~4.8M-point meshes. — [arXiv HTML](https://arxiv.org/html/2604.18491)
- Verdict: correct that full replacement was not claimed, but it missed the replacement threshold on only 2 of 20 parts.

**(f) arXiv 2509.18178 (Foam-Agent 2.0)**
- "Foam-Agent 2.0: An End-to-End Composable Multi-Agent Framework for Automating CFD Simulation in OpenFOAM"; Ling Yue, Nithin Somasekharan, Tingwen Zhang, Yadi Cao, Shaowu Pan; v1 17 Sep 2025, v2 30 Sep 2025; preprint (2025, flag). 110-task benchmark: 88.2% success with Claude 3.5 Sonnet vs 55.5% for MetaOpenFOAM; meshing, HPC scripts, ParaView, MCP tools. — [arXiv abs](https://arxiv.org/abs/2509.18178)

**(g) Siemens/NVIDIA lithography**
- Siemens release dated 15 Oct 2026: "at least 10x acceleration for key lithography simulation workloads" and "simulation speed-ups ranging from at least 10x to 17x for key workloads" with cuLitho in Calibre; no baseline, no customer named. eeNews Europe (16 Oct) headlines "up to 12x faster full-chip OPC". Company claim, unconfirmed. — [iConnect007 reprint of Siemens release](https://iconnect007.com/article/152003/siemens-advances-ai-chip-lithography-with-nvidia-culitho/152000/smt); [eeNews Europe](https://www.eenewseurope.com/en/siemens-and-nvidia-speed-up-ai-chip-lithography-by-12x/); [engineering.com, 23 Oct](https://www.engineering.com/siemens-and-nvidia-accelerate-computational-lithography/)

**(h) July 2026 Kimi K3 / EDA episode** (being completed)
- Moonshot's own K3 blog: "As an early proof of concept, Kimi K3 designed a chip to serve a nano model…"; "In a single 48-hour autonomous run, K3 built, optimized, and verified the chip using open-source EDA tools"; Nangate 45 nm, within 4 mm², timing closed at 100 MHz, >8,700 tokens/s "in simulation"; tools not named; no tape-out. Company claim, unconfirmed. — [Kimi blog](https://www.kimi.com/blog/kimi-k3)
- 17 Jul 2026: Cadence −9.6% intraday to $329.56 (prior close $364.65) per Investing.com; closed −9.47% at $330.11 per TIKR; "roughly 9%" for both CDNS and SNPS per Investing.com/Yahoo. — [Investing.com](https://www.investing.com/news/stock-market-news/why-is-cadence-design-systems-stock-plummeting-today-93CH-4798909); [TIKR](https://www.tikr.com/blog/cadence-stock-fell-9-in-a-day-on-a-chinese-ai-chip-demo-heres-where-the-stock-could-go-in-2026); [Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/cadence-synopsys-slide-kimi-k3-162824133.html)

**(i) FugakuNEXT**
- RIKEN, 22 Aug 2025: "AI-oriented hardware performance exceeding 600 exaFLOPS (EFLOPS) in FP8 precision (sparse)"; "expected to become the world's first 'Zetta-scale' system as a supercomputer for HPC"; NVIDIA's Ian Buck: "zettascale performance with application speeds nearly 100 times faster"; >5x hardware, 10-20x from software, up to 100x application performance, ~40 MW, operation around 2030. — [RIKEN](https://www.riken.jp/en/news_pubs/news/2025/20250822_1/index.html)
- The Next Platform: 600 EF is FP8 with sparsity; first zettascale "as measured in sparse FP4 performance" at 1,200 EF is the author's inference; FP64 given as "30 EFLOPS or more" (table) and "more than 2.6 exaflops" (text), unreconciled. — [The Next Platform, 22 Aug 2025](https://www.nextplatform.com/hpc/2025/08/22/nvidia-tapped-to-accelerate-rikens-fugakunext-supercomputer/1638019)

### Inferences
- (to be completed)

### Gaps
- (to be completed)

## Q2. Prior 1: AI-built GPU versions of CPU-only open codes by 2028 (60%)
(in progress — inventory and AI-porting projects: CReSS, NICAM, FESOM2, ORB5X, LANL Fortran-to-Kokkos)

## Q3. Prior 2: agents cut question-to-result time five-fold by 2028 (65%)
(in progress)

## Q4. Prior 3: learned-proposer / solver-certifier as default in commercial solvers by early 2030s (55%)
(in progress)

## Q5. Prior 4: order of change (speed, scale, accuracy)
(in progress)

## Q6. Prior 5: ease of use stops protecting vendors; sign-off solver remains
(in progress)

## Q7. Prior 6: hardware shift to AI-oriented supercomputers and FP64
(in progress)

## Could not verify
(in progress)

## Dated source list
(in progress)
