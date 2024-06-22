def calculate_structure_sum(*args):
    """
    Подсчёт суммы всех чисел и длинн всех строк
    :param args: - входная последовательность
    :return: - результат
    """

    res = 0
    if len(args) == 1:
        arg = args[0]
    elif len(args) == 0:
        return 0
    else:
        arg = args
    if isinstance(arg, str):
        return len(arg)
    elif isinstance(arg, int) or isinstance(arg, float):
        return arg

    elif isinstance(arg, dict):
        for key, value in arg.items():
            res += calculate_structure_sum(key)
            res += calculate_structure_sum(value)

    else:
        for i in arg:
            if isinstance(i, str) or isinstance(i, int) or isinstance(i, float):
                res += calculate_structure_sum(i)
            elif isinstance(i, dict):
                res += calculate_structure_sum(i)
            else:
                res += calculate_structure_sum(*i)

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
