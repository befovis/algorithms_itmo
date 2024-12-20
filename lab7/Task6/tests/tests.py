import unittest
from lab7.Task6.src.LISFinder import LISFinder

class TestFindLIS(unittest.TestCase):
    def test_given_sequence_when_find_lis_then_correct(self):
        # GIVEN
        sequence = [2, 9, 4, 7, 3]
        # WHEN
        length, subseq = LISFinder.find_lis(sequence)
        # THEN
        self.assertEqual(length, 3)
        self.assertEqual(subseq, [2,4,7])

    def test_given_ascending_when_find_lis_then_full(self):
        # GIVEN
        sequence = [1,2,3]
        # WHEN
        length, subseq = LISFinder.find_lis(sequence)
        # THEN
        self.assertEqual(length, 3)
        self.assertEqual(subseq, [1,2,3])

    def test_given_descending_when_find_lis_then_one(self):
        # GIVEN
        sequence = [5,4,3]
        # WHEN
        length, subseq = LISFinder.find_lis(sequence)
        # THEN
        self.assertEqual(length, 1)
        self.assertEqual(subseq, [3])

    def test_given_all_equal_when_find_lis_then_one(self):
        # GIVEN
        sequence = [10,10,10]
        # WHEN
        length, subseq = LISFinder.find_lis(sequence)
        # THEN
        self.assertEqual(length, 1)
        self.assertEqual(subseq, [10])


if __name__ == "__main__":
    unittest.main()