# UQPU Project Goals

## North-star goal

Create a new **Universal Quantum Processing Unit (UQPU)** whose internal process does not need to resemble a GPU, but whose external capabilities can satisfy every major objective currently served by GPUs.

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
- arbitrary kernel fallback

## Economic goal

Primary target: **at least 100× lower total cost per useful completed task than a competitive GPU implementation.**

Moonshot target: **up to 100,000,000× lower cost/task** for workload classes where quantum algorithms and hardware economics make this possible.

## Design principles

1. Same goal/output, different internal process is allowed.
2. Functional equivalence matters more than instruction compatibility.
3. Semantic compilation is preferred over instruction translation.
4. Quantum-native execution is preferred when beneficial.
5. Reversible deterministic execution exists as a fallback.
6. End-to-end accounting includes input, state preparation, QEC, measurement and output.
7. CPU/control electronics are allowed; GPU dependency is not.
8. Claims must be benchmarked and falsifiable.
9. Cost targets are goals, not assumed outcomes.
10. The project must preserve negative results and unresolved barriers.

## Success definition

A workload is functionally replaced when no GPU is required and the UQPU produces an accepted result under the workload's output contract.

A workload is economically surpassed when:

[
C_{GPU/task}/C_{UQPU/task} ge 100
]

The long-term program succeeds only when broad functional coverage and strong economic advantage converge.
