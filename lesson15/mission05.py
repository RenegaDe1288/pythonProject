nums_list = []

N = int(input('Кол-во чисел в списке: '))

for _ in range(N):
    num = int(input('Очередное число: '))
    nums_list.append(num)

degree = int(input('Введите делитель: '))
summ = 0
for i in nums_list:
    if i % degree == 0:
        summ += nums_list.index(i)
print('Сумма элементов списка =', summ)
