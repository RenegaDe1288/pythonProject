boots = [40, 41, 42, 43, 50, 39]
mens = [42, 41, 42, 41, 39, 45, 40]
count = 0
for i in mens:
    count1 = 0
    for y in boots:
        if i <= y:
            boots.remove(y)
            count += 1
            count1 += 1
            print('Чувак с размером: ', i, ' взял ботинки размером: ', y)
            break
    if count1 == 0:
        print('Чувак с размером', i, 'пролетает!')
    if len(boots) != 0:
        print('остались размеры: ', boots)
    else:
        break
print('Наибольшее кол-во людей, которые могут взять ролики:', count)