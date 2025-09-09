from enum import Enum
from typing import Protocol, Any, Optional


class Comparable(Protocol):
    def __lt__(self, other: Any) -> bool: ...

    def __eq__(self, other: Any) -> bool: ...

    def __le__(self, other: Any) -> bool: ...


def merge_sort[T: Comparable](
    arr: list[T], start: Optional[int] = None, end: Optional[int] = None
) -> None:
    """
    Merge sort the input list in-place.

    Args:
        arr: The list to sort
        start: The start index of the list to be sorted (inclusive)
        end: The end index of the list to be sorted (exclusive)

    Raises:
        ValueError: If start/end indices are invalid
    """
    if not arr:
        return

    total_length = len(arr)
    if start is None:
        start = 0
    if end is None:
        end = total_length

    if start < 0 or start >= end or end > total_length:
        raise ValueError('Invalid start/end arguments for merge_sort')

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


def partition[T: Comparable](
    arr: list[T], start: int, end: int, i_pivot: int
) -> int:
    """
    Partition the arr between [start, end) using the given index i_pivot.

    Args:
        arr: The list to partition
        start: Start element index (inclusive)
        end: End element index (exclusive)
        i_pivot: The index of the pivot element

    Returns:
        The final position of the pivot element

    Raises:
        ValueError: If indices are invalid
    """
    if not arr:
        raise ValueError("Cannot partition empty array")

    total_length = len(arr)
    if start < 0 or start >= end or end > total_length:
        raise ValueError('Invalid start/end arguments for partition')
    if i_pivot < start or i_pivot >= end:
        raise ValueError('i_pivot must be in range [start, end)')

    if i_pivot != start:
        arr[i_pivot], arr[start] = arr[start], arr[i_pivot]

    left = start
    right = end - 1
    i_pivot = left

    while left < right:
        while left < end and arr[left] <= arr[i_pivot]:  # Move left if item <= pivot
            left += 1
        while right >= start and arr[right] > arr[i_pivot]:  # Move right
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]

    # right is then the final location
    arr[right], arr[i_pivot] = arr[i_pivot], arr[right]
    i_pivot = right
    return i_pivot


def quick_sort[T: Comparable](
    arr: list[T],
    start: Optional[int] = None,
    end: Optional[int] = None,
    pivot: Optional[QsPivot] = None,
) -> None:
    """
    Quick sort algorithm implementation.

    Args:
        arr: The list to sort
        start: The start index of the list to be processed (inclusive)
        end: The end index of the list to be processed (exclusive)
        pivot: The type of pivot selection strategy

    Raises:
        ValueError: If indices are invalid or pivot type is wrong
    """
    if not arr:
        return

    total_length = len(arr)
    if start is None:
        start = 0
    if end is None:
        end = total_length

    if start < 0 or start >= end or end > total_length:
        raise ValueError('Invalid start/end arguments for quick_sort')

    if pivot is None:
        pivot = QsPivot.Random
    if not isinstance(pivot, QsPivot):
        raise ValueError('pivot must be a QsPivot enum value')

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
            raise ValueError('Invalid pivot index after partition')

        if i_pivot - start > 1:
            quick_sort(arr, start, i_pivot)
        if end - i_pivot > 2:
            quick_sort(arr, i_pivot, end)
