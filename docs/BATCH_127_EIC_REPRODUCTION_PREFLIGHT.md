# Batch 127 — equation-stability known-law fixture and external EIC provenance gate

**Date:** 2026-10-29  
**Starting main SHA:** 268a423add2a5960aa4b7efa9711c1311aeaa318  
**Primary owner:** Lane A — equation diagnostic and known-law fixture  
**Integration/evidence owner:** Lane F  
**Source-provenance/publication owner:** Lane H  
**Evidence class:** SOFTWARE DIAGNOSTIC + SYNTHETIC TESTS + SOURCE-PROVENANCE AUDIT; MODEL_ONLY

## Starting-state and CI audit

Started from the newest main commit, Batch 126. Re-read PROJECT_CHARTER.md, VERSION_INVARIANTS.md, GOALS.md, README.md, docs/RESEARCH_OPERATING_SYSTEM.md, docs/OPEN_FRONTIER_RESEARCH_DIRECTIVE.md, docs/KANUSANAN_PONGPANNA_MODEL.md, STRATEGIC_PLAN_REFERENCES.md, root directives 00/00A/01–06, Batch 126, focused equation-stability and matched-robustness gaps, RESEARCH_GAPS.md, WORKLOG.md, the lane scoreboard, integration index and current Actions.

On the starting SHA, the Prototype/Invariant workflow completed successfully at https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40858117234 and the cold-start handoff audit passed at https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40858117248. The new commit's exact-head Actions are the acceptance gate.

## Literature surveillance and source accounting

The current public search revisited symbolic regression, equation discovery, AI theorem discovery, physics-informed PDEs, experimental design, quantum thermodynamic bounds, biomass conversion and fusion cost accounting. GOLLuM and constraint-aware symbolic regression were already indexed in the 2026-10-25 literature watch and Batch 057; EIC and symbolic-regression search complexity were already covered by Batch 126; CoSR status, LegoSR/RISR, TINNs, theorem-discovery and thermodynamic sources were already indexed. No new-to-repository material primary source was identified, so no duplicate literature-watch article is created.

A source-provenance audit of the EIC implementation at https://github.com/tsinghua-fib-lab/EIC found the latest main/tree commit SHA 6e3abfcc308f2c71292abfa683ffb404412d022a (dated 2026-03-31), repository metadata marked it as a fork, and the API reported no repository license. No root-level LICENSE/COPYING file was present; the discovered license files were scoped to nested data/PMLB and third-party subprojects. The README also documents a correction to earlier PySR noise-call and CPU-time comparisons. This is a reproducibility and reuse blocker, not evidence of misconduct or a result about physics. UQPU did not copy, vendor or execute the external EIC code.

## Implementation

Added software/uqpu-prototype/uqpu/equation_stability_benchmark.py and a regression test module. The deterministic fixture compares two algebraically equivalent forms near zero: the stable rationalized expression 1/(sqrt(1+x)+1) and the cancellation-prone expression (sqrt(1+x)-1)/x. It uses an 80-digit Decimal intermediate as a numeric reference and the existing normalized perturbation proxy under declared input/output scales.

The fixture tests whether the UQPU diagnostic detects a known floating-point failure mode. It does not implement EIC, compare symbolic-regression search methods, prove a general stability theorem, or establish a physical law. The full fit-plus-complexity versus EIC versus UQPU-proxy benchmark remains preregistered but not run; the EIC arm remains blocked until code-reuse rights, exact source/data revisions and environment are resolved.

## A–H status

| Lane | This-cycle advance / reviewed status | Evidence class | Next gate |
|---|---|---|---|
| A — quantum programming/workloads/compiler/runtime | Added a known-equivalent-form stability fixture and tests; Priority-1 QUBO/QAOA accepted-output contracts remain in force. | SOFTWARE_DIAGNOSTIC / MODEL_ONLY | Run exact-head CI; then compare fit-plus-complexity and UQPU proxy on frozen grouped known-law cases; add EIC only after rights and source pinning. |
| B — cloud/QPU/provider integration | Provider-neutral routes maintained; no provider adapter or target claim changed. No paid job submitted. | MAINTAINED / NO TARGET EXECUTION | Simulator/dry-run first; later pair quality and price for the same provider and target. |
| C — RAM/VRAM/HBM/storage/state/data movement | Classical output/readout, memory and transfer accounting remain distinct from Hilbert-space dimension. No new memory measurement. | CONTRACT / NO NEW MEASUREMENT | Record state/I/O bytes, peak memory, transfers, reconstruction and host compute per accepted task. |
| D — device/chip/process/fabrication/packaging | Batch 126 molecular spin–photon gate remains external and unreproduced; no device result from this batch. | EXTERNAL LITERATURE / NO REPRODUCTION | Independent device-observable replication and substrate integration gate. |
| E — biomass/materials/bio-oil/fusion/cooling/infrastructure | INV-030 functional substitution, BIO-001 accepted liquid and FUS-001 net electricity remain open; no commercial evidence added. | OPEN_GAPS | Pangola mass/energy/product assay; fusion net-electric and lifecycle-cost account. |
| F — economics/benchmarks/evidence/integration | Added numeric-reference provenance and explicit EIC source-reuse blocker; no cost-per-accepted-result measurement. | SOURCE AUDIT / SOFTWARE DIAGNOSTIC | Equal candidate/time/CPU/memory/precision budgets; report failures, false discoveries and total cost. |
| G — chip-manufacturing equipment/software/factory systems | D/G co-design retained; no process-window, yield or cost-per-good-device evidence. | MAINTAINED / NO FACTORY MEASUREMENT | Link device requirements to repeatability, process window, yield, equipment and packaging cost. |
| H — Kanusanan Pongpan­na Model, strategy/finance/publication | Source-status audit recorded; multilingual master-plan links and strategic AI-agent/funding references preserved. | RESEARCH GOVERNANCE | Resolve source reuse rights and publish only a genuine new source delta; no duplicate article. |

## Foundational and equation-discovery status

FND-001 thermodynamic-gap accounting, FND-002 output-information bounds, FND-003 matched control versus quantum-speed-limit measurement, FND-004 alternative physical primitives and FND-005 QFT/particle mechanism scans receive no new physical measurement or theorem in this batch. FND-006 advances at the synthetic diagnostic level only. EQN-001–006 remain active and evidence-gated; a numerical stability score supplements, but does not replace, dimensional/symmetry/conservation/causality checks, limiting cases, held-out prediction, counterexample search, proof/simulation, discriminating experiment and independent replication.

## INV-029 through INV-035 and mission boundary

INV-029 remains a long-horizon physical-compression goal; no phone-class service, energy, form-factor or lifecycle-cost contract is closed. INV-030 has no Pangola-carbon functional-substitution result and no elemental transmutation claim. INV-031 has no accepted saleable-liquid/biofuel cost result. INV-032 has no net reliable delivered fusion-electricity result. INV-033 has no measured financed-principal/interest-per-milestone or WACC reduction. INV-034 remains the permanent foundational agenda. INV-035 is strengthened only by a testable numerical diagnostic and stricter source provenance; no candidate is promoted to a physical law. INV-025/026/027 remain preserved.

The six-language Thai/English/Chinese/Japanese/Korean/German master-plan references, strategic AI-agent/funding context, root directives and Kanusanan Pongpan­na Model are unchanged. No real-QPU advantage, material substitution, commercial bio-oil, commercial fusion, reduced WACC, 100x/100,000,000x advantage or Data-Center-to-One-Phone closure is claimed. No paid QPU job was authorized or submitted.

## Sync and next gate

This batch adds a focused Lane A contract, source audit, integration record and regression tests. README, integration index, living gap register, worklog and scoreboard are updated together; no append-only sync debt is intentionally left by this batch. Next highest-value gate: exact-head CI; then freeze grouped known-law fixtures and compare fit-plus-complexity against the UQPU perturbation proxy under equal budgets. The EIC method arm remains blocked until code-reuse rights and source/data/environment provenance are resolved.

Research-Sync: main
