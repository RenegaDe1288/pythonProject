num = int(input('Введите число'))
for row in range(1, num + 1):
    for col in range(1, num + 1):
        if row >= col:
            print(row, end=' ')
    print()
