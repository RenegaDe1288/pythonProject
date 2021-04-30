import  random

educational_grant = random.randint(1000,2000)
expenses = random.randint(educational_grant, educational_grant + 200)
total_money = 0
money = 0
print('стипендия = ', educational_grant)
print(' Расходы = ', expenses)
for month in range(1, 11):
    if month != 1:
        expenses = round(expenses * 0.03 + expenses)
    total_money = expenses - educational_grant
    money += total_money
    print('Расходы за месяц', month, 'составили ', expenses)
    print('Перерасход за месяц', total_money)
    print()
print('Родители должны выслать для того чтобы их мальчик не сдох = ', money)