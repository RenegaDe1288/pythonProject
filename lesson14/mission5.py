import random

n = random.randint(2,170)
print(n)
min = n
for num in range(n+1, 1, -1):
    if n%num == 0:
        if num <= min:
            min = num
print('Наименьший делитель, отличный от единицы: ', min)