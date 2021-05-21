text = input('Введите строку: ')
test = input('Введите проверочную строку: ')

list1 = [x for x in text]

for x in range(len(list1)):
    list1 = [list1[-1]] + list1[:-1]
    if test == ''.join(list1):
        print('Первая строка получается из второй со сдвигом', x + 1)
        break
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')
