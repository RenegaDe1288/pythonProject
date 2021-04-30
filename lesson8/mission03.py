number = int(input('Введите число: '))
new = 1
for num in range(1, ((number + 1) // 2) + 1):
    print('Квадрат числа: ', new, 'равен ', new ** 2)
    new = 2 * num + 1
