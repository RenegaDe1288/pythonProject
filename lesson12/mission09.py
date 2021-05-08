import math


def line1(x, y):
    line = math.sqrt(x ** 2 + y ** 2)
    print('Расстояние равно:', line)


def line2(x_1, x_2, y_1, y_2):
    line = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)
    print('Расстояние равно:', line)


change = int(input('Введите что хотите сделать: 1 или 2 '))
if change == 1:
    x = int(input('Введите координату икс: '))
    y = int(input('Введите координату игрек: '))
    line1(x, y)
elif change == 2:
    x_1 = int(input('Введите координату икс1: '))
    y_1 = int(input('Введите координату игрек1: '))
    x_2 = int(input('Введите координату икс2: '))
    y_2 = int(input('Введите координату игрек2: '))
    line2(x_1, x_2, y_1, y_2)
else:
    print('Ошибка ввода ')
