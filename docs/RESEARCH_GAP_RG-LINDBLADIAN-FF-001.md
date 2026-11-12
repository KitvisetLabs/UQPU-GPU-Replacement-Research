# Research gap — 2026-10-26: class-specific Lindbladian fast-forwarding benchmark

**Stable ID:** RG-LIND-FF-001  
**Status:** LITERATURE_ONLY / NOT_YET_IMPLEMENTED  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Integration owner:** Lane F — benchmarks/evidence/economics  
**Cross-cutting:** FND-003, FND-004, FND-006, EQN-001–006  
**Canonical starting main:** 412403efebabd7186dcbfca286d8481308dab176

## Objective

Independently reproduce a small, explicitly specified member of a Lindbladian family for which the peer-reviewed Lévy–Khintchine/Hamiltonian-twirling result predicts a class-specific expected Hamiltonian-simulation-time scaling, then determine whether the result changes any end-to-end accepted-task decision after a competitive classical baseline and all resource costs are included.

## Current evidence

Gao, Ji and Liu, *Physical Review Letters* 137, 160405 (published 2026-10-16), DOI 10.1103/qy4b-gzlq; arXiv:2511.10253. The paper reports Θ(√t) for Gaussian dephasing, Θ(t) for compound-Poisson jumps and Θ(t^(1/α)) for symmetric α-stable families (α in (1,2]), with asymptotic lower bounds for the classes studied. Evidence class: peer-reviewed theoretical algorithm/lower bound. UQPU has not independently implemented or reproduced this result.

## Blockers

- No source-exact implementation of the selected generator/channel and twirling distribution is committed for this gate.
- No independently reproduced channel error, held-out scaling result, or lower-bound check exists.
- No competitive classical solver result uses the same input, output, accuracy, and runtime/resource contract.
- No target-specific compilation, energy, memory/I/O, price, or cost-per-accepted-task data exist.
- Asymptotic expected Hamiltonian-simulation time cannot be substituted for wall-clock latency or total task cost.

## Unlock criteria

1. Freeze a source-linked test manifest with exact generator, units, initial state, time grid, target error, observable and output contract.
2. Independently implement the channel and twirling route; use a predeclared channel-distance metric for tractable cases and publish raw outputs.
3. Check Gaussian and compound-Poisson cases separately; do not infer a universal result from one family.
4. Test a held-out parameter grid, failure cases, and numerical tolerance sensitivity.
5. Compare against an optimized classical master-equation/ODE solver at equal quality and accuracy.
6. Record preparation, controls/oracle access, randomization, gates/queries, shots/measurements, reconstruction, host compute, memory/I/O, retries, energy where measurable, and total cost.
7. Require independent reproduction before any algorithmic claim is promoted. Any hardware execution remains simulator-first and requires explicit authorization, credentials, bounded budget, and user consent.

## Negative controls

- A unit test that only evaluates the stated exponent is not a reproduction of the paper.
- A good log-log fit on the same points used to choose the model is not a held-out prediction.
- A channel simulation is not a real-QPU result.
- A theoretical lower bound is not an achievable device specification.
- A faster quantum subroutine is not end-to-end advantage if preparation, measurements, reconstruction, or classical postprocessing dominate.

## Mission impact and evidence boundary

No present claim changes for INV-029 through INV-035. This gap supplies a possible A-lane workload and FND-003/004 mathematical lead; it does not demonstrate quantum advantage, readable-memory substitution, critical-material reduction, accepted bio-oil, commercial fusion electricity, lower interest/WACC, or physical compression into a phone.

## Synchronization debt

This dated artifact is proposed as a new stable gap record. The large RESEARCH_GAPS.md, WORKLOG.md, and root README are intentionally not rewritten from partial history. After review/merge and current-head CI, reconcile this record into the canonical gap index and work log without truncating existing history.
