string = input('Введте число: ')
mantisse = ''
method = ''
print(string)


def reverse(number):
    x2 = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        x2 = x2 * 10
        x2 = x2 + digit
    return x2


for symbol in string:
    if symbol == "*":
        break
    else:
        mantisse += symbol


def reverse(string):
    string = string[::-1]
    return string

string = reverse(string)

for symbol in string:
    if symbol == "*":
        break
    else:
        method += symbol
print('Должно  выглядеть так: \nМантисса = ', mantisse, '\nПорядок = ', reverse(method))