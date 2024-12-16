import unittest
from lab2.Task3.scr.inversions_count import count_inversions

class TestCountInversions(unittest.TestCase):

    def test_count_inversions_basic(self):
        # GIVEN
        array = [1, 20, 6, 4, 5]
        n = len(array)
        expected_inversions = 5

        # WHEN
        result = count_inversions(array, n)

        # THEN
        self.assertEqual(result, expected_inversions)

    def test_count_inversions_no_inversions(self):
        # GIVEN
        array = [1, 2, 3, 4, 5]
        n = len(array)
        expected_inversions = 0

        # WHEN
        result = count_inversions(array, n)

        # THEN
        self.assertEqual(result, expected_inversions)

    def test_count_inversions_all_inversions(self):
        # GIVEN
        array = [5, 4, 3, 2, 1]
        n = len(array)
        expected_inversions = 10

        # WHEN
        result = count_inversions(array, n)

        # THEN
        self.assertEqual(result, expected_inversions)

    def test_count_inversions_timeout(self):
        # GIVEN
        large_array = list(range(100000, 0, -1))
        n = len(large_array)
        time_limit = 0.0001
        expected = "Превышено время выполнения"

        # WHEN
        result = count_inversions(large_array, n, time_limit)

        # THEN
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

