import os
from lab3.utils import *
from lab3.task7.scr.digital_sort import digital_sort

@measure_time_and_memory
def main():
    # Чтение данных
    data = read_file(os.path.join(TXT_DIR, INPUT_FILES_DIR, 'input.txt'))
    n, m, k = map(int, data[0].split())

    if len(data[1:]) != m:
        raise ValueError(f"Ожидалось {m} строк данных, получено {len(data[1:])}.")

    # Преобразование данных
    strings = [''.join(data[1 + i][j] for i in range(m)).strip() for j in range(n)]

    if any(len(s) != m for s in strings):
        raise ValueError(f"Некорректная длина строк. Все строки должны быть длины {m}.")

    # Обработка данных
    sorted_strings = digital_sort(strings, k, m)

    # Подготовка результата
    result_indices = [strings.index(s) + 1 for s in sorted_strings]
    result = '\n'.join(map(str, result_indices))

    # Запись результатов
    write_file(result, os.path.join(TXT_DIR, OUTPUT_FILES_DIR, 'output.txt'))

if __name__ == "__main__":
    main()
