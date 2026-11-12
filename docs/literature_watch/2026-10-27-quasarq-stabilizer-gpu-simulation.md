# Literature watch — 2026-10-27: GPU stabilizer simulation as a stronger classical baseline, not quantum advantage

**Primary owner:** Lane H — literature surveillance and publication  
**Implementation owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Cross-lane consumers:** Lane C (memory/state/data movement), Lane F (benchmark/evidence/energy accounting), Lane D/G (device and production boundary review)  
**Work item:** QUASARQ-REPRO-001  
**Evidence class:** PEER-REVIEWED EXTERNAL SOFTWARE/ALGORITHM RESULT + PREREGISTRATION; NOT YET REPRODUCED BY UQPU

## Primary sources and dates

1. Muhammad Osama, Dimitrios Thanos and Alfons Laarman, “GPU-Accelerated Quantum Simulation of Stabilizer Circuits,” Quantum 10, 2225, published 2026-10-01, DOI https://doi.org/10.22331/q-2026-10-01-2225. Official journal record: https://quantum-journal.org/papers/q-2026-10-01-2225/
2. Official arXiv record, version 2 revised 2026-09-23: https://arxiv.org/abs/2603.14641
3. Public implementation: https://github.com/System-Verification-Lab/QuaSARQ. The displayed repository identifies itself as a fork of muhos/QuaSARQ. Pin an immutable commit and check its license/dependency graph before attempting reproduction.

## Genuine technical delta

The paper describes GPU-oriented stabilizer-tableau simulation with a dual tableau layout, GPU-friendly gate scheduling, pivot compaction, a three-pass prefix-XOR formulation for measurement-related Gaussian elimination, and Pauli-frame many-shot sampling. It reports tests on random Clifford/OpenQASM circuits up to 180,000 qubits and depth 1,000 (roughly 130 million gates), with author-reported results including up to 105× speedup on selected operations/workloads, more completed heavy-suite circuits, and over 80% energy reduction on demanding cases.

The important UQPU insight is methodological: **classical simulator architecture is part of the baseline, not a disposable control.** A quantum or hybrid workload claim can be misleading if it is compared against a generic or poorly matched classical simulator while a specialized stabilizer implementation changes the baseline by orders of magnitude. The paper also supplies a concrete memory/data-movement case study: tableau layout, transposes, memory allocation, scheduling and host-to-device transfers are part of the measured runtime.

## Limitations and exact boundary

- These are the authors’ published results, not an independent UQPU reproduction.
- The tested domain is the stabilizer/Clifford circuit class, which is classically simulable; it does not establish quantum hardware advantage, universal quantum computation, general-purpose GPU replacement, or Data-Center-to-One-Phone compression.
- The paper reports an RTX 4090 with 24 GB GPU memory and CUDA 12.6 for GPU experiments, and a separate DAS-6 CPU cluster with AMD EPYC 7282 CPUs and 256 GB RAM. The paper notes a CPU clock roughly 20% faster than the GPU clock; this is not a same-box CPU/GPU comparison.
- The reported energy method multiplies runtime by average processing-unit power. That is not automatically a full wall-plug/system energy boundary: host CPU, idle/active system components, power-supply losses, memory, cooling and facility overhead may be omitted.
- The measurement-performance benchmark uses one simulation run per circuit; sampling uses a 1,024-shot comparison. A UQPU reproduction should quantify run-to-run variation, timeouts and uncertainty rather than infer confidence from a single run.
- Random circuit structure is useful for a controlled microbenchmark but is not, by itself, representative coverage of QEC decoding, application-level quantum algorithms or customer useful work.
- The public source repository reports GPL-3.0. This watch does not copy its code. Before reuse, pin exact source/dependency revisions and obtain a license-compatible implementation plan.

## Falsifiable follow-up: QUASARQ-REPRO-001

1. Freeze the exact paper version, source commit, license, dependencies, compiler/toolchain, circuit generator version, seeds, circuit files and SHA-256 hashes. Do not use a mutable branch name as the reproducibility identity.
2. Rebuild a small correctness tier first, then medium cases, then resource-bounded large cases. Use the same exact circuit bytes, gate/measurement semantics, shots and timeout policy for QuaSARQ and each comparator. Do not compare a sampled output with a single-shot output.
3. Use Stim as the primary specialized CPU baseline and, where available, Qiskit-Aer CPU/GPU as secondary comparators. Record CPU/GPU model, RAM/VRAM, driver, compiler flags, power mode, process affinity and background load. Prefer same-host comparisons; if separate machines are unavoidable, report them as separate configurations and do not call the result a controlled same-system comparison.
4. **Accepted-output gate:** on small circuits, compare exact deterministic results and cross-check sampled results against an independent reference. On stochastic cases, compare observable/detector distributions with preregistered statistical tests and confidence intervals; require logical-observable error-rate agreement where applicable. Any output mismatch is a correctness failure, regardless of speed.
5. **Performance gate:** include parsing, allocation, scheduling, transfer, kernel execution, synchronization and output reconstruction in end-to-end latency. Also report phase-level timings. Run warmups and repeated timed trials; preregister repetition counts by size tier, retain all timeouts/failures and do not report only completed instances. Use at least 5 timed repeats per feasible deterministic case and at least 30 paired sampling seeds where the budget permits; disclose any tier where these counts cannot be reached.
6. **Energy gate:** report the source method (GPU/CPU telemetry versus external wall-plug meter), sampling interval, idle subtraction, calibration/uncertainty and included components. The primary system metric should include host + accelerator energy over the same end-to-end boundary; provide device-only energy separately. Never convert runtime × nominal TDP into measured energy.
7. **Memory/I/O gate:** record peak host RAM, peak VRAM, allocation/reservation, transfer bytes, transfer time, temporary buffers, output bytes, retry/reconstruction costs and any state retained between shots. A tableau or qubit count is not readable classical RAM/storage capacity.
8. **Economics gate:** only compute cost per accepted task when hardware, utilization, energy tariff, amortization, software/license and workload boundaries are documented. Do not combine one target’s success probability with another target’s price. For this classical simulator study, distinguish direct simulator cost from any later quantum execution cost.
9. **Falsifier:** reject a claimed advantage if accepted outputs disagree, speed/energy gains disappear on a fair baseline, the advantage depends on unreported timeouts or different workloads, resource boundaries are inconsistent, or the gain fails to generalize outside a cherry-picked subset. A successful replication would establish a classical simulator result only—not quantum advantage or universal subsystem replacement.

## Cross-lane implications

- **A:** strengthen the competitive classical baseline before any QUBO/QAOA or quantum workload economics claim; do not substitute this Clifford-only result for a target workload.
- **B:** no provider adapter or real-QPU claim follows. Simulator/dry-run remains the rule.
- **C:** capture tableau layout, peak memory, host/device transfers, output buffers and many-shot state reuse; formula complexity is not a proxy for readable memory.
- **D/G:** dual-layout/parallel-prefix ideas motivate architecture and memory-hierarchy questions only. They do not demonstrate a new quantum chip, process window, fabrication yield or equipment capability. Keep D/G co-design explicit.
- **E:** measured simulator energy is an infrastructure input, not bio-oil or fusion evidence. No Pangola/material substitution or net fusion-electricity result follows.
- **F:** enforce identical useful output, fair CPU/GPU baselines, total cost per accepted output, uncertainty and complete energy boundaries.
- **H:** publish the external result with its limitations and retain the multilingual Kanusanan Pongpanna Model context; strategy is not evidence.
- **INV-034/035:** no new physical equation or law is proposed. The method is conventional algorithm/software engineering under known stabilizer theory.

## Relation to other literature

The 2026-10-26 CoSR/transformer/search-control/structural-guidance watch remains the canonical equation-discovery-method comparison. QuaSARQ is a distinct classical simulator and memory/data-movement result; it is not a duplicate of that watch and does not rank equation-discovery methods. No new claim is made about BIO-001 accepted liquid fuel, FUS-001 net reliable delivered electricity, FIN-001 financing, material qualification or physical-law discovery.
