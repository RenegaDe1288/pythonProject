n = 10
sets1 = set([])
sets2 = set([])
count = 0
print(type(sets1))
while len(sets1) != 1 or len(sets2) >= (n-1):
    x = set(input('Введите числа через пробел: ').split())
    answer = input('Введите отдет(Да/Нет)').lower()
    if answer == 'да' and len(sets1) == 0:
        sets1 = x
    elif answer == 'да' :
        sets1 = sets1 & x
        sets2 = sets2 |(sets2-sets1)
    elif answer == 'нет':
        sets2 = sets2 | x
    elif answer == 'помогите':
        print(sets1)
        print(sets2)
        print('Возможные числа', sets1 - sets2)
        break
    else:
        print('Неверный ввод. поробуйте снова')

print('Загаданное Число: ', sets1 - sets2)
