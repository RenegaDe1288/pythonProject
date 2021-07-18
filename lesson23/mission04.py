file = open('people.txt','r')
total = 0
for line in file:
    line = line.removesuffix('\n')
    if len(line) > 3:
        total += len(line)
    else:
        raise BaseException('Количество символов в имени меньше или равно 3')
print(total)
file.close()