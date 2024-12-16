# Lab6/Task8/src/HashSolver.py

"""Module for solving hash-related tasks based on given parameters."""

from typing import List


class HashSolver:
    """
    A class to solve hash-related problems with value modifications upon detecting X in the hash table.
    """

    def solve_hash(self, input_data: List[List[int]]) -> str:
        """
        Processes the hash task based on the provided parameters.

        :param input_data: A list containing two lists:
                           - First list: [N, X, A, B]
                           - Second list: [AC, BC, AD, BD]
        :return: A string formatted as "X A B" after all operations.
        """
        N, X, A, B = input_data[0]
        AC, BC, AD, BD = input_data[1]

        hash_set = set()

        for _ in range(N):
            if X in hash_set:
                A = (A + AC) % 1000
                B = (B + BC) % (10 ** 15)
            else:
                hash_set.add(X)
                A = (A + AD) % 1000
                B = (B + BD) % (10 ** 15)

            X = (X * A + B) % (10 ** 15)

        return f"{X} {A} {B}"
