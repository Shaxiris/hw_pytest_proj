from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([1, 2, 3, 4], -1, "test") == 4
    assert arrs.get([1, 2, 3, 4], 10, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4], 0, 10) == [1, 2, 3, 4]
    assert arrs.my_slice([], 0, 10) == []


def test_swap():
    assert arrs.swap([1, 2, 3], 0, 1) == [2, 1, 3]
    assert arrs.swap([], 0, 1) == []
    assert arrs.swap([1, 2, 3], -1, 2) == [1, 2, 3]
    assert arrs.swap([1, 2, 3], 0, 5) == [1, 2, 3]


def test_remove_duplicates():
    assert arrs.remove_duplicates([1, 2, 3, 2, 4, 4]) == [1, 2, 3, 4]
    assert arrs.remove_duplicates([1, 1, 1, 1, 1]) == [1]
    assert arrs.remove_duplicates([]) == []


def test_concatenate():
    assert arrs.concatenate([1, 2], [3, 4]) == [1, 2, 3, 4]
    assert arrs.concatenate([], []) == []
    assert arrs.concatenate([1], []) == [1]
    assert arrs.concatenate([], [1]) == [1]