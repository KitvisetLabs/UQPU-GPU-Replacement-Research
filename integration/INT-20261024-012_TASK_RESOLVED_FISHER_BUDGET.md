# Integration contract INT-20261024-012 — task-resolved Fisher information and accepted-task cost

**Status:** `PROPOSED / MODEL_ONLY / PENDING-MAIN`  
**Date:** 2026-10-24  
**Primary owner:** Lane F — benchmark evidence and integration  
**Technical owner:** Lane C; Lane A runtime interface; Lane H literature provenance  
**Canonical base SHA:** `c7b5958af58fad04a101ef5c6abf6a29293c867e`  
**Source commit / PR mapping:** recorded in the associated PR and the next main-sync summary; not merged at this stage.

## Inputs and evidence class

- External literature: Yang Peng, “Task-Resolved Fisher Spectroscopy for Quantum Reservoir Computing,” arXiv:2609.29570, 2026-08-26; `LITERATURE_ONLY`.
- Gap: `docs/RESEARCH_GAP_RG044_TASK_RESOLVED_FISHER_SPECTROSCOPY.md`.
- Lane-H source watch: `research_lanes/H_strategy_finance_future_industries/LITERATURE_WATCH_2026-10-24_TASK_RESOLVED_FISHER_SPECTROSCOPY.md`.
- Software interface: `software/uqpu-prototype/uqpu/task_resolved_fisher.py`.
- Unit tests: `software/uqpu-prototype/tests/test_task_resolved_fisher.py`.

## Integration hypothesis

If task-specific information lost at measurement and feature compression predicts the finite-shot resources needed for an accepted output, Lane C can choose a representation that minimizes record/feature movement without changing the useful-output contract. The hypothesis fails if the information diagnostic does not predict blind held-out quality, if shot and reconstruction overhead dominates, or if a matched classical baseline is cheaper.

## Shared contract

Every record is bound to one workload ID, model ID/version, immutable task-score-basis ID, split SHA-256, evidence label, exact provider/target context where applicable, and explicit feature-order cutoff. QFI, complete-record Fisher information and retained-feature matrices must use the same score coordinates. Analytic matrices must satisfy the expected matrix-order hierarchy; estimated matrices may violate the point-estimate hierarchy under finite data and must carry uncertainty diagnostics.

The Python contract reports:
- information trace retention only within the same task-score basis;
- raw-record bytes / retained-feature bytes (classical representation only);
- quality acceptance against a preregistered threshold;
- end-to-end energy/cost per accepted task only when the full-run boundary is known;
- `None` for unknown energy/cost or zero accepted tasks.

It does not prove that an equation is a physical law, that the QFI hierarchy was experimentally observed, or that a lower feature byte count improves total system cost.

## A–I integration scan

| Lane | Contribution / status |
|---|---|
| A — workloads/compiler/runtime | Use the same accepted prediction task and quality predicate across feature orders; freeze model selection before blind testing. |
| B — cloud/QPU integration | Provider-neutral metadata only; zero provider calls and zero paid jobs. |
| C — state/memory/storage/data movement | Primary technical owner: compare measured record bytes, retained-feature bytes, shot budget and reconstruction overhead. |
| D — devices/chips/process/packaging | No device requirement changes until a repeatable target-specific effect is independently established. |
| E — biomass/materials/bio-oil/fusion/cooling | No direct result for BIO-001, INV-030, INV-031 or INV-032; future energy measurements must preserve the full boundary. |
| F — economics/evidence/integration | Require same-quality total-resource comparison and cost per accepted window; unknowns remain unknown. |
| G — manufacturing equipment/factory systems | D/G co-design remains downstream of validated device requirements; no process-window/yield claim. |
| H — strategy/finance/publication | Preserve provenance and publish the falsifiable follow-up; no financing/WACC claim. |
| I — field-agnostic vehicle-lift specialist lane | No causal connection established; remain explicitly unchanged. |

## Foundational / invariant traceability

- **FND-001:** adds finite-shot resource measurements to future thermodynamic-gap accounting; no energy gap is measured here.
- **FND-002:** strengthens output-information accounting without claiming that quantum state-space dimension is readable classical storage.
- **FND-003:** offers a possible task-specific observable for later matched control measurements; no speed-limit experiment was run.
- **FND-004 / FND-005:** no new physical primitive or particle/QFT mechanism.
- **FND-006 / EQN-001:** advances reproducible, task-defined mathematical diagnostics. EQN-002–006 remain gated on their existing tests, proof/simulation, experiment and independent validation.
- **INV-029:** improves the accounting contract only; no phone-class physical-compression result.
- **INV-030–033:** no new materials, accepted fuel, net fusion electricity, financing principal or interest measurement.
- **INV-034–035:** method development only; no new law or displaced physical limit.
- **INV-025–027:** retain subsystem-specific equivalent-useful-output contracts and the 100M-unit moonshots as falsifiable goals.

## Required next gate

Audit the source artifacts and licensing, reproduce the five-spin numerical example, freeze train/validation/held-out split hashes, then compare full-record and feature-order arms under equal finite-shot and total-resource budgets. Require independent replay before any positive method claim. No paid QPU execution without explicit authorization.

## Sync debt and rollback

This work is not on `main` until merged. The root-level append-only directives, `VERSION_INVARIANTS.md`, `RESEARCH_GAPS.md`, `integration/COLD_START_HANDOFF_MANIFEST.json` and other canonical ledgers are not overwritten in this branch. If the branch is not merged, a separate pending-main summary PR must record its source SHA, changed files, tests, evidence class, limitations and next gate. Rollback consists of reverting this branch/PR; no provider, data or hardware state was changed.
