conteiners = []
new_conteiners = []
total = int(input('Введите количество контейнеров: '))
for _ in range(total):
    conteiners.append(int(input('Введите вес контейнера: ')))

print(conteiners)

x = int(input('Введите массу новго контейнера: '))

for i in range(len(conteiners)):
    if conteiners[i] >= x:
        new_conteiners.append(conteiners[i])
    elif conteiners[i] < x:
        new_conteiners.append(x)
        d = i
        print('Номер нового контейнера = ', i+1)
        break
for i in range(d ,len(conteiners)):
    new_conteiners.append(conteiners[i])

print(new_conteiners)



