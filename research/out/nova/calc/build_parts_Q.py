#!/usr/bin/env python3
"""Build out/nova/parts/Q1.csv (product map), Q3.csv (Nova's own X-ray statements and products),
Q5.csv (advanced packaging), Q6.csv (integrated-metrology channel). Quotes validated by evrow.row().
Usage: python3 -I research/out/nova/calc/build_parts_Q.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from evrow import row, write

HERE = os.path.dirname(os.path.abspath(__file__))
PARTS = os.path.join(HERE, "..", "parts")
F20 = "2026-02-17_nova_20-F-FY2025.pdf"
F20_20 = "2021-03-01_nova_20-F-FY2020.pdf"
IDD = "2025-03-13_nova_investor-day-2025-presentation.pdf"
IDT = "2025-03-13_stockanalysis_transcript-investor-day-2025.html"
DMD = "2026-02-01_nova_brochure-dimensional-metrology-2026.pdf"
T = lambda d, k: f"{d}_stockanalysis_transcript-{k}.html"
Q3T = T("2026-11-05", "Q3-2026-call")


def R(tag, claim, value, pf, pc, doc, date, f, quote, conf="", note="", unit="", section=None):
    return row("x", tag, claim, value, unit, pf, pc, doc, date, f, quote, conf, note, section)


Q1 = [
    # --- portfolio structure (20-F FY2025) ---
    R("[F]", "Integrated metrology (Nova i-platform): optical CD mounted on process tools for wafer-to-wafer and within-die control; targets advanced logic, memory and advanced packaging", "product line", "FY2025", "as of Feb 2026",
      "Nova Form 20-F FY2025, Item 4B", "2026-02-17", F20, "Integrated metrology systems are directly integrated with manufacturing process equipment"),
    R("[F]", "Stand-alone dimensional metrology (T-series, MMSR, VeloCD, Prism, SemDex, WMC): CD, topography, thin film, roughness, thickness incl. WLP, TSV, PCB and IC-substrate", "product line", "FY2025", "as of Feb 2026",
      "Nova Form 20-F FY2025, Item 4B", "2026-02-17", F20, "Nova's stand-alone platforms are targeted for critical dimensions (CD), topography, thin-film, roughness and film thickness measurements"),
    R("[F]", "VeraFlex = XPS with optional low-energy XRF channel for elemental composition and thickness of thin films", "product line", "FY2025", "as of Feb 2026",
      "Nova Form 20-F FY2025, Item 4B", "2026-02-17", F20, "Nova's VeraFlex combines enhanced XPS (X-Ray photoelectron spectroscopy) capability with an optional unique low energy XRF (X-Ray fluorescence) channel"),
    R("[F]", "Metrion = in-line SIMS depth profiling for 3D logic and memory", "product line", "FY2025", "as of Feb 2026",
      "Nova Form 20-F FY2025, Item 4B", "2026-02-17", F20, "Nova Metrion targets process control of 3D logic and memory semiconductor devices and by applying inline SIMS"),
    R("[F]", "Elipson = Raman spectroscopy for strain, crystallinity, phase, grain size, composition", "product line", "FY2025", "as of Feb 2026",
      "Nova Form 20-F FY2025, Item 4B", "2026-02-17", F20, "Nova Elipson utilizes Raman spectroscopy, a vibrational technique, to detect multiple material properties"),
    R("[F]", "Chemical metrology (ancosys): AncoScene for damascene Cu and Co plating; Ancolyzer for advanced-packaging plating; DMR metal replenishment", "product line", "FY2025", "as of Feb 2026",
      "Nova Form 20-F FY2025, Item 4B", "2026-02-17", F20, "Nova AncoScene - a platform for damascene copper and cobalt plating interconnects applications"),
    R("[F]", "Chemical metrology portfolio serves backend WLP, TSV, front-end dual damascene, PCB and IC-substrate plating", "product line", "FY2025", "as of Feb 2026",
      "Nova Form 20-F FY2025, Item 4B", "2026-02-17", F20, "chemical metrology platforms for backend wafer-level packaging, TSV, front-end dual-damascene, and PCB and IC-Substrate process steps"),
    # --- integrated metrology products ---
    R("[C]", "i500: 'industry standard' for CMP process control with 'thousands of deployments' (company website claim)", "thousands of units (claim)", "n/a", "page read 21 Nov 2026",
      "Nova website, Nova i500 product page", "2026-11-21", "2026-11-21_nova_product-i500.html", "Sets industry standard for CMP process control with thousands of deployments"),
    R("[F]", "i550: integrated metrology for CMP and etch in advanced logic, 3D NAND double-deck and advanced DRAM", "application", "n/a", "page read 21 Nov 2026",
      "Nova website, Nova i550 product page", "2026-11-21", "2026-11-21_nova_product-i550.html", "integrated metrology platform that provides superior metrology performance for CMP and etch process control"),
    R("[F]", "i570 HP: most advanced integrated platform; 'attaches to the industry's fastest CMP polishers'", "application", "n/a", "page read 21 Nov 2026",
      "Nova website, Nova i570 HP product page", "2026-11-21", "2026-11-21_nova_product-i570.html", "attaches to the industry's fastest CMP polishers"),
    R("[F]", "i580 (introduced 2025): CMP and etch integrated metrology plus optional wafer-edge metrology for bonding in advanced packaging", "launch 2025", "FY2025", "Mar 2025",
      "Nova Investor Day 2025 presentation, slide 40", "2025-03-13", IDD, "Introducing Nova i580"),
    R("[F]", "i580 page: optional pre-bonding parameters (thickness profile, discoloration, defectivity, wafer centricity)", "application", "n/a", "page read 21 Nov 2026",
      "Nova website, Nova i580 product page", "2026-11-21", "2026-11-21_nova_product-i580.html", "Optional capability offering precise measurement of pre-bonding-related parameters, such as thickness profile, discoloration, defectivity, and wafer centricity"),
    # --- stand-alone OCD ---
    R("[F]", "Prism (spectral interferometry + SE/SR) introduced in 2020; Elipson (Raman) introduced in 2020", "launch 2020", "FY2020", "Jan-Dec 2020",
      "Nova Form 20-F FY2020, Item 4A/5 developments", "2021-03-01", F20_20, "Introduction of NovaPrism"),
    R("[F]", "Prism selected by another top IC manufacturer for 3D NAND advanced nodes (1 Mar 2021)", "customer (unnamed memory)", "FQ1 FY2021", "Mar 2021",
      "Nova press release 1 Mar 2021", "2021-03-01", "2026-11-21_nova_pr-prism-additional-manufacturer.html", "another top integrated circuits (IC) manufacturer recently selected the Nova Prism platform for its 3D NAND advanced nodes"),
    R("[F]", "Prism 2 selected by a leading foundry for advanced-packaging steps (29 Aug 2023)", "customer (unnamed foundry)", "FQ3 FY2023", "Aug 2023",
      "Nova press release 29 Aug 2023", "2023-08-29", "2026-11-21_nova_pr-prism2-foundry-packaging.html", "one of the world's leading foundry manufacturers recently selected Nova Prism 2 for its advanced packaging process steps"),
    R("[F]", "Prism 2 qualified by a leading logic manufacturer for backside power delivery; multiple-tool order (10 Oct 2024)", "customer (unnamed logic)", "FQ4 FY2024", "Oct 2024",
      "Nova press release 10 Oct 2024", "2024-10-10", "2026-11-21_nova_pr-prism2-logic.html", "qualified Nova Prism 2 to address backside power delivery applications in front-end processes of advanced logic nodes"),
    R("[F]", "Prism 2 key applications per brochure: 3D NAND, DRAM active area to capacitors, TSV, deep trenches, FinFET, GAA modules", "applications", "n/a", "brochure 2023-2025",
      "Nova dimensional metrology brochure (uploaded Feb 2026)", "2026-02-01", DMD, "Key Application Challenges Addressed by Nova Prism"),
    R("[F]", "MMSR+: high-end stand-alone CD and thin-film platform for complex 2D/3D structures (multi-channel ellipsometry + normal-incidence reflectometry)", "application", "n/a", "page read 21 Nov 2026",
      "Nova website, Nova MMSR+ product page", "2026-11-21", "2026-11-21_nova_product-mmsr.html", "high-end standalone dimensional metrology platform targeted for critical dimensions (CD) and thin film measurements"),
    R("[F]", "VeloCD: stand-alone OCD for high productivity in logic and memory (dual measurement units)", "application", "n/a", "page read 21 Nov 2026",
      "Nova website, Nova VeloCD product page", "2026-11-21", "2026-11-21_nova_product-velocd.html", "optimized for high productivity in a wide range of Logic and Memory applications"),
    R("[F]", "T500 / T550: stand-alone engineering stations fully matched to the integrated fleet (recipe creation, redundancy)", "application", "n/a", "page read 21 Nov 2026",
      "Nova website, Nova T500 product page", "2026-11-21", "2026-11-21_nova_product-t500.html", "Used for recipe creation and as a redundancy tool"),
    # --- Sentronics / WMC ---
    R("[F]", "Sentronics (acquired Jan 2025) adds SemDex modular multi-sensor metrology: total thickness variation, bow & warp, topography, roughness, TSV; WLP and PLP; 150-300 mm", "applications", "FY2025", "Mar 2025",
      "Nova Investor Day 2025 presentation, slide 14", "2025-03-13", IDD, "Total Thickness Variation"),
    R("[F]", "WMC released 26 Aug 2025: adopted by a leading memory maker for HBM; orders from logic, advanced memory and power-device makers", "launch Aug 2025", "FQ3 FY2025", "Aug 2025",
      "Nova press release 26 Aug 2025", "2025-08-26", "2026-11-21_nova_pr-wmc-release.html", "The platform has already been adopted by one of the world's leading memory manufacturers for High Bandwidth Memory"),
    R("[C]", "WMC designated tool-of-record by a leading global foundry after a competitive evaluation (2 Jul 2026); deployments at several memory and foundry customers", "TOR (unnamed foundry; competitor unnamed)", "FQ3 FY2026", "Jul 2026",
      "Nova press release 2 Jul 2026 (PDF)", "2026-07-02", "2026-07-02_nova_wmc-update-pdf.pdf", "The selection followed a competitive evaluation, resulting in the Nova WMC", "", "no outside party confirms; competitor not named"),
    R("[S]", "WMC: more than 10 customers have ordered or completed acceptance (FQ3 FY2026 call)", ">10 customers", "FQ3 FY2026", "Nov 2026",
      "Third-party transcript of Nova Q3 2026 call", "2026-11-05", Q3T, "with more than 10 customers having placed orders or completing acceptance of the platform", "", "company statement"),
    R("[F]", "WMC applications per product page: thickness profile/TTV, bow, bonded-stack layer thickness, bonding eccentricity, CD/height of RDLs and bumps, die warpage", "applications", "n/a", "page read 21 Nov 2026",
      "Nova website, Nova WMC product page", "2026-11-21", "2026-11-21_nova_product-wmc.html", "including features like RDLs, bumps, and laser grooves"),
    # --- materials metrology ---
    R("[F]", "VeraFlex IV launched 2021: >$23M of materials-metrology orders from logic and foundry customers included the new VeraFlex IV (28 Jan 2021)", ">$23M", "FQ1 FY2021", "Jan 2021",
      "Nova press release 28 Jan 2021", "2021-01-28", "2021-01-28_nova_press-release-materials-metrology-orders.html", "The combined orders represent more than $23 million in revenue."),
    R("[F]", "VeraFlex IV selected by a leading multinational logic manufacturer (12 Oct 2021)", "customer (unnamed logic)", "FQ4 FY2021", "Oct 2021",
      "Nova press release 12 Oct 2021", "2021-10-12", "2021-10-12_nova_press-release-logic-selects-latest-materials-platform.html", "a leading multinational logic manufacturer recently selected the Nova VeraFlex IV"),
    R("[F]", "VeraFlex adopted by a leading analog / mixed-signal manufacturer; numerous tools delivered (7 Jul 2022)", "customer (unnamed analog)", "FQ3 FY2022", "Jul 2022",
      "Nova press release 7 Jul 2022", "2022-07-07", "2022-07-07_nova_press-release-analog-veraflex-orders.html", "a leading analog and mixed-signal device manufacturer recently adopted the Nova VeraFlex"),
    R("[F]", "Nova Fit machine learning for VeraFlex IV deployed at a customer for GAA (21 Nov 2024)", "1 customer (unnamed)", "FQ4 FY2024", "Nov 2024",
      "Nova press release 21 Nov 2024", "2024-11-21", "2024-11-21_nova_press-release-nova-fit-veraflex.html", "The solution has already been successfully deployed at a customer's site"),
    R("[S]", "XPS tools per fab reach up to 9 at leading memory customers; significant XPS order from a major memory customer (FQ3 FY2026 call)", "up to 9 per fab", "FQ3 FY2026", "Nov 2026",
      "Third-party transcript of Nova Q3 2026 call", "2026-11-05", Q3T, "which drives an increase in numbers of tools per fab, which reach up to nine", "", "company statement"),
    R("[F]", "Metrion (in-line SIMS) launched 8 Dec 2021; first revenue expected Q4 2021", "launch Dec 2021", "FQ4 FY2021", "Dec 2021",
      "Nova press release 8 Dec 2021", "2021-12-08", "2026-11-21_nova_pr-metrion-introduced.html", "announced today the launch of Nova Metrion"),
    R("[F]", "Metrion selected by a leading logic manufacturer under a long-term collaboration covering the full materials suite (12 Jul 2022)", "customer (unnamed logic)", "FQ3 FY2022", "Jul 2022",
      "Nova press release 12 Jul 2022", "2022-07-12", "2026-11-21_nova_pr-metrion-advanced-logic.html", "a leading logic manufacturer recently selected Nova Metrion"),
    R("[F]", "Second-generation Metrion available for shipment (16 Jan 2024)", "launch Jan 2024", "FQ1 FY2024", "Jan 2024",
      "Nova press release 16 Jan 2024", "2024-01-16", "2026-11-21_nova_pr-metrion-second-generation.html", "announces the second-generation Nova Metrion"),
    R("[F]", "Metrion selected by a leading memory maker for advanced DRAM R&D and DRAM and NAND HVM lines (8 Jan 2025)", "customer (unnamed memory)", "FQ1 FY2025", "Jan 2025",
      "Nova press release 8 Jan 2025", "2025-01-08", "2026-11-21_nova_pr-metrion-leading-memory.html", "selected the Nova Metrion"),
    R("[F]", "Metrion purchased by global memory and logic leaders for GAA and advanced DRAM (29 Jan 2026)", "customers (unnamed)", "FQ1 FY2026", "Jan 2026",
      "Nova press release 29 Jan 2026", "2026-01-29", "2026-01-29_nova_press-release-metrion-two-manufacturers.html", "The platform was purchased for Gate-All-Around (GAA) and advanced DRAM device production"),
    R("[S]", "Metrion: 4 of 5 target customers adopting (HVM proliferation or evaluation); fifth hoped for 2027 (FQ3 FY2026 call)", "4 of 5", "FQ3 FY2026", "Nov 2026",
      "Third-party transcript of Nova Q3 2026 call (TradingKey)", "2026-11-05", "2026-11-05_tradingkey_transcript-Q3-2026-call.html", "We do see right now 4 out of the 5 already adopting the Metrion", "", "company statement; qualification status mixed"),
    R("[F]", "Elipson additional order for HVM of advanced memory after R&D use (30 Sep 2021)", "customer (unnamed memory)", "FQ3 FY2021", "Sep 2021",
      "Nova press release 30 Sep 2021", "2021-09-30", "2026-11-21_nova_pr-elipson-advanced-memory.html", "recently ordered an additional Elipson platform for high-volume manufacturing of advanced memory devices"),
    R("[F]", "Elipson selected by a leading global logic manufacturer (20 Dec 2022)", "customer (unnamed logic)", "FQ4 FY2022", "Dec 2022",
      "Nova press release 20 Dec 2022", "2022-12-20", "2026-11-21_nova_pr-elipson-leading-logic.html", "a leading global logic manufacturer recently selected Nova Elipson"),
    R("[C]", "Elipson tool-of-record at a leading global foundry for GAA HVM; several tools delivered (6 Oct 2025)", "TOR (unnamed foundry)", "FQ4 FY2025", "Oct 2025",
      "Nova press release 6 Oct 2025", "2025-10-06", "2025-10-06_nova_press-release-elipson-foundry-GAA.html", "has been selected as Tool of Record by a leading global foundry customer for advanced Gate-All-Around (GAA) manufacturing processes", "", "no outside confirmation"),
    R("[C]", "Investor Day 2025: VeraFlex 'Industry standard ... Market leader'; Metrion and Elipson 'Each adopted by 3 top-5 IC manufacturers'", "3 of top 5 each", "FY2025", "Mar 2025",
      "Nova Investor Day 2025 presentation, slide 42", "2025-03-13", IDD, "Each adopted by 3 top-5 IC manufacturers"),
    # --- chemical metrology ---
    R("[F]", "ancosys Ancolyzer front-end version selected by five leading front-end fabs incl. a world-leading foundry (9 Feb 2022)", "5 customers (unnamed)", "FQ1 FY2022", "Feb 2022",
      "Nova press release 9 Feb 2022", "2022-02-09", "2026-11-21_nova_pr-ancosys-front-end-customer.html", "has been selected by five leading front-end wafer manufacturers, including a world-leading foundry"),
    R("[S]", "AncoScene completed acceptance and release to HVM at a leading foundry in FQ3 FY2026; KLA named as the only front-end chemical-metrology competitor", "HVM release", "FQ3 FY2026", "Nov 2026",
      "Third-party transcript of Nova Q3 2026 call", "2026-11-05", Q3T, "We have one competitor in the chemical metrology front-end space, which is KLA", "", "company statement"),
    R("[F]", "Chemical metrology capacity doubled with new Bad Urach (Germany) site (28 Jan 2025)", "2x capacity", "FQ1 FY2025", "Jan 2025",
      "Nova press release 28 Jan 2025", "2025-01-28", "2026-11-21_nova_pr-chemical-capacity-germany.html", "Doubling the capacity of Nova's Chemical Metrology Division"),
    # --- named customer collaborations ---
    R("[F]", "Samsung R&D co-authored two SPIE 2024 papers with Nova: spectral interferometry for HAR 3D NAND, and Raman (27 Feb 2024)", "Samsung (named)", "FQ1 FY2024", "Feb 2024",
      "Nova press release 27 Feb 2024", "2024-02-27", "2024-02-26_nova_pr-samsung-nova-joint-research-SPIE-2024.html", "it will publish two co-authored papers with Samsung R&D Center research at SPIE Advanced Lithography 2024"),
    R("[F]", "Samsung + Nova paper on chalcogenide (OTS) layer thickness via spectral interferometry, Raman and hybrid ML won SPIE 'Collaborations in Metrology' award (18 Mar 2025)", "Samsung (named)", "FQ1 FY2025", "Mar 2025",
      "Nova press release 18 Mar 2025", "2025-03-18", "2026-11-21_nova_pr-samsung-nova-ukraintsev-award.html", "has been selected as the winner of the Vladimir Ukraintsev Award"),
    R("[F]", "Division structure since ancosys: three full P&L divisions (dimensional, materials, chemical)", "3 divisions", "FY2022", "Sep 2022",
      "Nova Investor Day 2022 transcript (company PDF)", "2022-09-21", "2022-09-21_nova_investor-day-2022-transcript.pdf", "With the integration of ancosys, Nova now operates with 3 full P&L divisions"),
    R("[S]", "Revenue mix by division (Investor Day 2025 Q&A): ~40-50% dimensional, ~30-40% materials, ~10-20% chemical; ratio expected to stay intact through 2027", "40-50 / 30-40 / 10-20", "FY2024-FY2027", "Mar 2025",
      "Third-party transcript of Nova Investor Day 2025", "2025-03-13", IDT, "We currently have about 40%-50% coming out of the dimensional metrology, about 30%-40% from material, and about 10%-20% from chemical.", "", "company statement; only division split found"),
    R("[F]", "Investor Day 2025 slide on Sentronics presents Nova WMC as the 'next-gen platform' of the acquired line (WMC then released Aug 2025)", "WMC = next-gen Sentronics platform", "FY2025", "Mar 2025",
      "Nova Investor Day 2025 presentation, slide 14", "2025-03-13", IDD, "Coming soon: next-gen platform"),
]

Q3 = [
    R("[F]", "Nova describes itself as delivering optical, X-ray, SIMS and chemical analysis technology", "X-ray in portfolio", "FY2025", "as of Feb 2026",
      "Nova Form 20-F FY2025, Item 4B", "2026-02-17", F20, "Nova's capability to deliver innovative Optical, X-ray, SIMS and Chemical analysis technology solutions"),
    R("[F]", "X-ray entered Nova via the April 2015 acquisition of ReVera (stand-alone thin-film and composition metrology)", "acquisition 2015", "FY2015", "Apr 2015",
      "Nova Form 20-F FY2025, Item 4A", "2026-02-17", F20, "In April 2015, we acquired ReVera Inc., a privately held company headquartered in Santa Clara, California"),
    R("[F]", "20-F names Onto and KLA as main competitors plus process-tool makers' in-situ sensors and Chinese entrants; Rigaku is not mentioned", "competitors", "FY2025", "as of Feb 2026",
      "Nova Form 20-F FY2025, risk factors", "2026-02-17", F20, "We compete mainly with Onto Innovation Inc., and KLA Corp.", "", "word 'Rigaku' NOT FOUND in 20-F FY2025 (findpage)"),
    R("[S]", "Q1 2026 call (14 May 2026), asked about peers' X-ray opportunities: CEO says Nova's strategy 'taps into hybrid metrology' with homegrown optical and X-ray", "statement", "FQ1 FY2026", "May 2026",
      "Third-party transcript of Nova Q1 2026 call", "2026-05-14", T("2026-05-14", "Q1-2026-call"), "We do have a broad portfolio of both optical and X-ray, both homegrown.", "", "first Nova remark on X-ray after the 21 Apr 2026 Rigaku-Onto notice; Onto and Rigaku not named"),
    R("[S]", "Same answer cites joint papers: Samsung (hybrid OCD + Raman) and IBM (hybrid OCD with X-ray and machine learning)", "statement", "FQ1 FY2026", "May 2026",
      "Third-party transcript of Nova Q1 2026 call", "2026-05-14", T("2026-05-14", "Q1-2026-call"), "plus machine learning with IBM on hybrid OCD with X-ray and machine learning", "", "company statement"),
    R("[S]", "Same answer: emerging XPS and materials-metrology competition from a local Chinese vendor and others", "statement", "FQ1 FY2026", "May 2026",
      "Third-party transcript of Nova Q1 2026 call", "2026-05-14", T("2026-05-14", "Q1-2026-call"), "We are also seeing emerging XPS and material metrology competition.", "", "company statement"),
    R("[S]", "BofA conference (3 Jun 2026): Nova is 'currently a sole source' in X-ray (XPS) metrology, expects competition 'probably next year'; keeps investing in XPS and XRF", "statement", "FQ2 FY2026", "Jun 2026",
      "Third-party transcript, BofA Global Technology Conference 2026", "2026-06-03", T("2026-06-03", "bofa-tech-conf-2026"), "We're currently a sole source, but we expect competition to come.", "", "company claim reported by transcript"),
    R("[S]", "Evercore conference (3 Jun 2026): X-ray tools have the longest lead times in Nova's portfolio", "statement", "FQ2 FY2026", "Jun 2026",
      "Third-party transcript, Evercore TMT Conference 2026", "2026-06-03", T("2026-06-03", "evercore-tmt-conf-2026"), "The longer lead times are the X-ray ones.", "", "company statement"),
    R("[S]", "Q3 2026 call: expected competition (2H 2027) is 'centered around XPS only'; Nova does not sell XRF as a stand-alone tool", "statement", "FQ3 FY2026", "Nov 2026",
      "Third-party transcript of Nova Q3 2026 call (TradingKey)", "2026-11-05", "2026-11-05_tradingkey_transcript-Q3-2026-call.html", "We are not selling, by the way, XRF as a stand-alone tool.", "", "company statement"),
    R("[S]", "Citi conference (4 Sep 2025, before the alliance): 'very few companies possess both optical and X-ray'; X-ray used for composition, depth profile, ultra-thin film thickness", "statement", "FQ3 FY2025", "Sep 2025",
      "Third-party transcript, Citi TMT Conference 2025", "2025-09-04", T("2025-09-04", "citi-tmt-conf-2025"), "very few companies, by the way, possess both optical and X-ray in general, and definitely in our space", "", "company statement"),
    R("[I]", "No Nova statement naming Onto-Rigaku, Rigaku, CD-SAXS or T-SAXS found in any 2026 call or conference transcript (Jan-Nov 2026) or in Nova releases; the closest is the May 2026 hybrid-metrology answer", "absence", "FY2026", "Jan-Nov 2026",
      "grep of 9 transcripts dated 14 Jan-5 Nov 2026 and Nova releases saved", "2026-11-21", "", "", "Medium", "absence of evidence in third-party transcripts; Nova may have commented in unrecorded meetings"),
    R("[I]", "No Nova product, programme, partnership or acquisition in X-ray CD (SAXS) found in 20-F FY2023-FY2025, releases or calls; Nova's X-ray activity is XPS plus integrated low-energy XRF for film composition and thickness", "none found", "FY2023-FY2026", "2023-2026",
      "20-F FY2023-FY2025; releases; transcripts", "2026-11-21", "", "", "Medium", "see XR.csv for website/paper checks by the X-ray module"),
]

Q5 = [
    R("[S]", "Packaging-related business ~10% of overall revenue in 2023 (Q1 2024 call)", "~10% of total revenue", "FY2023", "Jan-Dec 2023",
      "Third-party transcript of Nova Q1 2024 call", "2024-05-09", T("2024-05-09", "Q1-2024-call"), "packaging-related business was about 10% of our overall revenue", "", "base is total revenue, later figures use product revenue"),
    R("[S]", "AP revenue 'more than doubled' in 2024 to 15% of product revenue (Q4 2024 call)", "15% of product revenue", "FY2024", "Jan-Dec 2024",
      "Third-party transcript of Nova Q4 2024 call", "2025-02-13", T("2025-02-13", "Q4-2024-call"), "Our advanced packaging revenue more than doubled this year, reaching 15% of product revenue", "", "company statement"),
    R("[I]", "Inconsistency: 10% of 2023 total revenue = ~$51.8M; 15% of 2024 product revenue = ~$80.8M, i.e. +56%, not 'more than doubled'; doubling fits only if the 2023 base was ~10% of product revenue (~$40.5M)", "+56% vs +100%", "FY2023-FY2024", "2023-2024",
      "inputs: FY2023 revenue 517,922 and products 405,037; FY2024 products 538,350 (20-F FY2025)", "2026-11-21", "", "", "Medium", "management shares are rounded and the base switches between total and product revenue; flag for reviewer"),
    R("[S]", "2027 target: AP to become 20% of product sales, split between logic AP and HBM (Investor Day 2025)", "20% by 2027", "FY2027 target", "Mar 2025",
      "Third-party transcript of Nova Investor Day 2025", "2025-03-13", IDT, "By 2027, we expect it to become 20% of our product sales", "", "reached ~20% in 2025 per Q4 2025 call (A1)"),
    R("[S]", "Chemical metrology was about half of advanced-packaging revenue (Q2 2024 call)", "~50% of AP revenue", "FQ2 FY2024", "Aug 2024",
      "Third-party transcript of Nova Q2 2024 call", "2024-08-08", T("2024-08-08", "Q2-2024-call"), "So Chemical Metrology is about half of our packaging or Advanced Packaging and advanced packaging revenue.", "", "company statement"),
    R("[S]", "About half of Prism 2 record bookings came from AP processes such as TSV (Q2 2024 call)", "~50% of Prism 2 bookings", "FQ2 FY2024", "Aug 2024",
      "Third-party transcript of Nova Q2 2024 call", "2024-08-08", T("2024-08-08", "Q2-2024-call"), "Approximately half of Prism 2 record bookings stem from advanced packaging processes, such as through-silicon via", "", "company statement"),
    R("[F]", "Cu recess / dishing before hybrid bonding addressed by Prism; edge roll-off and bevel trim by OCD-based edge metrology; TTV, bow and warp by WMC (company blog; VLSI 2025 workshop material)", "tool mapping", "n/a", "page read 21 Nov 2026",
      "Nova blog 'Precision Metrology for Hybrid Bonding'", "2026-11-21", "2026-11-21_nova_blog-hybrid-bonding-metrology.html", "particularly copper recess or dishing, must be tightly controlled to avoid bonding defects"),
    R("[F]", "Plating-bath control for packaging: Ancolyzer = 'Market-leading chemical metrology platform for backend and advanced packaging' (company claim) and DMR metal replenishment", "tool mapping", "n/a", "page read 21 Nov 2026",
      "Nova website, Nova Ancolyzer product page", "2026-11-21", "2026-11-21_nova_product-ancolyzer.html", "Market-leading chemical metrology platform for backend and advanced packaging"),
    R("[S]", "Evercore (Jun 2026): AP applications TSV, RDL, topography and warpage; 'encouraging signs' in hybrid bonding", "statement", "FQ2 FY2026", "Jun 2026",
      "Third-party transcript, Evercore TMT Conference 2026", "2026-06-03", T("2026-06-03", "evercore-tmt-conf-2026"), "targeting advanced packaging in certain applications such as the TSVs, such as in the RDL, such in topography, and warpage", "", "company statement"),
    R("[S]", "Integrated metrology adopted by four of the top five advanced-packaging manufacturers (Q4 2024 call)", "4 of top 5", "FY2024", "Feb 2025",
      "Third-party transcript of Nova Q4 2024 call", "2025-02-13", T("2025-02-13", "Q4-2024-call"), "Our integrated metrology solutions have been adopted by four of the top five advanced packaging manufacturers", "", "company claim; no outside confirmation"),
    R("[S]", "Cantor (Mar 2026): 'a couple of customers' already adopted WMC as tool of record", "2 TOR (claim)", "FQ1 FY2026", "Mar 2026",
      "Third-party transcript, Cantor conference 2026", "2026-03-10", T("2026-03-10", "cantor-conf-2026"), "already a couple of customers adopted that as a tool of record", "", "company claim"),
    R("[F]", "20-F: Sentronics puts Nova 'in direct competition with companies such as Merck and Camtek' in WLP and specialty", "competitors named", "FY2025", "as of Feb 2026",
      "Nova Form 20-F FY2025, risk factors", "2026-02-17", F20, "positions us in direct competition with companies such as Merck and Camtek"),
    R("[S]", "Needham (Jan 2026): CEO maps competition - integrated metrology vs Onto; stand-alone OCD vs Onto and KLA; chemical vs KLA (Nova 'lion's share' backend, KLA majority front end); Camtek via FRT", "statement", "FQ1 FY2026", "Jan 2026",
      "Third-party transcript, Needham Growth Conference 2026", "2026-01-14", T("2026-01-14", "needham-conf-2026"), "On the optical CD standalone, we're competing directly with Onto and KLA.", "", "company statement"),
    R("[S]", "New cleanroom extension 'enables us to triple our production capacity for advanced packaging optical metrology' (Q3 2025 call)", "3x capacity", "FQ3 FY2025", "Nov 2025",
      "Third-party transcript of Nova Q3 2025 call", "2025-11-06", T("2025-11-06", "Q3-2025-call"), "enables us to triple our production capacity for advanced packaging optical metrology solutions", "", "company statement"),
    R("[I]", "No non-vendor source (customer, trade press, analyst) found that documents a specific Nova packaging win against KLA, Onto, Camtek or Bruker; every win in hand is company-sourced and the losing vendor is never named", "none found", "FY2023-FY2026", "2023-2026",
      "web searches 21 Nov 2026 (trade press, customer releases); Nova releases", "2026-11-21", "", "", "Medium", "SEMICON Taiwan 2026 deck refused the script; trade press (TheElec, DigiTimes, Yole) not found or paywalled"),
]

Q6 = [
    R("[F]", "Integrated systems (optical CD IM and chemical metrology) depend on PEMs selling process equipment that can integrate them", "dependence", "FY2025", "as of Feb 2026",
      "Nova Form 20-F FY2025, risk factors", "2026-02-17", F20, "Sales of such integrated systems, which include Optical CD integrated metrology and chemical metrology, depend upon the ability of PEMs"),
    R("[F]", "Some PEM agreements contain exclusivity provisions and limits on joint IP", "contract terms", "FY2025", "as of Feb 2026",
      "Nova Form 20-F FY2025, risk factors", "2026-02-17", F20, "some of our commercial agreements with PEMs also include limitations on the use of certain joint intellectual property"),
    R("[F]", "Until 2008 most products were sold to PEMs such as Applied Materials and Ebara; since then substantially all sold directly to chipmakers", "direct since 2008", "FY2025", "as of Feb 2026",
      "Nova Form 20-F FY2025, Item 4A", "2026-02-17", F20, "Until 2008, most of our products were sold to PEMs such as Applied Materials, Inc. and Ebara Corp."),
    R("[F]", "Process-equipment makers (ASML, Lam Research, Applied Materials) are also named as competitors through in-situ sensors and metrology", "competitors", "FY2025", "as of Feb 2026",
      "Nova Form 20-F FY2025, risk factors", "2026-02-17", F20, "we compete with process equipment manufacturers, such as ASML Holdings N.V., LAM Research, and Applied Materials Inc."),
    R("[S]", "Trade item (11 Jan 2010): NovaScan integrated metrology available with Applied Materials, Lam Research and Ebara CMP and etch tools", "AMAT, Lam, Ebara (2010)", "FY2010", "Jan 2010",
      "AZoNano reproduction of Nova release (dated 11 Jan 2010)", "2010-01-11", "2026-11-21_azonano_news-nova-IM-etch-customers.html", "The NovaScan integrated metrology platform is available in conjunction with Applied Materials, Lam Research and Ebara Corporation CMP and Etch tools.", "", "16 years old; current partner list NOT DISCLOSED"),
    R("[S]", "Investor Day 2025: Nova claims market leadership in integrated metrology for CMP and #2 share in optical CD and film metrology", "#1 IM-CMP; #2 OCD/film (claim)", "FY2024", "Mar 2025",
      "Third-party transcript of Nova Investor Day 2025", "2025-03-13", IDT, "we are the market leader in integrated metrology for CMP and hold the second largest market share for optical CD and film metrology", "", "company claim; no third-party share figure retrieved"),
    R("[S]", "Q2 2025 call: one key competitor in integrated metrology, two in stand-alone OCD", "1 / 2 competitors", "FQ2 FY2025", "Aug 2025",
      "Third-party transcript of Nova Q2 2025 call", "2025-08-07", T("2025-08-07", "Q2-2025-call"), "We have one key competitor on the integrated metrology, and we're competing with two on the standalone OCD.", "", "company statement; Needham Jan 2026 names Onto in IM"),
    R("[S]", "Chemical metrology entered the qualified vendor list of a major OEM for front-end opportunities (Q1 2023 call)", "1 OEM (unnamed)", "FQ1 FY2023", "May 2023",
      "Third-party transcript of Nova Q1 2023 call", "2023-05-11", T("2023-05-11", "Q1-2023-call"), "We recently entered the qualified vendor list of a major OEM, setting the stage for new opportunities in the front end.", "", "company statement"),
    R("[S]", "Citi (Sep 2025): Gartner put Nova's share at 24.8% in 2024 (from ~20% in 2023), second to KLA at ~50% (market segment not named in the transcript)", "24.8%", "FY2024", "Jan-Dec 2024",
      "Third-party transcript, Citi TMT Conference 2025", "2025-09-04", T("2025-09-04", "citi-tmt-conf-2025"), "we have grown our market share from around 20% in 2023 to 24.8% in 2024", "", "Gartner report itself NOT RETRIEVED"),
    R("[I]", "Share of revenue that depends on PEMs: NOT DISCLOSED; integrated-metrology revenue is not reported separately; current PEM partners are not named in 20-F FY2023-FY2025", "NOT DISCLOSED", "FY2023-FY2025", "2023-2025",
      "20-F FY2023-FY2025; releases; transcripts", "2026-11-21", "", "", "High", "NOT DISCLOSED (read: 20-F FY2025 Items 3D, 4B, Note 16; Q4 FY2025-Q3 FY2026 releases)"),
]

for name, lst in (("Q1", Q1), ("Q3", Q3), ("Q5", Q5), ("Q6", Q6)):
    for i, r in enumerate(lst, 1):
        r["id"] = f"{name}-{i:03d}"
    write(os.path.join(PARTS, f"{name}.csv"), lst)
