def sqr(x: float):
    return x ** 2


def sqr_l(int_list: list):
    return list(map(sqr, int_list))


def apply_all_func(int_list: list, *functions):
    result = {}
    for function_ in functions:
        result[function_.__name__] = function_(int_list)
    return result


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
print(apply_all_func([6, 20, 15, 9], max, min, sqr_l))
