# Task4/src/BracketChecker.py

"""Модуль для валидации скобок в строке."""

from lab4.utils.IOHandler import IOHandler


class BracketChecker:
    """Класс для проверки правильности расстановки скобок в строке."""

    def __init__(self):
        """Инициализация соответствия закрывающих и открывающих скобок."""
        self.bracket_map = {')': '(', ']': '[', '}': '{'}

    def check_brackets(self, text):
        """
        Проверяет строку на корректность расстановки скобок.

        :param text: Строка для проверки.
        :return: "Success" или индекс первой ошибки.
        """
        stack = []
        for pos, char in enumerate(text, start=1):
            if char in "([{":
                stack.append((char, pos))
            elif char in ")]}":
                if not stack or stack[-1][0] != self.bracket_map.get(char):
                    return str(pos)
                stack.pop()

        if stack:
            return str(stack[0][1])

        return "Success"

    @staticmethod
    def load_data(file_path):
        """
        Загружает строку для проверки из файла.

        :param file_path: Путь к входному файлу.
        :return: Строка для проверки.
        """
        lines = IOHandler.read_file(file_path)
        return lines[0].strip()

    @staticmethod
    def save_result(file_path, result):
        """
        Сохраняет результат проверки в файл.

        :param file_path: Путь к выходному файлу.
        :param result: Результат проверки.
        """
        IOHandler.write_file(file_path, result)
