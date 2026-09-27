import json
from pathlib import Path
import unittest

from uqpu.benchmark_contract import OptimizationBenchmarkContract
from uqpu.optimization_baseline import exact_qubo_baseline
from uqpu.qaoa import qubo_to_ising
from uqpu.qaoa_objective_selection import compare_p1_grid_objectives
from uqpu.scalable_qubo import seeded_erdos_renyi_maxcut


ROOT = Path(__file__).resolve().parents[3]
FREEZE_PATH = ROOT / "benchmarks/experiments/cycle002-delta01-er6-frozen-contract.json"
B019_RESULT_PATH = ROOT / "benchmarks/results/batch019-qaoa-cvar-target-comparison.json"
B020_PATH = ROOT / "benchmarks/experiments/batch020-er6-mean-vs-cvar-real-qpu-protocol.json"


class Cycle002Er6FreezeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.freeze = json.loads(FREEZE_PATH.read_text(encoding="utf-8"))
        cls.b019 = json.loads(B019_RESULT_PATH.read_text(encoding="utf-8"))
        cls.b020 = json.loads(B020_PATH.read_text(encoding="utf-8"))
        cls.instance = seeded_erdos_renyi_maxcut(6, 0.5, 42)
        cls.ising = qubo_to_ising(cls.instance)

    def test_seeded_er6_is_frozen_by_full_content_hash(self):
        freeze = self.freeze
        self.assertEqual(freeze["fixture"]["case_id"], "er6")
        self.assertEqual(freeze["fixture"]["generator"], {
            "function": "seeded_erdos_renyi_maxcut",
            "node_count": 6,
            "edge_probability": 0.5,
            "seed": 42,
        })
        self.assertEqual(self.ising.instance_sha256, freeze["fixture"]["qubo_to_ising_sha256"])
        self.assertEqual(
            [[u, v] for (u, v), w in sorted(self.instance.quadratic.items()) if w == 2.0],
            freeze["fixture"]["edges"],
        )

    def test_existing_contract_id_and_exact_output_semantics_are_unchanged(self):
        contract = OptimizationBenchmarkContract(
            "er6", "batch012-verification-fixture", 42, 6, required_relative_gap=0.0
        )
        self.assertEqual(contract.contract_id, "8efaa94bb3306d25")
        self.assertEqual(contract.contract_id, self.freeze["output_contract"]["contract_id"])
        self.assertTrue(contract.accepts(-7.0, -7.0))
        self.assertFalse(contract.accepts(-6.999, -7.0))
        self.assertEqual(self.freeze["output_contract"]["accepted_objective"], -7.0)
        self.assertEqual(self.freeze["output_contract"]["required_relative_gap"], 0.0)
        self.assertIn("not the Cycle-001 scalar-energy epsilon/confidence-0.95 template", self.freeze["output_contract"]["semantic_note"])

    def test_all_64_qubo_and_ising_energies_match_and_reference_is_exact(self):
        for basis_index in range(1 << 6):
            self.assertAlmostEqual(
                self.instance.energy(self.ising.assignment(basis_index)),
                self.ising.energy(basis_index),
                places=12,
            )
        baseline = exact_qubo_baseline(self.instance, max_variables=12)
        self.assertEqual(baseline.objective, -7.0)
        self.assertEqual(baseline.states_evaluated, 64)
        accepted = [
            basis_index
            for basis_index in range(1 << 6)
            if self.instance.energy(self.ising.assignment(basis_index)) == -7.0
        ]
        self.assertEqual(accepted, [11, 14, 49, 52])
        encoded = [
            "".join(str(self.ising.assignment(i)[q]) for q in reversed(range(6)))
            for i in accepted
        ]
        self.assertEqual(encoded, [row["bits_v5_to_v0"] for row in self.freeze["output_contract"]["accepted_outputs"]])

    def test_frozen_mean_and_cvar_candidates_reproduce_batch019_ideal_results(self):
        sweep = compare_p1_grid_objectives(
            self.instance,
            alphas=(0.5,),
            gamma_steps=24,
            beta_steps=24,
            contract_id=self.freeze["output_contract"]["contract_id"],
        )
        self.assertEqual(sweep.evaluations, 576)
        self.assertEqual(sweep.exact_optimum, -7.0)
        result_by_objective = {row.objective: row for row in sweep.selections}
        b019_rows = {row["selection"]: row for row in self.b019["results"]}
        for name in ("mean_energy", "cvar_alpha_0.5"):
            actual = result_by_objective["mean_energy" if name == "mean_energy" else "cvar_minimization"]
            frozen = b019_rows[name]
            self.assertAlmostEqual(actual.gamma, frozen["gamma"], places=12)
            self.assertAlmostEqual(actual.beta, frozen["beta"], places=12)
            self.assertAlmostEqual(actual.expected_energy, frozen["ideal_expected_energy"], places=9)
            self.assertAlmostEqual(actual.optimum_probability, frozen["ideal_optimum_probability"], places=9)
        self.assertEqual(self.b019["shared_parameter_grid_evaluations"], sweep.evaluations)
        self.assertEqual(self.b019["paid_job_submitted"], False)
        self.assertEqual(self.b019["real_qpu_executed"], False)

    def test_provider_packet_keeps_the_frozen_equal_shot_gate_and_authorization(self):
        b019_candidates = {row["selection"]: row for row in self.b019["results"]}
        protocol_candidates = {row["id"]: row for row in self.b020["frozen_candidates"]}
        self.assertEqual(protocol_candidates["mean_energy_p1"]["gamma"], b019_candidates["mean_energy"]["gamma"])
        self.assertEqual(protocol_candidates["mean_energy_p1"]["beta"], b019_candidates["mean_energy"]["beta"])
        self.assertEqual(protocol_candidates["cvar_alpha_0.5_p1"]["gamma"], b019_candidates["cvar_alpha_0.5"]["gamma"])
        self.assertEqual(protocol_candidates["cvar_alpha_0.5_p1"]["beta"], b019_candidates["cvar_alpha_0.5"]["beta"])
        self.assertEqual(self.b020["execution_plan"]["initial_shots_per_candidate"], 8192)
        self.assertTrue(self.b020["explicit_budget_authorization_required"])
        self.assertFalse(self.b020["paid_job_submitted"])
        self.assertFalse(self.b020["real_qpu_executed"])


if __name__ == "__main__":
    unittest.main()
