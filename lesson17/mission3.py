import random


def random_number():
    team = [round(random.uniform(5.00, 8.00), 2) for _ in range(20)]
    return team


def count(t1, t2):
    lists = [1 for player in range(len(t1)) if t1[player] > t2[player]]
    return len(lists)


team_1 = random_number()
team_2 = random_number()
print(team_1)
print(team_2)

winners = [team_1[i] if team_1[i] > team_2[i] else team_2[i] for i in range(len(team_1))]
print('Количество победителей в команде №1 = ', count(team_1, team_2))
print('Количество победителей в команде №2 = ', count(team_2, team_1))

print('Победители: ', winners)
