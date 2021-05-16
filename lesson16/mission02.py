workers = []
total = int(input(('Введите количество сотрудников: ')))
for _ in range (total):
    workers.append(int(input('Введите зарплату: ')))
print(workers)

for i in workers:
    if i == 0:
        workers.remove(i)

print('осталось сотрудников: ', len(workers))
print(workers)
print('Минимальная зарплата: ', min(workers))
print('Максимальная зарплата: ', max(workers))