import unittest
from lab4.Task3.src.BracketSequenceChecker import BracketSequenceChecker

class TestBracketSequenceChecker(unittest.TestCase):
    def setUp(self):
        self.checker = BracketSequenceChecker()

    def test_given_empty_string_when_check_then_valid(self):
        # GIVEN
        # WHEN
        result = self.checker.is_valid_sequence("")
        # THEN
        self.assertTrue(result)

    def test_given_complex_sequence_when_check_then_valid(self):
        # GIVEN
        # WHEN
        result = self.checker.is_valid_sequence("{[()]}")
        # THEN
        self.assertTrue(result)

    def test_given_incorrect_sequence_when_check_then_invalid(self):
        # GIVEN
        # WHEN
        result = self.checker.is_valid_sequence("([)]")
        # THEN
        self.assertFalse(result)

    def test_given_large_valid_sequence_when_check_then_true(self):
        # GIVEN
        sequence = "()" * 1000
        # WHEN
        result = self.checker.is_valid_sequence(sequence)
        # THEN
        self.assertTrue(result)

    def test_given_invalid_data_when_validate_then_false(self):
        # GIVEN
        # WHEN
        result = self.checker.validate_data(0, [])
        # THEN
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()