"""Module implementing a stack based on a linked list."""

from typing import Optional


class Node:
    """Node class for a singly linked list."""

    def __init__(self, data: int) -> None:
        self.data: int = data
        self.next_node: Optional['Node'] = None


class Stack:
    """Stack based on a linked list."""

    def __init__(self) -> None:
        """Initialize the stack."""
        self.top_node: Optional[Node] = None

    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return self.top_node is None

    def push(self, data: int) -> None:
        """Add an element to the top of the stack."""
        new_node: Node = Node(data)
        new_node.next_node = self.top_node
        self.top_node = new_node

    def pop(self) -> Optional[int]:
        """
        Remove the top element from the stack.

        :return: Value of the removed element or None if the stack is empty.
        """
        if self.is_empty():
            return None
        removed_node: Node = self.top_node
        self.top_node = self.top_node.next_node
        return removed_node.data

    def display(self) -> None:
        """Display the elements of the stack."""
        if self.is_empty():
            return
        current: Optional[Node] = self.top_node
        while current:
            print(current.data, end=", ")
            current = current.next_node
        print("None")
