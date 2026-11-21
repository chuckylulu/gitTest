"""Builds research/out/comet/parts/RV.csv; checks every quote against the local text before writing."""
import csv, os, re, sys

ROOT = "/home/user/gitTest"
SRC = "research/sources/comet/"
MAN = os.path.join(ROOT, SRC, "_manifest.csv")
urls = {}
for r in csv.DictReader(open(MAN)):
    if r["status"] == "RETRIEVED":
        urls[r["local_file"]] = r["url"]


def norm(s):
    s = s.replace("­", "").replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"').replace("–", "-").replace("—", "-")
    s = re.sub(r"\s+", " ", s).strip().lower()
    return s


def pages_of(lf):
    stem = os.path.splitext(os.path.basename(lf))[0]
    return open(os.path.join(ROOT, SRC, "_text", stem + ".txt"), encoding="utf-8", errors="replace").read().split("\f")


H = ["id", "tag", "claim", "value", "unit", "period_fiscal", "period_calendar", "document", "date",
     "page_or_section", "url", "local_file", "quote", "confidence", "note"]
rows = []

CA20 = "2026-11-21_comet_yxlon-product-page-CA20.html"
CA23 = "2026-11-21_comet_yxlon-news-CA20-launch-2023.html"
CA24 = "2026-11-21_comet_yxlon-news-CA20-launch-2024.html"
NLX = "2026-11-21_zeiss_product-page-NLX.html"
ZW = "2026-10-12_zeiss_press-release-SEMICON-West-2026-NLX.html"
ZT = "2026-09-02_zeiss_press-release-SEMICON-Taiwan-2026.html"
ZK = "2026-07-10_zeiss_press-release-innovation-center-korea.html"
ZP = "2026-11-21_zeiss_page-advanced-semiconductor-packaging.html"
ZV = "2026-11-21_zeiss_press-release-Versa-2026.html"
RP = "2026-11-21_rigaku_page-advanced-packaging-metrology.html"
RO = "2025-12-17_rigaku_press-release-ONYX-3200.html"
RE = "2026-11-21_rigaku_event-page-ECTC-2026.html"
RX = "2026-11-21_rigaku_product-page-XTRAIA-XT.html"
RH = "2026-08-07_rigaku_H1-2026-results-filing.pdf"
OR = "2026-04-20_onto_press-release-Rigaku-partnership-nasdaq-copy.html"
NW25 = "2025-10-01_nordson_press-release-SEMICON-West-2025-pdf.pdf"
NW26 = "2026-11-21_iconnect007_article-Nordson-SEMICON-West-2026.html"
NHBM = "2026-11-21_semiengineering_article-Nordson-HBM-3D-xray.html"
NQ4 = "2025-12-10_nordson_press-release-Q4-FY2025-results-bizwire-copy.html"
SE24 = "2026-11-21_semiengineering_article-xray-essential-advanced-packaging.html"
SE22 = "2026-11-21_semiengineering_article-HBM-nanosheet-xray-fab-use.html"
BM = "2026-11-21_bruker_page-automated-xray-metrology.html"
BX = "2026-11-21_bruker_product-page-X200-en.html"
BW = "2025-06-24_bruker_press-release-advanced-packaging-WLI-order.pdf"
SI = "2024-07-01_sigray_IEEE-EPS-SCV-presentation-2024-07.pdf"
SA = "2024-08-01_sigray_AVS-NCCAVS-presentation-2024-08.pdf"
SQX = "2026-11-21_sigray_distributor-page-Apex-XCT-QD.html"
SQH = "2026-11-21_sigray_distributor-page-Apex-Hybrid-QD.html"
SWP = "2025-11-10_sigray_Apex-Hybrid-white-paper.pdf"
OM = "2026-11-21_omron_product-page-VT-X950.html"
OMEU = "2026-11-21_omron_news-VT-X950-EU.html"
OMD = "2026-11-21_dempa_article-Omron-VT-X950.html"
OMM = "2024-12-20_monoist_article-Omron-VT-X950-SEMICON-Japan-2024.html"
VI = "2026-11-21_viscom_product-page-iX7059-One.html"
SEC1 = "2026-02-04_asiae_article-SEC-Micron-HBM-xray-order.html"
SEC2 = "2026-05-21_asiae_article-SEC-growth-strategy.html"
SEC3 = "2026-11-10_asiae_article-SEC-Micron-Singapore-order-ko.html"
SEC4 = "2026-11-21_technews_article-SEC-inline-HBM-TGV.html"
SEC5 = "2026-09-22_economist-kr_article-SEC-inline-HBM.html"
SEC6 = "2026-11-21_sec-distributor-renex_distributor-page-X-EYE-NF120.html"
SEC7 = "2026-01-16_asiae_article-SEC-NDR-inline.html"
XA = "2026-02-09_koreadaily_article-XAVIS-SEMICON-Korea-2026.html"
UA = "2026-04-17_unicomp_disclosure-AN202604171821302692.pdf"


def add(tag, claim, value, unit, doc, date, sect, lf, quote, conf, note="", pf="n/a", pc="n/a", url=None):
    rows.append(dict(tag=tag, claim=claim, value=value, unit=unit, period_fiscal=pf, period_calendar=pc,
                     document=doc, date=date, page_or_section=sect, local_file=(SRC + lf) if lf else "",
                     url=url or urls.get(SRC + lf, ""), quote=quote, confidence=conf, note=note))


# ---------------- CA20 reference row (Comet's own page; XS agent owns the full CA20 profile)
add("[C]", "CA20 (Comet Yxlon) reference: stated defect size detectable", "<1", "um", "Comet Yxlon CA20 product page", "2026-11-21", "Product header", CA20,
    "Defect size: <1 µm, <50 µm, <1 mm", "High", "Reference row for comparison table; XS agent covers CA20 in full")
add("[F]", "CA20 first presented at productronica / SEMICON Europa, 15 Nov 2023, with 3D resolution below 1 um", "2023-11-15", "date", "Comet Yxlon news: CA20 launch 2023", "2023-11-15", "News body", CA23,
    "Three-dimensional X-ray images with a resolution of less than 1 µm can reliably identify typical defects in 3D IC solder connections", "High", "", "FY2023", "Nov 2023")
add("[F]", "Next-generation CA20 (fully automated, fab version) officially launched at SEMICON Europa 2024 (news dated 13 Nov 2024)", "2024-11-12", "date", "Comet Yxlon news: CA20 launch 2024", "2024-11-13", "News body", CA24,
    "Yesterday afternoon, Comet Yxlon officially launched the new solution with live demonstrations and invited guests at Semicon Europa.", "High", "News dated November 13, 2024; 'yesterday' = 12 Nov 2024", "FY2024", "Nov 2024")
add("[C]", "CA20 detector active area (field of view at detector)", "130 x 130", "mm", "Comet Yxlon CA20 product page", "2026-11-21", "Technical Data", CA20,
    "Detector Active Area 130 x 130 mm", "High", "Max. inspection envelope 435 mm (17 in) per same table")
add("[C]", "CA20 time claim: 3D insight into bumps/TSVs 'within minutes'; no per-wafer time stated", "within minutes", "text", "Comet Yxlon CA20 product page", "2026-11-21", "Highlights", CA20,
    "Non-destructive technology for three-dimensional insights into solder bumps or TSVs within minutes", "High", "Time per wafer NOT DISCLOSED on page")
add("[C]", "CA20 automation: fab version with fully automatic loader and ADC software", "fully automatic loader + ADC", "text", "Comet Yxlon CA20 product page", "2026-11-21", "Fully-automated inspection", CA20,
    "With a fully automatic loader and ADC software, the CA20 is designed to complement your production line", "High")
add("[C]", "CA20 wafer handling: Wafer Manager aligns wafers; 2.5D TSV software for wafer-level packaging", "Wafer Manager", "text", "Comet Yxlon CA20 product page", "2026-11-21", "Batch Manager / Wafer Manager", CA20,
    "our newly released Wafer Manager package automatically aligns wafers for inspection in seconds", "High", "Page does not state '300 mm' explicitly; envelope 435 mm")
add("[C]", "CA20 defect software: TSV Insights X 2.5D, fully automated TSV metrology and defect classification (KLARF output)", "TSV Insights X 2.5D", "text", "Comet Yxlon CA20 product page", "2026-11-21", "TSV Insights X 2.5D", CA20,
    "TSV Insights X 2.5D is our specialised software for the CA20 equipped with a fully-automated inspection package specifically designed for wafer level packaging.", "High")
add("[C]", "CA20 dose to memory: Dose Manager switches off X-ray at dose limit to protect flash and DRAM", "Dose Manager", "text", "Comet Yxlon CA20 product page", "2026-11-21", "Dose Manager", CA20,
    "To avoid damage to sensitive components such as flash and DRAM memories, it switches off the X-ray automatically once the dosage limit is reached.", "High")

# ---------------- ZEISS
add("[C]", "ZEISS NLX: in-line 3D X-ray laminography at 300 mm wafer level for micro bumps and TSVs in stacked dies", "300", "mm wafer", "ZEISS SMT NLX product page", "2026-11-21", "Intro", NLX,
    "ZEISS NLX introduces in-line 3D X-ray laminography at 300 mm wafer level", "High")
add("[C]", "ZEISS NLX-100: fully automated in-line configuration with EFEM wafer loading and fab automation integration", "NLX-100", "text", "ZEISS SMT NLX product page", "2026-11-21", "NLX-100", NLX,
    "It includes automated wafer loading via an Equipment Front End Module (EFEM), alignment functions and integration into fab automation systems.", "High")
add("[C]", "ZEISS NLX-100M: reduced automation, near-line / pilot line / engineering use", "NLX-100M", "text", "ZEISS SMT NLX product page", "2026-11-21", "NLX-100M", NLX,
    "It is particularly suitable for near-line inspection, pilot lines and engineering tasks", "High")
add("[C]", "ZEISS NLX dose: X-Guard dedicated shielding minimises X-ray exposure of sensitive wafer areas ('to avoid any damage'); no memory-specific dose figure", "X-Guard", "text", "ZEISS SMT NLX product page", "2026-11-21", "Imaging principle", NLX,
    "complements this concept with dedicated shielding that minimizes", "High", "Sentence continues: X-ray exposure in sensitive areas on the wafer to avoid any damage. No dose number or DRAM/HBM mention")
add("[C]", "ZEISS NLX metrology targets HBM alignment: shift, overlay, tilt; bump height/coplanarity", "HBM alignment", "text", "ZEISS SMT NLX product page", "2026-11-21", "Metrology section", NLX,
    "Precise measurements of shift, overlay, and tilt provide critical process control for the alignment of high-bandwidth memory (HBM)", "High")
add("[C]", "ZEISS NLX software: ZEISS INSPECT X-Ray for 3D metrology, defect inspection and recipes", "ZEISS INSPECT X-Ray", "text", "ZEISS SMT NLX product page", "2026-11-21", "Data evaluation, automation and AI", NLX,
    "Data evaluation on ZEISS NLX is powered by ZEISS INSPECT X-Ray, enabling 3D metrology, defect inspection and automated inspection flows in a single environment.", "High")
add("[C]", "ZEISS NLX AI-based segmentation of structures and defects in volume data", "AI segmentation", "text", "ZEISS SMT NLX product page", "2026-11-21", "Automation and AI-supported inspection", NLX,
    "AI-based routines within the platform automatically highlight and segment relevant structures and defects in the volume data.", "High", "Resolution, field of view and time per wafer/site: NOT DISCLOSED on page")
add("[F]", "ZEISS presented NLX at SEMICON West 2026 (release 12 Oct 2026) as 300 mm system for development and high-volume production", "2026-10-12", "date", "ZEISS SMT press release SEMICON West 2026", "2026-10-12", "Release body", ZW,
    "The system is designed for 300-millimeter wafers and supports both the development of new processes and high-volume production.", "High", "", "", "Oct 2026")
add("[F]", "ZEISS NLX shown at SEMICON Taiwan 2026 (2-4 Sep 2026)", "2026-09-02", "date", "ZEISS SMT press release SEMICON Taiwan 2026", "2026-09-02", "Release body", ZT,
    "Designed for 300 mm wafers, ZEISS NLX supports both process development and use in volume production.", "High", "", "", "Sep 2026")
add("[F]", "ZEISS opened Semiconductor Innovation Center in Yongin, Korea (10 Jul 2026) with an NLX-100 in its cleanroom for customer evaluation", "2026-07-10", "date", "ZEISS SMT press release Innovation Center Korea", "2026-07-10", "Image caption", ZK,
    "Cleanroom at the ZEISS Semiconductor Innovation Center Yongin with NLX", "High", "Demo/evaluation tool, not a customer order; no NLX customer or order named in any ZEISS document read", "", "Jul 2026")
add("[C]", "ZEISS Xradia Versa (lab XRM): 30 um microbumps imaged at 0.8 um/voxel (failure analysis positioning)", "0.8", "um/voxel", "ZEISS Microscopy advanced semiconductor packaging page", "2026-11-21", "Image gallery", ZP,
    "Virtual cross section from same analysis highlights 30 µm microbumps imaged at 0.8 µm/voxel resolution.", "High")
add("[C]", "ZEISS Xradia Context microCT: package-on-package scan at 10 um/voxel, large field of view", "10", "um/voxel", "ZEISS Microscopy advanced semiconductor packaging page", "2026-11-21", "Image gallery", ZP,
    "Large field of view 3D X-ray scan of package-on-package (POP) from a smartphone main control board imaged at 10 µm/voxel.", "High")
add("[F]", "ZEISS introduced VersaXRM 5 Insight hybrid XRM/microCT (release 14 Sep 2026); lab tool", "2026-09-14", "date", "ZEISS Microscopy press release VersaXRM 5 Insight", "2026-09-14", "Release body", ZV,
    "ZEISS today introduced ZEISS VersaXRM 5 Insight, a hybrid 3D X-ray microscope", "High", "File saved with retrieval date in name; release dated 14 September 2026", "", "Sep 2026")
add("[C]", "VersaXRM 5 Insight example: 5G modem package bump scan at 0.8 um/voxel took ~1.5 hours", "1.5", "hours", "ZEISS Microscopy press release VersaXRM 5 Insight", "2026-09-14", "Image caption", ZV,
    "acquired at 0.8 μm / voxel using a 4x objective (~1.5 hours)", "High", "Shows lab XRM scan time scale, not a fab throughput")

# ---------------- Rigaku
add("[C]", "Rigaku: in-line X-ray imaging for micro-bump/TSV defect detection is under development (no product name, no launch)", "in development", "text", "Rigaku Advanced Packaging Metrology page", "2026-11-21", "TSV (Through-silicon via) inspection", RP,
    "Rigaku is developing inline X-ray imaging solutions for automated defect detection in micro-bumps and TSVs, supporting high-throughput advanced packaging production.", "High", "No product named 'XHENA' found; see premise corrections")
add("[C]", "Rigaku packaging portfolio is thickness/composition metrology (XRF/hybrid) across ~100 nm to 100 um structures", "~100 nm to 100 um", "range", "Rigaku Advanced Packaging Metrology page", "2026-11-21", "Advanced Packaging Metrology", RP,
    "Rigaku delivers X-ray metrology solutions engineered to characterize thickness, composition, and structural integrity across packaging structures from ~100 nm to 100 µm.", "High")
add("[F]", "Rigaku launched ONYX 3200 (17 Dec 2025): film thickness, composition and bump metrology for wafer-level processes", "2025-12-17", "date", "Rigaku press release ONYX 3200", "2025-12-17", "Release body", RO,
    "a new semiconductor metrology system to measure film thickness, composition and bump* structures for wafer-level processes", "High", "", "", "Dec 2025")
add("[C]", "ONYX 3200 is optical 3D confocal scanner plus XRF, not transmission X-ray imaging/CT", "optical + XRF", "text", "Rigaku press release ONYX 3200", "2025-12-17", "Features of the ONYX 3200", RO,
    "integrates an optical scanner to capture the overall bump shape and total height and a fluorescent X-ray detector", "High")
add("[C]", "Rigaku shipped an initial ONYX 3200 to a major global foundry for an advanced packaging line", "1", "system", "Rigaku press release ONYX 3200", "2025-12-17", "Market outlook", RO,
    "Rigaku has shipped an initial ONYX 3200 system to a major global foundry for deployment in an advanced packaging line", "High", "Customer not named")
add("[C]", "Rigaku ONYX 3200 sales target JPY 1.5bn in FY2026, JPY 3bn in FY2027", "1.5", "JPY bn", "Rigaku press release ONYX 3200", "2025-12-17", "Market outlook", RO,
    "The company targets JPY 1.5 billion in ONYX 3200 sales in FY2026, with plans to double to JPY 3 billion in FY2027", "High", "Rigaku Holdings FY = calendar year", "FY2026", "Jan-Dec 2026")
add("[C]", "Rigaku at ECTC 2026 listed its packaging X-ray techniques: XRR, HRXRD, TXRF, CD-SAXS, X-ray topography (no CT/laminography)", "5 techniques", "count", "Rigaku ECTC 2026 event page", "2026-11-21", "Event description", RE,
    "Our portfolio of X-ray techniques, including XRR, HRXRD, TXRF, CD-SAXS, and X-ray topography", "High")
add("[C]", "Rigaku XTRAIA XT is in-line X-ray topography for crystallographic wafer defects, not package interconnect inspection", "XTRAIA XT", "text", "Rigaku XTRAIA XT product page", "2026-11-21", "Product overview", RX,
    "designed for in-line detection of crystallographic defects across wafers and epitaxial layer stacks", "High")
add("[F]", "Rigaku H1 2026 (Jan-Jun 2026): semiconductor process control instruments revenue +18.2% YoY; filing does not mention X-ray imaging for packaging", "18.2", "% YoY", "Rigaku Holdings H1 2026 summary of results (English translation)", "2026-08-07", "p5", RH,
    "In the semiconductor process control instruments business, revenue increased by 18.2% year on year to", "High", "Revenue JPY 12,791m per same sentence", "H1 FY2026", "Jan-Jun 2026")
add("[F]", "Onto Innovation agreed to buy 27% of Rigaku from a Carlyle affiliate (release 20 Apr 2026); collaboration is CD-SAXS with Ai Diffract, not imaging", "27", "% stake", "Onto Innovation press release (Nasdaq copy)", "2026-04-20", "Release body", OR,
    "to acquire 27% of the outstanding common stock of Rigaku", "High", "Closing reported Aug 2026 by search leads only (not read)", "", "Apr 2026")
add("[C]", "Onto/Rigaku joint CD-SAXS offering selected by two customers", "2", "customers", "Onto Innovation press release (Nasdaq copy)", "2026-04-20", "Release body", OR,
    "This new offering has already been selected by two key customers", "High", "CD-SAXS metrology, not 3D X-ray inspection of interconnects")

# ---------------- Nordson
add("[C]", "Nordson XM8000 Automated X-ray Metrology: 2D/2.5D/3D of micron-scale features for CoWoS, TSVs, 2.5/3D IC, wafer bumps", "XM8000", "text", "Nordson T&I release SEMICON West 2025 (PDF)", "2025-09", "p2", NW25,
    "applications such as CoWoS, TSVs, 2.5 and 3D IC packaging and wafer bumps.", "High", "PDF metadata date 2025-10-01; release text says September 2025", "", "Sep 2025")
add("[C]", "Nordson XM8000 positioned for high-throughput metrology and defect review of optically hidden features", "XM8000", "text", "Nordson T&I release SEMICON West 2025 (PDF)", "2025-09", "p2", NW25,
    "The system is designed for high-throughput metrology and defect review for optically hidden features, including voiding, fill levels, overlay and critical dimensions", "High")
add("[C]", "Nordson XM8000Pro (SEMICON West 2026): sub-micron 3D reconstruction for wafer- and panel-level packaging at 'production-speed throughput'", "sub-micron", "text", "Nordson T&I release as reproduced by I-Connect007", "2026-09-21", "Article body", NW26,
    "delivers sub-micron 3D reconstruction with unprecedented imaging fidelity and production-speed throughput", "High", "Company text on trade site; nordson.com product page refused (403)", "", "Sep 2026")
add("[C]", "Nordson Dynamic Planar CT (AXI) for flip-chip and micro-bump inspection, claimed lower radiation exposure", "Dynamic Planar CT", "text", "Nordson T&I release as reproduced by I-Connect007", "2026-09-21", "Article body", NW26,
    "improving throughput while reducing radiation exposure. It is particularly effective for semiconductor applications such as flip-chip and micro-bump inspection.", "High", "No dose figure")
add("[C]", "Nordson (author Christopher Rand) recommends Micro CT for FA and X-Plane Pro limited-angle 3D for production HBM inspection", "X-Plane Pro", "text", "Semiconductor Engineering (Nordson-authored blog)", "2026-06-09", "Article body", NHBM,
    "X-Plane Pro is designed to deliver limited-angle 3D imaging for larger samples, making it an excellent choice for high-throughput environments.", "High", "Same text as Nordson blog 6 May 2026 (nordson.com refused 403)")
add("[F]", "Nordson FQ4 FY2025 (Aug-Oct 2025): ATS sales -4%; fewer deliveries of test and inspection systems, particularly x-ray", "-4", "% YoY ATS sales", "Nordson Q4 FY2025 results release (Business Wire copy)", "2025-12-10", "Segment results", NQ4,
    "Ongoing sales strength in electronics dispense systems was more than offset by fewer deliveries of test and inspection systems, particularly x-ray systems.", "High", "Nordson FY ends 31 Oct", "FQ4 FY2025", "Aug-Oct 2025")
add("[S]", "Nordson's Perkins: full 3D reconstruction of every part is impractical in production", "n/a", "text", "Semiconductor Engineering: X-ray Inspection Becoming Essential In Advanced Packaging", "2024-07-09", "Article body", SE24,
    "We can't spend an hour inspecting every chip.", "Medium", "Third-party article quoting Nordson")
add("[S]", "Nordson AXM XM8000 Pro product page claims IC-Safe in-line inspection without radiation damage and 100 nm defect recognition", "IC-Safe", "text", "Nordson AXM XM8000 Pro product page (not saved)", "2026-11-21", "Search snippet", "",
    "", "Low", "NOT RETRIEVED: nordson.com returned 403 to fetch.py; wording seen only in web-search snippet; cannot be [F]/[C]",
    url="https://www.nordson.com/en/products/test-and-inspection-products/axm-xm8000-pro")

# ---------------- Bruker
add("[C]", "Bruker packaging X-ray metrology is uXRF for bump composition and UBM (not imaging)", "uXRF", "text", "Bruker automated X-ray metrology page", "2026-11-21", "Product list", BM,
    "Fully automated µXRF metrology platform to monitor bump composition and under bump metallization", "High")
add("[C]", "Bruker X200 product URL now resolves to an X-ray defect inspection overview (XRDI) page with no X200 content; packaging items listed are app notes", "n/a", "text", "Bruker X-ray defect inspection overview (redirect target of X200 URL)", "2026-11-21", "Semiconductor & Advanced Packaging Inspection", BX,
    "Support defect inspection and process monitoring in advanced semiconductor manufacturing.", "Medium", "og:url = x-ray-defect-inspection-systems.html; X200 status (current/discontinued) NOT DISCLOSED")
add("[S]", "Bruker X200 (earlier product page, per search snippet): in-line 2D X-ray, 12x18 mm FOV, 2.8 um/pixel, 1-2 full 300 mm wafers/hour", "1-2", "wafers/hour", "Bruker X200 product page (cached, not saved)", "2026-11-21", "Search snippet", "",
    "", "Low", "NOT RETRIEVED: X200 page now redirects; figures seen only in web-search snippet",
    url="https://www.bruker.com/en/products-and-solutions/semiconductor-solutions/x-ray-defect-inspection/x200.html")
add("[F]", "Bruker's AI advanced-packaging order (Jun 2025) was 27 InSight WLI optical systems, not X-ray", "27", "systems", "Bruker press release 24 Jun 2025", "2025-06-24", "p1", BW,
    "installation is part of a larger order from this semiconductor manufacturer for 27 Bruker optical metrology systems", "High", "", "FY2025", "Jun 2025")
add("[S]", "Bruker (Shulner) on HBM-on-logic AI packages driving early inspection need", "n/a", "text", "Semiconductor Engineering 2024-07-09", "2024-07-09", "Article body", SE24,
    "That adds complexity to each package and each process, leading to the need for early inspection and metrology of those chips.", "Medium")
add("[S]", "Bruker (Ryan, 2022): packaging X-ray at ~3 um resolution; CT 'too slow for production'", "3", "um", "Semiconductor Engineering interview 2022-03-08", "2022-03-08", "Interview", SE22,
    "On the packaging side, we’re down in 3µm resolution, which for back-end defects is fine.", "Medium", "Dated 2022; context only")
add("[S]", "Trade press: X-ray overexposure of HBM is a significant concern; dose must be managed", "n/a", "text", "Semiconductor Engineering 2024-07-09", "2024-07-09", "Article body", SE24,
    "With the increased sensitivities of HBM and other advanced semiconductor components, the danger of X-ray overexposure has become a significant concern.", "Medium", "Unattributed paragraph")

# ---------------- Sigray (Applied Materials)
add("[C]", "Sigray Apex XCT: 0.5 um resolution, <0.3 um voxel, laminography for large planar objects incl. 300 mm wafers", "0.5", "um", "Sigray presentation, IEEE SCV EPS 18 Jul 2024", "2024-07-18", "p8", SI,
    "0.5um Resolution and <0.3um Voxel", "High")
add("[C]", "Sigray 300 mm wafer case study: 12-minute scan at 0.2 um pixel size", "12", "min", "Sigray presentation, IEEE SCV EPS 18 Jul 2024", "2024-07-18", "p15", SI,
    "12 Minute Scan, 0.2 µm Pixel Size", "High")
add("[C]", "Sigray announced an 'Apex XCT-in-Line' system for advanced packaging (Jul 2024)", "Apex XCT-in-Line", "text", "Sigray presentation, IEEE SCV EPS 18 Jul 2024", "2024-07-18", "p18", SI,
    "Apex XCT-in-Line In-line System for Advanced Packaging", "High")
add("[C]", "Sigray adoption claim (Eclipse XRM / Apex XCT): received and expecting multiple POs", "multiple", "POs", "Sigray presentation, IEEE SCV EPS 18 Jul 2024", "2024-07-18", "p2", SI,
    "Received and expecting multiple POs", "Medium", "No customer named; slide pairs it with 'Multiple installations in two major companies' (AttoMap column)")
add("[C]", "Sigray: 3D wafer spot analysis in as little as 2-3 minutes", "2-3", "min per spot", "Sigray presentation, AVS NCCAVS user group Aug 2024", "2024-08", "Apex XCT-150 slide", SA,
    "Enables 3D wafer spot analysis in as little as 2-3 minutes.", "High")
add("[C]", "Sigray Apex XCT-300 series (300E/300W): 500 nm, up to 10 WPH site inspection, EFEM/FOUP, SECS/GEM - shown as 'Coming Soon'", "10", "WPH", "Sigray presentation, AVS NCCAVS user group Aug 2024", "2024-08", "Apex XCT-300 slide", SA,
    "Fast Site Inspection: Up to 10 WPH", "High", "Same slide: 'Coming Soon!' and garbled 'Coming: Q4 20..'; shipment NOT DISCLOSED")
add("[C]", "Sigray Apex XCT-150 (via distributor): 0.5 um 3D resolution in <15 min; sample up to 300 mm dia x 25 mm", "<15", "min", "Quantum Design (Sigray distributor) Apex XCT page", "2026-11-21", "Product features", SQX,
    "0.5 µm 3D spatial resolution in <15 minutes", "High", "Distributor reproduces maker specs")
add("[C]", "Sigray Apex Hybrid: laminography of 300 mm wafer / 213x213 mm panel; 350 nm spatial resolution", "350", "nm", "Quantum Design (Sigray distributor) Apex Hybrid page", "2026-11-21", "Specifications", SQH,
    "Laminography: 300 mm wafer / 213 × 213 mm panel", "High", "Apex Hybrid launched Apr 2025 per search lead (accessnewswire refused 403)")
add("[C]", "Sigray white paper: Apex XCT has EFEM for in-line use; Apex Hybrid EFEM on roadmap", "EFEM", "text", "Sigray Apex-Hybrid white paper (QD)", "2025-11-10", "p6 Table 1", SWP,
    "EFEM for In-line Use Yes On the Roadmap", "High", "Date from PDF metadata")
add("[S]", "Sigray is now part of Applied Materials: sigray.com 301-redirects to appliedmaterials.com/us/en/sigray.html (observed 2026-11-21)", "n/a", "text", "sigray.com redirect / Applied Materials Sigray page (not saved)", "2026-11-21", "HTTP redirect", "",
    "", "Medium", "NOT RETRIEVED: appliedmaterials.com returned 403; acquisition date/terms not found",
    url="https://www.appliedmaterials.com/us/en/sigray.html")

# ---------------- Omron
add("[C]", "Omron VT-X950 CT-type AXI: first VT model for cleanrooms, mid-process incl. wafer-to-wafer bonding", "VT-X950", "text", "Omron VT-X950 product page (EU)", "2026-11-21", "Product description", OM,
    "The X950 is the first in the VT series to support clean rooms for mid-process semiconductors where wafer-to-wafer bonding processes occur.", "High")
add("[C]", "Omron VT-X950 automation: conveyor-based automatic loading/unloading; AI deep-learning pass/fail", "conveyor auto-load", "text", "Omron VT-X950 product page (EU)", "2026-11-21", "Features", OM,
    "Equipped with a conveyor-based automatic loading/unloading function, contributing to automation and manpower saving in the manufacturing process", "High", "No 300 mm wafer EFEM/FOUP handling stated; resolution not on page")
add("[C]", "Omron VT-X950 captures stereoscopic images without stopping; targets narrow-pitch bump electrodes", "n/a", "text", "Omron VT-X950 news (EU)", "2026-11-21", "News body", OMEU,
    "The VT-X950 features technology that captures stereoscopic images without stopping, ensuring continuous inspection.", "High")
add("[S]", "Omron VT-X950 announced Nov 2023 for sequential release from Feb 2024", "2024-02", "date", "Dempa AEI article", "2026-11-21", "Article body", OMD,
    "They will be released sequentially from February 2024 onward.", "Medium")
add("[S]", "Monoist: Omron began selling VT-X950 in Dec 2024; demand found also in development stage, not only in-line", "2024-12", "date", "MONOist SEMICON Japan 2024 report", "2024-12-20", "Article body", OMM,
    "同年12月から販売を開始したCT型X線自動検査装置「VT-X950」を紹介した。", "Medium", "Conflicts with Feb/spring 2024 release plan in earlier coverage")

# ---------------- Viscom
add("[C]", "Viscom iX7059 One: 2D/2.5D/3D AXI down to 1 um, standalone or 100% in-line; solder bumps and advanced packaging listed; panel-format, not 300 mm wafer handling", "1", "um", "Viscom iX7059 One product page", "2026-11-21", "Product description", VI,
    "this system delivers unrivaled image quality down to an astonishing 1μm resolution", "High")

# ---------------- SEC Co., Ltd. (Korea, KOSDAQ 081180)
add("[S]", "SEC NF120 (manual) HBM X-ray tool deployed on Micron HBM mass-production line since 2023", "2023", "year", "Asia Business Daily 2026-02-04", "2026-02-04", "Article body", SEC1,
    "Despite being a manual system, it has been deployed to Micron's mass-production line since 2023 and is being used for HBM process inspection.", "Medium")
add("[S]", "SEC additional Micron order: ~KRW 1.8bn HBM X-ray equipment for Micron Taiwan, delivery by Jul 2026", "1.8", "KRW bn", "Asia Business Daily 2026-02-04", "2026-02-04", "Article body", SEC1,
    "Sec signed a supply contract on the 3rd for HBM X-ray inspection equipment worth approximately 1.8 billion won", "Medium", "KRX/DART filing NOT RETRIEVED (kind.krx.co.kr 403)", "", "Feb 2026")
add("[S]", "SEC: ~KRW 5.8bn Micron Singapore order (contract 6 Nov 2026) for manual NF120 HBM X-ray tools; 9.84% of prior-year sales", "5.8", "KRW bn", "Asia Business Daily (Korean) 2026-11-10", "2026-11-10", "Article body", SEC3,
    "마이크론 싱가포르 법인과 약 58억원 규모의 HBM용 X-ray 검사장비 공급계약을 체결했다고 밝혔다", "Medium", "Prior-year sales KRW 59.2bn per article; filing not retrieved", "", "Nov 2026")
add("[S]", "SEC won its first contract (Oct 2026) to supply 'Semi-scan Wafer' to a global OSAT's WLP mass-production line", "1", "first contract", "Asia Business Daily (Korean) 2026-11-10", "2026-11-10", "Article body", SEC3,
    "글로벌 반도체 후공정 전문기업(OSAT)의 웨이퍼 레벨 패키징(WLP) 양산라인에 자체 개발한 'Semi-scan Wafer'를 처음 공급하는 계약을 확보했다", "Medium", "OSAT not named; amount not stated", "", "Oct 2026")
add("[S]", "SEC Semi-Scan-SW in-line X-ray detects 3-5 um defects in HBM stacking; alpha testing from Apr 2026", "3-5", "um", "TechNews (Taiwan) 2026-04-02", "2026-04-02", "Article body", SEC4,
    "可偵測在 HBM 堆疊製程中產生的 3 微米（ μm ）至 5 微米缺陷", "Medium")
add("[S]", "SEC sold 8 manual HBM tools to Micron in 2025; in-line tool in validation at a domestic memory maker; order possible earliest Q1 2027", "8", "units (2025)", "Economist (Korea) 2026-09-22", "2026-09-22", "Article body", SEC5,
    "2025년에는 미국 메모리 업체 마이크론에 HBM용 수동 검사장비 8대를 판매하며", "Medium", "", "FY2025", "Jan-Dec 2025")
add("[S]", "SEC holds a registered patent on reducing X-ray damage to HBM during inspection; 1 um-class tube for TSV/hybrid bonding in development", "patent", "text", "Economist (Korea) 2026-09-22", "2026-09-22", "Article body", SEC5,
    "검사 과정에서 HBM에 가해질 수 있는 X-ray 손상을 줄이는 기술도 특허 등록을 마쳤다", "Medium")
add("[S]", "SEC (IR, May 2026): HBM in-line tool under customer evaluation; TSV/hybrid-bonding version targeted for Q2-Q3 2026", "Q2-Q3 2026", "target", "Asia Business Daily 2026-05-21", "2026-05-21", "Article body", SEC2,
    "The company is currently conducting evaluations of its inline inspection equipment for HBM with customers", "Medium")
add("[S]", "X-EYE NF120 (distributor listing): 0.2 um min resolution, 12-inch wafer table, optional 3D CT, wafer handler", "0.2", "um", "Renex (distributor) X-EYE NF120 page", "2026-11-21", "Specifications", SEC6,
    "Tomography is available if 3D CT module is added and Wafer Bump Automatic Inspection is available from loading to inspection with wafer handler systems.", "Low", "Page does not name the maker; NF120 is SEC's per Asiae 2026-02-04; resolution conflicts (400 nm tube vs 0.2 um)")
add("[S]", "SEC targeted completing HBM in-line X-ray tool development in Feb 2026", "2026-02", "target", "Asia Business Daily 2026-01-16", "2026-01-16", "Article body", SEC7,
    "our inline X-ray inspection equipment for HBM, which we introduced with the goal of completing development in February", "Medium")

# ---------------- XAVIS
add("[C]", "XAVIS Xscan-9860A (SEMICON Korea, Feb 2026): wafer-level package in-line, 0.25 um, 2D/3D hybrid + high-speed CT, EFEM/OHT, dose reduction", "0.25", "um", "XAVIS release as published by Korea Daily", "2026-02-09", "Article body", XA,
    "the Xscan-9860A, a wafer-level package inline inspection equipment, provides 0.25μm image resolution utilizing AI", "Medium", "Company release text on newspaper site; XAVIS KOSDAQ 254120")
add("[C]", "XAVIS Xscan-9860A dose claim: X-ray dose reduction technology (no figure)", "n/a", "text", "XAVIS release as published by Korea Daily", "2026-02-09", "Article body", XA,
    "With various features and X-ray dose reduction technology, it can provide customized solutions to meet diverse customer requirements.", "Medium")

# ---------------- Unicomp (China, 688531)
add("[F]", "Unicomp FY2025 annual report: advanced-packaging X-ray CT inspection equipment is in customer validation and introduction (no orders stated)", "validation", "text", "Unicomp Technology FY2025 annual report", "2026-04-17", "p28", UA,
    "目前，公司正在积极推进先进封装检测设备", "High", "Sentence continues on next line: customer validation and introduction", "FY2025", "Jan-Dec 2025")
add("[C]", "Unicomp claims sub-micron microfocus source + CT for advanced packaging, suited to in-line integration", "sub-micron", "text", "Unicomp Technology FY2025 annual report", "2026-04-17", "p28", UA,
    "公司面向半导体先进封装场景研发的 X 射线智能检测设备，依托亚微米级分辨率微焦点 X 射线源", "High")

# ---------------- additions (Sigray detail)
add("[C]", "Sigray Apex XCT bridging demo: throughput mode 2.5 um voxel over 7.35 x 5.75 mm FOV (high-res mode 0.5 um over 1.47 x 1.15 mm)", "7.35 x 5.75", "mm", "Sigray presentation, IEEE SCV EPS 18 Jul 2024", "2024-07-18", "p11", SI,
    "Field of View 1.47 x 1.15 mm 7.35 x 5.75 mm", "High", "Same slide: total integration time 30 min (high res) vs 12 min (throughput)")
add("[C]", "Sigray Apex XCT claims advanced defect-detection algorithms; ML classification of wet vs non-wet joints", "n/a", "text", "Sigray presentation, IEEE SCV EPS 18 Jul 2024", "2024-07-18", "p8", SI,
    "Advanced algorithms for defect detection", "High", "p17: 'Wet vs Non Wet Joints (Machine Learning)'")
add("[C]", "Sigray Apex Hybrid automation: in-system robot for up to ten 100 x 100 mm samples", "10", "samples", "Quantum Design (Sigray distributor) Apex Hybrid page", "2026-11-21", "Automation and detector options", SQH,
    "capable of handling up to ten 100 × 100 mm samples automatically", "High")

# --------- verify and number
bad = 0
for i, r in enumerate(rows, 1):
    r["id"] = f"RV-{i:03d}"
    if r["local_file"]:
        if not r["url"]:
            print("NO URL", r["id"], r["local_file"]); bad += 1
        pages = pages_of(r["local_file"])
        q = norm(r["quote"])
        hits = [n for n, p in enumerate(pages, 1) if q in norm(p)]
        if not hits:
            print("QUOTE NOT FOUND", r["id"], r["quote"][:60]); bad += 1
        elif r["local_file"].endswith(".pdf") and r["page_or_section"].startswith("p") and r["page_or_section"][1:].split()[0].isdigit():
            pg = int(r["page_or_section"][1:].split()[0])
            if pg not in hits:
                print("PAGE", r["id"], pg, "found on", hits); bad += 1
        if len(r["quote"].split()) > 25:
            print("LONG", r["id"]); bad += 1
out = os.path.join(ROOT, "research/out/comet/parts/RV.csv")
os.makedirs(os.path.dirname(out), exist_ok=True)
with open(out, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=H)
    w.writeheader()
    for r in rows:
        w.writerow({k: r[k] for k in H})
from collections import Counter
print(len(rows), "rows", Counter(r["tag"] for r in rows), "problems:", bad)
