class Family:
    surname = 'Воронины'
    money = 100000
    house = False

    def info(self):
        print('Фамилия: {} \nДеньги: {}\nНаличе дома: {}'.format(self.surname, self.money, self.house))

    def work(self, earn):
        self.money += earn

    def buy_house(self, price, discount):
        if self.money > price - (price * (discount / 100)):
            self.money -= price
            print('Дом куплен!')
            print('Остаток денег: ', self.money)
            self.house = True
        else:
            print('Денег не хватило')


family_1 = Family()
family_1.info()
price = 1000000
while family_1.house is False:
    family_1.work(100000)
    family_1.buy_house(price, 10)
    family_1.info()
