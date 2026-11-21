# TH - AI / HBM / advanced-packaging exposure, technology position, customer-side evidence (Advantest Corporation, TSE Prime 6857)

Fiscal year ends 31 March and is named by its start year: FY2026 = Apr 2026-Mar 2027; FY2026 Q2 = Jul-Sep 2026. Tester-market (TAM) and market-share figures are calendar-year (CY) company estimates in USD. Evidence ids refer to `research/out/advantest/parts/TH.csv`; calculations are in `research/out/advantest/calc/TH_*.py` with outputs in `TH_*.out.txt`. Statement rows carry the fiscal quarter that contains the statement date, e.g. "FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026)". Every [F], [C] and [S] quote was re-found in the saved text by `research/tools/quote_check.py` (184 of 184 found, 12 of them only after layout-insensitive matching because of bilingual or two-column layouts); `row_check.py` reports 0 flags. Adversarial verification log: `parts/TH_verify.md`.

No margin or profit figure is used in this module, so the one-off rule (figures with and without management-named one-offs) does not apply here; margins are in module A1.

## Premise notes

| Premise item | Finding | Tag / ids |
|---|---|---|
| Legal name | Advantest Corporation (EDINET E01950) | [F] TH-001 |
| Listing | Tokyo Stock Exchange Prime, code 6857; moved to Prime in Apr 2022 | [F] TH-002, TH-003 |
| US listing | Listed on NYSE Sep 2001, delisted April 2016 (Annual Securities Report, 84th term, p.8, History) | [F] TH-004 |
| US ADR | Still exists, over-the-counter only: ATEYY, CUSIP 00762U200, 1 ADR = 1 share, depositary JPMorgan Chase Bank, N.A. (Advantest IR share-information page, saved 21 Nov 2026) | [F] TH-005 |
| Listing summary | No US exchange listing; OTC ADR only | [I] TH-195 (High) |
| Fiscal-year naming | Run facts are right: "Q2 FY26" = three months ended 30 Sep 2026; "FY2025" = period ended 31 Mar 2026 | [F] TH-006, TH-007 |
| Segments | Two segments: Test System Business; Services and Others | [F] TH-008 |
| Segment change | The former Mechatronics Systems segment was folded in from FY2025 Q1. Other Systems (handlers, device interfaces, SLT) now sit inside Test System Business | [F] TH-009, TH-010 |
| "Inspection, metrology, test" framing | Advantest is a test (ATE) company. Its only metrology line is the photomask CD-SEM (nanotechnology products, inside Services and Others), which measures mask patterns, not wafers or packages. The latest model is the E3660 (Sep 2025) | [F] TH-011, TH-012, TH-013 |
| Metrology R&D | FY2025 basic research lists "micro area metrology" for structural failures inside devices. No product is disclosed | [F] TH-014 |
| Premise correction | Advantest does not supply wafer or package inspection or metrology for AI chips, HBM or hybrid bonding | [I] TH-194 (High) |
| Hybrid bonding | No hybrid-bonding product. Hybrid-bonding terms (English and Japanese, incl. Cu-Cu and direct bond) appear in 0 of the 164 Advantest-issued documents saved this run, and in 0 of all 180 saved Advantest files; "wafer/defect inspection" and "CoWoS" also appear 0 times. The scan prints its full file list | [I] TH-193 (High) |
| Toray Engineering | The Apr 2024 partnership is about microLED display production, not hybrid bonding | [F] TH-016 |
| Probe cards, sockets | Advantest does not make probe cards in-house. It bought 2.5% of Technoprobe and agreed to buy a small minority stake directly from FormFactor (Jan 2025), and agreed a stake in Micronics Japan (Feb 2025). Sockets and interface boards come from its Advantest Interconnect Solutions unit (Essai 2020, R&D Altanova 2021) | [F] TH-018, TH-019, TH-017 |

Where hybrid bonding does matter is the customers' HBM and 3D-logic stacks. Advantest's exposure there is indirect: it tests the dies before stacking, the stacks, and the final packages (sections 3-4). An academic preprint says a hybrid-bonded die can carry hundreds of thousands to several million I/O pads [S] (TH-155) at 10,000 to 1 million connections per mm2 [S] (TH-156). In an industry survey preprint, 54% of respondents rated hybrid bonding the hardest new architecture for failure analysis [S] (TH-158).

## 1. How much of revenue is AI / HBM / advanced packaging

NOT DISCLOSED (read: Q3 FY2025 Financial Briefing Q&A A4; Q2 FY26 Financial Briefing slides p.15-16; Investors Guide 2610 Ch.1 p.5; Annual Securities Report 84th term; Semi-Annual Securities Report 85th term) - AI, HBM or advanced-packaging share of revenue.

The company's stated policy is to give no breakdown below "Computing and Communications" [F] (TH-126). Its definition, quoted from the Investors Guide (Oct 2026, p.5): "'Computing' in 'Computing and Communications' includes leading-edge devices such as HPC (High Performance Computing) and AI, and 'Communications' include application processors (APs) for smartphones" [F] (TH-128). Management adds that "the majority" of the category is currently on the HPC/AI side, with no number [C] (TH-205).

| Measure | FY2024 (Apr 2024-Mar 2025) | FY2025 (Apr 2025-Mar 2026) | FY2026e (forecast, 2026-10-28) | Tag / ids |
|---|---|---|---|---|
| SoC tester sales, JPY bn | 440.4 | 767.4 | 1,375.0 | [F] TH-130, TH-129; [C] TH-131 |
| Computing / Communications share of SoC sales (rounded to 5%) | 90% | 95% | 90% (forecast, a company claim) | [F] TH-127 |
| PROXY, NOT an AI share: Computing / Communications SoC sales as % of net sales | 50.8% (49.4-52.2) | 64.6% (62.9-66.3) | 66.4% (64.6-68.3) | [I] TH-190 (Medium) |
| SoC test systems as % of net sales | 56.5% | 68.0% | 1H FY2026 (Apr-Sep 2026): 72.5% | [I] TH-192 (High) |
| DRAM share of memory tester sales (rounded to 5%) | 95% | 90% | 85% (forecast, a company claim) | [F] TH-059 |
| Proxy: DRAM tester sales (HBM inside, not split) as % of net sales | - | 13.7% (13.3-14.1) | - | [I] TH-191 (Medium) |

- The proxy is not an AI share: the category includes smartphone application processors [F] (TH-128), so it overstates AI/HPC. The ranges come from the 5% rounding.
- At market level, management said Computing and Communications was about 80% of the CY2025 SoC tester TAM [C] (TH-124). The Japanese text of the same answer ("同分野") makes clear that the 80% refers to the whole category, not to HPC/AI alone. A year earlier, management gave roughly 70% for CY2024 and CY2025 [C] (TH-125).

## 2. The company's test-intensity thesis and its limits

| Statement (speaker, date) | Tag / id |
|---|---|
| The rise in test volume is structural, driven by complexity (Nov 2024) | [C] TH-021 |
| Exponential transistor growth caused "explosive growth" in scan test volume; scan coverage is typically 95-99.5% | [C] TH-027, TH-028 |
| The 2020s add die-specific test insertions plus multi-temperature, burn-in and SLT | [C] TH-029 |
| More dies per package mean longer test time; die-to-die interconnects add test items | [C] TH-025, TH-026 |
| HPC device cycles are about one year, leaving little time for test-time optimisation | [C] TH-024 |
| Test demand is driven more by test content than by production volume (Oct 2024) | [C] TH-031 |
| High ASPs and costly packages make customers test more rather than scrap (Oct 2024, Nov 2025) | [C] TH-032, TH-033 |
| "In some cases" test times rise "by multiples" from one generation to the next (CEO, 2026-11-12) | [C] TH-034 |
| Accelerators with 3D packaging bring longer test times and extra insertions. At final test, accelerators need more test intensity than CPUs (Jul 2026) | [C] TH-036, TH-037 |
| Agentic-AI CPU test demand is the largest factor in the raised FY2026 SoC forecast (Oct 2026) | [C] TH-041 |
| Tester TAM has grown at an annual average of about 50% or slightly above over the past few years; no slowdown seen; CY2027 figures promised for the January 2027 briefing (Oct 2026) | [C] TH-042 |

Counterpoints from the same company documents:
- Test times, volume and insertions are "very difficult to predict" [C] (TH-022). They stay uncertain until the device is in silicon [C] (TH-035).
- Customers are generating more efficient patterns to cut scan test time [C] (TH-023).
- Part of the roughly 30% raise to the CY2025 SoC TAM reflected caution in the January and April forecasts; the rest leaned more to unit volume than to test content [C] (TH-038). The CY2026 TAM growth was attributed mainly to custom-ASIC unit volume [C] (TH-039).
- Management says GPU and custom ASIC test content is comparable [C] (TH-040).
- Chinese SoC tester vendors are growing in the low-end China market [C] (TH-043).

Advantest's growth explanation mixes test intensity and unit volume, and no test-time-per-device series is disclosed [I] TH-197 (Medium).

## 3. HBM and memory test

| Item | Tag / id |
|---|---|
| Worked with HBM customers for more than 10 years (Apr 2024) | [C] TH-048 |
| Stricter HBM quality requirements drive rigorous testing | [C] TH-049 |
| HBM3 to HBM3E to HBM4 adds speed, density, thermal-control, power-management and handling requirements (Jun 2024) | [C] TH-051 |
| Memory testers average lower margins than the company mix (qualitative, no figure). The fix is upgrades plus new high-value HBM4 testers | [C] TH-052, TH-053 |
| HBM tester sales "not slowing" (Oct 2024, answering a competitor's view of a decline). Profit gains from upgrades came slower than planned | [C] TH-054, TH-055 |
| HBM4/HBM4E and higher stacks are a key memory-tester growth driver (Jul 2025) | [C] TH-057 |
| FY2025 Q2 (Jul-Sep 2025): memory test system sales JPY 43.9 bn; high-performance DRAM including HBM increased | [F] TH-058 |
| DRAM output allocation is shifting to HBM and server DRAM; DRAM is also a cost headwind for Advantest's own testers (Oct 2026) | [C] TH-060 |
| CY2025 memory tester share fell about 2 points to around 60% | [C] TH-064 |
| Memory share "may experience a decline" in CY2026. NAND is not a traditional stronghold. New products with customer commitments are coming (Jul 2026) | [C] TH-061, TH-062, TH-063 |
| T5801 DRAM tester (36 Gbps PAM3), global release early 2026. M5241 AI-memory handler, first shipments Q2 CY2026 | [C] TH-082, TH-083, TH-084 |

## 4. Die-level, KGD/KGS, SLT and burn-in

| Item | Tag / id |
|---|---|
| A real KGD needs accurate die-level test with high-performance thermal control. Complexity is adding insertions at wafer sort and die level (Jan 2025) | [C] TH-065, TH-066 |
| No significant die-level test revenue expected in CY2025 (Jan 2025) | [C] TH-067 |
| Wafer sort is growing faster than final test as chiplets make packages expensive (Jul 2025) | [C] TH-068, TH-069 |
| Die-level probe for KGD and known-good chip-on-wafer "appears later next year" (CY2026) to ramp, followed by several years of high growth (CEO, 2025-11-17) | [C] TH-070 |
| Wafer-level power, heat and warpage push customers to die-level KGD test at hot temperature | [C] TH-071 |
| Joint development of an HPC die-level prober with Tokyo Seimitsu announced 2025-12-16 | [F] TH-072 |
| MTP3 roadmap: HBM die-carrier solution and die-level handling for 3D chiplets | [C] TH-073 |
| FormFactor/Advantest SWTest 2025 poster (conference presentation, not peer-reviewed): singulated HBM stack test up to 4 GHz. Stack-die test claimed at 100% efficiency vs 90/80/70% for post-stack wafer test | [C] TH-075, TH-076 |
| 2017 Advantest/FormFactor known-good-stack HBM2 cell (SWTest 2017, conference presentation, not peer-reviewed): T5503HS tester + HA1000L die-level handler | [F] TH-077 |
| GPU/ASIC makers exploring combined burn-in and SLT (Oct 2024). SLT business "not large" | [C] TH-078, TH-079 |
| 7038 STR SLT/burn-in: liquid cooling up to 1.4 kW per site | [F] TH-080 |
| FY2026 Q2 SLT sales rose mainly on consumer electronics, not AI | [F] TH-081 |

## 5. Dated product, roadmap and capacity claims

| Date stated | Claim | Tag / id |
|---|---|---|
| 2024-12-10 | HA1100 die prober (power-semiconductor KGD) global release in the second quarter of 2025 | [C] TH-074 |
| 2025-02-12 | T5801 in use at strategic memory customers; global release early 2026 | [C] TH-082 |
| 2025-02-20 | SiConic product introduced (company news index) | [F] TH-087 |
| 2025-07-29 | Can ship more than 3,000 V93000 systems a year | [C] TH-092 |
| 2025-11-17 | SoC tester capacity of at least 5,000 systems by end FY2026 (Mar 2027), then 7,500 within a couple of years, then 10,000 | [C] TH-091 |
| 2025-12-10 | M5241 handler: first shipments Q2 CY2026; "multiple major memory manufacturers" preparing to adopt | [C] TH-083, TH-084 |
| 2026-04-22 | Pin Scale 5000B "now ramping with key customers" | [C] TH-085 |
| 2026-04-27 | Claims to lead silicon-photonics test; market to more than double next year | [C] TH-089 |
| FY2025 (IAR 2026-11-11) | First large ATE volume-production order in silicon photonics | [C] TH-088 |
| 2026-07-29 | 10,000-system target equals about 20,000 systems in 2020 configuration | [C] TH-095 |
| 2026-10-28 | More than 5,000 systems/year achieved; 10,000 (originally end FY2028) pulled in, no date given; 20,000 under discussion | [C] TH-093, TH-094 |
| 2026-10-28 | CPO tester market to double or triple annually to about USD 1 bn | [C] TH-090 |
| 2026-11-17 | V93000 EXA Scale QX (36 slots) available in the first quarter of FY2027 (Apr-Jun 2027) | [C] TH-086 |

## 6. Market size and share claims

Company TAM estimates (USD bn, "Source: Advantest"), first estimate vs latest or final:

| Market | First estimate | Path | Final / latest | Change vs first midpoint | Tag / ids |
|---|---|---|---|---|---|
| SoC CY2024 | 3.3-3.6 (Jan 2024) | 2.9-3.2 (Apr 2024) | 4.1 | +18.8% (+34.4% vs the cut) | [C] TH-104, TH-106, TH-099; [I] TH-186 |
| SoC CY2025 | 4.2-4.8 (Jan 2025) | 5.7-6.3 (Jul), 6.5-6.9 (Oct 2025) | 6.9 | +53.3% | [C] TH-107, TH-109, TH-110, TH-096; [I] TH-184 |
| SoC CY2026e | 8.5-9.5 (Jan 2026) | 8.7-9.5 (Apr), 10.5-11.5 (Jul 2026) | about 11.5 (Oct 2026) | +27.8% | [C] TH-111, TH-113, TH-114, TH-102; [I] TH-185 |
| Memory CY2024 / CY2025 / CY2026e | 1.3-1.6 / 1.7-2.2 / 2.2-2.7 | - | 1.9 / 2.1 / 2.5-3.0 (around midpoint) | +31.0% / +7.7% / +12.2% | [C] TH-105, TH-100, TH-108, TH-097, TH-112, TH-103; [I] TH-199 |
| Total | - | - | 4.4 (CY23), 6.0 (CY24), 9.0 (CY25), 13.0-14.5 (CY26e) | YoY +36.4%, +50.0%, +44.4% to +61.1% | [C] TH-179, TH-098, TH-101; [I] TH-187 |

- The CY2023-26e CAGR is 43.5-48.8%, slightly below management's "about 50% or slightly above", whose window is not defined [I] TH-187 (High).
- The CY2024-26 TAM now averages 9.33-9.83 USD bn, 58-67% above the 5.9 USD bn the MTP3 plan assumed for that period in June 2024 [I] TH-188 (High).
- Teradyne also puts the 2025 ATE TAM at about USD 9.0 bn. Its target-model TAM (USD 12-14 bn) overlaps Advantest's CY2026 forecast [C] TH-175; [I] TH-189 (Medium).

Share claims and checks:

| Item | Value | Tag / ids |
|---|---|---|
| Overall tester share | 58% (CY2023), 58% (CY2024), 65% (CY2025) | [C] TH-120, TH-115 |
| SoC tester share | 59% (CY2023), 56% (CY2024), 66% (CY2025); "path to above 70%" | [C] TH-119 note, TH-116, TH-117 |
| Memory tester share | 56% (CY2023), 63% (CY2024), 61% / "around 60%" (CY2025); may decline in CY2026 | [C] TH-119, TH-064, TH-061 |
| AI accelerator test | "Captured a majority share of the market globally" (no number) | [C] TH-118 |
| MTP3 assumption | Share above 58% for the CY2024-26 average (MTP2 CY2021-23: 54%) | [C] TH-122 |
| Check: CY2025 SoC sales / own SoC TAM | 66.0%, in line with the 66% claim | [I] TH-180 (Medium) |
| Check: CY2024 SoC sales / own SoC TAM | 56.6%, in line with the 56% claim | [I] TH-204 (Medium) |
| Check: CY2025 memory sales / own memory TAM | 54.0% vs 61% claimed (7.0 points below) | [I] TH-181 (Medium) |
| Check: CY2024 memory sales / own memory TAM | 54.3% vs 63% claimed (8.7 points below) | [I] TH-204 (Medium) |
| Check: Jul-Sep 2026, Advantest vs Teradyne only | SoC 76.4% (3.25x Teradyne); memory 52.4% (1.10x) | [I] TH-182, TH-183 (Low) |

The SoC share claims reconcile with reported SoC Test Systems sales in both years; the memory share claims do not, in either year. Because the gap recurs, a difference in definition (for example memory handlers or interfaces counted in the share, or a shipments basis) is more likely than FX or timing [I] TH-181 (Medium). The method itself is a gap:

NOT DISCLOSED (read: FY25 Financial Briefing slides p.18 "Source: Advantest"; FY2025 briefing notes p.13; Q2 FY2026 Q&A A2) - method behind the tester TAM and share estimates.

## 7. Technical papers bearing on test demand (open access, saved)

None of the six saved arXiv papers prints a peer-reviewed or conference venue, and their arXiv records have no journal reference or DOI (saved metadata: `research/sources/advantest/2026-11-21_arxiv_api-metadata-TH-papers.xml`; YAP+ is "under review by IEEE TCAD"). Under the evidence rules they are therefore [S], not [F].

| Source | What it states | Tag / id |
|---|---|---|
| Mitra et al., Google (arXiv 2508.01786, Aug 2025, preprint) | Data-center compute chips escape manufacturing test at ≥10x industrial targets: about 5,000 DPM vs 100-500 DPM expected | [S] TH-150, TH-151 |
| Same | More than several minutes of per-chip manufacturing test time is "often regarded as impractical". The paper proposes in-field testing, where far longer tests are economic | [S] TH-152, TH-153 |
| CATCH (UCLA/ASU/Etched, arXiv 2503.15753, preprint) | 16-chiplet 2.5D case: low die-level fault coverage gives very high scrap cost; the cost optimum is at 95% coverage (immature node case) | [S] TH-154 |
| YAP+ (UCLA, arXiv 2511.05506, preprint under review) | Hybrid-bonded dies may carry hundreds of thousands to several million pads, at 10,000 to 1 million connections per mm2 | [S] TH-155, TH-156 |
| DT-MATCH (ASU with Ampere Computing, arXiv 2611.19544, preprint) | Chiplet packages make testing and repair "a first-order concern"; pre-bond test data drives chiplet matching | [S] TH-157 |
| FA industry survey (arXiv 2606.22149, preprint) | Hybrid bonding is the most difficult new architecture to analyse (54% of respondents) | [S] TH-158 |
| Sadi and Guin (arXiv 2006.04798, preprint) | With 5% faulty processing elements, AI accelerator accuracy degrades by less than 1%, so binning can reduce scrap | [S] TH-159 |

The open literature points to rising test pressure per chip. It also shows a ceiling on ATE time per chip, plus routes that move test out of ATE: in-field test and fault-tolerant binning [I] TH-196 (Medium). These sources are preprints [S] and conference presentations [F], so the inference rests on secondary-grade evidence.

NOT RETRIEVED (tried: Firecrawl paper search and WebSearch; IEEE Xplore is paywalled) - peer-reviewed ITC / VTS / ECTC papers on HBM known-good-stack test, pre-bond test of 3D stacks and hybrid-bond interconnect test.

## 8. Customer-side and competitor-side evidence

| Source | What it states | Tag / id |
|---|---|---|
| SK hynix with FormFactor, SWTest 2021 (conference presentation, not peer-reviewed) | Known-good-die/stack (KGDS) test cuts advanced-packaging cost. HBM has three test-insertion choices. The KGS HBM2 and KGD LPDDR4 probe cards were built for Advantest T5503 HS2 testers | [F] TH-160, TH-162, TH-161 |
| SK hynix, Hot Chips 28 tutorial (2016, conference tutorial, not peer-reviewed) | HBM carries IEEE1500 test/repair features for test after SiP assembly. The flow has hot/cold test, repair and a KGSD speed test | [F] TH-163 |
| TSMC award (Advantest release, 2025-12-24) | Recognised for flexibility in expanding production capacity | [F] TH-164 |
| Micron, Fiscal Q4 2026 remarks (2026-09-30) | Says agreements are done for the vast majority of its CY2027 HBM bit supply; nothing on test | [C] TH-165 |
| Teradyne Q3 2026 (quarter ended 27 Sep 2026) | Revenue: SoC USD 676 m, memory USD 301 m (a record) [F] TH-166, TH-167; Teradyne attributes the record to HBM/DRAM and NAND [C] TH-206 (split from TH-167 in fix round 1). The two plus IST USD 95 m equal the USD 1,072 m Semi Test revenue in the press release | as shown |
| Teradyne | Test share of semiconductor capex rose from 6.4% (2025) to 8.1% (Jan-Aug 2026) | [C] TH-169 |
| Teradyne | Claims higher share in HBM performance test. Says lower HBM stack heights raise that TAM | [C] TH-168 |
| Teradyne | Dual-vendor progress: first hyperscaler in the mature phase (next ramp mid-2027); merchant GPU customer in fast follower (revenue 2027); second hyperscaler in fast follower (capacity buys 2H 2027); third in qualification. Mature-vendor share range 30-70% | [C] TH-170, TH-171, TH-172, TH-173 |
| Teradyne | "No current ATE solution" for the most complex 2027 AI devices; launched new UltraFLEX instruments | [C] TH-174 |
| Teradyne | 2025 compute product revenue USD 753 m (USD 109 m in 2023) | [F] TH-176 |
| Teradyne | Partnerships with Technoprobe and FiconTEC; new partnership with FormFactor | [F] TH-177 |
| Teradyne | Frames ATE as a duopoly (Analyst Day 2025) | [C] TH-178 |

Teradyne reports dual-vendor wins with 2027 ramps, while Advantest claims a path to SoC share above 70%. The saved documents cannot settle which prevails [I] TH-198 (Medium).

## 9. What the module leans on

1. Advantest's AI/HPC exposure is visible only through a proxy that is not an AI share: Computing/Communications SoC sales at about 65% of FY2025 net sales [I] TH-190, a category the company defines to include smartphone APs [F] TH-128.
2. The SoC share claims (56% CY2024, 66% CY2025) reconcile with reported sales and the company's own TAM; the memory share claims do not in either year (54% implied vs 63% and 61%) [I] TH-180, TH-204, TH-181.
3. The TAM has repeatedly been revised up, by +28% to +53% from first estimates for CY2025-26, and in both directions for CY2024; management says part of the CY2025 raise reflected earlier caution [I] TH-184 to TH-186; [C] TH-038.
4. Advantest is not an inspection/metrology or hybrid-bonding supplier; the premise is corrected [I] TH-194, TH-193.
5. The main competitive risk in the documents is Teradyne's dual-vendor programme at hyperscalers and the merchant GPU customer [C] TH-170 to TH-172; [I] TH-198.

Handoff candidates (for B5):
- Theme share of revenue (company definition): NOT DISCLOSED as an AI, HBM or advanced-packaging share. Company category "Computing and Communications" (Computing = leading-edge devices such as HPC and AI; Communications = smartphone APs) was 95% of FY2025 SoC tester sales, rounded to 5% [F] TH-127, TH-128; as a proxy, 64.6% (62.9-66.3%) of FY2025 net sales (Apr 2025-Mar 2026), not an AI share [I] TH-190.
- Main strength: SoC tester share 66% in CY2025, up from 56% (company estimate) [C] TH-116, and it reconciles with reported SoC sales over the company's own TAM in both years [I] TH-180, TH-204.
- Main vulnerability: Teradyne's dual-vendor programme at two hyperscalers and the merchant GPU customer, with ramps in 2027 [C] TH-170 to TH-172; secondary: memory tester share slipping and a share claim that does not reconcile with sales [C] TH-061; [I] TH-181, TH-204.

## Run notes for the integrator

- Files I saved this run (all through fetch.py, issuer in the name):
  - 12 Advantest news releases (2024-04-10 to 2026-11-17)
  - 6 arXiv PDFs, plus (verifier) the arXiv API metadata record for the six papers
  - 3 conference PDFs (SWTest 2017, 2021, 2025)
  - SK hynix Hot Chips 28 tutorial
  - Teradyne: IR home page, presentations index, Q3 2026 release, remarks and slides, Q4 2025 slides, Analyst Day 2025
  - Micron Fiscal Q4 2026 remarks
- Manifest rows that point to deleted files:
  - The first arXiv attempt saved 6 PDFs under `.html` names dated 2026-11-21 (URLs without the `v1` suffix). I deleted those files and their text copies and re-saved the papers as `.pdf` with v1 URLs and submission dates.
  - A PMC fetch returned a reCAPTCHA page. I deleted it without working around it (see gaps).
  - All 7 of these manifest rows still read RETRIEVED; the manifest was not edited because other agents append to it.
- Two attempts at Teradyne URLs returned 404 and are logged NOT RETRIEVED in the manifest. Firecrawl credits ran out mid-run, so later searches used WebSearch.
