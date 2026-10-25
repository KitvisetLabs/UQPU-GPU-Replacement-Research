# Pending-main sync — 2026-10-26 FND-003 gate-level quantum speed limits

**Status:** PENDING REVIEW / NOT MERGED INTO MAIN  
**Canonical repository:** `KitvisetLabs/UQPU-GPU-Replacement-Research`  
**Main base SHA at audit:** `5fbe3d295ad6ca5b7c701f05c64899829910cbe8`  
**Source PR:** [#55 — FND-003 thermodynamic speed-limit literature and falsifiable test contract](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/pull/55)  
**Source branch/head at this handoff:** `research/2026-10-24-fnd003-thermodynamic-speed-limits` @ `6179dc52c6f350048d119e0897c760705c7e1b87`  
**Source commit:** [6179dc52c6f350048d119e0897c760705c7e1b87](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/commit/6179dc52c6f350048d119e0897c760705c7e1b87)  
**Research-Sync:** pending-main until reviewed/merged.

## What the source PR adds

- `software/uqpu-prototype/uqpu/gate_speed_limit_contract.py`: provenance-bound gate-QSL record validation and uncertainty-interval classification. It does not derive a theorem from an abstract or promote a below-bound observation to new physics.
- `software/uqpu-prototype/tests/test_gate_speed_limit_contract.py`: 10 focused tests for hashes, scope checks, evidence labels, numeric validity, interval classification and audit semantics.
- `docs/literature_watch/2026-10-26-gate-level-quantum-speed-limits.md`: two official APS accepted-paper records (Nelson & Barnes, accepted 2026-10-15, DOI 10.1103/28zn-ch8y; Stepanenko et al., accepted 2026-10-21, DOI 10.1103/rsjw-pk53), limitations and falsifiable follow-up.
- `research_lanes/D_device_chip_fabrication_packaging/FND_003_GATE_LEVEL_SPEED_LIMIT_CONTRACT_2026-10-26.md`: Lane-D primary contract.
- `integration/INT-20261026-001-GATE-QSL.json`: machine-readable A–H integration and mission-boundary record.

## Method and observed results

The new literature sharpens FND-003 by motivating gate-/operator-specific QSLs under explicit Hamiltonian/control assumptions. The full accepted-paper derivations were not available in the accessed APS records, so no theorem formula was implemented. The software contract requires a theorem-source hash and a separate bound-derivation hash, explicit gate/target/calibration provenance, scope checks and uncertainty intervals.

**Local focused test result:** 10 passed, 0 failed in an isolated Python standard-library unittest harness using the committed module/test content. This is a software-contract result only.

**Hosted CI:** run `40215812473` for source head `6179dc52c6f350048d119e0897c760705c7e1b87` was `queued` at last poll. Previous source head `180ce23207a57b3bd91bb39eaf9461f7df3646f9` passed run `40053421690`, but that earlier pass does not validate the new files. Current main's combined-status query returned no status records; success cannot be inferred. Source PR #55 still uses an older base SHA `c7b5958af58fad04a101ef5c6abf6a29293c867e`, so refresh/rebase and exact-head CI are required before merge.

## A–H and foundational status

- **A:** gate/unitary identity interface added; no workload speedup or accepted-task advantage.
- **B:** provider-neutral/no-submit; no credentials, provider calls, paid QPU jobs or shots.
- **C:** no readable classical memory/storage equivalence; host, output and I/O remain separate.
- **D:** gate-QSL record/uncertainty contract added; no physical timing/calibration measurement.
- **E:** no Pangola material, accepted bio-oil, net fusion electricity or cooling measurement.
- **F:** provenance-bound interval classifier added; no energy, lifecycle cost, principal, interest or WACC result.
- **G:** D/G co-design remains downstream of validated native schedules and calibration; no fabrication/process result.
- **H:** literature publication and handoff; six-language master-plan context and recorded strategic AI/funding references remain preserved.

FND-001 has no erasure/heat/wall-plug measurement; FND-002 has no new output-information lower bound; FND-003 has a better measurement contract but no project timing/energy result; FND-004 has no demonstrated alternative primitive; FND-005 has no new QFT/particle mechanism or credible anomaly; FND-006 remains mathematics-first; EQN-001..006 remain evidence-gated. BIO-001, FUS-001 and FIN-001 gain no new commercial or measured evidence.

## INV-029–035 boundary

- **INV-029:** no Data-Center-to-One-Phone service, physical-support, energy or lifecycle-cost contract passed.
- **INV-030:** no Pangola-carbon substitution/recovery or critical-material reduction; no transmutation claim.
- **INV-031:** no accepted liquid fuel or cost-per-delivered-energy result.
- **INV-032:** no reliable net delivered fusion electricity or lifecycle-cost result.
- **INV-033:** no measured principal, interest, time-to-evidence or WACC effect.
- **INV-034:** a falsifiable gate-level control-bound path is specified; current physical constraints remain binding.
- **INV-035:** no generated formula is promoted to physical law; theorem assumptions, units, falsifiers and independent validation remain mandatory.

INV-025/026/027, root directives 00–06, and Thai/English/Chinese/Japanese/Korean/German master-plan links remain preserved. The 100×/100,000,000× targets, universal subsystem replacement, low-cost bio-oil/fusion and Data-Center-to-Phone remain goals.

## Next actions

1. Wait for exact-head CI on source PR #55 and recheck the result.
2. Refresh/rebase the source branch against current main; resolve any conflicts and rerun the full suite.
3. Obtain the full accepted-paper derivation, independently reproduce small-gate examples and only then implement a numerical theorem-specific bound.
4. Freeze matched target, gate/unitary, Hamiltonian spectral width, control boundary, calibration, environment and timing uncertainty before any physical measurement.
5. Keep paid QPU execution disabled unless explicit user consent, credentials and a bounded budget are present.
6. Keep Lane A's equivalent-useful-output CPU/GPU/NPU comparison as Priority #1 while continuing meaningful A–H and FND/EQN work.

No QPU job, physical experiment, material purchase, funding or external spending was performed or authorized.
