def eqv(x,y,z):
    if  abs(x + y - z) < 1e-15:
       print('Сумма первых чисел равно третьему')
    else:
        print('Сумма не равна')

x = float(input('Введите первое число:  '))
y = float(input('Введите второе число:  '))
z = float(input('Введите третье число:  '))

print(x+y-z)

eqv(x,y,z)