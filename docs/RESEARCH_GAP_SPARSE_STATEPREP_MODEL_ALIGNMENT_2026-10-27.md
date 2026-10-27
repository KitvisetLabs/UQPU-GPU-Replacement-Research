# Research gap RG-STATEPREP-SPARSE-001 — sparse state-preparation theorem model alignment

**Opened:** 2026-10-27  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Cross-lane owners:** Lane C memory/state/data movement; Lane F evidence and integration; Lane H publication  
**Status:** OPEN / MODEL_ALIGNMENT_REQUIRED / MODEL_ONLY  
**Source:** Luo and Li, arXiv:2608.00414 (first posted 2026-08-01).  
**Related:** RG-QROM-SPARSE-001, INV-025/026/027, INV-029, INV-034/035.

## Question

Can the theorem in arXiv:2608.00414 be mapped to the same synthesis problem as the sparse-state-preparation corollary in arXiv:2607.28260v2, or do their target-state representation, classical description/access, preprocessing, approximation or circuit-model assumptions differ?

## Current evidence

The 2608.00414 abstract reports an O-tilde upper expression
O-tilde(min(s, n^(3/4) sqrt(s)) + sqrt(s log(1/epsilon)) + log(1/epsilon))
and a lower expression Omega(min(s, sqrt(n s))) for 0 < epsilon <= 1/6 and 2 <= s <= 2^(n/2). The 2607.28260v2 abstract separately reports a sparse-state-preparation corollary with square-root dependence on s in a sparse-QROM setting.

The abstracts alone do not settle whether the theorem models are comparable. The apparent tension is recorded as a question, not a contradiction or a claim that either paper improves the other. No project-derived exact count or independent theorem verification exists.

## Required acceptance gate

- Read and archive exact versions of both full papers and supplements where available.
- Extract theorem statements, definitions, input/access models, target-state families, support promises, precision metrics, gate sets, preprocessing and hidden-factor assumptions.
- Build a theorem-assumption matrix and independent derivation for small cases.
- Create a counterexample/edge-case suite at the theorem-range boundaries, including s=1, s=2, s near 2^(n/2), and epsilon=1/6.
- Freeze disjoint held-out (n,s,epsilon) cases and independently synthesize small circuits. Record exact T-count, depth, ancillas, classical preprocessing and description/storage bytes separately.
- Bind only a verified subroutine to an accepted useful-output workload; include all initialization, I/O, host work, measurement and reconstruction.
- Require independent review/reproduction before any evidence promotion.

## Explicit nonclaims

This gap is not a physical-memory lower bound, readable classical-storage equivalence, runtime/energy/cost result, quantum-advantage result or new physical law. No provider execution is authorized by this artifact. The sparse-QROM theorem and sparse-state-preparation theorem remain distinct until model alignment is demonstrated.
