# Lane A — Quantum Programming / Workloads / Compiler / Runtime

**Priority:** #1, while all eight lanes remain active.

## Scope
Quantum programming models, algorithms, semantic IR, workload contracts, compiler/lowering, runtime orchestration, hybrid execution, complexity research and provider-neutral workload preparation.

## Integration responsibilities
A supplies useful-output/workload contracts to B-H. It consumes provider constraints from B, state constraints from C, hardware constraints from D/G, material/infrastructure constraints from E, benchmark/economic gates from F and strategic sequencing from H.

## Future structure
Special projects may add `algorithms/`, `compiler/`, `runtime/`, `workloads/`, `experiments/`, `references/` or other subfolders as needed, subject to the repository-wide 16-level depth limit.


## Current reproducibility gate — 2026-10-29

- [Exact 2x2 Hermitian reference contract](SMALL_HAMILTONIAN_REFERENCE_CONTRACT_2026-10-29.md) defines the bounded analytic fixture, fail-closed tests and next sparse-oracle gate.
- Canonical implementation: `software/uqpu-prototype/uqpu/small_hamiltonian_reference.py`.
- Focused gap: `docs/RESEARCH_GAP_A_FND002_EXACT_2X2_REFERENCE_2026-10-29.md`.


## Current RAG/QUBO comparison gate — 2026-10-29

- [Machine-readable RAG context-selection contract](RAG_CONTEXT_SELECTION_CONTRACT_2026-10-29.json) freezes the task/manifest/acceptance boundary before any run.
- Source watch: `docs/literature_watch/2026-10-29-pdcim-near-memory-isings-for-rag.md`; focused gap: `docs/RESEARCH_GAP_PDCIM_MATCHED_QUBO_RAG_COMPARISON_2026-10-29.md`.
- Regression guard: `software/uqpu-prototype/tests/test_rag_context_selection_contract.py`.
- p-DCIM is a classical near-memory baseline; larger source-paper workloads are model-based. No UQPU reproduction or quantum advantage is claimed.
