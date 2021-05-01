num = int(input('Введите число  '))
for a in range(num+1):
    for b in range(0, 11, 2):
        print(b + a, end='\t')
    print()
