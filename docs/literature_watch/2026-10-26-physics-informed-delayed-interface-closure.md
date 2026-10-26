# Literature watch — 2026-10-26: physics-informed symbolic regression for delayed interface forces

**Publication date:** 2026-09-08  
**Primary source:** Lazebnik, Mortenfeld & Liberzon, *Machine Learning: Science and Technology* 7 (2026), 055004. DOI: 10.1088/2632-2153/ae9c8b.  
**Official record:** https://doi.org/10.1088/2632-2153/ae9c8b  
**Institutional research record:** https://cris.haifa.ac.il/en/publications/physics-informed-symbolic-regression-reveals-a-delayed-oscillator/  
**Evidence class:** PEER-REVIEWED, EXPERIMENTAL-DATA-CONSTRAINED EFFECTIVE-MODEL DISCOVERY  
**Project evidence promoted:** none; the study has not been independently reproduced by UQPU.

## Result and genuine novelty

The authors apply physics-informed symbolic regression (PISR) to high-resolution trajectories of spheres crossing sharply stratified water–salt and water–glycerol interfaces. Rather than rely only on a classical buoyancy–drag description or an auxiliary virtual-mass ODE, their selected reduced-order force closure contains a delayed activation envelope, exponential decay and a phase-shifted oscillatory term. The candidate is intended to capture transient slowdown, interface retention and rebound-like recovery within the tested regime.

The paper reports operator-library ablations: removing the sine/cosine terms, exponential envelope or delayed-time component worsened validation RMSE in its experiment. Those results motivate ablation tests as a discovery diagnostic; they are paper-reported values, not measurements reproduced by this repository. The meaningful advance is a concrete example of physically constrained equation search producing an interpretable, testable effective closure from measured time series, with explicit model-form comparisons.

## Limitations and evidence boundary

- The result is an effective model for a particular particle/interface class, not a new fundamental law.
- The authors' own discussion calls for blind validation on new particle sizes, density contrasts, interface widths and fluid pairs.
- The trajectory classes and parameter ranges are limited; the no-minimum class is especially small and comes from one fluid pair.
- A good fit or an ablation win does not prove the proposed microscopic mechanism is unique. Other closures may be observationally equivalent on the available data.
- No UQPU run reproduced the dataset, model selection, coefficients or reported errors. No claim follows about QPU advantage, new physical laws, biomass conversion, fusion plasma behavior, material substitution, electricity cost or finance.

## Exact UQPU relevance

- **EQN-001/002:** candidate generation should be conditioned on units, known force balance, domain constraints and an explicit operator grammar.
- **EQN-003:** reserve blind trajectories and out-of-domain fluid/interface conditions before model selection.
- **EQN-004:** search counterexamples, limiting cases and alternative closures; record failed operator ablations and false discoveries.
- **EQN-006 / FND-006:** preserve the path from a symbolic expression to a causal interpretation, discriminating observable, independent validation and any downstream device/system consequence.
- **Lane E / FUS-001:** the method is a possible template for testing reduced-order transport or thermal closures, but plasma-facing and fusion-relevant regimes require their own data, governing assumptions and validation. No transfer of coefficients or conclusions is justified.
- **BIO-001 / INV-030:** the same method could be considered for measured biomass-slurry or conversion dynamics only after suitable data and an accepted process output are defined. This article supplies no Pangola, carbon-material or accepted-liquid-energy evidence.
- **INV-033:** no capital, interest, WACC or cost result is implied.

## Proposed falsifiable follow-up

Add PISR as an explicitly identified method in the existing matched equation-discovery comparison protocol, without copying the paper's reported score as a UQPU result. Freeze source/data hashes, units, preprocessing, operator grammar, split membership, acceptance rules and identical resource budgets. Use at least 30 preregistered seeds where compute permits; hold out complete fluid pairs and scales rather than random points from the same trajectories; include operator-library ablations, residual autocorrelation, dimensional and limiting-case checks, alternative candidate closures, counterexample search, failed searches and full training-plus-inference cost. Require an independent implementation or blind experimental replication before claiming transferability. The method-level hypothesis is falsified if gains vanish on held-out fluid/scale families, depend on leakage or unequal budgets, or improve fit without improving accepted predictions and physical constraints.

## Status

Literature-only addition for INV-034/035 and the EQN-001–006 workflow. No candidate is promoted to a physical law or engineering advantage.
