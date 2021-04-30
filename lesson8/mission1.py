import random

cereal = random.randint(20, 100)
print('Всего кг гречки =  ', cereal)
for num in range(1, 10):
    if cereal >= 4:
        cereal -= 4
        print('Месяц = ', num)
        print('На конец месяца Осталось гречки', cereal)
    else:
        print('Вы здохли на месяце ', num)
        break
