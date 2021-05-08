def test():
    n = int(input('Введите число: '))
    if n < 0:
        negative()
    else:
        positive()


def negative():
    print('Отрицательное')


def positive():
    print('Положительное')


test()
test()
test()
test()