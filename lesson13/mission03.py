round = int(input('Введите количество цифр: '))


def count(round):
    maxcount = 0
    maxnum = 0
    for num in range(1, round + 1):
        x = int(input('Введите число: '))
        count = counts(x)
        if count > maxcount:
            maxcount = count
            maxnum = x
    print('Наибольшее количество цифр  в цифре ', maxnum, ' всего = ', maxcount)


def counts(x):
    count = 0
    if x <= 0:
        print('Обнуляю. чисел в цифре ноль')
        return count
    else:
        while x > 0:
            count = count + 1
            x = x // 10
    print("Количество цифр равно:", count)
    return count


count(round)
