import copy
import importlib.util
import json
import unittest

from uqpu.er6_qsvt_target_snapshot_identity import (
    PERSISTED_CERTIFICATE,
    SDK_REQUIREMENTS,
    build_target_identity,
    reproduce_target_identity,
    validate_identity,
)


class _Operation:
    def __init__(self, name, num_qubits=1):
        self.name = name
        self.num_qubits = num_qubits


class _VariableOperation:
    @property
    def name(self):
        raise AssertionError("class-level property must not be read")

    @property
    def num_qubits(self):
        raise AssertionError("class-level property must not be read")


class _Target:
    operation_names = {"rz", "cx", "x"}

    def __init__(self, reverse=False):
        rows = [
            (_Operation("rz"), (0,)),
            (_Operation("cx", 2), (0, 1)),
            (_Operation("x"), (1,)),
            (_Operation("delay"), None),
            (_VariableOperation, None),
        ]
        self.instructions = list(reversed(rows)) if reverse else rows


class _Coupling:
    def __init__(self, reverse=False):
        self.reverse = reverse

    def get_edges(self):
        rows = [(0, 1), (1, 0)]
        return list(reversed(rows)) if self.reverse else rows


class DummyBackend:
    name = "saved_dummy"
    num_qubits = 2

    def __init__(self, reverse=False):
        self.target = _Target(reverse)
        self.coupling_map = _Coupling(reverse)


class TargetSnapshotIdentityTests(unittest.TestCase):
    def test_identity_is_order_stable_and_valid(self):
        left = build_target_identity(DummyBackend(False), SDK_REQUIREMENTS)
        right = build_target_identity(DummyBackend(True), SDK_REQUIREMENTS)
        self.assertEqual(left, right)
        self.assertEqual(validate_identity(left), [])
        signatures = left["target"]["instruction_signature_counts"]
        self.assertIn(
            {
                "operation": f"class:{_VariableOperation.__module__}.{_VariableOperation.__qualname__}",
                "arity": "variable",
                "instances": 1,
            },
            signatures,
        )

    def test_mutations_fail_closed(self):
        identity = build_target_identity(DummyBackend(), SDK_REQUIREMENTS)
        changed = copy.deepcopy(identity)
        changed["target"]["num_qubits"] = 3
        self.assertIn("target_identity_sha256", validate_identity(changed))

        changed = copy.deepcopy(identity)
        changed["authorization"]["provider_jobs"] = 1
        self.assertIn("authorization", validate_identity(changed))

        changed = copy.deepcopy(identity)
        changed["environment"]["packages"]["qiskit"] = "unbounded"
        self.assertIn("environment.packages", validate_identity(changed))


@unittest.skipUnless(importlib.util.find_spec("qiskit_ibm_runtime"), "optional saved-target SDK")
class PinnedTargetSnapshotIdentityTests(unittest.TestCase):
    def test_pinned_fake_backend_identity(self):
        identity = reproduce_target_identity()
        self.assertEqual(validate_identity(identity), [])
        self.assertEqual(identity["target"]["class"], "FakeKingston")
        self.assertEqual(identity["authorization"]["provider_jobs"], 0)

    def test_persisted_hosted_identity_matches_reproduction(self):
        persisted = json.loads(PERSISTED_CERTIFICATE.read_text(encoding="utf-8"))
        self.assertEqual(validate_identity(persisted), [])
        provenance = persisted.pop("provenance")
        self.assertEqual(
            provenance["source_commit"],
            "c63ee9d5251e23f50b210ee9d25333b91e63c80e",
        )
        self.assertEqual(provenance["workflow_job_id"], 117468829435)
        self.assertEqual(persisted, reproduce_target_identity())


if __name__ == "__main__":
    unittest.main()
