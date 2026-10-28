# Lane A contract — exact small-Hamiltonian reference fixture

**Date:** 2026-10-29  
**Owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Interfaces:** C (sparse encoding/state/I/O), D/G (target and manufacturing co-design), F (resource/economic acceptance), INV-034/035.

## Purpose

Provide an auditable, dependency-free analytic reference for the smallest nontrivial Hermitian Hamiltonian family,
\[
H=\begin{pmatrix}a&b\\b^*&d\end{pmatrix},\qquad U(t)=e^{-iHt}.
\]
The implementation uses the closed form obtained from \(H=\mu I+K\) and \(K^2=\delta^2I\). It reports the maximum row/column Euclidean norm and row sparsity, then returns the analytic 2x2 evolution and a unitarity residual.

## Acceptance and non-claims

- Check the Pauli-X analytic form, diagonal/degenerate limit, zero-time identity, unitarity and semigroup composition.
- Reject booleans, non-finite entries, malformed matrices and non-finite time.
- Label metadata MODEL_ONLY. Floating-point agreement is a code/reference check, not a theorem reproduction.
- This fixture is not a sparse-oracle implementation, does not validate the source theorem's access model, and does not compare a quantum algorithm with a competitive classical algorithm.
- Next gate: add a pinned sparse-entry access contract, then compare at least one candidate simulation algorithm against this exact reference over held-out matrices, times and error tolerances. Account for oracle construction, state preparation, synthesis, host work, memory/I/O, output reconstruction, retries, verification and accepted-task cost.

## Stable identifiers

- Gap: RG-A-FND002-EXACT2X2-REF-001
- Foundational interfaces: FND-002 and FND-004
- Equation-discovery interfaces: EQN-001–EQN-006
