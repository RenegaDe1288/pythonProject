def new_list(index):
    list1 = [x for x in range(index, index+9, 4)]
    return list1


my_list = [new_list(x) for x in range(1, 5)]

print(my_list)