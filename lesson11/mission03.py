height = float(input('Введите рост:  '))
weight = float(input('Введите вес: '))
bmi = round(weight / height ** 2, 2)
if bmi < 18.5:
    print('Вы дистрофаню ИМТ = ', bmi)
elif bmi < 25:
    print('Все гудю ИМТ= ', bmi)
elif bmi < 30:
    print('Походу ты жиреешью ИМТ = ', bmi)
elif bmi < 35:
    print('Ты жиробас. ИМТ = ', bmi)
