# Literature watch — 2026-10-27: thermodynamic control with quantum side information

**Source publication status:** accepted by *Physical Review Letters* on 2026-10-06; APS accepted-paper record accessed 2026-10-27  
**Primary source:** Kaiyuan Ji, Gilad Gour, and Mark M. Wilde, “Fundamental limits for thermodynamic control with quantum feedback,” DOI [10.1103/x67n-33gr](https://doi.org/10.1103/x67n-33gr); [official APS accepted-paper record](https://journals.aps.org/prl/accepted/10.1103/x67n-33gr); [arXiv:2503.09012v4](https://arxiv.org/abs/2503.09012v4), version 4 posted 2026-10-09.  
**Evidence class:** PEER_REVIEWED_THEORY / OPERATIONAL THERMODYNAMIC BOUNDS; no UQPU reproduction and no new physical-law claim  
**Primary owner:** Lane H — literature surveillance/publication  
**Implementation owner:** Lane A — thermodynamic workload/accounting contract  
**Evidence/economics owner:** Lane F  
**Feeds:** FND-001, FND-003, EQN-001–006 where relevant, INV-034/035; cross-lane review A–H  
**Promotion:** literature and theorem-reproduction gate only

## Material delta

The APS record reports acceptance on 2026-10-06. The paper formalizes thermodynamic state conversion when a controller holds quantum side information that may be fed back coherently. From stated operational principles, the authors derive tight single-shot bounds on work of formation and extractable work for arbitrary quantum systems conditioned on arbitrary quantum side information. In the asymptotic regime they derive a generalized second law expressed through conditional free energy. They explicitly reconcile this with the traditional second law when acquisition, processing and reset of side information are accounted for.

The genuine UQPU-relevant point is an accounting and modeling constraint: a feedback-assisted work bound cannot be interpreted as free work supplied by information. The information/controller boundary and the operational meaning of work must be specified. The theorem does not establish an engineering energy saving for UQPU and does not replace direct wall-plug measurement.

## Relevance across the project

- **Lane A / FND-001:** make side-information assumptions and the work-bound convention explicit before implementing a reference calculation. A small-system fixture should compare the conditional bound with exact finite-dimensional calculations and recover the declared classical/no-side-information limits.
- **Lane B:** quantum memory held by a controller is a mathematical resource in the theorem, not evidence that a particular cloud QPU can acquire or preserve it at the assumed cost.
- **Lane C:** state representation, controller storage, measurement records and information transfer must remain visible; conditional entropy is not classical readable storage capacity.
- **Lane D/G:** no device, control-electronics or manufacturing result follows. If later mapped to hardware, controller preparation, control, readout and reset require target-specific measurements.
- **Lane E:** the result informs thermodynamic boundary discipline, not biomass conversion, critical-material substitution, fusion gain or net delivered electricity.
- **Lane F:** distinguish extractable work (J), dissipated heat (J), wall-plug energy (J), and monetary cost per accepted task. Avoid double-counting or omitting information acquisition, processing and reset.
- **Lane H / INV-034/035:** this is a rigorous theoretical constraint to incorporate into the frontier ledger, not a speculative alternative law.

## Limitations and nonclaims

The primary result is theoretical. UQPU has not independently reconstructed the proof, implemented the full bounds, reproduced numerical examples, or validated an experiment. An accepted theorem does not by itself establish that a real controller can attain the bound. The paper's operational assumptions, definitions and sign conventions must be checked from the full source before any implementation. No AI-generated equation or new physical law is asserted.

## Proposed falsifiable follow-up

Open RG-FND001-QUANTUM-FEEDBACK-WORK-BOUNDARY-001. Pin the arXiv v4 and APS DOI; independently transcribe the theorem assumptions and equations; select finite-dimensional Hamiltonians and correlated controller/system states; compare exact reference calculations against the bound; verify limiting cases and signs; then account separately for side-information acquisition, processing, control and reset at one declared boundary. Reject any implementation that violates the bound under its assumptions or only appears favorable after omitting or double-counting an information cost. Simulated checks remain MODEL_ONLY.
