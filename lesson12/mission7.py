x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))

def min():
    print('Минимальное число = ', int((x + y - abs(x - y)) / 2))

min()

