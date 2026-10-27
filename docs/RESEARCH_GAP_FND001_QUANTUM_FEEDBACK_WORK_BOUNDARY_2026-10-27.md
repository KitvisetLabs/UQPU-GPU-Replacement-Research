# Research gap RG-FND001-QUANTUM-FEEDBACK-WORK-BOUNDARY-001 — conditional work bounds and side-information accounting

**Opened:** 2026-10-27  
**Status:** OPEN / LITERATURE_ONLY / EQUATION_RECONSTRUCTION_NOT_RUN / IMPLEMENTATION_DEFERRED  
**Primary owner:** Lane A — executable thermodynamic reference contract  
**Evidence/accounting owner:** Lane F  
**Publication owner:** Lane H  
**Cross-lane consumers:** B, C, D, E, G; FND-001, FND-003, INV-034/035  
**Literature watch:** docs/literature_watch/2026-10-27-quantum-feedback-thermodynamic-limits.md

## Objective

Independently reconstruct and test the quantum-feedback work bounds of Ji, Gour and Wilde before translating them into an executable UQPU resource contract. The specific question is whether the conditional single-shot/asymptotic expressions are implemented with the correct assumptions and signs, while information acquisition, processing and reset are accounted for exactly once at a common boundary.

## Source and evidence

- APS accepted-paper record: “Fundamental limits for thermodynamic control with quantum feedback,” accepted 2026-10-06, DOI [10.1103/x67n-33gr](https://doi.org/10.1103/x67n-33gr).
- Official preprint: [arXiv:2503.09012v4](https://arxiv.org/abs/2503.09012v4), version 4 posted 2026-10-09.
- Evidence class: accepted theoretical work / operational thermodynamic bounds.
- UQPU status: literature watch only; no proof reconstruction, implementation, physical experiment or cost advantage has been demonstrated.

## Known result boundary

The authors derive single-shot work-of-formation and extractable-work bounds for arbitrary quantum systems conditioned on arbitrary quantum side information, and an asymptotic generalized second law governed by conditional free energy. The source states that the traditional second law is recovered consistently when acquisition, processing and reset of side information are included.

Do not replace the paper's expressions with a guessed subtraction formula. First establish the exact theorem definitions, assumptions, units, sign convention and boundary from the primary source.

## Blocking unknowns

- Exact equations and operational assumptions have not yet been independently transcribed into a pinned UQPU fixture.
- No finite-dimensional reference cases or independently derived inequalities have been run.
- Classical/no-side-information limits, conditional-entropy sign conventions and single-shot versus asymptotic transitions are not yet tested.
- Controller preparation, information acquisition, processing, feedback, reset and any recoverable work may be coupled; naive addition/subtraction could double-count terms.
- No mapping exists from the theorem's work quantity to whole-device wall-plug energy or accepted-task economics.

## Unlock criteria

1. Pin arXiv version, DOI, equations, definitions, theorem assumptions and source hash in a reproducibility manifest.
2. Independently derive a small finite-dimensional reference case with known Hamiltonian and explicit system/controller state.
3. Compare the source bound against exact numerical quantities in the same operational convention; retain trivial bounds, solver failures and counterexamples.
4. Test the no-side-information and classical-side-information limits, sign conventions, units, and single-shot/asymptotic consistency.
5. Define one boundary and ledger acquisition, controller preparation, processing, control, feedback, reset, measurement, data movement and host costs without double counting.
6. Require independent review of the derivation and frozen test fixtures before adding any executable helper.

## Falsification and stop rules

Reject the implementation if a source-valid case violates the theorem bound beyond numerical tolerance, if the declared limits do not recover their required reference cases, if the proof assumptions are silently weakened, or if the result depends on omitted/double-counted side-information costs. Do not use this gap to claim free energy, device efficiency, a new physical law, or lower cost per useful task.

## Current decision

No production code was added this cycle: the high-value next Lane A action is equation reconstruction and reference-case preregistration. Adding a guessed net-work formula before confirming the theorem's operational convention would create a risk of double counting and false confidence. The next cycle should implement only after those equations and limiting cases are pinned.
