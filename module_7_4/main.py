# исходные данные
score_1 = 40  # Очки команды Мастера кода
score_2 = 42  # Очки команды Волшебники Данных
team1_time = 2052.512  # Время команды Мастера кода в секундах
team2_time = 2153.31451  # Время команды Волшебники Данных в секундах


if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

tasks_total = 82  # Общее количество задач
time_avg = (team1_time + team2_time) / tasks_total # Среднее время выполнения задач

# Вывод результата
print(f"Результат соревнования: {result}")
print(f"Всего задач: {tasks_total}")
print(f"Среднее время выполнения задач: {time_avg:.2f} секунды на задачу ")


# Первая команда
team1 = "Мастера кода"
team1_num = 5
result = "В команде %s участников: %d !" % (team1, team1_num)
print(result)

# Общее количество участников
team1_num = 5
team2_num = 6
result = "Общее количество  в командах участников: %d и %d !" % (team1_num, team2_num)
print(result)


result = "Команда Волшебники данных решила задач: {} !" .format(score_2)
print(result)
result = "Волшебники данных решили задачи за {:.1f} с !".format(team2_time)
print(result)

# Решенные задачи  по командам: score_1, score_2
score_1 = 40
score_2 = 42
result = f'Команды решили {score_1} и {score_2} задач.'
print(result)

# Результат соревнований
challenge_result = 'победа команды  Волшебники данных'
result = f'Сегодня было решено {tasks_total} задач, в среднем по { time_avg:.1f} секунды на задачу!"'
print(result)