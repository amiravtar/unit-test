from iter import PermutationsAndCombinations

def test_get_permutations():
    pc = PermutationsAndCombinations()
    items = [1, 2, 3]
    permutations = pc.get_permutations(items)
    assert len(permutations) == 6
    assert (1, 2, 3) in permutations
    assert (1, 3, 2) in permutations
    assert (2, 1, 3) in permutations
    assert (2, 3, 1) in permutations
    assert (3, 1, 2) in permutations
    assert (3, 2, 1) in permutations

def test_get_combinations():
    pc = PermutationsAndCombinations()
    items = [1, 2, 3]
    combinations = pc.get_combinations(items, 2)
    assert len(combinations) == 3
    assert (1, 2) in combinations
    assert (1, 3) in combinations
    assert (2, 3) in combinations
