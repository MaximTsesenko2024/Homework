def print_params(a='Привет', b=7, c=True):
    print(a, b, c)


print_params()
print_params((2, 4), b=[2, 4], c=2)
print_params(1)
print_params(b=25)
print_params(c=[1, 2, 3])
values_list = ['Строка', True, 3]
values_dict = {'a': 'Строка', 'b': True, 'c': 3}
print_params(*values_list)
print_params(**values_dict)
values_list2 = ['Строка', 3.4]
print_params(*values_list2, 42)
