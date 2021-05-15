def sort(my_list):
    for n in range(int(len(my_list)/2)):
        min = my_list[n]
        for i in range(len(my_list)):
            if my_list[i] < min:
                min = my_list[i+n]
                index_min = i+n
        my_list[index_min] = my_list[n]
        my_list[n] = min
    return my_list


my_list = [1,4,-3,0,10,15,-10]

my_list = sort(my_list)
print(my_list)


