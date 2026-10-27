# Batch 071 — bind formal-proof evidence to equation hypotheses

**Date:** 2026-10-27  
**Canonical starting main SHA:** 9858c84a4971e46d484d1507668493d4a357a3f4  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime and equation-discovery tooling  
**Evidence owner:** Lane F — reproducibility, benchmarks, economics and integration  
**Publication/strategy owner:** Lane H  
**Cross-lane consumers:** B/C data and state bounds; D/G device/fabrication claims; E materials/energy; INV-034/035  
**Shared IDs:** RG-047, RG-046, FND-001–006, EQN-001–006, BIO-001, FUS-001, FIN-001, INV-025–035  
**Evidence class:** SOFTWARE CONTRACT + UNIT TESTS; no physical/economic advantage accepted

## Starting state and preservation

The newest observed main head was 9858c84a4971e46d484d1507668493d4a357a3f4. Its core workflow [#1775](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40455182752) passed all 15 jobs, including Python 3.10/3.11/3.12, QSP phase synthesis, QSVT prefixes, routed statevector probes, target snapshot identity, no-submit target transpilation and independent Qiskit verification. The cold-start handoff audit [#978](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40455182875) also passed. Those checks apply to the starting SHA, not to this new commit; exact-head CI must run after publication.

The charter, invariants, goals, README, research operating system, open-frontier directive, Kanusanan Pongpanna Model, strategic references, root directives 00/00A/01–06, Batch 070, current RG-047/RG-046/RG-EQN-008/QAOA-parity gaps, equation-discovery/proof modules and current Actions state were inspected. The six-language Thai/English/Chinese/Japanese/Korean/German plan context and recorded AI-agent/funding references remain preserved. INV-025/026/027 and INV-029–035 remain binding. No paid QPU or hazardous test was authorized.

## Lane A implementation

The standalone `FormalProofEvidence` record already binds exact theorem statement, proof bytes, environment and run-log digests to checker/toolchain metadata. The missing integration was that `EquationHypothesis.formal_proof_status` could still say `CHECKED` based on notes alone, without carrying that record.

This batch:
- adds optional `formal_proof_evidence` to `EquationHypothesis` and the discovery-field contract;
- requires a bound record for every proof state beyond `NOT_RUN`/ `NOT_APPLICABLE`;
- requires `claim_id == equation_id`, claim kind `PHYSICAL_EQUATION_HYPOTHESIS`, and exact status agreement;
- keeps `CHECKED` only as a compatibility alias for a bound `KERNEL_CHECKED` record;
- preserves separate `FORMAL_STATEMENT`, `KERNEL_CHECKED`, `INDEPENDENTLY_REPRODUCED`, `FAILED` and `INCONCLUSIVE` states;
- adds negative tests for missing evidence, claim-ID mismatch, status mismatch, formal-statement non-promotion, retained failures and the distinction between proof reproduction and physical replication.

The new tests are submitted for hosted validation. This runtime could not clone GitHub locally because DNS resolution for github.com is unavailable, so no local test-pass claim is made. A passing metadata test would establish schema consistency only, not that a prover ran or that a physical law is true.

## Fresh literature surveillance

Fresh searches revisited STRIDE (arXiv:2605.17790), the October 2026 AI-mathematics survey (arXiv:2610.17090), sparse-QROM/state-preparation bounds (arXiv:2607.28260), graph-based constitutive-law discovery (Science Advances, 2026-09-11), higher-order parity QAOA (arXiv:2610.26381) and the peer-reviewed HIDRA lithium-vapor study (published 2026-06-10). The relevant current-main watches already cover these sources; no additional material source warranted a duplicate literature article in this cycle. All remain external literature, not UQPU reproductions or project evidence.

## A–H status

- **A — Workloads/compiler/runtime:** advanced RG-047 by binding proof records into EquationHypothesis; QAOA parity and matched equation-discovery benchmarks remain open.
- **B — Cloud/QPU:** provider-neutral adapters and dry-run paths preserved; no paid/live QPU submission.
- **C — Memory/state/data movement:** sparse-QROM/state-preparation lower bounds remain model-specific circuit-complexity results, not classical memory equivalence.
- **D — Device/chip/fabrication:** FND-003 remains a matched-comparison contract; no new physical measurement or chip result.
- **E — Materials/energy:** BIO-001 accepted-liquid evidence and FUS-001 net-reliable-electricity/lifecycle-cost evidence remain open; HIDRA observations stay in their experimental regime.
- **F — Economics/evidence/integration:** proof states, false discoveries and failure outcomes remain separate; missing costs cannot become zero.
- **G — Manufacturing equipment/factory:** D/G co-design remains active; no fabrication/yield result is inferred.
- **H — Strategy/finance/publication:** multilingual strategic-plan links and recorded AI-agent/funding references remain preserved; no financing-rate or capital-cost outcome is claimed.

The repository's additional Lane I vehicle/levitation work remains preserved as contract/plan-only; this run does not silently promote it or substitute it for A–H.

## Foundational agenda and invariants

FND-001–006 and EQN-001–006 remain active and evidence-gated. RG-047's schema-integration item is closed by this code change, but the real pinned proof/checker run and independent rebuild remain open. RG-046 still lacks acquired, hash-verified raw SRSD-Feynman data and the preregistered >=30-seed comparison. FND-003 has a matched control/quantum contract but no new physical speed-limit measurement. BIO-001, FUS-001 and FIN-001 receive no new commercial evidence.

- **INV-029:** phone-class physical compression remains a measurable service/energy/thermal/lifecycle-cost mission; a remote terminal is insufficient.
- **INV-030:** Pangola carbon targets functional substitution, minimization, recovery/recycling, hybridization or redesign; no elemental transmutation claim.
- **INV-031:** accepted saleable liquid energy and full process cost remain unmeasured for target-cost claims.
- **INV-032:** net reliable delivered electricity and lifecycle cost remain unproven at target cost.
- **INV-033:** lower financed principal/time-at-risk may reduce absolute interest at unchanged terms; WACC/risk-premium claims require separate evidence.
- **INV-034:** foundational physics/mathematics remains an upstream research layer feeding A–H.
- **INV-035:** AI may generate hypotheses, but exact formal proof evidence, held-out prediction, falsification, experiment and independent physical validation remain distinct gates.

## Integration and next gate

Updated the focused RG-047 gap, aggregate research-gap/worklog summaries, README first-page cycle index and cold-start handoff manifest in one main-branch commit. The next highest-value gate is to run exact-head Actions, then pin and execute a real formal checker on an immutable theorem/proof/environment bundle, independently rebuild it, and only afterward connect that mathematical result to a held-out empirical test. No result is promoted from metadata alone.
