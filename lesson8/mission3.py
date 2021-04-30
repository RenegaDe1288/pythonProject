import random

all_seconds = random.randint(2, 3)
print('Всего Секунд ', all_seconds)
summ_credit = 0
for num in range(all_seconds, -1, -1):
    if num == 0:
        print('Бомба РВАНУЛА!!!')
        break
    print('Осталось секунд ', num)
    want = random.randint(0, 1)
    if want == 0:
        print('Вы решили ничего не делать! таймер продолжает работать.')
        continue
    elif want == 1:
        print('Бомба обезврежена!!!')
        break

