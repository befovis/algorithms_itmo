import unittest
from lab2.Task2.scr.merge_sort_with_indices import merge_sort


class TestMergeSortWithIndices(unittest.TestCase):

    def test_merge_sort_unsorted(self):
        # GIVEN
        array = [38, 27, 43, 3, 9, 82, 10]
        expected = sorted(array)

        # WHEN
        merge_sort(array, 0, len(array) - 1)

        # THEN
        self.assertEqual(array, expected)

    def test_merge_sort_sorted(self):
        # GIVEN
        array = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]

        # WHEN
        merge_sort(array, 0, len(array) - 1)

        # THEN
        self.assertEqual(array, expected)


    def test_merge_sort_reverse_sorted(self):
        # GIVEN
        array = [5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5]

        # WHEN
        merge_sort(array, 0, len(array) - 1)

        # THEN
        self.assertEqual(array, expected)


    def test_merge_sort_single_element(self):
        # GIVEN
        array = [42]
        expected = [42]

        # WHEN
        merge_sort(array, 0, len(array) - 1)

        # THEN
        self.assertEqual(array, expected)


if __name__ == '__main__':
    unittest.main()
