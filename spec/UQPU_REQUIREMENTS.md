# UQPU Functional Requirements Specification

## R1 — No-GPU dependency
A validated UQPU workload must complete without a GPU in the execution path.

## R2 — Functional coverage
The roadmap must cover all workload classes in `docs/GPU_FUNCTIONAL_COVERAGE.md`.

## R3 — Output contract
Each operation declares one of: exact, bounded-error, approximate, sampled, probabilistic.

## R4 — End-to-end accounting
Benchmarks include input transfer, encoding/state preparation, execution, error correction, measurement, decoding, and output transfer.

## R5 — Reversible fallback
Unsupported exact classical operations must have a theoretically valid reversible implementation path.

## R6 — Quantum-native preference
Use a quantum-native algorithm only when estimated total cost is lower or it provides a capability/quality advantage.

## R7 — Whole-graph optimization
Optimize across nominal GPU kernels to avoid unnecessary classical intermediate outputs.

## R8 — Resource transparency
Expose logical qubits, physical-qubit estimate when available, gate counts, non-Clifford count, depth, shots, state-preparation cost, and measurement cost.

## R9 — Reproducibility
Record source workload, compiler version, backend, hardware assumptions, error model, and accuracy threshold.

## R10 — Honest classification
Results use:
- `FUNCTIONALLY_SUPPORTED`
- `COMPETITIVELY_SUPPORTED`
- `QUANTUM_ADVANTAGE_CANDIDATE`
- `NO_ADVANTAGE_FOUND`
- `UNRESOLVED`
