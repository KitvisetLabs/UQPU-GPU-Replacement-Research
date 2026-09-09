# UQPU Project Goals

## North-star goal

Create a **Universal Quantum Processing Unit (UQPU)** software/hardware architecture whose internal process can differ fundamentally from a GPU, while covering the full functional workload domain currently served by GPUs and targeting the functional/economic roles of accelerator VRAM/HBM plus reductions in host-RAM/data-movement burden.

## Mandatory cloud goal

The UQPU software must run across the broadest practical set of **quantum cloud computers from multiple providers**.

Provider lock-in is not acceptable.

The software must continuously track:
- existing quantum cloud providers;
- newly launched providers;
- new hardware targets from existing providers;
- preview/announced targets;
- retired targets;
- SDK/API changes;
- pricing and access changes.

## Execution objective

For every workload:

```text
UQPU workload
  -> provider discovery
  -> capability match
  -> provider-specific lowering
  -> cloud QPU execution
  -> normalized result
  -> GPU comparison
```

## Memory-system goal

The project must explicitly model and challenge the cost/function of:
- GPU-local VRAM/HBM;
- host RAM used to feed accelerators;
- memory bandwidth;
- intermediate tensor/frame/simulation materialization;
- interconnect/data-movement energy and cost.

The preferred UQPU path is not necessarily a one-for-one replacement of memory chips. Whole-graph semantic execution should avoid materializing large classical intermediate states whenever possible.

Classical RAM remains allowed where required for control, exact storage, ingress/egress and compatibility.

See `docs/MEMORY_REPLACEMENT.md`.

## Functional goal

UQPU must ultimately cover:

- graphics and rendering
- ray/path tracing
- AI training and inference
- tensor and matrix computation
- scientific/HPC workloads
- simulation
- signal/image/video processing
- data analytics
- general-purpose parallel compute
- optimization/search
- arbitrary-kernel fallback

## Economic goal

Primary target: **at least 100× lower total cost per useful completed task than a competitive GPU + VRAM/HBM + host-memory implementation.**

Moonshot target: **up to 100,000,000× lower cost/task** for workload classes where quantum algorithms, provider economics and hardware characteristics make this physically achievable.

For cloud execution, total cost includes provider billing, shots, reservations, retries, classical orchestration, error mitigation/QEC, data transfer and output reconstruction.

## Design principles

1. Same goal/output, different internal process is allowed.
2. Functional equivalence matters more than instruction compatibility.
3. Semantic compilation is preferred over instruction translation.
4. Provider-specific SDKs stay behind adapters.
5. Capability negotiation is mandatory.
6. Quantum-native execution is preferred when beneficial.
7. Reversible deterministic execution exists as a fallback.
8. End-to-end accounting includes input, state preparation, QEC, measurement and output.
9. CPU/control electronics are allowed; GPU dependency is not.
10. Claims must be benchmarked and falsifiable.
11. Cost targets are goals, not assumed outcomes.
12. Negative results and provider incompatibilities must be recorded.
13. Provider discovery is continuous, not a one-time survey.

## Success definition

A workload is functionally replaced when no GPU is required in the validated execution path and the UQPU produces an accepted result.

A cloud provider reaches integration success when it progresses through adapter/dry-run/simulator/real-QPU validation.

A workload is economically surpassed when:

[
C_{GPU/task}/C_{UQPU-cloud/task} ge 100
]

The long-term program succeeds only when broad GPU functional coverage, broad quantum-cloud portability and strong economic advantage converge.
