incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

all_incomes = sum(incomes.values())
print('Общий доход составляет:', all_incomes)
minimum = min(incomes.values())
for price in incomes:
    if incomes[price] == minimum:
        print('Минимальный доход от {} и он составляет: {}'.format(price, minimum))
        incomes.pop(price)
        print(incomes)
        break
