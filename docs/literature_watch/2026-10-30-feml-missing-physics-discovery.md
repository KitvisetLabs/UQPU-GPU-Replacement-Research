# Literature watch — 2026-10-30: differentiable FEM for missing constitutive and thermal physics

**Checked:** 2026-10-30  
**Primary owner:** Lane D — device/material constitutive-model transfer  
**Cross-lane interfaces:** E (Pangola/advanced materials), F (measurement/economics), G (process/manufacturability), H (publication); INV-034/035  
**Evidence class:** PEER-REVIEWED METHOD + AUTHOR-REPORTED REAL BENCHMARK DATA; NOT REPRODUCED BY UQPU

## Primary source

Ado Farsi, Nacime Bouziani and David A. Ham, “Missing physics discovery through fully differentiable finite element-based machine learning,” Scientific Reports (published 2026-08-25), DOI https://doi.org/10.1038/s41598-026-65125-z. The current arXiv v3 was revised 2026-07-16: https://arxiv.org/abs/2507.15787v3. Full HTML: https://arxiv.org/html/2507.15787v3. Reproduction archive: https://doi.org/10.5281/zenodo.21251671.

## Genuine methodological contribution

FEML embeds a learnable missing-physics operator inside a differentiable finite-element PDE solve. The measured loss is computed from observable quantities such as displacement, boundary force or temperature; adjoint differentiation propagates that loss through the PDE solver into the operator parameters. The paper uses structure-preserving operator networks over finite-element spaces, rather than learning only a configuration-specific solution surrogate.

The paper separates known PDE structure from the unknown operator and demonstrates a progressive discovery workflow:

1. Synthetic displacement-controlled tests recover a nonlinear elastic response from six noisy force–displacement pairs.
2. Synthetic load-controlled tests recover a monotone plastic-hardening operator from full-field displacement data.
3. Frozen operators are composed and transferred without retraining to a synthetic 3-D torsion problem with different geometry/loading, kept within the trained strain envelope.
4. On real benchmark data from the Second Sandia Fracture Challenge, four Ti–6Al–4V shear-coupon specimens are used to learn a plastic-hardening law and a ductile-damage operator. The paper reports 0.54 kN RMSE (about 1.9% of peak force) and agreement within specimen-to-specimen scatter.
5. A separate thermal-conductivity example is synthetic; symbolic regression extracts a positive power-law candidate over the fitting range, with a reported extrapolation error beyond that range.

The novelty relevant to UQPU is the operator-level inverse problem: infer a hidden constitutive/transport relation from indirect, measurable system outputs while retaining known PDE and variational structure.

## Evidence limits and negative findings

- The four real specimens belong to one titanium-alloy benchmark. They are not Pangola-derived material, semiconductor, photonic or fusion-component data.
- The real shear-coupon experiment samples essentially one stress-state path. The authors state that a general triaxiality-dependent damage law is not identifiable from that experiment; their damage operator is a reduced scalar function of accumulated plastic strain.
- The synthetic elastic, hardening, torsion and thermal examples use generated data with known ground truth. Synthetic zero-shot transfer is not independent real-material transfer.
- Thermal-conductivity and symbolic-regression results are synthetic in this paper; the real-data result is the Ti–6Al–4V shear coupon.
- Training requires a forward FEM solve and an adjoint solve for each load/time step. The paper reports minutes to hours on a 10-core Apple M4 laptop for its examples; this is not a field-scale cost result. The reported forward-inference overhead of the learned operator is below 1.3% in tested cases, but training cost is dominated by adjoints.
- The paper identifies operator non-identifiability as a risk and relies on embedded PDE constraints, restricted operator parameterisations and sufficiently diverse loading to reduce it.
- The real benchmark result is author-reported. UQPU has not downloaded the Zenodo archive, pinned its bytes/environment, independently reproduced the solver or checked the reported statistics.
- A neural operator or symbolic fit is not, by itself, a newly established physical law.

## Exact UQPU relevance

- **INV-030 / Lane D-E:** FEML is a candidate characterization method only if a specific Pangola-derived carbon material has a defined mechanical or thermal target function. It may help test functional substitution, minimization, hybridization or redesign; it cannot imply elemental transmutation or material equivalence.
- **INV-035 / FND-006 / EQN-001–006:** the method supplies a candidate generator/evaluator architecture for hidden constitutive operators. Every candidate still needs dimensional, symmetry/objectivity, conservation, thermodynamic-dissipation, positivity, limiting-case, held-out and counterexample checks, followed by independent experiments.
- **Lane G:** process variables, porosity, orientation, binder, heat treatment, batch yield and process-window variability must be tracked with D; a constitutive fit cannot replace manufacturing qualification.
- **Lane F:** the cost account must include solver/adjoint calls, mesh degrees of freedom, memory, wall time, energy and compute cost, not just fit error.
- **INV-029:** no computing, device, energy or physical-compression milestone follows from this material-modeling method.

## Falsifiable follow-up

1. Retrieve Zenodo record 10.5281/zenodo.21251671 and pin its version, archive hash, source tree, data files, Firedrake/PyTorch/JAX versions and hardware environment.
2. Reproduce the four-specimen Ti–6Al–4V shear-coupon result from published data, including the 0.54 kN metric, specimen-scatter normalization, boundary conditions, mesh refinement and independent solver check.
3. Freeze the target function before collecting Pangola-derived carbon-composite data. If the target is mechanical or thermal, create multiple material batches, independently measured composition/porosity/orientation/density/ash/binder/moisture and calibrated coupon tests. Electrical-conductivity claims require a separately specified electrical PDE and direct measurements; this paper does not establish them.
4. Split by material batch, specimen and geometry, not randomly by adjacent time/load points. Keep a blind batch and a new geometry/loading condition for transfer.
5. Compare conventional constitutive models, direct supervised fits and FEML under equal data, compute and parameter-selection budgets. Test objectivity, tensor symmetry, positivity, dissipation/energy balance, mesh objectivity, limiting cases and counterexamples.
6. Extract symbolic expressions only after operator validation; report fitting and extrapolation ranges separately and test every expression on sealed conditions.
7. Record forward/adjoint solves, mesh DOFs, peak memory, wall time, retries, energy where measurable and cost per accepted material-property prediction.

**Disposition:** new-to-main literature lead; source archive and independent reproduction remain open. No Pangola material qualification, substitution, device result or new physical law is claimed.
