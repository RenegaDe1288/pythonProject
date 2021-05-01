num = int(input('Введите число  '))
for a in range(1, num+1):
    for b in range(1, a):
        print(b, end='\t')
    print()
