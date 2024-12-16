import os
from lab3.utils import *
from lab3.task8.scr.k_points import get_k_closest_points


@measure_time_and_memory
def main():
    # Чтение данных
    data = read_file(os.path.join(TXT_DIR, INPUT_FILES_DIR, 'input.txt'))
    n, k = map(int, data[0].split())
    points = [tuple(map(int, line.strip().split())) for line in data[1:n + 1]]

    # Обработка данных
    closest_points = get_k_closest_points(points, k)

    # Подготовка результата
    formatted_result = ','.join([f"[{x},{y}]" for (x, y) in closest_points])

    # Запись результатов
    write_file(formatted_result, os.path.join(TXT_DIR, OUTPUT_FILES_DIR, 'output.txt'))

if __name__ == "__main__":
    main()
