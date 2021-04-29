import random

num = random.randint(1, 100)
print(num)
count = 0
n = 50
d = 25
x = 0
while n != num:
    print('Мое число ', n)
    x = int(input('Твоё число равно, меньше или больше, чем число?'))
    if x == 3:
        n = n - d
        print('Число меньше, чем нужно. Попробуйте ещё раз!')
    elif x == 2:
         n = n + d
         print('Число больше, чем нужно. Попробуйте ещё раз!')
    elif x == 1:
        print('Вы угадали! Число попыток = ', count)
        break
    d = int(d / 2)
    count += 1
    print(n)
else:
        print('Вы угадали! Число попыток = ', count)
