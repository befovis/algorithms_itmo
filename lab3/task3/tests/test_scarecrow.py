import unittest

from lab3.task3.scr.scarecrow import scarecrow_sort


class TestScarecrowSort(unittest.TestCase):

    def test_scarecrow_sort_correct_sorting(self):
        # GIVEN
        n, k = 6, 2
        sizes = [6, 5, 4, 3, 2, 1]
        expected_result = True

        # WHEN
        result = scarecrow_sort(n, k, sizes)

        # THEN
        self.assertEqual(result, expected_result)

    def test_scarecrow_sort_incorrect_sorting(self):
        # GIVEN
        n, k = 6, 2
        sizes = [1, 2, 3, 4, 5, 6]
        expected_result = False

        # WHEN
        result = scarecrow_sort(n, k, sizes)

        # THEN
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
