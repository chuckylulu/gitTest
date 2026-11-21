# KLA Corporation (KLAC) - dossier

KLAC is listed on Nasdaq; the company is based in the USA. Session date: 2026-11-21.

KLA's fiscal year ends **June 30**. In this dossier, Q1 FY27 means Jul-Sep 2026, which is the latest reported quarter: the release came out on 2026-10-28 and the 10-Q on 2026-10-29. A 10-for-1 stock split took effect on 2026-06-11. Per-share figures say whether they are pre-split or post-split.

**Tags.** Every claim carries one tag and an evidence id from `evidence.csv`:
- [F] a fact read in a saved primary document;
- [C] a company claim that cannot be tested independently;
- [S] a secondary source;
- [I] an inference or calculation, whose script is in `calc/`.

The detailed sections after Module B are the module notes, kept as written. Each ends with its own prior-claim check and gap list.

---

## 0. Premise check: corrections to the prompt and to prior/

**Prompt**
1. **Onto–Rigaku direction.** Onto bought 27.0% of Rigaku (announced 2026-04-20, closed 2026-08-10, JPY 113.08B, about $720M, one board seat) [F] Q1-015, Q1-018. Rigaku did not buy a stake in Onto. "Ai Diffract" is Onto software; it is used with Rigaku's CD-SAXS tools [C] Q1-016.
2. **Axion family.** KLA has one X-ray line, Axion (the T2000, launched 2022-12-06). No successor or other X-ray product (XRR/XRF/HRXRD) was found [F] Q1-001, Q1-004. "Axion Series" does appear in the 10-K FY23-FY26 product lists. A note in this session's agent brief said otherwise; it was wrong and is corrected in run_log.md.
3. **AP revenue figures use two definitions.**
   - CY2025 "total systems revenue": about $950M [C] Q2-005.
   - CY2025 "Semiconductor Process Control product portfolio" revenue: about $635M [C] Q2-007.
   - The CY2026 target is "approximately $1.1 billion" of AP *process control systems* revenue [C] Q2-010.

   So the ledger wording "exceeds $1.1B" is stronger than what KLA says.
4. **Export-rule estimates.**
   - The Dec 2024 rules: KLA's estimate is about $500M ± $100M for CY2025, i.e. $400-600M, with about 70% in systems [C] A4-063.
   - The "Affiliates Rule": KLA's ~$300-350M estimate covers Oct 2025-Dec 2026, not FY26. KLA called it "extended export controls" and did not name the rule [C] A4-068.
   - "Oct 17, 2023" is the date BIS announced the rule. It was published in the Federal Register on 2023-10-25 [F] A4-060.
5. **Affiliates Rule suspension.** The suspension did not end in Nov 2026; it was extended to 2027-01-10 [S] A4-073.
6. **Earnings-call Q&A.** KLA does not post call transcripts. Every call quote here comes from a third-party transcript and is tagged [S]. The Q4 FY26 call transcript (2026-07-28) was NOT RETRIEVED (tried: fool.com URL patterns, 404; fortune.com page holds only the header).

**prior/ (the "KLA Corporation Metrology Audit" chat, Step 1)**

Where the file sits: the repo's `prior/` held only `.gitkeep`. The chat was taken from the user's Google Drive and extracted to `prior/text/kla_metrology_audit.md`; see run_log.md.

Status words in the prior-claim checks: MATCHES SOURCE, CORRECTED, PARTLY MATCHES SOURCE, or UNSUPPORTED (no saved source supports the claim; the reason and the documents read are given). Missing data uses only NOT DISCLOSED (read: ...) or NOT RETRIEVED (tried: ...).

| # | Prior claim | Status | Evidence |
|---|---|---|---|
| 7 | 2022 Investor Day CY2026 target "MET" | CORRECTED: tested against FY26 (Jul 2025-Jun 2026) figures; CY2026 is not yet reported. On an implied basis revenue and OM beat the model, while non-GAAP GM (~62.5%) misses its ~63% | [C] A3-037, [I] A3-039 |
| 8 | Backlog rise from $7.86B to $12.57B caused by optical bottlenecks | Figures MATCHES SOURCE; cause CORRECTED. The 10-K attributes the rise to AI-infrastructure demand | [F] A2-001 |
| 9 | "Flat CY26 capacity plan" | No such statement found | — |
| 10 | DRAM cost pressure "into H2 CY2027" | CORRECTED: the 10-K says fiscal 2027, which ends Jun 2027 | [C] Q5-005 |
| 11 | Services ">3-yr fixed subscriptions, <20% T&M" | CORRECTED: >80% of services revenue comes from multi-year subscription contracts, with ~3-year average length and 95% renewal; 95% of revenue is "recurring" including T&M | [C] A1-062, A1-063 |
| 12 | Kronos 1190XR as the hybrid-bonding pre-bond tool | CORRECTED: KLA says Kronos is "not going to be sufficient" for hybrid bonding | [C] Q3-003 |
| 13 | SPIE 10.1117/12.3090197 is an Axion "twisting validation" (Lam, 651 sites, R²>0.84) | CORRECTED: the paper is on hole-to-hole distance variance. The prior's figures are UNSUPPORTED | [S] Q1-014 |
| 14 | TeraBeam 8xx "at TSMC N2 HVM" | Unsupported. KLA says five years of development at TSMC, released 2026 | [C] Q4-005 |
| 15 | IMAPS DOI 10.4071/001c.171430 (2026-08-11) supports irArcher, Kronos and void details | CORRECTED: it is a generic KLA abstract (Crossref date 2026-09-21) and supports none of these details | [F] Q3-019 |
| 16 | FPD manufacturing "ended Dec 31, 2024" | CORRECTED: that was the announced target; no later filing gives the completion date | [F] A5-053 |
| 17 | CY25 mix "94.2% / 5.8%" | CORRECTED: Semi PC systems plus services = 93.2%; PCB and Component = 5.2%; Specialty Semi Process 4.4% was left out | A12 notes |
| 18 | Lasertec "JPY 114.8B FY25 ACTIS sales" | UNSUPPORTED: Lasertec's filings give no product split, and its results presentation was NOT RETRIEVED (tried: lasertec.co.jp IR results page, script widget; publicnow copy, 403) | — |
| 19 | "Actinic 7xx … Early Demo Stage, requires NA change" | MATCHES SOURCE on the slide page image | [F] Q4-001 |
| 20 | Gen4/Gen5 lead times >12 months | MATCHES SOURCE in call transcripts only | [S] Q5-027, Q5-028 |
| 21 | Q1 FY27 revenue $4.14B, non-GAAP OM 46.1%, FCF $1.34B, LTM revenue $14.51B | MATCHES SOURCE | [F] A1-001, A1-018, A1-028; [I] A1-025 |
| 22 | Names | "Teron 6xx" is not a KLA product name; the transcript renders Kronos as "Chronos" and actinic as "Ectinic" | [F] Q4-003 |

---

## 1. Answers to the company-specific questions (summary; details in Parts Q1-Q5 below)

### Q1. X-ray metrology vs Rigaku

**KLA's X-ray products**

| Product | Launch | Applications | Status in KLA's words | Status in customers' words | Throughput | Revenue / units |
|---|---|---|---|---|---|---|
| Axion T2000 (transmission CD-SAXS) | 2022-12-06 [F] Q1-001 | 3D NAND and DRAM; logic not mentioned [F] Q1-001 | Launch: "multiple systems in operation at leading memory manufacturers" [C] Q1-003. Mar 2026: "used in high volume manufacturing today" [C] Q1-005 | No customer statement on production status found. Customer co-authored papers use CD-SAXS as a reference or screening method [S] Q1-011, Q1-012 and note its low depth sensitivity [S] Q1-013 | NOT DISCLOSED (read: launch release 2022-12-06; 10-K FY26 Item 1; Investor Day deck and transcripts) | NOT DISCLOSED (read: 10-K FY26 Items 1 and 7; letters Q4 FY24-Q1 FY27; Investor Day deck). CFO remark: X-ray CD market $75-100M, KLA about 60% [S] Q1-009, which implies about $45-60M a year [I] Q1-010 (Low) |

**KLA statements since April 2026 on the Onto–Rigaku alliance or on hybrid X-ray + optical CD**
- Only one was found, on the Q3 FY26 call of 2026-04-29, nine days after the deal was announced.
  - CEO: "I don't think you're going to see a quick adoption of X-ray anytime soon" [S] Q1-008.
  - CFO: the market figures above [S] Q1-009.
  - KLA named neither Onto nor Rigaku.
- Nothing in the Q3 FY26, Q4 FY26 or Q1 FY27 letters, the 10-K FY26, the Q1 FY27 10-Q, the 2026 press releases, or the Q1 FY27 call transcript [I] Q1-028.
- The Q4 FY26 call transcript is NOT RETRIEVED (tried: fool.com 404; fortune.com header only), so Q1-028 has Medium confidence.

### Q2. Advanced packaging vs Onto and Camtek

| Period | Total AP systems | AP process control (inspection + metrology) | Other AP (process equipment etc.) |
|---|---|---|---|
| CY2025 actual | ~$950M, >70% YoY [C] Q2-005 | ~$635M (66.8%) [C] Q2-007, [I] Q2-I03 | ~$315M, not broken out by KLA. Covers SPTS etch/deposition/dicing (Specialty Semi Process) and ICOS/Zeta/Orbotech substrate lines (PCB and Component Inspection) [I] Q2-I03 (Medium) |
| CY2026 target | Jan 2026: "mid-teens" growth, not updated since [C] Q2-006 | "approximately $1.1 billion", >70% YoY. Set 2026-07-28, reaffirmed 2026-10-28 [C] Q2-009, Q2-010. Like-for-like: +73.2% [I] Q2-I01 | NOT DISCLOSED (read: letters Q2 FY26-Q1 FY27 Outlook sections) |
| CY2027 | NOT DISCLOSED (read: Q4 FY26 and Q1 FY27 letters, Outlook). AP is named only among drivers of 2027 capacity growth [C] Q2-011 | NOT DISCLOSED (read: same) | NOT DISCLOSED (read: same) |

- Product families in the process-control bucket (Semi PC segment): Kronos, CIRCL-AP, Micro-SR, irArcher, PWG5 XT, eDR7xxxAP and others [F] Q2-019.
- ICOS and Zeta are in the PCB and Component Inspection segment [F] Q2-020. SPTS is in Specialty Semiconductor Process [F] Q2-021.
- **Wins and losses reported by non-KLA sources: none name KLA** [I] Q2-I07.
  - An HBM maker chose Onto's Dragonfly G5 + 3Di after onsite evaluations, "displacing the previously established tool of record". The incumbent is not named [C] Q2-029.
  - Camtek reports >$50M of Hawk orders from "a leading HBM player" [F] Q2-035.
  - Onto's 10-K names "KLA and Camtek" as its principal AP-inspection competitors [F] Q2-028.

### Q3. Hybrid-bonding coverage map

| Step | KLA tool | Status | Gap |
|---|---|---|---|
| Incoming wafer shape | PWG5 with XT Option | In the 10-K product list [F] Q3-005; hybrid-bonding shipment status NOT DISCLOSED (read: 10-K FY26 Item 1; Investor Day deck and transcript) | No die-level warpage product named |
| Pre-bond surface defects / particles | Puma, Voyager, broadband plasma (29xx); "whole suite" plus "next four systems" [C] Q3-001, Q3-002. Kronos "not going to be sufficient" [C] Q3-003 | Announced; HVM status NOT DISCLOSED (read: Investor Day transcript p30, p78; letters Q3 FY26-Q1 FY27) | KLA's own target is 0.05-0.5 µm sensitivity [C] Q3-004 |
| Cu recess / dishing | No tool named for hybrid bonding in KLA documents | NOT DISCLOSED (read: 10-K FY26 Item 1; Investor Day slides 66-67 and transcript) | Target 0.001 µm Cu-recess accuracy [C] Q3-004 |
| Bond overlay | irArcher Series | In the 10-K [F] Q3-005; die-to-wafer status NOT DISCLOSED (read: 10-K FY26 Item 1; Investor Day deck) | Precision specs NOT RETRIEVED (tried: kla.com product page, bot check; ECTC 2023 paper, 403) |
| Post-bond buried voids | **None** | No product, partnership, acquisition or stated intent in any saved KLA document [I] Q3-I01 | Onto: EchoScan launched Jan 2025, ≥1 µm voids [C] Q3-012, in validation on Samsung lines [S] Q3-014. Camtek: 2027-28 roadmap item [C] Q3-016 |

### Q4. EUV mask inspection vs Lasertec

- **Actinic.** The Investor Day slide lists "Actinic 7xx … *Requires NA Change … Early Demo Stage" [F] Q4-001. In KLA's words it is a lab prototype with first images and a first inspection [C] Q4-007. KLA calls it "Defense 3", a low-frequency check [C] Q4-009, with "quite bad" cost of ownership for requalification [C] Q4-010.
- **E-beam.** TeraBeam 8xx (multi-column e-beam) released in 2026 [F] Q4-002 after five years of development at TSMC [C] Q4-005. A Samsung + KLA paper reports it in production use at Samsung [S] Q4-014.
- **Optical.** Teron 640e/eS/eS2 (mask shop, 2017) and Teron SL670e/XP/XP2 (fab requalification, 2018) [F] Q4-003, Q4-004.
- **EUV optics supplier.** NOT DISCLOSED (read: 10-K FY26 Item 1 Manufacturing, Item 1A); the 10-K has only general single-source language [F] Q4-020.
- **Lasertec.**
  - ACTIS A150 shipped in 2019 [F] Q4-022, and the A200HiT was released 2025-10-31 at 3x the A150's speed [F] Q4-021.
  - FY2026 (Jul 2025-Jun 2026) orders were JPY 237.5B against 105.2B the year before [F] Q4-024.
  - ACTIS sales: NOT DISCLOSED (read: Lasertec tanshin FY2026 p18, Q1 FY2027 p10).

### Q5. Supply limits

- **Components named.** Optics (glass and "volume optics") are the longest-lead item [S] Q5-024, Q5-029. The Investor Day supply slide lists sole-sourced optics, sensors and lasers, plus mostly sole-sourced stages and motion control [C] Q5-018.
- **Lead times.** Historically about 6 months; 7-9 months in Oct 2025 [S] Q5-022; an order-to-ship time fence of almost 60 weeks in Mar 2026 [C] Q5-019; about 12 months on average in Oct 2026, with Gen4/Gen5 longer [S] Q5-027, Q5-028. The months figures appear in no KLA document.
- **Backlog conversion.** H1 CY26 was capacity-limited and H2 CY26 is about 20-25% above H1 [C] Q5-013, Q5-016. Revenue lost or deferred, and the 12-month share of the $12.57B backlog, are NOT DISCLOSED (read: letters Q2 FY26-Q1 FY27; FY26 10-K Item 1 Backlog and MD&A). Purchase commitments rose to $8.87B [F] A2-029.
- **DRAM chips.** These are a cost problem, not a shipment limit: a 75-100 bps hit to CY26 gross margin [C] Q5-011, continuing through fiscal 2027 [C] Q5-005.

---

## 2. Module A headline (details in Parts A1-A6 below)

| Item | Value | Evidence |
|---|---|---|
| Revenue ($M), Q2 FY26 (Oct-Dec 2025) / Q3 FY26 (Jan-Mar 2026) / Q4 FY26 (Apr-Jun 2026) / Q1 FY27 (Jul-Sep 2026) | 3,297.1 / 3,415.1 / 3,657.6 / 4,136.0; YoY +7.2 / +11.5 / +15.2 / +28.9% | [F] A1-001..004, [I] A1-005 |
| FY26 (Jul 2025-Jun 2026) | $13,579.5M, +11.7%; GM 61.3% GAAP / 62.4% non-GAAP; OM 41.7% / 43.1% | [F] A1-002, [I] A1-023 |
| LTM: Q2 FY26-Q1 FY27 (Oct 2025-Sep 2026) | $14,505.8M (+15.8%); FCF $4,037.6M; SBC/FCF 8.0% | [I] A1-025, A1-036 |
| One-offs management named | Q2 FY26-Q1 FY27 (Oct 2025-Sep 2026): acquisition-related charges only (the non-GAAP exclusion). FY25 (Jul 2024-Jun 2025): $239.1M PCB impairment and $7.1M restructuring | [F] A1-009, A1-015, A1-016 |
| Product groups, Q1 FY27 (Jul-Sep 2026) | Wafer inspection $2,111M; patterning $862M; services $851M (+14%) | [F] A1-043..047 |
| End market, semi PC systems, Q2 FY26 (Oct-Dec 2025) to Q1 FY27 (Jul-Sep 2026) | Foundry/logic ~60 / 62 / 79 / 72%. Memory DRAM:NAND 75:25 / 86:14 / ~83:17 / not disclosed | [F] A1-051..054 |
| Services | FY26 (Jul 2025-Jun 2026) $3,125.9M (+16.5%, 23% of revenue); >80% multi-year subscription contracts; ~3-year average; 95% renewal; target 13-15% CAGR | [I] A1-061; [C] A1-062, A1-063, A1-066 |
| Backlog / RPO | Quarterly RPO (end of Q1 FY24, Sep 2023, to Q4 FY25, Jun 2025): $10.85B → $9.83B → $7.86B. KLA's own 12-month share rose from 50-60% to 71-76% [F] A2-035..050; [C] 12-month shares. KLA stopped the quarterly RPO note after Jun 2025: NOT DISCLOSED (read: 10-Q Notes Q1 FY26 to Q1 FY27). Annual backlog at the end of FY26 (Jun 30, 2026): $12.57B, 12-month share NOT DISCLOSED (read: FY26 10-K Item 1 Backlog and Notes) | [F] A2-001; [I] A2-051 |
| Orders / book-to-bill | NOT DISCLOSED (read: letters, slides, releases and 10-Qs Q2 FY26-Q1 FY27); FY26 (Jul 2025-Jun 2026) implied ~1.35 | [I] A2-006 (Low) |
| Purchase commitments | $2.75B (Dec 31, 2025, end of Q2 FY26) → $8.87B (Sep 30, 2026, end of Q1 FY27) | [F] A2-029..032 |
| Inventory, end of Q4 FY25 (Jun 2025) → end of Q1 FY27 (Sep 2026) | +27%; raw materials +43%, WIP +29%, finished goods −13% | [I] A2-011 |
| Guidance record, Q2 FY25 (Oct-Dec 2024) to Q1 FY27 (Jul-Sep 2026) | Revenue 0 beat / 8 in-line / 0 miss (above the midpoint every quarter). Non-GAAP EPS 1 / 7 / 0. GAAP EPS 0 / 7 / 1, the miss due to an impairment | [I] A3-025 |
| China share | Q1 FY24 (Jul-Sep 2023) 42.8% → peak 44.6% in Q4 FY24 (Apr-Jun 2024) → low 24.3% in Q3 FY26 (Jan-Mar 2026) → 34.5% in Q1 FY27 (Jul-Sep 2026). FY24 42.8%, FY25 33.3%, FY26 29.8% | [F] A4-010..013, [I] A4-016..028 |
| Export-rule estimates (KLA's own) | Oct 2022: $500-900M gross CY23. Oct 2023: none. Dec 2024: ~$500M ± $100M CY25. Affiliates Rule: ~$300-350M for Oct 2025-Dec 2026 | [C] A4-057, A4-063, A4-068; [F] A4-061 (no estimate given) |
| Customers >10% | TSMC ~19% of FY26 (Jul 2025-Jun 2026) revenue; two unnamed customers at 21% and 13% in Q1 FY27 (Jul-Sep 2026) | [F] A4-046, A4-051 |
| Debt, end of Q1 FY27 (Sep 30, 2026) | Notes $5.95B (8 fixed-rate tranches, 2029-2062); cash and securities $4.74B; net debt $1.21B; next maturity $800M 4.10% due 2029-03-15; $1.5B revolver undrawn; no convertibles | [F] A5-006..014, [I] A5-028 |
| Buyback | Remaining authorisation $8.81B (Sep 30, 2026); repurchases in Q2 FY26-Q1 FY27 (Oct 2025-Sep 2026) $2.68B | [F] A5-038, [I] A5-037 |
| Last downturns | CY2022-23: revenue −21.1%; GAAP OM −10.7 pts, or −6.0 pts ex impairments; non-GAAP −5.7 pts. CY2012-15: revenue −28.0%; GAAP OM −18.7 pts, no one-off named at the low in Q1 FY15 (Jul-Sep 2014) [I] A6-027 | [I] A6-010..012, A6-023, A6-024 |

---

## 3. Module B

### B1. Disputed-claims ledger

| Claim | Who said it, when | Evidence for | Evidence against | Strongest tag on each side |
|---|---|---|---|---|
| Process-control intensity rises with advanced packaging and HBM | KLA, Investor Day 2026-03-12 and letters; the user's claim | KLA "packaging intensity" 0.4% (2018) → 5.6% (2025) [C] Q2-016. HBM gave a $450M incremental intensity gain in CY25 [C] Q2-018. Hybrid-bonding specs are ~10x tighter [C] Q3-004. KLA's CY26 AP process-control growth is ~2x the AP market [C] Q2-009 | KLA's intensity metric is its own revenue divided by the AP market, so it mixes share gain (>50% share, +14 pts [C] Q2-014, Q2-015) with true intensity. No third-party quantified intensity was found. Onto says AP demand is "driven by assembly volumes" [F] Q2-039 | For [C] / Against [F] |
| AP revenue exceeds $1.1B in CY2026 | User's claim; KLA guide of 2026-07-28, reaffirmed 2026-10-28 | "approximately $1.1 billion" of AP process-control systems revenue, >70% YoY, reaffirmed [C] Q2-010. Like-for-like growth +73.2% [I] Q2-I01 | KLA says "approximately", not "exceeds". The figure covers process control only. On the total-systems basis the last guide was mid-teens growth on ~$950M, about $1.07-1.11B [C] Q2-006. CY26 actual is due in late Jan 2027 [I] B-002 | For [C] / Against [C] |
| Actinic patterned-mask inspection is close to production | Question raised at Investor Day 2026-03-12; the user's claim | KLA has a lab prototype with first images and a first inspection, and says results "look quite impressive" [C] Q4-007. "We are developing an actinic inspection system" [C] Q4-011 | Slide release column reads "Early Demo Stage" with no date [F] Q4-001. KLA positions actinic as low-frequency "Defense 3" with poor cost of ownership [C] Q4-009, Q4-010. Nothing in the letters or 2026 press releases [F] Q1-027. KLA's 2026 mask launch was e-beam (TeraBeam) [F] Q4-002. Lasertec has shipped ACTIS since 2019 and launched the A200HiT in Oct 2025 [F] Q4-021, Q4-022. [I] Q4-033: KLA's own disclosures refute "close to production" (Medium) | For [C] / Against [F] |
| Post-bond buried-void inspection stays outside KLA's portfolio | User's claim; prior chat (Nov 2026) | No void product, partnership, acquisition or stated intent in the 10-K FY26, Q1 FY27 10-Q, Annual Report 2026, Investor Day deck and transcript, or letters [I] Q3-I01. Onto has a launched tool and a Samsung development deal [C] Q3-012, [S] Q3-014 | KLA claims a "whole suite" of hybrid-bonding systems and four more developed, unnamed [C] Q3-001, Q3-002. kla.com product pages could not be retrieved, so an unlisted product cannot be ruled out. "Stays outside" is a forecast that no document can settle | For [I] / Against [C] |
| China revenue has normalised | KLA letter 2026-10-28 ("high-20s" CY26); CFO Oct 2026 ("low-20s" in 2027) | Jan-Sep 2026 China share 28.7% [I] A4-031, inside KLA's high-20s guide [C] A4-041 and the FY21-FY23 range of 26.5-28.9% [I] A4-034. China grew 6.4% in that period vs 18.6% total [I] A4-033 | Q1 FY27 China +49% QoQ to 34.5% [F] A4-010, A4-015. China dollars are flat (FY24 $4.20B, FY25 $4.04B, FY26 $4.05B) [F] A4-011..013. KLA itself expects a further fall to the low-20s in 2027 [S] A4-078. The Affiliates Rule suspension ends 2027-01-10 unless extended [S] A4-073, against KLA's own $300-350M estimate [C] A4-068 | For [C] / Against [F] |
| X-ray CD metrology will not see quick production adoption (found claim) | KLA CEO, Q3 FY26 call, 2026-04-29 | Axion took years to reach adoption [S] Q1-007. The X-ray CD market is only $75-100M [S] Q1-009. A Lam paper notes CD-SAXS's low depth sensitivity [S] Q1-013 | KLA said at Investor Day that Axion is "used in high volume manufacturing today" [C] Q1-005. Onto paid ~$720M for 27% of Rigaku [F] Q1-018. Onto says Ai Diffract + Rigaku CD-SAXS has been "selected by two key customers" [C] Q1-016. Rigaku targets ≥$300M incremental opportunity by 2030 [C] Q1-021 | For [S] / Against [F] |

### B2. Facts that weaken each reading ([F], [C] or [S] only)

**Weaken the optimistic reading**
1. Purchase commitments rose from about $2.75B at the end of Q2 FY26 (Dec 31, 2025) to $8.87B at the end of Q1 FY27 (Sep 30, 2026) [F] A2-032, A2-029.
2. China was $1,425.7M, 34.5% of Q1 FY27 (Jul-Sep 2026) revenue, up 49% from the prior quarter [F] A4-010.
3. KLA's Investor Day slide of 2026-03-12 (Q3 FY26) lists its actinic EUV mask inspector as "Early Demo Stage" [F] Q4-001.

**Weaken the pessimistic reading**
1. Q1 FY27 (Jul-Sep 2026) revenue was $4,136.0M [F] A3-023, against the $4.0B ± $0.2B guidance KLA gave the quarter before [F] A3-022.
2. Backlog was $12.57B at the end of FY26 (Jun 30, 2026), up from $7.86B a year earlier [F] A2-001.
3. Over 80% of services revenue ($3.13B in FY26, Jul 2025-Jun 2026) comes from multi-year subscription contracts, according to KLA [C] A1-062.

### B3. Dated catalysts, next 12 months (2026-11-21 to 2027-11-20)

| Date | Event | Evidence |
|---|---|---|
| 2026-12-01 | Dividend of $0.23/share (post-split) payable; record date 2026-11-16 | [F] B-001 |
| 2027-01-10 | Suspension of the BIS Affiliates Rule ends unless extended. KLA's own exposure estimate was $300-350M | [S] A4-073; [C] A4-068 |
| Late Jan 2027 (date not yet announced) | Q2 FY27 (Oct-Dec 2026) results. They test the $4.7B ± $0.2B guide [C] A3-026; complete CY2026 against KLA's "~$1.1B" AP process-control target [C] Q2-010, the high-20s China share [C] A4-041, and the 2022 Investor Day CY2026 model [C] A3-037 | [I] B-002 |
| Late Apr 2027 (expected) | Q3 FY27 (Jan-Mar 2027) results | [I] B-002 (same pattern) |
| Through Jun 2027 | KLA expects DRAM chip costs to weigh on gross margin "in fiscal 2027" | [C] Q5-005 |
| Late Jul 2027 / early Aug 2027 (expected) | Q4 FY27 and FY27 results, then the FY27 10-K with the annual backlog figure (and possibly the 12-month conversion share) | [I] B-002; [F] A2-001 |
| Late Oct 2027 (expected) | Q1 FY28 (Jul-Sep 2027) results | [I] B-002 |
| None in the window | No debt maturity before 2029-03-15 ($800M 4.10% notes). The revolver runs to 2030-07-03. No lock-ups apply | [F] A5-006, A5-017 |
| Not dated | Onto–Rigaku hybrid X-ray/optical product: "selected by two key customers", no production date given. KLA Actinic 7xx: no release date. KLA "next four" hybrid-bonding systems: no dates | [C] Q1-016; [F] Q4-001; [C] Q3-002 |

### B4. Gap log
See `gaps.md`: every NOT DISCLOSED and NOT RETRIEVED item, one line each.

### B5. Handoff row
See `handoff.md`. It also holds the extra cell: products where KLA competes directly with Rigaku, Onto, Camtek, Nova and Lasertec.

---

# Detailed sections (module notes)
