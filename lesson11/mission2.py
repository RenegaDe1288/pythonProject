import math
num = int(input('Введите количество цифр'))

for number in range(num):
    x = float(input('Введите число'))
    if x > 0:
        print(math.ceil(x))
        print('log(x) = ', math.log(math.ceil(x)))
    else:
        print(math. floor(x))
        print('exp (x) = ', math.exp(math.floor(x)))
