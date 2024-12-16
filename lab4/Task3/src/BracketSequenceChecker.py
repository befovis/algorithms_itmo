# Task3/src/BracketSequenceChecker.py

"""Модуль для валидации скобочных последовательностей."""

from lab4.utils.IOHandler import IOHandler


class BracketSequenceChecker:
    """Класс для проверки корректности скобочных последовательностей."""

    def __init__(self):
        """Инициализация соответствия открывающих и закрывающих скобок."""
        self.pair_brackets = {')': '(', ']': '[', '}': '{'}

    def is_valid_sequence(self, sequence):
        """
        Проверяет правильность скобочной последовательности.

        :param sequence: Строка со скобками.
        :return: True, если последовательность корректна, иначе False.
        """
        stack = []

        for char in sequence:
            if char in "([{":
                stack.append(char)
            elif char in ")]}":
                if stack and stack[-1] == self.pair_brackets.get(char):
                    stack.pop()
                else:
                    return False
        return not stack

    def evaluate_sequences(self, sequences):
        """
        Оценивает список скобочных последовательностей.

        :param sequences: Список строковых последовательностей.
        :return: Список результатов ("YES" или "NO").
        """
        outcomes = []
        for seq in sequences:
            clean_seq = seq.strip()
            outcomes.append("YES" if self.is_valid_sequence(clean_seq) else "NO")
        return outcomes

    @staticmethod
    def load_sequences(file_path):
        """
        Загружает скобочные последовательности из файла.

        :param file_path: Путь к входному файлу.
        :return: Кортеж из количества и списка последовательностей.
        """
        lines = IOHandler.read_file(file_path)
        count = int(lines[0])
        seqs = lines[1:]
        return count, seqs

    @staticmethod
    def validate_data(count, sequences):
        """
        Валидирует входные данные.

        :param count: Количество последовательностей.
        :param sequences: Список строковых последовательностей.
        :return: True, если данные валидны, иначе False.
        """
        if not (1 <= count <= 500):
            return False
        if len(sequences) != count:
            return False
        for seq in sequences:
            if not (1 <= len(seq.strip()) <= 10**4):
                return False
        return True

    @staticmethod
    def save_results(file_path, results):
        """
        Сохраняет результаты в файл.

        :param file_path: Путь к выходному файлу.
        :param results: Список строковых результатов.
        """
        output = "\n".join(results)
        IOHandler.write_file(file_path, output)
