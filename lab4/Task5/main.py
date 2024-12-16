# Task5/main.py

"""Основной скрипт для работы со стеком MaxStack."""

import os
from lab4.Task5.src.MaxStack import MaxStack
from lab4.utils.consts import TXT_DIR, INPUT_FILES_DIR, OUTPUT_FILES_DIR
from lab4.utils.decorate import measure_time_and_memory
from lab4.utils.IOHandler import IOHandler


@measure_time_and_memory
def main():
    """Запускает обработку команд для стека MaxStack."""
    # Определение путей к файлам
    base_directory = os.path.dirname(os.path.abspath(__file__))
    txt_folder = IOHandler.get_path(base_directory, TXT_DIR)
    input_file = IOHandler.get_path(txt_folder, INPUT_FILES_DIR, 'input.txt')
    output_file = IOHandler.get_path(txt_folder, OUTPUT_FILES_DIR, 'output.txt')

    # Инициализация стека
    stack = MaxStack()

    # Загрузка и проверка команд
    total, commands = stack.load_commands(input_file)
    if not MaxStack.validate_commands(total, commands):
        print("Некорректные данные. Пожалуйста, проверьте ввод.")
        return

    # Обработка команд
    results = []
    for cmd in commands:
        if cmd.startswith("push"):
            _, value = cmd.split()
            stack.push(int(value))
        elif cmd == "pop":
            stack.pop()
        elif cmd == "max":
            current_max = stack.get_max()
            results.append(str(current_max) if current_max is not None else "None")

    # Сохранение результатов
    MaxStack.save_output(output_file, results)
    print("Обработка завершена. Результаты записаны в output.txt")


if __name__ == '__main__':
    main()
