import unittest
from lab4.Task4.src.BracketChecker import BracketChecker

class TestBracketChecker(unittest.TestCase):
    def setUp(self):
        self.checker = BracketChecker()

    def test_given_correct_sequence_when_check_then_success(self):
        # GIVEN
        # WHEN
        result = self.checker.check_brackets("([]){()}")
        # THEN
        self.assertEqual(result, "Success")

    def test_given_incorrect_sequence_when_check_then_error(self):
        # GIVEN
        # WHEN
        result = self.checker.check_brackets("{[}")
        # THEN
        self.assertEqual(result, "3")

    def test_given_unmatched_closing_when_check_then_error(self):
        # GIVEN
        # WHEN
        result = self.checker.check_brackets("foo(bar);)")
        # THEN
        self.assertEqual(result, "10")

    def test_given_unmatched_opening_when_check_then_error(self):
        # GIVEN
        # WHEN
        result = self.checker.check_brackets("([]")
        # THEN
        self.assertEqual(result, "1")

    def test_given_empty_string_when_check_then_success(self):
        # GIVEN
        # WHEN
        result = self.checker.check_brackets("")
        # THEN
        self.assertEqual(result, "Success")

    def test_given_no_brackets_when_check_then_success(self):
        # GIVEN
        # WHEN
        result = self.checker.check_brackets("Hello")
        # THEN
        self.assertEqual(result, "Success")

    def test_given_complex_sequence_when_check_then_success(self):
        # GIVEN
        # WHEN
        result = self.checker.check_brackets("([](){([])})")
        # THEN
        self.assertEqual(result, "Success")

    def test_given_incorrect_nested_when_check_then_error(self):
        # GIVEN
        # WHEN
        result = self.checker.check_brackets("({[}])")
        # THEN
        self.assertEqual(result, "4")

    def test_given_unmatched_opening_start_when_check_then_error(self):
        # GIVEN
        # WHEN
        result = self.checker.check_brackets("{")
        # THEN
        self.assertEqual(result, "1")

    def test_given_unmatched_closing_start_when_check_then_error(self):
        # GIVEN
        # WHEN
        result = self.checker.check_brackets("}")
        # THEN
        self.assertEqual(result, "1")


if __name__ == '__main__':
    unittest.main()