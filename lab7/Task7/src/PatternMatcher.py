# Lab7/Task7/src/PatternMatcher.py

"""Module for checking if a string matches a pattern containing '?' and '*'."""

from typing import List


class PatternMatcher:
    """
    A class to check if a string matches a given pattern.
    The pattern may contain:
    - Letters
    - '?', which matches any single character
    - '*', which matches zero or more characters
    """

    @staticmethod
    def matches_pattern(pattern: str, string: str) -> str:
        """
        Checks if the given string matches the pattern.

        :param pattern: The pattern string containing letters, '?', and '*'.
        :param string: The string to be matched against the pattern.
        :return: "YES" if the string matches the pattern, otherwise "NO".
        """
        pattern_length: int = len(pattern)
        string_length: int = len(string)
        dp: List[List[bool]] = [[False] * (string_length + 1) for _ in range(pattern_length + 1)]
        dp[0][0] = True

        # Initialize dp for patterns starting with '*'
        for pattern_idx in range(1, pattern_length + 1):
            if pattern[pattern_idx - 1] == '*':
                dp[pattern_idx][0] = dp[pattern_idx - 1][0]
            else:
                break

        for pattern_idx in range(1, pattern_length + 1):
            for string_idx in range(1, string_length + 1):
                if pattern[pattern_idx - 1] == string[string_idx - 1] or pattern[pattern_idx - 1] == '?':
                    dp[pattern_idx][string_idx] = dp[pattern_idx - 1][string_idx - 1]
                elif pattern[pattern_idx - 1] == '*':
                    dp[pattern_idx][string_idx] = dp[pattern_idx - 1][string_idx] or dp[pattern_idx][string_idx - 1]

        return "YES" if dp[pattern_length][string_length] else "NO"
