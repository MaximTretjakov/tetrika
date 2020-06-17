def get_zeros(n):
    """
    - Какая сложность у вашего алгоритма?
    Асимптотическая сложность алгоритма O(n2) – квадратичная сложность, т.к. производим проход по 2 массивам.
    второй цикл отрабатывает не полностью и прерывает работу на первой же операции где остаток от деления на 10 != 0
    будет несколько быстрее, но я оцениваю так.
    """
    f = count = 0
    if n > 0: f = 1
    for i in range(2, n + 1):
        f *= i

    for j in range(n):
        if f % 10 == 0:
            count += 1
            f //= 10
        else:
            break

    return count


if __name__ == '__main__':
    data = int(input('Введите число : '))
    print(f'OUT: >> {get_zeros(data)}')

