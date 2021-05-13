def operation(string):
    str = ''
    for symbol in string:
        if symbol == "*":
            break
        else:
            str += symbol
    return str


def reverse(string):
    string = string[::-1]
    return string


string = input('Введте число: ')
print(string)
mantisse = operation(string)
string = reverse(string)
method = operation(string)


print('Должно  выглядеть так: \nМантисса = ', mantisse, '\nПорядок = ', reverse(method))