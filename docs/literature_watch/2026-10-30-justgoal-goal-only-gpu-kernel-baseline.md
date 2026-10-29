# Literature watch — goal-only AI baselines for GPU kernel optimization

**Review date:** 2026-10-30  
**Source:** Yaojian Chen et al., “JustGoal: With Only a Goal, the AI Baseline Is Above the Expert Kernels,” arXiv:2610.36434, 2026-10-27. https://arxiv.org/abs/2610.36434  
**Evidence class:** OFFICIAL PREPRINT; PAPER-REPORTED B200 GPU TIMINGS; NOT REPRODUCED BY UQPU  
**Primary owner:** Lane H; implementation owner: Lane A. Interfaces: C, D/G and F; INV-025/026/029/035.

## Novelty

A general-purpose agent receives only the optimization objective and constraints, without kernel-specific knowledge, predefined search workflow or specialized evaluation infrastructure, and builds its own evaluation loop. The authors report 11 operators and 42 shapes on NVIDIA B200. Excluding a DSA top-k comparison with an unverified baseline protocol, JustGoal beats selected open-source kernels on 8 of 10 operators (per-operator geometric means 1.14×–2.34×) and beats the fastest available specialized-agent kernel on 5 of 9 comparable operators.

The key result is scope dependence in a same-model Fable 5.1 comparison: single-shape aggregate 1.18× for JustGoal versus 1.12× for KDA-0.5; whole-operator coverage 0.71× versus 0.97×. Specialized workflow value therefore depends on model version and workload scope; a single-shape win is not whole-operator coverage.

## Limitations

- B200, specific driver/runtime, models, operators and shapes only; no UQPU reproduction or universal agent advantage.
- Other comparisons use different or undisclosed models and do not isolate harness effects.
- The authors disclose two constraint-violating runs (reference-code access by one JustGoal run; a library-kernel call by one KDA run). DSA top-k is excluded from the library comparison because its baseline protocol was unverified.
- Timed kernel intervals exclude JIT, cache flushing and synchronization; end-to-end cost must be accounted separately.
- No energy, cost-per-useful-task, NPU, QPU, fabrication or material result is established.

## UQPU relevance

A provides a control against over-crediting specialized compiler/agent scaffolding in GPU baselines. C must include HBM/VRAM/SRAM traffic, peak memory, transfers and reconstruction. D/G results remain target-specific. F must match model/version, reasoning effort, target, driver/runtime, precision, budget, evaluator and timing protocol, preserve failures, and compute per-shape results. H may use the result as AI-agent strategy context, not funding or R&D-cost evidence.

## Falsifiable follow-up

Pin source revision, prompt, model/version, target, driver/runtime, precision and evaluator. Compare goal-only and specialized arms with identical budgets and shape sets. Keep single-shape and whole-operator scope IDs separate. Independently verify every output and run sanitizers/anti-cheating checks. Preserve raw per-shape latency, JIT/compile, agent compute, host work, memory/I/O, throughput, retries, energy if measured and cost per accepted operation. Compare to the same useful-output contract used by any UQPU candidate.

**Decision:** add a fail-closed contract validator and synthetic tests only. No B200 run, GPU speedup, QPU advantage or 100M replacement claim is made.