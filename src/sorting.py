import random
import unittest


def merge_sort(alist, start=None, end=None):
    """
    Merge sort the input list and return sorted list.
    :param start: The start index of the list to be sorted.
    :param end: The end index of the list to be sorted.
    :param alist: The list to sort.
    """
    if not alist:
        return
    total_length = len(alist)
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
        if alist[start] > alist[end - 1]:
            alist[start], alist[end - 1] = alist[end - 1], alist[start]
    else:
        middle = start + length // 2
        merge_sort(alist, start, middle)
        merge_sort(alist, middle, end)
        # Drawback of merge sort algorithm that requires extra memory space for merging
        a = alist[start:middle]
        b = alist[middle:end]
        i = 0
        j = 0
        max_i = len(a) - 1
        max_j = len(b) - 1
        for k in range(start, end):
            if i <= max_i and j <= max_j:
                if a[i] < b[j]:
                    alist[k] = a[i]
                    i += 1
                else:
                    alist[k] = b[j]
                    j += 1
            elif i <= max_i:
                alist[k] = a[i]
                i += 1
            elif j <= max_j:
                alist[k] = b[j]
                j += 1


def quick_sort(alist, start=None, end=None):
    """
    Quick sort algorithm implementation.
    :param alist: The list to sort.
    :param start: The start index of the list to be processed.
    :param end: The end index of the list to processed.
    """
    pass


class TestSorting(unittest.TestCase):
    def setUp(self):
        self.input = [1, 4, 8, 95, 20, 400, 83, 44, 0, 11, 4444, 3]

    def merge_sort_test(self, alist):
        merge_sort(alist)
        # print(output)
        for idx in range(0, len(alist) - 1):
            self.assertTrue(alist[idx] <= alist[idx + 1])

    def test_merge_sort(self):
        self.merge_sort_test(self.input)

    def test_merge_sort_random(self):
        for j in range(0, 100):
            self.merge_sort_test([int(1000 * random.random()) for i in range(100)])


if __name__ == '__main__':
    unittest.main()
