import unittest
from lab4.Task2.src.QueueProcessor import QueueProcessor

class TestQueueProcessor(unittest.TestCase):
    def test_given_empty_queue_when_push_pop_fifo(self):
        # GIVEN
        processor = QueueProcessor()
        # WHEN
        processor.process_commands(["+ 10", "+ 20", "-", "-"])
        # THEN
        self.assertEqual(processor.get_results(), [10, 20])

    def test_given_only_push_when_no_pop_then_no_results(self):
        # GIVEN
        processor = QueueProcessor()
        # WHEN
        processor.process_commands(["+ 1", "+ 2", "+ 3"])
        # THEN
        self.assertEqual(processor.get_results(), [])

    def test_given_invalid_commands_when_validate_then_false(self):
        # GIVEN
        processor = QueueProcessor()
        # WHEN
        result = processor.validate_commands(["enqueue5", "-"])
        # THEN
        self.assertFalse(result)

    def test_given_out_of_range_value_when_validate_then_false(self):
        # GIVEN
        processor = QueueProcessor()
        # WHEN
        result = processor.validate_commands(["+ 9999999999999", "-"])
        # THEN
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()