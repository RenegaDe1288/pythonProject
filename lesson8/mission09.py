import random

total = random.randint(10, 21)
print('Всего секнд =  ', total)
for num in range(total + total % 2, 0, -2):
    num -= 2
    print('Осталось секунд', num)
print('Я иду искать')
