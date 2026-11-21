# XR module notes: X-ray dose and radiation damage to memory, plus the TSMC SEMICON Taiwan 2026 keynote

Run date 2026-11-21. Period: 1 Jan 2025 to 21 Nov 2026. Evidence rows are in `research/out/customer_side/parts/XR.csv` (XR-001 to XR-038). `quote_check.py` result: 34 of 34 quotes FOUND (2 layout-insensitive, both hyphenation line breaks in the SMT007 PDF). There are no flags. Arithmetic is in `research/out/customer_side/calc/XR_dose_units.py`. Fiscal periods do not apply (`n/a`): all items are technical documents dated by calendar month.

## 1. Findings

### XR-1: chipmaker statements on X-ray damage to memory (Jan 2025 to Nov 2026)

**Bottom line.** I found four in-period chipmaker sources.
- **Intel** is the only one that gives dose numbers.
- **Micron** appears as a co-author on one journal paper, which I read as an abstract only.
- **Samsung** appears in a patent application.
- **TSMC** appears only through press accounts of its September 2026 keynote.

I found nothing in period from SK hynix or Amkor. ASE's in-period paper uses 3D X-ray but its abstract says nothing about dose. None of these sources gives an HBM-specific dose limit or a measured HBM failure dose.

**Intel (the strongest item, with one caveat on dates).** SMT007 Magazine republished the Intel paper "DRAM Damage Due to X-ray Inspections Post-PCB Assembly" in April 2025. All six authors are from Intel Corporation. The paper first appeared at SMTA International in October 2024, which is outside the period. That original version is logged as out-of-period context in XR-027.
- **Problem framing.** The authors say X-ray damage to on-package DRAM "poses a significant challenge to the inspections of BGAs with on-package DRAM" (XR-001).
- **Failure mode.** They name static refresh time (tref, i.e. retention) as the most sensitive parameter, with reverse-junction leakage as the probable cause. This comes from the literature they cite, not from their own measurement (XR-004).
- **Doses.** They stepped the dose up in 50-rad increments to 350 rad (3.5 Gy), and MemTest86 showed no errors (XR-002).
- **Limit.** They call 350 rad "three times the limit provided by DRAM manufacturer". They saw no infant-mortality failures but warn that long-term reliability "may be reduced" (XR-003). The manufacturer's limit and the supplier's name are not stated. Read literally, the limit is about 117 rad (XR-035, Low confidence).
- **Test set-up.** All dose DOE runs used a 2D manual X-ray tool (MXI), with TLD dosimeters. Settings were 120–160 kV, 14.5–20 W and 55–315 s, with no filter or with Al, Zn or Cu filters of 1.6–4.8 mm. Dose on three BGA builds was also measured in typical 3D automated (AXI) scans (XR-005).
- **Dose drivers.** Copper filters cut dose the most but made images unusable. Dose rose linearly with inspection time, and the PCB and substrate acted as shields (XR-006).
- **Production constraint?** The authors call it an inspection challenge, not a production constraint. Elsewhere they say latent damage is expected to affect only a small share of samples (p46).
- **Scope.** The memory is on-package DRAM in an Intel BGA, not HBM.

**Micron (co-author).** Micron's S. Beltrami (Process R&D, Vimercate) co-authored an IEEE TNS paper in August 2025 with the University of Padova (XR-008).
- **Finding.** Earlier X-ray exposure did not significantly change the alpha soft-error rate of 3D NAND, "at least for small doses" (XR-007).
- **Dose framing.** The "small doses" at which no significant change was seen were still "well above those commonly used for printed circuit board inspections" (XR-009).
- **Failure modes studied.** Threshold-voltage shifts and bit-error rates.
- **Limits of the evidence.** I read the abstract only, and it gives no dose numbers. The authors do not frame it as a production constraint.

**Micron, adjacent only.** Micron's IRPS 2026 abstract says the total-ionizing-dose damage threshold for terrestrial use cases "is measured and shown to be inconsequential" (XR-010). That covers field radiation (neutrons and alphas), not X-ray inspection, and the abstract gives no threshold value.

**Samsung.** Samsung's patent application US 2026/0126403 A1 was filed in October 2025 and published in May 2026.
- **Damage wording.** It says a low-pass filter between the source and the object means "damage and defects that may occur in the object to be inspected due to the X-ray beam can be reduced" (XR-011).
- **HBM link.** It names HBM microbump bonding structures (microbumps of 1 µm or less) as the inspection target. The method is inline X-ray laminography or CT (XR-012).
- **Limits.** It gives no dose numbers and names no failure mode. It is a patent application, not a paper.

**TSMC (press only).** DIGITIMES reported on 4 September 2026 that TSMC "is calling for future HBM and DRAM designs to become more compatible with X-ray inspection", citing "radiation exposure to sensitive memory devices" (XR-013). The speaker is identified as Zhihua Zou (XR-014). The article is paywalled, so only the teaser and caption were read, and no dose figure is visible. For details of the talk, see the XR-2 section below.

**In-period chipmaker X-ray papers with no dose statement.**
- Intel with Comet, ISTFA 2026: X-ray CT de-warping of FCPGA packages. The abstract does not mention dose (XR-023).
- ASE, ICEP-IAAC 2025: 3D X-ray failure analysis of fan-out packages. The abstract does not mention dose (XR-024).

**Not found.** I found no in-period statement from SK hynix or Amkor on X-ray damage to memory. That covers news.skhynix.com searches, Korean-language searches, Crossref searches by affiliation (SK hynix, Samsung, Micron, TSMC, Intel, ASE, Amkor with "X-ray"), the saved Crossref volume lists for ECTC, IRPS, ISTFA, IPFA, EPTC, IEDM, VLSI, ASMC, IMW, IITC, ITC, LTB-3D and the SPIE metrology volumes for 2025–26, and the coordinator's `calc/paper_candidates.csv`. ASE's only in-period X-ray paper is XR-024 (no dose statement). I found no chipmaker paper on X-ray damage from CD-SAXS, XRF or XRD metrology to memory wafers. The only CD-SAXS damage paper in the SPIE 2026 volume covers EUV resists and is by IBM and Brookhaven, not one of the seven companies (see leads).

**Non-chipmaker context, in period (not chipmaker statements).**
- **Hanyang University and Radiate Inc., IEEE TNS November 2026.** DDR4 parts from three unnamed makers were irradiated in a 130 kV PCB X-ray inspection machine, and retention failed-bit counts were measured. The dose-sensitivity metric varies 5.46 times depending only on which dose quantity is used (XR-025).
- **Hanyang, Radiate and Cisco, MDPI Electronics, 19 November 2026.** The HBM-relevant dose-rate equivalent during PCB 3D CT inspection was about 0.46 mGy(Si)/s on an Omron VT-X750 at 115 kV, 130 µA, with 1 mm Al (XR-026). At that rate, 1 Gy takes about 36 minutes of beam-on time, and Intel's 350 rad would take about 127 minutes. That comparison is Low confidence because the dose quantities differ (XR-036).
- **Trade press.** Semiconductor Engineering says dose control is "a top-line concern for memory chips" (Nov 2025, XR-020) and that HBM is "very sensitive to radiation damage" (Feb 2026, XR-021). Both are the journalist's own words, not chipmaker quotes.

**Out-of-period chipmaker context (labelled; not used for the in-period answer).**
- Intel, SMTA International October 2024 abstract: DRAM exposure limits "are not clear or readily available" (XR-027).
- Samsung patent US 10,984,853 B2 (granted 2021): X-ray damage to memory devices "is increasing" and "quantifying the X-ray dosage is difficult". The patent puts an on-chip BJT dose detector in the memory device (XR-028).
- Samsung patent US 11,217,495 B2 (granted 2022): soft X-rays "may be absorbed" in the substrate and cause "degradation of refresh characteristics or a charge loss" (XR-029).
- Intel patent US 11,506,709 B2 (granted 2022): commercial X-ray radiation "may potentially induce irreversible damage" at gate level in memory dies. It names DRAM, SRAM and HBM (XR-030).
- NIST report on ECTC 2024: TSMC's Zou named 3D X-ray imaging and IR inspection as TSMC techniques. The summary contains no dose remark (XR-031).

### Dose statements table

| Chipmaker | Document, date | Exact wording | Dose / numbers | Failure mode | Method | Tag + evidence id |
|---|---|---|---|---|---|---|
| Intel | SMT007 Mag., Apr 2025 (republication of SMTA paper, Oct 2024), p48 | "The DRAM damage due to irradiation poses a significant challenge to the inspections of BGAs with on-package DRAM" | none in sentence | DRAM damage (on-package DRAM) | Post-SMT 2D/3D X-ray | [F] XR-001 |
| Intel | same, p54 | "Even after total exposure of 350 rads, MemTest86 gave no errors on the DRAM." | 350 rad (3.5 Gy) total, 50 rad steps; DOE 120–160 kV, 14.5–20 W, 55–315 s, Al/Zn/Cu 1.6–4.8 mm (Table 1) | No functional errors (MemTest86) | 2D manual X-ray (MXI); TLD dosimetry; 3D AXI dose also measured | [F] XR-002, XR-005 |
| Intel | same, p54 | "even after overexposure to three times the limit provided by DRAM manufacturer, no infant mortality failures were observed." | 3× maker limit; limit not stated (≈117 rad implied, [I] XR-035, Low) | No infant mortality; "reliability ... over longer periods of usage may be reduced" | 2D MXI | [F] XR-003 |
| Intel | same, p48 | "the increase in reverse junction leakage is the most probable cause for tref degradation" | none | Retention / static refresh (tref) degradation via junction leakage (from cited literature) | n/a (literature) | [F] XR-004 |
| Micron (co-author, Padova lead) | IEEE TNS, Aug 2025, abstract | "Experimental results show that the alpha soft error rate is not significantly affected by previous X-ray irradiation, at least for small doses" | "Small doses" still "well above those commonly used for printed circuit board inspections"; no values in abstract | Vt shifts, bit errors (3D NAND); no significant alpha SER change | Lab X-ray irradiation, then alpha exposure | [F] XR-007, XR-008, XR-009 |
| Micron (adjacent) | IRPS, Mar 2026, abstract | "The threshold for total ionizing dose damage from terrestrial usecases is measured and shown to be inconsequential." | Threshold value not in abstract | TID (terrestrial, not X-ray inspection) | Accelerated neutron/alpha tests | [F] XR-010 |
| Samsung | US 2026/0126403 A1, filed Oct 2025, pub. May 2026 | "damage and defects that may occur in the object to be inspected due to the X-ray beam can be reduced" | None | "damage and defects" (unspecified); HBM microbump bonding named as target | Inline X-ray laminography/CT with low-pass filter | [F] XR-011, XR-012 |
| TSMC (press account) | DIGITIMES, 4 Sep 2026 (teaser; paywalled) | "TSMC is calling for future HBM and DRAM designs to become more compatible with X-ray inspection" | None visible | "radiation exposure to sensitive memory devices" | X-ray inspection (type not stated) | [S] XR-013, XR-014 |
| TSMC (press about the abstract) | WindowsForum, 5 Sep 2026 | "The public keynote abstract explicitly lists “DRAM/HBM damage concern by X-ray” among the challenges for advanced-packaging inspection." | None ("no ... inspection doses" identified, XR-018) | "DRAM/HBM damage" (unspecified) | Not stated | [S] XR-015, XR-018 |
| Intel (with Comet) | ISTFA, Oct 2026, abstract | No dose or damage wording (abstract is about CT de-warping) | n/a | n/a | X-ray CT | [F] XR-023 |
| ASE | ICEP-IAAC, Apr 2025, abstract | No dose or damage wording | n/a | n/a | 3D X-ray (fan-out FA) | [F] XR-024 |
| OUT OF PERIOD: Intel | SMTA Intl., Oct 2024, abstract | "the limits to which these DRAMs can be exposed are not clear or readily available" | n/a | DRAM degradation | Post-PCB X-ray | [F] XR-027 |
| OUT OF PERIOD: Samsung | US 10,984,853 B2, 2021 | "the damage of semiconductor memory devices by X-ray is increasing. However, quantifying the X-ray dosage is difficult." | none | Leakage from Vt change; refresh degradation (body text) | X-ray inspection; on-chip BJT dosimeter | [F] XR-028 |
| OUT OF PERIOD: Samsung | US 11,217,495 B2, 2022 | "cause various failures, such as degradation of refresh characteristics or a charge loss in the semiconductor chip" | Soft X-ray ~0.1–12 keV filtered; hard ~12–120 keV for imaging | Refresh degradation, charge loss | X-ray inspection with semiconductor absorption filter | [F] XR-029 |
| OUT OF PERIOD: Intel | US 11,506,709 B2, 2022 | "the radiation used in commercial x-ray equipment may alter the electrical conditions of memory die at gate level, which may potentially induce irreversible damage." | none | Gate-level irreversible damage (DRAM, SRAM, HBM named) | Interconnect X-ray inspection; titanium filter | [F] XR-030 |

**Production constraint?** None of the chipmaker documents uses the words "production constraint".
- **Intel** comes closest. It calls the damage "a significant challenge to the inspections" (XR-001), and its abstract says safe exposure limits are unclear (XR-027, out of period).
- **TSMC**, per press, asks for HBM and DRAM designed for X-ray inspection. That implies an upstream design requirement (XR-013), but the TSMC wording itself is not available. WindowsForum says the abstract frames it as a "challenge", not a mandate (XR-015, XR-017).

**Vendor material (context only; not chipmaker statements).**
- Nextin, a Korean inspection-tool maker, says its collimated-beam X-ray tool for HBM hybrid bonding aims to overcome concern about chip damage from X-ray exposure (etnews, July 2025, XR-022).
- SEC Co. says it supplies HBM X-ray inspection tools to Micron's Singapore unit, about 5.8 billion won. This is the vendor's claim, with no dose wording (saved: `2026-11-21_etoday_sec-micron-hbm-xray-order.html`, 10 Nov 2026).
- The Rigaku and ZEISS SEMICON Taiwan 2026 releases contain no dose wording (saved).
- A July 2024 Semiconductor Engineering article (out of period) carries an unattributed paragraph on "the danger of X-ray overexposure" for HBM. From the surrounding quotes, it appears to be Nordson's Brad Perkins, but the attribution is not certain (saved: `2026-11-21_semiengineering_semieng-xray-inspection-essential-adv-packaging.html`).

### XR-2: the TSMC advanced-packaging metrology keynote at SEMICON Taiwan, September 2026

**Does it exist?** Yes, with qualifications (XR-037).
- **Who and where.** DIGITIMES's photo caption shows "TSMC's Zhihua Zou" speaking on advanced packaging inspection challenges at SEMICON Taiwan 2026 (XR-014).
- **Title.** A WindowsForum article links to a page with the anchor text "Keynote: Challenges and Opportunities for Metrology and Inspection of Advanced Packaging", at https://www.semicontaiwan.org/en/node/18506 (XR-016).
- **Slot.** Search snippets of the refused forum page place it as the keynote of the **Semiconductor Advanced Inspection and Metrology Forum** on **Friday 4 September 2026, 09:45–10:25, Room 402, TaiNEX 1 (4F)**. The slot details are leads only.
- **Not a main-stage keynote (snippets only).** Per the same snippets it was a forum keynote, not a show-level keynote; the saved WindowsForum page says only "keynote". A third-party guide (snippet only) says TSMC was not on the main keynote stage that year.

**(a) Published abstract text: NOT RETRIEVED.** It sits on semicontaiwan.org, which refuses scripts (HTTP 403 on https://www.semicontaiwan.org/en/node/18506). I found no copy on a script-friendly host: no SEMI newswire release, co-organiser page or hosted PDF programme carried it. The user can save these pages by hand:
- https://www.semicontaiwan.org/en/node/18506 (keynote abstract)
- https://semicontaiwan.org/en/Metrology_2026 (forum agenda)
- https://www.semicontaiwan.org/en/node/17406 (speaker bio; Chinese version https://semicontaiwan.org/zh/node/17406)

**(b) What search snippets suggest (leads only, not evidence).**
- **Forum agenda snippet (semicontaiwan.org/en/Metrology_2026).**
  - Keynote: "Dr. Zhihua Zou, Director, TSMC", "Challenges and Opportunities for Metrology and Inspection of Advanced Packaging".
  - Timing: Friday 4 Sept. Snippets give the forum as 9:00 am–3:55 pm and the keynote as 9:45–10:25 am.
  - Forum chair: Dr. I-Shih Tseng (CEO, Chroma ATE). The forum is advised by the SEMI Inspection and Metrology Committee.
  - Other speakers come from NIST, ITRI, NPL, imec and TRUMPF.
- **Speaker bio snippet (semicontaiwan.org/en/node/17406).**
  - Current role: Director of the Advanced Packaging Metrology Engineering (APME) Division at TSMC's "APTS", covering InFO, CoWoS and SoIC metrology. The snippet's expansion of APTS is uncertain.
  - Background: about 18 years at Intel in assembly and test development, then about 2 years as principal engineer on hybrid bonding, joining TSMC in 2023. He holds 15 patents.
- **Abstract contents.** A search snippet repeats WindowsForum's statement that the abstract lists "DRAM/HBM damage concern by X-ray". No snippet showed any dose number in the abstract.
- **Date check.** A TechTimes snippet dates the SEMICON Taiwan 2026 kick-off to 31 August. That is the start of the pre-show programmes; Focus Taiwan (XR-033) gives related programmes as 31 Aug–4 Sept and the exhibition as 2–4 Sept. It does not conflict with a 4 September forum date.

**(c) Press paraphrase [S]. Every item here is secondary, and none is TSMC's own wording.**
- **DIGITIMES, 4 Sep 2026 (Sherri Wang; paywalled teaser).** TSMC "is calling for future HBM and DRAM designs to become more compatible with X-ray inspection", citing buried defects and "radiation exposure to sensitive memory devices" (XR-013, XR-014).
- **WindowsForum, 5 Sep 2026 (unsigned analysis).**
  - It says the public abstract lists "DRAM/HBM damage concern by X-ray". It also says the abstract names collaboration with foundry customers, HBM vendors and equipment vendors, and "design for metrology", as opportunities (XR-015, XR-017).
  - It says the abstract does not set a mandatory design rule or supplier requirement.
  - It says no public evidence in the material it reviewed gives doses or failure rates (XR-018).
  - Its title for the talk, "a TSMC advanced-packaging metrology keynote at SEMICON Taiwan", matches the user's wording.
- **Uncle Stock Notes, 7 Sep 2026 (Chinese investor Substack paraphrasing DIGITIMES).**
  - It attributes the talk to TSMC's advanced-packaging quality and reliability team at the closing session (XR-019). Saved sources do not corroborate this: the caption names only Zou (no team or session) and WindowsForum gives no time slot. Neither contradicts it; the forum-keynote slot is a snippet lead only.
  - It says TSMC "named" SK hynix, Samsung and Micron, and asked for X-ray markers designed into HBM dies ("DFI"). No other saved source supports this. Treat it as the blogger's reading.
- **Not saved.** An apparent full copy of the DIGITIMES article on lcdproduct.com was not fetched, because it would get around the DIGITIMES paywall (see leads).

**Other TSMC talks at SEMICON Taiwan 2026.**
- **Saved [S].**
  - James Chen, Advanced Packaging R&D Director: AI system power and microchannel cooling (TrendForce, 2 Sep 2026, XR-032).
  - Cliff Hou, SVP: co-hosted the 2 September CEO summit fireside chat with ASE's Tien Wu (Focus Taiwan, 15 Aug 2026, XR-033).
- **Snippets only (leads).**
  - Advanced Testing Forum: Jian Ting Chen and Oscar Lee.
  - Silicon Photonics Global Summit: Ming Fa Chen (COUPE); K.C. Hsu, co-chair.
  - Smart Manufacturing Forum keynote: Chris Lin, VP and CIO.
  - Strategic Materials Conference: April Li, keynote; Min-Te Chen, chair.

**SEMICON Taiwan 2025 (10–12 September 2025).**
- **No TSMC metrology or inspection talk found.** Snippets of the refused 2025 forum page (12 Sept 2025, chair I-Shih Tseng) list speakers from Thermo Fisher, TESCAN, Chroma ATE and OmniMeasure, and no TSMC speaker.
- **Closest item.** TSMC VP Jun He spoke at the launch of the SEMI 3DIC Advanced Packaging Manufacturing Alliance on 9 September 2025. He said about 10 million HBM stacks are consumed per quarter, so a 1% yield loss is costly. The reporter adds that this shows why inspection matters. There is no X-ray or dose content (UAnalyze, XR-034).
- **Test talks (snippets only).** Chris Wang and Harvey Lin of TSMC were listed for the 2025 Advanced Testing Forum, on test topics.

## 2. Gaps

- NOT RETRIEVED (tried: https://www.semicontaiwan.org/en/node/18506, keynote abstract, fetch.py HTTP 403; refused host, no workaround)
- NOT RETRIEVED (tried: https://semicontaiwan.org/en/Metrology_2026, 2026 forum agenda, fetch.py HTTP 403)
- NOT RETRIEVED (tried: https://www.semicontaiwan.org/en/node/17406, speaker bio, fetch.py HTTP 403; zh version https://semicontaiwan.org/zh/node/17406 not attempted, same refused host)
- NOT RETRIEVED (tried: https://www.semicontaiwan.org/en/semiconductor_advanced_inspection_and_metrology_forum_2025, 2025 forum page, fetch.py HTTP 403)
- NOT RETRIEVED (tried: https://semihub.io/en/blog/semicon-taiwan-2026-guide.html, third-party attendee guide with the Zou slot, fetch.py HTTP 403)
- NOT RETRIEVED (tried: https://www.digitimes.com/news/a20260904VL218/tsmc-inspection-hbm-packaging-design.html full text; paywall serves teaser only)
- NOT RETRIEVED (tried: https://www.mdpi.com/2079-9292/15/22/5391, fetch.py HTTP 403; Crossref abstract used instead)
- NOT RETRIEVED (tried: full texts of https://doi.org/10.1109/TNS.2025.3561936, https://doi.org/10.1109/IRPS61424.2026.11499239, https://doi.org/10.1109/TNS.2026.3739333; ieeexplore.ieee.org refuses scripts, abstracts used)
- NOT RETRIEVED (tried: Semantic Scholar search API, 4 of 5 keyword queries returned HTTP 429; Crossref searches used instead)
- NOT RETRIEVED (tried: https://www.circuitinsight.com/uploads/2/dram_damage_due_xray_inspections_post_pcb_assembly_smta.pdf; served a non-PDF page; same paper read in SMT007 Apr 2025 PDF)
- NOT RETRIEVED (tried: https://manuscript.isc.ac/Inventory/49/1053941.htm, record said to give Micron affiliation of the 2006 IRPS paper; connection failed)
- NOT RETRIEVED (tried: https://ectc.net/wp-content/uploads/2025/06/ECTC2025_SpecialSession_6-Advances-in-Chiplets.pdf identified via search; ectc.net is a refused host, not fetched)
- NOT RETRIEVED (tried: not fetched; https://lcdproduct.com/tsmc-urges-hbm-makers-to-design-for-x-ray-inspection-as-packaging-grows-more-complex/ appears to republish the paywalled DIGITIMES article)
- NOT DISCLOSED (read: SMT007 Apr 2025 Intel article pp46-56, DRAM manufacturer's X-ray dose limit value and supplier name)
- NOT DISCLOSED (read: SMT007 Apr 2025 Intel article pp49-55, numeric dosimeter readings; figures only)
- NOT DISCLOSED (read: Semantic Scholar abstract of 10.1109/TNS.2025.3561936, X-ray dose values)
- NOT DISCLOSED (read: Semantic Scholar abstract of 10.1109/IRPS61424.2026.11499239, TID threshold value)
- NOT DISCLOSED (read: US 2026/0126403 A1 description, dose numbers and failure mode)
- NOT DISCLOSED (read: Crossref abstract of 10.31399/asm.cp.istfa2026p0587, dose or damage)
- NOT DISCLOSED (read: Semantic Scholar abstract of 10.23919/ICEP-IAAC64884.2025.11003029, dose or damage)
- NOT DISCLOSED (read: DIGITIMES 2026-09-04 teaser and caption, dose numbers and TSMC's exact wording)

## 3. Premise problems in the prompt

1. **"Keynote at SEMICON Taiwan, September 2026."** The talk exists: the speaker comes from the DIGITIMES caption, and "keynote" and the title from WindowsForum. Per search snippets only, it was the keynote of one forum, the Semiconductor Advanced Inspection and Metrology Forum, on 4 September 2026, not a SEMICON Taiwan main-stage keynote (XR-014, XR-037).
2. **"Quote the published abstract."** The abstract is published only on semicontaiwan.org, which refuses scripts, and I found no copy elsewhere. It is NOT RETRIEVED. What we have about it is a secondary paraphrase (WindowsForum, XR-015, XR-017), which must not be treated as the abstract.
3. **"TSMC urges HBM makers to design for X-ray inspection."** That is DIGITIMES's headline framing. The claim that TSMC "named" SK hynix, Samsung and Micron, and asked for X-ray markers in HBM dies, comes only from an investor blog (XR-019). WindowsForum says the abstract states no mandate (XR-017).
4. **The XR-1 premise that chipmakers have published HBM X-ray dose limits.** In period, no chipmaker document gives an HBM dose limit or HBM failure dose. The only chipmaker dose numbers are Intel's, for on-package DRAM: 350 rad tested, three times an unstated maker limit (XR-002, XR-003). Intel's article is an April 2025 republication of an October 2024 paper, so it is in period only through the republication.
5. **The blog's description of the talk.** It attributes the talk to TSMC's quality and reliability team at the "closing session". No saved source corroborates or contradicts this; it fits poorly only with snippet leads (the forum-keynote slot and the APME (metrology) role in the speaker-bio snippet) (XR-019).

## 4. Unverified leads (could not be turned into [F] or [S] rows)

- **Lee, Yun, Seo, Kang, Lee, Cho, "An Evaluation of X-Ray Irradiation Induced Dynamic Refresh Characterization in DRAM", IRPS 2019.** https://doi.org/10.1109/IRPS.2019.8720574. The affiliation is not in the saved Crossref or Semantic Scholar records; it may be SK hynix. It is out of period. It matters because it would be the only SK hynix X-ray refresh study. Saved record: `2026-11-21_semanticscholar_10.1109-irps.2019.8720574.json`.
- **Ditali, Ma, Johnston, "X-Ray Inspection-Induced Latent Damage in DRAM", IRPS 2006, plus TDMR 2007 and IRPS 2007 follow-ups.** https://doi.org/10.1109/RELPHY.2006.251226. A search summary says Micron Boise and a 120 rad(Si) susceptibility, but neither is in the saved records. It is out of period.
- **IMAPS Device Packaging, "Effects of x-ray exposure on NOR and NAND flash memories during high-resolution 2D and 3D X-ray inspection".** https://imapsource.org/article/56080-effects-of-x-ray-exposure-on-nor-and-nand-flash-memories-during-high-resolution-2d-and-3d-x-ray-inspection.pdf. Per snippets it tested Micron NAND (first byte errors at about 75–150 Gy) against routine 2D inspection at about 15–20 Gy. It is third-party and older.
- **ECTC 2025 Special Session 6, "Advances in Chiplets" (fault isolation and failure analysis).** https://ectc.net/wp-content/uploads/2025/06/ECTC2025_SpecialSession_6-Advances-in-Chiplets.pdf. Per a snippet it includes an HBM case study and a speaker now at Samsung. The host is refused.
- **SEC Co.** A BigGo Finance snippet says SEC patented a way to reduce X-ray damage to HBM and supplies X-ray tools to Micron (https://finance.biggo.com/news/4be6a91b-ef72-4cc1-b609-b22f13690a99). This is vendor material, and the patent was not identified.
- **IBM and Brookhaven, "Mitigating x-ray–induced damage in CD-SAXS metrology of EUV resists", SPIE AL+P 2026.** DOI 10.1117/12.3090456. The subject is resist, not memory dies, and the authors are not chipmakers. The SPIE page is refused, and the saved Crossref record has no affiliations.
- **Marvell, Bosch and Infineon, "Impact of X-Ray Radiation on Mixed Signal Products with Planar and FinFET Processes", IRPS 2026.** DOI 10.1109/IRPS61424.2026.11499248. It covers logic and mixed-signal parts, and the authors are not among the seven (saved Crossref record).
- **Axiom Electronics, "Component Failure Resulting from Over-Exposure to Ionizing Radiation During Manual X-Ray Solder Joint Inspection", SMTA International 2025.** DOI 10.37665/smbqvvu54217. An EMS company, not a chipmaker.
- **University of Florida, arXiv 2606.26430 (design guidelines for X-ray inspection of CoWoS, IMAPS 2025) and arXiv 2606.22149 (failure-analysis survey).** These are academic; the abstract pages are saved. No chipmaker co-authors and no dose content.
- **KAIST, Korean Nuclear Society, May 2026, HBM X-ray 3D imaging system.** Saved: `2026-03-29_kns_26S-509-hbm-fast-xray-3d.pdf`. It gives an optimal 80–120 kVp but no dose. Academic.
- **Samsung CN110136862B.** This is the Chinese family member of US 11,217,495 B2 (XR-029) and is out of period.
- **SemiHub SEMICON Taiwan 2026 guide.** Snippets say TSMC "appears not on the keynote stage but scattered across 8 technology forums with 14 talks". The page is refused.
- **Process notes.**
  - I used `firecrawl_scrape` once, on the JS-only page https://iconnect007.uberflip.com/i/1533904/45. It returned only the viewer shell, saved as `2026-11-21_iconnect007_smt007-apr2025-p45-viewer.md` (via firecrawl_scrape (JS page)). The article was then read from the issue PDF.
  - One `firecrawl_search` call failed for lack of credits. Discovery otherwise used WebSearch.
  - Four DIGITIMES Taiwan pages fetched while looking for a Chinese version of the article proved unrelated video items and are not cited (`2026-11-21_digitimes-tw_shwnws-*.html`).
  - These saved files are also uncited or off-topic: `2025-08-28_nist_material-needs-measurement-challenges-adv-packaging.pdf`, `2025-01-10_zeiss_ebook-semiconductor-packaging-failure-analysis.pdf`, `2026-11-21_cnyes_semi-test-metrology-three-demands-2025.html`, `2026-11-21_googlepatents_US12237032B1.html` (University of Alabama in Huntsville), and `2026-11-21_smta-circuitinsight_dram-damage-xray-post-pcb-assembly-served.html` (a non-paper page).

## Corrections after verification (2026-11-21)

- Rows changed after an independent two-stage check: XR-005, XR-009, XR-014, XR-018, XR-019, XR-022, XR-029, XR-037.
- XR-005: Intel's dose DOE ran on the 2D MXI machine only; AXI was used only to measure dose on three BGA builds (p50).
- XR-009: claim restated as the abstract's finding (no significant alpha-SER change at small doses that are still well above PCB-inspection doses); new quote; Micron link now cited to the Crossref record.
- XR-014: note cross-reference corrected to XR-013 / XR-037.
- XR-018: WindowsForum's limiter "in the material reviewed" restored.
- XR-019: blog's team and closing-session attribution is "not corroborated" by saved sources, not "in conflict" with them.
- XR-022: publication date corrected to 2025-07-21; partner spelled Axiomatique (via the NexRay JV).
- XR-029: "may" restored; damaged chip 35 has no stated type (logic/memory types belong to the two-chip embodiment).
- XR-037: talk date and "forum keynote" slot marked in the claim as coming from unsaved search snippets only.
