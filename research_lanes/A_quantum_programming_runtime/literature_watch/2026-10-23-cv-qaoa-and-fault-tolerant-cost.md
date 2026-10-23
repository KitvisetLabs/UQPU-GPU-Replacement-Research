# Lane A literature watch — CV-QAOA query bounds and fault-tolerant execution cost

**Date accessed:** 2026-10-23  
**Primary owner:** Lane A — quantum programming, workloads, compiler/runtime  
**Work ID:** A-CVQAOA-001  
**Related:** INV-025–027, INV-029, FND-002, FND-003, FND-006, EQN-001–006  
**Evidence class:** `LITERATURE_ONLY / THIRD_PARTY_PREPRINTS`  
**UQPU evidence promotion:** none

## Primary sources and genuine delta

1. Sriram Bharadwaj, Di Luo and Leo Zhou, “CV-QAOA: Efficient Low-Depth Quantum Optimization of Continuous Variables,” arXiv:2610.06815, submitted 2026-10-05: https://arxiv.org/abs/2610.06815
2. Yunxin Tang et al., “Low-cost algorithm-to-execution framework for surface-code quantum computing,” arXiv:2609.10965, submitted 2026-09-10 (page text updated 2026-10-14): https://arxiv.org/abs/2609.10965

Both are external theory/resource-model evidence, not UQPU execution measurements. The first supplies query-complexity results for continuous-variable optimization; the second connects logical algorithms to scheduling, non-Clifford supply, surface-code organization and physical-resource estimates.

### Delta 1 — query complexity must be paired with a dequantization audit

The CV-QAOA preprint reports a (2d)-query result for (d)-dimensional strictly convex quadratics and a two-query, one-step result for its Rotated Double Well (RDW) family. Crucially, the same paper shows that the RDW protocol is efficiently dequantizable and that a gradient-aligned classical line search reaches (O(d)) queries, near the stated Ω(d/logd) information-theoretic lower bound. It separately introduces a Rotated Square Well (RSW) family with a flat landscape and proves a classical hidden-rotation query lower bound under its stated oracle model, while giving a subpolynomial-query quantum construction.

The actionable novelty is not a blanket quantum advantage. It is a concrete example of why UQPU must classify workload structure and run the strongest structure-aware classical baseline before interpreting query counts. RDW is a required negative/dequantization control; RSW is a candidate positive-theory benchmark whose oracle assumptions, finite precision, state preparation, measurements and physical realization must be audited.

### Delta 2 — compilation/scheduling changes physical resource estimates

The surface-code framework constructs dependency-preserving schedules with time-resolved non-Clifford demand and architecture-aware layouts. It reports that physical costs can differ substantially between circuits with similar logical counts; under the authors' direct-rotation calibration, a QAOA amplitude-amplification example has up to a 241.5x reduction in estimated space-time volume versus an all-synthesis baseline. The paper reports lower routed-latency estimates for its 20 benchmark circuits and lower space-time volume for 13.

This supports adding schedule, routing/communication and non-Clifford resource supply to the compiler-to-cost interface. The multiplier is source-reported, calibration-dependent and not a universal factor. It is not a UQPU benchmark, hardware observation, accepted-task cost, or measured energy saving.

## Limits and evidence boundary

- Query complexity is not wall-clock latency, throughput, energy, reliability, or total cost per accepted useful result.
- CV-QAOA results depend on the specified cost-function oracle and mathematical problem family; the paper's classical dequantization result must not be omitted when presenting RDW.
- The RSW separation is scoped to the paper's oracle/hidden-rotation assumptions. Independent implementation, finite-precision sensitivity and adversarial counterexamples remain open.
- Fault-tolerant resource estimates depend on error rates, code distance, gate/rotation implementation, factory throughput, scheduling, layout, decoder and calibration assumptions. A model estimate is not measured device cost.
- Neither paper demonstrates provider execution, universal GPU/CPU/NPU replacement, classical memory/storage replacement, material substitution, accepted bio-oil, net fusion electricity, financing savings, or Data-Center-to-One-Phone compression.
- No QPU job, provider session, credential, shot, purchase or paid resource was used for this watch.

## Falsifiable UQPU follow-up

Create a frozen continuous-variable optimization workload contract with:
1. objective family and dimension (d);
2. exact oracle interface, precision, query accounting and allowed side information;
3. accepted output (objective value / optimality gap), quality tolerance, success probability and stopping rule;
4. training/validation/test seeds and hidden rotations committed before method selection;
5. CV-QAOA, the paper's dequantized RDW baseline, and at least one strong structure-aware classical optimizer;
6. RSW classical lower-bound assumptions and an independently implemented candidate quantum method;
7. full wall time, oracle calls, host compute, memory/data movement, state preparation, measurement/reconstruction, retries, energy where measurable and lifecycle cost per accepted output;
8. an explicit falsifier: if a matched classical method meets the same output contract within the same or lower total resource budget, reject an advantage claim for that instance.

Separately, map the best candidate circuit to a target-aware logical schedule and estimate non-Clifford supply, layout/routing, physical qubits, space-time volume and latency with pinned assumptions. Keep model-derived resources separate from actual target transpilation and authorized execution. No paid QPU submission without credentials, bounded budget and explicit consent.

## Cross-lane consequences

- **A:** add RDW dequantization and RSW oracle assumptions to the workload/benchmark backlog; no current compiler/runtime advantage is established.
- **B:** keep provider-neutral interfaces; no target is presumed to support the continuous-variable primitive or required fault-tolerant operations.
- **C:** include oracle input/output, state preparation, classical data movement and reconstruction; query counts do not imply memory capacity.
- **D:** derive device requirements only after a concrete primitive, precision and schedule exist.
- **E:** no new material, bio-oil, fusion, cooling or infrastructure evidence.
- **F:** require equal accepted-output quality and complete total-cost/energy accounting; never multiply the paper's reported factors into project economics.
- **G:** D/G co-design waits for a validated device/resource contract; no process-window or factory result.
- **H:** preserve source-scoped publication and capital discipline; no funding or WACC claim.

Lane I is supplemental repository scope only; it does not replace or reduce the permanent A–H architecture. FND-001–006, EQN-001–006, BIO-001, FUS-001 and FIN-001 remain active and unpromoted. INV-029–035 remain mission goals and evidence rules, not achieved outcomes.
