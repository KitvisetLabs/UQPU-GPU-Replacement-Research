# Eight-Lane Batch 010 — Reference Generation Pipeline

## Advance
Batch 010 turns RG-024 from a schema-only gap into an executable certificate-generation path.

The optional OR-Tools CP-SAT baseline can now produce a provenance-bearing reference certificate for the exact same versioned benchmark contract.

Evidence rule:
- solver status **OPTIMAL** -> `EXACT_OPTIMUM`;
- merely **FEASIBLE** -> `BEST_KNOWN_FEASIBLE`, never proof-quality evidence.

A JSON manifest writer records certificate ID, contract ID, objective, method, evidence level, source, runtime, solver status and whether optimality was proven.

## Why this matters
The project can now mechanically prevent a time-limited classical incumbent from being mislabeled as the true optimum. That is necessary before QPU output-quality comparisons are meaningful.

## Remaining blocker
The default CI environment does not install OR-Tools, so this batch tests certificate semantics with controlled solver-result fixtures. A dedicated benchmark environment must execute the optional solver and record real hardware/software provenance before RG-024 can close.

## Eight-lane integration
A: benchmark quality gate strengthened.
B: identical contract remains ready for QUBO provider lowering.
C: no new memory-performance claim.
D/G: process-window framework remains pending numeric calibration.
E: functional-unit material economics remains pending sourced comparisons.
F: proof-strength provenance is now machine-readable.
H: evidence-gated strategy remains the publication/governance rule.

No quantum advantage or >=100x result is claimed.
