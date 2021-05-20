import random
def miss(list, n):
    L_i = random.randint(1, n - 1)
    R_i = random.randint(L_i + 1, n)
    print('Сбиты палки с номера ', L_i, 'по номер ', R_i)
    sticks = ['.' if L_i <= x + 1 <= R_i else list[x] for x in range(n)]
    view(sticks)
    return sticks


def view(list):
    for i in list:
        print(i, end='')
    print()


n = random.randint(10, 20)
k = random.randint(2, 4)

sticks = ['|' for _ in range(1, n + 1)]
view(sticks)

for kicks in range(k):
    print('Бросок: ', kicks+1, end=' ')
    sticks = miss(sticks, n)
