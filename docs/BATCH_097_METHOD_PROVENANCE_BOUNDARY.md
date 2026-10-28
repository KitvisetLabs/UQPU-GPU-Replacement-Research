# Batch 097 — matched equation-discovery method-provenance boundary

**Date:** 2026-10-28  
**Cycle-start main SHA:** d04eb7987b2e3b0c82840b77e263cf2ae8e41285  
**Lane A:** workload/compiler and reproducible comparator implementation (primary execution priority)  
**Lane F:** benchmark/evidence contract and integration (primary artifact owner)  
**Lane H:** literature surveillance and handoff/publication  
**Cross-lane interfaces:** A–H; D/G co-design; FND-001–006; EQN-001–008; BIO-001; FUS-001; FIN-001  
**Evidence class:** SOFTWARE_CONTRACT / REGRESSION_TESTS_PENDING_EXACT_HEAD_CI  
**Hardware:** no real QPU, no paid job, no physical experiment

## 1. Canonical start and source audit

The cycle started from the newest observed main commit, `d04eb7987b2e3b0c82840b77e263cf2ae8e41285`, then read the charter, version invariants, goals, README, Research Operating System, open-frontier directive, Kanusanan Pongpanna Model, strategic references, current Batch 096, focused equation-discovery gap, existing comparator and its tests, split-manifest validator, cold-start handoff principle, commit-sync policy, and cross-lane integration protocol. The root directives `00_ULTIMATE_NORTH_STAR_DATA_CENTER_TO_PHONE.md`, `00A_PERMANENT_AI_EQUATION_DISCOVERY_PRINCIPLE.md`, and `01`–`06` remain required and preserved. Thai, English, Chinese, Japanese, Korean and German public master-plan links remain in `STRATEGIC_PLAN_REFERENCES.md`.

The newest prior batch was Batch 096; no Batch 097 existed at cycle start. The large append-oriented `RESEARCH_GAPS.md` was not rewritten wholesale. The focused owner record remains `docs/RESEARCH_GAP_EQN008_MATCHED_DISCOVERY_COMPARISON.md`.

## 2. Code and test delta

The prior comparator (schema v3) checked common dataset/split/preprocessing/grammar/unit/acceptance/holdout hashes, identical declared budgets, at least 30 shared preregistered seeds, resource ceilings, and consistent cost basis. Audit found a reproducibility hole: `method_revision_sha256` was validated per row but not required to stay fixed across seeds of the same method, and configuration/runtime and dataset-source/license provenance were not separately represented.

The comparator now uses schema `uqpu-equation-discovery-matched-comparison-v4`:
- `dataset_provenance_sha256` binds the declared source/version/license/acquisition manifest and must match across methods;
- `method_config_sha256` binds fixed method settings, including relevant prompts, operators, hyperparameters and model/checkpoint identifiers;
- `runtime_environment_sha256` binds the pinned runtime/dependency/container environment;
- within each method, source revision, configuration and runtime-environment hashes must remain constant across all preregistered seeds;
- the summary exposes the shared dataset-provenance digest and each method's provenance digests.

Method-specific configuration/runtime hashes may differ across methods; each must be fixed across that method's seeds. Hashes do not authenticate their referenced artifacts. Actual source, lockfile, model/checkpoint and manifest bytes must still be stored or resolvable and independently verified.

Regression fixtures were extended for the new fields, schema v4 reporting, dataset-provenance mismatch, invalid digests, and per-method provenance drift. The split-disjointness fixtures now provide the additional provenance fields. The three source commits on main are:
- comparator: [`8d109a78d4360320af059d6b0af1f903777be8b5`](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/commit/8d109a78d4360320af059d6b0af1f903777be8b5)
- comparator tests: [`a3e9aff7acca8962970aafca052d859a7d610cb3`](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/commit/a3e9aff7acca8962970aafca052d859a7d610cb3)
- split-disjointness fixture: [`e8c82e30c1e03cacc4471c4f977d9548460385d3`](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/commit/e8c82e30c1e03cacc4471c4f977d9548460385d3)

The owner gap was synchronized in [`f8a93b1f76bf32b2212896977b353172af1502cc`](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/commit/f8a93b1f76bf32b2212896977b353172af1502cc). All listed commits are on canonical `main`; exact-head CI has not yet been verified for the final combined state.

## 3. Literature surveillance delta

Fresh searches rechecked dimensionality-aware symbolic regression (SymFM, Zenodo DOI [10.5281/zenodo.22093560](https://doi.org/10.5281/zenodo.22093560)), physics-informed adaptive candidate generation (PiT-PO, [arXiv:2602.10576](https://arxiv.org/abs/2602.10576)), LLM-controlled symbolic search ([arXiv:2607.04156](https://arxiv.org/abs/2607.04156)), and AI-generated mathematical-instrument/proof-provenance work ([arXiv:2610.17090](https://arxiv.org/abs/2610.17090)). The current repository already has dated watches for these sources, so this cycle did not create a duplicate literature article. The sources remain external literature/preprints, not UQPU reproduction. No additional searched result changed the project's evidence status. In particular, no paper-reported score, reward, symbolic fit, or formal-looking expression is treated as a physical law.

## 4. A–H and cross-lane integration review

| Lane | Status this cycle | Evidence boundary and next gate |
|---|---|---|
| A — programming/workloads/compiler/runtime | **ADVANCED** | Added fixed per-method provenance bindings. Next: exact-head CI, then provider-neutral lowering and exact classical/reference plus target-aware simulator comparison for the frozen signed-Max-Cut useful-output contract. |
| B — cloud/QPU/provider integration | MAINTAINED | IBM Quantum, Braket, Azure Quantum, IonQ, Rigetti, D-Wave, IQM, Quantinuum, Pasqal, QuEra, Quandela, OQC and emerging providers remain provider-neutral targets. Dry-run/simulator first; no credentials, bounded budget and explicit consent for paid execution. |
| C — RAM/VRAM/HBM/storage/state/data movement | MAINTAINED | Dataset provenance and grouped holdouts are now more explicit; state-space size is not readable classical memory. Bytes, state preparation, addressability, I/O, transfer and reconstruction remain required costs. |
| D — device/chip/process/fabrication/packaging | MAINTAINED | Any future equation-derived process model must bind to measured process windows, metrology, yield, reliability and packaging. No device measurement or fabrication advantage. |
| E — Pangola/materials/bio-oil/fusion/cooling/infrastructure | MAINTAINED; gates open | BIO-001 still requires accepted-liquid mass/energy/yield/upgrading/full-cost evidence; FUS-001 still requires net reliable delivered electricity and lifecycle cost. No material substitution, commercial fuel or fusion electricity result. |
| F — economics/evidence/integration | **ADVANCED** | Schema v4 now binds dataset source provenance and per-method configuration/runtime consistency. No real experiment cost, accepted-equation cost, WACC reduction or commercial economics measured. |
| G — chip manufacturing equipment/software/factory systems | MAINTAINED; D/G co-design continuous | Link future process equations to metrology, defectivity, process control, yield and cost per good die/device/package. No factory result. |
| H — strategic/finance/future industries/publication | MAINTAINED | Literature provenance, six-language public plan links and strategic AI-agent/funding context preserved. Strategic references remain context, not independent market/financing evidence. |

The 28 possible unordered A–H pair interfaces remain the operating review surface. This cycle specifically reviewed A↔F↔H (method provenance and evidence acceptance), C↔F (dataset/state/output accounting), D↔G (process-model validation), E↔F↔H (full energy/material/economic boundaries), and INV-034/035→A–H. No cross-lane hypothesis was promoted without measurements.

## 5. Foundations and equation-discovery program

- **FND-001:** thermodynamic/ergotropy limits remain scoped ideal bounds; they are not wall-plug energy measurements.
- **FND-002:** output-information lower bounds must use accepted-output semantics and reconstruction/I/O costs; no Hilbert-space-to-storage equivalence.
- **FND-003:** matched control-versus-quantum-speed-limit measurement and exact theorem reconstruction remain open.
- **FND-004:** alternative physical primitives remain hypothesis scans; no measured advantage.
- **FND-005:** QFT/elementary-particle mechanisms remain literature/hypothesis work; no new particle mechanism claimed.
- **FND-006:** advanced at reproducibility-governance level only; no discovered equation was independently accepted.
- **EQN-001–006:** unchanged evidence gates; candidate generation must still pass units, symmetry, conservation, causality, limiting cases, held-out predictions, counterexample search, proof/simulation where appropriate, a discriminating experiment and independent validation.
- **EQN-007–008:** formal-proof and matched-method comparisons remain separate; schema v4 is a contract hardening, not an executed benchmark.
- **BIO-001 / FUS-001 / FIN-001:** no accepted bio-oil, net fusion electricity, reduced financed principal/absolute interest or lower WACC result.

## 6. Permanent invariants and explicit non-claims

INV-029 remains the physical Data-Center-to-One-Phone north star measured by equivalent useful service, energy, physical boundary and lifecycle cost; a remote terminal does not count. INV-030 permits carbon-material functional substitution, minimization, recovery/recycling, hybridization or redesign, never elemental transmutation. INV-031 uses accepted liquid-energy/fuel function and full process/upgrading/logistics/financing cost. INV-032 uses reliable NET delivered electricity and full lifecycle cost. INV-033 distinguishes reducing financed principal/time at unchanged terms from separately proving a lower WACC/risk premium. INV-034 keeps the mathematics-to-physics-to-device/system ladder open. INV-035 allows broad AI-generated hypotheses but no equation is a physical law by declaration.

INV-025/026/027 remain falsifiable goals. The 100× and 100,000,000× cost targets, 100,000,000-GPU and universal 100,000,000-unit replacement, material substitution, commercial ultra-low-cost bio-oil/fusion, lower WACC, and physical Data-Center-to-Phone compression remain unachieved until the appropriate end-to-end evidence gates pass.

## 7. CI, sync and next gate

The previous parent-state CI was green for its exact SHA, but that result does not transfer. The GitHub combined-status query returned no status entries for the newer commits, and the available workflow-run connector returns only PR-triggered runs; therefore this batch does **not** claim that the new exact-head CI passed. The next action is to inspect the actual Actions runs for the final main SHA and repair any failure. If the workflow is not triggered or the result cannot be read, record that limitation rather than inferring success.

**Next highest-value gate:** exact-head prototype/invariant tests and cold-start audit for schema v4; then run the preregistered 30-seed comparison only after source/config/runtime manifests, raw-data provenance and group-disjoint split certificate are pinned. In parallel, keep Lane A provider-neutral lowering on the frozen signed-Max-Cut contract moving. No paid QPU job is authorized.

**Sync:** no feature-branch or unmerged code is claimed. The code/test commits above are on `main`; this batch and the integration record provide the handoff detail. After the initial batch publication, `RESEARCH_GAPS.md` was safely appended in commit [`6534cfd698643470e96730f1821502157932a855`](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/commit/6534cfd698643470e96730f1821502157932a855) and `WORKLOG.md` in commit [`3530a818d8af7bfb86ea46749f93c9e9801071ba`](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/commit/3530a818d8af7bfb86ea46749f93c9e9801071ba). Both appends used the full fetched canonical files (80,902 and 160,886 bytes before append) as exact prefixes; this cycle's aggregate gap/work-log sync debt is resolved without truncating prior history. Exact-head CI remains unverified.
