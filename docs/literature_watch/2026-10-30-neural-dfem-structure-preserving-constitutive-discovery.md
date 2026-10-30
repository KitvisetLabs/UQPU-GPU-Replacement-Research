# Literature watch — 2026-10-30 — structure-preserving constitutive discovery with differentiable FEM

**Primary source:** Francesco Regazzoni, “Hyperelastic constitutive model discovery with differentiable finite elements and structure-preserving neural networks,” *Computational Mechanics* (2026), published 2026-09-06. [Publisher article / DOI 10.1007/s00466-026-02850-2](https://doi.org/10.1007/s00466-026-02850-2).  
**Official preprint:** [arXiv:2603.26517](https://arxiv.org/abs/2603.26517), submitted 2026-03-27.  
**Code source:** [FrancescoRegazzoni/Neural-DFEM](https://github.com/FrancescoRegazzoni/Neural-DFEM). The public repository page declares BSD-3-Clause and showed three commits when inspected; no immutable commit SHA or local source-tree hash has yet been pinned.  
**Evidence class:** Peer-reviewed original method with synthetic numerical validation; external source only. UQPU has not installed or reproduced it.  
**Owners:** Lane H — literature publication; Lane D — constitutive/device-material transfer contract; Lane E — Pangola-material qualification; Lane G — process/metrology co-design; Lane F — evidence and lifecycle economics.  
**Feeds:** INV-030, INV-034, INV-035, EQN-003/EQN-005/EQN-006; interfaces D/E/F/G/H.

## Genuine methodological novelty

The paper embeds a differentiable finite-element equilibrium solve inside the constitutive-learning loop. Candidate strain-energy densities are evaluated through the displacement fields and global reaction forces they induce, so training can use dense boundary-displacement observations and global reactions without paired local stress–strain measurements or full-field interior displacement data.

Its Hyperelastic Neural Network construction is designed to enforce, by architecture, a set of mechanical admissibility properties including a stress-free reference state, frame indifference, isotropic material symmetry, polyconvexity, coercivity and controlled volumetric growth. Momentum balance is imposed through the finite-element solve during training. The article reports two- and three-dimensional numerical tests, including geometry/loading-condition holdouts and synthetic noise sweeps.

This is a useful *methodological* advance for inverse constitutive modeling: it couples the candidate material law to the forward mechanics and makes structural constraints part of the hypothesis class rather than relying only on penalty terms in a loss function.

## Source and environment observations

The public code repository states that it contains the implementation and configurations used for the paper. Its README lists a legacy environment: Python 3.8.12, FEniCS 2019.1.0, dolfin-adjoint 2023.0.0, NumPy 1.21.4 and pandas 1.3.4. This is repository-page metadata, not a verified clean installation. The upstream commit, source bytes, configuration/data bytes, dependency closure and exact license text still require independent pinning and verification before reproduction.

## Limitations and evidence boundary

- The numerical assessment uses synthetic data generated from known constitutive models. The authors explicitly identify validation on real experimental measurements as future work.
- Data generation and identification use the same finite-element discretization and solver. This controlled design isolates learning/generalization effects but may make absolute errors optimistic when discretization or solver implementations differ.
- The present formulation is restricted to path-independent hyperelasticity and isotropic materials. History-dependent behavior requires substantial changes; anisotropy requires a different or extended invariant set.
- The polyconvex hypothesis class cannot represent genuinely non-polyconvex responses with arbitrary accuracy. The paper's three-dimensional Ishihara example demonstrates a representational mismatch; a residual error is not automatically an optimizer defect.
- Prediction quality deteriorates when held-out local strain-state distributions move away from the training regime. Finite observations do not guarantee unique recovery of the underlying strain-energy function.
- Boundary observations in the reported setups are dense measurements over the specimen boundary together with global reactions, not arbitrary sparse sensors.
- The work concerns mechanical constitutive response. It does not establish electrical conductivity, thermal conductivity, corrosion resistance, wear life, semiconductor compatibility or any other Pangola-carbon functional substitution.
- A structurally admissible learned constitutive model is not automatically a new physical law. It is a candidate model within stated assumptions and a particular material domain.

## Exact UQPU and strategic relevance

**INV-030 / Lane D–E–G:** The method may help qualify mechanical response of a future engineered composite when independent measurements show that the material is adequately described as isotropic, path-independent hyperelasticity. For Pangola-derived carbon composites, first determine whether anisotropy, binder response, porosity, viscoelasticity, plasticity, cracking/damage, rate effects or temperature dependence invalidate this model class. Carbon processing must never be described as elemental transmutation. A valid material claim must compare the required function and lifecycle cost per accepted functional unit.

**D/G co-design:** If a candidate composite is relevant to a device, manufacturing orientation, porosity, binder fraction, cure/activation, layer thickness, defects and contact/interface quality must be measured as process variables. Lane G's metrology and process-window evidence must feed Lane D's material acceptance envelope. No device or manufacturing result follows from this paper.

**INV-034/035:** Differentiable solvers and structure-preserving model classes are useful candidate generators/evaluators. Their mathematical constraints narrow the search space; they do not replace held-out tests, counterexample search, real measurements or independent validation. No equation or physical law is promoted.

**INV-029/031/032/033:** This source does not advance phone-class physical compression, accepted biomass liquid fuel, net delivered fusion electricity or project financing/interest reduction.

## Falsifiable follow-up

1. Pin the upstream Neural-DFEM commit, source-tree SHA-256, exact license, configuration files and data provenance. Record all dependency versions and build a reproducible isolated environment; do not silently modernize the numerical stack during the first reproduction.
2. Reproduce one published 2D Mooney–Rivlin training setup and its held-out geometry/loading cases. Compare displacement and reaction-force metrics with the paper's definitions and preserve all failed seeds and solver failures.
3. Repeat at least one case with an independently implemented or independently versioned finite-element solver and a mesh/discretization mismatch. A same-solver reproduction alone is insufficient to establish robust transfer.
4. Include the reported non-polyconvex Ishihara case as a negative/representational control. Separate optimizer failure, solver failure, insufficient strain-state coverage and hypothesis-class mismatch.
5. Before any Pangola transfer, characterize real coupons under cyclic tension/compression/shear, multiple rates, temperatures and orientations. Use DIC boundary fields and reaction-force data, plus independent local strain–stress measurements for validation. Establish whether the response is isotropic, path-independent and hyperelastic before selecting this ansatz.
6. Hold out geometries, loading paths, strain-invariant regions, manufacturing lots and measurement sessions. Search for counterexamples to objectivity, symmetry, stability, coercivity and generalization. Quantify identifiability and uncertainty rather than assuming one fitted energy is unique.
7. Only after mechanical validation, test the separate target function (e.g. electrical/thermal/mechanical role), service life, recovery/recycling and full cost per functional unit. Do not infer a critical-material substitution from a mechanical fit.

**Promotion rule:** external method → pinned assets → reproduced synthetic benchmark → independent solver/mesh checks → real coupon data → held-out independent validation → device/material functional test → lifecycle economics. No stage is skipped.

**Nonclaims:** no UQPU reproduction, no Pangola material result, no critical-material substitution, no elemental transmutation, no new physical law, no real-QPU advantage and no commercial/economic result is established by this watch.
