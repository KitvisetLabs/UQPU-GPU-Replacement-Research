# Batch 053 — QOS phase-synthesis execution gate

## Gate

`QOS-AUDIT-010B2` executes the Batch-052 frozen public interface against the exact Batch-051 coefficient fingerprint.

The CI job installs `qsppack==0.3.0` plus the explicitly pinned missing runtime dependency `sympy==1.14.0`, checks the environment with `pip check`, imports the package, and executes `synthesize_with_pinned_qsppack()` with the frozen Newton/parity/target/convention settings.

## Observed result

CI run 423 reached the solver after the runtime dependency closure passed. The pinned call raised:

`ValueError: could not broadcast input array from shape (41,) into shape (42,)`

No phase vector was produced. This is preserved in `benchmarks/results/batch053-qos-phase-synthesis-failure.json`.

A separate harness defect was also found: Batch 052 had reimplemented the coefficient fingerprint with a different serialization than Batch 051, so the reported runtime fingerprint was not comparable to the frozen certificate fingerprint. This branch now imports the Batch-051 `coefficient_fingerprint()` directly and fails closed on a real mismatch.

## Public implementation evidence

The upstream QSPPACK examples pass only the definite-parity Chebyshev subsequence to the solver (for example, `coef = coef(parity+1:2:end)` before `QSP_solver`). Therefore the observed 41-to-42 broadcast exception is not, by itself, evidence that a full 82-entry Chebyshev vector should be supplied. The next audit must locate the exact Python 0.3.0 shape assumption or test a separately pinned solver/method without silently changing the polynomial contract.

## Evidence level

`PINNED_PUBLIC_NUMERICAL_PHASE_SYNTHESIS_EXCEPTION`.

This is implementation/interface execution evidence only. It is not evidence that the Batch-051 polynomial is mathematically unrealizable by QSP, and it is not an independent QSP reconstruction or theorem proof.

## Acceptance boundary

A phase vector may be frozen only after a pinned solver returns convergence for the exact Batch-051 fingerprint. Independent reconstruction must then use repository-owned matrix-product code rather than the synthesis package's response helper.

## Non-claims

This batch does not claim real-QPU execution, quantum advantage, theorem-certified QSP/QSVT correctness, full-channel D.23, GPU/NPU/RAM/DRAM/HBM replacement, >=100x, >=100,000,000x, measured economic advantage, or a new physical law.

## Next gate

`QOS-AUDIT-010B2A`: reproduce and isolate the QSPPACK 0.3.0 41-to-42 shape exception against a minimal odd-parity fixture and the degree-81 candidate, inspect the pinned implementation's expected dimensions, and compare at least one separately pinned synthesis method/implementation if necessary. Preserve all failures; do not weaken Batch-051 boundedness or target-error requirements.
