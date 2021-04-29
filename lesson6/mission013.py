ways_count = int(input('Введите количество мешков: '))
count = 0
total_weight = 0
n = 0
rest_weight = 0
while count < ways_count:
    bag_weight = int(input('Введите вес мешка: '))
    if bag_weight <= 10:
        total_weight += bag_weight
        print('Сейчас общий вес = ', total_weight)
    else:
        print('Тяжелый мешок')
        rest_weight += bag_weight
        n += 1
    count += 1
print('Общий вес перетащенных', ways_count - n, 'мешков', total_weight, 'кг')
print('Общий вес оставленных', n, 'мешков', rest_weight, 'кг')
