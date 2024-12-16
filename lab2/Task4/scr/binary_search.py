import time
import tracemalloc
from lab2.utils import write_output

def binary_search(a, s):
    lw = 0
    hg = len(a) - 1
    while lw <= hg:
        mid = (lw + hg) // 2
        if s == a[mid]:
            return mid
        elif s > a[mid]:
            lw = mid + 1
        else:
            hg = mid - 1
    return -1
