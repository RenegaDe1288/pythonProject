class Property:

    def __init__(self, worth):
        self.name = None
        self.wotrh = worth

    def tax(self, divider):
        self.tax = self.wotrh / divider
        print('Налог на {} равен: {}'.format(self.name, self.tax))
        return self.tax


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.name = 'Аппартаменты'


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.name = 'Машина'


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)
        self.name = 'Дом'


money = int(input('Сколько у Вас денег? '))
price = [1000000, 20000, 90000]
ap = Apartment(price[0])
car = Car(price[1])
house = CountryHouse(price[2])
all_tax = ap.tax(1000) + house.tax(500) + car.tax(200)
print('Общая сумма налогов: ', all_tax)
if all_tax < money:
    print('\nДенег достаточно для оплаты налогов. У вас останется: ', money - all_tax)
else:
    print('\nДенег не хватает на налоги!!! Нужно еще: ', all_tax - money)
