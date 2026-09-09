# Eight-Lane Batch 005 — Representative Optimization Workload Contract

Batch 005 advances RG-019 from a tiny fixed correctness fixture toward reproducible scalable instances.

## What changed
- deterministic weighted Max-Cut -> QUBO conversion;
- seeded Erdos-Renyi instance generation;
- dependency-free greedy bit-flip reference heuristic;
- immutable benchmark contract with stable contract ID and explicit quality tolerance.

## Why this matters
CPU/GPU and QPU paths must consume the same instance family and be judged by the same useful-output contract. A stable contract ID prevents silent benchmark drift.

## Evidence boundary
The greedy heuristic is a software/reference baseline, **not** a competitive GPU baseline. No speedup or cost advantage is claimed.

## Next gate
1. establish representative size/density tiers;
2. integrate an established optimized CPU solver;
3. add a GPU-capable implementation where appropriate;
4. capture runtime, memory, transfer, energy/cloud-price provenance;
5. execute the identical contract through simulator and authorized real QPU/hybrid paths.
