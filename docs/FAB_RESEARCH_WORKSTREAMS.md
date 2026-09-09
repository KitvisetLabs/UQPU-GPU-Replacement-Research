# Parallel Fab Research Workstreams

The project is organized as parallel research workstreams that can be executed independently and integrated through shared requirement/cost schemas.

| Workstream | Scope | Integration output |
|---|---|---|
| FAB-LITHO | DUV/EUV/maskless/nanoimprint | feature-size, overlay, throughput, cost |
| FAB-DEPOSITION | CVD/PVD/ALD/epitaxy | films, uniformity, contamination, cost |
| FAB-ETCH | plasma/wet etch | selectivity, anisotropy, damage |
| FAB-DOPING | implantation/diffusion/anneal | junction/device requirements |
| FAB-METROLOGY | CD/overlay/defect inspection | yield feedback |
| FAB-CLEAN | wet/dry cleaning, contamination | purity/yield |
| FAB-PHOTONICS | Si/SiN/other photonic processes | loss/coupling/device yield |
| FAB-QUANTUM | modality-specific device processes | fidelity/coherence/yield |
| FAB-PACKAGING | chiplets/2.5D/3D/optical/cryo | system bandwidth/thermal/yield |
| FAB-MATERIALS | conventional + biomass-derived candidates | property/cost/TRL matrix |
| FAB-ECON | CAPEX/OPEX/throughput/yield | cost/device and cost/task |
| FAB-AUTOMATION | robotics/AI/process control | utilization/labor/yield impact |

## Integration meeting protocol

Each workstream reports:
- verified evidence;
- current model;
- interfaces/dependencies;
- bottlenecks;
- negative results;
- cost impact;
- next experiment.

The integration layer then asks whether combined changes improve the permanent UQCS objective: broad computing functional coverage with >=100x total cost/useful-task target and 100M× workload-specific moonshot.

Parallelism does not permit incompatible assumptions. Shared physical units, evidence levels and cost boundaries are mandatory.
