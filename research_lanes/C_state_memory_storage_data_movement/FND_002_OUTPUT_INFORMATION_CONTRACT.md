# FND-002 — Output-Information Lower-Bound Contract

**Owner:** Lane C — State / Memory / Storage / Data Movement  
**Foundation:** INV-034 / FND-002  
**Mission link:** INV-026 and INV-029

## Purpose

A quantum state may use a very large Hilbert space internally, but an application-visible result still has an output contract. FND-002 prevents state-space dimension from being confused with freely accessible classical RAM, VRAM, storage or output bandwidth.

## Zero-error identity bound

If a result must exactly identify one arbitrary outcome among `M` distinguishable possibilities, a fixed-length classical label requires at least

`b = ceil(log2 M)` bits.

Reason: `b` bits provide at most `2^b` distinct labels.

For one arbitrary `n`-bit assignment there are `2^n` possible assignments, therefore the exact identity output floor is `n` classical bits. This is an **output-label bound**, not a lower bound on computation time, quantum memory, circuit width, energy or storage capacity.

## Approximate identity / error-tolerant contract

When the target outcome is uniformly distributed over `M` possibilities and the decoder is allowed error probability `Pe`, the project may use Fano's inequality as a lower bound on the mutual information required by the stated decision problem:

`I(X;Y) >= log2(M) - h2(Pe) - Pe log2(M-1)`.

Record the prior, error definition and decoder. Do not convert this mutual-information lower bound directly into qubit count, physical wire rate, memory cells or operations without an additional channel/implementation theorem.

## Fixed-width service-rate contract

For a service that emits independent fixed-width labels at `R` results/s, the raw label bitrate is

`ceil(log2 M) * R` bit/s.

This is a fixed-width interface requirement, not a universal Shannon channel-capacity lower bound. Correlations, side information, variable-length/source coding, batching or a changed application contract may reduce transported average bits.

## Required evidence fields

For every use of an output-information bound record:

- workload/contract ID;
- what constitutes a distinct accepted outcome;
- number of distinguishable outcomes `M` or derivation thereof;
- exact-vs-approximate output requirement;
- allowed error probability and prior distribution where applicable;
- whether side information is available to the receiver;
- whether the interface is fixed-width, compressed, batched or interactive;
- result rate/latency requirement;
- decoder/reconstruction cost;
- actual measured output bytes/bits when available.

## Memory/storage boundary

This contract explicitly rejects the shortcut `n qubits => 2^n readable classical memory words`. Hilbert-space dimension is not by itself application-visible random-access storage capacity. A RAM/VRAM/storage replacement claim must separately satisfy capacity, access, persistence, bandwidth, latency, durability/recovery and output/read semantics.

## Data-Center-to-Phone consequence

The final phone-class system must be judged by the service it actually exposes. If a service contract requires a high rate of distinct classical outputs, the egress/reconstruction path cannot be hidden outside the device boundary. Conversely, if the application only needs a compact decision, statistic, sample or optimization witness, UQPU research should preserve that smaller semantic output rather than materializing unnecessary classical intermediate state.

## Next experiments

1. attach output-information fields to UQPU workload contracts;
2. instrument measured output bytes and reconstruction time in classical/QPU benchmark artifacts;
3. compare semantic compact-output formulations against materialized intermediate-state pipelines;
4. for approximate outputs, use explicit task-quality/error contracts rather than assuming every amplitude must be read out;
5. propagate the output floor into network, storage, energy and total-cost accounting.
