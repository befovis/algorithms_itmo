import os
from lab2.utils import *
from lab2.Task4.scr.binary_search import binary_search


def task():
    input_path = os.path.join(TXT_DIR, INPUT_FILES_DIR, 'input.txt')
    output_path = os.path.join(TXT_DIR, OUTPUT_FILES_DIR, 'output.txt')

    with open(input_path, "r", encoding='utf-8') as f:
        _ = int(f.readline().strip())
        a = list(map(int, f.readline().strip().split()))
        k = int(f.readline().strip())
        b = list(map(int, f.readline().strip().split()))

    results = [binary_search(a, b[i]) for i in range(k)]

    write_output(output_path, results)
