# FND-QFI-001 — GHZ QFI analytic audit

**Date:** 2026-10-23  
**Primary implementation owner:** Lane A — quantum programming/runtime  
**Cross-cutting programs:** FND-002, FND-003, FND-006, EQN-001, EQN-004, INV-034, INV-035  
**Evidence class:** MODEL_ONLY  
**Project evidence promotion:** none

## Purpose

The 21 October 2026 preprint by Qi Liu, Xin-Yu Hao and Jing Liu, “Evaluation of the quantum Fisher information for large systems via an ancilla” (arXiv:2610.29146v1), gives a scoped no-go condition for perfect transfer of system quantum Fisher information (QFI) to a lower-dimensional ancilla under its specified controlled-unitary protocol and an already-optimal projective measurement. The condition is that the number m of distinct nonzero score values, d(log p_i)/dx, exceeds ancilla dimension n.

This run adds a small deterministic audit for the paper’s worked GHZ measurement example. It checks the direct-measurement classical Fisher information (CFI) against the known N-squared QFI and records the theorem’s m > n precondition without claiming to reproduce the ancilla protocol or prove the theorem.

## Implementation and reproducibility

- Module: software/uqpu-prototype/uqpu/qfi_ancilla_transfer_audit.py
- Tests: software/uqpu-prototype/tests/test_qfi_ancilla_transfer_audit.py
- Result: benchmarks/results/fnd-qfi-001-ghz-analytic-audit.json
- Integration edge: INT-20261023-001
- Local validation: 6/6 focused unittest cases passed on CPython 3.13.5.
- Phase: x = 0.173 radians, chosen away from singular score/probability points.
- Tested system sizes: N = 1, 2, 3, 5, 8; QFI/CFI agree within the stated tolerance.
- For N = 6, the generic GHZ measurement has m = 2 score classes. With ancilla dimension 2, m > n is false; with dimension 1, m > n is true. This only classifies the paper’s precondition.
- Provider jobs = 0; shots = 0; measured energy and cost are null.

## Evidence boundary and limitations

The direct GHZ formula is a consistency check, not an independent reproduction of Theorem 2. The implementation does not construct or optimize the controlled unitaries T_i, compute the reduced ancilla density matrix/QFI, prove attainability when m <= n, or demonstrate a transfer gap when m > n. The theorem’s assumptions and the notation mismatch flagged in the 23 October literature watch still require independent mathematical review.

No conclusion follows about arbitrary quantum compression, classical-readable memory, RAM/VRAM/storage, computational advantage, real-QPU performance, or the Data-Center-to-One-Phone objective. The evidence label remains MODEL_ONLY.

## Falsifiable next gate

Implement an exact small-state density-matrix reference for the paper’s reduced ancilla state. Freeze parameterized probability families before search, calculate system QFI and reduced-ancilla QFI independently, and enumerate m <= n and m > n cases. Optimize admissible T_i under a declared ancilla dimension and unitary parameterization; search counterexamples; compare against a separately written reference; retain failed and non-identifiable cases. The expected discriminant is whether perfect equality can be achieved within the paper’s protocol assumptions, not whether QFI represents arbitrary useful output or storage capacity.

## Strategic and invariant impact

- INV-029: adds an information-retention boundary test only; no physical-compression result.
- INV-034: advances a reproducible, assumption-scoped foundational check.
- INV-035: treats the preprint theorem as a candidate claim to independently test, not a new physical law by declaration.
- INV-025/026/027 and all permanent material, fuel, fusion and finance goals remain unchanged and unpromoted.
