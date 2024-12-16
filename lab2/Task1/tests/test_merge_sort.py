import unittest
from lab2.Task1.scr.merge_sort import merge_sort


class TestMergeSort(unittest.TestCase):

    def test_should_sort_positive_numbers(self):
        # GIVEN
        data = [5, 3, 8, 1, 2]

        # WHEN
        result = merge_sort(data)

        # THEN
        self.assertEqual(result, [1, 2, 3, 5, 8])

    def test_should_sort_negative_numbers(self):
        # GIVEN
        data = [-5, -1, -3, -2, -8]

        # WHEN
        result = merge_sort(data)

        # THEN
        self.assertEqual(result, [-8, -5, -3, -2, -1])

    def test_should_handle_empty_list(self):
        # GIVEN
        data = []

        # WHEN
        result = merge_sort(data)

        # THEN
        self.assertEqual(result, [])

    def test_should_handle_single_element(self):
        # GIVEN
        data = [1]

        # WHEN
        result = merge_sort(data)

        # THEN
        self.assertEqual(result, [1])

    def test_should_sort_mixed_numbers(self):
        # GIVEN
        data = [-3, 2, -1, 5, -4]

        # WHEN
        result = merge_sort(data)

        # THEN
        self.assertEqual(result, [-4, -3, -1, 2, 5])

    def test_should_handle_duplicates(self):
        # GIVEN
        data = [4, 1, 3, 1, 2]

        # WHEN
        result = merge_sort(data)

        # THEN
        self.assertEqual(result, [1, 1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
