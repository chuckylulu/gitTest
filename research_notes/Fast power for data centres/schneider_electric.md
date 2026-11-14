# Schneider Electric (Euronext Paris: SU) — supplier of fast power for data centres (state of affairs as of 14 November 2026)

Conventions: every bullet carries a source link, publication date and a tag — **[company]** = Schneider press releases, filings, results documents, investor materials, Schneider blogs, executive statements (including transcripts hosted by third parties); **[independent]** = customers, partners, suppliers, competitors, regulators, standards bodies, courts, papers, journalists, analysts. "(snippet)" = the fact was taken from a search-engine result summary of that URL, not from a full-page read in this session — treat with more caution. Primary documents read in full this session: FY2025 results release, FY2025 results presentation and FY2025 call transcript (all 26 Feb 2026), H1 2026 results release (30 Jul 2026), Q1 2026 revenue release (30 Apr 2026), Q3 2026 revenue release (16 Oct 2026), Q3 2026 call transcript (Investing.com), CMD 2025 release (11 Dec 2025). Note: the session's web-search budget ran out part-way through; see section 11.

## (1) Products and stage

### Takeaway
Schneider sells almost the whole in-building electrical chain for data centres — SF6-free medium-voltage (MV) switchgear (AirSeT), low-voltage (LV) switchboards, Galaxy three-phase UPS, rack PDUs and busway, prefabricated power modules and skids, and EcoStruxure/ETAP software. It also sells cooling (Motivair liquid cooling, Uniflair chillers, CDUs and fan walls). These AC products are shipping. Newer items sit at earlier stages:
- **800 VDC sidecar** (co-developed with NVIDIA): demonstration or early availability.
- **Full 800 VDC architecture**: roadmap, about 2028.
- **Software-defined MV switchgear**: live pilot at Equinix, with broader availability in 2028.
- **RM AirSeT 38 kV**: orders from 2027, deliveries from 2028.

No in-house on-site generation, large power transformers or HVDC product was found. For on-site power Schneider partners (Wärtsilä in a "Generator-to-Chip" model).

### Cited Findings
**Company positioning**
- Schneider describes its Data Center & Networks position as "#1 in electrical distribution" with the "Most complete portfolio, Including liquid cooling", and puts the data-centre market CAGR at ">10%" for 2025–30. Key trends it lists for the segment are "800V DC", "Power & Liquid cooling efficiency" and "Convergence White/Grey space". — [FY2025 results presentation, p.13, 26 Feb 2026 [company]](https://www.se.com/ww/en/assets/564/document/528239/presentation-fy-results-2025.pdf)
- The AI-factory "Build" portfolio slide lists:
  - SF6-free MV switchgear and "MV to LV for architecture flexibility";
  - the "Dynamic load tolerant GVXL" (Galaxy VXL UPS) and automatic transfer switches;
  - rPDU ("maximum rack power delivery");
  - Uniflair CDU, Uniflair Fan Wall, Turbocor chillers and liquid cooling;
  - EcoStruxure Foresight, Power Monitoring Expert, EcoStruxure Building Operations and EcoCare for Data Center services;
  - an "AI Factory digital twin" combining ETAP and NVIDIA Omniverse.
  — [FY2025 results presentation, p.17–18, 26 Feb 2026 [company]](https://www.se.com/ww/en/assets/564/document/528239/presentation-fy-results-2025.pdf)
- In Q4 2025 the release cites "strong uptake for the Group's electrical panels, UPS, racks, prefabricated solutions and liquid cooling" in data centres. — [FY2025 results release, 26 Feb 2026 [company]](https://www.se.com/ww/en/assets/564/document/528237/release-fy-results-2025.pdf)
- Q2 2026 Systems revenue rose 28% organic. "Prefabricated solutions, cooling technologies and 3-phase UPS all seeing significant growth." — [H1 2026 results release, 30 Jul 2026 [company]](https://www.se.com/ww/en/assets/pdf/release-hy-results-2026)

**MV switchgear (SF6-free)**
- SM AirSeT uses pure air and vacuum interruption instead of SF6 and keeps the footprint and mechanism of the SM6 range. Stage: shipping. — [Schneider press release on SM AirSeT (snippet; URL ID suggests Oct 2020) [company]](https://se.com/ww/en/about-us/newsroom/news/press-releases/schneider-electric-announces-sm-airset™-the-green-and-digital-switchgear-with-no-sf6-greenhouse-gas-5f7efa6d9700eb29c2576f15); [Engineering News, 7 May 2021 (snippet) [independent]](https://www.engineeringnews.co.za/article/digital-switchgear-goes-green-2021-05-07)
- Pilot projects reported at utilities: E.ON (Sweden), GreenAlp (France) and EEC Engie (New Caledonia). — [EnergyGlobal, 19 May 2023 (snippet; article appears to be vendor-sourced) [independent]](https://www.energyglobal.com/special-reports/19052023/Secure-migration-to-SF6-free-switchgear/)
- Uptake of pure-air switchgear reported as growing in East Africa. — [Engineering News, 15 Jan 2026 (snippet) [independent]](https://www.engineeringnews.co.za/print-version/pure-air-switchgear-increasingly-adopted-across-east-africa-2026-01-15)
- RM AirSeT 38 Software Defined GIS (announced at YOTTA 2026, Las Vegas):
  - 38 kV, extending the AirSeT platform from 24 kV to 36/38 kV campus distribution;
  - pressurised pure air plus vacuum interruption; no SF6 or other F-gases;
  - stage: **roadmap**, with order intake in 2027 and first deliveries in 2028.
  — [StorageReview, 2 Oct 2026 [independent, reporting company launch]](https://www.storagereview.com/news/schneider-electric-software-defined-medium-voltage-switchgear-yotta-2026-equinix-pilot)
- "Software-defined" MV switchgear:
  - control logic is separated from hardware; protection, telemetry and upgrades are deployed as software modules over the air;
  - first live deployment is a colocation pilot with Equinix; pilots run through 2027, with "broader availability" in 2028;
  - stage: **pilot**.
  — [StorageReview, 2 Oct 2026 [independent]](https://www.storagereview.com/news/schneider-electric-software-defined-medium-voltage-switchgear-yotta-2026-equinix-pilot); [Engineering News reprint of release, 1 Oct 2026 (snippet) [company]](https://engineeringnews.co.za/print-version/schneider-electric-unveils-the-worlds-first-fully-software-defined-medium-voltage-switchgear-to-accelerate-the-speed-and-scalability-of-ai-factories-2026-10-01)

**LV switchgear and switchboards**
- The Digital Realty supply-capacity agreement covers UPS, low-voltage switchgear (LVS) and prefabricated power skids, and "adds a dedicated LVS production line". Stage: shipping. — [TechInformed, 20 Nov 2025 [independent]](https://techinformed.com/schneider-electric-signs-2-27-billion-u-s-data-center-supply-deals-with-switch-and-digital-realty/); [Data Center Frontier, 24 Nov 2025 [independent]](https://www.datacenterfrontier.com/machine-learning/article/55332455/schneider-electrics-23-billion-worth-of-ai-power-and-cooling-deals-sends-message-to-data-center-sector)

**UPS (Galaxy family)**
- Galaxy VXL specifications (stage: shipping):
  - 500–1,250 kW, 400 V, three-phase; up to 1.25 MW from one frame, scaling to 5 MW in parallel;
  - 1,042 kW/m²;
  - efficiency "up to 99%" and "up to 97.5%" (operating modes not attributed in the article);
  - lithium-ion and VRLA compatible; "Live Swap"; meets IEC 62443-4-2; EcoStruxure IT monitoring;
  - planned output of 9,000 units a year by 2025.
  — [ITdaily, 5 Dec 2024 [independent, reporting company launch]](https://itdaily.com/news/datacenter/schneider-electric-galaxy-vxl-ups)
- Asia-Pacific launch release, 7 Apr 2025 (snippet): 125 kW power modules; "52% space savings" against the industry average (company claim); built at Sant Boi, Barcelona. — [Malay Mail / Media OutReach release (snippet) [company]](https://www.malaymail.com/news/money/mediaoutreach/2025/04/07/schneider-electric-announces-galaxy-vxl-ups-the-industrys-most-compact-high-density-power-protection-system-for-ai-data-center-and-large-scale-electrical-workloads/373424)
- Galaxy VXL "Global platform adaptation to the Chinese market". — [FY2025 results presentation, p.22, 26 Feb 2026 [company]](https://www.se.com/ww/en/assets/564/document/528239/presentation-fy-results-2025.pdf)

**Prefabricated power**
- Prefabricated Power Modules and Power Skids (announced 16 Sep 2026):
  - 2 MW, 2.25 MW and 2.5 MW ratings, the 2.5 MW unit being the largest single-container version;
  - contents: Galaxy VXL UPS, switchgear, cooling, lithium-ion battery, busway and power distribution;
  - follow NVIDIA reference designs and are sized for GB300 NVL72;
  - built at Sant Boi de Llobregat (5,000 m² of dedicated production space);
  - available immediately in Europe, North America "later this year" (2026).
  Stage: shipping in Europe, launching in North America. — [MGRID, 21 Sep 2026 [independent]](https://mgrid.org/2026/09/21/schneider-electric-launches-a-2-5-mw-prefabricated-power-block-with-north-america-waiting-until-later-this-year/)
- In Q4 2025, Data Center systems growth was led by the prefabricated offer: "sales of the Group's prefabricated offer were particularly strong". — [FY2025 results release, 26 Feb 2026 [company]](https://www.se.com/ww/en/assets/564/document/528237/release-fy-results-2025.pdf)

**Busway and PDUs**
- Busway is integrated in the 2.5 MW prefab modules. — [MGRID, 21 Sep 2026 [independent]](https://mgrid.org/2026/09/21/schneider-electric-launches-a-2-5-mw-prefabricated-power-block-with-north-america-waiting-until-later-this-year/)
- Market context (not Schneider-specific): in 1Q 2025 power distribution was the fastest-growing data centre physical infrastructure segment, with busway "up over 40%" year on year. — [Lightwave, reporting Dell'Oro, 8 Jul 2025 [independent]](https://www.lightwaveonline.com/home/article/55301804/schneider-electric-and-vertiv-dominate-the-data-center-physical-infrastructure-market)

**Cooling (Motivair, Uniflair)**
- Motivair products: coolant distribution units, rear-door heat exchangers, cold plates, heat dissipation units and chillers. It is based in Buffalo, NY, has 150+ employees, and was run after the acquisition by CEO Rich Whitmore. — [Facilities Dive, 21 Oct 2024 [independent]](https://www.facilitiesdive.com/news/schneider-electric-to-buy-controlling-stake-in-motivair/730423/)
- Uniflair chillers use oil-free, variable-speed centrifugal compressors with integrated free cooling. Their first North American deployment is with Switch, under a three-year full-service contract. — [Switch-hosted release, 19 Nov 2025 [independent – customer]](https://www.switch.com/schneider-electric-and-switch-expand-partnership-with-1-9-billion-supply-capacity-agreement-to-power-ai-factories/)

**800 VDC**
- NVIDIA lists Schneider Electric with Eaton and Vertiv as "data center power systems" partners for its 800 VDC architecture. — [NVIDIA Technical Blog, 20 May 2025 (updated 31 Jul 2025) [independent – partner]](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/)
- Schneider is "Co-developing 800V DC sidecar with NVIDIA to deliver up to 1.2 MW per rack". — [FY2025 results presentation, p.18, 26 Feb 2026 [company]](https://www.se.com/ww/en/assets/564/document/528239/presentation-fy-results-2025.pdf)
- A 24 Oct 2025 release describes the sidecar converting incoming AC to 800 VDC for racks up to 1.2 MW. — [ARC Advisory summary (snippet) [independent]](https://www.arcweb.com/blog/schneider-electric-advances-800-vdc-power-systems-support-nvidias-next-generation-gpus); [Business Wire release, 24 Oct 2025 (snippet) [company]](https://www.businesswire.com/news/home/20251024311492/en/Schneider-Electric-Highlights-Innovation-in-800-VDC-Power-Systems-in-Support-of-NVIDIA%E2%80%99s-Next-Generation-GPUs)
- At the OCP Global Summit (Oct 2026), Schneider Electric, ABB, Siemens and Eaton "brought their own 800 Vdc protection and power hardware to NVIDIA's MGX wall". No Schneider-specific sidecar specification is given. Stage: demonstration hardware. — [Dell'Oro Group (Alex Cordovil), 19 Oct 2026 [independent]](https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/)

**Software and digital twins**
- Schneider, AVEVA, Nscale and Start Campus completed a pilot digital twin for Nscale's AI data-centre operations at the SINES campus in Portugal. Stage: technology pilot, not a supply contract. — [HPCwire, carrying a 27 Oct 2026 GlobeNewswire release (snippet) [company]](https://www.hpcwire.com/off-the-wire/schneider-electric-and-partners-pilot-digital-twin-for-nscales-ai-infrastructure/)

**Storage, microgrids and on-site power**
- Schneider eStar is a joint venture with StarCharge for "EV charging and storage solutions for Europe". — [FY2025 results presentation, p.22, 26 Feb 2026 [company]](https://www.se.com/ww/en/assets/564/document/528239/presentation-fy-results-2025.pdf)
- Lithium-ion batteries are integrated in the prefab power modules. — [MGRID, 21 Sep 2026 [independent]](https://mgrid.org/2026/09/21/schneider-electric-launches-a-2-5-mw-prefabricated-power-block-with-north-america-waiting-until-later-this-year/)
- On-site generation: Schneider presented a "Generator-to-Chip" delivery model with partners Wärtsilä Energy and Stanley Consultants (partners, not customers). Wärtsilä's Risto Paldanius: "For many data center projects, power has become the schedule." The release gives no supporting figures, customers or dates. — [StorageReview, 2 Oct 2026 [independent]](https://www.storagereview.com/news/schneider-electric-software-defined-medium-voltage-switchgear-yotta-2026-equinix-pilot)

### Inferences
- **Stage summary as of 14 Nov 2026:**
  - Shipping: SM AirSeT and RM AirSeT ≤24 kV, LV switchboards, Galaxy VXL and other Galaxy 3-phase UPS, rPDU, busway, prefab modules and skids (Europe; North America launching), Motivair and Uniflair cooling, EcoStruxure and ETAP software.
  - Demonstration or early availability: 800 VDC sidecar.
  - Pilot: software-defined MV switchgear (Equinix).
  - Roadmap: RM AirSeT 38 kV (2027–28), full 800 VDC architecture (~2028), solid-state transformer (no product found).
- Schneider's exposure to fast power for data centres is concentrated in the facility (MV/LV distribution, UPS, prefab) rather than in generation or grid connection. No Schneider HVDC, large power transformer or gas-turbine/fuel-cell product turned up. Relative to the other six companies in the study it therefore overlaps most with Hitachi Energy and Siemens Energy at MV/switchgear, and with GE Vernova, Caterpillar and Bloom only as a potential integration partner for on-site power. This is an inference from absence of evidence, not a sourced statement.

### Gaps
- No 2025–2026 information found on the AlphaStruxure microgrid JV (with Carlyle) or on a named Schneider BESS or microgrid product for data centres.
- Busway and PDU product names (e.g., Canalis, I-Line, APC NetShelter) and their stage were not verified.
- The specific NVIDIA reference designs (GB200/GB300 NVL72, Mission Control) were seen only in secondary snippets.
- Which Galaxy VXL efficiency figure belongs to which mode (eConversion/eco-mode vs double conversion) was not stated in the source read.

## (2) Technology and roadmap with dates

### Takeaway
NVIDIA ties full-scale 800 VDC production to Kyber/Rubin Ultra in 2027. Schneider's plan has two steps:
- a sidecar that it says is available now, or before Kyber;
- a full 800 VDC architecture that its CEO says "could be ready by '28", with market impact "step by step between probably '28 and 2030" and 15–25% of demand affected by 2030.

Other dated roadmap items:
- 2.5 MW prefab blocks: Europe from Sep 2026, North America later in 2026.
- Software-defined MV switchgear: broader availability in 2028.
- RM AirSeT 38 kV: orders from 2027, deliveries from 2028.
- Capacity: the $700m+ US programme runs through 2027, with liquid-cooling capacity being added in North America, India, Italy and China.

### Cited Findings
**NVIDIA's schedule**
- "Full-scale" 800 VDC data-centre production will "coincide with" NVIDIA Kyber rack-scale systems in 2027, supporting 1 MW IT racks and beyond.
- At GTC 2025 NVIDIA showed an 800 V sidecar powering 576 Rubin Ultra GPUs in one Kyber rack.
- NVIDIA and partners are "actively studying the CapEx and, OpEx, and safety implications" of transformer-based versus solid-state-transformer (SST) approaches.
— [NVIDIA Technical Blog, 20 May 2025 [independent – partner]](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/)

**Schneider's 800 VDC statements**
- Schneider blog (16 Oct 2025): Rubin Ultra in Kyber will ship from 2027 and Schneider's sidecar will reach the market before then. — [Schneider blog (snippet; page returned 403) [company]](https://blog.se.com/datacenter/2025/10/16/the-1-mw-ai-it-rack-is-coming-and-it-needs-800-vdc-power/)
- A Schneider executive op-ed says technical specifications and a reference design would be shared ahead of deployment. — [DCD opinion, Nov 2025 (snippet) [company]](https://www.datacenterdynamics.com/en/opinions/the-1mw-ai-it-rack-is-coming-and-it-needs-800vdc-power/)
- CEO Olivier Blum, FY2025 call (26 Feb 2026) — [FY2025 call transcript [company]](https://www.se.com/ww/en/assets/564/document/528236/transcript-Q4-results-2025.pdf):
  - "we are developing one, what we call, as you know, the sidecar concept, which can be available immediately, which is a minor evolution of the infrastructure. But we are developing those full definitely architecture that could be ready by '28 when the market will start to grow."
  - "all reports in the market estimate 15%, 25% of the demand could be impacted by 2030"
  - "will impact our market step by step between probably '28 and 2030"
  - Schneider is "leveraging here a lot of competency we have in-house in particular in China, but also we're working with partners."
- The analyst question on that call asked specifically about "solid-state transformer and solid-state braking". The CEO's answer named no SST or solid-state breaker product or date. — [FY2025 call transcript, 26 Feb 2026 [company]](https://www.se.com/ww/en/assets/564/document/528236/transcript-Q4-results-2025.pdf)
- CFO Nathan Fast, Q3 2026 call (16 Oct 2026): "So far we have not had a question on 800 volt or the technology moves." He said Schneider's design-partner role gives it visibility into such shifts. — [Investing.com transcript [company statements]](https://www.investing.com/news/transcripts/earnings-call-transcript-schneider-electric-posts-record-q3-2026-revenue-93CH-4953279)

**Independent view of 800 VDC maturity (Dell'Oro, 19 Oct 2026)** — [Dell'Oro [independent]](https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/)
- The sidecar "is here", but upstream 800 Vdc architecture remains "an object of engineering ambition and speculation" and the full chain "still needs work".
- On SSTs: "volumes remain modest, field reliability is unproven at scale", and protection and grounding practices are still being written.
- OCP's draft SST specification targets units up to 10 MW with at least 98% efficiency from half to full load.

**Other product dates**
- Galaxy VXL: launch coverage dated 5 Dec 2024 ([ITdaily [independent]](https://itdaily.com/news/datacenter/schneider-electric-galaxy-vxl-ups)), 17 Feb 2025 ([IPP Media (snippet) [independent]](https://ippmedia.com/the-guardian/business/read/schneider-electric-launches-high-effiency-ups-for-ai-data-centres-2025-02-17-151212)) and 7 Apr 2025 ([Malay Mail release (snippet) [company]](https://www.malaymail.com/news/money/mediaoutreach/2025/04/07/schneider-electric-announces-galaxy-vxl-ups-the-industrys-most-compact-high-density-power-protection-system-for-ai-data-center-and-large-scale-electrical-workloads/373424)). This looks like a staggered regional roll-out.
- Prefab Power Modules and Skids: announced 16 Sep 2026; Europe immediately, North America later in 2026. — [MGRID, 21 Sep 2026 [independent]](https://mgrid.org/2026/09/21/schneider-electric-launches-a-2-5-mw-prefabricated-power-block-with-north-america-waiting-until-later-this-year/)
- Software-defined MV switchgear: pilots through 2027, broader availability in 2028. RM AirSeT 38: orders from 2027, deliveries from 2028. — [StorageReview, 2 Oct 2026 [independent]](https://www.storagereview.com/news/schneider-electric-software-defined-medium-voltage-switchgear-yotta-2026-equinix-pilot)

**Capacity roadmap**
- US: more than $700m of investment through 2027, announced March 2025, described as the largest single capital commitment in Schneider's 135+ year history. It covers:
  - a new MV facility in Mt. Juliet, Tennessee;
  - an expanded El Paso, Texas campus for switchgear and power distribution;
  - a Houston innovation centre;
  - eight sites across Texas, Tennessee, Ohio, North Carolina, Massachusetts and Missouri, with more than 1,000 jobs.
  Together with $440m committed since 2020, US investment passes $1bn this decade. — [Manufacturing Dive, Mar 2025 (snippet) [independent]](https://www.manufacturingdive.com/news/schneider-electric-700-million-investment-us-data-center-demand-ai/743630/); [The Register, 26 Mar 2025 (snippet) [independent]](https://www.theregister.com/2025/03/26/schneider_electric_ai_investment/)
- Regional hub investments shown in Feb 2026 — [FY2025 results presentation, p.22, 26 Feb 2026 [company]](https://www.se.com/ww/en/assets/564/document/528239/presentation-fy-results-2025.pdf):
  - "New factory in Macon (France), €100m investment";
  - "Mt Juliet (US) new manufacturing facility" and a campus expansion "producing custom power distribution equipment";
  - "New plant opening in Bengaluru" (India);
  - a liquid-cooling "Center of competency with Motivair";
  - Galaxy VXL adapted for China.
- CEO (Feb 2026): Schneider "decided to open a new factory in India" for Motivair liquid cooling and works "strongly with companies like Samsung and Foxconn" for flexible capacity, with Infineon as a supplier partner. — [FY2025 call transcript, 26 Feb 2026 [company]](https://www.se.com/ww/en/assets/564/document/528236/transcript-Q4-results-2025.pdf)
- CFO (Oct 2026): "we continue to make capacity investments across our regional hubs", including liquid cooling in North America, India, Italy and China. Prefab capacity is being added "both internally and externally", including with Foxconn. — [Investing.com Q3 2026 transcript, 16 Oct 2026 [company statements]](https://www.investing.com/news/transcripts/earnings-call-transcript-schneider-electric-posts-record-q3-2026-revenue-93CH-4953279)

### Inferences
- Schneider's "full architecture ready by ~2028" is about one year behind NVIDIA's "full-scale 800 VDC production" with Kyber in 2027. Until then Schneider is relying on the sidecar (AC in, 800 VDC out at row level) to bridge Kyber-generation deployments. This is consistent with Dell'Oro's view that the sidecar is real but facility-level DC distribution is not.
- The CEO's "15–25% of demand impacted by 2030" means Schneider expects the AC portfolio (AC switchgear, AC UPS) to remain the bulk of data-centre demand through 2030.

### Gaps
- No Schneider product name, rating or date was found for a solid-state transformer, a solid-state DC breaker or a facility-level 800 VDC UPS/BESS.
- No new Galaxy UPS line after Galaxy VXL (2024–25) was identified for 2026.
- No dated plant-opening announcement for 2026 was verified (Mt. Juliet, El Paso, Macon, Bengaluru liquid cooling, Mexico).
- Nothing was found on Schneider plants in Mexico for data-centre equipment. Mexico appears in the results only as a weak sales market.

## (3) Milestones met or missed

### Takeaway
Financial promises have been met or beaten since the 2023 CMD:
- FY2025 organic growth was +8.9%, inside the 7–10% target band.
- The FY2026 target has been raised twice (Jul and Oct 2026). Organic revenue growth is running at +15.0% for 9M 2026 against an initial +7–10%.

Margin progress was at the bottom of the range in FY2025 (+50bps organic). Operational milestones are partly verified:
- Motivair consolidated; the SEIPL buyout closed in Dec 2025.
- The 800 VDC sidecar has been shown at OCP.
- Deliveries under the Switch and Digital Realty deals, plant openings and the 9,000-unit Galaxy VXL output were not independently confirmed.

Herweck was removed in Nov 2024 for "divergences in the execution of the company roadmap".

### Cited Findings
**Mid-term targets**
- Promise (2023 CMD, 9 Nov 2023): organic revenue growth +7% to +10% CAGR 2023–2027, plus organic adjusted EBITA margin expansion of "around +50 basis points". — [Schneider CMD 2023 release via Webdisclosure (snippet) [company]](https://webdisclosure.com/press-release/schneider-electric-epa-su-schneider-electric-hosts-a-capital-markets-day-for-investors-and-financial-analysts-Y3eOo6edoer). Utility Dive described it as cumulative organic annual growth of 7–10% from 2023 through 2027 and long-term growth "north of 5% on average across the economic cycle". — [Utility Dive, 6 Nov 2024 [independent]](https://www.utilitydive.com/news/schneider-electric-replaces-ceo-peter-herweck-amid-strategic-execution-issue/732175/)
- Outcome: FY2025 revenue +8.9% organic, adjusted EBITA +12.3% organic, margin +50bps organic to 18.7%. — [FY2025 results release, 26 Feb 2026 [company]](https://www.se.com/ww/en/assets/564/document/528237/release-fy-results-2025.pdf). FY2024 organic growth was "+8% organic to €38 billion" per the company's FY2024 presentation, and 8.4% per a call-transcript summary. — [Schneider FY2024 results presentation (snippet) [company]](https://se.com/ww/en/assets/564/document/505718/presentation-fy-results-2024.pdf); [roic.ai FY2024 call transcript (snippet) [company statements]](https://www.roic.ai/quote/SBGSY/transcripts/2024-year/4-quarter)
- Reset (CMD, 11 Dec 2025, McLaren Technology Center, Woking, UK) — [CMD 2025 release, 11 Dec 2025 [company]](https://cdn.financialreports.eu/financialreports/media/filings/1651/2025/ISS/1651_iss_2025-12-11_bb1b122f-b857-4156-b220-f276a77441b4.pdf):
  - organic revenue growth target of +7–10% CAGR "extended through 2030" (2025–2030);
  - +250bps cumulative organic adjusted EBITA margin expansion 2026–2030;
  - cash conversion around 100%; ROCE ambition 15–20%;
  - share buyback of €2.5–3.5bn through 2030 and disposals of €1.0–1.5bn of revenue by 2030.

**FY2026 target (three versions)** — [FY2025 release [company]](https://www.se.com/ww/en/assets/564/document/528237/release-fy-results-2025.pdf); [H1 2026 release [company]](https://www.se.com/ww/en/assets/pdf/release-hy-results-2026); [Q3 2026 revenue release [company]](https://www.finanzwire.com/press-release/schneider-electric-epa-su-third-quarter-revenues-2026-odiihfxJLgs)

| Date | Adj. EBITA organic growth | Organic revenue growth | Organic margin change | Implied margin |
|---|---|---|---|---|
| Set 26 Feb 2026 | +10% to +15% | +7% to +10% | +50 to +80bps | c.19.1–19.4% |
| Raised 30 Jul 2026 | +14% to +19% | +10% to +13% | +70 to +100bps | c.19.4–19.7% |
| Raised 16 Oct 2026 | +18% to +21% | +12% to +14% | +100 to +120bps | c.19.7–19.9% |

- Delivery so far: Q1 2026 +11.2% organic, H1 +14.0%, 9M +15.0%, and H1 adjusted EBITA margin 19.3% (+120bps organic).

**Buyback**
- Promise: a €600m tranche executed by Natixis from 9 Mar 2026, to be completed by November 2026.
- Outcome: by 12 Oct 2026, 1.8m shares bought for €497m at an average of €269; "on track" for end-November.
- The overall €2.5–3.5bn programme runs to 2030, with a pause expected in 2027 and 2028 (paraphrase of the release, not a verbatim quote).
— [Q1 2026 release, 30 Apr 2026 [company]](https://finanzwire.com/press-release/schneider-electric-epa-su-first-quarter-revenues-2026-hD4UmP80CSR); [Q3 2026 release, 16 Oct 2026 [company]](https://www.finanzwire.com/press-release/schneider-electric-epa-su-third-quarter-revenues-2026-odiihfxJLgs)

**CEO change (Nov 2024)** — [Utility Dive, 6 Nov 2024 [independent]](https://www.utilitydive.com/news/schneider-electric-replaces-ceo-peter-herweck-amid-strategic-execution-issue/732175/); [Bloomberg, 4 Nov 2024 (snippet) [independent]](https://www.bloomberg.com/news/articles/2024-11-04/schneider-electric-names-olivier-blum-as-ceo-replacing-herweck)
- On Monday 4 Nov 2024, effective immediately, the board replaced CEO Peter Herweck (CEO since May 2023) with Olivier Blum. The release cited "divergences in the execution of the company roadmap at a time of significant opportunities".
- CFO Hilary Maxson and IR head Amit Bhalla said the board "felt the strategy was not being as decisively or collaboratively implemented as hoped and that the CEO's style was not a fit".
- Analysts: J.P. Morgan called it a "major surprise" and Blum "the continuity candidate for a strategy that remains unchanged". Jefferies cited "a disagreement as to the style of management particularly around collaboration". J.P. Morgan noted M&A disagreements "were not cited as a factor".

**Motivair**
- Promise (Oct 2024): a 75% stake for $850m cash (mid-single-digit multiple of projected FY2025 revenue), with the remaining 25% expected to be bought in 2028. — [Facilities Dive, 21 Oct 2024 [independent]](https://www.facilitiesdive.com/news/schneider-electric-to-buy-controlling-stake-in-motivair/730423/)
- Outcome: Motivair is in the consolidation scope from Q1 2025 (one month in Q1 2025, then 3m, 3m, 3m and 2m in Q1 2026) and "Effective from Q2'26, Motivair now forms part of the organic performance". — [FY2025 release, scope appendix [company]](https://www.se.com/ww/en/assets/564/document/528237/release-fy-results-2025.pdf); [H1 2026 release [company]](https://www.se.com/ww/en/assets/pdf/release-hy-results-2026)
- Expansion: a new Motivair factory in India was decided in 2025 (CEO, Feb 2026), and liquid-cooling capacity is now in North America, India, Italy and China (CFO, Oct 2026). — [FY2025 call transcript [company]](https://www.se.com/ww/en/assets/564/document/528236/transcript-Q4-results-2025.pdf); [Investing.com Q3 transcript [company]](https://www.investing.com/news/transcripts/earnings-call-transcript-schneider-electric-posts-record-q3-2026-revenue-93CH-4953279)

**Temasek's 35% of Schneider Electric India (SEIPL)**
- Outcome: completed and announced 18 Dec 2025, giving 100% ownership. Net debt rose by €5.5bn "relating to the purchase of the remaining minority interests in SEIPL".
- Financing: a €750m 2.750% bond due July 2030 issued 3 Dec 2025, and about €150m of incremental 2026 finance costs.
— [FY2025 results release, 26 Feb 2026 [company]](https://www.se.com/ww/en/assets/564/document/528237/release-fy-results-2025.pdf)

**800 VDC sidecar**
- Promise (Oct 2025): "to market" before Kyber in 2027. — [Schneider blog (snippet) [company]](https://blog.se.com/datacenter/2025/10/16/the-1-mw-ai-it-rack-is-coming-and-it-needs-800-vdc-power/)
- Status (Oct 2026): Schneider 800 Vdc hardware was shown at OCP 2026; no named customer deployment was found. — [Dell'Oro, 19 Oct 2026 [independent]](https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/)

**CFO succession**
- Hilary Maxson left on 5 Apr 2026; Nathan Fast (Head of IR, with Schneider since 2007) became CFO on 6 Apr 2026. — [FY2025 results release, 26 Feb 2026 [company]](https://www.se.com/ww/en/assets/564/document/528237/release-fy-results-2025.pdf)

### Inferences
- The first-year FY2026 guidance (+100–120bps organic margin) would deliver about 40–48% of the cumulative +250bps 2026–2030 CMD margin target in year one.
- The buyback pause expected in 2027–2028 coincides with the expected Q3 2027 closing of the $23.7bn-EV PTC deal (section 4). The release does not state the link explicitly.
- The FY2025 margin of +50bps organic was at the low end of the original FY2025 ambition range and was held back by mix (Systems), tariffs and raw materials (section 4). Treat that as "met at the low end".

### Gaps
- The original FY2025 guidance (set Feb 2025) and FY2024 guidance compliance were not retrieved, beyond a snippet saying FY2024 guidance was +6–8% organic revenue, +8–12% adjusted EBITA and +40–60bps.
- The exact 2023 CMD margin wording (per year or cumulative) was not verified in the primary document.
- No confirmation was found of actual Galaxy VXL output against the 9,000 units/year plan, of Switch and Digital Realty delivery milestones, or of the Temasek deal's original announcement date and price (only the €5.5bn cash outflow is sourced).

## (4) Financials

### Takeaway
Group revenue rose from €38.2bn (FY2024) to €40.2bn (FY2025, +8.9% organic). It is accelerating in 2026: Q3 2026 €11.46bn, +16.9% organic, a record; 9M +15.0%. Energy Management, the business containing data centres, is driving growth (Q3 +18.8% organic, adjusted EBITA margin 22.4% in H1 2026), while Industrial Automation lags (+8.1% in Q3, 14.0% margin).

Data Center & Networks was 30% of FY2025 orders; the CFO says direct data-centre exposure is about 4 points lower. Data-centre demand has grown triple digits in three of the last four quarters, with sales up "strong double digits".

Net debt rose to €15.4bn (Jun 2026) after the SEIPL buyout, and before the pending $23.7bn-EV PTC, $3.1bn Cognite, $350m-EV AiDASH and €1.2bn Shelly deals.

### Cited Findings
**Group key figures (€m)** — [FY2025 release, 26 Feb 2026 [company]](https://www.se.com/ww/en/assets/564/document/528237/release-fy-results-2025.pdf); [H1 2026 release, 30 Jul 2026 [company]](https://www.se.com/ww/en/assets/pdf/release-hy-results-2026); [Q1 2026 release, 30 Apr 2026 [company]](https://finanzwire.com/press-release/schneider-electric-epa-su-first-quarter-revenues-2026-hD4UmP80CSR); [Q3 2026 release, 16 Oct 2026 [company]](https://www.finanzwire.com/press-release/schneider-electric-epa-su-third-quarter-revenues-2026-odiihfxJLgs)

| Item | FY2024 | FY2025 | H1 2026 | Q3 2026 / 9M 2026 |
|---|---|---|---|---|
| Revenue | 38,153 | 40,152 (+5.2% reported, +8.9% organic) | 21,226 (+9.8% reported, +14.0% organic) | Q3 11,460 (+17.9% reported, +16.9% organic); 9M 32,686 (+12.5% reported, +15.0% organic) |
| Adjusted EBITA | 7,083 (18.6%) | 7,520 (18.7%; +12.3% organic; margin +10bps reported / +50bps organic) | 4,093 (19.3%; +22.1% organic; +120bps organic) | n/a (revenue-only release) |
| Net income, group share | 4,269 | 4,163 (−2%) | 2,488 (+30.1%) | n/a |
| Free cash flow | 4,216 | 4,635 (+10%; cash conversion 111%, 106% adjusted) | 1,631 (+244%; +140% excluding the 2025 fine) | n/a |
| Adjusted EPS (€) | 8.32 | 8.59 (+3%; +13.6% organic) | 4.79 (+20.7%) | n/a |
| Dividend per share (€) | 3.90 | 4.20 (+8%; proposed "subject to Shareholder approval on May 7, 2026"; the AGM vote itself was not verified) | — | — |
| Net debt (period end) | 8,147 | 13,721 | 15,360 (30 Jun 2026) | n/a |

- Q1 2026 revenue was €9,767m (+11.2% organic, +4.7% reported; FX −6.7%; scope +1.1%, mainly Motivair).
- Q2 2026 revenue was €11,459m (+16.5% organic). Q4 2025 revenue was €11,095m (+10.7% organic).

**Quarterly progression**
- Q4 2025: €11,095m, +10.7% organic.
- Q1 2026: €9,767m, +11.2%.
- Q2 2026: €11,459m, +16.5%.
- Q3 2026: €11,460m, +16.9% — a record quarter, up from €11,459m in Q2.

**Energy Management (EM) vs Industrial Automation (IA)**
- FY2025: EM revenue €33,130m (+10.3% organic), adjusted EBITA €7,235m (21.8%, about flat organically). IA €7,022m (+3.0% organic), adjusted EBITA €994m (14.2%). Central costs €709m. — [FY2025 release [company]](https://www.se.com/ww/en/assets/564/document/528237/release-fy-results-2025.pdf)
- H1 2026: EM €17,641m (+15.4% organic), adjusted EBITA €3,957m (22.4%, about +100bps organic). IA €3,585m (+7.7% organic), €501m (14.0%, about +50bps). — [H1 2026 release [company]](https://www.se.com/ww/en/assets/pdf/release-hy-results-2026)
- Q3 2026: EM €9,615m (+18.8% organic); IA €1,845m (+8.1% organic). 9M: EM €27,256m (+16.6%); IA €5,430m (+7.9%). — [Q3 2026 release [company]](https://www.finanzwire.com/press-release/schneider-electric-epa-su-third-quarter-revenues-2026-odiihfxJLgs)

**Regions and business models**
- Q3 2026 by region (organic):
  - North America €4,637m (+19.9%; 40% of the quarter);
  - Europe €2,646m (+8.6%);
  - China & East Asia €2,153m (+26.1%; EM +32.4%);
  - South Asia & International €2,024m (+13.2%).
  — [Q3 2026 release [company]](https://www.finanzwire.com/press-release/schneider-electric-epa-su-third-quarter-revenues-2026-odiihfxJLgs)
- Q3 2026 by business model: Products 48% of revenue (+17% organic), Systems 35% (+22%), Software & Services 17% (+7%). FY2025 mix was Products 47%, Systems 34%, Software & Services 19%. — [Q3 2026 release [company]](https://www.finanzwire.com/press-release/schneider-electric-epa-su-third-quarter-revenues-2026-odiihfxJLgs); [FY2025 release [company]](https://www.se.com/ww/en/assets/564/document/528237/release-fy-results-2025.pdf)
- FY2025 North America: 39% of revenue, +17.0% organic for EM. — [FY2025 release [company]](https://www.se.com/ww/en/assets/564/document/528237/release-fy-results-2025.pdf)

**Data Center & Networks (DC&N) share and growth**
- DC&N was 30% of FY2025 orders ("End-market exposure, % of FY 2025 Orders"). The other end-markets were Buildings 29%, Industry 27% and Infrastructure 14%. — [FY2025 presentation, p.13 [company]](https://www.se.com/ww/en/assets/564/document/528239/presentation-fy-results-2025.pdf)
- CFO Fast (16 Oct 2026): "the exposure to data center last year at the end of the year was 30% on data center and networks"; "The direct exposure on data center was about four points less than that". He expects exposure to rise. — [Investing.com Q3 transcript [company]](https://www.investing.com/news/transcripts/earnings-call-transcript-schneider-electric-posts-record-q3-2026-revenue-93CH-4953279)
- Reuters (19 Nov 2025): Schneider's data-centre business accounts for nearly a quarter of total revenue. — [The Star (Reuters copy) (snippet) [independent]](https://www.thestar.com.my/tech/tech-news/2025/11/19/schneider-electric-seals-23-billion-in-us-data-centre-deals-to-power-ai-boom)
- Quarterly data-centre commentary:

| Quarter | Demand / orders | Sales | Source |
|---|---|---|---|
| Q4 2025 | Pure data-centre demand up triple digits year on year (hyperscale and colocation) | Pure data-centre sales "strong double-digit"; Distributed IT sales slightly down | [FY2025 release [company]](https://www.se.com/ww/en/assets/564/document/528237/release-fy-results-2025.pdf) |
| Q1 2026 | DC&N demand up double digits despite "a single, particularly large order booked in Q1'25" in the base | "Strong double-digit" | [Q1 2026 release [company]](https://finanzwire.com/press-release/schneider-electric-epa-su-first-quarter-revenues-2026-hD4UmP80CSR) |
| Q2 2026 | DC&N demand up triple digits | DC&N sales "strong double-digit"; Distributed IT up low single digits | [H1 2026 release [company]](https://www.se.com/ww/en/assets/pdf/release-hy-results-2026) |
| Q3 2026 | DC&N demand up triple digits; pure data-centre demand up triple digits globally; Distributed IT orders and sales up double digits | Pure data-centre sales "strong double digits" | [Q3 2026 release [company]](https://www.finanzwire.com/press-release/schneider-electric-epa-su-third-quarter-revenues-2026-odiihfxJLgs) |

  The CFO described triple-digit demand growth in "three out of the last four quarters". — [Facilities Dive, 20 Oct 2026 [independent]](https://www.facilitiesdive.com/news/schneider-electric-data-center-earnings/833443/)

**Backlog**
- End-2025 backlog was €25,362m (+18%). EM backlog was €21,340m (+21%), "with the most significant increase seen in Systems in North America due to accelerated demand in the Data Center end-market", and strong growth in backlog for 2027 and beyond. — [FY2025 release [company]](https://www.se.com/ww/en/assets/564/document/528237/release-fy-results-2025.pdf)
- Q3 2026: "another record backlog at quarter-end"; no figure given. — [Q3 2026 release [company]](https://www.finanzwire.com/press-release/schneider-electric-epa-su-third-quarter-revenues-2026-odiihfxJLgs)

**Margin drivers, cash and investment**
- FY2025 drivers:
  - Gross margin 42.1%, −40bps organic.
  - Industrial productivity +€596m.
  - Net price −€179m, with raw materials and tariffs at −€255m, including a tariff impact of about −€160m.
  - Mix −€243m, from Systems growing faster.
  - FX −€482m.
  — [FY2025 release [company]](https://www.se.com/ww/en/assets/564/document/528237/release-fy-results-2025.pdf)
- H1 2026: net tariff impact −€104m, partly offset by "some tariff refunds received at the end of H1". — [H1 2026 release [company]](https://www.se.com/ww/en/assets/pdf/release-hy-results-2026)
- FY2025 operating cash flow €6,748m. R&D cash cost €2,380m (5.9% of revenue). Net capex €1,496m (about 3.7% of revenue). — [FY2025 release [company]](https://www.se.com/ww/en/assets/564/document/528237/release-fy-results-2025.pdf)
- Non-recurring items:
  - a €207m fine paid in 2025 (French case, section 8);
  - impairment of investments in associates of −€388m, mainly Uplight equity and convertible notes.
  — [FY2025 release [company]](https://www.se.com/ww/en/assets/564/document/528237/release-fy-results-2025.pdf)
- 2026 assumptions: restructuring about €450m; effective tax rate 23–25%. FY2026 FX impact estimated at −€300m to −€400m (Oct 2026), revised from −€850m to −€950m (Feb 2026). — [Q3 2026 release [company]](https://www.finanzwire.com/press-release/schneider-electric-epa-su-third-quarter-revenues-2026-odiihfxJLgs); [FY2025 release [company]](https://www.se.com/ww/en/assets/564/document/528237/release-fy-results-2025.pdf)

**Debt, ratings and financing**
- "The Group remains committed to retaining its A-grade credit ratings, which were recently re-affirmed by S&P Ratings and Moody's following announcement on June 30th of the proposed acquisition of Cognite." — [H1 2026 release [company]](https://www.se.com/ww/en/assets/pdf/release-hy-results-2026)
- Financing since Q1 2026:
  - €850m OCEANEs due 2034 (4 Jun 2026), with concurrent repurchase of about 94% of the OCEANEs due 2030;
  - €1.5bn EMTN issue (1 Jul 2026): €800m floating-rate due Jul 2028 and €700m 3.375% due Dec 2033.
  — [H1 2026 release [company]](https://www.se.com/ww/en/assets/pdf/release-hy-results-2026)

**Shareholder returns**
- Buyback €2.5–3.5bn through 2030 (CMD Dec 2025); first €600m tranche in 2026; pause expected in 2027–28. — [Q3 2026 release [company]](https://www.finanzwire.com/press-release/schneider-electric-epa-su-third-quarter-revenues-2026-odiihfxJLgs)
- Reuters called it the first buyback in nearly three years. — [Global Banking & Finance (Reuters copy) (snippet) [independent]](https://www.globalbankingandfinance.com/schneider-strategy/)

**M&A in 2026 (group context)**
- Cognite: 100% for $3.1bn cash, agreed 30 Jun 2026.
- AiDASH: about 90% at an implied enterprise value of $350m, agreed 20 Jun 2026.
- PTC: $205/share cash, about $22.6bn equity value and about $23.7bn enterprise value, a 42.3% premium to $144.03, announced 5 Oct 2026. Targets: €250m cost synergies by year 3 and about €800m revenue synergies. Closing expected by Q3 2027.
- Shelly Group: all-cash tender offer of about €1.2bn, requiring more than 95% ownership, closing expected by Q1 2027.
— [H1 2026 release [company]](https://www.se.com/ww/en/assets/pdf/release-hy-results-2026); [Q3 2026 release [company]](https://www.finanzwire.com/press-release/schneider-electric-epa-su-third-quarter-revenues-2026-odiihfxJLgs); [TheNextWeb, 5 Oct 2026 [independent]](https://thenextweb.com/news/schneider-electric-ptc-22-6bn)

**Longer-term targets (2026–2030, CMD 11 Dec 2025)**
- Organic revenue growth +7–10% CAGR (2025–2030); +250bps cumulative organic adjusted EBITA margin; cash conversion about 100%; ROCE 15–20%.
- Digital Flywheel above 70% of revenue (62% in 2025); Software & Services about 25% (19% in 2025).
— [CMD 2025 release [company]](https://cdn.financialreports.eu/financialreports/media/filings/1651/2025/ISS/1651_iss_2025-12-11_bb1b122f-b857-4156-b220-f276a77441b4.pdf); [FY2025 release [company]](https://www.se.com/ww/en/assets/564/document/528237/release-fy-results-2025.pdf)

### Inferences
- Data-centre orders (triple-digit) are growing much faster than data-centre sales ("strong double digits"). That points to a data-centre book-to-bill well above 1 and a backlog building toward 2027–28, consistent with the CFO's "visibility into 2027 and 2028".
- On the CFO's numbers, DC&N was about 30% and pure data-centre about 26% of FY2025 orders. The 30% figure is an order-mix exposure, not audited revenue.
- On the company's own numbers, EM, which contains data centres, earns about 8 points more adjusted EBITA margin than IA (22.4% vs 14.0% in H1 2026). Data-centre growth is therefore margin-accretive at group level, though Systems mix dilutes gross margin.
- Net debt was €15.4bn in Jun 2026, before paying for PTC (about $23.7bn EV), Cognite ($3.1bn), AiDASH and Shelly. Leverage will rise materially on closing unless the equity component is large; see the share-count note in sections 7 and 10.

### Gaps
- Not obtained: specific S&P and Moody's rating letters and outlooks, and any rating action after the PTC announcement (5 Oct 2026).
- The PTC financing mix (debt, equity or hybrid) was not verified.
- The FY2024 organic growth figure (8.3% vs 8.4%) and the FY2024 DC&N share (a secondary source said 24% of 2024 end-orders) were not verified in primary documents.
- No Q3 2026 backlog figure or data-centre revenue figure in euros has been disclosed.

## (5) Customers and contracts

### Takeaway
Named contracts are mostly US colocation and AI operators:
- Switch: $1.9bn supply-capacity agreement (SCA), Nov 2025, confirmed on Switch's own website.
- Digital Realty: $373m SCA, Nov 2025; no Digital Realty-side confirmation found.
- Compass Datacenters: $3bn five-year prefab agreement, Nov 2023.
- Equinix: software-defined MV switchgear pilot, Oct 2026.
- Nscale: digital-twin pilot, Oct 2026.

Schneider does not name hyperscaler customers and declined to split hyperscaler, colocation and neocloud exposure. No Schneider agreements with Aligned or CyrusOne were found.

### Cited Findings
**Switch**
- The two-phase SCA worth $1.9bn was announced on 19 Nov 2025 at Schneider's Innovation Summit North America, Las Vegas. It covers prefabricated power modules (standardised, pretested layouts), the first North American deployment of Uniflair chillers and a three-year full-service chiller contract.
- Switch campuses: Las Vegas, Tahoe Reno, Atlanta, Grand Rapids and Austin.
- Quotes: Vandana Singh, SVP Secure Power North America, Schneider; Jason Hoffman, Chief Strategy Officer, Switch.
- "The SCA model provides guaranteed capacity, advanced cooling solutions and full-service support." The release does not say whether purchase volumes are binding.
— [Switch.com copy of the release, 19 Nov 2025 [independent – customer]](https://www.switch.com/schneider-electric-and-switch-expand-partnership-with-1-9-billion-supply-capacity-agreement-to-power-ai-factories/); [Schneider US newsroom (snippet) [company]](https://www.se.com/us/en/about-us/newsroom/news/press-releases/Schneider-Electric-and-Switch-Expand-Partnership-with-1-9-Billion-Supply-Capacity-Agreement-to-Power-AI-Factories-691d16cc3a880bee320a9cc6)

**Digital Realty**
- The $373m SCA covers UPS, LV switchgear and prefabricated power skids for US builds, plus a dedicated LVS production line.
- A Schneider spokesperson told Reuters both contracts "are phased across 2025 and 2026".
- Neither DCF nor TechInformed carried a Digital Realty quote.
— [Data Center Frontier, 24 Nov 2025 [independent]](https://www.datacenterfrontier.com/machine-learning/article/55332455/schneider-electrics-23-billion-worth-of-ai-power-and-cooling-deals-sends-message-to-data-center-sector); [TechInformed, 20 Nov 2025 [independent]](https://techinformed.com/schneider-electric-signs-2-27-billion-u-s-data-center-supply-deals-with-switch-and-digital-realty/)
- DCF's reading of the SCA model: Schneider commits dedicated lines and inventory in exchange for forecastable volume. It "signals confidence that AI demand is durable". — [Data Center Frontier, 24 Nov 2025 [independent]](https://www.datacenterfrontier.com/machine-learning/article/55332455/schneider-electrics-23-billion-worth-of-ai-power-and-cooling-deals-sends-message-to-data-center-sector)

**Compass Datacenters**
- A $3bn multi-year (five-year) agreement for prefabricated modular power products ("prefabricated data center power rooms", per Compass CEO Chris Crosby) was announced at Schneider's CMD on 9 Nov 2023.
- About 150 modular solutions had already been delivered from West Chester, Ohio.
- A 110,000 sq ft integration facility sits next to Compass's Red Oak, Texas campus.
— [Lightwave (snippet) [independent]](https://lightwaveonline.com/data-center/article/14301450/schneider-electric-and-compass-datacenters-expand-partnership-with-3b-agreement); [EW (snippet) [independent]](https://www.ewweb.com/news/article/21277180/thats-billion-with-a-b-schneider-seals-3billion-deal-with-compass-datacenters)

**Equinix**
- First live deployment (pilot) of software-defined MV switchgear in a colocation data centre; no site, capacity or results disclosed. — [StorageReview, 2 Oct 2026 [independent]](https://www.storagereview.com/news/schneider-electric-software-defined-medium-voltage-switchgear-yotta-2026-equinix-pilot)

**Nscale**
- Digital-twin pilot (with AVEVA and Start Campus) at SINES, Portugal; no supply contract disclosed. — [HPCwire (27 Oct 2026 release) (snippet) [company]](https://www.hpcwire.com/off-the-wire/schneider-electric-and-partners-pilot-digital-twin-for-nscales-ai-infrastructure/)

**NVIDIA (technology partner, not a customer)**
- 800 VDC data-centre power-systems partner. — [NVIDIA blog, 20 May 2025 [independent – partner]](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/)
- CEO: "being able to work with NVIDIA, with our customer, the large hyperscaler, on how you can design and simulate". — [FY2025 call transcript, 26 Feb 2026 [company]](https://www.se.com/ww/en/assets/564/document/528236/transcript-Q4-results-2025.pdf)

**Hyperscalers and neoclouds**
- CFO: "We do not break down exactly the impact or the split of hyperscaler, colo, neocloud, et cetera." CEO: "We are extremely careful to select those companies that will be there in the long term." — [Facilities Dive, 20 Oct 2026 [independent]](https://www.facilitiesdive.com/news/schneider-electric-data-center-earnings/833443/)
- The CFO referred to Schneider's "position with many of the hyperscalers" in China and growing share of wallet with hyperscalers and colocation operators. — [Investing.com Q3 transcript [company]](https://www.investing.com/news/transcripts/earnings-call-transcript-schneider-electric-posts-record-q3-2026-revenue-93CH-4953279)

**Other projects named in results**
- "Execution on a large data center project" in Indonesia (Q4 2025); data-centre project execution in the Netherlands, the Nordics and Australia; Canadian colocation and "emerging AI-related investments". — [FY2025 release [company]](https://www.se.com/ww/en/assets/564/document/528237/release-fy-results-2025.pdf); [H1 2026 release [company]](https://www.se.com/ww/en/assets/pdf/release-hy-results-2026)

### Inferences
- The SCAs read as capacity reservations (guaranteed capacity, dedicated lines) rather than firm purchase orders. Their headline values ($1.9bn, $373m, $3bn) should be treated as framework values unless the customers disclose take-or-pay terms. No source states binding volumes.
- Only Switch's website independently hosts the Switch announcement, and that text is the joint release. There is no customer filing (e.g., a 10-K) confirming value, so all contract values are effectively company-sourced.

### Gaps
- No Schneider agreements found with Aligned Data Centers or CyrusOne, nor any Nscale supply contract.
- No named hyperscaler contract (Microsoft, Google, Meta, AWS, Oracle) found.
- No Digital Realty or Compass statement or filing verifying contract values found.
- No new data-centre SCA announced between June and November 2026 found. Coverage may be incomplete because the search budget ran out.

## (6) Capacity and lead times

### Takeaway
Schneider says it reviews data-centre capacity every quarter against a two-year demand view. It cites 18–24 months of data-centre visibility and adds capacity both in-house and through partners (Foxconn, Samsung). For lead times it gives seller-defined figures only:
- standardised 2.5 MW prefab blocks "as little as six months" to manufacture, against 12–14 months for earlier customised prefab;
- software-defined MV switchgear "up to 3x" faster ordering and manufacturing, modelled.

Third-party market estimates for MV switchgear lead times range from roughly 20–44 weeks (standard) to 52–80+ weeks; these are not Schneider-specific.

### Cited Findings
**How Schneider plans capacity**
- CEO Blum, FY2025 call (26 Feb 2026) — [FY2025 call transcript [company]](https://www.se.com/ww/en/assets/564/document/528236/transcript-Q4-results-2025.pdf):
  - with large hyperscalers "we freeze the design, we look at the planning they need in terms of capacity and it helps us to adjust our capacity";
  - "if we have a two years visibility on the demand, we can react on capacity. We can do it by ourselves by building extra capacity. But we are also working more and more with different partners", naming Foxconn;
  - capacity review moved from every two to three years, to annually, to "every quarter, we revisit the demand for the next two years";
  - "a large part of what we booked in Q4 will be executed more in '27".
- CFO Maxson on the same call: data-centre visibility of "18 to 24 months", and "all that backlog you see in less than one year, we'd obviously expect to accomplish in 2026". — [FY2025 call transcript [company]](https://www.se.com/ww/en/assets/564/document/528236/transcript-Q4-results-2025.pdf)
- FY2025 US performance: "Recent capacity investment supported enhanced volumes". Industrial productivity of +€596m reflected supply-chain investment "primarily in North America and India in H2'24". — [FY2025 release [company]](https://www.se.com/ww/en/assets/564/document/528237/release-fy-results-2025.pdf)
- CFO Fast (Oct 2026): capacity is being expanded with partners including Foxconn, which should keep pace with triple-digit demand. Prefab can be delivered "inside their normal construction time frames". No lead-time numbers were given. — [Investing.com Q3 transcript [company]](https://www.investing.com/news/transcripts/earnings-call-transcript-schneider-electric-posts-record-q3-2026-revenue-93CH-4953279)

**Plants**
- US: $700m+ through 2027 (Mt. Juliet, TN, new MV facility; El Paso, TX, switchgear and power distribution expansion; eight sites; 1,000+ jobs). — [Manufacturing Dive, Mar 2025 (snippet) [independent]](https://www.manufacturingdive.com/news/schneider-electric-700-million-investment-us-data-center-demand-ai/743630/)
- A data-centre integration facility opened in Texas in June 2024. — [ACHR News (snippet) [independent]](https://www.achrnews.com/articles/163450-schneider-electric-opens-data-center-integration-facility-in-texas)
- Europe: production capacity increased at "its largest data centre factory in Europe" (Barcelona; snippet, URL ID suggests Nov 2024). — [Schneider UK newsroom (snippet) [company]](https://www.se.com/uk/en/about-us/newsroom/news/press-releases/schneider-electric-increases-production-capacity-at-its-largest-data-centre-factory-in-europe-67330db2059b306f8b0853e4)
- Sant Boi de Llobregat has 5,000 m² of dedicated prefab production. — [MGRID, 21 Sep 2026 [independent]](https://mgrid.org/2026/09/21/schneider-electric-launches-a-2-5-mw-prefabricated-power-block-with-north-america-waiting-until-later-this-year/)
- New €100m factory in Macon, France. — [FY2025 presentation, p.22 [company]](https://www.se.com/ww/en/assets/564/document/528239/presentation-fy-results-2025.pdf)
- India: new plant opening in Bengaluru and a new Motivair liquid-cooling factory. — [FY2025 presentation [company]](https://www.se.com/ww/en/assets/564/document/528239/presentation-fy-results-2025.pdf); [FY2025 call transcript [company]](https://www.se.com/ww/en/assets/564/document/528236/transcript-Q4-results-2025.pdf)
- China: power-electronics hub; liquid-cooling manufacturing being accelerated (CEO, Oct 2026). Italy: liquid-cooling capacity (CFO, Oct 2026). — [Investing.com Q3 transcript [company]](https://www.investing.com/news/transcripts/earnings-call-transcript-schneider-electric-posts-record-q3-2026-revenue-93CH-4953279)
- Galaxy VXL planned output: more than 9,000 units in 2025. — [ITdaily, 5 Dec 2024 [independent]](https://itdaily.com/news/datacenter/schneider-electric-galaxy-vxl-ups)

**Capacity reservation**
- The Digital Realty SCA "adds a dedicated LVS production line"; the Switch SCA "provides guaranteed capacity". — [TechInformed, 20 Nov 2025 [independent]](https://techinformed.com/schneider-electric-signs-2-27-billion-u-s-data-center-supply-deals-with-switch-and-digital-realty/); [Switch.com, 19 Nov 2025 [independent – customer]](https://www.switch.com/schneider-electric-and-switch-expand-partnership-with-1-9-billion-supply-capacity-agreement-to-power-ai-factories/)

**Lead times quoted by Schneider**
- Standardised prefab block "can be manufactured in as little as six months", against 12–14 months for earlier customised prefab systems (both Schneider claims). Tarunjeet Sarao, SVP data center systems: deployment "in months rather than years". — [MGRID, 21 Sep 2026 [independent reporting company claims]](https://mgrid.org/2026/09/21/schneider-electric-launches-a-2-5-mw-prefabricated-power-block-with-north-america-waiting-until-later-this-year/)
- Software-defined MV switchgear claims, against conventional engineered-to-order gear in a 20-panel comparison (Schneider White Paper 303; described as "studies and estimations"):
  - up to 3x faster ordering and manufacturing;
  - up to 2x faster commissioning and site acceptance testing;
  - 87% less control wiring.
  — [StorageReview, 2 Oct 2026 [independent reporting company claims]](https://www.storagereview.com/news/schneider-electric-software-defined-medium-voltage-switchgear-yotta-2026-equinix-pilot)

**Third-party market estimates (not Schneider-specific)**
- 15 kV MV switchgear 52–80 weeks; standard switchgear about 20–44 weeks. — [Industrial Sage, 2026 (snippet) [independent]](https://www.industrialsage.com/switchgear-lead-times-2026/)
- 40–80+ weeks for transformers, switchgear and breakers (Jul 2026). — [IPS (snippet) [independent]](https://www.ips.co/news/the-hidden-risk-in-data-center-growth-power-equipment-lead-times)

**Independent caveat**
- "Every number that makes this launch look fast comes from the seller"; "No customer has run the cycle in public yet". Equipment is often not the binding constraint on US sites: "On most US data center sites it is not." — [MGRID, 21 Sep 2026 [independent]](https://mgrid.org/2026/09/21/schneider-electric-launches-a-2-5-mw-prefabricated-power-block-with-north-america-waiting-until-later-this-year/)

### Inferences
- Schneider's lead-time advantage comes from standardisation (fixed 2–2.5 MW blocks, software-defined MV) and from capacity reservation (SCAs). Customers who do not reserve capacity likely face market-level lead times. That is an inference from the SCA design and the third-party estimates.
- Schneider has quantified no lead time for its core MV switchgear or Galaxy UPS in 2026.

### Gaps
- No Schneider-published lead times found for MV switchgear, LV switchboards or Galaxy UPS.
- No capacity figures in MW or units per year for 2026.
- No status found for the Mt. Juliet or El Paso openings.
- Nothing found on Mexico, or on China data-centre power plants other than liquid cooling.

## (7) Ownership and key people

### Takeaway
Schneider is widely held: free float about 86%, BlackRock about 7.7–7.9%, employees about 3.3–3.7%, treasury about 2.6% (aggregator data, 2025–May 2026).

Leadership:
- CEO: Olivier Blum since 4 Nov 2024.
- Chair: Jean-Pascal Tricoire, as of Nov 2024; 2026 status not re-verified.
- CFO: Nathan Fast since 6 Apr 2026, replacing Hilary Maxson.

Data-centre leadership sits in "Secure Power & Data Centers", with conflicting evidence on the global EVP. The share count rose to 603.6m by 22 Oct 2026, from about 574–577m around end-2025; the cause was not verified.

### Cited Findings
**Shareholders**
- Shareholder structure: free float 86.40%, BlackRock, Inc. 7.70%, employees 3.30%, treasury 2.60%. The page shows no date; a search snippet attributes it to COFISEM, 7 May 2026. — [ABC Bourse [independent – data aggregator]](https://www.abcbourse.com/analyses/chiffres/SUp)
- BlackRock about 7.93% (7.9% of shares outstanding, Aug 2025 article); employee share scheme (ESOP) about 3.74%; top 25 shareholders 37.13% (data as of May 2025). — [Simply Wall St (snippet) [independent – aggregator]](https://simplywall.st/stocks/us/capital-goods/otc-sbgs.y/schneider-electric/ownership)
- Employee share offering (Jan 2026):
  - up to 3,700,000 shares, about 0.645% of share capital at 31 Dec 2025;
  - offered in 46 countries, covering about 85% of employees;
  - priced at 85% of the reference price.
  — [Boursorama (snippet) [independent reporting company release]](https://www.boursorama.com/bourse/actualites/schneider-electric-lance-une-augmentation-de-capital-reservee-a-ses-salaries-d7da9b92fcc9beb33881e1c586bc8614)
- CEO: "63% of our employees have invested in our worldwide [plan] last year, with some country growing above 80% of employees." — [FY2025 call transcript, 26 Feb 2026 [company]](https://www.se.com/ww/en/assets/564/document/528236/transcript-Q4-results-2025.pdf)

**Share count**
- 603,605,363 shares; 628,741,439 theoretical and 612,926,447 exercisable voting rights, as of 22 Oct 2026. — [Schneider share-count page [company]](https://www.se.com/ww/en/about-us/investor-relations/regulatory-information/share-count-voting-rights.jsp)
- The same page, as indexed earlier, showed 577,122,512 shares as of 31 Oct 2025. — [Schneider share-count page (snippet) [company]](https://www.se.com/ww/en/about-us/investor-relations/regulatory-information/share-count-voting-rights.jsp)

**Board and executives**
- CEO Olivier Blum: appointed 4 Nov 2024. Previously EVP Energy Management, Chief Strategy & Sustainability Officer and Chief HR Officer; Executive Committee member since 2014. — [Utility Dive, 6 Nov 2024 [independent]](https://www.utilitydive.com/news/schneider-electric-replaces-ceo-peter-herweck-amid-strategic-execution-issue/732175/)
- Chairman Jean-Pascal Tricoire, and vice-chairman and lead independent director Fred Kindle (Nov 2024). — [Utility Dive, 6 Nov 2024 [independent]](https://www.utilitydive.com/news/schneider-electric-replaces-ceo-peter-herweck-amid-strategic-execution-issue/732175/)
- CFO: Hilary Maxson until 5 Apr 2026; Nathan Fast from 6 Apr 2026 (US citizen, joined 2007, previously Head of IR). — [FY2025 release [company]](https://www.se.com/ww/en/assets/564/document/528237/release-fy-results-2025.pdf)
- Investor relations: Amit Bhalla moved roles; Nathan Fast became SVP-Head of IR on 1 Jan 2026. — [CMD 2025 release [company]](https://cdn.financialreports.eu/financialreports/media/filings/1651/2025/ISS/1651_iss_2025-12-11_bb1b122f-b857-4156-b220-f276a77441b4.pdf). Antoine Sage is listed as Investor Relations contact on the H1 2026 release. — [H1 2026 release, 30 Jul 2026 [company]](https://www.se.com/ww/en/assets/pdf/release-hy-results-2026)
- Frederic Godemel is quoted as EVP Energy Management. — [H1 2026 release [company]](https://www.se.com/ww/en/assets/pdf/release-hy-results-2026)
- Governance change: on 29 Jul 2026 the board appointed Julia Liuson (President of Microsoft's Developer Division 2021–2026) as observer. She is to be proposed as an independent director at the 2027 AGM and will join the Digital Committee. — [H1 2026 release [company]](https://www.se.com/ww/en/assets/pdf/release-hy-results-2026)

**Data-centre business leadership (evidence conflicts)**
- Pankaj Sharma has appeared as "Executive Vice President, Secure Power, Data Centers & Global Services". — [Schneider US release (snippet; URL ID suggests Dec 2024) [company]](https://www.se.com/us/en/about-us/newsroom/news/press-releases/Schneider-Electric-Announces-New-Solutions-to-Address-the-Energy-and-Sustainability-Challenges-Spurred-by-AI-674f1aaeda55de201f0ca8c4)
- A Schneider blog author page lists Manish Kumar as "Executive Vice President, Secure Power & Data Centers", leading the global business (undated). — [blog.se.com (snippet) [company]](https://blog.se.com/author/manish-kumar)
- Vandana Singh is SVP Secure Power North America (Nov 2025). — [Switch.com, 19 Nov 2025 [independent – customer-hosted]](https://www.switch.com/schneider-electric-and-switch-expand-partnership-with-1-9-billion-supply-capacity-agreement-to-power-ai-factories/)
- Tarunjeet Sarao is SVP for data center systems (Sep 2026). — [MGRID, 21 Sep 2026 [independent]](https://mgrid.org/2026/09/21/schneider-electric-launches-a-2-5-mw-prefabricated-power-block-with-north-america-waiting-until-later-this-year/)
- Regional Secure Power appointments (all snippets):
  - Matthew Baynes, VP Secure Power & Data Centre UK&I, 6 Jan 2026 ([PR Newswire](https://tools.prnewswire.com/en-us/live/20813/release/20260106EN57245));
  - Steven Santini, VP Secure Power Sub-Saharan Africa, 12 Mar 2026 ([Engineering News](https://www.engineeringnews.co.za/article/schneider-electric-appoints-steven-santini-as-vice-president-secure-power-sub-saharan-africa-2026-03-12));
  - Marco Geiser, VP Secure Power DACH, from 1 Apr 2026 ([Computer&Automation](https://www.computer-automation.de/energy-supply/schneider-electric-marco-geiser-becomes-new-vice-president-secure-power-dach.htm));
  - Damien Dhellemmes, SVP Secure Power & Data Center Europe, undated ([Data Centre Magazine](https://datacentremagazine.com/news/schneider-electric-damien-dhellemmes-takes-europe-svp-role));
  - Sumati Sahgal, VP Secure Power & Data Centres Greater India, undated ([Energetica India](https://www.energetica-india.net/news/schneider-electric-elevates-sumati-sahgal-to-lead-data-centres-and-secure-power-in-greater-india)).
  [independent, reporting company appointments]
- Employees: "160,000 employees and 1 million partners in over 100 countries" (Dec 2025 boilerplate). — [CMD 2025 release [company]](https://cdn.financialreports.eu/financialreports/media/filings/1651/2025/ISS/1651_iss_2025-12-11_bb1b122f-b857-4156-b220-f276a77441b4.pdf)

### Inferences
- The share count rose by about 26.5m shares (about +4.6%) between 31 Oct 2025 (577.1m) and 22 Oct 2026 (603.6m). From the Jan 2026 offering figures, capital at 31 Dec 2025 was about 573.6m shares, implying about +30m (+5%). That is far more than an employee plan (≤3.7m) or OCEANE conversions would explain. One secondary report said PTC would be financed by "a combination of equity and new debt" (snippet, Manufacturing Digital). An equity placement linked to PTC in Oct 2026 is therefore plausible but **unverified**.
- If new shares were issued, BlackRock's and employees' percentages from before Oct 2026 are likely diluted. Current percentages need the next threshold declarations or the 2026 URD.

### Gaps
- The shareholding table of the 2025 Universal Registration Document (filed with the AMF on 27 Mar 2026) was not read. The official 31 Dec 2025 breakdown, double voting rights and other >1% holders (e.g., Norges, Amundi) are unverified.
- Whether Tricoire remained Chair through 2026 was not re-verified.
- The current global head of the data-centre business is unresolved (Sharma vs Kumar).
- The reason for the 2026 share-count increase was not found.

## (8) Legal and regulatory

### Takeaway
- **Antitrust:** France's competition authority fined Schneider €207m in Oct 2024 (decision 24-D-09) for vertical resale price-fixing of LV electrical equipment between 2012 and 2018. Schneider "firmly contests" it and paid the fine in H1 2025. A parallel criminal investigation, opened in 2018, was ongoing at the time of the decision. The appeal outcome was not found.
- **Cyber:** Schneider was a ransomware or data-theft victim in Jan 2024 (Cactus), Nov 2024 (HellCat/Jira) and Oct 2025 (named by Cl0p in the Oracle EBS campaign, 116 GB alleged, unconfirmed by Schneider).
- **Recalls:** the latest found is a 2022 US recall of 1.4m Square D QO load centres. No UPS or data-centre product recall was found for 2024–26.
- **Tariffs:** about −€160m in FY2025 and −€104m net in H1 2026, offset by pricing.
- **EU F-gas Regulation 2024/573:** adopted 7 Feb 2024, applies from 11 Mar 2024. It underpins the SF6-free AirSeT strategy; the switchgear dates were not verified from the legal text in this session.
- **Pending approvals:** the PTC, Cognite, AiDASH and Shelly deals.

### Cited Findings
**French resale price-fixing case**
- Decision 24-D-09 is dated 29 Oct 2024 (press release 30 Oct 2024). Fines: Schneider €207m, Legrand €43m, Rexel €124m and Sonepar €96m, €470m in total.
- The practice was vertical resale price-fixing via the "derogation" system for LV electrical equipment. Schneider's infringement, with Rexel and Sonepar, ran Dec 2012 to Sep 2018.
- The Autorité: derogated prices were "in fact conceived by Schneider Electric and Legrand as fixed prices from the outset" and "all the parties in questions were aware of the illegality of their practices".
- It came to light through a 2018 Paris prosecutor investigation. "The Autorité's decision in no way prejudges the outcome of the criminal proceedings."
— [Autorité de la concurrence, 30 Oct 2024 [independent – regulator]](https://www.autoritedelaconcurrence.fr/en/press-release/electrical-equipment-autorite-imposes-fines-eu470-million-manufacturers-schneider)
- Schneider "conteste fermement" (firmly contests) the decision and reserved the right to appeal. — [EnergyNews / AFP (snippet) [independent]](https://energynews.pro/schneider-electric-rexel-sonepar-et-legrand-condamnes-a-470-millions-deuros-pour-entente-anticoncurrentielle)
- Fine paid: "a fine of -€207 million paid in 2025 in relation to a previously disclosed legal case in France" (H1 2025 per the H1 2026 release). — [FY2025 release [company]](https://www.se.com/ww/en/assets/564/document/528237/release-fy-results-2025.pdf); [H1 2026 release [company]](https://www.se.com/ww/en/assets/pdf/release-hy-results-2026)
- Bloomberg Law's article on the CEO change sits at a URL whose slug reads "schneider-electric-replaces-ceo-after-price-fixing-case". The headline shown in search is "Schneider Electric Ousts CEO After Disagreements Over Strategy". Coverage noted the change came shortly after the French price-fixing fine; the company did not link the two. — [Bloomberg Law (snippet) [independent]](https://news.bloomberglaw.com/antitrust/schneider-electric-replaces-ceo-after-price-fixing-case-2)

**Cyber incidents**
- Jan 2024: Cactus ransomware hit Schneider's Sustainability Business division (Resource Advisor platform). Cactus claimed 1.5 TB. — [SecurityWeek (snippet) [independent]](https://www.securityweek.com/cactus-ransomware-group-confirms-hacking-schneider-electric/amp/); [Data Center Knowledge (snippet) [independent]](https://www.datacenterknowledge.com/data-breaches/-cactus-ransomware-strikes-schneider-electric)
- Nov 2024: a HellCat member ("Grep") claimed theft of 40+ GB from Schneider's Jira developer platform, with a $125,000 ransom demand. Schneider launched a probe. — [SecurityWeek (snippet) [independent]](https://www.securityweek.com/schneider-electric-launches-probe-after-hackers-claim-theft-of-user-data/)
- 28 Oct 2025: the Cl0p leak site named Schneider Electric and Emerson as Oracle E-Business Suite campaign victims, with 116 GB of archives "allegedly belonging to Schneider Electric". Schneider did not respond to SecurityWeek. SecurityWeek's structural analysis found the data "likely originates from an Oracle environment". — [SecurityWeek, 28 Oct 2025 [independent]](https://www.securityweek.com/industrial-giants-schneider-electric-and-emerson-named-as-victims-of-oracle-hack/)

**Product recalls**
- CPSC recall 22-159 (16 Jun 2022): about 1.4m Square D QO Plug-on-Neutral load centres in the US (plus 289,000 in Canada) for thermal burn and fire hazards. — [CPSC (snippet) [independent – regulator]](https://www.cpsc.gov/Recalls/2022/Schneider-ElectricTM-Recalls-1-4-Million-Electrical-Panels-Due-to-Thermal-Burn-and-Fire-Hazards)

**Tariffs and trade**
- FY2025 raw-material impact included "a tariff impact of c.-€160m". Q4 2025 pricing was "led by North America in response to tariffs". — [FY2025 release [company]](https://www.se.com/ww/en/assets/564/document/528237/release-fy-results-2025.pdf)
- H1 2026: net tariff impact −€104m, with "some tariff refunds received at the end of H1". — [H1 2026 release [company]](https://www.se.com/ww/en/assets/pdf/release-hy-results-2026)
- Q3 2026: the company expects to offset raw-material inflation and net tariffs through pricing in 2026. — [Q3 2026 release [company]](https://www.finanzwire.com/press-release/schneider-electric-epa-su-third-quarter-revenues-2026-odiihfxJLgs)
- Commentary: The Register framed the US investment as a way to sidestep tariffs (commentary, not a company-stated reason). — [The Register, 26 Mar 2025 (snippet) [independent]](https://www.theregister.com/2025/03/26/schneider_electric_ai_investment/)

**Geopolitics**
- The Middle East (under 5% of 2025 revenue) fell low single digits in Q1 2026. — [Q1 2026 release [company]](https://finanzwire.com/press-release/schneider-electric-epa-su-first-quarter-revenues-2026-hD4UmP80CSR)
- "Disruption in the Middle East to impact H2, with potential for pressure on global supply chains and increased inflation". — [H1 2026 release [company]](https://www.se.com/ww/en/assets/pdf/release-hy-results-2026)
- An April 2026 price increase responded to the Middle East conflict (oil, transport, plastics). — [Investing.com Q3 transcript [company]](https://www.investing.com/news/transcripts/earnings-call-transcript-schneider-electric-posts-record-q3-2026-revenue-93CH-4953279)

**EU F-gas Regulation (EU) 2024/573**
- "adopted on 7 February 2024 and started to apply on 11 March 2024". — [European Commission F-gas page [independent – regulator]](https://climate.ec.europa.eu/eu-action/fluorinated-greenhouse-gases/f-gas-legislation_en); [EUR-Lex (text not readable in session)](https://eur-lex.europa.eu/eli/reg/2024/573/oj)
- Schneider positions AirSeT (≤24 kV, and 38 kV from 2027–28) as free of SF6 and other F-gases. — [StorageReview, 2 Oct 2026 [independent]](https://www.storagereview.com/news/schneider-electric-software-defined-medium-voltage-switchgear-yotta-2026-equinix-pilot)

**Pending merger approvals**
- PTC: subject to regulatory approvals and PTC shareholders; closing expected by Q3 2027. — [TheNextWeb, 5 Oct 2026 [independent]](https://thenextweb.com/news/schneider-electric-ptc-22-6bn)
- Cognite and AiDASH: subject to regulatory approvals as of 30 Jul 2026. — [H1 2026 release [company]](https://www.se.com/ww/en/assets/pdf/release-hy-results-2026)

### Inferences
- The French case concerns LV distribution products in France, not data-centre products specifically. Its relevance to the data-centre business is reputational and governance-related.
- The three cyber incidents involved corporate IT and an energy-software division, not OT or data-centre products, as far as reported.

### Gaps
- Not found: the appeal status before the Paris Court of Appeal, and the status of the criminal proceedings.
- Not found: any other antitrust investigations (EU, US, China) in 2025–26.
- Not found: details of the 2022 Russia exit (buyer, impairment), export-control or sanctions matters, the URD litigation list, and any UPS or data-centre product recalls or safety notices in 2024–26.
- Not verified from the legal text: the precise F-gas switchgear phase-out dates and voltage bands. Commonly reported: new MV ≤24 kV from 1 Jan 2026; 24–52 kV from 1 Jan 2030; 52–145 kV from 1 Jan 2028; >145 kV from 1 Jan 2032, with derogations where tenders find no alternative. Do not use without checking Annex IV.
- Not found: the regulatory status of the PTC review (HSR, EU) as of 14 Nov 2026.

## (9) Science and engineering — demonstrated, verified, unproven, limits

### Takeaway
Schneider's shipping AC portfolio (LV/MV switchgear, Galaxy UPS, prefab) rests on mature, standards-based technology and commercial volumes. However, the efficiency, density and "dynamic load tolerant" claims found were company-sourced, with no third-party test reports located.
- **AI load swings:** demonstrated as a real grid problem by a Microsoft/OpenAI/NVIDIA team (arXiv Aug 2025; Microsoft blog Oct 2025). Their solution relies on GPU firmware smoothing plus rack-level storage; no electrical vendor is named.
- **800 VDC:** NVIDIA's own material concedes open safety, standards, protection and workforce issues. Dell'Oro (Oct 2026) says SST field reliability is unproven at scale.
- **SF6-free vacuum/air MV switchgear:** in commercial service with utility pilots. No independent type-test certificate was located in this session.

Verdict, as an inference: solid ground for AC equipment; not yet solid ground for facility-level 800 VDC and SSTs; unproven at scale for software-defined MV switchgear.

### Cited Findings
**UPS efficiency**
- Galaxy VXL is quoted at "up to 99%" and "up to 97.5%" efficiency, without mode attribution. A snippet attributes 99% to one mode and 97.5% to another, typically eConversion and double conversion. — [ITdaily, 5 Dec 2024 [independent reporting company spec]](https://itdaily.com/news/datacenter/schneider-electric-galaxy-vxl-ups)
- No independent efficiency measurement was found.

**Dynamic AI loads (who verified what)**
- Paper: "Power Stabilization for AI Training Datacenters", arXiv 2508.14318, submitted 20 Aug 2025 (v2 21 Aug), 57 authors (incl. Ian Buck and Jonah Alben). Findings:
  - synchronous training alternates compute and communication phases, causing large power swings whose amplitude "is ever increasing";
  - their frequency content can match utility-critical frequencies;
  - mitigations were evaluated on real hardware and with Microsoft's in-house cloud power simulator.
  — [arXiv [independent – preprint, not peer-reviewed]](https://arxiv.org/abs/2508.14318)
- Microsoft companion post (13 Oct 2025) — [Microsoft Azure blog [independent]](https://techcommunity.microsoft.com/blog/azurecompute/power-stabilization-for-ai-training-datacenters/4460937):
  - "We have partnered closely with OpenAI and Nvidia";
  - oscillation limits apply in "0.1–20 Hz";
  - "We co-developed a power smoothing feature with Nvidia that was introduced in their GB200 GPUs";
  - rack-level batteries and capacitors work but carry "high cost and rack-space requirements";
  - recommended mix: storage for steady-state fluctuations plus GPU smoothing for ramps;
  - no UPS or electrical-equipment vendor is mentioned.
- NVIDIA's 800 VDC design includes energy storage to "help data center infrastructure handle load spikes" and sub-second GPU power fluctuations. — [NVIDIA blog, 20 May 2025 [independent – partner]](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/)
- Schneider's own claim: "Dynamic load tolerant GVXL". — [FY2025 presentation, p.17 [company]](https://www.se.com/ww/en/assets/564/document/528239/presentation-fy-results-2025.pdf). No third-party validation was found.

**800 VDC claims and limits (NVIDIA as partner)** — [NVIDIA blog, 20 May 2025 [independent – partner]](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/)
- Claimed benefits (vendor claims, not independently verified):
  - up to 5% end-to-end efficiency improvement over 54 V systems;
  - 85% more power through the same conductor size;
  - about 45% less copper than 415 VAC row distribution;
  - up to 70% lower maintenance cost and up to 30% lower TCO.
- Acknowledged limits:
  - "Deploying 800 VDC at the facility level introduces new challenges in safety, standards, and workforce training";
  - "Innovations will still be required to fully deliver possible overcurrent protection reliability and maintenance gains";
  - "fault detection and serviceability in VDC systems is a key area for innovation";
  - protection options listed: fuse-and-disconnect combinations, emerging solid-state devices and safety breakers.
- Dell'Oro (19 Oct 2026) on SSTs: "volumes remain modest, field reliability is unproven at scale"; protection and grounding practices are still being written. OCP draft SST spec: up to 10 MW, ≥98% efficiency from half to full load. — [Dell'Oro [independent]](https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/)
- Schneider's CEO calls the sidecar "a minor evolution of the infrastructure" and full architecture "could be ready by '28". — [FY2025 call transcript [company]](https://www.se.com/ww/en/assets/564/document/528236/transcript-Q4-results-2025.pdf)

**SF6-free MV switchgear**
- AirSeT uses pure air for insulation and vacuum for interruption. Pilots were reported at E.ON (Sweden), GreenAlp (France) and EEC Engie (New Caledonia). — [EnergyGlobal, 19 May 2023 (snippet) [independent]](https://www.energyglobal.com/special-reports/19052023/Secure-migration-to-SF6-free-switchgear/)
- KEMA Labs (CESI) issues IEC 62271 type-test certificates, but none tied to SM or RM AirSeT was found. — [CESI (snippet) [independent]](https://cesi.it/our-expertise/products-expertise/medium-voltage-switchgear-and-switching-device/)
- RM AirSeT 38 kV extends the approach to 36/38 kV, but deliveries only start in 2028. — [StorageReview, 2 Oct 2026 [independent]](https://www.storagereview.com/news/schneider-electric-software-defined-medium-voltage-switchgear-yotta-2026-equinix-pilot)

**Lithium-ion battery fire safety**
- UL 9540A is "the American and Canadian national standard for assessing fire propagation related to thermal runaway events". It tests at cell, module, unit and installation level, and "UL 9540A is the only consensus standard explicitly cited in NFPA 855 for large-scale fire testing". — [UL Solutions [independent – standards body]](https://www.ul.com/services/ul-9540a-test-method)
- Galaxy VXL supports Li-ion and VRLA batteries ([ITdaily [independent]](https://itdaily.com/news/datacenter/schneider-electric-galaxy-vxl-ups)). Schneider's 2.5 MW prefab modules integrate Li-ion batteries ([MGRID [independent]](https://mgrid.org/2026/09/21/schneider-electric-launches-a-2-5-mw-prefabricated-power-block-with-north-america-waiting-until-later-this-year/)). No UL 9540A report or NFPA 855 compliance statement for these Schneider products was found.

**Liquid cooling**
- Market state (Oct 2026): "Multi-megawatt is now table stakes" for CDUs (CoolIT 3 MW, Nidec 3.2 MW prototype). The cold plate drew the most attention; two-phase cooling drew rising interest. — [Dell'Oro, 19 Oct 2026 [independent]](https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/)
- In Q1 2025 direct liquid cooling revenue more than doubled year on year (market-wide). — [Lightwave / Dell'Oro, 8 Jul 2025 [independent]](https://www.lightwaveonline.com/home/article/55301804/schneider-electric-and-vertiv-dominate-the-data-center-physical-infrastructure-market)
- No Schneider/Motivair CDU capacity rating or third-party performance test was found.

**Software-defined MV switchgear**
- The claimed reductions are modelled ("studies and estimations"; White Paper 303, 20-panel comparison); the only live deployment is the Equinix pilot. — [StorageReview, 2 Oct 2026 [independent]](https://www.storagereview.com/news/schneider-electric-software-defined-medium-voltage-switchgear-yotta-2026-equinix-pilot)

### Inferences
These are general engineering background, not sourced in this session; label them as such if used.
- Double-conversion UPS loses energy in both rectifier and inverter, while eco-mode/eConversion bypasses part of that path. The roughly 1.5-point efficiency gap trades against exposure to grid disturbances and the transfer behaviour needed for steep AI load steps.
- DC fault interruption lacks a natural current zero, so 800 VDC protection needs solid-state or hybrid breakers, or fuses. That is why protection, arc-flash and grounding practice is the gating item that NVIDIA and Dell'Oro flag.
- Vacuum interruption plus air insulation is a mature combination for ≤24 kV. Extending to 36–40.5 kV without SF6 enlarges dielectric clearances or needs pressurised air, consistent with RM AirSeT 38 arriving only in 2028.
- Rack-level and UPS-level storage can buffer sub-second AI swings. The Microsoft/NVIDIA team still relies on GPU firmware smoothing for ramps and depleted storage, which suggests electrical-side storage alone has not been shown sufficient at scale.
- On solid ground? Yes for Schneider's AC MV/LV/UPS/prefab products: shipping, standards-based (IEC 62271 class switchgear; IEC 62443-4-2 cited for Galaxy VXL), used by named customers, and with Dell'Oro co-leadership in the market. Not yet for 800 VDC facility architecture and SSTs: no field reliability data, standards still being written, and Schneider's own timing of 2028. Evidence is thin for the software-defined MV and prefab speed claims: seller-modelled, one pilot, no public customer cycle.

### Gaps
- Not found:
  - independent (KEMA/CESI or utility) type-test certificates for SM AirSeT or RM AirSeT;
  - a utility fleet-adoption count;
  - third-party efficiency or dynamic-load tests of Galaxy VXL;
  - UL 9540A results for Schneider Li-ion UPS or prefab;
  - Schneider participation in the OCP 800 VDC or SST specification work;
  - peer-reviewed (as opposed to arXiv) publications on AI power stabilisation involving Schneider equipment.

## (10) Cross-examination and contradictions

### Takeaway
- **Market share:** Dell'Oro's independent data puts Schneider and Vertiv "virtually tied" for global data-centre physical infrastructure share (1Q 2025). That conflicts with Schneider's "#1" positioning language.
- **Data-centre share of the group:** the 30% DC&N exposure is an order measure, not revenue; direct data-centre exposure is about 26%, and Reuters said "nearly a quarter of revenue".
- **800 VDC timing:** NVIDIA says full-scale production is 2027; Schneider's CEO says the full architecture "could be ready by '28".
- **Q3 release date:** the H1 release scheduled it for 29 Oct; it came out on 16 Oct because of the PTC deal.
- **Leadership:** two different people appear as global data-centre EVP, and an aggregator's report that the IR head left is contradicted by Schneider's own release.
- **Speed claims:** lead-time and speed claims are seller-sourced and are criticised by an independent analyst.

Competitor financial cross-checks (Eaton, Vertiv, ABB, Siemens, Legrand, Hitachi Energy, Siemens Energy, GE Vernova) could not be gathered after the search budget ran out.

### Cited Findings
**Contradictions**
- **Market leadership.**
  - Claim (Schneider, 26 Feb 2026): DC&N "#1 in electrical distribution", "Most complete portfolio, Including liquid cooling". — [FY2025 presentation, p.13 [company]](https://www.se.com/ww/en/assets/564/document/528239/presentation-fy-results-2025.pdf)
  - Conflicting evidence: Dell'Oro (1Q 2025) found Schneider and Vertiv "virtually tied for global market share, separated by just a tenth of a percentage point" in data-centre physical infrastructure. — [Lightwave, 8 Jul 2025 [independent]](https://www.lightwaveonline.com/home/article/55301804/schneider-electric-and-vertiv-dominate-the-data-center-physical-infrastructure-market)
  - Earlier, Dell'Oro (4Q 2022) said Schneider held the No.1 position and Vertiv No.2. — [CablingInstall, 2023 (snippet) [independent]](https://cablinginstall.com/data-center/article/14291375/schneider-electric-vertiv-square-off-on-data-center-physical-infrastructure-analyst)
  - The categories differ (electrical distribution vs total data-centre physical infrastructure), so the claims are not strictly contradictory, but "#1" is not independently confirmed for 2025–26.
- **UPS market share (low-quality sources disagree).** Global Market Insights (snippet) puts Schneider largest at about 11% of the UPS market, with ABB, Eaton, Huawei, Schneider and Vertiv together about 65% ([GMI [independent]](https://www.gminsights.com/industry-analysis/ups-market)). MarketsandMarkets (snippet) says the top 5 hold about 40–42% of the data-centre UPS market ([MarketsandMarkets [independent]](https://www.marketsandmarkets.com/ResearchInsight/data-center-ups-market.asp)). Omdia share data were not accessible.
- **Data-centre share of Schneider.**
  - "30%" is DC&N's share of FY2025 orders ([FY2025 presentation [company]](https://www.se.com/ww/en/assets/564/document/528239/presentation-fy-results-2025.pdf)). The CFO called it "exposure" and said direct data-centre exposure was about 4 points lower ([Investing.com Q3 transcript [company]](https://www.investing.com/news/transcripts/earnings-call-transcript-schneider-electric-posts-record-q3-2026-revenue-93CH-4953279)).
  - Reuters (19 Nov 2025): "nearly a quarter of total revenue" ([The Star / Reuters (snippet) [independent]](https://www.thestar.com.my/tech/tech-news/2025/11/19/schneider-electric-seals-23-billion-in-us-data-centre-deals-to-power-ai-boom)).
  - Orders share and revenue share are being conflated in coverage.
- **Data-centre market growth.** Schneider's FY2025 presentation says DC market CAGR ">10%" for 2025–30 ([company](https://www.se.com/ww/en/assets/564/document/528239/presentation-fy-results-2025.pdf)). A secondary summary of CMD coverage said Schneider expects the data-centre market to grow 12–14% CAGR ([Barron's via iTiger (snippet) [independent]](https://www.itiger.com/news/2590854341)). Not reconciled.
- **800 VDC timing.**
  - NVIDIA: full-scale 800 VDC production "coincide[s] with" Kyber in 2027 ([NVIDIA blog [independent – partner]](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/)).
  - Schneider CEO (26 Feb 2026): full architecture "could be ready by '28", impact "between probably '28 and 2030"; sidecar "available immediately" ([FY2025 call transcript [company]](https://www.se.com/ww/en/assets/564/document/528236/transcript-Q4-results-2025.pdf)).
  - Schneider blog (Oct 2025): sidecar to market before Kyber 2027 ([blog.se.com (snippet) [company]](https://blog.se.com/datacenter/2025/10/16/the-1-mw-ai-it-rack-is-coming-and-it-needs-800-vdc-power/)).
  - Dell'Oro (Oct 2026): sidecar "is here", upstream architecture still "ambition and speculation" ([Dell'Oro [independent]](https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/)).
- **Q3 2026 release date.**
  - The H1 2026 release (30 Jul 2026) said "Q3 2026 Revenues will be presented on October 29, 2026" ([H1 2026 release [company]](https://www.se.com/ww/en/assets/pdf/release-hy-results-2026)), and the research brief assumed "late October".
  - Actual: released 16 Oct 2026 ([Q3 2026 release [company]](https://www.finanzwire.com/press-release/schneider-electric-epa-su-third-quarter-revenues-2026-odiihfxJLgs); [Facilities Dive, 20 Oct 2026 [independent]](https://www.facilitiesdive.com/news/schneider-electric-data-center-earnings/833443/)), brought forward "because of the deal" (PTC) ([TheNextWeb, 5 Oct 2026 [independent]](https://thenextweb.com/news/schneider-electric-ptc-22-6bn)).
- **CFO named in the brief.** The brief lists CFO Hilary Maxson. She left on 5 Apr 2026, and Nathan Fast has been CFO since 6 Apr 2026. — [FY2025 release [company]](https://www.se.com/ww/en/assets/564/document/528237/release-fy-results-2025.pdf)
- **IR head.** An executive-moves aggregator reported (23 Jun 2026) that Antoine Sage, SVP & CFO of Secure Power, Data Centre, Power Systems & Services, "has left the company" ([The Official Board (snippet) [independent]](https://www.theofficialboard.com/news/schneider-electric)). Schneider's H1 2026 release (30 Jul 2026) lists Antoine Sage as Investor Relations contact ([company](https://www.se.com/ww/en/assets/pdf/release-hy-results-2026)). This suggests an internal move, not a departure.
- **Global data-centre EVP.** Pankaj Sharma is titled "EVP, Secure Power, Data Centers & Global Services" (Schneider release, about Dec 2024, snippet), while a Schneider blog lists Manish Kumar as "EVP, Secure Power & Data Centers" (undated, snippet). — [se.com (snippet)](https://www.se.com/us/en/about-us/newsroom/news/press-releases/Schneider-Electric-Announces-New-Solutions-to-Address-the-Energy-and-Sustainability-Challenges-Spurred-by-AI-674f1aaeda55de201f0ca8c4); [blog.se.com (snippet)](https://blog.se.com/author/manish-kumar). Unresolved.
- **Prefab speed.** Schneider claims six-month manufacture against 12–14 months previously; MGRID: "Every number that makes this launch look fast comes from the seller … No customer has run the cycle in public yet." — [MGRID, 21 Sep 2026 [independent]](https://mgrid.org/2026/09/21/schneider-electric-launches-a-2-5-mw-prefabricated-power-block-with-north-america-waiting-until-later-this-year/)
- **Software-defined MV speed.** "Up to 3x" faster ordering and manufacturing is labelled by Schneider's own release as "studies and estimations" (White Paper 303). — [StorageReview, 2 Oct 2026 [independent]](https://www.storagereview.com/news/schneider-electric-software-defined-medium-voltage-switchgear-yotta-2026-equinix-pilot)
- **Motivair closing.** Early coverage conflicted: Facilities Dive (21 Oct 2024) said "agreed to acquire" while Silicon UK said "has acquired" ([Silicon UK (snippet) [independent]](https://silicon.co.uk/cloud/datacenter/schneider-electric-motivair-acquisition-584617)). Schneider's scope table resolves it: consolidated from Q1 2025, with one month of scope in Q1 2025 ([FY2025 release [company]](https://www.se.com/ww/en/assets/564/document/528237/release-fy-results-2025.pdf)).
- **Herweck removal.** The board cited "divergences in the execution of the company roadmap", yet J.P. Morgan called it a "major surprise" and said the strategy "remains unchanged". Coverage noted the stock had risen strongly under Herweck. — [Utility Dive, 6 Nov 2024 [independent]](https://www.utilitydive.com/news/schneider-electric-replaces-ceo-peter-herweck-amid-strategic-execution-issue/732175/)
- **Galaxy VXL launch date.** Dated 5 Dec 2024 (ITdaily), 17 Feb 2025 (IPP Media) and 7 Apr 2025 (Malay Mail); a market-research summary calls it an April 2025 launch. Staggered regional launches, but "launch date" varies by source. — [ITdaily [independent]](https://itdaily.com/news/datacenter/schneider-electric-galaxy-vxl-ups); [IPP Media (snippet)](https://ippmedia.com/the-guardian/business/read/schneider-electric-launches-high-effiency-ups-for-ai-data-centres-2025-02-17-151212); [Malay Mail (snippet)](https://www.malaymail.com/news/money/mediaoutreach/2025/04/07/schneider-electric-announces-galaxy-vxl-ups-the-industrys-most-compact-high-density-power-protection-system-for-ai-data-center-and-large-scale-electrical-workloads/373424)
- **AI power-stabilisation authorship.** Microsoft's blog says Microsoft "partnered closely with OpenAI and Nvidia" ([Microsoft [independent]](https://techcommunity.microsoft.com/blog/azurecompute/power-stabilization-for-ai-training-datacenters/4460937)). The arXiv abstract page lists 57 authors without affiliations and does not name OpenAI ([arXiv [independent]](https://arxiv.org/abs/2508.14318)). OpenAI's authorship role is unconfirmed from the paper page.
- **Share count.** 577.1m shares (31 Oct 2025, snippet) and about 573.6m implied at 31 Dec 2025 (Jan 2026 offering) against 603.6m on 22 Oct 2026 ([se.com [company]](https://www.se.com/ww/en/about-us/investor-relations/regulatory-information/share-count-voting-rights.jsp)). No explanatory source was found; see section 7.

**Competitor overlap evidence gathered**
- NVIDIA's 800 VDC "data center power systems" partners are Eaton, Schneider Electric and Vertiv. Silicon and power-component partners include Infineon, Navitas, Delta, Flex Power, LiteOn and Megmeet. — [NVIDIA blog [independent – partner]](https://developer.nvidia.com/blog/nvidia-800-v-hvdc-architecture-will-power-the-next-generation-of-ai-factories/)
- OCP 2026 (Dell'Oro) — [Dell'Oro, 19 Oct 2026 [independent]](https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/):
  - Schneider, ABB, Siemens and Eaton showed 800 Vdc protection and power hardware;
  - Delta showed a 660 kW in-row power rack with 480 kW of battery backup;
  - xFusion showed a 300 kW–1.2 MW sidecar prototype;
  - Rittal/Bosch showed a sidecar demonstrator scaling to 2 MW;
  - Vertiv bought Strategic Thermal Labs, and Johnson Controls bought Alloy Enterprises.
- Market size, per Dell'Oro press-release titles (snippets): $14bn in 2Q 2026 (+27% y/y); $12bn in 1Q 2026 (+28% y/y). — [Dell'Oro 2Q 2026](https://www.delloro.com/news/data-center-physical-infrastructure-market-grows-27-percent-y-y-to-14-billion-in-2q-2026/); [Dell'Oro 1Q 2026](https://www.delloro.com/news/data-center-physical-infrastructure-market-expands-28-percent-y-y-in-1q-2026/) [independent]
- Competitor moves (snippet, market-research summary): Eaton acquired Resilient Power Systems in Jul 2025; Vertiv unveiled OneCore in Aug 2025. — [MarketsandMarkets (snippet) [independent]](https://www.marketsandmarkets.com/ResearchInsight/data-center-ups-market.asp)

### Inferences
- Schneider's Q3 2026 group organic growth of +16.9% and Energy Management's +18.8% sit close to Dell'Oro's market growth of +27–28% in 1H 2026. However, Schneider's numbers include non-data-centre end-markets, so no market-share conclusion can be drawn from them.
- On the seven-company comparison, Schneider is the only one of the seven whose data-centre exposure is mainly in-building (UPS, LV/MV distribution, prefab, cooling). GE Vernova, Siemens Energy, Hitachi Energy and HD Hyundai Electric are grid-side (transformers, HV switchgear, HVDC). Bloom and Caterpillar are on-site generation. Direct product overlap with the other six is mainly in MV switchgear and, through partnerships, on-site power integration. This is an inference; no source compared them.

### Gaps
- Not collected because the search budget was exhausted:
  - Eaton, Vertiv, ABB, Siemens and Legrand Q3 2026 data-centre growth, orders and backlog;
  - Hitachi Energy, Siemens Energy and GE Vernova MV switchgear overlap;
  - Omdia UPS share data;
  - Dell'Oro 2025–26 vendor rankings beyond 1Q 2025.

## (11) What could not be found or verified

### Takeaway
The main unverified items are listed below.
- Customer-side confirmation of most contract values; only Switch hosts the release.
- Schneider-specific lead times for core MV, LV and UPS products.
- Independent test evidence for AirSeT, Galaxy VXL and Li-ion fire safety.
- The precise EU F-gas switchgear dates from the legal text.
- Credit-rating letters and post-PTC rating actions; the PTC financing mix and the cause of the 2026 share-count increase.
- The URD shareholder and litigation sections; the appeal of the French fine.
- The Russia exit; AlphaStruxure and microgrid/BESS status.
- Omdia market share and competitor Q3 2026 figures.

The session's web-search budget was exhausted part-way through, so later checks used only direct fetches of URLs already found.

### Cited Findings
- No published Schneider lead times exist in the documents read: the Q3 2026 release contains no capacity or lead-time comments. — [Q3 2026 release [company]](https://www.finanzwire.com/press-release/schneider-electric-epa-su-third-quarter-revenues-2026-odiihfxJLgs)
- Schneider does not disclose backlog by end-market: CFO Maxson said "we didn't give a backlog breakdown by end markets. And I don't think we would intend to do that." — [FY2025 call transcript [company]](https://www.se.com/ww/en/assets/564/document/528236/transcript-Q4-results-2025.pdf)
- No hyperscaler customer split: "We do not break down exactly the impact or the split of hyperscaler, colo, neocloud, et cetera." — [Facilities Dive, 20 Oct 2026 [independent]](https://www.facilitiesdive.com/news/schneider-electric-data-center-earnings/833443/)

### Inferences
- Several key quantitative claims (contract values, lead times, efficiency, density) rest only on Schneider's own statements: the first two on releases and executive statements, the last two on product specifications. The independent sources found (Dell'Oro, MGRID, Utility Dive, SecurityWeek, the Autorité, NVIDIA and Microsoft) verify market context, governance and legal facts, and some technology risks. They do not verify Schneider's product performance.

### Gaps
Searched for (or attempted) but not found or not verifiable in this session:
1. **Customers:**
   - Digital Realty, Compass or Equinix confirmation of Schneider contract values or terms (binding vs reservation);
   - Aligned, CyrusOne or Nscale supply contracts;
   - named hyperscaler contracts;
   - new data-centre SCAs from Jun to Nov 2026.
2. **Lead times and capacity:**
   - Schneider-quoted lead times for MV switchgear, LV switchboards or Galaxy UPS in 2025–26;
   - capacity in MW or units;
   - status of Mt. Juliet and El Paso;
   - Mexico plants;
   - actual Galaxy VXL output against the 9,000-unit plan.
3. **800 VDC and solid state:**
   - Schneider SST or solid-state breaker product and date;
   - sidecar customer deployments;
   - Schneider role in OCP specifications.
   NVIDIA/Schneider reference designs for GB200/GB300/Mission Control appear only in secondary snippets.
4. **Science:**
   - KEMA/CESI or IEC type-test certificates for SM AirSeT or RM AirSeT;
   - utility adoption counts;
   - independent Galaxy VXL efficiency and dynamic-load tests;
   - UL 9540A/NFPA 855 documentation for Schneider Li-ion UPS and prefab;
   - Motivair CDU performance data.
5. **Financial:**
   - S&P and Moody's rating letters and outlooks, and any action after the PTC announcement (5 Oct 2026);
   - PTC financing structure;
   - explanation of the share-count rise to 603.6m;
   - FY2025 original guidance text;
   - FY2024 DC&N share (a snippet said 24% of 2024 end-orders; unverified);
   - Q3 2026 backlog value.
6. **Ownership and governance:**
   - the 2025 URD shareholding table (31 Dec 2025) and >1% holders other than BlackRock;
   - Chair status in 2026;
   - current global data-centre EVP (Sharma vs Kumar);
   - the original announcement date and price of the Temasek/SEIPL deal (only the 18 Dec 2025 completion and the €5.5bn outflow are sourced).
7. **Legal and regulatory:**
   - French fine appeal outcome and criminal case status;
   - other antitrust matters;
   - URD litigation list;
   - Russia exit (2022) details;
   - export-control or sanctions issues;
   - UPS or data-centre product recalls in 2024–26;
   - exact F-gas Annex IV switchgear dates (EUR-Lex text did not render);
   - PTC antitrust review status.
8. **Microgrids and storage:** AlphaStruxure (Carlyle JV) 2025–26 status and data-centre microgrid projects; a Schneider BESS product line for data centres.
9. **Market data and competitors:**
   - Omdia UPS or data-centre power share;
   - Dell'Oro vendor shares after 1Q 2025;
   - competitor (Eaton, Vertiv, ABB, Siemens, Legrand, Hitachi Energy, Siemens Energy, GE Vernova) Q3 2026 data-centre figures for cross-checking.
