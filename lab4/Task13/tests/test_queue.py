import unittest
from lab4.Task13.src.Queue import Queue

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue(5)

    def test_given_empty_queue_when_enqueue_then_peek_and_size_correct(self):
        # GIVEN
        # WHEN
        self.queue.enqueue(42)
        # THEN
        self.assertEqual(self.queue.peek(), 42)
        self.assertEqual(self.queue.size(), 1)

    def test_given_queue_one_element_when_dequeue_then_empty(self):
        # GIVEN
        self.queue.enqueue(10)
        # WHEN
        removed = self.queue.dequeue()
        # THEN
        self.assertEqual(removed, 10)
        self.assertTrue(self.queue.is_empty())

    def test_given_full_queue_when_enqueue_then_overflow(self):
        # GIVEN
        for i in range(5):
            self.queue.enqueue(i)
        # WHEN
        result = self.queue.enqueue(99)
        # THEN
        self.assertEqual(result, 'Очередь переполнена')

    def test_given_empty_queue_when_dequeue_then_underflow(self):
        # GIVEN
        # WHEN
        result = self.queue.dequeue()
        # THEN
        self.assertEqual(result, 'Очередь пуста')


if __name__ == '__main__':
    unittest.main()