# Literature watch — 2026-10-30: peer-reviewed Mamba neural decoder for QEC

**Source:** Lee, Hur & Park, “Scalable neural decoders for practical real-time quantum error correction,” *npj Quantum Information*, published 2026-10-28, DOI https://doi.org/10.1038/s41534-026-01403-y. Preprint: arXiv:2510.22724v1, https://arxiv.org/abs/2510.22724.  
**Primary owner:** Lane B. **Interfaces:** A/C/D/F/G/H.  
**Evidence:** PEER-REVIEWED EXTERNAL PAPER + SOURCE-REPORTED SYCAMORE DATA REANALYSIS + SIMULATED REAL-TIME NOISE; NOT REPRODUCED BY UQPU.  
**Work item:** QEC-MAMBA-001. **Gap:** ../RESEARCH_GAP_QEC_MAMBA_DECODER_REPRODUCTION_2026-10-30.md.

## Genuine novelty

The authors replace the attention mixer in a recurrent surface-code decoder with a Mamba structured state-space module. They report architecture-specific O(d²) scaling with surface-code distance d versus O(d⁴) for the Transformer attention comparator. The publisher abstract reports matching memory performance on Sycamore hardware data and better simulated real-time performance with decoder-induced noise, tested up to d=9.

The accessible arXiv v1 gives detail: its hardware memory analysis covers d=3 and d=5 on a 72-qubit Sycamore processor, X/Z bases and up to 25 correction cycles. It reports Mamba logical error per round around 2.98×10⁻² at d=3 and 3.03×10⁻² at d=5; at d=5 both neural decoders underperform the tensor-network comparator. The preprint reports up to 100 million synthetic pretraining samples and local RTX 4090 block timing.

## Version and evidence boundary

The publisher abstract says simulated real-time results extend to d=9. The accessible preprint v1 describes real-time simulations at d=3/5/7 and a threshold crossover calculated from d=3 versus d=5. Its reported 0.0104 (Mamba) versus 0.0097 (Transformer) threshold uses a modeled decoder-induced-noise channel, with p_dec proportional to d² or d⁴ and calibrated using an approximately 40 μs AlphaQubit d=9 latency. This is not measured Mamba hardware-in-the-loop feedback. Reconcile the version-of-record PDF and supplement before transferring preprint numbers to the journal article.

The inspected preprint PDF identifies no author code repository. UQPU has not retrieved or hashed the dataset, model, environment or supplement.

## Limitations and relevance

- Sycamore hardware-data reanalysis is source-reported, not an independent UQPU reproduction.
- Local RTX 4090 block timing is not full controller latency, deadline compliance or p50/p95/p99.
- The preprint's threshold is a d=3/d=5 crossover, not an asymptotic large-distance demonstration.
- Keep the negative d=5 tensor-network comparison visible.
- **A/B:** logical memory and real-time feedback are distinct accepted-output tasks; no provider job.
- **C:** measure syndrome bytes, model/checkpoint bytes, hidden-state bytes, buffers, RAM/VRAM, transfer and reconstruction. Decoder state is classical state, not quantum memory or persistent storage.
- **D/G:** derive control-electronics/accelerator constraints only from measured cadence, precision, memory and power.
- **E/F:** no fuel, fusion, cooling-energy or cost advantage; future economics must include training, inference, host, memory, transfer, energy and cost per accepted correction.
- **H/INV-029/034/035:** this is a subsystem research lead, not physical data-center compression or a new law.

## Falsifiable follow-up

Reconcile the version of record; identify and license-check the exact Sycamore data and shot groups; pin hashes and environment; reproduce Mamba/Transformer memory metrics and MWPM/TN baselines on identical shots; reproduce the simulated-noise arm separately; then measure actual target latency and deadline misses. Add group-disjoint device/patch/noise holdouts and report logical-error counts, uncertainty, p50/p95/p99, sustained throughput, model/state/buffer bytes, peak memory, transfer, retries, energy and cost per accepted logical correction. Reject real-time claims if latency tails miss cadence, held-out quality fails, or full costs erase the benefit.

No UQPU decoder result, real-time hardware feedback, quantum advantage, memory replacement or physical law is claimed.
