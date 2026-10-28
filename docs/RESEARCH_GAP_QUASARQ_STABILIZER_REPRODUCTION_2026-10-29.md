# Research gap RG-A-QUASARQ-STABILIZER-REPRO-001 — reproducible GPU stabilizer simulation

**Opened:** 2026-10-29  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Interfaces:** B (simulator/provider separation), C (memory and data movement), F (benchmark/economics), H (publication)  
**Status:** OPEN / LITERATURE_ONLY / SOURCE-PINNING-AND-REPRODUCTION-NOT-STARTED  
**Source:** https://doi.org/10.22331/q-2026-10-01-2225  
**Related:** INV-025/026/027, INV-029, INV-034/035, RG-QAOA-PARITY-001

## Objective

Determine whether the published QuaSARQ GPU stabilizer simulator can be independently reproduced on a bounded public circuit suite and whether any speed/energy benefit remains after the full simulator task boundary is counted.

## Current evidence

Osama, Thanos and Laarman, *Quantum* 10, 2225 (2026-10-01), report a GPU simulator for stabilizer/Clifford circuits, with benchmarks reaching 180,000 qubits, depth 1,000 and about 130 million gates. The paper reports up to 105× speedup and over 80% energy reduction on selected demanding instances. These are third-party benchmark results, not UQPU reproduction.

The starting main head's parity-map encode/decode-bijection test has passed the exact-head repository CI; it exhaustively checks the graph mapping for all 1,099 labelled simple graphs with one through five vertices. That is a classical mapping correctness gate only. It does not implement a parity-QAOA circuit, reproduce QuaSARQ, or demonstrate a QPU or economic advantage.

## Acceptance contract

- Pin source commit, dependencies, build flags, GPU/CPU models, driver/runtime, circuit suite, seeds and all input/output manifest hashes.
- Check exact output/syndrome correctness against a declared reference before timing.
- Report qubits, circuit family, depth, gate/measurement counts, shots, warm-up, compilation/setup, steady-state and end-to-end latency, throughput, retries and failed cases.
- Record peak host/device memory, transfer bytes/time, reconstruction and host compute.
- Measure energy with a declared boundary and instrument where feasible; label unmeasured components UNKNOWN rather than zero.
- Keep each baseline's version, hardware and configuration paired with its measurements.
- Test a held-out circuit family or size regime and publish negative results.
- Treat this as a classical simulator comparison, not a physical QPU comparison. Do not use stabilizer-only simulation as a generic non-Clifford QAOA simulator.

## Falsifiers and unlock criteria

The reproduction fails if the declared output/syndrome contract fails, if benchmark inputs or baselines cannot be matched, or if the reported performance is not reproducible within preregistered uncertainty. A claimed end-to-end benefit is rejected if setup, transfer, memory pressure, host work or energy overhead erases the advantage. Closing this gap requires pinned-source reproduction, held-out tests and a complete, auditable result record.

## Nonclaims

No real-QPU execution, quantum advantage, GPU replacement, readable classical-memory equivalence, universal 100×/100,000,000× economics, new physical law, material substitution, accepted bio-oil, net fusion electricity, lower WACC or Data-Center-to-One-Phone closure is established. BIO-001, FUS-001 and FIN-001 remain independent evidence gates.
