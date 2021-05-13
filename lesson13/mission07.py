budget = float(input('Введите бюджет страны: '))
tax = float(input('Введите новые поступления: '))
c= abs(budget-tax)
d = budget-tax-budget

print(c,d)
def all_tax(budget, tax):
    if abs(budget+tax-budget) > 1e-15:
        c = abs(budget-tax)
        print('Бюджет увеличлся')
    else:
        print('Бюджет не увеличлся')

all_tax (budget,tax)
