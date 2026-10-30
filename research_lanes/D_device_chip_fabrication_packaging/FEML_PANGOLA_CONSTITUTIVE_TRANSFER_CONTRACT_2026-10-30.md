# Lane D contract — FEML constitutive transfer to Pangola-derived materials

**Date:** 2026-10-30  
**Primary owner:** Lane D  
**Interfaces:** E (material function/feedstock), F (evidence and economics), G (process-window/manufacturing), H (publication)  
**Evidence class:** LITERATURE_ONLY / PREREGISTERED_TRANSFER_CONTRACT

## Scope

Use Farsi, Bouziani and Ham's FEML method only as a candidate inverse-modeling workflow for a specified mechanical or thermal material function. Do not assume Pangola-derived carbon has a required property, and do not infer electrical properties from a mechanical/thermal model.

## Required source pins

- Paper: https://doi.org/10.1038/s41598-026-65125-z
- arXiv v3: https://arxiv.org/abs/2507.15787v3
- Reproduction archive: https://doi.org/10.5281/zenodo.21251671

Record exact archive/source/data hashes, license, Firedrake/pyadjoint/PyTorch/JAX versions, solver configuration, compiler/runtime and hardware before reproduction.

## Experimental contract

1. Define the accepted function and incumbent material before model selection.
2. Record Pangola feedstock and carbonization/activation/compounding route, batch, composition, ash/impurity, moisture, binder, density, porosity, orientation, thermal history and specimen geometry.
3. Calibrate instruments and obtain replicated measurements across independent batches. Mechanical tests require force/displacement fields and specimen variability; thermal tests require geometry, heat flux, boundary conditions and transient temperature measurements.
4. Freeze batch/specimen/geometry-level train, validation and blind-test partitions. Never split adjacent load/time points across train and test.
5. Compare conventional constitutive/thermal models and direct data-driven fits against FEML under equal data, optimizer, compute and model-selection budgets.
6. Enforce relevant mathematical structure: dimensions, objectivity/frame indifference, stress symmetry, positive moduli/conductivity, thermodynamic dissipation, energy balance, boundary conditions, stability and mesh objectivity. Use anisotropic structure if the material is anisotropic; do not impose isotropy without evidence.
7. Test a blind batch and a new geometry/loading/thermal regime. Search counterexamples and report failure cases.
8. Extract symbolic equations only after the operator passes validation; test the expression outside its fitting range and against physical constraints.

## Resource and cost ledger

Record mesh DOFs, forward and adjoint solves, load/time steps, optimizer epochs, CPU/GPU model, peak memory, wall time, retries, solver failures, energy where measurable and compute cost. The paper reports that adjoint solves dominate training; do not infer field-scale cost from its laptop examples.

## Acceptance

The paper's Ti–6Al–4V benchmark must first be reproduced from the pinned archive. Pangola transfer then requires measured coupon evidence and independent validation. INV-030 functional substitution requires comparison against incumbent material's accepted function, durability, process stability, recycling/recovery and lifecycle cost.

**No transmutation, substitution, device qualification or new physical law is implied by this contract.**
