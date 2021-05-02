n =7
num =0

print('Сначала было так\n')
for y in range(n):
    num = y
    for x in range(n):
        if x >= n - y-1:
            print(y+num+1, end='  ')
            num += 2
        else:
            print(' ', end=' ')
    print('')