
def summ(n):
    summ = 0
    while n > 0:
         x = n % 10
         summ += x
         n = n//10
    return summ

def count(n):
    count =0
    while n > 0:
        count += 1
        n = n //10
    return count

n = int(input('Введите число: '))
print('Сумма цифр = ', summ(n))
print('Количество цифр =  ', count(n))
print('Разность суммы чиел и количества = ', summ(n) - count(n))

