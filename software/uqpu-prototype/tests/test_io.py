import unittest
from uqpu.io import workload_from_dict
from uqpu.ir import OperationKind, ResultContract


class IOTests(unittest.TestCase):
    def test_parse(self):
        w = workload_from_dict({
            "name": "x", "domain": "data", "contract": "probabilistic",
            "operations": [{"kind": "search"}], "input_bytes": 8, "output_bytes": 1
        })
        self.assertEqual(w.contract, ResultContract.PROBABILISTIC)
        self.assertEqual(w.operations[0].kind, OperationKind.SEARCH)
