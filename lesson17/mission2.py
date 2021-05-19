import random


my_list = [1 if num % 2 == 0 else num % 5 for num in range(random.randint(8, 12))]

print(my_list)
