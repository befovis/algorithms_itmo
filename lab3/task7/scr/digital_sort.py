def counting_sort(strings, index):
    """Стабильная сортировка подсчетом для символа на заданной позиции."""
    count = [0] * 26  # Алфавит a-z
    output = [None] * len(strings)

    for s in strings:
        char = s[index] if index < len(s) else 'a'
        count[ord(char) - ord('a')] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for s in reversed(strings):
        char = s[index] if index < len(s) else 'a'
        pos = ord(char) - ord('a')
        count[pos] -= 1
        output[count[pos]] = s

    return output

def digital_sort(strings, k, m):
    """Цифровая сортировка справа налево."""
    for phase in range(1, k + 1):  # k фаз
        strings = counting_sort(strings, m - phase)
    return strings
