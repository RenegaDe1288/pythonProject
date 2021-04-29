number = int(input('Введите число: '))
count = 0
while number % 10 != 0:
    count += 1
    number = number // 10
print('количество знаков = ', count)
