# Literature watch — 2026-10-24: formal proof search and model-to-physics boundaries

**Accessed:** 2026-10-24  
**Primary owner:** Lane H — strategy, finance, future-industry research and publication  
**Feeds:** FND-006; EQN-004/EQN-005; Lane A mathematical contracts; Lane F evidence/cost accounting; INV-034/INV-035  
**Evidence class:** `LITERATURE_ONLY` — peer-reviewed mathematical-method evidence plus its public preprint  
**Project evidence promotion:** none

## Source and date

George Tsoukalas et al., “Advancing mathematics research with AI-driven formal proof search,” *Science* 394(6820), 234–239, published **2026-10-08**, DOI: https://doi.org/10.1126/science.aej2213. Public preprint: https://arxiv.org/abs/2605.22763 (submitted 2026-05-21).

The authors describe an agent that alternates language-model proof generation with Lean-based verification. The paper reports resolving 9 of 353 open Erdős problems and proving 44 of 492 OEIS conjectures; the authors also report that a basic generation/Lean-verification loop replicated the Erdős successes. These are claims about the studied mathematical tasks and formalization pipeline, not results produced by UQPU.

## Genuine methodological delta

The useful distinction for UQPU is between **candidate generation** and **proof checking**. A language model may propose a lemma, inequality, algebraic identity or bound; a proof assistant can check a proof relative to a declared formal system and its dependencies. This can make some mathematical subclaims reproducible instead of relying on natural-language plausibility.

This strengthens the formal-proof stage in FND-006 and EQN-004/005. It does not change the project's physical assumptions, current QSVT acceptance thresholds or any technology/economic conclusion.

## Limitations and proof-status boundary

- A kernel-checked theorem is true relative to the formal statement, imported library, axioms and definitions actually used. It does not establish that the theorem's premises describe a physical device or that input data are valid.
- Formalizing a claim can omit engineering assumptions or encode an unintended proposition; statement review and premise-to-model mapping remain necessary.
- The reported problem counts and costs are source-specific and must not be generalized to all theorem discovery or UQPU's total cost per accepted useful task.
- A proof of a mathematical lower bound does not by itself establish that a hardware implementation reaches the bound; a proof about an effective model does not establish that the model is nature's law.
- No UQPU lemma was formalized or checked during this literature watch. This artifact is not a reproduced proof, physical experiment, new physical law, QPU result or economic measurement.

## Falsifiable UQPU follow-up — FORMAL-PROOF-001

Select one small, bounded mathematical proposition already used by a repository-owned equation-discovery or QSVT contract. Before proof search, freeze the exact proposition, variables/units where applicable, hypotheses, target theorem, Lean version, imported dependencies and permitted axioms.

1. Implement the proposition in Lean and retain the exact source commit and dependency lock.
2. Require the declared Lean checker to accept the proof; enumerate axioms and nontrivial imported assumptions.
3. Have an independent reviewer map each formal premise to the corresponding repository model assumption and check that no physical premise was silently smuggled into a definition.
4. Add negative controls: mutate a premise or theorem statement so that the intended claim should no longer follow, and retain the failing proof/check or counterexample.
5. Independently replay the proof from a clean environment and report generation, checking, host, dependency and review time/cost separately.
6. Only then connect the checked lemma to a bounded simulation or measurement protocol. Any physical claim still needs a discriminating observable, held-out prediction, experiment and independent empirical validation.

**Falsifier:** the proof fails to check in the pinned environment, depends on undeclared axioms, the proposition does not match the intended model statement, independent replay fails, or the claimed physical consequence is not entailed by the verified mathematical result. A failed proof is retained as a negative result.

## Cross-lane implications

- **A — programming/runtime:** formalize bounded semantic, algebraic and resource-contract lemmas; preserve the distinction between theorem truth and execution success.
- **B — cloud/provider:** proof verification does not imply target capability or authorize a provider call/job.
- **C — memory/state/I/O:** theorem or Hilbert-space size is not readable classical storage; output-information and reconstruction contracts remain necessary.
- **D/G — devices and manufacturing:** a proved model property is not fabrication feasibility, yield or process-window evidence.
- **E — materials, biomass, bio-oil, fusion and cooling:** mathematical verification cannot replace Pangola-specific material qualification, accepted liquid-energy accounting or net delivered-electricity measurements.
- **F — economics/evidence:** count candidate generation, proof checking, dependency setup, failed attempts, independent review and accepted outputs under one declared budget boundary.
- **H — strategy/finance:** proof provenance improves auditability and can reduce some uncertainty, but no time-to-evidence, principal, interest or WACC benefit is measured.

## INV-034/035 conclusion

This source supports a stronger *method* for mathematics-first invention: use AI for broad hypothesis/proof search, then use an explicit formal checker and independent review for the mathematical claim. It does not remove the empirical gate. Present physics remains binding for engineering; a new physical law would still require a precisely changed incumbent assumption, a dimensionally and symmetrically consistent alternative, a distinct observable, held-out prediction, discriminating experiment and independent replication.

No change is made to the IBM `ibm_kingston` read-only snapshot preregistration. No provider was contacted and no QPU job was submitted.
