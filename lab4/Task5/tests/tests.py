# Task5/tests/tests.py

"""Тесты для MaxStack."""

import unittest
from lab4.Task5.src.MaxStack import MaxStack


class TestMaxStack(unittest.TestCase):
    """Класс для тестирования MaxStack."""

    def test_should_push_and_get_max(self):
        """Тест операций push и get_max."""
        get_max_stack = MaxStack()
        get_max_stack.push(2)
        self.assertEqual(get_max_stack.get_max(), 2)

        get_max_stack.push(1)
        self.assertEqual(get_max_stack.get_max(), 2)

        get_max_stack.push(3)
        self.assertEqual(get_max_stack.get_max(), 3)

    def test_should_pop(self):
        """Тест операции pop."""
        get_max_stack = MaxStack()
        get_max_stack.push(5)
        get_max_stack.push(3)
        get_max_stack.push(7)

        get_max_stack.pop()
        self.assertEqual(get_max_stack.get_max(), 5)

        get_max_stack.pop()
        self.assertEqual(get_max_stack.get_max(), 5)

        get_max_stack.pop()
        self.assertIsNone(get_max_stack.get_max())

    def test_should_handle_empty_stack_get_max(self):
        """Тест получения get_max из пустого стека."""
        get_max_stack = MaxStack()
        self.assertIsNone(get_max_stack.get_max())

    def test_should_push_pop_push(self):
        """Тест последовательности операций push и pop."""
        get_max_stack = MaxStack()
        get_max_stack.push(10)
        get_max_stack.pop()
        get_max_stack.push(20)
        self.assertEqual(get_max_stack.get_max(), 20)

    def test_should_push_same_values(self):
        """Тест с одинаковыми значениями."""
        get_max_stack = MaxStack()
        get_max_stack.push(5)
        get_max_stack.push(5)
        get_max_stack.push(5)
        self.assertEqual(get_max_stack.get_max(), 5)

        get_max_stack.pop()
        self.assertEqual(get_max_stack.get_max(), 5)

        get_max_stack.pop()
        self.assertEqual(get_max_stack.get_max(), 5)

        get_max_stack.pop()
        self.assertIsNone(get_max_stack.get_max())

    def test_should_validate_commands(self):
        """Тест валидации команд."""
        valid_n = 3
        valid_commands = ["push 10", "pop", "max"]
        self.assertTrue(MaxStack.validate_commands(valid_n, valid_commands))

        invalid_n = 0
        invalid_commands = []
        self.assertFalse(MaxStack.validate_commands(invalid_n, invalid_commands))

        invalid_n = 3
        invalid_commands = ["push -1", "pop", "max"]
        self.assertFalse(MaxStack.validate_commands(invalid_n, invalid_commands))

        invalid_commands = ["push 100001", "pop", "max"]
        self.assertFalse(MaxStack.validate_commands(invalid_n, invalid_commands))

        invalid_commands = ["push", "pop", "max"]
        self.assertFalse(MaxStack.validate_commands(invalid_n, invalid_commands))

        invalid_commands = ["invalid_command", "pop", "max"]
        self.assertFalse(MaxStack.validate_commands(invalid_n, invalid_commands))


if __name__ == '__main__':
    unittest.main()
