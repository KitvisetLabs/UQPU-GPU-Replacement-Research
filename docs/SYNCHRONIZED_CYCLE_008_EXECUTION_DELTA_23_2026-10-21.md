# Cycle 008 Delta 23 — authenticated read-only snapshot preregistration

QOS-AUDIT-010B25 freezes the acquisition and validation contract for the first authenticated **read-only** metadata snapshot of IBM Quantum `ibm_kingston`. It advances the Delta 22 fail-closed candidate without using credentials, initializing an execution service, opening a session, invoking a primitive or submitting a job.

The contract is fixed before any authenticated metadata are observed. A later implementation must capture only allowlisted target metadata, redact account or credential material before persistence, serialize deterministically, compute SHA-256, and pass explicit freshness, structure and counterexample gates. The snapshot may unlock target-specific route construction; it can never authorize QPU execution.

## Frozen snapshot gate

- exact provider and target: IBM Quantum Compute / `ibm_kingston`
- maximum snapshot age at route build: 900 seconds
- canonical UTF-8 JSON with recursive key sorting and field-specific normalization
- required package versions, backend status, target structure, timing constraints and calibration provenance
- directed coupling edges preserved and range checked
- absent provider fields represented as explicit nulls with reasons
- credentials, authorization headers, account identifiers, instance CRNs and private endpoints forbidden
- one-byte digest mutation, stale timestamps, malformed topology and secret-field injection must all fail closed

Passing this gate establishes only that a redacted metadata snapshot was captured reproducibly and was fresh enough for route construction. It does not establish entitlement, queue availability, calibration quality, circuit feasibility, accepted useful output or economics.

## A–I status

- **A:** freezes the metadata input required before rebuilding the ten-query route; no circuit result changes.
- **B:** owns the provider snapshot contract and keeps every submission-capable operation disabled.
- **C:** requires deterministic snapshot bytes and digest accounting; no RAM/VRAM/HBM/storage replacement claim.
- **D:** adds topology, timing and calibration-provenance validation but no device-quality conclusion.
- **E:** BIO-001, FUS-001, Pangola, cooling and infrastructure receive no evidence promotion.
- **F:** preserves fail-closed economics; price, quota, jobs, shots and accepted-output denominator remain absent.
- **G:** exposes topology/timing metadata as a later D/G interface; no fabrication, process-window, yield or factory evidence.
- **H:** preserves the Kanusanan Pongpanna/Ketskaew Chulamani strategy, finance discipline and Thai/English/Chinese/Japanese/Korean/German publication context.
- **I:** no-contact lift remains out of this experiment and `MODEL_ONLY`; no Earth-field or gravity-control claim.

## Foundational and equation-discovery status

FND-001–006 and EQN-001–006 remain unchanged. The generator → constraints → evaluator → held-out test → counterexample → proof/simulation → discriminating experiment → independent replication → device consequence → economics chain remains mandatory. This preregistration generates no alternative physical law and does not weaken incumbent physics.

No material literature delta beyond the already-published Delta 22 surveillance was identified in the repository state reviewed for this contract; therefore no duplicate literature-watch article is created.

## Invariants and evidence boundary

INV-025–035 remain binding. INV-029 gains a reproducible target-metadata gate but Data-Center-to-Phone remains unachieved. INV-030–033 receive no new material, fuel, fusion-electricity, financed-principal, interest-rate or WACC evidence. INV-034/035 retain falsifier, held-out and independent-validation requirements. The 100x and 100,000,000x goals remain unverified.

Evidence class is `MODEL_ONLY_PREREGISTRATION`. Credentials, live service, jobs, shots and authorized cost are zero/false/null.

## Artifacts and next gate

Primary owner: Lane B.

- Contract: `benchmarks/results/cycle008-delta23-er6-readonly-target-snapshot-preregistration.json`
- Upstream canonical commit: `1c43d5c9244ca50ac2d848a4f04594ee0be6d84f`
- Upstream Git blob: `91f8db989553c87aa3dd865fdea74c6a8fcd5996`

The next gate is implementing this contract in an authorized environment, capturing the redacted snapshot, running all failure/counterexample tests and recording a pass/fail certificate. Only after a pass may the exact target-specific route and native-conformance certificate be built. Job submission still requires separate explicit consent with bounded jobs, shots and cost.
