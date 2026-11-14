# Independent science and engineering evidence behind fast power for data centres (state of knowledge at 14 November 2026)

Scope: independent technical evidence for the technology classes used by GE Vernova, Siemens Energy, Bloom Energy, Caterpillar (incl. Solar Turbines), Hitachi Energy, Schneider Electric and HD Hyundai Electric. Data and information only; no rankings, recommendations or investment views.

Source tags: **[company]** = controlled by one of the seven companies; **[independent]** = everything else. Where an "independent" source is itself a vendor or has a financial interest (NVIDIA, Kohler, Emerald AI, Mitsubishi Power, UL, a short-seller-affiliated newsroom), this is stated next to the tag. "Via search summary" means the fact came from a search-engine result snippet/summary of the cited URL and the page itself was not opened; treat those as lower confidence. HHV = higher heating value, LHV = lower heating value. Unless stated, conversions use the SGIP report's natural-gas LHV/HHV ratio of 0.9019 and the EPA factor of 53.06 kg CO2/MMBtu (both cited below).

---

## 1. Heavy-duty and aeroderivative gas turbines

### Takeaway
Gas turbines stand on solid technical ground as a mature, heavily deployed technology with independently audited fleet performance data (EIA) and third-party-recognised efficiency records. In practice, though, the US combined-cycle fleet averages about 45% HHV (about 50% LHV) against a record of 64.18%. The binding constraints in 2026 are manufacturing (rotor forgings, single-crystal hot-section blades, castings), not physics. For AI loads, the independent evidence shows two problems. Sub-second load swings are faster than turbine governors and combustors can follow. And repetitive AI power oscillations can line up with turbine-generator shaft torsional modes and grid oscillation modes. Turbines therefore need storage, load-side smoothing or a grid connection to serve AI training loads. Hydrogen blending at 20–50% by volume has been demonstrated on Mitsubishi units with EPRI on site. For the GE Vernova and Siemens Energy hydrogen claims, this session found no independently verified results.

### Cited Findings

**Efficiency records versus fleet reality**
- The current Guinness record for "most efficient combined cycle power plant" is **64.18%**, held by Siemens Energy at SSE Thermal's Keadby 2 (North Lincolnshire, UK). It was achieved and verified on **21 May 2024**. The Guinness page does **not** say whether the figure is net or gross, LHV or HHV, or who measured it. Keadby 2 also holds the record for "most powerful combined cycle power plant". — [Guinness World Records, record 431420, verified 21 May 2024](https://www.guinnessworldrecords.com/world-records/431420-most-efficient-combined-cycle-power-plant) [independent]
- Keadby 2's output is listed as **849.45 MW** (via search summary of the German Guinness listing). — [guinnessworldrecords.de, record 431420](https://guinnessworldrecords.de/world-records/431420-most-efficient-combined-cycle-power-plant) [independent]
- Earlier records for GE HA-class plants: EDF Bouchain, France, **62.22%** (2016, the first record in this category; reported as net), and Chubu Electric Nishi-Nagoya Block 1, Japan, with GE 7HA turbines, **63.08% gross** (2018). The two figures use different bases (net versus gross), so they are not directly comparable (via search summary). — [Guinness World Records news, July 2016](https://www.guinnessworldrecords.com/news/commercial/2016/7/general-electric-and-edf-build-world%E2%80%99s-most-efficient-combined-cycle-power-plant-434523); [Power Engineering, 27 Mar 2018](https://www.power-eng.com/2018/03/27/ge-powered-plant-awarded-world-record-efficiency-by-guinness/) [independent]
- EIA full-load *tested* heat rates for US natural gas units in 2025 (weighted by net summer capacity, Form EIA-860):
  - combined cycle: **7,535 Btu/kWh** (7,655 in 2015)
  - simple-cycle gas turbine: **10,975 Btu/kWh** (11,302 in 2015)
  - internal combustion: **8,853 Btu/kWh**
  - steam: **10,293 Btu/kWh**

  — [EIA Electric Power Annual, Table 8.2, data 2015–2025, accessed 14 Nov 2026](https://www.eia.gov/electricity/annual/html/epa_08_02.html) [independent]
- EIA *operating* heat rate (EIA-923/EIA-860) for all natural gas generation: **7,781 Btu/kWh in 2025**, 7,754 in 2024 and 7,869 in 2015. — [EIA Electric Power Annual, Table 8.1](https://www.eia.gov/electricity/annual/html/epa_08_01.html) [independent]

**Ambient derating (fleet-level indicator)**
- US natural gas capacity in 2025 was **578,378.8 MW nameplate**, **513,400.6 MW net summer** and **549,882.8 MW net winter**. — [EIA Electric Power Annual, Table 4.3 "Existing Capacity by Energy Source, 2025"](https://www.eia.gov/electricity/annual/html/epa_04_03.html) [independent]

**Start-up and ramping (versus load dynamics)**
- NERC: large power-electronic loads "can shift their consumption in seconds, much quicker than conventional generators can ramp". Loads that ramp within seconds or minutes need fast-frequency-response services, and rapid ramp-downs "may necessitate units that can rapidly shut down" (white paper, July 2025). — [NERC Large Loads Task Force white paper, "Characteristics and Risks of Emerging Large Loads", July 2025](https://www.nerc.com/globalassets/who-we-are/standing-committees/rstc/whitepaper-characteristics-and-risks-of-emerging-large-loads.pdf) [independent]
- NVIDIA states that generation resources "can take one minute to 90 minutes to respond to sudden ramp-ups because of their physical ramp-rate limits" (28 Jul 2025, updated 27 Aug 2025). This is a vendor statement and is not unit-specific. — [NVIDIA Technical Blog, "How New GB300 NVL72 Features Provide Steady Power for AI"](https://developer.nvidia.com/blog/how-new-gb300-nvl72-features-provide-steady-power-for-ai) [independent – vendor, not one of the seven]

**Interaction of AI load oscillations with turbine-generators**
- The joint Microsoft/OpenAI/NVIDIA paper reports that FFT energy in production AI-training power traces is concentrated between **0.2 and 3 Hz**. It lists grid resonance bands at <1 Hz (long lines), ~1–2.5 Hz (closely coupled sources) and **≥~7 Hz (shaft torsional modes)**. It cites a 2019 event in which a ~200 MW oscillating source at a Florida combined-cycle unit drove wide-area oscillations, and it discusses steam turbine-generator torsional resonance and sub-synchronous resonance (arXiv:2508.14318, submitted 20 Aug 2025, v2 21 Aug 2025). — [Choukse et al., "Power Stabilization for AI Training Datacenters", arXiv](https://arxiv.org/html/2508.14318) [independent – authors from Microsoft, OpenAI and NVIDIA, none of the seven]
- NERC (July 2025) warns that AI data centres can have "periodic, repetitive, and sustained" load profiles. Forced oscillations at sub-synchronous frequencies may cause "accelerated aging of BPS equipment (generators in particular)". NERC cites the 1970s Mohave generator shaft failures from sub-synchronous resonance. — [NERC LLTF white paper, July 2025](https://www.nerc.com/globalassets/who-we-are/standing-committees/rstc/whitepaper-characteristics-and-risks-of-emerging-large-loads.pdf) [independent]

**Hydrogen co-firing demonstrations**
- **June 2022, Georgia Power Plant McDonough-Atkinson** (Georgia Power, Mitsubishi Power, EPRI):
  - The test ran **20% hydrogen by volume** in one Mitsubishi M501G (~265 MW) at partial and full load, at the design natural-gas firing temperature.
  - Turndown up to 20% H2 was tested at minimum emissions-compliant load.
  - Results: about **7% CO2 reduction**, operation "within emissions compliance" and no impact on maintenance intervals.
  - No NOx figures were published. EPRI was "on-site", but independent EPRI measurement is not confirmed in the article.

  — [POWER magazine, 16 Jun 2022](https://www.powermag.com/southern-co-gas-fired-demonstration-validates-20-hydrogen-fuel-blend/) [independent]
- **June 2025**: Georgia Power and Mitsubishi Power reported a **50% hydrogen** blend on an M501GAC at partial and full load, with about **22% CO2 reduction** (via search summary). — [Business Wire, 16 Jun 2025](https://www.businesswire.com/news/home/20250616385154/en) [independent – utility/vendor release; neither is one of the seven]

**Known reliability problems (HA class)**
- **September 2018**: an "oxidation issue" on a GE 7HA component shut down one unit at Exelon's Colorado Bend plant in Texas. Exelon idled three others as a precaution.
  - The issue was found during planned outages.
  - At the time GE had 82 7HA orders, had shipped 51 machines and had installed 30.
  - GE said it had "identified the solution".

  — [Utility Dive, 21 Sep 2018](https://www.utilitydive.com/news/trouble-in-texas-causes-shutdown-of-advanced-ge-turbine/532901/) [independent]
- GE said the stage-1 blade oxidation issue could also affect 9FB units (reportedly ~75 machines). EDF's Bouchain HA plant was also shut down. GE described "cold oxidation" inside the blade, with oxidation at the blade shank leading to a crack (via search summary, Sept–Oct 2018 coverage). — [Turbomachinery Magazine, 2018](https://turbomachinerymag.com/view/general-electric-says-blade-problem-affects-more-gas-turbines); [Modern Power Systems, "The Colorado Bend saga"](https://www.modernpowersystems.com/news/the-colorado-bend-saga-latest-from-ge-6804533/) [independent]

**Supply chain: castings, forgings, single-crystal blades**
- EPRI experts John Shingledecker and Bobby Noble (POWER magazine, **15 Jan 2026**) said:
  - **Rotor forgings and hot-section blades are "the primary bottlenecks"**.
  - Some large frame turbines have shipped *without rotors or blades*, which are installed on site later.
  - Large forgings have few suppliers worldwide.
  - Utilities needing capacity by 2028 face backlogs extending to 2030.
  - Data centres compete for 30–100 MW turbines.
  - Orders for turbines under 20 MW hit records in 2025.
  - Aeroderivatives compete with commercial aviation for supply.
  - EPRI's process compensated resonance testing (PCRT) has caught quality issues early.

  — [POWER magazine via Yahoo Finance, 15 Jan 2026](https://finance.yahoo.com/news/gas-turbine-supply-chain-bottlenecks-130656088.html) [independent]
- On **8 Sep 2026**, GE Aerospace (a separate company from GE Vernova) agreed to buy castings maker Consolidated Precision Products for **$11.75 bn**, citing castings bottlenecks. About 60% of CPP's revenue is commercial aerospace; the rest is defence, power and other markets. Closing is expected in H2 2027. — [GE Aerospace press release, 8 Sep 2026](https://www.geaerospace.com/news/press-releases/ge-aerospace-acquire-consolidated-precision-products-cpp-expanding-mission-critical); [BNN Bloomberg, 8 Sep 2026](https://www.bnnbloomberg.ca/business/2026/09/08/ge-aerospace-to-buy-castings-maker-cpp-for-nearly-us12-billion/) [independent]
- Secondary, unverified figures from blog/newsletter sources, via search summary:
  - Wood Mackenzie data put global gas-turbine orders at ~110 GW at end-2025 against ~60–70 GW/yr manufacturing capacity.
  - A set of 40 single-crystal blades costs >$600,000 and takes 60–90 weeks.
  - A new single-crystal foundry takes 4–6 years to build (another analyst says ~2 years to first qualified production).

  The primary Wood Mackenzie document was not seen. — [Paradox Intelligence](https://www.paradoxintelligence.com/themes/gas-turbine-manufacturing-bottleneck-power-ai-demand); [Industrial Sage](https://www.industrialsage.com/gas-turbine-manufacturing-capacity-bottleneck/) [independent – low confidence]

### Inferences
- Converting EIA's 2025 tested heat rates with 3,412 Btu/kWh:
  - US combined-cycle fleet: ≈45.3% HHV ≈ 50.2% LHV.
  - Simple-cycle gas turbines: ≈31.1% HHV ≈ 34.5% LHV.

  The 64.18% record is a best case for a new, clean, full-load plant and is roughly 14 percentage points above the US fleet average, even if the record is on an LHV basis.
- If the 64.18% figure is net LHV, it equals ≈57.9% HHV, ≈5,895 Btu/kWh and ≈0.31 t CO2/MWh. The Guinness page does not confirm the basis, so this conversion is conditional.
- CO2 intensity at EIA 2025 tested heat rates:
  - combined cycle ≈0.40 t/MWh (≈881 lb/MWh)
  - simple cycle ≈0.58 t/MWh (≈1,284 lb/MWh)
- In 2025, net summer gas capacity was 6.6% below net winter capacity and 11.2% below nameplate (EIA Table 4.3). This is consistent with hot-weather derating of gas-fired units, but EIA's seasonal ratings also reflect other factors, so it is an indicator, not a per-unit derating curve.
- 20% H2 by volume giving only ~7% CO2 reduction (and 50% giving ~22%) follows from hydrogen's low volumetric energy density. Meaningful decarbonisation through blending needs very high H2 fractions.
- The HA-class oxidation episode surfaced in **September 2018**, not 2019. The 2019 references in the brief likely refer to the remediation period.
- On the evidence gathered, gas turbines can supply bulk energy reliably, but no independent source in this session documents a gas turbine following AI-training swings (0.2–3 Hz, up to 1.9 p.u./s, section 7) without storage or load-side smoothing.

### Gaps
- No independent, unit-specific data were obtained on start times or ramp rates for heavy-duty versus aeroderivative units. The usual figures (aeroderivatives starting in ~5–10 min; heavy-duty simple cycle in ~10–30 min) are vendor claims. This session could not reach independent sources: NREL was not reachable from this environment, and the search budget was exhausted.
- No source was obtained on part-load efficiency curves or per-°C ambient derating coefficients.
- The text of EPA NSPS Subpart KKKK (NOx limits), the status of the proposed KKKKa revision, typical SCR permit limits (BACT), CO limits and ammonia slip could not be retrieved: eCFR redirected to an "unblock" page.
- No source on water use was retrieved (NREL's Macknick et al. factors were unreachable).
- This session could not verify GE's Long Ridge 5% hydrogen test (2022), its planned 20% phase, Siemens Energy's HYFLEXPOWER 100% hydrogen test, or any independent EPRI report on the McDonough tests.
- No independent post-2018 data were found on whether the HA blade fix proved durable, and no information on any 2025–2026 HA, HL or aeroderivative fleet issues.
- The net/gross and LHV/HHV basis and the measuring party for the Keadby 2 64.18% record were not found.

---

## 2. Reciprocating gas and diesel engines

### Takeaway
Reciprocating engines stand on solid ground: they are mature, modular and covered by an established transient-performance standard (ISO 8528-5). The independent and vendor evidence agrees that lean-burn **gas** engines accept load in smaller steps and recover more slowly than **diesel** engines. Caterpillar's own white paper says gas units typically have lower load acceptance than diesel and suggests running gas at base load with diesel following load. Gas engines alone therefore cannot match diesel block-loading or follow fast AI swings without staged loading, UPS ramp stretching or batteries. US fleet data show natural-gas internal-combustion units at about 38.5% HHV (≈42.7% LHV) full-load tested efficiency. Independent data on maintenance, availability and multi-hundred-MW engine plants serving data centres were not obtained in this session.

### Cited Findings
- **ISO 8528-5:2022** sets transient performance classes G1–G4 (G4 user-defined), as reproduced from the standard's Table 4. Class G3 is the tightest standard class:
  - transient frequency deviation on sudden load increase ≤ −15% (G1), ≤ −10% (G2), **≤ −7% (G3)** from rated
  - on 100% load rejection ≤ +18% / +12% / **+10%**
  - frequency recovery ≤ 10 s / 5 s / **3 s**
  - transient voltage deviation on load increase ≤ −25% / −20% / **−15%**, and on rejection ≤ +35% / +25% / **+20%**
  - voltage recovery ≤ 10 s / 6 s / **4 s**

  — [Kohler Energy (B. Wudtke), "ISO 8528-5 and Generator Transient Performance", Power Systems Topics 143, undated; cites ISO 8528-5:2022](https://techcomm.kohler.com/techcomm/pdf/ISO%208528-5%20and%20Generator%20Transient%20Performance_WP.pdf) [independent – genset vendor, not one of the seven]
- Kohler on how the standard is applied and where gas engines differ:
  - Load-acceptance testing uses BMEP-based load steps, and "higher BMEP engines take smaller steps".
  - Rejection is tested as a single 100% step.
  - For G3, the frequency limits are given as **±7%/±10% for diesel and ±15%/±10% for gas**.
  - "Gaseous engines respond slower than diesel due to fuel delivery differences".
  - Standby ratings typically assume ≤200 h/yr (some models up to 500 h).
  - Kohler calls a 0–100% single load step "an unrealistic scenario" under the standard's approach.

  — [Kohler white paper (as above)](https://techcomm.kohler.com/techcomm/pdf/ISO%208528-5%20and%20Generator%20Transient%20Performance_WP.pdf) [independent – vendor]
- Caterpillar's white paper (via search summary; the page fetch timed out):
  - It states that "gas units would typically have lower load acceptance capabilities than diesel units".
  - It suggests running gas units in base-load mode and diesel units in load-follow mode.
  - It proposes load sequencing, "stretching of uninterruptible power supply ramp times" and smaller block loads to fit gas units.
  - It states that new gas-engine technology "begins to approach" diesel performance.

  — [Caterpillar, "Converting Data Centers From Diesel To Gas Power Generation" (undated)](https://www.cat.com/en_IN/by-industry/electric-power/Articles/White-papers/converting-data-centers-from-diesel-to-gas-power-generation.html) [company]
- US natural gas internal-combustion units had a full-load tested heat rate of **8,853 Btu/kWh in 2025** (9,322 in 2015). Petroleum internal-combustion units were 10,484 Btu/kWh in 2025. — [EIA Electric Power Annual, Table 8.2](https://www.eia.gov/electricity/annual/html/epa_08_02.html) [independent]
- In California's SGIP program (2019; mostly small CHP engines) measured internal-combustion engines showed:
  - electrical conversion efficiency **36%**, thermal 22%, system 58%; capacity factor 34%
  - non-renewable GHG rate **0.62 t CO2/MWh (2018) and 0.54 t (2019)**, against 0.25–0.26 t/MWh of avoided grid generation

  The evaluation used an LHV basis. — [Verdant Associates, "2018-2019 SGIP Impact Evaluation", 14 Jan 2021, Tables ES-3, 5-1, 5-2](https://www.cpuc.ca.gov/-/media/cpuc-website/divisions/energy-division/documents/self-generation-incentive-program/sgip_impact_report_2018-2019_finaldraft.pdf) [independent]
- EPRI's DCFlex ran a field emissions test (contractor Mostardi Platt) at a Compass Datacenters site in Dallas on **6 May 2026**. It compared HVO renewable diesel with fossil diesel on a **2 MW Cummins QSK60** backup engine at 50% and 100% load, with a GREET-based lifecycle GHG assessment. The page names the pollutants measured but gives no values. — [EPRI DCFlex Demonstrations page, accessed 14 Nov 2026](https://dcflex.epri.com/demonstrations) [independent]
- EPRI (Jan 2026) notes that "aeroderivative and reciprocating engine plants are gaining traction" as near-term options while large-frame turbines are backlogged. — [POWER magazine via Yahoo Finance, 15 Jan 2026](https://finance.yahoo.com/news/gas-turbine-supply-chain-bottlenecks-130656088.html) [independent]

### Inferences
- An 8,853 Btu/kWh heat rate converts to ≈38.5% HHV (≈42.7% LHV) and ≈0.47 t CO2/MWh (≈1,036 lb/MWh). This is higher CO2 per MWh than the combined-cycle fleet (≈0.40 t) and lower than simple-cycle turbines (≈0.58 t).
- The ISO 8528-5 G3 limits allow a −7% (diesel) to −15% (gas) frequency dip for each BMEP-limited load step. AI training swings of about 1.9 p.u./s (section 7) would be large repetitive steps for an islanded engine plant. On this evidence, gas-engine islands serving AI training would need electrical buffering (UPS, BESS or capacitors) and/or GPU-side ramp limits. The standard's step-based test regime does not directly test repetitive 0.2–3 Hz oscillatory loading.
- Caterpillar's own text concedes the gas-versus-diesel load-acceptance gap. Any claim that gas gensets are a drop-in replacement for diesel block-load backup should therefore be checked against model-specific ISO 8528-5 step data.

### Gaps
- No independent data were obtained on:
  - lean-burn gas engine block-load percentages by model
  - maintenance intervals, overhaul cycles or availability statistics
  - fleet experience of engine plants at 100–500+ MW serving data centres (scaling, controls, N+x redundancy)
- NOx, CO and particulate limits were not retrieved: EPA NSPS IIII/JJJJ, RICE NESHAP ZZZZ, Tier 4 Final, SCR/oxidation-catalyst performance, and the 100 h/yr limit on emergency engines for maintenance and testing (eCFR blocked).
- NFPA 110 Level 1/Type 10 (10-second start) requirements could not be verified from the standard text.
- The emissions results of the EPRI HVO test (6 May 2026) were not published on the page.
- Caterpillar/Solar Turbines industrial gas turbine performance: no independent data obtained.

---

## 3. Solid-oxide fuel cells

### Takeaway
The underlying science stands on solid ground: laboratory short-stacks have run for 100,000 h with average voltage degradation of about 0.5%/1,000 h, and some phases are as low as ~0.1%/1,000 h. Commercial field evidence is weaker and contested, however. California's independent SGIP evaluation measured electric-only fuel cells at about **53% (LHV) electrical efficiency** in 2019, with GHG emissions of 0.36 t CO2/MWh. That rate is higher than the California grid generation they displaced. A July 2026 data analysis by a short-seller-affiliated newsroom found:
- Bloom efficiency falling by about 2.4 percentage points per year in New York data
- output averaging well below 95% of nameplate across US datasets
- many units falling below contractual efficiency guarantees well before the ~5-year stack-replacement interval Bloom describes

Bloom's own Q2 2026 10-Q refers to "fleet degradation" and a jump in warranty accruals. On CO2, a Bloom unit at its datasheet efficiency is roughly at parity with a new best-in-class combined cycle. It is better than the US combined-cycle fleet average and much better than simple-cycle turbines or engines, but the advantage shrinks as stacks degrade. Independent evidence on SOFC start-up time, load-following of AI swings and hydrogen operation was **not** found in this session.

### Cited Findings

**Laboratory and stack degradation (peer-reviewed / research institute)**
- A two-layer short stack of anode-supported SOFCs ran galvanostatically for **100,000 h at 700 °C and 0.5 A/cm²**. The degradation slope varied over time, and the **overall voltage degradation was 0.5% per 1,000 h**. This is from a 2020 paper reported as Journal of Power Sources (via search snippet). The snippet does not name the institution, and the page was not retrievable. — [peeref record of the paper](https://peeref.com/works/21460552) [independent]
- In long-term testing (>20,000 h) under realistic stack conditions at Forschungszentrum Jülich, degradation in "zone III dropped drastically to around **0.1%/kh** and remained stable until the end of life" (2025, via search snippet; full text returned HTTP 403). — [J. Mater. Chem. A, 2025, d5ta03917g](https://pubs.rsc.org/en/content/articlehtml/2025/ta/d5ta03917g) [independent]
- Jülich reported cutting voltage degradation to about **0.1% per 1,000 h at 700 °C** in a short-stack test that had passed 15,000 h. The Real-SOFC benchmark stack had completed **40,000 h by March 2012** (2013 summary, via search snippet). — [TIB document](https://edocs.tib.eu/files/e01fb16/869048252.pdf) [independent]
- Thunder Said Energy (2 Aug 2023), on materials and fleet history:
  - SOFCs operate at **650–850 °C**.
  - Bloom patents focus on scandia-stabilised zirconia, which has a cubic-to-rhombohedral phase transition below 580 °C.
  - Interconnects are "high-grade chromium alloys", anodes are Ni-YSZ and cathodes typically LSM.
  - Of **160 historical US fuel-cell deployments** (all types, not Bloom-specific), output declined about **5% per year** on average, and retirement came after about 10–12 years.
  - Thunder Said estimates scandia loading at ~30 t/GW.

  — [Thunder Said Energy, "Bloom Energy: solid oxide fuel cell technology", 2 Aug 2023](https://thundersaidenergy.com/downloads/bloom-energy-solid-oxide-fuel-cell-technology/) [independent – research consultancy]

**Field efficiency and emissions: independent programme evaluation**
- SGIP 2018–2019 evaluation (LHV basis):
  - Electric-only fuel cells: **electrical conversion efficiency 53%** (2019), "even without any useful heat recovery", against a program minimum of 36.1% LHV (40% HHV) for electric-only fuel cells.
  - Fuel-cell CHP: 40% electrical plus 13% thermal.
  - Table ES-3 gives a capacity factor of **59%** for electric-only fuel cells in 2019. The executive-summary text says 81%. This is an unexplained internal inconsistency in the report.
  - The report confirmed at least 322 projects had been physically removed by end-2019. Many poorly performing CHP fuel cells were decommissioned before meeting permanence requirements.

  — [Verdant Associates, SGIP Impact Evaluation, 14 Jan 2021](https://www.cpuc.ca.gov/-/media/cpuc-website/divisions/energy-division/documents/self-generation-incentive-program/sgip_impact_report_2018-2019_finaldraft.pdf) [independent]
- SGIP measured non-renewable GHG impact rates:
  - electric-only fuel cells **0.36 t CO2/MWh** (2018 and 2019), against 0.25–0.26 t/MWh of displaced power-plant emissions, a net **increase** of 0.10–0.11 t/MWh
  - gas turbines 0.56; engines 0.54–0.62; microturbines 0.68–0.72

  Non-renewable electric-only fuel cells showed "the largest increase in GHG emissions across all technologies" in the program, **91–102 thousand t CO2** in 2018–2019. Against the conventional baseline they still had "the lowest emissions impact" per MWh of the non-renewable technologies. — [Verdant Associates, SGIP Impact Evaluation, Tables 5-1/5-2, 14 Jan 2021](https://www.cpuc.ca.gov/-/media/cpuc-website/divisions/energy-division/documents/self-generation-incentive-program/sgip_impact_report_2018-2019_finaldraft.pdf) [independent]

**Field efficiency and output: Bloom-specific data analysis (adversarial source)**

All findings in this block are from [Hunterbrook, D. Patel, "Do Bloom's Fuel Cells Work as Claimed? Data Says No", 30 Jul 2026](https://newsletter.hntrbrk.com/p/do-blooms-fuel-cells-work-as-claimed) [independent – **Hunterbrook Capital was short Bloom (BE) at publication**; efficiency reported on an HHV basis].

- **Datasets:** NYSERDA daily data for 37 Bloom systems (2014–2025); Delaware PSC monthly filings for the ~30 MW Delmarva fleet (156 months, 2012–2025); SGIP data for 234 projects (~92 MW); EIA-923/860 data for 126 Bloom plants (~245 MW) in nine states, identified by cross-reference; Korean utility data.
- **Contract benchmarks** (restated to HHV): guarantee line **46.9%**; replacement floor **45.2%** (from a 2025 Fresno contract); output guarantee **95% of nameplate**; stack replacement ~5 years.
- **New York:** average starting efficiency 52.0%, falling **2.4 percentage points per year**. All 37 units fell below the guarantee line at a **median of 20 months**. 28 of 37 reached the replacement floor, with a median projected time under three years.
- **Delaware:** below the guarantee line in 67 of 156 months. Output averaged about **86% of nameplate**.
- **California:** median efficiency 55.6% in the first three months, falling to **47.9% in year five**. Output was below 95% in 97.4% of project-months.
- **EIA national data:** about 51% when new and about 47% within two years. 110 of 111 reliably metered plants averaged below 95% output.
- **Korean plants:** about 51%→46% (Yeongwol, Honam) and about 58%→52% (Bukpyeong).
- **Caveats stated by Hunterbrook:**
  - A reading below a benchmark is not necessarily a contract breach.
  - The New York sample skews toward older ES-5 hardware (mostly 2017–2021).
  - Rebounds may reflect maintenance.
  - Bloom did not respond.

**Bloom's own disclosures (company data, as reported by an independent outlet)**
- Bloom's Q2 2026 10-Q, as reported by Energy News Beat:
  - Accrued warranty rose from **$20.0 M (31 Dec 2025) to $77.8 M (30 Jun 2026)**, mostly a $58.3 M specific reserve.
  - Service costs included higher performance-guarantee costs "reflecting the effects of **fleet degradation**".
  - Guarantee payments were $5.4 M in Q2 and $13.8 M in H1 2026.
  - Guarantee payments are capped at $846.1 M, with $468.9 M of exposure remaining.

  — [Energy News Beat (C. Savage), 22 Oct 2026](https://energynewsbeat.co/data-center/bloom-energy-fuel-cells-natural-gas-and-the-ai-power-rush/) [independent outlet reporting company filings]
- Bloom's ES 6.5 datasheet (Feb 2026) gives **65% to 53% electrical efficiency (LHV, "cumulative")**, as reported by Energy News Beat. Energy News Beat computes this as **679–833 lb CO2/MWh**. It compares that with:
  - the US combined-cycle fleet at EIA's 2025 tested heat rate: ≈881 lb/MWh
  - new best-in-class combined cycle at Lazard heat rates of 6,475–6,550 Btu/kWh: ≈757–766 lb/MWh
  - simple cycle: ≈1,284 lb/MWh
  - eGRID2023 US grid average: 767 lb/MWh

  The EPA factor used is 53.06 kg CO2/MMBtu. — [Energy News Beat, 22 Oct 2026](https://energynewsbeat.co/data-center/bloom-energy-fuel-cells-natural-gas-and-the-ai-power-rush/) [independent, using company spec data]; EPA factor originally from [EPA GHG Emission Factors Hub](https://www.epa.gov/climateleadership/ghg-emission-factors-hub) [independent]
- Bloom's technical primer says rising resistance over time is a key driver of efficiency degradation and of mean time to replacement (MTTR). It expects the **2018 vintage and later to have an MTTR of at least 5 years** (via search summary). Bloom's 2018 IPO prospectus said early replacement intervals were 12–18 months. — [Bloom Energy, "A primer to understanding fuel cell power module life" (undated)](https://www.bloomenergy.com/wp-content/uploads/bloom-energy-a-primer-to-understanding-fuel-cell-power-module-life.pdf) [company]

### Inferences
- Lab short-stack degradation (≈0.1–0.5%/1,000 h, i.e. ≈0.9–4.4% voltage loss per 8,760-h year) is far lower than the field efficiency decline in the Bloom datasets (≈2.4 percentage points per year from ≈52% HHV, i.e. ≈4.6% relative per year in New York). This is consistent with field factors absent from the lab: fuel processing, thermal cycling, balance of plant, operating at constant output as cells age, and older hardware generations. The cause cannot be apportioned from the sources gathered.
- CO2 comparisons:
  - At Bloom's datasheet range (65%→53% LHV), CO2 is ≈0.31–0.38 t/MWh (≈681–835 lb/MWh).
  - At Bloom's own replacement floor (45.2% HHV ≈ 50.1% LHV), CO2 is ≈0.40 t/MWh (≈883 lb/MWh). That is the same as the 2025 US combined-cycle fleet average and worse than a new H/HA-class combined cycle.
  - SGIP's measured 0.36 t/MWh sits in the middle of this range.
  - All of these are well below simple-cycle turbines (≈0.58 t) and gas engines (≈0.47 t).

  The CO2 advantage of SOFCs is therefore real against peakers and engines, but marginal against modern combined cycle, and it depends on the stack-replacement cadence.
- Whether fuel cells "reduce emissions" depends on the baseline. Against California's 2018–2019 displaced generation (0.25–0.26 t/MWh), natural-gas fuel cells **increased** emissions (SGIP). Against simple-cycle on-site generation they reduce emissions.

### Gaps
- No independent, peer-reviewed field degradation rates in %/1,000 h for *commercial* SOFC systems were found. The only field evidence is the SGIP aggregate and the adversarial Hunterbrook analysis. There is no independent replication of Hunterbrook, and Energy News Beat explicitly did not replicate it.
- Delaware PSC filings and the DOE/NETL SOFC program reports (degradation targets, field results) were not retrieved directly.
- No independent data on SOFC cold-start time, hot-standby practice, ramp rates, or ability to follow 0.2–3 Hz AI training swings. Bloom's statements on AI load-following were not checked against independent tests.
- No independent data on 100% hydrogen operation of commercial SOFC systems (efficiency, degradation).
- Detailed high-temperature degradation mechanisms (Cr poisoning from interconnects, Sr segregation, Ni coarsening/agglomeration, redox and thermal-cycling cracking, sulfur poisoning) were not retrieved from a fetched primary source. The RSC article was HTTP 403, so they cannot be cited here beyond Thunder Said's materials list.
- The SGIP report's internal inconsistency on capacity factor (59% in the table versus 81% in the text) is unresolved.

---

## 4. Power transformers and switchgear (including SF6-free designs)

### Takeaway
Conventional transformer and switchgear technology stands on solid ground. Surveyed major-failure rates are below 1% per year in CIGRE data, and about 0.3% per year in a later CIGRE working-group dataset. The constraint is supply: lead times of ~2.5–3 years, an estimated 15% US power-transformer shortage in 2026, a new US executive order banning Chinese bulk-power equipment, a single North American GOES producer for distribution transformers, and copper. The DOE 2024 distribution-transformer rule (compliance April 2029) was designed so that ~75% of the market could still use GOES, and DOE reopened it for comment in June 2026.

SF6-free switchgear is proven at medium voltage (vacuum plus air) and at ~145 kV, where hundreds of vacuum/clean-air breakers are in service. At 420 kV, the only available GIS uses fluoronitrile (C4F7N) mixtures. Those mixtures are PFAS and face both 3M's supply exit and a proposed EU PFAS restriction. Fluorine-free 420 kV equipment (clean air plus vacuum) is still in type-test and pilot phases in 2026.

### Cited Findings

**Supply, lead times and policy**
- Wood Mackenzie on US T&D supply (study with American Clean Power, 15 Oct 2025):
  - Q2 2025 average lead times: **GSUs 143 weeks**; **power transformers 128 weeks** (down 10 weeks); **switchgear 44 weeks**.
  - GSU shortage of **more than 700 units in 2025**, projected to narrow to ~140 by 2030.
  - Electrical steel prices up more than 20% "in recent months"; copper winding wire cited as a bottleneck.
  - T&D equipment demand up 35–274% from 2019 to 2025.
  - A DOE study cited found 55% of in-service distribution transformers (~40 million) were over 33 years old.
  - US data-centre pipeline above 125 GW in Q1 2025.

  — [Wood Mackenzie, "Mind the gap", 15 Oct 2025](https://www.woodmac.com/news/opinion/mind-the-gap-tackling-supply-chain-challenges-in-the-electric-td-sector/) [independent]
- Wood Mackenzie on Executive Order 14420 (31 Aug 2026):
  - The order bans imported bulk-power equipment from certain nations, especially China, which supplied "almost all bulk-power imports since the start of 2025".
  - It could affect more than $22 bn of imports since 2025 and up to 24 nations. DOE has 120 days to implement it.
  - Estimated 2026 shortages: **15% for power transformers** and **8% for substations**.
  - The >10 MVA power-transformer market has grown nearly 300% since 2020.
  - Data centres have used Chinese 100 MVA+ units to cut lead times, and are expected to bear most of the impact.

  — [Wood Mackenzie press release, 31 Aug 2026](https://www.woodmac.com/press-releases/us-executive-order-banning-chinese-bulk-power-equipment-set-to-worsen-critical-transformer-shortage/) [independent]
- Earlier Wood Mackenzie projections cited in secondary sources (30% power and 10% distribution transformer deficits in 2025) are higher than the August 2026 figure. The secondary sources conflict and were not verified (via search summary). — [EEPower](https://eepower.com/tech-insights/transformer-supply-chain-woes-persist-as-energy-demand-grows) [independent – low confidence]

**DOE distribution-transformer efficiency standard**
- DOE published its final rule on **22 Apr 2024**. Compliance is required from **23 Apr 2029**, a five-year period instead of the three years proposed in the January 2023 NOPR. DOE said the NOPR "would likely have represented about a 95% market shift to amorphous alloy", while under the final rule "about **75% of the market** will be able to achieve the standards with **GOES**" (via search summary of DOE/NRECA material). — [Federal Register 2024-07480, 22 Apr 2024](https://www.govinfo.gov/content/pkg/FR-2024-04-22/html/2024-07480.htm); [NRECA, electric.coop](https://www.electric.coop/doe-finalizes-much-improved-standard-for-distribution-transformers) [independent]
- In **June 2026**, DOE requested public comment on the 2024 standards, focused on national-security effects, domestic manufacturing capacity, supply-chain resilience and material availability. Utility Dive (29 Jul 2026) reported:
  - EEI, APPA, NRECA, NEMA and ERMCO back keeping the 2024 rule.
  - **Cleveland-Cliffs**, which describes itself as the sole North American GOES producer for distribution transformers, now supports revising it to preserve GOES use.
  - Lead times were 18+ months when the rule was finalised.

  — [Utility Dive (R. Walton), 29 Jul 2026](https://www.utilitydive.com/news/doe-mulls-changes-to-biden-era-transformer-rule-raising-utility-concerns/826440/) [independent]

**Failure statistics**
- CIGRE TB 642 (2015, WG A2.37) collected **964 major failures (1996–2010) from 58 utilities in 21 countries**. Failure rates for substation transformers, GSU transformers and the combined group were "all within 1%" per year. A follow-up WG A2.62 analysis covered more than **425,000 unit-years and 1,159 major failures**, giving about **0.3% per year**. Rates were below 1% except for the ≥700 kV class (via search summary; brochure not opened). — [CIGRE TB 642](https://e-cigre.org/publication/642-transformer-reliability-survey); [CIGRE ISH2017-598](https://www.e-cigre.org/publications/detail/ish2017-598-results-of-a-standardized-survey-about-the-reliability-of-power-transformers.html) [independent]
- Earlier CIGRE HVDC surveys found that **converter transformers in LCC systems are the single largest contributor to forced energy unavailability** (via search summary). — [CIGRE Electra 320, Feb 2022, "Converter transformer failure survey results from 2013 to 2020"](https://electra.cigre.org/320-february-2022/technical-brochures/converter-transformer-failure-survey-results-from-2013-to-2020) [independent]

**SF6 phase-out: regulation**
- SF6 has a GWP of **24,300** (IPCC AR6), according to Germany's environment agency (UBA, page updated 13 Nov 2025). The UBA also notes:
  - From **1 Jan 2035** only reclaimed or recycled SF6 may be used for servicing.
  - SF6 emissions from German electrical equipment fell from about 50 t (1998) to about 10 t (2021), while the SF6 bank in switchgear is "steadily increasing".
  - "Fluorinated alternatives fall under the PFAS definition".
  - If commissioning slips past a ban date, the operator can show no suitable alternative was available when the contract was awarded.

  — [Umweltbundesamt, "Switchgear", updated 13 Nov 2025](https://www.umweltbundesamt.de/en/topics/climate-energy/fluorinated-greenhouse-gases-fully-halogenated-cfcs/application-domains-emission-reduction/switchgear) [independent – government agency]
- SINTEF (8 Dec 2025) summarises Regulation (EU) 2024/573:
  - The first ban applies from **January 2026** to medium voltage **≤24 kV**.
  - From **January 2032** "in principle all new circuit breakers" must be SF6-free.
  - At medium voltage, fluorinated gases are banned regardless of GWP.
  - At 145 kV, C4F7N installations are allowed only if just one supplier offers a GWP<1 solution (from 1 Jan 2028), or if none does (from 1 Jan 2030).
  - At 420 kV the same two-step rule applies from **1 Jan 2032 / 1 Jan 2034**.
  - A derogation through the Ecodesign (ESPR) route is possible, but switchgear is not in the 2025–2030 ESPR work plan.

  — [SINTEF Blog (N. S. Støa-Aanensen), 8 Dec 2025](https://blog.sintef.com/energy/what-is-the-status-of-phasing-out-sf6-gas-in-switchgear-and-circuit-breakers/) [independent – research institute]
- Ban dates by voltage band in consultancy tables (via search summary): **≤24 kV from 1 Jan 2026; 24–52 kV from 1 Jan 2030; 52–145 kV (≤50 kA) from 1 Jan 2028; >145 kV (including HVDC converter stations) from 1 Jan 2032**. Article 13(13) allows an F-gas switchgear exception where a life-cycle assessment shows a lower footprint. A 2026 Council document shows member states pressing the Commission to act on that mechanism. — [Futurebridge](https://www.futurebridge.com/industry/perspectives-energy/beyond-compliance-the-strategic-shift-to-fluorine-free-switchgear/); [Council of the EU, ST-10693-2026-REV-1](https://data.consilium.europa.eu/doc/document/ST-10693-2026-REV-1/en/pdf) [independent]

**SF6-free alternatives: maturity (SINTEF, 8 Dec 2025, unless noted)**

Source for this block unless another is given: [SINTEF Blog, 8 Dec 2025](https://blog.sintef.com/energy/what-is-the-status-of-phasing-out-sf6-gas-in-switchgear-and-circuit-breakers/) [independent]

- **≤24 kV:** air or CO2/N2/O2 insulation with vacuum interruption has been "standard for decades".
- **145 kV:**
  - C4F7N–CO2 GIS (Hyundai) is available.
  - C4F7N–CO2–O2 has several installations in Europe.
  - Siemens Energy vacuum with N2/O2 has "**hundreds of breakers in Norway and Europe**". The GIS is somewhat larger than SF6 equivalents.
  - CO2/O2 outdoor breakers (Hitachi Energy, GE Vernova) are available.
  - A vacuum/N2 252 kV outdoor breaker (Pinggao) has run in China since 2024.
- **420 kV:**
  - C4F7N GIS from **Hitachi Energy is offered up to 550 kV/63 kA**. Statnett has ordered nine 420 kV GIS. A first 420 kV installation in Scotland was being commissioned.
  - CO2/O2 outdoor breakers are available.
  - **Vacuum with N2/O2 is "not yet ready"**, with first pilots (Statnett, RTE) planned from late 2026 under the EU MISSION project.
- **GWP:** C4F7N mixtures about **300–700**; vacuum with N2/O2 and CO2/O2 below 1.
- **Physics limits:** air and CO2 have lower breaking and insulation capability than SF6, so they need higher pressures. Vacuum "does not scale easily with voltage" and conducts heat poorly.
- **PFAS restriction:** the EU proposal covers C4F7N and PTFE nozzles. The latest estimate for a decision is 2028. New products would be banned 6.5 years after entry into force, sooner for breakers up to 145 kV, with a 20-year postponement for spare parts.
- **3M exit:** C4-FN is sold as 3M Novec 4710, used in GE's g3 and reportedly in Hitachi Energy's EconiQ GIS. 3M announced in **Dec 2022** that it would exit PFAS manufacturing by end-2025, and Novec 4710 is on that list. Completion of the exit was not verified from a 3M primary source (via search summary). — [3M EMSD PFAS announcement (hosted copy)](https://www.besttechnologyinc.com/wp-content/uploads/3M-Novec-PFAS-announcement-EMSD.pdf); [Wikipedia, C4-FN](https://en.wikipedia.org/wiki/C4-FN) [independent]
- **First 420 kV site tests (company claim):** on **12 June 2026** Hitachi Energy and TenneT Germany said they had completed final high-voltage site acceptance tests of "the world's first SF6-free 420 kilovolts (kV) gas-insulated switchgear (GIS)" (EconiQ GIS) at Erzhausen substation near Hanover. The release also calls it the "world's first installation of SF₆-free 420 kV GIS validated in a real substation environment". The release does **not**:
  - name the replacement insulating gas or give its GWP
  - give a current (kA) rating
  - name any independent test laboratory (the tests were run by Hitachi Energy and TenneT "according to applicable international standards")
  - give an energisation or commercial-operation date

  — [Hitachi Energy press release, 12 Jun 2026](https://www.hitachienergy.com/news-and-events/press-releases/2026/06/hitachi-energy-and-tennet-germany-complete-on-site-testing-of-worlds-first-sf6-free-420-kv-gas-insulated-switchgear) [company]
- **Fluorine-free 420 kV programmes:**
  - Siemens Energy's EU-backed LIFE Blue 420 kV clean-air plus vacuum GIS: type testing scheduled for 2026, pilot operation expected in 2027.
  - MISSION 420 kV vacuum breaker: type testing in early 2026, pilots in Norway and France in H2 2026.
  - CIGRE 2026 session papers cover F-gas-free 420 kV GIS and 420 kV/80 kA SF6-free breakers.

  All via search summary. — [Switchgear Magazine, LIFE Blue](https://switchgear-magazine.com/news/products/life-blue-project-advances-sf%E2%82%86-free-420-kv-gis-technology/); [CIGRE B3-11997 (2026)](https://www.e-cigre.org/publications/detail/b3-11997-2026-f-gas-free-420-kv-gis-based-on-clean-air-and-vacuum-switching-technology.html); [CIGRE A3-12252 (2026)](https://www.e-cigre.org/publications/detail/a3-12252-2026-420-kv-sf6-free-live-tank-circuit-breakers-and-gas-insulated-switchgear-for-80-ka-applications.html); [CORDIS project 101135484 (MISSION)](https://cordis.europa.eu/project/id/101135484/reporting) [independent]

### Inferences
- For data-centre substations above 145 kV in the EU, the only commercially available SF6-free GIS in late 2026 (C4F7N-based) carries two regulatory risks: the F-gas two-step rule (2032/2034 at 420 kV) and the proposed PFAS restriction. Fluorine-free 420 kV (clean air plus vacuum) is not expected to have operating pilots before late 2026–2027. This is a maturity gap, not a physics barrier, but vacuum's poor scaling with voltage is a real engineering constraint.
- The supply problem is structural and policy-amplified. EO 14420 removes the supply route that data-centre developers used for 100 MVA+ units. A sole domestic GOES producer and DOE's reopened rule add uncertainty. Wood Mackenzie's own estimates moved from 30% (2025) to 15% (2026), so shortage figures should be treated as model outputs.
- Low failure rates (~0.3–1%/yr) mean long lead times matter more than failure risk for project timing. They also mean a single failed large unit can take years to replace, because spares are scarce.

### Gaps
- This session could not obtain primary data on:
  - test-bay capacity
  - insulation-material (pressboard, ester fluid) constraints
  - amorphous-core manufacturing capacity (domestic producers and output)
  - copper-specific bottleneck figures
- IEEE transformer failure statistics were not retrieved. CIGRE figures come from summaries, not the brochures.
- No independent (KEMA/DNV, CESI, IPH) type-test reports were found for any SF6-free product.
- 2026 status of GE Vernova's g3 gas supply after 3M's exit: not found.
- EUR-Lex text of Regulation (EU) 2024/573 Annex IV was not opened. Dates come from SINTEF, UBA and consultancy tables, which agree with each other.
- The outcome of DOE's June 2026 comment request (any proposed amendment): not found.
- HD Hyundai Electric transformers and GIS: no independent performance or failure data found beyond SINTEF's note that Hyundai C4F7N–CO2 145 kV GIS is available.

---

## 5. HVDC and grid-forming equipment

### Takeaway
Point-to-point HVDC stands on solid ground. In CIGRE data, LCC converter stations show ~98–99% energy availability and radial VSC links ~96.5%, though these are older aggregates. Multi-terminal, multi-vendor DC grids are not yet proven at scale. DC circuit breakers are large and expensive, vendor interoperability is unresolved, and only a handful of firms can build VSC converters and HVDC cables. Grid-forming (GFM) battery inverters are, in NERC's words (Sept 2023), "commercially available and field-proven for transmission-connected applications". Field experience covers Kauai since 2018, Hornsdale since 2022 and Australian NEM projects. Islanded-system studies (Maui) suggest ~30% of online capacity needs to be grid-forming at zero inertia. No independent evidence was found on GFM performance with AI data-centre loads specifically.

### Cited Findings
- CIGRE Technical Brochure 713 figures, as summarised by KU Leuven/EnergyVille and Elia (arXiv:2512.13496v2, 23 Jul 2026):
  - LCC HVDC converter stations: **~98–99% energy availability**; forced outages of **~3–4 per year for a single pole and 0.1 per year for a bipole**.
  - Radial VSC-HVDC: **~96.5%** availability, with downtime "mainly due to forced outages".
  - Submarine cable failure rate: 0.096 per 100 km per year, with ~60 days repair.

  The same paper says:
  - "only a handful of manufacturers can currently build HVDC cables and (VSC-MMC) converters", with no new entrant expected soon
  - a DC circuit breaker occupies about **400 m²**
  - expansion of multi-terminal grids "depends on the ability of components supplied by multiple vendors to be compatible", which is the interoperability problem

  — [Bastianel et al., arXiv:2512.13496v2, 23 Jul 2026](https://arxiv.org/abs/2512.13496) [independent]
- CIGRE's annual HVDC reliability survey (2023–2024 edition presented as a 2026 paper) now reports transistor-based VSC systems alongside LCC. It gives forced-outage statistics for 2023–2024 and a cumulative average for 1989–2024. The figures themselves were not accessible. In the 2017–2018 survey, reports came from **49 LCC and 3 VSC systems (2017)** and **50 LCC and 4 VSC (2018)**. — [CIGRE B4-11765 (2026)](https://www.e-cigre.org/publications/detail/b4-11765-2026-survey-of-the-reliability-of-hvdc-systems-throughout-world-during-2023-2024.html); [CIGRE CSE N°23, 2017–2018 survey](https://cse.cigre.org/cse-n023/a-survey-of-the-reliability-of-hvdc-systems-throughout-the-world-during-2017-2018) [independent]
- NERC's grid-forming white paper (Sept 2023) concludes:
  - GFM is "commercially available and field-proven for transmission-connected applications, particularly for BESS".
  - "All newly interconnecting BPS-connected BESS should be ... commissioned with GFM controls enabled".
  - Existing BESS may be retrofitted at "relatively low incremental controller and hardware costs", subject to restudy.

  Projects listed as deployed or under construction: Kauai 13 MW (2018); Kauai PMRF 14 MW (2022); Kapolei 185 MW (2023); **Hornsdale Power Reserve 150 MW (2022)**; Wallgrove 50 MW (2022); Broken Hill 50 MW (2023); Riverina and Darlington Point 150 MW (2023); New England BESS 50 MW (2023); Dalrymple 30 MW (2018). — [NERC White Paper: Grid Forming Functional Specifications for BPS-Connected BESS, Sept 2023](https://www.nerc.com/comm/RSTC_Reliability_Guidelines/White_Paper_GFM_Functional_Specification.pdf) [independent]
- **Kauai field experience** (same NERC paper): KIUC has run a 13 MW PV+BESS in GFM mode since 2018, on a 70 MW peak system, and a second 14 MW plant fully in GFM mode since Aug 2022. Both have been stable with IBR share ranging **6–95%** and inertia **0.5–2.7 MW·s/MVA**, with no adverse interaction between the two GFM plants. — [NERC GFM white paper, Sept 2023, Appendix A](https://www.nerc.com/comm/RSTC_Reliability_Guidelines/White_Paper_GFM_Functional_Specification.pdf) [independent]
- **Maui hardware-in-the-loop tests at NREL** (same NERC paper):
  - A 2.2 MVA commercial inverter was tested in power-hardware-in-the-loop against a real-time EMT model of Maui's grid.
  - In GFL mode the system was unstable in some very-low-inertia dispatches; in GFM mode it was stable, including at zero inertia.
  - About **30% of online generation capacity** needed to be GFM for adequate damping.
  - **Hornsdale** was upgraded from GFL to GFM with an inertia service in **July 2022**.

  — [NERC GFM white paper, Sept 2023](https://www.nerc.com/comm/RSTC_Reliability_Guidelines/White_Paper_GFM_Functional_Specification.pdf) [independent]
- NERC lists synchronous condensers and "GFM STATCOM with energy storage" as transmission-side alternatives for stability in IBR-dominated areas. It notes that a large concentration of power electronics near a STATCOM or HVDC terminal raises converter-interaction risk. — [NERC GFM white paper, Sept 2023](https://www.nerc.com/comm/RSTC_Reliability_Guidelines/White_Paper_GFM_Functional_Specification.pdf); [NERC LLTF white paper, July 2025](https://www.nerc.com/globalassets/who-we-are/standing-committees/rstc/whitepaper-characteristics-and-risks-of-emerging-large-loads.pdf) [independent]
- NERC (July 2025): large loads' phase-locked-loop controls "can become unstable at low short-circuit ratios (e.g., 2 or less)". The risk is greatest where loads sit close to generation, series-compensated lines, STATCOMs or HVDC terminals, with weak coupling. — [NERC LLTF white paper, July 2025](https://www.nerc.com/globalassets/who-we-are/standing-committees/rstc/whitepaper-characteristics-and-risks-of-emerging-large-loads.pdf) [independent]

### Inferences
- For data centres, HVDC is mainly relevant as bulk transmission, which is mature for point-to-point links. Any claim of multi-terminal, multi-vendor DC grids (or a DC "backbone" campus) at GW scale goes beyond what the independent evidence shows as proven in 2026.
- GFM BESS is the best-evidenced fast-acting stabiliser in the independent record. Its field evidence is concentrated in islands and weak grids (Hawaii, South Australia, NSW) at 13–185 MW. Large, weakly coupled data-centre clusters next to on-site turbines are an untested configuration in this evidence set.
- The VSC availability figure (~96.5%) comes from a small and dated sample (3–4 VSC systems in the 2017–2018 survey). Statistically robust VSC reliability data were not available in what was retrieved.

### Gaps
- Headline numbers from CIGRE's 2023–2024 HVDC reliability survey (paywalled; abstract only).
- AEMO field reports on GFM inverters (2024–2026) could not be retrieved: the AEMO voluntary-specification URL failed and the search budget was exhausted.
- NREL GFM research (UNIFI consortium) was not retrieved (nrel.gov unreachable from this environment).
- No 2024–2026 NERC GFM guideline or standard updates were found, and the ERCOT GFM requirements for energy storage were not retrieved.
- No independent field data on GFM STATCOMs with supercapacitors (e.g. vendor "enhanced STATCOM" products) or on rotating grid stabilisers.

---

## 6. UPS, batteries, supercapacitors, 800 VDC and solid-state power distribution

### Takeaway
UPS and battery technology is mature, but grid events have shown that data-centre UPS **control logic** is a grid-reliability issue. In the July 2024 Virginia event, a scheme counting voltage disturbances (typically three dips in one minute) moved ~1,260 MW to backup and kept it there for hours. ERCOT now prohibits such count-based transfer schemes for large computational loads (NOGRR 282, effective 1 Aug 2026). Li-ion fire-safety test methods are still evolving: UL 9540A's 5th edition (2025) and 6th edition, which adds an installation-level large-scale fire test, and NFPA 855's 2026 edition. EPRI's incident statistics could not be retrieved in this session.

For load smoothing, NVIDIA's GB300 power shelf stores about **65 J per GPU** in electrolytic capacitors, and NVIDIA's own test claims a 30% cut in peak grid demand. The Microsoft/OpenAI/NVIDIA paper finds that rack-level storage has low energy overhead but high cost, and that GPU smoothing alone cannot meet tight utility specifications. 800 VDC distribution and solid-state transformers are vendor-led (NVIDIA plus partners including Schneider Electric, GE Vernova, Hitachi Energy and Siemens). This session found no independent demonstrations, standards or reliability data, so they are **not yet on independently verified ground** as of November 2026.

### Cited Findings

**UPS architectures and the role of UPS controls in grid events**
- NERC describes three UPS architectures:
  - centralized static UPS of **2–5 MW**
  - rack-level UPS of **3–4 kW**
  - diesel rotary UPS (DRUPS, flywheel), whose transfer back to the grid "typically ... must be done manually"

  A protection scheme counts voltage disturbances, typically **three within one minute**. When triggered it transfers load to backup, where it stays until manually reconnected. In the July 2024 event, **~1,260 MW** dropped at the third reclose "and did not return for hours". — [NERC Incident Review, 8 Jan 2025](https://www.nerc.com/globalassets/our-work/reports/event-reports/incident_review_large_load_loss.pdf) [independent]
- NERC (July 2025): "power delivery systems for HPC loads (AI data centers) commonly exclude UPS protection systems for the IT equipment", relying on checkpoint saving instead. "For AI training loads, there may be no UPS for the IT equipment." — [NERC LLTF white paper, July 2025](https://www.nerc.com/globalassets/who-we-are/standing-committees/rstc/whitepaper-characteristics-and-risks-of-emerging-large-loads.pdf) [independent]
- ERCOT's proposed NOGRR 282 language (Feb 2026) prohibits large electronic loads from implementing "a load trip or transfer scheme that disconnects or transfers load to backup generation due solely to a certain number of voltage sags or swells within a certain period of time". The stated intent is "to mitigate risk as seen in northern Virginia events". It also limits current during disturbances to ≤125% of maximum normal current, noting that observed events showed **150–200%**. — [ERCOT SPWG presentation (P. Gravois), 24 Feb 2026](https://www.ercot.com/files/docs/2026/03/02/04_LEL-RT-Requirements_SPWG_Feb2026.pdf) [independent]

**Li-ion fire safety standards**
- UL 9540A tests at four levels:
  - cell: thermal runaway, gas composition and flammability
  - module: propagation, heat/gas release, deflagration
  - unit: fire spread between modules, re-ignition
  - installation: fire-protection effectiveness

  The 6th edition renames the installation level the "Installation Level – Large Scale Fire Test". UL describes 9540A as "the only consensus standard explicitly cited in NFPA 855 for large-scale fire testing". The **2026 edition of NFPA 855 adds Annex G.11** on large-scale fire testing where fire could spread between BESS units. — [UL Solutions, "UL 9540A Test Method" (references UL 9540A:2025, 5th ed.; 6th ed.), accessed 14 Nov 2026](https://www.ul.com/services/ul-9540a-test-method) [independent – certification body]

**Load smoothing: capacitors, supercapacitors, GPU controls and storage**
- NVIDIA's GB300 NVL72 power shelves use **electrolytic capacitors**, about half of PSU volume, storing **65 J per GPU** (co-designed with LITEON). They are combined with:
  - a power cap that ramps gradually at job start
  - a hardware "power burner" that holds power during ramp-down
  - configurable floors and ramp-down rates

  NVIDIA reports peak grid demand **30% lower** when training Megatron. The comparison is GB200 without storage against GB300 with storage, on the same rack and workload. The storage does not export to the grid. — [NVIDIA Technical Blog, 28 Jul 2025 (updated 27 Aug 2025)](https://developer.nvidia.com/blog/how-new-gb300-nvl72-features-provide-steady-power-for-ai) [independent – vendor (NVIDIA)]
- eeNews Europe noted that electrolytic capacitors "are notoriously unreliable and can fail in high temperature environments" (via search summary; date not captured). — [eeNews Europe](https://www.eenewseurope.com/en/nvidia-details-ai-power-supply-adds-innoscience-gan) [independent – trade press]
- Joint Microsoft/OpenAI/NVIDIA paper (Aug 2025), mitigation results:
  - **Software (Firefly):** fills communication phases with secondary work, keeping overhead on the primary workload **under 5%**.
  - **GPU power smoothing on GB200:** the minimum power floor can be set up to 90% of TDP, but electrical design power is at least 1.1× TDP, so at least ~20% of TDP remains as dynamic range. A 90% floor on a production waveform cost **10.5% energy overhead** in simulation.
  - **Rack-level energy storage** is recommended as the best placement, rated "low" on energy overhead and "high" on cost. No sizing results are given.
  - In the paper's illustrative 100 MW case, a tight (10%) dynamic-range requirement cannot be met by GPU smoothing alone.

  — [Choukse et al., arXiv:2508.14318, Aug 2025](https://arxiv.org/html/2508.14318) [independent – non-seven authors]
- NVIDIA's 800 VDC white paper (13 Oct 2025) proposes multi-timescale storage:
  - **capacitors/supercapacitors** near racks for milliseconds to seconds
  - **facility BESS** at the utility interconnection for seconds to minutes, which also provides "ride-through during transfers to backup generators"

  — [NVIDIA Technical Blog, "Building the 800 VDC Ecosystem for Efficient, Scalable AI Factories", 13 Oct 2025](https://developer.nvidia.com/blog/building-the-800-vdc-ecosystem-for-efficient-scalable-ai-factories/) [independent – vendor (NVIDIA)]

**800 VDC and solid-state distribution**
- NVIDIA's claims (13 Oct 2025):
  - Traditional AC systems can have end-to-end efficiency "less than 90%".
  - The same wire gauge carries **157% more power at 800 VDC than at 415 VAC**; the basis is not stated.
  - A three-wire DC arrangement replaces four-wire AC.
  - The Kyber rack's 64:1 LLC converter uses 26% less area.
  - The transition is described in phases, with no year on this page.
  - The **Open Compute Project** is the only standards forum named. The page says the industry must align on voltage ranges, connectors and safety practices, without specifics. It does not discuss DC arc-fault protection, solid-state circuit breakers, IEC/UL standards or solid-state transformers.
  - Named data-centre power partners include **Schneider Electric, GE Vernova, Hitachi Energy**, Siemens (Siemens AG, not Siemens Energy), ABB, Eaton, Vertiv, Mitsubishi Electric and Heron Power.

  — [NVIDIA Technical Blog, 13 Oct 2025](https://developer.nvidia.com/blog/building-the-800-vdc-ecosystem-for-efficient-scalable-ai-factories/) [independent – vendor (NVIDIA); lists three of the seven as partners]

### Inferences
- 65 J/GPU × 72 GPUs ≈ 4.7 kJ per NVL72 rack. That would carry a full 72 kW step for only ≈65 ms (a third-party analysis, GPUSmith, 28 Oct 2026, reports the same order of magnitude; via search summary: [GPUSmith](https://gpusmith.com/articles/en/gpu-power-smoothing-synchronous-training-load-swings)). PSU capacitors therefore smooth only sub-cycle-to-tens-of-ms transients. Swings at 0.2–3 Hz (periods of 0.3–5 s) and checkpoint transitions need GPU-level ramp control, software, or seconds-scale storage (supercapacitors or BESS). That is consistent with NVIDIA's own multi-timescale proposal.
- The July 2024 Virginia event shows that UPS/backup transfer logic, not UPS hardware capability, drove the grid impact. The ERCOT rule bans exactly the counting scheme NERC identified. This is evidence that the risk is controllable through protection settings (NERC's April 2026 event; section 7).
- No independent efficiency, reliability or fault-protection data for 800 VDC or solid-state transformers were found. Vendor efficiency claims (e.g. "<90% AC end-to-end") are unverified, and the "157%" figure cannot be reproduced without its stated basis.

### Gaps
- UPS efficiency in practice (double-conversion versus eco-mode at partial load; ENERGY STAR UPS data; LBNL field studies): not retrieved.
- EPRI BESS Failure Incident Database statistics: the page redirected and rendered no content. Failure-rate trends and root-cause shares could not be cited.
- Data-centre lithium-ion fires were not verified in this session. These include the 26 Sept 2025 lithium-ion UPS battery fire at South Korea's National Information Resources Service, Daejeon, and the 2022 Kakao/SK C&C Pangyo fire. They are widely reported but no source was fetched.
- OCP specifications for ±400 VDC "Mt Diablo"/Diablo 400 and Open Rack v3: not retrieved.
- IEC/UL standards for 800 VDC data-centre distribution and DC protection (arc-fault detection, solid-state breakers): not found.
- Solid-state transformer demonstrations, efficiency (versus ~99% for line-frequency units) and field reliability: no independent source found.
- No independent field data on supercapacitor smoothing at facility scale.

---

## 7. AI data-centre load dynamics and how each technology copes

### Takeaway
Independent evidence that AI data-centre loads behave in grid-relevant ways is now strong and official. NERC has documented:
- a 1,500 MW customer-initiated load loss in Virginia (10 Jul 2024)
- a ~500 MW sustained loss in a similar fault (18 Apr 2026), after data centres changed protection settings
- a "nearly 4 GW" customer-initiated load reduction in Virginia (July 2026), still under analysis in September 2026

NERC escalated from a Level 2 alert (Sept 2025) to a rare **Level 3 essential-actions alert (4 May 2026)**. FERC directed NERC to complete computational-load registry criteria and foundational reliability standards by **end-2026**. ERCOT's ride-through rule for large computational loads took effect **1 Aug 2026**.

Measured AI-training dynamics are fast and repetitive:
- ramps of ~1.9 p.u./s for ~250 ms
- 450→40 MW in 36 s
- 35–70 MW within a minute at xAI Colossus
- production oscillation energy at 0.2–3 Hz, overlapping grid and shaft-torsional resonance bands

No prime mover in the evidence set is independently documented to follow these alone. The evidence supports layered mitigation: GPU-level power floors and ramp limits, software, PSU capacitors, supercapacitors or BESS, and ride-through-compliant protection settings. Demand flexibility is real but so far demonstrated at small scale: up to 40% reduction with sub-minute response on an out-of-production cluster (EPRI/National Grid/Nebius/Emerald, Dec 2025), and 25% for 3 hours in Arizona according to Emerald AI.

### Cited Findings

**Documented events (NERC)**
- **10 Jul 2024, Virginia:**
  - Event sequence:
    - A lightning arrester failed on a 230 kV line.
    - The line's auto-reclosing was set for three attempts, producing six voltage depressions of 42–66 ms at 0.25–0.40 p.u.
    - About **1,500 MW** of load was lost, "exclusively data center-type load".
    - **~1,260 MW** dropped at the third reclose and did not return for hours.
  - Grid response: frequency peaked at **60.047 Hz** and settled in about 4 minutes. Voltage rose to **1.07 p.u.**, and operators removed shunt capacitors.
  - NERC asked TOPs to include **load reconnection ramp rates** in operating agreements.
  - Published 8 Jan 2025.

  — [NERC Incident Review, 8 Jan 2025](https://www.nerc.com/globalassets/our-work/reports/event-reports/incident_review_large_load_loss.pdf) [independent]
- NERC's July 2025 white paper describes the same event as faults "within 82 seconds" with frequency peaking at **60.053 Hz**, a minor inconsistency with the incident review's 60.047 Hz. It notes that a load loss of similar size could cause much larger frequency deviations in smaller interconnections, citing ~235 mHz in ERCOT. — [NERC LLTF white paper, July 2025](https://www.nerc.com/globalassets/who-we-are/standing-committees/rstc/whitepaper-characteristics-and-risks-of-emerging-large-loads.pdf) [independent]
- **18 Apr 2026:** a fault "in the same vicinity and with similar characteristics" to July 2024 caused **only 500 MW of sustained data-centre load loss**. NERC links the improvement possibly to data centres lengthening voltage-dip counting windows and changing the count thresholds. The transmission entity now requires these settings for all new facilities.
- **July 2026, Virginia:** a "**nearly 4 GW** customer-initiated load reduction occurred in Virginia, demonstrating that the risk is increasing, not abating". Specifics were "still being analyzed as of September 2026".
- **Regulatory direction:** FERC has directed NERC to complete registry criteria and foundational standards (commissioning, communications, modelling) **by the end of 2026**. Ride-through performance standards may follow.

  All three points — [NERC Reliability Insights, "Large Computational Load Risks Due to Voltage Sensitivity", September 2026 (file created 8 Sep 2026)](https://www.nerc.com/globalassets/who-we-are/news/2026/09/reliability-insights_large-computational-load-risks-due-to-voltage-sensitivity.pdf) [independent]
- Secondary sources date the July 2026 event to **22 July 2026** in Dominion's territory, at **~3.8 GW**, with a PJM preliminary review to its Operating Committee on 6 Aug 2026 (via search summary; not verified against PJM). — [RMS Energy](https://rmsenergy.com/tdec-post/after-3-8-gw-dropped-in-virginia-nercs-computational-load-standards-move-from-draft-to-deadline/); [Battalion Energy](https://battalion.energy/blog/why-data-centers-must-ride-through-grid-faults/) [independent – low confidence]

**Alerts and regulation**
- The **Level 2 alert (Sept 2025)** cited "widespread and unexpected customer-initiated load reduction of large loads", mostly in 2024–2025, **each involving ≥1,000 MW**. NERC found that entities "generally did not have sufficient processes, procedures, or methods to address emerging computational loads". The **Level 3 alert** was issued **4 May 2026**. The NERC 2025 LTRA projects summer peak demand growth of 224 GW over 10 years. — [Utility Dive, 21 Apr 2026](https://www.utilitydive.com/news/data-center-load-disruptions-nerc-alert-recommendations/818036/) [independent]
- The Level 3 alert's seven essential actions, as summarised by Davis Wright Tremaine (1 May 2026):
  1. Model-data lists.
  2. At-least-annual stability-margin studies.
  3. A revised "qualified change" definition.
  4. A commissioning process.
  5. System-side corrective actions so normally cleared faults do not cause loss of firm load.
  6. Dynamic fault recorders.
  7. Better communication with large loads.

  Proposed Computational Load Entity registration thresholds: **≥20 MW aggregate, ≥60 kV, ≥1 MW computational load**. Registered entities had to acknowledge by 11 May 2026 and report by 3 Aug 2026 (deadlines via search summary). — [Davis Wright Tremaine, 1 May 2026](https://www.dwt.com/blogs/energy--environmental-law-blog/2026/05/nerc-level-3-alert-large-loads-data-centers) [independent – law firm]

  Morgan Lewis (13 May 2026) words the first action as requiring modelling data "including on-site generation". It says the alert "does not itself impose new mandatory obligations" and that data centres are not directly required to respond, though transmission owners may pass requests on to them. Other secondary commentary describes the actions as effectively non-optional for transmission entities, so characterisations of the alert's binding status differ. — [Morgan Lewis, 13 May 2026](https://www.morganlewis.com/blogs/datacenterbytes/2026/05/nerc-alert-signals-growing-reliability-focus-on-data-centers) [independent – law firm]
- **ERCOT NOGRR 282** "Large Computational Load Ride-Through Requirements":
  - Recommended by TAC on 29 Apr 2026 and by the Board on 2 Jun 2026; approved by the PUCT on **9 Jul 2026**; **effective 1 Aug 2026**.

  — [ERCOT NOGRR282 page](https://www.ercot.com/mktrules/issues/NOGRR282) [independent]

  The Feb 2026 proposal (the final text may differ) set the following:

  - **Scope:** applies to loads **≥75 MW** where at least 50% is computational.
  - **Voltage ride-through** (minimum time at the service delivery point):

    | Voltage (p.u.) | Minimum ride-through |
    |---|---|
    | 1.10–1.20 | 2.0 s |
    | 0.90–1.10 | continuous |
    | 0.80–0.90 | 2.0 s |
    | 0.50–0.80 | 0.5 s |
    | 0.20–0.50 | 0.25 s |
    | <0.20 | 0.15 s |

  - **Frequency ride-through:** continuous between **58.8 and 61.2 Hz**; 299 s for 57.0–58.8 Hz and 61.2–61.8 Hz.
  - **Recovery:** loads must return to ≥90% of pre-disturbance consumption within 2 s of voltage recovering above 0.9 p.u.
  - **Count-based transfer schemes:** banned.

  — [ERCOT SPWG presentation, 24 Feb 2026](https://www.ercot.com/files/docs/2026/03/02/04_LEL-RT-Requirements_SPWG_Feb2026.pdf) [independent]
- The Data Center Coalition and Google argued for limiting ride-through to computational load, exempting mechanical cooling, or to a share such as 70% of load (via search summary). — [ERCOT NOGRR 282 comments (Google, 31 Mar 2026)](https://www.ercot.com/files/docs/2026/03/31/282NOGRR-18-Google-Comments-033126.docx) [independent]

**Measured load dynamics**
- **AI training block:** a 50 MW block of a 200 MW AI training data centre, recorded at high speed, changed demand at **1.9 p.u./s for ~250 ms** at its fastest. Training/checkpoint transitions can occur "in under one second", with jittery spikes during training. NERC also notes that "the rapid ramps up and down seen in AI training/checkpoint cycles are not observed in current AI inference methods".
- **Data-centre ramp:** a North American data centre ramped from **~450 MW to ~40 MW within 36 s**.
- **xAI Colossus:** training can change load by **35–70 MW or more within a minute**.
- **Crypto-mining comparison:** a facility ramped down 298 MW in 25 s, with ~25 MW peak-to-peak oscillations.

  All four points — [NERC LLTF white paper, July 2025](https://www.nerc.com/globalassets/who-we-are/standing-committees/rstc/whitepaper-characteristics-and-risks-of-emerging-large-loads.pdf) [independent]
- **Joint Microsoft/OpenAI/NVIDIA paper:**
  - Swings can reach "tens or hundreds of megawatts" at scale.
  - Compute-to-communication power drops occur from about once per second to once every tens of seconds.
  - Production FFT energy sits at **0.2–3 Hz**.
  - An example utility limit caps harmonic energy in a **0.1–20 Hz** critical band at 20% of total.
  - Telemetry latency is 1–100 ms.

  — [arXiv:2508.14318, Aug 2025](https://arxiv.org/html/2508.14318) [independent – non-seven authors]
- Microsoft (13 Oct 2025) lists three kinds of utility requirement for AI training sites:
  - ramp-rate limits (MW per second)
  - dynamic power-range limits
  - limits on oscillation magnitude in critical frequency bands (example 0.1–20 Hz), which "vary depending on the utility and its power generation equipment"

  No numeric limits are given. The recommended approach combines rack-level storage for steady-state fluctuations with GPU-level software/hardware smoothing for ramp-up and ramp-down. Facility BESS is not discussed. The work is part of an industry collaboration "initiated by Google, Meta, and Microsoft". — [Microsoft Azure Compute Blog, "Power stabilization for AI training datacenters", 13 Oct 2025](https://techcommunity.microsoft.com/blog/azurecompute/power-stabilization-for-ai-training-datacenters/4460937) [independent – Microsoft, not one of the seven]
- **Behind-the-meter loads:** NERC says that when co-located generation trips, a behind-the-meter load either loses supply or shifts suddenly onto the grid, which "may stress the transmission system". Visibility of such configurations is limited. — [NERC LLTF white paper, July 2025](https://www.nerc.com/globalassets/who-we-are/standing-committees/rstc/whitepaper-characteristics-and-risks-of-emerging-large-loads.pdf) [independent]
- **Demand outlook:** the LBNL projection cited by NERC is up to ~12% of US electricity by 2028, from 4.4% in 2023. — [NERC LLTF white paper, July 2025](https://www.nerc.com/globalassets/who-we-are/standing-committees/rstc/whitepaper-characteristics-and-risks-of-emerging-large-loads.pdf) [independent]

  EPRI (2024) projects up to 9% by 2030. — [EPRI press release, 2 Feb 2026](https://www.prnewswire.com/news-releases/epris-dcflex-initiative-expands-to-nine-demonstration-sites-across-us-europe-302676241.html) [independent]

**Flexibility evidence (EPRI DCFlex)**
- **UK test (Dec 2025, EPRI with National Grid, Nebius and Emerald AI):**
  - The test used "a high-compute production cluster that was **taken out of active production** operation for this testing".
  - It achieved **100% compliance with more than 200 power targets and ramp-rate constraints**, with **load reductions of up to 40% and sub-minute response**. SLAs for high-priority workloads were preserved, and carbon-signal response cut emissions by more than 10%.
  - EPRI calls it a "small-scale demonstration".
- **Flex MOSAIC framework:** released **24 Mar 2026**. It defines flexibility by notification time, duration, frequency of use, depth, ramp behaviour and availability. More than 50 organisations, including NERC, MISO and SPP, have signed the open letter.
- **Aurora Project:** targets nearly **100 MW** of flexible AI load in late 2026.

  All three points — [EPRI, "DCFlex: Flex MOSAIC and Demonstration Summary" (2026)](https://restservice.epri.com/publicattachment/98143) [independent]
- **Arizona (Emerald AI claim):** a 25% reduction for three hours, which Emerald says was "published in Nature Energy". **London:** more than 200 targets and up to 40%. Both are attributed to Emerald AI, with no independent verifier named. — [Unite.AI, 2 Nov 2026](https://www.unite.ai/emerald-ai-becomes-full-member-of-epris-dcflex-initiative/) [independent outlet relaying a vendor claim]
- **Programme scope:** DCFlex has expanded to nine sites, including Ashburn–Chicago geographic load shifting, Manassas, London and Dallas (HVO backup). Demonstration partners listed include **Schneider** and Compass, Constellation, Google, NVIDIA and Oracle. — [EPRI press release, 2 Feb 2026](https://www.prnewswire.com/news-releases/epris-dcflex-initiative-expands-to-nine-demonstration-sites-across-us-europe-302676241.html); [EPRI DCFlex demonstrations page](https://dcflex.epri.com/demonstrations) [independent]

### Inferences
**What each technology faces against AI training loads.** These combine the measurements above with the technology sections.
- **Gas turbines:** ramps of ~1.9 p.u./s and 0.2–3 Hz oscillations are faster than turbine-governor and combustion response, which NERC describes as slower than power-electronic loads. Oscillations near ≥7 Hz shaft torsional modes are a known damage mechanism for turbine-generator shafts (Microsoft et al.; NERC citing Mohave). An islanded or behind-the-meter turbine plant serving training loads is therefore exposed to both frequency-control and torsional-fatigue risk unless the load is smoothed upstream.
- **Reciprocating engines:** ISO 8528-5 G3 tolerates −7% (diesel) / −15% (gas) frequency dips per BMEP-limited step, with recovery in 3 s or less. Repetitive multi-hertz swings would keep an island in near-continuous transient; gas engines are weaker than diesel.
- **SOFC:** no independent ramp or AI-following evidence was found. Thermal limits make step-following without electrical buffering unlikely to be demonstrated at scale without storage, but this is an unverified inference.
- **BESS, supercapacitors and GPU controls:** these are the only measures in the independent record (Microsoft et al.; NERC GFM paper) shown to act on millisecond-to-second timescales. Grid-forming BESS have field evidence of stable operation in low-inertia systems.
- **Fault ride-through needs to be engineered as a system.** The 2024–2026 Virginia sequence (1,500 MW, then 500 MW after setting changes, then ~4 GW) shows protection settings help but are not sufficient as clusters grow. NERC calls the common-mode risk from all loads on a circuit seeing the same disturbance "significant".
- **Flexibility claims:** the strongest independent statement (EPRI) covers a small out-of-production cluster. Scale-up evidence (~100 MW Aurora) was pending as of late 2026. Claims that flexibility can unlock "up to 100 GW" are projections.

### Gaps
- NREL studies on data-centre load dynamics and flexibility could not be retrieved (nrel.gov unreachable).
- The LBNL 2024 report was not opened directly; its figures are cited via NERC.
- The text of NERC's Level 3 alert, its accompanying reliability guideline, and the September 2025 Level 2 alert were not opened directly.
- The FERC order (docket number, date) was not found. Secondary sources say July 2026.
- PJM/NERC analysis of the July 2026 ~4 GW event (exact date, mechanism, generator responses) was still pending per NERC in Sept 2026.
- The Nature Energy paper on the Arizona demonstration (title, date, peer-review status): not retrieved.
- The final approved text of NOGRR 282, which may differ from the Feb 2026 draft tables quoted above, was not opened.
- No independent measurement was found of an islanded gas-turbine, engine or SOFC plant serving a synchronous AI-training load, including ride-through, frequency excursions and shaft-fatigue monitoring.

---

## 8. Specific company claims that independent evidence supports or contradicts

### Takeaway
Independent evidence **supports** several claims:
- Siemens Energy's Keadby 2 efficiency record (Guinness, May 2024)
- the existence of SF6-free switchgear at ≤145 kV, including Siemens Energy clean-air vacuum breakers and Hitachi Energy and GE Vernova CO2/O2 breakers
- Caterpillar's own caution that gas gensets accept load less well than diesel
- turbine OEMs' statements that castings and forgings are the binding bottleneck

Independent evidence **contradicts or qualifies** several others:
- GE's earlier "world's most efficient" titles (superseded in 2024)
- Bloom's stack-life and efficiency-guarantee framing (adversarial but data-based; Bloom's own 10-Q acknowledges "fleet degradation")
- fuel-cell emission-reduction claims when measured against a clean grid baseline
- "world's first" framing for SF6-free 420 kV GIS (possible conflict; unresolved)

The 800 VDC and AI-load-following claims tied to Schneider, GE Vernova, Hitachi Energy and Bloom are **unverified** by any independent test found.

### Cited Findings

**Supported**
- **Siemens Energy / SSE Keadby 2 efficiency record:** Guinness lists Siemens Energy as holder of the most-efficient combined-cycle record at 64.18%, verified 21 May 2024. The measurement basis is undisclosed, so the size of the margin over GE's 63.08% gross (2018) cannot be assessed on a like-for-like basis. — [Guinness World Records](https://www.guinnessworldrecords.com/world-records/431420-most-efficient-combined-cycle-power-plant) [independent]
- **Turbine bottleneck statements:** Siemens Energy's statement that large castings and forgings are the tightest constraint (via search summary of Siemens Energy remarks) [company] is **supported** by EPRI's experts (rotor forgings and hot-section blades are "the primary bottlenecks", Jan 2026). — [POWER, 15 Jan 2026](https://finance.yahoo.com/news/gas-turbine-supply-chain-bottlenecks-130656088.html) [independent]
- **GE Vernova backlog:** reported as 116 GW of gas equipment backlog plus slot reservations at end-June 2026, with reservations for 2031 deliveries (via search summary; primary GE Vernova document not opened) [company]. This is **consistent with** EPRI's statement that utilities needing capacity by 2028 face backlogs to 2030. — [POWER, 15 Jan 2026](https://finance.yahoo.com/news/gas-turbine-supply-chain-bottlenecks-130656088.html) [independent]
- **Caterpillar on gas load acceptance:** the claim that gas units typically have lower load acceptance than diesel and should run at base load while diesel follows load ([Caterpillar white paper, undated](https://www.cat.com/en_IN/by-industry/electric-power/Articles/White-papers/converting-data-centers-from-diesel-to-gas-power-generation.html) [company]) is **supported** by ISO 8528-5:2022 G3 limits (gas −15% versus diesel −7% frequency dip) and Kohler's statement that gaseous engines respond more slowly because of fuel delivery. — [Kohler white paper](https://techcomm.kohler.com/techcomm/pdf/ISO%208528-5%20and%20Generator%20Transient%20Performance_WP.pdf) [independent – vendor]
- **SF6-free at ≤145 kV:** Siemens Energy's vacuum plus N2/O2 ("clean air") HV breakers are **supported** at ≤145 kV, with "hundreds of breakers" in Norway and Europe per SINTEF (8 Dec 2025). CO2/O2 outdoor breakers from Hitachi Energy and GE Vernova are "available". HD Hyundai's C4F7N–CO2 145 kV GIS is "available". — [SINTEF, 8 Dec 2025](https://blog.sintef.com/energy/what-is-the-status-of-phasing-out-sf6-gas-in-switchgear-and-circuit-breakers/) [independent]
- **Bloom ES 6.5 datasheet efficiency range:** Bloom's Feb 2026 datasheet range of 65%→53% LHV cumulative (via ENB) [company] is **broadly consistent** with SGIP's independently measured average of ~53% LHV for electric-only fuel cells in 2019 at the low end. — [Verdant/SGIP, 14 Jan 2021](https://www.cpuc.ca.gov/-/media/cpuc-website/divisions/energy-division/documents/self-generation-incentive-program/sgip_impact_report_2018-2019_finaldraft.pdf) [independent]

**Contradicted or qualified**
- **GE "world's most efficient plant" titles:** GE claimed this for Bouchain (62.22%, 2016) and Nishi-Nagoya (63.08% gross, 2018) ([GE press release](https://www.ge.com/news/press-releases/ge-sets-guinness-world-records%E2%84%A2-title-most-efficient-power-plant) [company]). Both were true when made but were **superseded** by Keadby 2 (Siemens Energy, 64.18%, 21 May 2024). Any present-tense use of the title by GE Vernova would conflict with the current Guinness record. — [Guinness World Records](https://www.guinnessworldrecords.com/world-records/431420-most-efficient-combined-cycle-power-plant) [independent]
- **GE HA-class reliability:** GE stated in Sept 2018 that it had "identified the solution" to the 7HA/9FB stage-1 blade oxidation ([Utility Dive, 21 Sep 2018](https://www.utilitydive.com/news/trouble-in-texas-causes-shutdown-of-advanced-ge-turbine/532901/), quoting GE [company statement in independent outlet]). The fix's long-term effectiveness was **not independently verified** in this session. **Date correction:** the issue surfaced in Sept 2018, not 2019.
- **Bloom stack life:** Bloom's 2019 claim of an average newer-stack life of 4.8–5.2 years (as reported by Hunterbrook) and its primer's expected "MTTR of at least 5 years" for 2018-vintage and later units ([Bloom primer](https://www.bloomenergy.com/wp-content/uploads/bloom-energy-a-primer-to-understanding-fuel-cell-power-module-life.pdf) [company]) are **contradicted** by Hunterbrook's analysis of NYSERDA data (30 Jul 2026):
  - median time below the guarantee line: 20 months
  - 28 of 37 units reached the replacement floor, with projected median time under 3 years
  - only one unit was on pace to exceed five years

  Caveats: Hunterbrook is short Bloom, and the New York sample is older ES-5 hardware from 2017–2021. Hunterbrook also reports Bloom's 2025 impact report **removed** an earlier five-year refurbishment statement. — [Hunterbrook, 30 Jul 2026](https://newsletter.hntrbrk.com/p/do-blooms-fuel-cells-work-as-claimed) [independent – short position disclosed]
- **Bloom output guarantee:** Bloom contracts commonly guarantee output of 95% of nameplate annually (as reported by Hunterbrook) [company terms]. This is **contradicted** by multiple datasets in the same analysis:
  - Delaware averaged ~86%.
  - California projects were below 95% in 97.4% of project-months.
  - 110 of 111 EIA plants averaged below 95%.

  Bloom disclosed $18 M (2025) and $8.4 M (Q1 2026) of underperformance payments (per Hunterbrook). — [Hunterbrook, 30 Jul 2026](https://newsletter.hntrbrk.com/p/do-blooms-fuel-cells-work-as-claimed) [independent – adversarial]

  Bloom's Q2 2026 10-Q links higher guarantee costs to "fleet degradation" and shows accrued warranty rising from $20.0 M to $77.8 M. — [Energy News Beat, 22 Oct 2026](https://energynewsbeat.co/data-center/bloom-energy-fuel-cells-natural-gas-and-the-ai-power-rush/) [independent outlet reporting company filings]
- **Fuel-cell emission reductions versus the grid:** claims that natural-gas SOFCs reduce emissions versus the grid are **contradicted for California 2018–2019**. SGIP measured electric-only fuel cells at 0.36 t CO2/MWh against 0.25–0.26 t/MWh of displaced generation, the largest program-wide GHG increase of any technology at 91–102 kt/yr. — [Verdant/SGIP, 14 Jan 2021](https://www.cpuc.ca.gov/-/media/cpuc-website/divisions/energy-division/documents/self-generation-incentive-program/sgip_impact_report_2018-2019_finaldraft.pdf) [independent]

  Against the US combined-cycle fleet (≈881 lb/MWh) or simple-cycle turbines (≈1,284 lb/MWh), Bloom's datasheet range (679–833 lb/MWh) is lower. It is roughly equal to new best-in-class combined cycle (≈757–766 lb/MWh). — [Energy News Beat, 22 Oct 2026](https://energynewsbeat.co/data-center/bloom-energy-fuel-cells-natural-gas-and-the-ai-power-rush/) [independent]
- **"World's first" SF6-free 420 kV GIS:** Hitachi Energy and TenneT used this description on 12 June 2026 for the EconiQ unit at Erzhausen, qualified as "validated in a real substation environment" ([Hitachi Energy press release, 12 Jun 2026](https://www.hitachienergy.com/news-and-events/press-releases/2026/06/hitachi-energy-and-tennet-germany-complete-on-site-testing-of-worlds-first-sf6-free-420-kv-gas-insulated-switchgear) [company]). The release names no gas, no GWP and no independent test lab. SINTEF reported in Dec 2025 that a first 420 kV C4F7N GIS installation in Scotland was already being commissioned, and that Statnett had ordered nine 420 kV C4F7N GIS ([SINTEF, 8 Dec 2025](https://blog.sintef.com/energy/what-is-the-status-of-phasing-out-sf6-gas-in-switchgear-and-circuit-breakers/) [independent]). **Possible conflict, unresolved**: the "world's first" may rest on the qualifier, and the Scottish installation's vendor and energisation status were not identified. The claim rests only on the company's own site tests; no independent verification was found.

  Separately, "SF6-free" C4F7N GIS is still a fluorinated PFAS gas mixture (GWP ~300–700). It is not GWP<1 and faces the proposed EU PFAS restriction (SINTEF; [UBA, 13 Nov 2025](https://www.umweltbundesamt.de/en/topics/climate-energy/fluorinated-greenhouse-gases-fully-halogenated-cfcs/application-domains-emission-reduction/switchgear) [independent]).
- **Fluorine-free 420 kV GIS readiness:** Siemens Energy's own LIFE Blue timeline is type testing in 2026 and a pilot in 2027 ([Switchgear Magazine](https://switchgear-magazine.com/news/products/life-blue-project-advances-sf%E2%82%86-free-420-kv-gis-technology/), via search summary [independent]). SINTEF judged vacuum plus N2/O2 at 420 kV "not yet ready" (Dec 2025). Any claim of field-proven fluorine-free 420 kV equipment before 2027 would conflict with this evidence. No such specific claim was captured in this session.
- **GB300 peak-demand reduction:** NVIDIA (not one of the seven, but partnered with Schneider, GE Vernova and Hitachi Energy on 800 VDC) claims "up to 30%" lower peak grid demand ([NVIDIA, 28 Jul 2025](https://developer.nvidia.com/blog/how-new-gb300-nvl72-features-provide-steady-power-for-ai) [independent – vendor]). This is **qualified**: it comes from NVIDIA's own GB200-versus-GB300 test on one workload. The joint Microsoft/OpenAI/NVIDIA paper finds hardware smoothing alone leaves at least ~20% of TDP as dynamic range and costs ~10.5% energy at a 90% floor (simulation). — [arXiv:2508.14318](https://arxiv.org/html/2508.14318) [independent]

**Unverified (no independent test found)**
- **800 VDC partners:** Schneider Electric, GE Vernova and Hitachi Energy are named as 800 VDC ecosystem partners (NVIDIA, 13 Oct 2025). No independent demonstration, efficiency measurement, DC-protection standard or reliability record was found. — [NVIDIA, 13 Oct 2025](https://developer.nvidia.com/blog/building-the-800-vdc-ecosystem-for-efficient-scalable-ai-factories/) [independent – vendor]
- **Schneider Electric and DCFlex:** Schneider is listed as a DCFlex demonstration partner. No Schneider-specific demonstration result was published on EPRI's pages as of 14 Nov 2026. — [EPRI DCFlex demonstrations](https://dcflex.epri.com/demonstrations) [independent]

### Inferences
- The best-supported company claims are those that concede constraints (Caterpillar on gas load acceptance; Siemens Energy and GE Vernova on supply bottlenecks) or that have third-party records (Guinness).
- The most contested claims concern SOFC longevity and guarantees. The only quantitative independent evidence is a 2018–2019 programme evaluation and a 2026 short-seller-linked analysis. Bloom's own 2026 filings partially corroborate degradation costs, which narrows but does not settle the dispute.

### Gaps
- Bloom's direct response to Hunterbrook's July 2026 analysis (Bloom did not reply to Hunterbrook) and any independent replication: not found.
- **Unverified claim areas (no independent test found):**
  - the ability of Bloom's or any SOFC to follow AI-training power swings
  - GE Vernova/Siemens Energy aeroderivative fast-start or ramp claims for data-centre islands
  - hydrogen co-firing on GE Vernova or Siemens Energy units in 2024–2026

  The underlying company claim texts were not retrieved in this session, so they are listed here as untested rather than as supported or contradicted.
- Primary texts of GE Vernova, Siemens Energy, Hitachi Energy, Schneider Electric and HD Hyundai Electric technical claims were mostly not retrieved here. Other researchers are covering company disclosures, so claims were tested only where an independent counterpart surfaced.

---

## 9. What could not be found or verified

### Takeaway
Coverage is strongest for AI load dynamics (NERC primary documents, ERCOT, EPRI) and weakest for emission limits (NSPS KKKK/IIII/JJJJ), water use, independent start/ramp data, UPS efficiency, Li-ion incident statistics, 800 VDC and solid-state transformers, and SOFC operational dynamics. Several access limits applied in this session:
- **The shared web-search budget for this turn was exhausted** partway through. Further work used only direct fetches of URLs that had already surfaced, or of well-known primary pages.
- **www.nrel.gov did not resolve** in this environment and must be allowed in the session's network settings to reach NREL reports.
- **eCFR redirected to an "unblock" page.**
- EPRI's BESS failure database page, the RSC journal article (HTTP 403), peeref (HTTP 302), Caterpillar's white paper (timeout) and the LBNL 2024 report PDF (empty download) did not return content.
- After the budget ran out, the coordinator suggested switching to the Exa and Consensus search tools. They were **not** used, because the harness's exhausted-budget notice explicitly said not to work around the limit by searching through other services. Only direct fetches of already-known URLs were made afterwards.

### Cited Findings
- These items were seen **only in secondary sources** and are recorded as unverified:
  - the 22 July 2026 date and 3.8 GW size of the July 2026 Virginia event (NERC's primary document says only "July 2026" and "nearly 4 GW") — [RMS Energy](https://rmsenergy.com/tdec-post/after-3-8-gw-dropped-in-virginia-nercs-computational-load-standards-move-from-draft-to-deadline/) [independent – low confidence]
  - Wood Mackenzie's 110 GW turbine orders versus 60–70 GW/yr capacity — [Paradox Intelligence](https://www.paradoxintelligence.com/themes/gas-turbine-manufacturing-bottleneck-power-ai-demand) [independent – low confidence]
  - earlier 30%/10% transformer deficit figures — [EEPower](https://eepower.com/tech-insights/transformer-supply-chain-woes-persist-as-energy-demand-grows) [independent – low confidence]

### Inferences
- The gaps are concentrated where the evidence is either regulatory text (blocked) or vendor-dominated (800 VDC, SSTs, SOFC dynamics, aeroderivative start times). The absence of independent tests in the vendor-dominated areas is itself a finding at this date. It is not proof that the claims are false.

### Gaps
Searched for or attempted, but not found or not verifiable in this session:

**AI load dynamics and regulation**
- NERC Level 3 alert text (4 May 2026), the accompanying Reliability Guideline for computational loads, and the September 2025 Level 2 alert text.
- FERC's 2026 order directing computational-load standards (docket, date).
- PJM analysis of the July 2026 event.
- The Nature Energy paper on the Arizona DCFlex demonstration.
- Final NOGRR 282 text.
- NREL large-load and flexibility studies.
- The LBNL 2024 report, read directly.

**Gas turbines**
- Independent start-time and ramp-rate data for heavy-duty versus aeroderivative units.
- Part-load efficiency curves and ambient derating coefficients.
- NSPS KKKK and KKKKa NOx/CO limits; SCR performance and ammonia slip.
- Water consumption factors (NREL).
- GE Long Ridge hydrogen results (5%/20%); Siemens Energy HYFLEXPOWER 100% H2 results; the EPRI McDonough report.
- Post-2018 HA-class fleet reliability data; any 2025–2026 turbine fleet issues.
- Basis and measuring party for the Keadby 2 64.18% figure.
- Primary Wood Mackenzie turbine capacity data.
- Solar Turbines (Caterpillar) industrial turbine data.

**Reciprocating engines**
- Model-specific gas-engine block-load steps.
- Maintenance and availability statistics.
- Independent data on 100–500+ MW engine plants for data centres.
- EPA engine emission limits (NSPS IIII/JJJJ, NESHAP ZZZZ, Tier 4 Final) and emergency-engine hour limits.
- NFPA 110 text.
- Results of EPRI's 6 May 2026 HVO test.

**Solid-oxide fuel cells**
- Peer-reviewed field degradation rates for commercial systems.
- Delaware PSC primary filings; DOE/NETL SOFC programme results.
- Independent SOFC start-up time, ramp rate and AI load-following tests.
- 100% hydrogen operation data.
- Primary peer-reviewed text on degradation mechanisms (Cr poisoning, Ni coarsening, thermal cycling).
- The institution behind the 100,000 h stack paper (believed to be Forschungszentrum Jülich, but the snippet did not say).

**Transformers and switchgear**
- Test-bay capacity; amorphous-steel and insulation supply data.
- IEEE failure statistics; full CIGRE TB 642 tables.
- Independent type-test reports (KEMA/DNV) for SF6-free products.
- 2026 supply status of 3M Novec 4710 (C4-FN) for GE Vernova g3.
- EUR-Lex Annex IV of Regulation (EU) 2024/573.
- Outcome of DOE's June 2026 request for comment.
- Independent data on HD Hyundai Electric equipment.

**HVDC and grid-forming**
- Headline figures from CIGRE's 2023–2024 HVDC reliability survey.
- AEMO GFM performance reports (2024–2026); NREL/UNIFI GFM results.
- GFM STATCOM and supercapacitor field data.
- ERCOT GFM energy-storage requirements.

**UPS, batteries, 800 VDC and SSTs**
- UPS efficiency in practice (ENERGY STAR, LBNL).
- EPRI BESS Failure Incident Database statistics and root causes.
- The 26 Sept 2025 Daejeon (South Korea) National Information Resources Service lithium-ion UPS battery fire and other data-centre battery fires; widely reported but not fetched.
- NFPA 855 2026 edition text (beyond UL's description).
- OCP ±400 VDC (Mt Diablo/Diablo 400) specifications.
- IEC/UL DC-protection standards for 800 VDC.
- Solid-state transformer demonstrations, efficiency and reliability.
- Independent supercapacitor smoothing at facility scale.

If more searching is needed, a follow-up turn with a fresh search budget, and with nrel.gov allowed in network settings, would let the gaps above be addressed, starting with NSPS limits, NREL water and flexibility studies, EPRI BESS statistics, AEMO GFM reports and the NERC Level 3 alert text.
