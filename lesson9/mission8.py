import random

all_symbols = random.randint(12, 20)
mark = random.randint(3, 8)
print(all_symbols, mark)
print('*' * ((all_symbols - mark) // 2), mark * '!', '*' * ((all_symbols - mark) // 2))
part = (all_symbols - mark) // 2
summ = ''
for num in range(all_symbols):
    if num < part:
        summ += '*'
    if part <= num < part+mark:
        summ += '!'
    if num >= mark+part:
        summ += '*'
print(summ)
