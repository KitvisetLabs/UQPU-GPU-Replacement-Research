# Pending-main research sync — 2026-10-24 equation-metric finite gate

**Status:** `PENDING-MAIN / EXACT-HEAD-CI-PENDING`  
**Branch:** `research/2026-10-24-eqn-metric-finite-gate`  
**Canonical base SHA:** `c7b5958af58fad04a101ef5c6abf6a29293c867e`  
**Work item:** `RG-045` / `INT-20261024-013`  
**Evidence class:** software validation defect and proposed repair only; no scientific evidence promotion.

## Changed files

- `software/uqpu-prototype/uqpu/equation_discovery.py` — reject non-finite/non-real held-out metrics and malformed independent-validation counts; fail closed when checking held-out improvement.
- `software/uqpu-prototype/tests/test_equation_discovery.py` — add regression tests for NaN, positive/negative infinity, false promotion, boolean/string/object metrics and invalid validation counts.
- `docs/RESEARCH_GAP_RG045_NONFINITE_EQUATION_METRICS.md` — finding, counterexample, literature surveillance, falsifier and next gate.
- `integration/INT-20261024-013_EQUATION_METRIC_FINITE_GATE.md` — cross-lane integration and invariant traceability.
- This pending-main note records the sync boundary.

## Validation state

The code and tests are committed on the research branch. Hosted CI has not yet completed for the final branch head; therefore no new test pass is claimed. No local repository checkout was available in this run. The next acceptance condition is exact-head GitHub Actions success, followed by review and merge through the repository's normal integration path.

## Current repository / CI boundary

At inspection time, `main` pointed to `c7b5958af58fad04a101ef5c6abf6a29293c867e` (merge commit dated 2026-10-22 17:06:54 UTC). Its combined commit-status response contained no status entries. Recent open PRs #56–#60 carried newer research and CI runs; those branches are not main content. PR #56 (CoSR preregistration) and PR #58 (task-resolved Fisher ledger) had successful exact-head prototype/invariant and cold-start checks in the inspected runs. PR #60 had an earlier cold-start failure followed by a successful fix-branch run. These facts are snapshots, not substitutes for this branch's CI.

The root append-oriented `RESEARCH_GAPS.md`, `WORKLOG.md`, discovery registry and cold-start manifest were not overwritten because several open branches are concurrently adding to them. The canonical multilingual strategic-plan links and directives 00–06 remain untouched.

## A–H and permanent invariant status

Lane A receives the actual code change; B–H were explicitly reviewed in `INT-20261024-013`. No paid QPU job was submitted. INV-025/026/027 and INV-029–035 remain unchanged; BIO-001, FUS-001 and FIN-001 receive no new measured evidence. AI-generated equations and the current 100x/100,000,000x mission targets remain evidence-gated.

**Next highest-value gate:** exact-head hosted CI, then a review of adjacent metric schemas for the same finite-value issue. Do not merge or promote based on a non-final CI snapshot.
