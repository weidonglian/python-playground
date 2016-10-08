import random
import unittest


def merge_sort(alist):
    """
    Merge sort the input list and return sorted list.
    :param alist: The list to sort.
    :return: The sorted list.
    """
    length = len(alist)
    if length <= 1:
        return alist
    else:
        a = merge_sort(alist[:length // 2])
        b = merge_sort(alist[length // 2:])
        if len(a) + len(b) != length:
            raise Exception('Wrong split the array')
        c = []
        i = 0
        j = 0
        max_i = len(a) - 1
        max_j = len(b) - 1
        for k in range(0, length):
            if i <= max_i and j <= max_j:
                if a[i] < b[j]:
                    c.append(a[i])
                    i += 1
                else:
                    c.append(b[j])
                    j += 1
            elif i <= max_i:
                c.append(a[i])
                i += 1
            elif j <= max_j:
                c.append(b[j])
                j += 1
        return c


class TestSorting(unittest.TestCase):
    def setUp(self):
        self.input = [1, 4, 8, 95, 20, 400, 83, 44, 0, 11, 4444, 3]

    def merge_sort_test(self, ainput):
        output = merge_sort(ainput)
        # print(output)
        self.assertTrue(len(output) == len(ainput))
        for idx in range(0, len(output) - 1):
            self.assertTrue(output[idx] <= output[idx + 1])

    def test_merge_sort(self):
        self.merge_sort_test(self.input)

    def test_merge_sort_random(self):
        for j in range(0, 100):
            self.merge_sort_test([int(1000 * random.random()) for i in range(100)])


if __name__ == '__main__':
    unittest.main()
