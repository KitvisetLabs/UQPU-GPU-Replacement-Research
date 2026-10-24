# Pending research sync - PR #53 PiT-PO adaptive equation-search audit

Date: 2026-10-24
Status: PENDING_MAIN_REVIEW; this is a discoverability record, not a claim that source work is merged.
Canonical main at source start: c7b5958af58fad04a101ef5c6abf6a29293c867e
Source branch: research/2026-10-24-equation-discovery-audit-v2
Initial implementation head: 992d07fd70f0ffc57e484b43a8f70f0a3f375694
Latest source head after Lane A QAOA literature integration: 8d717d64688a713fb3c8799c26a9b02e9d8fab6b
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
- research_lanes/A_quantum_programming_runtime/LITERATURE_WATCH_2026-10-24_QAOA_GRAPH_SPARSIFICATION.md
- research_lanes/A_quantum_programming_runtime/QAOA-SPARSE-001_MATCHED_ACCEPTED_TASK_BENCHMARK.md
- docs/literature_watch/2026-10-24-qaoa-graph-sparsification.md
- integration/INT-20261024-009-QAOA-GRAPH-SPARSIFICATION.md

The new dependency-free SearchBudget/SearchRun contract validates matched benchmark/split digests and declared resource caps, actual usage, false-discovery counts, held-out error, hard-constraint compliance, independent replay, and the conditions under which cost-per-accepted-model and energy comparisons are defined. Thirteen scratch unit tests passed before commit.

## Literature delta and scientific boundary

Wang et al., arXiv:2602.10576v2, describe PiT-PO, an adaptive in-search policy-optimization method for symbolic equation discovery, with a reported KDD 2026 acceptance. This is external method evidence only. The Support Exclusion Theorem has explicit finite-dictionary, sparse-support, coefficient-bound, Gram-matrix and interference assumptions. The practical normalized-coefficient threshold rho = 1e-2 is not by itself a theorem guarantee. The proposed EQN-002C / EXP-DESIGN-003 audit therefore includes a true small-coefficient term, correlated basis functions, missing-basis tests, equivalent unit/basis rescaling, OOD held-out groups, shuffled-feedback controls, independent replay and total cost per accepted useful model.

The benchmark and source-paper reproduction were not executed. No model API, QPU, provider, instrument, purchase or external funding action was used. No new physical law, quantum advantage, material substitution, accepted fuel/electricity, WACC effect or Data-Center-to-One-Phone achievement is claimed.

## CI snapshot at record creation

Initial source-head workflow run 40043329775:
https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40043329775

Latest source head 8d717d64688a713fb3c8799c26a9b02e9d8fab6b has cold-start audit run 40048819369 green:
https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40048819369
The exact-head prototype/invariant run 40048822792 is still IN_PROGRESS at this snapshot:
https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40048822792
Python 3.10, 3.11 and 3.12 test jobs passed; QSVT ten-query/bounded-prefix/eight-query, Qiskit verification and routed-statevector probes were still running. Do not claim full exact-head CI until every required job completes. The source tree change after 992 is documentation/manifest only; no QPU or provider execution occurred.

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

Finish all jobs on source head 8d717d64688a713fb3c8799c26a9b02e9d8fab6b, then run the frozen synthetic pilot under the declared matched budgets if suitable local compute is available. QAOA-SPARSE-001 is a separate proposed offline gate, NOT EXECUTED. Preserve this pending-sync state until PR review/merge; reconcile overlapping PRs #48-#53 without force-pushing main.

## Parallel Lane F update — 2026-10-24

PR #49 was extended on branch head b15a25ab47f497a4883f58a892acda0211e26197 with a Lane-F-owned watch and integration note for Yadav & Lam's biomass pyrolysis TEA (DOI 10.1021/acs.energyfuels.5c05655) and Whyte et al.'s fusion economic-gain criterion (DOI 10.1007/s10894-026-00577-9). Stable proposed follow-ups: BIO-TEA-001 and FUS-ECON-001. Its cold-start audit run 40049026771 passed; prototype/invariant jobs remain in progress at this snapshot. This branch is separate from PR #53 and is not merged. Neither paper demonstrates commercial fuel, net fusion electricity, a WACC change or mission achievement.

## Open-PR reconciliation snapshot

- PR #48 exact-head prototype/invariant and cold-start workflows: success.
- PR #50 exact-head prototype/invariant and cold-start workflows: success.
- PR #51 exact-head prototype/invariant and cold-start workflows: success.
- PR #49 and PR #53: latest full prototype/invariant workflows still in progress; cold-start audits green.
- PR #54: pending-sync summary only; keep unmerged until the source deltas and overlap/conflict plan are reviewed.

PR #53 overlaps PR #51 on equation-discovery implementation/tests and the handoff manifest; PR #49 is a supplement to PR #48. Do not force-push main or assume branch-only work is canonical.

Research-Sync: pending-main
