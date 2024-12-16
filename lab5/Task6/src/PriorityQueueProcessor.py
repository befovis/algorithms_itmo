# Lab5/Task6/src/PriorityQueueProcessor.py

"""Module for processing priority queue operations."""

import heapq
from typing import List, Tuple


class PriorityQueueProcessor:
    """
    A class to process priority queue operations:
    - A x: Add element x.
    - X: Extract the minimum element.
    - D x y: Decrease the value of the element added in line x+1 to y.
    """

    def __init__(self):
        self.heap: List[Tuple[int, int]] = []        # Min-heap
        self.element_map: dict = {}                  # id → value
        self.id_map: dict = {}                       # line number → element id
        self.removed_elements: set = set()           # Set of removed elements
        self.next_id: int = 0                        # Unique id for each added element

    def process_operations(self, operations: List[str]) -> List[str]:
        """
        Processes a list of priority queue operations.

        :param operations: List of operation strings.
        :return: List of results for 'X' operations.
        """
        output_results: List[str] = []
        for index, operation in enumerate(operations):
            tokens = operation.split()
            command = tokens[0]
            if command == "A":
                # Add element
                value = int(tokens[1])
                heapq.heappush(self.heap, (value, self.next_id))
                self.element_map[self.next_id] = value
                self.id_map[index + 1] = self.next_id
                self.next_id += 1

            elif command == "X":
                # Extract minimum
                self._remove_invalid_elements()
                if self.heap:
                    _, element_id = heapq.heappop(self.heap)
                    output_results.append(str(self.element_map[element_id]))
                    self.removed_elements.add(element_id)
                else:
                    output_results.append("*")

            elif command == "D":
                # Decrease element value
                line_number = int(tokens[1]) + 1
                new_value = int(tokens[2])
                element_id = self.id_map[line_number]
                self.element_map[element_id] = new_value
                heapq.heappush(self.heap, (new_value, element_id))

        return output_results

    def _remove_invalid_elements(self) -> None:
        """Removes elements from the heap that have already been removed."""
        while self.heap and self.heap[0][1] in self.removed_elements:
            heapq.heappop(self.heap)
