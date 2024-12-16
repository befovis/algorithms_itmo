import unittest
from lab3.task6.scr.sort_integers import mult

class TestMutl(unittest.TestCase):

    def test_should_return_zero_for_empty_arrays(self):  # GIVEN
        mas1 = []
        mas2 = []
        expected_sum = 0

        # WHEN
        result = mult(mas1, mas2)

        # THEN
        self.assertEqual(result, expected_sum)

    def test_should_handle_single_element_arrays(self):  # GIVEN
        mas1 = [3]
        mas2 = [4]
        expected_sum = 12  # 3 * 4 = 12

        # WHEN
        result = mult(mas1, mas2)

        # THEN
        self.assertEqual(result, expected_sum)


if __name__ == '__main__':
    unittest.main()
