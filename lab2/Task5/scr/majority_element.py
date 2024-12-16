import time, tracemalloc
from lab2.utils import read_input, write_output


def count_occurrences(arr, left, right, element):
    return sum(1 for i in range(left, right + 1) if arr[i] == element)


def majority_element_rec(arr, left, right):
    if left == right:
        return arr[left]

    mid = (left + right) // 2
    left_majority = majority_element_rec(arr, left, mid)
    right_majority = majority_element_rec(arr, mid + 1, right)

    if left_majority == right_majority:
        return left_majority

    left_count = count_occurrences(arr, left, right, left_majority)
    right_count = count_occurrences(arr, left, right, right_majority)

    return left_majority if left_count > right_count else right_majority


def has_majority_element(arr):
    n = len(arr)
    candidate = majority_element_rec(arr, 0, n - 1)
    count = count_occurrences(arr, 0, n - 1, candidate)
    return 1 if count > n // 2 else 0
