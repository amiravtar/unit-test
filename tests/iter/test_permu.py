import unittest
from iter import PermutationsAndCombinations


class TestPermutationsAndCombinations(unittest.TestCase):
    def setUp(self):
        self.pc = PermutationsAndCombinations()
        self.items = [1, 2, 3]

    def test_get_permutations(self):
        permutations = self.pc.get_permutations(self.items)
        self.assertEqual(len(permutations), 6)
        self.assertIn((1, 2, 3), permutations)
        self.assertIn((1, 3, 2), permutations)
        self.assertIn((2, 1, 3), permutations)
        self.assertIn((2, 3, 1), permutations)
        self.assertIn((3, 1, 2), permutations)
        self.assertIn((3, 2, 1), permutations)

    def test_get_combinations(self):
        combinations = self.pc.get_combinations(self.items, 2)
        self.assertEqual(len(combinations), 3)
        self.assertIn((1, 2), combinations)
        self.assertIn((1, 3), combinations)
        self.assertIn((2, 3), combinations)


if __name__ == "__main__":
    unittest.main()
