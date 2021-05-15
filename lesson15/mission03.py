count = int(input('Введите количество сотрудников: '))
list = []
for num in range(count):
    id = int(input('Введите ID сотрудника '))
    list.append(id)
searchID = int(input('Какой ID ищем? '))
for num in list:
    if num == searchID:
        print('Сотрудник на месте')
        count = 1
        break
if count != 1:
        print('Сотрудник не работает')