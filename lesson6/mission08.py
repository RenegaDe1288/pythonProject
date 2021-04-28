number = int(input('Введите число: '))
while number % 10 != 5:
    print(number%10)
    number = number // 10
    if number == 0:
        break
else:
    print('Обнаружена цифра 5')
