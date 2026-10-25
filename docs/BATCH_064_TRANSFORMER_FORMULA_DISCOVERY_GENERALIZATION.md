# Eight-Lane Research Batch 064 — transformer formula discovery and generalization gate

**Date:** 2026-10-25  
**Starting canonical main SHA:** 70796ef8b918fe2e95382bc49cd7016a825db7e1  
**Primary owner:** Lane F — evidence and benchmark integration  
**Cross-cutting programs:** FND-001–006, EQN-001–006, BIO-001, FUS-001, FIN-001  
**Evidence class:** LITERATURE_ONLY + MODEL_ONLY_SYNTHETIC_CONTRACT_TESTS  
**Promotion:** no physical law, QPU advantage, material substitution, accepted fuel, net electricity, economic advantage or phone-class compression promoted

## Starting-state and invariant audit

The cycle began at the newest main commit, 70796ef8b918fe2e95382bc49cd7016a825db7e1 (2026-10-25 06:28:31 UTC), not a remembered batch. The required charter, version invariants, goals, README, Research Operating System, open-frontier directive, Kanusanan Pongpanna Model, strategic references, root directives 00/00A/01–06, current Batch 063, current research gaps and latest integration/Actions records were inspected. The high-visibility directives and the Thai, English, Chinese, Japanese, Korean and German master-plan links remain preserved. INV-025/026/027 and INV-029–035 remain binding; no large append-only canonical history was rewritten from a partial read.

The starting main head's Prototype/Invariants workflow and Cold-Start Handoff Audit passed. This is starting-head CI evidence only; the new branch must pass its own current-head checks before promotion.

## Literature delta

The official arXiv v1 preprint “Synthesizing Physics Formulae with Transformers” (arXiv:2610.03947, submitted 2026-10-02) reports a formula-trained transformer that synthesizes candidates in roughly ten seconds and improves extrapolation on selected SRBench/LLM-SRBench tasks. The paper also reports a failure regime on LSR-Synth, where physical scales are far from the training distribution, and about two weeks of training on one H100 80 GB GPU for a roughly 145-million-parameter model. These are author-reported literature results, not project measurements. Inference latency excludes training amortization unless explicitly accounted for.

The current repository already contains a symbolic-ensemble interatomic-potential watch and a Batch 063 watch on Physical Law Ecology. The progressive Chain of Symbolic Regression paper is already the subject of an open project PR; this cycle does not duplicate it. The Oct 25 IAEA fusion leads and scalar–tensor no-go preprint are already recorded in Batch 063. No new anomaly or physical law is promoted.

## Implementation and test result

Added a dependency-free matched-budget audit helper and synthetic tests. It rejects inconsistent dataset/split identities, non-distinct train/held-out/extrapolation split hashes, unmatched declared budgets, non-finite errors, duplicate seeds, invalid resource values and inconsistent training accounting for a reused model hash. It reports mean held-out/extrapolation errors by method while retaining constraint failures, counterexamples, false discoveries and failed searches. Training resources are aggregated once per model hash rather than once per seed.

Local smoke suite: 12/12 passed under Python 3.13. This does not establish compatibility with the project's Python 3.10/3.11/3.12 CI matrix; those workflow results are required on the new head. No model was downloaded, no external benchmark was reproduced, no QPU job was submitted, and no physical experiment was performed.

## Explicit A–H status

| Lane | Work this cycle | Status / evidence boundary |
|---|---|---|
| A — Quantum programming/workloads/compiler/runtime | Added a reusable equation-generator comparison gate with matched budgets, held-out/extrapolation metrics and fail-closed input validation. | SOFTWARE_CONTRACT / MODEL_ONLY; no workload or QPU advantage. |
| B — Cloud/QPU/provider integration | Reaffirmed provider-neutral accounting and simulator/dry-run-first policy. | No provider credentials, target job, shots or billable usage. |
| C — RAM/VRAM/HBM/storage/state/data movement | Added peak-memory and optional token/energy fields to the benchmark contract; training resources require a stable model hash. | No quantum-state/classical-storage equivalence or memory advantage measured. |
| D — Devices/chip/process/fabrication/packaging | Reviewed the external H100 training requirement as an infrastructure cost dependency, not a chip result. | No device/process/packaging experiment or yield data. |
| E — Biomass/materials/bio-oil/fusion/energy/cooling | Identified formula discovery as a possible future candidate-generation tool for constitutive models, gated by domain data and experiment. | BIO-001 and FUS-001 remain open; no material, fuel or net-electric result. |
| F — Economics/benchmarks/evidence/integration | Owns the new matched-resource contract, RG-046 and INT-20261025-021. | 12 synthetic unit tests pass locally; scientific replication remains DATA_BLOCKED. |
| G — Quantum-chip manufacturing equipment/software/factory systems | Included training compute/memory/energy provenance as upstream resource inputs to any later device/factory model. | No process-window, equipment, yield or cost-of-fabrication evidence. D/G co-design remains active but unchanged. |
| H — Kanusanan Pongpanna Model strategy/finance/future industries/publication | Published the dated literature watch and mapped model-training amortization to FIN-001/INV-033 and external-infrastructure accounting to INV-029. | Strategic relevance only; no commercial or financial result. |

The repository also has an auxiliary Lane I; it is not used to redefine or replace the required A–H architecture.

## Foundational and equation-discovery progress

- **FND-001:** Batch 063's repeated-seed conditional-mutual-information calibration remains synthetic and estimator-specific; this cycle adds no entropy-production or energy inference.
- **FND-002:** output-information lower bounds remain theoretical/contractual; no new bound or measured output-information result.
- **FND-003:** matched classical-control versus quantum-speed-limit measurement remains open.
- **FND-004:** alternative physical primitives remain hypothesis space only.
- **FND-005:** QFT/elementary-particle mechanism scans remain unvalidated research leads.
- **FND-006:** mathematics-first invention gains a fair-budget candidate-generator comparison contract.
- **EQN-001:** adds a falsifiable comparison between formula-trained transformers and search-based methods.
- **EQN-002:** preserves known-law recovery and held-out/extrapolation checks; no novel law.
- **EQN-003–005:** unchanged; no new physical mechanism or theorem promoted.
- **EQN-006:** strengthens the generator → constraints → evaluator → held-out test → counterexample → proof/simulation → discriminating experiment → independent replication → system consequence → economics pipeline.

## INV-029 through INV-035

- **INV-029:** no Data-Center-to-Phone progress claim. External model-training infrastructure and full lifecycle cost must be counted; a phone terminal or small inference latency does not prove physical compression.
- **INV-030:** no Pangola-carbon functional substitution, elemental transmutation or critical-material reduction demonstrated.
- **INV-031:** no accepted liquid-fuel yield, upgrading or cost result; BIO-001 remains open.
- **INV-032:** no net reliable delivered fusion electricity or lifecycle-cost result; FUS-001 remains open.
- **INV-033:** explicitly accounts for model-training GPU-hours/energy and model-hash identity so training is not counted once per inference seed; actual dollar cost and amortization volume remain unmeasured.
- **INV-034:** expands the mathematics-first candidate search while preserving incumbent physical constraints.
- **INV-035:** AI-generated formulae remain hypotheses; no candidate becomes a physical law without the required falsification, experiment and independent validation.

## Integration and next gate

Primary artifact: software/uqpu-prototype/uqpu/formula_discovery_benchmark.py. Tests: software/uqpu-prototype/tests/test_formula_discovery_benchmark.py. Literature watch: docs/literature_watch/2026-10-25-transformer-physics-formula-synthesis.md. Gap: docs/RESEARCH_GAP_RG046_TRANSFORMER_FORMULA_GENERALIZATION.md. Machine-readable integration: integration/INT-20261025-021-TRANSFORMER-FORMULA-GENERALIZATION.json. Local smoke evidence: benchmarks/results/formula-discovery-benchmark-contract-smoke-2026-10-25.json.

Next highest-value gate: run the project Python 3.10/3.11/3.12 matrix and full current-head QSP/QSVT/invariant/cold-start workflows; then pin the paper's source/weights/data and run a matched-budget, at-least-30-seed replication with independent split validation. No paid QPU jobs, material experiments, fabrication, purchases or funding actions were authorized.
