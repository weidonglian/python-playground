import unittest
from typing import Optional
from .sorting import Comparable, merge_sort


def inversions_fast[T: Comparable](
    arr: list[T], start: Optional[int] = None, end: Optional[int] = None
) -> int:
    """
    Count the number of inversions in the input list using divide-and-conquer.

    Args:
        arr: The list to count inversions in
        start: The start index of the list to be processed (inclusive)
        end: The end index of the list to be processed (exclusive)

    Returns:
        The number of inversions in the list

    Raises:
        ValueError: If start/end indices are invalid
    """
    total_length = len(arr)
    if start is None:
        start = 0
    if end is None:
        end = total_length

    length = end - start
    if start < 0 or end > total_length:
        raise ValueError('Invalid start/end arguments for inversions_fast')

    if length <= 1:
        return 0
    elif length == 2:
        return 1 if arr[start] > arr[end - 1] else 0
    else:
        middle = start + length // 2
        a_res = inversions_fast(arr, start, middle)
        b_res = inversions_fast(arr, middle, end)
        a = arr[start:middle]
        b = arr[middle:end]
        merge_sort(a)
        merge_sort(b)
        merge_res = 0
        i = 0
        j = 0
        while j < len(b):
            if i >= len(a):
                break
            elif b[j] < a[i]:
                merge_res += len(a) - i
                j += 1
            else:
                i += 1
        return merge_res + a_res + b_res


def inversion_slow[T: Comparable](arr: list[T]) -> int:
    """
    Count the number of inversions using O(n²) algorithm.

    Args:
        arr: The list to count inversions in

    Returns:
        The number of inversions in the list
    """
    cnt = 0
    for i in range(0, len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                cnt += 1
    return cnt


class TestSorting(unittest.TestCase):
    def setUp(self) -> None:
        self.input = [1, 8, 9, 4, 100, 48, 999, 33, 222, 22, 7, 5]

    def test_inversion(self) -> None:
        arr = self.input.copy()
        nb_fast = inversions_fast(arr)
        nb_slow = inversion_slow(arr)
        self.assertEqual(nb_fast, nb_slow)


if __name__ == '__main__':
    unittest.main()
