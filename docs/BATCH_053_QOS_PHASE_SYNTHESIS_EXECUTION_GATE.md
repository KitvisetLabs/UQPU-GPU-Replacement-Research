# Batch 053 — QOS phase-synthesis execution gate

## Gate

`QOS-AUDIT-010B2` executes the Batch-052 frozen public interface against the exact Batch-051 coefficient fingerprint in CI.

The CI job installs `qsppack==0.3.0` in Python 3.12 and executes `synthesize_with_pinned_qsppack()` with the frozen Newton/parity/target/convention settings. The emitted JSON is uploaded as the `batch053-qos-phase-synthesis` workflow artifact whether numerical synthesis converges or not. Solver non-convergence is preserved as research evidence; only coefficient-contract corruption fails the runner.

## Public implementation evidence

QSPPACK's public solver documentation specifies that `solve(coef, parity, opts)` accepts the nonzero definite-parity Chebyshev coefficients ordered low-to-high and reports phase factors plus `converged`, `value`, `iter`, parity, target and phase-type metadata. Batch 052 pinned that interface to version 0.3.0. Batch 053 turns the previously pending execution into a repository CI gate.

## Evidence level

`PINNED_PUBLIC_NUMERICAL_PHASE_SYNTHESIS_EXECUTION` if the CI artifact reports `SYNTHESIS_CONVERGED`; otherwise `PINNED_PUBLIC_NUMERICAL_PHASE_SYNTHESIS_FAILURE` with the exact status/exception retained.

Neither outcome is an independent QSP reconstruction or a theorem proof.

## Acceptance boundary

A converged phase vector may be frozen only after the CI artifact is inspected. Independent reconstruction must use repository-owned matrix-product code rather than QSPPACK's `get_entry`; that is a separate gate.

## Non-claims

This batch does not claim real-QPU execution, quantum advantage, theorem-certified QSP/QSVT correctness, full-channel D.23, GPU/NPU/RAM/DRAM/HBM replacement, >=100x, >=100,000,000x, measured economic advantage, or a new physical law.

## Next gate

If synthesis converges: `QOS-AUDIT-010B3` freezes the phase vector and independently reconstructs the QSP response with an explicit convention map to the Batch-036 interface.

If synthesis fails: preserve the failure and audit feasibility margin/solver-method sensitivity without weakening the Batch-051 boundedness or target-error requirements.
