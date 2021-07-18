import random


def luck():
    pos = random.randint(0, 38)
    print('Выпало: ', pos)
    try:
        raise exceptions[pos]
    except IndexError:
        print('Удача!')


file_1 = open('total.txt', 'w')
total = 0
exceptions = [ArithmeticError, ImportError, MemoryError]
while total < 777:
    number = int(input('Введите число: '))
    luck()
    file_1.write(str(number) + '\n')
    total += number
file_1.close()
