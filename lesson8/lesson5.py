import random

begin_nun = random.randint(2, 3)
end_num = random.randint(9, 20)
print('Начала отрезка = ', begin_nun)
print('Конец отрезка  = ', end_num)
step = int(input('Введите отрицательный шаг: '))
for x in range(end_num, begin_nun-1, step):
    y = x ** 3 + 2 * x ** 2 + 4 * x + 1
    print('В точке', x, 'функция равна ', y)
