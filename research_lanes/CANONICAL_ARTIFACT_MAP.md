# Canonical Artifact Ownership Map

This map assigns existing repository areas to a **primary lane owner** without forcing an unsafe immediate file move. Cross-lane consumers should use `integration/LANE_INTERFACE_CONTRACT.md`.

## Lane A — Programming / workloads / compiler / runtime
Primary ownership includes compiler/runtime/workload/QAOA programming artifacts under `software/uqpu-prototype/uqpu/`, workload contracts, compiler/runtime documentation and quantum-programming experiments. Provider-specific submission code remains B-owned even when physically located in the same Python package during migration.

## Lane B — Cloud / QPU / provider integration
Primary ownership includes provider registry/adapters/CLI, provider hardware snapshots, cloud compatibility, target calibration/runtime integration, provider-specific simulation/execution evidence and cloud adapter documentation.

## Lane C — State / memory / storage / data movement
Primary ownership includes state-service semantics, state/I/O accounting, memory/materialization models, transfer/reconstruction assumptions and RAM/VRAM/HBM/storage functional-equivalence work.

## Lane D — Device / chip / fabrication / packaging
Primary ownership includes hardware/device requirements, inverse hardware models, quantum/photonic/semiconductor architecture, fabrication requirements, package architecture and device-manufacturability research.

## Lane E — Materials / energy / cooling / infrastructure
Primary ownership includes biomass functional-substitution studies, material qualification requirements, energy/cooling/facility models and infrastructure research.

## Lane F — Economics / benchmark / evidence / integration
Primary ownership includes benchmark contracts/artifacts, classical baselines, reference certificates, cloud/owned economics, accepted-solution economics, evidence gates, mission scoring, economic sensitivity and integrated scorekeeping.

## Lane G — Manufacturing equipment / factory software
Primary ownership includes fabrication-route selection, fab flow/cost/yield, lithography/manufacturing-equipment matrices, metrology/process-control/EDA/TCAD/automation/packaging/test equipment research and D↔G co-design artifacts.

## Lane H — Strategy / finance / future industries
Primary ownership includes `docs/KANUSANAN_PONGPANNA_MODEL.md`, `STRATEGIC_PLAN_REFERENCES.md`, Lane-H articles, financial/stage-gate roadmaps, AI-agent/One-Person-Business strategy and future-industry planning.

## Shared / integration-owned coordination artifacts
`integration/`, project invariants/charter, high-level goals, cross-lane scoreboard, decisions, worklog and research-gap backlog coordinate the whole system. They should reference lane owners rather than duplicate lane source artifacts.

## Migration policy
When an existing artifact is physically moved into a lane folder, the same change must update every import, link, workflow, test and reproducibility reference that depends on the old path. If compatibility cannot be guaranteed, keep the canonical file in place and link to it from the lane folder until a safe migration is available.
