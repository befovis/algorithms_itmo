# Task8/src/PostfixEvaluator.py

"""Модуль для вычисления выражений в постфиксной записи."""

from lab4.utils.IOHandler import IOHandler


class PostfixEvaluator:
    """Класс для вычисления выражений в постфиксной записи."""

    def __init__(self):
        """Инициализация класса."""
        self.MAX_LIMIT = 2 ** 31

    def evaluate_postfix(self, tokens):
        """
        Вычисляет значение выражения в постфиксной записи.

        :param tokens: Список строк, представляющих постфиксное выражение.
        :return: Результат вычисления.
        :raises ValueError: Если найдено число, выходящее за пределы |2^31|,
                            или если обнаружен неизвестный оператор.
        :raises IndexError: Если выражение некорректно (например, недостаточно операндов).
        """
        stack = []

        for token in tokens:
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                num = int(token)
                if abs(num) >= self.MAX_LIMIT:
                    raise ValueError("Найдено число, выходящее за пределы |2^31|")
                stack.append(num)
            else:
                if len(stack) < 2:
                    raise IndexError("Недостаточно операндов для выполнения операции")
                right = stack.pop()
                left = stack.pop()

                if token == '+':
                    result = left + right
                elif token == '-':
                    result = left - right
                elif token == '*':
                    result = left * right
                else:
                    raise ValueError("Неизвестный оператор: {}".format(token))

                if abs(result) >= self.MAX_LIMIT:
                    raise ValueError("Промежуточный результат превышает предел |2^31|")
                stack.append(result)

        if len(stack) != 1:
            raise IndexError("Некорректное выражение")

        return stack.pop()

    @staticmethod
    def load_expression(file_path):
        """
        Считывает выражение из входного файла.

        :param file_path: Путь к входному файлу.
        :return: Кортеж из числа элементов и списка элементов выражения.
        """
        lines = IOHandler.read_file(file_path)
        if not lines:
            raise ValueError("Входной файл пуст")
        count = int(lines[0].strip())
        expression = lines[1].strip().split()
        return count, expression

    @staticmethod
    def validate_expression(count, tokens):
        """
        Валидирует постфиксное выражение.

        :param count: Количество элементов в выражении.
        :param tokens: Список элементов выражения.
        :return: True, если данные валидны, иначе False.
        """
        if not (1 <= count <= 10 ** 6):
            return False
        if len(tokens) != count:
            return False
        for token in tokens:
            if token.isdigit() or (token.startswith('-') and token[1:].isdigit()):
                num = int(token)
                if abs(num) >= 2 ** 31:
                    return False
            elif token not in {'+', '-', '*'}:
                return False
        return True

    @staticmethod
    def save_result(file_path, result):
        """
        Записывает результат в выходной файл.

        :param file_path: Путь к выходному файлу.
        :param result: Результат вычисления.
        """
        IOHandler.write_file(file_path, str(result))
