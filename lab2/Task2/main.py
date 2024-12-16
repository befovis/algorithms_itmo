import time, tracemalloc
from lab2.utils import *
from lab2.Task2.scr.merge_sort_with_indices import merge_sort
import os


def main():
    tracemalloc.start()
    t_start = time.perf_counter()

    n, array = read_input(os.path.join(TXT_DIR, INPUT_FILES_DIR, 'input.txt'))
    merge_sort(array, 0, len(array) - 1)

    write_output(os.path.join(TXT_DIR, OUTPUT_FILES_DIR, 'output.txt'), array)

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Текущая память:", tracemalloc.get_traced_memory()[0] / 2 ** 20, "MB; Пик памяти:", tracemalloc.get_traced_memory()[1] / 2 ** 20, "MB")
    tracemalloc.stop()

if __name__ == "__main__":
    main()
