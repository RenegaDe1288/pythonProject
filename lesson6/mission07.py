temp = int(input('Сколько градусов на улице? '))
dist = 0
while temp > 15:
    dist += 20
    temp -= 2
    print('Температура = ', temp)
    print('Вы пробежали ', dist)
    if temp > 15:
          dist += 10
print(dist, temp)
