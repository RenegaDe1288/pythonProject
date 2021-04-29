import random
total_balance = 0

for month in range(1, 13):
    balance = random.randint(20000, 30000)
    total_balance += balance
    print(total_balance)
    mid_balance = round(total_balance / month)
    print('Месяц =', month, 'Средняя зарплата =', mid_balance)
