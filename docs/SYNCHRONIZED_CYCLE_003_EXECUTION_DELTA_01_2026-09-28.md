# Synchronized Multi-Lane Cycle 003 — Delta 01

**Date:** 2026-09-28  
**Status:** CYCLE 003 DELTA 01 CLOSED AFTER ALL 12 LANE EVENTS AND ARTIFACT-INCLUSIVE GREEN CI / NO NEW EMPIRICAL CLAIM  
**Branch:** `research/cycle-003-delta-01-2026-09-28`  
**Cycle base:** Cycle 002 closed at `176db539f271f89b795e1552fe4af580065c43f3`

## 1. Executive result

Cycle 003 Delta 01 advances all 12 portfolio lanes with a provider-neutral ER6 circuit/resource packet, a complete-null cost gate, a source-bounded bosonic-QEC calculation, current ASTM catalog metadata, and a deterministic synthetic SCM calibration fixture. All work remains at protocol, source-analysis, or model level. This delta contains no new empirical hardware, materials, human-participant, SCM-source, AI-training, or commercial-economics result; it does not demonstrate quantum advantage or GPU replacement.

The latest Cycle 002 closeout and Cycle 004 starting packet were verified on GitHub before work began. This branch starts from Cycle 002's actual closeout commit, including its later follow-up commit. The Cycle 003 closeout was completed after GitHub Actions verified the committed reproducibility artifacts and mandatory artifact-to-generator equality test.

## 2. Synchronized lane progress

| Lane | Delta 01 progress | Evidence state and remaining dependency |
|---|---|---|
| A | Lowered the frozen ER6 p=1 mean-energy and CVaR candidates into provider-neutral OpenQASM 3, preserving the instance and accepted-output contract. Each candidate has 6 qubits and 39 logical gate instructions: 6 H, 18 CX, 9 RZ and 6 RX. | Logical circuit model only. Provider transpilation, physical layout/depth, QPU output and a stronger classical baseline are absent. |
| B | Rechecked the official AWS Braket Rigetti Cepheus task/shot tariff. Two 8,192-shot tasks yield $7.5632 in task-plus-shot arithmetic. | Tariff sensitivity only; full AWS/cloud charges, provider selection, quote, billing record and authorization are absent. |
| C | Added exact readout payload bounds: each candidate returns 49,152 raw bits (6,144 bytes if bit-packed); the pair is 12,288 packed bytes. Two bits can label one of the four accepted output identities. | Provider serialization size and transfer, persistence, readout and decode time remain null/unmeasured. |
| D | Reconciled the published distance-5 cat-code experiment with its five storage modes, four syndrome ancillas and 2.8 μs cycle. | Literature context only; no matched UQPU device target, calibration or reproduction. |
| E | Refreshed the official ASTM D4935 catalog gate: the page lists D4935-18(2026), designation D4935-18R26, and $80.00 catalog price. | Full method text is unavailable to the project; purchase is not authorized; no compliance claim or material result. |
| F | Calculated the narrow tariff component while building a complete accepted-output cost gate with every missing input explicitly null. | Full bill and cost per accepted output remain null, including host, queue, transfer/storage, mitigation/decoder, retries, energy/cooling, capital and accepted-output count. |
| G | Updated the no-fabrication readiness gate with current method edition and uncertainty factors stated by ASTM. | No authenticated Pangola lot, frozen resin/hardener/cure, metrology uncertainty analysis, fabrication or VNA measurement. |
| H | Rechecked CAP-DMF-EMI-001 and CAP-BOSONIC-001 against this cycle's evidence. | Both remain NOT_AUTHORIZED; capital at risk remains null. |
| FND/EQN | Re-recorded the primary bosonic-QEC result and derived a central-value-only phase-memory bound under explicit assumptions. | No new law or project result; no confidence-bound interpretation, target horizon, or raw Zenodo data extraction. |
| SCM | Built deterministic CAL-001 synthetic controls and injected-interference trials with integrity hashes and a replication schema. | Fixture counts are not physical sensitivity/specificity. Labeled truth and trial ledger are present in the same JSON bundle, so it is not operationally blinded; no second-site or human study. |
| AI-COST | Preserved the owner-defined 50,000 THB ceiling and planning FX as arithmetic bounds against the existing $10T/$100T proxies. | No functionally equivalent AI task, measured incumbent baseline, provider bill or residual-cost result. |
| QOS/QSVT | Added hashed OpenQASM 3 circuit payloads and logical gate/readout counts under the same ER6 contract. | No provider transpilation or independent hardware result; application-specific QSVT reconstruction and end-to-end resources remain gated. |

Every lane is recorded as BLOCKED_WITH_PROGRESS. No lane is NO_UPDATE, and no evidence has been promoted between lanes.

## 3. Shared ER6 workload, circuit and readout contract

The source fixture is `seeded_erdos_renyi_maxcut(6, 0.5, 42)`, with frozen QUBO-to-Ising SHA-256 `bc3fb615b6fd2530694b097fde804e62f165fd7d0953bf66aff4602cd77fa201` and accepted-output contract `8efaa94bb3306d25`. Its exact optimum is -7 with accepted bitstrings `001011`, `001110`, `110001`, and `110100` (displayed v5…v0; qubit 0 is the integer least-significant bit).

Two 8,192-shot candidate circuits are preserved in provider-neutral OpenQASM 3. The generator reports logical instruction counts only; it does not claim provider-valid compilation, physical gate counts, depth, placement or calibration. Raw samples contain six bits each. The 6,144-byte per-candidate and 12,288-byte paired payloads are exact bit-packing arithmetic, not measured provider response sizes or network/storage measurements. The minimum two-bit label bound describes only which of four accepted identities was observed; it cannot replace the full raw sample distribution.

- Circuit/resource manifest: `benchmarks/experiments/cycle003-delta01-er6-provider-neutral-manifest.json`
- Manifest SHA-256: `6e2df63eb26f38b7ba1c6da26df5f31622c16b32f1349b5ded20b1f09fffe511`
- Source contract: `benchmarks/experiments/cycle002-delta01-er6-frozen-contract.json`
- Provider protocol: `benchmarks/experiments/batch020-er6-mean-vs-cvar-real-qpu-protocol.json`

## 4. Provider tariff and full-cost boundary

The AWS Braket pricing page, checked 2026-09-28, lists $0.30 per Rigetti Cepheus task plus $0.000425 per shot. For two tasks with 8,192 shots each, the arithmetic is $0.60 task charge + $6.9632 shot charge = $7.5632. It excludes other AWS services and all project-specific host, queue, retry, mitigation, energy, storage, labor and capital charges. It is not a quote, invoice or cost-per-accepted-output result. No provider or backend was selected, and no job was submitted.

The full-stack model keeps total cost, accepted-output count and cost per accepted output null until every required component and an observed acceptance count exist. RG028 remains open: a provider-matched workload, execution and billing record plus competitive baseline are still required; results from different providers cannot be combined.

## 5. Bosonic-QEC source record and bounded inference

Putterman et al., *Nature* 638, 927–934 (2025), DOI 10.1038/s41586-025-08642-7, reports the distance-5 encoded cat-qubit experiment's best measured logical error as 1.65 ± 0.03% at `|α|² = 1.5`; its syndrome cycle is 2.8 μs. The reported uncertainty is retained as a paper error bar, not converted to a confidence interval. The paper distinguishes logical phase/bit error and logical-X lifetime.

The code derives a conditional `T_X ≥ 42.424 μs` lower bound from the 1.65% central value and `εL = (εphase + εbit)/2`, using `εphase = Tcycle/(2 TX)`. Assumptions: the central reported value is used without its error bar; bit-flip probability is nonnegative; and the paper's equations apply. This is arithmetic inference, not a confidence bound, project lifetime, target, or reproduction. The linked Zenodo data record is cited, but its raw files were not re-extracted after rate limiting during this run.

## 6. ASTM and fabrication readiness

The ASTM catalog page, checked 2026-09-28, shows active edition D4935-18(2026) / D4935-18R26, a listed price of $80.00, normal-incidence far-field plane-wave scope for planar materials, and uncertainty dependence on material, transmission-line mismatches, system dynamic range and ancillary equipment. The catalog page is metadata; the full standard text is not available to this project. No purchase is authorized, no compliance is claimed, and no physical work occurred.

The existing Pangola process recipe remains proposal-only. Species/lot authentication, exact resin/hardener/cure, authorized method access and a metrology uncertainty review remain gates before fabrication or VNA testing. The price is a catalog listing, not project spending.

## 7. SCM synthetic CAL-001 fixture and blinding boundary

The deterministic fixture contains 128 synthetic controls and 128 synthetic known-interference trials. Its rule is `|z| ≥ 4` per channel and a coincident event on at least 2 of 6 channels. For this fixed generated fixture, all 128 injected trials trigger and all 128 controls do not. These are exact fixture counts, not estimates of any physical detector's sensitivity, specificity or false-positive rate. Calibration records are synthetic; the independent-site manifest is `NOT_EXECUTED_NO_SECOND_SITE`; no human data were collected.

Each observation payload omits its condition label, but the committed JSON bundle includes labeled truth and a labeled trial ledger alongside observations. Anyone with the artifact can unseal it. The file is not operationally blinded or cryptographically sealed; the corrected wording and regression assertion preserve that boundary.

- Fixture: `benchmarks/results/cycle003-delta01-scm-cal001-synthetic.json`
- SHA-256 of the full fixture: `393b8ef61c7bb0c0f22b95a51814a5865d371916f67d284e78cb2c34eb6c7f7d`
- SHA-256 of the canonical observation/truth/ledger bundle: `553381511defb23c374cf10c7ea6fdb5cf880f3142f161cc527a970ba44a89c2`
- Generator commit recorded in its replication manifest: `7b3ca1fde4a34238f40408df51236600cf4a4a61`

## 8. AI-cost ceiling and capital gates

The owner-defined ceiling of 50,000 THB at the planning rate 33.045 THB/USD equals $1,513.088213043 before all other costs. Against the repository's $10T and $100T baseline proxies, the zero-fixed-cost maximum shares are 1.513088213043e-10 and 1.513088213043e-11. These are sensitivity bounds only. Functional equivalence, baseline provenance, provider costs and residual allowable shares remain null.

CAP-DMF-EMI-001 and CAP-BOSONIC-001 remain NOT_AUTHORIZED with null capital at risk. This cycle authorizes no spending, paid job, materials purchase, fabrication, human study, or capital deployment.

## 9. Open gates and Cycle 004 handoff

| Lane | Open dependency | Next bounded action |
|---|---|---|
| A | No stronger classical baseline or provider-specific physical circuit exists. | Freeze a reproducible classical baseline and measure its end-to-end time/resources against the same accepted-output contract. |
| B | RG028 lacks same-provider execution and billed-cost provenance; credentials/authorization remain absent. | Update official terms/quote and provider-ready packet; preserve the no-job gate and do not mix providers. |
| C | Only payload bounds are known; provider serialization and latency are null. | Measure local serialization, persistence and decode bytes/times reproducibly; keep provider transfer values null absent a run. |
| D | No project logical-memory target or matched device calibration exists. | Define service/retention contract first; extract source-level control/readout/decoder resources and state the device dependency. |
| E | Current catalog metadata is available, but full D4935 text and matched material inputs are not. | Use authorized text access if available; reconcile feedstock, resin and incumbent/candidate measurement requirements before any fabrication. |
| F | Full lifecycle cost and accepted-output denominator remain null. | Extend the ledger with all provider, host, queue, storage, retry, mitigation, energy, labor and classical baseline components. |
| G | Authenticated feedstock, fixed recipe and metrology capability are absent. | Complete a no-fabrication readiness review of provenance, resin/cure and uncertainty against the measurement range. |
| H | Both capital gates remain NOT_AUTHORIZED. | Reconcile gate evidence only; keep amounts null and make no funding or purchase decision. |
| FND/EQN | Zenodo raw data were not retrieved; inference does not set a project target. | Retry primary-data retrieval and separate per-cycle error, lifetime, component rates and uncertainty before modeling a target. |
| SCM | Fixture truth is unsealed in the same JSON; no independent site exists. | Design a two-party synthetic-only blinded handoff with separately controlled truth, a pre-frozen scorer and manifest; test unseal controls before any field protocol. |
| AI-COST | No frozen equivalent AI workload or measured baseline exists. | Specify one functionally equivalent task, quality gate and baseline provenance before any residual-cost calculation. |
| QOS/QSVT | QASM is logical; no independent provider compilation or application certificate is attached. | Cross-parse/reconstruct the saved circuit with an independent SDK, record decomposition/serialization, and keep hardware/QSVT promotion gated. |

## 10. Verification and closure

- GitHub Actions run #485 on `3494042aaac89cfeb36d8fbdd6b6a3ca65449065`: success across the configured Python matrix and verification jobs.
- GitHub Actions run #486 on `7b3ca1fde4a34238f40408df51236600cf4a4a61`: success across all configured jobs after the SCM blinding-boundary correction.
- GitHub Actions run #487 on `59154aa6c6a8ff64219a611fad82b5091bd41a2c`: success. The Python 3.10/3.11/3.12 test matrix passed with the committed artifacts present and the artifact-to-generator equality check mandatory; all other configured workflow jobs also passed.
- Local Cycle 003 unit tests: 10/10 passed with the generated artifacts present.

Cycle 003 Delta 01 is closed as a synchronized protocol and reproducibility cycle. Closure records no evidence promotion, new empirical claim, paid execution, fabrication or capital authorization.

## 11. Sources and linked artifacts

Primary and official sources checked on 2026-09-28:

- Putterman et al., *Nature* 638, 927–934 (2025), published 2025-02-26, DOI 10.1038/s41586-025-08642-7: https://www.nature.com/articles/s41586-025-08642-7
- Associated data record, DOI 10.5281/zenodo.14257632: https://doi.org/10.5281/zenodo.14257632
- AWS Braket pricing, including Rigetti task and shot example: https://aws.amazon.com/braket/pricing/
- ASTM D4935 active catalog entry D4935-18R26: https://store.astm.org/standards/d4935

All source-dependent values include publication/access dates, evidence class, assumptions and limitations above. Repository code, protocol and JSON artifacts are linked within the cycle packet.
