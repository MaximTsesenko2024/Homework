my_dict = {'Алгебра': 5, 'География': 4, 'Литература': 4}
print('Мой словарь:', my_dict)
print('Существующий элемент:', my_dict.get('Алгебра'))
print('Несуществующий элемент:', my_dict.get('История'))
my_dict['Физика'] = 4
my_dict['Геометрия'] = 5
val = my_dict.pop('География')
print('Значение удалённого элемента:', val)
print('Мой словарь: ', my_dict)
my_set = {1, 3, (1, 2), 3, 5, 1, 'Test', True, 'Test'}
print('Моё множество:', my_set)
my_set.add(12)
my_set.add((4, 5))
my_set.remove(5)
print('Моё изменённое множество:', my_set)
