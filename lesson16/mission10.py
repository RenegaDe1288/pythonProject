my_list = [1, 2, 4, 5, 5]
count = 0
for i in range(len(my_list) - 1, -1, -1):
    my_list.append(my_list[i])
    count += 1
print(my_list)
print('Нужно дописать чисел: ', count)
