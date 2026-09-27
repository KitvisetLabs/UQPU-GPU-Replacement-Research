"""Cycle-001 Delta-06 experiment/resource ledgers."""
from dataclasses import dataclass

@dataclass(frozen=True)
class MatchedResourceLedger:
    case_id:str; accepted_output:str
    prep_seconds:float; execution_seconds:float; shots:int
    readout_seconds:float; postprocess_seconds:float
    energy_joules:float; cost:float
    evidence_class:str="RESOURCE_LEDGER_TEMPLATE"

    def total_seconds(self):
        return self.prep_seconds+self.execution_seconds+self.readout_seconds+self.postprocess_seconds

def validate_resource(x):
    e=[]
    if not x.case_id.strip():e.append("missing:case_id")
    if not x.accepted_output.strip():e.append("missing:accepted_output")
    for n in ("prep_seconds","execution_seconds","readout_seconds","postprocess_seconds","energy_joules","cost"):
        if getattr(x,n)<0:e.append("invalid:"+n)
    if x.shots<0:e.append("invalid:shots")
    return tuple(e)

@dataclass(frozen=True)
class CouponPreregistration:
    case_id:str; feedstock:str; incumbent:str; frequency_band:str
    thickness_rule:str; primary_metric:str; secondary_metrics:tuple[str,...]
    process_fields:tuple[str,...]
    evidence_class:str="PREREGISTRATION_NO_MEASUREMENTS"

def pangola_emi_coupon():
    return CouponPreregistration(
      "DMF-BIOCARBON-EMI-001","Pangola-derived carbon, lot provenance required",
      "named commercial carbon/polymer shielding incumbent","PRECOMMIT_BEFORE_MEASUREMENT",
      "compare at matched thickness and report areal density",
      "shielding effectiveness versus frequency",
      ("conductivity","areal density","thermal stability","mechanical integrity","yield","energy","chemical use","cost"),
      ("moisture","ash","carbonization_temperature","residence_time","atmosphere","purification","activation_or_graphitization","binder_fraction"))

def ai_cost_canonical_rows():
    # USD ambition proxy from project canon; target is 50,000 THB converted at frozen 33.045 THB/USD.
    target_usd=50_000/33.045
    baselines=(10_000_000_000_000,100_000_000_000_000)
    residuals=(1e-2,1e-4,1e-6,1e-8,1e-10,1e-12)
    return tuple((b,r,b*r,r<=target_usd/b) for b in baselines for r in residuals)
