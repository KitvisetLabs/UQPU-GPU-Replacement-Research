# Research Gap RG-BELL-QSL-001 — Bell quantum signal learning under matched resources

**Created:** 2026-10-26  
**Primary owner:** Lane A  
**Integration owners:** Lanes B/C/D/F/G; publication owner Lane H  
**Status:** OPEN — THEORY SOURCE IDENTIFIED; PROJECT REPRODUCTION NOT STARTED  
**Evidence class:** external peer-reviewed theory; no UQPU execution evidence

## Question

Can the Bell quantum signal learning protocol in Cotler, Danielson and Kannan, Physical Review X 16, 041025 (2026), DOI 10.1103/6ps1-mw9l, be independently reproduced for a bounded task and retain an advantage over the strongest eligible entanglement-free baseline when useful-output quality and total resources are matched?

## Current evidence

The source reports a protocol based on two-mode squeezing, passive optics and static homodyne measurements; the same dataset can support post-hoc estimation of multiple classical-signal properties. It proves query-complexity separations in specified formal models and reports practical comparisons to homodyne/heterodyne strategies. UQPU has only recorded and scoped the source. No code reproduction, simulation, hardware execution or cost result has been produced.

The source preprint (https://arxiv.org/abs/2602.17591), Appendix E.4, also makes an important resource distinction: one separate squeezing-only example chooses (r = \frac{1}{2}\log n), for which a single-mode squeezed vacuum has mean photon number \(\bar n = \sinh^2(r) = \Theta(n)\). That example's exponential sample-complexity separation is therefore not a fixed-probe-energy claim. It must not be conflated with the paper's distinct entanglement-enabled Bell-QSL results. Mean probe photon number also does not measure wall-plug power required for squeezing generation and stabilization.

## Blocking uncertainties

1. Exact source/supplement assumptions, signal oracle, task distribution, comparator class and resource units must be extracted and frozen.
2. The property-vector output contract and acceptance tolerance are not yet implemented.
3. Squeezing/entanglement resource conventions may change the comparison; report resource-explicit and end-to-end accounting separately.
4. Any instance-dependent squeezing-energy scaling must be charged explicitly or kept in a separately labeled resource convention.
5. Real source, detector, loss, bandwidth, calibration and acquisition constraints are not represented by a theorem alone.
6. Provider modality may not match bosonic sensing; no cross-provider target/price substitution is allowed.
7. Classical reconstruction and multi-property output may dominate nominal query advantage.
8. The canonical RESEARCH_GAPS.md is append-only and was not rewritten from partial content; this artifact is the detailed owner record until safe ledger synchronization.

## Unlock criteria

- [ ] Source theorem and supplemental assumptions reviewed and transcribed.
- [ ] Separate entanglement-enabled and squeezing-only theorem/resource conventions explicitly identified.
- [ ] Independent minimal implementation passes an analytic/small-instance check.
- [ ] Covariance/noise calculations agree with an independent implementation within a preregistered tolerance.
- [ ] Output vector, loss, confidence and held-out split frozen before comparison.
- [ ] Homodyne, heterodyne and strongest eligible entanglement-free baseline use identical useful-output requirements.
- [ ] Total probe energy, squeezing, displacement, source/pump wall-plug energy, controls, detection, classical compute, reconstruction, memory/I/O, energy and cost are accounted for without double counting.
- [ ] Any exponential claim is tested under a declared energy/resource scaling; uncharged instance-scaled squeezing cannot support a fair fixed-energy claim.
- [ ] Noise, loss, bandwidth and calibration sweeps include negative controls and failed cases.
- [ ] Independent reproduction and target eligibility reviewed before any hardware request.
- [ ] Paid execution, if ever proposed, has explicit user consent, credentials and bounded budget.

## Promotion rule

A pass at the theoretical/simulator gate may promote the item only to SIMULATION_INDEPENDENT_REPRODUCTION. It cannot promote it to measured quantum advantage, lower cost/energy, a new physical law, or a general-purpose GPU/CPU/NPU replacement. Hardware claims require same-target measurements; economic claims require total cost per accepted output at matched quality.
