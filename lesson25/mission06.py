class Unit:

    def __init__(self, name, hitpoints = 100):
        self.__name = name
        self.__hitpoints = hitpoints

    def damage(self, dam):
        self.__hitpoints -= 0

    def get_data(self):
        return self.__name, self.__hitpoints




class Solder(Unit):

    def __init__(self, name, hitpoints):
        super().__init__(name)
        self.hitpoints = hitpoints

    def damage(self, dam):
        self.dam = dam
        self.hitpoints = self.hitpoints - self.dam
        print(self.__str__())

    def __str__(self):
        return ('Солдат {} получил урон {} и тепрь у него {} здоровья'.format(self.get_data()[0], self.dam,
                                                                              self.hitpoints))

class Civil(Unit):

    def __init__(self, name, hitpoints):
        super().__init__(name)
        self.hitpoints = hitpoints

    def damage(self, dam):
        self.hitpoints = self.hitpoints - dam * 2
        print(self.__str__(dam))

    def __str__(self, dam):
        return ("Гражданский {} получил урон {} и тепрь у него {} здоровья".format(self.get_data()[0], dam * 2,
                                                                                   self.hitpoints))
solder = Solder('MadMax', 100)
solder.damage(20)
solder.damage(20)
solder.damage(20)

civil = Civil('Anna', 100)
civil.damage(30)
civil.damage(20)




