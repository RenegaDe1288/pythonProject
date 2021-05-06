import math

x = float(input('Введите число  '))
x = abs(math.floor(x) - x)
print(x)
print(math.floor(x * 10))
