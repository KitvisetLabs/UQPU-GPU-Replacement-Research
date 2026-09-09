import unittest

from uqpu.cloud_economics import (
    CloudPricingKind, CloudPricingProfile, CloudWorkloadUsage,
    cloud_cost_per_useful_task, estimate_cloud_cost,
)
from uqpu.cloud_pricing_snapshot import official_pricing_snapshot_2026_09
from uqpu.cloud_vs_owned import (
    OwnedHardwareEconomics, OwnedWorkloadUsage, compare_cloud_vs_owned,
    owned_cost_per_useful_task,
)


class CloudEconomicsTests(unittest.TestCase):
    def test_aws_task_shot_formula(self):
        p = CloudPricingProfile("x","x",CloudPricingKind.PER_TASK_SHOT,per_task=.3,per_shot=.001)
        u = CloudWorkloadUsage(executions=2,shots_per_execution=100,useful_tasks=1)
        self.assertAlmostEqual(estimate_cloud_cost(p,u),0.8)

    def test_gate_shot_minimum(self):
        p = CloudPricingProfile("x","x",CloudPricingKind.PER_GATE_SHOT,per_one_qubit_gate_shot=.001,per_two_qubit_gate_shot=.002,minimum_program_price=10)
        u = CloudWorkloadUsage(executions=1,shots_per_execution=1,one_qubit_gates=1,two_qubit_gates=1)
        self.assertEqual(estimate_cloud_cost(p,u),10)

    def test_rigetti_time_increment_rounds_up(self):
        p = CloudPricingProfile("x","x",CloudPricingKind.PER_TIME_INCREMENT,time_increment_seconds=.01,per_time_increment=.02)
        u = CloudWorkloadUsage(runtime_seconds=.011)
        self.assertAlmostEqual(estimate_cloud_cost(p,u),.04)

    def test_owned_utilization_matters(self):
        u = OwnedWorkloadUsage(1000,1000)
        low = owned_cost_per_useful_task(OwnedHardwareEconomics(1_000_000,10_000_000,.1,1000),u)
        high = owned_cost_per_useful_task(OwnedHardwareEconomics(1_000_000,10_000_000,.9,1000),u)
        self.assertLess(high,low)

    def test_cloud_vs_owned_returns_route(self):
        p = CloudPricingProfile("x","x",CloudPricingKind.PER_SECOND,per_second=1)
        cu = CloudWorkloadUsage(runtime_seconds=100,useful_tasks=100)
        hw = OwnedHardwareEconomics(1000,1_000_000,.8,100)
        ou = OwnedWorkloadUsage(100,100)
        r = compare_cloud_vs_owned(p,cu,hw,ou)
        self.assertIn(r.cheaper_route,{"CLOUD","OWNED","TIE"})

    def test_snapshot_has_major_pricing_routes(self):
        ids={p.provider_id for p in official_pricing_snapshot_2026_09()}
        for x in {"ibm_quantum","aws_braket_rigetti_cepheus","azure_ionq_aria","azure_pasqal_fresnel","azure_rigetti_cepheus"}:
            self.assertIn(x,ids)


if __name__=="__main__":
    unittest.main()
