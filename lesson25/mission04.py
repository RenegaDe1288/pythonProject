class Robot:
    def __init__(self, model):
        self.model = model

    def operate(self):
        pass


class Cleaner(Robot):
    count = 0

    def operate(self):
        self.count += 1
        print('Робот {}  пылесосит. Текущая заполненость мешка: {}'.format(self.model, self.count))


class WarRobot(Robot):

    def __init__(self, model):
        super().__init__(model)

    def operate(self):
        print('Робот {}  защищает.'.format(self.model))


class WaterRobot(WarRobot):

    def __init__(self, model, depth):
        super().__init__(model)
        self.depth = depth

    def operate(self):
        super().operate()
        print('Подводный робот {}   атакует под водой на глубине {} метров'.format(self.model, self.depth))

r = Robot("zzzzzz")
r_1 = Cleaner('r2d2')
r_2 = WarRobot('yy6')
r_3 = WaterRobot('QWE3', 4)
r_1.operate()
r_2.operate()
r_3.operate()
r_1.operate()
r.operate()
