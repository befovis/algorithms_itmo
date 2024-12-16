def merge(array, left, middle, right):
    left_sub, right_sub = array[left:middle + 1] + [float('inf')], array[middle + 1:right + 1] + [float('inf')]
    i = j = 0
    for k in range(left, right + 1):
        if left_sub[i] <= right_sub[j]:
            array[k], i = left_sub[i], i + 1
        else:
            array[k], j = right_sub[j], j + 1

def merge_sort(array, left, right):
    if left < right:
        middle = (left + right) // 2
        merge_sort(array, left, middle)
        merge_sort(array, middle + 1, right)
        merge(array, left, middle, right)
