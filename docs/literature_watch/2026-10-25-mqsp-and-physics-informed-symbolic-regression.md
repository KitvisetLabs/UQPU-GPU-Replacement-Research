# Literature watch — 2026-10-25: experimental physics-informed equation discovery and QSP/QSVT reconciliation

**Search date:** 2026-10-25  
**Primary owner:** Lane A — quantum programming, workloads, compiler and runtime  
**Integration owner:** Lane F — evidence, benchmark and lifecycle-cost accounting  
**Cross-cutting:** Lane H publication; D/G resource co-design; FND-006; EQN-001–006; INV-025–027 and INV-029–035  
**Evidence class:** `LITERATURE_ONLY`  
**Canonical starting main:** `6af8ce896368ed993fe2b8278afa6082e1ecc916`  
**Project-evidence promotion:** none

## Executive delta

The current Batch 056 artifact is a bounded, single-matrix numerical QSVT fixture. Two cross-lane items were reviewed against the newest main state. The October 1 M-QSP preprint was **already recorded** in `docs/LITERATURE_WATCH_2026-10-17_MULTIVARIATE_QSP.md`; this cycle reconciles that existing follow-up with the newer QSP/QSVT feasibility watch and Batch 056. The new literature delta is a peer-reviewed September 8 paper reporting a **physics-informed symbolic-regression closure** for experimentally tracked spheres crossing water–salt and water–glycerol density interfaces. It is a compact, testable effective model tied to observed trajectories, not a new fundamental law.

Neither item is a UQPU benchmark result. M-QSP does not retroactively validate or invalidate Batch 056; the fluid-dynamics paper supplies no Pangola, semiconductor, fusion, or UQPU measurement.

## Cross-watch reconciliation — multivariate QSP transfer functions (previously recorded)

Guang Hao Low, “Multivariate Quantum Signal Processing,” arXiv:2610.01125, submitted 2026-10-01. Official preprint: https://arxiv.org/abs/2610.01125

### Relevant boundary and integration delta

This paper was already recorded by the project on 2026-10-17; it is not counted as a newly discovered source in this run. The current integration delta is to keep its multi-oracle contract separate from the newer QSP/QSVT feasibility and Batch-056 single-matrix gates.

The preprint treats matrix-valued transformations of multiple noncommuting, nonnormal block-encoded matrices through an analytic transfer-function framework analogous to multiport infinite-impulse-response filters. It reports uniform analytic bounds over the specified oracle promise and applies the framework to multi-term Hamiltonian simulation, sparse simulation, linear systems, differential equations, ground-state preparation/energy estimation, generalized eigenvalue problems, and selected coarse-grained Hamiltonian / graph-classification examples.

The useful project delta is not “QSVT is faster.” It is a more explicit way to describe **multi-oracle workload structure and per-oracle cost**. The reported weighted costs depend on block-encoding normalizations and oracle costs; they therefore motivate a richer workload contract than a single undifferentiated query count.

### Evidence class and limitations

- **Class:** preprint / theoretical algorithm result, not peer-reviewed evidence at the access date.
- The paper’s guarantees are conditional on its stated oracle model, transfer-function conditions, block encodings, normalization factors and error assumptions.
- The reported asymptotic query expressions do not automatically include application input preparation, state preparation, classical preprocessing, target-native synthesis, routing, QEC, readout/reconstruction, retries, energy, provider billing or accepted-output quality.
- The current repository’s Batch 056 is a static 2×2 Hermitian-contraction simulation with degree 81, 81 signal queries, 82 phase rotations, one signal ancilla, zero provider jobs/shots, and no gate decomposition or energy/cost measurement. M-QSP is not required to validate that narrow univariate fixture.
- The result is not evidence of quantum advantage, readable classical-memory replacement, or an end-to-end economic win.

### Falsifiable follow-up — QOS-MQSP-001

Freeze a small two-oracle workload family before implementation. Record each oracle’s identity, block-encoding normalization, query-cost unit, access assumptions, input/state-preparation cost, transfer-function target, approximation domain, error tolerance and accepted useful output. Use noncommuting, nonnormal matrices with a separately computed classical reference and held-out parameter instances.

Compare (a) a direct classical baseline, (b) a justified sequential/univariate QSP/QSVT construction, and (c) the M-QSP construction only where the full paper’s feasibility conditions are satisfied. Count each oracle call separately and also report the normalization/cost-weighted sum. Include counterexamples at boundary/degenerate instances, independent numerical evaluation of the transformed output, native-gate/resource estimates, host work, input/output bytes, reconstruction, retries and energy/cost where measurable.

**Reject or defer the M-QSP extension** if a claimed instance violates the theorem’s assumptions, held-out output error exceeds the frozen tolerance, the independent reference disagrees, a required oracle is not actually available, or total cost per accepted task is not improved under matched useful-output semantics. No real-QPU submission is authorized by this literature watch.

## New-to-this-watch source — physics-informed symbolic regression on measured particle-interface trajectories

Teddy Lazebnik, Chen Mortenfeld and Alex Liberzon, “Physics-informed symbolic regression reveals a delayed oscillatory closure for particle–interface dynamics,” *Machine Learning: Science and Technology* 7, 055004, published 2026-09-08. DOI: https://doi.org/10.1088/2632-2153/ae9c8b. Author publication page: https://acml.teddylazebnik.com/publications/physics-informed-symbolic-regression-reveals-delayed-oscillatory/

### Genuine novelty relevant to equation discovery

The study applies scientist-in-the-loop, physics-informed symbolic regression to high-resolution experimental trajectories of spheres crossing water–salt and water–glycerol density interfaces. It reports a compact delayed, exponentially damped oscillatory force closure that captures transient features such as slowdown, prolonged retention and rebound-like motion better than the selected virtual-mass baseline in the reported transient-rich cases. The search incorporates measured quantities and physical considerations including gravitational scaling, density contrast, interface width, viscosity, far-field behavior and dimensional consistency.

This is a concrete example of the INV-035 workflow in a narrow domain: experimental data and physical constraints guide a candidate generator; the selected expression remains a model whose generalization and mechanism require further tests.

### Evidence class and limitations

- **Class:** peer-reviewed, experiment-informed effective-model result in the stated fluid-dynamics domain.
- The selected equation is a domain-specific closure, not a universal law or a challenge to fundamental physics.
- The reported advantage is scoped to the studied trajectories, search space, model-selection choices and baseline. It does not establish universal extrapolation, unique identifiability, or independent replication.
- It has no direct evidence for Pangola-derived materials, critical-mineral substitution, fusion materials, bio-oil yields/costs, UQPU performance or financing.

### Falsifiable follow-up — EQN-PISR-001

If reusing this method in UQPU material/energy research, preregister the incumbent equation, variables and units, train/validation/held-out split by whole experimental conditions, permitted operators, symmetry/objectivity and conservation/thermodynamic constraints, baseline metrics, search/host-resource budgets and counterexample tests before generation. Hold out physical regimes such as interface thickness, viscosity or density contrast; measure uncertainty and false discoveries; and require independent data or experiments before promoting a candidate into a device/material model. Reject a candidate that wins only on training data, violates constraints, fails held-out regimes or cannot be independently reproduced.

This is a transferable *method* proposal only; the fluid experiment cannot substitute for project-specific material or energy validation.

## Cross-lane disposition

| Lane | Delta / interface | Status and boundary |
|---|---|---|
| A — programming/workloads/compiler/runtime | Separate multi-oracle M-QSP contracts from the existing single-oracle QSVT fixture; preserve equivalent-output baselines. | Literature-only; no M-QSP implementation or task advantage claimed. |
| B — cloud/QPU/provider integration | Make oracle availability, target identity, provider access and per-oracle price explicit. | No credentials, provider calls, jobs, shots or billing. |
| C — memory/state/storage/data movement | Include input preparation, state materialization, output bits, transfer and reconstruction. | No Hilbert-space/readable-memory equivalence. |
| D — device/chip/fabrication/packaging | Consume only later validated native-gate, depth, ancilla, control and error requirements. | No device or fabrication conclusion from query bounds. |
| E — biomass/materials/bio-oil/fusion/energy | Transfer the constrained-model method only when project-specific data exist. | No Pangola, accepted fuel, net fusion electricity or cooling evidence. |
| F — economics/benchmarks/evidence/integration | Count weighted oracle costs and all host, preparation, readout, retry and accepted-task costs. | No measured economic advantage; BIO-001/FUS-001/FIN-001 unchanged. |
| G — manufacturing equipment/factory systems | D/G co-design can consume future validated circuit/device requirements. | No process-window, yield or factory-cost claim. |
| H — strategy/finance/publication | Preserve the master-plan context and evidence typing. | No funding, principal, interest or WACC effect. |

Auxiliary Lane I remains auxiliary; it does not replace A–H. The six public master-plan languages (Thai, English, Chinese, Japanese, Korean and German), root directives 00–06, INV-025/026/027, and INV-029–035 remain required context. Existing INV-036/037 are left untouched.

## Literature-surveillance boundary

The 2026-10-25 targeted scan also checked symbolic/neural-symbolic equation discovery, AI-assisted theorem/proof search, differentiable/physics-informed modeling, automated experiment design, QSP/QSVT/query bounds, material constitutive models, biomass liquids, fusion net-electric cost and financing. The PISR source is newly added to the current repository watch; the M-QSP source is a cross-watch reconciliation. No directly relevant source dated 2026-10-24 or 2026-10-25 was identified that changes the current real-QPU, material, fuel, net-electricity, financing or Data-Center-to-Phone evidence gates. This is a bounded search result, not proof that no such source exists.

No new physical law is asserted. No third-party claim is project evidence. No paid QPU job was submitted.
