# Batch 095 — non-Hermitian exceptional-point speedup and accepted-output QSL accounting

**Date:** 2026-10-28  
**Starting main SHA:** `b3252a556b61b7e566d5e057606c1f2e917d79e8`  
**Primary owner:** Lane A — workload/control contract; Lane H owns literature publication  
**Cross-lane:** A–H; FND-001–006; EQN-001–006; BIO-001; FUS-001; FIN-001  
**Evidence class:** PEER_REVIEWED_LITERATURE_WATCH + PREREGISTERED_GAP; no UQPU reproduction  
**Hardware:** no provider contacted, no paid job and no physical experiment

## Starting-state audit

Resolved the newest `main` dynamically at `b3252a556b61b7e566d5e057606c1f2e917d79e8`. Re-read the project charter, version invariants, goals, README, operating system, open-frontier directive, Kanusanan Pongpanna Model, strategic references, root directives 00/00A/01–06, current Batch 094, Batch 093, focused QSL gap, latest signed-Max-Cut source/tests and equation-discovery helpers. The six-language Thai/English/Chinese/Japanese/Korean/German strategic references remain preserved.

The exact-head combined commit-status query returned no status contexts. The available commit-workflow-runs connector returns only pull-request-triggered runs and returned no runs for this main push. Therefore exact-head Actions status is **UNVERIFIED**, not green. The latest source fixes the certificate runner's newline literal, but no hosted result is inferred from that change.

## Literature delta

Added a focused watch for two official APS primary sources not found in the current repository search:
- Yuan et al., PRL 136, 210201, published 2026-05-28, DOI 10.1103/g8v5-rbq7: trapped-ion exceptional-point route, with source-reported faster entanglement generation relative to an equivalent Hermitian interaction and a success-probability trade-off.
- del Campo et al., PRL 136, 210202, published 2026-05-28, DOI 10.1103/l7dq-n61h: flux-flux-correlator transition rates and complementary quantum speed limits for open processes, including measurements.

These do not replace the current QSLs or establish a universal bound violation. They sharpen the need to compare conditional dynamics with total resources per accepted output.

## Work produced

1. `docs/literature_watch/2026-10-28-nonhermitian-ep-speedup-and-transition-rate-qsl.md` — Lane H primary-source watch, limitations and falsifiable follow-up.
2. `docs/RESEARCH_GAP_FND003_NONHERMITIAN_EP_2026-10-28.md` — stable gap RG-FND003-NH-EP-001.
3. `integration/INT-20261028-FND003-NH-EP-001.json` — machine-readable cross-lane interface and acceptance gate.
4. `integration/DAILY_CYCLE_2026-10-28_NONHERMITIAN_EP_QSL.md` — A–H handoff, invariant impact and sync/CI status.

Large append-only `WORKLOG.md` and `RESEARCH_GAPS.md` are intentionally not rewritten. Their sync debt is recorded here and must be reconciled after review/merge.

## A–H status

| Lane | Current status and this-cycle contribution | Next gate |
|---|---|---|
| A — workloads/compiler/runtime | Priority #1 remains the signed-Max-Cut pinned-SDK gate; FND003-NH-EP-001 adds a matched accepted-output control protocol, not code or performance evidence. | Verify exact-head SDK certificate runner; then independent small-model open-system reconstruction. |
| B — cloud/QPU integration | Provider-neutral routes retained; no target, credential or job used. | Preserve provider/target/calibration/billing identity in any future result. |
| C — memory/state/data movement | Include failed trajectories, state preparation, readout, reset, retries and reconstruction. No state-space-to-classical-storage equivalence. | Add resource fields to a frozen execution contract before any hardware test. |
| D — device/chip/process | Exceptional-point controls are target-specific; no device calibration or fabrication result. | Match the model to a real device only after authorized and bounded evidence planning. |
| E — materials/energy/fuel/fusion/cooling | Full controller/reservoir/dissipation/cooling boundary retained; no Pangola, fuel or fusion result. | Charge all physical energy streams in a future measurement. |
| F — evidence/economics/integration | Distinguish QSL, model time, conditional success and total accepted-output time/energy/cost. | Use measured totals and accepted counts; keep uncertainty and failed attempts. |
| G — manufacturing/factory systems | D/G co-design remains visible; no process/yield/equipment claim. | Only derive device/process requirements after a validated control target exists. |
| H — strategy/publication | New official-source watch and self-contained gap; six-language strategic plan preserved. | Independently replay and publish null/negative outcomes as well as positive ones. |

## Foundational and equation-discovery status

- FND-001: add controller, measurement, reset, reservoir and dissipation costs to the energy boundary; no measured thermodynamic gain.
- FND-002: no new output-information lower bound.
- FND-003: sharpen matched control-vs-QSL comparison and separate conditional from accepted-output time.
- FND-004: preserve non-Hermitian/open-system route as a hypothesis under explicit assumptions, not a universal primitive.
- FND-005: no QFT/particle mechanism result.
- FND-006 and EQN-001–006: any candidate model must declare the incumbent assumption, alternative equation, dimensional/symmetry/conservation/causality checks, limits, falsifier, held-out prediction and independent validation.
- EQN-001–006 remain governed hypotheses; this batch does not generate or promote a new physical equation.

## INV-029–035 and permanent-root preservation

- INV-029: no physical Data-Center-to-One-Phone compression or lifecycle-cost milestone.
- INV-030: no elemental transmutation or Pangola-carbon functional substitution.
- INV-031: no accepted-liquid bio-oil/fuel mass balance or commercial-cost evidence.
- INV-032: no reliable net delivered fusion electricity or lifecycle-cost evidence.
- INV-033: no realized principal, interest or WACC change; project-rate claims remain separate.
- INV-034/035: foundational alternatives remain open but evidence-gated.
- INV-025/026/027 and all root directives 00, 00A and 01–06 remain preserved. The Kanusanan Pongpanna Model, multilingual public plan links and strategic AI-agent/funding references are unchanged.

## GitHub sync and next gate

This work is on a feature branch until reviewed and merged; it is not yet canonical `main`. Exact source commit SHAs and PR status must be mapped in the pending-main record. The next highest-value gate remains exact-head CI for the signed-Max-Cut certificate runner, followed by the two-route offline FND003-NH-EP-001 reproduction. No paid QPU execution is authorized.
