import unittest
from lab5.Task6.src.PriorityQueueProcessor import PriorityQueueProcessor

class TestPriorityQueueProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = PriorityQueueProcessor()

    def test_given_ops_add_extract_min_then_fifo_order_by_priority(self):
        # GIVEN
        # WHEN
        result = self.processor.process_operations(["A 5", "A 3", "A 7", "X", "X", "X"])
        # THEN
        self.assertEqual(result, ["3", "5", "7"])

    def test_given_extract_on_empty_then_star(self):
        # GIVEN
        # WHEN
        result = self.processor.process_operations(["X", "X"])
        # THEN
        self.assertEqual(result, ["*", "*"])

    def test_given_decrease_key_when_extract_then_correct_order(self):
        # GIVEN
        # WHEN
        result = self.processor.process_operations(["A 10", "A 15", "A 20", "D 1 5", "X", "X", "X"])
        # THEN
        self.assertEqual(result, ["5", "10", "20"])

    def test_given_large_values_when_process_then_correct(self):
        # GIVEN
        # WHEN
        result = self.processor.process_operations(["A 1000000000", "A -1000000000", "X", "X", "X"])
        # THEN
        self.assertEqual(result, ["-1000000000", "1000000000", "*"])


if __name__ == '__main__':
    unittest.main()