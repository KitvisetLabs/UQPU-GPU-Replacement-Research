# Research and Engineering Process

This file records the working method for the UQPU project.

## Process

### 1. Define GPU goals
Enumerate the practical application objectives for which GPUs are used.

### 2. Define output contracts
For each workload specify whether the result must be exact, bounded-error, approximate, sampled, or probabilistic.

### 3. Extract semantics
Translate source workloads into mathematical intent rather than preserving GPU implementation details.

### 4. Generate candidate UQPU mappings
Consider gate-model, reversible, variational, analog, photonic, continuous-variable, sampling, and future quantum modalities.

### 5. Estimate resources
For each mapping estimate state preparation, logical qubits, physical qubits, logical depth, non-Clifford resources, shots, QEC overhead, measurement and output reconstruction.

### 6. Build classical baselines
Use competitive CPU/GPU implementations and record end-to-end latency, throughput, energy and cost.

### 7. Compare end-to-end
Do not exclude data movement or quantum overhead.

### 8. Classify result
Use:
- FUNCTIONALLY_SUPPORTED
- COMPETITIVELY_SUPPORTED
- QUANTUM_ADVANTAGE_CANDIDATE
- NO_ADVANTAGE_FOUND
- UNRESOLVED

### 9. Update architecture
Feed benchmark results back into compiler, runtime, memory and hardware-design decisions.

### 10. Preserve decision history
Every major design change should be written into `DECISIONS.md` and every meaningful progress step into `WORKLOG.md`.

## Cost-optimization process

For every workload investigate:

1. algorithmic work reduction
2. state-preparation reduction
3. memory/data-movement reduction
4. shot/measurement reduction
5. QEC reduction
6. energy reduction
7. hardware utilization
8. amortization/lifetime
9. manufacturing and packaging
10. failure/retry reduction

The 100× minimum target and 10^8× moonshot target must be tested through this full stack.


## Parallel Simple Mode
The canonical coordination method is defined in `docs/RESEARCH_OPERATING_SYSTEM.md`.

All research is grouped into eight lanes:
A) workloads/software; B) quantum/cloud; C) memory/photonics/interconnect; D) devices/fabrication/packaging; E) biomass/materials/energy/infrastructure; F) economics/evidence/integration; G) quantum-chip manufacturing equipment/software; H) strategic-plan/finance/future-industry research.

All lanes use one work-item contract and converge through one integration gate. Prioritize P0 integration blockers and P1 economic bottlenecks before broad feature expansion. Parallel agents may execute lanes concurrently when available; otherwise use the identical lane decomposition sequentially and record the limitation.


## Continuous evidence and publication
Every working cycle performs targeted searches of primary research and official provider/programming documentation, recording access date, review depth and the concrete experiment/decision informed. Quantum programming is Priority #1; A–H all receive explicit progress or blocker review.

Publish code, articles, reproducibility data and negative results at every meaningful validated milestone. Verify the remote commit and its own CI state; old successful runs and empty status lists are not proof of current-commit success. Relevant Gmail notifications are diagnostic inputs; inspect the corresponding public workflow and publish project evidence rather than private mail or tracking links.

## Per-interaction GitHub publication invariant
When the project owner asks to check progress and continue research, the interaction is not complete until the resulting progress is published to this GitHub repository.

Every such research interaction must end with at least one durable public GitHub update appropriate to the evidence produced: executable code, tests, benchmark/result artifacts, a dated research/literature note, a decision/gap record, or a tracking issue. If no code change or positive scientific result is justified, publish a dated status/negative-result note recording the checked HEAD, evidence reviewed, why no promotion was made, and the next falsifiable gate instead of leaving the result only in chat.

After publication, verify the new remote HEAD and inspect CI for the new state whenever the changed paths trigger a workflow. Do not report an old successful workflow as proof for a newer commit. Scientific evidence labels and non-claims remain binding even when publication is mandatory.
