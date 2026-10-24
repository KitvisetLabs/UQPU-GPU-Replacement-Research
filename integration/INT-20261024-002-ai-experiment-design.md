# INT-20261024-002 — AI experiment design and staged evidence gates

**Date:** 2026-10-24  
**Primary owner:** Lane H — publication and strategic research synthesis  
**Co-owners:** Lane A (offline workload/experiment contract), Lane F (matched-budget evidence and cost accounting)  
**Canonical source main SHA:** `c7b5958af58fad04a101ef5c6abf6a29293c867e`  
**Source branch:** `research/2026-10-24-equation-discovery-audit-v2`  
**Source literature artifact:** `research_lanes/H_strategy_finance_future_industries/LITERATURE_WATCH_2026-10-24_AI_EXPERIMENT_DESIGN.md`  
**Work ID:** `EXP-DESIGN-002`  
**Status:** PROPOSED_OFFLINE_BENCHMARK; current branch CI required  
**Evidence class:** LITERATURE_ONLY + MODEL_ONLY protocol proposal  
**Project evidence promotion:** none

## Hypothesis

A physics-aware, AI-proposed experimental plan may improve the number of accepted held-out model-discriminating results per total resource budget, but only if its advantage survives matched controls, simulator-discrepancy checks, hard feasibility constraints, and independent reproduction.

This is a falsifiable method hypothesis, not a statement that AI planning is generally superior or that an AI-generated equation is a physical law.

## Interface contract

Every candidate plan must contain:
- incumbent model and exact assumptions;
- alternative model/equation and the changed assumption;
- typed observable, units, predicted distributions, uncertainty and acceptance predicate;
- an explicit falsifier and held-out prediction;
- simulator/instrument capability and hard safety/feasibility constraints;
- frozen training/validation/held-out data identifiers and hashes;
- generation, simulator, host, transfer, instrument, retry, reconstruction and replication budgets;
- independent validation method and evidence class.

The evaluator, not the generator, decides acceptance. An experiment that violates a hard constraint is rejected even if its predicted information gain is high.

## Proposed offline design

1. Freeze known-law, noisy, held-out-domain and deliberately non-identifiable cases.
2. Compare a human-written baseline, a simple information-gain/optimal-design baseline and an AI planner under matched simulator calls, wall-clock, CPU/GPU time and energy where measurable.
3. Score held-out model discrimination, calibration, replicate stability, counterexample detection, hard-constraint violations, and accepted discriminating results per total budget.
4. Preserve null results, failed candidates and counterexamples.
5. Require independent simulator/analytic checks where feasible.
6. Do not access real instruments, provider credentials or QPU execution in this offline work item.

## Falsifier

Reject the hypothesis of practical improvement if the AI planner fails to outperform the simple baseline on accepted held-out discrimination, or if an apparent gain disappears after charging generator/evaluator cost, retries, transfer, reconstruction, feasibility violations and independent replication.

## Cross-lane interfaces

- **A↔F:** objective and accepted-result accounting; no raw fit score substitutes for accepted useful output.
- **A↔B:** provider-neutral capability metadata and no-submit preflight remain upstream of any execution.
- **C↔F:** state preparation, measured output bytes, data transfer, decoding, reconstruction and storage are reported separately.
- **D↔G:** process/instrument search must stay inside measured capability and fabrication windows.
- **D↔E:** materials/energy experiments require target-specific functional units and observables.
- **E↔F:** BIO-001 and FUS-001 use full accepted-product/net-electricity cost boundaries; generic AI planning adds no material or energy evidence.
- **H↔A–G:** strategic and publication layer carries evidence labels and does not strengthen a source's evidence class.
- **Lane I:** inspected as a repository extension; no relevant physical lift claim is supported by this work.

The remaining lane-pair combinations were reviewed for this integration decision and are marked not directly coupled to EXP-DESIGN-002 at this stage; artificial integration is not required. D/G co-design remains an explicit dependency where process or instrument design is involved.

## A–H cycle status

| Lane | Status after this delta | Next gate |
|---|---|---|
| A | Existing equation-discovery integrity guard and regression tests are on the PR branch; EXP-DESIGN-002 is only specified. | Run exact-head CI, then implement frozen offline cases. |
| B | Provider-neutral no-submit contract unchanged. | No provider access until separately authorized; read-only target metadata gate remains separate. |
| C | Output-information and reconstruction requirements preserved. | Add byte/precision/transfer/reconstruction counters to any accepted-task benchmark. |
| D | Device/instrument feasibility remains a hard constraint. | No device claim until target-aware measurements exist. |
| E | BIO-001/FUS-001 evidence status unchanged. | Pangola-specific accepted-liquid and net-electricity data required. |
| F | Matched-budget and full-cost methodology specified. | Execute the offline comparison and publish positive/negative results. |
| G | D/G co-design preserved; no factory or process result. | Require measured process-window and yield contracts. |
| H | Dated literature watch and this integration contract published on the PR branch. | Maintain source/date/evidence/provenance records and review the next gate. |

## FND/EQN and mission boundary

FND-001..006 and EQN-001..006 remain active. The new experiment-planning workflow can help select discriminating measurements, but does not revise thermodynamics, output-information limits, quantum-speed limits, established field equations or any no-go theorem. Any proposed challenge must identify the changed incumbent assumption, replacement equation, dimensional/symmetry/conservation/causality checks, limiting cases, falsifier, distinct observable, held-out prediction, proof or experiment, and independent validation.

INV-029 remains a physical-compression objective, not remote terminal access. INV-030 does not permit elemental transmutation claims. INV-031/032 require accepted liquid-energy and net reliable delivered-electricity measurements. INV-033 distinguishes lower principal/shorter capital lock-up from a separately evidenced lower WACC. INV-034/035 remain permanent cross-cutting research principles, not evidence that new physics has been established. INV-025/026/027 and all multilingual strategic links remain preserved.

## CI and synchronization

The parent branch head `a21450d432e7dc214cebfc4f7a58b32a4836f057` had a passing UQPU Prototype and Project Invariants workflow (run 40009861223) and passing cold-start handoff audit (run 40009852992). This integration commit changes the branch head, so those results do **not** validate the new head. Re-run both workflows on the final PR head before treating the addition as CI-validated.

The change is still on a PR branch. It is not merged to canonical `main`. The large append-only `WORKLOG.md`, `DECISIONS.md` and `RESEARCH_GAPS.md` were not rewritten from partial reads; synchronization debt remains explicit.

No QPU job, paid provider call, real instrument experiment, material/fuel/fusion measurement, physical-law claim or economic advantage is claimed.
