# Task1/src/StackProcessor.py

"""Модуль для управления стековыми операциями."""

from lab4.utils.IOHandler import IOHandler


class StackProcessor:
    """Класс для выполнения операций со стеком."""

    def __init__(self):
        """Создание стека и списка для результатов."""
        self.stack = []
        self.results = []

    def process_commands(self, commands):
        """
        Выполняет команды и сохраняет результаты.

        :param commands: Список строковых команд.
        """
        for cmd in commands:
            if cmd.startswith("+"):
                _, num = cmd.split()
                self.stack.append(int(num))
            elif cmd == "-":
                if self.stack:
                    self.results.append(self.stack.pop())

    @staticmethod
    def read_commands(input_path):
        """
        Загружает команды из указанного файла.

        :param input_path: Путь к файлу с командами.
        :return: Список команд.
        """
        lines = IOHandler.read_file(input_path)
        return [command.strip() for command in lines[1:]]

    @staticmethod
    def validate_commands(commands):
        """
        Проверяет корректность списка команд.

        :param commands: Список строковых команд.
        :return: True если все команды валидны, иначе False.
        """
        if not (1 <= len(commands) <= 10**6):
            return False
        for command in commands:
            if command.startswith("+"):
                parts = command.split()
                if len(parts) != 2:
                    return False
                try:
                    num = int(parts[1])
                    if abs(num) > 10**9:
                        return False
                except ValueError:
                    return False
            elif command != "-":
                return False
        return True

    def get_results(self):
        """
        Получает список результатов выполнения команд.

        :return: Список чисел.
        """
        return self.results

    @staticmethod
    def write_results(output_path, results):
        """
        Сохраняет результаты в указанный файл.

        :param output_path: Путь к выходному файлу.
        :param results: Список чисел для записи.
        """
        output_data = "\n".join(map(str, results))
        IOHandler.write_file(output_path, output_data)
