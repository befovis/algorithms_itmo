import unittest
from lab2.Task4.scr.binary_search import binary_search


class TestBinarySearch(unittest.TestCase):

    def test_should_find_element_in_array(self):
        # GIVEN
        data = [1, 2, 3, 4, 5]
        target = 3
        expected_index = 2

        # WHEN
        result = binary_search(data, target)

        # THEN
        self.assertEqual(result, expected_index)

    def test_should_return_minus_one_for_missing_element(self):
        # GIVEN
        data = [1, 2, 3, 4, 5]
        target = 6
        expected_index = -1

        # WHEN
        result = binary_search(data, target)

        # THEN
        self.assertEqual(result, expected_index)

    def test_should_find_first_element(self):
        # GIVEN
        data = [1, 2, 3, 4, 5]
        target = 1
        expected_index = 0

        # WHEN
        result = binary_search(data, target)

        # THEN
        self.assertEqual(result, expected_index)

    def test_should_find_last_element(self):
        # GIVEN
        data = [1, 2, 3, 4, 5]
        target = 5
        expected_index = 4

        # WHEN
        result = binary_search(data, target)

        # THEN
        self.assertEqual(result, expected_index)

    def test_should_handle_empty_array(self):
        # GIVEN
        data = []
        target = 1
        expected_index = -1

        # WHEN
        result = binary_search(data, target)

        # THEN
        self.assertEqual(result, expected_index)

    def test_should_handle_single_element(self):
        # GIVEN
        data = [3]
        target = 3
        expected_index = 0

        # WHEN
        result = binary_search(data, target)

        # THEN
        self.assertEqual(result, expected_index)


if __name__ == '__main__':
    unittest.main()
