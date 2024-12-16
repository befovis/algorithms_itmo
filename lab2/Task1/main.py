import time
import tracemalloc
from lab2.utils import *
from lab2.Task1.scr.merge_sort import merge_sort
import os


def main():
    tracemalloc.start()
    t_start = time.perf_counter()

    n, arr = read_input(os.path.join(TXT_DIR, INPUT_FILES_DIR, 'input.txt'))
    sorted_arr = merge_sort(arr)

    write_output(os.path.join(TXT_DIR, OUTPUT_FILES_DIR, 'output.txt'), sorted_arr)

    print("Время работы: %s секунд" % (time.perf_counter() - t_start))
    print("Max memory:", tracemalloc.get_traced_memory()[1] / 2 ** 20, "MB")
    tracemalloc.stop()



if __name__ == "__main__":
    main()
