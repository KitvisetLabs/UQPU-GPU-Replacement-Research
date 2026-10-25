# RG-050 Lane F contract — provider-matched execution records

**Primary owner:** Lane F  
**Implementation:** Lane A  
**Work item:** RG-050  
**Integration record:** integration/INT-20261026-RG050-PROVIDER-MATCHED-EXECUTION.json  
**Gap record:** docs/RESEARCH_GAP_RG050_PROVIDER_MATCHED_EXECUTION_RECORD.md

## Required accounting boundary

A cost-per-accepted-useful-output result must bind the execution, quality/probability estimate and billing record to the same provider, target, region, route, workload contract, circuit digest and target snapshot. The calibration snapshot and timestamp used for probability must match the execution record; billed job IDs must match the executed job IDs.

The machine validator is software/uqpu-prototype/uqpu/provider_matched_execution_record.py. Its contract is structural and provenance-oriented: it does not contact providers, authenticate invoices, validate physical calibration or promote evidence.

## Required measurements

Record shots requested/completed, quality metric and frozen threshold, accepted-output count, actual billable cost/currency, pricing source and observation timestamp, queue/execution/end-to-end latency, host preprocessing/postprocessing, peak host memory, bytes sent/received, retries, and energy status/value when measured or estimated.

Cost per accepted output is actual billable cost divided by the number of outputs that passed the frozen useful-output gate. When that count is zero, the cost per accepted output is undefined and must remain null; it must not be recorded as zero.

## Acceptance tests and evidence status

The isolated test suite covers matching records, provider/target/circuit/calibration/job identity mismatches, invalid probabilities/shots, pricing URL/cost errors, quality-threshold consistency and the zero-output boundary. Fourteen local unit tests passed in the research environment. Exact-head GitHub Actions checks remain pending; no live provider or QPU was contacted.

## Gate to real evidence

Require a frozen workload contract and competitive classical baseline, exact target and calibration snapshots, official pricing provenance, explicit user consent, credentials and a predeclared bounded budget. Preserve failed/no-output runs. Do not combine probability or price from different providers/targets, and do not treat execution success as quality acceptance.
