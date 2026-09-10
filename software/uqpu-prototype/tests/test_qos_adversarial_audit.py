import unittest

from uqpu.qos_adversarial_audit import (
    D16RepeatedPairWitness,
    d16_repeated_pair_certificate,
    printed_d16_sample_threshold,
    rational_envelope_checks,
    repeated_pair_coherence,
    repeated_pair_diamond_error,
    smallest_even_integer_at_least,
)


class QOSAdversarialAuditTests(unittest.TestCase):
    def test_printed_threshold_is_met_by_752_samples(self):
        w = D16RepeatedPairWitness()
        threshold = printed_d16_sample_threshold(
            t=w.t,
            p_max=w.p_max,
            alphabet_size=w.alphabet_size,
            repetition_number=w.repetition_number,
            epsilon=w.epsilon,
        )
        self.assertAlmostEqual(threshold, 750.2148110962436, places=10)
        self.assertEqual(smallest_even_integer_at_least(threshold), 752)

    def test_repeated_pair_channel_misses_stated_error_target(self):
        w = D16RepeatedPairWitness()
        c = repeated_pair_coherence(t=w.t, samples=w.samples)
        err = repeated_pair_diamond_error(t=w.t, samples=w.samples)
        self.assertAlmostEqual(c, 0.9488539991849398, places=12)
        self.assertAlmostEqual(err, 0.051146000815060155, places=12)
        self.assertGreater(err, w.epsilon)

    def test_rational_envelopes_all_hold(self):
        self.assertTrue(all(rational_envelope_checks().values()))

    def test_certificate_is_scoped_and_non_promotional(self):
        cert = d16_repeated_pair_certificate()
        self.assertTrue(cert["threshold_condition_satisfied"])
        self.assertTrue(cert["stated_error_target_violated"])
        self.assertFalse(cert["qos_globally_invalidated"])
        self.assertFalse(cert["quantum_advantage_demonstrated"])
        self.assertFalse(cert["uqpu_advantage_demonstrated"])

    def test_even_sample_contract(self):
        with self.assertRaises(ValueError):
            repeated_pair_coherence(t=1.0, samples=751)


if __name__ == "__main__":
    unittest.main()
