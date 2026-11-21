# IXM: X-ray Modules division. Who buys Comet sources, and how the roadmap compares (Q4)

Comet's fiscal year is the calendar year (ends 31 Dec). Evidence ids refer to `research/out/comet/parts/IXM.csv`. Arithmetic is in `research/out/comet/calc/IXM_intersegment.py`.

## Summary

- **Comet discloses markets, not customers.** No annual report, half-year report, results deck or CMD deck (2021, 2022, 2023, 2025) names an external buyer of IXM sources. The "key accounts" note covers only PCT's largest customer [F] (IXM-010). IXM customer concentration is **NOT DISCLOSED**. IXM external sales in FY2025 (Jan-Dec 2025) split into NDT CHF 60.3m, Security CHF 15.4m and Others CHF 13.4m [F] (IXM-009). That is 67.7% / 17.3% / 15.0%, and Security grew 32.0% YoY [I] (script).
- **Internal vs external.** IXM sells to other Comet segments at third-party prices [F] (IXM-008). Intersegment sales were CHF 9.9m in FY2025 and CHF 6.0m in H1 2026 (Jan-Jun 2026) [F] (IXM-001, IXM-006). They made up 10.0% of IXM total net sales in FY2025 and 11.2% in H1 2026, against 12-17% in FY2020-FY2024 [I] (IXM-007; Medium, because Comet does not name the buying segment). Comet's own words show that IXS (Comet Yxlon) systems carry IXM tubes: CA20 [F] (IXM-011), FF35 CT with two FXE tubes [F] (IXM-012), UX20 with MesoFocus 225 [F] (IXM-013), and the legacy Cheetah/Cougar FeinFocus line [F] (IXM-014).
- **Named external buyers come only from Comet's marketing pages, plus one Waygate statement.** They are diondo (d3: 450 kV HP plus 450 kV MesoFocus), IMS (steel gauges, since the 1990s), North Star Imaging (MesoFocus), Pinnacle X-Ray Solutions (MesoFocus/HP), X-RIS (BLOX) and Waygate (MesoFocus option on the Phoenix V|tome|x C450, which Waygate says was developed with Comet). Every named buyer is in industrial NDT, battery, castings, aerospace or steel. **No semiconductor-inspection system maker was found stating that it uses a Comet source.**
- **In the high-resolution and semiconductor tier, the evidence points to in-house sources or Excillum, not Comet.** Waygate's Nanotom HR, Rigaku's CT Lab HR160 (Sep 2026), SFA's in-fab HBM/TGV tool (Sep 2026) and TechValley all use Excillum sources [F] (IXM-023, IXM-026..028). Nikon (since 1986), Zeiss (ZXR-1, Jan 2026), Viscom, Nordson DAGE (QuadraNT) and SEC (Hybrid Open Tube) build their own sources [F]/[S] (IXM-029..033).
- **Roadmap.** Comet's semiconductor source is FYNE 160 NF4: an open tube, 400 nm resolution, launched Feb-Apr 2025 [C] (IXM-056, IXM-057). It was followed by NF12 (1.1 um, up to 10x dose) [C] (IXM-058), FXE-190 nano CT (0.45 um) [C] (IXM-053) and FXE-160 nano CT (0.7 um) [C] (IXM-052). On the datasheet numbers, competing nanofocus sources resolve finer: Excillum NanoTube N3 at 150 nm [F] (IXM-063) and Hamamatsu L10711-26 at 0.2 um [F] (IXM-069). Comet has no disclosed liquid-metal-jet or other high-brightness (kW-class microfocus) plan. Excillum's MetalJet E1+/F1016 runs at 1,000-1,600 W [F]/[C] (IXM-065, IXM-066).

## (1) Buyers table

Who says it: **Comet** = a Comet publication (it may quote the customer); **Maker** = the system maker's own statement; **Third party** = press or trade site.

| System maker | Evidence | Who says it | Tag | Id |
|---|---|---|---|---|
| Comet Yxlon (IXS, internal) | CA20 semiconductor systems "equipped with Comet IXM's advanced x-ray tubes" (AR 2024) | Comet | [F] | IXM-011 |
| Comet Yxlon (IXS, internal) | FF35 CT delivered to PCT Flamatt with two FXE tubes (Sep 2023) | Comet | [F] | IXM-012 |
| Comet Yxlon (IXS, internal) | UX20 offered with MesoFocus 225 (AR 2021) | Comet | [F] | IXM-013 |
| Comet Yxlon (IXS, internal) | FXE sold inside Yxlon systems; Cheetah and Cougar were FeinFocus products; tubes moved to Comet X-ray from 2019 | Comet | [F] | IXM-014 |
| All other segments (internal) | IXM intersegment sales CHF 9.9m in FY2025 (10.0% of IXM total) and CHF 6.0m in H1 2026 (11.2%) | Comet; calc | [F]/[I] | IXM-001..007 |
| diondo (DE) | d3 CT integrates Comet 450 kV High Power plus 450 kV MesoFocus; diondo is quoted: "Using Comet's sealed HP 11 and MesoFocus tubes" (Jan 2025) | Comet (quotes diondo) | [F] | IXM-015 |
| IMS Messsysteme / IMS Röntgensysteme (DE) | Comet tubes in steel-industry gauges since the 1990s; joint 100 kV metal-ceramic tube; MiniMax 2009; MXR-228 (Apr 2025) | Comet (quotes IMS MD) | [F] | IXM-016 |
| North Star Imaging (US; not part of Comet) | "MesoFocus tube we use at our facility..." (Mar 2026); NSI and Comet BLOX (May 2026) | Comet (quotes NSI staff) | [F] | IXM-017, IXM-018 |
| Pinnacle X-Ray Solutions (US) | Builds cabinets with Comet MesoFocus/HP; "some customers request ... a Comet tube" (May 2025) | Comet (quotes Pinnacle CPO) | [F] | IXM-019 |
| Pinnacle X-Ray Solutions (US) | Also runs an Excillum MetalJet CT demonstrator (Nov 2024), so it buys from more than one source maker | Excillum | [F] | IXM-024 |
| X-RIS (BE) | Uses Comet BLOX data to service its systems (Apr 2026) | Comet (quotes X-RIS) | [F] | IXM-020 |
| Waygate Technologies / Baker Hughes | "The closed Comet iXRS 450 MF tube provides an alternative to the 450 kV Isovolt Minifocus X-ray tube" on the Phoenix V|tome|x C450 | Waygate, via BINDT reprint | [S] | IXM-021 |
| Waygate Technologies | Mesofocus "developed in collaboration with Comet"; 63 um at 450 kV (Oct 2024) | Waygate, via OnestopNDT | [S] | IXM-022 |
| Waygate Technologies | Nanotom HR uses the Excillum NanoTube N3, not a Comet source (May 2025) | Excillum (joint release) | [F] | IXM-023 |
| Rigaku | CT Lab HR160 (Sep 2026) uses an Excillum nano-focus source; 250 nm | Excillum (quotes Rigaku) | [F] | IXM-026 |
| SFA Engineering (KR) | In-fab HBM/TGV inspection on the Excillum N3; demo system 2026 | Excillum (quotes SFA) | [F] | IXM-027 |
| TechValley (KR) | In-line PCB laminography on the N3; first deployments July 2024 | Excillum (quotes TechValley) | [F] | IXM-028 |
| Bruker, Sigray, Sanying, Royma, ProCon, Xenocs and others | On Excillum's partner list (Zeiss, Nordson and Nikon are not on it) | Excillum | [F] | IXM-025 |
| Nikon | Sources "designed and manufactured in-house since 1986" | Maker | [F] | IXM-029 |
| Zeiss | Own ZXR-1 source on VersaXRM 730 (Jan 2026). Source maker for earlier Versa models: NOT DISCLOSED | Maker | [F] | IXM-030 |
| Viscom | Proprietary x-ray tubes, also sold to OEMs (a competitor in the OEM tube market) | Maker (AR 2024) | [F] | IXM-031 |
| Nordson DAGE | QuadraNT sealed tube "from Nordson DAGE" (Quadra 3/5/7; 2018) | Nordson, via iConnect007 | [S] | IXM-032 |
| SEC Co. (KR) | Independently developed "Hybrid Open Tube" for HBM in-line tools (May 2026) | SEC, via Asia Economy | [S] | IXM-033 |
| Sigray | Apex-Hybrid uses "a novel x-ray source" with microstructured calibration targets; vendor not named | Maker | [F] | IXM-034 |
| Werth | TomoScope monoblock transmission tubes, 130-230 kV; who builds them is not stated | Maker | [F] | IXM-035 |
| Unnamed foundries, IDMs and OSATs | "X-ray modules and systems are deployed by leading foundries, IDMs ... OSATs" | Comet | [C] | IXM-036 |
| Omron, Saki, Lumafield, Unicomp, RX Solutions, Smiths/Rapiscan/Nuctech | No saved evidence either way (see Gaps) | n/a | n/a | n/a |

The table names 25 makers. Comet sources are evidenced, by Comet or by the maker, at 7: Comet Yxlon, diondo, IMS, NSI, Pinnacle, X-RIS and Waygate (450 kV Mesofocus only).

**Market position claims (Comet only).**
- Comet claims "#1 in industrial x-ray sources" [C] (IXM-037).
- At CMD 2023 Comet gave segment ranks: #1 in stationary and integrated tubes, #3 in stationary modules, "new entry" in sealed micro focus, #4 in open micro focus and #3 in open nano focus [C] (IXM-038). On Comet's own account, then, it is not the leader in the micro and nano focus tiers that matter for semiconductor inspection.
- In H1 2025 IXM reported a "drive for lower-cost suppliers, domestic production and more intense competition" [C] (IXM-039).
- In FY2025 it reported share gains in the U.S. and China [C] (IXM-040).
- H1 2026 growth came from aerospace, defense and security, battery, and AI/advanced packaging [C] (IXM-041).
- The 2028e target is IXM sales of CHF 110-130m at a 23-27% EBITDA margin [C] (IXM-042; read from a chart, Low).

## (2) Roadmap comparison table

| Source | Maker | Focal spot / resolution | kV / power | Brightness | Target | Semiconductor positioning | Launch / date | Tag | Id |
|---|---|---|---|---|---|---|---|---|---|
| FYNE 160 NF4 (open nanofocus) | Comet | 400 nm resolution at 160 kV (thin target); about 1.2 um with a thicker target | 60-160 kV | Up to 4x usable dose at 400 nm vs "conventional nano-focus" | Transmission, thickness selectable; emitter life 10x previous open tube; >2,600 h | Advanced packaging, HBM/GPU bumps, TSV | Feb-Apr 2025 | [C] | IXM-056..058, IXM-060 |
| FYNE NF12 | Comet | 1.1 um | n/d | Up to 10x dose at 1.1 um | n/d | HBM/C2/C4 bumps | Named Oct 2026 | [C] | IXM-058 |
| Unnamed new module (FY2024 AR) | Comet | Focal spot "as small as 600 nanometers" | n/d | n/d | n/d | Semiconductor and advanced packaging | FY2024 | [C] | IXM-059 |
| FXE-190 nano CT | Comet | 0.45 um (HRP target, 1.4 W); 0.6 um nano mode; 0.9 um micro mode; 2 um high-power mode | Up to 190 kV; target power to 30 W | n/d | Transmission, HPT/HRP targets; internal cooling; Clear(TM) low-Z | Lab, electronics FA | Jul 2025 | [C] | IXM-053 |
| FXE-160 nano CT | Comet | 0.7 um (1.6 W); 1.8 um (10 W); 2.8 um (15 W) | 160 kV; 2-15 W | n/d | Transmission high-power target; external cooling (2 um drift vs 18 um) | Sub-micron lab inspection | Apr 2026 (resolution upgrade); cooling Feb 2024 | [C] | IXM-052, IXM-054 |
| FXE 225.48 (directional) | Comet | 4 um max resolution | 225 kV; 32-280 W (text: 320 W) | n/d | Reflection; HDP target doubles power density (Aug 2024) | Electronics and battery throughput | Datasheet 2026; HDP Aug 2024 | [F]/[C] | IXM-050, IXM-051 |
| FXE series (open, ex-FeinFocus) | Comet | "500 nm to a few millimeters" feature recognition | Up to 225 kV | n/d | Transmission and reflection; Quickswap filament (Jun 2026) | PCBA, IC packaging, WLCSP, MEMS | FeinFocus 1982; at Comet since 2004; under IXM from 2019/2021 | [F]/[C] | IXM-014, IXM-055 |
| MesoFocus MXC 450 MF (sealed) | Comet | 0.063-0.450 mm (5 spots); detail to 25 um | 450 kV; 50-450 W | n/d | Sealed metal-ceramic, bipolar, oil-cooled | Battery, castings, aerospace (not semi) | June 2021 (about page says 2022) | [F]/[C] | IXM-047..049 |
| Xplorer (sealed micro focus) | Comet | n/d in saved files | n/d | n/d | Sealed | Electronics | Introduced after 2023 CMD roadmap | [C] | IXM-044 |
| BLOX | Comet | n/a: IIoT health monitor for tubes and generators | n/a | n/a | n/a | Uptime | Jul 2025 | [C] | IXM-061 |
| NanoTube N3 | Excillum | 150 nm resolution (lines and spaces); "300 nm focal spot technology" | 40-160 kV; 16.6 W (160 kV model) | n/d | W on diamond, transmission; LaB6; spot stability <100 nm | HBM micro-bumps, TSV, hybrid bonds; SFA in-fab HBM/TGV | N3 launched Dec 2021 (lead); datasheet 2024 | [F]/[C] | IXM-063, IXM-064, IXM-068 |
| MetalJet E1+ 160 kV | Excillum | <10 um min spot | 30-160 kV; 0-1000 W | 17x flux vs 30 W solid anode at 30 um | Liquid-metal jet (ExAlloy) | In-line inspection | Product page 2026 | [F] | IXM-065 |
| MetalJet F1016 | Excillum | 30 um at 1,600 W | 160 kV; 1,600 W | ">230 MetalJets shipped" | Liquid-metal jet | "Lab to fab" in semiconductor and battery | Mar 2025 | [C] | IXM-066 |
| L10711-26 (open) | Hamamatsu | 0.2 um (LaB6, S mode); 0.8 um (W mode) | 20-160 kV; 9.6 W (W mode) | n/d | Tungsten transmission, diamond window | NDT, industrial CT | Aug 2026 | [F] | IXM-069 |
| MFX series | Hamamatsu | n/d | 20-300 kV; sealed and open | n/d | n/d | Semiconductor, PCB, battery | Catalog Feb 2025 | [F] | IXM-070 |
| ZXR-1 (sealed) | Zeiss (in-house) | VersaXRM 730 <450 nm spatial resolution | 30-160 kV; 25 W | n/d | Tungsten-diamond transmission, actively cooled, LaB6 | XRM (FA, research) | Jan 2026 | [F] | IXM-030, IXM-071 |
| QuadraNT (sealed) | Nordson DAGE (in-house) | 0.95 um to sub 0.1 um feature recognition (claimed) | n/d | n/d | Sealed transmission | Semi and PCBA AXI | Quadra 3, 2018 | [S] | IXM-032 |
| 450 kV microfocus / Rotating.Target 2.0 | Nikon (in-house) | 80 um at 450 kV | 450 kV; 450 W | n/d | Rotating reflection target | Dense parts (competes with MesoFocus) | Page 2026 | [C] | IXM-072 |
| PXS10 (sealed) | Thermo Fisher | 6 um at 4 W | 130 kV | n/d | Sealed | EV battery, PCBA in-line | Page 2026 | [F] | IXM-073 |
| Apex-Hybrid / ApexXCT source | Sigray | 350 nm (open, 16 W) / 500-600 nm (sealed, 25 W) | n/d | n/d | Microstructured target (calibration) | 300 mm wafer and package XCT | Nov 2025 | [F] | IXM-074 |
| Hybrid Open Tube | SEC (in-house) | n/d | n/d | n/d | Open/closed hybrid | HBM in-line | 2026 | [S] | IXM-033 |
| Monoblock transmission tube | Werth | "a few micrometres" | 130-160 / 200 / 230 kV | n/d | Transmission, open monoblock | Metrology CT | Page 2026 | [F] | IXM-035 |
| Tubes for OEMs | Oxford Instruments X-Ray Technology | n/d | n/d | n/d | n/d | Analytical, medical, NDT OEMs | Page 2026 | [F] | IXM-075 |
| 180 kV closed tube (iX7059) | Viscom (in-house) | n/d | 180 kV | n/d | Closed | In-line AXI | FY2024 | [F] | IXM-076 |
| CT Lab HR160 source | Excillum, inside a Rigaku system | 250 nm true spatial resolution (system) | Up to 160 kV | n/d | n/d | Semiconductor devices, MLCC, batteries | Sep 2026 | [F] | IXM-026 |

**Reading the table** [I] (Medium; inputs IXM-052, 053, 056-058, 063, 069, 071):
- Comet's best disclosed figures (0.4 um FYNE, 0.45 um FXE-190) fall short of the finest merchant nanofocus figures (Excillum 150 nm lines and spaces; Hamamatsu 0.2 um). They sit close to Zeiss's in-house ZXR-1 system (<450 nm).
- The figures are not like-for-like. Comet quotes mask-line resolution on its own imaging chain. Excillum quotes lines and spaces. Hamamatsu quotes "minimum resolution".
- Comet's pitch is dose at a given resolution plus lifetime (FYNE: 4-10x dose, >2,600 h), not ultimate resolution.
- Comet has no counterpart to Excillum's liquid-metal-jet line (1-1.6 kW at about 30 um). Comet's highest microfocus power is the FXE-225 reflection tube at about 280-320 W.

## Gaps

- NOT DISCLOSED (read: Comet Annual Reports FY2021-FY2025 note 04.3 "Sales with key accounts" and segment notes; H1 2026 half-year report note 03): IXM customer names and customer concentration (largest IXM customer, share of top-N).
- NOT DISCLOSED (read: Comet AR FY2025 note 04.1; H1 2026 report note 03.1): which segment buys IXM's intersegment sales (IXS vs PCT split).
- NOT DISCLOSED (read: CMD 2021/2022/2023/2025 decks; AR FY2023-FY2025 IXM sections; comet.tech/xray FYNE, FXE and need-for-speed pages): any Comet liquid-metal-jet or other kW-class high-brightness microfocus source plan.
- NOT DISCLOSED (read: comet.tech/xray FYNE 160 NF4 product page and FYNE focus topic): FYNE NF4 power in watts and brightness.
- NOT DISCLOSED (read: Comet AR FY2024 X-Ray Modules review): the name of the "new high-resolution x-ray module ... as small as 600 nanometers".
- NOT DISCLOSED (read: Zeiss ZXR-1 flyer, Jan 2026): the source maker for Xradia Versa models before the 730.
- NOT DISCLOSED (read: Comet Yxlon CA20 product page and CA20 launch news 2023/2024): which IXM tube type (FXE or FYNE) is in the CA20.
- NOT RETRIEVED (tried: fetch.py on bakerhughes.com/waygate-technologies/.../mesofocus-x-ray-tubes): it returned a 212-byte bot-check stub (saved as 2026-11-21_waygate_product-page-mesofocus-x-ray-tubes.html, but it is not the page). The Baker Hughes 25-year brochure PDF also failed. Waygate's own MesoFocus statement is cited via BINDT/OnestopNDT [S].
- NOT RETRIEVED (tried: fetch.py on yxlon.comet.tech/en/blog/450-kv-mesofocus-ct-part-1): connection failed (http 000).
- NOT RETRIEVED (tried: fetch.py on nordson.com Quadra 7 Pro page and investors.nordson.com 2016 Quadra launch release): 403. medicalexpo.com Quadra 7 Pro listing: 403.
- NOT RETRIEVED (tried: fetch.py on directindustry.com Unicomp microfocus source listing): 403. Whether Unicomp builds its sources in-house rests on a web-search lead only.
- NOT RETRIEVED (tried: web search for diondo's own d3 page naming Comet tubes): no diondo-side statement found.
- NOT RETRIEVED (tried: web search "Comet" with Smiths Detection / Rapiscan / Nuctech): no named security OEM buyer found, although Security was 17% of IXM external sales in FY2025.
- NOT RETRIEVED (tried: web search for Lumafield Neptune and RX Solutions EasyTom source suppliers): neither names its tube maker.
- NOT RETRIEVED (tried: grep of the saved Monoist article on the Omron VT-X950 for a tube or source vendor; Saki not searched): source supplier unknown for Omron and Saki.
- NOT DISCLOSED (read: comet.tech/xray product listing pages for FXE micro/nano and Xplorer, saved 2026-11-21): the pages render by script, and the saved text has no specs.

## Premise corrections

- **North Star Imaging is not related to Comet Yxlon.** NSI calls itself an ITW (Illinois Tool Works) company (search lead, not saved). It is an external Comet MesoFocus user (IXM-017).
- **The pct-yxlon-collaboration item is internal.** It shows a Yxlon FF35 CT with two Comet FXE tubes installed at Comet PCT in Flamatt (Sep 2023). It is not evidence of an external customer (IXM-012).
- **Rigaku is not purely in-house.** Its new CT Lab HR160 (Sep 2026) uses an Excillum nano-focus source (IXM-026).
- **Zeiss sources.** The ZXR-1 on the VersaXRM 730 is a Zeiss in-house design (Jan 2026). The source maker for earlier Versa models is not stated (IXM-030).
- **Waygate buys from both Comet and Excillum.** It takes the 450 kV MesoFocus from Comet and the NanoTube N3 for the Nanotom HR from Excillum, and also makes its own Isovolt tubes. It is not simply an in-house competitor (IXM-021..023).
- **"Mesofocus (450 kV)" is the MXC/iXRS 450 MF.** A MesoFocus 225 variant also exists (IXM-013).
- **The MesoFocus launch year is inconsistent on Comet's own sites:** June 2021 in the news article, "2022" on the X-ray "About" page (IXM-047).
- **FeinFocus (the FXE origin) joined Comet in 2004.** Comet acquired Yxlon in 2007. FXE tube production moved from Yxlon to Comet X-ray after a 2019 decision (IXM-014).
- **The FXE resolution article is dated 20 Apr 2026, and the HDP target article 30 Aug 2024.** FYNE was first presented on 3 Feb 2025, and the news release followed on 2 Apr 2025.
- **"Fyne" and "BLOX" in the prompt.** FYNE is the nanofocus source (FYNE 160 NF4; NF12 also named). BLOX is an IIoT health-monitoring service, not a source.
