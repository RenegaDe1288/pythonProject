import math
hour = int(input('Введите на какой градус повернулась Часовая стрелка: '))

min = (hour - 30 * int(math. floor(hour/30)))*12

print(min)

