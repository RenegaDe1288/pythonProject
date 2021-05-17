def counts(x):
    global new_list, count
    for i in range(len(my_list) - x, -1, -1):
        my_list.append(my_list[i])
        count += 1
        new_list.append(my_list[i])


my_list = [1, 2, 4, 5, 5, 6, 6, 5, 5, 6]
count = 0
new_list = []
print(my_list[len(my_list)-1])
if my_list[len(my_list)-1] == my_list[len(my_list)-2]:
    counts(3)
else:
    counts(2)
print(my_list)
print('Нужно дописать чисел: ', count)
print('Сами числа: ', new_list)
