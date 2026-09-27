"""Cycle-001 Delta-02 instantiated analytic ledgers.

All examples are MODEL/ACCOUNTING fixtures. They exercise cross-lane contracts
without claiming real-QPU, device, material, factory, or economic performance.
"""
from __future__ import annotations
from dataclasses import dataclass
import math
from .cross_lane_contracts import UsefulOutputLedger, DeviceFactoryChain, DifferenceToTechnology

@dataclass(frozen=True)
class ResidualCostCase:
    baseline_cost: float
    residual_fraction: float
    accelerated_fraction_speedup: float
    def projected_cost(self):
        r=self.residual_fraction; s=self.accelerated_fraction_speedup
        return self.baseline_cost*(r+(1-r)/s)

def minimum_output_bits(distinct_accepted_outputs:int)->float:
    if distinct_accepted_outputs<1: raise ValueError("distinct outputs must be >=1")
    return math.log2(distinct_accepted_outputs)

def cycle001_fixtures():
    workload=UsefulOutputLedger(
        "CYCLE001-OBS-001","one accepted scalar observable",
        "absolute error <= preregistered epsilon",1024,0.25,1.0,8,0.1,0.0,0.0)
    chain=DeviceFactoryChain(
        "sensor/qubit readout SNR","predeclared minimum SNR",
        "loss/conductivity/interface property","deposition/anneal/process window",
        "film thickness/loss/readout SNR","good devices per processed unit","cost per good device")
    primitive=DifferenceToTechnology(
        "candidate measurable state-dependent response","blinded classifier above frozen null",
        "reproducible state preparation","controlled drive/input","measured retention/coherence window",
        "calibrated sensor/readout","accepted-output primitive","energy/time/error overhead",
        "returns to null under discriminating control")
    return workload,chain,primitive
