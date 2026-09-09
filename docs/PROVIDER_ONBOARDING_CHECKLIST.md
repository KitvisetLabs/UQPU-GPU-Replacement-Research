# Quantum Cloud Provider Onboarding Checklist

Use this checklist for every existing or newly launched provider.

## Level 0 — Registry
- provider ID
- official name
- active/preview/announced/retired status
- paradigm(s)
- official docs/access URL
- SDK/API name
- supported program formats

## Level 1 — Serialization / dry-run
- concrete UQPU adapter exists
- portable program lowers to provider form
- no vendor SDK import leaks into UQPU core
- diagnostics run without credentials
- provider target is explicit

## Level 2 — Credential and SDK health
- provider SDK imports successfully
- credential source is documented
- secrets are not committed
- target discovery succeeds
- account/quota access checked

## Level 3 — Simulator verification
- a minimal diagnostic workload submits
- status polling/result retrieval works
- result normalization works
- actual provider job ID is recorded
- zero/free-cost path is preferred when available

## Level 4 — Real-QPU smoke verification
Requires explicit user consent and budget before submission.
- backend operational
- expected cost checked
- tiny bounded smoke job
- job ID/status/results recorded
- actual billed cost/usage recorded where available

## Level 5 — UQCS benchmark verification
- workload output contract satisfied
- GPU/CPU baseline defined
- state preparation/I/O/retries included
- cloud cost/useful-task calculated
- evidence/reproducibility artifact committed

## Current rule

An adapter can be “software prepared” at Levels 1–2 without claiming real-QPU verification. Real QPU validation requires credentials, account entitlement, target availability and explicit paid-execution approval.

## Aggregator strategy

For hardware providers reachable through Amazon Braket or Azure Quantum, UQPU may use the aggregator adapter as the primary production route. This is intentional: it reduces duplicated authentication, billing and lifecycle code while retaining target-specific capability negotiation.

## New-provider invariant

Provider surveillance is continuous. A newly discovered provider should be added to:
- `providers.py`
- `provider_adapters.py`
- cloud compatibility documentation
- pricing/hardware snapshots where data exists
- adapter tests

before it is considered integrated.
