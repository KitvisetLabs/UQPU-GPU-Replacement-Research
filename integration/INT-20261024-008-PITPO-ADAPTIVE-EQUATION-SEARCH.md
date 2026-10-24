# INT-20261024-008 - adaptive equation-search integration contract

Date: 2026-10-24
Status: PROPOSED / BENCHMARK NOT EXECUTED
Primary component owner: Lane A
Literature owner: Lane H
Integration owner: Lane F
Evidence class: SOFTWARE_CONTRACT
Canonical main at cycle start: c7b5958af58fad04a101ef5c6abf6a29293c867e
Source branch at cycle start: research/2026-10-24-equation-discovery-audit-v2
Source start SHA: 76f6f5957e280893e713f1983f0390a4995675a9

## Hypothesis and causal mechanism

Adaptive search feedback may improve the rate at which a constrained equation-search process returns useful, generalizing equations. The proposed mechanism is in-search policy adaptation plus physics constraints and a redundancy penalty. It competes against static prompting, classical symbolic regression and a shuffled-feedback control.

This is a hypothesis about search efficiency and candidate quality, not a claim that the discovered equations are new physical laws.

## Stable interface

Lane A provides SearchBudget and SearchRun records through software/uqpu-prototype/uqpu/search_comparison.py. The validator requires:
- identical benchmark, dataset and train/validation/held-out digests across compared methods;
- identical declared wall-time, evaluator-call, token, optional-energy and optional-direct-cost caps;
- actual resource usage within caps;
- finite nonnegative held-out errors and costs;
- first-class false-discovery counts where ground truth makes them measurable;
- independent replay for each accepted useful model;
- undefined cost/energy comparisons when their measurements are absent.

Lane H owns the PiT-PO literature watch and theorem-assumption audit. Lane F owns full resource and cost accounting. The synthetic experiment is defined in research_lanes/A_quantum_programming_runtime/EXP-DESIGN-003_PITPO_MATCHED_SEARCH_BENCHMARK.md.

## Cross-lane interface and mission scan

- A: implement the matched-run schema and test fail-closed behavior; the synthetic search benchmark is not executed.
- B: no provider adapter or QPU is used; preserve provider-neutral no-submit rules.
- C: dataset digests, stored candidate state, reconstruction and classical output remain explicit; no quantum-state/readable-memory equivalence is inferred.
- D: no device or chip requirement follows from an equation-search result alone.
- E: no Pangola-carbon material qualification, saleable bio-oil, fuel-cost or net-delivered-fusion-electricity result is produced.
- F: total direct cost per accepted useful model is defined only when both total run cost and accepted count are known; energy efficiency is undefined when energy is unknown.
- G: no fabrication process, yield or factory-equipment requirement is promoted.
- H: peer-reviewed method evidence and the authors' preprint/repository are preserved as external provenance, not UQPU evidence.
- INV-034/035: constraints, counterexamples, held-out prediction and independent replay remain mandatory. A fixed coefficient threshold cannot bypass the theorem's assumptions.

D/G co-design remains active but downstream of a validated device or material mechanism. The other permanent lanes are not suspended by this experiment.

## Evidence, resources and economics

Current evidence is limited to a literature review and 13 scratch unit tests for the comparison contract. No PiT-PO training, source-paper reproduction, QPU call, device/material experiment or economic benchmark was performed. No model API was called. Energy is not inferred from runtime, and direct cost must include model inference/fine-tuning, evaluation, storage, failed attempts, retries and independent replay. No cross-provider price/probability combination is allowed.

The source paper's normalized coefficient threshold is treated as heuristic unless the Support Exclusion Theorem assumptions and full inequality are verified for the actual dictionary and data. Equivalent unit/basis rescaling is a mandatory counterexample search.

## Invariants and non-claims

INV-029 remains a physical Data-Center-to-One-Phone goal, not achieved. INV-030 does not claim elemental transmutation or universal material substitution. INV-031 and INV-032 remain commercial bio-oil and net reliable fusion-electricity goals. INV-033 records no measured financing-principal, interest or WACC change. INV-034/035 are advanced only through a more testable equation-search protocol; no new physical law is claimed.

INV-025/026/027 and the 100,000,000-GPU / universal 100,000,000-unit moonshots remain falsifiable goals. The eight root directives, Kanusanan Pongpanna Model, STRATEGIC_PLAN_REFERENCES.md and Thai/English/Chinese/Japanese/Korean/German public plan links remain canonical and untouched.

## Next gate

1. Pass exact-head CI for the new source commit.
2. Run the synthetic pilot with frozen hashes and matched caps.
3. Report exact recovery, OOD error, false discoveries, constraint violations, independent replay, total cost per accepted useful model and energy only when measured.
4. Test unit/basis rescaling and theorem assumptions before any redundancy-pruning guarantee.
5. Update the pending-main sync record with the exact source SHA and current CI; do not claim synchronization until PR review and merge.
