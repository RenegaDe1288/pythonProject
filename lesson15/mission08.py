new_list = list(input('Введите строку: '))
position_number = 3
n_list = []
count = 0
print('Символ слева: ', new_list[position_number-2])
print('Символ слева: ', new_list[position_number])

for index in range(position_number-2, position_number+1):
    if new_list[index] == new_list[position_number-1]:
        count += 1

if count == 1:
    print('Таких же символов нет')
elif count == 2:
    print('Есть 1 такойже символ ')
elif count == 3:
    print('Есть 2 одинаковых соседа')
