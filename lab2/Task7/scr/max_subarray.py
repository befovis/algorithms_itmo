import time, tracemalloc
from lab2.utils import read_input, write_output


def search_max_subarray(lst):
    start_idx = end_idx = 0
    max_sum = -float('inf')
    current_sum = 0
    temp_start = 0

    for i in range(len(lst)):
        current_sum += lst[i]
        if current_sum > max_sum:
            max_sum = current_sum
            start_idx, end_idx = temp_start, i
        if current_sum < 0:
            current_sum = 0
            temp_start = i + 1

    return lst[start_idx:end_idx + 1]
