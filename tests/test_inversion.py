"""Tests for inversion counting algorithms."""

import pytest
from algorithms.inversion import inversions_fast, inversion_slow


def test_inversion_empty():
    """Test inversion counting with empty array."""
    arr = []
    assert inversions_fast(arr) == 0
    assert inversion_slow(arr) == 0


def test_inversion_single():
    """Test inversion counting with single element."""
    arr = [42]
    assert inversions_fast(arr) == 0
    assert inversion_slow(arr) == 0


def test_inversion_two_elements():
    """Test inversion counting with two elements."""
    # No inversions
    arr = [1, 2]
    assert inversions_fast(arr) == 0
    assert inversion_slow(arr) == 0

    # One inversion
    arr = [2, 1]
    assert inversions_fast(arr) == 1
    assert inversion_slow(arr) == 1


def test_inversion_sorted():
    """Test inversion counting with sorted array."""
    arr = [1, 2, 3, 4, 5]
    assert inversions_fast(arr) == 0
    assert inversion_slow(arr) == 0


def test_inversion_reverse_sorted():
    """Test inversion counting with reverse sorted array."""
    arr = [5, 4, 3, 2, 1]
    expected = 10  # 4+3+2+1 = 10 inversions
    assert inversions_fast(arr) == expected
    assert inversion_slow(arr) == expected


def test_inversion_duplicates():
    """Test inversion counting with duplicate elements."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    fast_result = inversions_fast(arr)
    slow_result = inversion_slow(arr)
    assert fast_result == slow_result


def test_inversion_random_data():
    """Test inversion counting with random data."""
    test_cases = [
        [1, 8, 9, 4, 100, 48, 999, 33, 222, 22, 7, 5],
        [64, 34, 25, 12, 22, 11, 90],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    ]

    for arr in test_cases:
        fast_result = inversions_fast(arr)
        slow_result = inversion_slow(arr)
        assert fast_result == slow_result, f"Failed for array: {arr}"


@pytest.mark.parametrize("arr", [
    [1, 2, 3, 4, 5],  # Sorted
    [5, 4, 3, 2, 1],  # Reverse sorted
    [1, 3, 2, 4, 5],  # One inversion
    [2, 1, 4, 3, 5],  # Two inversions
    [1, 1, 1, 1, 1],  # All same
])
def test_inversion_edge_cases(arr):
    """Test inversion counting with various edge cases."""
    fast_result = inversions_fast(arr)
    slow_result = inversion_slow(arr)
    assert fast_result == slow_result


def test_inversion_large_array():
    """Test inversion counting with larger array."""
    arr = list(range(100, 0, -1))  # 100 to 1
    expected = 4950  # Sum of 99+98+...+1
    assert inversions_fast(arr) == expected
    assert inversion_slow(arr) == expected


def test_inversion_negative_numbers():
    """Test inversion counting with negative numbers."""
    arr = [3, -1, 4, -2, 5, -3]
    fast_result = inversions_fast(arr)
    slow_result = inversion_slow(arr)
    assert fast_result == slow_result


def test_inversion_float_numbers():
    """Test inversion counting with float numbers."""
    arr = [3.14, 1.41, 2.71, 0.58, 1.73]
    fast_result = inversions_fast(arr)
    slow_result = inversion_slow(arr)
    assert fast_result == slow_result
