# INT-20261024-006 — Gaussian quantum-repeater no-go scope

**Date:** 2026-10-24  
**Primary owner:** Lane H — literature and strategic synthesis  
**Integration owners:** Lane B (provider/network contract), Lane C (photonic interconnect/data movement), Lane F (capacity/economics boundary)  
**Canonical main base:** c7b5958af58fad04a101ef5c6abf6a29293c867e  
**Source:** Ahmed and Smith, PRL 137, 170804, published 2026-10-23, DOI 10.1103/5cyh-2mqf  
**Status:** LITERATURE SCOPE REVIEW; FULL-TEXT ASSUMPTION AUDIT OPEN  
**Evidence class:** LITERATURE_ONLY; no project evidence promotion

## Integration decision

Do not assume that a Gaussian-only repeater improves quantum/private communication capacity over direct transmission for the pure-loss bosonic channel and operation class covered by the theorem. Do not generalize the no-go to all repeaters or all photonic computation. The source's full text must be reviewed before translating theorem details into an implementation-specific guard.

The theorem changes the constraint ledger, not the physics model or any measured UQPU result. A candidate architecture that claims an exception must identify the exact changed assumption and derive a distinct, testable capacity/service prediction.

## A–H status

| Lane | Status in this cycle | Next gate |
|---|---|---|
| A — quantum programming/workloads/compiler/runtime | No compiler change; offline experiment-plan schema guard remains in place. | If distributed workloads are evaluated, bind accepted output and channel assumptions to the workload contract. |
| B — cloud/QPU/provider integration | Gaussian-repeater scope reviewed; no provider contacted. | Read-only capability/architecture records must not imply repeater capacity gain without model evidence. |
| C — memory/state/storage/data movement | Network capacity is kept separate from classical readable bytes and reconstruction. | Add matched direct-vs-repeater capacity/resource accounting only after full assumption review. |
| D — device/chip/process/fabrication | No new device result. | No photonic device requirement without a changed-model observable and target evidence. |
| E — biomass/materials/bio-oil/fusion/cooling | No new material, fuel, net-electricity or cooling evidence. | BIO-001 and FUS-001 remain on their own accepted-product/net-electricity gates. |
| F — economics/evidence/integration | Capacity theorem is not a cost measurement. | Measure latency, loss/retry, host/control/data movement, energy and cost per accepted useful task. |
| G — manufacturing equipment/software/factory | No process-window or yield result. | D/G co-design remains conditional on measured device requirements. |
| H — strategy/finance/publication | Dated peer-reviewed no-go watch recorded with full-text limitation. | Complete theorem premise audit and retain counterexamples/negative results. |

## Foundational mapping

- **FND-001:** no physical energy/duration measurement added.
- **FND-002:** channel-capacity bounds inform information flow, not readable RAM/storage equivalence.
- **FND-003:** no matched control/QSL experiment added.
- **FND-004:** no new physical primitive; one operation/channel class is constrained.
- **FND-005:** no QFT/particle mechanism or device consequence.
- **FND-006:** mathematics-first work remains allowed, but theorem premises and model adequacy must be separated.
- **EQN-001:** new source/date and evidence class recorded.
- **EQN-002/003:** no symbolic-regression result added; alternative architectures need typed assumptions and deterministic checks.
- **EQN-004:** counterexamples and changed-assumption controls remain mandatory.
- **EQN-005:** formal no-go theorem is model-scoped; map exact premises before applying it.
- **EQN-006:** no system or economic consequence is promoted.

## INV-029 through INV-035

INV-029 remains a physical Data-Center-to-One-Phone target with external networking and infrastructure counted; this theorem supplies no mission closure. INV-030 has no material-substitution result. INV-031 has no saleable-liquid evidence. INV-032 has no net reliable delivered-electricity evidence. INV-033 has no principal/interest/WACC measurement. INV-034 preserves the broad mathematics/physics frontier. INV-035 requires explicit assumptions, discriminating predictions and independent validation; the no-go cannot be bypassed by saying future physics may change.

The eight permanent root directives, Kanusanan Pongpanna Model, STRATEGIC_PLAN_REFERENCES.md and Thai/English/Chinese/Japanese/Korean/German public master-plan links remain preserved. Lane I remains a separate repository extension and does not replace A–H.

## Next gate

Complete a full-text assumption audit, then create QNET-GAUSS-001 as a small model-scoped consistency test. Do not claim a repeater advantage unless the model changes explicitly and the resulting observable/capacity prediction is independently checked. No provider job is authorized.
