# Camtek Ltd. (CAMT): products, application mix, HBM and hybrid bonding, competition, orders, Module A fact base and Module B claims ledger

**As of 21 November 2026.** Fiscal year = calendar year. The latest reported quarter is **Q3 2026**: results released and call held on 4 Nov 2026 (6-K; [release PDF](https://cdn.camtek.com/wp-content/uploads/Q32026.pdf)).

**Method.** This report states data only, with no recommendations. Every figure carries a period and a source. Sources are tagged **[CO]** (Camtek-controlled), **[IND]** (independent) or **[CO-relayed]** (a third party repeating Camtek). **DERIVED** marks my own arithmetic and **ESTIMATE** marks a modelled figure. The rules block in `research/CLAUDE.md` is still a placeholder, and the repository does not define "Module A" or "Module B". The stand-ins used here are set out in `README.md` in this folder.

**Evidence base.** Full citations (numbered source lists with URLs) are in `notes/`:

| File | Content |
|---|---|
| `01_products.md` | Q1, product map |
| `02_quarterly_revenue_mix_margin_china.md` | Q2 application mix, geography, gross margin |
| `03_module_a_financials_customers_converts.md` | Module A financials, customers, convertible notes, ownership |
| `04_module_a_china_export_rules.md` | Export rules and China |
| `05_hbm_inspection_steps.md` | Q3, inspection steps per HBM generation |
| `06_hybrid_bonding.md` | Q4, hybrid bonding, including the micro-bump estimate |
| `07_competition_onto_kla_china.md` | Q5, head-to-head competition |
| `08_orders_backlog_capacity.md` | Q6, orders, backlog and capacity |
| `ledger_C1.md` to `ledger_C4.md` | Module B entries |
| `99_gap_fill_and_consistency.md` | Cross-file corrections; it governs where files disagree |

---

## Summary of findings

1. **Products.** Camtek ships three platform families: **Hawk** (launched Feb 2025), **Eagle**, led by **Eagle G5** (launched Sep 2024), and the FRT-derived **MicroProf/NanoProf** metrology line (NanoProf first installs Q1 2026). Hawk and G5 together were ~30% of FY2025 revenue and ~57% of Q3 2026 systems revenue [CO]. Camtek publishes no absolute throughput figure for any main platform, and there is no independent test of its specifications.
2. **Application mix.** Camtek has never published an application table; every split is an approximate figure given on a call. Advanced packaging rose from ~70% of revenue through 2025 to **~80% in Q3 2026**. Camtek has split HBM from chiplet/CoWoS-type revenue only once: **HBM 40% of revenue in Q1 2024**.
3. **HBM steps.** Camtek has **never quantified** inspection steps per HBM generation. Its wording has moved: in May 2024 it said stack height "doesn't change our business"; from Nov 2025 it called HBM4 "inspection and metrology intensive". Independent sources agree that HBM4 makes inspection harder. None counts steps. Onto says HBM4→HBM4E demand is "all about the wafers".
4. **Hybrid bonding.** Camtek sells pre-bond inspection (Hawk at 150 nm) and pre-bond metrology (NanoProf). It has **no post-bond void product**; that item and copper-dishing metrology are on the 2027–28 roadmap. Hybrid-bonding revenue is "low magnitude", with "nothing substantial" expected in 2027 [CO, 4 Nov 2026]. No independent source names Camtek as a hybrid-bonding supplier.
5. **Competition.** No customer document names Camtek as the HBM tool of record. Onto reports a >$240M HBM volume purchase agreement (Feb 2026) and a "displaced tool of record" G5 + 3Di win at an HBM maker (Mar 2026). SK hynix gave Onto a partner award for HBM defect prevention (Sep 2026). An ASE/SPIL procurement filing is the only independent document naming a Camtek purchase at a target account. It covers NT$1.75bn (≈US$54–55M) in Jun–Jul 2026.
6. **Orders.** Camtek reported >$600M of orders year to date at 10 Aug 2026 and >$800M at 14 Oct 2026. Delivery is stated only as "2026 and 2027". Camtek gives no backlog dollar figure, no backlog definition and no cancellation terms. Its "$260M" HBM figure mixes orders with customer forecasts. Every quarter from Q1 2024 to Q3 2026 met or beat revenue guidance.
7. **Module A.**
   - China was 49% of FY2025 revenue and is guided "~45%" for FY2026. Camtek does not give China share by quarter.
   - Camtek tools are likely AT-only **3B992**-class items. The December 2024 BIS FDP rules can reach them when shipped from Israel to Footnote 5 entities, but only if they contain a US-origin IC; Camtek has not said whether they do.
   - One customer took 11% of revenue in 2025. Top-three share is not disclosed; it is bounded at 11%–31%.
   - The 2026 notes were 83.5% repurchased for cash at ~160% of par in Sep 2025 and the rest mostly converted in Q1 2026. $63k remains, due 1 Dec 2026.
   - The $500M 2030 notes convert at $109.34. The stock met the 130% trigger on closing prices in the Q3 2026 test window, by a thin margin.
   - Non-GAAP gross margin has held at 51–52% since Q1 2025. Management blames component costs and the shekel, and has deferred the expected improvement four times.
8. **Module B ledger.**

   | Claim | Verdict | Confidence |
   |---|---|---|
   | C1: HBM4/4E add steps per stack | Partly supported | Medium |
   | C2: Hybrid bonding expands the addressable market | Partly supported | Medium |
   | C3: Camtek holds or gains share against Onto at HBM makers | **Not supported** | Medium |
   | C4: 2026 orders convert on schedule | Partly supported | Medium |

   **Micro-bump handoff cell (ESTIMATE):**
   - About **48.5%** of last-twelve-month (LTM) revenue is tied to bump inspection and metrology of any kind (range 34.5–57.3%).
   - About **10%** is tied to the die-to-die micro-bumps that hybrid bonding would remove (range 5.4–25.8%).

---

## Q1. Product map with production status

### Platforms currently shipping (all [CO]: Camtek website, 20-F FY2025, releases, Oct 2026 investor deck)

| Product | Status (Nov 2026) | Launch | What it inspects / measures | Stated throughput | Stated resolution | Notes |
|---|---|---|---|---|---|---|
| **Hawk** | Volume: "dozens" installed in the year to Feb 2026 | Orders >$50M before launch (27 Nov 2024); launched SEMICON Korea, Feb 2025 | 2D defect inspection; 3D bump height/CD on wafers with >500M bumps; IR overlay | "x2 higher TPT compared to Eagle G5" (condition not stated); IR Gen2 mode **10 WPH @ 1 µm** | Defects **150 nm** (20-F, deck) vs "0.1 µm" (website), a contradiction; bump pitch <10 µm (website) vs <12 µm (20-F); CD <5 µm; IR overlay repeatability <15 nm | CTS Gen 9 white-light triangulation sensor |
| **Eagle G5** | Volume. First shipments Q4 2024 | 24 Sep 2024 (SEMICON Taiwan); $20M initial orders, mainly fan-out 2D | Surface defects, multi-layer RDL, FOWLP, 2.5D, CIS, SiC; bump height/coplanarity (Eagle family) | "2X" vs prior Eagle (condition not stated) | BF 0.5 µm / DF 0.3 µm; 1.4 µm L/S | Clear-Sight Illumination; Eagle "price tag of a million plus" (Q2 2025 call) |
| Eagle-T AP / AP Plus | Shipping, no volume data | Pre-2023 | 2D + 3D: bump height, coplanarity, PR/PI thickness, via depth, RDL | "Ultra high" (qualitative) | Bumps down to 2 µm; >60M bumps/wafer; bump range 2–250 µm | CTS, confocal (CCS), interferometer (CLIP) |
| Eagle-T i / i Plus | Shipping, no volume data | Pre-2023 | 2D surface defects; fan-out RDL; inner cracks after dicing | Inner-crack mode: full wafer <3 min | i: 0.2 µm; i Plus: BF 0.42 / DF 0.3 µm | — |
| Golden Eagle | Shipping, no data | Pre-2023 | Fan-out panel-level packaging | Not stated | BF 0.8 / DF 0.6 µm | Panels up to 650×650 mm |
| **NanoProf** | Initial installs Q1 2026; launched SEMICON Taiwan, Sep 2026 | 2026 | Die/wafer warp, RDL, TSV, pre-bond (hybrid bonding) metrology, post-CMP nano-topography, thin film, overlay | "Engineered for high TPT" (qualitative) | **Not stated** | Up to 300 mm; FRT-derived |
| MicroProf (AP, FE, FS, PT, MHU, TL, 200/300) | Shipping; ">30" MicroProf systems at one tier-1 customer (Q2 2025 call) | FRT acquired 1 Nov 2023 for $100M | Topography, roughness, TTV, warp, film thickness, bumps, TSV | MHU "up to 180 wph" (website) vs 220 (FY2023 20-F) | White-light interferometer "sub-nanometer" height resolution | SurfaceSens multi-sensor |
| 360°Scan (Eagle/Hawk add-on) | Offered, no shipment data | Launch date not found | Edge, bevel, backside; edge trim; bonding alignment | Not stated | Edge/bevel 3 µm; backside 1 µm | — |
| New modules (Aug 2026) | Announced | 10 Aug 2026 | High-resolution backside inspection; fluorescence illumination for organic/PI residue | Not stated | Not stated | — |

Roadmap items [CO, deck 14 Oct 2026]:
- 10th-generation bump sensor for bumps under 5 µm, expected 2027.
- For 2027–28: a next-generation inspection platform with sub-150 nm defect detection, post-bond void detection, copper-dishing metrology, high-throughput die-warp metrology, and TSV-depth metrology.

Installed base [CO]:
- 2023: >2,150 systems.
- 2024 and 2025: ">3,000" (unchanged wording in both years).
- Oct 2026 deck: "~4,000".

Camtek publishes no installed base by product.

### Software and AI classification [CO]

- Products listed on the website:
  - EDC: AI nuisance filtering, standard on tools.
  - ADC: deep-learning classification.
  - AiDC: real-time on-tool classification.
  - 2D AI-based detection.
  - Compass analytics and MDC (manual classification).
  - FRT Acquire XT and Mark III.
- **No accuracy or false-call metric is stated** for any of them.
- Visual Layer, a Tel Aviv visual-AI company, was acquired in Q2 2026; the price was not disclosed. ESTIMATE ≈ $45M or more, from the rise in goodwill plus intangibles.
- On 4 Nov 2026 the CFO said Camtek has "pretty much 0 software offerings" sold separately. Software sales are to start in Q1 2027. The three-year model assumes ~$40M of new software revenue.
- Service + software revenue was $20M (2024) and $28M (2025). Service alone is ~$40M in 2026.

---

## Q2. Revenue by application, as Camtek states it

### Definitions (verbatim labels; all [CO], from calls, notes/02 §1.1)

| Period | Label | Camtek's definition |
|---|---|---|
| 2023 | "Advanced interconnect packaging" (AIP) | "we include chiplet modules, HBM, heterogeneous integration, WLP". The remainder was "compound semiconductor for power device, CIS, and process control". |
| Q1 2024 | AIP split | "40% from HBM segment, 20% from chiplets, and 20% from other advanced packaging". **The only explicit HBM vs chiplet split.** |
| 2024 – Q3 2025 | "HPC" + "other/conventional advanced packaging" | "HPC modules include mainly chiplets, HBM and silicon substrates". From Q1 2025 HPC was given as a range, because OSAT tools cannot be attributed to HPC with certainty. Camtek said: "we do not specify what goes to chiplets and what goes to the high bandwidth memory". |
| Q4 2025 – Q1 2026 | "AI-related products" | The remainder was "CMOS image sensors, compound semiconductors, front-end and general 2D applications". |
| Q2 – Q3 2026 | "Advanced Packaging", majority AI. "AI-related/HPC" = **HBM + "CoWoS and CoWoS-like"** | The remainder in Q2 2026 was "General 2D applications; Photonics". At the Oct 2026 Analyst Day Camtek said "60%-70% of Camtek business is in high-end AP" (2.5D interposers, 3D IC, some fan-out). |

CMOS image sensors, compound semiconductors and front-end are **never given separately** after 2024. Earlier figures:
- Q3 2023: SiC + front-end 20–25%; CIS 5–10%.
- Q2 2024: CIS "ones and twos" %.

### Eight-quarter trend (Q4 2024 – Q3 2026; all [CO], approximate as stated; $ DERIVED)

| Quarter | Revenue $M | HPC / AI-related (HBM + CoWoS-type) | Other / conventional AP | Total AP | Rest |
|---|---|---|---|---|---|
| Q4 2024 | 117.3 | Quarter not given. FY2024 "around 50%" | FY2024 ~20% | FY2024 ~70% | ~30% |
| Q1 2025 | 118.6 | 45–50% | ~20% (Q&A 15–20%) | ~65–70% | ~35% "2D applications" |
| Q2 2025 | 123.3 | ~45–50% (Q&A "50%") | ~20% | 70% | ~30% |
| Q3 2025 | 126.0 | ~45% (~$57M) | ~25% | ~70% | ~30% |
| Q4 2025 | 128.1 | Quarter not given. FY2025 "approximately 50%" AI | FY2025 20% | ~70% | ~30% |
| Q1 2026 | 121.7 | ~50% (~$61M) | ~20% | ~70% | ~30% |
| Q2 2026 | 133.2 | "over 50%, 55% plus" | ~20% | ~75% (~$100M) | 25% (general 2D, photonics) |
| **Q3 2026** | **161.3** | Not stated. DERIVED ~65% (~$105M), low precision | ~15% "in average per quarter" | **~80%** (~$129M) | ~20% |

- **HBM separately:** >10% (Q1 2023); ~20% (H2 2023); **40% (Q1 2024)**; not disclosed since then.
- **HBM in orders:** >20% of the >$600M received to 10 Aug 2026. In Q3 2026 Camtek stopped updating this figure.
- **Reasons management gave:**
  - "shift of CoWoS-like production toward OSATs" (2025).
  - "transition to HBM4 and the associated capacity expansion" and "Rapid 2.5D/3DIC capacity expansion" (2026).
  - Advanced-packaging revenue guided "approximately 70%" higher in Q4 2026 than in Q1 2026 (DERIVED check: consistent with ~80% of the ~$180M Q4 guide).

---

## Q3. Inspection steps per HBM generation

**Bottom line:** no Camtek statement gives a number of inspection or metrology steps for any HBM generation. Nor does any memory maker, competitor, analyst or paper found. The only quantified "steps" statement from Camtek ("tens of new inspection and metrology steps", Feb 2024) is not tied to HBM.

### Camtek statements, chronological (all [CO]; notes/05, ledger_C1)

| Date / venue | Statement | Quantified? |
|---|---|---|
| Q1 2023 call (10 May 2023) | HBM customers ">10% of our revenue" | QUANTIFIED (revenue, not steps) |
| Q1 2024 call (9 May 2024) | "moving from eight to 12 doesn't change our business… we scan wafers". Asked about ASP uplift: "No there isn't". Stack of 8, 12 or 16 "does not require any changes". | QUALITATIVE. Rejects a per-stack frame. |
| Q2 2024 call (1 Aug 2024) | Customers "use more inspection steps to maintain high yield". On how much: "a little bit too early… to really pinpoint the steps". | QUALITATIVE |
| Q4 2024 call (12 Feb 2025) | Bumps per HBM wafer "over 100 million… stays in this range… not going to go to 300 million". Intensity grows "as you're putting more and more dies in the same module". | QUANTIFIED (bump count) |
| Q1 2025 call (13 May 2025) | HBM3→HBM4 "brings additional opportunities with more inspection and metrology steps" | QUALITATIVE |
| Q2 2025 call (5 Aug 2025) | On HBM3E→HBM4 content: "we will scan more wafers. There is some change in the number of bumps, some pitch differences"; "most of the equipment that we sold to HBM3 will be used for HBM4 as well" | QUALITATIVE |
| Q3 2025 call (10 Nov 2025) | HBM4 "inspection and metrology intensive because the bumps are getting tighter. There are going to be more bumps". "Tool of record for all the 3D metrology for HBM4 at all the HBM manufacturers." | QUALITATIVE |
| Q4 2025 call (18 Feb 2026) | "more metrology and inspection intensive" | QUALITATIVE |
| Analyst Day (14 Oct 2026) | "increased complexity contributes more inspection and metrology steps". Bump height 6 → 5 → 3 µm. HBM die-warp spec from 1 mm to 100 µm, which "cannot be met with a current sensor". | QUANTIFIED specs; steps QUALITATIVE |
| Q3 2026 call (4 Nov 2026) | HBM4/4E not mentioned. Opportunity framed as gaining "share in 2D for additional steps… not really specific… whether it's a GPU or HBM". | QUALITATIVE |
| 20-F FY2024, FY2025 | "Chiplets and HBM require more inspection and metrology steps" | QUALITATIVE |

### What Camtek sells per HBM step (by Camtek's account)

| HBM step | What Camtek offers |
|---|---|
| Front-side micro-bump wafer, 2D inspection | Eagle G5 and Hawk. Claimed "tool of record for several 2D inspection steps". |
| Micro-bump 3D metrology | CTS Gen 8/9 sensors on Eagle and Hawk, plus dedicated bump-metrology systems. Claimed reference tool for HBM4/HBM4E. |
| Thinned-wafer backside and edge | 360°Scan. No HBM-specific statement. |
| Wafer warp | MicroProf/NanoProf. Die warp at high throughput is a 2027–28 roadmap item. |
| Die-stack planarity; known-good-package | Named generically in the 20-F. |
| Not addressed in any Camtek statement found | Die-to-wafer stacked inspection; inspection of the HBM4 logic base die made at a foundry. |
| Hybrid-bonded stacks | Pre-bond inspection at 150 nm and pre-bond metrology. Post-bond void detection is roadmap only. |

### Independent views [IND]

- **KLA (29 Oct 2025):** HBM raised DRAM front-end process-control intensity by "another point or so". KLA also said packaging users "won't inspect at the frequency" over time.
- **Onto (9 Nov 2026):** packaging process-control intensity "increased fairly dramatically". For HBM4→HBM4E, demand is "driven a lot by volume… It's all about the wafers for us".
- **SemiEngineering (11 Nov 2025):** bumps go from 30–20 µm in HBM3E to ~10 µm in HBM4, "pushing defect inspection to the limit".
- **TrendForce (21 Apr 2025):** JEDEC HBM4 has 2,048-bit I/O and 32 channels per stack.
- **Market alternatives for HBM steps:** X-ray and CT (SEC, Techvalley) and Korean optical tools (Nextin, Pemtron, Youngwoo DSP) are winning HBM steps, per TheElec and Hankyung in 2025–26.
- **Fewer dies per stack:** GPU/ASIC makers are reportedly weighing 8-high instead of 12-high HBM (TrendForce via EE Times Japan, 30 Sep 2026).
- **Summary:** independent sources support "more difficult and more intensive"; none supports "more Camtek steps per stack" with a number.

---

## Q4. Hybrid bonding

### (a) Tools by step [CO, unless noted]

| Hybrid-bonding step | Camtek product | Status |
|---|---|---|
| Pre-bond particles and defects | Hawk at **150 nm** (Camtek says hybrid bonding needs "sub 150 nm"); some Eagle units | Shipping, used at pilot lines |
| Sub-150 nm next generation | New platform | Roadmap 2027–28 |
| Copper pad recess / dishing (post-CMP) | Dedicated sensor | **Roadmap 2027–28** |
| Post-CMP roughness / topography | FRT white-light interferometer and confocal sensors today (generic, sub-nm height resolution); improved sensor planned | Shipping (generic); improvement on the 2027–28 roadmap |
| Pre-bond metrology (general) | NanoProf ("Pre-bonding metrology"); MicroProf AP | Initial installs (NanoProf); shipping (MicroProf AP) |
| Wafer / die warp | MicroProf (wafer); high-throughput die warp | Wafer: shipping. Die: roadmap |
| Edge, bevel and bonding alignment of stacked wafers | 360°Scan | Offered |
| **Post-bond voids / bond interface** | **None.** Camtek is "evaluating several technologies" | **Roadmap 2027–28; technology not chosen** |

Other vendors named by independent sources for these steps:
- Onto: opto-acoustic void detection and scatterometry.
- PVA TePla and Nordson: acoustic microscopy.
- Bruker and Park: AFM.
- Zeiss: X-ray.
- Applied Materials: CD-SEM of hybrid-bonding pads.
- KLA: SoIC/hybrid-bonding sensitivity.
- Nextin: ASPER at 50 nm; IRIS-III IR for voids.

Sources: SemiEngineering 10 Nov 2026; Chip Scale Review 5 Sep 2025; TheElec 14 Jul 2026.

### (b) Systems shipped, revenue and customers [CO]

| Date | Camtek's description |
|---|---|
| May 2023 | "working with customers that are doing hybrid bonding" |
| Feb 2025 | "installed machines at several sites… for several steps" |
| May 2025 | "pilot lines" |
| Nov 2025 | "a few machines at… major customer sites" |
| 4 Nov 2026 | "some business, but really on a low magnitude"; "in 2027, I do not expect to see any substantial business"; volume "2028 and onwards" |

- **Units, revenue and customer type: not disclosed.**
- **Order releases:** none attributes an order to hybrid bonding.
- **Image sensors:** CIS makers have used wafer-to-wafer hybrid bonding since the mid-2010s, and Camtek sells to "the largest CIS manufacturers". Camtek does not count CIS as hybrid-bonding business.
- **Timing has slipped:** "starting 2027, 2028" (Feb 2025) → "higher in '27" (Nov 2025) → "slower than we expected" and "not full steam before the end of this decade" (Oct 2026) → "2028 and onwards" (Nov 2026).

### (c) Reverse question: revenue that depends on micro-bumps

What hybrid bonding removes:
- **HBM:** the core-die-to-core-die micro-bumps.
- **Logic SoIC:** hybrid bonding stacks die on die and leaves the interposer bumps in place. It is additive.
- **CIS:** not bump-based.

Timing for HBM, independent sources:
- TrendForce (7 Jul 2026): 16-high HBM4E is "earliest likely adoption"; 12-high HBM4E remains mainstream.
- SK hynix (Hot Chips 2026; Herald 20 Sep 2026): hybrid bonding for stacks of 20 or more dies, and only after 90–98% yield is reached.
- Counterpoint (Apr 2026): HBM5 with hybrid bonding around 2029–30.
- Hankyung (25 Feb 2026), relaying Samsung: hybrid bonding in HBM4 samples, partial use at HBM4E.

Camtek (14 Oct 2026) says HBM5 "is going to continue to be based on bumps". **No independent source found states that HBM5 stays on micro-bumps.**

Camtek's quantified anchors:
- 2026 tool units: 60% 2D-only, 25% inspection + 3D bump sensor, 15% dedicated bump metrology. So 40% of units carry a 3D bump sensor.
- HBM >20% of 2026 orders to 10 Aug.
- HBM 40% of revenue in Q1 2024.

Estimate (notes/06 §6; LTM Q4 2025–Q3 2026 revenue $544.3M):

| Measure | Low | Base | High |
|---|---|---|---|
| M1: revenue tied to bump inspection/metrology of any kind | 34.5% | **48.5%** | 57.3% |
| M2: revenue tied to die-to-die micro-bumps that hybrid bonding would remove | 5.4% (~$29M) | **10.0%** (~$54M) | 25.8% (~$140M) |

The inputs are Camtek's unit split and its verbal percentages plus my assumptions; **no independent input exists**. The disclosures that would pin it down are listed in notes/06 §6.4: revenue by tool type, HBM revenue after Q1 2024, and Camtek content per hybrid-bonded wafer vs per micro-bumped wafer.

---

## Q5. Head-to-head at the same accounts (non-Camtek sources)

Direction column: **+** = Camtek win or presence; **−** = rival gain; **±** = dual sourcing or neutral; **?** = cannot be tied to Camtek.

| Account | What non-Camtek sources report | Basis | Direction |
|---|---|---|---|
| **SK hynix** | SK hynix Best Partner Award to **Onto**, presented by the SK hynix CEO on 28 Sep 2026, for HBM defect prevention with Dragonfly G5 (Onto release, 12 Oct 2026). SK hynix's own list does not name awardees. | Firsthand (vendor relay of customer award) | − / ± |
| SK hynix | Nextin KROKY HBM inspection contracts ≈KRW 17bn (2025, exchange disclosures). Pemtron in-stack inspection order (Sep 2025). | Firsthand | − (local vendors) |
| SK hynix | "SK hynix uses Camtek" (Jason's Chips, Feb 2026) | Unsourced | + |
| **Unnamed "leading HBM maker"** | Onto, 19 Feb 2026: volume purchase agreement **>$240M** for Dragonfly 2D + 3D bump metrology (>$60M 3D) through 2027. Onto, 16 Mar 2026: double-digit G5 + 3Di orders for "the majority of their 2D inspection needs", "**displacing the previously established tool of record**". Neither the customer nor the displaced vendor is named. | Firsthand (Onto) | − |
| Two HBM customers | Onto 3Di "full qualification at… two HBM customers" (6 Nov 2025). Pre-reflow metrology, possibly a new step. | Firsthand (Onto) | ± |
| **Samsung** | "Samsung uses Onto" (Jason's Chips). Jefferies (Sep 2025) implies Onto exposure. Onto JDP for laser-ultrasound hybrid-bonding/TSV inspection, already on a mass-production line (TheElec, 31 Mar 2026). Nextin ASPER in qualification at "S사" (TheElec, 13 Feb 2026). No Samsung document names any vendor. | Unsourced / secondhand / trade press | − / ? |
| **Micron** | "Micron switched to Onto as their primary die-level inspection supplier" (Jason's Chips). SEC X-ray order for Micron HBM (TheElec, 10 Nov 2026). No Micron document names an optical vendor. | Unsourced / trade press | − / ? |
| **TSMC (CoWoS)** | Onto lost 2.5D share to a "very, very large competitor" (Onto, May 2025; KLA by implication) and reports recapture with G5 (Apr 2026). KLA claims #1 in advanced-wafer-level-packaging process control in 2025 (+14 pts). Ta Liang says its HBM incoming AOI entered TSMC's supply chain (TechNews, Apr 2026). No TSMC document names Camtek. | Firsthand (vendors) / press | ? for Camtek |
| **ASE / SPIL** | **ASE MOPS filing: SPIL bought 6 batches from Camtek Ltd. for NT$1,749.6M (≈US$54.3–55.3M at FRED rates), 22 Jun – 16 Jul 2026.** This matches Camtek's $55M "tier-1 OSAT" order of 2 Jun 2026 in size and timing (INFERENCE). ASE also bought from KLA (NT$1.10bn Jan–Oct 2025; NT$1.14bn Nov 2025–Feb 2026; tool type unstated) and Machvision. Onto: >$200M from one OSAT (Q2 2026); Camtek says it got an order "not much smaller from the same customer". | Firsthand filings; vendor statements | + / ± (dual sourcing at one OSAT) |
| Amkor, JCET, Tongfu, Powertech | No independent evidence naming any inspection vendor. | — | — |
| Intel | Intel 2026 EPIC awards: Camtek and KLA both recognized; Onto not on the list. | Firsthand (customer) | + / ± |
| Chinese vendors | Skyverse: advanced packaging ≈15% of orders, mainly HBM and 2.5D/3D (Q3 2026); batch sales to "several overseas AP customers". CETC Fenghua and Changchuan active. Onto told BIS (Jan 2024) that Camtek gained China share at Onto's expense. | Secondhand / firsthand (Onto) | − / + |

Comparison figures [IND, company-reported]:
- **Onto:** SD&AP revenue $504M in FY2025. 2026 advanced-packaging growth "north of 80%", "evenly split" between 2.5D and HBM. 3Di revenue more than doubled in 9M 2026 ("share gain… we didn't have much of a position"). Record $1.3B backlog. Onto names "KLA and Camtek" as its principal packaging-inspection competitors.
- **KLA:** advanced-packaging process-control revenue ~$1.1B expected for CY2026.
- **Camtek [CO]:** Korea revenue fell from **$117.1M (2024) to $36.9M (2025)**, −68.5%, unexplained by Camtek. Stifel (Nov 2025, secondhand) attributes the drop to Samsung weakness.

Camtek's own claims, kept separate [CO]:
- "tool of record for all the 3D metrology for HBM4 at all the HBM manufacturers" (Nov 2025).
- "not lost any market share" (Feb 2026).
- Losing share? "absolutely no" (May 2026).
- Taiwan OSAT share "at least 50%" (Oct 2026).

---

## Q6. Orders: definitions, periods, delivery, cancellation, capacity

### Order and backlog figures relating to 2026 [CO]

| Date | Figure | Delivery stated | What it is |
|---|---|---|---|
| 10 Feb 2026 | $25M Hawk order; $45M cumulative from a tier-1 IDM | "2026" | Orders |
| 30 Mar 2026 | $31M OSAT (CoWoS-like); Q1 OSAT orders >$90M | "within this year" | Orders |
| 12 May 2026 | >$260M from 2 HBM makers | 2026 and 2027, split not given ("significant" part in 2026) | **"order and forecast" / "POs and forecast"**. The PO portion is not disclosed. |
| 2 Jun 2026 | $55M tier-1 OSAT + >$50M Hawk from an HBM maker | **All 2027** | Orders. The $55M size matches the SPIL filing. |
| 10 Aug 2026 | >$600M year to date (~80% advanced packaging; >50% OSAT; >20% HBM; 5% photonics) | "remainder of 2026 and into 2027" | "Orders received" |
| 14 Oct 2026 | >$800M year to date | "2026 and 2027" | "Incoming orders" |
| 14 Oct / 4 Nov 2026 | 2027 revenue outlook >$800M ("not a guidance"); ~$1.2B target in ~3 years | — | "backlog and sales pipeline" |

Definitions and terms:
- **Order:** never defined in writing. Management describes backlog as POs in hand. "Pipeline" includes customers who reserved a slot and "committed to give the purchase order at a later date".
- **Backlog:** Camtek gives no dollar figure, no RPO and no book-to-bill ("this is as far as we can go", 4 Nov 2026). DERIVED lower bound: ≥~$200M of 2026 orders for 2027 delivery as of mid-Oct 2026 (notes/08 §10.4).
- **Cancellation and rescheduling:** no fees or deposit terms are disclosed. The 20-F lists "changes made by customers to orders… and/or installation schedules" as a risk and says Camtek has "limited visibility and do[es] not have long-term purchase commitments with many customers".
- **Payments:** Camtek receives "advanced payments before shipment from most customers"; milestones are shipping and installation. Customer advances + deferred revenue fell from $28.9M (2024) to $18.0M (2025).
- **Revenue recognition:** at transfer of control, generally on shipment.
- **No cancellation or push-out** of any order has been reported, 2023 – Q3 2026.

Capacity [CO]:

| Date | Stated capacity |
|---|---|
| Feb 2024 | ≥$500M |
| Nov 2024 | >$600M → ~$660M with a Europe addition |
| Feb 2026 | "well over $700M" (process efficiency); further Germany capacity "late 2026" (earlier promised for 2025) |
| Oct 2026 | "infrastructure… in place" for $1.2B, relying on subcontract "manufacturing partners" |

- The unit behind these figures, the partners' names and the German expansion's size and cost are not disclosed.
- Supply chain, 4 Nov 2026: "experiencing certain supply chain challenges" in memory, CPUs and handling parts, with a fix in "three to six months… We're not sure". In Aug 2026 Camtek had said "we don't see any issues".

Conversion record [CO]:
- Quarterly guidance was met or beaten every quarter from Q1 2024 to Q3 2026: 10 beats, 1 met, average +1.9% vs midpoint.
- H2 2026 guidance was raised in steps to an implied +33.9% over H1.
- Hawk orders "for 2025" shipped within 2025, starting in Q2.

---

## Module A. Financial and corporate fact base

### A.1 Annual and 9M financials ($M; [CO], 20-F and releases)

| | FY2022 | FY2023 | FY2024 | FY2025 | 9M 2026 |
|---|---|---|---|---|---|
| Revenue | 320.9 | 315.4 | 429.2 | 496.1 | 416.2 (+13.1%) |
| GAAP / non-GAAP gross margin | 49.8% / 50.2% | 46.8% / 48.4% | 48.9% / 50.8% | 50.5% / 51.6% | 50.0% / 51.1% |
| GAAP / non-GAAP operating margin | 25.4% / 28.7% | 20.7% / 26.4% | 25.2% / 30.4% | 25.8% / 30.0% | 22.7% / 27.5% |
| GAAP net income | 79.9 | 78.6 | 118.5 | 50.7 (after a $100.9M note-extinguishment loss) | 97.8 |
| Non-GAAP diluted EPS ($) | 1.88 | 1.96 | 2.83 | 3.26 | 2.45 |
| Operating cash flow | 57.8 | 79.3 | 122.2 | 141.9 | 86.4 |
| FCF (DERIVED) | 49.5 | 71.1 | 111.9 | 127.1 | Capex not disclosed |
| Cash + deposits + securities (period end) | 478.7 | 448.6 | 501.2 | 851.1 | 877.1 (30 Sep) |

- **Net cash at 30 Sep 2026:** ≈ $377M (DERIVED: 877.1 − 500.0 − 0.063).
- **Headcount:** 709 (end-2025); "750+" (Oct 2026).
- **Q3 2026:** revenue $161.3M; GAAP operating income $39.8M; GAAP net income $42.8M. (A "$8M" figure in one notes file was an extraction error, corrected in notes/99.)
- **Guidance:** Q4 2026 ~$180M; FY2026 ~$595M; FY2027 >$800M (outlook).

### A.2 Gross margin by quarter, with the mix effects management names (non-GAAP; [CO])

| Quarter | GM | Drivers named by management |
|---|---|---|
| Q1 2023 | 47.3% | Product mix, smaller customers, component inflation |
| Q2–Q4 2023 | 48.0% → 49.0% → 49.2% | Cost actions. Configuration mix ("basic configuration… lower gross margin"). FRT purchase accounting hit GAAP only (44.9% in Q4 2023). |
| Q1 2024 | 50.6% | Advanced-packaging/HBM mix; cost structure; ASPs |
| Q2–Q4 2024 | 51.0% / 50.8% / 50.6% | Product mix (range "50.5–51.5%"); volume "limited" at GM level; new-product accretion deferred "to 2026" |
| Q1 2025 | 52.1% | Favourable mix. Tariffs immaterial. |
| Q2 2025 | 51.9% | Hawk "more expensive… positive contribution". Iran-conflict freight (>$0.5M) hit opex. |
| Q3 2025 | 51.5% | New-tool mix; volume |
| Q4 2025 | 51.1% | Bill-of-material actions. H1 2026 guided 50.5–51.5%. |
| Q1 2026 | 51.0% | Supply-chain cost pressure; improvement expected H2 2026 with Hawk/G5 |
| Q2 2026 | 51.4% | Hoped-for "52.5–53%" exit rate; ASP increases |
| **Q3 2026** | **51.1%** | "price pressure on parts, components, and material" (memory, CPUs, handling parts); **shekel strength on COGS**; favourable product mix; ASP increases to help "in 2027"; improvement "starting from the first quarter of 2027" |
| Target | 55–56% at $1.2B | Hawk/G5 mix plus software and services, "around 3.4 points" |

- **China mix has never been named** as a gross-margin driver.
- The expected improvement from new products has been deferred four times: 2026 → H2 2026 → exit 2026 → Q1 2027.

### A.3 China share and export rules

China share of revenue (20-F, by destination of shipment; [CO]):

| Period | China share |
|---|---|
| 2021 | 54.8% (DERIVED) |
| 2022 | 44.2% |
| 2023 | 47% |
| 2024 | 31% |
| 2025 | **49%** ($243.9M, +84% YoY) |
| FY2026 (guided) | "45-ish" / "around 45%"; 2027 backlog China "at least as high as this year" |

- **China share by quarter since 2023: not disclosed by Camtek.**
- Camtek gives only Asia vs rest of world each quarter:

| Year | Q1 | Q2 | Q3 | Q4 |
|---|---|---|---|---|
| 2023 | 90% | 83% | 81% | 82% |
| 2024 | 86% | 92% | 87% | 92% |
| 2025 | 91% | 90% | 93% | 89% |
| 2026 | not given | 92% | **95%** | — |

- An independent proxy (China customs HS 9031.41 imports from Israel) was searched for but not obtained.

Rules that apply to an Israeli supplier (notes/04; primary regulatory text):
1. **Product classification.** No US rule names packaging AOI or bump metrology. The front-end inspection controls (3B993.q, 3B994.q) target sub-21 nm patterned-wafer inspection and similar tools. On their wording, Camtek tools fit the AT-only **3B992.b** (ANALYSIS). Camtek has not disclosed ECCNs, US content or licences.
2. **When US rules reach an Israeli tool.** Tools made in Israel and Germany are outside the EAR unless one of these applies:
   - US content above de minimis.
   - An FDP rule.
   - US-person activity (Camtek USA Inc. is a US person).
3. **December 2024 FDP rules (extended January 2025).** For Category 3B items, including 3B992, that contain **any US-origin IC**, there is **no de minimis floor** when the item goes to:
   - Footnote 5 Entity-List firms (e.g. XMC, SMIC entries, Huawei-linked fabs), or
   - China facilities producing advanced-node logic or DRAM.
   - A licence is then required where the exporter is headquartered outside Country Groups A:5 and Supplement 4 to Part 742. **Israel is A:6 only and is not in Supplement 4**, so the rule can reach Camtek. XMC is eligible for License Exception RFF for 3B991/3B992 items.
4. **The HBM rules** (December 2024) control HBM chips (3A090.c) and TSV etch tools, **not inspection or metrology**.
5. **Customer status.** CXMT is not on the Entity List as of 13 Nov 2026 (a senator requested its addition on 12 Nov). Tongfu and JCET are not on it. Sales to unlisted Chinese OSATs appear to need no US licence on the text reviewed.
6. **Pending.** The MATCH Act (not enacted as of 17 Nov 2026) would extend US controls to allied tools with >0% US content. It presumptively covers 3B001/3B002/3B993, **not 3B992**. No new BIS SME rule was published between 1 Jan 2025 and 19 Nov 2026. The 50% affiliates rule is suspended to 10 Jan 2027.
7. **Israel.** Israel controls dual-use exports under the 2006 Order (Wassenaar lists; Israel is not a member). **No Israeli SME control aligned with US rules was found.** A draft dual-use law of 26 Mar 2026 does not mention semiconductors.

What Camtek says [CO]:
- Nov 2022: the October 2022 rules' "direct revenue impact will be marginal, if any"; customers are "mainly OSATs".
- **FY2023 20-F:** Entity-Listed Chinese manufacturers "have acquired and may continue to acquire several of our metrology solutions". **This sentence was dropped in FY2024.**
- FY2024 20-F: added "additional export controls on our products… could lead to further revenue losses". **Removed again in FY2025.**
- On HBM: "definitely not a Chinese business" (Feb 2024).
- Asked about CXMT (Aug 2026): "we cannot talk about names of customers".
- **Never quantified:** revenue from Entity-Listed customers, licences, or revenue lost to export controls.
- Independent scrutiny: Onto told BIS (17 Jan 2024) that "Israeli companies such as Camtek… are supplying to entity-listed companies" and asked that US rules apply to Israel.

### A.4 Customer concentration [CO, 20-F]

| Year | Customers >10% of revenue | Top-three share (DERIVED bounds) |
|---|---|---|
| 2021 | None | ≤ ~30% |
| 2022 | One at 11% | 11% to ≤ ~31% |
| 2023 | One at 15% ("more than 15%" in FY2023 20-F) | 15% to ≤ ~35% |
| 2024 | Three at **15%, 10%, 10%** | **~35%** |
| 2025 | One at **11%** (~$54.6M) | 11% to ≤ ~31% |

- No customer is named. Camtek reports >300 customers (Oct 2026); OSATs were >50% of 2026 orders.
- INFERENCE (low confidence):
  - The 2023 customer is consistent with a Korean HBM maker: Korea revenue was $47.4M, or 15.0%.
  - The 2025 11% customer **cannot** ship only to Korea, because Korea revenue was $36.9M, below $54.6M.

### A.5 Convertible notes [CO, 20-F FY2025, releases; notes/03 §c, notes/99 §2.2]

| | 2026 Notes | 2030 Notes |
|---|---|---|
| Principal | $200M, 0% | $500M, 0.00% |
| Issued | Nov 2021 | Priced 12 Sep 2025; closed 16 Sep 2025 |
| Maturity | **1 Dec 2026** | **15 Sep 2030** |
| Conversion price | ~$58.45 (17.1092 shares per $1,000) | ~**$109.34** (9.1455 shares per $1,000) |
| Settlement | Cash, shares or a mix, at Camtek's election | Same |
| Capped call | None disclosed | None disclosed |
| Issuer call | From 6 Dec 2024 at 130% | From **20 Sep 2028** at 130% |
| Status | See below | Carrying value $489.2M (30 Sep 2026); 4.57M underlying shares = **9.8%** of shares outstanding |

How the nearest maturity (the 2026 Notes) is being settled:
- **Sep 2025:** $167.1M (83.5%) repurchased for **$267.0M cash**, about 159.8% of par, funded from the 2030 notes. This produced a $100.9M pre-tax extinguishment loss.
- **1 Jan – 4 Mar 2026:** ~$32.9M converted. The method was not stated; share settlement is INFERRED, about 0.56M shares or 1.2% dilution.
- **Residual:** **$63,000** outstanding as of 4 Mar 2026, due 1 Dec 2026. No notice has been filed.

2030 Notes conversion trigger:
- The trigger is 130% × $109.34 = $142.14.
- On closing prices, at least 20 of the 30 trading days ending 30 Sep 2026 closed at or above $142.14. The 20th qualifying day cleared the trigger by **$0.47**.
- That would open holder conversion for Q4 2026 (DERIVED; the indenture's price definition was not re-read).
- At the 20 Nov 2026 close of $89.20, conversion value is ~$816 per $1,000, about 18% below par.
- Camtek has not commented and kept the notes in long-term liabilities.
- No other debt and no buyback. One dividend: $1.33 per share (~$60M) in 2024.

### A.6 Ownership, people, legal

**Holders above 5%:**

| Holder | Stake | As of / source |
|---|---|---|
| Priortech | 20.61% | 18 Jun 2026 |
| Chroma ATE | 16.75% | 18 Jun 2026 |
| Migdal | 10.06% | 15 Oct 2026 (13G/A) |
| Harel | 7.8% | 31 Mar 2026 |
| Phoenix | 5.12% | 6 Aug 2026 |
| Menora | 5.08% | 14 Oct 2026 |

- Wasatch fell to 4.5% (30 Jun 2026).
- Priortech and Chroma vote together, with combined control of 37.4%.
- The registration-rights agreement was extended to 2031 on 24 Jun 2026, and the demand threshold was cut to 1%. No sale has been announced.

**People:**
- CEO: Rafi Amit (founder, 77).
- CFO: Moshe Eisenberg (since 2011).
- President & COO: Ramy Langer (title since Aug 2026).
- Executive Chairman: Lior Aviram (since 1 Jun 2025).
- No CTO is listed. Technology is led by an EVP R&D, hired in Feb 2026.
- No succession plan has been disclosed.
- Insider open-market sales on 11–17 Aug 2026 totalled 30,190 shares (EDGAR Forms 4).

**Legal and operating risk:**
- No material proceedings. Preferred Enterprise tax rate of 7.5%.
- The $7.7M one-time tax expense fell in **Q2 2026**; its nature is not disclosed.
- War risk: during the Feb–May 2026 Iran war Camtek "have not missed even 1 shipment" [CO]. Its insurance excludes security events.

### A.7 Guidance track record [CO]

| Quarter | Q1 | Q2 | Q3 | Q4 |
|---|---|---|---|---|
| 2024 | Beat | Beat | Beat | Beat |
| 2025 | **Met** (within range) | Beat | Beat | Beat |
| 2026 | Beat | Beat | Beat | Pending (~$180M; report ~Feb 2027) |

- No misses. Beats are small (+0.8% to +3.5% vs midpoint).
- FY2026 guidance only rose: "double-digit" → ~$595M.

---

## Module B. Claims ledger

Full entries with every cited item: `notes/ledger_C1.md` to `ledger_C4.md`. Under the stand-in rule, a claim supported only by [CO] sources is capped at "partly supported".

| # | Claim | Who makes it | Verdict | Confidence | Evidence for | Evidence against | Independent share | Next checkpoints |
|---|---|---|---|---|---|---|---|---|
| C1 | HBM4 and HBM4E add inspection steps per stack | Camtek only (calls May 2025 – Feb 2026; Analyst Day 14 Oct 2026; 20-F) | **Partly supported** | Medium | Independent sources confirm higher HBM4 difficulty: bumps to ~10 µm, 2× I/O, warpage, lower yields (SemiEngineering, TrendForce, NewDaily, KLA "+1 point" front-end). Onto says HBM4 has "a large number of inspection steps". | No step count from anyone. Camtek in 2024–25: stack height "doesn't change our business"; "most of the equipment… for HBM3 will be used for HBM4". Onto: HBM4→4E is "all about the wafers". Steps added for taller stacks went to X-ray and Korean vendors. 8-high HBM reconsidered. HBM's weight in Camtek orders (>20%) is below its Q1 2024 revenue share (40%). HBM not mentioned on the Q3 2026 call. | ~55% of items; **0%** on "more steps per stack" | Camtek Q4 2026 results (~mid-Feb 2027); SEMICON Korea (Feb 2027); 10th-gen sensor (2027); HBM4E stack-height mix (late 2027) |
| C2 | Hybrid bonding expands Camtek's addressable market instead of shrinking it | Camtek only (2023–2026; deck slide "HB growth provides new opportunities") | **Partly supported** | Medium | Hybrid bonding adds steps: 50 nm particles, 2–5 nm Cu recess, 0.5 nm roughness, voids (SemiEngineering, Onto/CSR, KLA). Micro-bumps persist in HBM through HBM4E (TrendForce, SK hynix). Yole: TCB bonders $936M vs hybrid bonders $397M by 2030. | Camtek has no void or dishing product (roadmap 2027–28). Its 150 nm pre-bond sensitivity trails Nextin (50 nm) and KLA (~100 nm). No independent source names Camtek in any hybrid-bonding step. Hybrid-bonding revenue is "low magnitude", with timing slipped to "2028 and onwards". Camtek itself says hybrid bonding "eliminates the need for micro-bumps", and its tool-of-record position is in micro-bump metrology. Samsung may adopt hybrid bonding at HBM4E. | ~60% of items; **0%** on Camtek capturing hybrid-bonding steps | SK hynix hybrid-bonding decision (end-2026); Samsung HBM4E process (1H 2027); Camtek roadmap releases (2027–28); JEDEC HBM5 height decision |
| C3 | Camtek holds or gains share against Onto at the HBM makers | Camtek only ("tool of record… at all the HBM manufacturers", Nov 2025; "absolutely no" share loss, May 2026); Jefferies relays it | **Not supported** | Medium | Only [CO] and [CO-relayed] statements, plus secondhand analyst notes not specific to HBM or Onto, plus "led by Camtek and Onto" as of HBM3E (Dealsite 2025). | Onto: >$240M HBM VPA with >$60M of 3D metrology (19 Feb 2026, the day after Camtek's "not lost any share"). Onto: G5 + 3Di "displacing the previously established tool of record" at an HBM maker (Mar 2026). Onto 3Di qualified at 2 HBM customers; 3Di revenue >2× ("share gain"). SK hynix award to Onto. Morgan Stanley: "HBM metrology share is diverging". Camtek Korea revenue −68.5% in 2025 while Onto's South Korea revenue fell −1.7%. Camtek narrowed "all HBM makers" to "2 HBM manufacturers" (May 2026) and stopped reporting HBM order share. | 55% of items; **0** firsthand independent items for the claim | Onto and Camtek Q4 results (Feb 2027); Camtek FY2026 20-F Korea revenue and 10% customers (Mar 2027); Nextin PO at Samsung (Q4 2026); SK hynix Partners Day 2027 |
| C4 | 2026 orders convert to revenue on the stated schedule | Camtek only (order releases Feb–Jun 2026; Q3 call "we will not miss any delivery schedules") | **Partly supported** | Medium | 11 quarters with no guidance miss. H2 2026 guidance raised in steps. No cancellation ever reported. Q3 2026 OCF $71.1M. Demand context [IND]: Onto $1.3B backlog; ASE record capex; SK hynix sold out; CoWoS capacity doubling. The SPIL filing independently sizes one 2026 order (≈$55M). | The schedule is only "2026 / 2027" buckets. There is no backlog $, RPO or split. The $260M figure mixes POs and forecasts. "Pipeline" includes slots without POs. Customer advances fell to $18.0M. The 20-F says Camtek has "limited visibility". Supply chain went from "no issues" (Aug) to "challenges", "3–6 months… not sure" (Nov). Industry lead times are >18 months. China is ~45% of the 2027 backlog, with MATCH Act risk. Korea revenue swung −68.5% in 2025. | ~42% of items; **0%** on Camtek's own order-to-shipment timing | **Q4 2026 results vs ~$180M (~mid-Feb 2027)**; component recovery (Feb–May 2027); FY2026 20-F advances/RPO (Mar 2027); Q2 2027 for the $105M "2027" orders; FY2027 vs >$800M (Feb 2028) |

### Handoff table

| Cell | Value | Status / basis |
|---|---|---|
| C1 verdict | Partly supported (medium) | Direction supported; per-stack step increase unquantified by anyone |
| C2 verdict | Partly supported (medium) | Industry-level step addition supported; Camtek's capture unshown; net effect never quantified |
| C3 verdict | **Not supported** (medium) | Independent evidence points to Onto gains at ≥1 HBM maker; displaced vendor not named |
| C4 verdict | Partly supported (medium) | Guidance record clean; order-level schedule untestable; Q4 2026 is the next test |
| **Share of revenue that depends on micro-bump inspection** | **≈48.5% of LTM revenue (range 34.5–57.3%)** tied to bump inspection and metrology of any kind. Of that, **≈10% of revenue (range 5.4–25.8%)** is tied to the die-to-die micro-bumps that hybrid bonding would remove. | **ESTIMATE**, LTM Q4 2025 – Q3 2026, revenue $544.3M. Inputs: Camtek's 2026 unit split (60/25/15), verbal AI/AP shares, HBM share 15–30%; my assumptions on ASPs and layer mix. No disclosure or independent figure exists. Exposure runs over a multi-year transition (16-high HBM4E at the earliest; most likely 20-high HBM5 around 2029–30). |
| China share of revenue | 49% (FY2025); ~45% (FY2026 guided) | [CO]; quarterly not disclosed |
| Largest customer | 11% (FY2025); top three 11–31% (bounds) | [CO]; DERIVED bounds |
| Net cash | ≈$377M (30 Sep 2026) | DERIVED |
| Nearest note maturity | $63k due 1 Dec 2026 | [CO]; immaterial |

---

## What is not disclosed or could not be verified

- **Not disclosed by Camtek:**
  - China share by quarter.
  - HBM vs CoWoS-type revenue after Q1 2024.
  - CIS, compound and front-end revenue by quarter.
  - Step counts per HBM generation.
  - Hybrid-bonding units, revenue and customers.
  - Customer names.
  - Top-three customer share.
  - Backlog in dollars, RPO, book-to-bill and the order definition.
  - Cancellation fees and deposit terms.
  - ECCNs, US-origin content and export licences.
  - Settlement method of the Q1 2026 conversions.
  - Visual Layer price.
  - Absolute throughput of Hawk, G5 and NanoProf.
  - The nature of the $7.7M tax item.
- **Not found from independent sources:**
  - Any SK hynix, Samsung, Micron or TSMC document naming Camtek for HBM or CoWoS inspection.
  - Any independent source naming Camtek in a hybrid-bonding step.
  - Any independent step count per HBM generation.
  - Any independent HBM inspection share dataset.
- **Identity gap:** the "previously established tool of record" that Onto displaced at an HBM maker in March 2026 is **not identified**. It is the single fact that would most change ledger C3.

## Main contradictions recorded (detail in the notes files)

1. **Hawk specifications.** Sensitivity is 100 nm on the website but 150 nm in the 20-F and deck, while sub-150 nm also appears as a 2027–28 roadmap item. Bump pitch is <10 µm vs <12 µm.
2. **Share claim vs Onto.** "Tool of record for 3D metrology at all HBM makers" (Nov 2025) vs Onto's "displacing the previously established tool of record" at an HBM maker (Mar 2026). One of the two is overstated, or the displaced tool was not Camtek's.
3. **HBM content framing.** Camtek said stack height "doesn't change our business" (May 2024) and later "more inspection and metrology steps" with HBM4 (2025–26).
4. **Hybrid bonding in HBM5.** Camtek says HBM5 stays on bumps (Oct 2026); independent sources expect hybrid bonding for 20-high HBM5 around 2029–30.
5. **Software.** The FY2025 20-F says AI software would be offered "during 2026"; the CFO said on 4 Nov 2026 that there is "pretty much 0" and sales start Q1 2027.
6. **Installed base.** ">3,000" at both end-2024 and end-2025, then "~4,000" by Oct 2026.
7. **Gross-margin timing.** Expected accretion was deferred four times; the supply-chain message reversed within one quarter.
8. **Export-control risk factors.** The Entity-List customer sentence (FY2023) and the "revenue losses" sentence (FY2024) were each removed the following year.
9. **2030 notes.** Closing prices met the 130% conversion test for Q4 2026 while the notes stayed classified as long-term. Settlement in shares would make this consistent; Camtek has not commented.
