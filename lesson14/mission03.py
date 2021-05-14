z = input('Введите что вы хотите сделать: ')


num = int(input('Введите количество операндов: '))

for number in range(1, num+1):
    x = int(input('Введите цифру: '))
    if number == 1:
        c = x
    else:
        if z == '+':
            c = c+x
        elif z == '-':
            c= c-x
        elif z =='*':
            c = c*x
        elif z == '/':
            c = c/x

print('Значение равно ', c)