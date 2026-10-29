# Batch 128 — accuracy-plus-stability acceptance gate for equation candidates

**Date:** 2026-10-29  
**Starting main SHA:** 17e3c8ff96d4dc7a95001e39186387cf8ccca28d  
**Primary owner:** Lane A — equation-candidate evaluation  
**Evidence/integration owner:** Lane F  
**Literature/provenance owner:** Lane H  
**Evidence class:** SOFTWARE_DIAGNOSTIC + SYNTHETIC REGRESSION TESTS; MODEL_ONLY

## Starting-state and CI audit

Started from the newest committed `main` state (Batch 127). Re-read the charter, version invariants, goals, README, research operating system, open-frontier directive, Kanusanan Pongpanna Model, strategic references, root directives 00/00A/01–06, current gaps, work log, latest Batch/gap records, lane scoreboard and Actions state. The Batch 127 head had successful Prototype/Invariant workflow [#2008](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40861306475) and Cold-Start Handoff Audit [#1271](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40861306385).

## Fresh literature surveillance

Fresh public searches covered symbolic regression and structural stability, neural-symbolic equation discovery, AI theorem discovery/formalization, physics-informed/time-dependent PDE models, automated experiment design, quantum-speed/thermodynamic bounds, material discovery, biomass conversion and fusion cost accounting. No material primary source new to this repository was identified in this cycle. The CoSR/AI-Newton progressive-discovery papers, EIC and search-complexity work, TINNs, the 28 October 2026 Nature single-molecule spin–photon paper, and current AI-formalization sources are already indexed in the latest literature watches. They remain external evidence, not UQPU reproduction.

## Implementation

Batch 127's preregistered comparison already requires both held-out error and stability metrics, but it did not yet provide one fail-closed candidate-level acceptance function. A stability-only score can wrongly favor a constant or otherwise uninformative candidate: zero output change under perturbation is not evidence of accuracy. Lane A therefore adds `equation_candidate_gate.py`, which combines:
- normalized held-out RMS error using predeclared positive output scales;
- a separately measured perturbation-amplification metric and predeclared threshold;
- hard rejection for constraint violations and numerical failures;
- strict rejection of non-finite values, booleans, invalid counts, and invalid thresholds;
- explicit synthetic-only evidence labels and a no-physical-claim boundary.

Six regression tests include the decisive counterexample: a constant candidate with zero perturbation amplification is rejected for poor accuracy. This is a software-level diagnostic, not a symbolic-regression competition, reproduction of EIC, proof of physical validity, or a new equation of nature. The external EIC method arm remains blocked because its repository has no top-level license declaration; no EIC code was copied or run.

## A–H status

| Lane | Status this cycle | Next evidence gate |
|---|---|---|
| A — programming/workloads/compiler/runtime | Added fail-closed candidate acceptance gate and counterexample tests; Priority-1 QUBO/QAOA accepted-output path remains primary. | Exact-head CI; then frozen grouped known-law comparison under equal budgets. |
| B — cloud/QPU/provider integration | Provider-neutral routes maintained; no target execution and no paid job. | Simulator/dry-run, then target-specific quality, usage and cost only with credentials, bounded budget and explicit consent. |
| C — state/memory/storage/data movement | Classical output, state, memory, transfer and reconstruction remain distinct from Hilbert-space dimension. | Measure memory, I/O, transfer, reconstruction and host compute in accepted-task contracts. |
| D — device/chip/fabrication/packaging | Molecular spin–photon interface remains a peer-reviewed external result, not UQPU device replication. | Independently reproduce observables and establish substrate/integration constraints. |
| E — biomass/materials/energy/cooling | Pangola functional substitution, BIO-001 accepted liquid and FUS-001 net electricity remain open. | Function-specific materials tests; closed mass/energy/product balance; reliable net delivered electricity and lifecycle cost. |
| F — economics/benchmarks/evidence/integration | Candidate gate now forbids stability-only or fit-only acceptance; resource/evidence boundaries are explicit. | Equal candidate/time/CPU/memory/precision budgets and cost per accepted candidate. |
| G — manufacturing equipment/factory systems | D/G co-design retained; no process-window, yield or cost-per-good-device data added. | Translate a replicated device requirement into process window, repeatability, yield and capital cost. |
| H — strategy/finance/publication | Literature deduplicated; strategic model, funding/agent context and multilingual public links preserved. | Publish only genuine source deltas; keep source provenance and staged capital gates. |

All 28 unordered A–H interfaces were reviewed. INV-034/035 remain upstream cross-cutting layers feeding all lanes.

## Foundational and mission invariants

- **FND-001–005:** no new physical measurement or changed lower bound; thermodynamic accounting, output-information limits, matched control/QSL measurement, alternative primitives and QFT/particle scans remain evidence-gated.
- **FND-006:** candidate evaluation now rejects a low-sensitivity but inaccurate synthetic candidate. Formal proof, semantic physics validation, held-out prediction, counterexample search and independent replication remain separate gates.
- **EQN-001–006:** literature surveillance, matched symbolic-regression evaluation, constraint-aware generation, counterexample/falsification, new-physics escalation and equation-to-technology traceability remain the pipeline. No AI-generated equation is promoted to a physical law.
- **INV-029:** phone-class physical compression remains a mission target requiring useful-service, energy, external-infrastructure and lifecycle-cost accounting; a remote terminal is insufficient.
- **INV-030:** Pangola carbon is pursued for functional substitution/minimization/recovery/hybridization/redesign; no elemental transmutation is claimed.
- **INV-031:** no accepted saleable-liquid/fuel cost result.
- **INV-032:** no reliable net delivered fusion-electricity result.
- **INV-033:** no measured reduction in financed principal/interest per milestone or WACC.
- **INV-034/035:** the foundational and AI-assisted equation-discovery programs advance only in evaluation methodology; present physics remains binding for engineering claims.
- **INV-025/026/027 and INV-036/037:** preserved. The 100× and 100,000,000× targets remain unproven goals.

## Synchronization and next gate

README, integration hub, eight-lane scoreboard, living research-gap register and work log are updated in this same commit alongside the helper, tests, focused gap and machine-readable integration record. No append-only sync debt is intentionally left. Exact-head Actions for this new commit are the acceptance gate; no local full-suite result is claimed. No paid QPU job was submitted.

**Next highest-value gate:** exact-head CI, followed by a frozen grouped known-law comparison with family-disjoint holdouts, null/constant and ill-conditioned controls, at least 30 preregistered seeds, identical candidate/time/CPU/memory/precision budgets, retained failed candidates, and independent replication. Keep EIC disabled until source-reuse rights and environment/data provenance are resolved.

Research-Sync: main
