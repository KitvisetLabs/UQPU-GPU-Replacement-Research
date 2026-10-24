# Literature watch — 2026-10-24: verifiable PDE and constitutive modeling

**Accessed:** 2026-10-24  
**Primary owner:** Lane H — strategy, finance and future-industry research  
**Feeds:** A–H; FND-001–006; EQN-001–006; BIO-001; FUS-001; FIN-001  
**Evidence class:** `LITERATURE_ONLY / THIRD_PARTY_RESEARCH`  
**Project evidence promotion:** none  
**Canonical starting main SHA:** `c7b5958af58fad04a101ef5c6abf6a29293c867e`

## Why this delta is distinct

The main-branch literature watch dated 2026-10-23 covers optimization-law discovery and an assumption-scoped ancilla-QFI boundary. Parallel PR #65 covers AI-mathematics candidate ranking, proof verification, novelty assessment and physical validation. This note focuses on applied-model validation: converting informal partial differential equation (PDE) tasks into machine-checkable specifications, and keeping physics-informed constitutive-model fitting separate from material qualification.

The result is a method lead for EQN/FND workflow design, not a newly discovered physical law or a UQPU result.

## Primary source — verifiable PDE reasoning

Wuyang Chen, **“Verifiable PDE Reasoning and Modeling with Neurosymbolics,”** Proceedings of IJCAI 2026, Early Career Spotlight, pp. 8144–8149, DOI 10.24963/ijcai.2026/903. Official proceedings: https://ijcai.org/proceedings/2026/903.

The paper describes a semantics-first approach that formalizes informal PDE problems, synthesizes solver-ready code, decomposes control tasks for external solvers, and uses semantics-aware Lean/Mathlib theorem retrieval to assist formalization. The proposed connection is important for physical modeling because PDEs appear in plasma, fluid, heat-transfer, materials and device models.

## Secondary Lane D/E/G signal — physics-informed alloy constitutive modeling

Prashil S. Joshi, Diksha Mahadule and Rajesh K. Khatirkar, **“Physics-Informed Residual Deep Learning for Constitutive Modeling of Hot Deformation and Dynamic Recrystallization in a Mo-Rich α+β Titanium Alloy,”** arXiv:2607.13467, submitted 2026-07-15. Official preprint: https://arxiv.org/abs/2607.13467.

The preprint reports residual physics-informed neural networks for Ti-6Al-4Mo-1V-0.1Si hot-deformation data, with thermal/strain-rate/strain-hardening constraints and a dynamic-recrystallization submodel. It reports cross-validated error on its own dataset. The useful novelty for UQPU is a concrete example of embedding constitutive constraints into a data-driven model for manufacturing-relevant material behavior; the reported values are third-party results and are not UQPU measurements.

Transfer is unproven. The alloy, processing conditions and measured response are specific to that study. A fitted model does not establish a new constitutive law, independent reproducibility, manufacturing yield, qualified carbon material, device reliability or lower cost. No extrapolation to Pangola-derived carbon, quantum chips, fusion-facing materials or factory process windows is justified without new data.

## Genuine novelty, evidence class and limitations

The PDE source offers an explicit interface between natural-language model requirements, formal specifications, solver execution and theorem retrieval. The alloy source shows a complementary pattern: a constitutive model can encode physical constraints while still requiring held-out validation against experimental data. Together they motivate claim-type-specific gates: proof for formal statements, solver checks for numerical models, and material/device experiments for empirical adequacy.

A formal proof establishes a statement under encoded assumptions; numerical convergence establishes a property of a computation; and a low prediction error establishes only performance on the evaluated data distribution. None alone proves that the selected model describes nature across an untested regime. Solver residuals, boundary conditions, stability assumptions, thermodynamic consistency, uncertainty, independent replication and physical validation remain separate gates.

No post-2026-10-23 result found in this expanded scan changes UQPU's current physical, provider, or economic acceptance criteria. These are newly connected method signals, not claims that the source papers were published today.

## Falsifiable UQPU follow-up — EQN-PDE-001

Build a small offline manufactured-solution benchmark before connecting generated PDE models to real engineering decisions:

1. Freeze a set of PDEs with known analytic/manufactured solutions, units, domain, boundary/initial conditions and any justified conservation or symmetry properties.
2. Have the candidate pipeline translate each verbal task into a formal specification and solver input. Keep a hand-checked oracle hidden from the generator.
3. Evaluate dimensional consistency, boundary-condition compliance, residual norms, convergence under mesh/time-step refinement and theorem-assumption coverage.
4. Hold out parameter ranges, boundary-condition combinations and at least one equation family. Report interpolation and extrapolation separately.
5. Search for counterexamples, malformed domains, unstable discretizations and candidates that satisfy a formalized statement but not the intended physical specification. Preserve the smallest failing fixture and seed.
6. Compare with a conventional hand-authored solver and a fixed-generator baseline under matched data, wall-clock, host-compute and validation budgets.
7. Record false discoveries, solver failures, proof failures and the full cost of validation. A successful synthetic benchmark remains computational evidence only; a physical claim requires a discriminating observable and independent measurement.

**Falsifier:** the pipeline accepts an incorrect formalization, violates a declared boundary/constraint, fails a preregistered convergence or held-out gate, or cannot distinguish an intentionally incorrect model from the oracle. Any such event blocks promotion.

**Acceptance artifact:** machine-readable claim type, assumptions, units, source/specification hashes, solver and checker versions, held-out metrics, counterexample status, proof status, resource ledger and explicit non-claims. A green result must not silently promote a PDE model to physical truth.

### Conditional material-model follow-up — MAT-CONST-001

Only after Lane D/E selects a concrete candidate material or process, compare a physics-informed constitutive model with a simple established baseline using matched samples/lots, held-out temperature/strain-rate or process regimes, uncertainty intervals and independent repeats. Include thermodynamic consistency where applicable, process-window/yield measurements and lifecycle cost. Reject the candidate if the apparent gain disappears on held-out regimes, violates the declared constraints, or fails independent measurement. The titanium-alloy preprint supplies a test-design example, not a Pangola-material result.

## Cross-lane relevance

- **A — Quantum programming/compiler/runtime (Priority #1):** use claim-aware formal contracts for compiler and workload transformations; PDE work is an offline discovery subtrack, not a replacement for the QOS/QSVT acceptance gate.
- **B — Cloud/QPU:** formal model or solver success does not authorize provider submission; preserve provider/target provenance and the no-paid-job boundary.
- **C — Memory/state/data movement:** include state, serialization, input/output, transfers and reconstruction when a model workflow is mapped to compute; state-space size is not readable classical storage.
- **D — Device/chip/process/packaging:** use verified assumptions and measurable observables before translating a PDE-derived requirement into device constraints.
- **E — Biomass/materials/bio-oil/fusion/cooling:** potential future uses include heat/mass transport, reactor/plasma, upgrading and material-process models; none of BIO-001, FUS-001 or material qualification advances without validated inputs and measurements.
- **F — Economics/evidence/integration:** count generation, proof attempts, solver runs, host compute and validation delay in cost-per-accepted-output and time-to-evidence accounting.
- **G — Manufacturing equipment/factory systems:** pair any device/process model with Lane D; formal consistency alone does not establish process-window, yield or factory economics.
- **H — Strategy/finance/publication:** preserve reproducible artifacts, negative results and the multilingual Kanusanan Pongpanna Model context; do not treat AI-agent/funding references as proof.
- **Lane I — additional canonical field-agnostic vehicle research:** retained as a separate contract-only lane; these literature signals give it no lift, propulsion or energy evidence and do not replace any A–H lane.

## INV-029–035 and foundational status

- **INV-029:** offers a route to more auditable service/device models; no data-center-to-phone physical compression is demonstrated.
- **INV-030:** could later structure carbon-material process models; no elemental transmutation or functional material substitution is claimed.
- **INV-031:** may inform future reaction/transport models only after qualified feedstock and accepted-liquid mass/energy/cost data exist.
- **INV-032:** may inform plasma/heat/blanket models only with assumption-scoped validation; no net delivered fusion electricity or commercial cost is established.
- **INV-033:** charge validation compute and time-to-evidence; no WACC or economy-wide interest-rate reduction is inferred.
- **INV-034:** adds a testable applied-mathematics route from formal specification to solver and device/system consequence.
- **INV-035:** permits AI-generated alternative equations while preserving dimensional, symmetry, conservation, causality, held-out, falsification and independent-validation gates.

FND-001 thermodynamic-gap accounting, FND-002 output-information lower bounds, FND-003 matched control-vs-speed-limit measurement, FND-004 alternative physical primitives, FND-005 QFT/particle scans and FND-006 mathematics-first invention remain separate work items. EQN-001–006 still require generator → constraints → evaluator → held-out/generalization → counterexample → proof/simulation → discriminating experiment → independent replication → system consequence → economics. This literature item creates no new result for those programs by itself.

## Negative evidence and next gate

No UQPU workload, real-QPU, material, accepted bio-oil, net-fusion-electricity, or project-finance measurement was produced. No physical law is promoted. No provider probability is combined with another target's price. Paid QPU execution remains unauthorized without credentials, a bounded budget and explicit user consent.

**Next highest-value gate:** implement EQN-PDE-001 as a deterministic offline manufactured-solution test harness, connect its result schema to the existing equation-discovery ledger without duplicating PR #65's general AI-mathematics audit, and require exact-head hosted CI before integration. Consider MAT-CONST-001 only after a specific candidate material/process and qualified data are available.
