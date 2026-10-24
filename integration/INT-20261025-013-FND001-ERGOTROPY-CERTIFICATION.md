# Integration handoff — INT-20261025-013: FND-001 finite-information ergotropy certification

**Date:** 2026-10-25 (Asia/Bangkok)  
**Primary owner:** Lane F — evidence, benchmarks, energy economics and integration  
**Priority lane:** A — quantum programming, workloads, compiler/runtime  
**Status:** PROPOSED / PULL REQUEST REVIEW REQUIRED  
**Canonical main base:** 6af8ce896368ed993fe2b8278afa6082e1ecc916  
**Source branch:** research/2026-10-25-fnd001-ergotropy-certification  
**Initial source commit:** 5664aaef15ede2335b61bde6b65d3e67fe76ae18  
**Machine-readable contract:** integration/INT-20261025-013-FND001-ERGOTROPY-CERTIFICATION.json  
**Primary Lane F work item:** research_lanes/F_economics_benchmarks_evidence_integration/FND-ERG-001_2026-10-25.md  
**Literature artifact:** docs/literature_watch/2026-10-25-fnd001-ergotropy-certification.md  
**Evidence class:** LITERATURE_ONLY + preregistered test protocol  
**Project evidence promotion:** none

## Objective and method

Add a dated, source-checked literature watch for the peer-reviewed 2026-09-21 PRL paper “Certifying ergotropy under partial information” and define FND-ERG-001 as a falsifiable follow-up. The paper's SDP certificate bounds extractable work from partial state measurements with finite-shot confidence regions. The proposed UQPU follow-up explicitly separates that state-resource certificate from metered joules per accepted computing task and from any ideal physical lower bound.

The source article records the paper's assumptions, experimental scope, finite-statistics relation, limitations, independent-reference plan, counterexamples, and evidence boundaries. No source code, equation-discovery candidate, hardware result, energy measurement or economic claim was changed or promoted by this handoff.

## Current canonical baseline and gaps

- Latest observed main SHA before this branch: 6af8ce896368ed993fe2b8278afa6082e1ecc916.
- Latest canonical computing control remains Batch 056: a 2x2 Hermitian-contraction / 4x4 one-ancilla QSVT simulation with degree 81, 81 signal queries and 82 phase rotations. Its residuals passed predeclared numerical tolerances, but it is SIMULATION evidence only; no provider job, shots, native target circuit, measured energy or accepted-task economics resulted.
- The current main-head combined-status endpoint returned no status checks for SHA 6af8ce896368ed993fe2b8278afa6082e1ecc916. The previously recorded successful cold-start check was on older SHA c7b5958af58fad04a101ef5c6abf6a29293c867e; a current-main full-suite result was not observed in the latest reconciliation. Do not label current main CI green from those older runs.
- RG-034 remains execution-disabled pending explicit authorization and accounting. No credentials, bounded budget or explicit approval were supplied for a paid QPU job, and none was submitted.
- Existing open QSP/QSVT and FND-001 related PRs remain subject to their own review/CI gates. This literature lead does not replace or duplicate their code changes.

## Eight-lane status at this run

| Lane | Status at canonical baseline | Contribution in this handoff / next gate |
|---|---|---|
| A — quantum programming, workloads, compiler/runtime | PRIORITY #1; Batch 056 simulation control; QSP/QSVT feasibility gate not yet merged | Preserve the existing QOS-QSVT-FEAS-001 gate. Add only a future measurement-certificate interface: observable set, shots, confidence delta, solver tolerance and exact-reference result. Do not substitute ergotropy for accepted-output quality or task-energy measurement. |
| B — cloud/QPU/provider integration | DRY_RUN_ONLY / no new provider call | Keep provider-neutral path and target metadata. A hardware replication would require an authorized target, bounded budget, job IDs, billable usage and exact target-matched results. |
| C — RAM/VRAM/HBM/storage/state/data movement | No subsystem-equivalence evidence | Count measurement and classical post-processing overhead; never equate Hilbert-space size with readable classical memory/storage. |
| D — quantum/photonic/semiconductor device/chip/process/fabrication/packaging | No new device/process evidence | If later implemented, capture native gates, depth, readout, control, calibration and device constraints. |
| E — biomass/materials/bio-oil/fusion/cooling/infrastructure | BIO-001 and FUS-001 remain blocked on qualified input and end-to-end evidence | No Pangola, material substitution, saleable liquid fuel, net fusion electricity, cooling or infrastructure measurement. |
| F — economics, benchmarks, evidence and integration | Primary owner for this contract; FND-001 is the receiving workstream | Keep ergotropy certificate, metered task energy, ideal lower bound and any gap as distinct fields unless units and system boundaries are compatible. Retain negative/zero-bound cases. |
| G — quantum-chip manufacturing equipment/software/factory systems | No manufacturing or yield evidence | Continue D/G co-design; no equipment, process-window, throughput, yield or factory-cost claim. |
| H — Kanusanan Pongpanna Model strategy, finance, future industries and publication | Literature publication only | Preserve the strategic master document and Thai/English/Chinese/Japanese/Korean/German public master-plan links; no funding, principal, interest, WACC or future-industry claim. |

INV-034 and INV-035 remain upstream cross-cutting layers for every lane. The repository also contains an experimental Lane I program; this A–H handoff neither reclassifies nor deletes it.

## Foundational and equation-discovery disposition

- **FND-001:** add FND-ERG-001 as a proposed finite-statistics state-resource certificate study. Stage 0 must reproduce the public paper's two-SDP method and known-Hamiltonian assumption; Stage 1 must compare the certificate against exact ergotropy for frozen small systems and test declared confidence coverage; Stage 2 must retain adversarial failures; Stage 3 must separately meter total system energy for an identical accepted task.
- **FND-002:** unchanged. Output-information lower bounds remain independent of ergotropy and classical memory equivalence.
- **FND-003:** unchanged. No matched control-vs-quantum-speed-limit measurement was made.
- **FND-004:** unchanged. No alternative physical primitive was experimentally established.
- **FND-005:** unchanged. No new QFT/elementary-particle mechanism or device consequence was validated.
- **FND-006:** strengthened procedurally by a new candidate falsifier and an exact-reference/independent-replication requirement; no new mathematical theorem is claimed.
- **EQN-001:** new literature-watch entry.
- **EQN-002:** no benchmark execution; future comparisons must use frozen train/validation/held-out partitions and record false discoveries.
- **EQN-003:** no generator change.
- **EQN-004:** add lower-bound violations, confidence-coverage failure, calibration/model mismatch and non-monotonicity as explicit counterexamples.
- **EQN-005:** not triggered; no established physics is challenged.
- **EQN-006:** preserve the trace from paper claim -> certificate assumptions -> exact reference -> experiment -> system consequence -> economics.

## Invariant impact — INV-029 through INV-035

- **INV-029:** no Data-Center-to-One-Phone achievement; this only tightens one possible energy-accounting method.
- **INV-030:** no biomass-carbon or critical-material functional-substitution evidence.
- **INV-031:** no accepted bio-oil/biofuel yield, quality, upgrading or cost evidence.
- **INV-032:** no net reliable delivered fusion-electricity evidence.
- **INV-033:** no reduction in financed principal, capital lock-up, interest expense, risk premium or WACC measured.
- **INV-034:** adds a falsifiable foundational thermodynamics research path while retaining established physical limits.
- **INV-035:** no AI-generated equation is declared a law; formal optimization, numerical fit, extractable-work certification and physical truth remain distinct.

INV-025/026/027 are preserved: no 100,000,000x or universal subsystem-replacement target is promoted.

## Literature and cross-lane integration edges

- APS/PRL paper -> FND-001 finite-shot state-resource certificate -> Lane F evidence ledger.
- Certificate observables/shots -> Lane A workload/measurement accounting and Lane B target provenance.
- Classical solver/post-processing and output reconstruction -> Lane C I/O accounting and Lane F total cost per accepted useful task.
- Any later device experiment -> Lane D/G target-native resource and process constraints.
- Facility energy and cooling -> Lane E system boundary, independently metered rather than inferred from ergotropy.
- Published and replicated result -> Lane H dissemination, preserving strategic-plan provenance.

No cross-lane edge changes an evidence class automatically. Literature and MODEL_ONLY outputs cannot be promoted to hardware, material, fuel, electricity or economic evidence by documentation alone.

## Validation, sync and next gate

- This is a documentation/protocol-only change. No code tests are claimed as run or passed by this branch.
- Hosted CI on the exact pull-request head is required before accepting the record; inspect cold-start and test workflows independently.
- No paid QPU job, purchase, fabrication action, material/fuel experiment or funding action was performed or authorized.
- Source branch is not canonical main. Do not claim synchronization until reviewed and merged. A separate pending-main sync PR must record the complete source head SHA, changed files, evidence class, CI state, blockers and the source-PR-to-main mapping when available.
- The eight high-visibility root directives 00–06, docs/KANUSANAN_PONGPANNA_MODEL.md, STRATEGIC_PLAN_REFERENCES.md and all six public master-plan language editions remain unmodified.

**Next highest-value gate:** keep Lane A's QSP/QSVT feasibility test as Priority #1. In parallel, independently reproduce FND-ERG-001 Stage 0 and freeze exact small-state fixtures, solver tolerances, shot budgets and coverage criteria before any implementation or provider use.