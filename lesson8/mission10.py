import random

boys = random.randint(7, 9)
girls = random.randint(7, 20)
print('Мальчиков =', boys)
print('Девочек = ', girls)

answer = ''
if girls > 2 * boys or boys > 2 * girls:
    print('Рассадить детей невозможо!')
elif girls > boys:
    k = girls - boys
    for gbg in range(k):
        answer += 'gbg'
    for gb in range(1, girls - k):
        answer += 'gb'
elif girls < boys:
    k = boys - girls
    for bgb in range(k):
        answer += 'bgb'
    for gb in range(1, boys - k):
        answer += 'bg'
print(answer)
