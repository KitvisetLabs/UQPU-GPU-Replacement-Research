# Pending research sync - PR #53 PiT-PO adaptive equation-search audit

Date: 2026-10-24
Status: PENDING_MAIN_REVIEW; this is a discoverability record, not a claim that source work is merged.
Canonical main at source start: c7b5958af58fad04a101ef5c6abf6a29293c867e
Source branch: research/2026-10-24-equation-discovery-audit-v2
Source head for this delta: 992d07fd70f0ffc57e484b43a8f70f0a3f375694
Source PR: https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/pull/53
Pending-sync PR: https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/pull/54

## Source-branch delta

This source commit adds:
- software/uqpu-prototype/uqpu/search_comparison.py
- software/uqpu-prototype/tests/test_search_comparison.py
- research_lanes/A_quantum_programming_runtime/EXP-DESIGN-003_PITPO_MATCHED_SEARCH_BENCHMARK.md
- research_lanes/H_strategy_finance_future_industries/LITERATURE_WATCH_2026-10-24_PITPO_ADAPTIVE_EQUATION_SEARCH.md
- integration/INT-20261024-008-PITPO-ADAPTIVE-EQUATION-SEARCH.md
- integration/COLD_START_HANDOFF_MANIFEST.json updated with the new files, work IDs, lane status and current frontier.

The new dependency-free SearchBudget/SearchRun contract validates matched benchmark/split digests and declared resource caps, actual usage, false-discovery counts, held-out error, hard-constraint compliance, independent replay, and the conditions under which cost-per-accepted-model and energy comparisons are defined. Thirteen scratch unit tests passed before commit.

## Literature delta and scientific boundary

Wang et al., arXiv:2602.10576v2, describe PiT-PO, an adaptive in-search policy-optimization method for symbolic equation discovery, with a reported KDD 2026 acceptance. This is external method evidence only. The Support Exclusion Theorem has explicit finite-dictionary, sparse-support, coefficient-bound, Gram-matrix and interference assumptions. The practical normalized-coefficient threshold rho = 1e-2 is not by itself a theorem guarantee. The proposed EQN-002C / EXP-DESIGN-003 audit therefore includes a true small-coefficient term, correlated basis functions, missing-basis tests, equivalent unit/basis rescaling, OOD held-out groups, shuffled-feedback controls, independent replay and total cost per accepted useful model.

The benchmark and source-paper reproduction were not executed. No model API, QPU, provider, instrument, purchase or external funding action was used. No new physical law, quantum advantage, material substitution, accepted fuel/electricity, WACC effect or Data-Center-to-One-Phone achievement is claimed.

## CI snapshot at record creation

Exact source-head workflow run 40043329775:
https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40043329775

At the latest poll, unit/invariant jobs passed on Python 3.10, 3.11 and 3.12. The Python 3.12 log reported 589 tests passing. QSP phase synthesis, target-snapshot identity and target no-submit transpilation had passed; remaining QSVT, routed-probe, Qiskit-verification and reference-benchmark jobs were still in progress. Cold-start handoff audit run 40043325641 passed on the same source head. Re-check the latest exact-head workflow state before merge; no full-CI pass is claimed by this snapshot.

## A-H and INV-029..035

- A: matched equation-search run contract implemented; the synthetic benchmark is NOT EXECUTED.
- B: no provider or QPU calls; no-submit boundary preserved.
- C: data/split digests and classical output remain explicit; no memory/state equivalence claim.
- D/G: no device, process, fabrication or factory result.
- E: no Pangola material, accepted bio-oil, net reliable fusion-electricity or cooling result.
- F: cost per accepted model is undefined when cost is unknown or no model is accepted; energy comparison is unavailable if any run lacks energy measurement.
- H: literature and strategic provenance recorded; no funding/WACC claim.
- FND-001..006 and EQN-001..006 remain evidence-gated; the new work strengthens EQN-002/003/004 methods only.
- INV-029: physical Data-Center-to-One-Phone remains unachieved.
- INV-030: no elemental transmutation or universal material substitution.
- INV-031/032: commercial ultra-low-cost bio-oil and net reliable fusion electricity remain unproven.
- INV-033: no financing-principal, absolute-interest or WACC effect measured.
- INV-034/035: foundational search is open, but present physics remains binding for engineering claims.

The permanent eight root directives, docs/KANUSANAN_PONGPANNA_MODEL.md, STRATEGIC_PLAN_REFERENCES.md and Thai/English/Chinese/Japanese/Korean/German public master-plan links remain preserved. INV-025/026/027 and the 100,000,000-GPU / universal 100,000,000-unit moonshots remain falsifiable goals.

## Next gate

Finish all jobs on source head 992d07fd70f0ffc57e484b43a8f70f0a3f375694, then run the frozen synthetic pilot under the declared matched budgets if suitable local compute is available. Preserve this pending-sync state until PR review/merge; reconcile overlapping PRs #48-#53 without force-pushing main.

Research-Sync: pending-main
