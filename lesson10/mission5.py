count = 0
lent = int(input('Введите количество запросов:'))
for num in range(lent):
    number = int(input('Введите число:'))
    max = 0
    while number >0:
        count +=1
        max += 1
        number = number//10
    print('Число сотсоит из ', max, 'цифр')
print('Общее количество цифр в последовательности = ', count)