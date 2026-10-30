# Focused research gap — Neural-DFEM constitutive-model transfer to Pangola-derived materials

**Gap ID:** RG-D-NEURAL-DFEM-MATERIAL-TRANSFER-001  
**Date:** 2026-10-30  
**Primary owner:** Lane D — device/material constitutive modeling  
**Interfaces:** Lane E (Pangola materials and functional requirements), Lane G (process/metrology), Lane F (uncertainty and lifecycle cost), Lane H (publication/strategic integration)  
**Status:** OPEN / LITERATURE_ONLY / UPSTREAM REPRODUCTION NOT RUN  
**Evidence class:** PEER_REVIEWED_METHOD + SYNTHETIC_NUMERICAL_VALIDATION (external only)  
**Literature watch:** [2026-10-30 Neural-DFEM watch](literature_watch/2026-10-30-neural-dfem-structure-preserving-constitutive-discovery.md)  
**Lane D contract:** [NEURAL_DFEM_CONSTITUTIVE_MODEL_TRANSFER_CONTRACT_2026-10-30.md](../research_lanes/D_device_chip_fabrication_packaging/NEURAL_DFEM_CONSTITUTIVE_MODEL_TRANSFER_CONTRACT_2026-10-30.md)

## Objective

Determine whether the differentiable-FEM / structure-preserving hyperelastic model-discovery method of Regazzoni (2026) can be independently reproduced and, only if the material class is appropriate, transferred to a measured engineered composite relevant to INV-030.

The immediate question is methodological: can boundary displacement and reaction-force observations identify a mechanically admissible constitutive model under controlled conditions, with a demonstrable generalization envelope? It is not yet a Pangola substitution project result.

## Pinned external source

- Regazzoni, *Computational Mechanics* (2026), published 2026-09-06, DOI 10.1007/s00466-026-02850-2.
- Official preprint: arXiv:2603.26517, submitted 2026-03-27.
- Upstream code: https://github.com/FrancescoRegazzoni/Neural-DFEM
- Public repository page declares BSD-3-Clause and lists Python 3.8.12, FEniCS 2019.1.0, dolfin-adjoint 2023.0.0, NumPy 1.21.4 and pandas 1.3.4.
- **Not yet pinned:** upstream commit SHA, source-tree hash, dependency lock, exact license bytes, data/config hashes and full asset provenance.

## Current evidence

The peer-reviewed article reports synthetic two- and three-dimensional tests in which a differentiable finite-element solver is embedded in training. The candidate hyperelastic class is designed to enforce stress-free reference, frame indifference, isotropic symmetry, polyconvexity, coercivity and controlled volumetric growth. Boundary displacement and global reaction observations are used in the reported partial-observation cases.

The authors state that real experimental validation remains future work and that data generation and identification use the same FE discretization and solver. The framework is restricted to isotropic, path-independent hyperelasticity; non-polyconvex responses may not be represented arbitrarily, and generalization depends on coverage of the local strain-state distribution. UQPU has not downloaded, installed, run or independently reproduced the upstream code.

## Blocking unknowns

1. Exact upstream source revision, source-tree hash, data/config bytes and license verification.
2. Whether the listed legacy FEniCS/Python environment can be reproduced cleanly and securely.
3. Whether the reported training/testing commands reproduce the paper's metrics and runtime.
4. Whether results survive an independently versioned FE solver, mesh mismatch and disjoint strain-state holdouts.
5. Whether a real Pangola-derived composite is isotropic, path-independent and hyperelastic at all; this cannot be assumed.
6. Whether mechanical response is even the function that matters for the intended device/material role. Electrical/thermal/chemical performance requires separate tests.
7. Whether process variables (orientation, porosity, binder, cure/activation, layer thickness, defects) dominate lot-to-lot behavior.
8. Whether any mechanically acceptable material also meets service-life, recovery/recycling and cost-per-functional-unit requirements.

## Falsifiable reproduction protocol

### Gate 1 — source integrity and environment

- Resolve the upstream default branch to an immutable commit SHA.
- Record SHA-256 for the source archive/tree, license, every configuration and all required input data.
- Reconstruct the declared environment in an isolated container/VM; record OS, Python, FEniCS, dolfin-adjoint, NumPy, pandas, solver and BLAS versions.
- Do not patch dependency versions without recording a separate compatibility branch and numerical-difference report.

### Gate 2 — synthetic positive control

- Reproduce one published 2D Mooney–Rivlin setup using the paper's training configuration and random seed.
- Test the prescribed geometry/loading holdouts and compare vRMSE, reaction-force error, convergence and training time using the paper's definitions.
- Preserve all optimizer restarts, failed runs, rejected models and solver failures.
- Re-run with an independently implemented/versioned FE solver or a changed mesh to expose inverse-crime optimism.

### Gate 3 — negative and identifiability controls

- Include the paper's non-polyconvex Ishihara example. A bounded residual may reflect the polyconvex hypothesis-class restriction rather than optimizer failure.
- Hold out strain-state regions, not merely random mesh nodes.
- Test whether distinct constitutive functions produce indistinguishable boundary/reaction observations. If so, report non-identifiability rather than selecting one as uniquely recovered.
- Test measurement noise, mesh refinement, geometry shifts, loading-path shifts and boundary-condition changes.

### Gate 4 — material-class decision before Pangola transfer

Use independent coupon tests to determine whether the candidate material is:
- isotropic or anisotropic;
- path-independent or history-dependent;
- hyperelastic, viscoelastic, elastoplastic, damage-dominated or brittle/fracturing;
- rate- and temperature-sensitive;
- repeatable across orientation and manufacturing lots.

If the material is anisotropic or history-dependent, do not force the isotropic hyperelastic ansatz. Select an appropriate constitutive family and add its own physical constraints and falsifiers.

### Gate 5 — independent material and functional validation

- Use DIC or equivalent full-field/boundary measurement and calibrated force/reaction instrumentation.
- Keep an independent local strain–stress measurement set for validation; do not validate only against the same boundary observations used for fitting.
- Hold out specimens, lots, orientations, temperatures, rates, geometries and loading paths.
- Separately test the required functional property (mechanical, electrical, thermal, chemical, wear, corrosion or other) under the actual service environment.
- Calculate cost per accepted functional unit including feedstock, pretreatment, carbonization/activation, binder, energy, yield, rejects, processing, service life, recovery/recycling and logistics.

## Acceptance and stop rules

**Pass only if:** the source is pinned; the declared synthetic benchmark is reproduced within a preregistered tolerance; independent solver/mesh and held-out strain tests are reported; model-class limitations are explicit; real coupon data are independently validated; and the actual target function is measured.

**Stop or redesign if:** the material is not hyperelastic/isotropic/path-independent; distinct laws remain observationally indistinguishable; the model fails held-out strain states; solver/discretization mismatch destroys the result; process-lot variability dominates; or the target function/cost fails. Preserve the negative result and switch to anisotropic, viscoelastic, elastoplastic, damage or architecture-level approaches as justified.

## Nonclaims

No Pangola-derived material has been tested in this work item. No critical-material substitution, universal carbon replacement, device qualification, elemental transmutation, new physical law, commercial cost advantage or INV-029 Data-Center-to-Phone progress is established. The source paper's synthetic results remain external evidence until independently reproduced.
