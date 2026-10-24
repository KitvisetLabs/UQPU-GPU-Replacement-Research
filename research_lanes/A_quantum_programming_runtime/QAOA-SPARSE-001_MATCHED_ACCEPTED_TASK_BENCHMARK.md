# QAOA-SPARSE-001 — matched accepted-task benchmark for approximation-aware QAOA compilation

**Date:** 2026-10-24  
**Primary owner:** Lane A — quantum programming, workloads, compiler/runtime  
**Cross-lane interfaces:** B provider lowering; C state/data movement; D/G device/factory co-design; F economics/evidence  
**Status:** PROPOSED / NOT EXECUTED  
**Evidence class:** EXPERIMENT_PLAN / LITERATURE_ONLY

## Objective

Test whether graph sparsification or weighted-graph decomposition reduces the full cost of producing an accepted Max-Cut solution when compared with dense/reference QAOA and competitive classical methods under identical useful-output rules. The 2026 *Quantum* paper is a method hypothesis, not project evidence.

## Frozen task and acceptance contract

- Define the objective sign convention, graph family, weight domain, feasible bitstring, cut-value calculation, and accepted-output predicate before any method sees the held-out graphs.
- Hash instance sets and split by whole graph instances/families, not by repeated samples from one graph.
- Use exact optima for tractable instances. For larger instances, state the source and date of each best-known bound and do not relabel it an optimum.
- Predeclare epsilon/tolerance values, parameter-optimization calls, shots, retry limits, noise assumptions and stopping rules.
- Keep dense/reference QAOA, sparsified QAOA, decomposition-based QAOA, and classical baselines on the same instances and acceptance threshold.

## Required measurements

For each method, graph, seed and target/noise condition, record:
- objective/cut value, approximation ratio, accepted/rejected output, and uncertainty;
- graph and serialized-circuit bytes, preprocessing time, compile time, optimizer calls, host runtime and peak memory when measurable;
- logical/physical qubits, ancillas, gates/pulses, depth, routing/connectivity overhead and readout/reconstruction;
- shots, retries, mitigation and orchestration;
- measured energy only with a declared measurement boundary and instrument; actual provider charge only from the same provider/target route that generated the accepted-output data;
- total cost per accepted useful task, undefined when no task is accepted or the cost denominator is unknown.

No cross-provider probability/price mixing is allowed. A simulator result stays SIMULATION_ONLY. Execution success without output-quality acceptance is failure for this contract.

## Baselines and resource fairness

1. Exact optimization for small graphs.
2. At least one strong, documented classical approximation/heuristic baseline, including its tuning and preprocessing cost.
3. Dense/reference QAOA with the same parameter-search and shot budgets as the transformed variants.
4. Sparsified and decomposed variants with epsilon fixed before held-out evaluation.

Keep all method budgets explicit and equal at the contract level. Record actual resource use separately; a declared cap is not a measured use. If energy cannot be measured for every method, omit comparative energy claims.

## Stop / falsification conditions

Reject a practical improvement claim if any of the following occurs:
- accepted held-out quality falls outside the predeclared tolerance;
- the gain is not robust across held-out graph families and seeds;
- noise-model changes reverse the ranking without a defensible target-specific explanation;
- the classical baseline achieves the same accepted output at lower total cost;
- preprocessing, tuning, retry, mitigation or reconstruction costs are missing;
- an independent replay fails;
- provider-specific success probability is paired with another target's price.

## Execution boundary and next gate

First implement a deterministic offline fixture and exact/known-bound checks. Then perform target-aware simulation and independent SDK lowering. Real-QPU execution is a separate gate and remains prohibited until credentials, a bounded budget and explicit user consent are present.

No material/fuel/fusion result, WACC effect, new physical law, memory replacement, or Data-Center-to-One-Phone achievement can be inferred from this benchmark.
