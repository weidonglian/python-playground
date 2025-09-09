#!/usr/bin/env python3
"""Demo script for sorting algorithms."""

import random
import time
from typing import List, Callable

from algorithms.sorting import (
    merge_sort, quick_sort, QsPivot, Comparable
)
from algorithms.inversion import inversions_fast, inversion_slow


def generate_random_array(
    size: int, min_val: int = 1, max_val: int = 1000
) -> List[int]:
    """Generate a random array of given size."""
    return [random.randint(min_val, max_val) for _ in range(size)]


def time_sorting_algorithm(
    arr: List[Comparable],
    sort_func: Callable[[List[Comparable]], None],
    name: str,
) -> float:
    """Time a sorting algorithm and return execution time."""
    arr_copy = arr.copy()
    start_time = time.perf_counter()
    sort_func(arr_copy)
    end_time = time.perf_counter()
    execution_time = end_time - start_time

    # Verify the array is sorted
    is_sorted = all(arr_copy[i] <= arr_copy[i + 1] for i in range(len(arr_copy) - 1))
    if not is_sorted:
        print(f"❌ {name} failed to sort correctly!")
        return -1

    return execution_time


def demo_basic_sorting():
    """Demonstrate basic sorting algorithms."""
    print("🔄 Basic Sorting Algorithm Demo")
    print("=" * 50)

    # Test with small array
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {arr}")

    # Test merge sort
    arr_merge = arr.copy()
    merge_sort(arr_merge)
    print(f"Merge sort result: {arr_merge}")

    # Test quick sort
    arr_quick = arr.copy()
    quick_sort(arr_quick)
    print(f"Quick sort result: {arr_quick}")

    print()


def demo_performance_comparison():
    """Compare performance of different sorting algorithms."""
    print("⚡ Performance Comparison")
    print("=" * 50)

    sizes = [100, 1000, 10000]

    for size in sizes:
        print(f"\nArray size: {size}")
        arr = generate_random_array(size)

        # Time merge sort
        merge_time = time_sorting_algorithm(arr, merge_sort, "Merge Sort")
        if merge_time >= 0:
            print(f"Merge Sort: {merge_time:.6f} seconds")

        # Time quick sort with different pivot strategies
        for pivot in [QsPivot.First, QsPivot.Last, QsPivot.Random]:
            quick_time = time_sorting_algorithm(
                arr,
                lambda x: quick_sort(x, pivot=pivot),
                f"Quick Sort ({pivot.name})"
            )
            if quick_time >= 0:
                print(f"Quick Sort ({pivot.name}): {quick_time:.6f} seconds")

        # Built-in sort for comparison
        builtin_time = time_sorting_algorithm(arr, list.sort, "Built-in Sort")
        if builtin_time >= 0:
            print(f"Built-in Sort: {builtin_time:.6f} seconds")


def demo_inversion_counting():
    """Demonstrate inversion counting algorithms."""
    print("\n🔄 Inversion Counting Demo")
    print("=" * 50)

    test_cases = [
        ([1, 2, 3, 4, 5], "Sorted array"),
        ([5, 4, 3, 2, 1], "Reverse sorted array"),
        ([3, 1, 4, 1, 5, 9, 2, 6, 5, 3], "Random array with duplicates"),
        ([1, 8, 9, 4, 100, 48, 999, 33, 222, 22, 7, 5], "Large random array"),
    ]

    for arr, description in test_cases:
        print(f"\n{description}: {arr}")

        # Count inversions with fast algorithm
        fast_count = inversions_fast(arr)
        print(f"Fast algorithm inversions: {fast_count}")

        # Count inversions with slow algorithm (for small arrays)
        if len(arr) <= 100:  # Only for small arrays to avoid long execution
            slow_count = inversion_slow(arr)
            print(f"Slow algorithm inversions: {slow_count}")
            print(f"✅ Algorithms agree: {fast_count == slow_count}")
        else:
            print("⏭️  Skipping slow algorithm for large array")


def demo_edge_cases():
    """Demonstrate edge cases for sorting algorithms."""
    print("\n🔍 Edge Cases Demo")
    print("=" * 50)

    edge_cases = [
        ([], "Empty array"),
        ([42], "Single element"),
        ([1, 1, 1, 1], "All same elements"),
        ([1, 2, 3, 4, 5], "Already sorted"),
        ([5, 4, 3, 2, 1], "Reverse sorted"),
        ([1, 3, 2, 4, 5], "Nearly sorted"),
    ]

    for arr, description in edge_cases:
        print(f"\n{description}: {arr}")

        # Test merge sort
        arr_merge = arr.copy()
        merge_sort(arr_merge)
        print(f"Merge sort: {arr_merge}")

        # Test quick sort
        arr_quick = arr.copy()
        quick_sort(arr_quick)
        print(f"Quick sort: {arr_quick}")

        # Verify both produce same result
        is_same = arr_merge == arr_quick
        print(f"✅ Results match: {is_same}")


def main():
    """Main demo function."""
    print("🐍 Python Playground - Sorting Algorithms Demo")
    print("=" * 60)

    try:
        demo_basic_sorting()
        demo_performance_comparison()
        demo_inversion_counting()
        demo_edge_cases()

        print("\n🎉 Demo completed successfully!")

    except Exception as e:
        print(f"\n❌ Error during demo: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())