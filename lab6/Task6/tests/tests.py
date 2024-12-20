import unittest
from lab6.Task6.src.FibonacciChecker import FibonacciChecker

class TestFibonacciChecker(unittest.TestCase):
    def setUp(self):
        self.checker = FibonacciChecker()

    def test_given_numbers_when_check_fibo_then_correct_yes_no(self):
        # GIVEN
        numbers = [2, 3, 4, 5, 13, 14]
        # 2(Fibo),3(Fibo),4(Not),5(Fibo),13(Fibo),14(Not)
        # WHEN
        result = self.checker.process_fibonacci(numbers)
        # THEN
        self.assertEqual(result, ["Yes\n", "Yes\n", "No\n", "Yes\n", "Yes\n", "No\n"])


if __name__ == '__main__':
    unittest.main()