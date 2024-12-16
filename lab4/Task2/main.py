# Task2/main.py

"""Главный модуль для запуска обработки очередных команд."""

import os
from lab4.Task2.src.QueueProcessor import QueueProcessor
from lab4.utils.consts import TXT_DIR, INPUT_FILES_DIR, OUTPUT_FILES_DIR
from lab4.utils.decorate import measure_time_and_memory
from lab4.utils.IOHandler import IOHandler


@measure_time_and_memory
def main():
    """Инициализация и выполнение обработки команд очереди."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    txt_directory = IOHandler.get_path(base_dir, TXT_DIR)
    input_file = IOHandler.get_path(txt_directory, INPUT_FILES_DIR, 'input.txt')
    output_file = IOHandler.get_path(txt_directory, OUTPUT_FILES_DIR, 'output.txt')

    queue_processor = QueueProcessor()
    commands = queue_processor.read_commands(input_file)

    if not queue_processor.validate_commands(commands):
        print("Некорректные данные. Пожалуйста, проверьте ввод.")
        return

    queue_processor.process_commands(commands)
    queue_processor.write_results(output_file, queue_processor.get_results())
    print("Завершено. Результаты сохранены в output.txt")


if __name__ == '__main__':
    main()
