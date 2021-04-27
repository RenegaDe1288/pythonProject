money = int(input('Введите сумму дохода: '))
tax = 0
if 0 < money <= 10000:
    tax = money * 0.13
    print(tax)
elif 10000 < money <= 50000:
    tax = (money - 10000) * 0.2 + 10000 * 0.13
    print(tax)
elif 50000 < money:
    tax = (money - 50000) * 0.3 + 40000*0.2 + 10000 * 0.13
    print(tax)
else:
    print("Бомжара")
