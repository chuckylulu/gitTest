# AI Processor Industry Research Report

## User prompt 1

Deep research, data and information only. Sector: AI processors. Companies: NVIDIA; AMD; Broadcom (custom-chip division); Google's TPU unit (division of Alphabet); Amazon's chip unit, Annapurna Labs; Huawei's Ascend unit; Cerebras.

For each company, or for the relevant division where the business sits inside a larger group, gather the facts: what it makes and at what stage, technology and roadmap with dates, which past milestones were met or missed, revenue, margins, cash, debt and funding, customers and contracts, capacity, ownership and key people, legal and regulatory matters.

Examine the science under each one: what has been demonstrated, who outside the company has verified it, what remains unproven, and which physical or engineering limits apply. State whether it stands on solid ground, and why.

Cross-examine: test every important claim against sources the company does not control (customers, suppliers, competitors, regulators, published papers) and against the other companies on this list, and record the contradictions.

No rankings, recommendations or investment opinions. Give a date and a source for every figure, and say what you could not find or verify.

## Model response 1

*Research cutoff: November 18, 2026. All figures carry their reporting dates and primary or secondary sources. Where a unit sits inside a larger corporate parent that does not report standalone division financials, consolidated parent/segment figures are given and undisclosed division figures are explicitly flagged.*

---

## 1. NVIDIA Corporation

### A. Factual Profile

* **Products & Stage:**
  * **Blackwell (B200 / GB200 NVL72):** TSMC 4NP, 208B transistors, 192 GB HBM3e (8 TB/s), NVLink 5 (1.8 TB/s); in broad cloud availability across 15+ providers ``.
  * **Blackwell Ultra (B300 / GB300 NVL72):** Binned/upgraded Blackwell (288 GB HBM3e, 14 PFLOPS dense / 28 PFLOPS sparse FP4); shipping in volume and driving Q3 FY27 margin expansion ``.
  * **Vera Rubin (R200 GPU + 88-core Vera CPU, NVL72 rack):** TSMC 3nm, 336B transistors, 288 GB HBM4 (~22 TB/s), 35 PFLOPS dense / 50 PFLOPS sparse FP4, NVLink 6 (3.6 TB/s); entered full production May 2026, began production shipments August 2026, deployed September 2026, and shipped in NVL72 systems during Q3 FY27 ``. Standalone Vera CPUs are also shipping (SpaceXAI, OCI, Q3 FY27 revenue contributor) ``.
  * **Groq 3 LPX:** 256 SRAM-based LP30 local processing units per rack (128 GB total SRAM, 150 TB/s per-chip SRAM bandwidth, 640 TB/s rack scale-up bandwidth, no HBM), fabricated by Samsung Foundry on 4nm using IP licensed from Groq; entered full production August 24, 2026, with Nebius as first cloud adopter ``.
  * **Upcoming / Unshipped:** **Rubin Ultra** (2027 target) and **Kyber NVL144** rack ``; **Rubin HPC** (>50,000 CUDA cores, NVLink 7, announced Nov 16, 2026 for 2028) ``; **Feynman** (Rosa CPU, die stacking, custom HBM, NVLink 8 with co-packaged optics, penciled for 2028) ``.

* **Technology & Roadmap with Dates:**
  * Shifted from biennial cadence (Ampere 2020, Hopper 2022) to an annual cadence formalized at GTC March 2025: Blackwell Ultra (H2 2025), Vera Rubin (H2 2026, launched CES Jan 5, 2026), Rubin Ultra (H2 2027), Feynman (2028) ``.
  * **Software / Memory / Interconnect:** CUDA 13.4 (Sept 9, 2026) added preview Rubin (`sm_107`) support ``. Announced **NVLink Fusion** (open chiplet/switch interface for external XPU/CPU partners) and **NVHBM** (Aug 26, 2026—custom memory controller placed in HBM base die, claiming +30% bandwidth, -15% HBM power, +25% compute-die area vs standard HBM4e, targeted for FY29+) ``.

* **Past Milestones Met or Missed:**
  * *Met:* Blackwell shipped after initial 2024 interposer/mask fixes (``); Vera Rubin hit its fall 2026 shipment target (``); Groq 3 LPX reached production within 8 months of the Dec 24, 2025 Groq license agreement (``).
  * *Missed / Contested:* Blackwell experienced 2024 interposer packaging delays and 2025 Monolithic Power module overheating (``). In March–July 2026, SemiAnalysis and CNBC reported that the original 4-compute-die / 16-HBM4E Rubin Ultra package was canceled/halved to 2 dies over TSMC CoWoS-L substrate warpage, and that the Kyber NVL144 rack slipped 12+ months to 2028 due to 78-layer PCB midplane manufacturing difficulties (``); NVIDIA denied delays (``). Rubin CPX did not appear at GTC 2026 (``). In Q1 FY26, U.S. H20 restrictions forced $4.5B in net charges ($4.3B net for 9M FY26) (``).

* **Revenue, Margins, Cash, Debt & Funding:**
  * **FY2026 (ended Jan 25, 2026, reported Feb 25, 2026):** Revenue $215.938B (+65% YoY; Data Center $193.7B, +68% YoY); GAAP gross margin 71.1%, Non-GAAP 71.3%; GAAP operating income $130.387B; GAAP net income $120.067B; operating cash flow (OCF) $102.718B; free cash flow (FCF) $96.575B; cash, cash equivalents & marketable securities $62.556B; total debt $8.468B ($999M short-term, $7.469B long-term) ``.
  * **Q3 FY2027 (ended Oct 25, 2026, reported Nov 17, 2026):** Revenue $115.8B ($115.844B, +103% YoY, +20% QoQ); Compute & Networking segment $106.0B (+108% YoY), Graphics $9.8B (+62% YoY); Data Center platform $107.6B (+110% YoY: Hyperscale $60.1B, AI Clouds/Industrial/Enterprise $47.5B); China Data Center Hopper shipments $2.4B ``. GAAP GM 74.8%, Non-GAAP GM 74.9% (note: starting Q1 FY27, NVIDIA includes stock-based compensation in Non-GAAP metrics) ``. GAAP net income $65.287B; OCF $48.253B; FCF $43.777B ``.
  * **Q4 FY27 Outlook (Nov 17, 2026, 14-week quarter):** Revenue $130.0B ±3% (assuming $0 China Data Center compute revenue); GAAP and Non-GAAP GM guided down to **71.0%–72.0%** due to HBM/DRAM cost inflation absorbed on fixed-price orders and initial Rubin ramp costs (management guides FY28 GM at 72%–73% and ~75% revenue growth) ``.
  * **Balance Sheet & Off-Balance-Sheet Exposure (Oct 25, 2026):** Cash, cash equivalents & marketable debt securities $53.5B; marketable equity securities $44.219B and non-marketable equity securities $65.528B ($109.747B total equity investments, after $1.8B Q3 impairment); long-term debt $32.37B (up from $7.47B in Jan 2026 after $24.9B issuance; $1.0B repaid in Q3, $0 short-term debt); accounts receivable $81.0B (DSO 64 days vs 60 in Q2); inventory $39.7B ``. Total future commitments $518B ($390B supply/capacity, $74B uncommenced data center leases, $28B cloud agreements, $20B equity investments, $6B capex), plus $32B conditional neocloud agreements and $118B maximum gross guarantees ($105B for SB Energy's 4.25 GW PORTS-Pike campus leased to OpenAI) ``. Paid $13.0B in Q4 FY26 and $2.9B in H1 FY27 toward the ~$20B Groq licensing/talent transaction ``.

* **Customers & Contracts:**
  * AWS (committed 1M GPUs in March 2026 + 2M additional Blackwell Ultra/Rubin/Rubin Ultra GPUs for 2027–2028 in Aug 2026) ``; Meta (multiyear deal for millions of Blackwell/Rubin GPUs and CPUs) ``; Oracle OCI (multi-GW Vera Rubin NVL72 + Vera CPU + HGX Rubin NVL8) ``; Microsoft, Google Cloud, CoreWeave (>5 GW by 2030), Nebius, OpenAI (~10–12 GW LOI / $105B Ohio lease credit backstop), Anthropic (Azure scaling + $10B IPO cornerstone buy), SpaceXAI (standalone Vera CPUs) ``.

* **Capacity:**
  * **Foundry:** TSMC 4NP (Blackwell) and 3nm/3NP (Rubin) ``; Samsung Foundry 4nm sole manufacturer for Groq 3 LPX ``.
  * **Packaging & Memory:** Primary driver of TSMC CoWoS-L (130k wpm across industry in 2026 ``); OSATs SPIL, Amkor, KYEC, plus substrate suppliers Kinsus, Samsung Electro-Mechanics, IBIDEN, Unimicron ``. SK Hynix, Samsung, and Micron qualified for Rubin HBM4 ``. Supply commitments hit $390B as of Oct 25, 2026 ``.

* **Ownership & Key People:**
  * Publicly traded (NASDAQ: NVDA); broad institutional ownership; former CEO Jensen Huang held no super-voting shares (~3.6% voting power) ``.
  * **Leadership Crisis (Nov 2026):** Co-founder/CEO **Jensen Huang resigned effective Nov 12, 2026** as President, CEO, and director following *New York Times* reports of extramarital affairs with an employee (Kimberly Powell) and with Alice Huang (former Megaspeed executive suspected by U.S. intelligence of being a Chinese intelligence asset) ``. **Colette Kress** (EVP & CFO) is **Interim CEO**; longtime director **Harvey Jones** was named NVIDIA's first independent Board Chair ``. On Nov 17, 2026, Huang posted he would return if asked, while CNBC/Fortune reported the Board closed the door on a return and is conducting a search (reportedly sounding out Arm CEO Rene Haas, though the Board stated it had not formally engaged candidates) ``. General Counsel: Tim Teter ``. Groq founder Jonathan Ross and President Sunny Madra joined NVIDIA in Dec 2025 ``.

* **Legal & Regulatory Matters:**
  * **Export Controls & Congressional/SEC Probes (Nov 2026):** Board formed a National Security & Export Control Oversight Committee (Nov 17, 2026) and retained Wachtell Lipton for a board probe ``. Huang and Tim Teter agreed to appear before House Foreign Affairs, China Select, and Intelligence Committees over Megaspeed (which imported $4B+ / allegedly diverted 240,000 chips) ``. *WSJ* reported Nov 17, 2026 that the SEC opened a civil probe into whether NVIDIA's disclosures misled investors ``. On Nov 15–16, 2026, BIS issued an interim final rule (`RIN 0694-AK50`) requiring licenses for AI chip shipments to Indonesia, Malaysia, Singapore, Thailand, and Brazil and restricting remote compute >12M aggregate TPP for China/D:5 entities ``. Earlier BIS Jan 15, 2026 rule allowed case-by-case H200 review (`TPP < 21,000`), though Q4 FY27 outlook assumes $0 China Data Center revenue ``.
  * **Antitrust:** DOJ probing NVIDIA's proposed $12.93B acquisition of Hugging Face (Oct 2026; EU expected to review) ``; European Commission advancing informal NVIDIA antitrust investigation (Oct 2026) ``.

* **Could Not Find / Verify:**
  * Q3 FY27 Form 10-Q (not yet filed as of Nov 18, 2026) ``; standalone revenue split between Blackwell Ultra, Vera Rubin, Vera CPU, and Networking; permanent CEO outcome; verified conclusion on whether Alice Huang acted as a Chinese intelligence operative (AG Todd Blanche stated DOJ had reached no conclusion as of Nov 12, 2026 ``).

### B. Scientific & Engineering Examination

* **Demonstrated:** Full-stack hardware-software co-design combining SIMT Tensor Core GPUs, hardware-coherent NVLink scale-up domains (NVL72), NVFP4 (block size 16) quantization, CUDA compiler/runtime maturity, and deterministic SRAM-based decode via Groq 3 LPX ``. Measured at massive production scale in MLPerf Training v6.1 (Nov 16, 2026: 10,240-GPU GB300 cluster for DeepSeek-V3 671B; Vera Rubin NVL72 achieving >97% scaling efficiency from 256 to 1,024 GPUs and winning 6 of 7 benchmarks) ``.
* **External Verification:**
  * **MLCommons MLPerf Training v6.1 (Nov 16, 2026) & Inference v6.1 (Sept 16, 2026):** 14 partner organizations submitted independent NVIDIA results in Inference v6.1 ``.
  * **Harvard / Meta ISPASS 2026 (`arXiv:2604.10852`, Apr 12, 2026):** Independently verified on A100/H100 that NVIDIA GPUs consume only 20% TDP at idle and 50–60% TDP in memory-bound decode, maintain full per-kernel and built-in power telemetry, and remain Pareto-optimal at higher throughput batch sizes ``.
  * **SemiAnalysis / Artificial Analysis:** Verified Blackwell Ultra and Rubin InferenceX performance and Groq 3 LPX token rates ``.
* **Unproven:** Rubin Ultra's 4-die (or revised 2-die) CoWoS-L/SoIC thermal and warpage stability ``; Kyber NVL144 78-layer PCB midplane manufacturability at volume ``; Feynman's 2028 co-packaged optics NVLink 8 and custom HBM ``; real-world adoption of Groq 3 LPX (non-CUDA toolchain) inside Rubin clusters ``; and whether NVFP4 maintains numerical convergence on all future scientific/frontier architectures without precision fallback.
* **Physical & Engineering Limits:**
  * **Packaging & Warpage:** Reticle-limit multi-die packages (2+2 dies + 12–16 HBM4/4E stacks) encounter coefficient-of-thermal-expansion (CTE) warpage on CoWoS-L interposers/organic substrates, and SK Hynix notes a 775-micron HBM stack height ceiling forcing 30-micron DRAM die thinning ``.
  * **Power & Cooling Density:** Rack power jumping from ~120–145 kW (GB200 NVL72) toward liquid-cooled 700–1,400 W+ GPUs and dense 144-GPU Kyber midplanes ``.
  * **Memory Wall:** HBM4/DRAM supply limits and base-die controller area/power overhead ``.
* **Scientific Grounding Assessment:** **Stands on solid engineering and scientific ground for shipped systems (Hopper, Blackwell, Blackwell Ultra, Vera Rubin NVL72)**, supported by peer-reviewed MLPerf submissions across 14 external submitters and independent academic telemetry (`arXiv:2604.10852`) ``. However, **2027–2028 architectural scaling claims (4-die Rubin Ultra, Kyber NVL144, Feynman)** face unresolved physical packaging, midplane PCB signal-integrity, and HBM-height limits evidenced by credible supply-chain engineering reports ``.

---

## 2. Advanced Micro Devices (AMD)

### A. Factual Profile

* **Products & Stage:**
  * **Instinct MI300X / MI325X (CDNA 3):** Shipping in volume (192 GB HBM3 / 256 GB HBM3e); MI308 custom China-compliant variant ``.
  * **Instinct MI350X / MI355X (CDNA 4) & MI350P (PCIe):** TSMC 3nm, up to 288 GB HBM3e (8 TB/s), 5.03 PFLOPS dense FP8; broadly available in cloud/enterprise (MI350P introduced May 2026) ``.
  * **Instinct MI400 Series & Helios Rack-Scale System (CDNA 5):** Multi-chiplet package combining **TSMC 2nm (N2)** compute dies (3D hybrid-bonded XCDs) and **TSMC 3nm (N3P)** I/O/cache dies on CoWoS-L, 320B transistors ``. Lineup launched July 23, 2026 and expanded Nov 12, 2026 ``:
    * **MI455X:** 432 GB HBM4 (12 stacks), 23.3 TB/s peak bandwidth (19.6 TB/s in rack brochure), ~40.3 PFLOPS FP4; ramping in **Helios** racks (72 MI455X GPUs + 18 EPYC "Venice" Zen 6 SP7 CPUs, UALoE 1.8 TB/s/direction/GPU scale-up, Pensando Vulcano 800 AI NICs) ``.
    * **MI450X:** 288 GB HBM4, same compute/bandwidth, introduced Nov 12, 2026 (no customer shipment date stated) ``.
    * **MI430X:** Native FP64 + 432 GB HBM4 (23.3 TB/s) for HPC/AI; won EuroHPC LUMI-AI (live H2 2027) and Oak Ridge Lux ``.
    * **MI440X:** Enterprise on-prem variant teased Jan 2026 ``.
  * **Upcoming:** **Instinct MI500 (CDNA 6, 2nm)** targeted for 2027 ``.

* **Technology & Roadmap with Dates:**
  * MI300X (late 2023) → MI325X (late 2024/2025) → MI350X/MI355X (May 2025/Q1 2026) → MI455X / Helios (July 23, 2026 launch; initial deployments Q3 2026; volume ramp Q4 2026–2027) → MI500 (2027) ``.
  * Software: **ROCm 10** and **Primus** training framework, now on a 6-week ROCm release cadence (announced July 2026 via TheRock build system) ``. Also acquired **ZT Systems** (closed Mar 31, 2025 for $4.4B per 10-Q; sold manufacturing to Sanmina Oct 27, 2025 for $3B while retaining rack design team) ``, **Taalas** (announced Aug 6, 2026; closed Nov 2026 for up to $2.9B incl. $1.4B earn-out; etches AI weights into silicon) ``, and **World Labs** (announced Sept 28, 2026; closed Nov 13, 2026 for ~14.98M shares / ~$8.2B announced value) ``.

* **Past Milestones Met or Missed:**
  * *Met:* Achieved initial Helios/MI450 customer workload bring-up in Q3 2026 (confirming Anush Elangovan's Feb 2026 rebuttal of H2 2026 delay rumors) ``; opened Oak Ridge Lux supercomputer (Top500 #14, 220.79 PFLOPS) on Nov 16, 2026 ``.
  * *Missed / Unresolved:* As of Sept 26, 2026, **zero warrant shares** had vested under either the OpenAI or Meta 6 GW agreements ``; Q3 2026 earnings gave no shipped GW counts ``; MI455X did not appear in official peer-reviewed MLPerf v6.1 rounds ``; and 2025 BIS MI308 export rules forced ~$800M in Q2 2025 inventory charges (~$360M reversed in Q4 2025, ~$440M net 2025 charge; Q1 2026 China MI308 revenue called "not material") ``.

* **Revenue, Margins, Cash, Debt & Funding:**
  * **FY2025 Segment Highlights:** Data Center $16.635B (+32% YoY), Client $10.640B (+51% YoY) ``.
  * **Q3 2026 (ended Sept 26, 2026, reported Nov 3, 2026):** Total revenue $13.377B (+45% YoY, +16% QoQ); **Data Center $8.546B** (+97% YoY, +27% QoQ; segment operating income $2.9B, 34% margin); Client & Gaming $3.722B (-8% YoY: Client $2.949B, Gaming $773M); Embedded $1.109B (+29% YoY) ``.
  * **Margins & Profit (Q3 2026):** GAAP GM 54%, Non-GAAP GM 56%; GAAP operating income $2.832B (21% margin), Non-GAAP operating income $3.923B (29% margin); GAAP net income $2.428B (depressed by a $1.097B non-cash warrant liability remeasurement charge), Non-GAAP net income $3.471B ``.
  * **Cash, Debt & Cash Flow (Sept 26, 2026):** Cash, cash equivalents & short-term investments $15.78B ($15.8B); total debt $7.08B ($7.1B, including $4.75B senior notes issued Aug 2026); inventories $11.46B (+$3.0B QoQ for Q4 Helios build); OCF $1.2B; FCF $554M ``. Unconditional purchase commitments $30.3B as of June 27, 2026 ``.
  * **Guidance (Nov 3, 2026):** Q4 2026 revenue ~$17.0B ±3% (+66% YoY; Data Center ~+50% QoQ); 2026 & 2027 revenue expected to grow >80% (Data Center >80% of 2027 revenue) ``.

* **Customers & Contracts:**
  * **OpenAI:** Oct 6, 2025 agreement for 6 GW Instinct GPUs (starting 1 GW MI450 H2 2026) + warrant for up to **160M AMD shares at $0.01/share** (vesting on GW milestones and stock targets up to $600, expiring Oct 5, 2030) ``. On Nov 16, 2026, **TensorWave** signed a 6-year contract to supply OpenAI with **457 MW** of dedicated MI455X/Helios capacity (first online H1 2027, full early 2028) ``. OpenAI also pairs Broadcom-built Jalapeño ASICs with AMD EPYC Turin CPUs ``.
  * **Meta:** Feb 23, 2026 agreement for up to 6 GW Instinct GPUs + matching warrant for **160M AMD shares at $0.01/share** (expiring Feb 23, 2031) ``; AMD also invested $1.0B in a public company equity offering in Oct 2026 (Meta Helios testing) ``. Together, OpenAI and Meta warrants represent 320M shares (~19.6% of July 2026 outstanding shares) ``.
  * **Anthropic:** July 20, 2026 partnership for up to 2 GW MI450 GPUs (S-1 lists >$20B MI450 commitment; AMD buying $2.5B in Anthropic IPO placement) ``.
  * **Other:** Microsoft, Oracle Cloud Infrastructure, Crusoe, HPE/Vultr, HUMAIN (Saudi Arabia), EuroHPC LUMI-AI (€387.8M via Bull), Oak Ridge Lux, and Cerebras (July 22, 2026 disaggregated inference: AMD GPUs for prefill) ``.

* **Capacity:**
  * Fabless, relying on **TSMC** for all ≤7nm CPU/GPU wafers (`2nm N2` + `3nm N3P` for MI455X/Venice) and CoWoS-L ``. Signed HBM4 supply MOU with **Samsung** on Mar 18, 2026 ``. Announced >$10B Taiwan advanced packaging supply-chain investments (May 21, 2026) ``. System NPI/manufacturing partnered with **Sanmina** ``.

* **Ownership & Key People:**
  * Publicly traded (NASDAQ: AMD). Chair & CEO: **Dr. Lisa Su**; EVP & CFO: **Jean Hu**; EVP Data Center Solutions: **Forrest Norrod**; CVP & GM Data Center GPU Business: **Andrew Dieckmann**; SVP AI: **Vamsi Boppana**; EVP & Chief Scientist: **Fei-Fei Li** (joined Nov 2026 via World Labs) ``.

* **Legal & Regulatory Matters:**
  * **Export Controls:** MI308 restricted to China (Apr 2025 license requirement, ~$440M net 2025 charge); BIS Jan 13–15, 2026 rule allowed case-by-case MI325X (`TPP ~20,800 < 21,000`) exports while barring MI400 series (`>21,000 TPP`, `>6.5 TB/s`) ``. Nov 15–16, 2026 BIS interim rule imposed licensing on 5 third-country hubs and remote compute >12M TPP ``.
  * **Customer Warrant Accounting:** Carry $4.5B unamortized revenue-reduction potential upon qualifying sales (``).

* **Could Not Find / Verify:**
  * Standalone Instinct AI GPU revenue vs EPYC server CPU revenue inside Data Center ($8.546B in Q3 2026); MI455X/MI450X official per-GPU TDP; exact shipped GW count to OpenAI/Meta; FY2025 consolidated revenue/cash totals from the FY2025 10-K; independent confirmation of Greg Brockman's Nov 18, 2026 claim that OpenAI models compressed 12 months of AMD chip design into 5 months ``.

### B. Scientific & Engineering Examination

* **Demonstrated:** Modular chiplet disaggregation (`2nm` compute XCDs + `3nm` I/O/cache dies on CoWoS-L with 3D hybrid bonding) reduces defect exposure on leading-edge 2nm wafers while scaling HBM4 capacity to 432 GB (12 stacks) and native FP64 (MI430X) ``. Open standards networking (UALoE / Ultra Ethernet / RoCE) scaled cleanly to 128 GPUs in training and 512 MI355X GPUs in inference ``. Software optimization velocity was quantitatively demonstrated: on unchanged MI355X hardware, ROCm updates improved GPT-OSS-120B MLPerf Inference throughput by +37.9%–38% (v6.0→v6.1) and reduced training times ~16%–19% ``.
* **External Verification:**
  * **MLCommons MLPerf Inference v6.1 (Sept 16, 2026) & Training v6.1 (Nov 16, 2026):** 9 submitters (Dell, HPE, Supermicro, Oracle, MiTAC, Crusoe, etc.) reproduced MI355X/MI350X/MI350P numbers within ~4% of AMD's own scores; 8-GPU MI355X matched NVIDIA B300 within 0.4% per GPU on `gpt-oss-120b` Server inference ``.
  * **Harvard / Meta ISPASS 2026 (`arXiv:2604.10852`):** Independently verified MI300X on physical 8-GPU hardware: 20% TDP idle power, 0.81× power of H100 per equivalent FLOP, consistent thermal regulation, and Pareto-optimality at high batch sizes (though decode draws 80% of TDP vs NVIDIA's 50–60%) ``.
* **Unproven:** **MI455X / Helios performance in independent hands.** AMD's Nov 12, 2026 headline of 21,333 tok/s/GPU on DeepSeek-R1 (+30% over Vera Rubin) was an internal AMD lab measurement in Offline mode, not an official MLPerf submission ``. Neither MI455X nor Helios has appeared in MLPerf v6.1, `arXiv:2604.10852`, or Multi-GW OpenAI/Meta production runs ``.
* **Physical & Engineering Limits:**
  * **3D Hybrid-Bonding & 12-High HBM4 Thermals:** Stacking N2 XCDs on 3nm cache/I/O dies increases vertical thermal resistance while 12 HBM4 stacks approach CoWoS-L reticle/substrate boundaries ``.
  * **Ecosystem & Kernel Coverage:** Independent testing still flags edge-case compiler/kernel parity gaps vs CUDA and the risk of software fragmentation across ROCm, Taalas weight-etched ASICs, and Pensando fabrics ``.
* **Scientific Grounding Assessment:** **CDNA 3/4 (MI300X/MI355X) and ROCm software momentum stand on solid, externally verified ground** via 9 independent MLPerf v6.1 submitters and Harvard/Meta physical measurements ``. **CDNA 5 (MI455X/Helios) rests on sound chiplet physics and early customer bring-up, but its +30% throughput claim over Vera Rubin remains scientifically unverified outside AMD's own lab** ``.

---

## 3. Broadcom Inc. (Custom-Chip / XPU Division)

### A. Factual Profile

* **Products & Stage:**
  * **Custom AI Accelerators (XPUs / ASICs):** Co-designs physical layout, high-speed 200G/400G SerDes, memory subsystem integration, and advanced packaging (`3.5D XDSiP` combining TSMC SoIC face-to-face 3D stacking with 2.5D CoWoS, supporting >6,000 mm² silicon and up to 12 HBM stacks) ``.
  * **Current Shipping Custom Programs (Q3 FY26, Sept 2, 2026):** High-volume shipments of **Google TPU v7 (Ironwood)** to Google and Anthropic; began production shipments of **Google TPU v8i**; shipped **OpenAI Jalapeño** (first-generation inference ASIC, TSMC N3P, 216 GiB HBM4); **Meta MTIA** ramping production shipments in Q4 FY26 (with 2nm multi-GW partnership through 2029); **Apple** custom ASICs (reportedly **Baltra** AI server chip, TSMC N3E, targeted 2027, agreement extended to 2031); **ByteDance** and **Fujitsu** also named among XPU customers ``.
  * **AI Networking (Complementary Scale-Up/Out):** **Tomahawk 6** (100G/200G SerDes, deployed by "pretty much all" hyperscalers), **Tomahawk Ultra** (scale-up Ethernet, shipping Q3–FY27), **Tomahawk 7** (taped out by Sept 2026), plus **VCSEL Near-Package Optics / Co-Packaged Optics (CPO)** ``.

* **Technology & Roadmap with Dates:**
  * Google TPU partnership since 2014 (7+ generations), extended **Apr 6, 2026 through 2031** ``.
  * OpenAI 10 GW collaboration announced **Oct 13, 2025** (racks starting H2 2026–2029 using 3nm and 2nm designs; Jalapeño unveiled June 24, 2026, benchmarked Hot Chips Aug 25, 2026, shipped Q3 FY26) ``.
  * Meta multi-year 2nm MTIA partnership announced **Apr 14, 2026** (extending through 2029, >1 GW initial phase, 3 GW through 2028) ``.
  * Apple custom ASIC extension filed **July 6, 2026** through 2031 ``.

* **Past Milestones Met or Missed:**
  * *Met:* Completed OpenAI Jalapeño tape-out in ~16 months from mid-2024 hiring to shipping B0 silicon in Q3 FY26 ``; began TPU v8i production shipments ahead of MediaTek's TPU v8t ``.
  * *Missed / Headwinds:* Lost exclusive single-source status at Google as Google brought in **MediaTek** for TPU I/O / TPU 8t to reduce Broadcom reliance and pricing ``. In Aug 2026, SemiAnalysis cut Broadcom's 2026 Google TPU CoWoS estimates by 500k v7 and 80k v8i units due to CoWoS-S bottlenecks ``. Apple's Baltra reportedly faced mid-2026 delays ``.

* **Revenue, Margins, Cash, Debt & Funding:**
  * *Standalone XPU Division:* Broadcom does **not** report standalone XPU P&L, gross margin, cash, or debt; it reports **Semiconductor Solutions** and **Infrastructure Software** segments ``.
  * **Q3 FY2026 (ended Aug 2, 2026, reported Sept 2, 2026):** Consolidated revenue $29.591B (+86% YoY); **Semiconductor Solutions $20.839B** (+127% YoY, 70% of revenue); Infrastructure Software $8.752B (+29% YoY) ``. **AI semiconductor revenue $16.7B** (+221% YoY, +54% QoQ; **XPUs = 73% ≈ $12.2B**, AI networking = 27% ≈ $4.5B) ``.
  * **Margins & Profit (Q3 FY26):** Consolidated GAAP GM **69.1%** ($20.456B / $29.591B); GAAP operating income $15.955B (53.9%); Non-GAAP operating income $20.095B (67.9% record margin); GAAP net income $13.088B; Non-GAAP net income $16.372B; OCF $14.197B; CapEx ~$532M; FCF $13.665B (46% of revenue) ``. Tan warned investors that custom AI chip mix dilutes gross margin while preserving operating margin ``.
  * **Cash, Debt & RPO (Aug 2, 2026 10-Q):** Cash & cash equivalents $23.975B; total debt $59.419B carrying value ($2.252B short-term, $57.167B long-term; $61.079B principal, digested down from VMware's $61B deal); RPO **$179.2B** (incl. new custom AI contract signed Q2 FY26) ``.
  * **Guidance & Financing Commitments:** Q4 FY26 consolidated revenue ~$34.8B, AI semiconductor revenue **$21.7B** (+236% YoY), FY26 AI total **$58B** ``. Management formally guided AI semiconductor revenue to **~$115B in FY27** and **~$230B in FY28** (explicitly noting supply & data-center readiness constraints) ``. Broadcom also agreed to lend **Anthropic up to $42B** (convertible note facility) to finance **$161.2B** of 5-year TPU equipment leases, closed a **$35B AI XPV financing tranche** with Apollo/Blackstone, arranged a **$63B SPV lease structure** (Oct 26, 2026) carrying an estimated **~$43B peak residual-value backstop** (8-K), and disclosed a **$29B** 5-year 85%-threshold lease backstop in its Q3 10-Q ``.

* **Customers & Contracts:**
  * Google (multi-tens of billions annually through 2031), Anthropic (1 GW Ironwood 2026 → 5 GW TPU 8i 2027 → 10 GW 2028; $161.2B leases), OpenAI (10 GW term sheet; 1.3 GW Jalapeño 2027 → >5 GW 2028), Meta (3 GW MTIA through 2028–2029), ByteDance, Fujitsu, Apple (~20% of total Broadcom revenue across wireless/RF/ASICs; renewed through 2031) ``.

* **Capacity:**
  * Fabless, heavily concentrated at **TSMC** (N3P, N2, SoIC, CoWoS-S/L) ``. Expanding Singapore substrate capacity and tripling indium phosphide/laser capacity for optics ``. Management flagged HBM, substrates, lasers, and data-center shell/power as deployment caps ``.

* **Ownership & Key People:**
  * Publicly traded (NASDAQ: AVGO). Chairman: **Henry Samueli**; President & CEO: **Hock Tan** (also took Meta advisory role Apr 2026 ``); CFO: **Amie Thuener**; President, Semiconductor Solutions Group: **Dr. Charlie Kawwas**; VP & GM, ASIC Products Division: **Frank Ostojic** ``.

* **Legal & Regulatory Matters:**
  * **EU Antitrust Inquiry (VMware):** On Feb 26, 2026, European Commission issued a formal RFI alleging dominant-position abuse (tying, >1,000% price hikes, terminating Cloud Service Provider partner model); EU General Court dismissed Broadcom's attempt to withhold U.S.-privileged in-house counsel documents on Aug 3, 2026 (Case T-280/26); EU questioning of European cloud providers intensified Sept 2026 (potential fines up to 10% of global revenue) ``.
  * **Export Controls:** BIS Nov 15–16, 2026 interim rule explicitly scrutinizes ByteDance/Chinese remote compute and foreign-designed ASICs (``), directly impacting ByteDance XPU supply risk (``).
  * **Anthropic S-1 Conflict Disclosure:** Anthropic's Oct 2026 IPO filing flagged "potential conflicts of interest" from Broadcom acting simultaneously as hardware supplier, lessor, and $42B lender ``.

* **Could Not Find / Verify:**
  * Standalone custom-XPU revenue vs AI networking exact split in Q4/FY26; standalone ASIC division gross/operating margins and cash/debt; whether the $43B 8-K lease guarantee and $29B 10-Q backstop are additive or overlapping ``; ByteDance custom ASIC current shipment status under Nov 2026 BIS rules.

### B. Scientific & Engineering Examination

* **Demonstrated:** Broadcom supplies foundational physical-layer IP—200G SerDes, UCIe/die-to-die interfaces, Tomahawk Ethernet switching, and **3.5D XDSiP** (face-to-face SoIC + CoWoS)—allowing hyperscalers without 3nm/2nm physical implementation teams to tape out competitive accelerators in 9–16 months ``. Broadcom-implemented silicon (TPU v7 Ironwood, OpenAI Jalapeño, TPU v8i) is physically taped out, shipping, and executing production LLM inference ``.
* **External Verification:**
  * **Customer & Independent Benchmarks:** OpenAI & SemiAnalysis benchmarked Broadcom-implemented **Jalapeño** (TSMC N3P, 6 HBM4 stacks / 216 GiB / 15.4 TB/s, 13.4 PFLOPS MXFP4, 700W package / ≤550W measured) on SemiAnalysis's public **InferenceX** suite at Hot Chips (Aug 25, 2026), measuring 700+ tok/s/user on DeepSeek-R1 and 1.5–1.9× throughput per watt vs GB200/GB300 ``. SemiAnalysis's InferenceX (Sept 2026) and Inferact (Sept 23, 2026) independently verified Broadcom-built **TPU v7 Ironwood** beating GB200/B300 ``.
* **Unproven:** Broadcom's **TPU v8i** comparability to NVIDIA Vera Rubin (asserted by Hock Tan Sept 2, 2026, with zero public third-party benchmarks ``); Jalapeño vs **Vera Rubin** (Jalapeño was only tested against Blackwell GB200/GB300, and using single-token rather than multi-token prediction ``); **3.5D XDSiP** high-volume yields >6,000 mm² with 12 HBM stacks; and **Meta MTIA / Apple Baltra** production performance.
* **Physical & Engineering Limits:**
  * **Advanced Packaging Bottleneck:** CoWoS-S/L interposer capacity and substrate warpage (``); 12-stack HBM4 thermal dissipation and 775 µm stack height limits (``).
  * **Customer-Owned Software & Model Portability:** Broadcom owns physical silicon/memory-layer implementation (``) rather than the ML compiler/software stack—meaning system efficiency depends on the customer's software (Google XLA/Pallas, OpenAI kernels, Meta compilers), and Broadcom faces disintermediation if customers shift to MediaTek (``) or Intel EMIB-T (``).
* **Scientific Grounding Assessment:** **Stands on solid engineering ground in physical design, SerDes/Ethernet switching, and multi-generation ASIC execution**, validated by working silicon across Google TPUs and OpenAI Jalapeño ``. However, **Broadcom does not own the AI compiler/software moat**, leaving its FY27–FY28 $115B–$230B revenue trajectory heavily exposed to TSMC packaging/HBM bottlenecks and customer data-center financing/construction readiness ``.

---

## 4. Google's TPU Unit (Division of Alphabet Inc.)

### A. Factual Profile

* **Products & Stage:**
  * **TPU v5e / v5p & v6e (Trillium):** Broadly deployed on Google Cloud (v6e GA mid-2025: 918 TFLOPS BF16, 32 GB HBM) ``.
  * **TPU v7 (Ironwood / TPU7x):** First native-FP8 TPU (4,614 TFLOPS FP8, 2,307 TFLOPS BF16, 192 GiB HBM3e at 7.38 TB/s, 2 TensorCores, 4 SparseCores, 1.2 TB/s ICI, 9,216-chip superpods = 42.5 FP8 ExaFLOPS, ~600W TDP) ``. Announced Apr 2025, Preview Nov 24, 2025, **GA Mar 31, 2026** (Compute Engine integration GA June 1, 2026) ``. **Now sold externally as standalone hardware systems** for customer data centers ``.
  * **8th-Generation TPUs (Bifurcated Training & Inference, Announced Apr 22 & Nov 9, 2026):**
    * **TPU 8t (Training):** 12.6 PFLOPS FP4, 216 GB HBM at 6.528 TB/s, 128 MB SRAM, Arm Axion hosts, 9,600-chip superpods, Virgo fabric (>134,000 chips), claiming up to 2.7× Ironwood training price-performance ``.
    * **TPU 8i (Inference / Reasoning):** 10.1 PFLOPS FP4, 288 GB HBM at 8.601 TB/s, 384 MB SRAM, Boardfly high-radix switch topology (1,152-chip domains, halving network hops from 16 to ~7), Arm Axion hosts, claiming +80% inference price-performance vs Ironwood ``. Broadcom stated it began production shipments of TPU 8i in Q3 FY26, while Google Cloud's product page listed it as "Coming Soon" ``.
    * **TPU 8tx & TPU 8i Max (Announced Nov 9, 2026):** System configurations reusing 8th-gen silicon (no GA date, pricing, or regions published as of Nov 9 ``): **TPU 8tx** pairs 8t silicon with **5th Gen AMD EPYC hosts** and Boardfly networking for hardware-encrypted confidential inference ``; **TPU 8i Max** co-packages **2 TPU 8i chips** in one package, doubling compute, SRAM, and HBM bandwidth (to 17.2 TB/s) for long-context agents ``.

* **Technology & Roadmap with Dates:**
  * First internal TPU deployed 2015 ``. Annual/rapid cadence: v5p (2023/2024) → v6e Trillium (2024/2025) → v7 Ironwood (Apr 2025 unveil, Mar 31, 2026 GA) → 8th Gen 8t & 8i (Apr 22, 2026) → 8tx & 8i Max (Nov 9, 2026; 4 systems in 1 year) ``.
  * **Software & Stack:** Open-sourced **TorchTPU**, **TPU Sync** (tiering KV caches off HBM to host DRAM/storage, claiming >90% TTFT latency reduction), **llm-d 1.0**, and **AI-Hypercomputer/tpu-codesign** guide (Nov 16, 2026) ``. Note: TensorFlow is no longer supported on TPU7x (JAX and PyTorch only) ``.
  * **Future Rumors:** Reportedly exploring Intel **EMIB-T** packaging for future **TPU v9** parts ``.

* **Past Milestones Met or Missed:**
  * *Met:* Ironwood reached GA Mar 31, 2026 and scaled to ~100 external customers ``; Gemini 4 Argon & Carbon trained/served at 32B tokens/minute ``; Broadcom began shipping TPU 8i in Q3 FY26 ``.
  * *Missed / Bottlenecked:* Ironwood lacked native FP4 (losing FP4 benchmarks until 8th-gen) ``. SemiAnalysis (Aug 2026) cut 2026 TPU v7 CoWoS forecasts by 500,000 units (3.2M→2.7M) and TPU 8i by 80,000 units due to CoWoS-S bottlenecks ``. TPU 8t (MediaTek) trailed 8i in shipment timing despite starting earlier ``. Alphabet is renting third-party compute due to supply constraints ``.

* **Revenue, Margins, Cash, Debt & Funding:**
  * *Standalone TPU Unit:* Alphabet does **not** disclose TPU revenue, margins, R&D, cash, or debt separately ``.
  * **Alphabet Q3 2026 (ended Sept 30, 2026, reported Oct 28, 2026):** Consolidated revenue $127.58B (+25% YoY; >$500B run rate); **Google Cloud revenue $30.709B** (+103% YoY, 24% of Alphabet); **Cloud operating income $11.121B** (**36.2% margin**, up from 23.7% a year earlier); Cloud backlog **$560.8B** (total Alphabet backlog $567.7B) ``. Management stated external **TPU systems sales** were a "meaningful contributor" to Cloud growth, with inventory jumping from $2.4B to **$13.3B** ahead of 2027 ramp ``.
  * **Alphabet Cash, Debt & CapEx (Sept 30, 2026):** GAAP net income available to common $26.2B (hit by $8.7B equity loss, primarily SpaceX markdown) ``; OCF $42.29B; **CapEx $51.36B** (+114% YoY; FY26 CapEx guide **$195–$205B**, rising significantly in 2027); **Q3 FCF -$9.07B** (`-$5.86B` in Q2) ``. Cash & marketable securities **$265.1B** (incl. $90.4B marketable equity securities, $75.2B SpaceX); **Long-term debt $125.102B** (up from $46.547B at end-2025) ``. In 2026, Alphabet paused buybacks and raised ~$85.22B in debt, $42.87B in common stock (incl. $10B Berkshire Hathaway, $12.4B ATM), and $19.06B in mandatory convertible preferred stock ``. Purchase commitments total **$924.4B**, plus $130.5B in uncommenced data center/energy leases ``.

* **Customers & Contracts:**
  * Nearly 100 external TPU customers ``. **Anthropic:** ~1M TPUs (>1 GW Ironwood in 2026, expanding to ~3.5–3.9 GW+ TPU 8i in 2027; Anthropic S-1 discloses **$114.5B** direct to Google through July 2033 + **$161.2B** 5-year Broadcom TPU leases + $125–$150B est. 2028–2031; Google buying $10B in Anthropic IPO for up to 14.99% equity) ``. Other named users/partners: **Apple** (customized Gemini / TPU usage), **Oracle**, **Crux AI**, **Citadel Securities**, **Ineffable Intelligence**, and **Meta** (running TPU capacity) ``.

* **Capacity:**
  * Co-designed with **Broadcom** and **MediaTek**, fabricated at **TSMC** (CoWoS-S/L bottlenecks in H2 2026 ``; exploring Intel EMIB-T for v9 ``). Heavy reliance on Optical Circuit Switches (OCS) and 4th-gen liquid cooling ``.

* **Ownership & Key People:**
  * Internal division of **Google LLC / Alphabet Inc.** (NASDAQ: GOOGL/GOOG). CEO: **Sundar Pichai**; Google Cloud CEO: **Thomas Kurian**; SVP & Chief Technologist, AI & Infrastructure: **Amin Vahdat**; VP Infrastructure: **Mark Lohmeyer**; Distinguished Engineer: **Diwakar Gupta** (TPU technical lead) ``.

* **Legal & Regulatory Matters:**
  * **U.S. Search Antitrust (`U.S. v. Google`, D.D.C.):** Judge Amit Mehta found illegal search monopoly (Aug 2024); Final Judgment (Dec 2025) barred exclusive defaults, mandated annual contract rebidding, and ordered search-index data sharing (covering Gemini placement), rejecting Chrome/Android breakup; both DOJ/States and Google appealed in Feb 2026 ``.
  * **U.S. AdTech Antitrust (`U.S. v. Google`, E.D.V.A.):** Judge Leonie Brinkema found illegal AdX/DFP monopoly (Apr 17, 2025); on **Sept 2, 2026**, rejected forced AdX divestiture and ordered behavioral/interoperability remedies ``.
  * **EU DMA:** Ongoing DMA fines and compliance scrutiny ``.

* **Could Not Find / Verify:**
  * Standalone TPU unit revenue, CapEx allocation, BOM cost, or operating margins; TPU 8t/8i/8tx/8i Max foundry node (likely 3nm/2nm), TDP, pricing, and GA dates ``; official Google confirmation of Broadcom vs MediaTek partner assignments ``.

### B. Scientific & Engineering Examination

* **Demonstrated:** Systolic-array matrix units coupled with dedicated **SparseCores** (for MoE/embedding acceleration), 3D torus **Inter-Chip Interconnect (ICI)** + Optical Circuit Switches (in Ironwood), and hierarchical **Boardfly** high-radix switching (in 8i, halving worst-case network hops across 1,024–1,152 chips from 16 to ~7) ``. Proven at multi-thousand-chip production scale for Gemini 4 and Claude training/inference ``.
* **External Verification:**
  * **SemiAnalysis InferenceX (Sept & Nov 2026):** Independently verified **TPU v7 Ironwood** delivering +50.4% more tokens/$ than B200 and +96.0% over B300 at 20 tok/s/user on Qwen3.5 397B (FP8), and Nov 2026 FP8 results beating GB300 NVL72 FP4 at 1.67× perf/$ ``.
  * **Inferact (Sept 23, 2026):** Open-sourced Pallas megakernels on 16× TPU v7 Ironwood measuring 709 tok/s on Kimi K3 vs 452 tok/s on 16× GB200 ``.
  * **Harvard / Meta ISPASS 2026 (`arXiv:2604.10852`):** Physically profiled TPUv5e on GCP, finding it had one of the most mature software/profiling stacks outside NVIDIA/AMD (exposing per-kernel latency and `tpu-info` telemetry) and reached the Pareto frontier at throughput-oriented batch sizes ``.
* **Unproven:** **8th-gen TPUs (8t, 8i, 8tx, 8i Max)** have zero published third-party or MLPerf benchmarks ``; TPU Sync's >90% KV-cache latency cut and 150K+ token context tiering vs dedicated SRAM/HBM hardware remain unproven at frontier production scale ``; confidential encryption's "near-zero performance penalty" on TPU 8tx is vendor-claimed only ``.
* **Physical & Engineering Limits:**
  * **Static Shape / Systolic Rigidity:** Google's own Nov 16, 2026 co-design guide admits TPUs trade general-purpose hardware scheduling for wide systolic arrays, imposing hard Model FLOP Utilization (MFU) ceilings unless models adhere to hardware-aligned static tensor shapes ``.
  * **Precision Lag (v7) & Packaging Constraints:** Ironwood's lack of native FP4 constrains quantized MoE throughput until 8th-gen ``, while CoWoS-S capacity bottlenecks cut 2026 unit expectations ``.
* **Scientific Grounding Assessment:** **TPU v5e–v7 Ironwood stand on very solid scientific and engineering ground**, backed by 11 years of production deployment, independent academic telemetry (`arXiv:2604.10852`), and SemiAnalysis/Inferact benchmarks ``. **TPU 8th-gen (8t/8i/8tx/8i Max) and external multi-vendor chassis claims remain unverified by independent third-party tests as of Nov 18, 2026** ``.

---

## 5. Amazon's Chip Unit — Annapurna Labs (Division of Amazon / AWS)

### A. Factual Profile

* **Products & Stage:**
  * **AWS Trainium2 (Trn2):** 5nm, 1.3 PFLOPS FP8, 96 GB HBM; deployed in massive volume (~1M chips serving Anthropic, including 500k-chip Project Rainier in Indiana live since Oct 2025); "largely sold out" ``.
  * **AWS Trainium3 (Trn3) & Trn3 UltraServers:** Annapurna's first **TSMC 3nm (N3P)** AI chip; unveiled and launched into **General Availability Dec 2, 2025** at re:Invent ``. Eight NeuronCore-v4 cores delivering **2,517 TFLOPS (2.52 PFLOPS) MXFP8 / MXFP4**, 671 TFLOPS BF16/FP16, 144 GiB HBM3e at 4.9 TB/s, NeuronLink-v4 at 2.56 TB/s/device; scales to 144 chips per Trn3 UltraServer (362 FP8 PFLOPS, 20.7 TB HBM3e) ``. Nearly fully subscribed in 2026 ``.
  * **AWS Inferentia / Inferentia2:** Inference-focused line (2018–2023); now secondary as Trainium serves both training and inference ``.
  * **Adjacent Silicon:** **AWS Graviton** (Arm server CPUs up to 192-core **Graviton5** announced Dec 2025; 98% of top 1,000 EC2 customers) and **AWS Nitro** (7 generations up to 1,600 Gbps, inside every AWS server since 2015) ``.
  * **Upcoming:** **Trainium4** (announced Dec 2025; targeted 2027 deliveries; promising ≥6× FP4, ≥3× FP8, 4× memory bandwidth, 8 HBM4 stacks / ~288 GB, plus **NVIDIA NVLink Fusion** and **NVHBM** support) ``. On Oct 29, 2026, CEO Andy Jassy announced plans to **sell Trainium chips externally outside AWS starting in late 2027** ``.

* **Technology & Roadmap with Dates:**
  * Annapurna Labs acquired Jan 2015 (~$350M) `` → Inferentia (2018) → Trainium1 (2020/2022) → Trainium2 (2024/2025) → Trainium3 GA (Dec 2, 2025) → **TorchNeuron** native PyTorch backend public beta (Neuron 2.33.0, Oct 19, 2026) and **vLLM Neuron** (July 2026) `` → Trainium4 & External Trainium sales (2027) ``.

* **Past Milestones Met or Missed:**
  * *Met:* Deployed ~1M Trainium2 chips incl. 500k-chip Project Rainier (Oct 2025) ``; launched Trainium3 GA Dec 2025 ``; eliminated legacy XLA `xm.step()` boilerplate via TorchNeuron in Oct 2026 ``.
  * *Missed / Friction:* Marvell lost the Trainium3 design bakeoff to Alchip ``; SemiAnalysis rated AWS "Silver" on ClusterMAX 2.0 (noting Slurm/Kubernetes operational headaches) ``; full `LNC=8` NeuronCore virtualization slipped to mid-2026 ``; Trainium3 delivers identical raw TFLOPS for MXFP4 and MXFP8 (lacking NVFP4 advantage) ``; and key Annapurna AI chip director **Rami Sinno** departed for Arm in Aug 2025 (followed by another Annapurna leader, Hutt, in early 2026) ``.

* **Revenue, Margins, Cash, Debt & Funding:**
  * *Standalone Annapurna Labs / Trainium:* Amazon does **not** disclose standalone Annapurna Labs or Trainium-only revenue, margins, cash, or debt ``.
  * **Combined Custom Silicon Run Rate:** Passed **$20B** annualized in Q1/May 2026 and **$25B+** annualized in July 2026 (growing triple-digits YoY, but **includes Graviton CPUs and Nitro cards alongside Trainium**) ``. Trainium revenue commitments exceeded **$225B** as of April/May 2026 ``.
  * **AWS & Amazon Consolidated Q3 2026 (ended Sept 30, 2026, reported Oct 29, 2026):** Amazon net sales $201.944B (+12% YoY); consolidated operating income $28.076B (record 13.9% margin); net income $20.685B ``. **AWS revenue $45.984B** (+39.3% YoY, $184B annual run rate); **AWS operating income $17.773B** (**38.7% margin**, up from 34.6% YoY; CFO Olsavsky cautioned AI services carry lower margins than legacy cloud) ``.
  * **Cash, Debt & CapEx (Sept 30, 2026):** Cash & marketable securities **$114.2B**; **Long-term debt $173.125B** (up from $65.648B at Dec 2025, after issuing $48.1B long-term debt in Q3 alone) ``; Q3 PP&E purchases $77.26B (+120% YoY), 2026 cash CapEx guidance **~$220B** (raised from $200B on memory inflation, rising further in 2027); **TTM FCF -$42.357B** (vs +$14.8B a year prior); total backlog $578B ``.

* **Customers & Contracts:**
  * **Anthropic:** Project Rainier (~500k–1M Trainium2 chips); April 20, 2026 expanded pact for **>$100B over 10 years** (`$110B` in Anthropic S-1 ``) and up to **5 GW** across Trainium2–Trainium4; Amazon equity commitments up to $33B (`$8B` deployed 2023–2025, $5B + up to $20B milestone-linked) ``.
  * **OpenAI:** Q1 2026 commitment for ~2 GW Trainium capacity ramping 2027 `` (Amazon also invested $21.3B in OpenAI post-June 30 ``).
  * **Other:** **Uber** (Trainium3), **Decart** (real-time video), **Poolside**, **Karakuri**, **Meta** (multi-billion-dollar Graviton5 deal, Apr 2026), **Cerebras** (disaggregated inference: Trainium3 prefill + CS-3 decode), and **Qualcomm** (multi-generation custom silicon/optical deal, up to $60B ceiling reported Sept 2026) ``.

* **Capacity:**
  * Top-5 to top-10 **TSMC** customer (N5/N3P); **Alchip** won Trainium3 physical design partner role over Marvell ``. System ODMs include Quanta, Foxconn, Accton, Wistron ``. Also contracted **Qualcomm** and **3M+ total NVIDIA GPUs** for AWS cloud capacity ``.

* **Ownership & Key People:**
  * Wholly owned subsidiary of Amazon.com, Inc. (NASDAQ: AMZN) ``. Amazon CEO: **Andy Jassy**; AWS CEO: **Matt Garman**; AWS AI Head: **Peter DeSantis**; Annapurna Labs co-founder & AWS VP/Distinguished Engineer: **Nafea Bshara**; Lead Architect: **Ron Diamant**; co-founded with **Hrvoje Bilic** and **Ronen Boneh** (`Rami Sinno` departed Aug 2025 to Arm) ``.

* **Legal & Regulatory Matters:**
  * **Export Controls:** Cloud-only access prevented physical Trainium diversion, though BIS's Nov 15–16, 2026 remote-access rule (`RIN 0694-AK50`) now requires due diligence and licensing if any AWS overseas data center supplies >12M TPP to Chinese/D:5-headquartered entities ``.
  * **Anthropic S-1 Risk Disclosure:** Anthropic flagged conflicts of interest from AWS being simultaneously investor, cloud supplier, and rival model provider ``.

* **Could Not Find / Verify:**
  * Standalone Trainium revenue (isolated from Graviton/Nitro), operating margins, cash, or debt; official Trainium3 TDP (~1,000W is third-party cited ``); Trainium4 final specs, process node, or firm GA date; independent peer-reviewed MLPerf results for Trainium2 or Trainium3; pricing/terms for late-2027 external Trainium sales ``.

### B. Scientific & Engineering Examination

* **Demonstrated:** Massive cost-per-TCO systolic/vector/scalar engine co-design (`NeuronCore-v4` with embedded GPSIMD, stochastic rounding, and 16 collective-communication CC-Cores) plus `NeuronLink` all-to-all scale-up fabrics (`2.56 TB/s` per Trainium3 device) ``. Operationally proven at ~1M-chip scale for Anthropic Claude training and inference ``.
* **External Verification:**
  * **SemiAnalysis (Oct 23, 2026 & Dec 4, 2025):** Hands-on testing of physical Trainium3 racks verified major progress with **TorchNeuron** (native PyTorch eager mode & `torch.compile`) and an 80,000-core automated CI fleet ``.
  * **Customer Testimony:** Anthropic Head of Compute James Bradbury and customers Decart/Karakuri publicly confirmed large-scale production training/inference deployments ``.
* **Unproven:** **Independent standardized benchmarks**—AWS has not submitted Trainium2 or Trainium3 to MLPerf Training/Inference v6.1, nor was Trainium included in Harvard/Meta's `arXiv:2604.10852` ``. Trainium4's 6× FP4 / 3× FP8 / NVLink Fusion / NVHBM integration exists only on roadmaps ``.
* **Physical & Engineering Limits:**
  * **Precision & Quantization Bottleneck:** Trainium3 uses OCP MXFP4 (block size 32, E4M3 scale) with identical peak FLOPS to MXFP8 (`2,517 TFLOPS`), missing NVFP4's (block size 16) 2× compute multiplier over FP8 ``.
  * **Compiler / Ecosystem Friction:** SemiAnalysis explicitly hit bugs during hands-on Trainium3 testing in Oct 2026 and noted Neuron SDK remains "nowhere close to the maturity of the CUDA ecosystem" ``.
  * **Architectural Lock-In vs Portability:** Selling Trainium externally in 2027 requires porting Neuron/NKI tooling outside AWS's proprietary Nitro/EFA control plane ``.
* **Scientific Grounding Assessment:** **Trainium2 and Trainium3 stand on solid systems-engineering ground inside AWS's own cloud for large, engineering-rich tenants (chiefly Anthropic)**, verified by 1M-chip scale and SemiAnalysis rack testing ``. However, **peer-reviewed open benchmarking is absent**, and **Neuron SDK maturity plus Trainium4's NVLink Fusion/external hardware pivot remain unproven in the field** ``.

---

## 6. Huawei Technologies — Ascend Unit (HiSilicon / Computing Product Line)

### A. Factual Profile

* **Products & Stage:**
  * **Ascend 910B:** SMIC N+2 (7nm DUV multi-patterning), shipped 2022–2025 ``.
  * **Ascend 910C:** Dual-die 910B package (SMIC N+2 + stockpiled TSMC/Korean HBM), ~780 TFLOPS BF16, 128 GB HBM2e at 3.2 TB/s, ~310W; in volume deployment in **CloudMatrix 384 / Atlas 900 A3 SuperPoD** (384 chips, ~300 PFLOPS dense BF16, 49.2 TB HBM, ~559–560 kW) ``.
  * **Ascend 950 Series (950PR & 950DT):** Unveiled Sept 18, 2025; **950PR** (inference prefill/recommendation, 1 PFLOPS FP8 / 2 PFLOPS FP4, 128 GB Huawei **HiBL 1.0** memory at 1.6 TB/s) entered reported mass production in Q1/March 2026; **950DT** (decode/training, 144 GB **HiZQ 2.0** memory at 4 TB/s) scheduled Q4 2026 ``.
  * **Upcoming:** **Ascend 960** (Q4 2027, 2× compute/bandwidth/capacity, 288 GB HBM, proprietary **HiF4** 4-bit format, Atlas 960/960E SuperPoD up to 15,488 chips with Near-Packaged Optics / UnifiedBus scaling to 1M NPUs); **Ascend 970** (Q4 2028) ``. *(Note: Earlier reported 910D quad-chiplet / 920C 6nm variants appear superseded or absorbed into the 950–970 roadmap ``.)*

* **Technology & Roadmap with Dates:**
  * Ascend 310 (2018) → 910 (TSMC 7nm, 2019) → 910B (2022) → 910C & CloudMatrix 384 (Mar–Aug 2025) → First public 3-year roadmap unveiled Huawei Connect **Sept 18, 2025** `` → 950PR (Q1 2026) → 950DT (Q4 2026) → Atlas 960E / UnifiedBus unveiled **Sept 17, 2026** `` → Ascend 960 (Q4 2027) → Ascend 970 (Q4 2028) ``.
  * **Software:** **CANN** (Compute Architecture for Neural Networks) + **MindSpore**; Huawei committed to open-sourcing CANN (2025–2026) and integrating official **PyTorch** backend support (`4M+` Ascend/Kunpeng developers claimed ``). DeepSeek open-sourced `TileLang-Ascend` and `DeepGEMM-Ascend` on Sept 30, 2026 ``.

* **Past Milestones Met or Missed:**
  * *Met:* Deployed CloudMatrix 384 commercially across Huawei Cloud and Chinese hyperscalers ``; shipped 572,000 data-center AI accelerators in China in H1 2026 (up from 300k+ in H1 2025, lifting China unit share to 28% vs NVIDIA's 34% per IDC ``); achieved Day-0 inference support for DeepSeek V4 ``.
  * *Missed / Bottlenecked:* Reported Ascend 910C yields at SMIC are only **20%–40%** (80% 910B dies binned down ``); 2025–2026 shipments heavily depended on an illicit pre-ban stockpile of **~2.9M TSMC 7nm dies** obtained via Sophgo and stockpiled Korean HBM exhausting in 2026 ``; DeepSeek V4-Pro API throughput remained compute-constrained pending 950 supernodes ``.

* **Revenue, Margins, Cash, Debt & Funding:**
  * *Standalone Ascend / HiSilicon:* Huawei does **not** report audited standalone Ascend chip revenue, margins, or balance sheet ``. *Financial Times* (May 2026) reported Huawei expects **~$12B AI chip revenue in 2026** (up 60% from ~$7.5B in 2025), which Reuters could not independently verify ``.
  * **Huawei Group FY2025 (year ended Dec 31, 2025, reported Mar 31, 2026, IFRS):** Total revenue **CNY 880.941B ($126.018B** at 6.9906 CNY/USD, +2.2% YoY; ICT Infrastructure CNY 375.014B, Cloud Computing CNY 32.161B external / CNY 72.075B incl. internal); operating profit **CNY 96.937B ($13.867B, 11.0% margin)**; net profit **CNY 68.036B ($9.732B)**; R&D **CNY 192.3B** (21.8% of revenue); OCF CNY 127.384B ($18.222B); cash & short-term investments **CNY 361.426B ($51.702B)**; total borrowings **CNY 239.284B ($34.229B)**; equity CNY 600.120B ($85.847B) ``.
  * **Huawei H1 2026 (reported Aug 31, 2026):** Revenue CNY 467.82B (+9.6% YoY); net profit plunged 36% YoY to CNY 23.81B as R&D surged 25% YoY to **CNY 121.38B** (25.9% of revenue) ``.

* **Customers & Contracts:**
  * Domestic Chinese hyperscalers and AI labs: **Alibaba, Tencent, ByteDance, Baidu, DeepSeek** (bulk orders for Ascend 950 and CloudMatrix 384 systems following DeepSeek V4 release Apr 2026), plus Chinese SOEs/telecoms and Huawei Cloud ``.

* **Capacity:**
  * **Foundry:** **SMIC** N+2 / N+3 (DUV multi-patterning / SAQP; SMIC Q3 2026 revenue record $3.19B at **97.3% capacity utilization**, 90.8% China revenue; advanced capacity ~45k wpm in 2025 toward ~60k wpm in 2026 ``).
  * **Memory:** Transitioning from exhausting pre-control SK Hynix/Samsung HBM2e/3 stockpiles to domestic **CXMT** (targeting 20% HBM3 line share in 2026) and Huawei's custom **HiBL 1.0 / HiZQ 2.0** ``. Epoch AI models ~1.5M Ascend units in 2026 (WSJ/Bloomberg cited 600k 910C + ~750k 950PR plans, while Nodvolt estimates HBM caps output below wafer capacity) ``.

* **Ownership & Key People:**
  * Private company wholly owned by employees via the **Union of Huawei Investment & Holding Co., Ltd.** and founder **Ren Zhengfei** (no outside or government equity disclosed in annual report ``).
  * Key leaders: Rotating Chairs **Meng Wanzhou (Sabrina Meng)**, **Xu Zhijun (Eric Xu)**, **Hu Houkun (Ken Hu)**, **Wang Tao (David Wang)**; Board Chair **Liang Hua**; Huawei Cloud CEO **Zhang Ping'an**; HiSilicon President & non-voting BOD Exec Committee attendee **He Tingbo** ``.

* **Legal & Regulatory Matters:**
  * **U.S. Export Controls & Sophgo Evasion:** Entity-listed since 2019; cut off from TSMC EUV/advanced nodes and foreign HBM ``. TSMC was fined **$1B** over ~2.9M 7nm dies fabricated for Huawei via Cayman shell **Sophgo** ``. On **May 13, 2025**, BIS issued global guidance warning industry that using Huawei Ascend chips (910B/910C/910D) anywhere risks violating U.S. export regulations ``.
  * **DOJ Brooklyn Criminal Trial (Sept–Nov 2026):** Huawei stands trial in E.D.N.Y. before Judge Ann Donnelly on **12 criminal counts** (racketeering conspiracy, bank/wire fraud, money laundering, obstruction of justice, trade-secret theft, IEEPA Iran sanctions); closing arguments ended **Nov 17, 2026**, with **jury deliberations beginning Nov 18, 2026** ``.

* **Could Not Find / Verify:**
  * Audited Ascend/HiSilicon standalone revenue, gross margin, or R&D split; SMIC's exact N+2/N+3 wafer allocation and die yields for Ascend 910C/950PR ``; true domestic manufacturing origin and stack count of Huawei's HiBL 1.0 / HiZQ 2.0 HBM; independent benchmarks of Atlas 950/960E or DeepSeek V4 pre-training hardware; Brooklyn criminal trial jury verdict (pending as of Nov 18, 2026).

### B. Scientific & Engineering Examination

* **Demonstrated:** Huawei compensates for lagging per-die lithography by substituting **system-level optical interconnect engineering** (**CloudMatrix 384 / Atlas 900 A3**: 384 Ascend 910C chips linked in an all-to-all optical mesh across 16 racks using UnifiedBus, achieving 300 PFLOPS dense BF16 and 49.2 TB HBM vs GB200 NVL72's 180 PFLOPS and 13.8 TB) ``. Successfully executed DeepSeek V4-Flash/Pro Day-0 inference and full-parameter post-training at **34.22% MFU** in a July 22, 2026 arXiv study ``.
* **External Verification:**
  * **SemiAnalysis (Apr & Sept 2025, June 2026):** Independently modeled CloudMatrix 384's system-level topology and power trade-offs (~559 kW vs 145 kW) and performed physical teardown of **SMIC N+3**, concluding it is "densified 7nm, not real 5nm" ``.
  * **IDC (Oct 14, 2026):** Independently tracked 572,000 Ascend unit shipments in China in H1 2026 ``.
  * **Epoch AI (Sept 2026):** Independently modeled memory supply channels vs Huawei's ~1.5M chip target ``.
* **Unproven:** Whether Huawei/SMIC/CXMT can manufacture **Ascend 950DT, 960, and 970** with purely domestic HiBL/HiZQ HBM at competitive yields without TSMC/Korean stockpiles ``; whether **Atlas 950/960 SuperPoDs** (8,192–15,488 chips) achieve stability in frontier pre-training (`DeepSeek V4-Pro` pre-training hardware remains undisclosed, and Tsinghua's Liu Zhiyuan noted NVIDIA likely trained it ``); and independent validation of `TileLang-Ascend` kernel parity ``.
* **Physical & Engineering Limits:**
  * **DUV Multi-Patterning (SAQP) Economics & Yield:** Without ASML EUV tools, SMIC relies on Self-Aligned Quadruple Patterning on 193i DUV, multiplying mask layers, overlay errors, cycle time, and defect density—capping large-die AI yields at ~20%–40% ``.
  * **No Hybrid Bonding / HBM Packaging Chokepoint:** Lack of leading-edge hybrid bonding at scale and restricted Japanese EUV/ArF photoresists limit HBM density and logic-memory integration ``.
  * **Power & Thermal Efficiency:** CloudMatrix 384 is **2.3× less power-efficient per FLOP** than GB200 NVL72 (~559 kW vs 145 kW) ``.
* **Scientific Grounding Assessment:** **CloudMatrix 384's optical scale-up engineering stands on solid systems ground as a brute-force silicon workaround** (validated by SemiAnalysis modeling, 572k H1 2026 unit shipments, and DeepSeek V4 inference/post-training deployment) ``. However, **frontier pre-training parity and the 2026–2028 domestic Ascend 950–970 roadmap do not yet stand on verified domestic silicon/HBM proof**, due to DUV yield ceilings, exhausting TSMC/Korean stockpiles, and absent independent hardware verification ``.

---

## 7. Cerebras Systems, Inc.

### A. Factual Profile

* **Products & Stage:**
  * **CS-3 / Wafer-Scale Engine 3 (WSE-3):** 46,225 mm² uncut monolithic TSMC 5nm wafer, 4 trillion transistors, 900,000 AI cores, **44 GB on-chip SRAM** (21 PB/s memory bandwidth, 125 PFLOPS sparse AI compute, ~23 kW system TDP, plus external **MemoryX** DRAM store up to 1.2 PB and **SwarmX** fabric) ``. Shipping in volume for on-prem appliances (67 clusters / >160 systems deployed) and Cerebras Cloud ``.
  * **CS-4 / Wafer-Scale Engine 4 (WSE-4):** Announced in Nov 2026 IPO/Q3 filings & press; **TSMC 3nm**, 2× compute, **>2× on-chip SRAM (~90+ GB)**, 2× memory bandwidth vs WSE-3; initial **pre-production systems scheduled for shipment in late 2026** for cloud deployments ``.
  * **Upcoming:** **CS-5 / WSE-5** (early development, targeted 2028) ``.
  * **Software / Cloud:** **CSTorch** (PyTorch interface compiling to static dataflow), **Cerebras Inference Cloud** (expanding toward 1 GW across 6 data centers; notably also uses **AMD GPUs** and **AWS Trainium3** for prefill in disaggregated inference deals) ``.

* **Technology & Roadmap with Dates:**
  * WSE-1 / CS-1 (TSMC 16nm, 2019) → WSE-2 / CS-2 (TSMC 7nm, 2021) → **WSE-3 / CS-3** (TSMC 5nm, unveiled Mar 13, 2024; shipping 2024–2026) `` → **WSE-4 / CS-4** (TSMC 3nm, pre-production shipments late 2026) `` → **WSE-5 / CS-5** (2028) ``.
  * **IPO:** Went public on NASDAQ (`CBRS`) in **May 2026** (`$6.4B` gross proceeds; `$6.233B` net proceeds recorded in Q3 10-Q cash flow statement) ``.

* **Past Milestones Met or Missed:**
  * *Met:* Completed May 2026 IPO after resolving 2024–2025 CFIUS/G42 friction ``; deployed >160 CS-3 systems across 67 clusters and scaled cloud capacity ``; signed OpenAI (750 MW), AWS, AMD, and Microsoft deals ``.
  * *Missed / Headwinds:* Experienced **data center delivery delays in Q3 2026**, requiring RPO delay-compensation deductions (`"expected reductions in future billings due to data center delivery delays"`) ``; previously relied heavily on G42 (87% of H1 2024 revenue, triggering 2024–2025 IPO postponement) ``; **Q3 2026 GAAP hardware gross margin fell to 11.0%** (from 42.3% a year earlier) due to customer-warrant amortization and pass-through hardware ``.

* **Revenue, Margins, Cash, Debt & Funding:**
  * **FY2025 (reported in IPO filing):** Revenue **$510M** (+76% YoY) ``.
  * **Q3 2026 (ended Sept 30, 2026, reported Nov 12, 2026 via Form 8-K):**
    * **GAAP Revenue:** **$210.809M** (+55% YoY; Hardware $68.881M, Cloud & other $141.928M).
    * **Core (Non-GAAP) Revenue** *(adds back $20.064M non-cash OpenAI warrant amortization)*: **$230.873M** (+70% YoY; Hardware $85.959M, Cloud & other $144.914M) ``.
    * **Gross Margin:** **GAAP 20.0%** (Hardware 11.0%, Cloud & other 24.3%); **Core (Non-GAAP) 41.0%** (Hardware 31.0%, Cloud & other 46.9%) ``.
    * **Operating & Net Income:** GAAP Operating Loss **-$224.149M** (-106.3% margin, incl. $147.8M SBC + $20.1M warrant amortization + $12.3M depreciation/warrant adjustments); Core Operating Loss **-$33.108M** (-14.3% margin). GAAP Net Loss **-$161.218M**; Core Net Income **+$29.823M** ``.
    * **9M 2026 Cash Flow:** OCF **-$388.859M**; CapEx **-$1,046.091M** (`-$1.05B` cloud buildout) ``.
  * **Cash, Debt & RPO (Sept 30, 2026):** Cash, cash equivalents, restricted cash, and short/long-term investments total **$7.805B** ($3,074.8M cash/equiv + $444.0M restricted cash + $4,286.0M investments) ``. Working capital loan **$829.1M** ($706.5M current + $122.6M non-current, drawn from OpenAI's $1.005B loan agreement); operating lease liabilities $621.1M; unused revolving credit facility $850M ``. **RPO $26.1B** as of Sept 30, 2026 ``.
  * **Guidance (Nov 12, 2026):** Q4 2026 Core revenue $310–$330M; FY26 Core revenue $940–$960M (implies >$1B GAAP/Core run-rate entering 2027) ``.

* **Customers & Contracts:**
  * **OpenAI:** Multi-year **750 MW** compute deal starting 2026 through 2028 ($10B+ reported value; also invested $1.014B in Series H, extended $1.005B working capital loan, and holds **33.4M warrants** vesting on MW milestones) ``.
  * **AWS (Announced Oct 2026):** Disaggregated inference via Amazon Bedrock (Trainium3 prefill + CS-3 decode) ``.
  * **Microsoft (Announced Nov 12, 2026):** Strategic cloud partnership adding 6 data centers / 1 GW capacity ``.
  * **Other:** **AMD** (disaggregated inference, July 2026), **IBM** (4096-qubit Quantum error decoding / Granite training, July 2026), **Meta** (Llama API partner), **Mistral**, **Perplexity**, **GLP-1 / BioPharma** ($38M contract), **National Energy Technology Laboratory (NETL)**, **Argonne National Lab**, **Aleph Alpha**, **Sandia**, **G42** (non-controlling shareholder; dropped to minor share in 2026) ``.

* **Capacity:**
  * **Foundry & Assembly:** 100% single-sourced on **TSMC** (5nm for WSE-3, 3nm for WSE-4) with Cerebras's proprietary micro-bump/interconnect packaging in Fremont/San Jose and **6 U.S. manufacturing facilities** (10× system capacity expansion in 2026) ``. Supplying 150 MW by end-2026, targeting 1 GW across 6 data centers by 2028 ``.

* **Ownership & Key People:**
  * Publicly traded (NASDAQ: CBRS, May 2026 IPO) ``. Co-founder & CEO: **Andrew Feldman**; Co-founder & CTO: **Sean Lie**; CFO: **Alex Ippoliti**; VP Hardware Engineering: **Dhiraj Mallick**; Board includes Benchmark, Eclipse, Coatue, Altimeter, Fidelity, OpenAI ``.

* **Legal & Regulatory Matters:**
  * **CFIUS Resolution:** G42 (UAE) agreed to divest/restructure its non-voting stake below regulatory thresholds to clear CFIUS review ahead of the May 2026 IPO ``.
  * **Export Controls:** All CS-2/CS-3 systems exceed BIS TPP thresholds; restricted from China/D:5 and subject to Nov 15–16, 2026 third-country/remote-access licensing ``.
  * **Culper Research Short Report & Rebuttal (Oct–Nov 2026):** On **Oct 26, 2026**, short-seller Culper Research published a report alleging CS-3 wafers suffer fatal electromigration/TDDB failure within ~12 months due to thermal/voltage stress and citing wafer delamination/decommissioning ``. On **Nov 5, 2026**, Cerebras issued a detailed technical rebuttal (with Feldman's statement) asserting fleet junction temperatures average `<65°C` (`85°C` max, well below TSMC's `105°C` 10-year spec), `<0.5%` wafer decommissioning since 2024 across >160 systems, and zero delamination failure mode on continuous wafer-scale copper interconnect ``. No SEC enforcement or class-action judgment exists as of Nov 18, 2026.

* **Could Not Find / Verify:**
  * Independent physical telemetry verifying fleet-wide CS-3 `<65°C` junction temperatures, `<0.5%` wafer decommissioning rate, or TSMC's specific 10-year qualification certificate for uncut 46,225 mm² wafers ``; exact financial terms/MW split of the Nov 12, 2026 Microsoft cloud deal ``; exact dollar size of Q3 2026 OpenAI delay-compensation RPO adjustments ``; WSE-4 manufacturing yield or unit economics.

### B. Scientific & Engineering Examination

* **Demonstrated:** Eliminating off-wafer SerDes/PCIe/HBM boundaries keeps weights and activations in **44 GB on-chip SRAM** at **21 PB/s** (`100×–1,000×` HBM bandwidth), driving ultra-low single-request decode latency for models that fit across one or a cluster of WSE-3 wafers (e.g., 2,000–2,500+ tok/s on Llama 3.1/3.3 70B and Qwen 32B) ``. Proven physically by external labs (Argonne, NETL) and commercial cloud customers (Mistral, Perplexity) ``.
* **External Verification:**
  * **Harvard / Meta ISPASS 2026 (`arXiv:2604.10852`, Apr 12, 2026):** Conducted direct physical benchmarking of a **Cerebras CS-3** (with external Fluke electrical power clamping and API instrumentation). Verified `4.8×` to `24.6×` lower latency per token on Llama 3.1 8B/70B and GPT-OSS-120B at low concurrency vs 8×H100/MI300X, and `3.3×` better energy-per-token at small batch sizes (batch 1) when at high duty cycle ``.
  * **Artificial Analysis & Argonne/NETL:** Independently confirmed >2,000 tok/s decode speeds on Cerebras Inference Cloud and sustained scientific CFD/MD runs ``.
* **Unproven:** **10-year wafer-scale thermomechanical reliability** under continuous commercial load (Culper vs Feldman claims remain unverified by an independent materials-science audit ``); **WSE-4 (3nm)** yield, power density, and >90 GB SRAM performance in customer hands ``; and standalone large-batch prefill competitiveness (which Cerebras itself bypassed via AMD/AWS prefill deals ``).
* **Physical & Engineering Limits:**
  * **Static High Idle Power (Harvard/Meta ISPASS 2026):** Physical Fluke measurements proved CS-3 draws **80% of its 23 kW TDP (~18 kW) while completely idle** and **100% during decode** (because all 900,000 SRAM-coupled cores remain powered at fixed frequency)—requiring a **≥34% active duty cycle** just to match a 32-GPU H100 cluster in energy-per-token ``.
  * **44 GB Per-Wafer Memory Ceiling & Batch Scaling:** Models >44 GB require multi-wafer sharding or slower external MemoryX DRAM; at higher batch sizes, CS-3 falls off the throughput-per-watt Pareto frontier relative to HBM-equipped GPUs/TPUs ``.
  * **Thermomechanical Stress & Telemetry Opacity:** Coupling a 46,225 mm² silicon wafer (CTE ~2.6 ppm/°C) to large organic/metallic cold-plate assemblies creates cyclical mechanical stress governed by Coffin-Manson fatigue, while `arXiv:2604.10852` documented that Cerebras APIs abstract away internal power and kernel telemetry (requiring sudo PDU access) ``.
* **Scientific Grounding Assessment:** **CS-3's ultra-low-latency SRAM decode physics stands on solid, independently measured scientific ground** (`arXiv:2604.10852`, Argonne, Artificial Analysis) **specifically for small-batch, high-duty-cycle decode and stencil physics**. Conversely, **CS-3 is scientifically disadvantaged at low utilization (80% idle power floor), large-batch prefill, and multi-terabyte parameter models**, and **long-term wafer-scale thermal durability and WSE-4 (3nm) yields remain unverified by independent engineers** ``.

---

## 8. Cross-Examination & Contradiction Ledger

Testing every major company assertion against customers, suppliers, competitors, regulators, published papers, and the other six companies exposes **eight major contradictions**:

| # | Company Claim | Contradicting Source(s) | Exact Contradiction & Evidence |
|---|---|---|---|
| **1** | **NVIDIA:** "Our roadmap is on track" (Nov 17, 2026) and NVFP4/Rubin extend structural cost/margin leadership ``. | SemiAnalysis, CNBC, supply-chain teardowns, **and NVIDIA's own Q3 FY27 filing** ` | Multiple engineering/supply-chain reports (Mar–Jul 2026) state the original 4-die Rubin Ultra was scrapped/halved to 2 dies over CoWoS-L warpage and Kyber NVL144 slipped 12+ months to 2028 over 78-layer PCB midplane flaws (which NVIDIA denied) `</br>` Meanwhile, NVIDIA's own Q4 FY27 guidance cut gross margin **300–400 bps (74.9% → 71%–72%)** due to HBM/DRAM inflation, while AR hit $81.0B (DSO 64 days) and off-balance-sheet guarantees reached $118B ``. |
| **2** | **NVIDIA:** >99% of Singapore-billed controlled compute served U.S. customers; China DC compute is minimal ($0 Q4 guide); Jensen Huang offered on Nov 17 to return as CEO ` | **BIS, DOJ, U.S. House Committees, SEC, and NVIDIA's own Board Chair** ` | U.S. intelligence/DOJ/House probes allege Megaspeed imported $4B+ (240,000 chips) tied to Chinese diversion; SEC opened a civil disclosure probe (Nov 17, 2026); BIS issued the Nov 15–16, 2026 rule specifically closing the Singapore/SEA/remote-access loophole `</br>` Board Chair Harvey Jones explicitly ruled out Huang's return as CEO despite Huang's public Nov 17 post ``. |
| **3** | **AMD:** MI455X outperforms Vera Rubin by **+30%** (21,333 tok/s/GPU on DeepSeek-R1) and Helios/MI450 is shipping/on target in H2 2026 ``. | **MLCommons v6.1, AMD's own Form 10-Q, Jon Peddie Research, & TensorWave** ` | JPR/Venture Atlas note the 21,333 tok/s score is an **unverified internal AMD Offline lab figure** (ignoring Server latency); AMD did **not** submit MI455X/Helios to MLPerf Training v6.1 (Nov 16) or Inference v6.1 (Sept 16), submitting only MI355X/350 `</br>` AMD's Q3 10-Q/warrant disclosures confirm **zero OpenAI or Meta warrant shares had vested** as of Sept 26, 2026, AMD refused to disclose shipped GW counts, and TensorWave's 457 MW OpenAI MI455X contract does not come online until **H1 2027–2028** `</br>` Separately, OpenAI's Greg Brockman claimed OpenAI compressed 12 months of AMD chip design into 5 months—uncorroborated by AMD ``. |
| **4** | **Broadcom vs Trade Press & Google:** Hock Tan stated (Sept 2, 2026) **Broadcom ships TPU 8i** ahead of **MediaTek's TPU 8t**, and projects **$115B FY27 / $230B FY28** AI semi revenue ` | **Google, SemiAnalysis, JPR, Anthropic S-1, & Broadcom's own 10-Q/8-K** ` | Trade analysts (JPR Dec 2025, *Who Owns AI?* May 2026, InferenceChips Aug 2026) reversed the assignment (claiming Broadcom = 8t, MediaTek = 8i), while **Google refuses to confirm either assignment** and lists 8i as "Coming Soon" while Broadcom claims it is shipping `</br>` SemiAnalysis (Aug 2026) cut 2026 TPU v7 CoWoS forecasts by **500k units** due to CoWoS-S bottlenecks, and Broadcom's $115B–$230B projection relies on **$42B convertible loans** and **$29B–$43B residual-value lease backstops** (which Anthropic's S-1 explicitly flags as a conflict of interest) ``. |
| **5** | **Google:** TPU v7 Ironwood beats GB300 NVL72 at **1.67× perf/$**, and TPU ecosystem is open via TorchTPU for ~100 customers ``. | **Anthropic S-1, Google's own hardware specs & co-design guide, & TPU7x docs** ` | Google's Nov 2026 win compares TPU v7 FP8 against GB300 NVL72 FP4, yet **Ironwood lacks native FP4** (forcing reliance on 8th-gen TPU 8t/8i, which have zero independent benchmarks) ``; Google's own Nov 16 co-design guide admits systolic TPUs require rigid static tensor shapes; and TPU7x **dropped TensorFlow support** `</br>` Moreover, Google's flagship TPU customer **Anthropic** disclosed a 4-silicon hedge ($161.2B Broadcom + $114.5B Google + $110B Amazon + $44.9B Microsoft + >$20B AMD) and flagged conflicts of interest with Google ``. |
| **6** | **Amazon / Annapurna Labs:** Trainium breaks NVIDIA dependence at 30%–50% better price-performance and >$225B commitments ``. | **NVIDIA (NVLink Fusion / NVHBM), Anthropic S-1, SemiAnalysis, & AWS deals with NVIDIA/Cerebras** ` | For **Trainium4**, Annapurna partnered directly with **NVIDIA** to adopt **NVLink Fusion and NVHBM**—making its anti-NVIDIA chip reliant on NVIDIA's interconnect and custom memory-controller ecosystem `</br>` Anthropic committed **$275B+** to Google/Broadcom TPUs ($161.2B Broadcom + $114.5B Google + future est.) vs **$110B to Amazon** `</br>` SemiAnalysis (Oct 2026) hit real software bugs on Trainium3 and found Neuron "nowhere close to CUDA" ``, while AWS simultaneously ordered **3M+ NVIDIA GPUs** and outsourced decode on Bedrock to **Cerebras CS-3** ``. |
| **7** | **Huawei Ascend:** CloudMatrix 384 (300 PFLOPS) surpasses GB200 NVL72 (180 PFLOPS), domestic HiBL/HiZQ HBM powers 950PR/DT, and DeepSeek V4 runs/trains on Ascend ` | **SemiAnalysis teardowns, BIS / TSMC fine, Epoch AI, DeepSeek arXiv paper, & Tsinghua Univ.** ` | Independent modeling proves CloudMatrix 384 requires **5.3× more chips (384 vs 72)** and **3.9× more power (~559 kW vs ~145 kW)**, making it **2.3× worse in FLOP/watt** ``; SMIC N+3 is **densified 7nm** with **20%–40% 910C yields**, and 2025–2026 shipments leaned on **~2.9M illicit TSMC 7nm dies** via Sophgo ($1B TSMC fine) plus exhausting Korean HBM stockpiles `</br>` While Chinese state media touted DeepSeek V4 training on Ascend, the July 22, 2026 arXiv paper covered **post-training only (34.22% MFU)** and Tsinghua's Liu Zhiyuan told *MIT Tech Review* DeepSeek-V4-Pro was likely pre-trained mainly on NVIDIA GPUs ``. |
| **8** | **Cerebras:** Wafer-scale single-system simplicity yields huge efficiency and speed gains over GPUs, backed by a $26.1B RPO ``. | **Harvard/Meta ISPASS 2026 (`arXiv:2604.10852`), Culper Research, Cerebras's own 8-K, & AWS/AMD deals** ` | Harvard/Meta physical Fluke measurements proved CS-3 pulls **80% of TDP (~18 kW) while idle** and **100% during decode**, requiring a **≥34% duty cycle** just to break even with 32 H100s in energy/token, falling off the Pareto curve at large batches, and hiding kernel telemetry `</br>` Because single wafers hold only 44 GB SRAM, Cerebras uses **AMD GPUs and AWS Trainium3** for prefill `</br>` Cerebras's Q3 2026 **GAAP gross margin was 20.0% (11.0% GAAP hardware)** vs **41.0% Core** (adjusted for warrant amortization), and **OpenAI data center delivery delays** in Q3 2026 forced RPO delay-compensation deductions ``. |
