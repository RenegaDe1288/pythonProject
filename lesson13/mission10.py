def count(s, a, i):
    year = 1
    global new
    while year <= new:
        pers = s * i
        main = a - pers
        # print('коэффициэнт = ', k)
        print('\nОстаток долга = ', s)
        print('         общая сумма погашения за год ', year, ' = ', round(a, 3))
        print('Выплачено процентов = ', round(pers, 3))
        print('Выплачено тело кредита = ', round(main, 3))
        s = round(s - main,3)
        year += 1
    return s



def ak(s, i, n):
    k = (i * (1 + i) ** n) / ((1 + i) ** n - 1)
    a = k * s
    return a


s = 40000000
i = 0.06
n = 5
new = 3

a = ak(s, i, n)
s = count(s, a, i)
print('\nОстаток долга = ', s)

i = 0.1
new = 4
new = n - 3 + new
a = ak(s, i, new)
s = count(s, a, i)
print('\nОстаток долга = ', s)


