# Synchronized Cycle 008 Execution Delta 11 — Eight-Query Growth Falsifier Preregistration

**Work ID:** `QOS-AUDIT-010B12`  
**Canonical start:** `643b35bb3e3c54cb5bb5822dbe293308ea81f054`  
**Primary owner:** Lane A; integration owners F/H; downstream B/C/D/G  
**Evidence:** `MODEL_ONLY`; experiment and provider execution not performed

## Result

The next ER6 QSVT prefix is frozen at **eight block queries** before execution.
The preregistration consumes only the persisted, provenance-bearing 1/2/3/5-
query certificates and binds their file digests, work IDs and hosted
provenance. A Theil-Sen median pairwise-slope model with median intercept is
used as a robust, deterministic planning falsifier rather than as degree-81
evidence.

The following model-rejection ceilings are now immutable for the eight-query
run:

| Metric | Frozen upper limit |
|---|---:|
| CX | `8,132` |
| decomposed depth | `18,791` |
| decomposed size | `26,129` |
| RZ / SX / X | `15,057` / `2,532` / `408` |
| serialized OpenQASM 2 | `376,658 bytes` |

Runtime and traced memory are retained as diagnostics but excluded from model
acceptance because the four measurements came from shared hosted runners and
do not form a controlled timing/memory experiment. They remain subject to the
absolute stop limits of `900 s` and `750,000,000 bytes`; QASM also retains the
absolute `500,000-byte` stop. Raw logical/decomposed spectral residuals must
remain at or below `2e-12` across all 64 sectors and seven unique eigenvalues.

Exceeding a deterministic model limit rejects the observed near-linear growth
model but does not erase an otherwise numerically valid circuit. Exceeding a
residual or absolute safety limit stops the experiment. Thresholds cannot be
changed after observing the eight-query result.

## A–I and integration status

| Lane | Advance or reviewed blocker |
|---|---|
| A | eight-query prefix and growth falsifier preregistered; execution pending |
| B | provider-neutral/no-submit; jobs and shots remain zero |
| C | host memory and serialization gates remain resource diagnostics, not memory replacement |
| D | no target schedule, calibration or device response follows from this model |
| E | Pangola, BIO-001, FUS-001, materials, cooling and infrastructure reviewed; no qualified measurement added |
| F | separates model rejection from absolute experiment stop and keeps economics null |
| G | no fabrication/process-window conclusion before target mapping and characterization |
| H | preregistration and cold-start handoff reduce post-result discretion; no capital/WACC authorization |
| I | quiet/high-thrust/minimum-energy vehicle work remains `MODEL_ONLY`; I-012 remains open |

A/F share stable query, provenance, metric and acceptance fields. A/B/C share
explicit zero-job/zero-shot and resource-reporting boundaries. D/G remain
downstream of target-aware mapping. E/I continue to require functional-unit or
matched-mission evidence rather than importing circuit planning metrics.

## Literature, foundations and mission boundaries

Fresh surveillance on 2026-10-17 found no primary result newer than the
existing same-day multivariate-QSP and AI-generated-mathematical-instrument
watches that changes this preregistration. No duplicate literature article was
created. FND-001–006, EQN-001–006, BIO-001, FUS-001 and FIN-001 were reviewed
without evidence promotion.

INV-029 gains an auditable compute experiment gate, not physical Data-Center-
to-Phone compression. INV-030–033 gain no material, fuel, fusion or finance
measurement. INV-034–035 retain falsifier, held-out, proof/experiment and
independent-validation requirements. INV-025–027 remain unachieved targets.

No real-QPU execution, quantum advantage, subsystem replacement,
`>=100x`/`100,000,000x` result, commercial bio-oil/fusion, lower WACC, vehicle
demonstration or new physical law is claimed.

## Validation and next gate

- New targeted tests: 6 passed.
- Contract digest: `b4982d043a2cdd0beae0d3be3be83cfd56a7754003de7b4646ff26b4af5a8009`.
- Provider submission and paid execution are explicitly false.
- Negative-result interpretation is predeclared: a model rejection is a useful
  result and cannot be hidden by the absolute experiment gate.

Next: implement the unchanged eight-query prefix in the isolated pinned-Qiskit
job, stop on residual/absolute-limit failure, persist the raw result with
commit/run/job/artifact provenance, and compare it against these frozen model
limits. Do not proceed to degree 81 from a passing eight-query result alone.

