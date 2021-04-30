import random

all_rules = random.randint(200, 202)
print('Общее количество правил = ', all_rules)
all_solders = random.randint(0, 20)
print('Количество солдат:', all_solders)
print()
push_count = 0
if all_solders <= 4:
    print('Солдат в шеренге меньше 5')
else:
    for solder in range(all_solders - 4, 0, -4):
        solder_rules = random.randint(200, 202)
        print('Солдат', solder, 'отвечает =', solder_rules)
        if solder_rules != all_rules:
            push_count += solder * 10
            print('Неправильно! Отжимайся ', solder * 10, 'раз')
        else:
            print('Молодец! Хорошо знаешь устав!')
        if all_solders <= 4:
            print('Солдат в шеренге меньше 5')
        print()
    print('Общее количество отжиманий равно ', push_count)

