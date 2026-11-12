# Co-packaged optics, CPO switch makers, AI-cluster connectors and fibre, and processor-to-processor optical links (worldwide, as of 12 November 2026)

Research date: 12 Nov 2026. Scope: system-level adopters of co-packaged optics (CPO), optical-interconnect start-ups, packagers of optical engines, connector and fibre makers. Lasers, plug-in modules, silicon-photonics foundries and photonic test are another researcher's scope (touched here only where they bear on a key company's path, e.g. Marvell-Lumentum).

Conventions:
- Every figure carries the period covered and the publication date where known. "Derived" = my arithmetic on cited figures.
- "Company claim, unconfirmed" = no outside party has confirmed it. "Secondary" = trade press, analyst or blog estimate.
- No share prices, valuation multiples, market capitalisation, price targets or share-price moves are used (deal values are given only where they define a transaction).
- Research-process caveat (matters for how much weight to put on gaps): mid-run, the shared web-search budget was exhausted and the Exa and Firecrawl tools ran out of credits. After that, only direct fetches of already-found URLs and companies' own IR press-release feeds were possible. As a result, Japanese (TDnet/EDINET), Chinese (cninfo/SSE/SZSE/HKEX), Korean (DART), Indian (NSE/BSE) and Israeli (MAYA) filings were NOT checked, and coverage of mainland-China, Japan, Korea, India and most of Europe is thin. Section 7 lists these gaps.

---

## 1. Segment map

### Takeaway
The CPO and AI-fibre value chain is concentrated in the US (NVIDIA, Broadcom, Marvell, Arista, Cisco, Corning, Amphenol) and Taiwan (TSMC COUPE, SPIL/ASE, KYEC, Accton, Wiwynn). Israel matters through NVIDIA's ex-Mellanox networking unit and through start-ups that are being bought up (DustPhotonics, which Credo bought; Teramount, which Molex apparently bought). Europe has start-ups but no system-level CPO adopter. Japan supplies fibre, connectors and substrates, and its primary filings show it is a big AI-fibre winner in 2026: Fujikura's Information & Communications profit nearly tripled in H1 FY26, and Sumitomo Electric and Furukawa both cite data-centre optical demand. Korea's role is substrates and packaging only; no Korean CPO switch or optical-I/O company turned up. Mainland China has its own domestic AI-networking and fibre up-cycle, which its Q3 2026 filings confirm: Ruijie revenue +37% on data-centre switches; YOFC +86% with both volume and price rising; T&S +65%. None of these firms is on NVIDIA's CPO capacity-expansion list. Their CPO product status was not verified. India has no real player in this segment beyond design centres.

### Map (home country; listing/ticker or private; role; why it matters or why left brief)

**A. Switch-chip and switch-system makers**

| Company | Home | Listing | Role | Why it matters / status of evidence |
|---|---|---|---|---|
| NVIDIA (networking unit, roots in Israel's Mellanox) | US / Israel | Nasdaq: NVDA | Switch silicon and systems (Spectrum-X Ethernet, Quantum-X InfiniBand, NVLink switch); CPO switches (Quantum-X Photonics, Spectrum-X Photonics, Spectrum-6 CPO) | KEY. Largest networking vendor by revenue (above $17.5B in the quarter to Jul 2026). Has a production CPO deployment (Lambda, Jun 2026). Locks up CPO back-end capacity through prepayments. |
| Broadcom | US | Nasdaq: AVGO | Merchant switch silicon (Tomahawk 6/7), CPO switches (TH5-Bailly, TH6-Davisson), optical DSPs, lasers | KEY. Third-generation CPO with Meta-published reliability data; Tomahawk 7 (200T) taped out Sep 2026. |
| Marvell | US | Nasdaq: MRVL | Electro-optic DSPs, Teralynx switches, Celestial AI Photonic Fabric (scale-up optics), XConn; agreed to merge with Lumentum | KEY. The largest successor-side bet: closed Celestial AI in Feb 2026 and agreed in Nov 2026 to buy Lumentum (all-stock). |
| Arista | US | NYSE: ANET | Ethernet switch systems (mostly Broadcom silicon), EOS software, XPO pluggable MSA, Etherlink SU-144 scale-up racks | KEY. Leading AI-Ethernet systems vendor; openly resists proprietary CPO. |
| Cisco | US | Nasdaq: CSCO | Silicon One G300 102.4T chip and systems; Acacia optics | Brief. Says it has CPO technology but is "looking for business alignment" (Feb 2026); $9.3B hyperscale AI orders in FY26. |
| Celestica | Canada | NYSE/TSX: CLS | ODM/JDM switch systems for hyperscalers (HPS); DS6005 CPO switch announced 12 Oct 2026 | Brief. Fast growth, thin margins (adjusted operating margin 8.5%). |
| Accton | Taiwan | TWSE: 2345 | ODM white-box switches (800G) | Brief. Record Q3 2026 revenue. Q3 2026 financial statements not yet in TWSE open data as of 12 Nov 2026 (filing deadline mid-November), so margins and EPS are unavailable. |
| Wiwynn | Taiwan | TWSE: 6669 | Rack integrator | Strategic investor in Ayar Labs; integrates TeraPHY into its racks (2026). Jan-Sep 2026 (TWSE open data; read as year-to-date): revenue NT$989.3B, gross margin ~8.6%, operating margin ~7.1%, basic EPS NT$94.04 (derived ratios). |
| Micas Networks | Not verified | Private | White-box switches on Broadcom TH6, including a 1RU Davisson CPO box | Davisson CPO switch due Q1 2027; pluggable TH6 versions Q4 2026 (StorageReview). |
| Xsight Labs | Israel | Private | Ethernet switch silicon / DPU | Left brief: no 2026 evidence retrieved. |
| Huawei | China | Private (employee-owned) | CloudEngine switches; in-house optics | Left brief: not verified in this run (search budget exhausted); cut off from US supply chains by export controls. |
| H3C (Unisplendour subsidiary) | China | Parent SZSE: 000938 | Switches, servers; "computing x connectivity" strategy | Parent 9M 2026 (Q3 report, 30 Oct 2026): revenue RMB102.16B (+32.1%), net profit RMB2.77B (+97.5%), operating cash flow RMB-8.58B; cites intelligent-computing and domestic-substitution opportunities. CPO status not verified. |
| Ruijie Networks | China | SZSE: 301165 | Switches incl. white-box for Chinese hyperscalers | 9M 2026 (Q3 report, 20 Oct 2026): revenue RMB14.60B (+36.7%; Q3 RMB5.76B, +43.0%), "mainly due to growth in data-centre switch product revenue". Raising funds for "high-speed interconnect network systems for large-scale intelligent-computing clusters". CPO status not verified. |
| ZTE | China | SZSE: 000063 / HKEX: 0763 | Switches, servers, telecom | 9M 2026 (Q3 report, 27 Oct 2026): revenue RMB116.84B (+16.2%; Q3 +34.0%), net profit RMB4.06B (-23.7%). CPO status not verified. |
| Nokia (incl. ex-Infinera) | Finland | Nasdaq Helsinki / NYSE: NOK | Pushing into AI data-centre optics with Infinera's lasers | Headline only (Fierce Network, 6 Nov 2026); content blocked. |

**B. Optical-interconnect start-ups and recent acquisitions**

| Company | Home | Status | Role | Evidence |
|---|---|---|---|---|
| Ayar Labs | US | Private | TeraPHY optical-I/O chiplets + SuperNova remote laser | $500M Series E (3 Mar 2026; $3.75B post-money; total raised $870M) + $150M (10 Sep 2026); Wiwynn investor; NVLink Fusion ecosystem member (Jun 2026). |
| Lightmatter | US | Private | Passage M1000/L200 photonic interconnect (NPO to CPO) | $850M raised; $4.4B at Series D (Oct 2024). Company roadmap: NPO 2026, CPO 2027, photonic interposer 2028+. No named volume customer found. |
| Celestial AI | US | Acquired by Marvell, closed 2 Feb 2026 | Photonic Fabric optical interposer / scale-up | ~$1.3B cash + ~24.5M shares + revenue-milestone earnout to FY2029 (Marvell 10-K). |
| Nubis Communications | US | Acquisition by Ciena announced 22 Sep 2025 | 6.4T CPO/NPO engines; active copper cables | First Ciena product built on it: Vesta 200 6.4T CPX pluggable CPO engine (25 Feb 2026). |
| Hyperlume | North America (country not stated in release) | Acquired by Credo; closing announced 29 Sep 2025 | MicroLED chip-to-chip links | Credo launched the OCP SRMO micro-emitter optics workstream (12 Oct 2026). |
| DustPhotonics | Israel | Acquired by Credo; agreed 13 Apr 2026, closed 28 May 2026 | Silicon-photonics PICs for 800G/1.6T/3.2T, NPO/CPO | Upfront $750M cash + ~0.92M Credo shares + up to ~3.21M contingent shares (Credo release, 13 Apr 2026). Booked total consideration $1.251B: $769.6M cash, $169.1M shares, $310M contingent at fair value (Credo 10-Q, quarter to 1 Aug 2026). Lead from another researcher ("~$750M cash plus stock, completed by 1 Aug 2026") CONFIRMED. |
| Teramount | Israel | Apparently absorbed by Molex (unconfirmed) | Detachable fibre-to-chip connectors (TeraVERSE) | teramount.com 301-redirects to a Molex "TeraVERSE detachable optical chiplet connectors" product page (observed 12 Nov 2026). No deal announcement retrieved. |
| Enosemi | US | Reported acquired by AMD (2025) | Silicon-photonics design | NOT verified in this run (AMD IR feed failed). |
| aiXscale Photonics | Germany | Reported acquired by Astera Labs (2025) | Fibre-to-chip coupling | NOT verified in this run (Astera IR feed blocked). |
| Ranovus | Canada | Private | CPO engines | No 2026 evidence retrieved. |
| Oriole Networks | UK | Private | Photonic network fabric | No 2026 evidence retrieved. |
| OpenLight | US | Private | Open silicon-photonics platform with integrated lasers | Named by Fierce (16 Oct 2026); funding not verified. |
| Avicena | US | Private | MicroLED parallel links | No 2026 evidence retrieved. |
| Salience Labs | UK | Private | Photonic switching | $125M Series B led by Bullhound (AMD Ventures, Intel Capital, HRT, British Business Bank) per Fierce (Oct 2026). |
| iPronics | Spain | Private | Programmable silicon-photonics optical circuit switch | Named by Fierce (Oct 2026). |
| Enlightra | Switzerland | Private | Comb lasers (>50 wavelengths) for GPU/TPU links | Named by Fierce (Oct 2026). |
| Quintessent | US | Private | Quantum-dot DWDM comb lasers | $40M Series A (Aug 2026). |
| Lumilens | Not stated | Private | Optical start-up (product not stated in source) | >$700M Series C (Aug 2026) at $5.51B; total >$900M. |

**C. Packagers, test and substrates for optical engines**

| Company | Home | Listing | Role | Evidence |
|---|---|---|---|---|
| TSMC | Taiwan | TWSE: 2330 / NYSE: TSM | COUPE photonic-engine packaging (SoIC-based) | Used by Broadcom Davisson (16 x 6.4T engines) and NVIDIA Spectrum-X CPO (secondary). |
| SPIL (ASE Technology group) | Taiwan | ASE: TWSE 3711 / NYSE: ASX | NVIDIA's CPO optical-engine packager | NVIDIA, GTC Berlin (21 Oct 2026): 15x optical-engine capacity by mid-2027, doubling again by end-2028. ASE group Jan-Sep 2026 (TWSE open data; read as year-to-date): revenue NT$608.9B, gross margin ~21.2%, operating margin ~11.8%, basic EPS NT$14.17 (derived ratios). |
| KYEC | Taiwan | TWSE: 2449 | Test | $1.1B NVIDIA capacity-reservation advance for a US test site (HVM Apr 2027). Jan-Sep 2026 (TWSE open data; read as year-to-date): revenue NT$33.5B, gross margin ~38.9%, operating margin ~26.1%, basic EPS NT$5.78 (derived ratios). |
| Amkor | US / Korea | Nasdaq: AMKR | Interposers / advanced packaging | $1.5B multi-year NVIDIA partnership (Jul 2026). |
| IBIDEN (Japan, TSE 4062), Unimicron (Taiwan, TWSE 3037), Samsung Electro-Mechanics (Korea, KRX 009150) | | | Substrates | Under NVIDIA capacity reservations (Oct 2026); Korea's only verified role in this chain. |
| Fabrinet | Thailand (Cayman) | NYSE: FN | Optical contract manufacturing | No 2026 data retrieved (IR feed blocked). |
| Foxconn | Taiwan | TWSE: 2317 | NVIDIA silicon-photonics ecosystem partner (GTC 2025) | Not re-verified in 2026. |

**D. Connectors, fibre and cable**

| Company | Home | Listing | Role | Evidence |
|---|---|---|---|---|
| Corning | US | NYSE: GLW | Fibre, cable, connectivity; multicore fibre; CPO fibre systems | KEY. Meta deal up to $6B (Jan 2026); NVIDIA partnership (May 2026): 10x US connectivity capacity. |
| Amphenol (incl. ex-CommScope CCS) | US | NYSE: APH | Copper and fibre interconnect | KEY. Closed CCS 12 Jan 2026. Communications Solutions +51% organic in Q3 2026. |
| US Conec | US | Private | MTP/MPO, MMC very-small-form-factor connectors, PRIZM expanded-beam ferrules | Licensed PRIZM TMT to Corning (11 Mar 2026). |
| Senko | Japan | Private | Connectors (SN-MT etc.) | Founding participant in the OCP SRMO workstream (12 Oct 2026). |
| Molex (Koch Industries) | US | Private | Optical connectors; TeraVERSE (ex-Teramount) | See Teramount above. |
| Samtec | US | Private | CPX co-packaged copper connectors | Ciena's CPO engine targets compatibility with Samtec CPX (Feb 2026). |
| TE Connectivity | Switzerland / Ireland | NYSE: TEL | High-speed copper/optical interconnect | No 2026 data retrieved. |
| Fujikura (incl. AFL) | Japan | TSE: 5803 | Fibre, high-density cable, connectors, optical components | KEY (added). Information & Communications segment H1 FY26 (Apr-Sep 2026): sales ¥581.5B (+91.6%), operating profit ¥217.7B (+194.8%; ~37% margin), on data-centre demand (TDnet, 10 Nov 2026). AFL is in the SRMO workstream. |
| Sumitomo Electric | Japan | TSE: 5802 | Fibre incl. multicore; optical wiring; optical devices | Info & Comms segment H1 FY26: sales ¥201.5B (+48.8%), operating profit ¥61.2B, on "data-centre optical wiring products, optical devices" for generative AI (TDnet, 30 Oct 2026). Only ~7% of group sales; autos dominate. |
| Furukawa Electric (OFS, Lightera brand not verified) | Japan | TSE: 5801 | Fibre and cable; optical semiconductors | Optical Solutions segment H1 FY26: sales ¥130.9B (+43.9%), operating profit ¥23.6B (up ¥22.9B y/y) on data-centre fibre/cable volume, price revisions and mix. FY guide raised on 9 Nov 2026 (TDnet). |
| Huber+Suhner | Switzerland | SIX: HUBN | Fibre connectivity; optical circuit switching | No 2026 data retrieved. |
| Rosenberger | Germany | Private | Connectors | No 2026 data retrieved. |
| Prysmian (added) | Italy | Borsa Italiana: PRY | Fibre cable | No 2026 data retrieved. |
| YOFC | China | SSE: 601869 / HKEX: 6869 | Fibre and cable | 9M 2026 (Q3 report, 31 Oct 2026): revenue RMB19.12B (+86.1%; Q3 RMB9.32B, +139.4%); net profit +1,205%. Industry "entering an up-cycle" as intelligent-computing centre construction accelerates, with main products' sales volume AND average unit price both up substantially. Founding participant in SRMO (Oct 2026). Hollow-core fibre work not verified. |
| T&S Communications | China | SZSE: 300570 | High-density passive optical connectivity (MPO etc.) | 9M 2026 (Q3 report, 30 Oct 2026): revenue RMB2.008B (+65.4%; Q3 RMB1.007B, +161%); net profit RMB295M (only +13.3%) because of USD depreciation FX losses, ramp inefficiency on new products and capacity, raw-material price rises and rush-delivery costs. Receivables +111%. |
| Sterlite Technologies (STL) | India | NSE: STLTECH | Fibre and cable | No 2026 data retrieved. |
| Credo | US (Cayman) | Nasdaq: CRDO | Active copper cables; ZeroFlap optics; micro-emitter optics (SRMO) | Bought Hyperlume (2025) and DustPhotonics (2026). |
| Ciena | US | NYSE: CIEN | Nubis-based pluggable CPO engine; interconnects segment from FY27 | FY29 targets: ~30% revenue CAGR 2026-29 (16 Sep 2026). |
| BizLink (Taiwan, TWSE 3665), Foxlink (Taiwan, TWSE 2392), ams OSRAM (Austria, SIX: AMS), Heraeus Covantics (Germany, private) | | | Cable assemblies / emitters / glass | SRMO participants (Oct 2026). |

Regions with thin coverage: mainland China (switch vendors, YOFC, T&S, domestic CPO), Japan (Fujikura, Sumitomo, Furukawa local briefings), Korea (beyond substrates), India (beyond design centres) and Europe's connector makers. The cause is the tool constraint described at the top, not evidence that these companies are absent.

### Cited findings for the map
- NVIDIA networking revenue above $17.5B in Q2 FY27, more than Cisco's total revenue ($17.3B) for the same period; Dell'Oro estimates NVSwitch at about one third of NVIDIA networking revenue — [The Register, 31 Oct 2026](https://www.theregister.com/networks/2026/10/31/backbone-of-a-beast-charting-nvidias-rise-to-networking-titan/5306499)
- Marvell-Lumentum merger agreement (8-K/425 dated 1-2 Nov 2026) — [SEC](https://www.sec.gov/Archives/edgar/data/0001835632/000119312526442723/d81187d425.htm)
- Celestial AI close 2 Feb 2026; XConn close 10 Feb 2026 — [Marvell FY26 10-K](https://www.sec.gov/Archives/edgar/data/1835632/000183563226000011/mrvl-20260131.htm)
- Ciena-Nubis announced 22 Sep 2025; Vesta 200 6.4T CPX on 25 Feb 2026 — Ciena IR press-release feed ([investor.ciena.com](https://investor.ciena.com/feed/PressRelease.svc/GetPressReleaseList?LanguageId=1&bodyType=1&pressReleaseDateFilter=3&pageSize=200&pageNumber=0&year=2025))
- Credo-Hyperlume (closing announced 29 Sep 2025), Credo-DustPhotonics (agreed 13 Apr 2026, closed 28 May 2026), SRMO workstream (12 Oct 2026) — Credo IR feed ([investors.credosemi.com](https://investors.credosemi.com/feed/PressRelease.svc/GetPressReleaseList?LanguageId=1&bodyType=1&pressReleaseDateFilter=3&pageSize=200&pageNumber=0&year=2026))
- Amphenol completed the CommScope CCS acquisition on 12 Jan 2026 — [Amphenol release](https://s21.q4cdn.com/564806605/files/doc_news/2026/Jan/12/2026_01_12-PR-Closes-acq-of-CCS.pdf)
- Start-up funding (Lumilens, Salience, Quintessent; Ayar, OpenLight, iPronics and Enlightra named) — [Fierce Network, 16 Oct 2026](https://www.fierce-network.com/broadband/5-optical-startups-watch-ai-pushes-optics-deeper-network) (secondary)
- Ayar Labs Series E and extension — [Insight Partners, Mar 2026](https://www.insightpartners.com/ideas/ayar-labs-closes-500m-series-e-accelerates-volume-production-of-co-packaged-optics/); [SiliconANGLE, 10 Sep 2026](https://siliconangle.com/2026/09/10/ayar-labs-bags-150m-in-additional-series-e-funding-to-help-make-bigger-ai-chip-clusters/)
- Lightmatter roadmap and funding (company page, updated 24 Apr 2026; company claims) — [lightmatter.co/llms.txt](https://lightmatter.co/llms.txt)
- NVIDIA's six-partner capacity push (SPIL, KYEC, Amkor, IBIDEN, SEMCO, Unimicron) — [TechTimes, 22 Oct 2026](https://www.techtimes.com/articles/329352/20261022/nvidia-locks-ai-chip-testing-optics-capacity-six-partner-prepayment-push.htm) (secondary, attributed to NVIDIA's newsroom release)
- Micas Davisson 1RU CPO switch due Q1 2027 — [StorageReview](https://www.storagereview.com/news/micas-networks-tomahawk-6-102t-switches-davisson-cpo) (secondary)
- Celestica DS6005 CPO switch, 12 Oct 2026 — [Celestica release](https://corporate.celestica.com/news-releases/news-release-details/celestica-introduces-ds6005-data-center-switch-co-packaged) (title only; page returned 403, so the silicon and dates are unverified)
- NVIDIA-Rebellions-SK Telecom NVLink Fusion collaboration (8 Nov 2026), the only Korea system-level item found — [NVIDIA newsroom](https://nvidianews.nvidia.com/news)

### Inferences
- Optical-interconnect start-ups are being absorbed by integrated platform companies (Marvell, Ciena, Credo, apparently Molex, and reportedly AMD and Astera) rather than reaching independent scale. Of the start-ups named in the brief, only Ayar Labs and Lightmatter remain well funded and independent.
- No mainland-Chinese vendor appears among NVIDIA's CPO supply-chain expansion partners ([SimpleTechTrend, 26 Oct 2026](https://www.simpletechtrend.com/en/post/nvidia-cpo-prepaid-capacity-spil-kyec-2026-w43-en), secondary). Chinese CPO efforts therefore look like a separate domestic track, but I could not verify their 2026 status.

### Gaps
- Status in 2026 of Huawei, H3C, Ruijie and ZTE CPO switches; YOFC hollow-core fibre; T&S; Sterlite; Fujikura, Sumitomo and Furukawa AI-fibre results; Xsight, Ranovus, Oriole and Avicena funding and products; the AMD-Enosemi and Astera-aiXscale deals; Molex-Teramount deal terms.

---

## 2. Evidence on tests (a) to (e) for key companies

Key companies chosen: NVIDIA (networking and optics), Broadcom, Arista, Corning, Amphenol and Marvell. Cisco, Celestica, Accton, Credo and Ciena get brief financial profiles at the end of this section.

### 2.1 NVIDIA — networking and optics (weight in group: about 18% of revenue)

**Takeaway.** NVIDIA's networking unit is now larger than Cisco by quarterly revenue. It is the only vendor with a named production CPO-switch deployment, and it is turning CPO back-end capacity into a constraint it controls, through prepayments to SPIL and KYEC and its partnership with Corning. Its CPO switches have slipped by 6-12 months against the GTC 2025 plan. Group margins and net cash are exceptional; concentration is in hyperscalers and neoclouds.

**(a) Position.**
- "Judge" or constraint: NVIDIA does not own the fab. CPO engines are packaged by TSMC (COUPE, secondary source) and SPIL. What NVIDIA does own is the system reference design (NVLink, Spectrum-X, Quantum-X), which in practice decides which optics and connectors get qualified into its AI factories. It is also buying scarce back-end capacity in advance: SPIL 15x optical engines by mid-2027; KYEC $1.1B test prepayment; Amkor $1.5B — [TechTimes, 22 Oct 2026](https://www.techtimes.com/articles/329352/20261022/nvidia-locks-ai-chip-testing-optics-capacity-six-partner-prepayment-push.htm). It has also contracted a 10x US connectivity-capacity build at Corning — [Corning/NVIDIA release, 6 May 2026](https://investor.corning.com/news-and-events/news/news-details/2026/NVIDIA-and-Corning-Announce-Long-Term-Partnership-To-Strengthen-U-S--Manufacturing-for-AI-Infrastructure/default.aspx).
- BRIDGE / SUCCESSOR by product:
  - Quantum-X800 / Spectrum-X800 switches with pluggable optics: BRIDGE.
  - Quantum-X Photonics (Q3450-LD; 144 x 800G, 18 laser modules, 144 MPO connectors, liquid-cooled): SUCCESSOR, in production at Lambda alongside GB300 NVL72 in June 2026 — [Glenn Klockwood notes](https://www.glennklockwood.com/garden/spectrum-x-photonics) (secondary).
  - Spectrum-X Photonics: SUCCESSOR. Announced at GTC 2025 with a "2025" ship date; it shipped "to select partners" only in 2026 — [TechTimes](https://www.techtimes.com/articles/329352/20261022/nvidia-locks-ai-chip-testing-optics-capacity-six-partner-prepayment-push.htm) (secondary). HPCwire (Apr 2026) said the Spectrum-X CPO switch was due to start shipping by end-Q3 2026, per the search summary. SLIP: roughly 6-12 months.
  - Spectrum-6 CPO (409.6 Tb/s, 512 x 800G), unveiled Jul 2026 in copper and CPO versions; Ian Buck calls it "the building block for scale-out networking for Vera Rubin" — [SDxCentral, 21 Oct 2026](https://www.sdxcentral.com/news/nvidia-targets-15x-optics-capacity-expansion-by-2027-to-meet-cpo-demand/).
  - In-rack copper NVLink (NVL72; Kyber NVL144 copper-only): BRIDGE. Successors are a CPO NVLink switch for multi-rack NVL576 pods and native CPO on the GPU package with Feynman in 2028 — [Counterpoint, 2 Apr 2026](https://counterpointresearch.com/en/insights/from-blackwell-to-feynman-analyzing-nvidias-optics-roadmap) (secondary); [SemiAnalysis, GTC 2026](https://newsletter.semianalysis.com/p/nvidia-the-inference-kingdom-expands) (secondary): Jensen Huang called Feynman NVL1152 "all CPO".
  - Optics-on-Interposer (OOI): research prototype shown at SEMICON West, 13 Oct 2026. "No commercialization timeline"; framed as post-2028 — [GCN, 27 Oct 2026](https://gcn.com/?p=22794).

**(b) Lead (outside evidence).**
- Dell'Oro's Sameh Boujelbene credits integrated compute plus networking. NVIDIA has "bigger datacenter Ethernet sales than any other vendor", and Meta uses Spectrum switches at its Prometheus cluster — [The Register, 31 Oct 2026](https://www.theregister.com/networks/2026/10/31/backbone-of-a-beast-charting-nvidias-rise-to-networking-titan/5306499).
- Lambda's production CPO deployment is the only named customer deployment found — [Klockwood](https://www.glennklockwood.com/garden/spectrum-x-photonics) (secondary).
- NVIDIA's CPO benefit claims (3.5x power efficiency, 10x resiliency, etc.) are company claims, unconfirmed — [NVIDIA release, 2025](https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Announces-Spectrum-X-Photonics-Co-Packaged-Optics-Networking-Switches-to-Scale-AI-Factories-to-Millions-of-GPUs/default.aspx).
- I found no NVIDIA-specific CPO reliability data published by a customer.

**(c) Revenue model.**
- Networking is one-off hardware: switches, NICs, NVLink switch trays. NVIDIA is mainly the payer of prepayments and has supply and capacity commitments of $279B (up from $119B) — [10-Q, quarter to 26 Jul 2026](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000075/nvda-20260726.htm).
- It also receives customer advances: $2.8B balance at 26 Jul 2026 (vs $160M at 25 Jan 2026). Deferred-revenue additions in 1H FY27 were $17.7B, including $15.6B of customer advances (same 10-Q). Group-level, not networking-specific.
- No labour-hour or per-seat dependence in networking. The software share of networking was not found.

**(d) Financial strength** (group; networking not broken out in the filings retrieved).
- Q2 FY27 (quarter to 26 Jul 2026; reported 26 Aug 2026):
  - Revenue $96.2B (+106% y/y); Data Center $89.0B (+117%).
  - GAAP gross margin 75.0%; operating income $63.7B (~66% margin, derived). Compute & Networking segment operating income $62.7B.
  - Networking: "another record quarter", +18% q/q; Spectrum-X +2.6x y/y — [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/08/31/nvidia-nvda-q2-2027-earnings-call-transcript/). Above $17.5B per [The Register](https://www.theregister.com/networks/2026/10/31/backbone-of-a-beast-charting-nvidias-rise-to-networking-titan/5306499), versus $7.252B in Q2 FY26 ([SEC 8-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581025000207/q2fy26cfocommentary.htm)). That is about +140% y/y and about 18% of group revenue (derived).
  - Balance sheet at 26 Jul 2026: cash $22.4B + marketable debt securities $34.1B (+ $42.8B equity securities); debt $33.4B after $25B of notes issued in Jun 2026. Net cash about $23B excluding equity stakes (derived).
  - Inventory $31.6B (from $25.8B) — [CFO commentary](https://www.marketscreener.com/news/nvidia-second-quarter-2027-cfo-commentary-ce7858d9d18df324).
  - Q3 guide $108B ±2%.
- Free cash flow and capex for the quarter: not retrieved (gap).
- Concentration (from the 10-Q text, retrieved directly from EDGAR):
  - Q2 FY27: one direct customer was 16% of total revenue. 1H FY27: three direct customers were 16%, 15% and 13%, all mainly Compute & Networking. Q2 FY26: two direct customers were 23% and 16%.
  - "One AI research and deployment company contributed a meaningful amount of our revenue by purchasing cloud services from our customers" (indirect).
  - Accounts receivable: five direct customers held 22/14/13/11/10% of AR.
  - Revenue mix: hyperscale about $49B (~55%) of $89B Data Center; "ACIE" including neoclouds about $40B — [transcript](https://www.fool.com/earnings/call-transcripts/2026/08/31/nvidia-nvda-q2-2027-earnings-call-transcript/).
- Geography (by direct-customer headquarters, Q2 FY27): United States $60.07B (62%); Taiwan $26.99B (28%); China incl. Hong Kong $7.88B (8%); other $1.28B. Revenue from customers headquartered outside the US was 38% of the total — [10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm). NVIDIA notes that end-customer and shipping locations can differ from customer headquarters.
- Return on capital (TTM, aggregator, secondary): ROIC ~92%, ROE ~117%; FCF ~$127B; net cash ~$23.6B — [stockanalysis.com, retrieved 12 Nov 2026](https://stockanalysis.com/stocks/nvda/statistics/).
- Return on capital: not computed (gap).

**(e) Resilience.**
- Cycle position: "we expect supply to remain a bottleneck, at least through the end of fiscal year '28" (Kress). Memory price rises "exceeded our prior expectations" — [transcript](https://www.fool.com/earnings/call-transcripts/2026/08/31/nvidia-nvda-q2-2027-earnings-call-transcript/). Huang at GTC Berlin: "Capacity is the constraint" — [SDxCentral](https://www.sdxcentral.com/news/nvidia-targets-15x-optics-capacity-expansion-by-2027-to-meet-cpo-demand/).
- Pause exposure: $279B of commitments and $2.1B already accrued for excess-inventory purchase obligations ([10-Q](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000075/nvda-20260726.htm)). Neocloud buyers are "the most cash-strapped" (SimpleTechTrend commentary on Huang's Berlin remarks; secondary).
- NVIDIA's own financing-risk disclosure (10-Q, Aug 2026): "AI clouds and AI model makers ... currently lack the ability to secure long-term infrastructure contracts and investment-grade financing capacity", which "could delay customer and partner deployments". NVIDIA is "securing and providing guarantees of land, power, shell, and capacity of select data center infrastructure that customers require". This is direct evidence for the financing-led-pause mechanism in the brief's scenarios.
- Export controls: the outlook assumes no China Data Center compute revenue; China Hopper shipments were below 1% of Data Center revenue in Q2 — [CFO commentary](https://www.marketscreener.com/news/nvidia-second-quarter-2027-cfo-commentary-ce7858d9d18df324).
- Scenarios (inference): steady growth — networking compounds with the CPO ramp. Financing-led pause around 2028 — prepayments and commitments become fixed costs and neocloud demand is most at risk, but net cash and a 75% gross margin absorb it. Acceleration — the SPIL, KYEC and Corning capacity locks become the advantage.

### 2.2 Broadcom — switching, CPO and optical components (weight: AI semis 56% of group revenue; networking not separately disclosed)

**Takeaway.** Broadcom is the merchant CPO pioneer. It has three generations of CPO, a Meta-published lab reliability result and a 200T switch already taped out. For processor-to-processor (scale-up) links it is deliberately copper-first. Cash generation is very strong, but leverage is material.

**(a) Position.**
- Owns CPO process know-how across three generations: TH5-Bailly, TH6-Davisson, and Humboldt from earlier reporting. The optical engines rely on TSMC's COUPE, which Broadcom does not own — [ServeTheHome, 12 Oct 2025](https://www.servethehome.com/broadcom-tomahawk-6-davisson-102-4t-switch-with-co-packaged-optics-shipping/).
- Self-described "de facto standard in the industry for CPO components", including 1.6T DSPs and CW/EML lasers (Q2 FY26 call, 3 Jun 2026, via search summary; company claim, unconfirmed).
- Products:
  - Tomahawk 6 with pluggables: BRIDGE.
  - TH6-Davisson BCM78919: SUCCESSOR. Broadcom said "now shipping" (8-12 Oct 2025); other outlets said sampling to early-access customers — [StorageReview](https://www.storagereview.com/news/broadcom-ships-tomahawk-6-davisson-cpo-ethernet-switch-doubling-bandwidth-to-102-4-tb-s-for-ai-fabrics); [STORDIS](https://stordis.com/broadcom-tomahawk-6-vs-th6-davisson/). Downstream systems: Micas 1RU Davisson box Q1 2027.
  - Tomahawk 7 (200T): taped out by Sep 2026 (Q3 FY26 call, via search summary).
  - Copper-based scale-up Ethernet (direct-attach copper on 200G/400G SerDes): BRIDGE for transition (1).

**(b) Lead (outside evidence).**
- Meta's ECOC 2025 paper (S. Amiralizadeh): about 1 million cumulative 400G-equivalent port device-hours with zero link flaps on Bailly in Meta's lab, high-temperature characterisation; 65% lower power per 100G lane versus retimed pluggables; described as "the highest device hours reported for CPO technology operation at the system level" — [NextPlatform, 17 Oct 2025](https://www.nextplatform.com/connect/2025/10/17/the-third-time-will-be-the-charm-for-broadcom-switch-co-packaged-optics/1635588); [Broadcom release, 1 Oct 2025](https://www.globenewswire.com/news-release/2025/10/01/3159570/19933/en/broadcom-showcases-industry-leading-quality-and-reliability-of-co-packaged-optics.html).
- Caveat: lab data, not field fleet data. No LPO comparison.
- Third-party merchant-switch market share: not retrieved (gap).

**(c) Revenue model.**
- Semiconductors are hardware ($20.8B, 70% of Q3 FY26 revenue). Infrastructure software ($8.8B, 30%) is largely recurring VMware, but sits outside this segment — [8-K, quarter to 2 Aug 2026](https://www.sec.gov/Archives/edgar/data/0001730168/000173016826000076/avgo-08022026x8kxex99.htm).

**(d) Financial strength.**
- Q3 FY26 (quarter to 2 Aug 2026; reported 2 Sep 2026):
  - Revenue $29.6B (+86%); AI semis $16.7B (+221% y/y, +54% q/q).
  - GAAP gross margin ~69.1% (derived); GAAP operating income $16.0B (~54%, derived).
  - Operating cash flow $14.2B; capex $0.5B; FCF $13.7B (46% of revenue).
  - Cash $24.0B; debt ~$59.4B, so net debt ~$35B (derived).
  - Q4 guide: revenue $34.8B, AI $21.7B (+236%); non-GAAP operating margin ~66% — [8-K](https://www.sec.gov/Archives/edgar/data/0001730168/000173016826000076/avgo-08022026x8kxex99.htm).
- Concentration (10-Q for quarter to 2 Aug 2026 and FY25 10-K, from EDGAR):
  - Top five end customers through all channels about 50% of net revenue in the nine months to 2 Aug 2026 (about 40% in FY2025 and FY2024). Concentration is rising with the AI ramp.
  - Distributors 56% of net revenue (48% in FY2025).
  - About 58% of contract liabilities relate to contracts with termination-for-convenience provisions — [10-Q](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm); [10-K FY25](https://www.sec.gov/Archives/edgar/data/1730168/000173016825000121/avgo-20251102.htm).
- Geography (revenue by region, Q3 FY26): Asia Pacific $20.94B (71%), Americas $5.51B, EMEA $3.13B. Products revenue in APAC $20.2B, reflecting Asian contract manufacturers and ODMs (10-Q).
- Return on capital (TTM, aggregator, secondary): ROIC ~30.7%, ROE ~44%, ROCE ~26%; net debt ~$35.4B — [stockanalysis.com, retrieved 12 Nov 2026](https://stockanalysis.com/stocks/avgo/statistics/).
- Networking share of AI revenue: not retrieved (gap).

**(e) Resilience.**
- Very high FCF conversion and an asset-light model cushion a pause. Leverage and dependence on a handful of XPU customers are the exposures (concentration not quantified here).
- A copper-first scale-up stance protects near-term revenue if optical scale-up slips. The risk is that Broadcom is late if optical scale-up arrives in 2027-28 (inference).

### 2.3 Arista Networks

**Takeaway.** Best-in-class margins and zero debt. Its strategy is explicitly bridge-side: pluggables, LPO and the new XPO form factor, with "open CPO" only in 2028-30. It owns no physical constraint and depends on merchant silicon and on two cloud titans.

**(a) Position.**
- No owned constraint or judge. Its edge is EOS software and long qualification at cloud titans.
- Products:
  - Pluggable-optics switches: BRIDGE, extended deliberately via LPO.
  - XPO (12.8 Tbps liquid-cooled pluggable; 204.8 Tbps per OCP rack unit; MSA formed 12 Mar 2026): bridge extension.
  - Open CPO with socketed engines: SUCCESSOR, guided to "'28 to '30" and "not imminent".
  - Etherlink SU-144 Ethernet scale-up (up to 144 XPUs per rack, 1,024 across racks; announced 7 Oct 2026 with AMD, Arm, Broadcom, d-Matrix, Meta, Microsoft, Qualcomm): trials 2027, production 2028.
  - Sources: [Arista XPO release](https://investors.arista.com/feed/PressRelease.svc/GetPressReleaseList?LanguageId=1&bodyType=1&pressReleaseDateFilter=3&pageSize=200&pageNumber=0&year=2026); [Q3 2026 call, 3 Nov 2026](https://www.fool.com/earnings/call-transcripts/2026/11/04/arista-anet-q3-2026-earnings-call-transcript/).
- Ullal: "We don't want to build proprietary co-packaged optics" ... "long live pluggable optics" (Q3 2026 call).

**(b) Lead (outside evidence).**
- Microsoft (Matthew Mattina) and Dell'Oro (Sameh Boujelbene) endorse XPO; Dell'Oro says it is "supported by all major optical module suppliers" (in Arista's release).
- Microsoft and Meta ("M&M") are each above 10% of revenue, and Arista expects "at least 1, maybe 2" more 10% customers (Q3 call).
- Third-party Ethernet-switch share for 2026: not retrieved (gap).

**(c) Revenue model.**
- Q3 2026 product $3.19B (+66.9%); services $467.6M (+17.9%), about 13% of revenue and recurring (derived) — [Q3 release](https://s21.q4cdn.com/861911615/files/doc_news/Arista-Networks-Inc--Reports-Third-Quarter-2026-Financial-Results-2026.pdf).
- Deferred revenue about $6.8B (call).

**(d) Financial strength.**
- Q3 2026 (quarter to 30 Sep; reported 3 Nov 2026):
  - Revenue $3.658B (+58.5% y/y, +20.5% q/q).
  - Gross margin GAAP 63.6% / non-GAAP 64.0%; operating margin GAAP 44.9% / non-GAAP 49.1%.
  - Operating cash flow about $1.2B; cash and marketable securities about $14.4B; zero debt.
  - Purchase commitments $11.4B (from $9.7B); inventory $3.2B (from $2.5B).
- Guidance: FY26 about $13.3B (+48%); FY27 +38-40% (~$18.5B); FY27 gross margin 62-64%. AI fabrics target $3.5B in 2026, about $7B in 2027 — [release](https://s21.q4cdn.com/861911615/files/doc_news/Arista-Networks-Inc--Reports-Third-Quarter-2026-Financial-Results-2026.pdf); [call](https://www.fool.com/earnings/call-transcripts/2026/11/04/arista-anet-q3-2026-earnings-call-transcript/).
- Concentration (FY2025 10-K): two end customers were 26% and 16% of FY2025 revenue (20%/15% in 2024; 18%/21% in 2023). The call calls them "M&M", i.e. Microsoft and Meta — [10-K](https://www.sec.gov/Archives/edgar/data/1596532/000159653226000013/anet-20251231.htm).
- Geography (Q3 2026, by shipping address): Americas $2.975B (81%; US $2.956B), EMEA $381M, APAC $301M — [10-Q](https://www.sec.gov/Archives/edgar/data/1596532/000159653226000254/anet-20260930.htm).
- Return on capital (TTM, aggregator, secondary): ROE ~33.5%, ROCE ~28.1%. The aggregator's ROIC (~240%) is an artefact of Arista's large net cash and small invested capital; do not use it — [stockanalysis.com](https://stockanalysis.com/stocks/anet/statistics/).

**(e) Resilience.**
- Visibility is about two quarters. Supply is constrained "industry-wide", and Arista is signing long-term deals for silicon, PCB and memory; product cost inflation partly offset margin (call).
- No tariff comments found.
- In a pause, the net cash cushions it, but $11.4B of purchase commitments and the concentration in two buyers are exposures (inference).

### 2.4 Corning (Optical Communications)

**Takeaway.** Corning owns a real physical constraint — fibre glass know-how and draw and cable capacity — and is getting customers to fund its expansion. Its demand rises with both transitions: about 16 fibres per GPU today, about 160 with optical scale-up.

**(a) Position.**
- Physical constraint plus process know-how. Meta, under a deal worth up to $6B (27 Jan 2026), is the anchor customer of a new Hickory, NC cable plant (construction from 31 Mar 2026). NVIDIA partnership (6 May 2026): 10x US optical-connectivity capacity, >50% more US fibre capacity, three new plants in North Carolina and Texas — Corning IR feed: [Meta](https://investor.corning.com/news-and-events/news/news-details/2026/Corning-and-Meta-Announce-Multiyear-up-to-6-Billion-Agreement-to-Accelerate-US-Data-Center-Buildout/default.aspx); [NVIDIA](https://investor.corning.com/news-and-events/news/news-details/2026/NVIDIA-and-Corning-Announce-Long-Term-Partnership-To-Strengthen-U-S--Manufacturing-for-AI-Infrastructure/default.aspx).
- Products: fibre, cable and connectivity (SUCCESSOR-aligned). Multicore fibre (4x capacity per fibre in a 125-micron cladding; claimed up to 75% fewer connectors — company claim, unconfirmed). Contour Flow 1,728-fibre micro cable. "Co-packaged optics systems" for scale-out and "eventually scale-up". PRIZM TMT expanded-beam ferrules licensed from US Conec (11 Mar 2026) — [Corning IR feed](https://investor.corning.com/feed/PressRelease.svc/GetPressReleaseList?LanguageId=1&bodyType=1&pressReleaseDateFilter=3&pageSize=60&pageNumber=0&year=2026).

**(b) Lead (outside evidence).**
- Named contracts with Meta and NVIDIA are third-party confirmation of qualification.
- Gen AI product sales grew more than 100% y/y, "significantly outpacing GPU unit growth" (company statement) — [Q3 call, 27 Oct 2026](https://www.fool.com/earnings/call-transcripts/2026/10/27/corning-glw-q3-2026-earnings-call-transcript/).
- Third-party fibre share: not retrieved (gap).

**(c) Revenue model.**
- Hardware/materials, but increasingly under long-term agreements with upfront customer cash. Weeks: customers "provide upfront cash to fund our capacity". Customer deposits were $639M in 9M 2026.
- LTAs announced in Q3 2026 with Zayo, Verizon and AT&T (carriers) — [call](https://www.fool.com/earnings/call-transcripts/2026/10/27/corning-glw-q3-2026-earnings-call-transcript/).

**(d) Financial strength.**
- Q3 2026 (reported 27 Oct 2026):
  - Optical Communications $2.38B (+44% y/y; Q2 $2.072B); segment net income $532M (+80%; ~22% margin, derived); Enterprise +84%.
  - Core sales $5.08B (+19%); core operating margin 22.7%.
  - Adjusted FCF $661M (9M about $2.3B); 2026 capex about $2B (9M $1.3B).
  - Average debt maturity >20 years; net debt not disclosed on the call — [8-K](https://www.sec.gov/Archives/edgar/data/0000024741/000002474126000273/glw-20261027xex99xq32026.htm); [call](https://www.fool.com/earnings/call-transcripts/2026/10/27/corning-glw-q3-2026-earnings-call-transcript/).
- Springboard targets: annualised sales run-rate $20B by end-2026, $30B by end-2028, $40B by end-2030.
- Return on capital (TTM, aggregator, secondary): ROIC ~12.1%, ROE ~17.9%, ROCE ~10.8%; net debt ~$6.6B (fills the "net debt not disclosed" gap) — [stockanalysis.com, retrieved 12 Nov 2026](https://stockanalysis.com/stocks/glw/statistics/). This is the weakest return profile among the key companies after Marvell.
- Customer percentages: not disclosed. Weeks: "Our customers are primarily the major hyperscalers."

**(e) Resilience.**
- Capacity is growing ahead of demand ($2B capex). Prepayments and LTAs cushion it.
- Chinese fibre is "not ... a significant competitive pressure" for now (Weeks).
- US-based manufacturing fits tariff and "Made in America" policies (NVIDIA release language).
- Inference: Corning is the most exposed of the key companies to a 2028 financing pause because of fixed capacity, but the most leveraged to the optical-scale-up upside.

### 2.5 Amphenol (copper and fibre interconnect, incl. ex-CommScope CCS)

**Takeaway.** Amphenol straddles the copper bridge and the fibre successor. It has excellent margins and cash generation and has added a fibre-connectivity franchise (CCS) that is running ahead of plan.

**(a) Position.**
- Manufacturing scale (facilities in about 40 countries) and design-in across IT datacom. No owned judge.
- Copper high-speed interconnect for scale-up is BRIDGE. Fibre connectivity (CCS) is successor-aligned — [CCS close release, 12 Jan 2026](https://s21.q4cdn.com/564806605/files/doc_news/2026/Jan/12/2026_01_12-PR-Closes-acq-of-CCS.pdf).
- Amphenol's specific NVLink copper content was not verified in this run (gap).

**(b) Lead.** Communications Solutions grew +51% organically in Q3 2026. CCS full-year 2026 sales expectation was raised from $4.1B (at close) to $4.6B and then $5.1B — [Q3 release, 28 Oct 2026](https://s21.q4cdn.com/564806605/files/doc_financials/2026/q3/2026_10_28-PR-3Q-2026-Results_Dividend-Increase-and-Buyback.pdf). Third-party share: not retrieved.

**(c) Revenue model.** One-off hardware, diversified across end markets. No recurring element found.

**(d) Financial strength.**
- Q3 2026 (quarter to 30 Sep; reported 28 Oct 2026):
  - Sales $10.23B (+65% USD, +37% organic); orders $12.2B (book-to-bill 1.19).
  - GAAP / adjusted operating margin 29.5% / 29.7%; operating cash flow $2.1B, FCF $1.6B.
  - Communications Solutions $6.583B (+99%, +51% organic), segment operating margin 33.1%.
  - Cash and short-term investments $5.30B; debt $17.87B, so net debt about $12.6B (derived).
  - FY26 guide $36.9-37.1B (about +60%) — [Q3 release](https://s21.q4cdn.com/564806605/files/doc_financials/2026/q3/2026_10_28-PR-3Q-2026-Results_Dividend-Increase-and-Buyback.pdf).
- Return on capital (TTM, aggregator, secondary): ROIC ~22.7%, ROE ~40%, ROCE ~25.7%; net debt ~$12.6B (matches the derived figure) — [stockanalysis.com](https://stockanalysis.com/stocks/aph/statistics/).

**(e) Resilience.** Diversified end markets and a book-to-bill of 1.19 at the top of the cycle. Exposed to a copper-content decline when scale-up goes optical, partly hedged by CCS fibre (inference).

### 2.6 Marvell (incl. Celestial AI; pending Lumentum)

**Takeaway.** Marvell is the most aggressive successor-side consolidator. But its scale-up optics revenue is "virtually zero today", GAAP margins are modest, concentration is high, and the transformative Lumentum deal does not close until 1H 2028.

**(a) Position.**
- IP owner (SerDes, PAM4 DSPs, Photonic Fabric). With Lumentum it would gain indium-phosphide (InP) laser fabs, a physical constraint — [8-K/425, 1-2 Nov 2026](https://www.sec.gov/Archives/edgar/data/0001835632/000119312526442723/d81187d425.htm).
- Products:
  - Pluggable DSPs ("electro-optics"; ~$1.4B in Q2 FY27 per a NextPlatform author estimate, secondary): BRIDGE.
  - Celestial AI Photonic Fabric, "Fast Pipe" and "Flat Pipe" light engines: SUCCESSOR. "Multi-hundred-million-dollar" scale-up optics revenue is guided from next year (2027) — [Futurum, 9 Oct 2026](https://futurumgroup.com/insights/marvell-investor-day-2026-targets-80b-fy-2031-revenue-with-custom-silicon-and-optics/). An analyst estimates Celestial hardware at about $150M in FY28 — [NextPlatform, 2 Sep 2026](https://www.nextplatform.com/connect/2026/09/02/optics-still-driving-marvells-ai-business-more-than-custom-chips/5294018) (secondary).
  - Teralynx T100 102.4T switch. UALink U115 switch expected in CY2027 (a Futurum watch item).

**(b) Lead.** Management says demand for Celestial CPO and NPO "exceeded expectations" (Q2 call, via search summary; company claim, unconfirmed). No named Celestial customer and no third-party share found.

**(c) Revenue model.** Hardware plus custom-silicon programmes (including a Google warrant agreement per Futurum). Earnout payments to Celestial's former owners depend on revenue milestones through FY2029 ([10-K](https://www.sec.gov/Archives/edgar/data/1835632/000183563226000011/mrvl-20260131.htm)).

**(d) Financial strength.**
- Q2 FY27 (quarter to 1 Aug 2026; reported 27 Aug 2026):
  - Revenue $2.739B (+37%); Data Center $2.172B (79%).
  - Gross margin GAAP 53.1% / non-GAAP 58.9%; operating margin GAAP 16.8% / non-GAAP 36.6%.
  - Operating cash flow $605.5M; capex $126.7M.
  - Cash $3.93B; long-term debt $4.96B, so net debt about $1.0B (derived) — [8-K](https://www.sec.gov/Archives/edgar/data/0001835632/000183563226000022/q227_8kx812026ex-991.htm).
- FY26 (to 31 Jan 2026): revenue $8.19B (+42%). Concentration: Distributor A 37%, Customer A 14%. About 77% of revenue shipped to customers with operations in Asia — [10-K](https://www.sec.gov/Archives/edgar/data/1835632/000183563226000011/mrvl-20260131.htm).
- Targets: FY28 about $20B; FY31 $70-90B (Investor Day, 6 Oct 2026; company targets).
- Return on capital (TTM, aggregator, secondary): ROIC ~6.9%, ROE ~16.5%, ROCE ~6.3% (GAAP returns depressed by acquisition amortisation); net debt ~$1.35B — [stockanalysis.com](https://stockanalysis.com/stocks/mrvl/statistics/).
- Lumentum pro forma: annualised revenue about $17.7B, non-GAAP gross margin 57%, operating margin 39%, ">$1B" cost synergies; close expected 1H CY2028 — [8-K/425](https://www.sec.gov/Archives/edgar/data/0001835632/000119312526442723/d81187d425.htm).

**(e) Resilience.**
- The Lumentum deal is all-stock, so it is not leveraging the balance sheet. But it closes into the window the brief gives for a possible financing-led pause, and it needs regulatory approvals that the filing does not name. A China review is a plausible risk given 77% Asia exposure (inference).
- The 10-K flags export-licence and China-substitution risk.

### 2.7 Brief financial profiles of other named companies
- **Cisco** — Q4 FY26 (quarter to Jul 2026; reported 12 Aug 2026):
  - Revenue $17.3B (+18%); product orders +35% (networking +40%); non-GAAP operating margin 35.9%; RPO $46.7B.
  - Hyperscale AI-infrastructure orders $4B in the quarter and $9.3B for FY26; AI-infrastructure revenue about $4B in FY26, expected $7.5B in FY27.
  - FY27 guide $72.2-73.4B — [unite.ai, 12 Aug 2026](https://www.unite.ai/cisco-books-4b-in-quarterly-ai-orders-as-networking-supercycle-lifts-fy2027-outlook/) (secondary).
  - Q1 FY27 results were not yet published or indexed as of the research date.
  - FY26 10-K (FY to 25 Jul 2026; filed 2 Sep 2026): revenue $63.3B (+12%); Americas 59.7%, EMEA 26.2%, APJC 14.1%. Operating cash flow $14.2B; capex $1.4B; cash and investments $15.9B; total debt $29.5B ($23.0B notes + $6.7B commercial paper); inventories $5.69B (from $3.16B); RPO $46.7B.
  - Total gross margin fell 0.4 pp on product mix and "higher memory costs". The 10-K warns that AI-infrastructure sales to hyperscalers "may be concentrated among a limited number of customers" — [10-K](https://www.sec.gov/Archives/edgar/data/858877/000085887726000132/csco-20260725.htm).
  - TTM (aggregator, secondary): ROIC ~20.4%, ROE ~27.3%, FCF ~$12.8B, net debt ~$15.3B — [stockanalysis.com](https://stockanalysis.com/stocks/csco/statistics/).
  - CPO: G300 systems ship with pluggable 1.6T OSFP and 800G LPO. Chopra: "We certainly have the technology, we're looking for business alignment to sort of productize it" — [The Register, 10 Feb 2026](https://www.theregister.com/2026/02/10/cisco_challenges_broadcom_nvidia_switch_chips/).
- **Celestica** — Q3 2026 (release 26 Oct 2026):
  - Revenue $5.83B (+83%); CCS $4.87B (+102%; 84% of revenue; segment margin 8.9%); HPS about $2.3B (+70%); adjusted operating margin 8.5%.
  - FCF $127.5M; capex $274M; cash $3.96B against debt $819M.
  - FY26 FCF guide cut to $460M (from $600M) for working capital. 2027 outlook: revenue $40B (+90%), adjusted operating margin 9.0%, capex $1.5-2.0B — [Celestica release](https://finviz.com/news/408117/celestica-announces-third-quarter-2026-financial-results-and-will-hold-2026-investor-and-analyst-day).
  - Concentration (Q3 2026 10-Q, primary): three CCS customers were 35%, 17% and 14% of Q3 2026 revenue (66% combined; YTD 34/16/15). Top-10 customers were 85% of Q3 revenue (80% a year earlier). Its A/R sales programme was raised to $1.0B (from $450M) in Sep 2026, a working-capital financing signal — [10-Q](https://www.sec.gov/Archives/edgar/data/1030894/000103089426000050/cls-20260930.htm). This supersedes the earlier "three buyers = 63%" analyst estimate.
  - 1.6T revenue is expected to pass 800G in 2027. DS6005 CPO switch announced 12 Oct 2026.
  - TTM (aggregator, secondary): ROIC ~41.9%, ROE ~30.2%, ROCE ~20.6%; gross margin ~11.5% — [stockanalysis.com](https://stockanalysis.com/stocks/cls/statistics/).
- **Accton** — Q3 2026 consolidated revenue NT$120.74B (+26.4% q/q, +65.5% y/y, record); 9M NT$286.40B (+62.45%) (Money Weekly, via search summary; secondary).
  - Q2 2026 NT$95.54B (+58% y/y) — [Taiwan News](https://www.taiwannews.com.tw/news/6396424); August 2026 NT$40.873B, a monthly record — [Digitimes tag page](https://www.digitimes.com/tag/accton/001693.html).
  - Q3 2026 gross margin and EPS NOT found. Reference point: Q3 2025 EPS NT$14 and gross margin 17.1% — [StatementDog, 28 Nov 2025](https://statementdog.com/news/15154). Expanding in Vietnam, Malaysia, Mexico and the US (same source).
- **Credo** — no FY27 Q1 financials retrieved. Strategy is vertical (SerDes + DSP + SiPh via DustPhotonics + microLED via Hyperlume). Expects its optical portfolio to be "a significant growth driver in fiscal 2027" (company claim, unconfirmed) — [Credo IR feed](https://investors.credosemi.com/feed/PressRelease.svc/GetPressReleaseList?LanguageId=1&bodyType=1&pressReleaseDateFilter=3&pageSize=200&pageNumber=0&year=2026).
- **Ciena** — FY29 targets (16 Sep 2026): ~30% revenue CAGR 2026-29, ~50% gross margin, 32-35% operating margin, ~20% FCF margin. New "Interconnects" reporting segment from FY27 — [Ciena IR feed](https://investor.ciena.com/feed/PressRelease.svc/GetPressReleaseList?LanguageId=1&bodyType=1&pressReleaseDateFilter=3&pageSize=200&pageNumber=0&year=2026).

### 2.7b Fujikura (added as a seventh key company) and the other Japanese fibre makers — primary TDnet filings (Japanese-language)

**Takeaway.** Fujikura is the purest listed AI-fibre profit story found. Its Information & Communications segment margin (~37%) is well above Corning's optical segment net margin (~22%), and it has net cash. Customer concentration and the product-level CPO roadmap are unverified.

- **(a) Position.**
  - Physical constraint and process know-how in fibre, high-density cable and optical components (successor-aligned for transitions 1 and 2).
  - The company says demand came from "expanding data-centre investment", and that it also won optical-component orders by meeting short lead times ("短納期対応により受注した光コンポーネント製品等") — H1 FY26 決算短信, 10 Nov 2026, https://www.release.tdnet.info/inbs/140120261109569418.pdf.
  - Portfolio pruning: selling its 60.8% stake in power-cable maker Nishi Nippon Electric Wire to an Aspirant Group fund (TDnet, 5 Nov 2026, https://www.release.tdnet.info/inbs/140120261105565331.pdf).
- **(b) Lead.** Segment sales +91.6% and operating profit +194.8% y/y (H1 FY26). Third-party share and named customers: not retrieved (gap).
- **(c) Revenue model.** One-off hardware; no LTA or prepayment disclosure found.
- **(d) Financial strength.**
  - H1 FY26 (Apr-Sep 2026; released 10 Nov 2026): group net sales ¥867.4B (+55.2%); operating profit ¥235.0B (+160.6%; ~27% margin); net income ¥180.3B (+168.5%); total assets ¥1,171.6B; equity ratio 59.2%.
  - FY26 guide (revised 10 Nov 2026): sales ¥1,768B (from ¥1,755B), operating profit ¥429B (from ¥432B; trimmed for a stronger yen, now ¥156/USD vs ¥160), net income ¥326B. FY25 actual: sales ¥1,182.4B, operating profit ¥188.7B — https://www.release.tdnet.info/inbs/140120261109570131.pdf.
  - TTM (aggregator, secondary): ROIC ~44.8%, ROE ~45.1%, ROCE ~41.0%, FCF ~¥181B, net cash ~¥137B — https://stockanalysis.com/quote/tyo/5803/statistics/.
- **(e) Resilience.** Yen sensitivity is explicit. Customer and country concentration is not disclosed in the 決算短信 (gap). Fibre has historically been cyclical (inference).
- **Path / verdict:** a beneficiary of copper-to-optical (more fibre per GPU), like Corning. No CPO-specific product evidence was retrieved. **Suggested verdict: COHERENT on financial evidence; path evidence thin.**
- **Sumitomo Electric** (H1 FY26 released 30 Oct 2026):
  - Group sales ¥2,764.9B (+16.5%), operating profit ¥219.6B (+43.5%), both records. Info & Comms sales ¥201.5B (+48.8%), operating profit ¥61.2B (up ¥39.2B), driven by "data-centre optical wiring products, optical devices" — https://www.release.tdnet.info/inbs/140120261029559548.pdf.
  - TTM ROIC ~11%, net debt ~¥481B (aggregator, secondary). AI fibre is a small part of a diversified group.
- **Furukawa Electric** (H1 FY26 released 9 Nov 2026):
  - Group sales ¥737.7B (+20.8%), operating profit ¥57.6B (+201%). Optical Solutions sales ¥130.9B (+43.9%), operating profit ¥23.6B (up ¥22.9B); Information Components ¥118.9B (+23.2%), operating profit ¥15.2B — https://www.release.tdnet.info/inbs/140120261106567992.pdf.
  - FY26 guide raised (9 Nov 2026) to sales ¥1,570B and operating profit ¥136B (from ¥1,530B / ¥123B; FY25 actual ¥1,307.6B / ¥63.9B), "mainly due to increased demand for data-centre-related products" — https://www.release.tdnet.info/inbs/140120261106568021.pdf.
  - TTM ROIC ~10%, FCF negative, net debt ~¥254B (aggregator, secondary).

### 2.8 Return-on-capital summary (TTM to latest reported quarter; stockanalysis.com statistics pages retrieved 12 Nov 2026; aggregator methodology, secondary; valuation fields deliberately ignored)

| Company | ROIC | ROE | ROCE | Net cash (+) / net debt (-) |
|---|---|---|---|---|
| NVIDIA | ~92% | ~117% | ~71% | +$23.6B |
| Broadcom | ~30.7% | ~44% | ~26% | -$35.4B |
| Arista | n/m (artefact ~240%) | ~33.5% | ~28.1% | +$14.4B |
| Amphenol | ~22.7% | ~40% | ~25.7% | -$12.6B |
| Cisco | ~20.4% | ~27.3% | ~18.3% | -$15.3B |
| Celestica | ~41.9% | ~30.2% | ~20.6% | +$2.9B |
| Corning | ~12.1% | ~17.9% | ~10.8% | -$6.6B |
| Fujikura | ~44.8% | ~45.1% | ~41.0% | +¥137B |
| Sumitomo Electric | ~11.0% | ~16.2% | ~13.4% | -¥481B |
| Furukawa Electric | ~10.1% | ~28.5% | ~15.1% | -¥254B |
| Marvell | ~6.9% | ~16.5% | ~6.3% | -$1.35B |

### Gaps (section 2)
- NVIDIA's FCF and capex for the quarter, from the primary cash-flow statement (the aggregator gives TTM FCF of ~$127B).
- Amphenol's 10%-customer list (none found; diversified).
- Broadcom's networking share of AI revenue.
- Third-party market shares: Dell'Oro and 650 Group 2026 switch shares, and fibre/connector shares.

---

## 3. Path-forward evidence and suggested verdicts

The transitions are numbered as in the brief: (1) copper to optical between processors; (2) pluggables to CPO; (3) hybrid bonding; (4) panel and glass packaging; (5) two-phase cooling; (6) 600 kW-1 MW racks on 800 VDC. Note: TSMC's COUPE photonic engines use SoIC-X die stacking ([TechTimes](https://www.techtimes.com/articles/329352/20261022/nvidia-locks-ai-chip-testing-optics-capacity-six-partner-prepayment-push.htm), secondary), so CPO adopters are tied to transition (3) through TSMC.

### NVIDIA networking
- **Must pass:** (1), (2), (3) via COUPE, (5) (its CPO switches are liquid-cooled), (6).
- **SAID:**
  - CPO scale-out from 2026.
  - Spectrum-6 CPO for Vera Rubin.
  - SPIL optical-engine capacity 15x by mid-2027 and about 30x by end-2028.
  - CPO NVLink switch for multi-rack NVL576 (Counterpoint, secondary).
  - Feynman (2028) "all CPO" NVL1152 (SemiAnalysis, secondary).
  - OOI for post-2028.
- **DONE:**
  - Quantum-X Photonics in production at Lambda (Jun 2026).
  - Spectrum-X Photonics shipping to select partners (2026).
  - Vera Rubin production shipments began in Aug 2026 ([transcript](https://www.fool.com/earnings/call-transcripts/2026/08/31/nvidia-nvda-q2-2027-earnings-call-transcript/)).
  - Prepayments: KYEC $1.1B, Amkor $1.5B.
  - Corning 10x connectivity partnership.
  - OCI MSA founding member (OFC 2026).
  - $2B Lumentum agreement (Counterpoint, secondary).
- **Funded:** yes, from operating cash.
- **Timing and slips:** Spectrum-X Photonics slipped from "2025" to 2026. The NVLink 8 path (CPO electrical switch vs optical circuit switching vs hybrid) is "unclear" (Counterpoint).
- **What must go right:** SPIL yields at 15x; laser supply (InP); fibre-attach and test throughput; customers accepting CPO serviceability.
- **Verdict: COHERENT.** It has shipped successor products, has customers in production and has funded capacity. The residual risk is execution on the 2027-28 scale-up timing.

### Broadcom
- **Must pass:** (1), (2), (3) via COUPE.
- **SAID:** CPO component leadership; copper-first scale-up; Tomahawk 7.
- **DONE:**
  - Bailly with Meta lab data.
  - Davisson "shipping" (Oct 2025), with ecosystem systems (Micas, Q1 2027).
  - TH7 taped out (Sep 2026).
- **Funded:** yes (FCF $13.7B/quarter).
- **Bridge-side test:** copper scale-up is the bridge. A credible successor exists for switches (Davisson). For optical scale-up, no Broadcom XPU-side optical product was found in this run.
- **Verdict: COHERENT for (2); PARTLY COHERENT for (1)** — it relies on copper lasting, which the evidence supports through 2027-28.

### Arista
- **Must pass:** (2), (1) for its scale-up entry, (5) (XPO cold plate up to 400W), (6).
- **SAID:** open CPO 2028-30; scale-up Ethernet trials 2027 and production 2028; "long live pluggable optics".
- **DONE:**
  - XPO MSA (Mar 2026), endorsed by Microsoft.
  - LPO products.
  - Etherlink SU-144 rack-scale platforms (Oct 2026) with AMD, Meta, Microsoft and others.
- **Funded:** yes ($14.4B cash, no debt).
- **Bridge-side test:** the successor (open CPO) is not yet shown as a product. Its credibility rests on the hyperscalers' preference for open, multi-vendor optics, which the XPO, OCI and SRMO MSAs show is real.
- **Timing:** plausible, and consistent with LightCounting's CPO/NPO volume from 2029.
- **What must go right:** pluggables and XPO stay competitive at 1.6T-3.2T; hyperscalers resist NVIDIA's proprietary CPO/NVLink stacks; merchant CPO (Broadcom) becomes "open".
- **Verdict: PARTLY COHERENT (leaning coherent).** The plan is internally consistent and funded, but the successor product is unproven and the company depends on others' silicon.

### Corning
- **Must pass:** a beneficiary of (1) and (2) rather than tested by them. Possibly (4) through glass, not researched here.
- **SAID:** optical scale-up accelerates in 2028; fibres per GPU go from about 16 to about 160; Springboard $30B run-rate by end-2028.
- **DONE:**
  - Meta deal up to $6B and Hickory plant under construction.
  - NVIDIA 10x partnership with three new plants.
  - US Conec licence.
  - Multicore fibre and CPO fibre systems at OFC 2026.
  - Customer deposits $639M.
- **Funded:** largely by customers plus operating cash.
- **Successor-side test:** it can fund a 1-2 year slip (operating cash; LTAs), but would carry under-used capacity (inference).
- **Verdict: COHERENT.**

### Amphenol
- **Must pass:** (1), where copper content is at risk and fibre content gains; (6) power interconnect, not researched.
- **SAID/DONE:** bought CCS ($5.1B FY26 sales expected, ahead of plan); Communications Solutions +51% organic; buying Dexgreen (FTTH fibre).
- **Funded:** yes (FCF $1.6B/quarter).
- **Verdict: COHERENT**, with the caveat that its exposure to NVLink copper content was not verified.

### Marvell
- **Must pass:** (1), (2), (3).
- **SAID:** scale-up optics multi-hundred-million revenue from 2027; FY28 about $20B; FY31 $70-90B.
- **DONE:**
  - Closed Celestial AI (about $1.3B cash + stock) and XConn (Feb 2026).
  - Agreed the Lumentum merger (Nov 2026).
  - Light-engine product lines named.
- **Funded:** the successor R&D yes (net debt about $1.0B; operating cash $605M/quarter). The big step (Lumentum) is stock-funded.
- **Slip test:** survivable financially, but the Celestial earnout and the merger synergies assume adoption in 2027-29.
- **Timing:** "100% of XPU-to-XPU links run on copper today" (Futurum's summary of Investor Day) versus revenue "next year" — ambitious.
- **Verdict: PARTLY COHERENT.** Committed capital is real; adoption and integration risks are high, and customer evidence for scale-up optics is not public.

---

## 4. Suggested ordering of key companies by quality alone (not valuation, not size)

Final suggested order (seven key companies):

1. **NVIDIA (networking)** — the highest margins of the group, net cash, a shipped successor and control of scarce capacity.
2. **Broadcom** — a NEAR-TIE with NVIDIA that I cannot cleanly separate. Broadcom leads on merchant CPO maturity and FCF conversion. NVIDIA leads on balance sheet (net cash vs Broadcom's net debt of about $35B), on a named production CPO deployment and on capacity control.
3. **Fujikura** (LOW-CONFIDENCE placement; added after the Japanese filings were retrieved). On returns (ROIC ~45%), net cash and Information & Communications margin (~37%) it beats everything below it and roughly matches Broadcom on returns. It is held back by unverified customer and country concentration, yen sensitivity, a history of cyclical fibre markets, and thin evidence on CPO-specific products.
4. **Arista**, 5. **Amphenol**, 6. **Corning** — a TIE CLUSTER I cannot separate with confidence:
   - Arista: best margins and no debt, but no owned constraint, bridge-side positioning and two-customer concentration.
   - Amphenol: strong margins (29.7%) and diversification; straddles copper and fibre.
   - Corning: owns the physical constraint and has customer-funded LTAs, but lower margins (core operating margin 22.7%) and capital intensity.
7. **Marvell** — successor-side and strategically bold, but GAAP operating margin of 16.8%, a 37% distributor concentration, scale-up optics revenue near zero, and large integration risk to 2028.

Fujikura and Corning are the two "physical constraint" fibre owners. Fujikura currently converts that position into far higher returns (ROIC ~45% vs ~12%). Corning has the stronger contracted demand (Meta up to $6B; NVIDIA partnership; customer deposits), while Fujikura's contracts were not found.

Return-on-capital cross-check (section 2.8, secondary TTM data): the ordering holds at the top (NVIDIA ROIC ~92% > Broadcom ~31%) and at the bottom (Marvell ~7%). Within the tie cluster, returns favour Arista (ROE ~34%, ROCE ~28%, net cash) and Amphenol (ROIC ~23%) over Corning (ROIC ~12%). If a strict order is needed, use Arista ≥ Amphenol > Corning, while noting that Corning alone owns a physical constraint (fibre capacity and glass know-how) and has customer-funded LTAs.

Concentration cross-check (primary filings): the most concentrated are Celestica (top-3 = 66% of Q3 2026 revenue; top-10 = 85%) and Arista (26% + 16% in FY25). Broadcom's top-5 end customers are ~50% of revenue (9M FY26). NVIDIA's largest direct customer is 16% (Q2 FY27). Marvell's Distributor A is 37% (FY26). Amphenol is diversified.

Outside the key set, indicative only: Cisco (cash-generative, ROIC ~20%, CPO laggard) would sit around Amphenol or Corning. Celestica (ROIC ~42% but an ODM with ~11% gross margin and very high concentration) and Accton (thin ODM margins) would sit below Marvell on quality as defined here, because they own neither a judge nor a constraint.

---

## 5. Check of the background priors

| Prior (mid-Nov 2026 analysis) | Verdict | Current evidence (dated) |
|---|---|---|
| CPO in network switches began shipping in 2026 | **UPDATED.** Merchant CPO shipped from late 2025; NVIDIA's from 2026; all at low volume | Broadcom said TH6-Davisson "now shipping" 8-12 Oct 2025 ([STH](https://www.servethehome.com/broadcom-tomahawk-6-davisson-102-4t-switch-with-co-packaged-optics-shipping/)). NVIDIA Quantum-X Photonics in production at Lambda Jun 2026; Spectrum-X Photonics to select partners in 2026, slipped from 2025. LightCounting calls 2026-27 a "validation phase", with volume from 2029 (OCP, Oct 2026, [secondary](https://www.simpletechtrend.com/en/post/ocp-2026-lightcounting-cpo-npo-forecast-scenarios-en)). |
| NVIDIA and its packaging partner plan a 15x rise in optical-engine capacity by mid-2027 | **CONFIRMED, with corrections** | Claim made by NVIDIA at GTC Berlin on 21 Oct 2026 ([SDxCentral](https://www.sdxcentral.com/news/nvidia-targets-15x-optics-capacity-expansion-by-2027-to-meet-cpo-demand/); [Taiwan News, 22 Oct 2026](https://www.taiwannews.com.tw/news/6463331)). The partner is SPIL (ASE group), not TSMC. The baseline is "today's level" (2026), with no absolute units disclosed. A further doubling (about 30x) is planned by end-2028. It is a capacity ceiling, not a demand forecast (SimpleTechTrend view). Digitimes (10 Nov 2026): "Nvidia, SPIL target CPO volume shipments in 2027" (paywalled). |
| Optical links between processors planned for 2028, may slip to 2028-29; copper stretched to 2027-28 | **CONFIRMED, with nuance** | First optical scale-up is cross-rack: a CPO NVLink switch for NVL576 pods in the Vera Rubin / Rubin Ultra era (2027; Counterpoint, secondary). Native CPO on the GPU arrives with Feynman in 2028; in-rack Kyber NVL144 stays copper-only (SemiAnalysis). Marvell: 100% copper today, scale-up optics revenue from 2027. Arista: scale-up trials 2027, production 2028. Corning: optical scale-up accelerates in 2028. LightCounting: scale-up is about one third of CPO/NPO volume in 2029 and 58% in 2031. Slip signals: Spectrum-X Photonics +6-12 months; NVLink 8 path "unclear"; OOI research-only (post-2028); Lightmatter CPO only in 2027 (company roadmap). |
| 70% that at least one of A16 / panel packaging / optics between processors misses 2028 volume | **Optics leg supports the prior (cannot assess A16 or panel here)** | For optics alone, "volume in 2028" conflicts with LightCounting (volume from 2029) and with NVIDIA's OOI (post-2028). NVIDIA's 2028 Feynman is a launch date, not a volume date. In my reading, the optics leg alone carries a high probability of missing 2028 volume (inference), consistent with a ≥70% combined prior. |
| Optical links a binding constraint in 2028-30; pluggables lose share 2028-30, but bridges last longer than roadmaps say | **CONFIRMED** | Constraint: transceiver demand was about 2x supply and InP lasers were the "critical bottleneck" (LightCounting, ECOC 2025, [EE Times](https://www.eetimes.com/ai-demand-reshapes-optical-connectivity-and-photonics-roadmaps/)). "Capacity is the constraint" (Huang, Oct 2026). Supply a bottleneck through FY28 (Kress, Aug 2026). Bridges: LightCounting 2031 — 89% of 800G and 43% of 1.6T ports still retimed pluggables (about 48% of all ports, weighted). Arista "long live pluggable optics" and the XPO MSA. Cisco shipping LPO and pluggables with no CPO commitment. |

Additional prior-relevant data: LightCounting's Ethernet-optics scenarios (OCP, Oct 2026) include a "Bumpy Ride" case — peak in 2027, trough in 2029 about 35% lower — which the presenter said "best fits history". It maps onto the brief's financing-led pause scenario ([SimpleTechTrend](https://www.simpletechtrend.com/en/post/ocp-2026-lightcounting-cpo-npo-forecast-scenarios-en), secondary).

---

## 6. Open question: which successor ships in volume first, and who captures the value

### Takeaway
CPO in scale-out switches ships in volume first: capacity in 2027, real volume in 2028-29. Optical scale-up follows, cross-rack in 2027 and on-package in 2028+, with volume most likely in 2029+. Near-packaged optics (NPO) and linear pluggables (LPO, XPO) will carry much of the volume in between. Value is moving to integrated giants and large incumbents: NVIDIA, Broadcom, TSMC/SPIL, Marvell-Lumentum and Corning-scale fibre suppliers. Specialist start-ups are being acquired rather than capturing value independently.

### Cited findings
- LightCounting CPO+NPO ports (chart readings, secondary): about 4.5M in 2027, about 16.5M in 2028, about 42M in 2029, about 91M in 2030, about 189M in 2031. NPO is roughly equal to CPO in each year — [SimpleTechTrend, 22 Oct 2026](https://www.simpletechtrend.com/en/post/ocp-2026-lightcounting-cpo-npo-forecast-scenarios-en).
- An earlier LightCounting figure was "close to 100 million" CPO ports and about $10B of CPO engines in 2030 — [LightCounting, Dec 2025](https://www.lightcounting.com/newsletter/en/december-2025-aocs-dacs-linear-drive-pluggable-and-co-packaged-optics-320). Whether the Oct 2026 numbers are a downgrade (about 47M CPO-only in 2030) or a definitional change cannot be resolved without the original slides.
- Kozlov expects transceivers' share of capex to fall from about 5% to 3.5-4% by 2029-30 (same source) — value leaves module makers.
- Vertical integration moves:
  - Marvell-Lumentum release: the industry is "shifting from discrete, modular components toward highly integrated optical solutions" ([8-K/425](https://www.sec.gov/Archives/edgar/data/0001835632/000119312526442723/d81187d425.htm)).
  - Credo calls itself a "vertically integrated connectivity stack" after DustPhotonics (May 2026).
  - Ciena bought Nubis (2025).
  - NVIDIA is building "an exclusive end-to-end optical ecosystem" (Counterpoint view, [2 Apr 2026](https://counterpointresearch.com/en/insights/from-blackwell-to-feynman-analyzing-nvidias-optics-roadmap)).
- Counterweights for specialists and open ecosystems: XPO MSA (Arista; Microsoft support); OCI MSA (NVIDIA a founding member); SRMO in OCP (Credo, with Senko, YOFC, AFL and others); Ciena's "open, multi-vendor" pluggable CPO engine (Feb 2026); Arista's open-CPO design with socketed engines and pigtail fibres.
- The passive-fibre content explosion goes to big incumbents. About 16 to about 160 fibres per GPU (Corning, 27 Oct 2026); "thousands of fibers per server rack and switch rack" (Corning, 11 Mar 2026). Supply is locked through Meta's $6B and NVIDIA's 10x deals with Corning, and through Amphenol's CCS.
- Bottlenecks:
  - Back-end optical-engine packaging (SPIL), test (KYEC) and InP lasers (LightCounting, 2025).
  - CPO and AI chips compete for the same advanced-packaging (2.5D/3D) capacity, and the SPIL deal does not solve this ([TechTimes](https://www.techtimes.com/articles/329352/20261022/nvidia-locks-ai-chip-testing-optics-capacity-six-partner-prepayment-push.htm), attributed to TrendForce; secondary).
  - Fibre-attach and fibre-array units are a likely bottleneck, but no 2026 source quantified it (gap). Detachable fibre-to-chip connectors are being consolidated (Teramount and TeraVERSE apparently to Molex; unconfirmed).

### Inferences
- Integrated giants capture the optical-engine and switch value. Fibre and connector incumbents capture the volume growth. Module makers and small specialists are squeezed or acquired. The main way specialists keep value is through open MSAs that hyperscalers back (XPO, OCI, SRMO).

---

## 7. What could not be verified

- NVIDIA's own GTC Berlin press release (Oct 2026). The 15x claim is sourced to trade press that cites it. Networking revenue in NVIDIA's own words (the $17.5B is The Register's figure; the 10-Q reports only the combined Compute & Networking segment). NVIDIA's concentration and geography are now verified from the 10-Q.
- Broadcom's networking share of AI revenue. The Q3 FY26 transcript was blocked or missing. Broadcom's concentration and geography are now verified from the 10-Q/10-K.
- Both leads passed on by the coordinator are now VERIFIED against primary sources:
  - Marvell-Lumentum: all-stock merger agreement (8-K/425; event 1 Nov 2026, signed 2 Nov 2026; close expected 1H CY2028).
  - Credo-DustPhotonics: closed 28 May 2026; upfront $750M cash + ~0.92M shares (release); total booked consideration $1.251B including $310M contingent (10-Q for quarter to 1 Aug 2026).
- Customer-published CPO reliability beyond the Meta/Broadcom lab result (no NVIDIA-CPO customer reliability data found). Field-fleet failure rates.
- Third-party CPO share-of-ports figures for 2026-2030 straight from LightCounting, Dell'Oro, 650 Group or Cignal AI publications. Only secondary chart readings were available.
- Chinese CPO switches: product status at Huawei, H3C, Ruijie and ZTE is still unverified, and Huawei is unlisted, so no filing exists. Q3 2026 headline financials for Unisplendour/H3C, Ruijie, ZTE, YOFC and T&S are now VERIFIED from cninfo filings. Chinese export-control specifics for switches and optics beyond NVIDIA's China exclusion remain unverified. Hollow-core fibre (Microsoft, YOFC). Multicore-fibre adoption beyond Corning's launch. VSFF (MMC, SN-MT) adoption shares.
- Japanese fibre makers: H1 FY26 results are now VERIFIED from TDnet 決算短信 (Fujikura 10 Nov, Sumitomo Electric 30 Oct, Furukawa 9 Nov 2026). Still unverified: their customer concentration, named hyperscaler contracts, CPO, multicore and hollow-core product progress, and Senko and other private connector makers.
- Supplier shares for fibre and connectors. Demand per rack beyond Corning's per-GPU figures.
- India: Sterlite Technologies (STL) results not retrieved (the BSE announcements API returned "Access Denied" to automated access); NSE not tried. India's verified role in this segment is design centres only (Ayar Labs Bengaluru, Sep 2026; Marvell operations per its 10-K) and Amphenol's CCS-related ADC India open offer (2026).
- Europe: Huber+Suhner's 2026 figures not retrieved; its investor page shows the next release (order intake and net sales FY2026) on 21 Jan 2027. Prysmian, Rosenberger and TE Connectivity not checked. Nokia's AI-optics push known only from a headline (Fierce Network, 6 Nov 2026).
- Korea: no Korean CPO-switch or optical-I/O company found. Korea's verified roles are substrates (Samsung Electro-Mechanics), packaging (Amkor Korea) and an NVLink Fusion collaboration (Rebellions/SK Telecom, 8 Nov 2026). DART was not searched.
- AMD's optical scale-up roadmap and the AMD-Enosemi deal; the Astera Labs-aiXscale deal; Molex-Teramount terms; Ranovus, Oriole, Avicena, OpenLight and Xsight funding and runway; Celestica DS6005 specs.
- Cisco Q1 FY27 results (not out or not indexed by 12 Nov 2026); Cisco's FY26 gross-margin level (only the -0.4 pp change was extracted). Accton Q3 2026 gross margin and EPS: its statements were not yet in TWSE open data on 12 Nov 2026.
- Return on capital comes only from an aggregator (stockanalysis.com, TTM). It was not recomputed from filings, and methodology differences (e.g. Arista's ~240% ROIC) make cross-company comparison approximate.
- Start-up runway (months of cash). Only funding totals are known: Ayar Labs $870M + $150M in 2026; Lightmatter $850M. Inference: both could fund a 1-2 year slip at current raise levels, but burn rates are not public.

---

## 8. Sources (URL; publication date; type)

Primary — filings and company releases:
- NVIDIA 10-Q, quarter to 26 Jul 2026 — https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000075/nvda-20260726.htm (Aug 2026)
- NVIDIA Q2 FY27 CFO commentary — https://www.marketscreener.com/news/nvidia-second-quarter-2027-cfo-commentary-ce7858d9d18df324 (26 Aug 2026; reproduction)
- NVIDIA Q2 FY26 CFO commentary (prior-year networking) — https://www.sec.gov/Archives/edgar/data/1045810/000104581025000207/q2fy26cfocommentary.htm (Aug 2025)
- NVIDIA Spectrum-X Photonics release — https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Announces-Spectrum-X-Photonics-Co-Packaged-Optics-Networking-Switches-to-Scale-AI-Factories-to-Millions-of-GPUs/default.aspx (Mar 2025)
- NVIDIA newsroom (Rebellions/SKT NVLink Fusion, 8 Nov 2026) — https://nvidianews.nvidia.com/news
- Broadcom Q3 FY26 8-K — https://www.sec.gov/Archives/edgar/data/0001730168/000173016826000076/avgo-08022026x8kxex99.htm (2 Sep 2026)
- Broadcom CPO reliability release — https://www.globenewswire.com/news-release/2025/10/01/3159570/19933/en/broadcom-showcases-industry-leading-quality-and-reliability-of-co-packaged-optics.html (1 Oct 2025)
- Marvell Q2 FY27 8-K — https://www.sec.gov/Archives/edgar/data/0001835632/000183563226000022/q227_8kx812026ex-991.htm (27 Aug 2026)
- Marvell FY26 10-K — https://www.sec.gov/Archives/edgar/data/1835632/000183563226000011/mrvl-20260131.htm (early 2026)
- Marvell-Lumentum 8-K/425 — https://www.sec.gov/Archives/edgar/data/0001835632/000119312526442723/d81187d425.htm (1-2 Nov 2026)
- Arista Q3 2026 release — https://s21.q4cdn.com/861911615/files/doc_news/Arista-Networks-Inc--Reports-Third-Quarter-2026-Financial-Results-2026.pdf (3 Nov 2026)
- Arista IR feed (XPO 12 Mar 2026; rack-scale 7 Oct 2026) — https://investors.arista.com/feed/PressRelease.svc/GetPressReleaseList?LanguageId=1&bodyType=1&pressReleaseDateFilter=3&pageSize=200&pageNumber=0&year=2026
- Corning Q3 2026 8-K — https://www.sec.gov/Archives/edgar/data/0000024741/000002474126000273/glw-20261027xex99xq32026.htm (27 Oct 2026)
- Corning IR feed (Meta 27 Jan 2026; Hickory 31 Mar 2026; PRIZM 11 Mar 2026; OFC 16 Mar 2026; NVIDIA 6 May 2026) — https://investor.corning.com/feed/PressRelease.svc/GetPressReleaseList?LanguageId=1&bodyType=1&pressReleaseDateFilter=3&pageSize=60&pageNumber=0&year=2026
- Corning-Meta release — https://investor.corning.com/news-and-events/news/news-details/2026/Corning-and-Meta-Announce-Multiyear-up-to-6-Billion-Agreement-to-Accelerate-US-Data-Center-Buildout/default.aspx (27 Jan 2026)
- NVIDIA-Corning release — https://investor.corning.com/news-and-events/news/news-details/2026/NVIDIA-and-Corning-Announce-Long-Term-Partnership-To-Strengthen-U-S--Manufacturing-for-AI-Infrastructure/default.aspx (6 May 2026)
- Amphenol CCS close — https://s21.q4cdn.com/564806605/files/doc_news/2026/Jan/12/2026_01_12-PR-Closes-acq-of-CCS.pdf (12 Jan 2026)
- Amphenol Q3 2026 release — https://s21.q4cdn.com/564806605/files/doc_financials/2026/q3/2026_10_28-PR-3Q-2026-Results_Dividend-Increase-and-Buyback.pdf (28 Oct 2026)
- Celestica Q3 2026 release — https://finviz.com/news/408117/celestica-announces-third-quarter-2026-financial-results-and-will-hold-2026-investor-and-analyst-day (26 Oct 2026; reproduction)
- Celestica DS6005 (title only) — https://corporate.celestica.com/news-releases/news-release-details/celestica-introduces-ds6005-data-center-switch-co-packaged (12 Oct 2026)
- Ciena IR feed (Nubis 22 Sep 2025; Vesta 25 Feb 2026; FY29 targets 16 Sep 2026) — https://investor.ciena.com/feed/PressRelease.svc/GetPressReleaseList?LanguageId=1&bodyType=1&pressReleaseDateFilter=3&pageSize=200&pageNumber=0&year=2025 and ...&year=2026
- Credo IR feed (Hyperlume 29 Sep 2025; DustPhotonics 13 Apr / 28 May 2026; SRMO 12 Oct 2026) — https://investors.credosemi.com/feed/PressRelease.svc/GetPressReleaseList?LanguageId=1&bodyType=1&pressReleaseDateFilter=3&pageSize=200&pageNumber=0&year=2026
- Lightmatter company page — https://lightmatter.co/llms.txt (updated 24 Apr 2026)
- Broadcom 10-Q, quarter to 2 Aug 2026 — https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm (filed 10 Sep 2026); Broadcom 10-K FY25 — https://www.sec.gov/Archives/edgar/data/1730168/000173016825000121/avgo-20251102.htm (filed 18 Dec 2025)
- Arista 10-K FY25 — https://www.sec.gov/Archives/edgar/data/1596532/000159653226000013/anet-20251231.htm (filed 17 Feb 2026); Arista 10-Q Q3 2026 — https://www.sec.gov/Archives/edgar/data/1596532/000159653226000254/anet-20260930.htm (filed 4 Nov 2026)
- Cisco 10-K FY26 — https://www.sec.gov/Archives/edgar/data/858877/000085887726000132/csco-20260725.htm (filed 2 Sep 2026)
- Celestica 10-Q Q3 2026 — https://www.sec.gov/Archives/edgar/data/1030894/000103089426000050/cls-20260930.htm (filed 26 Oct 2026)
- Credo 10-Q, quarter to 1 Aug 2026 (DustPhotonics purchase accounting) — https://www.sec.gov/Archives/edgar/data/1807794/000162828026060111/crdo-20260801.htm (filed 2 Sep 2026)
- TWSE open data, listed-company income statements (ASE 3711, KYEC 2449, Wiwynn 6669; 2026 Q3, table dated 12 Nov 2026) — https://openapi.twse.com.tw/v1/opendata/t187ap06_L_ci
- stockanalysis.com statistics pages (TTM return metrics only; aggregator; retrieved 12 Nov 2026) — https://stockanalysis.com/stocks/nvda/statistics/ (likewise /avgo/, /anet/, /glw/, /aph/, /mrvl/, /csco/, /cls/); Japan: https://stockanalysis.com/quote/tyo/5803/statistics/ (likewise /5802/, /5801/)
- TDnet (Japan Exchange timely disclosure; Japanese-language primary filings):
  - Fujikura H1 FY26 決算短信 — https://www.release.tdnet.info/inbs/140120261109569418.pdf (10 Nov 2026)
  - Fujikura forecast revision — https://www.release.tdnet.info/inbs/140120261109570131.pdf (10 Nov 2026)
  - Fujikura subsidiary transfer — https://www.release.tdnet.info/inbs/140120261105565331.pdf (5 Nov 2026)
  - Sumitomo Electric H1 FY26 決算短信 — https://www.release.tdnet.info/inbs/140120261029559548.pdf (30 Oct 2026)
  - Furukawa Electric H1 FY26 決算短信 — https://www.release.tdnet.info/inbs/140120261106567992.pdf (9 Nov 2026)
  - Furukawa forecast revision — https://www.release.tdnet.info/inbs/140120261106568021.pdf (9 Nov 2026)
  - Daily listing pages used to locate them: https://www.release.tdnet.info/inbs/I_list_001_20261110.html (etc.)
- cninfo (China; Chinese-language Q3 2026 reports, 三季度报告; located via cninfo's announcement-query API by stock code):
  - Ruijie Networks — http://static.cninfo.com.cn/finalpage/2026-10-20/1225610290.PDF (20 Oct 2026)
  - Unisplendour (H3C parent) — http://static.cninfo.com.cn/finalpage/2026-10-30/1225643427.PDF (30 Oct 2026)
  - ZTE — http://static.cninfo.com.cn/finalpage/2026-10-27/1225623166.PDF (27 Oct 2026)
  - YOFC — http://static.cninfo.com.cn/finalpage/2026-10-31/1225649258.PDF (31 Oct 2026)
  - T&S Communications — http://static.cninfo.com.cn/finalpage/2026-10-30/1225643320.PDF (30 Oct 2026)

Earnings-call transcripts (third-party transcription):
- NVIDIA Q2 FY27 — https://www.fool.com/earnings/call-transcripts/2026/08/31/nvidia-nvda-q2-2027-earnings-call-transcript/ (26 Aug 2026 call)
- Arista Q3 2026 — https://www.fool.com/earnings/call-transcripts/2026/11/04/arista-anet-q3-2026-earnings-call-transcript/ (3 Nov 2026 call)
- Corning Q3 2026 — https://www.fool.com/earnings/call-transcripts/2026/10/27/corning-glw-q3-2026-earnings-call-transcript/ (27 Oct 2026 call)

Secondary — trade press and analysts:
- SDxCentral (15x claim, GTC Berlin) — https://www.sdxcentral.com/news/nvidia-targets-15x-optics-capacity-expansion-by-2027-to-meet-cpo-demand/ (21 Oct 2026)
- Taiwan News (SPIL 15x; KYEC) — https://www.taiwannews.com.tw/news/6463331 (22 Oct 2026)
- TechTimes (six-partner prepayments) — https://www.techtimes.com/articles/329352/20261022/nvidia-locks-ai-chip-testing-optics-capacity-six-partner-prepayment-push.htm (22 Oct 2026)
- SimpleTechTrend (15x analysis) — https://www.simpletechtrend.com/en/post/nvidia-cpo-prepaid-capacity-spil-kyec-2026-w43-en (26 Oct 2026)
- SimpleTechTrend (LightCounting OCP 2026 forecast) — https://www.simpletechtrend.com/en/post/ocp-2026-lightcounting-cpo-npo-forecast-scenarios-en (22 Oct 2026)
- Digitimes (headline only) — https://www.digitimes.com/news/a20261110PD223/cpo-spil-nvidia-infrastructure-investment.html (10 Nov 2026)
- GCN (NVIDIA OOI prototype) — https://gcn.com/?p=22794 (27 Oct 2026)
- The Register (NVIDIA networking) — https://www.theregister.com/networks/2026/10/31/backbone-of-a-beast-charting-nvidias-rise-to-networking-titan/5306499 (31 Oct 2026)
- The Register (Cisco G300) — https://www.theregister.com/2026/02/10/cisco_challenges_broadcom_nvidia_switch_chips/ (10 Feb 2026)
- Counterpoint (NVIDIA optics roadmap) — https://counterpointresearch.com/en/insights/from-blackwell-to-feynman-analyzing-nvidias-optics-roadmap (2 Apr 2026)
- SemiAnalysis (GTC 2026) — https://newsletter.semianalysis.com/p/nvidia-the-inference-kingdom-expands (Mar 2026; via search summary)
- HPCwire (silicon photonics roadmap; content blocked, search summary only) — https://www.hpcwire.com/2026/04/20/inside-nvidias-silicon-photonics-roadmap/ (20 Apr 2026)
- Glenn Klockwood notes (Quantum-X / Spectrum-X Photonics) — https://www.glennklockwood.com/garden/spectrum-x-photonics (Jun 2026)
- Futurum (Marvell Investor Day) — https://futurumgroup.com/insights/marvell-investor-day-2026-targets-80b-fy-2031-revenue-with-custom-silicon-and-optics/ (9 Oct 2026)
- NextPlatform (Marvell Q2 FY27) — https://www.nextplatform.com/connect/2026/09/02/optics-still-driving-marvells-ai-business-more-than-custom-chips/5294018 (2 Sep 2026)
- NextPlatform (Broadcom/Meta CPO) — https://www.nextplatform.com/connect/2025/10/17/the-third-time-will-be-the-charm-for-broadcom-switch-co-packaged-optics/1635588 (17 Oct 2025)
- ServeTheHome (TH6-Davisson) — https://www.servethehome.com/broadcom-tomahawk-6-davisson-102-4t-switch-with-co-packaged-optics-shipping/ (12 Oct 2025)
- StorageReview (Davisson; Micas) — https://www.storagereview.com/news/broadcom-ships-tomahawk-6-davisson-cpo-ethernet-switch-doubling-bandwidth-to-102-4-tb-s-for-ai-fabrics ; https://www.storagereview.com/news/micas-networks-tomahawk-6-102t-switches-davisson-cpo
- STORDIS (Davisson sampling) — https://stordis.com/broadcom-tomahawk-6-vs-th6-davisson/
- LightCounting Dec 2025 newsletter — https://www.lightcounting.com/newsletter/en/december-2025-aocs-dacs-linear-drive-pluggable-and-co-packaged-optics-320 (Dec 2025)
- EE Times (LightCounting at ECOC 2025) — https://www.eetimes.com/ai-demand-reshapes-optical-connectivity-and-photonics-roadmaps/ (25 Nov 2025)
- Fierce Network (optical start-ups) — https://www.fierce-network.com/broadband/5-optical-startups-watch-ai-pushes-optics-deeper-network (16 Oct 2026)
- Dell'Oro newsroom (DC capex +92% 2Q26, 16 Sep 2026; memory-crunch note, 29 Oct 2026) — https://www.delloro.com/news/
- unite.ai (Cisco Q4 FY26) — https://www.unite.ai/cisco-books-4b-in-quarterly-ai-orders-as-networking-supercycle-lifts-fy2027-outlook/ (12 Aug 2026)
- evertiq (Celestica) — https://evertiq.com/news/2026-11-06-celestica-expects-revenue-to-almost-double-to-40-billion-in-2027 (6 Nov 2026)
- Taiwan News (Accton Q2 2026) — https://www.taiwannews.com.tw/news/6396424 ; Digitimes Accton tag — https://www.digitimes.com/tag/accton/001693.html ; StatementDog (Accton Q3 2025) — https://statementdog.com/news/15154 (28 Nov 2025)
- Ayar Labs funding — https://www.insightpartners.com/ideas/ayar-labs-closes-500m-series-e-accelerates-volume-production-of-co-packaged-optics/ (Mar 2026); https://siliconangle.com/2026/09/10/ayar-labs-bags-150m-in-additional-series-e-funding-to-help-make-bigger-ai-chip-clusters/ (10 Sep 2026)
- Teramount redirect observation — https://teramount.com/ redirects to https://www.molex.com/en-us/products/optical-solutions/teraverse-detachable-optical-chiplet-connectors (observed 12 Nov 2026)
