import random
count = 0

for number in range (11):
    num = random.randint(-1000, 1000)
    if num >= 0 and num % 2 == 0:
        count += 1
        print('Положительное четное число', num)
print(' Всего нужных чисел: ', count)


