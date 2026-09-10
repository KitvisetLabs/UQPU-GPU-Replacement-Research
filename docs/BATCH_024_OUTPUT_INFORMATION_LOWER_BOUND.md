# Batch 024 — Output-Information Lower Bounds

**Date:** 2026-09-10  
**Foundation:** INV-034 / FND-002  
**Primary owner:** Lane C — State / Memory / Storage / Data Movement  
**Evidence:** THEORY + EXECUTABLE_BOUND  
**REAL_QPU:** No  
**Paid QPU job:** No

## Question

If a future UQPU uses an exponentially large quantum state internally, can that fact alone eliminate the classical output, RAM/VRAM/storage and data-movement requirements of the application?

## Result

No. Internal state-space size and application-visible classical information are different resources.

If a useful result must exactly identify one arbitrary outcome from `M` distinguishable possibilities, any fixed-length classical label needs at least

`ceil(log2 M)` bits.

The proof is the elementary counting argument: `b` classical bits provide at most `2^b` labels.

This result does **not** say that a quantum algorithm must read out every amplitude. It says the opposite: the project must define what compact useful result is actually required and then account for at least that result's output semantics.

## Executable implementation

`software/uqpu-prototype/uqpu/output_information.py` now implements:

- exact distinguishable-outcome label floor;
- full `n`-bit assignment identity floor;
- fixed-width results/s bitrate accounting;
- binary entropy;
- a Fano-inequality mutual-information lower bound for uniformly distributed error-tolerant M-way identity.

The unit tests include outcome sets through `2^512` without constructing a statevector.

## Exact zero-error scenarios

| Contract | distinguishable outcomes | minimum fixed-length label |
|---|---:|---:|
| binary decision | 2 | 1 bit |
| triangle 3-bit assignment identity | 8 | 3 bits |
| ER6 assignment identity | 64 | 6 bits |
| ER8 assignment identity | 256 | 8 bits |
| 32-variable full assignment | 2^32 | 32 bits |
| 128-variable full assignment | 2^128 | 128 bits |
| 512-variable full assignment | 2^512 | 512 bits |

This is why `2^512` possible assignments do **not** mean a 512-qubit optimizer has to transmit `2^512` classical bits merely to return one selected 512-bit assignment. The output identity floor for that contract is 512 bits. Conversely, the huge Hilbert space also cannot be advertised as `2^512` directly readable classical memory entries.

## Service-rate examples

If every result must be emitted independently as an uncompressed fixed-width label:

- 32-bit assignment at 1,000,000 results/s -> 32,000,000 bit/s raw label rate;
- 128-bit assignment at 1,000,000 results/s -> 128,000,000 bit/s;
- 512-bit assignment at 1,000,000 results/s -> 512,000,000 bit/s.

These are **fixed-width interface calculations**, not universal channel-capacity lower bounds. Source coding, correlations, side information, batching or a different application contract can change actual transport requirements.

## Error-tolerant identity: Fano lower bound

For a uniformly distributed target over `M` outcomes with decoder error probability `Pe`, Fano's inequality gives

`I(X;Y) >= log2(M) - h2(Pe) - Pe*log2(M-1)`.

For `M=64`:

- `Pe=0`: at least 6.000000 bits mutual information;
- `Pe=0.01`: at least 5.85943406486909 bits;
- `Pe=0.10`: at least 4.933276414060727 bits.

This is a mutual-information bound for that statistical decision problem. It must **not** be re-labeled as physical qubit count, memory cells, network bits or operation count without an additional implementation theorem.

## Strategic consequence

FND-002 gives the project two simultaneous rules:

1. **Do not overcount output:** a quantum algorithm need not materialize its entire internal state when the useful contract only needs a compact decision/sample/witness.
2. **Do not hide required output:** when the user actually requires large classical data, the readout/reconstruction/network/storage path remains part of Data-Center-to-One-Phone and total-cost accounting.

This directly strengthens INV-026. RAM/VRAM/storage replacement must be judged by application-visible semantics, not by Hilbert-space dimension.

## Eight-lane integration

| Lane | Batch 024 effect | Next gate |
|---|---|---|
| A | compiler can preserve compact semantic outputs instead of materializing unnecessary state | attach output contract to first workload IR |
| B | provider result decoding must satisfy the same distinguishability/error contract | measured provider result bytes/latency |
| C | exact and error-tolerant output-information floors are executable | instrument real state/I/O/reconstruction |
| D | readout hardware must support the required service semantics | measured readout/control path |
| E | information movement becomes an energy/cooling input, but no energy floor is inferred from bits alone | measured joules/accepted result |
| F | output bytes/rate become mandatory total-cost evidence | classical/QPU matched accounting |
| G | readout/control/test equipment requirements inherit output-rate contracts | equipment throughput/reliability evidence |
| H | extreme-compression strategy cannot hide external egress/storage resources | finance compact-output experiments first |

## Next highest-value FND-002 experiment

Extend UQPU workload contracts and benchmark artifacts with explicit `required_output_information`, `measured_output_bytes`, `reconstruction_seconds`, `side_information`, `error_probability` and `output_rate` fields. Then compare a compact semantic-output quantum formulation against the competitive classical pipeline under the **same accepted useful result**.

No quantum advantage, 100x/100,000,000x advantage, RAM/VRAM/storage replacement or Data-Center-to-Phone feasibility is demonstrated by this mathematical bound alone.
