my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
print('Мой список: ', my_list)
i = 0
while not (my_list[i] < 0):
    i += 1
    if i > len(my_list):
        break
    if my_list[i-1] == 0:
        continue
    print('Положительное число из списка: ', my_list[i-1])
print('End')
