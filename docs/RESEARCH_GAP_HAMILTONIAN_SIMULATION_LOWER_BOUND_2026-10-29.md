# Research gap RG-A-FND002-HAMILTONIAN-SIM-LOWER-BOUND-001 — theorem-to-resource-contract reproduction

**Opened:** 2026-10-29  
**Primary owner:** Lane A — workloads/algorithms/resource contracts  
**Interfaces:** B (provider-neutral lowering), C (state/data movement), D/G (target implementation), F (evidence/economics), H (literature provenance)  
**Status:** OPEN / OFFICIAL-PREPRINT-THEOREM-CLAIM / UQPU-REPRODUCTION-NOT-STARTED  
**Source:** https://arxiv.org/abs/2607.19852  
**Literature watch:** [Hamiltonian-simulation lower bounds](literature_watch/2026-10-29-hamiltonian-simulation-lower-bound.md)  
**Related:** INV-025–027, INV-029, INV-034/035, FND-002/003/004, EQN-001–EQN-006

## Objective

Determine when the reported composite-qDRIFT gate/query trade-off can be used as a valid resource-bound certificate for a UQPU workload, without confusing an asymptotic theorem for a measured runtime, a physical speed limit, or a full-stack economic result.

## Source claim and applicability contract

For sorted positive normalized coefficients a₁ ≥ … ≥ aL > 0, Σⱼ aⱼ = 1, and tail weight λK = Σⱼ>K aⱼ, the preprint reports an asymptotic trade-off of the form

\[
\Omega\!\left(\min_{0\le K\le L}\left(Kt+\frac{t^2\lambda_K^2}{\epsilon}\right)\right).
\]

The bound applies to suitable hard-instance families under the paper's assumptions and error/access models. It is not universal for every Hamiltonian. The query model is classical and does not allow coherent superposition queries. Specialized algorithms exploiting additional structure or input-state properties may fall outside the direct scope.

## Acceptance contract

- Pin the paper version, source URL, local copy/hash, and any implementation or derivation.
- Independently review theorem statement and proof assumptions before treating the expression as a certificate.
- Implement the coefficient-tail/minimizing-cut calculation as an **asymptotic trade-off proxy**, not an exact finite-size lower-bound calculator.
- Freeze uniform, power-law and exponential coefficient profiles plus a held-out profile.
- Compare direct product-formula, qDRIFT and composite-qDRIFT implementations against exact small-instance evolution at a matched trace-distance target.
- Record term count, coefficient profile, time, error target, gates, depth, query model, oracle-construction cost, state preparation, compilation, host compute, memory/I/O, retries and output verification.
- Keep gate count, query count, physical pulse time, fault-tolerant runtime, energy and total cost as separate fields. Unknown energy is UNKNOWN, not zero.
- Require independent review of the theorem and reproduction of at least one held-out case.

## Falsifiers and unlock criteria

- Do not apply the bound if the tested Hamiltonian/access model violates the stated assumptions.
- Treat discrepancies as reproducibility/model-mapping issues until source revision, error metric, gate convention and oracle construction are reconciled.
- A finite-instance benchmark cannot prove an asymptotic theorem; it can test implementation and show whether a workload lies in the theorem's scope.
- Do not infer a new physical law, faster-than-limit device or mission-level cost advantage from a theorem fit or gate-count comparison.

## Next cheapest decisive experiment

Freeze a small bounded-degree Hamiltonian family, exact reference, three coefficient profiles and one held-out profile. Independently compute the minimizing cut K, then compare direct product formula, qDRIFT and composite qDRIFT under a common trace-distance tolerance and complete task-boundary accounting. Publish source/result hashes, including null and failed cases.

## Non-claims

No UQPU reproduction, real-QPU execution, new physical law, QPU advantage, 100x/100,000,000x cost advantage, GPU/CPU/NPU/RAM/VRAM/storage replacement, material substitution, accepted bio-oil, net fusion electricity, lower WACC or Data-Center-to-One-Phone result is established.
