# Cycle 010 integration gap — EQN-PROOF-001 and FUS-MHD-BENCH-001

**Date:** 2026-10-24  
**Primary owner:** Lane F — evidence and integration  
**Related owners:** Lane H (literature), Lane E (fusion modeling), Lane A (formal methods/runtime)  
**Evidence class:** MODEL_ONLY / THIRD_PARTY_SOURCE  
**Status:** OPEN; no independent reproduction claimed

## EQN-PROOF-001 — proof-carrying equation-discovery checks

**Question.** Can a proof assistant check the finite-distribution score-grouping identities used in FND-QFI-001 while keeping mathematical assumptions separate from physical claims?

**Incumbent statement.** For a finite differentiable distribution with all p_i > 0, define q_i = p_i'/p_i. For each group of equal scores, P_k' = q_k P_k, and therefore (P_k')^2/P_k = q_k^2 P_k. Summing over groups preserves classical Fisher information exactly.

**Protocol.** Formalize the identity and normalization assumptions; prove the grouping lemma; compare independently with exact-rational fixtures; retain the zero-score class; treat support-changing boundaries separately. Formalize the implication from pairwise orthogonality to a dimension lower bound separately. Do not silently upgrade a necessary condition into a general sufficiency theorem.

**Falsifiers and acceptance.** A failed proof obligation, a counterexample under the declared assumptions, disagreement with exact rational fixtures, or hypotheses that do not match the source protocol blocks acceptance. Passing proves only the formalized mathematics.

## FUS-MHD-BENCH-001 — independent analytic-equilibrium verification

**Question.** Can the two published non-stellarator-symmetric ideal-MHD solution families be independently reproduced as exact-reference fixtures?

**Incumbent equations.** (curl B) cross B = grad p and div B = 0, under the source's stated ideal-MHD assumptions, geometry, parameter domains and flux-surface conditions.

**Protocol.** Freeze source version and parameters; independently transcribe the fields; verify divergence and force-balance residuals symbolically and numerically; test the symmetry-restoring zero-parameter limit; sweep admissible asymmetry parameters and domain boundaries; compare solver convergence with and without the relevant symmetry restriction.

**Falsifiers and acceptance.** Any nonzero symbolic residual, reproducible numerical residual beyond a preregistered tolerance, invalid flux-surface domain, failed limiting case or disagreement between independent implementations blocks acceptance. A pass is a solver-validation result only—not experimental plasma validation, stability proof, reactor feasibility, net electricity or commercial cost.

## Cross-cutting constraints

- No paid QPU or provider job is required or authorized.
- Do not infer a new physical law from proof-search success or exact solutions of incumbent equations.
- Keep FND-QFI-001 and QOS-AUDIT-010B25 separate; this gap does not close Priority-1 QOS.
- Preserve INV-029 through INV-035, INV-025/026/027, all A–H lanes, D/G co-design, multilingual strategic links, and BIO-001/FUS-001/FIN-001.
- Next action: fix the handoff evidence enum mismatch, run exact-final-commit CI, then preregister the offline proof and residual tests with all failures retained.
