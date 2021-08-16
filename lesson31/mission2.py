import re

numbers = 'A578BE777 OP233787 K901MH666 CT46599 CYJ2929П777 666AMP666'

civil_cars = re.findall(r'[ABEKMHOPCTYX]\d{3}[ABEKMHOPCTYX]{2}\d{2,3}', numbers)
print('Список номеров частных автомобилей: ', civil_cars)
taxi_cars = re.findall(r'[ABEKMHOPCTYX]{2}\d{4,5}', numbers)
print('Список номеров такси: ', taxi_cars)
