players_dict = {

    1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},

    2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},

    3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},

    4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},

    5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},

    6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},

    7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},

    8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}

}

for i in players_dict.values():
    if i['team'] == 'A' and i['status'] == 'Rest':
        print('{} из команды {} отдыхает'. format(i['name'], i['team']))
    if i['team'] == 'B' and i['status'] == 'Training':
        print('{} из команды {} тренируется'. format(i['name'], i['team']))
    if i['team'] == 'C' and i['status'] == 'Travel':
        print('{} из команды {} путешествует'. format(i['name'], i['team']))


