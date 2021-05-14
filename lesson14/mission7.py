x = int(input('ВВедите первый год: '))
y = int(input('ВВедите второй год: '))

for num in range(x, y + 1):
    num = str(num)
    count = 0
    count2 = 0
    for sym in num:
        if sym == num[3]:
            count += 1
        if sym == num[0]:
            count2 += 1

    if count == 3 or count2 == 3:
        print(num)

y = str(1909 % 10)
print(type(y))
