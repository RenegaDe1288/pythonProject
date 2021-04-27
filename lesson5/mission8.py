square = int(input('Введите площадь квартиры: '))
price = int(input('Введите стоимость квартиры: '))
if square >= 100 and price <= 10000000 or square >= 80 and price <= 7000000:
    print('Подходящая квартира')
else:
    print('Квартира не подходит')
