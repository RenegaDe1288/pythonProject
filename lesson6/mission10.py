import random

num = random.randint(1, 100)
print(num)
count = 0
start = 50
divisor = 25
comp_num = 0
while start != num:
    print('Мое число ', start)
    comp_num = int(input('Твоё число равно, меньше или больше, чем число?'))
    if comp_num == 3:
        start = start - divisor
        print('Число меньше, чем нужно. Попробуйте ещё раз!')
    elif comp_num == 2:
         start = start + divisor
         print('Число больше, чем нужно. Попробуйте ещё раз!')
    elif comp_num == 1:
        print('Вы угадали! Число попыток = ', count)
        break
    divisor = int(divisor / 2)
    count += 1
    print(start)
else:
        print('Вы угадали! Число попыток = ', count)
