# Batch 039 — AI-COST-002 Classical AI-Training Baseline

**Gate:** `AI-COST-002`  
**Classification:** `CLASSICAL_AI_TRAINING_ACCEPTED_CAPABILITY_BASELINE_FROZEN`  
**Evidence level:** `EXECUTABLE_CLASSICAL_SOFTWARE_BASELINE_PLUS_ANALYTIC_RESOURCE_LEDGER`  
**Primary lane:** Lane A — Quantum Programming / Workloads / Compiler / Runtime  
**Cross-lane dependencies:** Lane C (memory/data movement), Lane F (benchmark/economics/evidence)

## Research Attribution

- **Research Owner / Principal Investigator / Research Direction:** Kanutsanan Pongpanna
- **Facebook:** https://www.facebook.com/LoveMoneyTH
- **YouTube:** https://www.youtube.com/@LoveMoneyTHOfficial
- **AI Research Agent:** OpenAI GPT-5.6 Sol
- **AI-assisted contribution:** classical baseline design, exact resource-ledger derivation, executable implementation, tests, reference measurement, literature/benchmark-practice check and research documentation.

Attribution reflects roles in this batch only.

## Why this gate exists

Batch 038 established that the moonshot cannot be evaluated by quoting an isolated quantum speedup. A quantum/hybrid route must be compared with a concrete classical workload under the same accepted-capability contract and with resource categories exposed.

Batch 039 therefore freezes the first small, reproducible classical training workload. It is intentionally small enough to run in ordinary CI and simple enough that source-level arithmetic counts and logical tensor payloads can be audited by hand. It is **not** intended to represent frontier-model training.

The design follows the same core benchmarking principle used by MLPerf Training: a training result is meaningful only together with a target quality threshold. As of 2026-09-13, MLPerf Training v6.0 is the current public MLCommons training suite and defines benchmarks by dataset plus quality target while measuring training-system performance. See:

- https://mlcommons.org/benchmarks/training/
- https://mlcommons.org/2026/06/mlperf-training-v6-0-results/

This provenance motivates the quality-gated structure only. UQPU's toy workload is not an MLPerf result and is not comparable in scale to MLPerf frontier workloads.

## Frozen workload

The task is deterministic XOR-quadrant binary classification:

- inputs: two real scalars `x1, x2` sampled uniformly from `[-1, 1]` by a fixed Python RNG seed;
- label: `1` when `x1*x2 >= 0`, otherwise `0`;
- training examples: `256`;
- held-out examples: `256` generated from a distinct deterministic seed;
- model: dense MLP `2 -> 16 -> 1`;
- hidden activation: `tanh`;
- output: sigmoid;
- optimizer: full-batch gradient descent;
- epochs: `800`;
- learning rate: `0.2`;
- trainable parameters: `65`.

The task is deliberately non-linear: a single linear separator cannot represent the quadrant-XOR decision boundary.

## Accepted-capability contract

A candidate implementation must use the frozen train/test examples and satisfy both:

- held-out accuracy `>= 0.98`;
- held-out binary cross entropy `< 0.19`.

The frozen reference execution produced:

- train accuracy: `0.9765625`;
- train BCE: `0.18211116370212715`;
- held-out accuracy: `0.98046875`;
- held-out BCE: `0.17734677266198473`.

The held-out accuracy threshold is therefore met exactly with one extra correct classification beyond 97.65625% on the 256-example held-out set. Later routes must not lower the quality target merely to create an apparent speed/cost advantage.

## Exact source-level training operation ledger

The implementation separates ordinary scalar arithmetic from nonlinear operations instead of pretending all operations have the same hardware cost.

For the complete 800-epoch training run:

| Quantity | Count |
|---|---:|
| training examples processed | 204,800 |
| scalar multiply | 29,595,200 |
| add/subtract | 26,676,000 |
| tanh | 3,276,800 |
| exp | 204,800 |
| division | 204,800 |

These are **algorithm/source-level operation counts**, not CPU instructions, GPU FLOPs, tensor-core operations, energy measurements or wall-clock-equivalent operations.

## Logical FP64 tensor payload / traffic contract

The first memory contract freezes dense payload bytes independent of Python object overhead:

| Quantity | Bytes |
|---|---:|
| parameters | 520 |
| gradients | 520 |
| training dataset | 6,144 |
| streaming activations per example | 136 |
| logical peak streaming payload | 7,320 |
| minimum dataset reads across 800 epochs | 4,915,200 |
| optimizer parameter traffic proxy | 832,000 |

These values are **not measured DRAM/HBM traffic** and are not process RSS. They are logical payload/traffic proxies that the quantum/hybrid comparison must either preserve, replace, compress or explicitly re-account.

## Reference runtime snapshot

A seven-run reference measurement outside repository CI produced a median training wall time of `1.1564624219998905 s` on the reporting environment:

- Python `3.13.5`;
- Linux x86_64;
- CPU reported as `AMD EPYC 9V74 80-Core Processor`.

Runtime samples are frozen in `benchmarks/results/batch039-ai-cost-002-classical-baseline.json`.

This is a measurement of one execution environment, **not** a hardware-neutral performance result. Repository CI is used primarily to verify determinism, quality thresholds and invariants rather than to compare wall-clock performance across runners.

## Explicit cost scenario — model, not measured TCO

To make the accounting interface executable without pretending that unmeasured power is measured, Batch 039 separates runtime measurement from cost assumptions.

Illustrative scenario:

- host power assumption: `65 W`;
- electricity price assumption: `$0.10/kWh`;
- host capital cost assumption: `$500`;
- lifetime assumption: `3 years`;
- utilization assumption: `50%`.

Using the median reference runtime gives:

- modelled energy: `2.0880571508331355e-05 kWh`;
- modelled electricity cost: `$2.0880571508331354e-06`;
- modelled host amortization rate: `$0.0380517503805175/hour`;
- modelled host amortization per run: `$1.2223727612885702e-05`;
- modelled electricity + host amortization: `$1.4311784763718838e-05` per run.

These numbers are classified `MODELLED_SCENARIO_COST_NOT_MEASURED_TCO`. Facility power/cooling, networking, storage lifecycle, labor, software/licensing, financing, reliability/redundancy and data acquisition/curation are excluded. They must be added before any end-to-end economic claim.

## Information gained

`AI-COST-002` converts the AI-training moonshot from an unconstrained aspiration into a comparison interface:

1. **task semantics are frozen**;
2. **quality is frozen**;
3. **training work is executable in CI**;
4. **source-level arithmetic and nonlinear work are auditable**;
5. **memory payload and minimum traffic proxies are explicit**;
6. **runtime measurement is separated from cost-model assumptions**;
7. **future quantum/hybrid routes must include state preparation, measurement/readout and classical residual work**.

The most important consequence is that `AI-COST-003` cannot claim an advantage by comparing quantum kernel time against the entire classical run. It must compare accepted-capability end-to-end ledgers under the same task and quality contract.

## Next gate — AI-COST-003

Reproduce at least one public quantum/hybrid learning route against this exact task contract or an explicitly justified compatible reformulation. The first candidate should maximize information gain rather than expected positive results.

Required ledger:

- classical preprocessing;
- data/state preparation;
- circuit/logical operations;
- shots or amplitude-estimation repetitions;
- optimization iterations;
- measurement/readout;
- classical post-processing;
- memory/state payload;
- provider/simulator/hardware execution provenance;
- accepted held-out quality;
- wall time where meaningful;
- cost model with assumptions separated from measurements.

A result showing that the quantum/hybrid route is slower, more expensive, less accurate, or blocked by loading/readout is a valid research result.

`AI-COST-004` remains the later residual-cost destruction map across compute, memory, data movement, communication, control, energy and lifecycle infrastructure.

## Non-claims

Batch 039 does **not** demonstrate:

- frontier-model or LLM training performance;
- real-QPU AI training;
- quantum advantage;
- a practical quantum-training speedup;
- GPU/NPU/RAM/DRAM/HBM replacement;
- `100,000,000x`, billion-fold or tens-of-billions-fold savings;
- data-center capability for tens of thousands of Thai baht;
- measured end-to-end energy/TCO;
- a new physical law.
