# Literature watch — 2026-10-25: formal proof search and physics-constrained equation discovery

**Accessed:** 2026-10-25  
**Primary owner:** Lane H — strategy, foundational research publication and future-industry integration  
**Integration owner:** Lane F — evidence, benchmark and cross-lane accounting  
**Feeds:** A–H; FND-001–006; EQN-001–006; INV-025–027; INV-029–035  
**Evidence class:** `LITERATURE_ONLY` (one peer-reviewed paper; related arXiv preprints)  
**Project evidence promotion:** none  
**Canonical starting main:** `c7b5958af58fad04a101ef5c6abf6a29293c867e`

## Executive delta

The 2026-10-23 repository watch already covers optimization-law discovery and a scoped ancilla-QFI no-go result. This cycle adds a different, currently unrecorded method signal: **AI-assisted formal proof search has reached a peer-reviewed, research-problem-scale demonstration**, while adjacent equation-discovery work suggests a useful separation between hypothesis generation, numerical search, and independent constraint inspection.

The practical UQPU implication is methodological, not a new physical capability: use a proof assistant to check mathematical statements and derivations when they can be formalized; use numerical symbolic regression to search candidate equations; and use independent constraint tests and held-out evidence to reject false candidates. A proof of a formal statement is only as relevant as the correctness and completeness of the formalization. It is not an experiment and cannot establish that a candidate equation describes nature.

Targeted searches on 2026-10-25 did not identify a directly relevant paper dated 2026-10-24 or 2026-10-25 that changes the project's current physical, QPU, biomass, fusion, or finance evidence. The peer-reviewed result below is dated 2026-10-08 and was missing from the repository's latest 2026-10-23 literature watch; the other sources are complementary preprints, not fresh project evidence.

## Sources and evidence classes

### 1. Peer-reviewed formal proof search at research-problem scale

George Tsoukalas et al., “Advancing mathematics research with AI-driven formal proof search,” *Science* 394(6820), 234–239, published 2026-10-08. DOI: [10.1126/science.aej2213](https://doi.org/10.1126/science.aej2213). Public bibliographic record: [PubMed](https://pubmed.ncbi.nlm.nih.gov/42848891/). The authors' preprint is [arXiv:2605.22763](https://arxiv.org/abs/2605.22763).

The reported agent resolved 9 of 353 attempted open Erdős problems and proved 44 of 492 attempted OEIS conjectures. Its important methodological contribution is the use of Lean-checked formal proof terms inside a search loop, including more elaborate agent coordination for difficult problems. The paper also reports that a basic generation/verification loop reproduced the Erdős successes, supporting the idea that kernel-checked feedback—not fluent natural-language reasoning alone—is a key trust boundary.

**Why it matters:** FND-006 and EQN-001–006 can benefit from separating (a) conjecture/equation generation, (b) formal proof obligations, (c) numerical tests, and (d) physical validation. Formal proof is especially useful for algebraic transformations, lower-bound derivations, invariants, and exact compiler/workload contracts.

**Limitations:** the success fractions are task-set-specific, not universal solve rates. Formal verification proves a statement relative to its formal statement, imports, axioms, and proof-assistant kernel; it does not by itself prove that the statement models a physical system, that the formalization captured every intended assumption, or that an experimental result is reproducible. Failed attempts and search/compute costs remain relevant. No UQPU code, physical equation, or mission result is validated by this third-party paper.

### 2. LLMs as symbolic-search controllers, not equation judges

Zikai Xie et al., “Language models guide symbolic equation discovery by controlling search,” [arXiv:2607.04156](https://arxiv.org/abs/2607.04156), submitted 2026-07-05; preprint at access time.

The authors assign the language model control over variables, operators, transformations, and search depth, while a symbolic-regression engine enumerates/fits candidates and deterministic metrics decide retention. They report tests on 74 AI-Feynman equations, seven complex formula-recovery tasks, and a battery dataset. The relevant design lesson is to let a generator influence the *search distribution* while retaining an explicit, reproducible evaluator.

**Limitations:** benchmark recovery of known equations is not blind discovery of a new law; dataset composition and task scope limit generalization; the preprint is not project validation. Search-cost accounting must include the LLM, symbolic engine, host runtime, energy, and all failed candidates rather than token count alone.

### 3. Independent physical-constraint inspection for constitutive models

Marius Tacke et al., “LLM-driven design of physics-constrained constitutive models: two agents are better than one,” [arXiv:2605.23754](https://arxiv.org/abs/2605.23754), v2 revised 2026-09-01; preprint at access time.

A Creator proposes constitutive models and an Inspector numerically probes stated physical constraints across deformation states, rotations, and perturbations. The reported pass-rate improvements differ by model backbone; the paper's result supports independent adversarial inspection as a useful filter, not a guarantee of physical validity.

**Limitations:** sampled numerical checks do not prove constraints globally; results are scoped to the studied constitutive-model families and datasets. A physically constrained fit still requires identifiability, held-out loading paths, uncertainty, experiments, and independent replication before being used as a material law.

## Synthesis: the missing boundary is typed verification, not another “AI discovered physics” label

The three methods support a layered pipeline:

1. **Generator/controller:** produce candidate equations, theorem statements, transformations, or search configurations.
2. **Explicit constraints:** dimensional consistency; domain; symmetry; conservation; thermodynamic admissibility; causality; known limiting cases; and the incumbent theorem/model.
3. **Deterministic evaluator:** numerical fit and complexity with pinned data, code, seeds, resource limits, and baseline.
4. **Held-out/generalization:** freeze train/validation/test splits before candidate selection; include out-of-domain regimes where scientifically justified.
5. **Counterexample search:** perturb parameters, boundaries, symmetries, noise, degeneracies, and adversarial inputs; preserve false discoveries.
6. **Proof or simulation:** use a pinned proof assistant for exact mathematical claims; use independently implemented simulation for numerical claims. Record theorem statement hashes, checker/tool versions, imported assumptions, and proof-admission policy.
7. **Discriminating experiment:** state a measurable observable that separates candidate and incumbent predictions.
8. **Independent replication:** use independent data, implementation, instrument, or team as appropriate.
9. **Device/system consequence:** derive explicit effects on compiler cost, memory/I/O, materials, energy, or controls.
10. **Economics:** count full lifecycle costs, failed attempts, host computation, energy, uncertainty, financing and time-to-evidence.

**Do not merge these gates.** A formally proved theorem can be physically irrelevant; a low-residual fit can be non-identifiable; a simulation can omit a dominant resource; and a physical effect can be too expensive to engineer. A candidate does not become a new physical law by passing only one gate.

## Proposed falsifiable follow-up: EQN-PROOF-001

**Objective:** determine whether formal-verification feedback reduces false mathematical claims in the UQPU equation-discovery pipeline without hiding failures or increasing total discovery cost beyond the measured benefit.

### Preregistered design

- Freeze a benchmark manifest and hashes before any run. Include exact mathematical identities/transformations already used by `fundamental_limits.py`, `frontier_hypothesis.py`, and `equation_discovery.py`, plus a separately labeled set of synthetic equation-recovery tasks with known ground truth.
- Pin the proof assistant, library revision, Python/tool versions, dataset versions, seeds, timeouts, and resource ceilings. If Lean is selected, reject proof terms with `sorry`/unapproved axioms and archive the exact theorem statement and imports. Any nontrivial axiomatic dependency must be listed rather than silently trusted.
- Compare at least four arms under matched total wall-clock and host-resource budgets: (i) existing deterministic contract/evaluator only; (ii) numerical symbolic regression; (iii) LLM-guided symbolic search; and (iv) candidate generation plus formal-proof feedback where a proof obligation is applicable.
- Keep separate scorecards for theorem/proof validity, equation recovery, held-out predictive error, dimensional/symmetry/conservation/causality checks, counterexample discovery, candidate complexity, false-discovery rate, wall-clock, tokens, host compute, energy where measurable, and total cost. Count all failed searches and retries.
- For physical/material candidates, predeclare a discriminating observable and blind prediction before any experiment. Formal proof cannot replace measured constitutive behavior, a material qualification test, or independent replication.

### Pass/fail rules

- **Mathematical-verification pass:** every accepted proof artifact checks against the frozen statement under the pinned kernel; no hidden admissions or statement drift. Failed proof attempts remain in the ledger.
- **Equation-discovery pass:** the candidate beats the incumbent on a predeclared held-out criterion and survives adversarial counterexample checks under matched resource accounting. A fit-only win is insufficient.
- **Physical-promotion gate:** remains closed until an independent experiment/replication supports the discriminating prediction and the full system/economic consequence is measured. No automatic promotion from `CONCEPT`, `THEORY`, `MODEL_ONLY`, `SIMULATION`, or `LITERATURE_ONLY`.
- **Null/failure outcome:** if formal feedback fails to improve verified correctness, false-discovery rate, or useful discovery per total resource, record the negative result and keep the simpler pipeline.

### Mission relevance

- **INV-029 / A:** proof-checkable workload transformations may improve compiler correctness and auditable service contracts, but they do not compress remote infrastructure into a phone.
- **INV-030 / D–G:** independent constitutive-constraint inspection can inform carbon-material candidates; no Pangola-derived material substitution is demonstrated.
- **INV-031 / E:** formal mass/energy-balance identities may help audit BIO-001 accounting; no saleable bio-oil, yield, or cost result is added.
- **INV-032 / E:** proof can check model algebra, not net fusion electricity, availability, lifetime, or commercial cost.
- **INV-033 / F–H:** resource accounting may shorten time-to-evidence or reduce wasted search principal; no financing-rate/WACC effect is measured.
- **INV-034 / FND-006:** strengthens mathematics-first invention and explicit proof/counterexample retention.
- **INV-035 / EQN-001–006:** adds a formal-verification option to the discovery chain while preserving empirical falsification.

## A–H review

| Lane | This cycle's contribution | Boundary / next gate |
|---|---|---|
| A — workloads/compiler/runtime | Defines a proof-checkable transformation gate for mathematical/compiler claims. | Implement EQN-PROOF-001 on frozen workload/equation fixtures; no compiler performance claim. |
| B — cloud/QPU integration | Requires proof/equivalence checks before provider lowering where a transformation admits exact semantics. | No provider call, credential use, target snapshot, QPU job, shot, or billable usage. |
| C — memory/state/I/O | Keeps information bounds and state-space dimension distinct from readable classical memory. | No RAM/VRAM/HBM/storage equivalence or data-movement reduction measured. |
| D — device/chip/process/packaging | Adds constraint-inspection as a candidate filter for device/material equations. | No fabrication, device, yield, reliability, or physical-material result. |
| E — biomass/materials/bio-oil/fusion/energy | Identifies where formal mass/energy balance and constitutive constraints can be audited. | BIO-001 and FUS-001 remain MODEL_ONLY/DATA_BLOCKED; no commercial evidence. |
| F — economics/evidence/integration | Specifies matched-budget evaluation and failure-cost accounting. | No accepted-task cost advantage, measured energy benefit, or financing effect. |
| G — manufacturing equipment/factory systems | Requires validated device requirements before manufacturing consequences are inferred. | D/G co-design remains active; no tool/factory requirement derived from this literature alone. |
| H — strategy/publication | Publishes the method boundary and falsifiable follow-up. | Strategic master plan remains context, not scientific proof. |

INV-025/026/027 remain evidence-gated. Lane I in the current repository manifest is auxiliary to this A–H review and does not replace the permanent A–H mission architecture.

## Cross-cutting foundational status

- **FND-001:** the open FND-001 accepted-task Landauer-gap contract is a software accounting guard only; this literature does not supply measured wall-plug energy or erased-bit counts.
- **FND-002:** no output-information lower bound is changed; never infer readable bits from qubit count/Hilbert-space dimension.
- **FND-003:** no matched control-vs-quantum-speed-limit measurement is supplied.
- **FND-004:** no alternative physical primitive is demonstrated.
- **FND-005:** no QFT/particle mechanism, new particle, or anomaly is established.
- **FND-006:** formal proof search is a candidate tool for exact mathematics, subject to frozen statements and explicit assumptions.
- **EQN-001–006:** candidate generation/evaluation remains evidence-gated; add formal proof where applicable, and retain held-out, counterexample, experimental, replication and economics gates.

## Other surveillance lanes and non-claims

The targeted review also checked symbolic-regression control, physics-informed/constitutive modeling, automated discovery, optimization-law work, QFI/no-go literature, and relevant energy/material/fusion/finance terms. No new source found in this pass changes the project's current BIO-001, FUS-001, FIN-001, provider-execution, or Data-Center-to-Phone evidence. This is a literature-search boundary, not proof that no such source exists.

No real-QPU, material, fuel, net-electricity, financing, physical-law, or quantum-advantage result is claimed. No paid provider job was submitted. No credentials were used. No new physical law is proposed by this watch.
