# Lab7/Task6/src/LISFinder.py

"""Module for finding the Longest Increasing Subsequence (LIS) in a sequence."""

from bisect import bisect_left
from typing import List, Tuple


class LISFinder:
    """
    A class to find the length and the actual Longest Increasing Subsequence (LIS) in a sequence.
    """

    @staticmethod
    def find_lis(sequence: List[int]) -> Tuple[int, List[int]]:
        """
        Finds the length of the LIS and the subsequence itself.

        :param sequence: A list of integers representing the sequence.
        :return: A tuple containing the length of the LIS and the LIS as a list of integers.
        """
        sequence_length: int = len(sequence)
        lis: List[int] = []
        predecessors: List[int] = [-1] * sequence_length
        lis_indices: List[int] = []

        for current_index in range(sequence_length):
            current_value: int = sequence[current_index]
            insertion_position: int = bisect_left(lis, current_value)

            if insertion_position == len(lis):
                lis.append(current_value)
                lis_indices.append(current_index)
            else:
                lis[insertion_position] = current_value
                lis_indices[insertion_position] = current_index

            if insertion_position > 0:
                predecessors[current_index] = lis_indices[insertion_position - 1]

        lis_length: int = len(lis)
        lis_sequence: List[int] = []
        current_position: int = lis_indices[-1] if lis_indices else -1

        for _ in range(lis_length):
            lis_sequence.append(sequence[current_position])
            current_position = predecessors[current_position]

        lis_sequence.reverse()
        return lis_length, lis_sequence
