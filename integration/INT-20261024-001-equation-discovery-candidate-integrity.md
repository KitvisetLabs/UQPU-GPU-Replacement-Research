# INT-20261024-001 — equation-discovery candidate integrity

**Status:** FOLLOW-UP HARDENING on PR branch; previous exact-head CI passed; new exact-head CI pending  
**Owner:** Lane A for code contract; Lane H for literature watch  
**Source main SHA:** `c7b5958af58fad04a101ef5c6abf6a29293c867e`  
**Source branch:** `research/2026-10-24-equation-discovery-audit-v2`  
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

## Append-only synchronization debt

The inspected `WORKLOG.md` currently ends at the 2026-10-19 Cycle 008 Delta 21 entry, while later Delta 22/23 and the 2026-10-23 literature watch exist as separate artifacts. Because `WORKLOG.md` is a large append-only canonical file and this run did not obtain a safe full-history editing workflow, it was not replaced or partially rewritten. **Sync debt:** append a dated summary to `WORKLOG.md` only after the reviewed research change is merged; until then this record itself is branch-only and `main` remains the canonical state at `c7b5958af58fad04a101ef5c6abf6a29293c867e`.

## Foundational and equation-discovery status at this cycle

| ID | Status after current literature/code review | Next falsifiable gate |
|---|---|---|
| FND-001 thermodynamic-gap accounting | Existing Landauer/Margolus–Levitin helpers remain ideal lower-bound tools; no new matched physical energy measurement or bound revision. | Pair observed operation duration with energy for the same physical evolution; retain all host/control/thermal terms separately. |
| FND-002 output-information lower bounds | No new general classical-output lower bound was identified. Ancilla QFI is parameter-information-specific, not readable-byte capacity. | Define output entropy/precision/accepted output and compare with input/output and reconstruction costs. |
| FND-003 matched control vs quantum-speed-limit measurement | No matched physical control/QSL experiment was found in this run. | Freeze the same state transition, energy boundary, duration and success criterion for control and candidate. |
| FND-004 alternative physical primitives | No credible anomaly or independently validated primitive changed the incumbent engineering constraints. | Require a specific incumbent assumption, replacement model, distinct observable and smallest decisive experiment. |
| FND-005 QFT/elementary-particle mechanism scans | The October symmetric-mass-generation PRL work is model-specific field-theory/lattice progress; no new particle or device primitive is established. | Reproduce model assumptions, critical scaling and independent numerical observables before tracing to a device. |
| FND-006 mathematics-first invention | Transformer formula synthesis and AI-mathematical-instrument survey provide generator/proof-workflow candidates; candidate metrics are now guarded against non-finite values. | Run frozen known-law, extrapolation and non-identifiability tests with matched compute/energy budgets. |
| EQN-001 literature surveillance | This dated literature watch records source dates, evidence classes, limitations and follow-ups. | Repeat public-source scan next cycle; do not treat source claims as project evidence. |
| EQN-002 symbolic-regression benchmark | Matched-budget comparison is specified but not yet executed. | Freeze data splits/hashes and compare transformer, symbolic-search and negative-control generators. |
| EQN-003 constraint-aware generator | Transformer is a candidate generator only; physical constraints and deterministic evaluators remain authoritative. | Measure dimensional/symmetry/conservation checks and candidate survival after constraint enforcement. |
| EQN-004 counterexample/falsification engine | Non-identifiability and held-out counterexamples are specified; no new engine implementation is claimed. | Demonstrate that deliberately equivalent-on-training but divergent-on-held-out equations are rejected. |
| EQN-005 new-physics escalation gate | Formal proof status must be separated from empirical premise validity; no alternative law promoted. | Record formal-system/kernel status, assumptions, distinct observable, experimental falsifier and independent replication. |
| EQN-006 equation-to-technology traceability | Integration record maps generator results to Lane A/F and mission gates without asserting a technology consequence. | Require an accepted useful-output, device/system, lifecycle-resource and economics chain before promotion. |

**BIO-001 / FUS-001 / FIN-001:** inspected as permanent cross-cutting tracks; no new Pangola-to-saleable-liquid mass/energy/cost evidence, net-delivered fusion-electricity evidence, or financed-principal/interest/time-to-evidence measurement was added. Their evidence classes remain unchanged.


## Post-CI adversarial review — 2026-10-24

The prior branch head `6ebc1591bd5b859251a8cca91d2a1c9c8df188fb` passed run 960, but code review found that float coercion could admit numeric strings while the property compared unnormalized values. The follow-up requires `numbers.Real` (excluding booleans), rejects strings/objects and returns false for malformed values in `has_heldout_improvement`. Regression tests cover both fields. This is a software input-integrity result; exact-head CI for the follow-up is pending and no scientific evidence class is promoted.
