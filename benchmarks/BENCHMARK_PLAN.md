# UQPU Benchmark Plan

## Principle
Do not compare FLOPS to "quantum operations." Compare completed application tasks end-to-end.

## Tier 1 — Microbenchmarks
Integer add/multiply, fixed-point arithmetic, reversible logic, reduction, search, FFT/QFT variants, linear solve, expectation estimation, sampling, graph search.

## Tier 2 — AI
Small classifier, transformer-attention micrograph, embedding search, small training loop, matrix-chain inference graph.

Metrics: latency/sample, throughput, accuracy, energy estimate, logical qubits, shots, state-preparation time, output reconstruction time.

## Tier 3 — Graphics
Single-ray intersection, batched ray traversal, Monte Carlo integral for one pixel, small path-traced scene, image reconstruction, framebuffer emission.

## Tier 4 — Scientific computing
Sparse Ax=b, eigenvalue problem, Poisson equation, small fluid grid, Ising simulation, molecular Hamiltonian observable.

## Tier 5 — Data analytics
Unordered search, histogram, approximate counting, graph traversal, sort, vector similarity search.

## Tier 6 — Media
Block transform, motion search, entropy-model subproblem, standards-compliant small encode/decode test.

## Baselines
Each benchmark pairs optimized CPU, optimized GPU, naive reversible quantum, and quantum-native candidate implementations.

## Decision record
```text
Functional correctness: pass/fail
Competitive: yes/no
Quantum-native: yes/no
GPU fully removed: yes/no
Dominant bottleneck:
  input / state prep / gates / QEC / shots / measurement / output
```
