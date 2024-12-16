import os
from lab3.utils import *
from lab3.task1.scr.quick_sort import quick_sort


@measure_time_and_memory
def main():
    # Чтение данных
    data = read_file(os.path.join(TXT_DIR, INPUT_FILES_DIR, 'input.txt'))
    n = int(data[0])
    mas = list(map(int, data[1].split()))

    # Обработка данных
    sorted_mas = quick_sort(mas)

    # Подготовка результата
    result = " ".join(map(str, sorted_mas))

    # Запись результатов
    write_file(result, os.path.join(TXT_DIR, OUTPUT_FILES_DIR, 'output.txt'))

if __name__ == "__main__":
    main()
