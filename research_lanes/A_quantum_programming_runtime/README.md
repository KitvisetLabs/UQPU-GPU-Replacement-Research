# Lane A — Quantum Programming / Workloads / Compiler / Runtime

**Priority:** #1, while all eight lanes remain active.

## Scope
Quantum programming models, algorithms, semantic IR, workload contracts, compiler/lowering, runtime orchestration, hybrid execution, complexity research and provider-neutral workload preparation.

## Integration responsibilities
A supplies useful-output/workload contracts to B-H. It consumes provider constraints from B, state constraints from C, hardware constraints from D/G, material/infrastructure constraints from E, benchmark/economic gates from F and strategic sequencing from H.

## Future structure
Special projects may add `algorithms/`, `compiler/`, `runtime/`, `workloads/`, `experiments/`, `references/` or other subfolders as needed, subject to the repository-wide 16-level depth limit.


## Current gate — 2026-10-23

QOS-AUDIT-010B25 remains the next target-specific transition gate. Lane A does not alter the frozen QSVT circuit or claim native conformance until Lane B supplies a passing, fresh, digest-bound redacted target snapshot. The accepted QOS-AUDIT-010B20/22 routed probes remain finite simulation evidence only; full-operator equivalence, hardware quality, accepted useful-output quality and cost advantage remain unaccepted.

See docs/BATCH_057_READONLY_SNAPSHOT_OFFLINE_VALIDATOR_AND_LITERATURE.md for the current dependency and next gate.

## Delta 25 — adaptive-circuit semantic gate (2026-10-23)

The provider-neutral contract is implemented at `software/uqpu-prototype/uqpu/adaptive_circuit_contract.py`. It requires target-specific source provenance and explicit mid-circuit measurement, reset and classical-conditional fields. Fifteen focused adversarial tests passed in an isolated Python 3.13 harness; hosted CI remains the integration gate. This is a capability/lowering contract only, not execution permission or useful-task acceptance.

See `integration/adaptive_circuit_capability_contract.md` and `docs/BATCH_058_ADAPTIVE_CIRCUIT_CAPABILITY_CONTRACT.md`.
