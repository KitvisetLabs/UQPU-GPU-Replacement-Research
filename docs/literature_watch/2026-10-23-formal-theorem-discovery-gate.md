# Literature watch — 2026-10-23: formal theorem discovery and singular equation search

**Accessed:** 2026-10-23  
**Primary owner:** Lane H — strategy / future-industry research and publication  
**Implementation consumer:** Lane A software research; integration owner Lane F  
**Feeds:** FND-006, EQN-001–006, INV-034, INV-035; secondary links to A/B/C and D/G  
**Evidence class:** `LITERATURE_ONLY / THIRD-PARTY PREPRINT`  
**Project evidence promotion:** none

## Sources reviewed

1. Kazuki Ota, Takayuki Osa and Tatsuya Harada, *Self-Supervised Theorem Discovery in a Formal Axiomatic System*, arXiv:2606.28747v1, submitted 2026-06-27; listed for the AI for Math Workshop at ICML 2026.  
   https://arxiv.org/abs/2606.28747
2. Sergei Garmaev, Maurice Gauché and Olga Fink, *Complex Equation Learner: Rational Symbolic Regression with Gradient Descent in Complex Domain*, arXiv:2605.03841v1, submitted 2026-05-05.  
   https://arxiv.org/abs/2605.03841

Both are third-party research reports. This watch records their reported methods and limitations; it does not independently reproduce their results.

## Material delta 1 — self-growing theorem libraries can be an explicit discovery mechanism

Ota et al. describe an agent that starts from axioms and inference rules, alternates proof search with extraction of reusable theorems, and feeds the resulting theorem library back into later proof search. The authors report discovery of tens of thousands of theorems and successful proofs for human-written benchmark problems; they also report improved LLM proof performance when discovered lemmas are supplied as prompts.

**Genuine relevance:** FND-006 should treat formal theorem discovery as a generator family in its own right, not merely as a final proof step after equation generation. A reusable lemma library may expose mathematical structures, lower bounds, or counterexamples that can later be connected to EQN-001–006 and to workload/compiler constraints.

**Limitations:** the result is relative to the chosen axioms, inference rules, proof representation, and checker. A formally derived theorem does not establish that its axioms describe a physical system. The project has not reproduced the reported theorem counts, benchmark results, proof-search cost, or theorem utility. Counts of generated theorems are not a measure of novelty, mission relevance, or physical truth.

## Material delta 2 — complex-domain search may widen equation candidates around singular operators

Garmaev et al. extend Equation Learner-style symbolic regression with complex-valued optimization weights to mitigate real-domain optimization pathologies around division, logarithms, square roots, poles, and domain restrictions. The paper reports benchmark recovery and an experimental frequency-response example with singular behavior.

**Genuine relevance:** EQN-001 candidate generation should not silently exclude rational or singular forms solely because a particular optimizer has difficulty crossing real-axis degeneracies. But any such candidate must carry an explicit real-valued domain, pole/branch-cut conditions, and a falsifier.

**Limitations:** a search trajectory in complex parameter space does not make a complex-valued expression a physical law. Singularities can be overfit, hidden by the loss function, or lie outside the measurement domain. The reported benchmarks and example are not UQPU material, bio-oil, fusion, device, or cost evidence.

## Project implementation delta

A new metadata-only gate, `software/uqpu-prototype/uqpu/formal_proof_gate.py`, now represents the minimum provenance needed for a theorem candidate to be reviewed:

- exact theorem statement and its SHA-256 digest;
- axiom-set and proof-object digests;
- checker identity/version, checker image digest, result, exit code, and log digest;
- a second checker with a different identity and image digest;
- matching theorem, axiom-set, and proof-object digests across both records.

Nine isolated unit tests passed on Python 3.13.5. These tests validate metadata consistency only. They do **not** parse or verify a proof object, run a proof assistant, or promote a mathematical claim. The result is `LOCAL_UNIT_TESTS_ONLY`; exact-commit CI remains to be checked.

## Falsifiable follow-up

Work ID: `FND6-PROOF-001`.

1. Freeze a small formal system, its axiom-set digest, inference rules, theorem statement, and proof object before evaluation.
2. Include known theorems, false claims, inconsistent premises, altered proof bytes, altered axiom sets, and a theorem that is independent of the selected axioms if such a fixture is available.
3. Run the proof object through a primary trusted checker and a genuinely independent checker build. Require identical theorem, axiom, and proof digests; retain complete logs.
4. Verify that false or altered fixtures are rejected and that incomplete, mismatched, or single-checker records remain unverified.
5. Record proof-search runtime, CPU time, peak memory, artifact bytes, and checker versions; compare discovery utility against a fixed baseline and held-out theorem families.
6. For any candidate intended to change physics, separately require incumbent assumptions, units/dimensions, symmetry, conservation, causality, limiting cases, discriminating observables, held-out predictions, counterexample search, experiment/proof, and independent validation.

**Preregistered falsifier:** the gate fails if a single-checker record is accepted as independent replay, if a changed theorem/axiom/proof digest passes, or if a metadata-complete record is described as a verified physical law.

## A–H integration and evidence boundaries

| Lane | Consequence this cycle |
|---|---|
| A | Adds a testable proof-provenance interface for future theorem/algorithm discovery; no compiler or useful-task advantage. |
| B | No provider initialization, credential use, target snapshot, job, shot, or billable usage. |
| C | Formal proof metadata is not readable memory, storage capacity, or state-service equivalence. |
| D | No device, chip, process, packaging, or fabrication result. |
| E | No Pangola material, accepted bio-oil, net fusion electricity, cooling, or infrastructure result. |
| F | Adds a reproducibility and evidence-class gate; no accepted-task economics, capital, interest, or WACC result. |
| G | No manufacturing equipment or factory-system consequence before a validated device requirement exists; D/G co-design remains open. |
| H | Publishes a source-scoped literature delta and next falsifiable gate while preserving the strategic-plan references. |

## Invariant contribution

- **INV-029:** no physical Data-Center-to-One-Phone compression is demonstrated.
- **INV-030:** no carbon functional substitution is validated; no elemental transmutation is claimed.
- **INV-031:** no accepted liquid-energy/fuel product or commercial target cost is demonstrated.
- **INV-032:** no net reliable delivered fusion electricity or commercial cost is demonstrated.
- **INV-033:** no reduction in financed principal, absolute interest, risk premium, or WACC is measured.
- **INV-034:** advances the mathematics-first theorem-discovery workflow, without treating mathematical possibility as physical realizability.
- **INV-035:** strengthens proof provenance and independent replay as explicit gates; AI-generated equations remain hypotheses, not laws.

INV-025/026/027 and the 100× / 100,000,000× targets remain unproven. No Hilbert-space dimension is equated with readable classical memory. NPU comparisons still require neural-workload semantics and full quality/latency/throughput/memory/data-movement/cost contracts.

## Surveillance boundary

The wider scan covered symbolic regression, differentiable/physics-informed models, automated experiment design, no-go/lower-bound results, and relevant provider documentation. The already-published 2026-10-23 optimization-law / ancilla-QFI watch remains the record for those two preprints. No additional verified project evidence was found for Pangola materials, bio-oil, fusion electricity, financing, manufacturing, or QPU execution.

Provider surveillance rechecked official documentation: IBM's September 2026 changelog already records `ibm_phoenix` for Premium, Flex, and Pay-As-You-Go plans; AWS Braket's current overview lists AQT, IonQ, IQM, QuEra, and Rigetti; Microsoft's Azure Quantum provider page lists IonQ, Pasqal, Quantinuum, and Rigetti, with QCI private preview. These observations are vendor documentation, not independent performance claims, and the IBM target is already represented in the repository's September market snapshot.

## Next highest-value gate

Keep the software-first QOS-AUDIT-010B25 read-only `ibm_kingston` snapshot as the highest hardware-transition gate, but do not bypass missing authorization or credentials. In parallel, execute `FND6-PROOF-001` on exact-commit CI and build the first false-claim theorem fixture. Do not submit paid or free QPU work without the required authorization; no QPU execution is part of this result.
