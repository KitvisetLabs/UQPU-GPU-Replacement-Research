import unittest
from uqpu.moonshot_contract import ReplacementContract, required_uqpu_cost

class MoonshotContractTests(unittest.TestCase):
 def test_math_does_not_promote_unmeasured_claim(self):
  c=ReplacementContract("gpu",100_000_000,1.0,1.0,True,False)
  self.assertEqual(c.financial_advantage,100_000_000)
  self.assertFalse(c.moonshot_status()["demonstrated"])
 def test_requires_equivalent_output(self):
  c=ReplacementContract("cpu",100_000_000,1.0,0.5,False,True)
  self.assertFalse(c.moonshot_status()["demonstrated"])
 def test_npu_is_permanent_executable_scope(self):
  c=ReplacementContract("npu",100_000_000,1.0,1.0,True,False)
  self.assertEqual(c.financial_advantage,100_000_000)
  self.assertFalse(c.moonshot_status()["demonstrated"])
 def test_full_contract_can_pass(self):
  c=ReplacementContract("storage",100_000_000,1.0,1.0,True,True)
  self.assertTrue(c.moonshot_status()["demonstrated"])
 def test_required_cost(self):
  self.assertEqual(required_uqpu_cost(100_000_000),1.0)
 def test_invalid(self):
  with self.assertRaises(ValueError): ReplacementContract("qubit",1,1,1,True,True)
  with self.assertRaises(ValueError): ReplacementContract("ram",0,1,1,True,True)
if __name__=="__main__": unittest.main()
