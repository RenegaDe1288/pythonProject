dogs_point = []
N = int(input('Кол-во собак в списке: '))

for _ in range(N):
    num = int(input('Введите очки собаки: '))
    dogs_point.append(num)

maximum = dogs_point[0]
minimum = dogs_point[0]
min_index = 0
max_index = 0


for i in dogs_point:
    if maximum < i:
        maximum = i
        max_index = dogs_point.index(i)
    if minimum > i:
        minimum = i
        min_index = dogs_point.index(i)
print('Максимальное очко в списке:', maximum, ' с индексом: ', max_index)
print('Минимальное очко в списке:', minimum, ' с индексом: ', min_index)

dogs_point[max_index] = minimum
dogs_point[min_index] = maximum

print('Новый список очков собак = ', dogs_point)
