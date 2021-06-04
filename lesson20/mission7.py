def sort(tuple_new):
    for i in tuple_new:
        if isinstance(i, float):
            return (tuple_new)
    else:
        list1 = list(tuple_new)
        for i in range(len(list1)):
            minimum = i
            for j in range(i + 1, len(list1)):
                if list1[j] < list1[minimum]:
                    minimum = j
            list1[minimum], list1[i] = list1[i], list1[minimum]
        return tuple(list1)
        # или просто
        # return (sorted(tuple))


tuple1 = (1, 0, 0, 2, 3.5, 5, 6, 7, 9)
tuple2 = (3, 5, 6, 8, 4, 5, 65, 6, 6, 8, 4, 6, 8, 4, 6)
print(sort(tuple1))
print(sort(tuple2))
