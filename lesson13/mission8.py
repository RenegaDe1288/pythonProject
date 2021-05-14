d_from = 0
d_to = 4

max_danger = float(input('Максимальный уровень опасности: '))
x = d_from + (d_to - d_from) / 2
d = x ** 3 - 3 * x ** 2 - 12 * x + 10

if max_danger < 0:
    print('Некорректный ввод')
else:
    while abs(d) > max_danger:
        if d > 0:
            d_from = x
        else:
            d_to = x
        x = d_from + (d_to - d_from) / 2
        d = x ** 3 - 3 * x ** 2 - 12 * x + 10

print('Глубина безопасной кладки:', x)


