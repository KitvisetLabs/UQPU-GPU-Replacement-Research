import unittest
from uqpu.ir import Operation, OperationKind, ResultContract, Workload, WorkloadDomain


class IRTests(unittest.TestCase):
    def test_validation(self):
        w = Workload(
            name="x",
            domain=WorkloadDomain.HPC,
            operations=[Operation(OperationKind.SEARCH)],
            contract=ResultContract.BOUNDED_ERROR,
        )
        w.validate()

    def test_rejects_negative_io(self):
        w = Workload(
            name="x",
            domain=WorkloadDomain.HPC,
            operations=[Operation(OperationKind.SEARCH)],
            contract=ResultContract.BOUNDED_ERROR,
            input_bytes=-1,
        )
        with self.assertRaises(ValueError):
            w.validate()
