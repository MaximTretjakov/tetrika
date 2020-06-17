def search_pairs(k, arr):
    """
    - Какая сложность у вашего алгоритма?
    Операция добавления элемента в список tmp.append() проходит за: O(1) - константная сложность.
    Асимптотическая сложность алгоритма O(n) – линейная сложность, т.к. производим проход по n элементам массива.
    Массив предварительно отсортирован.

    - Можно ли его оптимизировать?
    наверное возможно.
    """
    start = 0
    tmp = []
    end = len(arr) - 1
    while start < end:
        summ = arr[start] + arr[end]
        if summ > k:
            end -= 1
        elif summ < k:
            start += 1
        else:
            tmp.append((arr[start], arr[end]))
            end -= 1

    return tmp


if __name__ == '__main__':
    test_array = [1, 2, 6, 5, 3, 4, 7, 8, 3, 2]
    target = 5
    result = search_pairs(target, sorted(test_array))
    print(f'result : {set(result)}')
