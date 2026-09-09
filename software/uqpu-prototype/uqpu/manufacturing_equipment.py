from __future__ import annotations
from dataclasses import dataclass
from enum import Enum


class EquipmentClass(str, Enum):
    LITHOGRAPHY = "LITHOGRAPHY"
    DEPOSITION = "DEPOSITION"
    ETCH = "ETCH"
    DOPING = "DOPING"
    CLEAN = "CLEAN"
    METROLOGY = "METROLOGY"
    WAFER_HANDLING = "WAFER_HANDLING"
    CHARACTERIZATION = "CHARACTERIZATION"
    BONDING_PACKAGING = "BONDING_PACKAGING"
    PROCESS_CONTROL = "PROCESS_CONTROL"


@dataclass(frozen=True)
class ManufacturingEquipmentRequirement:
    equipment_class: EquipmentClass
    function: str
    target_metric: str
    target_value: str
    evidence_level: str = "FABRICATION_PROPOSAL"
    software_control_required: bool = True


def baseline_quantum_chip_toolchain() -> tuple[ManufacturingEquipmentRequirement, ...]:
    return (
        ManufacturingEquipmentRequirement(EquipmentClass.LITHOGRAPHY,"pattern critical device features","resolution/overlay","process dependent"),
        ManufacturingEquipmentRequirement(EquipmentClass.DEPOSITION,"deposit superconducting/semiconductor/dielectric/photonic films","thickness/uniformity/purity","device dependent"),
        ManufacturingEquipmentRequirement(EquipmentClass.ETCH,"transfer device pattern","selectivity/profile/damage","device dependent"),
        ManufacturingEquipmentRequirement(EquipmentClass.CLEAN,"remove residues/particles","surface contamination","device dependent"),
        ManufacturingEquipmentRequirement(EquipmentClass.METROLOGY,"measure dimensions/defects","CD/overlay/defect sensitivity","process dependent"),
        ManufacturingEquipmentRequirement(EquipmentClass.CHARACTERIZATION,"electrical/optical/cryogenic validation","fidelity/loss/noise","device dependent"),
        ManufacturingEquipmentRequirement(EquipmentClass.BONDING_PACKAGING,"assemble chiplets/modules","alignment/yield/interconnect loss","architecture dependent"),
        ManufacturingEquipmentRequirement(EquipmentClass.PROCESS_CONTROL,"close manufacturing feedback loop","SPC/APC/traceability","factory dependent"),
    )
