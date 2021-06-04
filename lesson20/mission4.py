players = {

    ("Ivan", "Volkin"): (10, 5, 13),

    ("Bob", "Robbin"): (7, 5, 14),

    ("Rob", "Bobbin"): (12, 8, 2)

}

list_1 = []
for key, value in players.items():
    list_1.append(tuple(key + value))
print(list_1)


list_2 = [(key + value) for key, value in players.items()]
print(list_2)