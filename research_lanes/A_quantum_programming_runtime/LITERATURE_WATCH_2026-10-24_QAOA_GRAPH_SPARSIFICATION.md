# Literature watch — QAOA graph sparsification and decomposition for noise-aware compilation

**Accessed:** 2026-10-24  
**Publication:** 2026-08-07, *Quantum* 10, article 2185  
**Primary owner:** Lane A — quantum programming, workloads, compiler and runtime  
**Feeds:** A, B, C, D/G co-design, F, INV-025–029, INV-034–035  
**Evidence class:** `LITERATURE_ONLY / PEER_REVIEWED_PRIMARY_SOURCE`  
**Project evidence promotion:** none

## Primary source and genuine novelty

Jai Moondra, Phillip C. Lotshaw, Greg Mohler and Swati Gupta, “Promise of Graph Sparsification and Decomposition for Noise Reduction in QAOA: Analysis for Trapped-Ion Compilations,” *Quantum* 10, 2185 (2026), published 2026-08-07. DOI: https://doi.org/10.22331/q-2026-08-07-2185; arXiv: https://arxiv.org/abs/2406.14330v4.

The paper studies Max-Cut QAOA and moves approximation-aware classical preprocessing into the compiler contract. It combines graph sparsification (reduce edges while approximately preserving cut structure) and decomposition of weighted graphs into unweighted components. The authors prove guarantees for the considered transformations and analyze trapped-ion-style all-to-all Ising-pulse implementations. For a controlled `(1-epsilon)` Max-Cut approximation loss, the paper reports worst-case Ising-pulse scaling from `O(n^2)` to `O(n log(n/epsilon))`; the stated Pauli-X count becomes `O(n log(n/epsilon)/epsilon^2)`. Its decomposition experiments are simulated and include dephasing noise. These are algorithm-/model-scoped guarantees and results, not a UQPU result.

## Limits that block promotion

- The evaluated objective is Max-Cut/QAOA, not arbitrary QUBO, neural inference, general GPU/CPU/NPU replacement, or a universal compiler theorem.
- Sparsification permits a controlled approximation loss. That loss must be measured against the exact project acceptance predicate; a shorter circuit is not automatically an accepted useful answer.
- The trapped-ion findings depend on the interaction and noise model. Hardware topology, gate/pulse calibration, routing, measurement, readout mitigation and provider billing can change the result.
- The paper does not provide UQPU target execution, project-specific provider-matched charges, total host/preprocessing energy, or cost per accepted useful task.
- Asymptotic circuit/pulse counts do not establish finite-instance speedup or economic advantage. Classical preprocessing and parameter-search cost must be included.
- No material, fuel, fusion-electricity, finance-rate or new-physical-law conclusion follows.

## Exact UQPU relevance

**Lane A:** add an approximation-aware compiler alternative before provider-neutral lowering. Compare dense/reference QAOA with sparsified and decomposed forms under one frozen workload contract.

**Lane B:** any eventual route must use the same provider, target, calibration period, circuit, shot policy and billing source for acceptance probability and economics. This watch authorizes no provider call or paid job.

**Lane C:** record graph/instance bytes, serialized circuit size, host preprocessing, parameter-search memory, transfer, state/readout, reconstruction and retries separately. Qubit count or Hilbert-space dimension is not readable RAM/storage.

**Lanes D/G:** expose target-specific interaction, gate/pulse, depth and connectivity demand as a co-design interface only after target-aware lowering. No fabrication or process-window inference is justified by this paper alone.

**Lane F:** include classical preprocessing, optimizer calls, compilation, shots, retries, reconstruction and measured energy/cost in cost per accepted useful task. Never combine one target's success probability with another target's price.

**INV-029:** a possible compiler-side resource reduction is a narrow stepping stone; it does not demonstrate data-center-to-phone physical compression. INV-025/026/027 and the 100x/100,000,000x moonshots remain unproven.

## Falsifiable follow-up

Run the pre-registered `QAOA-SPARSE-001` contract in `QAOA-SPARSE-001_MATCHED_ACCEPTED_TASK_BENCHMARK.md`.

1. Freeze and hash weighted/unweighted graph families, train/validation/held-out graph groups, seeds, objective convention, reference solutions for small cases and acceptance threshold before tuning.
2. Compare (a) dense/reference QAOA, (b) sparsified QAOA, (c) decomposition-based QAOA and (d) competitive classical Max-Cut baselines on identical instances and output-quality rules.
3. Predeclare epsilon values and parameter/shot/optimizer budgets. Use exact optimum where tractable; otherwise report a separately identified best-known bound and its provenance.
4. Run noise-free simulation first, then a documented noise model. Keep hardware/SDK checks separate from simulation; do not submit a paid QPU job without credentials, bounded budget and explicit owner consent.
5. Record cut value and approximation ratio, acceptance rate, gate/pulse counts, depth, compile and host time, graph/circuit bytes, shots, retries, reconstruction, measured energy where available, actual provider charge where available, and total cost per accepted useful task.
6. Include preprocessing and tuning costs for every method. If energy is unavailable for any compared method, report the energy comparison as unavailable, not zero.
7. Falsify the practical improvement claim if held-out accepted quality violates the declared tolerance, the gain disappears across seeds/noise assumptions, the classical baseline matches at lower total cost, or independent replay fails.

This follow-up tests a compiler/workload hypothesis. It does not test or revise a fundamental physical law. FND-001–006 and EQN-001–006 retain their current physics, mathematics, proof and evidence constraints.

## Current status

`LITERATURE_ONLY`; `QAOA-SPARSE-001` is proposed and **NOT EXECUTED**. No provider, QPU, paid model, instrument, purchase or funding action was used. No positive UQPU benchmark result is claimed.
