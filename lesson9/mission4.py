import random

rows = random.randint(5, 6)
places = random.randint(7, 8)
metres = random.randint(2, 4)
print('рядов: ', rows, '\nмест:  ', places, '\nметров: ', metres)

for row in range(rows):
    print('-'* places, '*' * metres, '-' *places)


