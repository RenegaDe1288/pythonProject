import random

boys = random.randint(7, 9)
girls = random.randint(7,11)
print('Мальчиков =', boys)
print('Девочек = ', girls)
if girls -  boys != 0 and (boys-girls > 2 or girls - boys > 2):
    print('Рассадить детей невозможо!')
elif boys == girls:
    for place in range (1, girls + boys+1):
        if place%2 == 1:
            print('b')
        else:
            print('g')
elif boys - girls == 1:
    for place in range (1, girls + boys):
        if place%2 == 1:
            print('b')
        else:
            print('g')
    print('b')
elif girls - boys == 1:
    for place in range (1, girls + boys):
        if place%2 == 1:
            print('g')
        else:
            print('b')
    print('g')
elif girls - boys == 2:
    for place in range (1, girls + boys):
        if place%2 == 1:
            print('g')
        else:
            print('b')
        if place == 3:
            print('g')
elif boys - girls == 2:
    for place in range (1, girls + boys):
        if place%2 == 1:
            print('b')
        else:
            print('g')
        if place == 3:
            print('b')


