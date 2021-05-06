import random
import math

x = random.randint(-5, 10)
y = random.randint(-5, 10)
print(x, y)
s = (x + y + abs(y - x)) / 2
print(int(s))
