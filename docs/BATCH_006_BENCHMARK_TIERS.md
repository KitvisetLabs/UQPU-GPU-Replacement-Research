# Batch 006 — Benchmark Tiers and Measurement Contract

RG-020 now has a concrete first-pass tier manifest.

| Tier | Variables | ER edge probability | Quality tolerance | Intended gate |
|---|---:|---:|---:|---|
| small | 32 | 0.15 | exact/reference target | correctness + adapter smoke |
| medium | 128 | 0.08 | 2% relative objective gap | optimized CPU scaling + simulator mapping |
| large | 512 | 0.03 | 5% relative objective gap | competitive multicore/GPU + hybrid-QPU economics |

These are RESEARCH STARTING POINTS, not claims of industrial scale or current QPU capacity.

Every serious baseline should preserve contract ID, implementation/solver class, runtime, objective/acceptance, CPU/platform, accelerator, transfer time, peak memory, energy when measurable, and defensible cost/useful-task. Unknown fields remain unknown.

Next gate: integrate an established optimized classical solver, produce measured artifacts, then add a GPU-capable baseline before any serious advantage claim.
