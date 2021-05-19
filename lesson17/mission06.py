import random

squad_1 = [random.randint(50, 80) for _ in range(10)]
squad_2 = [random.randint(30, 60) for _ in range(10)]
print(squad_1, '\n', squad_2)
squad_3 = ['Погиб' if squad_1[i] + squad_2[i] > 100 else 'Выжил' for i in range(10)]
print('Третий отряд: ', squad_3)
print('Выжило: ', squad_3.count('Выжил'), 'Померло: ', squad_3.count('Погиб'))
