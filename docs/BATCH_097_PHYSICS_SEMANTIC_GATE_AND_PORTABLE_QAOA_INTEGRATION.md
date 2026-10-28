# Batch 097 — physical-semantic gate and portable signed-Max-Cut QAOA integration

**Date:** 2026-10-28  
**Starting main SHA:** d04eb7987b2e3b0c82840b77e263cf2ae8e41285  
**Primary owner:** Lane F — evidence contract and cross-lane integration  
**Priority execution owner:** Lane A — workload/compiler/runtime  
**Literature owner:** Lane H — formalization and foundational-physics surveillance  
**Cross-lane scope:** A–H; INV-029–035; FND-001–006; EQN-001–EQN-006; BIO-001; FUS-001; FIN-001  
**Evidence class:** SOFTWARE_CONTRACT_CHANGE + TESTS_ADDED_PENDING_CI + LITERATURE_ONLY  
**Hardware:** no real QPU job, no paid execution, no physical experiment

## 1. Canonical start and cold-start audit

The current main head was resolved dynamically as d04eb7987b2e3b0c82840b77e263cf2ae8e41285. The cycle read PROJECT_CHARTER.md, VERSION_INVARIANTS.md, GOALS.md, README.md, docs/RESEARCH_OPERATING_SYSTEM.md, docs/OPEN_FRONTIER_RESEARCH_DIRECTIVE.md, docs/KANUSANAN_PONGPANNA_MODEL.md, STRATEGIC_PLAN_REFERENCES.md, the permanent root directives 00, 00A and 01–06, Batch 096, the newest equation-discovery gaps and literature watch, the signed-Max-Cut gate, A–H manifest/scoreboard, and current CI observations.

All eight permanent root directives remain present. The Kanusanan Pongpanna Model, Thai/English/Chinese/Japanese/Korean/German public master-plan links, and strategic AI-agent/funding references remain canonical context. INV-025/026/027, INV-029–035, the eight operational lanes A–H, and the historical Lane I legacy workstream are preserved.

The connector returned no combined-status contexts and no commit-associated workflow runs for main SHA d04eb7987b2e3b0c82840b77e263cf2ae8e41285. The preceding main SHA 0cdc1514a82716d6bfd171ca774344b17b13f4df had prototype/invariant workflow #1881 and cold-start audit #1107 green. Those parent results do not certify d04eb or this new branch. The current branch therefore remains CI-pending until its exact-head checks are observed.

## 2. Priority-1 Lane A — join the signed objective to the portable QAOA path

The repository already has a pure-Python signed-Max-Cut lowering, a pinned Qiskit 2.5.2 operator-semantic check, a portable QAOA program builder, a small statevector simulator, and IBM/Braket/Azure inspection adapters. The missing integration gate was a single test that joins these pieces under the same frozen signed objective.

Added software/uqpu-prototype/tests/test_signed_maxcut_portable_qaoa_integration.py. It:

1. Reuses the six frozen signed graph fixtures.
2. Builds the minimization instance for negative signed-Max-Cut score and checks every tiny assignment against the direct objective and the independently reconstructed Ising energy.
3. Builds the provider-neutral PortableProgram QAOA circuit and compares its ideal statevector with a separate dense reference constructed from direct objective scores rather than compiler Ising coefficients.
4. Verifies normalized output probabilities and the frozen contract ID, objective sense, qubit-0 least-significant-bit convention, and shot budget.
5. Lowers the same signed workload through IBM Quantum, Amazon Braket and Azure Quantum inspection adapters, requiring DRY_RUN_ONLY and paid_job_submitted=false.

This is an exact finite software/reference gate plus ideal statevector simulation. It does not test a noisy target, provider billing, real-QPU behavior, throughput, energy, or accepted-task economics. The new test has not been executed locally because this runtime could not resolve github.com for a repository clone; exact-head GitHub Actions must determine whether it passes. Any failure must be retained and fixed before the gate advances.

**Next Lane A gate:** after CI, add target-aware simulator/reference comparison on the same signed workload and frozen output-quality acceptance contract. Keep execution success separate from quality acceptance. Real-QPU submission remains unauthorized without credentials, bounded budget and explicit user consent.

## 3. INV-035 implementation — formal proof is not physical interpretation

The formal equation-candidate contract already binds proof evidence to a claim ID, status, checker/version, source revision, proof artifact, environment and run log. It did not explicitly require a separate review that the formal definitions and assumptions faithfully represent the intended physical system.

Updated software/uqpu-prototype/uqpu/equation_discovery.py to add:
- physical_interpretation_review_status with NOT_REVIEWED, INDEPENDENTLY_REVIEWED, FAILED and INCONCLUSIVE states;
- auditable review notes required for reviewed, failed and inconclusive states;
- required-field reporting for the new gate; and
- a promotion rule that requires INDEPENDENTLY_REVIEWED in addition to the existing empirical evidence, held-out improvement, independent validation, counterexample and false-discovery gates.

The tests now verify that a kernel-checked formal statement cannot bypass physical-interpretation review, and that failed or unknown review states do not silently promote a candidate. This is a conservative evidence-contract change, not a formalization of a new physical law. The exact-head tests are pending CI.

## 4. Fresh literature surveillance

### AI-assisted physics formalization and AxQM

Krippendorf, Sarra and Tooby-Smith, arXiv:2610.14059 (submitted 2026-10-06; current HTML text dated 2026-10-15), argue for formalization as a reusable verification layer while emphasizing that the checked definitions must still capture the intended physics. Yin, Taylor, Englund and Koppens, AxQM, arXiv:2609.05157 (submitted 2026-09-04), report 1,019 kernel-checkable proof-synthesis tasks across 479 items in finite-dimensional quantum mechanics. The authors explicitly discuss semantic defects that a proof kernel cannot detect.

The literature watch and focused gap require a physical-interpretation review separate from proof status. These external sources remain LITERATURE_ONLY; UQPU has not run AxQM or independently audited its library.

### Planckian quantum dynamical entropy

Cao, *Physical Review Letters* 137, 030402, DOI 10.1103/wd91-v58h, published 2026-07-13, derives a CNT dynamical-entropy rate formula for a specified continuous-monitoring scheme and conjectures a broader Planckian rate bound. The specific Gaussian mesoscopic-observable analysis supports a restricted bound, while the universal extension remains conjectural. A dated watch and reproduction gap distinguish this information-gain rate from computation runtime, Landauer heat, wall-plug energy and cost per accepted task. No UQPU reproduction or new universal law is claimed.

The current-main surveillance also checked the existing SymFM/PiT-PO watch, the CoSR accepted-versus-withdrawn source conflict, formal theorem-discovery leads, recent symbolic regression and physics-informed modeling, and prior QSL/thermodynamic watches. Duplicate articles were not created where the source or gap was already recorded. No credible new anomaly or independently validated physical-law modification was promoted in this cycle.

## 5. Eight-lane status

- **A — Quantum programming/workloads/compiler/runtime:** integrated signed-Max-Cut -> negative-score QUBO -> portable QAOA -> ideal statevector/reference test added; exact-head CI pending. Next: fix any failure, then target-aware simulation and accepted-output quality.
- **B — Cloud/QPU/provider integration:** the new test uses IBM Quantum, Amazon Braket and Azure Quantum adapters only in dry-run inspection. The broader provider-neutral roster (IonQ, Rigetti, D-Wave, IQM, Quantinuum, Pasqal, QuEra, Quandela, OQC and relevant emerging providers) remains preserved. No target or price was borrowed across providers.
- **C — RAM/VRAM/HBM/storage/state/data movement:** the new test checks bit order and finite output probabilities only. It does not equate Hilbert-space size with readable classical storage or measure state/I-O bytes, transfer, memory, reconstruction or host compute.
- **D — Quantum/photonic/semiconductor device/chip/process/fabrication/packaging:** no device measurement or target-native schedule was added. Hamiltonian mapping, gate fidelity, control, leakage, thermal and fabrication constraints remain target-specific.
- **E — Biomass/advanced materials/bio-oil/fusion/cooling/infrastructure:** the Planckian entropy paper is a theoretical monitoring lead only. No Pangola functional-substitution result, accepted liquid-fuel cost, fusion net-electricity, cooling or infrastructure result was produced.
- **F — Economics/benchmarks/evidence/integration:** equation promotion now distinguishes formal proof from physical interpretation; A/B software integration is testable. No measured cost/task advantage, energy winner, lower WACC or commercial evidence.
- **G — Manufacturing equipment/software/factory systems:** continuous D/G co-design remains mandatory; no equipment capability, yield, cost-per-good-device or packaging evidence.
- **H — Strategy/finance/future industries/publication:** two dated literature watches and two focused gaps were added. The Kanusanan Pongpanna Model and all six multilingual master-plan links remain preserved; strategy and external papers are context, not automatic evidence.

## 6. Foundational and equation-discovery progress

- **FND-001:** the Planckian CNT entropy-rate conjecture is now a source-pinned reproduction lead. No independent rate integral, finite-size scaling or wall-plug-energy result exists.
- **FND-002:** output-information lower bounds remain separate from Hilbert-space dimension and readable memory. No new storage-capacity result.
- **FND-003:** the CNT entropy-rate paper is not a generic quantum-speed-limit theorem. Existing matched control-versus-QSL measurement remains open.
- **FND-004:** no alternative physical primitive passed a discriminating experiment.
- **FND-005:** no new QFT/elementary-particle mechanism or independently validated device consequence.
- **FND-006:** formal proof versus physical-model faithfulness is now an explicit evidence gate; no new theorem or law is claimed.
- **EQN-001–EQN-006:** no candidate promoted. Generator, explicit constraints, held-out/generalization tests, counterexamples, proof/simulation, discriminating experiments, independent replication, device consequences and economics remain separate steps. Failed and undecided candidates remain first-class evidence.
- **BIO-001 / FUS-001 / FIN-001:** unchanged open gates. No accepted liquid-energy cost, net reliable fusion electricity, lower financed principal/interest, lower WACC or time-to-evidence saving was measured.

## 7. INV-029 through INV-035

- **INV-029:** physical Data-Center-to-One-Phone remains the highest mission. The US$10T–US$100T number is only an ambition-scale proxy; measurable service, capability, energy, physical-compression and lifecycle-cost contracts are still required. A remote terminal is not physical compression.
- **INV-030:** Pangola/agricultural-residue carbon remains a functional substitution, minimization, recovery/recycling, hybridization or redesign strategy. No elemental transmutation or qualified material replacement is claimed.
- **INV-031:** ultra-low-cost bio-oil remains a goal. Full feedstock/preprocessing, yield, upgrading, hydrogen/catalyst, utilities, CAPEX/OPEX, logistics, financing and non-double-counted coproduct boundaries remain mandatory.
- **INV-032:** ultra-low-cost fusion electricity remains a goal. NET delivered electricity must include recirculating power, capacity factor, construction time, component lifetime/replacement, fuel cycle, materials damage, maintenance/remote handling, conversion/cooling, grid interfaces, financing and decommissioning.
- **INV-033:** no lower project WACC or economy-wide rate is inferred. Lower required principal can lower absolute interest at unchanged terms, but no such project measurement was made.
- **INV-034:** foundational physics/mathematics remains an upstream layer feeding A–H; present physical constraints remain binding.
- **INV-035:** AI may generate alternatives, but no generated equation is a law by declaration. The new independent physical-interpretation gate strengthens the generator-to-evidence chain.

INV-025/026/027 and both 100,000,000-unit moonshots remain falsifiable goals. GPU/CPU/NPU/RAM/VRAM/storage comparisons require subsystem-specific equivalent useful output; NPU comparisons require real neural-workload semantics, quality, precision, latency, throughput, data movement and cost, not TOPS alone.

## 8. Integration, synchronization and next gate

The branch adds the two literature watches, two focused gaps, Lane A integration test, equation-discovery code/tests, refreshed Lane A gate status, this Batch 097 report, a cross-lane integration report, README summary, scoreboard, WORKLOG, RESEARCH_GAPS and cold-start manifest updates. The large append-only WORKLOG.md and RESEARCH_GAPS.md were fetched completely before their append operations; their previous contents are preserved as exact prefixes.

**Main synchronization:** all new changes are on the source branch and remain pending PR review. They are not described as merged main work. Older historical branch/fork coverage and earlier sync debt remain unresolved. The source SHA and PR mapping must be recorded once the final branch head and PR exist.

**CI:** no exact-head result is available yet for the source branch. Parent-main green checks do not carry forward. No local test result is claimed.

**Next highest-value gate:** observe exact-head core/invariant and cold-start CI; repair any failures; verify the new physical-interpretation tests and signed-Max-Cut portable-QAOA integration test; then proceed to target-aware simulation under the same accepted-output contract. No paid QPU job is authorized.
