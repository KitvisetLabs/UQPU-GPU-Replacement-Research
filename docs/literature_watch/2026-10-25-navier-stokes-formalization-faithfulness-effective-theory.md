# Literature watch — 2026-10-25: AI proof formalization faithfulness and effective-theory boundaries

**Accessed:** 2026-10-25  
**Primary owner:** Lane H — strategic research and publication  
**Integration owners:** A — formal workload/compiler correctness; F — evidence governance  
**Feeds:** FND-006; EQN-001–006; INV-034; INV-035; lanes A, D, E, F and H  
**Evidence class:** OFFICIAL CLAIM + CRITICAL PREPRINT + JOURNAL EDITORIAL  
**Project evidence promotion:** none

## Sources and dates

1. OpenAI, “On the Navier–Stokes Millennium Prize Problem,” 2026-09-08, announcing a natural-language proof and Lean formalization: https://openai.com/index/navier-stokes-solution/
2. Alexander Bastounis, Fabian Circelli and Anders C. Hansen, “Navier-Stokes lost in translation: Why Lean verification of AI autoformalisation does not guarantee correct natural language proofs,” arXiv:2610.08144, submitted 2026-10-06: https://arxiv.org/abs/2610.08144
3. Amin Doostmohammadi, “The Navier-Stokes equations blow up, and planes still fly,” Communications Physics 9, 325, published 2026-10-14: https://www.nature.com/articles/s42005-026-02930-y
4. The public Lean certificate repository accompanying the announcement: https://github.com/openai/NavierStokesAndEuler

## Genuine novelty

The critical preprint argues that the Lean formalization released alongside the announcement does not semantically correspond to the natural-language proof, including mismatches in statements and intermediate bounds. The authors explicitly do **not** claim that the natural-language proof is false. The point is narrower and methodologically important: a kernel-checked proof establishes the formal theorem that was compiled, not automatically the intended theorem in an accompanying paper.

The Communications Physics editorial adds a separate physics boundary: even if a continuum PDE admits a singular solution, that does not imply a real fluid reaches infinite speed outside the model's molecular-scale validity regime. The editorial discusses an effective-theory domain, not a new experiment or a refutation of the mathematical theorem.

## Limitations and contested status

- The critical autoformalization analysis is a preprint, not a final peer-reviewed adjudication of the Navier–Stokes claim.
- A statement mismatch is not, by itself, a proof that the natural-language argument is false; it means the formal artifact does not certify that argument as stated.
- The journal editorial is secondary interpretation, not a new primary proof or experimental measurement.
- This watch does not decide the underlying Navier–Stokes theorem, claim a new physical law, or treat a continuum singularity as an observed physical infinity.

## Exact UQPU relevance

- **FND-006 / EQN-001–006:** split mathematical-claim ingestion into at least three independent gates: formal theorem compilation, semantic faithfulness to the intended statement, and relevance to the physical model/domain.
- **Lane A:** a verified compiler or algorithm artifact must preserve workload semantics; passing a backend check is not enough if the source contract changed.
- **Lanes D/E/G:** constitutive and continuum models must declare their scale of validity and the physical model that replaces them outside that domain.
- **Lane F:** record formal status, proof status, experimental status and economic status as separate evidence predicates.
- **INV-031 / INV-032 / INV-033:** no direct evidence about bio-oil, fusion net electricity, financing principal, interest or WACC follows from this mathematics case study.

## Proposed falsifiable follow-up — EQN-AUTOFORMAL-002

1. Freeze the natural-language theorem, source revision, formal theorem statement, definitions, imported axioms and exact Lean toolchain.
2. Build a statement map covering quantifiers, hypotheses, initial/boundary data, forcing, function spaces, regularity, energy bounds and conclusion strength.
3. Independently compile the formal proof and attempt a statement-equivalence/faithfulness check. Record every omitted hypothesis or weakened conclusion as a mismatch; do not infer that the original theorem is false solely from a mismatch.
4. For any physical interpretation, record the incumbent equation's scale assumptions, the scale at which those assumptions fail, the replacement microscopic model and a discriminating observable. A mathematical singularity is not a measured physical divergence.
5. Preserve failed proof attempts and counterexamples. Require independent review before promoting a theorem claim, and experimental validation before promoting a physical-law claim.

**Pass condition:** the compiled formal theorem is demonstrably faithful to the frozen intended statement, with dependencies and assumptions audited.  
**Fail condition:** a statement, hypothesis, domain or conclusion changes without an explicit justified equivalence, or the build fails.  
**Promotion boundary:** passing this gate validates a mathematical artifact only; it does not establish a new physical law, technology advantage or economic benefit.
