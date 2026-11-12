# Technical evidence on how AI is changing physical simulation software, and tests of six prior views (as of 12 Nov 2026)

Method note: pages accessed 12 Nov 2026; about half the evidence comes from raw results gathered earlier that day (interrupted first attempt, sibling strands), re-read here. WebSearch, Firecrawl, Exa and Consensus quotas ran out mid-session; later checks used direct page fetches and GitHub. Labels: [PR] peer-reviewed or accepted at a reviewed venue; [PP] preprint; [CC] company claim, unconfirmed by any outside party; [2024]/[2025] = older than 2026.

## Summary for the report writer

- **Cited items: all nine exist; four need correcting.** (a) CReSS: "162 routines" are 162 GPU kernels (OpenMP regions exercised by one typhoon case, of 387), checked element-wise against one dumped state at 1e-5 (single precision); 5.1x is per step on one GH200 (H100 vs its 72-core Grace); "scenario-specific", not in production. (b) 2608.04400: >7 orders is the *median* residual ratio; the mean fell ~3 orders and stayed above the 1e-8 acceptance level; 15.5x is per optimisation generation, with an added GPU and ≤6 Newton updates. (c) 2605.08988: "often an order of magnitude", up to ~1,000x for energies, on purpose-built compositional splits. (e) Dallara: the replacement threshold was met on 18 of 20 parts. (g) Siemens 10-17x: company claim, no baseline or customer. (h) Kimi K3: Moonshot's own blog (45 nm, simulation only); 17 Jul closes Cadence −9.47%, Synopsys −7.85%; analysts split; the sign-off argument came mostly from commentators. (i) RIKEN itself says "zetta-scale" for "AI performance (FP8)": ≥600 EF FP8 with sparsity (0.6 ZF) against ≥2.6 EF FP64.
- **Prior 1 (60%) looks too high, ~25-40%.** Most listed codes already had hand-written GPU paths; no AI-built port is in production for a CPU-only code. Closest: CPPWRF (Oct 2026), an unaffiliated C++/CUDA port of WRF 4.8.0, bit-identical in FP64, 2.6-4.7x, 1 GitHub star, method unstated. AI-assisted ports (CReSS, NICAM, FESOM2, ORB5X) are 2026 preprints.
- **Prior 2 (65%) plausible, but all large numbers are company claims** (Renesas 34x, Nokia 5x, MediaTek 1.4-2x). A run that executes is not a correct result (ChatCFD: 82.1% ran, 68.12% physically faithful).
- **Prior 3 (55%) reasonable, perhaps 55-65%.** Weather centres operate learned-plus-physics hybrids (NOAA HGEFS, Dec 2025; Canada's spectral nudging, May 2026); Ansys announced Fluent AI initialisation (company claim); nothing is a default in commercial solvers; no learned preconditioner found shipping.
- **Prior 4 contradicted twice.** Deployed GPU speed is mostly hand-written by vendors and labs, not AI rewriting; in weather, learned models already beat physics on verified scores (ECMWF up to 20%; the Google DeepMind ensemble was the best individual track model in NHC's 2025 verification) while still needing physics-based starting states.
- **Prior 5 half supported.** Agents drive open tools, but vendors are wiring their own tools to agents (PyAnsys, Keysight, MATLAB connectors; Neural Concept's bridge to CATIA, NX, Abaqus); no loss of ground in 2026 data; the moat is moving to certified sign-off.
- **Prior 6 largely supported** (US and Japanese flagships AI-first; Rubin native FP64 33 TF), but the June 2026 TOP500 No. 1 is China's CPU-only LineShine, also the HPCG leader.

## Q1. Do the nine cited items say what the earlier analysis says?

### Takeaway
All nine exist and support the general direction; (b) rests on the median, (e) understates the result, (g) and (h) are company claims, and (i) needs the qualifier "FP8 with sparsity".

### Cited Findings

**(a) arXiv 2608.13122 [PP]**
- "Validation-Centric AI-Assisted GPU Porting of a 250,000+ Line Legacy Weather Simulation Code". Authors: Tetsuya Hoshino, Masaya Kato, Kazuhisa Tsuboki, Daichi Mukunoki, Takahiro Katagiri, Toshihiro Hanawa. v1 13 Aug 2026, cs.DC, "Submitted to AgenticAI4HPC 2026". — [arXiv](https://arxiv.org/abs/2608.13122)
- The code is CReSS (Cloud Resolving Storm Simulator): Fortran 90 with MPI and OpenMP, 599 files, about 260,000 lines and 387 OpenMP regions, in development since 1998. The agent was "Claude Code Opus 4.5–4.6"; the target was OpenACC with nvfortran (HPC SDK 25.9) and unified memory. — [arXiv HTML](https://arxiv.org/html/2608.13122)
- Validation used dumps of the program state at each kernel's last call in a 360-step run. The test was element-wise relative error ≤1e-5 (single precision, not bitwise), plus an application-level check on maximum and minimum pressure perturbation (<1e-4; 1.0e-5 and 5.6e-5 achieved). The 162 ported kernels are the OpenMP regions executed in the typhoon scenario. Five kernels showed single-element discrepancies (a one-ulp threshold flip, exp/log/sqrt differences, a zero-valued reference), which the developers accepted. — [arXiv HTML](https://arxiv.org/html/2608.13122)
- The 5.1x is the median time per step: 9.51 s on the 72-thread Grace CPU against 1.88 s on the H100 of the same GH200 (one Miyabi-G node, JCAHPC). The work took about 100 GPU-node hours over roughly three months. The authors' limitations: the validation "does not certify all control paths", dumps exceeded 400 GB, one scenario and one node; "a scenario-specific validated GPU port, not a complete GPU port of all CReSS executions". No production use is claimed. — [arXiv HTML](https://arxiv.org/html/2608.13122)

**(b) arXiv 2608.04400 [PP]**
- "Reliable and efficient steady CFD from surrogate predictions through Newton–Krylov correction". Authors: Mingcheng Lei, Weishao Tang, Yufei Zhang, Haixin Chen (School of Aerospace Engineering, Tsinghua University). v1 5 Aug 2026, physics.flu-dyn. — [arXiv](https://arxiv.org/abs/2608.04400)
- Set-up: the ADflow solver (steady RANS with the Spalart–Allmaras model); diffusion-transformer surrogates; a state is accepted when the residual ratio is ≤1e-8. The out-of-distribution test set is 20,052 flow states on 3,409 airfoils taken from optimisation runs; 98.1% of them lie beyond the 95th percentile of distance from the training set. — [arXiv PDF](https://arxiv.org/pdf/2608.04400)
- Table 1 (FSB-DiT model, 15 Newton–Krylov updates): median residual ratio 1.29e-3 → 9.46e-11 (about 7.1 orders); mean 1.73e-3 → 1.64e-6 (about 3 orders, still above 1e-8); 90th percentile 3.26e-3 → 2.12e-9. — [arXiv PDF](https://arxiv.org/pdf/2608.04400)
- Control test from the same surrogate state: Newton–Krylov converged in 14 updates (5.6 s), approximate Newton–Krylov in 297 (58.1 s), pseudo-time stepping in 12,883 (453.1 s). From uniform or pseudo-time starting states, Newton–Krylov failed to converge within budget. — [arXiv PDF](https://arxiv.org/pdf/2608.04400)
- The 15.5x (Table 2) is per generation of 32 candidates: 1,080.15 s for CFD on 72 cores against 69.90 s for surrogate plus at most six Newton updates on 1 GPU and 72 cores. Against converged CFD, the online drag error fell from 11.8 to 1.7 drag counts (RAE2822) and from 10.0 to 0.4 (OAT15A). In 3D, on 48 flying-wing planforms outside the training data, the median residual fell from 1.32e-2 to 1.36e-9. — [arXiv PDF](https://arxiv.org/pdf/2608.04400)

**(c) arXiv 2605.08988 [PR, NeurIPS 2026 Datasets and Benchmarks track]**
- "Benchmarking Compositional Generalisation for Machine Learning Interatomic Potentials". Authors: Amir Masoud Nourollah, Irtaza Khalid, Stefano Leoni, Steven Schockaert (Cardiff). v1 9 May 2026, v2 22 Oct 2026. — [arXiv](https://arxiv.org/abs/2605.08988)
- The paper says out-of-distribution errors are "often an order of magnitude higher" than in-distribution ones. For MACE energies the gap is "more than two" orders on one task and "about three orders of magnitude" on another. Fine-tuned foundation models (UMA-small, MACE-MP-0) "do not consistently outperform from-scratch models". Scope: small H/C/N/O molecules in vacuum. — [arXiv HTML](https://arxiv.org/html/2605.08988)

**(d) McGreivy & Hakim [PR, 2024]**
- "Weak baselines and reporting biases lead to overoptimism in machine learning for fluid-related partial differential equations", Nature Machine Intelligence 6(10), Oct 2024, DOI 10.1038/s42256-024-00897-5. Of 76 articles claiming to beat a standard method, 79% (60) "compare to a weak baseline"; outcome-reporting and publication bias are "widespread". — [arXiv 2407.07218](https://arxiv.org/abs/2407.07218)
- The two rules: compare at equal accuracy or equal runtime, and compare against an efficient numerical method. Hakim: "If I find results that seem too good to be true, they probably are." — [ScienceDaily/PPPL, 25 Sep 2024](https://www.sciencedaily.com/releases/2024/09/240925123554.htm)

**(e) arXiv 2604.18491 [PP]**
- "Faster by Design: Interactive Aerodynamics via Neural Surrogates Trained on Expert-Validated CFD". Authors: Thumiger, Bartezzaghi, Rigotti, Skura, Frick, Serioli, Arbucci, Malossi (IBM Research and Dallara). v1 20 Apr 2026, v2 27 Apr 2026. — [arXiv](https://arxiv.org/abs/2604.18491)
- "Dallara established specific absolute error thresholds in advance": a "usability threshold" and a stricter "CFD replacement threshold", both as per-part drag errors (values redacted). "The usability threshold is met for every part, while the CFD replacement threshold is met by 18/20 parts." Whole-car drag error 0.6%, downforce 0.7%. — [arXiv HTML v2](https://arxiv.org/html/2604.18491v2)

**(f) arXiv 2509.18178 [PP, 2025]**
- "Foam-Agent 2.0: An End-to-End Composable Multi-Agent Framework for Automating CFD Simulation in OpenFOAM". Authors: Ling Yue, Nithin Somasekharan, Tingwen Zhang, Yadi Cao, Shaowu Pan. 17/30 Sep 2025. Reports 88.2% success on 110 tasks with Claude 3.5 Sonnet, against 55.5% for MetaOpenFOAM, covering meshing, HPC scripts and ParaView, with tools exposed over the Model Context Protocol (MCP). — [arXiv](https://arxiv.org/abs/2509.18178)

**(g) Siemens/NVIDIA lithography [CC]**
- Siemens release, 14 Oct 2026 (Plano): "up to 12x acceleration for full-chip optical proximity correction (OPC) workloads"; "at least 10x acceleration for key lithography simulation workloads"; "Verified engineering data supports simulation speed-ups ranging from at least 10x to 17x". No GPU, baseline, workload, customer or availability is named. — [Siemens](https://news.siemens.com/en-us/siemens-calibre-nvidia-culitho/); [Calibre blog, 14 Oct](https://blogs.sw.siemens.com/calibre/2026/10/14/the-virtuous-cycle-of-silicon-how-siemens-is-accelerating-the-era-of-physical-ai-with-nvidia-culitho/)

**(h) The July 2026 Kimi K3 episode**
- What was published: Moonshot's own K3 blog. "As an early proof of concept, Kimi K3 designed a chip to serve a nano model…"; "In a single 48-hour autonomous run, K3 built, optimized, and verified the chip using open-source EDA tools." Details: Nangate 45 nm, within 4 mm², timing closed at 100 MHz, 1.46M cells, >8,700 tokens/s "in simulation". Not stated: the tools used, design-rule or layout-versus-schematic checks, or any tape-out [CC]. — [Kimi blog](https://www.kimi.com/blog/kimi-k3). K3 was released on 16 July 2026. — [Wikipedia](https://en.wikipedia.org/wiki/Moonshot_AI)
- Share moves on Friday 17 Jul 2026: Synopsys closed at $384.28 (−7.85%) and was −13.74% for the week; Cadence closed −9.47% and was −14.07% for the week; the Nasdaq fell 1.40%. — [ts2.tech](https://ts2.tech/en/synopsys-nasdaqsnps-loses-6-3-billion-following-kimi-k3-chip-design-demonstration/); Cadence closed at $330.11 — [TIKR](https://www.tikr.com/blog/cadence-stock-fell-9-in-a-day-on-a-chinese-ai-chip-demo-heres-where-the-stock-could-go-in-2026)
- Analysts. BNP Paribas called the reaction overdone and a chance to "buy the dip": top firms still use Cadence and Synopsys for complex designs. — [Seeking Alpha headline](https://seekingalpha.com/news/4615018-cadence-synopsys-sink-as-moonshot-brings-eda-disruption-risks-bnp-says-buy-the-dip), via TIKR. Needham and BNP: overreaction, because 45 nm is far from 2-5 nm. — [Mickevicius, 23 Jul](https://vidasmickevicius.substack.com/p/will-ai-disrupt-chip-design-business). Bloomberg Intelligence (Niraj Patel): "We see no immediate threat to Cadence and Synopsys' revenue bases"; Bernstein's Robin Zhu said market reactions "generally feel sensible". — [Yahoo/Investing, 17 Jul](https://finance.yahoo.com/technology/ai/articles/cadence-synopsys-slide-kimi-k3-162824133.html)
- The sign-off argument was made explicitly by commentators: TSMC requires Synopsys PrimeTime timing analysis before tape-out, and open process kits cover only old nodes. — [Tech Fund, 27 Jul](https://www.techinvestments.io/p/the-eda-crash-and-the-massive-ai). Another account: "no fabricated chip, manufacturing yield or advanced-node sign-off". — [ts2.tech](https://ts2.tech/en/synopsys-nasdaqsnps-stock-sinks-as-kimi-chip-demo-tests-the-eda-moat/). Cadence CEO Devgan, later: "Even if they design such a module, they still need EDA tools." — [36Kr, 29 Sep 2026](https://eu.36kr.com/de/p/4003768849258377)
- By 11 Nov 2026 Synopsys had recovered to $462.12, while Cadence was at $329.26, about its 17 July close. — [stockanalysis SNPS](https://stockanalysis.com/stocks/snps/history/); [CDNS](https://stockanalysis.com/stocks/cdns/history/)

**(i) FugakuNEXT and AI-oriented machines**
- RIKEN, 22 Aug 2025: "AI-oriented hardware performance exceeding 600 exaFLOPS (EFLOPS) in FP8 precision (sparse)"; "the world's first 'Zetta-scale' system as a supercomputer for HPC" (fragment as extracted); NVIDIA's Ian Buck: "zettascale performance with application speeds nearly 100 times faster". — [RIKEN](https://www.riken.jp/en/news_pubs/news/2025/20250822_1/index.html)
- RIKEN's project page states the goal as "AI性能（FP8）で世界初のゼタ（Zetta）スケール" ("world's first zetta-scale in AI performance (FP8)"); operation around 2030. — [R-CCS FugakuNEXT](https://www.r-ccs.riken.jp/fugaku-next/)
- Basic-design specification (workshop, 6 Mar 2026): FP64 vector ≥2.6 EF on the accelerators plus ≥48 PF on the CPUs, about 4.8x Fugaku's 537 PF; FP16/BF16 matrix ≥150 EF; FP8 matrix ≥300 EF, or ≥600 EF with sparsity; ≥3,400 nodes; ≤40 MW. The government target was "≥50 EFLOPS effective" for AI, "with zetta-FLOPS-scale peak in mind". — [RIKEN workshop PDF](https://www.r-ccs.riken.jp/events/20260306-1/fugakunext-3.pdf)
- Conflict: The Next Platform derives "zettascale" from sparse FP4 (1,200 EF, the author's own inference) and lists FP64 as "30 EFLOPS or more", which contradicts RIKEN's ≥2.6 EF. — [Next Platform, 22 Aug 2025](https://www.nextplatform.com/hpc/2025/08/22/nvidia-tapped-to-accelerate-rikens-fugakunext-supercomputer/1638019)

### Inferences
- (a) and (c) hold if worded precisely; (b) should say "median" and "per generation"; (e) is closer to replacement than implied; (h) was a company demo and analysts disagreed; (i) is accurate (even FP8 with sparsity is 0.6 ZF).

### Gaps
- The Kimi K3 EDA technical report was not found. The Seeking Alpha text on BNP returned HTTP 403, so its reasoning is known only second-hand. Siemens's 10-17x has no published baseline.

## Q2. Prior 1: half of CPU-only open codes have an AI-built GPU version in use by 2028 (60%)

### Takeaway
The population is smaller than assumed, since many listed codes already had hand-written GPU paths. For those still CPU-only, no AI-built GPU port is in production, though AI-assisted porting became fast and cheap in 2026.

### Cited Findings

**Inventory (status in the main release line, Nov 2026; "HW" = hand-written)**

| Code | GPU status | AI-built port? | Source |
|---|---|---|---|
| OpenFOAM | v2606 is "the first release to support GPU offloading" (C++ std::execution; field algebra, linear solvers, boundaries; "non-deterministic"; separate track, target v2612). HW by Keysight/OpenCFD, STFC, Exeter, AMD, NVIDIA. SPUMA, a full port, is a Dec 2025 preprint [PP] | none stated | [openfoam.com](https://www.openfoam.com/node/684); [SPUMA](https://arxiv.org/abs/2512.22215) |
| SU2 | Experimental GPU linear solver (CUDA FGMRES in v8.3.0, 1 Sep; GPU ILU and an "end-to-end CUDA FGMRES" path in v8.6.0, 30 Oct; years not shown, likely 2025/2026) | none | [GitHub](https://github.com/su2code/SU2/releases) |
| Code_Saturne | Partial: AmgX/HYPRE GPU solvers (2020-21); HIP backend and GPU-compatible API in 9.2.0 (6 Jul 2026) | none | [NEWS](https://raw.githubusercontent.com/code-saturne/code_saturne/master/NEWS.md) |
| NekRS | GPU-native (OCCA: CUDA, HIP, DPC++); v26.0 | none | [GitHub](https://github.com/Nek5000/nekRS) |
| MFEM | Native GPU (memory manager, `mfem::forall`, CUDA, RAJA) | none | [mfem.org](https://mfem.org/gpu-support/) |
| MOOSE | Kokkos-MOOSE ports "foundational components" to GPU; "only tested with NVIDIA GPUs thus far" (HW, INL) | none | [GitHub doc](https://github.com/idaholab/moose/blob/master/framework/doc/content/syntax/Kokkos/index.md) |
| LAMMPS | GPU package (CUDA, OpenCL, HIP) and KOKKOS package (CUDA, HIP, SYCL); manual dated 30 Sep 2026 | none | [docs](https://docs.lammps.org/Speed_packages.html) |
| MPAS | OpenACC GPU dynamical core in the main line (8.4.0: data movement, GPU-resident halo exchanges) | none | [GitHub](https://github.com/MPAS-Dev/MPAS-Model/releases) |
| ICON | Gordon Bell Prize 2025: full Earth system at 1.25 km on GH200 (JUPITER, Alps), 145.7 simulated days per day; release 2026.10 (30 Oct 2026) | none | [ICON news, 15 Dec 2025](https://www.icon-model.org/news/news-1/icon-simulation-wins-gordon-bell-prize-for-climate-modelling-2025); [icon-model.org](https://www.icon-model.org/) |
| OpenLB | NVIDIA and AMD GPUs (AMD initial in 1.9, 19 Dec 2025); Intel via SYCL, preliminary (2 Mar 2026) | none | [openlb.net](https://www.openlb.net/news/) |
| CalculiX | Main solvers are CPU; an optional GPU direct solver (PaStiX4CalculiX, 2020) exists. A third party (7 Nov 2026) says that build "fails" on current toolchains and "parts that do build give wrong results on the GPU". Patched, it runs 6.1-7.2x faster than PARDISO above ~1M equations (RTX 3090 Ti), using FP32 factorisation with GMRES refinement to FP64 | method not stated | [ccx-gpu](https://github.com/Tj-Barrett/ccx-gpu) |
| WRF | Main line has no GPU (4.8.0, 8 Jun 2026). **CPPWRF v1.0.0** (repo created 13 Oct 2026): an unaffiliated C++20/CUDA port of WRF-ARW 4.8.0 (dynamics, physics, nesting) claiming "bit-identical to WRF v4.8.0 real*8" on CPU and on GPU (79 CUDA FP64 runs at tolerance 0 on L4, RTX PRO 6000 and A100); 192 test cases plus 33 restart checks. GPU FP64 2.6-4.7x and FP32 4.3-8.2x faster than WRF's best layout on a 24-core EPYC; no MPI, moving nests, urban or lake models; 1 star | development method not stated; no adoption found | [WRF releases](https://github.com/wrf-model/WRF/releases); [CPPWRF](https://github.com/Xassemblianist/CPPWRF) |
| FDS | No GPU in the release notes (6.11.1, 10 Jul 2026) | none found | [GitHub](https://github.com/firemodels/fds/releases) |
| GROMACS | 2026.4 is current; the page read did not list GPU backends (GPU support not re-verified) | none | [manual](https://manual.gromacs.org/current/release-notes/index.html) |
| OpenMC | Release-note index (0.16.0) shows no GPU item; GitHub search found no "openmc gpu offload" repositories | none found | [docs](https://docs.openmc.org/en/latest/releasenotes/index.html) |
| Not verified this session | Code_Aster, Elmer, FEniCS, OpenRadioss (no GPU repository found on GitHub), Quantum ESPRESSO, CP2K, E3SM, NEMO, OpenFAST, ngspice/Xyce, OpenROAD, openEMS/MEEP, Palabos | — | — |

**AI-assisted porting projects (all preprints, none in production)**
- CReSS: see Q1a. A secondary summary says the agent "spent an entire session modifying the dump function" over a misdiagnosed bug. — [arXiv](https://arxiv.org/abs/2608.13122); [Signals summary](https://signals.aktagon.com/articles/2026/08/validation-centric-ai-assisted-gpu-porting-of-a-250000-line-legacy-weather-simulation-code/)
- NICAM (Ren, Shimokawabe, Yashiro; 30 Oct 2026): about 140,000 lines of Fortran/OpenACC became about 35,000 lines of C++/Kokkos, with Claude Code "primarily with the Fable 5 model". The record: 797 human instructions and 6,007 assistant messages over 23 active days; 4,024.8M tokens; about US$5,589 at API list prices. Validation: 100-member ensembles, with 95.3% of z-scores within |z|≤2; components to 1e-13 relative error. Speed: 1.71x on GH200 and 1.54x on MI300A, compared with the *existing* Fortran/OpenACC GPU version. The authors "aim to make a production configuration" available. — [arXiv](https://arxiv.org/abs/2610.41313); [HTML](https://arxiv.org/html/2610.41313)
- FESOM2 ocean model (AWI, 9 Jun 2026): Claude Code with Opus 4.7, about 74,000 lines, Fortran → C → Kokkos. Validation: the Kokkos build on CPU is bit-identical to the C reference; on GPU it is statistically close (SST correlation 1.0, bias +1e-4 °C). One A100 node runs 1.6-3.7x faster than a 128-core CPU node; 32 GH200 nodes on JUPITER reach 3.5 simulated years per day. "Not yet a production replacement." — [arXiv](https://arxiv.org/abs/2606.11356); [HTML](https://arxiv.org/html/2606.11356)
- ORB5X gyrokinetic plasma code (Sadr et al.; v2 8 Sep 2026): Fortran to C++/Kokkos, "almost machine accuracy" against Fortran on initial test cases, runs on LUMI-G and Daint-Alps; no speed figures. — [arXiv](https://arxiv.org/abs/2607.17363)
- Agentic Fortran-to-Kokkos workflow (Gupta et al., report LA-UR-25-28882; v5 28 Oct 2026): kernels only; GPT-5 and o4-mini-high were the most reliable, while open-weight models struggled. — [arXiv](https://arxiv.org/abs/2509.12443)
- Validation ranges from element-wise tolerance on dumps (CReSS) and ensemble statistics (NICAM) to bitwise checks against a C reference (FESOM2) and bit-identical FP64 on GPU (CPPWRF, by replicating summation order and libm and disabling fused multiply-add).

### Inferences
- Of the 28 codes, at least 12 already had hand-written GPU paths in their main or official lines; GROMACS probably also does, but that was not re-verified. That leaves perhaps 8-12 CPU-only codes (WRF and FDS confirmed; the rest unverified). For the prior to come true, four to six of those must have an AI-built port *in use* by 2028.
- Creating a port is no longer the bottleneck: NICAM took 23 active days for about US$5.6k, and CPPWRF appeared about four months after WRF 4.8.0. Adoption is the bottleneck. Upstream teams are choosing hand-written portability layers (OpenFOAM, MOOSE, MPAS, ICON), and CPPWRF is "not affiliated with or endorsed by NCAR".
- **Today: about 25-40%, not 60%.** The figure depends on whether one production user counts as "in use".

### Gaps
- Status of the 14 codes marked "not verified". No evidence found on who uses CPPWRF, or how it was developed.

## Q3. Prior 2: agents cut question-to-result time five-fold at early adopters by 2028 (65%)

### Takeaway
Agents that set up and run simulations exist and are being sold. Reported gains of 5x or more come only from vendors, mostly in chip design (EDA). Benchmarks show a large gap between a run that executes and a result that is physically correct.

### Cited Findings
- **Benchmarks.**
  - ChatCFD (v3 7 Feb 2026; journal version in Adv. Intell. Discov. 2025): runs completed in 82.1% of 315 cases, against 6.2% for MetaOpenFOAM and 42.3% for Foam-Agent; "physical fidelity" was 68.12%; about $0.208 per case, using DeepSeek-R1/V3. — [arXiv](https://arxiv.org/abs/2506.02019)
  - Foam-Agent scored 88.2% on its own benchmark, against 42.3% here, so results depend heavily on the benchmark. — [arXiv](https://arxiv.org/abs/2509.18178)
  - CFDLLMBench (CFDQuery, CFDCodeBench, FoamBench; J. Data-centric ML Research 2026, v3 26 Apr 2026) scores executability, accuracy and convergence. — [arXiv](https://arxiv.org/abs/2509.20374)
  - FEABench (Google; Apr 2025, NeurIPS 2024 workshops): the best strategy "generates executable API calls 88% of the time" in COMSOL. — [arXiv](https://arxiv.org/abs/2504.06260)
- **Commercial launches [CC].**
  - Synopsys AgentEngineer and its Autopilot platform (28 Sep 2026): agents for verification, implementation, analog, manufacturing and "simulation and analysis", including task agents for "combustion, resonance, and signal integrity". — [Synopsys](https://news.synopsys.com/2026-09-28-Synopsys-Powers-Autonomous-Engineering-with-a-Broad-Portfolio-of-Long-Horizon-Agents-and-Autopilot-Platform)
  - Ansys 2026 R1 (11 Mar 2026): a Mesh Agent ("exploratory use"), a Discovery Validation Agent ("early customer evaluation") and Engineering Copilot. — [Synopsys](https://news.synopsys.com/2026-03-11-Synopsys-Launches-Ansys-2026-R1-to-Re-Engineer-Engineering-with-Joint-Solutions-and-AI-Powered-Products)
  - Cadence ChipStack (Feb 2026; "up to 10x" productivity; early access for Altera, NVIDIA, Qualcomm and Tenstorrent). — [EE Times Japan](https://eetimes.itmedia.co.jp/ee/articles/2602/25/news040.html)
  - Cadence Maestro models (27 Oct 2026; early access in Q4 2026). — [engineering.com](https://www.engineering.com/cadence-launches-ai-model-portfolio-for-engineering-workflows/)
  - Siemens Fuse EDA AI Agent, for "autonomous, long-running, self-verifying EDA workflows". — [Siemens](https://news.siemens.com/en-us/siemens-tsmc-oip-ecosystem-forum-2026/)
  - Dassault virtual companions: on the latest release for 100% of cloud customers, enabled for 12-14% of the on-premises base, ~100 strategic customers on use cases; priced per user (humans and agents) plus units of work and tokens (Q3 2026 call). — [Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-dassault-systemes-beats-q3-2026-estimates-shares-fall-93CH-4978361)
- **Gains at named adopters [CC, Cadence Q3 2026 call, 26 Oct 2026].** MediaTek (ChipStack in production verification): 50-70% better coverage and "1.4–2x lower engineering effort". Renesas (InnoStack): 34x productivity. Socionext: up to 5x expected. Nokia (AuraStack on Cadence's Millennium system): 5x. — [TradingKey transcript](https://www.tradingkey.com/news/transcripts/262240586-tradingkey). NVIDIA is piloting AgentEngineer for formal verification. — [Synopsys, 28 Oct 2025](https://news.synopsys.com/2025-10-28-Synopsys-Spotlights-Agentic-AI,-Accelerated-Computing,-and-AI-Physics-at-NVIDIA-GTC-Washington,-D-C)
- **Large time-to-result cuts in simulation come mostly from GPUs, not agents [CC].** Ansys Speos at T-Systems: 4.5 h → 19 min. Lumerical at iPronics: a 9-day parameter sweep → 18 h. Sentaurus at Infineon: 12x. — [Synopsys, 21 Oct 2026](https://news.synopsys.com/2026-10-21-Synopsys-at-NVIDIA-GTC-Berlin-Delivering-Engineering-Precision-with-Speed)
- **Documented failure modes.**
  - NICAM: the agent carried over Fujitsu-specific directives, shortened variable names, and missed an initialisation step that unit tests did not expose; it generated code faster than humans could review, and sessions hit "five-hour usage limits". — [arXiv HTML](https://arxiv.org/html/2610.41313)
  - FESOM2: the model tended to "simplify" or "improve" code and to describe the Fortran from paraphrase rather than the source. A hardcoded 1e-9 constant (instead of 0.1) caused an Arctic instability after about 110 model days, and a CUDA-only preprocessor guard silently disabled the GPU path on AMD. — [arXiv HTML](https://arxiv.org/html/2606.11356)

### Inferences
- If vendor-reported gains at early adopters count, a five-fold cut by 2028 is likely, and the EDA claims already exceed it. If independent measurement of the whole loop from question to result is required, no such study exists yet.
- In engineering simulation outside chip design, agents are at the "exploratory" stage.
- **Today: about 65% if company numbers count; about 40-50% if independent measurement is required.**

### Gaps
- No independent or third-party time study was found. Success rates for agents running finite-element, molecular-dynamics or COMSOL jobs end to end were not established beyond the abstracts above.

## Q4. Prior 3: learned model proposes, solver certifies, as a default in major commercial solvers by the early 2030s (55%)

### Takeaway
The pattern already runs in operational weather forecasting and is built into agentic chip-design tools. In commercial CFD it has been announced but not made the default.

### Cited Findings
- **Weather, operational.**
  - ECMWF's AI model (AIFS) went operational on 25 Feb 2025 at 28 km, "outperforms… for many measures… gains of up to 20%", uses about 1,000x less energy, and runs alongside the physics model (IFS). — [ECMWF](https://www.ecmwf.int/en/about/media-centre/news/2025/ecmwfs-ai-forecasts-become-operational)
  - Its ensemble followed on 1 Jul 2025 (51 members, 31 km against IFS's 9 km); it "relies on physics-based data assimilation". — [ECMWF](https://www.ecmwf.int/en/about/media-centre/news/2025/ecmwfs-ensemble-ai-forecasts-become-operational)
  - NOAA (17 Dec 2025): AIGFS uses 0.3% of GFS compute but degrades tropical-cyclone intensity; AIGEFS uses 9% of GEFS compute. HGEFS, a 62-member physics-plus-AI ensemble, "consistently outperforms" both, which NOAA calls the first operational hybrid. — [NOAA](https://www.noaa.gov/news-release/noaa-deploys-new-generation-of-ai-driven-global-weather-models)
  - Canada (27 May 2026): an operational hybrid in which the AI model GEML "guides" the physics model at large scales by spectral nudging, while small scales evolve under physics; Canada calls it "the first of its kind". — [ECCC](https://www.canada.ca/en/environment-climate-change/news/2026/05/environment-and-climate-change-canada-launches-ai-weather-model-to-strengthen-forecasting-for-severe-weather.html)
  - DWD's AICON (operational 2 Mar 2026) starts from ICON analyses. [PP] — [arXiv 2608.24651](https://arxiv.org/abs/2608.24651)
- **CFD [CC].** Ansys Fluent "AI initialization" with NVIDIA PhysicsNeMo/DoMINO "multiplies GPU time gains by 10x"; "two weeks… about 40 minutes". (Synopsys, 28 Oct 2025, Q3). At Blue Origin, AI-proposed candidates were "validated by CUDA-X-accelerated solvers". — [NVIDIA blog, 28 Oct 2025](https://blogs.nvidia.com/blog/ai-physics-aerospace-automotive-design-engineering). No evidence was found that Fluent's AI initialisation is generally available or the default.
- **EDA [CC].** In Cadence's Maestro, "principled algorithms and deterministic solvers" check agent output against "ground truth". — [engineering.com, 27 Oct 2026](https://www.engineering.com/cadence-launches-ai-model-portfolio-for-engineering-workflows/). Siemens describes its Fuse agents as "self-verifying" (Siemens forum page, Q3).
- **Lithography.** Calibre with cuLitho accelerates physics-based simulation; it is not machine learning (Calibre blog, Q1g). TSMC "is using" cuLitho for "20-50% improvement in cost effectiveness or cycle time" [CC]. — [NVIDIA, 1 Jun 2026](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-and-TSMC-Bring-AI-Into-Fabs-to-Advance-Semiconductor-Design-and-Manufacturing/default.aspx).
- **Drug discovery.** Boltz-2 (MIT et al., 18 Jun 2025) [PP, 2025] claims affinity predictions approaching free-energy-perturbation (FEP) accuracy at ≥1000x lower compute. — [bioRxiv](https://www.biorxiv.org/content/10.1101/2025.06.14.659707v1). OpenFE offers open-source FEP under the MIT licence. — [openfree.energy](https://openfree.energy/)

### Inferences
- Four major weather centres already run learned models in operations and anchor them to physics. They do so as parallel products or hybrids, not as the default replacing physics.
- In commercial engineering software the first offers are announced (Fluent) or built into agents (EDA). No learned preconditioner is shipping.
- **Today: 55% is reasonable, perhaps 55-65%.** The main uncertainty is whether a vendor turns it on by default.

### Gaps
- Not verified: Siemens Solido's machine-learning sampling with SPICE verification, Schrödinger's active-learning FEP+, whether Fluent's AI initialisation has shipped, and machine-learning OPC in production. These searches were not possible after the quotas ran out.

## Q5. Prior 4: the order of change (speed, then scale, then accuracy)

### Takeaway
The order depends on the domain. GPU speed has come overwhelmingly from hand-written code. In weather, accuracy gains from learned models arrived early, though they still depend on physics.

### Cited Findings
- **Speed has come mostly from hand-written code.**
  - Examples: OpenFOAM v2606 (vendors and laboratories), MOOSE, MPAS, ICON, LAMMPS, NekRS (see Q2).
  - Synopsys reports ">20 GPU-enabled… EDA and multiphysics solutions" [CC] (21 Oct 2026 release, Q3).
  - cuLitho in Calibre and at TSMC [CC] (Q4).
  - AI-rewritten ports report modest gains: NICAM 1.71x over an existing GPU code, FESOM2 1.6-3.7x, CReSS 5.1x.
- **Accuracy, counter-evidence from weather.**
  - In the National Hurricane Center's 2025 verification, the Google DeepMind ensemble mean (GDMI) "performed considerably better than all of the other individual models" for Atlantic track and slightly beat official forecasts at short range. In the eastern Pacific it "excelled from 48–120 h". — [NHC 2025 verification](https://www.nhc.noaa.gov/verification/pdfs/Verification_2025.pdf)
  - AIFS v2 wave forecasts show "substantial improvement… compared to the physical model". — [ECMWF, 12 May 2026](https://www.ecmwf.int/en/about/media-centre/news/2026/ifs-cycle-50r1-aifsv2-live)
- **Accuracy, supporting evidence (learned models fail outside their data or need physics).**
  - ECMWF stopped running GraphCast, Aurora, Pangu and FourCastNet. Fine-tuned models degraded after the physics analysis changed, because fine-tuning "introduces greater sensitivity to the exact initiating analysis". — [ECMWF blog, 11 May 2026](https://www.ecmwf.int/en/about/media-centre/aifs-blog/2026/farewell-external-ai-models)
  - AICON underestimates winds and smooths small scales. — [arXiv 2608.24651](https://arxiv.org/abs/2608.24651)
  - Interatomic potentials degrade about 10x out of distribution (Q1c), and raw surrogate residuals (about 1e-3) are far above the solver's 1e-8 acceptance level (Q1b).
- **Scale.** NHC: "we may soon have thousands of possible forecast outcomes", though "None of the models are perfect". — [NWS](https://www.weather.gov/news/261102-AI-Hurricane-Forecasting). Agent runs cost about $0.2 per case (ChatCFD).

### Inferences
- "Speed via AI rewriting" is the least supported link: by 2026, AI rewriting has added little of the GPU speed actually deployed.
- "Accuracy last" fails in weather but holds for interatomic potentials, CFD surrogates and the Dallara case. The failure on long chaotic runs was not tested directly here; climate emulators were not checked.

### Gaps
- No measured split of deployed GPU speed between hand-written and AI-written code exists. Long-run stability of learned climate models was not checked.

## Q6. Prior 5: agents erode the ease-of-use moat; certified sign-off solvers keep value

### Takeaway
The second half is supported. The first half is weakened, because vendors are opening their own tools to agents, and no loss of ground by commercial products shows up in 2026 data.

### Cited Findings
- **Agents on open tools.**
  - Kimi K3 on open EDA tools (Q1h); Foam-Agent and ChatCFD on OpenFOAM (Q3).
  - Agent "skills" for OpenFOAM, SU2, LS-DYNA, FEniCS, CalculiX, Elmer, LAMMPS, GROMACS, Quantum ESPRESSO and VASP (103 stars, Mar 2026). — [HPC-Skills](https://github.com/SciMate-AI/HPC-Skills)
- **Agents on commercial tools.**
  - PyAnsys MCP servers for Fluent, Mechanical, AEDT, MAPDL, Lumerical and CFX. — [docs.pyansys.com](https://docs.pyansys.com/)
  - Keysight ADS 2027 MCP servers, "available now" (6 Oct 2026). — [Keysight](https://www.keysight.com/us/en/about/newsroom/catalog/news-release.2026.1006_pr26-095-keysight-advances-its-design-software-with-agentic-ai.html)
  - MathWorks's MATLAB MCP server. — [GitHub](https://github.com/matlab/matlab-mcp-core-server)
  - Neural Concept MCP Bridge (19 Oct 2026), driving CATIA, NX, ANSA, HyperMesh and Abaqus. — [Neural Concept](https://www.neuralconcept.com/press-release/neural-concept-launches-mcp-bridge)
- **Vendor stance.**
  - Dassault's CEO Daloz rejected "frontier model + MCP" approaches and called a general model "useless" for advanced design exploration. — [Schnitger, 26 Aug 2026](https://schnitgercorp.com/2026/08/26/plmish-earnings-check-what-have-we-learned/)
  - Cadence's CFO: agentic AI is "a demand accelerator for EDA" (Q3 2026 call, see Q3).
- **Sign-off certification.** At TSMC's partner forum (23 Sep 2026), Cadence's digital, sign-off and custom flows were certified for A16 and A14; Siemens Calibre nmDRC, nmLVS, xACT and PERC were certified for A14; Synopsys flows "implementation to signoff" were certified for A14. — [Futurum, 24 Sep 2026](https://futurumgroup.com/insights/tsmcs-oip-forum-turns-agentic-chip-design-demos-into-production-flows/)
- **No visible loss of ground in 2026.**
  - Siemens Digital Industries software revenue rose 15% in fiscal Q3 2026, with EDA up more than 30%. Dassault's Q2 revenue was €1.556B (+4%), with 3DEXPERIENCE +14% and cloud +60% (Schnitger, as above).
  - Cadence reported a record $8.2B backlog. — [TradingKey](https://www.tradingkey.com/news/transcripts/262240586-tradingkey)
  - One market report read the July selloff as pricing "a future moat risk, not a verified revenue loss". — [ts2.tech](https://ts2.tech/en/synopsys-nasdaqsnps-stock-sinks-as-kimi-chip-demo-tests-the-eda-moat/)

### Inferences
- Agents commoditise ease of use for *both* open and commercial tools, so the open-source gain is mainly licence cost.
- Value is consolidating around certified engines plus proprietary data and models (Maestro, SimAI). This matches the prior's second half.

### Gaps
- No quantitative data were found on industrial adoption of open-source solvers, or on shifts in seat counts.

## Q7. Prior 6: hardware shift to AI-oriented supercomputers and double precision (FP64)

### Takeaway
New US, Japanese and European flagships are AI-first, and native FP64 per GPU is stagnating. China's new No. 1 is a CPU-only design oriented to double precision.

### Cited Findings
- **US.** Solstice (100,000 NVIDIA Blackwell GPUs) and Equinox (10,000 Blackwell, 2026) at Argonne, built with NVIDIA and Oracle, will be "the largest AI supercomputer in the DOE's lab complex", for AI-for-science and agentic workflows. — [DOE, 28 Oct 2025](https://www.energy.gov/articles/energy-department-announces-new-partnership-nvidia-and-oracle-build-largest-doe-ai)
- **Japan.** FugakuNEXT (Q1i). RIKEN's route to 100x relies on software: surrogates and physics-informed networks (10-20x), mixed precision, and FP64 emulation by the Ozaki scheme (2-8x). — [RIKEN PDF](https://www.r-ccs.riken.jp/events/20260306-1/fugakunext-3.pdf)
- **TOP500 (June 2026).**
  - No. 1 is LineShine (National Supercomputing Centre in Shenzhen): 2.198 EF on HPL, CPU-only (304-core LX2 processors), the leader on HPCG at 22.00 PF, and "the first China-based system to lead the TOP500 since Sunway TaihuLight in 2017". JUPITER Booster (GH200) is No. 5 at 1.000 EF. Eight of the top 10 use accelerators. — [TOP500](https://top500.org/lists/top500/2026/06/)
  - Korea, Taiwan, India and Israel in the top 100 are mostly AI clouds: NHN Cloud B200 (No. 20), Samsung SSC-24 H100 (25), Yotta Shakti H100 (32), NCHC Nano 4 H200 (33), Israel-1 H100 (59), SDS AI B200 (70-71) (same list).
- **HPL-MxP (June 2026).** El Capitan 16.68 EF (9.2x its HPL), Aurora 11.64, Frontier 11.39, LineShine 7.92 (only 3.6x), JUPITER 7.92, SoftBank CHIE-4 3.30 (24.4x). FP8 entries have been "no longer admissible" since November 2025. — [HPL-MxP](https://hpl-mxp.org/results.md)
- **FP64 per device.**
  - Rubin has about 33 TF native FP64, below the H100. FP64 matrix rate fell from 67 TF on Hopper to 40-45 TF on Blackwell. Emulation in CUDA libraries gives Rubin "up to 200 TFLOPS" of FP64 matrix performance. — [The Register, 18 Jan 2026](https://www.theregister.com/2026/01/18/nvidia_fp64_emulation/)
  - NVIDIA's Dan Ernst: "it's still FP64. It's not mixed precision." AMD's Nicholas Malaya: emulation gives little or no benefit for 60-70% of HPC workloads, since "the vast majority of real HPC workloads rely on vector FMA, not DGEMM". He adds that it "starts to break down" for poorly conditioned problems, uses about twice the memory, and does not fully follow IEEE rules. AMD's MI430X keeps FP64 in hardware (same article).
- **Mixed precision in practice.** CalculiX's GPU direct solver defaults to FP32 factorisation with FP64 GMRES refinement, and consumer GPUs run FP64 at 1/64 of their FP32 rate. — [ccx-gpu](https://github.com/Tj-Barrett/ccx-gpu). The CReSS port runs in single precision (Q1a), and CPPWRF offers an FP32 fast mode (Q2).

### Inferences
- Conventional FP64 codes that are limited by memory bandwidth (most CFD and finite-element solvers) will still gain from bandwidth, which on Rubin is 22 TB/s of HBM4, but get little growth in FP64 compute. Dense-algebra codes depend on emulation. Sparse iterative solvers need mixed precision with FP64 refinement.
- LineShine contradicts the claim that all new scientific supercomputers are AI machines.

### Gaps
- Not verified: ORNL's Lux and Discovery, NERSC's Doudna (HTTP 403), France's Alice Recoque, Korea's KISTI-6 and India's national systems. HPCwire's Genesis Mission/Ozaki report returned HTTP 403.

## Could not verify
1. That any AI-built GPU port is in production use for any listed CPU-only code. How CPPWRF was developed, and who uses it.
2. GPU status of Code_Aster, Elmer, FEniCS, OpenRadioss, Quantum ESPRESSO, CP2K, E3SM, NEMO, OpenFAST, ngspice/Xyce, OpenROAD, openEMS/MEEP and Palabos. GROMACS GPU support was not re-checked.
3. Whether Fluent's AI initialisation has shipped or is on by default. Siemens Solido and Schrödinger's active-learning FEP+ were not checked.
4. The Kimi K3 EDA technical report and the tools it used. BNP Paribas's full note (Seeking Alpha returned HTTP 403).
5. The baseline and hardware behind Siemens/NVIDIA's 10-17x; no foundry confirmation.
6. Any independent measurement of time saved by agents.
7. Data on industrial adoption of open-source solvers.
8. The systems listed under Q7 Gaps.
9. Which FP64 figure for FugakuNEXT is right: The Next Platform's 30 EF or RIKEN's ≥2.6 EF. RIKEN's ISC2026 handout and basic-design report (29 May 2026) were not read.
10. Regional coverage is thin for Korea, India and Israel (TOP500 entries only) and for Chinese simulation-AI work beyond Tsinghua, Moonshot and LineShine.

## Dated source list
All accessed 12 Nov 2026; each URL is given inline above.
- **Papers and preprints:** arXiv 2608.13122 (13 Aug 2026); 2608.04400 (5 Aug 2026); 2605.08988 (9 May, v2 22 Oct 2026; NeurIPS 2026 D&B); 2604.18491 (20/27 Apr 2026); 2509.18178 (17/30 Sep 2025); 2407.07218, Nature Machine Intelligence 6(10) (Jul/Oct 2024); 2610.41313 NICAM (30 Oct 2026); 2606.11356 FESOM2 (9 Jun 2026); 2607.17363 ORB5X (19 Jul, v2 8 Sep 2026); 2509.12443 (v5 28 Oct 2026); 2512.22215 SPUMA (22 Dec 2025); 2506.02019 ChatCFD (v3 7 Feb 2026); 2509.20374 CFDLLMBench (v3 26 Apr 2026); 2504.06260 FEABench (8 Apr 2025); 2608.24651 AICON (25 Aug 2026); bioRxiv Boltz-2 (18 Jun 2025).
- **Vendors and companies:** Siemens release (14 Oct 2026), Calibre blog (14 Oct 2026), Siemens TSMC forum page (Sep 2026); NVIDIA–TSMC (1 Jun 2026); NVIDIA blog (28 Oct 2025); Synopsys releases (28 Oct 2025; 11 Mar, 28 Sep, 21 Oct 2026); PyAnsys docs (undated); Cadence ChipStack (EE Times Japan, 25 Feb 2026), Maestro (engineering.com, 27 Oct 2026), Q3 2026 call (TradingKey, 26 Oct 2026); Dassault Q3 2026 call (Investing.com, Oct 2026); Keysight (6 Oct 2026); Neural Concept (19 Oct 2026); MATLAB MCP server (GitHub, undated); Moonshot Kimi K3 blog (Jul 2026).
- **Market coverage and trade press:** Investing.com (17 Jul 2026); Yahoo Finance (17 Jul); TIKR (18 Jul); ts2.tech (17 Jul); Mickevicius Substack (23 Jul); Tech Fund (27 Jul); 36Kr (29 Sep); Schnitger Corp (26 Aug); Futurum (24 Sep); stockanalysis (to 11 Nov 2026); The Register (18 Jan 2026); The Next Platform (22 Aug 2025); ScienceDaily/PPPL (25 Sep 2024); Signals (Aug 2026); Wikipedia, Moonshot AI.
- **Public bodies:** RIKEN (22 Aug 2025; workshop PDF 6 Mar 2026; project page); US DOE (28 Oct 2025); ECMWF (25 Feb 2025; 1 Jul 2025; 11 May 2026; 12 May 2026); NOAA (17 Dec 2025, updated 17 Feb 2026); NHC 2025 verification report (2026); NWS Q&A with the NHC (undated, after the 2025 season); ECCC (27 May 2026); TOP500 and HPL-MxP lists (June 2026).
- **Code repositories and documentation:** OpenFOAM v2606 page; SU2 releases (v8.6.0, 30 Oct); Code_Saturne NEWS (9.2.0, 6 Jul 2026); NekRS (v26.0); MFEM GPU page; MOOSE Kokkos doc; LAMMPS manual (30 Sep 2026); MPAS releases (8.4.x); WRF releases (4.8.0, 8 Jun 2026); CPPWRF (created 13 Oct 2026); FDS releases (6.11.1, 10 Jul 2026); ICON (2026.10, 30 Oct 2026; Gordon Bell news, 15 Dec 2025); OpenLB news (1.9, 19 Dec 2025); OpenMC release notes (0.16.0); GROMACS 2026.4 notes; ccx-gpu (created 7 Nov 2026); HPC-Skills (created 16 Mar 2026).
