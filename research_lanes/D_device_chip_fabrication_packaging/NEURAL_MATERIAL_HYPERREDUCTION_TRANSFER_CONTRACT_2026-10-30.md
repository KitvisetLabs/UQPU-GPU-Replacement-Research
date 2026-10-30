# Lane D contract — neural-material hyperreduction transfer gate

**Stable ID:** MAT-NEURAL-HYPERREDUCTION-001  
**Primary owner:** Lane D — device/material constitutive models  
**Interfaces:** A (equation-discovery runtime), C (snapshot/storage/I/O), E (Pangola materials and process streams), F (evidence and lifecycle cost), G (metrology/process equipment), H (strategic publication)  
**Opened:** 2026-10-30  
**Status:** OPEN / LITERATURE_ONLY / REPRODUCTION_NOT_RUN  
**Source:** Holthusen, Knipper & Linka, arXiv:2610.31322v1 (2026-10-22), https://arxiv.org/abs/2610.31322  
**Related:** MAT-NEURAL-DFEM-001; INV-030; INV-034/035; EQN-001/003/004/006.

## Objective

Determine whether adaptive POD + energy-conserving sampling/weighting (ECSW) + adjoint sensitivities can reduce the complete cost of inverse constitutive-model identification while preserving full-order prediction quality on independently held-out deformation states, specimens and meshes.

This is a computational-method question. It does not itself qualify a material or demonstrate Pangola substitution.

## Source-reported method and scope

The arXiv preprint combines:
- POD projection of equilibrium onto an evolving reduced displacement subspace;
- ECSW weighted evaluation of internal energy on a selected element subset;
- adjoint sensitivities of the reduced inverse problem;
- adaptive snapshots and sampled elements as neural constitutive weights change;
- a polyconvex neural strain-energy class built with zero-anchored input-convex structure, logarithmic normalization and a growth term.

The paper reports two experimental-data cases and one synthetic 3-D case. It reports a reduction from about 9 h to 41 min for one two-phase specimen, but its full-order bootstrap/canary checks consume substantial runtime. Reported timings were measured on a 10-core Apple M4 CPU with 24 GB memory in double precision. The implementation is described as in-house ASIMOV/JAX; no public implementation pin was identified.

## Reproduction protocol

### Gate 0 — provenance and environment
1. Pin arXiv version, paper hash, cited dataset versions, licenses and any later source/data release.
2. Reconstruct the JAX/Python/solver environment from the paper; record OS, CPU, memory, numerical precision and dependency lock.
3. Preserve the original full-order reference, all hyperreduction settings, random seeds and raw run logs.
4. Do not substitute the authors' in-house implementation with a new implementation and label it a reproduction without an explicit method-equivalence audit.

### Gate 1 — exact source-case reproduction
1. Reproduce the first experimental case from its published Mechanical MNIST source data.
2. Compare full-order and hyperreduced predictions on the same mesh, boundary conditions, load steps, constitutive architecture and loss.
3. Report reaction-force error and independent displacement-field error, not only the optimized training loss.
4. Include bootstrap, reduced epochs, canary epochs, basis rebuilds, ECSW rebuilds and final full-order evaluation in wall-clock/resource totals.

### Gate 2 — counterexamples and identifiability
- Add a deformation-localization negative control and vary the canary interval/snapshot freshness.
- Add an independent mesh and, where possible, independent solver check.
- Test force-only versus force-plus-DIC losses to expose non-identifiability.
- Hold out load paths and deformation modes (e.g. shear/equibiaxial versus uniaxial) not used for fitting.
- Preserve failed convergence, unstable tangent, poor displacement prediction and non-identifiable material fits.

### Gate 3 — material-class boundary
The published method demonstrates isotropic hyperelasticity. It discusses anisotropic extension but does not demonstrate it; inelasticity requires history-dependent adjoints. Before any Pangola transfer, measure and classify the actual material:
- constituent composition, orientation and anisotropy;
- porosity, density and moisture;
- binder/cure/activation and processing history;
- strain-rate and temperature dependence;
- viscoelasticity, plasticity, damage, fracture and cyclic degradation;
- specimen-to-specimen and lot variability.

If the measured behavior is not isotropic path-independent hyperelasticity, the current source model is out of class. Do not force-fit it.

### Gate 4 — accepted function and lifecycle economics
Only after Gates 0–3 pass, define the actual component-level function and matched reference material. Measure the required mechanical/electrical/thermal function, reliability, environmental stability, replacement interval and manufacturing yield. Include sample preparation, characterization, compute hardware, full-order checks, energy, storage/I/O, failed specimens, CAPEX/OPEX, recovery/recycling and lifecycle cost per accepted function.

## Required metrics

- full-order and reduced wall time separately and in total;
- number of full-order solves, canary solves, basis rebuilds and ECSW updates;
- force and displacement errors on fit, validation and held-out load paths;
- deformation-state coverage and localization diagnostics;
- FE degrees of freedom, retained modes, sampled elements and ECSW weights;
- solver iterations, adjoint solves, gradient checks and convergence failures;
- peak RAM, checkpoint/snapshot bytes, storage and data transfer;
- CPU/GPU model, precision, utilization, energy where measurable;
- total cost per accepted material model and uncertainty across seeds/specimens.

Unknown resource/cost fields remain unknown, never zero.

## Acceptance and falsifiers

A reproduction passes only if:
1. the pinned source case matches within predeclared numerical tolerances;
2. full-order canary checks bound reduced-model error over the entire training trajectory;
3. held-out mesh/load-path tests do not reveal unacceptable error or non-identifiability;
4. total cost includes all canary/rebuild/full-order work;
5. independent replication confirms the result.

Reject transfer if the material class is incompatible, deformation-state coverage is insufficient, the reduced basis fails under localization, full-order checks erase the speed gain, or measured function/cost does not beat the matched reference.

## Current result

No source installation, code reproduction, FE simulation, Pangola coupon, material substitution, device fabrication or economic measurement was performed in this cycle. The source remains external preprint evidence only. See `docs/literature_watch/2026-10-30-agentic-equation-discovery-and-constitutive-models.md`.

## Next action

Pin source/data/configuration and reproduce the first experimental-data case against the full-order solver. Do not begin Pangola transfer or a material-substitution claim before independent material-class and coupon evidence exists.
