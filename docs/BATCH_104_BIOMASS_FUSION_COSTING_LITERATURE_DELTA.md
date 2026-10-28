# Batch 104 — biomass pilot-yield and fusion cost-account literature delta

**Date:** 2026-10-28  
**Starting main SHA:** 10ba9ec2ffa6d37ac09b65092d09e70b798cd2db  
**Primary lanes:** E (biomass/fusion), F (economics/evidence)  
**Cross-lane owners:** A (model holdouts), C (data/resource accounting), D/G (device/manufacturing cost drivers), H (publication/strategy)  
**Evidence class:** PEER-REVIEWED LITERATURE + OFFICIAL ARXIV PREPRINTS + RESEARCH-GAP CONTRACTS  
**Execution boundary:** no external code/data reproduction, no Pangola experiment, no fusion plant experiment, no QPU

## 1. Dynamic start and CI state

The starting main head was resolved as 10ba9ec2ffa6d37ac09b65092d09e70b798cd2db; Batch 103 was the newest main-branch batch. The prior Batch 103 head's Python test matrix completed successfully in Python 3.10, 3.11 and 3.12 (821 tests per matrix job, including the 11 new temporal-holdout tests). Its full UQPU core/invariant workflow was still running with no failure reported at the observation; its cold-start handoff audit passed. This addendum's own head requires separate exact-head Actions.

The root mission, INV-025/026/027 and INV-029–035, A–H architecture, FND-001–006, EQN-001–010, BIO-001/FUS-001/FIN-001, Ketskaew Chulamani/Kanusanan Pongpanna Model and all six strategic-plan language links remain preserved.

## 2. Fresh literature surveillance — BIO-001 / INV-031

Two peer-reviewed Bioresource Technology records not indexed in the starting main head were added to a focused watch:

- Yang et al. (online 2026-06-24), pilot-scale pine-sawdust dual-fluidized-bed pyrolysis with in-situ biochar recovery. The authors report 61.5 wt% bio-oil, 13.2 wt% recovered char, a Grade D quality statement, and a model-derived minimum selling price of 0.94 CNY/kg under the stated 90% char-recovery scenario.
- Sudha et al. (Epub 2026-04-21), ANN-assisted sugarcane-bagasse pyrolysis modeling. The authors report R²=0.958 for bio-oil yield and 0.941 for char yield over their evaluated range, alongside 50 kg/h feed throughput and a volumetric liquid rate.

The useful novelty is the coupling of char recovery/heat integration with liquid quality and model-based yield prediction. The required next step is not to copy yields into the Pangola model: reconcile dry-feed/moisture basis, wt% versus L/h using measured density, close mass/energy balances, verify product acceptance and upgrading demand, and test future-time/feedstock-family/reactor-scale generalization. The reported 0.94 CNY/kg is a scenario-specific TEA output, not a universal or independently verified commercial price.

## 3. Fresh literature surveillance — FUS-001 / FIN-001

Woodruff's official arXiv preprints (2601.21724 and 2602.19389) document the standards-aligned FECONs/pyFECONs fusion-costing framework and an extension for MFE/IFE/MIFE driver-specific cost accounts, material/TRL/learning uncertainty, safety/regulatory adders and NPV/IRR/MIRR/WACC-based metrics. A public notebook/Colab repository was found at https://github.com/Woodruff-Scientific-Ltd/PyFECONs-GoogleColab.

The project-relevant advance is a candidate common accounting spine that can improve architecture-neutral FUS-001 comparability while retaining different dominant physics/engineering drivers. The code and benchmark were not executed in this cycle. Follow-up requires pinning exact source/code/data/licence hashes, reproducing a public case, mapping all net-electric cost drivers, and preserving uncertainty and FOAK/NOAK distinctions. WACC/risk-premium changes remain scenarios, not evidence of a causal rate reduction.

## 4. A–H integration

| Lane | Delta | Evidence boundary / next gate |
|---|---|---|
| **A — workloads/software (Priority #1)** | Temporal holdout certificate from Batch 103 can be used for ANN/surrogate validation; signed-Max-Cut QAOA/SDK PRs #149/#150 remain open. | Exact-head CI, then source-pinned future-time and feedstock/geometry holdouts. No QPU execution. |
| **B — cloud/QPU** | No provider or target action; provider-neutral routes unchanged. | Simulator/dry-run first; no paid job. |
| **C — memory/state/data movement** | No new data-movement result. Future model comparisons must record raw-data bytes, transfers, peak memory and reconstruction. | Measure resources on matched workloads. |
| **D — devices/chips/process** | No device or fabrication evidence. | Keep device/material cost inputs traceable to measured designs and component lifetimes. |
| **E — biomass/fusion/materials** | Added BIO-001 pilot/ANN source leads and pyFECONs fusion-costing references. | Pangola-specific mass/energy/product-quality closure and net-electric fusion lifecycle model remain open. |
| **F — economics/evidence** | New source-specific gaps formalize yield-basis reconciliation and fusion cost-account reproduction. | No TEA result accepted until inputs, boundaries, financing and uncertainty are auditable. |
| **G — manufacturing/factory systems** | pyFECONs highlights learning and driver manufacturing as modeled cost factors; no actual factory/yield data. | Validate learning with observed production, yield, component replacement and cost per good unit. |
| **H — strategy/publication** | Two source-specific watches, two focused gaps, batch and integration report published; strategic references preserved. | Keep ambition, model output and demonstrated evidence distinct. |

## 5. INV-029–035 and foundational status

- **INV-029:** no physical Data-Center-to-One-Phone compression, capability equivalence, energy closure or lifecycle-cost evidence.
- **INV-030:** recovered biochar is a candidate carbon stream; no Pangola material qualification, universal substitution or elemental transmutation.
- **INV-031:** literature leads only; no accepted Pangola saleable-liquid cost or commercial fuel result.
- **INV-032:** pyFECONs is a costing method, not net delivered fusion electricity or commercial low-cost fusion evidence.
- **INV-033:** finance/value metrics can be modeled; no project-level interest saving or WACC reduction measured. Lower principal lowers absolute interest only at unchanged terms.
- **INV-034:** no new physical limit or law.
- **INV-035:** ANN/operator/cost equations remain hypotheses or models; dimensional/physical/held-out/replication gates remain binding.

FND-001 thermodynamic-gap accounting, FND-002 output-information bounds, FND-003 matched QSL measurement, FND-004 alternative primitives, FND-005 QFT/particle scans and FND-006 mathematics-first discovery remain evidence-gated. EQN-001–010 remain unpromoted. BIO-001, FUS-001 and FIN-001 have more precise follow-up source leads but remain open.

## 6. Sync and next gate

This batch adds two dated literature watches, two focused research gaps, this batch and integration report, and synchronized README, integration index, eight-lane scoreboard, cold-start manifest, RESEARCH_GAPS and WORKLOG updates. Append-only history is extended rather than reconstructed. The manifest adds all new artifacts to its required-reading list.

**Next highest-value gate:** pass exact-head core/invariant and cold-start Actions; then pin and reproduce one pyFECONs public benchmark and close one biomass pilot mass/energy/product-quality balance. Do not mix author-reported yields, model-derived selling prices or WACC scenarios with measured UQPU evidence.
