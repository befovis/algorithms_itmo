import unittest
from lab2.Task5.scr.majority_element import has_majority_element


class TestMajorityElement(unittest.TestCase):

    def test_has_majority(self):
        # GIVEN
        arr = [1, 2, 3, 1, 1]
        expected_majority = 1

        # WHEN
        result = has_majority_element(arr)

        # THEN
        self.assertEqual(result, expected_majority)


    def test_single_element(self):
        # GIVEN
        arr = [1]
        expected_majority = 1

        # WHEN checking for a majority element
        result = has_majority_element(arr)

        # THEN
        self.assertEqual(result, expected_majority)


if __name__ == '__main__':
    unittest.main()
