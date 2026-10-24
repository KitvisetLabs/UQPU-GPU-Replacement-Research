# Literature watch — 2026-10-24: formal mathematical discovery, verification boundaries, and UQPU equation gates

**Accessed:** 2026-10-24  
**Primary owner:** Lane H — strategic research/publication  
**Cross-lane consumers:** A–I; FND-001–006; EQN-001–006; INV-029, INV-034, INV-035  
**Evidence class:** `LITERATURE_ONLY` (one peer-reviewed research article; official research release; one unrefereed survey preprint)  
**Project evidence promotion:** none  
**Canonical start SHA:** `c7b5958af58fad04a101ef5c6abf6a29293c867e`

## Sources reviewed and what is genuinely new to this cycle

1. George Tsoukalas et al., [“Advancing mathematics research with AI-driven formal proof search,” *Science* 394(6820), 234–239, published 2026-10-08](https://pubmed.ncbi.nlm.nih.gov/42848891/), DOI [10.1126/science.aej2213](https://doi.org/10.1126/science.aej2213). The paper reports an AI proof-search agent resolving 9 of 353 attempted open Erdős problems and proving 44 of 492 OEIS conjectures; the authors also report that a simpler LLM/Lean feedback loop reproduced the Erdős successes. These are reported mathematical proof-search results, not UQPU results.
2. OpenAI, [“Sharing AI progress in mathematics,” 2026-10-06](https://openai.com/index/sharing-ai-progress-in-mathematics/), and its [public `openai/math` repository](https://github.com/openai/math). The initial release described 722 manuscripts in 372 families, with formal Lean artifacts for some but not all results. The upstream repository explicitly warns that unformalized results may contain issues and that formalizations continue to be added.
3. Ying Xie, [“What the Machine Invented: Mining New Mathematical Instruments from OpenAI's October 2026 Release of AI-Generated Mathematics,” arXiv:2610.17090, submitted 2026-10-12](https://arxiv.org/abs/2610.17090). This unrefereed survey examines 38 result families and extracts candidate lemmas, constructions, inequalities and proof mechanisms. Its own description says no Lean development was compiled or kernel-checked for that survey; novelty judgments are provisional.

The material delta for UQPU is not that AI has discovered a new physical law. It is that **AI-generated mathematical candidates can be routed through a formal proof checker as a distinct verification stage**, while literature mining and unverified natural-language arguments remain lower evidence classes. This suggests a useful proof-carrying interface for the equation-discovery pipeline.

## Evidence classification and limits

- The *Science* result is peer-reviewed evidence that formal proof-search workflows can solve a nonzero fraction of selected open mathematical problems. The reported denominators matter: it does not imply a high general success rate, automatic physical-law discovery, or guaranteed economics.
- A Lean proof certifies a statement relative to the formal definitions, axioms, imports and theorem actually checked. It does **not** by itself validate the choice of physical variables, empirical premises, dimensional interpretation, data provenance, causal mechanism, experimental applicability or an engineering claim.
- A symbolic fit, an AI-written manuscript, a literature survey, and a kernel-checked theorem are different evidence classes. Do not collapse them into a single “AI discovered a law” label.
- The public mathematical corpus has version/correction history. Any future UQPU reuse must pin the exact paper, repository revision, theorem statement, Lean environment and dependency hashes; a catalogue count is not a truth certificate.
- No source above supplies a UQPU workload result, target execution, material/fuel/electricity measurement, net-cost advantage, or independent physical replication.

## EQN-FORMAL-001 — schema-level gate implemented on this review branch

**Question:** Can a proof-carrying candidate format reduce false acceptance of algebraic equation-discovery outputs without hiding empirically false or non-identifiable models?

**Implemented in this PR branch:** `software/uqpu-prototype/uqpu/equation_discovery.py` now records formal-verification status, formal-system/statement/assumption/proof provenance, a pinned held-out split hash, counterexample-search status/provenance, a discriminating experiment protocol, and independent-replication status/provenance. Validation rejects missing or malformed proof/split hashes and incomplete completed-stage records. The physical-candidate gate now requires held-out improvement, a completed counterexample search with no counterexample found, and independent replication; a formal proof by itself cannot promote a concept. Focused tests were added in `software/uqpu-prototype/tests/test_equation_discovery.py`. The proof assistant itself is not invoked by this schema, and hosted CI is still pending.

**Candidate pipeline:**

1. **Generator:** `equation_discovery.py` (or a successor) emits a typed symbolic AST plus a separate natural-language rationale. The rationale is never the certificate.
2. **Constraint layer:** check declared units/dimensions, variable domains, symmetries, conservation conditions, causality assumptions, sign/positivity constraints and scaling/limiting cases. Unsupported constraints must be marked unknown, not silently assumed.
3. **Formal obligations:** translate only suitable algebraic identities, transformation rules, inequalities or theorem claims into Lean (or another proof assistant) with explicit definitions and axioms. Record whether the obligation is proved, disproved, or unresolved.
4. **Evaluator:** compare against a frozen incumbent model and simple baselines using the same data, compute/time budget and objective. Keep prediction score, symbolic complexity, proof status and resource use as separate fields.
5. **Held-out/generalization:** freeze train/validation/test split hashes before search. Test held-out conditions and out-of-domain scaling; do not tune against the final falsifier.
6. **Counterexample search:** generate boundary cases, singular/zero-probability cases, dimensional mismatches, symmetry violations, conservation violations and competing expressions with observationally equivalent predictions.
7. **Proof/simulation:** a formal proof establishes only its encoded mathematical statement; numerical simulation is separately labelled and must include solver/tolerance/convergence controls.
8. **Discriminating experiment:** state the observable that differs between the incumbent and candidate, the expected effect/uncertainty, controls, sample requirements and a stopping/failure criterion.
9. **Independent validation:** a separate implementation/reviewer must reproduce the formal and numerical checks before any device/system consequence is considered.
10. **Economics:** only after a candidate clears its relevant evidence gates may its effect be propagated into latency, throughput, energy, manufacturing, CAPEX/OPEX or cost per accepted useful task.

**Proposed benchmark and falsifiers:**

- Start with a small, version-pinned suite of known algebraic identities and dimensionally typed toy equations; include correct candidates, wrong-sign candidates, unit-inconsistent candidates, underdetermined alternatives and deliberately false natural-language rationales.
- Blind the generator to the canonical expression while preserving declared domain and constraints. Freeze all splits and hashes before generation.
- Measure false acceptance, false rejection, unresolved proof rate, counterexample yield, wall-clock/CPU use and reproducibility. Do not compare token count alone as total compute cost.
- Reject the method as an improvement if it fails to lower false acceptance at a matched budget, if proof obligations are satisfied only by overly strong/incorrect assumptions, or if held-out/experimental falsifiers still cannot distinguish non-identifiable candidates.
- Passing this benchmark would be **internal mathematical-tooling evidence only**. A candidate constitutive law or physical theory still requires empirical discrimination and independent replication.

## A–I integration edges

| Lane | Action from this literature delta | Boundary retained |
|---|---|---|
| A — workloads/compiler/runtime | Consider proof-carrying algebraic rewrites and semantic-equivalence obligations for candidate compiler/runtime transformations; preserve identical useful-output contracts and competitive CPU/GPU/NPU baselines. | A proof of a rewrite is not a QPU speedup or accepted-task advantage. |
| B — cloud/QPU/provider integration | Use formalized provider-neutral interface invariants where feasible; preserve no-submit preflight. | No credentials, provider session, job, shots or bill were used. |
| C — memory/state/data movement | Formalize addressability, output and information-accounting assumptions where mathematically suitable. | Hilbert-space dimension and QFI are not readable RAM/VRAM/storage capacity. |
| D — device/chip/process/packaging | Require explicit units, constitutive assumptions and bounded device-response obligations before downstream design claims. | No device, process-window, fabrication or packaging evidence. |
| E — biomass/materials/bio-oil/fusion/cooling | A future model may use formal checks for mass/energy balances and units; measured feedstock, product quality and net-energy inputs remain mandatory. | No Pangola material substitution, accepted fuel, or net delivered fusion-electricity result. |
| F — economics/benchmarks/evidence/finance | Keep proof status, measured outputs, resource budgets, uncertainty and cost per accepted task as separate typed fields. | Formal validity does not establish market cost, lower WACC or commercial viability. |
| G — manufacturing equipment/factory systems | Derive equipment/process requirements only from accepted D/device contracts; co-design continuously with D. | No manufacturing-tool or factory-capability result. |
| H — strategy/finance/future industries | Own this literature watch; preserve the Kanusanan Pongpanna Model and multilingual public references. | Strategic ambition remains separate from scientific/economic evidence. |
| I — contactless vehicle/levitation frontier | Formal proof methods may check the stated mathematical model and its assumptions. | No gravity/geomagnetic manipulation, levitation, propulsion or vehicle demonstration is implied. |

## Foundational and invariant contribution

- **FND-001:** no thermodynamic-gap value changes; formalize accounting identities only after variables, boundaries and units are explicit.
- **FND-002:** no output-information lower bound changes; proof obligations cannot turn state-space size into readable classical memory.
- **FND-003:** no matched control-vs-quantum-speed-limit measurement was made.
- **FND-004:** no alternative physical primitive is promoted.
- **FND-005:** no QFT/particle mechanism or anomaly is promoted.
- **FND-006:** the generator→constraints→proof/evaluator workflow gains a candidate formal-verification stage.
- **EQN-001–006:** all remain open/evidence-gated; `EQN-FORMAL-001` is a proposed test harness, not an implemented result or new law.
- **INV-029:** no evidence of physical Data-Center-to-One-Phone compression; remote infrastructure still counts.
- **INV-030:** no elemental transmutation claim; biomass remains a functional-substitution/minimization/recovery/hybridization/redesign program.
- **INV-031:** no accepted liquid-fuel or commercial bio-oil evidence.
- **INV-032:** no net reliable delivered fusion-electricity or commercial cost evidence.
- **INV-033:** no project-principal, interest-expense, WACC or economy-wide-rate result.
- **INV-034:** strengthens the mathematics-first research method while retaining physical and experimental boundaries.
- **INV-035:** AI may propose equations and proofs, but neither generated expressions nor formal validity alone establishes a physical law.

INV-025/026/027 and the 100× / 100,000,000× moonshots remain unproven. Existing later repository invariants are not weakened. The Thai, English, Chinese, Japanese, Korean and German master-plan links, AI-agent/One Person Business Company context, and strategic/funding references remain unchanged.

## Next gates

1. **Offline first:** implement or prototype `EQN-FORMAL-001` on the small adversarial suite; pin proof-assistant version and all assumptions; record false positives and failed candidates.
2. **Lane A priority:** continue the existing QOS-AUDIT-010B25 read-only target-snapshot contract only in an authorized environment. This literature result does not authorize credentials, a session, or any QPU job.
3. Reproduce the Oct-23 ancilla-QFI theorem separately on exactly solvable parameterized states before using it to constrain any UQPU architecture claim; resolve the paper's notation/assumption boundaries first.
4. Keep BIO-001, FUS-001 and FIN-001 at their current evidence class until measured inputs and complete functional-unit economics exist.

**Run conclusion:** literature delta plus schema-level validation code/tests on a review branch. No Lean proof, simulation, physical experiment, or provider execution was run by this cycle; hosted CI is pending. No project scientific or economic evidence was promoted.
