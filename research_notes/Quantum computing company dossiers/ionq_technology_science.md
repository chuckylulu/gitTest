# IonQ: technology, roadmap and science (fact file, current to 14 November 2026)

Source labels used throughout: **CC** = company-controlled (IonQ, its subsidiaries Oxford Ionics / Lightsynq / SkyWater, IonQ-authored papers and blogs, IonQ SEC filings). **IND** = independent publisher (academics, courts, journalists, analysts, cloud-platform documentation). **IND-relay** = independent outlet whose article mainly restates an IonQ release. **COMP** = competitor (independent of IonQ but an interested party). **(excerpt)** = seen only in a search-result excerpt; the page itself was not fetched or was blocked. Research note: the shared web-search budget ran out partway through this task; items that could not be re-checked are flagged and listed under Gaps. All dates are publication dates unless stated; "accessed 14 Nov 2026" means a live page read on that date.

## 1. Products and their stage (Aria, Forte, Forte Enterprise, Tempo, Superion)

### Takeaway
As of 14 Nov 2026, the IonQ machines anyone can rent on public clouds are still the 25-qubit Aria and the 36-qubit Forte and Forte Enterprise. These use ytterbium ions and laser gates, with roughly 99.5–99.6% typical two-qubit fidelity. The fifth-generation barium-based Tempo (IonQ: 100 "target" qubits, #AQ 64 claimed September 2025) is sold for on-premises and private-cloud use and is not listed on AWS or Azure. The sixth-generation Superion 256 (on-chip "Electronic Qubit Control", chips made by IonQ's subsidiary SkyWater) was launched on 8 Sep 2026. Ions have been trapped in prototypes, but no gate or fidelity data have been published, and customer deliveries are planned for 2027.

### Cited Findings
**Aria (cloud)**
- Azure Quantum lists target "IonQ Aria 1" (ionq.qpu.aria-1), 25 qubits. Its average fidelities are: single-qubit 99.95% (SPAM-corrected); two-qubit 99.6% (not SPAM-corrected); SPAM 99.61%. Timings: T1 10–100 s, T2 1 s, single-qubit gate 135 µs, two-qubit gate 600 µs. "Debiasing" error mitigation is on by default for Aria and Forte and is priced. The page says IonQ manipulates "hyperfine energy states of Ytterbium ions with lasers" — [Microsoft Learn (IND platform doc; specs vendor-supplied), "IonQ quantum computing provider – Azure Quantum", ms.date 17 Sep 2025, updated 29 Aug 2026](https://learn.microsoft.com/en-us/azure/quantum/provider-ionq)
- Amazon Braket's device table (accessed 14 Nov 2026) lists only IonQ Forte-1 and Forte-Enterprise-1 (us-east-1). Aria and Tempo are not listed — [AWS (IND platform doc), "Amazon Braket supported regions and devices", accessed 14 Nov 2026](https://docs.aws.amazon.com/braket/latest/developerguide/braket-devices.html)

**Forte / Forte Enterprise (36 qubits, cloud and on-prem)**
- Azure lists Forte 1 and Forte Enterprise 1, each 36 qubits. Forte Enterprise is described as a Forte "adapted and ruggedized for deployment in a standard data center", and "the base quantum computing hardware and performance are the same" — [Microsoft Learn (IND platform doc), 2026](https://learn.microsoft.com/en-us/azure/quantum/provider-ionq)
- Peer-reviewed, IonQ-authored benchmark of Forte. The 30-qubit configuration of a 36-ion chain was used: the optics can address 40 ions, but available photon-detection channels limited the study.
  - Two-qubit direct randomized benchmarking (DRB) error over all 435 pairs: median 46.4×10⁻⁴ (≈99.54% fidelity); 10th percentile 34.5×10⁻⁴; 90th percentile 99.6×10⁻⁴; best pair 27.8×10⁻⁴ (≈99.72%); worst pair 885×10⁻⁴ (≈91.2%). Error bars are 20–40% of values.
  - Median single-qubit DRB error 2.0×10⁻⁴; SPAM error 0.5% per qubit.
  - Single-qubit gate 110 µs; ZZ gate ~900 µs average (770–1,103 µs).
  - #AQ 29 reached with error mitigation.
  - Source: [Chen et al. (IonQ authors; CC, peer-reviewed), "Benchmarking a trapped-ion quantum computer with 30 qubits", Quantum 8, 1516, published 7 Nov 2024 (arXiv v1 9 Aug 2023)](https://quantum-journal.org/papers/q-2024-11-07-1516/pdf/); [arXiv:2308.05071](https://arxiv.org/abs/2308.05071)
- IonQ unveiled the "rack-mounted" Forte Enterprise ("target performance of #AQ 35") and Tempo ("expected to demonstrate record-breaking #AQ 64") on 27 Sep 2023. Then-CEO Peter Chapman said the systems "will lead to commercial advantage within a two-year time frame" — [IonQ (CC), "IonQ Unveils Forte Enterprise and Tempo…", 27 Sep 2023](https://www.ionq.com/news/ionq-unveils-forte-enterprise-and-tempo-rack-mounted-enterprise-grade)
- Forte Enterprise #AQ 36 (first IonQ system in Europe, at QuantumBasel) is listed as December 2024 — [Wikipedia (IND tertiary), "Algorithmic qubits", accessed 14 Nov 2026](https://en.wikipedia.org/wiki/Algorithmic_qubits), citing [IonQ (CC) announcement](https://ionq.com/news/ionq-unveils-its-first-quantum-computer-in-europe-online-now-at-a-record). IonQ's own systems page lists Forte Enterprise as "#AQ 36, 36 qubits" — [IonQ (CC), Tempo/systems page, accessed 14 Nov 2026](https://ionq.com/quantum-systems/tempo)
- IonQ announced global availability of Forte Enterprise via Amazon Braket and IonQ Quantum Cloud on 1 Apr 2025 — [The Quantum Insider (IND-relay), 1 Apr 2025 (excerpt)](https://thequantuminsider.com/2025/04/01/ionq-forte-enterprise-now-globally-accessible-via-amazon-braket-and-ionq-quantum-cloud/)

**Tempo (fifth generation, barium; on-prem / private cloud)**
- IonQ's Tempo page lists "Target qubits: 100", "Target fidelity: 99.9%", #AQ 64 (in the page title), mid-circuit measurement, and a "pre-sales" inquiry route. There is no cloud listing and no ship date — [IonQ (CC), "IonQ Tempo" product page, accessed 14 Nov 2026](https://ionq.com/quantum-systems/tempo)
- On 25 Sep 2025 IonQ announced #AQ 64 on "an IonQ Tempo system… fifth-generation", "three months ahead of schedule". The release does not give the number of qubits used, the error-mitigation settings or any fidelities — [IonQ (CC), "IonQ Achieves Record-Breaking Quantum Performance Milestone of #AQ 64", 25 Sep 2025](https://ionq.com/news/ionq-achieves-record-breaking-quantum-performance-milestone-of-aq-64)
- Other descriptions of the #AQ 64 run differ:
  - An aggregator says it was a Tempo "development system" that reached #AQ 64 "on a 64-qubit computational register" — [Quantum Market Cap (IND aggregator), "Quantum Computing Roadmap 2026", IonQ block "last verified Aug. 15, 2026"](https://quantummarketcap.com/roadmap)
  - PostQuantum also says "Tempo development system", dated October 2025 — [PostQuantum (IND), M. Ivezic, "Quantum Benchmarks: Why Vendor Numbers Don't Compare", 3 Aug 2026](https://postquantum.com/quantum-computing/quantum-computing-metrics-vendor-benchmarks/)
  - QCR headlined a "100-qubit Tempo system" — [Quantum Computing Report (IND-relay), 27 Sep 2025](https://quantumcomputingreport.com/ionq-reaches-aq-64-milestone-on-100-qubit-tempo-system-ahead-of-schedule/)
- Precursor result: ">99.9%" two-qubit fidelity on a two-ion chain on a "barium development platform", framed as a step toward Tempo — [IonQ press release via Silicon UK (CC, sponsored), 12 Sep 2024](https://www.silicon.co.uk/press-release/ionq-achieves-industry-breakthrough-first-trapped-ion-quantum-system-to-surpass-99-9-fidelity-on-barium)
- KISTI (South Korea): the agreement to deliver "Tempo 100", integrated with the KISTI-6 supercomputer and accessed via private cloud, was finalized 23 Dec 2025 — [DCD (IND-relay) (excerpt)](https://www.datacenterdynamics.com/en/news/ionq-finalizes-agreement-with-south-koreas-kisti-for-delivery-of-tempo-quantum-computer/). In August 2026 COO/CFO Inder Singh said KISTI subsystems were "currently being delivered and assembled in Korea at the customer site" — [Yahoo Finance (IND), "IonQ, Inc. Q2 2026 Earnings Call Summary" (excerpt)](https://finance.yahoo.com/markets/stocks/articles/ionq-inc-q2-2026-earnings-123000874.html)
- 2026 earnings releases mention Tempo only in revenue terms:
  - Q1 2026 (6 May 2026) headline: "Demand for Fifth-Generation Tempo Remains Strong" — [IonQ (CC), Q1 2026 results, 8-K Ex. 99.1, 6 May 2026](https://www.sec.gov/Archives/edgar/data/0001824920/000119312526208923/ionq-ex99_1.htm)
  - Q2 (5 Aug 2026) and Q3 (5 Nov 2026) credit "global deployments of our IonQ Tempo quantum computers"; IonQ Platform segment revenue rose 127% to $90.3M in Q3. Neither names Tempo customers or gives specifications — [IonQ (CC), Q2 2026 results, 5 Aug 2026](https://www.sec.gov/Archives/edgar/data/0001824920/000119312526335040/ionq-ex99_1.htm); [IonQ (CC), Q3 2026 results, 5 Nov 2026](https://www.sec.gov/Archives/edgar/data/0001824920/000119312526449779/ionq-ex99_1.htm)
- IonQ says its 2026 breakeven error-correction work ran on a "Tempo engineering test system" — [IonQ (CC), Superion launch release, 8 Sep 2026](https://www.ionq.com/news/ionq-launches-superion-product-line-industry-leading-upgradeable-platform-designed-to-scale-manufacturable-fault-tolerant-quantum-computing). The matching preprint used a stationary chain of 40 ¹³³Ba⁺ ions — [PostQuantum (IND), 5 Jun 2026](https://postquantum.com/quantum-research/ionq-qldpc-breakeven-trapped-ion/)

**Superion 256 / Superion 10K (sixth generation onward; pre-delivery)**
- Superion launch, 8 Sep 2026 [IonQ (CC), "IonQ Launches Superion Product Line…", 8 Sep 2026](https://www.ionq.com/news/ionq-launches-superion-product-line-industry-leading-upgradeable-platform-designed-to-scale-manufacturable-fault-tolerant-quantum-computing). IonQ's statements:
  - Status: IonQ "has fabricated its first fully integrated 256-qubit quantum processing units (QPUs) at its subsidiary SkyWater" and "has trapped the first ions in prototype Superion 256 systems".
  - Technology and fabrication: on-chip Electronic Qubit Control (EQC) replaces laser gate systems. There were six tapeouts in the first half of 2026.
  - Delivery and access: orders are open with "customer deliveries in 2027". Production systems will be offered on IonQ's cloud (no date given).
  - Fault tolerance: "full fault tolerance reality in a 2027 lab setting", with manufacturable commercial systems in 2028.
  - Superion 10K is "well underway", and cryo-CMOS test chips are on display. Cost per qubit is expected to fall by more than 300×.
  - The release gives no Superion gate fidelity, gate speed, coherence or ion species, and does not say any gate has been run on the integrated chip.
- Trade coverage of the launch adds no independent commentary, and its demonstrated-vs-planned split matches the release — [The Quantum Insider (IND-relay), 8 Sep 2026](https://thequantuminsider.com/2026/09/08/ionq-launches-superion-256-quantum-computing-platform/)
- In Q1 2026 IonQ sold its first sixth-generation 256-qubit system, to the University of Cambridge. This was a sale, not a delivery. IonQ also said it had received "first ion trap chip samples back from the fab" and was moving to integrated system-level testing — [IonQ (CC), Q1 2026 results, 6 May 2026](https://www.sec.gov/Archives/edgar/data/0001824920/000119312526208923/ionq-ex99_1.htm)
- Q3 2026 orders [IonQ (CC), Q3 2026 results, 5 Nov 2026](https://www.sec.gov/Archives/edgar/data/0001824920/000119312526449779/ionq-ex99_1.htm):
  - NVIDIA "will deploy" a Superion 256 as the first on-premises quantum computer at its Accelerated Quantum Research Center.
  - SDT: $33M contract covering a Superion 256 and a quantum memory platform.
  - Florida International University: $25M contract for a Superion 256.
- Cloud availability claim: "Our quantum computing services have been available through all major cloud providers since 2021" (boilerplate, Q3 2026 release). Only AWS and Azure listings could be checked (above).

### Inferences
- In Nov 2026 the cloud-accessible IonQ hardware is the same class as in 2023–2025: 25–36-qubit, ytterbium, laser-gate machines. Tempo is being sold on-prem and Superion is pre-delivery. This comes from the AWS and Azure listings plus the absence of Tempo or Superion entries.
- The gap between "median" and "best" is large and should not be blurred. The only peer-reviewed full-device data (Forte, 2023–24) show a median of 99.54%, a best pair of 99.72% and a worst pair of ~91.2%. By contrast, 99.9% is a Tempo target and 99.99% is a two-ion lab result (section 5).
- IonQ's own page still calls Tempo's 100 qubits a "target" 14 months after #AQ 64. No public source shows a 100-qubit Tempo running at its 99.9% target. #AQ 64 needs at least 64 working qubits; the aggregator says a 64-qubit register was used.

### Gaps
- No IonQ-published median or best two-qubit fidelity, SPAM, crosstalk or gate-time data for Tempo or production Forte Enterprise units.
- No Tempo cloud listing found. Google Cloud availability could not be verified.
- Not found: whether the KISTI Tempo is commissioned or accepted, and the number of Tempo units delivered.
- Superion 256 ion species, trap geometry and any gate data are undisclosed.

## 2. Roadmap: current targets, dates, and changes after Oxford Ionics and Lightsynq

### Takeaway
IonQ's roadmap page (undated, read 14 Nov 2026) gives these targets:

| Year | Physical qubits | Logical qubits | Logical error | Notes |
|---|---|---|---|---|
| 2026 | 100–256+ | 12 | <1E-7 | |
| 2027 | 10,000 | 800 | <1E-7 | |
| 2028 | 20,000 | 1,600 | <1E-7 | |
| 2029 | 200,000 | 8,000 | — | first year listing a photonic interconnect |
| 2030 | 2,000,000 | 80,000 | — | |

This physical/logical-qubit plan replaced the #AQ-based plans of 2020–2023. It was introduced in June 2025 around the Lightsynq and Oxford Ionics acquisitions. In 2026 it became the SkyWater-fabricated Superion line, and 256-qubit deliveries are now dated 2027. DARPA's QBI Stage C will check it independently through 2029.

### Cited Findings
- The roadmap table on IonQ's page, as rendered on 14 Nov 2026:

| Year | Physical qubits | Physical fidelity | Logical qubits | Logical error | Listed features |
|---|---|---|---|---|---|
| 2024 | 36+ | 99.6% | — | — | optical gate operations, 1D qubit array |
| 2025 | 64–100+ | 99.9% | — | — | "microwave gate operations", 2D array, mid-circuit measurement, parallel operations |
| 2026 | 100–256+ | 99.99% | 12 | <1E-7 | as 2025 |
| 2027 | 10,000 | 99.99% | 800 | <1E-7 | as 2025 |
| 2028 | 20,000 | 99.99% | 1,600 | <1E-7 | as 2025 |
| 2029 | 200,000 | 99.99% | 8,000 | "<1.00^-12" (sic) | adds photonic interconnect |
| 2030 | 2,000,000 | 99.99% | 80,000 | "<1.00^-12" | as 2029 |

  The page marks no milestone as achieved and carries no last-updated date — [IonQ (CC), "Industry-leading roadmap", accessed 14 Nov 2026](https://ionq.com/roadmap)
- The "accelerated roadmap" of 13 Jun 2025 [IonQ (CC), "IonQ's Accelerated Roadmap: Turning Quantum Ambition into Reality", 13 Jun 2025](https://www.ionq.com/blog/ionqs-accelerated-roadmap-turning-quantum-ambition-into-reality):
  - 2025: "Development systems supporting 100 physical qubits for Tempo".
  - 2027: 10,000 physical qubits on a single chip.
  - 2028: two interconnected chips with 20,000 physical qubits, networking online, and a commercially available interconnected system.
  - 2030: >2,000,000 physical qubits → 40,000–80,000 logical qubits, logical error <1E-12.
  - Oxford Ionics (deal then pending): 2D traps with "up to 300x higher trap density" than projected 1D systems.
  - Lightsynq (deal completed): quantum-memory-based photonic interconnects that "increase the ion-ion entanglement rate by up to 50x" versus memory-less links, making "clustered quantum computing commercially ready by 2028".
- An independent analysis of the June 2025 roadmap [PostQuantum (IND), M. Ivezic, "IonQ's 2025 Roadmap: Toward a Cryptographically Relevant Quantum Computer by 2028", 19 Jun 2025](https://postquantum.com/industry-news/ionqroadmap-crqc/):
  - It records IonQ's statement that the roadmap could yield a cryptographically relevant machine "as early as 2028" (~1,600 logical qubits at ~10⁻⁷).
  - It calls 2028 "aggressive but not guaranteed".
  - It flags several risks: growing from ~100 to 10,000+ qubits in 2–3 years is "unprecedented"; 2D-trap yield; photonic interconnects with "no performance data"; and dependence on the 10⁻⁷ logical-error assumption.
- October 2025: IonQ said the 99.99% EQC lab result would form the basis of 256-qubit systems "scheduled for demonstration in 2026" — [Quantum Computing Report (IND-relay), 21 Oct 2025](https://quantumcomputingreport.com/ionq-achieves-99-99-two-qubit-gate-fidelity-using-electronic-qubit-control-technology/)
- April 2026: IonQ published the "Walking Cat" fault-tolerant architecture (ion-shuttling QCCD + LDPC codes) — [arXiv:2604.19481 (CC), 21 Apr 2026](https://arxiv.org/abs/2604.19481). Superion 10K is "the first hardware" planned to run it — [IonQ (CC), Superion release, 8 Sep 2026](https://www.ionq.com/news/ionq-launches-superion-product-line-industry-leading-upgradeable-platform-designed-to-scale-manufacturable-fault-tolerant-quantum-computing)
- September 2026 Superion timeline: 256-qubit deliveries in 2027; fault tolerance in an IonQ lab in 2027; commercial, manufacturable fault tolerance in 2028; no date for Superion 10K — [IonQ (CC), 8 Sep 2026](https://www.ionq.com/news/ionq-launches-superion-product-line-industry-leading-upgradeable-platform-designed-to-scale-manufacturable-fault-tolerant-quantum-computing)
- Manufacturing claims (all IonQ statements): the SkyWater acquisition closed 31 Jul 2026 — [IonQ (CC), 8-K Ex. 99.1, 8 Sep 2026](https://www.sec.gov/Archives/edgar/data/0001824920/000119312526384388/ionq-ex99_1.htm). The design cycle fell from nine months to two, and wafer-lot output was 12× a previous foundry's over six months — [IonQ (CC), 8 Sep 2026](https://www.ionq.com/news/ionq-launches-superion-product-line-industry-leading-upgradeable-platform-designed-to-scale-manufacturable-fault-tolerant-quantum-computing). The Nexus Photonics acquisition targets integrated photonics and miniaturization — [IonQ (CC), Q2 2026 results](https://www.sec.gov/Archives/edgar/data/0001824920/000119312526335040/ionq-ex99_1.htm)
- DARPA Quantum Benchmarking Initiative (QBI), Stage C, 7 Oct 2026:
  - IonQ's account: an agreement worth "up to $300 million" (subject to appropriations) for "independent verification and validation" of IonQ's fault-tolerant approach "through 2029", covering "multiple Superion generations". IonQ says it completed Stages A and B and shared prototype hardware data with DARPA — [IonQ (CC), "IonQ Advances to Final Stage of DARPA's Quantum Benchmarking Initiative", 7 Oct 2026](https://www.ionq.com/news/ionq-advances-to-final-stage-of-darpas-quantum-benchmarking-initiative)
  - Independent account: DARPA picked Atom Computing, Diraq, IBM and IonQ, who join Microsoft and PsiQuantum. Stage C moves from blueprint audits to physical testing. QBI asks whether hardware can reach "utility scale" by 2033 — [Quantum Computing Report (IND), 7 Oct 2026](https://quantumcomputingreport.com/darpa-selects-atom-computing-diraq-ibm-and-ionq-for-final-stage-c-verification-under-quantum-benchmarking-initiative/)
  - IonQ says it is the only trapped-ion company in Stage C — [IonQ (CC), Q3 2026 results](https://www.sec.gov/Archives/edgar/data/0001824920/000119312526449779/ionq-ex99_1.htm)
- A Nasdaq/Zacks article states that "an independent review confirmed" the parts for a two-million-qubit computer could cost under $30 million in 2025 dollars. The reviewer is not named — [Nasdaq (IND-relay), "IonQ's Quantum Roadmap and Foundry Strategy Through 2030" (excerpt)](https://www.nasdaq.com/articles/ionqs-quantum-roadmap-and-foundry-strategy-through-2030)

### Inferences
- Change of yardstick: the 2020–2023 roadmaps were stated in #AQ (e.g., #AQ 64 in 2025). The June 2025 and later roadmaps are stated in physical and logical qubits and logical error. They rest on acquired technology (Oxford Ionics 2D traps and EQC; Lightsynq memories) and, from 2026, on an owned fab (SkyWater).
- Changes between versions:
  - June 2025 put two photonically interconnected chips in 2028; the current page lists "photonic interconnect" only from 2029.
  - The 2030 logical range of 40,000–80,000 became a flat 80,000.
  - The 256-qubit generation moved from "demonstration in 2026" (Oct 2025) to "customer deliveries in 2027" (Sep 2026).
- Scale of the jumps (arithmetic from the roadmap page): 256 → 10,000 physical qubits from 2026 to 2027 is about 39×; 12 → 800 logical qubits is about 67× in one year.
- DARPA Stage C is the first scheduled third-party verification of the roadmap. No Stage C results exist yet.

### Gaps
- Not determined: when the roadmap page was last changed, and whether the 2027 10,000-qubit target still applies, since the Superion release gives Superion 10K no date.
- No system-level data for the Lightsynq "up to 50x" claim.
- The reviewer behind the "<$30M for 2M qubits" claim is unknown.

## 3. Milestones met, missed, or changed (2020 roadmap, 2021 SPAC era, 2023 product targets, 2025–26 targets)

### Takeaway
IonQ met or beat its own #AQ milestones: #AQ 29 (2023), #AQ 35 (January 2024, "a year ahead") and #AQ 64 (September 2025, "three months ahead"). All were company-measured, with error mitigation and compiler optimization allowed. It did not meet its more physical 2020 commitments:
- Modular systems "networked together in a datacenter" by 2023: rack-mounted Forte Enterprise arrived in 2024–25, and two commercial machines were first linked photonically only in April 2026, with no metrics disclosed.
- #AQ 64 "using 16:1 error-correction encoding" by 2025: #AQ 64 was reached on a ~64–100-qubit machine, which rules out 16:1 encoding (that would need ~1,024 physical qubits). IonQ's release mentions no error correction.
- "Broad quantum advantage" by 2025: there is no evidence it happened. IonQ's 2025 advantage claims are narrow.
- The 2026 target of 256-qubit demonstrations became 2027 deliveries.

### Cited Findings
- December 2020 roadmap, IonQ's words [IonQ (CC), "Scaling IonQ's Quantum Computers: The Roadmap", 9 Dec 2020](https://www.ionq.com/blog/december-09-2020-scaling-quantum-computer-roadmap):
  - The 32-qubit system "is expected to feature 22 Algorithmic Qubits".
  - "By 2023, IonQ will deploy modular quantum computers small enough to be networked together in a datacenter."
  - "by 2025, we expect to achieve broad quantum advantage."
  - A note on the page says an AQ estimator was removed in February 2022 because it did not accurately reflect the metric's definition.
- Contemporary press account of the same roadmap [VentureBeat (IND), 9 Dec 2020](https://venturebeat.com/2020/12/09/ionq-roadmap-quantum-machine-learning-2023-broad-quantum-advantage-2025/):
  - 2023: second next-gen computer with 29 AQ; rack-mounted modular machines networked in a datacenter.
  - 2025: third next-gen computer with 64 AQ "using 16:1 error-correction encoding"; broad advantage "roughly 2024-2025".
  - Later years: 32:1 encoding.
  - Physical qubits to double every 12–18 months.
- FY2021 10-K (SPAC-era filing): "we expect the error-correction overhead to be about 16:1 to achieve the first useful quantum applications"; "meeting future milestones included in our roadmap is not guaranteed" — [IonQ (CC), Form 10-K FY2021, filed Mar 2022](https://www.sec.gov/Archives/edgar/data/1824920/000119312522086738/d257705d10k.htm)
- The Fourth Circuit states IonQ unveiled a 32-qubit system in October 2020 but "did not make this new system commercially available at the time". The dMY III SPAC merger agreement was signed 7 Mar 2021, and IonQ began trading 1 Oct 2021 — [U.S. Court of Appeals, 4th Cir. (IND), Defeo v. IonQ, No. 24-1709, decided 8 Apr 2025](https://www.ca4.uscourts.gov/opinions/241709.P.pdf)
- #AQ claims over time:

| Date | System | Claim | Source |
|---|---|---|---|
| Feb 2022 | Aria | #AQ 20 | [insideHPC (IND-relay), "Quantum: IonQ Claims 20 Algorithmic Qubits", Feb 2022 (headline only)](https://insidehpc.com/2022/02/quantum-ionq-claims-20-algorithmic-qubits/) |
| 2022 | Aria | "achieved our technical milestone of 25 algorithmic qubits"; public roadmap "remains unchanged" | [IonQ (CC), Form 10-K FY2022 (excerpt)](https://www.sec.gov/Archives/edgar/data/1824920/000119312523085558/d424437d10k.htm) |
| 2023 (preprint Aug 2023) | Forte | #AQ 29, with error mitigation | [Chen et al., Quantum 2024 (CC, peer-reviewed)](https://quantum-journal.org/papers/q-2024-11-07-1516/pdf/) |
| 25 Jan 2024 | Forte | #AQ 35 "a year ahead of schedule" | [IonQ (CC), 25 Jan 2024 (excerpt)](https://ionq.com/news/ionq-achieves-technical-milestone-one-year-ahead-of-schedule) |
| Dec 2024 | Forte Enterprise | #AQ 36 | [Wikipedia (IND tertiary)](https://en.wikipedia.org/wiki/Algorithmic_qubits) |
| 25 Sep 2025 | Tempo | #AQ 64, "three months ahead of schedule" | [IonQ (CC)](https://ionq.com/news/ionq-achieves-record-breaking-quantum-performance-milestone-of-aq-64) |

- Rack-mounted systems: Forte Enterprise and Tempo were announced as "rack-mounted" on 27 Sep 2023, with targets only — [IonQ (CC), 27 Sep 2023](https://www.ionq.com/news/ionq-unveils-forte-enterprise-and-tempo-rack-mounted-enterprise-grade). Forte Enterprise went generally available on Braket in March–April 2025 — [TQI (IND-relay), 1 Apr 2025 (excerpt)](https://thequantuminsider.com/2025/04/01/ionq-forte-enterprise-now-globally-accessible-via-amazon-braket-and-ionq-quantum-cloud/)
- Networked commercial machines: the first claim came on 14 Apr 2026, with no metrics (section 5) — [IonQ (CC), 14 Apr 2026](https://www.ionq.com/news/ionq-achieves-key-photonic-interconnect-milestone-demonstrating-networked-quantum-systems-using-entanglement)
- Quantum advantage claims and what the papers say:
  - In September 2023 Chapman promised commercial advantage "within a two-year time frame" — [IonQ (CC), 27 Sep 2023](https://www.ionq.com/news/ionq-unveils-forte-enterprise-and-tempo-rack-mounted-enterprise-grade)
  - In June 2025 CEO Niccolo de Masi claimed "narrow commercial advantage" for the AstraZeneca workflow, and TQI called it a proof-of-concept — [The Quantum Insider (IND-relay), 9 Jun 2025](https://thequantuminsider.com/2025/06/09/ionq-speeds-quantum-accelerated-drug-development-application-in-partnership-with-astrazeneca-aws-and-nvidia/)
  - The underlying AstraZeneca paper makes no quantum-advantage claim — [arXiv:2506.22408, 27 Jun 2025](https://arxiv.org/abs/2506.22408)
  - The Ansys paper claims "up to 12% for some problems" — [arXiv:2503.13128, 17 Mar 2025](https://arxiv.org/abs/2503.13128)
- 2026 hardware target versus delivery: the 256-qubit system was "scheduled for demonstration in 2026" — [QCR (IND-relay), 21 Oct 2025](https://quantumcomputingreport.com/ionq-achieves-99-99-two-qubit-gate-fidelity-using-electronic-qubit-control-technology/). As of September 2026, chips were fabricated and ions trapped in prototypes, with "customer deliveries in 2027" — [IonQ (CC), 8 Sep 2026](https://www.ionq.com/news/ionq-launches-superion-product-line-industry-leading-upgradeable-platform-designed-to-scale-manufacturable-fault-tolerant-quantum-computing)
- Machine sizes: an independent benchmark lists IonQ machines as ionq_harmony (11 qubits), ionq_aria_2 (25), ionq_forte (36) and ionq_forte_enterprise (36) — [Montañez-Barrera, Michielsen, Bernal Neira (IND), arXiv:2502.06471 v2, 28 May 2025](https://arxiv.org/html/2502.06471v2)
- Short-seller allegations about the 2020–21 claims (detailed in section 5):
  - Scorpion (May 2022) called the 32-qubit machine "a brazen hoax" — [4th Cir. (IND), 8 Apr 2025](https://www.ca4.uscourts.gov/opinions/241709.P.pdf)
  - Kerrisdale (March 2025) said a former executive told it IonQ had only an 11-qubit system in 2020 — [Benzinga (IND), March 2025 (excerpt; page returned HTTP 403)](https://www.benzinga.com/trading-ideas/movers/25/03/44307671/is-high-flying-ionq-stock-a-disaster-in-the-making-shares-slide-as-short-seller-raises-red-flags)

### Inferences
- The #AQ milestones were met as IonQ defines the metric. But the meaning of "#AQ 64 by 2025" changed. In 2020 it was to be reached with 16:1 error-correction encoding, which would need about 1,024 physical qubits. In 2025 it was reached on a roughly 64–100-qubit machine using error mitigation and no error correction. (Arithmetic from VentureBeat 2020 and IonQ's 2025 release.)
- Rough timing against the 2020 plan:
  - The "22 AQ" expected of the 32-qubit (2020) system was first matched in 2022 (#AQ 20, then #AQ 25), on 25-qubit Aria.
  - Rack-mounted data-center machines arrived about 1–2 years after the 2023 target.
  - Networked machines arrived about 3 years late, and without published performance.
  - Broad quantum advantage by 2025 is not evidenced by any source found.
- Timelines continue to slip at the system level (256-qubit: demonstration in 2026 → deliveries in 2027). Component milestones (gate fidelity) have tended to arrive on time or early as lab results.

### Gaps
- Not retrieved: the March 2021 dMY III/IonQ investor presentation (SPAC-era technical projections), the exact year-by-year #AQ graphic in the 2020 roadmap, the Kerrisdale report text and IonQ's response to it, and an exact date for the #AQ 25 announcement.

## 4. The #AQ metric: definition, criticism, changes, independent measurements

### Takeaway
#AQ ("algorithmic qubits", IonQ, 2020) is an application-circuit benchmark. Six algorithm families derived from QED-C work must pass a success threshold of 1/e at circuit width n and depth n². It explicitly allows compiler optimization and error mitigation. IonQ's own peer-reviewed Forte paper shows #AQ 29 was passed only after plurality-vote mitigation; without mitigation, circuits typically failed after ~200 two-qubit gates. Competitor Quantinuum measured Forte at AQ 9 without mitigation. An independent Jülich/Purdue benchmark found IonQ's largest certified run at 28 qubits, against 56 for Quantinuum H2-1. IonQ has not dropped #AQ but, since April 2026, also reports a 13-workload application suite.

### Cited Findings
- Definition: circuits pass if success probability minus statistical error exceeds 1/e (~0.37). #AQ is the largest n for which all circuits of width ≤ n and depth ≤ n² (CX count) pass. AQ 1.0 uses six algorithm families: QFT, phase estimation, amplitude estimation, Monte Carlo sampling, VQE and Hamiltonian simulation — [Wikipedia (IND tertiary), "Algorithmic qubits", accessed 14 Nov 2026](https://en.wikipedia.org/wiki/Algorithmic_qubits)
- IonQ says #AQ builds on QED-C's algorithmic benchmarks but uses a different fidelity metric and its own threshold, since QED-C did not define a single number — [IonQ (CC), "Algorithmic Qubits: A Better Single-Number Metric" (excerpt)](https://ionq.com/resources/algorithmic-qubits-a-better-single-number-metric)
- What IonQ's own Forte paper shows [Chen et al., Quantum 8, 1516 (2024) (CC, peer-reviewed)](https://quantum-journal.org/papers/q-2024-11-07-1516/pdf/):
  - "#AQ benchmark incorporates the pre- and post-processing gains due to compiler optimizations and error mitigation."
  - Mitigation runs 25 variant circuits and aggregates them, with plurality voting "particularly effective" for 5 of the 6 families.
  - #AQ 29 was limited by amplitude-estimation circuits (≈604 two-qubit gates, post-mitigation fidelity 0.125).
  - "Before error mitigation… we typically see 200 two-qubit gate applications before noise reduces the fidelity to below 1/e."
  - The paper thanks Quantinuum's Charlie Baldwin "for feedback on the supplemental data".
- Quantinuum critique [Quantinuum (COMP), "Debunking algorithmic qubits", 1 Mar 2024](https://www.quantinuum.com/blog/debunking-algorithmic-qubits):
  - AQ is "very susceptible to tricks". Plurality voting mixes mitigation with device performance and "is unlikely to be scalable to larger systems".
  - Compilation shrinks the benchmark circuits: at AQ 32, phase estimation fell from 992 to 141 entangling gates and amplitude estimation from 868 to 72.
  - Without mitigation, Forte scored AQ 9 and H2-1 scored AQ 26. Two-qubit average fidelity was 99.816(5)% for H2-1 versus 99.35% for Forte.
  - Measured H2-1 quantum volume was 2^16 versus a Quantinuum estimate of about 2^5 for Forte. (The superscripts were lost in the fetched text and rendered as "216" and "25"; read them as exponents.)
- Azure documentation confirms "debiasing" is on by default on Aria and Forte and is priced. Its "Sharpening" option "filters out the erroneous results" — [Microsoft Learn (IND platform doc), 2026](https://learn.microsoft.com/en-us/azure/quantum/provider-ionq)
- PostQuantum on #AQ [PostQuantum (IND), M. Ivezic, 3 Aug 2026](https://postquantum.com/quantum-computing/quantum-computing-metrics-vendor-benchmarks/):
  - #AQ permits disclosed full-stack optimization and error mitigation. IonQ's defence is that users care about the delivered system.
  - In April 2026 IonQ introduced a 13-workload application benchmark reporting solution quality, time-to-solution and energy-to-solution "alongside #AQ". The author reads this as IonQ accepting that one number is not enough; IonQ has not said so.
  - Quantinuum H2 reached QV 2^25 in September 2025.
- Independent hardware measurement, Jülich Supercomputing Centre / RWTH Aachen / Purdue linear-ramp QAOA (LR-QAOA) benchmark of 24 processors from IBM, IQM, IonQ, Quantinuum, Rigetti and OriginQ [Montañez-Barrera, Michielsen, Bernal Neira (IND), "Evaluating the performance of quantum processing units at large width and depth", arXiv:2502.06471, v2 28 May 2025 (preprint)](https://arxiv.org/html/2502.06471v2):
  - IonQ Forte Enterprise: largest certified fully connected run was 28 qubits at p=3 (1,134 two-qubit gates, r=0.770).
  - IonQ Forte: a 35-qubit p=5 run (2,975 gates) did not pass.
  - IonQ Aria 2: results indistinguishable from random at 23 qubits.
  - Quantinuum H2-1: certified 56 qubits at p=3 (4,620 ZZ gates). "Only the Quantinuum family sustains coherent output above 30 qubits."
- Academic review, per a search excerpt: #AQ's fidelity-based scoring scales poorly because computing ideal output distributions needs classical resources that grow exponentially with qubits. The abstract itself does not mention #AQ — [Acuaviva, Aguirre, Peña, Sanz (IND), "Benchmarking Quantum Computers: Towards a Standard Performance Evaluation Approach", arXiv:2407.10941 v4 9 Mar 2026; Quantum Sci. Technol. 11, 025004 (2026) (excerpt)](https://arxiv.org/abs/2407.10941)

### Inferences
- #AQ measures the whole delivered stack (hardware, compiler and mitigation), not raw hardware or error correction. Two non-IonQ measurements point the same way: Quantinuum's unmitigated AQ 9 for Forte, and the independent Jülich certification limit of ≤28 qubits for IonQ against #AQ 29–36 claims. Both suggest #AQ scores sit well above what the hardware delivers unmitigated on deep circuits.
- The #AQ 64 run is the least documented of IonQ's #AQ claims: no register size, mitigation settings or circuit data were published in the release.

### Gaps
- Not found: QED-C or national-laboratory measurements of Tempo or of the #AQ 64 result, or any independent reproduction of an IonQ #AQ score. QED-C publications could not be searched because the search budget ran out.
- The names and results of IonQ's April 2026 13-workload suite were not found.

## 5. Demonstrations and claims: what was shown, peer review, outside co-authors, checks and disputes

### Takeaway
Only two IonQ-family flagship results are peer-reviewed, and both are company-authored: Oxford Ionics' 99.97% all-electronic two-qubit result (PRX Quantum, 2025) and the 2023 Forte benchmark (Quantum, 2024). The rest are preprints or press releases as of 14 Nov 2026:
- The 99.99% gate (two ⁴⁰Ca⁺ ions, one pair, estimated).
- qLDPC "breakeven" (marginal, 74.8% of shots discarded, larger codes worse).
- The Walking Cat architecture (theory).
- The April 2026 photonic link (no metrics).

The two "advantage" applications carry partner co-authors but have narrow or ill-defined baselines. Neither paper claims quantum advantage over the best classical methods. Short-seller technical allegations (Scorpion 2022, Kerrisdale 2025) were never tested on their technical merits. A court found the Scorpion report unreliable as evidence, not false. The first formal independent verification is DARPA QBI Stage C, which runs to 2029.

### Cited Findings
**5a. 99.99% two-qubit gate (announced 21 Oct 2025)**
- IonQ's blog [IonQ (CC), "Accelerating Towards Fault Tolerance: Unlocking 99.99% Two-Qubit Gate Fidelities", 21 Oct 2025](https://www.ionq.com/blog/accelerating-towards-fault-tolerance-unlocking-99-99-two-qubit-gate):
  - It calls the result an "estimated fidelity of 99.99%" for gates "above the Doppler limit", without ground-state cooling.
  - Its plot uses SLERB (subspace leakage error randomized benchmarking) with up to 500 Cliffords (1,083 two-qubit gates) on "a qubit pair". About 90% survival after ~1,000 gates converts to ≈0.01% error per gate.
  - The prior record (Oxford Ionics 2024, 3×10⁻⁴) used ground-state cooling.
- The paper [Hughes, Srinivas, Löschnauer, Knaack, Matt, Ballance, Malinowski, Harty, Sutherland (CC; no non-IonQ/Oxford Ionics affiliation identified), "Trapped-ion two-qubit gates with >99.99% fidelity without ground-state cooling", arXiv:2510.17286 v1, 20 Oct 2025; no journal reference as of 14 Nov 2026](https://arxiv.org/abs/2510.17286); details from the [full text](https://arxiv.org/html/2510.17286v1):
  - Result: estimated error 8.4(7)×10⁻⁵ (≈99.992%), on ⁴⁰Ca⁺ in a two-ion crystal, for a single pair, in a cryogenic trap.
  - Gate: laser-free, driven by an oscillating current (magnetic-field gradient), lasting 225.8 µs. Lasers are still used for Doppler cooling, optical pumping and readout.
  - Temperature: Doppler-cooled data at mean phonon number n̄=3.5(1); error stays ≲5×10⁻⁴ up to n̄=9.4(3).
  - Fit: the 8.4(7)×10⁻⁵ figure comes from fits truncated at ≤200 Cliffords (432 gates). The full 500-Clifford dataset (1,083 gates) gives 1.16(6)×10⁻⁴ (≈99.988%).
  - Assumptions and limits: SPAM is "assumed negligible"; errors grow by ~3×10⁻⁵ for longer sequences (non-Markovian); the main residual error is drift of the magnetic-field-sensitive qubit frequency; multi-pair operation is "not demonstrated".
- Companion method paper: SLERB of Mølmer–Sørensen gates, all-electronic gate error 2.6(2)×10⁻⁴ — [Sutherland, Hughes, Marceaux, Knaack, Löschnauer, Srinivas (CC), arXiv:2510.09508 v1, 10 Oct 2025, no journal reference](https://arxiv.org/abs/2510.09508)
- Predecessor result, now peer-reviewed: a seven-zone trap that "can control up to 10 qubits", single-qubit 99.99916(7)%, two-qubit (maximally entangled states) 99.97(1)% — [Löschnauer et al. (Oxford Ionics; CC, peer-reviewed), "Scalable, high-fidelity all-electronic control of trapped-ion qubits", arXiv:2407.07694 (10 Jul 2024); PRX Quantum 6, 040313 (2025)](https://arxiv.org/abs/2407.07694)
- Trade press repeated the "first… four-nines" framing with no independent assessment — [Quantum Computing Report (IND-relay), 21 Oct 2025](https://quantumcomputingreport.com/ionq-achieves-99-99-two-qubit-gate-fidelity-using-electronic-qubit-control-technology/). IonQ's 2026 earnings releases repeat it as "a world record" — [IonQ (CC), Q3 2026 results](https://www.sec.gov/Archives/edgar/data/0001824920/000119312526449779/ionq-ex99_1.htm)

**5b. Ansys LS-DYNA "outperformed classical" claim (20–21 Mar 2025)**
- The claim: IonQ Forte assisted a graph-partitioning step in a blood-pump simulation in Ansys LS-DYNA, giving "up to 12% faster processing" and "a 12% performance improvement over classical computing". It was billed as "one of the first instances where quantum computing has surpassed classical approaches". The classical baseline was not named — [Quantum Zeitgeist (IND-relay), 21 Mar 2025](https://quantumzeitgeist.com/ionq-and-ansys-achieve-milestone-quantum-computing-outperforms-classical-with-12-speed-increase-in-medical-device-design/). Quantum Computing Report's article of 20 Mar 2025 is paywalled — [QCR](https://quantumcomputingreport.com/ionq-and-ansys-demonstrate-quantum-speedup-in-engineering-simulation-workflow/)
- The paper [Aboumrad, Zhu, Girotto, Rouet, Jojo, Lucas, Pathak, Kaushik, Roetteler, "Accelerating large-scale linear algebra using variational quantum imaginary time evolution", arXiv:2503.13128, v1 17 Mar 2025, v2 14 Apr 2025; no journal reference; affiliations not shown on the abstract page](https://arxiv.org/abs/2503.13128):
  - Method: variational quantum imaginary-time evolution (VarQITE) applied to graph partitioning, to reduce fill-in in sparse matrix factorization.
  - Hardware and scale: IonQ Aria and Forte; meshes up to 6 million elements.
  - Result: LS-DYNA wall-clock time "can be improved by up to 12% for some problems". Hardware solutions were improved by a classical heuristic inspired by Fiduccia–Mattheyses.
  - Not in the abstract: qubit count and classical baseline.
- No independent technical critique was found. Coverage is mostly relays.

**5c. AstraZeneca / AWS / NVIDIA "20x" chemistry workflow (9 Jun 2025)**
- IonQ press release [IonQ (CC), 9 Jun 2025](https://investors.ionq.com/news/news-details/2025/IonQ-Speeds-Quantum-Accelerated-Drug-Development-Application-With-AstraZeneca-AWS-and-NVIDIA/default.aspx):
  - Claim: ">20 times improvement in end-to-end time-to-solution compared to previous implementations"; expected runtime cut "from months to days".
  - Set-up: Forte with NVIDIA CUDA-Q, Amazon Braket and AWS ParallelCluster using H200 GPUs.
  - No qubit count is given.
- IonQ's technical blog [IonQ (CC), blog, 9 Jun 2025](https://ionq.com/blog/ecosystem-innovation-ionqs-life-sciences-application-workflow-accelerates):
  - Method: quantum-classical auxiliary-field quantum Monte Carlo (QC-AFQMC) with matchgate shadows, applied to a nickel-catalyzed Suzuki–Miyaura reaction.
  - The 20× is measured against "our collaborators' 'state-of-the-art estimates'", not against IonQ's own earlier run.
  - The quantum step was sped up 9× (median 1.1 s vs 9.9 s per circuit) by runtime improvements. GPU post-processing was "the main source of the speedup".
  - Runtime was ~18 h per molecule versus an estimated week or more. No quantitative accuracy is given.
- The paper [Zhao et al. (41 authors; partner co-authorship implied by the releases; affiliations not shown on the abstract page), arXiv:2506.22408, 27 Jun 2025; related DOI 10.1103/n1tf-8kr7 listed, journal not named](https://arxiv.org/abs/2506.22408):
  - Qubits: 24 on Forte (16 for the trial state plus 8 ancillas used for error mitigation).
  - Speedups: 9× faster measurement collection; 656× faster distributed post-processing than the prior QC-AFQMC implementation.
  - Accuracy: reaction barriers agree with the classical CCSD(T) reference within ±4 kcal/mol on an ideal simulator, but only within 10 kcal/mol on the real processor.
  - The paper does not claim quantum advantage.
- Trade coverage notes that "previous methods" is undefined, the runtime is "projected", and the work is a proof-of-concept — [The Quantum Insider (IND-relay), 9 Jun 2025](https://thequantuminsider.com/2025/06/09/ionq-speeds-quantum-accelerated-drug-development-application-in-partnership-with-astrazeneca-aws-and-nvidia/)

**5d. Photonic interconnect and networking**
- 14 Apr 2026 claim [IonQ (CC), "IonQ Achieves Key Photonic Interconnect Milestone…", 14 Apr 2026](https://www.ionq.com/news/ionq-achieves-key-photonic-interconnect-milestone-demonstrating-networked-quantum-systems-using-entanglement):
  - IonQ "photonically interconnect[ed] two independent trapped-ion quantum systems". It validated "the generation, transmission, and detection of photons used to enable quantum entanglement" between two commercial computers "at a distance".
  - The work was partly AFRL-funded.
  - No fidelity, rate, distance, species, wavelength or paper is given.
- PostQuantum's assessment [PostQuantum (IND), M. Ivezic, 20 Apr 2026](https://postquantum.com/industry-news/ionq-photonic-interconnect-networked-quantum/):
  - It calls the result "a directional signal rather than a quantitative proof point".
  - Academic comparators: Duke (PRL 2024) 250 Bell pairs per second; Innsbruck 1.2 km of fiber at 95.9±1.5% fidelity with a 4.59× multiplexing speedup.
  - An IonQ theory proposal (Moore et al., 2025) targets more than 1,000 Bell pairs per second, but that is a proposal, not an experiment.
  - Lightsynq's "up to 50x" has not been shown at system level.
- Kerrisdale (March 2025) said IonQ "has never disclosed performance metrics for its photonic interconnect development" — [Benzinga (IND), March 2025 (excerpt; page returned HTTP 403)](https://www.benzinga.com/trading-ideas/movers/25/03/44307671/is-high-flying-ionq-stock-a-disaster-in-the-making-shares-slide-as-short-seller-raises-red-flags)
- Other 2026 networking items (all IonQ statements, no technical data):
  - Q1: selection for DARPA's HARQ program (modular computing using quantum interconnects); first commercial sale of a quantum memory node into the Mid-Atlantic Regional Quantum Internet; a national quantum communication network in Poland — [IonQ (CC), Q1 2026 results](https://www.sec.gov/Archives/edgar/data/0001824920/000119312526208923/ionq-ex99_1.htm)
  - Q2: "World's First Commercial Quantum Memory Unit Installed in a Live Fiber Optic Network", at the Tennessee center run with EPB — [IonQ (CC), Q2 2026 results](https://www.sec.gov/Archives/edgar/data/0001824920/000119312526335040/ionq-ex99_1.htm)
  - Q3: a $7.5M Air Force Research Laboratory follow-on for "full-stack quantum networking" — [IonQ (CC), Q3 2026 results](https://www.sec.gov/Archives/edgar/data/0001824920/000119312526449779/ionq-ex99_1.htm)

**5e. Error correction, logical qubits, fault-tolerance architecture**
- The breakeven preprint [Tham, Goldman, Debnath, Patel, Saraladevi, Nguyen, Nielsen, Pisenti, Wright, Gamble, Delfosse (CC), "Breakeven demonstration of quantum low-density parity-check codes", arXiv:2606.06455, v1 4 Jun 2026, v2 14 Sep 2026; no journal reference](https://arxiv.org/abs/2606.06455):
  - Nine codes from qLDPC, topological and concatenated families ran on one device without reconfiguration.
  - The headline qLDPC code stores 4 logical qubits in 18 physical qubits, with logical error "up to 9×" better than a superconducting demonstration of a similar code.
  - Mid-circuit measurement used an optical–metastable–ground (OMG) scheme, with no ion transport.
- PostQuantum's analysis [PostQuantum (IND), M. Ivezic, 5 Jun 2026](https://postquantum.com/quantum-research/ionq-qldpc-breakeven-trapped-ion/):
  - Hardware: a stationary chain of 40 ¹³³Ba⁺ ions.
  - Codes: bivariate-bicycle codes BB5 [[18,4,3]], [[24,4,4]] and [[30,4,5]]; a generalized-bicycle code GB4 [[26,2,5]]; two toric codes; a concatenated [[16,4,4]] code.
  - Lifetimes: GB4 logical lifetime 3.95±0.68 s versus physical 3.3±0.9 s (derived from T2* of 1.1±0.3 s). BB5 [[24,4,4]] reached 3.36±0.57 s.
  - Error rates: BB5 [[18,4,3]] X/Z logical errors were 4×/9× lower than the Kunlun superconducting bivariate-bicycle result (~9% per logical qubit per cycle). GB4 Z-basis error was 0.96% per logical qubit per cycle.
  - Leakage and discards: [[30,4,5]] discarded 74.8% of shots at six rounds because of detected leakage. Leakage was ~1.7×10⁻³ per mid-circuit-measurement round.
  - Larger codes performed worse, so below-threshold scaling is not shown. Breakeven is "marginal" and within error bars.
- Hagar's critique [Amit Hagar (IND critic; credentials not stated on page), "Breakeven Is Not a Milestone", Substack "Dear Quantum Computing Industry", 8 Oct 2026](https://amithagar.substack.com/p/breakeven-is-not-a-milestone):
  - The physical baseline is T2* without dynamical decoupling, which the paper says "can significantly improve" coherence.
  - The margin is about half an error bar, and noise parameters "cannot be uniquely determined".
  - Post-selection discards 74.8% of shots.
  - Distance 3 beats distance 5, so the suppression factor is below 1.
  - Pauli rates were fitted on the same experiments being reported.
  - A ~1 Hz magnetic noise bath (noise with memory) conflicts with the threshold theorem's assumptions.
- IonQ's Superion release says "In August 2026, IonQ reported breakeven quantum error correction using qLDPC codes on a Tempo engineering test system" — [IonQ (CC), 8 Sep 2026](https://www.ionq.com/news/ionq-launches-superion-product-line-industry-leading-upgradeable-platform-designed-to-scale-manufacturable-fault-tolerant-quantum-computing). This conflicts with the 4 Jun 2026 preprint date; possibly a later announcement or the v2 revision.
- Scheduled qLDPC: an IonQ preprint and blog claim up to 74× faster Clifford and 5× faster Toffoli execution. This is a compilation/scheduling result, not a hardware run — [Quantum Computing Report (IND-relay) (excerpt)](https://quantumcomputingreport.com/ionq-demonstrates-scheduled-qldpc-error-correction-to-accelerate-fault-tolerant-gate-execution-by-up-to-74x/); [IonQ (CC) blog (excerpt)](https://www.ionq.com/blog/how-qldpc-with-scheduled-error-correction-unlocks-faster-fault-tolerant-quantum-computers)
- Walking Cat architecture, theory only [Tripier … Delfosse (18 IonQ authors; CC), "Fault-Tolerant Quantum Computing with Trapped Ions: The Walking Cat Architecture", arXiv:2604.19481 v1, 21 Apr 2026, 110 pp; no journal reference](https://arxiv.org/abs/2604.19481):
  - Design: QCCD ion shuttling plus LDPC codes, with "cat factories" producing cat states for logical measurement.
  - A "fast" design uses a [[70,6,9]] code. A "dense" design uses [[102,22,9]]: 110 logical qubits, ~1 million T gates per day, 2,514 physical qubits.
  - A 100-site Heisenberg-model simulation would need ~1 month on 10,000 physical qubits.
  - QCR adds that the design assumes two-qubit fidelity above 99.99%, replaces lost ions from reservoirs, and compiles 20-bit Shor onto a 102-qubit instance. QCR gives no independent evaluation — [Quantum Computing Report (IND-relay), 7 May 2026](https://quantumcomputingreport.com/ionq-details-walking-cat-blueprint-for-fault-tolerant-trapped-ion-systems/)
- In Q1 2026 the CEO said IonQ is "poised to be the first company in history to fully demonstrate fault-tolerance at scale". This is a goal — [IonQ (CC), Q1 2026 results](https://www.sec.gov/Archives/edgar/data/0001824920/000119312526208923/ionq-ex99_1.htm)

**5f. Short-seller technical allegations and outcomes**
- Scorpion Capital, 3 May 2022, as summarized by the Fourth Circuit [U.S. Court of Appeals, 4th Cir. (IND), Defeo v. IonQ, No. 24-1709, decided 8 Apr 2025](https://www.ca4.uscourts.gov/opinions/241709.P.pdf):
  - The report called IonQ "[a] scam built on phony statements". It said the 32-qubit machine "is a brazen hoax", that "rapid miniaturization" claims were "completely outrageous", and that error rates were mischaracterized ("slammed the error rates shown as a joke").
  - It relied on unnamed former employees and experts, and warned that quotes "may be paraphrased, truncated, and/or summarized".
  - IonQ (4 May 2022) said the report "contain[ed] important inaccuracies and mischaracterizations".
  - The court affirmed dismissal of the investor suit because the report's anonymous, disclaimed character "rendered it inadequate" to reveal truth (loss causation). It stated: "We are not experts in quantum computing". There was no finding on the technical allegations.
- Kerrisdale Capital, March 2025: photonic-interconnect metrics never disclosed; a former executive allegedly said IonQ had only an 11-qubit system in 2020 when the former CEO claimed a "perfect" 32-qubit system — [Benzinga (IND) (excerpt; HTTP 403)](https://www.benzinga.com/trading-ideas/movers/25/03/44307671/is-high-flying-ionq-stock-a-disaster-in-the-making-shares-slide-as-short-seller-raises-red-flags)
- Wolfpack Research, February 2026: about revenue and earmarks, not technology. IonQ called it "false, misleading, and unsubstantiated" — [Fortune (IND), 4 Feb 2026 (headline/excerpt)](https://fortune.com/2026/02/04/ionq-wolfpack-research-short-seller-says-quantum-computing-company-misled-investors-about-cancelled-government-backdoor-earmarks/); [Yahoo Finance (IND) (excerpt)](https://finance.yahoo.com/news/short-seller-claims-ionq-biggest-212406696.html)

### Inferences
- Peer review: of the core technical claims, only the 2024 Oxford Ionics 99.97% gate and the 2023 Forte benchmark are peer-reviewed, and both are company-authored. The 99.99% gate, breakeven QEC and Walking Cat had no journal reference on arXiv as of 14 Nov 2026. The April 2026 interconnect has no paper at all.
- Outside co-authors appear only on the application papers (Ansys; AstraZeneca/AWS/NVIDIA), as implied by the joint releases; affiliations were not visible on the arXiv abstract pages. No outside group has replicated an IonQ hardware result.
- The "99.99%" headline rests on a truncated fit (8.4×10⁻⁵). The full 1,083-gate dataset gives 1.16×10⁻⁴ (≈99.988%), which rounds to 99.99% but is not ">99.99%". It is a two-ion, one-pair, ⁴⁰Ca⁺ cryogenic result with SPAM assumed negligible.
- The "20x" chemistry speedup comes mainly from classical GPU post-processing and runtime engineering, measured against a prior hybrid implementation. The quantum-hardware result was less accurate (within 10 kcal/mol) than the ideal simulation (±4 kcal/mol).

### Gaps
- Not found: independent replication or peer review of the 99.99% gate or of breakeven qLDPC; any published fidelity, rate or distance for the April 2026 link; any independent technical critique of the Ansys 12% result.
- A search excerpt attributed an AstraZeneca-baseline critique to analyst Olivier Ezratty on X, but the post could not be located or verified.
- The Kerrisdale and Scorpion report texts and IonQ's point-by-point responses (if any) were not retrieved.
- The date conflict for the breakeven result (June vs August 2026) is unresolved.

## 6. What remains unproven (as of 14 Nov 2026)

### Takeaway
None of the scaling pillars of IonQ's roadmap has been demonstrated in public data at the scale the roadmap needs:
- Logical qubits at useful scale: best shown is breakeven-level, with ≤4 logical qubits per code, post-selection, and larger codes doing worse.
- Many-qubit 2D EQC chips: 256-qubit chips are fabricated and ions trapped, but there is no gate data.
- Fast, high-fidelity photonic links between modules: the April 2026 link has no metrics.
- Commercial-scale quantum advantage.

### Cited Findings
- **Logical qubits:** the 2026 roadmap target is 12 logical qubits at <1E-7 — [IonQ (CC), roadmap page](https://ionq.com/roadmap). The best IonQ hardware data are ~0.96% logical error per qubit per cycle (GB4 [[26,2,5]]), ≤4 logical qubits per code, 74.8% of shots discarded on the largest code, and no improvement with distance — [PostQuantum (IND), 5 Jun 2026](https://postquantum.com/quantum-research/ionq-qldpc-breakeven-trapped-ion/); [Hagar (IND), 8 Oct 2026](https://amithagar.substack.com/p/breakeven-is-not-a-milestone)
- **EQC at scale:**
  - Published EQC records are a two-ion pair (99.99% estimate) — [arXiv:2510.17286 (CC)](https://arxiv.org/html/2510.17286v1) — and a 7-zone, ≤10-qubit trap (99.97%) — [PRX Quantum 6, 040313 (CC, peer-reviewed)](https://arxiv.org/abs/2407.07694).
  - For Superion 256, only fabrication and "first ions trapped" are claimed — [IonQ (CC), 8 Sep 2026](https://www.ionq.com/news/ionq-launches-superion-product-line-industry-leading-upgradeable-platform-designed-to-scale-manufacturable-fault-tolerant-quantum-computing).
  - The 99.99% paper says multi-pair operation is "not demonstrated" — [arXiv:2510.17286 (CC)](https://arxiv.org/html/2510.17286v1).
- **Photonic links:** no IonQ rate or fidelity has been published. Lightsynq's 50× is not shown at system level — [PostQuantum (IND), 20 Apr 2026](https://postquantum.com/industry-news/ionq-photonic-interconnect-networked-quantum/)
- **Tempo at spec:** 100 qubits and 99.9% are still labelled "target" — [IonQ (CC), Tempo page, accessed 14 Nov 2026](https://ionq.com/quantum-systems/tempo)
- **Advantage:** the Ansys paper says "up to 12% for some problems" — [arXiv:2503.13128](https://arxiv.org/abs/2503.13128). The AstraZeneca paper makes no advantage claim — [arXiv:2506.22408](https://arxiv.org/abs/2506.22408).
- **Roadmap verification:** DARPA's independent verification of the roadmap runs "through 2029" — [IonQ (CC), 7 Oct 2026](https://www.ionq.com/news/ionq-advances-to-final-stage-of-darpas-quantum-benchmarking-initiative); [QCR (IND), 7 Oct 2026](https://quantumcomputingreport.com/darpa-selects-atom-computing-diraq-ibm-and-ionq-for-final-stage-c-verification-under-quantum-benchmarking-initiative/)
- **Manufacturing economics:** cost-per-qubit reduction >300× is an IonQ expectation — [IonQ (CC), 8 Sep 2026](https://www.ionq.com/news/ionq-launches-superion-product-line-industry-leading-upgradeable-platform-designed-to-scale-manufacturable-fault-tolerant-quantum-computing). The "<$30M for 2M qubits" review has no named reviewer — [Nasdaq (IND-relay) (excerpt)](https://www.nasdaq.com/articles/ionqs-quantum-roadmap-and-foundry-strategy-through-2030)

### Inferences
- The gap to the 2026 logical target is about five orders of magnitude: ~1×10⁻² measured per-cycle logical error versus a <1×10⁻⁷ target. The units are not identical: the roadmap's "logical error state" has no stated unit. No public evidence through 14 Nov 2026 shows the 12-logical-qubit target being met.
- Ion-species continuity is unproven:
  - Commercial machines use ytterbium (Aria/Forte, per Azure).
  - The breakeven work used barium-133 (Tempo-class).
  - The EQC records used ⁴⁰Ca⁺.
  - Superion's species is undisclosed.

  It is therefore not public whether the 99.99% gate physics carries over to the Superion chip.

### Gaps
- Not found: any IonQ data on yield, uniformity, crosstalk or transport fidelity for SkyWater-made traps, or quantum-memory specifications (efficiency, storage time) for the Lightsynq/EPB memory products.

## 7. Physical and engineering limits of IonQ's approach (with numbers)

### Takeaway
Trapped ions offer long coherence (T2 ≈1 s on IonQ commercial systems; up to ~600 s shown for hyperfine qubits) but slow operations:
- IonQ commercial two-qubit gates take 0.6–1.1 ms, and the record EQC gate takes 0.23 ms. An independent benchmark found trapped-ion wall-clock runtimes about 4 orders of magnitude longer than an IBM device on a comparable job.
- Longer single chains bring motional-mode crowding (~10 kHz spacing in Forte's 36-ion chain), slower gates and more crosstalk.
- Shuttling ions instead (QCCD) has historically spent most runtime on cooling and transport.
- Photonic links have reached only ~180–250 Bell pairs per second at ~94% fidelity in academic labs.
- Logical-level throughput in IonQ's own fault-tolerant design is ~10⁶ T gates per day.

### Cited Findings
- **Gate speed:**
  - Aria: 600 µs two-qubit and 135 µs single-qubit gates — [Microsoft Learn (IND platform doc)](https://learn.microsoft.com/en-us/azure/quantum/provider-ionq)
  - Forte: ZZ gates 770–1,103 µs (Mølmer–Sørensen median 672 µs); single-qubit gates 110 µs — [Chen et al. (CC, peer-reviewed)](https://quantum-journal.org/papers/q-2024-11-07-1516/pdf/)
  - Trapped-ion gate times of 600–2,000 µs. A 25-qubit, p=100, 1,000-shot job took ~18,000 s on Aria 2 versus 0.5 s on ibm_fez — [Jülich/Purdue (IND), arXiv:2502.06471](https://arxiv.org/html/2502.06471v2)
  - Lab two-qubit gates are "typically 10–100 µs" — [Bruzewicz, Chiaverini, McConnell, Sage, MIT Lincoln Laboratory (IND), "Trapped-Ion Quantum Computing: Progress and Challenges", arXiv:1904.04178, Apr 2019 (older)](https://arxiv.org/abs/1904.04178)
  - EQC smooth gate 225.8 µs (Walsh-1 MS reference ~124 µs) — [arXiv:2510.17286 (CC)](https://arxiv.org/html/2510.17286v1)
- **Coherence:**
  - Aria: T1 10–100 s, T2 ~1 s — [Microsoft Learn](https://learn.microsoft.com/en-us/azure/quantum/provider-ionq)
  - Barium qubits in the breakeven experiment: T2* 1.1±0.3 s without dynamical decoupling — [PostQuantum (IND), 5 Jun 2026](https://postquantum.com/quantum-research/ionq-qldpc-breakeven-trapped-ion/)
  - Demonstrated coherence ranges from 0.2 s (optical qubits) to 600 s (hyperfine qubits), about 10⁶ times gate times — [MIT-LL review (IND), 2019](https://arxiv.org/abs/1904.04178)
- **Chain length and motional-mode crowding:**
  - In Forte, the entangling angle for fixed duration scales as 1/r³ with ion separation r, and optimal duration grows with ion distance "as spectral crowding of the transverse modes starts to dominate infidelity". Neighboring mode separation is "approximately 10 kHz". The optics address 40 ions, but a 36-ion chain was used — [Chen et al. (CC, peer-reviewed)](https://quantum-journal.org/papers/q-2024-11-07-1516/pdf/)
  - The review finds two-qubit gate speed "generally decreases as the total number of ions grows". Ion-ion coupling scales as 1/s^α with α=1–3, with spectral crowding and more heating exposure for longer gates. Proposals extend to 50-ion chains — [MIT-LL review (IND), 2019](https://arxiv.org/abs/1904.04178)
  - IonQ's QEC experiment used a 40-ion chain — [PostQuantum (IND)](https://postquantum.com/quantum-research/ionq-qldpc-breakeven-trapped-ion/)
- **Crosstalk and errors the component model misses:** Forte's observed application-circuit error (~100×10⁻⁴ per two-qubit gate) was about twice the component median (46.4×10⁻⁴). The authors attribute the difference to "out-of-model" errors such as crosstalk and drift. Without mitigation, about 200 two-qubit gates fit before fidelity falls below 1/e — [Chen et al. (CC, peer-reviewed)](https://quantum-journal.org/papers/q-2024-11-07-1516/pdf/)
- **Heating:**
  - Anomalous motional heating scales roughly as d⁻⁴ with ion–electrode distance, while trap frequency scales as d^-1/2. At d=40–80 µm, heating "can be made sufficiently low" for fault tolerance using ion milling or cryogenic operation below ~10 K. Ion transport has been shown at ~50 m/s with 0.1 quanta of added motion — [MIT-LL review (IND), 2019](https://arxiv.org/abs/1904.04178)
  - The EQC smooth gate keeps error ≲5×10⁻⁴ up to n̄=9.4 — [arXiv:2510.17286 (CC)](https://arxiv.org/html/2510.17286v1)
- **QCCD overhead:** in a published QCCD demonstration, runtime was about 2% gates, 27% transport and 68% cooling — [IonQ blog (CC) citing Pino et al., Nature 2021](https://www.ionq.com/blog/accelerating-towards-fault-tolerance-unlocking-99-99-two-qubit-gate); [Nature article](https://www.nature.com/articles/s41586-021-03318-4) (not fetched).
- **Leakage and ion loss:**
  - ~1.7×10⁻³ leakage per mid-circuit-measurement round, with 74.8% of shots discarded on [[30,4,5]]. Simulated erasure conversion (re-initializing leaked qubits instead of discarding the shot) raised worst-case logical error by ~11% for BB5 and ~20% for GB4 — [PostQuantum (IND), 5 Jun 2026](https://postquantum.com/quantum-research/ionq-qldpc-breakeven-trapped-ion/)
  - Walking Cat includes a "qubit factory" with reservoirs to replace lost ions — [QCR (IND-relay), 7 May 2026](https://quantumcomputingreport.com/ionq-details-walking-cat-blueprint-for-fault-tolerant-trapped-ion-systems/)
- **Laser versus electronic control:**
  - Laser control: Raman-laser gates are limited by spontaneous scattering. The review cites ~99.993% single-qubit fidelity at 7.5 µs with Raman beams, and notes that near-field microwave gates face crosstalk in addressing — [MIT-LL review (IND), 2019](https://arxiv.org/abs/1904.04178)
  - Electronic control (EQC), earlier result: single-qubit 99.99916(7)% and two-qubit 99.97(1)% in a ≤10-qubit trap — [PRX Quantum 6, 040313 (CC, peer-reviewed)](https://arxiv.org/abs/2407.07694)
  - Electronic control, record gate: residual error is dominated by magnetic-field drift, and lasers are still used for cooling, state preparation and readout — [arXiv:2510.17286 (CC)](https://arxiv.org/html/2510.17286v1)
- **Photonic link physics:**
  - Rate formula: Γ_RE = γ_rep(η_c·η_d)²/2, where γ_rep is the attempt rate and η_c, η_d are photon collection and detection efficiencies. The best collection efficiencies were 0.02–0.04 (as of 2019), and each attempt needs ~1 µs to re-initialize — [MIT-LL review (IND), 2019](https://arxiv.org/abs/1904.04178)
  - Oxford: ⁸⁸Sr⁺, 182 s⁻¹, F=0.940(5), success probability 2.18×10⁻⁴ per attempt — [Stephenson et al., Oxford (IND), PRL 124, 110501 (2020), arXiv:1911.10841](https://arxiv.org/abs/1911.10841)
  - Duke: Ba⁺ with Yb⁺ sympathetic cooling, 0.8 NA objectives, 250 s⁻¹, F>94%. Both ions were in the same apparatus, so this is a building block rather than a remote link — [O'Reilly et al., Duke (IND), PRL 133, 090802 (2024), arXiv:2404.16167](https://arxiv.org/abs/2404.16167)
  - Innsbruck 1.2 km at 95.9±1.5%, and IonQ's >1,000 s⁻¹ theory proposal — [PostQuantum (IND), 20 Apr 2026](https://postquantum.com/industry-news/ionq-photonic-interconnect-networked-quantum/)
  - Lightsynq "up to 50x" (claim) — [IonQ (CC), 13 Jun 2025](https://www.ionq.com/blog/ionqs-accelerated-roadmap-turning-quantum-ambition-into-reality)
- **Logical throughput:** Walking Cat's dense design gives 110 logical qubits at ~10⁶ T gates per day on 2,514 physical qubits. A 100-site Heisenberg simulation takes ~1 month on 10,000 physical qubits — [arXiv:2604.19481 (CC)](https://arxiv.org/abs/2604.19481)

### Inferences
- Arithmetic from the sources above:
  - 10⁶ T gates per day is ≈12 T gates per second.
  - At 180–250 Bell pairs per second, one remote pair takes ~4–5.5 ms, the length of ~4–25 local gates. Inter-module logical operations would be link-limited unless memory buffering or multiplexing gains (50× claimed; >1,000 s⁻¹ proposed) are realized.
  - The median Forte two-qubit error (~4.6×10⁻³) is ~40–55× the two-ion EQC result (0.84–1.16×10⁻⁴).
- Moving from long laser-addressed chains (Forte/Tempo) to 2D electronic QCCD chips (Superion) trades mode crowding for transport, cooling and leakage/loss overheads. The size of those overheads on IonQ's chips is not public.

### Gaps
- Not found: heating rates, transport times or speeds, ion-loss rates, or cooling overheads for IonQ/SkyWater chips; crosstalk data for Tempo; memory efficiency and storage time for Lightsynq-derived products.
- The 2019 review numbers are older and may understate current lab performance. Newer reviews could not be searched because the search budget ran out.

## 8. How solid is each major claim? (evidence-strength summary)

### Takeaway
Evidence is strongest for IonQ's present-generation component performance: a peer-reviewed full-device Forte benchmark plus independent benchmarking that agrees with it. It is moderate for laboratory gate physics (peer-reviewed 99.97%; preprint 99.99%). It is weak or absent for system-scale and forward claims: Tempo 100 qubits at 99.9%, #AQ 64 details, photonic links, logical qubits, Superion performance and roadmap dates. These rest on company releases or company-authored preprints and have not been checked externally. The planned check is DARPA QBI Stage C, running to 2029.

### Cited Findings
Evidence levels below: *peer-reviewed and independently checked*; *peer-reviewed, company-authored*; *preprint, company-authored*; *press release only*; *forward-looking*.

| Claim | Evidence type and basis |
|---|---|
| Aria/Forte two-qubit fidelity ~99.5–99.6% (avg/median) | Peer-reviewed, company-authored (median 99.54% over 435 pairs) — [Chen et al.](https://quantum-journal.org/papers/q-2024-11-07-1516/pdf/). Platform docs give 99.6% average — [Microsoft Learn](https://learn.microsoft.com/en-us/azure/quantum/provider-ionq). Competitor figure 99.35% — [Quantinuum (COMP)](https://www.quantinuum.com/blog/debunking-algorithmic-qubits). Independent benchmark consistent with modest-depth performance up to ~20–28 qubits — [Jülich/Purdue (IND)](https://arxiv.org/html/2502.06471v2). |
| #AQ 29/35/36/64 | #AQ 29 is peer-reviewed but needs error mitigation — [Chen et al.](https://quantum-journal.org/papers/q-2024-11-07-1516/pdf/). #AQ 35/36/64 are press releases only. Competitor measured unmitigated AQ 9 for Forte — [Quantinuum (COMP)](https://www.quantinuum.com/blog/debunking-algorithmic-qubits). No independent reproduction. #AQ 64 register size and mitigation are undisclosed — [IonQ (CC)](https://ionq.com/news/ionq-achieves-record-breaking-quantum-performance-milestone-of-aq-64). |
| 99.97% electronic two-qubit gate (Oxford Ionics, 2024) | Peer-reviewed, company-authored — [PRX Quantum 6, 040313 (2025)](https://arxiv.org/abs/2407.07694). Scale ≤10 qubits. |
| 99.99% two-qubit gate (Oct 2025) | Preprint, company-authored, not peer-reviewed as of 14 Nov 2026. Two ⁴⁰Ca⁺ ions, one pair, cryogenic, SPAM assumed negligible, truncated-fit estimate (full dataset 99.988%). No outside replication — [arXiv:2510.17286](https://arxiv.org/html/2510.17286v1). |
| qLDPC breakeven (Jun/Aug 2026) | Preprint, company-authored. Marginal (within error bars), 74.8% of shots discarded, larger codes worse. Critiqued by independent commentators — [PostQuantum (IND)](https://postquantum.com/quantum-research/ionq-qldpc-breakeven-trapped-ion/); [Hagar (IND)](https://amithagar.substack.com/p/breakeven-is-not-a-milestone). |
| Walking Cat resource estimates | Theory preprint, company-authored; assumes >99.99% gates — [arXiv:2604.19481](https://arxiv.org/abs/2604.19481); [QCR](https://quantumcomputingreport.com/ionq-details-walking-cat-blueprint-for-fault-tolerant-trapped-ion-systems/). |
| Two commercial computers photonically linked (Apr 2026) | Press release only; no fidelity, rate or distance — [IonQ (CC)](https://www.ionq.com/news/ionq-achieves-key-photonic-interconnect-milestone-demonstrating-networked-quantum-systems-using-entanglement). Independent view: "directional signal" — [PostQuantum (IND)](https://postquantum.com/industry-news/ionq-photonic-interconnect-networked-quantum/). |
| Lightsynq memory link "up to 50x" rate | Company claim; not shown at system level — [IonQ (CC)](https://www.ionq.com/blog/ionqs-accelerated-roadmap-turning-quantum-ambition-into-reality); [PostQuantum (IND)](https://postquantum.com/industry-news/ionq-photonic-interconnect-networked-quantum/). |
| Superion 256 chips fabricated, ions trapped | Company statement, no data; deliveries 2027 — [IonQ (CC)](https://www.ionq.com/news/ionq-launches-superion-product-line-industry-leading-upgradeable-platform-designed-to-scale-manufacturable-fault-tolerant-quantum-computing). |
| Ansys "12% faster than classical" | Preprint with partner co-authors (implied); "up to 12% for some problems"; classical heuristic post-processing; baseline not specified in the abstract. No independent critique found — [arXiv:2503.13128](https://arxiv.org/abs/2503.13128). |
| AstraZeneca/AWS/NVIDIA "20x" | Preprint with partner co-authors. Speedup is vs a prior QC-AFQMC implementation and mostly GPU post-processing. QPU accuracy within 10 kcal/mol vs ±4 kcal/mol ideal. No advantage claimed by the paper — [arXiv:2506.22408](https://arxiv.org/abs/2506.22408); [IonQ blog (CC)](https://ionq.com/blog/ecosystem-innovation-ionqs-life-sciences-application-workflow-accelerates). |
| Roadmap 2027–2030 (10k → 2M physical; 800 → 80k logical) | Forward-looking. Independent commentator calls the 2028 plan "aggressive but not guaranteed" — [PostQuantum (IND)](https://postquantum.com/industry-news/ionqroadmap-crqc/). DARPA verification pending to 2029 — [QCR (IND)](https://quantumcomputingreport.com/darpa-selects-atom-computing-diraq-ibm-and-ionq-for-final-stage-c-verification-under-quantum-benchmarking-initiative/). |
| Scorpion 2022 "32-qubit hoax" allegation | Not adjudicated on technical merits. The court found the report's anonymous, disclaimed sourcing inadequate as evidence for loss causation — [4th Cir. (IND)](https://www.ca4.uscourts.gov/opinions/241709.P.pdf). |
| DARPA QBI Stage C selection | Independently confirmed selection (7 Oct 2026). Verification results not yet available — [QCR (IND)](https://quantumcomputingreport.com/darpa-selects-atom-computing-diraq-ibm-and-ionq-for-final-stage-c-verification-under-quantum-benchmarking-initiative/). |

### Inferences
- Pattern: IonQ's component-level physics claims tend to be backed by papers, often company-authored and peer-reviewed later. System-level and schedule claims tend to be backed only by releases, and several have slipped or been redefined: #AQ 64 without error correction; networking 2023 → 2026; 256-qubit demonstration in 2026 → deliveries in 2027.

### Contradictions recorded (between sources)
- **#AQ 64 date and system:** IonQ dates it 25 Sep 2025 on "an IonQ Tempo system". PostQuantum dates it October 2025 on a "development system". The aggregator says "64-qubit computational register". QCR headlined a "100-qubit" system, while IonQ's page still lists 100 qubits as a target. Sources: [IonQ](https://ionq.com/news/ionq-achieves-record-breaking-quantum-performance-milestone-of-aq-64); [PostQuantum](https://postquantum.com/quantum-computing/quantum-computing-metrics-vendor-benchmarks/); [Quantum Market Cap](https://quantummarketcap.com/roadmap); [QCR](https://quantumcomputingreport.com/ionq-reaches-aq-64-milestone-on-100-qubit-tempo-system-ahead-of-schedule/)
- **Breakeven date:** the arXiv v1 is dated 4 Jun 2026, while IonQ's Superion release says "In August 2026". Sources: [arXiv](https://arxiv.org/abs/2606.06455); [IonQ](https://www.ionq.com/news/ionq-launches-superion-product-line-industry-leading-upgradeable-platform-designed-to-scale-manufacturable-fault-tolerant-quantum-computing)
- **99.99% figure:**
  - The headline "99.99%" and the paper title ">99.99%" rest on 8.4(7)×10⁻⁵ from a truncated fit; the full dataset gives 1.16(6)×10⁻⁴.
  - The blog's ≈0.01% comes from ~90% survival after ~1,000 gates.
  - The companion SLERB paper reports 2.6(2)×10⁻⁴ for its all-electronic MS gates.
  - Sources: [arXiv:2510.17286](https://arxiv.org/html/2510.17286v1); [IonQ blog](https://www.ionq.com/blog/accelerating-towards-fault-tolerance-unlocking-99-99-two-qubit-gate); [arXiv:2510.09508](https://arxiv.org/abs/2510.09508)
- **Roadmap versions:**
  - The June 2025 blog puts two photonically linked chips in 2028 and 40,000–80,000 logical qubits in 2030. The current page lists photonic interconnect from 2029 and 80,000 logical.
  - The 256-qubit system was "demonstration in 2026" in October 2025 and is "deliveries in 2027" as of September 2026.
  - Sources: [IonQ blog](https://www.ionq.com/blog/ionqs-accelerated-roadmap-turning-quantum-ambition-into-reality); [IonQ roadmap](https://ionq.com/roadmap); [QCR](https://quantumcomputingreport.com/ionq-achieves-99-99-two-qubit-gate-fidelity-using-electronic-qubit-control-technology/); [IonQ](https://www.ionq.com/news/ionq-launches-superion-product-line-industry-leading-upgradeable-platform-designed-to-scale-manufacturable-fault-tolerant-quantum-computing)
- **Forte two-qubit fidelity:** 99.6% average (Azure, not SPAM-corrected) vs 99.54% median DRB (Chen et al.) vs 99.35% (Quantinuum's figure for Forte). Sources: [Azure](https://learn.microsoft.com/en-us/azure/quantum/provider-ionq); [Chen et al.](https://quantum-journal.org/papers/q-2024-11-07-1516/pdf/); [Quantinuum](https://www.quantinuum.com/blog/debunking-algorithmic-qubits)
- **AstraZeneca speedup baseline:** the press release says "previous implementations". The blog says collaborators' "state-of-the-art estimates", with GPU post-processing as the main source. The paper gives 9× (measurement) and 656× (post-processing) against the prior QC-AFQMC implementation. Sources: [IonQ PR](https://investors.ionq.com/news/news-details/2025/IonQ-Speeds-Quantum-Accelerated-Drug-Development-Application-With-AstraZeneca-AWS-and-NVIDIA/default.aspx); [IonQ blog](https://ionq.com/blog/ecosystem-innovation-ionqs-life-sciences-application-workflow-accelerates); [arXiv:2506.22408](https://arxiv.org/abs/2506.22408)
- **Ansys problem size:** "up to 2.6 million vertices and 40 million edges" (Quantum Zeitgeist) vs "meshes of up to six million elements" (arXiv abstract). These are different units and not necessarily inconsistent. Sources: [Quantum Zeitgeist](https://quantumzeitgeist.com/ionq-and-ansys-achieve-milestone-quantum-computing-outperforms-classical-with-12-speed-increase-in-medical-device-design/); [arXiv](https://arxiv.org/abs/2503.13128)

### Gaps (consolidated list of what could not be found or verified)
- **Specifications:** Tempo and Forte Enterprise median/best two-qubit fidelities, SPAM and crosstalk; register size and mitigation settings for #AQ 64; Superion 256 gate, coherence and species data.
- **Independent checks:** any independent (QED-C, national-lab, academic) measurement of Tempo; independent replication of the 99.99% gate or breakeven QEC.
- **Interconnect and memory:** photonic-link fidelity, rate and distance for the April 2026 demonstration; Lightsynq/EPB quantum-memory specifications.
- **Deployments:** KISTI Tempo acceptance status; number of Tempo units delivered; Google Cloud availability; Tempo availability on any public cloud.
- **Historical records:** the 2021 SPAC investor presentation's technical projections; the full Kerrisdale (2025) and Scorpion (2022) reports and IonQ's detailed rebuttals; the source of an Ezratty critique of the AstraZeneca baseline.
- **2026 items:** the names and results of IonQ's April 2026 13-workload benchmark suite; the roles involved in IonQ's 13 Nov 2026 leadership change (article returned HTTP 403; likely a finance matter covered by the other researcher).
- **Limits data:** newer (post-2019) independent reviews of trapped-ion limits, and IonQ-chip heating, transport and ion-loss rates. The search budget ran out before these could be sought.
