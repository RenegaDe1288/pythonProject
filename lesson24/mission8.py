import random


class Cards:

    def __init__(self, name, points):
        self.name = name
        self.points = points


class Gamers:

    def __init__(self):
        self.player_points = 0
        self.dealer_points = 0

    def info(self):
        print('У Игрока {}  очков. У Дилера {} очков '.format(self.player_points, self.dealer_points))

    def pl_count(self, card):
        self.player_points += card.points
        print('У Игрока выпала  {}  и всего  {} очков '.format(card.name, self.player_points))

    def dl_count(self, card):
        self.dealer_points += card.points
        print('У Дилера выпала  {} и всего  {} очков '.format(card.name, self.dealer_points))

    def check(self):
        if self.player_points <= 21 and self.dealer_points <= 21:
            return True
        else:
            return False


name_list = ['Двойка', 'Тройка', 'Четверка', 'Пятерка', 'Шестерка', 'Семерка', 'Восьмерка', 'Девятка', 'Десятка']
list_cards = [Cards(name, num + 2) for num, name in enumerate(name_list)]
list_cards.append(Cards('Дама', 10))
list_cards.append(Cards('Валет', 10))
list_cards.append(Cards('Король', 10))
list_cards.append(Cards('Туз', 11))

player = Gamers()

player.pl_count(random.choice(list_cards))
player.pl_count(random.choice(list_cards))
player.dl_count(random.choice(list_cards))
player.dl_count(random.choice(list_cards))

while player.check():
    answer = int(input('Игроку: Хотите взять еще карту? 1/2 :  '))
    if answer == 1:
        player.pl_count(random.choice(list_cards))
        if player.player_points > 21:
            print('Победил Дилер с очками  {} \n Игрок програл с очками {}'.format(player.dealer_points,
                                                                               player.player_points))
            break
    player.info()
    answer2 = int(input('Дилеру: Хотите взять еще карту? 1/2 :  '))
    if answer2 == 1:
        player.dl_count(random.choice(list_cards))
        if player.dealer_points > 21:
            print('Победил Игрок с очками  {} \n Дилер програл с очками {}'.format(player.player_points,
                                                                                   player.dealer_points))
            break
    elif answer and answer2 == 2:
        player.info()
        if player.player_points > player.dealer_points:
            print('Победил       Игрок с очками  {} \n Дилер програл с очками {}'.format(player.player_points,
                                                                                         player.dealer_points))
            break

        elif player.player_points < player.dealer_points:
            print('Победил      Дилер с очками  {} \n Игрок програл с очками {}'.format(player.dealer_points,
                                                                                        player.player_points))

            break
        else:
            print('Ничья', player.info())
    elif player.player_points and player.dealer_points == 21:
        print('Ничья', player.info())
