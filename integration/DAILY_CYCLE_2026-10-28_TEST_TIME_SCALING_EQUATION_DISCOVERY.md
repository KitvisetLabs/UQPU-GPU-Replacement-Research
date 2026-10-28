# Daily integration — 2026-10-28 — test-time scaling for equation discovery

**Cycle start:** `d63de3e3eaa6696df2cad55ec78f66e1ad06fd2c`  
**Cycle artifacts:** [Batch 098](../docs/BATCH_098_TEST_TIME_SCALING_EQUATION_DISCOVERY.md), [literature watch](../docs/literature_watch/2026-10-28-test-time-scaling-equation-discovery.md), [RG-EQN-008](../docs/RESEARCH_GAP_EQN008_MATCHED_DISCOVERY_COMPARISON.md)  
**Evidence:** external peer-reviewed method paper + protocol proposal; no UQPU benchmark or physical experiment

## Shared interface changes

The official EMNLP 2026 paper motivates adding search width as a preregistered configuration factor to the existing schema-v4 matched equation-discovery comparison. Each width must be a distinct arm with a fixed configuration hash across its preregistered seeds. All arms share dataset/source/license provenance, preprocessing, grammar, units, acceptance rules, group-disjoint split manifests, seed set and hard resource ceilings. This is a design update only; no method was run or ranked.

## A–H review and cross-lane integration

| Lane | Integration status | Stable edge / next gate |
|---|---|---|
| A | Protocol advanced; remains Priority #1 | RG-EQN-008 width factor; continue signed-Max-Cut lowering/reference/simulator gate after exact-head CI. |
| B | Provider-neutral path preserved | No credentials or paid QPU jobs; provider/target prices and probabilities remain target-specific. |
| C | Resource contract preserved | Count tokens, candidate evaluations, peak memory, host compute, I/O and reconstruction; state-space size is not classical storage. |
| D | Device research preserved | Any equation-derived process/device model needs measured windows, metrology, yield and reliability. |
| E | BIO-001/FUS-001 gates preserved | No accepted saleable liquid or reliable net delivered fusion electricity evidence added. |
| F | Acceptance design advanced | Equal budgets, held-out errors, uncertainty, counterexamples, false discoveries and one cost basis per comparison. |
| G | D/G co-design preserved | Process equations must eventually connect to factory control, defectivity and cost per good die/package. |
| H | Literature publication and handoff advanced | Official source linked; multilingual master-plan and strategic agent/funding context remains context, not evidence. |

The 28 unordered A–H interfaces remain required. The strongest specific links this cycle are A↔F, A↔H, C↔F, D↔G and E↔F↔H. INV-034/035 feed every lane; no scientifically unsupported coupling is asserted.

## Evidence boundary and next gate

The reported search-width pattern is external literature, not UQPU evidence. It does not establish a new physical law or downstream computing/material/fuel/fusion/finance advantage. Current main's combined-status query returned no check entries at the cycle-start SHA, and the available workflow-run connector only exposes PR-triggered runs; exact-head CI is therefore unverified. After the cycle's final main SHA is known, re-query combined status and available Actions evidence, and record any limitations.

**Next gate:** exact-head prototype/invariant and cold-start audit; then freeze dataset/model/source/runtime manifests and group-disjoint split certificates before any 30-seed comparison. Lane A provider-neutral lowering on the frozen signed-Max-Cut contract remains the highest execution priority. No paid QPU execution is authorized.
