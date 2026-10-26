# Literature watch — formal proof reconstruction and counterexample generation

**Date searched:** 2026-10-27  
**Primary lane:** A — quantum programming / equation-discovery tooling  
**Evidence owner:** F — reproducibility and evidence  
**Publication owner:** H — strategic research publication  
**Cross-cutting:** INV-034, INV-035, FND-006, EQN-001–006, RG-047  
**Evidence class:** external conference-paper/preprint claims + project follow-up proposal; no UQPU reproduction or physical-law claim

## Why this watch exists

The current equation-discovery program needs positive proof evidence and strong negative-search evidence. Proof text, a formal statement, a kernel-checked artifact, independent reproduction, numerical counterexamples and physically discriminating experiments are different states and must not collapse into a single “verified” flag.

## Primary sources and bounded novelty

1. **Taprogge, Blanqui and Steen, “Formal Verification of Proofs from Automated Theorem Provers for Higher-Order Logic,” arXiv:2609.24594 (2026-09-21).**  
   Source: https://arxiv.org/abs/2609.24594  
   The authors describe proof-step reconstruction in Dedukti/Leo-III for higher-order logic, reporting automatic reconstruction of about 80% of generated proof steps and noting that implementation exposed bugs in Leo-III. The project-relevant novelty is the operational distinction between an automated prover's internal derivation and a separately reconstructable/checkable artifact. The reported percentage is scoped to the authors' system and task; it is not a universal proof-verification rate and has not been reproduced by UQPU.

2. **Li et al., “Learning to Disprove: Formal Counterexample Generation with Large Language Models,” arXiv:2603.19514v2 (revised 2026-10-14).**  
   Source: https://arxiv.org/abs/2603.19514  
   The authors describe symbolic mutation of theorem hypotheses and Lean-verified counterexample-generation tasks, reporting gains on three collected benchmarks. This motivates treating failed hypotheses and verified counterexamples as first-class outputs rather than rewarding proof search alone. It remains a preprint claim; UQPU has not reproduced its benchmarks, and a formally valid counterexample to a formal statement does not by itself establish that the statement accurately models nature.

3. **Already-covered context:** Xia and Zhang, *Physical Review Research* accepted paper “Data-driven progressive discovery of physical laws,” accepted 2026-10-06, DOI https://doi.org/10.1103/f2kp-pp4q. Its progressive symbolic-search approach is already recorded in the 2026-10-26 main-branch watch, so this cycle does not duplicate that article.

## Concrete UQPU relevance

- **RG-047 / EQN-001–006:** bind exact theorem statement, source revision, proof bytes, checker/toolchain, environment and run log; distinguish proof text, formal statement, kernel-checked, independently reproduced, failed and inconclusive outcomes.
- **FND-006 / INV-034–035:** preserve mathematics-first candidate generation while requiring explicit assumptions, counterexample search and independent checking.
- **Lane A:** the typed `FormalProofEvidence` to `EquationHypothesis` implementation is already proposed in open PR #132. This cycle deliberately does not create a duplicate implementation or duplicate Batch 071.
- **Lanes B–D and G:** no provider, device, chip or manufacturing claim follows from proof metadata.
- **Lane E / INV-030–032:** these methods may later help audit constitutive/material or transport models, but no Pangola-carbon substitution, accepted bio-oil or net fusion electricity follows without domain-specific data and experiments.
- **Lane F / INV-033:** theorem checking does not establish cost or financing advantage; capital, duration, risk and cost inputs still need measurement.
- **INV-029:** proof tooling can improve research reliability but does not demonstrate phone-class physical compression or a service/energy/lifecycle-cost contract.

## Proposed falsifiable follow-up

1. Pin an actual Lean/Dedukti checker and toolchain at an immutable revision; record imports, axioms, exact statement/proof/environment/log digests and the executed command.
2. Run a known theorem fixture, a deliberately mutated invalid proof, a timeout/inconclusive fixture and a separately rebuilt run. Require the invalid proof to fail and retain its log.
3. For a declared false equation hypothesis, generate a boundary or held-out counterexample, bind its source/data and reproduce it independently; if a formal counterexample is claimed, check the certificate separately.
4. Keep mathematical correctness separate from semantic adequacy, dimensional/symmetry/conservation/causality checks, held-out physical prediction, discriminating experiment and economics.
5. Do not report a discovery-method winner until RG-046 raw-data provenance and RG-EQN-008 matched, law-family-disjoint, resource-matched comparison gates close.

## Non-claims

No new physical law, theorem priority, quantum advantage, real-QPU result, material substitution, saleable fuel, fusion electricity, lower WACC or Data-Center-to-Phone achievement is claimed. This article records external-method surveillance and a falsifiable project follow-up only.
