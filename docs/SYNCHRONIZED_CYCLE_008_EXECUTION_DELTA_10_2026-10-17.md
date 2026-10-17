# Synchronized Cycle 008 Execution Delta 10 — Bounded 3/5-Query Prefix Ladder

**Work ID:** `QOS-AUDIT-010B11`  
**Canonical start:** `614de82718888563760b6e1d99de7e7d5a27494c`  
**Primary owner:** Lane A; integration owners F/H; downstream B/C/D/G  
**Evidence:** `SIMULATION_INDEPENDENT_SDK_BOUNDED_PREFIX_CHECK`; hosted SDK/resource gate passed

## Result

The ER6 experiment now has explicit three- and five-query prefixes rather than
an extrapolation from the two-query circuit. For every one of the 64 workload
sectors, the repository evaluates the seven unique normalized eigenvalues with
two separately coded 2x2 recurrences:

1. left-to-right matrix multiplication of `P(phi_0) U_a ... U_a P(phi_q)`;
2. right-to-left state propagation from `P(phi_q)|0>`.

The maximum matrix-versus-state residual across both prefixes is
`3.0436364816617974e-16`, below the frozen `2e-12` tolerance. The contract is
bound to all 82 frozen phases and the unchanged ER6 PREP/SELECT contract.

The hosted job must separately measure logical/decomposed sector residuals,
runtime, traced peak host memory and serialized OpenQASM 2 bytes for each
prefix. It fails closed above `900 s`, `750,000,000 bytes`, `500,000 bytes`, or
the residual tolerance. It stops after the first failing prefix rather than
silently promoting the five-query result.

Exact implementation commit `39fa6f99d6cc512555e5613deb182ed79d054f34`
passed the isolated hosted gate in project run #741:

| Prefix | Max raw sector residual | Runtime | Peak traced host memory | OpenQASM 2 | CX | Depth |
|---|---:|---:|---:|---:|---:|---:|
| 3 queries | `1.7456727791002127e-13` | `203.655504116 s` | `84,791,827 bytes` | `141,919 bytes` | 3,062 | 7,076 |
| 5 queries | `2.7613238692498116e-13` | `342.837898385 s` | `85,003,559 bytes` | `235,806 bytes` | 5,090 | 11,762 |

Both prefixes passed all frozen limits. Artifact `12087010676` is persisted
with commit, run, job and artifact-digest provenance. These remain generic CI
host/circuit measurements, not target-QPU resources or economics.

## A–I and integration status

| Lane | Advance or reviewed blocker |
|---|---|
| A | 3/5-query spectral prefixes pass exact-commit hosted Qiskit and resource gates |
| B | provider-neutral circuit only; submission and paid execution remain disabled |
| C | host memory/serialization limits are explicit but are not RAM/VRAM/storage equivalence |
| D | no calibrated device schedule or error response follows from generic decomposition |
| E | Pangola, BIO-001, FUS-001, materials, cooling and infrastructure reviewed; no new qualified measurement |
| F | per-prefix tolerance/resource ceilings and null economics are executable |
| G | no fab/process-window conclusion before target-specific scheduling and characterization |
| H | cold-start handoff, gaps, decision and publication trail updated; no capital/WACC authorization |
| I | I-012 quiet/high-thrust/minimum-energy matched mission remains `MODEL_ONLY` |

A/F now shares a stop-on-failure prefix ladder. A/B/C shares stable query,
phase, sector and resource fields. D/G remain downstream of target mapping.
E/I retain matched functional-unit/mission gates rather than importing circuit
resource counts as physical-system evidence.

## Literature, foundations and mission boundaries

Fresh surveillance on 2026-10-17 found no primary result newer than the
existing multivariate-QSP and AI-generated-mathematics watches that changes
this bounded experiment. No duplicate literature article was created. The
original QSVT theorem remains the present mathematical basis; external SDK
tutorials are implementation guidance, not project evidence.

FND-001–006, EQN-001–006, BIO-001, FUS-001 and FIN-001 remain active without
evidence promotion. INV-029 gains a bounded reproducible compute gate, not
physical Data-Center-to-Phone compression. INV-030–033 gain no material, fuel,
fusion or finance measurement. INV-034–035 retain assumption, dimension,
symmetry/conservation, counterexample, held-out, proof/experiment and
independent-validation gates. INV-025–027 remain targets.

No provider job, shot, receipt, bill or energy measurement exists. No quantum
advantage, subsystem replacement, >=100x/100,000,000x result, commercial
bio-oil/fusion, lower WACC, vehicle demonstration or new physical law is
claimed.

## Validation and next gate

- Targeted contract suite: 4 passed; optional pinned-Qiskit test skipped locally.
- Full core suite after certificate persistence: 507 passed, 14 optional-dependency skips.
- Cold-start audit: `READY_FOR_COLD_START`, 36 A–I integration pairs.
- Hosted exact-commit project CI #741: passed all nine jobs.
- Cold-start run #17: passed.

The first full audit failed closed because the new
`SIMULATION_BOUNDED_PREFIX_CONTRACT` label was absent from the executable
evidence allowlist. The taxonomy was updated explicitly and the full suite then
passed; the initial failure is retained as a handoff-schema negative result.

Next: use the measured 1/2/3/5-query series to define a preregistered next
prefix and resource-growth falsifier before execution. Degree-81 synthesis,
target-aware mapping and provider execution remain separate gates.
