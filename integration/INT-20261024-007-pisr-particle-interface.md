# INT-20261024-007 — physics-informed symbolic regression and generalization boundary

**Date:** 2026-10-24  
**Primary owner:** Lane H — literature and strategic synthesis  
**Cross-lane owners:** Lane A (equation-discovery contract), Lane D (constitutive/device modeling), Lane E (materials/energy), Lane F (evidence/economics)  
**Canonical main base:** c7b5958af58fad04a101ef5c6abf6a29293c867e  
**Source:** Lazebnik, Mortenfeld and Liberzon, *Machine Learning: Science and Technology* 7, 055004 (2026-09-08), DOI 10.1088/2632-2153/ae9c8b  
**Status:** LITERATURE REVIEW; SYNTHETIC AUDIT PROPOSED; SOURCE REPRODUCTION DATA-BLOCKED  
**Evidence class:** LITERATURE_ONLY + PROTOCOL_PROPOSAL; no project evidence promotion

## Integration decision

Use the paper as a method-design reference for physics-informed symbolic regression, not as a transferable law. Its delayed damped oscillatory closure was selected from a constrained operator library using experimental particle trajectories, repeated searches and ablations. The authors report 17/20 structural recoveries under the full configuration, but the model is limited to its measured fluid/interface regime, and the underlying commercially sensitive data are not public.

The main UQPU delta is to keep four scores separate: (1) equation-family recovery, (2) held-out predictive error, (3) physical-constraint compliance, and (4) total resource cost. Good fit alone cannot establish identifiability, mechanism or a new law.

## PISR-AUDIT-001 interface

**Inputs:** frozen baseline and candidate generator; equation/data/split/noise/operator/constraint/scoring hashes; held-out trajectory and parameter-group labels; repeated seeds; explicit resource caps.

**Required negative controls:** no-trigonometric, no-exponential and no-delay operator ablations; shuffled/no-signal data; intentionally misspecified simulator; failed and non-identifiable candidates.

**Acceptance:** improvement over the baseline on untouched held-out groups; stable equation-family recovery across seeds; no comparable discovery rate on shuffled data; all dimensional/boundary/boundedness/dissipation checks pass; and independent replay reproduces metrics under the declared budget.

**Falsifiers:** held-out failure, unstable family, constraint violation, false-discovery rate indistinguishable from the no-signal control, or non-reproducible metrics. All failures must be retained.

**Source reproduction:** DATA_BLOCKED until the authors provide the commercially sensitive dataset and sufficient artifacts. Synthetic results must never be labelled as a reproduction of the published study.

## A–H status and next gate

| Lane | Cycle consequence | Next gate |
|---|---|---|
| A — programming/workloads/compiler/runtime | Equation-discovery software contract informed; no code or performance change claimed in this record. | Implement a frozen synthetic PISR audit with whole-trajectory and parameter-group splits. |
| B — cloud/QPU/provider integration | No provider contact or QPU job. | Keep the first benchmark offline and provider-neutral. |
| C — memory/state/storage/data movement | No memory replacement evidence. | Record dataset, intermediate-state, transfer and reconstruction bytes in the benchmark. |
| D — device/chip/process/fabrication | No device or fabrication result. | Require a validated mechanism before device requirements are inferred. |
| E — materials/bio-oil/fusion/cooling | Method is potentially reusable but no domain result transfers from fluid dynamics. | Use separate qualified Pangola/material data or net-electric fusion data only. |
| F — economics/evidence/integration | Search and replay resource accounting is explicitly part of acceptance. | Measure cost per accepted held-out discrimination; energy stays null unless measured. |
| G — manufacturing equipment/software/factory | No manufacturing consequence. | Remain downstream of measured device/process requirements. |
| H — strategy/finance/publication | Dated source and limitations recorded; data-access gap remains explicit. | Request data/artifacts, then independently reproduce or retain DATA_BLOCKED status. |

## Foundational mapping

- **FND-001:** no thermodynamic-gap or physical-energy measurement.
- **FND-002:** no new output-information lower bound; dataset and classical output bytes remain explicit.
- **FND-003:** no matched control-versus-quantum-speed-limit experiment.
- **FND-004:** no new physical primitive.
- **FND-005:** no QFT/particle mechanism.
- **FND-006:** supports constrained mathematics-first model generation, not physical-law promotion.
- **EQN-001:** source/date and evidence class recorded.
- **EQN-002:** proposes a reproducible equation-family/held-out benchmark.
- **EQN-003:** requires dimensional, boundary and boundedness constraints before acceptance.
- **EQN-004:** adds seed/operator ablations, shuffled-data controls and blind parameter-group tests.
- **EQN-005:** no new-physics escalation; incumbent fluid assumptions remain binding until a discriminating observable and independent measurement exist.
- **EQN-006:** no device, system or economic consequence is promoted.

## INV-029 through INV-035

INV-029 remains a physical-compression goal, not a remote-terminal claim. INV-030 has no Pangola-carbon substitution result. INV-031 has no saleable-liquid fuel evidence. INV-032 has no net reliable delivered-electricity evidence. INV-033 has no financing/interest/WACC result. INV-034 remains open to mathematical alternatives while present physical limits bind engineering. INV-035 permits equation hypotheses but requires held-out prediction, falsification and independent validation.

The root mission directives, KANUSANAN_PONGPANNA_MODEL.md, STRATEGIC_PLAN_REFERENCES.md and Thai/English/Chinese/Japanese/Korean/German public master-plan links remain unchanged. Lane I remains an auxiliary repository extension and does not replace A–H.

## Next highest-value gate

Implement the synthetic PISR-AUDIT-001 fixture and deterministic scorer, then run its negative controls under exact-head CI. Do not attempt source-paper reproduction until the data-access blocker is resolved. No provider, instrument, material or paid execution is authorized.
