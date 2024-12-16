# Lab4/Task13/main.py

"""Main script to demonstrate the functionality of Queue and Stack."""

from lab4.Task13.src.Queue import Queue
from lab4.Task13.src.Stack import Stack
from lab4.utils.decorate import measure_time_and_memory


@measure_time_and_memory
def main():
    # Demonstrate Queue operations
    print("Queue Demonstration:")
    queue = Queue(5)
    queue.enqueue(10)
    print("Queue size:", queue.size())
    print("First element:", queue.peek())
    queue.dequeue()
    print("Queue size after dequeue:", queue.size())
    print("First element after dequeue:", queue.peek())
    print()

    # Demonstrate Stack operations
    print("Stack Demonstration:")
    stack = Stack()
    print("Is stack empty:", stack.is_empty())
    stack.push(10)
    stack.display()
    popped_value = stack.pop()
    print("Popped element:", popped_value)
    stack.display()
    print("Is stack empty after pop:", stack.is_empty())
    print()


if __name__ == '__main__':
    main()
