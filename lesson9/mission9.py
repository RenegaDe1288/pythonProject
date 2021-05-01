milk = 0
all_milk = 0
for num in range(1, 11):
    text = input('Введите текст:  ')
    if text == 'a':
        milk = num * 2
        all_milk += milk
        print(' в стойле = ', num, 'молока надоено', milk)
    if text == 'b':
        continue
print('Количество молока =  ', all_milk)