# Research cycle — 2026-10-25: BIC candidate-count stability

**Canonical starting main:** `b5aac63f295c2b586f044bcbb228ad0ffb0660ef`  
**Primary owner:** Lane A — quantum programming, workloads and equation-discovery tooling  
**Integration owner:** Lane F — benchmark/evidence/economics  
**Publication owner:** Lane H — strategic research publication  
**Evidence class:** SOFTWARE + UNIT TESTS + LITERATURE_ONLY  
**Promotion:** no real-QPU advantage, physical law, material substitution, accepted fuel, net-fusion-electricity, WACC reduction or Data-Center-to-Phone result promoted.

## 1. Canonical state and governance audit

Started from the current default branch, not a remembered batch number. Reviewed `PROJECT_CHARTER.md`, `VERSION_INVARIANTS.md`, `GOALS.md`, `README.md`, `docs/RESEARCH_OPERATING_SYSTEM.md`, `docs/OPEN_FRONTIER_RESEARCH_DIRECTIVE.md`, `docs/KANUSANAN_PONGPANNA_MODEL.md`, `STRATEGIC_PLAN_REFERENCES.md`, the current gaps and newest committed Batches 059–063, the latest daily reconciliation and pending-main sync record. Verified the eight high-visibility root directives (00, 00A, 01–06) remain present.

The six multilingual strategic master-plan editions/links (Thai, English, Chinese, Japanese, Korean and German), the strategic AI-agent/funding references, INV-025/026/027 and INV-029–035 remain preserved. No append-only `RESEARCH_GAPS.md` or `WORKLOG.md` rewrite was attempted from partial excerpts. The directory architecture still uses `research_lanes/` and `integration/`; no new deep directory hierarchy is introduced.

At starting main `b5aac63`, the latest Prototype/Invariants run `40188356586` and Cold-Start Handoff Audit `40188356599` both completed successfully. Current open PR #98's exact head `0730fdaf` also has a successful prototype workflow; PR #99's exact head `003fc399` has a successful extended prototype workflow and cold-start audit. These are separate unmerged branches and are not evidence that their contents have reached main.

## 2. Lane A implementation

The Batch 063 BIC comparator chooses a candidate count using
`BIC = n log(RSS/n) + p log(n)`. A single winning run can hide instability under seed/noise changes, so this cycle adds `evaluate_bic_selection_stability` to `software/uqpu-prototype/uqpu/equation_discovery.py`.

The helper requires:
- at least two nonempty, named replicate records;
- exact agreement between replicate IDs and per-replicate sample counts;
- the same candidate-count set and a shared free-parameter map for each replicate;
- the existing fail-closed BIC input validation on every replicate;
- a preregistered minimum winning fraction in (0, 1];
- a unique plurality meeting that fraction before returning a stable selected count.

A tie is unstable even when the configured threshold is 0.5. The result records every replicate's selected count and the per-candidate win count/frequency. Four tests cover a 4/5 selection threshold, a tie, missing/mismatched replicate metadata, and invalid thresholds.

**Scope:** this is a selection-stability diagnostic. It cannot make correlated or duplicated samples independent, prove the candidate pool is complete, establish identifiability, or replace held-out generalization, counterexample search, proof and experiment. It is not a reproduction of SMILE or Physical Law Ecology.

## 3. Fresh literature surveillance

Fresh public searches covered symbolic regression/neural-symbolic equation discovery, formal theorem discovery, physics-constrained constitutive modeling, automated discovery, quantum-memory/thermodynamic limits and energy/fusion terms.

A material method signal not indexed by the current main-branch search was found: Montazerin, Ortega and Srivastava, “SMILE: Bridging Continuous Optimization and Discrete Symbolic Recovery,” arXiv:2609.04639, first submitted 2026-09-04. A dated Lane H literature-watch article was added at `docs/literature_watch/2026-10-25-smile-continuous-discrete-symbolic-recovery.md`.

The article distinguishes continuous optimization used to guide search from the discrete symbolic expression that must still pass independent tests. The reported SRBench results are preprint claims; target-domain generalization, benchmark/split audit, matched compute/energy budgets, noise robustness, operator coverage and physical validation remain open. No other newly surfaced result in this pass changes UQPU, biomass, fuel, fusion or financing evidence. This is a search boundary, not proof that no other relevant paper exists.

## 4. Explicit A–H status

- **A — Quantum programming/workloads/compiler/runtime (Priority #1):** added replicate-level BIC stability accounting and four regression tests. The identical useful-output/QUBO-QAOA/reference-certificate path remains the priority; no application-level quantum advantage established.
- **B — Cloud/QPU/provider integration:** provider-neutral and D-Wave serialization work is in PR #99, not main. No paid job submitted; credentials, bounded budget and explicit consent remain prerequisites.
- **C — RAM/VRAM/HBM/storage/state/data movement:** stability records are classical metadata, not readable memory capacity. State preparation, output information, I/O, host memory and transfer remain separately costed.
- **D — Quantum/photonic/semiconductor devices, fabrication and packaging:** no new device result. D/G co-design remains necessary; native resource, yield, process-window, packaging, calibration and lifetime evidence are open.
- **E — Pangola carbon, materials, bio-oil, fusion, cooling and infrastructure:** no material or fuel experiment and no net-electricity result. BIO-001 accepted-liquid mass/energy/cost closure remains open. FUS-001's plasma-to-net-electricity evidence gate is in PR #99 and remains unmerged.
- **F — Economics, benchmarks, evidence and integration:** the stability result makes model-selection variability visible; no cost claim follows until search/training/inference/retries, host compute, energy and accepted-output costs are matched.
- **G — Quantum-chip manufacturing equipment/software/factory systems:** no manufacturing result. The next valid bridge is from reproducible device resource requirements to process/yield/tooling and cost models.
- **H — Strategy, finance and publication:** published the dated SMILE literature watch and preserved the strategic master-plan links; no strategic valuation, funding or WACC claim is promoted.

## 5. Foundational physics and equation discovery

- **FND-001:** the recent memory-order/thermodynamic diagnostic remains a synthetic estimator; calibration, uncertainty and matched control-vs-quantum-speed-limit energy/time measurements remain open.
- **FND-002:** output-information lower bounds remain a contract/boundary condition, not a claim that Hilbert-space dimension is readable classical storage.
- **FND-003:** matched control-vs-QSL measurement still needs same-output, same-quality, same-boundary and full-system energy accounting.
- **FND-004:** alternative physical primitives remain hypotheses until a distinct observable and independent experimental path are specified.
- **FND-005:** QFT/particle mechanism scans remain literature/theory work; no particle-to-technology effect is promoted.
- **FND-006:** advanced statistical model-count robustness by recording replicate-to-replicate selection, with failed/unstable outcomes retained.
- **EQN-001–006 / INV-035:** the discovery chain remains generator -> explicit constraints -> evaluator -> held-out/generalization -> counterexample -> proof/simulation -> discriminating experiment -> independent replication -> device/system consequence -> economics. BIC or symbolic fit alone is not physical truth.

## 6. INV-029–035 mission traceability

- **INV-029:** no physical data-center-to-phone compression; capability, energy, form-factor and lifecycle-cost contracts still gate the mission.
- **INV-030:** no elemental transmutation or material substitution claim; a future constitutive candidate must be tied to accepted function and measurements.
- **INV-031:** no saleable-liquid yield or cost evidence; BIO-001 remains open.
- **INV-032:** no reliable net delivered fusion electricity or lifecycle-cost evidence; FUS-001 remains open.
- **INV-033:** no measured principal, time-to-evidence, interest or WACC reduction; model-search compute accounting is a future finance input only.
- **INV-034:** the foundational agenda remains active through bounded model-selection and falsification work.
- **INV-035:** candidate generation remains open-ended; physical claims remain evidence-gated.

## 7. Evidence, gaps, sync and next gate

**Positive evidence:** implementation and regression tests are committed to this branch; the fresh SMILE method lead is documented with limitations and a falsifiable follow-up.  
**Negative/remaining evidence:** no independent SMILE reproduction, no matched benchmark/energy run, no held-out physical-law discovery, no QPU job, no materials/fuel/fusion measurement and no economic advantage.  
**Sync debt:** the full `RESEARCH_GAPS.md` and `WORKLOG.md` histories were left intact. The transformer-formula work (PR #98) and FUS-001/no-go work (PR #99) remain separate from main until reviewed/merged; do not imply their contents are canonical.  
**CI:** exact-head runs for this branch must complete before the implementation is considered validated; starting-main and other-PR successes do not validate this branch.  
**Next highest-value gate:** run the new tests plus full Python 3.10/3.11/3.12 and project invariants workflow; then use a pinned known-law fixture suite with preregistered seeds/noise, matched search budgets, blind scale-shift holdouts, and counterexample checks. Publish selection instability and false discoveries, not only the winning formula.
