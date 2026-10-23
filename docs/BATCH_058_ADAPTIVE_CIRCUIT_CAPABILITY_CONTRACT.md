# Eight-Lane Research Batch 058 — adaptive-circuit capability contract

**Date:** 2026-10-23  
**Canonical main at cycle start:** \`c7b5958af58fad04a101ef5c6abf6a29293c867e\`  
**Working PR branch at cycle start:** \`719332433d7457fc99c009edc777db2817f5fdb2\`  
**PR:** [#48 — Cycle 008 Delta 24](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/pull/48)  
**Status:** Code and documentation proposed on the open PR branch; hosted CI pending for the resulting head.

## Objective

Advance Lane A with an explicit, provider-neutral adaptive-circuit capability interface, informed by a peer-reviewed report of mid-circuit measurement/reset/feedback on up to 100 qubits. Preserve the software-first route and avoid converting external experimental evidence into UQPU execution or economic evidence.

## Changes

1. Added \`uqpu.adaptive_circuit_contract.AdaptiveCircuitCapability\`.
2. Added 15 focused adversarial unit tests covering evidence-class separation, unknown capability fail-closed behavior, target/source provenance, strict UTC timestamp syntax, SHA-256 shape, contradictory limits, invalid latency, and explicit non-claims.
3. Added the integration contract describing stable fields and the simulator/dry-run-first acceptance path.
4. Added a dated literature watch for the Nature Physics adaptive monitored-circuit experiment.
5. Appended this batch, the live research-gap record and WORKLOG entry without removing prior history.
6. Updated Lane A/B workspaces and the README checkpoint. Root directives, multilingual strategic references and INV-025–035 are preserved.

The 15 new tests passed in an isolated Python 3.13 harness using the same module/test source. This is not a full repository test run. The exact-commit GitHub Actions workflow was queued for the previous PR head; the latest commit still requires hosted CI.

## Literature delta

Pokharel et al., *Order from chaos with adaptive circuits on quantum hardware*, Nature Physics, published 2026-10-09; arXiv:2509.18259. The experiment reports up to 100 qubits, nearly 5,000 entangling gates and nearly 5,000 non-unitary mid-circuit operations. The useful UQPU delta is a stricter runtime/provider capability contract for measurement, reset and classical conditionals.

The study is not general fault-tolerant error correction, a UQPU run, a provider capability certificate, or an accepted useful-task/cost result. Its large data/simulation package is available on request rather than as a complete public reproduction bundle. See [the literature watch](literature_watch/2026-10-23-adaptive-circuits-and-mid-circuit-feedback.md).

## A–H status

| Lane | Status this cycle | Evidence and next gate |
|---|---|---|
| A — Quantum programming/workloads/compiler/runtime | Advanced | Added dynamic-circuit capability contract and 15 adversarial tests. Next: integrate into semantic lowering and run deterministic branch tests. |
| B — Cloud/QPU/provider integration | Advanced at interface level | Target-specific official-source evidence is required; no provider is declared supported by this artifact. Next: populate the capability matrix without credentials or submission. |
| C — RAM/VRAM/HBM/storage/data movement | Preserved | Measurement records and feed-forward state must be counted; no quantum-state/classical-memory equivalence. |
| D — Quantum/photonic/semiconductor devices | Research-only | Control timing and calibration remain target-specific; no device/fabrication evidence. |
| E — Biomass/materials/bio-oil/fusion/cooling | Reviewed, no new physical evidence | BIO-001/FUS-001 remain unqualified; no material, fuel, electricity or cooling claim. |
| F — Economics/benchmarks/evidence/integration | Advanced | Contract separates documented capability from hardware evidence and accepted-task economics. No advantage or financing result. |
| G — Manufacturing equipment/factory systems | Research-only | D/G co-design remains active; manufacturing consequences require measured target requirements. |
| H — Strategic plan/publication/finance | Advanced | Published experiment and limits recorded; no capital allocation or WACC effect. |

Lane I remains an auxiliary \`MODEL_ONLY\` stream, not a ninth permanent architecture lane. The permanent architecture remains A–H.

## Foundational and equation-discovery status

- FND-001 thermodynamic-gap accounting: no new measurement.
- FND-002 output-information lower bounds: no new storage/readout bound.
- FND-003 matched control vs. quantum speed limit: no matched speed/energy result.
- FND-004 alternative physical primitives: no new demonstrated primitive.
- FND-005 QFT/particle mechanism scans: no new mechanism evidence.
- FND-006 mathematics-first invention: external result retained with falsifiable system follow-up.
- EQN-001 literature surveillance and EQN-004 counterexample/falsification governance: strengthened through a dated primary-source watch and executable negative tests.
- EQN-002, EQN-003, EQN-005 and EQN-006: no new validated equation, generator, physical law or device/economic consequence.
- \`BIO-001\`, \`FUS-001\`, and \`FIN-001\`: remain evidence-gated; no commercial or finance claim promoted.

## INV-029–INV-035

- **INV-029:** Data-Center-to-One-Phone remains the highest long-horizon mission; no physical compression result.
- **INV-030:** Pangola/biomass carbon remains functional substitution/minimization/recovery/recycling; no elemental transmutation claim.
- **INV-031:** accepted liquid-fuel cost remains unmeasured end-to-end.
- **INV-032:** reliable net delivered fusion-electricity economics remain unmeasured.
- **INV-033:** no lower financed principal, interest burden or WACC result.
- **INV-034:** current physical constraints remain binding; deep-frontier research remains open.
- **INV-035:** AI may generate hypotheses, but no generated equation becomes a law without the required evidence chain.

INV-025/026/027 remain preserved. The 100,000,000-GPU and universal 100,000,000-unit objectives remain falsifiable moonshots, not demonstrated achievements.

## GitHub sync, CI and blockers

The active branch is the existing PR branch, not \`main\`. No direct write to \`main\`, provider credentials, cloud session, QPU job, shot or billable execution occurred. The previous exact-head workflow run \`39940917215\` was queued when inspected; the new branch head must be checked for its own completed matrix before merge.

**Next highest-value gate:** wire the capability contract into semantic lowering, freeze a deterministic adaptive workload and exact useful-output contract, then run simulator/dry-run positive and negative branch tests. Only after official target metadata passes may an owner-authorized, bounded hardware attempt be considered.
