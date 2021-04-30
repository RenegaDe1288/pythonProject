import random

all_credits = random.randint(20, 40)
print('Всего должников =  ', all_credits)
summ_credit = 0
for num in range(0, all_credits, 5):
    print('Должник = ', num)
    credit = random.randint(1000, 10000)
    print('Должен ', credit)
    print()
    summ_credit += credit
print('Сумма задодженности', summ_credit)
