team1_num = 5
team2_num = 6
team1_time = 1552.512
team1_time =2153.31451
score_1 = 40
score_2 = 42



tasks_total = score_2+score_1
# time_avg = result
print('В команде Мастера кода участников: %s !' % team1_num )
print('Итого сегодня в командах участников: %s и %s !' %(team1_num, team2_num ))
print('Команда Волшебники данных решила задач: {}'.format(score_2))
print("Волшебники данных решили задачи за {} с" .format(team1_time))
print(f"Команды решили {score_1} и {score_2} задач")
print("Результат битвы: победа команды Мастера кода!")
print(f"Сегодня было решено  {tasks_total} задач, в среднем по 350.4 секунды на задачу!.")

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result= "Победа команды Мастера кода!"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = "Победа команды Волшебники Данных!"
else:
    result="Ничья!"
challenge_result=result
print(challenge_result)




