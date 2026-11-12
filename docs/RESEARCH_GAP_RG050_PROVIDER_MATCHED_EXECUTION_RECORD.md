# Research Gap RG-050 — provider-matched execution-record validation

**Opened:** 2026-10-26  
**Primary owner:** Lane F — economics, benchmarks, evidence and integration  
**Implementation owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Cross-lane dependencies:** B — provider identity and billing; C — state, transfer and host-memory accounting  
**Status:** IMPLEMENTED / SYNTHETIC_TESTS_PASS / REAL_QPU_DATA_CREDENTIAL_BLOCKED  
**Evidence class:** SOFTWARE_CONTRACT + SYNTHETIC_TEST_FIXTURES

## Objective

Make it difficult to compute or report cost per accepted useful QPU output from incompatible provider, target, workload, circuit, calibration or billing records. A valid schema is necessary for evidence discipline, but is not proof that a bill, calibration snapshot, result or provider claim is authentic.

## Current implementation

The new dependency-free module is:

- software/uqpu-prototype/uqpu/provider_matched_execution_record.py
- software/uqpu-prototype/tests/test_provider_matched_execution_record.py

The validator requires matching provider, target, region, execution route, workload contract, circuit digest, target snapshot digest and target snapshot timestamp across execution, quality/probability and billing sections. It also checks that the execution and quality records use the same calibration snapshot/time and that billed job IDs match executed job IDs.

The record explicitly captures shots, accepted outputs, the frozen quality metric/threshold/direction, actual billable cost and currency, pricing provenance, queue/execution/end-to-end latency, host preprocessing/postprocessing, host peak memory, bytes sent/received, retries, and energy-measurement status. It rejects inconsistent quality flags, invalid hashes/timestamps, non-HTTPS pricing references, malformed costs and impossible shot/output counts.

**Zero accepted outputs means cost per accepted useful output is undefined, not zero.** For a positive accepted-output count, the derived ratio is actual billable cost divided by accepted outputs. This arithmetic does not convert MODEL_ONLY, SIMULATION, DRY_RUN or synthetic data into real-QPU evidence.

## Validation completed locally

The isolated dependency-free unit suite passed 14/14 tests on the research environment. Cases include valid same-target records; provider/target/circuit/calibration/job-ID mismatches; invalid probabilities and shot counts; invalid pricing URL and negative cost; quality-threshold inconsistency; cost-ratio mismatch; and the zero-accepted-output boundary.

This is local unit-test evidence only. Exact-head GitHub Actions validation remains pending, and no provider service was initialized or contacted.

## Unlock criteria

1. Freeze the exact workload/output contract, circuit hash, target identity, target snapshot and calibration snapshot.
2. Obtain credentials and explicit user consent for a bounded real-QPU run; set maximum jobs, shots and cost before submission.
3. Record actual job IDs, provider/target, pricing source and observation time, billable cost, quality metric and accepted outputs in one identity-matched record.
4. Include retries, host compute, I/O/transfer, memory, reconstruction, energy where measurable and the full accepted-output threshold.
5. Compare against a competitive classical baseline under the identical useful-output contract.
6. Independently review the result and preserve failed/no-output runs as negative evidence.

## Cross-lane and mission boundary

- **Lane A:** the record validator closes a software-contract gap; it does not show an algorithmic speedup or quantum advantage.
- **Lane B:** provider and target provenance are explicit; credentials and live execution remain unavailable/not authorized in this cycle.
- **Lane C:** memory and byte-transfer fields become mandatory inputs to future system accounting; no memory or data-movement saving is measured.
- **Lane F:** the same-task cost denominator and evidence class remain explicit.
- **INV-029:** no data-center-to-phone service, physical-compression, energy or lifecycle-cost closure.
- **INV-033:** no project principal, interest, time-to-evidence or WACC change.
- **INV-034/035:** this is a mathematical/software evidence guard, not a new physical law.

No paid or free QPU job was submitted. Paid QPU execution remains disabled unless the required credentials, bounded budget and explicit user consent are present.
