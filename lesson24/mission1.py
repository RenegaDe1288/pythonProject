import random


class Fighters:

    def __init__(self, index, health=100):
        self.name = index
        self.health = health
        print('Боец {} имеет {} здоровья'.format(self.name, self.health))

    def death(self, player):
        print('\tБоец {} выбыл из соревнования'.format(self.name))
        list_of_fight.remove(player)

    def fight(self, player):
        player.health -= random.randint(15, 30)
        print('Боец {} Получил урон! Теперь у него: {} здоровья'.format(player.name, player.health))
        if player.health <= 0:
            player.death(player)
            return True


names_list = ['Yoshimitsu', 'ПОЛЕНО', 'Утка КРЯ-КРЯ', 'Johny Sins']
list_of_fight = [Fighters(fighter) for fighter in names_list]

while len(list_of_fight) > 1:
    battle_list = random.sample(list_of_fight, k=2)
    player, player_2 = battle_list[0], battle_list[1]
    print('\n\t!!!!Битва между {} и {}!!!!\n'.format(player.name, player_2.name))
    if player.fight(player):
        continue
    else:
        player_2.fight(player_2)

print('\n\tПобедитель: {}  с очками здоровья: {}'.format(list_of_fight[0].name, list_of_fight[0].health))
