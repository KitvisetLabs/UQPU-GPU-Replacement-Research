# Eight-Lane UQPU integration — 2026-10-28 — SymbolFit uncertainty gate

**Integration ID:** INT-20261028-SYMBOLFIT-UNCERTAINTY  
**Starting main:** `28de5409eeac3e0244ee9231652eecec4c059da`  
**Primary work owner:** Lane A  
**Evidence/accounting owner:** Lane F  
**Literature/publication owner:** Lane H  
**Evidence class:** LITERATURE_ONLY + PROTOCOL_ONLY  
**Status:** integrated in documentation/protocol; no matched benchmark or physical experiment

## Shared contract

The new source [SymbolFit, arXiv:2607.19750](https://arxiv.org/abs/2607.19750) (v2 revised 2026-10-19) is added as a domain-specific HEP binned-fit task under existing RG-EQN-008. It is not pooled with general law-recovery or interactive experiment-design scores. The [literature watch](../docs/literature_watch/2026-10-28-symbolfit-uncertainty-aware-equation-discovery.md), [Batch 100](../docs/BATCH_100_SYMBOLFIT_UNCERTAINTY_AWARE_EQUATION_DISCOVERY.md) and machine-readable [Lane A preregistration manifest](../research_lanes/A_quantum_programming_runtime/SYMBOLFIT_UNCERTAINTY_PROTOCOL_V1.json) share this boundary.

The existing schema-v4 comparator remains the canonical matched-resource interface. Its current output includes a Wilson interval for accepted-candidate rate and descriptive paired acceptance counts, but not a full calibration/coverage analysis for predictive intervals. The next code change should add that missing capability only after synthetic positive/null controls and tests are specified. No parallel generic comparator is introduced.

## Cross-lane integration

| Interface | Integration rule |
|---|---|
| A ↔ F | Freeze the dataset/source/license, model/config/runtime, splits, acceptance rules, shared seeds and hard budgets; account for training + inference, failures and one cost basis. |
| A ↔ H | Source-date metadata distinguishes original v1 submission (2026-07-22) from v2 revision (2026-10-19); author-reported scores remain external. |
| A ↔ C | Raw data bytes, memory, I/O, transfer and reconstruction are resources; state-space size is not readable classical storage. |
| A ↔ B | No cloud/QPU execution is needed for the literature gate; provider-neutral paths remain dry-run-first. |
| D ↔ G | Continuous device/process and manufacturing-equipment co-design preserved; VortexOp supplies an external solver-in-the-loop methodology candidate, not device/factory evidence. |
| E ↔ F/H | BIO-001 accepted-liquid cost and FUS-001 reliable net-electric lifecycle cost remain separate, open gates; no cross-pillar economic evidence is inferred. |
| A–H ↔ INV-034/035 | New candidate methods still pass math/physics constraints, counterexample search, held-out tests and independent validation before any physical claim. |

## A–H status

- **A:** advanced the preregistration protocol; next add/test calibration metrics on synthetic known-function and null controls. Priority-1 signed-Max-Cut provider-neutral lowering/reference/simulator remains ahead of this secondary method study.
- **B:** maintained provider-neutral cloud adapter inventory; no credentials, paid jobs or new provider evidence.
- **C:** maintained memory/state/data-movement accounting; no classical memory/storage equivalence claim.
- **D:** advanced literature surveillance for physics-guided active material/geometry design; no measured UQPU device/process result.
- **E:** maintained Pangola/carbon, accepted-liquid bio-oil, fusion electricity, cooling and infrastructure tracks; VortexOp did not test biomass carbon and adds no material-substitution evidence.
- **F:** advanced uncertainty/total-resource acceptance criteria; no measured economics or WACC effect.
- **G:** advanced the D/G literature gate: future solver-in-loop design must include process windows, metrology, yield, rework and cost per good part/package.
- **H:** published the literature synthesis; multilingual Thai/English/Chinese/Japanese/Korean/German strategic-plan links and strategic AI-agent/funding references remain preserved as context.

## Foundations and permanent missions

FND-001–006 and EQN-001–008 remain active. No change is made to current physical-limit helpers, and no AI-generated equation is promoted. INV-029–035 and INV-025/026/027 remain preserved. The US$10T–US$100T proxy, 100×/100,000,000× targets, universal subsystem/material substitution, low-cost commercial bio-oil/fusion, lower WACC and Data-Center-to-One-Phone remain unachieved goals until their own end-to-end evidence gates pass.

BIO-001, FUS-001 and FIN-001 remain open. Carbon processing is not elemental transmutation. Lower financed principal can reduce absolute interest at unchanged terms; a lower WACC or economy-wide rate requires separate evidence.

## CI, sync and next gate

The cycle-start combined-status query returned no status entries; the available workflow-run wrapper returned no applicable runs because it exposes PR-triggered runs only. Exact-head CI is **UNVERIFIED**, not green. The repository's required `Research-Sync: main` trailer is included in created commit messages. README, WORKLOG and RESEARCH_GAPS were synchronized on main by the final documentation commits; exact-head CI still must be verified on the resulting head.

Next gate: source-byte/license verification -> synthetic positive/null controls -> uncertainty calibration tests -> blind matched comparison if controls pass. No paid QPU job is authorized.


## Supplementary Lane D/G/E surveillance — VortexOp

A new-to-repository peer-reviewed source, Moeinnia, Islam and Kim, “VortexOp: Autonomous Physics-Guided Discovery of Functionally Graded Metamaterials,” *Journal of Computational Design and Engineering*, published 2026-09-21 (corrected/typeset 2026-10-21), DOI https://doi.org/10.1093/jcde/qwag085, is recorded in `docs/literature_watch/2026-10-28-vortexop-physics-guided-metamaterial-design.md` and the Batch 100 addendum.

The relevant method is finite-element-solver-in-the-loop active design with Gaussian-process surrogates and constrained Bayesian optimization. Transfer is blocked pending code/data access, mesh convergence, independent-solver verification, replicated specimens, held-out geometry/load/scale and process-aware printability/yield tests. The paper's one-specimen-per-configuration design and linear-static/small-strain solver prevent a broad material-performance claim. No Pangola/carbon material was tested.

This addition advances the Lane D/G co-design research question while keeping INV-030 evidence-gated: measure the actual material function first, then compare a characterized carbon-rich candidate with a matched incumbent; never claim elemental transmutation. Lane F must include rework/yield and total lifecycle cost.
