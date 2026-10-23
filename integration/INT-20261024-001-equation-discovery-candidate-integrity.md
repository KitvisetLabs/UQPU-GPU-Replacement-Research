# INT-20261024-001 — equation-discovery candidate integrity

**Status:** TESTING on branch; merge/CI pending  
**Owner:** Lane A for code contract; Lane H for literature watch  
**Source main SHA:** `c7b5958af58fad04a101ef5c6abf6a29293c867e`  
**Source branch:** `research/2026-10-24-equation-discovery-audit`  
**Evidence class:** SOFTWARE_CONTRACT / LITERATURE_ONLY; no physical/economic promotion

## Hypothesis and mechanism

Rejecting non-finite held-out errors and non-integer validation counts prevents malformed score telemetry from satisfying the candidate-comparison gate. This is a software integrity improvement, not evidence that any candidate equation is physically correct.

## Interface and acceptance

- Interface: `EquationHypothesis.validate()`, `has_heldout_improvement`, `ready_for_physical_candidate_claim`.
- Baseline: finite/nonnegative metric requirement was not enforced; positive infinity could make a finite candidate look better.
- Combined system: validation rejects NaN/±infinity and invalid validation counts before promotion checks.
- Falsifier: a unit test demonstrates that any non-finite metric or non-integer/boolean validation count is still accepted.
- Required CI: `python -m unittest discover -s tests -v` across configured Python versions, plus repository invariant workflow.
- Rollback: revert only the small validation/test diff if type compatibility fails; preserve the literature record and negative evidence.

## Cross-lane edges

- A ↔ H: use transformer equation generation only as candidate production; deterministic evaluators retain acceptance authority.
- A ↔ F: any future speed/cost claim must count generator, evaluator, data access, retries and accepted outputs on the same budget boundary.
- FND-006 / EQN-004: candidate must survive held-out generalization and counterexample search.
- FND-005 / EQN-005: formal proofs are model-scoped and require premise-to-physical-assumption mapping.
- INV-029/030/031/032/033: no mission-level compression, material, fuel, fusion, interest or WACC result is claimed.

## Current result

Implementation and regression tests are staged on the research branch. CI and merge state must be updated from GitHub after the PR runs; this record must not be read as merged or validated until then.
