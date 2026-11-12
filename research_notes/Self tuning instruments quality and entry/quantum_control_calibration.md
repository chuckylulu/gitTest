# Self-tuning instruments: quantum-computer control and calibration (as of 12 November 2026)

Status: COMPLETE (final pass written 12 Nov 2026).

Labels used: [independently confirmed: by whom] / [company claim, not independently confirmed] / [secondary report] / [inference] / "could not verify". Every figure carries its period, its publication date and a URL. Quality evidence is kept apart from entry (valuation) facts. Valuation, funding and listing data are recorded as identity facts only and are not judged.

Method note: the shared web-search budget for this research run ran out after about 25 searches. After that I used only direct fetches of known primary URLs: SEC EDGAR filings (IQM, SEEQC, Rigetti), arXiv, company newsrooms, Quantum Computing Report's 2026 news archive and government pages. Some items below therefore rest on trade-press headlines (labelled [secondary report: QCR headline]). Coverage of China (QuantumCTek, Origin Quantum's IPO status, ZWDX), the UK/EU/Japan export-control texts, Riverlane's 2026 funding and Quantum Machines' revenue is thin. Section 7 lists these gaps. A few facts are cross-referenced from sibling team notes in the same folder (electronic_test_measurement.md, asia_china_korea_taiwan_india.md). Those are marked "[from team notes; source as cited there]" and I did not re-fetch them.

---

## 1. Segment map (by region)

### Takeaway
The segment has four layers.
1. Room-temperature control electronics: Quantum Machines, Zurich Instruments (Rohde & Schwarz), Qblox, Keysight and QuEL, plus the open QICK and QubiC designs.
2. Calibration and control software and AI models: Q-CTRL, Qruise, QuantrolOx, Quantum Elements and Conductor Quantum; NVIDIA's open Ising models; general agent harnesses such as Claude Code and Anthropic's MHS.
3. Real-time error-correction stacks: Riverlane, NVIDIA NVQLink and decoders.
4. Processor makers who increasingly build control in-house: IBM, Google, IQM, SDT, Origin Quantum and SpinQ, and Rigetti through contract manufacturer Quanta.

2026 brought a listing wave among processor makers: IQM, Quantinuum, Infleqtion, Xanadu, Horizon and SEEQC listed, and Pasqal is pending. Only one control/calibration specialist raised a mega-round: Q-CTRL, US$290m on 12 Nov 2026. Quantum Machines last raised in Feb 2025. China is running a separate, domestic stack.

### Cited Findings

#### 1.1 Control electronics vendors (room temperature)
- Quantum Machines (QM; Israel; private). Sells the OPX1000/OPX+ controllers, the QUA language/Quantum Orchestration Platform, the open-source QUAlibrate calibration framework, DGX Quantum with NVIDIA, the "Open Acceleration Stack" (Mar 2026) and the OPNIC network card. It operates the Israeli Quantum Computing Center (IQCC). Details in 4.1. — [Gix Internet 6-K, 26 Oct 2026 ("Israeli Quantum Computing Center Operated by Quantum Machines")](https://www.sec.gov/Archives/edgar/data/1782265/000149315226048578/form6-k.htm); [QCR, 16 Mar 2026](https://quantumcomputingreport.com/quantum-machines-introduces-open-acceleration-stack-for-hybrid-computing/)
- Zurich Instruments (Switzerland; wholly owned by Rohde & Schwarz since June 2021). Sells HDAWG, SHFQC/SHFQC+, QCCS (first commercialised 2018), ZQCS (launched 9 Mar 2026; >1,000 channels per 19-inch rack; direct-RF; FPGA and GPU links) and the LabOne Q software. — [QCR, 9 Mar 2026](https://quantumcomputingreport.com/zurich-instruments-launches-zqcs-quantum-control-system/); [Wikipedia (conflict-of-interest notice on page)](https://en.wikipedia.org/wiki/Zurich_Instruments)
- Qblox (Netherlands; private). Sells the "Cluster" open-architecture control stack for superconducting and trapped-ion systems; US manufacturing with Prodrive in Canton, Massachusetts, shipping from 1 Apr 2026; US commercial licensee of Fermilab's open QICK platform (CRADA plus licence finalised 24 Jun 2026). — [QCR, 17 Mar 2026](https://quantumcomputingreport.com/qblox-launches-u-s-manufacturing-for-quantum-control-systems/); [Qblox, 24 Jun 2026](https://qblox.com/newsroom/doe-fermilab-and-qblox-partner-to-commercialize-qick-platform-and-boost-quantum-workforce)
- Keysight (US; NYSE KEYS). Sells the Quantum Control System (PXIe/AXIe), delivered at >1,000-qubit scale to Japan's AIST G-QuAT (July 2025) and embedded in Fujitsu/RIKEN's 256-qubit machine (May 2025). — [RCR Wireless, 30 Jul 2025](https://rcrwireless.com/20250730/test-and-measurement/quantum-control-system); [JETRO, 13 Mar 2026](https://www.jetro.go.jp/biz/areareports/special/2026/0301/7f28e3ff9e1e15b0.html); [QCR headline via search](https://quantumcomputingreport.com/keysight-control-system-powers-fujitsu-and-rikens-256-qubit-quantum-computer/)
- QuEL Inc. (Japan; Osaka University/QIQB spin-out; private). Sells the QuEL-1 / QuEL-1 SE microwave qubit controllers. — [Osaka University ResOU, 27 Mar 2026](https://resou.osaka-u.ac.jp/ja/research/2026/20260327_1); [QuEL news](https://quel-inc.com/ja/category/news/)
- SDT (South Korea). Unveiled an "independently developed" Qubit Controller Unit (QCU, up to 8.5 GHz) at NVIDIA GTC 2026 and runs a 20-qubit superconducting "Kreo" system with DGX B200 servers over NVQLink in Seoul. — [QCR, 17 Mar 2026](https://quantumcomputingreport.com/sdt-launches-koreas-first-commercial-quantum-ai-hybrid-data-center-via-nvidia-nvqlink/)
- Open designs: QICK (Fermilab; RFSoC/FPGA based; now commercialised in the US by Qblox) and QubiC (LBNL; named as one of five NVQLink "control system builders" alongside Keysight, QM, Qblox and Zurich Instruments). — [DOE](https://www.energy.gov/technologycommercialization/articles/energy-department-announces-partnership-fermilab-and-qblox); [NVIDIA NVQLink release, 28 Oct 2025](https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Introduces-NVQLink--Connecting-Quantum-and-GPU-Computing-for-17-Quantum-Builders-and-Nine-Scientific-Labs/default.aspx)
- Market structure, as described by a listed peer: "Many quantum hardware developers and integrators continue to build their own control electronics, while certain vendors, such as Keysight, Zurich Instruments, Qblox, and Quantum Machines, provide off-the-shelf solutions ... broadly adopted standards have not yet emerged, particularly in the control layer." — [SEEQC 424B3 prospectus, 1 Jul 2026](https://www.sec.gov/Archives/edgar/data/1779977/000121390026074258/ea0278139-08.htm)

#### 1.2 Calibration software, AI models and agent layers
- Q-CTRL (Australia; private). Sells Boulder Opal (calibration/autonomy; "Scale Up" variant), Fire Opal (error suppression, offered through IBM Quantum Functions and IonQ), Black Opal (education) and Ironstone Opal (quantum navigation). Details in 4.2.
- Qruise (Germany, Saarbrücken; private). QruiseOS automated bring-up. Proof of concept with QM at IQCC: 21-qubit QuantWare Contralto QPU taken from uncalibrated to operational in ~15 min (May 2026). — [QCR, 2 May 2026](https://quantumcomputingreport.com/qruise-and-quantum-machines-automate-21-qubit-qpu-bring-up-at-iqcc/)
- QuantrolOx (UK; private). Quantum EDGE automated tuning. Claimed CZ gate tuned in <25 min with Qblox electronics on QuantWare QPUs (Jan 2025). First US office at UC Berkeley under a five-year MoU. APAC partner RAQS Quantum (Apr 2026); MAHE "Q-HUB" in India (Mar 2026); AQSolotl partnership (Jun 2026). — [TQI, 22 Jan 2025](https://thequantuminsider.com/2025/01/22/automated-2-qubit-gate-tuning-in-under-25-minutes-with-quantrolox-and-qblox-using-quantware-qpus/); [HPCwire](https://www.hpcwire.com/off-the-wire/uc-berkeley-welcomes-quantrolox-to-its-quantum-innovation-corridor/); [APS 2026 abstract (Naples, Quantum EDGE on QuantWare Contralto-D)](https://meetings-archive.aps.org/smt/2026/mar-l07/14/)
- Quantum Elements (US). AI/digital-twin development platform; won the 2024 IQCC calibration challenge results (see 2.4); added funding in Feb 2026 (SAFE). — [QCR archive, 21 Feb 2026](https://quantumcomputingreport.com/quantum-elements-secures-additional-funding-for-ai-driven-development-platform/)
- Conductor Quantum (US). "CODA MCP", a Model Context Protocol server that lets AI agents (Claude Desktop, Cursor and others) generate, transpile and run circuits on IBM, AQT, IQM, IonQ and Rigetti backends. No control-electronics or calibration integration is stated. Separately named as an NVIDIA Ising calibration adopter (EeroQ + Conductor "autonomous lab workflows", Apr 2026). — [QCR, 23 Mar 2026](https://quantumcomputingreport.com/conductor-quantum-launches-coda-mcp-to-integrate-quantum-tools-with-ai-agents/); [NVIDIA, 14 Apr 2026](https://nvidianews.nvidia.com/news/nvidia-launches-ising-the-worlds-first-open-ai-models-to-accelerate-the-path-to-useful-quantum-computers)
- NVIDIA Ising (open models, Apr 2026) and the Quantum Calibration Agent Blueprint (GitHub; NeMo Agent Toolkit). Details in 4.7.
- Anthropic's Model Hardware Standard (MHS), research preview of 27 Aug 2026: "a shared specification for AI agents to safely operate physical devices", reachable through MCP and to be open-sourced later. In its QuEra pilot an agent built a controller that recovered the laser "lock" inside QuEra's neutral-atom machines 99.3% of the time without human intervention. [company claim, not independently confirmed] — [Anthropic, 27 Aug 2026](https://www.anthropic.com/news/model-hardware-standard-research-preview)
- Riverlane (UK; private). Error-correction stack (Deltaflow decoders). 2026 items: QEC roadmap (12 Mar), real-time QEC latency results (9 Apr), partner in QM's Open Acceleration Stack, HPE's eight-partner initiative (15 Jun), and Rigetti's UK NQCC 36-qubit QEC upgrade. — [QCR archive](https://quantumcomputingreport.com/news-archive-2026/); [Rigetti 10-K FY2025, 4 Mar 2026](https://www.sec.gov/Archives/edgar/data/1838359/000110465926023454/rgti-20251231x10k.htm)

#### 1.3 Processor makers and their control/calibration stance
- IBM: in-house stack. Pledged US$10bn in global quantum expansion toward fault-tolerant systems by 2029 [secondary report: QCR headline, 29 May 2026](https://quantumcomputingreport.com/ibm-pledges-10-billion-global-quantum-expansion-to-deliver-fault-tolerant-supercomputers-by-2029/). Its Anderon foundry subsidiary has a US$1bn CHIPS letter of intent (21 May 2026) [QCR](https://quantumcomputingreport.com/u-s-department-of-commerce-proposes-2-billion-chips-investment-across-nine-quantum-hardware-and-foundry-developers/). Hosts Q-CTRL Fire Opal as an IBM Quantum Function [QCR, 11 Nov 2026](https://quantumcomputingreport.com/q-ctrl-deploys-fire-opal-dynamics-simulator-on-ibm-quantum-functions-achieving-12x-speedup-on-nighthawk/). Could not verify IBM's own disclosures on control-electronics sourcing in this session.
- Google Quantum AI: in-house. Its RL-during-QEC result ran on proprietary Google software (see 2.3). It acquired Atlantic Quantum [secondary report: GQI Q3 2026 summary](https://quantumcomputingreport.com/gqi-q3-2026-state-of-play-investment-consolidation-accelerating-q-day-horizons-and-the-shift-to-second-generation-architectures/).
- IQM: claims in-house control electronics and software. It also runs a joint real-time QEC demonstrator with Zurich Instruments' ZQCS. See 4.6.
- Rigetti (Nasdaq RGTI): its collaboration with Quanta Computer (Taiwan) lets Quanta develop "control systems, dilution refrigerators, flexible cables". Each party will invest ≥US$250m over five years. FY2025 revenue US$7.088m. — [Rigetti 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1838359/000110465926023454/rgti-20251231x10k.htm). QM separately ran Rigetti's Novera QPU on an OPX1000 that "replaced the native control stack" (May 2026; see 2.4).
- Quantinuum (Nasdaq QNT): IPO priced 4 Jun 2026 at US$60 for 28m shares, ~US$1.68bn gross at a ~US$15.6bn implied valuation [secondary report: QCR](https://quantumcomputingreport.com/quantinuum-completes-its-ipo-at-an-upscale-price-and-number-of-shares/). Could not verify its control sourcing.
- IonQ: first quantum company above US$100m annual revenue in FY2025, with ~US$3.3bn cash [secondary report: QCR headline, 25 Feb 2026](https://quantumcomputingreport.com/ionq-reports-fourth-quarter-and-full-year-2025-financial-results-first-quantum-company-to-surpass-100m-annual-revenue/). Named Ising Calibration adopter [NVIDIA, 14 Apr 2026](https://nvidianews.nvidia.com/news/nvidia-launches-ising-the-worlds-first-open-ai-models-to-accelerate-the-path-to-useful-quantum-computers). Integrated Q-CTRL Fire Opal (24 Apr 2026, QCR headline).
- Alice & Bob (France): NVentures backing (22 May 2026). Proposed "decoupled AI topologies" for microsecond control-loop latencies (26 Jun 2026). [secondary report: QCR headlines](https://quantumcomputingreport.com/news-archive-2026/)
- Pasqal (France): US$2.0bn pre-money SPAC merger with Bleichroeder Acquisition Corp II (Nasdaq BBCQ). F-4 filed 30 Jun 2026; ~US$500m gross proceeds if there are no redemptions; closing pending. Claims "end-to-end sovereignty over its component supply chain". — [QCR, 30 Jun 2026](https://quantumcomputingreport.com/pasqal-and-bleichroeder-acquisition-corp-ii-file-form-f-4-sec-registration-for-2-billion-public-nasdaq-merger/)
- Oxford Quantum Circuits (UK): £260m (US$350m) Series C (3 Jun 2026) and a €92m Barcelona hub (19 Jun 2026) [secondary report: QCR headlines](https://quantumcomputingreport.com/oxford-quantum-circuits-closes-260-million-series-c-round-to-scale-superconducting-quantum-infrastructure-globally/). Early QUAlibrate user (2025) [TQI](https://thequantuminsider.com/2025/05/19/quantum-machines-launches-open-source-framework-that-cuts-quantum-computer-calibration-from-hours-to-minutes/).
- SEEQC (US; SPAC with Allegro Merger Corp at a US$1bn valuation with a US$65m PIPE, announced 17 Jan 2026; 424B3 dated 1 Jul 2026; ticker SEQC): digital SFQ control chips co-located with qubits. FY2025 revenue US$4.157m. — [QCR, 17 Jan 2026](https://quantumcomputingreport.com/seeqc-to-go-public-via-merger-with-allegro-merger-corp-at-1-billion-valuation/); [SEEQC 424B3](https://www.sec.gov/Archives/edgar/data/1779977/000121390026074258/ea0278139-08.htm)

#### 1.4 NVIDIA and open-source stacks
- NVIDIA: CUDA-Q; DGX Quantum (co-developed with QM; installed at IQCC); NVQLink ("open system architecture", 28 Oct 2025; 5 control builders, 19 named QPU builders, 8 labs named); Ising Calibration and Ising Decoding (14 Apr 2026); Ising Calibration 1.5 (27 Jul 2026). — [NVIDIA, 28 Oct 2025](https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Introduces-NVQLink--Connecting-Quantum-and-GPU-Computing-for-17-Quantum-Builders-and-Nine-Scientific-Labs/default.aspx); [NVIDIA, 14 Apr 2026](https://nvidianews.nvidia.com/news/nvidia-launches-ising-the-worlds-first-open-ai-models-to-accelerate-the-path-to-useful-quantum-computers); [NVIDIA dev blog, 27 Jul 2026](https://developer.nvidia.com/blog/nvidia-ising-enables-fully-automated-quantum-computer-calibration-with-enhanced-in-context-learning)
- Open frameworks:
  - QUAlibrate (QM; BSD-3; graph-based calibration nodes; launched 19 May 2025) — [TQI, 19 May 2025](https://thequantuminsider.com/2025/05/19/quantum-machines-launches-open-source-framework-that-cuts-quantum-computer-calibration-from-hours-to-minutes/)
  - QuarkStudio (open measurement framework, used by BAQIS for its 112-qubit agent bring-up) — [arXiv 2606.22376](https://arxiv.org/pdf/2606.22376)
  - QICK (Fermilab)
  - Origin Pilot (China's open-sourced quantum OS, 7 Mar 2026) — [QCR](https://quantumcomputingreport.com/china-open-sources-origin-pilot-the-first-domestically-developed-quantum-os/)
  - Open Quantum Design open-source trapped-ion hardware repository (26 Mar 2026) — [QCR](https://quantumcomputingreport.com/open-quantum-design-launches-open-source-hardware-repository-for-trapped-ion-quantum-computing/)
- Qibolab/Qibocal (TII) and LabOne Q licence status: could not verify in this session.

#### 1.5 Regions
- China:
  - Origin Quantum "Wukong-180": 180 computational plus 251 coupler qubits; a "Quantum Computing Measurement and Control System"; the "Origin Sīnán" OS performs "automated chip calibration"; claims "full-stack independence" (14 May 2026) — [QCR](https://quantumcomputingreport.com/origin-quantum-unveils-origin-wukong-180-fourth-generation-quantum-computer/)
  - SpinQ: Series C (Jan and Apr 2026) and RMB 1bn Series D (30 Jun 2026), RMB 2bn in six months, from CICC Capital, Shanghai Semiconductor Industry Investment, AVIC Honghua, Shenzhen TopoScend and Shanghai SEARI. 25- and 103-qubit QPUs; describes an in-house "control plane" — [QCR, 30 Jun 2026](https://quantumcomputingreport.com/spinq-closes-rmb-1-billion-series-d-capitalization-to-scale-fault-tolerant-superconducting-quantum-computing-platforms/)
  - QBoson CNY 1bn Series B (7 Apr 2026); Taiyi Quantum RMB 300m (26 Jun 2026) [QCR headlines]
  - BAQIS/IOP-CAS/DP Technology "Vibe Calibration" (see 2.2)
  - CIQTEK 国仪量子 listed on SSE STAR (688828) [from team notes; SSE filing 27 Aug 2026 as cited there](https://pdf.dfcfw.com/pdf/H2_AN202608261828489393_1.pdf). Its "ION I" trapped-ion computer was reported delivered [company claim via broker note, 30 Oct 2026, from team notes](https://pdf.dfcfw.com/pdf/H3_AP202611031831349963_1.pdf)
  - QuantumCTek 国盾量子, ZWDX 中微达信 and Origin Quantum's STAR IPO status: could not verify.
- Japan:
  - Keysight QCS at AIST G-QuAT, July 2025, ">1,000 superconducting qubits", described as the "world's largest commercial" control system — [JETRO, 13 Mar 2026](https://www.jetro.go.jp/biz/areareports/special/2026/0301/7f28e3ff9e1e15b0.html)
  - G-QuAT's ABCI-Q combines NVIDIA GPUs with Fujitsu superconducting, QuEra neutral-atom and OptQC photonic machines (same JETRO source)
  - QuEL-1 SE published 24 h stability results: 15 channels, amplitude s.d. 0.09-0.22%, phase s.d. 0.35-0.44°, Review of Scientific Instruments, 27 Mar 2026, DOI 10.1063/5.0311173; funded by MEXT Q-LEAP, JST COI-NEXT and JST Moonshot — [ResOU](https://resou.osaka-u.ac.jp/ja/research/2026/20260327_1)
  - QuEL joined two JST Moonshot Goal 6 Phase 2 (2026-2030) projects (30 Apr 2026) — [QuEL news](https://quel-inc.com/ja/category/news/)
  - Nikkei reported QuEL supplies "QuEL-1" for RIKEN's 144-qubit machine and planned a 1,000-qubit compact controller for early 2026 (racks 25 -> 4) [secondary report; the article is ~1.5 years old; launch not verified] — [Nikkei xTECH](https://xtech.nikkei.com/atcl/nxt/mag/nmc/18/00011/00298/)
  - Japan FY2025 supplementary budget: ¥33.5bn for the Quantum Technology Innovation Hubs and a flagship project — [JETRO](https://www.jetro.go.jp/biz/areareports/special/2026/0301/7f28e3ff9e1e15b0.html)
- South Korea: SDT's QCU, Kreo 20-qubit system and NVQLink data centre (above); SDT–IonQ cooperation (18 Apr 2026); IonQ–KISTI NVQLink (16 Mar 2026); Yonsei is an Ising Decoding user. — [QCR archive](https://quantumcomputingreport.com/news-archive-2026/); [NVIDIA](https://nvidianews.nvidia.com/news/nvidia-launches-ising-the-worlds-first-open-ai-models-to-accelerate-the-path-to-useful-quantum-computers). SDT's listing status and funding: could not verify.
- Taiwan:
  - Quanta Computer is developing control systems for Rigetti (10-K).
  - SEEQC's US-Taiwan ecosystem: Kinpo Group co-develops room-temperature electronics for SFQ chips; ITRI manufactures SEEQC's superconducting control processors; TSMC hosts a joint tape-out with NTU and UC Berkeley (12 Jan 2026) — [QCR](https://quantumcomputingreport.com/seeqc-establishes-us-taiwan-quantum-technology-ecosystem-to-accelerate-chip-based-scaling/)
  - Academia Sinica is an NVIDIA Ising calibration adopter and an early QUAlibrate user.
  - IQM booked €2.0m of FY2025 revenue from Taiwan — [IQM 424B3](https://www.sec.gov/Archives/edgar/data/2113060/000119312526259957/d900375d424b3.htm)
- India:
  - QpiAI: 64-qubit "Kaveri" processor with a custom-hardware union-find decoder (1.5 µs cycle latency; DST-supported; National Quantum Mission) and a 25-qubit system for IIIT-Dharwad (25 Mar 2026) — [QCR](https://quantumcomputingreport.com/qpiai-implements-high-speed-hardware-decoder-for-64-qubit-kaveri-processor/)
  - Rigetti: US$8.4m order for a 108-qubit system from C-DAC (Jan 2026) — [Rigetti 10-K](https://www.sec.gov/Archives/edgar/data/1838359/000110465926023454/rgti-20251231x10k.htm)
  - IQM's Kreos loan names "QPI Quantum Pvt Ltd. (India)" as a competitor. QpiAI's funding and its control-electronics sourcing: could not verify.
- Israel:
  - QM and IQCC
  - Quantum Art: trapped ions; Series A extended to US$140m, 27 Apr 2026
  - Q-Factor: neutral atoms; US$24m seed, 6 Apr 2026
  - Qedma: error mitigation; named in IQM's competitor list
  - Quantum X Labs: acquired by Viewbix; runs QEC programmes at IQCC on OPX1000
  - QTREX: government grant
  - Classiq: an Intel definitive agreement to acquire it for US$2.3bn, reported by GQI [secondary report] — [GQI Q3 2026](https://quantumcomputingreport.com/gqi-q3-2026-state-of-play-investment-consolidation-accelerating-q-day-horizons-and-the-shift-to-second-generation-architectures/)
  - QuamCore: could not verify.

#### 1.6 Capital-markets context, 2026 (identity facts, not valuation judgements)
- Listings:
  - Infleqtion, NYSE via Churchill Capital Corp X, US$550m raised (17 Feb 2026)
  - Horizon Quantum, Nasdaq HQ via dMY Squared (19 Mar 2026)
  - Xanadu, Nasdaq/TSX XNDU (Mar 2026; "$286M" cash at Q3 2026 per QCR headline, 11 Nov 2026)
  - Quantinuum IPO, Nasdaq QNT (4 Jun 2026)
  - IQM, Nasdaq IQMX via RAAQ (2 Jul 2026)
  - SEEQC, SEQC via Allegro (2026; completion date not verified)
- Pending listings: Pasqal (US$2bn SPAC), Terra Quantum (US$3.25-3.5bn SPAC) and EigenQ (US$3bn SPAC).
- Private rounds: Q-CTRL US$290m Series C (12 Nov 2026); OQC £260m; QuantWare US$178m Series B (5 May 2026); Quantum Motion US$160m; Quobly €115m; Photonic US$200m final close at a US$2bn valuation; PsiQuantum US$1bn (GQI).
- Consolidation: IonQ–Oxford Ionics, Google–Atlantic Quantum, D-Wave–Quantum Circuits and Intel–Classiq (GQI).
- GQI describes Q3 2026 as "consolidation and capital concentration".
- [secondary report: QCR archive and GQI] — [QCR news archive 2026](https://quantumcomputingreport.com/news-archive-2026/); [QCR home, Nov 2026](https://quantumcomputingreport.com/); [GQI Q3 2026, 27 Oct 2026](https://quantumcomputingreport.com/gqi-q3-2026-state-of-play-investment-consolidation-accelerating-q-day-horizons-and-the-shift-to-second-generation-architectures/)

### Inferences
- [inference] The independent control-hardware vendors (QM, ZI, Qblox, Keysight, QuEL) are small next to the processor makers, and their customers are mostly processor startups and national labs. Every new processor-maker listing has two effects for them: a better-funded customer, and a potential in-house competitor.
- [inference] China is a closed, parallel market. Origin, SpinQ, CIQTEK and BAQIS's DDS electronics with QuarkStudio are all described as domestic. Western control vendors are effectively absent, and US export rules set a presumption of denial for D:5 countries (section 3.6).

### Gaps
- No independent market-share data for controllers (units, revenue or share of published experiments). The only share claim is QM's own ("majority"/"more than half" of QC developers).
- I could not get SDT's, QuEL's or QpiAI's funding and listing status, or Chinese control-electronics vendors' revenue (QuantumCTek, ZWDX, Origin's control business).

---

## 2. Verification of the three background items

### Takeaway
All three items resolve to real, dated sources.
- (i) IQM/NVIDIA 20-qubit: real, but it is an IQM blog post (21 Oct 2026) with no timing, no human comparison and no fidelity numbers. The model is NVIDIA Ising Calibration, an open VLM.
- (ii) arXiv 2606.22376 resolves. A Chinese academic team (BAQIS / IOP-CAS / ITP-CAS / DP Technology) used Claude Code as the agent harness, driving a fine-tuned Qwen3.6-35B-A3B. It did single-qubit bring-up of 108 of 112 qubits in 4.7 h, against an estimated 18-24 h for an expert. Two-qubit gates were not automated.
- (iii) Google: real. It is a Nature paper (Sivak et al., arXiv 2511.08493; press coverage 10 Jul 2026). A reinforcement-learning agent steered >1,000 control parameters on Willow during QEC, using detection events as the training signal, and reached ~20% lower logical error than an expert-tuned baseline.

None of the three has been independently replicated.

### 2.1 IQM + NVIDIA: agent calibrating a 20-qubit chip
- Source and date: IQM blog post "What happened when we let AI calibrate a quantum chip using NVIDIA Ising", 21 Oct 2026, by Max Haeberlein (Senior Partnership Manager, IQM). [company claim, not independently confirmed] — [IQM blog, 21 Oct 2026](https://iqm.tech/blog/what-happened-when-we-let-ai-calibrate-a-quantum-chip-using-nvidia-ising/)
- What the agent did:
  - NVIDIA Ising Calibration VLMs were connected to "IQM's own calibration software" (not named).
  - The AI read each calibration chart and chose the next step.
  - When a qubit's correct setting fell outside the chart's range, it identified those qubits, widened the scan and reran only those.
  - Every decision was logged in plain English for review.
  - Quote: "AI has calibrated all 20 qubits on an IQM quantum chip." — [IQM blog](https://iqm.tech/blog/what-happened-when-we-let-ai-calibrate-a-quantum-chip-using-nvidia-ising/)
- Time against a human: NOT reported. There is no timing, no comparison with a human or with IQM's prior automation, and no gate fidelities. I could not verify any speed-up figure for this run.
- Model used: NVIDIA Ising Calibration. The post gives no version; it says NVIDIA tested a compressed version on a DGX Station.
  - Ising Calibration 1 is open-weight, based on Qwen3.5-35B-A3B — [QCalEval, arXiv 2604.25884, 28 Apr 2026](https://arxiv.org/abs/2604.25884)
  - Ising Calibration 1.5 (31B parameters; BF16 and NVFP4; OpenMDW licence) was released 27 Jul 2026 — [NVIDIA dev blog](https://developer.nvidia.com/blog/nvidia-ising-enables-fully-automated-quantum-computer-calibration-with-enhanced-in-context-learning)
- Benchmark context: QCalEval has 243 samples across 87 scenario types and 22 experiment families (superconducting and neutral-atom). Per IQM, 57 charts come from real hardware and the rest are simulated. Ising Calibration 1 scored 74.7 zero-shot against 72.3 for the best general-purpose model. The benchmark was built and scored by NVIDIA with collaborators: among its 32 authors are NVIDIA's Sam Stanwyck, Timothy Costa, Krysta Svore and Elica Kyoseva, plus Aspuru-Guzik, NPL's Rungger and Harvard's Semeghini. It is therefore not an independent evaluation. — [arXiv 2604.25884](https://arxiv.org/abs/2604.25884)
- Precursor: on 14 Apr 2026 (World Quantum Day) IQM announced "AI-driven agentic calibration" with Ising: parallel agents inspect all qubits at each stage. It gave no qubit counts, no time figures and no named customers. NVIDIA's Sam Stanwyck called it "a pioneering demonstration". — [TQI, 14 Apr 2026](https://thequantuminsider.com/2026/04/14/iqm-ai-based-calibration-scalable-quantum-systems/). IQM's H1 2026 report lists "AI-driven parallel qubit calibration using the NVIDIA Ising open family of AI models, helping automate system tuning and improve system uptime" as an ecosystem highlight. — [IQM 6-K, 4 Aug 2026](https://www.sec.gov/Archives/edgar/data/2113060/000119312526331538/iqmx-ex99_1.htm)
- Stated limits: only 20 qubits; behaviour in unseen situations "still open"; 186 of 243 QCalEval charts are simulated.

### 2.2 arXiv 2606.22376, "Vibe Calibration" (resolves; full PDF read)
- Bibliographic details: "Vibe Calibration: Autonomous Bring-up of a 112-Qubit Superconducting Quantum Processor by a Skill-Orchestrating Language Agent". v1 submitted 21 Jun 2026 (dated 23 Jun 2026 in the PDF). 14 authors, led by Huikai Xu, Jiaxiu Han, Shigang Ou and Cheng Ye; corresponding authors Lei Wang, Lin-Feng Zhang, Pan Zhang and Hai-Feng Yu. Preprint, not peer reviewed. — [arXiv abs](https://arxiv.org/abs/2606.22376); [PDF](https://arxiv.org/pdf/2606.22376)
- Institutions: BAQIS (Beijing Key Laboratory of Fault-Tolerant Quantum Computing); IOP-CAS; ITP-CAS; UCAS; Hangzhou Institute for Advanced Study; DP Technology (深势科技, a Beijing AI-for-science company); AI for Science Institute Beijing; Hefei National Laboratory.
- Funding: NSFC, the Innovation Program for Quantum Science and Technology (2021ZD0301802) and the CAS Strategic Priority Research Program.
- Hardware: 112 frequency-tunable transmons with tunable couplers, in a 7 x 16 tilted square lattice; f01 maxima 3.8-4.3 GHz; readout ~7.0 GHz.
- Control stack:
  - Per-qubit direct-digital-synthesis sources at 6 GS/s, 16-bit, producing pulses directly at qubit frequency.
  - Readout digitised directly at 4 GS/s.
  - "QSYNC" trigger distribution, ±20 ps.
  - Software: the QuarkStudio measurement framework (quarkstudio.readthedocs.io) plus in-house quark/measlib/qulab scripts, reached through a config-store API that writes device parameters atomically.
  - The electronics maker is not named (could not verify).
- Agent and model:
  - Quote: "For the agent and the large language model, in this work we chose Claude Code and a fine-tuned Qwen model, respectively."
  - The deployed checkpoint is Qwen3.6-35B-A3B fine-tuned with a LoRA variant ("35B-DA").
  - A Qwen3.5-4B variant failed transfer tests.
  - Kimi K2.6 was the negative control: 69 tool calls and 62k tokens without executing the requested action.
  - DeepSeek-V4 was used to process training data.
- What was automated: single-qubit bring-up only.
  - Steps: init, S21 resonator search, spectroscopy including flux maps (dynamic-programming ridge fit), time-Rabi, power-Rabi, single-shot readout optimisation, T1 and Ramsey; plus a transmission-line characterisation Skill.
  - Quality gates: R^2 > 0.9 before any write-back; fit SNR ≥ 10 dB; rollback edges.
  - The backend exposes "hardware-safe qubit groups" that respect topology and shared control resources, so a damage and safety constraint is built into the interface.
  - Development ran in three phases: human-guided (1 qubit), semi-autonomous with a remote expert (16 qubits), fully autonomous (112 qubits).
- Results:
  - Full campaign: a single 4.7 h session (1.2 h wiring checks including manual cable reconnection; 3.1 h parallel per-qubit calibration; 0.4 h reporting).
  - Valid T1 fits on 108/112 qubits (96%) and T2R on 102/112 (91%), against 112/112 and 110/112 for the expert.
  - Median T1 96.2 µs (agent) vs 95.7 µs (expert). Median T2R 7.9 µs vs 14.4 µs, because the agent did not tune to the flux sweet spot.
  - The expert's full-campaign time is an ESTIMATE of 18-24 h, which is the basis of the "4-5x" claim.
  - Measured head-to-head on a random 16-qubit subset: agreement on 14/16 qubits; 0.6 h vs 3.8 h (6.3x).
  - Repeatability: frequencies within ±120 kHz rms across three power-cycled runs (8 qubits).
- Limits (from the paper):
  - Two-qubit gates, crosstalk and spectator mitigation are future work.
  - No continuous drift tracking.
  - Low-level scripts need adapting per platform.
  - The full human baseline is estimated.
  - Not peer reviewed.
  - [academic claim, not independently confirmed]

### 2.3 Google: AI steering >1,000 control parameters during error correction (July 2026)
- Paper: "Reinforcement Learning Control of Quantum Error Correction", Volodymyr Sivak et al. (299 authors, including Alexis Morvan, Paul V. Klimov, Johannes Bausch, Andrew W. Senior and Hartmut Neven).
  - arXiv 2511.08493: v1 11 Nov 2025, v4 19 Jun 2026 — [arXiv](https://arxiv.org/abs/2511.08493)
  - Nature (article id s41586-026-10759-2, per TQI's link), covered 10 Jul 2026 — [TQI, 10 Jul 2026](https://thequantuminsider.com/2026/07/10/google-study-shows-quantum-computer-can-learn-from-its-own-errors-while-it-computes/); [NextPlatform, 20 Jul 2026](https://www.nextplatform.com/compute/2026/07/20/google-uses-ai-reinforcement-learning-for-quantum-error-correction/5275023)
  - APS Global Physics Summit, March 2026 — [abstract](https://meetings-archive.aps.org/smt/2026/mar-z05/1/)
- Method: QEC detection events both correct the logical state and train an RL agent that adjusts control parameters while the computation runs. More than 1,000 parameters were steered (pulse amplitudes, frequencies, couplings) on Willow, across distance-5/7 surface codes and a distance-5 colour code.
- Results:
  - ~20% lower logical error than after exhaustive conventional calibration plus expert tuning.
  - Under injected drift: 3.5x better logical stability and 31% lower error (hardware plus decoder parameters); 2.4x and 24% (hardware only).
  - Record logical error per cycle 7.72(9)x10^-4 (surface code) and 8.19(14)x10^-3 (colour code).
  - Simulations of distance-15 codes with ~40,000 parameters suggest optimisation speed independent of size.
- Limits:
  - Proprietary Google software; the authors give a mathematical description for replication.
  - Exploration must not degrade the computation.
  - Fast drift outruns the agent.
  - Scaling results are simulation only; no other modalities.
  - [peer reviewed (Nature); not independently replicated]
- No Google blog post was located (search budget exhausted). The summary rests on the arXiv record and two trade-press articles.

### 2.4 Other 2025-2026 automated or agent-run calibration results (with confirmation status)
| Date | Who | What | Result | Confirmation |
|---|---|---|---|---|
| Sep 2024 | QM + NVIDIA | RL optimisation of a control pulse on a Rigetti QPU in real time on DGX Quantum | — | [company claim via QM release] — [QM release](https://www.quantum-machines.co/press-release/quantum-machines-and-rigetti-announce-successful-ai-powered-calibration-of-a-quantum-computer/) |
| 10 Dec 2024 | QM, Rigetti, NVIDIA; Quantum Elements, Qruise | "AI for Quantum Calibration Challenge" at IQCC: 9-qubit Rigetti Novera + OPX1000 + DGX Quantum | Quantum Elements 99.9% 1Q / 98.5% 2Q; Qruise tuned all nine qubits simultaneously; Rigetti's CTO said results matched system specs (work that can take "weeks" manually) | [secondary report: search summary of joint release] — [Rigetti IR](https://investors.rigetti.com/news-releases/news-release-details/quantum-machines-and-rigetti-announce-successful-ai-powered); [TQI](https://thequantuminsider.com/2024/12/10/ai-driven-quantum-calibration-achieved-in-rigetti-and-quantum-machines-challenge/) |
| Dec 2024 | S. Cao, ..., P. Leek, A. Aspuru-Guzik | "Agents for self-driving laboratories applied to quantum computing", arXiv 2412.07978 | — | (title and authors from the 2606.22376 reference list; paper not re-read) |
| 22 Jan 2025 | QuantrolOx + Qblox + QuantWare | Fully automated characterisation and CZ gate | <25 min | [company claim] — [TQI](https://thequantuminsider.com/2025/01/22/automated-2-qubit-gate-tuning-in-under-25-minutes-with-quantrolox-and-qblox-using-quantware-qpus/) |
| 19 May 2025 | QM | QUAlibrate open-source graph calibration | Multi-qubit superconducting calibration in 140 s at IQCC; early users OQC, Qolab, Quantum Elements, Academia Sinica, Diraq | [company claim] — [TQI](https://thequantuminsider.com/2025/05/19/quantum-machines-launches-open-source-framework-that-cuts-quantum-computer-calibration-from-hours-to-minutes/) |
| 9 Mar 2026 | Univ. Chicago (Cleland group) | LLM framework generating tools on demand; autonomous resonator characterisation and reproduction of a QND qubit measurement | No numbers on abstract page | [academic claim] — [arXiv 2603.08801](https://arxiv.org/abs/2603.08801) |
| Mar 2026 | Univ. Napoli Federico II | QuantrolOx Quantum EDGE tuning 1Q/2Q gates on a QuantWare Contralto-D | Ongoing | [academic abstract] — [APS 2026](https://meetings-archive.aps.org/smt/2026/mar-l07/14/) |
| 14 Apr 2026 | NVIDIA + partners | Ising launch; same-day Ising announcements by IQM, Q-CTRL, Infleqtion, EdenCode, EeroQ + Conductor Quantum, Northwestern/Fermilab | Calibration adopters: Atom Computing, Academia Sinica, EeroQ, Conductor Quantum, Fermilab, Harvard SEAS, Infleqtion, IonQ, IQM, LBNL AQT, Q-CTRL, UK NPL. Decoding users include Cornell, EdenCode, Infleqtion, IQM, Quantum Elements, Sandia, SEEQC, UCSD, UCSB, UChicago, USC, Yonsei | [company claim] — [NVIDIA](https://nvidianews.nvidia.com/news/nvidia-launches-ising-the-worlds-first-open-ai-models-to-accelerate-the-path-to-useful-quantum-computers) |
| 14 Apr 2026 | Q-CTRL | Boulder Opal on a 21-qubit QuantWare QPU, no human intervention | Cold start in "a few hours"; median 1Q 0.9988, ~2x the human operators' median; recovered a qubit humans had marked inoperable | [company claim] — [Q-CTRL](https://q-ctrl.com/blog/scaling-quantum-autonomy-with-nvidia-ising) |
| 2 May 2026 | Qruise + QM | 21-qubit QuantWare Contralto at IQCC; >25 single- and two-qubit experiments incl. CZ chevrons and interleaved RB | ~15 min total; no fidelities; proof of concept | [secondary report] — [QCR](https://quantumcomputingreport.com/qruise-and-quantum-machines-automate-21-qubit-qpu-bring-up-at-iqcc/) |
| 14 May 2026 | Origin Quantum | Wukong-180 with Sīnán OS "automated chip calibration" | No metrics | [company claim] — [QCR](https://quantumcomputingreport.com/origin-quantum-unveils-origin-wukong-180-fourth-generation-quantum-computer/) |
| 29 May 2026 | QM | Rigetti Novera (9 qubits) on OPX1000 replacing the native stack, tuned with QUAlibrate | Median 2Q 99.5% over 11 couplings; 1Q 99.93%; "full calibration within ten days"; results "match the peak internal calibration metrics recorded by the hardware manufacturer"; no AI mentioned | [manufacturer-matched metrics; company report] — [QCR](https://quantumcomputingreport.com/quantum-machines-achieves-99-5-two-qubit-gate-fidelity-operating-rigettis-novera-qpu/) |
| 23 Jun 2026 | Aegiq | "Automated AI calibration" (photonic) | Headline only | [secondary report: QCR headline] |
| 27 Jul 2026 | NVIDIA | Ising Calibration 1.5 | ~10% better than the next-best comparable open model zero-shot; ~86.5-86.7% better than its predecessor with in-context learning (text and figure differ) | [company claim] — [NVIDIA dev blog](https://developer.nvidia.com/blog/nvidia-ising-enables-fully-automated-quantum-computer-calibration-with-enhanced-in-context-learning) |
| 27 Aug 2026 | Anthropic MHS + QuEra | Agent-built laser-lock recovery controller | 99.3% recovery without human intervention | [company claim] — [Anthropic](https://www.anthropic.com/news/model-hardware-standard-research-preview) |
| 16 Sep 2026 | A. B. Özgüler | Analysis of AI advisers in QEC: opposite coherent X rotations give identical passive syndrome statistics, so the syndrome record alone cannot pick the right correction, and a manipulated adviser can push harmful updates. Proposes calibration-state measurements, an independent evaluator and calibration-age limits | Conditional guarantees | [academic preprint] — [arXiv 2609.19090](https://arxiv.org/abs/2609.19090) |
| 18 Sep / 11 Nov 2026 | Q-CTRL | Push-button cold-start bring-up on QuantWare Contralto-D21 | <3 h per 5-qubit feedline; 1Q SX median 99.95%; 2Q CZ device median 96% (peaks >98%); readout median 93%; run-time recalibration "through late 2026" | [company claim] — [Q-CTRL](https://q-ctrl.com/blog/making-quantum-computer-calibration-autonomous-informative-and-easy); [QCR, 11 Nov 2026](https://quantumcomputingreport.com/q-ctrl-demonstrates-push-button-cold-start-calibration-on-quantware-superconducting-qpus/) |
| 21 Oct 2026 | IQM + NVIDIA | 20-qubit Ising calibration | See 2.1 | [company claim] |

- Japanese groups: no 2025-2026 agent-calibration paper was found for RIKEN, Fujitsu or QuEL. QuEL's 2026 output is controller hardware (stability; cryogenic time-division-multiplexed voltage control for trapped ions, APL, 31 Aug 2026). Search was cut short, so this is a gap rather than a finding of absence. — [QuEL news](https://quel-inc.com/ja/category/news/)
- IBM and Alice & Bob: no automated-calibration result was located. IBM is using AI to find QEC codes (13 Jun 2026, QCR headline). Alice & Bob published on AI topologies for control-loop latency (26 Jun 2026, QCR headline).
- Independent confirmation overall:
  - The only peer-reviewed item is Google (Nature).
  - The only third-party-matched metric is QM's Novera result, which was matched against Rigetti's own internal figures.
  - No national-lab head-to-head benchmark of calibration agents or of controllers was found.

### Gaps
- IQM's 20-qubit run has no timing or fidelity data and no dedicated paper (only QCalEval).
- Google: I did not open the Nature page itself (title and date rest on arXiv plus TQI).
- 2606.22376 does not name its electronics vendor.

---

## 3. Durability of the control and calibration layer

### Takeaway
The evidence splits by layer.

Room-temperature control hardware still has buyers at scale. Recent examples:
- Keysight at AIST (>1,000 qubits) and Fujitsu/RIKEN (256 qubits)
- QM operating Rigetti's QPU and running IQCC
- ZQCS paired with IQM for real-time QEC
- HPE choosing QM and Qblox
- DOE/Fermilab choosing Qblox for QICK

But the largest and newest processor makers say they build control in-house: IQM, SDT, SpinQ and Origin, while Rigetti outsources it to Quanta. Its long-run content per qubit is threatened by cryogenic and on-chip control (SEEQC, D-Wave, EeroQ, Equal1).

Calibration software is commoditising fast:
- QM gives QUAlibrate away (BSD-3).
- NVIDIA gives Ising away as open weights.
- A Chinese academic team did 112-qubit bring-up with Claude Code, an open Qwen model and an open measurement framework.
- Google's best-in-class in-operation calibration was done in-house.

Value capture so far points to processor makers and model or compute suppliers, not to calibration-software vendors. Q-CTRL is the exception that raised a mega-round, and a large part of its pitch is navigation.

### Cited Findings

#### 3.1 Processor makers building control and calibration in-house vs buying
- IQM: "We design, fabricate, and integrate our own superconducting quantum processors, control electronics and software stack, with third party components, including cryogenic systems." Its patents cover "control electronics" and, increasingly, "pulse control, auto-calibration, error mitigation, and error correction". [company claim in SEC prospectus] — [IQM 424B3, 5 Jun 2026](https://www.sec.gov/Archives/edgar/data/2113060/000119312526259957/d900375d424b3.htm)
- IQM's Kreos loan (23 Dec 2025) defines "Competitor" as 38 names. These include Zurich Instruments, Keysight, Quantum Machines, "Qblocks" (sic), NVIDIA, QuantWare, Qedma, Fujitsu, Origin Quantum, Huawei, Alibaba and Baidu; Q-CTRL is absent. — [IQM F-4/A Exhibit 10.20, filed 3 Jun 2026](https://www.sec.gov/Archives/edgar/data/2113060/000119312526255796/d900375dex1020.htm)
- Yet IQM and Zurich Instruments run a "joint project" real-time QEC demonstrator: IQM 20-qubit processor plus ZI ZQCS plus NVQLink, <4 µs end-to-end latency (16 Mar 2026). — [QCR](https://quantumcomputingreport.com/iqm-and-zurich-instruments-develop-real-time-qec-via-nvidia-nvqlink/)
- Rigetti: control systems among the "Covered Components" Quanta Computer may develop. — [Rigetti 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1838359/000110465926023454/rgti-20251231x10k.htm)
- SDT (Korea): its own QCU. SpinQ and Origin (China): vertically integrated "control plane" / "full-stack independence". — [QCR, 17 Mar 2026](https://quantumcomputingreport.com/sdt-launches-koreas-first-commercial-quantum-ai-hybrid-data-center-via-nvidia-nvqlink/); [QCR, 30 Jun 2026](https://quantumcomputingreport.com/spinq-closes-rmb-1-billion-series-d-capitalization-to-scale-fault-tolerant-superconducting-quantum-computing-platforms/); [QCR, 14 May 2026](https://quantumcomputingreport.com/origin-quantum-unveils-origin-wukong-180-fourth-generation-quantum-computer/)
- Google: RL-QEC calibration on proprietary software (2.3).
- SEEQC's prospectus: many hardware makers "continue to build their own control electronics". — [SEEQC 424B3](https://www.sec.gov/Archives/edgar/data/1779977/000121390026074258/ea0278139-08.htm)
- Buying, by contrast:
  - AIST G-QuAT bought Keysight QCS for >1,000 qubits (Jul 2025) — [JETRO](https://www.jetro.go.jp/biz/areareports/special/2026/0301/7f28e3ff9e1e15b0.html)
  - Fujitsu/RIKEN 256-qubit machine uses Keysight QCS (May 2025) [secondary report]
  - QM's deployment partners include Fermilab, Montana State University and Horizon Quantum (May 2026) — [QCR](https://quantumcomputingreport.com/quantum-machines-achieves-99-5-two-qubit-gate-fidelity-operating-rigettis-novera-qpu/)
  - HPE's eight-partner hybrid initiative names QM and Qblox as "quantum control infrastructure" (15 Jun 2026; pre-commercial) — [QCR](https://quantumcomputingreport.com/hewlett-packard-enterprise-hpe-signals-hybrid-quantum-push-with-eight-partner-infrastructure-initiative/)
- Could not verify control sourcing at IBM, Quantinuum or IonQ from their own filings in this session.

#### 3.2 NVIDIA and open-source models/frameworks commoditising calibration software
- NVIDIA Ising Calibration: open weights (Ising 1.5 under the OpenMDW licence, covering weights, datasets, benchmarks and recipes), runnable locally (NVFP4 on a single GPU or DGX Spark). Comes with the open QCalEval benchmark and leaderboard, a "cookbook" of workflows and training data, NIM microservices for fine-tuning, and the Quantum Calibration Agent Blueprint on GitHub. — [NVIDIA, 14 Apr 2026](https://nvidianews.nvidia.com/news/nvidia-launches-ising-the-worlds-first-open-ai-models-to-accelerate-the-path-to-useful-quantum-computers); [NVIDIA, 27 Jul 2026](https://developer.nvidia.com/blog/nvidia-ising-enables-fully-automated-quantum-computer-calibration-with-enhanced-in-context-learning)
- Ising 1.5 was trained on "data generated from partner contributions across multiple qubit modalities". The model supplier aggregates the calibration data. — [NVIDIA dev blog](https://developer.nvidia.com/blog/nvidia-ising-enables-fully-automated-quantum-computer-calibration-with-enhanced-in-context-learning)
- QM's own calibration framework is open source (QUAlibrate, BSD-3). — [TQI](https://thequantuminsider.com/2025/05/19/quantum-machines-launches-open-source-framework-that-cuts-quantum-computer-calibration-from-hours-to-minutes/)
- The BAQIS team got 112-qubit bring-up from a general agent harness (Claude Code), an open model (Qwen) and an open framework (QuarkStudio). — [arXiv 2606.22376](https://arxiv.org/pdf/2606.22376)
- Q-CTRL offers a 30-day free Boulder Opal trial to QuantWare system users. — [Q-CTRL](https://q-ctrl.com/blog/making-quantum-computer-calibration-autonomous-informative-and-easy)
- Anthropic's MHS (vendor-neutral device standard, MCP-reachable, to be open-sourced; QuEra pilot) and Conductor's CODA MCP show general AI firms building the agent-to-hardware layer. — [Anthropic](https://www.anthropic.com/news/model-hardware-standard-research-preview); [QCR](https://quantumcomputingreport.com/conductor-quantum-launches-coda-mcp-to-integrate-quantum-tools-with-ai-agents/)

#### 3.3 Cheap RFSoC-based and open hardware (QICK) vs proprietary controllers
- QICK is an open-source FPGA/RFSoC design from Fermilab. DOE and Fermilab finalised a CRADA plus "full licensing arrangement" giving Qblox manufacturing, supply-chain coordination and commercial distribution of QICK in the US (24 Jun 2026; LOI Nov 2025). Exclusivity is not stated. — [Qblox, 24 Jun 2026](https://qblox.com/newsroom/doe-fermilab-and-qblox-partner-to-commercialize-qick-platform-and-boost-quantum-workforce); [DOE](https://www.energy.gov/technologycommercialization/articles/energy-department-announces-partnership-fermilab-and-qblox); [TQI, 19 Nov 2025](https://thequantuminsider.com/2025/11/19/doe-fermilab-qblox-qick-us/)
- QubiC (LBNL, open) sits beside the commercial vendors as an NVQLink "control system builder". — [NVIDIA, 28 Oct 2025](https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Introduces-NVQLink--Connecting-Quantum-and-GPU-Computing-for-17-Quantum-Builders-and-Nine-Scientific-Labs/default.aspx)
- The BAQIS 112-qubit system uses direct-RF DDS electronics (6 GS/s per channel). That is the same direct-RF architecture direction as RFSoC designs and ZI's ZQCS ("direct-RF ... first Nyquist zone"). — [arXiv 2606.22376](https://arxiv.org/pdf/2606.22376); [QCR](https://quantumcomputingreport.com/zurich-instruments-launches-zqcs-quantum-control-system/)
- QED-C and NIST completed research on compacting and optimising control electronics (26 Feb 2026). [secondary report: QCR headline] — [QCR](https://quantumcomputingreport.com/qed-c-and-nist-finalize-research-to-compact-and-optimize-quantum-control-electronics/)

#### 3.4 Integration of control into cryogenic CMOS or onto the chip
- SEEQC (Nature Electronics, reported 21 Mar 2026): SFQ digital control logic flip-chip-bonded with a five-qubit chip at 10 mK; 1Q fidelities >99.5% (peak 99.9%); nanowatts per qubit; no detectable quasiparticle poisoning. Roadmap: on-die flux control and digital readout. — [QCR](https://quantumcomputingreport.com/seeqc-reports-integrated-qubit-control-logic-operating-at-millikelvin-temperatures/)
- D-Wave: on-chip cryogenic control for gate-model qubits (6 Jan 2026). EeroQ: a CMOS control architecture for a million electron-on-helium qubits with <50 control lines (15 Jan 2026). Equal1: silicon quantum servers, US$60m round (15 Jan 2026). FrostByte €1.3m and Rhonexum US$1m (cryo-CMOS startups, 2026). HKU: cryogenic neuromorphic chip (12 Jun 2026). [secondary report: QCR headlines] — [QCR archive](https://quantumcomputingreport.com/news-archive-2026/)
- QuEL: cryogenic time-division-multiplexed voltage control for trapped ions (APL, 31 Aug 2026). — [QuEL news](https://quel-inc.com/ja/category/news/)
- Export rules already treat cryo-CMOS ICs designed for ≤4.5 K as a controlled item (US ECCN 3A901.a; see 3.6).

#### 3.5 Openness of control interfaces and who captures value
- Interfaces are largely open or being opened:
  - QUAlibrate (BSD-3) on QUA/QUAM. QUA itself is proprietary (QM's language).
  - QM's "Open Acceleration Stack" (Mar 2026) lets third-party GPUs, CPUs, FPGAs and ASICs run inside the control loop via OPNIC and NVQLink, with AMD and Riverlane as partners. The licence is not stated.
  - ZI's ZQCS and LabOne Q offer pulse-, gate- and workflow-level interfaces. Per ZI, LabOne Q "provides automation for calibration and tune-up" [from team notes; ZI release 9 Mar 2026](https://www.zhinst.com/de/news/zurich-instruments-launches-zqcs-quantum-control-system-master-long-lived-logical-qubit/).
  - Qblox calls its Cluster "open-architecture".
  - NVQLink is an "open system architecture" with no published spec; access is by sign-up.
  - Sources: [QCR, 16 Mar 2026](https://quantumcomputingreport.com/quantum-machines-introduces-open-acceleration-stack-for-hybrid-computing/); [TQI, 9 Mar 2026](https://thequantuminsider.com/2026/03/09/zurich-instruments-zqcs-quantum-control-system-logical-qubits/); [NVIDIA](https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Introduces-NVQLink--Connecting-Quantum-and-GPU-Computing-for-17-Quantum-Builders-and-Nine-Scientific-Labs/default.aspx)
- Who has captured value so far:
  - Processor makers: Google keeps its RL-QEC in-house. IQM patents auto-calibration and treats control vendors as competitors. IQM's on-premises model gives customers "full control and data sovereignty" (424B3).
  - Model and compute suppliers: NVIDIA's models are free and tie into CUDA-Q, NVQLink and DGX.
  - Users: BAQIS built its own agent.
  - Control vendors: they capture the hardware sale (one-off) and position their software as free or open.
  - Q-CTRL is the only pure calibration/control-software vendor with a large fresh raise (US$290m, Nov 2026). Its press release leads on "AI for quantum" software and quantum navigation, and it discloses no calibration revenue. — [Q-CTRL, 12 Nov 2026](https://q-ctrl.com/blog/q-ctrl-secures-us-290-million-series-c-funding-led-by-salesforce-ventures-to-accelerate-the-convergence-of-quantum-and-ai)

#### 3.6 Export controls (test e background)
- US BIS interim final rule, published and effective 6 Sep 2024 (89 FR, No. 173), compliance for some A:1 destinations delayed to 5 Nov 2024 — [govinfo FR 2024-19633](https://www.govinfo.gov/content/pkg/FR-2024-09-06/html/2024-19633.htm). New quantum entries:
  - 4A906: quantum computers, controlled by number of working physical qubits (BIS cites ≥34) and C-NOT error rates. 4A906.c covers "quantum control components and quantum measurement devices specially designed" for those computers.
  - 3A901.a: cryogenic CMOS ICs designed for ≤4.5 K. 3A901.b: parametric (quantum-limited) amplifiers including TWPAs.
  - 3A904: cryogenic cooling systems (≥600 µW at ≤0.1 K).
  - 3B904: cryogenic wafer probers.
  - 3C907-909: isotopically enriched Si/Ge.
  - 4D906 and 4E906: software and technology.
- Licensing under that rule:
  - Worldwide national-security and regional-stability licence requirement.
  - Review policy: presumption of approval for A:1/A:5/A:6, presumption of denial for D:1/D:5, case by case otherwise. China is listed in EAR Country Groups D:1/D:5; I did not re-check that listing this session.
  - Licence Exception IEC for countries that have implemented equivalent controls.
  - Deemed-export general licence for D:1/D:5 nationals (General Order No. 6), with reporting duties.
  - Rationale: BIS harmonises with "like-minded" partners because quantum is not yet on a multilateral list.
- EU/Finland: IQM cites EU Reg. 2021/821 and the Finnish Act on Export Control of Dual-Use Items (500/2024), and states "EU member states and the United States have adopted targeted controls on certain types of quantum technologies". — [IQM 424B3](https://www.sec.gov/Archives/edgar/data/2113060/000119312526259957/d900375d424b3.htm)
- US Executive Orders 14412 and 14413 (22 Jun 2026):
  - PQC migration deadlines.
  - The QC-ADDS initiative (at least one system at a DOE facility).
  - A Commerce analysis of QIST supply chains, with "advance market commitments and prize challenges" for domestic critical quantum-enabling components.
  - Expanded FBI counterintelligence protection (QCPT).
  - No export-control provisions.
  - [QCR, 22 Jun 2026](https://quantumcomputingreport.com/president-trump-signs-two-executive-orders-on-quantum-technology/)
- Supply-chain localisation by vendors: Qblox began US manufacturing (with Prodrive, Canton MA) to "align with federal procurement standards" and DOE/national-lab funding requirements (17 Mar 2026). QM opened R&D in Illinois (4 Feb 2026). — [QCR](https://quantumcomputingreport.com/qblox-launches-u-s-manufacturing-for-quantum-control-systems/); [QCR headline](https://quantumcomputingreport.com/quantum-machines-to-establish-rd-hub-at-illinois-quantum-and-microelectronics-park/)
- UK, EU-level (Annex I) updates, Japan (METI), Israel's regime and US Entity List additions of Chinese quantum firms since 2024: could not verify in this session.

#### 3.7 Funding cycle and dependence on government budgets (2026)
- Government money in 2026:
  - US Commerce CHIPS letters of intent, US$2.013bn across nine quantum hardware and foundry firms for minority equity stakes (21 May 2026): IBM/Anderon US$1bn, GlobalFoundries US$375m, and US$100m each (or "up to") for Atom, D-Wave, Infleqtion, PsiQuantum, Quantinuum and Rigetti, with Diraq up to US$38m. No control vendor is included. — [QCR](https://quantumcomputingreport.com/u-s-department-of-commerce-proposes-2-billion-chips-investment-across-nine-quantum-hardware-and-foundry-developers/)
  - UK £2bn (17 Mar 2026); DOE Genesis Mission US$293.76m, including "AI to accelerate quantum advantage" (18 Mar 2026); France +€1bn (22 May 2026); Canada "$900M" defence industrial strategy with a quantum focus (21 Mar 2026; currency as reported); Singapore RIE2030 S$37bn (14 Feb 2026); DARPA QBI expansion (11 Mar 2026); NQI reauthorisation advancing (Senate Commerce, 19 Apr 2026). [secondary report: QCR headlines] — [QCR archive](https://quantumcomputingreport.com/news-archive-2026/)
  - Japan ¥33.5bn FY2025 supplementary budget — [JETRO](https://www.jetro.go.jp/biz/areareports/special/2026/0301/7f28e3ff9e1e15b0.html)
- Private and listed money: see 1.6. GQI's Q3 2026 view is "consolidation and capital concentration" and a "double down or exit" posture for investors. — [GQI](https://quantumcomputingreport.com/gqi-q3-2026-state-of-play-investment-consolidation-accelerating-q-day-horizons-and-the-shift-to-second-generation-architectures/)
- Customer concentration in government: IQM's FY2025 revenue came from Finland, Italy, Germany, the Czech Republic and Taiwan, largely supercomputing and research centres. Four customers made up 75%. — [IQM 424B3](https://www.sec.gov/Archives/edgar/data/2113060/000119312526259957/d900375d424b3.htm)

### Inferences
- [inference] Control hardware is a position that lasts only while processor makers lack the scale to build in-house. Once they scale they integrate it: IQM, Google, IBM and SDT already have, and Rigetti routes it through a contract manufacturer. The vendors' durable customers are national labs, testbeds (AIST, IQCC, Fermilab, NQCC) and small or new processor makers. Real-time QEC latency (sub-µs to <4 µs loops) is a genuine physical constraint, which favours whoever owns the FPGA/pulse-processor next to the qubits.
- [inference] Calibration software as a stand-alone product is being squeezed from three sides: open frameworks given away by hardware vendors (QUAlibrate), open models given away by NVIDIA, and general agent harnesses (Claude Code, MHS, MCP). The defensible piece is (a) tacit-knowledge "Skills" and quality gates and (b) proprietary calibration data from many devices. NVIDIA is collecting (b) through partner contributions.
- [inference] A financing-led pause around 2028 would hit control vendors through their customers: venture-funded and SPAC-funded processor makers. Two examples: IQM's stated runway reaches only into Q2 2028, and most 2026 listings are SPACs. Government-funded labs and testbeds would cushion it. National budgets were rising in 2026 in the US, UK, France, Japan, Canada and Singapore.

### Gaps
- No data on controller unit volumes, average selling prices or the share of published experiments by controller brand.
- No primary text of the UK, EU 2025 or Japanese quantum export controls, and no Entity List updates (search budget).

---

## 4. Leading companies (tests a-e, transitions T1-T5)

### 4.1 Quantum Machines (QM)
- Identity: Israel (Tel Aviv); private. Founded 2018 per PitchBook. ~300 employees plus ~100 openings (May 2026) — [Calcalist, 5 May 2026](https://www.calcalistech.com/ctechnews/article/bkzobwd0bx). PitchBook lists 344 — [PitchBook](https://pitchbook.com/profiles/company/234705-70).
- Funding, valuation and route to exposure:
  - US$170m Series C (25 Feb 2025) led by PSG Equity with Intel Capital (its first quantum investment), Red Dot Capital Partners and existing investors; total raised US$280m. — [TQI, 25 Feb 2025](https://thequantuminsider.com/2025/02/25/quantum-machines-raises-170-million-as-its-customer-base-exceeds-50-of-companies-developing-quantum-computers/)
  - Globes, citing unnamed sources: ~US$520m pre-money and ~US$670m post-money, with US$20m of the round a secondary sale by founders and employees. — [Globes, 25 Feb 2025](https://en.globes.co.il/en/article-1001502993) [secondary report]
  - Forge lists US$664.68m; aggregators show ~US$700m marks [aggregator estimates].
  - No 2026 round, IPO or SPAC found.
  - Route to exposure: none listed. The investor Intel is listed, but QM is immaterial to it.
- Theme share [inference]: ~100%. QM is pure-play control hardware plus orchestration and calibration software. In 2026 it acquired QHarbor (TU Delft data-management/visualisation platform; Delft office; 5 May 2026) and PCB Design Ltd (Budapest; ~40 engineers; 17 Jun 2026). — [TQI, 5 May 2026](https://thequantuminsider.com/2026/05/05/quantum-machines-acquires-qharbor/); [QCR, 17 Jun 2026](https://quantumcomputingreport.com/quantum-machines-establishes-budapest-rd-hub-through-acquisition-of-pcb-design-ltd/)
- Test a (position):
  - QM sits on the measurement path: its controllers generate the pulses and digitise readout, so they produce the raw data any calibration agent judges against. It also operates a national testbed (IQCC).
  - QM's calibration graph is open (QUAlibrate, BSD-3). Its Open Acceleration Stack invites third-party processors into the loop (NVIDIA, AMD, Riverlane).
  - The interfaces are open enough that QM captures value mainly through hardware.
  - The gap risk is that processor makers build their own controllers (IQM lists QM as a competitor) and that on-chip/cryo control reduces room-temperature content.
- Test b (outside evidence of lead):
  - The joint release with Rigetti (Dec 2024) and the May 2026 Novera result: OPX1000 replaced Rigetti's native stack and matched "the peak internal calibration metrics recorded by the hardware manufacturer" (median 2Q 99.5%).
  - Selected by HPE as one of two control-infrastructure partners (Jun 2026).
  - One of five NVQLink control builders (Oct 2025).
  - Its controllers sit at IQCC, which is used by third parties (Quantum X Labs, Qruise).
  - QUAlibrate early users include OQC, Qolab, Quantum Elements, Academia Sinica and Diraq.
  - The "majority"/"more than half of the world's quantum computing developers" usage claim is a [company claim, not independently confirmed]. No independent share data was found.
  - Sources: [QCR, 29 May 2026](https://quantumcomputingreport.com/quantum-machines-achieves-99-5-two-qubit-gate-fidelity-operating-rigettis-novera-qpu/); [QCR, 15 Jun 2026](https://quantumcomputingreport.com/hewlett-packard-enterprise-hpe-signals-hybrid-quantum-push-with-eight-partner-infrastructure-initiative/); [QCR, 9 Jun 2026](https://quantumcomputingreport.com/quantum-x-labs-partners-with-iqcc-to-evaluate-ai-based-transformer-decoders/)
- Test c (revenue model): not disclosed. [inference] Mostly one-off controller hardware plus support. The software (QUAlibrate) is free. QHarbor adds a data/software layer. Supply deal for Qubic cryo-amplifiers (May 2026), a component resale/integration line.
- Test d (financial facts): only the Feb 2025 raise (~US$150m primary if the Globes secondary figure is right) and headcount growth. No revenue, cash or runway disclosed: could not verify.
- Test e (resilience):
  - Customers are venture-funded processor makers and government labs, so QM is sensitive to a 2028 financing pause through its customers [inference].
  - Under the US rule, "quantum control components ... specially designed" for 4A906 computers are 4A906.c items. [inference] US-rule reach over an Israeli-made controller depends on US-origin content, which was not checked. Israeli export rules for QM could not be verified, so China access is unclear but likely restricted.
  - US footprint via the Illinois R&D hub (Feb 2026); operations in the US, Germany, France, Denmark, Japan, Singapore and the Netherlands (Calcalist).
- Transitions:
  - T1 (agent-run set-up). Said: QUAlibrate cuts calibration "from hours to minutes" (May 2025); the Open Acceleration Stack is "AI-native" (Mar 2026). Done: QUAlibrate shipped; AI calibration challenge (Dec 2024); Qruise bring-up proof of concept at ~15 min (May 2026); Novera tuned in "ten days" (not agent-run). Funded: Series C; two acquisitions. Timing: no agent product announced. Must go right: the agent layer (NVIDIA, Qruise, Q-CTRL, general LLM harnesses) has to keep running on QM hardware rather than routing around it.
  - T2 (open interfaces). Done: QUAlibrate open-sourced; NVQLink support; OPNIC/Open Acceleration Stack. QUA remains proprietary.
  - T3 (to software/subscription): no evidence of subscription revenue. QHarbor is the only software-business step.
  - T4 (cheaper hardware, heavier compute): DGX Quantum and the Open Acceleration Stack move compute next to the controller. The threats are QICK (now sold by Qblox) and cryo/on-chip control.
  - T5 (data): the QHarbor acquisition puts QM in experiment-data management. Data ownership terms were not found.
- Unverified claims: the share-of-developers claim; the valuation (unconfirmed by the company).

### 4.2 Q-CTRL
- Identity: Australia (Sydney); private. Product lines: Boulder Opal (control/calibration; "Scale Up"), Fire Opal (performance software, including via IBM Quantum Functions), Black Opal (education) and Ironstone Opal (quantum navigation, RTCA DO-160 qualified, Nov 2026).
- Funding, valuation and route to exposure:
  - Series C US$290m (A$415m), 12 Nov 2026, led by Salesforce Ventures with Bullhound Capital and Affinity Partners.
  - New investors: AMD Ventures, EDGE Group, MPower Partners, Australia's National Reconstruction Fund Corporation and SPARX Asset Management. Returning: Alpha Edison, Alumni Ventures, DCVC, In-Q-Tel, Lockheed Martin Ventures, Main Sequence, Ridgeline, Salus and Square Peg.
  - Valuation undisclosed; "mints the newest quantum-sector unicorn" [company claim]. — [Q-CTRL, 12 Nov 2026](https://q-ctrl.com/blog/q-ctrl-secures-us-290-million-series-c-funding-led-by-salesforce-ventures-to-accelerate-the-convergence-of-quantum-and-ai)
  - Prior: Series B expanded to US$113m (Oct 2024; B-2 led by GP Bullhound) — [TQI, 8 Oct 2024](https://thequantuminsider.com/2024/10/08/q-ctrl-sets-global-quantum-technology-fundraising-record-increasing-series-b-to-usd-113m-led-by-gp-bullhound/)
  - Route to exposure: none; private, no listing announced. The corporate investors (Salesforce, Lockheed, AMD) are listed, but Q-CTRL is immaterial to them.
- Theme share [inference]: high but not total. Calibration/autonomy (Boulder Opal) is one of two growth pillars. The Series C use of funds names "AI-driven software" and quantum-navigation deployment, and navigation features prominently.
- Test a (position):
  - Q-CTRL owns no judge (no instrument or installed base of its own). It runs on others' controllers ("FPGA-based controllers"; no vendor named) and others' QPUs (QuantWare, Equal1, Anyon).
  - It depends on open interfaces and processor makers choosing to buy. It is exposed to free substitutes: Ising, QUAlibrate, in-house tools.
  - Its counter is integrating Ising into Boulder Opal and fine-tuning on customer hardware (planned).
- Test b:
  - Customers and partners named by others: Rigetti lists Q-CTRL as a software customer (10-K); IBM hosts Fire Opal as a Quantum Function; IonQ integrated Fire Opal (Apr 2026); NVIDIA lists Q-CTRL as an Ising adopter. QuantWare, Equal1 and Anyon partnerships are announced by Q-CTRL and partners.
  - No independent benchmark of Boulder Opal versus alternatives.
  - Its 2Q median of 96% on QuantWare (Nov 2026) is below the 99.5% median QM reported on Novera (different devices, so not comparable) [company claims].
  - The Oct 2024 investor list (Lockheed Martin Ventures, NTT Finance) and the 2026 list (In-Q-Tel, EDGE, Lockheed) indicate defence-sector interest.
- Test c: software and subscriptions, plus navigation systems. No revenue disclosed. Last company-disclosed figure: ">$15M in bookings across quantum computing and quantum sensing divisions in 2022" — [Q-CTRL, 31 Jan 2023](https://q-ctrl.com/blog/q-ctrl-announces-expansion-of-industry-leading-series-b-for-quantum-infrastructure-software). The Latka 2024 revenue estimate of US$16.8m is unverified.
- Test d: a fresh US$290m (Nov 2026). Cash, burn and revenue not disclosed.
- Test e [inference]: well funded into a 2028 pause by the size of the fresh round, though burn is unknown. Australian, US and UK defence links (In-Q-Tel, Lockheed) bring both support and export-control exposure for navigation. Software exports for 4A906 computers fall under 4D906/4E906 categories if "specially designed" [inference from the BIS rule].
- Transitions:
  - T1. Said: "industry's first push-button solution for fully autonomous quantum computer bring-up, operation, and maintenance" (18 Sep 2026). Done: QuantWare cold-start results (Apr/Sep/Nov 2026); Equal1 and Anyon integrations. Funded: Series C. Timing: run-time recalibration "through late 2026". Must go right: fidelity at production level (2Q 96% median today); processor makers paying rather than building; staying ahead of free Ising-based agents.
  - T2: benefits from open controllers and NVQLink (claims 50x latency reduction).
  - T3: already software-first; no recurring-revenue disclosure.
  - T4: its core pitch is making hardware perform better through software, e.g., Fire Opal speed-ups on IBM Nighthawk (Nov 2026).
  - T5: plans an Ising Calibration VLM "trained on a customer's specific hardware" (Apr 2026). That raises the question of who owns customer calibration data; terms not disclosed.
- Unverified claims: unicorn valuation; "100 times better" navigation; 2x human fidelity.

### 4.3 Zurich Instruments (Rohde & Schwarz)
- Identity: Switzerland (Zurich); wholly owned by Rohde & Schwarz (private, family-owned, Munich) since June 2021. Leadership per Wikipedia: CEO Andrea Orzati. Wikipedia infobox shows 168 employees (date unclear; treat as unreliable). — [Wikipedia](https://en.wikipedia.org/wiki/Zurich_Instruments)
- Funding and exposure: none. R&S is unlisted. R&S group FY2025/26 (Jul 2025–Jun 2026) net revenue €3.6bn [from team notes; R&S release 27 Oct 2026](https://www.rohde-schwarz.com/jp/_229356-1706630.html). ZI and quantum figures are not disclosed (could not verify).
- Theme share: ZI also sells lock-in amplifiers and impedance analysers. Quantum is a part of ZI and a very small part of R&S [inference].
- Test a:
  - Owns the control hardware (HDAWG, SHFQC+, QCCS, ZQCS) and the LabOne Q software layer (automation for "calibration and tune-up").
  - ZQCS is aimed at QEC-scale systems: >1,000 channels per rack, FPGA and GPU links, water cooling.
  - Interfaces: pulse, gate and workflow level.
  - NVQLink control builder.
- Test b:
  - Joint real-time QEC demonstrator with IQM, which otherwise claims in-house control (Mar 2026).
  - Named partners per team notes: Photonic Inc., QuantrolOx integration, Australia's National Quantum Computing Testbed.
  - ZQCS has no named customer ("being deployed to power error-correction experiments").
  - Showcased SHFQC and ZQCS "from a single qubit to 1000 qubits" at electronica (10–13 Nov 2026) — [R&S, electronica 2026](https://www.rohde-schwarz.com/us/about-us/news-press/all-news/rohde-schwarz-at-electronica-2026-from-everyday-bench-work-to-extraordinary-test-applications_229356-1706630.html)
- Test c: hardware-led [inference]; no disclosure.
- Test d: inside a €3.6bn-revenue private group; ZI-level figures not available.
- Test e: R&S's defence and critical-infrastructure weight cushions an AI-capex pause [from team notes]. ZI's quantum exports fall under 4A906.c-type controls (EU/Swiss equivalents not verified). It has a Shanghai subsidiary (Wikipedia); its current China quantum sales are unknown.
- Transitions:
  - T1: automation in LabOne Q (classical, not agentic). No AI-agent product found. Must go right: become the default hardware under agents (NVQLink/Ising pairing).
  - T2: open interfaces (LabOne Q; licence not verified this session).
  - T3: no evidence.
  - T4: direct-RF ZQCS with GPU links.
  - T5: no evidence.

### 4.4 Qblox
- Identity: Netherlands (Delft); private; CEO Niels Bultink. Sells the Cluster open-architecture control stack. US manufacturing with Prodrive (Canton MA) from 1 Apr 2026.
- Funding, valuation and route to exposure:
  - US$26m Series A (2024) led by Quantonation and Invest-NL with QDNL Participations and the EIC, described as its first external equity — [Quantum Security Defence (secondary)](https://quantumsecuritydefence.com/quantum-news/qblox-funding/)
  - PitchBook lists a Sept 2025 debt deal (amount undisclosed) — [PitchBook](https://pitchbook.com/profiles/company/439353-64)
  - Valuation not disclosed. Route to exposure: none.
- Theme share: ~100% [inference].
- Test a: owns controller hardware. It has taken the open RFSoC threat in-house: it is now the licensed US manufacturer and distributor of QICK, with DOE/Fermilab training programmes. Its Cluster is "open-architecture".
- Test b:
  - Government selection by DOE/Fermilab (CRADA plus licence, Jun 2026).
  - HPE control partner (Jun 2026); NVQLink control builder.
  - QuantrolOx automation demo on Qblox hardware (Jan 2025); Institut quantique joined the Qblox Excellence Center (Mar 2026).
  - Listed peer SEEQC names it among the four off-the-shelf vendors.
- Test c: hardware; training programmes planned. Founder says growth was revenue-funded [secondary report]. No revenue disclosed.
- Test d: small equity base (US$26m Series A); revenue-funded claim unverified.
- Test e: the US plant reduces US procurement and export friction. Exposure to DOE/national-lab budgets is high [inference].
- Transitions:
  - T1: hardware partner for third-party automation (QuantrolOx). No own agent product found.
  - T2: strongest open-hardware stance (QICK).
  - T3: no evidence.
  - T4: QICK puts Qblox on both sides of cheap RFSoC hardware.
  - T5: no evidence.

### 4.5 Keysight (quantum control business)
- Identity: US; NYSE KEYS. Group FY2025 (to 31 Oct 2025) revenue US$5,375m; software and services ~37% of revenue and ARR 29% (group level) [from team notes; Keysight 2025 Annual Report and Q4 FY2025 remarks](https://s22.q4cdn.com/444849635/files/doc_financials/2025/ar/2025-Annual-Report.pdf). Quantum revenue not disclosed; it is immaterial to the group [inference].
- Test a: sells QCS hardware at the largest commercial scale reported (AIST >1,000 qubits). No agent or AI calibration capability was found on its quantum product page, which shows the Q5401A 2- and 5-qubit system with API and GUI. — [Keysight QCS page](https://www.keysight.com/us/en/products/modular/pxi-products/quantum-control-system.html)
- Test b: AIST G-QuAT (Jul 2025; JETRO calls it "world's largest commercial" control system); Fujitsu/RIKEN 256-qubit machine (May 2025) [secondary report]; NVQLink control builder. A five-year Singapore research agreement covering Keysight QCS appeared only in a search-result summary; the source URL was not kept, so treat it as unverified.
- Test c: hardware sale for quantum. Group-level recurring share as above.
- Test e: AI-capex exposure is group-level (team notes). The Japan quantum business is tied to Japanese government programmes (G-QuAT).
- Transitions:
  - T1: none found for quantum. The group's MCP instrument server is not quantum-specific.
  - T2: group MCP server works with any MCP client [from team notes].
  - T3: group-level only.
  - T4: large-channel-count systems.
  - T5: none found.

### 4.6 IQM
- Identity: Finland (Espoo), with major operations in Munich; full-stack superconducting QC maker; >400 employees. Listed on Nasdaq as ADSs (IQMX) from 2 Jul 2026 via a SPAC merger with RAAQ; Finnish prospectus approved 1 Jul 2026 for a Nasdaq Helsinki dual listing. — [IQM 6-K, 4 Aug 2026](https://www.sec.gov/Archives/edgar/data/2113060/000119312526331538/iqmx-ex99_1.htm); [DCD](https://www.datacenterdynamics.com/en/news/iqm-completes-spac-merger-with-raaq-begins-trading-on-nasdaq/)
- Funding and route to exposure:
  - SPAC announced 23 Feb 2026 at a US$1.8bn initial equity valuation — [CNBC, 23 Feb 2026](https://www.cnbc.com/2026/02/23/finlands-iqm-listing-quantum-computing.html)
  - PIPE upsized to US$146m with Ilmarinen (2 Jun 2026) — [QCR headline](https://quantumcomputingreport.com/iqm-upsizes-spac-merger-pipe-financing-to-146-million-with-capital-commitment-from-pension-insurer-ilmarinen/)
  - US$320m Series B (Sep 2025) at US$1bn led by Ten Eleven Ventures (CNBC)
  - Kreos €50m loan facility (23 Dec 2025) — [Exhibit 10.20](https://www.sec.gov/Archives/edgar/data/2113060/000119312526255796/d900375dex1020.htm)
  - Exposure is direct (IQMX).
- Theme share: control and calibration are internal capabilities, not products sold separately [inference from the revenue split below].
- Test a:
  - Owns the judge for its own systems (QPU plus installed base: 26 sold, 17 delivered).
  - Claims in-house control electronics and auto-calibration IP.
  - Treats control vendors as competitors, yet partners with ZI for QEC.
  - On-prem model: customers keep "full control and data sovereignty".
- Test b:
  - Customers include CINECA (Radiance 54 live, Jun 2026), Oak Ridge National Laboratory (first US delivery, Jun 2026), CSC/LUMI AI Factory, a Japanese enterprise (Apr 2026) and Deutsche Bahn (use case).
  - FY2025: four customers ≥10% of revenue.
  - Calibration claims (Ising) are company-only.
  - Sources: [IQM 6-K](https://www.sec.gov/Archives/edgar/data/2113060/000119312526331538/iqmx-ex99_1.htm); [QCR, 11 Jun 2026](https://quantumcomputingreport.com/iqm-radiance-54-superconducting-quantum-computer-goes-live-at-cineca-in-italy/)
- Test c: FY2025 revenue €31.333m (2024: €16.436m), of which —
  - on-prem system sales €30.588m (97.6%)
  - professional services €0.112m
  - co-development €0.349m
  - cloud €0.284m (0.9%)
  - Revenue recognised over time was 56%. Remaining performance obligations: €33.0m within one year plus €34.3m later. — [IQM 424B3](https://www.sec.gov/Archives/edgar/data/2113060/000119312526259957/d900375d424b3.htm)
- Test d (H1 2026, to 30 Jun):
  - Revenue €8.9m; operating loss €60.5m; operating cash flow −€50.0m.
  - Cash €113.4m at 30 Jun and €309.4m at 2 Jul including listing proceeds. The CFO states runway "well into the second quarter of 2028".
  - Backlog €69.1m (30 Jun), >€102.1m at 3 Aug.
  - FY2026 guidance: revenue €42–47m; order intake €65–75m.
  - >€40m fab expansion to 30 systems/year.
  - Source: [IQM 6-K](https://www.sec.gov/Archives/edgar/data/2113060/000119312526331538/iqmx-ex99_1.htm)
- Test e:
  - Runway ends inside the 2028 pause window [fact plus inference].
  - Government and supercomputer-centre customers dominate.
  - EU/Finnish dual-use controls apply.
  - Its competitor list includes Chinese firms (Origin, Huawei, Alibaba, Baidu).
- Transitions:
  - T1. Said: agentic calibration (Apr 2026). Done: 20-qubit Ising run (Oct 2026). Funded: listing cash. Timing: "larger chips next". Must go right: agentic calibration raising uptime on delivered systems.
  - T2: "open and modular software architecture" (prospectus) plus NVQLink; IQM still treats control vendors as competitors.
  - T3: 0.9% cloud; HPC integration service launched May 2026 (QCR headline).
  - T4: HPC/AI-factory integration (HPE Cray, LUMI, NVIDIA).
  - T5: customer data sovereignty is part of the pitch.

### 4.7 NVIDIA (quantum effort)
- Identity: US; Nasdaq NVDA. Quantum revenue not disclosed; immaterial [inference].
- Effort:
  - CUDA-Q; DGX Quantum (with QM); NVQLink (Oct 2025; RDMA over Ethernet; <4 µs end-to-end latency in the IQM/ZI demonstrator).
  - Ising Calibration 1 (35B, Qwen3.5-35B-A3B base; Apr 2026) and 1.5 (31B; Jul 2026; OpenMDW licence); Ising Decoding (0.9M and 1.8M-parameter 3D CNNs; claimed 2.5x faster and 3x more accurate than PyMatching); QCalEval; the Quantum Calibration Agent Blueprint.
  - Investments: NVentures in Alice & Bob (May 2026, QCR headline). Others not verified in this session.
  - Sources: [NVIDIA, 14 Apr 2026](https://nvidianews.nvidia.com/news/nvidia-launches-ising-the-worlds-first-open-ai-models-to-accelerate-the-path-to-useful-quantum-computers); [QCR, 16 Mar 2026](https://quantumcomputingreport.com/iqm-and-zurich-instruments-develop-real-time-qec-via-nvidia-nvqlink/)
- Test a: owns no quantum judge. It owns the compute and interconnect constraint (low-latency GPU coupling) and the open model layer. It gives the models away and aggregates partner calibration data [inference: monetisation via GPUs, DGX and NVQLink systems].
- Test b:
  - 12 named calibration adopters and 12 decoding users (Apr 2026).
  - Cited by independent academic work: BAQIS references Ising and the Blueprint. Its benchmark is self-built.
  - 17 QPU builders and 5 control builders on NVQLink.
- Test c: software free; hardware monetised [inference].
- Test e: AI-cycle exposure is group-level. NVIDIA's China sales are restricted by separate US chip rules (not checked here).
- Transitions:
  - T1: Ising plus Blueprint shipped (done).
  - T2: open weights, open benchmark, "open" NVQLink.
  - T3: n/a.
  - T4: central (GPU decoders, AI calibration).
  - T5: collects partner data across modalities for training (done, per NVIDIA).

### 4.8 Others assessed briefly
- Qruise (Germany; private): QruiseOS. IQCC 21-qubit bring-up in ~15 min with QM (May 2026); NV-centre bring-up with Goethe University Frankfurt (May 2026); took part in the Dec 2024 challenge. Funding per aggregators: grants (Innovate UK, Apr 2025), total US$2.65–4.92m (conflicting; CB Insights/Caplight) [aggregator, low reliability]. No independent benchmark.
- QuantrolOx (UK; private): Quantum EDGE; integrations with Qblox, ZI, UC Berkeley, Naples, RAQS (APAC), MAHE (India) and AQSolotl. Funding: could not verify.
- Riverlane (UK; private): QEC stack (see 1.2). 2026 funding: could not verify.
- Quantum Elements (US): AI/digital-twin platform; SAFE funding (Feb 2026); Rigetti digital-twin exploration (Apr 2026).
- Conductor Quantum (US): CODA MCP; Ising adopter.
- SEEQC (US; SEQC): on-chip SFQ control. FY2025 revenue US$4.157m. US$1bn SPAC valuation with US$65m PIPE (Jan 2026). Taiwan manufacturing ecosystem. Ising Decoding user.
- QuEL (Japan; private): QuEL-1 SE; Moonshot Phase 2 projects (2026–2030); RIKEN 144-qubit controller (Nikkei, secondary). Funding: could not verify.
- SDT (Korea): in-house QCU (8.5 GHz); 20-qubit Kreo; NVQLink data centre; plans 64 qubits in 2026 and photonic integrated circuits in 2027 [company claim]. Listing and funding: could not verify.
- Origin Quantum (China; private; IPO status could not be verified): Wukong-180; Sīnán OS automated calibration; Origin Pilot open-sourced; claims full-stack independence. In IQM's competitor list.
- SpinQ (China; private): Series C plus D, RMB 2bn in six months (2026); in-house control plane.
- CIQTEK (China; SSE STAR 688828): quantum measurement and spin instruments plus an "ION I" trapped-ion computer; 9M 2026 revenue RMB 404m [from team notes; broker note].
- QpiAI (India): Kaveri 64-qubit with hardware decoder; DST and NQM backing. Funding and control sourcing: could not verify.
- Israel cluster: Quantum Art (US$140m Series A, Apr 2026), Q-Factor (US$24m seed), Qedma, Quantum X Labs/Viewbix, QTREX, Classiq (Intel acquisition reported by GQI). These are processor or software firms, not control vendors.

---

## 5. Companies considered and left out, with reasons
- IBM, Google Quantum AI, Quantinuum, IonQ, Rigetti, Alice & Bob, Pasqal, OQC, Infleqtion, Xanadu, Horizon Quantum, Atom Computing, QuEra: processor makers whose control and calibration are internal capabilities, not a sold product. They are used as evidence for "in-house vs buy" (section 3.1), not ranked.
- Classiq, Qedma, Phasecraft, Algorithmiq, Haiqu, Zapata: algorithm, compiler and error-mitigation software rather than instrument control and calibration.
- Bluefors, Maybell and other cryogenic suppliers; Qubic (cryo-amplifiers): physical-component suppliers, outside the control/calibration agent thesis. Mentioned only where they touch controllers (QM–Qubic supply agreement).
- Fujitsu and RIKEN: users and integrators of Keysight/QuEL control; no calibration-product evidence found.
- QuantumCTek 国盾量子 and ZWDX 中微达信: could not verify their control-electronics businesses, so they are not assessed.
- Anthropic (MHS) and Moonshot/Alibaba Qwen/DeepSeek (models used by BAQIS): general AI suppliers. They are recorded as agent-layer competitors to vendor software, not as segment companies.

---

## 6. Where the evidence contradicts the thesis
- The judge is not always unambiguous.
  - In QEC, opposite coherent errors can produce identical passive syndrome statistics, so an agent that tunes only against the instrument's own syndrome reading can be misled. A manipulated adviser can push harmful updates. Safeguards need known calibration states and an independent evaluator. — [arXiv 2609.19090, 16 Sep 2026](https://arxiv.org/abs/2609.19090)
  - In the BAQIS run, the agent passed all its quality gates while choosing a worse operating point: median T2R 7.9 µs vs 14.4 µs for the expert. The gate was satisfied but performance was lower. — [arXiv 2606.22376](https://arxiv.org/pdf/2606.22376)
- Agent-run set-up is not yet doing the hard part at scale.
  - BAQIS automated only single-qubit steps.
  - IQM published no timing or fidelity.
  - Q-CTRL's autonomous 2Q median is 96%.
  - QM's best-in-class 99.5% 2Q on Novera took "ten days" with QUAlibrate, and no AI is mentioned.
  - The most powerful in-operation calibration (Google RL) needed the processor maker's proprietary stack.
- Closed interfaces are not the main obstacle.
  - Most control interfaces are already open or being opened: QUAlibrate (BSD-3), QuarkStudio, QICK, the "open" NVQLink, LabOne Q's workflow interfaces, the Open Acceleration Stack.
  - The obstacles cited by the primary sources are tacit knowledge and quality gates (BAQIS), latency (NVQLink, QEC loops), drift speed (Google) and trust/safety (2609.19090).
- The hardware-damage obstacle looks smaller here than for electron microscopes or accelerators. The only safety mechanism found was "hardware-safe qubit groups" and parameter gates (BAQIS) [inference: superconducting control pulses are low power; the main costs of errors are miscalibration and lost uptime].
- Value is not accruing to the instrument (controller) maker.
  - Google captured in-operation calibration in-house.
  - IQM claims control and calibration as its own IP and lists control vendors as competitors.
  - NVIDIA gives calibration models away.
  - BAQIS used a general agent plus an open model.
  - QM gives its calibration framework away.
  - The only richly funded calibration-software company (Q-CTRL) owns no instrument, and its raise leans heavily on navigation.
- Physical integration may remove the room-temperature controller altogether: SEEQC SFQ at 10 mK, D-Wave and EeroQ on-chip/CMOS control, cryo-CMOS startups. That would undercut "the instrument maker owns the judge" for control-electronics vendors.

---

## 7. What could not be verified
- QM: revenue, cash, runway, current valuation (only Globes' unnamed-source figure), the share-of-developers claim, export-licensing regime.
- Q-CTRL: valuation (only the company's "unicorn" claim), revenue/ARR since 2022 bookings, Boulder Opal pricing and customer count.
- Zurich Instruments: revenue, quantum share, employees (Wikipedia figure undated), LabOne Q licence terms.
- Qblox: revenue, valuation, whether the QICK licence is exclusive, the Mar 2026 "open-architecture quantum computer" launch (aggregator only).
- Keysight: quantum revenue; the Fujitsu/RIKEN BusinessWire release (403 on fetch).
- IQM: which control electronics ship in current commercial systems. The prospectus claims in-house; the ZI partnership exists.
- IQM 20-qubit Ising run: timing, fidelities, human comparison.
- Google: the Nature page itself and any Google blog post.
- 2606.22376: maker of the DDS control electronics.
- China: QuantumCTek's control-system revenue and Entity List status, ZWDX, Origin Quantum's IPO/tutoring filing and its 本源天机 control product versions. Baidu Baike and Wikipedia fetches failed (empty or 404); the search budget was exhausted.
- Export controls: UK, EU-level 2025 Annex I update, Japan METI rules, Israel; Entity List additions since 2024; any BIS quantum amendments after Sept 2024. An EUR-Lex fetch returned empty.
- SDT, QuEL, QpiAI, Riverlane, QuantrolOx, QuamCore funding and listing status.
- Share of published experiments by controller brand. Independent national-lab benchmarks of controllers or calibration agents: none found.
- NVIDIA quantum investments beyond Alice & Bob (NVentures, May 2026).
- SEEQC SPAC completion date (424B3 1 Jul 2026 implies an effective registration; closing not confirmed).
- Intel–Classiq US$2.3bn acquisition (GQI summary only).

---

## 8. Sources with dates
Primary filings and papers:
- IQM 424B3 prospectus, 5 Jun 2026 — https://www.sec.gov/Archives/edgar/data/2113060/000119312526259957/d900375d424b3.htm
- IQM F-4/A Exhibit 10.20 (Kreos loan, dated 23 Dec 2025), filed 3 Jun 2026 — https://www.sec.gov/Archives/edgar/data/2113060/000119312526255796/d900375dex1020.htm
- IQM 6-K H1 2026 results, 4 Aug 2026 — https://www.sec.gov/Archives/edgar/data/2113060/000119312526331538/iqmx-ex99_1.htm
- SEEQC 424B3, 1 Jul 2026 — https://www.sec.gov/Archives/edgar/data/1779977/000121390026074258/ea0278139-08.htm
- Rigetti 10-K FY2025, 4 Mar 2026 — https://www.sec.gov/Archives/edgar/data/1838359/000110465926023454/rgti-20251231x10k.htm
- Gix Internet 6-K, 26 Oct 2026 — https://www.sec.gov/Archives/edgar/data/1782265/000149315226048578/form6-k.htm
- BIS interim final rule, Federal Register 6 Sep 2024 (FR Doc 2024-19633) — https://www.govinfo.gov/content/pkg/FR-2024-09-06/html/2024-19633.htm
- arXiv 2606.22376 (Vibe Calibration), 21 Jun 2026 — https://arxiv.org/abs/2606.22376 ; https://arxiv.org/pdf/2606.22376
- arXiv 2511.08493 (Sivak et al., RL control of QEC), v1 11 Nov 2025, v4 19 Jun 2026 — https://arxiv.org/abs/2511.08493
- arXiv 2604.25884 (QCalEval), 28 Apr 2026 — https://arxiv.org/abs/2604.25884
- arXiv 2603.08801 (LLM-assisted superconducting qubit experiments), 9 Mar 2026 — https://arxiv.org/abs/2603.08801
- arXiv 2609.19090 (AI advisers in QEC), 16 Sep 2026 — https://arxiv.org/abs/2609.19090
- APS Global Physics Summit 2026 abstracts — https://meetings-archive.aps.org/smt/2026/mar-z05/1/ ; https://meetings-archive.aps.org/smt/2026/mar-l07/14/
- Osaka University ResOU (QuEL-1 SE, RSI DOI 10.1063/5.0311173), 27 Mar 2026 — https://resou.osaka-u.ac.jp/ja/research/2026/20260327_1

Company releases and blogs:
- IQM blog, 21 Oct 2026 — https://iqm.tech/blog/what-happened-when-we-let-ai-calibrate-a-quantum-chip-using-nvidia-ising/
- NVIDIA Ising release, 14 Apr 2026 — https://nvidianews.nvidia.com/news/nvidia-launches-ising-the-worlds-first-open-ai-models-to-accelerate-the-path-to-useful-quantum-computers
- NVIDIA Ising 1.5 developer blog, 27 Jul 2026 — https://developer.nvidia.com/blog/nvidia-ising-enables-fully-automated-quantum-computer-calibration-with-enhanced-in-context-learning
- NVIDIA Ising solutions page (accessed 12 Nov 2026) — https://www.nvidia.com/en-us/solutions/quantum-computing/ising/
- NVIDIA NVQLink release, 28 Oct 2025 — https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Introduces-NVQLink--Connecting-Quantum-and-GPU-Computing-for-17-Quantum-Builders-and-Nine-Scientific-Labs/default.aspx
- Q-CTRL Series C release, 12 Nov 2026 — https://q-ctrl.com/blog/q-ctrl-secures-us-290-million-series-c-funding-led-by-salesforce-ventures-to-accelerate-the-convergence-of-quantum-and-ai
- Q-CTRL autonomous calibration blog, 18 Sep 2026 — https://q-ctrl.com/blog/making-quantum-computer-calibration-autonomous-informative-and-easy
- Q-CTRL Ising blog, 14 Apr 2026 — https://q-ctrl.com/blog/scaling-quantum-autonomy-with-nvidia-ising
- Q-CTRL Series B-1 release, 31 Jan 2023 — https://q-ctrl.com/blog/q-ctrl-announces-expansion-of-industry-leading-series-b-for-quantum-infrastructure-software
- Q-CTRL blog index (accessed 12 Nov 2026) — https://q-ctrl.com/blog
- Qblox QICK release, 24 Jun 2026 — https://qblox.com/newsroom/doe-fermilab-and-qblox-partner-to-commercialize-qick-platform-and-boost-quantum-workforce
- DOE (Fermilab–Qblox), Nov 2025 — https://www.energy.gov/technologycommercialization/articles/energy-department-announces-partnership-fermilab-and-qblox
- QM release (QM–Rigetti AI calibration), Dec 2024 — https://www.quantum-machines.co/press-release/quantum-machines-and-rigetti-announce-successful-ai-powered-calibration-of-a-quantum-computer/
- Rigetti IR (same), Dec 2024 — https://investors.rigetti.com/news-releases/news-release-details/quantum-machines-and-rigetti-announce-successful-ai-powered
- Anthropic MHS research preview, 27 Aug 2026 — https://www.anthropic.com/news/model-hardware-standard-research-preview
- Keysight QCS product page (accessed 12 Nov 2026) — https://www.keysight.com/us/en/products/modular/pxi-products/quantum-control-system.html
- R&S electronica 2026 release — https://www.rohde-schwarz.com/us/about-us/news-press/all-news/rohde-schwarz-at-electronica-2026-from-everyday-bench-work-to-extraordinary-test-applications_229356-1706630.html
- QuEL news (accessed 12 Nov 2026) — https://quel-inc.com/ja/category/news/

Government and agency pages:
- JETRO Japan quantum R&D report, 13 Mar 2026 — https://www.jetro.go.jp/biz/areareports/special/2026/0301/7f28e3ff9e1e15b0.html

Trade press and secondary sources (dates as given):
- The Quantum Insider: 25 Feb 2025 (QM Series C) https://thequantuminsider.com/2025/02/25/quantum-machines-raises-170-million-as-its-customer-base-exceeds-50-of-companies-developing-quantum-computers/ ; 19 May 2025 (QUAlibrate) https://thequantuminsider.com/2025/05/19/quantum-machines-launches-open-source-framework-that-cuts-quantum-computer-calibration-from-hours-to-minutes/ ; 10 Dec 2024 (calibration challenge) https://thequantuminsider.com/2024/12/10/ai-driven-quantum-calibration-achieved-in-rigetti-and-quantum-machines-challenge/ ; 22 Jan 2025 (QuantrolOx) https://thequantuminsider.com/2025/01/22/automated-2-qubit-gate-tuning-in-under-25-minutes-with-quantrolox-and-qblox-using-quantware-qpus/ ; 8 Oct 2024 (Q-CTRL B-2) https://thequantuminsider.com/2024/10/08/q-ctrl-sets-global-quantum-technology-fundraising-record-increasing-series-b-to-usd-113m-led-by-gp-bullhound/ ; 14 Apr 2026 (IQM agentic calibration) https://thequantuminsider.com/2026/04/14/iqm-ai-based-calibration-scalable-quantum-systems/ ; 10 Jul 2026 (Google RL) https://thequantuminsider.com/2026/07/10/google-study-shows-quantum-computer-can-learn-from-its-own-errors-while-it-computes/ ; 5 May 2026 (QHarbor) https://thequantuminsider.com/2026/05/05/quantum-machines-acquires-qharbor/ ; 9 Mar 2026 (ZQCS) https://thequantuminsider.com/2026/03/09/zurich-instruments-zqcs-quantum-control-system-logical-qubits/ ; 19 Nov 2025 (DOE/Fermilab/Qblox) https://thequantuminsider.com/2025/11/19/doe-fermilab-qblox-qick-us/
- Quantum Computing Report: 2026 news archive (Jan–Jun 2026) https://quantumcomputingreport.com/news-archive-2026/ ; homepage (late Oct–11 Nov 2026) https://quantumcomputingreport.com/ ; individual articles cited inline (dates in text)
- GQI Q3 2026 State of Play (via QCR), 27 Oct 2026 — https://quantumcomputingreport.com/gqi-q3-2026-state-of-play-investment-consolidation-accelerating-q-day-horizons-and-the-shift-to-second-generation-architectures/
- CNBC, 23 Feb 2026 (IQM SPAC) — https://www.cnbc.com/2026/02/23/finlands-iqm-listing-quantum-computing.html
- DCD (IQM listing) — https://www.datacenterdynamics.com/en/news/iqm-completes-spac-merger-with-raaq-begins-trading-on-nasdaq/
- BusinessWire, 14 May 2026 (IQM F-4) — https://www.businesswire.com/news/home/20260514989293/en/IQM-and-Real-Asset-Acquisition-Corp.-Announce-Public-Filing-of-Form-F-4-Registration-Statement-with-the-SEC
- Globes, 25 Feb 2025 (QM valuation) — https://en.globes.co.il/en/article-1001502993
- Calcalist, 5 May 2026 (QM headcount) — https://www.calcalistech.com/ctechnews/article/bkzobwd0bx
- RCR Wireless, 30 Jul 2025 (Keysight AIST) — https://rcrwireless.com/20250730/test-and-measurement/quantum-control-system
- NextPlatform, 20 Jul 2026 (Google RL) — https://www.nextplatform.com/compute/2026/07/20/google-uses-ai-reinforcement-learning-for-quantum-error-correction/5275023
- Nikkei xTECH (QuEL; undated in fetch, ~2024–25) — https://xtech.nikkei.com/atcl/nxt/mag/nmc/18/00011/00298/
- Wikipedia, Zurich Instruments (accessed 12 Nov 2026) — https://en.wikipedia.org/wiki/Zurich_Instruments
- Aggregators (low reliability, used only where labelled): PitchBook QM https://pitchbook.com/profiles/company/234705-70 ; PitchBook Qblox https://pitchbook.com/profiles/company/439353-64 ; Quantum Security Defence (Qblox Series A) https://quantumsecuritydefence.com/quantum-news/qblox-funding/

Cross-referenced from team notes (not re-fetched by me):
- R&S release, 27 Oct 2026 (FY2025/26 revenue €3.6bn) — https://www.rohde-schwarz.com/jp/_229356-1706630.html
- ZI ZQCS release, 9 Mar 2026 — https://www.zhinst.com/de/news/zurich-instruments-launches-zqcs-quantum-control-system-master-long-lived-logical-qubit/
- Keysight 2025 Annual Report — https://s22.q4cdn.com/444849635/files/doc_financials/2025/ar/2025-Annual-Report.pdf
- CIQTEK SSE filing, 27 Aug 2026 — https://pdf.dfcfw.com/pdf/H2_AN202608261828489393_1.pdf ; Kaiyuan Securities note, 30 Oct 2026 — https://pdf.dfcfw.com/pdf/H3_AP202611031831349963_1.pdf
