# Literature watch — sparse quantum state preparation with sublinear T-count

**Date recorded:** 2026-10-27  
**Primary source:** Jingquan Luo and Lvzhou Li, *Sparse Quantum State Preparation with Sublinear T-Count*, arXiv:2608.00414, first posted 2026-08-01.  
**Source URL:** https://arxiv.org/abs/2608.00414  
**Evidence class:** OFFICIAL ARXIV PREPRINT / THEOREM CLAIMS REVIEWED AT ABSTRACT LEVEL; full-model audit pending.  
**UQPU status:** external mathematics only; no independent reproduction, measured resource saving or quantum advantage.

## Genuine result to track

The abstract reports a Clifford+T synthesis upper bound for an n-qubit target state supported on at most s computational-basis states:

- Upper-bound expression: O-tilde(min(s, n^(3/4) sqrt(s)) + sqrt(s log(1/epsilon)) + log(1/epsilon)).
- Lower-bound expression: Omega(min(s, sqrt(n s))) for 0 < epsilon <= 1/6 and 2 <= s <= 2^(n/2).

These are asymptotic theorem statements. The O-tilde factors, synthesis assumptions, amplitude representation and preprocessing model must be understood before translating them into gate counts or workload cost.

## Important model-alignment issue

The repository already tracks Li et al., *Optimal T Counts under Sparsity: from QROM to State Preparation and Block Encoding*, arXiv:2607.28260v2, whose abstract also reports a sparse-state-preparation corollary with square-root dependence on support size. The newer abstract's statement that previous upper bounds remained linear in s therefore cannot be interpreted as a direct improvement or contradiction without comparing the full theorem statements and input/access models.

Keep the two source records separate. Do not replace the existing sparse-QROM expression with the new expression, and do not claim one theorem is tighter until the same target-state definition, support promise, classical description/access mechanism, error metric, gate set, precision and preprocessing assumptions have been aligned.

## Exact UQPU relevance

- **Lane A:** coherent state preparation may be part of workload initialization; synthesis and classical preprocessing must be charged to the accepted-task ledger.
- **Lane C:** sparse state support is not equivalent to physical RAM, VRAM, HBM, SSD capacity or readable classical memory. QROM lookup, target-state synthesis and classical storage are separate resource contracts.
- **Lane B:** any target-aware circuit comparison must bind the same provider, device, calibration snapshot and circuit identity; this preprint alone authorizes no job.
- **Lane D/G:** T-count is not physical gate depth, routing, magic-state factory footprint, yield or packaging demand.
- **Lane F:** no numeric value should be derived from asymptotic notation as though it were a certified exact count; include preprocessing, ancillas, depth, memory/I/O, reconstruction, energy where measured and cost per accepted output.
- **Lanes E/H:** no new material, bio-oil, fusion-electricity, finance or strategic-market evidence follows from this circuit theorem.

## Falsifiable follow-up

1. Read both full papers and create a theorem-assumption matrix covering target-state class, amplitude/support representation, oracle or QROM access, classical preprocessing, Clifford+T model, approximation metric, epsilon range and hidden logarithmic factors.
2. Independently derive the smallest-n/s examples and compare exact synthesized circuits with each theorem's claimed regime. Preserve counterexamples and theorem-range failures.
3. Freeze disjoint held-out (n, s, epsilon) cases before evaluating. Compare actual synthesized T-count, depth, ancillas, classical preprocessing and input-description bytes; do not score the formula's asymptotic expression as measured data.
4. Only after mathematical model alignment, bind the state-preparation subroutine to a real UQPU workload and count all initialization, measurement, data movement and reconstruction overhead.
5. Independent reproduction and exact-head tests are required before promotion beyond MODEL_ONLY.

## Decision

The paper is a useful new-to-repository candidate for a model-alignment study. It is not evidence of a new physical law, physical-memory compression, lower energy, lower cost per accepted useful task or advantage over a classical baseline.
