while True:
    x= float(input('Введите координату х '))
    y = float(input('Введите координату у '))
    if  0 < x < 1 and 0 < y < 1:
        break
    else:
        print('Введите допустимыe значения координат от 0 до 1')

print('Фигура находится в точке = ', int(x*10), int(y*10))

