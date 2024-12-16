import random
from lab3.utils import read_file, write_file, measure_time_and_memory


def quick_sort(mas):
    if len(mas) <= 1:
        return mas
    elem = mas[random.randint(0, len(mas) - 1)]
    left = [i for i in mas if i < elem]
    mid = [elem] * mas.count(elem)
    right = [i for i in mas if i > elem]
    return quick_sort(left) + mid + quick_sort(right)

