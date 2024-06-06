grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print(students)
students = list(students)
print(students)
my_dic = {k: v for k, v in zip(students, [sum(grades[x])/len(grades[x]) for x in range(len(grades))])}
print('Средний бал по каждому ученику: ', my_dic)
