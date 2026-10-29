# Lane A contract — exact versus first-order product-formula reference

**Stable ID:** RG-A-FND002-TROTTER-REFERENCE-001  
**Owner:** research_lanes/A_quantum_programming_runtime/  
**Date:** 2026-10-29  
**Evidence class:** MODEL_ONLY mathematical simulator

## Input contract

- `alpha`, `beta`, `time`: finite real numbers.
- `steps`: positive integer; booleans are invalid.
- Hamiltonian: (H=\alpha Z+\beta X=\begin{pmatrix}\alpha&\beta\\\beta&-\alpha\end{pmatrix}).
- Exact target: `evolve_2x2_hermitian(alpha, -alpha, beta, time)`.

## Output / acceptance

- Approximation: (U_r=(e^{-i\alpha Zt/r}e^{-i\beta Xt/r})^r).
- Error: Frobenius norm between approximation and exact unitary.
- Independent numerical check: maximum unitarity residual.
- Tests must verify decreasing error on the frozen noncommuting case, exact agreement for either single-term commuting limit, and fail-closed input handling.

## Boundaries and dependencies

This contract contains no sparse oracle, no provider SDK, no native-gate count, no QEC overhead, no energy measurement, no output reconstruction or accepted-task economics. It is not a theorem proof or quantum-advantage claim. The next dependency is a pinned sparse-entry access model and held-out 2x2/4x4 fixtures for product-formula/qDRIFT/composite-qDRIFT comparison.

## Next action

Record exact inputs, source hash, error tolerance, reference residual, all operations and I/O costs; preserve failed profiles and counterexamples. Simulator/dry-run first; paid QPU execution remains unauthorized.
