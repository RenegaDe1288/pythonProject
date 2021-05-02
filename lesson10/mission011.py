count = 0
for num in range(7):
    number = int(input('Введите число'))
    while number > 0:
        if number % 10 > 5:
            count += 1
        number = number // 10
print(count)
