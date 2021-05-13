def max(x, y):
    if x > y:
        return x
    else:
        return y


x = int(input('Введите  1 число: '))
y = int(input('Введите  2 число: '))
z = int(input('Введите  3 число: '))
x = max(x, y)
x = max(x, z)
print('Наибольшее число:  ', x)
