# Lane A — Quantum Programming / Workloads / Compiler / Runtime

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
