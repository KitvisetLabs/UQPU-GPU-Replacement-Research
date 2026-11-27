# Batch 146 — QGR-EXP-001 execution contracts and first workload freeze

**Date:** 2026-11-27  
**Starting main:** `0764c3e720daafaf0a3b1e778357dfb3821c5cc2` (reported at the end of Batch 145)  
**Status:** CONTRACTS FROZEN FOR IMPLEMENTATION; NO EXPERIMENT RUN CLAIMED  
**Evidence class:** SOFTWARE_CONTRACT / THEORY / MODEL_ONLY as explicitly separated below.

## Purpose

Move QGR-EXP-001 from a portfolio-level preregistration to executable, falsifiable first-stage contracts. This batch defines the exact acceptance boundary for EXP-00 and EXP-01 and selects a deliberately simple structured matrix family for the first EXP-05 feasibility study. It does not claim a quantum speedup, measured GPU result, simulator result, or QPU result.

## 1. EXP-00 — semantic and exact-reference control

### Frozen control workload

Reuse the existing signed-Max-Cut held-out fixtures and exact-reference assets already maintained by the repository. Do not create a second dataset, alter the train/validation/test split, or use test instances for tuning.

For every fixture, the canonical input is the signed weighted graph plus its frozen split/family metadata. The accepted classical reference is exhaustive enumeration for these small instances, including the complete set of maximizing assignments—not just one optimum.

### Required independent checks

1. Recompute the objective from canonical edges and a candidate bit assignment without calling the implementation under test.
2. Verify the declared sign convention and edge-weight convention using hand-calculated two- and three-vertex controls.
3. Verify bit order, vertex-to-qubit mapping, endianness and measurement-string decoding with basis-state controls.
4. Verify direct QUBO and edge-parity encodings represent the same logical objective after decoding.
5. Verify parity-cycle feasibility and reject infeasible bitstrings (fail closed; never silently repair).
6. Recompute optimum score and the full argmax set independently; preserve degeneracy.
7. Verify that every accepted output satisfies the frozen feasibility and normalized-regret contract.
8. Hash-bind the input manifest and exact-reference assets in every result record.

### Pass/fail rule

EXP-00 passes only if all controls agree exactly on all frozen fixtures and every deliberately malformed encoding/bit-order/decoder control is rejected. Any mismatch blocks all quantum-vs-classical performance comparisons. The existing Batch 143/144 artifacts provide useful controls, but their existence is not a claim that the new unified execution runner has passed.

### Outputs to implement

- machine-readable case manifest referencing existing immutable fixture IDs and hashes;
- independent reference evaluator;
- encoding/decoding cross-checks;
- positive and negative unit tests;
- per-case JSON result with evidence class and provenance.

## 2. EXP-01 — optimized classical/GPU baseline contract

EXP-01 must establish a trustworthy classical baseline before any QPU comparison. The benchmark harness must report two distinct scopes:

- **Kernel scope:** timed compute only, with inputs resident in the target memory; report this separately and never use it as the sole end-to-end result.
- **Accepted-task scope:** input generation/transfer, preprocessing, compute, synchronization, result extraction, validation and retries required to produce an accepted output.

For each run, record GPU model and architecture, CPU/host, RAM and VRAM, operating system, driver, runtime, compiler, library versions, precision mode, clock/power policy where accessible, batch size, warm-up, repetitions, synchronization method, input hash, output hash, correctness/quality, median and tail latency, throughput, peak memory, energy measurement method (or null with reason), and full software command/environment.

### Fairness and statistics

- Compare the same frozen workload, input, output contract, precision and acceptance threshold.
- Use a tuned, documented implementation appropriate to the GPU; include a CPU reference and a GPU implementation. Add multi-GPU only where the workload and scaling policy make it relevant.
- Separate compilation/JIT from steady-state execution and report both cold-start and warm measurements.
- Use paired inputs and fixed seeds; publish all repetitions, not only the best run.
- Report median, p95 and uncertainty intervals; do not infer a performance win from a single timing.
- Do not compare FLOP/s or TOPS against gate counts. Compare accepted useful tasks.
- No GPU hardware is presumed available in this workflow. If no physical GPU can be measured, mark the result DATA_BLOCKED and retain only a clearly labelled MODEL_ONLY or externally sourced baseline.

### Pass/fail rule

EXP-01 passes only when correctness is independently validated, the environment and commands are reproducible, and the baseline is sufficiently optimized and fully accounted. Missing hardware, energy telemetry or software provenance must be explicit; missing values are null, never fabricated.

## 3. EXP-05 first structured matrix candidate

### Candidate: one-dimensional Dirichlet Poisson operator

For dimension (N=2^m), define the real symmetric tridiagonal matrix

`A_N = tridiag(-1, 2, -1)`

with Dirichlet boundary conditions and a normalized right-hand side `b=e_1`. The accepted output is the single scalar

`z_N = b^T A_N^{-1} b = N/(N+1)`.

This is a compact-observable task, not a request to output the full solution vector. The exact scalar is an analytic reference and can be independently checked with a classical tridiagonal solve.

### Why this is the first candidate

- Sparse, structured and exactly specified matrix family.
- Closed-form reference makes semantic mistakes visible.
- The input/state preparation for `e_1` is simple and must be reported honestly.
- The observable is scalar, so the comparison does not pretend that a measured quantum state yields a full classical vector.
- It is intentionally a hard falsification baseline: classical tridiagonal algorithms are highly efficient, so no quantum advantage is presumed.

### Required quantum-side accounting

For every (N), report logical qubits, physical-qubit estimate separately, block-encoding normalization, oracle/query model and its construction cost, state-preparation cost, QSVT polynomial degree, controlled/reflection operations, gate count, two-qubit count, depth, ancillas, connectivity/routing, precision/error bound, shots or coherent estimation repetitions, measurement and postprocessing, QEC assumptions, and classical host work. If the access model assumes an oracle, its implementation cost cannot be set to zero without an explicitly justified hardware primitive.

### Classical comparator

Use a stable tridiagonal direct solver as the primary algorithmic baseline; include a dense solver only as a diagnostic, not as the deliberately weak comparator. Measure the scalar output and residual/forward error under the same precision target. Report input construction and complete accepted-task time separately from resident-kernel timing.

### Initial size sweep

Use (N in {16, 32, 64, 128, 256, 512, 1024}) for analytic and classical controls. Quantum resource estimation may extend to larger (N) only if the access model and precision are explicit. These are study points, not a claim that the QPU can run them.

### Falsification criteria

The candidate fails to show a useful crossover if state preparation/oracle construction, QSVT degree, precision, measurement, QEC, or host costs dominate the tridiagonal classical solve throughout the tested range. A negative result is retained and informs workload selection; it is not replaced with a more favorable problem after observing results without a new preregistration.

## 4. Cross-lane work opened

- **A:** reference evaluator, semantic IR and QSVT resource contract.
- **B:** provider-neutral capability metadata only; no job submission.
- **C:** state preparation, sparse-oracle construction, output bandwidth and host-memory boundary.
- **D:** logical-to-physical mapping, native gates and QEC assumptions.
- **E:** control/cooling/energy boundary; no unmeasured energy claim.
- **F:** baseline reproducibility, uncertainty, acceptance contract and cost-per-task.
- **G:** packaging/connectivity constraints only where supported by a target architecture.
- **H:** preserve the full GPU-replacement objective while clearly labelling this as one narrow workload.

## 5. Immediate implementation order

1. Implement EXP-00 independent reference and negative controls against the existing frozen fixtures.
2. Implement the EXP-05 analytic Poisson reference and classical tridiagonal baseline.
3. Add EXP-01 benchmark metadata/result schema and capture a physical GPU baseline only on a known available device.
4. Produce ideal-circuit and resource estimates only after the semantic contract passes.
5. Consider noisy simulation after ideal correctness; consider real QPU execution only after explicit user approval, credentials, a bounded budget and the preregistered gates.

## 6. Evidence and authorization boundary

This batch freezes contracts and a candidate mathematical workload. It does **not** report that EXP-00, EXP-01, or EXP-05 has been executed. No simulator, GPU benchmark, QPU job, energy measurement, hardware purchase or external spend is authorized or claimed. Paid QPU work and any external expenditure still require explicit user approval.

## 7. Handoff

The next agent should implement the independent EXP-00 evaluator and tests first, then the exact Poisson scalar reference and classical baseline. Preserve all frozen fixture hashes and test/holdout boundaries. Update this batch with actual commands, environment, outputs and failures only after running them.