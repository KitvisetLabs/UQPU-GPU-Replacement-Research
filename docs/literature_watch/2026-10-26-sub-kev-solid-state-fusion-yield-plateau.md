# Literature watch — 2026-10-26: sub-keV fusion-yield plateau in metal hydrides

**Observed / recorded:** 2026-10-26  
**Primary source:** Micah E. Karahadian, Matthew Colborne, Arun Persaud, Thomas Schenkel and Jeremy N. Munday et al., “Enhanced nuclear fusion in the sub-keV energy regime,” *Nature Communications* 17, Article 8845 (published 2026-07-18; version of record 2026-08-24).  
**Official article:** https://www.nature.com/articles/s41467-026-74421-1  
**DOI:** 10.1038/s41467-026-74421-1  
**Primary owner:** Lane E — materials, energy, cooling and infrastructure  
**Integration owner:** Lane F — evidence, benchmarks and lifecycle economics  
**Co-design:** Lanes D/G — device/material metrology, process windows and manufacturability  
**Publication / foundational owner:** Lane H — strategy and research publication  
**Feeds:** FUS-001, FND-005, FND-006, EQN-001–006, INV-032, INV-034, INV-035  
**Evidence class:** PEER-REVIEWED PRIMARY EXPERIMENT; LITERATURE_ONLY FOR UQPU  
**Project evidence promoted:** none

## Why this source is being added

The repository's current main branch had no indexed reference to this paper at the time of the targeted search. The article reports a surprising, experimentally controlled low-energy D–D fusion-yield regime that is relevant to foundational reaction-physics surveillance and the materials side of FUS-001. This is a newly incorporated literature lead, not a claim that the result was published today, independently reproduced by UQPU, or useful for commercial power generation.

## Reported result and genuine novelty

The authors bombard palladium and titanium foils with low-energy deuterium ions while comparing beam-only targets with electrochemically deuterium-loaded targets. Their center-of-mass energy sweep spans approximately 0.25–6.5 keV. They report a relative-yield plateau below roughly 2 keV where a constant, homogeneous screening-potential model no longer describes the measured trend. Proton products provide the low-energy yield measurement; neutron-channel measurements supply a cross-check in the higher-energy region where the neutron signal is usable.

The paper's largest quoted enhancement—approaching or exceeding 10^18 at the lowest energy—is defined relative to an **unscreened bare-nucleus yield model**. It is not a 10^18 increase in useful electrical output, not a net-energy-gain measurement, and not a commercial fusion result. The experiment uses an externally powered ion beam and reports relative reaction yields, not a complete plant energy balance.

The methodological novelty is the observed low-energy plateau across two different metal hosts, alongside the authors' evidence that one energy-independent effective screening potential does not fit the full curve. The authors discuss depth-dependent, heterogeneous reaction environments involving near-surface defects, trapped deuterium and non-equilibrium occupancy as possible contributors. The microscopic mechanism is not uniquely established.

## Limits and interpretation boundary

- This is a peer-reviewed experiment, but it is not an independent replication by UQPU and is not yet an independently replicated general mechanism.
- The relative yield is normalized to a higher-energy reference point. The very large enhancement ratio depends on the unscreened comparison model; it must not be read as a large absolute fusion power.
- A fitted “effective screening potential” is a compact model parameter. In a heterogeneous target it need not equal a single, uniform microscopic potential.
- Proton and neutron channels have different usable signal-to-background regimes; their overlap is a valuable cross-check, not a license to treat every low-energy bin as independently confirmed by both channels.
- A yield plateau does not show that the Coulomb barrier is absent, that conservation laws fail, or that net energy is produced.
- The paper does not establish fusion-electricity CAPEX/OPEX, capacity factor, recirculating-power margin, component lifetime, tritium/fuel-cycle closure, maintenance, grid delivery or lifecycle cost.
- No biomass-carbon substitution, Pangola conversion, accepted bio-oil, critical-material reduction, financing benefit, quantum advantage or Data-Center-to-Phone capability follows from this result.

## Candidate model and physics checks — hypothesis, not a new law

**Incumbent assumption being tested:** the standard screened thick-target yield calculation with a spatially homogeneous reaction environment and a constant effective screening potential over the energy interval is adequate to describe the yield curve.

**Candidate alternative:** a depth-weighted mixture of near-surface and bulk reaction environments, where deuterium density, defect population and effective screening vary with implantation depth. One testable schematic form is

\[
Y(E)=\int_0^{d(E)} n_D(z)\,P_{DD}\!\left(E_{\mathrm{local}}(E,z),\eta(z)\right)\,dz,
\]

where \(d(E)\) is the energy-dependent implantation depth, \(n_D(z)\) is the deuterium profile and \(\eta(z)\) represents independently measured local environment variables. This is a model class for testing heterogeneous-target explanations, not a fitted or validated UQPU equation and not a declaration of new physics.

Required checks before any promotion:

1. **Dimensions:** the arguments of the reaction-probability model must be dimensionally valid; energy terms must use consistent frames and units; the final yield must retain its defined yield-per-charge units.
2. **Symmetry and conservation:** retain the known D–D reaction channels and charge, baryon-number and energy accounting. A material-dependent yield model does not by itself modify the underlying nuclear reaction law.
3. **Causality:** loading, beam exposure and defect evolution must precede the yield changes attributed to them; avoid fitting a causal story to a correlated post-run characterization alone.
4. **Scaling and limiting cases:** the heterogeneous model should approach the homogeneous model when the two environments become identical or one component's weight vanishes. At higher energies, where the sampled depth and reaction environment become more bulk-like, its prediction should recover the measured high-energy regime without arbitrary pointwise tuning.
5. **No-go boundary:** a present model mismatch is not permission to ignore conservation, tunneling physics or established constraints. The alternative must state exactly which uniform-environment assumption changes and what different observable follows.

## Falsifiable follow-up — FUS-SOLID-001 / FND-005

1. Freeze the paper's source, data and supplementary-material hashes, calibration assumptions, target composition, energy grid and analysis protocol before attempting reproduction.
2. Preregister a blinded independent replication using Pd/PdD and Ti/TiD conditions, matched beam-current and energy calibration, detector-efficiency checks, interleaved background controls, and beam-only / loading-only / beam-plus-loading controls. Include isotopic or target controls where practical.
3. Measure absolute proton and neutron yields per delivered charge where detector sensitivity permits; report relative yields separately. Preserve all failed runs, excluded bins and background decisions.
4. Measure deuterium depth profiles and defect populations using suitable independent methods (for example, nuclear-reaction analysis or elastic-recoil detection for hydrogen/deuterium, and positron-annihilation methods for open-volume defects). Test whether the candidate mechanism predicts the observed energy dependence from those measurements rather than estimating every parameter from the yield curve.
5. Fit the constant-screening incumbent and a preregistered heterogeneous-depth model with the same data budget. Hold out low-energy bins and at least one material/condition for prediction. Report uncertainty, residuals, sensitivity to energy spread and background subtraction, and a complexity penalty; do not select a model solely because it has more adjustable parameters.
6. **Discriminating observables:** the shape and absolute scale of yield versus energy; plateau reproducibility; dependence on independently measured deuterium occupancy and defect density; and whether the same frozen model predicts held-out conditions.
7. **Falsifiers:** the plateau disappears under blinded replication; a corrected detector/beam/background model explains it; the candidate fails held-out prediction; or yield does not track the independently measured state variables required by the proposed mechanism.
8. Require independent replication and a physics review before changing the FUS-001 model. Any later energy-economics analysis must start from measured absolute reaction rates and a complete input-energy ledger. Relative enhancement alone cannot establish net energy.

## Exact cross-lane and mission relevance

- **A — Quantum programming/workloads/runtime:** no computing or quantum-advantage result; keep software-first workload contracts as the priority execution path.
- **B — Cloud/QPU/provider integration:** no provider or QPU execution; paid jobs remain disabled without credentials, a bounded budget and explicit consent.
- **C — Memory/state/data movement:** no memory or storage result.
- **D — Device/chip/process/material metrology:** potential source of measurement requirements for surface condition, defect state and target damage; no device benefit is established.
- **E — Materials/energy/cooling/infrastructure:** a candidate variable set for reaction-physics research only; no useful power or fuel product is demonstrated.
- **F — Economics/evidence/integration:** FUS-001 remains open. No net MWh, lifecycle cost, financing term or uncertainty-bounded commercial model is available from this paper alone.
- **G — Manufacturing equipment/factory systems:** no process yield, reproducible manufacturing window, target lifetime or scale-up evidence.
- **H — Strategy/publication:** preserve the dated source and falsifiable follow-up; the multilingual Kanusanan Pongpanna Model remains strategic context, not experimental evidence.

### INV-029–INV-035 status impact

- **INV-029:** no phone-class physical compression or equivalent useful-service closure.
- **INV-030:** no Pangola-derived carbon substitution or critical-material reduction; no elemental transmutation is implied.
- **INV-031:** no accepted biomass liquid fuel, yield or cost result.
- **INV-032:** no reliable net delivered fusion electricity or lifecycle-cost result; this is not a power-plant milestone.
- **INV-033:** no financed-principal, absolute-interest, risk-premium or WACC change.
- **INV-034:** adds a source-bounded, testable reaction-physics lead while preserving known constraints.
- **INV-035:** the candidate heterogeneous model remains a hypothesis subject to dimensional, symmetry/conservation/causality, limiting-case, held-out, falsification and independent-validation gates. No new physical law is claimed.

**Current decision:** retain as LITERATURE_ONLY. Do not promote the enhancement factor to a device, energy, material, fusion-electricity or economic advantage. No external experiment or QPU job was performed in this cycle.
