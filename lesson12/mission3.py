def calc():
    choise = int(
        input('Введите что вы хотите сделать:  \n 1 - сложить \n 2 - найти наибольшее \n 3 - найти наименьшее\n'))
    if choise == 1:
        summ()
    elif choise == 2:
        max()
    elif choise == 3:
        min()
    else:
        print('Ошибка ввода')


def summ():
    print('Сумма = ', x + y)


def max():
    print((x + y + abs(y - x)) / 2)


def min():
    print((x + y - abs(x - y)) / 2)


while True:
    x = int(input('Введите первое число: '))
    y = int(input('Введите второе число: '))
    calc()
