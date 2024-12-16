import os
from lab3.utils import *
from lab3.task3.scr.scarecrow import scarecrow_sort


@measure_time_and_memory
def main():
    # Чтение данных
    data = read_file(os.path.join(TXT_DIR, INPUT_FILES_DIR, 'input.txt'))
    n, k = map(int, data[0].split())
    sizes = list(map(int, data[1].split()))

    # Обработка данных
    result = scarecrow_sort(n, k, sizes)

    # Подготовка результата
    output = "ДА" if result else "НЕТ"

    # Запись результатов
    write_file(output, os.path.join(TXT_DIR, OUTPUT_FILES_DIR, 'output.txt'))

if __name__ == "__main__":
    main()
