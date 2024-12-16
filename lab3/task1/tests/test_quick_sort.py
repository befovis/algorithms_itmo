import unittest
from lab3.task1.scr.quick_sort import quick_sort


class TestQuickSort(unittest.TestCase):

    def test_quick_sort_sorted_input(self):
        # GIVEN
        array = [1, 2, 3, 4, 5]
        expected_result = [1, 2, 3, 4, 5]

        # WHEN
        result = quick_sort(array)

        # THEN
        self.assertEqual(result, expected_result)

    def test_quick_sort_unsorted_input(self):
        # GIVEN
        array = [5, 3, 1, 4, 2]
        expected_result = [1, 2, 3, 4, 5]

        # WHEN
        result = quick_sort(array)

        # THEN
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
