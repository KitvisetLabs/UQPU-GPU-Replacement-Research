# Daily cycle — 2026-10-29 — sparse state-preparation Toffoli-cost model alignment

## Integrated decision

A new-to-repository peer-reviewed result on sparse quantum state preparation was recorded in the Lane A literature watch. The result is relevant to initialization cost, but the headline metric is Toffoli count and cannot be treated as T-count, circuit depth, runtime, energy or cost per accepted task.

## Artifacts

- Batch: [Batch 134](../docs/BATCH_134_SPARSE_STATEPREP_TOFFOLI_MODEL_ALIGNMENT.md)
- Literature watch: [Rupprecht–Wölk sparse state preparation](../docs/literature_watch/2026-10-29-sparse-stateprep-improved-toffoli-cost.md)
- Focused gap: [Toffoli model alignment](../docs/RESEARCH_GAP_SPARSE_STATEPREP_TOFFOLI_MODEL_ALIGNMENT_2026-10-29.md)
- Preregistered benchmark: [SPARSE_STATEPREP_TOFFOLI_BENCHMARK_V1](../research_lanes/A_quantum_programming_runtime/SPARSE_STATEPREP_TOFFOLI_BENCHMARK_V1.json)
- Regression guard: [test_sparse_stateprep_toffoli_contract.py](../software/uqpu-prototype/tests/test_sparse_stateprep_toffoli_contract.py)
- Machine-readable record: [INT-20261029-SPARSE-STATEPREP-TOFFOLI](INT-20261029-SPARSE-STATEPREP-TOFFOLI.json)

## A–H integration

A owns the algorithm and benchmark; C tracks classical description, state/I/O and readable-memory semantics; F owns evidence labels and total cost; B retains provider-neutral, no-paid-job rules; D/G translate logical resources into device/manufacturing consequences; E continues independent BIO-001/FUS-001 work; H preserves strategy and provenance. No lane was suspended, and D/G co-design remains continuous.

## Cross-cutting invariants

INV-029 is unchanged at mission level. INV-030–033 have no new evidence from this algorithmic paper. INV-034 requires formal assumption alignment, exact small cases and counterexamples; INV-035 requires falsifiable held-out predictions and independent verification before any claim promotion. INV-025/026/027 remain active.

## Decision and next gate

Keep the external result at literature-only status. The next gate is an independent small-instance circuit reproduction and a theorem-assumption matrix comparing the paper's Toffoli metric with the existing T-count and sparse-QROM contracts. No real-QPU run, physical memory equivalence or economic advantage is claimed.
