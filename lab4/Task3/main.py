# Task3/main.py

"""Главный скрипт для проверки скобочных последовательностей."""

import os
from lab4.Task3.src.BracketSequenceChecker import BracketSequenceChecker
from lab4.utils.consts import TXT_DIR, INPUT_FILES_DIR, OUTPUT_FILES_DIR
from lab4.utils.decorate import measure_time_and_memory
from lab4.utils.IOHandler import IOHandler


@measure_time_and_memory
def main():
    """Запуск процесса проверки скобочных последовательностей."""
    # Определение путей к необходимым директориям и файлам
    base_directory = os.path.dirname(os.path.abspath(__file__))
    txt_directory = IOHandler.get_path(base_directory, TXT_DIR)
    input_file = IOHandler.get_path(txt_directory, INPUT_FILES_DIR, 'input.txt')
    output_file = IOHandler.get_path(txt_directory, OUTPUT_FILES_DIR, 'output.txt')

    # Инициализация проверяющего
    checker = BracketSequenceChecker()

    # Загрузка и проверка входных данных
    total, sequences = checker.load_sequences(input_file)
    if not BracketSequenceChecker.validate_data(total, sequences):
        print("Некорректный ввод. Пожалуйста, проверьте данные.")
        return

    # Оценка последовательностей
    results = checker.evaluate_sequences(sequences)

    # Сохранение результатов
    BracketSequenceChecker.save_results(output_file, results)
    print("Процесс завершен. Результаты сохранены в output.txt")


if __name__ == '__main__':
    main()
