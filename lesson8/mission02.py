cells = 1
total_hours = int(input('Введите коичество часов: '))
for hour in range(1, total_hours // 3 + 1):
    hour *= 3
    cells *= 2
    print('Прошло часов: ', hour)
    print('Клеток = ', cells)
    print()
print('всего прошло =', hour, 'часов. Клеток = ', cells, 'Осталось часов = ', total_hours - hour)
