# Research gap RG-A-FND002-TROTTER-REFERENCE-001 — exact evolution versus product-formula approximation

**Opened:** 2026-10-29  
**Primary owner:** Lane A — workload algorithms and reference contracts  
**Interfaces:** B provider-neutral lowering; C state/data movement; D/G native-gate and device mapping; F evidence/resource accounting; H literature provenance  
**Status:** MODEL_ONLY / UNIT-TESTED REFERENCE COMPARATOR; SPARSE-ORACLE AND qDRIFT REPRODUCTION OPEN  
**Related:** INV-025–027, INV-029, INV-034/035, FND-002/FND-004, EQN-001–EQN-006, RG-A-FND002-EXACT2X2-REF-001, RG-A-ROOT-SPARSITY-REPRO-001

## Objective

Create a deterministic first-order product-formula baseline that is checked against the exact analytic 2x2 Hermitian reference before the project spends effort on sparse-oracle algorithms or provider-specific execution.

## Frozen mathematical contract

Use (H=\alpha Z+\beta X=\begin{pmatrix}\alpha&\beta\\\beta&-\alpha\end{pmatrix}) with finite real `alpha`, `beta`, and evolution time `t`. The exact reference is `evolve_2x2_hermitian(alpha, -alpha, beta, t)`. For positive integer (r), the first-order approximation is
[
U_r=\left(e^{-i\alpha Zt/r}e^{-i\beta Xt/r}\right)^r.
]
Measure the Frobenius norm (\|U_r-U_{exact}\|_F) as a numerical comparator and independently check unitarity residual. This is a small-instance matrix error metric, not a complete workload acceptance predicate.

## Current implementation

`software/uqpu-prototype/uqpu/product_formula_reference.py` supplies the dependency-free product-formula simulator and matrix-distance validator. Tests cover a decreasing error sequence over fixed step counts, commuting single-term limits, unitarity and fail-closed inputs.

## Acceptance contract and next unlock

- Preserve the exact-reference formula and frozen inputs in the lane contract.
- Expand from this two-term 2x2 fixture to independently specified sparse 2x2/4x4 matrix-entry records with a pinned access/oracle contract.
- Compare exact evolution, product formula, qDRIFT and composite-qDRIFT on identical held-out matrices and trace-distance tolerances.
- Record query counts separately from oracle construction, state preparation, synthesis, compilation, host compute, peak memory, transfers, reconstruction, retries, verification and cost per accepted useful task.
- Keep any unknown energy as UNKNOWN, not zero; no cross-provider probability/price mixing.
- Require independent theorem-assumption review and a held-out reproduction before promoting evidence beyond MODEL_ONLY/SIMULATION.

## Falsifiers and stop conditions

The reference path fails if the approximation error does not improve for the frozen test family, the commuting limits disagree with the exact solution, unitarity residual exceeds the declared tolerance, or invalid inputs are not rejected. A successful toy test does not establish sparse-query theorem applicability, QPU advantage, a new physical law or economic benefit.

## Non-claims

No real-QPU execution, quantum advantage, physical speedup, new physical law, GPU/CPU/NPU/RAM/VRAM/storage replacement, Pangola-carbon substitution, accepted bio-oil, net fusion electricity, lower WACC or Data-Center-to-One-Phone milestone is established.
