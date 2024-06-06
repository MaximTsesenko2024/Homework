Count_complete_homework = 12
Count_hours = 1.5
Name_course = 'Python'
Hours_per_homework = Count_hours/Count_complete_homework
Out_string = 'Курс '+str(Name_course)+', всего задач: '+str(Count_complete_homework)
Out_string = Out_string + ', затрачено часов: '+str(Count_hours)
Out_string = Out_string + ', среднее время выполнения '+str(Hours_per_homework)+' часа.'
print(Out_string)
