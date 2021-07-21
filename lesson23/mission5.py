with open('calc.txt', 'r') as file_1:
    total = 0
    for pos, line in enumerate(file_1):
        data = line.split()
        try:
            x, y = int(data[0]), int(data[2])
            if data[1] == '+':
                total += (x + y)
            elif data[1] == '-':
                total += (x - y)
            elif data[1] == '*':
                total += (x * y)
            elif data[1] == '/':
                total += (x / y)
            elif data[1] == '**':
                total += (x ** y)
            else:
                print('Операция не найдена: строка: ', pos + 1)
        except SyntaxError:
            print('Невозможно определить операцию: строка: ', pos + 1)
        except TypeError:
            print('Невозможно провести операцию между строками: строка: ', pos + 1)
        except ValueError:
            print('Невозможно определить операнд: строка: ', pos + 1)
        except IndexError:
            print('В задаче менее 3 операндов: строка: ', pos + 1)
    print('Общая сумма: ', total)
