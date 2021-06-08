def pack(list_1):
    new_list = []
    for num in list_1:
        if isinstance(num, int):
            new_list.append(num)
        else:
            internal_list = pack(num)
            for value in internal_list:
                new_list.append(value)
    return new_list


nice_list = [1, [[[[[[2]]]]]], [3, 4], [[5, 6, 7], [8, 9, 10]], [[[11, 12, 13]], [14, 15], [16, 17, 18]]]

print(pack(nice_list))
