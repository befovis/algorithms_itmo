import unittest
from lab4.Task1.src.StackProcessor import StackProcessor

class TestStackProcessor(unittest.TestCase):
    def test_given_empty_stack_when_push_multiple_then_no_results(self):
        # GIVEN
        processor = StackProcessor()
        # WHEN
        processor.process_commands(["+ 10", "+ 20", "+ 30"])
        # THEN
        self.assertEqual(processor.get_results(), [])

    def test_given_stack_when_push_and_pop_all_then_results_reverse(self):
        # GIVEN
        processor = StackProcessor()
        processor.process_commands(["+ 5", "+ 1", "+ 100"])
        # WHEN
        processor.process_commands(["-", "-", "-"])
        # THEN
        self.assertEqual(processor.get_results(), [100, 1, 5])

    def test_given_stack_when_interleave_push_pop_then_correct_results(self):
        # GIVEN
        processor = StackProcessor()
        # WHEN
        processor.process_commands(["+ 7", "+ 14", "-", "+ 21", "-", "+ 28", "-"])
        # THEN
        self.assertEqual(processor.get_results(), [14, 21, 28])

    def test_given_invalid_commands_when_validate_then_false(self):
        # GIVEN
        processor = StackProcessor()
        # WHEN
        result = processor.validate_commands(["push10", "pop"])
        # THEN
        self.assertFalse(result)

    def test_given_out_of_range_number_when_validate_then_false(self):
        # GIVEN
        processor = StackProcessor()
        # WHEN
        result = processor.validate_commands(["+ 999999999999", "-"])
        # THEN
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()