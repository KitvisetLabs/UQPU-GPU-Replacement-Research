# Provider Watch — Qiskit 2.6, Amazon Braket QEC decoding and compliance boundary

**Watch date:** 2026-10-26  
**Primary owner:** Lane B — cloud/QPU/provider integration  
**Cross-lane owners:** Lane A compiler/runtime; Lane C state and data movement; Lane F benchmark/economics; Lane D/G device and manufacturing co-design; Lane H publication  
**Evidence class:** OFFICIAL_PROVIDER_RELEASES_AND_VENDOR_REPORTED_BENCHMARKS  
**UQPU evidence status:** PROVIDER_SURVEILLANCE_ONLY; no adapter compatibility, independent performance reproduction, or project economic claim promoted

## 1. IBM Qiskit SDK v2.6 — published 2026-10-22

Official source: https://www.ibm.com/quantum/blog/qiskit-2-6-release-summary

IBM describes v2.6 as a C-API-focused release. It adds a customizable C API pass-manager framework, type-checked lowering across multiple intermediate representations, QPY circuit serialization from the C API, custom operations including hardware-native operations, and QPY format v18 as the default with a more compact encoding. The release continues work toward using Qiskit's C API in environments without Python; Python remains a dependency in the current release's stated limitations.

**UQPU relevance:** this is a concrete Lane A/B interface lead for provider-neutral compiler lowering and cross-language runtime design. It may help future C/C++/Julia/Fortran clients and reduce serialization overhead for large circuit/register payloads. It is not proof that UQPU's current provider adapters work with v2.6 or that QPY v18 is backward-compatible.

**Follow-up:** keep the currently pinned SDK baseline unchanged until compatibility is tested. Add a version-matrix check for the existing supported SDK, v2.6, QPY v18 and explicitly requested older QPY versions; verify semantic round-trip, metadata preservation, byte size, serialization/deserialization time, and failure behavior. A smaller QPY file is not itself a measured reduction in network transfer, memory pressure, energy, or total cost.

## 2. Amazon Braket + NVIDIA Ising Decoding — published 2026-10-21

Official source: https://aws.amazon.com/blogs/quantum-computing/decoding-quantum-errors-with-nvidia-ising-decoding-on-aws/

AWS reports a classical GPU-assisted pre-decoder for quantum error correction. Its training comparison uses eight-GPU EC2 instances spanning A100, H100, H200, Blackwell B200 and L40S accelerators, with simulated distance-9 surface-code syndromes and a circuit-level depolarizing noise model at physical error rate 0.006. The vendor reports up to about 39% lower training epoch time from A100-based P4d to B200-based P6; its listed instance comparisons show cost/time tradeoffs rather than a single universally optimal GPU. For inference at code distance 31, AWS reports roughly 2.4×–2.9× lower decoding latency per round than MWPM alone while improving logical error rate for the described setup.

**Evidence classification and limitations:** these are vendor-reported benchmark results for a particular model, simulator/noise setting, GPU instance configuration and decoding pipeline. They are not an independent reproduction, not an end-to-end QPU workload benchmark, and not evidence that quantum hardware replaces the GPUs used for training or decoding. The reported latency must be assessed alongside decoder accuracy, QEC cycle timing, instance cost, utilization, memory, host/data movement and deployment overhead. A simulated syndrome dataset is not a real-QPU result.

**UQPU relevance:** Lane A must treat classical QEC decoding as part of the accepted-task path, not as a free external service. Lane F should use this as a source-bound baseline candidate for GPU/CPU/NPU decoder comparison. Lane C should account for syndrome volume and transfers; D/G should use validated latency and control requirements before inferring device or fabrication needs. Any cost comparison must retain the same noise model, code distance, logical-error target, throughput and target-specific pricing in one matched record.

**Follow-up:** reproduce the vendor configuration from pinned code and dataset/noise assumptions; report model-training and inference costs separately; compare MWPM-only and pre-decoder-plus-MWPM at matched logical error rate and QEC-cycle deadline; include instance prices, wall-clock time, GPU memory, energy if measured, and all failed runs. Do not combine this simulated benchmark with another provider's QPU success probability or price.

## 3. Amazon Braket FedRAMP Class C scope — published 2026-10-16

Official source: https://aws.amazon.com/about-aws/whats-new/2026/10/braket-fedramp-class-c/

AWS states that the Braket API/SDK, job orchestration and management, compilation and S3 result storage are within the stated FedRAMP-certified boundary in available AWS US Regions, while quantum workloads executed on third-party hardware providers are outside that boundary.

**UQPU relevance:** this is a Lane B governance and deployment-boundary update, not a new QPU target, price change or performance result. The adapter and workload contract must distinguish AWS-managed control-plane/data services from the actual hardware-provider execution boundary when compliance, data retention, residency or risk enters a cost/service contract.

**Follow-up:** update the provider capability/security matrix only after checking the official scope and target's region; identify which payloads and result artifacts leave the AWS-managed boundary; keep compliance metadata separate from technical acceptance and measured economics.

## Cross-lane decision

- **A:** investigate Qiskit 2.6 C API / multi-IR / QPY compatibility without changing the pinned baseline until exact-version tests pass.
- **B:** update provider surveillance metadata for IBM Qiskit and Amazon Braket; no new hardware adapter or target authorization is implied.
- **C:** measure serialization and syndrome/data movement only on matched payloads; do not infer energy savings from file-size or latency claims alone.
- **D:** use QEC latency/error constraints only as inputs to a device contract; no device claim follows from vendor benchmark numbers.
- **E:** no direct biomass, material, fuel, fusion or cooling result.
- **F:** preserve vendor evidence labels, matched hardware/workload/pricing boundaries, and total cost per accepted logical result.
- **G:** no manufacturing/yield/equipment result; co-design only after validated device/resource requirements.
- **H:** keep provider announcements as source-linked strategic intelligence, not evidence that a planned commercial or industrial outcome has been achieved.

## Next highest-value gate

Before any provider-path change, run a pinned SDK compatibility matrix and a source-exact, reproducible QEC-decoder benchmark with matched logical-error target and total cost. No paid QPU job is authorized by this watch; simulator/dry-run first.
