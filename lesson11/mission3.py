import math

size = int(input('Введите размер файла: '))
speed = int(input('Введите скорость соединения: '))
all = 0
for sec in range(1, math.ceil(size / speed) + 1):
    if all <= size - speed:
        all = sec * speed
        print('Прошло ', sec, 'сек. Скачано', all, 'из ', size, 'Мб, ', int(all / size * 100), '%')
    else:
        all = size
        print('Прошло ', sec, 'сек. Скачано', all, 'из ', size, 'Мб, ', int(all / size * 100), '%')

print('Загрузка завершена')
