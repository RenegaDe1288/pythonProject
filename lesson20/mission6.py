list1 = [10, 11, 12, 13, 4, 5, 6, 7, 8, 9]

list_3 = [tuple([num, list1[index + 1]]) for index, num in enumerate(list1) if index % 2 == 0]
print(list_3)

list_4 = [tuple([num, list1[list1.index(num)] + 1]) for num in list1[::2]]
print(list_4)
