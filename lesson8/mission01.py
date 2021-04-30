
number = int(input('Введите последнее число: '))
for num in range(1, number // 2 + 1):
    num *= 2
    print('для числа: ', num, ' третья степень = ', num**3)
