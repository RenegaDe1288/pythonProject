num = int(input('Введите число: '))
for a in range(1,num+1):
    for b in range(1,num+1):
        if b%3==0:
            print(b, end='\t')
        else:
            print(a, end='\t')
    print()