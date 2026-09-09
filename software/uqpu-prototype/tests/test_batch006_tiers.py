import unittest
from uqpu.benchmark_tiers import representative_tiers

class Batch006Tests(unittest.TestCase):
    def test_tiers_increase(self):
        tiers=representative_tiers()
        self.assertEqual([t.name for t in tiers],["small","medium","large"])
        self.assertTrue(tiers[0].variable_count < tiers[1].variable_count < tiers[2].variable_count)
    def test_contract_and_instance_match(self):
        for tier in representative_tiers():
            self.assertEqual(len(tier.instance().variables),tier.contract().variable_count)
    def test_contract_ids_differ(self):
        ids=[t.contract().contract_id for t in representative_tiers()]
        self.assertEqual(len(ids),len(set(ids)))
if __name__=="__main__": unittest.main()
