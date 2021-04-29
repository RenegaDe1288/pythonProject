x = int(input('Введите число: '))
num = 5
count = 0
while x != num:
    if x < num:
        print('Число меньше, чем нужно. Попробуйте ещё раз!')
    elif x > num:
        print('Число больше, чем нужно. Попробуйте ещё раз!')
    count += 1
    x = int(input('Введите число: '))
else:
    count += 1
    print('Вы угадали! Число попыток = ', count)
