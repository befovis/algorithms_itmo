def scarecrow_sort(n, k, sizes):
    groups = [[] for _ in range(k)]
    for i in range(n):
        groups[i % k].append(sizes[i])
    for group in groups:
        group.sort(reverse=True)

    sorted_dolls = [groups[i % k][i // k] for i in range(n)]
    return sorted_dolls == sorted(sorted_dolls, reverse=True)
