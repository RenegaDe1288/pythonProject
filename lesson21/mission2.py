tuple_1 = (1, 2, 3, 4, 66, 8, 8, 8, 8, 8, 9)
list_1 = [7, 8, 9, 6, 5, 7, 6]
string_1 = 'gfgfgggfgffdfdf'


# s = zip(r,t)
# print(list(s))


# count = 0
# list2 = [(r[i],t[i]) for i in range(min(len(t),len(r)))]
# print(list2)


def zip(object_1, object_2, i):
    try:
        answer.append((object_1[i], object_2[i]))
        zip(object_1, object_2, i + 1)
    except:
        IndexError
    return answer


answer = []
print(zip(tuple_1, string_1, 0))
