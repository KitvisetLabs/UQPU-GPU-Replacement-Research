# RG-028 — Provider-Matched Accepted-Solution Economics

Status: DATA/CREDENTIAL_BLOCKED / PARTIALLY_IMPLEMENTED  
Date: 2026-09-10

## Objective

Measure total cloud-QPU cost per **accepted useful solution** using success probability and billing data from the same provider, target, calibration period, workload contract and execution route.

## Current implementation

The repository now has:
- target-snapshot accepted-output probability for a bounded IBM FakeKingston/Aer experiment;
- active physical-qubit calibration extraction for that routed snapshot circuit;
- `accepted_solution_economics.py` for shot/confidence budgets;
- `quality_adjusted_cloud_cost.py` for task+shot and time-priced accounting;
- official dated provider-pricing snapshots elsewhere in the repository.

## Blocker

The current success probability is a saved IBM fake-backend snapshot simulation. It is not valid to combine that probability with another provider's per-shot price and present the result as a measured cloud cost.

For IBM/time-priced execution, actual billable QPU usage is required. For Amazon Braket task+shot targets, a target-specific accepted-output probability and actual task/shot billing are required.

## Unlock criteria

At least one bounded real-QPU execution must provide:
1. exact workload/contract ID;
2. provider and target identity;
3. calibration/execution timestamp;
4. shots or billable QPU usage;
5. accepted-output rate/quality;
6. retries/mitigation/classical orchestration;
7. actual provider charge or auditable billing calculation;
8. competitive classical baseline under the same useful-output contract.

## Next experiment

Choose the cheapest scientifically useful provider-matched route after credentials and explicit budget consent are available. Simulator/snapshot work can optimize the circuit first, but cannot close this gap.

## Evidence boundary

No >=100x or >=100,000,000x financial advantage is demonstrated until this gap and the competitive-baseline gaps are closed with end-to-end evidence.
