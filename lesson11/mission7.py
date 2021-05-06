import math
while  True:
    x = float(input('введите положение коня  х '))
    y = float(input('введите положение коня  у '))
    x_1 = float(input('введите положение   x '))
    y_1 = float(input('введите положение   у '))
    count = 0
    if abs(round(math.ceil((x_1 - x)*10),1)) == 2 and abs(round(math.ceil((y_1 - y)*10),1)) == 1:
        count+=1
    if abs(round(math.ceil((x_1 - x)*10),1)) == 1 and abs(round(math.ceil((y_1 - y)*10),1)) == 2:
        count+=1
    if count >= 1:
         print('Конь может ходить')
         print()
    else:
        print('Конь не может ходить')

    print(abs(round(math.ceil((x_1 - x)*10),1)))
    print(abs(round(math.ceil((y_1 - y)*10),1)))


