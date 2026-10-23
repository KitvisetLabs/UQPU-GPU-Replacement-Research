# EQN-PROGRESSIVE-001 — progressive versus one-step symbolic-law discovery

**Status:** PROPOSED / LITERATURE_MOTIVATED / NOT_EXECUTED  
**Date:** 2026-10-24  
**Primary owner:** Lane A — quantum programming/runtime and mathematical candidate evaluation  
**Integration owner:** Lane F — evidence, reproducibility and economics  
**Strategic/literature owner:** Lane H  
**Source main SHA:** c7b5958af58fad04a101ef5c6abf6a29293c867e  
**Evidence class:** PEER-REVIEWED ACCEPTED PAPER + PROJECT PREREGISTRATION  
**Project evidence promotion:** none

## Question

Under matched observations and search budgets, does a progressive chain of interpretable intermediate relations improve recovery of a known composite law or held-out predictions over the strongest one-step symbolic-regression baseline?

## Source

Xia and Zhang, “Data-driven progressive discovery of physical laws,” *Physical Review Research*, accepted 2026-10-06, DOI 10.1103/f2kp-pp4q. Official APS record: https://journals.aps.org/prresearch/accepted/10.1103/f2kp-pp4q.

The source motivates the method family; it does not supply project evidence.

## Competing hypotheses

- H1: progressive decomposition improves structural recovery or held-out prediction when intermediate structure is identifiable and observations support it.
- H0: a one-step model matches or beats the chain after controlling observations, candidate grammar, search budget and model complexity.
- H2: apparent gains arise from extra intermediate data, extra compute, split leakage, or post-hoc model selection.
- H3: multiple structurally different models remain observationally equivalent; no unique mechanism is identified.

## Frozen comparison requirements

1. Define the one-step and progressive candidate grammars before evaluating test data.
2. Generate deterministic synthetic composite-law families with known equations, units, coefficients and intermediate variables; record source code and data hashes before execution.
3. Use identical raw observations for the main comparison. If a chain uses intermediate measurements, expose the same observations to the one-step baseline through a declared joint objective.
4. Split by entire law family and parameter regime. Do not rely only on random row-level train/test splitting.
5. Include noisy observations, correlated distractors, dimensionally invalid expressions, a deliberately misspecified chain and an observational-equivalence control.
6. Match wall-clock, host CPU time, candidate evaluations, coefficient-fit calls and any LLM token budget. Record peak memory and energy only when actually measured.
7. Retain every failed/invalid candidate and every seed; report false-discovery and selection rates.

## Metrics and acceptance

Report held-out residual and uncertainty, exact structure recovery only where identifiable, expression complexity, dimensional validity, declared symmetry/conservation checks, counterexample survival, parameter identifiability, false-discovery rate, runtime, memory, candidate count and complete search-resource accounting.

Accept a method-level improvement only if a preregistered held-out metric or identifiable structural-recovery metric improves over the strongest baseline under matched budgets, without worsening constraint violations. A tie or ambiguous structural result is a valid null outcome. Failure is retained, not hidden.

## Stop and promotion rules

- Stop before any claimed result if dataset/split hashes, baseline versions or search budgets were not frozen.
- Stop if train/validation/test data leak across a law family or if candidate selection uses the held-out outcomes.
- Do not promote an expression to a physical law because it fits or extrapolates on a synthetic fixture.
- A passing offline benchmark remains MODEL_ONLY and does not demonstrate QPU advantage, material substitution, commercial bio-oil, net fusion electricity, lower WACC or Data-Center-to-One-Phone compression.
- Any proposed challenge to established physics must separately satisfy the full INV-035 hypothesis contract and an experiment/proof plus independent-validation path.

## Dependencies and next gate

Depends on 06_AI_ASSISTED_PHYSICS_EQUATION_DISCOVERY.md, software/uqpu-prototype/uqpu/equation_discovery.py, FND-006 and EQN-001–006. Next gate: implement the deterministic fixtures and exact split-hash manifest, then run a focused test suite and exact-head CI. No provider access is required or authorized.