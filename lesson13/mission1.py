number = float(input('Введите число: '))


def exp(number):
    count = 0
    number_1 = number
    if 1 > number > 0:
        while number_1 < 1:
            count -= 1
            number_1= number_1*10
        print('Число с экспонентой равно ', number * (10 ** abs(count)), '* 10 **', (count))
    elif number_1 > 1:
        while number_1 > 9:
            count += 1
            number_1 = number_1//10
        print('Число с экспонентой равно ', number/(10**(count)), '* 10 **', count )
    else:
        print('Введено отрицательное число. Поробуйте снова ')
exp(number)