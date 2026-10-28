# Pending-main sync — FND-002 output accounting

**Date:** 2026-10-26  
**Canonical main base SHA:** 5fbe3d295ad6ca5b7c701f05c64899829910cbe8  
**Source PR:** #112 — FND-002: integrate output-information and reconstruction accounting  
**Source branch:** research/2026-10-26-fnd002-output-accounting  
**Source head at sync-record creation:** f50d99310a0563565fe30476cc36e651b022840f  
**Work item:** FND002-OUT-001  
**Integration record:** INT-FND002-OUTPUT-ACCOUNTING-20261026-001  
**Status:** PENDING_MAIN_REVIEW; source implementation is not merged and must not be treated as canonical main.

## What the source PR proposes

- Add output-information contract semantics for distinguishable accepted outcomes, exactness/error budget, uniform-prior assumption, side-information provenance, encoding mode and output rate.
- Add per-accepted-result output bytes, reconstruction time, side-information bytes, measured result rate and measured error.
- Integrate the contract into WorkloadContract and BenchmarkRunPlan with fail-closed validation.
- Add 15 focused tests and a dated A–H cycle report plus a machine-readable integration record.

## Files on the source branch

- software/uqpu-prototype/uqpu/output_accounting.py
- software/uqpu-prototype/uqpu/workload_contracts.py
- software/uqpu-prototype/uqpu/benchmark_pipeline.py
- software/uqpu-prototype/tests/test_output_accounting.py
- docs/DAILY_CYCLE_2026-10-26_FND002_OUTPUT_ACCOUNTING.md
- integration/INT-FND002-OUTPUT-ACCOUNTING-20261026-001.json

## Validation and evidence boundary

GitHub Actions run #1476 for the source head was queued at the last check, with Python 3.10/3.11/3.12 jobs not yet completed. This is pending, not a pass. No local repository suite was run. No QPU job, external spending, physical experiment, material substitution, accepted fuel, net-electric fusion, financing effect, new physical law or Data-Center-to-Phone outcome is claimed.

The new contract treats information-theoretic bounds as output-semantics constraints only. It does not infer readable memory capacity from Hilbert-space dimension or convert bits directly into energy/cost.

## Invariants and lane disposition

INV-025/026/027 and INV-029–035 remain preserved. Lane C owns the FND-002 contract; Lane A implements the workload/benchmark integration; Lane F owns evidence and cross-lane integration; Lane H owns publication. Lanes B, D, E and G were explicitly reviewed in the dated cycle report and remain active.

## Canonical README pointer sync debt

The top README checkpoint still names Batch 062 while Batch 063 is the latest canonical batch and is referenced later in the README. Do not overwrite the large README from a partial read; reconcile its top pointer with a focused, hash-checked edit after review.

## Required next action

Review and merge the source PR only after exact-head Python 3.10/3.11/3.12, invariant and cold-start checks pass. After any merge, record all source-SHA-to-main-SHA mappings and update the canonical handoff without overwriting the append-only RESEARCH_GAPS.md or WORKLOG.md.
