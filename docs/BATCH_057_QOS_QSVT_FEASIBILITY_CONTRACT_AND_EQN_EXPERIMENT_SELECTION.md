# Eight-Lane Research Batch 057 — QSVT feasibility preregistration and uncertainty-aware experiment design

**Date:** 2026-10-25  
**Canonical starting main:** 6af8ce896368ed993fe2b8278afa6082e1ecc916  
**Starting CI:** latest main Actions observed successful for the QSP/QSVT literature-watch integration; latest listed main runs completed successfully. New commit CI is pending until Actions executes.  
**Primary owner:** Lane A — quantum programming/compiler/runtime  
**Integration/evidence owner:** Lane F  
**Publication owner:** Lane H  
**Evidence class:** software contract/tests + LITERATURE_ONLY + MODEL_ONLY where explicitly stated

## Highest-value work selected

The latest main state contains Batch 056, a bounded 2×2 Hermitian-contraction QSVT matrix fixture. Its recorded residuals are within predeclared tolerances, but it remains a dense numerical convention check with 81 signal queries and 82 phase rotations; it has no provider jobs, target-gate decomposition, energy measurement or accepted workload. The next documented gate is QOS-QSVT-FEAS-001: decide feasibility before paying the cost of phase synthesis and compilation, while keeping univariate regression behavior unchanged.

This batch adds a fail-closed preregistration/provenance contract in:
- software/uqpu-prototype/uqpu/qos_qsvt_feasibility_contract.py
- software/uqpu-prototype/tests/test_qos_qsvt_feasibility_contract.py

The contract validates fixture class, exact statement hash, theorem scope, expected classification, and the distinct metadata required for univariate QSP, multivariate QSP and unknown-channel QSVT. A solver/tool exception is classified as TOOL_BLOCKED, never as mathematical infeasibility. A theorem-labelled result is only READY_FOR_INDEPENDENT_AUDIT; it cannot skip synthesis or support a hardware/economic claim. The contract is not a QSP/M-QSP feasibility algorithm and does not independently verify the proof/certificate contents.

## Literature surveillance delta

A new dated watch records two primary literature sources not found in the repository's existing text search:
- GOLLuM uncertainty-calibrated LLM-assisted experimental optimization, Nature Machine Intelligence, published 2026-08-28.
- ASP-assisted symbolic regression for 3D laminar channel flow, Scientific Reports, published 2026-04-30.

The genuine project implication is to separate candidate generation, physical/domain constraint filtering, calibrated experiment selection, held-out evaluation and counterexample search. Both results are methods evidence, not a UQPU replication, new physical law, Pangola/fusion result, or commercial economics evidence. The GOLLuM article's Gaussian-process scaling and domain/representation limitations are retained in the watch. The existing 2026-10-25 QSP/QSVT, QFI and formal-proof watches remain unchanged.

New publication: docs/literature_watch/2026-10-25-uncertainty-calibrated-experiment-selection-and-constraint-aware-equation-discovery.md

## A–H status

- **A — Quantum programming/workloads/compiler/runtime (Priority #1):** added a preregistration/provenance contract and unit tests for the next QSP/QSVT feasibility gate. The actual published M-QSP decision algorithm, independently sourced fixtures, and provider-neutral lowering remain open.
- **B — Cloud/QPU/provider integration:** no paid or free target job submitted; no credentials used. IBM Quantum, Braket, Azure/provider adapters, IonQ, Rigetti, D-Wave, IQM, Quantinuum, Pasqal, QuEra, Quandela, OQC and emerging providers remain in the provider-neutral roadmap.
- **C — RAM/VRAM/HBM/storage/state/data movement:** Batch-056 state-space and resource ledger remains a small mathematical fixture, not readable classical memory/storage. A target-aware output/I/O/transfer/memory contract is still required.
- **D — Quantum/photonic/semiconductor device/process/packaging:** no device or fabrication result. Keep physical interface, materials, lifetime and process-window evidence distinct from algorithmic feasibility.
- **E — Biomass/materials/bio-oil/fusion/cooling/infrastructure:** Pangola carbon functional substitution, BIO-001 accepted-liquid mass/energy/cost closure, and FUS-001 net-electric cost envelope remain evidence gaps. No transmutation, commercial fuel, or cheap-fusion claim.
- **F — Economics/benchmarks/evidence/energy/finance/integration:** added explicit metadata and independent-audit boundary; no measured accepted-task cost, plant TEA, financed-principal saving, interest saving or WACC reduction.
- **G — Quantum-chip manufacturing equipment/software/factory systems:** no fab equipment claim; D/G co-design remains mandatory for process-window, yield, lifetime, equipment and capital-intensity evidence.
- **H — Kanusanan Pongpanna Model/strategy/finance/publication:** added the dated literature watch and this batch. Strategic plan, AI-agent/funding references, and Thai/English/Chinese/Japanese/Korean/German public master-plan links remain preserved.

## Foundational and equation-discovery progress

FND-001–006 remain active and evidence-gated:
- FND-001 thermodynamic-gap accounting: no new matched control-versus-quantum measurement.
- FND-002 output-information lower bounds: retain the distinction between readable output and Hilbert-space dimension.
- FND-003 control time versus quantum speed limit: no new physical-duration or control-energy data.
- FND-004 alternative physical primitives: no validated new primitive.
- FND-005 QFT/elementary-particle mechanism scans: no new discriminating experimental anomaly identified in this cycle.
- FND-006 mathematics-first invention: improved operational ordering from generator → constraints → uncertainty-aware experiment choice → held-out/generalization → counterexample → proof/simulation → experiment → replication → system consequence → economics.

EQN-001–006 remain in force. The new literature supports EQN-003 candidate generation/constraints and EQN-004 false-discovery/counterexample accounting; it does not promote an AI-generated equation. Current physical laws and known no-go results remain binding for engineering claims.

## Permanent invariant contribution

- **INV-029:** no change to Data-Center-to-One-Phone success criteria; phone-as-remote-terminal remains insufficient. No physical compression evidence.
- **INV-030:** constrained experiment selection may help prioritize carbon functional-substitution tests; elemental transmutation is explicitly excluded.
- **INV-031:** proposes better experiment ranking only after feedstock/product assays and mass/energy closure exist; saleable liquid function and full upgrading cost remain the objective.
- **INV-032:** proposes cost-aware measurement prioritization, not fusion net-electricity evidence.
- **INV-033:** records experiment cost and time-to-evidence as candidate design variables; lower principal may reduce absolute interest at unchanged terms, while WACC/rate effects require separate evidence.
- **INV-034:** adds a testable workflow refinement while preserving thermodynamic, information, speed-limit, conservation, causality and no-cloning constraints.
- **INV-035:** enforces hypothesis generation without declaring AI equations to be laws; every future challenge must include baseline, assumptions, dimensions/symmetries/conservation/causality, limits, falsifier, observable, held-out prediction and independent validation.

INV-025/026/027 remain preserved. The 100× and 100,000,000× targets, universal subsystem replacement, real-QPU advantage, commercial low-cost bio-oil/fusion, lower project WACC and phone-class physical compression remain goals rather than demonstrated outcomes.

## Evidence, negative results and gaps

Positive: a new typed contract can prevent a tool exception or mismatched hash from being mistaken for mathematical infeasibility; test cases cover univariate/multivariate metadata, unknown-channel requirements, hash mismatch, tool errors, incomplete records and no-promotion flags.

Negative / not yet established:
- no M-QSP feasibility theorem implementation;
- no independently sourced feasible/infeasible fixture pair;
- no independent adversary-bound cross-check;
- no provider-neutral lowering or target-aware resource ledger;
- no real-QPU, material, fuel, fusion, energy, financing, or new-physics evidence;
- no exact-commit CI result for this batch until Actions completes.

## Integration and next gate

Shared interfaces are fixture IDs, immutable SHA-256 statement hashes, model-class labels, theorem scope, auditable certificate references, and fail-closed statuses. The next highest-value gate is to implement the published M-QSP decision algorithm from its complete specification, freeze source and fixture hashes, add independent feasible/infeasible controls, and test deterministic replay plus semantically irrelevant input reordering. Keep Batch-056 as the univariate regression control. Unknown-channel QSVT needs its own dimension/delta/oracle-access/diamond-norm/query-bound ledger; do not copy static-matrix fixture resource counts.

Root directives 00, 00A and 01–06; docs/KANUSANAN_PONGPANNA_MODEL.md; STRATEGIC_PLAN_REFERENCES.md; the multilingual master-plan links; and strategic AI-agent/funding references were inspected and preserved without replacement. No paid provider job was submitted.

## Canonical append-only sync debt

This batch is the dated canonical record for the cycle. WORKLOG.md was not rewritten because it is a large append-only history; its cross-reference remains a small sync debt to resolve through a safe append-only update. 00D_NEW_DISCOVERY_ARTICLES.md was intentionally not updated because its permanent gate reserves that index for verified new discoveries, while this new literature watch is LITERATURE_ONLY. README's verified-discovery list was likewise left unchanged. No verified-discovery status is implied.
