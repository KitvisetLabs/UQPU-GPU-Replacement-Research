# EXP-DESIGN-002 implementation delta — offline plan contract

**Date:** 2026-10-24  
**Primary owner:** Lane A — quantum programming, workloads, compiler and runtime  
**Cross-lane owner:** Lane F — evidence and matched-budget economics  
**Canonical main base:** c7b5958af58fad04a101ef5c6abf6a29293c867e  
**Research branch before this delta:** d89e150d4a1d1984450d3f96a4d7b0e93ebbd0ab  
**Status:** SCHEMA GUARD IMPLEMENTED; FULL BENCHMARK NOT EXECUTED  
**Evidence class:** SOFTWARE_CONTRACT / UNIT_TEST

## Change

Added a dependency-free, offline-only contract in **software/uqpu-prototype/uqpu/experiment_design.py** and regression tests in **software/uqpu-prototype/tests/test_experiment_design.py**.

The validator requires:
- a declared incumbent and alternative model, the exact changed assumption, a typed observable/unit, predictions under both models, uncertainty, a held-out prediction, acceptance predicate and explicit falsifier;
- separate, valid SHA-256 hashes for training, validation and held-out splits;
- named simulator/model versions, hard feasibility constraints and an independent replay method;
- finite, nonnegative resource counters, nonnegative integer counts and explicit separation of unknown energy from zero energy;
- the human, information-gain and AI-proposed planner roles under the identical declared budget cap;
- zero provider jobs/cost and zero instrument time, with OFFLINE_SIMULATION and MODEL_ONLY fixed as non-promotable defaults.

This is a fail-closed schema/feasibility gate. It does not run an AI planner, simulate a physical experiment, decide equation truth or authorize any instrument or provider.

## Validation performed before commit

An isolated scratch unit suite for the new module passed **8/8 tests**. It covers valid plans, split-hash separation, observable-unit mismatch, invalid/non-finite counters, budget overruns, hard-constraint violations, forbidden live modes, unknown-vs-measured energy, planner-role coverage and identical matched caps.

The new commit still requires exact-head GitHub Actions. A scratch test pass is not a substitute for repository CI.

## Remaining EXP-DESIGN-002 gate

The actual benchmark remains NOT EXECUTED. Next:
1. freeze the known-law/noisy/held-out/non-identifiable fixture and hashes;
2. run the fixed human plan, information-gain plan and an actual AI-proposed plan with the same generation, simulator, wall-time, CPU/GPU, transfer, retry, reconstruction and replication caps;
3. include generator inference/training costs and energy where measurable;
4. retain false discoveries, counterexamples and failed runs;
5. independently replay the accepted result and report cost per accepted held-out discriminating result.

No paid model inference, real instrument, provider contact or QPU job was used in this delta.
