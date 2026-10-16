# Synchronized Cycle 008 Execution Delta 07 — One-Query QSVT Projector Phase

**Work ID:** `QOS-AUDIT-010B8`  
**Canonical start:** `bb7db2ec35ef2476d99beabf9717f2230f425971`  
**Primary owner:** Lane A; integrations B/C/F/H and downstream D/G  
**Evidence:** `SIMULATION_PROVIDER_NEUTRAL_ONE_QUERY_CONTRACT`; local optional-SDK check pending exact-commit hosted confirmation

## Result

The repository now defines the bounded mathematical fragment

`P(phi_0) U_ER6 P(phi_1)`, with `P(phi)=exp(i phi (2 Pi-I))` and
`Pi=|0000><0000| tensor I_system`.

The fragment binds the first two entries of the unchanged 82-phase fingerprint
to the unchanged ER6 PREP/SELECT contract. Its projected block must equal the
ER6 normalized cost diagonal multiplied by `exp(i(phi_0+phi_1))`. Provider
submission and paid execution remain false.

Local Qiskit 2.5.2 validation passed the logical projected fragment at
`5.6158631957729706e-14`, the generic-basis projected fragment at
`3.6061746050468526e-14`, and full decomposed-vs-logical operator agreement at
`7.75091532099517e-14`, all below `2e-12`. The local generic decomposition had
1,034 CX, 1,911 RZ, 320 SX and 58 X gates, depth 2,390, size 3,323 and 48,035
OpenQASM 2 bytes on ten logical qubits. These environment measurements require
exact-commit hosted reproduction before becoming a provenance-bound certificate.

This validates one phase/query/phase convention only. It does not prove that
the complete degree-81 sequence has the intended transformed block, and its
resource counts must not be multiplied by 81 and presented as a synthesized
end-to-end circuit.

## A–I status

| Lane | Advance or reviewed blocker | Evidence boundary / next gate |
|---|---|---|
| A | One ER6 query is composed with the frozen multi-ancilla projector phases | hosted exact-commit reproduction, then bounded two-query recurrence |
| B | Circuit stays provider-neutral and no-submit | dated target-aware transpilation only after composed-operator gates |
| C | Ten logical qubits and serialization/host fields are explicit | no RAM/VRAM/storage equivalence; measure controlled I/O/transfer later |
| D | Projector-control structure is now visible | no device requirement without target schedule/calibration |
| E | Pangola, BIO-001, FUS-001, materials, cooling and infrastructure reviewed | no new material/fuel/net-electric measurement |
| F | Raw operator residual and null provider/cost/energy fields are acceptance gates | no accepted-task economics or advantage |
| G | Generic controlled-phase decomposition is visible | no process-window/factory conclusion without target mapping |
| H | Cold-start report and literature decision are publishable | no capital, WACC or investment claim |
| I | I-012 remains the deterministic matched-mission gate | no levitation/propulsion demonstration; `MODEL_ONLY` |

## Foundational, equation-discovery and mission integration

FND-001–006 and EQN-001–006 were inspected without promoting a model, fit or AI
equation to physical law. The projector-phase definition makes an incumbent
unitary assumption and discriminating matrix observable explicit; it does not
alter physics. BIO-001, FUS-001 and FIN-001 remain model-gated.

INV-029 receives a more exact useful-compute primitive but no physical
compression result. INV-030–033 receive no new commercial materials, fuel,
fusion or finance evidence. INV-034–035 retain their falsification and
independent-validation gates. INV-025–027 remain unachieved moonshots.

The tested integration edge is A/F: an operator convention is accepted only by
raw projected/full-matrix residuals. A/B/C exposes a serializable no-submit
contract; A/D/G remains blocked until target-aware data exists. The fresh
multivariate-QSP source is retained as `LITERATURE_ONLY`, not project evidence.

## Validation and handoff

- Core suite: 489 tests passed; 12 optional-dependency skips.
- Isolated local Qiskit 2.5.2: four focused tests passed.
- Hosted exact-commit pinned-Qiskit job: passed in run #735; full workflow target-noise job pending at certificate-preparation time.
- No provider job, shot, execution ID, bill or energy measurement exists.

Next: publish and require exact-commit pinned-Qiskit CI. If raw residuals pass,
persist a provenance-bearing certificate; then verify a two-query recurrence
against an independently assembled matrix before attempting all 81 queries.

## Hosted verification checkpoint

Commit `9d7e5d761fc8ddf18a0fec4a9564ce836e617e96` passed the pinned-Qiskit job in
project run #735. Hosted residuals were `5.4646887015828417e-14` logical
projected, `3.6424960685225636e-14` decomposed projected and
`7.593998529073269e-14` full decomposed-vs-logical. Artifact `12072606869`
records 1,034 CX, depth 2,390 and zero jobs/shots with null cost/energy.
Cold-start run #11 and all eight jobs in project run #735 passed, including
target-snapshot-noise. This is exact-commit CI and still not provider execution.
