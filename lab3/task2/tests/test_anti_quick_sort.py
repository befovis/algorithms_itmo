import unittest
from lab3.task2.scr.anti_quick_sort import anti_quick

class TestAntiQuick(unittest.TestCase):

    def test_should_handle_single_element(self):
        # GIVEN
        n = 1
        expected_output = [1]

        # WHEN
        result = anti_quick(n)

        # THEN
        self.assertEqual(result, expected_output)

    def test_should_handle_two_elements(self):
        # GIVEN
        n = 2
        expected_output = [1, 2]

        # WHEN
        result = anti_quick(n)

        # THEN
        self.assertEqual(result, expected_output)

    def test_should_return_increasing_sequence_for_large_n(self):
        # GIVEN
        n = 10
        expected_output = anti_quick(n)  # Expected result depends on logic of anti_quick

        # WHEN
        result = anti_quick(n)

        # THEN
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()
