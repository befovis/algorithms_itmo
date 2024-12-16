"""Module implementing a queue based on a linked list."""

from typing import Optional, Union


class Node:
    """Node class for a singly linked list."""

    def __init__(self, value: int) -> None:
        self.value: int = value
        self.next_node: Optional['Node'] = None


class Queue:
    """Queue with a limited size based on a linked list."""

    def __init__(self, max_size: int) -> None:
        """
        Initialize the queue.

        :param max_size: Maximum size of the queue.
        """
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.current_size: int = 0
        self.max_size: int = max_size

    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return self.current_size == 0

    def is_full(self) -> bool:
        """Check if the queue is full."""
        return self.current_size >= self.max_size

    def enqueue(self, value: int) -> Optional[str]:
        """
        Add an element to the end of the queue.

        :param value: Value to be added.
        :return: Message if the queue is full.
        """
        if self.is_full():
            return 'Очередь переполнена'
        new_node: Node = Node(value)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            assert self.tail is not None  # For type checker
            self.tail.next_node = new_node
            self.tail = new_node
        self.current_size += 1

    def dequeue(self) -> Union[int, str]:
        """
        Remove an element from the front of the queue.

        :return: Value of the removed element or message if the queue is empty.
        """
        if self.is_empty():
            return 'Очередь пуста'
        assert self.head is not None  # For type checker
        removed_value: int = self.head.value
        self.head = self.head.next_node
        if not self.head:
            self.tail = None
        self.current_size -= 1
        return removed_value

    def peek(self) -> Optional[int]:
        """
        Get the value of the first element without removing it.

        :return: Value or None if the queue is empty.
        """
        return self.head.value if self.head else None

    def size(self) -> int:
        """Get the current size of the queue."""
        return self.current_size
