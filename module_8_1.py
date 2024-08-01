def add_everything_up(first, second):
    try:
        return first + second
    except TypeError:
        return str(first) + str(second)


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
