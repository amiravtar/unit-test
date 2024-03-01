from itertools import permutations, combinations


class PermutationsAndCombinations:
    @staticmethod
    def get_permutations(items, r=None):
        return list(permutations(items, r))

    @staticmethod
    def get_combinations(items, r):
        return list(combinations(items, r))

