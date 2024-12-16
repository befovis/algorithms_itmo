# Lab7/Task5/src/LCS3Finder.py

"""Module for calculating the length of the Longest Common Subsequence (LCS) for three sequences."""

from typing import List


class LCS3Finder:
    """
    A class to find the length of the Longest Common Subsequence (LCS) among three sequences.
    """

    @staticmethod
    def longest_common_subsequence_3(
        sequence_a: List[int], sequence_b: List[int], sequence_c: List[int]
    ) -> int:
        """
        Calculates the length of the LCS for three sequences.

        :param sequence_a: The first sequence (list of integers).
        :param sequence_b: The second sequence (list of integers).
        :param sequence_c: The third sequence (list of integers).
        :return: The length of the LCS for the three sequences.
        """
        len_a: int = len(sequence_a)
        len_b: int = len(sequence_b)
        len_c: int = len(sequence_c)
        dp: List[List[List[int]]] = [
            [[0] * (len_c + 1) for _ in range(len_b + 1)] for __ in range(len_a + 1)
        ]

        for i in range(1, len_a + 1):
            for j in range(1, len_b + 1):
                for k in range(1, len_c + 1):
                    if (
                        sequence_a[i - 1] == sequence_b[j - 1]
                        and sequence_a[i - 1] == sequence_c[k - 1]
                    ):
                        dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                    else:
                        dp[i][j][k] = max(
                            dp[i - 1][j][k],
                            dp[i][j - 1][k],
                            dp[i][j][k - 1],
                        )

        return dp[len_a][len_b][len_c]
