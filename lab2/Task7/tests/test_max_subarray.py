import unittest
from lab2.Task7.scr.max_subarray import search_max_subarray


class TestSearchMaxSubarray(unittest.TestCase):

    def test_search_max_subarray_basic(self):
        # GIVEN
        array = [-2, -3, 4, -1, -2, 1, 5, -3]
        expected_subarray = [4, -1, -2, 1, 5]

        # WHEN
        result = search_max_subarray(array)

        # THEN
        self.assertEqual(result, expected_subarray)

    def test_search_max_subarray_all_negative(self):
        # GIVEN
        array = [-8, -3, -6, -2, -5, -4]
        expected_subarray = [-2]

        # WHEN
        result = search_max_subarray(array)

        # THEN
        self.assertEqual(result, expected_subarray)

    def test_search_max_subarray_single_element(self):
        # GIVEN
        array = [7]
        expected_subarray = [7]

        # WHEN
        result = search_max_subarray(array)

        # THEN
        self.assertEqual(result, expected_subarray)

    def test_search_max_subarray_empty(self):
        # GIVEN
        array = []
        expected_subarray = []

        # WHEN
        result = search_max_subarray(array)

        # THEN
        self.assertEqual(result, expected_subarray)


if __name__ == '__main__':
    unittest.main()
