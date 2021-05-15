cells = []
total = int(input(('Введите количество клеток: ')))
for _ in range (total):
    cells.append(int(input('Введите значение клетки: ')))

bad_cells = []
for index in range(len(cells)):
    if cells[index] < index+1:
        bad_cells.append(cells[index])


print('Неподходящие значения: ', end='')
for i in range(len(bad_cells)):
    print(bad_cells[i], end=' ')
