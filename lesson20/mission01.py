import random

tuple_1 = tuple([random.randint(0, 5) for _ in range(10)])
tuple_2 = tuple([random.randint(-5, 0) for _ in range(10)])
tuple_3 = tuple_1 + tuple_2
print('Третий кортеж:', tuple_3)
print('Количество нулей в третьем кортеже: ', tuple_3.count(0))
