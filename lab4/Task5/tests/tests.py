import unittest
from lab4.Task5.src.MaxStack import MaxStack

class TestMaxStack(unittest.TestCase):
    def test_given_push_get_max_then_correct_max(self):
        # GIVEN
        s = MaxStack()
        # WHEN
        s.push(2)
        s.push(1)
        s.push(3)
        # THEN
        self.assertEqual(s.get_max(), 3)

    def test_given_push_pop_check_max_then_correct_behavior(self):
        # GIVEN
        s = MaxStack()
        s.push(5)
        s.push(3)
        s.push(7)
        # WHEN
        s.pop()
        # THEN
        self.assertEqual(s.get_max(), 5)
        s.pop()
        self.assertEqual(s.get_max(), 5)
        s.pop()
        self.assertIsNone(s.get_max())

    def test_given_empty_stack_when_get_max_then_none(self):
        # GIVEN
        s = MaxStack()
        # WHEN
        # THEN
        self.assertIsNone(s.get_max())

    def test_given_sequence_push_pop_then_correct_max(self):
        # GIVEN
        s = MaxStack()
        # WHEN
        s.push(10)
        s.pop()
        s.push(20)
        # THEN
        self.assertEqual(s.get_max(), 20)

    def test_given_same_values_when_pop_then_max_remains(self):
        # GIVEN
        s = MaxStack()
        # WHEN
        s.push(5)
        s.push(5)
        s.push(5)
        s.pop()
        # THEN
        self.assertEqual(s.get_max(), 5)

    def test_given_commands_validation_then_correct_result(self):
        # GIVEN
        # WHEN
        valid = MaxStack.validate_commands(3, ["push 10", "pop", "max"])
        invalid_empty = MaxStack.validate_commands(0, [])
        invalid_negative = MaxStack.validate_commands(3, ["push -1", "pop", "max"])
        invalid_large = MaxStack.validate_commands(3, ["push 100001", "pop", "max"])
        invalid_no_arg = MaxStack.validate_commands(3, ["push", "pop", "max"])
        invalid_unknown = MaxStack.validate_commands(3, ["invalid_command", "pop", "max"])
        # THEN
        self.assertTrue(valid)
        self.assertFalse(invalid_empty)
        self.assertFalse(invalid_negative)
        self.assertFalse(invalid_large)
        self.assertFalse(invalid_no_arg)
        self.assertFalse(invalid_unknown)


if __name__ == '__main__':
    unittest.main()