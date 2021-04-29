number_1 = int(input('Введите первое число последовательности:'))
count = 0
while number_1 > 1:
    if (number_1 % 2) == 0:
        count += 1
    number_1 -= 1
    if number_1 <= 1:
        print('Количество четных дней:', count)
        number_1 = int(input('Введите первое число последовательности:'))
        if number_1 != 0:
            count = 0
            continue
        else:
            print('Вы ввели 0:')
            break
