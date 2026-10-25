import random
import unittest

from uqpu.thermodynamic_memory_order import (
    adjacent_lag_cmi_profile_bits,
    conditional_mutual_information_bits,
)


def _first_order_binary_chain(seed=1729, length=30000):
    rng = random.Random(seed)
    values = [rng.randrange(2)]
    for _ in range(1, length):
        previous = values[-1]
        values.append(previous if rng.random() < 0.9 else 1 - previous)
    return values


def _second_order_xor_chain(seed=2718, length=30000, flip_probability=0.03):
    rng = random.Random(seed)
    values = [rng.randrange(2), rng.randrange(2)]
    for _ in range(2, length):
        prediction = values[-1] ^ values[-2]
        values.append(prediction ^ int(rng.random() < flip_probability))
    return values


class AdjacentLagCMITests(unittest.TestCase):
    def test_first_order_chain_loses_second_lag_information_after_conditioning(self):
        profile = adjacent_lag_cmi_profile_bits(_first_order_binary_chain(), 2)
        self.assertGreater(profile[0], 0.45)
        self.assertLess(profile[1], 0.01)
        self.assertLess(profile[2], 0.01)

    def test_second_order_xor_chain_exposes_second_order_memory(self):
        profile = adjacent_lag_cmi_profile_bits(_second_order_xor_chain(), 2)
        self.assertGreater(profile[1], 0.7)
        self.assertLess(profile[2], 0.01)

    def test_replay_is_deterministic(self):
        sequence = _second_order_xor_chain(length=3000)
        self.assertEqual(
            adjacent_lag_cmi_profile_bits(sequence, 2),
            adjacent_lag_cmi_profile_bits(sequence, 2),
        )

    def test_invalid_orders_and_short_sequences_fail_closed(self):
        for order in (-1, True, 1.5):
            with self.assertRaises(ValueError):
                conditional_mutual_information_bits([0, 1, 0, 1], order)
        with self.assertRaises(ValueError):
            adjacent_lag_cmi_profile_bits([0, 1, 0], 2)
        with self.assertRaises(ValueError):
            conditional_mutual_information_bits([[0], [1], [0]], 0)


if __name__ == "__main__":
    unittest.main()
