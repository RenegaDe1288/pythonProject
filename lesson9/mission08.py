import random

number = random.randint(10, 12)
step = random.randint(2, 4)
summ = 0
for num in range(3):
    print(number, end='.')
    summ += number
    number -= step
print(summ)
