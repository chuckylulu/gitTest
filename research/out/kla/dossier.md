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
   - CY2025 "total systems revenue": about $950M [F] Q2-005.
   - CY2025 "Semiconductor Process Control product portfolio" revenue: about $635M [F] Q2-007.
   - The CY2026 target is "approximately $1.1 billion" of AP *process control systems* revenue [C] Q2-010.

   So the ledger wording "exceeds $1.1B" is stronger than what KLA says.
4. **Export-rule estimates.**
   - The Dec 2024 rules: KLA's estimate is about $500M ± $100M for CY2025, i.e. $400-600M, with about 70% in systems [F] A4-063.
   - The "Affiliates Rule": KLA's ~$300-350M estimate covers Oct 2025-Dec 2026, not FY26. KLA called it "extended export controls" and did not name the rule [F] A4-068.
   - "Oct 17, 2023" is the date BIS announced the rule. It was published in the Federal Register on 2023-10-25 [F] A4-060.
5. **Affiliates Rule suspension.** The suspension did not end in Nov 2026; it was extended to 2027-01-10 [S] A4-073.
6. **Earnings-call Q&A.** KLA does not post call transcripts. Every call quote here comes from a third-party transcript and is tagged [S]. The Q4 FY26 call transcript (2026-07-28) was NOT RETRIEVED.

**prior/ (the "KLA Corporation Metrology Audit" chat, Step 1)**

Where the file sits: the repo's `prior/` held only `.gitkeep`. The chat was taken from the user's Google Drive and extracted to `prior/text/kla_metrology_audit.md`; see run_log.md.

| # | Prior claim | Status | Evidence |
|---|---|---|---|
| 7 | 2022 Investor Day CY2026 target "MET" | CORRECTED: tested against FY26 (Jul 2025-Jun 2026) figures; CY2026 is not yet reported. On an implied basis revenue and OM beat the model, while non-GAAP GM (~62.5%) misses its ~63% | [F] A3-037, [I] A3-039 |
| 8 | Backlog rise from $7.86B to $12.57B caused by optical bottlenecks | Figures CONFIRMED; cause CORRECTED. The 10-K attributes the rise to AI-infrastructure demand | [F] A2-001 |
| 9 | "Flat CY26 capacity plan" | No such statement found | — |
| 10 | DRAM cost pressure "into H2 CY2027" | CORRECTED: the 10-K says fiscal 2027, which ends Jun 2027 | [F] Q5-005 |
| 11 | Services ">3-yr fixed subscriptions, <20% T&M" | CORRECTED: >80% of services revenue comes from multi-year subscription contracts, with ~3-year average length and 95% renewal; 95% of revenue is "recurring" including T&M | [C] A1-062, A1-063 |
| 12 | Kronos 1190XR as the hybrid-bonding pre-bond tool | CORRECTED: KLA says Kronos is "not going to be sufficient" for hybrid bonding | [C] Q3-003 |
| 13 | SPIE 10.1117/12.3090197 is an Axion "twisting validation" (Lam, 651 sites, R²>0.84) | CORRECTED: the paper is on hole-to-hole distance variance. The prior's figures are NOT VERIFIABLE | [S] Q1-014 |
| 14 | TeraBeam 8xx "at TSMC N2 HVM" | Unsupported. KLA says five years of development at TSMC, released 2026 | [C] Q4-005 |
| 15 | IMAPS DOI 10.4071/001c.171430 (2026-08-11) supports irArcher, Kronos and void details | CORRECTED: it is a generic KLA abstract (Crossref date 2026-09-21) and supports none of these details | [F] Q3-019 |
| 16 | FPD manufacturing "ended Dec 31, 2024" | CORRECTED: that was the announced target; no later filing confirms the date | [F] A5-053 |
| 17 | CY25 mix "94.2% / 5.8%" | CORRECTED: Semi PC systems plus services = 93.2%; PCB and Component = 5.2%; Specialty Semi Process 4.4% was left out | A12 notes |
| 18 | Lasertec "JPY 114.8B FY25 ACTIS sales" | NOT VERIFIABLE: Lasertec's filings give no product split, and its results presentation was NOT RETRIEVED | — |
| 19 | "Actinic 7xx … Early Demo Stage, requires NA change" | CONFIRMED on the slide page image | [F] Q4-001 |
| 20 | Gen4/Gen5 lead times >12 months | CONFIRMED in call transcripts only | [S] Q5-027, Q5-028 |
| 21 | Q1 FY27 revenue $4.14B, non-GAAP OM 46.1%, FCF $1.34B, LTM revenue $14.51B | CONFIRMED | [F] A1-001, A1-018, A1-028; [I] A1-025 |
| 22 | Names | "Teron 6xx" is not a KLA product name; the transcript renders Kronos as "Chronos" and actinic as "Ectinic" | [F] Q4-003 |

---

## 1. Answers to the company-specific questions (summary; details in Parts Q1-Q5 below)

### Q1. X-ray metrology vs Rigaku

**KLA's X-ray products**

| Product | Launch | Applications | Status in KLA's words | Status in customers' words | Throughput | Revenue / units |
|---|---|---|---|---|---|---|
| Axion T2000 (transmission CD-SAXS) | 2022-12-06 [F] Q1-001 | 3D NAND and DRAM; logic not mentioned [F] Q1-001 | Launch: "multiple systems in operation at leading memory manufacturers" [C] Q1-003. Mar 2026: "used in high volume manufacturing today" [C] Q1-005 | No customer statement on production status found. Customer co-authored papers use CD-SAXS as a reference or screening method [S] Q1-011, Q1-012 and note its low depth sensitivity [S] Q1-013 | NOT DISCLOSED | NOT DISCLOSED. CFO remark: X-ray CD market $75-100M, KLA about 60% [S] Q1-009, which implies about $45-60M a year [I] Q1-010 (Low) |

**KLA statements since April 2026 on the Onto–Rigaku alliance or on hybrid X-ray + optical CD**
- Only one was found, on the Q3 FY26 call of 2026-04-29, nine days after the deal was announced.
  - CEO: "I don't think you're going to see a quick adoption of X-ray anytime soon" [S] Q1-008.
  - CFO: the market figures above [S] Q1-009.
  - KLA named neither Onto nor Rigaku.
- Nothing in the Q3 FY26, Q4 FY26 or Q1 FY27 letters, the 10-K FY26, the Q1 FY27 10-Q, the 2026 press releases, or the Q1 FY27 call transcript [I] Q1-028.
- The Q4 FY26 call transcript is NOT RETRIEVED, so Q1-028 has Medium confidence.

### Q2. Advanced packaging vs Onto and Camtek

| Period | Total AP systems | AP process control (inspection + metrology) | Other AP (process equipment etc.) |
|---|---|---|---|
| CY2025 actual | ~$950M, >70% YoY [F] Q2-005 | ~$635M (66.8%) [F] Q2-007, [I] Q2-I03 | ~$315M, not broken out by KLA. Covers SPTS etch/deposition/dicing (Specialty Semi Process) and ICOS/Zeta/Orbotech substrate lines (PCB and Component Inspection) [I] Q2-I03 (Medium) |
| CY2026 target | Jan 2026: "mid-teens" growth, not updated since [C] Q2-006 | "approximately $1.1 billion", >70% YoY. Set 2026-07-28, reaffirmed 2026-10-28 [C] Q2-009, Q2-010. Like-for-like: +73.2% [I] Q2-I01 | NOT DISCLOSED |
| CY2027 | NOT DISCLOSED; AP is named only among drivers of 2027 capacity growth [C] Q2-011 | NOT DISCLOSED | NOT DISCLOSED |

- Product families in the process-control bucket (Semi PC segment): Kronos, CIRCL-AP, Micro-SR, irArcher, PWG5 XT, eDR7xxxAP and others [F] Q2-019.
- ICOS and Zeta are in the PCB and Component Inspection segment [F] Q2-020. SPTS is in Specialty Semiconductor Process [F] Q2-021.
- **Wins and losses reported by non-KLA sources: none name KLA** [I] Q2-I07.
  - An HBM maker chose Onto's Dragonfly G5 + 3Di after onsite evaluations, "displacing the previously established tool of record". The incumbent is not named [C] Q2-029.
  - Camtek reports >$50M of Hawk orders from "a leading HBM player" [F] Q2-035.
  - Onto's 10-K names "KLA and Camtek" as its principal AP-inspection competitors [F] Q2-028.

### Q3. Hybrid-bonding coverage map

| Step | KLA tool | Status | Gap |
|---|---|---|---|
| Incoming wafer shape | PWG5 with XT Option | In the 10-K product list [F] Q3-005; hybrid-bonding shipment status NOT DISCLOSED | No die-level warpage product named |
| Pre-bond surface defects / particles | Puma, Voyager, broadband plasma (29xx); "whole suite" plus "next four systems" [C] Q3-001, Q3-002. Kronos "not going to be sufficient" [C] Q3-003 | Announced; HVM status NOT DISCLOSED | KLA's own target is 0.05-0.5 µm sensitivity [C] Q3-004 |
| Cu recess / dishing | No tool named for hybrid bonding in KLA documents | NOT DISCLOSED | Target 0.001 µm Cu-recess accuracy [C] Q3-004 |
| Bond overlay | irArcher Series | In the 10-K [F] Q3-005; die-to-wafer status NOT DISCLOSED | Precision specs NOT RETRIEVED |
| Post-bond buried voids | **None** | No product, partnership, acquisition or stated intent in any saved KLA document [I] Q3-I01 | Onto: EchoScan launched Jan 2025, ≥1 µm voids [C] Q3-012, validating at Samsung [S] Q3-014. Camtek: 2027-28 roadmap item [C] Q3-016 |

### Q4. EUV mask inspection vs Lasertec

- **Actinic.** The Investor Day slide lists "Actinic 7xx … *Requires NA Change … Early Demo Stage" [F] Q4-001. In KLA's words it is a lab prototype with first images and a first inspection [C] Q4-007. KLA calls it "Defense 3", a low-frequency check [C] Q4-009, with "quite bad" cost of ownership for requalification [C] Q4-010.
- **E-beam.** TeraBeam 8xx (multi-column e-beam) released in 2026 [F] Q4-002 after five years of development at TSMC [C] Q4-005. A Samsung + KLA paper reports it in production use at Samsung [S] Q4-014.
- **Optical.** Teron 640e/eS/eS2 (mask shop, 2017) and Teron SL670e/XP/XP2 (fab requalification, 2018) [F] Q4-003, Q4-004.
- **EUV optics supplier.** NOT DISCLOSED; the 10-K has only general single-source language [F] Q4-020.
- **Lasertec.**
  - ACTIS A150 shipped in 2019 [F] Q4-022, and the A200HiT was released 2025-10-31 at 3x the A150's speed [F] Q4-021.
  - FY2026 (Jul 2025-Jun 2026) orders were JPY 237.5B against 105.2B the year before [F] Q4-024.
  - ACTIS sales are NOT DISCLOSED in Lasertec's filings.

### Q5. Supply limits

- **Components named.** Optics (glass and "volume optics") are the longest-lead item [S] Q5-024, Q5-029. The Investor Day supply slide lists sole-sourced optics, sensors and lasers, plus mostly sole-sourced stages and motion control [C] Q5-018.
- **Lead times.** Historically about 6 months; 7-9 months in Oct 2025 [S] Q5-022; an order-to-ship time fence of almost 60 weeks in Mar 2026 [C] Q5-019; about 12 months on average in Oct 2026, with Gen4/Gen5 longer [S] Q5-027, Q5-028. The months figures appear in no KLA document.
- **Backlog conversion.** H1 CY26 was capacity-limited and H2 CY26 is about 20-25% above H1 [C] Q5-013, Q5-016. Revenue lost or deferred, and the 12-month share of the $12.57B backlog, are NOT DISCLOSED. Purchase commitments rose to $8.87B [F] A2-029.
- **DRAM chips.** These are a cost problem, not a shipment limit: a 75-100 bps hit to CY26 gross margin [F] Q5-011, continuing through fiscal 2027 [F] Q5-005.

---

## 2. Module A headline (details in Parts A1-A6 below)

| Item | Value | Evidence |
|---|---|---|
| Revenue Q2 FY26 to Q1 FY27 ($M) | 3,297.1 / 3,415.1 / 3,657.6 / 4,136.0; YoY +7.2 / +11.5 / +15.2 / +28.9% | [F] A1-001..004, [I] A1-005 |
| FY26 (Jul 2025-Jun 2026) | $13,579.5M, +11.7%; GM 61.3% GAAP / 62.4% non-GAAP; OM 41.7% / 43.1% | [F] A1-002, [I] A1-023 |
| LTM to Sep 2026 | $14,505.8M (+15.8%); FCF $4,037.6M; SBC/FCF 8.0% | [I] A1-025, A1-036 |
| One-offs management named | Last 4 quarters: acquisition-related charges only (the non-GAAP exclusion). FY25: $239.1M PCB impairment and $7.1M restructuring | [F] A1-009, A1-015, A1-016 |
| Product groups, Q1 FY27 | Wafer inspection $2,111M; patterning $862M; services $851M (+14%) | [F] A1-043..047 |
| End market, semi PC systems, Q2 FY26 to Q1 FY27 | Foundry/logic ~60 / 62 / 79 / 72%. Memory DRAM:NAND 75:25 / 86:14 / ~83:17 / not disclosed | [F] A1-051..054 |
| Services | FY26 $3,125.9M (+16.5%, 23% of revenue); >80% multi-year subscription contracts; ~3-year average; 95% renewal; target 13-15% CAGR | [I] A1-061; [C] A1-062, A1-063, A1-066 |
| Backlog | $9.83B (Jun 2024), $7.86B (Jun 2025), $12.57B (Jun 2026). Annual only. 12-month share NOT DISCLOSED for FY26; 71-76% for FY25 | [F] A2-001, A2-003 |
| Orders / book-to-bill | NOT DISCLOSED; FY26 implied ~1.35 | [I] A2-006 (Low) |
| Purchase commitments | $2.75B (Dec 2025) → $8.87B (Sep 2026) | [F] A2-029..032 |
| Inventory, Jun 2025 → Sep 2026 | +27%; raw materials +43%, WIP +29%, finished goods −13% | [I] A2-011 |
| Guidance record, last 8 quarters | Revenue 0 beat / 8 in-line / 0 miss (above the midpoint every quarter). Non-GAAP EPS 1 / 7 / 0. GAAP EPS 0 / 7 / 1, the miss due to an impairment | [I] A3-025 |
| China share | Q1 FY24 to Q1 FY27: 42.8 → 44.6 peak (Q4 FY24) → 24.3 (Q3 FY26) → 34.5% (Q1 FY27). FY24 42.8%, FY25 33.3%, FY26 29.8% | [F] A4-010..013, [I] A4-016..028 |
| Export-rule estimates (KLA's own) | Oct 2022: $500-900M gross CY23. Oct 2023: none. Dec 2024: ~$500M ± $100M CY25. Affiliates Rule: ~$300-350M for Oct 2025-Dec 2026 | [F] A4-058, A4-061, A4-063, A4-068 |
| Customers >10% | TSMC ~19% of FY26 revenue; two unnamed customers at 21% and 13% in Q1 FY27 | [F] A4-046, A4-051 |
| Debt | Notes $5.95B (8 fixed-rate tranches, 2029-2062); cash and securities $4.74B; net debt $1.21B; next maturity $800M 4.10% due 2029-03-15; $1.5B revolver undrawn; no convertibles | [F] A5-006..014, [I] A5-028 |
| Buyback | Remaining authorisation $8.81B (Sep 30, 2026); last-4-quarter repurchases $2.68B | [F] A5-038, [I] A5-037 |
| Last downturns | CY2022-23: revenue −21.1%; GAAP OM −10.7 pts, or −6.0 pts ex impairments; non-GAAP −5.7 pts. CY2012-15: revenue −28.0%; GAAP OM −18.7 pts | [I] A6-010..012, A6-023, A6-024 |

---

## 3. Module B

### B1. Disputed-claims ledger

| Claim | Who said it, when | Evidence for | Evidence against | Strongest tag on each side |
|---|---|---|---|---|
| Process-control intensity rises with advanced packaging and HBM | KLA, Investor Day 2026-03-12 and letters; the user's claim | KLA "packaging intensity" 0.4% (2018) → 5.6% (2025) [C] Q2-016. HBM gave a $450M incremental intensity gain in CY25 [C] Q2-018. Hybrid-bonding specs are ~10x tighter [C] Q3-004. KLA's CY26 AP process-control growth is ~2x the AP market [C] Q2-009 | KLA's intensity metric is its own revenue divided by the AP market, so it mixes share gain (>50% share, +14 pts [C] Q2-014, Q2-015) with true intensity. No third-party quantified intensity was found. Onto says AP demand is "driven by assembly volumes" [F] Q2-039 | For [C] / Against [F] |
| AP revenue exceeds $1.1B in CY2026 | User's claim; KLA guide of 2026-07-28, reaffirmed 2026-10-28 | "approximately $1.1 billion" of AP process-control systems revenue, >70% YoY, reaffirmed [C] Q2-010. Like-for-like growth +73.2% [I] Q2-I01 | KLA says "approximately", not "exceeds". The figure covers process control only. On the total-systems basis the last guide was mid-teens growth on ~$950M, about $1.07-1.11B [C] Q2-006. CY26 actual is due in late Jan 2027 [I] B-002 | For [C] / Against [C] |
| Actinic patterned-mask inspection is close to production | Question raised at Investor Day 2026-03-12; the user's claim | KLA has a lab prototype with first images and a first inspection, and says results "look quite impressive" [C] Q4-007. "We are developing an actinic inspection system" [C] Q4-011 | Slide release column reads "Early Demo Stage" with no date [F] Q4-001. KLA positions actinic as low-frequency "Defense 3" with poor cost of ownership [C] Q4-009, Q4-010. Nothing in the letters or 2026 press releases [F] Q1-027. KLA's 2026 mask launch was e-beam (TeraBeam) [F] Q4-002. Lasertec has shipped ACTIS since 2019 and launched the A200HiT in Oct 2025 [F] Q4-021, Q4-022. [I] Q4-033: KLA's own disclosures refute "close to production" (Medium) | For [C] / Against [F] |
| Post-bond buried-void inspection stays outside KLA's portfolio | User's claim; prior chat (Nov 2026) | No void product, partnership, acquisition or stated intent in the 10-K FY26, Q1 FY27 10-Q, Annual Report 2026, Investor Day deck and transcript, or letters [I] Q3-I01. Onto has a launched tool and a Samsung development deal [C] Q3-012, [S] Q3-014 | KLA claims a "whole suite" of hybrid-bonding systems and four more developed, unnamed [C] Q3-001, Q3-002. kla.com product pages could not be retrieved, so an unlisted product cannot be ruled out. "Stays outside" is a forecast that no document can settle | For [I] / Against [C] |
| China revenue has normalised | KLA letter 2026-10-28 ("high-20s" CY26); CFO Oct 2026 ("low-20s" in 2027) | Jan-Sep 2026 China share 28.7% [I] A4-031, inside KLA's high-20s guide [F] A4-041 and the FY21-FY23 range of 26.5-28.9% [I] A4-034. China grew 6.4% in that period vs 18.6% total [I] A4-033 | Q1 FY27 China +49% QoQ to 34.5% [F] A4-010, A4-015. China dollars are flat (FY24 $4.20B, FY25 $4.04B, FY26 $4.05B) [F] A4-011..013. KLA itself expects a further fall to the low-20s in 2027 [S] A4-078. The Affiliates Rule suspension ends 2027-01-10 unless extended [S] A4-073, against KLA's own $300-350M estimate [F] A4-068 | For [F] / Against [F] |
| X-ray CD metrology will not see quick production adoption (found claim) | KLA CEO, Q3 FY26 call, 2026-04-29 | Axion took years to reach adoption [S] Q1-007. The X-ray CD market is only $75-100M [S] Q1-009. A Lam paper notes CD-SAXS's low depth sensitivity [S] Q1-013 | KLA said at Investor Day that Axion is "used in high volume manufacturing today" [C] Q1-005. Onto paid ~$720M for 27% of Rigaku [F] Q1-018. Onto says Ai Diffract + Rigaku CD-SAXS has been "selected by two key customers" [C] Q1-016. Rigaku targets ≥$300M incremental opportunity by 2030 [C] Q1-021 | For [S] / Against [F] |

### B2. Facts that weaken each reading ([F], [C] or [S] only)

**Weaken the optimistic reading**
1. Purchase commitments rose from about $2.75B (Dec 31, 2025) to $8.87B (Sep 30, 2026) [F] A2-032, A2-029. A long-term receivables line ($266.8M at Sep 30, 2026) appeared in Jun 2026 [F] A2-023. The FY26 10-K does not say how much of the $12.57B backlog ships within 12 months [F] A2-001.
2. China was 34.5% of Q1 FY27 revenue [F] A4-010. The suspension of the Affiliates Rule runs to 2027-01-10 [S] A4-073, and KLA's own estimate for "extended export controls" was ~$300-350M [F] A4-068.
3. KLA's actinic EUV mask inspector is at "Early Demo Stage" [F] Q4-001, while Lasertec released a 3x-faster ACTIS A200HiT on 2025-10-31 [F] Q4-021. Separately, an HBM maker replaced its "tool of record" with Onto's Dragonfly G5 + 3Di [C] Q2-029.

**Weaken the pessimistic reading**
1. Revenue landed inside the guided range, and above its midpoint, in each of the last 8 quarters (Q2 FY25 to Q1 FY27) [F] A3-001..A3-023 (rows by quarter). The current Q2 FY27 guide is $4.7B ± $0.2B [F] A3-026.
2. Backlog was $12.57B at Jun 30, 2026, up from $7.86B a year earlier [F] A2-001, against FY26 revenue of $13.58B [F] A1-002.
3. Services revenue was $3.13B in FY26, +16.5% [F] A1-046. Over 80% of it comes from multi-year subscription contracts, with a 95% renewal rate [C] A1-062, A1-063.

### B3. Dated catalysts, next 12 months (2026-11-21 to 2027-11-20)

| Date | Event | Evidence |
|---|---|---|
| 2026-12-01 | Dividend of $0.23/share (post-split) payable; record date 2026-11-16 | [F] B-001 |
| 2027-01-10 | Suspension of the BIS Affiliates Rule ends unless extended. KLA's own exposure estimate was $300-350M | [S] A4-073; [F] A4-068 |
| Late Jan 2027 (date not yet announced) | Q2 FY27 (Oct-Dec 2026) results. They test the $4.7B ± $0.2B guide [F] A3-026; complete CY2026 against KLA's "~$1.1B" AP process-control target [C] Q2-010, the high-20s China share [F] A4-041, and the 2022 Investor Day CY2026 model [F] A3-037 | [I] B-002 |
| Late Apr 2027 (expected) | Q3 FY27 (Jan-Mar 2027) results | [I] B-002 (same pattern) |
| Through Jun 2027 | KLA expects DRAM chip costs to weigh on gross margin "in fiscal 2027" | [F] Q5-005 |
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

## Part Q1, Q4, Nova: X-ray vs Rigaku, EUV mask vs Lasertec, Nova overlap

KLA fiscal year ends June 30. Lasertec fiscal year ends June 30 (Lasertec "FY2026" = Jul 2025-Jun 2026). Nova and Onto use calendar years. Rigaku: calendar year (not used for figures here).
Evidence rows: `parts/Q1.csv` (28), `parts/Q4.csv` (33), `parts/NV.csv` (6). Arithmetic: `calc/q14_calcs.py`. Text rebuild of OpenAlex abstract records: `calc/q14_openalex_to_text.py` (rebuilds `_text/*.txt` from saved JSON; quotes in rows were checked against that text).
Tag note: SPIE papers could not be opened on spiedigitallibrary.org (Incapsula bot block). Abstracts were saved from the OpenAlex index (copies of the publisher abstract). They are tagged [S], not [F].

### Premise issues
- "Axion does not appear in KLA's 10-K/10-Q text": wrong for the 10-K. "Axion® Series" is in the Item 1 metrology product list of the 10-K FY23 through FY26 [F] Q1-004. It does not appear in the 10-Qs or in any shareholder letter.
- KLA has one X-ray product line, Axion (T2000, launched 2022-12-06) [F] Q1-001. No Axion successor, and no KLA XRR, XRF or HRXRD product, appears in the 10-K FY26 product list, the Investor Day deck, or the KLA IR press releases for Jan-Nov 2026 [F] Q1-004, Q1-027.
- Onto–Rigaku: the "~April 2026" date is right (announced 2026-04-20). "Rigaku 27%" is right, but Onto bought the 27% stake in Rigaku, not the other way round. "Ai Diffract" is an Onto software product, not a joint product name [F] Q1-015, Q1-018.
- The SPIE paper doi 10.1117/12.3090197 has the title "Monitoring of hole-to-hole distance variance in 3D NAND using Axion x-ray critical dimension metrology". It is not a "twisting validation" paper. The prior chat's details (Lam co-authors, 2 wafers, 651 sites, R²>0.84) cannot be checked [S] Q1-014.
- "Teron 6xx" is not a KLA slide name. The names on Investor Day slide p91 are: Teron 610/630/640, Teron 640e/eS/eS2, Teron SL650/655/670, Teron SL670e/XP/XP2, Gen5 Agera Wafer Print Check, TeraBeam® 8xx and Actinic 7xx [F] Q4-001..004.
- In the Investor Day transcript, "extra metrology" (p42) stands for "X-ray metrology", and "Ectinic" (p40-41) stands for "actinic". These are transcription errors in KLA's own PDF.

### Q1 X-ray metrology vs Rigaku

#### KLA X-ray products
| Product | Launch | Applications (KLA words) | Status, KLA words | Status, customer or partner papers | Throughput | Revenue or units |
|---|---|---|---|---|---|---|
| Axion T2000 (CD-SAXS, transmission) | 2022-12-06 [F] Q1-001 | 3D NAND and DRAM. Logic is not mentioned [F] Q1-001, Q1-002 | At launch: "multiple systems in operation at leading memory manufacturers" [C] Q1-003. Mar 2026: "used in high volume manufacturing today" for vertical NAND and DRAM capacitor [C] Q1-005. Apr 2026: adoption "took quite a while"; no "quick adoption of X-ray anytime soon" [S] Q1-007, Q1-008 | KLA+Lam 2024: CD-SAXS as a rapid screen for tilt and bending [S] Q1-011. Kioxia+WD+KLA 2024: CD-SAXS as the reference that trains OCD [S] Q1-012. Lam 2025: CD-SAXS has low depth sensitivity and averages over the spot [S] Q1-013. 2026 Axion 3D NAND hole-distance paper: title only [S] Q1-014 | NOT DISCLOSED (read: launch release; 10-K FY26 Item 1; Investor Day deck and transcripts). Fact sheet NOT RETRIEVED | NOT DISCLOSED (read: 10-K FY26 Item 1 and Item 7; letters Q4 FY24 to Q1 FY27; Investor Day deck). The CFO said the market is $75-100M and KLA's share is about 60% [S] Q1-009. Implied KLA revenue $45-60M a year [I] Q1-010 (Low) |
| Other X-ray (XRR/XRF/HRXRD) | none found | n/a | n/a | n/a | n/a | n/a |

- Investor Day 2026 lists "X-Ray Metrology" under "Portfolio Expansion" (slide p100). It gives no roadmap, revenue or units [F] Q1-006.
- The CFO (Q3 FY26 call) said X-ray CD metrology adoption has been mostly in memory. The market could reach about $150M "over the next few years" [S] Q1-009.

#### Onto–Rigaku alliance
| Item | Value | Tag / id |
|---|---|---|
| Announcement | 2026-04-20 (Onto release; Rigaku release on the same deal, undated page) | [F] Q1-015, Q1-019 |
| Terms | Onto buys 61,123,436 Rigaku shares (27.0%) from Atom Investment L.P. (Carlyle) for about $710M. Onto gets one board seat, uses the fair value option and does not consolidate. Rigaku keeps management independence, and transfers and further share purchases are restricted | [F] Q1-015, Q1-020 |
| Close | 2026-08-10, JPY 113.08B (about $720M) | [F] Q1-018 |
| Product | Onto Ai Diffract analysis software combined with Rigaku CD-SAXS platforms. "selected by two key customers". Market above $1B within 5 years (TechInsights, per Onto) | [C] Q1-016 |
| Aim | "next-generation hybrid metrology" combining X-ray and optical for FEOL logic and memory. OCD gives speed and location, X-ray gives precision on deeper structures | [F] Q1-019, [C] Q1-017 |
| Rigaku target | At least $300M of incremental market opportunity for Rigaku products by 2030 | [C] Q1-021 |
| Prior work | The two companies were already collaborating on Rigaku CD-SAXS plus Onto analytics before the equity deal | [F] Q1-022 |

#### KLA statements since April 2026 on the alliance or on hybrid X-ray + optical CD
| Document | What it says | Tag / id |
|---|---|---|
| Q3 FY26 call, 2026-04-29 (third-party transcript) | Analyst asks about "x-ray versus optical for CD". Wallace: Axion adoption was slow; X-ray may help debug, but cost and throughput block production; "I don't think you're going to see a quick adoption of X-ray anytime soon". Higgins: market $75-100M, KLA about 60%. Onto and Rigaku are not named by KLA | [S] Q1-007..009 |
| Shareholder letters Q3 FY26 (Apr 2026), Q4 FY26 (Jul 2026), Q1 FY27 (Oct 2026) | No mention of X-ray, Axion, Onto, Rigaku or hybrid metrology. NOT DISCLOSED (read: full text of all three letters) | — |
| 10-K FY26 (2026-08-06), 10-Q Q1 FY27 (2026-10-29) | Competition paragraph names Lasertec and Onto; Rigaku is not named; nothing on the alliance. NOT DISCLOSED (read: Item 1 Competition, Item 1A) | [F] Q1-025 |
| KLA IR press releases Jan-Nov 2026 | No product or metrology release | [F] Q1-027 |
| Q1 FY27 call, 2026-10-28 (third-party transcript) | No mention of X-ray, Onto or Rigaku. NOT DISCLOSED (read: full transcript, search for x-ray/Axion/Onto/Rigaku/hybrid) | — |
| Q4 FY26 call, 2026-07-28 | NOT RETRIEVED (tried: fool.com URL 404; fortune.com page holds only header and participants) | — |
| Earlier context (before the alliance), Investor Day Q&A 2026-03-12 | "Hybrid metrology 10 years ago was going to just take over everything but nothing." The remark answered an AI/data question | [C] Q1-026 |
- Summary [I] Q1-028: the only KLA reaction found is the Q3 FY26 call answer. Confidence is Medium because the Q4 FY26 call transcript is missing.

### Q4 EUV mask inspection vs Lasertec

#### KLA reticle portfolio (Investor Day 2026 slide p91, checked against the page image)
| Product | Type | Litho / use case | Release (slide words) | Tag / id |
|---|---|---|---|---|
| Actinic 7xx | actinic (13.5 nm) patterned | EUV, 2x–3x nm, "*Requires NA Change" | "Early Demo Stage" | [F] Q4-001 |
| TeraBeam® 8xx | multi-column e-beam, mask shop | EUV, 1x–3x nm | 2026 | [F] Q4-002 |
| Teron 640e/eS/eS2 | optical, mask shop | EUV, >3x nm | 2017 | [F] Q4-003 |
| Teron 610/630/640 | optical, mask shop | 193/193i, >70 nm | 2009 | [F] Q4-003 |
| Teron SL670e/XP/XP2 | optical, IC fab requal | EUV particles | 2018 | [F] Q4-004 |
| Teron SL650/655/670 | optical, IC fab | 193/193i particles | 2014 | [F] Q4-004 |
| Gen5 Agera wafer print check | wafer inspection | EUV printing particles | 2019 | [F] Q4-004 |

- Actinic status in KLA's words (Mar 2026): a prototype in KLA's lab, with first images and a first inspection taken weeks before Investor Day [C] Q4-007. "We are developing an actinic inspection system" [C] Q4-011. KLA says each scanner NA needs a new actinic system [C] Q4-008. In the IC fab, actinic is "Defense 3", one inspection every 2,000-5,000 wafers, after SL670e XP2 (every 100-200) and Gen5 Agera (every 200-400) [C] Q4-009. KLA calls actinic cost of ownership for requal "quite bad" [C] Q4-010.
- TeraBeam history: the "8XX" e-beam mask platform shipped in 2021 and began customer qualification for 3nm and below [F] Q4-012. It was released to market in 2026 after five years of development at TSMC [C] Q4-005. Use on N2 HVM layers: NOT DISCLOSED (read: Investor Day transcript p40-41, slides p91-94).
- Customer adoption:
  - TSMC is named by KLA for TeraBeam development [C] Q4-005. The TSMC-KLA paper is SPIE 13981-231, DOI 12.3111792, title only [S] Q4-013.
  - Samsung + KLA paper (Photomask, Oct 2026) reports multi-column EBMI used at Samsung as a "production solution". Capture rates were 98% and 96% against specs of 84% and 79% [S] Q4-014.
  - Samsung also co-publishes with Lasertec on actinic (APMI) software [S] Q4-030.
  - SK hynix publishes on an APMI tool; the vendor is not named [S] Q4-031.
  - TSMC evaluated the Lasertec X9ULTRA 193nm tool for N3 EUV masks [S] Q4-032.
- Business signals: the letters cite strong reticle demand in Q1 FY26 and Q2 FY26 [C] Q4-015, Q4-016, and better CY25 mask-inspection share [C] Q4-017. Reticle revenue is reported only inside "Patterning" (Q1 FY27: +29% YoY, 21% of revenue) [F] Q4-018. Q1 FY26 call: KLA is "in conversations with all the leading mask manufacturers" on pellicle and requal strategy [S] Q4-019.
- EUV and reticle optics supplier: NOT DISCLOSED (read: 10-K FY26 Item 1 Manufacturing/Raw Materials, Item 1A supply risk). The 10-K gives only general single- and limited-source language [F] Q4-020. Zeiss is not mentioned.

#### Lasertec ACTIS
| Item | Value | Tag / id |
|---|---|---|
| ACTIS A150 | first actinic EUV patterned mask inspection system, 2019 | [F] Q4-022 |
| ACTIS A200HiT | released 2025-10-31, "Triple inspection speed of ACTIS A150", for wafer-fab incoming and periodic QA | [F] Q4-021 |
| ACTIS A300 Series | listed in the Mar 2026 company profile (High-NA per a secondary lead only) | [F] Q4-023 |
| HVM adoption | "widely adopted in high-volume manufacturing" (Lasertec paper). The paper puts A200HiT at 3x the A100, while the release says 3x the A150 | [S] Q4-029 |
| FY2026 (Jul 2025-Jun 2026) orders | JPY 237.5B vs 105.2B (+125.7%). Semiconductor orders JPY 172.2B; semiconductor backlog JPY 301.3B at 2026-06-30 (93.3% of total backlog). Semiconductor book-to-bill 1.02 | [F] Q4-024, Q4-025; [I] Q4-028 |
| Q1 FY2027 (Jul-Sep 2026) | sales JPY 40.4B (-25.5%), semiconductor JPY 23.8B (-42.9%). FY2027 order outlook "exceeded previous expectations"; advances received +JPY 42.8B | [F] Q4-026; [C] Q4-027 |
| ACTIS sales or orders | NOT DISCLOSED (read: tanshin FY2026 pp5,18; tanshin Q1 FY2027 pp4,10; Business Report page). The results presentation, where any ACTIS split would be, is NOT RETRIEVED (tried: lasertec.co.jp/en/ir/data/result.html, which loads through a JS widget from eir-parts.net; publicnow copy 403) | — |

### NV: KLA vs Nova (light touch)
- Nova names Onto and KLA as its main competitors in CD, thin-film and chemical metrology [F] NV-001.
- KLA counterparts: SpectraShape (OCD), SpectraFilm and Aleris (films), Archer/ATL (overlay), Axion (X-ray CD) [F] NV-005. ECI Technology (chemical, acquired 2022) [F] NV-004, [C] NV-006.
- Nova's X-ray product is VeraFlex (XPS+XRF materials metrology). Nova also has Metrion (SIMS) and Elipson (Raman). KLA lists no XPS, SIMS or Raman product [F] NV-002, NV-003, NV-005.

### Competition table (handoff)
| Area | KLA product | Rigaku | Onto | Lasertec | Nova | Tags |
|---|---|---|---|---|---|---|
| X-ray CD (CD-SAXS) for HAR memory | Axion T2000 (2022). KLA claims HVM use and ~60% of a $75-100M market | XTRAIA CD-3200T (TSAXS), CD-3200G (GISAXS) | Ai Diffract software on Rigaku CD-SAXS, plus 27% equity in Rigaku | — | none found | [F] Q1-001, Q1-023, Q1-015; [S] Q1-009 |
| X-ray films/materials (XRR, XRF, HRXRD, XPS) | none listed | XTRAIA MF (EDXRF+XRR+XRD, hybrid with optical), XTRAIA XD (HRXRD), TXRF, WDXRF | via Rigaku | — | VeraFlex (XPS+XRF) | [F] Q1-024, NV-002 |
| Hybrid X-ray + optical CD | none announced; CEO skeptical | with Onto | with Rigaku | — | — | [F] Q1-019; [S] Q1-008 |
| OCD / films | SpectraShape, SpectraFilm, Aleris | — | Atlas OCD | — | i Platform, T-platform, VeloCD, Prism | [F] NV-005, NV-002, Q1-017 |
| Materials metrology (SIMS, Raman, chemical) | ECI chemical analysis only | — | — | — | Metrion, Elipson, Ancolyzer | [F] NV-002, NV-004 |
| EUV actinic patterned mask | Actinic 7xx, Early Demo Stage | — | — | ACTIS A150 (2019), A200HiT (2025), A300 | — | [F] Q4-001, Q4-021..023 |
| EUV e-beam patterned mask | TeraBeam 8xx (2026) | — | — | none found | — | [F] Q4-002 |
| EUV optical mask (mask shop / fab requal) | Teron 640e/eS/eS2; Teron SL670e/XP/XP2; Gen5 Agera print check | — | — | X9ULTRA (193nm, TSMC N3 evaluation) | — | [F] Q4-003, Q4-004; [S] Q4-032 |

### Disputed-claims ledger row
| Claim | Who said it, when | Evidence for | Evidence against | Strongest tag on each side |
|---|---|---|---|---|
| KLA's actinic patterned-mask inspection is close to production | Prior chat (Nov 2026) framing; the Investor Day question about actinic, Mar 2026 | KLA has a lab prototype with first images and a first inspection, and says results "look quite impressive" [C] Q4-007. "We are developing an actinic inspection system" [C] Q4-011 | Slide release column reads "Early Demo Stage" with no date [F] Q4-001. KLA itself places actinic as a low-frequency "Defense 3" and calls its cost of ownership poor [C] Q4-009, Q4-010. No actinic mention in letters Q3 FY26-Q1 FY27 or in any 2026 press release [F] Q1-027, Q4-018. Lasertec ACTIS has shipped since 2019, and the 3x-throughput A200HiT has been out since Oct 2025 [F] Q4-021, Q4-022. KLA's 2026 product launch was e-beam (TeraBeam), not actinic [F] Q4-002. [I] Q4-033: KLA's own disclosures refute "close to production" (Medium) | For: [C]. Against: [F] |

### Prior-claim check (kla_metrology_audit.md lines 21-68 and the KLA row at line 1033; Onto row at 1034 where it touches Rigaku)
| Prior claim | Result | Evidence |
|---|---|---|
| EUV reticle tools: Teron 640e/eS/eS2, Teron SL670e XP2, Gen5 Agera print check, TeraBeam 8xx | CONFIRMED (names) | Q4-002..004 |
| TeraBeam 8xx "12×12 multi-column EBMI at TSMC N2 HVM" | CORRECTED: KLA says 5 years of development at TSMC, released 2026 [C]. "N2 HVM" is NOT VERIFIABLE. "12×12" is in the transcript, but the same passage says "24 columns" | Q4-005, Q4-006 |
| "Actinic 7xx … Early Demo Stage, requires NA change" | CONFIRMED. "*Requires NA Change" is a footnote on the 2x–3x nm use case; "Early Demo Stage" is in the release-date column | Q4-001 |
| TeraBeam High-NA and nano-imprint reticle feasibility | NOT VERIFIABLE (nano-imprint appears in no saved doc) | — |
| 8xx shipped for ≤3 nm qualification "Q2 CY2021" (Q4 FY21 letter) | CORRECTED (minor): the letter says "shipped last quarter" in the Jun-2021-quarter letter, which may mean Jan-Mar or Apr-Jun 2021. Qualification at "3nm and below" is CONFIRMED | Q4-012 |
| Actinic 7xx milestone "MISSED" | NOT VERIFIABLE as "missed": no dated KLA commitment was found. Status is early demo | Q4-001, Q4-033 |
| Lasertec ACTIS A200HiT launched Oct 2025, 3× A150 speed | CONFIRMED (2025-10-31). A Lasertec paper uses the A100 as the 3x baseline | Q4-021, Q4-029 |
| Lasertec JPY 114.8B FY25 ACTIS sales | NOT VERIFIABLE: the presentation is NOT RETRIEVED and the tanshin has no product split. A secondary lead attributes the figure to the Lasertec FY6/2025 presentation script | — |
| Lasertec ACTIS "sole commercial 13.5 nm actinic HVM system" | NOT VERIFIABLE as "sole". Lasertec claims wide HVM adoption [S]. No other commercial actinic patterned inspector was found | Q4-029 |
| Axion: transmissive CD-SAXS, non-destructive HVM 3D shape/tilt metrology | CONFIRMED (CD-SAXS, transmissive; HVM as a KLA claim). "Twisting" is not in KLA's words (release says width, shape, tilt) | Q1-002, Q1-005 |
| Axion 3D NAND twisting validation (Lam + KLA, 2 wafers, 651 sites, R²>0.84, CD-SEM calibration), doi 10.1117/12.3090197 | CORRECTED: the DOI exists, but its title is about hole-to-hole distance variance. The figures and the Lam affiliation are NOT VERIFIABLE (abstract NOT RETRIEVED) | Q1-014 |
| TSMC + KLA: optical hits resolution limits on N2 curvilinear masks, requiring 12×12 e-beam (doi 12.3111792) | NOT VERIFIABLE (abstract NOT RETRIEVED). KLA's summary of the TSMC paper: DUV covers ≥36 nm reticle printed pitch, e-beam down to 20 nm | Q4-013; transcript p40 |
| Onto row: "Rigaku 27% / Ai Diffract X-ray tie-up" | CONFIRMED (Onto holds 27% of Rigaku; Ai Diffract is Onto software) | Q1-015, Q1-016, Q1-018 |
| Onto row: Rigaku optical+X-ray HVM guided ~2028+ (Onto Q1 2026 call) | NOT VERIFIABLE (Onto call transcript not retrieved) | — |

### Gaps (one line each)
- Axion fact sheet: NOT RETRIEVED (tried: kla.com/documents/pdf/KLA_Axion_T2000_ProductFactSheet.pdf returns HTML; kla.com Axion page and metrology product page are JS shells with no text).
- Axion throughput: NOT DISCLOSED (read: launch release 2022-12-06; 10-K FY26 Item 1; Investor Day deck and transcripts).
- Axion revenue and units: NOT DISCLOSED (read: 10-K FY26 Items 1 and 7; letters Q4 FY24-Q1 FY27; Investor Day deck). Only the CFO market and share remark exists [S].
- SPIE abstracts 10.1117/12.3090197 and 12.3111792: NOT RETRIEVED (tried: doi.org to spiedigitallibrary.org, Incapsula block; Crossref and OpenAlex have no abstract).
- KLA Q4 FY26 call transcript: NOT RETRIEVED (tried: fool.com 404; fortune.com header only).
- Lasertec FY2026 and Q1 FY2027 results presentations (ACTIS split): NOT RETRIEVED (tried: lasertec.co.jp IR result page JS widget; publicnow 403).
- ACTIS sales or orders: NOT DISCLOSED (read: Lasertec tanshin FY2026 p18, Q1 FY2027 p10).
- Actinic 7xx release date: NOT DISCLOSED (read: Investor Day slides p91-94, transcript p40-41, Q&A p12; letters Q3 FY26-Q1 FY27).
- TeraBeam unit count and customers beyond TSMC/Samsung: NOT DISCLOSED (read: Investor Day slides p91-93, transcript p40).
- Reticle inspection revenue: NOT DISCLOSED (read: letters Q1 FY26-Q1 FY27, Patterning paragraphs).
- KLA EUV/reticle optics supplier: NOT DISCLOSED (read: 10-K FY26 Item 1 Manufacturing, Item 1A).
- Onto-Rigaku Business Wire copies: NOT RETRIEVED (tried: three businesswire.com URLs, HTTP/2 stream error). Onto's own q4cdn PDFs were saved instead.
- Rigaku release date on rigaku.com: NOT DISCLOSED on the page (read: full page text). Date taken from Onto's same-day release.
- Onto Q1 2026 call / 10-Q (Rigaku HVM timing): NOT RETRIEVED (not tried: investors.ontoinnovation.com is a known 403).

## Part Q2, Q3: advanced packaging, hybrid bonding

KLA fiscal year ends June 30. Calendar years (CY) are used for AP revenue because KLA states them that way. Onto and Camtek have December year-ends. No per-share figures are used here. Evidence ids refer to `parts/Q2.csv` and `parts/Q3.csv`. Arithmetic: `calc/q2_ap_revenue.py`.

### Q2-A. KLA advanced-packaging (AP) revenue: two definitions

KLA uses two different AP figures. The prior chat put them side by side as if they were the same thing.

| Period | Figure | KLA definition (wording) | Date stated | Evidence |
|---|---|---|---|---|
| CY24 (Jan-Dec 2024) | > $500M, later "~$500M" | "total advanced packaging revenue across the entire KLA portfolio" | 2024-07-24, 2025-01-30 | [F] Q2-001, Q2-002 |
| CY25 estimate | > $925M; process control "over 70%" of it | "advanced packaging related revenue" | 2025-07-31 | [F] Q2-003 |
| **CY25 actual, total** | **~$950M, ">70% YoY"** | "calendar 2025 total systems revenue" (all KLA AP systems) | 2026-01-29 | [F] Q2-005; same on Investor Day slide 68 [F] Q2-012 |
| **CY25 actual, process control** | **~$635M** | "Semiconductor Process Control product portfolio revenue" | 2026-04-29 | [F] Q2-007 |
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

### Q2-B. Tool-level wins and losses vs Onto and Camtek (non-KLA sources)

| KLA tool | Non-KLA report of a specific KLA win or loss | What competitors report nearby |
|---|---|---|
| Kronos 1190 / 1190XR (2D patterned AP inspection) | None found | Onto: an HBM maker chose Dragonfly G5 + 3Di after onsite competitive evaluations, "displacing the previously established tool of record" (incumbent not named) [C] Q2-029. Camtek: >$50M Hawk orders from "a leading HBM player" [F] Q2-035 |
| CIRCL-AP (all-surface cluster) | None found | Onto Dragonfly G5 qualified for 2.5D (second qualification) [C] Q2-031 |
| ICOS F26x / T-series (component, post-dice) | None found | n/a (Onto and Camtek do not target final component inspection in the saved documents) |
| Zeta-5xx/6xx, Micro-SR, eDR AP, irArcher, PWG5 XT | None found | Camtek's 3D bump metrology "leadership" (call summaries, not saved) |

- Result: **no non-KLA source located names a specific KLA packaging win or loss.** Competitors' win releases do not name the vendor they displaced. [I] Q2-I07.
- Onto's 10-K names "KLA and Camtek" as its principal AP-inspection competitors. [F] Q2-028
- Camtek's 20-F names no competitor. It describes about six months of side-by-side competitive evaluations. [F] Q2-033. Its Oct 2026 deck says "Compete with larger players" without naming them. [C] Q2-037
- KLA's own view: AP process-control share above 50% in 2025, "more concentrated in leading edge logic", with memory and OSATs named as opportunities. [C] Q2-015. #1 share, +14 pp. [C] Q2-014
- Scale for comparison: Camtek's Q3 2026 revenue was $161.3M and its FY26 guide is ~$595M [F] Q2-038; >$800M orders YTD, ~80% AP [C] Q2-036. Onto's Q3 2026 revenue was $409.7M, with record AP revenue led by Dragonfly G5/Firefly [F] Q2-032.
- Onto frames AP demand as "driven by assembly volumes" [F] Q2-039. KLA frames it as intensity plus share.
- Leads not saved: an Onto technology award from SK hynix for Dragonfly G5 (Zacks via web search, not retrieved) and DigiTimes CoWoS tool allocation (paywalled). Neither names KLA.

### Q3. Hybrid-bonding coverage map

| Step | KLA tool offered | Status (evidence) | Gap | Onto | Camtek |
|---|---|---|---|---|---|
| Incoming wafer shape / flatness, bow, warpage | PWG5 with XT Option (packaging list) | Listed in 10-K FY24-FY26 [F] Q3-005. HB/D2W shipment status NOT DISCLOSED (read: 10-K FY26 Item 1) | No die-level warpage product named | Not in saved docs | Pre-bond wafer and die warpage: 2027-28 roadmap [C] Q3-017 |
| Pre-bond surface defects / particles | Puma, Voyager, BBP (29xx/Gen4). KLA says Kronos "not going to be sufficient" [C] Q3-003; "whole suite of systems", "next four systems" developed [C] Q3-001, Q3-002 | Announced/ready per KLA (Mar 2026). HB-specific HVM shipments NOT DISCLOSED | KLA's target: 0.05-0.5 µm sensitivity [C] Q3-004 | Dragonfly G5 150 nm [C] (Q2-029 release) | Hawk 150 nm, marketed for HB [F] Q2-034; <150 nm HB requirement [C] Q3-018 |
| Cu recess / dishing, topography | Not named for HB in saved docs. Candidates on slide 66 (SpectraShape, Zeta, Aleris) are an inference only | Status NOT DISCLOSED | KLA's target: 0.001 µm Cu-recess accuracy [C] Q3-004 | 3Di (bumps) | Post-CMP dishing/roughness: 2027-28 roadmap [C] Q3-017 |
| Bond overlay (post-bond, IR) | irArcher Series | Listed in 10-K [F] Q3-005. The ST/KLA ECTC 2023 paper (irArcher 007 for W2W) is a lead only (403). D2W status NOT DISCLOSED | Precision specs not retrievable | Not in saved docs (TheElec says PLA can also measure overlay [S] Q3-014) | Not in saved docs |
| Post-bond buried voids | **None found** | [I] Q3-I01 | Gap | EchoScan (launched Jan 2025, ≥1 µm voids) [C] Q3-012; PLA SPIE 2026 [F] Q3-010, [C] Q3-011; in validation on Samsung production lines [S] Q3-014 | 2027-28 roadmap item [C] Q3-016 |

- Onto, describing the incumbent void method (unnamed, presumably SAM): "≥10µm void size sensitivity", water immersion required. [C] Q3-013
- Samsung is also talking to several ultrasound and X-ray vendors (not named) [S] Q3-015. SAM vendors (e.g. PVA TePla, Hitachi, Sonix) are not covered by any saved source: NOT RETRIEVED (tried: no search pass on SAM vendors beyond TheElec).
- KLA on HBM: two stacking processes are in use, and failure rates rise "on a log scale" with stack height [C] Q3-007. Both HB and TC-NCF raise intensity, and KLA is "not choosing" [C] Q3-008. The Annual Report says customers "increasingly adopted" HB in FY26 [C] Q3-006.
- Post-bond voids at KLA: no product, partnership, acquisition or stated intent appears in the 10-K FY26, the 10-Q for Q1 FY27, Annual Report 2026, the Investor Day deck and transcript, or the letters [I] Q3-I01. The IMAPS 2026 KLA paper abstract is generic [F] Q3-019. KLA job postings: NOT RETRIEVED (tried: not searched, time). SPIE/ECTC full texts by KLA authors (e.g. 10.1117/12.3049615 "Shape-induced overlay for W2W hybrid bonding", 2025; affiliations not confirmed): NOT RETRIEVED (tried: Crossref metadata only).

### Ledger evidence (B1 input)

| Claim | For | Against | Strongest tag (for / against) |
|---|---|---|---|
| Process-control intensity rises with AP and HBM | KLA packaging intensity (KLA Semi PC AP revenue / AP market) 0.4% (2018) → 5.6% (2025) [C] Q2-016; HB specs ~10x tighter (0.05-0.5 µm vs 1-5 µm) [C] Q3-004; HBM gave a $450M incremental intensity gain in CY25 [C] Q2-018; KLA's CY26 AP process-control growth is ~2x the AP market [C] Q2-009; Camtek: <150 nm HB particle sensitivity, more RDL steps [C] Q3-018; Onto: AP inspection rates are high [F] Q2-039 | KLA's "intensity" metric mixes share gain with intensity (KLA's own definition, Q2-016). Process control's share of AP capex is NOT DISCLOSED as a number (read: Investor Day slide 143, a chart without data labels; a visual read puts it at ~$1.3B of ~$11.3B, [I] Q2-I06, Low). Onto: AP demand is driven by assembly volumes [F] Q2-039. No third-party quantified intensity figure found | [C] / [F] |
| AP revenue exceeds $1.1B in CY26 | Guide ~$1.1B (>70%) on 2026-07-28, reaffirmed 2026-10-28 [C] Q2-009, Q2-010; call summary [S] Q2-030 | It is "approximately $1.1B", not "exceeds". The definition is AP **process control systems** only. On the total-systems basis the Jan 2026 guide (mid-teens on $950M ≈ $1.07-1.11B) was never updated [C] Q2-006; KLA has not given a CY26 total-AP figure since. CY26 actual is not reported until late Jan 2027 | [C] / [C] |
| Post-bond buried-void inspection stays outside KLA's portfolio | No void product or intent in KLA filings, deck or transcript [I] Q3-I01; Onto has a launched tool and a Samsung JDP [C] Q3-012, [S] Q3-014 | KLA says it has a "whole suite" of HB systems and four more developed (unnamed) [C] Q3-001, Q3-002. kla.com product pages were not retrievable, so an unlisted product cannot be excluded. Camtek is also only at roadmap stage [C] Q3-016 | [I] / [C] |

### Competition table for the handoff (step by step; names from saved sources)

| Step | KLA | Onto | Camtek |
|---|---|---|---|
| 2D patterned AP inspection (bumps, RDL, post-dice) | Kronos 1190/1190XR, CIRCL-AP; Puma/Voyager/29xx adapted [F] Q2-019, [C] Q2-026 | Dragonfly G5 (150 nm), Firefly (panel) [C]/[F] Q2-029, Q2-032 | Hawk (150 nm), Eagle G5 / Eagle-i / Eagle-AP [F] Q2-034 |
| 3D bump metrology | Zeta-5xx/6xx, Micro-SR (inference: segment lists, no spec retrieved) | 3Di on Dragonfly [C] Q2-029 | Eagle-AP / Hawk 3D metrology; 10th-generation sensor for <5 µm bumps in 2027 [C] (Camtek deck p17) |
| Defect review | eDR7xxxAP [F] Q2-019 | not in saved docs | not in saved docs |
| Wafer/die shape, warpage | PWG5 XT [F] Q3-005 | not in saved docs | roadmap [C] Q3-017 |
| Bond overlay | irArcher [F] Q3-005 | not in saved docs | not in saved docs |
| Post-bond voids | none found [I] Q3-I01 | EchoScan / PLA [C] Q3-012 | roadmap [C] Q3-016 |
| Final component inspection | ICOS F26x / Tx [F] Q2-020 | n/a | n/a |
| Process tools (etch, dicing, deposition) | SPTS (Specialty Semiconductor Process) [F] Q2-021 | lithography (JetStep) | n/a |

### Prior-claim check (prior/text/kla_metrology_audit.md)

| Prior claim | Result | Evidence |
|---|---|---|
| "Total AP revenue ~$950M in CY25" | CONFIRMED (total systems basis) | [F] Q2-005, Q2-012 |
| "AP Process Control Systems revenue on track for $1.1B+ in CY26 (+70%+ YoY)" | CORRECTED: "approximately $1.1 billion", not "$1.1B+"; growth >70% on a $635M process-control base, not on $950M | [C] Q2-010, [F] Q2-007, [I] Q2-I01, Q2-I02 |
| "share ~4x over 4 years" | CONFIRMED as KLA claim | [C] Q2-013 |
| "irArcher 007 post-bond IR overlay 1.5-3.3 nm precision across 100-350 µm die" | NOT VERIFIABLE: irArcher Series is in the 10-K, but no saved source gives these numbers (kla.com JS challenge; ECTC 2023 PDF 403; IMAPS abstract silent) | [F] Q3-005, [F] Q3-019 |
| "PWG5 XT option" | CONFIRMED (10-K FY24-FY26: "PWG5 with XT Option") | [F] Q3-005 |
| "Kronos 1190XR down to 150 nm" | NOT VERIFIABLE from KLA (the 2020 release gives no nm figure; kla.com not retrievable; DirectIndustry 403). Also, KLA says Kronos is not sufficient for HB, so its use as an HB pre-bond tool is CORRECTED | [F] Q2-027, [C] Q3-003 |
| "IMAPS 2026-08-11 doi 10.4071/001c.171430" | CORRECTED: the DOI resolves to Chet Lenox (KLA), "AI-Driven Process Control for Advanced Packaging", IMAPSource Proceedings, Crossref date 2026-09-21 (an 08-11 event date is not shown). The abstract does not support the irArcher, Kronos or void details the prior chat cited to it | [F] Q3-019 |
| "Samsung + Onto SPIE 2026 doi 10.1117/12.3095356 PLA 1 µm voids under 665 µm Si" | PARTLY CONFIRMED: the DOI, title and 1 µm figure check out; it was presented 2026-02-24 and published 2026-04-08 (not "Apr 8 presentation"). Samsung co-authorship and "665 µm Si" are NOT VERIFIABLE (no affiliations in Crossref; the abstract lacks 665 µm). A Samsung–Onto JDP is reported by [S] TheElec | [F] Q3-010, [C] Q3-011, [S] Q3-014 |
| "HBM hybrid bonding future adoption; 8H/12H and 12H/16H remain TCB" | NOT VERIFIABLE as a KLA statement. KLA says DRAM moves to HB "in the future" and it is indifferent; the deck shows "8 to 12 chip stacks"; no 16H/TCB roadmap appears in the KLA deck or transcript | [C] Q3-009, Q3-008 |
| "KLA has no commercial post-bond buried-void tool" | CONFIRMED as absence in saved KLA documents (inference) | [I] Q3-I01 |
| KLA row "zero post-bond buried-void PLA tool" | CONFIRMED (same basis) | [I] Q3-I01 |

### Premise issues

- The prompt's "$1.1B" and "$950M" use different definitions: process-control systems vs total systems (see Q2-A).
- The CY26 process-control guide is "approximately $1.1 billion", not "$1.1B+" or "exceeds $1.1B".
- The transcript renders Kronos as "Chronos" (p29-30) and "corona" (p78).
- The prompt names "CIRCL" lines; the 10-K spells it CIRCL-AP (Semi PC). ICOS and Zeta sit in the PCB and Component Inspection segment, not Semi PC. "Frontier" does not appear in the 10-K FY26; the PCB line is "Frontline". The Orbotech packaging-related lines are Corus/Precise (IC substrate).
- IMAPS DOI date: Crossref gives 2026-09-21, not 2026-08-11.
- SPIE 2026 PLA paper: Onto presented it on 2026-02-24; proceedings were published 2026-04-08.

### Retrieval notes (for the lead)

- www.kla.com serves a JavaScript bot-challenge page to fetch.py. These saved files contain no content and should be treated as NOT RETRIEVED although the manifest says RETRIEVED: `2026-11-21_kla_product-page-AP-wafer-inspection-metrology.html`, `2026-11-21_kla_solutions-page-advanced-packaging.html`, `2026-11-21_kla_advance-article-p74080.html`. `Advanced_Packaging_Portfolio_Overview.pdf` returned HTML (NOT RETRIEVED).
- The Camtek order release `2026-01-01_camtek_press-release-105M-orders-OSAT-HBM.html` is actually dated 2026-06-02 (wrong date in the file name; the CSV gives the correct date).
- The Onto Q3 2026 release was saved from a finviz copy of Business Wire (`2026-11-05_onto_...`); the release date in the text is 2026-11-09.

### Gaps

- NOT DISCLOSED (read: KLA letters Q4 FY24-Q1 FY27, 10-K FY26): AP revenue by product family; SPTS and PCB/Component AP revenue; CY26 total-systems AP update; CY27 AP figure.
- NOT DISCLOSED (read: Investor Day slide 143): process-control share of AP equipment market as a number.
- NOT RETRIEVED (tried: kla.com product pages via fetch.py → JS challenge): Kronos 1190XR, CIRCL-AP, irArcher, ICOS F26x, Zeta, Micro-SR specification pages.
- NOT RETRIEVED (tried: conferences.computer.org 403): ECTC 2023 ST/KLA irArcher paper.
- NOT RETRIEVED (tried: directindustry.com 403): Kronos 1190XR 150 nm listing.
- NOT RETRIEVED (tried: Crossref only): affiliations and full text of SPIE 10.1117/12.3095356 (Samsung co-authorship, 665 µm Si).
- NOT RETRIEVED (tried: web search; DigiTimes paywalled; no Korean/Taiwan article names KLA): a non-KLA report of a specific KLA AP win or loss.
- NOT DISCLOSED (read: Camtek 20-F FY2025 Item 3/4; Oct 2026 deck; Q3 2026 release): Camtek's named competitors.
- NOT RETRIEVED (tried: not attempted): KLA job postings on void or acoustic inspection; SAM vendor sources.

## Part A1, A2: results, segments, services, leading signals

Fiscal year ends June 30. Quarters: Q2 FY26 = Oct-Dec 2025, Q3 FY26 = Jan-Mar 2026, Q4 FY26 = Apr-Jun 2026, Q1 FY27 = Jul-Sep 2026 (latest). $ in millions unless stated. Per-share figures: Q4 FY26 and later documents are post-split (10-for-1, effective June 11, 2026); the Q2 and Q3 FY26 releases and letters are pre-split [F] A1-037. No per-share figure is used below.
Scripts: `research/out/kla/calc/a12_results.py` (A1), `research/out/kla/calc/a12_leading.py` (A2). Every built-in check passed: segment and product sums, FY26 = sum of quarters, adjustment totals, recomputed non-GAAP margins within 0.05pp of KLA's stated figures.

### A1 Results

#### Quarterly and annual P&L, GAAP vs non-GAAP

KLA's non-GAAP figures leave out the one-off items it names itself. For the four latest quarters that means only **acquisition-related charges**, which are mainly intangible amortisation [F] A1-009. In Q4 FY26 they also include an $11.6M discrete interest release, which sits below operating income [F] A1-010. FY25 also left out **restructuring/severance** of $7.1M [F] A1-016 and a **$239.1M goodwill and intangible impairment** of the PCB business [F] A1-015. Tax-only items affect net income, not margins: Pillar Two UTPR taxes ($20.2M in Q1 FY27) and discrete tax items [F] A1-011. KLA does not print an operating income line, so GAAP operating income here = revenue - COGS - R&D - SG&A (- impairment).

| Period | Revenue | YoY | GM GAAP | GM ex one-offs (non-GAAP) | OM GAAP | OM ex one-offs (non-GAAP) | One-offs above op. line | FCF | SBC | SBC/FCF |
|---|---|---|---|---|---|---|---|---|---|---|
| Q2 FY26 (Oct-Dec 25) | 3,297.1 | +7.2% | 61.4% | 62.6% | 41.3% | 42.8% | acq. 49.0 | 1,262.0 | 73.9 | 5.9% |
| Q3 FY26 (Jan-Mar 26) | 3,415.1 | +11.5% | 61.1% | 62.2% | 41.2% | 42.6% | acq. 47.0 | 622.3 | 83.9 | 13.5% |
| Q4 FY26 (Apr-Jun 26) | 3,657.6 | +15.2% | 61.4% | 62.4% | 42.5% | 43.7% | acq. 44.7 (+(11.6) below op.) | 817.1 | 82.1 | 10.0% |
| Q1 FY27 (Jul-Sep 26) | 4,136.0 | +28.9% | 61.9% | 62.7% | 45.0% | 46.1% | acq. 43.0 | 1,336.2 | 84.1 | 6.3% |
| FY26 (Jul 25-Jun 26) | 13,579.5 | +11.7% | 61.3% | 62.4% | 41.7% | 43.1% | acq. 189.7 (+(11.6) below) | 3,767.1 | 310.2 | 8.2% |
| FY25 (Jul 24-Jun 25) | 12,156.2 | +23.9% | 60.9% | 62.3% | 39.3% | 43.1% | acq. 219.7, restr. 7.1, impairment 239.1 | 3,746.6 | 265.0 | 7.1% |
| LTM to Sep 30, 2026 | 14,505.8 | +15.8% | 61.5% | 62.5% | 42.6% | 43.9% | acq. 183.6 | 4,037.6 | 324.1 | 8.0% |

Sources: revenue [F] A1-001..004; YoY [I] A1-005. GAAP GM as printed by KLA (61.9/61.4/61.1/61.4) [F] A1-006. Non-GAAP GM/OM as stated by KLA [F] A1-017..022. Margin table [I] A1-023, A1-024 (High). LTM [I] A1-025, A1-026 (High). FCF [F] A1-027..031: Q1 FY27 OCF 1,530.9 - capex 194.8 = 1,336.2 [F] A1-028. SBC [F] A1-032..035; SBC/FCF [I] A1-036.
- Q3 FY26 items KLA named but neither excluded nor quantified: opex higher on "prototype materials timing and other reserve adjustments", and other income helped by a mark-to-market gain on a strategic supply investment [F] A1-021. The amounts are NOT DISCLOSED (read: Q3 FY26 letter p5, Q3 FY26 release reconciliation), so the margin cannot be shown without them.
- FCF swings with working capital. Q3 FY26 FCF of $622M was low because deferred system revenue fell $237M and receivables rose $234M; this comes from the cash-flow statement in the Q3 FY26 release, not from a separate evidence row.

#### Revenue by reported segment (USD M; YoY; share of revenue)

| Segment | Q2 FY26 | Q3 FY26 | Q4 FY26 | Q1 FY27 | FY26 |
|---|---|---|---|---|---|
| Semiconductor Process Control (incl. its services) | 3,004.6 (+9.0%; 91%) | 3,083.9 (+12.6%; 90%) | 3,256.8 (+13.2%; 89%) | 3,754.3 (+29.5%; 91%) | 12,244.7 (+11.9%; 90%) |
| Specialty Semiconductor Process | 140.6 (-12.4%) | 164.0 (+4.8%) | 159.7 (+12.6%) | 139.5 (+16.5%) | 584.1 (-0.5%) |
| PCB and Component Inspection | 152.2 (-5.5%) | 167.6 (-0.5%) | 241.1 (+56.5%) | 242.2 (+27.8%) | 750.4 (+20.7%) |

[F] A1-038..041; [I] A1-042.

#### Revenue by major product group (10-Q/10-K disaggregation; USD M, YoY)

| Product | Q2 FY26 | Q3 FY26 | Q4 FY26 | Q1 FY27 | FY26 |
|---|---|---|---|---|---|
| Wafer Inspection | 1,572.8 (+0.7%) | 1,739.7 (+16.3%) | 1,781.1 (+0.5%) | 2,111.2 (+37.3%) | 6,630.8 (+7.0%) |
| Patterning (metrology + reticle inspection) | 696.2 (+31.2%) | 615.1 (-3.4%) | 728.1 (+60.8%) | 862.5 (+29.2%) | 2,706.8 (+23.2%) |
| Specialty Semi Process (systems) | 121.6 (-15.0%) | 144.2 (+4.2%) | 136.5 (+11.0%) | 113.6 (+13.3%) | 502.5 (-2.8%) |
| PCB & Component Inspection (systems) | 80.3 (-13.9%) | 95.1 (-8.7%) | 167.5 (+96.2%) | 167.5 (+42.8%) | 460.3 (+29.3%) |
| Services | 786.1 (+17.8%) | 774.8 (+15.8%) | 820.4 (+16.8%) | 850.5 (+14.2%) | 3,125.9 (+16.5%) |
| Other (refurb/legacy/upgrades) | 40.2 | 46.2 | 23.9 | 30.7 | 153.1 |

[F] A1-043..047; [I] A1-048. The Q4 FY25 base is derived as FY25 minus 9M FY25 and reconciles to reported Q4 FY25 revenue. No finer split (metrology vs reticle inspection, e-beam, optical) is given each quarter: NOT DISCLOSED (read: 10-Q Q1 FY27 segment note; Q1 FY27 letter p4-5; slides p6) [F] A1-049.

#### End market (Semi Process Control systems only, semiconductor customers only, approximate)

KLA definition: "approximate Semi Process Control system-only sales to Foundry/Logic customers or Memory customers only" [F] A1-050.

| | Q2 FY26 | Q3 FY26 | Q4 FY26 | Q1 FY27 | Q2 FY27 guide |
|---|---|---|---|---|---|
| Foundry/logic | ~60% | ~62% | ~79% | ~72% | ~60% |
| Memory | ~40% | ~38% | ~21% | ~28% | ~40% |
| DRAM / NAND within memory | 75 / 25 | 86 / 14 | ~83 / 17 | NOT DISCLOSED (read: Q1 FY27 letter p4, slides p5) | ~84 / ~16 |

[F] A1-051..054; guide [C] A1-055. Implied DRAM share of the base: 30.0% / 32.7% / 17.4% [I] A1-056 (Medium; built from rounded approximations).

#### Services

- Quarterly: $786M (+18%), $775M (+16%), $820M (+17%), $850M (+14%) [F] A1-057..060. FY26 $3,125.9M, +16.5%, 23.0% of revenue. LTM $3,231.8M (22.3%) [I] A1-061. CY25 $2.9B, +15% [F] A1-068.
- Contracted share: ">80% of revenue (up from >75% in CY22) coming from multi-year, subscription service contracts" [C] A1-062. Same Investor Day deck: "~3-year average contract length", "95% contract renewal rate", and "95% of revenue is recurring: inclusive of both contract and time-and-materials" [C] A1-063. Spoken at Investor Day, the contracts are "more than three years" [C] A1-064. This differs from the slide's "~3-year average", so treat contract length as about 3 years. The Nov 2025 update (CY24 actuals) gave >75% contracts, >95% renewal and >3 yr length [C] A1-065.
- KLA does not give a share of contracts on long-term agreements beyond the >80% figure, and no RPO for service contracts beyond deferred service revenue: NOT DISCLOSED (read: Investor Day slides p104-113; 10-Q Q1 FY27 Note 2).
- Long-term target: 13-15% CAGR, raised at the Mar 2026 Investor Day (12-14% in 2022, 9-11% in 2019) [C] A1-066. CY26 is expected at the top end of that range [C] A1-067.

#### Advanced packaging / HBM / AI (light touch; the AP agent owns the deep dive)

KLA uses two AP revenue definitions, and they are not interchangeable:
- "calendar 2025 **total systems revenue** of approximately $950 million", >70% YoY (Q2 FY26 letter) [C] A1-069. The Investor Day slide labels it "~$950M KLA Advanced Packaging Revenue in 2025".
- AP "**Semiconductor Process Control product portfolio** revenue": ~$635M in 2025, rising to ~$1B in CY26 (Apr 2026 view) [C] A1-070. Since Jul 2026, "Advanced Packaging **process control systems** revenue" is expected at ~$1.1B in CY26, >70% YoY [C] A1-071. So the >70% growth is measured on the ~$635M process-control base.
- Intensity definition: "KLA Semi PC systems revenue in Advanced Packaging / Advanced Packaging Market" = 5.6% in 2025 [C] A1-072.
- Implied share of CY25 revenue ($12,745M): ~7.5% on the $950M total-systems basis and ~5.0% on the $635M process-control basis. The ~$315M gap is probably non-process-control AP systems (e.g. SPTS); KLA does not say so [I] A1-073 (Medium).
- KLA gives no HBM or AI percentage of revenue, only qualitative statements: NOT DISCLOSED (read: Q1 FY27 letter/slides/10-Q, Q4 FY26 letter) [F] A1-074.

### A2 Leading signals

| Item | Jun 30, 2025 | Dec 31, 2025 | Mar 31, 2026 | Jun 30, 2026 | Sep 30, 2026 | Evidence |
|---|---|---|---|---|---|---|
| Backlog ($B) | 7.86 | NOT DISCLOSED | NOT DISCLOSED | 12.57 | NOT DISCLOSED ("continues to grow") | [F] A2-001, A2-003; [C] A2-004 |
| Orders / book-to-bill | NOT DISCLOSED | NOT DISCLOSED | NOT DISCLOSED | FY26 implied ~1.35 | NOT DISCLOSED | [I] A2-006 (Low) |
| Inventory total ($M) | 3,212.1 | 3,282.6 | 3,437.0 | 3,648.5 | 4,090.4 | [F] A2-007..010 |
| - raw materials | 1,491.8 | 1,568.7 | 1,648.4 | 1,849.7 | 2,126.9 | |
| - WIP | 833.9 | 836.2 | 929.6 | 937.7 | 1,076.9 | |
| - finished goods | 285.7 | 252.2 | 256.5 | 238.4 | 247.5 | |
| - customer service parts | 600.8 | 625.5 | 602.5 | 622.7 | 639.0 | |
| Contract liabilities ($M) | 1,713.7 | 1,727.9 | 1,448.9 | 1,775.1 | 1,707.8 | [F] A2-012..016 |
| - of which due <12 months | n/a | 84.3% | 82.6% | 86.6% | 86.5% | [I] A2-018 |
| - deferred system revenue | 816.8 | 858.1 | 620.8 | 932.9 | 843.0 | [F] A2-017 |
| Customer deposits (cur.+non-cur.) | 643.2 | 370.6 | 420.9 | 433.9 | 507.8 | [F] A2-019..021 |
| AR net ($M) | 2,263.9 | 2,073.6 | 2,304.5 | 2,889.2 | 3,072.1 | [F] A2-022, 024, 025 |
| Long-term AR ($M) | 0 | 0 | 0 | 180.7 | 266.8 | [F] A2-023 |
| DSO (days, trade AR) | | 57.9 | 60.7 | 71.9 | 68.3 | [I] A2-027 |
| Purchase commitments ($B) | n/a | 2.75 | 4.83 | 5.97 | 8.87 | [F] A2-029..032 |

- Backlog is "primarily consisting of sales orders where written customer requests have been received" [F] A2-002. It is disclosed only annually, in the 10-K. The FY26 10-K attributes the rise to AI-infrastructure demand. Unlike the FY25 10-K (71-76% within 12 months [F] A2-003), it gives **no share due within 12 months**: NOT DISCLOSED (read: 10-K FY26 Item 1 Backlog).
- KLA's 10-Q "transaction price not yet recognized" table equals contract liabilities only ("which equals our contract liabilities") [F] A2-013. It is not a full RPO or backlog figure, so the 10-Qs give no quarterly backlog: NOT DISCLOSED (read: 10-Q Q2 FY26, Q3 FY26, Q1 FY27 Note 2).
- Orders, bookings and book-to-bill: NOT DISCLOSED (read: Q2 FY26-Q1 FY27 letters, slides, releases, 10-Qs). The FY26 implied orders of ~$18.3B and book-to-bill of ~1.35 = (revenue + Δbacklog) / revenue [I] A2-006 (Low: cancellations, FX and backlog scope are unknown).
- Inventory signal: since Jun 2025 total inventory is up 27%, raw materials up 43% and WIP up 29%, while finished goods are down 13%. The raw-material share rose from 47.8% to 52.0% [I] A2-011. This pattern means building ahead of shipments, not unsold product (Medium). KLA says it raised purchase commitments "in part to secure the supply of key components" [F] A2-033. In Q2 FY26 it said lead times were rising on supply constraints [C] A2-005.
- Purchase commitments rose 3.2x in three quarters to $8.87B, equal to 1.59x LTM COGS [I] A2-034.
- Receivables: DSO rose from ~58 to ~68-72 days, and a long-term AR line appeared in Jun 2026 ($267M at Sep 2026) [F] A2-023. Factoring was $515M in FY26 vs $231M in FY25, but only $32M in Q1 FY27 [F] A2-028. Payment terms are 70-90% within 30-60 days of shipment [F] A2-026. Lower factoring in Q1 FY27 partly explains the DSO level; when factoring is high, reported DSO understates the true figure (Medium).

### Prior-claim check (research/prior/text/kla_metrology_audit.md, lines 21-68 and the KLA handoff row)

| Prior claim | Verdict | Correct value / comment | Evidence |
|---|---|---|---|
| Backlog $7.86B (Jun 30, 2025) to $12.57B (Jun 30, 2026) | CONFIRMED (amounts); CORRECTED (cause) | Amounts are right. The 10-K attributes the rise to "strong demand driven by the AI infrastructure buildout"; it does not cite optical supply bottlenecks as the prior file implies | [F] A2-001 |
| Services $3.1B FY26; $850M Q1 FY27 +14% YoY | CONFIRMED | FY26 $3,125.9M; Q1 FY27 $850.5M, +14.2% | [F] A1-046, A1-057; [I] A1-061 |
| >80% of services on >3-yr (fixed) subscription contracts; <20% T&M | CORRECTED | >80% of revenue from multi-year subscription contracts [C]; the written slide says "~3-year average contract length" (spoken: "more than three years"). "Fixed" is not KLA's word. The slide says 95% of services revenue is recurring including T&M, and gives no "<20% T&M" figure | [C] A1-062..064 |
| 95% contract renewal | CONFIRMED | 95% contract renewal rate (Investor Day); >95% in Nov 2025 update | [C] A1-063, A1-065 |
| Services CAGR target raised to 13-15% (Mar 2026) | CONFIRMED | | [C] A1-066 |
| Q1 FY27 revenue $4.14B, non-GAAP OM 46.1%, GM 61.9% / 62.7% | CONFIRMED | 4,136.0; 46.1% (recomputed 46.05%); GAAP GM 61.9%, NG 62.7% | [F] A1-001, A1-006, A1-017, A1-018 |
| Q1 FY27 +28.9% YoY | CONFIRMED | +28.9% | [I] A1-005 |
| LTM $14.51B | CONFIRMED | $14,505.8M (+15.8% YoY) | [I] A1-025 |
| LTM GM 61.5% / 62.5% | CONFIRMED | 61.47% / 62.47% | [I] A1-026 |
| Q1 FY27 FCF $1.34B (OCF $1.53B - capex $195M) | CONFIRMED | 1,530.9 - 194.8 = 1,336.2 | [F] A1-027, A1-028 |
| FY26 revenue $13.58B | CONFIRMED | 13,579.5 | [F] A1-002 |
| Q2 FY27 guidance $4.70B ± $200M | CONFIRMED | $4.7B ± $200M; NG GM 62.5% ± 1% | [C] A1-075 |
| Services 20.6% of Q1 FY27 revenue; FY26 23.0% | CONFIRMED | 20.6%; 23.0% | [I] A1-061 |
| Recurring ~16.5%-18.4% of total revenue | NOT VERIFIABLE as stated | >80% x FY26 services = ≥18.4% of FY26 revenue (illustrative lower bound only); KLA gives no recurring-revenue % of total | a12_results.py output |
| CY25: $9.0B Semi PC + $3.0B services / $12.74B; "94.2% Semi PC + Services; ~5.8% PCB/Comp" | CORRECTED | CY25 total $12,745M is right. Semi PC systems (WI+Patterning+Other) $8,971M + services $2,903M = 93.2%. PCB & Component segment = 5.2% (systems only 3.0%). Specialty Semi Process (4.4%) is missing from the prior split | Q2 FY26 slides p6-7; a12_results.py |
| Total AP revenue ~$950M CY25; AP process-control systems $1.1B+ in CY26 (+70%+) | CORRECTED (wording) | $950M is "total systems revenue" [C]. The CY26 figure is "approximately $1.1 billion" (not "$1.1B+") on a ~$635M process-control base, >70% YoY | [C] A1-069..071 |
| Gen4/Gen5 lead times >12 months; optical bottlenecks constrained H1 CY26 | NOT VERIFIABLE (in A1/A2 docs) | Q2 FY26 letter: lead times "increasing due to supply constraints", with no months stated | [C] A2-005 |

### Premise issues
- The prior file implies the 10-K ties the backlog rise to optical supply bottlenecks. The 10-K cites AI-driven demand (above).
- The prior file treats "$1.1B+" AP process control and "$950M total AP" as one series. They are different definitions; the CY25 base for the $1.1B is ~$635M.
- The prior handoff row's "94.2% / ~5.8%" CY25 mix does not reconcile with KLA's CY25 table (see above).
- "Order backlog" in the 10-Q intangibles note (Note 6) is an acquired-intangible category, not a backlog disclosure. Do not read it as one.
- Pre-split vs post-split: Q2 and Q3 FY26 per-share figures in their own releases (e.g. NG EPS $8.85, $9.40) are pre-split. The Q4 FY26 release restates them post-split ($0.94 for Q3 FY26).

### Gaps (for gaps.md)
- Quarterly backlog: NOT DISCLOSED (read: 10-Q Q2 FY26, Q3 FY26, Q1 FY27; letters and slides Q2 FY26-Q1 FY27).
- Backlog share due within 12 months at Jun 30, 2026: NOT DISCLOSED (read: 10-K FY26 Item 1 Backlog).
- Orders / bookings / book-to-bill: NOT DISCLOSED (read: letters, slides, releases, 10-Qs Q2 FY26-Q1 FY27).
- DRAM vs NAND split of Q1 FY27 actual memory revenue: NOT DISCLOSED (read: Q1 FY27 letter p4, slides p5).
- HBM or AI share of revenue: NOT DISCLOSED (read: Q1 FY27 letter, slides, 10-Q; Q4 FY26 letter).
- Finer product split (metrology vs reticle inspection, e-beam): NOT DISCLOSED (read: 10-Q Q1 FY27 segment note; letters).
- Amounts of the Q3 FY26 reserve/prototype opex items and the supply-investment mark-to-market gain: NOT DISCLOSED (read: Q3 FY26 letter p5; Q3 FY26 release).
- Services contract share by term beyond ">80%", and services RPO: NOT DISCLOSED (read: Investor Day slides p104-113; 10-Q Q1 FY27 Note 2).

## Part A3, A6, Q5: guidance record, cycle, supply limits

Fiscal year ends June 30. Q1 FY27 = Jul-Sep 2026 (latest reported). Per-share figures: pre-split up to and including Q3 FY26 results; post-split from Q4 FY26 results onward (10-for-1, effective after the Nasdaq close on 2026-06-11) [F] A3-027.
Calc scripts: `research/out/kla/calc/a3_guidance_record.py`, `a6_cycle_drawdowns.py`, `q5_supply_calc.py` (run with `python3 -I`).

### Premise issues
- BRIEF says there is no Q3 FY25 shareholder letter. One is saved: `research/sources/kla/2025-04-30_kla_shareholder-letter-Q3FY25.pdf` (16 pp). I used it [F] A3-005.
- The Q3 FY25 earnings-release text extraction is garbled (font encoding). I took the exact Q3 FY25 revenue ($3,063,029K) from the comparative column of the Q3 FY26 release and from the Q3 FY25 letter.
- Prior file (kla_metrology_audit.md, line 33) tests the 2022 Investor Day **CY2026** target against **FY26** revenue ($13.58B, Jul 2025-Jun 2026). That mixes the fiscal and calendar years. CY2026 ends Dec 2026 and is not yet reported.
- Prior file cites the FY26 10-K for "optical component bottlenecks" and "Gen4/Gen5 lead times past 12 months". The 10-K names neither optics nor Gen4/Gen5. Those statements come from the earnings call (secondary) and the Investor Day.
- The Q2 FY26 Motley Fool transcript reads "2026 revenue will grow mid-single digits compared to 2025". The letter says H1 CY26 vs H2 CY25 [F] A3-033. I treat this as a transcription error. The Q3 FY26 transcript says "first half of 2016" where it means 2026 [S] Q5-026.
- The Q3 FY25 letter calls 63.0% non-GAAP GM "about 50 basis points higher than the midpoint of guidance". The guided midpoint was 62% (Q2 FY25 letter p.11; slides p.12), so 63.0% is 100 bps above it, at the top of the range. This is an internal inconsistency in KLA's letter. I classified it as in-line [I] A3-006.

### A3 Guidance record

Rule (stated once and used for every metric): result **above the top** of the guided range = BEAT; **inside or equal to an end** = IN-LINE; **below the bottom** = MISS. Guidance is taken from the prior quarter's shareholder letter. EPS guidance given before the split (Q4 FY26, issued 2026-04-29) is divided by 10.

| Quarter (calendar) | Revenue guide → actual ($M) | Non-GAAP GM guide → actual | Non-GAAP EPS guide → actual | GAAP EPS guide → actual | Evidence |
|---|---|---|---|---|---|
| Q2 FY25 (Oct-Dec 2024) | 2,950±150 → 3,076.9 IN-LINE | 61.5±1 → 61.7 IN | 7.75±0.60 → 8.20 IN | 7.45±0.60 → **6.16 MISS** | [F] A3-001/002, [I] A3-003 |
| Q3 FY25 (Jan-Mar 2025) | 3,000±150 → 3,063.0 IN | 62±1 → 63.0 IN (top) | 8.05±0.60 → 8.41 IN | 7.77±0.60 → 8.16 IN | [F] A3-004/005, [I] A3-006 |
| Q4 FY25 (Apr-Jun 2025) | 3,075±150 → 3,174.7 IN | 63±1 → 63.2 IN | 8.53±0.78 → **9.38 BEAT** | 8.28±0.78 → 9.06 IN (=top) | [F] A3-007/008, [I] A3-009 |
| Q1 FY26 (Jul-Sep 2025) | 3,150±150 → 3,209.7 IN | 62±1 → 62.5 IN | 8.53±0.77 → 8.81 IN | 8.28±0.77 → 8.47 IN | [F] A3-010/011, [I] A3-012 |
| Q2 FY26 (Oct-Dec 2025) | 3,225±150 → 3,297.1 IN | 62±1 → 62.6 IN | 8.70±0.78 → 8.85 IN | 8.46±0.78 → 8.68 IN | [F] A3-013/014, [I] A3-015 |
| Q3 FY26 (Jan-Mar 2026) | 3,350±150 → 3,415.1 IN | 61.75±1 → 62.2 IN | 9.08±0.78 → 9.40 IN | 8.85±0.78 → 9.12 IN | [F] A3-016/017, [I] A3-018 |
| Q4 FY26 (Apr-Jun 2026) | 3,575±200 → 3,657.6 IN | 61.75±1 → 62.4 IN | 0.987±0.10* → 1.05 IN | 0.966±0.10* → 1.04 IN | [F] A3-019/020, [I] A3-021 |
| Q1 FY27 (Jul-Sep 2026) | 4,000±200 → 4,136.0 IN | 62.5±1 → 62.7 IN | 1.16±0.10 → 1.22 IN | 1.14±0.10 → 1.18 IN | [F] A3-022/023, [I] A3-024 |
| **Q2 FY27 (Oct-Dec 2026), current** | 4,700±200 | 62.5±1 | 1.44±0.11 | 1.41±0.11 | [F] A3-026 |

\* Pre-split guidance of $9.87±$1.00 (non-GAAP) and $9.66±$1.00 (GAAP), divided by 10.

**Count over 8 quarters** [I] A3-025:
- Revenue: 0 beat, 8 in-line, 0 miss. Revenue came in above the guided midpoint every quarter, by +1.9% to +4.3%.
- Non-GAAP GM: 0 beat, 8 in-line, 0 miss.
- Non-GAAP EPS: 1 beat (Q4 FY25), 7 in-line, 0 miss.
- GAAP EPS: 0 beat, 7 in-line, 1 miss (Q2 FY25).

One-off items management named:
- Q2 FY25 GAAP EPS of $6.16 included a $239.1M goodwill and intangible impairment ($1.76/share) [F] A3-028. Without it, GAAP EPS was $7.92, inside the range (6.85-8.05) [I] A3-003. The impairment was not in the guidance.
- The Q4 FY25 non-GAAP EPS beat came from the tax rate: 9.9% actual vs 13.5% guided. At the guided rate, EPS would have been $9.00, inside the range [F] A3-029. Q3 FY25 at the guided rate: $8.55, also in-line.

**Guidance maintained late in a period and then missed: none found.** KLA does not update quarterly guidance within the quarter. Its calendar-year views were raised, never cut, over 2025-2026. Examples: CY25 GM went from 62%±0.5 to 62.5%±0.5; CY26 wafer-equipment (WFE) outlook went from low $120B (core) to >$140B, then low-$150B, then mid-$150B [F] A3-030, A3-033 to A3-035.

#### Calendar-year and long-range statements (last 3) and outcomes
| Statement | Made | Outcome | Evidence |
|---|---|---|---|
| CY2025: WFE up mid-single digits from high-$90B; KLA to outperform; non-GAAP GM ~62%±50bps (raised to 62.5%±50bps in Apr 2025) | 2025-01-30 | KLA revenue +17% to $12.745B, against KLA's own estimate of low-double-digit industry growth. GM 62.8%, inside the raised range. **Met/beat** | [F] A3-030, A3-031; [I] A3-032 |
| CY2026: H1 CY26 up mid-single digits vs H2 CY25 (Jan 2026); KLA growth "high teen" YoY (Apr 2026); H2/H1 ~20% (Jul), then ~25% (Oct); GM ~62%±50bps | 2026-01-29 to 2026-10-28 | H1 CY26 came in +8.7% vs H2 CY25 (above "mid-single"). Using the Q2 FY27 midpoint, CY26 is about $15.91B (+24.8%), above "high teen", and H2/H1 is +24.9%. CY26 GM about 62.5%, at the top of the range. **Exceeded so far; not final** | [F] A3-033 to A3-035; [I] A3-036 |
| 2022 Investor Day CY2026 model: revenue $14B±$0.5B; non-GAAP GM ~63%; OM 41-43%; EPS $38±$1.50 (pre-split = $3.80±$0.15) | 2022-06-16 | Implied CY26: revenue about $15.91B (above $14.5B top), non-GAAP OM about 45.2%, non-GAAP EPS about $4.65 post-split ($46.5 pre-split): all **beat**. Non-GAAP GM about 62.5%, **below** the ~63% target; management named DRAM cost and tariffs | [F] A3-037, A3-041, [C] A3-038, [I] A3-039 |
| Pending: 2030 model of $26B±$2.5B revenue, OM 45-47%, EPS $84±$8 (pre-split) | 2026-03-12 | Due 2031 | [F] A3-040 |

### A6 Cycle: last two downturns

**Why these two.** Test used: reported quarterly revenue falls at least 10% from a quarterly peak and stays below that peak for at least 3 quarters.
- **2022-23** passes.
- **2018-19** fails on reported revenue: Q2 FY19 to Q3 FY19 was only −2.0%, because Orbotech (consolidated from 2019-02-20) added $161.3M [F] A6-021. Excluding Orbotech, Q3 FY19 was −16.4%, but that can only be computed for one quarter [I] A6-025.
- **2020** (COVID) was −5.7%.
- The next qualifying episode is the **FY2013-FY2016 (CY2012-15)** trough. Revenue stayed below the Jun-2012 peak until Apr-Jun 2016 [I] A6-023.
- 2008-09 was deeper (−59.4% revenue; GAAP OM 25.6% → −12.4%) but older [I] A6-025.

| | Downturn 1: CY2022-23 | Downturn 2: CY2012-15 |
|---|---|---|
| Revenue peak | Q2 FY23 (Oct-Dec 2022) $2,983.9M [F] A6-001 | Q4 FY12 (Apr-Jun 2012) $892.5M [F] A6-014 |
| Revenue trough | Q4 FY23 (Apr-Jun 2023) $2,355.1M, **−21.1%**. Second dip in Q3 FY24 (Jan-Mar 2024) at $2,359.8M | First trough Q2 FY13 (Oct-Dec 2012) $673.0M, −24.6%. Deepest Q1 FY16 (Jul-Sep 2015) $642.6M, **−28.0%** |
| Quarters below peak | 7 (peak regained in Q2 FY25) | 15 (peak regained in Q4 FY16) |
| GAAP OM at peak → low | 40.2% → 29.5% in Q2 FY24, **−10.7 pts**, including a $219.0M impairment. Excluding impairments: 34.2% in Q3 FY24, **−6.0 pts** | 35.7% → 17.0% in Q1 FY15 (Jul-Sep 2014), **−18.7 pts**. At the Sep-2015 revenue low: 25.0% (26.1% excluding the $7.1M restructuring) |
| Non-GAAP OM at peak → low | 42.4% → 36.8% in Q3 FY24, **−5.7 pts**. From the margin peak in Q1 FY23 (44.1%): −7.3 pts | NOT RETRIEVED (tried: no KLA-Tencor 2012-15 earnings releases fetched) |
| One-offs named by management | Impairments of $219.0M (Q2 FY24) and $70.5M (Q3 FY24); restructuring of $19.1M (Q3 FY23) and $8.1M (Q4 FY23) [F] A6-005, A6-006, A6-009 | Restructuring of $22.4M (Q4 FY15) and $7.1M (Q1 FY16) [F] A6-019. One-offs in Q1 FY15: not identified |
| Evidence | [I] A6-010, A6-011, A6-012 | [I] A6-023, A6-024 |

Method notes:
- KLA's FY23-FY24 income statement has no operating-income line. I used GAAP OI = revenue − cost of revenues − R&D − SG&A − impairment.
- Non-GAAP OI = GAAP OI + the pre-tax adjustments booked in those lines, from the release tables [F] A6-008. KLA did not publish this figure, so these numbers are my derivation (Medium confidence).
- 2012-15 operating income is as reported in the 10-K quarterly notes and the 10-Q tables [F] A6-014 to A6-018.

### Q5 Supply limits (statements since Jan 2025)

**Components named:**
- Optics (glass and "volume optics"): the longest-lead item, named by the CFO on the Q2 FY26 call [S] Q5-024 and the Q1 FY27 call [S] Q5-029, and by the CEO [S] Q5-025.
- Investor Day slide 153 [C] Q5-018 groups the parts:
  - low-volume, sole-sourced complex parts: optics, sensors, lasers;
  - high-volume, mostly sole-sourced parts: volume optics, stages, motion control;
  - Tier 2-4: semiconductors, electronic components.
- DRAM chips for the image-processing computers shipped with the tools. These are a **cost** problem, not a shipment limit: KLA says it "secured the required supply" [C] Q5-012. Filings: suppliers discontinued certain DRAM chips and prices rose [F] Q5-004, Q5-005.
- Rare-earth elements: a risk factor only, with no stated impact [F] Q5-008.

**Lead times (months):**
- Historically about 6 months.
- 7-9 months in Oct 2025 [S] Q5-022.
- "Increasing due to supply constraints, limiting first-half growth" in Jan 2026 [C] Q5-010.
- Material-to-ship time fence of almost 60 weeks in Mar 2026 [C] Q5-019.
- About 12 months on average in Oct 2026, with Gen4/Gen5 longer [S] Q5-027, Q5-028.
- Lead-time months: NOT DISCLOSED (read: FY26 10-K Item 1 Backlog and Item 1A; Q1 FY27 10-Q; letters Q2 FY26 to Q1 FY27). They appear only in the secondary transcripts.

**Capacity actions:**
- About $250M+ invested in supplier capacity over roughly 2 years; suppliers get about 8 quarters of visibility; KLA does not cancel orders [C] Q5-018, Q5-021.
- Q1 FY27 letter: KLA worked with strategic partners over the past year to raise their capacity [C] Q5-015.
- "We are adding capacity" [C] Q5-014.
- CapEx to trend up to $600-800M a year [S] Q5-032.
- 10-K: KLA gives financial support to vendors to add capacity [F] Q5-009.

**Effect on backlog conversion and revenue timing:**
- H1 CY26 capacity was set "inside a lead time" before demand accelerated [C] Q5-020, and was "virtually sold out" [S] Q5-023.
- H2 CY26 is about 20-25% above H1 as long-lead capacity comes online [C] Q5-013, Q5-016.
- Backlog rose from $7.86B to $12.57B in FY26 (+59.9%). The 10-K attributes this to AI-driven demand and lists supply-chain constraints among the timing variables [F] Q5-002, [I] Q5-003.
- Purchase commitments rose from $5.97B to $8.87B in Q1 FY27 (+48.6%) [F] Q5-006, [I] Q5-007.
- Revenue lost or deferred because of supply: NOT DISCLOSED (read: Q2 FY26 to Q1 FY27 letters; FY26 10-K MD&A). The CFO said "We don't really look at what we could have done" [I] Q5-034.
- FY26 backlog share to convert within 12 months: NOT DISCLOSED (read: FY26 10-K Item 1 Backlog). The FY25 10-K gave 71-76% [F] Q5-001.

**DRAM cost on gross margin:**
- 75-100 bps hit to CY26 GM (Jan 2026) [F] Q5-011.
- About 100 bps "over the next several quarters" (Apr 2026) [C] Q5-012.
- FY26 10-K: adverse GM impact "in fiscal 2027" (Jul 2026-Jun 2027) [F] Q5-005.
- Oct 2026: "persistently high" memory costs; system redesign under way to use less memory [C] Q5-017.

### Prior-claim check (kla_metrology_audit.md lines 21-68 and line ~1033, in scope)
| Prior claim | Verdict | Evidence |
|---|---|---|
| 2022 Investor Day CY2026 target $14.0B ± $500M, 41-43% OM: "MET" | **CORRECTED.** CY2026 is not complete, and the prior used FY26 revenue. On a CY26 implied basis (Q2 FY27 guidance midpoint), revenue of about $15.9B **exceeds** the top of the range and OM of about 45% exceeds 41-43%. The same target model's ~63% GM is **not met** (about 62.5%). EPS target $38±1.50 pre-split, implied about $46.5 | A3-037, A3-039, A3-041 |
| Optical component bottlenecks constrained H1 CY26 shipments | **CONFIRMED** (company statements [C] and calls [S]; not in the 10-K, which the prior cited) | Q5-010, Q5-020, Q5-024, Q5-030 |
| Gen4/Gen5 lead times extended past 12 months | **CONFIRMED [S] only** (Q1 FY27 call: average about 12 months, Gen4/Gen5 "longer"); not in KLA documents | Q5-027, Q5-028 |
| Backlog $7.86B (Jun 2025) → $12.57B (Jun 2026) lifted by optical bottlenecks | Figures **CONFIRMED**; cause **CORRECTED**. The 10-K attributes the increase to "strong demand driven by the AI infrastructure buildout" | Q5-002 |
| Management planned flat CY26 capacity | **CORRECTED.** No capacity plan statement found. Oct 2025 guidance was H1 CY26 revenue "roughly flat to modestly up" vs H2 CY25. CFO (Oct 2026, [S]): they had expected 2026 "pretty flat". H1 capacity decisions were made inside the lead time [C] | Q5-020, Q5-031 |
| DRAM memory pricing pressuring image-processing compute costs into H2 CY2027 | **CORRECTED.** Filings say a GM impact "in fiscal 2027" (to Jun 2027 = H1 CY2027). Letters say pricing persists "through at least calendar 2026". No H2 CY2027 statement found | Q5-005, Q5-011, Q5-012, Q5-017 |
| Current KLA tool delivery lead time ~12 months average | **CONFIRMED [S]** (Q1 FY27 call, 2026-10-28) | Q5-027 |
| Q2 FY27 guidance $4.70B ± $200M; Q1 FY27 non-GAAP OM 46.1% | **CONFIRMED** | A3-026, A3-041 |

### Gaps
- Q4 FY26 earnings-call transcript (2026-07-28): NOT RETRIEVED (tried: fool.com URL patterns for 07/28 and 07/29 returned 404; GuruFocus is paywalled; not worked around).
- Non-GAAP operating margin for the 2012-15 downturn: NOT RETRIEVED (tried: no KLA-Tencor FY12-FY16 earnings releases fetched).
- Lead times in months: NOT DISCLOSED (read: FY26 10-K Item 1 Backlog and Item 1A; Q1 FY27 10-Q Item 1A; letters Q2 FY26 to Q1 FY27). Secondary sources only.
- Revenue deferred by supply constraints: NOT DISCLOSED (read: letters Q2 FY26 to Q1 FY27; FY26 10-K MD&A).
- 12-month conversion share of the FY26 backlog: NOT DISCLOSED (read: FY26 10-K Item 1 Backlog).
- Q4 FY19 revenue excluding Orbotech: NOT DISCLOSED (read: FY19 10-K Note 20; Q3 FY19 10-Q revenue-by-product table).
- One-off items in Q1 FY15 (Jul-Sep 2014, the OM low): NOT RETRIEVED (tried: the Q1 FY15 10-Q was not fetched; the FY15 10-K quarterly note has no operating detail).
- Q3 FY25 earnings release: text extraction unreadable (font encoding). Values taken from the Q3 FY25 letter and the Q3 FY26 release comparative.

## Part A4, A5: concentration, China, export rules, balance sheet, capital

Fiscal year ends June 30. Q1 FY27 = Jul-Sep 2026 (latest; 10-Q filed 2026-10-29). $ in thousands unless stated. Evidence ids refer to `parts/A4.csv` and `parts/A5.csv`. Arithmetic: `calc/a4_region_parse.py`, `calc/a4_segment_parse.py`, `calc/a4_china_share.py` (output `calc/a4_china_share_output.txt`), `calc/a5_capital.py` (output `calc/a5_capital_output.txt`).

No margin or profit figures are computed in A4/A5, so no one-off adjustment table is needed. The impairments listed under A5 are the one-off items management named for FY24 and FY25 (handled by A1 for margins).

### A4.1 Customers above 10%

| Period | >10% customers (revenue) | Named? | Evidence |
|---|---|---|---|
| FY26 (Jul 2025-Jun 2026) | one customer, ~19% | Yes: TSMC (Item 1 table) | [F] A4-046, A4-047 |
| FY25 (Jul 2024-Jun 2025) | one customer, ~19% | Yes: TSMC | [F] A4-046, A4-047 |
| FY24 (Jul 2023-Jun 2024) | one customer, ~13% | Yes: TSMC | [F] A4-048, A4-050 |
| FY23 / FY22 (context) | two customers 18% and 15% / 20% and 12% | Yes: TSMC and Samsung | [F] A4-049, A4-050 |
| Q1 FY26 (Jul-Sep 2025) | three customers 15%, 11%, 10% | No | [F] A4-052 |
| Q2 FY26 (Oct-Dec 2025) | two customers 17%, 11% | No | [F] A4-053 |
| Q3 FY26 (Jan-Mar 2026) | two customers 19%, 11% | No | [F] A4-054 |
| Q1 FY27 (Jul-Sep 2026) | two customers 21%, 13% | No | [F] A4-051 |

- Annual 10-Ks name the >10% customers; quarterly 10-Qs give percentages only, never names. [F] A4-046, A4-051
- Receivables: TSMC >10% of AR at Jun 30, 2024 (TSMC and Samsung at Jun 30, 2023) [F] A4-056; two customers at Jun 30, 2025 and Dec 31, 2025; three at Sep 30, 2025 and Mar 31, 2026 (unnamed) [F] A4-055.
- AR concentration at Jun 30, 2026 and Sep 30, 2026: NOT DISCLOSED (read: FY26 10-K Note 1 Concentration of Credit Risk and Note 17; Q1 FY27 10-Q Note 16).

### A4.2 Revenue by region, last 4 quarters (share of total, %)

| Region | Q2 FY26 (Oct-Dec 2025) | Q3 FY26 (Jan-Mar 2026) | Q4 FY26 (Apr-Jun 2026) | Q1 FY27 (Jul-Sep 2026) | LTM |
|---|---|---|---|---|---|
| China | 30.2 | 24.3 | 26.2 | 34.5 | 29.0 |
| Taiwan | 25.6 | 25.4 | 31.1 | 24.7 | 26.7 |
| North America | 12.0 | 12.0 | 17.9 | 14.9 | 14.3 |
| Korea | 14.5 | 19.9 | 10.2 | 12.0 | 14.0 |
| Japan | 6.9 | 5.3 | 5.8 | 3.9 | 5.4 |
| Rest of Asia | 5.9 | 5.8 | 4.3 | 5.3 | 5.3 |
| Europe and Israel | 4.9 | 7.2 | 4.6 | 4.7 | 5.3 |
| Total revenue ($k) | 3,297,146 | 3,415,078 | 3,657,556 | 4,136,015 | 14,505,795 |

[I] A4-036 to A4-040, High confidence; inputs are the 10-Q/10-K geography notes. Q4 FY26 printed directly in the Q1 FY27 10-Q QoQ table [F] A4-014.

### A4.3 China share by quarter, Q1 FY24 to Q1 FY27 (13 quarters)

| Quarter | Calendar | China ($k) | Total ($k) | China % | QoQ % | YoY % | Source |
|---|---|---|---|---|---|---|---|
| Q1 FY24 | Jul-Sep 2023 | 1,025,944 | 2,396,956 | 42.8 | - | - | [F] A4-001 |
| Q2 FY24 | Oct-Dec 2023 | 1,027,780 | 2,486,726 | 41.3 | +0.2 | - | [F] A4-002 |
| Q3 FY24 | Jan-Mar 2024 | 996,885 | 2,359,830 | 42.2 | -3.0 | - | [F] A4-003 |
| Q4 FY24 | Apr-Jun 2024 | 1,146,118 | 2,568,735 | 44.6 | +15.0 | - | [I] derived FY24 10-K minus 9M |
| Q1 FY25 | Jul-Sep 2024 | 1,198,305 | 2,841,541 | 42.2 | +4.6 | +16.8 | [F] A4-004 |
| Q2 FY25 | Oct-Dec 2024 | 1,092,525 | 3,076,851 | 35.5 | -8.8 | +6.3 | [F] A4-005 |
| Q3 FY25 | Jan-Mar 2025 | 792,884 | 3,063,029 | 25.9 | -27.4 | -20.5 | [F] A4-006 |
| Q4 FY25 | Apr-Jun 2025 | 958,854 | 3,174,741 | 30.2 | +20.9 | -16.3 | [I] derived FY25 10-K minus 9M |
| Q1 FY26 | Jul-Sep 2025 | 1,267,156 | 3,209,696 | 39.5 | +32.2 | +5.7 | [F] A4-007 |
| Q2 FY26 | Oct-Dec 2025 | 994,891 | 3,297,146 | 30.2 | -21.5 | -8.9 | [F] A4-008 |
| Q3 FY26 | Jan-Mar 2026 | 829,583 | 3,415,078 | 24.3 | -16.6 | +4.6 | [F] A4-009 |
| Q4 FY26 | Apr-Jun 2026 | 956,728 | 3,657,556 | 26.2 | +15.3 | -0.2 | [F] A4-014 |
| Q1 FY27 | Jul-Sep 2026 | 1,425,744 | 4,136,015 | 34.5 | +49.0 | +12.5 | [F] A4-010 |

Shares and growth rates: [I] A4-016 to A4-028, High (script `a4_china_share.py`). KLA itself prints +49% QoQ and +13% YoY for Q1 FY27 [F] A4-015.

Fiscal years: FY24 42.8%, FY25 33.3%, FY26 29.8% [F] A4-011 to A4-013. Calendar years: CY2024 40.9%, CY2025 31.5%, Jan-Sep 2026 28.7% [I] A4-029 to A4-031. Pre-surge baseline: FY21 26.5%, FY22 28.9%, FY23 27.3% [I] A4-034.

**China share of Semi Process Control systems.** NOT DISCLOSED (read: shareholder letters and earnings slides Q4 FY24-Q1 FY27; Investor Day 2026 slides and transcripts). KLA gives only a total-company China share. The CFO said the total includes non-semi-PC business in China (PCB, component inspection) that "skews the numbers a bit up", without quantifying it [S] A4-079. So the semi PC systems share is probably slightly below the total share, but the gap is unknown.

### A4.4 Prior-period figures changed between filings

- Regional revenue: no unexplained changes. All 7 regions plus the total for Q1-Q3 FY24, Q1-Q3 FY25 and Q1 FY26 are identical as first reported and as the prior-year column of the next 10-Q. FY23, FY24 and FY25 annual regional figures are identical across later 10-Ks. [I] A4-042, High.
- Segment revenue: no changes in amounts. The segment was renamed from "PCB, Display and Component Inspection" (through Q3 FY24) to "PCB and Component Inspection" (FY24 10-K onward). [I] A4-043.
- Presentation only: the Q4 FY24 letter shows China at 44%, but the figure derived from the 10-K is 44.6%. KLA rounded so the regions add to 100%. [I] A4-044, [F] A4-045. From Q1 FY26 the 10-Q prints region shares to one decimal place instead of whole percent. This is a format change only.

### A4.5 Export rules that bind KLA, and KLA's own estimate of each one's impact

| Rule (date) | What it restricts (as KLA or the FR text says) | KLA's own impact statement | Evidence |
|---|---|---|---|
| Oct 7, 2022 BIS IFR (87 FR 62186) | Licences needed for effectively all KLA products and services to China fabs making non-planar or <=16/14nm logic, >=128-layer NAND, or <=18nm half-pitch DRAM; limits on US-person support; limits on tools sold to China WFE makers | Preliminary **gross direct CY2023 impact of $500M-$900M** (based on backlog, before reallocation). By Aug 2023: "have not significantly impacted our operations to date" | [F] A4-057, A4-058, A4-059; FR text NOT RETRIEVED |
| Oct 17, 2023 update (SME IFR 88 FR 73424, published Oct 25, 2023; effective Nov 2023) | Revises the 2022 parameters, adds anti-circumvention measures, extends coverage to arms-embargoed countries | **No quantified impact**: "still evaluating these rules" | [F] A4-060, A4-061 |
| Dec 2, 2024 IFR (89 FR 96790) + Entity List additions; Jan 2025 follow-on rules | New SME controls, new foreign direct product (FDP) rules, HBM controls, more Entity List names, a revised advanced-DRAM definition | **~$500M ± $100M CY2025 revenue impact, ~70% systems** (first given early Dec 2024). **RPO cut by ~$430M** (about half due within 12 months). Services growth hit in Mar 2025 quarter | [F] A4-062, A4-063, A4-064, A4-066; [S] A4-065 |
| Sep 29, 2025 Affiliates Rule IFR (90 FR 47201) | Entity List / MEU restrictions extended to entities ≥50% owned by listed parties | **~$300-350M across the Dec 2025 quarter and CY2026**, described as "extended export controls" (KLA did not name the rule). CFO: the Dec 2025 quarter impact was "fairly immaterial" | [F] A4-067, A4-068; [S] A4-069 |
| Nov 10, 2025 suspension (FR 2025-19846), to Nov 9, 2026 | Affiliates Rule stayed | Jan 2026 CFO: China now expected **up** in CY2026, versus modestly down three months earlier; the affiliate business "feathered" back into the forecast; the recovered amount was "that ballpark" of $300-350M (no exact figure) | [F] A4-070, A4-071; [S] A4-072 |
| Nov 9, 2026 extension of the suspension to Jan 10, 2027 | Affiliates Rule still stayed | No KLA statement (falls after the Q1 FY27 10-Q). The Q1 FY27 10-Q has no new export risk factor | [S] A4-073; [F] A4-074 |
| 2026 SME-specific BIS rules | none found that KLA names | FY26 10-K and Q1 FY27 10-Q list no 2026 rule | [F] A4-074 |

- Calendar 2025 outcome against the Dec 2024 guidance: China revenue fell 9.5% in CY2025 [I] A4-032, against the "~20%" decline the CFO gave at UBS [S] A4-065. KLA did not publish a realised-impact figure for the $500M estimate: NOT DISCLOSED (read: Q2 FY25-Q4 FY26 letters and 10-Qs).
- The Affiliates Rule now returns on Jan 10, 2027 unless BIS extends the suspension again. This is a dated regulatory risk for the B3 catalysts list [S] A4-073.

### A4.6 "China revenue has normalised": evidence for and against

What KLA calls normal: a China share in the high-20s percent of revenue in CY2026 (letter [F] A4-041; CFO "27% to 29%" [S] A4-078), falling to the low-20s in 2027 [S] A4-078. The CFO attributed the decline partly to export controls and partly to "general normalization" [S] A4-075. China's growth is expected to be slower than WFE [S] A4-077.

For:
- CY2026 Jan-Sep China share is 28.7%, inside KLA's high-20s range [I] A4-031. If Q2 FY27 lands at a 25-29% China share, CY2026 comes out at 27.6-28.8% [I] A4-035.
- The pre-surge level (FY21-FY23) was 26.5-28.9%, so the current share matches history [I] A4-034.
- China revenue grew 6.4% in Jan-Sep 2026 against 18.6% total growth [I] A4-033. This is the slower growth that "normalisation" implies.

Against:
- Q1 FY27 China jumped +49% QoQ to 34.5% of revenue, driven by mature-node foundry/logic [F] A4-015. Quarterly swings of 24-40% persist [I] A4-016 to A4-028.
- In dollars, China revenue has not shrunk: FY26 was $4.05B, against $4.04B in FY25 and $4.20B in FY24 [F] A4-011 to A4-013. The share falls only because other regions grow.
- The FY26 share benefited from suspension of the Affiliates Rule. If the rule returns on Jan 10, 2027, KLA's own ~$300-350M estimate becomes relevant again [S] A4-072, A4-073.
- The stated 2027 level (low-20s) is below the CY2026 level, so KLA does not treat the current share as the floor [S] A4-078.

### A5.1 Balance sheet (Sep 30, 2026 unless stated)

| Item | Value | Evidence |
|---|---|---|
| Cash, equivalents and marketable securities | $4,741.2M (Jun 30, 2026: $4,902.4M; Mar 31: $4,957.9M; Dec 31, 2025: $5,207.5M; Sep 30, 2025: $4,683.6M) | [F] A5-001 to A5-005 |
| Senior notes principal | $5,950.0M; carrying value $5,723.3M | [F] A5-014 |
| Net debt (principal minus cash) | $1,208.8M (Q2 FY26 $742.5M, Q3 $992.1M, Q4 $1,047.6M) | [I] A5-028 |
| Revolver | $1.50B, Credit Agreement Jul 3, 2025, matures Jul 3, 2030 (+2 one-year extensions, +$500M accordion), undrawn | [F] A5-017 |
| Covenants | Max net leverage 3.25x (3.75x after a material acquisition); indenture limits on liens and sale-leaseback; 101% change-of-control put; in compliance | [F] A5-018, A5-019 |
| Commercial paper | NOT DISCLOSED (read: Q1 FY27 10-Q Note 7 and Liquidity; FY26 10-K Item 7 and Note 8). No programme mentioned | [I] A5-029 |
| Convertibles | None. All debt is fixed-rate senior unsecured notes | [I] A5-030 |
| Ratings | Moody's A2, S&P A-, Fitch A- | [F] A5-021 |
| Swaps | $2.00B of 2022 notes swapped fixed-to-floating (SOFR), FY26 | [F] A5-015 |
| Interest expense | Q2 FY26 $69.7M; Q3 FY26 $70.4M; Q4 FY26 $73.3M (derived); Q1 FY27 $67.9M; LTM $281.3M; FY26 $284.4M, FY25 $302.2M | [F] A5-022 to A5-025 range; [I] A5-026 |

Debt ladder (Q1 FY27 10-Q Note 7) [F] A5-006 to A5-013:

| Coupon | Maturity | Principal ($M) | Effective rate |
|---|---|---|---|
| 4.100% | Mar 15, 2029 | 800 | 4.159% |
| 4.650% | Jul 15, 2032 | 1,000 | 4.657% |
| 4.700% | Feb 1, 2034 | 500 | 4.777% |
| 5.650% | Nov 1, 2034 | 250 | 5.670% |
| 5.000% | Mar 15, 2049 | 400 | 5.047% |
| 3.300% | Mar 1, 2050 | 750 | 3.302% |
| 4.950% | Jul 15, 2052 | 1,450 | 5.023% |
| 5.250% | Jul 15, 2062 | 800 | 5.259% |
| **Total** | | **5,950** | weighted 4.668% effective / 4.629% coupon; 17.8 yrs [I] A5-027 |

There is no maturity before Mar 2029. The $750M note due Nov 1, 2024 was repaid [F] A5-020.

### A5.2 Buybacks, authorisation, dividend

| Quarter | Shares repurchased (post-split, k) | Cost ($M, trade date) | Evidence |
|---|---|---|---|
| Q1 FY26 (Jul-Sep 2025) | 6,230 (623 pre-split) | 564.4 | [F] A5-032 |
| Q2 FY26 (Oct-Dec 2025) | 4,600 (460 pre-split) | 537.6 | [F] A5-033 |
| Q3 FY26 (Jan-Mar 2026) | 4,400 (440 pre-split) | 631.9 | [F] A5-034 |
| Q4 FY26 (Apr-Jun 2026) | 3,011 (derived) | 570.1 (derived) | [I] A5-036 |
| Q1 FY27 (Jul-Sep 2026) | 4,914 | 942.9 (cash basis $935.8M) | [F] A5-031 |
| Last 4 quarters | 16,925 | 2,682.5 | [I] A5-037 |

- Authorisations: +$2B announced Sep 5, 2023 [F] (Q1 FY24 release, note in A5-039). +$5.00B in Q4 FY25, announced Apr 30, 2025 [F] A5-039, A5-041. +$7.00B in Q3 FY26 (Jan-Mar 2026), announced publicly with results on Apr 29, 2026 [F] A5-039, A5-040.
- Remaining authorisation: **$8.81B at Sep 30, 2026** [F] A5-038. Earlier: $9.74B (Jun 2026), $10.31B (Mar 2026), $3.94B (Dec 2025), $4.47B (Sep 2025), $5.03B (Jun 2025). The roll-forward reconciles within KLA's $10M rounding [I] A5-043.
- Dividend: $1.90/quarter pre-split from Apr 2025 [F] A5-041; $2.30/quarter pre-split from the May 2026 declaration [F] A5-040, which is $0.23 post-split; Q1 FY27 declared $0.230 [F] A5-042. Dividends paid in Q1 FY27: $305.1M.
- 10-for-1 split, effective Jun 11, 2026 (split-adjusted trading Jun 12). The Q1 FY27 10-Q and FY26 10-K show post-split, retroactively adjusted share counts. The Q1-Q3 FY26 10-Qs show pre-split counts, so multiply those by 10 to compare [F] A5-044. Shares outstanding: 1,302,962,435 (Oct 26, 2026), down 0.25% from the split-adjusted Apr 27, 2026 count [F] A5-045, [I] A5-046. All per-share figures above say whether they are pre- or post-split.

### A5.3 M&A (FY22 to FY27 YTD) and impairments since

| Date | Deal | Price | Evidence |
|---|---|---|---|
| Jul 1, 2021 (Q1 FY22) | Anchor Semiconductor | $81.7M (+ up to $35M contingent) | [F] A5-047 |
| Feb 28, 2022 (Q3 FY22) | ECI Technology | $431.5M cash ($266.4M goodwill) | [F] A5-048 |
| May 1, 2022 (Q4 FY22) | Unnamed private company | $8.6M | [F] A5-049 |
| Aug 9, 2022 (Q1 FY23) | Unnamed materials-supply company | $32.7M | [F] A5-050 |
| Aug 11, 2022 (Q1 FY23) | Sale of Orbograph | $110.0M consideration, $29.7M gain | [F] A5-050 |
| FY24-Q1 FY27 | No business acquisitions ($3.7M FY24 outflow = holdback payment) | - | [F] A5-050 note |

Impairments:
- Q2 FY24: $219.0M, PCB and Display ($192.6M goodwill + $26.4M intangibles) [F] A5-051.
- Q3 FY24: $70.5M Display goodwill after the March 2024 exit decision [F] A5-052.
- Q2 FY25: $239.1M, PCB ($230.4M goodwill + $8.7M intangibles) [F] A5-055.
- FY26 annual test (Dec 31, 2025): no impairment [F] A5-056.

Cumulative charges are $528.6M across three charges, all in the Orbotech-derived PCB and Display businesses (KLA does not tie them to the Orbotech deal by name in these filings). The Display exit followed a major Display customer's cancellation of a technology project, and a settlement was received in Q2 FY25 (amount NOT DISCLOSED) [F] A5-054.

### Prior-claim check (prior/text/kla_metrology_audit.md)

| Prior claim | Verdict | Evidence |
|---|---|---|
| "Q1 FY27 10-Q: China +49% QoQ / +13% YoY" | CONFIRMED. The exact share is 34.5% (the prior said "exact SEC % pending") | [F] A4-010, A4-015 |
| "Announced FPD manufacturing exit Mar 2024" | CONFIRMED (decision March 2024) | [F] A5-053 |
| "following customer project cancellation" | CONFIRMED (FY25 10-K) | [F] A5-054 |
| "ended manufacturing Dec 31, 2024" | CORRECTED: Dec 31, 2024 was the *announced target* for ending manufacturing of *most* Display products. No later filing confirms the actual completion date | [F] A5-053 |
| "$70.5M Q3 FY24 goodwill impairment" | CONFIRMED. The prior omits the related $219.0M (Q2 FY24) and $239.1M (Q2 FY25) PCB/Display impairments | [F] A5-051, A5-052, A5-055 |
| "Q1 FY27 10-Q accession 0000319201-26-000034 dated 2026-10-29" | CONFIRMED (ir.kla.com mirror URL; signature date October 29, 2026) | [F] A4-010 url |
| KLA handoff row "China %: Pending" | Now filled: Q1 FY27 34.5%; FY26 29.8%; LTM 29.0% | [I] A4-028, [F] A4-013 |
| KLA row "LTM $14.51B" (cross-check only, A1 scope) | Consistent: LTM regional total $14,505.8M | [I] A4-040 |

### Premise issues

- The prompt dates the 2023 update "Oct 17, 2023". That is the BIS announcement date. The SME rule was published in the Federal Register on Oct 25, 2023 (88 FR 73424) and took effect in November 2023 [F] A4-060.
- The prompt says KLA estimated "~$400-500M CY2025 impact" for the Dec 2024 rules. KLA's figure was ~$500M ± $100M, i.e. $400-600M, with ~70% in systems [F] A4-063.
- The prompt frames the "affiliates rule ~$300-350M" estimate as an FY26 figure. KLA framed it as the Dec 2025 quarter plus calendar 2026 (Oct 2025-Dec 2026), and attributed it to "extended export controls" without naming the Affiliates Rule [F] A4-068.
- The suspension of the Affiliates Rule did not simply end in Nov 2026. It was extended to Jan 10, 2027 [S] A4-073.
- The prompt expects a "China share of semi process control systems" figure. KLA does not publish one (NOT DISCLOSED above).
- Prior file: the FPD "ended manufacturing Dec 31, 2024" claim is corrected above.

### Gaps

- NOT RETRIEVED (tried: govinfo.gov PDF and HTML for FR 2022-21658, 502 errors): Oct 7, 2022 BIS IFR text. The date and scope are taken from 88 FR 73424 and KLA's filings.
- NOT RETRIEVED (tried: federalregister.gov, which returned a CAPTCHA page, now deleted; manifest row for `2025-11-12_bis-fr_affiliates-rule-suspension.html` points to a removed captcha page, use `2025-11-12_bis-fr_rule-affiliates-suspension-Nov2025.html`): the Nov 9, 2026 FR rule extending the suspension. Only a law-firm alert was saved [S].
- NOT RETRIEVED (tried: web search for a UBS Dec 4, 2024 transcript; Seeking Alpha is paywalled): KLA's own Dec 2024 statement. The ~$500M figure is [F] only via the Jan 2025 letter.
- NOT DISCLOSED (read: Q2 FY25-Q1 FY27 letters, 10-Qs, FY26 10-K): KLA's realised revenue loss against the $500M (CY2025) and $300-350M estimates.
- NOT DISCLOSED (read: letters/slides Q4 FY24-Q1 FY27, Investor Day 2026): China share of Semi Process Control systems revenue.
- NOT DISCLOSED (read: FY26 10-K Note 1 and Note 17, Q1 FY27 10-Q Note 16): customers above 10% of receivables at Jun 30 and Sep 30, 2026.
- NOT DISCLOSED (read: all 10-Qs Q1 FY26-Q1 FY27): names of the quarterly >10% customers.
- NOT DISCLOSED (read: FY25 10-K Item 7): amount of the Q2 FY25 Display customer settlement.
- NOT DISCLOSED (read: FY24-FY26 10-Ks): actual completion date of Display manufacturing wind-down.
- NOT DISCLOSED (read: Q1 FY27 10-Q Note 7, FY26 10-K): commercial paper programme. None mentioned.

