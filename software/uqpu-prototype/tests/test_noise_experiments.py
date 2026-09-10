import unittest
from uqpu.noise_experiments import independent_bitflip_distribution, sample_distribution

class ReadoutNoiseTests(unittest.TestCase):
    def test_zero_noise_identity_and_normalization(self):
        p=(0.1,0.2,0.3,0.4)
        self.assertEqual(independent_bitflip_distribution(p,2,0),p)
        for e in (0.01,0.1,0.5):
            q=independent_bitflip_distribution(p,2,e)
            self.assertAlmostEqual(sum(q),1.0,places=12)
            self.assertTrue(all(x>=0 for x in q))

    def test_single_qubit_channel(self):
        self.assertEqual(independent_bitflip_distribution((1.0,0.0),1,0.25),(0.75,0.25))
        q=independent_bitflip_distribution((1.0,0.0),1,0.5)
        self.assertEqual(q,(0.5,0.5))

    def test_sampling_reproducible(self):
        a=sample_distribution((0.2,0.8),1000,seed=7)
        self.assertEqual(a,sample_distribution((0.2,0.8),1000,seed=7))
        self.assertEqual(sum(a.values()),1000)

    def test_invalid_inputs(self):
        for e in (-0.1,0.51,float('nan')):
            with self.assertRaises(ValueError): independent_bitflip_distribution((0.5,0.5),1,e)
        with self.assertRaises(ValueError): independent_bitflip_distribution((0.5,0.4),1,0.1)
        with self.assertRaises(ValueError): sample_distribution((1.0,),True)

if __name__=="__main__": unittest.main()
