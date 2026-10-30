# Research gap — FEML transfer from published benchmark to Pangola-derived materials

**Opened:** 2026-10-30  
**Work item:** MAT-FEML-PANGOLA-001  
**Gap ID:** RG-FEML-PANGOLA-TRANSFER-001  
**Primary owner:** Lane D — device/material constitutive transfer  
**Cross-lane owners:** E (Pangola feedstock/material function), F (measurement/economics), G (process windows/manufacturing), H (publication)  
**Status:** LITERATURE_ONLY / DATA_BLOCKED / REPRODUCTION_NOT_RUN  
**Related:** INV-030, INV-034, INV-035, FND-006, EQN-001–006

## Objective

Determine whether fully differentiable finite-element machine learning (FEML) can identify a useful mechanical or thermal constitutive operator for a specified Pangola-derived carbon material from indirect, experimentally accessible measurements. This is a transfer hypothesis, not a claim that Pangola carbon has any required material property.

## Source basis

Farsi, Bouziani and Ham, Scientific Reports (2026-08-25), DOI 10.1038/s41598-026-65125-z; arXiv:2507.15787v3 (2026-07-16); Zenodo reproduction archive DOI 10.5281/zenodo.21251671. See [literature watch](literature_watch/2026-10-30-feml-missing-physics-discovery.md) and [Lane D contract](../research_lanes/D_device_chip_fabrication_packaging/FEML_PANGOLA_CONSTITUTIVE_TRANSFER_CONTRACT_2026-10-30.md).

## What is actually supported

The paper reports a real-data demonstration on four Ti–6Al–4V shear-coupon specimens from the Second Sandia Fracture Challenge, learning plastic hardening and a reduced scalar ductile-damage operator with a 0.54 kN RMSE (about 1.9% of peak force), within specimen-to-specimen scatter. Its synthetic studies include nonlinear elasticity, plastic hardening, zero-shot transfer to a 3-D torsion setup and thermal conductivity. UQPU has not independently reproduced these results.

## Blocking gaps

1. No Pangola-derived carbon specimen, composition, manufacturing route, material-property measurement or target function is present in this work.
2. A mechanical or thermal operator is useful only after a functional requirement is chosen. Electrical conductivity requires a separate PDE/measurement model and cannot be inferred from this paper.
3. The published real-data damage model is deliberately reduced because one shear-coupon path does not identify general triaxiality dependence.
4. The synthetic zero-shot transfer is not real-material transfer. Thermal-conductivity and symbolic-regression examples are synthetic.
5. FEML training requires forward and adjoint PDE solves; mesh, solver, memory, energy and cost scaling must be measured.
6. A fitted operator may be non-identifiable or non-generalizing. Objectivity, tensor symmetry, positivity, thermodynamic dissipation, energy balance, mesh objectivity, limiting cases and counterexamples must be checked.
7. No independent source archive, environment or solver reproduction has been completed by UQPU.

## Shared material-data interface with the parallel hyperreduction work

PR #154 separately carries MAT-NEURAL-HYPERREDUCTION-001 (Holthusen et al., adaptive POD/ECSW and adjoint hyperreduction). Its contract is available on the source commit at https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/blob/3b11949c517631df77ac893bbaa189a35e108971/research_lanes/D_device_chip_fabrication_packaging/NEURAL_MATERIAL_HYPERREDUCTION_TRANSFER_CONTRACT_2026-10-30.md. Do not create two independent Pangola coupon campaigns. Reuse one versioned material/function specification, batch/specimen IDs, calibration records, geometry/load/thermal splits and blind holdouts; compare conventional models, FEML and hyperreduction as separate solver methods under matched data and compute budgets. Keep method-specific cost terms separate: FEML forward/adjoint solves versus hyperreduction basis/sampling rebuilds, canaries and full-order checks. Both remain literature-only until source reproduction and actual Pangola data pass.

## Acceptance gates

- **Gate 0 — material/function specification:** define the intended substitute or hybrid function and incumbent reference material. Record composition, batch, process, porosity, orientation, density, ash/impurity, binder, moisture and thermal history.
- **Gate 1 — source reproduction:** pin Zenodo/PDF/source/data hashes and environment; reproduce the four-specimen Ti–6Al–4V benchmark and its reported metric using an independent reviewer/solver check.
- **Gate 2 — Pangola coupons:** use multiple independently produced batches, replicate specimens and calibrated instruments. Choose mechanical or thermal tests before model fitting.
- **Gate 3 — identifiability/generalization:** split by batch/specimen/geometry; hold out a blind batch and new geometry/loading condition; compare conventional constitutive models, direct regression and FEML under equal data/compute budgets.
- **Gate 4 — physics/equation acceptance:** check dimensions, objectivity, tensor symmetry, positivity, dissipation/energy balance, mesh convergence, limiting cases, held-out predictions and adversarial counterexamples. Symbolic regression is post-processing only.
- **Gate 5 — functional substitution:** compare measured accepted function, durability, environmental/process stability, repair/recycling and full lifecycle cost against incumbent material. Only this gate can support INV-030 substitution language.

## Nonclaims

No Pangola material qualification, critical-material reduction, device result, fuel result, fusion result, elemental transmutation, commercial cost reduction or new physical law is established. All transfer calculations remain MODEL_ONLY until Gates 0–4; functional substitution remains unproven until Gate 5.
