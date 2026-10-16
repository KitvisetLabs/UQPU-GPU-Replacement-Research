# Synchronized Cycle 008 Execution Delta 08 — Two-Query QSVT Recurrence

**Work ID:** `QOS-AUDIT-010B9`  
**Canonical start:** `7b36280809d89416822e68e0de6a952bb4855dca`  
**Primary owner:** Lane A; integration owners B/C/F/H; downstream D/G  
**Evidence:** `SIMULATION_INDEPENDENT_SDK_TWO_QUERY_CHECK`; hosted exact-commit raw-matrix certificate persisted

## Result

The repository now defines and executes the bounded recurrence

`P(phi_0) U_ER6 P(phi_1) U_ER6 P(phi_2)`.

The expected 1024x1024 operator is assembled separately from the circuit order:
the verified ER6 primitive is combined with explicit dense projector-phase
diagonals using row/column scaling and two matrix products. This reference then
checks the logical circuit and its generic-basis decomposition.

Local pinned Qiskit 2.5.2 passed:

- logical full operator vs independent assembly: `1.487709209519727e-14`;
- logical projected block: `6.4373790806034785e-15`;
- decomposed full operator: `1.555229087579905e-13`;
- decomposed projected block: `1.4686258498911463e-13`;
- acceptance threshold: `2e-12`.

The generic circuit has ten logical qubits, two block queries, three projector
phases, 2,048 CX, 3,789 RZ, 636 SX and 108 X gates, depth 4,733, size 6,581 and
94,965 OpenQASM 2 bytes. Provider jobs/shots remain zero; cost and energy remain
null. Exact-commit hosted Qiskit 2.5.2 reproduced the result in run #737.
Hosted logical full/projected residuals were `1.5372480116112342e-14`/
`9.031103035004427e-15`; decomposed full/projected residuals were
`1.5525801392484516e-13`/`1.4696065413280135e-13`. Artifact `12075997394`
is bound to commit `2bf019cf21efd43ec7ae9f8196ec03e5734e7945` and job
`117198147300`. Hosted serialization was 94,969 bytes; jobs/shots remain zero
and cost/energy null.

## A–I status

| Lane | Advance or reviewed blocker | Boundary / next gate |
|---|---|---|
| A | two-query ordering and raw decomposition agree with independent dense assembly | verify projected spectral-sector recurrence, then bounded prefix ladder |
| B | provider-neutral serialization only | no submission; dated target mapping remains downstream |
| C | query/register/serialization/host memory fields exposed | no RAM/VRAM/storage equivalence |
| D | deeper control burden is measurable generically | no calibrated device requirement |
| E | Pangola, BIO-001, FUS-001, materials and cooling reviewed | no new qualified material/fuel/net-electric result |
| F | independent assembly, raw residual and null economics enforced | no accepted-task cost or advantage |
| G | generic gate growth visible | no process-window or factory evidence without target mapping |
| H | handoff, gap and decision records updated | no capital or lower-WACC claim |
| I | I-012 matched quiet/high-thrust/minimum-energy mission remains open | `MODEL_ONLY`; no vehicle demonstration |

## Foundational, equation-discovery and mission integration

FND-001–006 and EQN-001–006 were inspected. The recurrence exposes an explicit
mathematical falsifier—raw operator disagreement—but creates no new physical
law. BIO-001, FUS-001 and FIN-001 remain model-gated. No new primary literature
found in the dated surveillance changed the prior multivariate-QSP decision or
RG-034 identifiability experiment; the existing literature remains
`LITERATURE_ONLY`.

INV-029 gains a more reproducible computational primitive, not physical
Data-Center-to-Phone compression. INV-030–033 gain no new materials, fuel,
fusion or financing measurement. INV-034–035 retain dimensional, symmetry,
held-out, falsification and independent-validation requirements. INV-025–027
remain unachieved research targets.

## Integration and validation

The tested A/F edge is circuit order versus an independently assembled operator.
A/B/C shares the stable query/register/serialization contract. D/G receive
generic requirements only and remain blocked from fabrication conclusions.

- Full core suite after certificate persistence: 495 passed, 13 optional-dependency skips.
- Isolated local Qiskit 2.5.2: recurrence passed.
- Cold-start audit run #13: passed.
- Hosted project run #737: all eight jobs passed, including pinned Qiskit and
  downstream target-snapshot-noise.

Next: compare the projected 64-state block against independently derived
2x2 spectral-sector recurrences. Do not jump from two queries to an 81-query
resource or performance claim.
