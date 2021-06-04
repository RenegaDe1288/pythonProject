# play = {'jack': [(1, 69485), (6, 95715)],
#         'qwerty': [(2, 95715), (5, 197128)],
#         'Alex': [(3, 95715), (7, 93289), (8, 95715)],
#         'M': [(4, 83647), (9, 54)],
#         }


def win(players, n):
    maximum = 0
    for key, data in players.items():
        for num in data:
            if num[1] > maximum:
                position, maximum, winner = num[0], num[1], key
            elif num[1] == maximum and num[0] < position:
                position, maximum, winner = num[0], num[1], key
    print('{} место занял игрок {} количеством очков {}  в игре номер {}'.format(n + 1, winner, maximum, position + 1))
    del (players[winner])


games = int(input('Введите количество игр: '))

play = {}

for i in range(games):
    print('{} запись'.format(i + 1))
    points = input('Введите имя и грока  и очки ').split()
    if play.get(points[0]):
        play[points[0]].append((i, int(points[1])))
        print(play)
    else:
        play.update({points[0]: [(i, int(points[1]))]})

print(play)

for number in range(len(play)):
    win(play, number)
