import unittest
from lab4.Task13.src.Stack import Stack
from io import StringIO
from unittest.mock import patch

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_given_empty_stack_when_display_then_no_output(self):
        # GIVEN
        # WHEN
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.stack.display()
            # THEN
            self.assertEqual(fake_out.getvalue(), "")

    def test_given_empty_stack_when_push_pop_then_correct_element(self):
        # GIVEN
        # WHEN
        self.stack.push(10)
        popped = self.stack.pop()
        # THEN
        self.assertEqual(popped, 10)
        self.assertTrue(self.stack.is_empty())


if __name__ == '__main__':
    unittest.main()