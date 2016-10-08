import unittest


def inversions_fast(alist):
    """
    Counting the number of the inversions of the input list and return the number.
    :param alist: The list to sort.
    :return: The number of inversions.
    """
    length = len(alist)
    if length <= 1:
        return 0
    elif length <= 2:
        return alist[0] > alist[1] and 1 or 0
    else:
        a = alist[:length // 2]
        b = alist[length // 2:]
        if len(a) + len(b) != length:
            raise Exception('Wrong split the array')
        a_res = inversions_fast(a)
        b_res = inversions_fast(b)
        from src.sorting import merge_sort
        a = merge_sort(a)
        b = merge_sort(b)
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


def inversion_slow(alist):
    """
    Counting the number of inversion by O(N*N).
    """
    cnt = 0
    for i in range(0, len(alist) - 1):
        for j in range(i + 1, len(alist)):
            if alist[i] > alist[j]:
                cnt += 1
    return cnt


class TestSorting(unittest.TestCase):
    def setUp(self):
        self.input = [1, 8, 9, 4, 100, 48, 999, 33, 222, 22, 7, 5]

    def inversions_test(self, ainput):
        nb_fast = inversions_fast(ainput)
        print('inversion_fast={0}'.format(nb_fast))
        nb_slow = inversion_slow(ainput)
        print('inversion_slow={0}'.format(nb_slow))
        self.assertTrue(nb_fast == nb_slow)

    def test_inversion(self):
        self.inversions_test(self.input)

    def test_inversion_assignment(self):
        """
        see https://www.coursera.org/learn/algorithm-design-analysis/exam/YLbzP/programming-assignment-1
        """
        import os
        intarray = []
        arrayfilepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.pardir, 'data',
                                     'IntegerArray.txt')
        with open(arrayfilepath) as f:
            for line in f:
                intarray.append(int(line))
        self.assertTrue(len(intarray) == 100000)
        nb_fast = inversions_fast(intarray)
        print('nb_fast={0}'.format(nb_fast))
        self.assertTrue(nb_fast == 2407905288)


if __name__ == '__main__':
    unittest.main()
