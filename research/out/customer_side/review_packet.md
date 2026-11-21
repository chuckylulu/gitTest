# Review packet - customer_side (21 Nov 2026)

Question: what SK hynix, Samsung, Micron, TSMC, Intel, ASE and Amkor themselves say (Jan 2025 - Nov 2026) they use to inspect and measure HBM stacks and hybrid-bonded interfaces.

Caveats:
- Conference items rest on **abstracts**: the publisher pages refuse scripts, so a reviewer with a subscription can go further than we did.
- Tags: [F] primary document read; [C] company claim; [S] press; [I] our inference.

## 15 most important claims

| Id | Tag | Claim | Value | Period | Public URL | Page / section |
|---|---|---|---|---|---|---|
| PAPM-049 | [F] | Samsung PROPOSES an electrical pre-screen of HBM buffer-die pad-to-micro-bump interface resistance for use in mass production (adoption not stated) | - | Mar-Apr 2025 | https://doi.org/10.1109/irps48204.2025.10983202 | abstract |
| PAPM-222 | [C] | SK hynix authors say the optimised TSV SiO2 film process (IR inspection + FIB checks) was 'successfully applied in mass production' in the HBM WLP line (company claim) | - | Oct 2025 | https://doi.org/10.5573/JSTS.2025.25.5.490 | full text |
| PAPM-201 | [C] | SK hynix: in-line optical chip-warpage measurement for HBM is a 'commercialized solution currently in use' (company claim) | - | Oct 2025 | https://doi.org/10.5573/JSTS.2025.25.5.585 | full text |
| ADDL-002 | [C] | Intel (SWTest 2026, with FormFactor): micro-bump probing (wafer/die sort) in high-volume production on Foveros since 2019 (company claim; micro-bump test, not hybrid bonds) | 2019 | Jun 2026 | https://www.swtest.org/library/2026proc/pdf/W07_01_AHMED_SWTest-2026.pdf | p3 |
| PAPM-216 | [F] | SK hynix: IR post-bond die shift/tilt metrology validated on actual HBM wafers in a 'production-grade MI setup' | - | Oct 2025 | https://doi.org/10.5573/JSTS.2025.25.5.484 | full text |
| PAPM-136 | [F] | SK hynix HBM4 (VLSI 2026): daisy chain + C-SAM show 'void-free' micro-bumps on Mechanical Test Vehicle 4 | 12 | Jun 2026 | https://doi.org/10.1109/vlsitechnologyandcir65830.2026.11577576 | abstract |
| SMP-031 | [F] | Intel (ECTC 2026, with EV Group): C2W bond-overlay metrology aims at '100% chiplet inspection' (today: reduced sampling plans) | 100 | May 2026 | https://doi.org/10.1109/ectc51846.2026.00354 | abstract (Semantic Scholar record) |
| PAPL-046 | [F] | Intel (ECTC 2026): near-infrared post-bond chiplet-level overlay mapping on a fiducial-grid test vehicle | - | May 2026 | https://doi.org/10.1109/ectc51846.2026.00030 | abstract |
| PAPM-016 | [F] | Micron (ECTC 2025): wafer-to-wafer bonding for HBM density; CSAM 'clean of voids'; flow 'demonstrated' | - | May 2025 | https://doi.org/10.1109/ectc51687.2025.00097 | abstract |
| TALK-020 | [F] | Samsung (VLSI 2025 workshop): optical, X-ray microscopy, AFM and acoustic microscopy 'are examined' for hybrid bonding | 4 techniques + AI | Jun 2025 | https://archive.vlsisymposium.org/25web/workshop/workshop2025_9/index.html | talk 2 abstract |
| TALK-024 | [S] | Press only: Samsung reportedly validating Onto picosecond laser-ultrasound tools on mass-production lines | validation on production lines | Mar 2026 | https://www.thelec.net/news/articleView.html?idxno=6232 | body |
| XR-003 | [F] | Intel: on-package DRAM survived three times the DRAM maker's X-ray limit without infant mortality; long-term reliability may be reduced | 3 | Apr 2025 (orig. Oct 2024) | https://magazines007.com/pdf/SMT007-Apr2025.pdf | p54 |
| XR-015 | [S] | Press only: TSMC's SEMICON Taiwan 2026 forum keynote abstract reportedly lists 'DRAM/HBM damage concern by X-ray' | n/a | Sep 2026 | https://windowsforum.com/news/tsmcs-hbm-x-ray-inspection-focus-what-it-really-means.444052/ | body |
| ADDM-007 | [F] | Samsung-led SPIE 2025 paper: post-bond void maps of 3D NAND wafer-to-wafer hybrid bonds come from SAM; a full-wafer SAM scan takes 10-20 minutes, so an interferometry alternative was developed | 10-20 | Feb 2025 (conference); manuscript Apr 2025 | https://novami.com/wp-content/uploads/2025/04/challenges-and-responses-of-metrology-technologies-for-the-new-wave-of-3d-nand-devices.pdf | p4 |
| TALK-014 | [S] | Guest tech note by an Inha University professor on SK hynix's newsroom (Aug 2026): D2W hybrid bonding for HBM is 'progressing toward commercialization' (not SK hynix's own words) | status: toward commercialisation | Aug 2026 | https://news.skhynix.com/en/tech-note-series-ep2/ | section 'Bump-less Chip Connections Enable High Efficiency and Bandwidth, Drawing Particular Attention in the HBM', second paragraph after the figure captioned 'Two Major Hybrid Bonding Methods' |

## 5 inferences the conclusions lean on

1. [I] Production wording for an inspection or test step on stacked dies exists only as company claims (Intel micro-bump sort on Foveros; SK hynix HBM chip warpage 'currently in use', location unstated). SK hynix IR die-shift metrology and Samsung/Micron HBM electrical tests are pilot at most; every hybrid- or wafer-bonded-interface method is lab or pilot. (rows SYN-001, SYN-002, SYN-019, SYN-049). Inputs: ADDL-002 [C], PAPM-201 [C], PAPM-216, PAPM-049 ('We propose'), PAPM-107, PAPM-110 [C], ADDM-058 [C], SMP-016; all cells in calc/method_matrix.py.
2. [I] In period, chipmaker X-ray-damage statements come from Intel (dose numbers, on-package DRAM), Micron (co-author, 3D NAND), Samsung (patent application) and TSMC (press only); none gives an HBM dose limit. (rows XR-038). Inputs: XR-001..XR-013; searches listed in the XR module notes.
3. [I] HBM test intensity is rising (more insertions and items, higher test cost) but no chipmaker publishes a count or test time. (rows SMP-041). Inputs: SMP-009..SMP-015, SMP-038..SMP-040, PAPM-049.
4. [I] Memory makers present virtual metrology as extra coverage on every wafer, not as cutting physical measurements. (rows SMP-042). Inputs: SMP-001, SMP-002, SMP-005..SMP-008, SMP-022, SMP-025.
5. [I] Inspection, metrology and test vendors are about one winner in ten on the award lists read in full; no category names an HBM or hybrid-bonding product. (rows AW-058). Inputs: 17 of 177 winner entries on 8 full lists (calc/AW_counts.py).

## 3 questions we could not settle

1. What does TSMC's own abstract (https://www.semicontaiwan.org/en/node/18506) say about X-ray damage, methods and design-for-metrology? Only press paraphrase was available.
2. Is any non-electrical void or overlay inspection of HBM stacks in production at SK hynix or Samsung? Onto's reported SK hynix 2026 Best Partner Award for HBM hidden-defect prevention (Dragonfly G5) and TheElec's Samsung laser-acoustic report point that way, but neither is the chipmaker's own text.
3. Do the full texts of the key papers (Intel ECTC 2026 100% overlay; ASE ECTC 2026 CoW voids; SK hynix VLSI 2026 HBM4; Samsung IRPS 2025) name tools, X-ray or AFM use, and production status that the abstracts omit?
