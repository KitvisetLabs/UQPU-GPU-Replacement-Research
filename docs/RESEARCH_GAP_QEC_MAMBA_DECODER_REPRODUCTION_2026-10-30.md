# Research gap RG-QEC-MAMBA-001 — Mamba decoder reproduction and real-time validation

**Opened:** 2026-10-30 · **Primary owner:** Lane B · **Co-owners:** A/C/D/F/G/H  
**Status:** LITERATURE_ONLY / VERSION RECONCILIATION OPEN / REPRODUCTION NOT RUN  
**Source:** Lee, Hur & Park, *npj Quantum Information* (2026-10-28), DOI 10.1038/s41534-026-01403-y; arXiv:2510.22724v1.  
**Related:** INV-025/026/027/029/034/035; FND-002/003; FIN-001.

## Objective

Determine whether the source-reported Mamba QEC decoder can be reproduced and whether its architecture-specific scaling yields a measured target-specific deadline/quality improvement after full controller-path accounting. This is a classical QEC-support workload, not a quantum algorithmic advantage claim.

## Source and blockers

- Publisher abstract says simulated real-time results through d=9; accessible arXiv v1 describes d=3/5/7 simulations and a d=3-versus-d=5 threshold crossover. Reconcile version of record and supplement.
- Preprint hardware memory data: 72-qubit Sycamore, d=3/5, X/Z bases, up to 25 cycles; source reports a 50/50 fine-tuning/held-out split.
- Preprint real-time effect injects modeled decoder-induced noise p_dec proportional to d² (Mamba) or d⁴ (Transformer), calibrated from approximately 40 μs AlphaQubit latency at d=9. It is not measured Mamba hardware feedback.
- No author code repository was identified in the inspected PDF; no data/model license, hashes or environment have been verified by UQPU.

## Gates

**Gate 0 — provenance:** retrieve version-of-record PDF/supplement; diff against arXiv v1; identify dataset, scripts/checkpoints, license, byte lengths, hashes, shot/group IDs, detector-error model and calibration provenance; pin a clean environment. Stop if data access or license cannot be verified.

**Gate 1 — exact reproduction:** implement/source-pin Mamba and Transformer; reproduce memory metrics; run MWPM and tensor-network comparators on identical shots/labels; report integer error counts, denominators, uncertainty and failures. Preserve the preprint's negative d=5 TN comparison.

**Gate 2 — modeled real-time arm:** reproduce the paper's injected-noise model separately; record p_dec mapping, calibration constant, noise model, distances and sequence lengths. Vary the latency mapping and search counterexamples. Do not label this hardware feedback.

**Gate 3 — measured target:** measure acquisition-to-correction p50/p95/p99/worst latency, sustained throughput, deadline misses, logical quality on group-disjoint device/patch/noise holdouts, model/hidden-state/syndrome-buffer bytes, peak RAM/VRAM, transfers, retries, energy and cost per accepted correction.

Reject real-time claims if the measured latency tail misses cadence, held-out logical quality degrades, source results cannot be reproduced, or full resource/cost accounting erases the benefit.

**Nonclaims:** no QPU job, quantum advantage, memory replacement, physical-law change, Pangola substitution, accepted fuel, net fusion electricity, WACC or Data-Center-to-One-Phone result.
