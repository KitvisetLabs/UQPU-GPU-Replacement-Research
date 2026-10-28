# Literature watch — GPU-accelerated stabilizer simulation

**Date checked:** 2026-10-29  
**Primary owner:** Lane A — quantum programming, workloads, compiler and runtime  
**Interfaces:** B (provider-neutral simulation routing), C (memory/state/data movement), F (benchmark and lifecycle economics), H (publication)  
**Evidence class:** PEER-REVIEWED COMPUTATIONAL BENCHMARK / THIRD-PARTY RESULTS / NOT REPRODUCED BY UQPU  
**Stable IDs:** LIT-2026-10-01-QUASARQ; RG-A-QUASARQ-STABILIZER-REPRO-001; INT-20261029-QUASARQ-SIMULATOR

## Primary source

Muhammad Osama, Dimitrios Thanos and Alfons Laarman, “GPU-Accelerated Quantum Simulation of Stabilizer Circuits,” *Quantum* 10, 2225 (published 2026-10-01). DOI: https://doi.org/10.22331/q-2026-10-01-2225.  
Official journal page: https://quantum-journal.org/papers/q-2026-10-01-2225/  
Official preprint: https://arxiv.org/abs/2603.14641  
Open implementation: https://github.com/muhos/QuaSARQ

## Reported result and genuine novelty

The paper introduces QuaSARQ, a GPU-accelerated simulator for Clifford/stabilizer circuits. Its implementation reorganizes tableau evolution, Gaussian-elimination work and projective-measurement updates around data-parallel GPU primitives, including prefix-XOR scans and memory-coalesced layouts. The authors report benchmarks reaching 180,000 qubits, depth 1,000 and roughly 130 million gates; the paper reports up to 105× runtime speedup and over 80% energy reduction on demanding benchmark instances against the simulators and configurations evaluated.

The useful novelty for UQPU is a concrete, published example of algorithm/data-layout co-design that can strengthen the **classical simulation and verification layer** used in quantum error-correction and stabilizer-circuit research. It is not a new quantum algorithm advantage or a real-QPU result. The headline multipliers are source-reported, benchmark-specific measurements and have not been reproduced by UQPU.

## Exact UQPU relevance

- **Lane A / INV-025–027:** use the paper as a candidate reference for the classical simulator portion of a workload contract. Preserve exact circuit semantics, output/syndrome correctness and held-out circuit families. The current graph-parity encoder tests are classical mapping certificates; they do not implement parity-QAOA.
- **Lane B:** a simulator adapter can be provider-neutral, but its target identity must say “classical stabilizer simulator,” not a physical quantum provider. Simulator results and real-QPU results remain separate evidence classes.
- **Lane C:** tableau storage layout, peak memory, sampling throughput, host/device transfer and reconstruction are first-class metrics. Large state-space or qubit-count figures do not imply readable classical RAM/VRAM/storage equivalence.
- **Lane F:** compare total cost and energy per accepted, correct circuit/syndrome sample. Include setup, compilation, warm-up, data transfer, host work, memory, retries and measurement/sampling overhead; do not compare isolated kernel timing with end-to-end task timing.
- **INV-029:** a more efficient classical simulator may improve verification or development economics, but it does not compress data-center capability into one phone and does not eliminate external infrastructure.
- **INV-034–035:** the method is a systems/algorithmic engineering lead, not a new physical equation or law.

## Scope limits

QuaSARQ targets stabilizer/Clifford circuits. It is **not a general simulator for arbitrary non-Clifford QAOA rotations**; it must not be substituted for the parity-QAOA simulation gate except for genuinely Clifford subcircuits or separate stabilizer/QEC workloads. The paper's reported GPU results also depend on its evaluated hardware, software, circuit suite and baseline settings. UQPU has not independently verified the code revision, environment, hardware, power measurement, output equivalence or the reported speed/energy ratios.

## Falsifiable follow-up

1. Pin the exact paper revision, source commit, license, dependencies, benchmark manifests, GPU model, CPU model, driver/runtime and measurement scripts; record hashes and reproducible commands.
2. Select a small, fixed subset of public stabilizer circuits and freeze expected outputs/syndromes and correctness tolerances before tuning.
3. Compare QuaSARQ against the same-version, same-workload Stim CPU baseline and the paper's other supported baselines where reproducible. Separate warm-up/compilation from steady-state execution and also report end-to-end time.
4. Measure runtime distributions, samples/second, peak host/device memory, bytes transferred, retries, correctness failures and energy where a suitable meter is available. Record unavailable energy components as unknown, not zero.
5. Test at least one held-out circuit family or size regime and publish all failed cases and environment differences.
6. Accept the paper as reproduced only if the declared correctness contract passes and the measured results are consistent within predeclared uncertainty. Reject a claimed system benefit if transfers, setup, host work, memory limits or power overhead erase it.

**Disposition:** useful source-pinned simulator candidate; reproduction not started. No real-QPU advantage, general QAOA advantage, GPU replacement, commercial economic benefit, new physical law or Data-Center-to-One-Phone milestone is claimed.
