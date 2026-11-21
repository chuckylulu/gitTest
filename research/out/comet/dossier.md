# Comet Holding AG (SIX: COTN) - dossier

Research date: 21 Nov 2026. **Fiscal year = calendar year (ends 31 December).** Currency CHF unless stated.
Periods are written "H1 2026 (Jan-Jun 2026)", "Q3 2026 (Jul-Sep 2026)", "FY2025 (Jan-Dec 2025)". Comet reports half-years
(annual report early March, half-year report late July) plus trading updates for Q1 (April) and Q3 (October).
Divisions: **PCT** = Plasma Control Technologies (RF power); **IXS** = X-Ray Systems (brand Comet Yxlon, incl. CA20);
**IXM** = Industrial X-Ray Modules (sources, generators, detectors).

Tags: [F] read in a saved primary document; [C] company claim that cannot be tested; [S] secondary source; [I] my
inference or calculation (script under calc/). Ids in brackets refer to `evidence.csv` (653 rows: 363 [F], 188 [C], 41 [S], 61 [I];
every quote found in its cited file by `tools/quote_check.py`; 15 key rows re-checked by a clean-context agent, see run_log.md). Full module write-ups with every table: `parts/XS_notes.md` (CA20), `parts/RV_notes.md` (rivals),
`parts/IXM_notes.md` (x-ray modules), `parts/DV_notes.md` (divisions, IXS, PCT, CMD targets), `parts/A_notes.md` (Module A).
Gaps: `gaps.md`. Handoff row: `handoff.md`. Reviewer packet: `review_packet.md`.

---

## 0. Premise check (prompt items corrected)

1. **"Rigaku XHENA" does not exist.** The closest Rigaku name is XHEMIS, a TXRF wafer-contamination tool. Rigaku has no
   released 3D X-ray imaging tool for packaging interconnects; its own page calls in-line X-ray imaging for micro-bumps/TSVs
   "developing" [C] (RV-024). Its packaging products are metrology (ONYX 3200 optical + XRF, launched 17 Dec 2025 [F] RV-026).
2. **Sigray now sits inside Applied Materials**: sigray.com redirects to appliedmaterials.com (observed 21 Nov 2026) [S]
   (RV-059). Deal date and terms not found.
3. **Zeiss's wafer-level in-line X-ray tool is ZEISS NLX-100/100M** (ZEISS SMT), not the Xradia line, which stays a
   lab / failure-analysis product (RV-010..RV-023).
4. **Bruker** no longer shows its X200 in-line X-ray product; its June 2025 "AI advanced packaging" order was for optical tools
   [F] (RV-046). **Onto Innovation's** X-ray link is a 27% stake in Rigaku (agreed 20 Apr 2026) [F] (RV-033), not an imager.
5. **CA20 "successor or sibling"**: the 2023 and 2024 launch pages are two different launches - CA20 Lab (14 Nov 2023) and the
   fully automated CA20 Fab with EFEM (SEMICON Europa, Nov 2024) [F] (XS-001, XS-006). The only other named model in the line
   is the **CA16** (2D/2.5D wafer bumping, 300 mm EFEM) (XS-028..XS-032). Comet's H1 2026 "new models" are not named; that they
   include the CA16 is my inference [I] (XS-073, Medium).
6. **"Strategic options" for IXS**: no saved Comet document uses "strategic options", "sale", "divest" or "partner" for IXS.
   The FY2025 annual report speaks of "focused actions, rather than large structural exits" [C] (DV-114).
7. **Last capital markets day** = CMD 2025, held 13 Nov 2025 (the saved deck's file date 2026-01-09 is its PDF date) (DV-137..143).
8. **ebeam** was not a 2022 segment: sold/closed in 2018-2020, division dissolved 1 Jan 2021 [F] (A-176, A-177).
   **ORS/Dragonfly** was acquired effective 31 Dec 2020, so there was no M&A in 2021-2025 [F] (A-168..A-174).
9. **Comet does not report divisional orders or book-to-bill**; only group orders [F] (DV notes, Gaps). Quarterly figures are
   sales and orders only; Q2 and Q4 are derived.
10. **H1 2025 and FY2024 were restated** (inventory write-down error, CHF 2.1m + 0.3m) - PCT only [F] (A-027, A-028, DV-043).
    Comet's FY2025 deck compares an un-restated H1 2025 with a restated FY2025, so its "H2 2025 margin 11.1%" is 10.2% on a
    consistent basis [I] (A-215, DV-068).
11. **North Star Imaging** is an ITW company, not part of Comet; it is an external MesoFocus user (IXM-017).
12. prior/ is empty in this repository; no prior-chat claims were checked.

---

## 1. Summary

- **CA20 adoption is real but small and entirely company-sourced.** First purchase order FY2024 and first commercial sales FY2025
  [F] (XS-045, XS-057); CMD 2025 funnel: >60 evaluations, >25 qualifications, **5 orders** [C] (XS-051); POs "more than doubled"
  vs YE2025 by June 2026 [C] (XS-059), i.e. at least ~11 cumulative if the base was 5 [I] (XS-072, Low). No customer paper,
  customer release or independent report naming a CA20 user was found (gaps.md, XS).
- **Specs Comet leaves out**: CA20 voxel size, field of view at a stated resolution, wafers per hour, SECS/GEM, 300 mm handling
  for the CA20 (stated only for CA16), and any dose number (XS gaps).
- **Dose**: Comet says only that its Dose Manager stops exposure at a limit "to avoid damage to ... flash and DRAM memories" [C]
  (XS-022, XS-023). No maker - Comet or rival - publishes a dose figure (RV notes).
- **Rivals for in-line wafer sockets** exist on paper (ZEISS NLX, Nordson XM8000Pro, Sigray/Applied Apex XCT-300, XAVIS
  Xscan-9860A) [C]; the only third-party evidence of X-ray tools on an HBM production line concerns **SEC (Korea)** manual NF120
  units at Micron [S] (RV-066, RV-071).
- **IXM sources**: no semiconductor inspection-system maker was found stating it buys Comet sources; the high-resolution systems
  found use Excillum or in-house sources [F] (IXM-023, IXM-026..IXM-033). Comet ranked itself #4 in open micro focus and #3 in
  open nano focus (CMD 2023) [C] (IXM-038).
- **IXS economics**: EBITDA loss in 5 of 9 half-years since 2022, EBIT loss in 7 [I] (DV-055..068); H1 2026 EBITDA CHF -4.0m
  (-8.2%) [F] (DV-040); Comet's own 2028 IXS margin target is 5-9%, far below the 22-27% group target [C] (DV-142).
- **PCT carries the group**: 40-102% of group EBITDA per half-year [I] (DV-069); one unnamed PCT customer = 22.8% of FY2025 group
  sales [F] (A-120).
- **Cycle turn is in the numbers**: Q3 2026 sales CHF 155.6m (+51.9%), orders CHF 275.6m, book-to-bill 1.77; FY2026 guidance
  raised to CHF 570-590m and 17-19% EBITDA margin [F] (A-041, A-051, A-052, A-116).
- **Guidance record is weak**: FY2022-FY2025, against initial guidance 0 beats / 2 in-line / 6 misses of 8 [I] (A-242).

---

## 2. Q1 - CA20 and siblings

| Item | CA20 (Comet's statement) | Tag / id |
|---|---|---|
| Launch | CA20 Lab first shown 14 Nov 2023 (productronica / SEMICON Europa); CA20 Fab ("next generation", EFEM, ADR, CoS Insights) launched SEMICON Europa Nov 2024; wafer-inspection extension (Wafer Manager, TSV Insights X 2.5D, chip-on-wafer automation) in 2025 | [F] XS-001, XS-004, XS-006, XS-009; [F]/[C] XS-010, XS-055 |
| Sibling | CA16: 2D/2.5D only, flip chip and wafer bumping; Fab version with EFEM for 300 mm wafers; launch date not disclosed | [F] XS-028..XS-032 |
| Predecessor | FF70 CL / FF65 CL / FF65 IL laminography (2019, with Nagoya Electric Works) | [S] XS-066 |
| Resolution / voxel | "resolution of less than 1 µm"; defect classes <1 µm / <50 µm / <1 mm. **Voxel size: NOT DISCLOSED** | [C] XS-002, XS-014 |
| Field of view | Detector 130 x 130 mm (1536 px, 85 µm pitch, 40 fps), nanofocus source, oblique ±65°, envelope 435 mm. **FOV at a given resolution: NOT DISCLOSED** | [C] XS-011, XS-012 |
| Time per wafer / site | "within minutes"; "defects in seconds"; a Comet Taiwan blog (29 Oct 2026, system not named) shows a 4-minute 3D TSV cycle vs a 60-minute reference. **Wafers per hour: NOT DISCLOSED** | [C] XS-008, XS-040, XS-026, XS-027 |
| Automation | Fab version: EFEM loader, automatic defect classification, integration with fab material/information flows; KLARF/json/xml output; in-cabinet conditions "comparable to ISO Class 3". **SECS/GEM: NOT DISCLOSED** | [C] XS-015..XS-019 |
| 300 mm wafer handling | Stated only for CA16; the CA20 page has a Wafer Manager but no wafer diameter | [C] XS-029, XS-021 |
| Defect-recognition software | ADR/ADC for solder bumps; CoS Insights / CoS Insights X 3D "powered by Dragonfly"; DirectInspect / ProInsight Studio / Dragonfly 3D World (CMD 2025). Dragonfly comes from ORS (acquired Dec 2020) | [C] XS-034, XS-019, XS-020, XS-038, XS-039; [F] XS-037 |
| Source | CA20 machines "equipped with Comet IXM's advanced x-ray tubes"; which tube (FXE or FYNE): NOT DISCLOSED | [F] IXM-011; [C] XS-035 |
| **Dose to memory** | Dose Manager computes dose from tube power and distance and "switches off the X-ray automatically once the dosage limit is reached" to protect "flash and DRAM memories"; Dose Reduction Kit (collimator + 4 filters); Dragonfly deep learning to use "low dose" scans; Oct 2026 blog: a full-resolution 3D volume at a non-damaging dose takes too long for in-line use, hence single-frame low-dose acquisition. **No dose value, no default limit, HBM and NAND not named** | [C] XS-022..XS-025, XS-027 |

---

## 3. Q2 - Adoption

**(a) Comet's own words** (chronological; all [C] unless marked)

| Date | Statement | Id |
|---|---|---|
| Mar 2023 (FY2022 AR) | Advanced-packaging collaboration "with a leading company in this space is exceeding expectations" | XS-041 |
| Nov 2023 (CMD 2023) | "Increased installed base at semiconductor market leader: our co-creation partner" | XS-042 |
| 2023 baseline (CMD 2025 deck) | 5 evaluations, 2 qualifications, **0 orders** | XS-052 |
| Mar 2025 (FY2024 AR) | "first purchase order for the CA20" [F] | XS-045 |
| Jul 2025 (H1 2025 deck) | "market adoption remains delayed" | XS-048 |
| Oct 2025 (Q3 TU) | "a handful of purchase orders ... from various customers" | XS-049 |
| 13 Nov 2025 (CMD 2025) | >80 active collaborations; >60 evaluations, >25 qualifications, **5 orders**; co-creation with "OSAT, IDM, foundry leaders"; CA20 above break-even by 2028e | XS-050, XS-051, XS-053, XS-056 |
| Mar 2026 (FY2025) | "First commercial sales of CA20 systems" [F]; "double-digit million investments" in CA20 | XS-057, XS-058 |
| Jul 2026 (H1 2026) | "more than doubling the number of purchase orders for the CA20"; deck: "compared to YE25"; new models; break-even "still projected for 2028" | XS-059, XS-060, XS-033 |
| Oct 2026 (Q3 TU) | "Strong order momentum, additional customer engagements and successful qualifications" (no count) | XS-061 |

- Customer types named by Comet: OSAT, IDM, foundry [C] (XS-053). Memory makers are not named separately (IDM would cover them).
  No research lab is named as a customer.
- Production vs FA vs evaluation: Comet maps CA20 Lab to failure analysis and CA20 Fab to process control [C] (XS-054); the
  2025 funnel is mostly evaluation and qualification [C] (XS-051). **The lab/fab split of orders and whether any unit runs in
  high-volume production: NOT DISCLOSED.**
- Implied cumulative POs at 30 Jun 2026: at least 11 if the Nov 2025 count of 5 is the base [I] (XS-072, Low - Comet gives no
  base number).

**(b) Customer-side and third-party evidence**

| Item | What it shows | Tag / id |
|---|---|---|
| Resonac JOINT3 consortium release lists Comet Yxlon GmbH among 27 members | Membership in a panel-level interposer consortium; not a purchase | [F] XS-063 |
| Trade press (3D InCites, Silicon Semiconductor, BINDT, OneStopNDT, Semiconductor Packaging News) | Reprints of Comet releases; no customer named | [S] XS-064, XS-065 |
| Dragonfly HBM micro-bump "spotlight" on Comet's site | Study by Excillum authors on an Excillum nano-CT, analysed in Dragonfly; **not CA20 data** | [S] XS-068 |
| SMTA WLP 2024 paper and HKUST slides | Comet Yxlon-authored | [C] XS-069, XS-070 |

**No customer-side evidence of CA20 use was found** after searches combining CA20/Comet Yxlon with SK hynix, Samsung, TSMC,
Micron, ASE, Amkor, imec, Fraunhofer and ECTC/EPTC/IRPS/ISTFA (gaps.md).

---

## 4. Q3 - Rivals for the same sockets

Condensed; the full 15-row comparison with every cell tagged is in `parts/RV_notes.md`.

| System (maker) | Status | Resolution / voxel | Time per wafer / site | Automation / 300 mm | Defect software | Dose to memory | Lab vs in-line | Adoption: company [C] vs third party |
|---|---|---|---|---|---|---|---|---|
| CA20 (Comet Yxlon) | Lab 2023, Fab 2024 [F] | <1 µm [C] | "minutes" [C] | EFEM, ADC; 300 mm not stated [C] | Dragonfly-based ADR [C] | Dose Manager, flash/DRAM, no figure [C] | both | 5 orders Nov 2025 [C]; no third-party |
| ZEISS NLX-100 / 100M | shown Jul-Oct 2026 [F] (RV-017..019) | ND | ND ("high-throughput") | EFEM, 300 mm [C] (RV-010, RV-011) | ZEISS INSPECT X-Ray, AI segmentation [C] | X-Guard shielding, no figure [C] (RV-013) | in-line / near-line | none named; Yongin unit is a demo tool [F] (RV-019) |
| ZEISS Xradia Versa / VersaXRM 5 Insight / Context | VersaXRM 5 Insight 14 Sep 2026 [F] | 0.8 µm/voxel on 30 µm bumps [C] | ~1.5 h per package scan [C] (RV-023) | lab, no wafer handling | ND | ND | lab / FA | ND |
| Nordson XM8000 / XM8000Pro | SEMICON West Oct 2025 / Oct 2026 [C] | "micron scale" / "sub-micron" [C] | "production-speed", no number [C] (RV-037) | wafer- and panel-level; 300 mm ND | ND | "IC-Safe" (snippet, page refused) [S] (RV-042) | in-line metrology | no customer; FQ4 FY2025 fewer x-ray deliveries [F] (RV-040) |
| Nordson X-Plane Pro / Micro CT / Quadra 7 Pro | 2026 [C] | ND | ND | Quadra manual | ND | "reducing radiation exposure" [C] | FA and high-throughput 2.5D | Nordson: "can't spend an hour inspecting every chip" [S] (RV-041) |
| Sigray (Applied) Apex XCT-300 / XCT-in-Line | "Coming Soon" Aug 2024 [C] | 0.5 µm / <0.3 µm voxel [C] (RV-050) | up to 10 WPH site inspection; 2-3 min per spot [C] (RV-054, RV-055) | EFEM, FOUP, SECS/GEM, 300 mm [C] | ML wet/non-wet [C] | ND | lab + in-line | "multiple POs" [C] (RV-053); shipment ND |
| Sigray Apex Hybrid | Apr 2025 (lead) | 350 nm [C] | ND | 300 mm laminography, manual [C] | ND | ND | lab / FA | ND |
| Rigaku | in-line imaging "developing" [C] (RV-024) | ND | ND | ND | ND | ND | planned | ONYX 3200 (not imaging) shipped to "a major global foundry" [C] |
| Bruker X200 | page gone [C] | 2.8 µm/pixel [S] | 1-2 wafers/h [S] (RV-045) | 300 mm [S] | ND | ND | in-line 2D | current packaging X-ray = µXRF [C] |
| Omron VT-X950 | from Feb or Dec 2024 (sources conflict) [S] | NR | "without stopping" [C] | conveyor, no EFEM [C] | deep learning [C] | ND | in-line package/W2W | ND |
| Viscom iX7059 One | ND | down to 1 µm [C] | ND | panel format | ND | ND | in-line AXI | ND |
| SEC NF120 (Korea) | since 2012 [S] | 0.2 µm (distributor) [S] | ND | manual, 12-inch table [S] | ND | HBM damage-reduction patent [S] (RV-072) | manual tool on production lines | **Micron HBM line since 2023; 8 units 2025; KRW 1.8bn (Feb 2026) and 5.8bn (Nov 2026) Micron orders** [S] (RV-066..068, RV-071) |
| SEC Semi-Scan (in-line) | alpha tests from Apr 2026 [S] | 3-5 µm defects [S] | ND | in-line [S] | ND | as above | in-line HBM/WLP/TGV | first OSAT WLP contract Oct 2026; HBM version in validation, earliest order Q1 2027 [S] (RV-069, RV-071) |
| XAVIS Xscan-9860A (Korea) | SEMICON Korea Feb 2026 [C] | 0.25 µm [C] | ND | EFEM, OHT cassette [C] | AI, 2D/3D + fast CT [C] | "dose reduction technology" [C] (RV-077) | in-line WLP | ND |
| Unicomp (China) packaging CT | in customer validation [F] (RV-078) | "sub-micron" source [C] | ND | "in-line integration" [C] | ND | ND | in-line (claimed) | no orders stated [F] |

Added beyond the prompt: Omron, Viscom, XAVIS, SEC, Unicomp; **SFA Engineering (Korea)** is building an in-fab HBM/TGV
X-ray tool on an Excillum NanoTube N3 source (demo system 2026) [F] (IXM-027). No wafer-level HBM 3D X-ray product was found for
Zhengye, Nikon, Hitachi High-Tech, Waygate, Saki, Lumafield, Xwinsys, KLA, Nova, Camtek or Toray (gaps.md).
No maker states a resolution together with a time per 300 mm wafer for the same configuration; Sigray comes closest [C] (RV-051, RV-054).

---

## 5. Q4 - X-ray modules (IXM)

**Who buys Comet sources.**
- Comet names markets, not customers; IXM customer concentration is NOT DISCLOSED [F] (IXM-010). FY2025 IXM external sales:
  NDT CHF 60.3m, Security 15.4m, Others 13.4m [F] (IXM-009).
- Internal: IXM sold 10.0% of its total sales to other Comet segments in FY2025 and 11.2% in H1 2026 (12-17% in FY2020-FY2024)
  [I] (IXM-007, Medium); CA20, FF35 CT and UX20 systems carry IXM tubes [F] (IXM-011..IXM-013).
- Named external buyers, all industrial NDT / battery / castings / aerospace / steel, all from Comet's own pages except Waygate:
  diondo, IMS, North Star Imaging, Pinnacle, X-RIS [F] (IXM-015..IXM-020); Waygate offers the Comet iXRS 450 MF on its
  Phoenix V|tome|x C450 [S] (IXM-021, IXM-022).
- **No semiconductor inspection-system maker was found stating it uses a Comet source.** Waygate Nanotom HR, Rigaku CT Lab HR160
  (Sep 2026), SFA (in-fab HBM/TGV) and TechValley use Excillum [F] (IXM-023, IXM-026..IXM-028); Nikon, Zeiss (ZXR-1, Jan 2026),
  Viscom, Nordson DAGE (QuadraNT) and SEC build their own [F]/[S] (IXM-029..IXM-033). Comet's generic claim that its modules
  "are deployed by leading foundries, IDMs ... OSATs" names nobody [C] (IXM-036).

**Roadmap vs Excillum and in-house sources** (full table in `parts/IXM_notes.md`)

| Source | Maker | Best stated resolution / spot | Power | Note | Tag / id |
|---|---|---|---|---|---|
| FYNE 160 NF4 (open nanofocus) | Comet | 400 nm at 160 kV | ND | "up to 4x usable dose" at 400 nm; >2,600 h life; launched Feb-Apr 2025; aimed at HBM/GPU bumps, TSV | [C] IXM-056..IXM-060 |
| FYNE NF12 | Comet | 1.1 µm | ND | "up to 10x dose" | [C] IXM-058 |
| FXE-190 nano CT | Comet | 0.45 µm (1.4 W) | to 30 W | Jul 2025 | [C] IXM-053 |
| NanoTube N3 | Excillum | 150 nm lines/spaces | 16.6 W | in SFA, Rigaku, Waygate systems | [F] IXM-063 |
| MetalJet E1+ / F1016 | Excillum | <10 µm / 30 µm | 1,000-1,600 W | liquid-metal jet; Comet has no disclosed counterpart | [F]/[C] IXM-065, IXM-066 |
| L10711-26 | Hamamatsu | 0.2 µm | 9.6 W (W mode) | merchant open tube | [F] IXM-069 |
| ZXR-1 | Zeiss (in-house) | VersaXRM 730 <450 nm system | 25 W | Jan 2026 | [F] IXM-030, IXM-071 |
| QuadraNT | Nordson DAGE (in-house) | "sub 0.1 µm feature recognition" (claimed) | ND | sealed | [S] IXM-032 |
| CT Lab HR160 source | Excillum inside Rigaku | 250 nm system | ND | Rigaku buys rather than builds this one | [F] IXM-026 |

Reading [I] (IXM notes, Medium): Comet's best figures (0.4-0.45 µm) are coarser than the finest merchant nanofocus figures and
close to Zeiss's in-house source; the metrics differ by maker, so this is not like-for-like. Comet's pitch is dose at a given
resolution and lifetime, not ultimate resolution. Comet ranked itself #4 in open micro focus and #3 in open nano focus [C] (IXM-038).

---

## 6. Q5 - X-ray systems division (IXS) economics

| Half-year | IXS sales | IXS EBITDA | EBITDA % | IXS EBIT | Source |
|---|---|---|---|---|---|
| H1 2022 (Jan-Jun 2022) | 60.0 | -1.6 | -2.6% | -4.2 | [F] DV segment note |
| H2 2022 (Jul-Dec 2022) | 70.4 | 3.2 | 4.5% | 1.1 | [I] FY-H1 |
| H1 2023 | 56.8 | 0.2 | 0.3% | -2.0 | [F] |
| H2 2023 | 60.2 | 4.8 | 7.9% | 2.6 | [I] |
| H1 2024 | 55.2 | -1.9 | -3.5% | -4.1 | [F] |
| H2 2024 | 60.7 | -2.4 | -3.9% | -4.8 | [I] |
| H1 2025 | 48.7 | -7.5 | -15.4% | -9.6 | [F] |
| H2 2025 | 62.1 | 0.0 | 0.0% | -2.0 | [I] |
| H1 2026 (Jan-Jun 2026) | 48.7 | -4.0 | -8.2% | -5.8 | [F] DV-040 |

(Script `calc/DV_halfyears.py`; ids DV-001..DV-068. IXS figures were not affected by the restatement.)

- **Orders**: IXS orders and book-to-bill are NOT DISCLOSED by division; Q3 2026: IXS sales "slightly lower" than Q3 2025,
  orders and backlog up in all divisions [F] (DV-158, DV-159).
- **Semiconductor share**: Comet publishes no IXS semiconductor or CA20 share. Its "Electronics" end-market share of IXS sales
  fell from 44.7% (2022) to 36.0% (2025) while automotive rose to 37.9% [F] (DV-073..DV-077; read from annual-report pie charts,
  Medium).
- **Restructuring steps**: portfolio streamlining 2021-22 [C]; exit from "less profitable volume business" FY2022 [F] (DV-100);
  ORS integrated into IXS H1 2023 [F] (DV-101); low-margin products discontinued H1 2024 [F] (DV-103); organisational adjustments
  and workforce reduction decided Jul 2025 [F] (DV-105, DV-106); restructuring programme at IXS Hamburg in Q3 or Q4 2025 - Comet's
  documents disagree on the quarter [F] (DV-111, DV-112, DV-116). **Cost and headcount: NOT DISCLOSED.** No IXS goodwill
  impairment (CHF 19.9m at YE2025) [F] (DV-092..DV-094); the YE2024 test assumed 17.4% p.a. IXS sales growth for 2025-2027 vs
  actual 2025 -4.4% [F]/[I] (DV-093).
- **CA20 cost**: CHF 10-15m in 2024 [C] (DV-086); "double-digit million" in FY2025 [F] (DV-085). Without the 2024 CA20 spend
  IXS FY2024 EBITDA margin would have been roughly 4.9-9.2% instead of -3.7% [I] (DV-072, Medium, illustration only - Comet does
  not call it a one-off).
- **Every statement on strategic direction** (chronology with quotes in `parts/DV_notes.md` section 3): repositioning (CMD 2021,
  2022) [C]; "serve legacy opportunistically" (CMD 2023) [C] (DV-102); "restructuring non-semi IXS", "Turnaround or phasing-out
  unprofitable activities, especially non-Semi", "Downsizing low-profitability businesses, right-sizing cost base, CA20"
  (CMD 2025) [C] (DV-108..DV-110); a "comprehensive strategic review in 2025" that reaffirmed the core focus and a product-line
  review with "focused actions, rather than large structural exits" (AR2025) [C] (DV-113, DV-114); "remains committed to its
  strategy of downsizing low-margin businesses, right-sizing costs, and focusing on the CA20 platform" (H1 2026) [C] (DV-117);
  "confidence in sustained growth for IXS in the semiconductor market" (Q3 2026) [C] (DV-118). **No statement on a sale,
  partnership or "strategic options" for IXS was found.**

---

## 7. Module A - numbers

### A1 Results

| CHF m | H1 2025 restated (Jan-Jun 2025) | H2 2025 derived | FY2025 (Jan-Dec 2025) | H1 2026 (Jan-Jun 2026) |
|---|---|---|---|---|
| Net sales | 227.2 [F] | 229.9 [I] | 457.0 [F] (A-010) | 239.8 [F] (A-001) |
| YoY | +20.0% | -10.2% [I] | +2.6% (+7.3% cc) | +5.6% (+12.7% cc) |
| Gross margin | 39.5% | 36.5% [I] | 38.0% [F] | 41.4% [F] |
| EBITDA margin reported | 10.1% | 10.2% [I] | 10.1% [F] (A-013) | 13.1% [F] (A-004) |
| EBITDA margin ex one-offs named by management | 10.1% (none) | 9.2% ex CHF 2.1m fire-insurance recovery [I] | 9.7% [I] | 15.0% ex CHF 4.5m Penang/efficiency costs [I] (A-219) |
| EBIT margin | 5.4% | 5.4% [I] | 5.4% [F] | 8.5% [F]; 10.4% ex one-offs [I] |
| Free cash flow | 1.3 | 7.2 [I] | 8.5 [F] | -19.3 [F] |
| Share-based compensation | 0.37 | 1.05 [I] | 1.42 [F] | 0.67 [F] |

Quarters (sales and orders only; Comet publishes no quarterly profit): Q3 2025 102.5 / orders 102.1; Q4 2025 127.4 [I] / 129.9;
Q1 2026 106.3 / 144.9; Q2 2026 133.5 / 209.9 [I]; **Q3 2026 (Jul-Sep 2026) 155.6 (+51.9%) / 275.6, book-to-bill 1.77** [F]
(A-040..A-052). LTM to Sep 2026 net sales CHF 522.8m (+10.6%) [I] (A-226).

Segments FY2025 total sales: PCT 257.1, IXS 110.8, IXM 99.1, eliminations -10.0 [F] (A-034).
**Theme share**: the only line labelled "Semiconductor" is PCT's CHF 241.5m = 52.8% of FY2025 sales; adding IXS "Electronics"
gives 61.6% [F]/[I] (A-036, A-037, A-238). Comet's own "Semi / Electronics" share was 57% of FY2022 sales with ">80%" targeted
at the next peak [C] (A-038). **AI / HBM / advanced-packaging share: NOT DISCLOSED** - only qualitative statements [C] (A-039).

### Results by division, each half-year since 2022 (CHF m; EBITDA margin on total division sales)

| Half | PCT sales | PCT EBITDA % | IXS sales | IXS EBITDA % | IXM sales (ext.) | IXM EBITDA % | Group sales | Group EBITDA % |
|---|---|---|---|---|---|---|---|---|
| H1 2022 | 173.5 | 19.8 (25.0 ex XP legal) | 60.0 | -2.6 | 41.0 (34.3) | 15.0 | 267.5 | 14.1 |
| H2 2022 [I] | 208.0 | 34.0 | 70.4 | 4.5 | 47.7 (40.7) | 20.0 | 318.9 | 25.5 |
| H1 2023 | 106.8 | 5.3 | 56.8 | 0.3 | 50.8 (43.5) | 20.4 | 207.0 | 6.9 |
| H2 2023 [I] | 86.4 | 15.1 | 60.2 | 7.9 | 49.4 (44.0) | 27.2 | 190.4 | 16.1 |
| H1 2024 | 94.3 | 9.7 | 55.2 | -3.5 | 46.5 (39.9) | 15.7 | 189.3 | 6.9 |
| H2 2024 restated [I] | 153.1 | 26.9 (28.5 as first reported) | 60.7 | -3.9 | 48.1 (42.2) | 15.1 | 256.0 | 17.6 (18.5) |
| H1 2025 restated | 134.3 | 17.4 (15.8 as first reported) | 48.7 | -15.4 | 48.4 (44.2) | 17.2 | 227.2 | 10.1 (9.1) |
| H2 2025 [I] | 122.8 | 13.8 | 62.1 | 0.0 | 50.7 (44.9) | 14.7 | 229.9 | 10.2 |
| H1 2026 | 143.6 | 20.2 | 48.7 | -8.2 | 53.5 (47.5) | 16.1 | 239.8 | 13.1 |

[F] for H1 periods (segment notes, DV-001..DV-040); [I] for H2 (FY minus H1, `calc/DV_halfyears.py`). One-offs named by
management: XP Power trial cost CHF 9.0m in H1 2022 (PCT) [F] (DV-041); unquantified H1 2023 cost-reduction and San Jose closure
costs (PCT) [F] (DV-045, DV-046); FY2025 fire-insurance recovery ~CHF 2.1m (segment not stated) [F] (DV-049); H1 2026 one-time
costs CHF 4.5m (Penang ramp + efficiency programme; split not given) [F] (DV-051). Trading-update quarters carry only qualitative
divisional statements (table in `parts/DV_notes.md`); the 2022-2024 Q1/Q3 updates are cited from newswire copies [S] (DV-160..162).

### Plasma control: concentration, profit share, share vs AE/MKS

- **Largest customer** (unnamed, PCT): CHF 104.4m = 22.8% of FY2025 group sales (FY2024 23.8%; FY2023 17.7%; FY2022 36.1%;
  FY2021 30.4%) [F] (A-120..A-123, DV-119..DV-123) = 37-55% of PCT sales [I] (DV-124). No second customer above 10% is reported.
  Comet's deck: etch ~80% held by the top three OEMs, deposition ~70% by the top two [C] (DV-133). Lam Research appears as a PCT
  customer only in a search snippet [S] (DV-163, Low); which OEM is the largest customer is NOT DISCLOSED.
- **PCT share of group EBITDA** per half: 91%, 87%, 40%, 42%, 70%, 92%, 102%, 73%, 92% (H1 2022 ... H1 2026) [I] (DV-069).
  PCT semiconductor share of PCT sales 90.6-94.1% (2022-2025) [F] (DV-077, DV-078; chart reads, Medium).
- **Share vs Advanced Energy and MKS** (company words only): CMD 2023 lists AE and MKS as competitors in matchboxes and RF
  generators [F] (DV-125); "#1" with "~40%" in matchboxes and "~70%" in vacuum capacitors [C] (DV-126, DV-127); Synertia RF
  generator share target "~10%" by 2025 (CMD 2022) [C] (DV-128) - the share achieved is NOT DISCLOSED; by Nov 2025 Synertia RFG had
  >50 evaluations, >30 qualifications, 15 HVM orders [C] (DV-132); "market share gains" claimed in H1 2025 and Q3 2026 [C] (DV-131,
  DV-136). **No share loss is stated anywhere; no third-party share evidence (AE/MKS filings, analysts) was retrieved.**

### Mid-term targets (CMD 2025, 13 Nov 2025) vs results

| Target | Horizon | Latest actual | Gap | Ids |
|---|---|---|---|---|
| Net sales CHF 670-770m | next peak, 2028e | FY2025 457.0; LTM Sep 2026 522.8; FY2026 guide 570-590 | needs 13.6-19.0% CAGR 2025-28 [I] | DV-137, DV-149 |
| EBITDA margin 22-27% | 2028e | FY2025 10.1%; LTM Jun 2026 11.7%; FY2026 guide 17-19% | +10.3 to +15.3 pp vs LTM [I] | DV-138, DV-150 |
| ROCE 27-32% | 2028e | FY2025 5.2% [F] | +21.8 to +26.8 pp [I] | DV-139, DV-147 |
| PCT 430-480m at 27-33% | 2028e | LTM 266.4 at 17.2% | 18.7-23.1% sales CAGR needed [I] | DV-141, DV-142, DV-151 |
| IXS 130-160m at 5-9%; CA20 > break-even | 2028e | LTM 110.9 at -3.6% | +8.6 to +12.6 pp [I] | DV-087, DV-141, DV-142 |
| IXM 110-130m at 23-27% | 2028e | LTM 104.2 at 15.4% | +7.6 to +11.6 pp [I] | DV-141, DV-142 |
| (CMD 2023) 800-900m, 25-30%, ROCE 30-35% | peak then seen 2027 | replaced Nov 2025 | sales midpoint cut 15.3% [I] | DV-144, DV-152 |
| (2019) >830m, ~25%, ~30% | FY2025 | 457.0 / 10.1% / 5.2% | missed by CHF 373m / 14.9 pp [I] | DV-145 |

Comet's explanation of the Nov 2025 cut: "essentially unchanged in constant currencies", USD/CHF 0.70 (was 0.90), slower product
introductions, peak moved to 2028 [C] (DV-140). The CMD 2025 baselines use FY2024 as first reported, not restated [I].

### A2 Leading signals

- Orders: H1 2026 CHF 354.8m, book-to-bill 1.48; Q3 2026 CHF 275.6m, 1.77 [F] (A-047, A-048, A-051, A-052). Backlog CHF 125.4m at
  YE2025 (140.7m YE2024) [F] (A-062); half-year and quarter-end backlog NOT DISCLOSED; "significant share ... scheduled for
  delivery well into 2027" [C] (A-053).
- Inventory YE2025: raw 57.9m / WIP 11.9m / finished 19.7m (65/13/22%), total 89.5m [F] (A-068..A-070); 30 Jun 2026 total 113.7m
  (+27%), no split [F] (A-074); inventory days 148 vs 136 a year earlier [I] (A-231). Write-downs CHF 4.3m FY2025 vs 8.5m FY2024 [F] (A-071).
- Contract liabilities CHF 21.2m at 30 Jun 2026 (14.3m YE2025) [F] (A-077). Receivables CHF 78.6m, DSO 59 days at 30 Jun 2026 vs
  50 a year earlier [F]/[I] (A-081, A-232). Purchase obligations CHF 33.4m at YE2025 (63.2m YE2022) [F] (A-084, A-085).

### A3 Guidance record

| FY | Initial | Last before results | Result | vs initial | vs last |
|---|---|---|---|---|---|
| FY2022 | 570-610 / 21-23% [F] | confirmed 20 Oct 2022 [S] | 586.4 / 20.3% (21.8% company-adjusted) | in-line / miss | in-line / miss* |
| FY2023 | 440-480 / 13-15% (Apr 2023) [S] | 380-400 / 7-9% (Oct 2023) [S][F] | 397.5 / 11.3% | miss / miss | in-line / beat |
| FY2024 | 440-480 / 15-17% [F] | "lower end" Oct 2024 [S] | 445.4 / 13.6% (13.0% restated) | in-line / miss | in-line / miss* |
| FY2025 | 480-520 / 17-20% [F] | 460-500 / 10-14%, "lower end" Oct 2025 [F] | 457.0 / 10.1% | miss / miss | miss* / in-line |
| FY2026 | qualitative (Mar 2026) | 570-590 / 17-19% reported (Oct 2026) [F] (A-116) | results 5 Mar 2027 | - | - |

Count FY2022-FY2025 (8 items): vs initial **0 beats / 2 in-line / 6 misses**; vs last guidance 1 / 4 / 3 [I] (A-242).
\* Guidance maintained late in the period and then missed: FY2022 margin, FY2024 margin, FY2025 sales (CHF 457.0m vs the 460m
floor reaffirmed in October) [I] (A-243). FY2026's October range implies Q4 2026 sales of CHF 174.5-194.5m vs 155.6m in Q3 [I] (A-244).

### A4 Concentration, geography, export rules, changed figures

- One customer above 10% (above). Regions FY2025: Asia 289.8 (63.4%), of which China 114.6 (25.1%), Malaysia 71.2, Japan 18.7,
  rest of Asia incl. Korea/Taiwan 85.3; North America 81.6; Europe 78.2 [F] (A-125..A-131). China share: 18.1% (2022), 27.2%
  (2023), 27.0% (2024), 25.1% (2025) [I] (A-235). Half-year reports give no China, Korea or Taiwan figure.
- Export controls: Comet monitors "US export restrictions on the supply of semiconductor equipment to certain Chinese customers"
  [F] (A-140); latest wording "only affected to a limited extent" [C] (A-143). Quantified effect: NOT DISCLOSED.
- **Prior-period figures that changed**: H1 2025 EBITDA 20.7m (9.1%) -> 23.0m (10.1%) and FY2024 EBITDA 60.4m (13.6%) -> 58.0m
  (13.0%), explained (note 01.1 / AR2025 note 2.3) [F] (A-023..A-030); FY2025 deck's H2 2025 margin mixes bases (unexplained) [I]
  (A-215); **Q3 2025 orders 104.5m implied in Oct 2025 vs 102.1m shown in Oct 2026 - unexplained** [I] (A-228); Q1 2024
  book-to-bill 1.09 vs 1.12 - unexplained, small [I] (A-229); IXS 2021 market split changed between AR2021 and AR2022 - unexplained
  (DV notes).

### A5 Balance sheet and capital

- 30 Jun 2026: cash CHF 69.8m; CHF 60m 2.00% bond (issued Apr 2026, due 18 Apr 2031) replacing the 1.30% bond repaid 20 Apr 2026;
  leases 29.4m; **net debt CHF 19.3m incl. leases** (net cash 10.1m excl. leases); equity ratio 60.4% [F]/[I] (A-148..A-156, A-239).
- RCF CHF 100m (since Jun 2025), undrawn, five years from Apr 2023; covenant leverage max 3:1, complied FY2025 [F] (A-157, A-158).
  No convertibles [F] (A-249). No buybacks; dividends 3.50 / 3.70 / 1.00 / 1.50 / 0.50 per share for FY2021-FY2025 [F] (A-164).
- M&A last five years: none [F] (A-168..A-171). ORS (31 Dec 2020) CHF 8.98m, goodwill 4.71m, never impaired [F] (A-172..A-180).
- XP Power: USD 40m jury award (2022) plus ~USD 19m fees/interest (Jan 2025) never booked; on 14 Jul 2026 the Ninth Circuit vacated
  the judgment and ordered a new trial [F] (A-182..A-187); Comet: "not expected to have a material impact" [C] (A-188).

### A6 Cycle

| Downturn | Peak -> trough | Net sales | EBITDA margin | Id |
|---|---|---|---|---|
| 2018-19 | H1 2018 (Jan-Jun 2018) -> H1 2019 (Jan-Jun 2019) | -23.8% | 13.8% -> 4.8% | [I] A-245 |
| 2022-24 | H2 2022 (Jul-Dec 2022) -> H1 2024 (Jan-Jun 2024) | -40.6% | 25.5% -> 6.9% | [I] A-246 |
| 2024-25 soft patch | H2 2024 -> H1 2025 | -11.3% | 17.6% -> 10.1% | [I] A-247 |

Q3 2026 sales (155.6) are still 5.6% below the Q3 2022 peak quarter [I] (A-248). The 2009 downturn could not be measured (gaps.md).

---

## 8. Module B - close

### B1 Disputed-claims ledger

| Claim | Who said it, when | Evidence for | Evidence against | Strongest tag on each side |
|---|---|---|---|---|
| 1. 3D X-ray moves from the failure-analysis lab into in-line production for HBM and CoWoS-type packages | Comet (CA20 Fab launch Nov 2024; CMD 2025 "lab to fab"); rivals' in-line launches 2024-2026 | CA20 Fab with EFEM/ADR [F] (XS-006); funnel >60 eval / >25 qual / 5 orders [C] (XS-051); POs "more than doubled" H1 2026 [C] (XS-059); in-line tools announced by ZEISS, Nordson, Sigray/Applied, XAVIS [C] (RV-010, RV-037, RV-055, RV-076); SFA in-fab HBM/TGV demo on Excillum source [F] (IXM-027); manual SEC NF120 on Micron HBM line since 2023, 8 units in 2025 [S] (RV-066, RV-071) | No customer-side evidence of a CA20 in production; lab/fab split of orders not disclosed (gaps); Comet: "market adoption remains delayed" (Jul 2025) [C] (XS-048); ZEISS NLX only a demo unit [F] (RV-019); Sigray XCT-300 "Coming Soon" (Aug 2024) [C] (RV-055); Nordson: fewer x-ray deliveries FQ4 FY2025 [F] (RV-040) and "can't spend an hour inspecting every chip" [S] (RV-041); SEC's in-line HBM tool still in validation, order no earlier than Q1 2027 [S] (RV-071) | For: [F] (launches; SFA demo) - but production use only [S]. Against: [F] |
| 2. X-ray dose is a manageable problem for memory | Comet (Dose Manager text, 2023-2026); ZEISS, XAVIS, SEC (dose-reduction claims) | Dose Manager stops at a limit for flash/DRAM [C] (XS-022); Dose Reduction Kit [C] (XS-024); X-Guard [C] (RV-013); XAVIS "dose reduction technology" [C] (RV-077); SEC HBM damage-reduction patent [S] (RV-072); manual X-ray tools in use on an HBM production line [S] (RV-066) | No maker publishes a dose number or limit (gaps); HBM and NAND never named in Comet's dose text [C] (XS-022); Comet's Oct 2026 blog: a full 3D volume at a non-damaging dose takes too long for in-line use [C] (XS-027); trade press calls HBM overexposure "a significant concern" [S] (RV-049); no peer-reviewed dose-damage data retrieved (gaps) | For: [C]. Against: [C]. No [F] on either side |
| 3. The X-ray systems division reaches the group's margin target (22-27% EBITDA, 2028e) | Implied by group target, CMD 2025 | H1 2026 IXS EBITDA margin improved to -8.2% from -15.4% after Q4 2025 restructuring [F] (DV-040, DV-116); CA20 break-even targeted 2028 [C] (DV-091) | Comet's own 2028 IXS target is 5-9% EBITDA [C] (DV-142); IXS EBITDA negative in 5 of 9 half-years since 2022, best 7.9% (H2 2023) [I] (DV-055..068); LTM -3.6% [I] (DV-151); IXS share of group sales at peak cut to 15-25% [C] (DV-143) | For: [F] (improvement only). Against: [C] company target + [F] segment history |
| 4. Comet keeps the X-ray systems division | Comet, AR2025 (Mar 2026), H1 2026 (Jul 2026), Q3 2026 TU (Oct 2026) | "focused actions, rather than large structural exits" [C] (DV-114); "remains committed to ... focusing on the CA20 platform" [C] (DV-117); 2028 IXS targets set at CMD 2025 [C] (DV-141); no "strategic options"/sale/partner wording found in any saved document (DV notes); IXS goodwill not impaired [F] (DV-094) | "Turnaround or phasing-out unprofitable activities, especially non-Semi"; "restructuring non-semi IXS" [C] (DV-108, DV-109); losses as in row 3 [F]/[I]; "comprehensive strategic review in 2025" [C] (DV-113) - outcome stated only in company words | For: [C]. Against: [C] (+[F] losses). Forward-looking; no document can settle it |
| 5. The CMD 2025 targets (CHF 670-770m, 22-27% EBITDA in 2028) are reachable | Comet, CMD 13 Nov 2025 | Q3 2026 orders 275.6m, book-to-bill 1.77; FY2026 guidance raised to 570-590m / 17-19% [F] (A-051, A-052, A-116); efficiency programme CHF 20-30m EBITDA from 2028 [C] (DV-053) | 2019 targets for 2025 missed by CHF 373m and 14.9 pp [C]/[I] (DV-145); CMD 2023 targets cut in Nov 2025 [C]/[I] (DV-152); guidance vs initial 0 beats / 6 misses of 8 [I] (A-242); needs 13.6-19.0% sales CAGR [I] (DV-149) | For: [F]. Against: [F]-based [I] record |
| 6. "Sequential EBITDA margin improvement in H2 2025" (9.1% -> 11.1%) | Comet, FY2025 results deck, Mar 2026 | Deck figures [F] (A-031, DV-054) | H1 2025 restated to 10.1% in the H1 2026 report [F] (A-025); consistent-basis H2 2025 = 10.2% [I] (A-215, DV-068) | For: [F] (as printed). Against: [F] restatement + [I] |

### B2 Facts that most weaken each reading

Weaken the optimistic reading:
1. All CA20 adoption evidence comes from Comet; its last order count was **5 orders** at the CMD on 13 Nov 2025 [C] (XS-051),
   and no customer paper or release naming a CA20 user was found [C]/gaps.
2. IXS was still loss-making in H1 2026: EBITDA CHF -4.0m, -8.2% [F] (DV-040); Comet's own 2028 IXS margin target is 5-9% [C] (DV-142).
3. In the high-resolution semiconductor tier, buyers documented in this run use Excillum or in-house sources (SFA in-fab HBM tool,
   Rigaku CT Lab HR160, Waygate Nanotom HR) [F] (IXM-023, IXM-026, IXM-027), and Comet ranks itself #4 in open micro focus and #3
   in open nano focus [C] (IXM-038).

Weaken the pessimistic reading:
1. Q3 2026 orders CHF 275.6m (+170%), book-to-bill 1.77, and FY2026 guidance raised to CHF 570-590m [F] (A-051, A-052, A-116).
2. CA20 purchase orders "more than doubled" vs YE2025 in H1 2026, with >25 qualifications in 2025 and first commercial sales in
   FY2025 [C]/[F] (XS-059, XS-051, XS-057).
3. IXS EBITDA margin improved from -15.4% (H1 2025) to -8.2% (H1 2026) on flat sales after the Q4 2025 restructuring [F]
   (DV-040, DV-116); the CHF 100m credit facility was undrawn at 30 Jun 2026 and the only bond runs to April 2031 [F]
   (A-157, A-153).

### B3 Dated catalysts, next 12 months (Nov 2026 - Nov 2027)

| Date | Event | Tag / id |
|---|---|---|
| 5 Mar 2027 | FY2026 results (test of 570-590m / 17-19% guidance; implies Q4 2026 sales 174.5-194.5m) | [F] B-001; [I] A-244 |
| 15 Apr 2027 | 78th AGM and Q1 2027 trading update; Chairman Benjamin Loh's term runs to this AGM | [F] B-002 |
| Q1 2027 (earliest) | Rival SEC's in-line HBM X-ray tool: first order expected no earlier than Q1 2027 | [S] RV-071 |
| During 2027 | Penang plant "fully operational by 2027" | [C] B-003 |
| End 2027 | Efficiency programme fully implemented (CHF 20-30m EBITDA from 2028) | [C] B-004, DV-053 |
| Late Jul 2027 / Oct 2027 | H1 2027 results; Q3 2027 trading update (dates NOT DISCLOSED; past pattern late July / mid-to-late October) | gaps.md |
| Not dated | XP Power retrial after the Jul 2026 remand (contingent asset ~USD 59m, never booked) | [F] A-186; [I] A-241 |
| Outside window | RCF maturity ~Apr 2028 [I]; CA20 break-even and CMD targets 2028 [C]; bond maturity 18 Apr 2031 [F] (A-153) | |

No lock-ups or regulatory deadlines specific to Comet were found.

### B4 Gap log - see `gaps.md` (83 lines).
### B5 Handoff row - see `handoff.md`.

---

## 9. Data-quality notes

- Six percentages (IXS end-market split, PCT semiconductor share) were read from annual-report charts; only the captions could
  be quoted. They are tagged [F] with Medium confidence and a note.
- Nine downloads were not the documents they were meant to be (seven listing/JS pages deleted; a 212-byte Waygate bot-check page;
  an Elsevier redirect stub). The manifest now marks them NOT RETRIEVED (`calc/manifest_audit.py`); none is cited in evidence.csv.
- 2022-2024 Q1/Q3 trading updates are no longer on comet.tech and the Wayback Machine reset connections; they are cited as [S]
  newswire copies.
- The CMD 2025 deck (142 MB) is not in git (GitHub 100 MB limit); text and sha256 are.
