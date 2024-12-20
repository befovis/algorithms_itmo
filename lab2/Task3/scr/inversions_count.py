import time


def merge_and_count(arr, temp_arr, left, right, start_time, time_limit=2):
    if time.perf_counter() - start_time > time_limit:
        raise TimeoutError("Превышено время выполнения")

    if left == right:
        return 0

    mid = (left + right) // 2
    inv_count = 0

    inv_count += merge_and_count(arr, temp_arr, left, mid, start_time, time_limit)
    inv_count += merge_and_count(arr, temp_arr, mid + 1, right, start_time, time_limit)
    inv_count += merge(arr, temp_arr, left, mid, right)

    return inv_count


def merge(arr, temp_arr, left, mid, right):
    i, j, k = left, mid + 1, left
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_count += (mid - i + 1)
            j += 1
        k += 1

    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count


def count_inversions(arr, n, time_limit=2):
    temp_arr = [0] * n
    start_time = time.perf_counter()
    try:
        return merge_and_count(arr, temp_arr, 0, n - 1, start_time, time_limit)
    except TimeoutError:
        return "Превышено время выполнения"
