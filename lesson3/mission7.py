distance = 115
speed = int(input('Введите скорость: '))
time = int(input('Введите время: '))
point = distance*(speed*time//distance)
point_2 = speed*time-point
if point < distance:
    print(speed*time)
else:
    print(point_2)
