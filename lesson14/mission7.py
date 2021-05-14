x = int(input('ВВедите первый год: '))
y = int(input('ВВедите второй год: '))

for num in range(x, y+1):
    num = str(num)
    count = 0
    y = num[3]
    for sym in num:
        if sym == y:
            count+=1
        if count == 3:
            print(num)


y = str(1909%10)
print(type(y))