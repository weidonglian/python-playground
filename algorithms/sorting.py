import random
import unittest
from enum import Enum
from typing import Protocol, Any, Optional


class Comparable(Protocol):
    def __lt__(self, other: Any) -> bool: ...

    def __eq__(self, other: Any) -> bool: ...

    def __le__(self, other: Any) -> bool: ...


def merge_sort[T: Comparable](arr: list[T], start: Optional[int] = None, end: Optional[int] = None):
    """
    Merge sort the input list and return sorted list.
    :param start: The start index of the list to be sorted.
    :param end: The end index of the list to be sorted.
    :param arr: The list to sort.
    """
    if not arr:
        return
    total_length = len(arr)
    if start is None:
        start = 0
    if end is None:
        end = total_length
    if start < 0 or start >= end or end > total_length:
        raise Exception('Illegal start end argument for merge_sort')
    length = end - start
    if length <= 1:
        return
    elif length == 2:
        if arr[start] > arr[end - 1]:
            arr[start], arr[end - 1] = arr[end - 1], arr[start]
    else:
        middle = start + length // 2
        merge_sort(arr, start, middle)
        merge_sort(arr, middle, end)
        # Drawback of merge sort algorithm that requires extra memory space for merging
        a = arr[start:middle]
        b = arr[middle:end]
        i = 0
        j = 0
        max_i = len(a) - 1
        max_j = len(b) - 1
        for k in range(start, end):
            if i <= max_i and j <= max_j:
                if a[i] < b[j]:
                    arr[k] = a[i]
                    i += 1
                else:
                    arr[k] = b[j]
                    j += 1
            elif i <= max_i:
                arr[k] = a[i]
                i += 1
            elif j <= max_j:
                arr[k] = b[j]
                j += 1


class QsPivot(Enum):
    First = 1
    Last = 2
    Random = 3


def partition[T: Comparable](arr: list[T], start: int, end: int, i_pivot: int) -> Optional[int]:
    """
    Partition the arr between [start, end) using the given index i_pivot
    :param arr: The list to partition.
    :param start: Start element.
    :param end: End element.
    :param i_pivot: The index of the pivot element.
    """
    if not arr:
        return None
    total_length = len(arr)
    if start < 0 or start >= end or end > total_length:
        raise Exception('Illegal start end argument for partition')
    if i_pivot < start or i_pivot >= end:
        raise Exception('i_pivot has to be [start, end)')
    if i_pivot != start:
        arr[i_pivot], arr[start] = arr[start], arr[i_pivot]
    left = start
    right = end - 1
    i_pivot = left
    while left < right:
        while left < end and arr[left] <= arr[i_pivot]:  # Move left if item < pivot
            left += 1
        while right >= start and arr[right] > arr[i_pivot]:  # Move right if item > pivot
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
    # right is then the final location
    arr[right], arr[i_pivot] = arr[i_pivot], arr[right]
    i_pivot = right
    return i_pivot


def quick_sort[T: Comparable](arr: list[T], start: Optional[int] = None, end: Optional[int] = None,
                              pivot: Optional[QsPivot] = None):
    """
    Quick sort algorithm implementation.
    :param pivot: The type of QsPivot.
    :param arr: The list to sort.
    :param start: The start index of the list to be processed.
    :param end: The end index of the list to processed.
    :return The pivot index after partition.
    """
    if not arr:
        return
    total_length = len(arr)
    if start is None:
        start = 0
    if end is None:
        end = total_length
    if start < 0 or start >= end or end > total_length:
        raise Exception('Illegal start end argument for quick_sort')
    if pivot is None:
        pivot = QsPivot.Random
    if type(pivot) is not QsPivot:
        raise Exception('Illegal input pivot, it has to QsPivot')
    length = end - start
    if length <= 1:
        return
    elif length == 2:
        if arr[start] > arr[end - 1]:
            arr[start], arr[end - 1] = arr[end - 1], arr[start]
    else:
        if pivot == QsPivot.First:
            i_pivot = start
        elif pivot == QsPivot.Last:
            i_pivot = end - 1
        else:
            from random import randint
            i_pivot = randint(start, end - 1)
        i_pivot = partition(arr, start, end, i_pivot)
        if i_pivot < start or i_pivot >= end:
            raise Exception('Wrong i_pivot after partition process.')
        if i_pivot - start > 1:
            quick_sort(arr, start, i_pivot)
        if end - i_pivot > 2:
            quick_sort(arr, i_pivot, end)


class TestSorting(unittest.TestCase):
    def setUp(self):
        self.input = [1, 4, 8, 95, 20, 400, 83, 44, 0, 11, 4444, 3]

    def sort_test[T: Comparable](self, sort_method, arr: list[T]):
        sort_method(arr)
        for idx in range(0, len(arr) - 1):
            self.assertTrue(arr[idx] <= arr[idx + 1])

    def test_partition(self):
        arr = [1, 4, 8, 95, 20, 40, 83, 65, 0, 111, 4444, 3]
        i_pivot = 3
        pivot = arr[i_pivot]
        i_pivot = partition(arr, 0, len(arr), i_pivot)
        self.assertTrue(0 <= i_pivot < len(arr))
        self.assertTrue(arr[i_pivot] == pivot)
        for i in range(0, len(arr)):
            if i < i_pivot:
                self.assertTrue(arr[i] <= arr[i_pivot])
            elif i > i_pivot:
                self.assertTrue(arr[i] >= arr[i_pivot])

    def test_merge_sort(self):
        self.sort_test(merge_sort, self.input)

    def test_merge_sort_random(self):
        for j in range(0, 200):
            self.sort_test(merge_sort, [int(1000 * random.random()) for _ in range(1000)])

    def test_quick_sort(self):
        self.sort_test(quick_sort, self.input)

    def test_quick_sort_random(self):
        for j in range(0, 200):
            self.sort_test(quick_sort, [int(1000 * random.random()) for _ in range(1000)])


if __name__ == '__main__':
    unittest.main()
