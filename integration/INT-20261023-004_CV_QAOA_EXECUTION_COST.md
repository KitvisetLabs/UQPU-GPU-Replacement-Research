# Integration record INT-20261023-004 — CV-QAOA to fault-tolerant cost gate

**Status:** PROPOSED / BLOCKED ON REPRODUCTION  
**Date:** 2026-10-23  
**Primary owner:** Lane A; Lane F owns economic acceptance; Lane B owns provider feasibility; D/G own downstream device/manufacturing implications.  
**Canonical starting main SHA:** `c7b5958af58fad04a101ef5c6abf6a29293c867e`  
**Lane artifact:** `research_lanes/A_quantum_programming_runtime/literature_watch/2026-10-23-cv-qaoa-and-fault-tolerant-cost.md`  
**Lane artifact commit:** `236ecbabd5d83621d72319a9f27178ce970ed121` (branch-only; pending main synchronization)

## Hypothesis and causal mechanism

A continuous-variable optimization workload may be a useful candidate only when its query-model structure survives a strong classical-dequantization audit and its circuit/algorithm is then mapped through an explicit logical schedule, routing/layout and non-Clifford-resource model. Query-count reduction alone does not establish lower runtime, energy or total cost.

## Source evidence and assumptions

- CV-QAOA: arXiv:2610.06815, submitted 2026-10-05. The paper reports theoretical query bounds for specified function families, explicitly dequantizes its RDW example, and gives a separate RSW result under a stated hidden-rotation/oracle model.
- Surface-code algorithm-to-execution framework: arXiv:2609.10965, submitted 2026-09-10; page text updated 2026-10-14. Its resource reductions are model-derived and depend on the authors' calibration and scheduling assumptions.
- Both inputs are `LITERATURE_ONLY / THIRD_PARTY_PREPRINTS`. They are not project measurements.

## Shared interface and matched useful-output contract

Freeze one workload record containing:
- objective family, dimension, units, domain, oracle interface and precision;
- output type, optimality gap, quality tolerance, success probability and stopping rule;
- data/seed split hashes and hidden-orientation provenance;
- query budget and all permitted side information;
- classical baselines (including RDW dequantization), candidate quantum method and resource model versions;
- accepted output count, wall time, host compute, memory/I/O, state preparation, shots/measurements, reconstruction, retries, energy where measurable, target costs and lifecycle boundary.

No comparison is valid if it changes the objective, allowed oracle information, output quality or acceptance rule between methods.

## Expected gain vs measured result

- **Expected:** identify which continuous-optimization instances are already classically tractable; reduce the risk of false quantum-advantage claims; expose schedule/layout/non-Clifford costs before any target execution.
- **Measured in UQPU:** none. No implementation benchmark, target transpilation, provider execution, energy measurement or accepted-task cost was performed by this integration record.
- **Reported by sources:** theory/resource-model results only, not transferred to project metrics.

## Evidence gates and falsifier

1. Independently reproduce the mathematical query-model definitions and theorem assumptions.
2. Reproduce RDW classical dequantization as a negative control; include RSW only under the exact hidden-rotation/oracle conditions.
3. Freeze held-out instances and compare output quality, wall time, oracle calls, host resources, memory/I/O, and energy/cost where measurable.
4. Map the best candidate to a pinned logical schedule and target-aware resource estimate; keep estimated physical resources separate from device measurement.
5. Falsify any advantage claim if a matched classical method meets the same acceptance contract at equal or lower total resource/cost, or if the purported quantum separation disappears under the declared finite-precision/input-output model.
6. Promote no result beyond its actual evidence class; real-QPU work remains subject to credentials, a bounded budget and explicit user consent.

## Cross-lane scan

| Lane | Interface consequence | Current status |
|---|---|---|
| A | Workload contract, quantum/classical algorithms, query/quality tests, compilation and scheduling | READY FOR OFFLINE BENCHMARK DESIGN; no performance claim |
| B | Provider-neutral target capability and submission guard | BLOCKED on concrete primitive/target fit; no provider calls |
| C | Input/output, state preparation, measurement and reconstruction accounting | REQUIRED; no memory equivalence |
| D | Device requirements derived from precision, schedule and physical-resource model | BLOCKED on a validated circuit contract |
| E | Materials, cooling, energy and infrastructure | REVIEWED; no new measurement |
| F | Matched useful-output economics, resource ledger and uncertainty | REQUIRED; no cost/energy result |
| G | Device/fabrication/process-window response to validated resource requirements | BLOCKED on D |
| H | Literature publication and strategic/financial evidence discipline | PRESERVED; no capital/WACC claim |

D/G co-design remains continuous but cannot infer a process window from a query bound. Lane I remains an auxiliary repository workstream and does not redefine the permanent A–H architecture.

## INV-029 through INV-035

- **INV-029:** strengthens the route from algorithmic candidate to measured useful service; no phone-class physical compression.
- **INV-030:** no material substitution or transmutation claim.
- **INV-031:** no accepted liquid-fuel evidence.
- **INV-032:** no net reliable delivered fusion-electricity evidence.
- **INV-033:** no principal, interest, financing-duration or WACC measurement.
- **INV-034:** advances assumption-scoped lower-bound and model/resource audit methods.
- **INV-035:** maintains falsifiers, limiting cases, held-out tests and independent reproduction; neither preprint is a new physical law.

## Provenance and sync state

This record is being added to the open supplementary research PR branch `research/cycle-20261023-fnd-qfi-audit` (PR #49). It is not on canonical `main` until the PR is reviewed, CI passes on its exact head, and a merge SHA is observed. No main-branch sync is claimed.
