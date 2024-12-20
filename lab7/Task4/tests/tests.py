import unittest
from lab7.Task4.src.LCSFinder import LCSFinder

class TestLongestCommonSubsequence(unittest.TestCase):
    def test_given_two_arrays_when_lcs_then_correct_length(self):
        # GIVEN
        A = [4, 5, 6]
        B = [1, 4, 5, 7]
        # WHEN
        result = LCSFinder.longest_common_subsequence(A, B)
        # THEN
        self.assertEqual(result, 2)

    def test_given_disjoint_sets_when_lcs_then_zero(self):
        # GIVEN
        A = [1,2,3]
        B = [4,5,6]
        # WHEN
        result = LCSFinder.longest_common_subsequence(A, B)
        # THEN
        self.assertEqual(result, 0)

    def test_given_identical_when_lcs_then_full_length(self):
        # GIVEN
        A = [10,20,30]
        B = [10,20,30]
        # WHEN
        result = LCSFinder.longest_common_subsequence(A, B)
        # THEN
        self.assertEqual(result, 3)

    def test_given_empty_when_lcs_then_zero(self):
        # GIVEN
        A = []
        B = [1,2,3]
        # WHEN
        result = LCSFinder.longest_common_subsequence(A, B)
        # THEN
        self.assertEqual(result, 0)

    def test_given_repeats_when_lcs_then_correct_length(self):
        # GIVEN
        A = [2,2,2]
        B = [2,2]
        # WHEN
        result = LCSFinder.longest_common_subsequence(A, B)
        # THEN
        self.assertEqual(result, 2)


if __name__ == "__main__":
    unittest.main()