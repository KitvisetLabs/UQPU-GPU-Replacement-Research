# Synchronized Cycle 008 Execution Delta 13 — Ten-Query Boundary Preregistration

**Work ID:** `QOS-AUDIT-010B14`  
**Canonical start:** `d8dfd72cd3b8e5dc78a63809170663f74fa03b04`  
**Primary owner:** Lane A; integration owners F/H; downstream B/C/D/G  
**Evidence:** `MODEL_ONLY` immutable preregistration

## Result

The repository now binds the provenance-bearing 1/2/3/5/8-query certificates
and scans integer query counts 9 through 81 without changing the established
absolute stops. A Theil-Sen envelope plus three times the maximum observed
absolute residual selects ten queries as the largest planned prefix below all
unchanged ceilings.

| Boundary | Conservative upper | Frozen ceiling | Outcome |
|---|---:|---:|---|
| 10-query QASM | 470,551 bytes | 500,000 bytes | eligible |
| 10-query runtime | 716.865 s | 900 s | planning-eligible |
| 10-query traced memory | 187,377,521 bytes | 750,000,000 bytes | planning-eligible |
| 11-query QASM | 517,495 bytes | 500,000 bytes | blocked before execution |

The ten-query deterministic limits are 10,160 CX, depth 23,477, size 32,645,
18,813 RZ, 3,164 SX and 508 X. Residual tolerance remains `2e-12` across 64
sectors and seven unique eigenvalues. Provider submission and paid execution
remain false. Contract digest:
`47ad5e62cbae93fb613fd3d3a1a3a464f09c06b6eb3e54b2a5e3fabcc39795aa`.

## A–I, foundations and mission boundaries

| Lane | Advance or reviewed blocker |
|---|---|
| A | ten-query experiment boundary selected and frozen; no result yet |
| B | provider-neutral/no-submit; jobs, shots and budget remain zero |
| C | host memory/runtime/QASM are planning envelopes, not replacement evidence |
| D | no calibrated target schedule or device requirement is inferred |
| E | Pangola, BIO-001, FUS-001, materials/cooling reviewed; no new measurement |
| F | unchanged absolute stops and source provenance are executable controls |
| G | no fabrication/process-window conclusion before target characterization |
| H | autonomous handoff and publication trail updated; no capital/WACC claim |
| I | I-012 quiet/high-thrust/minimum-energy model remains open and `MODEL_ONLY` |

FND-001–006, EQN-001–006, BIO-001, FUS-001 and FIN-001 were inspected without
promotion. Fresh surveillance on 2026-10-17 found no primary result newer than
the existing same-day QSP/equation-discovery watches that changes this boundary
experiment, so no duplicate literature article was created.

INV-029 gains a bounded compute stop, not Data-Center-to-Phone compression.
INV-030–033 gain no new material, fuel, fusion or finance measurement.
INV-034–035 retain dimensional, symmetry, conservation, causality, held-out,
counterexample, proof/experiment and independent-validation gates. INV-025–027
remain unverified targets.

No ten-query execution, degree-81 feasibility, real-QPU result, quantum
advantage, subsystem replacement, `>=100x`/`100,000,000x`, commercial
bio-oil/fusion, lower WACC, vehicle demonstration or new physical law is
claimed.

## Validation and next gate

Four targeted tests cover source binding, exact boundary selection, frozen
limits and mutation rejection. Next: implement the unchanged ten-query runner
and isolated pinned-Qiskit job, then retain either acceptance or failure with
raw residual/resource provenance. Eleven queries remain blocked unless a new
representation lowers measured serialized size without changing useful-output
semantics or evidence thresholds.
