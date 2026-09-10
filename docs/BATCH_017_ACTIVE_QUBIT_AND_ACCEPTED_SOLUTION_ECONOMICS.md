# Eight-Lane Batch 017 — Active-Qubit Calibration and Accepted-Solution Economics

Date: 2026-09-10

## Executive result

Batch 017 connects the target-snapshot simulation to two stricter evidence layers:

1. calibration properties are now extracted only for the physical qubits and instruction instances actually used by the routed circuit;
2. output probability is converted into a shot budget and a provider-pricing-aware cost primitive for an **accepted useful result**, rather than treating every QPU shot as equally useful.

No real QPU was executed and no quantum advantage is claimed.

## Active physical-qubit result

The deterministic FakeKingston transpilation for the 3-qubit triangle fixture selected physical qubits:

`[108, 109, 110]`

Used routed operations:

| Operation | Count | Snapshot error summary on used instances | Duration |
|---|---:|---|---:|
| CZ | 9 | min/median/mean/max = 0.00111852 / 0.00111852 / 0.00125969 / 0.00143615 | 68 ns |
| measure | 3 | 0.00573730 / 0.00781250 / 0.00769043 / 0.00952148 | 2.28 us |
| SX | 21 | 0.000167898 / 0.000215605 / 0.000227774 / 0.000333505 | 32 ns |
| X | 1 | 0.000167898 | 32 ns |
| RZ | 19 | target metadata reports 0 | 0 |

These are **saved FakeKingston snapshot properties**, not live calibration. Instruction errors must not simply be multiplied and presented as complete circuit fidelity.

## Snapshot-noisy accepted-output result

For the same triangle contract:

- ideal optimum probability per shot: `0.9942078993800392`;
- FakeKingston/Aer snapshot-noisy optimum probability: `0.98095703125`;
- probability retention fraction: `0.9866719343727786`;
- expected independent shots to obtain one optimum sample: `1.0194126431060229`.

Under an independent Bernoulli interpretation of this snapshot-simulation probability, the minimum shot budgets for at least one optimum sample are:

| Confidence | Minimum shots |
|---|---:|
| 95% | 1 |
| 99% | 2 |
| 99.9% | 2 |
| 99.99% | 3 |

This high probability is specific to a tiny 3-qubit correctness fixture. It is not evidence that useful industrial workloads require only a few QPU shots.

## Provider-pricing-aware economics primitive

New module: `uqpu.quality_adjusted_cloud_cost`.

For providers using task + shot pricing, the model computes:

`P(success in n shots) = 1 - (1-p)^n`

`submission cost = task fee + n * shot fee`

`expected cost per accepted solution = submission cost / P(success in n shots)`

It can search a bounded range of shot counts for the lowest expected cost while respecting provider minimum-shot and minimum-success constraints.

For time-priced providers, a separate path requires **measured billable QPU seconds** plus accepted-output probability. Shot count alone is insufficient.

## Current public pricing structures checked

Amazon Braket currently documents on-demand QPU pricing as a per-task fee plus a device-specific per-shot fee, or hourly reservation pricing. Its current page lists a common `$0.30` on-demand task fee and device-specific shot prices; examples include Rigetti Cepheus at `$0.000425/shot`, IQM Garnet at `$0.00145/shot`, and IonQ Forte at `$0.08/shot`. IonQ error mitigation on Braket requires a minimum 2,500 shots per task.

Source: https://aws.amazon.com/braket/pricing/

IBM Quantum currently documents Open, Pay-As-You-Go, Flex, Premium and On-Prem plans. Open Plan provides a limited free QPU-time allowance; paid plans account for QPU usage/time through the selected instance. Therefore IBM dollar economics must be populated from measured billable QPU usage and the applicable account plan rather than inferred from the number of shots alone.

Sources:
- https://quantum.cloud.ibm.com/docs/en/guides/plans-overview
- https://quantum.cloud.ibm.com/docs/en/guides/manage-cost

IBM also reports the September 2026 `ibm_phoenix` Nighthawk r2 system with 120 programmable qubits, >100,000 MCPS and up to 25x higher throughput than Heron. That makes throughput-normalized accepted-output economics an important future routing variable, but it is not yet measured for the Batch-017 workload.

Source: https://quantum.cloud.ibm.com/docs/en/guides/changelog-quantum-compute-service

## Cross-provider warning

The FakeKingston success probability must **not** be combined with Rigetti/IQM/IonQ shot prices and called a real provider cost result. Probability is target- and calibration-dependent. Current pricing snapshots are used here to construct the accounting machinery only.

## Subsystem-replacement connection

The new compute/state service contracts make INV-025/026 stricter:

- GPU/CPU replacement needs accepted quality **and** throughput/latency equivalence;
- RAM/VRAM/storage replacement needs capacity **and** access/bandwidth/latency/retention/persistence/recovery semantics;
- financial advantage is evaluated only after the useful-function contract passes.

This prevents a 100,000,000x arithmetic ratio from being mistaken for 100,000,000-unit functional replacement.

## Eight-lane status

| Lane | Batch-017 progress | Next gate |
|---|---|---|
| A | QAOA target-aware accepted-output probability now feeds a cost primitive | larger meaningful workload + real QPU |
| B | pricing-model distinctions and active physical target are explicit | live/authorized target snapshot and execution |
| C | executable compute/state equivalence contracts | measured state/data movement |
| D | used physical-qubit/gate calibration becomes a device requirement signal | live calibration and hardware-specific bottleneck |
| E | no new material claim; functional-unit qualification remains mandatory | sourced component comparison |
| F | accepted-solution economics instead of raw-shot economics | competitive CPU/GPU + actual billed QPU cost |
| G | active-gate error/duration data can feed metrology/process requirements | correlate process/device variables with yield/error |
| H | capital gates can now use accepted-output economics rather than raw execution count | first quantified go/no-go capital threshold |

## Next highest-value experiments

1. run the same target-aware pipeline for a bounded 6-qubit fixture and quantify how accepted-solution shot burden scales;
2. calculate quality-adjusted cost only with a provider-matched probability and pricing model;
3. obtain competitive CPU/GPU throughput/cost measurements for the identical useful-output contract;
4. obtain explicit authorization/credentials/budget for a bounded real-QPU experiment;
5. feed real QPU job ID, billable usage, result quality, retries and host overhead into the existing verified-win and 100M-unit gates.

**Evidence status:** CALIBRATION_SNAPSHOT_SIMULATION + SOFTWARE/ECONOMIC MODEL.  
**REAL_QPU:** no.  
**Quantum advantage:** not demonstrated.  
**>=100x / >=100,000,000x cost advantage:** not demonstrated.
