# Literature watch — certified maximum-likelihood benchmarking for quantum LDPC decoders

**Watch date:** 2026-10-28  
**Primary source:** Michele Banfi, Marco Ferrari, Antonino Favano, Alberto Tarable and Luca Barletta, “Certified Non-Degenerate Maximum-Likelihood Benchmarking of Quantum LDPC Decoders,” arXiv:2610.28008v1, submitted 2026-10-20.  
**Source:** https://arxiv.org/abs/2610.28008  
**Evidence class:** `LITERATURE_ONLY` — official arXiv preprint; not independently reproduced by UQPU.

## Genuine methodological novelty

The paper proposes per-shot certification of a **non-degenerate maximum-likelihood (ML) decoding reference** under circuit-level noise. It bounds the minimum correction cost in the observed logical class and competing classes, classifies a shot as success, failure or undecided, and uses branch-and-bound to refine the intervals under resource limits. The aggregate interval width equals the undecided fraction. On two bivariate-bicycle QLDPC codes, the authors report that best-first ordered-statistics decoding (BF-OSD) tracks their non-degenerate ML benchmark closely but leaves some ML-correctable shots.

The contribution is a bounded reference-and-undecided accounting method, not a new physical law or an unconditional quantum-advantage result. It is especially relevant where a heuristic decoder's measured logical error rate is otherwise compared without a strong reference.

## Limitations and evidence boundary

- The source is an arXiv preprint; UQPU has not reproduced its derivation, per-shot bounds or reported decoder comparison.
- The reference is explicitly **non-degenerate ML**. It must not be silently equated with a fully degeneracy-aware optimal decoder or an architecture-independent oracle.
- Circuit-level noise, code family, syndrome sampling, correction-cost definition and logical-class convention affect the benchmark. Results cannot be transferred to another provider/target, noise model or code without a matched test.
- A shot left undecided under a resource limit is neither automatically a decoder failure nor a certified success. The undecided fraction must remain visible in the bound.
- The arXiv record does not provide a directly linked implementation/data package. If the source's exact circuits, noise parameters or sampled shots cannot be reconstructed, that is a blocker, not permission to replace them with an unlabelled simulation.

## Exact UQPU relevance

- **Lane A:** strengthens the priority-1 rule that execution success is not quality acceptance. A decoder/reference certificate can help define a quality oracle before comparing QUBO/QAOA or other candidate workloads, but only when the task contract and noise model match.
- **Lane B:** any future provider result must retain its own target, calibration/noise snapshot, SDK lowering, shots, billing and decoder configuration. Do not combine one target's logical success probability with another target's cost.
- **Lane C:** decoder working memory, syndrome/state I/O, latency and data movement are part of the usable system cost, not free post-processing.
- **Lane D/G:** code distance, connectivity and physical error assumptions must map to the actual device/process; no device or manufacturing result follows from the decoder paper.
- **Lane F:** measure reference search time, branch-and-bound nodes, memory, undecided fraction, decoder runtime, retries, host compute and energy where measurable; report cost per accepted useful task only after the same quality threshold is met.
- **FND-003:** this is a useful example of a certified statistical/computational reference, but it does not by itself measure a physical quantum-speed-limit gap.
- **INV-029–035:** the source does not demonstrate phone-class compression, memory replacement, Pangola substitution, bio-oil, fusion electricity, financing reduction or a new physical law.

## Proposed falsifiable follow-up

1. Pin the exact paper version and transcribe the correction-cost bounds, logical-class conventions and circuit-level noise assumptions.
2. Build a tiny independent reference where exhaustive enumeration gives the exact non-degenerate ML optimum. Check that every reported interval encloses the exhaustive value.
3. Use positive controls with uniquely classified shots and adversarial controls with ambiguous/tied logical classes or deliberately tight resource budgets. Verify that undecided cases remain undecided and that aggregate interval width equals the undecided fraction.
4. Reconstruct the two reported bivariate-bicycle examples only if the circuit, noise, code and sampled-shot inputs can be pinned. Retain source-to-result hashes and all failed cases.
5. Compare BF-OSD and other decoders on identical shots and parameters. Report success/failure/undecided counts, uncertainty, runtime, peak memory, decoder/host costs and any measured energy.
6. Require an independent implementation before using the reference as a benchmark gate. Keep simulated results distinct from target-specific hardware data and commercial economics.

## Stop rules

Reject the certificate implementation if any interval excludes the exhaustive reference, the undecided fraction does not match the declared aggregate interval, or benign parameter/implementation changes silently alter classification. Do not call a decoder “optimal” when only the non-degenerate ML reference was bounded. Do not promote decoder quality into end-to-end workload advantage unless accepted useful output, latency, throughput, host overhead, energy where measurable and total cost are matched.

## Decision

Open the focused gap `RG-QEC-ML-DECODER-CERTIFICATION-2026-10-28` for an independent, small-instance certificate reconstruction. Keep the existing Quantinuum Helios color-code reproduction gap separate: it addresses external hardware claims, whereas this gap addresses the decoder-reference method. No code or provider execution is changed in this cycle.
