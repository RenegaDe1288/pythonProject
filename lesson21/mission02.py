def power(a, n):
    if n == 1:
        return a
    des = a * power(a, n - 1)
    return des


float_num = float(input('Введите вещественное число: '))
int_num = int(input('Введите степень числа: '))

print(float_num, '**', int_num, '=', power(float_num, int_num))