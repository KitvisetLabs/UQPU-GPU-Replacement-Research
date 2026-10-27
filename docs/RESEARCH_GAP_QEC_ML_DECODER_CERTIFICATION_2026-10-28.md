# Research gap RG-QEC-ML-DECODER-CERTIFICATION-2026-10-28 — certified ML reference reconstruction

**Opened:** 2026-10-28  
**Primary owner:** Lane B — cloud/QPU/provider integration and target evidence  
**Co-owners:** Lane A — workload quality/reference certificates; Lane C — decoder memory/I/O; Lane F — benchmark/economics; Lane H — literature publication  
**Status:** OPEN / LITERATURE_ONLY / REPRODUCTION_NOT_RUN  
**Related:** INV-001/002/004/007/010/019/022/024, FND-003, INV-029/034/035  
**Primary source:** Banfi et al., [arXiv:2610.28008v1](https://arxiv.org/abs/2610.28008), submitted 2026-10-20  
**Literature watch:** `docs/literature_watch/2026-10-28-certified-qldpc-decoder-benchmark.md`

## Objective

Reconstruct the source's per-shot certificate for a non-degenerate maximum-likelihood (ML) decoder under circuit-level noise, then determine whether the certified reference can serve as a quality baseline for a matched QPU workload. This is a decoder-reference gap, distinct from the Helios color-code hardware-reproduction gap.

## Source-reported method and evidence boundary

The paper bounds minimum correction cost in the observed logical class and competing logical classes, then labels each sampled shot success, failure or undecided. Branch-and-bound refines the bounds under resource limits; the aggregate interval width is the undecided fraction. The authors apply the framework to two bivariate-bicycle QLDPC codes and report that BF-OSD tracks the non-degenerate ML benchmark closely but misses some ML-correctable shots.

These are external preprint claims. UQPU has not reproduced the derivation, code/data, circuit-level noise model, shot-level labels or aggregate results. The reference is explicitly non-degenerate ML, not automatically a fully degeneracy-aware optimum. The arXiv record does not provide a directly linked implementation/data package; exact inputs may therefore be a blocking dependency.

## Required inputs and contract

Freeze the source version, code/check matrices, logical-class convention, circuit-level noise channel and parameters, sampled shots/syndromes, correction-cost definition, decoder settings, branch-and-bound limits, software revision and all hashes. Keep these outcomes separate:

- certified success;
- certified failure;
- undecided under the declared resource limit.

Never silently map undecided to success or failure. Report counts and fractions for all three, along with the resulting valid interval. Preserve every malformed input, failed search and counterexample.

## Unlock protocol

1. Implement an independent tiny-instance oracle and compare every bound against exhaustive enumeration.
2. Verify that each interval contains the exact non-degenerate ML correction cost and that the aggregate interval width equals the undecided fraction.
3. Test positive controls (unique optimum / enough resources), negative controls (ties, deliberately constrained search, malformed syndromes) and implementation variants.
4. Reconstruct the two paper examples only if the circuit/noise/shot inputs are recoverable. Otherwise record the missing artifacts and stop at the specification level.
5. Compare BF-OSD and other candidate decoders on identical samples, with uncertainty, runtime, peak memory, decoder overhead and energy only where measured.
6. Require independent implementation/review before using this reference to accept a workload or claim a decoder-quality improvement.
7. Only after a software reproduction passes may a target-aware simulator and then an explicitly authorized hardware experiment be considered. Any paid job requires credentials, a bounded budget and explicit user consent.

## Falsifiers and stop rules

Fail the implementation if a certified interval excludes the exhaustive result, if the undecided accounting identity fails, if success/failure classifications change under a semantically neutral representation change, or if the source example cannot be reproduced but is nevertheless reported as reproduced. Do not claim general QEC optimality, a quantum advantage or a new physical limit from the benchmark.

## Cross-lane consequences

- **A:** use certified reference labels as one quality gate, not as the entire accepted-useful-output contract.
- **B:** retain provider/target, calibration, SDK, shot and billing provenance; never mix target-specific probabilities and prices.
- **C:** count decoder memory, syndrome I/O and reconstruction costs; no readable-memory replacement claim.
- **D/G:** bind code/noise assumptions to device connectivity and fabrication constraints; no yield or process result.
- **E:** no biomass, material, bio-oil, cooling or fusion evidence is supplied by this paper.
- **F:** cost per accepted useful task includes decoder/host compute, retries, latency, throughput, memory and energy where measured.
- **H:** preserve source limitations and multilingual strategy references; no financing-rate claim.
- **FND/EQN:** a statistical/computational reference is not a physical-speed-limit measurement or a new physical law.

**Evidence class:** `LITERATURE_ONLY` until independent bounds, controls and source-level reproduction pass. Any synthetic tiny-instance test is a software contract, not hardware or commercial evidence.
