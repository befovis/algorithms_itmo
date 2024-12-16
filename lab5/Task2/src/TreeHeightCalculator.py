"""Module for calculating the height of a tree from a list of parents."""

from typing import List


class TreeHeightCalculator:
    """
    A class to calculate the height of a tree.
    Assumes that -1 in the parents list denotes the root of the tree.
    """

    def tree_height(self, n: int, parents: List[int]) -> int:
        """
        Calculates the height of the tree.

        :param n: Number of nodes.
        :param parents: List of parents for each node (index = node, value = parent).
        :return: Height of the tree.
        """
        tree: List[List[int]] = [[] for _ in range(n)]
        root: int = -1

        for node in range(n):
            parent = parents[node]
            if parent == -1:
                root = node
            else:
                tree[parent].append(node)

        def height(node: int) -> int:
            """Recursively calculates the height of the tree from the given node."""
            if not tree[node]:
                return 1
            return 1 + max(height(child) for child in tree[node])

        return height(root)
