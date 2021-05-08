import math

radius = int(input('Введите радиус сферы: '))


def sphereArea(radius):
    print('\nПлощадь сферы равна - ', math.pi * radius ** 2 * 4)


def sphereVolume(radius):
    print('\nОбъем сферы равен - ', math.pi * radius ** 3 * (4 / 3))


sphereArea(radius)
sphereVolume(radius)
