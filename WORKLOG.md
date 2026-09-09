# UQPU Work Log

## 2026-09-09

### Project conception
Defined the core objective: design a QPU-like architecture that can replace the **functional goals** of GPUs without requiring the same internal process.

### Functional scope established
Identified target domains including graphics, rendering, AI, matrix/tensor workloads, HPC, simulation, analytics, signal processing, media, optimization and general-purpose parallel compute.

### Architecture direction
Proposed the Universal Quantum Processing Unit (UQPU) as a quantum-first heterogeneous accelerator with semantic compilation, quantum-native execution, reversible fallback, measurement/decoding, memory/I/O and QEC as first-class components.

### Compiler direction
Established a semantic compiler model:
application intent -> mathematical IR -> backend selection -> quantum/reversible execution.

### Feasibility framing
Recorded major barriers: state preparation, classical input/output lower bounds, measurement, reversible arithmetic overhead, latency, fault tolerance and cost.

### Repository creation
Research repository established at:
https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research

Repository verified public.

### Authorship
Lead Researcher: Kanutsanan Pongpanna  
AI Research Collaborator: OpenAI GPT-5.6 Sol

### Economic objective added
Added a primary target of at least **100× lower total cost per useful task** than GPU and a workload-specific moonshot target of **100,000,000×**.

### Process documentation
Added project goals, research/engineering process, decision log and work log so future changes can be traced.

## Next research work

- create formal cost model spreadsheets/data structures
- build per-workload resource estimators
- add semantic IR specification
- design prototype runtime and backend interface
- implement first reversible fallback kernels
- implement first quantum-native benchmark candidates
- compare against real GPU baselines
- identify which workload classes can realistically approach 100× and which cannot
