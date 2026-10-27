# Batch 087 — thermodynamically favoured molecular computing and independent parity-rank verification

**Date:** 2026-10-28  
**Canonical starting main SHA:** `7734020a3f48cfcd12c1eb198e8ca43dbafc1ca2`  
**Primary owner:** Lane A — quantum programming / workloads / compiler / runtime  
**Cross-lane owners:** C, D, E, F, G and H  
**Evidence:** SOFTWARE_CONTRACT_ONLY + LITERATURE_ONLY; external experiment is not UQPU reproduction  
**Paid QPU job:** no

## Starting state and CI

Started from dynamically resolved main, not remembered batch numbering. Inspected PROJECT_CHARTER, VERSION_INVARIANTS, GOALS, README, Research Operating System, open-frontier directive, Kanusanan Pongpanna Model, strategic references, root directives 00/00A/01–06, Batches 084–086, focused gaps, equation/fundamental-limit helpers, parity encoding, QEC interval contract, lane policies, main-sync policy and Actions. Newest prior batch: 086.

At `7734020a3f48cfcd12c1eb198e8ca43dbafc1ca2`, prototype/invariant workflow passed 16/16 jobs (https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40575874945) and cold-start audit passed (https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40575874829). These validate starting main only; this source branch needs exact-head CI.

Root directives 00/00A/01–06, INV-025–035, the Kanusanan Pongpanna Model, strategic AI-agent/funding context and Thai/English/Chinese/Japanese/Korean/German plan links remain preserved. INV-036/037 are untouched. No paid QPU job or hazardous physical test ran.

## Lane A — independent graph-parity rank cross-check

Added a test-only independent GF(2) row-reduction oracle for the graph incidence matrix. The exhaustive fixture enumerates all simple graphs on 1–4 vertices (75 graph masks), checks `cycle_rank = |E| - rank_GF2(incidence)`, and verifies the edge-parity encoding image equals all assignments satisfying the fundamental-cycle constraints. A private local sanity check passed the rank arithmetic for all 75 masks. This does not implement parity-QAOA circuits, signed-Max-Cut objective preservation, provider lowering or quantum advantage.

## FND-001 — accepted-task Landauer-gap diagnostic

Added `landauer_gap_ratio_for_accepted_task` and tests. It compares caller-supplied energy per accepted task with the ideal floor for a positive matched irreversible-erasure count at one declared temperature. It rejects non-positive/non-finite and boolean inputs. It does not measure energy, infer erasures, handle multi-temperature stages, establish attainability or promote a physical law. No SDC energy data were supplied.

## Literature delta — Scaffolded DNA Computer

Stérin et al., “A thermodynamically favoured molecular computer,” *Nature* 657, 646–652 (version of record 2026-09-16), DOI https://doi.org/10.1038/s41586-026-10996-5, was absent from the current literature-watch index. The paper reports ten programs and over 700 computations, including parity and arithmetic. The watch and Lane E gate treat this as external evidence only; strand inventory, preparation, heating/annealing, readout, failures, labour, equipment, reuse and scale must be counted. No UQPU reproduction, molecular energy/cost result, quantum advantage, new law or commercial claim is made.

## A–H ledger

- **A:** exhaustive GF(2) rank and parity-image tests; parity-QAOA, objective preservation and matched economics remain open.
- **B:** IBM Quantum, Amazon Braket, Azure Quantum/providers, IonQ, Rigetti, D-Wave, IQM, Quantinuum, Pasqal, QuEra, Quandela, OQC and emerging targets remain provider-neutral; no paid job.
- **C:** explicit molecular input/output, reporting/readout and persistence boundary; no state-space/readable-memory equivalence.
- **D:** alternative primitive reviewed; no device/chip/fabrication result.
- **E:** SDC-REPRO-001 opened; no Pangola substitution, accepted liquid fuel, net fusion electricity or cooling transfer.
- **F:** Landauer diagnostic and full accepted-task accounting plan; no measured energy/cost advantage.
- **G:** continuous D/G co-design retained; no process window, yield or cost-per-good-device result.
- **H:** source watch and strategic references preserved; no funding/principal/interest-rate/WACC result.

## FND/EQN status

- **FND-001:** helper added; no measured energy input, hence no empirical gap.
- **FND-002:** no new output-information/readable-storage bound.
- **FND-003:** no matched control-versus-quantum-speed-limit experiment.
- **FND-004:** new published alternative-primitive lead with falsifiable reproduction gate; not reproduced by UQPU.
- **FND-005:** no validated QFT/particle mechanism.
- **FND-006 / EQN-001–006:** source pinning, exact semantics, held-out tests, counterexamples and independent validation remain required; no equation/law promoted.

## INV-029–035 and moonshots

- **INV-029:** no phone-class physical compression or lifecycle closure; US$10T–US$100T remains an ambition-scale proxy.
- **INV-030:** no Pangola functional substitution/minimization/recovery result; no transmutation.
- **INV-031:** BIO-001 remains blocked on accepted-liquid mass/energy and upgrading/logistics/finance data.
- **INV-032:** FUS-001 remains model/cost-driver work; no net-electricity or commercial lifecycle-cost result.
- **INV-033:** no WACC/risk-premium/economy-wide-rate reduction.
- **INV-034:** testable alternative-primitive research advances; present physics remains binding.
- **INV-035:** external example only; units, symmetry/conservation/causality, limits, falsifiers, held-out predictions and independent validation remain mandatory.

INV-025/026/027 and the 100,000,000-GPU/universal 100,000,000-unit goals remain falsifiable targets. No end-to-end computing, memory, material, fuel, fusion, finance or Data-Center-to-One-Phone advantage is demonstrated.

## Architecture sync debt

AGENTS.md and the main-sync policy require A–I, and the nine-lane scoreboard contains I; docs/RESEARCH_OPERATING_SYSTEM.md and research_lanes/README.md still define A–H, and research_lanes/I_no_contact_vehicle_lift/README.md is absent (404). A–H were explicitly reviewed; repository-defined I remains MODEL_ONLY/no physical test. Reconcile architecture/manifest/path separately without deleting any track or claiming vehicle lift/field/gravity manipulation.

RESEARCH_GAPS.md and WORKLOG.md are extended from complete fetched contents, preserving the old content as an exact prefix. The active nine-lane scoreboard is appended; the legacy eight-lane history is untouched.

## Next gates

1. Exact-head CI on this branch; fix only reproducible failures.
2. Lane A: use the rank test as a prerequisite, then freeze signed-Max-Cut objective-preservation before any QAOA comparison.
3. Lane E: pin SDC source/protocol/data and reproduce one small program with blind inputs, controls and full wall-plug energy/cost.
4. Keep BIO-001, FUS-001 and FIN-001 separate and evidence-gated.
