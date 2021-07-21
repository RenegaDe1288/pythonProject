def change(pos, line):
    global file_1, lines
    answer = input('Обнаружена ошибка в строке {}: {} Хотите исправить? да/нет '.format(pos + 1, line))
    if answer == 'да':
        calculation = input('Введите правильный пример: ')
        lines[pos] = calculation + '\n'
        with open('calc.txt', 'w') as file_1:
            file_1.write(''.join(lines))


def math(lines):
    all = 0
    for pos, line in enumerate(lines):
        data = line.split()
        try:
            x, y = int(data[0]), int(data[2])
            if data[1] == '+':
                all += (x + y)
            elif data[1] == '-':
                all -= (x - y)
            elif data[1] == '*':
                all *= (x * y)
            elif data[1] == '/':
                all /= (x / y)
            elif data[1] == '**':
                all **= (x ** y)
        except:
            pass
    return all


def total(lines):
    operand_list = ['/', '+', '-', '**', '*']
    for pos, line in enumerate(lines):
        try:
            data = line.split()
            if data[1] in operand_list and data[0].isnumeric() and data[2].isnumeric():
                pass
            else:
                raise ValueError
        except (ValueError, IndexError):
            change(pos, line)
    all = math(lines)
    print('Общая сумма: ', all)


with open('calc.txt', 'r') as file_1:
    lines = file_1.readlines()
    total(lines)
