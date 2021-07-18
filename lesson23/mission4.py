def check(my_list, pos):
    if len(my_list) != 3:
        bad_log.write('\nСтрока {} == {} НЕ присутствуют все три поля: ValueError.\n'.format(pos, line))
    elif not my_list[0].isalpha():
        bad_log.write('\nСтрока {} == {} Поле имени содержит НЕ только буквы: NameError.\n'.format(pos, line))
    elif '@' and '.' not in my_list[1]:
        bad_log.write('\nСтрока {} == {} Поле «Имейл» НЕ содержит @ и .(точку): SyntaxError.\n'.format(pos, line))
    elif not 10 <= int(my_list[2]) < 100:
        bad_log.write(
            '\nСтрока {} == {} Поле «Возраст» НЕ является числом от 10 до 99: ValueError.\n'.format(pos, line))
    else:
        good_log.write(line)


bad_log = open('registrations_bad.log', 'w', encoding='utf-8')
good_log = open('registrations_good.log', 'w', encoding='utf-8')
with open('registrations.txt', 'r', encoding='utf-8') as file_1:
    for pos, line in enumerate(file_1):
        my_list = line.split()
        check(my_list, pos)
bad_log.close()
good_log.close()
