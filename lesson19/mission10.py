text = input('Введите строку: ')
new_str = [symbol for symbol in text]
new_set = set(new_str)
count = 0
for i in new_set:
    if new_str.count(i) % 2 != 0:
        count += 1
    if count > 1:
        print('Нельзя сделать палиндромом')
        break
else:
    print('Можно сделать палиндромом')
