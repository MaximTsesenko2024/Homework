first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')
if first == second and second == third:
    rez = 3
elif first == second or second == third or first == third:
    rez = 2
else:
    rez = 0
print('Количество равных чисел:', rez)
