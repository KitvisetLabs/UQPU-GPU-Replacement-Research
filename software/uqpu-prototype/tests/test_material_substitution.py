import unittest
from uqpu.material_substitution import MaterialCandidate, Strategy, allowed_strategy_for_elemental_replacement

class MaterialSubstitutionTests(unittest.TestCase):
    def test_cost_advantage(self):
        c=MaterialCandidate("graphite","electrode","pangola grass","hard carbon",Strategy.FUNCTIONAL_SUBSTITUTION,10,0.1,1.0)
        self.assertEqual(c.cost_advantage,100)
        self.assertTrue(c.reaches_100x)

    def test_invalid_reduction(self):
        with self.assertRaises(ValueError):
            MaterialCandidate("Cu","conduction","bagasse","carbon composite",Strategy.HYBRID,1,1,1.1).validate()

    def test_elemental_replacement_uses_valid_strategies(self):
        s=allowed_strategy_for_elemental_replacement("Au")
        self.assertIn(Strategy.MINIMIZATION,s)
        self.assertIn(Strategy.RECOVERY,s)
        self.assertNotIn("transmutation", [x.value for x in s])

if __name__=="__main__": unittest.main()
