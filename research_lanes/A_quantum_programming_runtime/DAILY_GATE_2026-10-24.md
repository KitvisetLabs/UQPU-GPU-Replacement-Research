# Lane A daily gate — 2026-10-24

**Primary owner:** Lane A — Quantum Programming / Workloads / Compiler / Runtime  
**Priority:** #1  
**Source main SHA:** `c7b5958af58fad04a101ef5c6abf6a29293c867e`  
**Evidence class:** `MODEL_ONLY_PREREGISTRATION` / `BLOCKED_EXTERNAL_AUTHORIZATION`  
**No-submit boundary:** preserved

## Newest canonical state inspected

The current main state retains `QOS-AUDIT-010B25` in `benchmarks/results/cycle008-delta23-er6-readonly-target-snapshot-preregistration.json` as the next hardware-transition gate. It specifies authenticated **read-only metadata capture** for IBM Quantum target `ibm_kingston`, canonical JSON/SHA-256, redaction, freshness and counterexample validation. It explicitly does not authorize service/session initialization, a QPU job, shots, or spending.

The current preregistration still has `freshness_gate_passed=false`, `snapshot_gate_passed=false`, `real_qpu_preflight_passed=false`, zero jobs/shots, and no authorized budget. The latest literature watch did not change those gates.

## Decision

**Status: BLOCKED pending owner-authorized read-only access and exact target evidence.** No credentials are available in this run and no provider connection, session, circuit submission or paid operation was attempted. The blocker is access/authorization and missing live target evidence, not evidence that the route or workload is impossible.

## Required next gate

1. Obtain explicit authorization and a suitable credentialed environment for a read-only metadata query. Do not persist secrets or account identifiers.
2. Capture only the allowlisted target metadata; record UTC capture time and exact client package versions.
3. Canonicalize the snapshot exactly as preregistered; reject NaN/Infinity, malformed or out-of-range qubit/coupling indices, stale timestamps, missing fields without explicit null reasons, digest mismatch, and any credential/account leakage.
4. Run every preregistered negative/counterexample test and publish a redacted snapshot plus SHA-256 and a fail-closed pass/fail report.
5. Only after a fresh snapshot passes, build the target-specific provider-neutral route and native-conformance certificate. Cross-check the same circuit/semantics with an independent SDK and simulator.
6. Preserve the identical useful-output contract and compare against competitive CPU/GPU/NPU baselines with reference/bound certificates. Record accepted quality, throughput, latency, shots, billable usage, retries, reconstruction, host compute, state/I/O/transfer/memory, energy where measurable, and total cost per accepted useful task.
7. Keep real-QPU execution as a separate gate requiring explicit user consent, credentials, bounded shots/jobs and an explicit cost ceiling. Execution success alone is not quality acceptance.

## Cross-lane dependencies

- **B:** exact provider and target identity; provider-specific probability and price must never be mixed across targets.
- **C:** state/input/output bytes, memory materialization, transfer and reconstruction.
- **D/G:** target topology, basis, timing and calibration only after a fresh authorized snapshot.
- **E/F:** power/cooling and full lifecycle cost are unmeasured; retain them as unknown rather than zero.
- **H:** do not escalate capital on a target-independent simulation or unaccepted output.
- **FND/EQN:** equation discovery can prioritize offline hypotheses but does not bypass target or physics gates.

## Non-claims

No real-QPU result, quantum advantage, accepted workload win, RAM/VRAM/storage replacement, 100× or 100,000,000× advantage, data-center-to-phone physical compression, new physical law, or measured economics is claimed.
