import random

violation = 0

for zone in range(30, 36):
    mans = random.randint(0, 20)
    print('Людей в ', zone, 'секторе: ', mans)
    if mans > 10:
        violation += 1
        print('Нарушение! Слишком много людей в секторе!')
    else:
        print('Всё спокойно.')
print('Зафиксировано: ', violation, 'нарушений')
