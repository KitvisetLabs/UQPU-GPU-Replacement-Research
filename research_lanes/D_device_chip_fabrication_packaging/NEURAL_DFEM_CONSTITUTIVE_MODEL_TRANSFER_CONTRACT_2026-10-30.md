# Lane D contract — Neural-DFEM constitutive-model transfer

**Contract ID:** MAT-NEURAL-DFEM-001  
**Primary owner:** Lane D — device/chip/material constitutive modeling  
**Interfaces:** E (Pangola-derived materials and functional requirements), G (process windows and metrology), F (uncertainty and lifecycle economics), H (publication and strategic integration)  
**Date:** 2026-10-30  
**Evidence level:** LITERATURE_ONLY; no UQPU reproduction or material measurement  
**Related gap:** [RG-D-NEURAL-DFEM-MATERIAL-TRANSFER-001](../../docs/RESEARCH_GAP_NEURAL_DFEM_PANGOLA_MATERIAL_TRANSFER_2026-10-30.md)  
**Source watch:** [Neural-DFEM literature watch](../../docs/literature_watch/2026-10-30-neural-dfem-structure-preserving-constitutive-discovery.md)

## Purpose

Create a fail-closed route for testing whether a differentiable finite-element constitutive-discovery method can help qualify an engineered material for a device role. The method is eligible only after measured material behavior is shown to fit the model class. It is not a generic material-discovery oracle.

## Candidate mathematical class

For a path-independent hyperelastic solid, a strain-energy density W(F) is a function of the deformation gradient F with det(F) > 0. For the isotropic class used by the paper, the energy may be represented through invariants of C = FᵀF, commonly I1, I2 and J = det(F).

Required checks include:

- **Dimensions:** F, I1, I2 and J are dimensionless; W is energy per reference volume (J m⁻³ = Pa); first Piola–Kirchhoff stress has units Pa; displacement is m and measured reaction force is N.
- **Frame indifference:** W(QF) = W(F) for proper spatial rotations Q in SO(3).
- **Material symmetry:** isotropy requires W(FR) = W(F) for material rotations R in SO(3). A carbon composite with preferred fibre/particle orientation must not be silently treated as isotropic.
- **Reference state:** the selected reference configuration must be stress-free under the declared calibration protocol.
- **Polyconvexity/coercivity:** if these are imposed by the selected architecture, verify the actual implementation and domain assumptions; do not infer them from a paper citation alone.
- **Volumetric admissibility:** test behavior as J approaches zero and under large compression/expansion within the physically relevant domain.
- **Equilibrium:** the finite-element solve must satisfy the declared balance equations and boundary conditions to a preregistered residual tolerance.

These are model-class constraints and validation requirements, not a declaration that one constitutive ansatz describes every real composite.

## Required inputs and outputs

**Inputs:** immutable source/code/config hashes; mesh and solver identity; material specimen/lot/orientation; boundary geometry and conditions; loading history; temperature/rate; DIC displacement observations; calibrated reaction forces; independent validation measurements; uncertainty model.

**Outputs:** fitted strain-energy parameters/function; solver convergence and residuals; predicted boundary displacement/reaction curves; held-out errors; strain-invariant coverage; counterexamples; identifiability/uncertainty report; runtime and compute resources; model-class rejection reasons.

## Material-class gate

Before using this contract for Pangola-derived carbon or a hybrid composite, run coupon tests across tension, compression, shear, cyclic loading, strain rate, temperature and orientation. Determine whether hysteresis, creep, plasticity, fracture, damage, anisotropy or microstructural evolution is material. If any of these are central, use a suitable history-dependent or anisotropic constitutive model instead of forcing isotropic path-independent hyperelasticity.

Mechanical constitutive acceptance is separate from electrical conductivity, thermal conductivity, electrochemical behavior, corrosion, wear, reliability and process compatibility. Each target function needs its own test and baseline.

## D/G manufacturing co-design

Lane D owns the device/material acceptance envelope. Lane G must expose process variables and metrology for orientation, porosity, particle distribution, binder fraction, cure/activation, layer thickness, defects, interfaces, yield and lot traceability. The same material formulation must be linked to process settings and measured coupon results. No factory throughput, yield or cost claim is inferred from a constitutive-model paper.

## Falsifier and promotion ladder

Reject transfer if the material class is incompatible, held-out strain regimes fail, independent solver/mesh checks fail, the candidate law is not identifiable from the observations, or independent coupon measurements disagree beyond a preregistered uncertainty envelope.

Promotion sequence:
1. upstream source/code/data pinned;
2. synthetic benchmark independently reproduced;
3. solver/mesh and negative-control tests passed;
4. actual material class established from coupon measurements;
5. independent held-out material and functional tests passed;
6. device reliability and process-lot repeatability passed;
7. lifecycle cost per accepted function evaluated.

No step may be skipped. A learned equation remains a candidate constitutive model, not a universal physical law.
