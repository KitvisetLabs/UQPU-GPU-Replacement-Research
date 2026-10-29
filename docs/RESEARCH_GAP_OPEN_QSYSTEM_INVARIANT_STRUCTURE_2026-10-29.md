# Research gap RG-OPEN-QSYS-INVARIANT-STRUCTURE-001

**Opened:** 2026-10-29  
**Owner:** Lane A (benchmark/output contract); Lane B (open-system model interface); Lane F (evidence/economics); Lane H (source provenance)  
**Status:** PREREGISTERED FOLLOW-UP / NOT IMPLEMENTED OR RUN / EXTERNAL PAPER NOT REPRODUCED

Teretenkov, Kuznetsov & Pechen, *Physical Review A* 114, 043115 (published 2026-10-21), DOI 10.1103/lv26-srm2, report machine-learning inference of invariant observable subalgebras from multi-time measurements under restricted access, with synthetic and waveguide-QED demonstrations. Only the official publisher abstract was accessible in this cycle; source code, data and detailed likelihood/model-selection methods were not audited.

## Missing evidence

- Reproduction-quality specification of model families, generator conventions, accessible measurement operators and sequence likelihood.
- Exact ground-truth invariant algebra and separately verified decoherence-free labels.
- Held-out performance on whole dynamics families/regimes, uncertainty calibration and false-discovery rate.
- Explicit abstention for structures that are not identifiable from the chosen measurement access.
- Robustness to symmetry breaking, non-Markovian model mismatch, measurement-label shuffling, finite-shot noise and candidate multiplicity.
- Matched baseline resource accounting: shots, measurement settings, host CPU/GPU time, memory, state/data movement, retries, reconstruction and total cost.
- Any demonstrated reduction in target-specific readout, runtime, energy, storage or cost per accepted useful task.

## Unlock

Implement the preregistered Lane A benchmark contract at `research_lanes/A_quantum_programming_runtime/OPEN_QUANTUM_INVARIANT_STRUCTURE_BENCHMARK_V1.json`. Start with exact small synthetic models and classical baselines; independently check invariance and algebra closure, and require stronger checks before using the term *decoherence-free*. Keep the source's reported waveguide-QED result external. Do not proceed to a paid QPU job without credentials, a bounded budget and explicit owner consent.

**Non-claims:** no new physical law, quantum advantage, reduced readable-memory lower bound, device/material improvement, accepted fuel, net fusion electricity, lower WACC or Data-Center-to-One-Phone closure.
