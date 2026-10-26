# Research gap RG040 — FND-001 finite-state objective is not yet an accepted-task or physical-energy benchmark

**Date opened:** 2026-10-26  
**Status:** Open — exact mathematical evaluator validated; physical and task-quality bridge absent  
**Primary owner:** Lane F  
**Implementation interface:** `software/uqpu-prototype/uqpu/finite_state_memory.py`  
**Preregistration:** `research_lanes/F_economics_benchmarks_evidence_integration/FND001_FINITE_STATE_POLICY_PREREGISTRATION_2026-10-26.md`  
**Latest result:** `benchmarks/results/fnd001_finite_state_heldout_2026-10-26.json`

## Known

- The finite-state joint transition matrix is constructed from a fixed policy, memory-update kernel and environment kernel.
- A normalized stationary distribution is solved directly; non-unique stationary laws fail closed.
- Six local unit tests passed, including a memoryless invariant-channel limit and a closed-form stationary-distribution check.
- Twelve deterministic Monte Carlo checks across four held-out transition values were within 0.02 bits/round of the exact stationary objective.
- The frozen toy-policy objective ranking did not reverse on the four held-out values.

## Unknown / blocking

- No matched useful-task semantics, acceptance threshold or task-quality distribution is specified.
- No physical memory implementation, bytes, state movement, erase/write count, latency, throughput or host reconstruction is measured.
- No physical work protocol is implemented; the entropy difference is an idealized model objective, not measured joules or demonstrated work extraction.
- No CPU/GPU/NPU baseline, real-QPU result, provider bill, energy measurement or cost per accepted task is available.
- The selected policy family is not optimized and does not establish a universal ranking. The observed ordering must not be generalized beyond this toy environment.

## Falsifiable next gate

1. Freeze one accepted useful-output contract with a minimum quality threshold and exact workload semantics.
2. Implement matched MEMORYLESS, PREDICTIVE and BOUNDED_MEMORY policies that all satisfy the same quality gate on held-out environment seeds/parameters.
3. Record physical memory bytes and movement, action/state I/O, latency, throughput, retries, reconstruction and host compute.
4. Measure energy at a declared boundary and report total cost per accepted useful task. If a physical information engine is used, measure work and heat with calibrated uncertainty and close the thermodynamic accounting.
5. Independently reproduce the result and report policy-rank reversals, false discoveries and failures. Do not infer device energy from entropy bits alone.

**Stop rule:** if quality is mismatched, the result is MODEL_ONLY; if rankings disappear or reverse, report the failure without tuning on held-out data; if physical energy or accepted-task economics is missing, do not claim efficiency advantage.
