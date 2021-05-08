x = int(input('Введите координату икс: '))
y = int(input('Введите координату игрек: '))


def coordinates(x, y):
    print('Координаты: ', x, y)
    if -1 <= x <= 1 and -1 <= y <= 1:
        print('Монетка где-то рядом. ')
    else:
        print('Монетки рядом НЕТ.')

coordinates(x, y)


