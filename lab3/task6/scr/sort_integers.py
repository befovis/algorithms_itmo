import random


def quick_sort(mas):
    if len(mas) <= 1:
        return mas
    elem = mas[random.randint(0, len(mas) - 1)]
    left = [i for i in mas if i < elem]
    mid = [elem] * mas.count(elem)
    right = [i for i in mas if i > elem]
    return quick_sort(left) + mid + quick_sort(right)

def mult(mas1, mas2):
    """Умножает элементы массивов, сортирует результат и суммирует каждый 10-й элемент."""
    lst = [eli * elj for eli in mas2 for elj in mas1]
    lst = quick_sort(lst)
    return sum(lst[i] for i in range(0, len(lst), 10))
