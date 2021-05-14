n1 = 132.12
f2 = 156.32


def rev(n1):
    n2 = 0
    while n1 > 0:
        digit = n1 % 10
        n1 = n1 // 10
        n2 = n2 * 10
        n2 = n2 + digit
    return n2


def summ(n1, npart_1):
    npart_2 = round(n1 - int(n1), 2) * 100
    npart_2 = rev(npart_2) / 100
    print('Число с реверсом частей = ', npart_1 + npart_2)
    return npart_1 + npart_2


npart_1 = rev(int(n1))
sum1 = summ(n1, npart_1)

fpart_1 = rev(int(f2))
sum2 = summ(f2, fpart_1)

print('Сумма реверсивных чисел равна :  ', sum1 + sum2)
