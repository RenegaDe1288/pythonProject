class CanFly:

    def __init__(self, height, speed):
        self.height = height
        self.speed = speed

    def fly_up(self):
        pass

    def fly(self):
        pass

    def land(self):
        self.height = 0
        self.speed = 0

    def __str__(self,height,speed):
        string = f'Высота: {self.height}\tСкорость: {self.speed}'
        return string


class Butterfly(CanFly):
    def __init__(self, height, speed):
        super().__init__(height, speed)
        self.name = 'Бабочка'

    def fly_up(self):
        self.height = 1
        self.__str__()

    def __str__(self):
        string = f'Высота: {self.height}\tСкорость: {self.speed}'
        print( '{} взлетела:\n{}'.format(self.name,string))

    def fly(self):
        self.speed = 0.5
        self.__str__()


class Roket(CanFly):
    def __init__(self, height, speed):
        super().__init__(height, speed)
        self.name = 'Ракета'

    def fly_up(self):
        self.height = 500
        self.speed = 200
        self.__str__()

    def __str__(self):
        string = super().__str__(self.height,self.speed)
        print( '{} взлетела:\n{}'.format(self.name,string))

    def land(self):
        self.height = 0
        self.speed = 0
        self.__str__()
        print('Ракета БАБХНУЛА')

    def bomb(self):
        print('Ракета БАБХНУЛА')


butterfly = Butterfly(0, 0)
roket = Roket(0, 0)
butterfly.fly_up()
butterfly.fly()
roket.fly_up()
roket.fly()
roket.land()
roket.bomb()
