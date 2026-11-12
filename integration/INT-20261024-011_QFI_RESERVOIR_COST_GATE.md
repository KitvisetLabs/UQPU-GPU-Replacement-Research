# Integration contract INT-20261024-011 — QFI-aware reservoir optimization and end-to-end cost

**Status:** `PENDING-MAIN / REVIEW REQUIRED`  
**Canonical base:** `main` at `c7b5958af58fad04a101ef5c6abf6a29293c867e`  
**Primary owner:** Lane F — economics / benchmark evidence / integration  
**Related work:** literature watch `docs/literature_watch/2026-10-24-qfi-aware-reservoir-optimization.md`, gap `RG-043`

## Integration decision

Treat the QFI-aware quantum-reservoir paper as an external, reproducibility-first workload lead. It is relevant to the software-first and AI-training-cost research only after the reported numerical result is reproduced and the optimizer is compared under matched total resources. Do not translate a readout-size comparison or held-out-error margin into a project-wide quantum advantage or a cost claim.

## Stable comparison contract

The same task and data-generation process must feed all arms. Freeze the forecast horizon, train/validation/held-out hashes, preprocessing, precision, prediction acceptance threshold, evaluation metric and seed schedule. Held-out data cannot guide parameter search, feature choice, stopping, prompt selection or repair.

Minimum arms:
1. QFI-aware optimizer on the same quantum reservoir family.
2. The paper's simple/grid-plus-Bayesian optimization stage.
3. Continued black-box optimization given the same additional trajectory-evaluation budget.
4. A tuned echo-state-network baseline.
5. A second classical temporal/neural baseline only when its budget and training protocol are frozen before evaluation.

## Resource ledger and acceptance

Report two distinct decisions:

- **Quality acceptance:** the preregistered useful-output threshold is met on blind held-out windows, with seed/window uncertainty and no unreported constraint or leakage failure.
- **End-to-end economics:** compare total cost per accepted prediction window using the same cost boundary. Include parameter/trajectory evaluations, state preparation, QFI estimation and shots, measurement/readout, retries, reconstruction, host compute, memory and data movement, wall-clock latency/throughput, calibration, energy where measured, device/provider charges and utilization/amortization when applicable.

Unknown energy and cost remain unknown; they are not zero. Do not combine success probability from one provider/target with another target's price. A simulator result is not a hardware result.

## A–H handoff

| Lane | Required contribution / interface |
|---|---|
| A | Workload semantics, reproducible optimizer arms and accepted-prediction contract. |
| B | Provider-neutral path only after local reproduction; no provider/QPU calls in this integration. |
| C | State/feature buffers, input/output and reconstruction/data-movement accounting. |
| D | Physical-reservoir device requirements only after a validated system-level effect; maintain D/G co-design. |
| E | No current BIO-001/FUS-001 or material result; later measured models must use full mass/energy/cost boundaries. |
| F | Matched total-resource budgets, uncertainty, quality gate, lifecycle/accepted-task economics and evidence labels. |
| G | No fab-tool, yield or process-window claim until device requirements are validated. |
| H | Literature provenance, public research article and capital-staging decision. |

## Cross-cutting foundation and invariants

FND-001 has no new measured energy gap; FND-002 still requires explicit I/O and output-information accounting; FND-003 has no new control-vs-speed-limit measurement; FND-004 has no accepted new physical primitive; FND-005 has no particle/QFT mechanism; FND-006 gains a reproducibility-first optimizer question. EQN-001 gains the literature watch; EQN-002–004 remain unexecuted; EQN-005 does not change incumbent physics; EQN-006 remains blocked on independent validation and full system/economic accounting.

INV-029 remains `LONG-HORIZON / NOT_YET_DEMONSTRATED`. INV-030–033 remain permanent strategic pillars without new material, fuel, fusion or financing evidence. INV-034–035 are advanced methodologically only; no new law is claimed. INV-025/026/027 remain falsifiable goals with subsystem-specific equivalent-useful-output contracts.

The eight permanent root directives, `docs/KANUSANAN_PONGPANNA_MODEL.md`, `STRATEGIC_PLAN_REFERENCES.md`, and Thai/English/Chinese/Japanese/Korean/German public master-plan links and recorded strategic AI-agent/funding references are preserved unchanged.

## Sync debt

This branch adds a standalone literature watch, gap artifact and integration contract. It does not edit the append-only `RESEARCH_GAPS.md`, `WORKLOG.md`, root discovery registry, README or cold-start manifest because multiple open PRs own pending suffixes. After exact-head CI and review, reconcile the stable `RG-043` and `INT-20261024-011` references into those canonical indexes without overwriting concurrent history.


## Research handoff and CI status

This artifact is a pending-main proposal based on canonical main SHA `c7b5958af58fad04a101ef5c6abf6a29293c867e`. The first cold-start handoff audit identified a governance failure, not a scientific failure: the commit message lacked the required `Research-Sync: pending-main` trailer. A follow-up commit restores the trailer and requests a fresh exact-head audit. The paper reproduction and matched-budget benchmark remain NOT EXECUTED.

## Next gate

Hash and audit the cited public reproduction deposit, then run the frozen source-reproduction check. Only after it passes should the matched-budget UQPU benchmark execute. No paid QPU job is requested or authorized.
