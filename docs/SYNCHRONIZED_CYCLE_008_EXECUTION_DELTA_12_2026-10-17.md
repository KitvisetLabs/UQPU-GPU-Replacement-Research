# Synchronized Cycle 008 Execution Delta 12 — Preregistered Eight-Query Execution

**Work ID:** `QOS-AUDIT-010B13`  
**Canonical start:** `b1ed8b6da28d04fa3bfc97348f50d9000ccd4db0`  
**Primary owner:** Lane A; integration owners F/H; downstream B/C/D/G  
**Evidence:** hosted `SIMULATION_INDEPENDENT_SDK_BOUNDED_PREFIX_CHECK`

## Implemented experiment

The repository now has a dedicated eight-query ER6 QSVT runner bound to the
immutable QOS-AUDIT-010B12 preregistration. It:

1. validates the preregistration digest and its measured 1/2/3/5-query inputs;
2. independently compares left-to-right 2x2 matrix recurrence with
   right-to-left state propagation over the seven unique ER6 eigenvalues;
3. constructs the ten-qubit eight-query circuit with nine projector phases;
4. checks all 64 projected workload sectors before and after generic basis
   decomposition in pinned `qiskit==2.5.2`;
5. records raw residuals, gate counts, depth, size, QASM bytes, runtime and
   traced host memory;
6. evaluates the frozen growth-model limits separately from absolute stop
   limits; and
7. keeps provider jobs/shots at zero and cost/energy null.

A new isolated `qsvt-eight-query` CI job has a 25-minute wall-clock limit and
uploads its certificate even when the experiment fails. A deterministic metric
exceedance rejects the local growth model but is retained as a useful negative
result; residual, absolute-resource, basis or authorization failures make the
experiment fail closed.

## A–I and integration status

| Lane | Advance or reviewed blocker |
|---|---|
| A | eight-query implementation and independent recurrences prepared; hosted certificate pending |
| B | provider-neutral/no-submit; provider jobs and shots fixed at zero |
| C | runtime/memory/QASM recorded as host-resource evidence only |
| D | generic circuit is not a calibrated device schedule or requirement response |
| E | Pangola, BIO-001, FUS-001, materials/cooling reviewed; no new qualified measurement |
| F | model rejection, absolute stop and null economics remain separate executable outcomes |
| G | process-window and factory conclusions remain blocked until target mapping/characterization |
| H | branch/PR handoff records exact pending status; no capital/WACC authorization |
| I | I-012 matched quiet/high-thrust/minimum-energy vehicle model remains open and `MODEL_ONLY` |

## Literature, foundations and mission boundaries

Fresh surveillance on 2026-10-17 found no primary publication newer than the
existing QSP and equation-discovery watches that changes this eight-query
experiment. No duplicate literature article was created. FND-001–006,
EQN-001–006, BIO-001, FUS-001 and FIN-001 were inspected without promotion.

INV-029 gains a bounded compute falsifier, not physical Data-Center-to-Phone
compression. INV-030–033 gain no new material, fuel, fusion or finance
measurement. INV-034–035 retain dimensional/symmetry/conservation,
counterexample, held-out, proof/experiment and independent-validation gates.
INV-025–027 remain targets.

No real-QPU execution, quantum advantage, subsystem replacement,
`>=100x`/`100,000,000x` result, commercial bio-oil/fusion, lower WACC, vehicle
demonstration or new physical law is claimed.

## Hosted result and next gate

- Exact source commit `b1ffc1de9c2a0b02d80886e548d1d4fe6be17213`
  passed all ten jobs in project run #745. The PR merge test commit was
  `00401e0a2d2fa223b16bca50f88853c87dc0f875`.
- Across 64 sectors, the maximum raw residual was
  `5.491292372342266e-13`, below the frozen `2e-12` tolerance. Independent
  matrix/state recurrence disagreement was `4.440892098500626e-16`.
- Generic decomposition measured 8,132 CX, depth 18,791, size 26,129 and
  376,644 QASM bytes. All deterministic growth limits passed; QASM was only
  14 bytes below its frozen model ceiling.
- Host runtime was `525.450692110 s` and traced peak memory was 85,858,826
  bytes. These are runner diagnostics, not portable performance evidence.
- Artifact `12094185194` and digest
  `sha256:6ea35e9525a49dd1838ae8662b591a8ee470c77c306c1f740f5b6713951b53c7`
  are persisted with run/job/source/merge provenance.
- Paid/provider execution remains disabled.

Next: preregister the next bounded boundary test only after using the measured
eight-query result to prove it remains below the unchanged absolute runtime,
memory and 500,000-byte QASM stops. Do not authorize degree 81, target/provider
execution or economics from this passing prefix.

