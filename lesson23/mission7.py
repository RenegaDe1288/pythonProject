# def change(pos, line):
#     global file_1, lines
#     answer = input('Обнаружена ошибка в строке {}: {} Хотите исправить? да/нет '.format(pos + 1, line))
#     if answer == 'да':
#         data1 = input('Введите правильный пример: ')
#         lines[pos] = data1 + '\n'
#         with open('calc.txt', 'w') as file_1:
#             file_1.write(''.join(lines))
#     else:
#         pass
#
#
# with open('calc.txt', 'r') as file_1:
#     while True:
#         total = 0
#         lines = file_1.readlines()
#         for pos, line in enumerate(lines):
#             data = line.split()
#             try:
#                 x, y = int(data[0]), int(data[2])
#                 if data[1] == '+':
#                     total += (x + y)
#                 elif data[1] == '-':
#                     total -= (x - y)
#                 elif data[1] == '*':
#                     total *= (x * y)
#                 elif data[1] == '/':
#                     total /= (x / y)
#                 elif data[1] == '**':
#                     total **= (x ** y)
#                 else:
#                     print('Операция не найдена: строка: ', pos + 1)
#                     change(pos, line)
#             except SyntaxError:
#                 print('Невозможно определить операцию: строка: ', pos + 1)
#                 change(pos, line)
#             except ValueError:
#                 print('Невозможно определить операнд: строка: ', pos + 1)
#                 change(pos, line)
#             except IndexError:
#                 print('В задаче менее 3 операндов: строка: ', pos + 1)
#                 change(pos, line)
#         break
#     print('Общая сумма: ', total)
#

def change(pos, line,total):
    global file_1, lines
    answer = input('Обнаружена ошибка в строке {}: {} Хотите исправить? да/нет '.format(pos + 1, line))
    if answer == 'да':
        data1 = input('Введите правильный пример: ')
        lines[pos] = data1 + '\n'
        with open('calc.txt', 'w') as file_1:
            file_1.write(''.join(lines))
        with open('calc.txt', 'r') as file_1:
            lines = file_1.readlines()
            total = math(lines)
            return total
    else:
        return total


def math(lines):
    total = 0
    for pos, line in enumerate(lines):
        data = line.split()
        try:
            x, y = int(data[0]), int(data[2])
            if data[1] == '+':
                total += (x + y)
            elif data[1] == '-':
                total -= (x - y)
            elif data[1] == '*':
                total *= (x * y)
            elif data[1] == '/':
                total /= (x / y)
            elif data[1] == '**':
                total **= (x ** y)
            else:
                print('Операция не найдена: строка: ', pos + 1)
                total = change(pos, line,total)
        except (ValueError, IndexError):
            print('Невозможно определить операнд: строка: ', pos + 1)
            total = change(pos, line,total)
    return total


with open('calc.txt', 'r') as file_1:
    lines = file_1.readlines()
    total = math(lines)
    print('Общая сумма: ', total)

