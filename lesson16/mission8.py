my_list = [1, 2, 3, 4, 5]
start = 1
while len(my_list) > 1:
    if start == len(my_list):
        start = 0
    for num in range(start, len(my_list)):
        number = int(input('Выбывает человек под номером: '))
        start = my_list.index(number)
        my_list.remove(number)
        break
    print('Начало счета с номера: ', my_list[start-1])
    print('Остались игроки: ', my_list)

print('Победитель: ', my_list)
