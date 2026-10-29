# Research gap RG-A-GOAL-ONLY-KERNEL-BASELINE-001

**Opened:** 2026-10-30 · **Owner:** Lane A · **Evidence:** external preprint + synthetic contract tests  
**Status:** CONTRACT IMPLEMENTED / GPU REPRODUCTION NOT RUN

Chen et al., arXiv:2610.36434, report B200 goal-only GPU-kernel results and a same-model comparison whose outcome changes between single-shape and whole-operator scope. No UQPU kernel or B200 run is reproduced.

Gap: prevent unequal model versions, reasoning effort, scope, budgets, target, precision, correctness evaluator or timing protocol from being reported as agent/harness gains. The new standard-library validator checks those fields, goal-only restrictions, per-shape coverage, correctness, independent verification and sanitizer checks. Ten isolated synthetic tests passed.

Unlock: pin source revision and reproduce one single-shape and one whole-operator case with matched goal-only/specialized arms, independent verification and raw per-shape timings. Include JIT, agent/host compute, memory/I/O, throughput, retries, energy if measured and cost per accepted useful operation.

No GPU speedup, QPU advantage, NPU replacement, 100M-unit replacement or mission progress is established.