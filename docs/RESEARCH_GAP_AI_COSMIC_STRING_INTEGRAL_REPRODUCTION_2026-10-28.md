# Research gap — independent reproduction of AI-assisted cosmic-string integral discovery

**Gap ID:** RG-EQN-AI-COSMIC-STRING-INTEGRAL-001  
**Opened:** 2026-10-28  
**Primary owner:** Lane F — evidence and reproducibility  
**Cross-cutting:** Lane H (literature/publication), FND-005/006, EQN-001–006, Lane A evaluator robustness  
**Status:** OPEN / LITERATURE-ONLY / NOT_REPRODUCED  
**Source:** [Brenner, Cohen-Addad & Woodruff, arXiv:2603.04735](https://arxiv.org/abs/2603.04735)  
**Related watch:** [AI-assisted cosmic-string integral discovery](literature_watch/2026-10-28-ai-assisted-cosmic-string-integral-discovery.md)

## Question

Can an independent implementation reproduce the paper's reported closed-form/spectral evaluation of the cosmic-string radiation integral across a predeclared held-out domain, while retaining all numerical and symbolic failures as explicit negative evidence?

## Incumbent and candidate

- **Incumbent:** independent high-precision numerical evaluation of the published integral, plus an independently implemented reference method.
- **Candidate:** the paper's preferred Gegenbauer/spectral closed-form route and one alternate recurrence/spectral route.
- **Claim under test:** mathematical/numerical agreement over a declared domain only. This is not a test of a new physical law.

## Main failure modes to test

1. Endpoint/singular-limit handling as opening angle approaches 0 or pi.
2. Even/odd harmonic behavior and large-harmonic asymptotics.
3. Catastrophic cancellation, ill-conditioned basis transformations, precision dependence, and convergence failure.
4. Candidate evaluator returns exception, NaN/Inf, or a plausible value after an internal fallback.
5. Agreement on a discovery grid but failure on held-out combinations of harmonic and angle.
6. Reused assumptions/code between candidate and reference make apparent agreement non-independent.

## Required protocol

- Pin source version, equations, numerical libraries and precision.
- Predeclare train/held-out parameter sets, residual tolerances and stopping/resource limits.
- Implement two independent numerical routes; do not let candidate code generate its own oracle.
- Include even/odd small and large integer harmonics, random interior angles, endpoint-near stress cases and adversarial conditioning points.
- Record each candidate's expression, assumptions, residual, precision, runtime, memory, error/exception class and disposition (PASS/FAIL/UNDECIDED).
- Treat NaN/Inf, timeout and precision exhaustion as explicit failure/undecided states, never a low-cost or high-quality success.
- Require independent symbolic derivation or proof review of the key identities, then a separate reviewer reproduction.
- Preserve counterexamples and failed derivation branches.

## Acceptance gate

This gap closes only when another implementation reproduces the declared held-out tests and an independent mathematical review confirms the transformations and limiting cases. Numerical agreement alone does not prove a universal identity. No result may be promoted to a new physical law without a distinct observable, a discriminating physical test and independent empirical validation.

## UQPU and mission relevance

The workflow can inform EQN-006/FND-006 and the reliability of equation-discovery evaluators. Batch 090's signed-Max-Cut numeric-range guard is a direct software analogy: finite inputs do not guarantee finite intermediate or final outputs, so every evaluator needs fail-closed arithmetic and complete failure accounting. The protocol could later be adapted to BIO-001 accepted-liquid yield/cost models or FUS-001 net-electricity models, but those domains require their own measured inputs and validation; this paper supplies none.

**Nonclaims:** no UQPU reproduction, no new physical law, no QPU advantage, no readable-memory equivalence, no Pangola material qualification, no accepted bio-oil, no fusion electricity, no financing/WACC effect, and no Data-Center-to-One-Phone progress.
