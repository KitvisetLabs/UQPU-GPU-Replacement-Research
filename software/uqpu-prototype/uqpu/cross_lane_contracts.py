"""Cycle-001 cross-lane integration contracts.

These dataclasses connect research lanes without copying evidence status across
interfaces. They are accounting/governance infrastructure, not hardware results.
"""
from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class UsefulOutputLedger:
    task_id: str
    accepted_output: str
    quality_threshold: str
    input_bytes: int
    state_prep_seconds: float
    execution_seconds: float
    readout_bytes: int
    classical_postprocess_seconds: float
    billed_cost: float
    energy_joules: float
    evidence_class: str = "ACCOUNTING_CONTRACT_ONLY"

@dataclass(frozen=True)
class DeviceFactoryChain:
    device_observable: str
    required_value: str
    material_property: str
    process_variable: str
    metrology_observable: str
    yield_metric: str
    cost_metric: str
    evidence_class: str = "REQUIREMENT_CHAIN_ONLY"

@dataclass(frozen=True)
class DifferenceToTechnology:
    candidate_difference: str
    distinguishability_test: str
    preparation: str
    control: str
    retention: str
    readout: str
    useful_function: str
    scaling_resource: str
    falsifier: str
    evidence_class: str = "HYPOTHESIS_CONTRACT_ONLY"

def validate_useful_output(x: UsefulOutputLedger)->tuple[str,...]:
    e=[]
    for n in ("task_id","accepted_output","quality_threshold"):
        if not getattr(x,n).strip(): e.append(f"missing:{n}")
    for n in ("input_bytes","readout_bytes"):
        if getattr(x,n)<0: e.append(f"invalid:{n}")
    for n in ("state_prep_seconds","execution_seconds","classical_postprocess_seconds","billed_cost","energy_joules"):
        if getattr(x,n)<0: e.append(f"invalid:{n}")
    return tuple(e)

def validate_device_factory(x: DeviceFactoryChain)->tuple[str,...]:
    return tuple(f"missing:{n}" for n in x.__dataclass_fields__ if n!="evidence_class" and not getattr(x,n).strip())

def validate_difference(x: DifferenceToTechnology)->tuple[str,...]:
    return tuple(f"missing:{n}" for n in x.__dataclass_fields__ if n!="evidence_class" and not getattr(x,n).strip())
