def remove(list, num):
    for i in list:
        if i == num:
            a.remove(i)
    return a


a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a.extend(b)
print('Количество цифр пять: ', a.count(5))
a = remove(a, 5)
print(a)

a.extend(c)
print('Количество цифр три: ', a.count(3))


print(a)
