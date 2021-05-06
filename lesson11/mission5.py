import math

earth = 10.8321 * 10 ** 11
planet = float(input('введите радиус Случайной планеты: '))
v_plan = math.pi * (4 / 3) * planet ** 3
print(v_plan)
if v_plan > earth:
    print('Объём планеты Земля больше в ', round(v_plan / earth, 3), 'раз')
else:
    print('Объём планеты Земля меньше в ', round(earth / v_plan, 3), 'раз')
