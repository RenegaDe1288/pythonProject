my_list = [1, 2, 3, 4, 5]
start = 0
while len(my_list) > 1:
    print('Остались игроки: ', my_list)
    print('Начало счета с номера: ', my_list[start])
    for num in range(start, len(my_list)):
        number = int(input('Выбывает человек под номером: '))
        start = my_list.index(number)
        my_list.remove(number)
        break
    if start == len(my_list):
        start = 0


print('Победитель: ', my_list[0])
