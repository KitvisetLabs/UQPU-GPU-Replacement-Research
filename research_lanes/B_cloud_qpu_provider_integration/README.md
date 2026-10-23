# Lane B — Quantum Cloud / QPU / Provider Integration

## Scope
Cloud-QPU access, provider adapters, SDK/API compatibility, target discovery, routing, calibration/runtime metadata, simulator/dry-run paths and real-QPU evidence.

## Integration responsibilities
B executes or validates A workload contracts; accounts for C transfer/state requirements; returns target constraints to D/G; feeds infrastructure observations to E; supplies billable/runtime/quality evidence to F; and informs H provider/deployment strategy.

Future provider/program subfolders are allowed subject to the 16-level depth limit.


## Current gate — 2026-10-23

QOS-AUDIT-010B25 remains open. The pure offline validator is software/uqpu-prototype/uqpu/er6_readonly_snapshot.py. The original 12 focused tests passed locally under Python 3.13 before a 13th strict-timestamp regression test was added; the updated full suite awaits hosted Python 3.10–3.12 CI. No IBM credentials, live service/session, target snapshot, job, shot or billable execution was used. A saved fake-backend snapshot is not a substitute for authenticated current metadata.

Only an owner-authorized read-only snapshot may enter the validator. A pass may unlock target-specific route construction; it never authorizes QPU submission. See docs/BATCH_057_READONLY_SNAPSHOT_OFFLINE_VALIDATOR_AND_LITERATURE.md.
