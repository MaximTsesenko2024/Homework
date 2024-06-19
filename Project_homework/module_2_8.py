def get_multiplied_digits(number):
    s = str(number)
    first = int(s[0])
    if len(s) > 1:
        return first * get_multiplied_digits(int(s[1:]))
    else:
        return first


num = int(input('Введите число: '))
mult = get_multiplied_digits(num)
print(num, mult)
