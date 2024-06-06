immutable_var = 1, 5, True, 'Тест', [12, 4]
print(immutable_var)
# immutable_var[1] = True Элемент кортежа нельзя изменить, так как для этого необходимо выполнить операцию присвоения
# элемену нового значения т.е. изменение ссылки в элементе кортежа, что не поддерживается языком.
immutable_var[4][1] = 5
print('Immutable tuple: ', immutable_var)
mutable_list = ['apple', 14, (1, 4), True]
mutable_list[2] = 4
print('Mutable list: ', mutable_list)
