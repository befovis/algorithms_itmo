# Task5/src/MaxStack.py

"""Модуль, реализующий стек с поддержкой получения максимума."""

from lab4.utils.IOHandler import IOHandler


class MaxStack:
    """
    Класс, реализующий стек с возможностью получения текущего максимума за O(1).
    """

    def __init__(self):
        """Инициализация основного стека и вспомогательного стека для хранения максимумов."""
        self.elements = []
        self.max_elements = []

    def push(self, val):
        """
        Добавляет элемент в стек.

        :param val: Число для добавления в стек.
        """
        self.elements.append(val)
        if not self.max_elements or val >= self.max_elements[-1]:
            self.max_elements.append(val)
        else:
            self.max_elements.append(self.max_elements[-1])

    def pop(self):
        """Удаляет верхний элемент из стека."""
        if self.elements:
            self.elements.pop()
            self.max_elements.pop()

    def get_max(self):
        """
        Возвращает текущий максимум в стеке.

        :return: Максимальное значение или None, если стек пуст.
        """
        return self.max_elements[-1] if self.max_elements else None

    @staticmethod
    def load_commands(file_path):
        """
        Загружает команды из файла.

        :param file_path: Путь к входному файлу.
        :return: Кортеж из количества команд и списка команд.
        """
        lines = IOHandler.read_file(file_path)
        total_commands = int(lines[0].strip())
        cmds = [line.strip() for line in lines[1:]]
        return total_commands, cmds

    @staticmethod
    def validate_commands(total, cmds):
        """
        Проверяет корректность списка команд.

        :param total: Общее количество команд.
        :param cmds: Список команд.
        :return: True, если все команды валидны, иначе False.
        """
        if not (1 <= total <= 400000):
            return False
        if len(cmds) != total:
            return False
        for command in cmds:
            if command.startswith("push"):
                parts = command.split()
                if len(parts) != 2:
                    return False
                try:
                    num = int(parts[1])
                    if not (0 <= num <= 100000):
                        return False
                except ValueError:
                    return False
            elif command not in {"pop", "max"}:
                return False
        return True

    @staticmethod
    def save_output(file_path, output_data):
        """
        Сохраняет результаты в файл.

        :param file_path: Путь к выходному файлу.
        :param output_data: Список результатов.
        """
        content = "\n".join(output_data)
        IOHandler.write_file(file_path, content)
