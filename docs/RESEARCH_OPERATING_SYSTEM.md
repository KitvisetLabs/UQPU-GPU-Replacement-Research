# UQCS Research Operating System

## Purpose
Coordinate all research tracks against one mission: complete useful-computing functional coverage with provider portability and a measured >=100x total cost/useful-task target, while retaining 100,000,000x as a workload-specific moonshot.

## Workstreams
1. Semantic compiler / CPU-GPU workload contracts
2. Quantum algorithms, QEC and logical architecture
3. Cloud providers and execution adapters
4. Memory / VRAM / HBM / storage
5. Photonics and optical interconnect
6. Semiconductor fabrication and lithography
7. Packaging, chiplets and interconnect
8. Biomass and advanced/critical materials
9. Power, cooling and data-center integration
10. Cost, inverse design and financing
11. Evidence, testing and system integration

## Interface contract
Every workstream returns:
- objective
- artifact/code/model
- evidence level
- measurable requirements
- cost contribution
- dependencies
- blockers/negative results
- next experiment
- integration impact

## Integration gate
A candidate architecture advances only when:
- workload output contract is defined;
- provider/hardware modality is compatible;
- memory/I/O path is included;
- fabrication route is plausible or explicitly blocked;
- power/cooling is included;
- cost/task includes all known major components;
- evidence label is explicit;
- unresolved gaps are written to RESEARCH_GAPS.md.

## Daily cycle
inspect -> research -> implement/model -> test -> falsify -> refine -> integrate -> document gaps -> update WORKLOG/DECISIONS -> sync GitHub.

## Priority rule
Prefer work that reduces the largest uncertainty or cost bottleneck, rather than work that merely adds features.
