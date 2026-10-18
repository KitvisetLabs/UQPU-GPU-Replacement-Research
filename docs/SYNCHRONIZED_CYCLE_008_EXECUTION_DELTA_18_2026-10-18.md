# Cycle 008 Delta 18 — Frozen routed-semantics runner

## Scope and result

QOS-AUDIT-010B20 implements the already frozen QOS-AUDIT-010B19 contract. It
reproduces the accepted ten-query circuit and saved-target route, rejects any
routed instruction outside physical wires 0–9, compacts those ten wires,
requires a bijective final-index layout, explicitly restores logical amplitude
ordering, removes one global phase and evaluates the four preregistered product
states. Exact-commit job `117572935487` passed: the four residuals range from
`2.234e-13` to `3.922e-13`, below the frozen `1e-9` stop. The observed final
layout was `[8,7,6,5,0,1,2,3,4,9]`, runtime 83.694 s and traced peak memory
48,643,558 bytes. Artifact `12123870315` preserves the certificate.

The runner always retains a JSON certificate or a tooling/capacity failure.
It enforces the frozen `1e-9` residual threshold, state norms, 1,800-second
runtime, 1.5 GB traced-memory limit and zero credentials/jobs/shots/paid
authority. A passing result will remain a same-SDK bounded probe check, not
full operator equivalence, independent-SDK verification, real-QPU evidence or
useful-output advantage.

## Eight-lane review

- **A:** priority path advanced from preregistration to an executable,
  fail-closed routed-semantics check.
- **B:** saved target only; no service initialization or submission.
- **C:** ten-qubit statevector and host-memory boundary added; no RAM/VRAM/HBM
  replacement inference.
- **D/G:** routing semantics do not establish device/process/factory evidence.
- **E:** BIO-001, FUS-001, Pangola and cooling retain prior evidence classes.
- **F:** full equivalence, accepted useful output, cost and energy remain open.
- **H:** the software-first evidence gate precedes capital expenditure.
- **I:** reviewed and unchanged at `MODEL_ONLY`.

FND-001–006, EQN-001–006, FIN-001 and INV-025–035 remain unpromoted. The
Thai/English/Chinese/Japanese/Korean/German master-plan links and strategic
AI/funding references remain canonical and unchanged.

## Literature delta

The fresh surveillance pass found relevant work on hybrid quantum-circuit
equivalence checking and transpilation-based mutant equivalence, but no new
primary result that changes this project's gate. Neither source converts four
same-SDK state probes into full equivalence, so no duplicate literature-watch
article was created.

## Next gate

Preregister an independently implemented or stronger scalable equivalence
check before any saved-snapshot noise/schedule diagnostic. Four passing
same-SDK probes do not prove the operator. Eleven queries and live/paid QPU
execution remain blocked.
