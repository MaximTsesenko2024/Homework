def calculate_structure_sum(arg):
    """
    Подсчёт суммы всех чисел и длинн всех строк
    :param arg: - входная последовательность
    :return: - результат
    """

    res = 0
    if isinstance(arg, str):
        return len(arg)
    elif isinstance(arg, (int, float)):
        return arg

    elif isinstance(arg, dict):
        for key, value in arg.items():
            res += calculate_structure_sum(key)
            res += calculate_structure_sum(value)

    elif isinstance(arg, (list, set, tuple)):
        for i in arg:
            res += calculate_structure_sum(i)

    return res


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
print(data_structure)
count = calculate_structure_sum(data_structure)
print(f'Результат подсчёта: {count}')
