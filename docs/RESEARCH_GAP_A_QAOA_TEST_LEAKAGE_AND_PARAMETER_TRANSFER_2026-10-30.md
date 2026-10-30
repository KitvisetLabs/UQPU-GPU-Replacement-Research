# Research gap — RG-A-QAOA-TEST-LEAKAGE-001: parameter transfer without test-objective adaptation

**Opened:** 2026-10-30  
**Primary owner:** Lane A — workloads/compiler/runtime  
**Evidence/integration owner:** Lane F  
**Cross-lane interfaces:** B (SDK/target identity), C (state/I/O), D/G (mapping and native topology), H (provenance/publication)  
**Related:** SIGNED-MAXCUT-PARITY-QAOA-001, INV-025/026/027/029, FND-002/003, EQN-002/004  
**Status:** OPEN / V1 PROTOCOL SUPERSEDED FOR GENERALIZATION / V2 CONTRACT ADDED / NO QAOA RUN  
**Evidence class:** SOFTWARE_CONTRACT; no optimizer or hardware result.

## Finding

The original Batch 143 manifest allowed per-instance variational-angle optimization on test objectives while describing the test split as final evaluation only. That is test-objective adaptation, not a clean family-held-out evaluation. Public exact references may be used for scoring and audit, but the optimizer must not query test objective values or test optima.

The original v1 manifest and references are preserved unchanged as historical artifacts. They must not be used to support a strict held-out generalization claim. Batch 145 adds a versioned v2 manifest and matching exact-reference file; the v2 policy freezes a train-derived parameter vector, uses validation only for preregistered method/hyperparameter selection, and reserves test instances for final evaluation and scoring.

## V2 protocol contract

- Train split only: optimizer objective evaluations and parameter fitting.
- Validation split only: select among preregistered methods/hyperparameters; do not inspect test outcomes.
- Test split only: final evaluation with frozen parameters. No per-instance test-objective adaptation.
- Exact references: scoring/audit only; never parameter, model, threshold or hyperparameter selection.
- Preserve graph-family disjointness and the original signed-Max-Cut useful-output contract.
- Use identical target/configuration, shots, optimizer budgets, repetitions, calibration/pricing snapshot and acceptance thresholds for direct and parity methods.
- Report quality/regret, accepted-solution probability, optimizer evaluations, qubits, native/routed gates and depth, retries, mitigation/decoding, host time, state/I/O/transfer/memory, reconstruction, billable usage, energy where measurable and total cost per accepted useful task.
- Keep the public test set's limitations explicit; it is family-held-out relative to train/validation, not a secret benchmark.

## Unlock criteria

1. Pass the v2 manifest policy regression test and exact-reference hash binding.
2. Implement a paired runner that can prove no test objective is sent to an optimizer or parameter-selection routine.
3. Independently validate objective sign, qubit order, parity constraints, decoder and exact references.
4. Validate the lowering/circuit with an independent SDK, then run target-aware simulation with equal budgets.
5. Compare direct and parity approaches on the same target and configuration; separate optimization shots from final evaluation shots.
6. Only after simulation gates pass may a real-QPU run be considered, and only with credentials, explicit user consent and a bounded budget.

**Non-claims:** no QAOA optimizer was run; no SDK or target-aware simulation was performed; no QPU advantage, memory replacement or economic advantage is established.
