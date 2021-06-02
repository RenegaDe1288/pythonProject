import math


def cylinder(data):
    side = 2 * math.pi * int(data[0]) * int(data[1])
    full = side + 2 * (2 * (int(data[0]) ** 2))
    return side, full


data = (input('Введите радиус и высоту: ')).split()
data_tuple = cylinder(data)

print('Площадь боковой поверхности: {} '
      '\nПолная площадь: {}'.format(data_tuple[0], data_tuple[1])
      )
