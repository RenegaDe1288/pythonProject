import  math
low_temp = int(input('Введите нижнюю границу темепературы: '))
high_temp = int(input('Введите верхнюю границу темепературы: '))
step_temp = int(input('Введите шаг темепературы: '))
print('C    F')
for temp in range(low_temp, high_temp+step_temp, step_temp):
    if temp >= high_temp:
        print(high_temp, ' ', int(high_temp * 1.8 + 32))
        break
    print(temp, end='   ')
    for far in range(temp, temp + 1):
        farenheit = (temp * 1.8) + 32
        print(int(farenheit))

