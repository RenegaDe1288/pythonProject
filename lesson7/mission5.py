num = int(input('Введите число:'))
factorial = 1
for number in range(0, num):
    factorial = (number + 1) * factorial
    print(factorial)

