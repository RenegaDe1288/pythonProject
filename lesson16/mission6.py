a = [1, 2, 3]
b = [2, 4, 6, 3, 3, 2, 1]

a.extend(b)

print(a)

for i in a:
    x = a.count(i)
    for num in range(a.count(i) - 1):
        a.remove(i)
print('Новый список: ', a)
