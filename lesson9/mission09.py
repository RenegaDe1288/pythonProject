import random

number = random.randint(1, 8)
step = 10


for num in range(number+1):
    print(number, end='-=-',)
    number += step
