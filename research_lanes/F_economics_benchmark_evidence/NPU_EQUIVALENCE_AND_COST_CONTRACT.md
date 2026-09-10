# NPU Equivalence and Cost Contract

**Primary owner:** Lane F — Economics / Benchmark / Evidence / Integration  
**Upstream:** Lane A NPU replacement track  
**Status:** ENGINEERING / ECONOMIC FRAMEWORK

## Purpose

Prevent false NPU-replacement claims based on peak TOPS, operation counts or isolated kernels.

## Accepted-output contract

For an NPU comparison, record at minimum:

- workload/model/checkpoint identity;
- dataset/input corpus and preprocessing;
- numerical precision/quantization;
- accepted quality/accuracy/loss/perplexity/task metric;
- batch, sequence and tensor dimensions;
- end-to-end latency distribution;
- useful accepted outputs per second;
- warmup/compile/setup time where relevant;
- host CPU/GPU/NPU assistance;
- RAM/VRAM/HBM/storage/network traffic;
- failed/retried executions;
- QPU shots/repetitions and mitigation/QEC;
- output decoding/reconstruction/verification;
- energy where measured;
- provider billing or hardware amortization;
- total cost per accepted useful output.

## Replacement ratio

For an agreed workload contract, define useful-throughput replacement as:

`R_capacity = accepted_conventional_NPU_capacity_required / accepted_UQPU_system_count`

and economic advantage as:

`R_cost = total_conventional_cost_per_accepted_output / total_UQPU_cost_per_accepted_output`.

The extreme target is `R_capacity >= 100,000,000` when the UQPU system count is one logically unified system, and `R_cost >= 100,000,000`.

These two ratios must not be conflated: a system might replace many devices without achieving the same cost ratio, or achieve a cost ratio on a workload that does not require 100 million physical NPUs.

## Baseline rule

The conventional side must use a competitive, workload-appropriate NPU/runtime rather than a naive reference implementation. CPU/GPU baselines may be retained as additional context, but they do not substitute for an NPU baseline when the claim is specifically NPU replacement.

## Evidence boundary

No ratio may be marked VERIFIED from theoretical complexity, simulator timing, qubit count, state-space size, vendor TOPS, roadmap projections or unpriced QPU resources alone. Verified status requires equivalent useful output and reproducible end-to-end measurements.
