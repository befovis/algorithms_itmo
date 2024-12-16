import os
from lab3.utils import *
from lab3.task2.scr.anti_quick_sort import anti_quick


@measure_time_and_memory
def main():
    # Чтение данных
    data = read_file(os.path.join(TXT_DIR, INPUT_FILES_DIR, 'input.txt'))
    n = int(data[0])

    # Обработка данных
    sorted_mas = anti_quick(n)

    # Подготовка результата
    result = " ".join(map(str, sorted_mas))

    # Запись результатов
    write_file(result, os.path.join(TXT_DIR, OUTPUT_FILES_DIR, 'output.txt'))

if __name__ == "__main__":
    main()
