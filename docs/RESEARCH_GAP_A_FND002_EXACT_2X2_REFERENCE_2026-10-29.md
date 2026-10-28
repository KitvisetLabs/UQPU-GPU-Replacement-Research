# Research gap RG-A-FND002-EXACT2X2-REF-001 — analytic Hamiltonian reference to sparse-algorithm comparison

**Opened:** 2026-10-29  
**Status:** PARTIALLY_UNLOCKED / MODEL_ONLY REFERENCE FIXTURE  
**Owner:** Lane A  
**Related:** INV-025–027, INV-029, INV-034/035, FND-002/FND-004, EQN-001–EQN-006, RG-A-ROOT-SPARSITY-REPRO-001

## Objective

Create the first deterministic exact reference fixture for the smallest nontrivial Hermitian Hamiltonian family, so later sparse-query algorithms have an independently specified expected evolution and explicit row/column norm contract.

## Current implementation

`software/uqpu-prototype/uqpu/small_hamiltonian_reference.py` implements the analytic 2x2 form for
\[
H=\begin{pmatrix}a&b\\b^*&d\end{pmatrix},\quad
\mu=(a+d)/2,\quad
\delta=\sqrt{((a-d)/2)^2+|b|^2}.
\]
It evaluates \(e^{-iHt}=e^{-i\mu t}[\cos(\delta t)I-i\sin(\delta t)K/\delta]\), with the continuous \(\delta=0\) limit, and reports a unitary residual. Regression tests cover Pauli-X, diagonal degeneracy, zero time, semigroup composition, row/column norms, sparsity and invalid inputs.

## Acceptance contract

- Exact formula and assumptions remain visible; input Hamiltonians are Hermitian by construction, not inferred from arbitrary matrix data.
- Run the unitary and semigroup checks under Python 3.10–3.12 CI.
- Extend to a frozen sparse-entry oracle and a candidate product-formula / qDRIFT / composite-qDRIFT implementation.
- Compare on identical time/error contracts with held-out matrices and report query calls separately from oracle construction, state preparation, synthesis, host compute, memory/I/O, reconstruction, retries and verification.
- Preserve all failed profiles and counterexamples; independent reproduction is required before promotion beyond MODEL_ONLY/SIMULATION.

## Stop conditions

The path stops or narrows if the candidate access model cannot be implemented, if exact-reference residuals fail, if held-out error misses the acceptance threshold, or if full resource accounting removes the proposed advantage.

## Non-claims

This is a 2x2 analytic software reference only. It is not a finite-size theorem proof, quantum algorithm, real-QPU result, measured runtime/energy/cost, new physical law, memory-storage replacement, material/fuel/fusion result, lower-WACC result or Data-Center-to-One-Phone milestone.
