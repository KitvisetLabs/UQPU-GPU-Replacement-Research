# Quantum Processor GPU Replacement — Research and Experiment Program

**Date:** 2026-11-27  
**Stable work ID:** QGR-EXP-001  
**Primary owner:** Lane A — Quantum programming / workloads / compiler / runtime  
**Cross-lane owners:** B provider integration; C memory/state/data movement; D device and chip; E materials/energy/cooling; F benchmarks/evidence/economics; G manufacturing; H strategy/publication  
**Status:** EXPERIMENTS DESIGNED / PREREGISTERED DRAFT / NOT EXECUTED  
**Canonical starting main SHA:** `41fac3953773ae0016a09539be57c3ed6b379771`  
**Evidence class at creation:** RESEARCH_DESIGN + SOFTWARE_CONTRACT_INTENT. No new simulation, hardware measurement, GPU benchmark, QPU run, or quantum-advantage result is claimed.

## 1. Mission and interpretation

The research target is **to replace GPU compute capability with quantum processing**, not merely to attach a QPU as a permanent helper to an otherwise unchanged GPU system. The project must investigate whether a small number of high-quality logical qubits, supported by a realizable physical architecture, can perform useful workloads with better total performance and capability than optimized GPU systems.

This is a research objective, not an established result. "A few qubits replace hundreds of GPUs" is a moonshot hypothesis that must be decomposed into workload-specific, falsifiable claims. A quantum state with (n) qubits has (2^n) complex amplitudes in its mathematical state description, but those amplitudes cannot be read out simultaneously as (2^n) classical values. State-space dimension alone is not a speedup proof.

The first proof obligation is therefore not "how many states exist?" but:

> For which accepted useful-output tasks can a quantum algorithm produce the required answer with lower end-to-end time, energy, and total cost than the best fair classical implementation, after accounting for input encoding, state preparation, gates, error correction, shots, measurement, output reconstruction, control, and classical support?

The long-term target remains full GPU replacement. Intermediate evidence may establish only a narrow workload win. Such a result must never be described as general GPU replacement.

## 2. Operational definitions

### 2.1 Functional replacement

For a workload (w), QPU replacement is demonstrated only if the QPU implementation:
1. accepts the same input distribution and problem sizes as the baseline;
2. produces outputs satisfying the same semantic and quality contract;
3. meets the same reliability and service-level constraints;
4. does not rely on an uncounted GPU/CPU service that performs the dominant computation;
5. records all resources and costs required to produce an accepted result.

A **full GPU replacement** claim additionally requires a preregistered portfolio spanning the GPU's relevant workload classes (e.g. dense/sparse linear algebra, AI inference/training, simulation, graphics, analytics, media, and general-purpose control), not one selected algorithm.

### 2.2 Performance and capability

Report separately:
- end-to-end latency and throughput;
- quality/correctness and failure probability;
- energy per accepted useful task and peak power;
- total cost per accepted task and amortized system cost;
- logical/physical qubits, ancillas, gate counts, circuit depth, connectivity and QEC overhead;
- classical CPU/GPU time, RAM/VRAM/HBM, data movement, network and storage;
- supported input sizes and workload coverage.

Never compare GPU FLOP/s or TOPS directly with "quantum operations". Compare completed tasks under identical accepted-output contracts.

### 2.3 Evidence classes

- **THEORY:** mathematical derivation or complexity analysis.
- **LITERATURE_ONLY:** externally reported result, not reproduced here.
- **MODEL_ONLY:** analytic resource model or constructed model.
- **SIMULATION_IDEAL:** ideal circuit/statevector/tensor simulation.
- **SIMULATION_NOISY:** explicitly parameterized noise simulation.
- **SOFTWARE_CONTRACT:** validated semantics, test fixtures or compiler contract.
- **HARDWARE_QPU:** actual target-device execution with job IDs and calibration provenance.
- **GPU_MEASURED:** actual measured optimized classical baseline.
- **SYSTEM_MEASURED:** end-to-end system energy/cost/latency measured.
- **REPLICATED:** independent reproduction under the same frozen contract.

A higher evidence class is not inferred from a lower one.

## 3. Core hypotheses and competing explanations

### H1 — Workload-specific quantum replacement
There exists at least one practically relevant workload family for which a fault-tolerant or sufficiently reliable QPU implementation meets the same output contract and outperforms the strongest fair GPU baseline in end-to-end latency or total cost.

**Falsifiers:** no asymptotic or finite-size crossover after full overhead; state preparation/output dominates; required precision/quality cannot be reached; physical resources or error correction erase the advantage.

### H2 — Small-logical-qubit leverage
For a restricted task family, a relatively small logical-qubit register can encode and process the useful problem representation more efficiently than a classical GPU implementation.

**Competing explanation:** the apparent compression merely moves the cost into state preparation, oracle construction, precision, ancillas, QEC, repeated shots, or output reconstruction.

**Falsifier:** total logical/physical resource and runtime estimates scale unfavorably against optimized classical baselines.

### H3 — Quantum matrix-processing advantage
Block Encoding, QSVT, QSP, or quantum linear-system methods can outperform classical GPU methods on selected structured matrix tasks when the input is sparse/structured and only a compact property or sample of the solution is required.

**Competing explanation:** dense input loading, condition number, normalization, precision, sparsity-oracle cost, and output readout remove the theoretical advantage.

**Falsifier:** the fair end-to-end comparison shows no crossover within the preregistered problem range or output contract requires the full classical vector.

### H4 — Quantum search/optimization advantage
Grover-style amplitude amplification, QAOA or related methods can improve accepted-solution quality per unit total resource on selected search or optimization families.

**Competing explanation:** oracle construction, optimizer evaluations, shot count, embedding/mapping, and classical postprocessing dominate; classical heuristics or exact small-instance methods remain stronger.

**Falsifier:** no statistically credible improvement under equal objective, quality threshold, tuning budget and total-resource accounting.

### H5 — Quantum sampling / amplitude-estimation advantage
Quantum amplitude estimation can reduce sample complexity for selected expectation/Monte-Carlo tasks enough to offset coherent circuit and state-preparation overhead.

**Competing explanation:** noise, deep circuits, state preparation and fault-tolerant costs dominate the sample-complexity gain.

**Falsifier:** equal-error/equal-confidence total cost is not lower than optimized classical Monte Carlo or variance-reduced methods.

### H6 — AI workload replacement
Quantum circuits or quantum-native representations can replace one or more GPU AI kernels or complete AI tasks while preserving model quality, data semantics, and throughput/latency requirements.

**Competing explanation:** data encoding, trainability, measurement, classical optimizer loops and limited output bandwidth make the QPU slower or more expensive.

**Falsifier:** no matched-quality crossover against optimized GPU/NPU baselines; a small kernel speedup does not transfer to whole-graph inference/training.

### H7 — Hardware co-design changes the feasible frontier
Co-design of algorithm, compiler, connectivity, control, QEC, memory and packaging can materially reduce total resources versus a generic circuit mapping.

**Competing explanation:** improvements are local and do not survive full-stack accounting or fabrication/control constraints.

**Falsifier:** target-aware synthesis and physical resource estimates fail to improve accepted-task performance.

### H0 — Classical dominance
For the tested workload and size range, optimized CPU/GPU methods remain superior after all quantum and classical overheads are counted. This is a valid and valuable result, not a failed research process.

## 4. Open questions and uncertainties ledger

Every question must receive a stable ID, owner, evidence class, answer status and next falsifier.

1. **Q-001:** What is the minimum logical-qubit count for each workload under a fixed output contract?
2. **Q-002:** How do state-preparation complexity and data access scale with input size and sparsity?
3. **Q-003:** Which tasks require only an expectation, sample, decision, or compact observable, and which require the full classical output?
4. **Q-004:** What are the actual gate, depth, ancilla, connectivity and precision costs after target-aware compilation?
5. **Q-005:** How many physical qubits and what QEC cycle time are needed for the logical circuit's target failure probability?
6. **Q-006:** Does entanglement provide a useful representational or algorithmic benefit on the target workload, or only increase control/error burden?
7. **Q-007:** Can circuit depth and two-qubit gate count be reduced without changing output semantics?
8. **Q-008:** What is the crossover size against optimized GPU implementations, not a naive CPU or unoptimized GPU?
9. **Q-009:** How many shots/repetitions are required to meet a predeclared confidence interval?
10. **Q-010:** Does measurement/output reconstruction erase the algorithmic advantage?
11. **Q-011:** What is the total energy boundary, including cryogenics/laser/control electronics, classical host and cooling?
12. **Q-012:** Which quantum hardware modality and connectivity graph best fits each workload?
13. **Q-013:** How much of the task can be performed without a GPU after the QPU is introduced?
14. **Q-014:** Can a small logical register cover a useful problem family, rather than a hand-selected toy instance?
15. **Q-015:** What is the effect of fault-tolerance overhead on the claimed crossover?
16. **Q-016:** Are results robust across held-out instances, seeds, device calibrations and compiler versions?
17. **Q-017:** Can a complete AI inference or training graph be run without hidden GPU execution?
18. **Q-018:** Which GPU capabilities are fundamentally outside the tested quantum algorithm's scope?

Do not silently resolve an open question by assumption. Record null, negative and inconclusive outcomes.

## 5. Experiment portfolio — multiple forms

### EXP-00: Semantic and exact-reference controls
**Purpose:** establish that all compared systems solve the same problem. Use tiny cases with exact classical references, invariants, known analytic answers, and complete output comparison.

- Input sizes: smallest nontrivial cases through the exact-reference limit.
- Arms: exact classical reference; independent implementation; circuit-level semantics; decoder/output validation.
- Tests: bit ordering, sign conventions, normalization, boundary cases, deterministic seeds, malformed inputs.
- Pass: all methods satisfy identical semantics and predeclared tolerances.
- Fail: any mismatch blocks performance claims.

### EXP-01: Classical GPU baseline ladder
**Purpose:** prevent weak baselines from creating false quantum wins.

- Arms: optimized CPU; optimized single GPU; multi-GPU where relevant; best established classical algorithm; simple baseline only as a diagnostic.
- Freeze hardware model, GPU count, drivers, libraries, compiler, precision, batch/shape, tuning budget, cache/warmup protocol and correctness.
- Include kernel-only and full application timing, reported separately.
- Record VRAM/RAM/HBM, transfers, launches, host overhead, energy where measurable and software versions.
- Pass: baselines are reproducible and independently checked.

### EXP-02: Ideal quantum algorithm / statevector experiments
**Purpose:** isolate mathematical algorithmic behavior before noise and physical constraints.

- Candidate methods: QSVT/QSP and block encoding; HHL/quantum linear solvers; Grover/amplitude amplification; QAOA; amplitude estimation; selected quantum simulation.
- Use ideal simulation only where the simulator can faithfully represent the circuit.
- Record logical qubits, ancillas, queries, gates, depth, precision, shots (if sampling) and output contract.
- Do not treat statevector simulation as evidence that a physical QPU can execute the circuit efficiently.

### EXP-03: Simulator diversity and applicability
Run the same frozen circuits through multiple simulation families when mathematically appropriate:
- statevector simulation for small general circuits;
- tensor-network/MPS simulation for circuits with exploitable entanglement/structure;
- stabilizer/tableau simulation only for circuits in its supported Clifford/stabilizer scope;
- density-matrix or trajectory simulation for noise, within tractable sizes;
- independent SDK/backend implementation for convention checking.

Record simulator assumptions and unsupported operations. A simulator's speed is not QPU speed and must not be compared as hardware performance.

### EXP-04: Noisy-circuit robustness
Sweep calibrated or explicitly hypothetical noise parameters, gate errors, readout errors, coherence/depolarization models and connectivity constraints.

- Include ideal, nominal, stressed and device-calibration-derived scenarios.
- Apply mitigation only as a separately budgeted arm.
- Report logical output quality, confidence intervals, mitigation overhead, shots, depth and runtime.
- Do not label hypothetical noise parameters as device measurements.

### EXP-05: Quantum matrix engine
**Primary candidates:** block encoding + QSVT/QSP; HHL/linear systems; eigenvalue/expectation estimation.

- Matrix families: dense small matrices; sparse matrices with controlled sparsity; structured/toeplitz or graph Laplacians; controlled condition numbers; positive-definite and Hermitian fixtures where required.
- Vary dimension, sparsity, condition number, normalization, precision and requested output (full vector versus expectation/observable).
- Arms: optimized GPU dense/sparse linear algebra; classical iterative solver; quantum ideal simulator; noisy/compiled circuit; target-resource estimate.
- Record oracle/input-access model and its cost. No free QRAM or free sparse-access oracle assumption.
- Pass only if accepted output and total resources outperform baseline within declared range.

### EXP-06: Search and optimization engine
- Grover/amplitude amplification on oracle-defined search tasks.
- QAOA and alternative quantum optimization on frozen signed-Max-Cut/QUBO fixtures already in the repository.
- Reuse existing 10-instance signed-Max-Cut manifest and exact references; do not create duplicate datasets or change held-out splits.
- Compare against exact solver for small cases and tuned classical heuristics for larger cases.
- Equal objective, constraints, quality threshold, total tuning/optimizer budget, shots and wall-clock boundary.
- Report optimality gap/regret, feasibility, success probability, evaluations and total runtime.

### EXP-07: Sampling and Monte-Carlo workloads
- Candidate tasks: approximate counting, expectation estimation, integral estimation, selected risk/uncertainty calculations.
- Compare quantum amplitude-estimation variants with classical Monte Carlo and variance-reduced baselines.
- Freeze error tolerance, confidence level, distribution, oracle cost and state-preparation cost.
- Pass only on lower total work/energy/cost for equal error and confidence.

### EXP-08: AI and matrix-kernel replacement
Test in increasing scope:
1. isolated dot-product / small matrix kernel;
2. attention subgraph with fixed tensors and accepted numerical tolerance;
3. embedding or similarity search;
4. small inference graph;
5. full small-model inference;
6. training microstep and then bounded full training loop.

Compare optimized GPU and NPU baselines with identical weights/data, precision policy, batch, quality metric and tuning budget. Count encoding, circuit, shots, decoding and optimizer loop. A kernel-only win is not a whole-model replacement.

### EXP-09: Hardware-target and real-QPU experiment
Only after EXP-00..08 produce a justified candidate:
- compile to a named device and frozen calibration snapshot;
- record provider, device, topology, calibration time, transpiler/compiler versions, circuit hash, job ID, queue time, execution time, shots, retries, failures and billed cost;
- compare target-aware simulation and resource estimates with hardware output;
- include host and network orchestration;
- do not submit paid jobs or incur charges without explicit user authorization and a bounded budget.

### EXP-10: Fault-tolerant resource and physical architecture study
For each promising workload estimate logical error target, code distance, physical qubits, syndrome extraction, magic-state factories/non-Clifford resources, cycle time, routing, control channels, cryogenic/laser/control power and packaging. Separate analytical estimates, synthesis outputs and measured device data.

### EXP-11: End-to-end energy, cost and crossover
Construct a complete boundary for GPU and QPU systems:
- acquisition/amortization and utilization;
- electricity and cooling;
- control/cryogenic/laser overhead;
- host compute, memory, network and storage;
- engineering, maintenance, queueing and failure/retry;
- accepted-task throughput and quality.
Report crossover curves over problem size and utilization, not a single cherry-picked point.

### EXP-12: Generalization and adversarial holdouts
Use family-disjoint train/validation/test sets, held-out sizes, seeds, distributions, noise regimes and device calibrations. Preserve all failed cases and test counterexamples that should favor classical algorithms.

## 6. Experimental design variants

The same workload should be studied in several complementary forms:

| Form | What it answers | Evidence boundary |
|---|---|---|
| Analytic/theoretical | Complexity, lower bounds, expected scaling | THEORY |
| Exact small-instance | Semantic correctness and reference answer | SOFTWARE_CONTRACT / MODEL_ONLY |
| Ideal simulator | Algorithmic behavior without noise | SIMULATION_IDEAL |
| Tensor-network/stabilizer | Structured simulation and simulator limits | SIMULATION_IDEAL, scope-limited |
| Noisy simulator | Sensitivity to noise and mitigation | SIMULATION_NOISY |
| Compiler/resource estimate | Gates, depth, ancillas, mapping and QEC estimate | MODEL_ONLY / compiled artifact |
| Real QPU | Device execution under a frozen calibration | HARDWARE_QPU |
| Measured GPU | Fair optimized classical performance | GPU_MEASURED |
| Whole-system test | Accepted-task latency, energy and cost | SYSTEM_MEASURED |
| Independent replication | Robustness and reproducibility | REPLICATED |

## 7. Size sweep and resource accounting

Initial logical-qubit sweep: 4, 6, 8, 10, 12 and 16 where the algorithm and simulator support it. This is a proposed sweep, not a claim that a target device supports these sizes or that these qubit counts suffice. Add larger sizes only when resource estimates and simulator feasibility justify them.

For every circuit, record:
- logical system qubits, ancillas and total logical qubits;
- estimated physical qubits and QEC assumptions, separately;
- one-qubit/two-qubit/non-Clifford gate counts;
- circuit depth, two-qubit depth, routing overhead and connectivity;
- oracle queries, state-preparation gates and data bytes;
- shots, confidence intervals, repetitions and postselection rate;
- compilation, queue, execution, measurement and decoding time;
- host CPU/GPU time and memory;
- energy measured or modeled, with boundary and uncertainty;
- total cost and cost per accepted result.

A small logical-qubit count does not imply a small physical machine. Never mix logical and physical qubit counts.

## 8. Fair comparison and statistical protocol

1. Freeze workload, input hashes, output contract, tolerance, precision and acceptance rule before execution.
2. Select the strongest feasible classical baseline; tune both sides under disclosed, comparable effort.
3. Use the same hardware time boundary: report kernel/circuit execution separately and full end-to-end time.
4. Randomize/interleave runs when thermal drift, queue or calibration drift can bias results.
5. Use repeated runs and report median, spread, confidence intervals and all failures. For stochastic algorithms, report success probability and shots.
6. Hold out entire instance families and problem sizes. Never tune on test data.
7. Compare only accepted useful outputs at equal quality/confidence.
8. Report raw measurements and scripts; no result from a toy instance is generalized without scaling evidence.
9. Preserve null, negative and inconclusive outcomes.
10. Independent verification is required before any replacement or advantage claim.

Primary ratios:
- speedup = baseline end-to-end latency / QPU end-to-end latency;
- energy ratio = baseline joules per accepted task / QPU joules per accepted task;
- cost ratio = baseline total cost per accepted task / QPU total cost per accepted task.

Ratios greater than 1 favor QPU only for the named workload and boundary. Include uncertainty intervals and quality parity.

## 9. Decision gates

- **G0 — Contract valid:** task, input, output and exact reference frozen.
- **G1 — Classical baseline valid:** optimized GPU/CPU baseline reproducible.
- **G2 — Algorithmic feasibility:** quantum method is applicable; no free oracle/data-loading assumption.
- **G3 — Ideal crossover candidate:** ideal resource/runtime model indicates a plausible advantage at a stated size.
- **G4 — Noise/compilation viability:** target-aware gates, noise and error mitigation preserve accepted output.
- **G5 — Physical feasibility:** QEC and physical resource estimates fit a credible target envelope.
- **G6 — Hardware evidence:** actual QPU execution is reproducible and matches the contract.
- **G7 — End-to-end advantage:** time/energy/cost per accepted task beats the fair GPU baseline with uncertainty accounted.
- **G8 — Replacement coverage:** repeated wins cover a preregistered portfolio and remove the GPU dependency for those tasks.
- **G9 — Full GPU replacement:** broad workload coverage, reliability, I/O, memory, programmability and system-level economics are independently demonstrated.

A failure at a gate does not end the program; it identifies the next redesign or a bounded no-go result.

## 10. Initial experiment order

1. EXP-00 + EXP-01: lock exact contracts and GPU baseline harness.
2. EXP-05: select one structured linear-system/matrix task with compact output; compare QSVT/block encoding and classical sparse solvers.
3. EXP-06: reuse frozen signed-Max-Cut fixtures for optimizer/sampler comparison without altering the existing held-out manifest.
4. EXP-07: amplitude-estimation task with a known integral and classical variance-reduced baseline.
5. EXP-03/04: simulator diversity and noise robustness for the leading candidates.
6. EXP-08: start with an attention or embedding subgraph, then whole-graph only if a valid path exists.
7. EXP-10/11: physical and system economics only for candidates passing earlier gates.
8. EXP-09: real QPU only after the evidence and authorization gates.

## 11. Safety, budget and no-claim rules

- No paid QPU job, cloud spend, hardware purchase, hazardous experiment or irreversible external action without explicit user authorization and a bounded budget.
- Do not imply that the repository's existing QSVT or QAOA fixtures prove QPU advantage. Existing QSVT matrix tests are bounded numerical convention checks; existing QAOA parity artifacts are preregistered/model-only exact mapping references unless their specific run evidence says otherwise.
- Do not assume free QRAM, free oracle calls, free state preparation, free error correction, free measurement, or free classical postprocessing.
- Do not claim that (2^n) amplitudes can be independently read out from (n) qubits.
- Do not conflate simulator speed with hardware speed or logical qubits with physical qubits.
- Publish counterexamples and no-go results with the same prominence as positive results.

## 12. Next-agent handoff

A new agent must:
1. read repository `AGENTS.md`, the main-sync policy, permanent cross-lane protocol and this experiment program;
2. inspect current main and existing Lane A QSVT/QAOA artifacts before adding code or fixtures;
3. choose one independent EXP-00/01/05/06 task, freeze its manifest and exact reference, then implement tests;
4. update a dated batch report, Lane A index, README, WORKLOG, RESEARCH_GAPS and integration record;
5. run available tests and exact-head Actions; distinguish pending CI from pass;
6. map source commits to main only after merge; if not merged, record the work as pending and do not claim it is on main.

**Current result:** the experimental program and falsifiable protocol are designed here. No experiment in EXP-00 through EXP-12 has been executed by this document.
