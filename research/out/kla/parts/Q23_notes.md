# Q2 / Q3 notes: KLA advanced packaging vs Onto and Camtek; hybrid-bonding coverage

KLA fiscal year ends June 30. Calendar years (CY) are used for AP revenue because KLA states them that way. Onto and Camtek have December year-ends. No per-share figures are used here. Evidence ids refer to `parts/Q2.csv` and `parts/Q3.csv`. Arithmetic: `calc/q2_ap_revenue.py`.

## Q2-A. KLA advanced-packaging (AP) revenue: two definitions

KLA uses two different AP figures. The prior chat put them side by side as if they were the same thing.

| Period | Figure | KLA definition (wording) | Date stated | Evidence |
|---|---|---|---|---|
| CY24 (Jan-Dec 2024) | > $500M, later "~$500M" | "total advanced packaging revenue across the entire KLA portfolio" | 2024-07-24, 2025-01-30 | [C] Q2-001, Q2-002 |
| CY25 estimate | > $925M; process control "over 70%" of it | "advanced packaging related revenue" | 2025-07-31 | [C] Q2-003 |
| **CY25 actual, total** | **~$950M, ">70% YoY"** | "calendar 2025 total systems revenue" (all KLA AP systems) | 2026-01-29 | [C] Q2-005; same on Investor Day slide 68 [C] Q2-012 |
| **CY25 actual, process control** | **~$635M** | "Semiconductor Process Control product portfolio revenue" | 2026-04-29 | [C] Q2-007 |
| CY26 guide (Jan 2026) | mid-teens growth | total-systems basis | 2026-01-29 | [C] Q2-006 |
| CY26 guide (early 2026) | > 30% growth | Semi PC basis | quoted in Apr 2026 letter | [C] Q2-008 |
| CY26 guide (Apr 2026) | ~$1.0B | Semi PC product portfolio | 2026-04-29 | [C] Q2-008 |
| CY26 guide (Jul 2026) | ~$1.1B, ">70% YoY", "almost two times faster than the advanced packaging market" | "Advanced Packaging process control systems revenue" | 2026-07-28 | [C] Q2-009 |
| **CY26 guide, latest** | **~$1.1B, ">70% YoY", reaffirmed** | same as Jul 2026 | **2026-10-28** (Q1 FY27 letter) | [C] Q2-010; call summary [S] Q2-030 |
| CY27 | no AP-specific figure; AP is named among the drivers of 2027 capacity growth | n/a | 2026-07-28 | [C] Q2-011. AP CY27 revenue: NOT DISCLOSED (read: Q4 FY26 and Q1 FY27 letters, Outlook sections) |

Arithmetic [I] (`calc/q2_ap_revenue.py`):
- The prior-chat pair does not reconcile: $950M × 1.70 = $1,615M, not $1.1B, and $1.1B / $950M = +15.8%. $950M is total AP systems revenue; $1.1B is AP process-control systems revenue. [I] Q2-I02, High.
- Like for like, $1,100M / $635M = **+73.2%**, consistent with KLA's ">70%". [I] Q2-I01, High.
- The CY26 process-control guide was raised twice and then held: >30% → +57.5% (~$1.0B) → +73.2% (~$1.1B) → reaffirmed on 2026-10-28. [I] Q2-I05.
- CY25 split: process control was $635M, 66.8% of the $950M total. The remaining ~$315M covers SPTS process tools plus PCB/Component lines (ICOS, Zeta, Orbotech) and is not broken out further. The July 2025 statement (">70% of >$925M", i.e. >$647.5M) was not met by the final $635M. [I] Q2-I03, Medium.
- The CY24 base is inconsistent: $950M / $500M = +90%, while KLA says "over 70%". The CY24 base was therefore up to ~$559M, or the definition changed. [I] Q2-I04, Medium.
- Investor Day slide 100 calls the ~$950M "process control solutions" revenue. The letters are more specific, so treat the slide wording as loose. [I] Q2-I08.

Split by product family, from 10-K FY26 Item 1 segment tables:

| Bucket | Segment | Product lines named for packaging | In $635M / $1.1B process-control figure? |
|---|---|---|---|
| Inspection and metrology (process control) | Semiconductor Process Control | Kronos Series, Micro-SR, CIRCL-AP, irArcher Series, PWG5 with XT Option, eDR7xxxAP, OmniMap RS-xxx, QualiSurf [F] Q2-019. The Investor Day AP slide also lists Puma, Voyager, 29xx, Surfscan, Archer, Aleris, SpectraShape, Lumina, Klarity, 5D Analyzer (slide 66) | Yes (segment basis; inference) |
| Component inspection and metrology | PCB and Component Inspection | ICOS F26x, ICOS Tx Series, Zeta-5xx/6xx [F] Q2-020; Orbotech Corus/Precise for IC substrates | No; part of the ~$315M residual (inference) |
| Process equipment | Specialty Semiconductor Process | SPTS Omega, Sigma, Delta, Osprey, Mosaic, MVD, Primaxx, Xactix: etch, plasma dicing, deposition [F] Q2-021; "primarily focused on process tools for advanced packaging and specialty device manufacturing" [F] Q2-022 | No |

- FY26 (Jul 2025-Jun 2026) segment revenue: Specialty Semiconductor Process $584M; PCB and Component Inspection $750M (+21%, "primarily driven by" AP customers). [F] Q2-023, Q2-024. AP share of each segment: NOT DISCLOSED (read: 10-K FY26 Item 7; Annual Report 2026).
- No margin figure is involved in Q2/Q3, so there are no one-off adjustments.

## Q2-B. Tool-level wins and losses vs Onto and Camtek (non-KLA sources)

| KLA tool | Non-KLA report of a specific KLA win or loss | What competitors report nearby |
|---|---|---|
| Kronos 1190 / 1190XR (2D patterned AP inspection) | None found | Onto: an HBM maker chose Dragonfly G5 + 3Di after onsite competitive evaluations, "displacing the previously established tool of record" (incumbent not named) [C] Q2-029. Camtek: >$50M Hawk orders from "a leading HBM player" [F] Q2-035 |
| CIRCL-AP (all-surface cluster) | None found | Onto Dragonfly G5 qualified for 2.5D (second qualification) [C] Q2-031 |
| ICOS F26x / T-series (component, post-dice) | None found | n/a (Onto and Camtek do not target final component inspection in the saved documents) |
| Zeta-5xx/6xx, Micro-SR, eDR AP, irArcher, PWG5 XT | None found | n/a in saved documents |

- Result: **no non-KLA source located names a specific KLA packaging win or loss.** Competitors' win releases do not name the vendor they displaced. [I] Q2-I07.
- Onto's 10-K names "KLA and Camtek" as its principal AP-inspection competitors. [F] Q2-028
- Camtek's 20-F names no competitor. It describes about six months of side-by-side competitive evaluations. [F] Q2-033. Its Oct 2026 deck says "Compete with larger players" without naming them. [C] Q2-037
- KLA's own view: AP process-control share above 50% in 2025, "more concentrated in leading edge logic", with memory and OSATs named as opportunities. [C] Q2-015. #1 share, +14 pp. [C] Q2-014
- Scale for comparison: Camtek's Q3 2026 revenue was $161.3M and its FY26 guide is ~$595M [F] Q2-038; >$800M orders YTD, ~80% AP [C] Q2-036. Onto's Q3 2026 revenue was $409.7M, with record AP revenue led by Dragonfly G5/Firefly [F] Q2-032.
- Onto frames AP demand as "driven by assembly volumes" [F] Q2-039. KLA frames it as intensity plus share.
- Leads not saved: an Onto technology award from SK hynix for Dragonfly G5 (Zacks via web search, not retrieved) and DigiTimes CoWoS tool allocation (paywalled). Neither names KLA.

## Q3. Hybrid-bonding coverage map

| Step | KLA tool offered | Status (evidence) | Gap | Onto | Camtek |
|---|---|---|---|---|---|
| Incoming wafer shape / flatness, bow, warpage | PWG5 with XT Option (packaging list) | Listed in 10-K FY24-FY26 [F] Q3-005. HB/D2W shipment status NOT DISCLOSED (read: 10-K FY26 Item 1) | No die-level warpage product named | Not in saved docs | Pre-bond wafer and die warpage: 2027-28 roadmap [C] Q3-017 |
| Pre-bond surface defects / particles | Puma, Voyager, BBP (29xx/Gen4). KLA says Kronos "not going to be sufficient" [C] Q3-003; "whole suite of systems", "next four systems" developed [C] Q3-001, Q3-002 | Announced/ready per KLA (Mar 2026). HB-specific HVM shipments NOT DISCLOSED (read: Investor Day transcript p30, p78; 10-K FY26 Item 1) | KLA's target: 0.05-0.5 µm sensitivity [C] Q3-004 | Dragonfly G5 150 nm [C] (Q2-029 release) | Hawk 150 nm, marketed for HB [F] Q2-034; <150 nm HB requirement [C] Q3-018 |
| Cu recess / dishing, topography | Not named for HB in saved docs. Candidates on slide 66 (SpectraShape, Zeta, Aleris) are an inference only | Status NOT DISCLOSED (read: 10-K FY26 Item 1; Investor Day slides 66-67) | KLA's target: 0.001 µm Cu-recess accuracy [C] Q3-004 | 3Di (bumps) | Post-CMP dishing/roughness: 2027-28 roadmap [C] Q3-017 |
| Bond overlay (post-bond, IR) | irArcher Series | Listed in 10-K [F] Q3-005. The ST/KLA ECTC 2023 paper (irArcher 007 for W2W) is a lead only (403). D2W status NOT DISCLOSED (read: 10-K FY26 Item 1; Investor Day deck) | Precision specs not retrievable | Not in saved docs (TheElec says PLA can also measure overlay [S] Q3-014) | Not in saved docs |
| Post-bond buried voids | **None found** | [I] Q3-I01 | Gap | EchoScan (launched Jan 2025, ≥1 µm voids) [C] Q3-012; PLA SPIE 2026 [F] Q3-010, [C] Q3-011; in validation on Samsung production lines [S] Q3-014 | 2027-28 roadmap item [C] Q3-016 |

- Onto, describing the incumbent void method (unnamed, presumably SAM): "≥10µm void size sensitivity", water immersion required. [C] Q3-013
- Samsung is also talking to several ultrasound and X-ray vendors (not named) [S] Q3-015. SAM vendors (e.g. PVA TePla, Hitachi, Sonix) are not covered by any saved source: NOT RETRIEVED (tried: TheElec article only; no further search of SAM vendors).
- KLA on HBM: two stacking processes are in use, and failure rates rise "on a log scale" with stack height [C] Q3-007. Both HB and TC-NCF raise intensity, and KLA is "not choosing" [C] Q3-008. The Annual Report says customers "increasingly adopted" HB in FY26 [C] Q3-006.
- Post-bond voids at KLA: no product, partnership, acquisition or stated intent appears in the 10-K FY26, the 10-Q for Q1 FY27, Annual Report 2026, the Investor Day deck and transcript, or the letters [I] Q3-I01. The IMAPS 2026 KLA paper abstract is generic [F] Q3-019. KLA job postings: NOT RETRIEVED (tried: none; no search was run in this session). SPIE/ECTC full texts by KLA authors (e.g. 10.1117/12.3049615 "Shape-induced overlay for W2W hybrid bonding", 2025; affiliations not shown in Crossref): NOT RETRIEVED (tried: Crossref metadata only).

## Ledger evidence (B1 input)

| Claim | For | Against | Strongest tag (for / against) |
|---|---|---|---|
| Process-control intensity rises with AP and HBM | KLA packaging intensity (KLA Semi PC AP revenue / AP market) 0.4% (2018) → 5.6% (2025) [C] Q2-016; HB specs ~10x tighter (0.05-0.5 µm vs 1-5 µm) [C] Q3-004; HBM gave a $450M incremental intensity gain in CY25 [C] Q2-018; KLA's CY26 AP process-control growth is ~2x the AP market [C] Q2-009; Camtek: <150 nm HB particle sensitivity, more RDL steps [C] Q3-018; Onto: AP inspection rates are high [F] Q2-039 | KLA's "intensity" metric mixes share gain with intensity (KLA's own definition, Q2-016). Process control's share of AP capex is NOT DISCLOSED (read: Investor Day slide 143, a chart without data labels; a visual read puts it at ~$1.3B of ~$11.3B, [I] Q2-I06, Low). Onto: AP demand is driven by assembly volumes [F] Q2-039. No third-party quantified intensity figure found | [C] / [F] |
| AP revenue exceeds $1.1B in CY26 | Guide ~$1.1B (>70%) on 2026-07-28, reaffirmed 2026-10-28 [C] Q2-009, Q2-010; call summary [S] Q2-030 | It is "approximately $1.1B", not "exceeds". The definition is AP **process control systems** only. On the total-systems basis the Jan 2026 guide (mid-teens on $950M ≈ $1.07-1.11B) was never updated [C] Q2-006; KLA has not given a CY26 total-AP figure since. CY26 actual is not reported until late Jan 2027 | [C] / [C] |
| Post-bond buried-void inspection stays outside KLA's portfolio | No void product or intent in KLA filings, deck or transcript [I] Q3-I01; Onto has a launched tool and a Samsung JDP [C] Q3-012, [S] Q3-014 | KLA says it has a "whole suite" of HB systems and four more developed (unnamed) [C] Q3-001, Q3-002. kla.com product pages were not retrievable, so an unlisted product cannot be excluded. Camtek is also only at roadmap stage [C] Q3-016 | [I] / [C] |

## Competition table for the handoff (step by step; names from saved sources)

| Step | KLA | Onto | Camtek |
|---|---|---|---|
| 2D patterned AP inspection (bumps, RDL, post-dice) | Kronos 1190/1190XR, CIRCL-AP; Puma/Voyager/29xx adapted [F] Q2-019, [C] Q2-026 | Dragonfly G5 (150 nm) [C] Q2-029; Firefly (panel) [F] Q2-032 | Hawk (150 nm), Eagle G5 / Eagle-i / Eagle-AP [F] Q2-034 |
| 3D bump metrology | Zeta-5xx/6xx, Micro-SR (inference: segment lists, no spec retrieved) | 3Di on Dragonfly [C] Q2-029 | Eagle-AP / Hawk 3D metrology; 10th-generation sensor for <5 µm bumps in 2027 [C] (Camtek deck p17) |
| Defect review | eDR7xxxAP [F] Q2-019 | not in saved docs | not in saved docs |
| Wafer/die shape, warpage | PWG5 XT [F] Q3-005 | not in saved docs | roadmap [C] Q3-017 |
| Bond overlay | irArcher [F] Q3-005 | not in saved docs | not in saved docs |
| Post-bond voids | none found [I] Q3-I01 | EchoScan / PLA [C] Q3-012 | roadmap [C] Q3-016 |
| Final component inspection | ICOS F26x / Tx [F] Q2-020 | n/a | n/a |
| Process tools (etch, dicing, deposition) | SPTS (Specialty Semiconductor Process) [F] Q2-021 | lithography (JetStep) | n/a |

## Prior-claim check (prior/text/kla_metrology_audit.md)

| Prior claim | Result | Evidence |
|---|---|---|
| "Total AP revenue ~$950M in CY25" | MATCHES SOURCE (total systems basis) | [C] Q2-005, Q2-012 |
| "AP Process Control Systems revenue on track for $1.1B+ in CY26 (+70%+ YoY)" | CORRECTED: "approximately $1.1 billion", not "$1.1B+"; growth >70% on a $635M process-control base, not on $950M | [C] Q2-010, [C] Q2-007, [I] Q2-I01, Q2-I02 |
| "share ~4x over 4 years" | MATCHES SOURCE as KLA claim | [C] Q2-013 |
| "irArcher 007 post-bond IR overlay 1.5-3.3 nm precision across 100-350 µm die" | UNSUPPORTED: irArcher Series is in the 10-K, but no saved source gives these numbers (kla.com JS challenge; ECTC 2023 PDF 403; IMAPS abstract silent) | [F] Q3-005, [F] Q3-019 |
| "PWG5 XT option" | MATCHES SOURCE (10-K FY24-FY26: "PWG5 with XT Option") | [F] Q3-005 |
| "Kronos 1190XR down to 150 nm" | UNSUPPORTED from KLA (the 2020 release gives no nm figure; kla.com not retrievable; DirectIndustry 403). Also, KLA says Kronos is not sufficient for HB, so its use as an HB pre-bond tool is CORRECTED | [F] Q2-027, [C] Q3-003 |
| "IMAPS 2026-08-11 doi 10.4071/001c.171430" | CORRECTED: the DOI resolves to Chet Lenox (KLA), "AI-Driven Process Control for Advanced Packaging", IMAPSource Proceedings, Crossref date 2026-09-21 (an 08-11 event date is not shown). The abstract does not support the irArcher, Kronos or void details the prior chat cited to it | [F] Q3-019 |
| "Samsung + Onto SPIE 2026 doi 10.1117/12.3095356 PLA 1 µm voids under 665 µm Si" | PARTLY MATCHES SOURCE: the DOI, title and 1 µm figure check out; it was presented 2026-02-24 and published 2026-04-08 (not "Apr 8 presentation"). Samsung co-authorship and "665 µm Si" are UNSUPPORTED (no affiliations in Crossref; the abstract lacks 665 µm). A Samsung–Onto JDP is reported by [S] TheElec | [F] Q3-010, [C] Q3-011, [S] Q3-014 |
| "HBM hybrid bonding future adoption; 8H/12H and 12H/16H remain TCB" | UNSUPPORTED as a KLA statement. KLA says DRAM moves to HB "in the future" and it is indifferent; the deck shows "8 to 12 chip stacks"; no 16H/TCB roadmap appears in the KLA deck or transcript | [C] Q3-009, Q3-008 |
| "KLA has no commercial post-bond buried-void tool" | MATCHES SOURCE as absence in saved KLA documents (inference) | [I] Q3-I01 |
| KLA row "zero post-bond buried-void PLA tool" | MATCHES SOURCE (same basis) | [I] Q3-I01 |

## Premise issues

- The prompt's "$1.1B" and "$950M" use different definitions: process-control systems vs total systems (see Q2-A).
- The CY26 process-control guide is "approximately $1.1 billion", not "$1.1B+" or "exceeds $1.1B".
- The transcript renders Kronos as "Chronos" (p29-30) and "corona" (p78).
- The prompt names "CIRCL" lines; the 10-K spells it CIRCL-AP (Semi PC). ICOS and Zeta sit in the PCB and Component Inspection segment, not Semi PC. "Frontier" does not appear in the 10-K FY26; the PCB line is "Frontline". The Orbotech packaging-related lines are Corus/Precise (IC substrate).
- IMAPS DOI date: Crossref gives 2026-09-21, not 2026-08-11.
- SPIE 2026 PLA paper: Onto presented it on 2026-02-24; proceedings were published 2026-04-08.

## Retrieval notes (for the lead)

- www.kla.com serves a JavaScript bot-challenge page to fetch.py. These saved files contain no content and were set to NOT RETRIEVED in the manifest by the lead (tried: fetch.py on kla.com, JavaScript bot check): `2026-11-21_kla_product-page-AP-wafer-inspection-metrology.html`, `2026-11-21_kla_solutions-page-advanced-packaging.html`, `2026-11-21_kla_advance-article-p74080.html`. `Advanced_Packaging_Portfolio_Overview.pdf` returned HTML: NOT RETRIEVED (tried: direct PDF URL).
- The Camtek order release `2026-01-01_camtek_press-release-105M-orders-OSAT-HBM.html` is actually dated 2026-06-02 (wrong date in the file name; the CSV gives the correct date).
- The Onto Q3 2026 release was saved from a finviz copy of Business Wire (`2026-11-05_onto_...`); the release date in the text is 2026-11-09.

## Gaps

- NOT DISCLOSED (read: KLA letters Q4 FY24-Q1 FY27, 10-K FY26): AP revenue by product family; SPTS and PCB/Component AP revenue; CY26 total-systems AP update; CY27 AP figure.
- NOT DISCLOSED (read: Investor Day slide 143): process-control share of AP equipment market as a number.
- NOT RETRIEVED (tried: kla.com product pages via fetch.py → JS challenge): Kronos 1190XR, CIRCL-AP, irArcher, ICOS F26x, Zeta, Micro-SR specification pages.
- NOT RETRIEVED (tried: conferences.computer.org 403): ECTC 2023 ST/KLA irArcher paper.
- NOT RETRIEVED (tried: directindustry.com 403): Kronos 1190XR 150 nm listing.
- NOT RETRIEVED (tried: Crossref only): affiliations and full text of SPIE 10.1117/12.3095356 (Samsung co-authorship, 665 µm Si).
- NOT RETRIEVED (tried: web search; DigiTimes paywalled; no Korean/Taiwan article names KLA): a non-KLA report of a specific KLA AP win or loss.
- NOT DISCLOSED (read: Camtek 20-F FY2025 Item 3/4; Oct 2026 deck; Q3 2026 release): Camtek's named competitors.
- NOT RETRIEVED (tried: none; no attempt in this session): KLA job postings on void or acoustic inspection; SAM vendor sources.
