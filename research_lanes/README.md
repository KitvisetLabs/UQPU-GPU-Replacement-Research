# Eight Research Lanes — Repository Architecture

This directory is the canonical lane-oriented workspace for the project.

## Permanent lanes
- `A_quantum_programming_runtime` — Priority #1 software/workloads/compiler/runtime
- `B_cloud_qpu_provider_integration` — cloud QPU/provider integration
- `C_state_memory_storage_data_movement` — volatile memory and state services: system/host RAM (including DDR/LPDDR/RDIMM/MRDIMM-class DRAM), accelerator-local VRAM/HBM/GDDR, on-chip SRAM/cache, storage/state/data movement
- `D_device_chip_fabrication_packaging` — device/chip/process/fabrication/packaging
- `E_materials_energy_cooling_infrastructure` — biomass/materials/energy/cooling/infrastructure
- `F_economics_benchmarks_evidence_integration` — economics/benchmark/evidence/integration
- `G_manufacturing_equipment_factory_software` — manufacturing equipment/software/factory systems
- `H_strategy_finance_future_industries` — strategy/finance/future industries

## Memory-taxonomy rule
Lane C uses **role-based memory taxonomy** rather than treating `DRAM` as a separate peer subsystem. DRAM is a technology family that can implement multiple volatile-memory roles: system DDR/LPDDR/RDIMM/MRDIMM and accelerator-local HBM/GDDR are all DRAM-derived or DRAM-class technologies, while SRAM/cache is a distinct volatile-memory class. Replacement/economic claims must therefore name the memory role and the physical technology being compared.

## Folder-depth rule
Future special projects may create additional subfolders inside the appropriate lane. A repository path must not exceed **16 directory levels from repository root**. Prefer shallower paths whenever possible.

## Ownership rule
Each substantive artifact has one **primary owning lane**. Cross-lane work should not be duplicated merely to appear in several folders. The owning artifact declares upstream inputs and downstream consumers.

## Integration rule
The research direction is shared: maximize scientifically useful integration across all A-H lanes. Every meaningful work package asks what it consumes from other lanes, what measurable outputs it returns, how it changes end-to-end feasibility/cost, and what evidence level supports it.

Shared cross-lane contracts and integrated programs live under `integration/`.

## Migration rule
Existing root-level, `docs/`, `software/`, `benchmarks/`, `spec/` and other canonical paths remain valid while artifacts are migrated incrementally. Do not break imports, links, reproducibility hashes or CI merely to change folder layout.
