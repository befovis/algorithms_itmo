# Lab7/Task4/src/LCSFinder.py

"""Module for calculating the length of the Longest Common Subsequence (LCS) of two sequences."""

from typing import List


class LCSFinder:
    """
    A class to find the length of the Longest Common Subsequence (LCS) between two sequences.
    """

    @staticmethod
    def longest_common_subsequence(sequence_a: List[int], sequence_b: List[int]) -> int:
        """
        Calculates the length of the LCS for two sequences.

        :param sequence_a: The first sequence (list of integers).
        :param sequence_b: The second sequence (list of integers).
        :return: The length of the LCS.
        """
        len_a: int = len(sequence_a)
        len_b: int = len(sequence_b)
        dp: List[List[int]] = [[0] * (len_b + 1) for _ in range(len_a + 1)]

        for i in range(1, len_a + 1):
            for j in range(1, len_b + 1):
                if sequence_a[i - 1] == sequence_b[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[len_a][len_b]
