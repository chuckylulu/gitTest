# Nova Ltd. (Nasdaq and TASE: NVMI) — dossier

Research date: 21 November 2026. **Fiscal year = calendar year (FY ends 31 December)**; FQ3 FY2026 = Jul–Sep 2026. USD unless stated; "k" = thousands. Every claim carries one tag ([F] fact read in a saved primary document, [C] company claim that cannot be tested, [S] secondary source, [I] my inference or calculation) and the id of its row in `evidence.csv`. Earnings-call content comes from third-party transcripts (stockanalysis.com, TradingKey) and is therefore tagged [S] even when it is management speaking. Arithmetic lives in `calc/`.

---

## 0. Premise check (prompt and inputs, corrected)

1. **Rules file.** `research/CLAUDE.md` on this branch held only a TODO. The full rules (Modules A and B, tags, self-check) were on branch `ccr-2b9561fc-mqqdg4` (commit 3bcba52); I copied that file and `research/tools/` onto this branch and followed them.
2. **prior/.** It is empty (only `.gitkeep`), so the "12 files exported from AI Studio" do not exist here and nothing was extracted to `prior/text/`. Notes from an earlier research branch (`ccr-34a6116a-tswdup`) were used as leads only, never as sources.
3. **"Materials metrology (XPS, SIMS, Raman)."** Correct, with one addition: VeraFlex is XPS **plus an optional low-energy XRF channel** [F] Q1-003, and Nova does not sell XRF stand-alone [S] Q3-009. So Nova does own an X-ray fluorescence capability, inside its XPS tools. This matters for Q4.
4. **"Wafer-level-packaging metrology acquired with Sentronics."** Sentronics Metrology GmbH (Mannheim) was bought on 30 Jan 2025 for $60.158M cash [F] A5-021. The acquired line (SemDex) was followed by WMC, which Nova presented as its "next-gen platform" [F] Q1-048 and released on 26 Aug 2025 [F] Q1-022.
5. **"Chemical metrology."** This came from the ancosys acquisition (25 Jan 2022, $90.2M including the earn-out) [F] A5-020.
6. **"Onto–Rigaku alliance since April 2026."** Confirmed. Rigaku's notice of a capital and business alliance was dated 21 Apr 2026, under which Onto buys 27.0% of Rigaku [F] XR-019. The deal closed on 10 Aug 2026 for JPY 113.08bn (about $720M) [F] XR-025. Joint CD-SAXS + OCD work began in May 2025 [F] XR-020.
7. **"Every series of convertible notes outstanding."** Only one series is outstanding: the 0% notes due 15 Sep 2030 ($750M) [F] A5-007. The 0% 2025 notes were fully converted during 2025 [F] A5-014.
8. **"China share by quarter since 2023."** Nova does not disclose China quarterly. Shares are annual in the 20-F [F] A4-001; the only quarterly figure is "approximately a third" for Q2 2023 [S] A4-010.
9. **"Process-equipment makers carry Nova's integrated tools."** Since 2008 Nova has sold substantially all products directly to chipmakers [F] Q6-003. Process-equipment makers (PEMs) integrate Nova's IM onto their tools rather than resell it, and the current partners are not named [F] Q6-001; [I] Q6-010.
10. **Packaging share.** On calls Nova splits product revenue in two (logic/foundry vs memory). Advanced packaging cuts across both and is given only approximately; it is not a third reported segment [S] A1-062–A1-065; [F] A1-061.
11. **"Nova statements since April 2026 about the Onto–Rigaku alliance."** I found none that names the alliance, Rigaku or CD-SAXS [I] Q3-011. The closest is a May 2026 answer on hybrid metrology (Q3 below).

---

## 1. Bottom line

- **Results.** LTM revenue was $1,000.7M (Oct 2025–Sep 2026), +17.4% YoY [I] A1-059. FQ3 FY2026 revenue was a record $287.8M, +28% YoY [F] A1-032, with GAAP operating margin 32.3% and non-GAAP 35.5% [I] A1-057.
- **Guidance.** Over the last 8 quarters Nova had no revenue or EPS miss: revenue 3 beats and 5 in-line; non-GAAP EPS 6 beats and 2 in-line [I] A3-017. The FQ4 FY2026 outlook is $305–315M [F] A3-019.
- **Balance sheet.** Cash, deposits and securities were $1.80B against $750M of 0% notes due 2030 [I] A5-006. Management says most of the cash is earmarked for M&A, possibly "at scale" [S] A5-029. It names only generic target areas [I] A5-031.
- **Packaging.** Advanced packaging was 15% of 2024 product revenue [F] A1-067, about 20% in 2025 and "nearly one-quarter" in Q2 2026 [S] A1-068, A1-070. No outside source confirms a named win against KLA, Onto, Camtek or Bruker [I] Q5-015.
- **China.** China was 33% of FY2025 revenue (39% in 2024) [F] A4-001, about $290.6M and up ~11% in dollars [I] B-010. The U.S.-made XPS and SIMS lines need BIS licences for Entity-List customers [F] A4-015, A4-017. The 50% Affiliates Rule is paused only until 10 Jan 2027 [F] A4-020.
- **X-ray.** Nova has no X-ray CD (SAXS) product, programme, partnership or acquisition. Its X-ray business is XPS plus LE-XRF film metrology [I] Q3-012, XR-018.
- **Optical CD vs X-ray CD (literature).** In GAA logic, OCD plus spectral interferometry and ML stays the in-line workhorse, and lab CD-SAXS is reference-grade [F] TH-020, TH-021. In high-aspect-ratio (HAR) memory, in-line CD-SAXS is already in fabs [F] TH-012 and is used to train ML-OCD [F] TH-009.
- **Main open contests.** XPS competition expected from 2H 2027 [S] Q3-009. The Onto–Rigaku CD-SAXS + OCD hybrid is due on memory lines in 1Q 2027 [C] XR-026.

---

## 2. Company-specific questions

### Q1. Product map with production status

| Line | Products | Applications | Customers named or described | Launch / key dates | Production status |
|---|---|---|---|---|---|
| **Optical CD, integrated** | i500, i550, i570 HP, i580 | CMP and etch process control mounted on the process tool; logic, memory, packaging. The i580 adds wafer-edge metrology for bonding [F] Q1-001, Q1-009, Q1-011, Q1-012 | "Thousands of deployments" [C] Q1-008. Adopted by 4 of the top 5 packaging makers [S] Q5-010 | i580 introduced 2025 [F] Q1-011. Older launch dates NOT DISCLOSED | Volume production. Nova claims IM-for-CMP leadership [S] Q6-006 |
| **Optical CD, stand-alone** | T500/T550 (matched to the IM fleet), MMSR+, VeloCD, Prism/Prism 2 | CD and films in complex 2D/3D stacks. Prism's spectral interferometry addresses 3D NAND, DRAM active area to capacitors, TSV, deep trench, FinFET, GAA [F] Q1-017–Q1-020 | Top IC maker, 3D NAND (Mar 2021) [F] Q1-014. Leading foundry, packaging (Aug 2023) [F] Q1-015. Leading logic maker, backside power (Oct 2024) [F] Q1-016. Samsung co-authored SI work [F] Q1-044, Q1-045 | Prism introduced 2020 [F] Q1-013. Prism 2 by Aug 2023 [F] Q1-015 | Volume production (multi-tool orders) [F] Q1-016 |
| **Packaging / WLP dimensional (Sentronics)** | SemDex; WMC | TTV, bow/warp, topography, roughness, TSV [F] Q1-021. CD/height of RDL and bumps, bonded-stack layers, die warpage [F] Q1-025 | Leading memory maker for HBM; orders from logic, memory and power-device makers [F] Q1-022. Tool of record at a leading foundry after a competitive evaluation (2 Jul 2026) [C] Q1-023. More than 10 customers [S] Q1-024 | Sentronics bought 30 Jan 2025 [F] A5-021. WMC released 26 Aug 2025 [F] Q1-022 | Volume production at the tool-of-record customer [C] Q1-023 |
| **Materials: XPS (+ LE-XRF)** | VeraFlex III, III+, IV | Thin-film thickness and composition: high-k/metal gate (HKMG), dipoles, SiGe(B) epi [F] Q1-003; XR-033 | Leading logic maker (Oct 2021) [F] Q1-027. Analog maker (Jul 2022) [F] Q1-028. GlobalFoundries uses it as process of record (POR) for SiGeB [F] XR-033. Up to 9 tools per fab at memory leaders [S] Q1-030 | XPS since the ReVera purchase (Apr 2015) [F] Q3-002. VeraFlex IV 2021 [F] Q1-026 | Volume production; Nova says "sole source" [S] Q3-007 |
| **Materials: SIMS** | Metrion | In-line depth profiles: epi, dopants, contamination, diffusion [F] Q1-004, Q1-033 | Leading logic maker (Jul 2022) [F] Q1-032. Leading memory maker, DRAM/NAND volume lines (Jan 2025) [F] Q1-034. Memory and logic leaders for GAA/DRAM (Jan 2026) [F] Q1-035. 4 of 5 target customers [S] Q1-036 | Launched 8 Dec 2021 [F] Q1-031. Gen 2 on 16 Jan 2024 [F] Q1-033 | Mixed: volume production at some, evaluation at others [S] Q1-036 |
| **Materials: Raman** | Elipson | Strain, crystallinity, phase, composition [F] Q1-005 | Memory volume-production order (Sep 2021) [F] Q1-037. Leading logic maker (Dec 2022) [F] Q1-038. Tool of record for GAA at a leading foundry (Oct 2025) [C] Q1-039 | Introduced 2020 [F] Q1-013 | Volume production at the tool-of-record foundry [C] Q1-039 |
| **Chemical metrology** | Ancolyzer (backend/packaging), AncoScene (front-end Cu/Co damascene), DMR (metal replenishment), AncoFlex (PCB/substrate) | Plating-bath analysis and replenishment, incl. TSV and WLP [F] Q1-006, Q1-007 | Five front-end fabs incl. a leading foundry (Feb 2022) [F] Q1-041. AncoScene released to volume production at a leading foundry in Q3 2026 [S] Q1-042 | ancosys bought 25 Jan 2022 [F] A5-020. Capacity doubled Jan 2025 [F] Q1-043 | Volume production. KLA is the only front-end rival [S] Q1-042 |
| **Software** | MARS (physical models), Nova Fit (ML), HPC, fleet management | Modelling for OCD and VeraFlex [F] Q1-029 | — | Nova Fit for VeraFlex IV: Nov 2024 [F] Q1-029 | Shipped |

- **Division mix.** Nova has three P&L divisions [F] Q1-046. Management's only stated split is about 40–50% dimensional, 30–40% materials and 10–20% chemical, which it expects to stay intact to 2027 [S] Q1-047.

### Q2. Limits of optical CD in HAR memory and GAA logic; where X-ray scatterometry enters

**3D NAND channel holes and contacts**
- **The core limit.** Samsung's flash team, writing with Nova, says the main HAR problem is how CD varies with depth [F] TH-002.
  - Bottom CD reached R² 0.89 only with spectral interferometry plus ML trained on reference CDs [F] TH-003.
  - The dedicated OCD target polishes 1.5–2x slower than the array, so in-cell measurement is needed [F] TH-004.
- **More limits from abstracts.** Carbon hardmasks are opaque in the usual OCD range [F] TH-006. Memory-hole OCD depends on destructive SEM/TEM reference [F] TH-007.
- **Where X-ray enters.**
  - IRDS says CD-SAXS already has the throughput for HAR contact holes, and in-line tools have been introduced [F] TH-012.
  - IBM + Nova confirm that in-line X-ray scattering has been demonstrated on channel holes [F] TH-015.
  - A SPIE 2026 abstract trains physics-informed ML on CD-SAXS CDs plus ellipsometry spectra (R² > 0.95 vs SEM) [F] TH-009. Its authors' affiliations are not disclosed on the volume page, so it should not be read as a Samsung paper.
- **Role left to OCD.** OCD keeps the small-spot, local and edge measurement; the CD-SAXS spot is about 300 µm [F] TH-010, TH-011. Inference: CD-SAXS is becoming a production reference and label source in HAR memory, not only a lab tool [I] TH-043 (Medium).

**DRAM capacitors / storage nodes**
- **Evidence is abstracts only.** Stacked-cylinder OCD models are inaccurate [F] TH-016. Physical-model compute rises steeply and labels are scarce [F] TH-017. ML-OCD is an ill-posed inverse problem [F] TH-018.
- **X-ray.** A vendor paper reports in-line T-SAXS on DRAM capacitors [F] TH-014.
- **Confidence.** No chipmaker full text was retrieved [I] TH-044 (Low).

**GAA nanosheet / CFET logic**
- **IRDS.** The main OCD problem is parameter cross-correlation [F] TH-019, yet scatterometry is still among the best in-line options for GAA [F] TH-020.
- **What logic CD-SAXS still needs.** In-line CD-SAXS needs under 1 min per site, a spot under 100 µm [F] TH-021, and sources at least 100x brighter [F] TH-022. IBM + Nova agree [F] TH-023.
- **IBM + Nova and imec + Nova papers.**
  - Scatterometry is the only non-destructive in-line method for sheet-specific indents [F] TH-026.
  - Tiny, correlated volumes are the limit [F] TH-027.
  - OCD tracks TEM at R² 0.85–0.99 on CFET steps [F] TH-031.
- **X-ray in logic.** It enters as XRF/XRD/XRR inputs and references, not as CD-SAXS [F] TH-029, TH-033, TH-034, TH-038, TH-040.
- **Inference.** In logic, OCD with ML remains the workhorse and X-ray CD is reference-grade [I] TH-045 (Medium).

**Hybrid cost**
- Hybrid metrology has been held back by cost of ownership [F] TH-036.

### Q3. Nova and X-ray

**Products and acquisition**
- **X-ray in Nova's portfolio.** Nova lists X-ray among its core technologies [F] Q3-001. X-ray came with ReVera (April 2015) [F] Q3-002.
- **Products.**
  - VeraFlex III, III+ and IV are in-line XPS tools with a simultaneous low-energy XRF channel [F] XR-002, XR-004, XR-006.
  - Nova claims the largest installed base of automated XPS/XRF tools [C] XR-003.
  - Nova does not sell XRF stand-alone [S] Q3-009.

**X-ray CD, partnerships and IP**
- **X-ray CD.** I found no Nova X-ray CD product, programme, partnership or acquisition [I] Q3-012, XR-018.
  - Nova's hybrid-metrology page names SEM and AFM, not SAXS [F] XR-010.
  - The only X-ray-scatterometry asset is an X-ray reflectance scatterometry patent family from ReVera (US patent granted Jan 2024; continuation published Mar 2026) [F] XR-014.
- **X-ray + OCD hybrids.** Nova's hybrids use film signals: an X-ray film + OCD offering from 2016 [F] XR-011; LE-XRF + scatterometry for Cu voids (2019) [F] TH-037; an XRF-enhanced OCD model (2026) [F] TH-040.
- **Partners.** Nova's X-ray work is co-authored with IBM Research and GlobalFoundries [F] XR-012, XR-033.

**Statements since April 2026**
- **The alliance.** None names the Onto–Rigaku alliance, Rigaku, CD-SAXS or T-SAXS [I] Q3-011. Nova's 20-F names Onto and KLA as its main competitors, not Rigaku [F] Q3-003.
- **Q1 2026 call (14 May 2026), asked about peers' X-ray opportunities.** The CEO said Nova's strategy "taps into hybrid metrology", with homegrown optical and X-ray [S] Q3-004.
  - He cited the IBM hybrid OCD + X-ray + ML work [S] Q3-005.
  - He flagged emerging XPS competition, including a local Chinese vendor [S] Q3-006.
- **Conferences and later call.**
  - BofA (3 Jun 2026): "currently a sole source"; competition expected "probably next year" [S] Q3-007.
  - Evercore (3 Jun 2026): X-ray tools have the longest lead times [S] Q3-008.
  - Q3 2026 call: new competition is "centered around XPS only" [S] Q3-009.

**The alliance itself (context)**
- **Rigaku targets.** A SAM of at least $300M by 2030 [C] XR-021. A CD-SAXS + OCD "Hybrid Engine" on memory production lines in 1Q 2027 [C] XR-026.
- **Onto claims.** Two key customers selected its AiDiffract + CD-SAXS offering, with systems delivered for V-NAND/DRAM [C] XR-022. Onto frames OCD as speed and X-ray as precision [C] XR-024.

### Q4. Overlap with Rigaku's film tools (XRF / XRD / XRR) and who holds the socket

Detail: `parts/XR_notes.md` §(c).

**Where the two compete**
- **HKMG and dipole ultra-thin films.** This is the most direct contest: VeraFlex XPS + LE-XRF against Rigaku MF-3400 (XRF/XRD) and ONYX 3200 (light-element XRF).
  - Rigaku markets ONYX explicitly against XPS [C] XR-028. It targets more than 70% of a $200M HKMG SAM [C] XR-030.
  - Nova calls VeraFlex the HKMG industry standard [C] XR-003.
  - No non-vendor source names the socket holder [I] XR-044.
- **Source/drain epi composition (SiGeB).** This is the same measurand. GlobalFoundries, co-authoring with Nova, says VeraFlex XPS is the process of record in a GF volume fab [F] XR-033. GF lists SIMS, XRD, XRF and XPS as the usual pad methods [F] XR-034.
- **Barrier/liner films.** IRDS lists XRR, XRF and acoustics for a barrier under Cu seed; XPS is not listed. No vendor is named [F] XR-038.

**Where they mostly complement each other**
- **SiGe/Si superlattice Ge %, thickness and strain.**
  - HR-XRD measures unpatterned targets after epitaxy and serves as the reference for Nova's in-die Raman and XPS [F] XR-035, XR-036, TH-039.
  - Trade press says HR-XRD is slow for volume production while Raman fits it [S] XR-041.
  - Rigaku claims POR at "more than half" of its major customers [C] XR-029.
  - Inference: complementary by measurement location [I] XR-045 (Medium).

**Market share**
- Rigaku, citing Yole, says it is No.1 in X-ray metrology (39.4% of $532M) and in film and materials metrology (20.6% of $1,016M) in 2025, with competitors left unnamed [C] XR-031, XR-032.
- Inference: Nova's "market leader" XPS claim and Rigaku's "No.1 in film metrology" claim cannot be reconciled without the unnamed Yole data [I] XR-044.

### Q5. Advanced packaging and hybrid bonding

**Share of revenue and definition**
- **Definition.** "Advanced packaging includes hybrid bonding and HBM processes" [F] A1-066.
- **Share by year.**
  - 2023: ~10% of *total* revenue [S] Q5-001.
  - 2024: 15% of *product* revenue [F] A1-067; [S] Q5-002.
  - 2025: ~20%, with packaging revenue up more than 60% [S] A1-068.
  - Q1 2026: "mid-20s" [S] A1-069. Q2 2026: "nearly one-quarter" [S] A1-070.
  - Q3 2026: not stated [F] A1-072.
- **Mix inside packaging.** HBM is about one-third [S] A1-071. Chemical metrology was about half in 2024 [S] Q5-005.
- **Targets.** The 2027 target of 20% was reached in 2025 [S] Q5-004. 2026 growth was guided only to "double-digit" [S] B-005.
- **Inconsistency.** The base switched from total to product revenue between 2023 and 2024. "More than doubled" in 2024 computes to about +56% on the stated shares [I] Q5-003.

**Tools sold by application**
- **Cu recess / dishing before hybrid bonding:** Prism [F] Q5-007. Bevel and edge: OCD-based edge metrology [F] Q5-007; i580 [F] Q1-012.
- **TSV:** Prism (about half of Prism 2 record bookings came from packaging such as TSV) [S] Q5-006; SemDex [F] Q1-021; TSV plating chemistry [F] Q1-007.
- **RDL:** WMC [F] Q1-025.
- **Wafer thickness, bow and warp:** WMC, SemDex [F] Q1-021, Q1-025.
- **Plating-bath control:** Ancolyzer, DMR, AncoScene [F] Q5-008, Q1-006.

**Customer wins against KLA, Onto, Camtek, Bruker**
- **Company-sourced wins only.**
  - WMC tool of record at a leading foundry after a competitive evaluation; the competitor is not named [C] Q1-023.
  - "A couple of customers" adopted WMC as tool of record [S] Q5-011.
  - Integrated metrology is at 4 of the top 5 packaging makers [S] Q5-010.
- **Who Nova competes with in packaging.** The 20-F names Merck and Camtek [F] Q5-012. The CEO also names Onto and KLA in OCD and KLA in chemical metrology [S] Q5-013.
- **Outside confirmation.** No non-vendor source documents a specific win against KLA, Onto, Camtek or Bruker [I] Q5-015.

### Q6. Integrated metrology channel

- **How the channel works.** Integrated optical CD and chemical metrology sales depend on PEMs selling process tools that can host them [F] Q6-001. Some PEM agreements carry exclusivity and joint-IP limits [F] Q6-002.
- **Direct selling.** Since 2008 Nova has sold substantially all products directly to chipmakers [F] Q6-003.
- **PEMs as rivals.** PEMs also compete through in-situ sensors (ASML, Lam, Applied) [F] Q6-004.
- **Which PEMs host Nova IM.** Current names are NOT DISCLOSED.
  - The last public naming I found is a January 2010 item: Applied Materials, Lam Research and Ebara CMP/etch tools [S] Q6-005.
  - The i570/i580 pages say they attach to "the industry's fastest CMP polishers" [F] Q1-010.
  - Chemical metrology entered a major OEM's qualified-vendor list in 2023 [S] Q6-008.
- **Share of revenue that depends on PEMs.** NOT DISCLOSED; IM revenue is not reported separately [I] Q6-010.
- **Competition in the channel.** One key IM competitor [S] Q6-007, which the CEO identifies as Onto [S] Q5-013.

---

## 3. Module A — numbers

### A1. Results (last four quarters and FY2025)

| | FQ4 FY2025 (Oct–Dec 2025) | FQ1 FY2026 (Jan–Mar 2026) | FQ2 FY2026 (Apr–Jun 2026) | FQ3 FY2026 (Jul–Sep 2026) | FY2025 | LTM Oct 2025–Sep 2026 |
|---|---|---|---|---|---|---|
| Revenue, $k [F] | 222,624 | 235,308 | 254,958 | 287,841 | 880,577 | 1,000,731 [I] |
| YoY [I] | +14.3% | +10.3% | +15.9% | +28.2% | +31.0% | +17.4% |
| Products / services, $k [F] | 174,954 / 47,670 | 186,263 / 49,045 | 201,472 / 53,486 | 231,861 / 55,980 | 705,598 / 174,979 | — |
| Gross margin GAAP / non-GAAP / ex one-offs [I] | 57.6 / 59.5 / 57.6% | 57.7 / 59.4 / 57.7% | 56.5 / 58.1 / 56.5% | 57.7 / 59.1 / 57.7% | 57.4 / 59.4 / 57.6% | 57.4 / 59.0 / 57.4% |
| Op. margin GAAP / non-GAAP / ex one-offs [I] | 27.3 / 31.6 / 27.4% | 30.1 / 34.2 / 30.1% | 29.9 / 33.4 / 29.9% | 32.3 / 35.5 / 32.3% | 28.8 / 33.2 / 29.2% | 30.0 / 33.8% |
| FCF (CFO − capex), $k [I] | 48,358 | 36,028 | 38,424 | 131,729 | 217,915 | 254,539 |
| SBC, $k [F] / SBC/FCF [I] | 6,977 / 14.4% | 7,305 / 20.3% | 6,764 / 17.6% | 7,079 / 5.4% | 26,291 / 12.1% | 28,125 / 11.0% |

Inputs are A1-001 to A1-047. Ratios come from `calc/metrics.py` [I] A1-051–A1-060.

- **One-off items management itself named** [F] A1-048, A1-049:
  - FY2025: acquisition inventory step-up $2.258M, acquisition expenses $0.859M (both Sentronics) and a discrete tax-reserve release $0.203M in operating income ($4.229M in net income).
  - FQ1–FQ3 FY2026: none listed.
  - FQ3 FY2026: the CFO attributed part of the opex rise to "costs related to ongoing strategic evaluations", not quantified and not excluded from non-GAAP [S] A1-050.
  - "Company-adjusted" (non-GAAP) also adds back recurring items: stock-based compensation, amortisation of acquired intangibles, lease/intercompany revaluation and debt-cost amortisation.
- **Segments.** Nova reports one segment [F] A1-061.
- **Product vs service gross margin, FY2025.** Products 60.0%, services 46.7% [I] A1-060.

**Addition: product vs service and end-market split, four quarters**

| Quarter | Services % of revenue [I] | Logic & foundry / memory, % of product revenue [S] | Implied memory product revenue [I] (Low) | Advanced packaging, % of product revenue |
|---|---|---|---|---|
| FQ4 FY2025 | 21.4% | 75 / 25 (A1-062) | ~$43.7M | FY2025 ~20% [S] A1-068 |
| FQ1 FY2026 | 20.8% | 66 / 34 (A1-063) | ~$63.3M | "mid-20s" [S] A1-069 |
| FQ2 FY2026 | 21.0% | 73 / 27 (A1-064) | ~$54.4M | "nearly one-quarter" [S] A1-070 |
| FQ3 FY2026 | 19.4% | 61 / 39 (A1-065) | ~$90.4M | NOT DISCLOSED [F] A1-072 |

Implied dollars are from `calc/segments.py` [I] B-012. Packaging sits inside the two buckets, mostly logic [S] A1-069. For reference, 2024 product revenue was logic 62%, memory 23% and packaging 15% [F] A1-067.

### A2. Leading signals (four-quarter trend)

| End of | FQ4 FY2025 | FQ1 FY2026 | FQ2 FY2026 | FQ3 FY2026 |
|---|---|---|---|---|
| Inventories, $k [F] | 183,671 | 178,850 | 185,273 | 200,731 |
| Deferred revenues (current), $k [F] | 67,163 | 49,092 | 45,945 | 64,949 |
| Trade receivables, $k [F] | 151,929 | 176,917 | 210,279 | 197,938 |
| DSO / inventory days [I] | 62.8 / 179 | 67.7 / 162 | 75.1 / 152 | 63.3 / 152 |

Sources: A2-001 to A2-012 [F]; ratios A2-013 [I].

- **Orders, backlog, book-to-bill.** NOT DISCLOSED. Nova calls backlog unreliable [F] A2-022. It reported record memory bookings in FQ3 FY2026 without a figure [S] A2-023 and claims visibility into 2027 [S] A2-024.
- **Remaining performance obligations (RPO).** RPO counts deferred revenue plus billed but unrecognised amounts and excludes unbilled orders: $65.5M at Dec 2023, $92.1M at Dec 2024 and $93.1M at Dec 2025 [F] A2-017–A2-019.
- **Inventory split (annual only)**, raw / service / WIP / finished goods [F] A2-014, A2-015:
  - Dec 2025: $58.4M / $43.2M / $41.6M / $40.5M.
  - Dec 2023: $50.2M / $31.4M / $31.9M / $24.8M.
  - Write-downs were $8.6M in 2025 [F] A2-016.
- **Non-cancelable purchase obligations.** $127.1M at Dec 2024 and $153.0M at Dec 2025 [F] A2-020, A2-021.

### A3. Guidance record

| Quarter guided (release) | Revenue guide → actual ($M) | GAAP EPS guide → actual | Non-GAAP EPS guide → actual |
|---|---|---|---|
| Q4 2024 (Q3 2024) | 181–191 → 194.8 **beat** | 1.51–1.70 → 1.58 in-line | 1.72–1.91 → 1.94 **beat** |
| Q1 2025 (Q4 2024) | 205–215 → 213.4 in-line | 1.75–1.91 → 2.03 **beat** | 2.00–2.16 → 2.18 **beat** |
| Q2 2025 (Q1 2025) | 210–220 → 220.0 in-line | 1.70–1.88 → 2.14 **beat** | 1.96–2.14 → 2.20 **beat** |
| Q3 2025 (Q2 2025) | 215–227 → 224.6 in-line | 1.77–1.97 → 1.90 in-line | 2.02–2.22 → 2.16 in-line |
| Q4 2025 (Q3 2025) | 215–225 → 222.6 in-line | 1.77–1.95 → 1.94 in-line | 2.02–2.20 → 2.14 in-line |
| Q1 2026 (Q4 2025) | 222–232 → 235.3 **beat** | 1.90–2.02 → 2.04 **beat** | 2.13–2.25 → 2.33 **beat** |
| Q2 2026 (Q1 2026) | 245–255 → 255.0 in-line | 2.10–2.24 → 2.20 in-line | 2.34–2.48 → 2.51 **beat** |
| Q3 2026 (Q2 2026) | 277–287 → 287.8 **beat** | 2.46–2.61 → 2.64 **beat** | 2.70–2.85 → 2.86 **beat** |

Guidance [F] A3-001…A3-015; verdicts [I] A3-002…A3-016.

- **Tally.** Revenue 3 beats / 5 in-line / 0 misses. GAAP EPS 4 / 4 / 0. Non-GAAP EPS 6 / 2 / 0 [I] A3-017.
- **Late misses.** No guidance was maintained late in a period and then missed. Nova gives no annual numeric guidance; its 2027 non-GAAP model is $1B revenue, 57–60% gross margin, 28–33% operating margin and ~$10 EPS [F] A3-020.
- **Revenue position.** All five in-line revenue quarters were in the upper half of the range [I] A3-017.
- **Longer record.** No miss found from FQ2 FY2020 to FQ3 FY2026 [I] A3-018.

### A4. Concentration and geography

- **Customers above 10%.** Customer A was 23% of total revenue in 2025 (18% in 2024) and Customer B 10% (14%) [F] A4-003. The top five were 51% (2025), 53% (2024), 52% (2023), 57% (2022) and 70% (2021) [F] A4-004, A4-005.
- **Per quarter (calls).** Customers and territories at ≥10% of product revenue [S] A4-006–A4-009:
  - FQ4 FY2025: 3 customers and 4 territories.
  - FQ1 FY2026: 4 customers and 5 regions.
  - FQ2 FY2026: 2 customers and 4 territories.
  - FQ3 FY2026: 4 customers and 4 territories.
- **Revenue by region (annual, % of total)** [F] A4-001, A4-002:

| | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|
| China | 28 | 36 | 39 | 33 |
| Taiwan | 32 | 18 | 20 | 29 |
| Korea | 13 | 20 | 18 | 16 |
| USA | 16 | 13 | 14 | 9 |
| Other | 11 | 13 | 9 | 13 |

- **Regions by quarter.** NOT DISCLOSED in releases or calls.
- **Restatements.** No prior-period figure changed between the FY2023, FY2024 and FY2025 20-Fs [F] A4-002.
- **China in dollars.** $186.5M (2023), $262.2M (2024), $290.6M (2025, +10.8%) [I] B-010.

**Addition: China by quarter since 2023 and management's direction**

| Period | China figure | Management comment |
|---|---|---|
| Q1 2023 | NOT DISCLOSED | China "especially strong" (call) |
| Q2 2023 | "approximately a third" [S] A4-010 | greenfield and mature-node expansions |
| Q3 2023–Q4 2024 | NOT DISCLOSED (FY2023 36%, FY2024 39% [F] A4-001) | Q3 2024: share to "moderate" as advanced nodes grow |
| Q1 2025–Q2 2025 | NOT DISCLOSED | China flat or slightly lower in dollars, lower in share |
| Q3 2025 | NOT DISCLOSED | 2025 China "nominally higher", share lower; business "normalized" in 2H 2025 [S] A4-014 |
| Q4 2025 | FY2025 33% [F] A4-001 | China "around 30% of our sales" in 2026; process control in China declined per external data [S] A4-011, B-006 |
| Q1 2026 | NOT DISCLOSED | China to "stabilize in the range of 25%-30%" long term [S] A4-012 |
| Q2 2026 | NOT DISCLOSED | — |
| Q3 2026 | NOT DISCLOSED | China rose in revenue and share in Q3; 2026 share below 2025 but "nominally grow" [S] A4-013 |

**Export rules that bind Nova** [F] A4-015–A4-021
- **Entity List.** Entity-List Chinese chipmakers "have acquired and continue to acquire" Nova tools, but its U.S. subsidiary cannot ship tools, parts or service to them without a BIS licence.
- **October 2022 rules.** They limit the U.S. subsidiary in "a small portion" of the Chinese market. Further rules followed in Oct 2023, Sep 2024 (GAAFET) and Dec 2024 (equipment, HBM, 140 entities).
- **Where products are made.** XPS and SIMS lines are made in Fremont, CA. Optical CD and Raman are made in Israel and are "not currently subject to control under Israeli law".
- **Affiliates Rule.** Issued Sep 2025, suspended from 10 Nov 2025 and extended to 10 Jan 2027 (91 FR 70789).
- **China's Ga/Ge export ban.** Suspended until 27 Nov 2026.

### A5. Balance sheet and capital

**Cash, debt and covenants**
- **Liquidity at 30 Sep 2026.** Cash $188.2M, short-term deposits $395.9M, current securities $493.3M, non-current securities $711.8M and long-term/restricted deposits $11.4M: $1,800.6M in total [F] A5-001–A5-004.
- **Debt.** The only debt is the 2030 notes, net carrying value $734.6M [F] A5-005, A5-016.
- **Net cash.** About $1,050.6M against principal [I] A5-006.
- **Next maturity.** 15 Sep 2030. There is nothing due in the next 12 months [F] A5-007.
- **Covenants.** None described [F] A5-015. The indenture itself is NOT RETRIEVED.

**Addition: convertible notes and capped calls**
- **2030 notes.** $750M of 0% senior unsecured notes, issued Sep 2025 and maturing 15 Sep 2030 [F] A5-007.
  - Initial conversion rate 3.1234 shares per $1,000 (about $320.16 per share, a 35% premium to $237.16) [F] A5-008, A5-013.
  - Settled in cash, shares or both at Nova's choice [F] A5-008.
  - Before 15 Jun 2030, holders may convert only on conditions, e.g. the share price at ≥130% of the conversion price for 20 of 30 trading days [F] A5-009. That trigger is $416.21 [I] B-011.
  - Optional redemption is from 20 Sep 2028. Note 11 also says "on or after October 20, 2028", an internal inconsistency [F] A5-010.
  - Fair value at Dec 2025 was ~$936.3M; effective rate 0.526% [F] A5-011.
- **Capped calls.** Cost $51.8M plus $1.4M in fees. The cap is $415.03 (a 75% premium). They are equity-classified [F] A5-012.
- **2025 notes.** $200M, 0%, conversion price ~$74.60. $181.5M converted in 2025 into 2,432,803 shares; none remain [F] A5-014.

**Buybacks**
- **$100M programme (Mar 2022).** $86.5M spent on 560,001 shares through Dec 2025 [F] A5-017.
- **$200M programme (2 Sep 2026).** $38.5M bought in FQ3 FY2026 [F] A5-018, A5-019.

**M&A in the last 5 years**
- **ancosys.** Bought 25 Jan 2022 for $90.2M ($81.7M cash plus an $8.5M earn-out at fair value, paid in 2022) [F] A5-020.
- **Sentronics.** Bought 30 Jan 2025 for $60.2M cash [F] A5-021.
- **Impairments.** None in 2023–2025 [F] A5-022.

**Addition: cash and stated M&A intent**
- **Priority.** Acquisitions are the stated top use of cash [F] A5-023; [S] A5-030.
- **Scale.** Most of ~$1.7B is "dedicated or designated" to M&A, possibly "at scale" [S] A5-029.
- **Target revenue.** $150–200M of inorganic revenue is targeted on top of the $1B organic plan [S] A5-026.
- **Areas named.**
  - "Complementary technologies such as materials, emerging metrology and [process]-control solutions, and adjacent high-growth market segments" [S] A5-025.
  - "Predominantly... semiconductor... process control" [S] A5-027.
  - Criteria: fit with the margin model, EPS-accretive within 12 months, and top-line or technology synergies [S] A5-028.
- **Live activity.** "Ongoing strategic evaluations" costs were booked in FQ3 FY2026 [S] A1-050.
- **Named targets.** None, and no technology such as X-ray CD has been named [I] A5-031.

### A6. Cycle — last two downturns

- **2023 downturn.**
  - Revenue peaked in FQ4 FY2022 (Oct–Dec 2022) at $151.2M and troughed in FQ2 FY2023 (Apr–Jun 2023) at $122.7M: −18.9% [F] A6-004, A6-006; [I] A6-009.
  - GAAP operating margin fell from 27.7% (FQ1 FY2022) to 23.4% (FQ2 FY2023): −4.3 pts. Non-GAAP fell from 34.7% to 27.6%: −7.1 pts [I] A6-009.
  - Annual revenue: FY2022 to FY2023 −9.3% [I] A6-009.
- **2019 downturn.**
  - FY2018 to FY2019 revenue −10.4% ($251.1M to $224.9M); GAAP operating margin 24.1% to 16.2% (−7.9 pts) [F] A6-001; [I] A6-003.
  - The quarterly trough was FQ2 FY2019 at $51.1M and 13.3% GAAP operating margin [F] A6-002.
  - The 2018 quarterly peak is NOT RETRIEVED; the 2019 releases are on sec.gov, which refused access.

---

## 4. Module B — close

### B1. Disputed-claims ledger

| Claim | Who said it, when | Evidence for | Evidence against | Strongest tag on each side |
|---|---|---|---|---|
| **1. Optical CD with ML keeps pace with HAR memory, so X-ray stays a niche reference tool** | Prompt claim. Nearest proponents: Nova's OCD+ML papers (Samsung+Nova Feb 2024; Nova review 2026) and the CEO's "hybrid" answer (May 2026) | SI+ML reached bottom-CD R² 0.89 in 3D NAND [F] TH-003. In logic, lab CD-SAXS is reference-grade only and needs ≥100x brighter sources [F] TH-021, TH-022. OCD tracks TEM at R² 0.85–0.99 on CFET [F] TH-031. Hybrid adoption is held back by cost of ownership [F] TH-036 | IRDS: in-line CD-SAXS tools are already in fabs for HAR holes [F] TH-012. CD-SAXS is the label source for ML-OCD (R² > 0.95) [F] TH-009. Proxy OCD targets misrepresent the array [F] TH-004. Onto: two key customers chose CD-SAXS, systems delivered for V-NAND/DRAM [C] XR-022. Rigaku: T-SAXS adopted in memory mass production [C] XR-027 | For: [F]. Against: [F]. Assessment [I] B-013: holds for logic, not for HAR memory (Medium) |
| **2. Materials metrology grows faster than dimensional** | Prompt claim. Nova's stated focus on materials [F] B-009 | Record materials bookings and up to 9 XPS tools per fab [S] Q1-030. Metrion at 4 of 5 targets [S] Q1-036. Elipson tool of record [C] Q1-039 | Nova reports one segment [F] A1-061. Management expects the 40–50 / 30–40 / 10–20 division ratio to stay "intact" to 2027 [S] Q1-047. Q3 2026 memory growth was "supported equally" by dimensional and materials [S] B-008. Yole via Rigaku: the film and materials metrology market shrank in 2025 [C] XR-032. XPS competition expected in 2H 2027 [S] Q3-009 | For: [S]. Against: [F] (no data) and [S]. Assessment [I] B-014: unsupported by company data (Medium) |
| **3. Advanced packaging becomes a material share of revenue** | Prompt claim. Nova Investor Day 2025 set a 20% target for 2027 [S] Q5-004 | 15% of 2024 product revenue [F] A1-067. ~20% in 2025 [S] A1-068. Mid-20s in 1H 2026 [S] A1-069, A1-070. Record packaging revenue in FQ3 FY2026 [F] A1-072. WMC tool of record [C] Q1-023 | Packaging is not a reported segment and shares are rounded call figures [F] A1-061. The base and the growth wording are inconsistent [I] Q5-003. 2026 growth guided only "double-digit" [S] B-005. No outside confirmation of wins [I] Q5-015 | For: [F]. Against: [S]. Assessment [I] B-015: already material (~$141M, ~20% of FY2025 product revenue); durability and definition are the open points (Medium) |
| **4. Nova's China revenue is sustainable under current export rules** | Prompt claim. Management (Feb, May, Nov 2026): China ~30%, 25–30% long term, nominally growing [S] A4-011–A4-013 | China revenue $290.6M in 2025, +10.8% [I] B-010. Israel-made products are not controlled under Israeli law [F] A4-018. The U.S. rules hit "a small portion" of the Chinese market [F] A4-016. Affiliates Rule paused to 10 Jan 2027 [F] A4-020 | Entity-List customers buy Nova tools, and the U.S.-made XPS/SIMS lines need licences [F] A4-015, A4-017. Licences partly suspended in Nov 2023 [F] A4-016. The Affiliates Rule can resume on 10 Jan 2027 [F] A4-020. Local Chinese XPS competitor [S] Q3-006. Shorter lead times reduce visibility [S] B-007 | For: [F]. Against: [F]. Assessment [I] B-016: sustainable under rules in force today; the main dated risk is Jan 2027 (Medium) |
| **5. (found) Nova is sole source in in-line XPS and will hold it when competitors arrive** | Nova CEO, BofA 3 Jun 2026 and Q3 call 5 Nov 2026 [S] Q3-007, Q3-009 | GlobalFoundries runs VeraFlex as POR for SiGeB [F] XR-033. Largest installed base claimed [C] XR-003. Up to 9 tools per fab [S] Q1-030 | Entrants expected 2H 2027, including a local Chinese vendor [S] Q3-006, Q3-009. Rigaku sells light-element XRF against XPS for dipoles [C] XR-028 and targets >70% of the HKMG SAM [C] XR-030. Rigaku claims No.1 in film metrology [C] XR-032 | For: [F]. Against: [C]. Assessment [I] B-017: open; first test in 2H 2027 (Low) |
| **6. (found) The Onto–Rigaku CD-SAXS + OCD hybrid will take memory OCD sockets** | Onto, 20 Apr 2026; Rigaku roadmap, Nov 2026 [C] XR-022, XR-026 | Two key customers selected AiDiffract + CD-SAXS [C] XR-022. In-line CD-SAXS already in HAR memory [F] TH-012. Onto now owns 27% of Rigaku [F] XR-025 | Nova memory revenue and bookings at a record in FQ3 FY2026 [S] A2-023. OCD keeps the local/edge role [F] TH-010. Hybrid cost of ownership [F] TH-036. The Hybrid Engine is still a 1Q 2027 target [C] XR-026 | For: [F]. Against: [F]. Assessment [I] B-018: open; first test in 1Q 2027 (Low) |

### B2. Three facts that most weaken each reading

**Against the optimistic reading**
1. Nova expects new XPS competitors from 2H 2027 in the materials line where it calls itself "sole source" [S] Q3-007, Q3-009.
2. China was 33% of FY2025 revenue. Nova's U.S.-made XPS/SIMS lines need BIS licences for Entity-List customers, and the Affiliates Rule pause ends 10 Jan 2027 [F] A4-001, A4-015, A4-020.
3. Onto, Nova's main optical CD rival, now owns 27% of Rigaku [F] XR-025. It reports two key customers for its CD-SAXS offering with systems delivered for V-NAND/DRAM [C] XR-022.

**Against the pessimistic reading**
1. FQ3 FY2026 revenue was a record $287.8M, +28% YoY. The FQ4 outlook is $305–315M [F] A1-032, A3-019.
2. Cash and investments of $1,800.6M face $750M of 0% notes not due until 15 Sep 2030. There were no impairments in 2023–2025 [F] A5-001–A5-005, A5-007, A5-022.
3. IRDS says in-line CD-SAXS for logic needs sources at least 100x brighter, and that scatterometry remains among the best in-line options for GAA [F] TH-020, TH-022.

### B3. Dated catalysts, next 12 months

| Date | Event | Tag / id |
|---|---|---|
| 27 Nov 2026 | End of China's suspension of its Ga/Ge export ban (per 20-F); current status not checked | [F] A4-021 |
| By 31 Dec 2026 | New Asia cleanroom operational | [S] B-002 |
| 10 Jan 2027 | BIS Affiliates Rule suspension ends unless extended | [F] A4-020 |
| ~Feb 2027 (date NOT DISCLOSED; FY2025 results came 12 Feb 2026) | FQ4 FY2026 results. Tests: >$1B FY2026 revenue; $500M cumulative 2024–26 GAA target; FQ4 guide $305–315M | [F] A3-019; [S] B-004 |
| ~Feb 2027 | 20-F FY2026 (geography, customer concentration, RPO) | [I] pattern of A4-001 |
| 9 Mar 2027 | Investor Day, NYC: new long-term model | [F] B-001 |
| 1Q 2027 (Jan–Mar 2027) | Rigaku/Onto CD-SAXS + OCD Hybrid Engine on memory lines; first GI-SAXS logic unit | [C] XR-026 |
| ~May, Aug, Nov 2027 | FQ1–FQ3 FY2027 results (dates NOT DISCLOSED) | — |
| 2H 2027 | Expected first XPS competitors | [S] Q3-009 |
| 2027 | Metrion fifth target customer | [S] Q1-036 |
| Each quarter | 2030-note conversion test (≥$416.21 for 20 of 30 days); no debt maturity or lock-up within 12 months | [I] B-011; [F] A5-007 |

### B4 and B5
- The gap log is in `gaps.md`.
- The handoff row and the extra Rigaku/Onto cell are in `handoff.md`.
