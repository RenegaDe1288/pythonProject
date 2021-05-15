my_list = [1, 4, -3, 0, 10]
k = int(input('Выберите сдвиг: '))
new_list = []
print('Изначальный список: ', my_list)
for i in range(len(my_list)):
    new_list.append(my_list[i - k])
print('Новый список: ', new_list)
