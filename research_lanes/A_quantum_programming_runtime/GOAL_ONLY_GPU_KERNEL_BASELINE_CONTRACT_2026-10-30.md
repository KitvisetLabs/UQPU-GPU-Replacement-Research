# Lane A contract — goal-only versus specialized GPU-kernel agents

**Date:** 2026-10-30 · **Work item:** RG-A-GOAL-ONLY-KERNEL-BASELINE-001  
**Source:** arXiv:2610.36434 · **Status:** CONTRACT IMPLEMENTED / 10 SYNTHETIC TESTS PASS / GPU REPRODUCTION NOT RUN

## Objective

Prevent a specialized workflow from receiving credit for a gain caused by a stronger model, larger budget, different scope, target, precision or evaluator.

## Matched fields

Both arms must match model ID/version, reasoning effort, GPU target, driver/runtime, operator, scope ID, complete shape set, budget, precision, correctness protocol, timing/cache protocol and reference-code access. Single-shape and whole-operator runs are different scope IDs.

The goal-only arm must not receive kernel-specific knowledge, a kernel-specific evaluator, a predefined search workflow or reference implementation code.

## Acceptance

Require at least three raw latency samples per declared shape, independent semantic correctness, independent verification and sanitizer/anti-cheating checks. Return per-shape medians and a declared geometric mean only when every shape is covered and every shared field matches. Reject the comparison without reporting speedup if any condition fails.

Record JIT/compile, warmup, host orchestration, GPU time, throughput, peak VRAM/RAM, HBM/SRAM traffic, transfer bytes/time, launches, retries, failures, energy when measured, agent/model inference cost and cost per accepted useful operation. State whether the timed interval excludes synchronization, cache flushing, JIT or host overhead.

For QPU comparisons, retain the same accepted useful-output contract and include state preparation, shots, billable usage, reconstruction, host compute, memory/I/O, energy and total cost. Never mix probability from one provider/target with another provider's price. NPU comparisons require real neural-workload semantics, quality, precision, latency, throughput, memory/data movement and cost, never TOPS alone.

Implementation: software/uqpu-prototype/uqpu/agent_baseline.py. Tests: software/uqpu-prototype/tests/test_agent_baseline.py. Ten isolated synthetic tests passed; no GPU benchmark or JustGoal reproduction is claimed.