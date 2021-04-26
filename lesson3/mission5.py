minutes = int(input('Ввведите количество минут: '))
hours = minutes // 60
rest = minutes % 60
print('В ', minutes, 'минутах: ', hours, 'часов', rest, 'минут')
