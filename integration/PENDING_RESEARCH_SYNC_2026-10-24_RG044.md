# Pending-main sync record — RG-044 task-resolved Fisher budget

**Status:** PENDING REVIEW / NOT MERGED  
**Date:** 2026-10-24  
**Canonical main SHA at start:** `c7b5958af58fad04a101ef5c6abf6a29293c867e`  
**Source repository:** `KitvisetLabs/UQPU-GPU-Replacement-Research`  
**Source branch:** `research/2026-10-24-task-resolved-fisher-ledger`  
**Source commits:** `dbc32d5f4eb8cdd16d42c7c5292ec8fab65da459` (initial artifacts); `15324b2a5ae6332b9a21ba9f23876c357773e1b7` (correct matrix-order direction); `ae4663b305c13dca61bd1a7c80fd41921b6014a3` (complete A–I pair scan).  
**Research PR:** #58 — https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/pull/58  
**Main sync mapping:** none yet; PR #58 is open and draft.

## Objective and files

Record the not-yet-merged work so a cold-start researcher can discover it without prior chat context.

- `software/uqpu-prototype/uqpu/task_resolved_fisher.py` — schema/consistency guard for task-score-basis QFI, complete-record Fisher information, feature-order matrices, feature bytes, shot budget and resource scope.
- `software/uqpu-prototype/tests/test_task_resolved_fisher.py` — tests for analytic information hierarchy, estimated-matrix warnings, PSD validation, accepted quality, representation ratios, unknown energy/cost, and provider/target provenance.
- `research_lanes/H_strategy_finance_future_industries/LITERATURE_WATCH_2026-10-24_TASK_RESOLVED_FISHER_SPECTROSCOPY.md` — Lane-H source assessment and falsifiable follow-up.
- `docs/RESEARCH_GAP_RG044_TASK_RESOLVED_FISHER_SPECTROSCOPY.md` — Lane-C-owned research gap and reproduction protocol.
- `integration/INT-20261024-012_TASK_RESOLVED_FISHER_BUDGET.md` — Lane-F integration contract and 36-pair A–I opportunity scan.

## Method and evidence

External source: Yang Peng, “Task-Resolved Fisher Spectroscopy for Quantum Reservoir Computing,” arXiv:2609.29570, submitted 2026-08-26. Evidence class is `LITERATURE_ONLY / THIRD_PARTY_PREPRINT`. The preprint proposes task-score coordinates connecting state QFI, complete measurement-record Fisher information, and retained feature moments; its five-spin open-reservoir demonstration is numerical, not UQPU hardware evidence.

The code validates record comparability and resource metadata. Analytic matrices must satisfy the information hierarchy; estimated matrices may show point-estimate hierarchy warnings. End-to-end cost/energy per accepted task is returned only when the full-run scope and accepted-task count are present. Unknown energy/cost remains `None`. The code is not a physical-law detector and does not reproduce the paper.

## Positive and negative results

- Initial CI on `dbc32d5f4eb8cdd16d42c7c5292ec8fab65da459` failed four new tests because the hierarchy check incorrectly required a retained feature matrix to dominate the complete measurement record.
- The defect was corrected in `15324b2a5ae6332b9a21ba9f23876c357773e1b7`: the complete record must dominate each compressed feature matrix, while higher feature order must dominate lower order.
- Hosted Python test matrix on `15324b2a5ae6332b9a21ba9f23876c357773e1b7` passed Python 3.10, 3.11 and 3.12. The full QOS/reference benchmark jobs were still in progress at the last check.
- The latest source head `ae4663b305c13dca61bd1a7c80fd41921b6014a3` has a new full-workflow run and cold-start audit in progress; do not report the final head as fully CI-green until those runs finish.
- The source literature has not been downloaded/hashed/licence-audited or reproduced. No provider calls, QPU jobs, measured energy, cost advantage, material/fuel/fusion result or new physical law is claimed.

## Cross-lane and invariant impact

- **A/C/F/H:** proposed measurement-information -> feature/shot budget -> quality-adjusted accepted-task cost integration.
- **B:** provider-neutral metadata only; zero provider calls and zero paid jobs.
- **D/G:** no target-specific device or manufacturing requirement; D/G co-design remains active but downstream-blocked.
- **E:** no new Pangola-carbon, accepted bio-oil, net fusion-electricity or cooling evidence.
- **I:** no supported causal connection to the specialist vehicle-lift lane.
- **INV-029:** accounting-contract progress only; no Data-Center-to-Phone physical compression result.
- **INV-030–033:** no material substitution, commercial fuel/electricity, financing-principal/interest or WACC result.
- **INV-034–035:** methodology and literature surveillance only; no new law and no displaced physical limit.
- **INV-025–027:** all moonshots remain falsifiable goals with subsystem-specific equivalent-useful-output contracts.
- The permanent root directives 00–06, `docs/KANUSANAN_PONGPANNA_MODEL.md`, `STRATEGIC_PLAN_REFERENCES.md`, multilingual Thai/English/Chinese/Japanese/Korean/German master-plan links, and strategic AI-agent/funding references were not modified.

## Next gate

1. Finish and inspect every workflow job for source head `ae4663b305c13dca61bd1a7c80fd41921b6014a3`.
2. Audit the source preprint, code, data provenance and licensing; pin hashes and environment.
3. Reproduce the five-spin numerical result, preserve failed outputs, and preregister blind train/validation/held-out splits.
4. Compare complete records with feature orders and finite-shot budgets under identical accepted-output quality and a matched classical baseline.
5. Merge only through normal review/CI. No paid QPU job without explicit user consent, credentials and a bounded budget.

## Remaining sync debt

- PR #58 is open; none of its source commits is on `main` yet.
- This file is a separate pending-main summary PR, not a claim that source code is already canonical.
- `README.md` still labels 2026-10-15 as its latest verified implementation checkpoint despite Batch 056 and newer open research branches; refresh that checkpoint in a dedicated reviewed change rather than rewriting the large README during concurrent work.
- `integration/COLD_START_HANDOFF_MANIFEST.json` still contains its older 2026-10-18 checkpoint and an older verified-CI reference; reconcile it in a dedicated reviewed update rather than overwriting it concurrently.
- This bookkeeping commit itself is recorded by Git history and should be included in the next reconciliation checkpoint.

Research-Sync: pending-main
