"""
Использование f-строк:

Переменные: количество задач (tasks_total) и среднее время решения (time_avg).
Пример итоговой строки: "Сегодня было решено 82 задач, в среднем по 350.4 секунды на задачу!."
"""

team1_num = 5
print('В команде Мастера кода участников: %s ! ' % team1_num)
team2_num = 6
print("Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num))
score_2 = 42
print("Команда Волшебники данных решила задач: {} !".format(score_2))
team2_time = 2153.31451
print(" Волшебники данных решили задачи за {time} с !".format(time=team2_time))
score_1 = 40
print(f"Команды решили {score_1} и {score_2} задач.")
team1_time = 1552.512

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'
print(f'Результат битвы: {challenge_result}')
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.")
