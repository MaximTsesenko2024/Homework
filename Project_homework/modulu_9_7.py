from math import sqrt, trunc


def is_prime(func):
    def check_prime(x):
        if x == 1:
            return False
        if x % 2 == 0:
            return False
        for i in range(3, trunc(sqrt(x)) + 1, 2):
            if x % i == 0:
                return False
        return True

    def func_dec(*args, **kwargs):
        result = func(*args, **kwargs)
        if check_prime(result):
            print('Простое число')
        else:
            print('Составное число')
        return result

    return func_dec


@is_prime
def sum_three(a, b, c):
    return a + b + c


s = sum_three(a=315, b=520, c=112)
print(s)
