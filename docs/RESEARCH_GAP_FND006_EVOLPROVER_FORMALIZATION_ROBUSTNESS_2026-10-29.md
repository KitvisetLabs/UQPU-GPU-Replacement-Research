# Research gap RG-FND006-EVOLPROVER-ROBUSTNESS-001 — symmetry and difficulty holdouts for formal discovery

**Opened:** 2026-10-29  
**Primary owner:** Lane H / FND-006, with Lane A formal-validation interface  
**Status:** LITERATURE-ONLY; REPRODUCTION NOT RUN  
**Source:** EvolProver, ICLR 2026 proceedings  
**Related:** INV-034/035, EQN-001/006, formal-proof evidence contract

## Objective

Test whether a proof-search pipeline remains reliable under semantics-preserving statement transformations and controlled difficulty shifts, rather than overfitting to one canonical formalization.

## Current evidence

The official ICLR 2026 proceedings page for EvolProver reports a training-data evolution approach using AST-level syntactic variants, semantic-domain translations and difficulty evolution. The source reports benchmark pass@32 results for a 7B non-reasoning prover. These are external benchmark claims, not a UQPU reproduction and not evidence of physical-law discovery.

## Blockers

- The source training/evaluation pipeline and exact model/data/configuration have not been reproduced here.
- A transformed theorem may accidentally change assumptions or meaning; AST change alone does not prove semantic equivalence.
- Kernel-checking establishes a proof relative to the encoded statement and axioms, not the physical truth of those premises.
- No pinned proof-assistant environment, theorem-family holdout or equal-budget UQPU baseline has been executed.

## Required unlock criteria

1. Pin source, theorem corpus, licenses, proof assistant/kernel version, dependencies and run configuration.
2. Separate AST-equivalent transformations from cross-domain translations; require checked equivalence certificates for the latter.
3. Hold out theorem families and difficulty bands before tuning.
4. Report kernel-checked proof rate, invalid/changed-statement rate, timeouts, failed proofs, counterexamples, resource use and reproducibility under equal budgets.
5. For physics equations, retain dimensional/symmetry/conservation/causality, limiting-case, held-out prediction, physical experiment and independent-replication gates separately.

## Falsifiers

The robustness hypothesis is weakened if transformed variants materially reduce kernel-checked proof rate, if the transformation changes semantics, if results do not reproduce under pinned configurations, or if apparent gains vanish under equal resource budgets.

## Non-claims

No new theorem about nature, physical equation, QPU advantage, material/fuel/electricity result, reduced WACC or Data-Center-to-One-Phone result is established.
