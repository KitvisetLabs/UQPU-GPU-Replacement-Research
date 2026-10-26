# Literature watch — formal proof reconstruction and counterexample generation

**Date searched:** 2026-10-27  
**Primary lane:** A — quantum programming / equation-discovery tooling  
**Evidence owner:** F — reproducibility and evidence  
**Publication owner:** H — strategic research publication  
**Cross-cutting:** INV-034, INV-035, FND-006, EQN-001–006, RG-047  
**Evidence class:** external conference-paper/preprint claims + project implementation proposal; no UQPU result or physical-law claim

## Why this watch exists

The current equation-discovery program needs both positive proof evidence and strong negative-search evidence. Formal theorem text, a proof assistant's checked result, independent reproduction, numerical counterexamples, and physically discriminating experiments are different states and must not collapse into a single “verified” flag.

## Primary sources and bounded novelty

1. **Taprogge, Blanqui and Steen, “Formal Verification of Proofs from Automated Theorem Provers for Higher-Order Logic,” arXiv:2609.24594 (2026-09-21).**  
   Source: https://arxiv.org/abs/2609.24594  
   The paper describes proof-step reconstruction in Dedukti/Leo-III for higher-order logic, reporting automatic reconstruction of about 80% of generated proof steps and noting that the implementation uncovered bugs in Leo-III. The project-relevant novelty is the operational distinction between a solver's internal derivation and a separately reconstructable/checkable artifact. The reported percentage is scoped to the paper's system and task; it is not a universal proof-verification rate and has not been reproduced by UQPU.

2. **Li et al., “Learning to Disprove: Formal Counterexample Generation with Large Language Models,” arXiv:2603.19514v2 (revised 2026-10-14).**  
   Source: https://arxiv.org/abs/2603.19514  
   The authors describe symbolic mutation of theorem hypotheses and Lean-verified counterexample-generation tasks, reporting gains on three collected benchmarks. This motivates treating failed hypotheses and verified counterexamples as first-class outputs rather than rewarding proof search alone. The result remains a preprint claim; UQPU has not reproduced its benchmarks, and a formally valid counterexample to a formal statement does not by itself establish that the statement accurately models nature.

3. **Context already represented on main:** Xia and Zhang, *Physical Review Research* accepted paper “Data-driven progressive discovery of physical laws,” accepted 2026-10-06, DOI https://doi.org/10.1103/f2kp-pp4q. This is not a new project discovery in this cycle; its progressive symbolic-search approach is already recorded in the 2026-10-26 watch.

## Concrete UQPU relevance

- **RG-047 / EQN-001–006:** bind the exact theorem statement, source revision, proof bytes, checker/toolchain, environment and run log; distinguish proof text, formal statement, kernel-checked, independently reproduced, failed and inconclusive outcomes.
- **FND-006 / INV-034–035:** preserve mathematics-first candidate generation while requiring counterexample search, explicit assumptions and independent checking.
- **Lane A:** typed proof metadata is now connected to `EquationHypothesis`; a status of `CHECKED` or `FAILED` requires the typed artifact-bound record in the new branch.
- **Lanes B–D and G:** no provider, device, chip or manufacturing claim follows from formal proof metadata.
- **Lane E / INV-030–032:** these methods may later support constitutive/material or transport model auditing, but no Pangola-carbon substitution, accepted bio-oil, or net fusion electricity result follows without domain-specific data and experiments.
- **Lane F / INV-033:** no financing or cost advantage is established by theorem checking; capital, duration, risk and cost inputs still need measurement.
- **INV-029:** proof tooling can improve research reliability, but does not demonstrate phone-class physical compression or a service/energy/lifecycle-cost contract.

## Proposed falsifiable follow-up

1. Pin an actual Lean/Dedukti checker and toolchain at an immutable revision; record imports, axioms, exact statement/proof/environment/log digests and the executed command.
2. Run a known theorem fixture, a deliberately mutated invalid proof, a timeout/inconclusive fixture and a separate independently rebuilt run. Require the invalid proof to fail and retain its log.
3. For a declared false equation hypothesis, generate a boundary or held-out counterexample, bind its source/data and reproduce it independently; if a formal counterexample is claimed, separately check the counterexample certificate.
4. Keep mathematical correctness separate from semantic adequacy, dimensional/symmetry/conservation/causality checks, held-out physical prediction, discriminating experiment and economics.
5. Do not report a method winner until RG-046 raw-data provenance and RG-EQN-008 matched, law-family-disjoint, resource-matched comparison gates are closed.

## Non-claims

No new physical law, theorem priority, quantum advantage, real-QPU result, material substitution, saleable fuel, fusion electricity, lower WACC or Data-Center-to-Phone achievement is claimed. This article records an external-method surveillance delta and a falsifiable project follow-up only.
