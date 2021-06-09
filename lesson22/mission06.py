def clear(file):
    file = file.read().split('\n')
    while '' in file:
        file.remove('')
    return file

#
file_1 = open('E:\\task\group_1.txt', 'r', encoding='utf-8')
file1 = clear(file_1)

summa = 0
for i_line in file1:
    info = i_line.split()
    summa += int(info[2])
print('Сумма очков из 1 файла : ', summa)

diff = 0
for i_line in file1:
    info = i_line.split()
    diff -= int(info[2])
print('Разность очков из 1 файла : ', diff)


file_2 = open('E:\\task\Additional_info\group_2.txt', 'r', encoding='utf-8')
file2 = clear(file_2)
compose = 1
for i_line in file2:
    info = i_line.split()
    compose *= int(info[2])

print('Произведение очков из 2 файла: ', compose)

file_1.close()
file_2.close()
