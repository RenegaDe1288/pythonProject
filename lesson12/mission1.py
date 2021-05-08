

def summa_n():
    summ = 0
    for num in range (1, n + 1):
        summ += num
    print('Я знаю, что сумма чисел от ', 1, 'до ', 5, 'равна ', summ)


while True:
    n = int(input('Введите число: '))
    summa_n()
