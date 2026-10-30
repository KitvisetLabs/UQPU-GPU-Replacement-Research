# Lane A — Quantum Programming / Workloads / Compiler / Runtime

## 2026-10-30 — goal-only baseline and equation-frontier gates

- [Goal-only GPU baseline contract](GOAL_ONLY_GPU_KERNEL_BASELINE_CONTRACT_2026-10-30.md), validator and 10 synthetic tests; no hardware benchmark.
- [Exact pair GLE contract](EXACT_GLE_PAIR_COORDINATE_ACCEPTANCE_CONTRACT_2026-10-30.md); full source still required.
- [Boson-star branch PINN contract](BOSON_STAR_BRANCH_SURROGATE_ACCEPTANCE_CONTRACT_2026-10-30.md); branch-disjoint reproduction remains open.

**Priority:** #1, while all eight lanes remain active.

## Scope
Quantum programming models, algorithms, semantic IR, workload contracts, compiler/lowering, runtime orchestration, hybrid execution, complexity research and provider-neutral workload preparation.

## Integration responsibilities
A supplies useful-output/workload contracts to B-H. It consumes provider constraints from B, state constraints from C, hardware constraints from D/G, material/infrastructure constraints from E, benchmark/economic gates from F and strategic sequencing from H.

## Future structure
Special projects may add `algorithms/`, `compiler/`, `runtime/`, `workloads/`, `experiments/`, `references/` or other subfolders as needed, subject to the repository-wide 16-level depth limit.


## Open-system generator cross-check — 2026-10-29

- [Amplitude-damping fixture contract](OPEN_QSYS_AMPLITUDE_DAMPING_FIXTURE_2026-10-29.md) adds a second analytically known generator beside the pure-dephasing fixture.
- The evaluator returns per-basis-image invariance membership and separately checks operator-algebra closure; tests preserve both invariant/non-algebra and closed/non-invariant negative controls.
- This is MODEL_ONLY. The full restricted-measurement benchmark, >=30-seed family/regime holdouts, uncertainty/abstention and resource accounting remain open.

## Current reproducibility gate — 2026-10-29

- [Exact 2x2 Hermitian reference contract](SMALL_HAMILTONIAN_REFERENCE_CONTRACT_2026-10-29.md) defines the bounded analytic fixture, fail-closed tests and next sparse-oracle gate.
- Canonical implementation: `software/uqpu-prototype/uqpu/small_hamiltonian_reference.py`.
- Focused gap: `docs/RESEARCH_GAP_A_FND002_EXACT_2X2_REFERENCE_2026-10-29.md`.


## Current RAG/QUBO comparison gate — 2026-10-29

- [Machine-readable RAG context-selection contract](RAG_CONTEXT_SELECTION_CONTRACT_2026-10-29.json) freezes the task/manifest/acceptance boundary before any run.
- Source watch: `docs/literature_watch/2026-10-29-pdcim-near-memory-isings-for-rag.md`; focused gap: `docs/RESEARCH_GAP_PDCIM_MATCHED_QUBO_RAG_COMPARISON_2026-10-29.md`.
- Regression guard: `software/uqpu-prototype/tests/test_rag_context_selection_contract.py`.
- p-DCIM is a classical near-memory baseline; larger source-paper workloads are model-based. No UQPU reproduction or quantum advantage is claimed.


## Equation-discovery matched-metric gate — 2026-10-29

- Shared prototype helper: software/uqpu-prototype/uqpu/equation_discovery_benchmark.py.
- Regression tests: software/uqpu-prototype/tests/test_equation_discovery_benchmark.py.
- The helper checks grouped split disjointness and paired held-out errors; it does not parse equations or prove semantic equivalence. See docs/RESEARCH_GAP_EQN_DISCOVERY_MATCHED_ROBUSTNESS_2026-10-29.md.


## Equation-discovery robustness gate — 2026-10-29
- [Batch 120 finite-value validation](../../docs/BATCH_120_FINITE_EQUATION_METRICS_AND_EVIDENCE_GATE.md) closes a fail-open edge case where NaN/infinite or boolean held-out errors could pass a simple non-negative check.
- Regression coverage is in `software/uqpu-prototype/tests/test_equation_discovery.py`; this guards numeric inputs only, not semantic equivalence or physical validity.


## Time-dependent PDE surrogate gate — 2026-10-29

- [TINN acceptance contract](TINN_TIME_DEPENDENT_PDE_ACCEPTANCE_CONTRACT_2026-10-29.md) preregisters a known-law comparison against conventional PINNs, compatible operator-splitting methods and a converged solver reference.
- The contract requires grouped trajectory/regime holdouts, matched budgets, physical residual/conservation/bound metrics, failure retention and memory/I/O/energy/cost accounting. External source claims remain unreproduced; see [focused gap](../../docs/RESEARCH_GAP_TINN_TIME_DEPENDENT_PDE_GENERALIZATION_2026-10-29.md).


## Duplicate-key JSON provenance guard — 2026-10-30

The sparse-state-preparation asset manifest remains `SOURCE_METADATA_ONLY`. The associated regression test now parses with an `object_pairs_hook` that rejects repeated keys recursively and includes a synthetic conflicting-`evidence_class` test. This prevents silent last-key-wins ambiguity in future evidence manifests. It does not verify downloaded bytes, source checksums, dependencies, the external circuit, physical resources or economics. See [Batch 136](../../docs/BATCH_136_JSON_PROVENANCE_GUARD_AND_GENESIS_WATCH.md) and [integration report](../../integration/DAILY_CYCLE_2026-10-30_JSON_PROVENANCE_GUARD.md).


## Scaling-exponent identifiability gate — 2026-10-30

- [Reference baseline](../../software/uqpu-prototype/uqpu/scaling_exponent_baseline.py) and [seven synthetic tests](../../software/uqpu-prototype/tests/test_scaling_exponent_baseline.py) cover exact positive power-law recovery, held-out-scale prediction, unit rescaling and degenerate-design rejection.
- [Acceptance contract](SCALING_EXPONENT_IDENTIFIABILITY_CONTRACT_2026-10-30.md), [focused gap](../../docs/RESEARCH_GAP_SCALING_EXPONENT_IDENTIFIABILITY_2026-10-30.md), and [literature watch](../../docs/literature_watch/2026-10-30-scaling-exponent-identifiability-msn-pinn.md) make the external-method and physical-law boundaries explicit.
- The isolated synthetic harness passed 7/7 tests. The external MSN-PINN method remains unreproduced; exact-head CI must be observed.


## Derivative-constrained PDE surrogate method watch — 2026-10-30

- [DC-PINN literature watch](../../docs/literature_watch/2026-10-30-derivative-constrained-pinns-equation-discovery.md) records the peer-reviewed APS method as external and unreproduced.
- [Focused reproduction gap](../../docs/RESEARCH_GAP_DCPINN_REPRODUCTION_2026-10-30.md) requires source/data/license pinning, equal-resource baselines, frozen spatiotemporal holdouts, derivative-constraint counterexamples, and full runtime/memory accounting.
- No PDE surrogate, physical equation, or engineering benefit is promoted from the paper abstract alone.


## 2026-10-30 — signed-Max-Cut parity held-out manifest

- Stable gate: A-GATE-PARITY-QAOA-HELDOUT-MANIFEST-001.
- [Frozen 10-instance manifest](../../benchmarks/manifests/qaoa-parity-heldout-2026-10-30.json) and [exact logical reference certificates](../../benchmarks/references/qaoa-parity-exact-references-2026-10-30.json).
- [Six manifest/reference tests](../../software/uqpu-prototype/tests/test_qaoa_parity_heldout_manifest.py).
- Split: 4 train / 3 validation / 3 test, with disjoint graph families; exact enumeration covers 688 logical assignments and complete argmax sets.
- Same decoded signed-Max-Cut objective; parity outputs must satisfy all cycle constraints; normalized regret threshold 0.05.
- Proposed equal p=1 budgets: 8,192 shots, 32 optimizer evaluations and 10 repetitions per instance/method.
- Status: PREREGISTERED_NOT_EXECUTED. Six isolated local tests passed. No QAOA optimizer, SDK, target-aware simulator or QPU run was performed.


## 2026-10-30 — Batch 144 exact mapping audit

- [Batch report](../../docs/BATCH_144_PARITY_QAOA_EXACT_MAPPING_AUDIT.md) and [daily integration](../../integration/DAILY_CYCLE_2026-10-30_PARITY_QAOA_MAPPING_AUDIT.md).
- Added `tests/test_qaoa_parity_heldout_mapping.py`: all 10 frozen signed-Max-Cut fixtures, 688 logical assignments, 7,072 physical parity strings, direct-QUBO exact baseline, parity exact certificate, fail-closed decoding and argmax correspondence.
- Evidence: software contract + model-only exact small-instance reference. No QAOA optimizer, SDK, target-aware simulation, QPU execution or advantage claim.
- Next: paired direct/parity optimizer/sampler under the frozen equal budgets; validate bit order, operator sign and decoder independently first.


## 2026-10-30 — equation-discovery runtime and QAOA holdout gate

- Literature interface: [SRHarness v2 and structure-preserving equation-discovery watch](../../docs/literature_watch/2026-10-30-agentic-equation-discovery-and-constitutive-models.md). Persistent scientific state, a common evaluator and trajectory provenance are candidate design patterns for `equation_discovery.py`; no code adoption or license approval is claimed.
- **Protocol defect found before execution:** `benchmarks/manifests/qaoa-parity-heldout-2026-10-30.json` describes test as final-evaluation-only but allows per-instance variational-angle optimization on test objectives. That is test-objective adaptation, not held-out generalization. Next gate: freeze shared angles/hyperparameters using train/validation only, or create a separate adaptation track with disjoint optimization and final-evaluation shots and label it non-generalization.
- No QAOA optimizer, simulator or QPU job was run in this cycle.
