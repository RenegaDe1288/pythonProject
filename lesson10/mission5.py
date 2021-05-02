count = 0
lent = int(input('Введите количество запросов:'))
for num in range(1, lent + 1):
    print('Введите число:', num, end=' ')
    number = int(input())
    max = 0
    while number > 0:
        count += 1
        max += 1
        number = number // 10
    print('Число состоит из ', max, 'цифр')
print('Общее количество цифр в последовательности = ', count)
