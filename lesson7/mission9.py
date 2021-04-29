import random
count = 0
prev_balance = 0
for month in range(1, 11):
    balance = random.randint(20000, 30000)
    if prev_balance < balance:
        print('Все Хорошо! Зарплата растет!')
    if prev_balance > balance:
        count  = 1
        print('Печально, похоже денег не хватает')
    prev_balance = balance
    print(prev_balance)
if count == 1:
    print('Зарплата идет неравномерно')