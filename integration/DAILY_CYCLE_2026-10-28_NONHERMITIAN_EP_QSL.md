# Daily Eight-Lane integration — 2026-10-28 — exceptional-point QSL and accepted-output accounting

**Starting main SHA:** `b3252a556b61b7e566d5e057606c1f2e917d79e8`  
**Batch:** [095 — non-Hermitian exceptional-point speedup and accepted-output QSL accounting](../docs/BATCH_095_NONHERMITIAN_EP_QSL_ACCEPTED_TASK_GATE.md)  
**Primary owner:** Lane A — matched control/output contract; Lane H — literature  
**Integration ID:** `INT-20261028-FND003-NH-EP-001`  
**Evidence class:** LITERATURE_ONLY + PREREGISTERED_GAP  
**Status:** PROPOSED / RECONSTRUCTION_NOT_RUN / EXACT-HEAD-CI_UNVERIFIED

## What changed

- Added official APS source coverage for a trapped-ion exceptional-point experiment and a transition-rate/QSL framework for open processes.
- Opened RG-FND003-NH-EP-001 with explicit incumbent assumptions, candidate model, required physical checks, held-out cases and a falsifier.
- Defined the comparison boundary as total resources per accepted output rather than conditional gate time alone.
- Kept the existing signed-Max-Cut pinned-Qiskit gate as the immediate Lane A priority.

## Cross-lane integration

The candidate integration is:
`target-specific control model + complete open-system outcomes -> accepted-output time/quality -> measured energy and total cost`.

D/G co-design is required before any device transfer. Lane E must include controller, reservoir, dissipation and cooling. Lane C must retain state/readout/reset/retry/reconstruction resources. Lane F owns matched accounting and uncertainty. Lane B preserves provider/target-specific provenance. Lane H maintains source and strategic-plan context.

## A–H review

| Lane | Status | Integration edge |
|---|---|---|
| A | ACTIVE / PRIORITY #1 | Signed-Max-Cut SDK CI remains first; FND003-NH-EP-001 is a secondary offline test contract. |
| B | ACTIVE / NO SUBMISSION | No provider call; future evidence must bind target, calibration and billing. |
| C | ACTIVE / ACCOUNTING CONTRACT | Count state preparation, readout, failed outcomes, reset, retries, memory and data movement. |
| D | ACTIVE / MODEL-ONLY INTERFACE | Match control assumptions to a device before hardware transfer. |
| E | ACTIVE / NO MATERIAL-ENERGY CLAIM | Include reservoir, dissipation and cooling; no bio-oil/fusion/material result. |
| F | ACTIVE / EVIDENCE GATE | Measure accepted-output quality, total time, energy and cost separately. |
| G | ACTIVE / D-G CO-DESIGN | No fabrication/yield claim; device/process consequences await validation. |
| H | ACTIVE / PUBLICATION | Publish source-bounded evidence and preserve the multilingual strategic model. |

## Foundational and invariant impact

FND-001/003/004 gain a tighter accounting and comparison specification. FND-002 and FND-005 are unchanged. FND-006 and EQN-001–006 retain the mandatory hypothesis/falsifier/held-out/independent-validation contract. INV-029–033 remain goals without new mission-level evidence; INV-034/035 are advanced methodologically only. INV-025/026/027 and the permanent root directives remain intact.

## CI and synchronization

The latest main commit's combined-status endpoint returned no status contexts; the available commit-workflow-run query is limited to pull-request-triggered runs and returned none for the main push. Exact-head CI is therefore **UNVERIFIED**. This branch is pending review and is not canonical main. Large append-only `WORKLOG.md` and `RESEARCH_GAPS.md` were not rewritten; record their sync debt in the pending-main PR and reconcile after merge.

## Next highest-value gate

1. Verify the exact-head GitHub Actions run for the current signed-Max-Cut source fix.
2. Freeze a small open-system model and run two independent offline evaluators for FND003-NH-EP-001.
3. Compare Hermitian and exceptional-point arms on the same target quality, control budget and accepted-output boundary.
4. Reject any claimed advantage that does not survive failure, retry, control, reset, dissipation, energy and cost accounting.
