from abc import ABC

class Robot(ABC):

    def __init__(self, name):
        self.name = name

    def get_name(self):
        print('Я Робот: ', self.name)


class CanFly:
    height = 0
    speed = 0

    def fly(self):
        print('Я могу летать')

    def height_on(self):
        self.height += 100
        print('Я взлетел на 100 метров и моя высота: ', self.height)

    def height_down(self):
        self.height -= 100
        print('Я опустился на 100 метров и моя высота: ', self.height)

    def speed_on(self):
        self.speed += 20
        print('Я набрал скорость и теперь она: ', self.speed)


class FlyRobot(Robot, CanFly):

    def __init__(self, name):
        super().__init__(name)

    def operate(self):
        print('Веду разведку с воздуха')


class WarRobot(Robot, CanFly):

    def __init__(self, name):
        super().__init__(name)
        self.gun = 'Rocket Launcher'

    def operate(self):
        print('Защищаю военный объект с воздуха с помощью ', self.gun)


robot_1 = WarRobot('Max')
robot_2 = FlyRobot('Ann')

robot_1.get_name()
robot_1.fly()
robot_1.operate()
robot_1.height_on()
robot_1.speed_on()
robot_1.height_down()
print()
robot_2.get_name()
robot_2.fly()
robot_2.operate()
robot_2.height_on()
robot_2.speed_on()
robot_2.height_down()
