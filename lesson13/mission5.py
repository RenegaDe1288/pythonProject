import math

number = int(input('введите точность расчета: '))
summ = 0
for  num in range(0, number+1):
    summ += 1/math.factorial(num)
print(summ)

number =float(input('введите точность расчета: '))
summ = 0
x = 1
i = 0
while number < x:
    x = 1/math.factorial(i)
    summ += x
    i += 1
print(summ)
