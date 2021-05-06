import random
import math

a= random.randint(1,4)
b= random.randint(1,4)
c= random.randint(1,4)
print( a,b,c)
discr = b ** 2 - 4 * a * c
print(discr)
if discr > 0:
    x_1 = (-b+math.sqrt(discr))/(2*a)
    x_2 = (-b-math.sqrt(discr))/(2*a)
    print(x_2, x_1)
if discr == 0:
    x_1 = -b/(2*a)
    print(x_1)
if discr < 0:
    print('решения нет')

print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discr = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discr)

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print(x1, x2)
elif discr == 0:
    x = -b / (2 * a)
    print(x)
else:
    print("Корней нет")

print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

discr = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % discr)

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif discr == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
else:
    print("Корней нет")