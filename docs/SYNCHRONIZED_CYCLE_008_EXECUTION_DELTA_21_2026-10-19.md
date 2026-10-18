# Cycle 008 Delta 21 — Fail-closed real-QPU pilot preregistration

QOS-AUDIT-010B23 binds the accepted Delta 20 independent-simulator certificate
before any live provider contact. It defines a two-phase transition:

1. `NO_SUBMIT_PREFLIGHT` fixes the provider/target, hashes a fresh target
   snapshot and exact submitted circuit, verifies native-gate/topology
   conformance, recomputes the ideal reference, and freezes shots, quality and
   cost ceilings without initializing a live service or submitting a job.
2. `AUTHORIZED_EXECUTION` remains disabled until explicit user consent,
   credentials, provider/target/region, maximum jobs, maximum shots, maximum
   cost, cost estimate and a passing preflight are all recorded.

The future execution record must keep provider-native target, result and price
provenance together. It must record shots, queue/execution/end-to-end latency,
host preprocessing/postprocessing, memory, bytes transferred, retries, quality,
accepted outputs, billable cost and energy-measurement status. Execution
success is not quality acceptance, and cross-provider probability/price joins
are forbidden.

## Evidence boundary

This delta is `MODEL_ONLY_PREREGISTRATION`. Jobs, shots, credentials, service
initialization, submission and authorized cost remain zero, false or null. It
is not real-QPU evidence and does not promote the Delta 20 saved-target result
to hardware fidelity. No paid or free provider job may run under this contract
without a later explicit authorization record.

## A–H and cross-cutting review

- **A:** adds the hardware-transition contract after bounded independent probes.
- **B:** formalizes provider-neutral preflight and provider-consistent provenance.
- **C:** requires payload/result bytes, host memory and data-movement accounting.
- **D/G:** requires a fresh target snapshot and exact native conformance; no
  device, fabrication, yield or factory result is claimed.
- **E:** records energy measurement status but adds no BIO-001, FUS-001,
  Pangola, cooling or infrastructure evidence.
- **F:** freezes cost ceilings, total billable cost, accepted-output denominator
  and fail-closed economics without claiming advantage.
- **H:** preserves software-first capital discipline, auditability and the
  Thai/English/Chinese/Japanese/Korean/German publication context.
- **I / FND / EQN:** remain `MODEL_ONLY`; no equation, hypothesis or physical
  law receives evidence promotion.

INV-025–035 remain binding. Data-Center-to-Phone, universal subsystem/material
replacement, commercial bio-oil/fusion, lower WACC and 100x/100,000,000x goals
remain unachieved. The next gate is to complete the no-submit preflight for one
specified provider/target and seek explicit bounded authorization; execution
cannot begin from this artifact alone.
