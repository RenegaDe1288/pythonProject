import random


def mainMenu():
    choice = int(input('\nВведите во что будете играть 1 - КНБ,  2 - Угадай число:   '))
    if choice == 1:
        rock_paper_scissors()
    elif choice == 2:
        guess_the_number()
    else:
        print('Ошибка ввода.')


def rock_paper_scissors():
    print('\nВы выбрали игру: Камень\ножницы\бумага ')
    unit = int(input('\nЧто выбираете? Камень, ножницы, бумага = 1/2/3: '))
    if unit == 1:
        print('Ничья. Два камня.')
    elif unit == 2:
        print('Вы проиграли камень ломает ножницы. ')
    elif unit == 3:
        print('Вы выйграли: Бумага обрачивает камень. ')
    else:
        print('Ошибка ввода.')


def guess_the_number():
    print('\nВы выбрали игру: Угадай число ')
    xnum = random.randint(1, 100)
    print(xnum)
    num = 0
    while xnum != num:
        num = int(input('\nВведите число от 0 до 100: '))
        if num > xnum:
            print('Загаданное число меньше Вашего.')
        elif num < xnum:
            print('Загаднное число больше Вашего.')
    print('Вы отгадали число ', num)


while True:
    mainMenu()
