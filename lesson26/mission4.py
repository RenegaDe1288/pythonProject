import random


def q_sequence(list, n):
    if list[0] and list[1] == 1:
        list_1 = list
        for i in range(2, n -2):
            list_1.append(list_1[i - list_1[i - 1]] + list_1[i - list_1[i - 2]])
        yield list_1
    else:
        return print('Ошибка в списке')


list = [1, 1]
num = random.randint(20, 40)

gen_list = (q_sequence(list, num))
for i in gen_list:
    print(i, end=' ')
