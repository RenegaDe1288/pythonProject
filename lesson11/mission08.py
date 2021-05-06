import math

line = float(input('Введите расстояние до цели:  '))
angle = int(input('Введите угол обнаружения: '))

angle /= 57.2958

x = math.cos(angle)*line
y = math.sin(angle)*line

print('Координаты цели : ', x,y)