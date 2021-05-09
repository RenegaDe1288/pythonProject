x = 2
count = 0
while x != 0:
    x = x/2
    if x == 0:
        print('Минимально возможное число = ', newx)
    newx = x
    count += 1
print('Общее количество делений = ', count)
