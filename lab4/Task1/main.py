# Task1/main.py

"""Главный модуль для запуска обработки стековых команд."""

import os
from lab4.Task1.src.StackProcessor import StackProcessor
from lab4.utils.consts import TXT_DIR, INPUT_FILES_DIR, OUTPUT_FILES_DIR
from lab4.utils.decorate import measure_time_and_memory
from lab4.utils.IOHandler import IOHandler


@measure_time_and_memory
def main():
    """Инициализация и выполнение обработки команд стека."""
    base_path = os.path.dirname(os.path.abspath(__file__))
    txtf_path = IOHandler.get_path(base_path, TXT_DIR)
    input_file = IOHandler.get_path(txtf_path, INPUT_FILES_DIR, 'input.txt')
    output_file = IOHandler.get_path(txtf_path, OUTPUT_FILES_DIR, 'output.txt')

    stack_processor = StackProcessor()
    cmds = stack_processor.read_commands(input_file)

    if not stack_processor.validate_commands(cmds):
        print("Некорректные данные. Пожалуйста, проверьте ввод.")
        return

    stack_processor.process_commands(cmds)
    stack_processor.write_results(output_file, stack_processor.get_results())
    print("Завершено. Результаты сохранены в output.txt")


if __name__ == '__main__':
    main()
