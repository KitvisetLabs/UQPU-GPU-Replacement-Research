# Literature watch — ProofEvolve and reusable verified proof-DAG schemas

**Date reviewed:** 2026-10-29  
**Source date:** 2026-08-26 (arXiv submission)  
**Evidence class:** OFFICIAL PREPRINT / THIRD-PARTY METHOD CLAIM / NOT REPRODUCED BY UQPU  
**Primary owner:** Lane H — literature provenance and publication  
**Interfaces:** Lane A formal-validation tooling; Lane F evidence/resource accounting; INV-034/035 and FND-006

## Source and genuine methodological delta

Wenqian Ye and colleagues, “ProofEvolve: Neuro-Symbolic Evolution for Formal Automated Theorem Proving,” arXiv:2608.26334, submitted 2026-08-26: https://arxiv.org/abs/2608.26334

The authors describe a neuro-symbolic loop that evolves explicit proof directed acyclic graphs (DAGs), asks a neural model to propose decompositions/repairs/schema recombinations, uses a Lean kernel to check proof transitions, and extracts verified sub-DAG schemas for reuse across problems. Residual premises are exposed as new subgoals rather than silently treated as solved. The abstract reports the highest average solve rate among evaluated systems on three Lean benchmarks. That score is an external author-reported result, not a UQPU measurement.

The project-specific novelty is not “AI proves physics.” It is a concrete evidence-structure worth testing: retain reusable proof fragments and failed/partial obligations as versioned graph nodes, while binding each checked node to its exact statement, proof-evidence record, checker log and immutable source revision.

## Limitations and evidence boundaries

- This is an arXiv preprint, and UQPU has not independently reproduced the reported benchmarks.
- The abstract alone does not establish theorem novelty, semantic correctness of generated transformations, equal resource budgets, or transfer to a new theorem family.
- A kernel can validate a proof of the encoded statement under its declared axioms; it cannot by itself prove that the statement captures the intended physical semantics or that the premises describe nature.
- A proof DAG, a symbolic-regression fit, or a formally verified mathematical theorem is not a new physical law, engineering result, QPU advantage or economic result.
- Code/checkpoint availability, exact environment, licensing, benchmark splits and per-attempt compute/cost require independent pinning and review before reproduction.

## Exact UQPU relevance

- **FND-006 / EQN-001–006:** reuse verified lemmas and expose unresolved assumptions without conflating proof status, equation fit, physical interpretation and technology.
- **INV-035:** use AI for candidate generation and proof-search guidance; require exact statement binding, constraints, counterexample search, held-out prediction and independent validation before any physics-facing claim.
- **Lane A:** graph-level metadata gate added in proof_dag_reuse.py; it complements, rather than replaces, formal_proof_evidence.py.
- **Lane F / INV-033:** time-to-evidence and compute cost should eventually be measured per independently accepted result, including failed attempts and timeouts. No cost saving is claimed here.
- **Lanes B–E and G / INV-029–032:** no provider, memory hardware, material, bio-oil, fusion-electricity, device or factory consequence is established by this preprint.

## Falsifiable follow-up

1. Pin source revision, license, theorem corpus, Lean/kernel version, dependencies, proof artifacts and run logs.
2. Preregister theorem-family-disjoint train/validation/test splits; do not tune on test families.
3. Compare baseline proof search against schema reuse under equal compute/time budgets and identical theorem statements.
4. Record kernel-checked success, invalid/changed statements, residual premises, cycles/invalid dependencies, failed proofs, timeouts, peak memory, wall time and energy where measurable.
5. Independently re-run a held-out subset and bind each result to exact statement/proof/log hashes.
6. For a physics equation, separately check dimensions, symmetries, conservation, causality and limits; require a discriminating observable, held-out prediction, experiment or physical proof, independent replication and downstream economics.

**Disposition:** useful method lead for FND-006; reproduction remains OPEN. No new physical law, real-QPU result, material/fuel/electricity advantage, reduced WACC or Data-Center-to-One-Phone milestone is claimed.
