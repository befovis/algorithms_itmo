import unittest
from lab4.Task8.src.PostfixEvaluator import PostfixEvaluator

class TestPostfixEvaluator(unittest.TestCase):
    def setUp(self):
        self.evaluator = PostfixEvaluator()

    def test_given_basic_operations_when_evaluate_then_correct_result(self):
        # GIVEN
        # WHEN
        res_add = self.evaluator.evaluate_postfix(["2", "3", "+"])
        res_sub = self.evaluator.evaluate_postfix(["10", "4", "-"])
        res_mul = self.evaluator.evaluate_postfix(["6", "7", "*"])
        # THEN
        self.assertEqual(res_add, 5)
        self.assertEqual(res_sub, 6)
        self.assertEqual(res_mul, 42)

    def test_given_complex_expression_when_evaluate_then_correct(self):
        # GIVEN
        # WHEN
        result = self.evaluator.evaluate_postfix(["2", "3", "+", "4", "*", "5", "+"])
        # THEN
        self.assertEqual(result, 25)

    def test_given_large_numbers_when_evaluate_then_correct(self):
        # GIVEN
        # WHEN
        result = self.evaluator.evaluate_postfix(["2147483646", "1", "+"])
        # THEN
        self.assertEqual(result, 2147483647)

    def test_given_invalid_operator_when_evaluate_then_error(self):
        # GIVEN
        # WHEN/THEN
        with self.assertRaises(ValueError):
            self.evaluator.evaluate_postfix(["2", "3", "&"])

    def test_given_overflow_when_evaluate_then_error(self):
        # GIVEN
        # WHEN/THEN
        with self.assertRaises(ValueError):
            self.evaluator.evaluate_postfix(["1073741824", "2", "*"])

    def test_given_out_of_bounds_number_when_evaluate_then_error(self):
        # GIVEN
        # WHEN/THEN
        with self.assertRaises(ValueError):
            self.evaluator.evaluate_postfix(["2147483648"])

    def test_given_empty_expression_when_evaluate_then_error(self):
        # GIVEN
        # WHEN/THEN
        with self.assertRaises(IndexError):
            self.evaluator.evaluate_postfix([])

    def test_given_unbalanced_expression_when_evaluate_then_error(self):
        # GIVEN
        # WHEN/THEN
        with self.assertRaises(IndexError):
            self.evaluator.evaluate_postfix(["2", "+"])

    def test_given_zeros_when_evaluate_then_correct(self):
        # GIVEN
        # WHEN
        result = self.evaluator.evaluate_postfix(["0", "0", "+", "0", "*"])
        # THEN
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()