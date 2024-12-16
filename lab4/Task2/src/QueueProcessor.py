# Task2/src/QueueProcessor.py

"""Модуль для управления операциями с очередью."""

from lab4.utils.IOHandler import IOHandler


class QueueProcessor:
    """Класс для выполнения операций с очередью."""

    def __init__(self):
        """Инициализация очереди, индекса передней части и списка результатов."""
        self.queue = []
        self.front = 0
        self.results = []

    def process_commands(self, commands):
        """
        Выполняет команды и сохраняет результаты.

        :param commands: Список строковых команд.
        """
        for cmd in commands:
            if cmd.startswith("+"):
                _, num = cmd.split()
                self.queue.append(int(num))
            elif cmd == "-":
                if self.front < len(self.queue):
                    self.results.append(self.queue[self.front])
                    self.front += 1

    @staticmethod
    def read_commands(file_path):
        """
        Загружает команды из указанного файла.

        :param file_path: Путь к файлу с командами.
        :return: Список команд.
        """
        lines = IOHandler.read_file(file_path)
        return [command.strip() for command in lines[1:]]

    @staticmethod
    def validate_commands(cmds):
        """
        Проверяет корректность списка команд.

        :param cmds: Список строковых команд.
        :return: True, если все команды валидны, иначе False.
        """
        if not (1 <= len(cmds) <= 10**6):
            return False
        for command in cmds:
            if command.startswith("+"):
                parts = command.split()
                if len(parts) != 2:
                    return False
                try:
                    number = int(parts[1])
                    if abs(number) > 10**9:
                        return False
                except ValueError:
                    return False
            elif command != "-":
                return False
        return True

    def get_results(self):
        """
        Возвращает список результатов выполнения команд.

        :return: Список чисел.
        """
        return self.results

    @staticmethod
    def write_results(file_path, results):
        """
        Сохраняет результаты в указанный файл.

        :param file_path: Путь к выходному файлу.
        :param results: Список чисел для записи.
        """
        output = "\n".join(map(str, results))
        IOHandler.write_file(file_path, output)
