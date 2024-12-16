# Lab6/Task6/src/FibonacciChecker.py

"""Module for checking if a number is a Fibonacci number."""

from typing import List


class FibonacciChecker:
    """
    A class to check if numbers are Fibonacci numbers.
    """

    def process_fibonacci(self, numbers: List[int]) -> List[str]:
        """
        For a list of numbers, returns "Yes" or "No" for each,
        depending on whether the number is a Fibonacci number.

        :param numbers: List of integers.
        :return: List of strings "Yes\n" or "No\n".
        """
        verification_results: List[str] = []
        for number in numbers:
            if self._is_fibonacci(number):
                verification_results.append("Yes\n")
            else:
                verification_results.append("No\n")
        return verification_results

    def _is_fibonacci(self, number: int) -> bool:
        """Checks if a number is a Fibonacci number."""
        expression1: int = 5 * (number ** 2) + 4
        expression2: int = 5 * (number ** 2) - 4
        return self._is_perfect_square(expression1) or self._is_perfect_square(expression2)

    def _is_perfect_square(self, x: int) -> bool:
        """Determines if x is a perfect square."""
        if x < 0:
            return False
        left: int = 0
        right: int = x
        while left <= right:
            mid: int = (left + right) // 2
            square: int = mid * mid
            if square == x:
                return True
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1
        return False
