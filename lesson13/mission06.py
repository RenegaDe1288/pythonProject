def exp(number):
    count = 0
    while number > 10:
        number = number//10
        count += 1
    return count


n = int(input('Введите число: '))

count = exp(n)

print('Формат плавающей точки: ', 'x = ', n/(10**count), '*', 10,'**', count)


