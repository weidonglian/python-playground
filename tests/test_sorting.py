import random
import pytest
from python_playground.algorithms.sorting import merge_sort, quick_sort, partition, QsPivot


# Simple Go-style tests (no classes needed)
def test_merge_sort_basic():
    """Test merge sort with basic input."""
    arr = [1, 4, 8, 95, 20, 400, 83, 44, 0, 11, 4444, 3]
    expected = sorted(arr.copy())
    merge_sort(arr)
    assert arr == expected


def test_merge_sort_empty():
    """Test merge sort with empty array."""
    arr = []
    merge_sort(arr)
    assert arr == []


def test_merge_sort_single():
    """Test merge sort with single element."""
    arr = [42]
    merge_sort(arr)
    assert arr == [42]


def test_merge_sort_already_sorted():
    """Test with already sorted array."""
    arr = [1, 2, 3, 4, 5]
    merge_sort(arr)
    assert arr == [1, 2, 3, 4, 5]


def test_merge_sort_reverse_sorted():
    """Test with reverse sorted array."""
    arr = [5, 4, 3, 2, 1]
    merge_sort(arr)
    assert arr == [1, 2, 3, 4, 5]


def test_merge_sort_duplicates():
    """Test with duplicate elements."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    expected = sorted(arr.copy())
    merge_sort(arr)
    assert arr == expected


def test_quick_sort_basic():
    """Test quick sort with basic input."""
    arr = [1, 4, 8, 95, 20, 400, 83, 44, 0, 11, 4444, 3]
    expected = sorted(arr.copy())
    quick_sort(arr)
    assert arr == expected


def test_quick_sort_empty():
    """Test quick sort with empty array."""
    arr = []
    quick_sort(arr)
    assert arr == []


def test_quick_sort_single():
    """Test quick sort with single element."""
    arr = [42]
    quick_sort(arr)
    assert arr == [42]


def test_partition():
    """Test partition function."""
    arr = [1, 4, 8, 95, 20, 40, 83, 65, 0, 111, 4444, 3]
    i_pivot = 3
    pivot_value = arr[i_pivot]

    new_pivot_index = partition(arr, 0, len(arr), i_pivot)

    assert 0 <= new_pivot_index < len(arr)
    assert arr[new_pivot_index] == pivot_value

    # Check partitioning property
    for i in range(len(arr)):
        if i < new_pivot_index:
            assert arr[i] <= arr[new_pivot_index]
        elif i > new_pivot_index:
            assert arr[i] >= arr[new_pivot_index]


# Parameterized tests (pytest feature)
@pytest.mark.parametrize("sort_func", [merge_sort, quick_sort])
def test_sorting_algorithms(sort_func):
    """Test multiple sorting algorithms with same data."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(arr.copy())

    sort_func(arr)
    assert arr == expected


@pytest.mark.parametrize("pivot_type", [QsPivot.First, QsPivot.Last, QsPivot.Random])
def test_quick_sort_pivot_types(pivot_type):
    """Test quick sort with different pivot strategies."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(arr.copy())

    quick_sort(arr, pivot=pivot_type)
    assert arr == expected


# Property-based testing with random data
@pytest.mark.parametrize("sort_func", [merge_sort, quick_sort])
def test_sorting_random_data(sort_func):
    """Test sorting with random data (property-based testing)."""
    for _ in range(10):  # Run multiple times with different random data
        arr = [random.randint(0, 1000) for _ in range(100)]
        expected = sorted(arr.copy())

        sort_func(arr)
        assert arr == expected


# Fixtures for complex setup (advanced pytest feature)
@pytest.fixture
def large_random_array():
    """Fixture that provides a large random array."""
    return [random.randint(0, 10000) for _ in range(1000)]


def test_merge_sort_performance(large_random_array):
    """Test merge sort with large array (using fixture)."""
    arr = large_random_array.copy()
    expected = sorted(arr.copy())

    merge_sort(arr)
    assert arr == expected


def test_quick_sort_performance(large_random_array):
    """Test quick sort with large array (using fixture)."""
    arr = large_random_array.copy()
    expected = sorted(arr.copy())

    quick_sort(arr)
    assert arr == expected


# Edge cases
def test_merge_sort_two_elements():
    """Test merge sort with two elements."""
    arr = [2, 1]
    merge_sort(arr)
    assert arr == [1, 2]

    arr = [1, 2]
    merge_sort(arr)
    assert arr == [1, 2]


def test_quick_sort_two_elements():
    """Test quick sort with two elements."""
    arr = [2, 1]
    quick_sort(arr)
    assert arr == [1, 2]

    arr = [1, 2]
    quick_sort(arr)
    assert arr == [1, 2]


# Stress testing (like the original unittest version)
def test_merge_sort_stress():
    """Stress test merge sort with many random arrays."""
    for _ in range(50):  # Reduced from 200 for faster testing
        arr = [random.randint(0, 1000) for _ in range(random.randint(10, 100))]
        expected = sorted(arr.copy())
        merge_sort(arr)
        assert arr == expected


def test_quick_sort_stress():
    """Stress test quick sort with many random arrays."""
    for _ in range(50):  # Reduced from 200 for faster testing
        arr = [random.randint(0, 1000) for _ in range(random.randint(10, 100))]
        expected = sorted(arr.copy())
        quick_sort(arr)
        assert arr == expected
