# XS - Comet Yxlon CA20 (and sibling CA16): specifications, dose claims, adoption

Company: Comet Holding AG (SIX: COTN). FY = calendar year (ends 31 Dec). Division: IXS (X-Ray Systems, brand Comet Yxlon).
Evidence ids refer to `research/out/comet/parts/XS.csv` (73 rows: 10 [F], 57 [C], 4 [S], 2 [I]). Arithmetic: `research/out/comet/calc/XS_ca20_po_count.py`.
Almost everything about CA20 is a company statement. Product specs are tagged [C] because nobody outside Comet has tested them.

## Q1. CA20 and its siblings

### Models and versions

| Name | What it is | Launch / first stated | Evidence |
|---|---|---|---|
| CA20 Lab (MXI) | 3D computed laminography + 2D/2.5D; software-assisted review | First shown at productronica / SEMICON Europa, Munich, 14 Nov 2023 [F] (XS-001); Comet calls it the "Lab version introduced in late 2023" [F] (XS-004) | XS-001, XS-004 |
| CA20 Fab (AXI), "next generation" CA20 | Same imaging platform plus an EFEM loader, automated defect recognition (ADR) and CoS Insights automated 3D metrology, designed to sit in the production line | Planned "later in 2024" [C] (XS-005); launched at SEMICON Europa 2024, Nov 2024 [F] (XS-006, XS-009) | XS-005..XS-009 |
| Wafer-inspection extension | Wafer Manager software, TSV Insights X 2.5D (automated TSV metrology, KLARF output), chip-on-wafer automation | Comet: "wafer inspection solutions in 2025" [F] (XS-010); CMD roadmap: automated chip-on-wafer inspection in 2025 [C] (XS-055) | XS-010, XS-018, XS-021, XS-055 |
| CA16 | Sibling model in the "CA product line". 2D/2.5D only (no 3D), for flip chips and wafer bumping. Fab version has an EFEM for 300 mm wafers and CoW Insights X 2D | Listed on the Comet Yxlon site [F] (XS-032). Launch date: no date on any saved page (see Gaps) | XS-028..XS-032 |
| "New models tailored for specific uses" / "CA20 and its variants" (H1 2026 report) | The report names no model [C] (XS-033) | H1 2026 | XS-033 |

The 2023 and 2024 launch pages describe two different launches:
- **2023 page** (`ca20-launch-2023`, dated 15 Nov 2023). This was the first launch of the CA20 as a laboratory / R&D system. It covered computed laminography with sub-1 µm resolution, deep-learning evaluation with report generation, the Dose Manager, the Batch Manager and an "Insights" package (XS-001..XS-003).
- **2024 page** (`ca20-launch-2024`, SEMICON Europa 2024). It covers the "next generation" or "latest revision" of the CA20 as a fully automated fab tool. New items were the EFEM loader, the "Chip-on-Substrate Insights" automated 3D metrology package, manual, assisted and fully automated defect recognition, and production-line integration (XS-006..XS-008). The FY2024 annual report confirms the order: lab version in 2023, fab version in 2024 (XS-009).
- A third Comet corporate page (comet.tech/en/news/ca20-launch, dated 21 Dec 2023) tells the development story. It says the product started from a discussion with an unnamed "3D IC manufacturer" (XS-043).

My reading is that the H1 2026 "new models" most likely include the CA16 [I] (XS-073, Medium confidence). It is the only non-CA20 model in the CA line, and its 2D/2.5D wafer-bump focus matches "entry into additional application areas". Comet has not tied the H1 2026 wording to the CA16 by name.

Predecessor context. In 2019 Yxlon launched the FF70 CL, FF65 CL and FF65 IL laminography systems for TSVs, C4 bumps and 3D packages, developed with Nagoya Electric Works [S] (XS-066). So the CA20 is not Comet Yxlon's first semiconductor laminography line. Comet calls it a "complete redesign".

### Specifications as Comet states them (all [C] unless noted)

| Item | Comet's statement | Id |
|---|---|---|
| Resolution / voxel | "resolution of less than 1 µm" (2023 and 2024 launch pages). Defect-size classes "<1 µm, <50 µm, <1 mm". **No voxel size is given for the CA20 anywhere in the saved Comet sources.** CoS 3D Clarity scans "for bumps down to 50 µm". | XS-002, XS-014, XS-020 |
| Detector / field of view | Detector active area 130 x 130 mm, 1536 x 1536 px, 85 µm pitch; up to 40 fps; nanofocus source; oblique viewing ±65°. Max inspection envelope 435 mm. **The field of view at a given voxel size is not stated.** | XS-011, XS-012 |
| X-ray source | CA20 machines "equipped with Comet IXM's advanced x-ray tubes"; flyer lists the source type as "nanofocus". Which tube (e.g. Fyne) is fitted is not stated. | XS-035, XS-012 |
| Footprint | Lab about 2,350 kg, 1650x1400x2050 mm. Fab about 3,650 kg, 1955x3100x2200 mm. Fab max part weight 0.5 kg including the carrier. | XS-013 |
| Time per sample / site | "within minutes" (2023 story and 2024 launch); "revealing defects in seconds" (JOINT3 release); Wafer Manager "aligns wafers ... in seconds". A Comet Taiwan application blog (29 Oct 2026, system not named) reports a **4-minute** 3D TSV inspection cycle (continuous-rotation laminography + deep-learning denoising) against a 60-minute reference. Void ratio was 8.72±0.38% vs 9.03±0.18%. **No wafers-per-hour or per-site throughput is given.** | XS-008, XS-040, XS-021, XS-026, XS-027 |
| Automation | Fab version: EFEM loader, "fully automatic loader and ADC software", integration into the "Fab's material and information flows". TSV Insights X 2.5D and CoW Insights X 2D need the automatic loader. Outputs are KLARF, json and xml. CA16 has recipe set-up with production limits and import/export. In-cabinet cleanroom conditions are "comparable to ISO Class 3". **SECS/GEM is not named in any saved Comet source.** SEMI S2/S8 is claimed for FF35 CT SEMI and Cheetah EVO Semi, not for the CA20. | XS-015..XS-019, XS-029..XS-031 |
| 300 mm wafers | Explicit only for the **CA16** ("EFEM loader for 300mm wafers"; "Ø 300 mm wafer mount"). The CA20 page mentions wafer inspection and a Wafer Manager but gives no wafer diameter. | XS-029, XS-021 |
| Defect recognition / AI | ADR / ADC for solder bumps (FY2024 annual report). CoS Insights / CoS Insights X 3D are "powered by Dragonfly". TSV Insights X 2.5D and CoS Insights X 3D are exclusive to Comet Yxlon systems. The CMD 2025 software stack is DirectInspect (fully automated), ProInsight Studio (assisted) and Dragonfly 3D World. | XS-034, XS-019, XS-020, XS-038, XS-039 |
| Dragonfly / ORS | ORS (Montreal, maker of Dragonfly) was acquired in December 2020 [F] and fully integrated into IXS (XS-037). | XS-037 |

### What Comet says about X-ray dose to memory devices

Comet's own words, tagged [C], are all qualitative:
- **Dose Manager.** It tracks the dose delivered to the sample, calculated from tube power and source-sample distance. "To avoid damage to sensitive components such as flash and DRAM memories, it switches off the X-ray automatically once the dosage limit is reached" (XS-022, XS-023). The same text is on the CA16 page.
- **Dose Reduction Kit.** A collimator and 4 filters shield parts outside the region of interest (XS-024).
- **Dragonfly deep-learning segmentation.** It extracts information "from the low dose scan that protects your sensitive parts" (XS-025). The Stifel deck (Jun 2024) says "Dose Manager: protection of X-ray sensitive components" (XS-005 note).
- **Oct 2026 Comet blog.** It says a full-resolution 3D volume "at a dose that will not damage the component" takes too long for in-line use, and that the fast method uses "single-frame, low-dose acquisition" (XS-027 note).

What Comet does not say:
- **No dose figure.** There is no Gy, rad or mGy value per scan and no default limit.
- **HBM and NAND are never named in a dose context.** The only memory types named are "flash and DRAM". HBM is mentioned only as an inspection target (JOINT3 release, blog articles).
- The IXM "Need for speed" article's "four times more usable X-ray dose" for the Fyne NF4 refers to source output for speed, not to dose absorbed by the sample (XS-036).

## Q2. Adoption

### (a) Comet's own words, in date order

| Date | Statement | Tag | Id |
|---|---|---|---|
| FY2022 AR (Mar 2023) | An advanced-packaging collaboration "with a leading company in this space is exceeding expectations" (before the CA20) | [C] | XS-041 |
| CMD 2023 (Nov 2023) | "Increased installed base at semiconductor market leader: our co-creation partner". Testimonial: "We just found a new failure type". System types not stated. | [C] | XS-042 |
| CMD 2025 deck, 2023 baseline | Funnel 2023: 5 evaluations, 2 qualifications, **0 orders** | [C] | XS-052 |
| H1 2024 (Jul 2024) | Potential customers show "significant interest" in using the CA20 in lab and production | [C] | XS-044 |
| FY2024 AR (Mar 2025) | "first purchase order for the CA20" (FY2024). FY24 results deck: "First commercial success with CA20". | [F] | XS-045 |
| Q1 2025 TU (Apr 2025) | Collaborating with multiple customers; "several commercial agreements anticipated for 2025" | [C] | XS-046 |
| H1 2025 (Jul 2025) | "gaining strong traction" but some customers are "holding off on decisions". The results deck says "market adoption remains delayed". | [C] | XS-047, XS-048 |
| Q3 2025 TU (Oct 2025) | "a handful of purchase orders ... from various customers"; several new Dragonfly orders | [C] | XS-049 |
| CMD 2025 (13 Nov 2025) | ">80 active collaborations" on the CA20. Funnel 2025: **>60 evaluation, >25 qualification, 5 orders**. "Co-Creation with top market OSAT, IDM, foundry leaders". CA20 investment CHF 10-15m (2024). CA20 to be above break-even by 2028e. | [C] | XS-050, XS-051, XS-053, XS-056 |
| FY2025 (Mar 2026) | "First commercial sales of CA20 systems" [F]. "Double-digit million investments" in the CA20 weighed on IXS profitability [C]. | [F]/[C] | XS-057, XS-058 |
| H1 2026 (Jul 2026) | "more than doubling the number of purchase orders for the CA20" (report). The deck says "more than doubled CA20 purchase orders compared to YE25". New models; break-even "still projected for 2028". | [C] | XS-059, XS-060, XS-033 |
| Q3 2026 TU (Oct 2026) | "Strong order momentum, additional customer engagements and successful qualifications" (no count) | [C] | XS-061 |

What the PO numbers imply [I] (XS-072, Low confidence; script `XS_ca20_po_count.py`). If the CMD's 5 orders (Nov 2025) is a floor for year-end 2025, and "more than doubled compared to YE25" refers to the cumulative count, then cumulative CA20 POs at 30 Jun 2026 were **at least 11**. That means at least 6 new POs in H1 2026. Comet has given no PO number since November 2025. The half-year report itself leaves out the base period. The deck's "compared to YE25" is the only base given.

Customer types (Comet's words). Comet names the types as OSAT, IDM and foundry (XS-053), and its "co-creation partner" as a "semiconductor market leader" (XS-042). Memory makers are not named as a separate type; IDM would cover them. No research lab is named as a customer. Fraunhofer IZM / IZM-ASSID appears only as a supplier of test samples (XS-067).

Production vs failure analysis vs evaluation (Comet's words):
- The CMD 2025 deck maps FF35 CT Semi to root cause, CA20 Lab to failure analysis and CA20 Fab to process control (XS-054). Comet says it is "ready to solve demands from failure analysis, product ramp-up to high volume production".
- JOINT3 release: "early use focused on micro-bumps" (XS-062).
- The 2025 funnel is mostly evaluation (>60) and qualification (>25) (XS-051).
- **How the POs split between lab (FA/R&D) and fab (production) units is not disclosed.** So is whether any unit runs in high-volume production.

### (b) Customer-side and third-party evidence

| Item | Tag | What it shows | Id |
|---|---|---|---|
| Resonac's JOINT3 launch release lists "Comet Yxlon GmbH" as one of 27 members (panel-level organic interposer line, 515x510 mm) | [F] | Consortium membership only. Not a purchase, qualification or installation. | XS-063 |
| Trade press: 3D InCites (Dec 2024), Silicon Semiconductor (2023), BINDT, OneStopNDT, Semiconductor Packaging News | [S] | Reprints of Comet releases. No customer named. | XS-064, XS-065 |
| EPP Europe 2019: FF70 CL / FF65 CL / FF65 IL developed with Nagoya Electric Works | [S] | Predecessor line and development partner, not CA20 adoption | XS-066 |
| Dragonfly "Publication Spotlight" (Comet site) on an HBM micro-bump study by Excillum authors (Microelectronics Reliability 168, 2025): 30 s at 2.6 µm voxel, 75 min at 600 nm voxel | [S] | Dragonfly software used on a **non-Comet (Excillum) nano-CT**. Not CA20 evidence. Paper not retrieved. | XS-068 |
| SMTA WLP Symposium 2024 paper (Kruidhof, Jan; Comet Yxlon), HKUST seminar slides (Comet Yxlon, Jan 2024; CoWoS/InFO C4 examples) | [C] | Vendor-authored, not customer evidence | XS-069, XS-070 |

**No customer-side evidence of CA20 use was found.** I searched for CA20 or Comet Yxlon together with SK hynix, Samsung, TSMC, Micron, ASE, Amkor, imec, Fraunhofer, and IEEE ECTC / EPTC / IRPS / ISTFA. That turned up no paper, customer press release or trade report naming a CA20 customer or describing a CA20 used by a customer or lab. All CA20 adoption evidence is Comet's own statements. See Gaps.

## Gaps
- NOT DISCLOSED (read: CA20 product page Technical Data; CA20 CoS Fab flyer 2024; CA20 launch pages 2023 and 2024): CA20 voxel size (only "<1 µm resolution" / defect size given)
- NOT DISCLOSED (read: CA20 product page Technical Data; CA20 flyer): CA20 field of view at a stated resolution / magnification
- NOT DISCLOSED (read: CA20 and CA16 product pages; launch pages; packaging- and wafer-inspection pages; Oct 2026 continuous-rotation blog): time per wafer, wafers per hour, or time per site/ROI for the CA20 (only "minutes", "seconds", and a 4-minute 3D TSV cycle for an unnamed system)
- NOT DISCLOSED (read: all saved Comet sources, full-text search for SECS, GEM, E84, E87, FOUP, HSMS): SECS/GEM or other fab host-interface standard for CA20 / CA16
- NOT DISCLOSED (read: CA20 product page Technical Data; CA20 flyer): 300 mm wafer handling for the CA20 (stated only for CA16)
- NOT DISCLOSED (read: CA20 and CA16 pages, Dose Manager sections; launch pages; Stifel deck 2024; Oct 2026 blog): any X-ray dose figure per scan, default dose limit, or HBM / NAND-specific dose sensitivity
- NOT DISCLOSED (read: CA16 product page; Comet Yxlon news index; SEMICON Europa 2026 event page): CA16 launch date
- NOT DISCLOSED (read: H1 2026 half-year report IXS section; H1 2026 results presentation): names of the "new models tailored for specific uses" / "CA20 variants"
- NOT DISCLOSED (read: Q3 2025 TU; CMD 2025 deck and release; FY2025 AR / results deck / release; H1 2026 report and deck; Q3 2026 TU): CA20 PO count after Nov 2025, installed base, revenue, customer names, regions, lab-vs-fab split
- NOT RETRIEVED (tried: Comet Yxlon semiconductors page download "Semiconductor Inspection with X-ray (pdf)", behind a registration form): Comet semiconductor brochure
- NOT RETRIEVED (tried: CA16 product page download "CA16 Flyer (English) (pdf)", behind a registration form): CA16 flyer
- NOT RETRIEVED (tried: semi.org PDFs of Stephan Haferl SEMICON Europa 2023 and 2024 talks, and semi.org blogs "Comet Yxlon: the future of advanced packaging is x-ray" and "How AI-driven 3D X-ray inspection supports a sustainable inspection strategy for AI chips"; all HTTP 403): SEMI-hosted Comet material
- NOT RETRIEVED (tried: pdf.directindustry.com cy-CA20-Brochure-en, HTTP 403; photonics.com product page, HTTP 403): third-party-hosted CA20 brochure
- NOT RETRIEVED (tried: doi.org/10.1016/j.microrel.2025.115694; only a redirect stub was saved): Dreier, Nilsson, Hallstedt, Microelectronics Reliability 168 (2025) 115694
- NOT RETRIEVED (tried: web searches combining CA20 / Comet Yxlon with SK hynix, Samsung, TSMC, Micron, ASE, Amkor, imec, Fraunhofer, HBM, hybrid bonding, ECTC, EPTC, IRPS, ISTFA, IMAPS, SEMI): any customer-authored paper, customer press release or independent trade report on CA20 use

## Premise corrections
- **"Launch pages for 2023 and 2024".** These are two different launches, not a duplicate. 2023 was the first (Lab / MXI) CA20 at productronica / SEMICON Europa on 14 Nov 2023. 2024 was the "next generation" fully automated Fab / AXI version with an EFEM loader at SEMICON Europa in Nov 2024. A third, corporate page dated 21 Dec 2023 tells the development story.
- **"CA20 and its variants" / "new models".** Comet's site names only one sibling model, the **CA16** (2D/2.5D, wafer bumping, 300 mm EFEM). "CA20 Lab" and "CA20 Fab" are configurations of the CA20, not separate models. The H1 2026 report names no model, so linking it to the CA16 is my inference (XS-073).
- **"More than doubled POs in H1 2026".** The half-year report gives no base. The results deck says "compared to YE25", which reads as the cumulative count at 30 Jun 2026 against 31 Dec 2025, not H1 2026 against H1 2025.
- **"CMD 2025 numbers".** The CMD was held on 13 Nov 2025. The repo deck file is dated 2026-01-09, which is the save date, not the event date. The funnel numbers (5 orders, >25 qualifications, >60 evaluations) are on deck page 63.
- **HBM micro-bump "evidence".** The Dragonfly HBM micro-bump spotlight comes from Excillum authors on an Excillum nano-CT, analysed in Dragonfly. It is not CA20 data, and its voxel and time numbers must not be read as CA20 specs.
- **Dose claims.** Comet's dose wording names "flash and DRAM", not HBM or NAND specifically, and gives no number.
- **ORS / Dragonfly.** The acquisition was in December 2020, not a recent deal.
