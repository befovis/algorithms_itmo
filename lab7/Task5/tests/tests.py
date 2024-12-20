import unittest
from lab7.Task5.src.LCS3Finder import LCS3Finder

class TestLongestCommonSubsequence3(unittest.TestCase):
    def test_given_three_arrays_when_lcs3_then_correct(self):
        # GIVEN
        a = [1,2,3,4]
        b = [2,3,4,5]
        c = [2,4,5,6]
        # WHEN
        result = LCS3Finder.longest_common_subsequence_3(a, b, c)
        # THEN
        self.assertEqual(result, 2)

    def test_given_no_common_when_lcs3_then_zero(self):
        # GIVEN
        a = [1]
        b = [2]
        c = [3]
        # WHEN
        result = LCS3Finder.longest_common_subsequence_3(a, b, c)
        # THEN
        self.assertEqual(result, 0)

    def test_given_all_same_when_lcs3_then_full_length(self):
        # GIVEN
        a = [5,5,5]
        b = [5,5,5]
        c = [5,5,5]
        # WHEN
        result = LCS3Finder.longest_common_subsequence_3(a, b, c)
        # THEN
        self.assertEqual(result, 3)

    def test_given_empty_when_lcs3_then_zero(self):
        # GIVEN
        a = []
        b = [1]
        c = [1]
        # WHEN
        result = LCS3Finder.longest_common_subsequence_3(a, b, c)
        # THEN
        self.assertEqual(result, 0)

    def test_given_single_match_when_lcs3_then_one(self):
        # GIVEN
        a = [10]
        b = [10,20]
        c = [30,10]
        # WHEN
        result = LCS3Finder.longest_common_subsequence_3(a, b, c)
        # THEN
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
