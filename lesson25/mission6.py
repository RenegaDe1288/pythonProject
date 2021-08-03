import random


class House:
    day = 1
    money = 100
    fridge = 50
    cat_eat = 30
    dirt = 0
    spend_moneu = 0

    def dirt_day(self):
        self.dirt += 5

    def __str__(self):
        print(
            '\n\tДенег: {}, Еды: {}, Кошачьей еды: {}, Грязь: {}'.format(self.money, self.fridge, self.cat_eat,
                                                                         self.dirt))


class Person:
    def __init__(self):
        self.hunger = 300
        self.happy = 100

    def eat(self):
        callories = random.randint(0, 30)
        if house.fridge >= callories:
            self.hunger += callories
            house.fridge -= callories
            print(self.name, 'Поел')
        else:
            print('Холодильник пустой')

    def cost(self):
        self.hunger -= 10

    def petting_cat(self):
        self.cost()
        self.happy += 5
        print("Погладил кота")

    def check_person(self):
        if self.hunger <= 0:
            print('Человек {} умер от голода'.format(self.name))
            return False
        elif self.happy <= 0:
            print('Человек {} умер от депрессии'.format(self.name))
            return False
        else:
            return True

    def check_dirt(self):
        if house.dirt > 90:
            self.happy -= 10

    def __str__(self):
        print('\nЖитель {} , Голод {}, Счастье {}'.format(self.name, self.hunger, self.happy))


class Man(Person):
    def __init__(self):
        super().__init__()
        self.name = 'Misha'

    def work(self):
        self.cost()
        house.money += 150
        print('Заработал 150')

    def play(self):
        self.cost()
        self.happy += 20
        print('Поиграл')

    def begin(self):
        self.__str__()
        if self.check_person():
            # answer = int(input('Введите действие: 1 - еда, 2 - деньги, 3, поиграть, 4 - погладить кота  '))
            answer = random.randint(1, 4)
            self.check_dirt()
            if answer == 1:
                self.eat()
            elif answer == 2:
                self.work()
            elif answer == 3:
                self.play()
            elif answer == 4:
                self.petting_cat()
            else:
                print('Ошибка ввода')


class Women(Person):
    fur = 0

    def __init__(self):
        super().__init__()
        self.name = 'Anna'

    def buy_fur(self):
        self.cost()
        if house.money > 350:
            house.money -= 350
            self.happy += 60
            house.spend_moneu += 350
            self.fur += 1
            print('Куплена шуба')
        else:
            print("Денег на шубу не хватило")

    def clear(self):
        self.cost()
        if house.dirt > 0:
            house.dirt = 0
            print("Дом убран")
        else:
            print('Дом и так чист!')

    def buy(self):
        self.cost()
        foodstuff = random.randint(20, 50)
        house.money -= foodstuff
        house.fridge += foodstuff
        house.cat_eat += 10
        house.spend_moneu += foodstuff
        print('Куплена еда')

    def begin(self):
        self.__str__()
        if self.check_person():
            # answer = int(input('\nВведите действие: 1 - еда, 2 - шуба, 3, продукты, 4 - погладить кота, 5 - убраться  '))
            answer = random.randint(1, 6)
            self.check_dirt()
            if answer == 1:
                self.eat()
            elif answer == 2:
                self.buy_fur()
            elif answer == 3:
                self.buy()
            elif answer == 4:
                self.petting_cat()
            elif answer == 5:
                self.clear()


class Cat:
    hunger = 300
    name = 'Vaska'

    def check_hunger(self):
        if self.hunger <= 0:
            print('Кот умер')
            return False
        return True

    def eat(self):
        callories = random.randint(0, 10)
        if house.cat_eat >= 0:
            self.hunger += callories * 2
            house.cat_eat -= callories
            print('Кот поел')
        else:
            print('Кошачьей еды нет')

    def tear_u_wallpaper(self):
        house.dirt += 5
        self.hunger -= 10

    def sleep(self):
        self.hunger -= 10

    def begin(self):
        self.__str__()
        if self.check_hunger():
            # answer = int(input('\nВведите действие: 1 - еда, 2 - обои, 3- спать  '))
            answer = random.randint(1, 4)
            if answer == 1:
                self.eat()
            elif answer == 2:
                self.tear_u_wallpaper()
            elif answer == 3:
                self.sleep()
        self.__str__()


husband = Man()
wife = Women()
cat = Cat()
house = House()

while all([husband.check_person(), wife.check_person()]):
    print('\n\tДень: ', house.day)
    house.__str__()
    husband.begin()
    wife.begin()
    cat.begin()
    house.dirt_day()
    house.day += 1
print('\n\tВсего прожито: {} дней, потрачено денег {} , и куплено шуб {}'.format(house.day, house.spend_moneu, wife.fur))
