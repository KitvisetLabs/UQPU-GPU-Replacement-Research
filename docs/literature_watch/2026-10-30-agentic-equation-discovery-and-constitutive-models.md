# Literature watch — 2026-10-30 — agentic equation-discovery runtimes and structure-preserving constitutive discovery

**Date checked:** 2026-10-30  
**Primary owner:** Lane D — device/material constitutive-model transfer  
**Cross-lane interfaces:** A, C, E, F, G, H; upstream FND-001/002/006 and EQN-001–006  
**Evidence class:** EXTERNAL ARXIV PREPRINTS + AUTHOR-REPORTED BENCHMARKS / EXPERIMENTAL-DATA FITS / HIGH-FIDELITY SIMULATION. No UQPU reproduction or project evidence is created here.  
**Starting canonical main SHA:** `41fac3953773ae0016a09539be57c3ed6b379771`

## Executive delta

Four previously unindexed primary preprints materially extend the project’s equation-discovery and constitutive-modeling surveillance:

1. **SRHarness v2** separates agentic symbolic-regression search logic from a reusable scientific runtime: composable actions, persistent candidate/evidence state, a shared evaluator and explicit trajectory lifecycle.
2. **Hyperreduction for neural-material discovery** combines POD, energy-conserving sampling/weighting (ECSW), adaptive reduced bases and adjoint sensitivities to lower the cost of inverse finite-element constitutive identification while retaining full-order checks.
3. **GINNGER** learns thermodynamic generators (entropy and an anisotropic friction operator) under the GENERIC structure rather than directly fitting an unconstrained constitutive operator.
4. **Physics-constrained symbolic regression for ZPG wall turbulence** combines classical asymptotic structure with staged symbolic searches for near-wall and Reynolds-dependent corrections.

These are method leads, not new physical laws. Only the hyperreduction paper reports fits to two experimental datasets; GINNGER's validation is simulation-based. None is Pangola-specific, and none establishes UQPU material, fuel, device, energy or economic advantage.

## 1. SRHarness v2 — symbolic-regression runtime as a first-class research component

**Source:** Zihan Yu, Shixuan Zhou, Hao Huang, Jingtao Ding and Yong Li, “SRHarness: A Harness for Agentic Symbolic Regression,” arXiv:2609.35501v2, revised 2026-10-24.  
**Primary source:** https://arxiv.org/abs/2609.35501  
**Full text:** https://arxiv.org/html/2609.35501v2  
**Paper license shown by arXiv:** CC BY-NC-ND 4.0. The linked code repository is https://github.com/tsinghua-fib-lab/SRHarness; its separate code license, immutable revision, dependencies and data provenance were not audited.

### Genuine novelty

The paper explicitly separates the base model, search strategy and harness. The harness contributes:
- composable scientific actions operating on raw, transformed and candidate-derived quantities under one task context;
- a shared evaluator and consistent fit/validation semantics across search tools;
- persistent scientific state retaining candidate equations, scores, residual evidence, provenance and dependency links across conversation branches/restarts;
- trajectory lifecycle management for continuation, branching, restart and termination under an explicit search budget.

On LLM-SRBench, the authors report 93.69% symbolic accuracy on LSR-Transform versus 62.16% for SR-Scientist under the matched DeepSeek-v4-flash-0731 backbone; on the anonymized condition they report 72.97% versus 39.64%. These are benchmark-specific author-reported results, not UQPU measurements.

### Limitations and exact UQPU relevance

- The benchmark comprises 128 synthetic LSR-Synth problems and 111 transformed-equation LSR-Transform problems; the anonymized condition reuses the same numerical values while removing semantic labels.
- Search sees an 80/20 fit/validation split of official training observations; official ID and OOD test sets are withheld until final submission. This is a useful leakage-control pattern for EQN work.
- Reported model/API usage, token counts and wall time are benchmark-specific and cannot be transferred to UQPU cost/task.
- The paper's CC BY-NC-ND license applies to the paper; do not assume the code or datasets have the same license.

**UQPU path:** compare the current `equation_discovery.py` workflow with a persistent, typed candidate/evidence ledger. Candidate records should bind the exact equation, units, variable definitions, dimensional/symmetry/conservation/causality checks, train/validation/test partition, evaluator version, residuals, counterexamples, proof/simulation status, falsifier, source/run hashes, false-discovery state and total search resources. A restart must not erase failed hypotheses or promote a validation score into a physical-law claim.

## 2. Hyperreduction for neural-material discovery

**Source:** Hagen Holthusen, Matthias Knipper and Kevin Linka, “Hyperreduction accelerates finite element model updating for the discovery of neural materials,” arXiv:2610.31322v1, submitted 2026-10-22.  
**Primary source:** https://arxiv.org/abs/2610.31322  
**Full text:** https://arxiv.org/html/2610.31322v1  
**Paper license shown by arXiv:** CC BY 4.0. The implementation is described as in-house ASIMOV built on JAX; no public source repository was identified in the paper.

### Genuine novelty and reported evidence

The method combines proper orthogonal decomposition (POD), energy-conserving sampling and weighting (ECSW), adjoint sensitivities of the reduced model, and adaptive updates of the trial space and sampled elements as neural-network weights evolve. A polyconvex neural energy is constructed using a zero-anchored input-convex architecture, logarithmic normalization and a growth term.

The authors report two experimental-data cases and one synthetic 3-D case. For a two-phase specimen, the reported training time falls from about 9 hours to 41 minutes relative to full-order identification. The synthetic 3-D case uses six modes in place of 48,672 degrees of freedom and 116 of 15,625 elements for internal-force evaluation. The reported timings were obtained in double precision on a 10-core Apple M4 CPU with 24 GB memory, not a GPU or QPU.

### Limitations that matter

- Full-order bootstrap/canary checks remain material to total runtime; in the first case canary epochs account for about 41% of wall time. The paper estimates an upper speed-up bound of about 28× even if reduced epochs were free.
- Reduced-model efficiency degrades with localized deformation; stale snapshots require expensive full-order checks/rebuilds.
- Reaction-force fit does not uniquely identify a material. The paper explicitly shows that the force constrains the energy only along deformation states activated by the experiment; additional displacement fields, specimens and load paths improve identifiability.
- The demonstrated constitutive class is isotropic hyperelasticity. Anisotropic extension is discussed, not demonstrated; inelasticity requires history-dependent adjoints.
- Generated study data were to be released upon publication; the two experimental source datasets are separately identified. UQPU has not retrieved, pinned, installed or reproduced the implementation.

**UQPU path:** add this as a Lane D/E/G method comparator to the existing Neural-DFEM/Pangola transfer gates. Reproduce one source case against full-order FE, then use an independent mesh/solver and a localization negative control. Measure total wall time including bootstrap, canaries, basis rebuilds, full-order checks, peak memory, energy and data movement. Do not transfer an isotropic hyperelastic model to Pangola composites until measured coupons establish the relevant material class and deformation coverage.

## 3. GINNGER — thermodynamic-generator discovery for rheology

**Source:** Imanol García de Beristain, David Nieto Simavilla and Marco Ellero, “A GENERIC-Informed Neural Network for Generative Rheology,” arXiv:2610.23352, submitted 2026-10-16.  
**Primary source:** https://arxiv.org/abs/2610.23352  
**Full text:** https://arxiv.org/html/2610.23352  
**Evidence class:** ARXIV PREPRINT / HIGH-FIDELITY SIMULATION VALIDATION.

### Genuine novelty

The authors recast constitutive discovery as learning the thermodynamic generators from which constitutive equations follow. A two-stage method learns a polymer configurational entropy and its conjugate tensor from stress/conformation data, then learns an unknown anisotropic friction operator from conformation dynamics. GENERIC degeneracy/structure is embedded in training to constrain energy conservation, entropy production and material objectivity. A spectral representation of the conformation tensor is used to combine shear, extensional and mixed-flow data in a common microstructural state space.

### Limitations and exact relevance

The abstract and full text describe high-fidelity simulation validation and predictions across unseen geometries; this is not an independent experimental campaign or a demonstrated new physical law. The framework is specific to polymeric rheology and makes assumptions about the conformation tensor as a complete microstructural state and affine deformation in the presented setup. Code/license and independent replication were not verified.

**UQPU path:** treat GENERIC as a candidate constrained model class for FND-001/EQN-001/006 and, only if relevant measurements exist, rheology of biomass slurries or bio-oil process streams. A follow-up must verify the degeneracy identities (reversible energy conservation and non-negative irreversible entropy production), objectivity, units, positive-semidefinite dissipation, limiting cases and held-out flow protocols. No Pangola slurry or bio-oil property is inferred from this polymer model.

## 4. Physics-constrained symbolic regression for ZPG wall turbulence

**Source:** Xianglin Shan and Weiwei Zhang, “Physics-Constrained Symbolic Regression for Mean-Velocity and Mixing-Length Scaling in Zero-Pressure-Gradient Turbulent Boundary Layers,” arXiv:2610.35276v1, submitted 2026-10-26.  
**Primary source:** https://arxiv.org/abs/2610.35276  
**Full text:** https://arxiv.org/html/2610.35276v1  
**Evidence class:** ARXIV PREPRINT / DATA-FITTED MODEL WITH DNS, LES AND EXPERIMENTAL PROFILE COMPARISONS.

### Genuine novelty

A staged PySR search retains prescribed near-wall and overlap asymptotics, then fits transition functions and Reynolds-number-dependent outer corrections. The mean-velocity expression is compared with 35 profiles from DNS, LES and experiments across friction Reynolds numbers 252–72,526. The effective mixing-length relation is evaluated only on 21 numerical-simulation profiles because the required Reynolds shear stress is not available in the experimental profiles.

### Limitations and exact relevance

- Classical logarithmic/Prandtl structures and asymptotic exponents are supplied as physical priors; the search does not discover those incumbent laws from scratch.
- The Reynolds-dependent coefficient fitting uses five DNS/LES profiles; the remaining profile comparisons are described as out-of-fit, but not as a statistically independent held-out validation set.
- The high-Reynolds-number limits 0.67 and 0.229 are prescribed asymptotic targets/soft constraints, not independently established universal constants.
- The Coles wake shape is fixed and its reference coefficient is least-squares calibrated rather than discovered by a new symbolic search.
- The domain is incompressible, smooth-wall, zero-pressure-gradient boundary layers. No claim is made for other turbulence regimes.

**UQPU path:** use the staged separation of prior physics, fitted corrections and post-fit asymptotic checks as an EQN-001/003/004 test pattern. Reproduce from pinned data/code, then reserve genuinely independent Reynolds-number/profile families and test dimensional consistency, asymptotic limits, residual structure and counterexamples. A fitted expression is not a new law.

## 5. Cross-lane integration and falsifiable follow-up

| Lane | Integration edge | Next gate |
|---|---|---|
| **A — programming/runtime** | SRHarness suggests persistent hypothesis/evidence state and one evaluator across equation-generation tools. | Compare a typed candidate ledger with the existing `equation_discovery.py`; preserve failed runs and enforce train/validation/test isolation. |
| **B — cloud/QPU** | No provider or QPU result in these papers. | If later accelerated, bind target, runtime, calibration, billable usage and price to the same run; simulator first. |
| **C — memory/state/data movement** | Persistent scientific state and FE snapshots create explicit storage/I/O obligations. | Measure archive bytes, checkpoint/rebuild I/O, peak memory and transfer; do not infer from state dimension. |
| **D — devices/material constitutive models** | Hyperreduced FE inverse identification is a new external method lead. | Pin/reproduce source case, full-order canary and independent mesh/solver checks; test localization and non-uniqueness negatives. |
| **E — biomass/materials/energy** | GENERIC is a candidate rheology constraint; hyperreduction may reduce future material-model calibration cost. | No Pangola transfer until measured feedstock-derived coupons/fluids identify a compatible constitutive class and independent tests. BIO-001/FUS-001 remain open. |
| **F — economics/evidence** | Training-time claims require full-order checks, rebuilds, compute hardware and energy to be included. | Report full cost per accepted model/material prediction; separate literature time savings from project economics. |
| **G — manufacturing/factory** | Constitutive models could inform process windows and metrology only after physical qualification. | Link measured orientation, porosity, cure, defects and lot variation to validated models; no equipment/yield result yet. |
| **H — strategy/publication** | The methods expand candidate discovery options without changing strategic claims. | Preserve source provenance and publish only reproduced project results; multilingual master-plan and AI/funding references remain unchanged. |

### Required all-pairs scan (28 pairs)

- A–B: runtime-to-provider lowering; no provider execution.
- A–C: persistent candidate/state storage and I/O; unmeasured.
- A–D: equation/material-model interface; no constitutive reproduction.
- A–E: rheology/biomass workload candidate; no Pangola measurements.
- A–F: evaluator and full accepted-task cost; no project benchmark.
- A–G: model requirements to process/metrology; no process data.
- A–H: discovery workflow to strategic publication; no mission milestone.
- B–C: target memory/I/O constraints; no target selected.
- B–D: device-native execution constraints; no native mapping.
- B–E: provider power/cooling interface; no facility data.
- B–F: same-target price and runtime accounting; no billable run.
- B–G: provider device specs to factory constraints; no manufacturing data.
- B–H: provider landscape to strategic plan; no new provider result.
- C–D: material/device state and FE snapshot representation; no measured storage.
- C–E: feedstock/process data and storage; no measured process stream.
- C–F: state/archive bytes to lifecycle cost; unmeasured.
- C–G: metrology and process-data pipeline; no equipment data.
- C–H: data infrastructure to strategic model; no validated capacity claim.
- D–E: constitutive class to Pangola composite qualification; blocked on coupon evidence.
- D–F: FE model fidelity/runtime to cost per accepted prediction; no UQPU run.
- D–G: material/device acceptance to process window/metrology; co-design retained, no factory result.
- D–H: qualified material capability to industrial strategy; no qualification.
- E–F: accepted-liquid and net-electric economics; BIO/FUS remain open.
- E–G: biomass processing/fusion infrastructure equipment; no process/plant measurement.
- E–H: Pangola/bio-oil/fusion deployment to strategic finance; no commercial evidence.
- F–G: equipment throughput/yield to cost-per-good-device; no yield data.
- F–H: financed principal/interest and project sequencing; FIN-001 remains model/literature only.
- G–H: factory capacity and future-industry planning; no manufacturing evidence.

Selected 3+ lane combinations: A+C+F for equation-search runtime/state/cost; A+D+E+F+G for material inverse discovery and process qualification; E+F+H for Pangola/bio-oil/fusion/finance; FND/EQN feeding A–H. All remain PROPOSED or BLOCKED; no combined empirical integration was executed in this cycle.

## 6. Equation-discovery and evidence gates

For all four sources, preserve the required sequence:

1. generator/search method and immutable source/configuration;
2. explicit dimensions, variable semantics, symmetries, conservation/thermodynamic constraints and admissible model class;
3. evaluator with a pinned baseline and identical metrics;
4. genuinely held-out data/trajectory/regime tests;
5. counterexample search and negative controls;
6. proof or numerical verification where applicable;
7. discriminating experiment and independent replication;
8. device/material/system consequence;
9. measured energy, runtime, lifecycle cost and financing.

Record false discoveries, failed runs, non-identifiability, out-of-domain failures and missing data as first-class outcomes. No symbolic fit, synthetic simulation, external preprint or AI-generated equation is a physical law by declaration.

## 7. Project status / non-claims

- FND-001–006 and EQN-001–006 remain active; no new thermodynamic measurement, lower bound, quantum-speed-limit result, alternative physical primitive, particle mechanism, theorem or validated physical equation was produced.
- INV-029: no phone-class physical compression or data-center service replacement.
- INV-030: no Pangola-derived material qualification, functional substitution or elemental transmutation.
- INV-031: no accepted Pangola liquid fuel, net plant-energy or commercial-cost result.
- INV-032: no net reliable fusion electricity or commercial lifecycle cost.
- INV-033: no project principal, interest, hurdle-rate or WACC reduction.
- INV-034/035: the candidate-search methods broaden the mathematics-first agenda; present physics remains binding and all alternatives remain hypotheses until discriminating evidence passes.
- INV-025/026/027: 100,000,000-unit/GPU goals remain falsifiable moonshots; no memory equivalence or NPU advantage is established.
- All eight root mission directives, the Kanusanan Pongpanna Model, six-language public master-plan references and strategic AI-agent/funding references remain unchanged.

**Next highest-value gate:** Lane D pins and reproduces the hyperreduction paper's first experimental case (including full-order/canary cost) while Lane A creates a non-invasive candidate/evidence-ledger adapter for `equation_discovery.py`. In parallel, correct the QAOA pilot's test-split protocol before any matched optimizer run: its current manifest says test is evaluation-only but also permits per-instance angle optimization on test objectives. Freeze test parameters using train/validation only, or separate any per-instance adaptation into a distinct protocol with independent evaluation shots; do not describe the latter as held-out generalization.

**No paid QPU job, material coupon test, fuel production, fusion experiment or financing transaction was performed.**
