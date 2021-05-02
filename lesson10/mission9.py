n =7
num =1

print('Сначала было так\n')
for y in range(n):
    for x in range(n):
        if x >= n - y:
            print(num, end='  ')
            num += 2
        else:
            print(' ', end=' ')
    print('')