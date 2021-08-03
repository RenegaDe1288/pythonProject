def create(element, other, new_element):
    print('При взаимодействии {} и {} создан: {} '.format(element.name, other.name, new_element.name))


class Water:
    name = 'Вода'

    def __add__(self, other):
        if other is wind:
            create(self, other, Storm)
        elif other is fire:
            create(self, other, Steam)
        elif other is earth:
            create(self, other, Mud)
        else:
            return None


class Wind:
    name = 'Воздух'

    def __add__(self, other):
        if other is fire:
            create(self, other, Ligting)
        elif other is earth:
            create(self, other, Dust)
        else:
            return None


class Earth:
    name = 'Земля'

    def __add__(self, other):
        return None


class Fire:
    name = 'Огонь'

    def __add__(self, other):
        if other is earth:
            create(self, other, Lava)
        else:
            return None


class Man:
    name = 'Человек'

    def __add__(self, other):
        if other == earth:
            create(self, other, Grave)
        elif other == wind:
            create(self, other, Plane)
        elif other == fire:
            create(self, other, Ash)
        elif other == water:
            create(self, other, Life)
        else:
            return None


class Storm:
    name = 'Шторм'


class Steam:
    name = 'Пар'


class Mud:
    name = 'Грязь'


class Ligting:
    name = 'Молния'


class Dust:
    name = 'Пыль'


class Lava:
    name = 'Лава'


class Grave:
    name = 'Могила'


class Plane:
    name = 'Самолет'


class Ash:
    name = 'Пепел'


class Life:
    name = 'Жизнь'


water = Water()
wind = Wind()
earth = Earth()
fire = Fire()
man = Man()

list_of_elemets = [water, wind, earth, fire, man]

new_list = [element + n_element for element in list_of_elemets for n_element in list_of_elemets]
