# Research gap RG-A-QUBO-EXACT-REFERENCE-001 — exhaustive small-instance certificates

**Opened:** 2026-10-29  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Cross-lane interfaces:** B provider routes; C memory/state/data movement; F evidence and economics  
**Status:** HELPER + REGRESSION TESTS ADDED; RAG APPLICATION NOT RUN  
**Related:** INV-025/026/029, FND-002, EQN-002/003, Batch 117

## Objective

Provide a deterministic, auditable objective reference for small binary QUBOs before comparing classical solvers, near-memory Ising hardware, QAOA simulation or any authorized QPU target.

## Implementation

`software/uqpu-prototype/uqpu/qubo_reference.py` enumerates all (2^n) bitstrings for (1 le n le 20), under the explicit convention

`E(x) = sum(q_ij * x_i * x_j)`

with each unique term supplied once using (0 le i le j < n). Decimal coefficients are normalized, all optimum bitstrings are retained, and both the normalized problem and the resulting certificate receive SHA-256 hashes. Duplicate/noncanonical terms, invalid coefficients, out-of-range indices and accidental oversized enumeration are rejected. Regression tests cover unique minima, ties, decimal sums, hash stability and validation failures.

## Boundaries and blockers

- The helper certifies the minimum of the declared QUBO objective only. Constraints represented outside that objective must be checked separately.
- Exhaustive enumeration is a small-instance reference, not a scalable solver or evidence of quantum advantage.
- The RAG workload still lacks frozen query/candidate/embedding/QUBO manifests, group-disjoint holdouts, and preregistered downstream-answer acceptance thresholds. Batch 117 therefore remains PREREGISTERED_NOT_RUN.
- No p-DCIM silicon, QAOA simulation, real-QPU job or complete system energy/cost comparison was run by this change.

## Unlock criteria

1. Freeze a synthetic fixture and then a real RAG manifest with hashes for source snapshot, query split, embeddings, QUBO, acceptance contract and target configuration.
2. Independently recompute the exact certificate and verify solver objective, tie set and feasibility.
3. Run CPU/GPU baselines and QAOA simulation on identical QUBO hashes; report downstream quality, latency, throughput, memory/data movement, host work, retries, energy boundary and cost per accepted answer.
4. Keep unknown resource values unknown and model-only results separate from direct-silicon or real-QPU measurements.
5. Consider hardware only after the simulator and acceptance gates pass; paid execution requires credentials, bounded budget and explicit user consent.

## Non-claims

No quantum advantage, 100x/100,000,000x economics, GPU/CPU/NPU or RAM/VRAM/HBM/storage replacement, new physical law, material substitution, accepted bio-oil, net fusion electricity, lower WACC or Data-Center-to-One-Phone completion is established.
