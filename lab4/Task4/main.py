# Task4/main.py

"""Главный скрипт для проверки правильности расстановки скобок в строке."""

import os
from lab4.Task4.src.BracketChecker import BracketChecker
from lab4.utils.consts import TXT_DIR, INPUT_FILES_DIR, OUTPUT_FILES_DIR
from lab4.utils.decorate import measure_time_and_memory
from lab4.utils.IOHandler import IOHandler


@measure_time_and_memory
def main():
    """Запуск процесса проверки скобок в строке."""
    # Определение путей к директориям и файлам
    base_dir = os.path.dirname(os.path.abspath(__file__))
    txt_directory = IOHandler.get_path(base_dir, TXT_DIR)
    input_file = IOHandler.get_path(txt_directory, INPUT_FILES_DIR, 'input.txt')
    output_file = IOHandler.get_path(txt_directory, OUTPUT_FILES_DIR, 'output.txt')

    # Инициализация проверяющего
    checker = BracketChecker()

    # Загрузка данных
    text = checker.load_data(input_file)

    # Проверка скобок
    results = checker.check_brackets(text)

    # Сохранение результата
    checker.save_result(output_file, results)
    print(f"Результат проверки: {results}")
    print("Обработка завершена. Результат записан в output.txt")


if __name__ == '__main__':
    main()
