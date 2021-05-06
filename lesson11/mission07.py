import math
a = int(input('Введите сторону  треугольника а '))
b = int(input('Введите сторону  треугольника b '))
c = int(input('Введите сторону  треугольника c '))
p = (a+b+c)/2
squre = math.sqrt((p*(p-a)*(p-b)*(p-c)))

print('Площадь треугольника равна  ', squre)
