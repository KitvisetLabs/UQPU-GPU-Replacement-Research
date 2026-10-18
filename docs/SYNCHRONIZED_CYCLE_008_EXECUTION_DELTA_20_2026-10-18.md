# Cycle 008 Delta 20 — Independent routed-probe execution

QOS-AUDIT-010B22 implements the immutable Delta 19 contract from canonical
start commit `588500f647bb42a43549a5ce38072198f61071ab`. Qiskit 2.5.2 reproduces
the frozen ten-query source and saved-target route; Qulacs 0.6.14 receives only
explicit complex matrices for `X`, `SX`, `RZ` and `CZ`.

## Local measured result

- Four probe residuals: `2.218e-13`, `3.205e-13`, `3.945e-13`, `3.333e-13`
- Frozen threshold: `1e-9`; observed gate set: `cz/rz/sx/x`
- Final layout inverted: `[8,7,6,5,0,1,2,3,4,9]`
- Routed size: 187,979 operations on ten compact qubits
- Runtime: 48.289 s; traced peak memory: 101,543,937 bytes
- Provider jobs/shots: `0/0`; cost and energy: not measured

Reversed RZ, perturbed SX, altered CZ mapping and omitted layout inversion were
all rejected. Swapping the two endpoints of the same CZ was null, as required
by `CZ(q0,q1) = CZ(q1,q0)`; the result is preserved rather than mislabeled as a
detectable physical defect.

Evidence class is `SIMULATION_INDEPENDENT_SDK_BOUNDED_ROUTED_PROBE_CHECK`.
This is not full operator equivalence, hardware fidelity, real-QPU execution,
energy/cost evidence, quantum advantage, eleven-query feasibility or subsystem
replacement evidence. Exact-commit hosted confirmation remains pending.

## Cross-lane and invariant review

- A gains a bounded independent-simulator result; stronger equivalence remains open.
- B remains provider-neutral, saved-target and no-submit.
- C records only host state/runtime/memory; no RAM/VRAM/storage equivalence.
- D/G gain no chip, process, yield, packaging or factory conclusion.
- E gains no BIO-001, FUS-001, Pangola, cooling or commercial evidence.
- F retains null economics and all accepted-output gates.
- H retains software-first finance/publication discipline and six-language context.
- I remains `MODEL_ONLY`; I-012 remains open.

FND-001–006, EQN-001–006, FIN-001 and INV-025–035 remain unpromoted. No
AI-generated equation is a physical law, and no Data-Center-to-Phone,
100x/100,000,000x, universal-material, bio-oil, fusion or WACC goal is claimed
as achieved. The same-day literature sweep produced no gate-changing primary
delta, so no duplicate literature-watch article is created.
