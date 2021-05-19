import random

a = random.randint(10, 15)
b = random.randint(20, 30)

list_1 = [num for num in range(a, b) if num%2 == 0]
print(list_1)