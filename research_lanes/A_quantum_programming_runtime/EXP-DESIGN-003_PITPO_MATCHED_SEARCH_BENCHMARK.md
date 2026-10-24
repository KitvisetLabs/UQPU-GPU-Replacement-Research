# EXP-DESIGN-003: matched-budget adaptive equation-search audit

Date: 2026-10-24
Primary owner: Lane A - quantum programming, workloads, compiler/runtime
Related programs: EQN-002, EQN-003, EQN-004, FND-006, PITPO-AUDIT-001, INV-034, INV-035
Status: CONTRACT IMPLEMENTED; UNIT TESTS PASS IN SCRATCH; BENCHMARK NOT EXECUTED
Evidence class: SOFTWARE_CONTRACT

## Objective

Test whether an adaptive, feedback-updated equation generator produces more accepted useful candidate equations than static prompting or classical symbolic regression when all methods share the same declared resource caps, data splits, acceptance criteria and independent-replay rules.

This is a methods benchmark. It cannot promote a fitted equation to a physical law.

## Frozen pilot design

Methods:
- STATIC_LLM_SR
- ADAPTIVE_PITPO
- CLASSICAL_SYMBOLIC_REGRESSION
- SHUFFLED_FEEDBACK_CONTROL

Initial synthetic task families:
- a nonlinear oscillator with known ground-truth support;
- a dimensionally typed constitutive relation with known ground-truth support;
- a multivariable synthetic dynamical system with held-out parameter groups.

Use three fixed seeds for each of the three tasks. Freeze dataset, train, validation and held-out digests before any method runs. Split whole trajectories or parameter groups; do not randomly scatter rows from one trajectory across all splits. Keep an untouched OOD group for every task.

Initial declared caps per method/task/seed:
- wall-clock time: 900 seconds;
- evaluator calls: 3,000;
- generated tokens: 100,000;
- energy cap: null until an appropriate meter and boundary are available;
- direct-cost cap: null until model, training, evaluation, retry, storage and replay costs can be measured.

The caps are a proposed pilot configuration, not observed execution. Method-specific actual resource use is recorded separately. For non-LLM baselines, generated-token usage is zero; the cap is still declared identically.

## Acceptance and reporting

A run record must include benchmark/dataset/split digests, method ID, identical declared caps, actual wall time, evaluator calls, generated tokens, energy if measured, direct cost if measured, candidate count, accepted useful-model count, held-out error, constraint violations, false discoveries and independent replays.

An accepted useful model requires:
- finite, nonnegative held-out error;
- zero hard-constraint violations for the accepted model;
- at least one independent replay per accepted model;
- no use of held-out data for search, prompt selection, model tuning or threshold selection.

The new dependency-free search_comparison module rejects mismatched caps/splits, non-finite metrics, resource-cap overruns, invalid false-discovery counts, accepted models without held-out evidence or independent replay, and cost/energy claims with missing measurements. Its 13 scratch unit tests passed on 2026-10-24; exact-head repository CI is still required.

Report exact recovery where ground truth is known, held-out/OOD error, constraint violations, false-discovery rate, candidate and accepted-model counts, paired uncertainty intervals, total cost per accepted useful model, and energy per accepted model only when energy is measured for every compared run. A zero accepted-model count or unknown direct cost yields an undefined cost-per-accepted-model metric, not zero.

## Theorem and unit-rescaling guard

The PiT-PO paper's Support Exclusion Theorem requires its stated finite-dictionary, sparse-support, coefficient-bound, Gram-matrix and interference assumptions. The practical normalized coefficient threshold rho = 1e-2 is not a universal theorem guarantee.

Run an explicit unit/basis-rescaling counterexample. Transform variables and coefficients so the physical relation and predictions remain identical. If the threshold's redundancy decision changes, classify the threshold as representation-sensitive and reject theorem-certified promotion unless a valid invariant normalization and the full theorem inequality are demonstrated. Include a true small-coefficient term, correlated basis functions and a missing-basis case.

## Falsification and stop conditions

Reject a claimed method improvement if:
- held-out/OOD gain is absent or unstable across paired seeds;
- false discoveries rise materially;
- hard constraints fail;
- the result cannot be independently replayed;
- any declared cap is exceeded;
- equivalent unit/basis scaling changes a purported theorem guarantee;
- the direct-cost denominator is unknown or no useful model is accepted.

No provider, QPU, paid model API, purchase or instrument experiment is required for the initial synthetic pilot. Full training is not authorized or claimed by this contract. The benchmark remains NOT EXECUTED until a reproducible run record is committed.
