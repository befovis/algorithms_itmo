import os
from lab3.utils import *
from lab3.task6.scr.sort_integers import mult


@measure_time_and_memory
def main():
    # Чтение данных
    data = read_file(os.path.join(TXT_DIR, INPUT_FILES_DIR, 'input.txt'))
    n, m = map(int, data[0].split())
    mas1 = list(map(int, data[1].split()))
    mas2 = list(map(int, data[2].split()))

    # Обработка данных
    result = mult(mas1, mas2)

    # Запись результатов
    write_file(str(result), os.path.join(TXT_DIR, OUTPUT_FILES_DIR, 'output.txt'))

if __name__ == "__main__":
    main()
