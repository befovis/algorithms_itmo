# Lab5/Task7/src/HeapSorter.py

"""Module for performing heap-based sorting of an array."""

from typing import List


class HeapSorter:
    """
    A class to perform heap sort on an array.
    """

    def heapify(self, array: List[int], size: int, root_index: int) -> None:
        """
        Converts a subtree with root at root_index into a max-heap.

        :param array: The array to be heapified.
        :param size: The size of the heap within the array.
        :param root_index: The index of the root of the subtree.
        """
        largest: int = root_index
        left_child: int = 2 * root_index + 1
        right_child: int = 2 * root_index + 2

        # Check if left child exists and is greater than root
        if left_child < size and array[left_child] > array[largest]:
            largest = left_child

        # Check if right child exists and is greater than the current largest
        if right_child < size and array[right_child] > array[largest]:
            largest = right_child

        # If the largest element is not the root, swap and continue heapifying
        if largest != root_index:
            array[root_index], array[largest] = array[largest], array[root_index]
            self.heapify(array, size, largest)

    def heapsort(self, array: List[int]) -> None:
        """
        Performs heap sort on the provided array.

        :param array: The array to be sorted.
        """
        n: int = len(array)

        # Build a max-heap from the array
        for idx in range(n // 2 - 1, -1, -1):
            self.heapify(array, n, idx)

        # Extract elements from the heap one by one
        for idx in range(n - 1, 0, -1):
            array[0], array[idx] = array[idx], array[0]  # Swap
            self.heapify(array, idx, 0)  # Heapify the reduced heap
