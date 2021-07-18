log_file = open('log.txt', 'w', encoding='utf - 8')
with open('people.txt', 'r') as file:
    total = 0
    my_list = file.readlines()
    for pos, string in enumerate(my_list):
        string = string.removesuffix('\n')
        try:
            if len(string) > 3:
                total += len(string)
            else:
                raise BaseException
        except BaseException:
            log_file.write('\nВ слове {} в строке {} меньше трех букв'.format(string, pos + 1))
    print('Всего букв в строках: ', total)
log_file.close()