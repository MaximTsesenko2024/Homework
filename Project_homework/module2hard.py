def find_dub(first_n):
    res = ''
    for i in range(1, first_n):
        for j in range(i + 1, first_n):
            sum_numb = i + j
            if first_n % sum_numb == 0:
                res += str(i)
                res += str(j)
    return res


#first = int(input('Введите первое число от 3 до 20: '))
for first in range(3,21):
    # поиск пар чисел
    list_num = find_dub(first)
    print(f'{first} - {list_num}')

#
