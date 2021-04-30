import random

number = random.randint(5, 6)
print(number)
s = 1
for num in range(1, number + 1):
    if num % 2 != 0:
        s = s - (1 / 2 ** num)
        print('На шаге = ', num, ' ---- Число равно', s)
    else:
        s = s + 1 / 2 ** num
        print('На шаге = ', num, ' ++++ Число равно', s)
summ = s + (-1 ** number) * (1 / 2 ** number)
print(summ)

